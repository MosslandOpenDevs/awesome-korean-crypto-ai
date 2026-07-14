# Archive

Entries removed, corrected, or retired, with the reason and date. Kept for provenance so the same mistakes aren't re-added.

## Removed — 2026-07-14 (v0.2 verified reboot)

- **CoinDesk Korea** (`coindeskkorea.com`) — **removed.** The domain no longer hosts crypto journalism. As of 2026-07-14 it serves generic SEO/content-farm articles (lab equipment, defense stocks, health, pet-groomer certifications, celebrity gossip) on a GeneratePress/WordPress build; the original news CMS is gone, and even legacy article URLs (e.g. `/news/articleView.html?idxno=91064`) now render the same spam. A normally-responding but repurposed domain is more dangerous in a catalog than a 404. If a CoinDesk Korean-language source is wanted again, verify a live property before re-adding.
- **`r/koreanstocks`** — **removed.** A Korean *equities* forum with only incidental crypto content; out of scope for a crypto × AI catalog.
- **Empty "Korean YouTube Channels" section** — **removed.** It contained no verified entries, only a "coming soon" placeholder. It will return when a verified whitelist export (e.g. from SignalMap) exists, one channel = one entry with evidence.
- **"Communities → Mossland (`moss.land`)"** — **not a neutral community entry.** Mossland is this catalog's maintainer; its resources were moved to the **Disclosures** section and marked `publisher_relation: maintainer` for transparency.

## Corrected — 2026-07-14

- **FRED "Korean Series"** — the old link pointed at category **32263**, which is FRED's **"International Data"** parent category, not Korea. Corrected to **32286 — "Korea, Republic of (South Korea)."**
- **Klaytn** (`github.com/klaytn`) — the core repo `klaytn/klaytn` was **archived 2024-08**. Replaced by its active successor **[Kaia](https://github.com/kaiachain/kaia)** (Klaytn × Finschia merger).
- **KOSIS operator** — updated from Statistics Korea (통계청) to the **National Data Administration (국가데이터처)**, which took over on 2025-10-01, and flagged the 2026 API changes (HTTPS-only, per-minute call limits).
- **KRX "free"** — corrected to **registration-gated and non-commercial-only**; the OPEN API (`openapi.krx.co.kr`) needs an account and an approved auth key.
- **MOC contract "On-chain tooling / Audited"** — reframed honestly as **Mossland's own token contract**, moved to Disclosures, with the CertiK audit described including its one **"Partially Resolved"** centralization finding (audit linked, not hosted in-repo).
- **LICENSE** — replaced a truncated CC0 excerpt (missing §§1–4) with the **full CC0 1.0 legal text**, and clarified that CC0 covers only the catalog metadata, not the linked resources.

## Watch list (in `data/`, `status: watch`)

Kept but flagged as degraded/uncertain, pending recovery:

- **Alpha by Mossland**, **Alpha MCP** — live beta with degraded upstream data (homepage counters render 0; some MCP tools return empty; AI personas self-declared pre-launch "Phase 1.2").
- **Kaia Agent Kit** — last significant commit 2025-10; README has incomplete/broken links; R3 (token transfer).

Promotion to `active` requires a fresh verification once the upstream recovers.
