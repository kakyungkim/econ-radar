# HANDOFF — econ-radar (2026-06-10)

오늘 데일리 발행 준비 + 하네스 대폭 개선 + 블로그 글 작성(미발행)까지 진행했다. 작업은 두 repo + 글로벌 스킬에 걸쳐 있다.

## 완료

### 1. 데일리 2026-06-10
전 파이프라인 실행: news-scout → market-analyst ∥ company-scout → newsletter-editor → style-critic → report-renderer → knowledge-curator.
- 로컬(gitignore): `vault/{raw,analysis,daily,topics}/*-2026-06-10.*`
- 추적: `vault/html/2026-06-10.html`, `vault/push/2026-06-10.md`

### 2. 하네스 구조 변경 (durable)
- **3렌즈: 산업·투자·유망 기업** (커리어 교체). 신규 `company-scout` 에이전트. CLAUDE.md·orchestrator·newsletter-editor 배선 완료.
- **문체 기준선**: 실제 한국 경제기사 표본 `vault/_meta/korean-style-samples.md` → newsletter-editor·style-critic 의무 참조. 규칙: 사건 과거형 · 금액 원화 병기 · 외래어 한글(영문) 병기 · 한 섹션 종결어미 통일.
- **핵심 항목**: `Key Point`(객관 사실) + `💡 Insight`(주관 의견) 분리. 심층 분석 라벨은 `관전 포인트`.
- **시각(report-renderer)**: Pretendard 폰트 · 딥 인디고 통일 + 청록(teal) 포인트 · 히어로 이미지 base64 인라인(브라우저 무관) · 발음 버튼은 voice-icon SVG 인라인 + 자연 음성 선택 · PC 폭 820px/모바일 반응형.
- **image-prompt-smith** 신규: 이미지는 직접 그리지 않고 외부 생성 AI 프롬프트로.
- 케이스스터디: `vault/_meta/2026-06-10-harness-iteration-casestudy.md` (발표·포스팅용).

### 3. 블로그 (~/kakyungkim.github.io) — 커밋만, **push 안 함**
- 한/영 빌드 노트: `_posts/{kr,en}/2026-06-10-econ-radar-agent-harness.md`
- 공개 아카이브 사이트: `econ-radar/` (index.html + 2026-06-10.html + og.jpg)
- 발행 시 링크: `/kr|/en/2026/06/10/econ-radar-agent-harness/`, `/econ-radar/`

### 4. 글로벌 스킬
- `~/.claude/skills/blog-post/` — 프로젝트 → 한/영 블로그 글 + 링크드인 티저 + Pages 호스팅 재사용 하네스.

## 보류 / 다음 (→ TODO.md)
- econ-radar 디자인 추가 손질(색·레이아웃 미세조정)
- 블로그 + econ-radar 사이트 **push(공개)** — 사람 승인 대기
- (선택) 링크드인 글 게시 / 데일리 푸시 메시지 발송

## 주의
- `.gitignore`: `vault/{raw,analysis,daily,topics,blog,book,reports}` = 로컬 전용. `html·push`만 추적.
- 외부 발송·발행은 **항상 사람 승인 뒤**. 블로그는 미발표 연구·동료·내부 repo 비공개, 본인 기여만 정확히.
- `vault/2026-06-10.bk2.html`은 스크래치 백업(커밋 제외).
