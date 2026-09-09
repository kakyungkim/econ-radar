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

## 2026-09-09
- KOSPI 7,051.64 (+1.40%) — 배터리·석화 동반 급등으로 33거래일 만에 7,000 탈환
- Mistral AI €3B(약 3조3,000억원) 삼성전자 주도 시리즈 D — 유럽 기술 역대 최대 에퀴티 라운드, 소버린 AI 테마
- Merck Winrevair PDUFA D-12(9/21) — HYPERION 새로 진단된 WHO FC II~III PAH 1차 치료 확장 카운트다운
- Ionis ZANVASTRO(zilganersen) 9/3 FDA 승인 — Alexander disease 첫 질환 수정 치료제, ASO 플랫폼 희귀신경질환 첫 상업화
- 유한양행 YH42946 WCLC 2026 서울 D-3 — HER2·EGFR 엑손20 이중 경구 TKI 첫 임상 데이터

## 2026-09-08
- WCLC 2026 서울 D-4 — AZ Tagrisso 8년 OS vs J&J MARIPOSA HR 0.75(42개월 OS 56% vs 44%), EGFR 1차 치료 표준 대결
- MSD+Gilead KEYNOTE-D46/EVOKE-03 중단 — TROP2 ADC+PD-1 병용, NSCLC 1차 치료 Phase 3 실패, ADC+IO 전략 첫 대형 벽
- Ultragenyx UX111 PDUFA D-11(9/19) — 산필리포 A형(MPS IIIA) 최초 AAV9 유전자치료제, BLA 재제출 수락
- BOJ 9/17~18 25bp 인상 유력 — 엔 캐리 언와인딩·KOSPI 선물 만기(1.7조) 수급 변동성, Goldman KOSPI 12,000 유지
- Daiichi Sankyo+MSD I-DXd(ifinatamab deruxtecan) — SCLC 2차 치료 B7-H3 ADC, PDUFA 10/10, WCLC 데이터 공개

## 2026-09-07
- Revolution Medicines Rasonque(daraxonrasib) FDA 승인(8/26) — 세계 최초 pan-RAS GTPase 억제제, 전이성 췌장선암(KRAS G12X 등 전 변이), NGS 동반진단 불필요
- BMS Zenbexus(iberdomide) FDA 가속 승인 — 첫 CELMoD 계열, RRMM, MRD 음성 CR 대리지표 최초 채택
- Nvidia Hugging Face $12.93B 인수 — GPU 공급자→AI 플랫폼 운영자, 1.8M+ 개발자·모델·데이터셋 생태계
- FOMC 인상 확률 38%→56~66% + CPI D-4(9/11) — Warsh 강경론(8/28), 이란 탄도미사일 발사·WTI $90+ 유가 변수 동시
- WCLC 2026 D-5(9/12개막) + AZ-Dizal EGFR $1.5B + zilurgisertib PDUFA D-19(9/26)

## 2026-09-06
- WCLC 2026 서울 D-6 — BioNTech ADC×IO(pumitamig+elfetabart drozuntecan) 글로벌 첫 인체 데이터·AbbVie 폐암 3종 발표(9/12~15)
- UX111(산필리포 B) PDUFA D-13 — Ultragenyx AAV9 유전자치료제, 9/19 심사 결론
- LLM 3파전 — GPT-6 Astra 일반 롤아웃·Claude Fable 5.1·Gemini 3.8 Flash, 벤치마크→기업 채택 경쟁 전환
- 9/11 CPI D-5·9/16 FOMC D-10 — 인상·동결 분기점, 이란 유조선 피격 유가 변수
- 리가켐바이오 SOT106 패스트트랙 + 국민성장펀드 5,000억 — 한국 ADC 플랫폼 글로벌 궤도

## 2026-09-05
- Ionis Zanvastro(Alexander병) FDA 조기 승인 — ASO 독자 상업화 첫 검증, RPD-PRV 수여
- GPT-6 Astra 일반 공개(9/5) + Microsoft MAI-Transcribe-2($0.10/시간) — AI 인프라 가격 파괴
- SK하이닉스 HBM 2026 전량 sold out + 삼성·SK H1 시설투자 43.2조(+35%)
- 알테오젠 노바티스 최대 4.4조원 SC 플랫폼 4연속 빅파마 메가딜, 목표주가 54만원
- 9월 PDUFA 집중기: UX111(9/19)·relutrigine(9/27)·Camzyos 소아(9/30)

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

