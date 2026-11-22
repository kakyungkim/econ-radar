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

원고는 Codex로 만드는 것을 기본으로 한다. ChatGPT 구독 한도를 쓰므로 Claude 한도와 따로 계산된다. Codex 한도도 떨어지면 `--provider claude`로 바꾼다.

### 스크립트로 한 번에 실행

아래 1번부터 7번까지 중 AI가 필요한 것은 원고 생성뿐이고, 나머지는 `scripts/manual_publish.py`가 처리한다. 터미널에서 직접 실행하면 Claude Code 세션 토큰을 쓰지 않는다.

```bash
cd ~/projects/econ-radar
python3 scripts/manual_publish.py --dry-run           # 누락 날짜와 할 일만 출력
python3 scripts/manual_publish.py                     # 최근 14일 누락분 전부 생성, 발행
python3 scripts/manual_publish.py --weekly            # 데일리 뒤 지난 일요일이 속한 주의 동향까지
```

| 옵션 | 쓰는 경우 |
| --- | --- |
| `--dates 2026-11-18 2026-11-19` | 날짜를 직접 지정 |
| `--blog-only` | 지난 날짜 소급. push, email 파일을 빼서 텔레그램, 메일이 나가지 않음 |
| `--skip-generate` | 원고는 이미 만들어 두었고 커밋과 push만 |
| `--provider claude` | Codex 한도가 떨어졌을 때 |
| `--no-push` | 로컬 커밋까지만 하고 직접 확인 |
| `--no-wait` | Actions와 블로그 공개 확인을 기다리지 않음 |
| `--weekly 2026-W47` | 주를 직접 지정 |

스크립트가 하는 일은 다음과 같다.

- `../econ-radar-publish`에 origin/main 기준 작업 폴더를 만들거나 재사용한다. 메인 폴더의 미커밋 변경은 건드리지 않는다.
- origin/main에서 후보 수집(`feed-DATE.json`)은 있고 데일리가 없는 날짜를 오래된 순으로 고른다.
- 날짜마다 `run_daily_pipeline.py`를 돌린 뒤 그 날짜 파일과 공용 인덱스(`vault/daily/index.md`, `vault/_meta/recent-headlines.md`, `vault/topics/*.md`)만 골라 커밋한다. 다른 날짜 파일, 코드, 삭제는 고르지 않는다(`tests/test_manual_publish.py`).
- 하루씩 rebase 뒤 push하고, 그 커밋에서 블로그, 텔레그램, 메일 워크플로가 모두 성공하고 블로그 주소가 열릴 때까지 기다린다. 하나라도 실패하면 다음 날짜로 넘어가지 않는다.
- `--weekly`는 `scripts/prompts/weekly-provider.md`로 주간 동향을 만들어 push한다. 월요일 08:00 KST 예약 실행이 이미 지나갔으면 `weekly-publish.yml`을 직접 실행하고, 아직이면 예약 실행에 맡긴다. 둘 다 돌면 두 번 발송된다.

스크립트가 중간에 멈추면 원인을 고친 뒤 같은 명령을 다시 실행한다. 이미 main에 올라간 날짜는 누락 목록에서 빠지고, 작업 폴더에 남은 원고는 다시 만들지 않고 이어서 커밋한다. 아래 1번부터 7번까지는 스크립트를 쓸 수 없을 때의 손 절차다.

### 주제 노트 보완

데일리 프롬프트(`scripts/prompts/daily-provider.md`)는 원고를 쓴 뒤 `vault/topics/*.md` 타임라인과 `vault/_meta/recent-headlines.md`까지 갱신한다. 2026-11-22 전 프롬프트로 만든 날짜처럼 원고만 있고 주제 노트가 빠졌으면 날짜마다 아래 명령으로 보완한 뒤 발행한다. 데일리와 분석 파일은 고치지 않는다.

```bash
python3 scripts/run_ai_provider.py 2026-11-18 --provider codex --template scripts/prompts/topics-provider.md
```

### 매일 자동 실행으로 걸기

수동 발행 스크립트를 이 Mac의 launchd에 걸면 매일 정해진 시각에 돈다. Mac이 꺼져 있으면 돌지 않고, 잠자기였다면 깨어날 때 한 번 돈다. 클라우드 루틴(18:30 KST, 19:45쯤 끝남)과 겹치지 않게 21:30에 건다. 클라우드 루틴이 그날 데일리를 이미 올렸으면 스크립트는 누락 날짜가 없어 아무것도 하지 않는다.

1. `~/Library/LaunchAgents/com.kkkim.econ-radar-publish.plist`를 만든다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.kkkim.econ-radar-publish</string>
  <key>WorkingDirectory</key><string>/Users/kkkim/projects/econ-radar</string>
  <key>ProgramArguments</key>
  <array>
    <string>/opt/anaconda3/envs/rag/bin/python3</string>
    <string>scripts/manual_publish.py</string>
    <string>--weekly</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key><string>/Users/kkkim/.npm-global/bin:/Users/kkkim/.local/bin:/usr/local/bin:/usr/bin:/bin</string>
  </dict>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>21</integer><key>Minute</key><integer>30</integer></dict>
  <key>StandardOutPath</key><string>/Users/kkkim/Library/Logs/econ-radar-publish.log</string>
  <key>StandardErrorPath</key><string>/Users/kkkim/Library/Logs/econ-radar-publish.log</string>
</dict>
</plist>
```

2. 등록하고 한 번 바로 돌려 본다.

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.kkkim.econ-radar-publish.plist
launchctl kickstart gui/$(id -u)/com.kkkim.econ-radar-publish
tail -f ~/Library/Logs/econ-radar-publish.log
```

3. 끄려면 등록을 해제한다.

```bash
launchctl bootout gui/$(id -u)/com.kkkim.econ-radar-publish
```

- PATH에는 `codex`(`~/.npm-global/bin`), `claude`(`~/.local/bin`), `gh`(`/usr/local/bin`)가 있어야 한다. launchd는 셸 설정 파일을 읽지 않는다.
- `--weekly`는 매일 붙여도 된다. 지난 일요일이 속한 주의 리포트가 이미 있으면 아무것도 하지 않는다.
- 이미 지난 날짜를 매일 발송으로 다시 내보내지 않으려면 `--days 1`을 더해 오늘과 어제만 보게 한다.

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
