# How metro/db was built

Scripts from the thread "Metro systems database" (12 Oct 2026). Paths inside them point at that session's scratch folders; change `SP` and `OV` at the top of each script to rerun.

1. `build_systems.py` → `systems.json`: the 239 candidate systems from Wikipedia's List of metro systems, with the definition's system rulings.
2. Regional passes (one agent per region, brief in `BRIEF.md`) wrote `workers/wNN-*.lines.jsonl` and `.stages.jsonl`: line facts and dated stages from Wikipedia.
3. OpenStreetMap, from the planet file of 8 Oct 2026 on AWS (`s3://osm-pds`), read by byte range: `pbf_find.py` locates the sections, `rels.py` keeps the metro route relations, `osm_lines.py` groups them into lines, `pbf_stream_lowmem.py ways|nodes PART NP` streams the ways and then the nodes they need (`need_nodes.py`), and `assemble_pbf.py` builds each line's geometry and station sequence. The result is `osm_lines_built.json.gz` (gunzip it to rerun step 4 without the planet file).
4. `merge.py OUTDIR` joins the passes with the OSM lines and writes every file in `metro/db/`; `qa.py OUTDIR` prints coverage; `build_viewer.py OUTDIR viewer_template.html OUT.html` builds the World Metro Database page.
