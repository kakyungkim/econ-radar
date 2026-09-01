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

## 2026-09-01
- 브로드컴 FY3Q 어닝 D-1 & OpenAI IPO S-1 기밀 제출 — AI ASIC $16B·FY27 $100B 가이던스 재확인과 생성 AI 수익 구조 최초 공개 동시 임박
- Besremi(ropeginterferon alfa-2b) ET FDA 승인 — PharmaEssentia, 30년 만의 ET 신약, SURPASS-ET 42.9% vs 6.0%(p=0.0001)
- 9월 FOMC 25bp 인상 확률 60.4%·호르무즈 탱커 기뢰 피격 — 브렌트유 $91.28(+0.87%), 유가·금리 이중 압박 정착
- zilurgisertib FOP PDUFA 9/26 — Mirum/Incyte, 전 세계 최초 경구 ALK2 억제제·FOP 첫 승인 약물 후보
- 한미약품-Genentech HM17321(UCN2) 최대 $2.3B(약 3조1,600억원) — 비GLP-1 비만 기전 첫 빅파마 글로벌 베팅, Phase 1 진행 중

## 2026-08-31
- 삼성바이오로직스 PolyPeptide $1.84B(약 2조5,200억원) 공개매수 개시(9/15~10/12) — 한국 바이오 해외 인수 사상 최대, GLP-1 펩타이드 CDMO 진입
- Medera SRD-002(AAV1/SERCA2a) ESC 2026 최종일 — HFpEF 유전자치료 12개월 PCWP 정상화 80%(n=10), 중대 이상반응 0건
- DeepSeek 첫 외부 펀딩 $7.4B·기업가치 $74B — 텐센트·CATL 참여, 2027 STAR 상장 준비
- 미국-이란 교전 재개 — 브렌트유 $90.32, 호르무즈해협 리스크 부활
- KOSPI 장중 -2.58%→종가 +0.46% V자 반등, 브로드컴 9/2 어닝(AI ASIC $16B 달성 여부) 주간 체크포인트

## 2026-08-30
- ESC 2026 Hot Line 6 LUMINARA — AZD5462(경구 릴렉신) HFpEF 1차 달성·HFrEF 미달, 경구 RXFP1 계열 최초 양성 신호
- Takeda MIMRYLO(rusfertide) FDA 승인 — PV 최초 헤프시딘 유사체, 사혈 불필요 76.9% vs 32.9%(VERIFY Ph3, n=293)
- BioNTech autogene cevumeran Phase 2 종료 — 생존 불균형, BNTX -8%·Moderna -6%, mRNA 단독 암치료 한계 확인
- Meta Hatch — Anthropic Claude 기반 에이전트 슈퍼앱 수주 내 출시, $199.99/월 프리미엄 검토
- Warsh 잭슨홀 여파 — KOSPI 7,000선 미회복 첫 정규 반영일, 9월 FOMC 인상 확률 55~59%(CME FedWatch)

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


