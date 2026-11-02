"""사건 표(events.csv) 생성기 검사. 네트워크 없이 작은 데일리 fixture 로 행, 주제 매칭, 평문화를 확인한다."""
import os, sys, csv
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import build_event_db as B

DAILY = """---
date: 2026-10-29
type: daily
---
# econ-radar 데일리 — 2026-10-29
> 부제

**At a Glance**
💰 한 줄

## Today's Top 5

### 1. 💊 ADC [[topics/ADC]] sac-TMT 임상, PFS HR 0.49 · 매출 190조원
Merck의 [임상 결과](https://example.com/a)가 나왔다. 주가는 +48% 올랐다(본문 확인 필요).
**Key Point**: 핵심
출처: [Merck IR](https://example.com/a) | [Onclive](https://example.com/b) — [[topics/ADC]]

# Deep Dive

## Macro & Policy

### [FOMC 동결 — 10-2 균열](https://example.com/fomc)
**관전 포인트**: 12월 인상 확률 80%다. 금리 경로가 관건이다.
**1차 자료**: [CNBC](https://example.com/c1) | [Fed](https://example.com/c2)

## 🙋 Demand

- **HBM 공급망 수요**: 엔비디아가 직접 구매자다. [출처](https://example.com/d)

## 💰 Investment

### 오늘의 투자 시사점

- **AIDS 백신 관련주**: 변동성이 크다.
- **AI 클라우드 ROI**: Azure +48% 성장.

## 🚀 Companies to Watch

- **Acme (ACME)**: 다음 관전 포인트. [Acme IR](https://example.com/e)
"""

TOPICS = {
    "ADC항체약물접합체.md": "---\ntype: moc\naliases: [ADC플랫폼]\n---\n# x\n",
    "ADC.md": "---\nstatus: deprecated\nmerged_into: topics/ADC항체약물접합체\n---\n# ADC\n",
    "AI.md": "---\ntype: moc\n---\n# AI\n",
    "FOMC.md": "---\ntype: moc\naliases: [FOMC금리]\n---\n",
    "FOMC금리.md": "---\nstatus: deprecated\nmerged_into: topics/FOMC\n---\n",
    "반도체HBM.md": "---\ntype: moc\naliases: [HBM공급망]\n---\n",
    "한.md": "---\ntype: moc\n---\n",
}


def _topics(tmp_path):
    d = tmp_path / "topics"
    d.mkdir()
    for n, c in TOPICS.items():
        (d / n).write_text(c, encoding="utf-8")
    return B.load_topics(str(d))


def _rows(tmp_path):
    return B.rows_from_markdown(DAILY, "2026-10-29", _topics(tmp_path))


def test_canonical_excludes_deprecated_and_merges_terms(tmp_path):
    t = _topics(tmp_path)
    assert "ADC" not in t and "FOMC금리" not in t
    assert {"ADC항체약물접합체", "ADC", "ADC플랫폼"} <= set(t["ADC항체약물접합체"])
    assert "FOMC금리" in t["FOMC"]


def test_row_counts_and_sections(tmp_path):
    rows = _rows(tmp_path)
    secs = [r["section"] for r in rows]
    assert secs == ["top5", "deepdive", "investment", "investment", "companies", "demand"]
    assert [r["id"] for r in rows][:2] == ["2026-10-29-top5-1", "2026-10-29-deepdive-1"]
    assert rows[1]["sector"] == "Macro & Policy"
    assert rows[0]["sector"] == ""


def test_plain_text_stripping(tmp_path):
    r = _rows(tmp_path)[0]
    assert "[[" not in r["title"] and "💊" not in r["title"]
    assert r["title"].startswith("ADC sac-TMT")
    assert "[" not in r["summary"] and "](" not in r["summary"]
    assert "…" not in r["summary"]


def test_urls_and_numbers(tmp_path):
    rows = _rows(tmp_path)
    assert rows[0]["url"] == "https://example.com/a"
    assert rows[0]["urls"] == "https://example.com/a|https://example.com/b"
    assert rows[1]["urls"].split("|") == ["https://example.com/fomc", "https://example.com/c1", "https://example.com/c2"]
    nums = rows[0]["numbers"].split("|")
    assert "HR 0.49" in nums and "190조원" in nums and "+48%" in nums
    assert rows[3]["url"] == ""  # 링크 없는 investment
    assert rows[4]["url"] == "https://example.com/e"


def test_fact_flag(tmp_path):
    rows = _rows(tmp_path)
    assert rows[0]["fact_flag"] == "unverified"
    assert rows[1]["fact_flag"] == ""


def test_topic_matching_alias_and_merged(tmp_path):
    rows = _rows(tmp_path)
    assert "ADC항체약물접합체" in rows[0]["topics"].split("|")   # 합쳐진 이름 ADC 로 매칭
    assert "FOMC" in rows[1]["topics"].split("|")
    assert "반도체HBM" in rows[5]["topics"].split("|")           # HBM공급망 alias, 공백 제거 매칭


def test_ascii_short_word_boundary(tmp_path):
    t = _topics(tmp_path)
    assert B.match_topics("AIDS 백신 관련주", t) == []
    assert B.match_topics("AI 클라우드", t) == ["AI"]
    assert B.match_topics("ADCs 시장", t) == ["ADC항체약물접합체"]
    assert B.match_topics("ADC는 성장", t) == ["ADC항체약물접합체"]
    assert B.match_topics("HBM 4 e", t) == []  # 'HBM' 단독은 별칭 아님(HBM공급망만)
    assert B.match_topics("한", t) == []       # 1글자 용어는 무시


def test_summary_cut_on_word_boundary():
    s = B.clip("가나다 라마바 사아자 차카타", 8)
    assert s == "가나다 라마바" and "…" not in s


def test_write_csv(tmp_path):
    rows = _rows(tmp_path)
    p = tmp_path / "e.csv"
    B.write_csv(rows, str(p))
    back = list(csv.DictReader(open(p, encoding="utf-8")))
    assert len(back) == len(rows) and back[0]["id"] == rows[0]["id"]
