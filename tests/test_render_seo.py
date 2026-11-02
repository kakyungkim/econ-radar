"""데일리 페이지의 검색 노출(SEO, GEO) 계약 검사.

2026-11-02 점검에서 데일리 페이지 제목이 날짜뿐("econ-radar — 2026-11-01")이었고, 검색 결과에 보일 요약,
링크 미리보기(og), 구조화 데이터(JSON-LD), 메일 구독 안내가 없었다. 블로그 글에는 이미 있는 것들이다.
"""
import os, sys, re, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import render_html as R

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATE = "2026-11-01"


def _html():
    md = open(os.path.join(ROOT, "vault", "daily", DATE + ".md"), encoding="utf-8").read()
    return R.build_html(R.parse_markdown(md), None)


def _meta(html, attr, name):
    m = re.search(r'<meta %s="%s" content="([^"]*)"' % (attr, re.escape(name)), html)
    return m.group(1) if m else None


def test_title_has_headline_not_only_date():
    t = re.search(r"<title>([^<]*)</title>", _html()).group(1)
    assert DATE in t and len(t) > len("econ-radar — " + DATE) + 5
    assert len(t) <= 70


def test_description_and_og():
    h = _html()
    d = _meta(h, "name", "description")
    assert d and 50 <= len(d) <= 170
    assert _meta(h, "property", "og:title")
    assert _meta(h, "property", "og:description") == d
    assert _meta(h, "property", "og:url") == "https://kakyungkim.github.io/econ-radar/%s.html" % DATE
    assert _meta(h, "property", "og:locale") == "ko_KR"


def test_jsonld_newsarticle():
    h = _html()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    assert blocks
    j = json.loads(blocks[0])
    assert j["@type"] == "NewsArticle"
    assert j["datePublished"].startswith(DATE)
    assert j["inLanguage"] == "ko-KR"
    assert j["author"]["name"] and j["headline"]


def test_no_template_placeholders_left():
    assert "{{" not in _html()


def test_footer_offers_email_and_telegram_subscription():
    h = _html()
    assert "buttondown.com/kakyungkim" in h
    assert "t.me/econradar" in h


def test_weekly_head_meta():
    import render_weekly as W
    h = W.head_meta("🧭 econ-radar 동향 리포트 · 2026-W44", ["ADC 임상 설계 문법이 정착했다.", "AI 투자 ROI의 첫 채점이 나왔다."], "2026-W44")
    assert '<meta name="description" content="ADC 임상 설계' in h
    assert 'property="og:url" content="https://kakyungkim.github.io/econ-radar/2026-W44.html"' in h
    j = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
    assert j["@type"] == "Article" and j["inLanguage"] == "ko-KR"
