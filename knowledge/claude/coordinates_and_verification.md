# Coordinates & verification — skyscrapers ≥150 m, by district

**Deliverables**

| File | What it is |
|---|---|
| `skyscrapers_150m.geojson` | 6,237 Point features (WGS84 / CRS84), one per tower, with full attributes. This is the map layer. |
| `skyscrapers_150m_by_district.csv` | Same 6,237 rows as a flat table, with `lat` / `lon` columns added. |
| `skyscrapers_150m_unplaced.csv` | 184 towers for which no defensible coordinate could be established. Deliberately excluded from the map rather than given a fake pin. |

**Coverage:** 6,237 of 6,421 towers placed (97.1%).

## How each coordinate was obtained

`coord_precision` on every feature says exactly what the point represents:

| Value | Count | Meaning |
|---|---:|---|
| `building` | 3,693 | CTBUH database coordinate for the tower |
| `building-verified` | 2,427 | OpenStreetMap building-footprint centroid, matched to the CTBUH record on height and/or name — the most precise class |
| `approximate` | 78 | Street- or area-level only. **Not** the building itself; suppress or style differently on a map |
| `building-geocoded` | 22 | Geocoded to a named building matching the CTBUH address |
| `complex` | 17 | Centre of the multi-tower complex the building belongs to |

`shares_point_with` counts other towers carrying the identical coordinate — 239 towers sit on 111 shared points, all of them genuine multi-tower complexes given a single point by the source (Wanda East Port 1–5 in Dalian, Galaxia 1–5 in Hong Kong, Binghatti Skyrise in Dubai, and so on). A map should spiderfy or offset these so each tower stays clickable.

## Verification

1. **OpenStreetMap cross-check.** 3,712 towers (60%) were matched to an independent OSM building footprint. Median offset between the CTBUH point and the OSM footprint centroid: **15.2 m** — i.e. the two sources are pointing at the same roof. Where the match was solid, the point was upgraded to the footprint centroid.
2. **Wikidata landmark check.** 29 well-known towers were checked against Wikidata's independently-sourced coordinates. Every tower that resolved to the correct Wikidata entity agreed to between **1 m and 49 m** (Guangzhou CTF 1 m, Petronas 1 1 m, Tianjin CTF 1 m, Jin Mao 4 m, Burj Khalifa 22 m, Shanghai Tower 29 m). Three apparent failures were name collisions in Wikidata's search, not coordinate errors — Beijing's CITIC Tower resolved to Hong Kong's, Balneário Camboriú's Iconic Tower to Cairo's, and Jinan's Ping An Finance Center to Shenzhen's.
3. **District spot-check.** 250 randomly sampled towers were reverse-geocoded and the returned administrative hierarchy compared with the assigned district. 204 matched on the first pass; of the 46 flagged, 45 were artefacts (the geocoder returning nothing below city level for Doha, Singapore, Miami, Los Angeles and Balneário; romanisation differences such as Watthana / Vadhana; correct parent-child relationships such as Tseung Kwan O inside Sai Kung District; Mumbai's MCGM ward letters, which the geocoder does not expose). **One real misassignment was found**, which prompted a full audit of Kuala Lumpur (see below).
4. **Geometric sanity.** Every point falls inside its city's bounding box; no nulls; heights 150–828 m. Per-city scatter plots reproduce the known shape of each skyline — Manhattan's two clusters, Dubai's Marina/Downtown split, Hong Kong's harbour ring, Shenzhen's west-east corridor.

## Known limits

- The 184 unplaced towers are concentrated in Shenyang (34), Tianjin (16), Wuhan (16), Nanning (15), Chongqing (10) and Ningbo (10). They are mostly recent residential complexes in cities where OSM carries almost no height tagging and the source database has no coordinate. They have no siblings already in the file to borrow a complex point from.
- Kuala Lumpur's "districts" are informal neighbourhood clusters, not official administrative units — KL's federal territory has no district tier. All 203 KL towers were therefore re-checked against OpenStreetMap's suburb polygons: 190 agreed, 13 were corrected (plus one sibling tower at the Bangsar/Damansara Heights boundary). Net effect on the KL district table in *District_skyscrapers_v2*: KLCC & Golden Triangle 64 → 63, Cheras / Bandar Tun Razak 29 → 28, Kampung Baru / Chow Kit 23 → 25, Bangsar / Brickfields / KL Sentral 25 → 23, Sentul / Titiwangsa 9 → 10, Kepong 1 → 3, and the single unassigned tower resolved. No other city's ranking changed.
- `approximate` (78) points should not be presented as the building's exact location.

## Licensing

Building data © CTBUH / Council on Vertical Urbanism. Coordinates derived in part from OpenStreetMap contributors (ODbL). Both must be attributed on any published map.
