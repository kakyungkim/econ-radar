# econ-radar 날짜별 생성 작업

대상 날짜: `{{DATE}}`
선택 제공자: `{{PROVIDER}}`

1. `AGENTS.md`와 `.agents/skills/econ-radar-daily-orchestrator/SKILL.md`를 전부 읽고 따른다.
2. `vault/raw/feed-{{DATE}}.json`과 `.md`, 직전 3일 데일리, 관련 주제 문서, `vault/_meta/recent-headlines.md`를 읽는다. recent-headlines에 있는 사건은 새 전개가 있을 때만 "후속"으로 짧게 다룬다.
3. 필요한 최신 사실은 웹에서 직접 확인하되 신뢰할 수 있는 원문 링크를 남긴다.
4. 다음 필수 파일을 완성한다: `vault/raw/news-{{DATE}}.md`, `vault/analysis/market-{{DATE}}.md`, `vault/analysis/company-{{DATE}}.md`, `vault/daily/{{DATE}}.md`.
5. 지식 노트를 갱신한다(데일리를 다 쓴 뒤).
   - 데일리 핵심 항목마다 관련 `vault/topics/*.md`(기존 파일 우선)를 찾아 `## 타임라인` 맨 위에 기존 형식대로 `### {{DATE}} [[daily/{{DATE}}]]` 블록과 한두 줄 요약, 관련 주제 링크(`→ [[topics/...]]`)를 넣고 frontmatter `updated`를 `{{DATE}}`로 바꾼다. 흐름이 바뀌었으면 타임라인 위 요약 불릿도 고친다.
   - 새 주제 파일은 기존 파일로 담을 수 없을 때만 같은 frontmatter 형식으로 만든다.
   - `vault/_meta/recent-headlines.md`에 `## {{DATE}}` 블록(핵심 5개, 후속이면 `[후속]`)을 맨 위에 추가하고 최근 7일치만 남긴다.
6. 날짜별 사실만 사용하고 과거 기사를 당일 신규 사건처럼 쓰지 않는다.
7. `scripts/render_html.py`, git, deploy.sh, 텔레그램, Buttondown은 실행하지 않는다. 바깥 파이프라인이 담당한다.
8. 최종 응답에는 만든 파일, 확인한 핵심 수치, 확인 불가 항목만 간결히 보고한다.
