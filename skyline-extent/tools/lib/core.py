import math, json
import numpy as np, pandas as pd
from shapely.geometry import Point, Polygon, MultiPolygon, shape, mapping
from shapely.ops import unary_union, transform
from shapely import prepared
from .geo import load
D=pd.read_csv('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv')
G=load()
class Proj:
    def __init__(s,lat0): s.k=math.cos(math.radians(lat0))*111320.0; s.ky=110574.0
    def fwd(s,g): return transform(lambda x,y,z=None:(np.asarray(x)*s.k,np.asarray(y)*s.ky),g)
    def inv(s,g): return transform(lambda x,y,z=None:(np.asarray(x)/s.k,np.asarray(y)/s.ky),g)
def parts(g):
    if g.is_empty: return []
    return [p for p in (g.geoms if hasattr(g,'geoms') else [g]) if p.geom_type=='Polygon']
def build(city, spec, R=280, C=450, smooth=70, min_towers=3):
    t=D[D.city==city]; e=G[city]; b=e['bbox']
    P=Proj((b[1]+b[3])/2)
    water=P.fwd(e['water']); park=P.fwd(e['park'])
    wo=spec.get('water_open',35)
    if wo: water=water.buffer(-wo,8).buffer(wo,8)
    water=unary_union([p for p in parts(water) if p.area>spec.get('water_min',60000)])
    pts=[(r.lon,r.lat) for r in t.itertuples()]
    zones=[]
    for z in spec['zones']:
        lasso=P.fwd(Polygon(z['poly']))
        if z.get('mode','towers')=='fill':
            g=lasso
            rd=z.get('round',0)
            if rd: g=g.buffer(-rd,16).buffer(rd,16)
        else:
            lp=prepared.prep(lasso)
            mp=[P.fwd(Point(p)) for p in pts]
            sel=[q for q in mp if lp.contains(q)]
            if not sel: continue
            r=z.get('R',R); c=z.get('C',C)
            g=unary_union([q.buffer(r,16) for q in sel]).buffer(c,16).buffer(-c,16)
            g=g.intersection(lasso.buffer(z.get('pad',0)))
            # drop parts with few towers
            keep=[]
            for p in parts(g):
                pp=prepared.prep(p)
                if sum(pp.contains(q) for q in sel)>=z.get('min',min_towers): keep.append(p)
            g=unary_union(keep) if keep else Polygon()
        zones.append((z['name'],g))
    U=unary_union([g for _,g in zones])
    if spec.get('fill_holes',True):
        U=unary_union([Polygon(p.exterior) for p in parts(U)])
    U=U.difference(water.buffer(5))
    for ex in spec.get('cut',[]):
        U=U.difference(P.fwd(Polygon(ex)))
    if spec.get('cut_parks'):
        big=[p for p in parts(park) if p.area>spec.get('park_min',300000)]
        if big: U=U.difference(unary_union(big))
    sm=spec.get('smooth',smooth)
    U=U.buffer(sm,8).buffer(-2*sm,8).buffer(sm,8)
    U=U.difference(water.buffer(5))
    if spec.get('fill_holes',True):
        U=unary_union([Polygon(p.exterior) for p in parts(U)]).difference(water.buffer(5))
        for ex in spec.get('cut',[]): U=U.difference(P.fwd(Polygon(ex)))
    U=unary_union([p for p in parts(U) if p.area>40000])
    U=U.simplify(12)
    out=P.inv(U)
    # stats
    op=prepared.prep(out)
    inside=t[[op.contains(Point(r.lon,r.lat)) for r in t.itertuples()]]
    st={'towers_in_core':int(len(inside)),'completed_in_core':int((inside.status=='Completed').sum()),
        'towers_in_city':int(len(t)),'share':round(len(inside)/len(t),3),
        'area_km2':round(U.area/1e6,2)}
    comp=inside[inside.status=='Completed']
    if len(comp):
        top=comp.sort_values('height_m',ascending=False).iloc[0]
        st['tallest_in_core']=f"{top['name']} ({top.height_m:.0f} m)"
    return out, st, [(n,P.inv(g)) for n,g in zones]
