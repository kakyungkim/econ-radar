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

## 2026-10-29
- MSFT Azure +48% CC 서프라이즈 · Alphabet EPS $2.12 미스 — AI 투자 수익화 속도 첫 분기점
- HBM4 시대 공식 개막 — SK하이닉스 OP 83.3조(+632%) · 삼성전자 OP 107.4조(+783%), 합산 190조원
- FOMC 10월 동결 10-2 균열(Cook·Hammack 인상 주장), 12월 인상 OIS 80%
- ESMO 2026 유방암 — iza-bren(BMS/SystImmune) PFS HR 0.41 · ribociclib NATALEE 6년 OS HR 0.809
- Anthropic S-1 제출(Nasdaq 'ANT') — 밸류 최대 $2조, 11월 16일 상장 목표, Nvidia $10B 앵커 협의

## 2026-10-28
- OptiTROP-Lung06(sac-TMT) PD-L1 음성 NSCLC 1차 치료 — ADC+ICI 병합 Phase 3 양성 첫 사례, mPFS 15.0 vs 5.7개월(HR ~0.49), NEJM 게재
- TroFuse-005(sac-TMT) 자궁내막암 2차+ — OS HR 0.68, mOS 19.0 vs 12.1개월(+6.9개월), Lancet 게재, PDUFA 2027/6/15
- FOMC + Alphabet Q3 + Microsoft FY2027Q1 — AI capex ROI 첫 공식 채점(오늘 밤 발표)
- SK하이닉스·삼성전자 Q3 D-1 — HBM4 첫 매출 반영 분기, 내일(10/29) 발표
- ARTEMIS-011(Ris-Rez, B7-H3 ADC) 골육종 Phase 3 — PFS HR 0.33(mPFS 5.5 vs 1.4개월), 희귀 소아·청소년 고형암 ADC 첫 3상 양성

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




