#!/usr/bin/env python3
"""econ-radar 수동 발행: 누락 날짜 탐지 → 원고 생성 → 날짜별 커밋·push → Actions 대기 → 블로그 공개 확인.

AI를 쓰는 것은 원고(데일리, 주간) 생성 단계뿐이다. 나머지는 이 스크립트가 처리한다.
자세한 사용법은 docs/AI-PROVIDER.md "수동 발행" 절.

    python3 scripts/manual_publish.py --dry-run          # 무엇을 할지만 출력
    python3 scripts/manual_publish.py                    # 최근 14일 누락분 전부
    python3 scripts/manual_publish.py --dates 2026-11-18 --blog-only
    python3 scripts/manual_publish.py --weekly auto      # 데일리 뒤 지난 일요일이 속한 주의 동향까지
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request

REPO = Path(__file__).resolve().parents[1]
KST = timezone(timedelta(hours=9))
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WEEK_RE = re.compile(r"^\d{4}-W\d{2}$")
BLOG_URL = "https://kakyungkim.github.io/econ-radar/{date}.html"
WF_BLOG, WF_TG, WF_EMAIL = "Daily Blog Publish", "Telegram Daily Push", "Email Daily Push (Buttondown)"
# 날짜와 무관하게 함께 올라가는 공용 파일
SHARED = re.compile(r"^(vault/daily/index\.md|vault/_meta/recent-headlines\.md|vault/topics/[^/]+\.md)$")


# ---------- 순수 함수 (tests/test_manual_publish.py) ----------

def missing_dates(feed_dates: set[str], daily_dates: set[str], today: date, days: int = 14) -> list[str]:
    """후보 수집은 됐는데 데일리가 없는 날짜. 오늘부터 days일 전까지, 오래된 순."""
    start = today - timedelta(days=days)
    out = [d for d in feed_dates - daily_dates
           if start <= date.fromisoformat(d) <= today]
    return sorted(out)


def parse_porcelain_z(raw: str) -> list[tuple[str, str]]:
    """`git status --porcelain -z -uall` 출력. -z 라 한글 경로가 따옴표로 감싸지지 않는다."""
    items = raw.split("\0")
    out, i = [], 0
    while i < len(items):
        item = items[i]
        i += 1
        if not item:
            continue
        status, path = item[:2], item[3:]
        if status[0] in "RC":  # rename/copy 는 원래 경로가 다음 항목에 온다
            i += 1
        out.append((status, path))
    return out


def date_pattern(date_str: str, blog_only: bool) -> re.Pattern[str]:
    d = re.escape(date_str)
    parts = [
        rf"vault/raw/(news|feed)-{d}\.(md|json)",
        rf"vault/analysis/[a-z]+-{d}\.md",
        rf"vault/daily/{d}\.md",
        rf"vault/html/{d}\.html",
        rf"artifacts/runs/{d}-[a-z-]+\.log",
    ]
    if not blog_only:
        parts += [rf"vault/push/{d}\.md", rf"vault/email/{d}\.html"]
    return re.compile("^(" + "|".join(parts) + ")$")


def select_paths(entries: list[tuple[str, str]], date_str: str,
                 blog_only: bool = False) -> tuple[list[str], list[str]]:
    """커밋할 파일과 남길 파일. 삭제는 절대 고르지 않는다."""
    pat = date_pattern(date_str, blog_only)
    selected, skipped = [], []
    for status, path in entries:
        if "D" not in status and (pat.match(path) or SHARED.match(path)):
            selected.append(path)
        else:
            skipped.append(path)
    return selected, skipped


def expected_workflows(paths: list[str]) -> set[str]:
    names = set()
    if any(p.startswith("vault/html/") for p in paths):
        names.add(WF_BLOG)
    if any(p.startswith("vault/push/") for p in paths):
        names |= {WF_TG, WF_EMAIL}
    return names


def week_of_last_sunday(today: date) -> str:
    sunday = today - timedelta(days=(today.weekday() + 1) % 7)
    y, w, _ = sunday.isocalendar()
    return f"{y}-W{w:02d}"


# ---------- git, gh, 실행 ----------

def sh(*cmd: str, cwd: Path, check: bool = True, capture: bool = True) -> str:
    print("+", " ".join(cmd), flush=True)
    res = subprocess.run(cmd, cwd=cwd, text=True, check=check,
                         stdout=subprocess.PIPE if capture else None)
    return (res.stdout or "") if capture else ""


def tree_dates(wt: Path, folder: str, pattern: str) -> set[str]:
    names = sh("git", "-c", "core.quotepath=false", "ls-tree", "--name-only", "origin/main",
               f"{folder}/", cwd=wt).split()
    return {m.group(1) for n in names if (m := re.search(pattern, n))}


def prepare_worktree(path: Path, dry: bool) -> Path:
    sh("git", "fetch", "-q", "origin", cwd=REPO)
    if not path.exists():
        if dry:
            print(f"[dry-run] 작업 폴더 생성 예정: {path}")
            return REPO
        sh("git", "worktree", "add", "--detach", str(path), "origin/main", cwd=REPO)
    return path


def status_entries(wt: Path) -> list[tuple[str, str]]:
    return parse_porcelain_z(sh("git", "status", "--porcelain", "-z", "-uall", cwd=wt))


def commit_and_push(wt: Path, paths: list[str], message: str, no_push: bool) -> str | None:
    sh("git", "add", "--", *paths, cwd=wt)
    deleted = sh("git", "diff", "--cached", "--diff-filter=D", "--name-only", cwd=wt).split()
    if deleted:
        raise SystemExit(f"삭제가 stage 됨({len(deleted)}개). 중단합니다: {deleted[:5]}")
    sh("git", "commit", "-q", "-m", message, cwd=wt)
    if no_push:
        return None
    left = [p for s, p in status_entries(wt) if s != "??"]
    if left:
        raise SystemExit(f"추적 파일 변경이 남아 rebase 할 수 없습니다: {left}")
    sh("git", "fetch", "-q", "origin", cwd=wt)
    sh("git", "rebase", "-q", "origin/main", cwd=wt)
    sh("git", "push", "origin", "HEAD:main", cwd=wt)
    return sh("git", "rev-parse", "HEAD", cwd=wt).strip()


def wait_actions(wt: Path, sha: str, expected: set[str], timeout_min: int) -> bool:
    deadline = time.time() + timeout_min * 60
    while time.time() < deadline:
        runs = json.loads(sh("gh", "run", "list", "--commit", sha, "--limit", "30",
                             "--json", "name,status,conclusion,url", cwd=wt) or "[]")
        names = {r["name"] for r in runs}
        if expected <= names and all(r["status"] == "completed" for r in runs):
            ok = True
            for r in runs:
                mark = "OK" if r["conclusion"] in ("success", "skipped") else "실패"
                ok &= mark == "OK"
                print(f"  [{mark}] {r['name']}: {r['conclusion']} {r['url']}")
            return ok
        time.sleep(20)
    print(f"  Actions 대기 시간 초과({timeout_min}분). gh run list --commit {sha} 로 확인하세요.")
    return False


def wait_blog(date_str: str, timeout_min: int = 10) -> bool:
    url = BLOG_URL.format(date=date_str)
    deadline = time.time() + timeout_min * 60
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                if r.status == 200:
                    print(f"  블로그 공개 확인: {url}")
                    return True
        except Exception:
            pass
        time.sleep(30)
    print(f"  블로그가 {timeout_min}분 안에 열리지 않습니다: {url}")
    return False


def generate_weekly(wt: Path, week: str, provider: str, model: str | None) -> int:
    sys.path.insert(0, str(wt / "scripts"))
    from run_ai_provider import build_command  # noqa: E402
    monday = date.fromisocalendar(int(week[:4]), int(week[6:]), 1)
    prompt = (wt / "scripts/prompts/weekly-provider.md").read_text(encoding="utf-8")
    prompt = (prompt.replace("{{WEEK}}", week).replace("{{PROVIDER}}", provider)
              .replace("{{START}}", monday.isoformat())
              .replace("{{END}}", (monday + timedelta(days=6)).isoformat()))
    log = wt / "artifacts" / "runs" / f"{week}-{provider}.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    cmd = build_command(provider, model, log)
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, input=prompt, text=True, cwd=wt).returncode


def publish_weekly(wt: Path, week: str, args) -> int:
    report = wt / "vault" / "reports" / f"{week}-동향.md"
    if args.dry_run:
        print(f"[dry-run] 주간 {week}: {'있음, 커밋만' if report.exists() else '생성 후 커밋'}")
        return 0
    if not report.exists() and not args.skip_generate:
        if generate_weekly(wt, week, args.provider, args.model) != 0 or not report.exists():
            print(f"주간 리포트 생성 실패: {report.relative_to(wt)}", file=sys.stderr)
            return 3
    pat = re.compile(rf"^(vault/reports/({re.escape(week)}-동향|index)\.md|artifacts/runs/{re.escape(week)}-[a-z]+\.log)$")
    paths = [p for s, p in status_entries(wt) if "D" not in s and pat.match(p)]
    if not paths:
        print(f"주간 {week}: 커밋할 변경 없음")
        return 0
    sha = commit_and_push(wt, paths, f"econ-radar: {week} 주간 동향 ({args.provider})", args.no_push)
    if not sha:
        return 0
    # 월 08:00 KST 예약 실행이 이미 지나갔으면(리포트가 없어 건너뛰었으므로) 직접 실행한다.
    # 아직 안 돌았으면 예약 실행에 맡긴다. 둘 다 돌면 두 번 발송된다.
    monday = date.fromisocalendar(int(week[:4]), int(week[6:]), 1) + timedelta(days=7)
    cron_utc = datetime(monday.year, monday.month, monday.day, tzinfo=timezone.utc) - timedelta(hours=1)
    runs = json.loads(sh("gh", "run", "list", "--workflow", "weekly-publish.yml", "--event", "schedule",
                         "--limit", "5", "--json", "createdAt", cwd=wt) or "[]")
    fired = any(datetime.fromisoformat(r["createdAt"].replace("Z", "+00:00")) >= cron_utc for r in runs)
    if fired:
        sh("gh", "workflow", "run", "weekly-publish.yml", "-f", f"period={week}",
           "-f", f"send={'draft' if args.blog_only else '1'}", cwd=wt)
        print(f"주간 {week}: 예약 실행이 이미 지나 직접 발행을 걸었습니다.")
    else:
        print(f"주간 {week}: 월 08:00 KST 예약 실행(실제로는 몇 시간 늦음)이 발행합니다.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dates", nargs="*", help="대상 날짜. 비우면 최근 --days 일의 누락분")
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--provider", choices=("codex", "claude"), default=os.environ.get("AI_PROVIDER", "codex"))
    ap.add_argument("--model", default=os.environ.get("AI_MODEL") or None)
    ap.add_argument("--blog-only", action="store_true", help="push, email 파일을 빼서 텔레그램, 메일 발송 없이 블로그만")
    ap.add_argument("--skip-generate", action="store_true", help="이미 만든 원고를 커밋, push만")
    ap.add_argument("--no-push", action="store_true", help="로컬 커밋까지만")
    ap.add_argument("--no-wait", action="store_true", help="Actions와 블로그 확인을 기다리지 않음")
    ap.add_argument("--weekly", nargs="?", const="auto", help="주간 동향도 처리. auto 또는 YYYY-Www")
    ap.add_argument("--worktree", type=Path, default=REPO.parent / "econ-radar-publish")
    ap.add_argument("--timeout-min", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    today = datetime.now(KST).date()
    wt = prepare_worktree(args.worktree.resolve(), args.dry_run)
    if args.dates:
        bad = [d for d in args.dates if not DATE_RE.fullmatch(d)]
        if bad:
            ap.error(f"날짜 형식 오류: {bad}")
        dates = sorted(args.dates)
    else:
        feeds = tree_dates(wt, "vault/raw", r"feed-(\d{4}-\d{2}-\d{2})\.json$")
        dailies = tree_dates(wt, "vault/daily", r"/(\d{4}-\d{2}-\d{2})\.md$")
        dates = missing_dates(feeds, dailies, today, args.days)
    print(f"작업 폴더: {wt}\n대상 날짜({len(dates)}개): {', '.join(dates) or '없음'}")

    done = []
    for d in dates:
        print(f"\n===== {d}")
        if args.dry_run:
            print(f"[dry-run] {args.provider}로 생성 → 날짜 파일과 공용 인덱스만 커밋 → push → Actions 대기")
            continue
        if not args.skip_generate:
            res = subprocess.run([sys.executable, "scripts/run_daily_pipeline.py", d,
                                  "--provider", args.provider], cwd=wt)
            if res.returncode != 0:
                print(f"{d} 생성 실패(종료 코드 {res.returncode}). 여기서 멈춥니다.", file=sys.stderr)
                return res.returncode
        daily = wt / "vault" / "daily" / f"{d}.md"
        if daily.exists() and not (wt / "vault" / "html" / f"{d}.html").exists():
            # 앞선 실행이 원고만 남기고 멈춘 경우: 렌더부터 다시
            sh(sys.executable, "scripts/render_html.py", d, cwd=wt, capture=False)
        selected, skipped = select_paths(status_entries(wt), d, args.blog_only)
        if not any(p == f"vault/daily/{d}.md" for p in selected):
            print(f"{d}: 새 데일리가 없어 건너뜀(이미 main에 있거나 생성 안 됨)")
            continue
        print(f"커밋 {len(selected)}개, 남김 {len(skipped)}개")
        sha = commit_and_push(wt, selected, f"econ-radar: {d} 데일리 발행 ({args.provider})", args.no_push)
        done.append(d)
        if sha and not args.no_wait:
            ok = wait_actions(wt, sha, expected_workflows(selected), args.timeout_min)
            ok &= wait_blog(d)
            if not ok:
                print(f"{d} 발행 확인 실패. 다음 날짜로 넘어가지 않습니다.", file=sys.stderr)
                return 5

    if args.weekly:
        week = week_of_last_sunday(today) if args.weekly == "auto" else args.weekly
        if not WEEK_RE.fullmatch(week):
            ap.error(f"주 형식 오류: {week}")
        rc = publish_weekly(wt, week, args)
        if rc:
            return rc
    print(f"\n완료: 데일리 {len(done)}개 {', '.join(done)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
