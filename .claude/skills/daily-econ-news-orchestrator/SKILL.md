---
name: daily-econ-news-orchestrator
description: econ-radar의 매일 뉴스 파이프라인 입구. "오늘 경제 뉴스 정리/뉴스레터/데일리", "오늘 뉴스 모아줘", "이번 주 바이오만", "투자 파트만 다시", "어제 이어서" 같은 일일 수집·분석·뉴스레터·HTML·푸시 요청에서 사용한다. 신뢰 경제지(국내외) 기반, 해외 기사 한국어 번역, 산업구조·투자(코스피+해외)·커리어 3렌즈로 정리하고 vault에 누적한다.
---

# daily-econ-news-orchestrator (1층 진행표 / 팀장)

매일 경제 뉴스를 수집→분석→뉴스레터→HTML·푸시로 만들고 vault에 누적하는 Agent Team을 지휘한다.

## 언제 이 스킬을 쓰나
- 초기 실행: "오늘 뉴스레터 만들어줘", "오늘 econ-radar 돌려줘".
- 부분 재실행: "투자 파트만 다시", "HTML만 다시 렌더".
- 연속: "어제 주제 이어서", "이번 주 바이오만".

## 실행 모드 분기 (먼저 확인)
1. `vault/raw/`, `vault/daily/`에서 **오늘 날짜** 산출물이 있는지 본다.
2. 분기:
   - 없음 → **초기 실행**(전체 파이프라인).
   - 있음 + 특정 부분 요청 → **부분 재실행**(해당 단계만, 나머지는 기존 파일 재사용).
   - "이어서"/기간 한정 → 해당 범위로 수집·분석.

## 팀 구성 (Agent Team)
news-scout, market-analyst, company-scout, newsletter-editor, style-critic, report-renderer, knowledge-curator.

## 품질 기준선
- `vault/_meta/benchmarks.md`의 "바로 반영할" 체크리스트를 품질 기준으로 삼는다(Why it matters 한 줄, 1차 자료 직접 링크, 양면 시각, 항목당 분량 상한, 재사용 전략 프레임). 이 파일이 없거나 오래됐으면 benchmark-scout를 먼저 돌릴 것을 제안한다.

## 실행 흐름
1. `TeamCreate`로 위 7명을 팀으로 만든다.
2. `TaskCreate`로 단계·의존관계 등록:
   - T1 수집(news-scout) → `vault/raw/`
   - T2 산업·투자 분석(market-analyst, T1 의존) → `vault/analysis/market-*`
   - T3 유망 기업 분석(company-scout, T1 의존) → `vault/analysis/company-*`  ※ T2와 병렬
   - T4 통합(newsletter-editor, T2·T3 의존) → `vault/daily/*`
   - **T4.5 문체 검수(style-critic, T4 의존) → `vault/daily/*` 윤문** (발행 전 AI스러운 표현 제거)
   - T5 렌더(report-renderer, T4.5 의존) → `vault/html/*.html`, `vault/push/*`
   - T6 vault 정리(knowledge-curator, T4.5 의존) → `vault/topics/*` 갱신
3. 팀원은 `TaskUpdate`로 진행/차단/완료를 갱신하고, `SendMessage`로 발견·출처 보강 요청을 주고받는다.
4. 팀장은 `TaskGet`으로 지연·차단을 확인하고, 막히면 재할당하거나 사람에게 알린다.
5. 각 산출물은 파일로 남긴다(대화로만 끝내지 않는다).

## 사람 승인 게이트
- 파일 생성(뉴스레터·HTML·푸시)은 자동.
- **외부 발송(메일·메신저로 푸시 전송, 뉴스레터 발행)은 사람 승인 뒤**에만. 팀장은 "발송 준비됨 — 보낼까요?"로 확인을 받는다. 절대 자동 발송하지 않는다.

## 마무리
- knowledge-curator까지 끝나면 `vault/_meta/improvement-log.md`에 오늘 실행 메모(빠진 소스, 약했던 분야)를 남긴다.
- `TeamDelete`로 팀을 정리한다.

## 산출물 계약
| 단계 | 파일 | 다음 단계가 읽음 |
| --- | --- | --- |
| 수집 | `vault/raw/news-YYYY-MM-DD.md` | 분석가 |
| 분석 | `vault/analysis/{market|company}-YYYY-MM-DD.md` | 편집자 |
| 통합 | `vault/daily/YYYY-MM-DD.md` | 렌더러·큐레이터·(3층) |
| 렌더 | `vault/html/*.html`, `vault/push/*.md` | 사람(읽기/발송) |
| 정리 | `vault/topics/*.md` | 내일 수집·3층 저술 |

## 실패 시
- 한 단계 실패 시 그 단계만 재시도. 두 번 실패하면 사람에게 알리고 부분 산출물을 남긴다.
