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

```bash
git add vault/raw vault/analysis vault/daily vault/html vault/push vault/email vault/topics
git commit -m "econ-radar: YYYY-MM-DD 데일리 발행"
git push origin main
```

push 뒤 채널별 재실행이 필요하면 GitHub Actions에서 날짜를 넣어 `Daily Blog Publish`, `Telegram Daily Push`, `Email Daily Push (Buttondown)`을 실행한다. 이메일은 `send=now` 또는 `send=1`을 선택한다.

## 전환 확인

```bash
python3 scripts/run_ai_provider.py 2026-11-11 --provider codex --dry-run
python3 scripts/run_ai_provider.py 2026-11-11 --provider claude --dry-run
python3 -m pytest -q tests/test_ai_provider_switch.py
```
