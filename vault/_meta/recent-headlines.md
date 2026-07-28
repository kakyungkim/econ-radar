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

## 2026-07-28
- 코스피 '검은 화요일' -10.84% — 중국 DUV 양산·CXMT 400% 급등 이중 충격, 서킷브레이커 1단계 발동
- 중국 DUV 노광장비 양산 착수 — 위량성(SiCarrier·화웨이 연계) 2026년 5대 납품, ASML -7%
- Capricor deramiocel AdCom D-1 — FDA 브리핑 "Hope-3 유효성 없음", 주가 -67%
- FOMC D-1(7/29) + SK하이닉스·MS·Meta 실적 + RP1·deramiocel AdCom — 이벤트 집중
- argenx, Forte Biosciences 22억 달러(약 3조 500억원) 인수 — 최초 항-CD122 항체 FB102

## 2026-07-27
- 한-미 $950B AI 칩 협약 + Nvidia-Naver $1B 전략 지분(4.5%, 204,500원/주, 납입 10/30), Naver +7.71%
- CXMT 상하이 STAR마켓 상장 — 시총 125조원 추정, DRAM 4위 7.67%, 코스피 장중 6,557 급락 후 +0.97% 6,755.75 마감
- Brent -6% $90.88 / WTI -5.6% $84.19 — 미-이란 공습 상호 중단, 지정학 리스크 프리미엄 급락
- Kimi K3 2.8T MoE 오픈웨이트 공개 확인(HuggingFace, Modified MIT) — 역대 최대, 코딩 벤치마크 1위
- Moderna mRNA-1010 PDUFA 8/5 — VRBPAC 9:0 만장일치, mRNA 플랫폼 독감 분야 최초 진입 분수령

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

