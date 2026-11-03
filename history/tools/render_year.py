#!/usr/bin/env python3
"""Draw the compiled map of one year as a PNG, for agents to look at (legibility before beauty).

    python3 -I tools/render_year.py <year> [--bbox lon1,lat1,lon2,lat2] [--out file.png] [--width 1600]
                                    [--highlight slug,...] [--labels N] [--compare-cliopatria] [--jan1]
                                    [--from DIR]

The ownership of the year is rebuilt from the window's start anchor (data/anchors-c/<stem>.json, 1 January
of the window's first year) plus the window's year records: compiled/<window>.json where a final file
exists, else compiled/_draft/<window>.json. By default the map shows the end of the year (after its
changes); --jan1 shows 1 January (before them). --from DIR reads the anchor and draft from a trial's
stage folder instead (tools/compile_dossiers.py --trial <window> --stage DIR); it holds one window.

Drawing: each pixel takes the H3 resolution-5 cell under it, so cells read as small hexagons when zoomed
in. A state's colour comes from colours.json (a stable colour from the slug's hash when it has none).
Following the plan (master-plan.md, levels of control):
  direct       the state's colour
  vassal       the suzerain's colour at the vassal tint: tools/colour.py tint(hex, "vassal") with the
               colours.json rules (OKLCH chroma x0.55, lightness +0.12). A colony is drawn the same way:
               the compiler gives it its metropole as suzerain (R1)
  constituent  the suzerain's colour at half the vassal tint: the OKLab midpoint of the full colour and
               its vassal tint (chroma about x0.78, lightness about +0.06)
  occupied     the owner's colour, lightened a little, with diagonal hatching in the occupier's colour; an
               occupied cell nobody owns (owner nobody, an occupier) is the occupier's hatching over the
               grey of nobody's land, as the site draws it (scripts/history/pack.py: owner 0, status occupied)
  contested    stripes of both claimants' colours
  nobody       grey land; sea is pale blue
Lines: thin grey between states; dark around a realm (a suzerain with the vassals, colonies and
constituents drawn in its colour); inside a realm each state keeps its own thin outline, in a darker
shade of the suzerain's colour. Labels name the cell's owner, so a vassal carries its own name.
--highlight fades every other state and outlines the named ones (a suzerain's tinted land stays lit with
it). --labels N writes the N largest states (by area in view) at a point inside each. --compare-cliopatria
adds a second panel below: Cliopatria's shapes for that year (tools/grid.py's feature cache when this
machine has it, else the nearest Phase A anchor, data/anchors/<stem>.json, at or before the year).

Output: --out; else DIR/render/<year>.png with --from DIR; else render_<year>.png in the current folder
(or under /tmp/claude-0/work/render_year/ when the current folder is inside the history folder). The path
is printed. Takes a few seconds for the world at 1600 px. Caches go to /tmp/claude-0/work/render_year/cache
and are replaced atomically, so several renders can run at once.
"""
import argparse
import colorsys
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import h3
import numpy as np
from h3.api import basic_int as h3i

HERE = Path(__file__).resolve().parent
HIST = HERE.parent
SRC = HIST                   # where anchors-c and compiled/ are read (--from DIR: a trial's stage)
CACHE = Path(os.environ.get("RENDER_YEAR_CACHE", "/tmp/claude-0/work/render_year/cache"))
FIRST_YEAR, LAST_YEAR = -6000, 2026
WORLD = (-180.0, -57.0, 180.0, 84.0)

DIRECT, VASSAL, OCCUPIED, CONTESTED, CONSTITUENT = 0, 1, 2, 3, 4
ST_CODE = {"direct": DIRECT, "neutral": DIRECT, "vassal": VASSAL, "occupied": OCCUPIED, "contested": CONTESTED,
           "constituent": CONSTITUENT}
SEA = (222, 233, 243)
NOBODY = (206, 206, 200)
FONT_DIRS = ["/usr/share/fonts/truetype/dejavu/", "/usr/share/fonts/dejavu/", "/usr/share/fonts/TTF/"]


def stem(year):
    return ("m%04d" % -year) if year < 0 else ("p%04d" % year)


def window_of(year):
    """The window holding a year: (id, first year, last year), as tools/compile_dossiers.py cuts them."""
    if year < 1600:
        a = FIRST_YEAR + (year - FIRST_YEAR) // 100 * 100
        b = a + 99
    else:
        a = 1600 + (year - 1600) // 10 * 10
        b = a + 9
    return "%s-%s" % (stem(a), stem(b)), a, b


def from_runs(runs):
    parts = []
    for r in runs:
        if isinstance(r, str):
            a, b = r.split("-")
            parts.append(np.arange(int(a), int(b) + 1, dtype=np.int64))
        else:
            parts.append(np.array([int(r)], dtype=np.int64))
    return np.concatenate(parts) if parts else np.zeros(0, dtype=np.int64)


def land_ints():
    """The land grid's cells as (sorted uint64 ids, their line numbers), cached under CACHE."""
    path = HIST / "data" / "grid" / "land_r5.txt"
    st = path.stat()
    cp = CACHE / ("land_r5_%d_%d.npz" % (st.st_size, int(st.st_mtime)))
    if cp.exists():
        z = np.load(cp)
        return z["ids"], z["order"]
    with open(path) as f:
        cells = [line.strip() for line in f if line.strip()]
    arr = np.fromiter((h3.str_to_int(c) for c in cells), dtype=np.uint64, count=len(cells))
    order = np.argsort(arr)
    ids = arr[order]
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = cp.with_name("%s.tmp%d.npz" % (cp.stem, os.getpid()))
    np.savez(tmp, ids=ids, order=order)
    os.replace(tmp, cp)
    return ids, order


class Names:
    def __init__(self):
        self.list, self.id = [], {}

    def __call__(self, s):
        if s is None:
            return -1
        i = self.id.get(s)
        if i is None:
            i = self.id[s] = len(self.list)
            self.list.append(s)
        return i


def compiled_state(year, jan1, n, names):
    """-> owner, status, extra arrays and a description of the sources used."""
    wid, a, b = window_of(year)
    anchor = SRC / "data" / "anchors-c" / (stem(a) + ".json")
    final = SRC / "compiled" / (wid + ".json")
    draft = final if final.exists() else SRC / "compiled" / "_draft" / (wid + ".json")
    if not anchor.exists() or (not draft.exists() and (year - 1 if jan1 else year) >= a):
        have = sorted(q.stem for q in (SRC / "compiled" / "_draft").glob("*.json")) if (SRC / "compiled" / "_draft").is_dir() else []
        raise SystemExit("render_year: %s has no anchor %s and draft %s for %d%s" % (
            SRC, anchor.name, wid, year, ("; it holds %s" % ", ".join(have)) if have else ""))
    owner = np.full(n, -1, np.int32)
    status = np.zeros(n, np.int8)
    extra = np.full(n, -1, np.int32)
    with open(anchor, encoding="utf-8") as f:
        an = json.load(f)
    for s, runs in an["owners"].items():
        owner[from_runs(runs)] = names(s)
    for st, groups in (an.get("status") or {}).items():
        for g in groups:
            c = from_runs(g["cells"])
            status[c] = ST_CODE[st]
            ex = g.get("suzerain") or g.get("occupier") or ((g.get("claimants") or [None, None])[1])
            extra[c] = names(ex)
    last = year - 1 if jan1 else year
    used = 0
    if last >= a:
        with open(draft, encoding="utf-8") as f:
            d = json.load(f)
        for y in sorted((int(k) for k in d.get("years", {})), key=int):
            if y > last:
                break
            for c in d["years"][str(y)].get("changes", []):
                cells = from_runs(c["cells"])
                owner[cells] = names(c.get("to"))
                status[cells] = ST_CODE.get(c.get("status"), DIRECT)
                ex = c.get("suzerain") or c.get("occupier") or ((c.get("claimants") or [None, None])[1])
                extra[cells] = names(ex) if c.get("status") in ("vassal", "constituent", "occupied", "contested") else -1
            used += 1
    src = ("" if SRC == HIST else "%s: " % SRC) + "data/anchors-c/%s.json" % stem(a)
    if last >= a:
        src += " + %s (%d years with records)" % (draft.relative_to(SRC), used)
    return owner, status, extra, src


def cliopatria_state(year, n, names, land_ids, land_order):
    """Cliopatria's shapes alive in the year on the grid -> (owner, description). The feature cache of
    tools/grid.py when this machine has it, else the nearest Phase A anchor at or before the year."""
    owner = np.full(n, -1, np.int32)
    try:
        sys.path.insert(0, str(HIST / "tools"))
        import grid
        if grid.FEATURES_PKL.exists() or grid.CLIO.exists():
            fts = grid.features_alive(year, leaf_only=True)
            name2slug = {}
            pc = HIST / "data" / "polities.csv"
            if pc.exists():
                import csv
                with open(pc, newline="", encoding="utf-8") as f:
                    for r in csv.DictReader(f):
                        name2slug[r["name"]] = r["slug"]
            for ft in sorted(fts, key=lambda ft: -ft["area"]):     # small shapes drawn last, on top
                cp = grid.CELLS_DIR / ("%05d.npy" % ft["i"])
                if cp.exists():                    # read grid.py's cell cache, never write it
                    arr = np.load(cp)
                else:
                    cells = grid.shape_cells(grid.feature_geometry(ft))
                    arr = np.sort(np.fromiter((h3.str_to_int(c) for c in cells), dtype=np.uint64, count=len(cells)))
                pos = np.searchsorted(land_ids, arr)
                pos[pos >= land_ids.size] = 0
                hit = land_ids[pos] == arr
                owner[land_order[pos[hit]]] = names(name2slug.get(ft["name"], ft["slug"]))
            return owner, "Cliopatria shapes alive in %d (%d, leaf shapes; tools/grid.py feature cache)" % (year, len(fts))
    except Exception as e:  # noqa: BLE001
        print("render_year: Cliopatria feature cache unavailable (%s); using a Phase A anchor" % e, file=sys.stderr)
    years = sorted(int(p.stem[1:]) * (-1 if p.stem[0] == "m" else 1)
                   for p in (HIST / "data" / "anchors").glob("[mp][0-9][0-9][0-9][0-9].json"))
    before = [y for y in years if y <= year] or years[:1]
    if not before:
        return owner, "no Phase A anchor found"
    ay = before[-1]
    with open(HIST / "data" / "anchors" / (stem(ay) + ".json"), encoding="utf-8") as f:
        an = json.load(f)
    for s, runs in an["owners"].items():
        owner[from_runs(runs)] = names(s)
    return owner, "Phase A anchor data/anchors/%s.json (Cliopatria on the grid, %d)" % (stem(ay), ay)


def read_colours():
    out = {}
    try:
        with open(HIST / "colours.json", encoding="utf-8") as f:
            c = json.load(f)
    except Exception:  # noqa: BLE001
        return out
    for r in c.get("fixed") or []:
        if isinstance(r, dict) and r.get("slug") and r.get("hex"):
            out[r["slug"]] = r["hex"]
    for slug, r in (c.get("assigned") or {}).items():
        if isinstance(r, dict) and r.get("hex"):
            out.setdefault(slug, r["hex"])
    return out


def read_rules():
    """colours.json "rules" (the tint factors), or {} to use colour.py's defaults."""
    try:
        with open(HIST / "colours.json", encoding="utf-8") as f:
            return json.load(f).get("rules") or {}
    except Exception:  # noqa: BLE001
        return {}


def _hex(rgb):
    return "#%02x%02x%02x" % tuple(int(round(min(255.0, max(0.0, float(c))))) for c in rgb)


def tints(pal, rules):
    """-> (vassal, constituent) palettes: each colour's vassal tint, tools/colour.py tint(hex, "vassal"),
    and the OKLab midpoint of the colour and that tint (half the tint)."""
    try:
        for d in (HERE, HIST / "tools"):             # the history folder's tools first
            if str(d) not in sys.path:
                sys.path.insert(0, str(d))
        import colour
        tint, blend = colour.tint, colour.blend
    except Exception as e:  # noqa: BLE001
        print("render_year: tools/colour.py did not load (%s); tints are a plain lightening" % e, file=sys.stderr)
        white = np.array([255, 255, 255], np.float32)
        return pal * 0.55 + white * 0.45, pal * 0.775 + white * 0.225
    pv, pc = np.zeros_like(pal), np.zeros_like(pal)
    memo = {}
    for i, rgb in enumerate(pal):
        hx = _hex(rgb)
        if hx not in memo:
            tv = tint(hx, "vassal", rules)
            memo[hx] = ([int(tv[k:k + 2], 16) for k in (1, 3, 5)],
                        [int(c[k:k + 2], 16) for c in [blend(hx, tv, 0.5)] for k in (1, 3, 5)])
        pv[i], pc[i] = memo[hx]
    return pv, pc


def fallback_colour(slug):
    h = hashlib.md5(slug.encode("utf-8")).digest()
    hue = h[0] / 255.0
    light = 0.50 + 0.18 * (h[1] / 255.0)
    sat = 0.40 + 0.30 * (h[2] / 255.0)
    r, g, b = colorsys.hls_to_rgb(hue, light, sat)
    return int(r * 255), int(g * 255), int(b * 255)


def palette(names, colours):
    pal = np.zeros((max(len(names.list), 1), 3), np.float32)
    for i, s in enumerate(names.list):
        hx = colours.get(s)
        if hx and len(hx) == 7:
            pal[i] = [int(hx[k:k + 2], 16) for k in (1, 3, 5)]
        else:
            pal[i] = fallback_colour(s)
    return pal


def view(bbox, width):
    """-> (lon0, lat0, lon1, lat1, width, height); lon1 may exceed 180 for a box across the antimeridian."""
    lon0, lat0, lon1, lat1 = bbox
    if lon1 <= lon0:
        lon1 += 360.0
    if bbox == WORLD:
        height = int(round(width * (lat1 - lat0) / (lon1 - lon0)))
    else:
        k = np.cos(np.radians((lat0 + lat1) / 2.0))
        height = int(round(width * (lat1 - lat0) / ((lon1 - lon0) * max(k, 0.2))))
    return lon0, lat0, lon1, lat1, width, max(height, 50)


def cell_map(v, land_ids, land_order):
    """Land cell index under each pixel (-1 for sea), looked up on a grid of step ~ 40 percent of a cell."""
    lon0, lat0, lon1, lat1, W, H = v
    cell_px = 0.14 * W / (lon1 - lon0)        # a res-5 cell is about 0.14 degrees of longitude at mid latitudes
    step = max(1, int(round(cell_px / 2.5)))
    xs = lon0 + (np.arange(0, W, step) + step / 2.0) * (lon1 - lon0) / W
    ys = lat1 - (np.arange(0, H, step) + step / 2.0) * (lat1 - lat0) / H
    xs = ((xs + 180.0) % 360.0) - 180.0
    f = h3i.latlng_to_cell
    ids = np.fromiter((f(la, lo, 5) for la in ys.tolist() for lo in xs.tolist()), dtype=np.uint64,
                      count=xs.size * ys.size).reshape(ys.size, xs.size)
    pos = np.searchsorted(land_ids, ids)
    pos[pos >= land_ids.size] = 0
    idx = np.where(land_ids[pos] == ids, land_order[pos], -1).astype(np.int32)
    if step > 1:
        idx = np.repeat(np.repeat(idx, step, axis=0), step, axis=1)
    return idx[:H, :W]


def boundaries(a, valid=None):
    """Pixels where a differs from its right or lower neighbour."""
    b = np.zeros(a.shape, bool)
    d = a[:, 1:] != a[:, :-1]
    b[:, 1:] |= d
    d2 = a[1:, :] != a[:-1, :]
    b[1:, :] |= d2
    if valid is not None:
        b &= valid
    return b


def compose(C, owner, status, extra, pal, highlight, pal_v, pal_c):
    H, W = C.shape
    land = C >= 0
    Ci = np.where(land, C, 0)
    own = np.where(land, owner[Ci], -2)
    st = np.where(land, status[Ci], 0)
    ex = np.where(land, extra[Ci], -1)
    img = np.empty((H, W, 3), np.float32)
    img[:] = SEA
    img[own == -1] = NOBODY
    has = own >= 0
    img[has] = pal[own[has]]
    yy, xx = np.mgrid[0:H, 0:W]
    white = np.array([255, 255, 255], np.float32)
    lord = np.where(ex >= 0, ex, own)              # a tinted cell takes its suzerain's colour
    m = has & (st == VASSAL)
    img[m] = pal_v[lord[m]]
    m = has & (st == CONSTITUENT)
    img[m] = pal_c[lord[m]]
    m = has & (st == OCCUPIED)
    img[m] = img[m] * 0.8 + white * 0.2
    m = land & (st == OCCUPIED)                    # owned or not: an unowned occupied cell keeps the grey fill
    hatch = m & ((xx - yy) % 7 < 2) & (ex >= 0)
    img[hatch] = pal[ex[hatch]]
    m = has & (st == CONTESTED) & (ex >= 0)
    stripe = m & (((xx + yy) // 4) % 2 == 1)
    img[stripe] = pal[ex[stripe]]
    if highlight:
        hl = np.isin(own, list(highlight)) | (np.isin(ex, list(highlight)) & np.isin(st, [VASSAL, CONSTITUENT]))
        fade = land & ~hl
        img[fade] = img[fade] * 0.3 + np.array([236, 236, 232], np.float32) * 0.7
    # lines: coast, states, realms (a tinted cell belongs to its suzerain's realm)
    realm = np.where(np.isin(st, [VASSAL, CONSTITUENT]) & (ex >= 0), ex, own)
    coast = boundaries(land.astype(np.int8))
    img[coast] = (120, 140, 160)
    sb = boundaries(own, land) & ~coast
    img[sb] = img[sb] * 0.45 + 60
    rb = boundaries(realm, land) & ~coast
    inner = sb & ~rb & (realm >= 0)                # a state's own outline inside a realm
    img[inner] = pal[realm[inner]] * 0.6
    if highlight:
        fl = inner & fade
        img[fl] = img[fl] * 0.3 + np.array([236, 236, 232], np.float32) * 0.7
    img[rb] = (35, 35, 35)
    if highlight:
        hb = boundaries(hl.astype(np.int8))           # around the named states with their tinted land
        hb |= np.roll(hb, 1, axis=0) | np.roll(hb, 1, axis=1)
        img[hb] = (0, 0, 0)
    return np.clip(img, 0, 255).astype(np.uint8), own


def interior_point(mask):
    """A pixel deep inside the largest part of a mask (erosion until it vanishes), or None."""
    ys, xs = np.nonzero(mask)
    if ys.size == 0:
        return None
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    m = np.zeros((y1 - y0 + 2, x1 - x0 + 2), bool)
    m[1:-1, 1:-1] = mask[y0:y1, x0:x1]
    last = m
    for _ in range(600):
        e = m.copy()
        e[1:, :] &= m[:-1, :]
        e[:-1, :] &= m[1:, :]
        e[:, 1:] &= m[:, :-1]
        e[:, :-1] &= m[:, 1:]
        if not e.any():
            break
        last = m = e
    py, px = np.nonzero(last)
    cy, cx = py.mean(), px.mean()
    i = int(np.argmin((py - cy) ** 2 + (px - cx) ** 2))
    return int(py[i]) + y0 - 1, int(px[i]) + x0 - 1


def font(size, bold=False):
    from PIL import ImageFont
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for d in FONT_DIRS:
        p = Path(d) / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default(size=size)


def display_names(slugs):
    out = {}
    for s in slugs:
        try:
            with open(HIST / "polities" / (s + ".json"), encoding="utf-8") as f:
                out[s] = json.load(f)["identity"].get("name") or s
        except Exception:  # noqa: BLE001
            out[s] = s
    return out


def draw_labels(im, own, names, n, width):
    from PIL import ImageDraw
    if n <= 0:
        return
    ids, cnt = np.unique(own[own >= 0], return_counts=True)
    order = np.argsort(-cnt)[:n]
    picks = [(int(ids[i]), int(cnt[i])) for i in order]
    dn = display_names([names.list[i] for i, _ in picks])
    dr = ImageDraw.Draw(im)
    base = max(9, int(round(12 * width / 1600.0)))
    boxes = []
    for rank, (sid, c) in enumerate(picks):
        p = interior_point(own == sid)
        if p is None:
            continue
        txt = dn.get(names.list[sid], names.list[sid])
        if len(txt) > 28:
            txt = txt[:27] + "."
        f = font(base + (3 if rank < 5 else 1 if rank < 15 else 0), bold=rank < 15)
        x0, y0, x1, y1 = dr.textbbox((0, 0), txt, font=f, stroke_width=2)
        w, h = x1 - x0, y1 - y0
        x, y = p[1] - w // 2, p[0] - h // 2
        x = min(max(x, 2), im.width - w - 2)
        y = min(max(y, 2), im.height - h - 2)
        bb = (x, y, x + w, y + h)
        if any(not (bb[2] < q[0] or bb[0] > q[2] or bb[3] < q[1] or bb[1] > q[3]) for q in boxes):
            continue
        boxes.append(bb)
        dr.text((x - x0, y - y0), txt, font=f, fill=(15, 15, 15), stroke_width=2, stroke_fill=(255, 255, 255))


def header(width, title, legend):
    """A title band; the legend sits at its right end, or on a second line when the image is narrow."""
    from PIL import Image, ImageDraw
    f = font(13, bold=True)
    fs = font(11)
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    need = int(probe.textlength(title, font=f)) + 12
    if legend:
        need += sum(int(probe.textlength(label, font=fs)) + 29 for label, _ in legend)
    two = bool(legend) and need > width
    h = 46 if two else 26
    im = Image.new("RGB", (width, h), (250, 250, 247))
    dr = ImageDraw.Draw(im)
    dr.text((6, 5), title, font=f, fill=(20, 20, 20))
    if legend:
        x = width - 6
        y0 = 26 if two else 6
        for label, sw in reversed(legend):
            tw = int(dr.textlength(label, font=fs)) + 1
            x -= tw
            dr.text((x, y0 + 1), label, font=fs, fill=(40, 40, 40))
            x -= 18
            im.paste(Image.fromarray(sw), (x, y0))
            x -= 10
    return im


def swatches(rules):
    """Small legend swatches (14 x 14) drawn the way the map draws each status; the tinted ones in the
    direct swatch's colour (the suzerain's), with the thin own outline."""
    base = np.array([70, 130, 180], np.float32)
    other = np.array([200, 90, 60], np.float32)
    white = np.array([255, 255, 255], np.float32)
    pv, pc = tints(base[None, :], rules)
    yy, xx = np.mgrid[0:14, 0:14]
    edge = (yy == 0) | (yy == 13) | (xx == 0) | (xx == 13)
    out = []
    a = np.empty((14, 14, 3), np.float32)
    a[:] = base
    out.append(("direct", a.copy()))
    a[:] = pv[0]
    a[edge] = base * 0.6
    out.append(("vassal, colony: suzerain's tint", a.copy()))
    a[:] = pc[0]
    a[edge] = base * 0.6
    out.append(("constituent: half tint", a.copy()))
    a[:] = base * 0.8 + white * 0.2
    a[((xx - yy) % 7 < 2)] = other
    out.append(("occupied", a.copy()))
    a[:] = NOBODY
    a[((xx - yy) % 7 < 2)] = other
    out.append(("occupied, no owner", a.copy()))
    a[:] = base
    a[(((xx + yy) // 4) % 2 == 1)] = other
    out.append(("contested", a.copy()))
    a[:] = NOBODY
    out.append(("nobody", a.copy()))
    return [(k, np.clip(v, 0, 255).astype(np.uint8)) for k, v in out]


def main(argv=None):
    global HIST, SRC
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("year", type=int)
    ap.add_argument("--bbox", help="lon1,lat1,lon2,lat2 (west, south, east, north); default: the world")
    ap.add_argument("--out", help="PNG path (default: see above)")
    ap.add_argument("--width", type=int, default=1600)
    ap.add_argument("--highlight", default="", help="slugs to emphasise, comma-separated")
    ap.add_argument("--labels", type=int, default=30, help="label the N largest states in view (default 30)")
    ap.add_argument("--compare-cliopatria", action="store_true", help="add a panel with Cliopatria's shapes")
    ap.add_argument("--jan1", action="store_true", help="1 January of the year instead of its end")
    ap.add_argument("--hist", default=None, help="the history folder (default: this tool's parent)")
    ap.add_argument("--from", dest="src", metavar="DIR", default=None,
                    help="read data/anchors-c and compiled/_draft from a trial's stage folder")
    argv = list(sys.argv[1:] if argv is None else argv)
    for i in range(len(argv) - 1):
        if argv[i] == "--bbox":           # a box starting west of Greenwich: "--bbox -10,35,30,60"
            argv[i:i + 2] = ["--bbox=" + argv[i + 1]]
            break
    args = ap.parse_args(argv)
    if args.hist:
        HIST = Path(args.hist)
    SRC = Path(args.src).resolve() if args.src else HIST
    from PIL import Image
    t0 = time.time()
    y = args.year
    if not FIRST_YEAR <= y <= LAST_YEAR:
        ap.error("year must be within %d..%d" % (FIRST_YEAR, LAST_YEAR))
    bbox = WORLD
    if args.bbox:
        try:
            bbox = tuple(float(v) for v in args.bbox.split(","))
            assert len(bbox) == 4 and bbox[3] > bbox[1]
        except Exception:  # noqa: BLE001
            ap.error("--bbox wants lon1,lat1,lon2,lat2 with lat2 > lat1")
    land_ids, land_order = land_ids_order = land_ints()
    n = land_ids.size
    names = Names()
    owner, status, extra, src = compiled_state(y, args.jan1, n, names)
    v = view(bbox, args.width)
    C = cell_map(v, *land_ids_order)
    highlight = set()
    for s in [x.strip() for x in args.highlight.split(",") if x.strip()]:
        if s in names.id:
            highlight.add(names.id[s])
        else:
            print("render_year: %s holds no land in %d" % (s, y), file=sys.stderr)
    panels = []
    clio = None
    if args.compare_cliopatria:
        clio = cliopatria_state(y, n, names, land_ids, land_order)
    pal = palette(names, read_colours())
    rules = read_rules()
    pal_v, pal_c = tints(pal, rules)
    img, own = compose(C, owner, status, extra, pal, highlight, pal_v, pal_c)
    im = Image.fromarray(img)
    draw_labels(im, own, names, args.labels, args.width)
    when = "1 January %d" % y if args.jan1 else "end of %d" % y
    nstates = len(np.unique(owner[owner >= 0]))
    panels.append(header(args.width, "%s  compiled (%s), %d states" % (when, src, nstates), swatches(rules)))
    panels.append(im)
    if clio is not None:
        co, csrc = clio
        z = np.zeros(n, np.int8)
        ze = np.full(n, -1, np.int32)
        pal = palette(names, read_colours())
        img2, own2 = compose(C, co, z, ze, pal, highlight, pal, pal)
        im2 = Image.fromarray(img2)
        draw_labels(im2, own2, names, args.labels, args.width)
        panels.append(header(args.width, "%d  %s" % (y, csrc), None))
        panels.append(im2)
    total_h = sum(p.height for p in panels)
    out_im = Image.new("RGB", (args.width, total_h), (255, 255, 255))
    yy = 0
    for p in panels:
        out_im.paste(p, (0, yy))
        yy += p.height
    name = "%s%s.png" % (y, "-jan1" if args.jan1 else "")
    if args.out:
        out = Path(args.out)
    elif args.src:
        out = SRC / "render" / name
    else:
        cwd, hr = Path.cwd().resolve(), HIST.resolve()
        inside = cwd == hr or hr in cwd.parents
        out = (Path("/tmp/claude-0/work/render_year") / ("%s-%d" % (name[:-4], os.getpid()) + ".png")) if inside \
            else cwd / ("render_" + name)
    out.parent.mkdir(parents=True, exist_ok=True)
    out_im.save(out, optimize=False)
    print("%s  (%dx%d, %.1f s)" % (out, out_im.width, out_im.height, time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
