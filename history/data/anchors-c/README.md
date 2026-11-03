# Phase C anchors (compiled from the reviewed dossiers)

Written by `tools/compile_dossiers.py` on 2026-11-03 (run it again after the dossiers change; see
`notes/phase-c/README.md`). These are the fixed handoff states of the Phase D windows
(`compiled/README.md` lists the windows): every anchor is the cell ownership **on 1 January of its
year, after every event dated in an earlier year**, so window `[a, b]` starts from anchor `a` and,
after every change it lists for the years a..b, ends exactly at anchor `b + 1`. The Phase A anchors in
`data/anchors/` (Cliopatria only) are left untouched as the comparison baseline.

Two files break the 1 January rule on purpose and say so in `as_of`: `p2026.json` is the final
snapshot, the map at the end of 2026 after every event; `p2030.json`, the end anchor of the last window
(2020 to 2029), holds the same cells, since the run stops at 2026 and nothing is dated later.

## Format

```json
{"year": 1600, "as_of": "1 January 1600 (after every event dated 1599 or earlier)",
 "grid": "land_r5.txt", "land_cells": 524441,
 "owners": {"ming-dynasty": ["401233-401240", 401242], ...},
 "status": {
   "vassal":    [{"owner": "joseon", "suzerain": "ming-dynasty", "relation": 12, "cells": [...]}],
   "constituent": [{"owner": "duchy-of-styria", "suzerain": "habsburg-monarchy", "relation": 2635, "cells": [...]}],
   "occupied":  [{"owner": "kingdom-of-france", "occupier": "kingdom-of-england", "relation": 40, "cells": [...]}],
   "contested": [{"owner": "kingdom-of-france", "claimants": ["kingdom-of-france", "kingdom-of-england"],
                  "relation": 41, "cells": [...]}]},
 "relations": {
   "contests":    [{"id": 41, "a": "<slug>", "b": "<slug or name>", "since": 1415, "war": "...", "event": "<slug>/ledger/<i>", "cells": 312}],
   "occupations": [{"id": 40, "occupier": "<slug or name>", "owner": "<slug, name or null>", "since": 1417, "event": "...", "cells": 88}],
   "vassals":     [{"id": 12, "suzerain": "<slug>", "vassal": "<slug or name>", "since": 1401, "event": "...", "cells": 2210},
                   {"id": 4154, "suzerain": "united-kingdom", "vassal": "british-africa", "since": 1885,
                    "event": "data/colonies.csv: british-africa, metropole united-kingdom from 1885", "cells": 23586, "colony": true}]},
 "polities": 97, "cells_owned": 184232, "compiler": "tools/compile_dossiers.py"}
```

- `owners`: dossier slug -> runs of indices into `data/grid/land_r5.txt` (`"start-end"` inclusive or a
  single integer; `grid.from_runs` / `grid.to_runs` convert), every cell the state owns whatever its
  status. A cell is in at most one slug's runs (checked by the self-check). Cells in no slug's runs are
  nobody's land (neutral), unless `status.occupied` lists them with `owner: null`.
- `status`: the cells whose status is not direct, grouped by owner, the other party and the relation;
  a cell an owner holds that is not listed here is **direct**. `constituent`: the owner is a member of
  `suzerain` (an Imperial Estate, a Soviet republic), from `data/hierarchy.csv` (rule R3 in
  `notes/phase-c/README.md`); drawn like a vassal. `vassal`: the owner is a vassal of
  `suzerain` (when the vassal has no dossier the owner is the suzerain itself, drawn in its own vassal
  tint; a colony's cells are its metropole's vassal land, rule R1 in `notes/phase-c/README.md`).
  `occupied`: held by `occupier` without annexation (owner null when the land belonged to
  nobody or to a state without a dossier). `contested`: fought over by `claimants` = [holder, challenger]
  (a challenger without a dossier appears by name).
- `relations`: every contest, occupation and vassal relation open at that moment (opened by a
  `*_start` event and not yet closed by its `*_end`), with its id (the `relation` of the status groups),
  first year, opening event (`<slug>/ledger/<index>`), the other names involved and its current number of
  cells (a relation can be open with 0 cells when its region held none of the parties' land). A vassal
  relation with `"colony": true` is a colony's tie to its metropole from `data/colonies.csv` (opened at
  the start of the row, `event` names the row), not a ledger event; an explicit suzerainty from the
  ledger shows over it while it is open. These are the window agents' `handoff.open_*` lists at the
  window boundary. A relation with `"hierarchy": "constituent"` or `"vassal"` (and its `confidence`) is a
  row of `data/hierarchy.csv` (rule R3), opened at the start of the row and closed at its end, not a
  ledger event; like a colony's, a suzerainty from the ledger shows over it while it is open.
- `polities`: slugs with at least one cell; `cells_owned`: cells with an owner.

Status codes are exclusive: a cell has one owner and one status. Vassals, occupations and contests are
the window brief's rule 4 and rule 6; colours, tints, hatches and blends are applied by the packer from
`colours.json`, never stored here.

## The anchors

| file | year | as of | polities | cells owned | status groups | open relations | KB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m6000 | -6000 | 1 January -6000 | 0 | 0 | 0 | 0 | 0 |
| m5900 | -5900 | 1 January -5900 | 26 | 77,938 | 0 | 0 | 24 |
| m5800 | -5800 | 1 January -5800 | 26 | 77,938 | 0 | 0 | 24 |
| m5700 | -5700 | 1 January -5700 | 27 | 78,297 | 0 | 0 | 25 |
| m5600 | -5600 | 1 January -5600 | 27 | 78,260 | 0 | 0 | 25 |
| m5500 | -5500 | 1 January -5500 | 28 | 78,778 | 0 | 0 | 26 |
| m5400 | -5400 | 1 January -5400 | 31 | 82,436 | 0 | 0 | 30 |
| m5300 | -5300 | 1 January -5300 | 30 | 81,367 | 0 | 0 | 29 |
| m5200 | -5200 | 1 January -5200 | 30 | 83,844 | 0 | 0 | 31 |
| m5100 | -5100 | 1 January -5100 | 31 | 84,945 | 0 | 0 | 33 |
| m5000 | -5000 | 1 January -5000 | 30 | 85,297 | 0 | 0 | 33 |
| m4900 | -4900 | 1 January -4900 | 32 | 88,780 | 0 | 0 | 38 |
| m4800 | -4800 | 1 January -4800 | 32 | 88,780 | 0 | 0 | 38 |
| m4700 | -4700 | 1 January -4700 | 33 | 88,813 | 0 | 0 | 38 |
| m4600 | -4600 | 1 January -4600 | 34 | 89,137 | 0 | 0 | 38 |
| m4500 | -4500 | 1 January -4500 | 35 | 89,220 | 0 | 0 | 39 |
| m4400 | -4400 | 1 January -4400 | 33 | 88,534 | 0 | 0 | 37 |
| m4300 | -4300 | 1 January -4300 | 35 | 88,583 | 0 | 0 | 37 |
| m4200 | -4200 | 1 January -4200 | 34 | 87,372 | 0 | 0 | 36 |
| m4100 | -4100 | 1 January -4100 | 33 | 87,356 | 0 | 0 | 36 |
| m4000 | -4000 | 1 January -4000 | 34 | 90,664 | 0 | 0 | 38 |
| m3900 | -3900 | 1 January -3900 | 34 | 90,588 | 0 | 0 | 37 |
| m3800 | -3800 | 1 January -3800 | 34 | 90,588 | 0 | 0 | 37 |
| m3700 | -3700 | 1 January -3700 | 35 | 90,834 | 0 | 0 | 38 |
| m3600 | -3600 | 1 January -3600 | 35 | 91,274 | 0 | 0 | 38 |
| m3500 | -3500 | 1 January -3500 | 33 | 63,343 | 0 | 0 | 32 |
| m3400 | -3400 | 1 January -3400 | 31 | 57,785 | 0 | 0 | 26 |
| m3300 | -3300 | 1 January -3300 | 31 | 27,529 | 0 | 0 | 27 |
| m3200 | -3200 | 1 January -3200 | 30 | 25,826 | 0 | 0 | 26 |
| m3100 | -3100 | 1 January -3100 | 31 | 28,934 | 0 | 0 | 28 |
| m3000 | -3000 | 1 January -3000 | 32 | 28,831 | 0 | 0 | 28 |
| m2900 | -2900 | 1 January -2900 | 30 | 28,115 | 0 | 0 | 27 |
| m2800 | -2800 | 1 January -2800 | 30 | 28,025 | 0 | 0 | 26 |
| m2700 | -2700 | 1 January -2700 | 28 | 26,688 | 0 | 0 | 25 |
| m2600 | -2600 | 1 January -2600 | 28 | 27,078 | 0 | 0 | 26 |
| m2500 | -2500 | 1 January -2500 | 28 | 22,264 | 0 | 0 | 22 |
| m2400 | -2400 | 1 January -2400 | 31 | 23,000 | 1 | 3 | 24 |
| m2300 | -2300 | 1 January -2300 | 28 | 23,284 | 0 | 1 | 24 |
| m2200 | -2200 | 1 January -2200 | 26 | 26,396 | 0 | 0 | 26 |
| m2100 | -2100 | 1 January -2100 | 25 | 25,447 | 0 | 0 | 24 |
| m2000 | -2000 | 1 January -2000 | 28 | 24,902 | 0 | 0 | 24 |
| m1900 | -1900 | 1 January -1900 | 26 | 14,514 | 0 | 0 | 19 |
| m1800 | -1800 | 1 January -1800 | 29 | 13,894 | 0 | 0 | 20 |
| m1700 | -1700 | 1 January -1700 | 26 | 16,611 | 1 | 1 | 22 |
| m1600 | -1600 | 1 January -1600 | 32 | 15,820 | 1 | 1 | 22 |
| m1500 | -1500 | 1 January -1500 | 29 | 14,631 | 1 | 1 | 21 |
| m1400 | -1400 | 1 January -1400 | 24 | 14,110 | 6 | 5 | 21 |
| m1300 | -1300 | 1 January -1300 | 29 | 15,690 | 10 | 9 | 25 |
| m1200 | -1200 | 1 January -1200 | 28 | 12,928 | 10 | 9 | 23 |
| m1100 | -1100 | 1 January -1100 | 27 | 13,114 | 0 | 0 | 17 |
| m1000 | -1000 | 1 January -1000 | 67 | 13,843 | 6 | 6 | 29 |
| m0900 | -900 | 1 January -900 | 74 | 16,031 | 5 | 5 | 32 |
| m0800 | -800 | 1 January -800 | 91 | 19,369 | 11 | 11 | 41 |
| m0700 | -700 | 1 January -700 | 89 | 20,753 | 11 | 16 | 43 |
| m0600 | -600 | 1 January -600 | 78 | 34,063 | 8 | 7 | 47 |
| m0500 | -500 | 1 January -500 | 80 | 40,700 | 11 | 22 | 53 |
| m0400 | -400 | 1 January -400 | 81 | 44,518 | 15 | 21 | 59 |
| m0300 | -300 | 1 January -300 | 82 | 54,278 | 8 | 7 | 58 |
| m0200 | -200 | 1 January -200 | 81 | 72,238 | 27 | 29 | 85 |
| m0100 | -100 | 1 January -100 | 83 | 82,092 | 26 | 32 | 94 |
| p0000 | 0 | 1 January 0 | 80 | 83,890 | 31 | 39 | 93 |
| p0100 | 100 | 1 January 100 | 68 | 91,461 | 17 | 24 | 84 |
| p0200 | 200 | 1 January 200 | 83 | 75,683 | 14 | 21 | 91 |
| p0300 | 300 | 1 January 300 | 79 | 85,674 | 17 | 21 | 85 |
| p0400 | 400 | 1 January 400 | 94 | 86,159 | 19 | 17 | 89 |
| p0500 | 500 | 1 January 500 | 109 | 97,041 | 21 | 19 | 96 |
| p0600 | 600 | 1 January 600 | 121 | 99,509 | 25 | 24 | 106 |
| p0700 | 700 | 1 January 700 | 126 | 113,475 | 19 | 21 | 100 |
| p0800 | 800 | 1 January 800 | 144 | 122,976 | 31 | 30 | 108 |
| p0900 | 900 | 1 January 900 | 201 | 112,928 | 42 | 41 | 146 |
| p1000 | 1000 | 1 January 1000 | 244 | 118,452 | 46 | 46 | 154 |
| p1100 | 1100 | 1 January 1100 | 291 | 132,420 | 78 | 83 | 191 |
| p1200 | 1200 | 1 January 1200 | 322 | 134,416 | 112 | 115 | 222 |
| p1300 | 1300 | 1 January 1300 | 384 | 170,907 | 162 | 173 | 248 |
| p1400 | 1400 | 1 January 1400 | 369 | 158,678 | 151 | 157 | 240 |
| p1500 | 1500 | 1 January 1500 | 368 | 179,387 | 139 | 146 | 251 |
| p1600 | 1600 | 1 January 1600 | 343 | 188,488 | 167 | 184 | 293 |
| p1610 | 1610 | 1 January 1610 | 349 | 190,902 | 165 | 183 | 296 |
| p1620 | 1620 | 1 January 1620 | 348 | 193,232 | 171 | 185 | 297 |
| p1630 | 1630 | 1 January 1630 | 352 | 193,944 | 185 | 204 | 306 |
| p1640 | 1640 | 1 January 1640 | 360 | 216,003 | 202 | 219 | 322 |
| p1650 | 1650 | 1 January 1650 | 363 | 224,633 | 205 | 223 | 336 |
| p1660 | 1660 | 1 January 1660 | 370 | 237,073 | 199 | 216 | 335 |
| p1670 | 1670 | 1 January 1670 | 368 | 240,594 | 188 | 207 | 333 |
| p1680 | 1680 | 1 January 1680 | 369 | 268,053 | 189 | 206 | 354 |
| p1690 | 1690 | 1 January 1690 | 366 | 265,394 | 203 | 216 | 345 |
| p1700 | 1700 | 1 January 1700 | 366 | 272,353 | 189 | 202 | 343 |
| p1710 | 1710 | 1 January 1710 | 374 | 276,063 | 194 | 216 | 354 |
| p1720 | 1720 | 1 January 1720 | 380 | 281,570 | 198 | 216 | 368 |
| p1730 | 1730 | 1 January 1730 | 385 | 282,542 | 192 | 208 | 369 |
| p1740 | 1740 | 1 January 1740 | 390 | 285,620 | 205 | 220 | 387 |
| p1750 | 1750 | 1 January 1750 | 398 | 275,617 | 196 | 213 | 383 |
| p1760 | 1760 | 1 January 1760 | 406 | 313,072 | 207 | 230 | 418 |
| p1770 | 1770 | 1 January 1770 | 403 | 330,478 | 203 | 231 | 424 |
| p1780 | 1780 | 1 January 1780 | 408 | 347,671 | 196 | 220 | 410 |
| p1790 | 1790 | 1 January 1790 | 415 | 364,943 | 209 | 229 | 418 |
| p1800 | 1800 | 1 January 1800 | 394 | 374,793 | 190 | 217 | 416 |
| p1810 | 1810 | 1 January 1810 | 362 | 378,430 | 176 | 204 | 406 |
| p1820 | 1820 | 1 January 1820 | 361 | 377,664 | 172 | 203 | 415 |
| p1830 | 1830 | 1 January 1830 | 359 | 408,997 | 160 | 193 | 390 |
| p1840 | 1840 | 1 January 1840 | 361 | 408,584 | 170 | 206 | 415 |
| p1850 | 1850 | 1 January 1850 | 354 | 418,329 | 171 | 212 | 397 |
| p1860 | 1860 | 1 January 1860 | 348 | 425,150 | 156 | 175 | 391 |
| p1870 | 1870 | 1 January 1870 | 331 | 423,022 | 166 | 188 | 389 |
| p1880 | 1880 | 1 January 1880 | 305 | 433,664 | 168 | 189 | 389 |
| p1890 | 1890 | 1 January 1890 | 286 | 455,531 | 173 | 201 | 398 |
| p1900 | 1900 | 1 January 1900 | 241 | 487,609 | 195 | 229 | 440 |
| p1910 | 1910 | 1 January 1910 | 207 | 506,035 | 167 | 202 | 417 |
| p1920 | 1920 | 1 January 1920 | 196 | 494,824 | 146 | 173 | 424 |
| p1930 | 1930 | 1 January 1930 | 197 | 511,235 | 135 | 162 | 418 |
| p1940 | 1940 | 1 January 1940 | 193 | 520,541 | 134 | 157 | 413 |
| p1950 | 1950 | 1 January 1950 | 171 | 520,745 | 88 | 104 | 348 |
| p1960 | 1960 | 1 January 1960 | 158 | 521,064 | 76 | 88 | 316 |
| p1970 | 1970 | 1 January 1970 | 195 | 520,421 | 56 | 61 | 285 |
| p1980 | 1980 | 1 January 1980 | 202 | 520,298 | 50 | 61 | 282 |
| p1990 | 1990 | 1 January 1990 | 209 | 520,342 | 50 | 55 | 283 |
| p2000 | 2000 | 1 January 2000 | 220 | 519,421 | 34 | 37 | 253 |
| p2010 | 2010 | 1 January 2010 | 217 | 519,404 | 18 | 24 | 239 |
| p2020 | 2020 | 1 January 2020 | 225 | 519,403 | 23 | 29 | 245 |
| p2026 | 2026 | end of 2026 | 224 | 519,396 | 26 | 29 | 250 |
| p2030 | 2030 | 1 January 2030 | 224 | 519,396 | 26 | 29 | 250 |
