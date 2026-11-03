# Coordinates added to the city CSVs — coverage report (v1, 2026-09-08)

Every CSV in `data/` now carries four extra columns: `coordinates` (WGS84 decimal `lat, lon`), `coord_source` (URL the point came from), `coord_precision`, `coord_notes`.

`coord_precision` values — use them to style the map pins:

- **building** — the point is the tower itself (OpenStreetMap footprint centroid, a Wikipedia list/article coordinate, Structurae, or DBpedia).
- **complex** — the point is the multi-tower complex/estate the tower belongs to (all towers of the estate share it; typically within 50–150 m of the tower).
- **area** — only a neighbourhood anchor (nearest metro station, cluster centroid or a neighbouring landmark); the note says which anchor and roughly how far. Draw these as a different icon or cluster them.
- **unknown** — no defensible coordinate found; the row is kept with an empty `coordinates` cell.

| file | rows | building | complex | area | unknown |
|---|---|---|---|---|---|
| bangkok_150m.csv | 203 | 182 | 14 | 4 | 3 |
| bangkok_150m_wikipedia.csv | 202 | 181 | 15 | 4 | 2 |
| busan_150m.csv | 72 | 32 | 5 | 35 | 0 |
| guangzhou_150m_by_district.csv | 160 | 29 | 5 | 98 | 28 |
| guangzhou_150m_by_district_v2.csv | 167 | 31 | 5 | 100 | 31 |
| guangzhou_150m_wikipedia.csv | 160 | 29 | 5 | 98 | 28 |
| hongkong_saikung_ytm.csv | 166 | 144 | 14 | 8 | 0 |
| istanbul_150m.csv | 78 | 16 | 32 | 29 | 1 |
| jakarta_150m.csv | 133 | 68 | 25 | 40 | 0 |
| manila_150m.csv | 162 | 59 | 32 | 59 | 12 |
| metro_manila_150m_wikipedia.csv | 162 | 59 | 32 | 59 | 12 |
| moscow_150m.csv | 137 | 137 | 0 | 0 | 0 |
| osaka_150m.csv | 53 | 42 | 2 | 9 | 0 |
| seoul_150m.csv | 127 | 56 | 18 | 50 | 3 |
| seoul_150m_wikipedia.csv | 127 | 56 | 18 | 50 | 3 |
| shanghai_150_200_band.csv | 81 | 8 | 2 | 68 | 3 |
| shanghai_200m_by_district.csv | 70 | 35 | 1 | 30 | 4 |
| shanghai_200m_by_district_v2.csv | 70 | 35 | 1 | 30 | 4 |
| shenzhen_150_200_band.csv | 36 | 7 | 2 | 15 | 12 |
| shenzhen_200m_by_district.csv | 140 | 77 | 2 | 27 | 34 |
| singapore_150m.csv | 126 | 83 | 19 | 24 | 0 |
| sydney_150m.csv | 63 | 63 | 0 | 0 | 0 |
| toronto_150m.csv | 117 | 117 | 0 | 0 | 0 |
| **all files** | 2812 | 1546 | 249 | 837 | 180 |

Unique buildings across the files: 1,948 — 1,165 building-level (60 %), 174 complex (9 %), 505 area (26 %), 104 unknown (5 %). Toronto, Sydney and Moscow are 100 % building-level; Hong Kong, Bangkok, Jakarta and Singapore are ≥ 75 % building/complex; Guangzhou and Shanghai are the weak spots (most of their 150–200 m towers carry neither a Wikipedia article nor an OSM height tag).

## Sources and licences
- OpenStreetMap building footprints via the Overpass API (© OpenStreetMap contributors, ODbL — attribute on the map). ~410 towers.
- English Wikipedia list tables with coordinate columns (Shenzhen, Hong Kong, Toronto, Singapore, Moscow, Sydney, Osaka, Bangkok) and building/estate articles, plus DBpedia (CC BY-SA). ~700 towers.
- Structurae, developer/official pages, Yandex Maps (Istanbul only), GeoNames for a few dozen.
- Not used: SkyDB (its robots/licence notice forbids storing or re-publishing its records), the Skyscraper Center (no coordinates on public pages). If you still have the second-edition per-building CSV (CTBUH coordinates for ~6,100 buildings), a join by name would lift most of the remaining area/unknown rows to building level in one step.

## Known issues to review (also in `coord_notes`)
- District conflicts found while locating towers: Guangdong Landmark Tower is in Luohu (not Nanshan); C Future City East/West are in Futian (not Nanshan); China International Center Tower B, Caesar's Palace 3 and Victory Garden are in Yuexiu (not Tianhe); The Cove (Sydney) is in The Rocks, not North Sydney; Academy Sweet is in Gangnam, Doosan Tower and Brownstone Seoul in Jung-gu; WBC The Palace is in Centum City, not Marine City; Four Winds (Istanbul) is Göztepe, Kadıköy.
- Source coordinates discarded as wrong: Galaxy World Towers (Wikipedia list point lands in Hong Kong), Skyland Istanbul and Tower 205 (Wikipedia copies), Milano Residences and Millennium Office Tower (DBpedia points 2 km off), Skyrise Avenue G and Park 24 C (Bangkok list errors), Equity Tower (Yandex).
- Hanking Center: the Wikipedia list coordinate sits ~1.3 km west of the tower's real site (Keyuan South Rd) — treat as area-level until replaced.
- Possible swaps in the source lists: Park Central North/South (Makati) heights; Millennium Residence I/II near-identical points.

## Next step
A second OpenStreetMap pass over the clusters the first pass could not reach (Guangzhou Binjiang East/Financial City/Pazhou/Wanbo, Shanghai Putuo/Xuhui/Zhangjiang/North Bund, Seoul Tower Palace/Mok-dong/Jamsil, Manila BGC/Ortigas, Busan BIFC/W, Istanbul Levent/Ataşehir, Osaka Umeda, Bangkok leftovers) is queued; it is slow because the fetch proxy allows ~10 requests a minute.