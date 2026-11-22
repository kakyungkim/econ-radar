"""manual_publish.py 의 순수 함수 계약 검사.

틀리면 다른 날짜 파일이나 관계없는 파일이 main 에 올라가 자동 발송되므로 먼저 쓴다.
"""
from datetime import date
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("manual_publish", ROOT / "scripts" / "manual_publish.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)


def test_missing_dates_only_feed_without_daily_in_window():
    feeds = {"2026-11-01", "2026-11-17", "2026-11-18", "2026-11-19", "2026-11-23"}
    dailies = {"2026-11-17"}
    got = mp.missing_dates(feeds, dailies, today=date(2026, 11, 22), days=14)
    # 11-01 은 창 밖, 11-17 은 이미 있음, 11-23 은 미래
    assert got == ["2026-11-18", "2026-11-19"]


def test_missing_dates_sorted_oldest_first():
    feeds = {"2026-11-20", "2026-11-18", "2026-11-19"}
    assert mp.missing_dates(feeds, set(), today=date(2026, 11, 20)) == [
        "2026-11-18", "2026-11-19", "2026-11-20"]


def test_parse_porcelain_z_keeps_korean_paths_unquoted():
    raw = " M vault/daily/index.md\0?? vault/topics/바이오제약.md\0?? vault/daily/2026-11-18.md\0"
    assert mp.parse_porcelain_z(raw) == [
        (" M", "vault/daily/index.md"),
        ("??", "vault/topics/바이오제약.md"),
        ("??", "vault/daily/2026-11-18.md"),
    ]


ENTRIES = [
    (" M", "vault/daily/index.md"),
    (" M", "vault/_meta/recent-headlines.md"),
    (" M", "vault/topics/AI반도체.md"),
    ("??", "vault/topics/새주제.md"),
    ("??", "vault/raw/news-2026-11-18.md"),
    ("??", "vault/analysis/market-2026-11-18.md"),
    ("??", "vault/analysis/company-2026-11-18.md"),
    ("??", "vault/daily/2026-11-18.md"),
    ("??", "vault/html/2026-11-18.html"),
    ("??", "vault/push/2026-11-18.md"),
    ("??", "vault/email/2026-11-18.html"),
    ("??", "artifacts/runs/2026-11-18-codex.log"),
    # 아래는 올라가면 안 된다
    ("??", "artifacts/runs/2026-11-19-codex.log"),
    ("??", "vault/daily/2026-11-19.md"),
    ("??", "vault/push/2026-11-19.md"),
    (" M", "scripts/render_html.py"),
    ("??", "vault/html/2026-W40-동향.html"),
]


def test_select_paths_takes_only_target_date_and_shared_indexes():
    selected, skipped = mp.select_paths(ENTRIES, "2026-11-18")
    assert "vault/push/2026-11-18.md" in selected
    assert "vault/email/2026-11-18.html" in selected
    assert "vault/topics/AI반도체.md" in selected
    assert "vault/topics/새주제.md" in selected
    assert "vault/daily/index.md" in selected
    assert "vault/_meta/recent-headlines.md" in selected
    for bad in ("artifacts/runs/2026-11-19-codex.log", "vault/daily/2026-11-19.md",
                "vault/push/2026-11-19.md", "scripts/render_html.py",
                "vault/html/2026-W40-동향.html"):
        assert bad not in selected
        assert bad in skipped
    assert len(selected) + len(skipped) == len(ENTRIES)


def test_select_paths_blog_only_drops_push_and_email():
    selected, skipped = mp.select_paths(ENTRIES, "2026-11-18", blog_only=True)
    assert "vault/html/2026-11-18.html" in selected
    assert "vault/push/2026-11-18.md" not in selected
    assert "vault/email/2026-11-18.html" not in selected
    assert "vault/push/2026-11-18.md" in skipped


def test_select_paths_never_takes_deletions():
    selected, skipped = mp.select_paths([(" D", "vault/topics/AI반도체.md")], "2026-11-18")
    assert selected == [] and skipped == ["vault/topics/AI반도체.md"]


def test_expected_workflows_follow_paths():
    full = mp.expected_workflows(["vault/html/2026-11-18.html", "vault/push/2026-11-18.md"])
    assert full == {"Daily Blog Publish", "Telegram Daily Push", "Email Daily Push (Buttondown)"}
    assert mp.expected_workflows(["vault/html/2026-11-18.html"]) == {"Daily Blog Publish"}


def test_week_of_last_sunday():
    assert mp.week_of_last_sunday(date(2026, 11, 22)) == "2026-W47"  # 일요일 당일
    assert mp.week_of_last_sunday(date(2026, 11, 23)) == "2026-W47"  # 월요일
    assert mp.week_of_last_sunday(date(2026, 11, 28)) == "2026-W47"  # 토요일
