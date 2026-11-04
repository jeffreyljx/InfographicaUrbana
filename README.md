# InfographicaUrbana source data

This branch holds the source data behind [InfographicaUrbana](https://infographicaurbana.vercel.app): the sheets, databases, research files and build tools that the site's four modes are made from. The site's code lives on `main`, which is what Vercel deploys. This branch has no site code and shares no history with `main`. Its `vercel.json` turns off Vercel builds, so pushing here never creates a deployment.

It's a snapshot of the project's shared folder, taken on 3 Nov 2026, right after CartaHistoria went live. It also includes the few files from the `Skyscrapers-by-District` folder on Jeffrey's Mac that weren't anywhere else. In all it comes to about 375 MB in about 8,800 files. The largest single file is 44 MB, so ordinary Git handles everything here and nothing needs Git LFS.

## What's where

| Folder | Size | Mode | What it holds | Built into the site by |
| --- | --- | --- | --- | --- |
| `knowledge/data/` | 3.8 MB | ScraperMap | `skyscrapers_150m_master_geocoded.csv`: every tower of 150 m or taller (8,076 rows, 25 columns) with its coordinates, city and district. Also the list of towers that couldn't be placed and the per-city research sheets and notes. | Copy the master to `data_master.csv` on `main` and run `npm run pack-data` (`scripts/build_data.py`). Rebuilt on 3 Nov 2026, it gives exactly the tower data the site ships. |
| `knowledge/claude/` | 0.2 MB | ScraperMap | Method notes, coordinate checks, and the deploy notes from before the repo existed. | |
| `from-mac/Skyscrapers-by-District/` | 8.5 MB | ScraperMap | `skyscrapers_150m.geojson` (the towers as points) and the first four-district tallies. | |
| `skyline-extent/`, `skyline-time/` | 4.1 MB | ScraperMap | Skyline extent polygons, the density rule, its tools, and the notes behind the year-by-year extents. | Shipped as `public/skyline-extent.geojson` |
| `scrapermap/` | 9.0 MB | ScraperMap, TransitMap | The patches applied before the repo existed (already part of `main`), plus screenshots and notes for each feature. | |
| `metro/db/` | 20 MB | TransitMap | The world metro database: 947 lines in 230 systems, 17,431 stations, dated stages and segments, and line paths as GeoJSON. `README.md` explains every file. | `scripts/metro/build_metro.py metro/db public/metro/metro.json` |
| `metro/tools/` | 16 MB | TransitMap | The database build, the regional research workers' output, and the OpenStreetMap line extract (`osm_lines_built.json.gz`). | |
| `metro/` (other) | 2 MB | TransitMap | `metro-definition.md` (what counts as a metro), `metro.md` (the log of every instruction and design choice), station structures, exits, shared track and Ningbo Line 12 notes. | |
| `metro-footprint/` | 12 MB | ScraperMap | The built-up footprint of 320 metro areas from ESA WorldCover 2021, with its tools and check images. | Shipped as `public/metro-footprint.json` |
| `city-trade-manufacturing/` | 0.3 MB | IndustryMap | City goods trade, container ports, manufacturing value added and exchange rates, plus the research workers' notes. | `scripts/industry/build_industry.py city-trade-manufacturing` |
| `history/` | 297 MB | CartaHistoria | Every state's borders from 6000 BCE. Includes 3,030 state dossiers (`polities/`), the H3 land grid, anchors, gazetteer and hierarchy (`data/`), the 119 compiled windows (`compiled/`), `colours.json`, the tools, the agent briefs, the working notes, and the Cliopatria download it starts from (`sources/`). Read `history/README.md` and `history/master-plan.md` first. | `python3 -I scripts/history/pack.py history` on `main` writes `public/history/` |
| `infographicaurbana/` | 0.4 MB | site | Screenshots from the rebrand. | |

## Left out

- Python bytecode caches (`__pycache__/`).
- Two screenshots uploaded to the project chat (a CTBUH building page and a Baidu map) and a Baidu Maps screenshot from `metro/structures/`. These belong to those sites, so they don't go in a public repo.
- A Vercel `.vercel/project.json` link file.
- Older copies of the site and of these sheets from the Mac folder. The site's code history is on `main`, and the sheets are identical to the ones in `knowledge/`.
- The OpenStreetMap planet extracts used to draw the station structures. They're many gigabytes and can be rebuilt from the public planet file with `scripts/metro/osm/` on `main`.

## Licences

- **Code and tools** on this branch (the Python and JavaScript in the `tools/` folders, the patches in `scrapermap/patches/`, and every other script) are under the [Apache License 2.0](LICENSE), like the site's code on `main`.
- **`history/`** is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), built on Cliopatria (CC BY 4.0). The one exception is `history/sources/historical-basemaps-index.json`, which is GPL-3 and kept only for cross-checks.
- **`metro/`** is under the [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/), because it's derived from OpenStreetMap.
- **`metro-footprint/`** and **`city-trade-manufacturing/`** are under CC BY 4.0.
- **The building data in `knowledge/`, `from-mac/`, `skyline-extent/`, `skyline-time/` and `scrapermap/` isn't openly licensed.** It is © CTBUH / The Skyscraper Center and used with citation.
- Notes and screenshots anywhere else are under CC BY 4.0.

## Sources

- **Buildings:** CTBUH / The Skyscraper Center, used with citation. Each tower links to its CTBUH page. Coordinates were partly checked against OpenStreetMap.
- **Metro lines and stations:** © OpenStreetMap contributors, under the [ODbL](https://opendatacommons.org/licenses/odbl/). Dates and figures come from Wikipedia (CC BY-SA). The metro database is a derived database, so it is shared under the ODbL.
- **Borders:** start from [Cliopatria](https://github.com/Seshat-Global-History-Databank/cliopatria) v0.2.1 by the Seshat Global History Databank (CC BY 4.0, [paper](https://doi.org/10.1038/s41597-025-04516-9)), corrected and dated from Wikipedia. Land outlines come from Natural Earth (public domain).
- **Metro footprints:** ESA WorldCover 2021 (CC BY 4.0).
- **Trade and manufacturing:** national statistics offices and customs agencies, cited row by row in the sheets.
