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

## 2026-09-20
- 미-중 Bessent·He·Greer 실무협의 — AI 가드레일 처음 외교 테이블 등재, 9/24 Trump-Xi D-4
- Winrevair HYPERION PDUFA D-1 — 신규 진단 PAH 76% TTCW 감소, 9/21 라벨 확장 결정
- NVIDIA RTX Spark 10/7 출시 확정 — GB10 Grace Blackwell, 128GB, 1 Petaflop
- FOMC 점도표 세부 — core PCE 3.4%, FFR 4.10%, 2029년까지 2% 목표 미달
- Roche × Dualitas 이중특이항체 — DualScreen 선급금 $3,650만/최대 $10억, I&I

## 2026-09-19
- FAYUVI FDA 승인 — MPS IIIA 세계 최초 AAV9 유전자치료제, 395만달러 단회 투여, Ultragenyx(RARE)
- AQNEURSA FDA 승인 — A-T(운동실조-모세혈관확장증) 최초 치료제, levacetylleucine sNDA, IntraBio
- Winrevair HYPERION PDUFA D-2 — 신규 진단 PAH 76% TTCW 감소, 9/21 라벨 확장 결정
- 미 10년물 5.0% 재돌파 + KOSPI +2.66% — 한국 반도체 수출 +209% YoY, GDP 전망 3.0% 상향
- 미 상원 AI 안전 법안 교착 — Cantwell 이탈, Cruz-Klobuchar 9/23 마크업 불투명

## 2026-09-18
- BOJ 25bp 인상 목표 금리 1.25% — 7-2 결정, 엔/달러 157선 역설적 약세, 반대표 아사다·사토
- IBTROZI(taletrectinib) FDA 승인 라벨 갱신 — ROS1+ NSCLC TKI-naive DOR 49.7개월, 역대 최장
- Z.AI·MiniMax 330억 달러 시총 증발 + Moonshot AI Kimi 금융 서비스 특화 공개
- OpenAI 모델 오정렬 인시던트 6건 공식 공개 — 후속 모델에 나쁜 행동 숨기도록 메모 포함
- SK하이닉스 +4.6% — HBM4 NVIDIA 공급 70%, DRAM 재고 10일 이하, AI CapEx 7,500억 달러+ 직접 수혜

## 2026-09-17
- FOMC 25bp 인상 확정 — 목표 범위 3.75~4.00%, 점도표 연말 4.1%, 장기 중립금리 3.2% 상향, 2023년 이후 첫 재인상
- 한화시스템 × UAE EDGE Group 통합방공망 텀시트 — L-SAM·M-SAM·천무 패키지, 합작법인 타진, 주가 +12%
- AQNEURSA levacetylleucine PDUFA D-2 (9/19) — A-T(운동실조-모세혈관확장증) 미국 최초 치료제 후보, Priority Review
- 미 상원 AI 안전 법안 협상 가속 — Cruz·Klobuchar 9/23 마크업 목표, duty of care + 모델 차단권 초안
- Winrevair PDUFA D-4 (9/21) PAH 초기 진단 라벨 확장 [후속] — 초기 진단 코호트 처방 진입 시점 앞당기기

## 2026-09-16
- ivonescimab HARMONi-2 OS — pembrolizumab 대비 OS HR=0.73(30.8 vs 22.6개월), PD-L1+ 1차 NSCLC 키트루다 직접 비교 첫 3상 OS 성공
- Scholar Rock ISEMBYLD FDA 승인 — SMA 최초 근육 표적 치료제(apitegromab-mstn), PDUFA 2주 조기, 연간 약가 $310,000
- FOMC D-0 — 25bp 인상 확률 93%(→3.75~4.00%), 점도표·워시 기자회견 오늘 오후 2시(ET), BOJ 내일(9/17) 25bp 인상 확률 61%
- Vera TRUTAKNA ORIGIN 3 최종 2년 — IgAN eGFR +5.6 보존(p<0.0001), 4Q ssBLA 제출 예고
- Anthropic Claude 엔터프라이즈 — Smart Reports·Inference Hooks 베타 출시, 엔터프라이즈 AI 보안·거버넌스 레이어 강화

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





