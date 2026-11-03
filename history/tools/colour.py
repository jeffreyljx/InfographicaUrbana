#!/usr/bin/env python3
"""EmpireMap colour tools: sRGB <-> OKLab/OKLCH maths, the colour registry (history/colours.json),
graph colouring of the polities without a fixed colour, and the neighbour check.

Edited 2026-11-01 by the colour agent: `check --relations` skips, per year, the pairs the snapshots' `status` key
puts in a vassal or constituent relation (one side the other's vassal or constituent, or both of one suzerain:
the map draws that land in the suzerain's tint); `check --drawn` also skips pairs where one side is drawn wholly in
a suzerain's tint that year. Both read the `status` key of each {year, owners} file; nothing else changed.

    python3 -I tools/colour.py <command> [options]

Commands
  seed       write rules, families, wheel and the fixed colours from tools/colour_seed.py into colours.json
             (refuses to overwrite an existing registry without --force; keeps "assigned" and "log")
  assign     colour every polity without a fixed colour by greedy graph colouring over the union of every
             anchor year's adjacency; writes colours.json "assigned"  [--no-seed-neighbours] [--dry] [--min D] [--anchors DIR]
  check      report every neighbouring pair in any anchor year closer than the minimum, with a suggestion
             [--min D] [--year Y] [--ring K] [--all] [--json FILE] [--anchors DIR] [--relations] [--drawn]
  set        change one polity's colour through the registry: set SLUG HEX --note "why" [--force]
  show       print a polity's colour, OKLCH, family, group and tints: show SLUG [SLUG...]
  swatch     write an HTML swatch sheet (default /tmp/claude-0/work/colours/swatch.html)
  distance A B | blend A B | tint HEX KIND | oklch HEX | hex L C H     colour maths on the command line

Library (import colour): distance(hex_a, hex_b), blend(hex_a, hex_b, t=0.5), tint(hex, kind), hex_to_oklab,
oklab_to_hex, hex_to_oklch, oklch_to_hex, contested(hex_a, hex_b), load_registry(), colour_of(slug).

The maths needs no external package. assign and check need h3 (installed) and use numpy when present.
Adjacency: two polities are neighbours in an anchor year when they own land cells that share an H3 edge
(h3.grid_ring(cell, 1) over each polity's cells; the ring table is cached once per land grid).
Caches live under /tmp/claude-0/work/colours/.
--anchors DIR points assign and check at another directory of {year, owners, land_cells} files on the same
grid (the compiled windows, once they exist) instead of data/anchors/.
"""
import csv
import datetime as _dt
import hashlib as _hashlib
import json
import math
import os
import sys
from array import array
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
HISTORY = HERE.parent
REGISTRY = HISTORY / "colours.json"
DATA = HISTORY / "data"
POLITIES_CSV = DATA / "polities.csv"
LAND_FILE = DATA / "grid" / "land_r5.txt"
ANCHOR_DIR = DATA / "anchors"
SEED_DIR = DATA / "polities"
WORK = Path("/tmp/claude-0/work/colours")

# ---------------------------------------------------------------------------------------------
# Colour maths: sRGB (hex) <-> linear RGB <-> OKLab <-> OKLCH (Björn Ottosson, 2020)
# ---------------------------------------------------------------------------------------------

def _cbrt(x):
    return math.copysign(abs(x) ** (1.0 / 3.0), x)


def _srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _linear_to_srgb(c):
    c = min(1.0, max(0.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_to_rgb(h):
    """'#rrggbb' or 'rgb' -> (r, g, b) floats in 0..1."""
    s = h.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6:
        raise ValueError("not a hex colour: %r" % h)
    return tuple(int(s[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return "#%02x%02x%02x" % tuple(int(round(min(1.0, max(0.0, c)) * 255)) for c in (r, g, b))


def linear_to_oklab(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = _cbrt(l), _cbrt(m), _cbrt(s)
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)


def oklab_to_linear(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def hex_to_oklab(h):
    r, g, b = (_srgb_to_linear(c) for c in hex_to_rgb(h))
    return linear_to_oklab(r, g, b)


def in_gamut(L, a, b, eps=0.0005):
    return all(-eps <= c <= 1 + eps for c in oklab_to_linear(L, a, b))


def oklab_to_hex(L, a, b, clip=True):
    """OKLab -> hex. With clip (default) an out-of-gamut colour keeps its lightness and hue and loses chroma
    until it fits sRGB (bisection); lightness is clamped to 0..1."""
    L = min(1.0, max(0.0, L))
    if clip and not in_gamut(L, a, b):
        lo, hi = 0.0, 1.0
        for _ in range(30):
            mid = (lo + hi) / 2
            if in_gamut(L, a * mid, b * mid):
                lo = mid
            else:
                hi = mid
        a, b = a * lo, b * lo
    r, g, bl = (_linear_to_srgb(c) for c in oklab_to_linear(L, a, b))
    return rgb_to_hex(r, g, bl)


def oklab_to_oklch(L, a, b):
    C = math.hypot(a, b)
    h = math.degrees(math.atan2(b, a)) % 360 if C > 1e-9 else 0.0
    return L, C, h


def oklch_to_oklab(L, C, h):
    return L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h))


def hex_to_oklch(h):
    return oklab_to_oklch(*hex_to_oklab(h))


def oklch_to_hex(L, C, h, clip=True):
    return oklab_to_hex(*oklch_to_oklab(L, C, h), clip=clip)


def max_chroma(L, h):
    """The largest chroma that stays in the sRGB gamut at this lightness and hue."""
    lo, hi = 0.0, 0.5
    for _ in range(30):
        mid = (lo + hi) / 2
        if in_gamut(*oklch_to_oklab(L, mid, h)):
            lo = mid
        else:
            hi = mid
    return lo


def distance(hex_a, hex_b):
    """Euclidean distance in OKLab (delta E OK)."""
    A, B = hex_to_oklab(hex_a), hex_to_oklab(hex_b)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(A, B)))


def blend(hex_a, hex_b, t=0.5):
    """The OKLab interpolation of two colours; t=0.5 is the midpoint used for contested land."""
    A, B = hex_to_oklab(hex_a), hex_to_oklab(hex_b)
    return oklab_to_hex(*[x + (y - x) * t for x, y in zip(A, B)])


DEFAULT_TINTS = {
    "vassal": {"chroma_factor": 0.55, "lightness_add": 0.12},
    "culture": {"chroma_factor": 0.40, "lightness_add": 0.15},
    "label": {"chroma_factor": 0.90, "lightness_add": -0.30, "lightness_min": 0.22},
    "outline": {"chroma_factor": 1.30, "lightness_add": -0.12},
    "hatch": {"chroma_factor": 1.00, "lightness_add": -0.18},
}


def tint(hex_colour, kind, rules=None):
    """The status tint of a colour: vassal (protectorate, tributary, client), culture, label, outline, hatch.
    Factors come from colours.json "rules" when given, else DEFAULT_TINTS."""
    kind = {"protectorate": "vassal", "tributary": "vassal", "client": "vassal"}.get(kind, kind)
    spec = None
    if rules:
        spec = (rules.get(kind) or {}).get("tint") or rules.get(kind)
    if not spec or "chroma_factor" not in spec:
        spec = DEFAULT_TINTS.get(kind)
    if spec is None:
        raise ValueError("unknown tint kind %r (vassal, culture, label, outline, hatch)" % kind)
    L, C, h = hex_to_oklch(hex_colour)
    L = L + spec.get("lightness_add", 0.0)
    L = max(spec.get("lightness_min", 0.0), min(spec.get("lightness_max", 0.94), L))
    return oklch_to_hex(L, C * spec.get("chroma_factor", 1.0), h)


def contested(hex_a, hex_b, rules=None):
    """Fill and hatch colour for land two states are fighting over: the OKLab midpoint plus a darker hatch."""
    fill = blend(hex_a, hex_b, 0.5)
    return {"fill": fill, "hatch": tint(fill, "hatch", rules)}


# ---------------------------------------------------------------------------------------------
# Registry I/O
# ---------------------------------------------------------------------------------------------

def load_registry(path=REGISTRY):
    with open(path) as f:
        return json.load(f)


def _dump_entries(f, entries, indent="  "):
    """One JSON object per line, so diffs stay readable."""
    for i, e in enumerate(entries):
        f.write(indent + json.dumps(e, ensure_ascii=False, separators=(", ", ": ")))
        f.write(",\n" if i < len(entries) - 1 else "\n")


def save_registry(reg, path=REGISTRY):
    """Write the registry: the small sections pretty-printed, "fixed" and "assigned" one entry per line.
    Atomic (temp file + replace)."""
    tmp = Path(str(path) + ".tmp")
    with open(tmp, "w") as f:
        f.write("{\n")
        keys = [k for k in ("version", "written", "owner", "tool", "rules", "families", "wheel") if k in reg]
        for k in keys:
            f.write(json.dumps(k) + ": " + json.dumps(reg[k], ensure_ascii=False, indent=1).replace("\n", "\n ") + ",\n")
        f.write('"fixed": [\n')
        _dump_entries(f, reg.get("fixed", []))
        f.write("],\n")
        f.write('"assigned_meta": ' + json.dumps(reg.get("assigned_meta", {}), ensure_ascii=False, indent=1).replace("\n", "\n ") + ",\n")
        f.write('"assigned": {\n')
        items = sorted(reg.get("assigned", {}).items())
        for i, (slug, e) in enumerate(items):
            f.write("  " + json.dumps(slug) + ": " + json.dumps(e, ensure_ascii=False, separators=(", ", ": ")))
            f.write(",\n" if i < len(items) - 1 else "\n")
        f.write("},\n")
        f.write('"log": [\n')
        _dump_entries(f, reg.get("log", []))
        f.write("]\n}\n")
    os.replace(tmp, path)


def colour_map(reg):
    """slug -> hex over fixed and assigned."""
    out = {e["slug"]: e["hex"] for e in reg.get("fixed", [])}
    for slug, e in reg.get("assigned", {}).items():
        out.setdefault(slug, e["hex"])
    return out


def group_map(reg):
    return {e["slug"]: e["group"] for e in reg.get("fixed", []) if e.get("group")}


def colour_of(slug, reg=None):
    reg = reg or load_registry()
    return colour_map(reg).get(slug)


def read_polities():
    """polities.csv -> {slug: row} for the leaf polities (umbrella == 0)."""
    out = {}
    with open(POLITIES_CSV, newline="") as f:
        for r in csv.DictReader(f):
            if r.get("umbrella", "0") == "0":
                out[r["slug"]] = r
    return out


def _today():
    return _dt.date.today().isoformat()


# ---------------------------------------------------------------------------------------------
# seed
# ---------------------------------------------------------------------------------------------

def build_wheel(spec):
    """The 24-hue wheel with its lightness variants; chroma is clipped to the sRGB gamut per hue."""
    colours = []
    for variant, v in spec["variants"].items():
        for hue in spec["hues"]:
            C = min(v["C"], max_chroma(v["L"], hue))
            hexc = oklch_to_hex(v["L"], C, hue)
            colours.append({"id": "h%03d-%s" % (hue, variant), "hue": hue, "variant": variant,
                            "hex": hexc, "oklch": [round(v["L"], 3), round(C, 3), hue]})
    return colours


def make_rules(minimum, why, neutral_hex):
    return {
        "space": "OKLab (Björn Ottosson 2020); hex values are 8-bit sRGB; distance() is Euclidean in OKLab (delta E OK)",
        "oklab_min_distance": minimum,
        "why": why,
        "neighbour": "two polities are neighbours in a year when they own land cells that share an H3 edge (grid_ring(cell, 1)); the check runs over every anchor year, and later over every compiled year; a clash is resolved by recolouring the smaller state everywhere, so the colour-for-life rule holds",
        "lifetime": "one colour per polity for its whole life; a dynasty change within a state keeps the colour; a successor that claims continuity takes a neighbouring hue of the same family; an unrelated successor takes an unrelated one; rows of one Cliopatria state (fixed entries sharing a group) share the colour",
        "readability": "every fixed and wheel colour keeps OKLab L between 0.40 and 0.86 and chroma at least 0.03 (0.06 for hues), so each fill reads on the pale basemap (L about 0.95) and none is mistaken for the neutral grey",
        "vassal": {"applies_to": ["vassal", "protectorate", "tributary", "client state"],
                   "tint": {"chroma_factor": 0.55, "lightness_add": 0.12, "lightness_max": 0.94},
                   "outline": "the vassal's own colour (the suzerain's full colour) at 1 px", "label": "its own label",
                   "note": "tint(hex, 'vassal'): OKLCH chroma x0.55, lightness +0.12; a vassal tint sits 0.12 to 0.14 from its suzerain's colour"},
        "occupied": {"fill": "the owner's colour", "hatch": {"colour": "the occupier's colour", "angle_deg": 45, "spacing_px": 7, "width_px": 2.5},
                     "note": "occupied land is the occupier's colour hatched over the owner's; it becomes the occupier's only if annexed"},
        "contested": {"fill": "blend(a, b): the OKLab midpoint of the two claimants (blue and red give purple)",
                      "hatch": {"colour": "tint(fill, 'hatch'): the fill darkened by 0.18 L", "angle_deg": -45, "spacing_px": 4, "width_px": 1},
                      "note": "a fine diagonal hatch so the blend also reads for colour-blind viewers; the zone merges into the winner's full colour when the contest ends"},
        "rebel": {"fill": "the rebel state's own colour at the vassal tint", "hatch": {"colour": "the rebel state's own colour", "angle_deg": 45, "spacing_px": 5, "width_px": 1.5},
                  "note": "rebel-held land is hatched in the rebels' own colour until they win (a new state keeps the rebel colour; a restoration keeps the old one) or are crushed"},
        "neutral": {"hex": neutral_hex, "oklch": [round(x, 3) for x in hex_to_oklch(neutral_hex)], "name": "warm neutral grey",
                    "note": "nobody's land: hunter-gatherers, stateless peoples, unorganised land; never blank"},
        "culture": {"applies_to": "archaeological cultures before 3400 BCE", "tint": {"chroma_factor": 0.40, "lightness_add": 0.15, "lightness_max": 0.94},
                    "dots": {"colour": "the culture's assigned colour at full chroma", "spacing_px": 5, "radius_px": 1},
                    "note": "tint(hex, 'culture'): a desaturated pastel with a dotted fill, labelled as a culture, not a state"},
        "expansion_outline": {"colour": "tint(hex, 'outline'): the state's colour darkened by 0.12 L at chroma x1.3", "width_px": 2, "duration": "the first year the land is held"},
        "label": {"colour": "tint(hex, 'label'): the state's colour at L -0.30 (not below 0.22), chroma x0.9", "note": "label size follows area"},
        "basemap": "no modern borders or labels: land, water, rivers and relief only, so the state colours are the only colours on the map",
    }


def cmd_seed(args):
    sys.path.insert(0, str(HERE))
    import colour_seed as S
    force = "--force" in args
    old = load_registry() if REGISTRY.exists() else None
    if old and not force:
        sys.exit("colours.json exists; seed --force rewrites rules, families, wheel and fixed (assigned and log are kept)")
    polities = read_polities()
    fixed, seen, unknown = [], set(), []
    for slug, L, C, h, family, group, note in S.FIXED:
        if slug in seen:
            sys.exit("duplicate fixed slug: " + slug)
        seen.add(slug)
        if slug not in polities:
            unknown.append(slug)
            continue
        Cmax = max_chroma(L, h)
        Cc = min(C, Cmax)
        e = {"slug": slug, "name": polities[slug]["name"], "hex": oklch_to_hex(L, Cc, h), "family": family,
             "oklch": [L, round(Cc, 3), h]}
        if group:
            e["group"] = group
        e["note"] = note + ("" if Cc >= C - 1e-6 else " (chroma clipped to the sRGB gamut: %.3f)" % Cc)
        if family not in S.FAMILIES:
            sys.exit("unknown family %s for %s" % (family, slug))
        fixed.append(e)
    if unknown:
        print("WARNING: %d fixed slugs are not in polities.csv and were skipped: %s" % (len(unknown), ", ".join(unknown)), file=sys.stderr)
    neutral_hex = oklch_to_hex(0.86, 0.012, 75)
    reg = {
        "version": 1, "written": _today(), "owner": "the colour agent (Phase A seed by the colours builder)",
        "tool": "tools/colour.py (see tools/colours-README.md); never edit hex values by hand",
        "rules": make_rules(S.MIN_DISTANCE, S.MIN_DISTANCE_WHY, neutral_hex),
        "families": S.FAMILIES,
        "wheel": {"hues": S.WHEEL["hues"], "variants": S.WHEEL["variants"], "note": S.WHEEL["note"], "colours": build_wheel(S.WHEEL)},
        "fixed": fixed,
        "assigned_meta": (old or {}).get("assigned_meta", {}),
        "assigned": (old or {}).get("assigned", {}),
        "log": (old or {}).get("log", []),
    }
    # warnings: two contemporary states (different groups) on nearly the same colour, so one map could show
    # both in one colour (states that never overlap in time may share a colour: Rome and the Han are both red);
    # and a colour too close to the neutral grey
    span = {s: (int(r["first_year"] or -9999), int(r["last_year"] or 9999)) for s, r in polities.items()}
    near = 0
    for i in range(len(fixed)):
        for j in range(i + 1, len(fixed)):
            a, b = fixed[i], fixed[j]
            if a.get("group") and a.get("group") == b.get("group"):
                continue
            sa, sb = span.get(a["slug"]), span.get(b["slug"])
            if sa and sb and (sa[1] < sb[0] or sb[1] < sa[0]):
                continue
            d = distance(a["hex"], b["hex"])
            if d < 0.03:
                near += 1
            if d < 0.02:
                print("WARNING: %s (%d..%d) and %s (%d..%d) are %.3f apart (two contemporary states on one colour)" % (
                    a["slug"], sa[0], sa[1], b["slug"], sb[0], sb[1], d), file=sys.stderr)
    if near:
        print("note: %d contemporary pairs of states are 0.02..0.03 apart (never neighbours; the neighbour rule is what check enforces)" % near, file=sys.stderr)
    for e in fixed + reg["wheel"]["colours"]:
        d = distance(e["hex"], neutral_hex)
        if d < S.MIN_DISTANCE:
            print("WARNING: %s is %.3f from the neutral grey" % (e.get("slug") or e.get("id"), d), file=sys.stderr)
    save_registry(reg)
    groups = {e["group"] for e in fixed if e.get("group")}
    print("seeded %s: %d fixed entries (%d states counting a group as one), %d families, wheel %d colours" % (
        REGISTRY, len(fixed), len(groups) + sum(1 for e in fixed if not e.get("group")), len(S.FAMILIES), len(reg["wheel"]["colours"])))


# ---------------------------------------------------------------------------------------------
# Adjacency from the anchors
# ---------------------------------------------------------------------------------------------

def _np():
    try:
        import numpy as np
        return np
    except ImportError:
        return None


def load_land(path=LAND_FILE):
    with open(path) as f:
        return [ln.strip() for ln in f if ln.strip()]


def neighbour_table(land, cache_dir=WORK):
    """For each land cell index, the indices of the land cells sharing an edge with it (grid_ring k=1),
    as a flat array of 6 int32 per cell, -1 for sea or missing. Cached once per land grid."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    n = len(land)
    key = {"n": n, "first": land[0], "last": land[-1], "res": 5}
    bin_path, key_path = cache_dir / "nbr_r5.bin", cache_dir / "nbr_r5.json"
    if bin_path.exists() and key_path.exists():
        try:
            if json.load(open(key_path)) == key:
                arr = array("i")
                with open(bin_path, "rb") as f:
                    arr.fromfile(f, n * 6)
                return arr
        except Exception:
            pass
    import h3
    index = {c: i for i, c in enumerate(land)}
    arr = array("i", [-1]) * (n * 6)
    t0 = _time()
    for i, c in enumerate(land):
        ring = h3.grid_ring(c, 1)
        k = 0
        for nb in ring:
            j = index.get(nb)
            if j is not None:
                arr[i * 6 + k] = j
                k += 1
                if k == 6:
                    break
    with open(bin_path, "wb") as f:
        arr.tofile(f)
    json.dump(key, open(key_path, "w"))
    print("built the H3 neighbour table for %d land cells in %.1f s" % (n, _time() - t0), file=sys.stderr)
    return arr


def _time():
    import time
    return time.time()


def expand_runs(runs):
    out = []
    for r in runs:
        if isinstance(r, str):
            a, b = r.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(r))
    return out


def anchor_files(anchor_dir=ANCHOR_DIR):
    files = sorted(p for p in Path(anchor_dir).glob("*.json") if not p.name.startswith("_"))
    return files


def year_adjacency(anchor, nbr, ring=1):
    """Edges (slug_a, slug_b) between owners of edge-sharing cells in one anchor, plus cells per slug.
    ring=2 also counts owners two cells apart (across a strait or a one-cell gap)."""
    owners = anchor["owners"]
    n = anchor["land_cells"]
    slugs = sorted(owners)
    sid = {s: i for i, s in enumerate(slugs)}
    cells = {s: 0 for s in slugs}
    np = _np()
    pairs = set()
    if np is not None:
        owner = np.full(n, -1, dtype=np.int32)
        for s in slugs:
            idx = np.fromiter(expand_runs(owners[s]), dtype=np.int64)
            cells[s] = int(idx.size)
            owner[idx] = sid[s]
        nb = np.frombuffer(nbr, dtype=np.int32).reshape(n, 6)
        owned = np.flatnonzero(owner >= 0)
        src = np.repeat(owner[owned], 6)
        j = nb[owned].ravel()
        ok = j >= 0
        src, j = src[ok], j[ok]
        hops = [(src, j)]
        if ring > 1:
            src2 = np.repeat(src, 6)
            j2 = nb[j].ravel()
            ok2 = j2 >= 0
            hops.append((src2[ok2], j2[ok2]))
        m = len(slugs)
        for s_arr, j_arr in hops:
            oj = owner[j_arr]
            both = (oj >= 0) & (oj != s_arr)
            a = np.minimum(s_arr[both], oj[both]).astype(np.int64)
            b = np.maximum(s_arr[both], oj[both]).astype(np.int64)
            for v in np.unique(a * m + b).tolist():
                pairs.add((slugs[v // m], slugs[v % m]))
    else:
        owner = [-1] * n
        for s in slugs:
            idx = expand_runs(owners[s])
            cells[s] = len(idx)
            for i in idx:
                owner[i] = sid[s]
        for i, oi in enumerate(owner):
            if oi < 0:
                continue
            base = i * 6
            for k in range(6):
                j = nbr[base + k]
                if j < 0:
                    continue
                oj = owner[j]
                if oj >= 0 and oj != oi:
                    pairs.add((slugs[min(oi, oj)], slugs[max(oi, oj)]))
                elif ring > 1:
                    for k2 in range(6):
                        j2 = nbr[j * 6 + k2]
                        if j2 >= 0:
                            o2 = owner[j2]
                            if o2 >= 0 and o2 != oi:
                                pairs.add((slugs[min(oi, o2)], slugs[max(oi, o2)]))
    return sorted(pairs), cells


def anchor_dir_arg(args):
    """The --anchors DIR option, else data/anchors/."""
    if "--anchors" in args:
        d = Path(args[args.index("--anchors") + 1])
        if not d.is_dir():
            sys.exit("--anchors %s is not a directory" % d)
        return d
    return ANCHOR_DIR


def load_adjacency(anchor_dir=ANCHOR_DIR, ring=1, cache_dir=WORK):
    """Per-anchor-year adjacency over every anchor file, cached under WORK keyed by the anchor files' sizes.
    Returns {"years": [{"year", "edges": [[a, b]...], "cells": {slug: n}}...], "ring": ring}."""
    anchor_dir = Path(anchor_dir).resolve()
    files = anchor_files(anchor_dir)
    if not files:
        return None
    key = {"ring": ring, "dir": str(anchor_dir), "files": [[p.name, p.stat().st_size] for p in files]}
    tag = "" if anchor_dir == ANCHOR_DIR.resolve() else "_" + _hashlib.md5(str(anchor_dir).encode()).hexdigest()[:8]
    cache = cache_dir / ("adjacency_r%d%s.json" % (ring, tag))
    if cache.exists():
        try:
            d = json.load(open(cache))
            if d.get("key") == key:
                return d
        except Exception:
            pass
    land = load_land()
    nbr = neighbour_table(land, cache_dir)
    years = []
    t0 = _time()
    for p in files:
        with open(p) as f:
            a = json.load(f)
        if a.get("land_cells") != len(land):
            raise SystemExit("%s was compiled on a different grid (%s cells, land_r5.txt has %d)" % (p.name, a.get("land_cells"), len(land)))
        edges, cells = year_adjacency(a, nbr, ring)
        years.append({"year": a["year"], "edges": edges, "cells": cells})
    d = {"key": key, "ring": ring, "built": _today(), "years": years}
    cache_dir.mkdir(parents=True, exist_ok=True)
    json.dump(d, open(cache, "w"))
    print("adjacency over %d anchors: %d year-edges in %.1f s" % (len(years), sum(len(y["edges"]) for y in years), _time() - t0), file=sys.stderr)
    return d


def load_seed_neighbours(seed_dir=SEED_DIR, cache_dir=WORK):
    """The polity table's neighbours[] (shapes within 25 km in an overlapping year, every year not just anchors),
    as {slug: {other: [from, to]}}; cached."""
    files = sorted(Path(seed_dir).glob("*.json")) if Path(seed_dir).exists() else []
    if not files:
        return {}
    cache = cache_dir / "seed_neighbours.json"
    key = [len(files), files[0].name, files[-1].name]
    if cache.exists():
        try:
            d = json.load(open(cache))
            if d.get("key") == key:
                return d["neighbours"]
        except Exception:
            pass
    out = {}
    for p in files:
        try:
            with open(p) as f:
                d = json.load(f)
        except Exception:
            continue
        out[d.get("slug", p.stem)] = {n["slug"]: [n.get("from"), n.get("to")] for n in d.get("neighbours", [])}
    cache_dir.mkdir(parents=True, exist_ok=True)
    json.dump({"key": key, "neighbours": out}, open(cache, "w"))
    return out


def union_graph(adj, seed_nb=None):
    """slug -> set(neighbour slugs) over every anchor year (and the seed neighbours when given),
    plus slug -> max cells over the anchors and slug -> mean per-year degree (crowding)."""
    nb = defaultdict(set)
    size = defaultdict(int)
    degs = defaultdict(list)
    for y in adj["years"]:
        d = defaultdict(int)
        for a, b in y["edges"]:
            nb[a].add(b)
            nb[b].add(a)
            d[a] += 1
            d[b] += 1
        for s, n in y["cells"].items():
            size[s] = max(size[s], n)
            degs[s].append(d.get(s, 0))
    if seed_nb:
        for s, others in seed_nb.items():
            for o in others:
                if o != s:
                    nb[s].add(o)
                    nb[o].add(s)
    crowd = {s: (sum(v) / len(v) if v else 0.0) for s, v in degs.items()}
    return nb, size, crowd


# ---------------------------------------------------------------------------------------------
# assign
# ---------------------------------------------------------------------------------------------

def variant_for(size_cells, crowd):
    """The lightness variant the crowding rule prefers: light for small states among many neighbours,
    deep for large or isolated ones, mid otherwise. crowd is the mean number of neighbours per anchor year
    (for a polity that falls between anchors, half its lifetime neighbour count)."""
    if size_cells < 150 and crowd >= 4:
        return "light"
    if size_cells >= 3000 or crowd < 2:
        return "deep"
    return "mid"


def pick_colour(wheel_lab, wheel, nb_labs, preferred, usage, minimum, exclude_ids=()):
    """The wheel colour for one polity: among the preferred variant's hues those at least `minimum` from every
    coloured neighbour, the one with the best (capped) margin, ties to the least-used hue; then the other
    variants; failing that the best margin anywhere (reported as short)."""
    order = [preferred] + [v for v in ("mid", "light", "deep") if v != preferred]
    best_any, best_any_d = None, -1.0
    for variant in order:
        feasible = []
        for i, w in enumerate(wheel):
            if w["variant"] != variant or w["id"] in exclude_ids:
                continue
            lab = wheel_lab[i]
            d = min((math.dist(lab, nl) for nl in nb_labs), default=1.0)
            if d > best_any_d:
                best_any, best_any_d = i, d
            if d >= minimum:
                feasible.append((min(d, 0.20), -usage[w["id"]], -abs(w["hue"] - 180) * 1e-4, i, d))
        if feasible:
            feasible.sort(reverse=True)
            i, d = feasible[0][3], feasible[0][4]
            return i, d, False
    return best_any, best_any_d, True


def cmd_assign(args):
    reg = load_registry()
    minimum = reg["rules"]["oklab_min_distance"]
    if "--min" in args:  # for measuring the wheel's capacity; the registry's rule is not changed
        minimum = float(args[args.index("--min") + 1])
    polities = read_polities()
    anchor_dir = anchor_dir_arg(args)
    adj = load_adjacency(anchor_dir, ring=1)
    seed_nb = None if "--no-seed-neighbours" in args else load_seed_neighbours()
    if adj is None:
        sys.exit("no anchors under %s; nothing to colour (use `python3 -I colour.py synthetic` to test the algorithm)" % anchor_dir)
    nb, size, crowd = union_graph(adj, seed_nb)
    fixed = {e["slug"]: e["hex"] for e in reg["fixed"]}
    colour = dict(fixed)
    lab = {s: hex_to_oklab(h) for s, h in colour.items()}
    wheel = reg["wheel"]["colours"]
    wheel_lab = [hex_to_oklab(w["hex"]) for w in wheel]
    usage = defaultdict(int)
    todo = [s for s in polities if s not in fixed]
    cells_of = lambda s: size.get(s) or (float(polities[s]["max_area_km2"] or 0) / 252.9)
    crowd_of = lambda s: crowd[s] if s in crowd else len(nb.get(s, ())) / 2.0
    todo.sort(key=lambda s: (-cells_of(s), s))
    assigned, short, variants = {}, [], defaultdict(int)
    for s in todo:
        nb_labs = [lab[o] for o in nb.get(s, ()) if o in lab and o != s]
        pref = variant_for(cells_of(s), crowd_of(s))
        i, d, is_short = pick_colour(wheel_lab, wheel, nb_labs, pref, usage, minimum)
        w = wheel[i]
        usage[w["id"]] += 1
        colour[s] = w["hex"]
        lab[s] = wheel_lab[i]
        e = {"hex": w["hex"], "wheel": w["id"], "min": round(d, 3) if nb_labs else None, "neighbours": len(nb_labs)}
        if is_short:
            e["short"] = True
            short.append((s, d))
        assigned[s] = e
        variants[w["variant"]] += 1
    meta = {"written": _today(), "anchors": len(adj["years"]), "ring": adj["ring"], "seed_neighbours": bool(seed_nb),
            "polities": len(todo), "fixed": len(fixed), "min_distance": minimum,
            "short": len(short), "variants": dict(variants),
            "order": "largest polity first (max cells over the anchors, else Cliopatria area); light variant for small states with 4 or more neighbours a year, deep for large or isolated ones, mid otherwise",
            "note": "assigned colours are from the wheel; change one only with `colour.py set`"}
    if "--dry" in args:
        print(json.dumps(meta, indent=1))
    else:
        reg["assigned"] = assigned
        reg["assigned_meta"] = meta
        save_registry(reg)
    print("assigned %d polities (%d fixed kept); variants %s; %d short of the minimum %.2f" % (
        len(assigned), len(fixed), dict(variants), len(short), minimum))
    for s, d in sorted(short, key=lambda x: x[1])[:40]:
        print("  short: %-40s best margin %.3f (%d neighbours)" % (s, d, len(nb.get(s, ()))))


# ---------------------------------------------------------------------------------------------
# check
# ---------------------------------------------------------------------------------------------

def family_hue_range(reg, family):
    r = (reg.get("families", {}).get(family) or {}).get("hue")
    return r


def hue_in_range(h, rng):
    a, b = rng
    h %= 360
    return a <= h <= b if a <= b else (h >= a or h <= b)


def suggest(reg, slug, colour, lab, nb, wheel, wheel_lab, minimum, is_fixed):
    """A replacement colour for `slug` that clears every neighbour: a fixed polity keeps its L and C and turns its
    hue inside its family range; a wheel polity takes the best wheel colour."""
    others = [lab[o] for o in nb.get(slug, ()) if o in lab and o != slug]
    if is_fixed:
        e = next(x for x in reg["fixed"] if x["slug"] == slug)
        L, C, h0 = e.get("oklch") or list(hex_to_oklch(e["hex"]))
        rng = family_hue_range(reg, e.get("family")) or [0, 359]
        best = None
        for step in range(0, 360, 5):
            h = (h0 + step) % 360
            if not hue_in_range(h, rng):
                continue
            for Lx in (L, L + 0.1, L - 0.1):
                if not 0.4 <= Lx <= 0.86:
                    continue
                cand = oklch_to_hex(Lx, C, h)
                cl = hex_to_oklab(cand)
                d = min((math.dist(cl, o) for o in others), default=1.0)
                if best is None or d > best[0]:
                    best = (d, cand, "oklch(%.2f, %.3f, %d)" % (Lx, C, h))
                if d >= minimum and Lx == L:
                    return cand, d, "turn the hue to %d in family %s" % (h, e.get("family"))
        return best[1], best[0], "best inside family %s: %s" % (e.get("family"), best[2])
    usage = defaultdict(int)
    cur = reg.get("assigned", {}).get(slug, {})
    pref = (cur.get("wheel") or "mid").split("-")[-1] if cur.get("wheel", "").startswith("h") else "mid"
    i, d, is_short = pick_colour(wheel_lab, wheel, others, pref, usage, minimum, exclude_ids=(cur.get("wheel"),))
    return wheel[i]["hex"], d, "wheel %s" % wheel[i]["id"]


def year_relations(anchor_dir, adj, drawn=False):
    """For check --relations / --drawn: {year: (suzerains, wholly)} from each file's `status` vassal and constituent
    groups. suzerains is {owner: {suzerain}}; wholly (with drawn) is the owners whose every cell that year is under
    a suzerain, so their own colour is not drawn. Files without a status key give no relations."""
    out = {}
    cells_of = {y["year"]: y["cells"] for y in adj["years"]}
    for p in anchor_files(anchor_dir):
        with open(p) as f:
            a = json.load(f)
        suz, under = defaultdict(set), defaultdict(int)
        for kind in ("vassal", "constituent"):
            for g in (a.get("status") or {}).get(kind, []):
                if g.get("suzerain") and g["suzerain"] != g["owner"]:  # a state's own vassal land is drawn in its tint
                    suz[g["owner"]].add(g["suzerain"])
                    under[g["owner"]] += len(expand_runs(g.get("cells", [])))
        cells = cells_of.get(a["year"], {})
        out[a["year"]] = (suz, {s for s, n in under.items() if drawn and n >= cells.get(s, 0) > 0})
    return out


def cmd_check(args):
    reg = load_registry()
    minimum = reg["rules"]["oklab_min_distance"]
    if "--min" in args:
        minimum = float(args[args.index("--min") + 1])
    ring = int(args[args.index("--ring") + 1]) if "--ring" in args else 1
    only_year = int(args[args.index("--year") + 1]) if "--year" in args else None
    anchor_dir = anchor_dir_arg(args)
    adj = load_adjacency(anchor_dir, ring=ring)
    if adj is None:
        sys.exit("no anchors under %s" % anchor_dir)
    seed_nb = load_seed_neighbours()
    nb, size, crowd = union_graph(adj, seed_nb)
    colour = colour_map(reg)
    groups = group_map(reg)
    fixed = {e["slug"] for e in reg["fixed"]}
    lab = {s: hex_to_oklab(h) for s, h in colour.items()}
    wheel = reg["wheel"]["colours"]
    wheel_lab = [hex_to_oklab(w["hex"]) for w in wheel]
    pairs, intended, uncoloured, checked = {}, {}, set(), 0
    use_rel = "--relations" in args or "--drawn" in args
    rel, skipped = (year_relations(anchor_dir, adj, "--drawn" in args) if use_rel else {}), 0
    for y in adj["years"]:
        if only_year is not None and y["year"] != only_year:
            continue
        suz, wholly = rel.get(y["year"], ({}, set()))
        for a, b in y["edges"]:
            if a not in colour or b not in colour:
                uncoloured.update(s for s in (a, b) if s not in colour)
                continue
            if suz:
                sa, sb = suz.get(a, set()), suz.get(b, set())
                if b in sa or a in sb or (sa & sb) or a in wholly or b in wholly:
                    skipped += 1
                    continue
            checked += 1
            d = math.dist(lab[a], lab[b])
            if d >= minimum:
                continue
            key = (a, b)
            target = intended if (groups.get(a) and groups.get(a) == groups.get(b)) else pairs
            if key not in target:
                target[key] = {"d": d, "years": []}
            target[key]["years"].append(y["year"])
    rows = []
    for (a, b), v in pairs.items():
        smaller = a if size.get(a, 0) <= size.get(b, 0) else b
        hexs, dmin, how = suggest(reg, smaller, colour, lab, nb, wheel, wheel_lab, minimum, smaller in fixed)
        rows.append({"a": a, "b": b, "distance": round(v["d"], 3), "years": [min(v["years"]), max(v["years"])], "n_years": len(v["years"]),
                     "a_hex": colour[a], "b_hex": colour[b], "a_cells": size.get(a, 0), "b_cells": size.get(b, 0),
                     "a_kind": "fixed" if a in fixed else "wheel", "b_kind": "fixed" if b in fixed else "wheel",
                     "recolour": smaller, "suggestion": hexs, "suggestion_margin": round(dmin, 3), "how": how})
    rows.sort(key=lambda r: r["distance"])
    if "--json" in args:
        out = args[args.index("--json") + 1]
        json.dump({"minimum": minimum, "ring": ring, "pairs_checked": checked, "clashes": rows,
                   "relations": ("drawn" if "--drawn" in args else "relations") if use_rel else None, "pairs_skipped_by_relations": skipped,
                   "intended": [{"a": a, "b": b, "distance": round(v["d"], 3), "years": [min(v["years"]), max(v["years"])]} for (a, b), v in intended.items()],
                   "uncoloured": sorted(uncoloured)}, open(out, "w"), indent=1)
    print("check: minimum %.3f, ring %d, %d anchor years, %d neighbour pairs checked (year-pairs), %d distinct pairs below the minimum, %d same-group pairs (intended), %d uncoloured polities" % (
        minimum, ring, len(adj["years"]), checked, len(rows), len(intended), len(uncoloured)))
    if use_rel:
        print("  %d year-pairs skipped by --%s (vassal or constituent relation that year%s)" % (
            skipped, "drawn" if "--drawn" in args else "relations", "; or one side drawn wholly in a suzerain's tint" if "--drawn" in args else ""))
    limit = None if "--all" in args else 60
    for r in rows[:limit]:
        print("  %.3f  %5d..%-5d %-36s %s %s  ~  %-36s %s %s   -> recolour %s: %s (%s, margin %.3f)" % (
            r["distance"], r["years"][0], r["years"][1], r["a"][:36], r["a_hex"], r["a_kind"][0], r["b"][:36], r["b_hex"], r["b_kind"][0],
            r["recolour"], r["suggestion"], r["how"], r["suggestion_margin"]))
    if limit and len(rows) > limit:
        print("  ... %d more (use --all)" % (len(rows) - limit))
    if uncoloured:
        print("uncoloured polities seen in the anchors: " + ", ".join(sorted(uncoloured)[:30]) + (" ..." if len(uncoloured) > 30 else ""))
    return 1 if rows else 0


# ---------------------------------------------------------------------------------------------
# set, show, swatch, maths, synthetic
# ---------------------------------------------------------------------------------------------

def cmd_set(args):
    if len(args) < 2:
        sys.exit("usage: set SLUG HEX --note 'why' [--force]")
    slug, hexc = args[0], args[1].lower()
    hex_to_rgb(hexc)
    if not hexc.startswith("#"):
        hexc = "#" + hexc
    note = args[args.index("--note") + 1] if "--note" in args else ""
    if not note:
        sys.exit("set needs --note: say why the colour changes (the log keeps it)")
    reg = load_registry()
    minimum = reg["rules"]["oklab_min_distance"]
    adj = load_adjacency(ring=1)
    nb = union_graph(adj, load_seed_neighbours())[0] if adj else {}
    colour = colour_map(reg)
    groups = group_map(reg)
    if slug not in colour:
        sys.exit("%s has no colour yet (run assign) and is not a fixed entry" % slug)
    L, C, h = hex_to_oklch(hexc)
    if not (0.40 <= L <= 0.86):
        print("WARNING: L %.2f is outside the readable range 0.40..0.86" % L, file=sys.stderr)
    clashes = []
    for o in nb.get(slug, ()):
        if o in colour and o != slug and groups.get(o) != groups.get(slug, object()):
            d = distance(hexc, colour[o])
            if d < minimum:
                clashes.append((d, o, colour[o]))
    if clashes and "--force" not in args:
        print("refused: %s at %s would clash with %d neighbour(s):" % (slug, hexc, len(clashes)))
        for d, o, oh in sorted(clashes):
            print("  %.3f %s %s" % (d, o, oh))
        sys.exit(2)
    old = colour[slug]
    entry = next((e for e in reg["fixed"] if e["slug"] == slug), None)
    if entry:
        entry["hex"] = hexc
        entry["oklch"] = [round(L, 3), round(C, 3), round(h)]
        entry["note"] = (entry.get("note", "") + "; " if entry.get("note") else "") + "changed %s: %s" % (_today(), note)
    else:
        reg["assigned"][slug] = {"hex": hexc, "wheel": "manual", "min": None, "neighbours": len(nb.get(slug, ())), "note": note}
    reg.setdefault("log", []).append({"date": _today(), "slug": slug, "from": old, "to": hexc, "note": note, "forced": bool(clashes)})
    save_registry(reg)
    print("%s: %s -> %s (%s)%s" % (slug, old, hexc, note, " FORCED over %d clashes" % len(clashes) if clashes else ""))


def cmd_show(args):
    reg = load_registry()
    colour = colour_map(reg)
    fixed = {e["slug"]: e for e in reg["fixed"]}
    for slug in args:
        h = colour.get(slug)
        if not h:
            print("%s: no colour" % slug)
            continue
        L, C, hue = hex_to_oklch(h)
        e = fixed.get(slug) or reg["assigned"].get(slug, {})
        print("%s: %s  oklch(%.3f %.3f %.0f)  %s%s%s" % (slug, h, L, C, hue,
              ("fixed, family %s" % e.get("family")) if slug in fixed else ("wheel %s" % e.get("wheel")),
              (", group %s" % e["group"]) if e.get("group") else "", (": " + e["note"]) if e.get("note") else ""))
        print("   vassal %s  culture %s  label %s  outline %s" % (tint(h, "vassal", reg["rules"]), tint(h, "culture", reg["rules"]),
                                                               tint(h, "label", reg["rules"]), tint(h, "outline", reg["rules"])))


def cmd_swatch(args):
    reg = load_registry()
    out = Path(args[0]) if args else WORK / "swatch.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    neutral = reg["rules"]["neutral"]["hex"]
    html = ["<!doctype html><meta charset=utf-8><title>EmpireMap colours</title>",
            "<style>body{font:13px/1.3 system-ui;background:#f4f2ee;margin:20px}div.s{display:inline-block;width:150px;height:62px;margin:2px;padding:4px;color:#111;vertical-align:top;border-radius:3px;overflow:hidden}"
            "div.s small{display:block;font-size:10px;opacity:.75}h2{margin:18px 0 6px}</style>",
            "<h1>EmpireMap colour registry (%s)</h1><p>neutral grey (nobody's land): <span style='background:%s;padding:2px 10px'>%s</span></p>" % (reg["written"], neutral, neutral)]
    byfam = defaultdict(list)
    for e in reg["fixed"]:
        byfam[e["family"]].append(e)
    for fam in reg["families"]:
        html.append("<h2>%s <small>%s</small></h2>" % (fam, reg["families"][fam]["note"]))
        for e in byfam.get(fam, []):
            html.append("<div class=s style='background:%s'>%s<small>%s%s</small><small>vassal <span style='background:%s;padding:0 6px'>&nbsp;</span> label <span style='color:%s'>Aa</span></small></div>" % (
                e["hex"], e["name"][:28], e["hex"], (" · " + e["group"]) if e.get("group") else "", tint(e["hex"], "vassal", reg["rules"]), tint(e["hex"], "label", reg["rules"])))
    html.append("<h2>wheel</h2>")
    for w in reg["wheel"]["colours"]:
        html.append("<div class=s style='background:%s;width:60px;height:40px'>%s<small>%s</small></div>" % (w["hex"], w["id"], w["hex"]))
    if reg.get("assigned"):
        html.append("<h2>assigned (%d)</h2>" % len(reg["assigned"]))
        for slug, e in sorted(reg["assigned"].items()):
            html.append("<div class=s style='background:%s;width:120px;height:44px'>%s<small>%s %s</small></div>" % (e["hex"], slug[:24], e["hex"], e.get("wheel", "")))
    out.write_text("\n".join(html))
    print("wrote %s" % out)


def cmd_synthetic(args):
    """Test assign and check on a synthetic adjacency (a few hundred polities, random edges) without anchors."""
    import random
    n = int(args[0]) if args else 300
    rnd = random.Random(1)
    reg = load_registry()
    minimum = reg["rules"]["oklab_min_distance"]
    wheel = reg["wheel"]["colours"]
    wheel_lab = [hex_to_oklab(w["hex"]) for w in wheel]
    fixed_hex = [e["hex"] for e in reg["fixed"]]
    slugs = ["p%03d" % i for i in range(n)]
    # a planar-ish graph: each polity links to a few random others nearby in index, plus some long edges
    nb = defaultdict(set)
    for i in range(n):
        for j in range(i + 1, min(n, i + 1 + rnd.randint(2, 6))):
            nb[slugs[i]].add(slugs[j]); nb[slugs[j]].add(slugs[i])
        if rnd.random() < 0.3:
            j = rnd.randrange(n)
            if j != i:
                nb[slugs[i]].add(slugs[j]); nb[slugs[j]].add(slugs[i])
    colour, lab = {}, {}
    for i in range(0, n, 7):  # a seventh are "fixed" with registry colours
        colour[slugs[i]] = fixed_hex[i % len(fixed_hex)]
        lab[slugs[i]] = hex_to_oklab(colour[slugs[i]])
    usage = defaultdict(int)
    short = 0
    for s in slugs:
        if s in colour:
            continue
        nl = [lab[o] for o in nb[s] if o in lab]
        i, d, is_short = pick_colour(wheel_lab, wheel, nl, rnd.choice(["light", "mid", "deep"]), usage, minimum)
        colour[s], lab[s] = wheel[i]["hex"], wheel_lab[i]
        short += is_short
    clashes = sum(1 for a in slugs for b in nb[a] if a < b and math.dist(lab[a], lab[b]) < minimum)
    edges = sum(len(v) for v in nb.values()) // 2
    print("synthetic: %d polities, %d edges, max degree %d, %d short, %d clashing pairs at minimum %.2f" % (
        n, edges, max(len(v) for v in nb.values()), short, clashes, minimum))


def cmd_maths(cmd, args):
    reg = load_registry() if REGISTRY.exists() else None
    rules = reg["rules"] if reg else None
    if cmd == "distance":
        print("%.4f" % distance(args[0], args[1]))
    elif cmd == "blend":
        t = float(args[2]) if len(args) > 2 else 0.5
        c = blend(args[0], args[1], t)
        print(c, "hatch", tint(c, "hatch", rules))
    elif cmd == "tint":
        print(tint(args[0], args[1], rules))
    elif cmd == "oklch":
        for h in args:
            L, C, hue = hex_to_oklch(h)
            print("%s  oklch(%.3f %.3f %.1f)  in gamut chroma max %.3f" % (h, L, C, hue, max_chroma(L, hue)))
    elif cmd == "hex":
        L, C, h = (float(x) for x in args[:3])
        print(oklch_to_hex(L, C, h), "(chroma max %.3f)" % max_chroma(L, h))


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[1], argv[2:]
    if cmd == "seed":
        return cmd_seed(args)
    if cmd == "assign":
        return cmd_assign(args)
    if cmd == "check":
        return cmd_check(args)
    if cmd == "set":
        return cmd_set(args)
    if cmd == "show":
        return cmd_show(args)
    if cmd == "swatch":
        return cmd_swatch(args)
    if cmd == "synthetic":
        return cmd_synthetic(args)
    if cmd in ("distance", "blend", "tint", "oklch", "hex"):
        return cmd_maths(cmd, args)
    sys.exit("unknown command %s\n%s" % (cmd, __doc__))


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
