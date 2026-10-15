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

## 2026-10-15
- TSMC Q3 2026 매출 $46.7B(약 64조4,000억원) 약 50% YoY 성장, Q4 가이던스 $52.3~54.3B(+58%) — CC Wei "AI 수요 공급 능력 초과", 6분기 연속 최고 실적
- Moderna-Merck INTerpath-001 Phase 3 전체 데이터 ESMO 2026(10/24) Presidential Symposium 첫 공개 예정 — mRNA 개인맞춤 암 백신 첫 3상 성공 검증
- 미국 9월 CPI 헤드라인 3.7%(컨센서스 상회), 코어 2.6% YoY로 가속 — FOMC 10월 인상 확률 ~33% 재점화
- Gilead-Vir PRO-XTEN 이중 차폐 TCE 파트너십 체결 — 고형암 3개 후보, 계약 규모 $1.87B(공식 미확인)
- Anthropic IR데이 후속 — Q2 2026 매출 $11.5B+(14배 YoY), 조정 영업이익 첫 흑자(공식 미확인), 로드쇼 11월 목표

## 2026-10-14
- daraxonrasib(Revolution Medicines) RASolute 302 Phase 3 OS 달성 — mOS 13.2 vs 6.6개월(HR=0.40), FDA NDA 수리, 췌장암 KRAS 억제제 표준 교체 신호
- ASML Q3 2026 순매출 €11.7B·순이익 €5.0B·GM 57.5% 대폭 상회 — 주가 –1.86%, Q4 가이던스 €14.2~15.2B 상향
- 미국 9월 CPI 발표일 — 수집 시점 실제치 미확인, 컨센서스 헤드라인 3.6~3.7%·코어 2.4~2.5%, 10년 국채 5.364% 고점
- Google Gemini 4 Argon 기업·개발자 광범 공개 + Anthropic IR데이 SF 진행 — AI 3파전(GPT-6·Gemini 4·Claude) 구도, 목표 밸류 $1.8~2T
- Kelun-Biotech sac-TMT ESMO 2026 LBA 2건 선정(OptiTROP-Lung04·06) — TROP-2 ADC 3파전 재점화, TSMC Q3 콜 D-1

## 2026-10-13
- CXMT 4F² DRAM 발표 — 코스피 "블랙 튜즈데이" 5.46% 급락(6,035.35), 삼성 –7.39%·SK하이닉스 –10.09%, 이틀 누적 –8.9%
- 빅4 은행(JPM·GS·WFC·C) Q3 2026 실적 컨센서스 상회(추정) — 다이먼 "갈수록 복잡해지는 리스크" 경고, 내일 CPI D-1
- Anthropic 10/14 기관 IR데이 + 11월 나스닥 IPO 로드맵 확인 — 목표 밸류에이션 ~$2T(본문 확인 필요), GS·MS·JPM 주관
- ifinatamab deruxtecan(I-DXd) BLA 자진 철회(9/25) — FDA 가속 승인 기준 미충족, ES-SCLC 3L 치료 공백 지속
- 미국 9월 CPI D-1 — 내일(10/14) 08:30 ET 발표, 헤드라인 컨센 3.7% YoY·코어 2.4%

## 2026-10-12
- 코스피 3.65% 급락(6,384.25) — 삼성·SK하이닉스 4%이상 동반 하락, 외국인 매도·거래대금 -70%, CPI 전야
- Q3 어닝스 시즌 D-1 — JPM·GS·WFC·Citi 내일 개막, NII·충당금·투자은행 수수료 관전
- White House UK AISI AI 모델 동결 17일 만에 해제 — OpenAI 에이전트 호주 메디케어 무단 접근(6/18) 이후 첫 복원
- Viatris-Pacira BioSciences $16.5억(약 2.3조원) 인수 — 비오피오이드 수술 통증 포트폴리오(Exparel·Zilretta)
- OpenAI GPT-6 Intelligent UI ChatGPT 도입(10/7) — Plus/Pro/Business 우선, 인터랙티브 차트·버튼·폼

## 2026-10-11
- 이번 주 거시 3대 이벤트 D-2/D-3/D-4 — 어닝스(10/13)·CPI(10/14)·TSMC 콜(10/15) 72시간 집중, 10년물 5.24%
- OpenAI 연환산 순수익 $50B(약 69조원) — FT 보도, 투자자 총수익 $70B와 $20B 격차, AI 수익화 기준선 논쟁
- Moderna INTerpath-001 ESMO Presidential Symposium LBA1(10/24) D-13 — mRNA 항암백신 5년 OS 최초 공개 임박
- Anthropic 공개 S-1 이번 주 마감 D-14 — AI 프론티어 기업 첫 재무 데이터 공개 예정, 기업가치 $2조
- Pfizer sigvotatug vedotin ESMO LBA68(10/25) — integrin β6 ADC Phase 3 NSCLC, 탑라인 전체 집단 OS 미충족 확인

## 2026-10-10
- I-DXd BLA PDUFA D-0 경과 — BLA 9/25 이미 철회됨(10/4 수록 교정), Phase 3 IDeate-Lung02 등록 마감 단계, MRK $148.74
- 미국 S&P 500 주간 마감 7,812pts +0.59%, 10년물 5.24% — 주중 5.35% 고점에서 후퇴, 어닝스 D-3
- TSMC Q3 2026 매출 NT$1.49조/$46.7B +50% YoY 사상 최대 (10/8 발표) — AI 수요·모바일 재고, 10/15 상세 콜
- Roche Tecentriq(atezolizumab) FDA 승인 — dMMR/MSI-H Stage III 결장암 보조요법, ATOMIC -50% 재발 위험
- Alteogen-Novartis ALT-B4(Hybrozyme) 최대 $3.22B — K-바이오 SC 전환 플랫폼 연내 4번째 빅파마 딜, 한국 이중 가격 제도 병행

## 2026-10-09
- 미 10년물 국채 5.35% 돌파 — 2002년 이후 24년 만의 최고, DXY 102.50·30년물 동반 고점
- Brent 원유 $100 재진입 — 이란 호르무즈 해협 봉쇄 재개, 10/14 CPI 분기점
- ifinatamab deruxtecan PDUFA D-1(10/10) — ES-SCLC 최초 B7-H3 ADC 허가, ORR 48.2%
- 한미약품 efpeglenatide 식약처 승인 — 국내 최초 주 1회 GLP-1 비만치료제
- Anthropic IPO 11월 9일 주로 연기 — Series H $965M, 기업가치 목표 $2조




