# Stream a section of the planet PBF in blob-aligned ~1 GB chunks; keep only wanted ways (pass 'ways') or nodes (pass 'nodes')
import urllib.request, struct, zlib, sys, json, time, concurrent.futures as cf, osmium, os
URL='https://osm-pds.s3.amazonaws.com/planet-latest.osm.pbf'
SIZE=95244184503; FIRST_WAY=63895028622; FIRST_REL=94351246300
mode=sys.argv[1]; PART=int(sys.argv[2]); NP=int(sys.argv[3])
def rng(a,b):
    for k in range(6):
        try:
            req=urllib.request.Request(URL, headers={'Range':f'bytes={a}-{b-1}'})
            d=urllib.request.urlopen(req, timeout=300).read()
            if len(d)==b-a: return d
        except Exception as e: pass
        time.sleep(2**k)
    raise RuntimeError(f'range {a}-{b}')
def prng(a,b,parts=8):
    step=(b-a+parts-1)//parts
    with cf.ThreadPoolExecutor(parts) as ex:
        return b''.join(ex.map(lambda x: rng(x, min(x+step,b)), range(a,b,step)))
def varint(b,i):
    s=0;r=0
    while True:
        x=b[i]; r|=(x&0x7f)<<s; i+=1; s+=7
        if x<0x80: return r,i
def hdr_ok(buf,p):
    hl=struct.unpack('>I',buf[p-4:p])[0]
    if not 8<=hl<64: return None
    i=p; end=p+hl; typ=None; ds=None
    try:
        while i<end:
            k,i=varint(buf,i); f=k>>3; w=k&7
            if w==2:
                l,i=varint(buf,i); v=buf[i:i+l]; i+=l
                if f==1: typ=v
            elif w==0:
                v,i=varint(buf,i)
                if f==3: ds=v
            else: return None
    except Exception: return None
    if typ==b'OSMData' and ds and ds<64_000_000: return hl,ds
    return None
def align(off):
    w=4_000_000
    while True:
        buf=rng(off, min(off+w,SIZE)); j=0
        while True:
            p=buf.find(b'\x0a\x07OSMData', j)
            if p<0: break
            if p>=4:
                r=hdr_ok(buf,p)
                if r:
                    hl,ds=r; nxt=p+hl+ds
                    if nxt+13>len(buf) or buf[nxt+4:nxt+13]==b'\x0a\x07OSMData': return off+p-4
            j=p+1
        w*=4
h=rng(0,100000); hl=struct.unpack('>I',h[:4])[0]
i=4; ds=None
while i<4+hl:
    k,i=varint(h,i); f=k>>3; w=k&7
    if w==2: l,i=varint(h,i); i+=l
    elif w==0:
        v,i=varint(h,i)
        if f==3: ds=v
HEADER=h[:4+hl+ds]
if mode=='ways':
    A,B=FIRST_WAY,FIRST_REL
    want=set(json.load(open('/tmp/claude-0/ov/pbf/way_ids.json')))
    out=open(f'/tmp/claude-0/ov/pbf/ways.{PART}.jsonl','w')
else:
    A,B=0,FIRST_WAY
    want=set(json.load(open('/tmp/claude-0/ov/pbf/need_nodes.json')))
    out=open(f'/tmp/claude-0/ov/pbf/nodes.{PART}.jsonl','w')
CH=1_000_000_000
bounds=[A]
x=A+CH
while x<B:
    bounds.append(align(x)); x=bounds[-1]+CH
bounds.append(B)
if bounds[0]==0: bounds[0]=len(HEADER)
print('chunks',len(bounds)-1, flush=True)
def fetch(k): return prng(bounds[k], bounds[k+1])
mine=[k for k in range(len(bounds)-1) if k%NP==PART]
t0=time.time(); found=0
with cf.ThreadPoolExecutor(1) as pre:
    fut=pre.submit(fetch,mine[0])
    for n,k in enumerate(mine):
        data=fut.result()
        if n+1<len(mine): fut=pre.submit(fetch,mine[n+1])
        fb=osmium.io.FileBuffer(HEADER+data,'pbf'); del data
        fp=osmium.FileProcessor(fb, osmium.osm.WAY if mode=='ways' else osmium.osm.NODE).with_filter(osmium.filter.IdFilter(want))
        for o in fp:
            if mode=='ways':
                out.write(json.dumps({'id':o.id,'nodes':[n_.ref for n_ in o.nodes],'tags':{t.k:t.v for t in o.tags}}, ensure_ascii=False)+'\n')
            else:
                out.write(json.dumps({'id':o.id,'lon':o.location.lon,'lat':o.location.lat,'tags':{t.k:t.v for t in o.tags}}, ensure_ascii=False)+'\n')
            found+=1
        del fb, fp
        out.flush()
        print(k, bounds[k], found, round(time.time()-t0), flush=True)
out.close()
print('done', found, time.time()-t0, flush=True)
