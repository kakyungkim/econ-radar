---
type: meta
tags: [운영, dedup]
timestamp: 2026-06-11T23:24:29+09:00
publish: false
---
# 최근 헤드라인 (recent-headlines) — 중복 회피 기준

클라우드 routine은 과거 vault(raw·analysis·daily·topics)에 접근할 수 없다(로컬 전용, gitignore). 그래서 **이 파일이 "이미 다룬 뉴스" 기준선**이다. 데일리 생성 시 규칙:

1. **시작할 때** 이 파일을 읽는다. 여기 적힌 항목은 **이미 다뤘으므로 다시 헤드라인으로 올리지 않는다.** 단, 그 사건에 **새로운 후속 전개**(승인 결과·딜 종결·실적 등)가 나왔으면 "후속/업데이트"로만 짧게 다룬다.
2. **끝낼 때** 오늘 핵심 5가지 제목을 아래 `## YYYY-MM-DD` 블록으로 **맨 위에 추가**하고, **최근 7일치만 남기고** 그 이전 블록은 지운다. 이 파일도 함께 커밋한다.

> 사람이 손으로 만든 발행본도 여기 반영한다(아래 6/10·6/11은 수작업 발행분).

---

## 2026-06-25
- SK하이닉스 Nasdaq ADR 최대 $294억(약 45조4,534억 원) 상장 확정(7월 10일) — 사상 최대급 해외 ADR, HBM 팹 증설 자금 조달
- Micron Q3 FY2026 어닝서프라이즈 — 매출 $415억·마진 84.9%·Q4 가이던스 $500억, 코스피 이틀 연속 급등(+4.19%, 9,000 가시권)
- Ionis olezarsen(Tryngolza) FDA 조기 승인(6/24, PDUFA 5일 앞당김) — sHTG 300만 명 GalNAc-ASO 대형 만성질환 첫 진입
- Eli Lilly·Centessa 인수 완료 $78억 — OX2R 작용제 cleminorexton 기면증·수면장애 파이프라인
- K바이오 상반기 라이선싱 ~13조 원($85억) — ABL Bio Grabody-B 견인(GSK 최대 $28억+Lilly $26억), 역대 최고 경신 가시권

## 2026-06-24
- AbbVie, Apogee Therapeutics $109억(약 16조8,000억 원) 인수 — 투여 편의성(zumilokibart 3~6개월 1회)이 면역학 M&A의 새 축으로
- 코스피 +3.26% 반등(8,471.02), 삼성전자 시총 1위 탈환 — 촉매는 자사주 90조 원 보도, 외국인 매도 지속
- SK바이오팜 + Insilico Medicine CNS 신경면역 AI 신약 최대 $25.7억(약 3조9,700억 원) 협력 — K바이오 AI 신약 최대 딜
- Micron Q3 FY2026 — HBM4 첫 분기 반영, 총마진 81.6% 컨센서스
- Ionis olezarsen PDUFA D-6 — RNA 치료제 대형 만성질환 첫 관문 6월 30일

## 2026-06-23
- 코스피 -9.99% 역대 최대 낙폭·서킷브레이커 발동 — 삼성전자·SK하이닉스 -12%, 외국인 4.67조 원 순매도, Fed Warsh 인상 편향 배경
- Alphabet -7% (시총 $2,500억 증발) — AlphaFold Jumper→Anthropic, Transformer Shazeer→OpenAI 동주 이탈
- Definium DT120 ODT 우울증 3상 성공 — MADRS 위약 대비 -8.1점(p<0.0001), LSD 기반 단회 투여 항우울제
- FDA Operation TrailBlazer — 초기 임상 6~12개월 단축 파일럿, 중국 임상 주도권 대응
- Ionis olezarsen PDUFA D-7(6/30 결정) — 중성지방 -72.2%, 췌장염 -85%, GalNAc-ASO 만성질환 관문

## 2026-06-22
- SK하이닉스 코스피 시총 1위 — 25년 7개월 만에 삼성전자 추월, 2,080조 vs 2,066조, HBM ~57% 점유, 당일 +5.61%
- MoonLake sonelokimab VELA 3상 52주 — HiSCR75 67.2%·HiSCR100 33.1%, BLA 9월 제출, VELA-2 p=0.053 미달
- Ionis olezarsen PDUFA 6/30 임박 — GalNAc-siRNA·APOC3 표적, 중성지방 -62.9%/-72.2%, RNA 치료제 만성질환 첫 관문
- Lilly retatrutide NDA Q4 예정 + CrossBridge Bio 이중페이로드 ADC 인수 최대 $3억 — TRANSCEND-T2D-1, 28.3% 체중감소
- BIO USA 2026 개막(K바이오 51개사·SNUH 단독 부스) + Claude Fable 5 6/23 유료 전환 — GPT-5.6 Polymarket 40% 재조정

## 2026-06-21
- DATROWAY(Dato-DXd) FDA TNBC 1선 승인 — TROP2 ADC 최초 1선, mOS 23.7개월 vs 18.7개월, ORR 64% vs 30%, NCCN Category 1
- Elicio ELI-002 7P 전이성 췌장암 완전반응 3명/3명 — KRAS mRNA 백신 + 면역관문억제제 순차 요법, AMPLIFY-7P 2상
- Nvidia Vera CPU 양산 — AI 에이전트 전용, 88 Olympus 코어, x86 대비 1.8배, OpenAI·Anthropic 납품
- 코스피 9,052 + 한국 5월 수출 877.5억달러 역대 최대 — 반도체 수출 169.4% 급증(371.6억달러)
- BIO USA 2026 개막 D-1 + GPT-5.6 출시 83% 확률(Polymarket) — 내일(6/22) 동시 이벤트

## 2026-06-20
- cytisinicline FDA CRL — 약효 데이터 건재, CMO cGMP OAI 판정이 허가 차단. 이미 Adare로 제조 이전 완료, Q4 2026 NDA 재제출·H1 2027 출시 예정
- BIO USA 2026 D-2 — K바이오 51개사, 서울대병원 병원 첫 단독 부스, ABL Bio·삼성바이오 Rockville·Rznomics 파트너링
- 유한양행 창립 100주년(6/20) — 'Great & Global' 비전, 렉라자 1Q 글로벌 $2.57억(+82.7%), 글로벌 톱 50 목표
- AI 모델 대전 6월 말 집중 — Claude Fable 5(6/9 출시), Gemini 3.5 Pro(3주째 미출시), GPT-5.6(6/22~28 출시 확률 83~90%)
- Moderna MFLUSIVA 주간 +28% + 브렌트유 $80.59 반등 — 이란 호르무즈 보험 의무 발언, 8/5 FDA 최종 결정 대기

## 2026-06-19
- Moderna MFLUSIVA VRBPAC 9-0 만장일치 권고 — mRNA 독감 백신 FDA 최종 결정 8/5, 3상 표준 백신 대비 효능 26.6%·응급실·입원 예방 47.9%
- Lilly Foundayo(orforglipron) 2형 당뇨 NDA Q2 2026 제출 예정 — 비만에 이어 두 번째 적응증, 식사 제한 없는 유일한 경구 GLP-1
- 미·이란 MOU 전자 서명 발효·스위스 서명식 취소 — 브렌트유 $75(4월 고점 대비 -38%), 핵 문제 미결
- K바이오 51개사 BIO USA 2026 출격 — Rznomics RNA 편집 FDA RMAT 3관왕(간세포암), 삼성바이오 Rockville 미국 생산시설 전면 부각
- 유한양행 창립 100주년 D-1 — 렉라자 1Q 글로벌 매출 $2.57억(+82.7%), 2030 비전 발표 예정


