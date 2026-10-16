# Nodes pass: stream the nodes section in blob-aligned ~1 GB chunks; keep the coordinates of every node the kept
# ways and stop areas need (need_nodes.npy), and every entrance node with its tags. Usage: nodes.py DIR PART NP
import sys, json, os, time
sys.path.insert(0, sys.argv[1]); D=sys.argv[1]+'/data'
from pbf import *
import osmium, numpy as np
PART=int(sys.argv[2]); NP=int(sys.argv[3])
need=np.load(D+'/need_nodes.npy')
flt=osmium.filter.IdFilter(need.tolist()); del need
ENT=[('railway','subway_entrance'),('railway','train_station_entrance'),('public_transport','entrance'),('railway','subway_station_entrance')]
bounds=json.load(open(D+'/node_bounds.json'))
H=header()
tagged=open(f'{D}/nodes.{PART}.jsonl','w'); t0=time.time(); nfound=0; nent=0
for k in range(len(bounds)-1):
    if k%NP!=PART: continue
    if os.path.exists(f'{D}/nxy.{k}.npy'): continue
    a,b=bounds[k],bounds[k+1]
    buf=H+prng(a,b)
    ids=[]; xs=[]; ys=[]
    for o in osmium.FileProcessor(osmium.io.FileBuffer(buf,'pbf'), osmium.osm.NODE).with_filter(flt):
        ids.append(o.id); xs.append(o.location.x); ys.append(o.location.y)
        if len(o.tags):
            tagged.write(json.dumps({'id':o.id,'lon':o.location.lon,'lat':o.location.lat,'tags':{t.k:t.v for t in o.tags}}, ensure_ascii=False)+'\n')
    for o in osmium.FileProcessor(osmium.io.FileBuffer(buf,'pbf'), osmium.osm.NODE).with_filter(osmium.filter.TagFilter(*ENT)):
        tagged.write(json.dumps({'id':o.id,'lon':o.location.lon,'lat':o.location.lat,'tags':{t.k:t.v for t in o.tags},'ent':1}, ensure_ascii=False)+'\n'); nent+=1
    del buf
    np.save(f'{D}/nxy.{k}.npy', np.array([ids, xs, ys], dtype=np.int64))
    nfound+=len(ids); tagged.flush()
    print(k, a, nfound, nent, round(time.time()-t0), flush=True)
tagged.close()
print('done', nfound, nent, round(time.time()-t0), flush=True)
