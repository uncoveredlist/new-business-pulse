# New Business Pulse

Daily aggregate counts of new business filings in Colorado, New York, Pennsylvania, Connecticut and Texas, scored for commercial insurance need. Published by [UncoveredList](https://uncoveredlist.com/pulse).

**Last updated:** Oct 22, 2026, 8:50 PM CT. `data/pulse-latest.csv` covers filing dates 2026-09-22 to 2026-10-21 (CO 2026-10-10..2026-10-21, NY 2026-10-10..2026-10-19, PA 2026-09-22..2026-10-01, CT 2026-10-10..2026-10-21, TX 2026-10-03..2026-10-17).

- **Live report:** https://uncoveredlist.com/pulse
- **Methodology:** https://uncoveredlist.com/methodology
- **Free county sample (25 leads, no card needed):** https://uncoveredlist.com/free-sample
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see [LICENSE](LICENSE))
- **Author:** UncoveredList Team · support@uncoveredlist.com

> **Cite as:** Source: UncoveredList, New Business Pulse (October 2026), uncoveredlist.com/pulse.

## What the Pulse is

The New Business Pulse counts new businesses that appear in official state records, broken down by state, industry, top county or city, and filing date, and shows how many score as likely commercial insurance buyers. It is built from the same pipeline that powers UncoveredList, a daily list of newly registered businesses for commercial P&C agents.

**Business-level public records only.** This dataset holds aggregate counts, never individual business records. There are no business names, owner, officer or registered-agent names, street addresses, filing or entity IDs, phone numbers, emails or per-business scores. The smallest geography is a county (NY, PA, TX) or a city (CO, CT), and only the top areas per state with at least 5 businesses are listed.

## Files

| File | Contents | Updated |
|---|---|---|
| `data/pulse-latest.csv` | Rolling last 30 days of filing dates (`edition` = `rolling-30d`) | Daily, around 7:30 AM CT, committed only when the numbers change |
| `data/pulse-2026-10.csv` | October 2026 edition, frozen. Same file as the [October 2026 report](https://uncoveredlist.com/pulse/october-2026) CSV | Never (one frozen file per monthly edition) |
| `datapackage.json` | [Frictionless Data](https://specs.frictionlessdata.io/data-package/) descriptor with the table schema | |
| `scripts/update_data.py` | Archives each published monthly edition from https://uncoveredlist.com/pulse/latest.csv | Weekly GitHub Action |

Note: `data/pulse-latest.csv` in this repo is the rolling 30-day file. The site's `/pulse/latest.csv` serves the latest **monthly edition**, which is archived here as `data/pulse-YYYY-MM.csv`.

## The five states and their data windows

| State | Source | What a record is |
|---|---|---|
| Colorado | Colorado Secretary of State | Business entity formations (domestic entities in Good Standing) |
| New York | New York Department of State, Division of Corporations | Articles of Organization and Certificates of Incorporation |
| Pennsylvania | Pennsylvania Department of State, Bureau of Corporations | New domestic business registrations (foreign registrations excluded) |
| Connecticut | Connecticut Secretary of the State | New business registrations, with state-reported NAICS code |
| Texas | Texas Comptroller of Public Accounts | New sales-tax permits for Texas locations (not Secretary of State formations; includes new locations of existing businesses) |

Each state has its own date window, given in the `window_start` / `window_end` columns. States publish on different schedules: Colorado, New York and Connecticut usually 1–2 days after filing; Pennsylvania's open-data file lags about two weeks; Texas permits refresh about weekly. Today is never counted, and incomplete first or last days (under 40% of that state's typical day) are left out, so the rolling file's windows are shorter than 30 days for lagging states. **Compare shares, not raw counts, across states.**

**October 2026 edition** (`pulse-2026-10.csv`): 19,733 new businesses, 6,730 scored 70+ and 4,229 Hot. Windows: Pennsylvania Sep 17–Oct 2 (16 days), Texas Oct 3–17 (15 days), Colorado and Connecticut Oct 10–18 (9 days), New York Oct 10–16 (7 days). Overall Sep 17–Oct 18, 2026. It is not a full month.

## Data dictionary

| Column | Type | Meaning |
|---|---|---|
| `edition` | string | `YYYY-MM` for a monthly edition, `rolling-30d` for the rolling file |
| `level` | string | Row type: `all_states`, `all_states_industry`, `state`, `state_industry`, `state_top_area`, `state_filing_date` |
| `state` | string | `CO`, `NY`, `PA`, `CT`, `TX`, or `ALL` |
| `state_name` | string | State name (list of states for `ALL`) |
| `window_start` / `window_end` | date | First and last filing (formation or permit) dates counted |
| `industry` | string | Industry group (industry rows only): one of 20 segments or `Unclassified` |
| `area_type` / `area` | string | `county` (NY, PA, TX) or `city` (CO, CT) and its name (`state_top_area` rows only) |
| `filing_date` | date | Single filing day (`state_filing_date` rows only) |
| `new_businesses` | integer | New businesses counted |
| `scored_70_plus` | integer | Of those, how many scored 70 or higher (high need) |
| `hot` | integer | Of those, how many are in the Hot tier |

Blank cells mean the column doesn't apply to that row's `level`. **Filter on `level` before summing**, or you'll double count.

## Method summary

Full detail: https://uncoveredlist.com/methodology

- **Sources.** Public records from each state's official open-data portal, read through public APIs, read-only. No logins, no paid data.
- **Filters.** Before counting, we remove holding and investment shells, registered-agent mail drops, New York filings served only through an agent company, shared virtual-office addresses (10 or more new entities at one address), and out-of-state or inactive entities.
- **Industry tags.** Assigned in three steps: the state NAICS code where the state reports one (Connecticut, Texas), keyword rules on the business name, then AI review that confirms or corrects the rules' answer. Low-confidence AI guesses never replace the rules, and names that say nothing about the business stay `Unclassified`.
- **Score.** A rules-based 1–100 commercial insurance need score: a base score by industry, plus adjustments from the record (for example a state NAICS code, a physical address, a new USDOT registration, a pending liquor license; minus points for PO-box-only addresses, low-confidence tags, nonprofits and Texas new locations of existing permit holders). **High need = 70+.** **Hot** = a business in a high-urgency industry (trucking, construction, restaurants and bars, healthcare, auto services, security and staffing) scoring 75 or more. Super hot is not reported in the Pulse.

## Limits

- **Short history.** Our database starts with filings from mid-September 2026 (Pennsylvania) and October 2026 (other states), so there are no month-over-month trends yet.
- **Windows differ by state** and are often shorter than the period requested.
- **Texas counts permits**, not formations, including new locations of existing businesses.
- **Industry tags can be wrong**, and some businesses can't be classified from their name alone (13% `Unclassified` in October 2026).
- **Filtering is rules-based**, so some shells and mail drops get through and some real businesses are removed.
- **Scores reflect what each state publishes.** States that report NAICS codes or more fields can score higher for the same industry. Connecticut's 70+ share is not comparable across Oct 19, 2026, when a bonus for a published business email was removed.
- **Public records have errors and delays**, and states can change or stop a feed.
- **Not advice.** Scores are estimates for prioritization, not insurance, underwriting, legal or compliance advice.

## How to cite

> Source: UncoveredList, New Business Pulse (October 2026), uncoveredlist.com/pulse.

For the rolling file, cite the same way and add the date window you used. Media and research questions: support@uncoveredlist.com.

## License

Data and documentation are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). You may share and adapt the data for any purpose, including commercially, with attribution using the citation above. See [LICENSE](LICENSE).
