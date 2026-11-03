import pandas as pd, numpy as np, sys
from sklearn.cluster import DBSCAN
d=pd.read_csv('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv')
cnt=d.groupby('city').size()
cities=[c for c in cnt[cnt>50].sort_values(ascending=False).index]
sel=sys.argv[1:] or cities
for c in sel:
    t=d[d.city==c].copy()
    lat0=t.lat.median(); 
    X=np.c_[(t.lon-t.lon.median())*111.32*np.cos(np.radians(lat0)), (t.lat-lat0)*110.57]
    lab=DBSCAN(eps=0.8,min_samples=4).fit(X).labels_
    t['cl']=lab
    print(f"\n=== {c}  n={len(t)} completed={sum(t.status=='Completed')}")
    g=t.groupby('cl')
    rows=[]
    for k,s in g:
        rows.append((len(s),k,s))
    rows.sort(key=lambda r:-r[0])
    for n,k,s in rows:
        if k==-1:
            print(f"  noise: {n} towers; districts: {dict(s.district.value_counts().head(8))}")
            continue
        top=s.sort_values('height_m',ascending=False).name.head(3).tolist()
        sa=s.sub_area.dropna().value_counts().head(4).to_dict()
        print(f"  C{k}: n={n} ctr=({s.lat.mean():.4f},{s.lon.mean():.4f}) bbox=[{s.lon.min():.3f},{s.lat.min():.3f},{s.lon.max():.3f},{s.lat.max():.3f}] maxh={s.height_m.max():.0f} dist={dict(s.district.value_counts().head(4))} sub={sa} top={top}")
