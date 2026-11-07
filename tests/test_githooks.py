"""저장소 훅 검사. 임시 저장소에서 실제 git commit 으로 돌린다."""
import pathlib
import subprocess

HOOKS = pathlib.Path(__file__).resolve().parents[1] / ".githooks"


def _repo(tmp_path):
    def git(*a):
        return subprocess.run(["git", *a], cwd=tmp_path, capture_output=True, text=True)
    git("init", "-q")
    git("config", "user.name", "t"); git("config", "user.email", "t@t")
    git("config", "core.hooksPath", str(HOOKS))
    return git


def test_ai_trailer_removed_human_kept(tmp_path):
    git = _repo(tmp_path)
    (tmp_path / "a.txt").write_text("x")
    git("add", "a.txt")
    msg = ("econ-radar: t\n\n본문\n\nCo-Authored-By: 동료 <a@b.c>\n"
           "Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n")
    assert git("commit", "-q", "-m", msg).returncode == 0
    body = git("log", "-1", "--format=%B").stdout
    assert "anthropic" not in body.lower()
    assert "동료" in body and "본문" in body


def test_mass_delete_blocked(tmp_path):
    git = _repo(tmp_path)
    for i in range(30):
        (tmp_path / f"f{i}.txt").write_text("x")
    git("add", "-A"); git("commit", "-q", "-m", "init")
    git("rm", "-q", "-r", "--cached", ".")
    assert git("commit", "-q", "-m", "oops").returncode != 0
