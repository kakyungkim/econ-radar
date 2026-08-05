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

## 2026-08-05
- Moderna mFLUSIVA PDUFA 당일 — 미국 최초 mRNA 독감백신 FDA 결정, 한국 시간 수집 기준 결과 미확인
- KOSPI +3.76%(6,598) · S&P 500 신고가 7,736 — SoftBank Cloud+AI +31% 아시아 랠리 파급
- AMD Q2 데이터센터 +107% · EPS 서프라이즈, 시간 외 -8% — 기대 격차 패턴 재확인
- Pfizer Q2 $15.03B 가이던스 상향 + GLP-1 경구제 2건 중단, berobenatide 단일 트랙 수렴
- BMS iberdomide PDUFA D-12(8/17) — 최초 CELMoD 제제 허가 임박, Replimune RP1 결정 지연·8-K 2건

## 2026-08-04
- Moderna mFLUSIVA(mRNA-1010) PDUFA D-1 — 내일(8/5) 미국 최초 mRNA 독감백신 결판, AdCom 9:0
- 미-이란 평화협상 재개 → WTI -5.97%·Brent -4.68% 급락, 이란 즉각 부인으로 불확실성 잔존
- Amazon 시총 $3T(약 4,170조원 추정) 첫 돌파, Nasdaq +2.1% 빅테크 랠리, Ai4 컨퍼런스 거버넌스 화두
- KOSPI +1.62%(6,358.95) 반등·KOSDAQ +5.88% 3연속 사이드카, 바이오·소부장 투심 이동 지속
- ISM 제조업 PMI 7월 55.6%(예상 54.0 상회), 4년 최고·고용 33개월 만에 확장

## 2026-08-03
- KOSPI -5.12%(6,257.45) vs KOSDAQ +2.44% — 7/31 역대 폭등 직후 차익 실현, 삼성전자 -8.76%·SK하이닉스 -8.79%, 바이오 섹터 로테이션
- Replimune RP1 FDA 최종 결정 오늘 대기 — AdCom 10:3, SEC 공모 준비 포착, 수집 시점 결과 미확인
- Anthropic 10월 나스닥 IPO 추진 — $965B 밸류, ARR $47B, Claude Code 코딩 점유 54%
- Regeneron garetosmab — FOP 최초 치료제 후보, 8월 FDA 결정 임박, HO 병변 최대 94% 감소
- BOK 8/27 금통위 D-24 — 2연속 인상론(신한·씨티·JP모간) vs 10월 연기론 팽팽

## 2026-08-02
- Replimune RP1 PDUFA 8/2 당일 — AdCom 10:3 통과, FDA 최종 결정 대기(수집 시점 미확인), OV+ICI 최초 허가 가능성
- 한국 7월 수출 $98.9B 역대 2위 — 반도체 $41B·+179% YoY, 무역흑자 $30.3B, 2개월 연속 $40B 돌파
- EU AI Act GPAI 집행 발효 + 캘리포니아 SB 942 동시 시행 — 과징금 3%, 챗봇 고지·딥페이크 레이블 즉시 집행
- 빅테크 Q2 CapEx 양극화 — MS/Amazon '수요 연결' 보상(+8%/+10%), Meta/Alphabet '증거 부재' 징벌(-10%/-15%)
- GLP-1 경구제 양강(Lilly Foundayo + Novo 경구 Wegovy) + Medicare $50/월 급여 7/1 시행

## 2026-07-31
- 코스피 +17.91% 역대 최대 단일일 폭등(6,595.45) — 외국인 7.25조원 순매수, Amazon AWS·Microsoft Azure AI 실수요 확인
- Replimune RP1 AdCom 10:3 찬성 — 항PD-1 불응 흑색종 OV 병용, PDUFA 8/2, REPL AH +127%
- Amazon Q2 AWS +37% 18분기 최고·$200.6B 첫 돌파 + Apple 메모리 "100년 홍수" 경고 AH -7%
- 미 Q2 GDP +1.5%(컨센 하회)·PCE +5.1% 가속 — 스태그플레이션 패턴, 9월 인상 72~82%
- OpenAI GPT-5.6 Luna 80% 인하 + EU AI Act GPAI 감독 D-1(8/2 발효)

## 2026-07-30
- Microsoft Azure $100B 돌파(FY2026·+43% YoY) vs Meta Q2 EPS -13.4% 미스 — AI 투자 수익화 경로 분기
- Capricor deramiocel AdCom 9:3 부결 — SAP 버전 충돌(v1.1 vs v3.0), PDUFA 8/22
- 삼성전자 Q2 영업이익 89.5조원·OPM 52% 서프라이즈 + KOSPI 3일 연속 하락(-1.23%, 5,593.56)
- Moderna mRNA-1010 PDUFA 8/5 D-6 — AdCom 9:0 만장일치, 미 최초 mRNA 독감 백신 분수령
- FOMC 3명 인상 이탈표·9월 확률 75~82% + EU AI Act 8/2 GPAI 감독 발효 D-2



