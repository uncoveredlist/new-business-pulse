# New Business Pulse

Open, aggregate counts of new business filings in Colorado, New York, Pennsylvania, Connecticut and Texas, published by [UncoveredList](https://uncoveredlist.com/pulse).

**Author:** UncoveredList Team
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
**Live report:** https://uncoveredlist.com/pulse

> **Credit line (required by CC BY 4.0):**
> Source: UncoveredList, New Business Pulse, uncoveredlist.com/pulse (CC BY 4.0)

## What's in this repo

| File | Contents |
|---|---|
| `data/pulse-latest.csv` | The current edition. Mirrors https://uncoveredlist.com/pulse/latest.csv |
| `data/pulse-YYYY-MM.csv` | One frozen file per monthly edition (e.g. `pulse-2026-10.csv`) |
| `datapackage.json` | [Frictionless Data](https://specs.frictionlessdata.io/data-package/) descriptor with the table schema |
| `scripts/update_data.py` | Refreshes `data/` from the live CSV |
| `.github/workflows/update-data.yml` | Runs the refresh weekly and commits only if the data changed |

## Totals only. No personal data

Every row is an aggregate count. The files contain **no business names, owner or agent names, street addresses, filing or entity IDs, phone numbers, emails, or individual lead scores**. The smallest geography is a county (NY, PA, TX) or a city (CO, CT), and only the top areas per state are listed.

## Data sources

Counts are compiled from public state records published on official state open-data portals:

- **Colorado:** Secretary of State business entity filings
- **New York:** Department of State corporation and business entity filings
- **Pennsylvania:** Department of State business entity filings
- **Connecticut:** Secretary of the State business registrations
- **Texas:** Comptroller of Public Accounts new sales-tax permits

Each state covers its own filing window; see the `window_start` / `window_end` columns. The October 2026 edition spans 2026-09-17 to 2026-10-18 overall (PA Sep 17–Oct 2 · TX Oct 3–17 · CO Oct 10–18 · CT Oct 10–18 · NY Oct 10–16).

Methodology: https://uncoveredlist.com/pulse/october-2026

## Columns

| Column | Meaning |
|---|---|
| `edition` | Pulse edition (YYYY-MM) |
| `level` | Row type: `all_states`, `all_states_industry`, `state`, `state_industry`, `state_top_area`, `state_filing_date` |
| `state` / `state_name` | CO, NY, PA, CT, TX, or ALL |
| `window_start` / `window_end` | First and last filing dates counted |
| `industry` | One of 21 industry groups (industry rows only) |
| `area_type` / `area` | `county` (NY, PA, TX) or `city` (CO, CT) (top-area rows only) |
| `filing_date` | Single filing day (`state_filing_date` rows only) |
| `new_businesses` | New businesses filed |
| `scored_70_plus` | Of those, how many scored 70+ for commercial insurance need |
| `hot` | Of those, how many fall in UncoveredList's Hot tier |

Blank cells mean the column doesn't apply to that row's `level`. Always filter on `level` before summing, or you'll double count.

## Updates

A GitHub Action checks https://uncoveredlist.com/pulse/latest.csv every Monday and commits only when the data has changed. To refresh by hand:

```bash
python3 scripts/update_data.py
```

## How to cite

> UncoveredList Team. *New Business Pulse* (October 2026). UncoveredList, uncoveredlist.com/pulse. Licensed under CC BY 4.0.

## License

Data and documentation are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE). You may share and adapt the data for any purpose, including commercially, as long as you give credit using the credit line above.
