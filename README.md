# InfographicaUrbana

The world's cities in maps and figures, in four modes: **ScraperMap** (the tower map below, the site's name until 31 Oct 2026), **TransitMap** (`/metro/`, the world's metro lines year by year), **IndustryMap** (`/industry/`, the cities that trade and make the most) and **CartaHistoria** (`/history/`, every state's borders year by year since 6000 BCE). The modes are listed in `src/lib/modes.ts`, with the site's name and address. The logo is drawn in `src/components/Logo.tsx`; `node scripts/brand/make-icons.mjs` redraws the favicon, app icons and link-preview image from it.

## The four modes

**ScraperMap** (`/`) pins every skyscraper of 150 m or taller to its exact spot: 8,076 towers in 348 cities, each assigned to one of 1,023 districts. Tables rank countries, cities and districts by their towers. The map draws each city's skyline extent, and the Skylines page sets them side by side at one scale. A time capsule slider rebuilds any year's skyline, including lost towers such as the original World Trade Center. A toggle shows the built-up footprint of 320 metro areas.

**TransitMap** (`/metro/`) animates how the world's metro systems grew: 947 lines in 230 systems, from London's Metropolitan line in 1863 to October 2026, drawn section by section in their own colours. Every station has a page, and when you zoom in, stations show their halls and lettered exits from OpenStreetMap.

**IndustryMap** (`/industry/`) shows the cities that trade and make the most, with circles to scale and tables ranking 2025 goods trade for 47 cities and manufacturing value added for 38.

**CartaHistoria** (`/history/`) shows every state's borders year by year from 6000 BCE to today: 3,178 states, empires, dynasties and cultures, with contested land marked and a page for each state showing its area over time.

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

## Credits and licences

CartaHistoria's borders start from Cliopatria (Seshat Global History Databank, CC BY 4.0), corrected and dated from Wikipedia. Building data © CTBUH / The Skyscraper Center, used with citation; each tower links to its CTBUH page and no CTBUH images are used. Coordinates partly derived from OpenStreetMap contributors (ODbL). Basemap by OpenFreeMap © OpenMapTiles, data from OpenStreetMap. Photographs from Wikimedia Commons, each credited in place.
