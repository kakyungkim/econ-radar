"""send_email.prepare_email 검사. 모듈을 import 하면 API 호출까지 돌므로 함수만 꺼내 쓴다."""
import ast
import html as htmllib
import pathlib
import re

SRC = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "send_email.py"


def _load():
    tree = ast.parse(SRC.read_text(encoding="utf-8"))
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "prepare_email")
    ns = {"re": re, "htmllib": htmllib}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(SRC), "exec"), ns)
    return ns["prepare_email"]


def test_subject_comment_removed_and_unescaped():
    prepare = _load()
    body = '<!-- SUBJECT: 📈 econ-radar 2026-11-07 · 심혈관 R&amp;D -->\n<html><body>본문</body></html>'
    subject, out = prepare(body, "2026-11-07")
    assert subject == "📈 econ-radar 2026-11-07 · 심혈관 R&D"
    assert "SUBJECT" not in out
    assert out.startswith("<html>")


def test_missing_comment_falls_back():
    prepare = _load()
    subject, out = prepare("<html></html>", "2026-11-08")
    assert subject == "econ-radar 2026-11-08"
    assert out == "<html></html>"


def test_real_email_files_have_no_visible_subject_after_prepare():
    prepare = _load()
    files = sorted((SRC.parents[1] / "vault" / "email").glob("2026-11-0*.html"))
    assert files
    for f in files:
        subject, out = prepare(f.read_text(encoding="utf-8"), f.stem)
        assert "SUBJECT:" not in out, f
        assert "&amp;" not in subject, f
