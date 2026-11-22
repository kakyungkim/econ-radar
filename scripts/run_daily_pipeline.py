#!/usr/bin/env python3
"""Collect (if needed), invoke selected AI provider, validate, and render."""
from __future__ import annotations

import argparse
import importlib.util
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def run(*cmd: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=ROOT, text=True, check=check)


def record_provider(daily: Path, provider: str) -> None:
    """Record provenance deterministically after either provider finishes."""
    text = daily.read_text(encoding="utf-8")
    if re.search(r"^provider:\s*", text, flags=re.MULTILINE):
        text = re.sub(r"^provider:\s*.*$", f"provider: {provider}", text,
                      count=1, flags=re.MULTILINE)
    elif text.startswith("---\n"):
        lines = text.splitlines(keepends=True)
        insert_at = next(
            (index + 1 for index, line in enumerate(lines[:20])
             if line.startswith("date:")),
            1,
        )
        lines.insert(insert_at, f"provider: {provider}\n")
        text = "".join(lines)
    else:
        raise ValueError("데일리 frontmatter가 없어 provider를 기록할 수 없습니다")
    daily.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("--provider", choices=("codex", "claude"),
                        default=os.environ.get("AI_PROVIDER", "codex"))
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not DATE_RE.fullmatch(args.date):
        parser.error("date는 YYYY-MM-DD 형식이어야 합니다")

    daily = ROOT / "vault" / "daily" / f"{args.date}.md"
    if daily.exists() and not args.force:
        print(f"이미 존재하여 건너뜀: {daily.relative_to(ROOT)}")
        return 0
    feed = ROOT / "vault" / "raw" / f"feed-{args.date}.json"
    if not feed.exists() and not args.dry_run:
        run("python3", "scripts/collect_news.py", args.date)
    provider_cmd = ["python3", "scripts/run_ai_provider.py", args.date,
                    "--provider", args.provider]
    if args.dry_run:
        provider_cmd.append("--dry-run")
        run(*provider_cmd)
        return 0
    run(*provider_cmd)

    if not daily.exists() or daily.stat().st_size == 0:
        print(f"필수 산출물 누락: {daily.relative_to(ROOT)}", file=sys.stderr)
        return 3
    try:
        record_provider(daily, args.provider)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 4
    run("python3", "scripts/validate_daily_contract.py", args.date,
        "--provider", args.provider)
    run("python3", "scripts/render_html.py", args.date)
    run("python3", "scripts/validate_daily_contract.py", args.date,
        "--provider", args.provider, "--require-rendered")
    run("python3", "scripts/check_market_numbers.py", args.date, check=False)
    if importlib.util.find_spec("pytest"):
        run(sys.executable, "-m", "pytest", "-q", "tests/test_render_seo.py",
            "tests/test_render_english.py", "tests/test_ai_provider_switch.py",
            "tests/test_daily_contract.py")
    else:
        print("pytest가 현재 Python에 없어 로컬 회귀 테스트를 건너뜀(CI에서는 설치 후 필수 실행)")
    print(f"생성·검증 완료: {args.date} ({args.provider})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
