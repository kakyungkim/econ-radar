"""주간 리포트의 근거 표기 계약 검사.

리포트 md는 옵시디언용 [[daily/DATE]] 위키링크로 근거를 단다. 공개 HTML에서는 이것이 괄호째 글자로 보였다.
블로그에서는 문장 안의 데일리 위키링크를 그날 데일리로 가는 짧은 날짜 링크로 바꾸고,
흐름 머리의 "근거 노트:" 줄과 끝의 "## 재료 출처" 절은 뺀다. 공개되지 않는 노트(topics, analysis) 링크는 지운다.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import render_weekly as W


def _html(md):
    return W.md_to_html(W.clean_evidence(md))


def test_inline_daily_becomes_date_link():
    out = _html("영업이익 83.3조원을 기록했다([[daily/2026-10-29]]). 다음 문장.")
    assert "[[" not in out
    assert '<a href="/econ-radar/2026-10-29.html">10/29</a>' in out
    assert "기록했다(" in out and ">10/29</a>)." in out


def test_adjacent_daily_links_are_joined():
    out = _html("일정을 구체화했다([[daily/2026-10-29]][[daily/2026-10-31]]).")
    assert '>10/29</a>, <a href="/econ-radar/2026-10-31.html">10/31</a>)' in out


def test_bare_trailing_daily_gets_parens():
    out = _html("추세가 관찰됐다. [[daily/2026-10-05]]")
    assert out == '<p>추세가 관찰됐다. (<a href="/econ-radar/2026-10-05.html">10/5</a>)</p>'


def test_daily_inside_existing_parens_adds_no_parens():
    # W35 실제 문장. 괄호를 하나 더 열면 "($3.87B, (8/27)"처럼 짝이 깨진다.
    out = _html("인디애나 착공($3.87B, [[daily/2026-08-27]]) 소식.")
    assert out == '<p>인디애나 착공($3.87B, <a href="/econ-radar/2026-08-27.html">8/27</a>) 소식.</p>'


def test_evidence_header_line_is_dropped():
    md = "## 흐름 1 — 거시\n\n근거 노트: [[daily/2026-10-05]] · [[daily/2026-10-08]] · [[analysis/market-2026-10-08]]\n\n본문이다."
    out = _html(md)
    assert "근거 노트" not in out and "[[" not in out
    assert "<p>본문이다.</p>" in out


def test_source_section_is_dropped():
    md = "## 다음 주 지켜볼 것\n\n- CPI\n\n---\n\n## 재료 출처\n\n[[daily/2026-10-05]] · [[daily/2026-10-06]]\n"
    out = _html(md)
    assert "재료 출처" not in out and "[[" not in out
    assert "<li>CPI</li>" in out
    assert not out.rstrip().endswith("<hr>")


def test_unpublished_wikilinks_are_removed():
    out = _html("추세가 관찰됐다. [[topics/RNA치료제]]")
    assert out == "<p>추세가 관찰됐다.</p>"


def test_idempotent():
    md = "기록했다([[daily/2026-10-29]]).\n\n근거 노트: [[daily/2026-10-29]]"
    once = W.clean_evidence(md)
    assert W.clean_evidence(once) == once


def test_plain_text_for_push_keeps_date():
    # 텔레그램·메일 평문에도 빈 괄호 "()"가 남지 않아야 한다.
    txt = W._plain(W.clean_evidence("기록했다([[daily/2026-10-29]])."))
    assert txt == "기록했다(10/29)."
