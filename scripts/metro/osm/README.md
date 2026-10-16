# Station structures from the OpenStreetMap planet

These scripts read the planet file on Amazon S3 (`https://osm-pds.s3.amazonaws.com/planet-latest.osm.pbf`, the
15 Oct 2026 copy for the first run) by byte range, so nothing larger than about 1 GB is ever held, and write the
extracts `scripts/metro/build_structures.py` reads. Each takes the working folder as its first argument and writes
into `<folder>/data/`. They need pyosmium and numpy. The section offsets in them (`SIZE` in pbf.py, `FIRST_WAY`,
`FIRST_REL`) belong to that planet: rerun `find.py` and update them for a newer one.

1. `find.py DIR` finds where the ways and relations sections start.
2. `bounds.py DIR A B NAME` cuts a section into blob-aligned 1 GB chunks (way_bounds.json, node_bounds.json).
3. `rels.py DIR` downloads the relations section (0.9 GB) and keeps stop areas and station, platform and indoor
   multipolygons; `relsel.py DIR` keeps the stop areas of the page's stations (metro/db/metro_stations.csv) with
   their groups, and lists the ways and nodes they need.
4. `ways.py DIR PART NP` (run NP of them, PART 0..NP-1) keeps platforms, station and indoor areas, underground
   footways, steps and corridors, entrances, and the member ways from step 3.
5. `need.py DIR` lists the nodes those ways need; `nodes.py DIR PART NP` keeps their coordinates (nxy.*.npy) and
   every entrance node with its tags (nodes.*.jsonl).
6. `ents.py DIR PART NP` keeps every entrance=* node near a page station (ents.*.jsonl); the builder takes the
   ones that say they are a metro exit (entrance_marker:subway, or a name such as "A口" or "Exit 2").

Then, from the site's root:

    python3 scripts/metro/build_metro.py METRO_DB public/metro/metro.json DIR/station_index.json
    python3 scripts/metro/build_structures.py METRO_DB public/metro/metro.json DIR/station_index.json DIR/data public/metro/structures COVERAGE.csv
