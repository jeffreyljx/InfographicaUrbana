import json, pickle, os, math
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
from shapely import make_valid
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
PK=os.path.join(ROOT,'geo_cache.pkl')
def _ring(r,s):
    pts=[]; x=y=0
    for i in range(0,len(r),2):
        x+=r[i]; y+=r[i+1]; pts.append((x/s,y/s))
    return pts
def _poly(rings,s):
    rr=[_ring(r,s) for r in rings]
    rr=[r for r in rr if len(r)>=4]
    if not rr: return None
    p=Polygon(rr[0],rr[1:])
    if not p.is_valid: p=make_valid(p)
    return p
def _old(g,s):
    t,c=g
    if t=='P': ps=[_poly(c,s)]
    elif t=='M': ps=[_poly(p,s) for p in c]
    else: ps=[]
    ps=[p for p in ps if p is not None and not p.is_empty]
    return unary_union(ps) if ps else MultiPolygon()
def _new(c,s=1e4):
    ps=[_poly(p,s) for p in c]; ps=[p for p in ps if p is not None and not p.is_empty]
    return unary_union(ps) if ps else MultiPolygon()
def load():
    if os.path.exists(PK): return pickle.load(open(PK,'rb'))
    J=json.load(open(os.path.join(ROOT,'geo_all.json')))
    out={}
    for c,e in J['old'].items():
        out[c]={'bbox':e['bbox'],'water':_old(e['water'],1e5),'park':_old(e['park'],1e4),'places':e.get('places',[])}
    for c,e in J['new'].items():
        out[c]={'bbox':e['bbox'],'water':_new(e['water']),'park':_new(e['park']),'places':e.get('places',[])}
    pickle.dump(out,open(PK,'wb')); return out
if __name__=='__main__':
    G=load()
    for c,e in sorted(G.items()):
        print(c, e['water'].geom_type, round(e['water'].area,5), 'parks',round(e['park'].area,5), 'places',len(e['places']))
