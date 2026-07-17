---
type: moc
tags: [AI, AI인프라, 반도체, 투자테마]
timestamp: 2026-06-21T10:20:47+00:00
publish: true
---
# 🗂 AI 인프라 — 주제 지도(MOC)

> 범위: AI 에이전트·LLM 구동에 필요한 하드웨어·소프트웨어·네트워크 인프라 전체 — GPU·CPU·HBM·데이터센터, 빅테크 CapEx, AI 모델 출시 경쟁.
> [AI](/topics/AI.md) 에서 인프라 레이어만 분리한 파일. 모델·서비스 경쟁은 [AI](/topics/AI.md) 참조.

## 핵심 흐름
- **TSMC Q2 AI 인프라 수요 실증(7/17)**: 순매출 $40.2B(+36%), HPC 66%, capex $60~64B. CEO "수요>공급" 직접 확인. 애리조나 2nm 팹 추가 $100B·미국 내 누계 $265B. TSMC 단일 capex 결정이 장비·소재 업체(ASML·TEL·Lam Research·Applied Materials) 2~3년 수주 가시성을 고정하는 구조.
- **capex 상향 후 반도체 섹터 하락**: 2~3년 후 공급 과잉을 시장이 선반영하기 시작한 신호일 수 있다. AI 칩 설계사보다 장비·소재 공급사의 수주 가시성이 더 안정적으로 유지될 수 있는 구간.
- **AI 하드웨어 자립화 경쟁 — OpenAI Jalapeño → Anthropic-Samsung 2nm(7/4)**: 추론 원가 절감이 AI 서비스 가격 경쟁력의 핵심 전장.
- **Google-Anthropic $32억 TPU 임대 CaaS 모델 정착(7/3)**: AI 컴퓨팅 조달 구조가 임대에서 자체 생산으로 이동하는 중간 단계.

## 타임라인
### 2026-07-17 [[daily/2026-07-17]]
- [[daily/2026-07-17]] TSMC Q2 2026 실적 확인 — 순매출 $40.2B(YoY +36%), 순이익 +77.4%, HPC 66%, capex $60~64B, CEO "수요>공급" 발언, 2026 연간 성장 40%+ 상향. 애리조나 팹 추가 $100B·미국 내 누계 $265B. 5분기 연속 분기 최고치
- [[daily/2026-07-17]] capex 상향 직후 반도체 섹터 하락 — 2~3년 후 공급 과잉을 시장이 선반영하기 시작한 신호. AI 칩 설계사보다 장비·소재(ASML·TEL·Lam·Applied Materials) 수주 가시성이 더 안정적일 수 있는 구간 진입 → [[topics/반도체HBM]]

### 2026-07-04 [[daily/2026-07-04]]
- [[daily/2026-07-04]] Google AI 전력 +37% YoY, 2019년 대비 +250% — AI 인프라 확장이 전력망 탈탄소화 속도 공식 추월. DR 1GW 통합·AI 워크로드 피크 이동 자동화 소프트웨어 가동. 역대 최대 연간 증가폭. 데이터센터 전력·냉각 인프라 구조적 수혜 논거 강화
- [[daily/2026-07-04]] Anthropic-Samsung 2nm AI 추론 칩 협상 — AI 하드웨어 자립화 경쟁(OpenAI Jalapeño → Anthropic-Samsung 2nm) 본격화. 추론 원가 절감이 AI 서비스 가격 경쟁력 핵심 전장으로 부상

### 2026-06-22 [2026-06-22](/daily/2026-06-22.md)
- **GPT-5.6 출시 창문 개막, Polymarket 확률 ~40%로 재조정**: 미출시 58% 선두. 1.5M 토큰 컨텍스트 + 정렬 재설계. 공식 발표 없음 — 출처: [TechTimes](https://www.techtimes.com/articles/318799/20260621/gpt-56-launch-window-starts-monday-alignment-fix-15m-token-context-inside.htm) | [Polymarket](https://polymarket.com/event/when-will-gpt-5pt6-be-released) — [2026-06-22](/daily/2026-06-22.md)
- **Claude Fable 5 6/23 크레딧 과금 전환**: 1M 토큰 컨텍스트, 입력 $10/출력 $50(백만 토큰). GPT-5.6·Gemini 3.5 Pro 미출시 상태에서 최상위 공개 모델 상업화 전환 — 출처: [Anthropic 공식](https://www.anthropic.com/news/claude-fable-5-mythos-5) — [2026-06-22](/daily/2026-06-22.md)
- **Gemini 3.5 Pro 6/30 자기부과 기한 대기**: 구글 I/O "6월 중 공개" 약속 대비 Vertex AI 기업 Preview 지속 — 출처: [GrowwingAssistant](https://growwingassistant.com/ai-news/gemini-3-5-pro-release-date-june-2026-every-confirmed-spec-pricing-when-it-drops/) — [2026-06-22](/daily/2026-06-22.md)

### 2026-06-21 [2026-06-21](/daily/2026-06-21.md)
- [2026-06-21](/daily/2026-06-21.md) — Nvidia Vera CPU 양산: AI 에이전트 전용 프로세서, 수직통합 가속
  - 88코어 Olympus, x86 대비 에이전트 태스크 1.8배. OpenAI·Anthropic·SpaceX·Dell 초기 고객
  - SK하이닉스 HBM4E 12단 샘플 조기 출하: 1분기 가이던스 앞당김, 엔비디아 Rubin Ultra 공급 경쟁 선두
  - GPT-5.6 6/22 출시 확률 83%(Polymarket). Gemini 3.5 Pro는 6/30 최후 기한 Preview 상태 지속
  - 한국 5월 반도체 수출 169.4% 급증(371.6억달러): AI 인프라 HBM 수요가 코스피 9,000대 지지

## 연결 주제
- [AI](/topics/AI.md) [반도체HBM](/topics/반도체HBM.md) [반도체](/topics/반도체.md) [한국거시](/topics/한국거시.md) [투자테마](/topics/투자테마.md) [유망기업](/topics/유망기업.md)
