---
type: log
title: econ-radar — 변경 이력(Changelog)
timestamp: 2026-06-24T00:00:00+00:00
publish: false
---
# 📑 econ-radar 변경 이력

하네스·vault의 날짜별 변경 기록을 최신순으로 모은 루트 로그다. 각 항목의 배경·동기·세부 진단은 [_meta/improvement-log.md](/_meta/improvement-log.md)에 양식과 함께 보존돼 있다. 이 파일은 "언제 무엇이 바뀌었나"의 색인이다.

## 2026-06-24
- vault OKF 마이그레이션 2층(큐레이션): 잔여 깨진 토픽 링크 43개 정리. RNA 치료제 계열(ASO·siRNA·mRNA·RNA 편집·AOC) 신규 canonical MOC [RNA치료제](/topics/RNA치료제.md) 생성, 관련 13개 타깃 통합. 기존 canonical 매핑 8개 타깃(엔비디아-수출규제→반도체, eli-lilly 계열→GLP-1비만치료, 유한양행-렉라자→한국제약바이오, AI-IPO→AI, biotech-IPO 계열→투자테마). 일회성 엔티티 22개는 OKF 규약대로 깨진 채 유지. 루트 변경 이력 `log.md` 신설.

## 2026-06-16~18 (GitHub Actions 버그 픽스 + 뉴스 신선도·중복 방지)
- 6/16 — GitHub Actions 다중 커밋 push 감지 버그 수정. 감지 범위 `HEAD~1 HEAD` → `github.event.before HEAD`, `fetch-depth: 0`. (커밋 6c7f12f)
- 6/17 — 첫 정상 자동 발행. 텔레그램 알림 자동 수신 확인.
- 6/18 — 뉴스 신선도·중복 방지 시스템 도입. news-scout: 48시간 이상 기사 `[배경]`·직전 발행 중복 항목 `[중복]` 태그로 분리. newsletter-editor: 직전 3일 daily에서 Today's Topic 중복 차단. "에이전트 관성"으로 같은 약·기업이 반복 등장하던 현상 제거.

## 2026-06-14 (미뤄둔 TODO 3건)
- MOC append-only 방지 규칙 명문화(핵심 흐름=덮어쓰기, 타임라인=누적+10개 초과 시 아카이브).
- 투자테마/투자전략 범위 분리(테마=어디 돈 몰리나 WHAT, 전략=거시·포지션·리스크 HOW), 각 MOC에 범위 노트.
- demand-analyst 승격 기준 문서화(`_meta/demand-analyst-criteria.md` 신규).

## 2026-06-13 (하네스 구조 검토 → 우선순위 4건)
- ① fact-checker 신설·T4.7 편입(자동 발행 사실 방어선, 수치 원문 대조·출처 없는 수치 차단).
- ② vault 전체 git 추적(레포 private 전환, 클라우드 큐레이션·멀티위크 연속성).
- ③ 렌더 템플릿화(`scripts/render_html.py` + `scripts/NEWSLETTER-FORMAT.md` 계약, 발행당 토큰 ~40% 절감 목표).
- ④ 3층 가동(주간 동향 리포트 클라우드 루틴, 일 21:00 KST → `reports/`).
- 상세: [_meta/2026-06-13-harness-review.md](/_meta/2026-06-13-harness-review.md)

## 2026-06-12
- 완전 자동 발행 전환. 클라우드 데일리 루틴(18:30 KST)이 생성→블로그 발행→텔레그램 채널 알림까지 수행.

## 2026-06-11 (고객/수요 렌즈 도입 + 큐레이션)
- 수요 렌즈(Demand) (A) 오버레이 도입. `_meta/demand-lens.md` 기준선 신규(투자자=공급·자본 ↔ Demand=수요, 제약/바이오 다중 수요자=환자·처방의·지불자). market-analyst·company-scout·sector-analysis에 수요 렌즈 단 추가.
- 큐레이션: 5개 MOC에 6/11 블록 누적(거시정책·AI·바이오제약·신약개발전략·유망기업), 투자테마·투자전략 드리프트 방지. 신규 발행분 죽은 링크 0건.

## 2026-06-10 (밀도 보강 + 렌즈 교체 + 문체 기준선)
- 뉴스레터 밀도 보강: 핵심 항목 3→5개, "왜 중요한가" 1줄 필수, 투자 섹션 강세/약세 양면 병기. news-scout 섹션당 4~6건·수치 맥락 병기.
- 세 번째 렌즈 교체: 커리어 → 유망 기업(company-scout, `topics/유망기업.md` 신규 MOC). 핵심 항목에 Key Point(객관)+💡 인사이트(주관) 분리.
- 문체 기준선 도입: `_meta/korean-style-samples.md`를 style-critic 의무 참조(AI 상투구 제거·사건 과거형·원화 병기).
- 큐레이션: `topics/방산.md` 신규 생성(죽은 링크 복구), 기존 MOC 6종 연결 주제에 유망기업 추가.

## 2026-06-09 (하네스 신규 구축 + 첫 1층 실행)
- 하네스 신규 구축(1층 전체 + vault/옵시디언 + 3층 골격). 소스=신뢰 경제지+해외 번역, 투자=코스피+해외, 바이오=신약개발 총괄 전략 시점.
- 첫 실행 후 개선: 뉴스레터 2층 구조(한눈에+심층)·전체 원문 링크화, style-critic 신설·T4.5 편입, benchmark-scout·`benchmarks.md`로 깊이 기준선 도입, 일일 HTML은 `html/`로 분리.
- 첫 실행 관찰: 바이오/AI 비중 약 67%(지침 40~50% 초과), paywall·1차 출처 미확정 항목 "확인 필요" 표기, 일일/주간 경계 규칙 차기 명확화 과제.
