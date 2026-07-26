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

## 2026-07-26
- FOMC D-3 + 빅테크 어닝즈 주 — 인상 확률 35% 급등, 7/29 MS·Meta·Q2 GDP·Apple·Amazon 72시간 밀집
- centanafadine SIMTRIYO FDA 승인 — 최초 NDSRI 계열 ADHD 신약, 6세 이상 전 연령, 24년 만의 새 기전
- Capricor deramiocel + Replimune RP1 AdCom 7/29 D-3 — DMD 세포치료·흑색종 OV 이진 이벤트 동시 밀집
- Kimi K3 오픈웨이트 공개 임박 — 7/27 00:00 UTC, 2.8T MoE, 데이터 주권 논점 부상
- Brent $97~100 고착 + 코스피 7/27 재개 — CENTCOM 14연속 이란 공습, 7월 누적 -23% 베어마켓

## 2026-07-25
- Claude Opus 5 출시 — FrontierBench SOTA 43.3%, Fable 5 절반 가격, 에이전틱 AI 가격전쟁 본격화
- 코스피 약 +5.8% 급반등 — 반도체 쇼트 스퀴즈, 외국인 연속 매수, FOMC D-4
- Replimune RP1 AdCom D-4(7/29) — PDUFA 8/2, 반응군 OS 83.5%, 브리핑 서류 7/27~28 공개
- Brent $97~100 구간 + FOMC 7/29 — 유가 고착이 연준 선택지를 좁힌다, CME FedWatch 동결 ~63-65%
- HLB 리보세라닙 완제공장 CAPA 7/25 제출 — DS VAI 해소 후 마지막 제조 관문

## 2026-07-24
- Brent $100.69 돌파 — 이란 IRGC 호르무즈 "완전 통제" 선언, Goldman $120 경보
- 코스피 -5.72% 6,690 매도 사이드카 — 유가·관세·금리 3중 충격, 외국인 1.75조 이탈
- HLB 리라퓨그라티닙 LCM 완료 "이견 없음" — PDUFA 9/25 순항, FGFR2 담관암
- centanafadine PDUFA 오늘(7/24) — NDSRI 최초 ADHD 신약, FDA 결정 대기 중
- Alphabet Q2 Google Cloud +82% $24.8B — capex $205B 상향

## 2026-07-23
- 한국 Q2 GDP +0.6% QoQ(전망치 3배), 코스피 7,096.89(+4.40%) 7,000선 재탈환 — GDI +15.6% YoY 38년 최고, 외국인 2.1조 순매수
- Brent $96.24(+2.37%) 5일 연속 상승 — 후티 사우디 유조선 Encelia·Layla 미사일·드론 공격, 7/21 대비 +$7.68
- 삼성바이오에피스-인투셀 SBE303 ADC 상업화 본계약 — Nectin-4 표적, OHPAS 링커, 글로벌 1상 149명 진행 중
- BridgeBio encaleret NDA FDA 수락 — ADH1 최초 표적치료제 후보, PDUFA 2027-05-08, AdCom 없음
- Google Gemini 3.6 Flash 출시 — 출력 단가 $7.50/M(-17%), DeepSWE 49%, GitHub Copilot 통합

## 2026-07-21
- 코스피 V자 반등 +3.56%(6,747.95) — 반도체 수출 역대 최고·삼성 RX 로봇 이중 촉매, 외국인+기관 약 2.2조 순매수
- 코오롱 그룹주 4종 하한가(-29.9~30%) — TG-C Study 1 실패 시장 반응, 코오롱티슈진 42,900원, 10월 Study 2가 분기점
- 삼성전자 RX(Robotics eXperience) 사업부 CEO 직속 신설 — 전현대차 이동건 수석, 물리 AI 가속, 주가 +7.6%
- 한국 7월 1~20일 수출 549억 달러 역대 최고 (+52.3%) — 반도체 221억 달러 +180.6%, 7월 중순 역대 최대
- Dyne Therapeutics z-rostudirsen BLA FDA 우선심사 수락 — DMD 엑손 51, PDUFA 2027-01-21, 출시 목표 2027 Q1

## 2026-07-20
- KOSPI 7/20 재개장 -4.46%(6,516포인트), 쌍사이드카 발동 — SOX·Brent $90·Kimi K3 3중 충격 압축 소화, KOSDAQ 바이오 동반 급락
- 코오롱티슈진 TG-C Study 1 1차 지표 유의성 미달 — 위약 반응 과잉, TKR 비율 0.6% vs 5.3% 긍정 이차지표, 10월 Study 2가 DMOAD 최종 분기점
- 한국 ADC 3사 — LigaChem LCB71 ORR 77%, ABL Bio ABL209 FDA IND, Genome&Company 신규 타겟 ADC 기술이전 2026~2027 목표
- 원화 국제화 로드맵 — MOEF·BOK 7/20 공동 발표, 2027년 24시간 역외 원화 결제, MSCI 선진국 편입 선결 조건 첫 단계
- HLB 리보세라닙 3차 CRL — 효능 아닌 CMC 이슈, 항서제약 VAI 분류, CAPA 7/24 제출·8~9월 FDA 결론 예상

## 2026-07-19
- 코스피 7/20 재개장 D-1 — SOX 베어마켓(-20%)·Brent $88·Kimi K3 AI 인프라 충격 3중 누적, TG-C 발표 미확정
- Kimi K3 독립 벤치마크 57점(Artificial Analysis) — Claude Opus 4.8(56점)·GPT-5.6 Terra(55점) 상회, 7/27 전체 가중치 공개 예정
- Padcev+Keytruda MIBC 수술 전후 platinum-free 첫 FDA 승인 — ADC+ICI perioperative 표준 첫 사례, 시스플라틴 적합성 무관
- GLP-1 경구제(Lilly Foundayo) 신규 처방 2/3가 주사제 미경험자 — 전환 아닌 시장 순증 확인, Goldman 2030 Lilly 60% 점유
- Sarclisa Escena 피하주사(Sanofi) FDA 승인 — 항암제 최초 온바디 인젝터(OBI) 투여 방식, 7/9 승인


