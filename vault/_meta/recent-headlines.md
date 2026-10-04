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

## 2026-10-04
- I-DXd BLA 자진 철회 — FDA의 ADC 가속승인 경로 구조적 협소화, SCLC Phase 3 데이터 없이 불가 확인
- 삼성전자 Q3 잠정실적 이번 주(10/7~8) — 영업이익 116조원 컨센, HBM4 매출 전 분기 대비 3배 급증 예상
- Q3 어닝스 시즌 D-9 — JPMorgan·Goldman·J&J 10월 13일 개막, S&P 500 Q3 EPS 성장 +23% 기대
- BMS Cobenfy ADEPT-1 탑라인 2027 초 재연기 — 알츠하이머 정신증 이벤트 축적 지연
- Apple iOS 27.2 한국어 Siri AI 10월 배포 — 카카오·네이버·삼성 갤럭시 AI와 경쟁 구도 본격화

## 2026-10-03
- 9월 NFP +29,000 고용 쇼크 — 컨센서스 +84,000 대폭 하회, Fed 10월 동결 기대 강화
- Anthropic 기업공개(IPO) 비공개 신청 — $965B 밸류에이션, 연매출 런레이트 $47B, 10월 상장 목표
- Novo Nordisk 2026 매출 최대 -13% 전망 — CagriSema 티르제파타이드 대비 열세(23% vs 25.5%), 경구 Wegovy 호조
- bepirovirsen(GSK/Ionis) PDUFA D-23(10/26) — 만성 B형 간염 최초 기능적 완치 후보, 결정 임박
- 바이오테크 M&A 2026 1분기 $840억 — 전년 $444억 대비 89% 급증, ADC·비만·면역종양 3축

## 2026-10-02
- Micron Q4 FY2026 데이터센터 $11.5B·전년 동기 7.5배 어닝스 빅 비트 — AI 메모리 사이클 FY2027 연장 확인
- 9월 고용보고서 오늘(10/2) 발표 — ADP 선행 +90K, BLS 컨센 +93~98K, Fed 10월 인상 경로 분수령
- Lilly Zepbound·Foundayo 미국 3대 PBM 전면 급여 10/1 발효 — GLP-1 보험 장벽 해소, 수요 병목 이동
- BMS Camzyos 소아 oHCM FDA 승인(9/30) — 심근 미오신 억제제(CMI) 최초 소아 적응증 획득
- GSK·Ionis bepirovirsen PDUFA 10/26 — 전 세계 2억4,000만 만성 B형 간염 환자 대상 기능적 완치 후보

## 2026-09-30
- AstraZeneca, Summit Therapeutics에 $2B 지분 투자 + ivonescimab·ADC 병용 임상 협약 — ADC+이중항체 병용의 새 문법
- Eli Lilly Zepbound·Foundayo 내일(10/1)부터 미국 3대 PBM 전면 급여 — GLP-1 만성질환 표준 편입 시작
- Anthropic Claude 4.5 출시 + ARR $30B 돌파, OpenAI 추월 — 엔터프라이즈 AI 침투 가속
- SK하이닉스 HBM4 Q4 출하 시작 + Micron Q4 FY2026 실적 오늘 발표(결과 대기) — HBM 구조 성장 확인 분기점
- KOSPI 3일 연속 하락(6,838.04, -0.48%) + Core PCE 8월 발표 + 외국인 누적 9조원 순매도

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
