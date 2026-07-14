# Awesome Korean Crypto × AI [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

> 한국 암호화폐 × AI 리소스를 **검증 가능한** 형태로 모은 카탈로그 — LLM과 에이전트가 바로 연결할 수 있는 채널·도구·MCP 서버·데이터셋·매크로 피드·애그리게이터.

한국 암호화폐 시장은 (KOSPI ↔ BTC, 김치 프리미엄, BOK·KOSIS 매크로 피드, 거대한 유튜브·텔레그램 생태계 등) 고유의 리듬을 갖지만 영어권 도구와 LLM에는 거의 보이지 않습니다. 이 목록은 그 격차를 메우는 리소스를 정리합니다. 모든 항목은 사실 확인을 거쳐 검증 날짜와 근거 링크를 달고, 실행 **위험 등급**(R0–R3)으로 분류되어 — 에이전트가 라이브 키에 연결하기 전에 각 리소스가 무엇을 *할 수 있는지* 알 수 있습니다.

이 목록은 일부 항목을 직접 발행하기도 하는 [Mossland](https://moss.land) 생태계가 관리합니다. 해당 항목은 `maintainer`로 표시하고 투명성을 위해 [이해관계 공개](#메인테이너-관계-리소스--이해관계-공개) 섹션에 모았습니다.

[English](README.md) · 이 파일은 `data/`에서 자동 생성됩니다. 직접 수정하지 마세요.

**26개 항목** · 독립 19 · 메인테이너 관계 7 · active 23 · watch 3 · 스냅샷 2026-07-14

## 읽는 법

모든 항목에는 사람이 마지막으로 사실을 확인한 날짜(`검증`)와 다음 메타데이터가 붙습니다.

- **실행 위험 등급** — `R0` 공개 읽기 · `R1` 계정 읽기 · `R2` 주문 실행 · `R3` 자산 이동(출금·전송). 라이브 키에 연결하기 전 반드시 확인.
- **발행 관계** — `공식`(해당 주체가 직접 운영) · `공공`(정부·공공기관) · `커뮤니티`(제3자) · `메인테이너 관계`(이 카탈로그 운영자와 이해관계 있음, 하단 별도 공개).
- **상태** — `active` 검증됨 · `👁 관찰` 데이터 품질 저하/불확실 · `⚠ 지원종료` · `🗄 보관`.

## 목차

- [애그리게이터 & 버티컬 미디어](#애그리게이터--버티컬-미디어)
- [시그널 파이프라인 & 데이터셋](#시그널-파이프라인--데이터셋)
- [MCP 서버 (한국 시장)](#mcp-서버-한국-시장)
- [거래소 API](#거래소-api)
- [거래소 트레이딩 에이전트 & 스킬](#거래소-트레이딩-에이전트--스킬)
- [매크로 & 시장 데이터 API](#매크로--시장-데이터-api)
- [규제 & 컴플라이언스 데이터](#규제--컴플라이언스-데이터)
- [온체인 & 지갑 도구](#온체인--지갑-도구)
- [한국 암호화폐 미디어](#한국-암호화폐-미디어)
- [메인테이너 관계 리소스 & 이해관계 공개](#메인테이너-관계-리소스--이해관계-공개)
- [기여하기](#contributing)

---

## 애그리게이터 & 버티컬 미디어

한국 암호화폐 내러티브를 구조화해 LLM이 인용할 수 있게 만든 서비스.

- **[Alpha by Mossland](https://alpha.moss.land)** — 한국 암호화폐 × AI 버티컬 미디어 — 채널별 스탠스 분포, AI 데일리 브리핑, RAG Q&A, 공개된 AI 페르소나 디렉터리. 한국 유튜브·뉴스·매크로 피드 기반. _라이브 베타 — 홈페이지의 엔티티/토픽/이벤트 카운터는 0으로 표시되지만 /ask 백엔드에는 데이터가 채워져 있고, AI 페르소나 기능은 사전 출시('Phase 1.2, 카탈로그만')를 스스로 명시. 수치를 인용하기 전 현재 상태 확인 필요._<br>
  <sub>**👁 관찰** · `R0 · 공개 읽기` · 메인테이너 관계 · Mossland · web · free · MIT · 검증 2026-07-14</sub>

## 시그널 파이프라인 & 데이터셋

한국 크리에이터·뉴스·매크로 피드를 받아 정규화된 데이터로 내보내는 도구.

- **[SignalMap](https://signalmap.moss.land)** — 큐레이션된 한국 유튜브 논평(뉴스·매크로 포함)을 수집·요약하고 관점별(같은 방향/다른 방향/관찰)로 매핑해 채널·토픽·영상의 정규 저장소로 내보내는 다중 소스 내러티브 파이프라인. _홈페이지는 82개 채널로 표시하지만 /about 문구는 '유튜버 30명'이라고 함(오래된 문구). 암호화폐는 여러 추적 토픽 중 하나이며 유일한 초점이 아님._<br>
  <sub>`R0 · 공개 읽기` · 메인테이너 관계 · Mossland · web · free · 검증 2026-07-14</sub>

## MCP 서버 (한국 시장)

한국 시장 데이터를 MCP 클라이언트(Claude, Cursor, Cline 등)에 노출하는 Model Context Protocol 서버.

- **[Alpha MCP (land.moss/alpha-mcp)](https://github.com/MosslandOpenDevs/alpha-mcp)** — alpha.moss.land 위에 약 12개 도구를 노출하는 원격 MCP 서버 — 한국 유튜브 채널 스탠스 검색, AI 브리핑, 엔티티/토픽/이벤트 저장소, KR 매크로 스냅샷(BOK ECOS + FRED), AI 페르소나 디렉터리. Streamable-HTTP, 인증 불필요. _저하된 베타인 alpha.moss.land 업스트림에 의존 — 일부 도구(예: list\_topics, list\_events)가 현재 빈 결과를 반환._<br>
  <sub>**👁 관찰** · `R0 · 공개 읽기` · 메인테이너 관계 · Mossland · mcp · free · MIT · 검증 2026-07-14</sub>

## 거래소 API

한국 암호화폐 거래소의 공식 REST/WebSocket API. 공개 시세 엔드포인트는 인증 불필요(R0)지만, 동일 API의 인증 엔드포인트가 주문·출금까지 수행하므로 각 항목은 최대 권한(R3) 기준으로 표기한다. 데이터는 인증 불필요 엔드포인트를 쓰고, API 키 권한은 신중히 설정할 것.

- **[Bithumb API](https://apidocs.bithumb.com/)** — 주요 KRW 거래소 빗썸의 공식 API. 공개 API(시세·오더북·캔들)는 인증 불필요, 프라이빗 API(JWT)는 잔고·주문·출금 제공. 에이전트용 llms.txt 제공.<br>
  <sub>`R3 · 자산 이동` · 공식 · Bithumb · rest, websocket, llms-txt · free · 검증 2026-07-14</sub>

- **[Coinone API](https://docs.coinone.co.kr/)** — KRW 거래소 코인원(국내 점유율 약 10%)의 공식 API. 공개 시세·오더북 엔드포인트는 인증 불필요, 프라이빗 엔드포인트는 잔고·주문·출금 제공. llms.txt 제공.<br>
  <sub>`R3 · 자산 이동` · 공식 · Coinone · rest, websocket, llms-txt · free · 검증 2026-07-14</sub>

- **[GOPAX API](https://gopax.github.io/API/)** — KRW 거래소 고팍스의 공식 REST API. 공개 엔드포인트는 인증 없이 사용 가능, 프라이빗(키) 엔드포인트는 계정·거래·출금 제공. 2017년부터 유지되는 문서.<br>
  <sub>`R3 · 자산 이동` · 공식 · GOPAX (Streami) · rest · free · 검증 2026-07-14</sub>

- **[Korbit Open API](https://docs.korbit.co.kr/)** — 국내 최초 거래소 코빗의 공식 API(v2). REST + 웹소켓, 공개 시세 및 프라이빗 계정·주문·입출금. AI 에이전트 지향 — llms.txt / llms-full.txt, MCP 서버, 공식 Go CLI(korbit-cli) 제공. _GitHub 조직 korbit-official은 GitHub 인증되었으나 신규(2026-06 생성); CLI/MCP 도구는 검증된 것이 아니라 갓 출시됨._<br>
  <sub>`R3 · 자산 이동` · 공식 · Korbit · rest, websocket, llms-txt, mcp, cli · free · 검증 2026-07-14</sub>

- **[Upbit Open API](https://docs.upbit.com/)** — 국내 거래대금 1위(약 72%) 거래소 업비트의 공식 API. KRW 페어 시세·캔들·오더북·웹소켓. 공개 시세 엔드포인트는 인증 불필요, 인증 엔드포인트는 잔고·주문·출금까지 제공.<br>
  <sub>`R3 · 자산 이동` · 공식 · Upbit (Dunamu) · rest, websocket · free · 검증 2026-07-14</sub>

## 거래소 트레이딩 에이전트 & 스킬

한국 거래소가 배포하거나 거래소를 위해 만든 에이전트용 키트(MCP/Skills/CLI). 상당수가 주문·출금까지 수행할 수 있으므로, 실거래 키에 연결하기 전에 위험 등급과 필요한 권한을 반드시 확인할 것.

- **[Upbit Strategy Toolkit](https://github.com/upbit-official/upbit-strategy-toolkit)** — AI 에이전트(Claude Code, Codex, Cursor)와 대화하며 업비트 트레이딩 전략을 설계·백테스트하는 공식 툴킷. 백테스트 전용 — 실거래 권한 불필요(베타, v0.8.1).<br>
  <sub>`R0 · 공개 읽기` · 공식 · Upbit · cli, python · free · 검증 2026-07-14</sub>

- **[Bithumb AI Trade Kit](https://github.com/bithumb-official/bithumb-ai-trade-kit)** — 빗썸 API를 AI 에이전트가 사용하도록 만든 공식 툴킷 — 시세·계정 조회·주문·입출금. MCP 서버, 터미널 CLI, Claude/Cursor/VS Code/Windsurf용 Skills로 제공.<br>
  <sub>`R3 · 자산 이동` · 공식 · Bithumb · mcp, cli, skills · free · MIT · 검증 2026-07-14</sub>

- **[Upbit Agent Skills](https://github.com/upbit-official/upbit-agent-skills)** — 시세·잔고·주문·입출금을 아우르는 업비트 공식 Agent Skills. AI 에이전트를 실계정에 직접 연결한다.<br>
  <sub>`R3 · 자산 이동` · 공식 · Upbit · skills · free · 검증 2026-07-14</sub>

## 매크로 & 시장 데이터 API

한국 매크로 지표·시장 통계를 위한 공식/프리미엄 API.

- **[BOK ECOS](https://ecos.bok.or.kr/api/)** — 한국은행 경제통계시스템(ECOS) 공개 API — 기준금리, 국고채 금리, 원/달러, CPI, M2, 국민계정, 국제수지(834개 통계표, 100+ 주요지표). 가입 시 자동 발급되는 무료 인증키(테스트는 'sample' 키).<br>
  <sub>`R0 · 공개 읽기` · 공공 · Bank of Korea · rest, json · free · 검증 2026-07-14</sub>

- **[FRED — Korea, Republic of (South Korea)](https://fred.stlouisfed.org/categories/32286)** — 세인트루이스 연은 FRED의 대한민국 카테고리(32286) — 한국 매크로 시계열(금리·환율·물가·국민계정) 미러. 무료 API 키. (기존 목록의 32263은 한국이 아니라 'International Data' 상위 카테고리였음.)<br>
  <sub>`R0 · 공개 읽기` · 공공 · Federal Reserve Bank of St. Louis · rest, csv, json · free · 검증 2026-07-14</sub>

- **[KOSIS Open API](https://kosis.kr/openapi/)** — 국가통계포털(KOSIS) 공개 API — 인구·물가·고용·산업생산. 2025-10-01 통계청을 대체한 국가데이터처가 운영. SSO 로그인과 무료 인증키 필요. _2026년 API 변경 — HTTP 엔드포인트 종료(HTTPS 전용) 및 분당 호출 제한(~1,000회/분), 2026-02-05 공지·2026-07-09 개정._<br>
  <sub>`R0 · 공개 읽기` · 공공 · National Data Administration (국가데이터처) · rest, json · free · 검증 2026-07-14</sub>

- **[KRX Market Data (Data Marketplace / OPEN API)](https://data.krx.co.kr/)** — 한국거래소 공식 시장 데이터 — KOSPI/KOSDAQ, ETF/ETN/ELW, 채권·파생 일별 OHLCV(2010~). 무료지만 계정 필요: 전체 접근과 OPEN API(openapi.krx.co.kr)는 KRX 계정·약관 동의·승인된 인증키(약 1일 내 발급, 1년 유효) 필요.<br>
  <sub>`R0 · 공개 읽기` · 공공 · Korea Exchange (한국거래소) · rest, openapi, web · registration-required · 검증 2026-07-14 · [약관](https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO002.jsp)</sub>

## 규제 & 컴플라이언스 데이터

신고 사업자·시장 구조에 관한 공식 근거 데이터. 컴플라이언스를 고려하는 에이전트에 유용.

- **[FSC Virtual-Asset Market Survey (가상자산사업자 실태조사)](https://www.fsc.go.kr/no010101/86534)** — 금융위원회/FIU가 반기마다 발표하는 국내 신고 가상자산사업자 실태조사 — 시가총액·거래량·원화예치금·이용자 수·상장 종목·영업이익. 2025년 하반기판(신고사업자 27곳)은 2026-03-25 발표.<br>
  <sub>`R0 · 공개 읽기` · 공공 · Financial Services Commission (금융위원회) / FIU · web, pdf · free · 검증 2026-07-14</sub>

- **[KoFIU Registered VASP Status (가상자산사업자 신고현황)](https://www.kofiu.go.kr/)** — 금융정보분석원(KoFIU)이 VASP 게시판에 XLSX로 공개하는 신고 가상자산사업자 목록(약 반기마다 갱신, 최신 2026-06-30). 어떤 한국 거래소·수탁사가 합법적으로 신고되었는지에 대한 공식 기록.<br>
  <sub>`R0 · 공개 읽기` · 공공 · Korea Financial Intelligence Unit (금융정보분석원) · xls, web · free · 검증 2026-07-14</sub>

## 온체인 & 지갑 도구

한국 시장과 관련된 온체인 인프라 및 에이전트 도구.

- **[Kaia](https://github.com/kaiachain/kaia)** — 클레이튼(카카오 Ground X) × 핀시아 합병으로 만들어진 퍼블릭 EVM 호환 L1 블록체인. 아카이브된 klaytn/klaytn 저장소의 현행 후속. _아카이브된 klaytn/klaytn 저장소를 대체(2024-08 아카이브)._<br>
  <sub>`R0 · 공개 읽기` · 공식 · Kaia Foundation · json · free · LGPL-3.0 · 검증 2026-07-14</sub>

- **[Kaia Agent Kit](https://github.com/kaiachain/kaia-agent-kit)** — Kaia 위에서 AI 에이전트를 만드는 TypeScript 툴킷 — 플러그인 기반 온체인 조회(Kaiascan), DEX(DragonSwap) 연동, Web3 토큰 전송. _마지막 주요 커밋 2025-10(마지막 릴리스 v0.0.16, 2025-04); README에 미완성/깨진 링크 존재. 토큰 전송 가능(R3) — 지갑 키 필요._<br>
  <sub>**👁 관찰** · `R3 · 자산 이동` · 공식 · Kaia Foundation · free · MIT · 검증 2026-07-14</sub>

## 한국 암호화폐 미디어

한국어 암호화폐·블록체인 뉴스 매체.

- **[Block Media (블록미디어)](https://www.blockmedia.co.kr/)** — 디지털 금융 정책·산업·리서치·시장을 다루는 한국 블록체인/암호화폐 뉴스 매체('No.1 블록체인 뉴스' 표방).<br>
  <sub>`R0 · 공개 읽기` · 커뮤니티 · Block Media · web · free · 검증 2026-07-14</sub>

- **[Decenter (디센터)](https://www.decenter.kr/)** — 서울경제가 운영하는 한국 암호화폐/블록체인 뉴스 허브. 실시간 시세와 토큰화·스테이블코인·정책 보도.<br>
  <sub>`R0 · 공개 읽기` · 커뮤니티 · Seoul Economic Daily (서울경제) · web · free · 검증 2026-07-14</sub>

- **[The Token Post (토큰포스트)](https://www.tokenpost.kr/)** — 시장 데이터·아카데미·에어드롭 섹션을 갖춘 한국 블록체인/암호화폐 뉴스 매체('대한민국 No.1').<br>
  <sub>`R0 · 공개 읽기` · 커뮤니티 · TokenPost · web · free · 검증 2026-07-14</sub>

## 메인테이너 관계 리소스 & 이해관계 공개

> ℹ️ 이 카탈로그의 메인테이너(Mossland 생태계)가 발행한 리소스를 이해관계 공개 차원에서 모았다. 중립적 추천이 아니라 투명성을 위해 나열한다.

- **[Moss Coin (MOC) ERC-20 Contract](https://github.com/mossland/MossCoin-ERC20-2025)** — Mossland 자체 Moss Coin(MOC) ERC-20(2025) 토큰 컨트랙트 — OpenZeppelin 표준 ERC-20(Burnable, Permit(EIP-2612), Votes(ERC20Votes)), 5억 고정 발행, 소유자 없이 이더리움 메인넷 배포. CertiK(Skynet) 감사(2025-08). _범용 '온체인 도구'가 아니라 Mossland 단일 프로젝트의 토큰 컨트랙트. CertiK 감사는 링크만 제공(리포에 미포함)되며 '부분 해결(Partially Resolved)'로 표시된 중앙화 관련 지적 1건 존재._<br>
  <sub>`R0 · 공개 읽기` · 메인테이너 관계 · Mossland · free · MIT · 검증 2026-07-14</sub>

- **[Mossland Disclosures](https://disclosure.moss.land/)** — Mossland 프로젝트 공시 대시보드 — MOC 토큰 공급 스케줄, 유통량, 온체인/DAO 활동, 자료 로그(라이브 시장 데이터를 불러오는 SPA).<br>
  <sub>`R0 · 공개 읽기` · 메인테이너 관계 · Mossland · web · free · 검증 2026-07-14</sub>

- **[Mossland Projects Timeline](https://github.com/mossland/Projects)** — 2018년부터 Mossland이 개발한 프로젝트 목록과 현재 서비스 상태. _저장소에 선언된 라이선스 없음._<br>
  <sub>`R0 · 공개 읽기` · 메인테이너 관계 · Mossland · web · free · 검증 2026-07-14</sub>

- **[Mossland Whitepaper v3.1](<https://s3.ap-northeast-2.amazonaws.com/moss.land/whitepaper/Mossland+Whitepaper+ENG+(v3.1).pdf>)** — Mossland 프로젝트 백서(v3.1), 영/한 이중언어.<br>
  <sub>`R0 · 공개 읽기` · 메인테이너 관계 · Mossland · pdf · free · 검증 2026-07-14</sub>

---

## Contributing

항목은 `data/resources/`에 리소스당 YAML 파일 하나로 추가합니다. 형식과 규칙은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 모든 항목에는 근거 URL과 검증 날짜가 필요하며, CI가 스키마·중복·생성 결과를 검사합니다.

## License

카탈로그 메타데이터는 [CC0 1.0](LICENSE)로 배포됩니다. **CC0는 이 목록의 메타데이터에만 적용되며, 링크된 외부 콘텐츠·소프트웨어·데이터에는 적용되지 않습니다** — 각 리소스의 라이선스·약관을 따르세요.
