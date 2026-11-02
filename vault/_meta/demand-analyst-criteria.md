---
type: meta
tags: [에이전트설계, 수요렌즈]
timestamp: 2026-06-14T12:22:02+09:00
publish: false
---
# demand-analyst 독립 에이전트 승격 기준

현재(2026-06-13~): **(A) 오버레이** — market-analyst·company-scout 출력에 수요 렌즈 단을 붙이는 방식.
다음 단계: **(C) 독립 에이전트** — demand-analyst가 단독으로 돌고 digest-editor가 4번째 렌즈로 통합.

## 승격 기준 (셋 중 둘 이상 충족 시)

1. **분량이 넘침**: market-analyst·company-scout의 수요 단이 매일 평균 300자를 넘어 두 에이전트의 핵심 분석을 밀어내는 현상이 3일 이상 관찰될 때.

2. **독립 소스가 필요해짐**: 수요 분석을 위해 기존 뉴스 원문과 다른 소스(처방 데이터, 보험 급여 결정, 환자 단체 발표 등)를 별도로 찾아야 하는 케이스가 주 3회 이상 생길 때.

3. **3층 저술에서 수요 데이터를 독립 참조**: trend-synthesizer나 content-writer가 수요 분석만 따로 읽어야 하는 구조가 생길 때 (예: "수요 흐름 리포트" 별도 발행).

## 승격 시 구조
- 에이전트 파일: `.claude/agents/demand-analyst.md`
- 파이프라인: T2 (market-analyst ∥ company-scout ∥ **demand-analyst**) 병렬 → T3 newsletter-editor
- 출력: `vault/analysis/demand-YYYY-MM-DD.md`
- 오케스트레이터 SKILL.md 업데이트 필요

## 판단 시점
- 매주 일요일 주간 동향 루틴 실행 시 improvement-log를 보고 판단.
- 승격 결정 후 이 파일에 날짜와 사유를 기록.

## 현재 상태 로그
- 2026-06-13: (A) 오버레이 시작. demand-lens.md 기준선 완비. 기준 미충족.
