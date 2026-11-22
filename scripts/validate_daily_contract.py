#!/usr/bin/env python3
"""Validate provider-neutral econ-radar daily artifacts before publication."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"https?://")
PROVIDER_RE = re.compile(r"^provider:\s*([a-z0-9_-]+)\s*$", re.MULTILINE)


def _nonempty(path: Path, errors: list[str]) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"필수 산출물 누락 또는 빈 파일: {path.relative_to(ROOT)}")


def _provider_from_run_logs(date: str, warnings: list[str]) -> str:
    """frontmatter가 없을 때 커밋된 실행 로그(artifacts/runs/DATE-PROVIDER.log)로 제공자를 판단한다."""
    run_dir = ROOT / "artifacts" / "runs"
    found = [name for name in ("codex", "claude")
             if (run_dir / f"{date}-{name}.log").is_file()]
    if len(found) == 1:
        warnings.append(f"provider frontmatter 없음; 실행 로그 {date}-{found[0]}.log로 {found[0]} 판단")
        return found[0]
    if found:
        warnings.append("provider frontmatter 없음; codex, claude 실행 로그가 둘 다 있어 unknown")
    else:
        warnings.append("provider frontmatter 없음; 실행 로그도 없어 unknown")
    return "unknown"


def validate(date: str, *, provider: str | None = None,
             provider_hint: str | None = None,
             require_rendered: bool = False) -> tuple[list[str], list[str], str]:
    errors: list[str] = []
    warnings: list[str] = []
    if not DATE_RE.fullmatch(date):
        return ["date는 YYYY-MM-DD 형식이어야 합니다"], warnings, "unknown"

    raw = ROOT / "vault" / "raw" / f"news-{date}.md"
    analysis = ROOT / "vault" / "analysis"
    daily = ROOT / "vault" / "daily" / f"{date}.md"
    for path in (raw, daily):
        _nonempty(path, errors)
    # 표준 이름이 없으면 과거 세션이 쓴 이름(companies-DATE, DATE-market 등)을 경고로만 받는다.
    # 이름 차이로 발행 워크플로 전체가 멈추지 않게 한다(2026-11-16 발행분 사례).
    for canonical, legacy_names in (
        (f"market-{date}.md", (f"{date}-market.md",)),
        (f"company-{date}.md", (f"companies-{date}.md", f"{date}-companies.md",
                                f"{date}-company.md")),
    ):
        path = analysis / canonical
        if path.is_file() and path.stat().st_size > 0:
            continue
        legacy = next((analysis / name for name in legacy_names
                       if (analysis / name).is_file() and (analysis / name).stat().st_size > 0),
                      None)
        if legacy:
            warnings.append(
                f"구형 파일명 사용: {legacy.relative_to(ROOT)}; 다음 실행부터 {canonical} 사용"
            )
        else:
            errors.append(f"필수 산출물 누락 또는 빈 파일: {path.relative_to(ROOT)}")

    if daily.is_file():
        daily_text = daily.read_text(encoding="utf-8")
        if f"date: {date}" not in daily_text[:1000]:
            errors.append("데일리 frontmatter 날짜 불일치")
        match = PROVIDER_RE.search(daily_text[:1000])
        if match:
            recorded_provider = match.group(1)
        elif provider_hint:
            recorded_provider = provider_hint
            warnings.append(f"provider frontmatter 없음; 실행 경로 힌트로 {recorded_provider} 기록")
        else:
            recorded_provider = _provider_from_run_logs(date, warnings)
        if provider and recorded_provider != provider:
            errors.append(f"제공자 기록 불일치: 기대={provider}, 기록={recorded_provider}")
    else:
        recorded_provider = provider or provider_hint or "unknown"

    for path in (raw, daily):
        if path.is_file() and not URL_RE.search(path.read_text(encoding="utf-8")):
            errors.append(f"직접 근거 URL 없음: {path.relative_to(ROOT)}")

    if provider:
        log_path = ROOT / "artifacts" / "runs" / f"{date}-{provider}.log"
        _nonempty(log_path, errors)

    if require_rendered:
        html = ROOT / "vault" / "html" / f"{date}.html"
        push = ROOT / "vault" / "push" / f"{date}.md"
        for path in (html, push):
            _nonempty(path, errors)
        if html.is_file() and date not in html.read_text(encoding="utf-8")[:5000]:
            errors.append("HTML에 대상 날짜가 없습니다")

    return errors, warnings, recorded_provider


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("--provider", choices=("codex", "claude"))
    parser.add_argument("--provider-hint", choices=("codex", "claude"))
    parser.add_argument("--require-rendered", action="store_true")
    args = parser.parse_args()
    errors, warnings, recorded_provider = validate(
        args.date,
        provider=args.provider,
        provider_hint=args.provider_hint,
        require_rendered=args.require_rendered,
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"contract_ok date={args.date} provider={recorded_provider}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
