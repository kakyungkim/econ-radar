# TODO — econ-radar

## 바로 다음
- [ ] econ-radar HTML 디자인 추가 손질 (색 포인트·레이아웃 미세조정).
- [ ] 블로그 글 + econ-radar 사이트 **push(공개)** — 확정 시. push 후 1~2분이면 GitHub Pages 빌드 완료.
  - 링크: `/kr/2026/06/10/econ-radar-agent-harness/`, `/en/...`, `/econ-radar/`, `/econ-radar/2026-06-10.html`
- [ ] (선택) 링크드인 글 게시 — 본문은 영어 티저, **블로그 링크는 첫 댓글에**.
- [ ] (선택) 데일리 푸시 메시지(`vault/push/2026-06-10.md`) 외부 발송 — 사람 승인 후.

## 매일 운영 (자동화 검토)
- [ ] 데일리 발행 시: 렌더된 HTML을 `~/kakyungkim.github.io/econ-radar/`에 복사 + `index.html`에 한 줄 추가 + push. → 오케스트레이터에 "배포" 단계로 넣어 자동화.

## 하네스 개선 (improvement-log 발췌)
- [ ] `투자테마` vs `투자전략` MOC 중복 정리(역할 분리 또는 통합).
- [ ] `유망기업` vs `신약개발전략` 바이오 기업 서술 중첩 정리(기업 단위 vs R&D 관점).
- [ ] 커리어 렌즈 중단 → '일의 미래' 테마를 3층 저술로 핸드오프하는 규칙 정의.
- [ ] **수요 렌즈(Demand) (C) 본격화** — `demand-analyst`(수요 분석가) 에이전트 신설해 market-analyst와 **병렬**로 돌리고, 뉴스레터에 네 번째 렌즈로 편입. (A) 오버레이 운영해 보고 효과 있으면 승격. 기준선: `vault/_meta/demand-lens.md`. 파이프라인(daily-orchestrator 진행표)·문체 기준선·HTML 렌더(report-renderer)·newsletter-editor 통합 양식까지 손봐야 함.
