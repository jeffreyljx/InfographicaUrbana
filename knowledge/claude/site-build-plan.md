# Build & deploy plan — the skyscraper map

**Goal:** every geocoded tower ≥150 m as a pin on an interactive world map, each pin opening its own small landing page with the building's facts and a link to its CTBUH entry. (Originally 6,237 towers in 58 cities; since 27 Sep 2026, 8,076 towers in 348 cities.)

**Status (2026-09-28): BUILT AND LIVE at https://scrapermap.vercel.app, with photos, every CTBUH city, a satellite view and rankings by country, city and district** — see `claude/scrapermap-deploy-notes.md` for the deployment details, how to redeploy and what is still open. Decisions taken: site name **ScraperMap**; shared-point towers open a **dropdown list** (no spiral offset); **no CTBUH photos**, CTBUH cited + linked per tower; shipped on free `scrapermap.vercel.app`, custom domain later; **Wikimedia Commons photos done** for 1,057 towers in a first pass (Wikidata P18 matched by coordinate + height/name, free licences only, credited in place; run from the user's Mac browser on 26 Sep 2026 and redeployed as `dpl_4DkkeJtu8kT53xPHndAd4btsZVJH`); **Cities page height-threshold ranking** (150/200/300 m switch, 200 m+ column, `?min=` deep links, ranks at 200/300 m on city pages) added 27 Sep 2026 and deployed as `dpl_7sxDy6SFtBrM8d57AKbDpC9L4KBQ`; **second photo pass** (Commons categories named after the tower or its development, every pick checked by eye; +236 towers, 107 in China; development-level photos labelled "Complex view") deployed 27 Sep 2026 as `dpl_Abhv8chM9hgvRKr12abx3HFhroRq`. Decision (27 Sep): all-rights-reserved images from Baidu, property portals etc. are not used — licence/takedown risk, and it would contradict the free-licence statement on `/method/`.

**Expansion + satellite (27 Sep 2026, `dpl_C4ptMnRvzE5ECTkzbFthKJSAd71u`).** Every other city in the CTBUH database added: 1,839 towers placed in 290 new cities (plus suburbs of existing cities), 44 more unplaced, 614 more photos → **8,076 towers, 348 cities, 1,023 districts, 1,907 photos**. User rules: suburbs are merged into their metro city (La Défense → Paris, Burnaby → Vancouver, Mississauga → Toronto, Noida/Gurugram → Delhi …) but each suburb stays its own district, never folded into a core-city district; principal cities of a metro (Yokohama, Sharjah, Fort Worth, Newark, Incheon, Jersey City) stay separate. Satellite basemap: **Esri World Imagery** (user's choice), toggle on the map, remembered per browser; all map actions work the same on it. The per-city CSVs in `data/` remain frozen; only the master (`data/skyscrapers_150m_master_geocoded.csv`, = the site's `data_master.csv`), the unplaced list and the GeoJSON were updated. Source archive, `photos.json` and data files are in the outputs / the user's Mac folder `Skyscrapers-by-District`.

**Rankings + sorting (28 Sep 2026, `dpl_KaSQ1Xx8oVS37gXTGoxmwpPKtoJ5`).** User's request: the top bar is now **Map · Countries · Cities · Districts · Method** (rankings by country, city and urban district). New `/countries/` page (threshold switch, cities/districts counts, leading city, tallest building); the district league table moved to `/districts/` (`/rankings/` forwards there). Every count column and Tallest on the Countries, Cities and Districts tables (and each city page's district table) has a small ▼ sort button — most-first, then least-first on a second click; `#` keeps the rank by completed towers; views link via `?sort=&order=`. User query the same day: "CITIC Securities tower in Nanshan missing" — it is in the data under CTBUH's name **CITIC Financial Center Tower 1** (312 m, structurally topped out, #10 in Nanshan; CITIC Securities' new global HQ; Tower 2 is its 200 m companion). It is hidden on the map by default only because the default filter shows completed towers; search does not know the "CITIC Securities" name.

The original plan follows, unchanged (numbers in it are the first edition's).

---

## 1. Stack

| Layer | Choice | Why |
|---|---|---|
| Map engine | **MapLibre GL JS** | Native GeoJSON clustering handles 6,237 points at 60 fps with no plugin. Leaflet + markercluster is DOM-based and stutters at this count. Open source, no licence key. |
| Basemap | **OpenFreeMap** | Free vector tiles, no API key, no registration, no request limits, commercial use permitted, attribution auto-injected by MapLibre. Removes the single biggest recurring cost and the only credential the site would otherwise need. |
| Site framework | **Next.js (App Router), static export** | ~6,700 pages generated at build time; one map island. Deploys to Vercel with no configuration, and leaves the door open to an API later. |
| Hosting | **Vercel** (free tier) | Static output, global CDN, deploy-on-push. Cloudflare Pages or GitHub Pages are drop-in alternatives if you'd rather. |
| Backend | **None** | Everything is static JSON. No database, no server, no keys, nothing to run up a bill or go down. |

**Total recurring cost: $0**, excluding a domain if you want one (~$12–15/yr).

---

## 2. Data pipeline

One build script turns the master CSV into four artefacts:

| Artefact | Contents | Size |
|---|---|---|
| `towers.json` | Positional array per tower with string tables for city/district/status/function/precision | ~90 KB gzipped |
| `details.json` | Everything else — material, address, CTBUH slug, coord note, OSM way, photo | lazy-loaded after first paint |
| `places.json` | The 58 cities and 421 districts with counts, tallest tower, bbox and rank — derived at build time | ~30 KB |
| `/tower/<slug>/` | 6,237 pre-rendered HTML pages, one per building | build artefact |

The index alone is what the map needs, so the map is interactive in well under a second on a normal connection. Slugs are name + id (`burj-khalifa-3`).

---

## 3. Map behaviour

- **Zoomed out:** clustered circles, sized and coloured by count. **Zoomed in:** individual pins.
- **Pin styling** by height band — 150–199 / 200–299 / 300–399 / 400 m+.
- **Precision honesty:** the 78 `approximate` pins render hollow and are off by default behind a toggle.
- **Shared points:** 239 towers sit on 111 shared complex points; clicking such a pin lists the towers in a dropdown. The stored coordinate never changes and the panel says the source gave one point for the whole complex.
- **Click → panel** (side panel on desktop, bottom sheet on mobile): name, height, floors, year, status, function, material, district, rank in city / district / world, address, **View on CTBUH**, and a "how this pin was placed" line from `coord_precision` + `coord_note`.
- **URL updates to `/tower/<slug>/`** via the History API, so every pin is shareable and lands on the pre-rendered page.
- **Filters:** city, district, height, year, status, use. Default status filter is **Completed only**, matching how the report counts.
- **Search:** client-side match over name / city / district.

### Pages beyond the map
- `/` — the map, full bleed.
- `/tower/<slug>/` — the landing page for each of the 6,237.
- `/city/<slug>/` and `/city/<slug>/<district>/` — tables plus "open on the map".
- `/rankings/` — the districts league table (moved to `/districts/` on 28 Sep 2026; `/countries/` added).
- `/method/` — where the data comes from, how coordinates were verified, what the precision classes mean, known gaps.

---

## 4. Attribution and licensing — settled

- **CTBUH:** their FAQ states the Skyscraper Center's information "is available for public use and inclusion within research if applicable citations referencing the Council on Tall Buildings and Urban Habitat (CTBUH) are made." CTBUH is cited on every tower page, in the footer and in the map attribution, with a link back to each building's page.
- **CTBUH images are explicitly *not* shareable.** No building photos from CTBUH. Imagery, if any, comes from Wikimedia Commons with author + licence credit.
- **OpenStreetMap:** 2,427 coordinates are OSM footprint centroids — "© OpenStreetMap contributors" in the attribution control and on the method page.
- **OpenFreeMap:** "OpenFreeMap © OpenMapTiles Data from OpenStreetMap" — added automatically by MapLibre.
- **Esri World Imagery** (satellite view, added 27 Sep 2026): "Esri, Maxar, Earthstar Geographics, and the GIS User Community" in the map attribution, footer and method page.

---

## 5. Phases

| # | Phase | Status |
|---|---|---|
| 1 | Data build | done |
| 2 | Map prototype | done (local Playwright smoke test, screenshots delivered) |
| 3 | Pages | done |
| 4 | Polish | filters, search, mobile layout, OG/JSON-LD, photos, satellite view, sortable rankings — done |
| 5 | Deploy | done via Vercel API (source bundle + packed data); Git connection and custom domain are the user's next steps |
| 6 | Expansion to every CTBUH city | done 27 Sep 2026 |

---

## 6. Open items

- Photos: 1,907 of 8,076 towers; mainland China coverage 357 of 3,662. Options still open: outbound "search photos" links for photo-less towers, permission-based sourcing, or hand additions to `photos.json`.
- Search only matches CTBUH names; alternate/common names (CTBUH "also known as" fields, or hand aliases such as "CITIC Securities" → CITIC Financial Center Tower 1) are not searchable yet.
- 228 towers unplaced (no defensible coordinate); they do not appear on the map.
- 101 towers the CTBUH index lists for the original 58 cities (63 completed) are not in the dataset — the expansion added new cities only.
- Expansion towers use the CTBUH coordinate checked by reverse geocoding, not OSM-footprint verified like the first edition.
- Jersey City / Incheon could be folded into New York / Seoul if wanted.
- Connect a GitHub repo to the Vercel project so deploys happen on push; add the custom domain when bought.
- The report will need a re-run in roughly a year as the pipelines in Nanshan (+43), Futian (+16) and Old Toronto (+16) complete.
