"""Turn the master CSV into the JSON the site ships with.
Run:  python3 scripts/build_data.py
Outputs:
  public/data/towers.json    compact index the map loads first
  public/data/details.json   everything else, lazy-loaded
  src/data/towers.json       same index, imported at build time for static pages
  src/data/details.json
  src/data/places.json       cities + districts with counts and ranks
"""
import pandas as pd, json, re, math, unicodedata, os

d = pd.read_csv('data_master.csv')
photos = {}
if os.path.exists('photos.json'):
    photos = {int(k): v for k, v in json.load(open('photos.json')).items()}

def slug(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-z0-9]+', '-', s.lower())
    return re.sub(r'-+', '-', s).strip('-') or 'x'

def lc(s):
    # approximation of JavaScript's String.localeCompare order (accent- and case-insensitive first)
    base = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode().casefold()
    return (base, str(s))

def nz(v):
    return None if (v is None or (isinstance(v, float) and math.isnan(v))) else v

# ---- string tables -------------------------------------------------------
cities = sorted(d.city.unique())
city_i = {c: i for i, c in enumerate(cities)}
dist_keys = sorted(set(zip(d.city, d.district)))
dist_i = {k: i for i, k in enumerate(dist_keys)}
statuses = ['Completed', 'Architecturally topped out', 'Structurally topped out', 'Under construction']
status_i = {s: i for i, s in enumerate(statuses)}
functions = sorted(d.function.fillna('').unique())
func_i = {f: i for i, f in enumerate(functions)}
precisions = ['building-verified', 'building', 'building-geocoded', 'complex', 'approximate']
prec_i = {p: i for i, p in enumerate(precisions)}

# ---- index rows ----------------------------------------------------------
rows = []
for r in d.itertuples():
    rows.append([
        int(r.id), r.name, round(float(r.lat), 5), round(float(r.lon), 5), float(r.height_m),
        city_i[r.city], dist_i[(r.city, r.district)], status_i[r.status],
        None if pd.isna(r.year) else int(r.year), int(r.floors),
        func_i[r.function if not pd.isna(r.function) else ''],
        prec_i[r.coord_precision], int(r.shares_point_with),
        1 if int(r.id) in photos else 0,
    ])
unplaced = pd.read_csv('data_unplaced.csv') if os.path.exists('data_unplaced.csv') else pd.DataFrame(columns=['city'])
meta = {'unplaced': int(len(unplaced)),
        'unplaced_top': [[c, int(n)] for c, n in unplaced.city.value_counts().head(4).items()]}
if os.path.exists('expansion_ids.txt'):
    meta['added_2026_09'] = sum(1 for l in open('expansion_ids.txt') if l.strip() and int(l) in set(d.id))
index = {
    'meta': meta,
    'schema': ['id','name','lat','lon','height_m','city','district','status','year','floors','function','precision','shares_point','has_photo'],
    'cities': cities,
    'districts': [[city_i[c], dname] for c, dname in dist_keys],
    'statuses': statuses,
    'functions': functions,
    'precisions': precisions,
    'rows': rows,
}

# ---- details (positional, keyed by id) --------------------------------
DETAIL_SCHEMA = ['country','sub_area','material','address','ctbuh_slug_if_different','height_confirmed','coord_note','osm_way','photo']
details = {'schema': DETAIL_SCHEMA, 'rows': {}}
for r in d.itertuples():
    ph = photos.get(int(r.id))
    cslug = r.ctbuh_url.rstrip('/').split('/')[-2]
    details['rows'][int(r.id)] = [
        r.country, nz(r.sub_area), nz(r.material), nz(r.address), (None if cslug == slug(r.name) else cslug),
        1 if bool(r.height_confirmed) else 0,
        nz(r.coord_note), None if pd.isna(r.osm_way) else int(r.osm_way),
        # photo: thumb, Commons page, author, licence, licence URL, and 'complex' when the photo is of the
        # tower's complex (a Commons category named for the development) rather than the tower alone
        ([ph['thumb'], ph['page'], ph.get('author'), ph.get('license'), ph.get('license_url')]
         + (['complex'] if ph.get('scope') == 'complex' else []) if ph else None),
    ]

# ---- places (cities + districts) ----------------------------------------
comp = d[d.status == 'Completed']
def agg(g):
    gc = g[g.status == 'Completed']
    tallest = (gc if len(gc) else g).loc[(gc if len(gc) else g).height_m.idxmax()]
    return {
        'count': int(len(g)),
        'completed': int((g.status == 'Completed').sum()),
        'supertall': int((g.height_m >= 300).sum()),
        # counts at the two higher thresholds: all statuses (count*) and completed only (completed*)
        'count200': int((g.height_m >= 200).sum()), 'completed200': int((gc.height_m >= 200).sum()),
        'count300': int((g.height_m >= 300).sum()), 'completed300': int((gc.height_m >= 300).sum()),
        # aggregate skyline height: heights of the completed towers added up, at each threshold (metres; same as derive.mjs)
        'skyline': round(float(gc.height_m.sum()), 1), 'skyline200': round(float(gc[gc.height_m >= 200].height_m.sum()), 1),
        'skyline300': round(float(gc[gc.height_m >= 300].height_m.sum()), 1),
        'tallest_id': int(tallest.id), 'tallest_name': tallest['name'], 'tallest_h': float(tallest.height_m),
        'lat': round(float(g.lat.median()), 5), 'lon': round(float(g.lon.median()), 5),
        'bbox': [round(float(g.lon.min()),4), round(float(g.lat.min()),4), round(float(g.lon.max()),4), round(float(g.lat.max()),4)],
    }
city_rows = []
for c, g in d.groupby('city'):
    a = agg(g); a.update({'name': c, 'slug': slug(c), 'country': g.country.iloc[0], 'districts': int(g.district.nunique()),
                          'districts200': int(g[g.height_m >= 200].district.nunique()), 'districts300': int(g[g.height_m >= 300].district.nunique())})
    city_rows.append(a)
# rank at each threshold by completed count, ties by name (the rule the site has always used for the
# 150 m rank). Cities with no completed tower at the threshold get 0 (unranked). Same rule as derive.mjs.
for key, field in (('completed', 'rank'), ('completed200', 'rank200'), ('completed300', 'rank300')):
    for i, c in enumerate(sorted(city_rows, key=lambda x: (-x[key], lc(x['name'])))):
        c[field] = i + 1 if c[key] > 0 else 0
city_rows.sort(key=lambda x: (x['rank'] == 0, x['rank'], lc(x['name'])))   # unranked last (same as derive.mjs)

dist_rows = []
for (c, dn), g in d.groupby(['city', 'district']):
    a = agg(g); a.update({'name': dn, 'city': c, 'city_slug': slug(c), 'slug': slug(dn), 'country': g.country.iloc[0]})
    dist_rows.append(a)
dist_rows.sort(key=lambda x: (-x['completed'], -x['count'], lc(x['city']), lc(x['name'])))   # same tie-breaks as derive.mjs
for i, x in enumerate(dist_rows): x['rank'] = i + 1
# guard: district slugs unique within a city
seen = set()
for x in dist_rows:
    k = (x['city_slug'], x['slug'])
    assert k not in seen, k
    seen.add(k)

places = {'cities': city_rows, 'districts': dist_rows,
          'totals': {'towers': int(len(d)), 'completed': int(len(comp)), 'cities': len(cities), 'districts': len(dist_keys),
                     'countries': int(d.country.nunique()), 'supertall': int((d.height_m >= 300).sum()),
                     'with_photo': int(sum(1 for r in rows if r[13]))}}

os.makedirs('public/data', exist_ok=True); os.makedirs('src/data', exist_ok=True)
for path in ('public/data/towers.json', 'src/data/towers.json'):
    json.dump(index, open(path, 'w'), ensure_ascii=False, separators=(',', ':'))
for path in ('public/data/details.json', 'src/data/details.json'):
    json.dump(details, open(path, 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(places, open('src/data/places.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(places, open('public/data/places.json', 'w'), ensure_ascii=False, separators=(',', ':'))

print('towers', len(rows), 'cities', len(cities), 'districts', len(dist_keys), 'photos', len(photos))
for f in ('public/data/towers.json', 'public/data/details.json', 'public/data/places.json'):
    print(f, os.path.getsize(f))
print('top districts (completed):', [(x['city'], x['name'], x['completed']) for x in dist_rows[:8]])
