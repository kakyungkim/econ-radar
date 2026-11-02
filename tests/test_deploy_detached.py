"""deploy.sh가 블로그 저장소의 detached HEAD에서도 실제로 공개하는지, 못 했으면 실패로 끝나는지 검사.

2026-10-28 클라우드 세션은 econ-radar에서 "detached HEAD 상태라 push가 안 됐습니다"를 겪은 뒤 deploy.sh를 돌렸고
"발행 완료"로 보고했지만 블로그에는 커밋이 없었다. detached HEAD에서 커밋하고 `git push origin main`을 하면
옛 main을 밀어 "Everything up-to-date"로 성공 종료한다.
"""
import os, subprocess, tempfile

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATE = "2026-10-28"  # vault/html 에 렌더본이 있는 날짜


def sh(*a, cwd=None, env=None):
    return subprocess.run(a, cwd=cwd, env=env, capture_output=True, text=True)


def _blog(tmp):
    remote = os.path.join(tmp, "remote.git")
    sh("git", "init", "-q", "--bare", remote)  # 오래된 git은 init -b 를 모른다
    sh("git", "--git-dir", remote, "symbolic-ref", "HEAD", "refs/heads/main")
    seed = os.path.join(tmp, "seed")
    sh("git", "clone", "-q", remote, seed)
    sh("git", "checkout", "-q", "-b", "main", cwd=seed)
    os.makedirs(os.path.join(seed, "econ-radar"))
    open(os.path.join(seed, "econ-radar", "index.html"), "w").write("<!-- ENTRIES:INSERT_AFTER -->\n")
    for a in (("add", "-A"), ("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "seed"), ("push", "-q", "origin", "main")):
        sh("git", *a, cwd=seed)
    blog = os.path.join(tmp, "blog")
    sh("git", "clone", "-q", remote, blog)
    sh("git", "checkout", "-q", "--detach", "origin/main", cwd=blog)  # 클라우드 세션과 같은 상태
    return remote, blog


def test_deploy_from_detached_head_publishes_or_fails():
    with tempfile.TemporaryDirectory() as tmp:
        remote, blog = _blog(tmp)
        env = dict(os.environ, BLOG=blog, CONFIRM="0",
                   GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
        r = sh("bash", os.path.join(ROOT, "deploy.sh"), DATE, "제목", env=env)
        published = sh("git", "--git-dir", remote, "cat-file", "-e", "main:econ-radar/%s.html" % DATE).returncode == 0
        assert published or r.returncode != 0, "공개되지 않았는데 성공으로 끝났다:\n" + r.stdout + r.stderr
        assert published, r.stdout + r.stderr


def _run(blog):
    env = dict(os.environ, BLOG=blog, CONFIRM="0",
               GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    return sh("bash", os.path.join(ROOT, "deploy.sh"), DATE, "제목", env=env)


def test_deploy_on_branch_still_publishes():
    with tempfile.TemporaryDirectory() as tmp:
        remote, blog = _blog(tmp)
        sh("git", "checkout", "-q", "main", cwd=blog)
        r = _run(blog)
        assert r.returncode == 0, r.stdout + r.stderr
        assert sh("git", "--git-dir", remote, "cat-file", "-e", "main:econ-radar/%s.html" % DATE).returncode == 0


def test_rejected_push_fails():
    # 다른 세션이 먼저 블로그에 올려 원격이 앞서 있으면 push가 거부된다. 성공으로 끝나면 안 된다.
    with tempfile.TemporaryDirectory() as tmp:
        remote, blog = _blog(tmp)
        seed = os.path.join(tmp, "seed")
        open(os.path.join(seed, "other.html"), "w").write("x")
        for a in (("add", "-A"), ("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "other"), ("push", "-q", "origin", "main")):
            sh("git", *a, cwd=seed)
        r = _run(blog)
        assert r.returncode != 0
        assert "공개 완료" not in r.stdout
