# Pick the relations that matter: stop areas of our stations (and their groups), and structure multipolygons
import json, csv, collections, sys
D=sys.argv[1]+'/data'
sa={int(r['osm_station'][2:]) for r in csv.DictReader(open('/mnt/project-files/metro/db/metro_stations.csv')) if r['osm_station'].startswith('sa')}
R={}
for l in open(D+'/rels.jsonl'):
    r=json.loads(l); R[r['id']]=r
groups=[r for r in R.values() if r['tags'].get('public_transport')=='stop_area_group']
keep=set(x for x in sa if x in R)
print('our stop areas', len(sa), 'found', len(keep))
for g in groups:
    mem={m[1] for m in g['members'] if m[0]=='r'}
    if mem & keep: keep |= {m for m in mem if m in R}; keep.add(g['id'])
print('with groups', len(keep))
mp=[r for r in R.values() if r['tags'].get('type') in ('multipolygon','building')]
c=collections.Counter()
for r in mp:
    t=r['tags']; c[(t.get('railway'),t.get('public_transport'),t.get('building'),'indoor' if 'indoor' in t else None)]+=1
print(len(mp)); print(c.most_common(15))
roles=collections.Counter(m[0]+':'+m[2] for i in keep for m in R[i]['members']); print(roles.most_common(20))
# nested member relations (platform multipolygons inside stop areas)
sel=set(keep)|{r['id'] for r in mp}
for i in list(keep):
    for m in R[i]['members']:
        if m[0]=='r' and m[1] in R: sel.add(m[1])
wid=set(); nid=set()
for i in sel:
    for m in R[i]['members']:
        if m[0]=='w': wid.add(m[1])
        elif m[0]=='n' and i in keep: nid.add(m[1])
json.dump(sorted(wid), open(D+'/rel_way_ids.json','w')); json.dump(sorted(nid), open(D+'/rel_node_ids.json','w'))
json.dump(sorted(keep), open(D+'/our_stop_areas.json','w'))
with open(D+'/rels_sel.jsonl','w') as f:
    for i in sorted(sel): f.write(json.dumps(R[i], ensure_ascii=False)+'\n')
print('relations kept', len(sel), 'member ways', len(wid), 'member nodes', len(nid))
