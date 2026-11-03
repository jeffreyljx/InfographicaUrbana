# Build the viewer page from the database files
import csv, json, sys, collections, datetime
from shapely.geometry import LineString
DB = sys.argv[1]; TEMPLATE = sys.argv[2]; OUT = sys.argv[3]
def enc(coords):
    out = []; plat = plng = 0
    for lng, lat in coords:
        la, ln = int(round(lat*1e5)), int(round(lng*1e5))
        for v in (la-plat, ln-plng):
            v = ~(v << 1) if v < 0 else (v << 1)
            while v >= 0x20:
                out.append(chr((0x20 | (v & 0x1f)) + 63)); v >>= 5
            out.append(chr(v + 63))
        plat, plng = la, ln
    return ''.join(out)
def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None
systems = list(csv.DictReader(open(f'{DB}/metro_systems.csv', encoding='utf8')))
lines = list(csv.DictReader(open(f'{DB}/metro_lines.csv', encoding='utf8')))
geo = {f['properties']['line_id']: f['geometry']['coordinates'] for f in json.load(open(f'{DB}/metro_lines.geojson'))['features']}
stations = list(csv.DictReader(open(f'{DB}/metro_stations.csv', encoding='utf8')))
stages = list(csv.DictReader(open(f'{DB}/metro_stages.csv', encoding='utf8')))
sidx = {s['system_id']: i for i, s in enumerate(systems)}
lidx = {l['line_id']: i for i, l in enumerate(lines)}
# system position: mean of its stations, else mean of its geometry
pos = collections.defaultdict(list)
for st in stations:
    if st['lat']:
        pos[st['line_id'].split(':')[0]].append((float(st['lon']), float(st['lat'])))
for lid, parts in geo.items():
    sid = lid.split(':')[0]
    if sid not in pos:
        pos[sid] += [tuple(p) for part in parts for p in part[::20]]
kmosm = collections.Counter()
for l in lines:
    if l['included'] == 'yes' and num(l['length_km_osm']):
        kmosm[l['system_id']] += num(l['length_km_osm'])
S = []
for s in systems:
    p = pos.get(s['system_id'])
    lon = round(sum(x for x, _ in p)/len(p), 4) if p else None
    lat = round(sum(y for _, y in p)/len(p), 4) if p else None
    S.append([s['system_id'], s['system_name'], s['city'], s['country'], s['ruling'], s['first_opened'] or s['opened_year_wikipedia'],
              int(s['lines_included'] or 0), int(s['lines_excluded'] or 0), num(s['annual_ridership_m']), s['ridership_year'],
              num(s['length_km_wikipedia']) or num(s['length_km_lines']), lon, lat, round(kmosm[s['system_id']], 1)])
L = []
npts = 0
for l in lines:
    parts = []
    for part in geo.get(l['line_id'], []):
        if len(part) < 2:
            continue
        g = LineString(part).simplify(0.00015)
        cs = list(g.coords); npts += len(cs)
        parts.append(enc(cs))
    L.append([l['line_id'], sidx[l['system_id']], l['ref'], l['name_en'], l['name_local'], l['colour_hex'], 1 if l['included'] == 'yes' else 0, l['ruling_test'],
              l['status'], l['opened'], l['latest_extension'], l['closed'], num(l['length_km']), num(l['length_km_osm']), num(l['stations']), num(l['stations_osm']),
              num(l['annual_ridership_m']), num(l['ridership_daily_k']), l['ridership_year'], l['rolling_stock'], l['car_type'], l['cars_per_train'],
              l['power_supply'], l['gauge_mm'], l['automation'], l['technology'], 1 if l['express'] == 'yes' else 0, l['operator'], l['termini'],
              l['ruling_note'], l['notes'], parts, l['sources']])
ST = []
seen = set()
for st in stations:
    if not st['lat'] or st['line_id'] not in lidx:
        continue
    key = (st['station_id'], st['line_id'])
    if key in seen:
        continue
    seen.add(key)
    ST.append([lidx[st['line_id']], st['name'], st['name_en'], round(float(st['lon']), 5), round(float(st['lat']), 5), st.get('opened', '')])
STG = collections.defaultdict(list)
for t in stages:
    if t['line_id'] in lidx:
        STG[lidx[t['line_id']]].append([t['event'], t['date'], t['from_station'], t['to_station'], num(t['length_km'])])
data = {'systems': S, 'lines': L, 'stations': ST, 'stages': STG, 'n_stations': len({s['station_id'] for s in stations}),
        'built': datetime.date.today().strftime('%-d %b %Y')}
txt = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = open(TEMPLATE, encoding='utf8').read().replace('__DATA__', txt)
open(OUT, 'w', encoding='utf8').write(html)
print('points', npts, 'bytes', len(html.encode('utf8')))
