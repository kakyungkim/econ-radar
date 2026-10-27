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

## 2026-10-27
- FOMC D-1 + Alphabet·Microsoft 어닝스 D-1 — AI capex ROI 첫 번째 공식 채점(10/28 동시 발표)
- Pfizer SigVie-002(IB6 ADC) nsq-NSCLC Phase 3 OS 미달 — ESMO LBA68, 1차 치료 전체 집단 실패
- AZ VOLGA Phase 3 양성 — MIBC EFS HR 0.51(49% 위험 감소)·OS HR 0.58(42% 위험 감소), ESMO LBA2
- SK하이닉스·삼성전자 Q3 D-2 — 10/29 동시 발표, HBM4 첫 매출 반영, SK하이닉스 컨센서스 OP 76.96조원
- Merck·Kelun-Biotech sac-TMT ESMO 3중 — TroFuse-005(자궁내막암)·Lung04 Final OS·Lung06(NSCLC 1차)

## 2026-10-26
- SAFFRON LBA6 전체 데이터 + SANOVO LBA69 — 사볼리티닙+오시머티닙 EGFRm NSCLC 2차(PFS 45% 감소/OS 32% 감소, NEJM) + 1차(PFS HR 0.56, 중앙 24.9개월) Phase 3 동시 확증
- GSK Hibsago(bepirovirsen) FDA 승인(10/20) — 세계 첫 만성 B형 간염 ASO 기능적 완치 치료제, 완치율 19% vs 0%
- Krascendo-1(divarasib) KRAS G12C head-to-head Phase 3 — PFS HR 0.58/OS HR 0.56 vs 소토라십·아다그라십
- Anthropic IPO 11월 임박 — 목표 밸류에이션 $2조, Nvidia 최대 $100억 투자 협의
- FOMC D-2 + 빅테크 어닝스(Alphabet/Microsoft 10/28) + SK하이닉스 Q3(10/29) — 이번 주 Q4 방향 결판

## 2026-10-25
- SAFFRON LBA6 — 사볼리티닙+오시머티닙 EGFR+MET NSCLC Phase 3(N=338) PFS+OS 달성, 오늘 저녁 ESMO 전체 HR 공개, FDA NDA 제출
- Incyte INCB161734 CRC 1상 데이터 ESMO 첫 발표 + Incyte-Genmab 1L CRC Phase 1/2 협력
- Ris-Rez(B7-H3 ADC) 골육종 ARTEMIS-011 Phase 3 PFS 달성, 내일 LBA9 전체 데이터
- SK하이닉스 Q3 실적 D-4 — 컨센서스 76.9조원, HBM4 첫 매출 반영, 10/29 발표
- 빅테크 어닝스 위크 D-3 — Alphabet Q3 컨센서스 $128B·Google Cloud 성장 연속성, FOMC 동결 유력(10/28)

## 2026-10-24
- INTerpath-001 Phase 3 ESMO LBA1 — mRNA 흑색종 백신 RFS HR 0.58(p<0.001), DMFS HR 0.62(p=0.002), NEJM 동시 게재, 세계 최초 mRNA 항암백신 Phase 3 성공
- DeLLphi-305 LBA3 — 타를라타맙+더발루맙 ES-SCLC 1차 유지요법 Phase 3 OS·PFS·ORR 달성
- IBI343 G-HOPE-001 OS HR 0.57 확인 [후속] — CLDN18.2 ADC 위암 3차 치료 mOS 10.2 vs 6.9개월
- 빅테크 어닝스+FOMC D-4 — Alphabet·Microsoft·SK하이닉스 Q3(10/28), PCE·GDP Q3(10/29)
- HLB 리픽투(Lyrfigtu) — FGFR2 담관암 FDA 승인(9/23), 국산 첫 항암 신약 직접 NDA, Q4 미국 출시

## 2026-10-23
- GSK Hibsago(bepirovirsen) FDA 승인(10/20) — 만성B형간염 기능적 완치율 19% vs 0%, CHB 첫 기능적 치유제 탄생
- Innovent IBI343 ESMO LBA77 위암 Phase 3 PFS 충족 — Takeda $11.4B 글로벌 파트너십, 계약금 $1.2B 확인
- INTerpath-001(intismeran autogene) ESMO LBA1 내일(10/24) — mRNA 흑색종 백신 Phase 3 RFS·DMFS 달성
- Meta Q3 2026년 capex 가이던스 $135~145B 상향 — AH -11%, AI 투자 ROI 타임라인 시험대
- FOMC D-5(10/28) — 현행 기준금리 3.75~4.00% 동결 전망, Warsh 의장 금리 경로 발언 예정

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


