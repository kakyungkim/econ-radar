#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notify_failure.py — 발행 워크플로 실패 시 런북 진단을 붙여 알린다.

용도 : "실패했다"만이 아니라 "왜, 그래서 뭘 하면 되는지"까지 전달한다.
       2026-07-02~04 이메일 결송(EMAIL_TAG 422)을 사흘간 못 본 교훈으로 도입.

동작 : 실패한 스텝의 로그 파일(인자)에서 마지막 부분을 읽어 런북(RUNBOOK)의
       알려진 패턴과 대조해 원인·조치를 진단하고,
       (1) GitHub Issue를 만들고 (2) 텔레그램 개인 DM을 보낸다.
       DM은 레포 Variable TELEGRAM_ALERT_CHAT_ID 가 있을 때만(없으면 Issue만).
       알림 자체는 절대 실패하지 않는다(원래 실패를 가리지 않게 항상 exit 0).

사용 : python3 scripts/notify_failure.py [로그파일...]
       (워크플로의 `if: failure()` 스텝에서 호출. 로그 파일이 없어도 동작.)

환경변수:
  GITHUB_TOKEN, GITHUB_REPOSITORY   Issue 생성용(Actions 기본 제공, issues: write 필요)
  WORKFLOW_NAME, RUN_URL, FAIL_TARGET   알림 본문 구성(워크플로명, 실행 링크, 날짜/주차)
  TELEGRAM_BOT_TOKEN, TELEGRAM_ALERT_CHAT_ID   (선택) 개인 DM
"""
import os
import re
import sys
import json
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "")
GH_TOKEN = os.environ.get("GITHUB_TOKEN", "")
WORKFLOW = os.environ.get("WORKFLOW_NAME", "발행 워크플로")
RUN_URL = os.environ.get("RUN_URL", "")
TARGET = os.environ.get("FAIL_TARGET", "")
TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT = os.environ.get("TELEGRAM_ALERT_CHAT_ID", "").strip()

# 런북: (로그 패턴, 원인 한 줄, 조치 안내). 위에서부터 첫 일치를 쓴다.
# 새 유형의 실패를 겪으면 여기에 항목을 추가한다(improvement-log에도 기록).
RUNBOOK = [
    (r"Tag filters must be valid tag identifiers",
     "EMAIL_TAG(태그 필터)가 설정돼 있으나 Buttondown 무료 플랜은 태그 기능을 지원하지 않음 (2026-07-02~04 결송과 동일 원인)",
     "레포 Variable EMAIL_TAG 를 삭제: `gh variable delete EMAIL_TAG -R %s` 후 Actions에서 Re-run. 상세: vault/_meta/improvement-log.md 2026-07-05." % REPO),
    (r"HTTP 401|Unauthorized",
     "API 키가 무효하거나 만료됨",
     "Buttondown(또는 해당 서비스) 대시보드에서 키 재발급 후 `gh secret set BUTTONDOWN_API_KEY -R %s` 로 갱신하고 Re-run." % REPO),
    (r"HTTP 429|rate.?limit",
     "요청 한도(rate limit) 초과",
     "몇 분 뒤 Actions에서 Re-run."),
    (r"HTTP 5\d\d",
     "외부 서비스(Buttondown/Telegram) 서버 오류",
     "일시 장애 가능성이 크니 잠시 뒤 Re-run. 반복되면 서비스 상태 페이지 확인."),
    (r"error_code[\":\s]*40[03]",
     "텔레그램 봇 권한 문제(토큰 무효 또는 채널 관리자 권한 없음)",
     "봇 토큰과 채널 관리자 권한을 확인. 토큰 재발급 시 `gh secret set TELEGRAM_BOT_TOKEN -R %s`." % REPO),
    (r"파일 없음|html 없음|md 없음|렌더 생략|FileNotFoundError",
     "렌더 입력 파일(데일리/주간 md 또는 렌더 산출물)이 없음",
     "데일리·주간 생성이 먼저 돌았는지 확인(vault/daily 또는 vault/reports). 생성 후 Re-run."),
    (r"publish_date",
     "이메일 예약 시각(publish_date) 값 문제",
     "send_email.py의 EMAIL_SEND_HOUR/예약 로직 확인. 급하면 EMAIL_SEND=now 로 수동 발송."),
    (r"네트워크 오류|URLError|timed out|Connection refused|Connection reset",
     "일시적 네트워크 오류",
     "Actions에서 Re-run. 반복되면 대상 서비스 상태 확인."),
]


def read_log_tail(paths, max_lines=40, max_chars=2500):
    lines = []
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                lines.extend(f.read().splitlines())
        except OSError:
            continue
    tail = "\n".join(lines[-max_lines:])
    return tail[-max_chars:]


def diagnose(log):
    for pat, cause, action in RUNBOOK:
        if re.search(pat, log, re.IGNORECASE):
            return cause, action
    return ("미등록 유형의 실패(런북에 없음)",
            "아래 로그와 실행 링크에서 원인 확인 후, scripts/notify_failure.py 의 RUNBOOK 에 항목을 추가해 다음부터 자동 진단되게 할 것.")


def post_json(url, body, headers):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    for k, v in headers.items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    log = read_log_tail(sys.argv[1:])
    cause, action = diagnose(log)
    label = ("%s %s" % (WORKFLOW, TARGET)).strip()

    # 1) GitHub Issue
    if GH_TOKEN and REPO:
        body = (
            "자동 생성된 발송 실패 리포트입니다.\n\n"
            "## 진단\n- **원인(추정)**: %s\n- **조치**: %s\n\n"
            "## 실행\n- 워크플로: %s\n- 대상: %s\n- 로그: %s\n\n"
            "## 실패 스텝 로그(끝부분)\n```\n%s\n```\n"
            % (cause, action, WORKFLOW, TARGET or "(미상)", RUN_URL, log or "(캡처된 로그 없음 — 위 실행 링크에서 확인)")
        )
        try:
            res = post_json(
                "https://api.github.com/repos/%s/issues" % REPO,
                {"title": "[발송 실패] %s — %s" % (label, cause[:60]), "body": body},
                {"Authorization": "Bearer %s" % GH_TOKEN, "Accept": "application/vnd.github+json"},
            )
            print("✓ GitHub Issue 생성: %s" % res.get("html_url", "?"))
        except Exception as e:  # noqa: BLE001 — 알림 실패가 원래 실패를 가리면 안 됨
            print("✗ Issue 생성 실패(무시하고 계속): %s" % e)

    # 2) 텔레그램 개인 DM (TELEGRAM_ALERT_CHAT_ID 변수 설정 시에만)
    if TG_TOKEN and TG_CHAT:
        text = (
            "🚨 발송 실패: %s\n\n원인(추정): %s\n\n조치: %s\n\n실행 로그: %s"
            % (label, cause, action, RUN_URL)
        )
        try:
            post_json(
                "https://api.telegram.org/bot%s/sendMessage" % TG_TOKEN,
                {"chat_id": TG_CHAT, "text": text, "disable_web_page_preview": True},
                {},
            )
            print("✓ 텔레그램 DM 발송 (chat_id=%s)" % TG_CHAT)
        except Exception as e:  # noqa: BLE001
            print("✗ 텔레그램 DM 실패(무시하고 계속): %s" % e)
    elif not TG_CHAT:
        print("ℹ TELEGRAM_ALERT_CHAT_ID 변수 미설정 — DM 생략(Issue만). "
              "설정: 봇에게 /start 후 `gh variable set TELEGRAM_ALERT_CHAT_ID --body <내 chat id>`")


if __name__ == "__main__":
    main()
    sys.exit(0)  # 알림 스텝은 절대 추가 실패를 만들지 않는다
