"""시장 수치 대조 검사.

2026-10-03, 10-04 호에 7월 기사의 "코스피 8,000", "원/달러 1,530~1,560원대"와 근거 없는 "10년물 4.49%"가 실렸다.
클라우드 세션은 원문 사이트 대부분에 접속하지 못해 사실 검증이 이것을 놓쳤다. 두 가지를 기계적으로 본다.
1. 시장 수치가 나오는 항목에 3주 넘게 지난 날짜의 기사 링크가 붙어 있는가(낡은 링크)
2. 본문의 코스피, 국채 10년물, 원/달러 값이 직전 30일 실제 시세 범위를 벗어나는가(시세 대조)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import check_market_numbers as C

# 2026-09-21 ~ 10-02 실제 종가(FRED DGS10, DEXKOUS / Yahoo ^KS11에서 받은 값)
REFS = {
    "us10y": {"2026-09-23": 4.96, "2026-09-25": 5.17, "2026-09-28": 5.24, "2026-09-29": 5.26,
              "2026-09-30": 5.29, "2026-10-01": 5.24, "2026-10-02": 5.28},
    "usdkrw": {"2026-09-25": 1356.51, "2026-09-28": 1359.78, "2026-09-29": 1355.40,
               "2026-09-30": 1355.91, "2026-10-01": 1364.83, "2026-10-02": 1345.75},
    "kospi": {"2026-09-21": 7007.72, "2026-09-22": 7017.91, "2026-09-23": 7080.92, "2026-09-28": 6889.74,
              "2026-09-29": 6870.81, "2026-09-30": 6838.04, "2026-10-01": 6971.35, "2026-10-02": 7003.74},
}
DATE = "2026-10-04"

STALE = """### [코스피 8,000 전후 — 반도체 어닝스 대기](https://www.koreatimes.co.kr/amp/economy/20260703/kospi-snaps-back-to-8000)
**관전 포인트**: 코스피는 8,000선 전후를 유지 중이다.

### [삼성 Q2 실적 확정](https://www.koreatimes.co.kr/business/20260707/samsung-q2)
**관전 포인트**: 2분기 영업이익은 89.4조원이었다.
"""


def test_stale_link_on_market_item_is_flagged():
    found = C.stale_links(STALE, DATE)
    assert len(found) == 1
    assert "20260703" in found[0]["url"]


def test_stale_link_without_market_number_is_not_flagged():
    assert all("20260707" not in f["url"] for f in C.stale_links(STALE, DATE))


def test_slash_date_url_is_parsed():
    md = "### [미 국채 10년물 4.49%](https://www.briefing.com/bond-market-update/archive/2026/7/20/treasury)\n본문"
    assert len(C.stale_links(md, DATE)) == 1


def test_recent_link_is_not_flagged():
    md = "### [코스피 7,003](https://example.com/news/2026/10/02/kospi)\n본문"
    assert C.stale_links(md, DATE) == []


def _flags(text):
    return [(f["series"], f["value"]) for f in C.check_values(text, REFS, DATE)]


def test_wrong_levels_are_flagged():
    text = ("코스피는 8,000선 전후를 유지 중이다. 미국채 10년물이 4.49%로 내려왔다. "
            "원/달러 환율 1,530~1,560원대에서 하방 요인이 생긴다.")
    got = _flags(text)
    assert ("kospi", 8000.0) in got
    assert ("us10y", 4.49) in got
    assert ("usdkrw", 1530.0) in got


def test_correct_levels_pass():
    text = ("코스피는 10월 2일 7,003.74로 마감했다. 10년물은 5.28%로 마감했고 장중 5.35%까지 올랐다. "
            "원/달러 환율 1,345.75원.")
    assert _flags(text) == []


def test_other_month_reference_is_skipped():
    # 과거 고점을 인용하는 문장은 실제 시세와 다른 게 정상이다
    text = "코스피 6/22 고점 9,114.55 대비 -20.5%. 6월 18일 코스피 9,000선 첫 돌파."
    assert _flags(text) == []


def test_missing_reference_series_does_not_crash():
    got = C.check_values("코스피 8,000", {"kospi": {}}, DATE)
    assert got == []


def test_sources_section_and_background_links_are_not_flagged():
    md = ("## Sources\n- [코스피 7월 기사](https://www.koreatimes.co.kr/amp/economy/20260703/kospi)\n\n"
          "### [삼성전자 Q3 잠정실적 — 코스피 7,000선 유지](https://example.com/2026/10/03/x)\n"
          "Q2 실적은 [Korea Times](https://www.koreatimes.co.kr/business/20260707/samsung-q2) 기준이다.\n")
    # 둘째 블록은 제목에 코스피가 있어 본다. 첫 블록(Sources)은 보지 않는다
    urls = [f["url"] for f in C.stale_links(md, DATE)]
    assert not any("20260703" in u for u in urls)


def test_targets_foreign_bonds_and_market_cap_are_skipped():
    # 2026-09~10월 호에서 실제로 잘못 걸렸던 문장들
    text = ("Goldman Sachs Timothy Moe는 KOSPI 12,000 목표(선행 PER 7.5배)를 유지했다. "
            "영국 10년물 국채(길트·gilts)는 5.44%로 2007년 이후 19년 최고치를 기록했다. "
            "KOSPI·KOSDAQ 합산 시총은 6,022조 원으로 줄었다.")
    assert _flags(text) == []


def test_source_lists_are_not_value_checked():
    text = ("**1차 자료**: [Bloomberg — Goldman KOSPI 12,000](https://www.bloomberg.com/x)\n\n"
            "## Sources\n- [Bloomberg — Goldman Moe KOSPI 12,000](https://www.bloomberg.com/y)\n")
    assert _flags(text) == []
