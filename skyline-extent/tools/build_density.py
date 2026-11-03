"""Rebuild skyline-extent.geojson with the density rule (11 Oct 2026).

Rule: every tower of 150 m+ in the master list counts, whatever its status. A tower is in a dense spot when at
least 4 towers (itself included) stand within 800 m of it; towers within 800 m of such a tower join its group
(DBSCAN, eps 800 m, min_samples 4, on great-circle distance). A group of 5 or more towers is a pocket, and every
pocket gets a skyline extent, in any city. The outline runs 300 m out from the pocket's towers, closes gaps of up to
about 1.9 km between them (closing radius 650 m), takes in land strips up to about 600 m wide between the outline
and the river, lake or sea it faces (waterfront fill; piers and other land under about 300 m wide with water on both
sides stay out, and so do spurs under about 300 m wide that would reach out toward a pond or a dock), is cut back
from the water, and is smoothed.

Run from this folder: python3 build_density.py [out.geojson]. Needs pandas, shapely, scikit-learn.
Water comes from geo_all.json (the first 38 cities) and water_new.json (every other city with a pocket, plus the
Hong Kong and Shenzhen pockets outside their geo_all areas, clipped to 650 m around each pocket). A city that newly
qualifies needs its water fetched first (see README).
"""
import sys, json, math, os, warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import numpy as np, pandas as pd
from sklearn.cluster import DBSCAN
from shapely.geometry import Point, Polygon, mapping
from shapely.ops import unary_union, transform
from shapely import prepared, from_wkt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.geo import load
from names import NAMES, NOTES

CSV = '/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv'
EPS, MIN_SAMPLES, MIN_TOWERS = 800, 4, 5           # density rule
R, C, SMOOTH = 300, 650, 70                        # outline: tower radius, gap closing, smoothing (m)
SHORE, SHORE_NEAR, PIER, NECK = 300, 600, 150, 150  # waterfront fill: closing with nearby water, pier and spur half-widths (m)
E = 6371000.0

D = pd.read_csv(CSV)

class Proj:
    def __init__(s, lat0): s.k = math.cos(math.radians(lat0)) * 111320.0; s.ky = 110574.0
    def fwd(s, g): return transform(lambda x, y, z=None: (np.asarray(x) * s.k, np.asarray(y) * s.ky), g)
    def inv(s, g): return transform(lambda x, y, z=None: (np.asarray(x) / s.k, np.asarray(y) / s.ky), g)

def parts(g):
    if g is None or g.is_empty: return []
    return [p for p in (g.geoms if hasattr(g, 'geoms') else [g]) if p.geom_type == 'Polygon']

def pockets():
    lab = DBSCAN(eps=EPS / E, min_samples=MIN_SAMPLES, metric='haversine').fit(np.radians(D[['lat', 'lon']].values)).labels_
    s = pd.Series(lab); sz = s[s >= 0].value_counts()
    keep = set(sz[sz >= MIN_TOWERS].index)
    return lab, keep

def water_for(city, G, NEW, pr):
    """Water near the city's pockets in the local metric projection, without thin channels and ponds.
    geo_all.json holds raw water for the first 38 cities; water_new.json holds already filtered water
    for every other pocket (and for the Hong Kong and Shenzhen pockets outside their geo_all bboxes)."""
    ws = []
    if city in G and not G[city]['water'].is_empty:
        W = pr.fwd(G[city]['water']).buffer(-35, 8).buffer(35, 8)
        ws += [p for p in parts(W) if p.area > 60000]
    if city in NEW:
        ws += parts(pr.fwd(from_wkt(NEW[city])))
    return unary_union(ws) if ws else None

def outline(city, members, G, NEW):
    pr = Proj(members.lat.mean())
    pts = [pr.fwd(Point(x, y)) for x, y in zip(members.lon, members.lat)]
    U = unary_union([q.buffer(R, 16) for q in pts]).buffer(C, 16).buffer(-C, 16)
    U = unary_union([Polygon(p.exterior) for p in parts(U)])
    W = water_for(city, G, NEW, pr)
    if W is not None and not W.is_empty:
        # waterfront fill: land strips up to ~600 m wide between the outline and the river, lake or sea it faces
        # are taken in, since a skyline runs down to its waterfront. Piers and other land under ~300 m wide with
        # water on both sides count as water here, so they stay out.
        Wc = W.buffer(PIER, 8).buffer(-PIER, 8)
        near = Wc.intersection(U.buffer(SHORE_NEAR, 8))
        F = unary_union([U, near]).buffer(SHORE, 16).buffer(-SHORE, 16).difference(Wc)
        add = F.difference(U)
        Ub = U.buffer(5).boundary
        touches = lambda p: p.buffer(6).intersection(Ub).length >= 200            # meets the outline along 200 m+
        # land wider than ~300 m that reaches the outline only through a narrow neck juts out into the water
        # (a landfill or an island, like Chicago's water plant north of Navy Pier) and stays out
        jut = [p for p in parts(add.buffer(-PIER, 8).buffer(PIER, 8)) if not touches(p)]
        if jut: add = add.difference(unary_union(jut).buffer(1))
        add = unary_union([p for p in parts(add.buffer(-20, 8).buffer(20, 8)) if touches(p)])
        # fill that sticks out of the outline as a spur under ~300 m wide (reaching for a pond, a river bend or
        # the tip of a dock) stays out; strips that run along the outline are kept whatever their width
        UA = unary_union([Polygon(p.exterior) for p in parts(unary_union([U, add]))])
        add = add.intersection(UA.buffer(-NECK, 8).buffer(NECK, 8))
        U = unary_union([U] + [p for p in parts(add.buffer(-20, 8).buffer(20, 8)) if touches(p)])
        U = unary_union([Polygon(p.exterior) for p in parts(U)])
        U = U.difference(W.buffer(5))
    U = U.buffer(SMOOTH, 8).buffer(-2 * SMOOTH, 8).buffer(SMOOTH, 8)
    if W is not None: U = U.difference(W.buffer(5))
    t = D[D.city == city]
    allpts = [pr.fwd(Point(x, y)) for x, y in zip(t.lon, t.lat)]
    keep = [p for p in parts(U) if p.area >= 40000 and any(prepared.prep(p).contains(q) for q in allpts)]
    U = unary_union(keep).simplify(12)
    return pr.inv(U), U.area / 1e6

def name_pocket(city, g):
    lat, lon = g.lat.mean(), g.lon.mean()
    best = None
    for la, lo, nm in NAMES.get(city, []):
        dkm = math.hypot((la - lat) * 111.0, (lo - lon) * 111.0 * math.cos(math.radians(lat)))
        if dkm < 3 and (best is None or dkm < best[0]): best = (dkm, nm)
    return best[1] if best else str(g.district.value_counts().index[0])

WORDS = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
def word(n): return WORDS[n] if n < len(WORDS) else str(n)

def plain(name):
    """'Dogok (Tower Palace)' -> 'Dogok, Tower Palace', so the tower count can follow in parentheses."""
    return name.replace(' (', ', ').replace(')', '')

def rnd(o):
    if isinstance(o, (list, tuple)): return [rnd(x) for x in o]
    if isinstance(o, float): return round(o, 5)
    return o

def main(out_path):
    G = load()
    NEW = json.load(open(os.path.join(HERE, 'water_new.json')))
    lab, keep = pockets()
    D['pocket'] = lab
    inpk = D[D.pocket.isin(keep)]
    cities = inpk.city.value_counts()
    order = D.groupby('city').size().loc[cities.index].sort_values(ascending=False, kind='stable').index
    feats = []
    for city in order:
        t = D[D.city == city]
        members = inpk[inpk.city == city]
        core, km2 = outline(city, members, G, NEW)
        op = prepared.prep(core)
        inside = t[[op.contains(Point(x, y)) for x, y in zip(t.lon, t.lat)]]
        pk = sorted(members.groupby('pocket'), key=lambda kv: -len(kv[1]))
        named = [(name_pocket(city, g), len(g)) for _, g in pk]
        areas = [n for n, _ in named]
        if len(named) == 1:
            txt = f"One pocket here is dense enough to count: {plain(named[0][0])} ({named[0][1]} towers)."
        else:
            txt = f"{word(len(named)).capitalize()} pockets here are dense enough to count: " + '; '.join(
                f"{plain(n)} ({k}{' towers' if i == 0 else ''})" for i, (n, k) in enumerate(named)) + "."
        rest = len(t) - len(inside)
        if rest == 1: txt += f" One of the city's {len(t)} towers stands apart from {'it' if len(named) == 1 else 'them'}."
        elif rest: txt += f" The other {rest} of the city's {len(t)} towers stand in groups too small or too spread out to count."
        if city in NOTES: txt += ' ' + NOTES[city]
        props = {'city': city, 'areas': areas, 'rationale': txt,
                 'towers_in_core': int(len(inside)), 'completed_in_core': int((inside.status == 'Completed').sum()),
                 'towers_in_city': int(len(t)), 'share': round(len(inside) / len(t), 3), 'area_km2': round(km2, 2)}
        comp = inside[inside.status == 'Completed']
        props['tallest_in_core'] = None                              # no completed tower yet (New Alamein City, Itapema, Fortaleza)
        if len(comp):
            top = comp.sort_values('height_m', ascending=False).iloc[0]
            props['tallest_in_core'] = f"{top['name']} ({top.height_m:.0f} m)"
        g = mapping(core)
        geom = {'type': 'MultiPolygon', 'coordinates': rnd(g['coordinates']) if g['type'] == 'MultiPolygon' else [rnd(g['coordinates'])]}
        feats.append({'type': 'Feature', 'properties': props, 'geometry': geom})
        print(f"{city:20s} {props['towers_in_core']:4d}/{props['towers_in_city']:4d} {km2:6.2f} km2  pockets={len(named)}")
    json.dump({'type': 'FeatureCollection', 'features': feats}, open(out_path, 'w'), ensure_ascii=False, separators=(',', ':'))
    print(len(feats), 'cities written to', out_path)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skyline-extent.geojson')
