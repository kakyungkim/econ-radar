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

## 2026-11-04
- 미국 중간선거 결과 — 민주당 상·하원 양원 장악, GRID Savings Act·AI 사업자 책임법안 입법 경로 개시
- AMD Q3 FY2026 Q4 가이던스 170억달러(약 25조원) — 컨센서스 대폭 상회, AI 인프라 수요 지속 첫 수치 확인
- 이보네시맙(Ivonescimab) PDUFA D-10(11/14) — 뇌전이 intracranial 데이터 보완, FDA 커뮤니케이션 없음
- Anthropic S-1 세부 — 상반기 매출 163억달러·순손실 807억달러, 로드쇼 D-5(11/9주 착수)
- 제약 PDUFA 집중 구간 — 넬라달킵 D-23(11/27)·셀멘도시란 11월 대기·Capricor deramiocel 2027년 초 연장

## 2026-11-03
- 미국 중간선거 당일 — 민주당 하원 다수 94% 예측(Kalshi), AI 규제·Anthropic IPO 공모가 직결 변수
- Apple Q4 FY2026 매출 $114.5B(+12%) EPS $2.10 컨센 상회, 마진 가이던스 약화로 주가 -3%
- Anthropic IPO 밸류에이션 $1.5~1.6T 하향 — 나스닥 100 최근 고점 대비 -10% 기술적 조정 반영
- 미타피바트(Pyrukynd) SCD PDUFA 2027-02-01로 3개월 연장(REMS 추가정보 요청) + I-DXd BLA 자진 철수 확인
- AMD Q3 FY2026 오늘 장 마감 후 발표 예정 — 데이터센터 컨센서스 $8.2B, 결과 미확인

## 2026-11-02
- BOJ 2026년 2% 물가 목표 달성 첫 공식 선언 — FY2027 근원 CPI 2.6% 상향, 12월 1.50% 인상 시장 확률 68%
- 한국 10월 수출 최종치 $115.3B(+93.7%) — 반도체 $56.4B 사상 최고 비중 48.9%, 연누계 $930B
- 미국 중간선거 D-1 — AI 규제 방향·Anthropic IPO 공모가(11/9주 로드쇼) 직결 변수
- 셀멘도시란(Cemdisiran, Regeneron) gMG FDA 결정 이달 — 최초 siRNA gMG 치료제, NIMBLE MG-ADL -2.3점
- 넬라달킵(Nuvalent) PDUFA D-25(11/27) — ALK 4세대 TKI, 로브레나 미투여 하위군 ORR 46%

## 2026-11-01
- Inovio Voceryq(INO-3107) FDA 가속승인 — DNA 플랫폼 미국 첫 허가, 재발성 호흡기유두종증(RRP) 대상, 현금 $37.7M 런치 자금 압박
- PCE 9월 코어 +3.1%·슈퍼코어 +3.60% YoY — 12월 FOMC 인상 OIS ~90%, 결정 변수 NFP(11/7)·CPI(11/13)
- 이보네시맙 PDUFA 11/14 — NSCLC 2차 PD-1/VEGF 이중항체, 중국 단독 임상 데이터 FDA 수용 여부 최대 변수
- 미국 중간선거 D-2 — AI 규제·빅테크 세금 핵심 정책 변수, Anthropic 로드쇼(11/9주) 시점 겹침
- 경구 GLP-1 이중 시장 — Novo 경구 Wegovy vs Lilly Foundayo, 접근성·급여 장벽 지속, 레타트루타이드 2027 BLA 예정

## 2026-10-31
- BOJ 10월 1.25% 동결(7-2 표결) — 12월 인상 기준선 높아졌다, 분기 경기전망 보고서 11/2 공개
- 한미약품 에페글레나타이드 식약처 10/7 허가 확인 — 국산 신약 45호, 국내 최초 GLP-1 비만치료제
- 삼성바이오로직스 PolyPeptide 최소 청약 충족(10/16) — CHF 1.46B(약 2.7조원), 펩타이드 CDMO 확장
- Anthropic IPO 로드쇼 11/9주 예정 — S-1 제출 완료, 밸류 ~$2T, 미국 중간선거 후 개시
- Inovio INO-3107 FDA PDUFA 10/30 경과 — 결과 미확인, DNA 플랫폼 최초 승인 여부 주목

## 2026-10-30
- intismeran autogene INTerpath-001 Phase 3 — 흑색종 mRNA 개인맞춤 암백신 항암 Phase 3 첫 성공(RFS HR 0.58, NEJM)
- divarasib KrasCendo-1 Phase 3 — KRAS G12C 3세대, sotorasib·adagrasib 동시 추월(PFS HR 0.58/OS HR 0.56, NEJM)
- Amazon Q3 + AI 클라우드 어닝스 총결산 — AWS $46B(+39.3%), 전사 OPM 13.9% 역대 최고, 2027 capex "materially higher"
- US GDP Q3 +3.4% SAAR — BEA 1차 추정치, 컨센서스 상회, 12월 FOMC 인상 OIS ~80% 압박 강화
- Eli Lilly Q3 FY2026 — tirzepatide(Mounjaro+Zepbound) 합산 $16.0B/분기, 성장 지속 vs 둔화 논쟁

## 2026-10-29
- MSFT Azure +48% CC 서프라이즈 · Alphabet EPS $2.12 미스 — AI 투자 수익화 속도 첫 분기점
- HBM4 시대 공식 개막 — SK하이닉스 OP 83.3조(+632%) · 삼성전자 OP 107.4조(+783%), 합산 190조원
- FOMC 10월 동결 10-2 균열(Cook·Hammack 인상 주장), 12월 인상 OIS 80%
- ESMO 2026 유방암 — iza-bren(BMS/SystImmune) PFS HR 0.41 · ribociclib NATALEE 6년 OS HR 0.809
- Anthropic S-1 제출(Nasdaq 'ANT') — 밸류 최대 $2조, 11월 16일 상장 목표, Nvidia $10B 앵커 협의


