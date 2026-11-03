#!/usr/bin/env python3
"""H3 resolution-5 land grid and Cliopatria-on-grid helpers for EmpireMap.

Library (import from tools/):
    land_cells(res=5)                -> {cell: index} for the world's land, cached in
                                        data/grid/land_r5.txt (sorted, one cell per line)
    shape_cells(geometry, res=5)     -> set of cells whose centre falls inside the geometry
                                        (h3.geo_to_cells), plus the centroid cell when the
                                        shape is smaller than one cell (or yields no cell)
    polity_cells(slug, year, res=5)  -> union of shape_cells over the Cliopatria shapes of
                                        that slug alive in that year (parsed-feature cache
                                        and per-shape cell cache under /tmp/claude-0/work/grid/)
    cells_to_geojson(cells)          -> GeoJSON geometry (h3.cells_to_h3shape), antimeridian-safe

Command line:
    python3 -I grid.py land          build or verify the land cell list
    python3 -I grid.py cache         parse Cliopatria into the feature cache
    python3 -I grid.py cells         precompute the cell cache for every shape alive at an anchor

Conventions shared with the rest of the project: years are integers, negative for
BCE; a Name starting with "(" is an umbrella or relation entity, not territory;
slugs come from tools/slug.py.
"""
import json
import math
import os
import pickle
import sys
import time
from pathlib import Path

import h3
import numpy as np
import shapely
from shapely.geometry import MultiPolygon, Polygon, box, shape

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from slug import slugify  # noqa: E402

HIST = HERE.parent
DATA = HIST / "data"
GRID_DIR = DATA / "grid"
ANCHOR_DIR = DATA / "anchors"
WORK = Path("/tmp/claude-0/work/grid")
CLIO = Path("/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson")
NE_LAND = Path("/tmp/claude-0/dl/ne/ne_50m_land.shp")

RES = 5
CELL_KM2 = 252.9          # mean area of a resolution-5 hexagon, km2 (h3: 252.9039)
SOUTH_LIMIT = -60.0       # nothing south of 60 S (drops Antarctica entirely)

ANCHOR_YEARS = list(range(-6000, 1601, 100)) + list(range(1610, 2021, 10)) + [2024]


def anchor_name(year):
    """File stem for an anchor year: m3400 for -3400, p0800 for 800, p2024 for 2024."""
    return ("m%04d" % -year) if year < 0 else ("p%04d" % year)


def anchor_year(stem):
    """Inverse of anchor_name."""
    stem = Path(stem).stem
    return -int(stem[1:]) if stem[0] == "m" else int(stem[1:])


# ----------------------------------------------------------------------------
# Antimeridian handling
# ----------------------------------------------------------------------------

def _unwrap_ring(coords):
    """Make longitudes continuous along a ring (no jump larger than 180 degrees)."""
    c = np.asarray(coords, dtype=float)
    if len(c) < 2:
        return c
    d = np.diff(c[:, 0])
    step = np.where(d > 180, -360.0, np.where(d < -180, 360.0, 0.0))
    shift = np.concatenate([[0.0], np.cumsum(step)])
    out = c.copy()
    out[:, 0] = c[:, 0] + shift
    return out


def _flatten(geom):
    """Polygons of any shapely geometry, dropping empties and non-areal parts."""
    if geom is None or geom.is_empty:
        return []
    if isinstance(geom, Polygon):
        return [geom]
    if hasattr(geom, "geoms"):
        out = []
        for g in geom.geoms:
            out.extend(_flatten(g))
        return out
    return []


def _shift(geom, dx):
    return shapely.transform(geom, lambda c: np.column_stack([c[:, 0] + dx, c[:, 1]]))


def _safe_intersection(geom, clip):
    try:
        return geom.intersection(clip)
    except Exception:
        return shapely.make_valid(geom).intersection(clip)


def split_antimeridian(poly):
    """Split a polygon so every piece lies within [-180, 180] and spans at most 180 degrees.

    Rings that jump across the antimeridian are unwrapped first (a vertex pair whose
    longitudes differ by more than 180 is read as the short way round), the unwrapped
    polygon is cut at +-180 and the outer pieces shifted back; any piece still wider
    than 180 degrees is cut at its middle meridian.
    """
    ext = _unwrap_ring(poly.exterior.coords)
    holes = [_unwrap_ring(r.coords) for r in poly.interiors]
    # bring a hole next to the exterior if unwrapping placed it a world away
    ex_mid = (ext[:, 0].min() + ext[:, 0].max()) / 2
    fixed_holes = []
    for h in holes:
        hm = (h[:, 0].min() + h[:, 0].max()) / 2
        k = round((ex_mid - hm) / 360)
        if k:
            h = h.copy()
            h[:, 0] += 360 * k
        fixed_holes.append(h)
    p = Polygon(ext, fixed_holes)
    if not p.is_valid:
        p = shapely.make_valid(p)
    minx, _, maxx, _ = p.bounds
    pieces = []
    if minx >= -180 and maxx <= 180:
        pieces = _flatten(p)
    else:
        k0 = math.floor((minx + 180) / 360)
        k1 = math.floor((maxx + 180 - 1e-9) / 360)
        for k in range(k0, k1 + 1):
            clip = box(-180 + 360 * k, -90, 180 + 360 * k, 90)
            part = _safe_intersection(p, clip)
            if k:
                part = _shift(part, -360 * k)
            pieces.extend(_flatten(part))
    out = []
    for q in pieces:
        qminx, _, qmaxx, _ = q.bounds
        if qmaxx - qminx > 180:
            mid = (qminx + qmaxx) / 2
            out.extend(_flatten(_safe_intersection(q, box(qminx - 1, -90, mid, 90))))
            out.extend(_flatten(_safe_intersection(q, box(mid, -90, qmaxx + 1, 90))))
        else:
            out.append(q)
    return out


def prepare_polygons(geometry):
    """Polygons of a shapely geometry or GeoJSON dict, antimeridian-split, each at most 180 wide."""
    if isinstance(geometry, dict):
        geometry = shape(geometry)
    out = []
    for p in _flatten(geometry):
        if p.is_empty:
            continue
        minx, _, maxx, _ = p.bounds
        coords_ok = minx >= -180 and maxx <= 180 and maxx - minx <= 180
        jump = False
        if coords_ok:
            c = np.asarray(p.exterior.coords)
            jump = bool((np.abs(np.diff(c[:, 0])) > 180).any())
        if coords_ok and not jump:
            out.append(p)
        else:
            out.extend(split_antimeridian(p))
    return out


# ----------------------------------------------------------------------------
# Land grid
# ----------------------------------------------------------------------------

_LAND_CACHE = {}


def _land_path(res):
    return GRID_DIR / ("land_r%d.txt" % res)


def _build_land(res):
    import shapefile  # pyshp
    t = time.time()
    reader = shapefile.Reader(str(NE_LAND))
    clip = box(-180, SOUTH_LIMIT, 180, 90)
    cells = set()
    island_cells = set()
    npoly = 0
    for rec in reader.iterShapes():
        g = shape(rec.__geo_interface__)
        if g.is_empty:
            continue
        if not g.is_valid:
            g = shapely.make_valid(g)
        g = _safe_intersection(g, clip)
        for p in prepare_polygons(g):
            if p.area <= 0:
                continue
            npoly += 1
            got = h3.geo_to_cells(p, res)
            if not got:
                # an island smaller than one cell (no cell centre on it): keep the cell
                # that holds its centroid, the same rule shape_cells applies to shapes
                c = _centroid_cell([p], res)
                island_cells.add(c)
                got = [c]
            cells.update(got)
    island_cells -= {c for c in island_cells if c not in cells}  # (always a subset; kept for clarity)
    cells = sorted(cells)
    GRID_DIR.mkdir(parents=True, exist_ok=True)
    tmp = _land_path(res).with_suffix(".tmp")
    with open(tmp, "w") as f:
        f.write("\n".join(cells))
        f.write("\n")
    os.replace(tmp, _land_path(res))
    ipath = GRID_DIR / ("land_r%d_island_cells.txt" % res)
    with open(ipath, "w") as f:
        f.write("\n".join(sorted(island_cells)))
        f.write("\n")
    print("land_cells: res %d, %d polygons, %d cells (%d island centroid cells), %.1f s" % (
        res, npoly, len(cells), len(island_cells), time.time() - t), file=sys.stderr)
    return cells


def land_cells(res=RES):
    """The H3 cells of the world's land (Natural Earth 50m, nothing south of 60 S) as {cell: index}.

    The index is the line number (from 0) in data/grid/land_r<res>.txt, which is the
    sorted cell list; anchors and every other grid file refer to cells by that index.
    """
    if res in _LAND_CACHE:
        return _LAND_CACHE[res]
    path = _land_path(res)
    if path.exists():
        with open(path) as f:
            cells = [line.strip() for line in f if line.strip()]
    else:
        cells = _build_land(res)
    d = {c: i for i, c in enumerate(cells)}
    _LAND_CACHE[res] = d
    return d


def land_cells_int(res=RES):
    """The land cells as a sorted numpy uint64 array (same order as land_cells)."""
    d = land_cells(res)
    arr = np.fromiter((h3.str_to_int(c) for c in d), dtype=np.uint64, count=len(d))
    order = np.argsort(arr)
    return arr[order], order  # sorted ints, and the index into the text order for each


# ----------------------------------------------------------------------------
# Shapes to cells
# ----------------------------------------------------------------------------

def approx_km2(geometry):
    """Rough planar area in km2 of a lon/lat geometry (enough to compare with one cell)."""
    total = 0.0
    for p in _flatten(geometry):
        lat = p.centroid.y if not p.is_empty else 0.0
        total += abs(p.area) * 111.19 ** 2 * max(math.cos(math.radians(lat)), 0.01)
    return total


def _centroid_cell(polys, res):
    best = max(polys, key=lambda p: p.area)
    c = best.centroid
    if c.is_empty or not best.contains(c):
        c = best.representative_point()
    return h3.latlng_to_cell(c.y, c.x, res)


def shape_cells(geometry, res=RES):
    """Cells whose centre falls inside the geometry, as a set of H3 strings.

    Uses h3.geo_to_cells on each antimeridian-safe polygon. When the shape is smaller
    than one cell (or no centre falls inside it) the cell containing the centroid of its
    largest part is added so that no shape vanishes.
    """
    polys = prepare_polygons(geometry)
    cells = set()
    for p in polys:
        try:
            cells.update(h3.geo_to_cells(p, res))
        except Exception:
            # pathological ring: try the valid version
            for q in _flatten(shapely.make_valid(p)):
                cells.update(h3.geo_to_cells(q, res))
    if polys and (not cells or approx_km2(geometry) < h3.average_hexagon_area(res, unit="km^2")):
        cells.add(_centroid_cell(polys, res))
    return cells


# ----------------------------------------------------------------------------
# Cliopatria feature cache
# ----------------------------------------------------------------------------

FEATURES_PKL = WORK / "features.pkl"
CELLS_DIR = WORK / ("cells_r%d" % RES)
_FEATURES = None


def build_feature_cache():
    """Parse the Cliopatria GeoJSON once into WORK/features.pkl (properties, slug, bbox, WKB)."""
    WORK.mkdir(parents=True, exist_ok=True)
    t = time.time()
    with open(CLIO) as f:
        data = json.load(f)
    feats = []
    for i, ft in enumerate(data["features"]):
        p = ft["properties"]
        g = shape(ft["geometry"])
        name = p["Name"]
        feats.append({
            "i": i,
            "name": name,
            "slug": slugify(name),
            "umbrella": name.startswith("("),
            "from": int(p["FromYear"]),
            "to": int(p["ToYear"]),
            "area": float(p["Area"]),
            "type": p.get("Type", ""),
            "wikipedia": p.get("Wikipedia", ""),
            "wikidata": p.get("Wikidata", ""),
            "seshat": p.get("SeshatID", ""),
            "components": p.get("Components", ""),
            "memberof": p.get("MemberOf", ""),
            "bbox": tuple(round(v, 4) for v in g.bounds),
            "nvert": int(shapely.get_num_coordinates(g)),
            "wkb": shapely.to_wkb(g),
        })
    del data
    tmp = FEATURES_PKL.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(feats, f, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(tmp, FEATURES_PKL)
    print("feature cache: %d features, %.1f s, %.1f MB" % (
        len(feats), time.time() - t, FEATURES_PKL.stat().st_size / 1e6), file=sys.stderr)
    return feats


def load_features():
    """The parsed Cliopatria features (list of dicts with 'wkb'), from the cache."""
    global _FEATURES
    if _FEATURES is None:
        if FEATURES_PKL.exists():
            with open(FEATURES_PKL, "rb") as f:
                _FEATURES = pickle.load(f)
        else:
            _FEATURES = build_feature_cache()
    return _FEATURES


def feature_geometry(feat):
    return shapely.from_wkb(feat["wkb"])


def feature_cells_int(feat, res=RES):
    """Cells of one feature as a sorted uint64 array, cached per shape under WORK/cells_r<res>/."""
    CELLS_DIR.mkdir(parents=True, exist_ok=True)
    path = CELLS_DIR / ("%05d.npy" % feat["i"])
    if path.exists():
        return np.load(path)
    cells = shape_cells(feature_geometry(feat), res)
    arr = np.fromiter((h3.str_to_int(c) for c in cells), dtype=np.uint64, count=len(cells))
    arr.sort()
    tmp = path.with_suffix(".tmp.npy")
    np.save(tmp, arr)
    os.replace(tmp, path)
    return arr


def features_alive(year, slug=None, leaf_only=False):
    """Cliopatria features alive in a year (FromYear <= year <= ToYear), optionally one slug."""
    out = []
    for ft in load_features():
        if ft["from"] <= year <= ft["to"]:
            if slug is not None and ft["slug"] != slug:
                continue
            if leaf_only and ft["umbrella"]:
                continue
            out.append(ft)
    return out


def polity_cells(slug, year, res=RES, land_only=False):
    """Cells of a Cliopatria polity (by slug) in a year, as a set of H3 strings.

    Union over every shape of that slug alive in the year. With land_only the set is
    restricted to the land grid. Returns an empty set when nothing is alive.
    """
    cells = set()
    for ft in features_alive(year, slug=slug):
        arr = feature_cells_int(ft, res)
        cells.update(h3.int_to_str(int(v)) for v in arr)
    if land_only:
        land = land_cells(res)
        cells = {c for c in cells if c in land}
    return cells


# ----------------------------------------------------------------------------
# Display
# ----------------------------------------------------------------------------

def cells_to_geojson(cells, decimals=None):
    """GeoJSON geometry (Polygon or MultiPolygon) for a set of cells, via h3.cells_to_h3shape.

    Polygons that straddle the antimeridian are split at it. With decimals, coordinates
    are rounded. Returns None for an empty set.
    """
    cells = list(cells)
    if not cells:
        return None
    if isinstance(cells[0], (int, np.integer)):
        cells = [h3.int_to_str(int(c)) for c in cells]
    shp = h3.cells_to_h3shape(cells)
    geom = shape(shp.__geo_interface__)
    polys = prepare_polygons(geom)
    if decimals is not None:
        polys = [shapely.set_precision(p, 10 ** -decimals, mode="pointwise") for p in polys]
        polys = [q for p in polys for q in _flatten(p)]
    if not polys:
        return None
    geom = polys[0] if len(polys) == 1 else MultiPolygon(polys)
    gj = shapely.geometry.mapping(geom)
    if decimals is not None:
        gj = _round_geojson(gj, decimals)
    return gj


def _round_geojson(gj, decimals):
    def rc(x):
        if isinstance(x, (list, tuple)):
            return [rc(v) for v in x]
        return round(float(x), decimals)
    return {"type": gj["type"], "coordinates": rc(gj["coordinates"])}


# ----------------------------------------------------------------------------
# Runs (compact index lists)
# ----------------------------------------------------------------------------

def to_runs(indices):
    """Sorted indices -> ["start-end", int, ...] with consecutive runs collapsed."""
    idx = np.asarray(sorted(set(int(i) for i in indices)), dtype=np.int64)
    if idx.size == 0:
        return []
    breaks = np.where(np.diff(idx) != 1)[0] + 1
    starts = np.concatenate([[0], breaks])
    ends = np.concatenate([breaks, [idx.size]])
    out = []
    for s, e in zip(starts, ends):
        a, b = int(idx[s]), int(idx[e - 1])
        out.append(a if a == b else "%d-%d" % (a, b))
    return out


def from_runs(runs):
    """["start-end", int, ...] -> sorted list of ints."""
    out = []
    for r in runs:
        if isinstance(r, str):
            a, b = r.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(r))
    return out


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def _cli(argv):
    cmd = argv[1] if len(argv) > 1 else "land"
    if cmd == "land":
        d = land_cells(RES)
        print("land cells r%d: %d" % (RES, len(d)))
    elif cmd == "cache":
        feats = load_features()
        print("features: %d" % len(feats))
    elif cmd == "cells":
        # optional "k/n": this worker takes every n-th shape starting at k
        k, n = (int(v) for v in argv[2].split("/")) if len(argv) > 2 else (0, 1)
        feats = load_features()
        need = [ft for ft in feats if not ft["umbrella"] and any(ft["from"] <= y <= ft["to"] for y in ANCHOR_YEARS)]
        need = need[k::n]
        t = time.time()
        for n, ft in enumerate(need):
            feature_cells_int(ft, RES)
            if (n + 1) % 200 == 0:
                print("  %d/%d shapes, %.0f s" % (n + 1, len(need), time.time() - t), file=sys.stderr)
        print("cell cache: %d shapes, %.0f s" % (len(need), time.time() - t))
    else:
        print(__doc__)


if __name__ == "__main__":
    _cli(sys.argv)
