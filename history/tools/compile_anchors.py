#!/usr/bin/env python3
"""Compile Cliopatria onto the land grid at every anchor year.

    python3 -I compile_anchors.py            every anchor year
    python3 -I compile_anchors.py 1600 2024  only those years (reports are still rewritten
                                             from every anchor file present)

Anchor years: every 100 years from -6000 to 1600, every 10 from 1610 to 2020, and 2024.

Writes, under history/data/anchors/:
    <stem>.json       {"year", "owners": {slug: runs}, "polities", "cells_owned", "conflicts", ...}
                      stem is m<abs year, 4 digits> for BCE and p<year, 4 digits> for CE
                      (m3400 = 3400 BCE, p0800 = 800 CE); runs are indices into
                      data/grid/land_r5.txt, "start-end" inclusive or a single int
    _conflicts.csv    year, slug_a (winner: smaller Cliopatria Area), slug_b (loser), cells
    _report.csv       year, polities, cells_owned, conflict_cells, conflict_pairs, seconds
    _areas.csv        year, slug, cells, cells_claimed, cells_all, cell_km2, clio_km2, ratio, ratio_claimed

Ownership rule: every non-umbrella Cliopatria shape alive in the year (FromYear <= year
<= ToYear) claims its land cells; where two polities claim one cell the one with the
smaller Cliopatria Area wins. "conflicts" in the anchor file is the number of land cells
with more than one claimant.
"""
import csv
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import grid  # noqa: E402

ANCHOR_DIR = grid.ANCHOR_DIR


def _write_json(path, obj):
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, separators=(",", ":"))
    os.replace(tmp, path)


def compile_year(year, feats, land_sorted, land_order, n_land):
    """Return (anchor dict, conflict pair rows, area rows, seconds)."""
    t0 = time.time()
    alive = [ft for ft in feats if not ft["umbrella"] and ft["from"] <= year <= ft["to"]]
    groups = defaultdict(lambda: {"area": 0.0, "feats": [], "name": None})
    for ft in alive:
        g = groups[ft["slug"]]
        g["area"] += ft["area"]
        g["feats"].append(ft)
        g["name"] = ft["name"]
    slugs = sorted(groups, key=lambda s: (groups[s]["area"], s))  # smaller Area wins
    slug_id = {s: i for i, s in enumerate(slugs)}

    owner = np.full(n_land, -1, dtype=np.int32)
    nclaims = np.zeros(n_land, dtype=np.int16)
    pair_conflicts = Counter()
    claimed = {}
    cells_all = {}
    for s in slugs:
        parts = [grid.feature_cells_int(ft) for ft in groups[s]["feats"]]
        arr = np.unique(np.concatenate(parts)) if len(parts) > 1 else parts[0]
        cells_all[s] = int(arr.size)
        pos = np.searchsorted(land_sorted, arr)
        pos[pos >= n_land] = 0
        hit = land_sorted[pos] == arr
        idx = land_order[pos[hit]]
        claimed[s] = int(idx.size)
        if idx.size == 0:
            continue
        cur = owner[idx]
        free = cur == -1
        owner[idx[free]] = slug_id[s]
        nclaims[idx] += 1
        taken = cur[~free]
        if taken.size:
            vals, counts = np.unique(taken, return_counts=True)
            for w, c in zip(vals, counts):
                pair_conflicts[(slugs[int(w)], s)] += int(c)

    owners = {}
    owned = {}
    if slugs:
        order = np.argsort(owner, kind="stable")
        sorted_owner = owner[order]
        start = np.searchsorted(sorted_owner, 0)
        ids = sorted_owner[start:]
        idxs = order[start:]
        if ids.size:
            bounds = np.flatnonzero(np.diff(ids)) + 1
            for chunk_ids, chunk_idx in zip(np.split(ids, bounds), np.split(idxs, bounds)):
                s = slugs[int(chunk_ids[0])]
                owned[s] = int(chunk_idx.size)
                owners[s] = grid.to_runs(chunk_idx)
    cells_owned = int((owner >= 0).sum())
    conflict_cells = int((nclaims > 1).sum())
    seconds = time.time() - t0

    anchor = {
        "year": year,
        "grid": "land_r5.txt",
        "land_cells": n_land,
        "owners": owners,
        "polities": len(slugs),
        "cells_owned": cells_owned,
        "conflicts": conflict_cells,
        "conflict_pairs": len(pair_conflicts),
    }
    conflict_rows = [(year, a, b, c) for (a, b), c in sorted(pair_conflicts.items(), key=lambda kv: -kv[1])]
    area_rows = []
    for s in slugs:
        clio = groups[s]["area"]
        own = owned.get(s, 0)
        area_rows.append({
            "year": year, "slug": s, "cells": own, "cells_claimed": claimed[s], "cells_all": cells_all[s],
            "cell_km2": round(own * grid.CELL_KM2, 1), "clio_km2": round(clio, 1),
            "ratio": round(own * grid.CELL_KM2 / clio, 4) if clio else "",
            "ratio_claimed": round(claimed[s] * grid.CELL_KM2 / clio, 4) if clio else "",
        })
    report = {"year": year, "polities": len(slugs), "cells_owned": cells_owned,
              "conflict_cells": conflict_cells, "conflict_pairs": len(pair_conflicts), "seconds": round(seconds, 2)}
    return anchor, conflict_rows, area_rows, report


def main(argv):
    years = [int(a) for a in argv[1:]] if len(argv) > 1 else list(grid.ANCHOR_YEARS)
    t_all = time.time()
    land = grid.land_cells()
    n_land = len(land)
    land_sorted, land_order = grid.land_cells_int()
    feats = grid.load_features()
    ANCHOR_DIR.mkdir(parents=True, exist_ok=True)
    work = grid.WORK / "anchor_side"
    work.mkdir(parents=True, exist_ok=True)
    for year in years:
        anchor, conflict_rows, area_rows, report = compile_year(year, feats, land_sorted, land_order, n_land)
        _write_json(ANCHOR_DIR / (grid.anchor_name(year) + ".json"), anchor)
        # side tables kept off the mount until the final merge
        with open(work / (grid.anchor_name(year) + ".json"), "w") as f:
            json.dump({"report": report, "conflicts": conflict_rows, "areas": area_rows}, f)
        print("%6d: %4d polities, %6d cells owned, %5d conflict cells, %4d pairs, %.1f s" % (
            year, report["polities"], report["cells_owned"], report["conflict_cells"],
            report["conflict_pairs"], report["seconds"]), file=sys.stderr)
    write_reports(work)
    print("total %.1f s" % (time.time() - t_all), file=sys.stderr)


def write_reports(work):
    """Merge the per-year side tables (every one present) into the three CSVs on the mount."""
    reports, conflicts, areas = [], [], []
    for p in sorted(work.glob("*.json"), key=lambda p: grid.anchor_year(p.stem)):
        with open(p) as f:
            d = json.load(f)
        reports.append(d["report"])
        conflicts.extend(d["conflicts"])
        areas.extend(d["areas"])
    with open(ANCHOR_DIR / "_report.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "polities", "cells_owned", "conflict_cells", "conflict_pairs", "seconds"])
        w.writeheader()
        w.writerows(reports)
    with open(ANCHOR_DIR / "_conflicts.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "slug_a", "slug_b", "cells"])
        w.writerows(conflicts)
    with open(ANCHOR_DIR / "_areas.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "slug", "cells", "cells_claimed", "cells_all", "cell_km2",
                                          "clio_km2", "ratio", "ratio_claimed"])
        w.writeheader()
        w.writerows(areas)


if __name__ == "__main__":
    main(sys.argv)
