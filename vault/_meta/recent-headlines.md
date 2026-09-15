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

## 2026-09-15
- WCLC 2026 최종일 — B7H3 ADC 2종(ARTEMIS-008·TAISHAN-302) 재발 SCLC 3상 OS HR 0.46 동시 달성, 수십 년 토포테칸 표준 교체 근거
- ADAURA 8년 OS — osimertinib 조기 NSCLC 보조요법 79% vs 위약 64%(HR 0.52), 역대 최장 추적 생존 이득 확인
- FOMC D-1 + BOJ 대기 — 미 10년물 5.02%(2007년 이후 최고), KOSPI -0.85%(6,627), 원화 1,359원, 48시간 내 이중 금리 결정
- REZILIENT3 — zipalertinib EGFR exon 20 삽입변이 NSCLC 1차 PFS HR 0.50 (P=0.00015), 경구 TKI 3상 근거 확립
- ARROS-1 — zidesamtinib ROS1+ NSCLC TKI-naive ORR 94%·두개 내 ORR 100%, ROS1 분자아형 표준 선점

## 2026-09-14
- J&J MARIPOSA 아시아 OS — amivantamab+lazertinib 사망위험 26% 감소(HR 0.74), EGFR 변이 NSCLC 이중표적 최초 OS 통계 유의 우위
- DESTINY-Lung04 — T-DXd HER2 변이 NSCLC 1차 PFS 14.3 vs 8.3개월, ADC가 면역항암제+화학요법 압도한 첫 Phase 3
- 유가 Brent $107 + FOMC D-2 인상 확률 80~87% — 사우디 파이프라인 드론 피격·호르무즈 협상 연기, 에너지-물가-긴축 삼각 루프
- KOSPI -3.26%(6,684) + 원화 1,347원 — 외국인 3.3조 순매도, 시총 한달 212조 소멸
- Scholar Rock apitegromab PDUFA D-16(9/30) + Merck Winrevair PDUFA D-7(9/21) — 두 PDUFA 정상 심사 궤도

## 2026-09-13
- FOMC D-3: 미·영 국채 수십 년래 최고(미 10년물 4.96%, 영국 30년물 5.89%) — '더 오래 높게' 구조 재진입 신호
- WCLC 2026 MAVERICK 3상 — PCI 40년 SCLC 표준 종식, MRI 단독 OS 비열등+인지력 손상 없이 생존 HR 0.60
- AbbVie WCLC 2026 — 편평 NSCLC 이중특이항체 ABBV-1480 ORR 90%, SCLC ADC ABBV-706 ORR 82% 동시 공개
- AriBio AR1001 — 한국 주도 글로벌 알츠하이머 3상 탑라인 9~10월 공개, 경구 GLP-1RA 계열 PoC 기로
- K-뷰티 APR·Silicon2 -20% 급락 vs 한국 GDP 3.0% 상향 — 수출 통계 오류+원화 강세 기술적 충격

## 2026-09-12
- WCLC 2026 개막 — J&J MARIPOSA 3년 OS 60% vs osimertinib 51%, EGFR+ NSCLC 1차 치료 OS 우위 첫 공식 확인
- FOMC D-4 — CPI 2.5% 이후 PPI+코어로 인상 확률 71% 재전환, 미 10년물 4.96%
- 한국 9월 초순 수출 $350억 +83% YoY — 반도체 $165억 +270%, 역대 최고, AI CapEx $7,240억 직접 수혜
- Telix Pixclara FDA 2차 CRL — 교모세포종 PET 진단제 연속 거절, 테라노스틱스 규제 리스크 재부각
- WCLC 2026 ADC 파이프라인 — BioNTech ADC×IO 첫 글로벌 데이터, 유한양행 YH42946 최초 임상 공개

## 2026-09-11
- 미국 8월 CPI 2.5% YoY (컨센서스 2.9~3.4% 대폭 하회) — FOMC 9/16 25bp 인하 기대 급등
- 유가 Brent $108 고점 — 사우디 산유량 급감 + 이란 확전, $120 꼬리 리스크 부상
- Telix Pixclara FDA PDUFA D-0 (9/11) — glioma PET 이미징 미국 첫 진단제 결정
- OpenAI Agents API 공개 베타 + Microsoft 38GW 데이터센터 계획 — AI 인프라 플랫폼 경쟁
- Merck Winrevair HYPERION 76% + WCLC 2026 서울 D-1 — PAH·폐암 데이터 맞춤발

## 2026-09-10
- WCLC 2026 D-2 — MAVERICK SCLC OS 첫 공개(9/12), Tagrisso 8년 OS vs MARIPOSA EGFR 1차 치료 구도 본격화
- Brent $101.25 돌파 — 미군 이란 유조선 5척 격침, CPI D-1 전날 에너지 충격
- Scholar Rock apitegromab PDUFA D-20(9/30) — 9/9 CMC(Catalent OAI) 이슈 해소, SMA 근육 표적 심사 재개
- Nvidia Vera Rubin Goldman 컨퍼런스 — CSP 5개사 납품 시작, Q3 데이터센터 매출 20% 기여 전망
- K바이오 딜 써밋 2026 + 알테오젠 Novartis $3.22B(약 4조3,000억원) — 빅파마 23개사 특허절벽 수혜 탐색

## 2026-09-09
- KOSPI 7,051.64 (+1.40%) — 배터리·석화 동반 급등으로 33거래일 만에 7,000 탈환
- Mistral AI €3B(약 3조3,000억원) 삼성전자 주도 시리즈 D — 유럽 기술 역대 최대 에퀴티 라운드, 소버린 AI 테마
- Merck Winrevair PDUFA D-12(9/21) — HYPERION 새로 진단된 WHO FC II~III PAH 1차 치료 확장 카운트다운
- Ionis ZANVASTRO(zilganersen) 9/3 FDA 승인 — Alexander disease 첫 질환 수정 치료제, ASO 플랫폼 희귀신경질환 첫 상업화
- 유한양행 YH42946 WCLC 2026 서울 D-3 — HER2·EGFR 엑손20 이중 경구 TKI 첫 임상 데이터

