# Group kept OSM route relations into lines (route_master, else by network+ref/name)
import json, collections
rels={}
for ln in open('/tmp/claude-0/ov/pbf/rels.jsonl'):
    r=json.loads(ln); rels[r['id']]=r
keep=set(json.load(open('/tmp/claude-0/ov/pbf/route_ids.json')))
master_of={}
masters={}
for rid,r in rels.items():
    t=r['tags']
    if t.get('type')=='route_master':
        kids=[ref for typ,ref,role in r['members'] if typ=='r' and ref in keep]
        if kids:
            masters[rid]=kids
            for k in kids: master_of.setdefault(k, rid)
lines={}
for rid in keep:
    r=rels[rid]; t=r['tags']
    if rid in master_of:
        key=('m',master_of[rid])
    else:
        key=('g', t.get('route'), t.get('network',''), t.get('ref') or t.get('name',''))
    lines.setdefault(key, []).append(rid)
out=[]
for key,rids in lines.items():
    if key[0]=='m':
        mt=rels[key[1]]['tags']; lid=f"m{key[1]}"
    else:
        mt={}; lid=f"r{min(rids)}"
    ways=[];stops=[];platforms=[]
    variants=[]
    for rid in rids:
        r=rels[rid]
        w=[ref for typ,ref,role in r['members'] if typ=='w' and role in ('','forward','backward','route','main','alternative','track')]
        st=[(typ,ref,role) for typ,ref,role in r['members'] if role.startswith('stop') or role.startswith('platform')]
        variants.append({'rel':rid,'tags':r['tags'],'ways':w,'stops':st})
    t0=variants[0]['tags']
    def g(k): return mt.get(k) or next((v['tags'].get(k) for v in variants if v['tags'].get(k)), '')
    out.append({'osm_line':lid,'route':g('route_master') or g('route'),'network':g('network'),'operator':g('operator'),'ref':g('ref'),
        'name':g('name'),'name_en':g('name:en'),'colour':g('colour'),'wikidata':g('wikidata'),'wikipedia':g('wikipedia'),'start_date':g('start_date'),
        'master_tags':mt,'variants':variants})
json.dump(out, open('/tmp/claude-0/ov/osm_lines.json','w'), ensure_ascii=False)
print(len(out), sum(1 for o in out if o['osm_line'][0]=='m'))
c=collections.Counter(o['route'] for o in out); print(c)
print(sum(1 for o in out if o['wikidata']), 'with wikidata;', sum(1 for o in out if o['start_date']), 'with start_date')
