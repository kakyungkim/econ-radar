---
name: content-studio-orchestrator
description: econ-radar의 저술 파이프라인 입구(3층). "이번 주/달 동향 리포트", "이 주제로 블로그 써줘", "책 목차/챕터 만들어줘", "블로그 초안 다듬어줘" 같은, 누적된 vault 자산을 동향 리포트·블로그·책으로 끌어올리는 요청에서 사용한다. vault에 재료가 쌓인 뒤 가동한다.
---

# content-studio-orchestrator (3층 진행표 / 저술 팀장)

매일 쌓인 vault 자산을 동향 리포트·블로그·책으로 끌어올리는 저술 파이프라인을 지휘한다.

## 언제 이 스킬을 쓰나
- "이번 주/이번 달 동향 리포트 만들어줘".
- "{주제}로 블로그 글 써줘", "블로그 초안 다듬어줘".
- "책 목차 잡아줘", "{주제} 챕터 써줘".

## 가동 전 확인
- vault에 재료가 충분한지 본다(`vault/analysis/`, `vault/topics/`). 너무 적으면 "아직 재료가 적습니다 — 며칠 더 쌓고 권장" 안내 후 진행 여부를 묻는다.

## 요청 분기
| 요청 | 흐름 | 산출물 |
| --- | --- | --- |
| 동향 리포트 | trend-synthesizer | `vault/reports/YYYY-Www-동향.md` |
| 블로그 | (동향 부족 시 trend-synthesizer 먼저 →) content-writer(블로그 모드) | `vault/blog/YYYY-MM-DD-{슬러그}.md` |
| 책 | content-writer(저술 모드) | `vault/book/outline.md`, `vault/book/chNN-*.md` |

## 실행 흐름
1. 필요한 작가만 `TeamCreate`로 구성(보통 1~2명: trend-synthesizer, content-writer).
2. `TaskCreate`로 단계 등록(예: T1 동향 종합 → T2 블로그 저술, 의존관계 설정).
3. 작가는 vault의 동향·MOC·원본을 읽어 산문으로 저술하고 파일로 저장한다.
4. 팀장은 `TaskGet`으로 진행을 확인하고, 부족한 근거가 있으면 trend-synthesizer 보강을 지시한다.
5. 결과를 사람이 검토하도록 제시한다.

## 사람 승인 게이트 (두껍게)
- 블로그·책 산출물은 **항상 `status: draft`**.
- **외부 발행·공개(블로그 게시, 원고 제출, 출판)는 사람이 검토·승인한 뒤**에만. 팀장은 발행하지 않고 "초안 준비됨 — 검토하세요"로 끝낸다.

## 마무리
- 저술 결과를 knowledge-curator가 vault에 연결하도록 `vault/topics/`와 상호 링크를 남긴다.
- `vault/_meta/improvement-log.md`에 저술 메모를 남기고 `TeamDelete`.

## 산출물 계약
| 단계 | 파일 | 다음 단계 |
| --- | --- | --- |
| 동향 | `vault/reports/*.md` | 블로그·책의 1차 재료 |
| 블로그 | `vault/blog/*.md` (draft) | 사람 검토 → 발행 |
| 책 | `vault/book/outline.md`, `chNN-*.md` | 사람 검토 → 출판 |
