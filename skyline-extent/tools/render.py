import json, pickle, sys, math
import pandas as pd, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapely.geometry import shape
W=pickle.load(open('/home/claude/work/geo/water_by_city.pkl','rb'))
d=pd.read_csv('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv')
def draw_poly(ax,g,**kw):
    if g.is_empty: return
    for p in (g.geoms if hasattr(g,'geoms') else [g]):
        if p.geom_type!='Polygon': continue
        x,y=p.exterior.xy; ax.fill(x,y,**kw)
        for r in p.interiors:
            x,y=r.xy; ax.fill(x,y,color='white')
def render(city, bbox=None, cores=None, out=None, labels=False, grid=0.01):
    t=d[d.city==city]
    if bbox is None:
        bbox=json.load(open('bboxes.json'))[city]
    fig,ax=plt.subplots(figsize=(10,10),dpi=90)
    ax.set_facecolor('#f4efe9')
    for g in W[city]: draw_poly(ax,g,color='#a9c6d6',lw=0)
    if cores is not None:
        for g in cores:
            for p in (g.geoms if hasattr(g,'geoms') else [g]):
                x,y=p.exterior.xy; ax.fill(x,y,color='#e8a33d',alpha=0.25,lw=0); ax.plot(x,y,color='#c0392b',lw=1.6)
    c=np.where(t.height_m>=300,'#8b0000',np.where(t.height_m>=200,'#d35400','#1f6f78'))
    ax.scatter(t.lon,t.lat,s=np.where(t.height_m>=300,22,9),c=c,zorder=5,lw=0)
    if labels:
        for _,r in t[t.height_m>=250].iterrows():
            ax.text(r.lon,r.lat,r['name'][:18],fontsize=5.5,zorder=6)
    ax.set_xlim(bbox[0],bbox[2]); ax.set_ylim(bbox[1],bbox[3])
    ax.set_aspect(1/math.cos(math.radians((bbox[1]+bbox[3])/2)))
    xs=np.arange(math.floor(bbox[0]/grid)*grid,bbox[2],grid); ys=np.arange(math.floor(bbox[1]/grid)*grid,bbox[3],grid)
    ax.set_xticks(xs); ax.set_yticks(ys); ax.tick_params(labelsize=6); plt.xticks(rotation=90)
    ax.grid(color='#999',lw=0.3,alpha=0.5)
    ax.set_title(f"{city}: {len(t)} towers",fontsize=10)
    fig.tight_layout(); fig.savefig(out or f'render/{city}.png'); plt.close(fig)
if __name__=='__main__':
    for c in sys.argv[1:]: render(c)
