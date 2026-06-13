---
marp: true
theme: default
paginate: true
size: 16:9
header: 'econ-radar · 뉴스레터 하네스 구조'
footer: '2026-06-13 · 스터디 발표'
style: |
  :root {
    --ink: #1e293b;
    --indigo: #4338ca;
    --indigo-deep: #3730a3;
    --indigo-soft: #eef2ff;
    --line: #c7d2fe;
    --muted: #64748b;
    --pop: #c026d3;
    --pop-soft: #fae8ff;
    --amber: #b45309;
    --amber-soft: #fef3c7;
    --teal: #0f766e;
    --teal-soft: #ccfbf1;
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
    padding-bottom: 12px;
    margin-bottom: 24px;
    background: linear-gradient(90deg, var(--indigo) 0, var(--pop) 56px, var(--line) 56px) bottom left / 100% 4px no-repeat;
  }
  strong { color: var(--indigo); font-weight: 700; }
  em { color: var(--muted); font-style: normal; }
  ul { margin-top: 6px; }
  li { margin: 9px 0; }
  li::marker { color: var(--pop); }
  code {
    background: var(--indigo-soft);
    color: var(--indigo-deep);
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.88em;
  }
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
    background: linear-gradient(90deg, var(--indigo) 0%, #6d28d9 100%);
    color: #fff;
    font-weight: 700;
    padding: 12px 16px;
    text-align: left;
  }
  td { background: #fff; padding: 11px 16px; border-bottom: 1px solid #eef0f7; }
  tr:nth-child(even) td { background: #fafbff; }
  blockquote {
    border-left: 5px solid var(--pop);
    background: linear-gradient(90deg, var(--pop-soft) 0%, var(--indigo-soft) 100%);
    margin: 18px 0 0;
    padding: 14px 22px;
    border-radius: 0 12px 12px 0;
    color: var(--indigo-deep);
    font-size: 22px;
  }
  blockquote::before { content: none; }
  header { color: #94a3b8; font-size: 15px; font-weight: 600; }
  footer { color: #94a3b8; font-size: 14px; }
  section::after { color: var(--indigo); font-weight: 700; text-shadow: none; }
  .small { font-size: 19px; color: var(--muted); }
  a { color: var(--indigo); }

  /* 배지 */
  .tag {
    display: inline-block;
    font-size: 15px; font-weight: 700;
    padding: 2px 12px; border-radius: 999px;
    vertical-align: 2px; margin-left: 8px;
  }
  .tag.new { background: var(--pop-soft); color: var(--pop); }
  .tag.auto { background: var(--teal-soft); color: var(--teal); }

  /* 파이프라인 플로우 */
  .flow { display: flex; flex-direction: column; align-items: center; gap: 4px; margin-top: 6px; }
  .frow { display: flex; gap: 14px; justify-content: center; }
  .node {
    background: #fff; border: 2px solid var(--line); border-radius: 12px;
    padding: 7px 20px; font-size: 19.5px; font-weight: 700; color: var(--indigo-deep);
    box-shadow: 0 3px 12px rgba(67,56,202,0.08); text-align: center; line-height: 1.35;
  }
  .node .role { display: block; font-size: 14.5px; font-weight: 500; color: var(--muted); }
  .node.gate { border-color: var(--amber); background: #fffbeb; color: var(--amber); }
  .node.script { border-color: var(--teal); background: #f0fdfa; color: var(--teal); }
  .arr { color: var(--pop); font-size: 15px; line-height: 1; }

  /* 타임라인 */
  .tl { list-style: none; padding-left: 0; margin-top: 4px; }
  .tl li { margin: 12px 0; padding-left: 26px; position: relative; }
  .tl li::before {
    content: ""; position: absolute; left: 4px; top: 12px;
    width: 11px; height: 11px; border-radius: 50%;
    background: linear-gradient(135deg, var(--indigo) 0%, var(--pop) 100%);
    box-shadow: 0 0 0 4px var(--indigo-soft);
  }
  .tl .d { font-weight: 800; color: var(--indigo-deep); margin-right: 8px; }

  /* 브라우저 목업 프레임 */
  .browser {
    background: #fff; border-radius: 14px; overflow: hidden;
    box-shadow: 0 18px 50px rgba(49,46,129,0.28), 0 2px 8px rgba(49,46,129,0.12);
    border: 1px solid #e2e8f0;
  }
  .browser .bar {
    display: flex; align-items: center; gap: 8px;
    background: #f1f5f9; padding: 9px 14px; border-bottom: 1px solid #e2e8f0;
  }
  .browser .dot { width: 11px; height: 11px; border-radius: 50%; }
  .browser .dot.r { background: #f87171; } .browser .dot.y { background: #fbbf24; } .browser .dot.g { background: #34d399; }
  .browser .url {
    flex: 1; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;
    font-size: 13.5px; color: var(--muted); padding: 2px 12px; line-height: 1.6;
    font-family: ui-monospace, "SF Mono", monospace;
  }
  .browser img { display: block; width: 100%; margin: 0; }
  .shots { display: flex; gap: 26px; align-items: flex-start; }
  .shots .browser { flex: 1; min-width: 0; }
  .clickme { text-align: center; font-size: 17px; color: var(--pop); font-weight: 700; margin-top: 12px; }

  /* 막대 차트 */
  .bars { margin-top: 10px; }
  .brow { display: flex; align-items: center; gap: 14px; margin: 9px 0; }
  .brow .lbl { width: 270px; font-size: 19.5px; font-weight: 600; text-align: right; color: var(--ink); }
  .brow .track { flex: 1; }
  .brow .bar1 {
    height: 24px; border-radius: 6px;
    background: linear-gradient(90deg, var(--indigo) 0%, #7c3aed 100%);
    color: #fff; font-size: 15.5px; font-weight: 700;
    display: flex; align-items: center; justify-content: flex-end; padding-right: 10px;
  }
  .brow .bar1.dead { background: #e2e8f0; color: var(--muted); text-decoration: line-through; }
  .brow .bar1.zero { background: var(--teal); width: 56px !important; text-decoration: none; }

  /* 표지·마무리 */
  section.lead {
    background:
      radial-gradient(90% 120% at 100% 0%, rgba(192,38,211,0.35) 0%, rgba(192,38,211,0) 55%),
      radial-gradient(120% 120% at 0% 0%, #4f46e5 0%, #4338ca 45%, #1e1b4b 100%);
    color: #eef2ff;
    text-align: center;
    justify-content: center;
  }
  section.lead h1 {
    font-size: 64px; margin-bottom: 6px;
    background: linear-gradient(90deg, #ffffff 30%, #e9d5ff 70%, #f0abfc 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
  }
  section.lead h2 {
    color: #c7d2fe; background: none; border: none;
    font-weight: 600; font-size: 30px; margin: 0 0 26px; padding-bottom: 0;
  }
  section.lead strong { color: #fff; }
  section.lead .small { color: #c7d2fe; }
  section.lead::after { color: #c7d2fe; }
  section.lead header, section.lead footer { color: rgba(199,210,254,0.55); }
  section.lead img.hero {
    width: 460px; border-radius: 18px; margin: 0 auto 26px;
    box-shadow: 0 24px 60px rgba(0,0,0,0.45), 0 0 0 1px rgba(255,255,255,0.14);
  }
  section.lead img.qr {
    width: 132px; border-radius: 12px; margin: 18px auto 0;
    box-shadow: 0 8px 24px rgba(0,0,0,0.35);
  }
---

<!-- _class: lead -->

<img class="hero" src="assets/cover.png" alt="econ-radar">

# econ-radar
## 뉴스레터를 "매일 도는 팀"으로 만든 하네스

경제 뉴스를 매일 **3렌즈**로 정리해 **자동 발행**하고, 그 누적을 **리포트 → 블로그 → 책**으로 키우는 개인 지식 자산 시스템

<span class="small">스터디 발표 · 2026-06-13 (v3)</span>

---

## 한 장 요약

- **문제**: 좋은 경제 뉴스 정리를 "매일, 같은 품질로" 하기 어렵다 — 사람이 지친다.
- **해법**: 일을 **에이전트 팀 + 작업 매뉴얼(스킬)** 로 쪼개 매일 자동으로 돌린다.
- **차별점**: 단발 요약이 아니라 **누적**한다 — vault(옵시디언)에 쌓아 동향·블로그·책으로 자란다.
- **운영**: 매일 **18:30 KST 클라우드가 생성→블로그 발행→텔레그램 알림까지 완전 자동**. 사람 승인 대신 **사실 검증(fact-check) 게이트**가 지킨다.

> 핵심 아이디어: *"프롬프트 한 번"이 아니라 "역할·매뉴얼·검수·누적이 있는 작은 조직"을 설계한다.*

---

## 실제 발행본 — 매일 저녁 이렇게 나온다

<a href="https://kakyungkim.github.io/econ-radar/2026-06-12.html">
<div class="browser" style="width: 62%; margin: 0 auto;">
  <div class="bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">kakyungkim.github.io/econ-radar/2026-06-12.html</span></div>
  <img src="assets/shot-issue.png" alt="econ-radar 2026-06-12 발행본">
</div>
</a>

<p class="clickme">▲ 클릭하면 라이브 페이지로 이동</p>

---

## 3층 구조 — 오늘이 쌓여 책이 된다

| 층 | 무엇 | 산출물 | 자동화 |
| --- | --- | --- | --- |
| **1층 (매일)** | 수집→분석→편집→검수→검증→렌더 | 일일 뉴스레터·HTML·푸시 | 매일 18:30 자동 |
| **2층 (자산)** | 옵시디언 vault에 누적 | 태그·`[[링크]]`·주제 MOC | 큐레이션 자동 |
| **3층 (저술)** | 누적에서 패턴 추출 | 동향 리포트·블로그·책 | **주간 리포트 자동** |

<br>

- 1층은 **매일 돌고**, 2층은 **연결**하고, 3층은 **매주 일요일 끌어올린다**.
- 위로 갈수록 기계가 만드는 건 초안까지 — 최종 판단·발행은 사람.

---

## 3렌즈 — 무엇을 보는가

뉴스를 항상 같은 세 각도로 분해한다.

1. **산업구조 (Industry)** — 누가 움직였나, 밸류체인 어디가 바뀌나
2. **투자 (Investment)** — 테마·종목·리스크·기회 *(코스피 + 해외)*
3. **시장 (Market)** — 유망 기업(파는 쪽) + **수요/Demand**(사는 쪽)

<br>

<span class="small">전 분야를 다루되 <strong>제약·바이오·AI</strong>에 비중. 제약의 수요는 셋으로 쪼갠다: 환자·처방의·지불자. 매수·매도 권유가 아니라 정보·시나리오·리스크로.</span>

---

## 1층 파이프라인 — 8명의 팀

<div class="flow">
  <div class="node">news-scout <span class="role">수집·번역 — 해석 없이 사실만</span></div>
  <div class="arr">▼</div>
  <div class="frow">
    <div class="node">market-analyst <span class="role">산업·투자·수요</span></div>
    <div class="node">company-scout <span class="role">유망 기업·수요</span></div>
  </div>
  <div class="arr">▼ <span style="font-size:13px">(병렬)</span></div>
  <div class="node">newsletter-editor <span class="role">한 편으로 통합 — md 계약 준수</span></div>
  <div class="arr">▼</div>
  <div class="frow">
    <div class="node gate">style-critic <span class="role">문체 게이트 — AI 상투구 제거</span></div>
    <div class="node gate">fact-checker <span class="role">사실 게이트 — 수치 원문 대조 ✦new</span></div>
  </div>
  <div class="arr">▼</div>
  <div class="frow">
    <div class="node script">render_html.py <span class="role">결정적 스크립트 렌더 ✦new</span></div>
    <div class="node">knowledge-curator <span class="role">vault 누적·MOC</span></div>
  </div>
</div>

---

## 설계의 핵심 4가지

- **역할 분리** — 수집가는 해석 안 하고, 분석가는 사실만 받고, 비평가는 표현만 고친다. 책임이 겹치지 않는다.
- **매뉴얼화(skill)** — "어떻게 잘하나"를 사람 머리가 아니라 `SKILL.md`에 적어둔다 → 매일 같은 품질.
- **이중 게이트** — 발행 전 `style-critic`(문체)과 `fact-checker`(사실)가 각각 한 번씩. 문체 게이트는 표현만, 사실 게이트는 수치·출처만 본다.
- **판단만 LLM에** — HTML 렌더처럼 판단이 필요 없는 단계는 **스크립트로 고정**(토큰 절감 + 양식 드리프트 차단). 누적은 `knowledge-curator`가 `[[링크]]`·MOC로 적립.

---

## 품질을 어떻게 지키나 — 기준선은 전부 파일

- **문체 기준선** — `korean-style-samples.md`(실제 기사 표본) 의무 참조. *"A가 아니라 B", "~인 셈"* 같은 AI 상투구 금지.
- **사실 기준선** <span class="tag new">NEW</span> — `fact-checker`가 핵심 수치 최대 10개를 원문과 대조. 출처 없는 수치 차단, 단일 소스 표기, 1차 출처(IR·규제기관) 승격.
- **깊이 기준선** — `benchmarks.md`: Why it matters 한 줄 · 1차 자료 직접 링크 · 양면 시각.
- **수요 렌즈** — `demand-lens.md`: 투자자=공급·자본 ↔ Demand=수요.
- **양식 기준선** <span class="tag new">NEW</span> — `NEWSLETTER-FORMAT.md` 계약 + 템플릿 렌더 → 양식이 드리프트하지 않는다.

> 기준선을 **파일로** 둔 게 핵심 — 에이전트가 매번 같은 잣대를 본다.

---

## 자동화 — 두 개의 클라우드 루틴

| 루틴 | 언제 | 하는 일 |
| --- | --- | --- |
| **데일리** <span class="tag auto">완전 자동</span> | 매일 18:30 KST | 수집→분석→편집→검수→검증→렌더→큐레이션→**블로그 발행→텔레그램 알림** |
| **주간 동향** <span class="tag new">NEW</span> | 일요일 21:00 KST | 한 주치에서 패턴 추출 → `reports/` 동향 리포트(3층) |

<br>

- 처음엔 발행 전 사람 승인이었지만 **이틀 만에 폐기** — 게이트를 지키는 사람이 매일 있어야 했다. "확인 전까지 안 나간다" → **"나가되, 이상하면 내린다"**.
- 알림이 안 오는 날 = 뭔가 고장난 날 → 텔레그램이 자연스러운 모니터링.
- vault 전체가 git 추적(private) → 클라우드가 과거를 읽고 멀티위크 흐름을 잇는다.

---

## 5일간의 진화 — 운영이 설계를 고친다

<ul class="tl">
<li><span class="d">6/09</span>하네스 구축, 첫 발행. 깊이 부족 피드백 → 항목 수·Why it matters 규칙화</li>
<li><span class="d">6/10</span>"문체가 AI 같다" → 실제 기사 표본 도입 + style-critic 게이트. 렌즈 교체(커리어→유망기업)</li>
<li><span class="d">6/11</span>"투자자 관점에 치우쳤다"(스터디 피드백) → <strong>수요(Demand) 렌즈</strong> 추가. 클라우드 루틴 가동</li>
<li><span class="d">6/12</span>승인 게이트 폐기 → <strong>완전 자동 발행</strong> + 텔레그램 채널</li>
<li><span class="d">6/13</span>구조 검토 → <strong>4건 일괄 개선</strong>: 사실 게이트·vault 전체 추적·렌더 스크립트화·주간 3층 루틴</li>
</ul>

> 패턴: *감각적 불만("어색하다", "치우쳤다")을 → 파일로 된 규칙·게이트로 변환한다.*

---

## 6/13 구조 검토 — 비판이 곧 백로그

발행 4호 시점에 하네스를 스스로 비판 검토 → 우선순위 4건 즉시 적용.

| 발견한 문제 | 처방 |
| --- | --- |
| 게이트가 문체뿐 — 잘못된 수치가 그대로 발행됨 | `fact-checker` 신설 (T4.7) |
| 3층(저술)이 비어 있음 — forcing function 부재 | 주간 동향 루틴 (일 21:00) |
| 클라우드가 과거를 못 봄 (vault 로컬 전용) | 레포 private + vault 전체 추적 |
| 렌더가 최대 비용(93K 토큰)인데 판단 불필요 | `render_html.py` 스크립트화 |

<span class="small">미적용분(MOC 요약 구조·백로그 트리아지)은 TODO로 — 검토 전문: <code>vault/_meta/2026-06-13-harness-review.md</code></span>

---

## 운영 비용 — 계측해야 고친다

1회 발행 ≈ **43만 토큰 / 벽시계 ~25분** (`run-metrics.md`에 단계별 누적)

<div class="bars">
  <div class="brow"><span class="lbl">렌더 report-renderer</span><div class="track"><div class="bar1 dead" style="width:100%">93K — 가장 비쌌던 단계</div></div></div>
  <div class="brow"><span class="lbl">→ render_html.py</span><div class="track"><div class="bar1 zero">≈0</div></div></div>
  <div class="brow"><span class="lbl">통합 editor</span><div class="track"><div class="bar1" style="width:84%">78K</div></div></div>
  <div class="brow"><span class="lbl">수집 news-scout</span><div class="track"><div class="bar1" style="width:67%">62K</div></div></div>
  <div class="brow"><span class="lbl">큐레이션 curator</span><div class="track"><div class="bar1" style="width:61%">57K</div></div></div>
  <div class="brow"><span class="lbl">문체 검수 style-critic</span><div class="track"><div class="bar1" style="width:55%">51K</div></div></div>
  <div class="brow"><span class="lbl">분석 2종 (병렬)</span><div class="track"><div class="bar1" style="width:94%">87K</div></div></div>
</div>

<br>

<span class="small">가장 비싼 단계가 가장 판단이 필요 없는 단계였다 → 스크립트로 대체해 <strong>발행당 ~22% 절감</strong>.</span>

---

## 안전선 — 하지 않는 것

- **자동 발행은 데일리 한정** — 블로그 발행+텔레그램 알림만 승인된 자동 동작. 메일·메신저 대량 전송·출판은 여전히 사람 승인 뒤에만.
- **매수·매도 권유 금지** — 투자·유망기업은 정보·시나리오·리스크로만.
- **출처 없는 수치 생성 금지** — fact-checker가 출처 없는 수치를 발행 전에 차단. 추정은 "추정"으로 명시.

> 자동화의 신뢰는 *"무엇을 자동으로 하느냐"* 보다 *"무엇을 자동으로 안 하느냐"* 에서 온다.

---

## 하네스로 배운 점 (스터디 토의용)

- **일을 조직으로 본다** — 프롬프트 한 방이 아니라 역할·매뉴얼·검수·누적의 작은 팀.
- **지식은 파일에** — 기준선·표본·계약을 파일로 두면 품질이 사람에게 안 묶인다.
- **게이트는 실패 모드별로** — 문체 게이트는 어색함을, 사실 게이트는 오류를 막는다. 자동 발행일수록 사실 게이트가 먼저다.
- **판단과 기계 작업을 가른다** — 판단 없는 단계(렌더)는 스크립트로, 판단 단계만 LLM으로.
- **운영이 설계를 고친다** — 5일간 매일 구조가 바뀌었다. 전부 운영 중 불만에서 출발했다.

<br>

<span class="small">→ 토의: 여러분의 반복 업무에서 "판단이 필요한 단계"와 "기계로 굳힐 단계"는 어디서 갈리나?</span>

---

## 직접 보기 — 아카이브 · 설계 노트

<div class="shots">
  <a style="flex:1; min-width:0;" href="https://kakyungkim.github.io/econ-radar/">
  <div class="browser">
    <div class="bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">kakyungkim.github.io/econ-radar/</span></div>
    <img src="assets/shot-archive.png" alt="econ-radar 아카이브">
  </div>
  </a>
  <a style="flex:1; min-width:0;" href="https://kakyungkim.github.io/kr/2026/06/10/econ-radar-agent-harness/">
  <div class="browser">
    <div class="bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">…/econ-radar-agent-harness/ (설계 노트 블로그)</span></div>
    <img src="assets/shot-blog.png" alt="설계 노트 블로그 글">
  </div>
  </a>
</div>

<p class="clickme">▲ 클릭하면 각 페이지로 이동</p>

---

<!-- _class: lead -->

# 감사합니다

**econ-radar** = 매일 도는 3렌즈 뉴스 팀 + 이중 게이트 + 누적되는 지식 자산

<a href="https://kakyungkim.github.io/econ-radar/"><img class="qr" src="assets/qr-archive.png" alt="QR — econ-radar 아카이브"></a>

<span class="small">QR = 아카이브 · 텔레그램 @econradar · 데모: 오늘자 HTML 리포트</span>
