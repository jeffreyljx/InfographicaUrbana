#!/usr/bin/env python3
"""Pack the historical-borders project into CartaHistoria's static data (public/history/).

    python3 -I scripts/history/pack.py /mnt/project-files/history            # write public/history/
    python3 -I scripts/history/pack.py /mnt/project-files/history --check    # replay and report only, write nothing
    options: --out DIR (default: public/history next to this repo's package.json)
             --drafts (read compiled/_draft/<window>.json even where a final compiled/<window>.json exists)

Run it again whenever the project's data changes (dossiers, colours, anchors or windows); it rewrites every file
it owns and deletes stale per-state files. It reads, never writes, the project folder. Needs numpy, and h3 for the
cell geometry (geo.bin is only rebuilt when the grid file changes).

Inputs (the project folder's layout, see its README.md and compiled/README.md):
    data/grid/land_r5.txt           the 524,441 H3 resolution-5 land cells; the line number is the cell id
    data/anchors-c/<stem>.json      full ownership at each window boundary (owners as runs, status groups)
    compiled/<window>.json          the window's per-year changes, captions and capitals (falls back to
                                    compiled/_draft/<window>.json until the window agent has written its file)
    colours.json                    one colour per state (fixed first, then assigned); states without one get a
                                    deterministic wheel colour from the slug's hash, marked "fb" in states.json
    polities/<slug>.json            one dossier per state: names, type, years, capitals, ledger, sources

Outputs (public/history/):
    index.json        the windows (file, years, bytes), the per-year count of cells that changed, the data's date
    geo.bin           gzip: the cell centres in Web Mercator, delta-coded (see GEO below)
    states.json       the state table: names, type, years, colour, capitals, search names (column arrays)
    w/<window>.bin    gzip: one window: the state of every cell at its start, then each year's changes, and its
                      captions (see CHUNK below)
    state/<slug>.json per state: names, years, capitals, rulers, area by year, ledger captions with sources, wars

GEO (after gunzip, little-endian): "CHG1", u32 N, u32 Q, then x as i32[N] and y as i32[N] split into byte planes
    (all low bytes, then the next byte, ...) of the delta-coded values: x[i] = x[i-1] + dx[i]. Mercator x, y in [0, 1]
    are x / Q, y / Q.
CHUNK (after gunzip): "CHW1", u32 header length, the header JSON (padded to 4 bytes), then the sections the header
    lists as name -> [byte offset, byte length], each 4-byte aligned:
      owner u16[N], status u8[N], other u16[N]      every cell at 1 January of the window's first year
      g_year i32[G], g_owner u16[G], g_status u8[G], g_other u16[G], g_runs u32[G]
                                                    the change groups, in year order: every cell in the group's
                                                    runs takes owner, status and other in g_year
      r_start u32[R] (delta-coded), r_len u32[R]    the runs, g_runs[g] of them per group
    owner and other are 1 + the row in states.json (0: nobody); status 0 direct, 1 vassal, 2 constituent,
    3 occupied, 4 contested; other is the suzerain (vassal, constituent), the occupier, or the other claimant.
"""
import argparse
import colorsys
import gzip
import hashlib
import json
import math
import os
import re
import shutil
import sys
import time
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[2]
FIRST, LAST = -6000, 2026
STATUS = {"direct": 0, "vassal": 1, "constituent": 2, "occupied": 3, "contested": 4, "neutral": 0}
TYPE_CODE = {"state": "s", "dynasty": "d", "culture": "c", "colony": "k", "rebel": "r", "umbrella": "u"}
Q = 2 ** 21          # Mercator quantisation of the cell centres (about 19 m at the equator)
CELL_KM2 = 252.9


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- helpers

def runs_to_idx(runs):
    """["401233-401240", 401242, ...] -> int array of cell ids."""
    if not runs:
        return np.zeros(0, np.int64)
    starts, ends = [], []
    for r in runs:
        if isinstance(r, int):
            starts.append(r); ends.append(r)
        else:
            a, b = r.split("-")
            starts.append(int(a)); ends.append(int(b))
    s = np.asarray(starts, np.int64); e = np.asarray(ends, np.int64)
    lens = e - s + 1
    if len(s) == 1:
        return np.arange(s[0], e[0] + 1)
    off = np.repeat(s - np.concatenate(([0], np.cumsum(lens)[:-1])), lens)
    return np.arange(lens.sum()) + off


def idx_to_runs(idx):
    """sorted unique cell ids -> (starts, lengths)."""
    if len(idx) == 0:
        return np.zeros(0, np.int64), np.zeros(0, np.int64)
    idx = np.sort(idx)
    brk = np.nonzero(np.diff(idx) != 1)[0] + 1
    starts = idx[np.concatenate(([0], brk))]
    ends = idx[np.concatenate((brk - 1, [len(idx) - 1]))]
    return starts, ends - starts + 1


def first_sentence(text, limit=320):
    """The caption: the note's first sentence (the dossier rule), cut at a sane length."""
    if not text:
        return ""
    t = " ".join(str(text).split())
    m = re.search(r"(?<=[.!?])[\"')\]]?\s+(?=[A-Z0-9'\"(\[])", t)
    s = t[:m.start() + 1].rstrip() if m and m.start() > 12 else t
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return s


# the compilers' workings, which a reader of the map should not see: "(infobox 1642-1663)", "(121 cells)",
# "(Cliopatria's British Raj row ends in 1947)", "; page silent"
WORKINGS = re.compile(r"\bcells?\b|Cliopatria|\brows?\b|page silent|\bpage's\b|\bthe page\b|^page undated|infobox|\bshapes?\b|keyframe|\bsnap"
                      r"|\banchors?\b|\bthe map's\b|dossier|gazetteer|reviewer|polygon|my reading|\boutline\b|as drawn|the window|/ledger/", re.I)
# a parenthesis that names the pages or files behind a caption is workings too: "(Lucanians page; ...)", "(eu-19)"
PAREN_WORKINGS = re.compile(WORKINGS.pattern + r"|\bpages?\b|\bledger\b|\b[a-z]{2}-\d{2}\b", re.I)


def public_text(text):
    """A caption as the map shows it: parentheses that hold the compilers' workings dropped, and the result returned
    with a flag for whether workings are still left in it (those are kept on the state's page, not in the dock)."""
    t = text
    for _ in range(3):
        t2 = re.sub(r"\s*\([^()]*\)", lambda m: "" if PAREN_WORKINGS.search(m.group(0)) else m.group(0), t)
        if t2 == t:
            break
        t = t2
    t = re.sub(r";\s*page silent\.?$", ".", t, flags=re.I)
    t = re.sub(r"\s+([.,;:])", r"\1", t).strip()
    if t and t[-1] not in ".!?…'\"":
        t += "."
    return t, bool(WORKINGS.search(t))


def pretty_name(s):
    """A party named without a dossier: keep names, title-case slug-like strings."""
    if re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)+", s):
        return " ".join(w if w in ("of", "the", "and", "de", "al", "el") else w.capitalize() for w in s.split("-"))
    return s


# ---- OKLab / OKLCH (Ottosson), for the fallback colours: same maths as tools/colour.py
def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _gam(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def oklch_to_rgb(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return r, g, bb


def oklch_hex(L, C, h):
    """OKLCH -> #rrggbb, chroma reduced until the colour is inside sRGB."""
    while C > 0:
        rgb = oklch_to_rgb(L, C, h)
        if all(-1e-4 <= v <= 1 + 1e-4 for v in rgb):
            break
        C -= 0.005
    rgb = oklch_to_rgb(L, max(C, 0), h)
    return "#" + "".join("%02x" % round(255 * min(1, max(0, _gam(min(1, max(0, v)))))) for v in rgb)


def fallback_colour(slug, wheel):
    """A deterministic wheel colour from the slug's hash (until the colour agent gives the state its own)."""
    hues = wheel.get("hues") or list(range(0, 360, 15))
    variants = wheel.get("variants") or {"mid": {"L": 0.7, "C": 0.12}}
    names = [v for v in ("mid", "light", "deep") if v in variants]
    h = int(hashlib.sha1(slug.encode()).hexdigest()[:8], 16)
    hue = hues[h % len(hues)]
    var = variants[names[(h // len(hues)) % len(names)]]
    return oklch_hex(var["L"], var["C"], hue)


def write_gz(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        # mtime=0 so an unchanged input gives a byte-identical file (clean git diffs)
        with gzip.GzipFile(fileobj=f, mode="wb", compresslevel=9, mtime=0) as g:
            g.write(data)
    return path.stat().st_size


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    path.write_text(s, encoding="utf-8")
    return len(s.encode())


def planes(a):
    """Byte planes of an array (all first bytes, then all second bytes, ...): compresses far better."""
    b = np.ascontiguousarray(a).view(np.uint8).reshape(-1, a.dtype.itemsize)
    return b.T.copy().tobytes()


# ---------------------------------------------------------------- geometry

def build_geo(grid_path, out_path):
    import h3
    cells = [l.strip() for l in open(grid_path) if l.strip()]
    n = len(cells)
    xs = np.zeros(n, np.int64); ys = np.zeros(n, np.int64)
    for i, c in enumerate(cells):
        lat, lon = h3.cell_to_latlng(c)
        lat = max(-85.0511, min(85.0511, lat))
        x = (lon + 180.0) / 360.0
        y = (1 - math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) / math.pi) / 2
        xs[i] = round(x * Q); ys[i] = round(y * Q)
    dx = np.diff(xs, prepend=0).astype(np.int32); dy = np.diff(ys, prepend=0).astype(np.int32)
    head = b"CHG1" + np.array([n, Q], np.uint32).tobytes()
    size = write_gz(out_path, head + planes(dx) + planes(dy))
    return n, size


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("project", help="the project folder (history/)")
    ap.add_argument("--out", default=str(REPO / "public" / "history"))
    ap.add_argument("--drafts", action="store_true", help="read the Phase C drafts even where a final window exists")
    ap.add_argument("--check", action="store_true", help="replay and report; write nothing")
    args = ap.parse_args()
    H = Path(args.project).resolve()
    OUT = Path(args.out).resolve()
    t0 = time.time()

    # ---- grid and geometry
    grid_path = H / "data" / "grid" / "land_r5.txt"
    grid_sha = hashlib.sha1(grid_path.read_bytes()).hexdigest()
    N = sum(1 for l in open(grid_path) if l.strip())
    log(f"grid: {N:,} cells ({grid_sha[:10]})")
    old_index = {}
    if (OUT / "index.json").exists():
        try:
            old_index = json.loads((OUT / "index.json").read_text())
        except Exception:
            old_index = {}
    if not args.check:
        if old_index.get("grid_sha") == grid_sha and (OUT / "geo.bin").exists():
            log("geo.bin: grid unchanged, kept")
        else:
            n, size = build_geo(grid_path, OUT / "geo.bin")
            log(f"geo.bin: {n:,} centres, {size / 1e6:.2f} MB")

    # ---- colours
    reg = json.loads((H / "colours.json").read_text())
    colour = {}
    for e in reg.get("fixed", []):
        colour.setdefault(e["slug"], e["hex"].lower())
    for s, e in (reg.get("assigned") or {}).items():
        colour.setdefault(s, e["hex"].lower())
    wheel = reg.get("wheel") or {}
    neutral = ((reg.get("rules") or {}).get("neutral") or {}).get("hex", "#d6d0c9")

    # ---- dossiers
    dossiers = {}
    bad = []
    for p in sorted((H / "polities").glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            d = json.loads(p.read_text())
            dossiers[d["identity"]["slug"] if d.get("identity", {}).get("slug") == p.stem else p.stem] = d
        except Exception as ex:   # a file mid-write by another agent: skip it, say so
            bad.append(f"{p.name}: {ex}")
    log(f"dossiers: {len(dossiers):,} read" + (f", {len(bad)} unreadable: {bad[:5]}" if bad else ""))

    # ---- windows: final compiled/<window>.json where present, else the draft
    drafts = sorted((H / "compiled" / "_draft").glob("*.json"))
    windows = []
    for p in drafts:
        final = H / "compiled" / p.name
        src = final if final.exists() and not args.drafts else p
        windows.append((p.stem, src))
    def wkey(w):
        a = w[0].split("-")[0]
        return -int(a[1:]) if a[0] == "m" else int(a[1:])
    windows.sort(key=wkey)
    n_final = sum(1 for _, s in windows if s.parent.name == "compiled")
    log(f"windows: {len(windows)} ({n_final} final, {len(windows) - n_final} drafts)")

    # ---- the state table: every dossier, then every party named without one
    names_only = set()
    win_data = []
    for wid, src in windows:
        w = json.loads(src.read_text())
        win_data.append((wid, src, w))
        for yv in w.get("years", {}).values():
            for c in yv.get("changes", []):
                for k in ("from", "to", "suzerain", "occupier"):
                    v = c.get(k)
                    if v and v not in dossiers:
                        names_only.add(v)
                for v in c.get("claimants") or []:
                    if v and v not in dossiers:
                        names_only.add(v)
            for cap in yv.get("captions", []):
                if cap.get("slug") and cap["slug"] not in dossiers:
                    names_only.add(cap["slug"])
    anchors = {}
    def anchor(stem):
        if stem not in anchors:
            anchors[stem] = json.loads((H / "data" / "anchors-c" / f"{stem}.json").read_text())
        return anchors[stem]
    for _, _, w in win_data:
        for stem in (w["start_anchor"], w["end_anchor"]):
            a = anchor(stem)
            for s in a["owners"]:
                if s not in dossiers:
                    names_only.add(s)
            for grp in (a.get("status") or {}).values():
                for e in grp:
                    for k in ("owner", "suzerain", "occupier"):
                        v = e.get(k)
                        if v and v not in dossiers:
                            names_only.add(v)
                    for v in e.get("claimants") or []:
                        if v and v not in dossiers:
                            names_only.add(v)
    slugs = sorted(dossiers) + sorted(names_only)
    pid = {s: i + 1 for i, s in enumerate(slugs)}
    P = len(slugs)
    assert P < 65535
    log(f"states: {len(dossiers):,} dossiers + {len(names_only)} parties named without one")

    def party(v):
        return pid.get(v, 0) if v else 0

    # ---- replay every window from its start anchor; write the chunks
    years_all = LAST - FIRST + 1
    changed = np.zeros(years_all, np.int64)
    area_series = {}               # pid -> list of [year, cells]
    last_area = np.zeros(P + 1, np.int64)
    first_land = np.full(P + 1, 99999, np.int64); last_land = np.full(P + 1, -99999, np.int64)
    peak = np.zeros(P + 1, np.int64); peak_year = np.zeros(P + 1, np.int64)
    seam_issues = []
    win_index = []
    caption_total = 0
    total_bytes = 0
    if not args.check:
        (OUT / "w").mkdir(parents=True, exist_ok=True)

    def state_from_anchor(a):
        owner = np.zeros(N, np.uint16); status = np.zeros(N, np.uint8); other = np.zeros(N, np.uint16)
        for s, runs in a["owners"].items():
            owner[runs_to_idx(runs)] = pid[s]
        for kind, grp in (a.get("status") or {}).items():
            code = STATUS.get(kind)
            if code is None:
                continue
            for e in grp:
                idx = runs_to_idx(e["cells"])
                status[idx] = code
                if kind in ("vassal", "constituent"):
                    other[idx] = party(e.get("suzerain"))
                elif kind == "occupied":
                    other[idx] = party(e.get("occupier"))
                    if not e.get("owner"):
                        owner[idx] = 0
                elif kind == "contested":
                    cl = [c for c in (e.get("claimants") or []) if c and c != e.get("owner")]
                    other[idx] = party(cl[0]) if cl else 0
        return owner, status, other

    def record_area(year, owner):
        cnt = np.bincount(owner, minlength=P + 1)
        diff = np.nonzero(cnt != last_area)[0]
        for p_ in diff:
            if p_ == 0:
                continue
            area_series.setdefault(int(p_), []).append([year, int(cnt[p_])])
        last_area[:] = cnt
        alive = cnt > 0
        first_land[alive] = np.minimum(first_land[alive], year)
        last_land[alive] = np.maximum(last_land[alive], year)
        up = cnt > peak
        peak[up] = cnt[up]; peak_year[up] = year

    for wi, (wid, src, w) in enumerate(win_data):
        wfrom, wto = int(w["from"]), int(w["to"])
        a0 = anchor(w["start_anchor"])
        owner, status, other = state_from_anchor(a0)
        start = (owner.copy(), status.copy(), other.copy())
        if wi == 0:
            record_area(wfrom - 1, owner)
        g_year, g_owner, g_status, g_other, g_runs, r_start, r_len = [], [], [], [], [], [], []
        captions = []
        years = sorted(int(y) for y in w.get("years", {}))
        for y in range(wfrom, min(wto, LAST) + 1):
            yv = w.get("years", {}).get(str(y))
            if not yv:
                if FIRST <= y <= LAST and y > wfrom - 1:
                    pass
                continue
            before = (owner.copy(), status.copy(), other.copy()) if True else None
            groups = {}
            for c in yv.get("changes", []):
                idx = runs_to_idx(c.get("cells"))
                if len(idx) == 0:
                    continue
                st = c.get("status", "direct")
                code = STATUS.get(st, 0)
                to = party(c.get("to")) if st != "neutral" else 0
                if st in ("vassal", "constituent"):
                    oth = party(c.get("suzerain"))
                elif st == "occupied":
                    oth = party(c.get("occupier"))
                elif st == "contested":
                    cl = [x for x in (c.get("claimants") or []) if x and x != c.get("to")]
                    oth = party(cl[0]) if cl else 0
                else:
                    oth = 0
                owner[idx] = to; status[idx] = code; other[idx] = oth
                groups.setdefault((to, code, oth), []).append(idx)
            # one group per (owner, status, other), cells sorted into runs; a later change in the same year wins,
            # so the groups are rebuilt from the final state of the cells this year touched
            touched = np.unique(np.concatenate([np.concatenate(v) for v in groups.values()])) if groups else np.zeros(0, np.int64)
            if len(touched):
                key = (owner[touched].astype(np.int64) << 24) | (status[touched].astype(np.int64) << 16) | other[touched].astype(np.int64)
                order = np.argsort(key, kind="stable")
                ks = key[order]; ts = touched[order]
                cut = np.nonzero(np.diff(ks))[0] + 1
                for part_k, part_c in zip(np.split(ks, cut), np.split(ts, cut)):
                    k = int(part_k[0])
                    s_, l_ = idx_to_runs(part_c)
                    g_year.append(y); g_owner.append(k >> 24); g_status.append((k >> 16) & 0xFF); g_other.append(k & 0xFFFF)
                    g_runs.append(len(s_)); r_start.extend(s_.tolist()); r_len.extend(l_.tolist())
                diffmask = (before[0][touched] != owner[touched]) | (before[1][touched] != status[touched]) | (before[2][touched] != other[touched])
                if FIRST <= y <= LAST:
                    changed[y - FIRST] += int(diffmask.sum())
            for cap in yv.get("captions", []):
                # keyframe notes describe how a shape was drawn, not an event: the dock leaves them out
                if cap.get("type") == "keyframe":
                    continue
                text, workings = public_text(first_sentence(cap.get("text", "")))
                if not text or workings:
                    continue
                c_ = {"y": int(cap.get("year", y)), "s": party(cap.get("slug")), "t": cap.get("type", ""), "x": text}
                if cap.get("month"):
                    c_["m"] = int(cap["month"])
                if cap.get("source"):
                    c_["u"] = cap["source"]
                captions.append(c_)
            record_area(y, owner)
        # seam check: the window must end at its end anchor
        a1 = anchor(w["end_anchor"])
        e_owner, e_status, e_other = state_from_anchor(a1)
        bad_cells = int(np.count_nonzero((e_owner != owner) | (e_status != status) | (e_other != other)))
        if bad_cells:
            seam_issues.append(f"{wid}: {bad_cells:,} cells differ from {w['end_anchor']}")
        caption_total += len(captions)

        if not args.check:
            arr = {
                "owner": start[0], "status": start[1], "other": start[2],
                "g_year": np.asarray(g_year, np.int32), "g_owner": np.asarray(g_owner, np.uint16),
                "g_status": np.asarray(g_status, np.uint8), "g_other": np.asarray(g_other, np.uint16),
                "g_runs": np.asarray(g_runs, np.uint32),
                "r_start": np.diff(np.asarray(r_start, np.int64), prepend=0).astype(np.int32).view(np.uint32),
                "r_len": np.asarray(r_len, np.uint32),
            }
            header = {"window": wid, "from": wfrom, "to": min(wto, LAST), "N": N, "G": len(g_year), "R": len(r_start),
                      "years": sorted({int(y) for y in g_year}), "captions": captions, "sections": {}}
            body = b""
            # offsets are relative to the start of the binary part (after the header)
            for name, a in arr.items():
                header["sections"][name] = [len(body), a.nbytes]
                body += a.tobytes()
                body += b"\0" * ((-len(body)) % 4)
            hj = json.dumps(header, ensure_ascii=False, separators=(",", ":")).encode()
            hj += b" " * ((-len(hj)) % 4)
            blob = b"CHW1" + np.array([len(hj)], np.uint32).tobytes() + hj + body
            size = write_gz(OUT / "w" / f"{wid}.bin", blob)
            total_bytes += size
            win_index.append({"id": wid, "from": wfrom, "to": min(wto, LAST), "kb": round(size / 1024),
                              "src": "final" if src.parent.name == "compiled" else "draft"})
        if wi % 10 == 0 or wi == len(win_data) - 1:
            log(f"  {wid}: {len(g_year)} groups, {len(r_start):,} runs, {len(captions)} captions"
                + (f", {win_index[-1]['kb']} KB" if win_index else ""))
    log(f"replay: {caption_total:,} captions; seams: {'clean' if not seam_issues else '; '.join(seam_issues[:8])}")

    # ---- the state table
    def yr(v):
        if isinstance(v, dict):
            return v.get("year")
        return v

    cols = {k: [] for k in ("slug", "name", "type", "start", "end", "colour", "fb", "first", "last", "peak", "peakYear",
                            "capitals", "alt", "wiki")}
    fb_count = 0
    for s in slugs:
        i = pid[s]
        d = dossiers.get(s)
        idn = (d or {}).get("identity", {})
        col = colour.get(s)
        fb = 0
        if not col:
            col = fallback_colour(s, wheel); fb = 1; fb_count += 1 if d else 0
        cols["slug"].append(s if d else "")
        cols["name"].append(idn.get("name") or pretty_name(s))
        cols["type"].append(TYPE_CODE.get(idn.get("type"), "s") if d else "n")
        cols["start"].append(yr(idn.get("start")))
        cols["end"].append(yr(idn.get("end")))
        cols["colour"].append(col)
        cols["fb"].append(fb)
        has = first_land[i] < 99999
        cols["first"].append(int(first_land[i]) if has else None)
        cols["last"].append(int(last_land[i]) if has else None)
        cols["peak"].append(int(peak[i]))
        cols["peakYear"].append(int(peak_year[i]) if has else None)
        caps = []
        for c in idn.get("capitals") or []:
            try:
                caps.append([c["name"], round(float(c["lon"]), 3), round(float(c["lat"]), 3), int(c["from"]), int(c["to"])])
            except (KeyError, TypeError, ValueError):
                pass
        cols["capitals"].append(caps)
        alt = []
        for k in ("alt_names", "native_names", "cliopatria_names"):
            for a in idn.get(k) or []:
                if a and a != cols["name"][-1] and a not in alt:
                    alt.append(a)
        cols["alt"].append(alt)
        cols["wiki"].append(idn.get("wikipedia") or "")
    built = time.strftime("%Y-%m-%d")
    states = {"built": built, "count": P, "neutral": neutral, "cellKm2": CELL_KM2, **cols}
    log(f"colours: {sum(1 for s in dossiers if s in colour):,} dossiers coloured by the registry, {fb_count:,} on the fallback wheel")

    # ---- per-state files
    def ledger_rows(d):
        rows = []
        for e in d.get("ledger") or []:
            note = e.get("note") or ""
            r = {"y": e.get("year"), "t": e.get("type", ""), "x": public_text(first_sentence(note) or (e.get("region") or {}).get("text", "") or "")[0]}
            if e.get("month"):
                r["m"] = e["month"]
            cp = e.get("counterpart")
            if cp and cp != "nobody":
                r["cp"] = cp
                if cp in pid and cp in dossiers:
                    r["cpn"] = cols["name"][pid[cp] - 1]
            if e.get("source"):
                r["u"] = e["source"]
            if e.get("confidence") is not None:
                r["c"] = e["confidence"]
            rows.append(r)
        rows.sort(key=lambda r: (r["y"] if isinstance(r["y"], int) else 0, r.get("m", 0)))
        return rows

    def handovers(lst):
        out = []
        for h in lst or []:
            s = h.get("slug")
            if not s:
                continue
            land = h.get("land") or {}
            out.append({"slug": s if s in dossiers else "", "name": cols["name"][pid[s] - 1] if s in pid else pretty_name(s),
                        "year": land.get("year"), "text": first_sentence(land.get("text", ""), 200)})
        return out

    state_bytes = 0
    if not args.check:
        sdir = OUT / "state"
        sdir.mkdir(parents=True, exist_ok=True)
        keep = set()
        for s, d in dossiers.items():
            i = pid[s]
            idn = d.get("identity", {})
            obj = {
                "slug": s, "name": idn.get("name") or s, "native": idn.get("native_names") or [], "alt": idn.get("alt_names") or [],
                "type": idn.get("type"), "family": idn.get("family"), "start": idn.get("start"), "end": idn.get("end"),
                "wikipedia": idn.get("wikipedia"), "wikidata": idn.get("wikidata"), "colour": cols["colour"][i - 1],
                "fb": cols["fb"][i - 1],
                "first": cols["first"][i - 1], "last": cols["last"][i - 1], "peak": cols["peak"][i - 1], "peakYear": cols["peakYear"][i - 1],
                "predecessors": handovers(idn.get("predecessors")), "successors": handovers(idn.get("successors")),
                "capitals": [{"name": c[0], "lon": c[1], "lat": c[2], "from": c[3], "to": c[4]} for c in cols["capitals"][i - 1]],
                "rulers": [{"name": r.get("name"), "from": r.get("from"), "to": r.get("to"), **({"title": r["title"]} if r.get("title") else {})}
                           for r in idn.get("rulers") or []],
                "area": area_series.get(i, []),
                "ledger": ledger_rows(d),
                "wars": [{"name": w.get("name"), "from": w.get("from"), "to": w.get("to"),
                          "outcome": first_sentence(w.get("outcome", ""), 260), "u": w.get("source")} for w in d.get("wars") or []],
                "certainty": [{"from": c.get("from"), "to": c.get("to"), "level": c.get("level"), "note": first_sentence(c.get("note", ""), 240)}
                              for c in d.get("certainty") or []],
                "sources": [{"url": x.get("url"), "title": x.get("title")} for x in d.get("sources") or [] if x.get("url")],
            }
            state_bytes += write_json(sdir / f"{s}.json", obj)
            keep.add(f"{s}.json")
        stale = [p for p in sdir.glob("*.json") if p.name not in keep]
        for p in stale:
            p.unlink()
        log(f"state/: {len(keep):,} files, {state_bytes / 1e6:.1f} MB" + (f", {len(stale)} stale removed" if stale else ""))

        st_bytes = write_json(OUT / "states.json", states)
        log(f"states.json: {st_bytes / 1e6:.2f} MB")
        # drop chunks of windows that no longer exist
        ids = {w["id"] for w in win_index}
        for p in (OUT / "w").glob("*.bin"):
            if p.stem not in ids:
                p.unlink()
        index = {
            "built": built, "grid_sha": grid_sha, "N": N, "Q": Q, "first": FIRST, "last": LAST, "P": P,
            "cellKm2": CELL_KM2, "windows": win_index,
            # cells whose owner or status changed, per year from FIRST
            "changed": [int(v) for v in changed],
            "seams": seam_issues,
            "source": {"project": "history/ (Historical borders)", "windows_final": n_final, "windows_draft": len(windows) - n_final,
                       "dossiers": len(dossiers), "fallback_colours": fb_count},
        }
        write_json(OUT / "index.json", index)
        total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
        biggest = max((p for p in OUT.rglob("*") if p.is_file()), key=lambda p: p.stat().st_size)
        log(f"chunks: {total_bytes / 1e6:.1f} MB in {len(win_index)} files; public/history: {total / 1e6:.1f} MB in all, "
            f"largest {biggest.relative_to(OUT)} {biggest.stat().st_size / 1e6:.2f} MB")
    log(f"done in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
