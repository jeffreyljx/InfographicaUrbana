# Extra pass: nodes tagged entrance=* (any value) within about 400 m of a page station, with their tags, to find
# exits that are not tagged railway=subway_entrance. Usage: ents.py DIR PART NP
import sys, json, os, time
sys.path.insert(0, sys.argv[1]); D=sys.argv[1]+'/data'
from pbf import *
import osmium
PART=int(sys.argv[2]); NP=int(sys.argv[3])
idx=json.load(open(sys.argv[1]+'/station_index.json'))
G=0.004  # grid cell in degrees; a node is kept when its cell or a neighbour holds a station
cells=set()
for rows in idx:
    for r in rows:
        cx,cy=int(r[1]//G),int(r[2]//G)
        for dx in (-1,0,1):
            for dy in (-1,0,1): cells.add((cx+dx,cy+dy))
bounds=json.load(open(D+'/node_bounds.json'))
H=header()
out=open(f'{D}/ents.{PART}.jsonl','a'); t0=time.time(); n=0
for k in range(len(bounds)-1):
    if k%NP!=PART: continue
    if os.path.exists(f'{D}/ents.{k}.done'): continue
    a,b=bounds[k],bounds[k+1]
    mid=align((a+b)//2)[0]
    for pa,pb in ([(a,mid),(mid,b)] if a<mid<b else [(a,b)]):
        buf=H+prng(pa,pb)
        for o in osmium.FileProcessor(osmium.io.FileBuffer(buf,'pbf'), osmium.osm.NODE).with_filter(osmium.filter.KeyFilter('entrance')):
            lon,lat=o.location.lon,o.location.lat
            if (int(lon//G),int(lat//G)) in cells:
                out.write(json.dumps({'id':o.id,'lon':lon,'lat':lat,'tags':{t.k:t.v for t in o.tags}}, ensure_ascii=False)+'\n'); n+=1
        del buf
    out.flush(); open(f'{D}/ents.{k}.done','w').close()
    print(k, n, round(time.time()-t0), flush=True)
out.close()
print('done', n, round(time.time()-t0), flush=True)
