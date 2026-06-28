#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_weekly.py — 주간 동향 리포트(vault/reports/YYYY-Wnn-동향.md)를 공개용 HTML로 렌더.
stdlib만 사용(자체 마크다운 변환). 데일리 render_html.py와 별도(주간은 보고서 형식).
사용: python scripts/render_weekly.py 2026-W26   [--out-suffix=-test]
출력: vault/html/2026-W26-동향.html
"""
import sys, os, re, html, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "vault", "reports")
HTML_DIR = os.path.join(ROOT, "vault", "html")
BLOG_BASE = "/econ-radar"  # 블로그 내 econ-radar 경로


def map_link(url):
    """vault 내부 링크를 공개 URL로 매핑. /daily/DATE.md→블로그, /topics→링크 해제(텍스트만)."""
    m = re.match(r"^/daily/(\d{4}-\d{2}-\d{2})\.md$", url)
    if m:
        return BLOG_BASE + "/" + m.group(1) + ".html"
    if url.startswith("/topics/") or url.startswith("/_meta/") or url.startswith("/reports/"):
        return None  # 공개 안 된 내부 자산 → 링크 해제
    return url  # http(s) 등 외부 링크는 그대로


def inline(text):
    """인라인 마크다운: 이스케이프 → 링크 → 굵게. 순서 중요."""
    # 1) 링크를 토큰으로 빼두고(텍스트 이스케이프가 url을 깨지 않게)
    links = []
    def stash(m):
        label, url = m.group(1), m.group(2)
        mapped = map_link(url)
        links.append((label, mapped))
        return "\x00%d\x00" % (len(links) - 1)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", stash, text)
    # 2) 나머지 텍스트 이스케이프
    text = html.escape(text, quote=False)
    # 3) 굵게
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # 4) 링크 토큰 복원
    def unstash(m):
        label, url = links[int(m.group(1))]
        label = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html.escape(label, quote=False))
        if url:
            return '<a href="%s">%s</a>' % (html.escape(url), label)
        return label
    return re.sub(r"\x00(\d+)\x00", unstash, text)


def md_to_html(body):
    out, i = [], 0
    lines = body.split("\n")
    n = len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()
        # 헤딩
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1)); out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl))
            i += 1; continue
        # 수평선
        if re.match(r"^(-{3,}|\*{3,})$", s):
            out.append("<hr>"); i += 1; continue
        # 표
        if s.startswith("|"):
            tbl = []
            while i < n and lines[i].strip().startswith("|"):
                tbl.append(lines[i].strip()); i += 1
            cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
            head = cells(tbl[0])
            rows = [cells(r) for r in tbl[2:]] if len(tbl) >= 2 else []
            t = ['<div class="tablewrap"><table>', "<thead><tr>"]
            t += ["<th>%s</th>" % inline(c) for c in head]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t)); continue
        # 블록인용
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf))); continue
        # 목록
        if re.match(r"^[-*]\s+", s):
            buf = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                buf.append(re.sub(r"^[-*]\s+", "", lines[i].strip())); i += 1
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in buf) + "</ul>"); continue
        # 빈 줄
        if not s:
            i += 1; continue
        # 문단(빈 줄 전까지)
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6}\s|>|[-*]\s|\||-{3,}$)", lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))
    return "\n".join(out)


def parse_front(md):
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", md, re.S)
    if not m:
        return fm, md
    for line in m.group(1).split("\n"):
        mm = re.match(r"^(\w[\w_]*):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm, m.group(2)


PAGE = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
:root{{--ink:#1e293b;--indigo:#4338ca;--indigo-deep:#3730a3;--soft:#eef2ff;--line:#c7d2fe;--muted:#64748b;--pop:#c026d3;}}
*{{box-sizing:border-box;}}
body{{font-family:'Pretendard',-apple-system,'Noto Sans KR',sans-serif;color:var(--ink);background:#f6f7fb;margin:0;line-height:1.78;font-size:16px;}}
.wrap{{max-width:780px;margin:0 auto;padding:30px 20px 80px;}}
.head{{background:linear-gradient(135deg,#4f46e5,#3730a3);color:#eef2ff;border-radius:18px;padding:26px 28px;margin-bottom:28px;box-shadow:0 12px 40px rgba(49,46,129,.28);}}
.head .kicker{{font-size:13px;letter-spacing:.08em;color:#c7d2fe;font-weight:700;}}
.head h1{{font-size:25px;margin:8px 0 6px;line-height:1.35;color:#fff;}}
.head .range{{font-size:14px;color:#c7d2fe;}}
.tags{{margin-top:12px;}}
.tags span{{display:inline-block;font-size:12px;background:rgba(255,255,255,.14);color:#e9d5ff;border-radius:999px;padding:2px 11px;margin:3px 4px 0 0;}}
h2{{color:var(--indigo);font-size:21px;margin:34px 0 12px;padding-bottom:8px;line-height:1.4;background:linear-gradient(90deg,var(--indigo) 0,var(--pop) 44px,var(--line) 44px) bottom left/100% 3px no-repeat;}}
h3{{color:var(--indigo-deep);font-size:17px;margin:22px 0 8px;}}
p{{margin:10px 0;}}
strong{{color:var(--indigo-deep);}}
a{{color:var(--indigo);text-decoration:none;border-bottom:1px solid var(--line);}}
a:hover{{background:var(--soft);}}
ul{{margin:10px 0;padding-left:20px;}} li{{margin:7px 0;}}
blockquote{{border-left:4px solid var(--line);background:#fff;margin:12px 0;padding:10px 16px;border-radius:0 10px 10px 0;color:var(--muted);font-size:14px;}}
blockquote a{{border:none;color:var(--muted);}}
.tablewrap{{overflow-x:auto;margin:14px 0;-webkit-overflow-scrolling:touch;}}
table{{border-collapse:collapse;width:100%;font-size:14px;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 18px rgba(67,56,202,.08);}}
th{{background:linear-gradient(90deg,var(--indigo),#6d28d9);color:#fff;text-align:left;padding:11px 13px;font-weight:700;}}
td{{padding:10px 13px;border-bottom:1px solid #eef0f7;vertical-align:top;}}
tr:nth-child(even) td{{background:#fafbff;}}
hr{{border:none;border-top:1px solid var(--line);margin:26px 0;}}
.back{{display:inline-block;margin-bottom:18px;font-size:14px;color:var(--indigo);border:none;}}
.foot{{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--muted);}}
@media(max-width:640px){{body{{font-size:15px;}}.wrap{{padding:18px 14px 60px;}}.head{{padding:20px;}}.head h1{{font-size:21px;}}h2{{font-size:19px;}}table{{font-size:13px;}}}}
</style></head>
<body><div class="wrap">
<a class="back" href="{blog}/">← econ-radar 아카이브</a>
<div class="head"><div class="kicker">WEEKLY · 주간 동향</div><h1>{h1}</h1><div class="range">{range}</div>{tags}</div>
{body}
<div class="foot">econ-radar 주간 동향 · 매일의 분석을 한 주 흐름으로 엮은 리포트. 투자·기업 언급은 정보·시나리오이며 매수·매도 권유가 아닙니다.</div>
</div></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("period", help="예: 2026-W26")
    ap.add_argument("--out-suffix", default="")
    args = ap.parse_args()
    if not re.match(r"^\d{4}-W\d{2}$", args.period):
        sys.stderr.write("형식: YYYY-Wnn (예 2026-W26)\n"); sys.exit(2)
    src = os.path.join(REPORTS, args.period + "-동향.md")
    if not os.path.isfile(src):
        sys.stderr.write("입력 없음: %s\n" % src); sys.exit(1)
    fm, body = parse_front(open(src, encoding="utf-8").read())
    # 본문 첫 H1은 헤더로 빼고 본문에선 제거
    h1m = re.search(r"^#\s+(.*)$", body, re.M)
    h1 = h1m.group(1) if h1m else (args.period + " 동향")
    if h1m:
        body = body[:h1m.start()] + body[h1m.end():]
    tags_html = ""
    if fm.get("tags"):
        ts = re.findall(r"[\w가-힣A-Za-z0-9.\-]+", fm["tags"])
        tags_html = '<div class="tags">' + "".join("<span>#%s</span>" % t for t in ts) + "</div>"
    page = PAGE.format(
        title=html.escape(h1), h1=inline(h1), blog=BLOG_BASE,
        range=html.escape(fm.get("date_range", "")), tags=tags_html,
        body=md_to_html(body))
    os.makedirs(HTML_DIR, exist_ok=True)
    out = os.path.join(HTML_DIR, args.period + "-동향" + args.out_suffix + ".html")
    open(out, "w", encoding="utf-8").write(page)
    sys.stderr.write("[render_weekly] 완료: %s (%d bytes)\n" % (out, len(page.encode("utf-8"))))


if __name__ == "__main__":
    main()
