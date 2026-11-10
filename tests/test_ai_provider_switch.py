import importlib.util
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("run_ai_provider", ROOT / "scripts" / "run_ai_provider.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_codex_command_uses_noninteractive_exec(tmp_path):
    cmd = MODULE.build_command("codex", None, tmp_path / "run.log")
    assert cmd[:2] == ["codex", "exec"]
    assert "--approve-for-me" in cmd
    assert "--sandbox" not in cmd
    assert cmd[-1] == "-"


def test_claude_command_uses_print_mode_without_bash(tmp_path):
    cmd = MODULE.build_command("claude", None, tmp_path / "run.log")
    assert "--print" in cmd
    tools = cmd[cmd.index("--allowedTools") + 1]
    assert "WebSearch" in tools
    assert "Bash" not in tools


def test_both_providers_have_dry_run():
    for provider in ("codex", "claude"):
        result = subprocess.run([sys.executable, "scripts/run_ai_provider.py", "2026-11-11",
                                 "--provider", provider, "--dry-run"],
                                cwd=ROOT, text=True, capture_output=True)
        assert result.returncode == 0, result.stderr
        assert f"provider={provider}" in result.stdout


def test_unknown_provider_is_rejected(tmp_path):
    try:
        MODULE.build_command("other", None, tmp_path / "run.log")
    except ValueError as exc:
        assert "지원하지 않는" in str(exc)
    else:
        raise AssertionError("unknown provider must fail")
