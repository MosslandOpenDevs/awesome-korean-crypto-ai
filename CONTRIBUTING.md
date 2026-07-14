# Contributing

This is a **data-driven, verifiable catalog**. The `README.md`, `README.ko.md`, and `catalog.json` files are **generated** — never edit them by hand. You edit the data under `data/`, run the build, and commit the result.

## Repository layout

```
data/resources/*.yaml     # one resource per file (the source of truth)
data/categories.yaml      # category definitions and ordering
schema/resource.schema.json
scripts/validate.py       # schema + referential + semantic checks
scripts/build.py          # regenerates README.md, README.ko.md, catalog.json
scripts/check_links.py    # URL health check (used by the weekly job)
README.md / README.ko.md  # GENERATED — do not edit
catalog.json              # GENERATED — machine-readable, for agents
ARCHIVE.md                # removed/retired entries and why
```

## Add or change a resource

1. Copy an existing file in `data/resources/` to `data/resources/<your-id>.yaml`. The filename (minus `.yaml`) must equal the `id` field and be unique.
2. Fill in every required field (see the schema and the checklist below).
3. Regenerate and validate:
   ```bash
   pip install pyyaml            # only dependency; jsonschema is optional but recommended
   python scripts/validate.py    # must pass
   python scripts/build.py       # regenerates README.md, README.ko.md, catalog.json
   ```
4. Commit the YAML **and** the regenerated files together. CI fails if they drift.

## Required fields

| Field | Notes |
|-------|-------|
| `id` | kebab-case, matches filename, unique |
| `name`, `url` | `url` must be `http(s)` |
| `category` | must be a key in `data/categories.yaml` |
| `publisher`, `publisher_relation` | `official` / `government` / `community` / `maintainer` |
| `description`, `korea_relevance`, `ai_utility` | what it is, why it's Korea-relevant, why an agent/LLM cares |
| `risk_class` | `R0` public read · `R1` account read · `R2` places orders · `R3` moves funds |
| `cost`, `status` | `status`: `active` / `watch` / `deprecated` / `archived` |
| `last_verified_at` | ISO date you personally confirmed the facts — not a guess |
| `evidence_urls` | at least one URL that substantiates your claims |

Optional but encouraged: `description_ko`, `interfaces`, `capabilities`, `auth`, `license`, `terms_url`, `status_reason`, `featured`.

## Rules the validator enforces

- **`risk_class` must match `capabilities`.** If `capabilities` includes `withdrawal` or `transfer`, the class must be `R3`; `trade` implies at least `R2`; `account-read` at least `R1`.
- **Maintainer affiliation must be disclosed.** `publisher_relation: maintainer` requires an `affiliation` value, and such entries belong in the `disclosures` category.
- **No future or fabricated verification dates.** `last_verified_at` cannot be in the future.
- **No duplicate `id`s or `url`s** — both are errors.

## What belongs here

- Korean-market crypto/AI resources an LLM or agent can actually use: APIs, MCP servers, agent kits, datasets, official statistics, and quality Korean-language media.
- Prefer **primary, official** sources. Every entry must be independently verifiable.

## What does not

- Dead, parked, or repurposed domains (we removed one that became SEO spam — see `ARCHIVE.md`).
- Affiliate/referral links; single-product self-promotion with no ecosystem value.
- Unverifiable claims, or anything you have not actually checked.
- Superlatives without scope or date (`largest`, `free`, `audited`, `full`). Say *largest by domestic volume (~72%)*, *free but registration-gated*, *audited by X, Aug 2025, one finding partially resolved*.

## Risk & disclosure conventions

- If a resource can place orders or move funds (R2/R3), the description must say so plainly. Do not bury withdrawal capability.
- MCP servers and tools that return external text are **read-only ≠ trusted** — flag that downstream content is untrusted input.

Open an issue first if you're unsure whether something fits.
