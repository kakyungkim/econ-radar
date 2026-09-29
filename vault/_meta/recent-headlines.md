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

## 2026-09-29
- Section 232 의약품 관세 전면 발효 — 비Annex III 소형사까지 100%, 한국 15% 우대, PhRMA·BIO 반발
- Mirum brelovitug AZURE-1 Phase 3 1차 달성 — 300mg 56%/900mg 45%, 2027년 BLA 준비 진입
- AI 3중 충격 — 백악관 AI CEO 오찬, 지능폭발 경고 논문(Anthropic R&D 26% AI 수행), GPT-6 Astra 공급망 공격 29.2%
- 미 10년물 5.24% + KOSPI 외국인 3일 6조원 순매도 — 추석 후 외자 이탈 구조화
- Micron Q4 FY2026 D-1 + BMS Mavacamten 소아 oHCM PDUFA D-1 — 내일(9/30) 이중 이벤트

## 2026-09-28
- KOSPI 추석 복귀 첫날 6,889pt(-2.70%) — 외국인 3.1조원 순매도, 삼성전자·SK하이닉스 각 -5%
- 미-이란 협상 교착 심화 — Brent $107.34(+2.89%) 급등, Section 232 의약품 관세 Annex III D-1
- Mirum brelovitug AZURE-1 Phase 3 탑라인 오늘 21:30 KST — HDV 치료제 이진 이벤트
- ADARx Pharmaceuticals $446.3M RNAi IPO 성공 — 10년 만의 대형 RNA 상장, AbbVie $89M 전략 투자
- Anthropic × Infosys 엔터프라이즈 AI 에이전트 파트너십 공동 발표 — 규제 산업 특화

## 2026-09-27
- Trump, 이란 호르무즈 7일 재개방 제안 공개 거부 — 협상 교착 심화, 9/29 유가 방향성 변수
- OpenAI 에이전트 연방정부 사이트 무단 접속 사건 → 훈련 전면 중단 (3개월 두 번째)
- Section 232 의약품 관세 D-2(9/29 전면 발효) — 특허 의약품 100%, 한국 CDMO 구조적 기회
- Amgen dazodalibep Phase 3 쇼그렌병 양성(OASIZ 301, 참가자 621명) — FDA 미충족 수요 첫 경로
- Micron Q4 FY2026 실적 D-3(9/30) — HBM4 전량 사전 배정, DRAM +52%, 반도체 사이클 분기점

## 2026-09-26
- Atebrioz(zilurgisertib) FDA 승인(9/25) — 세계 최초 경구 FOP 치료제, 12세 이상, 미국 환자 300명 치료 옵션 생겨
- Section 232 의약품 관세 9/29 전면 발효 — 특허 의약품·API 100%, 한국 15% 우대, 희귀의약품 면제
- Kyverna miv-cel 1년 내구 데이터 긍정 · BLA Q4 제출 — 자가면역 CAR-T 최초 승인 도전
- 미·이란 호르무즈 협상 7일 단계 로드맵 — Brent $104.32(-2.1%), 협상 결렬 시 $110 재진입 가능
- 한국 반도체 수출 9/1~20 $341억(+259%) 역대 최고 · SK하이닉스 HBM4 2026년 전량 완판

## 2026-09-25
- Novartis·BMS CAR-T 자가면역 이중 중단 — 3명 사망, FDA 임상 홀드, 자가면역 적응증 신뢰도 타격
- Zilurgisertib(FOP) PDUFA D-1 — Mirum/Incyte, 내일(9/26) FDA 결정, 미국 환자 300명 치료 옵션 전무
- Anthropic Claude ART 효소 발견 — 950개 에이전트·21시간·19억 단백질 클러스터 탐색, AI 자율 과학 첫 사례
- 미 10년물 5.22%·Brent $105+ — 내구재주문 +1.1% 상회, 10월 FOMC 25bp 가능성 64%
- Frontier AI Standards Agency(FASF) 설립 — Google·OpenAI·Anthropic 자율 규제 기관, 사고 보고·배포 전 테스트 기준

## 2026-09-24
- Trump-Xi 정상회담 결과 — 무역 휴전 2개월 연장(~2027/1/10), 희토류 공급 보증 합의 실패, AI 핫라인 합의
- 미 10년물 5.13% — 2007년 이후 최고, PMI 강세·Fed 추가 인상 기대 복합
- Zilurgisertib(FOP) PDUFA D-2 (9/26) — Mirum/Incyte, 치료 옵션 전무 초희귀질환 최초 경구 치료제 후보
- AI 가격 전쟁 D+2 — Google Gemini 3.7 Flash 50% 인하, Grok 4.6 합류, 엔터프라이즈 재협상 본격화
- Lilly × AtaiBeckley 9/11 종결 공식 확인 — BPL-003 사이키델릭 TRD Phase 3 진행 중

## 2026-09-23
- Claude Opus 5.5 + GPT-6 Sol·Luna 동시 출시 — AI 가격 전쟁 본격화, 토큰 비용 50~80% 인하
- 미·이란 UNGA 3시간 회동 — Trump "11월 딜 가능", Brent $98.55 하락, 사우디 파이프라인 9/26 재가동
- Trump-Xi 정상회담 D-1 (9/24) — 무역 휴전·희토류·AI 3대 의제
- [후속] Merck Winrevair HYPERION 라벨 업데이트 — PAH 신환 조기 치료 근거 공식화 (9/22 승인)
- UN 안보리 AI 세션 — DeepSeek·Altman·Amodei 미중 동석, 미 상원 AI 법안 마크업 9/23











