# econ-radar 날짜별 생성 작업

대상 날짜: `{{DATE}}`
선택 제공자: `{{PROVIDER}}`

1. `AGENTS.md`와 `.agents/skills/econ-radar-daily-orchestrator/SKILL.md`를 전부 읽고 따른다.
2. `vault/raw/feed-{{DATE}}.json`과 `.md`, 직전 3일 데일리, 관련 주제 문서를 읽는다.
3. 필요한 최신 사실은 웹에서 직접 확인하되 신뢰할 수 있는 원문 링크를 남긴다.
4. 다음 필수 파일을 완성한다: `vault/raw/news-{{DATE}}.md`, `vault/analysis/market-{{DATE}}.md`, `vault/analysis/company-{{DATE}}.md`, `vault/daily/{{DATE}}.md`.
5. 날짜별 사실만 사용하고 과거 기사를 당일 신규 사건처럼 쓰지 않는다.
6. `scripts/render_html.py`, git, deploy.sh, 텔레그램, Buttondown은 실행하지 않는다. 바깥 파이프라인이 담당한다.
7. 최종 응답에는 만든 파일, 확인한 핵심 수치, 확인 불가 항목만 간결히 보고한다.
