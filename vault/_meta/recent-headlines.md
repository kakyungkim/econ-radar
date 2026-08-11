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

## 2026-08-08
- [수정] 미 7월 NFP BLS 실제치 -23,000명 — 전일 SIA 추정치(+73K) 방향 반전, S&P 500 신고가 7,757.64(주간 +3.58%) 역방향 랠리
- AMD Taalas 인수(8/6) — AI 추론 특화 칩 스타트업, NVIDIA 범용 GPU 대항 포석, Q4 규제 승인 예정
- Ultragenyx DTX401 PDUFA 8/23 — GSDIa 최초 유전자치료제(AAV8) FDA 결정 임박, Priority Review·BT 지정
- 호르무즈 협상 진전 — 이란-오만 수로 방향 잠정 합의, 공동 성명 최종 초안 단계, 최종 미결
- Mediar Therapeutics-Ono Pharmaceutical 섬유증 항체 공동개발(8/6) — 일본 대형사+미국 바이오텍 발굴 파트너십

## 2026-08-07
- 미 7월 NFP +73K — 컨센서스(FactSet 97.5K) 하회, 2개월 연속 고용 냉각, 연준 9월 25bp 인하 기대 강화
- Replimune TUDRIQEV(RP1+니볼루맙) FDA 가속 승인 — 두 차례 CRL 역전, OV+ICI 최초 병용 허가, ORR 24.2% mDOR 14.1개월
- xAI Grok 4.6 출시 + 수 주 내 Grok 4.7(2.1T) 예고 — ARR 5억달러, 2026년 목표 20억달러
- 이란 호르무즈 봉쇄 초안 — Brent +3.8% $82.49, WTI +2.8% $77.29, 미·이란·오만 3자 협의
- KOSPI 6,258.77(-0.6%) 이틀 연속 하락, SK하이닉스 -4.88%, 주간 -5.0% 7주 연속 하락

## 2026-08-06
- Moderna mFLUSIVA FDA 승인 — 미국 최초 mRNA 독감백신, 50세+ 대상(50~64 정식·65+ 가속), 독감 시장 구도 변화 시작
- Eli Lilly Q2 +48% $23B, Mounjaro $9.9B · Foundayo 경구 GLP-1 첫 분기 $98M, 연간 가이던스 $85~87B 상향
- KOSPI -4.58% 6,296.38, KRX 매도 사이드카 — AMD 마진 미스(-8% 시간 외) 여파, SK하이닉스 -10.37%·삼성전자 -6.3%
- ADP 7월 민간 고용 44K(컨센서스 70K 대폭 하회) — NFP 8/7 D-1, 연준 9월 인하 기대 가열
- Pathos AI + Alphamab JSKN016 TROP2/HER3 이중특이성 ADC 글로벌 라이선스 $22억 — AI 플랫폼이 중국 3상 에셋 직접 인라이선스

## 2026-08-05
- Moderna mFLUSIVA PDUFA 당일 — 미국 최초 mRNA 독감백신 FDA 결정, 한국 시간 수집 기준 결과 미확인
- KOSPI +3.76%(6,598) · S&P 500 신고가 7,736 — SoftBank Cloud+AI +31% 아시아 랠리 파급
- AMD Q2 데이터센터 +107% · EPS 서프라이즈, 시간 외 -8% — 기대 격차 패턴 재확인
- Pfizer Q2 $15.03B 가이던스 상향 + GLP-1 경구제 2건 중단, berobenatide 단일 트랙 수렴
- BMS iberdomide PDUFA D-12(8/17) — 최초 CELMoD 제제 허가 임박, Replimune RP1 결정 지연·8-K 2건


