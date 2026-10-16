# Relations pass: download the relations section once, keep stop areas and station / platform / indoor multipolygons
import sys, json, os, time
sys.path.insert(0, sys.argv[1]); D=sys.argv[1]+'/data'
from pbf import *
import osmium
FIRST_REL=94485119388
p=D+'/relations.osm.pbf'
if not os.path.exists(p):
    t=time.time(); H=header(); body=prng(FIRST_REL, SIZE)
    open(p,'wb').write(H+body); print('downloaded', len(body), round(time.time()-t), flush=True)
out=open(D+'/rels.jsonl','w'); n=k=0
for r in osmium.FileProcessor(p, osmium.osm.RELATION):
    n+=1; t=r.tags
    typ=t.get('type'); keep=False
    if t.get('public_transport') in ('stop_area','stop_area_group'): keep=True
    elif typ in ('multipolygon','building'):
        if t.get('railway') in ('station','platform','subway_entrance','train_station_entrance') or t.get('public_transport') in ('station','platform') \
           or t.get('building') in ('train_station','transportation') or 'indoor' in t or t.get('highway') in ('platform','pedestrian','footway','corridor') \
           or t.get('station')=='subway' or t.get('subway')=='yes' or t.get('layer','0').startswith('-') or t.get('level','0').startswith('-'):
            keep=True
    if not keep: continue
    k+=1
    out.write(json.dumps({'id':r.id,'tags':{x.k:x.v for x in t},'members':[(m.type,m.ref,m.role) for m in r.members]}, ensure_ascii=False)+'\n')
out.close(); print('relations', n, 'kept', k, flush=True)
