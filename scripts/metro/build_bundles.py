# Shared track for the /metro map: where two or more lines run on the same track (New York's A, C and E down Eighth
# Avenue, Shanghai's lines 3 and 4, London's Metropolitan, Circle and Hammersmith & City), or on tracks right beside
# each other, the map draws one bundle instead of each line's own track on top of the others.
#
#   python3 scripts/metro/build_bundles.py public/metro/metro.json      (adds the "bundles" key in place)
#
# build_metro.py calls add_bundles() itself, so a rebuild of metro.json always carries them. Needs numpy and shapely.
#
# Method, city by city (systems in one city can share track: Tokyo Metro and Toei): each line's track, cut into points
# every STEP metres, is laid onto the corridors found so far. A run of points that stays within NEAR metres of one
# corridor, heading the same way, for at least MIN_RUN metres, rides that corridor; the rest of the line becomes new
# corridor. Where a line leaves or joins a corridor its own track is eased onto the corridor over BLEND metres, so a
# branch converges smoothly instead of jumping across. Each corridor is then cut wherever the set of lines on it, or
# the year one of them opened there, changes, and the pieces are drawn in directions that run on from one to the next,
# so each line's stripe stays on the same side of a bundle.
#
# Output, metro.json "bundles": [[polyline (1e-5), [line, year, line, year, ...]], ...]: one entry per piece of
# corridor, with every line on it and the year that line's stretch there opened. The lines are in stripe order: lines
# of one colour together (they are drawn as one stripe), colours in a fixed order for the city, so a bundle keeps its
# stripes in the same order from piece to piece.
import json, math, sys, collections, heapq
import numpy as np
import shapely
from shapely import STRtree

STEP = 12.0       # metres between points along each track
NEAR = 40.0       # metres: a track this close to a corridor, heading the same way, rides it
ANGLE = 30.0      # degrees: the most a track may turn from the corridor's heading and still ride it
HOLD = 55.0       # metres: a track already riding a corridor stays on it while this close (tracks spread apart around
HOLD_ANGLE = 40.0 #   stations and junctions, and a bundle should not flicker apart there)
ABSORB = 150.0    # metres: a shorter stretch of a line's own track between two runs on corridors rides the corridor
MIN_RUN = 160.0   # metres: a shorter run near a corridor is a crossing, not shared track
FILL = 70.0       # metres: a shorter gap between two runs on one corridor is part of the shared stretch
BLEND = 160.0     # metres over which a line leaving or joining a corridor is eased onto it
SIMPLIFY = 3.0    # metres
MAX_MEMBERS = 8   # lines in one bundle that the map can draw (the most anywhere is well below this)
MIN_PIECE = 6     # points (about 70 m): a shorter piece whose lines differ from both its neighbours takes theirs
STUB = 60.0       # metres: a shorter piece lying along other pieces with the same lines is dropped
STUB_NEAR = 10.0  #   (within this many metres of them)
JOIN = 3.0        # metres: piece ends this close meet


def decode(s):
    i = lat = lng = 0
    out = []
    while i < len(s):
        vals = []
        for _ in range(2):
            r = sh = 0
            while True:
                b = ord(s[i]) - 63; i += 1
                r |= (b & 31) << sh; sh += 5
                if b < 32:
                    break
            vals.append(~(r >> 1) if r & 1 else r >> 1)
        lat += vals[0]; lng += vals[1]
        out.append((lng / 1e5, lat / 1e5))
    return out


def enc(coords):
    out = []; plat = plng = 0
    for lng, lat in coords:
        la, ln = int(round(lat * 1e5)), int(round(lng * 1e5))
        for v in (la - plat, ln - plng):
            v = ~(v << 1) if v < 0 else (v << 1)
            while v >= 0x20:
                out.append(chr((0x20 | (v & 0x1f)) + 63)); v >>= 5
            out.append(chr(v + 63))
        plat, plng = la, ln
    return ''.join(out)


def densify(P, seg_years):
    """Points every STEP metres along polyline P (n, 2), each with the year of the stretch it lies on."""
    pts, yrs = [P[0]], [seg_years[0]]
    for j in range(len(P) - 1):
        a, b = P[j], P[j + 1]
        d = float(np.hypot(*(b - a)))
        k = max(1, int(math.ceil(d / STEP)))
        for t in range(1, k + 1):
            pts.append(a + (b - a) * (t / k))
            yrs.append(seg_years[j])
    return np.array(pts), np.array(yrs)


def tangents(P):
    if len(P) < 2:
        return np.tile([1.0, 0.0], (len(P), 1))
    T = np.empty_like(P)
    T[1:-1] = P[2:] - P[:-2]
    T[0] = P[1] - P[0]
    T[-1] = P[-1] - P[-2]
    n = np.hypot(T[:, 0], T[:, 1])
    n[n == 0] = 1
    return T / n[:, None]


def hermite(p0, t0, p1, t1):
    """Points every STEP metres on the cubic from p0, heading t0, to p1, heading t1 (unit vectors): a curve with no
    kink at either end."""
    c = float(np.hypot(*(p1 - p0)))
    k = max(2, int(math.ceil(c / STEP)))
    u = np.linspace(0, 1, k + 1)[:, None]
    return ((2 * u ** 3 - 3 * u ** 2 + 1) * p0 + (u ** 3 - 2 * u ** 2 + u) * c * t0
            + (-2 * u ** 3 + 3 * u ** 2) * p1 + (u ** 3 - u ** 2) * c * t1)


def ease(Q, Y, e0, e1):
    """A line's own track Q (with years Y) that comes off a corridor at e0 and/or goes onto one at e1, each (point,
    heading of the line there): the track within BLEND of each junction is shifted, by an amount that fades smoothly to
    nothing, so that it starts at the junction heading along the corridor. The track keeps its own curves, and a branch
    converges onto the corridor instead of turning a corner there."""
    s = np.concatenate([[0.0], np.cumsum(np.hypot(*np.diff(Q, axis=0).T))])
    L = s[-1]
    if e0 is not None and e1 is not None and L <= 4 * STEP:
        H = hermite(e0[0], e0[1], e1[0], e1[1])
        return H, np.full(len(H), Y[len(Y) // 2])
    Q = Q.copy()
    for e, along in ((e0, s), (e1, L - s)):
        if e is None:
            continue
        R = min(BLEND, L if (e0 is None or e1 is None) else L / 2)
        if R <= 0:
            continue
        k = 0 if e is e0 else len(Q) - 1
        j = int(np.argmin(np.abs(along - min(2 * STEP, R))))
        own = (Q[j] - Q[k]) * (1 if e is e0 else -1)
        n = float(np.hypot(*own))
        own = own / n if n else e[1]
        # the shift at the junction, and how fast it changes there, so the shifted track heads along the corridor
        D0 = e[0] - Q[k]
        dD = (e[1] - own) * (1 if e is e0 else -1)
        u = np.clip(along / R, 0, 1)[:, None]
        w0, w1 = 2 * u ** 3 - 3 * u ** 2 + 1, (u ** 3 - 2 * u ** 2 + u) * R
        Q = Q + np.where(u < 1, w0 * D0 + w1 * dD, 0)
    return Q, Y


def runs_of(c, idx):
    """[(start, end exclusive, corridor or -1)]: consecutive points on one corridor, its index moving steadily along it
    (a jump, where a loop passes over itself, starts a new run)."""
    out, s = [], 0
    for k in range(1, len(c) + 1):
        if k == len(c) or c[k] != c[s] or (c[k] >= 0 and abs(int(idx[k]) - int(idx[k - 1])) > 4):
            out.append((s, k, int(c[s])))
            s = k
    return out


class City:
    def __init__(self, kx):
        self.kx = kx
        self.corr = []        # corridors: dict(P=points (m, 2), T=tangents, use=[(line, lo, hi, years array)])
        self.tree = None
        self.owner = None     # per tree point: (corridor, index)

    def rebuild(self):
        if not self.corr:
            return
        P = np.concatenate([c['P'] for c in self.corr])
        self.owner = np.concatenate([np.stack([np.full(len(c['P']), ci), np.arange(len(c['P']))], 1) for ci, c in enumerate(self.corr)])
        self.Tall = np.concatenate([c['T'] for c in self.corr])
        self.Pall = P
        self.tree = STRtree(shapely.points(P))

    def candidates(self, P, T):
        """Corridor points near each point of P: per point, {corridor: (distance, index, strict)}, strict if within NEAR
        and ANGLE, else within HOLD and HOLD_ANGLE."""
        out = [dict() for _ in range(len(P))]
        if self.tree is None:
            return out
        qi, ti = self.tree.query(shapely.points(P), predicate='dwithin', distance=HOLD)
        if not len(qi):
            return out
        d = np.hypot(*(P[qi] - self.Pall[ti]).T)
        cos = np.abs((T[qi] * self.Tall[ti]).sum(1))
        strict = (d <= NEAR) & (cos >= math.cos(math.radians(ANGLE)))
        ok = strict | (cos >= math.cos(math.radians(HOLD_ANGLE)))
        for q, t, dd, st in zip(qi[ok], ti[ok], d[ok], strict[ok]):
            cc, ci = self.owner[t]
            have = out[q].get(cc)
            if have is None or (st, -dd) > (have[2], -have[0]):
                out[q][cc] = (float(dd), int(ci), bool(st))
        return out

    def match(self, P, T):
        """For each point of P: (corridor, index) of the corridor it rides, else (-1, -1). A point rides the nearest
        corridor it is strictly near; a point next to one riding corridor c keeps riding c while within HOLD of it."""
        n = len(P)
        cand = self.candidates(P, T)
        m = np.full((n, 2), -1)
        for k in range(n):
            st = [(d, cc, ci) for cc, (d, ci, s) in cand[k].items() if s]
            if st:
                d, cc, ci = min(st)
                m[k] = (cc, ci)
        for order in (range(n), range(n - 1, -1, -1)):
            prev = None
            for k in order:
                if m[k, 0] >= 0:
                    prev = (int(m[k, 0]), int(m[k, 1]))
                    continue
                if prev is not None and prev[0] in cand[k] and abs(cand[k][prev[0]][1] - prev[1]) <= 4:
                    m[k] = (prev[0], cand[k][prev[0]][1])
                    prev = (int(m[k, 0]), int(m[k, 1]))
                else:
                    prev = None
        return m, cand

    def nearest_on(self, cc, p, around, span):
        """Index of the point of corridor cc nearest to p, looking within span of index `around`."""
        Pc = self.corr[cc]['P']
        lo, hi = max(0, around - span), min(len(Pc), around + span + 1)
        return lo + int(np.hypot(*(Pc[lo:hi] - p).T).argmin())

    def add_part(self, line, P, yrs):
        T = tangents(P)
        m, cand = self.match(P, T)
        n = len(P)
        c, idx = m[:, 0].copy(), m[:, 1].copy()
        # a short run near a corridor with the line's own track on both sides is a crossing, not shared track (a short
        # piece of track that lies along a corridor from end to end, or runs onto one, is shared)
        for a, b, v in runs_of(c, idx):
            if v >= 0 and (b - a) * STEP < MIN_RUN and 0 < a and b < n and c[a - 1] == -1 and c[b] == -1:
                c[a:b] = -1
        # a short stretch of the line's own track between two runs on the same corridor (its track straying round a
        # station or a crossover) rides that corridor too, and so does a short stretch at either end of the track
        # beside the corridor it ends on; a stretch linking two different corridors is a real link and stays
        rs = runs_of(c, idx)
        for j, (a, b, v) in enumerate(rs):
            if v != -1 or (b - a) * STEP >= ABSORB:
                continue
            nbs = [(rs[j - 1][2], int(idx[a - 1])) if j > 0 else None, (rs[j + 1][2], int(idx[b])) if j + 1 < len(rs) else None]
            nbs = [x for x in nbs if x is not None and x[0] >= 0]
            if not nbs or (len(nbs) == 1 and 0 < a and b < n) or (len(nbs) == 2 and nbs[0][0] != nbs[1][0]):
                continue
            span = 2 * (b - a) + 6
            for k in range(a, b):
                best = None
                for cc, around in nbs:
                    ci = self.nearest_on(cc, P[k], around, span)
                    dd = float(np.hypot(*(self.corr[cc]['P'][ci] - P[k])))
                    if dd > HOLD:
                        continue
                    if best is None or dd < best[0]:
                        best = (dd, cc, ci)
                if best is not None:
                    c[k], idx[k] = best[1], best[2]
        rs = runs_of(c, idx)
        # a short gap between two runs on the same corridor is part of the shared stretch
        for j in range(1, len(rs) - 1):
            a, b, v = rs[j]
            if v == -1 and rs[j - 1][2] >= 0 and rs[j - 1][2] == rs[j + 1][2] and (b - a) * STEP <= FILL:
                i0, i1 = int(idx[a - 1]), int(idx[b])
                if abs(i1 - i0) <= 2 * (b - a) + 4:
                    c[a:b] = rs[j - 1][2]
                    idx[a:b] = np.round(i0 + (i1 - i0) * np.arange(1, b - a + 1) / (b - a + 1))
        rs = runs_of(c, idx)
        m = np.stack([c, idx], 1)

        def junction(k):
            # where point k of the line rides its corridor, and the line's heading along the corridor there
            cc, ci = int(m[k, 0]), int(m[k, 1])
            Tc = self.corr[cc]['T'][ci]
            return self.corr[cc]['P'][ci], Tc if np.dot(T[k], Tc) >= 0 else -Tc

        for j, (a, b, v) in enumerate(rs):
            # a line that passes straight from one corridor onto another: join the two where they don't meet
            if v >= 0 and j > 0 and rs[j - 1][2] >= 0:
                (J1, t1), (J2, t2) = junction(a - 1), junction(a)
                if float(np.hypot(*(J2 - J1))) > 1.5 * STEP:
                    Q = hermite(J1, t1, J2, t2)
                    self.corr.append({'P': Q, 'T': tangents(Q), 'use': [(line, 0, len(Q) - 1, np.full(len(Q), int(yrs[a])))]})
            if v >= 0:
                c = self.corr[v]
                idx = m[a:b, 1].astype(int)
                lo, hi = int(idx.min()), int(idx.max())
                if hi - lo < 1:
                    continue
                # the year of this line at each corridor point: that of its nearest point here
                cy = np.empty(hi - lo + 1, dtype=int)
                order = np.argsort(idx, kind='stable')
                si, sy = idx[order], yrs[a:b][order]
                pos = np.clip(np.searchsorted(si, np.arange(lo, hi + 1)), 0, len(si) - 1)
                pos2 = np.clip(pos - 1, 0, len(si) - 1)
                pick = np.where(np.abs(si[pos] - np.arange(lo, hi + 1)) <= np.abs(si[pos2] - np.arange(lo, hi + 1)), pos, pos2)
                cy[:] = sy[pick]
                c['use'].append((line, lo, hi, cy))
            else:
                # ease onto the corridor at either end where the line comes off or goes onto one
                e0 = junction(a - 1) if j > 0 and rs[j - 1][2] >= 0 else None
                e1 = junction(b) if j + 1 < len(rs) and rs[j + 1][2] >= 0 else None
                Q, Y = ease(P[a:b].copy(), yrs[a:b].copy(), e0, e1)
                if len(Q) < 2:
                    continue
                self.corr.append({'P': Q, 'T': tangents(Q), 'use': [(line, 0, len(Q) - 1, Y.astype(int))]})
        self.rebuild()


def drop_stubs(pieces):
    """Drop a short piece (under STUB metres) that lies, for every line on it, along other pieces carrying that line:
    a link of a few metres where a line passes from one corridor to the next would otherwise poke out of the bundle."""
    geoms = [shapely.linestrings(Q) for Q, _ in pieces]
    lines_of = [{l for l, _ in key} for _, key in pieces]
    tree = STRtree(geoms)
    drop = set()
    for i, g in enumerate(geoms):
        L = float(shapely.length(g))
        if L >= STUB:
            continue
        D = shapely.line_interpolate_point(g, np.linspace(0, L, max(2, int(L // 5) + 1)))
        qi, ti = tree.query(D, predicate='dwithin', distance=STUB_NEAR)
        keep = (ti != i) & np.array([t not in drop for t in ti], dtype=bool)
        if all(len(set(qi[keep & np.array([l in lines_of[t] for t in ti], dtype=bool)])) == len(D) for l in lines_of[i]):
            drop.add(i)
    return [p for i, p in enumerate(pieces) if i not in drop]


def orient(pieces, colour):
    """Which pieces to draw reversed, so a bundle keeps each line's stripe on the same side from one piece to the next.
    Pieces that meet end to end and share lines are drawn end to start; each network of them takes the direction of its
    longest piece along that piece's main axis, and joins sharing the most colours are settled first."""
    n = len(pieces)
    lines_of = [{l for l, _ in key} for _, key in pieces]
    E = np.array([Q[e] for Q, _ in pieces for e in (0, -1)])
    tree = STRtree(shapely.points(E))
    a_, b_ = tree.query(shapely.points(E), predicate='dwithin', distance=JOIN)
    edges = collections.defaultdict(list)
    for a, b in zip(a_, b_):
        i, j = a // 2, b // 2
        if i == j:
            continue
        common = lines_of[i] & lines_of[j]
        if common:
            edges[i].append((len({colour[l] or f'#{l}' for l in common}), a % 2, j, b % 2))
    length = [float(np.hypot(*np.diff(Q, axis=0).T).sum()) for Q, _ in pieces]
    flip = [None] * n
    for seed in sorted(range(n), key=lambda i: -length[i]):
        if flip[seed] is not None:
            continue
        d = pieces[seed][0][-1] - pieces[seed][0][0]
        flip[seed] = bool((d[0] < 0) if abs(d[0]) >= abs(d[1]) else (d[1] < 0))
        heap = [(-w, -length[j], seed, ei, j, ej) for w, ei, j, ej in edges[seed]]
        heapq.heapify(heap)
        while heap:
            _, _, i, ei, j, ej = heapq.heappop(heap)
            if flip[j] is not None:
                continue
            # the drawn end of piece i at the join, and the drawn end piece j must have there (the other one)
            want = 1 - (ei ^ flip[i])
            flip[j] = bool(ej != want)
            for w, ej2, k, ek in edges[j]:
                if flip[k] is None:
                    heapq.heappush(heap, (-w, -length[k], j, ej2, k, ek))
    return flip


def add_bundles(data):
    lines = data['lines']
    systems = data['systems']
    colour = [str(l[5] or '').strip().lower() for l in lines]
    by_city = collections.defaultdict(list)
    for g in data['geom']:
        by_city[systems[lines[g[0]][1]][2]].append(g)
    bundles = []
    stats = collections.Counter()
    for city, parts in by_city.items():
        dec = []
        for line, poly, runs in parts:
            cs = decode(poly)
            if len(cs) < 2:
                continue
            seg_years = []
            for k in range(0, len(runs), 2):
                seg_years += [runs[k]] * runs[k + 1]
            dec.append((line, cs, seg_years))
        if not dec:
            continue
        lat0 = float(np.mean([y for _, cs, _ in dec for _, y in cs]))
        kx = math.cos(math.radians(lat0)) * 111320.0
        ky = 110574.0
        C = City(kx)
        # longest first within each line's turn, lines in their packed order (by system, then opening date)
        dec.sort(key=lambda t: (t[0], -len(t[1])))
        for line, cs, seg_years in dec:
            P = np.array([(x * kx, y * ky) for x, y in cs])
            if len(seg_years) < len(P) - 1:
                seg_years = seg_years + [seg_years[-1] if seg_years else 9999] * (len(P) - 1 - len(seg_years))
            Pd, Yd = densify(P, seg_years)
            C.add_part(line, Pd, Yd)
        # a fixed stripe order for the city: colours by the first line that has them, lines by index
        crank = {}
        for line in sorted({u[0] for c in C.corr for u in c['use']}):
            crank.setdefault(colour[line] or f'#{line}', len(crank))
        city_pieces = []
        for c in C.corr:
            P = c['P']
            # a line that rides to within a couple of points of a corridor's end rides to its end (the next corridor
            # starts there)
            last = len(P) - 1
            c['use'] = [(line, 0 if lo <= 2 else lo, last if hi >= last - 2 else hi,
                         np.concatenate([[ys[0]] * (lo if lo <= 2 else 0), ys, [ys[-1]] * ((last - hi) if hi >= last - 2 else 0)]).astype(int))
                        for line, lo, hi, ys in c['use']]
            cuts = {0, last}
            for line, lo, hi, ys in c['use']:
                cuts |= {lo, hi}
                ch = np.nonzero(np.diff(ys))[0]
                cuts |= {lo + int(k) + 1 for k in ch}
            cuts = sorted(cuts)
            pieces = []
            for a, b in zip(cuts, cuts[1:]):
                if b <= a:
                    continue
                mid = (a + b) / 2
                mem = {}
                for line, lo, hi, ys in c['use']:
                    if lo <= a and hi >= b:
                        y = int(ys[min(len(ys) - 1, max(0, int(round(mid)) - lo))])
                        mem[line] = min(y, mem.get(line, y))
                if not mem:
                    continue
                key = tuple(sorted(mem.items()))
                if pieces and pieces[-1][2] == key and pieces[-1][1] == a:
                    pieces[-1][1] = b
                else:
                    pieces.append([a, b, key])
            # a short piece whose lines differ from both neighbours (a line's track straying for a few metres) takes
            # the lines of the neighbour that has all of its own
            for k in range(len(pieces)):
                a, b, key = pieces[k]
                nbs = [pieces[x] for x in (k - 1, k + 1) if 0 <= x < len(pieces) and pieces[x][1 if x < k else 0] == (a if x < k else b)]
                if b - a >= MIN_PIECE or not nbs or any(nb[2] == key for nb in nbs):
                    continue
                mine = {l for l, _ in key}
                fit = [nb[2] for nb in nbs if mine <= {l for l, _ in nb[2]}]
                if fit:
                    pieces[k][2] = max(fit, key=len)
            merged = []
            for a, b, key in pieces:
                if merged and merged[-1][2] == key and merged[-1][1] == a:
                    merged[-1][1] = b
                else:
                    merged.append([a, b, key])
            city_pieces += [(P[a:b + 1], key) for a, b, key in merged]
        city_pieces = drop_stubs(city_pieces)
        flips = orient(city_pieces, colour)
        for (Q, key), flip in zip(city_pieces, flips):
            g = shapely.simplify(shapely.linestrings(Q), SIMPLIFY)
            cs = [(x / kx, y / ky) for x, y in shapely.get_coordinates(g)]
            if flip:
                cs = cs[::-1]
            mem = sorted(key, key=lambda ly: (crank[colour[ly[0]] or f'#{ly[0]}'], ly[0]))
            if len(mem) > MAX_MEMBERS:
                stats['bundles_over_max'] += 1
                mem = sorted(sorted(mem, key=lambda ly: (ly[1], ly[0]))[:MAX_MEMBERS],
                             key=lambda ly: (crank[colour[ly[0]] or f'#{ly[0]}'], ly[0]))
            stats['pieces'] += 1
            stats[f'members_{min(len(mem), 5)}'] += 1
            stats['shared_m'] += (len(mem) > 1) * (len(Q) - 1) * STEP
            bundles.append([enc(cs), [v for ly in mem for v in ly]])
    data['bundles'] = bundles
    return stats


if __name__ == '__main__':
    path = sys.argv[1]
    data = json.load(open(path, encoding='utf8'))
    stats = add_bundles(data)
    txt = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    open(path, 'w', encoding='utf8').write(txt)
    print(dict(stats), len(txt.encode()), 'bytes', file=sys.stderr)
