#!/usr/bin/env python3
"""Refresh data/ from the live New Business Pulse CSV (stdlib only).

Writes data/pulse-latest.csv and data/pulse-<edition>.csv. Refuses to write
if the header changes or columns that could hold personal data show up.
"""
import csv
import io
import pathlib
import sys
import urllib.request

URL = "https://uncoveredlist.com/pulse/latest.csv"
DATA = pathlib.Path(__file__).resolve().parent.parent / "data"
EXPECTED = [
    "edition", "level", "state", "state_name", "window_start", "window_end",
    "industry", "area_type", "area", "filing_date",
    "new_businesses", "scored_70_plus", "hot",
]
LEVELS = {"all_states", "all_states_industry", "state", "state_industry",
          "state_top_area", "state_filing_date"}


def main() -> int:
    req = urllib.request.Request(URL, headers={"User-Agent": "new-business-pulse-updater"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        text = resp.read().decode("utf-8")

    rows = list(csv.reader(io.StringIO(text)))
    if not rows or rows[0] != EXPECTED:
        print(f"Unexpected header: {rows[0] if rows else None}", file=sys.stderr)
        return 1
    body = rows[1:]
    if not body:
        print("CSV has no data rows", file=sys.stderr)
        return 1
    editions = {r[0] for r in body}
    if len(editions) != 1:
        print(f"Expected one edition, got {sorted(editions)}", file=sys.stderr)
        return 1
    bad = [r for r in body if len(r) != len(EXPECTED) or r[1] not in LEVELS]
    if bad:
        print(f"{len(bad)} malformed rows, e.g. {bad[0]}", file=sys.stderr)
        return 1
    if any("@" in cell for r in body for cell in r):
        print("Found an '@' in the data; refusing to write", file=sys.stderr)
        return 1

    edition = editions.pop()
    DATA.mkdir(exist_ok=True)
    for name in ("pulse-latest.csv", f"pulse-{edition}.csv"):
        (DATA / name).write_text(text, encoding="utf-8", newline="")
    print(f"Wrote edition {edition}: {len(body)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
