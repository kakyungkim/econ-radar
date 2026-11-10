---
name: econ-radar-daily-orchestrator
description: econ-radar의 날짜별 뉴스 수집, 분석, 데일리 원고, 사실·문체 검증, HTML·푸시 렌더를 Codex 또는 Claude로 공통 실행할 때 사용한다. "오늘 뉴스", "데일리 발행", "누락분 복구", "econ-radar 돌려줘" 요청에서 우선 적용한다.
---

# econ-radar daily orchestrator

## 목적

선택한 AI 제공자와 무관하게 동일한 입력, 중간 산출물, 검증 기준과 렌더러를 사용해 날짜별 데일리를 만든다. AI는 외부 발송이나 Git push를 하지 않는다.

## 실행 모드

1. 대상 날짜 `YYYY-MM-DD`를 확정한다.
2. `vault/daily/DATE.md`가 있으면 부분 재실행 요청인지 확인한다. 명시적 `--force` 없이는 덮어쓰지 않는다.
3. `vault/raw/feed-DATE.{json,md}`가 없으면 `scripts/collect_news.py DATE`로 입력 후보를 만든다.
4. 기존 `vault/raw/news-DATE.md`가 있으면 재사용하고, 없으면 후보를 선별·보강한다.

## 실행 흐름

### Phase 0. 입력 확인

- `vault/raw/feed-DATE.md`와 JSON을 읽는다.
- 직전 3일 `vault/daily/`와 관련 `vault/topics/`를 읽어 중복과 후속 전개를 구분한다.
- `vault/_meta/benchmarks.md`, `vault/_meta/korean-style-samples.md`, `scripts/NEWSLETTER-FORMAT.md`를 품질 기준으로 사용한다.

### Phase 1. 조사

- 원문 또는 신뢰할 수 있는 1차 자료로 날짜·수치·사건을 확인한다.
- 해외 기사는 한국어로 요약한다.
- 사실, 전망, 필자의 해석을 구분한다.
- 결과를 `vault/raw/news-DATE.md`에 저장한다.

### Phase 2. 분석

- 산업구조·투자·수요 렌즈를 `vault/analysis/market-DATE.md`에 저장한다.
- 주목 기업과 관전 지표를 `vault/analysis/company-DATE.md`에 저장한다.
- 매수·매도 권유를 하지 않는다.

### Phase 3. 통합

- `vault/daily/DATE.md`를 `scripts/NEWSLETTER-FORMAT.md` 계약에 맞춰 작성한다.
- 기존 뉴스레터의 섹션 구조와 분량을 따른다.

### Phase 4. 검토

- 출처 없는 수치, 기사 날짜가 불분명한 항목, 단일 출처의 중대한 주장, 미래 시점 정보를 표시하고 보강한다.
- AI 상투구, 반복, 과장, 매수·매도 표현을 제거한다.
- 검증한 핵심 수치와 미확인 항목을 HTML 주석으로 문서 끝에 남긴다.

### Phase 5. 지식 연결

- 기존 주제 문서가 있는 링크만 우선 사용한다.
- 새 주제 파일이 꼭 필요하면 최소한의 근거와 날짜 링크를 포함해 만든다.
- `vault/daily/index.md`를 기존 규칙에 맞게 갱신한다.

### Phase 6. 결정적 후처리

AI 실행이 끝난 뒤 바깥 실행기가 필수 파일 확인, 렌더, 시장 수치 검사, 테스트, 승인된 배포를 담당한다.

## 산출물 계약

| 단계 | 파일 | 다음 단계 |
| --- | --- | --- |
| 후보 | `vault/raw/feed-DATE.{json,md}` | 조사 |
| 조사 | `vault/raw/news-DATE.md` | 분석 |
| 분석 | `vault/analysis/{market,company}-DATE.md` | 통합 |
| 통합 | `vault/daily/DATE.md` | 검토·렌더 |
| 렌더 | `vault/html/DATE.html`, `vault/push/DATE.md`, `vault/email/DATE.html` | 배포 워크플로 |
| 기록 | `artifacts/runs/DATE-PROVIDER.log` | 장애 분석·개선 |

## 실패 처리

- 입력 후보가 너무 적으면 과거 뉴스를 새 기사처럼 채우지 않는다.
- 핵심 수치를 확인하지 못하면 단정적 문장에서 제외한다.
- 한 단계 실패 시 기존 산출물을 삭제하지 않는다.
- 모델은 `git commit`, `git push`, `deploy.sh`, 텔레그램·Buttondown API를 직접 실행하지 않는다.

## 회귀 테스트

| 유형 | 입력 | 기대 결과 |
| --- | --- | --- |
| 정상 | 후보가 충분한 새 날짜 | raw→analysis→daily 파일 생성 |
| 애매함 | 후보가 거의 없는 날짜 | 확인 필요를 남기고 과거 기사 재포장 금지 |
| 실패 위험 | 출처 없는 시장 급등 수치 | 원고 제외 또는 명시적 검증 보류 |
| 반복 | 이미 생성된 날짜 | `--force` 없으면 무변경 종료 |
