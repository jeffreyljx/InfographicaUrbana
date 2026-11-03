import osmium, json, sys
KEEP_ROUTE={'subway','light_rail','train','monorail','tram'}
out=open('/tmp/claude-0/ov/pbf/rels.jsonl','w')
class H(osmium.SimpleHandler):
    def __init__(self): super().__init__(); self.n=0; self.k=0
    def relation(self, r):
        self.n+=1
        t=r.tags
        typ=t.get('type')
        keep=False
        if typ in('route','route_master') and t.get('route') in KEEP_ROUTE or t.get('route_master') in KEEP_ROUTE: keep=True
        if typ=='public_transport' and t.get('public_transport')=='stop_area': keep=True
        if typ=='multipolygon' and (t.get('public_transport')=='station' or t.get('railway')=='station'): keep=True
        if not keep: return
        self.k+=1
        out.write(json.dumps({'id':r.id,'tags':dict((x.k,x.v) for x in t),'members':[(m.type,m.ref,m.role) for m in r.members],'ts':str(r.timestamp)[:10]}, ensure_ascii=False)+'\n')
h=H(); h.apply_file('/tmp/claude-0/ov/pbf/relations.osm.pbf')
print(h.n, h.k)
