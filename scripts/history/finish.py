"""The finishing pass for CartaHistoria: coasts, lakes and gaps.

The border compiler works on the first land grid (cells whose centre is on a coarse coastline) and claims a
cell for a state only when the cell's centre falls inside that state's outline. That leaves three kinds of
hole, which this pass closes for every year, on the full grid (every cell that holds land on the
full-resolution shoreline):

  coasts   a coastal cell the first grid lacks follows the cell that holds the land nearest to it
  lakes    lake cells are shared out among the states on the shore, each cell to the nearest
  gaps     an empty cell in a gap at most two cells wide (sea counts as a wall), or in a small pocket
           walled in by states, goes to the neighbour that holds the most cells around it

and it applies the corrections that research wrote down (data/grid/v2/patches/*.json):

  {"cells": [runs], "from": y, "to": y, "owner": "<slug>" | null, "mode": "set" | "nearest" | "like",
   "like": cell, "over": bool, "replace": "<slug>", "suzerain": "<slug>"}

owner null keeps the cells empty (land no state held); mode "nearest" shares the cells out among the
neighbours; mode "like" gives the cells, year by year, to whoever holds the cell named by "like" (an
island that follows the mainland opposite). A patch only fills empty cells, unless "replace" names the
state whose cells it also takes over, or "over" lets it replace any owner. A patch never reaches outside
its owner's own lifetime.

    fin = Finisher(grid_dir, pid=slug->id, life=slug->(first year, last year))
    owner, status, other = fin.apply(owner0, status0, other0, year)
"""
import json
import os

import numpy as np

LAKE_PASSES = 12       # how far a lake is shared out from its shores, in cells
POCKET_MAX = 12        # a walled-in pocket up to this many cells is filled
POCKET_REACH = 4       # a pocket lies within this many cells of a state
POCKET_WALL = 0.5      # at least this share of a pocket's edge must be other states (the rest being sea)
LIVING = 2020          # a dossier that ends in or after this year describes a state that still exists


def runs_to_idx(runs):
    out = []
    for r in runs or []:
        if isinstance(r, str):
            a, b = r.split("-")
            out.append(np.arange(int(a), int(b) + 1, dtype=np.int64))
        else:
            out.append(np.array([int(r)], np.int64))
    return np.concatenate(out) if out else np.zeros(0, np.int64)


def neighbours(cells, cache=None):
    if cache and os.path.exists(cache):
        nb = np.fromfile(cache, np.int32).reshape(-1, 6)
        if len(nb) == len(cells):
            return nb
    import h3
    idx = {c: i for i, c in enumerate(cells)}
    nb = np.full((len(cells), 6), -1, np.int32)
    for i, c in enumerate(cells):
        k = 0
        for d in h3.grid_ring(c, 1):
            j = idx.get(d)
            if j is not None:
                nb[i, k] = j
            k += 1
    if cache:
        try:
            nb.tofile(cache)
        except OSError:
            pass
    return nb


class Finisher:
    def __init__(self, grid_dir, pid=None, patches=True, cache_dir=None, log=None, life=None):
        g = str(grid_dir)
        self.cells = [l.strip() for l in open(os.path.join(g, "land_r5_v2.txt")) if l.strip()]
        self.N = N = len(self.cells)
        self.parent = np.fromfile(os.path.join(g, "parent.i32"), np.int32)
        self.N0 = int(np.count_nonzero(self.parent == np.arange(N)))
        assert (self.parent[:self.N0] == np.arange(self.N0)).all(), "old cells must come first"
        self.frac = np.fromfile(os.path.join(g, "frac.f32"), np.float32)
        self.lake = np.fromfile(os.path.join(g, "lake.u8"), np.uint8).astype(bool)
        nb = neighbours(self.cells, os.path.join(cache_dir or g, "nbr.i32"))
        self.sea = nb < 0
        self.nb = np.where(nb < 0, 0, nb)
        self.kid = np.flatnonzero(self.parent[self.N0:] >= 0) + self.N0
        self.kid_parent = self.parent[self.kid]
        self.patches = []
        self._by_century = None
        self.patch_years = set()
        self.skipped = []
        self.life = life or {}
        if patches and pid is not None:
            pdir = os.path.join(g, "patches")
            if os.path.isdir(pdir):
                for name in sorted(os.listdir(pdir)):
                    if name.endswith(".json"):
                        self._load(os.path.join(pdir, name), pid)
        if log:
            log(f"finish: {self.N0:,} + {N - self.N0:,} coastal cells, {int(self.lake.sum()):,} lake cells, "
                f"{len(self.patches):,} corrections" + (f" ({len(self.skipped)} skipped)" if self.skipped else ""))

    # ---- corrections
    def _load(self, path, pid):
        try:
            doc = json.load(open(path))
        except (OSError, ValueError) as ex:
            self.skipped.append(f"{os.path.basename(path)}: {ex}")
            return
        for k, p in enumerate(doc.get("patches") or []):
            try:
                cells = runs_to_idx(p["cells"])
                cells = cells[(cells >= 0) & (cells < self.N)]
                y0, y1 = int(p["from"]), int(p["to"])
                mode = p.get("mode", "set")
                owner = p.get("owner")
                if mode == "set" and owner is not None and owner not in pid:
                    raise KeyError(f"unknown state {owner}")
                suz = p.get("suzerain")
                key = 0
                if mode == "set" and owner is not None:
                    key = (pid[owner] << 24) | ((1 << 16) | pid[suz] if suz and suz in pid else 0)
                    lf = self.life.get(owner)
                    if lf:
                        y0 = max(y0, int(lf[0]) if lf[0] is not None else y0)
                        if lf[1] is not None and int(lf[1]) < LIVING:   # a state alive today has no end
                            y1 = min(y1, int(lf[1]))
                only = pid.get(p.get("replace"), 0) if p.get("replace") else 0
                like = -1
                if mode == "like":
                    like = int(p["like"])
                    if not (0 <= like < self.N):
                        raise ValueError("like names no cell")
                if cells.size == 0 or y1 < y0:
                    raise ValueError("no cells or years")
            except (KeyError, TypeError, ValueError) as ex:
                self.skipped.append(f"{os.path.basename(path)}#{k}: {ex}")
                continue
            self.patches.append((y0, y1, cells, mode, key, bool(p.get("over")), only, like))
            self.patch_years.add(y0)
            self.patch_years.add(y1 + 1)

    def _active(self, year):
        """The corrections that can touch this year, in file order (looked up by century)."""
        if self._by_century is None:
            b = {}
            for i, p in enumerate(self.patches):
                for c in range(p[0] // 100, p[1] // 100 + 1):
                    b.setdefault(c, []).append(i)
            self._by_century = {c: [self.patches[i] for i in v] for c, v in b.items()}
        return self._by_century.get(year // 100, ())

    # ---- the pass
    def lift(self, a):
        """An array over the first grid, carried to the full grid: each coastal cell takes its parent's value."""
        out = np.zeros(self.N, a.dtype)
        out[:self.N0] = a
        out[self.kid] = a[self.kid_parent]
        return out

    def _vote(self, key, g):
        """For the empty cells g, the neighbouring owner holding most of the cells around each (0 if none)."""
        K = np.where(self.sea[g], 0, key[self.nb[g]])
        cnt = (K[:, :, None] == K[:, None, :]).sum(2)
        # the largest group wins; ties go to the smaller key, so the result does not depend on neighbour order
        score = cnt.astype(np.int64) * (1 << 48) - K
        score[K == 0] = -1
        return K[np.arange(g.size), score.argmax(1)]

    def _grow(self, key, mask, passes):
        """Share the empty cells of mask out among their neighbours, a ring at a time."""
        for _ in range(passes):
            g = np.flatnonzero(mask & (key == 0))
            if g.size == 0:
                break
            pick = self._vote(key, g)
            ok = pick != 0
            if not ok.any():
                break
            key[g[ok]] = pick[ok]

    def components(self, mask):
        """Connected groups of the cells in mask: (cell indices, label per cell as a position in that list)."""
        idx = np.flatnonzero(mask)
        E = idx.size
        if E == 0:
            return idx, np.zeros(0, np.int64)
        pos = np.full(self.N, -1, np.int64)
        pos[idx] = np.arange(E)
        nbp = pos[self.nb[idx]]
        nbp[self.sea[idx]] = -1
        has = nbp >= 0
        nbc = np.where(has, nbp, 0)
        lab = np.arange(E)
        while True:
            m = np.where(has, lab[nbc], E).min(1)
            new = np.minimum(lab, m)
            new = new[new]
            if np.array_equal(new, lab):
                break
            lab = new
        return idx, lab

    def apply(self, owner0, status0, other0, year, detail=False):
        owner = self.lift(owner0); status = self.lift(status0); other = self.lift(other0)
        key = (owner.astype(np.int64) << 24) | (status.astype(np.int64) << 16) | other.astype(np.int64)
        lifted = key != 0
        locked = np.zeros(self.N, bool)
        nearest = np.zeros(self.N, bool)
        for y0, y1, cells, mode, k, over, only, like in self._active(year):
            if not (y0 <= year <= y1):
                continue
            if mode == "like":
                k = int(key[like])
                if k == 0:
                    continue
            if over:
                c = cells
            elif only:
                k0 = key[cells]
                c = cells[(k0 == 0) | ((k0 >> 24) == only)]
            else:
                c = cells[key[cells] == 0]
            if mode == "nearest":
                key[c] = 0
                nearest[c] = True
            elif k == 0:
                key[c] = 0
                locked[c] = True
            else:
                key[c] = k
        patched = (key != 0) & ~lifted
        free = ~locked
        if nearest.any():
            self._grow(key, nearest & free, 40)
        self._grow(key, self.lake & free, LAKE_PASSES)
        after_lake = key != 0
        # gaps: empty cells in the closing (radius one cell, sea as wall) of the owned land, within two steps of an owner
        solid = key != 0
        nb, sea = self.nb, self.sea
        near1 = solid | (solid[nb] & ~sea).any(1)
        dil = solid | (solid[nb] | sea).any(1)
        closed = dil & (dil[nb] | sea).all(1)
        near2 = near1 | (near1[nb] & ~sea).any(1)
        self._grow(key, ~solid & closed & near2 & free, 2)
        after_gap = key != 0
        # pockets: small groups of empty cells walled in by states
        owned = key != 0
        zone = owned
        for _ in range(POCKET_REACH):
            zone = zone | (zone[nb] & ~sea).any(1)
        empty = (key == 0) & free & zone          # only empty land near a state can be a pocket
        if empty.any():
            idx, lab = self.components(empty)
            size = np.bincount(lab, minlength=idx.size)
            small = size[lab] <= POCKET_MAX
            if small.any():
                ids = idx[small]; l = lab[small]
                wall = ((key[nb[ids]] != 0) & ~sea[ids]).sum(1)
                water = sea[ids].sum(1)
                w = np.bincount(l, weights=wall, minlength=idx.size); s = np.bincount(l, weights=water, minlength=idx.size)
                good = (w[l] > 0) & (w[l] >= POCKET_WALL * (w[l] + s[l]))
                pocket = np.zeros(self.N, bool)
                pocket[ids[good]] = True
                self._grow(key, pocket, POCKET_MAX)
        owner = (key >> 24).astype(owner0.dtype)
        status = ((key >> 16) & 0xFF).astype(status0.dtype)
        other = (key & 0xFFFF).astype(other0.dtype)
        if detail:
            n0 = self.N0
            stats = {"coast": int(lifted[n0:].sum()), "patched": int(patched.sum()),
                     "lake": int((after_lake & ~lifted & ~patched).sum()),
                     "gap": int((after_gap & ~after_lake).sum()), "pocket": int(((key != 0) & ~after_gap).sum()),
                     "empty": int((key == 0).sum())}
            return owner, status, other, stats
        return owner, status, other
