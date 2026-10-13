# Ebola 2026 funding tracker: pledged versus released

A sourced ledger of money announced for the 2026 Bundibugyo Ebola outbreak in
eastern DR Congo, set against the evidence on how much has actually been
disbursed. Live page: https://arvind-kumar-git.github.io/ebola-2026-funding-tracker/ (GitHub Pages, from the `main` branch root).

## Files

| File | What it holds |
|---|---|
| `data/pledges.csv` | One row per funding announcement: donor, recipient, date, amount, type, earmark, whether it is counted in the headline total, overlap reasoning, disbursement evidence, source link, confidence. |
| `data/appeals.csv` | Response plans and agency appeals: requirement, amount received, coverage, as-of date, source. |
| `data/disbursement_evidence.csv` | Every dated statement found about money released, unpaid workers, or accounting for funds. |
| `data/timeline.csv` | Headline snapshots of total pledged and total reported released, by date and reporter. |
| `template.html` | Page template. `__DATA__` is replaced by the JSON payload. |
| `build.py` | Reads the CSVs and writes `index.html`. Standard library only. |
| `index.html` | Generated. Do not edit by hand. |

## Updating

1. Edit the CSV. Quote every field; keep dates as `YYYY-MM-DD`; amounts in
   USD millions in `amount_usd_m`, with the original currency and amount in
   their own columns.
2. Set `counts_in_total` to `Y` only for new, non-overlapping money. Use `N`
   for restated cumulative totals, allocations by pooled funds that pass donor
   money through (CERF, CEPI, WHO's contingency fund), in-kind goods, and
   requests that have not been enacted. Explain any judgment in
   `overlap_note`.
3. Run `python3 build.py` and commit the CSV and the generated `index.html`
   together.

## Method and caveats

- Compiled on 2026-10-12 from donor press releases, Africa CDC, WHO, OCHA,
  UN agency appeal pages, the Congressional Research Service and news
  reporting. Figures were taken from search-engine extracts of those pages;
  the pages themselves could not be opened from the build environment.
  Verify a figure against its link before quoting it.
- Currency conversions use approximate mid-2026 rates: EUR 1.15, GBP 1.33,
  CHF 1.24, CAD 0.73, NOK 0.098, SEK 0.105, DKK 0.154.
- The headline sum of counted rows (about $1.98bn) sits below Africa CDC's
  count of $2.997bn and between that and the US State Department's "above
  $2bn". The three do not reconcile; the largest unexplained item is an EU
  figure above $568m reported by CRS.
- The last official figure for the share of pledges released is 13% (Africa
  CDC, June 25, 2026). No later figure has been published by any donor or
  agency.

## Known gaps

OCHA's Financial Tracking Service and the WHO appeal funding table were not
retrievable. Canada's reported C$80m, a US pledge for Kenya, and the Oct 2
figure of $227m mobilised for the first national plan each rest on a single
source. No audit of 2026 Ebola funds was found. If you can supply a disbursed
figure from a donor or agency, that is the most useful contribution.
