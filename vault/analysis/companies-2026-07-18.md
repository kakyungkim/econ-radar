---
date: 2026-07-18
type: analysis
analyst: company-scout
lens: company
tags: [AI, 반도체, 제약바이오, 유전자세포치료, ADHD신약, MoE모델, HBM, 한국바이오]
links: ["[[topics/AI인프라]]", "[[topics/반도체AI인프라]]", "[[topics/바이오제약]]", "[[topics/한국제약바이오]]"]
---

# 유망 기업·주목 플레이어 — 2026-07-18

> 오늘 5선: Moonshot AI(Kimi K3·EDA 충격) / SK하이닉스(Q2 D-4·HBM 독주) / Otsuka(centanafadine PDUFA D-6) / 코오롱티슈진(TG-C 결과 임박) / Google·Alphabet(Gemini 3차 지연·구조적 균열)

---

## 1. Moonshot AI — DeepSeek 충격의 재연, EDA 해자(moat)까지 흔들다 (AI·중국)

- **무슨 일**: 중국 베이징 AI 스타트업 Moonshot AI가 2026년 7월 17일 Kimi K3를 공개했다. 혼합전문가(MoE·Mixture-of-Experts) 구조에 총 파라미터 2.8조 개, 1M 토큰 컨텍스트 창을 갖춘 역대 최대 오픈웨이트 모델이다. 코드 벤치마크(Frontend Code Arena)에서 1,679점으로 Claude Fable 5(1,631점)를 상회하는 1위를 기록했다. API 가격은 입력 $3·출력 $15(1M 토큰 기준)로 GPT-5.6 대비 낮은 수준이다. 전체 가중치 공개는 2026년 7월 27일 예정이다. 별도 공개한 시연에서 전자설계자동화(EDA·Electronic Design Automation) 전용 도구 없이 오픈소스만으로 48시간 안에 기능적 반도체 칩을 설계했다고 발표했으며, 이에 Cadence와 Synopsys 주가가 각각 9% 급락했다. Moonshot AI의 현재 기업가치는 약 315억달러(약 43조5,000억원)이며, 알리바바가 2024년 10억달러(약 1조3,800억원)를 투자한 바 있다. — [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals) | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3)

- **왜 주목**: 기술 성능 못지않게 생태계 충격이 더 크다. 미국의 고성능 칩 수출 제한 아래에서도 중국 스타트업이 GPT-5.6·Claude Fable 5와 정면 비교되는 오픈웨이트 모델을 내놓은 것 자체가 AI 인프라 투자 지속성에 대한 의구심을 재점화했다. EDA 시연은 "AI가 전통 전문 소프트웨어를 대체할 수 있느냐"는 질문을 반도체 설계 영역까지 확장했다. 반도체지수(SOX)가 주간 -11% 하락하며 기술적 베어마켓에 진입한 배경에 Kimi K3가 자리한다.

- **지켜볼 점**: ① 7/27 전체 가중치 공개 이후 커뮤니티 독립 벤치마크가 자체 발표 수치와 일치하는지. ② EDA 시연에 쓰인 45nm 오픈 공정이 AI 가속기 설계에 쓰이는 3nm·2nm 공정에서도 재현 가능한지 — 이 대목이 Cadence·Synopsys 해자의 진짜 깊이를 가른다. ③ Kimi K3가 주도하는 저비용 오픈웨이트 경쟁이 심화될 경우 엔비디아·SK하이닉스로 이어지는 HBM 수요 체인에 미치는 영향. ④ 미국 정부의 추가 제재 타깃 가능성.

- **수요자는 누구·왜 선택하나**: AI 개발자·연구자는 오픈웨이트 특성 덕에 직접 다운로드·파인튜닝이 가능하며, 클라우드 API 비용 없이 온프레미스 운영이 된다. 비용 민감 스타트업에게 API 단가 경쟁력이 채택 유인이 된다. 기업 도입 결정자 입장에서는 데이터 주권 요건이 있을 때 온프레미스 배포 선택지라는 우위가 있다. EDA 고객사(반도체 팹리스)에게는 아직 45nm 수준의 시연이라 실제 전환 장벽이 높다 — 검증 데이터 부족, 전문 EDA 툴 생태계와의 통합 미성숙이 채택 장벽이다.

---

## 2. SK하이닉스 — 마진 77% 목표, 그러나 Kimi K3 역풍 속 실적 해석이 관건 (반도체·한국)

- **무슨 일**: SK하이닉스가 2026년 7월 22일 2026년 2분기 실적을 발표한다. 시장 컨센서스는 영업이익 65조 원(전년 동기 대비 +556%)으로, 달성 시 분기 역대 최고치 경신이 예상된다. 영업이익률 추정치 77%는 엔비디아·TSMC를 포함한 글로벌 반도체 기업 중 최고 수준으로 꼽힌다. 고대역폭메모리(HBM·High Bandwidth Memory) 3E는 매진 상태이며, HBM4 양산은 3분기 시작 예정이다. 한편 한국투자증권이 7월 13일 영업이익을 60.4조 원으로 하향 조정한 이후 당일 주가가 -15.4% 급락해 컨센서스 하회 시 낙폭에 대한 경계감이 남아 있다. — [BigGo Finance](https://finance.biggo.com/news/e1254997-10cd-4d1e-940c-74bf59bdbf32) | [CNBC](https://www.cnbc.com/2026/04/23/sk-hynix-earnings-ai-memory-shortage-hbm-demand.html)

- **왜 주목**: SK하이닉스는 AI 메모리 공급망에서 현재 단일 불가결 지점(single critical node) 역할을 하고 있다. 엔비디아 Blackwell 가속기에 HBM3E를 독점에 가깝게 공급하며, HBM4 전환에서도 선두 입지를 유지하고 있다. 문제는 아무리 좋은 실적이 나와도 Kimi K3 충격으로 AI 인프라 투자 지속성에 대한 의구심이 커진 상황에서 주가 반응이 실적 수치에 비례하지 않을 수 있다는 점이다.

- **지켜볼 점**: ① 65조 원 컨센서스 달성 여부. ② HBM 장기공급계약(LTA·Long-Term Agreement) 단가가 예상보다 낮게 책정됐는지에 대한 경영진 가이던스. ③ HBM4 3분기 양산·고객 인도 일정 확인 — 2027년 수주 선점과 직결된다. ④ Kimi K3류 저비용 오픈웨이트 모델이 대형 AI 클러스터 투자를 줄이는 방향으로 시장 구조를 바꾼다면 중장기 HBM 수요 전망에 어떤 영향을 주는지.

- **수요자는 누구·왜 선택하나**: 수요자는 엔비디아·AMD·구글·마이크로소프트·메타 등 AI 가속기 설계·운영사다. 대형언어모델(LLM·Large Language Model) 추론·학습에서 HBM은 대역폭 제약을 해소하는 사실상 유일한 선택지다. 지불의향은 높고 대안이 제한적이다. 현재 채택 장벽은 공급 부족으로, 수요가 공급을 초과하는 상황이 이어지고 있다.

---

## 3. Otsuka — centanafadine, ADHD 비자극제 새 계열 첫 신약 PDUFA D-6 (제약·일본)

- **무슨 일**: 오츠카(Otsuka)의 ADHD 신약 centanafadine의 FDA 심사 결정일(PDUFA)이 2026년 7월 24일로 6일 앞으로 다가왔다. centanafadine은 노르에피네프린·도파민·세로토닌 3중 재흡수 억제제(NDSRI·Norepinephrine, Dopamine, Serotonin Reuptake Inhibitor) 계열 최초 신약이며, 소아·청소년·성인 ADHD를 아우르는 4건의 피벗 3상에서 위약 대비 증상 개선이 통계적으로 유의하게 확인됐다. 2026년 6월 25일에는 ADHD와 불안장애를 동반한 성인 대상 3b상에서도 긍정 결과를 추가로 확보했다. FDA 우선심사(Priority Review) 지정으로 검토 중이다. — [Otsuka US 공식](https://www.otsuka-us.com/news/otsuka-announces-fda-acceptance-and-priority-review-new-drug-application-centanafadine) | [Medical Daily](https://www.medicaldaily.com/centanafadine-fda-decision-july-24-2026-adhd-non-stimulant-children-adults-otsuka-476083) | [Applied XL](https://www.appliedxl.com/news/otsuka-pharmaceutical-development-commercialization-inc-otsuka)

- **왜 주목**: ADHD 비자극제 시장에서 현재 가장 많이 쓰이는 아토목세틴(atomoxetine·스트라테라)은 제네릭 경쟁이 치열하고, 빌록사진(viloxazine·큐엘브리)은 성인 적응증이 없다. centanafadine이 승인되면 새로운 기전의 최초 신약으로서 기존 비자극제 실패 환자에게 추가 선택지를 제공한다. 비자극제는 자극제 대비 의존성·남용 우려가 적어 지불자의 급여 거부감도 낮다. 불안장애 동반 환자군 3b상 데이터는 실제 임상에서 처방 근거를 넓히는 차별화 포인트다.

- **지켜볼 점**: ① 7/24 FDA 결정 결과 — 완전 승인, 조건부 승인, 보완요구서한(CRL·Complete Response Letter) 중 무엇인지. ② 승인 라벨 범위 — 소아·청소년·성인 모두 포함 여부가 시장 규모를 결정한다. ③ 약가 설정 전략 — 제네릭 아토목세틴 대비 프리미엄이 지불자 급여 협상의 핵심 변수다. ④ 일본·유럽 규제 전략 타임라인.

- **R&D·경쟁 구도**: ADHD 비자극제 경쟁자는 아토목세틴(제네릭), 구아파신(guanfacine·인투니브), 빌록사진이다. centanafadine의 3중 재흡수 억제 기전(NDSRI)은 단일·이중 억제 계열과 구분되며, 경구 서방형 1일 1회 투여로 편의성은 동등하다. 불안 동반 환자 데이터는 기존 약에 없는 라벨 우위가 될 수 있다.

- **수요자는 누구·왜 선택하나**:
  - 환자: 자극제(암페타민·메틸페니데이트) 부작용이나 남용 우려로 비자극제를 원하는 어린이·청소년·성인. 특히 불안장애 동반 환자는 단일 약물로 두 증상을 조절하는 미충족 수요가 있었다.
  - 처방의(정신건강의학과·소아과): 기존 비자극제 실패 환자에게 새 기전의 선택지가 생긴다. 3b상 불안 동반 데이터가 처방 근거를 제공한다. 채택 장벽은 새 기전에 대한 장기 안전성 데이터 축적 여부다.
  - 지불자(보험사·메디케이드): 비자극제라 의존성 분류 문제가 없어 사전승인 요건이 낮다. 다만 브랜드 신약 가격이 제네릭 아토목세틴 대비 크게 높으면 급여 등재 협상이 길어질 수 있다.

---

## 4. 코오롱티슈진 — TG-C 3상(1,066명) 톱라인, 7/20 전후 발표 임박 (바이오·한국)

- **무슨 일**: 코오롱티슈진의 골관절염 유전자세포치료제 TG-C(구 인보사) 미국 3상(15302 연구, 1,066명) 톱라인 결과가 7월 18일 현재 미공개 상태다. 회사는 "7월 중 발표"를 예고했으며, 코스피 거래일 기준 7월 20일(월) 재개장일이 유력한 발표 시점으로 꼽힌다. 2차 3상(12301 연구)은 10월 톱라인, BLA(생물의약품 허가 신청·Biologics License Application) 제출은 2027년 1분기를 목표로 한다. — [Seoul Economic Daily](https://en.sedaily.com/news/2026/06/25/kolon-tissuegene-nears-tg-c-phase-3-data-release) | [코오롱티슈진 IR](https://www.tissuegene.com/en_US/investors/pr/detail/40/tg-c)

- **왜 주목**: TG-C는 형질전환성장인자-β1(TGF-β1·Transforming Growth Factor-β1) 유전자를 탑재한 동종 연골세포를 관절강 내 단회 주사하는 유전자세포치료제다. 골관절염에서 2년 이상 지속적인 질병 수정 효과를 내는 약물은 현재 FDA 승인 사례가 없다. 1,066명 대규모 3상에서 1차 평가변수(통증·기능·환자전반평가 복합)를 달성하면 한국 바이오 기업 최초의 미국 FDA 승인 유전자세포치료제가 될 가능성이 있다. 성공·실패 시나리오 모두에서 주가 영향이 비대칭적으로 크다는 점에서 단기 이벤트 위험이 높다.

- **지켜볼 점**: ① 통계적 유의성 달성 여부 — 1차 평가변수(복합 통증·기능·전반평가)를 주요 하위그룹 모두에서 충족하는지. ② 2년 내구성(TGF-β1 발현 유지) 데이터. ③ 종양원성(tumorigenicity) 등 안전성 신호 여부. ④ 2차 3상(12301) 10월 결과와의 일관성 — FDA BLA 제출에는 두 시험 모두 긍정 결과가 필요하다.

- **R&D·경쟁 구도**: 골관절염 유전자치료 분야는 경쟁자가 극히 드물다. 기존 표준 치료는 NSAIDs(비스테로이드성 항염증제)·코르티코스테로이드·히알루론산 주사로, 이들은 증상 완화에 그치고 질병 진행을 막지 못한다. TG-C는 이 미충족 수요를 겨냥한다. 모달리티: 동종 세포+유전자 복합, 단회 관절강 내 주사.

- **수요자는 누구·왜 선택하나**:
  - 환자: 무릎 골관절염 중증 환자, 특히 기존 주사 치료로 효과가 불충분하고 인공관절 수술을 미루거나 피하려는 환자. 단회 주사로 2년 이상 통증 완화가 확인되면 치료 부담이 크게 줄어든다.
  - 처방의(정형외과·류마티스내과): 질병 수정 효과를 내는 골관절염 치료제 선택지 자체가 없는 상황이라 승인 시 처방 유인은 높다. 다만 유전자세포치료제 투여 프로토콜 훈련과 관리 인프라가 초기 채택 장벽이 된다.
  - 지불자(보험사·메디케어·메디케이드): 골관절염은 유병률이 매우 높아 급여 적용 범위가 상업화 최대 변수다. 단회 고가 유전자치료제 급여 모델이 선례(Novartis Zolgensma 등)로 자리 잡고 있으나, 생명에 직접적 위협이 없는 만성 근골격 질환에 이를 적용하는 비용효과 기준은 다를 수 있다. 약가·급여 협상이 미국 상업화의 진짜 관문이다.

---

## 5. Google·Alphabet — Gemini 3차 지연, 조직 구조가 기술보다 큰 문제 (AI·미국)

- **무슨 일**: 블룸버그가 2026년 7월 16일 내부 소식통을 인용해 Gemini 3.5 Pro가 내부 코딩 성능 기준을 충족하지 못해 세 번째 연속 출시 지연이 확정됐다고 보도했다. Sundar Pichai CEO가 5월 I/O에서 "6월 내 제공"을 약속했으나 마감을 세 차례 넘겼다. Alphabet 주가는 7월 16일 하루 4.4% 하락해 시가총액 약 2,000억달러(약 276조원)가 감소했다. 구글은 스톱갭으로 Gemini 3.5 Flash를 출시했고, 내부적으로 Gemini 3.6 Flash 모델명을 등록한 것으로 알려졌다. DeepMind 고참 연구원 4명이 Anthropic으로 이직했으며, 구글은 현재 주요 프런티어 AI 랩 중 유일하게 2026년 플래그십 모델을 출시하지 못한 곳이 됐다. — [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/google-gemini-launch-delayed-as-tech-falls-short-of-internal-goals) | [TechTimes](https://www.techtimes.com/articles/320736/20260716/rebuilt-gemini-35-pro-misses-third-deadline-google-eyes-stopgap-release.htm) | [Alphabet -$200B 분석](https://ts2.tech/en/alphabet-inc-nasdaqgoogl-sheds-nearly-200-billion-after-gemini-delay-raises-questions-on-ai-investment/)

- **왜 주목**: 지연 자체보다 구조적 원인이 더 중요하다. DeepMind·Cloud·Android·Search 팀이 AI 코딩 도구를 병렬로 개발하는 조직 중복이 원인으로 지목됐는데, 이는 기술 난제가 아니라 의사결정 구조 문제다. 경쟁사는 GPT-5.6(7/9), Grok 4.5(7/8), Kimi K3(7/17)를 잇따라 내놓으며 플래그십 격차를 벌리고 있다. DeepMind 인재 이탈이 단발이 아니라 추가 이직의 신호라면 중장기 R&D 역량 저하로 이어질 수 있다.

- **지켜볼 점**: ① Gemini 3.5 Pro 실제 출시 시점 — Gemini 3.5 Flash(스톱갭)와 등록된 Gemini 3.6 Flash 중 무엇이 먼저 나오는지. ② 7/22 Alphabet Q2 실적에서 AI 검색·Google Cloud 매출 성장률이 지연 우려를 상쇄할 수 있는지. ③ DeepMind 고참 이탈이 추가로 이어지는지 여부.

- **수요자는 누구·왜 선택하나**:
  - AI 개발자·기업 도입 결정자: Gemini API를 쓰는 기업은 플래그십 지연 시 OpenAI·Anthropic API로 전환을 검토하게 된다. 전환 비용이 0은 아니지만 대안이 충분히 존재하며, 현재 경쟁사의 플래그십 성능 우위가 유지되는 한 전환 유인이 지속된다. 구글 Workspace(Gmail·Docs·Meet) 통합 유인이 잔류를 지지하는 요인이다.
  - 기업 IT 예산 집행자(지불자): 클라우드 AI 계약을 갱신·확대할 시점에서 로드맵 지연은 협상 우위를 경쟁사에 넘겨주는 요인이 된다.
  - 최종 사용자(Workspace·Google Search 이용자): 플래그십 지연이 제품에 반영되기까지 시차가 있어 단기 체감 영향은 제한적이다.

---

## 오늘의 주목 플레이어 요약

- **Moonshot AI(Kimi K3)**: 미국의 칩 수출 제한에도 중국 스타트업이 최전선 오픈웨이트 모델을 공개했다. EDA 없는 48시간 칩 설계 시연이 Cadence·Synopsys를 각 9% 끌어내렸으나, 45nm 공정 한계라는 중요한 단서가 붙는다. 7/27 전체 가중치 공개 후 독립 검증이 이 시연의 실질적 의미를 가른다.
- **SK하이닉스**: 영업이익 65조 원(+556%) 컨센서스와 77% 마진 목표가 실현되면 글로벌 최고 수익성 기업 반열에 오른다. 그러나 Kimi K3 충격으로 AI 인프라 투자 전망이 흔들린 환경에서 HBM4 양산 일정 확인이 주가 반응을 결정하는 핵심 변수가 될 전망이다.
- **Otsuka(centanafadine)**: PDUFA D-6. NDSRI 계열 최초 신약 승인 시 비자극제 ADHD 시장 재편 가능성이 있다. 불안 동반 3b상 데이터가 차별화 포인트이나, 브랜드 약가와 제네릭 아토목세틴 간 급여 협상이 상업화 성패를 가르는 진짜 관문이다.
- **코오롱티슈진(TG-C)**: 1,066명 대규모 3상 결과가 7/20 전후 공개될 것으로 예상된다. 성공 시 골관절염 최초 질병 수정 유전자세포치료제·한국 바이오 최초 FDA 승인 사례가 된다는 상징성이 있다. 성공·실패 시나리오 모두에서 주가 영향이 비대칭적으로 크다.
- **Google·Alphabet**: 기술 지연보다 조직 구조 문제가 더 심각하다는 신호가 쌓이고 있다. 주요 프런티어 AI 랩 중 유일하게 2026년 플래그십 모델 공백 상태가 이어지며, 인재 이탈 추이가 중기 R&D 역량의 선행 지표가 될 것으로 보인다.

---

## 이어지는 주제

- [[topics/AI인프라]] — Moonshot AI Kimi K3·오픈웨이트 경쟁·EDA 해자 리스크
- [[topics/반도체AI인프라]] — SK하이닉스 HBM 독주·HBM4 전환·7/22 실적
- [[topics/바이오제약]] — centanafadine PDUFA 7/24·Otsuka ADHD 비자극제 시장
- [[topics/한국제약바이오]] — 코오롱티슈진 TG-C 3상 결과·유전자세포치료제 FDA 도전
