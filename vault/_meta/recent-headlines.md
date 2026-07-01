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

## 2026-07-01
- 한국 6월 수출 사상 첫 1,000억 달러 돌파 — 반도체 $448.2억(+199.5% YoY), 무역흑자 $361.5억 역대 최대, 세계 4번째
- Ipsen, Kartos Therapeutics 인수 합의 — MDM2 억제제 나브테마들린, 최대 $17.5억(약 2조 4,150억 원), Q3 2026 종결 목표
- OpenAI GeneBench-Pro + Microsoft MAI-Thinking-1 — 최고 AI 계산생물학 통과율 31.5%, AI 신약 개발 한계 수치화
- 알테오젠 ALT-B4 사노피 공개($13.7억 비독점·파트너 8곳) + 유한양행 렉라자 유럽 마일스톤 $3,000만(누적 $3억)
- 코스피 Q3 첫 거래일 차익 실현 — 수출 신기록에도 삼성전자 -4.27%·SK하이닉스 -2.54%, SK하이닉스 시총 1위 26년 만의 역전

## 2026-06-30
- Vera Therapeutics 아타시셉트 PDUFA 7/7 — IgA 신증 BAFF+APRIL 이중 억제 최초, ORIGIN 3 UPCR −46%, Breakthrough+Priority Review
- Revolution Medicines 졸돈라시브 ESMO GI 7/1 발표 — 췌장암 1차 ORR 82%, 2차 ORR 50%, 학회 공식 발표 D-1
- OpenAI·Broadcom Jalapeño ASIC 공개 — LLM 추론 전용 칩 9개월 설계, 2026년 말 기가와트 배포 목표
- Amazon 자체 칩 $20B 런레이트 — CEO "독립 기업이면 $50B", Trainium 3세대 매진·외부 판매 검토
- 한미약품 소네페글루타이드 Eli Lilly 라이선스 최대 $12.6억(약 1조8,950억 원) — GLP-2 단장증후군, 선급금 $7,500만

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


