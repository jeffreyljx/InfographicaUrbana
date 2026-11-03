# Build per-OSM-line track geometry (one direction plus branches), lengths and ordered stations from planet ways/nodes
import json, glob, os, math, collections
import pyarrow.parquet as pq
from shapely import wkb
OV='/tmp/claude-0/ov'
lines=json.load(open(f'{OV}/osm_lines.json'))
ways={}
for f in glob.glob(f'{OV}/pbf/ways.*.jsonl'):
    for ln in open(f):
        w=json.loads(ln); ways[w['id']]=w
nodes={}
for f in glob.glob(f'{OV}/pbf/nodes.*.jsonl'):
    for ln in open(f):
        n=json.loads(ln); nodes[n['id']]=n
plat={}
for f in sorted(glob.glob(f'{OV}/p3/*.parquet')):
    if os.path.getsize(f)==0: continue
    t=pq.read_table(f, columns=['osm_ref','geometry','names','source_tags'])
    for ref,g,nm,st in zip(*[t[k].to_pylist() for k in ['osm_ref','geometry','names','source_tags']]):
        if ref.startswith('w'):
            p=wkb.loads(g).representative_point(); tags=dict(st) if st else {}
            plat[int(ref[1:])]={'lon':p.x,'lat':p.y,'tags':tags}
stopareas={}
for ln in open(f'{OV}/pbf/rels.jsonl'):
    r=json.loads(ln)
    if r['tags'].get('public_transport')=='stop_area': stopareas[r['id']]=r
sa_of={}; sa_station={}
for rid,r in stopareas.items():
    st=None
    for typ,ref,role in r['members']:
        sa_of.setdefault((typ,ref), rid)
        if typ=='n' and ref in nodes and st is None:
            tg=nodes[ref]['tags']
            if tg.get('public_transport')=='station' or tg.get('railway') in('station','halt'): st=ref
    sa_station[rid]=st
def seglen(c):
    t=0
    for (x1,y1),(x2,y2) in zip(c,c[1:]):
        p=math.radians((y1+y2)/2); t+=math.hypot((x2-x1)*111.32*math.cos(p),(y2-y1)*110.57)
    return t
wgeom={}; wlen={}
for wid,w in ways.items():
    c=[(nodes[n]['lon'],nodes[n]['lat']) for n in w['nodes'] if n in nodes]
    if len(c)>=2: wgeom[wid]=c; wlen[wid]=seglen(c)
def ninfo(n):
    x=nodes[n]; tg=x['tags']
    return {'lon':round(x['lon'],6),'lat':round(x['lat'],6),'name':tg.get('name',''),'name_en':tg.get('name:en',''),'wikidata':tg.get('wikidata',''),'start_date':tg.get('start_date','')}
def station_of(typ,ref):
    sa=sa_of.get((typ,ref))
    if sa is not None:
        st=sa_station.get(sa); satags=stopareas[sa]['tags']
        if st is not None:
            d=ninfo(st); d['name']=d['name'] or satags.get('name',''); d['name_en']=d['name_en'] or satags.get('name:en','')
            return 'sa%d'%sa, d|{'osm_station_node':st}
        base={'name':satags.get('name',''),'name_en':satags.get('name:en',''),'wikidata':satags.get('wikidata',''),'start_date':''}
        if typ=='n' and ref in nodes: d=ninfo(ref); d['name']=base['name'] or d['name']; return 'sa%d'%sa, d
        if typ=='w' and ref in plat: return 'sa%d'%sa, base|{'lon':round(plat[ref]['lon'],6),'lat':round(plat[ref]['lat'],6)}
        return 'sa%d'%sa, base|{'lon':None,'lat':None}
    if typ=='n' and ref in nodes: return 'n%d'%ref, ninfo(ref)
    if typ=='w' and ref in plat:
        tg=plat[ref]['tags']; return 'w%d'%ref, {'lon':round(plat[ref]['lon'],6),'lat':round(plat[ref]['lat'],6),'name':tg.get('name',''),'name_en':tg.get('name:en',''),'wikidata':'','start_date':''}
    return '%s%d'%(typ,ref), {'lon':None,'lat':None,'name':'','name_en':'','wikidata':'','start_date':''}
TRACK={'','forward','backward','route','main','alternative','track'}
out=[]; miss=0; tot=0
for L in lines:
    vs=[]
    for v in L['variants']:
        sts=[]; seen=set()
        for typ,ref,role in v['stops']:
            k,d=station_of(typ,ref)
            # merge consecutive stop/platform pairs that resolve to the same place by name when no stop area
            if k in seen: continue
            if sts and d['name'] and sts[-1][1]['name']==d['name'] and not k.startswith('sa'): continue
            seen.add(k); sts.append((k,d))
        vs.append((v,sts))
    vs.sort(key=lambda x:(-len(x[1]), -sum(wlen.get(w,0) for w in x[0]['ways'])))
    chosen=[]; covered=set()
    for v,sts in vs:
        ids={k for k,_ in sts}
        if not chosen: chosen.append((v,sts)); covered|=ids; continue
        if ids and ids<=covered: continue
        if not ids: continue
        chosen.append((v,sts)); covered|=ids
    if not chosen and vs: chosen=[vs[0]]
    wl=[]; 
    for v,sts in chosen:
        for w in v['ways']:
            tot+=1
            if w not in wgeom: miss+=1; continue
            if w not in wl: wl.append(w)
    vlen=max([sum(wlen.get(w,0) for w in dict.fromkeys(v['ways'])) for v,_ in chosen] or [0])
    tl=sum(wlen[w] for w in wl) or 1
    tun=sum(wlen[w] for w in wl if ways[w]['tags'].get('tunnel') in ('yes','building_passage') or (ways[w]['tags'].get('layer','0').lstrip('-').isdigit() and int(ways[w]['tags'].get('layer','0'))<0 and ways[w]['tags'].get('tunnel')))
    brg=sum(wlen[w] for w in wl if ways[w]['tags'].get('bridge') in ('yes','viaduct'))
    sd=sorted({ways[w]['tags'].get('start_date') for w in wl if ways[w]['tags'].get('start_date')})
    stations=[]; sid=set()
    for v,sts in chosen:
        for k,d in sts:
            if k in sid: continue
            sid.add(k); stations.append({'osm_station':k,**d,'osm_route':v['rel']})
    out.append({k:L[k] for k in ['osm_line','route','network','operator','ref','name','name_en','colour','wikidata','wikipedia','start_date']} | {
        'variants_used':[v['rel'] for v,_ in chosen],'n_variants':len(L['variants']),'n_ways':len(wl),
        'ways_missing':sum(1 for v,_ in chosen for w in v['ways'] if w not in wgeom),
        'length_km_osm':round(vlen,2),'track_km_mapped':round(tl,2),'tunnel_share':round(tun/tl,2),'bridge_share':round(brg/tl,2),
        'way_start_dates':sd,'stations':stations,'variant_seq':{str(v['rel']):[k for k,_ in sts] for v,sts in chosen},
        'geometry':{'type':'MultiLineString','coordinates':[[ [round(x,6),round(y,6)] for x,y in wgeom[w]] for w in wl]} if wl else None})
json.dump(out, open(f'{OV}/osm_lines_built.json','w'), ensure_ascii=False)
print('lines',len(out),'way refs missing',miss,'of',tot,'stations',sum(len(o['stations']) for o in out),'no coords',sum(1 for o in out for s in o['stations'] if s['lon'] is None))
