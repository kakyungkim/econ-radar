---
type: meta
tags: [운영, dedup]
---
# 최근 헤드라인 (recent-headlines) — 중복 회피 기준

클라우드 routine은 과거 vault(raw·analysis·daily·topics)에 접근할 수 없다(로컬 전용, gitignore). 그래서 **이 파일이 "이미 다룬 뉴스" 기준선**이다. 데일리 생성 시 규칙:

1. **시작할 때** 이 파일을 읽는다. 여기 적힌 항목은 **이미 다뤘으므로 다시 헤드라인으로 올리지 않는다.** 단, 그 사건에 **새로운 후속 전개**(승인 결과·딜 종결·실적 등)가 나왔으면 "후속/업데이트"로만 짧게 다룬다.
2. **끝낼 때** 오늘 핵심 5가지 제목을 아래 `## YYYY-MM-DD` 블록으로 **맨 위에 추가**하고, **최근 7일치만 남기고** 그 이전 블록은 지운다. 이 파일도 함께 커밋한다.

> 사람이 손으로 만든 발행본도 여기 반영한다(아래 6/10·6/11은 수작업 발행분).

---

## 2026-06-21
- DATROWAY(Dato-DXd) FDA TNBC 1선 승인 — TROP2 ADC 최초 1선, mOS 23.7개월 vs 18.7개월, ORR 64% vs 30%, NCCN Category 1
- Elicio ELI-002 7P 전이성 췌장암 완전반응 3명/3명 — KRAS mRNA 백신 + 면역관문억제제 순차 요법, AMPLIFY-7P 2상
- Nvidia Vera CPU 양산 — AI 에이전트 전용, 88 Olympus 코어, x86 대비 1.8배, OpenAI·Anthropic 납품
- 코스피 9,052 + 한국 5월 수출 877.5억달러 역대 최대 — 반도체 수출 169.4% 급증(371.6억달러)
- BIO USA 2026 개막 D-1 + GPT-5.6 출시 83% 확률(Polymarket) — 내일(6/22) 동시 이벤트

## 2026-06-20
- cytisinicline FDA CRL — 약효 데이터 건재, CMO cGMP OAI 판정이 허가 차단. 이미 Adare로 제조 이전 완료, Q4 2026 NDA 재제출·H1 2027 출시 예정
- BIO USA 2026 D-2 — K바이오 51개사, 서울대병원 병원 첫 단독 부스, ABL Bio·삼성바이오 Rockville·Rznomics 파트너링
- 유한양행 창립 100주년(6/20) — 'Great & Global' 비전, 렉라자 1Q 글로벌 $2.57억(+82.7%), 글로벌 톱 50 목표
- AI 모델 대전 6월 말 집중 — Claude Fable 5(6/9 출시), Gemini 3.5 Pro(3주째 미출시), GPT-5.6(6/22~28 출시 확률 83~90%)
- Moderna MFLUSIVA 주간 +28% + 브렌트유 $80.59 반등 — 이란 호르무즈 보험 의무 발언, 8/5 FDA 최종 결정 대기

## 2026-06-19
- Moderna MFLUSIVA VRBPAC 9-0 만장일치 권고 — mRNA 독감 백신 FDA 최종 결정 8/5, 3상 표준 백신 대비 효능 26.6%·응급실·입원 예방 47.9%
- Lilly Foundayo(orforglipron) 2형 당뇨 NDA Q2 2026 제출 예정 — 비만에 이어 두 번째 적응증, 식사 제한 없는 유일한 경구 GLP-1
- 미·이란 MOU 전자 서명 발효·스위스 서명식 취소 — 브렌트유 $75(4월 고점 대비 -38%), 핵 문제 미결
- K바이오 51개사 BIO USA 2026 출격 — Rznomics RNA 편집 FDA RMAT 3관왕(간세포암), 삼성바이오 Rockville 미국 생산시설 전면 부각
- 유한양행 창립 100주년 D-1 — 렉라자 1Q 글로벌 매출 $2.57억(+82.7%), 2030 비전 발표 예정

## 2026-06-18
- 코스피 사상 첫 9,000 돌파(종가 9,063.84) — SK하이닉스 HBM4E 출하 공식화·주가 +6.98% 신고가
- Utebzi(tebipenem) FDA 승인 — 미국 최초 경구 카바페넴, 30년 만에 입원 의존 구조에 균열
- Lilly retatrutide 80주 28.3% 체중 감소(triple-G ADA 2026) — 현재 허가 비만약 최고 수치
- Anthropic, Coefficient Bio $4억 인수 — AI가 신약개발 밸류체인 내부로 직접 진입
- Moderna mRNA-1010 VRBPAC 심의 개시 — mRNA 플랫폼 계절 독감 백신 첫 허가 시험대

## 2026-06-17
- FOMC 중립 전환 확인 — 완화 편향 삭제, 워시 의장 점도 미제출, 점도표 2026년 인하 0회(3월 1회→후퇴)
- SK하이닉스 HBM4E 샘플 출하 6~7월로 조기 당김 — 주가 7% 급등, TSMC 3nm 베이스 다이 채택
- tebipenem PDUFA 6/18(내일) — 미국 최초 경구 카바페넴 첫 FDA 결정 임박
- AI 신약발견 '비선택의 해' — 임상 200개+·FDA 승인 0건, Recursion-Exscientia 통합 파이프라인
- K-바이오 BIO USA + 삼성바이오 록빌 거점 — 상반기 기술수출 13조 원, 첫 미국 생산기지 완료

## 2026-06-16
- ABL Bio, Eli Lilly와 BBB 셔틀 플랫폼 26억달러(약 3조6,000억원) 기술이전 — Grabody-B IGF1R 기반, K-바이오 최대급
- 바이오 M&A 집중 — 이번 주 4건: GSK-Nuvalent $10.6B, J&J-Firefly $1B(KRAS DAC), Incyte-Vega $1.25B, ABL Bio-Lilly $2.6B
- FOMC 6월 회의 — 동결 확실·내부 3명 이견 노출, 결과·점도표는 6/17 발표
- Medicare GLP-1 Bridge 7월 시행 — 월 50달러(약 6만9,000원), 메디케어 수혜자 6,500만명 접근
- OpenAI, 1조달러(약 138조8,000억원) 밸류에이션 기밀 IPO 신청 — Goldman·MS·JPMorgan 주관

## 2026-06-15
- 미·이란 합의 완료 선언 — 호르무즈 즉각 개방, 6월 19일 스위스 서명식, 브렌트 80달러 초반
- 노바티스 del-brax FSHD 임상 1/2상 바이오마커 성공 — AOC 플랫폼(Avidity 120억달러) 첫 외부 검증
- FOMC 6/16~17 — 워시 신임 의장 첫 회의, 동결 확률 99.6%, 스탠스 전환·점도표 주목
- SK하이닉스 HBM4 60~70% 다년 계약 + 트럼프 H200 중국 10개사 부분 재개
- Spero tebipenem PDUFA 6/18 + Kardigan IPO 6/18 — 바이오 카탈리스트 집중일


