"""Build src/data-gdp/gdp.json: city-limits GDP (from the research files) converted to nominal US$ and PPP intl$,
plus national GDP for the Countries table. Run: python3 scripts/gdp/build_gdp.py. rates.txt / countries.txt were pulled from the IMF SDMX API
(WEO April 2026; World Bank WDI for LKA/MCO/CUB). Conversion: IMF WEO April 2026 (implied exchange rate = NGDP/NGDPD,
price-level ratio = PPPGDP/NGDPD) for the figure's country and year."""
import json, glob
import os
D = os.path.dirname(os.path.abspath(__file__)) + '/'          # scripts/gdp/
S = D + 'research/'                                           # one JSON per research batch (see RULES.md, RULES2.md)
OUT = os.path.join(D, '..', '..', 'src', 'data-gdp', 'gdp.json')
iso = json.load(open(D + 'iso.json'))

def parse_pairs(path):
    out = {}
    for tok in open(path).read().replace('\n', ' ').split('|'):
        p = tok.split()
        if len(p) >= 3: out[p[0]] = (float(p[1]), float(p[2]))
    return out
R = parse_pairs(D + 'rates.txt')
R.update({'ECU2024': (1.0, 2.3216), 'KOR2023': (1305.66, 1.6875), 'ESP2023': (0.924573, 1.5623), 'PRY2024': (7560.25, 2.8857)})

recs = []
for g in ['A1', 'A2', 'B', 'C', 'D', 'E', 'F', 'G']:
    recs += json.load(open(S + f'out_{g}.json'))
by = {r['city']: r for r in recs}

def setv(city, **kw):
    r = by[city]; country = kw.pop('country', None) or r.get('country'); r.clear(); r.update(city=city, country=country, **kw)

# ---- gap fills done after the agent pass (official files read directly) ----
for city, kw in {
    'Manchester': dict(country='United Kingdom', value=3.9882e10, currency='GBP', year=2024, period='calendar', measure='GDP at current market prices',
                       area='Manchester local authority (E08000003)', coterminous='exact', source='ONS, Regional GDP by local authority 1998–2024, Table 5', confidence='high'),
    'Birmingham': dict(country='United Kingdom', value=4.1244e10, currency='GBP', year=2024, period='calendar', measure='GDP at current market prices',
                       area='Birmingham local authority (E08000025)', coterminous='exact', source='ONS, Regional GDP by local authority 1998–2024, Table 5', confidence='high'),
    'Guayaquil': dict(country='Ecuador', value=2.627788232e10, currency='USD', year=2024, period='calendar (provisional)', measure='Gross value added, current prices',
                      area='Cantón Guayaquil', coterminous='exact', source='Banco Central del Ecuador, cantonal accounts 2018–2024p', confidence='high'),
    'Bilbao': dict(country='Spain', value=1.425277e10, currency='EUR', year=2023, period='calendar', measure='GDP at current prices (PIB municipal)',
                   area='Municipality of Bilbao', coterminous='exact', source='Eustat, PIB por ámbitos territoriales', confidence='high'),
    'Cebu': dict(country='Philippines', value=4.104207663e11, currency='PHP', year=2025, period='calendar', measure='GDP at current prices',
                 area='City of Cebu (highly urbanized city)', coterminous='exact', source='PSA, GDP by Province and HUC (OpenSTAT)', confidence='high'),
    'Pohang': dict(country='South Korea', value=2.4938e13, currency='KRW', year=2023, period='calendar', measure='GRDP, nominal (지역내총생산)',
                   area='Pohang-si', coterminous='exact', source='Gyeongsangbuk-do, 시군단위 지역내총생산 2023', confidence='high'),
    'Asunción': dict(country='Paraguay', value=0.17 * 3.38237e14, currency='PYG', year=2024, period='calendar', measure='GDP, current prices',
                     area='Asunción (Capital district)', coterminous='exact', source='Banco Central del Paraguay, regional accounts 2024 (17.0% of national GDP)', confidence='medium',
                     notes='derived: BCP share of national GDP × national GDP'),
}.items():
    setv(city, **kw)

# ---- second pass (October 2026): newer figures for old entries (research/r2_STALE.json) ----
for r in json.load(open(S + 'r2_STALE.json')):
    if not r.get('newer'): continue
    note = None
    if r['city'] in ('Osaka', 'Kobe', 'Fukuoka'): note = 'prefecture’s estimate for the city (the city’s own series stops a year earlier)'
    if r['city'] == 'Kolkata': note = 'CMIE/KPMG estimate quoted by the West Bengal government (latest available)'
    setv(r['city'], value=r['value'], currency=r['currency'], year=r['year'], period=r.get('period') or 'calendar', measure=r.get('measure'),
         area=r.get('area'), coterminous='exact', source=r.get('source'), confidence='high', _note=note)

# ---- second pass: cities with no first-pass figure (research/r2_*.json, rules in research/RULES2.md) ----
# A city-limits figure ("strict") is used when one exists. Otherwise, as the site owner chose, the figure of the
# smallest official area that contains the city ("container") is shown, marked, with the city's population share.
AREA_LABEL = {
    'Toronto': 'Ontario (province)', 'Niagara Falls': 'Ontario (province)', 'Vancouver': 'British Columbia (province)', 'Kelowna': 'British Columbia (province)',
    'Calgary': 'Alberta (province)', 'Edmonton': 'Alberta (province)', 'Montreal': 'the island of Montréal (agglomeration)',
    'Panama City': 'Panamá Province', 'Monterrey': 'the state of Nuevo León', 'Guadalajara': 'the state of Jalisco', 'Puebla': 'the state of Puebla',
    'Querétaro': 'the state of Querétaro', 'Mérida': 'the state of Yucatán', 'León': 'the state of Guanajuato', 'Santiago': 'the Santiago Metropolitan Region',
    'La Paz': 'La Paz Department', 'Abu Dhabi': 'the emirate of Abu Dhabi', 'Sharjah': 'the emirate of Sharjah', 'Ras Al Khaimah': 'the emirate of Ras Al Khaimah',
    'Fujairah': 'the emirate of Fujairah', 'Erbil': 'the Kurdistan Region of Iraq', 'Sulaymaniyah': 'the Kurdistan Region of Iraq', 'Tehran': 'Tehran Province',
    'New Alamein City': 'Matrouh Governorate', 'Lagos': 'Lagos State', 'Salé': 'the Rabat-Salé-Kénitra region', 'Durban': 'KwaZulu-Natal (province)',
    'Johor Bahru': 'the state of Johor', 'Kota Kinabalu': 'the state of Sabah', 'Bentong': 'the state of Pahang', 'Colombo': 'Western Province',
    'Pattaya': 'Chonburi Province', 'Hyderabad': 'Hyderabad district', 'Bengaluru': 'Bengaluru Urban district', 'Lucknow': 'Lucknow district', 'Nha Trang': 'Khánh Hòa Province',
    'Ha Long': 'Quảng Ninh Province', 'Takamatsu': 'Kagawa Prefecture', 'Rotterdam': 'the Rijnmond area', 'Milan': 'the Metropolitan City of Milan',
    'Turin': 'the Metropolitan City of Turin', 'Lyon': 'the Rhône département (incl. the Métropole de Lyon)', 'Gdańsk': 'the Tricity subregion (Gdańsk, Gdynia, Sopot)',
    'Rzeszów': 'the Rzeszów subregion', 'Bratislava': 'the Bratislava Region', 'Seville': 'the province of Seville', 'Benidorm': 'the province of Alicante',
    'Batumi': 'Adjara (autonomous republic)', 'Yekaterinburg': 'Sverdlovsk Oblast', 'Athens': 'the Central Athens regional unit', 'Tirana': 'Tirana County',
}
SCOPE_NOTE = {  # areas that do not simply contain the city
    'Hyderabad': 'Figure for Hyderabad district, the core of the city (about 58% of its people); none is published for the whole city',
}
def add_area(city, country, value, currency, year, period, measure, label, share, source, multi=None):
    if city in SCOPE_NOTE: sn = SCOPE_NOTE[city]
    else:
        sn = f'Figure for {label}, the smallest area with a published GDP that contains {city}'
        if share: sn += f' ({city} has {round(share * 100)}% of its people' + (f'; {multi}' if multi else '') + ')'
        elif multi: sn += f' ({multi})'
    by[city] = dict(city=city, country=country, value=value, currency=currency, year=year, period=period or 'calendar', measure=measure,
                    area=label, source=source, _scope='area', _scope_note=sn)
    if not any(x['city'] == city for x in recs): recs.append(by[city])
    else:
        for i, x in enumerate(recs):
            if x['city'] == city: recs[i] = by[city]

for b in ['CA_AU', 'LATAM', 'GULF', 'MENA_AF', 'ASIA', 'EUROPE']:
    for r in json.load(open(S + f'r2_{b}.json')):
        st, ct = r.get('strict'), r.get('container')
        if st and st.get('value'):
            rec = dict(city=r['city'], country=r['country'], **{k: st.get(k) for k in ('value', 'currency', 'year', 'period', 'measure', 'area', 'coterminous', 'source')})
            if st.get('source_type') == 'city-published estimate': rec['_note'] = 'estimate published by the city'
            if r['city'] in by:
                for i, x in enumerate(recs):
                    if x['city'] == r['city']: recs[i] = rec
            else: recs.append(rec)
            by[r['city']] = rec
        elif ct and ct.get('value'):
            up, cp = ct.get('unit_population'), ct.get('city_population')
            share = cp / up if up and cp and cp < up else None
            add_area(r['city'], r['country'], ct['value'], ct['currency'], ct['year'], ct.get('period'), ct.get('measure'), AREA_LABEL[r['city']], share, ct.get('source'))

US = json.load(open(S + 'us_counties_2024.json'))
for r in US['rows']:
    multi = None
    if r['city_pop_in_county'] < r['city_pop'] * 0.995:
        multi = f"{round(100 * r['city_pop_in_county'] / r['city_pop'])}% of the city lies in this county"
    add_area(r['city'], 'United States', r['gdp_2024'], 'USD', 2024, 'calendar', 'GDP, current dollars', r['county'],
             r['city_pop_in_county'] / r['county_pop'], 'BEA, GDP by county 2024; Census Bureau population estimates 2024', multi)

# ---- owner's rule (2 Oct 2026): a stand-in figure may cover at most the city's metro area ----
# A province, state, emirate or region much larger than the metro (Ontario for Toronto, Jalisco for Guadalajara) is
# never used. Counties, districts and the like are kept, as are regions that are essentially the metro area
# (Santiago Metropolitan Region, Lagos State, Tehran Province, Colombo's Western Province, Nuevo León for Monterrey).
# Where a metro-area figure is published it replaces the oversized area; otherwise the city shows a dash.
TOO_BIG = ['Abu Dhabi', 'Batumi', 'Benidorm', 'Bentong', 'Durban', 'Erbil', 'Sulaymaniyah', 'Fujairah', 'Guadalajara', 'León',
           'Mérida', 'Puebla', 'Querétaro', 'Ha Long', 'Nha Trang', 'Johor Bahru', 'Kota Kinabalu', 'La Paz', 'New Alamein City',
           'Pattaya', 'Salé', 'Yekaterinburg', 'Toronto', 'Niagara Falls', 'Vancouver', 'Kelowna', 'Calgary', 'Edmonton']
for city in TOO_BIG:
    rec = dict(city=city, country=by[city]['country'], value=None)
    by[city] = rec
    for i, x in enumerate(recs):
        if x['city'] == city: recs[i] = rec
# Statistics Canada, table 36-10-0468-01: GDP at basic prices by census metropolitan area (CMA), current C$ millions,
# 2022 (latest year); city and CMA populations from the 2021 census.
for city, cma, gdp_m, city_pop, cma_pop in [
        ('Toronto', 'Toronto', 522379, 2794356, 6202225), ('Niagara Falls', 'St. Catharines–Niagara', 20359, 94415, 433604),
        ('Vancouver', 'Vancouver', 202459, 662248, 2642825), ('Kelowna', 'Kelowna', 13594, 144576, 222162),
        ('Calgary', 'Calgary', 129957, 1306784, 1481806), ('Edmonton', 'Edmonton', 103384, 1010899, 1418118)]:
    add_area(city, 'Canada', gdp_m * 1e6, 'CAD', 2022, 'calendar', 'GDP at basic prices, current dollars',
             f'the {cma} metro area (census metropolitan area)', city_pop / cma_pop,
             'Statistics Canada, table 36-10-0468-01 (GDP by CMA, 2022); 2021 census')
for city, extra in {'Monterrey': 'metro Monterrey has 92% of the state’s people, per the 2020 census',
                    'Colombo': 'the province is the official Colombo Metropolitan Region'}.items():
    by[city]['_scope_note'] = by[city]['_scope_note'][:-1] + '; ' + extra + ')'

NOTE = {  # short notes worth showing in the tooltip
    'Tokyo': 'Tokyo Metropolis; includes Hachioji', 'Ho Chi Minh City': 'territory after the July 2025 merger with Binh Duong and Ba Ria–Vung Tau',
    'Da Nang': 'territory after the July 2025 merger with Quang Nam', 'Kolkata': 'latest official district estimate',
    'Delhi': 'NCT of Delhi', 'Indianapolis': 'Marion County (also contains four small excluded towns)',
    'Jacksonville': 'Duval County (also contains four small beach towns)', 'Basel': 'canton Basel-Stadt (includes Riehen and Bettingen)',
    'Johannesburg': 'estimate published by the City (S&P Global)', 'Sydney': 'NIEIR estimate published by the council', 'Gold Coast': 'NIEIR estimate published by the council',
    'Penang': 'state of Penang', 'Malacca': 'state of Malacca', 'Dubai': 'emirate of Dubai', 'Asunción': 'derived from the central bank’s regional share',
    'Mumbai': 'Mumbai City + Mumbai Suburban districts (BMC area)', 'New York City': 'the five boroughs (counties)', 'Moscow': 'city government preliminary estimate',
    'St. Petersburg': 'city government preliminary estimate', 'Vladivostok': 'Rosstat pilot estimate of city GDP', 'Maebashi': 'latest year published by the prefecture',
}
EURO_FROM = {'Poland': 'DEU', 'Serbia': 'DEU', 'Monaco': 'FRA'}

def iso_of(r):
    if r['city'] == 'Hong Kong': return 'HKG'
    if r['city'] == 'Macau': return 'MAC'
    return iso[r['country']]

cities, problems = {}, []
for r in recs:
    v = r.get('value')
    if not v: cities[r['city']] = None; continue
    c, y, cur = iso_of(r), int(r['year']), r['currency']
    key = f'{c}{y}'
    if cur == 'EUR' and r['country'] in EURO_FROM:
        xr = R[f"{EURO_FROM[r['country']]}{y}"][0]
        P = R.get(key, (None, None))[1] if r['country'] != 'Monaco' else None
    elif cur == 'USD':
        xr = 1.0; P = R[key][1] if key in R else (1.0 if c == 'USA' else None)
    else:
        if key not in R: problems.append((r['city'], key)); continue
        xr, P = R[key]
    usd = v / xr
    ppp = usd * P if P else None
    per = r.get('period') or 'calendar'
    cities[r['city']] = dict(usd=round(usd, -5), ppp=round(ppp, -5) if ppp else None, year=y, lcu=v, cur=cur,
                             period=None if per.startswith('calendar') else per,
                             measure=(r.get('measure') or 'GDP')[:70], area=(r.get('area') or '')[:90],
                             src=(r.get('source') or '')[:120], note=r.get('_note') or NOTE.get(r['city']))
    if r.get('_scope') == 'area':
        cities[r['city']].update(scope='area', scope_note=r['_scope_note'])
print('problems', problems)

# ---- countries: IMF WEO April 2026 (2025); World Bank where the WEO has no 2025 figure ----
cty = {}
for tok in open(D + 'countries.txt').read().split('|'):
    p = tok.split()
    if not p: continue
    wb = p[0].startswith('WB:'); code = p[0][3:] if wb else p[0]
    c, y = code[:3], int(code[3:])
    if c in cty and not wb: continue
    if c == 'LKA' and not wb: continue          # IMF has no 2025 for Sri Lanka; use the World Bank's
    cty[c] = dict(usd=float(p[1]) * 1e9, ppp=float(p[2]) * 1e9 or None, year=y, src='World Bank WDI (July 2026)' if wb else 'IMF World Economic Outlook, April 2026')
countries = {}
for name, c in iso.items():
    if name == 'China':
        parts = [cty['CHN'], cty['HKG'], cty['MAC']]
        countries[name] = dict(usd=sum(x['usd'] for x in parts), ppp=sum(x['ppp'] for x in parts), year=2025,
                               src='IMF World Economic Outlook, April 2026', note='mainland China + Hong Kong + Macau')
    elif c in cty:
        countries[name] = dict(cty[c])
    else:
        countries[name] = None
meta = dict(cities_source='official city-limits statistics, researched October 2026 (see method page)', conversion='IMF WEO April 2026: implied exchange rate (NGDP/NGDPD) and PPP ratio (PPPGDP/NGDPD) of the figure’s country and year',
            updated='2026-10-02')
json.dump(dict(meta=meta, cities=cities, countries=countries), open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
n = sum(1 for v in cities.values() if v)
print('cities with GDP', n, 'of', len(cities), '| countries', sum(1 for v in countries.values() if v), 'of', len(countries))
top = sorted(((v['usd'], k, v['year'], v['ppp']) for k, v in cities.items() if v), reverse=True)
for u, k, y, p in top[:25]: print(f'{k:20} {u/1e9:8.1f}B  ppp {p/1e9 if p else 0:8.1f}B  {y}')
print('...')
for u, k, y, p in top[-8:]: print(f'{k:20} {u/1e9:8.2f}B  ppp {p/1e9 if p else 0:8.2f}B  {y}')
