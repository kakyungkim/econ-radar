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

## 2026-09-04
- 미 8월 NFP +22,000명(컨센서스 +55K 하회) — FOMC 인상 확률 66%→38%, KOSPI +1.64%(6,687.21)·KOSDAQ +2.95%(813.50), 9/11 CPI 최종 변수
- OpenAI GPT-6 Astra 제한 출시 — 사이버 Critical 등급 최초, FrontierMath Tier4 97.6%, 9/5 전면 출시 예정
- Eli Lilly + Orna Therapeutics 최대 $2.4B(약 3조2,880억원) — In Vivo CAR-T 자가면역 플랫폼, 세포치료 적응증 암→자가면역 확장 첫 대형 베팅
- Capricor deramiocel(DMD) PDUFA 11/22로 연장 — adcomm 3:9 부결 후 주요 수정안 제출, DMD 세포치료 최초 허가 재도전
- WCLC 2026 서울 9/12~15 D-8 개막 — ADC·T세포이중항체·AI 정밀의학 피봇 데이터 공개 예정, 알테오젠 SC→AOC 플랫폼 확장 시그널

## 2026-09-03
- 이란 IRGC 5개국 미군기지 드론·미사일 반격 — 브렌트유 $95.25/bbl 2일 연속, KOSPI +0.26%(6,579.48), 9/4 NFP → 9/16 FOMC 25bp 확률 66%
- Broadcom FY3Q: AI 매출 $16.7B(+221%)·전체 $29.6B(+86%), Q4 가이던스 $34.8B 컨센서스 하회 → 시간외 -4.04%, FY27 AI $115B 로드맵 첫 공개
- BioMarin-Alesta 인수 완료($490M max) — HPP 첫 경구 소분자 ALE1, Phase 1/2a
- zilurgisertib FOP PDUFA 9/26 + ENDO 2026 피봇 데이터 발표 임박 — Mirum/Incyte, 경구 ALK2 억제제
- KOSDAQ 바이오 3사 동반 상장(Organoid Sciences·AimedBio·Mezoo) — Mint Venture 1호, KOSDAQ -1.71%(790.21)

## 2026-09-02
- KOSPI -3.99%(6,562.72·-273pt)·브렌트유 $94.86/bbl — 미군 이란 탱커 보복 공습('탱커 for 탱커'), 외인 1.9조 순매도, 9월 FOMC 25bp 확률 66%
- Eli Lilly → Merida Biosciences 최대 $2.875B(약 3조9,350억원) — 자가항체 선택적 분해 플랫폼, MER511(그레이브스병·TED) Phase 1, 2026년 13번째 인수
- CXMT HBM3E 소량 생산 개시 — 알리바바·캠브리콘 테스트 공급, 한국 업체 대비 기술 격차(업계 추정, 본문 확인 필요)
- Runway Solaris — AI가 실시간으로 소프트웨어 인터페이스를 생성하는 월드 모델, 코드 없는 UI 생성 데모
- OpenAI IPO 2027년 연기 확인 — 공개 S-1 미제출, 순손실 $38.5B·흑자 전환 2030년·ARR $40B+(Bloomberg 2026-08-13)

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



