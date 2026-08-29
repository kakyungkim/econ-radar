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

## 2026-08-29
- Warsh 잭슨홀 '조용한 연준' 선언 — 9월 FOMC 인상 확률 55.7%(CME FedWatch, 전일 35.4%→), PCE 구성 요소 54% 연환산 3% 이상. 9/1(월) KOSPI 반응 분기점
- ESC 2026 STAREE — 70세+ 아토르바스타틴 1차 예방 최초 대규모 RCT: CV 이벤트 -30%, 장애 없는 생존 HR 0.94(95% CI 0.84~1.05, 미달). NEJM 동시 게재
- ESC 2026 ENRICH-AF — 뇌출혈 후 AF 에독사반: 대출혈 11.6% vs 5.2%(HR 2.23), 처방 공백 재확인
- Cytokinetics aficamten 후속 — ESC 추가 발표, 장중 52주 신고가 $74.35·종가 $74.23, RBC PT $87
- Roche Vabysmo SALWEEN 2년 — PCV형 nAMD BCVA +7.3글자, 20주 간격 61%

## 2026-08-28
- OpenAI·Broadcom Jalapeño 추론칩 공개 — TSMC 3nm, HBM4 216GiB·15.4TB/s, GB200·GB300 대비 와트당 1.5~1.9배 효율, 9개월 설계. NVDA 본장 +8.74%($226.15, 약 31만2,000원)
- Cytokinetics aficamten ACACIA-HCM Ph3 성공 — 비폐쇄성 HCM 역대 최초: KCCQ +3.0점(p=0.021), pVO2 +0.67 mL/kg/min(p=0.003), n=516. HCM 전체 스펙트럼 단일 약물 커버 가시화
- CARDIO-TTRansform 전체 데이터 — eplontersen(Ionis/AZ) ATTR-CM 1차 종점 미달 확정, 병용군 이득 없음(n=1,432). vutrisiran·tafamidis·acoramidis 반사이익 구도
- Warsh 잭슨홀 기조연설 오늘 23:00 KST 예정(수집 시점 미발표) — Core PCE 3.3%, 30Y 5.31%, 9월 인상 ~1/3 확률. BLS 고용 대수정 동시 발표
- NVIDIA AI 서버 15% 인상 예고(2027년 초)·KOSPI -0.95% 역행 — HBM 공급 부족. 삼성 HBM4·OpenAI Jalapeño 공급 경로 미확인

## 2026-08-27
- NVIDIA Q2 FY27 $96.2B 어닝서프라이즈(+106% YoY), EPS $2.22, Q3 가이던스 $108B — KOSPI +1.53%(삼성 +3.25%·270,000원, SK하이닉스 +5.45%·1,780,000원). "FY28까지 메모리 부족" 발언
- BOK 기준금리 2.75%→3.0%(+25bp) — 2회 연속 인상. 점도표 10명/21명(47.6%)이 3.25% 추가 인상 지지. 3년 7개월 만의 연속 긴축
- daraxonrasib(Rasonque) FDA 승인 — 전이성 췌장 선암 최초 RAS 억제제(Revolution Medicines). mOS 13.2개월 vs SOC 6.7개월(RASolute 302, n=500). 30년 "표적화 불가" 통념 돌파
- SK하이닉스 인디애나 착공 완료 — $3.87B HBM4 후공정 팹, CHIPS Act 보조금 $450M+대출 $500M. 최태원·곽노정 참석, Jensen Huang 미확인. 양산 2028년 하반기
- SK바이오팜 + Biohaven opakalim 계약 최대 $795M(선불 $350M) — Kv7.2/7.3 뇌전증 플랫폼, RISE3 탑라인 2H 2026. Biohaven +13%

## 2026-08-26
- Jazz Ziihera(zanidatamab) FDA 정규 승인 — HER2+ GEA 1차 치료, PD-L1 무관 비스페시픽 HER2 × PD-1 복합요법 최초 정규 승인. mOS 26.4개월, HERIZON-GEA-01(n=914). 2011년 트라스투주맙 이후 1차 표준 첫 교체
- NVIDIA FY27 Q2 실적 D-0 — 컨센서스 $91.85B(YoY +97%), EPS $2.08, Q3 가이던스 $95~104B 전망. 오늘 장 마감 후 발표, KOSPI +1.69% 선반영(삼성 +2.53%, SK하이닉스 1,689,000원 +0.66%)
- PCE 오늘 발표(Core MoM 컨센서스 +0.18%/YoY 3.2%) + BOK D-1(인상 67%, Reuters 35인 18:17) + Jackson Hole D-1(Warsh 8/28 10:00 EDT) + BLS 대수정 8/28(어제 8/26 예고 정정)
- SK하이닉스 인디애나 착공 D-1($3.87B, CHIPS Act $458M+$500M, Jensen Huang 미확인) + ESC 2026 D-2(CARDIO-TTRansform n=1,432 전체 데이터 8/28 핫라인)
- GBC 2026 서울 개막(식약처 주최, 5,000명·70개국, AI·세포유전자치료 규제 의제) + LG화학 Genuv GNV205 항체-사이토카인 융합 고형암 전임상 착수

## 2026-08-25
- NVIDIA 실적 D-1 + 3중 이벤트 — 반도체 섹터 시총 $1조 증발 후 KOSPI 장중 -4% → 종가 +0.68%(6,742.74) 반전. 내일 FY27 Q2 실적(컨센 $93.63B)·PCE·BLS 고용 대수정 동시 발표
- Jazz Ziihera(zanidatamab) HER2+ GEA 1차 FDA PDUFA 오늘 결과 미확인 — HERIZON-GEA-01 mOS 26.4개월(OS HR 0.72, PFS HR 0.63)
- BOK 금리결정 D-2 + Jackson Hole D-2 — 인상 51.4%(18명) vs 동결 48.6%(17명) 사실상 동수. Warsh 8/28 첫 기조연설
- Capricor deramiocel PDUFA 11/22로 연장 — 자문위 9대3 부결 후 FDA 적응증 정제(상지 기능) 재검토. DMD 심근병증 세포치료제 적응증 정제 전략 선례
- SK하이닉스 인디애나 착공 D-2(8/27) — $3.87B(약 5조4,000억원), CHIPS Act $450M. ESC 2026 D-3(CARDIO-TTRansform 전체 데이터 8/28)

## 2026-08-24
- LEQEMBI IQLIK(lecanemab SC) FDA 승인 — 알츠하이머 피하주사 개시용량(주 1회 500mg), 격주 IV → 자가주사 처방 채널 첫 전환. 8월 말 미국 출시 예정
- KOSPI -3.12%(6,696.96) — 삼성전자 -8.35% 폭락(주주환원 실망 매물) vs SK하이닉스 +2.4% 역행(HBM4 독점 구도 재확인). KOSDAQ +2.2%
- Bessent 이란 제재 세부안 발표 — 그림자 선단·중국·마샬아일랜드 선사 직격, 2차 제재 활성화. Brent $93.09(-1.38%) "선반영 완료"
- Google TPU 8t/8i Hot Chips Day 2 공개 — 훈련·추론 분리 아키텍처, 121 ExaFLOPS, TSMC 2nm, 2027년 말 외부 공급 예고
- 경구 GLP-1 Lilly Foundayo 점유율 56.7% vs Novo 37.1% — 경구 시장에서 브랜드 우위 역전 고착

## 2026-08-23
- Hot Chips 2026 Day 1 — NVIDIA Vera Rubin R100 공식(HBM4 대역폭 목표 22TB/s→초기 출하 ~20TB/s 미달, SK하이닉스 70%·삼성 30%) + AMD MI455X(CDNA 5·HBM4 432GB·23.3TB/s) 첫 공식 스펙 대결 + NVIDIA 실적 D-3(8/26·컨센서스 $92B)
- eplontersen CARDIO-TTRansform 1차 종점 미충족 — 스타빌라이저(tafamidis 등) 병용 환자군에서 효과 없음, 단일요법 서브그룹 HR 0.71, ESC 2026 핫라인(8/28) 전체 데이터 공개 예정
- Jazz Ziihera PDUFA D-2(8/25·HER2+ GEA 1차·zanidatamab·OS 26.4개월·HR 0.72)
- Bessent 이란 2차 제재 D-1 — 내일(8/24) 기자회견 "역사상 가장 강력한 제재", Brent ~$94/배럴, 30년물 5.25%+, DXY ~98.8
- 이번 주 5대 이벤트 집중 — NVIDIA 실적(8/26)·BOK 금리(8/27·25bp 인상 vs 동결+10월 시사)·Jackson Hole(8/27~29)·SK하이닉스 인디애나 착공(8/27)


