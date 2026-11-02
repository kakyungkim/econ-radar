#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_market_numbers.py — 데일리 md의 시장 수치를 기계적으로 점검한다.

1) 낡은 링크: 코스피, 금리, 환율 같은 시장 수치가 나오는 항목(### 블록)에 3주 넘게 지난 날짜의 기사 링크가 붙었는가.
   2026-10-03, 10-04 호가 7월 기사의 "코스피 8,000", "원/달러 1,530원대"를 그대로 실었다.
2) 시세 대조(--online): 본문의 코스피, 미 국채 10년물, 원/달러 값이 직전 30일 실제 종가 범위를 벗어나는가.
   시세는 FRED(DGS10, DEXKOUS)와 Yahoo(^KS11)에서 받는다. 받지 못하면 그 항목은 건너뛰고 그 사실을 적는다.

사용: python3 scripts/check_market_numbers.py 2026-10-04 [--online] [--json]
종료 코드: 0 = 문제 없음, 1 = 확인할 항목 있음. 발행을 막지 않는다. 사실 검증 단계와 감시 알림이 이 결과를 읽는다.
stdlib만 사용.
"""
import sys, os, re, json, csv, io, argparse, datetime as dt, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STALE_DAYS = 21
WINDOW_DAYS = 30
# 낡은 링크는 제목이 시장 수준을 다루는 항목에서만 본다. 본문에 배경 기사로 붙은 옛 링크는 정상이다.
MARKET_KW = re.compile(r"코스피|KOSPI|코스닥|국채|10년물|환율|원/달러|원달러|S&P|나스닥|다우")
SKIP_HEAD = re.compile(r"^#{2,3}\s*(Sources|출처|참고|원문)", re.I)

# 값 추출 패턴: (계열, 정규식). 값은 group("v")
PATTERNS = [
    ("kospi", re.compile(r"(?:코스피|KOSPI)[^0-9\n%]{0,15}?(?P<v>\d{1,2},\d{3}(?:\.\d+)?)")),
    ("us10y", re.compile(r"10년물[^0-9\n]{0,25}?(?P<v>\d\.\d{2,3})\s*%")),
    ("usdkrw", re.compile(r"(?:원/달러|원달러|환율)[^0-9\n]{0,20}?(?P<v>1,\d{3}(?:\.\d+)?)\s*(?:~|원)")),
]
# 실제 시세와 비교하면 안 되는 문맥: 목표가와 전망, 미국 외 국채. 2026-09~10월 호에서 잘못 걸렸던 것들
SKIP_CTX = re.compile(r"목표|전망|타깃|target|예상|컨센서스|시나리오|영국|길트|gilt|독일|분트|일본|JGB|중국|유로", re.I)
# 실제 범위 밖으로 허용하는 여유: 장중 값과 표기 반올림을 감안
TOL = {"kospi": ("pct", 0.05), "us10y": ("abs", 0.10), "usdkrw": ("pct", 0.02)}
LABEL = {"kospi": "코스피", "us10y": "미 국채 10년물(%)", "usdkrw": "원/달러"}

URL_DATE = [
    re.compile(r"/(?P<y>20\d{2})/(?P<m>\d{1,2})/(?P<d>\d{1,2})(?:/|$|[^0-9])"),
    re.compile(r"(?<![0-9])(?P<y>20\d{2})(?P<m>[01]\d)(?P<d>[0-3]\d)(?![0-9])"),
    re.compile(r"(?<![0-9])(?P<y>20\d{2})-(?P<m>[01]\d)-(?P<d>[0-3]\d)(?![0-9])"),
]


def _date(s):
    return dt.date.fromisoformat(s)


def _url_date(url):
    for p in URL_DATE:
        m = p.search(url)
        if m:
            try:
                return dt.date(int(m["y"]), int(m["m"]), int(m["d"]))
            except ValueError:
                continue
    return None


def _blocks(text):
    """### 제목부터 다음 ### 또는 ## 전까지를 한 블록으로."""
    parts, cur = [], []
    for ln in text.split("\n"):
        if re.match(r"^#{2,3}\s", ln) and cur:
            parts.append("\n".join(cur)); cur = []
        cur.append(ln)
    if cur:
        parts.append("\n".join(cur))
    return parts


def stale_links(text, date):
    """시장 수치가 나오는 블록에 붙은, date보다 STALE_DAYS일 넘게 지난 기사 링크."""
    d0 = _date(date)
    out = []
    for b in _blocks(text):
        head = b.split("\n", 1)[0]
        if SKIP_HEAD.match(head) or not MARKET_KW.search(head):
            continue
        head = head[:80]
        for url in re.findall(r"\]\((https?://[^)\s]+)\)", b):
            ud = _url_date(url)
            if ud and (d0 - ud).days > STALE_DAYS:
                out.append({"block": head, "url": url, "url_date": ud.isoformat(), "age_days": (d0 - ud).days})
    return out


def _other_month(ctx, date):
    """값 앞 문맥에 다른 달을 가리키는 날짜(6/22, 6월)가 있으면 과거 인용으로 본다."""
    d0 = _date(date)
    ok = {d0.month, (d0.replace(day=1) - dt.timedelta(days=1)).month}
    for m in re.finditer(r"(?<![0-9.,])(\d{1,2})\s*(?:/\d{1,2}|월)", ctx):
        mo = int(m.group(1))
        if 1 <= mo <= 12 and mo not in ok:
            return True
    return False


def _drop_source_lists(text):
    """출처 목록(Sources 절, '1차 자료' 줄)은 기사 제목을 옮긴 것이라 값 대조에서 뺀다."""
    out, skip = [], False
    for ln in text.split("\n"):
        if re.match(r"^#{1,3}\s", ln):
            skip = bool(SKIP_HEAD.match(ln))
        if skip or "1차 자료" in ln:
            continue
        out.append(ln)
    return "\n".join(out)


def check_values(text, refs, date):
    text = _drop_source_lists(text)
    d0 = _date(date)
    lo_day = (d0 - dt.timedelta(days=WINDOW_DAYS)).isoformat()
    out = []
    for series, pat in PATTERNS:
        vals = [v for k, v in (refs.get(series) or {}).items() if lo_day <= k <= date]
        if not vals:
            continue
        lo, hi = min(vals), max(vals)
        kind, t = TOL[series]
        lo_ok, hi_ok = (lo - t, hi + t) if kind == "abs" else (lo * (1 - t), hi * (1 + t))
        for m in pat.finditer(text):
            v = float(m.group("v").replace(",", ""))
            line_start = text.rfind("\n", 0, m.start()) + 1
            ctx = text[max(line_start, m.start() - 40):m.end()]
            if _other_month(ctx, date):
                continue
            tail = text[m.end():m.end() + 12]
            if SKIP_CTX.search(ctx + tail) or re.match(r"\s*(조|억)", tail):
                continue
            if not (lo_ok <= v <= hi_ok):
                out.append({"series": series, "value": v, "range": [round(lo, 2), round(hi, 2)],
                            "context": text[max(line_start, m.start() - 30):m.end() + 20].strip()})
    return out


# ---------- 시세 받기 ----------
def _get(url, timeout=30, tries=3, ua=None):
    # urllib은 FRED에서 시간 초과가 났다(맥과 GitHub 러너 모두). curl은 0.3초에 받는다.
    # FRED는 브라우저 흉내 User-Agent를 막고 curl 기본값만 받는다. Yahoo에만 ua를 준다.
    import subprocess
    last = None
    for _ in range(tries):
        cmd = ["curl", "-sfL", "-m", str(timeout)] + (["-A", ua] if ua else []) + [url]
        r = subprocess.run(cmd,
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout
        last = RuntimeError("curl exit %d" % r.returncode)
    raise last

def fetch_refs(date):
    d0 = _date(date)
    start = (d0 - dt.timedelta(days=WINDOW_DAYS + 5)).isoformat()
    refs, notes = {}, []
    for series, fred in (("us10y", "DGS10"), ("usdkrw", "DEXKOUS")):
        try:
            rows = csv.DictReader(io.StringIO(_get(
                "https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s&cosd=%s&coed=%s" % (fred, start, date))))
            refs[series] = {r["observation_date"]: float(r[fred]) for r in rows if r.get(fred) not in ("", ".", None)}
        except Exception as e:  # 네트워크 차단 등
            notes.append("%s 시세를 받지 못함(%s)" % (fred, type(e).__name__))
    try:
        p1 = int(dt.datetime.combine(_date(start), dt.time()).timestamp())
        p2 = int(dt.datetime.combine(d0 + dt.timedelta(days=1), dt.time()).timestamp())
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EKS11?period1={}&period2={}&interval=1d"
        j = json.loads(_get(url.format(p1, p2), ua="Mozilla/5.0"))["chart"]["result"][0]
        kst = dt.timezone(dt.timedelta(hours=9))
        refs["kospi"] = {dt.datetime.fromtimestamp(t, kst).date().isoformat(): c
                         for t, c in zip(j["timestamp"], j["indicators"]["quote"][0]["close"]) if c}
    except Exception as e:
        notes.append("코스피 시세를 받지 못함(%s)" % type(e).__name__)
    return refs, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--online", action="store_true", help="실제 시세와 대조(FRED, Yahoo)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    path = os.path.join(ROOT, "vault", "daily", a.date + ".md")
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)  # 사실 검증 기록 주석은 본문이 아니다
    res = {"date": a.date, "stale_links": stale_links(text, a.date), "values": [], "notes": []}
    if a.online:
        refs, res["notes"] = fetch_refs(a.date)
        res["values"] = check_values(text, refs, a.date)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        print("[시장 수치 점검] %s" % a.date)
        for f in res["stale_links"]:
            print("  낡은 링크 %d일 전(%s): %s\n    %s" % (f["age_days"], f["url_date"], f["block"], f["url"]))
        for f in res["values"]:
            print("  시세와 다름: %s %s (직전 30일 %s~%s) | %s" % (
                LABEL[f["series"]], f["value"], f["range"][0], f["range"][1], f["context"]))
        for n in res["notes"]:
            print("  참고: " + n)
        if not res["stale_links"] and not res["values"]:
            print("  확인할 항목 없음")
    sys.exit(1 if (res["stale_links"] or res["values"]) else 0)


if __name__ == "__main__":
    main()
