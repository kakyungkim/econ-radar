#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
send_email.py — econ-radar 일일 이메일을 Buttondown으로 발송(또는 초안 생성)한다.

입력 : vault/email/YYYY-MM-DD.html   (render_html.py 가 만든 인라인 스타일 이메일)
동작 : Buttondown API(POST /v1/emails)로 이메일을 만든다. 세 모드.
       - 기본(EMAIL_SEND 미설정): 초안(draft) 생성 → 대시보드에서 미리보고 직접 Send.
       - EMAIL_SEND=1: 다음 오전(기본 7시 KST)으로 예약 발송(status=scheduled).
         저녁에 생성해도 독자는 장 개장 전 아침에 받아본다.
       - EMAIL_SEND=now: 즉시 발송(status=about_to_send).

사용 : python3 scripts/send_email.py [DATE]
       DATE 생략 시 오늘 날짜(KST) 자동 사용.

환경변수:
  BUTTONDOWN_API_KEY   (필수) Buttondown API 키. 절대 코드/깃에 넣지 말 것.
  EMAIL_SEND           미설정→초안 / "1"·"true"·"yes"→다음 아침 예약 / "now"→즉시.
  EMAIL_SEND_HOUR      예약 발송 시각(KST, 0~23). 기본 7(오전 7시).

Buttondown 예약: status="scheduled" + publish_date(미래 UTC, YYYY-MM-DDTHH:MM:SSZ).
외부 의존성 없음(Python 3 표준 라이브러리만).
"""
import sys
import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

API_KEY = os.environ.get("BUTTONDOWN_API_KEY", "").strip()
_send = os.environ.get("EMAIL_SEND", "").strip().lower()
if _send in ("now", "immediate", "send"):
    MODE = "now"
elif _send in ("1", "true", "yes", "schedule", "scheduled"):
    MODE = "schedule"
else:
    MODE = "draft"
SEND_HOUR = int(os.environ.get("EMAIL_SEND_HOUR", "7"))
API_URL = "https://api.buttondown.email/v1/emails"

if not API_KEY:
    print("[ERROR] BUTTONDOWN_API_KEY 환경변수가 설정되지 않았습니다.")
    sys.exit(1)

KST = timezone(timedelta(hours=9))
date = sys.argv[1] if len(sys.argv) > 1 else datetime.now(KST).strftime("%Y-%m-%d")


def next_morning_utc(hour):
    """지금(KST) 이후 가장 가까운 hour시 정각(KST)을 UTC ISO(Z)로 반환."""
    now = datetime.now(KST)
    target = now.replace(hour=hour, minute=0, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return target.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), target

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
email_file = os.path.join(ROOT, "vault", "email", "%s.html" % date)

try:
    with open(email_file, encoding="utf-8") as f:
        html = f.read()
except FileNotFoundError:
    print("[ERROR] 파일 없음: %s  (먼저 데일리를 렌더하세요)" % email_file)
    sys.exit(1)

# 제목: render_html.py 가 본문에 박아둔 <!-- SUBJECT: ... --> 에서 추출.
m = re.search(r"<!--\s*SUBJECT:\s*(.+?)\s*-->", html)
subject = m.group(1).strip() if m else ("econ-radar %s" % date)

payload = {"subject": subject, "body": html}
sched_kst = None
if MODE == "now":
    payload["status"] = "about_to_send"
elif MODE == "schedule":
    publish_date, target = next_morning_utc(SEND_HOUR)
    payload["status"] = "scheduled"
    payload["publish_date"] = publish_date
    sched_kst = target.strftime("%Y-%m-%d %H:%M KST")
else:
    payload["status"] = "draft"
data = json.dumps(payload).encode("utf-8")

req = urllib.request.Request(API_URL, data=data, method="POST")
req.add_header("Authorization", "Token %s" % API_KEY)
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=30) as r:
        res = json.loads(r.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8", "replace")
    print("✗ 실패: HTTP %s\n%s" % (e.code, body))
    sys.exit(1)
except urllib.error.URLError as e:
    print("✗ 실패: 네트워크 오류 — %s" % e.reason)
    sys.exit(1)

label = {"now": "즉시 발송", "schedule": "예약 발송", "draft": "초안 생성"}[MODE]
print("✓ %s 완료 | id=%s | status=%s | %s"
      % (label, res.get("id", "?"), res.get("status", "?"), date))
print("  subject: %s" % subject)
if MODE == "schedule":
    print("  → 예약 시각: %s (publish_date=%s)" % (sched_kst, payload["publish_date"]))
elif MODE == "draft":
    print("  → Buttondown 대시보드(Emails → Drafts)에서 미리보기 후 Send 하세요.")
    print("    다음 아침 자동 예약 발송으로 바꾸려면 EMAIL_SEND=1, 즉시 발송은 EMAIL_SEND=now.")
