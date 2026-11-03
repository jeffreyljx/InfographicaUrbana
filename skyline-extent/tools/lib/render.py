import math, numpy as np, warnings
warnings.filterwarnings('ignore')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .core import D,G,parts
def fillg(ax,g,**kw):
    for p in parts(g):
        x,y=p.exterior.xy; ax.fill(x,y,**kw)
        for r in p.interiors:
            x,y=r.xy; ax.fill(x,y,color='#f4efe9',lw=0)
def render(city,core=None,zones=None,bbox=None,out=None,size=9,dpi=110,labels=True,grid=0.01,lassos=None,dlabels=True):
    t=D[D.city==city]; e=G[city]; bbox=bbox or e['bbox']
    fig,ax=plt.subplots(figsize=(size,size),dpi=dpi); ax.set_facecolor('#f4efe9')
    fillg(ax,e['park'],color='#d5e4c3',lw=0)
    fillg(ax,e['water'],color='#a9c6d6',lw=0)
    if core is not None:
        for p in parts(core):
            x,y=p.exterior.xy; ax.fill(x,y,color='#e8a33d',alpha=0.28,lw=0); ax.plot(x,y,color='#b42318',lw=1.4)
            for r in p.interiors:
                x,y=r.xy; ax.plot(x,y,color='#b42318',lw=0.8)
    if lassos:
        for L in lassos:
            x,y=zip(*(L+[L[0]])); ax.plot(x,y,color='#5b2c83',lw=0.7,ls='--')
    c=np.where(t.height_m>=300,'#8b0000',np.where(t.height_m>=200,'#d35400','#1f6f78'))
    ax.scatter(t.lon,t.lat,s=np.where(t.height_m>=300,18,7),c=c,zorder=5,lw=0)
    if labels:
        for n,cl,x,y in e['places']:
            if bbox[0]<x<bbox[2] and bbox[1]<y<bbox[3] and cl in ('suburb','quarter','neighbourhood','town','city','island'):
                ax.text(x,y,n[:22],fontsize=5.2 if cl!='city' else 7,color='#555' if cl!='city' else '#000',ha='center',zorder=6)
    if dlabels:
        for dn,s_ in t.groupby('district'):
            x,y=s_.lon.median(),s_.lat.median()
            if bbox[0]<x<bbox[2] and bbox[1]<y<bbox[3]:
                ax.text(x,y,f"{dn} ({len(s_)})",fontsize=6.5,color='#3b1f6b',weight='bold',ha='center',va='bottom',zorder=7,alpha=0.85)
    ax.set_xlim(bbox[0],bbox[2]); ax.set_ylim(bbox[1],bbox[3])
    ax.set_aspect(1/math.cos(math.radians((bbox[1]+bbox[3])/2)))
    xs=np.arange(math.floor(bbox[0]/grid)*grid,bbox[2],grid); ys=np.arange(math.floor(bbox[1]/grid)*grid,bbox[3],grid)
    ax.set_xticks(xs); ax.set_yticks(ys); ax.tick_params(labelsize=5); plt.xticks(rotation=90)
    ax.grid(color='#999',lw=0.3,alpha=0.5)
    ax.set_title(f"{city}: {len(t)} towers",fontsize=9)
    fig.tight_layout(); fig.savefig(out or f'render/{city}.png'); plt.close(fig)
