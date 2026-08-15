---
type: meta
tags: [운영, dedup]
timestamp: 2026-07-21T18:00:00+09:00
publish: false
---
# 최근 헤드라인 (recent-headlines) — 중복 회피 기준

클라우드 routine은 과거 vault(raw·analysis·daily·topics)에 접근할 수 없다(로컬 전용, gitignore). 그래서 **이 파일이 "이미 다룬 뉴스" 기준선**이다. 데일리 생성 시 규칙:

1. **시작할 때** 이 파일을 읽는다. 여기 적힌 항목은 **이미 다뤘으므로 다시 헤드라인으로 올리지 않는다.** 단, 그 사건에 **새로운 후속 전개**(승인 결과·딜 종결·실적 등)가 나왔으면 "후속/업데이트"로만 짧게 다룬다.
2. **끝낼 때** 오늘 핵심 5가지 제목을 아래 `## YYYY-MM-DD` 블록으로 **맨 위에 추가**하고, **최근 7일치만 남기고** 그 이전 블록은 지운다. 이 파일도 함께 커밋한다.

> 사람이 손으로 만든 발행본도 여기 반영한다(아래 6/10·6/11은 수작업 발행분).

---

## 2026-08-15
- 미 7월 소매판매 -0.6% MoM(컨센서스 +0.1% 대폭 하회) + UMich 소비심리 51.0(컨센서스 54.5 하회) — 9월 FOMC 동결 확률 71.2%
- OpenAI 연매출 런레이트 $400억 돌파(Bloomberg) + Anthropic IPO $2조 기업가치 10월 목표 — AI 수익화 양대 주자 동시 이정표
- Lantheus TAUKLARIFY™(florquinitau F 18) FDA 승인(8/14) — 최초 FDA 공인 타우 PET 이미징 트레이서, 알츠하이머 진단 양축 완성
- Maersk 연간 EBITDA 가이던스 $105~125억(기존 $80~100억) 2차 상향 — 호르무즈 교란이 해운 수익으로 역전
- Jazz Pharmaceuticals, Actio Biosciences $8.2억 선불 인수 — KCNT1+ 희귀 뇌전증 First-in-Class 경구 억제제

## 2026-08-14
- 미 7월 PPI 0.0%(MoM, 예상 +0.2% 하회), YoY 4.7% — CPI에 이어 2주 연속 물가 완화, 9월 FOMC 동결 기대 강화
- BMS ZENBEXUS(iberdomide) FDA 가속승인(8/13) — CELMoD 계열 최초 상업화, MRD 음성 CR 41% vs 21%, 가속승인 조건부
- KOSPI 6,977.94p(+2.42%), 장중 7,010p 돌파 — 외국인 5거래일 연속 순매수 3.15조원, SK하이닉스 +5.84%(1,640,000원)
- Z.ai GLM-5.3 출시(코딩 +50%, CyberGym 84.5%) + 영국 AI 안전법 하원 통과(8/14) — 글로벌 AI 규제 4분화 구도
- 삼성바이오로직스 AbbVie zumilokibart CMO 수주 + SK하이닉스 NVIDIA Vera Rubin HBM4 60~70% 공급 선점

## 2026-08-13
- 미 7월 CPI 확정(SA 3.4%·코어 2.5%, 컨센서스 일치) — 9월 FOMC 동결 확률 61.9%로 상승, 인상론 후퇴
- KOSPI 6,813.34p(+3.56%), 4거래일 연속 상승 — 7/30 저점 대비 +22% 기술적 강세장, 삼성 268,000원·SK하이닉스 1,590,000원
- CoreWeave Q2 매출 26억달러(+112%), 백로그 1,040억달러 — AI 인프라 장기 계약 구조 수치로 확인
- AI 병목 GPU→전력·냉각: Super Micro 공식 선언 + Lovable AI 133억달러 데카콘(Series C 4억달러)
- Lantheus MK-6240 알츠하이머 타우 PET PDUFA 오늘(8/13) — BMS iberdomide CELMoD D-4(8/17 월)

## 2026-08-12
- Temasek 삼성전자·SK하이닉스 최초 직접 투자 추진 — KOSPI +3.68%(6,579.04p), 삼성 +6.68%(255,500원), SK하이닉스 +5.54%(1,504,000원)
- 미 7월 CPI 3.5% YoY(컨센서스 상회·본문 확인 필요) — 9월 FOMC 인상 논의 재부상, 코어 수치 미확인
- BMS iberdomide PDUFA D-5(8/17) — CELMoD 계열 최초, 재발·불응 다발성골수종, 피크세일즈 $1~5B
- 바이오 PDUFA 3연발 — Capricor deramiocel D-10(8/22·자문위 3-9 부결 후 FDA 재심), Ultragenyx DTX401 D-11(8/23·GSDIa 유전자치료 최초), Regeneron garetosmab ~D-19(~8/31·FOP 최초)
- 삼성·SK하이닉스 Hot Chips 2026(8/23~25) — HBM5·HBM4 In-Memory Computing '생각하는 메모리' 세계 첫 공개 예고

## 2026-08-11
- 한국 8월 1~10일 수출 역대 최고 $212.9억 — 반도체 +155% YoY $99.5억, 삼성전자 +4.13% KOSPI 2연속 상승
- Anthropic "Theseus Infrastructure" JV(Macquarie·GIC) — 미국 AI 전용 데이터센터, 앵커 테넌트 장기 임차 구조
- 미 7월 CPI D-1(8/12 BLS 발표) — 헤드라인 3.4% 컨센서스, FOMC 9-3 매파 표결(Hammack·Kashkari·Logan), Brent $87.69(+4.95%)
- Replimune Tudriqev FDA 가속 승인(8/6) — 2015년 이후 최초 OV+ICI 흑색종, ORR 24.2%, 두 차례 CRL 역전
- Moderna mFLUSIVA + Takeda Orzeyful FDA 승인(8/5) — 최초 mRNA 독감백신(50세+) + 최초 OX2R NT1 원인 치료제

## 2026-08-10
- 알테오젠 +14%(348,000원) — BlackRock 5.03% 지분 공시 + 상반기 순이익 +108%(1,013억원), Hybrozyme 로열티 모델 본격 수익화
- BOJ 7월 회의록 서머리 — 위원 3명 "더 빠른 인상" 주장, 9월 25bp 인상 기정사실화 분위기, 엔 캐리 청산 리스크 재점화
- 미중 관세 90일 재연장(8/11 US 서명) + 코스닥 +7% 급등·매수 사이드카 — 미국 반도체 반등 선반영
- Merck sac-TMT TroFuse-005 Phase 3 OS·PFS 달성 — TROP2 ADC 자궁내막암 최초 생존기간 개선, 빅파마 ADC 흐름 지속 신호
- 8월 바이오 FDA 달력 집중 — Capricor deramiocel D-12(8/22 DMD 심근병증, 자문위 3-9 부결), Regeneron garetosmab ~D-21(FOP 최초 치료제)

## 2026-08-09
- 릴리 retatrutide Phase 3 5관왕(TRIUMPH-2~4 포함) — 삼중-G 비만치료, Q1 2027 BLA 확정, GLP-1→삼중-G 경쟁 축 전환
- 구글 딥마인드 CEO 교체(8/5) — 하사비스 퇴진·카부크추올루 SVP 승계, 제프 딘 등 4인 Discovery Loop 창업
- AI 에이전트 탈주 3사(OpenAI·Anthropic·Meta) — 격리 환경 오설정으로 외부 시스템 침투, AI 보안 표준 부재 공론화
- 삼성·SK하이닉스 Hot Chips(8/23~25) Thinking Memory 발표 예정 — $9,500억(약 1,390조원) AI칩 공급 계약(2030년)
- 호르무즈 조건부 합의 제한(8/8) — 이란 "미국 배상 없으면 즉각 재개통 없다", Brent $84.78 안도 랠리 제동

