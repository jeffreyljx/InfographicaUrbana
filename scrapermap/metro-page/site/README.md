# ScraperMap

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

## Deploy

Vercel: import the repo, framework "Next.js", no settings needed. Set `NEXT_PUBLIC_SITE_URL` to the public URL for correct canonical/OG links.
Anywhere else: `npm run build` and publish `out/`.

## Credits and licences

Building data © CTBUH / The Skyscraper Center, used with citation; each tower links to its CTBUH page and no CTBUH images are used. Coordinates partly derived from OpenStreetMap contributors (ODbL). Basemap by OpenFreeMap © OpenMapTiles, data from OpenStreetMap. Photographs from Wikimedia Commons, each credited in place.
