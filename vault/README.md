---
type: home
---
# 🏠 econ-radar vault — 홈 노트

이 폴더가 **지식 자산**이자 **옵시디언 vault**다. 옵시디언에서 이 `vault/` 폴더를 열면 그래프·백링크·태그로 쓸 수 있다.

## 산출물 지도 (어디에 뭐가 남나)
| 폴더 | 내용 | 누가 만드나 | 다음이 읽음 |
| --- | --- | --- | --- |
| `daily/` | 일일 뉴스레터(데일리노트) | newsletter-editor | 나, 렌더러, 큐레이터, 3층 |
| `raw/` | 수집 원본(출처 포함) | news-scout | 분석가 |
| `analysis/` | 산업·투자 / 커리어 분석 | market-analyst, career-analyst | 편집자 |
| `topics/` | 주제별 MOC(누적 자산의 핵심) | knowledge-curator | 내일 수집, 3층 저술 |
| `reports/` | 동향 리포트(주/월) | trend-synthesizer | 블로그·책 |
| `blog/` | 블로그 초안(draft) | content-writer | 나(검토)→발행 |
| `book/` | 책 목차·챕터 | content-writer | 나(검토)→출판 |
| `push/` | 푸시용 짧은 메시지 | report-renderer | 나(읽기/발송) |
| `html/` | HTML 시각 리포트(일일) | report-renderer | 나(브라우저) |
| `_meta/` | 개선 기록 등 | 오케스트레이터 | 다음 실행 |

## 주제 MOC (자산이 자라는 곳)
- [[topics/AI]]
- [[topics/바이오제약]]
- [[topics/신약개발전략]]
- [[topics/투자테마]]
- [[topics/커리어]]

## 전체 흐름
```
매일: 수집 → 분석(산업·투자·커리어) → 뉴스레터 → HTML·푸시 → vault 정리
누적: daily/analysis → topics MOC (복리로 쌓임)
저술: topics/reports → 동향 → 블로그 → 책
```

## 시작하기
- "오늘 econ-radar 돌려줘" → 오늘치 뉴스레터·HTML·푸시 생성.
- 며칠 쌓이면 "이번 주 동향 리포트" → 자산이 글이 되기 시작.
