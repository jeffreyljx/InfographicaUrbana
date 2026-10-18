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
import datetime, hashlib, time
BUILD_ID = hashlib.sha1(open(__file__, 'rb').read()).hexdigest()[:12]   # names this builder in its output, so stale files can be told apart
EXIT_KM = 0.35        # an exit belongs to the nearest station within this distance (stop area members always count)
TRAIN_EXIT_KM = 0.15  # railway=train_station_entrance is often a mainline station's: only near ones count
OWN_EXIT_KM = 1.0     # (worker E) a stop area member farther than this from every point of its station is a misplaced node
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
STOP_FAR_M = 400      #   (this far when the stop is named after the station and no other station of the line is nearer)
STOP_TRACK_M = 15     #   and a stop counts only this close to the line's (extended) track
LEVEL_FAR_M = 40      # a platform of another mode this far from every platform of the line's own mode is another line's
VPOS_PENALTY = 30     # a platform below ground scored against a line with no tunnel (or on a bridge against one with no viaduct)
TUNNEL_NONE, TUNNEL_SOME = 0.05, 0.1   #   where another candidate line has one: these are the tunnel shares that say so
BRIDGE_NONE, BRIDGE_SOME = 0.1, 0.3    #   and the viaduct shares (the 3's Livonia Avenue viaduct is 13% of a tunnel line)
STRIPE_ANGLE = 10     # boxes get one striped box only when they lie along one axis: within this many degrees ...
STRIPE_LATERAL_M = 15 #   and each centre within this far of the other's axis
MAPPED_W_M = 50       # a box from platforms is at most this wide (real platform sets reach 46 m): wider, the approximate box is used
DUP_APPROX_X = 0.3    # a mapped box of a line's colour over this share of its approximate box stands for it (0.6 of a mapped one)
TERM_END_M = 15       # at a terminus the approximate box ends this far past the end of the track
STRETCH_EXTRA_M = 60  #   and an exit stretches a box only within box_len / 2 + this of its centre (farther ones get a passage)
CONNECT_MAX_M = 150   # an exit with no mapped passage is joined to the station by an estimated passage up to this long
CONNECT_FAR_M = 250   #   (this long when the exit lies along one of the station's lines)
LINK_MAX_M = 200      # the disconnected parts of one station (two lines' boxes with no hall between) likewise
UP_HALL_M2 = 20_000   # an above-ground station building of the station's own stop area counts up to this size
CONC_HALF_M = 45      # an estimated concourse (from the exits, where no hall is mapped) reaches at most this far either side
CONC_HALF_UP_M = 30   #   of its box underground (this far above ground): out to the farthest exit on that side less EXIT_INSET_M
CONC_MIN_EXITS = 3    #   only where this many exits lie in the box's frame ...
CONC_MAX_M2 = 30_000  #   and a rectangle larger than this is not drawn (the box stays as it is)
MAX_CONN = 12         # estimated passages from exits: at most this many a station ...
MAX_CONN_M = 1500     #   and this long in all; the rest of the exits stay icons only (Nagoya drew 39, 7.3 km)
CHAIN_M = 25          # an exit this close to an estimated passage already drawn joins it, not the station body
PIECE_MIN_M2 = 50     # a hall piece smaller than this, or farther than PIECE_FAR_M from every box, is a cutting sliver: dropped
FAR_WHY = ('near the boxes', 'station building (geometry)', 'underground building on the boxes')   # halls taken for these reasons, and
    # indoor areas, lose their far pieces (PIECE_FAR_M); one the station's own stop area lists or named after it keeps them all
PIECE_JOIN_M2 = 100   #   one smaller than this joins the neighbouring line's piece
PIECE_FAR_M = 100     #   a detached piece this far from every box goes when under PIECE_FAR_M2 (Gangxia North's 85 m2 at 323 m)
PIECE_FAR_M2 = 1_000  #   or when its centre is over PIECE_FAR2_M away (Houtan's building, 128 m from the box but 250 m long);
PIECE_FAR2_M = 200    #   Wenbo Park's and Shanghai West's 2,500-2,900 m2 at 115-125 m stay
GROUP_BLD_M2 = 3_000  # a building of the station's stop area group (not its own stop area) is its own ticket hall up to this
                      #   size (Elephant & Castle's Bakerloo hall, 427 m2); a bigger one is the mainline terminus (Cannon Street's, 16,000 m2)
PASS_PIECE_M = 15     # a passage several stations claim is cut among them; a piece shorter than this joins its neighbour
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
                        r'\bstasiun\b|\bstesen\b|\bbuilding\b|\binterchange\b|\bcomplex\b|\bconcourse\b|'   # 'Stasiun LRT Setiabudi', 'Ameerpet Metro Interchange'
                        r'สถานี|محطة|станция|\bl[íi]nea\s*\d+\b|\bl\d{1,2}\b|\(.*?\)|（.*?）)', re.I)   # 'Pantitlán L1', 'Bellas Artes (Línea 2)'
_NAME_SEP = re.compile(r"[\s\-–—·・.,'’\"/]+")
def norm_words(v):
    """the words of a name with the station words dropped, as norm_name joins them (for the whole-word prefix test)"""
    v = unicodedata.normalize('NFKD', v or '')
    v = ''.join(ch for ch in v if not unicodedata.combining(ch))   # 'Félix U. Gómez' matches 'Felix U. Gomez'
    v = _NAME_DROP.sub('', v.lower()).strip()
    v = re.sub(r'^(?:di|de|del|della|des|du|do|da|of)\s+', '', v)   # stazione di X, gare de X
    return tuple(w for w in _NAME_SEP.split(v) if w)
def norm_name(v):
    return ''.join(norm_words(v))
def _affix(ws, n):
    """n is a whole-word prefix or suffix of the words ws"""
    return any(''.join(ws[:k]) == n or ''.join(ws[k:]) == n for k in range(1, len(ws)))
def same_name(t, names, words=None):
    """an OpenStreetMap object named after the station (岗厦北站 for 岗厦北, Gangxia North Station for Gangxia North); also
    one whose name is a whole-word prefix or suffix of the station's, or the other way round, when the shorter has 8
    characters or more ('Uthman Bin Affan' for Uthman Bin Affan Road), or differs by a trailing digit ('Acesso Norte 1').
    `words` maps a normalised station name to its words (norm_words), for the word boundary on the station's side"""
    for k in NAME_KEYS:
        ws = norm_words(t.get(k)); v = ''.join(ws)
        if not v: continue
        if v in names: return True
        for n in names:
            if len(v) > len(n):
                if v[-1].isdigit() and v[:-1] == n: return True
                if len(n) >= 8 and _affix(ws, n): return True
            elif len(n) > len(v):
                if n[-1].isdigit() and n[:-1] == v: return True
                pw = (words or {}).get(n)
                if len(v) >= 8 and pw and _affix(pw, v): return True
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

def vpos(t):
    """vertical position from the tags: -1 below ground, +1 on a bridge or an upper level, 0 when they say nothing"""
    if below_ground(t): return -1
    if pos(t.get('layer')) or pos(t.get('level')) or t.get('bridge') == 'yes' or t.get('location') in ('overground', 'overhead', 'bridge'): return 1
    return 0

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
def down_steps(t):
    """stairs that reach below ground (level -1;0): the way down to the metro, an underground passage however their top
    is tagged (the metro's own steps up into Gare Montparnasse's hall)"""
    return t.get('highway') == 'steps' and (neg_any(t.get('level')) or neg_any(t.get('layer')))

def passage_kind(t):
    hw = t.get('highway')
    if hw == 'service': return False   # a service lane in a tunnel (Hungerford Lane under Charing Cross) is a street, however it is tagged
    if hw in FOOT or t.get('indoor') == 'corridor':
        # a passage through a building counts only below ground and unnamed: a named one is a street arcade or lane
        # (The Arches under Charing Cross, layer -1), not a station passage
        if t.get('tunnel') == 'building_passage' and (any(t.get(k) for k in NAME_KEYS) or not (neg_any(t.get('level')) or neg_any(t.get('layer')))): return False
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
    if t.get('highway') in FOOT and (t.get('covered') == 'yes' or t.get('indoor') == 'yes') and not below_ground(t) and not down_steps(t): return ['passage_up']
    return ['passage'] if passage_kind(t) else []

CLOSED_RE = re.compile(r'未开通|尚未开通|暂未开通|暂未开放|未启用|施工|建设中|under construction|not yet open', re.I)
def closed_exit(t):
    """an entrance not open: under construction, disused, closed off, or named so (Fitness Center's 尚未开通)"""
    if any(k in t for k in ('construction', 'construction:railway', 'disused:railway', 'proposed', 'planned')): return True
    if t.get('railway') in ('construction', 'proposed') or t.get('building') == 'construction' or t.get('disused') == 'yes' or t.get('access') == 'no': return True
    if t.get('entrance') in ('emergency', 'service', 'no') or t.get('emergency') == 'yes' or t.get('exit') == 'emergency': return True   # Milano Centrale's emergency exits
    if t.get('entrance') == 'exit' or t.get('exit') == 'only' or t.get('exit_only') == 'yes': return True   # an exit-only gate (Chicago's rotogates): no way in
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

# the own stop areas listing each member (change 10a): a platform in a stop area whose rows name only some of the
# station's lines (Borough Hall's IRT platforms, in the 2 and 3's stop area, 1 m from the R's track) is those lines' only
member_sa = collections.defaultdict(set)      # 'w45' -> the own stop areas of member_own's station that list it
for i in range(NST):
    for s in sa_of[i]:
        r = rels.get(s)
        if not r: continue
        for t, ref, role in r['members']:
            key = t + str(ref)
            if member_own.get(key) == i: member_sa[key].add(s)
lines_with_sa = [{r[0] for r in rows if r[3].startswith('sa')} for rows in index]   # the lines whose rows name a stop area there
def sa_gate(oid, owner):
    """the lines whose rows at station owner name a stop area listing the object (empty: the stop areas say nothing)"""
    return set().union(*(sa_lines.get((owner, s), set()) for s in member_sa.get(oid, ())))

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

# ---------- every stop area an object is listed in, and the railway's stops (halls, below) ----------
# any_sa_member: 'w45' / 'r6' -> every stop area that lists it, the station's own, another page station's or a foreign one.
# A hall listed by a stop area that is not the station's own (Gul Circle's JRL station polygon, in 'Gul Circle (JRL)')
# is that stop area's, however near or alike in name
any_sa_member = collections.defaultdict(set)
def _sa_members(r):
    for t_, ref, role in r['members']:
        if t_ in ('w', 'r'): any_sa_member[t_ + str(ref)].add(r['id'])
for l in open(f'{OSM}/rels.jsonl', encoding='utf8'):
    if '"stop_area"' not in l: continue
    r = json.loads(l)
    if r['tags'].get('public_transport') == 'stop_area': _sa_members(r)
for r in rels.values():
    if r['tags'].get('public_transport') == 'stop_area': _sa_members(r)
own_grp = {}   # station -> its own stop areas (adopted ones too) and their group's
for i in range(NST):
    s_ = set(sa_of[i])
    for s in list(s_): s_ |= group_of.get(s, set())
    own_grp[i] = s_
# a railway's stop positions (train=yes and no metro mode, not a subway station): a building holding one is the
# railway's, not the metro's, unless the stop lies on the metro's own track (Changzhen's stop says train=yes)
_rail_stops = [(Point(o['lon'], o['lat']), o['id'], ' '.join(o['tags'].get(k_, '') for k_ in ('operator', 'network'))) for o in nodes.values()
               if (o['tags'].get('public_transport') == 'stop_position' or o['tags'].get('railway') in ('stop', 'station', 'halt'))
               and o['tags'].get('train') == 'yes' and not metro_mode(o['tags']) and o['tags'].get('station') not in ('subway', 'light_rail', 'monorail')]
rail_stop_tree = STRtree([p for p, _, _ in _rail_stops]) if _rail_stops else None
print(len(any_sa_member), 'ways and relations in some stop area;', len(_rail_stops), 'railway stop nodes', flush=True)
# an operator or network tag names the same body as the database's operator (or the system's or line's name): a token
# in common, or one a prefix of the other ('CMRL' and 'Chennai Metro Rail Limited (CMRL)', 'BTS' and 'BTSC'). Names in
# another script (東京都交通局) have no Latin token and cannot be compared: they pass
OP_GENERIC = {'metro', 'rail', 'railway', 'railways', 'transit', 'transport', 'transports', 'transportation', 'corporation', 'corp', 'company', 'co',
              'ltd', 'limited', 'authority', 'system', 'mass', 'rapid', 'light', 'line', 'lines', 'the', 'of', 'and', 'de', 'da', 'do', 'du', 'des',
              'la', 'le', 'el', 'pt', 'sa', 'inc', 'group', 'trains', 'train', 'subway', 'urban', 'city', 'public', 'bureau', 'government', 'municipal',
              'metropolitan', 'network', 'operator', 'ag', 'gmbh', 'srl', 'spa', 'plc', 'llc', 'ltda', 'mrt', 'lrt', 'tram', 'bus'}
def _fold(s):
    s = unicodedata.normalize('NFKD', (s or '').lower()); return ''.join(ch for ch in s if not unicodedata.combining(ch))
def op_tokens(s):
    s = _fold(s)
    out = {w for w in re.split(r'[^a-z0-9]+', s) if len(w) >= 2 and w not in OP_GENERIC}
    for phrase in re.split(r'[;,/()]+', s):   # and the initials of each phrase: 'Delhi Metro Rail Corporation' is DMRC
        ws = [w for w in re.split(r'[^a-z0-9]+', phrase) if w]
        if len(ws) >= 2: out.add(''.join(w[0] for w in ws))
    return out
def op_match(a, b):
    """'same' when the two name the same body, 'other' when they are both Latin names that share nothing, None when
    they cannot be compared (a name in another script, or no operator in the database)"""
    ta, tb = op_tokens(a), op_tokens(b)
    if not ta or not tb: return None
    if ta & tb or any(min(len(x), len(y)) >= 3 and (x.startswith(y) or y.startswith(x)) for x in ta for y in tb): return 'same'
    return 'other'
PARK_RE = re.compile(r'停车|駐車|주차|parking|car park|garage|estacionamiento|parcheggio|parkhaus', re.I)
plat_station = {}   # platform feature -> the page station it was assigned to (filled when the first station is drawn)
hall_whole = set()  # features some station drew whole: a clip of another station does not cut them
DEBUG_HALLS = {int(x) for x in os.environ.get('DEBUG_HALLS', '').split(',') if x}   # DEBUG_HALLS=5383,9498 prints their hall tests

# ---------- (worker E) whose exit is an entrance that no page station's stop area lists? ----------
# the other stop area's anchors: its station and stop nodes, and the centroids of its platform and station ways (the
# stop nodes of a railway's stop area are often not in the extracts). An unlabelled entrance nearer to them than to the
# page station is that stop area's (FGC Gràcia's exits 250 m from Fontana, Millennium Station's doors by Washington/
# Wabash, the Circumvesuviana's at Centro Direzionale), see the proximity exits below
osa_anchor = collections.defaultdict(list)   # entrance node -> [(lon, lat)] of the anchors of every such stop area listing it
ent_sas = collections.defaultdict(set)       # entrance node -> every stop area listing it, a page station's or not
for l in open(f'{OSM}/rels.jsonl', encoding='utf8'):
    if '"stop_area"' not in l: continue
    r = json.loads(l)
    if r['tags'].get('public_transport') != 'stop_area': continue
    ents_, anchors = [], []
    for t_, ref, role in r['members']:
        if t_ == 'n':
            nt = nodes[ref]['tags'] if ref in nodes else {}
            if nt.get('railway') in ('subway_entrance', 'train_station_entrance') or nt.get('public_transport') == 'entrance': ents_.append(ref)
            elif role in ('station', 'stop') or role.startswith('stop') or nt.get('railway') in ('station', 'halt', 'stop') or nt.get('public_transport') in ('station', 'stop_position'):
                p = node_xy(ref)
                if p: anchors.append(p)
        elif t_ == 'w' and ref in ways:
            wt = ways[ref]['tags']
            if role in ('platform', 'station') or wt.get('public_transport') in ('platform', 'station') or wt.get('railway') in ('platform', 'station'):
                c = way_coords(ways[ref])
                if c: anchors.append((sum(x for x, _ in c) / len(c), sum(y for _, y in c) / len(c)))
    for n in ents_: ent_sas[n].add(r['id'])
    if ents_ and anchors and r['id'] not in matched_sa:
        for n in ents_: osa_anchor[n].extend(anchors)
# a stop area of the station's group that is no page station's, named like the station and not a railway's or a bus
# station's, is the station's own as far as its exits go: Futian's 福田 lists exits 12A and 12B, 390-430 m from the node
# every line shares (the exits it brings in are metro entrances already, see group_skip). A railway's or a bus
# station's by its own tags or by its nodes ('London Liverpool Street (National Rail)' and 'Charing Cross (National
# Rail)' carry no operator, but every stop position says train=yes and the entrances are the railway's doors); not by
# its platform ways, which Shenzhen tags train=yes on the metro's own (Futian's), so foreign_sa's member test does
# not apply here
def rail_or_bus_sa(r):
    t = r['tags']
    if busy(t) or RAIL_OP_RE.search(' '.join(t.get(k, '') for k in ('operator', 'network'))): return True
    if (t.get('train') == 'yes' or t.get('tram') == 'yes') and not metro_mode(t): return True
    if metro_mode(t): return False
    # by its nodes: train, tram or bus stops and nothing of the metro's (Seoul tags a subway's stop positions train=yes,
    # but its station node station=subway and its entrances railway=subway_entrance; Vienna's same-named tram and bus
    # stop areas have only their stops). Not by its name: Toulouse's Marengo - SNCF and Miami's Dr. Martin Luther
    # King, Jr. are metro stations
    rail = metro = False
    for t_, ref, role in r['members']:
        nt = nodes[ref]['tags'] if t_ == 'n' and ref in nodes else None
        if not nt: continue
        if metro_mode(nt) or nt.get('station') == 'subway' or nt.get('railway') == 'subway_entrance' or nt.get('entrance_marker:subway') == 'yes': metro = True
        elif (role in ('stop', 'station') or nt.get('public_transport') in ('stop_position', 'station') or nt.get('railway') in ('stop', 'station', 'halt', 'tram_stop')) and \
                (nt.get('train') == 'yes' or nt.get('tram') == 'yes' or nt.get('bus') == 'yes'): rail = True
    return rail and not metro
sa_exit_own = {i: set(sa_of[i]) for i in range(NST)}   # the stop areas whose exits the station must draw
n_grp_own = 0; grp_own_log = []; grp_rail_log = []
for i in range(NST):
    names_ = {norm_name(st['name'][i]), norm_name(st['en'][i])} - {''}
    grp = set()
    for s in sa_of[i]: grp |= {x for x in group_of.get(s, ()) if x in rels and x not in sa_of[i] and x not in matched_sa}
    for s in grp:
        r = rels[s]
        if r['tags'].get('public_transport') != 'stop_area' or not same_name(r['tags'], names_): continue
        if rail_or_bus_sa(r): grp_rail_log.append((i, s, r['tags'].get('name', ''))); continue
        sa_exit_own[i].add(s); grp_own_log.append((i, s))
        for t_, ref, role in r['members']:
            if t_ == 'n' and ref in entrance_members[i] and (i, ref) not in own_ent: own_ent.add((i, ref)); n_grp_own += 1
print(len(osa_anchor), 'entrances of stop areas that are no page station\'s;', n_grp_own, 'exits of same-named group stop areas made own', grp_own_log[:12], flush=True)
print(len(grp_rail_log), 'same-named group stop areas left to the railway or the buses', grp_rail_log[:40], flush=True)

# ---------- (worker E, change 14 b) a rail platform of the station's own stop area tagged bus=yes ----------
BUS_PLAT_M = 60   # such a platform counts only from this length, within OWN_TRACK_M of the station's track, in a stop area with no bus stop
bus_plat_ok = []  # the ways taken, for the build log
def own_track_m(i, c):
    """metres from the way with lon/lat coords c to the nearest track of station i's lines (from the line geometry
    itself: the track index is built after the features)"""
    loc = Local(*c[len(c) // 2]); g = LineString(loc.geom(c)); best = None
    for li, _y in st['lines'][i]:
        gl = geo.get(L[li][0])
        if not gl: continue
        for p in (gl['coordinates'] if gl['type'] == 'MultiLineString' else [gl['coordinates']]):
            if len(p) < 2: continue
            d = LineString(loc.geom(p)).distance(g)
            if best is None or d < best: best = d
    return best
def bus_rail_platform(w, t):
    """a platform of the station's own stop area that is the train's though tagged bus=yes (MARTA's Civic Center: a
    covered platform on the bridge over the freeway, 99 m, 14.8 m from the page's line): at least BUS_PLAT_M long,
    within OWN_TRACK_M of one of the station's lines (the platform loop's own tolerance for a platform of the station's
    own stop area: Civic Center's lies 14.8 m off, beyond TRACK_M), and in a stop area with no bus stop, no bus-only
    platform and no rail platform of its own"""
    oid = 'w%d' % w['id']; i = member_own.get(oid)
    if i is None or t.get('public_transport') != 'platform' or t.get('bus') != 'yes' or metro_mode(t) or tram_only(t) or t.get('train') == 'yes': return False
    if t.get('highway') == 'bus_stop' or t.get('amenity') == 'bus_station' or BUS_RE.search(' '.join(t.get(k, '') for k in ('name', 'name:en', 'network', 'operator'))): return False
    c = way_coords(w)
    if not c: return False
    loc = Local(*c[0]); g = LineString(loc.geom(c))
    if is_closed(w):
        mrr = Polygon(loc.geom(c)).minimum_rotated_rectangle
        q = list(mrr.exterior.coords) if mrr.geom_type == 'Polygon' else []
        length = max(math.dist(q[0], q[1]), math.dist(q[1], q[2])) if len(q) >= 3 else 0
    else: length = g.length
    if length < BUS_PLAT_M: return False
    for s in sa_of[i]:
        r = rels.get(s)
        if not r or not any(m[0] == 'w' and m[1] == w['id'] for m in r['members']): continue
        for t_, ref, role in r['members']:
            nt = nodes[ref]['tags'] if t_ == 'n' and ref in nodes else {}
            if nt.get('highway') == 'bus_stop' or (nt.get('public_transport') in ('platform', 'stop_position') and nt.get('bus') == 'yes' and not metro_mode(nt)): return False
            # a stop area with a rail platform of its own needs no stand-in (Dundas West's bus loop over its subway platforms)
            wt = ways[ref]['tags'] if t_ == 'w' and ref != w['id'] and ref in ways else {}
            if (wt.get('public_transport') == 'platform' or wt.get('railway') == 'platform') and wt.get('bus') != 'yes' and not tram_only(wt): return False
    d = own_track_m(i, c)
    if d is None or d > OWN_TRACK_M: return False
    bus_plat_ok.append((i, oid, round(length), round(d, 1)))
    return True

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
        if not kinds and bus_rail_platform(w, t): kinds.append('platform')   # (worker E, change 14 b) MARTA's Civic Center
        if station_area_kind(t) and closed: kinds.append('station')
        elif station_up_kind(t) and closed: kinds.append('station_up')
        if passage_kind(t) and not closed: kinds.append('passage')
        if indoor_area_kind(t) and closed: kinds.append('indoor')
        if not closed and t.get('highway') in FOOT and t.get('indoor') == 'yes' and not below_ground(t) and not down_steps(t): kinds.append('passage_up')
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
# ---------- a railway's platforms ----------
# train=yes platforms with no metro mode are no features (platform_kind), so a building that holds one or stands within
# 10 m of one (Nagoya's JR station polygon r20258665, its platforms mapped as ways beside it) needs them listed here
_rail_plats = []
for w in ways.values():
    t = w['tags']
    if (t.get('public_transport') == 'platform' or t.get('railway') == 'platform') and t.get('train') == 'yes' and not metro_mode(t):
        c = way_coords(w)
        if not c: continue
        g = Polygon(c) if is_closed(w) else LineString(c)
        if not g.is_valid: g = g.buffer(0)
        if not g.is_empty: _rail_plats.append((g, 'w%d' % w['id'], ' '.join(t.get(k_, '') for k_ in ('operator', 'network'))))
for r in rels.values():
    t = r['tags']
    if t.get('type') == 'multipolygon' and (t.get('public_transport') == 'platform' or t.get('railway') == 'platform') and t.get('train') == 'yes' and not metro_mode(t):
        g = rel_polygon(r)
        if g is not None: _rail_plats.append((g, 'r%d' % r['id'], ' '.join(t.get(k_, '') for k_ in ('operator', 'network'))))
rail_plat_tree = STRtree([g for g, _, _ in _rail_plats]) if _rail_plats else None
print(len(_rail_plats), 'railway platforms', flush=True)
# ---------- indoor areas with no level at all ----------
# a closed indoor=area/room/corridor way or multipolygon with no level, layer, location or tunnel (Mexico City's Hidalgo,
# r17980792, which traces the whole station) says nothing about its depth: it counts as a hall (kind indoor0) only where
# it lies on an underground station's track and at two of its exits
def indoor0_kind(t):
    return t.get('indoor') in ('area', 'room', 'corridor') and t.get('type') in (None, 'multipolygon') and \
        not any(k in t for k in ('level', 'layer', 'location', 'tunnel', 'building', 'shop', 'amenity', 'parking'))
n_indoor0 = 0
_have = {f[3] for f in feats}
for w in ways.values():
    if 'w%d' % w['id'] in _have or not indoor0_kind(w['tags']) or not is_closed(w): continue
    c = way_coords(w)
    if not c: continue
    g = Polygon(c)
    if not g.is_valid: g = g.buffer(0)
    if g.is_empty: continue
    feats.append(('indoor0', g, w['tags'], 'w%d' % w['id'])); n_indoor0 += 1
for r in rels.values():
    if 'r%d' % r['id'] in _have or r['tags'].get('type') != 'multipolygon' or not indoor0_kind(r['tags']): continue
    g = rel_polygon(r)
    if g is None: continue
    feats.append(('indoor0', g, r['tags'], 'r%d' % r['id'])); n_indoor0 += 1
del _have
print(n_indoor0, 'indoor areas with no level', flush=True)
# a mainline station's platforms (train=yes and no metro mode) are no feature of the metro's, but their footprint matters:
# no passage inside them, or inside a mainline station building, is the metro's (Charing Cross's arcades over Embankment)
rail_plat, rail_plat_id = [], []
for w in ways.values():
    t = w['tags']
    if t.get('train') == 'yes' and not metro_mode(t) and (t.get('railway') == 'platform' or t.get('public_transport') == 'platform') and is_closed(w):
        c = way_coords(w)
        if not c: continue
        g = Polygon(c)
        if not g.is_valid: g = g.buffer(0)
        if not g.is_empty: rail_plat.append(g); rail_plat_id.append('w%d' % w['id'])
for r in rels.values():
    t = r['tags']
    if t.get('type') == 'multipolygon' and t.get('train') == 'yes' and not metro_mode(t) and (t.get('railway') == 'platform' or t.get('public_transport') == 'platform'):
        g = rel_polygon(r)
        if g is not None: rail_plat.append(g); rail_plat_id.append('r%d' % r['id'])
rail_tree = STRtree(rail_plat) if rail_plat else None
print(len(rail_plat), 'mainline platforms', flush=True)
del ways   # the features are built: the raw ways are not needed again
tree = STRtree([f[1] for f in feats])
# stations whose own building stands on a bridge or an upper level: above ground, whatever their exits are tagged
up_station = {member_own[oid] for kind, g, t, oid in feats if kind in ('station_up', 'own_bld') and oid in member_own and (pos(t.get('layer')) or t.get('bridge') == 'yes')}
# the station buildings and areas of each station's own stop area (change 7): its own word on underground or above ground
own_bld_of = collections.defaultdict(list)
for k, (kind, g, t, oid) in enumerate(feats):
    if kind in ('station', 'station_up', 'own_bld') and oid in member_own: own_bld_of[member_own[oid]].append(k)

print(len(bus_plat_ok), 'bus=yes platforms of own stop areas taken as the train\'s (station, way, m long, m off the track)', bus_plat_ok[:12], flush=True)

# ---------- exits ----------
EXIT_RE = [
    # no letter before the word: 'Deportes' holds no porte
    re.compile(r'(?<![A-Za-z])(?:exit|ausgang|eingang|sortie|salida|uscita|saída|saida|wyjście|výstup|kijárat|выход|вход|porte|acceso|acesso|accès|entrada|ieșire|çıkış|uitgang|gate|puerta)\s*(?:no\.?|number|nr\.?|n°|#)?\s*([A-Za-z]?\d{0,2}[A-Za-z]?)\b', re.I),
    # 东1（北）口 is exit 东1北: the 东1 exit's north stair, kept apart from its south one
    re.compile(r'([東西南北东]?[A-Za-z]?\d{1,2}[A-Za-z]?(?:[（(][東西南北东]{1,2}[)）])?|[A-Za-z])\s*(?:号|號)?\s*(?:出入口|出口|入口|口|番出口|番出入り?口|번\s*출구)'),
    re.compile(r'(?:出口|出入口)\s*([A-Za-z]?\d{0,2}[A-Za-z]?)'),
]
REF_OK = re.compile(r'^[東西南北东]?[A-Za-z]{0,2}\d{0,2}[A-Za-z]?(?:（[東西南北东]{1,2}）|\([NSEW]{1,2}\))?$')
QUAL_RE = re.compile(r'[（(]([東西南北东]{1,2})[)）]')   # a bracketed compass qualifier: kept without its brackets ('东1（北）' → 东1北)
BARE_LABEL = re.compile(r'^(?:[A-Z]{1,2}\d{0,2}[a-z]?|\d{1,2}[A-Za-z]?)$')
RAILWAY_RE = re.compile(r'railway station|train station|railroad|火车站|高铁|客运站|鐵路|铁路', re.I)
LIFT_RE = re.compile(r'电梯|電梯|elevator|lift|ascenseur|엘리베이터|에스컬레이터|エレベーター|エスカレーター', re.I)
def _lab(m):
    """the code a label pattern caught, or '' when it caught a word instead ('Sortie de nuit' → de, 'Exit to Mall' → to)
    or a lowercase letter that is one ('Acceso a la estación' → a, 'Entrada e Saída' → e)"""
    g = m.group(1) if m else ''
    if not g or (g.isalpha() and len(g) > 1 and not g.isupper()) or (len(g) == 1 and g.islower()): return ''
    return QUAL_RE.sub(r'\1', g)
COMPASS = {'northwest': 'NW', 'north-west': 'NW', 'north west': 'NW', 'northeast': 'NE', 'north-east': 'NE', 'north east': 'NE',
           'southwest': 'SW', 'south-west': 'SW', 'south west': 'SW', 'southeast': 'SE', 'south-east': 'SE', 'south east': 'SE',
           'north': 'N', 'south': 'S', 'east': 'E', 'west': 'W',
           'norte': 'N', 'sur': 'S', 'sul': 'S', 'este': 'E', 'leste': 'E', 'oeste': 'W', 'poniente': 'W', 'oriente': 'E',   # Santiago's Salida Norte, Lisbon's
           'noreste': 'NE', 'nordeste': 'NE', 'noroeste': 'NW', 'sureste': 'SE', 'sudeste': 'SE', 'suroeste': 'SW', 'sudoeste': 'SW',
           'شمال غربی': 'NW', 'شمال شرقی': 'NE', 'جنوب غربی': 'SW', 'جنوب شرقی': 'SE', 'شمال': 'N', 'جنوب': 'S', 'شرق': 'E', 'شرقی': 'E', 'غرب': 'W', 'غربی': 'W',
           '东北': 'NE', '東北': 'NE', '东南': 'SE', '東南': 'SE', '西北': 'NW', '西南': 'SW', '东': 'E', '東': 'E', '西': 'W', '南': 'S', '北': 'N'}
def line_refs(i):
    """the refs of station i's lines, with and without their letter ('L3' and '3', 'U2' and '2'): a label equal to one is
    a line's sign, not an exit's code"""
    out = set()
    for li, _y in st['lines'][i]:
        r = (L[li][2] or '').strip().upper()
        if r: out |= {r, re.sub(r'^[A-Z]+', '', r)}
    return out - {''}
def line_sign(lab, lrefs, bare=False):
    """a label that is a line's sign: 'L3' at a station of line L3 (Barcelona's Fontana, Madrid's L12 refs), 'U' or 'S'
    where the lines are U2 and U9 (Berlin's mode signs; not Tsim Sha Tsui's exits L1-L6 or a 南口's S); with bare, a
    plain number equal to a line's ('(7)' in Mexico City)"""
    u = lab.upper()
    if u in ('U', 'S'): return any(r.startswith(u) for r in lrefs)
    if re.match(r'^L\d{1,2}$', u): return u in lrefs or u[1:] in lrefs
    return bare and u in lrefs
def ref_label(t, lrefs=()):
    """the exit's code from its ref or local_ref: 'A3出口' and '出入口6' are exits A3 and 6, '东1（北）' is 东1北 (the 东1 exit's
    north stair, kept apart from the south one); a bare 出口, a lift's ref or a line's sign is no label"""
    for key in ('ref', 'local_ref'):
        ref = (t.get(key) or '').strip()
        if not ref or LIFT_RE.search(ref): continue   # ref=엘리베이터 is the lift, not a code (Samgakji)
        ref2 = re.sub(r'^(出入口|出口|入口)|(番出入口|番出口|出入口|出口|口)$', '', ref)
        if not ref2: continue
        if re.search(r'[A-Za-z0-9]', ref2): ref = ref2
        if len(ref) <= 4 and ' ' not in ref: lab = ref
        elif len(ref) <= 8 and REF_OK.match(ref): lab = QUAL_RE.sub(r'\1', re.sub(r'\([NSEW]{1,2}\)', '', ref))
        else: lab = next((x for x in (_lab(rx.search(ref)) for rx in EXIT_RE) if x), '')
        if lab and not line_sign(lab, lrefs): return lab
    return ''
def name_label(t, snames=(), lrefs=()):
    """the exit's code from its names: 出口A, Exit 3, Gate No. 4, 汉中门#2, さっぽろ駅 20, 'Porta Susa A', a bare F, or its
    compass point (Tehran's, Mashhad's, 东北出口, Santiago's Salida Norte)"""
    for key in ('name', 'name:en', 'name:zh', 'name:ja', 'name:ko', 'description'):
        v = t.get(key) or ''
        for rx in EXIT_RE:
            m = rx.search(v); lab = _lab(m)
            if lab and len(lab) == 1 and lab.isalpha() and re.match(r'\.\s*[A-Za-z]', v[m.end():]): continue   # 'Entrada E. Castellanos': an initial
            if lab and not line_sign(lab, lrefs): return lab
    low = {(sn or '').lower() for sn in snames} - {''}
    for key in ('name', 'name:zh', 'name:en'):
        v = (t.get(key) or '').strip()
        if not v: continue
        if BARE_LABEL.match(v) and v.lower() not in low and not line_sign(v, lrefs): return v   # name=F, with no ref (not QT8's own name)
        m = re.search(r'#\s*([A-Za-z]?\d{1,2}[A-Za-z]?)\s*$', v)
        if m: return m.group(1)
        m = re.match(r'^\s*([A-Z]{1,2}\d{0,2}[a-z]?)\s*[:：]', v)   # 'H: BTM Layout 2nd stage' (Bengaluru)
        if m: return m.group(1)
        m = re.search(r'[（(]([A-Z]{0,2}-?\d{1,2}[a-z]?)[)）]\s*$', v)   # 'サンロード(S7)', 'メルサ(3)' (Nagoya); not '(L9)' or '(7)' naming the line (Mexico City)
        if m and not line_sign(m.group(1), lrefs, bare=True): return m.group(1)
        if LIFT_RE.search(v): continue
        for sn in snames:   # the code after the station's own name
            if not sn or sn.lower() not in v.lower(): continue
            before = _NAME_DROP.sub('', v[:v.lower().index(sn.lower())]).strip(' \t-–—:：#・·')
            if BARE_LABEL.match(before): continue   # a sign before the name ('U Pankow', 'S Zoologischer Garten') is no code
            rest = _NAME_DROP.sub('', re.sub(re.escape(sn), '', v, count=1, flags=re.I)).strip(' \t-–—:：#・·')
            if BARE_LABEL.match(rest) and not re.match(r'^[A-Z]{2}', rest) and not line_sign(rest, lrefs): return rest   # 'Porta Susa A', not 'Porta Nuova FS' or 'Villa Fiorita MM2'
    # an exit named only by its compass point, with the station's own name and the word for exit taken out
    for key in ('name', 'name:en', 'name:fa', 'name:zh', 'name:es', 'name:pt'):
        v = (t.get(key) or '').lower()
        if not v: continue
        for sn in low: v = v.replace(sn, ' ')
        v = re.sub(r'\b(exit|entrance|gate|acceso|accés|acces|salida|sortida|entrada|acesso|saída|saida|puerta|lado|boca|ورودی|خروجی|درب|در)\b|出入口|出口|入口|口$', '', v).strip(' \t-–—:：·/()')
        if v in COMPASS: return COMPASS[v]
    return ''
def exit_label(t, snames=(), lrefs=()):
    """the exit's letter or number: its ref, else one in its name"""
    return ref_label(t, lrefs) or name_label(t, snames, lrefs)

exits = collections.defaultdict(list)       # station -> [(lon, lat, label, name, osm id)]
ex_labs = {}                                # (station, node) -> (label from the ref, label from the name), for the station's convention below
_lrefs = {}
def st_lrefs(i):
    if i not in _lrefs: _lrefs[i] = line_refs(i)
    return _lrefs[i]
def add_exit(i, x, y, t, nid):
    rl = ref_label(t, st_lrefs(i)); nl = name_label(t, (st['name'][i], st['en'][i]), st_lrefs(i))
    ex_labs[(i, nid)] = (rl, nl)
    exits[i].append((x, y, rl or nl, t.get('name', ''), nid))
# station nodes (not bus stations), for an unlabelled far exit that is nearer to another station than to the one it
# would go to (Centro Direzionale's podium doors)
sta_cells = collections.defaultdict(list)
for o in nodes.values():
    t = o['tags']
    if (t.get('railway') in ('station', 'halt') or t.get('public_transport') == 'station') and not busy(t):
        sta_cells[(int(math.floor(o['lon'] / CELL)), int(math.floor(o['lat'] / CELL)))].append(o['id'])
def other_station_nearer(o, i, dkm):
    """a station node that is not station i's own (not in its stop areas, not at its points) nearer to node o than dkm"""
    p = (o['lon'], o['lat']); cx, cy = int(math.floor(p[0] / CELL)), int(math.floor(p[1] / CELL)); r = int(math.ceil(dkm / 0.7)) + 1
    pts = [(q[1], q[2]) for q in index[i]] + [(float(lon[i]), float(lat[i]))]
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            for n in sta_cells.get((cx + dx, cy + dy), ()):
                if n in station_nodes[i]: continue
                qp = (nodes[n]['lon'], nodes[n]['lat'])
                if any(km(qp, s) < 0.05 for s in pts): continue
                if km(p, qp) < dkm: return True
    return False
taken = set()
# an exit two stations' stop areas share (Houhai's lines 2 and 11 are two stations 300 m apart) goes to the nearer
claims = collections.defaultdict(list)
for i, ids in entrance_members.items():
    for n in ids: claims[n].append(i)
for n, cl in claims.items():
    o = nodes[n]; taken.add(n)
    own_cl = [j for j in cl if (j, n) in own_ent]   # a station whose own stop area lists the exit beats a nearer one
    d, i = min((min(km((o['lon'], o['lat']), (q[1], q[2])) for q in index[j]), j) for j in (own_cl or cl))
    # an exit of the station's own stop area is kept up to OWN_EXIT_KM (Futian's 12A, 430 m from the node every line
    # shares; Shijiazhuang's 620 m east; not Qiaozikou's 'A' put 1.4 km off, past the next station: the build log counts
    # the own exits that go missing); one from a group's other stop area (Porta Venezia's Passante doors, 381 m) only
    # when near
    if d > (OWN_EXIT_KM if (i, n) in own_ent else 0.2): continue
    add_exit(i, o['lon'], o['lat'], o['tags'], n)
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
    d, i = cand[0]
    if not exit_label(t, (st['name'][i], st['en'][i]), st_lrefs(i)):
        # an unlabelled entrance is not the station's when a stop area that is no page station's lists it and that stop
        # area's own stops or platforms lie nearer (FGC Gràcia's exits by Fontana, Millennium Station's doors by
        # Washington/Wabash), nor, beyond 200 m, when another station's node is nearer (Centro Direzionale's podium doors)
        if any(km((o['lon'], o['lat']), a) < d for a in osa_anchor.get(o['id'], ())): continue
        if d > 0.2 and other_station_nearer(o, i, d): continue
    add_exit(i, o['lon'], o['lat'], t, o['id'])

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
        add_exit(i, o['lon'], o['lat'], t, o['id']); taken.add(o['id']); n_extra += 1
print(n_extra, 'exits mapped as entrance=*', flush=True)

# ---------- (worker E, change 14 a) duplicate page stations ----------
# two page stations of one system less than DUP_STATION_M apart with the same lines (MARTA's SEC District, 15269 and
# 15280, 9 m) are one station: the lower index draws it, with the other's exits; the higher draws nothing
DUP_STATION_M = 30
dup_station = {}   # the higher index -> the lower
for i in range(NST):
    for d_, j in near_stations((float(lon[i]), float(lat[i])), 0.1):
        if j < i and st_sys[j] == st_sys[i] and j not in dup_station and km((float(lon[i]), float(lat[i])), (float(lon[j]), float(lat[j]))) * 1000 < DUP_STATION_M \
                and {li for li, _y in st['lines'][j]} == {li for li, _y in st['lines'][i]}:
            dup_station[i] = j; break
for i, j in dup_station.items():
    exits[j].extend(exits.pop(i, []))
    for (i_, n_), v in list(ex_labs.items()):
        if i_ == i: ex_labs[(j, n_)] = v
print(len(dup_station), 'duplicate page stations drawn as their twin', sorted(dup_station.items()), flush=True)

# ---------- (worker E, change 5 d-f) each station's exits tidied ----------
DUP_LABEL_M = 100   # one label on two exits farther apart than this: the farther from the station loses it
MERGE_EXIT_M = 15   # unlabelled exits closer than this are one exit
merged_exit = set()   # exit nodes merged into a neighbour: drawn by it, not missing
exit_log = {'converted': [], 'unlabelled': [], 'merged': []}   # OUT/_exit_labels.json, for review
n_conv = n_dup = n_merge = 0
for i, exs in list(exits.items()):
    if not exs: continue
    loc = Local(float(lon[i]), float(lat[i]))
    xy = [loc.xy((e[0], e[1])) for e in exs]
    strictly_own = lambda nid: not (ent_sas.get(nid, set()) - sa_of[i])   # listed by no stop area but the station's own
    # (d) a ref that disagrees with the name's code (ref A on 长乐门-C1口, ref 4 on name 3; not ref 1-1 on 1-1번 출구, whose
    # name code 1 is part of the ref): the station's convention decides, where at least two other exits show ref and
    # name code agreeing, and more agree than disagree. Only where the ref collides with another exit's label (the
    # second 4 at Laoximen, A beside A1 and A2 at Changlemen): a lone ref beats its name (Shibuya's A1 named 渋谷駅2,
    # Hanzomon's 6 named Exit 2), and only for an exit of the station's own stop areas, or of none
    labs = [ex_labs.get((i, e[4]), ('', '')) for e in exs]
    code_ = lambda x: unicodedata.normalize('NFKC', x).upper().lstrip('0') or '0'   # Tenjin's '06' is its ref '6', Fushimi's '１' its '1'
    odd = lambda r_, n_: bool(r_ and n_ and code_(n_) not in code_(r_))
    def collides(k):
        c = code_(labs[k][0])
        return any(q != k and e[2] and (code_(e[2]) == c or (code_(e[2]).startswith(c) and len(e[2]) > len(labs[k][0]))) for q, e in enumerate(exs))
    agree = sum(1 for r_, n_ in labs if r_ and n_ and not odd(r_, n_)); differ = sum(1 for r_, n_ in labs if odd(r_, n_))
    if differ and agree >= 2 and agree > differ:
        conv = [k for k, (r_, n_) in enumerate(labs) if odd(r_, n_) and collides(k) and strictly_own(exs[k][4])]
        new_lab = lambda n_: re.sub(r'^0+(?=\d)', '', unicodedata.normalize('NFKC', n_))   # 07 is 7, Ｍ is M
        exs = [(x, y, new_lab(labs[k][1]) if k in conv else lab, nm, nid) for k, (x, y, lab, nm, nid) in enumerate(exs)]; n_conv += len(conv)
        exit_log['converted'] += [[i, 'n%d' % exs[k][4], labs[k][0], exs[k][2]] for k in conv]
    # (e) one label on exits more than DUP_LABEL_M apart (Euljiro 1(il)-ga's second 1, 2 and 3, an arcade's 290 m west):
    # an exit of one of the station's index-matched stop areas first (Longyang Road's own exit 1, not the maglev
    # station's 1 in a same-named stop area adopted above), then one of an adopted or group stop area, then the nearest
    # to the station keeps it; any within DUP_LABEL_M of a keeper (the two stairs of one exit) keeps it too
    def own_rank(nid):
        if ent_sas.get(nid, set()) & matched_sa & sa_of[i]: return 0
        return 1 if (i, nid) in own_ent else 2
    by_lab = collections.defaultdict(list)
    for k, e in enumerate(exs):
        if e[2]: by_lab[e[2]].append(k)
    unlab = set()
    for lab, ks in by_lab.items():
        kept = []
        for k in sorted(ks, key=lambda k: (own_rank(exs[k][4]), math.hypot(*xy[k]))):
            if kept and all(math.dist(xy[k], xy[q]) > DUP_LABEL_M for q in kept): unlab.add(k)
            else: kept.append(k)
    if unlab:
        exit_log['unlabelled'] += [[i, 'n%d' % exs[k][4], exs[k][2], round(math.hypot(*xy[k]))] for k in sorted(unlab)]
        exs = [(x, y, '' if k in unlab else lab, nm, nid) for k, (x, y, lab, nm, nid) in enumerate(exs)]; n_dup += len(unlab)
    # (f) unlabelled exits less than MERGE_EXIT_M apart (Santa Anita's 2 x 5 grid of gates, 12 m apart) are one exit,
    # drawn at the member nearest the group's centre
    un = [k for k, e in enumerate(exs) if not e[2]]
    root = {k: k for k in un}
    def find_(k):
        while root[k] != k: root[k] = root[root[k]]; k = root[k]
        return k
    for a in un:
        for b in un:
            if b < a and math.dist(xy[a], xy[b]) < MERGE_EXIT_M: root[find_(a)] = find_(b)
    groups_ = collections.defaultdict(list)
    for k in un: groups_[find_(k)].append(k)
    drop = set()
    for g in groups_.values():
        if len(g) < 2: continue
        cx = sum(xy[k][0] for k in g) / len(g); cy = sum(xy[k][1] for k in g) / len(g)
        keep = min(g, key=lambda k: math.hypot(xy[k][0] - cx, xy[k][1] - cy))
        for k in g:
            if k != keep: drop.add(k); merged_exit.add(exs[k][4]); exit_log['merged'].append([i, 'n%d' % exs[k][4], 'n%d' % exs[keep][4]])
    if drop: exs = [e for k, e in enumerate(exs) if k not in drop]; n_merge += len(drop)
    exits[i] = exs
print(n_conv, 'exit labels follow the station\'s name convention;', n_dup, 'duplicate labels dropped;', n_merge, 'unlabelled exits merged into a neighbour', flush=True)
os.makedirs(OUT, exist_ok=True)
json.dump(exit_log, open(f'{OUT}/_exit_labels.json', 'w', encoding='utf8'), ensure_ascii=False)

def own_exits_missing(si, out):
    """(worker E) the open metro entrances of the system's stations' own stop areas (and of the same-named group stop
    areas made own above) that no exit in out['exits'] draws within 3 m, under any station, and that no neighbour
    absorbed: counted per system in the build log, so a dropped exit shows. Called once per system, before its file is
    written"""
    cells = collections.defaultdict(list)   # this system's output exits: (lon, lat, station, label)
    for e in out['exits']:
        p = (e[1] / 1e6, e[2] / 1e6); cells[(int(math.floor(p[0] / CELL)), int(math.floor(p[1] / CELL)))].append((p, e[0], e[3]))
    # the other systems' exits, as assigned above (Bupyeong's exits sit in Seoul line 1's and Incheon line 1's stop areas:
    # the nearer, Incheon's, draws them)
    for j, exs in exits.items():
        if st_sys[j] == si: continue
        for e in exs: cells[(int(math.floor(e[0] / CELL)), int(math.floor(e[1] / CELL)))].append(((e[0], e[1]), j, e[2]))
    miss = []
    for i in range(NST):
        if st_sys[i] != si: continue
        for s in sa_exit_own[i]:
            r = rels.get(s)
            if not r: continue
            for t_, ref, role in r['members']:
                if t_ != 'n' or ref not in nodes: continue
                nt = nodes[ref]['tags']
                if not (nt.get('railway') == 'subway_entrance' or nt.get('public_transport') == 'entrance' or
                        (('entrance' in role or 'entrance' in nt) and (metro_mode(nt) or nt.get('entrance_marker:subway') == 'yes'))): continue
                if closed_exit(nt) or ref in merged_exit: continue
                p = (nodes[ref]['lon'], nodes[ref]['lat']); cx, cy = int(math.floor(p[0] / CELL)), int(math.floor(p[1] / CELL))
                near_ = [(km(p, q), j, lab) for dx in (-1, 0, 1) for dy in (-1, 0, 1) for q, j, lab in cells.get((cx + dx, cy + dy), ())]
                if any(d < 0.003 for d, j, lab in near_): continue
                # the same exit mapped twice (Namsan's 'exit 6' and 'gate 6' nodes, 5 m apart): the output keeps one of a
                # label within 15 m, see the exits of the station loop
                labs_ = {x for x in ex_labs.get((i, ref), ()) if x}
                if labs_ and any(d < 0.015 and j in (i, dup_station.get(i)) and lab in labs_ for d, j, lab in near_): continue
                miss.append((i, 'n%d' % ref, nt.get('ref') or nt.get('name') or ''))
    print(S[si][0], len(miss), 'own stop-area exits missing from the output', miss[:8], flush=True)
    return len(miss)

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

# platforms: each to the (station, line) whose track it runs along. Only features tagged as platforms frame a box: a
# platform-shaped footway ring or indoor area (Luoyang's station outlines, Times Square's A/C/E mezzanine) is a hall at most
plat_ids = [k for k, f in enumerate(feats) if f[0] == 'platform' and (f[2].get('railway') == 'platform' or f[2].get('public_transport') == 'platform')]
plat_to = collections.defaultdict(list)       # (station, line) -> [feature index]
plat_shared = collections.defaultdict(list)   # (station, line) -> platforms of another line on the same track
unassigned = []
DEBUG_PLAT = int(os.environ.get('DEBUG_STATION', '-1'))   # prints every candidate line of that station's platforms
DEBUG_SET = {DEBUG_PLAT} | {int(x) for x in os.environ.get('DEBUG_STATIONS', '').split(',') if x}   # DEBUG_STATIONS=1811,15472: several
def line_share(li, key):
    """the line's tunnel_share_osm or bridge_share_osm from the database, 0 where it has none"""
    try: return float(lines_csv.get(L[li][0], {}).get(key) or 0)
    except ValueError: return 0.0
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
    # (change 10a) the owner's lines whose rows name a stop area listing the platform: its other lines with a stop area
    # of their own are skipped, unless none of the listed lines runs within OWN_TRACK_M of it (a wrong membership)
    gate = sa_gate(oid, owner) if owner is not None else set()
    listed = gate   # the lines whose own stop area lists the platform: never penalised for it (Howard's yellow, elevated)
    gate_ok = False
    cands = []   # [score, station, line, distance, track direction, gated out, penalised]
    for d, i in cand:
        for li, _ in st['lines'][i]:
            if tram_only(t) and li not in TRAM_LINE: continue
            tr = track_near(li, loc, (0, 0), 500)
            if tr is None: continue
            dist = tr.distance(gx)
            if i == owner and li in gate and dist <= OWN_TRACK_M: gate_ok = True
            if dist > TRACK_M: continue
            tg = tangent_deg(tr, gx.centroid)
            da = angdiff(tg[0], ad) if tg else 0
            if da > ANGLE and gx.length > 30: continue
            # near ties go to the line the platform runs along, not the first in the station's list; the stop-area
            # bonus only for the station's own stop area, not a group's (PATH's 14 St platforms are not the M's)
            score = dist + 20 * d + 0.3 * da - (15 if member_own.get(oid) == i else 0)
            cands.append([score, i, li, dist, tg[0] if tg else None, i == owner and bool(gate) and li not in gate and li in lines_with_sa[owner], False])
    if not gate_ok:
        gate = set()
        for c_ in cands: c_[5] = False
    # (change 10b) a platform below ground is not a line's with no tunnel while another candidate line of the station has
    # one, nor a platform on a bridge a line's with no viaduct (Clark/Lake's Loop platform lies right over the Blue subway)
    vt = vpos(t)
    if vt:
        key_, none_, some_ = ('tunnel_share_osm', TUNNEL_NONE, TUNNEL_SOME) if vt < 0 else ('bridge_share_osm', BRIDGE_NONE, BRIDGE_SOME)
        sh = [line_share(c_[2], key_) for c_ in cands]
        for n_, c_ in enumerate(cands):
            if c_[1] == owner and c_[2] in listed: continue
            if sh[n_] < none_ and any(c2[1] == c_[1] and s2 >= some_ for c2, s2 in zip(cands, sh) if c2 is not c_):
                c_[0] += VPOS_PENALTY; c_[6] = True
    live = [c_ for c_ in cands if not c_[5]]
    best = min(live, key=lambda c_: c_[0]) if live else None
    if any(c_[1] in DEBUG_SET for c_ in cands):
        for c_ in cands: print('platform?', oid, L[c_[2]][0], 'station', c_[1], 'score %.1f dist %.1f' % (c_[0], c_[3]), 'gated' if c_[5] else '', 'penalised' if c_[6] else '', 'TAKEN' if c_ is best else '', flush=True)
    if best:
        plat_to[(best[1], best[2])].append(k)
        # other lines of the same station on the same track (Oslo's trunk, the Metropolitan and the Circle) share the
        # platform, but only where they have no platforms of their own (see below), and never across the stop-area
        # gate, a vertical penalty or tracks that cross at more than ANGLE degrees
        for sc_, i2, li2, d2, tg2, gated, pen in cands:
            if i2 == best[1] and li2 != best[2] and d2 <= best[3] + 5 and not gated and not pen and \
                    (tg2 is None or best[4] is None or angdiff(tg2, best[4]) <= ANGLE): plat_shared[(i2, li2)].append(k)
    elif owner is not None and member_own.get(oid) == owner: unassigned.append((k, owner, loc, gx, ad, gate))
n_shared = 0
for key, ks in plat_shared.items():
    if key not in plat_to: plat_to[key] = list(ks); n_shared += 1
print(n_shared, 'lines share another line\'s platforms', flush=True)
# a platform of the station's own stop area that lies further from the track than TRACK_M (split tracks, side
# platforms wide apart: Chengdu's Taipingyuan line 5) still goes to the line it runs parallel to
n_own = 0
for k, owner, loc, gx, ad, gate in unassigned:
    kind, g, t, oid = feats[k]
    best = None
    for li, _ in st['lines'][owner]:
        if tram_only(t) and li not in TRAM_LINE: continue
        if gate and li not in gate and li in lines_with_sa[owner]: continue   # (change 10a) the stop-area gate holds here too
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
def dist_m(ga, gb):
    """distance in metres between two lon/lat geometries"""
    c = ga.centroid; loc = Local(c.x, c.y)
    return affinity.scale(ga, loc.kx, loc.ky, origin=(0, 0)).distance(affinity.scale(gb, loc.kx, loc.ky, origin=(0, 0)))
def own_stop_nodes(i, li):
    """the stop positions of line li's own stop areas at station i: (node id, tags); not a railway's, nor one still
    proposed or being built (Shohada's line 3, railway=proposed)"""
    for r in index[i]:
        if r[0] != li or not r[3].startswith('sa'): continue
        rel = rels.get(int(r[3][2:]))
        if not rel: continue
        for t, ref, role in rel['members']:
            if t != 'n': continue
            nt = nodes.get(ref, {}).get('tags', {})
            if not (role.startswith('stop') or nt.get('public_transport') == 'stop_position' or nt.get('railway') == 'stop'): continue
            if nt.get('train') == 'yes' and not metro_mode(nt): continue
            if nt.get('railway') in ('proposed', 'construction') or any(k in ('proposed', 'construction') or k.startswith(('proposed:', 'construction:')) for k in nt): continue
            yield ref, nt
# (change 10c) a line's mode is the metro mode its platforms carry most often network-wide: in a set of mixed modes, the
# platforms of another mode far from every platform of the line's own are another line's (the Raide-Jokeri light rail
# platforms over Aalto-yliopisto's metro)
_mode_count = collections.defaultdict(collections.Counter)
for (i, li), ks in plat_to.items():
    for k in ks:
        for m in METRO_TAG:
            if feats[k][2].get(m) == 'yes': _mode_count[li][m] += 1
line_mode = {li: cnt.most_common(1)[0][0] for li, cnt in _mode_count.items()}
multi_level = {}   # (station, line) -> (its platforms before the level choice, the levels, most platforms and nearest its stops first)
for key, ks in list(plat_to.items()):
    i, li = key
    tagged = [k for k in ks if metro_mode(feats[k][2])]
    if tagged and len(tagged) < len(ks):
        lv_t = {plat_level(k) for k in tagged}
        ks = [k for k in ks if k in tagged or (feats[k][2].get('train') != 'yes' and plat_level(k) in lv_t)]
    lm = line_mode.get(li)
    if lm:
        own_m = [k for k in ks if feats[k][2].get(lm) == 'yes']
        if own_m and len(own_m) < len(ks) and any(feats[k][2].get(m) == 'yes' for k in ks if k not in own_m for m in METRO_TAG):
            ks = [k for k in ks if k in own_m or min(dist_m(feats[k][1], feats[k2][1]) for k2 in own_m) <= LEVEL_FAR_M]
    lv = collections.Counter(plat_level(k) for k in ks)
    if len(lv) > 1:
        # the level with most platforms; a tie goes to the level nearest the line's own stop positions (else the
        # station's point), not the first seen
        refs = [Point(q) for q in (node_xy(ref) for ref, _nt in own_stop_nodes(i, li)) if q] or [Point(float(lon[i]), float(lat[i]))]
        order = sorted(lv, key=lambda v: (-lv[v], min(dist_m(feats[k][1], rp) for k in ks if plat_level(k) == v for rp in refs)))
        multi_level[key] = (ks, order)
        ks = [k for k in ks if plat_level(k) == order[0]]
    plat_to[key] = ks
# lines of one colour with platforms in two places on two levels (Chambers Street's 1, 2 and 3: Chambers Street at level
# -2, Park Place at -3, 170 m apart) would all take one place and lose the other: where two lines of a colour take one
# level, a line of theirs whose other level lies beyond LEVEL_FAR_M of it, and that no line of the colour has, takes it
_level_lines = collections.defaultdict(collections.Counter)   # (station, colour) -> lines at each level
for (i, li), ks in plat_to.items():
    col = (L[li][5] or '').lower()
    if col and ks: _level_lines[(i, col)][plat_level(ks[0])] += 1
for key in sorted(multi_level):
    i, li = key; col = (L[li][5] or '').lower()
    if not col or not plat_to.get(key): continue
    cnt = _level_lines[(i, col)]; cur = plat_level(plat_to[key][0])
    if cnt[cur] < 2: continue
    ks_all, order = multi_level[key]
    here = [k for k in ks_all if plat_level(k) == cur]
    for v in order:
        if v == cur or cnt[v]: continue
        there = [k for k in ks_all if plat_level(k) == v]
        if min(dist_m(feats[a][1], feats[b][1]) for a in here for b in there) > LEVEL_FAR_M:
            if i in DEBUG_SET: print('level', L[li][0], 'moves from', cur, 'to', v, flush=True)
            plat_to[key] = there; cnt[cur] -= 1; cnt[v] += 1; break

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

def other_station_nearer(p, i, li):
    """another station of line li lies nearer to the point (lon/lat) than station i does"""
    ns = near_stations(p, STOP_FAR_M / 1000 + 0.1)
    d_i = next((d for d, j in ns if j == i), None)
    return d_i is None or any(j != i and d < d_i and any(l_ == li for l_, _y in st['lines'][j]) for d, j in ns)

def stop_centre(i, li, tr, loc, cx, cy):
    """where line li really stops at station i: the mean of its own stop area's stop positions on its track. At an
    interchange the station's point is often one node shared by every line, which can sit far from where a line's
    trains stop (Chengdu's Nijiaqiao line 8 stops 177 m from it)."""
    if tr is None: return None
    pts = []; up = False
    tre = extend_track(tr, MAX_HALF_M)   # a stop just past the end of the line's geometry still counts (Macau's Union Hospital)
    names_i = {norm_name(st['name'][i]), norm_name(st['en'][i])} - {''}
    for ref, nt in own_stop_nodes(i, li):
        p = node_xy(ref)
        if p is None: continue
        q = loc.xy(p)
        d = math.hypot(q[0] - cx, q[1] - cy)
        if i in DEBUG_SET: print('stop?', L[li][0], 'n%d' % ref, 'd %.0f track %.1f' % (d, tre.distance(Point(q))), 'far' if d > STOP_SHIFT_M else '', flush=True)
        if d > STOP_FAR_M or tre.distance(Point(q)) > STOP_TRACK_M: continue
        # (change 12) beyond STOP_SHIFT_M only a stop named after the station that no other station of the line is
        # nearer to (Kunming North's lines 4 and 5 stop 260 m east of the node the three lines share)
        if d > STOP_SHIFT_M and (not same_name(nt, names_i) or other_station_nearer(p, i, li)): continue
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
    far_drop = {}                                    # (OpenStreetMap id, station) -> its far pieces may go (see FAR_WHY)
    area_geom = {}                                   # feature -> the part of it drawn (a hub larger than AREA_MAX_M2)
    path_claims = collections.defaultdict(set)
    schematic = set()                                # passages drawn dashed: straight transfer links between station nodes
    claim_log = []                                   # every hall taken, with why (OUT/_claims/<system>.json, for review)
    stat = {}
    for i in stations_by_sys[si]:
        if i in dup_station:   # (worker E, change 14 a) a duplicate page station is drawn as its twin, see dup_station
            stat[i] = [0, 0, 0, 0]; continue
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
            # (change 8) where the geometry ends at the line's own stop positions the end stands: the platform lies back
            # along the track from the buffer stop, not half past it (Jiyindadao's line 5, Santa Anita's L4)
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
        # (change 7) underground or above ground from the station's own evidence: its platforms, its stop positions and
        # station nodes, and the buildings of its own stop area. Where they say nothing, exits tagged
        # railway=subway_entrance mean underground only on lines that run in tunnel somewhere (Hyderabad's elevated
        # stations have subway entrances too); else None, and box_len goes by the line's tunnel share
        if i in up_station: under_i = False
        else:
            ev = set()
            for li_, _y in st['lines'][i]:
                for k in plat_to.get((i, li_), ()): ev.add(vpos(feats[k][2]))
            for n_ in station_nodes[i]:
                if n_ in nodes: ev.add(vpos(nodes[n_]['tags']))
            for k in own_bld_of.get(i, ()): ev.add(vpos(feats[k][2]))
            ev.discard(0)
            if ev == {-1}: under_i = True
            elif ev == {1}: under_i = False
            elif any((nodes.get(e[4]) or {}).get('tags', {}).get('railway') == 'subway_entrance' for e in exs) and \
                    max((line_share(li_, 'tunnel_share_osm') for li_, _y in st['lines'][i]), default=0) > 0: under_i = True
            else: under_i = None
            if i in DEBUG_SET: print('under?', i, 'own evidence', sorted(ev), '->', under_i, flush=True)
        def approx_box(li, cx, cy, deg, length, end=0, pinned=False):
            ux, uy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
            lim = min(MAX_HALF_M, length / 2 + STRETCH_EXTRA_M)
            proj = lambda p_: (p_[0] - cx) * ux + (p_[1] - cy) * uy
            # the line's exits within reach: its own unreached ones for the stretch; for the terminus test (change 8) its
            # own, reached or not, and any exit right over its track, since one past the end of the track shows the
            # station going on there (Zhongnan Jie's exits 2 and 3, Aldgate's one exit)
            along = [a for a in (proj(p_) for p_, l_, r_ in zip(ex_xy, ex_line, ex_reached) if l_ == li and not r_) if abs(a) <= lim]
            along_all = [a for a in (proj(p_) for p_, l_ in zip(ex_xy, ex_line) if l_ == li or (li in trx and trx[li].distance(Point(p_)) <= BOX_HALF_W)) if abs(a) <= lim]
            if (end > 0 and any(a > TERM_END_M for a in along_all)) or (end < 0 and any(a < -TERM_END_M for a in along_all)): end = 0
            # the line's own stop positions mark where the train stands, normally the platform's middle: with them found
            # the box stays centred on them, and is laid back from the geometry end only where there are none
            if pinned: end = 0
            if i in DEBUG_SET: print('approx', L[li][0], 'len %.0f end %d pinned %s along %s all %s' % (length, end, pinned, [round(a) for a in along], [round(a) for a in along_all]), flush=True)
            if along and pinned:
                # centred on the line's own stop positions and stretched only outward to its exits, the stops kept in
                # the middle third (Futian's line 11 box was dragged 46 m off its stops); farther exits get a passage
                a0, a1 = min(-length / 2, min(along) + EXIT_INSET_M), max(length / 2, max(along) - EXIT_INSET_M)
                a1 = min(a1, -2 * a0); a0 = max(a0, -2 * a1)
            elif along:
                # the box reaches the line's exits, keeps the stops inside its middle, and is at least the train's length
                lo, hi = min(along) + EXIT_INSET_M, max(along) - EXIT_INSET_M
                a0, a1 = min(lo, -0.3 * length), max(hi, 0.3 * length)
                if a1 - a0 < length:
                    c = max(-0.3 * length, min(0.3 * length, (a0 + a1) / 2)); a0, a1 = c - length / 2, c + length / 2
            elif end:   # the track ends here: the box lies along the track, not half past its end
                a0, a1 = (-(length - TERM_END_M), TERM_END_M) if end > 0 else (-TERM_END_M, length - TERM_END_M)
            else:
                a0, a1 = -length / 2, length / 2
            # at a terminus the box stops just past the end of the track (an exit beyond it cleared `end` above)
            if end > 0: a1 = min(a1, TERM_END_M); a0 = min(a0, a1 - length)
            if end < 0: a0 = max(a0, -TERM_END_M); a1 = max(a1, a0 + length)
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
                # the platforms must run along the track (within ANGLE of its direction there): a set that lies across it
                # (中医大·省医院's lines 2 and 4 on line 5's platforms) frames no box, and the approximate one is used
                fr_p = box_frame(pu)
                along_track = not (tg and fr_p and fr_p[3] * 2 >= 30 and angdiff(fr_p[2], tg[0]) > ANGLE)
                if i in DEBUG_SET and not along_track: print('platforms across the track', lid, 'axis %.0f track %.0f' % (fr_p[2], tg[0]), flush=True)
                if tg and tg[2] <= 250 and along_track:
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
                        # no wider than MAPPED_W_M: a frame fitted to a whole station outline is no platform box
                        if i in DEBUG_SET: print('mapped frame', lid, 'len %.0f wid %.0f' % (x1 - x0, y1 - y0), flush=True)
                        if 30 <= x1 - x0 <= MAX_BOX_M and y1 - y0 <= MAPPED_W_M:
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
                got = (approx_box(li, tg0[1].x, tg0[1].y, tg0[0], box_len(lid, under_li), tg0[3] if end_station(i, li) else 0, has_sc), 1)
            if got is None and tr is None:
                # no track near: lay the box between the station's neighbours on the line
                deg = route_deg(i, li, loc)
                if deg is not None:
                    got = (approx_box(li, cx, cy, deg, box_len(lid, under_li)), 1)
            if got is None: continue
            # lines that share a platform and a colour (New York's 1, 2 and 3) get one box; an approximate box is a guess,
            # so a mapped box of its colour over DUP_APPROX_X of it is its platform (Times Square's A guess beside the C's frame)
            col = (L[li][5] or '').lower()
            def same_box(b2, ap2):
                ov = got[0].intersection(b2).area
                return ov > 0.6 * min(got[0].area, b2.area) or (bool(got[1]) != bool(ap2) and ov > DUP_APPROX_X * (got[0].area if got[1] else b2.area))
            dup = next((j for j, (c2, b2) in enumerate(box_cols) if col and c2 == col and same_box(b2, box_approx[j])), None)
            if dup is not None:
                # a mapped box replaces an earlier approximate one of the same colour (Columbus Circle's C under the A's guess)
                if got[1] or not box_approx[dup]: continue
                box_cols[dup] = (col, got[0]); boxes_xy[dup] = got[0]; box_approx[dup] = 0
                continue
            box_cols.append((col, got[0]))
            boxes_xy.append(got[0]); box_line.append(li); box_approx.append(got[1])
        # ---------- halls: the tests, used twice ----------
        # hall_ok decides whether a feature is a hall of this station given its boxes. It runs once here, on the
        # provisional boxes, so an accepted station building can set an approximate box's extent, and again below,
        # on the final boxes, to claim the halls
        names_i = {norm_name(st['name'][i]), norm_name(st['en'][i])} - {''}
        words_i = {norm_name(x): norm_words(x) for x in (st['name'][i], st['en'][i]) if norm_name(x)}
        rail_named_i = bool(RAILWAY_RE.search(st['en'][i] or '') or RAILWAY_RE.search(st['name'][i] or ''))
        ex_pts = [Point(p_) for p_ in ex_xy]
        ex_u = unary_union([p.buffer(15) for p in ex_pts]) if ex_pts else None
        tracks_i = [c_[2] for c_ in cen.values() if c_[2] is not None]
        # the station's own points: its rows' positions and the station and stop nodes of its own stop areas (not a
        # group's: that may be a mainline station's), and never a railway's stop
        own_pts = [Point(loc.xy((r[1], r[2]))) for r in rows]
        for s_ in sa_of[i]:
            for t_, ref, role in rels.get(s_, {'members': ()})['members']:
                if t_ != 'n' or ref not in station_nodes[i]: continue
                nt = (nodes.get(ref) or {}).get('tags', {})
                if nt.get('train') == 'yes' and not metro_mode(nt): continue
                q = node_xy(ref)
                if q: own_pts.append(Point(loc.xy(q)))
        plat_i = {k_ for li_, _y in st['lines'][i] for k_ in plat_to.get((i, li_), ())}
        if not plat_station:
            for (j_, lj_), ks_ in plat_to.items():
                for k_ in ks_: plat_station.setdefault(k_, j_)
        ops_i = ' '.join([lines_csv.get(L[li_][0], {}).get('operator') or '' for li_, _y in st['lines'][i]] + [S[si][1], S[si][2]] + [(L[li_][3] or '') + ' ' + (L[li_][4] or '') for li_, _y in st['lines'][i]])
        dbg_i = DEBUG_ST == i or i in DEBUG_HALLS
        def tunnel_share(lid):
            try: return float(lines_csv.get(lid, {}).get('tunnel_share_osm') or 0)
            except ValueError: return 0.0
        # the station is below ground by its own evidence, not only by its exits' tags (an elevated station's exits are
        # often railway=subway_entrance): a platform or stop of its own below ground and none above, or lines all in tunnel
        _pl_t = [feats[k_][2] for k_ in plat_i]
        _below = any(below_ground(t_) for t_ in _pl_t) or any(neg_any(nt_.get('level')) or neg_any(nt_.get('layer')) for nt_ in ((nodes.get(n_) or {}).get('tags', {}) for n_ in station_nodes[i]))
        _above = any(pos(t_.get('layer')) or pos(t_.get('level')) or t_.get('bridge') == 'yes' for t_ in _pl_t) or any(c_[5] for c_ in cen.values())
        deep_i = under_i is True and not _above and (_below or all(tunnel_share(L[li_][0]) >= 0.98 for li_, _y in st['lines'][i]))
        def longest_box():
            return max((box_frame(b)[3] * 2 for b in boxes_xy if box_frame(b)), default=0)
        def other_operator(t, g, gx, allbox):
            """why a building that is not in the station's stop area is another operator's (Shimbashi's JR and Yurikamome
            buildings, named 新橋 like the Asakusa line's station), or None: on a bridge or upper level at an underground
            station; an operator or network that is a railway's or not the line's; a railway's platform or stop inside it,
            or a platform that is no line's of this station"""
            op = ' '.join(t.get(k_, '') for k_ in ('operator', 'network', 'operator:en', 'network:en'))
            if RAIL_OP_RE.search(op): return 'a railway operator'
            # a railway stop or platform in the station's own boxes (Takashimadaira's platform edges say train=yes) is its
            # own; one on the station's own track (Hung Hom's East Rail, Changzhen's train=yes stop) is its own only for a
            # building: a bare public_transport=station area holding one is the railway's (Nagoya's r20258665 is the
            # outline of the JR platforms)
            bld_ = 'building' in t
            def on_own_track(g_): return g_.distance(allbox) <= 5 or (bld_ and any(tr_.distance(g_) <= 10 for tr_ in tracks_i))
            same_op = op_match(op, ops_i)
            if same_op == 'other': return 'another operator: ' + op.strip()
            if deep_i and same_op != 'same' and (pos(t.get('layer')) or t.get('bridge') == 'yes'): return 'above ground at an underground station'
            for k_ in tree.query(g):
                kd_, pg_, pt_, po_ = feats[k_]
                if kd_ != 'platform': continue
                pp_ = from_ll(loc, pg_)   # inside the building, or a good part of it under it (Buji's waiting hall over the railway)
                if not (pp_.representative_point().within(gx) or pp_.intersection(gx).area > min(0.3 * pp_.area, 500)): continue
                if pt_.get('train') == 'yes' and not metro_mode(pt_) and k_ not in plat_i and not (member_own.get(po_) == i and i not in rail_own): return 'holds a railway platform ' + po_
                # a platform of a railway operator or another operator, with no train tag (Nagoya's JR platforms, 東海旅客鉄道)
                pop_ = ' '.join(pt_.get(x_, '') for x_ in ('operator', 'network'))
                if k_ not in plat_i and not (member_own.get(po_) == i and i not in rail_own) and (RAIL_OP_RE.search(pop_) or op_match(pop_, ops_i) == 'other') \
                        and not on_own_track(pp_): return "holds another operator's platform " + po_ + ' ' + pop_.strip()
                # a platform of a page station elsewhere (not one of this interchange, which the page may split in two)
                j_ = plat_station.get(k_)
                if k_ not in plat_i and j_ is not None and j_ != i and member_station.get(po_) != i and km((lon[i], lat[i]), (lon[j_], lat[j_])) > 0.3: return 'holds a platform of station %d ' % j_ + po_
            # a railway's stop or platform inside it or within 10 m of it (Nagoya's JR station polygon has its stops and
            # platforms just outside): the railway's building, unless the stop or platform lies on the station's own track
            # (Changzhen's stop says train=yes; Hung Hom's East Rail) or is the operator's own
            if rail_stop_tree is not None:
                for j_ in rail_stop_tree.query(g.buffer(2e-4)):
                    p_, n_, op_ = _rail_stops[j_]
                    q_ = Point(loc.xy((p_.x, p_.y)))
                    if q_.distance(gx) > 10 or (member_own.get('n%d' % n_) == i and i not in rail_own) or op_match(op_, ops_i) == 'same': continue
                    if dbg_i: print('  railway stop n%d' % n_, round(q_.distance(gx), 1), 'm away; on own track:', on_own_track(q_), flush=True)
                    if on_own_track(q_): continue
                    return 'a railway stop inside or within 10 m: n%d' % n_
            if rail_plat_tree is not None:
                for j_ in rail_plat_tree.query(g.buffer(2e-4)):
                    pg_, po_, op_ = _rail_plats[j_]
                    pp_ = from_ll(loc, pg_)
                    if pp_.distance(gx) > 10 or (member_own.get(po_) == i and i not in rail_own) or op_match(op_, ops_i) == 'same': continue
                    if dbg_i: print('  railway platform', po_, round(pp_.distance(gx), 1), 'm away; on own track:', on_own_track(pp_), flush=True)
                    if on_own_track(pp_): continue
                    return 'a railway platform inside or within 10 m: ' + po_
            return None
        def hall_ok(k, allbox, reach, dbg=False):
            """feature k as a hall of this station, given the union of its boxes and their 60 m reach: (gx in metres, why,
            kind, the clipped part in lon/lat or None) or None"""
            kind, g, t, oid = feats[k]
            if kind not in ('station', 'station_up', 'indoor', 'indoor0', 'p2_named', 'under_bld', 'own_bld') or g.geom_type not in ('Polygon', 'MultiPolygon'): return None
            if unbuilt(t) or (kind not in ('indoor', 'indoor0') and busy(t)): return None
            gx = shapely.make_valid(from_ll(loc, g)).buffer(0)
            if gx.is_empty: return None
            mine = member_station.get(oid) == i; own_ = member_own.get(oid) == i
            if dbg: print('hall?', kind, oid, 'own', member_own.get(oid), 'mine', member_station.get(oid), round(gx.area), 'rail_own' if i in rail_own else '', {x: t.get(x) for x in ('building', 'train', 'name')}, flush=True)
            def rej(reason):
                if dbg: print('  no:', oid, reason, flush=True)
                return None
            # a railway's hall or platforms (Gare Montparnasse, Metro-North's platforms under Grand Central) are not the metro's
            if t.get('train') == 'yes' and not metro_mode(t) and not (own_ and i not in rail_own): return None
            # a stop area group's railway station (Gare Saint-Lazare, SNCF's) is not the metro's hall either
            if kind == 'station' and mine and not own_ and (RAIL_OP_RE.search(' '.join(t.get(x, '') for x in ('operator', 'network'))) or gx.area > NEAR_AREA_M2): return None
            # a shop, a room or a car-park level beside the boxes (Saint-Lazare's Sephora, 'Parking -3') is not a hall
            if kind in ('indoor', 'indoor0') and not own_ and ('shop' in t or 'parking' in t or t.get('indoor') == 'room' or t.get('amenity') in ('parking', 'bicycle_parking', 'cafe', 'restaurant', 'fast_food', 'bank', 'pharmacy', 'toilets')): return None
            # a station hall named after the station (Gangxia North's 岗厦北站, mapped underground but in no stop area)
            named = kind not in ('indoor', 'indoor0') and same_name(t, names_i, words_i) and t.get('train') != 'yes' and not weak_station(t)
            # another operator's building (Sants Estació's mainline hall, in RENFE's stop area) is not ours, whatever its name
            if not own_ and oid in in_other_sa and (kind in ('station_up', 'p2_named') or named): return None
            if not own_ and t.get('station') in ('train', 'tram', 'monorail') and not metro_mode(t): return None
            # listed by a stop area that is not the station's own, its group's or an adopted one (Gul Circle's JRL station,
            # 103 m away): that stop area's, not a named hall of ours nor one near our boxes
            other_sa = not own_ and not mine and bool(any_sa_member.get(oid, ()) and any_sa_member[oid] - own_grp[i])
            # the station's own building by geometry, where no stop area or name says so: a station building that holds
            # the station's node or stops, lies along its track (within 15 m) for 40 m, or carries two of its exits on
            # its outline, and that nothing marks as another operator's
            geo_own = False
            if kind in ('station', 'station_up', 'own_bld', 'p2_named') and not own_ and not named and not other_sa and oid not in in_other_sa \
                    and (t.get('building') in ('train_station', 'transportation') or t.get('public_transport') == 'station') \
                    and 150 <= gx.area <= UP_HALL_M2 and (t.get('train') != 'yes' or metro_mode(t)) \
                    and (gx.intersects(reach) or gx.distance(Point(0, 0)) < 80):   # not the next station's hall along the track
                nm_ = ' '.join(t.get(x, '') for x in NAME_KEYS)
                # never a car park, a substation or a railway station, however they are tagged (Lukou's 2号停车场, Riyadh Railway Station)
                if 'parking' in t or t.get('amenity') == 'parking' or 'power' in t or PARK_RE.search(nm_) or RAILWAY_RE.search(nm_): return rej('a car park, substation or railway station by name')
                if any(p.within(gx) for p in own_pts) or any(tr_.intersection(gx.buffer(15)).length >= 40 for tr_ in tracks_i) \
                        or sum(1 for p in ex_pts if gx.boundary.distance(p) <= 5) >= 2:
                    oo = other_operator(t, g, gx, allbox)
                    if oo: return rej(oo)
                    geo_own = True
            why = kind; clip = None
            if kind == 'p2_named':
                if not (named or geo_own): return None
                kind = 'station' if below_ground(t) else 'station_up'; why = 'named building (second pass)'
            if kind in ('own_bld', 'station_up') and gx.area < 150: return None   # an entrance canopy, not a hall (Kyoto's 28 m2 'stations')
            if geo_own:
                why = 'station building (geometry)'
            elif kind == 'own_bld':
                if not own_ or gx.area > NEAR_AREA_M2 or not (gx.intersects(reach) or gx.distance(Point(0, 0)) < 80): return None
                why = 'own stop area building'
            elif gx.area > AREA_MAX_M2:
                # an integrated hub (Futian's 135,000 m2 holds the high-speed hall too): only the part about the metro's boxes
                if kind != 'station' or not (own_ or named): return None
                part = gx.intersection(allbox.buffer(80))
                if part.is_empty or not 2000 <= part.area <= 2 * NEAR_AREA_M2: return None
                clip = to_ll_poly(loc, part); gx = part; why = 'hub clipped to the boxes'
            elif kind == 'under_bld':
                # a building below ground, with no station tag or name: only one the boxes run through
                if gx.area > NEAR_AREA_M2 or not gx.intersects(allbox) or gx.distance(Point(0, 0)) > 150: return None
                why = 'underground building on the boxes'
            elif kind == 'indoor0':
                # no level at all: only below ground, lying on the line's track and at two of the station's exits
                if other_sa or under_i is not True or gx.area > NEAR_AREA_M2: return None
                if not any(tr_.buffer(20).intersects(gx) for tr_ in tracks_i) or sum(1 for p in ex_pts if gx.distance(p) <= 10) < 2: return rej('indoor with no level, off the track or the exits')
                why = 'indoor (no level, on track and exits)'
            elif kind == 'station_up':
                # above ground, only the station's own building (Wimbledon's), and only a small one: never a mainline
                # terminus, which a stop area group brings in beside the station (Cannon Street's, Charing Cross's), nor
                # the railway station a metro station is named after (南京站's north building) unless it is the metro's own
                if t.get('train') == 'yes' and not metro_mode(t) and not (own_ and i not in rail_own): return None   # Cawang's LRT building says train=yes
                cap = NEAR_AREA_M2 if (own_ and named) else UP_HALL_M2
                if gx.area > cap or not (own_ or (named and not rail_named_i and gx.distance(Point(0, 0)) < 80)): return None
                if not own_:
                    oo = other_operator(t, g, gx, allbox)   # a building named like the station but another operator's (Shimbashi)
                    if oo: return rej(oo)
                why = 'own station building' if own_ else 'named station building'
                fr_ = box_frame(gx)
                if own_ and fr_ and boxes_xy and fr_[3] * 2 > max(250, 1.5 * longest_box()):
                    # a mainline gallery the metro's stop area lists (Torino Porta Susa, 385 m): only the part about the boxes
                    part = gx.intersection(allbox.buffer(60))
                    if part.is_empty or part.area < 300: return None
                    clip = to_ll_poly(loc, part); gx = part; why = 'own station building clipped to the boxes'
            elif named and not mine:
                if other_sa: return rej('named, but in another stop area')
                why = 'named hall'
                if gx.area > NEAR_AREA_M2:
                    if kind != 'station' or not gx.intersects(allbox.buffer(30)): return None
                elif not (gx.distance(Point(0, 0)) < 150 or gx.intersects(allbox.buffer(30))): return None
            elif not mine:
                if other_sa: return rej('in another stop area')
                why = 'near the boxes'
                if gx.area > NEAR_AREA_M2: return None
                if kind == 'indoor':
                    # an underground pedestrian area is the station's only when it meets its boxes or exits
                    if not (gx.intersects(allbox.buffer(20)) or (ex_u is not None and gx.intersects(ex_u))): return None
                elif not gx.intersects(reach) or not (gx.distance(Point(0, 0)) < 80 or gx.intersects(allbox)): return None
            if why in ('station', 'station_up', 'indoor'): why = ('own stop area ' if own_ else 'stop area group ') + why
            # a long own or named hall (Shenzhen Airport's 814 m ground transport centre basement, Gangxia North's 650 m)
            # is kept only about the metro's boxes, and along a strip to each of the station's exits it reaches that the
            # 80 m buffer leaves out (Houhai's hall reaches exits 130-220 m away)
            if clip is None and kind in ('station', 'own_bld', 'station_up') and (own_ or named) and boxes_xy:
                fr_ = box_frame(gx)
                if (fr_ and fr_[3] * 2 > max(250, 2 * longest_box())) or gx.area > NEAR_AREA_M2:
                    keep = allbox.buffer(80)
                    for p in ex_pts:
                        if gx.distance(p) <= 40 and not keep.intersects(p): keep = keep.union(LineString([nearest_points(allbox, p)[0], p]).buffer(30))
                    part = gx.intersection(keep)
                    if part.is_empty or part.area < 300: return rej('long hall, nothing of it about the boxes')
                    clip = to_ll_poly(loc, part); gx = part; why += ' clipped to the boxes'
            return gx, why, kind, clip
        # an accepted station building sets an approximate box's extent where the line runs lengthwise through it
        # (Ahmedabad's and Bengaluru's elevated stations, Siam): the box becomes the building's span along the track,
        # still approximate, its width the building's (BOX_W to 2 x BOX_HALF_W), the track kept inside it
        BLD_WHY = ('own station building', 'named station building', 'own stop area building', 'own stop area station', 'named hall', 'station building (geometry)')
        if any(box_approx):
            allbox0 = unary_union(boxes_xy); blds = []
            for k in tree.query(Point(loc.ll((0, 0))).buffer(0.004)):
                if feats[k][0] not in ('station', 'station_up', 'own_bld', 'p2_named'): continue
                r_ = hall_ok(k, allbox0, allbox0.buffer(60))
                if r_ and r_[1].replace(' clipped to the boxes', '') in BLD_WHY: blds.append(shapely.make_valid(from_ll(loc, feats[k][1])).buffer(0))   # the whole building, clipped or not
            for bk, (li, ap) in enumerate(zip(box_line, box_approx)):
                cx, cy, tr, has_sc, tg0, up = cen[li]
                if not ap or not blds or tr is None or not tg0: continue
                o = tg0[1]; ux, uy = math.cos(math.radians(tg0[0])), math.sin(math.radians(tg0[0]))
                bc = boxes_xy[bk].centroid; b_along = (bc.x - o.x) * ux + (bc.y - o.y) * uy
                half_len = 0.5 * box_len(L[li][0], False if up else under_i)
                best = None
                for bg in blds:
                    h0, v0, h1, v1 = affinity.rotate(affinity.translate(bg, -o.x, -o.y), -tg0[0], origin=(0, 0)).bounds
                    if dbg_i: print('box of', L[li][0], 'from a building? along', round(h0), round(h1), 'lateral', round(v0), round(v1), 'track through', round(tr.intersection(bg).length), 'm; box centre at', round(b_along), 'train', round(half_len * 2), flush=True)
                    if v0 < -40 or v1 > 40 or not half_len <= h1 - h0 <= MAX_BOX_M or not h0 - 30 <= b_along <= h1 + 30: continue
                    if tr.intersection(bg).length < max(40, 0.6 * (h1 - h0)): continue
                    if best is None or h1 - h0 > best[1] - best[0]: best = (h0, h1, v0, v1)
                if best:
                    h0, h1, v0, v1 = best
                    w_ = min(2 * BOX_HALF_W, max(BOX_W, v1 - v0))
                    vc = max(-(w_ - BOX_W) / 2, min((w_ - BOX_W) / 2, (v0 + v1) / 2))
                    nb = affinity.translate(affinity.rotate(sbox(h0 - 3, vc - w_ / 2, h1 + 3, vc + w_ / 2), tg0[0], origin=(0, 0)), o.x, o.y)
                    boxes_xy[bk] = nb; box_cols[bk] = (box_cols[bk][0], nb)
                    if dbg_i: print('box of', L[li][0], 'set from a building: along', round(h0), round(h1), 'wide', round(w_), flush=True)
        # lines of different colours that share one track or platform (Rio's 1 and 2, the Metropolitan and the Circle)
        # would get one box over another: they get one box striped lengthwise, a stripe a line
        groups = []
        def coaxial(a, b):
            """(change 11) two boxes on one axis: within STRIPE_ANGLE degrees, each centre within STRIPE_LATERAL_M of the
            other's axis. Crossing boxes (中医大·省医院's lines 2 and 4 against line 5) stay apart, drawn one over the other"""
            fa, fb = box_frame(boxes_xy[a]), box_frame(boxes_xy[b])
            if not fa or not fb or angdiff(fa[2], fb[2]) > STRIPE_ANGLE: return False
            for f1, f2 in ((fa, fb), (fb, fa)):
                dg = math.radians(f1[2])
                if abs(-(f2[0] - f1[0]) * math.sin(dg) + (f2[1] - f1[1]) * math.cos(dg)) > STRIPE_LATERAL_M: return False
            return True
        for a in range(len(boxes_xy)):
            for b in range(a):
                if boxes_xy[a].intersection(boxes_xy[b]).area <= 0.6 * min(boxes_xy[a].area, boxes_xy[b].area): continue
                if not coaxial(a, b): continue
                ga = next((g for g in groups if a in g), None); gb = next((g for g in groups if b in g), None)
                # against every member, so a group cannot chain across angles
                if ga and gb and ga is not gb:
                    if all(coaxial(x, y) for x in ga for y in gb): ga |= gb; groups.remove(gb)
                elif ga:
                    if all(coaxial(x, b) for x in ga): ga.add(b)
                elif gb:
                    if all(coaxial(a, y) for y in gb): gb.add(a)
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
        halls = []
        own_blds = []   # the station's own buildings, halls or not: an above-ground passage inside one is the station's
        halls_up = []   # its accepted halls that are buildings above ground (Uijeongbu's, inside the Korail complex)
        bld_all = []    # every building candidate seen, (feature, geometry): the others' buildings reject a footbridge inside them
        for k in tree.query(Point(loc.ll((0, 0))).buffer(0.004)):
            kind0, g0, t0, oid0 = feats[k]
            if kind0 in ('station_up', 'p2_named', 'own_bld') and g0.geom_type in ('Polygon', 'MultiPolygon') and not unbuilt(t0) and not busy(t0):
                gx0 = shapely.make_valid(from_ll(loc, g0)).buffer(0)
                if not gx0.is_empty:
                    bld_all.append((k, gx0))
                    mine0 = member_station.get(oid0) == i; own0 = member_own.get(oid0) == i
                    if kind0 in ('station_up', 'own_bld') and (own0 or (mine0 and oid0 not in in_other_sa and gx0.area <= GROUP_BLD_M2 and not (t0.get('train') == 'yes' and not metro_mode(t0)))):
                        own_blds.append(gx0)   # Elephant & Castle's Bakerloo ticket hall, in the stop area group but no hall (its name has a suffix)
            r_ = hall_ok(k, allbox, reach, dbg_i)
            if not r_: continue
            gx, why, kind, clip = r_
            t, oid = feats[k][2], feats[k][3]
            # a hall two stations clip differently (Houhai's, 300 m from the line 11 station's own box) is drawn as the
            # union of their clips; one a station takes whole stays whole
            if clip is None: hall_whole.add(k); area_geom.pop(k, None)
            elif k not in hall_whole: area_geom[k] = clip if k not in area_geom else unary_union([area_geom[k], clip])
            area_claims[k].add(i); halls.append(gx)
            far_drop[(k, i)] = kind in ('indoor', 'indoor0') or why.startswith(FAR_WHY)
            if kind in ('station_up', 'own_bld'): halls_up.append(gx)
            if dbg_i: print('hall!', oid, why, flush=True)
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
        # an estimated concourse from the exits, where OpenStreetMap has no hall: Chengdu South's 13 exits outline a
        # station far larger than its three boxes. Per line, an approximate box that no hall touches is widened on each
        # side to the farthest exit lying in its frame, less the exit's own stairs; at an interchange the lines'
        # rectangles are joined and cut back among the lines. It is drawn dashed and lighter (an area with a 4th element
        # 1), claims no hall or passage, and is made afresh on every build, so a hall mapped later replaces it
        conc_rects = []
        for b_, li_, ap_ in zip(boxes_xy, box_line, box_approx):
            if not ap_ or any(h_.intersects(b_.buffer(10)) for h_ in halls): continue
            fr_ = box_frame(b_)
            if not fr_: continue
            fx_, fy_, deg_, half_, hw_ = fr_
            ux_, uy_ = math.cos(math.radians(deg_)), math.sin(math.radians(deg_))
            inf = []   # (along, lateral, the line's own exit?) of every exit in the box's frame
            for n_, p_ in enumerate(ex_xy):
                a_ = (p_[0] - fx_) * ux_ + (p_[1] - fy_) * uy_; l_ = -(p_[0] - fx_) * uy_ + (p_[1] - fy_) * ux_
                if abs(a_) <= half_ + EXIT_INSET_M and abs(l_) <= EXIT_LATERAL_M: inf.append((a_, l_, ex_line[n_] == li_))
            own_ex = [x for x in inf if x[2]]   # at an interchange another line's exits widen that line's box, not this one
            if len(own_ex) >= CONC_MIN_EXITS: inf = own_ex
            if len(inf) < CONC_MIN_EXITS:
                if DEBUG_ST == i: print('concourse?', L[li_][0], len(inf), 'exits in the box frame: too few', flush=True)
                continue
            under_li = False if cen[li_][5] else under_i
            cap_ = CONC_HALF_UP_M if under_li is False else CONC_HALF_M
            w_ = [hw_, hw_]   # half-widths either side of the box's axis; a side with no exits keeps the box's own
            for s_, far in ((0, [-l for a, l, _ in inf if l < 0]), (1, [l for a, l, _ in inf if l > 0])):
                if far: w_[s_] = max(BOX_W / 2, min(cap_, max(far) - EXIT_INSET_M))
            r_ = affinity.translate(affinity.rotate(sbox(-half_, -w_[0], half_, w_[1]), deg_, origin=(0, 0)), fx_, fy_)
            if DEBUG_ST == i: print('concourse?', L[li_][0], len(inf), 'exits', round(2 * half_), 'x', round(w_[0]), '+', round(w_[1]), round(r_.area), 'm2', 'dropped' if r_.area > CONC_MAX_M2 else 'taken', flush=True)
            if r_.area > CONC_MAX_M2: continue
            conc_rects.append(r_)
        conc_u = unary_union(conc_rects) if conc_rects else None
        if conc_u is not None:
            for li_, piece in split_by_boxes(conc_u, list(zip(box_line, boxes_xy))).items():
                for ring in ring_ll(loc, piece, 0.6):
                    out['areas'].append([i, li_, [[round(x * 1e6), round(y * 1e6)] for x, y in ring], 1])
        # passages that lead to it (to a box, a hall or an exit): underground ones, and above ground only covered or
        # indoor walkways inside its halls or at its exits. A mainline station's platforms and buildings about it
        # (Charing Cross's over Embankment, Victoria's) hold arcades and concourse walkways that are not the metro's:
        # nothing inside them counts unless it is a tunnel or lies two levels down
        targets = [allbox.buffer(30)] + [p.buffer(20) for p in ex_pts]
        if halls_u is not None: targets.append(halls_u.buffer(15))
        tu = unary_union(targets)
        ex_20 = unary_union([p.buffer(20) for p in ex_pts]) if ex_pts else None
        halls_in = halls_u.buffer(2) if halls_u is not None else None
        own_in = unary_union(own_blds).buffer(2) if own_blds else None
        halls_up_in = unary_union(halls_up).buffer(2) if halls_up else None
        own_ids = {id(g_) for g_ in own_blds}
        other_blds = [g_ for k_, g_ in bld_all if i not in area_claims.get(k_, ()) and id(g_) not in own_ids]
        other_in = unary_union(other_blds) if other_blds else None   # a terminal (Heathrow's), a mainline station (Cannon Street's)
        # mainline platforms about the station, less its own: those its boxes are built on, or of its own stop area
        # (Uijeongbu's Korail platforms are line 1's); Liverpool Street's, crossing the Central line box, stay mainline
        rail_fp = []
        for j in (rail_tree.query(Point(loc.ll((0, 0))).buffer(0.004)) if rail_tree is not None else []):
            if member_own.get(rail_plat_id[j]) == i: continue
            g_ = from_ll(loc, rail_plat[j])
            if g_.intersection(allbox.buffer(5)).area < 0.5 * g_.area: rail_fp.append(g_)
        rail_pl_u = unary_union(rail_fp) if rail_fp else None
        for k in tree.query(Point(loc.ll((0, 0))).buffer(0.004)):
            kind, g, t, oid = feats[k]
            # a mainline station's building, not the metro's own ticket hall (Embankment's, building=train_station too):
            # in a stop area the station does not own, rail-tagged or -named, bigger than any metro building, or holding
            # mainline platforms (Victoria's, in no stop area at all)
            if kind != 'station_up' or g.geom_type not in ('Polygon', 'MultiPolygon') or member_own.get(oid) == i or metro_mode(t) or i in area_claims.get(k, ()): continue
            gx = shapely.make_valid(from_ll(loc, g)).buffer(0)
            if oid in in_other_sa or (oid in member_station and member_own.get(oid) != i and (member_station.get(oid) != i or gx.area > GROUP_BLD_M2)) or t.get('train') == 'yes' or gx.area > UP_HALL_M2 or \
                    RAIL_OP_RE.search(' '.join(t.get(x, '') for x in ('operator', 'network'))) or RAILWAY_RE.search(' '.join(t.get(x, '') for x in NAME_KEYS)) or \
                    (rail_pl_u is not None and gx.intersects(rail_pl_u)):
                rail_fp.append(gx)
        rail_u = unary_union(rail_fp) if rail_fp else None
        def in_rail(gx, t):
            """the passage lies in a mainline station's platforms or building and is not plainly below them: a tunnel, or
            on levels all below ground, is the metro's (Liverpool Street's ticket hall under the concourse), and so are
            steps that reach below ground (level -1;0: the metro's own stairs up into Gare Montparnasse's hall)"""
            if rail_u is None or t.get('tunnel') == 'yes' or neg(t.get('level')) or neg(t.get('layer')): return False
            if down_steps(t): return False
            return gx.intersection(rail_u).length > 0.8 * gx.length
        def low(t):
            """every numeric level and layer at most 1: a footbridge over the platforms, not a terminal's upper walkways"""
            vals = []
            for key in ('level', 'layer'):
                for x in (t.get(key) or '').split(';'):
                    try: vals.append(float(x))
                    except ValueError: pass
            return max(vals, default=0.0) <= 1
        claimed, pending = [], []
        for k, kind, gx in near_pass:
            t_ = feats[k][2]
            # inside one of the station's own above-ground halls it is the station's, whatever mainline footprint covers it too
            if in_rail(gx, t_) and not (halls_up_in is not None and gx.intersection(halls_up_in).length >= 0.7 * gx.length):
                if DEBUG_ST == i: print('passage in a mainline station', feats[k][3], kind, flush=True)
                continue
            if kind == 'passage_up':
                ok = any(u_ is not None and gx.intersection(u_).length >= 0.7 * gx.length for u_ in (halls_in, own_in)) or (ex_20 is not None and gx.intersects(ex_20)) or \
                    (gx.intersects(allbox) and low(t_) and not any(t_.get(x) for x in NAME_KEYS) and
                     (other_in is None or gx.intersection(other_in).length < 0.3 * gx.length))   # West Ham's footbridge over its platforms, not a terminal's walkway
            else:
                ok = gx.intersects(tu)
            if ok:
                path_claims[k].add(i); claimed.append(gx)
                if DEBUG_ST == i: print('passage!', feats[k][3], kind, {x: t_.get(x) for x in ('highway', 'level', 'layer', 'tunnel', 'indoor', 'covered', 'name')}, flush=True)
            elif kind == 'passage': pending.append((k, gx))
        # passages that only join other passages of the station (a corridor between two concourses), a few steps out
        added = 0
        for _ in range(3):
            if not pending or added > 600: break
            cu = unary_union(claimed) if claimed else None
            if cu is None: break
            more = []
            for k, gx in pending:
                if gx.distance(cu) <= 3:
                    path_claims[k].add(i); claimed.append(gx); added += gx.length
                    if DEBUG_ST == i: print('passage! (joins the others)', feats[k][3], flush=True)
                else: more.append((k, gx))
            if len(more) == len(pending): break
            pending = more
        # an exit no mapped passage reaches gets an estimated one (drawn dashed, as approximate), nearest exit first: to
        # an estimated passage already drawn within CHAIN_M of it; else, along the line beyond the box end (a long
        # passage or an underground street), a cross link to one trunk per box end, which runs along the track to the
        # farthest such exit; else straight to the nearest box, hall or concourse, in the colour of the box it reaches.
        # At most MAX_CONN of them and MAX_CONN_M in all a station (Nagoya drew 39, 7.3 km): the rest stay icons only
        n_conn = 0; conn_m = 0.0
        body = unary_union([allbox] + halls + ([conc_u] if conc_u is not None else []))
        my_paths = claimed
        est_lines = []
        def box_of(q):
            return min(zip(boxes_xy, box_line), key=lambda bl: bl[0].distance(q))[1] if boxes_xy else st['lines'][i][0][0]
        def emit(pts, li_=None):
            """an estimated passage through pts (metres), unless a mapped passage already runs there (Century Avenue's
            transfer footways): 1 when drawn"""
            seg = LineString(pts)
            if seg.length < 3 or any(g_.hausdorff_distance(seg) < 3 for g_ in my_paths): return 0
            out['paths'].append([i, box_of(Point(pts[-1])) if li_ is None else li_, [[round(x * 1e6), round(y * 1e6)] for x, y in (loc.ll(q) for q in pts)], 1])
            est_lines.append(seg)
            return 1
        def connector(p_, q): return emit([(p_.x, p_.y), (q.x, q.y)])
        done = set()
        box_by_line = {li: b for b, li in zip(boxes_xy, box_line)}
        trunks = {}   # (line, box end) -> [(centre, direction, half-length), how far along the track the trunk runs]
        def trunk_line(li_, s_):
            (fx, fy, ux, uy, half), reach = trunks[(li_, s_)]
            return LineString([(fx + s_ * half * ux, fy + s_ * half * uy), (fx + s_ * reach * ux, fy + s_ * reach * uy)])
        for n_ in sorted(range(len(ex_xy)), key=lambda n_: body.distance(Point(ex_xy[n_]))):
            p_ = ex_xy[n_]
            key = (round(p_[0]), round(p_[1]))
            if key in done: continue
            done.add(key)
            P = Point(p_)
            d = body.distance(P)
            if d < 6 or any(g_.distance(P) < 12 for g_ in my_paths): continue
            if any(kd == 'passage' and gx_.distance(P) < 20 for _, kd, gx_ in near_pass): continue   # reached through a mapped corridor, if another station's
            if n_conn >= MAX_CONN or conn_m >= MAX_CONN_M: break
            # a mapped passage of the station counts too: Sapporo's exits 20-25 m from Chi-ka-ho join it, not a trunk beside
            # it; the body itself, when nearer (Century Avenue's exit 8 m from its hall), still wins
            near_c = min([(g_.distance(P), g_) for g_ in est_lines + my_paths] + [(trunk_line(*ky).distance(P), trunk_line(*ky)) for ky in trunks], key=lambda x: x[0], default=None)
            if near_c and near_c[0] <= CHAIN_M and near_c[0] < d:
                if near_c[0] >= 6 and connector(P, nearest_points(near_c[1], P)[0]): n_conn += 1; conn_m += near_c[0]
                continue
            li_ = ex_line[n_]
            fr = box_frame(box_by_line[li_]) if li_ in box_by_line else None
            if fr:
                fx, fy, deg, half, hw = fr
                ux, uy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
                a_e = (P.x - fx) * ux + (P.y - fy) * uy; l_e = -(P.x - fx) * uy + (P.y - fy) * ux
                if abs(a_e) > half + 6 and abs(l_e) <= EXIT_LATERAL_M and abs(a_e) - half + abs(l_e) <= 400:
                    s_ = 1 if a_e > 0 else -1
                    reach = trunks[(li_, s_)][1] if (li_, s_) in trunks else half
                    cost = max(0.0, abs(a_e) - reach) + abs(l_e)
                    if conn_m + cost > MAX_CONN_M: continue
                    trunks[(li_, s_)] = [(fx, fy, ux, uy, half), max(reach, abs(a_e))]
                    emit([(fx + a_e * ux, fy + a_e * uy), (P.x, P.y)], li_)   # the cross link (none when the exit sits on the track)
                    n_conn += 1; conn_m += cost
                    continue
            if d > (CONNECT_FAR_M if li_ is not None else CONNECT_MAX_M) or conn_m + d > MAX_CONN_M: continue
            if connector(P, nearest_points(body, P)[0]): n_conn += 1; conn_m += d
        for (li_, s_), ((fx, fy, ux, uy, half), reach) in trunks.items():
            emit([(fx + s_ * half * ux, fy + s_ * half * uy), (fx + s_ * reach * ux, fy + s_ * reach * uy)], li_)
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
            if not any(g_.distance(p) < 12 and g_.distance(q) < 12 for g_ in my_paths): n_conn += connector(a_, b_)
            linked.append(p); rest.remove(p)
        stat[i] = [n_mapped, n_approx, len(seen), n_conn]

    # halls: each OpenStreetMap area once, cut among the boxes of the stations it belongs to (and any other box it
    # covers), each piece in its line's colour; overlapping halls of one line are merged
    pieces = collections.defaultdict(list); far_keep = collections.defaultdict(list)   # label -> pieces of halls that keep their far parts
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
            if not far_drop.get((k, lab[0]), True): far_keep[lab].append(pieces[lab][-1])   # a box the hall merely covers: no claim, so its pieces may go
    # the cut leaves slivers (Gangxia North's 85 m2 at 320 m from its boxes, Jiefang Road's 67 m2). Once a line's pieces
    # are merged, a polygon under PIECE_MIN_M2 goes, so does a detached one far from every box of the station (see
    # PIECE_FAR_M) unless it holds part of a hall the station's own stop area lists or one named after it (FAR_WHY: Toei
    # Shinjuku's share of the Shinjuku west concourse, 233 m from its box); one under PIECE_JOIN_M2 joins the polygon of
    # another line of the station it touches. The test is on the merged geometry, so a concourse mapped as many small
    # corridor ways (Saint-Lazare) keeps every one of them
    merged = {}   # (station, line) -> (Local, its polygons in that frame)
    far_cand = []   # far polygons of PIECE_JOIN_M2 or more: one continuing a neighbouring station's kept piece (Toei Shinjuku's
    # share of the Shinjuku west concourse, which runs on into Shinjuku-nishiguchi's) is not detached, so it is decided last
    for (i, li), ps in pieces.items():
        loc = Local(float(lon[i]), float(lat[i]))
        u = from_ll(loc, unary_union([shapely.make_valid(p) for p in ps])).buffer(0)
        bxs = [from_ll(loc, b) for (j, lj), b in sys_boxes.items() if j == i] or [Point(loc.xy((lon[i], lat[i]))).buffer(20)]
        keep = []; fk = from_ll(loc, unary_union([shapely.make_valid(p) for p in far_keep[(i, li)]])).buffer(0) if far_keep.get((i, li)) else None
        for pg in (u.geoms if hasattr(u, 'geoms') else [u]):
            if pg.geom_type != 'Polygon' or pg.area < PIECE_MIN_M2: continue
            if (fk is None or not pg.intersects(fk)) and min(pg.distance(b) for b in bxs) > PIECE_FAR_M and (pg.area < PIECE_FAR_M2 or min(pg.centroid.distance(b) for b in bxs) > PIECE_FAR2_M):
                if pg.area >= PIECE_JOIN_M2: far_cand.append((i, li, pg))
                continue
            keep.append(pg)
        merged[(i, li)] = (loc, keep)
    if far_cand:
        kept_ll = [(j, to_ll_poly(loc_, q)) for (j, lj), (loc_, qs) in merged.items() for q in qs]
        kt = STRtree([g_ for _, g_ in kept_ll]) if kept_ll else None
        for i, li, pg in far_cand:
            g_ = to_ll_poly(merged[(i, li)][0], pg).buffer(1.5e-5)   # about 1.5 m
            if kt is not None and any(kept_ll[j][0] != i for j in kt.query(g_, predicate='intersects')): merged[(i, li)][1].append(pg)
    for (i, li), (loc, qs) in merged.items():
        for pg in [q for q in qs if q.area < PIECE_JOIN_M2]:
            nb = min(((q.distance(pg), lab2, j) for lab2, (_, qs2) in merged.items() if lab2 != (i, li) and lab2[0] == i
                      for j, q in enumerate(qs2)), key=lambda x: x[0], default=None)
            if nb and nb[0] < 1:
                qs.remove(pg); merged[nb[1]][1][nb[2]] = merged[nb[1]][1][nb[2]].union(pg)
    n_areas = collections.Counter()
    pieces = collections.defaultdict(list)
    for (i, li), (loc, qs) in merged.items():
        if not qs: continue
        u = unary_union(qs).buffer(0); pieces[(i, li)].append(to_ll_poly(loc, u))
        for ring in ring_ll(loc, u, 0.6):
            out['areas'].append([i, li, [[round(x * 1e6), round(y * 1e6)] for x, y in ring]]); n_areas[i] += 1
    # passages: each once, in the colour of the line whose box (else station point) is nearest. One that several stations
    # claim (Namba Walk, the Tenjin underground street, Sapporo's Chi-ka-ho) is cut among them, each taking the stretch
    # nearest its own boxes and halls, so no station's part is lost to another's 320 m clip; a piece under PASS_PIECE_M
    # joins its neighbour. The geometry is OpenStreetMap's, so never marked approximate (Century Avenue's transfer footways)
    body_ll = collections.defaultdict(list)   # station -> its boxes and hall pieces (lon/lat)
    for (i, li), b in sys_boxes.items(): body_ll[i].append(b)
    for (i, li), ps in pieces.items(): body_ll[i].extend(ps)
    body_u = {}
    def station_body(j, loc):
        if j not in body_u: body_u[j] = unary_union(body_ll[j]) if body_ll[j] else Point(float(lon[j]), float(lat[j])).buffer(0.0002)
        return from_ll(loc, body_u[j])
    def nearest_line(j, loc, piece):
        best = None
        for li, _y in st['lines'][j]:
            b = sys_boxes.get((j, li))
            d = from_ll(loc, b).distance(piece) if b is not None else piece.distance(Point(loc.xy((lon[j], lat[j]))))
            if best is None or d < best[0]: best = (d, li)
        return best[1]
    for k, cl in path_claims.items():
        g = feats[k][1]; c = g.centroid; loc = Local(c.x, c.y)
        gx = from_ll(loc, g)
        lines_ = [x for x in (gx.geoms if hasattr(gx, 'geoms') else [gx]) if x.geom_type == 'LineString' and x.length > 0]
        cuts = []   # (station, piece)
        if len(cl) == 1:
            cuts = [(next(iter(cl)), x) for x in lines_]
        else:
            bodies = {j: station_body(j, loc) for j in cl}
            for x in lines_:
                # the nearest claimant every 5 m along it; runs of one owner become the pieces
                n = max(2, int(x.length / 5) + 1); ds = x.length / (n - 1)
                runs = []   # [station, first sample, last sample]
                for q in range(n):
                    p = x.interpolate(q * ds)
                    j = min(cl, key=lambda j_: bodies[j_].distance(p))
                    if runs and runs[-1][0] == j: runs[-1][2] = q
                    else: runs.append([j, q, q])
                while len(runs) > 1:
                    short = next((r_ for r_ in range(len(runs)) if (runs[r_][2] - runs[r_][1] + 1) * ds < PASS_PIECE_M), None)
                    if short is None: break
                    nb = short - 1 if short > 0 else 1   # a short run joins the run before it (the first the one after)
                    runs[nb][1] = min(runs[nb][1], runs[short][1]); runs[nb][2] = max(runs[nb][2], runs[short][2]); del runs[short]
                    merged = []
                    for r_ in runs:
                        if merged and merged[-1][0] == r_[0]: merged[-1][2] = r_[2]
                        else: merged.append(r_)
                    runs = merged
                for r_, (j, q0, q1) in enumerate(runs):
                    s0 = 0 if r_ == 0 else (q0 - 0.5) * ds; s1 = x.length if r_ == len(runs) - 1 else (q1 + 0.5) * ds
                    cuts.append((j, shapely.ops.substring(x, s0, s1)))
        for j, piece in cuts:
            piece = piece.intersection(Point(loc.xy((float(lon[j]), float(lat[j])))).buffer(320))
            if piece.is_empty: continue
            li = nearest_line(j, loc, piece)
            for c_ in line_ll(loc, piece, 0.6):
                out['paths'].append([j, li, [[round(x * 1e6), round(y * 1e6)] for x, y in c_]])
    for i in stations_by_sys[si]:
        nm = st['en'][i] or st['name'][i]
        n_mapped, n_approx, n_exits, n_conn = stat[i]
        cover.append({'system_id': sysrow[0], 'city': sysrow[2], 'station': nm, 'lines': len(st['lines'][i]),
                      'boxes_mapped': n_mapped, 'boxes_approx': n_approx, 'exits': n_exits, 'est_passages': n_conn,
                      'exits_labelled': sum(1 for e in out['exits'] if e[0] == i and e[3]), 'areas': n_areas[i],
                      'areas_est': sum(1 for a in out['areas'] if a[0] == i and len(a) > 3)})
    for k in ('boxes', 'areas', 'paths', 'exits'): total[k] += len(out[k])
    out['builder'] = BUILD_ID
    own_exits_missing(si, out)   # (worker E) the own stop-area exits that went missing, in the build log
    json.dump(out, open(f'{OUT}/{sysrow[0]}.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    os.makedirs(f'{OUT}/_claims', exist_ok=True)
    json.dump(claim_log, open(f'{OUT}/_claims/{sysrow[0]}.json', 'w', encoding='utf8'), ensure_ascii=False)
with open(COVER, 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=list(cover[0].keys())); w.writeheader(); w.writerows(cover)
# what this build was made from, for the deploy step to check against the files it ships
def _iso(ts): return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') if ts else None
def _extract(d):
    fs = [f for p in ('*.jsonl', '*.npy') for f in glob.glob(f'{d}/{p}')]
    return {'dir': d, 'files': len(fs), 'newest': _iso(max((os.path.getmtime(f) for f in fs), default=None))}
json.dump({'builder': BUILD_ID, 'built': _iso(time.time()), 'osm': [_extract(d) for d in (OSM, OSM2) if d],
           'systems': sorted({r['system_id'] for r in cover})}, open(f'{OUT}/_build.json', 'w'), indent=1)
print(dict(total), len(cover), 'stations', 'builder', BUILD_ID)
