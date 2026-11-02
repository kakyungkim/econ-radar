"""주간 메일의 흐름 제목 파싱 계약 검사.

계약은 `## 주요 흐름` 아래 `### 흐름 N: 부제`인데, W32~W43 리포트는 전부 `## 흐름 N — 부제`로
쓰여 메일과 텔레그램의 흐름 목록이 매주 0개였다. 두 형식 모두 같은 제목 목록으로 읽혀야 한다.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import render_weekly as W

CONTRACT = """# W43 동향

## 주요 흐름

### 흐름 1: ESMO 2026
본문

### 흐름 2: RNA 치료제
본문

## 투자 시사점
"""

H2 = """# W43 동향

## 흐름 1 — ESMO 2026
본문

## 흐름 2 — RNA 치료제
본문

## 투자 시사점
"""


def _flows(md):
    return W.parse_weekly({}, md, "2026-W43")["flow_titles"]


def test_contract_format():
    assert _flows(CONTRACT) == ["ESMO 2026", "RNA 치료제"]


def test_h2_format_matches_contract():
    assert _flows(H2) == _flows(CONTRACT)


def test_h2_with_colon():
    assert _flows(H2.replace(" — ", ": ")) == ["ESMO 2026", "RNA 치료제"]
