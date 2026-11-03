# Skyscrapers by District

A building-by-building tally of skyscrapers (≥150 m) assigned to the urban
district / borough / ward they stand in, aimed at a first-of-its-kind global
ranking of districts rather than cities.

Copy taken from the Claude project **"Skyscrapers in Cities and Districts"** on
2026-09-08. Layout mirrors the project's own `claude/` + `data/` split.

---

## Start here

| File | What it is |
|---|---|
| `claude/District_skyscrapers_v2.md` | **The report.** Second edition — 58 metropolitan units, 416 sub-city units, global ranking, methodology, caveats. |
| `claude/district-tally-progress.md` | Status, headline counts, method summary, open items for the next pass. |
| `data/skyscrapers_150m_master_geocoded.csv` | **The master dataset.** 6,237 buildings, every one geocoded and assigned to a district, with city/district/global rank columns. |

## The dataset

`data/skyscrapers_150m_master_geocoded.csv` — 6,237 buildings across 58 cities
and 20 countries. 25 columns: identity (`id`, `name`, `city`, `country`),
placement (`district`, `sub_area`, `lat`, `lon`, `coord_precision`,
`coord_source`, `osm_way`), building facts (`status`, `year`, `height_m`,
`height_confirmed`, `floors`, `function`, `material`) and precomputed
`rank_city` / `rank_district` / `rank_global`.

Status split: 5,775 completed · 269 under construction · 135 architecturally
topped out · 58 structurally topped out. **The published ranking counts
completed buildings only** — filter on `status == "Completed"`.

`data/skyscrapers_150m_unplaced.csv` — 184 buildings that could not be geocoded
to a district. Same ids, no coordinates. Master + unplaced = 6,421 buildings,
the full CTBUH-derived pool.

## Per-city working files

- `*_150m.csv` — CTBUH-derived building lists: Bangkok, Busan, Istanbul,
  Jakarta, Manila, Moscow, Osaka, Seoul, Singapore, Sydney, Toronto.
- `*_150m_wikipedia.csv` — Wikipedia-inclusive variants (Bangkok, Guangzhou,
  Metro Manila, Seoul), kept because Wikipedia and CTBUH disagree on inclusion
  for these cities.
- District breakdowns — `shanghai_200m_by_district.csv`,
  `guangzhou_150m_by_district.csv`, `shenzhen_200m_by_district.csv`, plus the
  `*_150_200_band.csv` files covering the 150–200 m band for Shanghai and
  Shenzhen, and `hongkong_saikung_ytm.csv` for Sai Kung / Yau Tsim Mong.
- `ctbuh_city_counts.csv` — CTBUH's own published city totals, used to
  reconcile the tally (exact match for 40 of 56 cities, within 1–5 for the rest).
- `*_notes.md` — per-city research notes and `discrepancies_notes.md` for
  unresolved source conflicts.

## Method, in one paragraph

Building lists come from the CTBUH / Skyscraper Center "Explore Data" tool,
sliced by city × completion year (× function × material where a year exceeded
the 25-row cap); index-only records were checked on individual building pages,
excluding 26 buildings at 149.x m and 23 with no confirmed height. Coordinates
come from CTBUH's public Algolia index (`SC_Buildings`, `_geoloc`) for 6,106
buildings, with Nominatim and targeted research covering the rest. Districts
were assigned by point-in-polygon against OpenStreetMap boundaries via Overpass
`is_in` (5,123 buildings), with geoBoundaries polygons as fallback and
cross-check, Nominatim reverse geocoding for cities without formal districts
(Dubai, Kuala Lumpur, Miami), and 155 buildings placed by hand.

## What was cleaned up in this copy

Three sets of near-duplicates existed in the project. The better copy is in the
main tree; the superseded one is in `_superseded/` rather than deleted.

- **`shanghai_200m_by_district.csv`** — the `_v2` pass won and now carries the
  plain name. Same 70 buildings, but it adds a `source` column and 57 corrected
  values (filled-in heights, and Shanghai SK Group Tower moved Xuhui → Pudong).
  Old copy: `_superseded/shanghai_200m_by_district_v1.csv`.
- **`guangzhou_150m_by_district.csv`** — likewise. `_v2` adds a `source` column,
  7 buildings the first pass missed (Nansha Yuexiu IFC towers A and B, JOYY HQ,
  Vipshop HQ South, Oppein International Plaza, 37 Interactive Global HQ, Window
  of Guangzhou Zone B) and 214 corrected values.
  Old copy: `_superseded/guangzhou_150m_by_district_v1.csv`.
- **`skyscrapers_150m_by_district_1.csv`** — the earlier single-file export of
  all 6,421 buildings, 19 columns. Verified to be exactly
  `skyscrapers_150m_master_geocoded.csv` + `skyscrapers_150m_unplaced.csv`,
  which supersede it with 25 columns including the rank fields. Kept in
  `_superseded/` only as the last known state of the combined export.

Nothing else was renamed, and no file was dropped.

## Known open items

- 184 buildings in `skyscrapers_150m_unplaced.csv` still need addresses —
  mostly 1990s–2010s towers in Shenyang, Chengdu, Wuhan, Tianjin and Suzhou.
- Two counts drifted between the report and the current master: Nanshan
  (Shenzhen) reads 189 in `District_skyscrapers_v2.md` but 186 in the master,
  and Luohu 76 vs 75. The other headline districts reconcile exactly
  (Manhattan 294, Futian 127, Sai Kung 122, Old Toronto 100, Pudong 92,
  Tianhe 87). Worth resolving before the report is cited.
- `District_skyscrapers_v2.xlsx` — the workbook with live COUNTIFS over the
  6,421-building sheet — was only ever delivered as a chat attachment and is
  not in the project. It can be rebuilt from
  `skyscrapers_150m_master_geocoded.csv`.
- Re-run in roughly a year: Nanshan (+43 in the pipeline), Futian (+16), Old
  Toronto (+16), Business Bay (+10) and Downtown Dubai (+9) will all shift.
- `four_district_tally_summary.md` at the root is the earliest four-city
  summary. It has since been dropped from the project but is kept here.

## Ideas parked

≥100 m threshold · Wikipedia-inclusive counts for Hong Kong, Seoul, Bangkok,
Mumbai and Manila · population-normalised skyscraper density per district.
