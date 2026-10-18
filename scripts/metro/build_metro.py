# Pack the world metro database (the project's metro/db folder) into the one JSON file the /metro page reads.
#
#   python3 scripts/metro/build_metro.py /path/to/metro/db public/metro/metro.json [station-index.json]
#
# Needs numpy and shapely. The layout of the output is described at the top of src/lib/metro.ts.
# Only lines that pass the metro definition are kept. Each line's track (OpenStreetMap, simplified to about 15 m)
# is cut into pieces by opening year: every track vertex takes the date of the nearest station-to-station
# segment of that line (metro_segments.csv), so the map can draw a line growing section by section.
# Track nearer an undated segment, or far from every segment, takes the line's own opening year.
import csv, json, math, os, sys, collections, datetime
import numpy as np
from shapely.geometry import LineString, MultiLineString
from shapely.ops import linemerge, nearest_points

DB, OUT = sys.argv[1], sys.argv[2]
SIMPLIFY = 0.00015  # degrees, about 15 m
FAR_KM = 1.5        # track further than this from every segment of its line counts as undated
PARALLEL = 0.0004   # degrees, about 45 m: a second track this close to one already kept is the same line
MIN_PIECE = 0.0006  # degrees, about 65 m: shorter leftovers of a second track are dropped
STRAY_KM = 4.0      # track further than this from every station of its line was matched to the wrong line: dropped

def rows(name):
    return list(csv.DictReader(open(f'{DB}/{name}', encoding='utf8')))

def year(d):
    return int(d[:4]) if d and d[:4].isdigit() else None

def num(x):
    try:
        v = float(x)
        return int(v) if v.is_integer() else v
    except (TypeError, ValueError):
        return None

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

systems = rows('metro_systems.csv')
lines = [l for l in rows('metro_lines.csv') if l['included'] == 'yes']
geo = {f['properties']['line_id']: f['geometry']['coordinates']
       for f in json.load(open(f'{DB}/metro_lines.geojson', encoding='utf8'))['features']}
stations = rows('metro_stations.csv')
segments = rows('metro_segments.csv')
stages = rows('metro_stages.csv')

used_sys = sorted({l['system_id'] for l in lines})
sidx = {s: i for i, s in enumerate(used_sys)}
sysrow = {s['system_id']: s for s in systems}
lines.sort(key=lambda l: (sidx[l['system_id']], l['opened'] or '9999', l['line_id']))
lidx = {l['line_id']: i for i, l in enumerate(lines)}

# Some lines picked up an OpenStreetMap route of the same name in another city (Hamburg's U1 and U2 took Stuttgart's,
# Moscow's line 1 Minsk's): find where each system is (the place most of its stations are near) and leave out every
# route, with its stations, segments and track, that lies far from it
def _xy(s):
    return float(s['lon']), float(s['lat'])
def _km(a, b):
    return math.hypot((a[0] - b[0]) * math.cos(math.radians((a[1] + b[1]) / 2)), a[1] - b[1]) * 111.32
route_pts = collections.defaultdict(list)
for s in stations:
    if s['line_id'] in lidx and s['lat']:
        route_pts[(s['line_id'], s['osm_route'])].append(_xy(s))
sys_routes = collections.defaultdict(list)
for (lid, r), pts in route_pts.items():
    c = (float(np.median([p[0] for p in pts])), float(np.median([p[1] for p in pts])))
    sys_routes[lines[lidx[lid]]['system_id']].append(((lid, r), c, len(pts)))
# the place: the stations ScraperMap itself puts in the system's city, where there are a few; otherwise the route
# centre with the most stations around it
in_city = collections.defaultdict(list)
for s in stations:
    if s['line_id'] in lidx and s['lat'] and s['scrapermap_city']:
        sid = lines[lidx[s['line_id']]]['system_id']
        if s['scrapermap_city'] == sysrow[sid]['city']:
            in_city[sid].append(_xy(s))
SYS_AT = {}
stray_routes = set()
for sid, rs in sys_routes.items():
    pts = in_city.get(sid, [])
    if len(pts) >= 3:
        at = (float(np.median([p[0] for p in pts])), float(np.median([p[1] for p in pts])))
    else:
        at = max((c for _, c, _ in rs), key=lambda c: sum(n for _, c2, n in rs if _km(c, c2) <= 60))
    SYS_AT[sid] = at
    stray_routes |= {k for k, c, _ in rs if _km(c, at) > 80}
# and a route more than ISOLATED_KM from every other station of its system, while its line has a longer route
# elsewhere, belongs to something else (Paris's line 2 picked up the "2" people mover at Charles de Gaulle airport;
# a line on its own far from the rest of its system, like Los Angeles's C Line, stays)
ISOLATED_KM = 10
for sid, rs in sys_routes.items():
    for k, c, n in rs:
        if k in stray_routes:
            continue
        if not any(k2[0] == k[0] and k2 != k and n2 > n for k2, _, n2 in rs):
            continue
        P = np.array(route_pts[k])
        O = np.array([p for k2, _, _ in rs if k2 != k and k2 not in stray_routes for p in route_pts[k2]])
        if not len(O):
            continue
        kx = math.cos(math.radians(float(P[:, 1].mean())))
        if np.hypot((P[:, None, 0] - O[None, :, 0]) * kx, P[:, None, 1] - O[None, :, 1]).min() * 111.32 > ISOLATED_KM:
            stray_routes.add(k)
STRAY_STATIONS = {s['station_id'] for s in stations if (s['line_id'], s['osm_route']) in stray_routes}
print('routes left out (another city, or far from the rest of their line):', sorted(f'{l}#{r}' for l, r in stray_routes), file=sys.stderr)
stations = [s for s in stations if (s['line_id'], s['osm_route']) not in stray_routes]
segments = [g for g in segments if g['from_station_id'] not in STRAY_STATIONS and g['to_station_id'] not in STRAY_STATIONS]

chord_year_at = collections.defaultdict(list)  # (station, line) -> years of the chords that touch it
# chords: straight station-to-station segments per line, dated where metro_segments.csv dates them
st_by_line = collections.defaultdict(list)
for s in stations:
    if s['line_id'] in lidx and s['lat']:
        st_by_line[s['line_id']].append(s)
dated = collections.defaultdict(dict)
for g in segments:
    if g['line_id'] in lidx:
        dated[g['line_id']][frozenset((g['from_station_id'], g['to_station_id']))] = (
            year(g['opened']), (float(g['from_lon']), float(g['from_lat']), float(g['to_lon']), float(g['to_lat'])))

def chords(lid):
    # every pair of consecutive stations along each mapped route of the line; a pair the segments table
    # leaves undated takes the year of the nearest dated pair along the same route (the earlier one on a tie)
    out = dict(dated[lid])
    by_route = collections.defaultdict(list)
    for s in st_by_line[lid]:
        by_route[s['osm_route']].append(s)
    for route in by_route.values():
        route.sort(key=lambda s: int(s['seq'] or 0))
        seq = []
        for a, b in zip(route, route[1:]):
            if a['station_id'] == b['station_id']:
                continue
            k = frozenset((a['station_id'], b['station_id']))
            seq.append((k, out[k][0] if k in out else None,
                        (float(a['lon']), float(a['lat']), float(b['lon']), float(b['lat']))))
        known = [(i, y) for i, (_, y, _) in enumerate(seq) if y]
        for i, (k, y, c) in enumerate(seq):
            if k in out:
                continue
            if known:
                d = min(abs(i - j) for j, _ in known)
                y = min(y2 for j, y2 in known if abs(i - j) == d)
                stats['chords_filled'] += 1
            out[k] = (y, c)
    for k, (y, _) in out.items():
        for sid in k:
            if y:
                chord_year_at[(sid, lid)].append(y)
    return list(out.values())

def drop_parallel(parts):
    # OpenStreetMap often maps each track of a line as its own way, so the line would be drawn (and measured)
    # twice: keep the longest runs, and of every later run only what lies more than PARALLEL from those kept,
    # joined back to the kept track where it leaves it (a branch, or the far end of a loop)
    if len(parts) < 2:
        return parts
    kx = math.cos(math.radians(float(np.mean([y for part in parts for _, y in part]))))
    geoms = sorted((LineString([(x * kx, y) for x, y in part]) for part in parts), key=lambda g: -g.length)
    kept, cover = [], None
    for g in geoms:
        rest = g if cover is None else g.difference(cover)
        pieces = [h for h in getattr(rest, 'geoms', [rest]) if h.geom_type == 'LineString' and h.length >= MIN_PIECE]
        if cover is not None and pieces:
            near = MultiLineString(kept)
            joined = []
            for h in pieces:
                cs = list(h.coords)
                ends = 0
                for end in (0, -1):
                    pt = LineString([cs[end], cs[end]]).centroid
                    a, _ = nearest_points(near, pt)
                    if a.distance(pt) <= PARALLEL * 1.6:
                        cs.insert(0 if end == 0 else len(cs), (a.x, a.y))
                        ends += 1
                # a stretch that leaves the kept track and comes back to it within a few hundred metres is the
                # other bore of a twin tunnel spreading apart (around a station, say), not a branch: drop it
                if ends == 2 and h.length < 0.0135 and h.hausdorff_distance(near) < 0.0027:
                    continue
                joined.append(LineString(cs))
            pieces = joined
        kept += pieces
        buf = g.buffer(PARALLEL)
        cover = buf if cover is None else cover.union(buf)
    stats['parallel_dropped'] += len(parts) - len(kept)
    return [[(x / kx, y) for x, y in h.coords] for h in kept]

def seg_dist_km(px, py, c, kx):
    # distance from points (px, py) to chord c, in km, on a local equirectangular projection
    ax, ay, bx, by = c
    ax, bx, pxx = ax * kx, bx * kx, px * kx
    dx, dy = bx - ax, by - ay
    t = np.clip(((pxx - ax) * dx + (py - ay) * dy) / ((dx * dx + dy * dy) or 1e-12), 0, 1)
    return np.hypot(pxx - ax - t * dx, py - ay - t * dy) * 111.32

stats = collections.Counter()
L = []
for l in lines:
    lid = l['line_id']
    y0 = year(l['opened']) or year(sysrow[l['system_id']]['first_opened'])  # a line without an opening date takes its system's
    ch = chords(lid)
    pieces = []
    # OpenStreetMap gives the track as many short ways: join them into continuous runs first
    raw = [p for p in geo.get(lid, []) if len(p) >= 2]
    merged = linemerge(MultiLineString([[(round(x, 7), round(y, 7)) for x, y in p] for p in raw])) if raw else None
    parts = [] if merged is None else [list(g.coords) for g in getattr(merged, 'geoms', [merged])]
    sts = st_by_line.get(lid)
    if sts and parts:
        S = np.array([(float(x['lon']), float(x['lat'])) for x in sts])
        def near_stations(part):
            P = np.array(part)
            kx = math.cos(math.radians(P[:, 1].mean()))
            d = np.hypot((P[:, None, 0] - S[None, :, 0]) * kx, P[:, None, 1] - S[None, :, 1]).min() * 111.32
            return d <= STRAY_KM
        keep = [p for p in parts if near_stations(p)]
        stats['stray_parts'] += len(parts) - len(keep)
        parts = keep
    elif parts and l['system_id'] in SYS_AT:
        at = SYS_AT[l['system_id']]
        keep = [p for p in parts if min(_km(q, at) for q in p[::max(1, len(p) // 20)]) <= 80]
        stats['stray_parts'] += len(parts) - len(keep)
        parts = keep
    parts = drop_parallel(parts)
    for part in parts:
        cs = list(LineString(part).simplify(SIMPLIFY).coords)
        P = np.array(cs)
        kx = math.cos(math.radians(P[:, 1].mean()))
        if ch:
            D = np.stack([seg_dist_km(P[:, 0], P[:, 1], c, kx) for _, c in ch])
            best = D.argmin(0)
            yrs = [ch[b][0] if D[b, k] <= FAR_KM else None for k, b in enumerate(best)]
        else:
            yrs = [None] * len(cs)
        stats['vertices'] += len(yrs); stats['vertices_undated'] += sum(1 for y in yrs if y is None)
        yrs = [y if y is not None else y0 for y in yrs]
        # a vertex's year opens the stretch from it to the next vertex: use the later of the two ends,
        # so a stretch never appears before both of its ends exist
        seg_years = [max(a, b) if a is not None and b is not None else (a or b) for a, b in zip(yrs, yrs[1:])]
        runs = []  # [year, number of stretches, year, number, ...]
        for y in seg_years:
            if runs and runs[-2] == y:
                runs[-1] += 1
            else:
                runs += [y, 1]
        pieces.append([enc(cs), runs])
        stats['pieces'] += len(runs) // 2
    s = sysrow[l['system_id']]
    L.append([
        lid, sidx[l['system_id']], l['ref'], l['name_en'], l['name_local'], l['colour_hex'] or '',
        l['opened'], l['latest_extension'], l['closed'], l['status'],
        num(l['length_km']), num(l['length_km_osm']), num(l['stations']), num(l['stations_osm']),
        num(l['annual_ridership_m']), num(l['ridership_daily_k']), l['ridership_year'],
        l['rolling_stock'], l['car_type'], l['cars_per_train'], l['power_supply'], l['gauge_mm'], l['automation'],
        l['technology'], 1 if l['express'] == 'yes' else 0, l['national_mode'], l['operator'], l['termini'],
        l['sources'], pieces])

# stations: one entry per station, with the year each of its lines reached it. Stations are ordered by system,
# then along their first line, so neighbouring entries are near each other and the coordinate deltas stay small.
line_year = {l['line_id']: year(l['opened']) or year(sysrow[l['system_id']]['first_opened']) for l in lines}
# OpenStreetMap often keeps one stop area per line at an interchange (King's Cross St Pancras is five): within a
# system, stations with the same Wikidata item less than MERGE_KM apart, or with the same name less than
# MERGE_NAME_KM apart, are one station (New York has five 23rd Streets a block or two apart, each its own station)
MERGE_KM, MERGE_NAME_KM = 0.6, 0.15
parent = {}
def find(a):
    while parent.setdefault(a, a) != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
groups = collections.defaultdict(list)
for s in stations:
    if s['line_id'] in lidx and s['lat']:
        sid = lines[lidx[s['line_id']]]['system_id']
        if s['wikidata']:
            groups[(sid, 'wd', s['wikidata'])].append(s)
        groups[(sid, 'name', ' '.join(s['name'].lower().split()))].append(s)
for k, g in groups.items():
    lim = MERGE_KM if k[1] == 'wd' else MERGE_NAME_KM
    for a in g:
        for b in g:
            if a['station_id'] < b['station_id'] and _km(_xy(a), _xy(b)) <= lim:
                parent[find(b['station_id'])] = find(a['station_id'])

ST = {}
routes = collections.defaultdict(lambda: collections.defaultdict(list))  # line -> route -> [(seq, station)]
for s in stations:
    lid = s['line_id']
    if lid not in lidx or not s['lat']:
        continue
    y = year(s['opened'])
    if y is None:
        ys = chord_year_at.get((s['station_id'], lid))
        y = min(ys) if ys else line_year[lid]
        stats['station_year_fallback'] += 1
    cid = find(s['station_id'])
    e = ST.get(cid)
    if e is None:
        e = ST[cid] = {'name': s['name'], 'en': s['name_en'] if s['name_en'] != s['name'] else '',
                       'pts': [], 'rows': [], 'lines': [], 'wd': s['wikidata'], 'key': (lidx[lid], int(s['seq'] or 0))}
    e['pts'].append(_xy(s))
    e['rows'].append([lidx[lid], *_xy(s), s['osm_station']])
    e['wd'] = e['wd'] or s['wikidata']
    have = next((x for x in e['lines'] if x[0] == lidx[lid]), None)
    if have is None:
        e['lines'].append([lidx[lid], y])
    elif y is not None and (have[1] is None or y < have[1]):
        have[1] = y
    e['key'] = min(e['key'], (lidx[lid], int(s['seq'] or 0)))
    routes[lidx[lid]][s['osm_route']].append((int(s['seq'] or 0), cid))
stats['stations_merged'] = sum(len(e['pts']) for e in ST.values()) - len(ST)
for e in ST.values():
    e['lon'] = sum(p[0] for p in e['pts']) / len(e['pts'])
    e['lat'] = sum(p[1] for p in e['pts']) / len(e['pts'])
order = sorted(ST, key=lambda k: ST[k]['key'])
pos = {k: i for i, k in enumerate(order)}
for e in ST.values():
    e['lines'].sort(key=lambda x: (x[1] or 9999, x[0]))
q = lambda v: int(round(v * 1e5))
lon = [q(ST[k]['lon']) for k in order]; lat = [q(ST[k]['lat']) for k in order]
stations_out = {
    'name': [ST[k]['name'] for k in order],
    'en': [ST[k]['en'] for k in order],
    'lon': [lon[0]] + [b - a for a, b in zip(lon, lon[1:])],  # 1e-5 degrees, delta-coded
    'lat': [lat[0]] + [b - a for a, b in zip(lat, lat[1:])],
    'lines': [ST[k]['lines'] for k in order],                  # [[line, year], ...], earliest first
    'wd': [ST[k]['wd'] for k in order],                        # Wikidata id
}
# each line's mapped routes as station sequences (indices into the station arrays), longest first
for i, l in enumerate(L):
    rs = []
    for r in routes[i].values():
        seq = [pos[sid] for _, sid in sorted(r)]
        rs.append([x for k, x in enumerate(seq) if k == 0 or x != seq[k - 1]])  # two stops of one merged station
    rs.sort(key=len, reverse=True)
    l.insert(len(l) - 1, rs)

S = []
for sid in used_sys:
    s = sysrow[sid]
    S.append([sid, s['system_name'], s['city'], s['country'], s['iso2'], s['first_opened'], num(s['annual_ridership_m']),
              s['ridership_year'], num(s['length_km_wikipedia']), num(s['stations_wikipedia'])])

STG = collections.defaultdict(list)
for t in stages:
    if t['line_id'] in lidx:
        STG[lidx[t['line_id']]].append([t['event'], t['date'], t['from_station'], t['to_station'], num(t['length_km'])])

# track, one entry per mapped part: [line, polyline, [year, stretches, year, stretches, ...]]
geom = [[i, g, r] for i, l in enumerate(L) for g, r in l.pop()]
data = {'v': 1, 'built': datetime.date.today().isoformat(), 'systems': S, 'lines': L, 'geom': geom,
        'stations': stations_out, 'stages': [STG.get(i, []) for i in range(len(L))]}
# shared track drawn once: the lines on each piece of corridor (scripts/metro/build_bundles.py)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_bundles import add_bundles
add_bundles(data)
txt = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
open(OUT, 'w', encoding='utf8').write(txt)
# optional: which database rows (line, lon, lat, OpenStreetMap stop area) each packed station came from, for
# scripts/metro/build_structures.py, which maps station outlines and exits
if len(sys.argv) > 3:
    json.dump([ST[k]['rows'] for k in order], open(sys.argv[3], 'w', encoding='utf8'), separators=(',', ':'))
print(len(S), 'systems', len(L), 'lines', len(order), 'stations', stats['pieces'], 'pieces',
      stats['station_year_fallback'], 'station years from fallback', len(txt.encode()), 'bytes;',
      stats['vertices_undated'], 'of', stats['vertices'], 'track vertices undated')
