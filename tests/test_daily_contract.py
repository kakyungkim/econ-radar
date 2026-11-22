import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_daily_contract", ROOT / "scripts" / "validate_daily_contract.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_invalid_date_is_rejected():
    errors, _, provider = MODULE.validate("not-a-date")
    assert errors
    assert provider == "unknown"


def test_complete_contract_passes_and_missing_render_fails(tmp_path, monkeypatch):
    monkeypatch.setattr(MODULE, "ROOT", tmp_path)
    date = "2026-11-11"
    files = {
        f"vault/raw/news-{date}.md": "출처 https://example.com/raw\n",
        f"vault/analysis/market-{date}.md": "시장 분석\n",
        f"vault/analysis/company-{date}.md": "기업 분석\n",
        f"vault/daily/{date}.md": (
            f"---\ndate: {date}\nprovider: claude\n---\n"
            "본문 https://example.com/daily\n"
        ),
        f"artifacts/runs/{date}-claude.log": "provider=claude\nreturncode=0\n",
    }
    for relative, content in files.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    errors, warnings, provider = MODULE.validate(date, provider="claude")
    assert not errors
    assert not warnings
    assert provider == "claude"
    errors, _, _ = MODULE.validate(date, provider="claude", require_rendered=True)
    assert any("vault/html" in error for error in errors)
    assert any("vault/push" in error for error in errors)


def test_record_provider_adds_and_updates_frontmatter(tmp_path):
    spec = importlib.util.spec_from_file_location(
        "run_daily_pipeline", ROOT / "scripts" / "run_daily_pipeline.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    daily = tmp_path / "daily.md"
    daily.write_text("---\ndate: 2026-11-11\ntype: daily\n---\n본문\n", encoding="utf-8")
    module.record_provider(daily, "claude")
    assert "provider: claude" in daily.read_text(encoding="utf-8")
    module.record_provider(daily, "codex")
    text = daily.read_text(encoding="utf-8")
    assert "provider: codex" in text
    assert text.count("provider:") == 1


def test_date_first_analysis_names_warn_but_do_not_block(tmp_path, monkeypatch):
    # 2026-11-16 실제 발행분은 analysis/2026-11-16-market.md, 2026-11-16-companies.md 로 저장됐다.
    # 이름만 다른 분석 파일 때문에 발행 워크플로가 막히면 안 된다.
    monkeypatch.setattr(MODULE, "ROOT", tmp_path)
    date = "2026-11-16"
    files = {
        f"vault/raw/news-{date}.md": "출처 https://example.com/raw\n",
        f"vault/analysis/{date}-market.md": "시장 분석\n",
        f"vault/analysis/{date}-companies.md": "기업 분석\n",
        f"vault/daily/{date}.md": f"---\ndate: {date}\n---\n본문 https://example.com/d\n",
        f"vault/html/{date}.html": f"<title>{date}</title>\n",
        f"vault/push/{date}.md": "푸시\n",
    }
    for relative, content in files.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    errors, warnings, _ = MODULE.validate(date, provider_hint="claude", require_rendered=True)
    assert not errors
    assert any(f"{date}-market.md" in w for w in warnings)
    assert any(f"{date}-companies.md" in w for w in warnings)
    # 분석 파일이 어떤 이름으로도 없으면 여전히 실패해야 한다.
    (tmp_path / f"vault/analysis/{date}-market.md").unlink()
    errors, _, _ = MODULE.validate(date, provider_hint="claude", require_rendered=True)
    assert any("market" in e for e in errors)


def _write(root, files):
    for relative, content in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def _base_files(date):
    return {
        f"vault/raw/news-{date}.md": "출처 https://example.com/raw\n",
        f"vault/analysis/market-{date}.md": "시장\n",
        f"vault/analysis/company-{date}.md": "기업\n",
        f"vault/daily/{date}.md": f"---\ndate: {date}\n---\n본문 https://example.com/d\n",
    }


def test_missing_frontmatter_uses_committed_run_log_not_a_fixed_guess(tmp_path, monkeypatch):
    # 2026-11-18~22 는 Codex 로 만들었고 frontmatter 없이 실행 로그만 커밋됐다.
    monkeypatch.setattr(MODULE, "ROOT", tmp_path)
    date = "2026-11-18"
    files = _base_files(date)
    files[f"artifacts/runs/{date}-codex.log"] = "returncode=0\n"
    files[f"artifacts/runs/{date}-codex-topics-provider.log"] = "보조 실행\n"
    _write(tmp_path, files)
    errors, warnings, provider = MODULE.validate(date)
    assert not errors
    assert provider == "codex"
    assert any("실행 로그" in w for w in warnings)


def test_no_frontmatter_and_no_log_is_unknown(tmp_path, monkeypatch):
    monkeypatch.setattr(MODULE, "ROOT", tmp_path)
    date = "2026-11-19"
    _write(tmp_path, _base_files(date))
    errors, _, provider = MODULE.validate(date)
    assert not errors
    assert provider == "unknown"


def test_both_provider_logs_is_unknown(tmp_path, monkeypatch):
    monkeypatch.setattr(MODULE, "ROOT", tmp_path)
    date = "2026-11-20"
    files = _base_files(date)
    files[f"artifacts/runs/{date}-codex.log"] = "x\n"
    files[f"artifacts/runs/{date}-claude.log"] = "x\n"
    _write(tmp_path, files)
    _, warnings, provider = MODULE.validate(date)
    assert provider == "unknown"
    assert any("둘 다" in w for w in warnings)


def test_publish_workflows_do_not_hardcode_a_provider():
    # 발행 워크플로는 어느 제공자가 원고를 만들었는지 모른다. 고정 힌트를 넘기면 Codex 날도 claude 로 찍힌다.
    for name in ("daily-blog-publish.yml", "email-push.yml", "telegram-push.yml"):
        text = (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")
        assert "validate_daily_contract.py" in text, name
        assert "--provider-hint" not in text, name
