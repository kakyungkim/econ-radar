#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tag_subscribers.py — 기존 Buttondown 구독자 전체에 태그 하나를 붙인다(백필).

용도 : 한 Buttondown 계정에서 econ-radar와 paper-radar를 태그로 나눠 굴리기 전에,
       이미 있는 구독자에게 기준 태그(예: econ-radar)를 한 번 입혀 둔다.
       이 백필을 먼저 하지 않고 send_email.py의 EMAIL_TAG 필터를 켜면,
       태그 없는 기존 구독자에게는 아무도 발송되지 않는다.

동작 : GET /v1/subscribers 로 전체를 훑어(페이지네이션), 해당 태그가 없는 구독자만
       PATCH /v1/subscribers/{id} 로 기존 tags에 태그를 추가한다(기존 태그 보존).
       기본은 드라이런(무엇을 바꿀지 건수만 출력). 실제 적용은 --apply.

사용 : BUTTONDOWN_API_KEY=... python3 scripts/tag_subscribers.py econradar          # 드라이런
       BUTTONDOWN_API_KEY=... python3 scripts/tag_subscribers.py econradar --apply  # 적용

환경변수:
  BUTTONDOWN_API_KEY   (필수) Buttondown API 키. 절대 코드/깃에 넣지 말 것.

외부 의존성 없음(Python 3 표준 라이브러리만).
"""
import sys
import os
import json
import time
import urllib.request
import urllib.error

API_KEY = os.environ.get("BUTTONDOWN_API_KEY", "").strip()
BASE = "https://api.buttondown.email/v1/subscribers"

if not API_KEY:
    print("[ERROR] BUTTONDOWN_API_KEY 환경변수가 설정되지 않았습니다.")
    sys.exit(1)

args = [a for a in sys.argv[1:] if a != "--apply"]
APPLY = "--apply" in sys.argv
if not args:
    print("사용법: python3 scripts/tag_subscribers.py <태그> [--apply]")
    sys.exit(1)
TAG = args[0].strip()


def api(method, url, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Token %s" % API_KEY)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode("utf-8")
        return json.loads(raw) if raw else {}


# 1) 전체 구독자 수집(페이지네이션)
subs = []
page = 1
while True:
    try:
        res = api("GET", "%s?page=%d" % (BASE, page))
    except urllib.error.HTTPError as e:
        print("✗ 목록 조회 실패 HTTP %s: %s" % (e.code, e.read().decode("utf-8", "replace")))
        sys.exit(1)
    results = res.get("results", [])
    if not results:
        break
    subs.extend(results)
    if not res.get("next"):
        break
    page += 1

total = len(subs)
need = [s for s in subs if TAG not in (s.get("tags") or [])]
have = total - len(need)
print("구독자 총 %d명 | 이미 '%s' 태그 있음 %d명 | 붙일 대상 %d명" % (total, TAG, have, len(need)))

if not APPLY:
    print("\n[드라이런] 실제로 붙이지 않았습니다. 적용하려면 --apply 를 붙이세요.")
    for s in need[:10]:
        print("  - %s (현재 태그: %s)" % (s.get("email_address", "?"), s.get("tags") or []))
    if len(need) > 10:
        print("  ... 외 %d명" % (len(need) - 10))
    sys.exit(0)

# 2) 적용: 대상만 PATCH(기존 태그 보존 + TAG 추가)
ok = 0
fail = 0
for s in need:
    sid = s.get("id") or s.get("email_address")
    new_tags = list(dict.fromkeys((s.get("tags") or []) + [TAG]))  # 중복 제거, 순서 보존
    try:
        api("PATCH", "%s/%s" % (BASE, sid), {"tags": new_tags})
        ok += 1
    except urllib.error.HTTPError as e:
        fail += 1
        print("  ✗ 실패 %s HTTP %s: %s" % (s.get("email_address", sid), e.code,
                                          e.read().decode("utf-8", "replace")[:200]))
    time.sleep(0.15)  # rate limit 여유

print("\n✓ 완료 | 대상 %d명 중 성공 %d명, 실패 %d명 | 태그='%s'" % (len(need), ok, fail, TAG))
print("  검증: 성공 %d + 이미있음 %d = %d / 총 %d" % (ok, have, ok + have, total))
