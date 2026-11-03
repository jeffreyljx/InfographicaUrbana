#!/usr/bin/env python3
"""Display test for an anchor year: cells -> polygons -> GeoJSON (and a PNG when PIL is importable).

    python3 -I preview.py 1600

Reads data/anchors/<stem>.json, converts each polity's cells with grid.cells_to_geojson,
reports the vertex count and byte size with full and 3-decimal coordinates, writes
data/grid/preview_<year>.geojson (3-decimal version) when it is under 15 MB, and renders
data/grid/preview_<year>.png (equirectangular, lon -180..180, lat -60..90, one fill per
polity) with PIL if it is installed; otherwise says so.
"""
import colorsys
import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import grid  # noqa: E402

MAX_BYTES = 15 * 1024 * 1024


def _count_vertices(gj):
    if gj is None:
        return 0
    if gj["type"] == "Polygon":
        return sum(len(r) for r in gj["coordinates"])
    return sum(len(r) for p in gj["coordinates"] for r in p)


def _colour(slug):
    h = int(hashlib.md5(slug.encode()).hexdigest()[:6], 16) / 0xFFFFFF
    s = 0.55 + 0.3 * (int(hashlib.md5(slug.encode()).hexdigest()[6:8], 16) / 255)
    r, g, b = colorsys.hsv_to_rgb(h, s, 0.85)
    return (int(r * 255), int(g * 255), int(b * 255))


def main(argv):
    year = int(argv[1]) if len(argv) > 1 else 1600
    t0 = time.time()
    path = grid.ANCHOR_DIR / (grid.anchor_name(year) + ".json")
    with open(path) as f:
        anchor = json.load(f)
    land = grid.land_cells()
    cells_by_index = list(land)
    names = {ft["slug"]: ft["name"] for ft in grid.load_features() if ft["from"] <= year <= ft["to"]}

    full, rounded = [], []
    nv_full = nv_round = 0
    for slug, runs in anchor["owners"].items():
        cells = [cells_by_index[i] for i in grid.from_runs(runs)]
        gj = grid.cells_to_geojson(cells)
        gj3 = grid.cells_to_geojson(cells, decimals=3)
        nv_full += _count_vertices(gj)
        nv_round += _count_vertices(gj3)
        props = {"slug": slug, "name": names.get(slug, slug), "cells": len(cells)}
        full.append({"type": "Feature", "properties": props, "geometry": gj})
        rounded.append({"type": "Feature", "properties": props, "geometry": gj3})
    fc_full = json.dumps({"type": "FeatureCollection", "year": year, "features": full}, separators=(",", ":"))
    fc_round = json.dumps({"type": "FeatureCollection", "year": year, "features": rounded}, separators=(",", ":"))
    out = {
        "year": year, "polities": len(full), "cells": anchor["cells_owned"],
        "vertices_full": nv_full, "bytes_full": len(fc_full.encode()),
        "vertices_3dp": nv_round, "bytes_3dp": len(fc_round.encode()),
        "geojson_written": False, "png": None, "seconds_polygons": round(time.time() - t0, 1),
    }
    gpath = grid.GRID_DIR / ("preview_%d.geojson" % year)
    if out["bytes_3dp"] < MAX_BYTES:
        with open(gpath, "w") as f:
            f.write(fc_round)
        out["geojson_written"] = str(gpath)

    try:
        from PIL import Image, ImageDraw
    except ImportError:
        out["png"] = "skipped: PIL not importable"
        print(json.dumps(out, indent=1))
        return out
    t1 = time.time()
    W, H = 3600, 1500  # 10 px per degree; lon -180..180, lat 90..-60
    def xy(lon, lat):
        return ((lon + 180) * 10, (90 - lat) * 10)
    img = Image.new("RGB", (W, H), (214, 228, 240))  # sea
    draw = ImageDraw.Draw(img)
    # land background from the same Natural Earth polygons as the grid
    import shapefile
    from shapely.geometry import box, shape
    import shapely
    clip = box(-180, grid.SOUTH_LIMIT, 180, 90)
    for rec in shapefile.Reader(str(grid.NE_LAND)).iterShapes():
        g = shape(rec.__geo_interface__)
        if not g.is_valid:
            g = shapely.make_valid(g)
        for p in grid.prepare_polygons(g.intersection(clip)):
            draw.polygon([xy(*c) for c in p.exterior.coords], fill=(236, 233, 226))
            for r in p.interiors:
                draw.polygon([xy(*c) for c in r.coords], fill=(214, 228, 240))
    # polities, largest first so enclaves drawn later sit on top
    feats = sorted(rounded, key=lambda ft: -ft["properties"]["cells"])
    for ft in feats:
        gj = ft["geometry"]
        if gj is None:
            continue
        col = _colour(ft["properties"]["slug"])
        polys = [gj["coordinates"]] if gj["type"] == "Polygon" else gj["coordinates"]
        for rings in polys:
            draw.polygon([xy(*c) for c in rings[0]], fill=col)
            for hole in rings[1:]:
                draw.polygon([xy(*c) for c in hole], fill=(236, 233, 226))
    draw.text((20, 20), "%d%s  %d polities  Cliopatria on H3 r5" % (abs(year), " BCE" if year < 0 else "", len(feats)),
              fill=(30, 30, 30))
    ppath = grid.GRID_DIR / ("preview_%d.png" % year)
    img.save(ppath, optimize=True)
    out["png"] = str(ppath)
    out["png_bytes"] = ppath.stat().st_size
    out["seconds_png"] = round(time.time() - t1, 1)
    print(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    main(sys.argv)
