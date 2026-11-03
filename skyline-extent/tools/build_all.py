import sys, json, importlib
sys.path.insert(0,'.')
from shapely.geometry import mapping
from lib.core import build, D
from rationale import R
cnt=D.groupby('city').size(); cities=[c for c in cnt[cnt>50].sort_values(ascending=False).index]
assert set(cities)==set(R), (set(cities)^set(R))
def rnd(o):
    if isinstance(o,(list,tuple)): return [rnd(x) for x in o]
    if isinstance(o,float): return round(o,5)
    return o
feats=[]; rows=[]
for c in cities:
    mod,rat=R[c]
    S=importlib.import_module('specs.'+mod).SPEC
    core,st,zones=build(c,S)
    g=mapping(core)
    g={'type':g['type'],'coordinates':rnd(g['coordinates'])}
    areas=[z['name'] for z in S['zones']]
    props={'city':c,'areas':areas,'rationale':rat,**st}
    feats.append({'type':'Feature','properties':props,'geometry':g})
    rows.append((c,st))
    print(f"{c:15s} {st['towers_in_core']:4d}/{st['towers_in_city']:4d} {st['share']:.2f} {st['area_km2']:6.2f} km2  parts={len(core.geoms) if hasattr(core,'geoms') else 1}  {st.get('tallest_in_core','')}")
fc={'type':'FeatureCollection','features':feats}
json.dump(fc,open('skyline-extent.geojson','w'),ensure_ascii=False,separators=(',',':'))
