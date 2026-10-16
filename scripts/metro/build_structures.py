# Station structures and exits for the /metro page, from OpenStreetMap.
#
#   python3 scripts/metro/build_structures.py DB METRO_JSON STATION_INDEX OSM_DIR OUT_DIR COVERAGE_CSV
#
# DB is the project's metro database (metro/db), METRO_JSON and STATION_INDEX come from build_metro.py (its optional
# third argument), OSM_DIR holds the planet extracts written by scripts/metro/structures/ (rels_sel.jsonl,
# ways.*.jsonl, nodes.*.jsonl), and OUT_DIR gets one file per system (public/metro/structures/<system>.json).
# Needs numpy and shapely.
#
# For every station on the page, and every line serving it:
#   box    the station's structure for that line, in the line's colour: the rotated rectangle around the line's mapped
#          platforms (railway=platform, public_transport=platform) and the track beside them; where OpenStreetMap
#          has no platform for it, a box of the line's train length laid along its track, marked approximate
#   area   concourses and station halls: station areas of its stop area (public_transport=station,
#          building=train_station) and indoor areas below ground that touch the boxes
#   path   underground passages (footways, steps and corridors in tunnels or below ground) leading to it
#          (areas and paths take the colour of the nearest line's box, as Baidu Maps draws them)
#   exit   its entrances (railway=subway_entrance, railway=train_station_entrance, public_transport=entrance, and the
#          entrance members of its stop area), labelled with the exit's letter or number where OpenStreetMap has one
import csv, glob, json, math, os, re, sys, collections
import numpy as np
from shapely.geometry import LineString, MultiLineString, Point, Polygon, MultiPolygon, box as sbox
from shapely.ops import unary_union, polygonize, nearest_points
from shapely import affinity
from shapely.strtree import STRtree

DB, METRO, INDEX, OSM, OUT, COVER = sys.argv[1:7]
EXIT_KM = 0.35        # an exit belongs to the nearest station within this distance (stop area members always count)
TRAIN_EXIT_KM = 0.15  # railway=train_station_entrance is often a mainline station's: only near ones count
PLATFORM_KM = 0.35    # platforms are looked for this far from a station
TRACK_M = 14          # a platform must lie this close to the line's track ...
ANGLE = 30            # ... and run within this many degrees of it
BOX_W = 24            # approximate box: two tracks and an island platform, with the walls
CAR_M = 21            # approximate box: this much per car, plus 60 m for an underground station's plant rooms
                      # and stairs (20 m for one above ground)
MAX_BOX_M = 340       # a platform box longer than this is a mapping slip: the approximate box is used instead
AREA_MAX_M2 = 120_000 # station areas larger than this are whole rail yards or terminals, not a metro concourse
NEAR_AREA_M2 = 40_000 # a hall not in the station's stop area counts only up to this size
BOX_HALF_W = 20       # a box from platforms reaches at most this far either side of its track
PLATFORM_ALONG_M = 170  # and only platforms within this distance along the track from the station count

def num(x):
    m = re.match(r'\s*(\d+)', x or '')
    return int(m.group(1)) if m else None

# ---------- the page's stations and lines ----------
page = json.load(open(METRO, encoding='utf8'))
index = json.load(open(INDEX, encoding='utf8'))
S = page['systems']; L = page['lines']
lines_csv = {l['line_id']: l for l in csv.DictReader(open(f'{DB}/metro_lines.csv', encoding='utf8'))}
geo = {f['properties']['line_id']: f['geometry'] for f in json.load(open(f'{DB}/metro_lines.geojson', encoding='utf8'))['features']}
st = page['stations']
lon = np.cumsum(st['lon']) / 1e5; lat = np.cumsum(st['lat']) / 1e5
NST = len(st['name'])
st_sys = [L[st['lines'][i][0][0]][1] for i in range(NST)]
assert len(index) == NST

class Local:
    """Equirectangular metres around a point; good to a few cm over a station's few hundred metres."""
    def __init__(self, lo, la):
        self.lo, self.la = lo, la; self.kx = 111320 * math.cos(math.radians(la)); self.ky = 110540
    def xy(self, p): return ((p[0] - self.lo) * self.kx, (p[1] - self.la) * self.ky)
    def ll(self, p): return (self.lo + p[0] / self.kx, self.la + p[1] / self.ky)
    def geom(self, coords): return [self.xy(p) for p in coords]

def km(a, b):
    return math.hypot((a[0] - b[0]) * math.cos(math.radians((a[1] + b[1]) / 2)), a[1] - b[1]) * 111.32

# grid of page stations for nearest lookups
CELL = 0.01
grid = collections.defaultdict(list)
for i in range(NST):
    grid[(int(math.floor(lon[i] / CELL)), int(math.floor(lat[i] / CELL)))].append(i)
def near_stations(p, rkm):
    cx, cy = int(math.floor(p[0] / CELL)), int(math.floor(p[1] / CELL)); r = int(math.ceil(rkm / 0.7)) + 1
    out = []
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            for i in grid.get((cx + dx, cy + dy), ()):
                d = min(km(p, (q[1], q[2])) for q in index[i])
                if d <= rkm: out.append((d, i))
    return sorted(out)

# ---------- OpenStreetMap extracts ----------
# node coordinates (ids, x, y in 1e-7 degrees) and the tagged nodes (entrances, stop area members) with their tags
_a = np.concatenate([np.load(f) for f in sorted(glob.glob(f'{OSM}/nxy.*.npy'))], axis=1)
_o = np.argsort(_a[0], kind='stable')
NID = _a[0][_o]; NX = _a[1][_o] / 1e7; NY = _a[2][_o] / 1e7
del _a, _o
nodes = {}
for f in sorted(glob.glob(f'{OSM}/nodes.*.jsonl')):
    for l in open(f, encoding='utf8'):
        o = json.loads(l); nodes[o['id']] = o
ways = {}
for f in sorted(glob.glob(f'{OSM}/ways.*.jsonl')):
    for l in open(f, encoding='utf8'):
        o = json.loads(l); ways[o['id']] = o
rels = {}
for l in open(f'{OSM}/rels_sel.jsonl', encoding='utf8'):
    o = json.loads(l); rels[o['id']] = o
print(len(NID), 'node locations', len(nodes), 'tagged nodes', len(ways), 'ways', len(rels), 'relations', flush=True)

def way_coords(w):
    ids = np.asarray(w['nodes'], dtype=np.int64)
    if len(ids) < 2: return None
    k = np.minimum(np.searchsorted(NID, ids), len(NID) - 1)
    if not np.all(NID[k] == ids): return None
    return list(zip(NX[k].tolist(), NY[k].tolist()))

def is_closed(w):
    return len(w['nodes']) >= 4 and w['nodes'][0] == w['nodes'][-1] and w['tags'].get('area') != 'no'

def rel_polygon(r):
    """lon/lat polygon of a multipolygon relation from its member ways (outers minus inners)."""
    outer, inner = [], []
    for t, ref, role in r['members']:
        if t != 'w' or ref not in ways: continue
        c = way_coords(ways[ref])
        if not c: continue
        (inner if role == 'inner' else outer).append(LineString(c))
    if not outer: return None
    po = list(polygonize(unary_union(outer)))
    if not po: return None
    g = unary_union(po)
    if inner:
        pi = list(polygonize(unary_union(inner)))
        if pi: g = g.difference(unary_union(pi))
    return g if not g.is_empty else None

def neg(v):
    return bool(v) and bool(re.match(r'^\s*-', v.split(';')[0]))

RAILPLAT = {'train', 'subway', 'light_rail', 'monorail'}
def platform_kind(t):
    # a mainline platform (train=yes, and no metro mode) is not a metro station's, however near its track it lies:
    # St Pancras' platforms sit right over the Piccadilly line
    if t.get('train') == 'yes' and not any(t.get(k) == 'yes' for k in ('subway', 'light_rail', 'monorail')): return False
    if t.get('railway') == 'platform': return True
    if t.get('public_transport') == 'platform':
        if any(t.get(k) == 'yes' for k in RAILPLAT) or t.get('railway'): return True
        return False
    return False

def below_ground(t):
    return neg(t.get('layer')) or neg(t.get('level')) or t.get('location') == 'underground' or t.get('tunnel') in ('yes', 'building_passage')

def station_area_kind(t):
    """a metro station's own hall: underground, or tagged as a subway station (a mainline terminus's train shed is not)"""
    if not (t.get('public_transport') == 'station' or t.get('railway') in ('station', 'halt') or t.get('building') == 'train_station'): return False
    return below_ground(t) or t.get('station') in ('subway', 'light_rail') or t.get('subway') == 'yes'

def passage_kind(t):
    hw = t.get('highway')
    if hw in ('corridor', 'footway', 'steps', 'path', 'pedestrian', 'elevator') or t.get('indoor') == 'corridor':
        return below_ground(t)
    return False

def indoor_area_kind(t):
    return t.get('indoor') in ('area', 'room', 'corridor') and below_ground(t)

# features as lon/lat shapely geometries with their kind and tags
feats = []   # (kind, geom, tags, osm id)
for w in ways.values():
    t = w['tags']
    kinds = []
    if platform_kind(t): kinds.append('platform')
    if station_area_kind(t) and is_closed(w): kinds.append('station')
    if passage_kind(t) and not is_closed(w): kinds.append('passage')
    if indoor_area_kind(t) and is_closed(w): kinds.append('indoor')
    if not kinds: continue
    c = way_coords(w)
    if not c: continue
    for k in kinds:
        g = Polygon(c) if is_closed(w) and k != 'passage' else LineString(c)
        if not g.is_valid: g = g.buffer(0)
        if not g.is_empty: feats.append((k, g, t, 'w%d' % w['id']))
for r in rels.values():
    t = r['tags']
    if t.get('type') not in ('multipolygon', 'building'): continue
    k = 'platform' if platform_kind(t) else 'station' if station_area_kind(t) else 'indoor' if indoor_area_kind(t) else None
    if not k: continue
    g = rel_polygon(r)
    if g is not None: feats.append((k, g, t, 'r%d' % r['id']))
print(collections.Counter(f[0] for f in feats), flush=True)
tree = STRtree([f[1] for f in feats])

# ---------- stop areas: which OpenStreetMap objects belong to which station ----------
sa_of = collections.defaultdict(set)          # station index -> stop area ids (with their groups' other stop areas)
for i, rows in enumerate(index):
    for r in rows:
        if r[3].startswith('sa'): sa_of[i].add(int(r[3][2:]))
group_of = collections.defaultdict(set)
for r in rels.values():
    if r['tags'].get('public_transport') == 'stop_area_group':
        mem = {m[1] for m in r['members'] if m[0] == 'r'}
        for m in mem: group_of[m] |= mem
member_station = {}                           # 'n123' / 'w45' / 'r6' -> station index
entrance_members = collections.defaultdict(set)
for i in range(NST):
    own = set(sa_of[i])
    for s in list(own): own |= {x for x in group_of.get(s, ()) if x in rels and rels[x]['tags'].get('public_transport') == 'stop_area'}
    for s in own:
        r = rels.get(s)
        if not r: continue
        for t, ref, role in r['members']:
            key = t + str(ref)
            member_station.setdefault(key, i)
            if t == 'n' and ref in nodes:
                nt = nodes[ref]['tags']
                if 'entrance' in role or 'entrance' in nt or nt.get('railway') in ('subway_entrance', 'train_station_entrance') or nt.get('public_transport') == 'entrance':
                    entrance_members[i].add(ref)

# platforms some other stop area claims (a mainline or RER station's, say) are not ours, however near our track
in_other_sa = set()
for l in open(f'{OSM}/rels.jsonl', encoding='utf8'):
    if '"stop_area"' not in l: continue
    r = json.loads(l)
    if r['tags'].get('public_transport') != 'stop_area': continue
    for t, ref, role in r['members']:
        if t in ('w', 'r'):
            key = t + str(ref)
            if key not in member_station: in_other_sa.add(key)
print(len(in_other_sa), 'ways and relations in other stop areas', flush=True)

# ---------- exits ----------
EXIT_RE = [
    re.compile(r'(?:exit|ausgang|sortie|salida|uscita|saída|wyjście|výstup|kijárat|выход)\s*([A-Za-z]?\d{0,2}[A-Za-z]?)\b', re.I),
    re.compile(r'([A-Za-z]?\d{1,2}[A-Za-z]?|[A-Za-z])\s*(?:号)?\s*(?:出入口|出口|入口|口|番出口|番出入口|번\s*출구|號出口|号出入口)'),
    re.compile(r'(?:出口|出入口)\s*([A-Za-z]?\d{0,2}[A-Za-z]?)'),
]
def exit_label(t):
    ref = (t.get('ref') or t.get('local_ref') or '').strip()
    if ref and len(ref) <= 4 and not ' ' in ref: return ref
    for key in ('name', 'name:en', 'name:zh', 'name:ja', 'name:ko', 'description'):
        v = t.get(key) or ''
        for rx in EXIT_RE:
            m = rx.search(v)
            if m and m.group(1): return m.group(1).upper() if len(m.group(1)) <= 1 else m.group(1)
    return ''

exits = collections.defaultdict(list)       # station -> [(lon, lat, label, name, osm id)]
taken = set()
# an exit two stations' stop areas share (Houhai's lines 2 and 11 are two stations 300 m apart) goes to the nearer
claims = collections.defaultdict(list)
for i, ids in entrance_members.items():
    for n in ids: claims[n].append(i)
for n, cl in claims.items():
    o = nodes[n]; taken.add(n)
    i = min(cl, key=lambda j: min(km((o['lon'], o['lat']), (q[1], q[2])) for q in index[j]))
    exits[i].append((o['lon'], o['lat'], exit_label(o['tags']), o['tags'].get('name', ''), n))
for o in nodes.values():
    if o['id'] in taken: continue
    t = o['tags']; r = t.get('railway')
    if not (r in ('subway_entrance', 'train_station_entrance') or t.get('public_transport') == 'entrance'): continue
    if t.get('disused') == 'yes' or 'disused:railway' in t: continue
    lim = TRAIN_EXIT_KM if r == 'train_station_entrance' else EXIT_KM
    cand = near_stations((o['lon'], o['lat']), lim)
    if not cand: continue
    exits[cand[0][1]].append((o['lon'], o['lat'], exit_label(t), t.get('name', ''), o['id']))

# ---------- per station: boxes, areas, passages ----------
# every line's track, cut into short pieces for a spatial index (lon/lat)
seg_geom, seg_line = [], []
for li, l in enumerate(L):
    g = geo.get(l[0])
    if not g: continue
    parts = g['coordinates'] if g['type'] == 'MultiLineString' else [g['coordinates']]
    for p in parts:
        for a in range(0, len(p) - 1, 12):
            piece = p[a:a + 13]
            if len(piece) >= 2: seg_geom.append(LineString(piece)); seg_line.append(li)
seg_tree = STRtree(seg_geom)
def track_near(li, loc, centre_xy, r=400):
    """line li's track within r metres of centre_xy, in loc's metres"""
    c = loc.ll(centre_xy); dx = r / loc.kx; dy = r / loc.ky
    out = []
    for k in seg_tree.query(sbox(c[0] - dx, c[1] - dy, c[0] + dx, c[1] + dy)):
        if seg_line[k] != li: continue
        out.append(LineString(loc.geom(seg_geom[k].coords)))
    if not out: return None
    u = unary_union(out).intersection(Point(centre_xy).buffer(r))
    return None if u.is_empty else u

# direction of each line at each station from its neighbours along the line's routes, for lines without track
ROUTES = [l[29] if len(l) > 29 and isinstance(l[29], list) else [] for l in L]
def route_deg(i, li, loc):
    for r in ROUTES[li]:
        if i not in r: continue
        k = r.index(i)
        a = r[max(0, k - 1)]; b = r[min(len(r) - 1, k + 1)]
        if a == b: continue
        pa = loc.xy((lon[a], lat[a])); pb = loc.xy((lon[b], lat[b]))
        return math.degrees(math.atan2(pb[1] - pa[1], pb[0] - pa[0])) % 180
    return None

def axis_deg(g):
    """direction of a geometry's long axis, degrees in [0, 180)"""
    mrr = g.minimum_rotated_rectangle
    if mrr.geom_type != 'Polygon':
        c = list(g.coords) if hasattr(g, 'coords') else [(0, 0), (1, 0)]
        (x0, y0), (x1, y1) = c[0], c[-1]
    else:
        c = list(mrr.exterior.coords)
        e1 = (c[1][0] - c[0][0], c[1][1] - c[0][1]); e2 = (c[2][0] - c[1][0], c[2][1] - c[1][1])
        (x0, y0), (x1, y1) = ((0, 0), e1) if math.hypot(*e1) >= math.hypot(*e2) else ((0, 0), e2)
    return math.degrees(math.atan2(y1 - y0, x1 - x0)) % 180

def tangent_deg(track, pt):
    """direction of the track at the point nearest pt"""
    best = None
    geoms = track.geoms if hasattr(track, 'geoms') else [track]
    for g in geoms:
        if g.geom_type != 'LineString' or g.length == 0: continue
        d = g.distance(pt)
        if best is None or d < best[0]: best = (d, g)
    if not best: return None
    g = best[1]; s = g.project(pt)
    a = g.interpolate(max(0, s - 30)); b = g.interpolate(min(g.length, s + 30))
    if a.distance(b) < 1: return None
    return math.degrees(math.atan2(b.y - a.y, b.x - a.x)) % 180, nearest_points(g, pt)[0], best[0]

def box_len(lid):
    """length of an approximate station box: the line's train, plus stairs and plant rooms"""
    l = lines_csv.get(lid, {})
    cars = num(l.get('cars_per_train', '')) or 6
    try: under = float(l.get('tunnel_share_osm') or 0) >= 0.5
    except ValueError: under = False
    return min(max(cars * CAR_M + (60 if under else 20), 80), 300)

def angdiff(a, b):
    d = abs(a - b) % 180
    return min(d, 180 - d)

def rect(cx, cy, deg, length, width):
    b = sbox(-length / 2, -width / 2, length / 2, width / 2)
    return affinity.translate(affinity.rotate(b, deg, origin=(0, 0)), cx, cy)

def ring_ll(loc, poly, tol=0.8):
    poly = poly.simplify(tol, preserve_topology=True)
    polys = poly.geoms if hasattr(poly, 'geoms') else [poly]
    out = []
    for p in polys:
        if p.geom_type != 'Polygon' or p.area < 4: continue
        out.append([loc.ll(c) for c in p.exterior.coords])
    return out

def line_ll(loc, g, tol=0.8):
    g = g.simplify(tol)
    gs = g.geoms if hasattr(g, 'geoms') else [g]
    return [[loc.ll(c) for c in x.coords] for x in gs if x.geom_type == 'LineString' and x.length > 3]

# platforms: each to the (station, line) whose track it runs along
plat_ids = [k for k, f in enumerate(feats) if f[0] == 'platform']
plat_to = collections.defaultdict(list)       # (station, line) -> [feature index]
for k in plat_ids:
    kind, g, t, oid = feats[k]
    c = g.centroid; p = (c.x, c.y)
    cand = near_stations(p, PLATFORM_KM)
    owner = member_station.get(oid)
    if owner is None and oid in in_other_sa: continue
    if owner is not None and all(i != owner for _, i in cand): cand.append((0, owner))
    if not cand: continue
    loc = Local(*p); gx = Polygon(loc.geom(g.exterior.coords)) if g.geom_type == 'Polygon' else \
        LineString(loc.geom(g.coords)) if g.geom_type == 'LineString' else None
    if gx is None:
        gx = unary_union([Polygon(loc.geom(x.exterior.coords)) for x in getattr(g, 'geoms', []) if x.geom_type == 'Polygon'])
    if gx.is_empty: continue
    ad = axis_deg(gx)
    best = None
    for d, i in cand:
        for li, _ in st['lines'][i]:
            tr = track_near(li, loc, (0, 0), 500)
            if tr is None: continue
            dist = tr.distance(gx)
            if dist > TRACK_M: continue
            tg = tangent_deg(tr, gx.centroid)
            if tg and angdiff(tg[0], ad) > ANGLE and gx.length > 30: continue
            score = dist + 20 * d - (15 if owner == i else 0)
            if best is None or score < best[0]: best = (score, i, li)
    if best: plat_to[(best[1], best[2])].append(k)

# one line's platforms at a station are tagged alike: where some are tagged subway / light_rail, untagged ones beside
# them are another railway's (Châtelet's RER platforms lie under line 14's), and they share one level
METRO_TAG = ('subway', 'light_rail', 'monorail')
for key, ks in list(plat_to.items()):
    tagged = [k for k in ks if any(feats[k][2].get(x) == 'yes' for x in METRO_TAG)]
    if tagged and len(tagged) < len(ks): ks = tagged
    lv = collections.Counter((feats[k][2].get('level') or feats[k][2].get('layer') or '') for k in ks)
    if len(lv) > 1:
        top = lv.most_common(1)[0][0]
        ks = [k for k in ks if (feats[k][2].get('level') or feats[k][2].get('layer') or '') == top]
    plat_to[key] = ks

if os.environ.get('DEBUG_STATION'):
    for (i, li), ks in plat_to.items():
        if i == int(os.environ['DEBUG_STATION']):
            for k in ks: print('platform', L[li][0], feats[k][3], {x: v for x, v in feats[k][2].items() if x in ('name', 'ref', 'layer', 'level', 'railway', 'public_transport', 'subway', 'train', 'local_ref')})
stations_by_sys = collections.defaultdict(list)
for i in range(NST): stations_by_sys[st_sys[i]].append(i)
import shapely
def to_ll_poly(loc, poly):
    polys = poly.geoms if hasattr(poly, 'geoms') else [poly]
    return unary_union([shapely.make_valid(Polygon([loc.ll(c) for c in p.exterior.coords], [[loc.ll(c) for c in h.coords] for h in p.interiors]))
                        for p in polys if p.geom_type == 'Polygon'])
def from_ll(loc, g):
    """lon/lat geometry to loc's metres"""
    return shapely.transform(g, lambda a: np.column_stack(((a[:, 0] - loc.lo) * loc.kx, (a[:, 1] - loc.la) * loc.ky)))

def cut(a, b):
    for grid in (None, 0.01, 0.1):
        try: return a.intersection(b) if grid is None else shapely.intersection(a, b, grid_size=grid)
        except shapely.errors.GEOSException: pass
    return None

def split_by_boxes(area, labelled):
    """Cut an area (metres) among the boxes in `labelled` [(label, box polygon)]: each piece goes to the box it is
    nearest, so one hall shared by two lines is drawn half in each line's colour, as Baidu Maps does."""
    if len(labelled) == 1: return {labelled[0][0]: area}
    seeds, labs, have = [], [], set()
    for lab, b in labelled:
        ring = b.exterior
        n = max(4, int(ring.length / 8))
        for k in range(n):
            q = ring.interpolate(k / n, normalized=True)
            key = (round(q.x, 1), round(q.y, 1))
            if key in have: continue
            have.add(key); seeds.append(Point(key)); labs.append(lab)
    cells = shapely.voronoi_polygons(shapely.MultiPoint(seeds), extend_to=area.envelope.buffer(200), ordered=True)
    by = collections.defaultdict(list)
    for cell, lab in zip(cells.geoms, labs): by[lab].append(cell)
    out = {}
    for lab, cs in by.items():
        # cut cell by cell (each cell is convex, so the cuts are robust), then join the bits
        bits = [x for x in (cut(area, c) for c in cs) if x is not None and not x.is_empty and x.area > 0.01]
        if not bits: continue
        try: piece = shapely.union_all(bits)
        except shapely.errors.GEOSException: piece = shapely.union_all([x.buffer(0.05) for x in bits])
        if piece.area > 4: out[lab] = piece
    return out

cover = []
total = collections.Counter()
ONLY = set(os.environ.get('ONLY', '').split(',')) - {''}   # ONLY=cn-shenzhen-metro,... rebuilds just those systems
for si, sysrow in enumerate(S):
    if ONLY and sysrow[0] not in ONLY: continue
    out = {'v': 1, 'boxes': [], 'areas': [], 'paths': [], 'exits': []}
    sys_boxes = {}                                   # (station, line) -> lon/lat box polygon
    area_claims = collections.defaultdict(set)       # OpenStreetMap id -> stations it belongs to
    path_claims = collections.defaultdict(set)
    stat = {}
    for i in stations_by_sys[si]:
        loc = Local(float(lon[i]), float(lat[i]))
        rows = index[i]
        boxes_xy = []; box_cols = []
        n_mapped = n_approx = 0
        for li, _y in st['lines'][i]:
            lid = L[li][0]
            pts = [loc.xy((r[1], r[2])) for r in rows if r[0] == li] or [(0.0, 0.0)]
            cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
            tr = track_near(li, loc, (cx, cy), 600)
            got = None
            ps = plat_to.get((i, li))
            if ps:
                geoms = []
                for k in ps:
                    g = feats[k][1]
                    gx = Polygon(loc.geom(g.exterior.coords)) if g.geom_type == 'Polygon' else \
                        LineString(loc.geom(g.coords)).buffer(4, cap_style=2) if g.geom_type == 'LineString' else \
                        unary_union([Polygon(loc.geom(x.exterior.coords)) for x in g.geoms if x.geom_type == 'Polygon'])
                    geoms.append(gx)
                pu = unary_union(geoms)
                tg = tangent_deg(tr, Point(cx, cy)) if tr is not None else None
                if tg and tg[2] <= 250:
                    # a rectangle along the track: as long as the platforms beside it, at most BOX_HALF_W either side
                    o = tg[1]
                    rot = affinity.rotate(affinity.translate(pu, -o.x, -o.y), -tg[0], origin=(0, 0))
                    rot = rot.intersection(sbox(-PLATFORM_ALONG_M, -BOX_HALF_W, PLATFORM_ALONG_M, BOX_HALF_W))
                    if not rot.is_empty:
                        x0, y0, x1, y1 = rot.bounds
                        y0 = min(y0, -8) - 3; y1 = max(y1, 8) + 3; x0 -= 3; x1 += 3
                        if 30 <= x1 - x0 <= MAX_BOX_M:
                            bx = affinity.translate(affinity.rotate(sbox(x0, y0, x1, y1), tg[0], origin=(0, 0)), o.x, o.y)
                            got = (bx, 0)
                elif tr is None:
                    mrr = pu.minimum_rotated_rectangle.buffer(3, join_style=2)
                    c = list(mrr.exterior.coords)
                    L1 = math.hypot(c[1][0] - c[0][0], c[1][1] - c[0][1]); L2 = math.hypot(c[2][0] - c[1][0], c[2][1] - c[1][1])
                    if max(L1, L2) <= MAX_BOX_M and min(L1, L2) <= 2 * BOX_HALF_W and mrr.area > 200:
                        got = (mrr, 0)
            if got is None and tr is not None:
                tg = tangent_deg(tr, Point(cx, cy))
                if tg and tg[2] <= 250:
                    got = (rect(tg[1].x, tg[1].y, tg[0], box_len(lid), BOX_W), 1)
            if got is None:
                # no track near: lay the box between the station's neighbours on the line
                deg = route_deg(i, li, loc)
                if deg is not None:
                    got = (rect(cx, cy, deg, box_len(lid), BOX_W), 1)
            if got is None: continue
            # lines that share a platform and a colour (New York's 1, 2 and 3) get one box
            col = (L[li][5] or '').lower()
            if any(col and c2 == col and got[0].intersection(b2).area > 0.6 * min(got[0].area, b2.area) for c2, b2 in box_cols): continue
            box_cols.append((col, got[0]))
            boxes_xy.append(got[0])
            if got[1]: n_approx += 1
            else: n_mapped += 1
            sys_boxes[(i, li)] = to_ll_poly(loc, got[0])
            for ring in ring_ll(loc, got[0], 0.3):
                out['boxes'].append([i, li, got[1], [[round(x * 1e6), round(y * 1e6)] for x, y in ring]])
        # concourses and halls that belong to it: its stop area's, or ones touching its boxes
        allbox = unary_union(boxes_xy) if boxes_xy else Point(0, 0).buffer(20)
        reach = allbox.buffer(60)
        for k in tree.query(Point(loc.ll((0, 0))).buffer(0.004)):
            kind, g, t, oid = feats[k]
            if kind not in ('station', 'indoor') or g.geom_type not in ('Polygon', 'MultiPolygon'): continue
            gx = shapely.make_valid(from_ll(loc, g)).buffer(0)
            if gx.is_empty or gx.area > AREA_MAX_M2: continue
            mine = member_station.get(oid) == i
            if not mine and (gx.area > NEAR_AREA_M2 or not gx.intersects(reach)): continue
            if not mine and kind == 'station' and not (gx.distance(Point(0, 0)) < 80 or gx.intersects(allbox)): continue
            area_claims[k].add(i)
        # exits
        seen = set()
        for x, y, lab, name, oid in exits.get(i, []):
            key = (round(x, 5), round(y, 5))
            if key in seen: continue
            seen.add(key)
            out['exits'].append([i, round(x * 1e6), round(y * 1e6), lab, name])
        # underground passages that lead to it (to a box, a hall or an exit)
        targets = [allbox.buffer(30)] + [Point(loc.xy((x, y))).buffer(20) for x, y, *_ in exits.get(i, [])]
        targets += [from_ll(loc, feats[k][1]).buffer(15) for k, cl in area_claims.items() if i in cl]
        tu = unary_union(targets)
        for k in tree.query(Point(loc.ll((0, 0))).buffer(0.003)):
            kind, g, t, oid = feats[k]
            if kind != 'passage' or g.geom_type != 'LineString': continue
            gx = from_ll(loc, g)
            if gx.distance(Point(0, 0)) > 250 or not gx.intersects(tu): continue
            path_claims[k].add(i)
        stat[i] = [n_mapped, n_approx, len(seen)]

    # halls: each OpenStreetMap area once, cut among the boxes of the stations it belongs to (and any other box it
    # covers), each piece in its line's colour; overlapping halls of one line are merged
    pieces = collections.defaultdict(list)
    box_tree_keys = list(sys_boxes)
    box_tree = STRtree([sys_boxes[k] for k in box_tree_keys]) if box_tree_keys else None
    for k, cl in area_claims.items():
        g = feats[k][1]; c = g.centroid; loc = Local(c.x, c.y)
        gx = shapely.make_valid(from_ll(loc, g)).buffer(0)
        labs = {key for key in box_tree_keys if key[0] in cl}
        if box_tree is not None:
            for j in box_tree.query(g.buffer(0.0003)): labs.add(box_tree_keys[j])
        labelled = [(lab, from_ll(loc, sys_boxes[lab])) for lab in sorted(labs)]
        if not labelled:
            i0 = min(cl); labelled = [((i0, st['lines'][i0][0][0]), Point(loc.xy((lon[i0], lat[i0]))).buffer(20))]
        for lab, piece in split_by_boxes(gx, labelled).items():
            pieces[lab].append(to_ll_poly(loc, piece))
    n_areas = collections.Counter()
    for (i, li), ps in pieces.items():
        loc = Local(float(lon[i]), float(lat[i]))
        u = from_ll(loc, unary_union([shapely.make_valid(p) for p in ps])).buffer(0)
        for ring in ring_ll(loc, u, 0.6):
            out['areas'].append([i, li, [[round(x * 1e6), round(y * 1e6)] for x, y in ring]]); n_areas[i] += 1
    # passages: each once, with the station and line whose box (else exit) is nearest
    for k, cl in path_claims.items():
        g = feats[k][1]
        best = None
        for i in cl:
            for li, _y in st['lines'][i]:
                b = sys_boxes.get((i, li))
                d = b.distance(g) if b is not None else km((lon[i], lat[i]), (g.centroid.x, g.centroid.y)) / 111
                if best is None or d < best[0]: best = (d, i, li)
        _, i, li = best
        loc = Local(float(lon[i]), float(lat[i]))
        for c in line_ll(loc, from_ll(loc, g).intersection(Point(0, 0).buffer(320)), 0.6):
            out['paths'].append([i, li, [[round(x * 1e6), round(y * 1e6)] for x, y in c]])
    for i in stations_by_sys[si]:
        nm = st['en'][i] or st['name'][i]
        n_mapped, n_approx, n_exits = stat[i]
        cover.append({'system_id': sysrow[0], 'city': sysrow[2], 'station': nm, 'lines': len(st['lines'][i]),
                      'boxes_mapped': n_mapped, 'boxes_approx': n_approx, 'exits': n_exits,
                      'exits_labelled': sum(1 for e in out['exits'] if e[0] == i and e[3]), 'areas': n_areas[i]})
    for k in ('boxes', 'areas', 'paths', 'exits'): total[k] += len(out[k])
    json.dump(out, open(f'{OUT}/{sysrow[0]}.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
with open(COVER, 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=list(cover[0].keys())); w.writeheader(); w.writerows(cover)
print(dict(total), len(cover), 'stations')
