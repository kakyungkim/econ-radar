# 뉴스레터 md 구조 계약 (NEWSLETTER-FORMAT)

`scripts/render_html.py`가 `vault/daily/YYYY-MM-DD.md`를 안정적으로 파싱해
`vault/html/YYYY-MM-DD.html`(2026-06-12 양식)과 `vault/push/YYYY-MM-DD.md`로
결정적 렌더링하기 위한 **입력 계약**이다. newsletter-editor의 출력 md는 이 계약을 따라야 한다.

> 기준 양식: `vault/html/2026-06-12.html` (영어 섹션 헤더 · At a Glance 리드 · KEY POINT/INSIGHT/DEMAND 카드 ·
> 영어 배지 Macro·AI·Bio·Market · 경제 영어 발음 버튼 · 좌측 인디고 강조선).
> 파서는 **줄 단위**로 헤더·접두 토큰을 인식한다. 토큰(예: `**Key Point**:`, `## Today's Top 5`)을 정확히 지킬 것.

---

## 0. 전체 골격 (섹션 순서)

```
---  (frontmatter: date 필수)
# econ-radar 데일리 — YYYY-MM-DD
> 부제(한 줄)
**At a Glance**
## Today's Top 5
## 🗣 Today's Topic — {제목}
## 🗽 Business English
# Deep Dive
## Macro & Policy
## AI & Infrastructure
## Bio & Pharma
## 🙋 Demand
## 💰 Investment
## 🚀 Companies to Watch
## Threads to Follow
## Sources
```

- 섹션이 비면 그 섹션은 **조용히 생략**되고 stderr에 경고가 찍힌다.
- 필수 최소 조건: `At a Glance` 또는 `Today's Top 5` 중 하나는 있어야 한다(없으면 비0 종료).
- 섹션 간 `---` 구분선은 있어도/없어도 무방(파서가 무시).

---

## 1. Frontmatter & 제목

```markdown
---
date: 2026-06-11
type: daily
tags: [...]
links: [...]
---

# econ-radar 데일리 — 2026-06-11
> 제약·바이오·AI에 무게를 둔 경제 데일리 — 산업구조·투자·시장 3렌즈
```

- `date:` → 발행 날짜. 없으면 CLI 인자 날짜를 사용.
- H1은 `econ-radar`로 시작. `— YYYY-MM-DD`에서 날짜를 보조 추출.
- 바로 다음의 `>` 인용 한 줄 = 헤더 부제.

## 2. At a Glance

```markdown
**At a Glance**
💰 한 문장…
🏭 한 문장…
🚀 한 문장…
```

- `**At a Glance**` 단독 줄로 시작. 이후 빈 줄 또는 `---` 전까지 각 줄이 한 개의 리드 `<p>`가 된다.
- 줄 앞 이모지는 그대로 표시된다(2~4줄 권장).

## 3. Today's Top 5

```markdown
## Today's Top 5

### 1. {카드 제목}
{리드 문단 — 한 단락(선택)}
**Key Point**: {객관 핵심}
🙋 **Demand**: {수요자 관점(선택)}
💡 **Insight**: {주관 해석(선택)}
출처: [이름](URL) | [이름](URL) — [[topics/거시정책]] | [[topics/AI]]
```

규칙
- 항목 헤더는 정확히 `### N. 제목` (번호+마침표). 최대 5개.
- 콜아웃 접두 토큰(공백·이모지 포함 정확히):
  - `**Key Point**:` → KEY POINT 카드(인디고 좌측선)
  - `🙋 **Demand**:` → Demand 카드(앰버)
  - `💡 **Insight**:` → Insight 카드(틸)
  - 콜아웃은 **md에 적힌 순서대로** 렌더된다.
- 리드 문단(콜아웃·출처가 아닌 일반 문장)은 카드 본문 `<p>`로 들어간다. 없어도 됨.
- `출처:` 줄: `[이름](URL)`들을 ` | `로 나열하고, 끝에 ` — [[topics/…]]`로 주제 위키링크.
  - **배지는 이 위키링크에서 자동 결정**된다(아래 §10 매핑). 위키링크가 없으면 제목 키워드로 추론.

## 4. Today's Topic

```markdown
## 🗣 Today's Topic — {제목}

{문단1}
{문단2}
- 💬 한 줄 요약: {요약}
- 블로그 소재: {…}        ← 렌더 시 무시(메모용)
- 출처: [이름](URL) | [이름](URL)
```

- 헤더의 `—` 뒤가 카드 제목.
- 일반 문장 줄 = 문단. `- 💬 한 줄 요약:` = 보라색 요약 박스. `- 출처:` 첫 링크 = 하단 출처.
- 배지는 제목·본문 키워드로 추론(§10).

## 5. Business English

```markdown
## 🗽 Business English

- **{word} ({영문 풀이, 한국어 뜻})**: {설명}
  - 📝 *{English example sentence}* → {한국어 번역}
```

- 굵은 표제 = `word (…, 뜻)`. 괄호 안 **마지막 콤마 세그먼트**가 화면의 뜻(eng-meaning).
- 괄호 첫 세그먼트가 영문이면 발음 버튼이 그 영문 풀이를, 아니면 word를 읽는다.
- `📝 *영문* → 한국어` = 예문 카드(▶ 재생 버튼이 영문을 읽음). 예문은 선택.

## 6. Deep Dive (Macro & Policy / AI & Infrastructure / Bio & Pharma)

```markdown
# Deep Dive

## Macro & Policy

### [{항목 제목}]({대표 URL})
**관전 포인트**: {본문}
**1차 자료**: [이름](URL) | [이름](URL)
**강세 vs 약세**:
- 강세: {…}
- 약세: {…}
**전략 프레임**: {본문}
```

- `# Deep Dive` 다음에 세 서브섹션(`## Macro & Policy`, `## AI & Infrastructure`, `## Bio & Pharma`)이 온다.
  - 서브섹션 이름이 곧 배지: Macro / AI / Bio.
- 각 항목은 `### [제목](URL)`로 시작하는 접이식(`<details>`) 카드.
- 필드 토큰(정확히):
  - `**관전 포인트**:` → 카드 본문 첫 문단.
  - `**강세 vs 약세**:` + 다음 줄들의 `- 강세…:` / `- 약세…:` → 초록/빨강 2열 그리드(선택).
  - `**전략 프레임**:` → "전략 프레임" 박스(선택).
  - `**1차 자료**:` → 하단 출처 링크(선택).
  - `**Demand …**:` + 이어지는 `- **소항목**: 텍스트` 들 → Demand 콜아웃(선택).

## 7. 🙋 Demand

```markdown
## 🙋 Demand

> 누가 사고 쓰나, 왜 — 수요자 눈으로 본 오늘.

- **{카드 제목}**: {수요자 관점 본문}
```

- `- **제목**: 본문` 불릿 하나가 앰버 카드 1개. 배지는 키워드 추론(§10).
- 첫 `>` 인용은 고정 리드로 대체되므로 자유롭게 적어도 무방.

## 8. 💰 Investment

```markdown
## 💰 Investment

### 오늘의 투자 시사점

- **{카드 제목}**: {본문} 강세 근거: {…} / 약세 근거: {…}
- **국내외 연결 고리**: {본문}        ← 있으면 인디고 박스로 렌더(선택)
```

- `- **제목**: 본문` 불릿 하나가 카드 1개.
- 본문에 `강세 근거: … / 약세 근거: …` 패턴이 있으면 그 부분을 초록/빨강 2열 그리드로 분리하고,
  앞쪽 텍스트는 카드 소개 문단이 된다. 패턴이 없으면 산문 카드.
- 제목에 "연결"이 들어간 불릿은 맨 아래 **국내외 연결 고리** 인디고 박스로 렌더.

## 9. Companies / Threads / Sources

```markdown
## 🚀 Companies to Watch

> 주목할 기업을 정보로 정리했습니다. 투자 참고용이며, 판단은 본인의 몫입니다.

- **{기업 — 관전 포인트}**: {본문} (본문에 [링크](URL)가 있으면 하단 출처로 표시)

## Threads to Follow

- [[topics/거시정책]] — {한 줄 추적 포인트}

## Sources

**거시·정책**
- [이름](URL) | [이름](URL)
**AI·기술**
- [이름](URL)
**바이오·제약**
- [이름](URL)
```

- Companies: 불릿 1개 = 카드 1개(배지 키워드 추론).
- Threads: `- [[topics/…]] — 텍스트`. 위키링크가 배지, 텍스트가 내용.
- Sources: `**카테고리**` 줄 + 그 아래 `- [이름](URL) | …` 링크들. 카테고리당 한 열(3열 그리드).

---

## 10. 배지 매핑(고정)

위키링크(`[[topics/…]]`) → 배지:

| 위키링크 | 배지 |
| --- | --- |
| 거시정책 | Macro |
| AI | AI |
| 반도체 | Semiconductor |
| 바이오제약 | Bio |
| 신약개발전략 | Bio |
| 유망기업 | Market |

위키링크가 없는 섹션(Topic·Demand·Investment·Companies)은 제목+본문 **키워드**로 추론한다
(우선순위: mRNA → ADC → K-Bio → Semiconductor/HBM → Bio → AI → Macro → Market, 기본값 Market).
세부 태그(mRNA·K-Bio·ADC 등)를 카드에 정확히 고정하려면 위키링크/키워드를 그에 맞게 쓰면 된다.

## 11. 인라인 표기 규칙

- 링크는 `[표시 텍스트](URL)` 표준 마크다운. URL의 `&`는 그대로 둔다(이스케이프하지 않음).
- 강조는 `**굵게**`만 인라인 변환된다(기울임 `*…*`는 Business English 예문에서만 특별 처리).
- `[[topics/…]]` 위키링크는 화면 텍스트에서 제거되고 배지/스레드에만 쓰인다.

## 12. 실행

```bash
python3 scripts/render_html.py 2026-06-11                 # 정식 산출(html/·push/ 덮어씀)
python3 scripts/render_html.py 2026-06-11 --out-suffix .test   # 2026-06-11.test.html 로 안전 출력
```

- 입력 md 없음 → 비0 종료. 필수 섹션 전무 → 비0 종료. 섹션 누락 → 생략 + stderr 경고.
