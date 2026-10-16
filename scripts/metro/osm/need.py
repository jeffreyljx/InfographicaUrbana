# Node ids the kept ways and our stop areas need
import json, glob, sys, numpy as np
D=sys.argv[1]+'/data'
s=set(json.load(open(D+'/rel_node_ids.json')))
nw=0
for f in glob.glob(D+'/ways.*.jsonl'):
    for l in open(f):
        s.update(json.loads(l)['nodes']); nw+=1
a=np.array(sorted(s), dtype=np.int64); np.save(D+'/need_nodes.npy', a); print(nw, 'ways', len(a), 'nodes')
