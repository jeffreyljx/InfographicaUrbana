import json, math, sys, os, gzip, base64, io, tarfile, urllib.request, concurrent.futures as cf
import mapbox_vector_tile as mvt
from shapely.geometry import shape, box, mapping, Polygon, MultiPolygon, LineString, MultiLineString, Point
from shapely.ops import unary_union, linemerge
from shapely import set_precision
bb=json.load(open('bboxes.json'))
tj=json.load(urllib.request.urlopen(urllib.request.Request('https://tiles.openfreemap.org/planet',headers={'User-Agent':'scrapermap-skyline/1.0'})))
URL=tj['tiles'][0]
Z=13; N=2**Z
def tile(lon,lat):
    x=int((lon+180)/360*N); y=int((1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*N); return x,y
def tolonlat(tx,ty,px,py,ext):
    x=(tx+px/ext)/N; y=(ty+py/ext)/N
    lon=x*360-180; lat=math.degrees(math.atan(math.sinh(math.pi*(1-2*y)))); return (lon,lat)
def conv(coords,tx,ty,ext):
    if isinstance(coords[0],(int,float)): return tolonlat(tx,ty,coords[0],coords[1],ext)
    return [conv(c,tx,ty,ext) for c in coords]
def get(tx,ty):
    u=URL.format(z=Z,x=tx,y=ty)
    for i in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'scrapermap-skyline/1.0'}),timeout=30).read()
            if r[:2]==b'\x1f\x8b': r=gzip.decompress(r)
            return tx,ty,mvt.decode(r,default_options={'y_coord_down':True})
        except Exception as e:
            err=e
    print('FAIL',u,err,file=sys.stderr); return tx,ty,{}
only=sys.argv[1:]
os.makedirs('out',exist_ok=True)
for city,b in bb.items():
    if only and city not in only: continue
    if os.path.exists(f'out/{city}.json'): continue    # resume after a stop
    x0,y1=tile(b[0],b[1]); x1,y0=tile(b[2],b[3])
    jobs=[(x,y) for x in range(x0,x1+1) for y in range(y0,y1+1)]
    water=[];park=[];roads={};places={}
    with cf.ThreadPoolExecutor(12) as ex:
        for tx,ty,t in ex.map(lambda a:get(*a),jobs):
            for lname,L in t.items():
                ext=L.get('extent',4096)
                for f in L['features']:
                    g=f['geometry']; p=f['properties']
                    if lname=='water' and g['type'] in('Polygon','MultiPolygon'):
                        try: water.append(shape({'type':g['type'],'coordinates':conv(g['coordinates'],tx,ty,ext)}).buffer(0))
                        except Exception: pass
                    elif lname=='park' and g['type'] in('Polygon','MultiPolygon'):
                        try: park.append(shape({'type':g['type'],'coordinates':conv(g['coordinates'],tx,ty,ext)}).buffer(0))
                        except Exception: pass
                    elif lname=='transportation' and p.get('class') in ('motorway','trunk','primary') and g['type'] in ('LineString','MultiLineString'):
                        roads.setdefault(p['class'],[]).append(shape({'type':g['type'],'coordinates':conv(g['coordinates'],tx,ty,ext)}))
                    elif lname=='place' and p.get('class') in ('suburb','neighbourhood','quarter','city','town','village','island') and g['type']=='Point':
                        nm=p.get('name:en') or p.get('name_en') or p.get('name:latin') or p.get('name')
                        if nm: places[(nm,p['class'])]=conv(g['coordinates'],tx,ty,ext)
    clip=box(*b)
    W=unary_union(water).intersection(clip) if water else Polygon()
    W=W.simplify(0.00006)
    kmdeg=111.0**2*math.cos(math.radians((b[1]+b[3])/2))
    polys=[g for g in (W.geoms if hasattr(W,'geoms') else [W]) if g.geom_type=='Polygon' and g.area*kmdeg>0.01]
    W=MultiPolygon(polys) if polys else MultiPolygon()
    P=unary_union(park).intersection(clip) if park else Polygon()
    P=P.simplify(0.0001)
    pp=[g for g in (P.geoms if hasattr(P,'geoms') else [P]) if g.geom_type=='Polygon' and g.area*kmdeg>0.25]
    P=MultiPolygon(pp) if pp else MultiPolygon()
    R={}
    for k,ls in roads.items():
        try: m=linemerge(unary_union(ls)).intersection(clip).simplify(0.00015)
        except ValueError: continue                      # linemerge refuses a single straight segment; roads are optional
        R[k]=set_precision(m,0.0001)
    def rnd(g,q=0.00002): return mapping(set_precision(g,q))
    out={'bbox':b,'water':rnd(W),'park':rnd(P,0.0001),'roads':{k:mapping(v) for k,v in R.items()},
         'places':[[n,c,round(xy[0],4),round(xy[1],4)] for (n,c),xy in places.items()]}
    s=json.dumps(out,separators=(',',':'))
    open(f'out/{city}.json','w').write(s)
    print(city,len(jobs),'tiles','water',len(polys),'parks',len(pp),'places',len(places),'bytes',len(s),flush=True)
