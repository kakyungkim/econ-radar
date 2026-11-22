# econ-radar 주간 동향 작성 작업

대상 주: `{{WEEK}}` ({{START}} ~ {{END}})
선택 제공자: `{{PROVIDER}}`

1. `AGENTS.md`와 `.agents/skills/content-studio-orchestrator/SKILL.md`를 전부 읽고 따른다.
2. 직전 주 리포트 `vault/reports/` 최신 파일의 frontmatter, 절 구성, 분량을 그대로 따른다.
3. 대상 주의 `vault/daily/`, `vault/analysis/`, 관련 `vault/topics/`만 근거로 쓴다. 데일리에 없는 사실이나 수치를 새로 만들지 않고, 원문 링크를 유지한다.
4. 사건 나열보다 주간 구조 변화, 투자 시사점, 반대 시나리오를 보여 준다. 매수·매도 권유를 하지 않는다.
5. 결과를 `vault/reports/{{WEEK}}-동향.md`에 저장하고 `vault/reports/index.md` 목록에 한 줄을 추가한다.
6. 렌더, git, deploy.sh, 텔레그램, Buttondown은 실행하지 않는다. 바깥 스크립트와 GitHub Actions가 담당한다.
7. 최종 응답에는 만든 파일과 확인 불가 항목만 간결히 보고한다.
