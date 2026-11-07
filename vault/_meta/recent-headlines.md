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

## 2026-11-07
- 미 10월 NFP +165,000명 — 컨센서스 2.8배 서프라이즈, 연준 12월 금리 인상 경로 확정
- J&J 리브레반트(amivantamab) 두경부암 FDA 가속승인 — bispecific Ab 적응증 두경부암 첫 확장
- Novartis 졸젠스마 암 발생 9례 — AAV insertional mutagenesis 2건 확인, 유전자치료 안전성 논쟁
- OpenAI $1.25조 조달 vs Anthropic IPO $1.5조 하회 경고 — AI 1세대 밸류에이션 분화
- K바이오 5사 3Q 모두 YoY 성장 — 삼성바이오로직스 1조 4,903억 원(+18.5%), 정부 R&D 투자 역행

## 2026-11-06
- KOSPI 이틀 연속 급락 + 서킷브레이커 — 삼성전자 188,700원(-6.35%)·SK하이닉스 1,132,000원(-10.44%), 이틀 누적 ~-11%
- AHA 2026 Scientific Sessions Day 1 개막 — 11/7 Braunwald Session 08:30 펠라카르센 Lp(a)HORIZON 전체 데이터 첫 공개
- CTX310 (CRISPR Therapeutics) AHA 2026 Late-Breaking 발표 예정 — ANGPTL3 편집 1년 추적 최대 -89% 유지(ESC 2026)
- Anthropic IPO D-4 — 기관투자자 밸류에이션 $2T → $1.5~1.6T 조정, 로드쇼 최소 11/10 착수
- 미 10월 NFP 오늘 KST 21:30 발표 예정 — 9월 +2.9만 충격 후 반등 여부(컨센서스 약 +65K)

## 2026-11-05
- 중간선거 후 에너지 프리미엄 붕괴 — Dow +3.03%·금 $4,066 첫 돌파, KOSPI -5.5% AI 반도체 순환매 이탈
- AHA 2026 Scientific Sessions 11/6 개막 — 11/7 펠라카르센 Lp(a)HORIZON 전체 실패 데이터 공개
- 수르보두티드 SYNCHRONIZE-CVOT AHA 11/9 발표 — 비만치료제 최초 대형 GLP-1/GCG 이중 CVOT
- Qualcomm Q4 FY2026 더블 비트 — 자동차 첫 $20억(약 2조9,400억원) 돌파(+89% YoY), FY2027 데이터센터 $5B 목표 재확인
- 미 10월 NFP 11/6(ET 08:30) 발표 예정 — 9월 +2.9만 충격 후 반등 여부, Fed 12월 인상 OIS ~80%

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


