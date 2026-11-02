"""주제 허브 페이지 생성기 검사. 작은 events fixture 로 head, JSON-LD, 정렬, 금지 문자를 확인한다."""
import os, sys, re, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import build_topic_hubs as H


def ev(date, title, topics, i=1, url="https://example.com/x", section="top5"):
    return {"id": "%s-%s-%d" % (date, section, i), "date": date, "section": section, "sector": "",
            "title": title, "summary": "요약 문장입니다. 둘째 문장.", "url": url, "urls": url,
            "numbers": "", "topics": topics, "fact_flag": ""}


ROWS = [
    ev("2026-09-30", "ADC 옛 소식", "ADC항체약물접합체"),
    ev("2026-11-01", "ADC 최신 소식 <b>", "ADC항체약물접합체"),
    ev("2026-10-15", "ADC 중간 소식", "ADC항체약물접합체|FOMC"),
    ev("2026-10-16", "금리 소식", "FOMC", url=""),
    ev("2026-10-17", "아무 주제 아님", ""),
]
NOTE = """---
type: moc
---
# t

## 핵심 흐름
- **첫째 흐름 — 제목**: 내용 하나입니다. 내용 둘입니다 [[topics/x]].
- **둘째 흐름**: 또 다른 내용입니다. 세부는 Trop-2·B7-H3·CLDN18.2 표적이다.
- **셋째**: 셋째 내용입니다.

## 타임라인
"""


def _page(tmp_path):
    d = tmp_path / "topics"
    d.mkdir()
    (d / "ADC항체약물접합체.md").write_text(NOTE, encoding="utf-8")
    intro = H.intro_for("ADC항체약물접합체", str(d))
    rows = [r for r in ROWS if "ADC항체약물접합체" in r["topics"].split("|")]
    return H.render_hub("ADC항체약물접합체", "adc", rows, intro), intro


def test_head_and_structure(tmp_path):
    page, _ = _page(tmp_path)
    assert '<html lang="ko">' in page and 'name="viewport"' in page
    assert "<title>ADC(항체약물접합체) 동향 타임라인 | econ-radar</title>" in page
    assert '<link rel="canonical" href="https://kakyungkim.github.io/econ-radar/topics/adc.html">' in page
    assert 'property="og:locale" content="ko_KR"' in page
    assert "<h1>ADC(항체약물접합체): econ-radar 주제 허브</h1>" in page
    assert "2026-09-30 ~ 2026-11-01" in page and "3건" in page
    assert 'data-goatcounter="https://kakyungkim.goatcounter.com/count"' in page
    assert "buttondown.com/kakyungkim" in page and "t.me/econradar" in page
    assert "투자 참고용 정보입니다. 판단과 책임은 본인에게 있습니다." in page


def test_jsonld_parses(tmp_path):
    page, _ = _page(tmp_path)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)
    data = json.loads(m.group(1))
    assert data["@type"] == "CollectionPage"
    items = data["hasPart"]["itemListElement"]
    assert len(items) == 3
    assert items[0]["url"] == "https://kakyungkim.github.io/econ-radar/2026-11-01.html"
    assert items[0]["datePublished"] == "2026-11-01"


def test_newest_first_and_month_groups(tmp_path):
    page, _ = _page(tmp_path)
    pos = [page.index(t) for t in ("ADC 최신 소식", "ADC 중간 소식", "ADC 옛 소식")]
    assert pos == sorted(pos)
    assert page.index("2026년 11월") < page.index("2026년 10월") < page.index("2026년 9월")


def test_escaping_and_forbidden_chars(tmp_path):
    page, intro = _page(tmp_path)
    assert "<b>" not in page and "&lt;b&gt;" in page
    assert "{{" not in page and "{topic" not in page
    assert "…" not in page
    assert "—" not in intro and "·" not in intro and "[[" not in intro and "**" not in intro


def test_intro_is_first_sentences_of_core_flow(tmp_path):
    _, intro = _page(tmp_path)
    assert intro.startswith("첫째 흐름") and "내용 하나입니다." in intro
    assert 2 <= len(re.findall(r"다\.", intro)) <= 3 + 1


def test_item_without_source_has_no_empty_link(tmp_path):
    rows = [r for r in ROWS if r["topics"] == "FOMC"]
    page = H.render_hub("FOMC", "fomc", rows, "소개입니다.")
    assert 'href=""' not in page


def test_select_hubs_excludes_generic():
    rows = [ev("2026-10-%02d" % (i % 28 + 1), "t", "AI") for i in range(40)] + \
           [ev("2026-10-01", "t", "ADC", i) for i in range(5)] + [ev("2026-10-02", "t", "", i) for i in range(5)]
    chosen, excluded = H.select_hubs(rows, n=12, generic_ratio=0.3)
    assert [t for t, _ in chosen] == ["ADC"]
    assert excluded[0][0] == "AI"


def test_index_lists_hubs():
    page = H.render_index([("ADC항체약물접합체", "adc", 3, "2026-09-30", "2026-11-01")])
    assert 'href="adc.html"' in page and "ADC항체약물접합체" in page and "…" not in page
