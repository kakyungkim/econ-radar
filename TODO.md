# TODO — econ-radar

## High priority
- [ ] 오늘 밤(7/5) 데일리, 월(7/6) 주간 발행 정상 통과 확인 — 실패 시 텔레그램 DM+Issue 자동 알림 옴. 첫 실전 통과 지점.
- [ ] paper-radar 이메일 분리: 별도 Buttondown 무료 계정 생성(사용자) → paper-radar 레포에 `BUTTONDOWN_API_KEY` 등록. (태그 분리 설계는 무료 플랜 미지원으로 폐기, 2026-07-05)

## Medium priority
- [ ] 블로그 "시행착오 모음" 글 발행 — 재료: `vault/_meta/improvement-log.md` 2026-07-05 항목 4개(결송 사후 분석, 안내 배너 재발송, 알림 시스템, 가짜 날짜 검증기·DM 시행착오). content-studio 파이프라인.
- [ ] 블로그 랜딩 폼(econ-radar/index.html)의 hidden `tag=econ-radar` 정리 — 무료 플랜에서 무의미(무해라 급하지 않음).
- [ ] 새 실패 유형 발생 시 `scripts/notify_failure.py` RUNBOOK에 항목 추가하는 습관 정착.

## Low priority — 하네스 개선 백로그 (2026-06-13 검토에서 이관)
- [ ] MOC "현재 상태 요약" 구조 — topics/*.md 상단 핵심 흐름 5줄, 타임라인은 아카이브로.
- [ ] 백로그 주간 트리아지 — 주 1회 1~2개만 처리, 나머지는 의식적 won't-fix.
- [ ] `투자테마` vs `투자전략` MOC 중복 정리.
- [ ] `유망기업` vs `신약개발전략` 바이오 기업 서술 중첩 정리.
- [ ] 커리어 렌즈 → '일의 미래' 테마 3층 저술 핸드오프 규칙 정의.
- [ ] 수요 렌즈(Demand) (C) 승격 판단 — 기준: Demand 단이 결론을 바꾼 사례 주 2회 이상이면 demand-analyst 신설.
- [ ] OKF 마이그레이션 내구성 — 레포 에이전트 지침이 아직 위키링크 기준이라 클라우드가 되돌리는 문제(메모리 okf-migration-durability-gap 참조).

## Blocked / Needs confirmation
- [ ] Claude 자동 진단·수정 PR 단계 — 레포에 ANTHROPIC_API_KEY 필요(과금), 사용자가 원할 때만.

## Done
- [x] 2026-07-05 — 이메일 결송 원인 규명(무료 플랜 태그 미지원)·EMAIL_TAG 삭제·복구, 밀린 7/2~7/4 안내 배너 붙여 재생성 → 사용자 수동 발송 완료.
- [x] 2026-07-05 — 실패 알림 시스템(notify_failure.py, 런북 진단→Issue+텔레그램 DM) 구축, 가짜 날짜 실패 주입으로 DM 도착까지 검증.
- [x] 2026-07-05 — EMAIL_NOTICE(1회성 안내 배너)·subscriber_stats.py(수신자 진단) 추가. "발송 경로 변경 후 즉시 관통 검증" 규율 CLAUDE.md 명시.
- [x] 2026-06-13 — fact-checker(T4.7), vault 전체 추적(레포 private), 렌더 템플릿화, 주간 동향 루틴.
- [x] 2026-06-12 — 데일리 자동 발행 + 텔레그램 채널 알림.
- [x] 2026-06-10 — 블로그 글 + econ-radar 사이트 공개.
