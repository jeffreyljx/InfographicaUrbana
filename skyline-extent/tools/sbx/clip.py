import json,lzma,base64,math,os
from shapely.geometry import shape, box
from shapely.ops import unary_union, transform
from shapely import set_precision
import numpy as np
bb=json.load(open('../w/bboxes.json')); per={}
for key,b in bb.items():
    f=f'out/{key}.json'
    if not os.path.exists(f): print('missing',key); continue
    W=shape(json.load(open(f))['water'])
    if W.is_empty: continue
    lat0=(b[1]+b[3])/2; k=math.cos(math.radians(lat0))*111320.0; ky=110574.0
    fwd=lambda g: transform(lambda x,y,z=None:(np.asarray(x)*k,np.asarray(y)*ky),g)
    inv=lambda g: transform(lambda x,y,z=None:(np.asarray(x)/k,np.asarray(y)/ky),g)
    Wm=fwd(W).buffer(-35,8).buffer(35,8)
    ps=[p for p in (Wm.geoms if hasattr(Wm,'geoms') else [Wm]) if p.geom_type=='Polygon' and p.area>60000]
    if not ps: continue
    dx=400/k; dy=400/ky
    cl=inv(unary_union(ps)).intersection(box(b[0]-dx,b[1]-dy,b[2]+dx,b[3]+dy))
    if cl.is_empty: continue
    per.setdefault(key.split('|')[0],[]).append(cl)
out={}
for c,gs in per.items():
    g=set_precision(unary_union(gs).simplify(0.00005),0.00001)
    if not g.is_empty: out[c]=g.wkt
raw=json.dumps(out,ensure_ascii=False).encode()
x=lzma.compress(raw,preset=9|lzma.PRESET_EXTREME); b=base64.b64encode(x).decode()
open('w6.b64','w').write(b)
for i in range(0,len(b),1490): open(f'w6.{i//1490:03d}','w').write(b[i:i+1490])
print(len(out),'cities',len(raw),'raw',len(b),'b64',(len(b)+1489)//1490,'chunks')
