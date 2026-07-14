# Maintainers

This catalog is only as good as its verification cadence. To stay honest it needs named owners and a review schedule — not just an initial dump.

## Curators

| Role | Owner | Responsibility |
|------|-------|----------------|
| Primary curator | _@TODO — fill in a GitHub handle_ | Reviews PRs, runs the weekly health job, updates `last_verified_at`, owns the gate decisions below. |
| Backup curator | _@TODO — fill in a second handle_ | Covers when the primary is unavailable; a single-owner catalog is a bus-factor risk. |

> Replace the `@TODO`s and the placeholder in [`.github/CODEOWNERS`](.github/CODEOWNERS) with real handles (or a `@MosslandOpenDevs/…` team) before relying on required reviews.

Maintained by the [Mossland](https://moss.land) ecosystem. Mossland also publishes some listed resources; those are marked `maintainer` and disclosed in the README's Disclosures section and in `ARCHIVE.md`.

## Verification policy

- Every entry carries a `last_verified_at` date and `evidence_urls`. "Verified" means a human actually opened the sources and confirmed the claims on that date.
- The weekly health job (`.github/workflows/health.yml`) checks every URL. Repeated failures move an entry to `status: watch`; prolonged failure makes it an archive candidate (see gates).

## Health → status policy

| Signal | Action |
|--------|--------|
| 3 health failures over ~7 days | Set `status: watch` with a `status_reason`. |
| ~30 days unrecovered | Open an "archive candidate" issue; do **not** auto-delete. A human decides and records it in `ARCHIVE.md`. |
| Recovered + re-verified | Promote back to `active` and bump `last_verified_at`. |

## Maintenance gates

Dates for this reboot (`v0.2`), set 2026-07-14:

| Date | Gate |
|------|------|
| 2026-08-13 | New official entries reflected; first CalVer snapshot tagged. |
| 2026-09-12 | 60-day gate — CI green, primary **and** backup curator named, every entry has evidence URLs, ≥ 2/3 of entries independent (non-maintainer). |
| 2026-10-12 | 90-day gate — ≥ 90% of entries verified within the last 90 days, ≥ 2 reviews/month sustained. |

If the 90-day gate is missed, the honest options are (1) tag a final snapshot and archive, or (2) rename to a scoped "Mossland Korean Crypto × AI Ecosystem Map." Do not let it drift as a stale "awesome" list.

Current independence: **19 / 26** entries are independent (official / government / community); **7** are maintainer-affiliated — above the 2/3 bar.
