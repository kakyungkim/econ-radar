#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collect_news.py — 프로토타입: 신뢰 경제지 RSS를 코드로 수집·중복제거·저장.
stdlib만 사용(urllib + xml.etree). news-scout 앞단에 붙일 '수집 레이어'.
"""
import sys, os, re, json, hashlib, time
import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

KST = timezone(timedelta(hours=9))
STORE = sys.argv[1] if len(sys.argv) > 1 else "./_store"
SEEN_FILE = os.path.join(STORE, "seen-hashes.txt")
FRESH_HOURS = 24                       # [D 가드①] 48h→24h: RSS가 며칠치를 담아 재탕 유발 → 좁힘
REPO = "/Users/kkkim/projects/econ-radar"
PUBLISHED_DAYS = 4                      # [D 가드②] 최근 N일 발행본의 URL을 읽어 이미 다룬 기사 제외

# 프로토타입 소스(RSS 있는 신뢰 매체 위주). lens: Macro/Bio/AI/Market
SOURCES = [
    {"name": "연합뉴스 경제", "url": "https://www.yna.co.kr/rss/economy.xml", "lens": "Macro"},
    {"name": "한국경제",     "url": "https://www.hankyung.com/feed/economy",  "lens": "Macro"},
    {"name": "전자신문",     "url": "https://rss.etnews.com/Section901.xml",  "lens": "AI"},
    {"name": "STAT News",    "url": "https://www.statnews.com/feed/",         "lens": "Bio"},
    {"name": "TechCrunch",   "url": "https://techcrunch.com/feed/",           "lens": "AI"},
    {"name": "FierceBiotech","url": "https://www.fiercebiotech.com/rss/xml",  "lens": "Bio"},
    {"name": "FiercePharma", "url": "https://www.fiercepharma.com/rss/xml",   "lens": "Bio"},
    {"name": "Endpoints",    "url": "https://endpts.com/feed/",               "lens": "Bio"},  # best-effort(Cloudflare)
]


def norm_title(t):
    return re.sub(r"[^0-9a-z가-힣]", "", (t or "").lower())


def art_hash(title, link):
    return hashlib.sha1((norm_title(title) + "|" + (link or "")).encode("utf-8")).hexdigest()[:16]


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def parse_dt(s):
    if not s:
        return None
    try:
        return parsedate_to_datetime(s)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S"):
        try:
            d = datetime.strptime(s.strip(), fmt)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except Exception:
            pass
    return None


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 econ-radar-collector/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _alltext(el):
    # 중첩 태그(<title><a>…</a></title>)까지 텍스트를 모은다
    return strip_html("".join(el.itertext())).strip()


def parse_feed(data):
    items = []
    root = ET.fromstring(data)
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        d = {}
        for ch in el:
            t = ch.tag.split("}")[-1]
            if t == "title" and not d.get("title"):
                d["title"] = _alltext(ch)
            elif t == "link":
                href = ch.get("href")
                d["link"] = href if href else (_alltext(ch) or d.get("link", ""))
            elif t in ("pubDate", "published", "updated", "date") and not d.get("date"):
                d["date"] = (ch.text or "").strip()
            elif t in ("description", "summary", "content") and not d.get("summary"):
                d["summary"] = _alltext(ch)[:300]
        if d.get("title"):
            items.append(d)
    return items


def load_published_urls():
    # [D 가드②] 최근 발행본(raw·daily)에서 이미 쓴 기사 URL을 모아 재탕 차단
    import glob
    urls = set()
    today = datetime.now(KST).date()
    pats = []
    for n in range(1, PUBLISHED_DAYS + 1):
        d = (today - timedelta(days=n)).strftime("%Y-%m-%d")
        pats += [os.path.join(REPO, "vault", "raw", "news-%s.md" % d),
                 os.path.join(REPO, "vault", "daily", "%s.md" % d)]
    for p in pats:
        for fp in glob.glob(p):
            try:
                txt = open(fp, encoding="utf-8").read()
            except Exception:
                continue
            for u in re.findall(r"https?://[^\s)\]]+", txt):
                urls.add(u.rstrip(".,)").strip())
    return urls


def main():
    os.makedirs(STORE, exist_ok=True)
    seen = set()
    if os.path.exists(SEEN_FILE):
        seen = set(open(SEEN_FILE, encoding="utf-8").read().split())
    published = load_published_urls()

    now = datetime.now(timezone.utc)
    fresh_cut = now - timedelta(hours=FRESH_HOURS)
    today = datetime.now(KST).strftime("%Y-%m-%d")
    out_path = os.path.join(STORE, "news-%s.jsonl" % today)

    rows, stats = [], []
    dup_exact = dup_seen = stale = dup_pub = 0
    batch_hashes = set()

    for s in SOURCES:
        t0 = time.time()
        n_raw = n_keep = 0
        err = ""
        try:
            data = fetch(s["url"])
            items = parse_feed(data)
            n_raw = len(items)
            for it in items:
                link = it.get("link", "")
                if link.startswith("/"):  # 상대 링크 보정
                    link = urllib.parse.urljoin(s["url"], link)
                h = art_hash(it.get("title", ""), link)
                dt = parse_dt(it.get("date"))
                if h in batch_hashes:
                    dup_exact += 1; continue
                batch_hashes.add(h)
                if h in seen:
                    dup_seen += 1; continue
                if link.rstrip(".,)").strip() in published:   # [D 가드②] 이미 발행한 기사
                    dup_pub += 1; continue
                if dt and dt < fresh_cut:
                    stale += 1; continue
                rows.append({"hash": h, "source": s["name"], "lens": s["lens"],
                             "title": it.get("title", ""), "link": link,
                             "published": (dt.astimezone(KST).strftime("%Y-%m-%d %H:%M") if dt else ""),
                             "summary": it.get("summary", "")})
                n_keep += 1
        except urllib.error.HTTPError as e:
            err = "HTTP %s" % e.code
        except Exception as e:
            err = type(e).__name__
        stats.append((s["name"], n_raw, n_keep, round(time.time() - t0, 1), err))

    # 저장 + seen 갱신
    with open(out_path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(SEEN_FILE, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(r["hash"] + "\n")

    # 리포트
    print("=== 수집 결과 (%s, 최근 %dh, 의존성: stdlib만) ===" % (today, FRESH_HOURS))
    print("%-14s %6s %6s %6s  %s" % ("소스", "원본", "채택", "초", "비고"))
    for name, raw, keep, sec, err in stats:
        print("%-14s %6d %6d %6.1f  %s" % (name, raw, keep, sec, err or "ok"))
    print("-" * 48)
    print("채택(신규·신선): %d건 | 정확중복: %d | seen: %d | 이미 발행(URL): %d | 오래됨(>%dh): %d"
          % (len(rows), dup_exact, dup_seen, dup_pub, FRESH_HOURS, stale))
    print("발행이력 URL %d개 로드(최근 %d일 raw·daily)" % (len(published), PUBLISHED_DAYS))
    by_lens = {}
    for r in rows:
        by_lens[r["lens"]] = by_lens.get(r["lens"], 0) + 1
    print("렌즈별:", ", ".join("%s %d" % (k, v) for k, v in sorted(by_lens.items())))
    print("저장: %s" % out_path)
    print("\n=== 샘플 헤드라인(최대 10) ===")
    for r in rows[:10]:
        print(" [%s/%s] %s" % (r["lens"], r["source"], r["title"][:70]))


if __name__ == "__main__":
    main()
