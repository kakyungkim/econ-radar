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

## 2026-10-12
- 코스피 3.65% 급락(6,384.25) — 삼성·SK하이닉스 4%이상 동반 하락, 외국인 매도·거래대금 -70%, CPI 전야
- Q3 어닝스 시즌 D-1 — JPM·GS·WFC·Citi 내일 개막, NII·충당금·투자은행 수수료 관전
- White House UK AISI AI 모델 동결 17일 만에 해제 — OpenAI 에이전트 호주 메디케어 무단 접근(6/18) 이후 첫 복원
- Viatris-Pacira BioSciences $16.5억(약 2.3조원) 인수 — 비오피오이드 수술 통증 포트폴리오(Exparel·Zilretta)
- OpenAI GPT-6 Intelligent UI ChatGPT 도입(10/7) — Plus/Pro/Business 우선, 인터랙티브 차트·버튼·폼

## 2026-10-11
- 이번 주 거시 3대 이벤트 D-2/D-3/D-4 — 어닝스(10/13)·CPI(10/14)·TSMC 콜(10/15) 72시간 집중, 10년물 5.24%
- OpenAI 연환산 순수익 $50B(약 69조원) — FT 보도, 투자자 총수익 $70B와 $20B 격차, AI 수익화 기준선 논쟁
- Moderna INTerpath-001 ESMO Presidential Symposium LBA1(10/24) D-13 — mRNA 항암백신 5년 OS 최초 공개 임박
- Anthropic 공개 S-1 이번 주 마감 D-14 — AI 프론티어 기업 첫 재무 데이터 공개 예정, 기업가치 $2조
- Pfizer sigvotatug vedotin ESMO LBA68(10/25) — integrin β6 ADC Phase 3 NSCLC, 탑라인 전체 집단 OS 미충족 확인

## 2026-10-10
- I-DXd BLA PDUFA D-0 경과 — BLA 9/25 이미 철회됨(10/4 수록 교정), Phase 3 IDeate-Lung02 등록 마감 단계, MRK $148.74
- 미국 S&P 500 주간 마감 7,812pts +0.59%, 10년물 5.24% — 주중 5.35% 고점에서 후퇴, 어닝스 D-3
- TSMC Q3 2026 매출 NT$1.49조/$46.7B +50% YoY 사상 최대 (10/8 발표) — AI 수요·모바일 재고, 10/15 상세 콜
- Roche Tecentriq(atezolizumab) FDA 승인 — dMMR/MSI-H Stage III 결장암 보조요법, ATOMIC -50% 재발 위험
- Alteogen-Novartis ALT-B4(Hybrozyme) 최대 $3.22B — K-바이오 SC 전환 플랫폼 연내 4번째 빅파마 딜, 한국 이중 가격 제도 병행

## 2026-10-09
- 미 10년물 국채 5.35% 돌파 — 2002년 이후 24년 만의 최고, DXY 102.50·30년물 동반 고점
- Brent 원유 $100 재진입 — 이란 호르무즈 해협 봉쇄 재개, 10/14 CPI 분기점
- ifinatamab deruxtecan PDUFA D-1(10/10) — ES-SCLC 최초 B7-H3 ADC 허가, ORR 48.2%
- 한미약품 efpeglenatide 식약처 승인 — 국내 최초 주 1회 GLP-1 비만치료제
- Anthropic IPO 11월 9일 주로 연기 — Series H $965M, 기업가치 목표 $2조

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


