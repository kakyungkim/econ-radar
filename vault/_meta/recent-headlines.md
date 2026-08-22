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

## 2026-08-18
- 미·이란 휴전 60일 만료(8/17) → Brent $91+·30년 국채 5.3146%(2004년래 최고)·달러인덱스 99.5 — 지정학 충격이 유가·채권·달러 동시 이동으로 번졌다
- KOSPI 재개장 +2.15%(7,127.77) 후 종가 -1.55%(6,869.83) 반전 — 외국인 5거래일 연속 순매수, 이번 주 누적 7조8,000억원(확인 필요)
- Hot Chips 2026 D-5(8/23~25, Stanford) — NVIDIA Rubin GPU·AMD MI400·삼성 HBM5·SK하이닉스 HBM4E 발표 예정, 8/26 NVIDIA 실적 연동
- Capricor deramiocel PDUFA D-4(8/22) — AdCom 3-9 부결(7/29) 후 FDA 독자 결정, DMD 심근병증 최초 세포치료제 기로
- Eli Lilly retatrutide 소송 6건(8/12~13) GLP-1 블랙마켓 정화 + GPT-5.6 Sol 오답률 68% 감소(GPT-5.5 Instant 대비)

## 2026-08-17
- Stripe, OpenRouter 인수 $70억+(약 9조5,000억원) 확정(8/16) — AI 모델 라우팅-결제 수직 통합, 결제 인프라 미들레이어 선점
- Leqembi IQLIK(lecanemab 피하주사) 8월 말 미국 출시 — 자가주사 첫 알츠하이머 치료제, SC 전환이 처방·급여 구조 변화
- 미 Empire State 11.9(예상 상회)·NAHB 32(예상 하회) — 제조업 선방 vs 주택 2연속 하락, 달러 약세·9월 FOMC 동결 60%
- PTC Therapeutics, 파브리병 유전자치료 ST-920 경매 낙찰 최대 2억1,100만달러(현금 $1.11억 + 마일스톤)
- 이번 주 소비 바로미터 — Home Depot(화)·Target(수)·Walmart(목) 실적 + FOMC 7월 의사록(8/20)

## 2026-08-16
- 잭슨홀(8/27~29) D-11 — Warsh 취임 후 첫 기조연설, 9월 FOMC 동결(71.2%) vs 인상(28.8%) 19일 전 방향타(직전 파일 개막일 8/21 표기 오류 → 실제 8/27 교정)
- NVIDIA 실적 D-10(8/26) — 가이던스 $910억 ±2%, 컨센서스 $930~950억, Blackwell 램프업 첫 공식 수치
- Definium DT120(리세르자이드) GAD Phase 3 VOYAGE 양성(8/12) — HAM-A 위약 대비 -5.4p(p<0.0001, Cohen's d=0.81), 사이키델릭 신약 역사상 첫 연속 3상 성공
- Capricor deramiocel BLA 피벗 — 적응증 DMD 심근병증(LVEF)→상지 골격근으로 변경, PDUFA 8/22 연장 예정
- 바이오 PDUFA 클러스터 — DTX401(GSDIa 최초 유전자치료 8/23)·garetosmab(FOP 최초 치료제 8/31) 연속 관문



