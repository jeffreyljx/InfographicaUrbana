# Coverage and sanity checks on a built database folder
import csv, sys, collections, json
DB = sys.argv[1]
L = list(csv.DictReader(open(f'{DB}/metro_lines.csv', encoding='utf8')))
S = list(csv.DictReader(open(f'{DB}/metro_systems.csv', encoding='utf8')))
inc = [l for l in L if l['included'] == 'yes']
openl = [l for l in inc if not l['closed']]
def cov(rows, f):
    return sum(1 for r in rows if r[f].strip())
print('systems', len(S), 'with included lines', sum(1 for s in S if int(s['lines_included'] or 0) > 0))
print('lines', len(L), 'included', len(inc), 'open', len(openl), 'closed', len(inc) - len(openl))
for f in ['length_km', 'opened', 'stations', 'annual_ridership_m', 'ridership_daily_k', 'rolling_stock', 'car_type', 'cars_per_train', 'gauge_mm', 'power_supply', 'colour_hex', 'length_km_osm']:
    print(f'  {f:20s} {cov(inc, f):4d}/{len(inc)}')
rid = sum(1 for r in inc if r['annual_ridership_m'].strip() or r['ridership_daily_k'].strip())
print('  ridership (annual or daily)', rid)
geo = collections.Counter(l['geometry_status'] for l in inc)
print('geometry', dict(geo))
print('open lines with path', sum(1 for l in openl if l['geometry_status'].startswith('ok')), '/', len(openl))
bad = []
for l in inc:
    try:
        a, b = float(l['length_km']), float(l['length_km_osm'])
    except ValueError:
        continue
    if a > 3 and (b / a > 1.6 or b / a < 0.6):
        bad.append((round(b / a, 2), l['line_id'], a, b))
print('length mismatches (osm/published outside 0.6-1.6):', len(bad))
for x in sorted(bad)[:15] + sorted(bad)[-15:]:
    print('  ', x)
