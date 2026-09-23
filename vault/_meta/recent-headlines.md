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

## 2026-09-23
- Claude Opus 5.5 + GPT-6 Sol·Luna 동시 출시 — AI 가격 전쟁 본격화, 토큰 비용 50~80% 인하
- 미·이란 UNGA 3시간 회동 — Trump "11월 딜 가능", Brent $98.55 하락, 사우디 파이프라인 9/26 재가동
- Trump-Xi 정상회담 D-1 (9/24) — 무역 휴전·희토류·AI 3대 의제
- [후속] Merck Winrevair HYPERION 라벨 업데이트 — PAH 신환 조기 치료 근거 공식화 (9/22 승인)
- UN 안보리 AI 세션 — DeepSeek·Altman·Amodei 미중 동석, 미 상원 AI 법안 마크업 9/23

## 2026-09-22
- AMD × OpenAI 6GW GPU 딜 MI450 — NVIDIA 대항 공급망 다변화, ROCm 생태계 첫 대규모 실배포
- 중국 희토류 수출 급감 + Trump-Xi D-2 — 협상 구도 역전, 9/24 정상회담 희토류 이행 조건 분기점
- KOSPI 7,161 (+2.20%) + 삼성·SK하이닉스 800조원($5,200억) 반도체 투자 공약
- UNGA AI 거버넌스 고위급 + DeepSeek UN 안보리 브리핑 — 미·중 불참 속 AI 규범 파편화 우려
- BMS Mavacamten(Camzyos) 청소년 oHCM PDUFA D-8 (9/30) — SCOUT-HCM n=44 근거

## 2026-09-21
- Winrevair(sotatercept) HYPERION FDA 승인 — PAH 신규 진단 세 번째 라벨, TTCW 76% 위험 감소, HR 0.24
- Bessent-He "매우 성공적" + 미중 AI 사고 통보 메커니즘 공식 제안
- KOSPI 7,000 탈환 + 한국 반도체 수출 $341억(+259%) 역대 최고
- Trump-Xi 정상회담 D-3 (9/24) — 무역휴전·AI·희토류 패키지
- Broadcom Q3 AI 칩 $167억(+221%) — ASIC 맞춤칩 모델 구조적 성장 확인

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





