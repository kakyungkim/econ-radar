#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subscriber_stats.py — Buttondown 구독자를 상태(type)별로 집계한다(읽기 전용).

용도 : "발송 대상이 생각보다 적다" 같은 상황에서 어디로 새는지 확인.
       실제 이메일을 받는 상태는 regular(+premium·gifted)뿐이다.
       unactivated(가입 확인 메일 미클릭), unsubscribed(수신거부),
       undeliverable(반송 누적) 등은 발송 대상에서 빠진다.

동작 : GET /v1/subscribers?type=<t> 를 상태별로 호출해 count만 읽는다(수정 없음).
       regular가 아닌 상태는 이메일 주소도 몇 개 보여준다(최대 10개).

사용 : read -s BUTTONDOWN_API_KEY; export BUTTONDOWN_API_KEY   # 키가 히스토리에 안 남게
       python3 scripts/subscriber_stats.py

환경변수:
  BUTTONDOWN_API_KEY   (필수) Buttondown API 키. 절대 코드/깃에 넣지 말 것.

외부 의존성 없음(Python 3 표준 라이브러리만).
"""
import os
import sys
import json
import urllib.request
import urllib.error

API_KEY = os.environ.get("BUTTONDOWN_API_KEY", "").strip()
BASE = "https://api.buttondown.email/v1/subscribers"

if not API_KEY:
    print("[ERROR] BUTTONDOWN_API_KEY 환경변수가 설정되지 않았습니다.")
    print("        read -s BUTTONDOWN_API_KEY; export BUTTONDOWN_API_KEY  후 다시 실행하세요.")
    sys.exit(1)

# Buttondown SubscriberType 전체(OpenAPI 기준). regular만 통상 발송 대상.
TYPES = [
    "regular", "unactivated", "unsubscribed", "undeliverable", "paused",
    "blocked", "complained", "removed", "premium", "gifted", "unpaid",
    "churning", "churned", "past_due", "trialed", "upcoming",
]
RECEIVES = {"regular", "premium", "gifted"}


def get(url):
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Token %s" % API_KEY)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


total = 0
nonzero = []
for t in TYPES:
    try:
        res = get("%s?type=%s" % (BASE, t))
    except urllib.error.HTTPError as e:
        print("✗ 조회 실패(type=%s) HTTP %s: %s" % (t, e.code, e.read().decode("utf-8", "replace")[:200]))
        continue
    n = res.get("count", len(res.get("results", [])))
    total += n
    if n:
        nonzero.append((t, n, res.get("results", [])))

print("구독자 상태별 집계 (총 %d명)" % total)
print("-" * 46)
for t, n, results in nonzero:
    mark = "← 발송 대상" if t in RECEIVES else ""
    print("  %-14s %4d명  %s" % (t, n, mark))
print("-" * 46)
recv = sum(n for t, n, _ in nonzero if t in RECEIVES)
print("이메일을 실제로 받는 구독자: %d명" % recv)

for t, n, results in nonzero:
    if t in RECEIVES:
        continue
    print("\n[%s] %d명 (최대 10명 표시)" % (t, n))
    for s in results[:10]:
        print("  - %s (가입: %s)" % (s.get("email_address", "?"), (s.get("creation_date") or "")[:10]))
    if n > 10:
        print("  ... 외 %d명" % (n - 10))
