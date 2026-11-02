---
date: 2026-08-23
type: analysis
lens: company
tags: [AI, 반도체, HBM4, NVIDIA, AMD, SKHynix, 제약바이오, JazzPharma, AstraZeneca, Ionis, ATTR-CM, HER2, HotChips2026]
links: ["[[topics/HotChips2026]]", "[[topics/NVIDIAEarnings]]", "[[topics/JazzZiihera]]", "[[topics/ESCCongress2026]]", "[[topics/SKHynixIndiana]]"]
---
# 유망 기업·주목 플레이어 2026-08-23

## NVIDIA (AI 가속기·반도체, 미국)
- **무슨 일**: 8월 23일 Hot Chips 2026(스탠퍼드 메모리얼 오디토리움) Day 1에서 Vera Rubin 플랫폼 공식 스펙을 발표했다. R100 GPU 트랜지스터 336억 개, TSMC 3나노 듀얼 다이 설계, HBM4 288GB, NVFP4 추론 성능 50 PFLOPS(블랙웰 대비 5배), NVLink 6 GPU 간 통신 3,600 GB/s가 확인됐다. 다만 목표 HBM4 대역폭 22 TB/s는 공급사가 달성하지 못해 초기 출하분은 약 20 TB/s 수준임이 TechPowerUp에 의해 병행 보도됐다. 실적 발표(FY2027 Q2)는 3일 후인 8월 26일이며 월가 컨센서스 매출은 약 920억달러(약 127조6,000억원), 주가 약 220달러(약 30만5,000원), 분석사 평균 목표가 약 305달러(약 42만3,000원) 수준이다.
- **왜 주목**: Vera Rubin는 데이터센터 AI 훈련·추론 시장의 사실상 성능 기준점이 된다. HBM4 대역폭 목표 미달이 공급사(SK하이닉스·삼성) 수율 한계를 드러낸 점, NVL72 랙 집계 합산 대역폭이 AMD와의 스펙 경쟁 무대가 됐다는 점이 핵심 변수다. 8월 26일 실적에서 데이터센터 매출 가이던스와 Vera Rubin 수요 선행지표가 동시에 제시될 것으로 보인다.
- **지켜볼 점**: ① 8월 26일 FY2027 Q2 매출이 컨센서스(~920억달러) 대비 어떻게 나오는지, 3분기 가이던스(컨센서스 950억~1,000억달러 범위) ② HBM4 공급 제약이 Rubin Ultra 출하 일정에 미치는 영향 — TrendForce는 8-Hi HBM4e·12-Hi HBM4 대안 검토를 전했다 ③ AMD MI455X 경쟁이 하이퍼스케일러 구매 결정에 실제 영향을 줄지 여부.
- **수요자는 누구·왜 선택**: 도입기업(하이퍼스케일러) Microsoft·Google·Meta·Oracle 등이 AI 훈련·추론 인프라를 구축하며 선택한다. CUDA 에코시스템이 전환 비용 장벽으로 작용해 경쟁 제품이 일부 스펙에서 우위를 보여도 당장 대규모 이탈이 어려운 구조다. 개발자·AI 스타트업은 CUDA 의존도가 높아 사실상 기본 선택지로 쓴다. HBM4 공급 제한으로 초기 수량이 제한될 전망이어서 대기업 우선 배정 구도가 예상된다. AMD가 메모리 용량 어드밴티지를 내세우며 일부 하이퍼스케일러의 포트폴리오 분산 가능성을 키우고 있다.
- 출처: [NVIDIA Hot Chips 공식](https://www.nvidia.com/en-us/events/hot-chips-conference/) | [Tech-Insider — Vera Rubin 스펙](https://tech-insider.org/nvidia-vera-rubin-platform-gtc-2026-rubin-r100-gpu/) | [TechPowerUp — HBM4 대역폭 미달](https://www.techpowerup.com/346983/nvidia-lowers-hbm4-specs-for-vera-rubin-vr200-as-memory-suppliers-miss-22-tb-s-target) | [Intellectia — 실적 프리뷰](https://intellectia.ai/blog/nvidia-earnings-august-2026-preview)

## AMD (AI 가속기·반도체, 미국)
- **무슨 일**: Hot Chips 2026 Day 1에서 Instinct MI455X와 MI430X의 공식 세부 스펙을 공개했다. MI455X는 CDNA 5 아키텍처, TSMC 2N GAA(게이트올어라운드) 공정, 트랜지스터 3,200억 개, HBM4 432GB(대역폭 23.3 TB/s), FP4 40 PFLOPS를 탑재했다. HBM4 용량 기준으로 NVIDIA VR200(288GB) 대비 50% 더 많다. MI430X는 FP64 288 TFLOPS로 HPC(고성능 컴퓨팅)·주권 AI·연구기관을 겨냥했다. Microsoft·Meta·Oracle에 Helios 랙스케일 플랫폼(EPYC 9006 + MI455X + Pensando)과 연동해 공급된다고 AMD가 밝혔다.
- **왜 주목**: AI 가속기 시장에서 NVIDIA에 맞선 실질적 경쟁 구도가 스펙 수준에서 처음으로 확인됐다. 단일 GPU에 더 큰 모델 파라미터를 올릴 수 있다는 메모리 용량 어드밴티지는 LLM(대형 언어 모델) 추론 비용 절감 논거로 쓰인다. HPCwire는 MI430X FP64 수치를 "예상보다 훨씬 크다"고 평가했다.
- **지켜볼 점**: ① HBM4 공급 확보 및 실제 출하 리드타임 ② ROCm(AMD 소프트웨어 에코시스템) 성숙도 — CUDA 대체 가능 수준인지가 실제 채택의 관문 ③ Microsoft·Meta·Oracle의 실제 구매 규모 공시 여부 ④ NVIDIA 실적(8/26) 이후 하이퍼스케일러 자본지출(capex) 배분 방향.
- **수요자는 누구·왜 선택**: 도입기업(하이퍼스케일러)은 HBM4 432GB로 더 큰 모델을 단일 칩에 올릴 수 있어 추론 비용 절감 논거로 검토한다. CUDA 에코시스템 외 공급원 확보로 협상력을 유지하려는 전략적 동기도 작용한다. HPC·연구기관은 MI430X FP64 성능이 과학 계산·기후 모델·바이오 시뮬레이션 수요에 직접 대응한다. ROCm 소프트웨어 미성숙이 실 배포 단계 전환 비용을 높이는 채택 장벽이다.
- **R&D/경쟁 구도**: CDNA 5는 TSMC 2N GAA 공정으로 전력 효율이 향상됐다. 경쟁 축은 "메모리 용량(AMD) vs 소프트웨어 에코시스템·GPU 간 연결(NVIDIA NVLink 6)"으로 분화됐다. MI430X FP64는 Intel Gaudi 3·NVIDIA H200 HPC 세그먼트와 직접 경쟁한다.
- 출처: [ServeTheHome — MI455X 딥다이브](https://www.servethehome.com/amd-instinct-mi455x-deep-dive-cdna-5-marks-the-next-era-of-instinct/) | [Tom's Hardware — MI455X vs NVIDIA](https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center) | [HPCwire — MI430X FP64](https://www.hpcwire.com/2026/08/03/amds-fp64-boost-with-mi430x-is-even-bigger-than-expected/) | [SiliconReport — AMD vs Vera Rubin 비교](https://www.siliconreport.com/amd-mi455x-vs-nvidia-vera-rubin-bd525bb4)

## SK하이닉스 (HBM·메모리 반도체, 한국)
- **무슨 일**: Hot Chips 2026 Day 1에서 이재식 부사장(SK Hynix America 패키지 엔지니어링 총괄)이 HBM4E 고급 패키징 기술 세션을 발표했다. MR-MUF(Molded Resin with Mass Reflow Underfill, 몰드 수지 매스 리플로우 언더필) 공법으로 핀당 16Gbps, 12층 스택 기준 48GB, 발열 저항 HBM4 대비 17% 절감이 확인됐다고 밝혔다. NVIDIA Vera Rubin용 HBM4 공급 비중은 약 70%이며, 인디애나 HBM 패키징 공장(38억7,000만달러·약 5조3,600억원 투자) 착공식이 4일 후인 8월 27일로 예정됐다.
- **왜 주목**: HBM 공급망에서 삼성과의 기술 경쟁축이 "패키징(SK하이닉스) vs 베이스 다이 설계(삼성)"으로 분화됐음이 Hot Chips 세션에서 확인됐다. NVIDIA 의존도 70%가 모멘텀이자 집중 리스크다. 인디애나 공장은 HBM 후공정 패키징 역량을 미국 현지화하는 첫 거점으로 지정학적 공급망 재편 흐름에서 중요한 위치를 차지한다.
- **지켜볼 점**: ① 8월 27일 인디애나 착공식 — 추가 정부 인센티브 발표 여부 ② NVIDIA 실적(8/26) 이후 Vera Rubin 출하 일정 변동이 HBM4 주문량에 미치는 영향 ③ HBM4E 양산 시점 및 삼성 대비 기술 격차 ④ TrendForce가 전한 Rubin Ultra HBM 구성 변경(12-Hi → 8-Hi 검토) 시나리오에서 수주량 재산정 가능성.
- **수요자는 누구·왜 선택**: 직접 수요자인 GPU 제조사(NVIDIA·AMD)가 AI 가속기 성능의 병목인 메모리 대역폭 확보를 위해 HBM을 구매한다. NVIDIA VR200용 HBM4에서 SK하이닉스가 약 70% 비중을 확보한 것은 수율·납기 경쟁력이 평가됐기 때문으로 풀이된다. 간접 수요의 풀은 하이퍼스케일러가 AI 인프라에 집행하는 자본지출이다. 고급 패키징(MR-MUF) 기술은 진입 장벽이 높아 단기 대체가 어렵다. NVIDIA가 삼성에 30% 비중을 유지하는 것은 단일 공급사 의존 리스크 분산 전략으로 분석된다.
- 출처: [Herald Business — Hot Chips 삼성·SK하이닉스](https://mbiz.heraldcorp.com/article/10834490) | [MobileMasr — HBM4E 샘플](https://mobilemasr.com/en/blogs/sk-hynix-ships-hbm4e-samples-2026) | [CNBC — SK하이닉스 투자](https://www.cnbc.com/2026/08/07/sk-hynix-memory-chips-ai-prices.html) | [TechPowerUp — HBM4 공급 배분](https://www.techpowerup.com/346983/nvidia-lowers-hbm4-specs-for-vera-rubin-vr200-as-memory-suppliers-miss-22-tb-s-target)

## Jazz Pharmaceuticals (종양학·바이오파마, 미국/아일랜드)
- **무슨 일**: HER2 양성(HER2+) 위장관선암(GEA, Gastroesophageal Adenocarcinoma) 1차 치료 적응증 확대를 위한 보충 생물의약품 허가 신청(sBLA)에 대한 FDA 최종 허가 목표일(PDUFA)이 8월 25일(월요일)로 이틀 앞으로 다가왔다. Ziihera(자니다타맙-hrii, zanidatamab-hrii)는 2024년 HER2+ 담도암 2차 치료로 이미 허가된 제품이며 이번은 적응증 확대 sBLA다. HERIZON-GEA-01 3상에서 자니다타맙 + 티슬렐리주맙(PD-1) + 화학요법 3제 병용군의 중위 전체 생존기간(OS) 26.4개월, 위험비(HR) 0.63~0.65(P<0.0001)가 확인됐다고 Jazz Pharma가 공시했다. 복수 매체가 승인 기대 우세를 보도 중이다.
- **왜 주목**: Jazz는 수면장애·마약성 진통제 등 특수 신경과·통증 포트폴리오 중심 기업이었다. Ziihera 승인 시 종양학 분야로의 다각화가 처음으로 구체화되며, HER2+ 위·식도·위식도접합부암은 HER2 표적 치료제 시장에서 유방암 다음으로 규모가 큰 세그먼트로 상업화 모멘텀이 기업 가치 재평가의 근거가 될 수 있다는 분석이 나온다.
- **지켜볼 점**: ① 8월 25일 FDA 승인 여부 — Complete Response Letter(CRL) 가능성도 배제할 수 없다 ② 승인 시 약가 설정 및 보험 급여 협상 일정 ③ Jazz의 자체 종양학 영업망 구축 여부 또는 공동 판매 파트너 계약 여부 ④ 트라스투주맙 데룩스테칸(T-DXd, ADC) 등 경쟁 약물 대비 임상 포지셔닝.
- **수요자는 누구·왜 선택**:
  - **환자**: HER2+ 위장관선암 1차 치료 환자는 현재 트라스투주맙(HER2 단일 표적) + 화학요법이 표준요법이다. 자니다타맙 3제 병용은 OS 26.4개월로 개선된 생존 데이터를 제시한다.
  - **처방의(종양내과의)**: HER2·HER3 이중 에피토프 이중특이항체(bispecific antibody) 메커니즘이 단일 표적 대비 저항성 극복 논거로 쓰인다. 3제 병용 복잡성과 독성 프로파일이 처방 결정의 실제 변수가 될 것으로 보인다.
  - **지불자(보험사·Medicare)**: HER2+ 위암은 상대적으로 희귀 적응증이어서 고가 약가 수용 가능성이 있으나, PD-1 + 화학요법 + HER2 항체 3제 병용의 비용효과(ICER) 분석이 급여 등재 협상의 관문이 될 전망이다.
- **R&D/경쟁 구도**: 자니다타맙은 HER2 ECD2·ECD4 이중 에피토프를 타겟하는 이중특이항체 모달리티다. 경쟁 약물은 아스트라제네카·다이이치산쿄의 트라스투주맙 데룩스테칸(T-DXd, ADC)으로, 2차 치료에서 강력한 입지를 구축했으나 1차 치료 자리를 두고 경쟁이 시작될 수 있다. 자니다타맙의 차별화 포인트는 PD-1 면역관문억제제와의 병용 설계다.
- 출처: [Jazz Pharma sBLA 수리 공시](https://investor.jazzpharma.com/news-releases/news-release-details/jazz-pharmaceuticals-announces-fda-acceptance-and-priority-0) | [OncLive — HERIZON-GEA-01 임상](https://www.onclive.com/view/fda-grants-priority-review-to-zanidatamab-based-regimens-in-first-line-her2-gea) | [PRNewswire — sBLA 발표](https://www.prnewswire.com/news-releases/jazz-pharmaceuticals-announces-fda-acceptance-and-priority-review-of-supplemental-biologics-license-application-for-ziihera-zanidatamab-hrii-combinations-in-first-line-her2-locally-advanced-or-metastatic-gea-302753741.html)

## AstraZeneca·Ionis (심혈관·RNA 치료제, 영국/미국)
- **무슨 일**: ATTR-CM(트랜스티레틴 아밀로이드 심근병증, transthyretin amyloid cardiomyopathy) 환자 1,400명 이상을 대상으로 한 CARDIO-TTRansform 3상(eplontersen, GalNAc-ASO 모달리티)이 1차 종점(심혈관 사망 + 재발 심혈관 사건 복합, 140주)을 충족하지 못했다고 7월 8일 아스트라제네카와 Ionis가 공동 발표했다. 단, 사전 지정 서브그룹에서 eplontersen 단일요법 대 위약 간 위험비(HR) 0.71(명목상 유의)이 확인됐다. 기존 스타빌라이저(tafamidis 등) 병용 환자군에서는 치료 효과가 없었다. ESC 2026(8월 28~31일, 뮌헨) 핫라인 세션에서 전체 데이터가 공개될 예정이다.
- **왜 주목**: ATTR-CM 치료제 시장은 Pfizer의 tafamidis(스타빌라이저)가 선점한 구도에서 RNA 기반 치료제(ASO·siRNA)의 추격이 핵심 서사였다. 1차 종점 실패는 이 경쟁 구도를 재설정하며, 특히 기존 스타빌라이저 병용 환자에서 추가 이익이 없다는 결과는 환자 선택 전략과 향후 임상 설계 방향에 직접 영향을 준다.
- **지켜볼 점**: ① 8월 28일 ESC 핫라인 전체 데이터 — 스타빌라이저 미사용 단독 코호트에서 HR 0.71이 얼마나 견고한지 ② 전체 데이터 공개 후 아스트라제네카·Ionis의 ATTR-CM 전략 재검토 발표 여부 ③ Pfizer tafamidis 유지 압력이 약가·시장 위치에 어떻게 반영될지 ④ Alnylam의 vutrisiran(siRNA, ATTR-CM 적응증 승인) 등 경쟁 RNA 치료제 포지션 변화.
- **수요자는 누구·왜 선택**:
  - **환자**: ATTR-CM은 진단이 늦고 예후가 불량한 심근병증으로 미충족 수요가 크다. 다만 eplontersen이 스타빌라이저 사용자에게 추가 이익을 주지 못하면 신규 단독 진단 환자(스타빌라이저 미사용)만이 실질 수요층이 된다.
  - **처방의(심장 전문의)**: 1차 종점 실패로 가이드라인 반영 가능성이 낮아졌다. ESC 전체 데이터가 서브그룹 이익을 명확히 하지 못하면 처방 채택 동기가 약해질 것으로 보인다.
  - **지불자(보험사·급여 당국)**: 1차 종점을 충족하지 못한 약물의 급여 등재는 상당한 난관이 예상된다. 비용효과(ICER) 입증이 어려워질 가능성이 있다는 분석이 나온다.
- **R&D/경쟁 구도**: eplontersen은 GalNAc 접합 ASO(안티센스 올리고뉴클레오타이드, antisense oligonucleotide) 모달리티로 TTR 단백질 생성을 간에서 억제한다. 경쟁 약물: Alnylam의 vutrisiran(GalNAc-siRNA, ATTR-CM 승인), patisiran(siRNA), Pfizer tafamidis(TTR 스타빌라이저). 1차 종점 실패로 아스트라제네카·Ionis의 ATTR-CM 전략 재검토가 불가피할 것으로 보인다.
- 출처: [AstraZeneca — CARDIO-TTRansform 업데이트](https://www.astrazeneca.com/media-centre/press-releases/2026/update-cardio-ttransform-phase-iii-trial.html) | [AJMC — 1차 종점 미충족](https://www.ajmc.com/view/eplontersen-misses-primary-end-point-in-phase-3-attr-cm-cardiovascular-outcomes-trial) | [BioSpace — 임상 업데이트](https://www.biospace.com/press-releases/update-on-cardio-ttransform-phase-3-trial-of-eplontersen-in-adults-with-transthyretin-mediated-amyloid-cardiomyopathy)

---

## 오늘의 주목 플레이어 요약

- **NVIDIA**: Vera Rubin R100 공식 스펙이 확인됐으나 HBM4 대역폭이 목표(22 TB/s) 대비 초기 출하분 약 20 TB/s로 공급사 한계가 드러났다. 8월 26일 실적에서 Vera Rubin 수주 상황과 3분기 가이던스가 동시에 공개되어 단기 시장 심리의 분수령이 될 것으로 보인다.
- **AMD**: MI455X HBM4 432GB·23.3 TB/s 스펙이 NVIDIA 대비 메모리 용량 50% 우위를 공식화했다. ROCm 소프트웨어 성숙도와 HBM4 공급 확보가 실제 하이퍼스케일러 채택으로 이어질지가 향후 6~12개월의 핵심 관전 포인트다.
- **SK하이닉스**: HBM4E MR-MUF 패키징 기술 선도·NVIDIA HBM4 공급 약 70% 비중·인디애나 착공(8/27) 세 모멘텀이 동시에 확인됐다. NVIDIA 의존도 집중이 리스크이며, Rubin Ultra HBM 구성 변경 검토 현실화 시 수주량 재산정 시나리오가 열린다.
- **Jazz Pharmaceuticals**: Ziihera HER2+ GEA 1차 치료 FDA 결정이 48시간 내로 다가왔다. 승인 시 종양학 포트폴리오 진입이 확인되고, 부결(CRL) 시 추가 임상 설계 부담이 생긴다. 3제 병용의 급여 협상 가능성이 상업화 속도의 핵심 변수다.
- **AstraZeneca·Ionis**: eplontersen ATTR-CM 1차 종점 실패는 RNA 기반 치료제가 스타빌라이저 사용 환자를 대체하기 어렵다는 시나리오를 부각시켰다. 8월 28일 ESC 전체 데이터에서 스타빌라이저 미사용 코호트 이익이 얼마나 견고한지가 파이프라인 향방을 가를 전망이다.

## 이어지는 주제
- [[topics/HotChips2026]]
- [[topics/NVIDIAEarnings]]
- [[topics/JazzZiihera]]
- [[topics/ESCCongress2026]]
- [[topics/SKHynixIndiana]]
