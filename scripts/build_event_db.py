#!/usr/bin/env python3
"""데일리 md 전체를 사건 표(vault/_meta/events.csv)로 바꾼다. 표준 라이브러리만 쓴다.

항목 하나가 한 행이다(top5, deepdive, investment, companies, demand). 주제는 vault/topics 의 대표 노트
(status: deprecated 가 아닌 것)를 기준으로 매긴다. 합쳐진 노트의 이름과 aliases 도 매칭 용어로 쓴다.
"""
import argparse, csv, html, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render_html as R  # noqa: E402

ROOT = os.path.dirname(HERE)
FIELDS = ["id", "date", "section", "sector", "title", "summary", "url", "urls",
          "numbers", "topics", "fact_flag"]
SECTIONS = ["top5", "deepdive", "investment", "companies", "demand"]

EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️‍]")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
WIKI_RE = re.compile(r"\[\[[^\]]*\]\]")
URL_RE = re.compile(r"https?://[^\s)\]|]+")
NUM_RES = [
    re.compile(r"[+\-−]?\d[\d,]*(?:\.\d+)?\s?%"),
    re.compile(r"HR\s*~?\d(?:\.\d+)?"),
    re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?\s?(?:조|억|만|[BMK]\b)?"),
    re.compile(r"\d[\d,]*(?:\.\d+)?\s?(?:조|억)(?:[\d,]*(?:\.\d+)?(?:억|만))?(?:원|달러|엔|위안)?"),
]


def plain(s):
    """마크다운, 위키링크, 이모지, HTML 엔티티를 걷어 낸 평문."""
    s = html.unescape(s or "")
    s = WIKI_RE.sub("", s)
    s = LINK_RE.sub(r"\1", s)
    s = s.replace("**", "").replace("`", "")
    s = EMOJI_RE.sub("", s)
    return re.sub(r"\s+", " ", s).strip()


def clip(s, n=240):
    """n자 안쪽으로 단어 경계에서 자른다. 말줄임표는 붙이지 않는다."""
    if len(s) <= n:
        return s
    cut = s[:n]
    # 문장 끝(다. 요. 음.)이 앞쪽 절반 뒤에 있으면 거기서 끊는다. 문장 중간에서 끊기면 읽기 어렵다
    ends = [m.end() for m in re.finditer(r"[다요음]\.(?=\s|$)", cut)]
    if ends and ends[-1] >= n * 0.5:
        return cut[:ends[-1]]
    if s[n] != " " and " " in cut:
        cut = cut[:cut.rfind(" ")]
    return cut.rstrip(" ,.;:")


def extract_numbers(text):
    out = []
    for rx in NUM_RES:
        for m in rx.finditer(text):
            v = m.group(0).strip()
            if v not in out:
                out.append(v)
    return out


# --- 주제 -----------------------------------------------------------------
def _front(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).split("\n"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm


def load_topics(topics_dir):
    """{대표 주제: [매칭 용어]}. 합쳐진 노트의 이름과 aliases 를 대표 주제의 용어로 모은다."""
    notes = {}
    for fn in sorted(os.listdir(topics_dir)):
        if fn.endswith(".md"):
            notes[fn[:-3]] = _front(os.path.join(topics_dir, fn))

    def canon(name, seen=()):
        fm = notes.get(name)
        if fm is None or fm.get("status") != "deprecated" or name in seen:
            return name
        tgt = fm.get("merged_into", "").split("/")[-1]
        return canon(tgt, seen + (name,)) if tgt in notes else None

    topics = {}
    for name, fm in notes.items():
        c = canon(name)
        if c is None or c not in notes or notes[c].get("status") == "deprecated":
            continue
        terms = topics.setdefault(c, [])
        for t in [name] + _aliases(fm):
            if t not in terms:
                terms.append(t)
    return topics


def _aliases(fm):
    v = fm.get("aliases", "").strip("[]")
    return [a.strip().strip("'\"") for a in v.split(",") if a.strip()]


def _norm(s):
    return re.sub(r"[\s\-]+", "", s).lower()


def _term_match(term, text, norm_text):
    t = _norm(term)
    if len(t) < 2:
        return False
    if t.isascii() and len(t) <= 3:
        # 짧은 영문 용어는 단어 경계가 있어야 맞는다. ADCs 같은 복수형은 허용한다.
        return re.search(r"(?<![A-Za-z0-9])%s(?:s)?(?![A-Za-z0-9])" % re.escape(t), text, re.I) is not None
    return t in norm_text


def match_topics(text, topics):
    norm_text = _norm(text)
    return [c for c, terms in topics.items()
            if any(_term_match(t, text, norm_text) for t in terms)]


# --- 행 만들기 -----------------------------------------------------------------
def _row(date, section, idx, sector, title, summary_raw, urls, full_raw, topics):
    title_p = plain(title)
    summary = clip(plain(summary_raw))
    urls = [u for u in dict.fromkeys(urls) if u]
    return {
        "id": "%s-%s-%d" % (date, section, idx), "date": date, "section": section,
        "sector": plain(sector), "title": title_p, "summary": summary,
        "url": urls[0] if urls else "", "urls": "|".join(urls),
        "numbers": "|".join(extract_numbers(title_p + " " + summary)),
        "topics": "|".join(match_topics(title_p + " " + summary, topics)),
        "fact_flag": "unverified" if "본문 확인 필요" in full_raw else "",
    }


def _urls_in(text):
    return [u.rstrip(".,") for u in URL_RE.findall(text or "")]


def rows_from_doc(doc, date, topics):
    rows = []
    for i, it in enumerate(doc["top5"], 1):
        lead = it["lead"][0] if it["lead"] else (it["callouts"][0][1] if it["callouts"] else "")
        full = " ".join([it["title"]] + it["lead"] + [c[1] for c in it["callouts"]])
        rows.append(_row(date, "top5", i, "", it["title"], lead, [u for _, u in it["links"]], full, topics))
    i = 0
    for sector, _badge, items in doc["deepdive"]:
        for it in items:
            i += 1
            full = " ".join([it["title"], it["watch"], it["frame"], it.get("bull") or "", it.get("bear") or ""])
            rows.append(_row(date, "deepdive", i, sector, it["title"], it["watch"],
                             [it["url"]] + [u for _, u in it["sources"]], full, topics))
    for sec in ("investment", "companies", "demand"):
        for i, it in enumerate(doc[sec], 1):
            rows.append(_row(date, sec, i, "", it["title"], it["body"], _urls_in(it["body"]),
                             it["title"] + " " + it["body"], topics))
    order = {s: n for n, s in enumerate(SECTIONS)}
    rows.sort(key=lambda r: order[r["section"]])
    return rows


def rows_from_markdown(md, date, topics):
    return rows_from_doc(R.parse_markdown(md), date, topics)


def write_csv(rows, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=os.path.join(ROOT, "vault"))
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    out = a.out or os.path.join(a.vault, "_meta", "events.csv")
    topics = load_topics(os.path.join(a.vault, "topics"))
    rows, issues = [], 0
    ddir = os.path.join(a.vault, "daily")
    for fn in sorted(os.listdir(ddir)):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", fn)
        if not m:
            continue
        issues += 1
        md = open(os.path.join(ddir, fn), encoding="utf-8").read()
        rows += rows_from_markdown(md, m.group(1), topics)
    write_csv(rows, out)
    sec = Counter(r["section"] for r in rows)
    tc = Counter(t for r in rows for t in r["topics"].split("|") if t)
    print("issues parsed: %d, rows: %d -> %s" % (issues, len(rows), out))
    print("rows per section:", dict(sec))
    print("rows with >=1 topic: %d (%.0f%%)" % (sum(1 for r in rows if r["topics"]),
          100 * sum(1 for r in rows if r["topics"]) / max(len(rows), 1)))
    print("canonical topics: %d, with rows: %d" % (len(topics), len(tc)))
    for t, n in tc.most_common(20):
        print("  %-20s %d" % (t, n))


if __name__ == "__main__":
    main()
