#!/usr/bin/env python3
"""Phase C compiler: every reviewed dossier, every year, one deterministic run.

    python3 -I tools/compile_dossiers.py                 full run: sync dossiers, resolve regions,
                                                         compile -6000..2026, write anchors-c, the
                                                         window drafts and the reports, self-check,
                                                         publish to the shared folder
    python3 -I tools/compile_dossiers.py --until 1900    compile to 1900 only and compare the Phase C
                                                         anchors at --compare years with Phase A; writes
                                                         nothing to the shared folder (scratch only)
    python3 -I tools/compile_dossiers.py --stage-only    full run, outputs left in scratch (stage/)
    python3 -I tools/compile_dossiers.py --build-colonies
                                                         full run that first derives data/colonies.csv
                                                         again (rows marked manual are kept)
    options: --no-sync (use the scratch copy of the dossiers as it is), --workers N (region
             resolution processes, default 4), --refresh (drop the region cache),
             --compare 1600,1900 (Phase A comparison years), --no-rules (size rule only, no R1/R2/R3)

Run from any directory (a scratch directory is best); inputs come from the shared folder
history/ (polities/, data/gazetteer/, data/grid/, data/shapes.csv, data/polities.csv, the
Cliopatria feature cache of tools/grid.py) and scratch lives in /tmp/claude-0/work/compile-c/.

What it does (history/briefs/window-brief.md section 3, applied once to every year instead of
once per window; the readings taken where the brief is silent are listed in
notes/phase-c/README.md and repeated here briefly):

  * Starts from an empty world (every cell nobody's) in the earliest dossier year and walks
    every year to 2026. In each year it applies, in (month, ledger order) order, every ledger
    event of every dossier dated that year (births first within a month; an *_end of one dossier
    before an *_start of another of the same month, or where either month is unknown), then the
    keyframe snaps of that year, then the deaths (identity.end.year of dossiers with a dissolve
    event; a dossier without one is alive through 2026).
  * Regions are resolved through tools/gazetteer.py: every leaf spec (country, admin1, place,
    region, cliopatria, river, lake, polygon, border_band, lon/lat) once, cached under
    /tmp/claude-0/work/compile-c/cache/ (invalidated per leaf when a gazetteer table it depends on
    changes); union / intersect / minus are composed here exactly as the gazetteer composes them.
    An event whose region does not resolve is skipped and reported, never guessed. An event whose
    region resolves to no land cell moves no land: a gain, loss, split, merge, contest_start or
    occupation_start over it is skipped and logged in skipped_events.csv (an *_end too when nothing
    is open), not reported as unresolved. Names the gazetteer documents as having no land cell
    (LANDLESS_NAMES: the Hawar and Swan Islands, Janan, Fasht ad Dibal, Antarctic claims) are read
    as no land while the gazetteer does not know them.
  * found: the region (else the first keyframe's corrected shape) goes to the new state; cells
    held by nobody, a predecessor or the counterpart move outright, cells of any other state are
    a conflict. gain: region cells the counterpart holds (nobody's land when the counterpart is
    nobody, has no dossier or holds none of the region). loss: the mirror, skipped when the
    counterpart's dossier carries the matching gain in the same year. split / merge: like
    collapse with their region (merge direction from who ends that year, else who holds the
    region; a merge whose counterpart has no living dossier that year is a gain from nobody, logged
    in skipped_events.csv with the branch that applied). vassal_start / occupation_start /
    contest_start: status over the region (roles of a
    reciprocal entry worked out from who holds the region); the matching *_end closes the whole
    relation (a vassal still under another open suzerainty takes that tint again). A dossier vassal
    keeps the tint on land it gains later. dissolve: at year end the remaining cells go to
    identity.successors (land intersected with the state's cells), the rest to nobody; relations the
    state was party to close.
  * Keyframes: in a keyframe's from year (or the birth year when it starts earlier), after the
    ledger, the union of the state's keyframes alive that year (corrected shape for adjust and
    wrong, the Cliopatria shape for ok) is compared with the state's cells; when setting the state
    to the keyframe would move more than 20 cells or more than 5 percent of the state, it is set:
    missing cells are taken (conflict rule), its direct cells outside the keyframe go to nobody.
    Snaps are reported as dossier gaps.
  * Conflicts: when a found or a keyframe claims a cell another state holds and no event of that
    year settled the cell, the first of these decides: R2, a successor (A.successors or
    B.predecessors) wins from its start year on (R2_BORN_AFTER, off: only a successor born after its
    predecessor); a ruling of data/patches/<window>.json for the pair,
    year (and cells, when it has a region) names the winner; R3, data/hierarchy.csv: a same_state row draws the
    parent, a constituent or vassal row gives the cell to the deepest child (status constituent or
    vassal, suzerain its immediate parent); rule 4, an open vassal of the other keeps its land;
    R1, of two colonies of the same metropole the smaller wins, and a colony with a metropole that
    year wins against any other dossier; otherwise the state with the smaller Cliopatria area that
    year wins (compiled area when it has no Cliopatria shape that year). Every pair is logged with the
    rule that settled it.
  * Colonies (R1): data/colonies.csv gives each type-colony dossier its metropole by years (derived
    by --build-colonies, or when the file is missing; see derive_colonies). Every colony cell is drawn
    in the vassal tint of its metropole (a vassal relation flagged "colony", below any suzerainty the
    ledger records), with or without a conflict.
  * Hierarchy (R3): rows of data/hierarchy.csv with confidence 2-3 tint the child's cells the same
    way (status vassal or constituent, a relation flagged "hierarchy"), for years without a
    colonies.csv row. Dossiers that fail tools/validate_dossier.py are left out (and listed).
  * Patches: data/patches/<window>.json (data/patches/README.md), the window agents' corrections:
    extra ledger events and keyframe_review overrides go into the dossiers in memory, rulings into the
    conflict rule. Each entry is checked as the validator checks a dossier (regions through the
    gazetteer); a bad entry is reported in notes/phase-c/patches_check.csv and skipped.
    --patches DIR reads another folder.
  * Outputs: data/anchors-c/<stem>.json at every window start (1 January of the year) plus p2030
    (end of the last window) and p2026 (the final snapshot, end of 2026); compiled/_draft/<window>.json
    in window-brief section 2 format; notes/phase-c/ reports. Self-check: replaying the drafts
    from the first anchor reaches every later anchor cell for cell (owner, status, suzerain /
    occupier / claimant), no cell has two owners, and the *_end events that close nothing are counted.
"""
import argparse
import csv
import io
import json
import os
import pickle
import re
import shutil
import sys
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import numpy as np

DEFAULT_HIST = Path("/mnt/project-files/history")
WORK = Path("/tmp/claude-0/work/compile-c")
# Cache folders (leaves.pkl, valid.pkl, edges_r5.npz): read from the first that has the file (a trial's own
# folder over the shared one), written to CACHE_WRITE only (None: nowhere). Files are replaced atomically
# through a per-process temporary name, so runs at the same time cannot corrupt one another's caches.
CACHE_READ = [WORK / "cache"]
CACHE_WRITE = WORK / "cache"
GRID_READONLY = False        # a trial reads tools/grid.py's per-shape cell cache but never writes it

FIRST_YEAR = -6000
LAST_YEAR = 2026
CENTURY_STARTS = list(range(-6000, 1600, 100))        # 76 windows, -6000..1599
DECADE_STARTS = list(range(1600, 2030, 10))           # 43 windows, 1600..2029
SNAP_CELLS = 20
# R2 switch (round 12, left off): True gives R2 only to a successor born after its predecessor (a same-year or
# older "successor" then goes on to rulings, R3, rule 4, R1 and the size rule). Tried on 2 Nov 2026: it moved
# 1.27M owner cell-years in 86 windows that the Phase D windows had reviewed and patched under the rule as it
# is; the pairs that lose R2 and where their claims go: /tmp/claude-0/work/r12/r2_moves.json (owner
# cell-years by window and pair: diff_a.json beside it). Kept for a review after launch.
R2_BORN_AFTER = False
# round 12: a merge whose counterpart has no living dossier that year (do_event)
MERGE_NO_CP = "merge whose counterpart has no living dossier that year"
MERGE_NO_CP_GAIN = MERGE_NO_CP + ": applied as a gain from nobody"
MERGE_NO_CP_NONE = MERGE_NO_CP + ": nothing moved (the region holds none of nobody's cells)"
SNAP_SHARE = 0.05
CELL_KM2 = 252.9

DIRECT, VASSAL, OCCUPIED, CONTESTED, CONSTITUENT = 0, 1, 2, 3, 4
STATUS_LABEL = {VASSAL: "vassal", OCCUPIED: "occupied", CONTESTED: "contested", CONSTITUENT: "constituent"}
TINTS = (VASSAL, CONSTITUENT)    # statuses drawn in a suzerain's tint

COMPOSITE = ("union", "intersect", "minus")
IGNORED_KEYS = ("text", "note", "confidence")


def log(msg):
    print(time.strftime("%H:%M:%S ") + msg, file=sys.stderr, flush=True)


# ----------------------------------------------------------------------------
# small helpers
# ----------------------------------------------------------------------------

def stem(year):
    return ("m%04d" % -year) if year < 0 else ("p%04d" % year)


def windows():
    out = []
    for s in CENTURY_STARTS:
        out.append((s, s + 99))
    for s in DECADE_STARTS:
        out.append((s, s + 9))
    return [{"id": "%s-%s" % (stem(a), stem(b)), "from": a, "to": b,
             "start_anchor": stem(a), "end_anchor": stem(b + 1)} for a, b in out]


def to_runs(idx):
    """Sorted unique int array -> ["a-b", c, ...]."""
    idx = np.asarray(idx, dtype=np.int64)
    if idx.size == 0:
        return []
    br = np.flatnonzero(np.diff(idx) != 1) + 1
    starts = np.concatenate(([0], br))
    ends = np.concatenate((br, [idx.size])) - 1
    return [int(a) if a == b else "%d-%d" % (a, b) for a, b in zip(idx[starts].tolist(), idx[ends].tolist())]


def from_runs(runs):
    parts = []
    for r in runs:
        if isinstance(r, str):
            a, b = r.split("-")
            parts.append(np.arange(int(a), int(b) + 1, dtype=np.int64))
        else:
            parts.append(np.array([int(r)], dtype=np.int64))
    return np.concatenate(parts) if parts else np.zeros(0, dtype=np.int64)


def canon(spec):
    if isinstance(spec, dict):
        return {k: canon(v) for k, v in sorted(spec.items()) if k not in IGNORED_KEYS}
    if isinstance(spec, list):
        return [canon(v) for v in spec]
    return spec


def spec_key(spec):
    return json.dumps(canon(spec), sort_keys=True, ensure_ascii=False)


_SENT = re.compile(r"(.+?[.!?])(?:['\"’”)]?)(?=\s+\S|\s*$)", re.S)


def first_sentence(note):
    if not note:
        return ""
    note = note.strip()
    pos = 0
    while True:
        m = _SENT.match(note, pos)
        if not m:
            return note[:300]
        end = m.end()
        cand = note[:end].strip()
        last = cand.rstrip(".!?'\"’”)").split()[-1:] if cand else []
        # do not stop at "c.", "St.", "Mt.", initials and the like
        if last and (len(last[0]) <= 2 or last[0].lower() in ("ca", "st", "mt", "gen", "col", "lt", "capt", "sgt")) \
                and end < len(note) and len(cand) < 240:
            pos = end
            continue
        return cand[:400]


def write_cache_file(name, dump):
    """Write a cache file into CACHE_WRITE (nothing when it is None) through a temporary name of this process."""
    if CACHE_WRITE is None:
        return
    CACHE_WRITE.mkdir(parents=True, exist_ok=True)
    path = CACHE_WRITE / name
    tmp = path.with_name("%s.tmp%d" % (path.name, os.getpid()))
    with open(tmp, "wb") as f:
        dump(f)
    os.replace(tmp, path)


def write_json(path, obj, compact=True):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        if compact:
            json.dump(obj, f, separators=(",", ":"), ensure_ascii=False)
        else:
            json.dump(obj, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    os.replace(tmp, path)


# ----------------------------------------------------------------------------
# inputs
# ----------------------------------------------------------------------------

def sync_dossiers(src, dst):
    """Copy new or changed dossier files from the mount to scratch; drop removed ones."""
    dst.mkdir(parents=True, exist_ok=True)
    seen, copied = set(), 0
    for e in os.scandir(src):
        if not e.name.endswith(".json") or not e.is_file():
            continue
        seen.add(e.name)
        st = e.stat()
        d = dst / e.name
        try:
            ds = d.stat()
            same = ds.st_size == st.st_size and int(ds.st_mtime) == int(st.st_mtime)
        except FileNotFoundError:
            same = False
        if not same:
            shutil.copy2(e.path, d)
            copied += 1
    removed = 0
    for d in dst.glob("*.json"):
        if d.name not in seen:
            d.unlink()
            removed += 1
    return len(seen), copied, removed


def validation_errors(hist, dossier_dir):
    """tools/validate_dossier.py over the scratch copies (schema and semantic errors; warnings ignored)
    -> {file stem: first errors}. Results are cached per file (size, mtime) and per validator/schema."""
    import validate_dossier as V
    key = []
    for p in (hist / "tools" / "validate_dossier.py", Path(V.SCHEMA_PATH)):
        st = p.stat()
        key.append((p.name, st.st_size, int(st.st_mtime)))
    cache = {}
    for d in reversed(CACHE_READ):            # the shared cache first, a trial's own over it
        path = d / "valid.pkl"
        if path.exists():
            with open(path, "rb") as f:
                got = pickle.load(f)
            if got.get("key") == key:
                cache.update(got["files"])
    schema = shapes = known = None
    out, files, n_new = {}, {}, 0
    for p in sorted(dossier_dir.glob("*.json")):
        if p.name.startswith("_"):
            continue
        st = p.stat()
        sig = (st.st_size, st.st_mtime_ns)
        have = cache.get(p.name)
        if have is not None and have[0] == sig:
            errs = have[1]
        else:
            if schema is None:
                with open(V.SCHEMA_PATH, encoding="utf-8") as f:
                    schema = json.load(f)
                shapes, known = V.load_shapes(), V.load_known_slugs()
            try:
                with open(p, encoding="utf-8") as f:
                    doc = json.load(f)
                e1 = V.schema_errors(doc, schema)
                e2, _w, _r = V.semantic_checks(doc, str(p), shapes, known, False)
                errs = ["%s: %s" % (a or "/", b) for a, b in (list(e1) + list(e2))][:3]
            except Exception as e:  # noqa: BLE001
                errs = ["%s: %s" % (type(e).__name__, e)]
            n_new += 1
        files[p.name] = (sig, errs)
        if errs:
            out[p.stem] = errs
    write_cache_file("valid.pkl", lambda f: pickle.dump({"key": key, "files": files}, f))
    log("validation: %d dossiers checked (%d new or changed), %d fail" % (len(files), n_new, len(out)))
    return out


class Inputs:
    def __init__(self, hist, dossier_dir):
        self.hist = hist
        t = time.time()
        with open(hist / "data" / "grid" / "land_r5.txt") as f:
            self.land = [line.strip() for line in f if line.strip()]
        self.n = len(self.land)
        # Cliopatria: names -> slugs (polities.csv keeps the -2 collision suffixes), shapes
        self.name2clio = {}
        with open(hist / "data" / "polities.csv", newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                self.name2clio[r["name"]] = r["slug"]
        self.shapes = {}
        with open(hist / "data" / "shapes.csv", newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                self.shapes[r["shape_id"]] = (int(r["from_year"]), int(r["to_year"]), float(r["area_km2"]))
        import grid
        self.grid = grid
        self.feats = grid.load_features()
        cnt = Counter()
        self.shape_feat = {}
        self.clio_feats = defaultdict(list)   # clio slug -> [(from, to, area)]
        for ft in self.feats:
            s = self.name2clio.get(ft["name"], ft["slug"])
            k = (s, ft["from"])
            cnt[k] += 1
            suf = "" if cnt[k] == 1 else chr(ord("a") + cnt[k] - 1)
            self.shape_feat[s + "_" + str(ft["from"]) + suf] = ft
            if not ft["umbrella"]:
                self.clio_feats[s].append((ft["from"], ft["to"], ft["area"]))
        self.land_sorted, self.land_order = grid.land_cells_int()
        self._feat_cells = {}
        # dossiers
        self.dossiers = {}
        self.invalid = []
        failing = validation_errors(hist, dossier_dir)
        for p in sorted(dossier_dir.glob("*.json")):
            if p.name.startswith("_"):
                continue
            if p.stem in failing:
                # compile only what validates (a dossier still being written, a gap dossier with errors)
                self.invalid.append((p.stem, "tools/validate_dossier.py: " + "; ".join(failing[p.stem])))
                continue
            try:
                with open(p, encoding="utf-8") as f:
                    d = json.load(f)
                slug = d["identity"]["slug"]
                if slug != p.stem:
                    self.invalid.append((p.stem, "identity.slug %r differs from the file name" % slug))
                d["identity"]["start"]["year"] = int(d["identity"]["start"]["year"])
                d["identity"]["end"]["year"] = int(d["identity"]["end"]["year"])
                self.dossiers[slug] = d
            except Exception as e:  # noqa: BLE001
                self.invalid.append((p.stem, "%s: %s" % (type(e).__name__, e)))
        log("inputs: %d land cells, %d shapes, %d dossiers (%d unreadable), %.1f s" % (
            self.n, len(self.shapes), len(self.dossiers), len(self.invalid), time.time() - t))

    def feature_cells(self, ft):
        i = ft["i"]
        if i not in self._feat_cells:
            cp = self.grid.CELLS_DIR / ("%05d.npy" % i)
            if not GRID_READONLY:
                arr = self.grid.feature_cells_int(ft)
            elif cp.exists():
                arr = np.load(cp)
            else:                     # a trial computes a missing shape without writing grid.py's cache
                import h3
                cells = self.grid.shape_cells(self.grid.feature_geometry(ft))
                arr = np.sort(np.fromiter((h3.str_to_int(c) for c in cells), dtype=np.uint64, count=len(cells)))
            pos = np.searchsorted(self.land_sorted, arr)
            pos[pos >= self.n] = 0
            hit = self.land_sorted[pos] == arr
            self._feat_cells[i] = np.sort(self.land_order[pos[hit]].astype(np.int32))
        return self._feat_cells[i]


# ----------------------------------------------------------------------------
# region resolution through the gazetteer, leaf by leaf, cached
# ----------------------------------------------------------------------------

LEAF_DEPS = {
    "region": None,  # any table
    "admin1": ["admin1.jsonl", "countries.jsonl"],
    "place": ["places.jsonl", "countries.jsonl"],
    "country": ["countries.jsonl"],
    "lon": [], "cliopatria": ["@features"], "polygon": [], "border_band": ["@features", "@anchors"],
    "river": ["rivers.jsonl"], "lake": ["lakes.jsonl"],
}
_G = None

# Names the gazetteer cannot give a land cell (data/gazetteer/README.md, "Known gaps": islands and shoals
# smaller than a cell, Antarctica, which the land grid leaves out). A leaf naming one, while the gazetteer
# does not know it, is read as no land rather than as an unresolved name.
LANDLESS_NAMES = {"hawar islands", "fasht ad dibal", "janan island", "swan islands",
                  "australian antarctic territory", "ross dependency"}
LANDLESS_RE = re.compile(r"antarctic", re.I)


def landless_leaf(leaf):
    for k in ("region", "place", "admin1", "country"):
        v = leaf.get(k) if isinstance(leaf, dict) else None
        if isinstance(v, str):
            name = re.sub(r"\s*\([^)]*\)\s*$", "", v).strip().lower()
            return name in LANDLESS_NAMES or bool(LANDLESS_RE.search(v))
    return False


def _leaf_kind(leaf):
    for k in ("region", "admin1", "place", "country", "lon", "cliopatria", "polygon", "border_band", "river", "lake"):
        if k in leaf:
            return k
    return "other"


def _worker_init(tools_dir):
    global _G
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    from gazetteer import Gazetteer
    _G = Gazetteer()


def _worker_resolve(key):
    try:
        cells = _G.resolve(json.loads(key))
        return key, np.fromiter(sorted(cells), dtype=np.int32, count=len(cells)), None
    except Exception as e:  # noqa: BLE001  (GazetteerError and malformed specs alike)
        msg = str(e) if type(e).__name__ == "GazetteerError" else "%s: %s" % (type(e).__name__, e)
        return key, None, msg


class Resolver:
    def __init__(self, hist, workers=4, refresh=False):
        self.hist = hist
        self.workers = workers
        self.fp = self._fingerprints()
        self.leaves = {}   # key -> (deps_fp, cells or None, error or None)
        self.own = set()   # leaves of the cache folder written to (or resolved by this run)
        if not refresh:
            for d in reversed(CACHE_READ):    # the shared cache first, a trial's own over it
                path = d / "leaves.pkl"
                if path.exists():
                    with open(path, "rb") as f:
                        got = pickle.load(f)
                    self.leaves.update(got)
                    if d == CACHE_WRITE:
                        self.own.update(got)
        self.memo = {}
        self.landless = set()   # leaf keys read as no land (LANDLESS_NAMES)

    def _fingerprints(self):
        gz = self.hist / "data" / "gazetteer"
        fp = {}
        for p in sorted(gz.glob("*.jsonl")):
            st = p.stat()
            fp[p.name] = (st.st_size, int(st.st_mtime))
        for name, p in (("@gazetteer.py", self.hist / "tools" / "gazetteer.py"),
                        ("@grid.py", self.hist / "tools" / "grid.py"),
                        ("@land", self.hist / "data" / "grid" / "land_r5.txt"),
                        ("@features", Path("/tmp/claude-0/work/grid/features.pkl"))):
            try:
                st = p.stat()
                fp[name] = (st.st_size, int(st.st_mtime))
            except FileNotFoundError:
                fp[name] = None
        anchors = sorted((self.hist / "data" / "anchors").glob("*.json"))
        fp["@anchors"] = (len(anchors), max((int(p.stat().st_mtime) for p in anchors[-3:]), default=0))
        return fp

    def _deps_fp(self, key):
        kind = _leaf_kind(json.loads(key))
        deps = LEAF_DEPS.get(kind)
        names = sorted(self.fp) if deps is None else sorted(set(deps) | {"@gazetteer.py", "@grid.py", "@land"})
        return tuple((n, self.fp.get(n)) for n in names)

    def collect_leaves(self, spec, out):
        if isinstance(spec, dict):
            for op in COMPOSITE:
                if op in spec and isinstance(spec[op], list):
                    for s in spec[op]:
                        self.collect_leaves(s, out)
                    return
        out.add(spec_key(spec) if isinstance(spec, dict) else json.dumps(spec))

    def prepare(self, specs):
        """Resolve every leaf of the given specs that is not cached (or whose tables changed)."""
        want = set()
        for s in specs:
            self.collect_leaves(s, want)
        todo = []
        for k in sorted(want):
            have = self.leaves.get(k)
            if have is None or have[0] != self._deps_fp(k):
                todo.append(k)
        log("regions: %d specs, %d distinct leaves, %d to resolve" % (len(specs), len(want), len(todo)))
        if todo:
            t = time.time()
            tools_dir = str(self.hist / "tools")
            if self.workers > 1 and len(todo) > 50:
                import multiprocessing as mp
                ctx = mp.get_context("fork")
                with ctx.Pool(self.workers, initializer=_worker_init, initargs=(tools_dir,)) as pool:
                    for n, (k, cells, err) in enumerate(pool.imap_unordered(_worker_resolve, todo, chunksize=8)):
                        self.leaves[k] = (self._deps_fp(k), cells, err)
                        if (n + 1) % 2000 == 0:
                            log("  %d/%d leaves, %.0f s" % (n + 1, len(todo), time.time() - t))
            else:
                _worker_init(tools_dir)
                for k in todo:
                    k, cells, err = _worker_resolve(k)
                    self.leaves[k] = (self._deps_fp(k), cells, err)
            self.own.update(todo)
            # the shared cache holds every leaf; a trial's own folder only the leaves the shared one lacks
            out = self.leaves if CACHE_WRITE == WORK / "cache" else {k: self.leaves[k] for k in self.own}
            write_cache_file("leaves.pkl", lambda f: pickle.dump(out, f, protocol=pickle.HIGHEST_PROTOCOL))
            log("regions: resolved %d leaves in %.0f s" % (len(todo), time.time() - t))

    def resolve(self, spec):
        """-> (sorted int32 cells or None, [(leaf key, error)])"""
        if not isinstance(spec, dict):
            return None, [(json.dumps(spec), "a region spec is a JSON object")]
        k = spec_key(spec)
        if k in self.memo:
            return self.memo[k]
        res = self._resolve(spec)
        self.memo[k] = res
        return res

    def _resolve(self, spec):
        for op in COMPOSITE:
            if op in spec and isinstance(spec[op], list):
                parts = [self.resolve(s) for s in spec[op]]
                errs = [e for _, es in parts for e in es]
                if errs:
                    return None, errs
                arrs = [c for c, _ in parts]
                if not arrs:
                    return np.zeros(0, np.int32), []
                if op == "union":
                    out = np.unique(np.concatenate(arrs)).astype(np.int32)
                elif op == "intersect":
                    out = arrs[0]
                    for a in arrs[1:]:
                        out = np.intersect1d(out, a, assume_unique=True)
                else:
                    out = arrs[0]
                    for a in arrs[1:]:
                        out = np.setdiff1d(out, a, assume_unique=True)
                return out.astype(np.int32), []
        k = spec_key(spec)
        have = self.leaves.get(k)
        if have is None:
            return None, [(k, "leaf not resolved (internal: prepare() missed it)")]
        if have[2] is not None:
            if landless_leaf(json.loads(k)):
                self.landless.add(k)
                return np.zeros(0, np.int32), []
            return None, [(k, have[2])]
        return have[1], []


# ----------------------------------------------------------------------------
# the compiler
# ----------------------------------------------------------------------------

class Compiler:
    def __init__(self, inp, res, until=LAST_YEAR, stage=None, colonies=None, rules=True, light=False,
                 hierarchy=None, rulings=None):
        self.inp = inp
        self.res = res
        self.until = until
        self.stage = stage
        self.rules = rules           # R1 (colonies) and R2 (succession) in the conflict rule
        self.light = light           # no change records, captions or adjacency (the colonies.csv pass)
        self.n = inp.n
        D = inp.dossiers
        self.slugs = sorted(D)
        self.names = list(self.slugs)
        self.name_id = {s: i for i, s in enumerate(self.slugs)}
        self.N = len(self.slugs)
        self.dos = [D[s] for s in self.slugs]
        self.umbrella = np.array([d["identity"]["type"] == "umbrella" for d in self.dos])
        self.start = np.array([d["identity"]["start"]["year"] for d in self.dos])
        self.has_dissolve = np.array([any(e.get("type") == "dissolve" for e in d["ledger"]) for d in self.dos])
        self.end = np.array([d["identity"]["end"]["year"] if hd else LAST_YEAR
                             for d, hd in zip(self.dos, self.has_dissolve)])
        self.is_colony = np.array([d["identity"]["type"] == "colony" for d in self.dos])
        # R2: (B, A) when B is A's successor (A.successors or B.predecessors names B)
        self.succ = set()
        for a, d in enumerate(self.dos):
            for s in d["identity"].get("successors", []) or []:
                b = self.name_id.get(s.get("slug"))
                if b is not None and b != a:
                    self.succ.add((b, a))
            for p in d["identity"].get("predecessors", []) or []:
                b = self.name_id.get(p.get("slug"))
                if b is not None and b != a:
                    self.succ.add((a, b))
        # R1: colony id -> [(from, to, metropole id or -1, confidence)] from data/colonies.csv
        self.colony_rows = defaultdict(list)
        for slug, rows in (colonies or {}).items():
            c = self.name_id.get(slug)
            if c is None:
                continue
            for f, t, m, conf in rows:
                self.colony_rows[c].append((f, t, self.name_id.get(m, -1) if m else -1, conf))
        for c in self.colony_rows:
            self.colony_rows[c].sort()
        self.colony_rel = {}         # colony id -> its open metropole relation
        # R3: data/hierarchy.csv rows, already clipped to both lives and to the child's years without a
        # colonies.csv row: (child, parent, from, to, kind, confidence)
        self.hier_rows = []
        self.hier_up = defaultdict(list)      # child id -> its vassal / constituent row numbers
        self.hier_same = defaultdict(list)    # (child id, parent id) -> [(from, to)] of same_state rows
        self.hier_rel = {}                    # row number -> its relation id, once opened
        self.r3_hop = {}                      # (winner, loser, year) -> row of the winner's immediate parent
        for (c, p, f, t, kind, conf) in (hierarchy or []):
            ci, pi = self.name_id.get(c), self.name_id.get(p)
            if ci is None or pi is None or ci >= self.N or pi >= self.N or ci == pi:
                continue
            if kind == "same_state":
                self.hier_same[(ci, pi)].append((f, t))
                continue
            self.hier_up[ci].append(len(self.hier_rows))
            self.hier_rows.append((ci, pi, f, t, kind, conf))
        # rulings of data/patches/<window>.json: settle a pair's conflicts for some years (after R2, before R3)
        self.rulings = []
        for R in (rulings or []):
            ia, ib, iw = (self.name_id.get(R[k]) for k in ("a", "b", "winner"))
            if ia is None or ib is None or iw is None:
                continue
            R = dict(R)
            R.update(a_id=ia, b_id=ib, winner_id=iw, extra_id=self.name_id.get(R.get("suzerain"), -1),
                     st=RULING_STATUS.get(R.get("status")), idx=len(self.rulings))
            self.rulings.append(R)
        self.ruling_by_id = {R["id"]: R["idx"] for R in self.rulings}
        self.rulings_by_pair = defaultdict(list)   # (low id, high id) -> rulings, those with a region first
        for R in sorted(self.rulings, key=lambda R: (R["cells"] is None, R["idx"])):
            self.rulings_by_pair[(min(R["a_id"], R["b_id"]), max(R["a_id"], R["b_id"]))].append(R["idx"])
        self.ruling_rel = {}                       # ruling -> the relation its status opened
        self.ruling_used = defaultdict(lambda: [0, set(), 0])   # ruling -> [cell-years, years, claims]
        self.ruling_r2 = Counter()                 # ruling -> claims R2 settled before it
        self.syn_rels = defaultdict(set)      # dossier -> its open colony and hierarchy relations
        self.hier_cell_years = Counter()      # kind -> cells tinted by a hierarchy relation, summed over years
        self.ended = set()           # dossiers whose end has been applied
        self.kf_cache = {}           # (dossier id, keyframe index) -> cells or None
        self.recip_vs = {}           # frozenset(pair), year -> (suzerain, vassal) for vassal_starts both record
        # Cliopatria area per dossier (sum of its Cliopatria names' shapes alive in a year)
        self.clio_slugs = []
        for d in self.dos:
            cs = []
            for nm in d["identity"].get("cliopatria_names", []) or []:
                s = inp.name2clio.get(nm)
                if s:
                    cs.append(s)
            self.clio_slugs.append(cs)
        self.clio_spans = [[sp for s in cs for sp in inp.clio_feats.get(s, [])] for cs in self.clio_slugs]
        self.clio_to_dossiers = defaultdict(set)
        for i, cs in enumerate(self.clio_slugs):
            for s in cs:
                self.clio_to_dossiers[s].add(i)
        # state
        n = self.n
        self.owner = np.full(n, -1, np.int32)
        self.status = np.zeros(n, np.int8)
        self.extra = np.full(n, -1, np.int32)
        self.rel = np.full(n, -1, np.int32)
        self.last_act = np.full(n, -1, np.int32)
        self.own_act = np.full(n, -1, np.int32)    # the act that gave each cell its owner (kept across years)
        self.evmask = np.zeros(n, bool)
        self.count = np.zeros(self.N, np.int64)
        self.touched = []
        # relations
        self.rels = []
        self.open_rel = {}
        self.vassal_stack = defaultdict(list)   # vassal dossier id -> its open vassal relations, oldest first
        self.closed_this_year = set()
        self.closed_contests = []
        # actions
        self.acts = []               # act id -> event reference string
        # logs
        self.log_unresolved = []     # dicts
        self.log_skipped = []
        self.log_conflicts = []      # (year, winner, loser, cells array, context, winner size, loser size, rule)
        self.log_snaps = []
        self.log_conflict_meta = []  # parallel to log_conflicts: (claimant, its act reference, holder's act per cell)
        self.log_snap_cells = []     # parallel to log_snaps: (cells added, removed, kept by others)
        self.last_kept = []          # plan_claim: the cells of its last call that their holders kept
        self.log_unclosed = []
        self.log_deaths = []         # (year, slug, cells_total, to_successors, to_nobody)
        self.log_noop = []           # events applied that moved nothing
        self.stats = Counter()
        self.flip_log = []
        self.year_records = {}
        self.window_buf = defaultdict(lambda: {"conflicts": [], "snaps": [], "unresolved": [], "skipped": []})
        self.anchor_meta = {}
        self.adj = {}                # pair code -> [first, last, max_edges, years]
        self.adj_open = {}           # pair code -> (start_year)
        self.adj_count = Counter()
        # window packets (notes/phase-c/windows/)
        self.adm = None              # (cell -> admin-1 label id, labels), set by main
        self.year_changed = {}       # year -> (cells changed, top places, top events)
        self.win_adj = {}            # pair -> most shared edges in the current window
        self.win_start_count = np.zeros(self.N, np.int64)
        self.win_data = {}           # window id -> counts at start and end, adjacency, open relation cells

    # ---- names -----------------------------------------------------------

    def nid(self, name):
        if name not in self.name_id:
            self.name_id[name] = len(self.names)
            self.names.append(name)
        return self.name_id[name]

    def alive(self, did, y):
        return 0 <= did < self.N and not self.umbrella[did] and self.start[did] <= y <= self.end[did]

    def counterpart(self, cp):
        """-> ('nobody', None) | ('dossier', id) | ('name', name_id)"""
        if cp is None:
            return ("none", None)
        c = str(cp).strip()
        if c.lower() in ("nobody", "none", "stateless"):
            return ("nobody", None)
        if c in self.name_id and self.name_id[c] < self.N:
            return ("dossier", self.name_id[c])
        s = self._slugify(c)
        if s in self.name_id and self.name_id[s] < self.N:
            self.stats["counterpart matched by slugify"] += 1
            return ("dossier", self.name_id[s])
        return ("name", self.nid(c))

    def _slugify(self, s):
        from slug import slugify
        return slugify(s)

    def metropole(self, did, y):
        """R1: the colony's metropole in year y (data/colonies.csv), -1 for a non-colony, a year without a
        metropole row or a metropole not alive."""
        if did < 0 or did >= self.N or not self.is_colony[did]:
            return -1
        for f, t, m, _ in self.colony_rows.get(did, ()):
            if f <= y <= t:
                return m if (m >= 0 and self.alive(m, y)) else -1
        return -1

    def weight(self, did, cp, y):
        """Size for working out who is the suzerain in a vassal_start: a colony with a metropole that year
        weighs as its metropole (R1: it is the metropole's land), except against that metropole or another
        colony of it."""
        s = self.size(did, y)
        m = self.metropole(did, y)
        if m >= 0 and m != cp and self.metropole(cp, y) != m:
            s = max(s, self.size(m, y))
        return s

    def clio_area(self, did, y):
        return sum(a for f, t, a in self.clio_spans[did] if f <= y <= t)

    def size(self, did, y, extra_cells=0):
        a = self.clio_area(did, y)
        if a > 0:
            return a
        return (int(self.count[did]) + extra_cells) * CELL_KM2

    # ---- cell operations -------------------------------------------------

    def _touch(self, idx, act, event=True):
        self.touched.append(idx)
        self.last_act[idx] = act
        if event:
            self.evmask[idx] = True

    def set_owner(self, idx, new, act, event=True, inherit_vassal=True):
        if idx.size == 0:
            return 0
        old = self.owner[idx]
        o = old[old >= 0]
        if o.size:
            self.count -= np.bincount(o, minlength=self.N)[: self.N]
        self.owner[idx] = new
        self.own_act[idx] = act if new >= 0 else -1
        self.rel[idx] = -1
        self.extra[idx] = -1
        self.status[idx] = DIRECT
        if new >= 0:
            self.count[new] += idx.size
            st = self.vassal_stack.get(new) if inherit_vassal else None
            r = st[-1] if st else None
            if r is not None:
                R = self.rels[r]
                self.status[idx] = R.get("st", VASSAL)
                self.extra[idx] = R["suzerain"]
                self.rel[idx] = r
        self._touch(idx, act, event)
        return int(idx.size)

    def set_status(self, idx, st, r, extra, act, event=True):
        if idx.size == 0:
            return 0
        self.status[idx] = st
        self.rel[idx] = r
        self.extra[idx] = extra
        self._touch(idx, act, event)
        return int(idx.size)

    def base_status(self, idx, act, event=True):
        """Cells leaving a relation: the owner's open vassal tint (an explicit suzerain, else a colony's
        metropole), else direct."""
        if idx.size == 0:
            return 0
        own = self.owner[idx]
        st = np.zeros(idx.size, np.int8)
        ex = np.full(idx.size, -1, np.int32)
        rl = np.full(idx.size, -1, np.int32)
        for o in np.unique(own).tolist():
            stack = self.vassal_stack.get(o) if o >= 0 else None
            if stack:
                r = stack[-1]
                m = own == o
                st[m] = self.rels[r].get("st", VASSAL)
                ex[m] = self.rels[r]["suzerain"]
                rl[m] = r
        self.status[idx] = st
        self.rel[idx] = rl
        self.extra[idx] = ex
        self._touch(idx, act, event)
        return int(idx.size)

    def held_by(self, cells, did):
        return cells[self.owner[cells] == did]

    # ---- relations -------------------------------------------------------

    def open_relation(self, key, kind, y, act, **kw):
        r = self.open_rel.get(key)
        if r is not None:
            return r, False
        r = len(self.rels)
        rec = {"id": r, "kind": kind, "since": y, "act": act, "open": True, "end": None, "key": key}
        rec.update(kw)
        self.rels.append(rec)
        self.open_rel[key] = r
        return r, True

    def close_relation(self, r, y, act, why="end event", event=True):
        R = self.rels[r]
        if not R["open"]:
            return 0
        if R.get("synthetic"):
            self.syn_rels[R["vassal"]].discard(r)
        cells = np.flatnonzero(self.rel == r)
        moved = 0
        if cells.size:
            if R["kind"] == "vassal":
                vas = R["vassal"]
                own_suz = cells[self.owner[cells] == R["suzerain"]]
                rest = cells[self.owner[cells] != R["suzerain"]]
                stack = self.vassal_stack.get(vas, [])
                if r in stack:
                    stack.remove(r)
                # still the vassal of another suzerain (nested vassalage) or a colony: that tint again
                self.base_status(rest, act, event)
                if own_suz.size:
                    # the suzerain held a vassal without a dossier (or one not drawn yet): the land
                    # returns to the vassal's own slug when it has a living dossier, else to nobody
                    target = vas if (vas < self.N and self.alive(vas, y) and vas not in self.ended) else -1
                    self.set_owner(own_suz, target, act)
                    moved = own_suz.size
            else:
                self.base_status(cells, act, event)
        R["open"] = False
        R["end"] = y
        R["end_act"] = act
        R["end_why"] = why
        R["cells_at_end"] = cells
        if self.open_rel.get(R["key"]) == r:
            del self.open_rel[R["key"]]
        if R["kind"] == "vassal" and r in self.vassal_stack.get(R["vassal"], []):
            self.vassal_stack[R["vassal"]].remove(r)
        self.closed_this_year.add(R["key"])
        if R["kind"] == "contest":
            self.closed_contests.append(r)
        return moved

    # ---- conflicts -------------------------------------------------------

    def decide(self, a, b, y, sa, sb, ruling=None):
        """a claims cells b holds that no event of the year settled. -> (winner, rule).
        R2: a successor (A.successors or B.predecessors) wins from its start year on (when each lists the
        other, the later-born one); with R2_BORN_AFTER (off) only a successor born after its predecessor.
        R3: data/hierarchy.csv (same_state: the parent; constituent / vassal:
        the deepest child). Rule 4: an open vassal of the other keeps its land. R1: of two colonies of the same metropole the smaller wins; a colony
        with a metropole that year wins against any other dossier. Otherwise the smaller state wins."""
        if self.rules:
            if R2_BORN_AFTER:
                # the successor born after its predecessor (of two that list each other, the later-born one)
                ab = (b, a) in self.succ and self.start[b] > self.start[a] and y >= self.start[b]
                ba = (a, b) in self.succ and self.start[a] > self.start[b] and y >= self.start[a]
                r2 = b if ab else (a if ba else None)
            else:
                ab = (b, a) in self.succ and y >= self.start[b]
                ba = (a, b) in self.succ and y >= self.start[a]
                r2 = None
                if ab != ba:
                    r2 = b if ab else a
                elif ab and ba and self.start[a] != self.start[b]:
                    r2 = a if self.start[a] > self.start[b] else b
            if r2 is not None:
                if ruling is not None:
                    self.ruling_r2[ruling] += 1
                return r2, "R2 succession"
            # a ruling of data/patches/<window>.json for this pair, year (and cells)
            if ruling is not None:
                return self.rulings[ruling]["winner_id"], "ruling " + self.rulings[ruling]["id"]
            # R3: data/hierarchy.csv (same_state: the parent's dossier is drawn; constituent or vassal: the
            # deepest child owns the cell, in its immediate parent's tint)
            if self.hier_rows or self.hier_same:
                h = self.hier_decide(a, b, y)
                if h is not None:
                    return h
            # rule 4: a state's open vassal keeps its land against its suzerain (a colony included)
            if ("vassal", a, b) in self.open_rel:
                return b, "vassal keeps"
            if ("vassal", b, a) in self.open_rel:
                return a, "vassal keeps"
            ma, mb = self.metropole(a, y), self.metropole(b, y)
            if ma >= 0 and ma == mb:
                return (a if sa < sb else b), "R1 same metropole"
            if ma >= 0 and mb < 0:
                return a, "R1 colony"
            if mb >= 0 and ma < 0:
                return b, "R1 colony"
        return (a if sa < sb else b), "size"

    def plan_claim(self, cells, did, y, allowed, claimant_size):
        """Which of `cells` did may take: nobody's, did's own and `allowed` holders' cells outright; a cell
        of any other state only when no event of this year settled it and `decide` gives it to did.
        -> (cells to take, conflicts [(winner, loser, cells, winner size, loser size, rule, claimant,
        the act that gave each cell to its holder)], cells kept by others); the kept cells go to self.last_kept"""
        self.last_kept = []
        if cells.size == 0:
            return cells, [], 0
        own = self.owner[cells]
        ok = (own == -1) | (own == did)
        for a in allowed:
            ok |= own == a
        parts = [cells[ok & (own != did)]]
        rest = cells[~ok]
        conflicts, lost = [], 0
        if rest.size:
            ro = self.owner[rest]
            for b in np.unique(ro).tolist():
                cb = rest[ro == b]
                cs = cb[~self.evmask[cb]]
                lost += cb.size - cs.size
                if cs.size < cb.size:
                    self.last_kept.append(cb[self.evmask[cb]])
                if cs.size == 0:
                    continue
                sb = self.size(b, y)
                for cp_, ru in self.ruling_parts(did, b, y, cs):
                    w, rule = self.decide(did, b, y, claimant_size, sb, ru)
                    hold = self.own_act[cp_]
                    if w == did:
                        parts.append(cp_)
                        conflicts.append((did, b, cp_, claimant_size, sb, rule, did, hold))
                    else:
                        lost += cp_.size
                        self.last_kept.append(cp_)
                        conflicts.append((b, did, cp_, sb, claimant_size, rule, did, hold))
        take = parts[0] if len(parts) == 1 else np.sort(np.concatenate(parts))
        return take, conflicts, lost

    def ruling_parts(self, a, b, y, cells):
        """Split a conflict's cells by the rulings in force for the pair in year y (a ruling with a region
        first, file order within each group) -> [(cells, ruling index or None)]"""
        lst = self.rulings_by_pair.get((min(a, b), max(a, b))) if self.rules else None
        if not lst:
            return [(cells, None)]
        out, rest = [], cells
        for k in lst:
            R = self.rulings[k]
            if not R["from"] <= y <= R["to"]:
                continue
            if R["cells"] is None:
                out.append((rest, k))
                rest = rest[:0]
                break
            m = np.isin(rest, R["cells"])
            if m.any():
                out.append((rest[m], k))
                rest = rest[~m]
            if rest.size == 0:
                break
        if rest.size:
            out.append((rest, None))
        return out

    def ruling_tint(self, cells, k, win, lose, y):
        """A ruling with a status: the cells it gave (or left) to its winner take that status, in a relation
        that closes at the start of the year after the ruling's last."""
        R = self.rulings[k]
        st = R["st"]
        if st is None:
            return
        mine = cells[self.owner[cells] == win]
        if mine.size == 0:
            return
        r = self.ruling_rel.get(k)
        if r is None or not self.rels[r]["open"]:
            act = self.new_act(patch_ref(R["window"], "rulings", R["k"]))
            if st in TINTS:
                r, _ = self.open_relation(("ruling", k), "vassal", y, act, suzerain=R["extra_id"], vassal=win,
                                          st=st, ruling=R["id"])
            elif st == OCCUPIED:
                r, _ = self.open_relation(("ruling", k), "occupation", y, act, occupier=R["extra_id"], owner=win,
                                          ruling=R["id"])
            else:
                r, _ = self.open_relation(("ruling", k), "contest", y, act, a=win, b=lose, war=None, ruling=R["id"])
            self.ruling_rel[k] = r
        Rr = self.rels[r]
        extra = lose if st == CONTESTED else R["extra_id"]
        self.set_status(mine, st, r, extra, Rr["act"], event=False)

    def do_rulend(self, did, y, k):
        r = self.ruling_rel.get(k)
        if r is None or not self.rels[r]["open"]:
            return
        R = self.rulings[k]
        act = self.new_act("%s ends after %d" % (patch_ref(R["window"], "rulings", R["k"]), R["to"]))
        self.close_relation(r, y, act, why="ruling ends", event=False)

    def hier_path(self, x, target, y):
        """R3: when `target` is x's parent, grandparent... in year y (vassal / constituent rows of
        data/hierarchy.csv), the row of x's immediate parent on that chain, else None."""
        first = {}
        frontier = [(x, None)]
        seen = {x}
        for _ in range(8):
            nxt = []
            for node, hop in frontier:
                for j in self.hier_up.get(node, ()):
                    c, p, f, t, kind, conf = self.hier_rows[j]
                    if not (f <= y <= t) or p in seen:
                        continue
                    h = j if hop is None else hop
                    if p == target:
                        return h
                    seen.add(p)
                    nxt.append((p, h))
            if not nxt:
                return None
            frontier = nxt
        return None

    def hier_decide(self, a, b, y):
        """R3 for a claim between a and b in year y -> (winner, rule) or None."""
        for c, p in ((a, b), (b, a)):
            for f, t in self.hier_same.get((c, p), ()):
                if f <= y <= t:
                    return p, "R3 same state"
        for c, p in ((a, b), (b, a)):
            j = self.hier_path(c, p, y)
            if j is not None:
                self.r3_hop[(c, p, y)] = j
                return c, "R3 " + self.hier_rows[j][4]
        return None

    def log_conflict_list(self, y, conflicts, context, ref=""):
        for (win, lose, cs, sw, sl, rule, claimant, hold) in conflicts:
            self.log_conflicts.append((y, win, lose, cs.copy(), context, sw, sl, rule))
            self.log_conflict_meta.append((claimant, ref, hold))
            if rule in ("R3 vassal", "R3 constituent"):
                self.r3_tint(cs, win, lose, y)
            elif rule.startswith("ruling "):
                k = self.ruling_by_id[rule[7:]]
                u = self.ruling_used[k]
                u[0] += int(cs.size)
                u[1].add(y)
                u[2] += 1
                self.ruling_tint(cs, k, win, lose, y)

    def r3_tint(self, cells, child, other, y):
        """R3: cells the child won or kept against its parent (or an ancestor) take the status of the row
        to its immediate parent, unless a suzerainty from the ledger is the child's current tint."""
        j = self.r3_hop.get((child, other, y))
        r = self.hier_rel.get(j) if j is not None else None
        if r is None or not self.rels[r]["open"]:
            return
        stack = self.vassal_stack.get(child)
        if stack and not self.rels[stack[-1]].get("synthetic"):
            return
        mine = cells[self.owner[cells] == child]
        R = self.rels[r]
        self.set_status(mine, R["st"], r, R["suzerain"], R["act"], event=False)

    def claim(self, cells, did, y, act, allowed, context, claimant_size, event=True):
        take, conflicts, lost = self.plan_claim(cells, did, y, allowed, claimant_size)
        moved = self.set_owner(take, did, act, event)
        self.log_conflict_list(y, conflicts, context, self.acts[act])
        return moved, lost

    # ---- the actions -----------------------------------------------------

    def region_cells(self, did, where, spec, y, etype):
        if spec is None:
            return None
        cells, errs = self.res.resolve(spec)
        if errs:
            self.log_unresolved.append({"slug": self.slugs[did], "where": where, "year": y, "type": etype,
                                        "spec": spec, "errors": errs})
            return None
        return cells

    def build_actions(self):
        """Per year: a list of (sort key, kind, dossier id, payload)."""
        acts = defaultdict(list)
        caption_years = set()
        for did, d in enumerate(self.dos):
            last_month = {}
            for i, e in enumerate(d["ledger"]):
                y = int(e["year"])
                m = e.get("month")
                if m is None:
                    m = last_month.get(y, 0)
                last_month[y] = m
                first = 0 if e.get("type") == "found" else 1
                acts[y].append(((m, first, did, i), "ev", did, i))
            if self.umbrella[did]:
                continue
            for y in self.keyframe_years(did):
                acts[y].append(((13, 0, did, 0), "kf", did, None))
            if self.has_dissolve[did]:
                acts[int(self.end[did])].append(((14, 0, did, 0), "end", did, None))
        # R1: a colony's metropole relation opens (or changes) at the start of each colonies.csv row
        for did, rows in self.colony_rows.items():
            starts = {f for f, t, m, c in rows}
            for f, t, m, c in rows:
                acts[f].append(((-1, 0, did, 0), "col", did, m))
                if t + 1 <= self.end[did] and t + 1 not in starts:
                    acts[t + 1].append(((-1, 0, did, 0), "col", did, -1))
        # R3: a hierarchy relation opens at the start of its row's first year and closes at the start of
        # the year after its last (a row ending with the child's life is closed by its death)
        for j, (c, p, f, t, kind, conf) in enumerate(self.hier_rows):
            acts[f].append(((-1, 2, c, j), "hier", c, j))
            if t + 1 <= min(self.end[c], self.until):
                acts[t + 1].append(((-1, 1, c, j), "hierend", c, j))
        # rulings with a status: their relation closes at the start of the year after the ruling's last
        for R in self.rulings:
            if R["st"] is not None and R["to"] + 1 <= self.until:
                acts[R["to"] + 1].append(((-1, 1, R["winner_id"], R["idx"]), "rulend", R["winner_id"], R["idx"]))
        moved = 0
        for y in acts:
            acts[y].sort(key=lambda a: a[0])
            acts[y], k = self.ends_first(acts[y])
            moved += k
        self.stats["*_start applied after a same-year *_end of another dossier (ends first)"] += moved
        self.actions = acts
        log("actions: %d years with something to do, %d actions; %d *_start events moved after another "
            "dossier's *_end" % (len(acts), sum(len(v) for v in acts.values()), moved))

    REL_START = ("vassal_start", "contest_start", "occupation_start")
    REL_END = ("vassal_end", "contest_end", "occupation_end")

    def ends_first(self, lst):
        """One year's actions (sorted by key) -> the same with the ledger events merged so that an *_end
        (vassal_end, contest_end, occupation_end) of one dossier is applied before an *_start of another
        dossier of the same month, or where either month is unknown (no event of its dossier in that year
        has a month), when their regions share land (fix round fx-02: a relation another state ends that
        year is closed before a new one over the same land opens). Each dossier's own order is kept: a
        start waits only while another dossier still has such an end to apply, and when every next event
        waits, the earliest goes.
        -> (actions, number of starts that now come after an end they came before)."""
        evs = [a for a in lst if a[1] == "ev"]
        if len(evs) < 2:
            return lst, 0
        dated = {a[2] for a in evs if self.dos[a[2]]["ledger"][a[3]].get("month") is not None}
        info = []
        for a in evs:
            t = self.dos[a[2]]["ledger"][a[3]].get("type")
            info.append((1 if t in self.REL_END else 2 if t in self.REL_START else 0, a[0][0], a[2] not in dated))
        if not any(k == 1 for k, _, _ in info) or not any(k == 2 for k, _, _ in info):
            return lst, 0
        queues = defaultdict(list)
        for j, a in enumerate(evs):
            queues[a[2]].append(j)
        for q in queues.values():
            q.reverse()                      # pop() from the end = the dossier's next event
        pend = defaultdict(set)              # dossier -> its ends not applied yet
        for j, (k, m, u) in enumerate(info):
            if k == 1:
                pend[evs[j][2]].add(j)

        cells = {}

        def land(j):
            if j not in cells:
                e = self.dos[evs[j][2]]["ledger"][evs[j][3]]
                c, errs = self.res.resolve(e["region"]) if e.get("region") is not None else (None, True)
                cells[j] = None if errs or c is None or not c.size else c
            return cells[j]

        def meets(j, j2):
            a, b = land(j), land(j2)
            return a is not None and b is not None and bool(np.isin(a, b, assume_unique=False).any())

        def waits(j):
            k, m, u = info[j]
            if k != 2:
                return False
            d = evs[j][2]
            return any(d2 != d and any((info[j2][1] == m or u or info[j2][2]) and meets(j, j2) for j2 in js)
                       for d2, js in pend.items() if js)

        order = []
        while len(order) < len(evs):
            heads = sorted(q[-1] for q in queues.values() if q)
            pick = next((j for j in heads if not waits(j)), heads[0])
            order.append(pick)
            queues[evs[pick][2]].pop()
            pend[evs[pick][2]].discard(pick)
        if order == sorted(order):
            return lst, 0
        pos = {j: i for i, j in enumerate(order)}
        moved = sum(1 for j, (k, _, _) in enumerate(info) if k == 2 and any(
            info[j2][0] == 1 and j2 > j and pos[j2] < pos[j] and meets(j, j2) for j2 in range(len(evs))))
        it = iter([evs[j] for j in order])
        return [next(it) if a[1] == "ev" else a for a in lst], moved

    def keyframes(self, did):
        """The dossier's keyframes as dicts {shape_id, verdict, from, to, spec | feat}."""
        d = self.dos[did]
        if "_kf" in d:
            return d["_kf"]
        out = []
        for j, k in enumerate(d.get("keyframe_review", [])):
            sid = k.get("shape_id")
            sh = self.inp.shapes.get(sid)
            fy = k.get("from", sh[0] if sh else None)
            ty = k.get("to", sh[1] if sh else None)
            if fy is None or ty is None:
                out.append({"j": j, "shape_id": sid, "verdict": k.get("verdict"), "from": None, "to": None,
                            "error": "no years (not in shapes.csv and no from/to)"})
                continue
            rec = {"j": j, "shape_id": sid, "verdict": k.get("verdict"), "from": int(fy), "to": int(ty),
                   "text": (k.get("correction") or {}).get("text") or k.get("note") or "",
                   "source": k.get("source")}
            if k.get("_patch"):
                rec["patch"] = patch_ref(k["_patch"], "keyframe_overrides", k["_patch_k"])
            if k.get("verdict") in ("adjust", "wrong") or (sh is None and k.get("correction")):
                rec["spec"] = k.get("correction")
                if rec["spec"] is None:
                    rec["error"] = "no correction"
            elif sh is not None:
                rec["feat"] = self.inp.shape_feat.get(sid)
            elif k.get("correction"):
                rec["spec"] = k["correction"]
            else:
                rec["error"] = "new keyframe without a correction"
            out.append(rec)
        d["_kf"] = out
        return out

    def keyframe_years(self, did):
        s, e = int(self.start[did]), int(self.end[did])
        ys = set()
        for k in self.keyframes(did):
            if k.get("from") is None or k["to"] < s or k["from"] > e or k["from"] > k["to"]:
                continue
            ys.add(max(k["from"], s))
        return sorted(ys)

    def keyframe_cells(self, did, k, y):
        key = (did, k["j"])
        if key in self.kf_cache:
            return self.kf_cache[key]
        where = "/keyframe_review/%d (%s)" % (k["j"], k["shape_id"])
        if k.get("error"):
            self.log_unresolved.append({"slug": self.slugs[did], "where": where, "year": y, "type": "keyframe",
                                        "spec": None, "errors": [("", k["error"])]})
            cells = None
        elif "feat" in k:
            cells = self.inp.feature_cells(k["feat"]) if k["feat"] is not None else None
        else:
            cells = self.region_cells(did, where, k["spec"], y, "keyframe")
        self.kf_cache[key] = cells
        return cells

    def new_act(self, ref):
        self.acts.append(ref)
        return len(self.acts) - 1

    def where(self, did, i):
        """A ledger event's place: /ledger/<i>, or data/patches/<window>.json: events/<k> for a patch event."""
        e = self.dos[did]["ledger"][i]
        if e.get("_patch"):
            return patch_ref(e["_patch"], "events", e["_patch_k"])
        return "/ledger/%d" % i

    def ev_index(self, did, i):
        e = self.dos[did]["ledger"][i]
        return patch_ref(e["_patch"], "events", e["_patch_k"]) if e.get("_patch") else i

    def skip(self, did, i, y, etype, reason, stat=None):
        self.stats["skipped: " + (stat or reason)] += 1
        self.stats["events skipped"] += 1
        rec = {"slug": self.slugs[did], "where": self.where(did, i), "year": y, "type": etype, "reason": reason}
        self.log_skipped.append(rec)

    # ---- one ledger event ------------------------------------------------

    def do_event(self, did, i, y, rec):
        d = self.dos[did]
        e = d["ledger"][i]
        t = e.get("type")
        slug = self.slugs[did]
        pw = e.get("_patch")
        act = self.new_act(patch_ref(pw, "events", e["_patch_k"]) if pw else "%s/ledger/%d" % (slug, i))
        note = e.get("note", "")
        cap = {"slug": slug, "year": y, "type": t, "text": first_sentence(note), "source": e.get("source")}
        if pw:
            cap["patch"] = pw
        if e.get("month"):
            cap["month"] = e["month"]
        rec["captions"].append(cap)
        if t in ("rename",):
            self.stats["events applied"] += 1
            return
        if t == "capital_move":
            self.stats["events applied"] += 1
            self.add_capitals(did, y, rec)
            return
        if self.umbrella[did]:
            self.skip(did, i, y, t, "umbrella dossier (moves no cells)")
            return
        if not self.alive(did, y):
            self.skip(did, i, y, t, "dossier not alive in the event year")
            return
        if t == "dissolve":
            self.stats["events applied"] += 1   # applied at year end (rule 7)
            return
        cells = self.region_cells(did, self.where(did, i), e.get("region"), y, t)
        if cells is None:
            if t == "found":
                self.birth(did, i, y, act, None, rec)
                return
            reason = "region does not resolve" if e.get("region") is not None else "no region"
            self.skip(did, i, y, t, reason)
            return
        if cells.size == 0 and t in ("gain", "loss", "split", "merge", "contest_start", "occupation_start"):
            # the region holds no land cell (an Antarctic claim, the Hawar or Swan Islands, a polity minus
            # itself): the event moves no land, so it is skipped and logged, not reported as unresolved
            self.skip(did, i, y, t, "region resolves to no land cell (the event moves no land)")
            return
        kind, cp = self.counterpart(e.get("counterpart"))
        cp_live = kind == "dossier" and self.alive(cp, y)
        cp_any_live = kind == "dossier" and 0 <= cp < self.N and not self.umbrella[cp] and \
            self.start[cp] <= y + 1 and y <= self.end[cp]
        moved = 0
        if t == "found":
            self.birth(did, i, y, act, cells, rec)
            return
        elif t == "gain":
            if cp_live:
                take = self.held_by(cells, cp)
                if take.size == 0:
                    take = self.held_by(cells, -1)
                    self.stats["gain: counterpart holds none of the region, took nobody's land"] += 1
            else:
                take = self.held_by(cells, -1)
            moved = self.set_owner(take, did, act)
        elif t == "loss":
            if cp_live and self.paired_gain(did, cp, y):
                self.stats["loss: applied as the counterpart's gain"] += 1
                self.stats["events applied"] += 1
                return
            give = self.held_by(cells, did)
            moved = self.set_owner(give, cp if cp_live else -1, act)
        elif t == "split":
            give = self.held_by(cells, did)
            moved = self.set_owner(give, cp if cp_any_live else -1, act)
        elif t == "merge":
            if not cp_live:
                # round 12: a merge into a counterpart with no living dossier that year (a name, nobody, an
                # umbrella, a slug not alive) is a gain from nobody: the region's cells nobody holds pass to
                # the state, its own cells stay (round 11 gave them to nobody when it held more of the region
                # than nobody did). Listed in skipped_events.csv with the branch that applied.
                mine = self.held_by(cells, did).size
                free = self.held_by(cells, -1)
                self.stats[MERGE_NO_CP] += 1
                if free.size == 0:
                    self.skip(did, i, y, t, "%s: nothing moved (the region holds %d of its cells and none of "
                              "nobody's)" % (MERGE_NO_CP, mine), stat=MERGE_NO_CP_NONE)
                    return
                self.stats[MERGE_NO_CP_GAIN] += 1
                self.log_skipped.append({"slug": slug, "where": self.where(did, i), "year": y, "type": t,
                                         "reason": "%s: applied as a gain from nobody (%d of nobody's cells to "
                                                   "the state; its %d cells in the region stay)" % (
                                                       MERGE_NO_CP, free.size, mine)})
                moved = self.set_owner(free, did, act)
            else:
                moved = self.merge(did, cp, kind, cells, y, act)
        elif t == "contest_start":
            moved = self.contest_start(did, cp, kind, cells, y, act, i)
        elif t == "contest_end":
            moved = self.relation_end("contest", did, cp, kind, y, act, i, landless=cells.size == 0)
        elif t == "occupation_start":
            moved = self.occupation_start(did, cp, kind, cells, y, act, i)
        elif t == "occupation_end":
            moved = self.relation_end("occupation", did, cp, kind, y, act, i, landless=cells.size == 0)
        elif t == "vassal_start":
            moved = self.vassal_start(did, cp, kind, cells, y, act, i)
        elif t == "vassal_end":
            moved = self.relation_end("vassal", did, cp, kind, y, act, i, landless=cells.size == 0)
        else:
            self.skip(did, i, y, t, "unknown event type")
            return
        if moved is None:
            return   # skipped inside (an *_end over no land with nothing open)
        self.stats["events applied"] += 1
        if moved == 0 and t not in ("contest_end", "occupation_end", "vassal_end"):
            self.stats["applied, no cell changed: " + t] += 1
            self.log_noop.append((slug, self.ev_index(did, i), y, t, int(cells.size)))

    def paired_gain(self, did, cp, y):
        """Does the counterpart's dossier carry the matching gain (same year, counterpart = this slug,
        a region that resolves)?"""
        slug = self.slugs[did]
        for e in self.dos[cp]["ledger"]:
            if e.get("type") == "gain" and int(e["year"]) == y:
                k, c = self.counterpart(e.get("counterpart"))
                if k == "dossier" and c == did:
                    cells, errs = self.res.resolve(e["region"]) if isinstance(e.get("region"), dict) else (None, [1])
                    if not errs:
                        return True
        return False

    def add_capitals(self, did, y, rec):
        for c in self.dos[did]["identity"].get("capitals", []) or []:
            if c.get("from") == y:
                rec["capitals"].append({"slug": self.slugs[did], "name": c.get("name"), "lon": c.get("lon"),
                                        "lat": c.get("lat")})

    def birth(self, did, i, y, act, cells, rec):
        d = self.dos[did]
        if cells is None or cells.size == 0:
            # rule 1 fallback: the first keyframe's corrected shape
            kfs = [k for k in self.keyframes(did) if k.get("from") is not None]
            kfs.sort(key=lambda k: k["from"])
            cells = None
            if kfs:
                cells = self.keyframe_cells(did, kfs[0], y)
                if cells is not None:
                    self.stats["birth from the first keyframe"] += 1
            if cells is None or cells.size == 0:
                self.stats["birth with no land"] += 1
                self.log_noop.append((self.slugs[did], i, y, "found", 0))
                self.add_capitals(did, y, rec)
                self.stats["events applied"] += 1
                return
        allowed = []
        for p in d["identity"].get("predecessors", []) or []:
            k, c = self.counterpart(p.get("slug"))
            if k == "dossier":
                allowed.append(c)
        k, c = self.counterpart(d["ledger"][i].get("counterpart") if i is not None else None)
        if k == "dossier":
            allowed.append(c)
        csize = self.clio_area(did, y) or cells.size * CELL_KM2
        moved, lost = self.claim(cells, did, y, act, allowed, "found", csize)
        self.add_capitals(did, y, rec)
        self.stats["events applied"] += 1

    def merge(self, did, cp, kind, cells, y, act):
        """A merge with a living counterpart (do_event makes the others a gain from nobody): the state that
        ends that year is absorbed, otherwise the side holding less of the region."""
        if kind == "dossier" and self.alive(cp, y):
            ends_me = self.has_dissolve[did] and self.end[did] == y
            ends_cp = self.has_dissolve[cp] and self.end[cp] == y
            if ends_me and not ends_cp:
                absorbed = True
            elif ends_cp and not ends_me:
                absorbed = False
            else:
                absorbed = self.held_by(cells, did).size >= self.held_by(cells, cp).size
            if absorbed:
                return self.set_owner(self.held_by(cells, did), cp, act)
            return self.set_owner(self.held_by(cells, cp), did, act)
        return 0

    def war_name(self, did, cp_name, y):
        best = None
        for w in self.dos[did].get("wars", []) or []:
            if cp_name in (w.get("belligerents") or []):
                if w.get("from", y) <= y <= w.get("to", y):
                    return w.get("name")
                if best is None:
                    best = w.get("name")
        return best

    def contest_start(self, did, cp, kind, cells, y, act, i):
        if kind in ("nobody", "none"):
            self.stats["contest with nobody: nothing to blend"] += 1
            return 0
        a, b = sorted((did, cp))
        r, new = self.open_relation(("contest", a, b), "contest", y, act, a=did, b=cp,
                                    war=self.war_name(did, self.names[cp], y))
        if not new:
            self.stats["contest_start merged into an open contest"] += 1
        own = self.owner[cells]
        mine = cells[own == did]
        theirs = cells[own == cp] if kind == "dossier" else cells[:0]
        n = self.set_status(mine, CONTESTED, r, cp, act)
        n += self.set_status(theirs, CONTESTED, r, did, act)
        return n

    def occupation_start(self, did, cp, kind, cells, y, act, i):
        own = self.owner[cells]
        h_me = int((own == did).sum())
        if kind == "dossier":
            h_cp = int((own == cp).sum())
            if h_cp >= h_me and h_cp > 0:
                occ, owner_id, take = did, cp, cells[own == cp]
            elif h_me > 0:
                occ, owner_id, take = cp, did, cells[own == did]
                self.stats["occupation_start recorded by the owner (roles reversed)"] += 1
            else:
                occ, owner_id, take = did, cp, cells[own == -1]
        else:
            h_free = int((own == -1).sum())
            if kind == "name" and h_me > h_free:
                occ, owner_id, take = cp, did, cells[own == did]
                self.stats["occupation_start recorded by the owner (roles reversed)"] += 1
            else:
                occ, owner_id, take = did, (cp if kind == "name" else -1), cells[own == -1]
        r, new = self.open_relation(("occupation", occ, owner_id), "occupation", y, act, occupier=occ, owner=owner_id)
        if not new:
            self.stats["occupation_start merged into an open occupation"] += 1
        return self.set_status(take, OCCUPIED, r, occ, act)

    def vassal_start(self, did, cp, kind, cells, y, act, i):
        if kind in ("nobody", "none"):
            self.stats["vassal_start with nobody: skipped"] += 1
            return 0
        own = self.owner[cells]
        pair = (frozenset((did, cp)), y) if kind == "dossier" else None
        if pair is not None and pair in self.recip_vs:
            # the counterpart recorded the same vassal_start this year: join the relation its record opened
            suz, vas = self.recip_vs[pair]
            take = cells[own == vas]
            self.stats["vassal_start recorded by both: joined the counterpart's relation"] += 1
        elif kind == "dossier" and self.alive(cp, y):
            h_me = int((own == did).sum())
            h_cp = int((own == cp).sum())
            w_me, w_cp = self.weight(did, cp, y), self.weight(cp, did, y)
            recip = self.reciprocal_vassal_start(did, cp, y)
            s_me = s_cp = None
            if recip:
                s_me, s_cp = self.shape_share(did, cells, y), self.shape_share(cp, cells, y)
            if self.metropole(did, y) == cp:
                # R1: between a colony and its own metropole, the metropole is the suzerain
                suz, vas, take = cp, did, cells[own == did]
                self.stats["vassal_start between a colony and its metropole: the metropole is the suzerain"] += 1
            elif self.metropole(cp, y) == did:
                suz, vas, take = did, cp, cells[own == cp]
                self.stats["vassal_start between a colony and its metropole: the metropole is the suzerain"] += 1
            elif recip and max(s_me, s_cp) >= 0.5 and min(s_me, s_cp) < 0.5 and abs(s_me - s_cp) >= 0.25:
                # both dossiers record it: the region is the vassal's land, so the party whose shape holds
                # most of it, when the other's does not, is the vassal (Himyar under Axum in 525, Aquitaine
                # under France in 990)
                if s_me > s_cp:
                    suz, vas, take = cp, did, cells[own == did]
                else:
                    suz, vas, take = did, cp, cells[own == cp]
                self.stats["vassal_start recorded by both: the vassal is the party whose shape holds the region"] += 1
            elif h_me > h_cp and w_cp > w_me:
                suz, vas, take = cp, did, cells[own == did]
                self.stats["vassal_start recorded by the vassal (roles reversed)"] += 1
            elif h_cp >= h_me and h_cp > 0 and w_cp > w_me and \
                    self.shape_share(did, cells, y) >= 0.5:
                # recorded by the vassal (the schema wants the suzerain's dossier to record it) whose land
                # the larger counterpart already holds: the counterpart is the suzerain, not the vassal
                suz, vas, take = cp, did, cells[:0]
                self.stats["vassal_start recorded by the vassal inside the suzerain's land (roles reversed)"] += 1
            elif h_me == 0 and h_cp == 0 and w_cp > w_me:
                # neither holds any of the region: the smaller party is the vassal
                suz, vas, take = cp, did, cells[:0]
                self.stats["vassal_start over land neither holds: the smaller party is the vassal"] += 1
            elif h_me > 0 and h_cp == 0 and self.count[cp] > 0 and self.shape_share(did, cells, y) >= 0.5 and \
                    self.shape_share(cp, cells, y) < 0.5:
                # the region is the recorder's own land (it holds it, inside its own shape and outside the
                # counterpart's, which holds land elsewhere): the recorder is the vassal (Qatna under Mitanni,
                # Kongo under Portuguese Angola, Ryukyu under the Southern Ming)
                suz, vas, take = cp, did, cells[own == did]
                self.stats["vassal_start recorded by the vassal over its own land (roles reversed)"] += 1
            else:
                suz, vas, take = did, cp, cells[own == cp]
        else:
            suz, vas, take = did, cp, cells[:0]
        r, new = self.open_relation(("vassal", suz, vas), "vassal", y, act, suzerain=suz, vassal=vas)
        if pair is not None:
            self.recip_vs.setdefault(pair, (suz, vas))
        if not new:
            self.stats["vassal_start merged into an open relation"] += 1
        if vas < self.N:
            if r not in self.vassal_stack[vas]:
                self.vassal_stack[vas].append(r)   # land the vassal gains or is born with later keeps the tint
        if take.size:
            return self.set_status(take, VASSAL, r, suz, act)
        # no dossier for the vassal, or it holds none of the region: the region's land held by the
        # suzerain or by nobody becomes the suzerain's, in the vassal tint (brief rule 4)
        take = cells[(own == suz) | (own == -1)]
        if kind == "dossier":
            self.stats["vassal_start: vassal holds none of the region, drawn as the suzerain's vassal land"] += 1
        self.set_owner(take, suz, act, inherit_vassal=False)
        return self.set_status(take, VASSAL, r, suz, act)

    def reciprocal_vassal_start(self, did, cp, y):
        """Does the counterpart's dossier record a vassal_start with this dossier in the same year?"""
        for e in self.dos[cp]["ledger"]:
            if e.get("type") == "vassal_start" and int(e["year"]) == y:
                k, c = self.counterpart(e.get("counterpart"))
                if k == "dossier" and c == did:
                    return True
        return False

    def shape_share(self, did, cells, y):
        """Share of `cells` inside the dossier's keyframe shape of year y (all its keyframes when none is alive)."""
        kfs = [k for k in self.keyframes(did) if k.get("from") is not None]
        alive = [k for k in kfs if k["from"] <= y <= k["to"]] or kfs
        parts = [c for c in (self.keyframe_cells(did, k, y) for k in alive) if c is not None and c.size]
        if not parts or cells.size == 0:
            return 0.0
        K = parts[0] if len(parts) == 1 else np.unique(np.concatenate(parts))
        return float(np.isin(cells, K).mean())

    def relation_end(self, kind, did, cp, ckind, y, act, i, landless=False):
        if ckind in ("nobody", "none"):
            keys = [("occupation", did, -1)] if kind == "occupation" else []
        elif kind == "contest":
            a, b = sorted((did, cp))
            keys = [("contest", a, b)]
        elif kind == "occupation":
            keys = [("occupation", did, cp), ("occupation", cp, did)]
            if ckind != "dossier":
                keys.append(("occupation", did, -1))
        else:
            keys = [("vassal", did, cp), ("vassal", cp, did)]
        for k in keys:
            r = self.open_rel.get(k)
            if r is not None:
                self.stats["%s_end closed a relation" % kind] += 1
                return self.close_relation(r, y, act) + 1
        if any(k in self.closed_this_year for k in keys):
            self.stats["%s_end already closed this year by its pair" % kind] += 1
            return 1
        if landless:
            # its start was skipped for the same landless region: skipped too, quietly
            self.skip(did, i, y, kind + "_end", "region resolves to no land cell and nothing is open")
            return None
        self.stats["%s_end closes nothing open" % kind] += 1
        self.log_unclosed.append((self.slugs[did], self.ev_index(did, i), y, kind + "_end",
                                  self.names[cp] if cp is not None else "nobody"))
        return 1

    # ---- keyframes -------------------------------------------------------

    def do_keyframe(self, did, y, rec):
        kfs = [k for k in self.keyframes(did) if k.get("from") is not None and k["from"] <= y <= k["to"]]
        starting = [k for k in kfs if k["from"] == y] or kfs
        parts = []
        for k in kfs:
            c = self.keyframe_cells(did, k, y)
            if c is not None:
                parts.append(c)
        if not parts:
            self.stats["keyframe year with no resolvable keyframe"] += 1
            return
        K = parts[0] if len(parts) == 1 else np.unique(np.concatenate(parts))
        if K.size == 0:
            self.stats["keyframe resolves to no land cell"] += 1
            return
        n = self.n
        inK = np.zeros(n, bool)
        inK[K] = True
        own = self.owner == did
        sp = own | (self.extra == did)
        nS = int(sp.sum())
        diff = int(np.count_nonzero(inK ^ sp))
        self.stats["keyframe checks"] += 1
        sid = starting[0]["shape_id"]
        ksize = self.clio_area(did, y) or K.size * CELL_KM2
        take, conflicts, lost = self.plan_claim(np.flatnonzero(inK & ~sp), did, y, [], ksize)
        kept = self.last_kept
        slug = self.slugs[did]
        kref = "%s/keyframe/%s" % (slug, sid)
        pk = [k["patch"] for k in kfs if k.get("patch")]
        if pk:
            kref += " [%s]" % ", ".join(pk)
        plain = self.status == DIRECT
        syn = self.syn_rels.get(did)
        if syn:
            # a colony's cells in its metropole's tint, a child's in its hierarchy parent's, count as direct
            plain |= np.isin(self.rel, np.fromiter(syn, np.int32, len(syn)))
        release = np.flatnonzero(own & plain & ~inK)
        moved = int(take.size + release.size)
        if not (moved > SNAP_CELLS or moved > SNAP_SHARE * nS):
            # within tolerance: nothing moves; overlaps the holder keeps are still logged as conflicts
            self.log_conflict_list(y, [c for c in conflicts if c[1] == did], "keyframe " + sid, kref)
            self.stats["keyframe within tolerance"] += 1
            return
        act = self.new_act(kref)
        added = self.set_owner(take, did, act, event=False)
        removed = self.set_owner(release, -1, act, event=False)
        self.log_conflict_list(y, conflicts, "keyframe " + sid, kref)
        self.stats["keyframe snaps"] += 1
        snap = {"slug": slug, "shape_id": sid, "shape_ids": [k["shape_id"] for k in starting], "year": y,
                "state_cells": nS, "keyframe_cells": int(K.size), "diff": diff, "added": int(added),
                "removed": int(removed), "kept_by_others": int(lost)}
        if pk:
            snap["patch"] = pk
        self.log_snaps.append(snap)
        kc = np.concatenate(kept).astype(np.int32) if kept else np.zeros(0, np.int32)
        self.log_snap_cells.append((take.astype(np.int32), release.astype(np.int32), kc, self.owner[kc]))
        if added or removed:
            text = first_sentence(starting[0].get("text", "")) or ("keyframe " + sid)
            cap = {"slug": slug, "year": y, "type": "keyframe", "shape_id": sid, "text": text,
                   "source": starting[0].get("source")}
            if pk:
                cap["patch"] = sorted({x.split(".json")[0].rsplit("/", 1)[-1] for x in pk})
            rec["captions"].append(cap)

    # ---- R1: colony metropoles -------------------------------------------

    def do_colony(self, did, y, m):
        """Open the colony's metropole relation for a colonies.csv row (closing the previous one) and tint
        the colony's cells: a synthetic vassal relation at the bottom of the colony's vassal stack, so an
        explicit suzerainty from the ledger shows over it and the metropole's tint returns when that ends."""
        if not self.alive(did, y):
            return
        old = self.colony_rel.get(did)
        if old is not None and self.rels[old]["open"] and self.rels[old]["suzerain"] == m:
            return
        if m >= 0 and not self.alive(m, y):
            self.stats["colonies.csv: metropole not alive in the row's first year"] += 1
            m = -1
        if old is None and m < 0:
            return
        slug = self.slugs[did]
        act = self.new_act("data/colonies.csv: %s, metropole %s from %d" % (
            slug, self.names[m] if m >= 0 else "none", y))
        if old is not None and self.rels[old]["open"]:
            R = self.rels[old]
            R["open"] = False
            R["end"] = y
            R["end_act"] = act
            R["end_why"] = "metropole changes (data/colonies.csv)"
            R["cells_at_end"] = np.flatnonzero(self.rel == old)
            if self.open_rel.get(R["key"]) == old:
                del self.open_rel[R["key"]]
            st = self.vassal_stack.get(did, [])
            if old in st:
                st.remove(old)
            self.syn_rels[did].discard(old)
        self.colony_rel.pop(did, None)
        if m >= 0:
            r, new = self.open_relation(("colony", m, did), "vassal", y, act, suzerain=m, vassal=did, colony=True,
                                        synthetic=True)
            st = self.vassal_stack[did]
            if r not in st:
                st.insert(0, r)
            self.colony_rel[did] = r
            self.syn_rels[did].add(r)
            self.stats["colony metropole relations opened"] += 1
        mine = np.flatnonzero(self.owner == did)
        if mine.size:
            sel = self.status[mine] == DIRECT
            if old is not None:
                sel |= self.rel[mine] == old
            self.base_status(mine[sel], act)

    # ---- R3: data/hierarchy.csv -------------------------------------------

    def do_hier(self, did, y, j):
        """Open a hierarchy row's relation. Confidence 2-3: a synthetic vassal / constituent relation under
        any suzerainty the ledger records for the child (like a colony's metropole tint), tinting the
        child's direct cells and the land it gains later. Confidence 1: the relation only marks the cells
        R3 settles in a conflict with the parent."""
        c, p, f, t, kind, conf = self.hier_rows[j]
        if not (self.alive(c, y) and self.alive(p, y)):
            self.stats["hierarchy.csv: row skipped, child or parent not alive in its first year"] += 1
            return
        st = CONSTITUENT if kind == "constituent" else VASSAL
        act = self.new_act("data/hierarchy.csv: %s %s of %s, %d-%d" % (self.slugs[c], kind, self.slugs[p], f, t))
        r, new = self.open_relation(("hier", p, c, j), "vassal", y, act, suzerain=p, vassal=c, hierarchy=kind,
                                    st=st, confidence=conf, synthetic=True)
        self.hier_rel[j] = r
        self.syn_rels[c].add(r)
        self.stats["hierarchy relations opened (%s, confidence %d)" % (kind, conf)] += 1
        if conf < 2:
            return
        stack = self.vassal_stack[c]
        pos = sum(1 for x in stack if self.rels[x].get("synthetic"))
        stack.insert(pos, r)
        mine = np.flatnonzero(self.owner == c)
        if mine.size:
            self.set_status(mine[self.status[mine] == DIRECT], st, r, p, act, event=False)

    def do_hierend(self, did, y, j):
        r = self.hier_rel.get(j)
        if r is None or not self.rels[r]["open"]:
            return
        c, p, f, t, kind, conf = self.hier_rows[j]
        act = self.new_act("data/hierarchy.csv: %s %s of %s ends after %d" % (self.slugs[c], kind, self.slugs[p], t))
        self.close_relation(r, y, act, why="data/hierarchy.csv row ends", event=False)

    # ---- deaths ----------------------------------------------------------

    def do_end(self, did, y, rec):
        d = self.dos[did]
        slug = self.slugs[did]
        di = max(i for i, e in enumerate(d["ledger"]) if e.get("type") == "dissolve")
        act = self.new_act("%s/ledger/%d" % (slug, di))
        self.ended.add(did)
        mine = np.flatnonzero(self.owner == did)
        total = int(mine.size)
        to_succ = 0
        for j, s in enumerate(d["identity"].get("successors", []) or []):
            if mine.size == 0:
                break
            k, c = self.counterpart(s.get("slug"))
            # a successor that has already ended (earlier in this year's deaths) takes nothing
            if k != "dossier" or self.umbrella[c] or not (self.start[c] <= y + 1 and y <= self.end[c]) or c == did \
                    or c in self.ended:
                self.stats["successor without a living dossier: its land goes to nobody"] += 1
                continue
            land = self.region_cells(did, "/identity/successors/%d" % j, s.get("land"), y, "successor")
            if land is None:
                continue
            inl = np.zeros(self.n, bool)
            inl[land] = True
            give = mine[inl[mine]]
            to_succ += self.set_owner(give, c, act)
            mine = mine[~inl[mine]]
        self.set_owner(mine, -1, act)
        self.log_deaths.append((y, slug, total, to_succ, int(mine.size)))
        # relations this state was party to
        for r in list(self.open_rel.values()):
            R = self.rels[r]
            parties = {R.get("a"), R.get("b"), R.get("occupier"), R.get("owner"), R.get("suzerain"), R.get("vassal")}
            if did in parties:
                self.close_relation(r, y, act, why="party ended")
                self.stats["relations closed by a party's end"] += 1
        # cells others hold under this state's name (vassal, occupied, contested) are released
        left = np.flatnonzero(self.extra == did)
        if left.size:
            self.base_status(left, act)
        self.colony_rel.pop(did, None)

    # ---- the year loop ---------------------------------------------------

    def run(self, anchor_years, on_anchor, on_window_end, window_ends):
        self.build_actions()
        first = min(min(self.actions), FIRST_YEAR)
        t0 = time.time()
        edges = self.edges()
        prev_years = 0
        for y in range(first, self.until + 1):
            if y in anchor_years:
                on_anchor(y, "start")
            acts = self.actions.get(y)
            if acts:
                self.owner0 = self.owner.copy()
                self.status0 = self.status.copy()
                self.extra0 = self.extra.copy()
                self.rel0 = self.rel.copy()
                self.touched = []
                self.closed_this_year = set()
                self.closed_contests = []
                rec = {"captions": [], "capitals": []}
                for key, kind, did, payload in acts:
                    if kind == "ev":
                        self.do_event(did, payload, y, rec)
                    elif kind == "kf":
                        self.do_keyframe(did, y, rec)
                    elif kind == "end":
                        self.do_end(did, y, rec)
                    elif kind == "col":
                        self.do_colony(did, y, payload)
                    elif kind == "hier":
                        self.do_hier(did, y, payload)
                    elif kind == "hierend":
                        self.do_hierend(did, y, payload)
                    elif kind == "rulend":
                        self.do_rulend(did, y, payload)
                self.finish_year(y, rec, edges)
            if self.hier_rel:
                self.count_hier(y)
            if y in window_ends:
                on_window_end(y)
            if (y - first) % 1000 == 0 and y != first:
                log("  year %d, %.0f s" % (y, time.time() - t0))
        for e in sorted(window_ends):
            if e > self.until:
                on_window_end(e)     # the last window (2020-2029) ends after the run's last year
        on_anchor(self.until + 1, "end")
        self.close_adjacency(self.until)
        log("compiled %d..%d in %.0f s" % (first, self.until, time.time() - t0))

    def count_hier(self, y):
        """Cells drawn in a hierarchy relation's tint this year, by kind (for the report)."""
        if not self.hier_rel or self.light:
            return
        ids = [r for r in self.hier_rel.values() if self.rels[r]["open"]]
        if not ids:
            return
        lut = np.zeros(len(self.rels) + 1, bool)
        lut[np.array(ids) + 1] = True
        m = lut[self.rel + 1]
        if m.any():
            st = self.status[m]
            self.hier_cell_years["vassal"] += int((st == VASSAL).sum())
            self.hier_cell_years["constituent"] += int((st == CONSTITUENT).sum())

    def finish_year(self, y, rec, edges):
        if self.touched:
            t = np.unique(np.concatenate(self.touched))
        else:
            t = np.zeros(0, np.int64)
        self.evmask[t] = False
        if self.light:
            self.last_act[t] = -1
            return
        ch = t[(self.owner0[t] != self.owner[t]) | (self.status0[t] != self.status[t]) | (self.extra0[t] != self.extra[t])]
        changes = []
        if ch.size:
            keys = np.stack([self.owner0[ch], self.owner[ch], self.status[ch].astype(np.int32), self.extra[ch],
                             self.last_act[ch]], axis=1)
            uk, inv = np.unique(keys, axis=0, return_inverse=True)
            inv = inv.ravel()
            order = np.argsort(inv, kind="stable")
            bounds = np.flatnonzero(np.diff(inv[order])) + 1
            for grp in np.split(order, bounds):
                o0, o1, st, ex, a = (int(v) for v in uk[inv[grp[0]]])
                cells = ch[grp]
                c = {"cells": to_runs(cells), "from": self.names[o0] if o0 >= 0 else None,
                     "to": self.names[o1] if o1 >= 0 else None}
                if st == DIRECT:
                    c["status"] = "direct" if o1 >= 0 else "neutral"
                else:
                    c["status"] = STATUS_LABEL[st]
                    if st in TINTS:
                        c["suzerain"] = self.names[ex]
                    elif st == OCCUPIED:
                        c["occupier"] = self.names[ex]
                    else:
                        c["claimants"] = [self.names[o1] if o1 >= 0 else None, self.names[ex]]
                c["event"] = self.acts[a] if a >= 0 else "anchor"
                c["n"] = int(cells.size)
                changes.append(c)
            self.stats["cells changed"] += int(ch.size)
            if self.adm is not None:
                lab, labels = self.adm
                u, c = np.unique(lab[ch], return_counts=True)
                o = np.lexsort((u, -c))[:3]
                pl = "; ".join("%s %d" % (labels[u[j]] if u[j] >= 0 else "unmapped", c[j]) for j in o)
                ua, ca = np.unique(self.last_act[ch], return_counts=True)
                oa = np.lexsort((ua, -ca))[:3]
                by = "; ".join("%s %d" % (self.acts[ua[j]] if ua[j] >= 0 else "?", ca[j]) for j in oa)
                self.year_changed[y] = (int(ch.size), pl, by)
            own_changed = ch[self.owner0[ch] != self.owner[ch]]
            if own_changed.size:
                self.update_adjacency(y, own_changed, edges)
        self.last_act[t] = -1
        # contests open in this year (rendering a single year needs them)
        contests = []
        rs = sorted({r for r in self.open_rel.values() if self.rels[r]["kind"] == "contest"} | set(self.closed_contests))
        for r in rs:
            R = self.rels[r]
            cells = np.flatnonzero(self.rel == r) if R["open"] else R.get("cells_at_end", np.zeros(0, np.int64))
            if cells.size == 0:
                continue
            contests.append({"cells": to_runs(cells), "a": self.names[R["a"]], "b": self.names[R["b"]],
                             "since": R["since"], "war": R.get("war"), "n": int(cells.size)})
        if changes or rec["captions"] or rec["capitals"]:
            self.year_records[y] = {"changes": changes, "contests": contests, "captions": rec["captions"],
                                    "capitals": rec["capitals"]}

    # ---- adjacency (shared cell edges between owners) ----------------------

    def edges(self):
        path = next((d / "edges_r5.npz" for d in CACHE_READ if (d / "edges_r5.npz").exists()), None)
        if path is not None:
            z = np.load(path)
            if int(z["n"]) == self.n:
                self.csr_ptr, self.csr_nb = z["ptr"], z["nb"]
                return z["u"], z["v"]
        import h3
        land = self.inp.land
        li = {c: i for i, c in enumerate(land)}
        ptr = np.zeros(self.n + 1, np.int64)
        nb = []
        for i, c in enumerate(land):
            ns = [li[x] for x in h3.grid_ring(c, 1) if x in li]
            nb.extend(ns)
            ptr[i + 1] = ptr[i] + len(ns)
        nb = np.array(nb, np.int32)
        src = np.repeat(np.arange(self.n, dtype=np.int32), np.diff(ptr))
        m = src < nb
        u, v = src[m], nb[m]
        write_cache_file("edges_r5.npz", lambda f: np.savez(f, n=self.n, ptr=ptr, nb=nb, u=u, v=v))
        self.csr_ptr, self.csr_nb = ptr, nb
        return u, v

    def update_adjacency(self, y, changed, edges):
        """Shared cell edges per pair of owners, updated from the cells whose owner changed."""
        ptr, nb = self.csr_ptr, self.csr_nb
        lens = ptr[changed + 1] - ptr[changed]
        tot = int(lens.sum())
        if tot == 0:
            return
        offs = np.concatenate(([0], np.cumsum(lens)[:-1]))
        idx = np.repeat(ptr[changed] - offs, lens) + np.arange(tot)
        src = np.repeat(changed, lens)
        dst = nb[idx]
        code = np.unique(np.minimum(src, dst).astype(np.int64) * self.n + np.maximum(src, dst))
        u = code // self.n
        v = code % self.n
        N1 = len(self.names) + 1
        touched = set()
        for own, sign in ((self.owner0, -1), (self.owner, 1)):
            a, b = own[u], own[v]
            m = (a != b) & (a >= 0) & (b >= 0)
            pa = np.minimum(a[m], b[m]).astype(np.int64)
            pb = np.maximum(a[m], b[m]).astype(np.int64)
            pc, cnt = np.unique(pa * N1 + pb, return_counts=True)
            for p, c in zip(pc.tolist(), cnt.tolist()):
                pair = (p // N1, p % N1)
                self.adj_count[pair] += sign * c
                touched.add(pair)
        for pair in touched:
            c = self.adj_count[pair]
            if c > 0:
                rec = self.adj.get(pair)
                if rec is None:
                    self.adj[pair] = rec = [y, y, c, 0]
                if pair not in self.adj_open:
                    self.adj_open[pair] = y
                if c > rec[2]:
                    rec[2] = c
                if c > self.win_adj.get(pair, 0):
                    self.win_adj[pair] = c
            else:
                if pair in self.adj_open:
                    s = self.adj_open.pop(pair)
                    rec = self.adj[pair]
                    rec[1] = y - 1
                    rec[3] += y - s
                del self.adj_count[pair]

    def drop_window(self, w):
        """A trial: forget the records of a window before its own (year records, conflict and snap logs)."""
        b = w["to"]
        for y in [y for y in self.year_records if y <= b]:
            del self.year_records[y]
        keep = [i for i, c in enumerate(self.log_conflicts) if c[0] > b]
        self.log_conflicts = [self.log_conflicts[i] for i in keep]
        self.log_conflict_meta = [self.log_conflict_meta[i] for i in keep]
        keep = [i for i, sn in enumerate(self.log_snaps) if sn["year"] > b]
        self.log_snaps = [self.log_snaps[i] for i in keep]
        self.log_snap_cells = [self.log_snap_cells[i] for i in keep]

    def window_start(self, y):
        self.win_adj = {p: c for p, c in self.adj_count.items() if c > 0}
        self.win_start_count = self.count.copy()

    def window_end(self, w):
        """Keep what the window's packet needs: cells per state at its start and end, the neighbour pairs of
        its years, the cells of the relations open at its end."""
        has = self.rel >= 0
        relc = np.bincount(self.rel[has], minlength=len(self.rels)) if has.any() else np.zeros(len(self.rels), np.int64)
        self.win_data[w["id"]] = {"start_count": self.win_start_count, "end_count": self.count.copy(),
                                  "adj": dict(self.win_adj),
                                  "open": {r: int(relc[r]) for r in self.open_rel.values() if r < relc.size}}

    def close_adjacency(self, y):
        for pair, s in list(self.adj_open.items()):
            rec = self.adj[pair]
            rec[1] = y
            rec[3] += y - s + 1
        self.adj_open = {}

    # ---- snapshots -------------------------------------------------------

    def snapshot(self, year, as_of):
        owners = {}
        o = self.owner
        order = np.argsort(o, kind="stable")
        so = o[order]
        s0 = np.searchsorted(so, 0)
        ids, idxs = so[s0:], order[s0:]
        if ids.size:
            bounds = np.flatnonzero(np.diff(ids)) + 1
            for ci, cx in zip(np.split(ids, bounds), np.split(idxs, bounds)):
                owners[self.names[int(ci[0])]] = to_runs(np.sort(cx))
        status = {"vassal": [], "constituent": [], "occupied": [], "contested": []}
        nd = np.flatnonzero(self.status != DIRECT)
        if nd.size:
            keys = np.stack([self.status[nd].astype(np.int32), self.owner[nd], self.extra[nd], self.rel[nd]], axis=1)
            uk, inv = np.unique(keys, axis=0, return_inverse=True)
            inv = inv.ravel()
            for gi, (st, ow, ex, r) in enumerate(uk.tolist()):
                cells = nd[inv == gi]
                g = {"owner": self.names[ow] if ow >= 0 else None}
                if st in TINTS:
                    g["suzerain"] = self.names[ex]
                elif st == OCCUPIED:
                    g["occupier"] = self.names[ex]
                else:
                    g["claimants"] = [self.names[ow] if ow >= 0 else None, self.names[ex]]
                g["relation"] = int(r)
                g["cells"] = to_runs(cells)
                status[STATUS_LABEL[st]].append(g)
        rels = {"contests": [], "occupations": [], "vassals": []}
        counts = Counter(self.rel[self.rel >= 0].tolist())
        for r in sorted(self.open_rel.values()):
            R = self.rels[r]
            base = {"id": r, "since": R["since"], "event": self.acts[R["act"]], "cells": int(counts.get(r, 0))}
            if R["kind"] == "contest":
                base.update({"a": self.names[R["a"]], "b": self.names[R["b"]], "war": R.get("war")})
                rels["contests"].append(base)
            elif R["kind"] == "occupation":
                base.update({"occupier": self.names[R["occupier"]],
                             "owner": self.names[R["owner"]] if R["owner"] >= 0 else None})
                rels["occupations"].append(base)
            else:
                base.update({"suzerain": self.names[R["suzerain"]], "vassal": self.names[R["vassal"]]})
                if R.get("colony"):
                    base["colony"] = True
                if R.get("hierarchy"):
                    base["hierarchy"] = R["hierarchy"]
                    base["confidence"] = R["confidence"]
                rels["vassals"].append(base)
            if R.get("ruling"):
                base["ruling"] = R["ruling"]
        return {"year": year, "as_of": as_of, "grid": "land_r5.txt", "land_cells": self.n,
                "owners": owners, "status": status, "relations": rels,
                "polities": len(owners),
                "cells_owned": int((self.owner >= 0).sum()),
                "compiler": "tools/compile_dossiers.py"}

    def open_lists(self):
        """handoff open_* lists for the current moment."""
        oc, oo, ov = [], [], []
        for r in sorted(self.open_rel.values()):
            R = self.rels[r]
            cells = np.flatnonzero(self.rel == r)
            if R["kind"] == "contest":
                oc.append({"cells": to_runs(cells), "a": self.names[R["a"]], "b": self.names[R["b"]],
                           "since": R["since"], "war": R.get("war"), "n": int(cells.size)})
            elif R["kind"] == "occupation":
                oo.append({"cells": to_runs(cells), "owner": self.names[R["owner"]] if R["owner"] >= 0 else None,
                           "occupier": self.names[R["occupier"]], "since": R["since"], "n": int(cells.size)})
            else:
                ov.append({"vassal": self.names[R["vassal"]], "suzerain": self.names[R["suzerain"]],
                           "cells": to_runs(cells), "since": R["since"], "n": int(cells.size)})
                if R.get("colony"):
                    ov[-1]["colony"] = True
                if R.get("hierarchy"):
                    ov[-1]["hierarchy"] = R["hierarchy"]
            if R.get("ruling"):
                (oc if R["kind"] == "contest" else oo if R["kind"] == "occupation" else ov)[-1]["ruling"] = R["ruling"]
        return oc, oo, ov


# ----------------------------------------------------------------------------
# replay (self-check)
# ----------------------------------------------------------------------------

def load_anchor_state(path, n):
    with open(path, encoding="utf-8") as f:
        a = json.load(f)
    owner = np.full(n, None, object)
    status = np.full(n, "direct", object)
    extra = np.full(n, None, object)
    seen = np.zeros(n, np.int32)
    for s, runs in a["owners"].items():
        c = from_runs(runs)
        owner[c] = s
        seen[c] += 1
    status[owner == None] = "neutral"  # noqa: E711
    for st, groups in a.get("status", {}).items():
        for g in groups:
            c = from_runs(g["cells"])
            status[c] = st
            if st in ("vassal", "constituent"):
                extra[c] = g["suzerain"]
            elif st == "occupied":
                extra[c] = g["occupier"]
            else:
                extra[c] = g["claimants"][1]
    return owner, status, extra, int((seen > 1).sum()), a


def replay(stage, wins, n):
    """Replay every draft from the first anchor; compare with each later anchor."""
    out = {"anchors_checked": 0, "anchors_matching": 0, "mismatches": [], "double_owner_cells": 0,
           "from_mismatch_cells": 0, "cells_listed_twice_in_a_year": 0}
    first = stage / "data" / "anchors-c" / (wins[0]["start_anchor"] + ".json")
    owner, status, extra, dbl, _ = load_anchor_state(first, n)
    out["double_owner_cells"] += dbl
    for w in wins:
        with open(stage / "compiled" / "_draft" / (w["id"] + ".json"), encoding="utf-8") as f:
            draft = json.load(f)
        for y in sorted(draft["years"], key=int):
            seen = np.zeros(n, np.int8)
            for c in draft["years"][y]["changes"]:
                cells = from_runs(c["cells"])
                seen[cells] += 1
                bad = owner[cells] != np.array(c["from"], dtype=object)
                out["from_mismatch_cells"] += int(bad.sum())
                owner[cells] = c["to"]
                status[cells] = c["status"]
                if c["status"] in ("vassal", "constituent"):
                    extra[cells] = c["suzerain"]
                elif c["status"] == "occupied":
                    extra[cells] = c["occupier"]
                elif c["status"] == "contested":
                    extra[cells] = c["claimants"][1]
                else:
                    extra[cells] = None
            out["cells_listed_twice_in_a_year"] += int((seen > 1).sum())
        path = stage / "data" / "anchors-c" / (w["end_anchor"] + ".json")
        o2, s2, e2, dbl, _ = load_anchor_state(path, n)
        out["double_owner_cells"] += dbl
        out["anchors_checked"] += 1
        m = (o2 != owner) | (s2 != status) | (e2 != extra)
        if m.any():
            out["mismatches"].append((w["end_anchor"], int(m.sum())))
        else:
            out["anchors_matching"] += 1
    return out


# ----------------------------------------------------------------------------
# R1: data/colonies.csv (colony -> metropole, by years)
# ----------------------------------------------------------------------------

COLONY_FIELDS = ["colony", "metropole", "from", "to", "basis", "confidence"]

# nation -> (words in names and notes, slug prefixes, the home states that act as its metropole). Where
# two home states are alive at once (spanish-empire and kingdom-of-spain), the one listed first is the
# metropole unless another scores more than 1 point higher (Vichy and Free France in 1940-1944).
NATIONS = {
    "britain": (r"british|britain|english|england|united kingdom", ("british-", "english-", "anglo-"),
                ["kingdom-of-england", "kingdom-of-great-britain", "united-kingdom", "commonwealth-of-england"]),
    "france": (r"french|france", ("french-", "france-"),
               ["kingdom-of-france", "french-first-republic", "french-directory", "french-consulate",
                "first-french-empire", "bourbon-kingdom-of-france", "french-second-republic", "second-french-empire",
                "french-third-republic", "vichy-france", "free-french", "french-fourth-republic",
                "french-fifth-republic"]),
    "spain": (r"spanish|spain|castile|castilian", ("spanish-",),
              ["crown-of-castile", "spanish-empire", "kingdom-of-spain", "second-spanish-republic", "francoist-spain"]),
    "portugal": (r"portuguese|portugal", ("portuguese-",),
                 ["portuguese-empire", "kingdom-of-portugal", "portuguese-republic", "estado-novo", "portugal"]),
    "netherlands": (r"dutch|netherlands?|(?<!new )holland", ("dutch-",),
                    ["dutch-republic", "batavian-republic", "sovereign-principality-of-the-united-netherlands",
                     "netherlands", "first-french-empire"]),     # Holland was part of the French Empire 1810-1813
    "denmark": (r"danish|denmark", ("danish-",),
                ["kingdom-of-denmark", "denmark-norway", "kingdom-of-denmark-1814-1940", "denmark"]),
    "sweden": (r"swedish|sweden", ("swedish-",), ["swedish-empire", "kingdom-of-sweden"]),
    "prussia": (r"brandenburg|brandenburger|prussian|prussia", ("brandenburger-",),
                ["brandenburg-prussia", "kingdom-of-prussia", "north-german-confederation", "german-empire",
                 "weimar-republic"]),
    "germany": (r"german|germany", ("german-",),
                ["north-german-confederation", "german-empire", "weimar-republic", "nazi-germany"]),
    "italy": (r"italian|italy", ("italian-",), ["kingdom-of-italy", "republic-of-italy"]),
    "belgium": (r"belgian|belgium", ("belgian-",), ["kingdom-of-belgium"]),
    "russia": (r"russian|russia|muscovy|muscovite|soviet", ("russian-", "soviet-"),
               ["tsardom-of-russia", "russian-empire", "union-of-soviet-socialist-republics",
                "russian-soviet-federative-socialist-republic"]),
    "venice": (r"venetian|venice", ("venetian-",), ["republic-of-venice"]),
    "genoa": (r"genoese|genoa", (), ["republic-of-genoa"]),
    "usa": (r"united states(?! of the ionian)|u\.s\.", ("united-states-",), ["united-states-of-america"]),
    "japan": (r"japanese|japan", ("japanese-",), ["empire-of-japan"]),
    "austria": (r"austrian|austria|habsburg", ("habsburg-", "austrian-"),
                ["habsburg-monarchy", "austrian-empire", "austria-hungary"]),
    "ottoman": (r"ottoman", ("ottoman-",), ["ottoman-empire"]),
    "byzantium": (r"byzantine|eastern roman", ("byzantine-",), ["eastern-roman-empire", "byzantine-empire"]),
    "china": (r"han dynasty|eastern han|western han|tang dynasty|tang china|chinese|cao wei|western jin|jin dynasty",
              (), ["han-dynasty", "xin-dynasty", "cao-wei", "western-jin", "sui-dynasty", "tang-dynasty",
                   "ming-dynasty", "qing-dynasty"]),
    "mongol": (r"mongol|mongols|yuan", (), ["mongol-empire", "yuan-dynasty"]),
    "khitan": (r"khitan|liao", (), ["liao-dynasty"]),
    "persia": (r"achaemenid|persian|persia", (), ["achaemenid-empire"]),
    "assyria": (r"assyrian|assyria", ("assyrian-",), ["neo-assyrian-empire"]),
    "egypt": (r"egyptian|egypt|khedive|khedivate|muhammad ali", (),
              ["muhammad-ali-dynasty", "khedivate-of-egypt", "sultanate-of-egypt", "kingdom-of-egypt"]),
    "sicily": (r"norman|normans|sicily|sicilian", (), ["kingdom-of-sicily"]),
    "poland": (r"polish|poland", (), ["kingdom-of-poland", "house-of-jagiellon", "polish-lithuanian-commonwealth"]),
    "phoenicia": (r"phoenician|phoenicia|tyre|tyrian", ("phoenician-",), ["phoenicia"]),
    "hospitallers": (r"hospitaller|hospitallers|knights of st\.? john", ("hospitaller-",), ["hospitaller-rhodes"]),
}

# Rows fixed by hand where the derivation has nothing to go on or goes wrong: slug -> [(metropole or "",
# from, to, reason)]; they replace the derived rows for those years. Rows of data/colonies.csv whose basis
# starts with "manual" are kept the same way when the file is derived again.
COLONY_MANUAL = {
    "croton": [("", -710, -277, "medium", "a Greek apoikia, politically independent of its mother city (Achaea): no metropole")],
    "sybaris": [("", -720, -510, "medium", "a Greek apoikia, politically independent of its mother city (Achaea): no metropole")],
    "taras": [("", -706, -272, "medium", "a Greek apoikia, politically independent of its mother city (Sparta): no metropole")],
    "massalia": [("", -600, -49, "medium", "a Greek apoikia, politically independent of its mother city (Phocaea): no metropole")],
    "new-hebrides": [("", 1887, 1980, "medium", "Anglo-French joint rule (naval commission 1887, condominium 1906-1980): no single metropole")],
    "illyrian-provinces": [("first-french-empire", 1809, 1814, "high", "a province of the French Empire, 1809-1814")],
    "colony-of-nova-scotia": [("kingdom-of-great-britain", 1710, 1712, "high", "British from the capture of Port Royal (1710), ceded at Utrecht (1713)")],
    "colony-of-jamaica": [("commonwealth-of-england", 1655, 1659, "high", "taken from Spain by the Commonwealth's Western Design, 1655")],
    "kexholm-county": [("swedish-empire", 1617, 1618, "high", "ceded to Sweden at Stolbovo, 1617")],
    "pale-of-calais": [("kingdom-of-england", 1558, 1558, "high", "English until the French took Calais in January 1558")],
    "saint-domingue": [("kingdom-of-france", 1659, 1791, "high", "the French colony of western Hispaniola (ceded by Spain at Ryswick, 1697)")],
    "spanish-tunis": [("spanish-empire", 1535, 1574, "high", "Charles V's protectorate over Hafsid Tunis, 1535-1574")],
    "state-of-milan": [("spanish-empire", 1535, 1706, "high", "Spanish Milan until the Austrian occupation of 1706"),
                       ("habsburg-monarchy", 1707, 1796, "high", "Austrian Lombardy, 1707 (ceded 1714) to 1796")],
    "viceroyalty-of-naples": [("crown-of-aragon", 1504, 1515, "high", "Ferdinand II of Aragon's conquest, 1504"),
                              ("spanish-empire", 1516, 1706, "high", "Spanish Naples"),
                              ("habsburg-monarchy", 1707, 1734, "high", "Austrian Naples, 1707-1734")],
    "state-of-the-presidi": [("spanish-empire", 1557, 1706, "high", "Spanish garrisons on the Tuscan coast"),
                             ("habsburg-monarchy", 1707, 1735, "medium", "Austrian with Naples, 1707 (ceded 1714) to 1735"),
                             ("kingdom-of-naples-bourbon", 1736, 1801, "medium", "with Bourbon Naples from 1735")],
    "united-states-army-military-government-in-korea": [("united-states-of-america", 1945, 1948, "high", "the US Army's military government south of the 38th parallel")],
    "soviet-civil-administration": [("union-of-soviet-socialist-republics", 1945, 1948, "high", "the Soviet military administration north of the 38th parallel")],
    "territory-of-nauru": [("commonwealth-of-australia", 1920, 1968, "medium", "a League mandate held by Britain, Australia and New Zealand and administered by Australia")],
}

COLONY_MIN_SCORE = 2.5


def dossier_lives(dossiers):
    out = {}
    for s, d in dossiers.items():
        hd = any(e.get("type") == "dissolve" for e in d["ledger"])
        out[s] = (int(d["identity"]["start"]["year"]), int(d["identity"]["end"]["year"]) if hd else LAST_YEAR,
                  d["identity"]["type"])
    return out


def read_colonies_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({"colony": (r.get("colony") or "").strip(), "metropole": (r.get("metropole") or "").strip(),
                         "from": int(r["from"]), "to": int(r["to"]), "basis": r.get("basis") or "",
                         "confidence": (r.get("confidence") or "").strip()})
    return rows


HIER_KINDS = ("constituent", "vassal", "same_state")


def read_hierarchy_csv(path):
    """data/hierarchy.csv -> (rows [dict], issues [(line, child, parent, issue)])."""
    rows, issues = [], []
    with open(path, newline="", encoding="utf-8") as f:
        for n, r in enumerate(csv.DictReader(f), start=2):
            c, p = (r.get("child") or "").strip(), (r.get("parent") or "").strip()
            kind = (r.get("kind") or "").strip()
            try:
                fy, ty = int(r["from"]), int(r["to"])
            except (TypeError, ValueError, KeyError):
                issues.append((n, c, p, "bad years %r..%r" % (r.get("from"), r.get("to"))))
                continue
            try:
                conf = int(r.get("confidence") or 0)
            except ValueError:
                conf = 0
            if kind not in HIER_KINDS:
                issues.append((n, c, p, "unknown kind %r" % kind))
                continue
            if conf not in (1, 2, 3):
                issues.append((n, c, p, "confidence %r is not 1, 2 or 3; read as 1" % r.get("confidence")))
                conf = 1
            rows.append({"line": n, "child": c, "parent": p, "from": fy, "to": ty, "kind": kind, "confidence": conf})
    return rows, issues


def check_hierarchy(rows, lives, colonies):
    """R3 rows against the dossiers and data/colonies.csv -> (rows to apply [(child, parent, from, to, kind,
    confidence)], issues [(line, child, parent, issue)]). Spans are clipped to the years both dossiers are
    alive (umbrella dossiers move no cells), and a colony child's span loses the years colonies.csv covers
    (R1 keeps those)."""
    out, issues = [], []
    for r in rows:
        n, c, p, f, t, kind, conf = (r[k] for k in ("line", "child", "parent", "from", "to", "kind", "confidence"))
        bad = [s for s in (c, p) if s not in lives]
        if bad:
            issues.append((n, c, p, "no dossier with the slug %s" % ", ".join(bad)))
            continue
        if c == p:
            issues.append((n, c, p, "child and parent are the same dossier"))
            continue
        if f > t:
            issues.append((n, c, p, "from %d is after to %d" % (f, t)))
            continue
        um = [s for s in (c, p) if lives[s][2] == "umbrella"]
        if um:
            issues.append((n, c, p, "%s is an umbrella dossier (draws no cells)" % ", ".join(um)))
            continue
        f2, t2 = max(f, lives[c][0], lives[p][0]), min(t, lives[c][1], lives[p][1])
        if f2 > t2:
            issues.append((n, c, p, "%d..%d is outside the years both are alive (%d..%d, %d..%d)" % (
                f, t, lives[c][0], lives[c][1], lives[p][0], lives[p][1])))
            continue
        if (f2, t2) != (f, t):
            issues.append((n, c, p, "clipped to the years both are alive: %d..%d" % (f2, t2)))
        spans = [(f2, t2)]
        if kind != "same_state" and c in colonies:
            for cf, ct, _m, _conf in colonies[c]:
                nxt = []
                for a, b in spans:
                    if ct < a or cf > b:
                        nxt.append((a, b))
                        continue
                    if a < cf:
                        nxt.append((a, cf - 1))
                    if b > ct:
                        nxt.append((ct + 1, b))
                spans = nxt
            if spans != [(f2, t2)]:
                issues.append((n, c, p, "colony: years with a colonies.csv row stay with R1; left %s" % (
                    ", ".join("%d..%d" % s for s in spans) or "none")))
        for a, b in spans:
            out.append((c, p, a, b, kind, conf))
    return out, issues


def check_colonies(rows, lives):
    """data/colonies.csv against the dossiers -> ({colony slug: [(from, to, metropole slug or "", confidence)]},
    issues [(colony, from, to, issue)]). Rows are clipped to the colony's life and to the metropole's."""
    out = defaultdict(list)
    issues = []
    for r in rows:
        c, m, f, t = r["colony"], r["metropole"], r["from"], r["to"]
        if c not in lives:
            issues.append((c, f, t, "no dossier with this slug"))
            continue
        cs, ce, ct = lives[c]
        if ct != "colony":
            issues.append((c, f, t, "the dossier is type %s, not colony" % ct))
            continue
        f2, t2 = max(f, cs), min(t, ce)
        if f2 > t2:
            issues.append((c, f, t, "outside the colony's life %d..%d" % (cs, ce)))
            continue
        if m:
            if m not in lives:
                issues.append((c, f, t, "metropole %s has no dossier" % m))
                m = ""
            elif lives[m][2] in ("colony", "umbrella"):
                issues.append((c, f, t, "metropole %s is type %s (chain it to its sovereign)" % (m, lives[m][2])))
                m = ""
            else:
                ms, me, _ = lives[m]
                if ms > f2 or me < t2:
                    issues.append((c, f, t, "metropole %s alive %d..%d only: no metropole outside it" % (m, ms, me)))
                    if max(f2, ms) <= min(t2, me):
                        if f2 < ms:
                            out[c].append((f2, ms - 1, "", r["confidence"]))
                        if t2 > me:
                            out[c].append((me + 1, t2, "", r["confidence"]))
                        f2, t2 = max(f2, ms), min(t2, me)
                    else:
                        m = ""
        out[c].append((f2, t2, m, r["confidence"]))
    for c in out:
        out[c].sort()
        keep, last = [], None
        for row in out[c]:
            if last is not None and row[0] <= last:
                issues.append((c, row[0], row[1], "overlaps the row before it: ignored"))
                continue
            keep.append(row)
            last = row[1]
        out[c] = keep
    for c, (cs, ce, ct) in sorted(lives.items()):
        if ct == "colony" and c not in out:
            issues.append((c, cs, ce, "colony without a row in data/colonies.csv: no metropole"))
    return dict(out), issues


def _dossier_text(d):
    out = []

    def walk(v, key=None):
        if isinstance(v, str):
            if key not in ("source", "wikidata"):
                out.append(v)
        elif isinstance(v, dict):
            for k, x in v.items():
                if not str(k).startswith("_"):
                    walk(x, k)
        elif isinstance(v, list):
            for x in v:
                walk(x, key)
    walk(d)
    return "\n".join(out).lower()


def derive_colonies(inp, res, existing, debug=None):
    """Derive data/colonies.csv. For every colony dossier and year the candidate metropoles are scored:
      nation: the home states (NATIONS) of a nation named by the colony's slug or primary name, +3; else of
        a nation its notes name, +2 x (its count / the top count)^2, damped when the top count is under 3;
        plus +2.5 when the candidate shares the colony's colour family and that family holds one nation's
        home states only (britain, portugal, china...), +1.5 when it holds several (france: France, the
        Netherlands, Belgium).
      suzerain: the colony's suzerain in a first compile with the size rule only (a suzerain smaller than
        the colony, which is how a mis-recorded vassal_start reads, is ignored), +4.
      shape: the share of the colony's keyframe shape inside the candidate's keyframe shape that year,
        +2 at half or more (+1 for a state of no nation of the colony).
      mentions: +0.25 per mention of the candidate's names in the dossier, at most +1.
      lineage: a predecessor or the found counterpart of the colony's own nation, +0.5.
    A colony candidate (an aggregate such as british-colonial-empire, or a colony that is the suzerain)
    stands for its own metropole that year when that is of the colony's own nation. A successor born in
    the colony's last two years is not a candidate. The best metropole is kept when it scores
    COLONY_MIN_SCORE or more; of two home states of one nation alive at once the first listed is taken
    unless it trails by more than 1 point; the previous year's metropole is kept while it is alive and
    within 1 point of a metropole of another nation (no flicker). Confidence: high at 5 or more with a lead
    of 2 over the best metropole of another nation, medium at 3 with a lead of 1, else low. Rows of
    COLONY_MANUAL and manual rows of the existing file replace the derived years they cover.
    -> rows as dicts"""
    t0 = time.time()
    debug = set(debug or ())
    log("colonies: first compile (size rule only) for the suzerains")
    comp = Compiler(inp, res, rules=False, light=True)
    comp.run(set(), lambda y, w: None, lambda y: None, set())
    N, slugs = comp.N, comp.slugs
    sid = {s: i for i, s in enumerate(slugs)}      # dossiers only (comp.name_id also holds bare names)
    nat_re = {k: re.compile(r"\b(?:%s)\b" % v[0]) for k, v in NATIONS.items()}
    nat_sov = {}
    for k, v in NATIONS.items():
        nat_sov[k] = [sid[s] for s in v[2] if s in sid]
        missing = [s for s in v[2] if s not in sid]
        if missing:
            log("colonies: nation %s: no dossier for %s" % (k, ", ".join(missing)))
    sov_nat = defaultdict(set)
    for k, ids in nat_sov.items():
        for i in ids:
            sov_nat[i].add(k)
    kfl = {}

    def kflist(did):
        if did not in kfl:
            kfl[did] = [k for k in comp.keyframes(did) if k.get("from") is not None]
        return kfl[did]

    union_memo = {}

    def claim(did, y):
        key = tuple(k["j"] for k in kflist(did) if k["from"] <= y <= k["to"])
        if (did, key) not in union_memo:
            parts = [comp.keyframe_cells(did, k, y) for k in kflist(did) if k["j"] in key]
            parts = [p for p in parts if p is not None and p.size]
            union_memo[(did, key)] = np.unique(np.concatenate(parts)) if parts else None
        return key, union_memo[(did, key)]

    maxsize_memo = {}

    def maxsize(did):
        if did not in maxsize_memo:
            a = max([ar for f, t, ar in comp.clio_spans[did]] or [0])
            if a <= 0:
                for k in kflist(did):
                    c = comp.keyframe_cells(did, k, k["from"])
                    if c is not None:
                        a = max(a, c.size * CELL_KM2)
            maxsize_memo[did] = a
        return maxsize_memo[did]

    name_nat_memo = {}

    def name_nations(did):
        if did not in name_nat_memo:
            txt = (comp.dos[did]["identity"].get("name") or "").lower()   # alt names mislead (Île Saint-Jean (French))
            name_nat_memo[did] = {k for k, v in NATIONS.items()
                                  if any(slugs[did].startswith(p) for p in v[1]) or nat_re[k].search(txt)}
        return name_nat_memo[did]

    def nations_of(x):
        return name_nations(x) if comp.is_colony[x] else sov_nat.get(x, set())

    family = [d["identity"].get("family") or "" for d in comp.dos]
    fam_nat = defaultdict(set)      # colour family -> nations with a home state in it
    for k, ids in nat_sov.items():
        for i in ids:
            if family[i]:
                fam_nat[family[i]].add(k)

    # pass-1 suzerains of colonies
    suz = defaultdict(list)
    for R in comp.rels:
        if R["kind"] != "vassal" or R.get("colony"):
            continue
        v, s = R["vassal"], R["suzerain"]
        if v < N and s < N and comp.is_colony[v]:
            e = R["end"] if R["end"] is not None else LAST_YEAR
            if R["end"] is not None and e > R["since"]:
                e -= 1
            suz[v].append((s, R["since"], e))
    stop = {"kingdom", "empire", "republic", "dynasty", "sultanate", "colony", "state", "province", "the"}
    search = []
    for x in range(N):
        ident = comp.dos[x]["identity"]
        ns = {slugs[x]} if len(slugs[x]) >= 5 else set()
        for nm in [ident.get("name")] + list(ident.get("alt_names") or []) + list(ident.get("cliopatria_names") or []):
            if nm and len(nm) >= 5 and nm.lower() not in stop:
                ns.add(nm.lower())
        search.append(sorted(ns))
    info = {}

    def colony_info(c):
        if c in info:
            return info[c]
        d = comp.dos[c]
        text = _dossier_text(d)
        nn = name_nations(c)
        fam = set(fam_nat.get(family[c], ()))
        cs, ce = int(comp.start[c]), int(comp.end[c])
        lineage = set()
        for p in d["identity"].get("predecessors", []) or []:
            if p.get("slug") in sid:
                lineage.add(sid[p["slug"]])
        for e in d["ledger"]:
            if e.get("type") == "found" and e.get("counterpart") in sid:
                lineage.add(sid[e["counterpart"]])
        lineage.discard(c)
        counts = {k: len(nat_re[k].findall(text)) for k in NATIONS}
        top = max(counts.values()) if counts else 0
        # share of the most named nation, damped when the notes name it fewer than 3 times
        tn = {k: counts[k] / top * min(1.0, top / 3.0) for k in counts if top and counts[k] >= 0.3 * top}
        top_tn = {k for k in counts if top and counts[k] == top}
        own = (nn or top_tn) | (fam if len(fam) == 1 else set())
        late_succ = set()
        for s in d["identity"].get("successors", []) or []:
            x = sid.get(s.get("slug"))
            if x is not None and comp.start[x] >= ce - 1:
                late_succ.add(x)
        mentions = {}
        for x in range(N):
            if x == c or comp.umbrella[x] or comp.end[x] < cs or comp.start[x] > ce:
                continue
            m = sum(text.count(nm) for nm in search[x])
            if m:
                mentions[x] = m
        nations = nn | set(tn) | fam
        good_suz = {s for s, f, t in suz[c] if (sov_nat.get(s, set()) & nations) or comp.is_colony[s]
                    or maxsize(s) > maxsize(c)}
        cands = {x for x in lineage if nations_of(x) & own or not nations} | {x for x, m in mentions.items() if m >= 2}
        cands |= good_suz
        for k in nations:
            cands |= set(nat_sov[k])
        for x in range(N):
            if x != c and comp.is_colony[x] and comp.end[x] >= cs and comp.start[x] <= ce and (name_nations(x) & own):
                cands.add(x)
        cands = {x for x in cands if x != c and not comp.umbrella[x] and x not in late_succ}
        # a colony candidate must share the colony's own nation, or be its suzerain
        cands = {x for x in cands if not comp.is_colony[x] or (name_nations(x) & own) or x in good_suz}
        info[c] = {"nn": nn, "tn": tn, "fam": fam, "own": own, "nations": nations, "lineage": lineage,
                   "mentions": mentions, "cands": sorted(cands), "good_suz": good_suz}
        return info[c]

    def natw(c, x):
        ci = colony_info(c)
        ks = nations_of(x)
        w, why = 0.0, ""
        for k in ks:
            if k in ci["nn"] and 3 > w:
                w, why = 3.0, "named %s" % k
            elif k in ci["tn"] and 2 * ci["tn"][k] ** 2 > w:
                w, why = 2 * ci["tn"][k] ** 2, "its notes name %s (%.2f)" % (k, ci["tn"][k])
        if ks and family[x] and family[x] == family[c]:
            w += 2.5 if len(ci["fam"]) == 1 else 1.5
            why = (why + ", " if why else "") + "same colour family"
        return w, why

    frac_memo = {}
    memo = {}

    def year_scores(c, y, chain=True):
        """-> {metropole id: (score, why)} for the colony in year y. With chain, a colony candidate stands for
        its own metropole that year (found without chaining: one level)."""
        if (c, y, chain) in memo:
            return memo[(c, y, chain)]
        ci = colony_info(c)
        ckey, ccells = claim(c, y)
        if ccells is None:
            ckey, ccells = ("all",), None
            parts = [comp.keyframe_cells(c, k, y) for k in kflist(c)]
            parts = [p for p in parts if p is not None and p.size]
            if parts:
                ccells = np.unique(np.concatenate(parts))
        mask = None
        by_m = {}
        for x in ci["cands"]:
            if not comp.alive(x, y) or (comp.is_colony[x] and not chain):
                continue
            w, why = natw(c, x)
            s = w
            parts = [why] if why else []
            if x in ci["good_suz"] and any(s_ == x and f <= y <= t for s_, f, t in suz[c]):
                s += 4
                parts.append("its suzerain in a first compile")
            if ccells is not None:
                xkey, xcells = claim(x, y)
                fk = (c, ckey, x, xkey)
                if fk not in frac_memo:
                    if xcells is None:
                        frac_memo[fk] = 0.0
                    else:
                        if mask is None:
                            mask = np.zeros(comp.n, bool)
                            mask[ccells] = True
                        frac_memo[fk] = float(mask[xcells].sum()) / ccells.size
                fr = frac_memo[fk]
                if fr > 0.02:
                    cw = 2.0 if (w > 0 or not ci["nations"]) else 1.0
                    s += cw * min(1.0, 2 * fr)
                    parts.append("its shape holds %d%% of the colony's" % round(100 * fr))
            m = ci["mentions"].get(x, 0)
            if m:
                s += 0.25 * min(m, 4)
                parts.append("%d mention%s" % (m, "" if m == 1 else "s"))
            if x in ci["lineage"] and (w > 0 or not ci["nations"]):
                s += 0.5
                parts.append("predecessor or found counterpart")
            if s <= 0:
                continue
            final, via = x, ""
            if comp.is_colony[x]:
                sc = year_scores(x, y, False)
                if not sc:
                    continue
                mm = max(sc.items(), key=lambda kv: (kv[1][0], -kv[0]))
                if mm[1][0] < COLONY_MIN_SCORE:
                    continue
                if not (nations_of(mm[0]) & ci["own"]) and x not in ci["good_suz"]:
                    continue        # that colony's metropole is of another nation
                final, via = mm[0], " (via %s)" % slugs[x]
            if final == c:
                continue
            if final not in by_m or s > by_m[final][0]:
                by_m[final] = (s, "; ".join(parts) + via)
        memo[(c, y, chain)] = by_m
        if chain and (slugs[c], y) in debug:
            log("colonies debug %s %d: nations name %s text %s family %s" % (
                slugs[c], y, sorted(ci["nn"]), {k: round(v, 2) for k, v in ci["tn"].items()}, sorted(ci["fam"])))
            for m, (s, why) in sorted(by_m.items(), key=lambda kv: -kv[1][0])[:8]:
                log("    %-45s %.2f  %s" % (slugs[m], s, why))
        return by_m

    def conf_of(s, lead):
        if s >= 5 and lead >= 2:
            return "high"
        if s >= 3 and lead >= 1:
            return "medium"
        return "low"

    manual = defaultdict(list)
    for c, rows in COLONY_MANUAL.items():
        for m, f, t, conf, why in rows:
            manual[c].append({"colony": c, "metropole": m, "from": f, "to": t, "basis": "manual: " + why,
                              "confidence": conf})
    for r in existing:
        if r["basis"].startswith("manual") and r["colony"] not in COLONY_MANUAL:
            manual[r["colony"]].append(dict(r))
    rows = []
    rank = {"high": 2, "medium": 1, "low": 0}
    for c in range(N):
        if not comp.is_colony[c]:
            continue
        slug = slugs[c]
        cs, ce = int(comp.start[c]), int(comp.end[c])
        man = manual.get(slug, [])
        covered = set()
        for r in man:
            covered.update(range(max(r["from"], cs), min(r["to"], ce) + 1))
        seq = []
        prev = -1
        for y in range(cs, ce + 1):
            if y in covered:
                seq.append(None)
                prev = -1
                continue
            sc = year_scores(c, y)
            ranked = sorted(sc.items(), key=lambda kv: (-kv[1][0], slugs[kv[0]]))
            if not ranked or ranked[0][1][0] < COLONY_MIN_SCORE:
                best = ranked[0] if ranked else None
                why = ("the best candidate, %s, scores %.2f (%s)" % (slugs[best[0]], best[1][0], best[1][1])) \
                    if best else "no candidate"
                seq.append((-1, "low", best[1][0] if best else 0.0, 0.0, why, ""))
                prev = -1
                continue
            m, (s, why) = ranked[0]
            # the nation's first-listed home state alive that year, unless it trails by more than 1 point
            for k in sorted(sov_nat.get(m, ())):
                for p in nat_sov[k]:
                    if p == m:
                        break
                    if p in sc and sc[p][0] >= s - 1.0:
                        m, (s, why) = p, sc[p]
                        break
            if prev >= 0 and prev != m and prev in sc and sc[prev][0] >= s - 1.0 and sc[prev][0] >= COLONY_MIN_SCORE \
                    and not (nations_of(prev) & nations_of(m)):
                m, (s, why) = prev, sc[prev]        # no flicker between two nations
            # the lead is over the best metropole of another nation (two home states of one nation are
            # the same answer for the colony)
            others = [(o, v) for o, v in ranked if o != m and not (nations_of(o) & nations_of(m))]
            s2 = others[0][1][0] if others else 0.0
            ru = "%s %.2f" % (slugs[others[0][0]], s2) if others else "none"
            seq.append((m, conf_of(s, s - s2), s, s - s2, why, ru))
            prev = m
        i = 0
        out_c = [dict(r) for r in man]
        while i < len(seq):
            if seq[i] is None:
                i += 1
                continue
            j = i
            while j + 1 < len(seq) and seq[j + 1] is not None and seq[j + 1][0] == seq[i][0]:
                j += 1
            run = seq[i:j + 1]
            confs = Counter(r[1] for r in run)
            conf = sorted(confs, key=lambda k: (-confs[k], rank[k]))[0]
            mid = run[len(run) // 2]
            m = mid[0]
            if m >= 0:
                basis = "%s; score %.2f, lead %.2f; next: %s" % (mid[4], mid[2], mid[3], mid[5])
            else:
                basis = "no metropole: %s" % mid[4]
            out_c.append({"colony": slug, "metropole": slugs[m] if m >= 0 else "", "from": cs + i, "to": cs + j,
                          "basis": basis, "confidence": conf})
            i = j + 1
        rows.extend(sorted(out_c, key=lambda r: r["from"]))
    log("colonies: %d rows for %d colony dossiers in %.0f s" % (len(rows), int(comp.is_colony.sum()), time.time() - t0))
    return rows


# ----------------------------------------------------------------------------
# driver
# ----------------------------------------------------------------------------

def collect_specs(dossiers):
    specs = []
    for d in dossiers.values():
        for e in d.get("ledger", []):
            if isinstance(e.get("region"), dict):
                specs.append(e["region"])
        for k in d.get("keyframe_review", []):
            if isinstance(k.get("correction"), dict):
                specs.append(k["correction"])
        for h in (d["identity"].get("successors", []) or []):
            if isinstance(h.get("land"), dict):
                specs.append(h["land"])
    return specs


def leaf_label(key):
    try:
        s = json.loads(key)
    except Exception:  # noqa: BLE001
        return ("?", key)
    if not isinstance(s, dict):
        return ("?", key)
    k = _leaf_kind(s)
    if k == "region":
        return ("region", s["region"])
    if k == "admin1":
        return ("admin1", "%s (%s)" % (s.get("admin1"), s.get("country")))
    if k == "place":
        return ("place", s["place"] + ((" (%s)" % s["country"]) if s.get("country") else ""))
    if k == "country":
        return ("country", s["country"])
    if k == "cliopatria":
        return ("cliopatria", s["cliopatria"])
    if k == "river":
        return ("river", s["river"])
    if k == "lake":
        return ("lake", s["lake"])
    if k == "border_band":
        bb = s["border_band"]
        return ("border_band", "%s|%s" % (bb.get("a"), bb.get("b")))
    return (k, key[:120])


# ----------------------------------------------------------------------------
# data/patches/<window>.json: the window agents' corrections (see data/patches/README.md)
# ----------------------------------------------------------------------------

PATCH_KINDS = ("events", "keyframe_overrides", "rulings")
PATCH_NO_TYPES = ("found", "dissolve")      # a state's life belongs to its dossier
RULING_STATUS = {"vassal": VASSAL, "constituent": CONSTITUENT, "occupied": OCCUPIED, "contested": CONTESTED}
RULING_KEYS = {"years", "a", "b", "winner", "status", "suzerain", "region", "source", "why"}


def patch_ref(w, kind, k):
    return "data/patches/%s.json: %s/%d" % (w, kind, k)


def patch_files(pdir, override=None):
    """The patch files of a folder in window order; `override` (a file named <window>.json) replaces that
    window's file."""
    files = sorted((q for q in pdir.glob("*.json") if not q.name.startswith("_")), key=_window_key) if pdir and pdir.is_dir() else []
    if override is not None:
        files = sorted([q for q in files if q.stem != override.stem] + [override], key=_window_key)
    return files


def _window_key(q):
    """Chronological window order: m1300-m1201 (start -1300) before m1200-m1101; a plain name sort put the
    later BCE window first (seam round sm-01, 3 Nov 2026)."""
    m = re.match(r"([mp])(\d+)-", q.stem)
    return ((-1 if m.group(1) == "m" else 1) * int(m.group(2)), q.stem) if m else (10 ** 6, q.stem)


def load_patches(pdir, inp, res, wins, files=None, known=None):
    """Read data/patches/<window>.json; check every entry as tools/validate_dossier.py checks a dossier (the
    schema of a ledger event or keyframe_review entry, then the semantic checks that apply), region specs
    through the gazetteer; put the good events and keyframe overrides into the in-memory dossiers and
    return the good rulings. A bad entry is reported and skipped, a bad file too.
    -> (rulings [dict], report rows [[window, kind, index, slug, outcome, message]], counts)"""
    import validate_dossier as V
    rows, rulings, counts = [], [], Counter()
    if files is None:
        files = patch_files(pdir)
    if not files:
        return rulings, rows, counts
    win = {w["id"]: w for w in wins}
    with open(V.SCHEMA_PATH, encoding="utf-8") as f:
        schema = json.load(f)
    defs = schema.get("$defs", {})

    def sub(node):
        out = dict(node)
        out["$defs"] = defs
        return out

    ev_schema = sub(schema["properties"]["ledger"]["items"])
    kf_schema = sub(schema["properties"]["keyframe_review"]["items"])
    reg_schema = sub({"$ref": "#/$defs/region"})
    url_schema = sub({"$ref": "#/$defs/url"})
    shapes = V.load_shapes() or {}
    D = inp.dossiers
    entries = []
    for q in files:
        w = q.stem
        counts["files"] += 1
        if w not in win:
            rows.append([w, "file", "", "", "skipped", "%s: the file name is not a window id (data/patches/<window>.json, "
                         "such as p1200-p1299.json or p1910-p1919.json)" % q.name])
            counts["files skipped"] += 1
            continue
        try:
            with open(q, encoding="utf-8") as f:
                doc = json.load(f)
        except Exception as e:  # noqa: BLE001
            rows.append([w, "file", "", "", "skipped", "not readable as JSON: %s" % e])
            counts["files skipped"] += 1
            continue
        if not isinstance(doc, dict):
            rows.append([w, "file", "", "", "skipped", "the file must hold one JSON object"])
            counts["files skipped"] += 1
            continue
        other = sorted(k for k in doc if k not in PATCH_KINDS and k not in ("window", "note"))
        if other:
            rows.append([w, "file", "", "", "note", "keys ignored: %s" % ", ".join(other)])
        if doc.get("window") not in (None, w):
            rows.append([w, "file", "", "", "note", "\"window\" says %r; the file name decides" % doc.get("window")])
        for kind in PATCH_KINDS:
            lst = doc.get(kind, [])
            if not isinstance(lst, list):
                rows.append([w, kind, "", "", "skipped", "%s must be a list" % kind])
                continue
            for k, e in enumerate(lst):
                entries.append((w, kind, k, e))
    specs = [e[key] for (_w, _kd, _k, e) in entries if isinstance(e, dict)
             for key in ("region", "correction") if isinstance(e.get(key), dict)]
    if specs:
        res.prepare(specs)

    def fmt(errs):
        return "; ".join("%s: %s" % (a or "/", b) for a, b in list(errs)[:3])

    def region_cells(spec):
        cells, errs = res.resolve(spec)
        if errs:
            return None, "region does not resolve through the gazetteer: " + "; ".join(e for _, e in errs)[:300]
        return cells, ""

    kf_taken = {}
    for (w, kind, k, e) in entries:
        W = win[w]
        slug = e.get("slug") if isinstance(e, dict) else None
        slug = slug if isinstance(slug, str) else ""

        def bad(msg):
            rows.append([w, kind, k, slug, "skipped", msg])
            counts[kind + " skipped"] += 1

        if not isinstance(e, dict):
            bad("an entry must be a JSON object")
            continue
        notes_ = []
        if kind in ("events", "keyframe_overrides"):
            d = D.get(slug)
            if d is None:
                bad("slug %r is not a compiled dossier (no such dossier, or it fails tools/validate_dossier.py)" % (slug or None))
                continue
            s0, e0 = d["identity"]["start"]["year"], d["identity"]["end"]["year"]
        if kind == "events":
            ev = {a: b for a, b in e.items() if a != "slug"}
            errs = V.schema_errors(ev, ev_schema)
            if errs:
                bad("schema (a ledger event plus slug): " + fmt(errs))
                continue
            if ev["type"] in PATCH_NO_TYPES:
                bad("type %s cannot be patched: a state's life (found, dissolve) belongs to its dossier" % ev["type"])
                continue
            if not s0 <= ev["year"] <= e0:
                bad("year %d lies outside the state's life %d..%d" % (ev["year"], s0, e0))
                continue
            if isinstance(ev.get("region"), dict):
                cells, msg = region_cells(ev["region"])
                if cells is None:
                    bad(msg)
                    continue
                if cells.size == 0 and ev["type"] not in ("contest_end", "occupation_end", "vassal_end"):
                    notes_.append("the region holds no land cell (the event will move nothing)")
            if not W["from"] <= ev["year"] <= W["to"]:
                notes_.append("year %d is outside the window %d..%d" % (ev["year"], W["from"], W["to"]))
            cp = ev.get("counterpart")
            if isinstance(cp, str) and V.SLUG_RE.match(cp) and cp != "nobody" and cp not in (D if known is None else known):
                notes_.append("counterpart %r looks like a slug but no compiled dossier has it" % cp)
            ev["_patch"], ev["_patch_k"] = w, k
            d["ledger"].append(ev)
        elif kind == "keyframe_overrides":
            kf = {a: b for a, b in e.items() if a not in ("slug", "why")}
            if "why" in e:
                kf["note"] = e["why"]
            sid = kf.get("shape_id")
            kr = d.setdefault("keyframe_review", [])
            old_j = next((j for j, x in enumerate(kr) if x.get("shape_id") == sid), None)
            if old_j is not None:
                for a in ("from", "to"):
                    if a not in kf and a in kr[old_j]:
                        kf[a] = kr[old_j][a]
            errs = V.schema_errors(kf, kf_schema)
            if errs:
                bad("schema (a keyframe_review entry plus slug, why for note): " + fmt(errs))
                continue
            own = {slug}
            if V.slugify:
                own |= {V.slugify(n) for n in d["identity"].get("cliopatria_names") or [] if isinstance(n, str)}
            kslug = sid.rsplit("_", 1)[0]
            if kslug not in own:
                bad("shape %r does not belong to this dossier (%s)" % (sid, ", ".join(sorted(own))))
                continue
            new_shape = sid not in shapes.get(kslug, [])
            if new_shape and not (isinstance(kf.get("from"), int) and isinstance(kf.get("to"), int)):
                bad("shape %r is not in data/shapes.csv, so it is a new keyframe and needs from and to" % sid)
                continue
            if new_shape and "correction" not in kf:
                bad("a new keyframe needs a correction describing the shape")
                continue
            if isinstance(kf.get("correction"), dict):
                cells, msg = region_cells(kf["correction"])
                if cells is None:
                    bad("correction: " + msg)
                    continue
            if (slug, sid) in kf_taken:
                bad("keyframe already overridden by %s (the first file in window order wins)" % kf_taken[(slug, sid)])
                continue
            sh = inp.shapes.get(sid)
            fy, ty = kf.get("from", sh[0] if sh else None), kf.get("to", sh[1] if sh else None)
            if fy is not None and ty is not None and (ty < W["from"] or fy > W["to"]):
                notes_.append("the keyframe's years %d..%d lie outside the window %d..%d" % (fy, ty, W["from"], W["to"]))
            kf["_patch"], kf["_patch_k"] = w, k
            if old_j is None:
                kr.append(kf)
                notes_.append("added: the dossier had no entry for this shape")
            else:
                kr[old_j] = kf
            kf_taken[(slug, sid)] = patch_ref(w, kind, k)
        else:
            slug = "%s|%s" % (e.get("a"), e.get("b"))
            extra = sorted(set(e) - RULING_KEYS)
            if extra:
                bad("unknown keys: %s" % ", ".join(extra))
                continue
            yrs = e.get("years")
            if not (isinstance(yrs, list) and len(yrs) == 2 and all(isinstance(v, int) and not isinstance(v, bool) for v in yrs)
                    and yrs[0] <= yrs[1]):
                bad("years must be [first, last]: two integers, first <= last")
                continue
            a, b, winner = e.get("a"), e.get("b"), e.get("winner")
            miss = [x for x in (a, b) if x not in D]
            if miss:
                bad("%s: not a compiled dossier" % ", ".join(repr(x) for x in miss))
                continue
            if a == b:
                bad("a and b are the same dossier")
                continue
            if winner not in (a, b):
                bad("winner must be a or b")
                continue
            st, suz = e.get("status"), e.get("suzerain")
            if st is not None and st not in RULING_STATUS:
                bad("status must be one of %s" % ", ".join(RULING_STATUS))
                continue
            if st in ("vassal", "constituent", "occupied"):
                if suz not in D or suz == winner:
                    bad("status %s needs suzerain: a compiled dossier other than the winner (for occupied, the occupier)" % st)
                    continue
            elif suz is not None:
                notes_.append("suzerain is ignored without status vassal, constituent or occupied")
            cells = None
            if "region" in e:
                errs = V.schema_errors(e["region"], reg_schema)
                if errs:
                    bad("region (the region grammar): " + fmt(errs))
                    continue
                cells, msg = region_cells(e["region"])
                if cells is None:
                    bad(msg)
                    continue
                if cells.size == 0:
                    bad("the region holds no land cell")
                    continue
            errs = V.schema_errors(e.get("source"), url_schema)
            if errs:
                bad("source must be the http(s) URL of the page the ruling rests on")
                continue
            if not isinstance(e.get("why"), str) or not e["why"].strip():
                bad("why: a sentence saying why is required")
                continue
            if yrs[1] < W["from"] or yrs[0] > W["to"]:
                notes_.append("years %d..%d lie outside the window %d..%d" % (yrs[0], yrs[1], W["from"], W["to"]))
            lo = max(yrs[0], D[a]["identity"]["start"]["year"], D[b]["identity"]["start"]["year"])
            hi = min(yrs[1], D[a]["identity"]["end"]["year"], D[b]["identity"]["end"]["year"])
            if lo > hi:
                notes_.append("a and b are never both alive in these years: the ruling can settle nothing")
            rulings.append({"id": "%s/rulings/%d" % (w, k), "window": w, "k": k, "a": a, "b": b, "winner": winner,
                            "from": yrs[0], "to": yrs[1], "status": st, "suzerain": suz,
                            "cells": None if cells is None else np.sort(cells), "why": e["why"].strip(),
                            "source": e.get("source"), "row": len(rows)})
        rows.append([w, kind, k, slug, "applied", "; ".join(notes_)])
        counts[kind + " applied"] += 1
    return rulings, rows, counts


# ----------------------------------------------------------------------------
# a window agent's own checks: --check-patch and --trial
# ----------------------------------------------------------------------------

def patch_target(arg, patch_dir):
    """WINDOW or a file named <window>.json -> (window id, the file to use instead of the folder's, or None)."""
    if arg.endswith(".json") or os.sep in arg:
        q = Path(arg).resolve()
        if q.parent == patch_dir.resolve():
            return q.stem, None
        return q.stem, q
    return arg, None


class _PatchInputs:
    """What load_patches needs, for a few dossiers read straight from the shared folder."""
    def __init__(self, dossiers, shapes):
        self.dossiers, self.shapes = dossiers, shapes


def check_patch(arg, hist, patch_dir):
    """Check one patch file as a compile would, without compiling. Prints a line per entry and a summary;
    -> exit code 0 when every entry is applied."""
    import validate_dossier as V
    t0 = time.time()
    global CACHE_WRITE
    CACHE_WRITE = None                     # read the shared region cache, write nothing
    wid, override = patch_target(arg, patch_dir)
    path = override if override is not None else patch_dir / (wid + ".json")
    if not path.exists():
        print("no patch file %s" % path)
        return 2
    try:
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)
    except Exception:  # noqa: BLE001
        doc = {}
    refs = set()
    for kind in PATCH_KINDS:
        for e in (doc.get(kind) or []) if isinstance(doc, dict) else []:
            if isinstance(e, dict):
                for k in ("slug", "a", "b", "winner", "suzerain"):
                    if isinstance(e.get(k), str):
                        refs.add(e[k])
    with open(V.SCHEMA_PATH, encoding="utf-8") as f:
        schema = json.load(f)
    vshapes, known = V.load_shapes(), V.load_known_slugs()
    dossiers, failing = {}, {}
    for s in sorted(refs):
        q = hist / "polities" / (s + ".json")
        if not q.exists() or s.startswith("_"):
            continue
        try:
            with open(q, encoding="utf-8") as f:
                d = json.load(f)
            errs = list(V.schema_errors(d, schema)) + list(V.semantic_checks(d, str(q), vshapes, known, False)[0])
        except Exception as e:  # noqa: BLE001
            errs = [("", "%s: %s" % (type(e).__name__, e))]
        if errs:
            failing[s] = "; ".join("%s: %s" % (a or "/", b) for a, b in errs[:2])
            continue
        d["identity"]["start"]["year"] = int(d["identity"]["start"]["year"])
        d["identity"]["end"]["year"] = int(d["identity"]["end"]["year"])
        dossiers[s] = d
    shapes = {}
    with open(hist / "data" / "shapes.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            shapes[r["shape_id"]] = (int(r["from_year"]), int(r["to_year"]), float(r["area_km2"]))
    res = Resolver(hist, workers=1)
    rulings, rows, counts = load_patches(None, _PatchInputs(dossiers, shapes), res, windows(), files=[path],
                                         known=known)
    bad = 0
    for w, kind, k, slug, outcome, msg in rows:
        where = kind if k == "" else "%s/%s" % (kind, k)
        if outcome == "applied":
            print("%-24s %-40s ok%s" % (where, slug, (" (note: %s)" % msg) if msg else ""))
        elif outcome == "note":
            print("%-24s %-40s note: %s" % (where, slug, msg))
        else:
            bad += 1
            print("%-24s %-40s REJECTED: %s" % (where, slug, msg))
    for s, why in sorted(failing.items()):
        print("note: dossier %s fails tools/validate_dossier.py, so it is not compiled: %s" % (s, why[:300]))
    n = sum(1 for r in rows if r[1] in PATCH_KINDS and r[2] != "")
    print("%s: %d entries, %d ok, %d rejected; checked in %.1f s%s" % (
        path, n, n - sum(1 for r in rows if r[4] == "skipped" and r[2] != ""), bad, time.time() - t0,
        "" if bad == 0 else " (rejected entries are skipped by the compile)"))
    return 0 if bad == 0 else 1


def _draft_digest(path):
    """A draft's conflicts by pair and its snaps -> ({pair: [cells, years, {winner: cells}, rules]}, {snap: (a, r, k)})"""
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    pairs = {}
    for c in d["handoff"].get("conflicts", []):
        k = tuple(sorted(str(x) for x in c["claimants"]))
        P = pairs.setdefault(k, [0, set(), Counter(), set()])
        P[0] += c["n"]
        P[1].add(c["year"])
        P[2][c["resolved_to"]] += c["n"]
        P[3].add(c["rule"].split(":")[0].split(" (")[0][:40])
    snaps = {(s_["slug"], s_["shape_id"], s_["year"]): (s_["added"], s_["removed"], s_["kept_by_others"])
             for s_ in d["handoff"].get("keyframe_snaps", [])}
    return pairs, snaps


def trial_finish(comp, inp, hist, stage, w, t_all):
    """A trial's outputs (the window's draft is written already): patches_check.csv, the packet, and a short
    comparison with the published draft printed."""
    import resource
    notes = stage / "notes" / "phase-c"
    prow = write_patches_check(comp, notes)
    write_window_packets(comp, inp, hist, notes, [w], prow)
    out = []
    out.append("trial %s: compiled %d..%d into %s" % (w["id"], FIRST_YEAR, comp.until, stage))
    mine = [r for r in prow if r[0] == w["id"]]
    out.append("patch entries of %s: %d" % (w["id"], len(mine)))
    for r in mine:
        where = r[1] if r[2] == "" else "%s/%s" % (r[1], r[2])
        out.append("  %-24s %-36s %s%s" % (where, r[3], r[4], (": " + r[5]) if r[5] else ""))
    others = [r for r in prow if r[0] != w["id"]]
    if others:
        out.append("other windows' patch entries: %d applied, %d skipped" % (
            sum(1 for r in others if r[4] == "applied"), sum(1 for r in others if r[4] == "skipped")))
    pub = hist / "compiled" / "_draft" / (w["id"] + ".json")
    new = stage / "compiled" / "_draft" / (w["id"] + ".json")
    if pub.exists():
        when = time.strftime("%Y-%m-%d %H:%M", time.localtime(pub.stat().st_mtime))
        p0, s0 = _draft_digest(pub)
        p1, s1 = _draft_digest(new)
        out.append("against the published draft (%s; dossier edits since then show here too):" % when)
        out.append("  conflicts: %d pairs, %d cell-years -> %d pairs, %d cell-years" % (
            len(p0), sum(v[0] for v in p0.values()), len(p1), sum(v[0] for v in p1.values())))

        def desc(v):
            if v is None:
                return "none"
            win = "; ".join("%s %d" % kv for kv in v[2].most_common(2))
            return "%d cell-years in %d years (won: %s; %s)" % (v[0], len(v[1]), win, ", ".join(sorted(v[3])))
        ch = []
        for k in set(p0) | set(p1):
            a, b = p0.get(k), p1.get(k)
            if a is None or b is None or a[0] != b[0] or a[2] != b[2] or a[3] != b[3]:
                ch.append((abs((a[0] if a else 0) - (b[0] if b else 0)) + (a[0] if a else 0), k, a, b))
        ch.sort(key=lambda x: (-x[0], x[1]))
        for _, k, a, b in ch[:10]:
            out.append("    %s / %s: %s -> %s" % (k[0], k[1], desc(a), desc(b)))
        if len(ch) > 10:
            out.append("    ... and %d more pairs changed" % (len(ch) - 10))
        out.append("  keyframe snaps: %d -> %d" % (len(s0), len(s1)))
        sc = []
        for k in set(s0) | set(s1):
            a, b = s0.get(k), s1.get(k)
            if a != b:
                sc.append(((sum(a[:2]) if a else 0) + (sum(b[:2]) if b else 0), k, a, b))
        sc.sort(key=lambda x: (-x[0], x[1]))
        for _, k, a, b in sc[:8]:
            f = lambda v: "none" if v is None else "added %d removed %d kept by others %d" % v  # noqa: E731
            out.append("    %s %s %d: %s -> %s" % (k[0], k[1], k[2], f(a), f(b)))
        if len(sc) > 8:
            out.append("    ... and %d more snaps changed" % (len(sc) - 8))
        pa = hist / "data" / "anchors-c" / (w["end_anchor"] + ".json")
        na = stage / "data" / "anchors-c" / (w["end_anchor"] + ".json")
        if pa.exists() and na.exists():
            o0, st0, e0, _d, _a = load_anchor_state(pa, comp.n)
            o1, st1, e1, _d, _a = load_anchor_state(na, comp.n)
            out.append("  end anchor %s: %d cells change owner, %d more change status or suzerain" % (
                w["end_anchor"], int((o0 != o1).sum()), int(((o0 == o1) & ((st0 != st1) | (e0 != e1))).sum())))
    else:
        out.append("no published draft %s to compare with" % pub)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    out.append("wrote %s, %s, %s and the anchors %s, %s; %.0f s, memory peak %.0f MB" % (
        new, notes / "patches_check.csv", notes / "windows" / (w["id"] + ".md"),
        w["start_anchor"], w["end_anchor"], time.time() - t_all, peak))
    print("\n".join(out))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hist", default=str(DEFAULT_HIST))
    ap.add_argument("--until", type=int, default=LAST_YEAR)
    ap.add_argument("--compare", default="1600,1900")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--no-sync", action="store_true")
    ap.add_argument("--stage-only", action="store_true")
    ap.add_argument("--build-colonies", action="store_true",
                    help="derive data/colonies.csv again (rows whose basis starts with 'manual' are kept)")
    ap.add_argument("--no-rules", action="store_true", help="size rule only (no R1, no R2), for comparison")
    ap.add_argument("--patches", default=None, help="the patches folder (default: <hist>/data/patches)")
    ap.add_argument("--check-patch", metavar="WINDOW|FILE",
                    help="check one patch file (data/patches/<window>.json, or a file named <window>.json) and stop")
    ap.add_argument("--trial", metavar="WINDOW|FILE",
                    help="compile up to that window's last year with every patch file (FILE replacing the window's "
                         "own) into --stage DIR only; never publishes")
    ap.add_argument("--stage", metavar="DIR", help="the private folder of a --trial")
    args = ap.parse_args(argv)
    if args.stage and not args.trial:
        ap.error("--stage DIR goes with --trial WINDOW (without --trial the compile publishes)")
    t_all = time.time()
    hist = Path(args.hist)
    sys.path.insert(0, str(hist / "tools"))
    patch_dir = Path(args.patches) if args.patches else hist / "data" / "patches"
    if args.check_patch:
        return check_patch(args.check_patch, hist, patch_dir)
    trial = None
    global CACHE_READ, CACHE_WRITE, GRID_READONLY
    if args.trial:
        if not args.stage:
            ap.error("--trial needs --stage DIR")
        wid, override = patch_target(args.trial, patch_dir)
        trial = next((w for w in windows() if w["id"] == wid), None)
        if trial is None:
            ap.error("%s is not a window id (such as p1200-p1299 or p1910-p1919)" % wid)
        stage = Path(args.stage).resolve()
        hr = hist.resolve()
        if stage == hr or hr in stage.parents or stage in hr.parents or args.build_colonies:
            ap.error("--stage must be a private folder outside %s (and --trial never derives colonies.csv)" % hist)
        args.until = min(trial["to"], LAST_YEAR)
        args.stage_only = True
        CACHE_READ = [stage / "cache", WORK / "cache"]
        CACHE_WRITE = stage / "cache"
        GRID_READONLY = True
        dossier_dir = stage / "polities"
        if not dossier_dir.exists() and (WORK / "polities").is_dir():
            # start from the local copy (same mtimes), then copy only what changed on the mount
            t = time.time()
            dossier_dir.mkdir(parents=True)
            for e in os.scandir(WORK / "polities"):
                if e.name.endswith(".json"):
                    shutil.copy2(e.path, dossier_dir / e.name)
            log("dossiers seeded from %s, %.0f s" % (WORK / "polities", time.time() - t))
    else:
        override = None
        WORK.mkdir(parents=True, exist_ok=True)
        dossier_dir = WORK / "polities"
    if not args.no_sync:
        t = time.time()
        n, copied, removed = sync_dossiers(hist / "polities", dossier_dir)
        log("dossiers synced: %d files, %d copied, %d removed, %.0f s" % (n, copied, removed, time.time() - t))
    inp = Inputs(hist, dossier_dir)
    res = Resolver(hist, workers=args.workers, refresh=args.refresh)
    # data/patches/<window>.json: events and keyframe overrides go into the dossiers (in memory), rulings
    # into the conflict rule
    rulings, patch_rows, patch_counts = load_patches(patch_dir, inp, res, windows(),
                                                     files=patch_files(patch_dir, override))
    log("patches: %s" % (dict(patch_counts) or "none"))
    res.prepare(collect_specs(inp.dossiers))
    full = args.until >= LAST_YEAR and trial is None
    if trial is None:
        stage = WORK / ("stage" if full else "stage-test")
        if stage.exists():
            shutil.rmtree(stage)
    for sub in ("data/anchors-c", "compiled/_draft"):
        (stage / sub).mkdir(parents=True, exist_ok=True)
        for q in (stage / sub).glob("*.json"):       # a trial's earlier outputs (its own subfolders only)
            q.unlink()
    (stage / "notes" / "phase-c" / "windows").mkdir(parents=True, exist_ok=True)
    # R1: data/colonies.csv, derived when missing or asked for, else read (and checked) as it is
    lives = dossier_lives(inp.dossiers)
    col_path = hist / "data" / "colonies.csv"
    existing = read_colonies_csv(col_path) if col_path.exists() else []
    col_built = bool(args.build_colonies or not col_path.exists())
    if col_built:
        col_rows = derive_colonies(inp, res, existing)
        write_csv(stage / "data" / "colonies.csv", COLONY_FIELDS, [[r[k] for k in COLONY_FIELDS] for r in col_rows])
    else:
        col_rows = existing
    colonies, col_issues = check_colonies(col_rows, lives)
    for iss in col_issues[:20]:
        log("colonies.csv: %s %s..%s: %s" % iss)
    # R3: data/hierarchy.csv, read and checked as it is
    hier_path = hist / "data" / "hierarchy.csv"
    raw, hier_rows, hier_issues = [], [], []
    if hier_path.exists() and not args.no_rules:
        raw, hier_issues = read_hierarchy_csv(hier_path)
        hier_rows, more = check_hierarchy(raw, lives, colonies)
        hier_issues += more
        log("hierarchy.csv: %d rows read, %d spans to apply, %d notes" % (len(raw), len(hier_rows), len(hier_issues)))
    comp = Compiler(inp, res, until=min(args.until, LAST_YEAR), stage=stage,
                    colonies=None if args.no_rules else colonies, rules=not args.no_rules, hierarchy=hier_rows,
                    rulings=rulings)
    comp.patch_rows, comp.patch_counts, comp.patch_dir = patch_rows, patch_counts, patch_dir
    t = time.time()
    comp.adm = admin1_lookup(hist, comp.n)
    log("admin-1 lookup: %d labels, %.1f s" % (len(comp.adm[1]), time.time() - t))
    comp.hier_info_out = {"rows_read": len(raw), "spans": len(hier_rows),
                          "issues": sorted(hier_issues),
                          "spans_by_kind": dict(Counter("%s, confidence %d" % (k, c) for _a, _b, _f, _t, k, c in hier_rows))}
    conf = Counter(r["confidence"] for r in col_rows)
    comp.colony_info_out = {
        "built_this_run": col_built, "rows": len(col_rows), "colonies": len({r["colony"] for r in col_rows}),
        "rows_by_confidence": dict(conf), "rows_without_metropole": sum(1 for r in col_rows if not r["metropole"]),
        "low_rows": [(r["colony"], r["metropole"], r["from"], r["to"], r["basis"]) for r in col_rows
                     if r["confidence"] == "low"],
        "issues": col_issues, "rules": not args.no_rules}
    wins = windows()
    anchor_years = {w["from"] for w in wins}
    window_ends = {w["to"]: w for w in wins}
    anchors_written = {}
    area_rows = []

    def add_area_rows(name, ay, snap):
        for slug, runs in snap["owners"].items():
            did = comp.name_id[slug]
            cells = int(sum((int(r.split("-")[1]) - int(r.split("-")[0]) + 1) if isinstance(r, str) else 1 for r in runs))
            clio = comp.clio_area(did, ay)
            area_rows.append((name, ay, slug, cells, round(cells * CELL_KM2, 1), round(clio, 1),
                              round(cells * CELL_KM2 / clio, 4) if clio else ""))

    def on_anchor(y, when):
        if when == "start":
            comp.window_start(y)
        if trial is not None:
            # a trial writes the window's start and end anchors only
            if (when == "start" and y == trial["from"]) or when == "end":
                name = stem(y) if when == "start" else trial["end_anchor"]
                snap = comp.snapshot(y, "1 January %d (after every event dated %d or earlier)" % (y, y - 1))
                write_json(stage / "data" / "anchors-c" / (name + ".json"), snap)
            return
        if when == "start" or not full:
            # 1 January of y (also the end of a test run, y = until + 1)
            snap = comp.snapshot(y, "1 January %d (after every event dated %d or earlier)" % (y, y - 1))
            write_json(stage / "data" / "anchors-c" / (stem(y) + ".json"), snap)
            anchors_written[stem(y)] = y
            add_area_rows(stem(y), y, snap)
            return
        # end of the full run: the final snapshot (end of 2026) and the last window's end anchor
        yy = comp.until
        snap = comp.snapshot(yy, "end of %d (after every event dated %d or earlier; the final snapshot)" % (yy, yy))
        write_json(stage / "data" / "anchors-c" / (stem(yy) + ".json"), snap)
        anchors_written[stem(yy)] = yy
        add_area_rows(stem(yy), yy, snap)
        last = wins[-1]
        s2 = dict(snap)
        s2["year"] = last["to"] + 1
        s2["as_of"] = "1 January %d (after every event; the run stops at %d and nothing is dated later)" % (
            last["to"] + 1, LAST_YEAR)
        write_json(stage / "data" / "anchors-c" / (last["end_anchor"] + ".json"), s2)
        anchors_written[last["end_anchor"]] = s2["year"]

    def on_window_end(y):
        w = window_ends[y]
        if trial is not None and w["id"] != trial["id"]:
            comp.drop_window(w)         # a trial keeps only its window's records
            return
        write_draft(comp, w, stage)
        comp.window_end(w)

    comp.run(anchor_years, on_anchor, on_window_end, set(window_ends) if full else
             {e for e in window_ends if e <= args.until})
    if trial is not None:
        return trial_finish(comp, inp, hist, stage, trial, t_all)
    report = finish(comp, inp, res, wins, stage, hist, anchors_written, area_rows, args, full, t_all)
    if full and not args.stage_only:
        publish(stage, hist)
    log("all done in %.0f s" % (time.time() - t_all))
    return report


def write_draft(comp, w, stage):
    a, b = w["from"], w["to"]
    years = {str(y): comp.year_records.pop(y) for y in sorted(list(comp.year_records)) if a <= y <= b}
    oc, oo, ov = comp.open_lists()
    conflicts = []
    for (y, win, lose, cells, ctx, sw, sl, rule) in comp.log_conflicts:
        if a <= y <= b:
            conflicts.append({"year": y, "cells": to_runs(np.sort(cells)), "n": int(cells.size),
                              "claimants": [comp.names[win], comp.names[lose]], "resolved_to": comp.names[win],
                              "rule": conflict_rule_text(comp, y, win, lose, ctx, sw, sl, rule)})
    snaps = [s for s in comp.log_snaps if a <= s["year"] <= b]
    unresolved = [{"slug": u["slug"], "where": u["where"], "year": u["year"], "type": u["type"], "spec": u["spec"],
                   "error": "; ".join(e for _, e in u["errors"])[:600]}
                  for u in comp.log_unresolved if a <= u["year"] <= b]
    skipped = [s for s in comp.log_skipped if a <= s["year"] <= b and s["reason"] != "region does not resolve"]
    notes = ("Draft compiled mechanically by tools/compile_dossiers.py on %s from the reviewed dossiers "
             "(window-brief section 3). It starts from anchor %s and ends at anchor %s by construction, so "
             "disagreements is empty. %d keyframe snaps (dossier gaps: the keyframe differs from the ledger by "
             "more than 20 cells or 5 percent) are listed in keyframe_snaps; %d events were skipped because their "
             "region does not resolve (unresolved_regions) and %d for other reasons (skipped)." % (
                 date.today().isoformat(), w["start_anchor"], w["end_anchor"], len(snaps), len(unresolved),
                 len(skipped)))
    gaps = []
    for s in sorted(snaps, key=lambda s: -(s["added"] + s["removed"]))[:25]:
        gaps.append("%s %d: keyframe %s adds %d and removes %d cells the ledger does not move" % (
            s["slug"], s["year"], s["shape_id"], s["added"], s["removed"]))
    if gaps:
        notes += " Largest gaps: " + "; ".join(gaps) + "."
    draft = {"window": w["id"], "from": a, "to": b, "grid": "land_r5.txt", "resolution": 5,
             "start_anchor": w["start_anchor"], "end_anchor": w["end_anchor"], "draft": True,
             "compiler": "tools/compile_dossiers.py",
             "years": years,
             "handoff": {"end_year": b, "disagreements": [], "conflicts": conflicts, "open_contests": oc,
                         "open_occupations": oo, "open_vassals": ov, "unresolved_regions": unresolved,
                         "keyframe_snaps": snaps, "skipped": skipped, "notes": notes}}
    write_json(stage / "compiled" / "_draft" / (w["id"] + ".json"), draft)


def conflict_rule_text(comp, y, win, lose, ctx, sw, sl, rule):
    if rule.startswith("ruling "):
        R = comp.rulings[comp.ruling_by_id[rule[7:]]]
        return "ruling of %s: %s (%s)" % (patch_ref(R["window"], "rulings", R["k"]), R["why"], ctx)
    if rule == "R2 succession":
        return "R2: %s succeeds %s and the year is in its life (%s)" % (comp.names[win], comp.names[lose], ctx)
    if rule in ("R3 vassal", "R3 constituent"):
        j = comp.r3_hop.get((win, lose, y))
        par = comp.names[comp.hier_rows[j][1]] if j is not None else "?"
        return "R3: data/hierarchy.csv makes %s a %s of %s (immediate parent %s); the child owns it (%s)" % (
            comp.names[win], rule.split(" ")[1], comp.names[lose], par, ctx)
    if rule == "R3 same state":
        return "R3: data/hierarchy.csv: %s and %s are one state these years; %s's dossier is drawn (%s)" % (
            comp.names[win], comp.names[lose], comp.names[win], ctx)
    if rule == "R1 colony":
        m = comp.metropole(win, y)
        return "R1: the colony owns it, in its metropole's vassal tint (%s; metropole %s)" % (
            ctx, comp.names[m] if m >= 0 else "?")
    if rule == "R1 same metropole":
        m = comp.metropole(win, y)
        return "R1: both are colonies of %s; the smaller one owns it (%s; %.0f km2 against %.0f km2)" % (
            comp.names[m] if m >= 0 else "?", ctx, sw, sl)
    return "smaller Cliopatria area that year wins (%s; %.0f km2 against %.0f km2)" % (ctx, sw, sl)


# The largest pairs the size rule still settles, categorised by hand (the rest are categorised by
# conflict_category's heuristic; conflicts.csv says which): nested = a state inside a larger one that
# is not its colony (an SSR, an ulus, a duchy of the Empire, a princely state, a nominal
# vassal); unrelated = two distinct states whose shapes claim the same land; same state = two
# dossiers for one state whose lives overlap; rebel = a type-rebel dossier.
CONFLICT_REVIEWED = {
    ("kazakh-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("khoshut-khanate", "tibet"): "nested",
    ("turkmen-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("union-of-soviet-socialist-republics", "uzbek-soviet-socialist-republic"): "nested",
    ("abbasid-caliphate", "great-seljuk-empire"): "nested",
    ("khoshut-khanate", "qing-dynasty"): "nested",
    ("kirghiz-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("kingdom-of-nagpur", "maratha-empire"): "nested",
    ("republic-of-china", "shanxi-clique"): "nested",
    ("abbasid-caliphate", "ghaznavid-empire"): "nested",
    ("mamluk-sultanate", "sharifate-of-mecca"): "nested",
    ("mihrabanids", "timurid-empire"): "nested",
    ("tajik-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("bikaner-state", "mughal-empire"): "nested",
    ("holy-roman-empire", "stem-duchy-of-bavaria"): "nested",
    ("han-dynasty", "han-sui"): "nested",
    ("cuan-clan", "liang-dynasty"): "nested",
    ("holy-roman-empire", "stem-duchy-of-saxony"): "nested",
    ("cuan-clan", "western-jin"): "nested",
    ("banu-kanz", "fatimid-caliphate"): "nested",
    ("croatia-in-union-with-hungary", "kingdom-of-hungary"): "nested",
    ("holy-roman-empire", "stem-duchy-of-swabia"): "nested",
    ("karelo-finnish-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("republic-of-china", "zhili-clique"): "nested",
    ("great-seljuk-empire", "kerman-seljuk-sultanate"): "nested",
    ("british-raj", "kingdom-of-mysore"): "nested",
    ("azerbaijan-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("han-dynasty", "lu-fang"): "nested",
    ("guiyi-circuit", "tang-dynasty"): "nested",
    ("duchy-of-lower-lorraine", "holy-roman-empire"): "nested",
    ("holy-roman-empire", "kingdom-of-arles"): "nested",
    ("qocho-kingdom", "ulus-of-chagatai"): "nested",
    ("jaisalmer-state", "mughal-empire"): "nested",
    ("duchy-of-styria", "habsburg-monarchy"): "nested",
    ("ottoman-empire", "sharifate-of-mecca"): "nested",
    ("khwarezmid-empire", "salghurids"): "nested",
    ("duchy-of-brunswick-luneburg", "holy-roman-empire-minor-states"): "nested",
    ("georgian-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("kalachuris-of-ratnapura", "mughal-empire"): "nested",
    ("kartids", "ulus-of-hulegu"): "nested",
    ("cuan-clan", "liu-song-dynasty"): "nested",
    ("bikaner-state", "british-raj"): "nested",
    ("british-raj", "kingdom-of-marwar"): "nested",
    # reviewed after R3 (round 3)
    ("blemmyes", "eastern-roman-empire"): "unrelated",
    ("blemmyes", "roman-empire"): "unrelated",
    ("timurid-empire", "uzbek-khanate-of-abul-khayr"): "unrelated",
    ("ottoman-empire", "safavid-dynasty"): "unrelated",
    ("tang-dynasty", "yenisei-kyrgyz"): "nested",
    ("eastern-gokturks", "yenisei-kyrgyz"): "nested",
    ("later-zhou", "liao-dynasty"): "unrelated",
    ("alchon-huns", "gupta-empire"): "unrelated",
    ("holy-roman-empire-minor-states", "principality-of-luneburg"): "nested",
    ("khanate-of-kalat", "qajar-dynasty"): "unrelated",
    ("mamluk-dynasty", "paramara-dynasty"): "unrelated",
    ("kerait", "liao-dynasty"): "nested",
    ("british-raj", "khanate-of-kalat"): "nested",
    ("khoshut-khanate", "wu-sangui-s-zhou"): "rebel",
    ("french-equatorial-africa", "german-africa"): "colony",
    ("german-africa", "tanganyika-territory"): "colony",
    ("british-colonial-empire", "german-new-guinea"): "colony",
    ("soomra-dynasty", "tughlaq-dynasty"): "nested",
    ("british-raj", "gwalior-state"): "nested",
    ("lulong-circuit", "tang-dynasty"): "nested",
    ("habsburg-netherlands", "iberian-union"): "nested",
    ("habsburg-netherlands", "kingdom-of-spain"): "nested",
    ("latvian-soviet-socialist-republic", "union-of-soviet-socialist-republics"): "nested",
    ("habsburg-monarchy", "habsburg-netherlands"): "nested",
    ("republic-of-china", "tibet"): "unrelated",
    ("alchon-huns", "white-huns"): "unrelated",
    ("han-dynasty", "xiongnu"): "unrelated",
    ("kimek-kipchak-confederation", "ulus-of-jochi"): "unrelated",
    ("han-2", "kingdom-of-han"): "unrelated",
    ("federated-republic-of-mexico", "united-states-of-america"): "unrelated",
    ("buyid-dynasty", "ghaznavid-empire"): "unrelated",
    ("northern-wei", "rouran-khaganate"): "unrelated",
    ("spanish-empire", "sultanate-of-maguindanao"): "unrelated",
    ("hotaki-dynasty", "khanate-of-kalat"): "unrelated",
    ("liu-song-dynasty", "northern-wei"): "unrelated",
    ("tang-dynasty", "tibetan-empire"): "unrelated",
    ("british-empire", "east-india-company"): "same state",
    ("kashmir", "lohara-dynasty"): "same state",
}


def conflict_category(comp, a, b, max_share):
    """-> (category, source) for a pair the size rule settled: rebel / same state / colony / nested /
    unrelated; source "reviewed" (CONFLICT_REVIEWED) or "heuristic": a type-rebel dossier; a shared
    Cliopatria name, Wikipedia title, Wikidata id or primary name, or a predecessor link; a colony (of another metropole, or of none);
    the conflict cells of one year reaching half the smaller state's area; otherwise unrelated."""
    key = tuple(sorted((a, b)))
    if key in CONFLICT_REVIEWED:
        return CONFLICT_REVIEWED[key], "reviewed"
    da, db = comp.name_id[a], comp.name_id[b]
    ia, ib = comp.dos[da]["identity"], comp.dos[db]["identity"]
    if "rebel" in (ia["type"], ib["type"]):
        return "rebel", "heuristic"
    ca, cb = set(ia.get("cliopatria_names") or []), set(ib.get("cliopatria_names") or [])
    if (ca & cb) or (ia.get("wikidata") and ia.get("wikidata") == ib.get("wikidata")) or \
            (ia.get("wikipedia") and ia.get("wikipedia") == ib.get("wikipedia")) or \
            (da, db) in comp.succ or (db, da) in comp.succ or \
            (ia.get("name") or "a").lower() == (ib.get("name") or "b").lower():
        return "same state", "heuristic"
    if comp.is_colony[da] or comp.is_colony[db]:
        return "colony", "heuristic"
    if max_share >= 0.5:
        return "nested", "heuristic"
    return "unrelated", "heuristic"


def finish(comp, inp, res, wins, stage, hist, anchors_written, area_rows, args, full, t_all):
    """Reports, self-check, Phase A comparison."""
    notes = stage / "notes" / "phase-c"
    out = {}
    st = comp.stats
    # --- unresolved
    rows, agg = [], defaultdict(lambda: {"events": 0, "dossiers": set(), "error": "", "types": Counter()})
    for u in comp.log_unresolved:
        leaves = [k for k, _ in u["errors"]]
        rows.append((u["slug"], u["where"], u["year"], u["type"],
                     " | ".join("%s: %s" % leaf_label(k) if k else "" for k in leaves),
                     "; ".join(e for _, e in u["errors"])[:500], json.dumps(u["spec"], ensure_ascii=False)[:800]))
        for k, e in u["errors"]:
            lab = leaf_label(k) if k else ("keyframe", e)
            a = agg[lab]
            a["events"] += 1
            a["dossiers"].add(u["slug"])
            a["types"][u["type"]] += 1
            if not a["error"]:
                a["error"] = e[:300]
    write_csv(notes / "unresolved_events.csv", ["slug", "where", "year", "type", "failing_leaves", "errors", "spec"],
              sorted(rows, key=lambda r: (r[2], r[0])))
    agg_rows = sorted(((k[0], k[1], v["events"], len(v["dossiers"]), " ".join("%s:%d" % kv for kv in v["types"].most_common()),
                        ";".join(sorted(v["dossiers"])[:12]), v["error"]) for k, v in agg.items()),
                      key=lambda r: (-r[2], -r[3], r[0], r[1]))
    write_csv(notes / "unresolved_names.csv", ["kind", "name", "events", "dossiers", "event_types", "example_dossiers", "error"],
              agg_rows)
    out["unresolved_events"] = len(rows)
    out["unresolved_names"] = len(agg_rows)
    # --- skipped, unclosed, no-op
    write_csv(notes / "skipped_events.csv", ["slug", "where", "year", "type", "reason"],
              [(s["slug"], s["where"], s["year"], s["type"], s["reason"]) for s in comp.log_skipped])
    write_csv(notes / "unclosed_ends.csv", ["slug", "ledger_index", "year", "type", "counterpart"], comp.log_unclosed)
    write_csv(notes / "noop_events.csv", ["slug", "ledger_index", "year", "type", "region_cells"], comp.log_noop)
    # --- conflicts by pair: the size rule's (the conflicts that remain) and those R1 and R2 settle
    pairs = defaultdict(lambda: {"years": set(), "cells": 0, "max": 0, "wins": Counter(), "ctx": Counter(),
                                 "claims": 0, "share": 0.0})
    for (y, win, lose, cells, ctx, sw, sl, rule) in comp.log_conflicts:
        a, b = sorted((comp.names[win], comp.names[lose]))
        p = pairs[(a, b, rule)]
        p["years"].add(y)
        p["cells"] += int(cells.size)
        p["claims"] += 1
        p["max"] = max(p["max"], int(cells.size))
        p["wins"][comp.names[win]] += int(cells.size)
        p["ctx"][ctx.split(" ")[0]] += 1
        small = min(sw, sl)
        if small > 0:
            p["share"] = max(p["share"], cells.size * CELL_KM2 / small)
    crow, rrow = [], []
    for (a, b, rule), p in pairs.items():
        ys = sorted(p["years"])
        common = (p["cells"], p["max"], len(ys), ys[0], ys[-1], " ".join(str(v) for v in ys[:40]),
                  "; ".join("%s %d" % kv for kv in p["wins"].most_common()),
                  " ".join("%s:%d" % kv for kv in p["ctx"].items()))
        if rule == "size":
            cat_, src_ = conflict_category(comp, a, b, p["share"])
            crow.append((a, b, cat_, round(min(p["share"], 9.99), 2)) + common + (p["claims"], src_))
        else:
            rrow.append((a, b, rule) + common + (p["claims"],))
    crow.sort(key=lambda r: (-r[4], r[0], r[1]))
    rrow.sort(key=lambda r: (-r[3], r[0], r[1]))
    write_csv(notes / "conflicts.csv", ["slug_a", "slug_b", "category", "max_share_of_smaller", "cells_total",
                                        "cells_max_one_year", "years_n", "first_year", "last_year", "years",
                                        "cells_won_by", "contexts", "claims", "category_source"], crow)
    write_csv(notes / "conflicts_settled_by_rule.csv", ["slug_a", "slug_b", "rule", "cells_total", "cells_max_one_year",
                                                        "years_n", "first_year", "last_year", "years", "cells_won_by",
                                                        "contexts", "claims"], rrow)
    tot = sum(r[4] for r in crow)
    out["conflict_pairs"] = len(crow)
    out["conflict_cells"] = tot
    out["conflict_events"] = sum(r[-2] for r in crow)
    out["conflict_top_share"] = {str(k): round(sum(r[4] for r in crow[:k]) / tot, 4) if tot else 0
                                 for k in (60, 100, 200, 400)}
    cat = defaultdict(lambda: [0, 0])
    for r in crow:
        cat[r[2]][0] += 1
        cat[r[2]][1] += r[4]
    out["conflict_categories"] = {k: {"pairs": v[0], "cells": v[1]} for k, v in sorted(cat.items())}
    out["conflict_top60"] = [(r[0], r[1], r[2], r[4], r[3], r[7], r[8], r[-1], r[10]) for r in crow[:60]]
    by_rule = defaultdict(lambda: [0, 0, 0])
    for (a, b, rule), p in pairs.items():
        by_rule[rule][0] += 1
        by_rule[rule][1] += p["cells"]
        by_rule[rule][2] += p["claims"]
    out["claims_by_rule"] = {k: {"pairs": v[0], "cells": v[1], "claims": v[2]} for k, v in sorted(by_rule.items())}
    # --- hierarchy.csv (R3)
    hi = comp.hier_info_out
    write_csv(notes / "hierarchy_check.csv", ["line", "child", "parent", "issue"], hi["issues"])
    r3 = defaultdict(lambda: {"pairs": set(), "cells": set(), "cell_years": 0, "claims": 0})
    for (y, win, lose, cells, ctx, sw, sl, rule) in comp.log_conflicts:
        if rule.startswith("R3"):
            k = rule[3:]
            r3[k]["pairs"].add((min(win, lose), max(win, lose)))
            r3[k]["cells"].update(cells.tolist())
            r3[k]["cell_years"] += int(cells.size)
            r3[k]["claims"] += 1
    out["hierarchy"] = {
        "rows_read": hi["rows_read"], "spans_applied": hi["spans"], "spans_by_kind": hi["spans_by_kind"],
        "notes": len(hi["issues"]),
        "not_applied": [list(x) for x in hi["issues"] if not x[3].startswith(("clipped", "colony"))],
        "relations_opened": sum(v for k, v in st.items() if k.startswith("hierarchy relations opened")),
        "settled_in_conflicts": {k: {"pairs": len(v["pairs"]), "distinct_cells": len(v["cells"]),
                                     "cell_years": v["cell_years"], "claims": v["claims"]} for k, v in sorted(r3.items())},
        "tinted_cell_years": dict(comp.hier_cell_years)}
    # --- colonies.csv
    col = comp.colony_info_out
    write_csv(notes / "colonies_check.csv", ["colony", "from", "to", "issue"], col["issues"])
    out["colonies"] = {k: v for k, v in col.items() if k != "issues"}
    out["colonies"]["issues"] = len(col["issues"])
    # --- keyframe snaps
    srows = [(s["slug"], s["shape_id"], s["year"], s["diff"], s["added"], s["removed"], s["kept_by_others"],
              s["state_cells"], s["keyframe_cells"], " ".join(s["shape_ids"])) for s in comp.log_snaps]
    srows.sort(key=lambda r: -(r[4] + r[5]))
    write_csv(notes / "keyframe_snaps.csv", ["slug", "shape_id", "year", "cells_differing", "cells_added", "cells_removed",
                                             "cells_kept_by_others", "state_cells_before", "keyframe_cells", "keyframes_alive_starting"],
              srows)
    out["keyframe_snaps"] = len(srows)
    # --- where the top conflicts and snaps are (admin-1 regions), for the dossier fixers
    t = time.time()
    out["place_reports"] = write_place_reports(comp, inp, hist, notes, crow)
    log("place reports: %s, %.1f s" % (out["place_reports"], time.time() - t))
    # --- data/patches/: what was applied, what each ruling settled
    prow = write_patches_check(comp, notes)
    out["patches"] = {"folder": str(comp.patch_dir), "counts": dict(comp.patch_counts),
                      "rulings_settling": sum(1 for R in comp.rulings if comp.ruling_used.get(R["idx"], [0])[0])}
    t = time.time()
    out["window_packets"] = write_window_packets(comp, inp, hist, notes, wins, prow)
    log("window packets: %s, %.1f s" % (out["window_packets"], time.time() - t))
    # --- areas at anchors
    write_csv(notes / "areas.csv", ["anchor", "year", "slug", "cells", "cell_km2", "clio_km2", "ratio"], area_rows)
    # --- adjacency
    arows = []
    for (a, b), (f, l, mx, ny) in comp.adj.items():
        if a >= comp.N or b >= comp.N:
            continue
        arows.append((comp.names[a], comp.names[b], f, l, ny, mx))
    arows.sort(key=lambda r: (r[0], r[1]))
    write_csv(notes / "adjacency.csv", ["slug_a", "slug_b", "first_year", "last_year", "years_adjacent", "max_shared_edges"], arows)
    out["adjacent_pairs"] = len(arows)
    # --- deaths
    write_csv(notes / "deaths.csv", ["year", "slug", "cells_at_end", "to_successors", "to_nobody"], comp.log_deaths)
    # --- self-check
    sc = None
    if full:
        t = time.time()
        sc = replay(stage, wins, comp.n)
        sc["seconds"] = round(time.time() - t, 1)
        log("self-check: %s" % {k: v for k, v in sc.items() if k != "mismatches"})
    out["self_check"] = sc
    # --- Phase A comparison
    comps = []
    for y in [int(v) for v in args.compare.split(",") if v.strip()]:
        pa = hist / "data" / "anchors" / (stem(y) + ".json")
        pc = stage / "data" / "anchors-c" / (stem(y) + ".json")
        if pa.exists() and pc.exists():
            comps.append(compare_phase_a(comp, pa, pc, y))
    out["phase_a"] = comps
    write_json(notes / "phase_a_comparison.json", comps, compact=False)
    # --- worst problems by land affected: snaps by cells moved, conflicts by the most cells at stake in
    # one year, ends by the cells that go to nobody
    probs = []
    for s_ in comp.log_snaps:
        probs.append((s_["added"] + s_["removed"], "keyframe snap", s_["slug"], s_["year"],
                      "keyframe %s adds %d and removes %d cells that no ledger event moves (the state had %d)" % (
                          s_["shape_id"], s_["added"], s_["removed"], s_["state_cells"])))
    for (a_, b_, rule_), p in pairs.items():
        if rule_ != "size":
            continue
        ys = sorted(p["years"])
        probs.append((p["max"], "conflict", "%s|%s" % (a_, b_), ys[0],
                      "both claim up to %d cells in one year, in %d years %d..%d (%s)" % (
                          p["max"], len(ys), ys[0], ys[-1], "; ".join("%s won %d cell-years" % kv for kv in p["wins"].most_common()))))
    for (y, slug, total, ts, tn) in comp.log_deaths:
        if tn:
            probs.append((tn, "end to nobody", slug, y, "%d of its %d cells go to nobody at its end (no living successor's land covers them)" % (tn, total)))
    probs.sort(key=lambda r: -r[0])
    write_csv(notes / "problems.csv", ["cells", "kind", "slug", "year", "what"], probs[:3000])
    out["problems_top"] = probs[:20]
    out["unresolved_top"] = agg_rows[:20]
    out["stats"] = dict(st)
    out["anchors_written"] = len(anchors_written)
    out["seconds"] = round(time.time() - t_all)
    out["dossiers"] = len(inp.dossiers)
    out["invalid_dossiers"] = inp.invalid
    out["events_total"] = sum(len(d["ledger"]) for d in inp.dossiers.values())
    out["relations"] = Counter(R["kind"] for R in comp.rels)
    write_json(notes / "run_summary.json", out, compact=False)
    write_readmes(comp, wins, stage, out, args, full)
    return out


# ----------------------------------------------------------------------------
# place reports: where the top size-rule conflicts and keyframe snaps are
# ----------------------------------------------------------------------------

PLACE_PAIRS = 150        # conflict_places.csv: the top pairs by cell-years
PLACE_YEARS = 12         # at most this many conflict years per pair (those with the most cells)
PLACE_SNAPS = 100        # snap_places.csv: the top snaps by cells differing (and by cells moved)
PLACE_TOP = 6
KF_TEXT_MAX = 200        # a keyframe's correction text is quoted when this short


def admin1_lookup(hist, n):
    """Cell -> label id: the admin-1 row of data/gazetteer/admin1.jsonl that lists the cell (a cell listed by
    two rows takes the smaller row), else its country from countries.jsonl. Reverse lookup only.
    -> (int32 array, -1 for no row; labels "Name (Country)")"""
    lab = np.full(n, -1, np.int32)
    labels = []
    gz = hist / "data" / "gazetteer"
    for name in ("admin1.jsonl", "countries.jsonl"):
        path = gz / name
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            rows = [json.loads(line) for line in f if line.strip()]
        for r in sorted(rows, key=lambda r: r.get("n_cells") or 0):
            idx = from_runs(r.get("cells") or [])
            idx = idx[(idx >= 0) & (idx < n)]
            idx = idx[lab[idx] == -1]
            if idx.size == 0:
                continue
            lab[idx] = len(labels)
            if name == "admin1.jsonl":
                labels.append("%s (%s)" % (r.get("name"), r.get("country") or r.get("adm0_a3") or "?"))
            else:
                labels.append("no admin-1 (%s)" % r.get("name"))
    return lab, labels


def write_place_reports(comp, inp, hist, notes, crow):
    """notes/phase-c/conflict_places.csv and snap_places.csv. -> {file: rows}"""
    import h3
    lab, labels = comp.adm if comp.adm is not None else admin1_lookup(hist, comp.n)
    lat = np.full(comp.n, np.nan)
    lon = np.full(comp.n, np.nan)

    def places(cells, k=PLACE_TOP):
        if cells.size == 0:
            return ""
        u, c = np.unique(lab[cells], return_counts=True)
        o = np.lexsort((u, -c))[:k]
        txt = "; ".join("%s %d" % (labels[u[i]] if u[i] >= 0 else "unmapped", c[i]) for i in o)
        return txt + ("; +%d more regions" % (u.size - k) if u.size > k else "")

    def geo(cells):
        need = cells[np.isnan(lat[cells])]
        for c in need.tolist():
            lat[c], lon[c] = h3.cell_to_latlng(inp.land[c])
        la, lo = lat[cells], lon[cells]
        ra, ro = np.radians(la), np.radians(lo)
        x, y_, z = (np.cos(ra) * np.cos(ro)).mean(), (np.cos(ra) * np.sin(ro)).mean(), np.sin(ra).mean()
        clat, clon = np.degrees(np.arctan2(z, np.hypot(x, y_))), np.degrees(np.arctan2(y_, x))
        w, e = lo.min(), lo.max()
        if e - w > 180:      # across the antimeridian: west edge east of the east edge
            l2 = np.where(lo < 0, lo + 360, lo)
            w, e = l2.min(), l2.max()
            w, e = (w - 360 if w > 180 else w), (e - 360 if e > 180 else e)
        return [round(float(v), 2) for v in (clat, clon, la.min(), w, la.max(), e)]

    kf_text = {}
    for did, d in enumerate(comp.dos):
        for k in d.get("keyframe_review", []) or []:
            key = (comp.slugs[did], k.get("shape_id"))
            txt = ((k.get("correction") or {}).get("text") or "").strip() if isinstance(k.get("correction"), dict) else ""
            if txt and key not in kf_text:
                kf_text[key] = txt

    def ref_text(ref):
        if ref == "":
            return "?"
        parts = ref.split(" [")[0].split("/")
        if len(parts) == 3 and parts[1] == "keyframe":
            txt = kf_text.get((parts[0], parts[2]), "")
            if txt and len(txt) > KF_TEXT_MAX:
                txt = first_sentence(txt)
            if txt and len(txt) <= KF_TEXT_MAX:
                return '%s "%s"' % (ref, txt)
        return ref

    def claims(cnt):
        items = cnt.most_common()
        if len(items) == 1:
            return ref_text(items[0][0])
        txt = "; ".join("%s (%d cells)" % (ref_text(r), n) for r, n in items[:3])
        return txt + ("; +%d more" % (len(items) - 3) if len(items) > 3 else "")

    # --- conflict_places.csv
    rank = {(r[0], r[1]): i + 1 for i, r in enumerate(crow[:PLACE_PAIRS])}
    by_pair = defaultdict(lambda: defaultdict(list))
    for i, (y, win, lose, cells, ctx, sw, sl, rule) in enumerate(comp.log_conflicts):
        if rule != "size":
            continue
        a, b = sorted((comp.names[win], comp.names[lose]))
        if (a, b) in rank:
            by_pair[(a, b)][y].append(i)
    ref_ids, ref_list = {}, []

    def rid(ref):
        if ref not in ref_ids:
            ref_ids[ref] = len(ref_list)
            ref_list.append(ref)
        return ref_ids[ref]

    crows = []
    for (a, b), years in sorted(by_pair.items(), key=lambda kv: rank[kv[0]]):
        ycells = {y: sum(int(comp.log_conflicts[i][3].size) for i in ix) for y, ix in years.items()}
        keep = sorted(years)
        note = ""
        if len(keep) > PLACE_YEARS:
            keep = sorted(sorted(years, key=lambda y: (-ycells[y], y))[:PLACE_YEARS])
            note = "%d of %d conflict years (those with the most cells)" % (PLACE_YEARS, len(years))
        for y in keep:
            ix = years[y]
            cells = np.unique(np.concatenate([comp.log_conflicts[i][3] for i in ix]))
            won = Counter()
            side = {a: ([], []), b: ([], [])}     # per side: reference ids, cells (a cell counts once per reference)
            for i in ix:
                _y, win, lose, cs, ctx, sw, sl, rule = comp.log_conflicts[i]
                won[comp.names[win]] += int(cs.size)
                claimant, ref, hold = comp.log_conflict_meta[i]
                holder = lose if win == claimant else win
                side[comp.names[claimant]][0].append(np.full(cs.size, rid(ref), np.int64))
                side[comp.names[claimant]][1].append(cs)
                ua, inv = np.unique(hold, return_inverse=True)
                hid = np.array([rid(comp.acts[x] if x >= 0 else "") for x in ua.tolist()], np.int64)
                side[comp.names[holder]][0].append(hid[inv])
                side[comp.names[holder]][1].append(cs)
            cnt = {}
            for k_, (ri, ce) in side.items():
                cnt[k_] = Counter()
                if ri:
                    u = np.unique(np.concatenate(ri) * comp.n + np.concatenate(ce))
                    rr, nn = np.unique(u // comp.n, return_counts=True)
                    for r_, n_ in zip(rr.tolist(), nn.tolist()):
                        cnt[k_][ref_list[r_]] = n_
            winner = won.most_common(1)[0][0] if len(won) == 1 else "; ".join("%s %d" % kv for kv in won.most_common())
            crows.append([rank[(a, b)], a, b, y, int(cells.size), winner, places(cells)] + geo(cells) +
                         [claims(cnt[a]), claims(cnt[b]), note])
    write_csv(notes / "conflict_places.csv", ["pair_rank", "slug_a", "slug_b", "year", "cells", "winner", "places",
                                              "lat", "lon", "lat_min", "lon_min", "lat_max", "lon_max",
                                              "claim_a", "claim_b", "years_note"], crows)
    # --- snap_places.csv
    S = comp.log_snaps
    by_diff = sorted(range(len(S)), key=lambda i: (-S[i]["diff"], S[i]["slug"], S[i]["year"]))
    by_moved = sorted(range(len(S)), key=lambda i: -(S[i]["added"] + S[i]["removed"]))   # keyframe_snaps.csv order
    r_diff = {i: r + 1 for r, i in enumerate(by_diff)}
    r_moved = {i: r + 1 for r, i in enumerate(by_moved)}
    pick = sorted(set(by_diff[:PLACE_SNAPS]) | set(by_moved[:PLACE_SNAPS]), key=lambda i: r_diff[i])
    srows = []
    for i in pick:
        s = S[i]
        did = comp.name_id[s["slug"]]
        take, release, kept, kowner = comp.log_snap_cells[i]
        y = s["year"]
        start = int(comp.start[did])
        prev_y = max([k for k in comp.keyframe_years(did) if k < y], default=None)
        prev = ""
        if prev_y is not None:
            ks = [k for k in comp.keyframes(did) if k.get("from") is not None and max(k["from"], start) == prev_y]
            prev = ks[0]["shape_id"] if ks else ""
        lo_ = prev_y if prev_y is not None else start - 1
        between = sum(1 for e in comp.dos[did]["ledger"] if lo_ < int(e["year"]) <= y)
        holders = ""
        if kept.size:
            # the holders as the snap left them (the keyframe moved none of these cells)
            u, c = np.unique(kowner, return_counts=True)
            o = np.lexsort((u, -c))[:3]
            holders = "; ".join("%s %d" % (comp.names[u[j]] if u[j] >= 0 else "nobody", c[j]) for j in o)
            if u.size > 3:
                holders += "; +%d more" % (u.size - 3)
        srows.append([r_diff[i], r_moved[i], s["slug"], s["shape_id"], y, s["diff"], s["added"], s["removed"],
                      places(take), places(release), int(kept.size), holders, places(kept),
                      prev, prev_y if prev_y is not None else "", between])
    write_csv(notes / "snap_places.csv", ["rank_by_differing", "rank_by_moved", "slug", "shape_id", "year",
                                          "cells_differing", "added", "removed", "added_places", "removed_places",
                                          "kept_by_others", "kept_by_others_holders", "kept_by_others_places",
                                          "prev_keyframe", "prev_keyframe_year", "ledger_between"], srows)
    return {"conflict_places.csv": len(crows), "snap_places.csv": len(srows),
            "conflict_pairs": len(by_pair)}


# ----------------------------------------------------------------------------
# window packets: notes/phase-c/windows/<window>.md, what each window agent should look at
# ----------------------------------------------------------------------------

PACKET_MAX = 25000           # bytes
COLOUR_CLOSE = 0.08          # OKLab distance under which two neighbours' colours are listed (the colour agent
                             # sets the real threshold in colours.json)


def hex_oklab(hx):
    """sRGB hex -> OKLab (L, a, b)."""
    v = [int(hx[i:i + 2], 16) / 255.0 for i in (1, 3, 5)]
    r, g, b = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in v]
    l_ = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m_ = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s_ = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)


def read_colours(hist):
    """colours.json -> {slug: hex} (fixed and assigned)."""
    out = {}
    try:
        with open(hist / "colours.json", encoding="utf-8") as f:
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


def window_of(y):
    """Index into windows() of the window holding year y."""
    if y < 1600:
        return max(0, (y - CENTURY_STARTS[0]) // 100)
    return len(CENTURY_STARTS) + min((y - 1600) // 10, len(DECADE_STARTS) - 1)


def md_cell(v):
    return str(v).replace("|", "/").replace("\n", " ")


def write_patches_check(comp, notes):
    """notes/phase-c/patches_check.csv: every patch entry, with what each ruling settled. -> the rows"""
    prow = [list(r) for r in comp.patch_rows]
    for R in comp.rulings:
        u = comp.ruling_used.get(R["idx"])
        if u and u[0]:
            msg = "settled %d cell-years in %d years (%d claims)" % (u[0], len(u[1]), u[2])
        else:
            msg = "settled nothing: no conflict between %s and %s in these years%s" % (
                R["a"], R["b"], " and cells" if R["cells"] is not None else "")
            if R["from"] > comp.until:
                msg += " (after the compiled years)"
        if comp.ruling_r2.get(R["idx"]):
            msg += "; R2 (succession) settled %d claims first" % comp.ruling_r2[R["idx"]]
        prow[R["row"]][5] = (prow[R["row"]][5] + "; " if prow[R["row"]][5] else "") + msg
    write_csv(notes / "patches_check.csv", ["window", "kind", "index", "slug", "outcome", "message"], prow)
    write_patch_overrides(comp, notes)
    return prow


def write_patch_overrides(comp, notes):
    """notes/phase-c/patch-overrides.csv: every keyframe a patch now controls (an applied keyframe_override),
    in window and entry order: window, shape_id, slug."""
    order = {w["id"]: i for i, w in enumerate(windows())}
    rows = []
    for did, d in enumerate(comp.dos):
        for k in d.get("keyframe_review", []):
            if k.get("_patch"):
                rows.append((order.get(k["_patch"], len(order)), k["_patch"], int(k.get("_patch_k", 0)),
                             k.get("shape_id"), comp.slugs[did]))
    rows.sort()
    write_csv(notes / "patch-overrides.csv", ["window", "shape_id", "slug"], [[r[1], r[3], r[4]] for r in rows])


def write_window_packets(comp, inp, hist, notes, wins, patch_rows):
    lab, labels = comp.adm if comp.adm is not None else admin1_lookup(hist, comp.n)
    names = comp.names
    allw = windows()               # the lists below are indexed by window_of(year) over every window
    windex = {x["id"]: i for i, x in enumerate(allw)}

    def places(cells, k=4):
        if cells.size == 0:
            return ""
        u, c = np.unique(lab[cells], return_counts=True)
        o = np.lexsort((u, -c))[:k]
        txt = "; ".join("%s %d" % (labels[u[i]] if u[i] >= 0 else "unmapped", c[i]) for i in o)
        return txt + ("; +%d more" % (u.size - k) if u.size > k else "")

    # conflicts of the size rule, by window and pair
    conf = [defaultdict(lambda: {"cells": 0, "years": set(), "won": Counter(), "idx": []}) for _ in allw]
    for i, (y, win, lose, cells, ctx, sw, sl, rule) in enumerate(comp.log_conflicts):
        if rule != "size":
            continue
        a, b = sorted((names[win], names[lose]))
        P = conf[window_of(y)][(a, b)]
        P["cells"] += int(cells.size)
        P["years"].add(y)
        P["won"][names[win]] += int(cells.size)
        P["idx"].append(i)
    snaps = [[] for _ in allw]
    for i, sn in enumerate(comp.log_snaps):
        snaps[window_of(sn["year"])].append(i)
    skipped = [[] for _ in allw]
    for sk in comp.log_skipped:
        skipped[window_of(sk["year"])].append(sk)
    unres = [[] for _ in allw]
    for u in comp.log_unresolved:
        unres[window_of(u["year"])].append(u)
    colours = read_colours(hist)
    lab_ok = {}
    by_win_patch = defaultdict(list)
    for r in patch_rows:
        by_win_patch[r[0]].append(r)
    today = date.today().isoformat()
    written, sizes = 0, []
    for w in wins:
        wi = windex[w["id"]]
        wd = comp.win_data.get(w["id"])
        if wd is None:
            continue
        a_, b_ = w["from"], w["to"]

        def build(cap):
            L = []
            L.append("# Window %s (%s to %s): review packet" % (w["id"], a_, b_))
            L.append("")
            L.append("Written by `tools/compile_dossiers.py` on %s from %d dossiers. The draft is "
                     "`compiled/_draft/%s.json`, from `data/anchors-c/%s.json` to `data/anchors-c/%s.json`. Look at a "
                     "year with `python3 -I tools/render_year.py <year> [--bbox lon1,lat1,lon2,lat2] [--highlight slug,...] "
                     "[--compare-cliopatria]`; record corrections in `data/patches/%s.json` (`data/patches/README.md`). "
                     "Lists are sorted by cells and cut at the length shown." % (
                         today, len(comp.dos), w["id"], w["start_anchor"], w["end_anchor"], w["id"]))
            L.append("")
            # this window's patch file
            pr = by_win_patch.get(w["id"], [])
            if pr:
                L.append("## Patch file (%d entries)" % len(pr))
                L.append("")
                L.append("| kind | # | slug | outcome | message |")
                L.append("| --- | --- | --- | --- | --- |")
                for r in pr[:cap["patch"]]:
                    L.append("| %s | %s | %s | %s | %s |" % tuple(md_cell(x) for x in (r[1], r[2], r[3], r[4], r[5][:300])))
                if len(pr) > cap["patch"]:
                    L.append("")
                    L.append("... and %d more (notes/phase-c/patches_check.csv)" % (len(pr) - cap["patch"]))
                L.append("")
            # rulings in force in these years (any window's file)
            rl = [R for R in comp.rulings if R["from"] <= b_ and R["to"] >= a_]
            if rl:
                L.append("## Rulings in force (%d)" % len(rl))
                L.append("")
                for R in rl[:cap["patch"]]:
                    u = comp.ruling_used.get(R["idx"], [0, set(), 0])
                    yrs = sorted(v for v in u[1] if a_ <= v <= b_)
                    L.append("- `%s`: %s..%s %s against %s, winner %s%s; settled cells in %d of these years. %s" % (
                        R["id"], R["from"], R["to"], R["a"], R["b"], R["winner"],
                        (", %s of %s" % (R["status"], R["suzerain"] or "the loser")) if R["status"] else "",
                        len(yrs), md_cell(R["why"][:200])))
                L.append("")
            # conflicts
            C = sorted(conf[wi].items(), key=lambda kv: (-kv[1]["cells"], kv[0]))
            tot = sum(v["cells"] for _, v in C)
            L.append("## Size-rule conflicts (%d pairs, %d cell-years)" % (len(C), tot))
            L.append("")
            if C:
                L.append("Both states claim the cells and no rule above the size rule settles them; the smaller state "
                         "won. `notes/phase-c/conflict_places.csv` has the top pairs year by year with claims.")
                L.append("")
                L.append("| pair | cell-years | years | won | where (distinct cells) |")
                L.append("| --- | --- | --- | --- | --- |")
                for (pa, pb), v in C[:cap["conf"]]:
                    cells = np.unique(np.concatenate([comp.log_conflicts[i][3] for i in v["idx"]]))
                    ys = sorted(v["years"])
                    yt = "%d..%d (%d)" % (ys[0], ys[-1], len(ys)) if len(ys) > 1 else str(ys[0])
                    L.append("| %s / %s | %d | %s | %s | %s |" % (pa, pb, v["cells"], yt,
                             md_cell("; ".join("%s %d" % kv for kv in v["won"].most_common())), md_cell(places(cells))))
                if len(C) > cap["conf"]:
                    L.append("")
                    L.append("... and %d more pairs (%d cell-years)" % (len(C) - cap["conf"], sum(v["cells"] for _, v in C[cap["conf"]:])))
            L.append("")
            # snaps
            S = sorted(snaps[wi], key=lambda i: -(comp.log_snaps[i]["added"] + comp.log_snaps[i]["removed"]))
            L.append("## Keyframe snaps (%d)" % len(S))
            L.append("")
            if S:
                L.append("The keyframe differs from the ledger by more than 20 cells or 5 percent, so the state was set to it: "
                         "an event is missing or the keyframe is wrong.")
                L.append("")
                L.append("| slug | keyframe | year | added | removed | kept by others | added where | removed where |")
                L.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
                for i in S[:cap["snap"]]:
                    sn = comp.log_snaps[i]
                    take, release, kept, kowner = comp.log_snap_cells[i]
                    L.append("| %s | %s | %d | %d | %d | %d | %s | %s |" % (
                        sn["slug"], sn["shape_id"], sn["year"], sn["added"], sn["removed"], sn["kept_by_others"],
                        md_cell(places(take, 3)), md_cell(places(release, 3))))
                if len(S) > cap["snap"]:
                    rest = S[cap["snap"]:]
                    L.append("")
                    L.append("... and %d more (%d cells moved)" % (len(rest), sum(comp.log_snaps[i]["added"] + comp.log_snaps[i]["removed"] for i in rest)))
            L.append("")
            # years with the most change
            Y = sorted(((y, v) for y, v in comp.year_changed.items() if a_ <= y <= b_), key=lambda kv: (-kv[1][0], kv[0]))
            L.append("## Years with the most cells changed")
            L.append("")
            if Y:
                L.append("| year | cells | where | by (event: cells) |")
                L.append("| --- | --- | --- | --- |")
                for y, (n, pl, by) in Y[:10]:
                    L.append("| %d | %d | %s | %s |" % (y, n, md_cell(pl), md_cell(by[:300])))
            else:
                L.append("No cell changes in this window.")
            L.append("")
            # skipped and unresolved
            sk = skipped[wi]
            L.append("## Skipped events (%d)" % len(sk))
            L.append("")
            for x in sorted(sk, key=lambda x: (x["year"], x["slug"]))[:cap["skip"]]:
                L.append("- %s %s %s (%s): %s" % (x["year"], x["slug"], x["where"], x["type"], md_cell(x["reason"])))
            if len(sk) > cap["skip"]:
                L.append("- ... and %d more (notes/phase-c/skipped_events.csv)" % (len(sk) - cap["skip"]))
            L.append("")
            un = unres[wi]
            L.append("## Unresolved regions (%d)" % len(un))
            L.append("")
            for x in sorted(un, key=lambda x: (x["year"], x["slug"]))[:cap["skip"]]:
                L.append("- %s %s %s (%s): %s" % (x["year"], x["slug"], x["where"], x["type"],
                                                   md_cell("; ".join(e for _, e in x["errors"])[:200])))
            if len(un) > cap["skip"]:
                L.append("- ... and %d more (notes/phase-c/unresolved_events.csv)" % (len(un) - cap["skip"]))
            L.append("")
            # relations: colony and hierarchy tints opened or closed, contests and occupations
            def rel_cells(r):
                R = comp.rels[r]
                if R["since"] <= b_ and (R["end"] is None or R["end"] > b_):
                    return wd["open"].get(r, 0), "open at the end"
                ce = R.get("cells_at_end")
                return (int(ce.size) if ce is not None else 0), "closed %d" % R["end"]
            tint, cont = [], []
            for R in comp.rels:
                opened = a_ <= R["since"] <= b_
                closed = R["end"] is not None and a_ <= R["end"] <= b_ + 1 and R["end"] != R["since"]
                if R["kind"] == "vassal" and (R.get("colony") or R.get("hierarchy") or R.get("ruling")) and (opened or closed):
                    n, state = rel_cells(R["id"])
                    src = "colony" if R.get("colony") else ("ruling" if R.get("ruling") else "hierarchy %s" % R.get("hierarchy"))
                    tint.append((n, "%s of %s (%s)" % (names[R["vassal"]], names[R["suzerain"]], src),
                                 "opened %d" % R["since"] if opened else "since %d" % R["since"], state))
                elif R["kind"] in ("contest", "occupation") and R["since"] <= b_ and (R["end"] is None or R["end"] >= a_):
                    n, state = rel_cells(R["id"])
                    if R["kind"] == "contest":
                        what = "contest %s / %s%s" % (names[R["a"]], names[R["b"]], (" (%s)" % R["war"]) if R.get("war") else "")
                    else:
                        what = "occupation of %s's land by %s" % (names[R["owner"]] if R["owner"] >= 0 else "nobody", names[R["occupier"]])
                    cont.append((n, what, "since %d" % R["since"], state))
            for title, lst, doc in (("Colony and hierarchy relations opened or closed", tint,
                                     "Tints from data/colonies.csv and data/hierarchy.csv (and rulings with a status)."),
                                    ("Contests and occupations", cont, "Open at some point in the window.")):
                lst.sort(key=lambda x: (-x[0], x[1]))
                L.append("## %s (%d)" % (title, len(lst)))
                L.append("")
                if lst:
                    L.append(doc)
                    L.append("")
                    L.append("| relation | cells | started | state |")
                    L.append("| --- | --- | --- | --- |")
                    for n, what, st_, state in lst[:cap["rel"]]:
                        L.append("| %s | %d | %s | %s |" % (md_cell(what), n, st_, state))
                    if len(lst) > cap["rel"]:
                        L.append("")
                        L.append("... and %d more" % (len(lst) - cap["rel"]))
                L.append("")
            # states alive
            alive = [i for i in range(comp.N) if not comp.umbrella[i] and comp.start[i] <= b_ and comp.end[i] >= a_]
            sc, ec = wd["start_count"], wd["end_count"]
            alive.sort(key=lambda i: (-max(int(sc[i]), int(ec[i])), names[i]))
            L.append("## States alive (%d)" % len(alive))
            L.append("")
            L.append("| slug | life | cells %d | cells %d |" % (a_, b_ + 1))
            L.append("| --- | --- | --- | --- |")
            for i in alive[:cap["alive"]]:
                L.append("| %s | %d..%d | %d | %d |" % (names[i], comp.start[i], comp.dos[i]["identity"]["end"]["year"], sc[i], ec[i]))
            if len(alive) > cap["alive"]:
                rest = alive[cap["alive"]:]
                L.append("")
                L.append("... and %d more, none above %d cells" % (len(rest), max(max(int(sc[i]), int(ec[i])) for i in rest)))
            L.append("")
            # neighbours with close colours
            close, nocol = [], 0
            for (pa, pb), edges_ in wd["adj"].items():
                if pa >= comp.N or pb >= comp.N:
                    continue
                ca, cb = colours.get(names[pa]), colours.get(names[pb])
                if not ca or not cb:
                    nocol += 1
                    continue
                for c_ in (ca, cb):
                    if c_ not in lab_ok:
                        lab_ok[c_] = hex_oklab(c_)
                la, lb = lab_ok[ca], lab_ok[cb]
                dist = sum((x - y_) ** 2 for x, y_ in zip(la, lb)) ** 0.5
                if dist < COLOUR_CLOSE:
                    close.append((edges_, names[pa], names[pb], dist, ca, cb))
            close.sort(key=lambda x: (-x[0], x[1], x[2]))
            L.append("## Neighbours with close colours (OKLab distance under %.2f) (%d)" % (COLOUR_CLOSE, len(close)))
            L.append("")
            L.append("Pairs sharing a border in this window whose colours.json colours are closer than %.2f (the colour "
                     "agent sets the real threshold); %d neighbour pairs have a state without a colour yet." % (COLOUR_CLOSE, nocol))
            L.append("")
            if close:
                L.append("| pair | shared cell edges (most) | distance | colours |")
                L.append("| --- | --- | --- | --- |")
                for e_, pa, pb, dist, ca, cb in close[:cap["col"]]:
                    L.append("| %s / %s | %d | %.3f | %s %s |" % (pa, pb, e_, dist, ca, cb))
                if len(close) > cap["col"]:
                    L.append("")
                    L.append("... and %d more" % (len(close) - cap["col"]))
                L.append("")
            return "\n".join(L) + "\n"

        cap = {"patch": 40, "conf": 25, "snap": 20, "skip": 25, "rel": 25, "alive": 80, "col": 25}
        txt = build(cap)
        for _ in range(8):
            if len(txt.encode("utf-8")) <= PACKET_MAX:
                break
            cap = {k: max(3, int(v * 0.7)) for k, v in cap.items()}
            txt = build(cap)
        with open(notes / "windows" / (w["id"] + ".md"), "w", encoding="utf-8") as f:
            f.write(txt)
        written += 1
        sizes.append(len(txt.encode("utf-8")))
    return {"packets": written, "largest_bytes": max(sizes) if sizes else 0}


def compare_phase_a(comp, pa, pc, y):
    n = comp.n
    with open(pa) as f:
        A = json.load(f)
    with open(pc) as f:
        C = json.load(f)
    oa = np.full(n, -1, np.int32)        # Phase A clio slug ids
    clio_names = sorted(A["owners"])
    for i, s in enumerate(clio_names):
        oa[from_runs(A["owners"][s])] = i
    oc = np.full(n, -1, np.int32)
    for s, runs in C["owners"].items():
        oc[from_runs(runs)] = comp.name_id[s]
    owned_a = oa >= 0
    owned_c = oc >= 0
    same = np.zeros(n, bool)
    for i, s in enumerate(clio_names):
        m = oa == i
        ds = comp.clio_to_dossiers.get(s, set())
        if ds:
            same[m] = np.isin(oc[m], list(ds))
    both = owned_a & owned_c
    has_clio = np.array([bool(comp.clio_slugs[i]) for i in range(comp.N)] + [False])
    comparable = both & has_clio[np.where(oc >= 0, oc, comp.N)]
    res = {"year": y, "phase_a_cells_owned": int(owned_a.sum()), "phase_c_cells_owned": int(owned_c.sum()),
           "owned_in_both": int(both.sum()), "same_state": int(same.sum()),
           "agreement_of_cells_owned_in_both": round(float(same.sum()) / max(int(both.sum()), 1), 4),
           "agreement_of_cells_owned_in_either": round(float(same.sum()) / max(int((owned_a | owned_c).sum()), 1), 4),
           "comparable_cells": int(comparable.sum()),
           "agreement_of_comparable_cells": round(float((same & comparable).sum()) / max(int(comparable.sum()), 1), 4),
           "phase_a_only": int((owned_a & ~owned_c).sum()), "phase_c_only": int((owned_c & ~owned_a).sum()),
           "phase_a_polities": len(A["owners"]), "phase_c_polities": len(C["owners"])}
    # per state differences (Phase C dossier view)
    diffs = []
    for s, runs in C["owners"].items():
        did = comp.name_id[s]
        mc = oc == did
        cs = set(comp.clio_slugs[did])
        ma = np.isin(oa, [clio_names.index(x) for x in cs if x in A["owners"]]) if cs else np.zeros(n, bool)
        diffs.append((int((mc ^ ma).sum()), s, int(mc.sum()), int(ma.sum()), int((mc & ma).sum())))
    covered = set()
    for did in range(comp.N):
        covered.update(comp.clio_slugs[did])
    for s in A["owners"]:
        if s not in covered:
            ma = oa == clio_names.index(s)
            diffs.append((int(ma.sum()), "(clio only) " + s, 0, int(ma.sum()), 0))
    diffs.sort(reverse=True)
    res["largest_differences"] = [{"slug": s, "phase_c_cells": c, "phase_a_cells": a, "common": b, "cells_differing": d}
                                  for d, s, c, a, b in diffs[:25]]
    return res


README_BEGIN = "<!-- compile_dossiers.py: begin generated section -->"
README_END = "<!-- compile_dossiers.py: end generated section -->"


def fmt_int(v):
    return "{:,}".format(int(v))


def write_readmes(comp, wins, stage, out, args, full):
    today = date.today().isoformat()
    st = out["stats"]
    # ---- anchors-c/README.md
    anchors = sorted((p for p in (stage / "data" / "anchors-c").glob("*.json")),
                     key=lambda p: (-int(p.stem[1:]) if p.stem[0] == "m" else int(p.stem[1:])))
    lines = []
    for p in anchors:
        with open(p, encoding="utf-8") as f:
            a = json.load(f)
        lines.append("| %s | %d | %s | %d | %s | %d | %d | %d |" % (
            p.stem, a["year"], a["as_of"].split(" (")[0], a["polities"], fmt_int(a["cells_owned"]),
            sum(len(g) for g in a["status"].values()), len(a["relations"]["contests"]) + len(a["relations"]["occupations"])
            + len(a["relations"]["vassals"]), round(p.stat().st_size / 1024)))
    txt = """# Phase C anchors (compiled from the reviewed dossiers)

Written by `tools/compile_dossiers.py` on %(today)s (run it again after the dossiers change; see
`notes/phase-c/README.md`). These are the fixed handoff states of the Phase D windows
(`compiled/README.md` lists the windows): every anchor is the cell ownership **on 1 January of its
year, after every event dated in an earlier year**, so window `[a, b]` starts from anchor `a` and,
after every change it lists for the years a..b, ends exactly at anchor `b + 1`. The Phase A anchors in
`data/anchors/` (Cliopatria only) are left untouched as the comparison baseline.

Two files break the 1 January rule on purpose and say so in `as_of`: `p2026.json` is the final
snapshot, the map at the end of 2026 after every event; `p2030.json`, the end anchor of the last window
(2020 to 2029), holds the same cells, since the run stops at 2026 and nothing is dated later.

## Format

```json
{"year": 1600, "as_of": "1 January 1600 (after every event dated 1599 or earlier)",
 "grid": "land_r5.txt", "land_cells": 524441,
 "owners": {"ming-dynasty": ["401233-401240", 401242], ...},
 "status": {
   "vassal":    [{"owner": "joseon", "suzerain": "ming-dynasty", "relation": 12, "cells": [...]}],
   "constituent": [{"owner": "duchy-of-styria", "suzerain": "habsburg-monarchy", "relation": 2635, "cells": [...]}],
   "occupied":  [{"owner": "kingdom-of-france", "occupier": "kingdom-of-england", "relation": 40, "cells": [...]}],
   "contested": [{"owner": "kingdom-of-france", "claimants": ["kingdom-of-france", "kingdom-of-england"],
                  "relation": 41, "cells": [...]}]},
 "relations": {
   "contests":    [{"id": 41, "a": "<slug>", "b": "<slug or name>", "since": 1415, "war": "...", "event": "<slug>/ledger/<i>", "cells": 312}],
   "occupations": [{"id": 40, "occupier": "<slug or name>", "owner": "<slug, name or null>", "since": 1417, "event": "...", "cells": 88}],
   "vassals":     [{"id": 12, "suzerain": "<slug>", "vassal": "<slug or name>", "since": 1401, "event": "...", "cells": 2210},
                   {"id": 4154, "suzerain": "united-kingdom", "vassal": "british-africa", "since": 1885,
                    "event": "data/colonies.csv: british-africa, metropole united-kingdom from 1885", "cells": 23586, "colony": true}]},
 "polities": 97, "cells_owned": 184232, "compiler": "tools/compile_dossiers.py"}
```

- `owners`: dossier slug -> runs of indices into `data/grid/land_r5.txt` (`"start-end"` inclusive or a
  single integer; `grid.from_runs` / `grid.to_runs` convert), every cell the state owns whatever its
  status. A cell is in at most one slug's runs (checked by the self-check). Cells in no slug's runs are
  nobody's land (neutral), unless `status.occupied` lists them with `owner: null`.
- `status`: the cells whose status is not direct, grouped by owner, the other party and the relation;
  a cell an owner holds that is not listed here is **direct**. `constituent`: the owner is a member of
  `suzerain` (an Imperial Estate, a Soviet republic), from `data/hierarchy.csv` (rule R3 in
  `notes/phase-c/README.md`); drawn like a vassal. `vassal`: the owner is a vassal of
  `suzerain` (when the vassal has no dossier the owner is the suzerain itself, drawn in its own vassal
  tint; a colony's cells are its metropole's vassal land, rule R1 in `notes/phase-c/README.md`).
  `occupied`: held by `occupier` without annexation (owner null when the land belonged to
  nobody or to a state without a dossier). `contested`: fought over by `claimants` = [holder, challenger]
  (a challenger without a dossier appears by name).
- `relations`: every contest, occupation and vassal relation open at that moment (opened by a
  `*_start` event and not yet closed by its `*_end`), with its id (the `relation` of the status groups),
  first year, opening event (`<slug>/ledger/<index>`), the other names involved and its current number of
  cells (a relation can be open with 0 cells when its region held none of the parties' land). A vassal
  relation with `"colony": true` is a colony's tie to its metropole from `data/colonies.csv` (opened at
  the start of the row, `event` names the row), not a ledger event; an explicit suzerainty from the
  ledger shows over it while it is open. These are the window agents' `handoff.open_*` lists at the
  window boundary. A relation with `"hierarchy": "constituent"` or `"vassal"` (and its `confidence`) is a
  row of `data/hierarchy.csv` (rule R3), opened at the start of the row and closed at its end, not a
  ledger event; like a colony's, a suzerainty from the ledger shows over it while it is open.
- `polities`: slugs with at least one cell; `cells_owned`: cells with an owner.

Status codes are exclusive: a cell has one owner and one status. Vassals, occupations and contests are
the window brief's rule 4 and rule 6; colours, tints, hatches and blends are applied by the packer from
`colours.json`, never stored here.

## The anchors

| file | year | as of | polities | cells owned | status groups | open relations | KB |
| --- | --- | --- | --- | --- | --- | --- | --- |
%(rows)s
""" % {"today": today, "rows": "\n".join(lines)}
    with open(stage / "data" / "anchors-c" / "README.md", "w", encoding="utf-8") as f:
        f.write(txt)
    # ---- compiled/README.md (generated section)
    wl = []
    for w in wins:
        p = stage / "compiled" / "_draft" / (w["id"] + ".json")
        if not p.exists():
            continue
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        nch = sum(len(v["changes"]) for v in d["years"].values())
        ncells = sum(c.get("n", 0) for v in d["years"].values() for c in v["changes"])
        ncap = sum(len(v["captions"]) for v in d["years"].values())
        wl.append("| `%s` | %d | %d | %s | %s | %d | %s | %d | %d | %d |" % (
            w["id"], w["from"], w["to"], w["start_anchor"], w["end_anchor"], len(d["years"]), fmt_int(ncells),
            ncap, len(d["handoff"]["keyframe_snaps"]), len(d["handoff"]["unresolved_regions"])))
    sect = """%(begin)s
## Windows and drafts (generated by tools/compile_dossiers.py, %(today)s)

119 windows: 76 centuries from 6000 BCE to 1599 and 43 decades from 1600 to 2029. A window's id is
its first and last year as anchor stems (`m` + four digits for BCE, `p` for CE: `m6000-m5901` is
6000 to 5901 BCE, `p1600-p1609` is 1600 to 1609). It starts from `data/anchors-c/<start_anchor>.json`
(1 January of its first year) and ends at `data/anchors-c/<end_anchor>.json` (1 January of the year
after its last); the last window ends at `p2030`, the map at the end of 2026 (the run stops at 2026).

`compiled/_draft/<window>.json` is the deterministic draft of each window, sliced from one run of
`tools/compile_dossiers.py` over every dossier, in the format of `briefs/window-brief.md` section 2,
plus: `"draft": true`, `"compiler"`, a cell count `"n"` on every change and contest, and in `handoff`
the lists `keyframe_snaps` (dossier gaps: years where the keyframe of record differs from the ledger by
more than 20 cells or 5 percent and the state was set to the keyframe) and `skipped` (events not applied,
with the reason). Each `handoff.conflicts` entry names the rule that settled it (R2 succession, a ruling
of `data/patches/<window>.json`, R3 hierarchy, rule 4, R1 colony, the size rule); the window agents'
corrections in `data/patches/` (see its README) are applied on every compile, and a change, caption or
snap they produced names its patch file; a colony's land is drawn as its metropole's vassal land (`data/colonies.csv`,
`"colony": true` in `open_vassals`), and a change whose `event` is `data/colonies.csv: ...` is the
metropole's tint starting or changing.

**Status `constituent`.** Beside the brief's `direct | vassal | occupied | contested | neutral`, a change
(and an anchor's `status` groups) can carry `"status": "constituent"` with `"suzerain": "<slug>"`: the
owner is a member of the suzerain (an Imperial Estate of the Holy Roman Empire, a Soviet republic of the
USSR, a duchy of the Habsburg Monarchy), drawn in the suzerain's tint like a vassal but marking
membership rather than overlordship. It comes from `data/hierarchy.csv` (rule R3 in
`notes/phase-c/README.md`), as do `vassal` cells whose relation is flagged `"hierarchy": "vassal"`; such
relations appear in `open_vassals` with `"hierarchy": "constituent"` or `"vassal"`, and a change whose
`event` is `data/hierarchy.csv: ...` is that tint starting or ending. Window agents keep these values as
they are; the packer treats `constituent` like `vassal` for colour. Each draft's first year starts from its start anchor and its last year ends at its end
anchor by construction, so `handoff.disagreements` is empty and every seam is clean; the window agents
review and fix their draft and write `compiled/<window>.json`. Notes on the run and the reports:
`notes/phase-c/README.md`.

| window | from | to | start anchor | end anchor | years listed | cells changed | captions | keyframe snaps | unresolved regions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
%(rows)s
%(end)s
""" % {"begin": README_BEGIN, "end": README_END, "today": today, "rows": "\n".join(wl)}
    with open(stage / "compiled" / "README.section.md", "w", encoding="utf-8") as f:
        f.write(sect)
    # ---- notes/phase-c/README.md
    write_notes_readme(comp, stage, out, args, full)


def patch_line(out):
    pc = (out.get("patches") or {}).get("counts") or {}
    if not pc.get("files"):
        return "no patch files"
    return ("%d files (%d skipped); applied %d events, %d keyframe overrides and %d rulings (%d of them settled "
            "conflicts); skipped %d entries" % (
                pc.get("files", 0), pc.get("files skipped", 0), pc.get("events applied", 0),
                pc.get("keyframe_overrides applied", 0), pc.get("rulings applied", 0),
                out["patches"].get("rulings_settling", 0),
                sum(v for k, v in pc.items() if k.endswith(" skipped") and k != "files skipped")))


def write_notes_readme(comp, stage, out, args, full):
    st = out["stats"]
    today = date.today().isoformat()
    sc = out.get("self_check") or {}
    comps = out.get("phase_a") or []
    cmp_lines = []
    for c in comps:
        cmp_lines.append("| %d | %s | %s | %s | %s | %.1f%% | %.1f%% | %.1f%% | %s | %s |" % (
            c["year"], fmt_int(c["phase_a_cells_owned"]), fmt_int(c["phase_c_cells_owned"]), fmt_int(c["owned_in_both"]),
            fmt_int(c["same_state"]), 100 * c["agreement_of_cells_owned_in_both"],
            100 * c["agreement_of_comparable_cells"], 100 * c["agreement_of_cells_owned_in_either"],
            fmt_int(c["phase_a_only"]), fmt_int(c["phase_c_only"])))
    big = []
    for c in comps:
        big.append("- %d: " % c["year"] + "; ".join("%s %s (C %s, A %s)" % (
            d["slug"], fmt_int(d["cells_differing"]), fmt_int(d["phase_c_cells"]), fmt_int(d["phase_a_cells"]))
            for d in c["largest_differences"][:10]))
    probs = "\n".join("| %d | %s | %s | %s | %s |" % (i + 1, fmt_int(p[0]), p[1], p[2], p[4].replace("|", "/"))
                      for i, p in enumerate(out["problems_top"][:20]))
    keys = sorted(st)
    stat_lines = "\n".join("| %s | %s |" % (k, fmt_int(st[k])) for k in keys)
    cr = out.get("claims_by_rule", {})

    def rule_line(k):
        v = cr.get(k, {"pairs": 0, "cells": 0, "claims": 0})
        return "%s pairs, %s cell-years, %s claims" % (fmt_int(v["pairs"]), fmt_int(v["cells"]), fmt_int(v["claims"]))
    sh = out.get("conflict_top_share", {})
    cats = out.get("conflict_categories", {})
    tot_c = out["conflict_cells"] or 1
    cat_lines = "\n".join("| %s | %s | %s | %.1f%% |" % (k, fmt_int(v["pairs"]), fmt_int(v["cells"]), 100.0 * v["cells"] / tot_c)
                          for k, v in sorted(cats.items(), key=lambda kv: -kv[1]["cells"]))
    top60 = "\n".join("| %d | %s | %s | %s | %s | %s..%s | %s |" % (
        i + 1, r[0], r[1], r[2] + ("" if r[7] == "reviewed" else " (heuristic)"), fmt_int(r[3]), r[5], r[6],
        (r[8] or "").replace("|", "/")[:70]) for i, r in enumerate(out.get("conflict_top60", [])))
    col = out.get("colonies", {})
    hier = out.get("hierarchy", {})
    low = "\n".join("| %s | %s | %s..%s | %s |" % (r[0], r[1] or "(none)", r[2], r[3], r[4].replace("|", "/")[:200])
                    for r in col.get("low_rows", []))
    rbc = col.get("rows_by_confidence", {})
    txt = """# Phase C: anchors and window drafts compiled from the dossiers

Written by `tools/compile_dossiers.py` (%(today)s run). One deterministic engine applies
`briefs/window-brief.md` section 3 (the twelve rules, keyframes versus the ledger, conflicts,
resolution) to every dossier for every year from 6000 BCE to 2026, starting from an empty world, and
slices the result into the 119 Phase D window drafts and their anchors. The window agents then review
and fix their window from its draft instead of compiling it themselves.

## How to run

```sh
mkdir -p /tmp/claude-0/work/compile-c && cd /tmp/claude-0/work/compile-c
python3 -I /mnt/project-files/history/tools/compile_dossiers.py --until 1900 --stage-only   # test: compile to 1900, compare 1600 and 1900 with Phase A, scratch only
python3 -I /mnt/project-files/history/tools/compile_dossiers.py                              # full run: writes and publishes everything below
python3 -I /mnt/project-files/history/tools/compile_dossiers.py --build-colonies             # the same, deriving data/colonies.csv again first (manual rows kept)
```

Re-run it after the dossiers or the gazetteer change: it copies new or changed dossiers from
`polities/` to `/tmp/claude-0/work/compile-c/polities/`, re-resolves only the region leaves whose
gazetteer tables changed (cache: `/tmp/claude-0/work/compile-c/cache/leaves.pkl`; `--refresh` drops it),
recompiles everything and rewrites `data/anchors-c/`, `compiled/_draft/`, the generated section of
`compiled/README.md` and this folder. Options: `--no-sync`, `--workers N`, `--stage-only` (leave the
outputs in `/tmp/claude-0/work/compile-c/stage/`), `--compare 1600,1900`, `--build-colonies`, `--no-rules`
(the size rule alone, without R1 and R2, for comparison). `data/colonies.csv` is read as it is when it
exists; it is derived (and published) only with `--build-colonies` or when it is missing.
This run: %(secs)s s end to end (region resolution is the slow part on a cold cache).

## This run in numbers

| | |
| --- | --- |
| dossiers | %(dossiers)s (%(invalid)d unreadable or failing `tools/validate_dossier.py`, left out%(invalid_list)s) |
| ledger events | %(events)s: %(applied)s applied, %(skipped)s skipped |
| events skipped because a region does not resolve | %(unres_ev)s (all unresolved specs, keyframes and successor lands included: %(unres_all)s) |
| distinct unresolved names | %(unres_names)s (`unresolved_names.csv`) |
| conflicts the size rule still settles | %(cpairs)s pairs, %(ccells)s cell-years (cells summed over the claims), %(cevents)s claims |
| settled by R2 (succession) | %(r2)s |
| settled by R3, a constituent against its parent | %(r3c)s |
| settled by R3, a vassal against its parent | %(r3v)s |
| settled by R3, two dossiers of one state | %(r3s)s |
| data/hierarchy.csv | %(hrows)s rows, %(hspans)s spans applied (%(hkinds)s); %(hnotes)s notes in `hierarchy_check.csv`, %(hbad)s rows not applied |
| cells drawn in a hierarchy tint (R3), summed over the years | %(htint)s |
| settled by R1, a colony against another dossier | %(r1c)s |
| settled by R1, two colonies of one metropole | %(r1m)s |
| settled by rule 4, a vassal against its suzerain | %(r4)s |
| data/colonies.csv | %(colrows)s rows for %(colcols)s colony dossiers: %(colhigh)s high, %(colmed)s medium, %(collow)s low confidence; %(colnone)s rows without a metropole; %(colissues)s problems (`colonies_check.csv`) |
| keyframe snaps (dossier gaps) | %(snaps)s |
| anchors written | %(anchors)s |
| adjacent pairs (any year) | %(adj)s |
| self-check | %(selfcheck)s |
| `*_end` events that close nothing open | %(unclosed)s |

Every counter of the run (`run_summary.json` has them all):

| counter | value |
| --- | --- |
%(stat_lines)s

## Rule R3 (hierarchy)

`data/hierarchy.csv` (documented at the end of `data/README.md`) says which state sat inside which:
one row per child, parent and span (`child,parent,from,to,kind,confidence,evidence`), `kind`
constituent (a member of the parent: an Imperial Estate, a Soviet republic), vassal (its own ruler
under the parent's overlordship) or same_state (two dossiers drawing one state). The classifiers wrote
it from this folder's nested, same-state and colony pairs of 500 cell-years or more. R3 comes right
after R2 in the conflict order (see the list below):

- **same_state**: in the row's years the parent's dossier is drawn; the child's claims on cells the
  parent holds yield, and the parent's claims take the child's cells (kashmir over the Lohara and Utpala
  dynasties, the East India Company over `british-empire` 1757-1858, the Habsburg Netherlands over
  `habsburg-monarchy` 1487-1515).
- **constituent or vassal**, in a year of the row: on a cell both the child and the parent claim, the
  child owns it, with status `constituent` or `vassal` and suzerain the parent. **Chains**: when rows
  link three states (an Imperial Estate inside an estate inside the Empire), the deepest child wins
  against any ancestor and its suzerain is its immediate parent.
- **The tint**: a row of confidence 2 or 3 also gives the child's other cells that status and suzerain,
  for the row's years the child is alive, like a colony's metropole tint: a relation flagged
  `"hierarchy"` (`data/anchors-c/` relations, `handoff.open_vassals`) opens at the start of the row's
  first year (the change's `event` names the row) and closes at the start of the year after its last;
  land the child gains meanwhile takes the tint; a suzerainty the dossiers record with `vassal_start`
  shows over it, and the row's tint returns when that ends (the dossier wins where it has an event). A
  parent's keyframe counts its children's tinted cells as its own, so it no longer claims them. A row of
  confidence 1 changes only the cells R3 settles in a conflict.
- **Colonies** keep R1: a colony child's row applies only to years without a `data/colonies.csv` row.
- Spans are clipped to the years both dossiers are alive; rows the compiler could not apply (unknown
  slug, bad years, no common life) and every clipped span are listed in `hierarchy_check.csv`.

R3 conflicts settled this run: %(r3text)s. Cells drawn in a hierarchy tint, summed over the years:
%(htint)s.

## Rules R1 (colonies) and R2 (succession)

Most of the conflicts of the first run were structural: a colony against its metropole or its
aggregate (the Spanish Empire against its viceroyalties, French Africa against French West Africa,
the British colonial empire against the Australian colonies), and a state against its own predecessor
or successor (the RSFSR against the USSR, colonial Brazil against the Empire of Brazil). Two rules now
settle them before the size rule. A conflict is a found or a keyframe claiming a cell another
dossier holds; a cell that a dated ledger event of the same year moved is settled by that event first.
Then, in this order:

1. **R2, succession.** When B is A's successor (A's `identity.successors` or B's
   `identity.predecessors` names the other) and the year is at or after B's start, B owns the cell.
   When each lists the other, the one born later wins. R2 holds for the whole overlap, also when the
   listed successor is the older state (the Sumerian city-states, born -3400, are listed as the
   successor of Ur, Umma and Kish; window patches give those cities their own land). A switch in the
   script, `R2_BORN_AFTER` (off), would give R2 only to a successor born after its predecessor; it was
   tried in round 12 and left off, because it moved 1.27M owner cell-years in 86 windows reviewed under
   this rule (the pairs it moves: `/tmp/claude-0/work/r12/r2_moves.json`).
2. **Rulings** (`data/patches/<window>.json`, the section on patches below): a window agent's ruling for
   the pair and year, limited to its region's cells when it has one, names the winner (and optionally a
   status).
3. **R3, hierarchy** (`data/hierarchy.csv`, the section above): same_state rows draw the parent; in a
   constituent or vassal row the deepest child owns the cell, in its immediate parent's tint.
4. **Rule 4, a vassal keeps its land.** When one of the two is the other's open vassal (a
   `vassal_start` not yet closed), the vassal keeps or takes the cell, in its suzerain's tint. Without
   this R1 would let a colony's keyframe swallow the protectorates the colony itself records (the
   sultanates of the Dutch East Indies, the princely states of the British Empire in India).
5. **R1, colonies.** Each type-colony dossier has a metropole by years in `data/colonies.csv`. When
   two colonies of the same metropole claim a cell, the smaller (Cliopatria area that year, else the
   compiled area) owns it: the specific colony wins against the aggregate (Queensland against the
   British colonial empire, Anglo-Egyptian Sudan against British Africa). When a colony with a metropole
   that year and any other dossier claim a cell, the colony owns it.
6. Otherwise **the size rule**: the state with the smaller Cliopatria area that year wins.

**The colony tint.** Every colony cell carries status `vassal` with `suzerain` = the colony's metropole
for that year, with or without a conflict: the compiler opens a vassal relation flagged
`"colony": true` (`data/anchors-c/` relations, `handoff.open_vassals`) at the start of each
`colonies.csv` row, closes it when the row ends or the metropole changes, and puts it under any
suzerainty the ledger records for the colony (an explicit `vassal_start` shows above it; when that
ends, the metropole's tint returns). Land the colony gains later is tinted the same way; a contest or
occupation over colony land returns to the tint when it ends. A colony row without a metropole (a
Greek apoikia, a condominium, a year whose metropole has no dossier) leaves the colony an ordinary
state for those years.

**`data/colonies.csv`** has one row per colony and stretch of years: `colony, metropole, from, to,
basis, confidence` (`metropole` empty: no metropole those years). A metropole can change
(Spanish then Austrian Milan; the Dutch colonies under the Batavian Republic, the French Empire in
1811-1814 and the Netherlands). The file is derived by `derive_colonies` and can be edited by hand:
a row whose `basis` starts with `manual` survives a new derivation. The derivation scores, for every
colony and year, the candidate metropoles alive that year:

- the home states of the nation the colony's slug prefix or name names (`british-`, `french-`,
  `spanish-`, `portuguese-`, `dutch-`, "New France", "New Sweden"...): +3; else of a nation its notes
  name, up to +2 for the most named (the table `NATIONS` lists the home states of %(nnat)d nations);
- the same colour family as the colony, which follows the metropole's (+2.5, or +1.5 when the family
  holds several nations' home states, as France's holds the Netherlands' and Belgium's);
- the colony's suzerain in a first compile with the size rule only: +4;
- the candidate's keyframe shape holding the colony's that year (the sovereign state whose claim
  contains it): up to +2;
- mentions of the candidate in the dossier: up to +1; a predecessor or the found counterpart of the
  colony's own nation: +0.5.

An aggregate colony (British Africa, French Africa, the British colonial empire, German Africa...) is
a candidate too and stands for its own metropole, so every chain ends at a sovereign state, never at
another colony. When two home states of one nation are alive at once (the Spanish Empire and the
Kingdom of Spain, the Portuguese Empire and the Kingdom of Portugal, the Swedish Empire and the
Kingdom of Sweden, the USSR and the RSFSR) the one listed first in `NATIONS` is taken unless the other
scores more than a point higher. A metropole needs 2.5 points. Confidence: **high** at 5 points with a
lead of 2 over the best metropole of another nation, **medium** at 3 with a lead of 1, **low** below.
`COLONY_MANUAL` in the script fixes %(colmanual)s colonies where the scores mislead (the Italian
possessions that passed from Spain to Austria, Saint-Domingue, Spanish Tunis, the Greek apoikiai
and the New Hebrides condominium without a metropole, the 1945 occupation governments in Korea,
Nauru); their basis says so.

The %(collow)s low-confidence rows:

| colony | metropole | years | basis |
| --- | --- | --- | --- |
%(low)s

**Engine fixes that went with the rules.** A `vassal_start` recorded by the vassal (the schema wants
the suzerain to record it, with the vassal as counterpart) used to make the vassal the suzerain in
several cases, and when both dossiers recorded the same vassalage the two records could open two
opposite relations. Checking the colony tint showed it: the Kingdom of Taqali was drawn as British
Africa's suzerain over 15,000 cells from 1898 and as Turco-Egyptian Sudan's over about 3,000 cells
1821-1884, Kongo as Portuguese Angola's over 1,190 cells 1859-1914, Ndongo as Angola's, and Belgium
as the Belgian Congo's vassal. The role rules in "How the brief was read" now settle these: the
metropole is always the suzerain of its own colony; for a same-year pair of records the party whose
shape holds the region is the vassal and the second record joins the first's relation (opposite
same-year relations went from 18 pairs to 0: Himyar under Axum, Aquitaine under France in 990, Ryukyu
under the Southern Ming, the Later Guptas under Harsha); a recorder that holds the region inside its
own shape, against a counterpart with land elsewhere and none of it there, is the vassal (Qatna under
Mitanni, Mitanni under the Hittites, Qocho under the Kara-Khitans, Chola under the Pandyas, Bima
under Gowa, Mengjiang under the Reorganized National Government); and a colony weighs as its
metropole when sizes decide. And a successor that has already ended in the same year's deaths no
longer receives land (Min kept 287 cells from 945 to 2026). In all, 47 of the 1,654 `vassal_start`
records now open a different relation or join one.

## The conflicts that remain

The size rule still settles %(cpairs)s pairs (%(ccells)s cell-years). The largest 60 pairs hold
%(sh60)s of those cell-years, the largest 100 %(sh100)s, 200 %(sh200)s and 400 %(sh400)s. By category
(the largest pairs categorised by hand, `CONFLICT_REVIEWED` in the script; the rest by a heuristic:
a type-rebel dossier; a shared Cliopatria name, Wikipedia title, Wikidata id or primary name; a colony of
another metropole or of none; one year's conflict reaching half the smaller state's area, nested;
otherwise unrelated):

| category | pairs | cell-years | share |
| --- | --- | --- | --- |
%(cat_lines)s

- **nested**: a state inside a larger one that is not its colony: the Central Asian SSRs inside the
  USSR, the stem duchies inside the Empire, the Rajput and princely states inside the Mughal Empire and
  the Raj, warlord cliques inside the Republic of China, nominal vassals of the Abbasid caliphate.
  These want a `vassal_start` in one of the two dossiers (or a keyframe that leaves the inner state
  out), not a compiler rule;
- **unrelated**: two distinct states whose shapes claim the same land (Tibet and the Republic of
  China, the Han and the Xiongnu, Mexico and the United States before 1848);
- **same state**: two dossiers for one state whose lives overlap (the British Empire in India and the
  East India Company; Kashmir and its Lohara dynasty);
- **rebel**: a type-rebel dossier against the state it rebels in;
- **colony**: a colony against a colony of another metropole, or one without a metropole.

The 60 largest:

| rank | pair | | category | cell-years | years | cells won by |
| --- | --- | --- | --- | --- | --- | --- |
%(top60)s

`conflicts.csv` lists every pair the size rule settled; `conflicts_settled_by_rule.csv` the pairs R1,
R2 and rule 4 settled.

## Phase A comparison

Phase C anchor (1 January, dossiers) against Phase A anchor (Cliopatria shapes alive that year).
"Same state" counts a cell when the Phase C owner is a dossier that lists the Phase A owner among its
`cliopatria_names`.

| year | Phase A cells owned | Phase C cells owned | owned in both | same state | agreement (both) | agreement (comparable) | agreement (either) | Phase A only | Phase C only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
%(cmp)s

"Comparable" leaves out the cells whose Phase C owner is a dossier with no Cliopatria name (a state
Cliopatria lacks, most often a colony or viceroyalty the dossiers split out of Cliopatria's aggregate
empire: the Viceroyalty of Peru and New Spain out of the Spanish Empire in 1600, Canada, the Australian
colonies and British Africa's protectorates out of the British Empire in 1900). Those splits, and the
dossiers' corrected life spans (Cliopatria keeps the Golden Horde alive in 1600; the dossier ends it in
1502), are most of the difference; the rest is the ledger moving borders between keyframes.

Largest per-state differences (cells in one and not the other):

%(big)s

## The problems that move the most land

| rank | cells | kind | state(s) | what |
| --- | --- | --- | --- | --- |
%(probs)s

`problems.csv` has the first 3,000. Keyframe snaps are the ledger's gaps: the keyframe of record says
the state held land (or lost land) that no event between the keyframes moves; most trace to an event
whose region does not resolve (`unresolved_events.csv`) or to a ledger that covers only part of the
period. Conflicts are two states whose shapes claim the same cells.

## The names the gazetteer lacks, most needed first

| kind | name | events | dossiers | error |
| --- | --- | --- | --- | --- |
%(unres_top)s

The full list is `unresolved_names.csv`; each failing spec with its dossier and place is in
`unresolved_events.csv`.

## Files

| file | what |
| --- | --- |
| `unresolved_events.csv` | every event, keyframe and successor land whose region spec does not resolve: slug, where, year, type, the failing leaves, the gazetteer's error, the spec |
| `unresolved_names.csv` | the same aggregated by failing name (kind, name, events, dossiers, event types, examples, error with the closest matches), most used first: the gazetteer agent's work list |
| `skipped_events.csv` | every event not applied, with the reason; also every merge whose counterpart has no living dossier, with the branch that applied (a gain from nobody, or nothing moved) |
| `noop_events.csv` | events applied that changed no cell (the counterpart did not hold the region, the region was already the state's) |
| `unclosed_ends.csv` | `*_end` events that close nothing open |
| `conflicts.csv` | the conflicts the size rule settled, by pair: category (and whether reviewed by hand), the most one year's conflict holds of the smaller state, cells summed over the claims (cell-years), the most in one year, years, who won how many cells, the context (found or keyframe), claims |
| `conflicts_settled_by_rule.csv` | the same for the pairs R2, R1 and rule 4 settled, with the rule |
| `colonies_check.csv` | problems found reading `data/colonies.csv` (unknown slugs, metropoles not alive, overlapping rows, colonies without a row) |
| `keyframe_snaps.csv` | dossier gaps: slug, shape_id, year, cells differing, added, removed, kept by others, the state before, the keyframe |
| `conflict_places.csv` | where the top 150 pairs of `conflicts.csv` (by cell-years) dispute land, one row per pair and conflict year (a pair with more than 12 conflict years keeps the 12 with the most cells, and `years_note` says so): pair_rank, slug_a, slug_b, year, cells (distinct cells that year), winner (cells won when both won some), places (the top 6 admin-1 regions of the cells, "Name (Country) n", from `data/gazetteer/admin1.jsonl`, a cell two rows list going to the smaller; a cell no admin-1 row lists gives "no admin-1 (Country)", or "unmapped" when no country row lists it either), the centroid (lat, lon) and bounding box (lat_min, lon_min, lat_max, lon_max; lon_min greater than lon_max means the box crosses the antimeridian), claim_a and claim_b: the event or keyframe each side claimed the cells by (for the claimant, the event or keyframe that made the claim; for the holder, the one that gave it the cells: `slug/ledger/i`, `slug/keyframe/shape_id` with its correction's `text` when at most 200 characters, or a `data/colonies.csv` or `data/hierarchy.csv` row), with the cells of each when there are several (top 3) |
| `snap_places.csv` | where the top 100 keyframe snaps by cells differing (and the top 100 by cells moved, the order of `keyframe_snaps.csv`) add and remove land: both ranks, slug, shape_id, year, cells differing, added, removed, added_places and removed_places (top 6 admin-1 regions, as above), the cells the keyframe wanted that others kept (count, the top 3 holders, their top 6 regions), the previous keyframe and its year, and ledger_between: the dossier's ledger events after the previous keyframe's year up to the snap's year (from its start when there is none) |
| `areas.csv` | area per state at each anchor against Cliopatria's area that year (the model is `data/anchors/_areas.csv`) |
| `adjacency.csv` | every pair of states sharing a border in any compiled year (owners, whatever the status; land neighbours only, so a strait separates): first year, last year, years adjacent, the most pairs of neighbouring cells across their border in one year (about the border's length in cells), for the colour agent's neighbour rule |
| `deaths.csv` | each state's end: cells it held, to successors, to nobody |
| `problems.csv` | snaps, conflicts and ends to nobody ranked by cells |
| `phase_a_comparison.json` | the comparison above with the 25 largest per-state differences per year |
| `run_summary.json` | every number of the run |
| `patches_check.csv` | every entry of `data/patches/<window>.json`: window, kind, index, slug (for a ruling, its two slugs joined by a vertical bar), outcome (applied, skipped, note) and why; for a ruling, the cell-years it settled |
| `patch-overrides.csv` | every keyframe a patch now controls (an applied `keyframe_overrides` entry): window, shape_id, slug. A dossier round that edits one of these keyframes in the dossier changes nothing on the map while the patch stands |
| `windows/<window>.md` | one review packet per window (under 25 KB): its patch file's entries and the rulings in force, its size-rule conflicts by pair with the admin-1 regions, its keyframe snaps with the regions added and removed, the 10 years with the most cells changed (where, by which events), skipped events and unresolved regions, colony and hierarchy relations opened or closed, contests and occupations, the states alive with their cells at its start and end, and neighbour pairs whose `colours.json` colours are closer than 0.08 in OKLab; each list sorted by cells and cut with a count of the rest |

## Patches (data/patches/<window>.json)

The window agents record corrections in one file per window, which every compile applies (the format,
with an example of each kind, is in `data/patches/README.md`; nothing is written back into the
dossiers):

- **events**: extra ledger events (a ledger event plus `slug`), applied as if they were in that dossier's
  ledger, after the dossier's own events of the same year and month. `found` and `dissolve` are refused
  (a state's life is its dossier's). The act is `data/patches/<window>.json: events/<k>`, so the change's
  `event`, the caption's `"patch"` and the skipped and no-op lists name the file.
- **keyframe_overrides**: a `keyframe_review` entry (plus `slug`, with `why` for `note`) replacing the
  dossier's entry for that `shape_id` (added when it has none); the first file in window order wins
  when two override one shape. Snaps, captions and changes name it: `<slug>/keyframe/<shape_id>
  [data/patches/<window>.json: keyframe_overrides/<k>]`.
- **rulings**: `{years, a, b, winner, status?, suzerain?, region?, source, why}` settle the pair's
  conflicts in those years (after R2, before R3; above): with a region only on its cells, otherwise on
  every cell both claim. With `status` (vassal or constituent with `suzerain`, occupied with `suzerain`
  the occupier, contested) the cells the winner gets or keeps take that status in a relation flagged
  `"ruling"`, which closes at the start of the year after the ruling's last (or when a party ends). The
  rule of a settled conflict is `ruling <window>/rulings/<k>`.

Each entry is checked as `tools/validate_dossier.py` checks a dossier (the schema of a ledger event or a
keyframe entry, the shape's owner, from/to for a new keyframe, the life span; regions through the
gazetteer); a bad entry or file is listed in `patches_check.csv` and skipped, never fatal. Patches dated
outside their window are applied with a note. This run: %(patch_line)s.

## How the brief was read (where it is silent or ambiguous)

- **Order within a year.** Ledger events in month order (an event without a month takes the month of
  the event before it in the same dossier and year, so a dossier's own order is kept; births first
  within a month), then keyframe snaps, then deaths (rule 7: after the year's other events). An `*_end`
  (vassal, contest, occupation) of one dossier goes before an `*_start` of another dossier of the same
  month, or where either month is unknown (no event of its dossier in that year has a month), when the
  two regions share land: a relation one state ends that year is closed before another opens over it
  (fix round fx-02: Han's protectorate of the Western Regions and the Xiongnu's in 74 and 91). The start
  waits, with the rest of its dossier's year, only while another dossier still has such an end to apply.
  This run moved %(ends_first)d starts.
- **Life span.** A dossier with a `dissolve` event ends at `identity.end.year`; one without is alive
  through 2026 (the validator ties both to the ledger). Events of a dead or unborn state, and of
  `umbrella` dossiers, move nothing (captions are kept).
- **Counterparts.** A counterpart is a dossier when it is a dossier slug or slugifies to one, and it
  counts only while that dossier is alive; otherwise it is a name without a dossier.
- **Regions with no land cell.** An event whose region resolves to no land cell moves no land: a gain,
  loss, split, merge, contest_start or occupation_start over it is skipped and logged in
  `skipped_events.csv` ("region resolves to no land cell"), and so is an `*_end` over it when nothing is
  open. The names the gazetteer documents as having no land cell are read as no land while it does not
  know them (`LANDLESS_NAMES` in the script: the Hawar Islands, Janan Island, Fasht ad Dibal, the Swan
  Islands and any Antarctic name), so they are not listed as unresolved; inside a union they add
  nothing. This run: %(landless_ev)s events skipped this way; landless names met: %(landless_names)s.
- **gain** takes the region's cells the counterpart holds; when the counterpart is nobody, has no
  living dossier or holds none of the region, the region's nobody's land. **loss** gives the region's
  cells this state holds to the counterpart (to nobody when it has no living dossier); a loss whose
  counterpart's dossier carries the matching gain (same year, counterpart this slug, a region that
  resolves) is applied once, as that gain. **split** gives the region's cells to the new state.
  **merge**: the state that ends that year is absorbed; otherwise the side holding more of the region
  is absorbed by the other. A merge whose counterpart has no living dossier that year (a name without a
  dossier, nobody, an umbrella, a slug not alive) is a gain from nobody: the region's cells nobody holds
  pass to the state and its own cells stay (round 12; round 11 gave the state's own cells in the region
  to nobody when it held more of the region than nobody did). Each one is listed in `skipped_events.csv`
  with the branch that applied ("applied as a gain from nobody", or "nothing moved" when the region holds
  none of nobody's cells). This run: %(merge_nocp)s.
- **found** takes the whole region (else the first keyframe's corrected shape) from nobody, the
  predecessors and the counterpart; cells of any other state are a conflict.
- **Relations.** One relation per pair is open at a time: both dossiers often record the same
  contest, occupation or vassalage, and the second record joins the first. Roles of a reciprocal record
  are taken from the land: an occupation recorded by the owner (it holds the region) is the
  counterpart's occupation. For a `vassal_start`, in this order: between a colony and its metropole
  that year, the metropole is the suzerain; when both dossiers record it in the same year, the party
  whose keyframe shape holds most of the region (half or more, the other's under half, 0.25 apart) is
  the vassal, and the second record joins the first's relation; a vassalage recorded by the vassal (it
  holds more of the region and is the smaller) is the counterpart's suzerainty; so is one whose larger
  counterpart already holds the region the recorder's own keyframe covers, and when neither holds any
  of the region the larger party is the suzerain; and when the recorder holds the region inside its own
  shape and the counterpart, which holds land elsewhere, holds none of it and its shape doesn't cover it,
  the recorder is the vassal. "Larger" weighs a colony with a metropole that year as its metropole (when
  the other party is neither that metropole nor another of its colonies). A vassal whose dossier holds
  none of the region (or has none) is
  drawn as the suzerain's land in the vassal tint; its `vassal_end` returns that land to the vassal's
  living dossier or to nobody. A state that is a vassal keeps its new land in the same tint; when one
  of two nested suzerainties ends, the other's tint returns. An `*_end`
  closes the whole relation; one that finds nothing open is counted (`unclosed_ends.csv`), unless the
  pair's other dossier closed it the same year.
- **Keyframes.** The keyframe of record in a year is the union of the state's keyframes alive that
  year (Cliopatria's shape for `ok`, the correction for `adjust` and `wrong`, the keyframe's own years
  for new keyframes, Cliopatria's for reviewed shapes); it is compared in each keyframe's `from` year
  (or the birth year when it starts earlier) against the state's cells plus the cells it holds as
  suzerain, occupier or claimant. The difference counted is what setting the state to the keyframe
  would actually move: the missing cells it may take (nobody's, or another state's under the conflict
  rule) plus its direct cells outside the keyframe. More than 20 cells or more than 5 percent of the
  state sets the state to the keyframe; less is ignored (coastline noise). Cells a smaller neighbour
  keeps are logged as conflicts in every keyframe year but never trigger a snap. Vassal, occupied
  and contested cells are left to their relations. A "years only" or "status only" verdict written in prose is not parsed:
  the shape is used at its Cliopatria years.
- **Conflicts.** A cell another state holds is claimed only by a birth or a keyframe; an event of the
  same year that moved the cell settles it for the event's state; otherwise R2, a ruling, R3, rule 4, R1 and the
  size rule decide in that order (above), and the pair is logged with the rule.
- **Colony cells in keyframes.** A colony's cells in its metropole's tint count as direct when a
  keyframe snap releases the cells outside the keyframe (cells in an explicit vassal, occupation or
  contest relation are left to it).
- **Regions.** Each leaf of a spec is resolved once by `tools/gazetteer.py` and cached; union,
  intersect and minus are composed exactly as the gazetteer composes them; a spec with any unresolved
  leaf is unresolved as a whole and its event skipped. `border_band` resolves against the Phase A
  anchors, as the gazetteer does.
""" % {"today": today, "secs": out["seconds"], "dossiers": fmt_int(out["dossiers"]), "invalid": len(out["invalid_dossiers"]),
       "events": fmt_int(out["events_total"]), "applied": fmt_int(st.get("events applied", 0)),
       "skipped": fmt_int(st.get("events skipped", 0)),
       "unres_ev": fmt_int(st.get("skipped: region does not resolve", 0)), "unres_all": fmt_int(out["unresolved_events"]),
       "landless_ev": fmt_int(st.get("skipped: region resolves to no land cell (the event moves no land)", 0)
                              + st.get("skipped: region resolves to no land cell and nothing is open", 0)),
       "landless_names": ", ".join(sorted({(json.loads(k).get("region") or json.loads(k).get("place") or
                                            json.loads(k).get("admin1") or json.loads(k).get("country") or k)
                                           for k in comp.res.landless})) or "none",
       "unres_names": fmt_int(out["unresolved_names"]), "cpairs": fmt_int(out["conflict_pairs"]),
       "ccells": fmt_int(out["conflict_cells"]), "cevents": fmt_int(out["conflict_events"]),
       "snaps": fmt_int(out["keyframe_snaps"]), "anchors": out["anchors_written"], "adj": fmt_int(out["adjacent_pairs"]),
       "selfcheck": ("anchors reached %d of %d; cells with two owners %d; change 'from' differing from the replay %d; cells listed twice in a year %d" % (
           sc.get("anchors_matching", 0), sc.get("anchors_checked", 0), sc.get("double_owner_cells", 0),
           sc.get("from_mismatch_cells", 0), sc.get("cells_listed_twice_in_a_year", 0))) if sc else "not run (test run)",
       "unclosed": "%d (contest_end %d, occupation_end %d, vassal_end %d; `unclosed_ends.csv`)" % (
           sum(st.get("%s_end closes nothing open" % k, 0) for k in ("contest", "occupation", "vassal")),
           st.get("contest_end closes nothing open", 0), st.get("occupation_end closes nothing open", 0),
           st.get("vassal_end closes nothing open", 0)),
       "unres_top": "\n".join("| %s | %s | %d | %d | %s |" % (r[0], r[1].replace("|", "/"), r[2], r[3], r[6].replace("|", "/")[:160])
                               for r in out.get("unresolved_top", [])),
       "stat_lines": stat_lines, "cmp": "\n".join(cmp_lines), "big": "\n".join(big), "probs": probs,
       "patch_line": patch_line(out),
       "ends_first": st.get("*_start applied after a same-year *_end of another dossier (ends first)", 0),
       "merge_nocp": "%s merges, %s applied as a gain from nobody, %s moving nothing" % (
           fmt_int(st.get(MERGE_NO_CP, 0)), fmt_int(st.get(MERGE_NO_CP_GAIN, 0)),
           fmt_int(st.get("skipped: " + MERGE_NO_CP_NONE, 0))),
       "r2": rule_line("R2 succession"), "r1c": rule_line("R1 colony"), "r1m": rule_line("R1 same metropole"),
       "r4": rule_line("vassal keeps"),
       "r3c": rule_line("R3 constituent"), "r3v": rule_line("R3 vassal"), "r3s": rule_line("R3 same state"),
       "hrows": hier.get("rows_read", 0), "hspans": hier.get("spans_applied", 0), "hnotes": hier.get("notes", 0),
       "hbad": len(hier.get("not_applied", [])),
       "hkinds": ", ".join("%s %d" % kv for kv in sorted(hier.get("spans_by_kind", {}).items())) or "none",
       "htint": "; ".join("%s %s" % (k, fmt_int(v)) for k, v in sorted(hier.get("tinted_cell_years", {}).items())) or "none",
       "r3text": "; ".join("%s: %d pairs, %s distinct cells, %s cell-years" % (
           k, v["pairs"], fmt_int(v["distinct_cells"]), fmt_int(v["cell_years"]))
           for k, v in sorted(hier.get("settled_in_conflicts", {}).items())) or "none",
       "invalid_list": (": " + ", ".join("`%s`" % s for s, _ in out["invalid_dossiers"][:20])) if out["invalid_dossiers"] else "", "colrows": fmt_int(col.get("rows", 0)), "colcols": col.get("colonies", 0),
       "colhigh": rbc.get("high", 0), "colmed": rbc.get("medium", 0), "collow": rbc.get("low", 0),
       "colnone": col.get("rows_without_metropole", 0), "colissues": col.get("issues", 0),
       "colmanual": len(COLONY_MANUAL), "low": low, "nnat": len(NATIONS),
       "sh60": "%.1f%%" % (100 * sh.get("60", 0)), "sh100": "%.1f%%" % (100 * sh.get("100", 0)),
       "sh200": "%.1f%%" % (100 * sh.get("200", 0)), "sh400": "%.1f%%" % (100 * sh.get("400", 0)),
       "cat_lines": cat_lines, "top60": top60}
    with open(stage / "notes" / "phase-c" / "README.md", "w", encoding="utf-8") as f:
        f.write(txt)


NOTES_OWN = {"README.md", "adjacency.csv", "areas.csv", "colonies_check.csv", "conflicts.csv",
             "conflicts_settled_by_rule.csv", "deaths.csv", "hierarchy_check.csv", "keyframe_snaps.csv",
             "conflict_places.csv", "snap_places.csv", "patches_check.csv", "patch-overrides.csv",
             "noop_events.csv", "phase_a_comparison.json", "problems.csv", "run_summary.json",
             "skipped_events.csv", "unclosed_ends.csv", "unresolved_events.csv", "unresolved_names.csv"}


def publish(stage, hist):
    """Copy the staged outputs to the shared folder; drop our stale files there; read back."""
    t = time.time()
    written = []
    for sub, pattern in (("data/anchors-c", "*.json"), ("compiled/_draft", "*.json"), ("notes/phase-c", "*"),
                         ("notes/phase-c/windows", "*.md")):
        src_dir = stage / sub
        dst_dir = hist / sub
        dst_dir.mkdir(parents=True, exist_ok=True)
        names = set()
        for p in sorted(src_dir.glob(pattern)):
            if not p.is_file():
                continue
            names.add(p.name)
            dst = dst_dir / p.name
            tmp = dst_dir / (p.name + ".tmp-compile")
            shutil.copyfile(p, tmp)
            os.replace(tmp, dst)
            written.append((p, dst))
        for p in [stage / sub / "README.md"]:
            if p.exists() and p.name not in names:
                dst = dst_dir / p.name
                tmp = dst_dir / (p.name + ".tmp-compile")
                shutil.copyfile(p, tmp)
                os.replace(tmp, dst)
                written.append((p, dst))
                names.add(p.name)
        for q in dst_dir.glob(pattern):
            # stale outputs of this script only: other agents write notes into notes/phase-c too
            ours = q.name in NOTES_OWN if sub == "notes/phase-c" else q.suffix == pattern[1:]
            if q.is_file() and q.name not in names and (ours or q.name.endswith(".tmp-compile")):
                q.unlink()
    # data/colonies.csv: only when this run derived it
    colp = stage / "data" / "colonies.csv"
    if colp.exists():
        dst = hist / "data" / "colonies.csv"
        tmp = hist / "data" / "colonies.csv.tmp-compile"
        shutil.copyfile(colp, tmp)
        os.replace(tmp, dst)
        written.append((colp, dst))
    # compiled/README.md: replace only the generated section, keep anything others wrote
    sect = (stage / "compiled" / "README.section.md").read_text(encoding="utf-8")
    readme = hist / "compiled" / "README.md"
    old = readme.read_text(encoding="utf-8") if readme.exists() else ""
    if README_BEGIN in old and README_END in old:
        a = old.index(README_BEGIN)
        b = old.index(README_END) + len(README_END)
        new = old[:a] + sect.strip() + old[b:]
    else:
        head = old if old else ("# compiled/: the year-by-year cell ownership, one file per window\n\n"
                                "Phase D writes `compiled/<window>.json` (briefs/window-brief.md section 2); "
                                "`compiled/_draft/` holds the Phase C drafts they start from.\n\n")
        new = head.rstrip() + "\n\n" + sect.strip() + "\n"
    tmp = readme.with_name("README.md.tmp-compile")
    tmp.write_text(new, encoding="utf-8")
    os.replace(tmp, readme)
    log("published %d files in %.0f s; reading back in 10 s" % (len(written) + 1, time.time() - t))
    time.sleep(10)

    def differs(src, dst):
        if not dst.exists() or dst.stat().st_size != src.stat().st_size:
            return True
        return dst.read_bytes() != src.read_bytes()          # every file, byte for byte

    late = [(s, d) for s, d in written if differs(s, d)]
    for _ in range(3):   # the network mount can show a replaced file late: look again before calling it bad
        if not late:
            break
        time.sleep(10)
        late = [(s, d) for s, d in late if differs(s, d)]
    bad = [str(d) for _, d in late]
    back = readme.read_text(encoding="utf-8")
    if sect.strip() not in back:
        bad.append(str(readme))
    if bad:
        log("READ-BACK MISMATCH: %s" % bad[:10])
    else:
        log("read-back ok")
    return bad


if __name__ == "__main__":
    rc = main()
    sys.exit(rc if isinstance(rc, int) else 0)
