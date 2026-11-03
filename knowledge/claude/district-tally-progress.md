# District skyscraper tally — status (session 2026-09-05)

## Done
- Second edition report saved as `claude/District_skyscrapers_v2.md` (exact building-by-building counts for 58 metropolitan units / 416 sub-city units; global ranking; methodology; caveats). The spreadsheet (`District_skyscrapers_v2.xlsx`, live COUNTIFS formulas over a 6,421-building sheet) and the per-building CSV were delivered in the chat (the project's doc store rejected the binary upload).

## Headline results (completed buildings ≥150 m, CTBUH status Completed)
Manhattan 294 · Nanshan (Shenzhen) 189 · Futian 127 · Sai Kung (HK) 122 · Old Toronto 100 · Pudong 92 · Tianhe 87 · Central & Western (HK) 79 · Luohu 76 · Downtown Core (Singapore) 71 · Loop (Chicago) 70 · Dubai Marina 64 · KLCC/Golden Triangle 64 · South Jakarta 63 · Yuzhong (Chongqing) 63 · Minato 61 · Melbourne CBD 59 · Makati 59.
Manhattan split: Midtown 207 / Lower 65 / Upper 22.

## Method (for reproducibility)
- Building list: CTBUH/CVU Skyscraper Center live "Explore Data" tool, sliced by city × completion year (× function × material when a year exceeded the 25-row cap); index-only records verified on building pages (26 excluded at 149.x m, 23 with no confirmed height). City totals reconcile exactly to CTBUH's published city ranking for 40 of 56 cities, within 1–5 for the rest.
- Coordinates: CTBUH's public Algolia search index (`SC_Buildings`, `_geoloc`) for 6,106 buildings; Nominatim search on CTBUH addresses / targeted research for the rest.
- District: OpenStreetMap boundaries via Overpass `is_in` (point-in-polygon, full admin hierarchy) — 5,123 buildings; geoBoundaries polygons as fallback/cross-check; Nominatim reverse geocode for cities without formal districts (Dubai, KL, Miami…); 155 buildings by targeted research; 28 (0.5%) left unassigned.
- Working files (session workspace only): `assigned.csv` (all fields), `district_ranking.csv`, `manual_district.json`, `override_district.json`, `names_norm.py` (name canonicalisation), `assign.py`, `make_report.py`, `make_xlsx.py`.

## Open items / ideas for a next pass
- 28 unassigned buildings (list in the report's Caveats) need addresses — mostly 1990s–2010s towers in Shenyang, Chengdu, Wuhan, Tianjin, Suzhou.
- Re-run in ~12 months: Nanshan (+43 in pipeline), Futian (+16), Old Toronto (+16), Business Bay (+10), Downtown Dubai (+9) will shift.
- Possible extensions: ≥100 m threshold; Wikipedia-inclusive counts for Hong Kong/Seoul/Bangkok/Mumbai/Manila; population-normalised density per district.
