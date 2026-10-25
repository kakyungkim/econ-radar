"""Business English 파싱 계약 검사.

2026-08-13~10-10 발행본 10개에서 괄호 풀이가 굵은 표기 밖에 있어(`**word** (뜻):`)
섹션이 통째로 빠졌다. 두 형식 모두 같은 카드로 읽혀야 한다.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import render_html as R

BASE = """# econ-radar 데일리 — 2026-10-01

## 🗽 Business English

{items}

---
"""

INSIDE = """- **guidance (실적 가이던스)**: 기업이 직접 제시하는 전망.
  - 📝 *Micron guided revenue to $61.5 billion.* → Micron은 매출을 615억달러로 제시했다."""
OUTSIDE = """- **guidance** (실적 가이던스): 기업이 직접 제시하는 전망.
  - 📝 *Micron guided revenue to $61.5 billion.* → Micron은 매출을 615억달러로 제시했다."""


def _eng(md):
    return R.parse_markdown(BASE.format(items=md))["english"]


def test_inside_paren_contract():
    e = _eng(INSIDE)
    assert len(e) == 1 and e[0]["word"] == "guidance" and e[0]["meaning"] == "실적 가이던스"
    assert e[0]["en"] and e[0]["ko"]


def test_outside_paren_reads_same_as_inside():
    assert _eng(OUTSIDE) == _eng(INSIDE)


def test_bold_without_paren_still_parsed():
    e = _eng("- **guidance**: 기업이 직접 제시하는 전망.")
    assert len(e) == 1 and e[0]["word"] == "guidance"
