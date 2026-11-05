# InfographicaUrbana

The world's cities in maps and figures, in four modes: **ScraperMap** (the tower map below, the site's name until 31 Oct 2026), **TransitMap** (`/metro/`, the world's metro lines year by year), **IndustryMap** (`/industry/`, the cities that trade and make the most) and **CartaHistoria** (`/history/`, every state's borders year by year since 6000 BCE). The modes are listed in `src/lib/modes.ts`, with the site's name and address. Each mode has a guide, a short page on what its map shows and how to use it, with a demo clip and its year dock explained: `/guide/`, `/metro/guide/`, `/industry/guide/` and `/history/guide/` (`src/components/Guide.tsx`; figures from `src/lib/guideData.ts`). The clips and dock pictures in `public/guide/` are recorded from a local build by `node scripts/guide/capture.mjs http://localhost:3456`, which needs ffmpeg and network access to the basemap tiles. The logo is drawn in `src/components/Logo.tsx`; `node scripts/brand/make-icons.mjs` redraws the favicon, app icons and link-preview image from it.

## ScraperMap

Every skyscraper of 150 m or taller in 348 cities — 8,076 towers — pinned to its exact location, assigned to its district, and ranked. Built on the *Skyscrapers by District* dataset.

## Stack

- **Next.js 16** (App Router, static export) — 8,076 tower pages, 348 city pages, 1,023 district pages, rankings, method.
- **MapLibre GL JS 6** — WebGL map with native clustering.
- **OpenFreeMap** — free vector basemap, no API key; **Esri World Imagery** for the satellite view (toggle on the map).
- No backend, no database. Deploys as static files to Vercel, Cloudflare Pages, Netlify, GitHub Pages or any static host.

## Layout

```
data/                data.br.partNN — the dataset, packed (towers, details, places JSON)
scripts/build_data.py   master CSV → JSON   (python3, pandas)
scripts/pack-data.mjs   JSON → data/data.br.partNN
scripts/prebuild.mjs    parts → public/data + src/data; copies MapLibre worker (runs on install/build)
src/app/             routes
src/components/      MapApp (client map), Panel, Chooser, Filters, Search, Legend, Nav, Shell, TowerTable
src/lib/             types, data loaders (server), client loaders, formatting, colours
```

## Run locally

```
npm install          # also unpacks the data and copies the map worker
npm run dev          # http://localhost:3000
npm run build        # static site in ./out
npx serve out
```

## Update the data

1. Replace `data_master.csv` with the new master (same 25 columns).
2. Optionally regenerate `photos.json` (Wikimedia Commons photo lookups).
3. `npm run pack-data` — rebuilds the JSON and repacks `data/`.
4. Commit and deploy.

## CartaHistoria data

The borders live on an H3 resolution-5 grid of the world's land (524,441 cells). `scripts/history/pack.py` reads the research folder (grid, dossiers, colours, the 119 compiled windows, or their drafts where no final exists) and writes `public/history/`: `geo.bin` (cell centres), `w/<window>.bin` (ownership at the window's start plus each year's changes), `states.json`, `state/<slug>.json` (area by year, ledger, sources) and `index.json`. It replays every window from its start anchor and reports any that does not end on its end anchor (`seams` in `index.json`); `--check` replays and reports without writing.

```
python3 -I scripts/history/pack.py /mnt/project-files/history    # then npm run build, and commit public/history
```

States with no colour in `colours.json` get one from a hash of their name and are marked `fb` (shown as "provisional colour").

## Deploy

Vercel: import the repo, framework "Next.js", no settings needed. Set `NEXT_PUBLIC_SITE_URL` to the public URL for correct canonical/OG links.
Anywhere else: `npm run build` and publish `out/`.

## Licence

The code is licensed under the [Apache License 2.0](LICENSE). [NOTICE](NOTICE) holds the credits that copies must keep. The data files aren't covered by Apache 2.0. Each set of data has its own licence:

| Data | Files | Licence |
| --- | --- | --- |
| CartaHistoria borders | `public/history/` | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), built on Cliopatria (CC BY 4.0) |
| TransitMap lines, stations and station structures | `public/metro/` | [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/), derived from OpenStreetMap |
| City and district boundary ids | `public/boundaries.json` | ODbL 1.0, OpenStreetMap ids |
| Metro footprints | `public/metro-footprint.json` | CC BY 4.0, derived from ESA WorldCover 2021 (CC BY 4.0) |
| Trade, manufacturing and city GDP | `src/lib/industry.json`, `src/data-gdp/gdp.json` | CC BY 4.0, with each figure's source cited in the file |
| Skyscraper data, and anything built from it | `data/`, `expansion_ids.txt`, `public/skyline-extent.geojson`, `public/tower-icons/`, `src/lib/lostTowers.json` | Not openly licensed. The building data is © CTBUH / The Skyscraper Center and used with citation. |
| Tower photos | `photos.json` | Each photo keeps its own Wikimedia Commons licence and is credited where it appears. |

## Credits

CartaHistoria's borders start from Cliopatria (Seshat Global History Databank, CC BY 4.0), corrected and dated from Wikipedia. Building data © CTBUH / The Skyscraper Center, used with citation; each tower links to its CTBUH page and no CTBUH images are used. Coordinates partly derived from OpenStreetMap contributors (ODbL). Basemap by OpenFreeMap © OpenMapTiles, data from OpenStreetMap. Photographs from Wikimedia Commons, each credited in place.
