#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""report_readership.py — 구독자가 얼마나 읽는지 주 1회 모아 개인 DM으로 보낸다.

- 메일: Buttondown API(GET /v1/emails, /v1/emails/{id}/analytics). 키는 GitHub Secret BUTTONDOWN_API_KEY.
- 텔레그램 채널: 공개 미리보기 페이지(t.me/s/econradar)의 구독자 수와 글별 조회수.
- 블로그 방문은 GoatCounter 대시보드(https://kakyungkim.goatcounter.com)에서 본다.

사용: python3 scripts/report_readership.py [--days 7] [--fields]   (--fields: 응답 필드 이름만 출력, 값과 키는 찍지 않음)
stdlib만 사용.
"""
import os, sys, re, json, argparse, datetime as dt, urllib.request

API = "https://api.buttondown.email/v1"


def _get(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8")


def bd(path):
    key = os.environ.get("BUTTONDOWN_API_KEY")
    if not key:
        raise SystemExit("BUTTONDOWN_API_KEY 없음")
    return json.loads(_get(API + path, {"Authorization": "Token " + key}))


def telegram(channel="econradar"):
    s = _get("https://t.me/s/" + channel, {"User-Agent": "Mozilla/5.0"})
    m = re.search(r'counter_value">([^<]+)</span>\s*<span class="counter_type">subscribers', s)
    posts = re.findall(r'tgme_widget_message_views">([^<]+)</span>.*?datetime="([^"]+)"', s, re.S)
    return (m.group(1) if m else "?"), [(d[:10], v) for v, d in posts]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--fields", action="store_true")
    a = ap.parse_args()
    since = (dt.datetime.utcnow() - dt.timedelta(days=a.days)).date().isoformat()

    emails = bd("/emails?ordering=-publish_date")
    items = emails.get("results", emails if isinstance(emails, list) else [])
    if a.fields:
        print("emails keys:", sorted(emails.keys()) if isinstance(emails, dict) else type(emails).__name__)
        if items:
            print("email item keys:", sorted(items[0].keys()))
            an = bd("/emails/%s/analytics" % items[0]["id"])
            print("analytics keys:", sorted(an.keys()) if isinstance(an, dict) else type(an).__name__)
        return

    lines = ["📊 econ-radar 읽힘 (최근 %d일)" % a.days]
    rows = []
    for e in items:
        pd = (e.get("publish_date") or "")[:10]
        if not pd or pd < since or e.get("status") not in (None, "sent"):
            continue
        try:
            an = bd("/emails/%s/analytics" % e["id"])
        except Exception as ex:
            an = {"error": type(ex).__name__}
        rows.append((pd, e.get("subject", "")[:40], an))
    for pd, subj, an in sorted(rows):
        nums = {k: v for k, v in an.items() if isinstance(v, (int, float))}
        show = ", ".join("%s %s" % (k, nums[k]) for k in ("recipients", "deliveries", "opens", "clicks") if k in nums) \
            or ", ".join("%s %s" % kv for kv in list(nums.items())[:4])
        lines.append("메일 %s %s | %s" % (pd, subj, show or an.get("error", "-")))
    if not rows:
        lines.append("메일: 기간 안에 보낸 메일 없음")
    try:
        subs, posts = telegram()
        recent = [p for p in posts if p[0] >= since]
        lines.append("텔레그램 구독자 %s명, 최근 글 조회: %s" % (subs, " ".join(v for _, v in recent[-10:]) or "-"))
    except Exception as ex:
        lines.append("텔레그램 집계 실패(%s)" % type(ex).__name__)
    lines.append("블로그 방문: https://kakyungkim.goatcounter.com")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
