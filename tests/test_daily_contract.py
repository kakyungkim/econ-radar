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
