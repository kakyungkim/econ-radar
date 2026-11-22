# AI provider 전환 운영법

## 로컬: 구독 로그인 사용

이 컴퓨터에서 Codex 또는 Claude Code 로그인이 유지돼 있으면 별도 API 키 없이 각 구독 한도 안에서 실행할 수 있다.

```bash
AI_PROVIDER=codex python3 scripts/run_daily_pipeline.py 2026-11-11
AI_PROVIDER=claude python3 scripts/run_daily_pipeline.py 2026-11-11
```

기존 날짜를 의도적으로 다시 만들 때만 `--force`를 붙인다.

## GitHub Actions: 무인 실행

- Variable `AI_PROVIDER`: `codex` 또는 `claude`
- Codex 선택: Secret `OPENAI_API_KEY`
- Claude 선택: Secret `ANTHROPIC_API_KEY`
- 블로그: Secret `BLOG_DEPLOY_TOKEN`
- 기존 발송: `TELEGRAM_BOT_TOKEN`, `BUTTONDOWN_API_KEY`

GitHub 호스팅 러너는 로컬 구독 로그인 세션을 이어받지 않는다. 비용을 구독 안으로 제한하려면 로컬에서 위 명령을 실행하고 결과를 push한다.

## 수동 발행

자동 루틴이 원고를 만들지 못했거나 발행 일부가 실패했을 때 로컬에서 이어받는 절차다. 발행 구조는 두 단계로 나뉜다. 원고(`vault/daily`, `vault/html`, `vault/push`, `vault/email` 등)를 만드는 일은 AI가 하고, main에 push된 원고를 블로그, 텔레그램, 메일로 내보내는 일은 GitHub Actions가 한다. 뉴스 후보 수집(`vault/raw/feed-DATE.{json,md}`)도 Actions가 따로 돌린다. 그래서 어느 단계에서 멈췄는지에 따라 손댈 곳이 다르다.

| 상황 | 증상 | 할 일 |
| --- | --- | --- |
| 원고 미생성 | 구독·토큰 한도, 루틴 실패나 중단, 러너 장애로 "뉴스 후보 수집" 커밋만 있음 | 1번부터 4번까지, 끝나면 7번 |
| 원고 재작성 | 이미 발행한 날짜의 내용을 고쳐 다시 내야 함 | 3번에서 `--force`, 4번에서 발송 여부 결정 |
| 발행만 실패 | 원고 커밋은 있는데 블로그 404, 텔레그램이나 메일 미수신 | 5번만 |
| 지난 날짜 소급 | 오래된 날짜를 블로그에만 남김 | 1번부터 4번까지(push와 email 파일 제외), 끝나면 7번 |
| 주간 동향 누락 | `vault/reports/`에 지난주 리포트가 없음 | 6번 |

원고는 Codex로 만드는 것을 기본으로 한다. ChatGPT 구독 한도를 쓰므로 Claude 한도와 따로 계산된다. Codex 한도도 떨어지면 `AI_PROVIDER=claude`로 바꾼다.

### 1. 누락 날짜 확인

```bash
cd ~/projects/econ-radar
git fetch origin
git log --oneline origin/main -20
```

"뉴스 후보 수집" 커밋만 있고 "자동 생성"이나 "데일리 생성" 커밋이 없는 날짜가 누락분이다.

### 2. 별도 작업 폴더 생성

메인 폴더에는 다른 세션이 커밋하지 않은 변경이 남아 있을 수 있으므로 origin 기준으로 작업 폴더를 따로 만든다.

```bash
git worktree add -b backfill ../econ-radar-backfill origin/main
cd ../econ-radar-backfill
```

### 3. 날짜별 원고 생성

```bash
AI_PROVIDER=codex python3 scripts/run_daily_pipeline.py 2026-11-18
```

- 조사, 분석, 원고 작성, HTML 렌더, 시장 수치 점검, 회귀 테스트까지 한 번에 돌고 날짜당 20분에서 40분쯤 걸린다.
- 이미 있는 날짜는 건너뛴다. 의도적으로 다시 만들 때만 `--force`를 붙인다.
- 여러 날이 빠졌으면 오래된 날짜부터 하나씩 순서대로 돌린다. 직전 데일리를 읽어 중복 기사를 거르기 때문이다.

### 4. 하루씩 커밋하고 push

대상 날짜 파일과 인덱스, 실제로 바뀐 주제 파일만 골라 stage한다. 날짜 폴더 전체를 한꺼번에 stage하지 않는다.

```bash
git status --short
D=2026-11-18
git add vault/raw/*$D* vault/analysis/*$D* vault/daily/$D.md vault/daily/index.md \
        vault/html/$D.html vault/push/$D.md vault/email/$D.html artifacts/runs/$D-codex.log
git add vault/topics   # 실제로 바뀐 주제 파일만
git commit -m "econ-radar: $D 데일리 발행"
git push origin backfill:main
```

- **반드시 하루치씩 따로 push한다.** 블로그와 텔레그램 워크플로는 한 번의 push에서 날짜 하나(가장 늦은 날짜)만 감지하므로, 여러 날을 묶어 올리면 마지막 날만 발행된다.
- 다음 날짜는 Actions 세 개(블로그, 텔레그램, 메일)가 끝난 뒤에 올린다. 상태는 `gh run list --limit 5`로 본다.
- 지난 날짜를 블로그에만 올리고 구독자 발송은 하지 않으려면 `vault/push`, `vault/email` 파일을 빼고 커밋한다. push 파일이 main에 들어가면 텔레그램과 메일이 자동으로 나간다.

### 5. 채널별 재실행

push 뒤 특정 채널만 다시 보내야 하면 날짜를 넣어 직접 실행한다.

```bash
gh workflow run "Daily Blog Publish" -f date=2026-11-18
gh workflow run "Telegram Daily Push" -f date=2026-11-18
gh workflow run "Email Daily Push (Buttondown)" -f date=2026-11-18 -f send=1
```

메일의 `send=1`은 다음 날 아침 예약 발송, `send=now`는 즉시 발송이다.

### 6. 주간 동향

주간 동향은 데일리처럼 한 번에 돌리는 스크립트가 없다. `.agents/skills/content-studio-orchestrator/SKILL.md`에 따라 `vault/reports/YYYY-Www-동향.md`를 만들어 push하면, 월요일 08:00 KST 예약 워크플로가 지난주분을 발행한다. 예약 실행이 지난 뒤에 올렸으면 직접 실행한다.

```bash
gh workflow run weekly-publish.yml -f period=2026-W47 -f send=1
```

### 7. 작업 폴더 정리

```bash
cd ~/projects/econ-radar
git worktree remove ../econ-radar-backfill
git branch -D backfill
git pull
```

## 전환 확인

```bash
python3 scripts/run_ai_provider.py 2026-11-11 --provider codex --dry-run
python3 scripts/run_ai_provider.py 2026-11-11 --provider claude --dry-run
python3 -m pytest -q tests/test_ai_provider_switch.py
```
