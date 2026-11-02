#!/usr/bin/env python3
"""events.csv 에서 주제 허브 페이지(정적 HTML)를 만든다. 표준 라이브러리만 쓴다.

사람들은 날짜가 아니라 주제를 검색하므로, 주제별로 항목을 시간순으로 모은 엔티티 페이지를 낸다.
"""
import argparse, csv, html, json, os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_event_db import clip  # noqa: E402

ROOT = os.path.dirname(HERE)
SITE = "https://kakyungkim.github.io/econ-radar"
SUBSCRIBE = "https://buttondown.com/kakyungkim"
TELEGRAM = "https://t.me/econradar"
GOATCOUNTER = '<script data-goatcounter="https://kakyungkim.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
DISCLAIMER = "투자 참고용 정보입니다. 판단과 책임은 본인에게 있습니다."
MAX_ITEMS = 150  # 페이지 하나에 싣는 최신 항목 수 상한(수백 건이면 페이지가 무거워진다)

SLUGS = {
    "AI": "ai", "AI인프라": "ai-infra", "AI반도체": "ai-semiconductor", "AI신약": "ai-drug-discovery",
    "AI에이전트": "ai-agent", "AI경쟁구도": "ai-competition", "AI규제": "ai-regulation",
    "SK하이닉스": "sk-hynix", "반도체HBM": "hbm-semiconductor", "한국증시": "korea-equities",
    "FOMC": "fomc", "ADC항체약물접합체": "adc", "GLP-1": "glp-1", "에너지": "energy",
    "한국바이오": "korea-bio", "TSMC": "tsmc", "희귀질환신약": "rare-disease-drugs",
    "삼성바이오로직스": "samsung-biologics", "KRAS": "kras", "ESMO2026": "esmo-2026",
    "HLB": "hlb", "AnthropicIPO": "anthropic-ipo", "거시정책": "macro-policy", "투자테마": "invest-themes",
    "CAR-T": "car-t", "FDA규제": "fda-regulation", "KOSPI반도체": "kospi-semiconductor",
}
# 화면에 보일 이름. 노트 파일명은 링크 호환 때문에 그대로 두고 표시만 바꾼다
DISPLAY = {
    "ADC항체약물접합체": "ADC(항체약물접합체)", "반도체HBM": "HBM과 메모리 반도체", "한국증시": "한국 증시",
    "AI인프라": "AI 인프라", "GLP-1": "GLP-1 비만 치료제", "희귀질환신약": "희귀질환 신약",
    "한국바이오": "한국 바이오", "FOMC": "FOMC와 미국 금리", "KRAS": "KRAS 표적 항암제",
    "AI반도체": "AI 반도체", "AI신약": "AI 신약개발", "에너지": "에너지와 유가",
}
# 주제라기보다 묶음에 가까워 허브로 만들지 않는다(AI는 808건으로 전체의 23%)
GENERIC = {"AI", "투자테마", "거시정책", "거시경제", "바이오제약"}
SECTION_ORDER = {"top5": 0, "deepdive": 1, "investment": 2, "companies": 3, "demand": 4}


def esc(s):
    return html.escape(s or "", quote=True)


def disp(topic):
    return DISPLAY.get(topic, topic)


def slug_for(topic):
    return SLUGS.get(topic) or "topic-%x" % (sum(map(ord, topic)) % 65536)


def read_events(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def select_hubs(rows, n=12, generic_ratio=0.3):
    """행 수 상위 n개 주제. 전체 행의 generic_ratio 를 넘는 주제는 포괄 주제로 보고 뺀다."""
    cnt = Counter(t for r in rows for t in r["topics"].split("|") if t)
    chosen, excluded = [], []
    for t, c in cnt.most_common():
        if t in GENERIC:
            excluded.append((t, c, "포괄 주제(GENERIC 목록)"))
        elif c > generic_ratio * len(rows):
            excluded.append((t, c, "전체 행의 %d%% 초과(포괄 주제)" % (generic_ratio * 100)))
        elif len(chosen) < n:
            chosen.append((t, c))
    return chosen, excluded


def intro_for(topic, topics_dir):
    """대표 노트 '## 핵심 흐름'의 첫 항목들에서 앞 문장 2~3개를 평문으로 뽑는다."""
    p = os.path.join(topics_dir, topic + ".md")
    if not os.path.exists(p):
        return ""
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"^## 핵심 흐름\s*\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    if not m:
        return ""
    bullets = [b[2:].strip() for b in m.group(1).split("\n") if b.startswith("- ")][:2]
    s = " ".join(bullets)
    s = re.sub(r"\[\[[^\]]*\]\]", "", s).replace("**", "").replace("`", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\s+—\s+|\s*—\s*", ", ", s).replace("·", ", ").replace("…", "")
    s = re.sub(r"\s+", " ", s).replace(" ,", ",").replace(":, ", ": ").strip()
    sents = re.split(r"(?<=[가-힣\)])\.\s+", s)
    out = ". ".join(x.rstrip(".") for x in sents[:3]).strip()
    return out + "." if out and not out.endswith(".") else out


def daily_url(date):
    return "%s/%s.html" % (SITE, date)


CSS = """
:root{--ink:#1e293b;--indigo:#4338ca;--deep:#3730a3;--soft:#eef2ff;--line:#c7d2fe;--muted:#64748b}
*{box-sizing:border-box}
body{font-family:'Pretendard',-apple-system,'Noto Sans KR',sans-serif;color:var(--ink);background:#f6f7fb;margin:0;line-height:1.75;font-size:16px;overflow-wrap:anywhere}
.wrap{max-width:760px;margin:0 auto;padding:28px 16px 70px}
a{color:var(--indigo);text-decoration:none}
a:hover{text-decoration:underline}
.back{font-size:14px}
.head{background:linear-gradient(135deg,#4f46e5,#3730a3);color:#eef2ff;border-radius:16px;padding:22px 24px;margin:14px 0 22px}
.head h1{font-size:clamp(20px,5vw,26px);line-height:1.35;margin:0 0 8px;color:#fff}
.head .meta{font-size:14px;color:#c7d2fe}
.intro{background:#fff;border-left:4px solid var(--line);border-radius:0 10px 10px 0;padding:12px 16px;margin:0 0 24px}
h2{font-size:18px;color:var(--indigo);margin:28px 0 8px;padding-bottom:6px;border-bottom:2px solid var(--line)}
ul{list-style:none;margin:0;padding:0}
li{background:#fff;border-radius:10px;padding:11px 14px;margin:8px 0;box-shadow:0 2px 10px rgba(67,56,202,.07)}
.d{font-size:13px;color:var(--muted)}
li .t{font-weight:700;display:block}
li p{margin:4px 0 2px;font-size:14.5px;color:#334155}
.src{font-size:13px}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin:34px 0 14px}
.btn{display:inline-block;padding:10px 18px;border-radius:999px;background:var(--indigo);color:#fff;font-weight:700;font-size:14px}
.btn.alt{background:#fff;color:var(--indigo);border:1.5px solid var(--indigo)}
.btn:hover{text-decoration:none;opacity:.9}
.foot{font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding-top:14px}
@media(max-width:640px){body{font-size:15px}.wrap{padding:18px 14px 56px}.head{padding:18px}}
"""


def head_html(title, desc, canonical, jsonld):
    return (
        '<!DOCTYPE html>\n<html lang="ko"><head><meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>%s</title>\n"
        '<meta name="description" content="%s">\n'
        '<link rel="canonical" href="%s">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:locale" content="ko_KR">\n'
        '<meta property="og:site_name" content="econ-radar">\n'
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        "<style>@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');%s</style>\n"
        '<script type="application/ld+json">%s</script>\n%s\n</head>\n'
        % (esc(title), esc(desc), esc(canonical), esc(title), esc(desc), esc(canonical), CSS,
           json.dumps(jsonld, ensure_ascii=False).replace("<", "\\u003c"), GOATCOUNTER))


def footer_html():
    return ('<div class="cta"><a class="btn" href="%s">메일로 구독하기</a>'
            '<a class="btn alt" href="%s">텔레그램 채널</a></div>\n'
            '<div class="foot">%s</div>\n</div></body></html>\n' % (SUBSCRIBE, TELEGRAM, DISCLAIMER))


def render_hub(topic, slug, rows, intro):
    rows = sorted(rows, key=lambda r: (r["date"], -SECTION_ORDER.get(r["section"], 9)), reverse=True)
    total = len(rows)
    dates = sorted(r["date"] for r in rows)
    shown = rows[:MAX_ITEMS]
    rng = "%s ~ %s · %d건" % (dates[0], dates[-1], total)
    if total > len(shown):
        rng += " (최근 %d건 표시)" % len(shown)
    canonical = "%s/topics/%s.html" % (SITE, slug)
    desc = clip(intro, 150) if intro else "%s 관련 경제 뉴스를 날짜순으로 모은 econ-radar 주제 허브입니다." % disp(topic)
    jsonld = {
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "%s 동향 타임라인" % disp(topic), "url": canonical, "inLanguage": "ko",
        "description": desc, "isPartOf": {"@type": "WebSite", "name": "econ-radar", "url": SITE + "/"},
        "hasPart": {"@type": "ItemList", "numberOfItems": len(shown), "itemListElement": [
            {"@type": "ListItem", "position": i, "name": r["title"], "url": daily_url(r["date"]),
             "datePublished": r["date"]} for i, r in enumerate(shown, 1)]},
    }
    body = ['<body><div class="wrap">\n<a class="back" href="%s/">econ-radar 아카이브</a> / <a class="back" href="index.html">주제 허브</a>' % SITE,
            '<div class="head"><h1>%s: econ-radar 주제 허브</h1><div class="meta">%s</div></div>' % (esc(disp(topic)), esc(rng))]
    if intro:
        body.append('<p class="intro">%s</p>' % esc(intro))
    month = None
    for r in shown:
        mk = r["date"][:7]
        if mk != month:
            if month:
                body.append("</ul>")
            month = mk
            body.append("<h2>%d년 %d월</h2>\n<ul>" % (int(mk[:4]), int(mk[5:7])))
        src = ' <a class="src" href="%s" rel="noopener">출처</a>' % esc(r["url"]) if r["url"] else ""
        summ = clip(r["summary"], 110)
        body.append('<li><span class="d">%s</span><a class="t" href="%s">%s</a>%s%s</li>' % (
            esc(r["date"]), esc(daily_url(r["date"])), esc(r["title"]),
            "<p>%s</p>" % esc(summ) if summ else "", src))
    body.append("</ul>")
    return head_html("%s 동향 타임라인 | econ-radar" % disp(topic), desc, canonical, jsonld) + "\n".join(body) + "\n" + footer_html()


def render_index(hubs):
    """hubs: [(주제명, slug, 건수, 시작일, 종료일)]"""
    canonical = SITE + "/topics/"
    desc = "econ-radar가 매일 쌓은 경제 뉴스를 주제별로 모은 허브 %d곳. 주제마다 날짜순 타임라인과 출처를 제공합니다." % len(hubs)
    jsonld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "econ-radar 주제 허브",
              "url": canonical, "inLanguage": "ko", "hasPart": {"@type": "ItemList", "itemListElement": [
                  {"@type": "ListItem", "position": i, "name": h[0], "url": "%s/topics/%s.html" % (SITE, h[1])}
                  for i, h in enumerate(hubs, 1)]}}
    body = ['<body><div class="wrap">\n<a class="back" href="%s/">econ-radar 아카이브</a>' % SITE,
            '<div class="head"><h1>econ-radar 주제 허브</h1><div class="meta">주제별로 모은 경제, 바이오, AI 동향</div></div>', "<ul>"]
    for name, slug, n, d0, d1 in hubs:
        body.append('<li><a class="t" href="%s.html">%s</a><span class="d">%s ~ %s, %d건</span></li>'
                    % (esc(slug), esc(name), esc(d0), esc(d1), n))
    body.append("</ul>")
    return head_html("주제 허브 | econ-radar", desc, canonical, jsonld) + "\n".join(body) + "\n" + footer_html()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default=os.path.join(ROOT, "vault", "_meta", "events.csv"))
    ap.add_argument("--topics", default=os.path.join(ROOT, "vault", "topics"))
    ap.add_argument("--out", default=os.path.join(ROOT, "out", "topics"))
    ap.add_argument("--n", type=int, default=12)
    a = ap.parse_args()
    rows = read_events(a.events)
    chosen, excluded = select_hubs(rows, a.n)
    os.makedirs(a.out, exist_ok=True)
    by = defaultdict(list)
    for r in rows:
        for t in r["topics"].split("|"):
            if t:
                by[t].append(r)
    hubs = []
    for t, c in chosen:
        slug = slug_for(t)
        ds = sorted(r["date"] for r in by[t])
        with open(os.path.join(a.out, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(render_hub(t, slug, by[t], intro_for(t, a.topics)))
        hubs.append((t, slug, c, ds[0], ds[-1]))
        print("%-14s %-20s %3d건  %s ~ %s" % (t, slug, c, ds[0], ds[-1]))
    with open(os.path.join(a.out, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index(hubs))
    for t, c, why in excluded:
        print("제외: %s (%d건) %s" % (t, c, why))
    print("출력: %s" % a.out)


if __name__ == "__main__":
    main()
