# The H3 land grid and the Cliopatria anchors

Written 18 Oct 2026 by the Phase A grid agent. Scripts: `tools/grid.py` (library and
land builder), `tools/compile_anchors.py` (anchors and the three CSVs),
`tools/preview.py` (display test). Run every script with `python3 -I` from a scratch
directory; the Cliopatria file and Natural Earth are read from `/tmp/claude-0/dl/`,
the parsed-feature cache and the per-shape cell cache live under
`/tmp/claude-0/work/grid/` and are rebuilt automatically when missing
(about 75 s end to end: land 16 s, feature cache 9 s, cells 37 s with two workers,
anchors 9 s).

## Files

| File | What |
| --- | --- |
| `land_r5.txt` | The land grid: 524,441 H3 resolution-5 cells, sorted, one per line. The line number from 0 is the cell's **index**; every other grid file refers to cells by that index. |
| `land_r5_island_cells.txt` | The 429 cells in the grid that hold the centroid of a Natural Earth island too small to put a cell centre on land (see the rule below). 422 of them have their own centre at sea. |
| `preview_1600.geojson` | Display test: the 1600 anchor as one polygon feature per polity, coordinates rounded to 3 decimals (properties: slug, name, cells). |
| `preview_1600.png` | The same, rendered with PIL (equirectangular, lon -180..180, lat -60..90, 10 px per degree). |
| `../anchors/<stem>.json` | Cell ownership at each anchor year (120 files, see below). |
| `../anchors/_report.csv` | One row per anchor year: polities alive, cells owned, conflict cells, conflict pairs, seconds. |
| `../anchors/_areas.csv` | One row per (year, slug): cells owned, cells claimed (land cells of the shape before conflicts), cells_all (including sea cells), cell area (cells x 252.9 km2), Cliopatria Area, ratio (owned / Cliopatria) and ratio_claimed. |
| `../anchors/_conflicts.csv` | One row per (year, pair): slug_a is the winner (smaller Cliopatria Area), slug_b the loser, cells the number of land cells both claimed. |

## The land grid

`grid.land_cells(res=5)` returns `{cell: index}` for the cells of Natural Earth 50m land
(`ne_50m_land`). Antarctica and everything south of 60 S are cut away first; every
polygon that crosses the antimeridian or spans more than 180 degrees of longitude is
split (unwrapped, cut at +-180, then cut at its middle meridian if still wider than
180) before `h3.geo_to_cells`, which keeps the cells whose centre falls on land. An
island with no cell centre on it (Mahe, Saint Kitts, Malta's smaller neighbours, atolls)
would otherwise vanish, so such a polygon contributes the cell containing its centroid;
those cells are listed in `land_r5_island_cells.txt`.

Count: 524,441 cells (524,019 with their centre on land plus 422 island centroid
cells), about 132.6 million km2 at 252.9 km2 per cell, which is the Earth's land minus
Antarctica. The master plan's figure of 214,699 cells (and the resolution-4 and -6
figures beside it) is an undercount by a factor of 2.4; the method here was checked by
summing `h3.cell_area` over the cells (134.3 million km2) and by spot points (Paris, the
Sahara, central Australia, Greenland, Chukotka and Fiji in; the mid Pacific, the Caspian
and the Antarctic Peninsula out). Lakes are land in this grid because `ne_50m_land`
has no lake holes; the Caspian is a hole.

## Anchor files

Anchor years: every 100 years from -6000 to 1600 inclusive, every 10 years from 1610 to
2020, and 2024; 120 anchors. File name: `m` plus the absolute year, four digits, for BCE
and `p` plus the year, four digits, for CE: `m6000.json` is 6000 BCE, `m3400.json` is
3400 BCE, `p0000.json` is year 0, `p0800.json` is 800 CE, `p2024.json` is 2024.
`grid.anchor_name(year)` and `grid.anchor_year(stem)` convert.

```json
{"year": 1600, "grid": "land_r5.txt", "land_cells": 524441,
 "owners": {"ming-dynasty": ["401233-401240", 401242, ...], ...},
 "polities": 97, "cells_owned": 184232, "conflicts": 278, "conflict_pairs": 9}
```

`owners` maps a slug (tools/slug.py rule) to runs of indices into `land_r5.txt`, each
run `"start-end"` (inclusive) or a single integer; `grid.from_runs` expands them,
`grid.to_runs` packs them. `polities` is the number of distinct leaf slugs alive in the
year (a slug with no land cell is counted but absent from `owners`). `conflicts` is the
number of land cells claimed by more than one polity before resolution.

Ownership rule: every Cliopatria shape alive in the year (FromYear <= year <= ToYear,
both inclusive) whose Name does not start with "(" claims the land cells of
`grid.shape_cells`: the cells whose centre falls inside the shape, plus the cell of the
centroid of its largest part when the shape is smaller than one cell (or no centre falls
inside it). Where two polities claim a cell the one with the smaller Cliopatria Area
wins (the sum over its shapes alive that year, usually the more specific polity), and
the pair is counted in `_conflicts.csv`. Anchor years before -3400 have no Cliopatria
data and are written with empty owners. The Cliopatria rows for 2024 are a clean
snapshot (1 conflict cell); the rows that run to 2023 carry the overlaps listed below.

Totals: 120 anchors, 120,881 conflict cells summed over all anchors (672 pairs), 9.2 MB
of anchor files and CSVs on the mount. Median area ratio 0.951 (cells owned x 252.9
over Cliopatria Area; 0.952 on claimed cells); 5th to 95th percentile 0.68 to 1.29. The
median sits under 1 because a coastal cell counts as land only when its centre is on
land, so shapes lose about half a cell along every coast, while Cliopatria's Area
includes the water its polygons cover.

## The 20 worst area ratios

One row per polity (its worst anchor year). ratio is on owned cells, ratio_claimed on
the shape's land cells before conflicts; cells_all includes sea cells.

| year | slug | cells | claimed | all | Cliopatria km2 | ratio | ratio_claimed | likely cause |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1630 | new-france | 0 | 0 | 1 | 222 | 0 | 0 | tiny shape drawn at Saint Martin (18.2 N, 63 W); the island is smaller than a cell and the shape's centroid cell is not the grid's island cell |
| 1810 | first-french-colonial-empire | 0 | 0 | 1 | 439 | 0 | 0 | tiny remnant shape (bbox -91..-56 E, 43..47 N) whose one centroid cell is at sea |
| 1970 | british-east-africa | 0 | 0 | 1 | 259 | 0 | 0 | the row 1969-72 is Mahe (Seychelles) under the East Africa Protectorate name; the shape sits 0.1 degree west of the island, so its centroid cell is a sea cell next to the grid's island cell |
| 1980 | seychelles | 0 | 0 | 1 | 259 | 0 | 0 | same shape; every anchor 1980-2024 |
| 1200 | kievan-rus | 4 | 5191 | 5195 | 1,199,824 | 0.0008 | 1.09 | Cliopatria keeps Kievan Rus' (1040-1235) alive beside its principalities (Novgorod, Chernigov, Rostov-Suzdal, Kiev, Smolensk, Polotsk), which are smaller and win |
| 1710 | english-colonial-empire | 5 | 777 | 941 | 227,770 | 0.006 | 0.86 | an aggregate polity overlapping its own colonies and the Gold Coast forts, which are drawn separately; 17 percent of its cells at sea |
| 1980 | netherlands-antilles | 6 | 547 | 555 | 149,155 | 0.01 | 0.93 | the 1877-2023 shape includes Suriname's land; Republic of Suriname (1975-) wins 541 cells |
| 1710 | brandenburg-prussia | 8 | 538 | 556 | 124,775 | 0.016 | 1.09 | overlaps the Kingdom of Prussia (1701-), drawn as a separate smaller leaf |
| 1610 | sultanate-of-malacca | 31 | 235 | 258 | 65,760 | 0.12 | 0.90 | a Malacca row alive 1600-1630 (after 1511) overlapping Mataram on Java (174 cells) and Patani; row to check |
| 1100 | viking-settlements | 23 | 137 | 185 | 47,313 | 0.12 | 0.73 | scattered coastal settlements: a quarter of the cells at sea, the rest lost to Norse Greenland (78) and the Kingdom of the Isles (36), drawn separately |
| 1990 | british-colonial-empire | 68 | 374 | 576 | 134,161 | 0.13 | 0.71 | 1969-95 remnants: a third of the cells at sea, the rest overlapping successor states still inside the shape (Solomon Islands, Belize, Fiji, Bahamas, Brunei) |
| 1800 | batavian-republic | 148 | 843 | 1036 | 259,681 | 0.14 | 0.82 | overlaps the Dutch East Indies (687 cells, flagged in the plan); 19 percent at sea |
| 900 | kingdom-of-mercia | 1 | 1 | 1 | 44 | 5.79 | 5.79 | tiny shape (44 km2) gets one whole cell |
| 1760 | republic-of-genoa | 11 | 45 | 55 | 14,307 | 0.19 | 0.80 | Corsica: loses to the smaller Corsican Republic drawn alongside, plus coastline clipping |
| 1900 | emirate-of-nejd | 1 | 1 | 1 | 53 | 4.81 | 4.81 | tiny shape (53 km2) gets one whole cell |
| 2000 | french-fifth-republic | 2696 | 11640 | 11765 | 3,029,276 | 0.23 | 0.97 | the single 1961-2023 shape still contains Algeria; Algeria wins 8,845 cells at every anchor 1970-2020 |
| 600 | kingdom-of-axum | 380 | 1671 | 1725 | 392,798 | 0.24 | 1.08 | Axum's Yemeni territory overlaps a Himyarite row that is still alive in 600 (1,291 cells) |
| 1100 | county-of-blois | 33 | 145 | 145 | 33,026 | 0.25 | 1.11 | overlaps the County of Champagne (112 cells), drawn alongside |
| 1920 | denmark-norway | 182 | 640 | 743 | 160,323 | 0.29 | 1.01 | a Denmark-Norway row dated 1864-1921 (the union ended 1814) covering Denmark and Iceland; the Kingdom of Iceland (1918-) wins 458 cells; row to check |
| 1000 | duchy-of-naples | 1 | 2 | 2 | 770 | 0.33 | 0.66 | tiny coastal shape: one of its two cells goes to the Republic of Amalfi, the rest is coastline clipping |

Three causes cover the list: Cliopatria overlaps where an aggregate or stale polity
row is alive beside its components or successors (the ratio_claimed column is near 1
for all of these, so the shape itself is fine and only ownership moves); islands and
coastal slivers smaller than a cell (ratio 0 or several times 1); and coastline
clipping, which costs about 20 to 30 percent on archipelago shapes and a few percent
elsewhere.

## Cliopatria rows to check (found while compiling)

- French Fifth Republic 1961-2023: one shape, 3.03 million km2, includes Algeria for its
  whole life (the 2024 row is correct).
- Great Britain 1969-2023: Area 672,038 km2 with a bbox reaching Oman; it overlaps the
  Sultanate of Oman by 1,440 cells at every anchor 1980-2020.
- Netherlands Antilles 1877-2023: includes Suriname's land.
- Kievan Rus' 1040-1235 beside its principalities; Brandenburg-Prussia beside the
  Kingdom of Prussia (1710); Blue Horde beside the Golden Horde (6,581 cells in 1400);
  Chinese Communist Party 1938-45 overlapping the USSR by 5,560 cells in 1940; Kingdom
  of Norway and Nazi Germany both drawn in 1940 (1,743 cells); Mughal Empire 1811-56
  beside the British Empire; Denmark-Norway alive in 1920; Sultanate of Malacca alive
  1600-1630; New Netherland 1800-02 (334 km2, Saint Martin); East Africa Protectorate
  1969-72 at Mahe.
- Reading `preview_1600.png`: the Safavid Dynasty is present (the violet area from
  about 52 E eastward); the blank between it and the Ottoman green is central Arabia,
  which Cliopatria leaves to nobody in 1600. Saint Kitts 1967-2023 is drawn at Saint
  Croix (64.7 W, 17.7 N), not Saint Kitts.

## API summary (tools/grid.py)

- `land_cells(res=5) -> {cell: index}`; `land_cells_int()` gives the sorted uint64
  array and the index map used by the compiler.
- `shape_cells(geometry, res=5) -> set[str]` for a shapely geometry or GeoJSON dict.
- `polity_cells(slug, year, res=5, land_only=False) -> set[str]`, the union of the
  slug's shapes alive in the year, through the caches.
- `cells_to_geojson(cells, decimals=None) -> GeoJSON geometry` via
  `h3.cells_to_h3shape`, split at the antimeridian.
- `features_alive(year, slug=None, leaf_only=False)`, `feature_geometry(feat)`,
  `anchor_name`, `anchor_year`, `to_runs`, `from_runs`, `ANCHOR_YEARS`, `CELL_KM2`.
