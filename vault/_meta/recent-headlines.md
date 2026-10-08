---
type: meta
tags: [운영, dedup]
timestamp: 2026-07-21T18:00:00+09:00
publish: false
---
# 최근 헤드라인 (recent-headlines) — 중복 회피 기준

클라우드 routine은 과거 vault(raw·analysis·daily·topics)에 접근할 수 없다(로컬 전용, gitignore). 그래서 **이 파일이 "이미 다룬 뉴스" 기준선**이다. 데일리 생성 시 규칙:

1. **시작할 때** 이 파일을 읽는다. 여기 적힌 항목은 **이미 다뤘으므로 다시 헤드라인으로 올리지 않는다.** 단, 그 사건에 **새로운 후속 전개**(승인 결과·딜 종결·실적 등)가 나왔으면 "후속/업데이트"로만 짧게 다룬다.
2. **끝낼 때** 오늘 핵심 5가지 제목을 아래 `## YYYY-MM-DD` 블록으로 **맨 위에 추가**하고, **최근 7일치만 남기고** 그 이전 블록은 지운다. 이 파일도 함께 커밋한다.

> 사람이 손으로 만든 발행본도 여기 반영한다(아래 6/10·6/11은 수작업 발행분).

---

## 2026-10-08
- 삼성전자 Q3 2026 영업이익 107.4조원·매출 195조원 — 한국 기업 분기 최초 100조원 돌파, YoY +782.5%, DS(반도체) HBM4 주도
- FOMC 9월 의사록: r* 3.25%로 상향(기존 3.06%) — 장기 중립금리 구조적 상승 공식화, 10/28 추가 인상 확률 ~38~46%
- Shionogi IntraBio $2B 인수 — Aqneursa(NPC·A-T) 희귀질환, 2026년 합산 희귀질환 투자 $4.5B
- ifinatamab deruxtecan PDUFA D-2(10/10) — B7-H3 ADC ES-SCLC 최초 ADC 허가 이틀 전
- PepsiCo Q3 실적 발표 — 매출 $25.27B(컨센 $24.97B 상회)·코어 EPS $2.34·유기성장 +3.1%, 어닝스 시즌 개막

## 2026-10-07
- Genmab·AbbVie epcoritamab EPCORE DLBCL-2 Phase 3 성공 — bispecific 최초 frontline DLBCL PFS 입증 (HR=0.49, R-CHOP 대비 진행·사망 위험 51% 감소)
- 삼성전자 Q3 잠정실적 D-0 — 내일(10/8) 영업익 컨센 106.1조원·분기 최초 100조원 돌파 여부
- Q3 S&P 500 어닝스 시즌 D-6 — FactSet EPS +29.5% YoY, JPMorgan 10/13 개막
- NVIDIA Blackwell Ultra — 2026년 740만 유닛·CoWoS +40%, H2 공급 병목 지속
- INOVIO INO-3107 PDUFA D-23(10/30) — DNA 치료제 플랫폼 첫 상업화 관문

## 2026-10-06
- Marvell 투자자의 날 결과 — FY2028 $18B 가이던스·Google ASIC 워런트 최대 7% 구조 공개
- ifinatamab deruxtecan PDUFA D-4(10/10) — B7-H3 ADC, ES-SCLC 최초 ADC 허가 가능성
- Vaxcyte VAX-31 OPUS-1 Phase 3 성공 — 31가 폐렴구균 백신 도전자 등장, 주가 +32%
- Alector–Genentech BBB 딜 $100M+$1.17B — CNS GCase 효소 대체요법, ABC 플랫폼 권리 보유
- 삼성전자 Q3 잠정실척 D-1(10/7) — HBM4 매출 QoQ 3배 성장 검증 관건

## 2026-10-05
- bepirovirsen(GSK/Ionis) PDUFA D-21(10/26) — 만성 B형 간염 기능적 완치 첫 상업화 심사 카운트다운
- FOMC 10/28 추가 인상 50/50 — CPI 10/14 결정타, 거시 불확실성 정점
- Marvell 투자자의 날(10/6) — Google ASIC 파트너십 규모 첫 공개 예정, 커스텀 ASIC 독립 축 확인
- 한미약품 에페글레나타이드 국내 허가 심사 — 국내 최초 GLP-1 치료제 허가 진행
- Lilly 시총 $1.02조 돌파 + retatrutide TRIUMPH Phase 3 전 적응증 성공(최대 30% 감량)

## 2026-10-04
- I-DXd BLA 자진 철회 — FDA의 ADC 가속승인 경로 구조적 협소화, SCLC Phase 3 데이터 없이 불가 확인
- 삼성전자 Q3 잠정실적 이번 주(10/7~8) — 영업이익 116조원 컨센, HBM4 매출 전 분기 대비 3배 급증 예상
- Q3 어닝스 시즌 D-9 — JPMorgan·Goldman·J&J 10월 13일 개막, S&P 500 Q3 EPS 성장 +23% 기대
- BMS Cobenfy ADEPT-1 탑라인 2027 초 재연기 — 알츠하이머 정신증 이벤트 축적 지연
- Apple iOS 27.2 한국어 Siri AI 10월 배포 — 카카오·네이버·삼성 갤럭시 AI와 경쟁 구도 본격화

## 2026-10-03
- 9월 NFP +29,000 고용 쇼크 — 컨센서스 +84,000 대폭 하회, Fed 10월 동결 기대 강화
- Anthropic 기업공개(IPO) 비공개 신청 — $965B 밸류에이션, 연매출 런레이트 $47B, 10월 상장 목표
- Novo Nordisk 2026 매출 최대 -13% 전망 — CagriSema 티르제파타이드 대비 열세(23% vs 25.5%), 경구 Wegovy 호조
- bepirovirsen(GSK/Ionis) PDUFA D-23(10/26) — 만성 B형 간염 최초 기능적 완치 후보, 결정 임박
- 바이오테크 M&A 2026 1분기 $840억 — 전년 $444억 대비 89% 급증, ADC·비만·면역종양 3축

## 2026-10-02
- Micron Q4 FY2026 데이터센터 $11.5B·전년 동기 7.5배 어닝스 빅 비트 — AI 메모리 사이클 FY2027 연장 확인
- 9월 고용보고서 오늘(10/2) 발표 — ADP 선행 +90K, BLS 컨센 +93~98K, Fed 10월 인상 경로 분수령
- Lilly Zepbound·Foundayo 미국 3대 PBM 전면 급여 10/1 발효 — GLP-1 보험 장벽 해소, 수요 병목 이동
- BMS Camzyos 소아 oHCM FDA 승인(9/30) — 심근 미오신 억제제(CMI) 최초 소아 적응증 획득
- GSK·Ionis bepirovirsen PDUFA 10/26 — 전 세계 2억4,000만 만성 B형 간염 환자 대상 기능적 완치 후보


