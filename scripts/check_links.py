#!/usr/bin/env python3
"""Health-check every URL in the catalog (primary `url`, `terms_url`, and `evidence_urls`).

Three outcomes per URL:
  * ALIVE       — 2xx/3xx, or a gated 401/403/405/429 (many KR gov/exchange sites block bots).
  * DEAD        — 404/410 (definitively gone). Only these fail CI under --fail-on-dead.
  * UNREACHABLE — 5xx, timeouts, DNS/connection errors that persist across retries. Reported
                  as warnings, never a hard failure — these are usually transient.

HEAD is only trusted when it succeeds: many servers answer HEAD with 404/403/405 while GET
works fine (Upbit's API is one), so any non-2xx HEAD is re-checked with GET before a verdict.
Each URL is also retried a few times to ride out transient blips.

Limitation: a parked/expired domain that serves an HTTP 200 landing page is indistinguishable
from a live site by status code alone, so it will read as ALIVE. Catching repurposed domains
(e.g. a former news site turned content farm) still needs a human — see CONTRIBUTING.md.

Stdlib only. Exit 0 by default (report-only); pass --fail-on-dead to fail CI on DEAD links.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import ssl
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESOURCE_DIR = ROOT / "data" / "resources"

UA = "Mozilla/5.0 (compatible; awesome-korean-crypto-ai link-check; +https://github.com/MosslandOpenDevs/awesome-korean-crypto-ai)"
TIMEOUT = 20
RETRIES = 3
_CTX = ssl.create_default_context()


def collect_urls() -> dict[str, set[str]]:
    """Return {url: {resource_id, ...}}."""
    urls: dict[str, set[str]] = {}
    for path in sorted(RESOURCE_DIR.glob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        rid = data.get("id", path.stem)
        for u in [data.get("url"), data.get("terms_url"), *(data.get("evidence_urls") or [])]:
            if isinstance(u, str) and u.startswith("http"):
                urls.setdefault(u, set()).add(rid)
    return urls


def _probe(url: str, method: str) -> tuple[str, str]:
    """One request. Returns (state, detail); state is alive | dead | gated | retry."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=_CTX) as resp:
            return "alive", str(resp.status)
    except urllib.error.HTTPError as e:
        c = e.code
        if c in (404, 410):
            return "dead", f"HTTP {c}"
        if c in (401, 403, 405, 429):
            return "gated", f"{c} (gated)"
        return "retry", f"HTTP {c}"  # 5xx, 400, etc. — retry
    except Exception as e:  # noqa: BLE001 - network errors are the point
        return "retry", type(e).__name__


def check(url: str) -> tuple[str, str, str]:
    """Returns (url, outcome, detail); outcome in {alive, dead, unreachable}.

    HEAD only short-circuits on success. Any non-alive HEAD is re-checked with GET, whose
    result is authoritative — so a server that 404s/403s HEAD but serves GET reads as ALIVE,
    and only a GET that returns 404/410 is DEAD."""
    detail = "unknown"
    for attempt in range(RETRIES):
        if _probe(url, "HEAD")[0] == "alive":
            return url, "alive", "200"
        state, detail = _probe(url, "GET")
        if state == "alive":
            return url, "alive", detail
        if state == "dead":
            return url, "dead", detail
        if state == "gated":
            return url, "alive", detail
        if attempt < RETRIES - 1:  # state == "retry"
            time.sleep(1.0 * (attempt + 1))
    return url, "unreachable", detail


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fail-on-dead", action="store_true", help="exit 1 if any link is DEAD (404/410)")
    args = ap.parse_args()

    urls = collect_urls()
    dead: list[tuple[str, str, set[str]]] = []
    unreachable: list[tuple[str, str, set[str]]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
        for url, outcome, detail in ex.map(check, urls):
            tag = {"alive": "OK  ", "dead": "DEAD", "unreachable": "WARN"}[outcome]
            print(f"{tag} {detail:>14}  {url}")
            if outcome == "dead":
                dead.append((url, detail, urls[url]))
            elif outcome == "unreachable":
                unreachable.append((url, detail, urls[url]))

    print(f"\n{len(urls)} url(s) checked — {len(dead)} dead, {len(unreachable)} unreachable.")
    for label, group in (("Dead", dead), ("Unreachable (transient?)", unreachable)):
        if group:
            print(f"\n{label}:")
            for url, detail, owners in group:
                print(f"  - {url}  [{detail}]  used by: {', '.join(sorted(owners))}")
    return 1 if (dead and args.fail_on_dead) else 0


if __name__ == "__main__":
    raise SystemExit(main())
