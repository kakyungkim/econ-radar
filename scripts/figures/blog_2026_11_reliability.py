#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""블로그 글(2026-11-02, econ-radar 5개월 점검) 결과 그림.

a: 2026년 10월 발행 상태. 날짜마다 데일리 생성 여부와 블로그 공개 여부, 감시 DM이 '누락'을 알린 날.
   블로그 상태는 블로그 저장소 커밋 기록, 감시 DM은 GitHub Actions 실행 로그(2026-11-02 확인).
b: 고치기 전 수치와 실제 값. 실제 값은 FRED(DGS10, DEXKOUS)와 Yahoo(^KS11)의 10월 2일 종가.

사용: python3 scripts/figures/blog_2026_11_reliability.py OUTDIR   → OUTDIR/reliability_kr.png, reliability_en.png
"""
import os, sys, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Patch

for f in ("Pretendard-Regular.ttf", "Pretendard-SemiBold.ttf", "Pretendard-Bold.ttf"):
    p = os.path.expanduser("~/Library/Fonts/" + f)
    if os.path.exists(p):
        fm.fontManager.addfont(p)
plt.rcParams["font.family"] = "Pretendard"
plt.rcParams["axes.unicode_minus"] = False

C_OK, C_BLOG, C_NONE, C_ALERT = "#8fb9a8", "#e8a87c", "#c96a6a", "#5b7c99"
C_WRONG, C_TRUE = "#c96a6a", "#7a8b99"

DAYS = [dt.date(2026, 10, 1) + dt.timedelta(days=i) for i in range(32)]  # 10/1 ~ 11/1
NOT_GENERATED = {"2026-10-01"}                       # 사용량 한도로 생성 안 됨(10/26 소급 발행)
BLOG_MISSING = {"2026-10-02", "2026-10-14", "2026-10-15", "2026-10-28", "2026-10-29"}
# 감시가 '누락' DM을 보낸 날짜(오알림). 10/6부터 매일, 실제로는 다음 날을 확인했다
FALSE_ALERT = {d.isoformat() for d in DAYS if d >= dt.date(2026, 10, 6)}

# (라벨, 실렸던 값, 실제 값, 단위)
NUMS = {
    "kr": [("코스피", 8000, 7003.74, ""), ("원/달러", 1530, 1345.75, "원"), ("미 국채 10년물", 4.49, 5.28, "%")],
    "en": [("KOSPI", 8000, 7003.74, ""), ("KRW per USD", 1530, 1345.75, ""), ("US 10-year yield", 4.49, 5.28, "%")],
}
TXT = {
    "kr": dict(a="a  2026년 10월 발행 상태", b="b  실렸던 수치와 10월 2일 실제 종가",
               ok="정상 발행", blog="데일리는 나갔고 블로그만 빠짐", none="데일리 생성 안 됨",
               alert="감시 DM이 '누락'을 알린 날(오알림)", row1="발행", row2="감시 DM",
               shown="실렸던 값", actual="실제 종가"),
    "en": dict(a="a  Publishing status, October 2026", b="b  Published figures vs. actual Oct 2 close",
               ok="Published", blog="Newsletter sent, blog page missing", none="Not generated",
               alert="Watchdog 'missing' DM (false alarm)", row1="Publish", row2="Watchdog DM",
               shown="Published", actual="Actual close"),
}


def draw(lang, out):
    t = TXT[lang]
    fig = plt.figure(figsize=(10, 6.2), dpi=160)
    gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.35], hspace=0.62, wspace=0.42,
                          left=0.115, right=0.97, top=0.9, bottom=0.08)
    ax = fig.add_subplot(gs[0, :])
    for i, d in enumerate(DAYS):
        k = d.isoformat()
        c = C_NONE if k in NOT_GENERATED else C_BLOG if k in BLOG_MISSING else C_OK
        ax.add_patch(plt.Rectangle((i, 1.15), 0.86, 0.75, color=c, lw=0))
        if k in FALSE_ALERT:
            ax.add_patch(plt.Rectangle((i, 0.1), 0.86, 0.75, color=C_ALERT, lw=0, alpha=0.85))
    ax.set_xlim(-0.3, len(DAYS) + 0.2); ax.set_ylim(0, 2.05)
    ax.set_yticks([0.47, 1.52]); ax.set_yticklabels([t["row2"], t["row1"]], fontsize=10)
    ticks = [i for i, d in enumerate(DAYS) if d.day in (1, 6, 11, 16, 21, 26) or i == len(DAYS) - 1]
    ax.set_xticks([i + 0.43 for i in ticks])
    ax.set_xticklabels([("%d/%d" % (DAYS[i].month, DAYS[i].day)) for i in ticks], fontsize=9, color="#555")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    ax.set_title(t["a"], loc="left", fontsize=12.5, fontweight="bold", pad=26)
    ax.legend(handles=[Patch(color=C_OK, label=t["ok"]), Patch(color=C_BLOG, label=t["blog"]),
                       Patch(color=C_NONE, label=t["none"]), Patch(color=C_ALERT, label=t["alert"])],
              loc="lower left", bbox_to_anchor=(0, 1.0), ncol=4, frameon=False, fontsize=8.6,
              handlelength=1.1, columnspacing=1.2)

    for j, (lab, shown, actual, unit) in enumerate(NUMS[lang]):
        bx = fig.add_subplot(gs[1, j])
        bars = bx.bar([0, 1], [shown, actual], color=[C_WRONG, C_TRUE], width=0.62)
        top = max(shown, actual)
        for b, v in zip(bars, (shown, actual)):
            s = ("{:,.2f}".format(v) if v < 100 else "{:,.2f}".format(v).rstrip("0").rstrip(".")) + unit
            bx.text(b.get_x() + b.get_width() / 2, v + top * 0.02, s, ha="center", va="bottom", fontsize=10)
        bx.set_ylim(0, top * 1.2)
        bx.set_xticks([0, 1]); bx.set_xticklabels([t["shown"], t["actual"]], fontsize=9.5)
        bx.set_yticks([])
        for s in ("top", "right", "left"):
            bx.spines[s].set_visible(False)
        bx.set_title(lab, fontsize=11, pad=6)
    fig.text(0.115, 0.5, t["b"], fontsize=12.5, fontweight="bold")
    fig.savefig(out, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    for lang in ("kr", "en"):
        draw(lang, os.path.join(outdir, "reliability_%s.png" % lang))
    print("ok", outdir)
