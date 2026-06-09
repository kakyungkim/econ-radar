---
name: obsidian-vault-conventions
description: econ-radar의 vault를 옵시디언 지식 그래프로 유지하기 위한 공통 규칙. 폴더 구조, frontmatter 태그 체계, [[위키링크]] 규칙, 주제 MOC 구조, 데일리노트 규칙을 정의한다. 모든 에이전트가 노트를 만들거나 연결할 때 따른다.
---

# obsidian-vault-conventions (옵시디언 vault 규칙)

vault 폴더를 옵시디언으로 그대로 열어 그래프·백링크·태그로 쓰기 위한 약속이다. **모든 에이전트가 노트를 쓸 때 이 규칙을 따른다.** knowledge-curator가 유지·점검한다.

## 옵시디언으로 여는 법
- 옵시디언에서 `vault/` 폴더를 vault로 열면 끝(변환 불필요).
- 권장 플러그인: Daily Notes(코어), Graph View(코어), Tag Pane(코어).

## 폴더 구조
| 폴더 | 내용 |
| --- | --- |
| `daily/` | 일일 뉴스레터(데일리노트) `YYYY-MM-DD.md` |
| `raw/` | 수집 원본 |
| `analysis/` | 렌즈별 분석 |
| `topics/` | 주제 MOC(자산의 핵심) |
| `reports/` | 동향 리포트 |
| `blog/` | 블로그 초안 |
| `book/` | 책 목차·챕터 |
| `push/` | 푸시용 메시지 |
| `_meta/` | 개선 기록 등 운영 파일 |

## frontmatter 표준
```yaml
---
date: 2026-06-09        # 날짜 있는 노트
type: daily|raw|analysis|moc|report|blog|book   # 노트 종류
tags: [AI, 바이오제약, 투자테마, 커리어, 거시정책, 산업기업, 글로벌]
links: ["[[topics/AI]]"]   # 핵심 연결(선택)
---
```

## 표준 태그 체계 (초기값)
`AI` `바이오제약` `투자테마` `커리어` `거시정책` `산업기업` `글로벌`
- 새 태그가 필요하면 추가하되, knowledge-curator가 유사 태그 난립을 정리한다.

## 위키링크 규칙
- 일일노트는 자기가 다룬 주제 MOC를 `[[topics/AI]]`처럼 링크한다.
- 주제 MOC는 타임라인에서 각 날짜 노트를 `[[daily/2026-06-09]]`로 링크한다.
- 동향 리포트는 근거가 된 일일노트를 링크한다.
- 링크는 폴더 경로 포함 형식(`[[daily/2026-06-09]]`)으로 통일한다.

## 주제 MOC 구조
`topics/{주제}.md` 는 핵심 흐름(현재 흐름 3줄) + 타임라인(날짜별 한 줄 + 링크) + 연결 주제로 구성한다. knowledge-curator 카드의 형식을 따른다.

## 품질 체크 (knowledge-curator가 매일)
- [ ] 오늘 노트에 frontmatter 태그·날짜가 있는가
- [ ] 오늘 일일노트가 관련 주제 MOC와 상호 링크됐는가
- [ ] 새 주제가 MOC로 생성됐는가
- [ ] 죽은 링크(존재하지 않는 노트 가리킴)가 없는가
- [ ] 유사·중복 태그가 정리됐는가
