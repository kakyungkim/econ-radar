#!/usr/bin/env python3
"""
텔레그램 채널 @econradar에 push 메시지를 발송한다.
사용: python3 scripts/send_push.py [DATE]
DATE 생략 시 오늘 날짜(KST) 자동 사용.
"""
import sys, json, os, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID   = os.environ.get("TELEGRAM_CHAT_ID", "-1004408420486")
API_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

if not BOT_TOKEN:
    print("[ERROR] TELEGRAM_BOT_TOKEN 환경변수가 설정되지 않았습니다.")
    sys.exit(1)

KST = timezone(timedelta(hours=9))
date = sys.argv[1] if len(sys.argv) > 1 else datetime.now(KST).strftime("%Y-%m-%d")
push_file = f"vault/push/{date}.md"

try:
    text = open(push_file, encoding="utf-8").read()
except FileNotFoundError:
    print(f"[ERROR] 파일 없음: {push_file}")
    sys.exit(1)

data = urllib.parse.urlencode({
    "chat_id": CHAT_ID,
    "text": text,
    "disable_web_page_preview": "false",
}).encode("utf-8")

req = urllib.request.Request(API_URL, data)
with urllib.request.urlopen(req, timeout=30) as r:
    res = json.loads(r.read().decode("utf-8"))

if res.get("ok"):
    print(f"✓ 전송 완료 | msg_id: {res['result']['message_id']} | {date}")
else:
    print(f"✗ 전송 실패: {res.get('description', res)}")
    sys.exit(1)
