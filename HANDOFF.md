# HANDOFF — econ-radar (2026-07-05)

이메일 결송 사고(7/2~7/4) 복구 세션. 원인 규명, 밀린 발송, 실패 알림 시스템 구축까지 완료된 시점의 체크포인트. (이전 체크포인트 2026-06-10분은 git 이력 참조.)

## Objective
7/2~7/4 데일리 이메일 3건이 발송되지 않은 원인을 찾아 복구하고, 같은 유형의 사고가 조용히 지나가지 않도록 실패 알림·진단 체계를 만든다.

## Current status — 모두 해결됨
- **원인**: 7/2에 켠 `EMAIL_TAG=econ-radar`(태그 필터 발송)가 HTTP 422 유발. 진짜 원인은 태그값 형식이 아니라 **Buttondown 무료 플랜에 태그 기능 자체가 없음**. 7/4 클라우드 세션의 하이픈 수정 2회(74d9276, befbb4f)는 헛짚음.
- **복구**: 레포 Variable `EMAIL_TAG` 삭제 → 전체 발송 복귀. draft 검증 통과.
- **밀린 발송**: 7/2·7/3·7/4치를 "뒤늦게 보내드립니다" 안내 배너(EMAIL_NOTICE) 붙여 draft 재생성 → **사용자가 3건 모두 수동 발송 완료**(2026-07-05).
- **실패 알림 시스템 가동**: 세 발행 워크플로 실패 시 런북 진단 → GitHub Issue 자동 생성 + 텔레그램 개인 DM. 가짜 날짜(2030-01-01) 실패 주입으로 Issue 생성·DM 도착까지 검증 완료. 테스트 이슈 6건은 닫음.
- 발송 수신자 약 20명(unactivated 1명은 주소 오타 추정, 20명 기준으로 정리하기로 사용자 결정).

## Files modified (이 세션, 모두 origin/main에 push됨)
- `scripts/send_email.py` — EMAIL_TAG를 유료 전용으로 명시(docstring), `EMAIL_NOTICE`(1회성 안내 배너, body 뒤 600px 노란 박스) 추가.
- `scripts/notify_failure.py` — 신규. 실패 로그를 런북과 대조해 원인·조치 진단, Issue 생성 + TG DM. 새 실패 유형은 RUNBOOK 리스트에 추가.
- `scripts/subscriber_stats.py` — 신규. 구독자 상태별 집계(읽기 전용). regular(+premium·gifted)만 발송 대상.
- `.github/workflows/{email-push,telegram-push,weekly-publish}.yml` — 로그 캡처(tee)+`if: failure()` 알림 스텝, `permissions: issues: write`, email-push에 `notice` 입력.
- `CLAUDE.md` — 안전선에 "발송 경로 변경 후 그 자리에서 draft 1회 관통 검증" 규율 추가.
- `vault/_meta/improvement-log.md` — 2026-07-05 항목 4개(사후 분석 / 재발송·수신자 / 알림 시스템 / 검증기·DM 시행착오). **블로그 시행착오 모음 소재로 사용자가 발행 예정.**

주요 커밋: 9421ba6(사후 분석) → 6de1dfb(EMAIL_NOTICE) → f8902c3(subscriber_stats) → c3fd042(알림 시스템) → 652bb5a·a07ceb0(기록).

## GitHub 설정 (레포 kakyungkim/econ-radar)
- Variables: `EMAIL_SEND=now`(자동 발송), `TELEGRAM_ALERT_CHAT_ID=7387431811`(사용자 개인 계정 ID, 봇 ID 아님). `EMAIL_TAG`는 **삭제된 상태가 정상**.
- Secrets: `BUTTONDOWN_API_KEY`, `TELEGRAM_BOT_TOKEN`(발송 봇=kkkim_agent_bot, 사용자 /start 완료), `BLOG_DEPLOY_TOKEN`.

## Key decisions
- 태그 분리(무료) 설계 폐기. **paper-radar 이메일은 별도 Buttondown 무료 계정**(계정당 100명)으로 분리하기로 방향 결정(미착수).
- 자동 수리 수준은 "무료 런북 진단"까지(사용자 선택). Claude가 진단 코멘트·수정 PR까지 하는 상위 단계는 API 키 과금 필요로 보류.
- 알림 검증은 프로덕션 설정을 건드리지 않는 가짜 날짜 실패 주입으로(EMAIL_TAG 재설정 방식은 재오염 위험으로 기각).

## Constraints / do-not-change
- **`EMAIL_TAG`를 다시 켜지 말 것**(Buttondown 유료 전용). send_email.py docstring에도 명시.
- 데일리·주간은 자동 발행 승인 상태(EMAIL_SEND=now). 그 외 외부 발송은 사람 승인 뒤.
- 발송 경로를 바꾸면 draft 1회 관통 검증 후 종료(CLAUDE.md 안전선).

## Known risks / unverified
- 오늘 밤(7/5) 데일리 18:30 KST 생성 → 발송이 첫 실전 통과 지점. 실패 시 DM+Issue가 올 것. `Unverified`
- 월 08:00 KST weekly-publish도 이번 세션에서 수정됨(YAML 파싱 검증만 함, 실행 검증은 안 함). `Unverified`
- 블로그 랜딩 폼의 hidden `tag=econ-radar`는 무료 플랜에서 무의미(무해) — 정리 미착수.
- 이 세션과 무관한 로컬 미커밋 변경 존재: `slides/econ-radar-harness.*`, `vault/blog-drafts/2026-07-01-linkedin-econ-radar.md`, 미추적 `vault/{email,push}/2026-W26-동향.*` — 이전 작업 잔여물, 건드리지 않음.

## Next steps
1. 오늘 밤 데일리와 월요일 주간 발행이 정상 통과하는지 확인(실패 시 DM·Issue 자동).
2. paper-radar 별도 Buttondown 계정 생성 → paper-radar 레포에 API 키 등록(사용자 작업 + 세션 지원).
3. 블로그 "시행착오 모음" 글 — 재료는 `vault/_meta/improvement-log.md` 2026-07-05 항목 4개. content-studio 파이프라인 사용.
4. 새 실패 유형을 겪으면 `scripts/notify_failure.py`의 RUNBOOK에 항목 추가.

## 다음 세션 첫 확인
`gh run list -R kakyungkim/econ-radar --limit 5` 로 최근 발행 워크플로 성공 여부부터 확인.
