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

## 2026-09-08
- WCLC 2026 서울 D-4 — AZ Tagrisso 8년 OS vs J&J MARIPOSA HR 0.75(42개월 OS 56% vs 44%), EGFR 1차 치료 표준 대결
- MSD+Gilead KEYNOTE-D46/EVOKE-03 중단 — TROP2 ADC+PD-1 병용, NSCLC 1차 치료 Phase 3 실패, ADC+IO 전략 첫 대형 벽
- Ultragenyx UX111 PDUFA D-11(9/19) — 산필리포 A형(MPS IIIA) 최초 AAV9 유전자치료제, BLA 재제출 수락
- BOJ 9/17~18 25bp 인상 유력 — 엔 캐리 언와인딩·KOSPI 선물 만기(1.7조) 수급 변동성, Goldman KOSPI 12,000 유지
- Daiichi Sankyo+MSD I-DXd(ifinatamab deruxtecan) — SCLC 2차 치료 B7-H3 ADC, PDUFA 10/10, WCLC 데이터 공개

## 2026-09-07
- Revolution Medicines Rasonque(daraxonrasib) FDA 승인(8/26) — 세계 최초 pan-RAS GTPase 억제제, 전이성 췌장선암(KRAS G12X 등 전 변이), NGS 동반진단 불필요
- BMS Zenbexus(iberdomide) FDA 가속 승인 — 첫 CELMoD 계열, RRMM, MRD 음성 CR 대리지표 최초 채택
- Nvidia Hugging Face $12.93B 인수 — GPU 공급자→AI 플랫폼 운영자, 1.8M+ 개발자·모델·데이터셋 생태계
- FOMC 인상 확률 38%→56~66% + CPI D-4(9/11) — Warsh 강경론(8/28), 이란 탄도미사일 발사·WTI $90+ 유가 변수 동시
- WCLC 2026 D-5(9/12개막) + AZ-Dizal EGFR $1.5B + zilurgisertib PDUFA D-19(9/26)


