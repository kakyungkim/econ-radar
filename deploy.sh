#!/usr/bin/env bash
# econ-radar 발행 배포 스크립트
# 렌더된 데일리 HTML을 블로그(GitHub Pages)로 복사 → 아카이브 index 갱신 → commit → push.
#
# 사용법:
#   ./deploy.sh                      # 오늘 날짜 발행본 배포 (push 전 확인)
#   ./deploy.sh 2026-06-11           # 특정 날짜
#   ./deploy.sh 2026-06-11 "오늘 헤드라인"   # 목록에 보일 제목 지정
#   CONFIRM=0 ./deploy.sh            # 확인 없이 바로 push
#   BLOG=~/work/kakyungkim.github.io ./deploy.sh   # 블로그 repo 경로 덮어쓰기
set -euo pipefail

DATE="${1:-$(date +%F)}"
TITLE="${2:-econ-radar 데일리 — $DATE}"
CONFIRM="${CONFIRM:-1}"   # 1 = push 전 확인 / 0 = 바로 push

# econ-radar repo = 이 스크립트가 있는 폴더. 블로그 repo는 기본 ~/kakyungkim.github.io (BLOG로 덮어쓰기)
ECON="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG="${BLOG:-$HOME/kakyungkim.github.io}"
SRC="$ECON/vault/html/$DATE.html"
DST="$BLOG/econ-radar/$DATE.html"
IDX="$BLOG/econ-radar/index.html"

[ -f "$SRC" ] || { echo "❌ 렌더 파일이 없습니다: $SRC  (먼저 데일리를 렌더하세요)"; exit 1; }
[ -d "$BLOG/econ-radar" ] || { echo "❌ 블로그 econ-radar 폴더 없음: $BLOG/econ-radar  (BLOG 경로 확인)"; exit 1; }

cp "$SRC" "$DST"
echo "✅ 복사: econ-radar/$DATE.html"

if grep -q "$DATE.html" "$IDX"; then
  echo "ℹ️  index에 $DATE 이미 있음 — 목록 추가 건너뜀"
else
  ENTRY="        <a href=\"$DATE.html\" class=\"block bg-white border border-gray-200 rounded-xl p-5 shadow-sm hover:shadow-md hover:border-indigo-200 transition\"><p class=\"text-xs text-gray-400 mb-1\">$DATE</p><p class=\"font-bold text-gray-900 text-[16px] leading-snug\">$TITLE</p></a>"
  awk -v e="$ENTRY" '{print} /<!-- ENTRIES:INSERT_AFTER -->/{print e}' "$IDX" > "$IDX.tmp" && mv "$IDX.tmp" "$IDX"
  echo "✅ index 목록에 $DATE 추가"
fi

cd "$BLOG"
git add "econ-radar/$DATE.html" "econ-radar/index.html"
if git diff --cached --quiet; then echo "변경 없음 — 종료"; exit 0; fi
git commit -q -m "econ-radar: $DATE 발행"
echo "✅ 커밋 완료"

if [ "$CONFIRM" = "1" ]; then
  read -r -p "지금 push 해서 공개할까요? [y/N] " yn
  case "$yn" in
    [yY]*) git push origin main && echo "🚀 공개 완료 (1~2분 뒤 라이브)";;
    *)     echo "⏸  push 보류 — 나중에:  (cd \"$BLOG\" && git push)";;
  esac
else
  git push origin main && echo "🚀 공개 완료 (1~2분 뒤 라이브)"
fi
