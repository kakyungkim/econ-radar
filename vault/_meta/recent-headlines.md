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

## 2026-08-22
- 삼성전자 KRW 90~110조 주주환원 이사회 공식 의결(한국 역대 최대·자사 최고 5배) — Q3 현금배당 ~30조 + 나머지 2027년 1월 결정
- Hot Chips 2026 내일 개막(8/23~25) — NVIDIA Vera Rubin(336B 트랜지스터·HBM4 288GB·22TB/s) vs AMD MI400(MI455X·MI430X) 첫 공식 스펙 대결 + NVIDIA 실적 D-4(8/26)
- Capricor deramiocel PDUFA 오늘 결과 없음 — BLA 수정(DMD 심근병증→상지 근기능 + 24개월 OLE) + PDUFA 연장 예정
- Trump "경제 D-Day" 이란 2차 제재 Bessent 8/24 세부 발표 예고 — Brent $93~94(주간 +5~6%), 30년물 5.273%, DXY ~98.8
- Jazz Ziihera PDUFA D-3(8/25·HER2+ GEA 1차·OS 26.4개월) + ESC Congress 2026 D-6(8/28, 핫라인 59개·CARDIO-TTRansform 최대 주목)

## 2026-08-21
- 삼성전자 Q2 영업이익 ₩89.5조(YoY +1,814% 사상 최대) + ₩100조 주주환원 이사회 월말 의결 임박 → KOSPI +0.88%(6,912.95), 삼성 +3.87%
- Walmart Q2 미국 동일점포 +2.6%(예상 +3.5% 하회) → 주가 -9%, 미 3대 지수 하락 + 이란 제재로 Brent $93+(주간 +5%, 3.5년래 최고)
- Jackson Hole D-6(8/27~29) — Warsh 첫 기조연설 8/28, 30년물 5.25% 재반등(Bessent 바이백 효과 희석)
- GENGLYCOS(DTX401/Ultragenyx) 8/19 FDA 가속 승인 확정(GSDIa 최초 유전자치료제) + Capricor deramiocel PDUFA D-1(8/22)
- AMD Helios Hot Chips D-2(8/23~25) — Microsoft 고객 확보, 컴퓨트 +15%·HBM +50% vs NVIDIA Vera Rubin + NVIDIA 실적 D-5(8/26)

## 2026-08-20
- SK Hynix ₩40조($28.6B) 자사주 전량 소각(한국 역대 최대) + FCF 50%+ 환원 정책 명문화 → KOSPI +5.9%·SK하이닉스 +14%·삼성전자 +10% 급반등
- FOMC 7월 의사록 광범위 매파(추가 긴축 가능 논거 다수) + Bessent 재무부 바이백 배증($2B→$4B+) → 30년물 5.26%→5.18%, 연준 vs 재무부 정책 분리 구도
- Capricor deramiocel PDUFA D-2(8/22) — AdCom 3-9 부결 후 FDA 독자 결정 72시간 이내, DMD 심근병증 최초 세포치료제 기로
- Ultragenyx DTX401 PDUFA D-3(8/23) + Regeneron garetosmab 8/19 FDA 승인(브랜드명 Pasatru) — GSDIa·FOP 최초 치료제 결정 클러스터
- Target Q2 EPS $4.11(컨센 $2.33 대폭 상회, 관세 환급 $752M 포함·제외 시 +20%)·매출 $26.5B·연간 가이던스 상향

## 2026-08-19
- UAE-이란 충돌 격화(UAE 무기한 무역금수·이란 미사일 공격) → KOSPI 6.45% 폭락·사이드카 발동(올해 48번째), 삼성전자 -7.5%·SK하이닉스 -8.8%, Brent $91.52 4일 연속 상승
- Regeneron garetosmab PDUFA ~D-12(~8/31) — FOP 최초 치료제 BLA 우선심사, OPTIMA 52주 신규 HO 병변 -94%/-90%(p값 확인)
- Capricor deramiocel PDUFA D-3(8/22) — FDA 72시간 이내 독자 결정, DMD 심근병증 최초 세포치료제 기로
- Home Depot Q2: EPS $4.92(예상 $4.73 상회)·매출 $47.9B(예상 $47.2B 상회)·FY2026 가이던스 재확인 — 잠김 효과(lock-in effect) 리모델링 수요 견고
- Chai Discovery 시리즈 C $4억(기업가치 $38억) + Pfizer·Lilly·Novartis 동시 AI 항체 설계 제휴 — 빅파마 AI 플랫폼 표준화 변곡점


