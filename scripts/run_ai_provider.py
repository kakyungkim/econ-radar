#!/usr/bin/env python3
"""Provider-neutral noninteractive runner for econ-radar."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROMPT_TEMPLATE = ROOT / "scripts" / "prompts" / "daily-provider.md"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def build_command(provider: str, model: str | None, log_path: Path) -> list[str]:
    if provider == "codex":
        binary = os.environ.get("CODEX_BIN", "codex")
        cmd = [binary, "exec", "--approve-for-me", "--cd", str(ROOT),
               "--output-last-message", str(log_path)]
        if model:
            cmd += ["--model", model]
        return cmd + ["-"]
    if provider == "claude":
        binary = os.environ.get("CLAUDE_BIN", "claude")
        cmd = [binary, "--print", "--permission-mode", "acceptEdits",
               "--allowedTools", "Read,Write,Edit,Glob,Grep,WebSearch,WebFetch",
               "--output-format", "text"]
        if model:
            cmd += ["--model", model]
        return cmd
    raise ValueError(f"지원하지 않는 AI_PROVIDER: {provider}")


def render_prompt(date: str, provider: str) -> str:
    text = PROMPT_TEMPLATE.read_text(encoding="utf-8")
    return text.replace("{{DATE}}", date).replace("{{PROVIDER}}", provider)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("--provider", choices=("codex", "claude"),
                        default=os.environ.get("AI_PROVIDER", "codex"))
    parser.add_argument("--model", default=os.environ.get("AI_MODEL") or None)
    parser.add_argument("--dry-run", action="store_true",
                        default=os.environ.get("AI_DRY_RUN") == "1")
    args = parser.parse_args()
    if not DATE_RE.fullmatch(args.date):
        parser.error("date는 YYYY-MM-DD 형식이어야 합니다")

    run_dir = ROOT / "artifacts" / "runs"
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / f"{args.date}-{args.provider}.log"
    cmd = build_command(args.provider, args.model, log_path)
    prompt = render_prompt(args.date, args.provider)

    if args.dry_run:
        print(f"provider={args.provider}")
        print("command=" + " ".join(cmd))
        print(f"prompt={PROMPT_TEMPLATE.relative_to(ROOT)}")
        return 0
    if shutil.which(cmd[0]) is None:
        print(f"실행 파일을 찾을 수 없습니다: {cmd[0]}", file=sys.stderr)
        return 2
    completed = subprocess.run(cmd, input=prompt, text=True, cwd=ROOT)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
