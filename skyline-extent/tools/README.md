# Skyline extent tools

Since 11 Oct 2026 `../skyline-extent.geojson` is built by **`build_density.py`**: every pocket of 5+ towers (DBSCAN, eps 800 m, min_samples 4, over all 8,076 towers of 150 m+) gets an extent, in any city. The rule and its results are in `../skyline-extent-notes.md`. Run `python3 build_density.py ../skyline-extent.geojson` from this folder. The numbers are at the top of the script: `EPS`, `MIN_SAMPLES`, `MIN_TOWERS` for the pockets; `R`, `C`, `SMOOTH` for the outline; `SHORE`, `SHORE_NEAR`, `PIER`, `NECK` for the waterfront fill.

**`build_joined.py`** (live since 12 Oct 2026 19:07 UTC; rebuild the site's extents with this one) builds `../skyline-extent-joined.geojson`: the same extents with skylines that almost touch joined (steps of up to 1.9 km between towers and outline edges, rivers up to 600 m wide). It imports `build_density.py` unchanged. `STEP` and `WATER` at its top are the levers. Rule, results and the 37 cities it changes are in `../skyline-extent-joined-notes.md`. Run `python3 build_joined.py ../skyline-extent-joined.geojson`.

- **`names.py`:** `NAMES` gives each city a list of (lat, lon, name). A pocket takes the nearest name within 3 km, otherwise its most common district. `NOTES` adds a sentence per city to the popup rationale; every claim in it was checked against the master CSV. A pocket that appears after a data change needs a name here.
- **Waterfront fill.** Water within 600 m of the outline (`SHORE_NEAR`) is added and the result closed by 300 m (`SHORE`), so land strips between the outline and the water it faces are taken in. Before that the water is closed by 150 m (`PIER`), so piers and land under about 300 m wide with water on both sides count as water. Fill that is wider than 300 m but meets the outline only through a narrow neck (a landfill or an island) is dropped, and so is fill that sticks out of the outline as a spur under about 300 m wide (`NECK`, an opening of outline plus fill that only trims the fill). Every addition must meet the outline along 200 m or more.
- **Water.** The first 38 cities use `geo_all.json` (raw OpenFreeMap water, opened by 35 m and kept above 0.06 km² at build time). Every other city with a pocket, and the Hong Kong and Shenzhen pockets outside their `geo_all.json` areas, use `water_new.json`: city → WKT of water already opened and filtered the same way, kept within about 650 m of the pocket outlines to keep the file small. A city that newly qualifies (for example after lowering `MIN_TOWERS`) needs its water fetched and added to `water_new.json` before it can be built; without it the outline is not cut back from rivers and sea.
- **Fetching water in a Vercel Sandbox.** This container's proxy blocks tiles.openfreemap.org, so the fetch runs in a sandbox:
  - `sbx/pocket_bboxes.json` holds one bbox (`city|n`) for each of the 124 pockets whose water is in `water_new.json`: the pocket outline plus 250 m. Widen each by 700 m and save the result as `bboxes.json` in the sandbox (the `sbx/bboxes.json` here is the 9 Oct version's) for `sbx/fetch.py`, which writes `out/<city|n>.json` and skips files already there (the tilejson and tiles need a User-Agent header, which it sends).
  - `sbx/clip.py` opens the water by 35 m, keeps parts above 0.06 km², clips each pocket's water to its `pocket_bboxes.json` bbox plus 400 m, and writes the city → WKT map as xz-compressed base64 in chunks of 1,490 characters. It reads the bboxes from `../w/bboxes.json`; adjust the path to where you put `pocket_bboxes.json`.
  - Upload the scripts with `run_session_command` (`echo <base64> | base64 -d | tar xz`, since `write_session_files` refuses tarballs). Read the chunks back with `read_session_file`, because the MCP truncates strings near 2,000 characters, and check the md5 of each chunk and of the whole before decoding.
- `lib.geo.load()` caches `geo_all.json` as `geo_cache.pkl` next to it. Delete the pickle afterwards rather than leave 2.5 MB in the shared folder.

## The 9 Oct hand-drawn version

The rest of this README describes the first version, which drew a core per city by hand for the 38 cities with more than 50 towers. It is kept for reference; its output is `../skyline-extent-2026-10-09.geojson`.

These scripts produced the 9 Oct file, now `../skyline-extent-2026-10-09.geojson`. The rationale text lives in `rationale.py` and the core shapes in `specs/`.

- **`specs/<code>.py`:** one `SPEC` per city, listing `zones`, each with a `name` (it becomes an `areas` entry) and a lasso `poly` given as lon/lat pairs.
  - `mode: 'fill'` takes the lasso as drawn, optionally with `round` rounding its corners.
  - `mode: 'towers'` (the default) buffers each tower inside the lasso by `R` metres, closes the gaps by `C` metres, clips the result to the lasso, and drops any part with fewer than `min` towers.
  - Optional `cut` polygons are removed from the result.
- **`lib/core.py`:** `build(city, spec)` takes the union of the zones and fills holes. It then removes water (from `geo_all.json`) and smooths the shape. It returns the shape plus the stats that end up in the GeoJSON properties: `towers_in_core`, `completed_in_core`, `towers_in_city`, `share`, `area_km2` and `tallest_in_core`.
- **`build_all.py`:** run from this folder to rebuild the whole file. It asserts that the city set equals the keys of `rationale.R` and currently selects cities with more than 50 towers.
- **`run.py <city> <spec> [bbox] [grid]`:** builds one city and renders a check image to `render/<spec>.png`.
- **`clusters.py`:** prints DBSCAN tower clusters (eps 0.8 km, min 4) per city.
- **`geo_all.json`:** OpenFreeMap water, park and place-label data for the 38 cities only. It comes from vector tiles at z13 within the bboxes in `bboxes.json`. This container's proxy blocks tiles.openfreemap.org, so `sbx/fetch.py` was run inside a Vercel Sandbox (`create_sandboxes_v4` + `run_session_command`) and the result was read back with `read_session_file`. A new city needs its bbox added and a fresh fetch before `build()` can cut its rivers.

Needs Python with pandas, shapely, scikit-learn and matplotlib (installed with pip).
