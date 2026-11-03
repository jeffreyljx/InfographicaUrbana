"""Group the 348 cities into jobs: cities whose tower boxes (padded 20 km) overlap are built together."""
import json, math, pandas as pd, numpy as np
D = pd.read_csv('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv').dropna(subset=['lat', 'lon'])
PAD = 20
g = D.groupby('city').agg(n=('id', 'size'), lat0=('lat', 'min'), lat1=('lat', 'max'), lon0=('lon', 'min'), lon1=('lon', 'max'))
def box(r):
    km = PAD / 110.574; kx = PAD / (111.32 * math.cos(math.radians((r.lat0 + r.lat1) / 2)))
    return (r.lon0 - kx, r.lat0 - km, r.lon1 + kx, r.lat1 + km)
B = {c: box(r) for c, r in g.iterrows()}
parent = {c: c for c in B}
def find(x):
    while parent[x] != x: x = parent[x]
    return x
cs = list(B)
for i, a in enumerate(cs):
    for b in cs[i + 1:]:
        A, Bb = B[a], B[b]
        if A[0] <= Bb[2] and Bb[0] <= A[2] and A[1] <= Bb[3] and Bb[1] <= A[3]: parent[find(a)] = find(b)
groups = {}
for c in cs: groups.setdefault(find(c), []).append(c)
jobs = sorted(groups.values(), key=lambda j: -sum(g.n[c] for c in j))
for j in jobs: j.sort(key=lambda c: -g.n[c])
json.dump(jobs, open('jobs.json', 'w'), ensure_ascii=False, indent=0)
print(len(jobs), 'jobs;', sum(len(j) > 1 for j in jobs), 'with several cities')
for j in jobs[:25]: print(len(j), j[:8])
