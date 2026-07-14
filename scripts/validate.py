#!/usr/bin/env python3
"""Validate the Korean Crypto x AI catalog.

Checks, in order:
  1. Structural — each data/resources/*.yaml against schema/resource.schema.json
     (uses the `jsonschema` package if installed; otherwise a pure-stdlib subset validator).
  2. Referential — category exists, id matches filename, ids and urls are unique.
  3. Semantic — risk_class is consistent with capabilities, maintainer affiliation is disclosed,
     watched/deprecated entries explain themselves, last_verified_at is a real, non-future date.

Exit code 0 = clean, 1 = errors found. Warnings never fail unless --strict is passed.
Only dependency is PyYAML; everything else is stdlib.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESOURCE_DIR = ROOT / "data" / "resources"
CATEGORIES_FILE = ROOT / "data" / "categories.yaml"
SCHEMA_FILE = ROOT / "schema" / "resource.schema.json"

# risk_class ordering and the minimum class each capability implies.
RISK_ORDER = {"R0": 0, "R1": 1, "R2": 2, "R3": 3}
CAPABILITY_MIN_RISK = {
    "public-read": "R0",
    "account-read": "R1",
    "trade": "R2",
    "withdrawal": "R3",
    "transfer": "R3",
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


# --- structural validation -------------------------------------------------

def _structural_stdlib(rid: str, data: dict, schema: dict, rep: Report) -> None:
    """Minimal, dependency-free check of the subset of JSON Schema we use."""
    props = schema["properties"]
    allowed = set(props)
    for key in data:
        if key not in allowed:
            rep.error(rid, f"unknown field '{key}' (additionalProperties is false)")
    for field in schema.get("required", []):
        if data.get(field) in (None, "", [], {}):
            rep.error(rid, f"missing required field '{field}'")
    for key, value in data.items():
        spec = props.get(key)
        if spec is None or value is None:
            continue
        _check_value(rid, key, value, spec, rep)


def _check_value(rid: str, key: str, value, spec: dict, rep: Report) -> None:
    t = spec.get("type")
    if t == "string" and not isinstance(value, str):
        rep.error(rid, f"'{key}' must be a string")
        return
    if t == "boolean" and not isinstance(value, bool):
        rep.error(rid, f"'{key}' must be a boolean")
        return
    if t == "array" and not isinstance(value, list):
        rep.error(rid, f"'{key}' must be a list")
        return
    if isinstance(value, str):
        if "enum" in spec and value not in spec["enum"]:
            rep.error(rid, f"'{key}'='{value}' not in {spec['enum']}")
        if "pattern" in spec and not re.search(spec["pattern"], value):
            rep.error(rid, f"'{key}'='{value}' fails pattern {spec['pattern']}")
        if "minLength" in spec and len(value) < spec["minLength"]:
            rep.error(rid, f"'{key}' shorter than {spec['minLength']} chars")
        if "maxLength" in spec and len(value) > spec["maxLength"]:
            rep.error(rid, f"'{key}' longer than {spec['maxLength']} chars")
    if isinstance(value, list):
        if spec.get("uniqueItems") and len(value) != len(set(map(str, value))):
            rep.error(rid, f"'{key}' has duplicate items")
        if "minItems" in spec and len(value) < spec["minItems"]:
            rep.error(rid, f"'{key}' needs at least {spec['minItems']} item(s)")
        items = spec.get("items", {})
        for item in value:
            _check_value(rid, f"{key}[]", item, items, rep)


def structural_validate(rid: str, data: dict, schema: dict, rep: Report) -> None:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        _structural_stdlib(rid, data, schema, rep)
        return
    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "(root)"
        rep.error(rid, f"schema: {loc}: {err.message}")


# --- semantic validation ---------------------------------------------------

def semantic_validate(rid: str, data: dict, today: dt.date, rep: Report) -> None:
    caps = data.get("capabilities", []) or []
    risk = data.get("risk_class")
    if risk and caps:
        implied = max((CAPABILITY_MIN_RISK[c] for c in caps if c in CAPABILITY_MIN_RISK),
                      key=lambda r: RISK_ORDER[r], default="R0")
        if RISK_ORDER.get(risk, 0) < RISK_ORDER[implied]:
            rep.error(rid, f"risk_class {risk} too low for capabilities {caps} (need >= {implied})")
    if risk == "R3" and not ({"withdrawal", "transfer"} & set(caps)):
        rep.warn(rid, "risk_class R3 but no withdrawal/transfer capability listed")

    if data.get("publisher_relation") == "maintainer" and not data.get("affiliation"):
        rep.error(rid, "publisher_relation=maintainer requires an 'affiliation' value (disclosure)")

    if data.get("status") in {"watch", "deprecated", "archived"} and not data.get("status_reason"):
        rep.warn(rid, f"status='{data.get('status')}' should include a 'status_reason'")

    lv = data.get("last_verified_at")
    if lv is not None and not isinstance(lv, str):
        # An unquoted YAML date (last_verified_at: 2026-07-14) parses as a date object,
        # not the string the schema requires. Structural validation already flagged the
        # type; don't also crash here.
        rep.error(rid, "last_verified_at must be a quoted string (YYYY-MM-DD), not a bare YAML date")
    elif lv:
        try:
            d = dt.date.fromisoformat(lv)
            if d > today:
                rep.error(rid, f"last_verified_at {lv} is in the future")
        except ValueError:
            rep.error(rid, f"last_verified_at '{lv}' is not a valid YYYY-MM-DD date")


# --- driver ----------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Validate the catalog data files.")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD) for reproducible CI")
    args = ap.parse_args()
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    rep = Report()
    schema = json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))
    categories = (load_yaml(CATEGORIES_FILE) or {}).get("categories", {})
    if not categories:
        rep.error("categories.yaml", "no categories defined")

    files = sorted(RESOURCE_DIR.glob("*.yaml"))
    if not files:
        rep.error("data/resources", "no resource files found")

    seen_ids: dict[str, str] = {}
    seen_urls: dict[str, str] = {}
    for path in files:
        rid = path.stem
        try:
            data = load_yaml(path)
        except yaml.YAMLError as exc:
            rep.error(rid, f"invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            rep.error(rid, "file does not contain a YAML mapping")
            continue

        structural_validate(rid, data, schema, rep)

        if data.get("id") != rid:
            rep.error(rid, f"id '{data.get('id')}' does not match filename '{rid}'")
        # Don't rely on truthiness here: an empty-string category is invalid but falsy,
        # and jsonschema (unlike the stdlib path) accepts "" as a string, so the two
        # validators must agree that "" is not a defined category.
        if "category" in data and data["category"] not in categories:
            rep.error(rid, f"category '{data['category']!r}' is not defined in categories.yaml")

        _id = data.get("id")
        if _id in seen_ids:
            rep.error(rid, f"duplicate id '{_id}' (also in {seen_ids[_id]})")
        elif _id:
            seen_ids[_id] = rid
        url = data.get("url")
        if url in seen_urls:
            rep.error(rid, f"duplicate url '{url}' (also in {seen_urls[url]})")
        elif url:
            seen_urls[url] = rid

        semantic_validate(rid, data, today, rep)

    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    n_ok = len(files) - len({e.split(':', 1)[0] for e in rep.errors})
    print(f"\n{len(files)} resource file(s) checked; "
          f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s).")

    if rep.errors or (args.strict and rep.warnings):
        return 1
    print("OK — catalog is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
