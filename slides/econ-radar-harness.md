---
marp: true
theme: default
paginate: true
size: 16:9
header: 'econ-radar · 뉴스레터 하네스 구조'
footer: '2026-06-12 · 스터디 발표'
style: |
  :root {
    --ink: #1e293b;
    --indigo: #4338ca;
    --indigo-deep: #3730a3;
    --indigo-soft: #eef2ff;
    --line: #c7d2fe;
    --muted: #64748b;
  }
  section {
    background: linear-gradient(160deg, #ffffff 0%, #f6f7ff 100%);
    color: var(--ink);
    font-family: "Pretendard", "Apple SD Gothic Neo", "Noto Sans KR", -apple-system, system-ui, sans-serif;
    font-size: 25px;
    line-height: 1.6;
    padding: 60px 70px;
  }
  h1 { color: var(--indigo-deep); font-weight: 800; letter-spacing: -0.02em; }
  h2 {
    color: var(--indigo);
    font-weight: 700;
    letter-spacing: -0.01em;
    border-bottom: 3px solid var(--line);
    padding-bottom: 10px;
    margin-bottom: 22px;
  }
  strong { color: var(--indigo); font-weight: 700; }
  em { color: var(--muted); font-style: normal; }
  ul { margin-top: 6px; }
  li { margin: 9px 0; }
  li::marker { color: var(--indigo); }
  code {
    background: var(--indigo-soft);
    color: var(--indigo-deep);
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.88em;
  }
  pre {
    background: #0f172a;
    color: #e2e8f0;
    border-radius: 14px;
    padding: 22px 26px;
    font-size: 19px;
    line-height: 1.5;
    box-shadow: 0 10px 30px rgba(15,23,42,0.18);
  }
  pre code { background: transparent; color: inherit; padding: 0; }
  table {
    font-size: 21px;
    border-collapse: separate;
    border-spacing: 0;
    width: 100%;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 18px rgba(67,56,202,0.10);
  }
  th {
    background: var(--indigo);
    color: #fff;
    font-weight: 700;
    padding: 12px 16px;
    text-align: left;
  }
  td { background: #fff; padding: 11px 16px; border-bottom: 1px solid #eef0f7; }
  tr:nth-child(even) td { background: #fafbff; }
  blockquote {
    border-left: 5px solid var(--indigo);
    background: var(--indigo-soft);
    margin: 18px 0 0;
    padding: 14px 22px;
    border-radius: 0 12px 12px 0;
    color: var(--indigo-deep);
    font-size: 22px;
  }
  blockquote::before { content: none; }
  header { color: #94a3b8; font-size: 15px; font-weight: 600; }
  footer { color: #94a3b8; font-size: 14px; }
  section::after {
    color: var(--indigo);
    font-weight: 700;
    text-shadow: none;
  }
  .small { font-size: 19px; color: var(--muted); }

  /* 표지·마무리 슬라이드 */
  section.lead {
    background: radial-gradient(120% 120% at 0% 0%, #4f46e5 0%, #4338ca 45%, #312e81 100%);
    color: #eef2ff;
    text-align: center;
    justify-content: center;
  }
  section.lead h1 { color: #fff; font-size: 64px; margin-bottom: 6px; }
  section.lead h2 {
    color: #c7d2fe;
    border: none;
    font-weight: 600;
    font-size: 30px;
    margin: 0 0 30px;
  }
  section.lead strong { color: #fff; }
  section.lead .small { color: #c7d2fe; }
  section.lead::after { color: #c7d2fe; }
  section.lead header, section.lead footer { color: rgba(199,210,254,0.55); }
---

<!-- _class: lead -->

# econ-radar
## 뉴스레터를 "매일 도는 팀"으로 만든 하네스

경제 뉴스를 매일 **3렌즈**로 정리하고
그 누적을 **리포트 → 블로그 → 책**으로 키우는
개인 지식 자산 시스템

<span class="small">스터디 발표 · 2026-06-12</span>

---

## 한 장 요약

- **문제**: 좋은 경제 뉴스 정리를 "매일, 같은 품질로" 하기 어렵다 — 사람이 지친다.
- **해법**: 일을 **에이전트 팀 + 작업 매뉴얼(스킬)** 로 쪼개 매일 자동으로 돌린다.
- **차별점**: 단발 요약이 아니라 **누적**한다 — vault(옵시디언)에 쌓아 동향·블로그·책으로 자란다.
- **운영**: 매일 **18:30 KST 클라우드가 자동 생성**, 발행만 사람이 승인.

> 핵심 아이디어: *"프롬프트 한 번"이 아니라 "역할·매뉴얼·검수·누적이 있는 작은 조직"을 설계한다.*

---

## 3층 구조 — 오늘이 쌓여 책이 된다

| 층 | 무엇 | 산출물 |
| --- | --- | --- |
| **1층 (매일)** | 수집→분석→편집→검수→렌더 | 일일 뉴스레터·HTML·푸시 |
| **2층 (자산)** | 옵시디언 vault에 누적 | 태그·`[[링크]]`·주제 MOC |
| **3층 (저술)** | 누적에서 패턴 추출 | 동향 리포트·블로그·책 챕터 |

<br>

- 1층은 **매일 돌고**, 2층은 **연결**하고, 3층은 **가끔 끌어올린다**.
- 위로 갈수록 자동화↓ 사람 판단↑.

---

## 3렌즈 — 무엇을 보는가

뉴스를 항상 같은 세 각도로 분해한다.

1. **산업구조 (Industry)** — 누가 움직였나, 밸류체인 어디가 바뀌나
2. **투자 (Investment)** — 테마·종목·리스크·기회 *(코스피 + 해외)*
3. **시장 (Market)** — 유망 기업(파는 쪽) + **수요/Demand**(사는 쪽)

<br>

<span class="small">전 분야를 다루되 <strong>제약·바이오·AI</strong>에 비중. 매수·매도 권유가 아니라 정보·시나리오·리스크로.</span>

---

## 1층 파이프라인 — 7명의 팀

```
news-scout            (수집·번역)
      │
      ▼
market-analyst  ∥  company-scout      ← 병렬 (산업·투자  /  유망기업·수요)
      │
      ▼
newsletter-editor     (한 편으로 통합)
      │
      ▼
style-critic          (문체 검수 — AI 상투구 제거)   ← 발행 전 게이트
      │
      ▼
report-renderer       (HTML·푸시)   +   knowledge-curator (vault 정리)
```

각자 **역할(agent)** 이 있고, **작업 매뉴얼(skill)** 을 보고 일하며, **파일**로 결과를 남긴다.

---

## 설계의 핵심 4가지

- **역할 분리** — 수집가는 해석 안 하고, 분석가는 사실만 받고, 비평가는 표현만 고친다. 책임이 겹치지 않는다.
- **매뉴얼화(skill)** — "어떻게 잘하나"를 사람 머리가 아니라 `SKILL.md`에 적어둔다 → 매일 같은 품질.
- **검수 게이트** — `style-critic`이 발행 전에 반드시 한 번 윤문. 사실·수치·링크는 건드리지 않고 문체만.
- **누적 우선** — 끝나면 `knowledge-curator`가 `[[링크]]`·태그·주제 MOC로 엮어 **자산으로 적립**.

---

## 자연어로 부른다 — 스킬명을 몰라도 됨

| 이렇게 말하면 | 이게 돈다 |
| --- | --- |
| "오늘 뉴스 정리해줘", "econ-radar 돌려줘" | `daily-econ-news-orchestrator` (1층 전체) |
| "투자 파트만 다시", "HTML만 다시" | 해당 단계만 부분 재실행 |
| "이번 주 동향 리포트", "이 주제로 블로그" | `content-studio-orchestrator` (3층) |

<br>

오케스트레이터(팀장)가 **진행표**를 들고 단계·의존관계를 챙긴다.

---

## 품질을 어떻게 지키나

- **문체 기준선** — `korean-style-samples.md`(실제 기사 표본)를 의무 참조. *"A가 아니라 B", "~인 셈"* 같은 AI 상투구 금지.
- **깊이 기준선** — `benchmarks.md`(본받을 매체) 체크리스트: Why it matters 한 줄 · 1차 자료 직접 링크 · 양면 시각.
- **수요 렌즈** — `demand-lens.md`: 투자자=공급·자본 ↔ Demand=수요(제약은 환자·처방의·지불자).
- **2층 글쓰기** — 한눈에(TL;DR) + 더 깊이 보기(심층), 모든 항목 원문 링크.

> 기준선을 **파일로** 둔 게 핵심 — 에이전트가 매번 같은 잣대를 본다.

---

## 자동화 — 매일 18:30 KST, 클라우드가 알아서

- **클라우드 routine**(cron)이 PC가 꺼져 있어도 파이프라인 전체를 돌린다.
- 결과를 **GitHub(origin/main)에 커밋·푸시** → 로컬은 `git pull`로 받아본다.
- **승인형**: 파일 생성까지만 자동, **외부 발행(블로그·메일)은 항상 사람 승인 뒤**.

<br>

<span class="small">중복 회피: <code>recent-headlines.md</code>를 기준선으로 이미 다룬 뉴스는 다시 헤드라인으로 안 올린다.</span>

---

## 안전선 — 하지 않는 것

- **외부 자동 발송 금지** — 메일·메신저·블로그·출판은 사람 승인 뒤에만.
- **매수·매도 권유 금지** — 투자·유망기업은 정보·시나리오·리스크로만.
- **출처 없는 수치 생성 금지** — 추정은 "추정"으로 명시, 1차 자료 재확인.

> 자동화의 신뢰는 *"무엇을 자동으로 하느냐"* 보다 *"무엇을 자동으로 안 하느냐"* 에서 온다.

---

## 하네스로 배운 점 (스터디 토의용)

- **일을 조직으로 본다** — 프롬프트 한 방이 아니라 역할·매뉴얼·검수·누적의 작은 팀.
- **지식은 파일에** — 기준선·표본·dedup을 파일로 두면 품질이 사람에게 안 묶인다.
- **누적이 복리** — 매일의 단편이 vault에서 연결되며 동향·책의 원료가 된다.
- **사람은 게이트에** — 자동화는 생성까지, 판단·발행은 사람이.

<br>

<span class="small">→ 토의: 여러분의 반복 업무 중 이렇게 "팀 + 매뉴얼"로 쪼갤 수 있는 건?</span>

---

<!-- _class: lead -->

# 감사합니다

**econ-radar** = 매일 도는 3렌즈 뉴스 팀 + 누적되는 지식 자산

<span class="small">데모: 오늘자 HTML 리포트 · vault 그래프</span>
