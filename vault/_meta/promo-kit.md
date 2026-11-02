---
type: meta
tags: [홍보, 운영]
timestamp: 2026-06-13T11:44:33+09:00
publish: false
---
# 홍보 키트 (promo-kit)

econ-radar 채널·블로그 홍보용 문안 모음. 외부 게시는 사람이 직접(승인 후).

## 1. 링크드인 게시 (영어 티저 본문 + 첫 댓글에 링크)
> 링크드인은 본문에 외부 링크가 있으면 도달이 떨어진다. **본문엔 링크를 넣지 말고, 게시 직후 첫 댓글에 링크를 단다.**

### 본문 (영어)
```
I gave up reading the economic news every day. Then I built a team of AI agents to do it for me.

Not one clever prompt — a small org with separated roles:
• a scout that gathers and translates the news (facts only)
• analysts that read it through three angles — industry, investing, market
• a style critic and a fact-checker as two gates before anything publishes
• a renderer and a curator that file each day into a knowledge vault

It runs itself every evening, publishes to a blog, and pings a Telegram channel — no human in the loop except for judgment.

Five days in, the most interesting part wasn't the automation. It was watching every vague complaint ("this reads like AI", "you're too focused on investors") turn into a concrete rule or a new gate the next day. Operating it kept redesigning it.

I wrote up the design notes — link in the comments.

#AIagents #ClaudeCode #BuildingInPublic #Bioinformatics #Automation
```

### 첫 댓글 (링크)
```
설계 노트 (한국어): https://kakyungkim.github.io/kr/2026/06/10/econ-radar-agent-harness/
Design notes (English): https://kakyungkim.github.io/en/2026/06/10/econ-radar-agent-harness/
매일 받아보기 (Telegram): https://t.me/econradar
```

### 한국어 버전 (국내 청중용, 택일)
```
경제 뉴스를 매일 읽으려다 포기했습니다. 대신 AI 에이전트 팀을 만들었어요.

똑똑한 프롬프트 하나가 아니라, 역할을 나눈 작은 조직입니다.
• 수집가는 뉴스를 모으고 번역합니다(해석 없이 사실만)
• 분석가들은 산업·투자·시장 세 관점으로 읽습니다
• 발행 전 문체 검수 + 사실 검증 두 게이트를 통과합니다
• 렌더·큐레이션이 매일을 지식 자산으로 쌓습니다

매일 저녁 알아서 돌고, 블로그에 발행하고, 텔레그램으로 보냅니다. 사람은 판단만 합니다.

닷새 운영하며 가장 흥미로웠던 건 자동화 자체가 아니라, "AI 같다", "투자자 입장에 치우쳤다" 같은 막연한 불만이 다음 날 구체적인 규칙·게이트로 바뀌는 과정이었습니다.

설계 노트는 첫 댓글에 링크를 답니다.
```

## 2. 텔레그램 토론(댓글) 기능 — 미리 준비
**봇 API로는 채널↔토론그룹 연결을 할 수 없다.** 채널 설정에서 사람이 직접 그룹을 연결해야 댓글이 켜진다. 아래는 켤 때 그대로 쓸 준비물.

### 켜는 절차 (텔레그램 앱, 데스크톱/모바일)
1. 토론용 **그룹 먼저 생성**(예: "econ-radar 토론"). 비공개로 만들어도 채널 연결 시 공개 노출됨.
2. 채널 @econradar → 채널명 탭 → **Edit(연필)** → **Discussion** → 방금 만든 그룹 선택 → 연결.
3. 연결되면 채널 글마다 자동으로 "💬 Leave a comment" 가 붙는다. 봇(@kkkim_agent_bot)을 그룹 관리자로 추가하면 모더레이션 자동화도 가능.

### 토론 그룹 준비물 (생성 시 붙여넣기)
- **그룹 이름**: `econ-radar 토론`
- **그룹 설명**: `econ-radar 발행본에 대한 의견·질문·토론 공간입니다. 투자 권유 금지, 출처 있는 이야기 환영.`
- **고정 규칙 메시지**:
```
여기는 econ-radar 댓글·토론방입니다 💬

• 발행본에 대한 의견·반론·추가 정보 환영합니다.
• 특정 종목 매수·매도 권유는 삼가주세요(정보·시나리오 공유는 OK).
• 수치·주장은 가능하면 출처와 함께.
• 서로 존중하며, 광고·스팸은 삭제됩니다.

오늘의 발행본: https://kakyungkim.github.io/econ-radar/
```

### 권장 타이밍
- 구독자가 어느 정도 모이기 전엔 일방향(채널만)이 깔끔. **댓글이 붙기 시작할 만큼 사람이 모이면** 그때 연결. 빈 토론방은 오히려 휑해 보인다.
