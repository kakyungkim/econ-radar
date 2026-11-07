#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collect_news.py — 신뢰 매체 RSS/Atom 피드에서 뉴스 후보를 모아 vault/raw/feed-DATE.{json,md}로 저장한다.

클라우드 데일리 루틴은 WebSearch/WebFetch에 토큰을 많이 쓰고 샌드박스에서 원문 사이트를 열지 못한다.
수집을 GitHub Actions로 옮기고, 루틴(news-scout)은 이 후보 파일을 읽는다.

사용: python3 scripts/collect_news.py 2026-11-06 [--hours 30] [--max-per-feed 15] [--max-items 120] [--fetch-text 0]
창: DATE 18:00 KST에서 거슬러 --hours 시간. 종료 코드: 0 = 피드 절반 이상 성공, 1 = 미만.
stdlib만 사용. 네트워크는 curl(subprocess)로 받는다(urllib가 일부 호스트에서 시간 초과, FRED류는 브라우저 UA 거부).
"""
import sys, os, re, json, argparse, subprocess, html, time, datetime as dt
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KST = dt.timezone(dt.timedelta(hours=9))
BOT_UA = "Mozilla/5.0 (compatible; econ-radar/1.0)"
BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
SECTIONS = ["macro", "markets", "korea", "bio", "ai", "policy"]
SECTION_LABEL = {"macro": "거시", "markets": "시장", "korea": "국내 경제", "bio": "제약·바이오",
                 "ai": "AI·테크", "policy": "정책·기관"}
FETCH_PRIORITY = {"bio": 0, "ai": 0, "korea": 0}   # 본문 수집 우선 섹션
TRACKING = re.compile(r"^(utm_|fbclid|gclid|mc_|ref$|cmpid|taid|guccounter)", re.I)


# ---------- 파싱 ----------
def _local(tag):
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def _plain(s):
    """HTML 조각을 평문으로. 엔티티 풀고 공백 정리."""
    s = html.unescape(s or "")
    s = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", s, flags=re.S)   # 이중 이스케이프된 CDATA
    s = re.sub(r"</?(?:b|i|em|strong|a|span|u|sup|sub)\b[^>]*>", "", s)   # 인라인 태그는 붙여서
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s) if "&" in s else s
    return re.sub(r"\s+", " ", s).strip()


def _parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)
    except (TypeError, ValueError, IndexError):
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d


def parse_feed(data, name, lang, section):
    """RSS 2.0, RSS 1.0(RDF), Atom을 같은 모양으로. data는 bytes."""
    root = ET.fromstring(data)
    out = []
    for el in root.iter():
        if _local(el.tag) not in ("item", "entry"):
            continue
        f = {}
        for ch in el:
            k = _local(ch.tag)
            if k == "link":
                href = ch.get("href")
                if href and ch.get("rel", "alternate") == "alternate":
                    f["link"] = href
                elif ch.text and ch.text.strip():
                    f.setdefault("link", ch.text.strip())
            elif k in ("title", "pubDate", "published", "updated", "date", "description", "summary", "encoded"):
                f.setdefault(k, ch.text or "")
        url = (f.get("link") or "").strip()
        title = re.sub(r"\s+", " ", _plain(f.get("title"))).strip()
        if not url or not title:
            continue
        pub = _parse_date(f.get("pubDate") or f.get("published") or f.get("updated") or f.get("date"))
        summ = _plain(f.get("description") or f.get("summary") or f.get("encoded"))
        out.append({"title": title, "source": name, "lang": lang, "section": section,
                    "published": pub, "url": url, "summary": summ[:500]})
    return out


# ---------- 필터와 중복 제거 ----------
def filter_window(items, end, hours):
    start = end - dt.timedelta(hours=hours)
    return [i for i in items if i["published"] and start <= i["published"] <= end]


def canonical_url(u):
    p = urlsplit(u.strip())
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not TRACKING.match(k)]
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"), urlencode(q), ""))


def _tkey(t):
    return re.sub(r"\s+", "", t).lower()


def dedupe(items):
    seen_u, seen_t, out = set(), set(), []
    for i in items:
        u, t = canonical_url(i["url"]), _tkey(i["title"])
        if u in seen_u or t in seen_t:
            continue
        seen_u.add(u)
        seen_t.add(t)
        out.append(i)
    return out


def interleave(items):
    """피드별 최신순 목록을 돌아가며 한 건씩 뽑는다. 상한으로 자를 때 특정 매체나 섹션이 몰리지 않게."""
    by = {}
    for i in sorted(items, key=lambda i: -i["published"].timestamp()):
        by.setdefault(i["source"], []).append(i)
    out, k = [], 0
    while any(k < len(v) for v in by.values()):
        out += [v[k] for v in by.values() if k < len(v)]
        k += 1
    return out


def pick_for_fetch(items, n):
    """bio/ai/korea 섹션 먼저, 같은 우선순위 안에서는 최신순."""
    ranked = sorted(items, key=lambda i: (FETCH_PRIORITY.get(i["section"], 1), -i["published"].timestamp()))
    return ranked[:n]


# ---------- 본문 추출 ----------
class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.in_article = 0
        self.in_p = False
        self.buf = []
        self.art, self.all = [], []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "nav", "footer", "header", "aside", "form"):
            self.skip += 1
        elif tag == "article":
            self.in_article += 1
        elif tag == "p" and not self.skip:
            self.in_p, self.buf = True, []

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "nav", "footer", "header", "aside", "form"):
            self.skip = max(0, self.skip - 1)
        elif tag == "article":
            self.in_article = max(0, self.in_article - 1)
        elif tag == "p" and self.in_p:
            self.in_p = False
            t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            if t:
                (self.art if self.in_article else self.all).append(t)

    def handle_data(self, d):
        if self.in_p and not self.skip:
            self.buf.append(d)


def html_to_text(page, limit=1800):
    p = _Text()
    try:
        p.feed(page)
    except Exception:
        pass
    paras = p.art or p.all
    text = "\n".join(t for t in paras if len(t) >= 40)
    return text[:limit]


def text_status(text):
    if not text:
        return "blocked"
    return "short" if len(text) < 300 else "ok"


# ---------- 네트워크 ----------
def curl(url, ua=BOT_UA, timeout=30):
    r = subprocess.run(["curl", "-sfL", "-m", str(timeout), "-A", ua, "--compressed", url],
                       capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"curl {r.returncode}")
    return r.stdout


def fetch_feed(url):
    try:
        return curl(url)
    except RuntimeError:
        return curl(url, BROWSER_UA)   # 일부 사이트는 브라우저 UA에만 응답


def fetch_article(url):
    for ua in (BOT_UA, BROWSER_UA):
        try:
            raw = curl(url, ua, 25)
        except RuntimeError:
            continue
        m = re.search(rb"charset=[\"']?([\w-]+)", raw[:3000], re.I)
        try:
            page = raw.decode(m.group(1).decode() if m else "utf-8", "replace")
        except LookupError:
            page = raw.decode("utf-8", "replace")
        t = html_to_text(page)
        if t:
            return t
    return ""


# ---------- 출력 ----------
def _kst(d):
    return d.astimezone(KST).strftime("%Y-%m-%d %H:%M")


def render_md(date, start, end, stats, items):
    ok = sum(1 for s in stats.values() if not s["error"])
    L = [f"# 뉴스 후보 {date} (Actions 수집)", "",
         f"- 창: {_kst(start)} ~ {_kst(end)} KST",
         f"- 피드 {ok}/{len(stats)}개 성공, 후보 {len(items)}건", "",
         "| 피드 | 받음 | 채택 | 오류 |", "| --- | --- | --- | --- |"]
    for n, s in stats.items():
        L.append(f"| {n} | {s['fetched']} | {s['kept']} | {s['error'] or '-'} |")
    for sec in SECTIONS:
        grp = [i for i in items if i["section"] == sec]
        if not grp:
            continue
        L += ["", f"## {SECTION_LABEL[sec]} ({sec}, {len(grp)}건)"]
        for i in grp:
            L += ["", f"### {i['title']}",
                  f"- ({i['source']}, {_kst(i['published'])} KST, {i['lang']}) {i['url']}"]
            if i.get("summary"):
                L.append(f"- 요약: {i['summary']}")
            if i.get("text"):
                L.append(f"- 본문 발췌 [{i.get('text_status')}]: {i['text'][:600]}")
            elif i.get("text_status") in ("blocked", "short"):
                L.append(f"- 본문: {i['text_status']}")
    return "\n".join(L) + "\n"


# ---------- 실행 ----------
def load_feeds(path):
    out = []
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        p = ln.rstrip("\n").split("\t")
        if len(p) == 4:
            out.append(p)
    return out


# 저장소가 공개라 기사 본문(저작권)은 받지도 저장하지도 않는다(2026-11-08 사용자 결정). RSS 요약까지만 남긴다.
DEFAULT_FETCH_TEXT = 0


def strip_text(d):
    """이미 저장된 페이로드에서 기사 본문 발췌를 지운다. 요약은 남긴다."""
    for i in d.get("items", []):
        i["text"] = ""
        i["text_status"] = "not_fetched"
    return d


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--hours", type=int, default=30)
    ap.add_argument("--max-per-feed", type=int, default=15)
    ap.add_argument("--max-items", type=int, default=120)
    ap.add_argument("--fetch-text", type=int, default=DEFAULT_FETCH_TEXT)
    ap.add_argument("--feeds", default=os.path.join(ROOT, "scripts", "feeds.tsv"))
    a = ap.parse_args(argv)
    t0 = time.time()
    end = dt.datetime.combine(dt.date.fromisoformat(a.date), dt.time(18, 0), tzinfo=KST)
    start = end - dt.timedelta(hours=a.hours)

    stats, items = {}, []
    for name, lang, sec, url in load_feeds(a.feeds):
        st = {"fetched": 0, "kept": 0, "error": ""}
        try:
            got = parse_feed(fetch_feed(url), name, lang, sec)
            st["fetched"] = len(got)
            got = filter_window(got, end, a.hours)
            got.sort(key=lambda i: -i["published"].timestamp())
            got = got[:a.max_per_feed]
            st["kept"] = len(got)
            items += got
        except Exception as e:
            st["error"] = f"{type(e).__name__}: {e}"[:80]
        stats[name] = st
        print(f"[feed] {name}: {st['fetched']} -> {st['kept']} {st['error']}", file=sys.stderr)

    items = dedupe(items)
    items = interleave(items)[:a.max_items]
    items.sort(key=lambda i: -i["published"].timestamp())

    for i in pick_for_fetch(items, a.fetch_text):
        i["text"] = fetch_article(i["url"])
        i["text_status"] = text_status(i["text"])
    for i in items:
        i.setdefault("text", "")
        i.setdefault("text_status", "not_fetched")
    for n, s in stats.items():
        s["kept"] = sum(1 for i in items if i["source"] == n)

    outdir = os.path.join(ROOT, "vault", "raw")
    os.makedirs(outdir, exist_ok=True)
    js = [dict(i, published=_kst(i["published"]) + " KST") for i in items]
    with open(os.path.join(outdir, f"feed-{a.date}.json"), "w", encoding="utf-8") as f:
        json.dump({"date": a.date, "window_start": start.isoformat(), "window_end": end.isoformat(),
                   "feeds": stats, "items": js}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(outdir, f"feed-{a.date}.md"), "w", encoding="utf-8") as f:
        f.write(render_md(a.date, start, end, stats, items))

    ok = sum(1 for s in stats.values() if not s["error"])
    sec_n = {s: sum(1 for i in items if i["section"] == s) for s in SECTIONS}
    ts = {}
    for i in items:
        ts[i["text_status"]] = ts.get(i["text_status"], 0) + 1
    print(f"feeds ok {ok}/{len(stats)}; items {len(items)}; sections {sec_n}; text {ts}; "
          f"{time.time()-t0:.0f}s", file=sys.stderr)
    return 0 if stats and ok * 2 >= len(stats) else 1


if __name__ == "__main__":
    sys.exit(main())
