# Station structures and exits for the /metro page, from OpenStreetMap.
#
#   python3 scripts/metro/build_structures.py DB METRO_JSON STATION_INDEX OSM_DIR OUT_DIR COVERAGE_CSV
#
# DB is the project's metro database (metro/db), METRO_JSON and STATION_INDEX come from build_metro.py (its optional
# third argument), OSM_DIR holds the planet extracts written by scripts/metro/osm/ (rels_sel.jsonl, ways.*.jsonl,
# nodes.*.jsonl, nxy.*.npy), and OUT_DIR gets one file per system (public/metro/structures/<system>.json). The OSM2
# environment variable names the second pass's directory (ways2.*.jsonl, rels2.jsonl, nxy2.*.npy: station buildings
# found by name or below ground). ONLY=system_id,... rebuilds just those systems. Needs numpy and shapely.
#
# For every station on the page, and every line serving it:
#   box    the station's structure for that line, in the line's colour: the rotated rectangle around the line's mapped
#          platforms (railway=platform, public_transport=platform) and the track beside them; where OpenStreetMap
#          has no platform for it, a box of the line's train length laid along its track at the line's stop
#          positions, stretched to reach the line's exits, marked approximate
#   area   concourses and station halls: station areas of its stop area (public_transport=station,
#          building=train_station), the station's own building, buildings named after it, and indoor areas and
#          underground buildings that touch the boxes
#   path   underground passages (footways, steps and corridors in tunnels or below ground) leading to it, and, dashed,
#          estimated passages from exits that no mapped passage reaches and between the disconnected parts of a station
#          (areas and paths take the colour of the nearest line's box, as Baidu Maps draws them)
#   exit   its entrances (railway=subway_entrance, railway=train_station_entrance, public_transport=entrance, and the
#          entrance members of its stop area), labelled with the exit's letter or number where OpenStreetMap has one
import csv, glob, json, math, os, re, sys, collections, unicodedata
import numpy as np
from shapely.geometry import LineString, MultiLineString, Point, Polygon, MultiPolygon, box as sbox
from shapely.ops import unary_union, polygonize, nearest_points, linemerge
from shapely import affinity
from shapely.strtree import STRtree

DB, METRO, INDEX, OSM, OUT, COVER = sys.argv[1:7]
OSM2 = os.environ.get('OSM2', '')
EXIT_KM = 0.35        # an exit belongs to the nearest station within this distance (stop area members always count)
TRAIN_EXIT_KM = 0.15  # railway=train_station_entrance is often a mainline station's: only near ones count
PLATFORM_KM = 0.35    # platforms are looked for this far from a station
TRACK_M = 14          # a platform must lie this close to the line's track ...
ANGLE = 30            # ... and run within this many degrees of it
OWN_TRACK_M = 45      # a platform of the station's own stop area may lie this far from the track (split tracks) ...
OWN_ANGLE = 15        # ... if it runs this parallel to it
BOX_W = 24            # approximate box: two tracks and an island platform, with the walls
CAR_M = 21            # approximate box: this much per car (17 for rubber-tyred cars), plus 60 m for an underground
TYRE_CAR_M = 17       # station's plant rooms and stairs (20 m for one above ground)
MAX_BOX_M = 340       # a platform box longer than this is a mapping slip: the approximate box is used instead
AREA_MAX_M2 = 120_000 # station areas larger than this are whole rail yards or terminals, not a metro concourse
NEAR_AREA_M2 = 40_000 # a hall not in the station's stop area counts only up to this size
BOX_HALF_W = 20       # a box from platforms reaches at most this far either side of its track (40 for split tracks)
EXIT_LATERAL_M = 90   # approximate box: an exit this close to a line's track stretches that line's box along the track
EXIT_INSET_M = 10     #   to this far short of the exit (the exit's own stairs and passage)
MAX_HALF_M = 180      #   but no further than this from the station either way
STOP_SHIFT_M = 250    # a line's own stop positions move its box centre at most this far from the station's point
TERM_END_M = 15       # at a terminus the approximate box ends this far past the end of the track
STRETCH_EXTRA_M = 60  #   and an exit stretches a box only within box_len / 2 + this of its centre (farther ones get a passage)
CONNECT_MAX_M = 150   # an exit with no mapped passage is joined to the station by an estimated passage up to this long
CONNECT_FAR_M = 250   #   (this long when the exit lies along one of the station's lines)
LINK_MAX_M = 200      # the disconnected parts of one station (two lines' boxes with no hall between) likewise
UP_HALL_M2 = 20_000   # an above-ground station building of the station's own stop area counts up to this size
METRO_TAG = ('subway', 'light_rail', 'monorail')
NAME_KEYS = ('name', 'name:en', 'name:zh', 'name:zh-Hans', 'name:zh-Hant', 'name:ja', 'name:ko', 'official_name', 'alt_name')

def num(x):
    """cars per train from the database's text: the largest plain count ('6 or 8' is 8, '3–4' is 4), never a model
    number ('MPM-10') or a train length ('9-car')"""
    best = None
    for m in re.finditer(r'(?<!\w)(\d{1,2})(?!\w)', x or ''):
        n = int(m.group(1)); a, b = m.start(), m.end()
        if not 1 <= n <= 12: continue
        if a >= 2 and x[a - 1] in '-–' and x[a - 2].isalpha(): continue
        if x[b:b + 4] in ('-car', '–car'): continue
        if best is None or n > best: best = n
    return best

_NAME_DROP = re.compile(r'(地铁站|地鐵站|捷運站|捷运站|轨道交通|站|駅|역|\bstation\b|\bmetro\b|\bsubway\b|\bunderground\b|\bu-bahn\b|'
                        r'\bs-bahn\b|\bmrt\b|\blrt\b|\bstazione\b|\bestación\b|\bestacion\b|\bestação\b|\bestacao\b|\bestació\b|\bgare\b|\bbahnhof\b|'
                        r'สถานี|محطة|станция|\bl[íi]nea\s*\d+\b|\bl\d{1,2}\b|\(.*?\)|（.*?）)', re.I)   # 'Pantitlán L1', 'Bellas Artes (Línea 2)'
def norm_name(v):
    v = unicodedata.normalize('NFKD', v or '')
    v = ''.join(ch for ch in v if not unicodedata.combining(ch))   # 'Félix U. Gómez' matches 'Felix U. Gomez'
    v = _NAME_DROP.sub('', v.lower()).strip()
    v = re.sub(r'^(?:di|de|del|della|des|du|do|da|of)\s+', '', v)   # stazione di X, gare de X
    return re.sub(r"[\s\-–—·・.,'’\"/]+", '', v)
def same_name(t, names):
    """an OpenStreetMap object named after the station (岗厦北站 for 岗厦北, Gangxia North Station for Gangxia North)"""
    for k in NAME_KEYS:
        v = norm_name(t.get(k))
        if not v: continue
        if v in names: return True
    return False

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
# lines whose cars are trams or light rail vehicles: tram platforms count for them only
TRAM_LINE = {li for li, l in enumerate(L) if re.search(r'tram|light|premetro|stadtbahn|lrv|lrt', (lines_csv.get(l[0], {}).get('car_type') or '').lower())}

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
_files = sorted(glob.glob(f'{OSM}/nxy.*.npy')) + (sorted(glob.glob(f'{OSM2}/nxy2.*.npy')) if OSM2 else [])
_a = np.concatenate([np.load(f) for f in _files], axis=1)
_o = np.argsort(_a[0], kind='stable')
NID = _a[0][_o]; NX = _a[1][_o] / 1e7; NY = _a[2][_o] / 1e7
del _a, _o
nodes = {}
for f in sorted(glob.glob(f'{OSM}/nodes.*.jsonl')):
    for l in open(f, encoding='utf8'):
        o = json.loads(l); nodes[o['id']] = o
def node_xy(nid):
    k = np.searchsorted(NID, nid)
    if k < len(NID) and NID[k] == nid: return float(NX[k]), float(NY[k])
    o = nodes.get(nid)
    return (o['lon'], o['lat']) if o else None
ways = {}
def near_way(o):
    """a way whose first node is within 1.2 km of a page station (the rest are nowhere near one)"""
    c = node_xy(o['nodes'][0]) if o['nodes'] else None
    return bool(c) and bool(near_stations(c, 1.2))
for f in sorted(glob.glob(f'{OSM}/ways.*.jsonl')):
    for l in open(f, encoding='utf8'):
        o = json.loads(l)
        if near_way(o): ways[o['id']] = o
rels = {}
for l in open(f'{OSM}/rels_sel.jsonl', encoding='utf8'):
    o = json.loads(l); rels[o['id']] = o
n2 = 0
if OSM2:
    # the second pass: buildings named like a station or below ground, and their multipolygons (flagged p2)
    for f in sorted(glob.glob(f'{OSM2}/ways2.*.jsonl')):
        for l in open(f, encoding='utf8'):
            o = json.loads(l)
            if o['id'] not in ways and near_way(o): o['p2'] = 1; ways[o['id']] = o; n2 += 1
    for l in open(f'{OSM2}/rels2.jsonl', encoding='utf8'):
        o = json.loads(l)
        if o['id'] not in rels: o['p2'] = 1; rels[o['id']] = o; n2 += 1
print(len(NID), 'node locations', len(nodes), 'tagged nodes', len(ways), 'ways', len(rels), 'relations', n2, 'from the second pass', flush=True)

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

NOT_HALL = {'parking', 'garage', 'garages', 'retail', 'commercial', 'residential', 'apartments', 'hotel', 'office'}
def neg(v):
    """every listed level below ground: a building spanning '-2;-1;0;1' (Gare Montparnasse) is not an underground hall"""
    return bool(v) and all(re.match(r'^\s*-', x) for x in v.split(';'))
def neg_any(v):
    """any listed level below ground: stairs from the street to a concourse are level 0;-1"""
    return bool(v) and any(x.strip().startswith('-') for x in v.split(';'))
def pos(v):
    try: return float((v or '0').split(';')[0]) > 0
    except ValueError: return False

RAILPLAT = {'train', 'subway', 'light_rail', 'monorail'}
def metro_mode(t):
    return any(t.get(k) == 'yes' for k in METRO_TAG)
def platform_kind(t):
    # a mainline platform (train=yes, and no metro mode) is not a metro station's, however near its track it lies:
    # St Pancras' platforms sit right over the Piccadilly line; nor is a bus stop's
    if t.get('train') == 'yes' and not metro_mode(t): return False
    if (t.get('bus') == 'yes' or t.get('trolleybus') == 'yes' or t.get('highway') in ('bus_stop', 'platform')) and not metro_mode(t): return False
    if t.get('railway') == 'platform': return True
    if t.get('public_transport') == 'platform':
        if any(t.get(k) == 'yes' for k in RAILPLAT) or t.get('railway'): return True
        # tagged with nothing else but lying below ground (Toei's Kuramae): a metro platform, not a bus stop's
        return t.get('tram') != 'yes' and below_ground(t)
    return False
def tram_only(t):
    return t.get('tram') == 'yes' and not metro_mode(t)

def below_ground(t):
    if t.get('location') in ('surface', 'overground', 'overhead', 'bridge') or t.get('bridge') == 'yes': return False
    if neg(t.get('layer')) or neg(t.get('level')) or t.get('location') == 'underground' or t.get('tunnel') == 'yes': return True
    # a passage through a building is at street level unless a level says otherwise (Xi'an's city-wall gates)
    return t.get('tunnel') == 'building_passage' and (neg_any(t.get('layer')) or neg_any(t.get('level')))

BUS_RE = re.compile(r'公交|客运|巴士|汽车站|\bbus\b|\bcoach\b|\bautobus\b', re.I)
def busy(t):
    """a bus or coach station: never a metro hall, however it is named (Changsha's 长沙火车站 bus terminals)"""
    if t.get('amenity') == 'bus_station': return True
    if (t.get('bus') == 'yes' or t.get('trolleybus') == 'yes') and not (metro_mode(t) or t.get('train') == 'yes'): return True
    return bool(BUS_RE.search(' '.join(t.get(k, '') for k in ('name', 'name:en', 'network', 'operator'))))
def unbuilt(t):
    """still being built (Wuhe's intercity station, construction=train_station): not drawn"""
    if 'construction' in t or t.get('landuse') == 'construction' or t.get('railway') == 'construction': return True
    # a metro station's own building left tagged building=construction after the line opened (Nanjing line 5's) still counts
    if t.get('building') == 'construction':
        return not ((t.get('railway') == 'station' or t.get('public_transport') == 'station') and metro_mode(t))
    return False
def weak_station(t):
    """public_transport=station with nothing that says rail: not evidence enough for a hall outside the station's stop area"""
    if t.get('public_transport') != 'station' or 'building' in t: return False
    return not (t.get('railway') in ('station', 'halt') or t.get('station') in ('subway', 'light_rail', 'train') or metro_mode(t) or t.get('train') == 'yes')

def station_area_kind(t):
    """a metro station's own hall: underground, or tagged as a subway station (a mainline terminus's train shed is not)"""
    if busy(t): return False
    if t.get('building') == 'transportation' and below_ground(t): return True
    if not (t.get('public_transport') == 'station' or t.get('railway') in ('station', 'halt') or t.get('building') == 'train_station'): return False
    return below_ground(t) or t.get('station') in ('subway', 'light_rail') or t.get('subway') == 'yes'

def station_up_kind(t):
    """a station building or area above ground (Wimbledon's, Xipu's): used only when it is the station's own, or named after it"""
    if busy(t): return False
    if not (t.get('public_transport') == 'station' or t.get('railway') in ('station', 'halt') or t.get('building') in ('train_station', 'transportation')): return False
    return not station_area_kind(t)

def own_bld_kind(t):
    """a building of the station's own stop area with no station tag (Nanjing's 汉中门, building=yes, layer -1)"""
    if t.get('train') == 'yes' and not metro_mode(t): return False
    if busy(t) or t.get('building') in NOT_HALL or 'shop' in t: return False
    if 'building' in t or t.get('location') == 'underground': return True
    # a concourse outline with no level at all, listed by the station's own stop area (Mexico City's Bellas Artes)
    return t.get('indoor') in ('area', 'room', 'corridor') and not any(k in t for k in ('level', 'layer', 'tunnel'))

UNDERPASS_RE = re.compile(r'زیرگذر|地下通道|地下街|underpass|unterführung|passage souterrain|sottopass', re.I)
def ring_kinds(c, t=None):
    """a closed footway below ground with no area tag (Luoyang's platform and concourse outlines): a platform-shaped
    ring is an indoor area and a platform candidate, a wide ring or a named underpass (Tehran's Teatr-e Shahr) a hall,
    any other ring a passage"""
    loc = Local(*c[0]); p = Polygon(loc.geom(c))
    if not p.is_valid: p = p.buffer(0)
    if p.is_empty: return ['passage']
    mrr = p.minimum_rotated_rectangle
    if mrr.geom_type == 'Polygon':
        q = list(mrr.exterior.coords); e1 = math.dist(q[0], q[1]); e2 = math.dist(q[1], q[2])
        if max(e1, e2) >= 50 and 5 <= min(e1, e2) <= 25 and p.area <= 6000: return ['indoor', 'platform']
        if 300 <= p.area <= 6000 and (min(e1, e2) > 25 or (t and UNDERPASS_RE.search(' '.join(t.get(k, '') for k in NAME_KEYS)))): return ['indoor']
    return ['passage']

FOOT = ('corridor', 'footway', 'steps', 'path', 'pedestrian', 'elevator')
def passage_kind(t):
    hw = t.get('highway')
    if hw in FOOT or t.get('indoor') == 'corridor':
        return below_ground(t) or neg_any(t.get('level')) or neg_any(t.get('layer'))
    return False

def indoor_area_kind(t):
    if t.get('indoor') in ('area', 'room', 'corridor') and below_ground(t): return True
    # an underground pedestrian hall mapped as an area of footway
    return t.get('highway') in ('pedestrian', 'footway', 'corridor') and (t.get('area') == 'yes' or 'area:highway' in t) and below_ground(t)

def p2_kinds(t, closed):
    """kinds of a second-pass object: p2_named (a building that counts only where its name is the station's) and
    under_bld (a building below ground that counts only where it touches the station's boxes); never a shop or car park"""
    if closed:
        if t.get('building') in NOT_HALL or t.get('amenity') in ('parking', 'marketplace') or 'shop' in t: return []
        if station_area_kind(t): return ['station']
        if station_up_kind(t): return ['station_up']
        ks = []
        if ('building' in t or 'building:part' in t) and any(t.get(k) for k in NAME_KEYS): ks.append('p2_named')   # a square named like the station is not a hall
        if below_ground(t) and ('building' in t or 'building:part' in t): ks.append('under_bld')
        return ks
    if t.get('highway') in FOOT and (t.get('covered') == 'yes' or t.get('indoor') == 'yes') and not below_ground(t): return ['passage_up']
    return ['passage'] if passage_kind(t) else []

CLOSED_RE = re.compile(r'未开通|尚未开通|暂未开通|暂未开放|未启用|施工|建设中|under construction|not yet open', re.I)
def closed_exit(t):
    """an entrance not open: under construction, disused, closed off, or named so (Fitness Center's 尚未开通)"""
    if any(k in t for k in ('construction', 'construction:railway', 'disused:railway', 'proposed', 'planned')): return True
    if t.get('railway') in ('construction', 'proposed') or t.get('building') == 'construction' or t.get('disused') == 'yes' or t.get('access') == 'no': return True
    if t.get('entrance') in ('emergency', 'service', 'no') or t.get('emergency') == 'yes' or t.get('exit') == 'emergency': return True   # Milano Centrale's emergency exits
    if (t.get('opening_date') or '') > '2026-10-15': return True
    if not (t.get('ref') or t.get('local_ref') or t.get('name')):
        # an unnamed gate deep inside the station (Saint-Lazare's gates into RER E at level -5) is a transfer, not an exit
        lv = t.get('level') or t.get('layer') or ''
        try:
            if lv and max(float(x) for x in re.split(r'[;,]', lv)) <= -2: return True
        except ValueError: pass
    return bool(CLOSED_RE.search(' '.join(t.get(k, '') for k in ('name', 'description', 'note'))))

# ---------- stop areas: which OpenStreetMap objects belong to which station ----------
sa_of = collections.defaultdict(set)          # station index -> stop area ids
sa_lines = collections.defaultdict(set)       # (station, stop area) -> the lines whose rows name it
for i, rows in enumerate(index):
    for r in rows:
        if r[3].startswith('sa'): sa_of[i].add(int(r[3][2:])); sa_lines[(i, int(r[3][2:]))].add(r[0])
matched_sa = set().union(*sa_of.values()) if sa_of else set()

RAIL_OP_RE = re.compile(r'国铁|中国铁路|铁路局|城际|National Rail|Network Rail|SNCF|Transilien|Renfe|Rodalies|Cercan|Deutsche Bahn|\bDB\b|'
                        r'S-Bahn|ÖBB|SBB|Trenitalia|Trenord|Amtrak|LIRR|Metro-North|NJ Transit|Sydney Trains|GO Transit|Korail|\bKTX\b|'
                        r'台鐵|臺鐵|\bTRA\b|\bJR\b', re.I)
def foreign_sa(r):
    """a stop area that is a mainline, tram or bus station's (Fuhai West's intercity station, Shepherd's Bush's National
    Rail station): nothing in it is the metro's. A stop area with only metro entrances in it (Link City's underground
    street, which lists Shopping Park's B exits) is not foreign"""
    t = r['tags']
    if busy(t) or RAIL_OP_RE.search(' '.join(t.get(k, '') for k in ('operator', 'network'))): return True
    if (t.get('train') == 'yes' or t.get('tram') == 'yes') and not metro_mode(t): return True
    for ty, ref, role in r['members']:
        o = nodes.get(ref) if ty == 'n' else ways.get(ref) if ty == 'w' else rels.get(ref)
        mt = o.get('tags') if o else None
        if not mt or metro_mode(mt): continue
        if mt.get('train') == 'yes' or mt.get('tram') == 'yes' or mt.get('bus') == 'yes' or mt.get('trolleybus') == 'yes' or \
                mt.get('railway') in ('tram_stop', 'halt', 'train_station_entrance') or mt.get('station') in ('train', 'tram'): return True
    return False

# every other stop area: a foreign one's members are not ours; a same-named one by a station the database did not link to it
# (沈家营's, whose line 5 rows name no stop area) is adopted as the station's own
in_other_sa = set()
other_sa_nodes = set()   # entrance and stop nodes of stop areas that are no page station's (Barcelona's FGC exits by Fontana)
n_adopt = 0
for l in open(f'{OSM}/rels.jsonl', encoding='utf8'):
    if '"stop_area"' not in l: continue
    r = json.loads(l)
    if r['tags'].get('public_transport') != 'stop_area' or r['id'] in matched_sa: continue
    if foreign_sa(r):
        for t, ref, role in r['members']:
            if t in ('w', 'r'): in_other_sa.add(t + str(ref))
            else: other_sa_nodes.add(ref)
        continue
    if not any(r['tags'].get(k) for k in NAME_KEYS): continue
    # adopted only when something in it says metro (a bus stop area named like the station says nothing)
    mts = [r['tags']] + [o['tags'] for o in ((nodes.get(ref) if t == 'n' else ways.get(ref) if t == 'w' else rels.get(ref)) for t, ref, role in r['members']) if o and o.get('tags')]
    if any(mt.get('highway') == 'bus_stop' for mt in mts): continue
    if not any(metro_mode(mt) or mt.get('station') == 'subway' or mt.get('railway') in ('subway_entrance', 'station', 'stop', 'platform') for mt in mts): continue
    p = next((q for q in (node_xy(ref) for t, ref, role in r['members'] if t == 'n') if q), None)
    if p is None: continue
    for d, i in near_stations(p, 0.3):
        if same_name(r['tags'], {norm_name(st['name'][i]), norm_name(st['en'][i])} - {''}):
            sa_of[i].add(r['id']); rels.setdefault(r['id'], r); n_adopt += 1; break
print(len(in_other_sa), 'ways and relations in foreign stop areas', len(other_sa_nodes), 'nodes;', n_adopt, 'same-named stop areas adopted', flush=True)
group_of = collections.defaultdict(set)
for r in rels.values():
    if r['tags'].get('public_transport') == 'stop_area_group':
        mem = {m[1] for m in r['members'] if m[0] == 'r'}
        for m in mem: group_of[m] |= mem
member_station = {}                           # 'n123' / 'w45' / 'r6' -> station index (own stop areas and their group's)
member_own = {}                               # the same for the station's own stop areas only
ent_line = {}                                 # (station, entrance node) -> the line whose own stop area lists it
station_nodes = collections.defaultdict(set)  # station -> its station and stop nodes
entrance_members = collections.defaultdict(set)
own_ent = set()                               # (station, node): an entrance of the station's own stop area
group_skip = set()                            # entrance nodes of a group's mainline stop area that are not the metro's
for i in range(NST):
    own = set(sa_of[i]); grp = set()
    for s in list(own): grp |= {x for x in group_of.get(s, ()) if x in rels and rels[x]['tags'].get('public_transport') == 'stop_area' and x not in own}
    for s in own | grp:
        r = rels.get(s)
        if not r: continue
        for t, ref, role in r['members']:
            key = t + str(ref)
            member_station.setdefault(key, i)
            if s in own: member_own.setdefault(key, i)
            if t != 'n': continue
            nt = nodes[ref]['tags'] if ref in nodes else {}
            if role in ('station', 'stop') or role.startswith('stop') or nt.get('public_transport') in ('station', 'stop_position') or nt.get('railway') in ('station', 'stop'):
                station_nodes[i].add(ref)
            if ref in nodes:
                if not ('entrance' in role or 'entrance' in nt or nt.get('railway') in ('subway_entrance', 'train_station_entrance') or nt.get('public_transport') == 'entrance'): continue
                if closed_exit(nt): continue
                if s in own and len(sa_lines[(i, s)]) == 1: ent_line.setdefault((i, ref), next(iter(sa_lines[(i, s)])))
                # a stop area the group brings in may be a mainline station's: from it only exits that say they are the metro's
                if s in grp and not (nt.get('railway') == 'subway_entrance' or metro_mode(nt) or nt.get('entrance_marker:subway') == 'yes'): group_skip.add(ref); continue
                entrance_members[i].add(ref)
                if s in own: own_ent.add((i, ref))

# a station whose own stop areas hold mainline stop positions (train=yes and no metro mode) shares them with a railway:
# its train=yes platforms and buildings are the railway's. Elsewhere train=yes on an own platform is only the mapper's
# word for a sub-surface line (Mansion House, Westbourne Park, Athens line 1) and it counts
rail_own = set()
for i in range(NST):
    for s in sa_of[i]:
        r = rels.get(s)
        if not r: continue
        for t_, ref, role in r['members']:
            if t_ != 'n' or ref not in nodes: continue
            nt = nodes[ref]['tags']
            if (nt.get('public_transport') == 'stop_position' or nt.get('railway') in ('stop', 'station')) and nt.get('train') == 'yes' and not metro_mode(nt):
                rail_own.add(i); break
        if i in rail_own: break
print(len(rail_own), 'stations share their stop areas with a railway', flush=True)
# what a station's own stop areas (or their group's) list is ours even when a foreign stop area lists it too
in_other_sa -= set(member_station)
other_sa_nodes -= {int(k[1:]) for k in member_station if k[0] == 'n'}

# features as lon/lat shapely geometries with their kind and tags
feats = []   # (kind, geom, tags, osm id)
pass_ends = {}   # passage feature -> (first node, last node)
for w in ways.values():
    t = w['tags']
    closed = is_closed(w)
    if w.get('p2'):
        kinds = p2_kinds(t, closed)
    else:
        kinds = []
        # a platform member of the station's own stop area counts even when tagged only public_transport=platform
        if platform_kind(t) or (t.get('public_transport') == 'platform' and 'w%d' % w['id'] in member_own and not tram_only(t)
                                and not (t.get('train') == 'yes' and not metro_mode(t) and member_own['w%d' % w['id']] in rail_own)
                                and t.get('bus') != 'yes' and (t.get('highway') not in ('bus_stop', 'platform') or below_ground(t))): kinds.append('platform')
        if station_area_kind(t) and closed: kinds.append('station')
        elif station_up_kind(t) and closed: kinds.append('station_up')
        if passage_kind(t) and not closed: kinds.append('passage')
        if indoor_area_kind(t) and closed: kinds.append('indoor')
        if not closed and t.get('highway') in FOOT and t.get('indoor') == 'yes' and not below_ground(t): kinds.append('passage_up')
        if closed and not kinds:
            if 'w%d' % w['id'] in member_own and own_bld_kind(t): kinds.append('own_bld')
            elif t.get('highway') in ('footway', 'corridor', 'pedestrian') and below_ground(t) and 'area' not in t and 'area:highway' not in t:
                c = way_coords(w)
                if c: kinds = ring_kinds(c, t)
            else: kinds = [k for k in p2_kinds(t, True) if k == 'p2_named']
    if not kinds: continue
    c = way_coords(w)
    if not c: continue
    for k in kinds:
        g = Polygon(c) if closed and k not in ('passage', 'passage_up') else LineString(c)
        if not g.is_valid: g = g.buffer(0)
        if g.is_empty: continue
        feats.append((k, g, t, 'w%d' % w['id']))
        if k in ('passage', 'passage_up'): pass_ends[len(feats) - 1] = (w['nodes'][0], w['nodes'][-1])
for r in rels.values():
    t = r['tags']
    if t.get('type') not in ('multipolygon', 'building'): continue
    if r.get('p2'):
        ks = [k for k in p2_kinds(t, True) if k != 'passage_up']
    else:
        k = 'platform' if platform_kind(t) else 'station' if station_area_kind(t) else 'indoor' if indoor_area_kind(t) else \
            'station_up' if station_up_kind(t) else 'own_bld' if 'r%d' % r['id'] in member_own and own_bld_kind(t) else None
        ks = [k] if k else [k for k in p2_kinds(t, True) if k == 'p2_named']
    if not ks: continue
    g = rel_polygon(r)
    if g is None: continue
    for k in ks: feats.append((k, g, t, 'r%d' % r['id']))
print(collections.Counter(f[0] for f in feats), flush=True)
del ways   # the features are built: the raw ways are not needed again
tree = STRtree([f[1] for f in feats])
# stations whose own building stands on a bridge or an upper level: above ground, whatever their exits are tagged
up_station = {member_own[oid] for kind, g, t, oid in feats if kind in ('station_up', 'own_bld') and oid in member_own and (pos(t.get('layer')) or t.get('bridge') == 'yes')}

# ---------- exits ----------
EXIT_RE = [
    re.compile(r'(?:exit|ausgang|eingang|sortie|salida|uscita|saída|saida|wyjście|výstup|kijárat|выход|вход|porte|acceso|acesso|accès|entrada|ieșire|çıkış|uitgang|gate|puerta)\s*(?:no\.?|number|nr\.?|n°|#)?\s*([A-Za-z]?\d{0,2}[A-Za-z]?)\b', re.I),
    re.compile(r'([東西南北东]?[A-Za-z]?\d{1,2}[A-Za-z]?|[A-Za-z])\s*(?:号|號)?\s*(?:出入口|出口|入口|口|番出口|番出入口|번\s*출구)'),
    re.compile(r'(?:出口|出入口)\s*([A-Za-z]?\d{0,2}[A-Za-z]?)'),
]
REF_OK = re.compile(r'^[東西南北东]?[A-Za-z]{0,2}\d{0,2}[A-Za-z]?(?:（[東西南北东]）|\([NSEW]\))?$')
BARE_LABEL = re.compile(r'^(?:[A-Z]{1,2}\d{0,2}[a-z]?|\d{1,2}[A-Za-z]?)$')
RAILWAY_RE = re.compile(r'railway station|train station|railroad|火车站|高铁|客运站|鐵路|铁路', re.I)
LIFT_RE = re.compile(r'电梯|電梯|elevator|lift|ascenseur|엘리베이터|에스컬레이터|エレベーター|エスカレーター', re.I)
def _lab(m):
    """the code a label pattern caught, or '' when it caught a word instead ('Sortie de nuit' → de, 'Exit to Mall' → to)"""
    g = m.group(1) if m else ''
    if not g or (g.isalpha() and len(g) > 1 and not g.isupper()): return ''
    return g.upper() if len(g) <= 1 else g
COMPASS = {'northwest': 'NW', 'north-west': 'NW', 'north west': 'NW', 'northeast': 'NE', 'north-east': 'NE', 'north east': 'NE',
           'southwest': 'SW', 'south-west': 'SW', 'south west': 'SW', 'southeast': 'SE', 'south-east': 'SE', 'south east': 'SE',
           'north': 'N', 'south': 'S', 'east': 'E', 'west': 'W',
           'شمال غربی': 'NW', 'شمال شرقی': 'NE', 'جنوب غربی': 'SW', 'جنوب شرقی': 'SE', 'شمال': 'N', 'جنوب': 'S', 'شرق': 'E', 'شرقی': 'E', 'غرب': 'W', 'غربی': 'W',
           '东北': 'NE', '東北': 'NE', '东南': 'SE', '東南': 'SE', '西北': 'NW', '西南': 'SW', '东': 'E', '東': 'E', '西': 'W', '南': 'S', '北': 'N'}
def exit_label(t, snames=()):
    """the exit's letter or number: its ref, else one in its name (出口A, Exit 3, Gate No. 4, 汉中门#2, さっぽろ駅 20, a bare F)"""
    for key in ('ref', 'local_ref'):
        ref = (t.get(key) or '').strip()
        if not ref or LIFT_RE.search(ref): continue   # ref=엘리베이터 is the lift, not a code (Samgakji)
        ref2 = re.sub(r'^(出入口|出口|入口)|(番出入口|番出口|出入口|出口|口)$', '', ref)   # 'A3出口' and '出入口6' are exits A3 and 6; a bare 出口 is no label
        if not ref2: continue
        if re.search(r'[A-Za-z0-9]', ref2): ref = ref2
        if len(ref) <= 4 and ' ' not in ref: return ref
        if len(ref) <= 8 and REF_OK.match(ref): return re.sub(r'（.*?）|\(.*?\)', '', ref)   # 东1（北）: the 东1 exit's north stair
        for rx in EXIT_RE:
            lab = _lab(rx.search(ref))
            if lab: return lab
    for key in ('name', 'name:en', 'name:zh', 'name:ja', 'name:ko', 'description'):
        v = t.get(key) or ''
        for rx in EXIT_RE:
            lab = _lab(rx.search(v))
            if lab: return lab
    for key in ('name', 'name:zh', 'name:en'):
        v = (t.get(key) or '').strip()
        if not v: continue
        if BARE_LABEL.match(v) and v.lower() not in {(sn or '').lower() for sn in snames}: return v   # name=F, with no ref (not QT8's own name)
        m = re.search(r'#\s*([A-Za-z]?\d{1,2}[A-Za-z]?)\s*$', v)
        if m: return m.group(1)
        m = re.match(r'^\s*([A-Z]{1,2}\d{0,2}[a-z]?)\s*[:：]', v)   # 'H: BTM Layout 2nd stage' (Bengaluru)
        if m: return m.group(1)
        m = re.search(r'[（(]([A-Z]{0,2}-?\d{1,2}[a-z]?)[)）]\s*$', v)   # 'サンロード(S7)', 'メルサ(3)' (Nagoya)
        if m: return m.group(1)
        if LIFT_RE.search(v): continue
        for sn in snames:   # the code after the station's own name
            if not sn or sn.lower() not in v.lower(): continue
            rest = _NAME_DROP.sub('', re.sub(re.escape(sn), '', v, count=1, flags=re.I)).strip(' \t-–—:：#・·')
            if BARE_LABEL.match(rest) and not re.match(r'^[A-Z]{2}', rest): return rest   # 'Porta Susa A', not 'Porta Nuova FS' or 'Villa Fiorita MM2'
    # an exit named only by its compass point (Tehran's, Mashhad's, 东北出口)
    for key in ('name', 'name:en', 'name:fa', 'name:zh'):
        v = (t.get(key) or '').lower()
        v = re.sub(r'\b(exit|entrance|gate|ورودی|خروجی|درب|در)\b|出入口|出口|入口|口$', '', v).strip(' \t-–—:：·')
        if v in COMPASS: return COMPASS[v]
    return ''

exits = collections.defaultdict(list)       # station -> [(lon, lat, label, name, osm id)]
taken = set()
# an exit two stations' stop areas share (Houhai's lines 2 and 11 are two stations 300 m apart) goes to the nearer
claims = collections.defaultdict(list)
for i, ids in entrance_members.items():
    for n in ids: claims[n].append(i)
for n, cl in claims.items():
    o = nodes[n]; taken.add(n)
    own_cl = [j for j in cl if (j, n) in own_ent]   # a station whose own stop area lists the exit beats a nearer one
    d, i = min((min(km((o['lon'], o['lat']), (q[1], q[2])) for q in index[j]), j) for j in (own_cl or cl))
    if d > 0.6: continue   # a stop area member far from every point of the station (Shijiazhuang's, 415-620 m east)
    if (i, n) not in own_ent and d > 0.2: continue   # from a group's other stop area (Porta Venezia's Passante doors, 381 m): only near ones
    exits[i].append((o['lon'], o['lat'], exit_label(o['tags'], (st['name'][i], st['en'][i])), o['tags'].get('name', ''), n))
for o in nodes.values():
    if o['id'] in taken or o['id'] in group_skip: continue
    t = o['tags']; r = t.get('railway')
    if not (r in ('subway_entrance', 'train_station_entrance') or t.get('public_transport') == 'entrance'): continue
    # a subway entrance is the metro's whatever stop area lists it (Havre-Caumartin's exits sit in RER E's)
    if closed_exit(t) or (o['id'] in other_sa_nodes and r != 'subway_entrance'): continue
    if r == 'train_station_entrance' and not metro_mode(t) and t.get('entrance_marker:subway') != 'yes':
        # a door in a railway station's building (Lille-Europe's TGV hall: building=train_station, SNCF, in no metro
        # stop area) is the railway's
        P = Point(o['lon'], o['lat'])
        def rail_bld(k):
            kd, g, t2, oid = feats[k]
            if g.geom_type not in ('Polygon', 'MultiPolygon') or g.distance(P) >= 3e-5 or oid in member_own or metro_mode(t2) or t2.get('station') == 'subway': return False
            return t2.get('train') == 'yes' or oid in in_other_sa or (t2.get('building') == 'train_station' and not below_ground(t2))
        if any(rail_bld(k) for k in tree.query(P.buffer(3e-5))): continue
    lim = TRAIN_EXIT_KM if r == 'train_station_entrance' else EXIT_KM
    cand = near_stations((o['lon'], o['lat']), lim)
    if not cand: continue
    i = cand[0][1]
    exits[i].append((o['lon'], o['lat'], exit_label(t, (st['name'][i], st['en'][i])), t.get('name', ''), o['id']))

# exits mapped as entrance=* on a building or passage rather than as a railway entrance (ents.*.jsonl, from
# osm/ents.py): kept only when the node itself says it is a metro exit, is at street level, and is not already there
EXIT_WORDS = re.compile(r'(出入口|出口|地铁|地鐵|捷運|捷运|駅|출구|metro|subway|u-bahn|underground|mrt|lrt|métro|метро|exit\s*[a-z0-9]{1,3}\b)', re.I)
def metro_exit(t):
    if t.get('entrance') in ('no', 'garage', 'service', 'emergency', 'home', 'shop', 'private'): return False
    if t.get('access') in ('private', 'no') or t.get('disused') == 'yes' or neg(t.get('level', '')) or neg(t.get('layer', '')): return False
    if any(k in t for k in ('amenity', 'shop', 'tourism', 'office', 'healthcare', 'emergency', 'parking', 'building', 'addr:housenumber', 'craft', 'leisure', 'construction')): return False
    if any(t.get(k) == 'yes' for k in ('entrance_marker:subway', 'subway', 'light_rail', 'monorail')): return True
    return bool(EXIT_WORDS.search(' '.join(t.get(k, '') for k in ('name', 'name:en', 'name:zh', 'description'))))
n_extra = 0
for f in sorted(glob.glob(f'{OSM}/ents.*.jsonl')):
    for l in open(f, encoding='utf8'):
        o = json.loads(l); t = o['tags']
        if o['id'] in nodes or o['id'] in taken or o['id'] in other_sa_nodes or not metro_exit(t) or closed_exit(t): continue
        cand = near_stations((o['lon'], o['lat']), 0.2)
        if not cand: continue
        i = cand[0][1]
        if any(km((o['lon'], o['lat']), (e[0], e[1])) < 0.015 for e in exits[i]): continue
        exits[i].append((o['lon'], o['lat'], exit_label(t, (st['name'][i], st['en'][i])), t.get('name', ''), o['id'])); taken.add(o['id']); n_extra += 1
print(n_extra, 'exits mapped as entrance=*', flush=True)

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
    """line li's track within r metres of centre_xy, in loc's metres (its pieces joined again)"""
    c = loc.ll(centre_xy); dx = r / loc.kx; dy = r / loc.ky
    out = []
    for k in seg_tree.query(sbox(c[0] - dx, c[1] - dy, c[0] + dx, c[1] + dy)):
        if seg_line[k] != li: continue
        out.append(LineString(loc.geom(seg_geom[k].coords)))
    if not out: return None
    u = unary_union(out)
    if u.geom_type == 'MultiLineString':
        try: u = linemerge(u)
        except Exception: pass
    u = u.intersection(Point(centre_xy).buffer(r))
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

def end_station(i, li):
    """the station is the first or last stop of one of the line's routes: a track end there is a terminus, elsewhere a gap"""
    return any(r and (r[0] == i or r[-1] == i) for r in ROUTES[li])

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
    """direction of the track at the point nearest pt: (degrees, that point, its distance from pt, end), where end is
    +1 or -1 when the track ends there (a terminus, or a gap in the line's geometry), in or against the direction"""
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
    deg = math.degrees(math.atan2(b.y - a.y, b.x - a.x)) % 180
    end = 0
    if s < 10 or g.length - s < 10:
        far = g.length - s < 10
        e = g.interpolate(g.length if far else 0); inner = a if far else b
        ux, uy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        sgn = 1 if (e.x - inner.x) * ux + (e.y - inner.y) * uy > 0 else -1
        if track.distance(Point(e.x + 30 * sgn * ux, e.y + 30 * sgn * uy)) > 25: end = sgn
    return deg, nearest_points(g, pt)[0], best[0], end

def extend_track(tr, m):
    """the track with each end carried straight on for m metres: tail tracks past a terminus are not in the line's
    geometry, and the station's exits can lie beyond its end"""
    parts = []
    for g in (tr.geoms if hasattr(tr, 'geoms') else [tr]):
        if g.geom_type != 'LineString' or len(g.coords) < 2: continue
        c = list(g.coords)
        def ext(p, q):
            d = math.dist(p, q) or 1
            return (p[0] + (p[0] - q[0]) / d * m, p[1] + (p[1] - q[1]) / d * m)
        parts.append(LineString([ext(c[0], c[1])] + c + [ext(c[-1], c[-2])]))
    return unary_union(parts) if parts else tr

def box_frame(b):
    """a box's centre, direction, half-length and half-width"""
    mrr = b.minimum_rotated_rectangle
    if mrr.geom_type != 'Polygon': return None
    q = list(mrr.exterior.coords); e1 = math.dist(q[0], q[1]); e2 = math.dist(q[1], q[2])
    p0, p1 = (q[0], q[1]) if e1 >= e2 else (q[1], q[2])
    return mrr.centroid.x, mrr.centroid.y, math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0])) % 180, max(e1, e2) / 2, min(e1, e2) / 2

_sys_cars = collections.defaultdict(list)
for _l in lines_csv.values():
    _n = num(_l.get('cars_per_train', ''))
    if _n: _sys_cars[_l.get('system_id')].append(_n)
def box_len(lid, under=None):
    """length of an approximate station box: the line's train, plus stairs and plant rooms. A line with no car count
    takes its system's usual one (two cars for a VAL or people mover), six only when the system has none"""
    l = lines_csv.get(lid, {})
    ct = (l.get('car_type') or '').lower()
    cars = num(l.get('cars_per_train', ''))
    if not cars:
        if re.search(r'\bval\b|\bagt\b|people mover|\bapm\b|maggaly|neoval|cityval', ct): cars = 2
        else:
            cs = sorted(_sys_cars.get(l.get('system_id'), []))
            cars = cs[len(cs) // 2] if cs else 6
    per = TYRE_CAR_M if 'rubber' in ct else CAR_M
    if under is None:
        try: under = float(l.get('tunnel_share_osm') or 0) >= 0.5
        except ValueError: under = False
    return min(max(cars * per + (60 if under else 20), 80), 300)

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

def plat_local(g):
    """a platform in metres around its own centroid: (Local, geometry) or None"""
    c = g.centroid; p = (c.x, c.y); loc = Local(*p)
    gx = Polygon(loc.geom(g.exterior.coords)) if g.geom_type == 'Polygon' else \
        LineString(loc.geom(g.coords)) if g.geom_type == 'LineString' else None
    if gx is None:
        gx = unary_union([Polygon(loc.geom(x.exterior.coords)) for x in getattr(g, 'geoms', []) if x.geom_type == 'Polygon'])
    return None if gx.is_empty else (loc, gx)

# platforms: each to the (station, line) whose track it runs along
plat_ids = [k for k, f in enumerate(feats) if f[0] == 'platform']
plat_to = collections.defaultdict(list)       # (station, line) -> [feature index]
plat_shared = collections.defaultdict(list)   # (station, line) -> platforms of another line on the same track
unassigned = []
for k in plat_ids:
    kind, g, t, oid = feats[k]
    c = g.centroid; p = (c.x, c.y)
    cand = near_stations(p, PLATFORM_KM)
    owner = member_station.get(oid)
    if owner is None and oid in in_other_sa: continue
    if owner is not None and all(i != owner for _, i in cand): cand.append((0, owner))
    if not cand: continue
    pl = plat_local(g)
    if not pl: continue
    loc, gx = pl
    ad = axis_deg(gx)
    best = None; cands = []
    for d, i in cand:
        for li, _ in st['lines'][i]:
            if tram_only(t) and li not in TRAM_LINE: continue
            tr = track_near(li, loc, (0, 0), 500)
            if tr is None: continue
            dist = tr.distance(gx)
            if dist > TRACK_M: continue
            tg = tangent_deg(tr, gx.centroid)
            da = angdiff(tg[0], ad) if tg else 0
            if da > ANGLE and gx.length > 30: continue
            # near ties go to the line the platform runs along, not the first in the station's list; the stop-area
            # bonus only for the station's own stop area, not a group's (PATH's 14 St platforms are not the M's)
            score = dist + 20 * d + 0.3 * da - (15 if member_own.get(oid) == i else 0)
            cands.append((score, i, li, dist))
            if best is None or score < best[0]: best = (score, i, li, dist)
    if best:
        plat_to[(best[1], best[2])].append(k)
        # other lines of the same station on the same track (Oslo's trunk, the Metropolitan and the Circle) share the
        # platform, but only where they have no platforms of their own (see below)
        for sc_, i2, li2, d2 in cands:
            if i2 == best[1] and li2 != best[2] and d2 <= best[3] + 5: plat_shared[(i2, li2)].append(k)
    elif owner is not None and member_own.get(oid) == owner: unassigned.append((k, owner, loc, gx, ad))
n_shared = 0
for key, ks in plat_shared.items():
    if key not in plat_to: plat_to[key] = list(ks); n_shared += 1
print(n_shared, 'lines share another line\'s platforms', flush=True)
# a platform of the station's own stop area that lies further from the track than TRACK_M (split tracks, side
# platforms wide apart: Chengdu's Taipingyuan line 5) still goes to the line it runs parallel to
n_own = 0
for k, owner, loc, gx, ad in unassigned:
    kind, g, t, oid = feats[k]
    best = None
    for li, _ in st['lines'][owner]:
        if tram_only(t) and li not in TRAM_LINE: continue
        tr = track_near(li, loc, (0, 0), 500)
        if tr is None: continue
        dist = tr.distance(gx)
        if dist > OWN_TRACK_M: continue
        tg = tangent_deg(tr, gx.centroid)
        if tg and angdiff(tg[0], ad) > OWN_ANGLE: continue
        if best is None or dist < best[0]: best = (dist, li)
    if best: plat_to[(owner, best[1])].append(k); n_own += 1
print(n_own, 'platforms of their own stop area matched off the track', flush=True)

# one line's platforms at a station are tagged alike: where some are tagged subway / light_rail, untagged ones beside
# them that are a railway's (train=yes) or on another level are another railway's (Châtelet's RER platforms lie under
# line 14's), and they share one level
def plat_level(k): return feats[k][2].get('level') or feats[k][2].get('layer') or ''
for key, ks in list(plat_to.items()):
    tagged = [k for k in ks if metro_mode(feats[k][2])]
    if tagged and len(tagged) < len(ks):
        lv_t = {plat_level(k) for k in tagged}
        ks = [k for k in ks if k in tagged or (feats[k][2].get('train') != 'yes' and plat_level(k) in lv_t)]
    lv = collections.Counter(plat_level(k) for k in ks)
    if len(lv) > 1:
        top = lv.most_common(1)[0][0]
        ks = [k for k in ks if plat_level(k) == top]
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
    # seeds along each box's long axis (its track), so the cut between two parallel boxes is one straight line midway
    seeds, labs, have = [], [], set()
    for lab, b in labelled:
        mrr = b.minimum_rotated_rectangle
        c = list(mrr.exterior.coords) if mrr.geom_type == 'Polygon' else []
        if len(c) >= 5:
            m01 = ((c[0][0] + c[1][0]) / 2, (c[0][1] + c[1][1]) / 2); m23 = ((c[2][0] + c[3][0]) / 2, (c[2][1] + c[3][1]) / 2)
            m12 = ((c[1][0] + c[2][0]) / 2, (c[1][1] + c[2][1]) / 2); m30 = ((c[3][0] + c[0][0]) / 2, (c[3][1] + c[0][1]) / 2)
            axis = LineString([m01, m23]) if math.dist(c[0], c[1]) < math.dist(c[1], c[2]) else LineString([m12, m30])
        else:
            axis = LineString([b.centroid.coords[0], (b.centroid.x + 0.1, b.centroid.y)])
        n = max(2, int(axis.length / 4) + 1)
        for k in range(n):
            q = axis.interpolate(k / (n - 1), normalized=True)
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

def stop_centre(i, li, tr, loc, cx, cy):
    """where line li really stops at station i: the mean of its own stop area's stop positions on its track. At an
    interchange the station's point is often one node shared by every line, which can sit far from where a line's
    trains stop (Chengdu's Nijiaqiao line 8 stops 177 m from it)."""
    if tr is None: return None
    pts = []; up = False
    tre = extend_track(tr, MAX_HALF_M)   # a stop just past the end of the line's geometry still counts (Macau's Union Hospital)
    for r in index[i]:
        if r[0] != li or not r[3].startswith('sa'): continue
        rel = rels.get(int(r[3][2:]))
        if not rel: continue
        for t, ref, role in rel['members']:
            if t != 'n': continue
            nt = nodes.get(ref, {}).get('tags', {})
            if not (role.startswith('stop') or nt.get('public_transport') == 'stop_position' or nt.get('railway') == 'stop'): continue
            if nt.get('train') == 'yes' and not metro_mode(nt): continue
            p = node_xy(ref)
            if p is None: continue
            q = loc.xy(p)
            if math.hypot(q[0] - cx, q[1] - cy) > STOP_SHIFT_M or tre.distance(Point(q)) > 15: continue
            pts.append(q); up = up or pos(nt.get('level')) or pos(nt.get('layer'))
    if not pts: return None
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts), up

cover = []
total = collections.Counter()
DEBUG_ST = int(os.environ.get('DEBUG_STATION', '-1'))   # DEBUG_STATION=9611 prints that station's hall candidates
ONLY = set(os.environ.get('ONLY', '').split(',')) - {''}   # ONLY=cn-shenzhen-metro,... rebuilds just those systems
for si, sysrow in enumerate(S):
    if ONLY and sysrow[0] not in ONLY: continue
    out = {'v': 2, 'boxes': [], 'areas': [], 'paths': [], 'exits': []}
    sys_boxes = {}                                   # (station, line) -> lon/lat box polygon
    area_claims = collections.defaultdict(set)       # OpenStreetMap id -> stations it belongs to
    area_geom = {}                                   # feature -> the part of it drawn (a hub larger than AREA_MAX_M2)
    path_claims = collections.defaultdict(set)
    schematic = set()                                # passages drawn dashed: straight transfer links between station nodes
    claim_log = []                                   # every hall taken, with why (OUT/_claims/<system>.json, for review)
    stat = {}
    for i in stations_by_sys[si]:
        loc = Local(float(lon[i]), float(lat[i]))
        rows = index[i]
        boxes_xy = []; box_cols = []; box_line = []; box_approx = []; approx_par = {}
        n_mapped = n_approx = 0
        exs = exits.get(i, [])
        ex_xy = [loc.xy((x, y)) for x, y, *_ in exs]
        # where each line stops: its track, and its own stop positions (at an interchange the station's point is one
        # node shared by every line, which can sit far from where a line's trains stop)
        cen = {}; trx = {}
        for li, _y in st['lines'][i]:
            pts = [loc.xy((r[1], r[2])) for r in rows if r[0] == li] or [(0.0, 0.0)]
            cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
            tr = track_near(li, loc, (cx, cy), 600)
            sc = stop_centre(i, li, tr, loc, cx, cy)
            up = False
            if sc: cx, cy, up = sc
            tg = tangent_deg(tr, Point(cx, cy)) if tr is not None else None
            if tg and tg[3] and tg[2] > 20:
                # the line's geometry stops short of the station: carry it on through the station rather than lay the
                # box backwards from the gap
                tr = extend_track(tr, MAX_HALF_M); tg = tangent_deg(tr, Point(cx, cy))
            if tg and tg[3] and sc is not None and tg[2] <= 15:
                # the geometry ends at the line's own stop positions (Bengaluru's RV Road yellow line): the platform is
                # centred there, not behind the end
                tg = (tg[0], tg[1], tg[2], 0)
            cen[li] = (cx, cy, tr, sc is not None, tg, up)
            if tr is not None: trx[li] = extend_track(tr, MAX_HALF_M)
        # each exit goes with the line whose own stop area lists it, else the line it lies along: nearest track within
        # EXIT_LATERAL_M, counting distance along the track beyond the box too, so an exit by one line's platform does
        # not stretch the other line's box across it
        ex_line = [None] * len(ex_xy)
        for n_, (p_, e_) in enumerate(zip(ex_xy, exs)):
            li_ = ent_line.get((i, e_[4]))
            if li_ is not None and li_ in trx: ex_line[n_] = li_; continue
            best = None
            for li, (cx, cy, tr, _, tg, _) in cen.items():
                if li not in trx: continue
                lat_ = trx[li].distance(Point(p_))
                if lat_ > EXIT_LATERAL_M: continue
                along = abs((p_[0] - cx) * math.cos(math.radians(tg[0])) + (p_[1] - cy) * math.sin(math.radians(tg[0]))) if tg else 0
                sc_ = lat_ + 0.5 * max(0, along - box_len(L[li][0]) / 2)
                if best is None or sc_ < best[0]: best = (sc_, li)
            if best: ex_line[n_] = best[1]
        # the mapped passages about the station (claimed further down): an exit one of them reaches stretches no box
        near_pass = []
        pass_r = max(250, min(400, max((math.hypot(*p_) for p_ in ex_xy), default=0) + 30))   # out to the farthest exit
        for k in tree.query(Point(loc.ll((0, 0))).buffer(0.0045)):
            kind, g, t, oid = feats[k]
            if kind in ('passage', 'passage_up') and g.geom_type == 'LineString':
                gx = from_ll(loc, g)
                if gx.distance(Point(0, 0)) <= pass_r: near_pass.append((k, kind, gx))
        # an exit counts as reached only by a run of passages that gets to the line's track (Grands Boulevards' exits 5
        # and 6 sit at the end of a passage stub 150 m from anything else of the station)
        pu_ = unary_union([gx.buffer(2) for _, kd, gx in near_pass if kd == 'passage']) if any(kd == 'passage' for _, kd, _ in near_pass) else None
        comps = list(pu_.geoms) if pu_ is not None and pu_.geom_type == 'MultiPolygon' else [pu_] if pu_ is not None else []
        ex_reached = []
        for p_ in ex_xy:
            P_ = Point(p_); ok = False
            for cp in comps:
                if cp.distance(P_) < 10:
                    ok = any(cp.distance(tx) < 25 for tx in trx.values()); break
            ex_reached.append(ok)
        # underground, unless its own building or stops are above ground: a station whose exits are subway entrances,
        # whatever share of its line runs in tunnel
        under_i = False if i in up_station else True if any((nodes.get(e[4]) or {}).get('tags', {}).get('railway') == 'subway_entrance' for e in exs) else None
        def approx_box(li, cx, cy, deg, length, end=0):
            ux, uy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
            lim = min(MAX_HALF_M, length / 2 + STRETCH_EXTRA_M)
            along = [(p_[0] - cx) * ux + (p_[1] - cy) * uy for p_, l_, r_ in zip(ex_xy, ex_line, ex_reached) if l_ == li and not r_]
            along = [a for a in along if abs(a) <= lim]
            if along:
                # the box reaches the line's exits, keeps the stops inside its middle, and is at least the train's length
                lo, hi = min(along) + EXIT_INSET_M, max(along) - EXIT_INSET_M
                a0, a1 = min(lo, -0.3 * length), max(hi, 0.3 * length)
                if a1 - a0 < length:
                    c = max(-0.3 * length, min(0.3 * length, (a0 + a1) / 2)); a0, a1 = c - length / 2, c + length / 2
            elif end:   # the track ends here: the box lies along the track, not half past its end
                a0, a1 = (-(length - TERM_END_M), TERM_END_M) if end > 0 else (-TERM_END_M, length - TERM_END_M)
            else:
                a0, a1 = -length / 2, length / 2
            # at a terminus the box stops just past the end of the track, unless exits show the station going on
            if end > 0 and not any(a > TERM_END_M for a in along): a1 = min(a1, TERM_END_M); a0 = min(a0, a1 - length)
            if end < 0 and not any(a < -TERM_END_M for a in along): a0 = max(a0, -TERM_END_M); a1 = max(a1, a0 + length)
            mid = (a0 + a1) / 2
            approx_par[li] = (cx + mid * ux, cy + mid * uy, deg, a1 - a0)
            return rect(cx + mid * ux, cy + mid * uy, deg, a1 - a0, BOX_W)
        for li, _y in st['lines'][i]:
            lid = L[li][0]
            cx, cy, tr, has_sc, tg0, up = cen[li]
            under_li = False if up else under_i
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
                # the frame is the track beside the platforms (not at the station's point, which on a curve can be
                # off to the side of them: Châtelet's line 4)
                pc = pu.centroid
                anchor = pc if math.hypot(pc.x - cx, pc.y - cy) <= 250 else Point(cx, cy)
                tg = tangent_deg(tr, anchor) if tr is not None else None
                if tg and tg[2] <= 250:
                    # a rectangle along the track: as long as the platforms beside it, at most BOX_HALF_W either side
                    # (wider when the platforms themselves lie further out, up to 40 m), and never over MAX_BOX_M
                    o = tg[1]
                    rot = affinity.rotate(affinity.translate(pu, -o.x, -o.y), -tg[0], origin=(0, 0))
                    half = MAX_BOX_M / 2 - 3
                    wide = BOX_HALF_W
                    near = rot.intersection(sbox(-half, -45, half, 45))
                    if not near.is_empty:
                        _, ny0, _, ny1 = near.bounds
                        if ny1 - ny0 <= 45: wide = min(40, max(BOX_HALF_W, max(-ny0, ny1) + 2))
                    rot = rot.intersection(sbox(-half, -wide, half, wide))
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
            if got is None and tg0:
                # on the line's track, at its stops (else at the track point nearest the station's point, however far:
                # a box laid off the track at the shared node would be worse)
                got = (approx_box(li, tg0[1].x, tg0[1].y, tg0[0], box_len(lid, under_li), tg0[3] if end_station(i, li) else 0), 1)
            if got is None and tr is None:
                # no track near: lay the box between the station's neighbours on the line
                deg = route_deg(i, li, loc)
                if deg is not None:
                    got = (approx_box(li, cx, cy, deg, box_len(lid, under_li)), 1)
            if got is None: continue
            # lines that share a platform and a colour (New York's 1, 2 and 3) get one box
            col = (L[li][5] or '').lower()
            dup = next((j for j, (c2, b2) in enumerate(box_cols) if col and c2 == col and got[0].intersection(b2).area > 0.6 * min(got[0].area, b2.area)), None)
            if dup is not None:
                # a mapped box replaces an earlier approximate one of the same colour (Columbus Circle's C under the A's guess)
                if got[1] or not box_approx[dup]: continue
                box_cols[dup] = (col, got[0]); boxes_xy[dup] = got[0]; box_approx[dup] = 0
                continue
            box_cols.append((col, got[0]))
            boxes_xy.append(got[0]); box_line.append(li); box_approx.append(got[1])
        # lines of different colours that share one track or platform (Rio's 1 and 2, the Metropolitan and the Circle)
        # would get one box over another: they get one box striped lengthwise, a stripe a line
        groups = []
        for a in range(len(boxes_xy)):
            for b in range(a):
                if boxes_xy[a].intersection(boxes_xy[b]).area <= 0.6 * min(boxes_xy[a].area, boxes_xy[b].area): continue
                ga = next((g for g in groups if a in g), None); gb = next((g for g in groups if b in g), None)
                if ga and gb and ga is not gb: ga |= gb; groups.remove(gb)
                elif ga: ga.add(b)
                elif gb: gb.add(a)
                else: groups.append({a, b})
        for g in groups:
            mem = sorted(g, key=lambda k: (box_approx[k], -boxes_xy[k].area))   # the frame from a mapped box, not a guess
            mrr = boxes_xy[mem[0]].minimum_rotated_rectangle
            if mrr.geom_type != 'Polygon': continue
            q = list(mrr.exterior.coords); e1 = math.dist(q[0], q[1]); e2 = math.dist(q[1], q[2])
            length, width = max(e1, e2), min(e1, e2)
            p0, p1 = (q[0], q[1]) if e1 >= e2 else (q[1], q[2])
            deg = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0])) % 180
            fx, fy = mrr.centroid.x, mrr.centroid.y
            n = len(mem); w = width / n
            ux, uy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
            for k, m in enumerate(mem):
                off = (k - (n - 1) / 2) * w
                boxes_xy[m] = rect(fx - off * uy, fy + off * ux, deg, length, w)
        for b, li, ap in zip(boxes_xy, box_line, box_approx):
            if ap: n_approx += 1
            else: n_mapped += 1
            sys_boxes[(i, li)] = to_ll_poly(loc, b)
            for ring in ring_ll(loc, b, 0.3):
                out['boxes'].append([i, li, ap, [[round(x * 1e6), round(y * 1e6)] for x, y in ring]])
        # concourses and halls that belong to it: its stop area's, its own or same-named buildings, or ones touching its boxes
        allbox = unary_union(boxes_xy) if boxes_xy else Point(0, 0).buffer(20)
        reach = allbox.buffer(60)
        names_i = {norm_name(st['name'][i]), norm_name(st['en'][i])} - {''}
        rail_named_i = bool(RAILWAY_RE.search(st['en'][i] or '') or RAILWAY_RE.search(st['name'][i] or ''))
        ex_pts = [Point(p_) for p_ in ex_xy]
        ex_u = unary_union([p.buffer(15) for p in ex_pts]) if ex_pts else None
        halls = []
        for k in tree.query(Point(loc.ll((0, 0))).buffer(0.004)):
            kind, g, t, oid = feats[k]
            if kind not in ('station', 'station_up', 'indoor', 'p2_named', 'under_bld', 'own_bld') or g.geom_type not in ('Polygon', 'MultiPolygon'): continue
            if unbuilt(t) or (kind != 'indoor' and busy(t)): continue
            gx = shapely.make_valid(from_ll(loc, g)).buffer(0)
            if gx.is_empty: continue
            mine = member_station.get(oid) == i; own_ = member_own.get(oid) == i
            if DEBUG_ST == i: print('hall?', kind, oid, 'own', member_own.get(oid), 'mine', member_station.get(oid), round(gx.area), 'rail_own' if i in rail_own else '', {x: t.get(x) for x in ('building', 'train', 'name')}, flush=True)
            # a railway's hall or platforms (Gare Montparnasse, Metro-North's platforms under Grand Central) are not the metro's
            if t.get('train') == 'yes' and not metro_mode(t) and not (own_ and i not in rail_own): continue
            # a stop area group's railway station (Gare Saint-Lazare, SNCF's) is not the metro's hall either
            if kind == 'station' and mine and not own_ and (RAIL_OP_RE.search(' '.join(t.get(x, '') for x in ('operator', 'network'))) or gx.area > NEAR_AREA_M2): continue
            # a shop, a room or a car-park level beside the boxes (Saint-Lazare's Sephora, 'Parking -3') is not a hall
            if kind == 'indoor' and not own_ and ('shop' in t or 'parking' in t or t.get('indoor') == 'room' or t.get('amenity') in ('parking', 'bicycle_parking', 'cafe', 'restaurant', 'fast_food', 'bank', 'pharmacy', 'toilets')): continue
            # a station hall named after the station (Gangxia North's 岗厦北站, mapped underground but in no stop area)
            named = kind != 'indoor' and same_name(t, names_i) and t.get('train') != 'yes' and not weak_station(t)
            # another operator's building (Sants Estació's mainline hall, in RENFE's stop area) is not ours, whatever its name
            if not own_ and oid in in_other_sa and (kind in ('station_up', 'p2_named') or named): continue
            if not own_ and t.get('station') in ('train', 'tram', 'monorail') and not metro_mode(t): continue
            why = kind
            if kind == 'p2_named':
                if not named: continue
                kind = 'station' if below_ground(t) else 'station_up'; why = 'named building (second pass)'
            if kind in ('own_bld', 'station_up') and gx.area < 150: continue   # an entrance canopy, not a hall (Kyoto's 28 m2 'stations')
            if kind == 'own_bld':
                if not own_ or gx.area > NEAR_AREA_M2 or not (gx.intersects(reach) or gx.distance(Point(0, 0)) < 80): continue
                why = 'own stop area building'
            elif gx.area > AREA_MAX_M2:
                # an integrated hub (Futian's 135,000 m2 holds the high-speed hall too): only the part about the metro's boxes
                if kind != 'station' or not (own_ or named): continue
                part = gx.intersection(allbox.buffer(80))
                if part.is_empty or not 2000 <= part.area <= 2 * NEAR_AREA_M2: continue
                area_geom[k] = to_ll_poly(loc, part); gx = part; why = 'hub clipped to the boxes'
            elif kind == 'under_bld':
                # a building below ground, with no station tag or name: only one the boxes run through
                if gx.area > NEAR_AREA_M2 or not gx.intersects(allbox) or gx.distance(Point(0, 0)) > 150: continue
                why = 'underground building on the boxes'
            elif kind == 'station_up':
                # above ground, only the station's own building (Wimbledon's), and only a small one: never a mainline
                # terminus, which a stop area group brings in beside the station (Cannon Street's, Charing Cross's), nor
                # the railway station a metro station is named after (南京站's north building) unless it is the metro's own
                if t.get('train') == 'yes' and not metro_mode(t) and not (own_ and i not in rail_own): continue   # Cawang's LRT building says train=yes
                cap = NEAR_AREA_M2 if (own_ and named) else UP_HALL_M2
                if gx.area > cap or not (own_ or (named and not rail_named_i and gx.distance(Point(0, 0)) < 80)): continue
                why = 'own station building' if own_ else 'named station building'
                fr_ = box_frame(gx)
                if own_ and fr_ and boxes_xy and fr_[3] * 2 > max(250, 1.5 * max(box_frame(b)[3] * 2 for b in boxes_xy if box_frame(b))):
                    # a mainline gallery the metro's stop area lists (Torino Porta Susa, 385 m): only the part about the boxes
                    part = gx.intersection(allbox.buffer(60))
                    if part.is_empty or part.area < 300: continue
                    area_geom[k] = to_ll_poly(loc, part); gx = part; why = 'own station building clipped to the boxes'
            elif named and not mine:
                why = 'named hall'
                if gx.area > NEAR_AREA_M2:
                    if kind != 'station' or not gx.intersects(allbox.buffer(30)): continue
                elif not (gx.distance(Point(0, 0)) < 150 or gx.intersects(allbox.buffer(30))): continue
            elif not mine:
                why = 'near the boxes'
                if gx.area > NEAR_AREA_M2: continue
                if kind == 'indoor':
                    # an underground pedestrian area is the station's only when it meets its boxes or exits
                    if not (gx.intersects(allbox.buffer(20)) or (ex_u is not None and gx.intersects(ex_u))): continue
                elif not gx.intersects(reach) or not (gx.distance(Point(0, 0)) < 80 or gx.intersects(allbox)): continue
            area_claims[k].add(i); halls.append(gx)
            if DEBUG_ST == i: print('hall!', oid, why, flush=True)
            if why in ('station', 'station_up', 'indoor'): why = ('own stop area ' if own_ else 'stop area group ') + why
            claim_log.append({'station': i, 'name': st['en'][i] or st['name'][i], 'osm': oid, 'kind': kind, 'why': why, 'm2': round(gx.area),
                              'dist_m': round(gx.distance(Point(0, 0))), 'tags': {x: v for x, v in t.items() if x in ('name', 'name:en', 'building', 'public_transport', 'railway', 'station', 'train', 'subway', 'layer', 'level', 'location', 'indoor', 'highway', 'operator', 'network')}})
        halls_u = unary_union(halls) if halls else None
        # exits
        seen = set(); by_lab = collections.defaultdict(list)
        for (x, y, lab, name, oid), p_ in zip(exs, ex_xy):
            key = (round(x, 5), round(y, 5))
            if key in seen: continue
            # the same exit mapped twice (Havre-Caumartin's 1 to 5 in the metro's and RER E's stop areas): once
            if lab and any(math.dist(p_, q_) < 15 for q_ in by_lab[lab]): continue
            seen.add(key); by_lab[lab].append(p_)
            out['exits'].append([i, round(x * 1e6), round(y * 1e6), lab, name])
        # passages that lead to it (to a box, a hall or an exit): underground ones, and above ground only covered or
        # indoor walkways inside its halls, at its exits or along its track (an elevated station's concourse)
        targets = [allbox.buffer(30)] + [p.buffer(20) for p in ex_pts]
        if halls_u is not None: targets.append(halls_u.buffer(15))
        tu = unary_union(targets)
        ex_touch = unary_union([p.buffer(3) for p in ex_pts]) if ex_pts else None
        tr_list = [c_[2] for c_ in cen.values() if c_[2] is not None]
        tr_u = unary_union(tr_list).buffer(30) if tr_list else None
        claimed, pending = [], []
        for k, kind, gx in near_pass:
            if kind == 'passage_up':
                ok = (halls_u is not None and gx.intersects(halls_u)) or (ex_touch is not None and gx.intersects(ex_touch)) or \
                    (tr_u is not None and gx.distance(Point(0, 0)) <= 150 and gx.intersection(tr_u).length >= 0.7 * gx.length)
            else:
                ok = gx.intersects(tu)
            if ok:
                path_claims[k].add(i); claimed.append(gx)
                ends = pass_ends.get(k)
                if ends and ends[0] in station_nodes[i] and ends[1] in station_nodes[i]: schematic.add(k)
            elif kind == 'passage': pending.append((k, gx))
        # passages that only join other passages of the station (a corridor between two concourses), a few steps out
        added = 0
        for _ in range(3):
            if not pending or added > 600: break
            cu = unary_union(claimed) if claimed else None
            if cu is None: break
            more = []
            for k, gx in pending:
                if gx.distance(cu) <= 3: path_claims[k].add(i); claimed.append(gx); added += gx.length
                else: more.append((k, gx))
            if len(more) == len(pending): break
            pending = more
        # an exit no mapped passage reaches gets an estimated one, straight to the nearest box or hall, in the colour of
        # the box it reaches (drawn dashed, as approximate): Chengdu South's exits then join its boxes, as on Baidu
        n_conn = 0
        body = unary_union([allbox] + halls)
        my_paths = claimed
        def box_of(q):
            return min(zip(boxes_xy, box_line), key=lambda bl: bl[0].distance(q))[1] if boxes_xy else st['lines'][i][0][0]
        def connector(p_, q):
            out['paths'].append([i, box_of(q), [[round(x * 1e6), round(y * 1e6)] for x, y in (loc.ll((p_.x, p_.y)), loc.ll((q.x, q.y)))], 1])
        done = set()
        box_by_line = {li: b for b, li in zip(boxes_xy, box_line)}
        for n_, p_ in enumerate(ex_xy):
            key = (round(p_[0]), round(p_[1]))
            if key in done: continue
            done.add(key)
            P = Point(p_)
            d = body.distance(P)
            if d < 6 or any(g_.distance(P) < 12 for g_ in my_paths): continue
            if any(kd == 'passage' and gx_.distance(P) < 20 for _, kd, gx_ in near_pass): continue   # reached through a mapped corridor, if another station's
            li_ = ex_line[n_]
            fr = box_frame(box_by_line[li_]) if li_ in box_by_line else None
            if fr:
                # an exit along the line beyond the box end (a long passage or an underground street): the estimated
                # passage runs along the track from the box end, then across to the exit
                fx, fy, deg, half, hw = fr
                ux, uy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
                a_e = (P.x - fx) * ux + (P.y - fy) * uy; l_e = -(P.x - fx) * uy + (P.y - fy) * ux
                if abs(a_e) > half + 6 and abs(l_e) <= EXIT_LATERAL_M and abs(a_e) - half + abs(l_e) <= 400:
                    s_ = 1 if a_e > 0 else -1
                    pts_ = [(fx + s_ * half * ux, fy + s_ * half * uy), (fx + a_e * ux, fy + a_e * uy), (P.x, P.y)]
                    out['paths'].append([i, li_, [[round(x * 1e6), round(y * 1e6)] for x, y in (loc.ll(q) for q in pts_)], 1]); n_conn += 1
                    continue
            if d > (CONNECT_FAR_M if li_ is not None else CONNECT_MAX_M): continue
            connector(P, nearest_points(body, P)[0]); n_conn += 1
        # the parts of the station nothing joins (two lines' boxes with no hall or passage mapped between them) are
        # joined the same way, nearest part to nearest part, up to LINK_MAX_M
        parts = sorted(body.geoms, key=lambda p: -p.area) if body.geom_type == 'MultiPolygon' else []
        linked, rest = parts[:1], parts[1:]
        while rest:
            d, p, q = min(((p.distance(q), p, q) for p in rest for q in linked), key=lambda t: t[0])   # ties must not compare polygons
            if d > LINK_MAX_M: break
            a_, b_ = nearest_points(p, q)
            mid_ = Point((a_.x + b_.x) / 2, (a_.y + b_.y) / 2)
            # over 100 m, only where an exit or an underground passage of the station lies along the link (Kuramae's two
            # lines, 199 m apart with a street between them, stay two parts)
            if d > 100 and not (any(e_.distance(mid_) < 40 for e_ in ex_pts) or any(kd == 'passage' and gx_.distance(mid_) < 40 for _, kd, gx_ in near_pass)):
                linked.append(p); rest.remove(p); continue
            if not any(g_.distance(p) < 12 and g_.distance(q) < 12 for g_ in my_paths): connector(a_, b_); n_conn += 1
            linked.append(p); rest.remove(p)
        stat[i] = [n_mapped, n_approx, len(seen), n_conn]

    # halls: each OpenStreetMap area once, cut among the boxes of the stations it belongs to (and any other box it
    # covers), each piece in its line's colour; overlapping halls of one line are merged
    pieces = collections.defaultdict(list)
    box_tree_keys = list(sys_boxes)
    box_tree = STRtree([sys_boxes[k] for k in box_tree_keys]) if box_tree_keys else None
    for k, cl in area_claims.items():
        g = area_geom.get(k, feats[k][1]); c = g.centroid; loc = Local(c.x, c.y)
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
            out['paths'].append([i, li, [[round(x * 1e6), round(y * 1e6)] for x, y in c]] + ([1] if k in schematic else []))
    for i in stations_by_sys[si]:
        nm = st['en'][i] or st['name'][i]
        n_mapped, n_approx, n_exits, n_conn = stat[i]
        cover.append({'system_id': sysrow[0], 'city': sysrow[2], 'station': nm, 'lines': len(st['lines'][i]),
                      'boxes_mapped': n_mapped, 'boxes_approx': n_approx, 'exits': n_exits, 'est_passages': n_conn,
                      'exits_labelled': sum(1 for e in out['exits'] if e[0] == i and e[3]), 'areas': n_areas[i]})
    for k in ('boxes', 'areas', 'paths', 'exits'): total[k] += len(out[k])
    json.dump(out, open(f'{OUT}/{sysrow[0]}.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    os.makedirs(f'{OUT}/_claims', exist_ok=True)
    json.dump(claim_log, open(f'{OUT}/_claims/{sysrow[0]}.json', 'w', encoding='utf8'), ensure_ascii=False)
with open(COVER, 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=list(cover[0].keys())); w.writeheader(); w.writerows(cover)
print(dict(total), len(cover), 'stations')
