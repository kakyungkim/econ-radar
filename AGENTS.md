# econ-radar provider-neutral harness

이 저장소는 같은 산출물 계약을 Codex와 Claude에서 공통으로 사용한다. AI 제공자는 실행기에서만 선택하고, 뉴스레터 형식·검증·렌더·발행 경로는 공유한다.

## 자연어 라우팅

- "오늘 뉴스 정리", "데일리 발행", "누락분 복구", "econ-radar 돌려줘" 요청은 `.agents/skills/econ-radar-daily-orchestrator/SKILL.md`를 먼저 읽고 따른다.
- "주간/월간 동향", "블로그/책 초안" 요청은 `.agents/skills/content-studio-orchestrator/SKILL.md`를 먼저 읽고 따른다.
- 제공자 전환은 `AI_PROVIDER=codex` 또는 `AI_PROVIDER=claude`로만 한다. 제공자별 프롬프트를 따로 만들어 산출물 규칙이 갈라지지 않게 한다.

## 주요 위치

- 공통 실행 매뉴얼: `.agents/skills/`
- Codex 역할 카드: `.codex/agents/`
- Claude 기존 역할 카드: `.claude/agents/`
- 공통 실행기: `scripts/run_ai_provider.py`
- 일일 관통 실행: `scripts/run_daily_pipeline.py`
- 실행 기록: `artifacts/runs/`
- 지식 자산과 최종 산출물: `vault/`

## 운영 원칙

- AI는 조사·분석·원고 파일만 만든다. `git push`, 블로그 배포, 텔레그램·이메일 발송은 결정적 스크립트나 GitHub Actions가 맡는다.
- 수치·날짜·승인·임상 결과에는 직접 근거 URL을 남긴다. 확인하지 못한 내용은 추측하지 않고 `확인 필요`로 표시한다.
- 기존 날짜를 다시 실행할 때는 `--force` 없이는 덮어쓰지 않는다.
- 외부 발행은 사용자가 명시적으로 요청했거나 이미 승인한 예약 워크플로에서만 수행한다.
- 투자 정보는 시나리오와 위험으로 제시하며 매수·매도 권유를 하지 않는다.
- 사용자가 만든 미추적 파일과 관련 없는 변경은 건드리지 않는다.

## 제공자 선택

```bash
# 로컬 Codex 로그인/구독 사용
AI_PROVIDER=codex python3 scripts/run_daily_pipeline.py 2026-11-11

# 로컬 Claude 로그인 또는 API 설정 사용
AI_PROVIDER=claude python3 scripts/run_daily_pipeline.py 2026-11-11
```

GitHub Actions에서는 저장소 변수 `AI_PROVIDER`로 전환한다. 호스팅 러너는 구독 로그인 세션을 공유하지 않으므로 선택한 제공자의 API 자격 증명이 필요하다.

## 하네스 변경 이력

| 날짜 | 변경 내용 | 대상 | 사유 |
| --- | --- | --- | --- |
| 2026-11-11 | Codex/Claude 전환 가능한 공통 하네스 추가 | `AGENTS.md`, `.agents`, `.codex`, 실행기, Actions | Claude 무료 전환 이후 중단된 발행 복구 및 제공자 종속 제거 |
