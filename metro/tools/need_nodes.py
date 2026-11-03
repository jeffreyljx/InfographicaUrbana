import json, glob
need=set()
nw=0
for f in glob.glob('/tmp/claude-0/ov/pbf/ways.*.jsonl'):
    for ln in open(f):
        w=json.loads(ln); need.update(w['nodes']); nw+=1
need|={n for n in json.load(open('/tmp/claude-0/ov/pbf/node_ids.json')) if n>0}
need|=set(json.load(open('/tmp/claude-0/ov/pbf/stoparea_node_ids.json')))
json.dump(sorted(need), open('/tmp/claude-0/ov/pbf/need_nodes.json','w'))
print('ways',nw,'nodes needed',len(need))
