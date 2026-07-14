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

## 2026-07-14
- 이란 UAE 유조선 2척 공격·브렌트 $86.27·트럼프 20% 통행료 — 호르무즈 에스컬레이션 2일차, IMO 법적 근거 없음 반발
- 올릭스 OLX501A R&D Day — ALK7 siRNA 영장류 84% mRNA 억제·GLP-1 1/10 병용 효과·L'Oréal 1,108억 납입 완료
- Biogen diranersen CELIA Phase 2 — 1차 평가변수 미달, tau 감소·인지 신호 동시 확인, 개발 지속 결정
- Google·MS·Salesforce A2A 연합 + Microsoft MAI 자체 모델 — Anthropic MCP 대항 에이전트 인프라 표준 전쟁 공식화
- 미국 6월 CPI 컨센서스 YoY 3.8% 발표 + 워시 의회 증언(매파) + 한국은행 D-2 전문가 10인 전원 25bp 인상 전망

## 2026-07-13
- KOSPI 블랙먼데이 — 6,806.93(-8.95%), 서킷브레이커 올해 7번째, SK하이닉스 -15.37% 역대 최대 낙폭
- 미-이란 호르무즈 충돌 격화 — 브렌트유 +4.2% $79.22/배럴, 통과 선박 6척으로 급감
- Anthropic $47B ARR, OpenAI 역전 — 기업가치 $9,650억달러, Fortune 100 70% 채택
- 한국 7월 상순 수출 298억달러 역대 최고 — 반도체 +193%($112억), 실물 vs 금융 단절
- Q32 Bio bempikibart SIGNAL-AA Part B 36주 결과 발표 — anti-IL-7Rα Phase 3 논의 진입 여부

## 2026-07-12
- 한국은행 7/16 기준금리 인상 유력 — 14개월 만에 2.50%→2.75%(+25bp), BNP파리바 연말 3.00% 시나리오
- Apple, OpenAI 영업비밀 탈취 소송 — 전직 직원 400명+, Tang Tan(전 VP of Product Design·현 CHO) 피고, OpenAI IPO 리스크
- Sanofi Sarclisa Escena FDA 승인(7/9) — 세계 최초 온바디 인젝터(OBI) 항암제, 다발성골수종 3개 적응증
- Google Gemini 3.5 Flash 검색 전면 도입 — AI Mode 10억 사용자 돌파, 25년 파란 링크 시대 전환
- PADCEV+Keytruda 근침윤성 방광암 전체 환자 FDA 승인 확대 — EFS 위험 47% 감소

## 2026-07-11
- 중국 AI OpenRouter 역전 — 샤오미 MiMo-V2-Pro 21.1%·전체 1위, 미국 모델 70%→30%(18개월), MiMo API $0.435/M vs GPT $5/M
- Intel -20%·AMD -10% 7월 급락 + BoA "AI 칩 버블" 경보 — NVIDIA P/E 22배 상대 방어
- Replimune RP1 3차 BLA 수리 + AdCom 7월 말·PDUFA 8/2 — 종양용해 바이러스+니볼루맙, ORR 33.6%, DOR 24.8개월
- 코오롱티슈진 TG-C(인보사) 미국 3상(1,066명) 톱라인 이달 발표 임박 — BLA 제출 로드맵, K-바이오 유전자치료제 최선봉
- Pharvaris 듀크릭티반트 경구 HAE NDA 수리 (PDUFA 2027-04-23) — 세계 최초 경구형 발작 치료제 도전

## 2026-07-10
- HLB 리보세라닙+캄렐리주맙 FDA 3차 CRL (7/10) — Hengrui cGMP Form 483 반복, 연내 4수 도전 예고. 3수 모두 제조 문제, 임상 유효성(mOS 23.8개월 HR 0.64) 유효
- [수정] SK하이닉스 SKHYV 나스닥 첫날 실제 $168.01(+12.8%) + KOSPI 실제 7,475.94(+2.52%) — $26.5B(약 40.1조원) 역대 최대 해외 ADR
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

