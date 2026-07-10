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

## 2026-07-10
- HLB 리보세라닙+캄렐리주맙 FDA 3차 CRL (7/10) — Hengrui cGMP Form 483 반복, 연내 4수 도전 예고. 3수 모두 제조 문제, 임상 유효성(mOS 23.8개월 HR 0.64) 유효
- [후속] SK하이닉스 SKHYV 나스닥 첫날 $158.14(+6.1%) + KOSPI +4.60%·7,627 기술적 베어마켓 탈출 — $26.5B(약 40.1조원) 역대 최대 해외 ADR
- SpaceXAI Grok 4.5 공개 — Cursor $60B 인수 후 첫 공동 모델, $2/$6/M 코딩 특화, SWE-Bench Pro 64.7%
- 미국 6월 CPI 예측 3.92%(Cleveland Fed Nowcast), 7/14 발표 — FOMC 9:8 분열 국면 결정 변수
- 마이크론 $30억(약 4.5조원) 미국 공급망 투자 — GlobalWafers 텍사스 웨이퍼 공장 $5억, 10년 계약. MU 7/9 +7%

## 2026-07-09
- OpenAI GPT-5.6 Sol·Terra·Luna 전체 공개(7/9) — 3단계 가격 체계(Sol $5/$30·Terra $2.5/$15·Luna $1/$6), CAIS 사전 검토 선례
- [후속] KOSPI 7/9 +0.62%·7,292 반등 — 장중 7,063 급락 후 AI 반도체(SK하이닉스 +5.83%)만 회복, ADB 한국 성장률 2.6% 상향
- SK하이닉스 ADR SKHY 7배 초과청약(D-1, 7/10 Nasdaq 상장) — 280억달러(약 42조4,480억원) 역대 최대 해외기업 ADR
- FOMC 6월 의사록 9:8 금리인상 지지·PCE 3.6% + Brent +5.06%·$77.92 — 스태그플레이션 리스크 복합
- HLB 리보세라닙+캄렐리주맙 PDUFA D-14(7/23) — K바이오 간암 1차 치료 3수, mOS 23.8 vs 15.2개월(HR 0.64), 제조 실사가 관건

## 2026-07-08
- KOSPI 이틀 연속 -5.35% — 기술적 베어마켓 진입·역사 12번째 서킷브레이커(7/7 발동, 7/8 사이드카)
- [후속] Vera Therapeutics TRUTAKNA FDA 가속승인 확정 — IgAN 최초 BAFF/APRIL 이중 억제제
- SK하이닉스 Nasdaq ADR 상장 D-2 — 역대 최대 해외기업 ADR 290억달러(약 44조원)
- Gemini 3.5 Pro 7/17 vs DeepSeek V4 7/24 — 개발자 AI 플랫폼 이중 마이그레이션 압박
- Vertex 포베타시셉트 PDUFA 2026-11-30 — IgAN 동일 기전 내 직접 경쟁

## 2026-07-07
- 삼성전자 Q2 영업이익 89.4조원(+1,810% YoY) 역대 최대 — KOSPI 사이드카·-4.9% 동시 발동(실적 역설)
- Novartis, Myricx Bio 인수 최대 $1.5B — NMTi 기반 차세대 ADC 페이로드 플랫폼(ADC 페이로드 전쟁)
- [후속] Vera 아타시셉트 PDUFA 당일(7/7) — SEC 8-K 제출 확인, 결과 미확정
- SpaceX Nasdaq 100 편입(7/7) — JPM 추산 $4.3B 패시브 매수 집중
- White House AI 자발적 표준 프레임워크 이번 주 발표 예상 — NSA 30일 사전 심사

## 2026-07-06
- KOSPI 8,000 이탈 + USTR Section 301 강제노동 관세 공청회(7/7) — 반도체 수출 최고에도 관세 프레임 전환 압력
- OpenAI, 전 트럼프 AI 보좌관 Dean Ball Strategic Futures 팀장 영입 — AI 정책·IPO 포지셔닝
- [후속] Vera 아타시셉트 PDUFA D-1(7/7) — IgAN BAFF·APRIL 이중 억제제, 내일 FDA 결정
- AI 모델 7월 대격돌 — Gemini 3.5 Pro·GPT-5.6·Grok 4.5 동시 경쟁 진입
- 미국 6월 NFP 5만 7,000명 — S&P +0.49% 강보합, 연준 고용 둔화 vs PCE 3.6% 교착

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






