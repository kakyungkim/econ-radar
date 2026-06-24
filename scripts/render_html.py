#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_html.py — econ-radar 일일 뉴스레터 결정적 렌더러

입력 : vault/daily/YYYY-MM-DD.md   (newsletter-editor 산출물, NEWSLETTER-FORMAT.md 계약 준수)
출력 : vault/html/YYYY-MM-DD.html  (단일 HTML 시각 리포트, 2026-06-12 양식)
       vault/push/YYYY-MM-DD.md    (메신저용 짧은 푸시 메시지)

사용 : python3 scripts/render_html.py 2026-06-11
       python3 scripts/render_html.py 2026-06-11 --out-suffix .test   # 기존 파일 보존

외부 의존성 없음(Python 3 표준 라이브러리만). LLM 토큰 0.
양식(HTML 뼈대·CSS·JS)은 scripts/template.html 에 고정돼 있다.
"""

import sys
import os
import re
import base64
import argparse

# ----------------------------------------------------------------------------
# 경로
# ----------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
TEMPLATE = os.path.join(SCRIPT_DIR, "template.html")
DAILY_DIR = os.path.join(ROOT, "vault", "daily")
HTML_DIR = os.path.join(ROOT, "vault", "html")
PUSH_DIR = os.path.join(ROOT, "vault", "push")
EMAIL_DIR = os.path.join(ROOT, "vault", "email")
HERO_IMG = os.path.join(ROOT, "vault", "assets", "econ-radar_logo-concept-16vs9.jpg")
BLOG_BASE = "https://kakyungkim.github.io/econ-radar"

# ----------------------------------------------------------------------------
# 배지 매핑
# ----------------------------------------------------------------------------
BADGE_CLASS = {
    "Macro": "badge-macro",
    "AI": "badge-ai",
    "Bio": "badge-bio",
    "Market": "badge-market",
    "Semiconductor": "badge-ai",
    "Infrastructure": "badge-ai",
    "mRNA": "badge-bio",
    "K-Bio": "badge-bio",
    "ADC": "badge-bio",
    "Company": "badge-company",
}
# 위키링크(topics/*) → 배지
TOPIC_BADGE = {
    "거시정책": "Macro",
    "AI": "AI",
    "반도체": "Semiconductor",
    "바이오제약": "Bio",
    "신약개발전략": "Bio",
    "유망기업": "Market",
}
# Deep Dive 서브섹션 → (영문 헤더, 배지)
DEEPDIVE_SUBS = {
    "Macro & Policy": ("Macro &amp; Policy", "Macro"),
    "AI & Infrastructure": ("AI &amp; Infrastructure", "AI"),
    "Bio & Pharma": ("Bio &amp; Pharma", "Bio"),
}
# 키워드 → 배지(Today's Topic·Demand·Investment·Companies 의 배지 추론용)
KEYWORD_BADGES = [
    ("mRNA", "mRNA"),
    ("ADC", "ADC"),
    ("K-바이오", "K-Bio"),
    ("반도체", "Semiconductor"),
    ("HBM", "Semiconductor"),
    ("바이오|항체|임상|FDA|담도암|희귀의약품|약가|환자|처방|신약|종양|백신", "Bio"),
    ("AI|GPU|모델|클라우드|데이터센터|오픈AI|엔비디아|capex|인프라", "AI"),
    ("CPI|금리|연준|FOMC|ECB|환율|인플레|긴축|유가", "Macro"),
    ("코스피|KOSPI|증시|투자|주가|밸류", "Market"),
]

POST_DEEPDIVE_SECTIONS = {
    "🙋 Demand", "💰 Investment", "🚀 Companies to Watch",
    "Threads to Follow", "Sources",
}

# ----------------------------------------------------------------------------
# 유틸: 인라인 마크다운 → HTML
# ----------------------------------------------------------------------------
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\s*\[\[[^\]]+\]\]\s*")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _bold(s):
    # s 는 이미 escape 된 문자열
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)


def inline(text, link_class="underline text-indigo-700 ml-1"):
    """[t](u) → <a>, **b** → <strong>, [[wikilink]] 제거."""
    text = WIKILINK_RE.sub(" ", text)
    out = []
    pos = 0
    for m in LINK_RE.finditer(text):
        out.append(_bold(esc(text[pos:m.start()])))
        url = m.group(2)  # URL 의 & 는 보존(공식본과 동일)
        out.append(
            '<a href="%s" class="%s" target="_blank">%s</a>'
            % (url, link_class, esc(m.group(1)))
        )
        pos = m.end()
    out.append(_bold(esc(text[pos:])))
    return "".join(out).strip()


def extract_links(text):
    """텍스트에서 [name](url) 목록을 추출."""
    return [(m.group(1), m.group(2)) for m in LINK_RE.finditer(text)]


def extract_topic_badges(text):
    """[[topics/거시정책]] 등에서 배지 목록을 순서·중복 제거로 추출."""
    badges = []
    for m in re.finditer(r"\[\[topics/([^\]]+)\]\]", text):
        b = TOPIC_BADGE.get(m.group(1).strip())
        if b and b not in badges:
            badges.append(b)
    return badges


def infer_badges(text, limit=2):
    """키워드로 배지를 추론(위키링크가 없는 섹션용)."""
    badges = []
    for pat, b in KEYWORD_BADGES:
        if b in badges:
            continue
        if re.search(pat, text):
            badges.append(b)
        if len(badges) >= limit:
            break
    return badges or ["Market"]


def badge_html(name, sub=False):
    cls = BADGE_CLASS.get(name, "badge-macro")
    if sub:
        return ('<span class="sum-badge %s text-xs font-semibold px-2 py-1 '
                'rounded-full flex-shrink-0">%s</span>') % (cls, name)
    return ('<span class="%s text-xs font-semibold px-2.5 py-1 rounded-full">%s</span>'
            % (cls, name))


def badges_row(names):
    spans = "\n            ".join(badge_html(n) for n in names)
    return ('          <div class="flex flex-wrap gap-2 mb-3">\n            %s\n          </div>'
            % spans)


def source_links_row(links, cls="text-indigo-600 hover:underline"):
    """카드 하단 출처 링크 한 줄."""
    if not links:
        return ""
    a = "\n            ".join(
        '<a href="%s" class="%s" target="_blank">%s</a>' % (u, cls, esc(n))
        for n, u in links
    )
    return ('          <div class="mt-3 flex flex-wrap gap-x-3 gap-y-1 text-sm">\n            %s\n          </div>'
            % a)


# ----------------------------------------------------------------------------
# 마크다운 파서
# ----------------------------------------------------------------------------
def warn(msg):
    sys.stderr.write("[render_html] 경고: %s\n" % msg)


def parse_markdown(md):
    """뉴스레터 md 를 구조화된 dict 로 파싱."""
    lines = md.split("\n")
    doc = {
        "date": None,
        "title": None,
        "subtitle": None,
        "glance": [],
        "top5": [],
        "topic": None,
        "english": [],
        "deepdive": [],   # [(eng_heading, badge, [items])]
        "demand": [],
        "investment": [],
        "companies": [],
        "threads": [],
        "sources": [],    # [(category, [(name,url)])]
    }

    # --- frontmatter ---
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            m = re.match(r"^date:\s*(.+)$", lines[i])
            if m:
                doc["date"] = m.group(1).strip()
            i += 1
        i += 1  # 닫는 ---

    body = lines[i:]

    # --- 섹션 분할(## / # 헤더 기준) ---
    # 먼저 제목/부제/At a Glance 를 본문 앞부분에서 처리
    n = len(body)
    j = 0
    in_deepdive = False
    current_dd = None  # (eng_heading, badge, items)

    while j < n:
        line = body[j]
        s = line.strip()

        # H1 제목
        m = re.match(r"^#\s+(.+)$", line)
        if m and not line.startswith("##"):
            h = m.group(1).strip()
            if h.startswith("econ-radar"):
                doc["title"] = h
                mm = re.search(r"(\d{4}-\d{2}-\d{2})", h)
                if mm and not doc["date"]:
                    doc["date"] = mm.group(1)
                j += 1
                continue
            if h == "Deep Dive":
                in_deepdive = True
                j += 1
                continue

        # 부제 (> ...) — At a Glance 앞 첫 인용
        if s.startswith(">") and doc["subtitle"] is None and not doc["glance"]:
            doc["subtitle"] = s.lstrip("> ").strip()
            j += 1
            continue

        # At a Glance
        if s == "**At a Glance**":
            j += 1
            while j < n and body[j].strip() not in ("---", "") :
                doc["glance"].append(body[j].strip())
                j += 1
            continue

        # H2 섹션
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            head = m.group(1).strip()
            if head == "Today's Top 5":
                j = _parse_top5(body, j + 1, doc)
                continue
            if head.startswith("🗣 Today's Topic"):
                j = _parse_topic(body, j, doc, head)
                continue
            if head.startswith("🗽 Business English"):
                j = _parse_english(body, j + 1, doc)
                continue
            if head in DEEPDIVE_SUBS:
                eng, badge = DEEPDIVE_SUBS[head]
                current_dd = (eng, badge, [])
                doc["deepdive"].append(current_dd)
                j = _parse_deepdive_sub(body, j + 1, current_dd[2])
                continue
            if head.startswith("🙋 Demand"):
                j = _parse_bullets_cards(body, j + 1, doc["demand"])
                continue
            if head.startswith("💰 Investment"):
                j = _parse_investment(body, j + 1, doc["investment"])
                continue
            if head.startswith("🚀 Companies to Watch"):
                j = _parse_bullets_cards(body, j + 1, doc["companies"])
                continue
            if head == "Threads to Follow":
                j = _parse_threads(body, j + 1, doc["threads"])
                continue
            if head == "Sources":
                j = _parse_sources(body, j + 1, doc["sources"])
                continue
            # 알 수 없는 섹션 → 건너뜀
            j += 1
            continue

        j += 1

    return doc


def _is_known_section(head):
    return (head in DEEPDIVE_SUBS or head in POST_DEEPDIVE_SECTIONS
            or head == "Today's Top 5" or head.startswith("🗣")
            or head.startswith("🗽"))


# --- Top 5 ---
def _parse_top5(body, j, doc):
    n = len(body)
    item = None
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        m = re.match(r"^###\s+\d+\.\s+(.+)$", line)
        if m:
            item = {"title": m.group(1).strip(), "lead": [], "callouts": [],
                    "links": [], "badges": []}
            doc["top5"].append(item)
            j += 1
            continue
        if item is None:
            j += 1
            continue
        # 출처
        m = re.match(r"^출처:\s*(.+)$", s)
        if m:
            item["links"] = extract_links(m.group(1))
            item["badges"] = extract_topic_badges(m.group(1)) or infer_badges(
                item["title"])
            j += 1
            continue
        # 콜아웃
        c = _match_callout(s)
        if c:
            item["callouts"].append(c)
            j += 1
            continue
        if s == "---" or s == "":
            j += 1
            continue
        # 리드 문단
        item["lead"].append(s)
        j += 1
    return j


def _match_callout(s):
    m = re.match(r"^\*\*Key Point\*\*:\s*(.+)$", s)
    if m:
        return ("KEY POINT", m.group(1).strip())
    m = re.match(r"^🙋\s*\*\*Demand\*\*:\s*(.+)$", s)
    if m:
        return ("DEMAND", m.group(1).strip())
    m = re.match(r"^💡\s*\*\*Insight\*\*:\s*(.+)$", s)
    if m:
        return ("INSIGHT", m.group(1).strip())
    return None


# --- Today's Topic ---
def _parse_topic(body, j, doc, head):
    n = len(body)
    title = head.split("—", 1)[1].strip() if "—" in head else head
    topic = {"title": title, "paras": [], "summary": None, "links": [],
             "badges": []}
    doc["topic"] = topic
    j += 1
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line) or re.match(r"^#\s+\w", line):
            break
        m = re.match(r"^-\s*💬\s*한 줄 요약:\s*(.+)$", s)
        if m:
            topic["summary"] = m.group(1).strip()
            j += 1
            continue
        m = re.match(r"^-\s*블로그 소재:", s)
        if m:
            j += 1
            continue
        m = re.match(r"^-\s*출처:\s*(.+)$", s)
        if m:
            topic["links"] = extract_links(m.group(1))
            j += 1
            continue
        if s == "---" or s == "":
            j += 1
            continue
        topic["paras"].append(s)
        j += 1
    topic["badges"] = infer_badges(title + " " + " ".join(topic["paras"]))
    return j


# --- Business English ---
def _parse_english(body, j, doc):
    n = len(body)
    cur = None
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##?\s+", line):
            break
        m = re.match(r"^-\s+\*\*(.+?)\*\*:\s*(.*)$", s)
        if m:
            head = m.group(1).strip()
            desc = m.group(2).strip()
            word, meaning, speak = _split_english_head(head)
            cur = {"word": word, "meaning": meaning, "speak": speak,
                   "desc": desc, "en": None, "ko": None}
            doc["english"].append(cur)
            j += 1
            continue
        m = re.match(r"^-\s*📝\s*\*(.+?)\*\s*→\s*(.+)$", s)
        if m and cur is not None:
            cur["en"] = m.group(1).strip().strip('"“”')
            cur["ko"] = m.group(2).strip()
            j += 1
            continue
        j += 1
    return j


def _split_english_head(head):
    """'long-acting antibody (half-life extended antibody, 장기지속형 항체)' →
       word='long-acting antibody', meaning='장기지속형 항체', speak='long-acting antibody'.
       발음은 항상 화면에 보이는 표제어(word)를 읽는다. 괄호 안 영어 설명·약자
       풀이를 읽으면 화면 단어와 안 맞으므로(예: 약자는 철자 그대로 읽힘) 쓰지 않는다."""
    m = re.match(r"^(.+?)\s*\((.+)\)\s*$", head)
    if not m:
        return head, "", head
    word = m.group(1).strip()
    inside = [p.strip() for p in m.group(2).split(",")]
    meaning = inside[-1] if inside else ""
    speak = word  # 표제어를 그대로 발음 — 화면 단어와 항상 일치
    return word, meaning, speak


# --- Deep Dive 서브섹션 ---
def _parse_deepdive_sub(body, j, items):
    n = len(body)
    item = None
    field = None
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line) or (re.match(r"^#\s+\w", line)):
            break
        m = re.match(r"^###\s+\[(.+?)\]\((.+?)\)\s*$", s)
        if m:
            item = {"title": m.group(1).strip(), "url": m.group(2).strip(),
                    "watch": "", "sources": [], "bull": None, "bear": None,
                    "frame": "", "demand": []}
            items.append(item)
            field = None
            j += 1
            continue
        if item is None:
            j += 1
            continue
        m = re.match(r"^\*\*관전 포인트\*\*:\s*(.+)$", s)
        if m:
            item["watch"] = m.group(1).strip()
            field = "watch"
            j += 1
            continue
        m = re.match(r"^\*\*1차 자료\*\*:\s*(.+)$", s)
        if m:
            item["sources"] = extract_links(m.group(1))
            field = None
            j += 1
            continue
        if re.match(r"^\*\*강세 vs 약세\*\*:", s):
            field = "bullbear"
            j += 1
            continue
        m = re.match(r"^\*\*전략 프레임\*\*:\s*(.+)$", s)
        if m:
            item["frame"] = m.group(1).strip()
            field = "frame"
            j += 1
            continue
        if re.match(r"^\*\*Demand[^\*]*\*\*:", s):
            field = "demand"
            j += 1
            continue
        # bull/bear 불릿
        m = re.match(r"^-\s*강세[^:]*:\s*(.+)$", s)
        if m and field == "bullbear":
            item["bull"] = m.group(1).strip()
            j += 1
            continue
        m = re.match(r"^-\s*약세[^:]*:\s*(.+)$", s)
        if m and field == "bullbear":
            item["bear"] = m.group(1).strip()
            j += 1
            continue
        # demand 불릿
        m = re.match(r"^-\s*\*\*(.+?)\*\*:\s*(.+)$", s)
        if m and field == "demand":
            item["demand"].append((m.group(1).strip(), m.group(2).strip()))
            j += 1
            continue
        j += 1
    return j


# --- Demand / Companies (간단 불릿 카드) ---
def _parse_bullets_cards(body, j, out):
    n = len(body)
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##?\s+", line):
            break
        m = re.match(r"^-\s+\*\*(.+?)\*\*:\s*(.+)$", s)
        if m:
            out.append({"title": m.group(1).strip(), "body": m.group(2).strip()})
        j += 1
    return j


# --- Investment ---
def _parse_investment(body, j, out):
    n = len(body)
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        m = re.match(r"^-\s+\*\*(.+?)\*\*:\s*(.+)$", s)
        if m:
            out.append({"title": m.group(1).strip(), "body": m.group(2).strip()})
        j += 1
    return j


# --- Threads ---
def _parse_threads(body, j, out):
    n = len(body)
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        m = re.match(r"^-\s+(.+)$", s)
        if m:
            content = m.group(1).strip()
            badges = extract_topic_badges(content)
            text = WIKILINK_RE.sub("", content)
            text = re.sub(r"^[\s—-]+", "", text).strip()
            out.append({"badges": badges or infer_badges(text, 1), "text": text})
        j += 1
    return j


# --- Sources ---
def _parse_sources(body, j, out):
    n = len(body)
    cur = None
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        m = re.match(r"^\*\*(.+?)\*\*\s*$", s)
        if m:
            cur = (m.group(1).strip(), [])
            out.append(cur)
            j += 1
            continue
        m = re.match(r"^-\s+(.+)$", s)
        if m and cur is not None:
            cur[1].extend(extract_links(m.group(1)))
        j += 1
    return j


# ----------------------------------------------------------------------------
# 발음 SVG (Business English)
# ----------------------------------------------------------------------------
VOICE_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" '
    'height="24" role="img" aria-label="발음 듣기">\n'
    '  <path fill="#0d9488" d="M11.4 4.18A1 1 0 0 1 13 5v14a1 1 0 0 1-1.6.8L6.66 16H4a1.6 1.6 0 0 1-1.6-1.6V9.6A1.6 1.6 0 0 1 4 8h2.66l4.74-3.82z"/>\n'
    '  <path fill="none" stroke="#0d9488" stroke-width="1.9" stroke-linecap="round" d="M16.2 9.1a4.2 4.2 0 0 1 0 5.8"/>\n'
    '  <path fill="none" stroke="#0d9488" stroke-width="1.9" stroke-linecap="round" d="M18.7 6.6a7.7 7.7 0 0 1 0 10.8"/>\n'
    '</svg>'
)
PLAY_SVG = '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M5 3.5l7 4.5-7 4.5V3.5z"/></svg>'


def js_str(s):
    """JS onclick 문자열 인자용 escape."""
    return s.replace("\\", "\\\\").replace("'", "\\'").replace('"', "")


# ----------------------------------------------------------------------------
# 섹션별 렌더
# ----------------------------------------------------------------------------
def render_header(doc, hero_b64):
    date = doc["date"] or ""
    subtitle = esc(doc["subtitle"] or "")
    return """    <!-- ===== HEADER ===== -->
    <header class="mb-8">
      <img
        src="data:image/jpeg;base64,{hero}"
        alt="econ-radar concept"
        class="w-full rounded-2xl shadow-md mb-6"
        style="max-height:260px; object-fit:cover;"
      >
      <div class="flex flex-wrap items-center gap-3 mb-2">
        <span class="text-2xl font-bold tracking-tight text-gray-900">📈 econ-radar 데일리</span>
        <span class="text-lg text-gray-500 font-medium">{date}</span>
      </div>
      <p class="text-sm text-gray-500 mt-1">{subtitle}</p>
      <p class="text-xs text-gray-400 mt-1">TailwindCSS CDN 사용 — 오프라인 환경에서는 스타일이 제한될 수 있습니다.</p>
    </header>""".format(hero=hero_b64, date=esc(date), subtitle=subtitle)


def render_glance(doc):
    if not doc["glance"]:
        warn("At a Glance 섹션이 비어 있어 생략합니다.")
        return ""
    ps = "\n".join(
        '        <p class="text-[15px] leading-relaxed text-gray-800">\n          %s\n        </p>'
        % inline(g, link_class="underline text-indigo-700")
        for g in doc["glance"]
    )
    return """    <!-- ===== AT A GLANCE ===== -->
    <section class="mb-8">
      <h2 class="text-xs font-bold tracking-widest text-indigo-600 uppercase mb-3">At a Glance</h2>
      <div class="bg-indigo-50 border border-indigo-200 rounded-2xl p-5 space-y-3">
{ps}
      </div>
    </section>""".format(ps=ps)


CALLOUT_META = {
    "KEY POINT": ("why-matters", "KEY POINT"),
    "INSIGHT": ("insight", "💡 Insight"),
    "DEMAND": ("customer", "🙋 Demand"),
}


def render_callout(kind, text):
    cls, label = CALLOUT_META[kind]
    return ('          <div class="%s">\n            <div class="label">%s</div>\n'
            '            <div class="text">%s</div>\n          </div>'
            % (cls, label, inline(text)))


def render_top5(doc):
    if not doc["top5"]:
        warn("Today's Top 5 섹션이 비어 있어 생략합니다.")
        return ""
    cards = []
    for idx, it in enumerate(doc["top5"], 1):
        parts = ["        <!-- Card %d -->" % idx,
                 '        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">']
        parts.append(badges_row(it["badges"] or ["Market"]))
        parts.append('          <h3 class="text-[17px] font-bold text-gray-900 leading-snug mb-1">\n            %s\n          </h3>'
                     % inline(it["title"]))
        if it["lead"]:
            lead = " ".join(it["lead"])
            parts.append('          <p class="text-[15px] text-gray-600 leading-relaxed mb-1">%s</p>'
                         % inline(lead))
        for kind, text in it["callouts"]:
            parts.append(render_callout(kind, text))
        sl = source_links_row(it["links"])
        if sl:
            parts.append(sl)
        parts.append("        </div>")
        cards.append("\n".join(parts))
    body = "\n\n".join(cards)
    return """    <!-- ===== TODAY'S TOP 5 ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Today's Top 5</h2>
      <div class="space-y-6">

{body}

      </div>
    </section>""".format(body=body)


def render_topic(doc):
    t = doc["topic"]
    if not t:
        warn("Today's Topic 섹션이 없어 생략합니다.")
        return ""
    badges = "\n          ".join(badge_html(b) for b in t["badges"])
    paras = "\n          ".join(
        '<p>%s</p>' % inline(p) for p in t["paras"])
    summary = ""
    if t["summary"]:
        summary = """        <div class="mt-5 p-4 bg-white rounded-xl border border-purple-100">
          <p class="text-sm font-semibold text-purple-700 mb-1">💬 한 줄 요약</p>
          <p class="text-[15px] text-gray-800">%s</p>
        </div>""" % inline(t["summary"])
    src = ""
    if t["links"]:
        n, u = t["links"][0]
        src = """        <div class="mt-3 text-sm text-gray-500">
          <a href="%s" class="underline text-indigo-600" target="_blank">↗ %s</a>
        </div>""" % (u, esc(n))
    return """    <!-- ===== TODAY'S TOPIC ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">🗣 Today's Topic</h2>
      <div class="bg-gradient-to-br from-purple-50 to-indigo-50 border border-purple-200 rounded-2xl p-7">
        <div class="flex flex-wrap gap-2 mb-4">
          {badges}
        </div>
        <h3 class="text-[19px] font-bold text-gray-900 mb-4">{title}</h3>
        <div class="space-y-3 text-[15.5px] text-gray-800 leading-relaxed">
          {paras}
        </div>
{summary}
{src}
      </div>
    </section>""".format(badges=badges, title=inline(t["title"]), paras=paras,
                         summary=summary, src=src)


def render_english(doc):
    if not doc["english"]:
        warn("Business English 섹션이 비어 있어 생략합니다.")
        return ""
    cards = []
    for e in doc["english"]:
        example = ""
        if e["en"]:
            example = """          <div class="eng-example">
            <div class="flex items-start gap-3">
              <button class="play-circle mt-0.5" onclick="_speak('{ensp}', this)" aria-label="예문 재생">
                {playsvg}
              </button>
              <div>
                <p class="en">{en}</p>
                <p class="ko">{ko}</p>
              </div>
            </div>
          </div>""".format(ensp=js_str(e["en"]), playsvg=PLAY_SVG,
                           en=inline(e["en"]), ko=inline(e["ko"] or ""))
        card = """        <div class="eng-card">
          <div class="flex items-center gap-3 flex-wrap">
            <span class="eng-word">{word}</span>
            <button class="voice-btn" onclick="_speak('{speak}', this)" aria-label="{word} 발음 듣기">
              {svg}
            </button>
          </div>
          <p class="eng-meaning">{meaning}</p>
          <p class="eng-desc">{desc}</p>
{example}
        </div>""".format(word=esc(e["word"]), speak=js_str(e["speak"]),
                         svg=VOICE_SVG, meaning=esc(e["meaning"]),
                         desc=inline(e["desc"]), example=example)
        cards.append(card)
    body = "\n\n".join(cards)
    return """    <!-- ===== BUSINESS ENGLISH ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">🗽 Business English</h2>
      <div class="space-y-5">

{body}

      </div>
    </section>""".format(body=body)


def render_deepdive(doc):
    if not doc["deepdive"]:
        warn("Deep Dive 섹션이 비어 있어 생략합니다.")
        return ""
    blocks = []
    for eng_head, badge, items in doc["deepdive"]:
        details = []
        for it in items:
            inner = []
            if it["watch"]:
                inner.append('              <p class="mt-3">%s</p>' % inline(it["watch"]))
            if it["bull"] or it["bear"]:
                bull = inline(it["bull"] or "")
                bear = inline(it["bear"] or "")
                inner.append("""              <div class="grid md:grid-cols-2 gap-3 mt-3">
                <div class="bg-green-50 border border-green-200 rounded-xl p-4">
                  <p class="text-xs font-bold text-green-700 mb-2">강세 근거</p>
                  <p class="text-[14px] text-gray-800 leading-relaxed">%s</p>
                </div>
                <div class="bg-red-50 border border-red-200 rounded-xl p-4">
                  <p class="text-xs font-bold text-red-700 mb-2">약세 근거</p>
                  <p class="text-[14px] text-gray-800 leading-relaxed">%s</p>
                </div>
              </div>""" % (bull, bear))
            if it["frame"]:
                inner.append("""              <div class="why-matters mt-4">
                <div class="label">전략 프레임</div>
                <div class="text">%s</div>
              </div>""" % inline(it["frame"]))
            for dt, dtext in it["demand"]:
                inner.append("""              <div class="customer mt-3">
                <div class="label">🙋 Demand · %s</div>
                <div class="text">%s</div>
              </div>""" % (esc(dt), inline(dtext)))
            if it["sources"]:
                a = " · ".join(
                    '<a href="%s" class="underline text-indigo-600" target="_blank">↗ %s</a>'
                    % (u, esc(n)) for n, u in it["sources"])
                inner.append('              <p class="mt-3 text-sm text-gray-500">%s</p>' % a)
            inner_html = "\n".join(inner)
            details.append("""          <details class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
            <summary class="flex items-center gap-3 p-5 hover:bg-gray-50 transition-colors">
              {badge}
              <span class="font-semibold text-gray-900 text-[15px] flex-1">{title}</span>
              <span class="chevron text-gray-400 flex-shrink-0">▼</span>
            </summary>
            <div class="px-5 pb-5 pt-1 text-[15px] text-gray-800 leading-relaxed border-t border-gray-100">
{inner}
            </div>
          </details>""".format(badge=badge_html(badge, sub=True),
                               title=inline(it["title"]), inner=inner_html))
        block = """      <div class="mb-6">
        <h3 class="text-base font-bold text-gray-700 uppercase tracking-wide mb-3 flex items-center gap-2">
          <span class="{cls} text-xs font-semibold px-2.5 py-1 rounded-full">{head}</span>
        </h3>
        <div class="space-y-4">

{details}

        </div>
      </div>""".format(cls=BADGE_CLASS.get(badge, "badge-macro"), head=eng_head,
                       details="\n\n".join(details))
        blocks.append(block)
    return """    <!-- ===== DEEP DIVE ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Deep Dive</h2>

{blocks}

    </section>""".format(blocks="\n\n".join(blocks))


def render_demand(doc):
    if not doc["demand"]:
        warn("Demand 섹션이 비어 있어 생략합니다.")
        return ""
    cards = []
    for d in doc["demand"]:
        badges = infer_badges(d["title"] + " " + d["body"])
        cards.append("""        <div class="bg-white rounded-2xl border border-amber-100 shadow-sm p-6">
{brow}
          <h3 class="text-[16px] font-bold text-gray-900 mb-3">{title}</h3>
          <div class="customer">
            <div class="label">🙋 Demand</div>
            <div class="text">{body}</div>
          </div>
        </div>""".format(brow=badges_row(badges), title=inline(d["title"]),
                         body=inline(d["body"])))
    return """    <!-- ===== DEMAND ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-2 pb-2 border-b border-gray-200">🙋 Demand</h2>
      <p class="text-sm text-gray-500 mb-5">누가 사고 쓰나, 왜 — 수요자 눈으로 본 오늘.</p>
      <div class="space-y-4">

{cards}

      </div>
    </section>""".format(cards="\n\n".join(cards))


def render_investment(doc):
    if not doc["investment"]:
        warn("Investment 섹션이 비어 있어 생략합니다.")
        return ""
    cards = []
    connector = None
    for it in doc["investment"]:
        if "연결" in it["title"]:
            connector = it
            continue
        badges = infer_badges(it["title"] + " " + it["body"])
        body = it["body"]
        grid = ""
        intro = body
        bm = re.search(r"강세\s*근거\s*:\s*(.+?)\s*/\s*약세\s*근거\s*:\s*(.+)$", body)
        if bm:
            intro = body[:bm.start()].strip()
            bull = bm.group(1).strip()
            bear = bm.group(2).strip()
            grid = """          <div class="grid md:grid-cols-2 gap-3{mt}">
            <div class="bg-green-50 border border-green-200 rounded-xl p-4">
              <p class="text-xs font-bold text-green-700 mb-2">강세 근거</p>
              <p class="text-[14px] text-gray-800 leading-relaxed">{bull}</p>
            </div>
            <div class="bg-red-50 border border-red-200 rounded-xl p-4">
              <p class="text-xs font-bold text-red-700 mb-2">약세 근거</p>
              <p class="text-[14px] text-gray-800 leading-relaxed">{bear}</p>
            </div>
          </div>""".format(mt=" mt-3" if intro else "", bull=inline(bull),
                           bear=inline(bear))
        intro_html = ('          <p class="text-[15px] text-gray-800 leading-relaxed">%s</p>'
                      % inline(intro)) if intro else ""
        cards.append("""        <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
{brow}
          <h3 class="text-[16px] font-bold text-gray-900 mb-3">{title}</h3>
{intro}
{grid}
        </div>""".format(brow=badges_row(badges), title=inline(it["title"]),
                         intro=intro_html, grid=grid))
    conn_html = ""
    if connector:
        conn_html = """\n        <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-5">
          <p class="text-sm font-bold text-indigo-800 mb-2">국내외 연결 고리</p>
          <p class="text-[14.5px] text-gray-800 leading-relaxed">%s</p>
        </div>""" % inline(connector["body"])
    return """    <!-- ===== INVESTMENT ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-2 pb-2 border-b border-gray-200">💰 Investment</h2>
      <p class="text-sm text-gray-500 mb-5">투자 참고용 정보입니다. 판단과 책임은 본인에게 있습니다.</p>
      <div class="space-y-4">

{cards}{conn}

      </div>
    </section>""".format(cards="\n\n".join(cards), conn=conn_html)


def render_companies(doc):
    if not doc["companies"]:
        warn("Companies to Watch 섹션이 비어 있어 생략합니다.")
        return ""
    cards = []
    for c in doc["companies"]:
        badges = infer_badges(c["title"] + " " + c["body"])
        links = extract_links(c["body"])
        body_text = c["body"]
        sl = ""
        if links:
            a = " · ".join(
                '<a href="%s" class="underline text-indigo-600" target="_blank">↗ %s</a>'
                % (u, esc(n)) for n, u in links)
            sl = '\n          <p class="mt-2 text-sm text-gray-500">%s</p>' % a
        cards.append("""        <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
{brow}
          <h3 class="text-[16px] font-bold text-gray-900 mb-2">{title}</h3>
          <p class="text-[15px] text-gray-800 leading-relaxed">{body}</p>{sl}
        </div>""".format(brow=badges_row(badges), title=inline(c["title"]),
                         body=inline(body_text), sl=sl))
    return """    <!-- ===== COMPANIES TO WATCH ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">🚀 Companies to Watch</h2>
      <div class="space-y-4">

{cards}

      </div>
    </section>""".format(cards="\n\n".join(cards))


def render_threads(doc):
    if not doc["threads"]:
        warn("Threads to Follow 섹션이 비어 있어 생략합니다.")
        return ""
    lis = []
    for t in doc["threads"]:
        badge = (t["badges"] or ["Market"])[0]
        lis.append("""          <li class="flex items-start gap-2">
            <span class="{cls} text-xs font-semibold px-2 py-0.5 rounded-full mt-0.5 flex-shrink-0">{name}</span>
            <span>{text}</span>
          </li>""".format(cls=BADGE_CLASS.get(badge, "badge-macro"), name=badge,
                          text=inline(t["text"])))
    return """    <!-- ===== THREADS TO FOLLOW ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Threads to Follow</h2>
      <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
        <ul class="space-y-3 text-[15px] text-gray-800">
{lis}
        </ul>
      </div>
    </section>""".format(lis="\n".join(lis))


def render_sources(doc):
    if not doc["sources"]:
        warn("Sources 섹션이 비어 있어 생략합니다.")
        return ""
    cols = []
    for cat, links in doc["sources"]:
        items = "\n".join(
            '              <li><a href="%s" class="text-indigo-600 underline" target="_blank">%s</a></li>'
            % (u, esc(n)) for n, u in links)
        cols.append("""          <div>
            <p class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">{cat}</p>
            <ul class="space-y-2 text-[13.5px]">
{items}
            </ul>
          </div>""".format(cat=esc(cat), items=items))
    return """    <!-- ===== SOURCES ===== -->
    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Sources</h2>
      <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
        <div class="grid md:grid-cols-3 gap-6">
{cols}
        </div>
      </div>
    </section>""".format(cols="\n".join(cols))


def render_footer(doc):
    date = esc(doc["date"] or "")
    return """    <!-- ===== FOOTER ===== -->
    <footer class="border-t border-gray-200 pt-8 pb-10 text-center">
      <a href="https://t.me/econradar" target="_blank" rel="noopener"
         class="inline-flex items-center gap-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold text-[15px] rounded-xl px-5 py-3 shadow-sm hover:shadow-md transition mb-2">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.94 4.6 18.7 19.9c-.24 1.08-.88 1.34-1.79.84l-4.94-3.64-2.38 2.29c-.26.26-.48.48-.99.48l.35-5.03 9.15-8.27c.4-.35-.09-.55-.62-.2L4.55 13.37l-4.87-1.52c-1.06-.33-1.08-1.06.22-1.57L20.57 3.05c.88-.33 1.65.2 1.37 1.55z"/></svg>
        매일 텔레그램으로 받기 <span class="text-indigo-200 font-normal text-sm">@econradar</span>
      </a>
      <p class="text-xs text-gray-400">매일 저녁(오후 6시 반 이후) 핵심 5건 요약 + 전체 링크.</p>
      <p class="text-sm text-gray-500 mt-4">econ-radar · {date}</p>
      <p class="text-xs text-gray-400 mt-1">투자 참고용 정보입니다. 판단과 책임은 본인에게 있습니다.</p>
    </footer>""".format(date=date)


# ----------------------------------------------------------------------------
# 푸시 메시지
# ----------------------------------------------------------------------------
EMOJI_NUM = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]


def render_push(doc):
    # 텔레그램 채널 구독자가 채널만 보고도 그날 핵심을 파악할 수 있게
    # 핵심 5건 제목까지 펼친다. 이 파일이 곧 텔레그램 메시지 본문이다.
    date = doc["date"] or ""
    lines = ["📰 econ-radar %s" % date]
    if doc["topic"]:
        topic_line = "🗣 오늘의 화제: %s" % doc["topic"]["title"]
        if doc["topic"].get("summary"):
            topic_line = "🗣 오늘의 화제: %s — %s" % (
                doc["topic"]["title"], doc["topic"]["summary"])
        lines.append(topic_line)
    lines.append("")
    for idx, it in enumerate(doc["top5"][:5]):
        title = re.sub(r"\s+", " ", it["title"]).strip()
        lines.append("%s %s" % (EMOJI_NUM[idx], title))
    lines.append("")
    # 전체 보기: 발행본 블로그 HTML(구독자가 풀 다이제스트로 이동)
    if date:
        lines.append("🔗 전체 보기: https://kakyungkim.github.io/econ-radar/%s.html" % date)
    # 핵심 1차 출처 1개: Today's Topic 첫 출처 → 없으면 Top1 첫 출처
    key = None
    if doc["topic"] and doc["topic"]["links"]:
        n, u = doc["topic"]["links"][0]
        key = ("%s — %s" % (doc["topic"]["title"], n), u)
    elif doc["top5"] and doc["top5"][0]["links"]:
        n, u = doc["top5"][0]["links"][0]
        key = ("%s — %s" % (doc["top5"][0]["title"], n), u)
    if key:
        # 텔레그램 평문에서 자동 링크되도록 맨 URL로(마크다운 [라벨](url) 미사용).
        lines.append("🔗 핵심 원문: %s" % key[1])
    return "\n".join(lines) + "\n"


# ----------------------------------------------------------------------------
# 이메일(Buttondown) — 하이브리드: At a Glance + Top 5 + 전체보기 CTA
# ----------------------------------------------------------------------------
# 이메일 클라이언트는 JS·외부 CSS·@import를 거의 못 쓴다. 따라서 Tailwind 대신
# 인라인 style 속성과 table 레이아웃만 쓰고, 깊이 있는 본문(Deep Dive 등)은
# 블로그 전체 리포트 링크로 넘긴다. Gmail 102KB 클리핑을 피하려고 히어로
# 이미지는 base64로 박지 않고 본문을 가볍게 유지한다.

# 배지 클래스 → (배경, 글자) 인라인 색
_CLASS_COLOR = {
    "badge-macro": ("#dbeafe", "#1e40af"),
    "badge-ai": ("#ede9fe", "#5b21b6"),
    "badge-bio": ("#dcfce7", "#166534"),
    "badge-market": ("#fef3c7", "#92400e"),
    "badge-company": ("#fef3c7", "#92400e"),
}


def email_badge(name):
    bg, fg = _CLASS_COLOR.get(BADGE_CLASS.get(name, "badge-macro"),
                              ("#dbeafe", "#1e40af"))
    return ('<span style="display:inline-block;background:%s;color:%s;'
            'font-size:12px;font-weight:600;padding:3px 9px;border-radius:999px;'
            'margin:0 6px 6px 0;">%s</span>' % (bg, fg, esc(name)))


def inline_email(text):
    """inline() 의 이메일판: 링크에 class 대신 인라인 style 을 단다."""
    text = WIKILINK_RE.sub(" ", text)
    out = []
    pos = 0
    for m in LINK_RE.finditer(text):
        out.append(_bold(esc(text[pos:m.start()])))
        url = m.group(2)
        out.append('<a href="%s" style="color:#4338ca;text-decoration:underline;" '
                   'target="_blank">%s</a>' % (url, esc(m.group(1))))
        pos = m.end()
    out.append(_bold(esc(text[pos:])))
    return "".join(out).strip()


def email_subject(doc):
    date = doc["date"] or ""
    hook = None
    if doc["topic"] and doc["topic"].get("title"):
        hook = doc["topic"]["title"]
    elif doc["top5"]:
        hook = doc["top5"][0]["title"]
    if hook:
        hook = WIKILINK_RE.sub(" ", hook)
        hook = re.sub(r"\*\*([^*]+)\*\*", r"\1", hook)
        hook = re.sub(r"\s+", " ", hook).strip()
        return "📈 econ-radar %s · %s" % (date, hook)
    return "📈 econ-radar %s" % date


def render_email(doc):
    """이메일용 단일 HTML 문서와 제목을 만든다. 반환: (subject, html)."""
    date = esc(doc["date"] or "")
    raw_date = doc["date"] or ""
    subtitle = esc(doc["subtitle"] or "")
    blog_url = "%s/%s.html" % (BLOG_BASE, raw_date)
    subject = email_subject(doc)

    blocks = []

    # At a Glance
    if doc["glance"]:
        ps = "".join(
            '<p style="margin:0 0 10px;font-size:15px;line-height:1.7;'
            'color:#1f2937;">%s</p>' % inline_email(g) for g in doc["glance"])
        blocks.append(
            '<tr><td style="padding:18px 24px 0;">'
            '<p style="margin:0 0 10px;font-size:12px;font-weight:700;'
            'letter-spacing:1px;text-transform:uppercase;color:#4f46e5;">At a Glance</p>'
            '<div style="background:#eef2ff;border:1px solid #c7d2fe;'
            'border-radius:14px;padding:18px 20px;">%s</div></td></tr>' % ps)

    # Today's Top 5
    if doc["top5"]:
        cards = []
        for idx, it in enumerate(doc["top5"], 1):
            badges = "".join(email_badge(b) for b in (it["badges"] or ["Market"]))
            lead = ""
            if it["lead"]:
                lead = ('<p style="margin:8px 0 0;font-size:14.5px;line-height:1.65;'
                        'color:#4b5563;">%s</p>' % inline_email(" ".join(it["lead"])))
            src = ""
            if it["links"]:
                n, u = it["links"][0]
                src = ('<p style="margin:10px 0 0;font-size:13px;">'
                       '<a href="%s" style="color:#4f46e5;text-decoration:none;" '
                       'target="_blank">↗ %s</a></p>' % (u, esc(n)))
            cards.append(
                '<div style="background:#ffffff;border:1px solid #eceef2;'
                'border-radius:14px;padding:18px 20px;margin:0 0 14px;">'
                '<div style="margin:0 0 8px;">%s</div>'
                '<p style="margin:0;font-size:16px;font-weight:700;line-height:1.45;'
                'color:#111827;"><span style="color:#9ca3af;">%d.</span> %s</p>%s%s'
                '</div>' % (badges, idx, inline_email(it["title"]), lead, src))
        blocks.append(
            '<tr><td style="padding:18px 24px 0;">'
            '<p style="margin:0 0 14px;font-size:19px;font-weight:700;color:#111827;'
            'border-bottom:2px solid #e5e7eb;padding-bottom:8px;">Today&#39;s Top 5</p>'
            '%s</td></tr>' % "".join(cards))

    # 오늘의 화제 한 줄 요약(있으면)
    if doc["topic"] and doc["topic"].get("summary"):
        blocks.append(
            '<tr><td style="padding:6px 24px 0;">'
            '<div style="background:#f5f3ff;border:1px solid #ddd6fe;'
            'border-radius:14px;padding:16px 20px;">'
            '<p style="margin:0 0 6px;font-size:12px;font-weight:700;color:#7c3aed;">'
            '🗣 오늘의 화제</p>'
            '<p style="margin:0;font-size:15px;line-height:1.65;color:#1f2937;">%s</p>'
            '</div></td></tr>' % inline_email(doc["topic"]["summary"]))

    # 전체보기 CTA — 일부 메일 클라이언트가 <a>의 background 를 무시해 버튼이
    # 평평한 링크 글씨로만 보이는 문제가 있다. 배경색을 td bgcolor 에 줘서
    # 어디서나 채워진 버튼으로 보이게 하는 bulletproof 패턴.
    # 인디고 배경 + 순백색 굵은 글씨(고대비, 브랜드색 유지).
    blocks.append(
        '<tr><td style="padding:26px 24px 8px;" align="center">'
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;">'
        '<tr><td bgcolor="#4f46e5" style="border-radius:12px;" align="center">'
        '<a href="%s" target="_blank" style="display:inline-block;padding:16px 36px;'
        'font-size:16px;font-weight:700;color:#ffffff;text-decoration:none;'
        'border-radius:12px;background:#4f46e5;">전체 리포트 보기 &rarr;</a>'
        '</td></tr></table>'
        '<p style="margin:14px 0 0;font-size:12px;color:#9ca3af;line-height:1.6;">'
        'Deep Dive · Demand · Investment · Companies · Sources 전체는 위 링크에서 보실 수 있습니다.</p>'
        '</td></tr>' % blog_url)

    subtitle_html = ""
    if subtitle:
        subtitle_html = ('<p style="margin:8px 0 0;font-size:14px;line-height:1.6;'
                         'color:#6b7280;">%s</p>' % subtitle)

    html = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light only">
<title>{subject}</title>
</head>
<body style="margin:0;padding:0;background:#f3f4f6;font-family:'Apple SD Gothic Neo','Malgun Gothic',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;-webkit-text-size-adjust:100%;">
<!-- SUBJECT: {subject} -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f3f4f6;">
  <tr><td align="center" style="padding:24px 12px;">
    <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#ffffff;border:1px solid #e5e7eb;border-radius:18px;overflow:hidden;">
      <tr><td style="padding:28px 24px 4px;">
        <p style="margin:0;font-size:22px;font-weight:800;color:#111827;">📈 econ-radar 데일리</p>
        <p style="margin:4px 0 0;font-size:14px;color:#6b7280;">{date}</p>
        {subtitle_html}
      </td></tr>
{blocks}
      <tr><td style="padding:26px 24px 24px;border-top:1px solid #e5e7eb;text-align:center;">
        <a href="https://t.me/econradar" target="_blank" style="color:#4f46e5;text-decoration:none;font-size:14px;font-weight:600;">텔레그램 @econradar 로도 받기</a>
        <p style="margin:12px 0 0;font-size:12px;color:#9ca3af;">econ-radar · {date}</p>
        <p style="margin:4px 0 0;font-size:12px;color:#9ca3af;">투자 참고용 정보입니다. 최종 판단과 책임은 본인에게 있습니다.</p>
      </td></tr>
    </table>
  </td></tr>
</table>
</body>
</html>
""".format(subject=esc(subject), date=date, subtitle_html=subtitle_html,
           blocks="\n".join(blocks))
    return subject, html


# ----------------------------------------------------------------------------
# 메인
# ----------------------------------------------------------------------------
def build_html(doc, hero_b64):
    sections = [
        render_header(doc, hero_b64),
        render_glance(doc),
        render_top5(doc),
        render_topic(doc),
        render_english(doc),
        render_deepdive(doc),
        render_demand(doc),
        render_investment(doc),
        render_companies(doc),
        render_threads(doc),
        render_sources(doc),
        render_footer(doc),
    ]
    body = "\n\n".join(s for s in sections if s)
    with open(TEMPLATE, encoding="utf-8") as f:
        tmpl = f.read()
    return tmpl.replace("{{DATE}}", doc["date"] or "").replace("{{BODY}}", body)


def main():
    ap = argparse.ArgumentParser(description="econ-radar 뉴스레터 HTML/푸시 렌더러")
    ap.add_argument("date", help="발행 날짜 (YYYY-MM-DD)")
    ap.add_argument("--out-suffix", default="",
                    help="출력 파일명 접미사(예: .test). 기존 정식본 보존용.")
    args = ap.parse_args()

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", args.date):
        sys.stderr.write("[render_html] 오류: 날짜 형식은 YYYY-MM-DD 여야 합니다.\n")
        sys.exit(2)

    md_path = os.path.join(DAILY_DIR, args.date + ".md")
    if not os.path.isfile(md_path):
        sys.stderr.write("[render_html] 오류: 입력 md 가 없습니다: %s\n" % md_path)
        sys.exit(1)

    if not os.path.isfile(TEMPLATE):
        sys.stderr.write("[render_html] 오류: 템플릿이 없습니다: %s\n" % TEMPLATE)
        sys.exit(1)

    if not os.path.isfile(HERO_IMG):
        sys.stderr.write("[render_html] 오류: 히어로 이미지가 없습니다: %s\n" % HERO_IMG)
        sys.exit(1)

    with open(md_path, encoding="utf-8") as f:
        md = f.read()

    try:
        doc = parse_markdown(md)
    except Exception as e:  # noqa
        sys.stderr.write("[render_html] 파싱 실패: %s\n" % e)
        sys.exit(1)

    if not doc["date"]:
        doc["date"] = args.date
    if not doc["top5"] and not doc["glance"]:
        sys.stderr.write("[render_html] 오류: 필수 섹션(At a Glance/Top 5)을 찾지 못했습니다. "
                         "NEWSLETTER-FORMAT.md 계약을 확인하세요.\n")
        sys.exit(1)

    with open(HERO_IMG, "rb") as f:
        hero_b64 = base64.b64encode(f.read()).decode("ascii")

    html = build_html(doc, hero_b64)
    push = render_push(doc)
    _, email_html = render_email(doc)

    suffix = args.out_suffix
    html_path = os.path.join(HTML_DIR, args.date + suffix + ".html")
    push_path = os.path.join(PUSH_DIR, args.date + suffix + ".md")
    email_path = os.path.join(EMAIL_DIR, args.date + suffix + ".html")
    os.makedirs(HTML_DIR, exist_ok=True)
    os.makedirs(PUSH_DIR, exist_ok=True)
    os.makedirs(EMAIL_DIR, exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    with open(push_path, "w", encoding="utf-8") as f:
        f.write(push)
    with open(email_path, "w", encoding="utf-8") as f:
        f.write(email_html)

    sys.stderr.write("[render_html] 완료\n")
    sys.stderr.write("  HTML : %s (%d bytes)\n" % (html_path, len(html.encode("utf-8"))))
    sys.stderr.write("  PUSH : %s\n" % push_path)
    sys.stderr.write("  EMAIL: %s (%d bytes)\n" % (email_path, len(email_html.encode("utf-8"))))
    sys.stderr.write("  섹션: top5=%d, deepdive=%d, demand=%d, investment=%d, "
                     "companies=%d, english=%d, threads=%d, sources=%d\n" % (
                         len(doc["top5"]), sum(len(x[2]) for x in doc["deepdive"]),
                         len(doc["demand"]), len(doc["investment"]),
                         len(doc["companies"]), len(doc["english"]),
                         len(doc["threads"]), sum(len(x[1]) for x in doc["sources"])))


if __name__ == "__main__":
    main()
