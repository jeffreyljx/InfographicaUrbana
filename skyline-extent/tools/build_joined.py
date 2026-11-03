"""Build skyline-extent-joined.geojson: the density-rule extents (build_density.py), with skylines that almost touch
joined into one (Jeffrey, 12 Oct 2026: "for skylines that are ALMOST connected but are severed, just connect them").

Join rule: two outline pieces of the same city join when you can get from one to the other in steps of at most 1.9 km
between 150 m+ towers (any status, pocket or not) and outline edges, no step crossing more than 600 m of water. 1.9 km
is set by Jeffrey's Shenzhen Bay-Xiangmihu example: its longest step is 1.8 km (Jindi Century at OCT to the Antosan
Headquarters towers); his Qianhai-Nanshan example needs 1.24 km. 600 m lets a river like the Pearl River between Tianhe
and Pazhou (360 m) or the Huangpu at Lujiazui join, but not Victoria Harbour, the Han or the Yangtze. The steps used are the shortest-longest-step links (a minimum spanning tree),
and each step becomes a bridge: the hull of the outline (or of 300 m around a tower) within 300 m of the step's two
ends, cut back from water unless the step itself crosses a river, with its corners rounded by 300 m. Stray towers along
the way are taken in with 300 m around them, so they count as inside. Cities with no join (91 of 128) come out exactly
as in skyline-extent.geojson; joined outlines are snapped to the file's 5 decimals with set_precision so they stay valid.

Run from this folder: python3 build_joined.py [out.geojson]. Uses build_density.py, unchanged, for everything else.
"""
import sys, os, json, collections, warnings
warnings.filterwarnings("ignore")
import numpy as np
from shapely.geometry import Point, LineString, mapping
from shapely.ops import unary_union, nearest_points
from shapely import prepared, set_precision
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_density as B

STEP, WATER, H, ROUND = 1900, 600, 300, 300   # longest step, widest water a step may cross, bridge half-width, corner rounding (m)

def join_forest(ps, towers, W):
    """Edges (u, v) of the minimum spanning forest over outline pieces and stray towers with steps <= STEP crossing
    <= WATER of water, pruned to the links that lie on a path between two pieces."""
    geoms = ps + towers; n = len(geoms); np_ = len(ps)
    Wp = prepared.prep(W) if W is not None else None
    rows, cols, vals, seg = [], [], [], {}
    for i in range(n):
        for j in range(i + 1, n):
            if i >= np_ and j >= np_ and abs(geoms[i].x - geoms[j].x) > STEP: continue
            d = geoms[i].distance(geoms[j])
            if d > STEP: continue
            a, b = nearest_points(geoms[i], geoms[j])
            wl = 0.0
            if d > 0 and Wp is not None:
                s = LineString([a, b])
                if Wp.intersects(s): wl = s.intersection(W).length
            if wl > WATER: continue
            rows.append(i); cols.append(j); vals.append(max(d, 0.01)); seg[(i, j)] = (a, b, wl)
    if not vals: return [], seg
    T = minimum_spanning_tree(coo_matrix((vals, (rows, cols)), shape=(n, n))).tocoo()
    adj = collections.defaultdict(set)
    for i, j in zip(T.row, T.col): adj[i].add(j); adj[j].add(i)
    # prune stray-tower leaves until every leaf is an outline piece
    leaves = [k for k in list(adj) if k >= np_ and len(adj[k]) == 1]
    while leaves:
        k = leaves.pop()
        for m in adj.pop(k, ()):
            adj[m].discard(k)
            if m >= np_ and len(adj[m]) == 1: leaves.append(m)
    for k in [k for k in adj if k >= np_ and not adj[k]]: adj.pop(k)
    edges = sorted({(min(i, j), max(i, j)) for i in adj for j in adj[i]})
    return edges, seg

def join(city, core):
    """core: the city's MultiPolygon from build_density (lon/lat). Returns (joined core, km2, list of joined groups)."""
    t = B.D[B.D.city == city]; members = t[t.pocket.isin(KEEP)]
    pr = B.Proj(members.lat.mean())
    U = pr.fwd(core); ps = B.parts(U)
    W = B.water_for(city, G, NEW, pr)
    pts = [pr.fwd(Point(x, y)) for x, y in zip(t.lon, t.lat)]
    stray = [q for q in pts if not any(p.distance(q) < 1 for p in ps)]
    edges, seg = join_forest(ps, stray, W)
    if not edges: return core, None, []
    geoms = ps + stray; np_ = len(ps)
    Wb = W.buffer(5) if W is not None else None
    bands, wet = [], []
    for i, j in edges:
        a, b, wl = seg[(i, j)]
        def end(k, p):
            return geoms[k].intersection(p.buffer(H, 16)) if k < np_ else geoms[k].buffer(B.R, 16)
        band = unary_union([end(i, a), end(j, b)]).convex_hull
        if Wb is not None and wl == 0:                           # a land step: cut water, keep the piece on the step
            on = LineString([a, b]) if a.distance(b) > 0 else a.buffer(1)
            band = unary_union([q for q in B.parts(band.difference(Wb)) if q.distance(on) < 1])
        bands.append(band)
        if wl > 0: wet.append(band)
    for k in {k for e in edges for k in e if k >= np_}:          # stray towers on the way, 300 m around them
        g = geoms[k].buffer(B.R, 16)
        if Wb is not None: g = unary_union([q for q in B.parts(g.difference(Wb)) if q.distance(geoms[k]) < 1])
        bands.append(g)
    Bd = unary_union(bands)
    J = unary_union([U, Bd])
    Jc = J.buffer(ROUND, 16).buffer(-ROUND, 16)                     # round the corners where bridges meet the outline
    add = Jc.difference(J).intersection(Bd.buffer(2 * ROUND, 8))
    if Wb is not None: add = add.difference(Wb.difference(unary_union(wet)) if wet else Wb)   # no rounding into water
    J = unary_union([J, add])
    keep = [p for p in B.parts(J) if p.area >= 40000 and any(prepared.prep(p).contains(q) for q in pts)]
    J = unary_union(keep).simplify(12)
    # which original pieces now share a piece
    groups = []
    for p in B.parts(J):
        inside = [k for k, q in enumerate(ps) if p.intersects(q.representative_point())]
        if len(inside) > 1: groups.append(inside)
    return pr.inv(J), J.area / 1e6, groups

JOIN_NOTES = {   # replaces build_density's note where the joins change what it says
    'Shenzhen': "Shekou, Bao'an, Xili and Longhua qualify on density too. Nanshan and Futian join through Jindi Century "
                "at Overseas Chinese Town and the Antosan Headquarters towers on the way to Xiangmihu.",
}

def skylines(city, core, members):
    """How many skylines the outline holds, counted as the Skylines page does: pieces sharing a pocket are one."""
    pr = B.Proj(members.lat.mean())
    sets = []
    for p in B.parts(pr.fwd(core)):
        pp = prepared.prep(p)
        ks = set(members.pocket[[pp.contains(pr.fwd(Point(x, y))) for x, y in zip(members.lon, members.lat)]])
        if not ks: continue
        for s_ in [s_ for s_ in sets if s_ & ks]: sets.remove(s_); ks |= s_
        sets.append(ks)
    return len(sets)

def joined_note(city, core, core0, members, n_pockets):
    """A sentence for the popup saying how the joins changed the city's skylines."""
    pr = B.Proj(members.lat.mean())
    n0, n1 = skylines(city, core0, members), skylines(city, core, members)
    txt = ''
    if n1 < n0:
        txt = (f"Skylines that almost touch are joined (towers up to 1.9 km apart, rivers up to 600 m wide), so the "
               f"{B.word(n_pockets)} pockets here make {B.word(n1)} skyline{'s' if n1 > 1 else ''}.")
    # a pocket whose pieces water cut apart is now one piece
    before = len(B.parts(pr.fwd(core0))) - n0 + n1
    if len(B.parts(pr.fwd(core))) < before:
        txt += (' ' if txt else '') + 'Pieces of one pocket that water cut apart are joined across it' + (' too.' if txt else '.')
    return txt

def main(out_path):
    global G, NEW, KEEP
    from lib.geo import load
    G = load(); NEW = json.load(open(os.path.join(HERE, 'water_new.json')))
    lab, KEEP = B.pockets(); B.D['pocket'] = lab
    inpk = B.D[B.D.pocket.isin(KEEP)]
    cities = inpk.city.value_counts()
    order = B.D.groupby('city').size().loc[cities.index].sort_values(ascending=False, kind='stable').index
    feats = []
    for city in order:
        t = B.D[B.D.city == city]
        members = inpk[inpk.city == city]
        core0, km2 = B.outline(city, members, G, NEW)
        core, km2j, groups = join(city, core0)
        if km2j is not None: km2 = km2j
        op = prepared.prep(core)
        inside = t[[op.contains(Point(x, y)) for x, y in zip(t.lon, t.lat)]]
        pk = sorted(members.groupby('pocket'), key=lambda kv: -len(kv[1]))
        named = [(B.name_pocket(city, g), len(g)) for _, g in pk]
        areas = [n for n, _ in named]
        if len(named) == 1:
            txt = f"One pocket here is dense enough to count: {B.plain(named[0][0])} ({named[0][1]} towers)."
        else:
            txt = f"{B.word(len(named)).capitalize()} pockets here are dense enough to count: " + '; '.join(
                f"{B.plain(n)} ({k}{' towers' if i == 0 else ''})" for i, (n, k) in enumerate(named)) + "."
        if km2j is not None:
            note = joined_note(city, core, core0, members, len(named))
            if note: txt += ' ' + note
        rest = len(t) - len(inside)
        if rest == 1: txt += f" One of the city's {len(t)} towers stands apart from {'it' if len(named) == 1 else 'them'}."
        elif rest: txt += f" The other {rest} of the city's {len(t)} towers stand in groups too small or too spread out to count."
        note = JOIN_NOTES.get(city, B.NOTES.get(city))
        if note: txt += ' ' + note
        props = {'city': city, 'areas': areas, 'rationale': txt,
                 'towers_in_core': int(len(inside)), 'completed_in_core': int((inside.status == 'Completed').sum()),
                 'towers_in_city': int(len(t)), 'share': round(len(inside) / len(t), 3), 'area_km2': round(km2, 2)}
        comp = inside[inside.status == 'Completed']
        props['tallest_in_core'] = None
        if len(comp):
            top = comp.sort_values('height_m', ascending=False).iloc[0]
            props['tallest_in_core'] = f"{top['name']} ({top.height_m:.0f} m)"
        if km2j is not None: core = set_precision(core, 1e-5)   # snap to the file's 5 decimals without self-intersections
        g = mapping(core)
        geom = {'type': 'MultiPolygon', 'coordinates': B.rnd(g['coordinates']) if g['type'] == 'MultiPolygon' else [B.rnd(g['coordinates'])]}
        feats.append({'type': 'Feature', 'properties': props, 'geometry': geom})
        if km2j is not None: print(f"{city:20s} {props['towers_in_core']:4d}/{props['towers_in_city']:4d} {km2:6.2f} km2  joined {groups}")
    json.dump({'type': 'FeatureCollection', 'features': feats}, open(out_path, 'w'), ensure_ascii=False, separators=(',', ':'))
    print(len(feats), 'cities written to', out_path)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skyline-extent-joined.geojson')
