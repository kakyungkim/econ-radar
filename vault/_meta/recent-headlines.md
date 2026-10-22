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

## 2026-10-22
- 한국은행 3.00% 동결 — 7인 만장일치, 점도표 3.25% 시사, 11월 추가 인상 가능성 열어둬
- Tesla Q3 EPS $0.48 beat, FCF $1.53B(약 2조1,100억원) 서프라이즈 — FSD 구독 174만 명(+67% YoY), 순이익 -43% YoY
- ESMO 2026 마드리드 내일 개막 — LBA1 INTerpath-001 mRNA 암백신 Phase 3 HR(10/24), LBA6 SAFFRON EGFR+MET HR(10/25) 첫 공개
- GSK Hibsago(bepirovirsen) FDA PDUFA D-4(10/26) — 만성B형간염 기능적 치유율 19% vs 0%, CHB 패러다임 전환 시험대
- 삼성바이오로직스 PolyPeptide 공개매수 87.92% 성사 — CHF 1.46B(약 2조2,000억원 추정), GLP-1 API CDMO 포트폴리오 진입

## 2026-10-21
- 영국 9월 CPI 3.5%(컨센서스 3.4% 상회) — BOE 11월 25bp 인상 확률 ~80%, 길트 10년물 5.44%(19년 최고)
- Netflix Q3 영업이익률 34.6%(가이던스 33.2% 대비 +140bp), EPS $0.87 상회 — 광고 연간 목표 $3.0B→$2.7B 하향
- SAFFRON NDA FDA 제출 완료 — 오시머티닙+사볼리티닙 EGFR+MET NSCLC Phase 3 PFS+OS 달성, ESMO LBA6(10/25) HR 공개 예정
- 한국은행 기준금리 결정 내일(10/22) — 전문가 11명 전원 동결(현 3.00%), 최종 3.50% 전망 다수
- INTerpath-001 ESMO LBA1 D-3(10/24) — mRNA 흑색종 백신 Phase 3 RFS·DMFS 모두 달성, 세계 최초 치료용 mRNA 3상 HR 수치 첫 공개

## 2026-10-20
- Merck KGaA × Silence Therapeutics 인수 합의 — EV $1.1B(약 1조5,000억원), 130% 프리미엄, GalNAc-siRNA 플랫폼 내재화
- ESMO 2026 LBA 초록 공개 — INTerpath-001 mRNA 암백신·sac-TMT ADC 3건 수치 10/24~26 발표 예정
- Regeneron pozelimab VEXAS 증후군 PDUFA 오늘(10/20) — 결과 미확인, 최초 VEXAS 표적치료제 후보
- GSK bepirovirsen 만성B형간염 기능적 완치 PDUFA D-6(10/26) — CHB 2억5,400만 명 시장 패러다임 전환 시험대
- Netflix Q3 오늘 장후 발표 — 가이던스 $128.6억, 컨센서스 $130.2억, 광고 구독·이익률 개선 확인 분수령

## 2026-10-19
- [후속] 중국 Q3 GDP +4.5% YoY — 컨센서스 +4.4% 상회, AI 수출 견인·내수 부동산 부진 동반
- GSK+Hansoh Ris-Rez(B7-H3 ADC) — 골육종 Phase 3 PFS 달성, ESMO LBA9 10/26 프레지덴셜
- GLP-1 경구 경쟁 — Lilly Foundayo(orforglipron) vs Novo Nordisk 경구 Wegovy 접근성 전쟁
- Pfizer SigVie-002 — NSCLC ADC 전체군 OS 미달, 바이오마커 선별 없는 ADC 설계 교훈
- Netflix Q3 D-1 — 10/20 장후 발표, 가이던스 $128.6억 vs 컨센서스 $130.2억

## 2026-10-18
- HUTCHMED SAFFRON Phase 3 — ESMO D-5, MET+EGFR 내성 NSCLC 첫 글로벌 3상 프레지덴셜 심포지엄 10/24(CICC 목표가 HK$26, NDA 9/29)
- Incyte INCB161734 — 경구 KRAS G12D 억제제, 대장암(10/25 #1007RO)·췌장암(10/26 #3137RO) ESMO 2건 발표
- SK하이닉스 Q3 실적 임박 — HBM4 수익화 첫 공식 확인 시점, 영업이익 추정 70.1~77.9조 원(하나·DS 범위)
- 중국 Q3 GDP — 10/19 오전 발표 예정, 컨센서스 +4.4% YoY(Reuters), 정부 목표 4.5~5.0% 하단 미달 우려
- Iambic Therapeutics(IAM) IPO 첫날 +18% — 공모가 $16→종가 $18.91(단일소스), AI 신약 플랫폼 기관 수요 확인

## 2026-10-17
- ESMO 2026 D-6 — INTerpath-001(Merck+Moderna mRNA 흑색종 백신) HR 수치 10/24 LBA1 첫 공개
- Legend Biotech LB2501 — 세계 최초 이중타깃(CD19/CD20) 체내(in vivo) CAR-T FDA IND 승인
- AstraZeneca-insitro AI 신약 발견 딜 — 선급금 $4,000만, 마일스톤 최대 $14.6억(MASH+심근병증)
- 삼성바이오로직스-PolyPeptide 공개매수 87.9% 응모 완료 — 국내 제약바이오 최대 해외 M&A 연말 종결 목표
- Anthropic 나스닥 IPO 11월 중순 로드쇼 목표 — 밸류에이션 $1.8~2조(복수 매체 보도, 공식 미확인)

## 2026-10-16
- Warsh 연준 의장 IMF 방콕 발언 — 10월 인상 확률 33%→15% 하락, S&P +0.33% ~7,744pt, 10년물 5.08% 안정
- Arrowhead ARO-MAPT Phase 1 — 피하 RNAi BBB 투과 PoC 최초 확인, CSF 타우 -73%(건강인, 105일)
- ImmunityBio Anktiva(N-803) — 방광암 유두종성 NMIBC 확대 FDA 조기 승인(원 PDUFA 2027-01-06보다 3개월 앞)
- ESMO 2026 마드리드 D-8 — Innovent IBI343(CLDN18.2 ADC) LBA77 위암 Phase 3 전체 데이터 10/23, 한국 Ligachem LCB02A도 동일 표적 발표
- 미국 8개 주 AG OpenAI 집단 고소(2026-10-14) — 아동 안전·소비자 기만, AI 기업 상대 최대 규모 주 공동 소송




