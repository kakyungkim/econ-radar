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

## 2026-07-05
- Wegovy 영국 MASH 조건부 승인 — GLP-1 계열 간질환 적응증 첫 영국 허가, NHS 급여 협상 별도 진행
- Vera Therapeutics 아타시셉트 PDUFA D-2(7/7) — IgAN BAFF·APRIL 이중 억제제, UPCR -46%
- Anthropic, Alibaba 관련자 가짜 계정 2만 5,000개·2,880만 건 모델 지식 추출 의회 서한 제출
- 한국 6월 수출 월간 첫 $100B 돌파 — 반도체 $448.2억(+199.5% YoY), 무역흑자 $361.5억 역대 최대
- H1 2026 글로벌 VC $5,100억 역대 최대 — OpenAI+Anthropic 43%($2,170억) 독식, MGX $490억 클로징

## 2026-07-04
- Anthropic, Samsung Electronics와 2nm 커스텀 AI 추론 칩 협상 착수 — 탈클라우드 AI 추론 독립 전략, 양산 일정 미정
- Vera Therapeutics 아타시셉트 PDUFA D-3(7/7) — IgAN 최초 BAFF·APRIL 이중 억제제, 가속 승인 조건부
- 졸돈라시브 ESMO GI 수치 확정 — 전이성 PDAC 1차 ORR 82%, DCR 96%, RASolute 305 3상 진행 중
- Google 데이터센터 전력 소비 +37% YoY — AI가 전력망 탈탄소화 속도를 추월
- OpenAI CEO Altman, 미국 정부 지분 5% 기부 제안 — $426억(기업가치 $8,520억), 알래스카 영구기금 모델

## 2026-07-03
- 미국 6월 NFP 5만 7,000명(컨센서스 11만 명 절반) — 10년물 금리 역설적 상승, 스태그플레이션 우려 부상
- KOSPI +5.76%(8,088p) V자 반등 — 삼성전자 +8.22%·SK하이닉스 +10.88%, 소버린AI 5조원 수요 내러티브
- Roche 디바라시브 Krascendo 1 Phase III — KRAS G12C NSCLC, 소토라시브·아다그라시브 head-to-head PFS·OS 모두 우위
- AstraZeneca EMERALD-3 HCC — STRIDE+lenvatinib+TACE, PFS 13.0 vs 9.8개월(HR 0.70, p=0.0007)
- 한국 소버린 AI 5조원 Rubin GPU 단일팀 + Google-Anthropic $32억 TPU 임대 CaaS 모델 가동

## 2026-07-02
- KOSPI -6.25%(7,784) 서킷브레이커 — 삼성전자 -9.06%·SK하이닉스 -14.57%, 외국인 3.17조 순매도, Meta Compute·애플 중국메모리·NPS 삼중 악재
- Meta Compute 잉여 AI 컴퓨팅 외부 판매 선언 — AWS·Azure 직접 경쟁, Meta +8.8%, Micron -10.6%·AMD -6.9%·Intel -9%
- Orca Bio Tregzi FDA 승인(6/30) — 최초 Treg 세포치료제, 혈액암 이식 1년 무GVHD 생존율 78% vs 38%
- 한국 6월 CPI 3.2%(30개월 최고) + 미국 ADP 6월 민간고용 9.8만(컨센서스 11.8만 하회)
- [후속] 졸돈라시브 ESMO GI 구두 발표 완료 — 1차 ORR 82%·2차 50% 재확인, RASolute 305 3상 첫 환자 투여

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


