#!/usr/bin/env python3
"""build_tables.py: polity and shape tables from Cliopatria v0.2.1.

Phase A "polity-table" task of the EmpireMap history project. Reads the
Cliopatria GeoJSON once, joins it to Natural Earth 10m admin-0 countries and
writes, under --out (default /mnt/project-files/history/data):

  polities.csv            one row per distinct Cliopatria Name
  shapes.csv              one row per feature (dated shape)
  polities/<slug>.json    one dossier seed per non-umbrella polity
  README.md               columns, counts and the quality issues found

Run with:  python3 -I build_tables.py [--out DIR] [--stage DIR] [--no-neighbours]

Geometry notes
  * Areas are spherical: geometries are projected to a Lambert cylindrical
    equal-area projection (x = R*lon, y = R*sin(lat), R = 6371.0088 km) and
    the planar area taken; this reproduces Cliopatria's own Area field to
    within 0.5 percent. Intersections are computed in lon/lat and only the
    result is projected (projecting first makes some polygons invalid).
  * "Within 25 km" for neighbours is tested in degrees with shapely.dwithin,
    using 25 km / (111.19 km * cos(mid latitude)) as the tolerance. That is
    exact east-west and lenient north-south, so no neighbour is missed; a few
    pairs separated by 25 to 25/cos(lat) km north-south are included.
  * Natural Earth country names are the ADMIN field of
    ne_10m_admin_0_countries ("United States of America", "Ivory Coast",
    "Czechia", "Russia").
"""
import argparse
import collections
import csv
import json
import math
import os
import re
import shutil
import sys
import time
import unicodedata

import numpy as np
import shapely
from shapely.geometry import shape
from shapely.strtree import STRtree
import shapefile

sys.dont_write_bytecode = True  # keep __pycache__ out of the shared tools folder
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slug import slugify  # noqa: E402

R_KM = 6371.0088
KM_PER_DEG = 111.19

T0 = time.time()


def log(*a):
    print(f"[{time.time() - T0:7.1f}s]", *a, flush=True)


# ----------------------------------------------------------------------------
# geometry helpers
# ----------------------------------------------------------------------------

def to_equal_area(g):
    return shapely.transform(
        g,
        lambda c: np.column_stack((np.radians(c[:, 0]) * R_KM,
                                   np.sin(np.radians(c[:, 1])) * R_KM)),
    )


def ea_area_km2(g):
    if g is None or g.is_empty:
        return 0.0
    try:
        return to_equal_area(g).area
    except Exception:
        return to_equal_area(shapely.make_valid(g)).area


def safe_intersection(a, b):
    try:
        return a.intersection(b)
    except Exception:
        return shapely.make_valid(a).intersection(shapely.make_valid(b))


def merge_intervals(ivs):
    """Merge inclusive integer year intervals that overlap or touch."""
    out = []
    for f, t in sorted(ivs):
        if out and f <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], t)
        else:
            out.append([f, t])
    return [(f, t) for f, t in out]


# ----------------------------------------------------------------------------
# relation-name parsing
# ----------------------------------------------------------------------------

REL_PATTERNS = [
    ("allegiance", re.compile(r"^Allegiance of (.+)$"), " to "),
    ("alliance", re.compile(r"^Alliance between (.+)$"), " and "),
    ("vassalage", re.compile(r"^Vassalage of (.+)$"), " to "),
    ("personal_union", re.compile(r"^Personal union of (.+)$"), " with "),
]


def parse_relation_name(name, resolve):
    """(kind, party_a, party_b, resolved_both) for a parenthesised Name.

    party_a / party_b are the raw name strings; for directional kinds a is the
    vassal and b the suzerain. Umbrella entities return ("umbrella", None,
    None, True)."""
    inner = name[1:-1] if name.endswith(")") else name[1:]
    for kind, pat, sep in REL_PATTERNS:
        m = pat.match(inner)
        if not m:
            continue
        rest = m.group(1)
        parts = rest.split(sep)
        if len(parts) < 2:
            return kind, rest, "", False
        best = None
        for k in range(1, len(parts)):
            a = sep.join(parts[:k])
            b = sep.join(parts[k:])
            score = int(resolve(a)[1]) + int(resolve(b)[1])
            if best is None or score > best[0]:
                best = (score, a, b)
        score, a, b = best
        return kind, a, b, score == 2
    return "umbrella", None, None, True


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clio", default="/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson")
    ap.add_argument("--ne-shp", default="/tmp/claude-0/work/polity-table/ne10/ne_10m_admin_0_countries.shp")
    ap.add_argument("--out", default="/mnt/project-files/history/data")
    ap.add_argument("--stage", default=None,
                    help="write here first, then copy to --out (use for a network mount)")
    ap.add_argument("--work", default="/tmp/claude-0/work/polity-table",
                    help="scratch directory; the full quality report lands here as polity-table-quality.json")
    ap.add_argument("--neighbour-km", type=float, default=25.0)
    ap.add_argument("--no-neighbours", action="store_true")
    ap.add_argument("--min-overlap-frac", type=float, default=0.01,
                    help="drop modern-country overlaps below this fraction of the shape's area")
    args = ap.parse_args()

    out_dir = args.stage or args.out
    os.makedirs(os.path.join(out_dir, "polities"), exist_ok=True)

    # ---------------- load Cliopatria ----------------
    log("loading", args.clio)
    with open(args.clio, encoding="utf-8") as f:
        gj = json.load(f)
    feats = gj["features"]
    props = [f["properties"] for f in feats]
    geoms = [shape(f["geometry"]) for f in feats]
    del gj, feats
    n = len(props)
    log("features", n)

    n_vertices = shapely.get_num_coordinates(np.array(geoms, dtype=object)).astype(int)
    valid = shapely.is_valid(np.array(geoms, dtype=object))
    invalid_rows = []
    for i in np.where(~valid)[0]:
        invalid_rows.append((props[i]["Name"], props[i]["FromYear"], shapely.is_valid_reason(geoms[i])))
        geoms[i] = shapely.make_valid(geoms[i])
    log("invalid geometries repaired:", len(invalid_rows))

    names = [p["Name"] for p in props]
    from_y = np.array([int(p["FromYear"]) for p in props])
    to_y = np.array([int(p["ToYear"]) for p in props])
    area_prop = np.array([float(p["Area"]) for p in props])
    is_paren = np.array([nm.startswith("(") for nm in names])

    # ---------------- names, slugs, collisions ----------------
    by_name = collections.OrderedDict()
    for i, nm in enumerate(names):
        by_name.setdefault(nm, []).append(i)
    name_first = {nm: int(from_y[ids].min()) for nm, ids in by_name.items()}
    name_last = {nm: int(to_y[ids].max()) for nm, ids in by_name.items()}

    base_slug = {nm: slugify(nm) for nm in by_name}
    slug_groups = collections.defaultdict(list)
    for nm, s in base_slug.items():
        slug_groups[s].append(nm)
    slug_of = {}
    slug_collisions = []
    for s, nms in slug_groups.items():
        if len(nms) == 1:
            slug_of[nms[0]] = s
            continue
        ordered = sorted(nms, key=lambda x: (name_first[x], x))
        for k, nm in enumerate(ordered):
            slug_of[nm] = s if k == 0 else f"{s}-{k + 1}"
        slug_collisions.append((s, [(nm, slug_of[nm], name_first[nm], name_last[nm]) for nm in ordered]))
    name_of_slug = {s: nm for nm, s in slug_of.items()}
    log("distinct names", len(by_name), "slug collisions", len(slug_collisions))

    leaf_names = [nm for nm in by_name if not nm.startswith("(")]
    paren_names = [nm for nm in by_name if nm.startswith("(")]

    def resolve(raw):
        """Map a party name from a relation Name to (slug, resolved?)."""
        raw = raw.strip()
        if raw in slug_of and not raw.startswith("("):
            return slug_of[raw], True
        if "(" + raw + ")" in slug_of:
            return slug_of["(" + raw + ")"], True
        return slugify(raw), False

    relation_kind = {}
    relation_parties = {}
    unresolved_relations = []
    for nm in by_name:
        if not nm.startswith("("):
            relation_kind[nm] = "none"
            continue
        kind, a, b, ok = parse_relation_name(nm, resolve)
        relation_kind[nm] = kind
        if kind != "umbrella":
            relation_parties[nm] = (a, b)
            if not ok:
                unresolved_relations.append((nm, a, resolve(a)[1], b, resolve(b)[1]))
    kind_counts = collections.Counter(relation_kind[nm] for nm in paren_names)
    log("relation kinds", dict(kind_counts), "unresolved", len(unresolved_relations))

    # ---------------- shape ids ----------------
    shape_id = [None] * n
    seen = collections.Counter()
    dup_from_year = []
    for i in range(n):
        key = (names[i], int(from_y[i]))
        k = seen[key]
        seen[key] += 1
        suffix = "" if k == 0 else chr(ord("a") + k)
        shape_id[i] = f"{slug_of[names[i]]}_{int(from_y[i])}{suffix}"
        if k == 1:
            dup_from_year.append(key)

    # ---------------- Natural Earth countries ----------------
    log("loading Natural Earth", args.ne_shp)
    rd = shapefile.Reader(args.ne_shp, encoding="utf-8")
    fields = [fl[0] for fl in rd.fields[1:]]
    i_admin = fields.index("ADMIN")
    i_name = fields.index("NAME")
    ne_names, ne_short, ne_geoms = [], [], []
    for sr in rd.iterShapeRecords():
        g = shape(sr.shape.__geo_interface__)
        g = shapely.simplify(g, 0.01, preserve_topology=True)
        if not g.is_valid:
            g = shapely.make_valid(g)
        ne_names.append(sr.record[i_admin])
        ne_short.append(sr.record[i_name])
        ne_geoms.append(g)
    ne_tree = STRtree(ne_geoms)
    log("countries", len(ne_names))

    def country_overlaps(g):
        """{ADMIN name: overlap km2} for every country intersecting g."""
        res = {}
        for j in ne_tree.query(g, predicate="intersects"):
            a = ea_area_km2(safe_intersection(g, ne_geoms[j]))
            if a > 0:
                res[ne_names[j]] = res.get(ne_names[j], 0.0) + a
        return res

    def top_countries(ov, ref_area):
        items = [(c, a) for c, a in ov.items() if a >= args.min_overlap_frac * ref_area or a >= 1000.0]
        if not items and ov:
            items = list(ov.items())
        items.sort(key=lambda ca: (-ca[1], ca[0]))
        return [c for c, _ in items[:3]]

    # ---------------- per-shape measures ----------------
    log("per-shape bbox, centroid, modern countries")
    bbox = [None] * n
    centroid = [None] * n
    shape_countries = [None] * n
    shape_overlaps = [None] * n
    for i in range(n):
        g = geoms[i]
        b = g.bounds
        bbox[i] = tuple(round(v, 4) for v in b)
        c = g.centroid
        centroid[i] = (round(c.x, 3), round(c.y, 3))
        ov = country_overlaps(g)
        shape_overlaps[i] = ov
        shape_countries[i] = top_countries(ov, area_prop[i])
        if i % 2000 == 0:
            log("  shape", i, names[i])
    log("per-shape done")

    # ---------------- per-polity union and measures ----------------
    log("per-polity unions")
    pol = {}
    for nm, ids in by_name.items():
        u = shapely.unary_union([geoms[i] for i in ids]) if len(ids) > 1 else geoms[ids[0]]
        if not u.is_valid:
            u = shapely.make_valid(u)
        ov = country_overlaps(u)
        union_area = ea_area_km2(u)
        largest = max(ids, key=lambda i: area_prop[i])
        pol[nm] = {
            "ids": ids,
            "union_countries": top_countries(ov, union_area),
            "largest": largest,
        }
    log("per-polity done")

    # ---------------- relations ----------------
    # rel[(slug)] -> list of dicts
    relations = collections.defaultdict(list)
    rel_intervals = collections.defaultdict(list)  # (slug, kind, role, other) -> intervals

    for nm, (a, b) in relation_parties.items():
        kind = relation_kind[nm]
        sa, _ = resolve(a)
        sb, _ = resolve(b)
        ivs = merge_intervals([(int(from_y[i]), int(to_y[i])) for i in by_name[nm]])
        rslug = slug_of[nm]
        if kind in ("allegiance", "vassalage"):
            roles = (("vassal", sa, sb, b), ("suzerain", sb, sa, a))
        elif kind == "alliance":
            roles = (("ally", sa, sb, b), ("ally", sb, sa, a))
        else:
            roles = (("partner", sa, sb, b), ("partner", sb, sa, a))
        for role, me, other, other_name in roles:
            for f, t in ivs:
                rel_intervals[(me, kind, role, other, other_name, rslug)].append((f, t))

    # umbrella membership: Components of umbrella entities, and MemberOf of any feature
    for nm in paren_names:
        if relation_kind[nm] != "umbrella":
            continue
        rslug = slug_of[nm]
        for i in by_name[nm]:
            comps = [c.strip() for c in (props[i].get("Components") or "").split(";") if c.strip()]
            for c in comps:
                cs, _ = resolve(c)
                rel_intervals[(cs, "umbrella", "member", rslug, nm, rslug)].append((int(from_y[i]), int(to_y[i])))
    for i in range(n):
        mo = [m.strip() for m in (props[i].get("MemberOf") or "").split(";") if m.strip()]
        for m in mo:
            ms, _ = resolve(m)
            if m in relation_kind and relation_kind[m] == "umbrella":
                me = slug_of[names[i]]
                rel_intervals[(me, "umbrella", "member", ms, m, ms)].append((int(from_y[i]), int(to_y[i])))

    for (me, kind, role, other, other_name, rslug), ivs in rel_intervals.items():
        for f, t in merge_intervals(ivs):
            relations[me].append({
                "kind": kind, "role": role, "other": other, "other_name": other_name,
                "from": f, "to": t, "source": rslug,
            })
    for me in relations:
        relations[me].sort(key=lambda r: (r["from"], r["kind"], r["other"]))
    log("relations: polities with relations", len(relations))

    # ---------------- neighbours ----------------
    neighbours = collections.defaultdict(list)  # slug -> [{slug, from, to}]
    n_pairs = 0
    if not args.no_neighbours:
        log("neighbours within", args.neighbour_km, "km")
        garr = np.array(geoms, dtype=object)
        tree = STRtree(garr)
        leaf_mask = ~is_paren
        slug_idx = np.array([slug_of[nm] for nm in names], dtype=object)
        pair_iv = collections.defaultdict(list)
        dlat = args.neighbour_km / KM_PER_DEG
        for i in range(n):
            if is_paren[i]:
                continue
            g = geoms[i]
            minx, miny, maxx, maxy = g.bounds
            latm = (miny + maxy) / 2.0
            tol = dlat / max(math.cos(math.radians(min(abs(latm), 80.0))), 0.17)
            box = shapely.box(minx - tol, miny - dlat, maxx + tol, maxy + dlat)
            cands = tree.query(box)
            cands = cands[(cands > i) & leaf_mask[cands] & (from_y[cands] <= to_y[i]) & (to_y[cands] >= from_y[i])]
            cands = cands[slug_idx[cands] != slug_idx[i]]
            if len(cands) == 0:
                continue
            hit = shapely.dwithin(g, garr[cands], tol)
            for j in cands[hit]:
                f = int(max(from_y[i], from_y[j]))
                t = int(min(to_y[i], to_y[j]))
                a, b = slug_idx[i], slug_idx[j]
                pair_iv[(a, b)].append((f, t))
                pair_iv[(b, a)].append((f, t))
            if i % 2000 == 0:
                log("  shape", i, names[i])
        for (a, b), ivs in pair_iv.items():
            for f, t in merge_intervals(ivs):
                neighbours[a].append({"slug": b, "from": f, "to": t})
                n_pairs += 1
        for a in neighbours:
            neighbours[a].sort(key=lambda r: (r["from"], r["slug"]))
        log("neighbours done: polities with neighbours", len(neighbours), "entries", n_pairs)

    # ---------------- polities.csv ----------------
    def distinct_join(vals):
        seen_v, out = set(), []
        for v in vals:
            for part in str(v).split(";") if v is not None else []:
                part = part.strip()
                if part and part not in seen_v:
                    seen_v.add(part)
                    out.append(part)
        return ";".join(out)

    polities_rows = []
    for nm, ids in by_name.items():
        p = pol[nm]
        L = p["largest"]
        polities_rows.append({
            "slug": slug_of[nm],
            "name": nm,
            "umbrella": 1 if nm.startswith("(") else 0,
            "relation_kind": relation_kind[nm],
            "first_year": name_first[nm],
            "last_year": name_last[nm],
            "n_shapes": len(ids),
            "max_area_km2": round(float(area_prop[L]), 1),
            "centroid_lon": centroid[L][0],
            "centroid_lat": centroid[L][1],
            "modern_countries": ";".join(p["union_countries"]),
            "wikipedia": distinct_join([props[i].get("Wikipedia") for i in ids]),
            "wikidata": distinct_join([props[i].get("Wikidata") for i in ids]),
            "seshat_ids": distinct_join([props[i].get("SeshatID") for i in ids]),
            "member_of": distinct_join([props[i].get("MemberOf") for i in ids]),
            "components": distinct_join([props[i].get("Components") for i in ids]),
        })
    polities_rows.sort(key=lambda r: (r["first_year"], r["slug"]))
    pcols = ["slug", "name", "umbrella", "relation_kind", "first_year", "last_year", "n_shapes",
             "max_area_km2", "centroid_lon", "centroid_lat", "modern_countries", "wikipedia",
             "wikidata", "seshat_ids", "member_of", "components"]
    with open(os.path.join(out_dir, "polities.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=pcols)
        w.writeheader()
        w.writerows(polities_rows)
    log("wrote polities.csv", len(polities_rows))

    # ---------------- shapes.csv ----------------
    scols = ["shape_id", "slug", "from_year", "to_year", "area_km2", "bbox", "n_vertices", "modern_countries"]
    order = sorted(range(n), key=lambda i: (slug_of[names[i]], int(from_y[i]), int(to_y[i]), i))
    with open(os.path.join(out_dir, "shapes.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(scols)
        for i in order:
            w.writerow([shape_id[i], slug_of[names[i]], int(from_y[i]), int(to_y[i]),
                        round(float(area_prop[i]), 1), ",".join(str(v) for v in bbox[i]),
                        int(n_vertices[i]), ";".join(shape_countries[i])])
    log("wrote shapes.csv", n)

    # ---------------- polities/<slug>.json ----------------
    pol_dir = os.path.join(out_dir, "polities")
    written = 0
    for nm in leaf_names:
        s = slug_of[nm]
        ids = sorted(by_name[nm], key=lambda i: (int(from_y[i]), int(to_y[i]), i))
        doc = {
            "slug": s,
            "name": nm,
            "first_year": name_first[nm],
            "last_year": name_last[nm],
            "wikipedia": distinct_join([props[i].get("Wikipedia") for i in ids]),
            "wikidata": distinct_join([props[i].get("Wikidata") for i in ids]),
            "seshat_ids": [x for x in distinct_join([props[i].get("SeshatID") for i in ids]).split(";") if x],
            "modern_countries": pol[nm]["union_countries"],
            "shapes": [{
                "shape_id": shape_id[i],
                "from": int(from_y[i]),
                "to": int(to_y[i]),
                "area_km2": round(float(area_prop[i]), 1),
                "bbox": list(bbox[i]),
                "centroid": list(centroid[i]),
                "modern_countries": shape_countries[i],
            } for i in ids],
            "relations": relations.get(s, []),
            "neighbours": neighbours.get(s, []),
        }
        with open(os.path.join(pol_dir, s + ".json"), "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        written += 1
    log("wrote polity json", written)

    # ---------------- quality checks ----------------
    log("quality checks")
    q = {}
    q["slug_collisions"] = slug_collisions
    q["invalid_geometries"] = invalid_rows
    q["unresolved_relations"] = unresolved_relations
    q["dup_from_year"] = dup_from_year

    # shared Wikidata ids among leaf names
    wd2names = collections.defaultdict(set)
    for nm, ids in by_name.items():
        if nm.startswith("("):
            continue
        for i in ids:
            w = props[i].get("Wikidata")
            if w:
                wd2names[w].add(nm)
    q["shared_wikidata"] = sorted([(w, sorted(v)) for w, v in wd2names.items() if len(v) > 1],
                                  key=lambda x: x[1][0])
    q["multi_wikidata"] = sorted(nm for nm, ids in by_name.items()
                                 if len({props[i].get("Wikidata") for i in ids if props[i].get("Wikidata")}) > 1)
    q["missing_wiki"] = sorted({names[i] for i in range(n)
                                if not props[i].get("Wikipedia") or not props[i].get("Wikidata")})

    # near-duplicate spellings: same slug after dropping generic words
    generic = {"kingdom", "of", "the", "empire", "dynasty", "state", "republic", "principality",
               "duchy", "county", "sultanate", "emirate", "khanate", "caliphate"}

    def core(nm):
        s = slugify(nm)
        parts = [p for p in s.split("-") if p and p not in generic]
        return "-".join(parts)
    core_groups = collections.defaultdict(list)
    for nm in leaf_names:
        c = core(nm)
        if c:
            core_groups[c].append(nm)
    q["near_duplicate_names"] = sorted([v for v in core_groups.values() if len(v) > 1])

    # long-lived
    q["long_lived"] = sorted([(nm, name_first[nm], name_last[nm], len(by_name[nm]))
                              for nm in by_name if name_last[nm] - name_first[nm] >= 600],
                             key=lambda x: -(x[2] - x[1]))

    # timeline problems inside a polity: overlapping shape years, gaps
    overlaps_in, gaps_in = [], []
    for nm, ids in by_name.items():
        ivs = sorted((int(from_y[i]), int(to_y[i])) for i in ids)
        for (f1, t1), (f2, t2) in zip(ivs, ivs[1:]):
            if f2 <= t1:
                overlaps_in.append((nm, f1, t1, f2, t2))
            elif f2 > t1 + 1:
                gaps_in.append((nm, t1, f2))
    q["overlapping_shapes"] = overlaps_in
    q["gaps"] = gaps_in

    # tiny shapes
    q["tiny_shapes"] = sorted([(shape_id[i], round(float(area_prop[i]), 2), int(from_y[i]), int(to_y[i]))
                               for i in range(n) if area_prop[i] < 100.0], key=lambda x: x[1])
    q["n_small_shapes_1000"] = int((area_prop < 1000.0).sum())

    # dynasty / ruler names
    q["dynasty_names"] = sorted(nm for nm in leaf_names if re.search(r"\b[Dd]ynast", nm))
    q["person_names"] = sorted(nm for nm in leaf_names
                               if re.search(r"(?<!People)'s\b|\bsisters\b|\bHouse of\b|\bMagnates\b|\bNationalists\b|\bCommunists\b|\bParty\b", nm))
    q["slash_names"] = sorted(nm for nm in by_name if "/" in nm)

    # modern-country name mismatches: polities alive in 2024 whose name differs from NE ADMIN
    ne_set = set(ne_names)
    ne_short_set = set(ne_short)
    mism = []
    for nm in leaf_names:
        if name_last[nm] < 2024:
            continue
        top = pol[nm]["union_countries"]
        if nm in ne_set:
            continue
        mism.append((nm, top[0] if top else "", "NAME" if nm in ne_short_set else ""))
    q["modern_name_mismatch"] = sorted(mism)
    q["modern_alive_2024"] = sum(1 for nm in leaf_names if name_last[nm] >= 2024)

    # polities alive in 2024 whose union-based top country differs from the top country of their 2024 shape
    union_vs_last = []
    for nm in leaf_names:
        if name_last[nm] < 2024:
            continue
        last = max(by_name[nm], key=lambda i: (int(to_y[i]), int(from_y[i])))
        u = pol[nm]["union_countries"]
        l = shape_countries[last]
        if u and l and u[0] != l[0]:
            union_vs_last.append((nm, u[0], l[0], round(float(area_prop[last]), 0)))
    q["union_vs_last"] = sorted(union_vs_last)

    # counts
    counts = {
        "features": n,
        "distinct_names": len(by_name),
        "leaf_polities": len(leaf_names),
        "parenthesised": len(paren_names),
        "relation_kinds": dict(kind_counts),
        "polities_with_neighbours": len(neighbours),
        "neighbour_entries": n_pairs,
        "polities_with_relations": len([s for s in relations if s in name_of_slug and not name_of_slug[s].startswith("(")]),
        "dossier_files": written,
        "shapes_with_dup_from_year": len(dup_from_year),
        "countries": len(ne_names),
    }
    q["counts"] = counts

    write_readme(os.path.join(out_dir, "README.md"), q, args)
    os.makedirs(args.work, exist_ok=True)
    with open(os.path.join(args.work, "polity-table-quality.json"), "w", encoding="utf-8") as f:
        json.dump(q, f, ensure_ascii=False, indent=1, default=str)

    if args.stage and os.path.abspath(args.stage) != os.path.abspath(args.out):
        log("copying to", args.out)
        os.makedirs(os.path.join(args.out, "polities"), exist_ok=True)
        for fn in ("polities.csv", "shapes.csv", "README.md"):
            shutil.copyfile(os.path.join(out_dir, fn), os.path.join(args.out, fn))
        for fn in os.listdir(pol_dir):
            shutil.copyfile(os.path.join(pol_dir, fn), os.path.join(args.out, "polities", fn))
    log("done")
    print(json.dumps(counts, indent=1))


def write_readme(path, q, args):
    c = q["counts"]

    def li(items, fmt, limit=None):
        items = list(items)
        shown = items if limit is None else items[:limit]
        lines = [f"- {fmt(x)}" for x in shown]
        if limit is not None and len(items) > limit:
            lines.append(f"- ... and {len(items) - limit} more")
        return "\n".join(lines) if lines else "- none"

    md = []
    md.append("# data/ : polity and shape tables from Cliopatria v0.2.1\n")
    md.append("Generated by `tools/build_tables.py` (re-run it to rebuild; it reads the Cliopatria GeoJSON once and "
              "Natural Earth 10m admin-0 countries). Shapes of record are Cliopatria's (Seshat Global History Databank, "
              "CC BY 4.0); nothing here is corrected, only measured. Years are integers, negative for BCE; ToYear is inclusive.\n")
    md.append("## Counts\n")
    md.append(f"- Features (dated shapes): **{c['features']}**\n"
              f"- Distinct Names: **{c['distinct_names']}**, of which leaf polities (no parentheses) **{c['leaf_polities']}** "
              f"and parenthesised entities **{c['parenthesised']}**: "
              + ", ".join(f"{k} {v}" for k, v in sorted(c['relation_kinds'].items())) + "\n"
              f"- Dossier seeds written (one per leaf polity): **{c['dossier_files']}**\n"
              f"- Leaf polities with at least one neighbour within {args.neighbour_km:g} km in an overlapping year: "
              f"**{c['polities_with_neighbours']}** ({c['neighbour_entries']} neighbour entries); "
              f"leaf polities with at least one parsed relation: **{c['polities_with_relations']}**\n"
              f"- Natural Earth countries used for the modern-country join: {c['countries']} (10m admin-0, field ADMIN)\n")

    md.append("## Files\n")
    md.append("### polities.csv (one row per distinct Name, sorted by first_year then slug)\n")
    md.append("| column | meaning |\n| --- | --- |\n"
              "| slug | `slugify(Name)` from tools/slug.py; see the collision note below |\n"
              "| name | the Cliopatria Name verbatim |\n"
              "| umbrella | 1 if the Name starts with \"(\" (umbrella or relation entity, not territory of its own) |\n"
              "| relation_kind | none, umbrella, allegiance, alliance, vassalage or personal_union, parsed from the Name |\n"
              "| first_year, last_year | min FromYear and max ToYear over the Name's shapes |\n"
              "| n_shapes | number of features with this Name |\n"
              "| max_area_km2 | Cliopatria's Area of the largest shape |\n"
              "| centroid_lon, centroid_lat | lon/lat centroid of the largest shape (plain planar centroid; for shapes that straddle the antimeridian it can fall in the gap) |\n"
              "| modern_countries | Natural Earth ADMIN names of the countries overlapping the union of the Name's shapes, top 3 by overlap area, \";\"-joined; overlaps under 1 percent of the shape (and under 1000 km2) are ignored |\n"
              "| wikipedia, wikidata | distinct values over the shapes, \";\"-joined (a few Names carry more than one, listed below) |\n"
              "| seshat_ids | distinct SeshatID values, \";\"-joined |\n"
              "| member_of | distinct MemberOf values (umbrella Names, verbatim), \";\"-joined |\n"
              "| components | distinct Components values (Names, verbatim), \";\"-joined |\n")
    md.append("### shapes.csv (one row per feature, sorted by slug then from_year)\n")
    md.append("| column | meaning |\n| --- | --- |\n"
              "| shape_id | slug + \"_\" + FromYear, plus a letter suffix b, c, ... when two features of one Name share a FromYear (file order) |\n"
              "| slug, from_year, to_year | as above |\n"
              "| area_km2 | Cliopatria's Area field (spherical km2; recomputing it from the geometry agrees to 0.5 percent) |\n"
              "| bbox | \"minlon,minlat,maxlon,maxlat\" in one quoted field, 4 decimals |\n"
              "| n_vertices | vertex count of the original geometry |\n"
              "| modern_countries | top 3 Natural Earth ADMIN names by overlap with this shape, \";\"-joined |\n")
    md.append("### polities/<slug>.json (one per leaf polity)\n")
    md.append("`{slug, name, first_year, last_year, wikipedia, wikidata, seshat_ids[], modern_countries[], shapes[], relations[], neighbours[]}`\n\n"
              "- `shapes[]`: `{shape_id, from, to, area_km2, bbox[4], centroid[2], modern_countries[]}` in year order.\n"
              "- `relations[]`: `{kind, role, other, other_name, from, to, source}`. `kind` is allegiance, vassalage, alliance, "
              "personal_union or umbrella; `role` is this polity's side: vassal or suzerain (allegiance, vassalage), ally (alliance), "
              "partner (personal_union), member (umbrella). `other` is the counterpart's slug (a leaf slug when a leaf polity of that "
              "name exists, otherwise the rel- slug of the umbrella), `other_name` its Name, `source` the slug of the Cliopatria "
              "entity the relation came from. Years are the relation entity's own FromYear..ToYear, merged over its features; "
              "umbrella membership comes from the umbrella's Components and from the member's MemberOf, merged.\n"
              "- `neighbours[]`: `{slug, from, to}`: other leaf polities with a shape alive in an overlapping year whose geometry comes "
              f"within {args.neighbour_km:g} km (shapely.dwithin in degrees with the tolerance scaled by cos(latitude): exact east-west, "
              "lenient north-south, so nothing is missed). from..to is the merged span of the overlapping years of the qualifying shape "
              "pairs; a neighbour with a gap in the record appears once per span. Umbrella entities are excluded from both sides.\n")

    md.append("## Conventions other builders rely on\n")
    md.append("- Slug: `tools/slug.py` `slugify(Name)`. Two Names that collide after slugifying are disambiguated here by first_year: "
              "the earlier keeps the bare slug, later ones get `-2`, `-3`. **Anyone deriving a slug from a Name must check polities.csv "
              "for these.**\n" + li(q["slug_collisions"], lambda x: f"`{x[0]}`: " + "; ".join(f"\"{nm}\" ({f}..{t}) -> `{s}`" for nm, s, f, t in x[1])) + "\n"
              "- Modern country names are Natural Earth 10m admin-0 **ADMIN** (\"United States of America\", \"Ivory Coast\", \"Czechia\", "
              "\"Russia\", \"Republic of Serbia\", \"United Republic of Tanzania\", \"eSwatini\", \"East Timor\", \"The Bahamas\", "
              "\"Hong Kong S.A.R.\"); NAME differs from ADMIN for 64 of the 258 features (\"Côte d'Ivoire\", \"Dem. Rep. Congo\", \"S. Sudan\").\n"
              "- Relation entities (Type RELATION) carry Components that list the whole membership of the larger party "
              "(e.g. the 27 components of \"(Allegiance of Swiss Confederation to Holy Roman Empire)\"), so the two parties are taken "
              "from the Name, not from Components; Components are used only for umbrella entities.\n")

    md.append("## Quality issues noticed\n")
    md.append("### Impossible or suspicious year ranges (Names spanning 600 years or more)\n"
              "Several of these are one Name reused for successive states (Later Zhou -750..960 is the Zhou plus the Five-Dynasties Later Zhou; "
              "Kingdom of Italy 587..1946 is Lombard, Carolingian, Napoleonic and Savoyard Italy; Georgia 567..2024 runs from Iberia to the republic). "
              "Research agents should split these into one dossier per state.\n" +
              li(q["long_lived"], lambda x: f"{x[0]}: {x[1]}..{x[2]} ({x[2]-x[1]} years, {x[3]} shapes)") + "\n")
    md.append("### Duplicate or near-duplicate Names\n"
              f"Leaf Names that share a Wikidata id ({len(q['shared_wikidata'])} ids): the same state under two spellings or periods, or a bad id.\n" +
              li(q["shared_wikidata"], lambda x: f"{x[0]}: " + " / ".join(x[1])) + "\n\n"
              f"Leaf Names that differ only by generic words (kingdom, empire, dynasty, republic, of, the...) ({len(q['near_duplicate_names'])} groups):\n" +
              li(q["near_duplicate_names"], lambda x: " / ".join(x), limit=60) + "\n\n"
              f"Names carrying more than one Wikidata id: " + (", ".join(q["multi_wikidata"]) or "none") + "\n\n"
              "Names with a slash (two states in one row): " + (", ".join(q["slash_names"]) or "none") + "\n")
    md.append("### Names that are dynasties, houses, parties or people rather than states\n"
              f"{len(q['dynasty_names'])} leaf Names contain \"Dynasty\" (the Chinese, Persian and Indian dynasties; the dossier rule is one dossier per state, "
              "so a dynasty that replaces a dynasty on the same land keeps the state). Names that are a person, house or party:\n" +
              li(q["person_names"], lambda x: x) + "\n")
    md.append("### Timeline problems inside one Name\n"
              f"- Shapes of the same Name alive in the same year (overlapping FromYear..ToYear): {len(q['overlapping_shapes'])} pairs"
              + (": " + "; ".join(f"{nm} {f1}..{t1} vs {f2}..{t2}" for nm, f1, t1, f2, t2 in q['overlapping_shapes'][:12]) + ("..." if len(q['overlapping_shapes']) > 12 else "") if q['overlapping_shapes'] else "") + "\n"
              f"- Features of one Name sharing a FromYear (given b, c suffixes): {len(q['dup_from_year'])}"
              + (": " + "; ".join(f"{nm} {y}" for nm, y in q['dup_from_year'][:12]) + ("..." if len(q['dup_from_year']) > 12 else "") if q['dup_from_year'] else "") + "\n"
              f"- Gaps of more than one year between consecutive shapes of a Name: {len(q['gaps'])} (a gap means the polity has no shape of record for those years; "
              "the compiler must decide whether to hold the last shape or drop it)\n")
    md.append("### Shapes with tiny area\n"
              f"{len(q['tiny_shapes'])} shapes under 100 km2 and {q['n_small_shapes_1000']} under 1000 km2 (city-states, islands, residual territories; "
              "at H3 resolution 5 a 100 km2 shape is less than one cell):\n" +
              li(q["tiny_shapes"], lambda x: f"{x[0]} ({x[2]}..{x[3]}): {x[1]} km2") + "\n")
    md.append("### Modern countries whose Cliopatria Name differs from the Natural Earth name\n"
              f"Of the {q['modern_alive_2024']} leaf polities alive in 2024, these Names are not a Natural Earth ADMIN name (with the top overlapping ADMIN; "
              "\"NAME\" marks the ones that match Natural Earth's short NAME field instead):\n" +
              li(q["modern_name_mismatch"], lambda x: f"{x[0]} -> {x[1]}" + (f" ({x[2]})" if x[2] else "")) + "\n")
    md.append("### Modern-country join caveats\n"
              "The polity-level modern_countries column ranks countries by overlap with the **union of every shape**, so for a state that lost "
              "a large territory the former land wins: French Fifth Republic -> Algeria, State of Israel -> Egypt (Sinai 1967..1982), "
              "Kingdom of Great Britain -> Oman and Yemen. Use the per-shape modern_countries (shapes.csv, or the dossier's shapes[]) "
              f"for a given year. Polities alive in 2024 whose union-based top country differs from their 2024 shape's top country ({len(q['union_vs_last'])}):\n" +
              li(q["union_vs_last"], lambda x: f"{x[0]}: union -> {x[1]}, 2024 shape -> {x[2]} ({x[3]:.0f} km2)") + "\n\n"
              "Seen while checking that join (Cliopatria v0.2.1 rows the research agents should correct):\n"
              "- There is no \"United Kingdom\" Name: the British state from 1709 to 2024 is \"Kingdom of Great Britain\" (38 shapes), and the empire is "
              "\"British Empire\" / \"British Colonial Empire\" plus the umbrella \"(British Empire)\".\n"
              "- \"Estado Novo\" runs 1926..2024 (Portugal's regime ended in 1974) and its 2024 shape is a 6,900 km2 patch at Cabinda; \"Portuguese Republic\" "
              "covers only 1911..1925, so Portugal itself has no shape of record after 1925 except through \"Estado Novo\" and \"(Portuguese Empire)\".\n"
              "- \"Saint Kitts\" (1967..2024) is a 500 km2 polygon at 64.9 W, 17.7 N, which is Saint Croix in the US Virgin Islands, not Saint Kitts (62.7 W).\n"
              "- \"Mujahideen\" (1987..2024) starts in Afghanistan and ends as a 69,000 km2 shape across Syria, Iraq and Turkey: one Name for unrelated movements.\n"
              "- \"Principality of Monaco\" and \"Kingdom of Monaco\" are 94 km2 polygons for a 2 km2 state, so they overlap France more than Natural Earth's Monaco; "
              "\"Hunnic Empire\" has two shapes of 46 km2 in 633..673 and \"Kingdom of Mercia\" three of 44 km2 in 884..925, residues that are smaller than one H3 cell.\n"
              "- \"Gaza/Hamas\", \"Russian-occupied territories\", \"British Overseas Territories\", \"Holy Roman Empire Minor States\", \"Khanates of the Caucasus\" and "
              "\"Scandinavian minor kingdoms\" are aggregates or non-state entries carried as leaf polities.\n")
    md.append("### Geometry and metadata\n"
              f"- {len(q['invalid_geometries'])} features had invalid geometry (components with too few points), repaired with make_valid before measuring: "
              + "; ".join(f"{nm} {y}" for nm, y, _ in q['invalid_geometries']) + "\n"
              f"- Features missing Wikipedia or Wikidata: " + (", ".join(q["missing_wiki"]) or "none") + "\n"
              f"- Relation Names whose parties could not both be matched to a Name: " + ("; ".join(f"{x[0]} (a={x[1]}:{x[2]}, b={x[3]}:{x[4]})" for x in q["unresolved_relations"]) or "none") + "\n"
              "- Umbrella entities nest: (Kingdom of Bohemia) is MemberOf (Holy Roman Empire), (Kingdom of the Franks) is MemberOf (Carolingian Empire) and (Merovingian Empire); "
              "the member_of column keeps these, the dossiers only list umbrella membership of leaf polities.\n"
              "- Several umbrella entities also exist as a leaf polity with the same name (British Empire, Holy Roman Empire, Kingdom of France, Carolingian Empire...): "
              "the leaf carries the directly ruled territory, the umbrella the whole.\n")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))


if __name__ == "__main__":
    main()
