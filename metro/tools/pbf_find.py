# Find where relations start in the planet PBF using HTTP range requests (blob boundary search + binary search)
import urllib.request, zlib, struct, sys
URL='https://osm-pds.s3.amazonaws.com/planet-latest.osm.pbf'
SIZE=95244184503
def rng(a,b):
    req=urllib.request.Request(URL, headers={'Range':f'bytes={a}-{b-1}'})
    return urllib.request.urlopen(req, timeout=120).read()
def varint(b,i):
    s=0;r=0
    while True:
        x=b[i]; r|=(x&0x7f)<<s; i+=1; s+=7
        if x<0x80: return r,i
def parse_header(b):
    # BlobHeader: 1 type(string) 2 indexdata 3 datasize(int32)
    i=0; typ=None; ds=None
    while i<len(b):
        k,i=varint(b,i); f=k>>3; w=k&7
        if w==2:
            l,i=varint(b,i); v=b[i:i+l]; i+=l
            if f==1: typ=v
        elif w==0:
            v,i=varint(b,i)
            if f==3: ds=v
        else: raise ValueError
    return typ,ds
def find_blob(off):
    buf=rng(off, off+40_000_000)
    j=0
    while True:
        p=buf.find(b'\x0a\x07OSMData', j)
        if p<0: raise RuntimeError('none')
        if p>=4:
            hl=struct.unpack('>I',buf[p-4:p])[0]
            if 8<=hl<64:
                try:
                    typ,ds=parse_header(buf[p:p+hl])
                    if typ==b'OSMData' and ds and ds<64_000_000:
                        nxt=p+hl+ds
                        if nxt+4+9<=len(buf):
                            hl2=struct.unpack('>I',buf[nxt:nxt+4])[0]
                            if buf[nxt+4:nxt+4+9]!=b'\x0a\x07OSMData': j=p+1; continue
                        return off+p-4, hl, ds
                except Exception: pass
        j=p+1
def blob_kind(start, hl, ds):
    raw=rng(start+4+hl, start+4+hl+ds)
    # Blob: 1 raw, 2 raw_size, 3 zlib_data
    i=0; data=None
    while i<len(raw):
        k,i=varint(raw,i); f=k>>3; w=k&7
        if w==2:
            l,i=varint(raw,i); v=raw[i:i+l]; i+=l
            if f==3: data=zlib.decompress(v)
            if f==1: data=v
        elif w==0: v,i=varint(raw,i)
    # PrimitiveBlock: 1 stringtable, 2 primitivegroup
    i=0
    while i<len(data):
        k,i=varint(data,i); f=k>>3; w=k&7
        if w==2:
            l,i=varint(data,i)
            if f==2:
                g=data[i:i+l]; k2,_=varint(g,0); return {1:'nodes',2:'dense',3:'ways',4:'relations'}.get(k2>>3,'?')
            i+=l
        elif w==0: v,i=varint(data,i)
        elif w==5: i+=4
        elif w==1: i+=8
    return '?'
lo, hi = int(SIZE*0.85), SIZE-3_000_000
# make sure lo is in ways
s,hl,ds=find_blob(lo); print('lo kind', blob_kind(s,hl,ds), flush=True)
while hi-lo>40_000_000:
    mid=(lo+hi)//2
    s,hl,ds=find_blob(mid); k=blob_kind(s,hl,ds); print(mid, s, k, flush=True)
    if k=='relations': hi=s
    else: lo=s+4+hl+ds
# linear scan from lo to first relations blob
off=lo
while True:
    s,hl,ds=find_blob(off); k=blob_kind(s,hl,ds)
    if k=='relations': print('FIRST_REL', s); break
    off=s+4+hl+ds
