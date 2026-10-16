# Ways pass: stream the ways section in blob-aligned ~1 GB chunks and keep station structure candidates:
# platforms, station and concourse areas, indoor areas and corridors, underground footways, entrances, and every way
# that a kept relation names as a member. Usage: ways.py DIR PART NP
import sys, json, os, time
sys.path.insert(0, sys.argv[1]); D=sys.argv[1]+'/data'
from pbf import *
import osmium
FIRST_WAY=63987482956; FIRST_REL=94485119388
PART=int(sys.argv[2]); NP=int(sys.argv[3])
want=set(json.load(open(D+'/rel_way_ids.json')))
TAGS=[('railway','platform'),('public_transport','platform'),('public_transport','station'),('railway','station'),('railway','halt'),
      ('building','train_station'),('railway','subway_entrance'),('railway','train_station_entrance'),('public_transport','entrance'),
      ('highway','corridor'),('highway','elevator'),('indoor','corridor'),('indoor','area'),('indoor','room'),('indoor','yes'),('indoor','level'),
      ('tunnel','yes'),('tunnel','building_passage'),('location','underground'),('station','subway'),('subway','yes'),('railway','traverser'),
      ('layer','-1'),('layer','-2'),('layer','-3'),('layer','-4'),('layer','-5'),
      ('level','-1'),('level','-2'),('level','-3'),('level','-4'),('level','-1;0'),('level','-2;-1'),('level','0;-1'),('level','-1;-2')]
FOOT={'footway','steps','corridor','path','pedestrian','elevator','platform','service'}
def keep(t):
    r=t.get('railway'); pt=t.get('public_transport'); hw=t.get('highway')
    if r in ('platform','station','halt','subway_entrance','train_station_entrance') or pt in ('platform','station','entrance'): return True
    if t.get('building')=='train_station' or t.get('station')=='subway' or t.get('subway')=='yes': return True
    if 'indoor' in t: return True
    if hw in FOOT:
        if hw in ('corridor','elevator'): return True
        if t.get('tunnel') in ('yes','building_passage') or t.get('location')=='underground': return True
        if t.get('layer','0').startswith('-') or t.get('level','0').startswith('-'): return True
    return False
bounds=json.load(open(D+'/way_bounds.json'))
H=header()
out=open(f'{D}/ways.{PART}.jsonl','w'); found=0; t0=time.time()
for k in range(len(bounds)-1):
    if k%NP!=PART: continue
    a,b=bounds[k],bounds[k+1]
    buf=H+prng(a,b)
    seen=set()
    for o in osmium.FileProcessor(osmium.io.FileBuffer(buf,'pbf'), osmium.osm.WAY).with_filter(osmium.filter.TagFilter(*TAGS)):
        t={x.k:x.v for x in o.tags}
        if keep(t) or o.id in want:
            out.write(json.dumps({'id':o.id,'nodes':[n.ref for n in o.nodes],'tags':t}, ensure_ascii=False)+'\n'); found+=1; seen.add(o.id)
    if want:
        for o in osmium.FileProcessor(osmium.io.FileBuffer(buf,'pbf'), osmium.osm.WAY).with_filter(osmium.filter.IdFilter(want)):
            if o.id in seen: continue
            out.write(json.dumps({'id':o.id,'nodes':[n.ref for n in o.nodes],'tags':{x.k:x.v for x in o.tags}}, ensure_ascii=False)+'\n'); found+=1
    del buf
    out.flush()
    print(k, a, found, round(time.time()-t0), flush=True)
out.close()
print('done', found, round(time.time()-t0), flush=True)
