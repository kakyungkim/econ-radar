---
name: content-studio-orchestrator
description: econ-radar vault의 데일리와 주제 자산을 주간·월간 동향, 블로그, 책 초안으로 끌어올릴 때 Codex와 Claude가 공통으로 사용하는 저술 오케스트레이터다.
---

# content studio orchestrator

## 입력과 분기

- 주간·월간 동향: `vault/daily/`, `vault/analysis/`, `vault/topics/`를 읽어 `vault/reports/`에 작성한다.
- 블로그: 동향과 주제 문서를 근거로 `vault/blog/`에 `status: draft`로 작성한다.
- 책: `vault/book/outline.md`와 장별 초안을 작성한다.

## 공통 기준

1. 원문으로 거슬러갈 수 있는 링크를 유지한다.
2. 새로운 사실이나 수치를 근거 없이 추가하지 않는다.
3. 동향은 사건 나열보다 구조 변화와 반대 시나리오를 보여준다.
4. 외부 공개는 별도 사람 승인 전 수행하지 않는다.

## 산출물 계약

| 요청 | 산출물 | 상태 |
| --- | --- | --- |
| 주간 동향 | `vault/reports/YYYY-Www-동향.md` | 검토 가능 |
| 블로그 | `vault/blog/YYYY-MM-DD-slug.md` | draft |
| 책 | `vault/book/outline.md`, `vault/book/chNN-*.md` | draft |
