#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
send_email.py — econ-radar 일일 이메일을 Buttondown으로 발송(또는 초안 생성)한다.

입력 : vault/email/YYYY-MM-DD.html   (render_html.py 가 만든 인라인 스타일 이메일)
동작 : Buttondown API(POST /v1/emails)로 이메일을 만든다.
       - 기본은 초안(draft) 생성 → 대시보드에서 미리보기 후 직접 Send.
       - EMAIL_SEND=1 이면 즉시 발송(status=about_to_send) → 구독자 전원에게.

사용 : python3 scripts/send_email.py [DATE]
       DATE 생략 시 오늘 날짜(KST) 자동 사용.

환경변수:
  BUTTONDOWN_API_KEY   (필수) Buttondown API 키. 절대 코드/깃에 넣지 말 것.
  EMAIL_SEND           "1"/"true"/"yes" 이면 즉시 발송. 미설정/그 외면 초안만.

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
SEND = os.environ.get("EMAIL_SEND", "").strip().lower() in ("1", "true", "yes")
API_URL = "https://api.buttondown.email/v1/emails"

if not API_KEY:
    print("[ERROR] BUTTONDOWN_API_KEY 환경변수가 설정되지 않았습니다.")
    sys.exit(1)

KST = timezone(timedelta(hours=9))
date = sys.argv[1] if len(sys.argv) > 1 else datetime.now(KST).strftime("%Y-%m-%d")

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

payload = {
    "subject": subject,
    "body": html,
    "status": "about_to_send" if SEND else "draft",
}
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

mode = "발송" if SEND else "초안 생성"
print("✓ %s 완료 | id=%s | status=%s | %s"
      % (mode, res.get("id", "?"), res.get("status", "?"), date))
print("  subject: %s" % subject)
if not SEND:
    print("  → Buttondown 대시보드(Emails → Drafts)에서 미리보기 후 Send 하세요.")
    print("    자동 발송으로 바꾸려면 EMAIL_SEND=1 환경변수를 설정하세요.")
