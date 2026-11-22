# Provider-neutral harness improvement log

## 2026-11-11

- 실행한 요청: Claude 중단 이후 Codex 대체, 향후 제공자 전환 가능 구조
- 기대한 결과: 동일 산출물 계약을 Codex/Claude가 공유하고 실행기에서만 전환
- 적용: 공통 Orchestrator, 제공자 어댑터, 일일 관통 실행, Actions와 회귀 테스트 추가
- 다음 확인: 로컬 Codex 구독 관통 실행, GitHub Secret 설정 후 예약 실행, 누락 날짜별 중복 발송 방지

## 2026-11-11 구독 장애 대비 보강

- 실행한 요청: Claude Pro 또는 Codex 결제 중단 시 다른 제공자로 안전하게 복구
- 기대한 결과: 제공자 추적, 공통 검증, 중복 발행 방지, watchdog 복구 안내
- 적용: provider frontmatter·실행 로그, 공통 계약 검사기, 발행 전 게이트, Claude 직접 발행 제거, 블로그 push 재시도
- 다음 확인: 다음 Claude 예약 실행이 `provider: claude`와 `company-DATE.md`를 남기는지 관찰
- 2026-11-23 반영 전 점검: 11-01~11-22 실제 발행분에 게이트를 돌리자 11-16이 실패했다(분석 파일이 `2026-11-16-market.md`, `2026-11-16-companies.md`). 이름만 다른 분석 파일은 경고로 받게 고쳤다. 동시 발행 테스트가 같은 1초 안에 같은 해시 커밋을 만들어 5회 중 3회 실패하던 것도 커밋 시각을 고정해 고쳤다.
- 같은 날 고침: 발행 워크플로가 `--provider-hint claude`를 고정으로 넘겨 Codex로 만든 날(11-18~22)도 claude로 찍혔다. 워크플로에서 힌트를 빼고, frontmatter가 없으면 커밋된 실행 로그(`artifacts/runs/DATE-PROVIDER.log`)로 판단하며 로그도 없으면 unknown으로 둔다. 재검사 결과 11-18~22는 codex, 로그가 없는 11-14~17은 unknown.
