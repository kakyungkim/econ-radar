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

## 2026-06-29
- 삼성·SK하이닉스 10년 2,000조 원 AI·반도체 투자 선언 — 발표 당일 삼성 −4.7%, SK −3.1% 하락
- OpenAI GPT-5.6 Sol·Terra·Luna 3종 발표 — 미 정부 사전 심사 후 ~20개 기관 한정 출시, 정부 게이트 공식화
- Viridian Lumvoa FDA 승인 — TED 활성기+만성기 광범위 라벨, Amgen Tepezza 독점 시장 첫 경쟁자
- 코스피 6/26 서킷브레이커 재발동 — 장 중 8,198.33, 주간 시총 550조 원 증발
- Larimar nomlabofusp BLA 롤링 제출 — 프리드라이히 실조증 가속 승인 경로, CMC 하반기 제출 예정

## 2026-06-28
- Sangamo Therapeutics Chapter 11 파산 — Lilly AAV·ZFP·MINT 플랫폼 $5,000만+부채, Astellas 파브리병 ST-920 $2,500만+마일스톤 스토킹호스 입찰
- Merck KGaA + Bio-Techne $113억(약 15조6,000억 원) — 공간생물학·세포/유전자치료 도구, Sigma-Aldrich 이후 최대 딜, 36% 프리미엄
- Isomorphic Labs(DeepMind 스핀오프) AI 설계 항암 신약 인간 임상 2026년 내 예고 — IsoDDE AlphaFold 3 대비 2배 정확도, Lilly·Novartis 파트너십
- Qualcomm + Tenstorrent 인수 협상 $80~100억 — RISC-V AI 칩, Nvidia 포위 구도(미확정)
- Lantheus LNTH-2501 FDA CRL — 6월 세 번째 CMO 제조 결함 불승인, 효능·안전성 무결 인정

## 2026-06-27
- Revolution Medicines 졸돈라시브(zoldonrasib) 전이성 췌장암 1차 ORR 82% — KRAS G12D 공유 억제, ESMO GI 7/1~4 구연 발표
- BofA 연준 75bp(3회) 인상 전망 전환 — 9·10·12월, 연말 기준금리 4.25~4.50%
- Sobi NASP FDA CRL — PDUFA 하루 전 CMO 제조 결함 통보, 효능·안전성 FDA 공식 무결 인정
- SK하이닉스·삼성·Micron Nvidia 16단 HBM4 수주 경쟁 + SK하이닉스 DDR5 마진 전략
- Takeda 자소시티닙 3상 — 데우크라바시티닙 대비 PASI 100 달성률 2.5배

## 2026-06-26
- 미국 5월 PCE 4.1% (3년 만에 4% 돌파) — Warsh 연준 금리 인상 논거 강화, 코스피 -3.39% 연동
- Definium DT120(리서지드 LSD ODT) Phase 3 MDD 성공 — MADRS -13.3 vs -5.2, 사이키델릭 FDA 표준 경로 첫 3상 통과
- 중국 2조 위안($295억) AI 국가망 — 화웨이 어센드 80% 의무화, Nvidia 중국 매출 구조적 배제 확정
- Moderna mFLUSIVA FDA 자문위 9-0 — 8/5 최종 결정, mRNA 독감백신 첫 승인 가시권
- 한국 MSCI 신흥국 유지(선진국 재탈락) — 원화 역외 비전달성·FX 접근 제한, 2027년 이후 재심사

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


