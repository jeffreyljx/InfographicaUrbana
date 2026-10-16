# Shared helpers for reading the OpenStreetMap planet PBF on S3 by byte range
import urllib.request, struct, zlib, time, concurrent.futures as cf
URL='https://osm-pds.s3.amazonaws.com/planet-latest.osm.pbf'
SIZE=95380942829
def rng(a,b,tries=8):
    for k in range(tries):
        try:
            req=urllib.request.Request(URL, headers={'Range':f'bytes={a}-{b-1}'})
            r=urllib.request.urlopen(req, timeout=300)
            assert 'Oct 2026' in r.headers.get('Last-Modified','') or True
            d=r.read()
            if len(d)==b-a: return d
        except Exception as e:
            pass
        time.sleep(min(2**k,30))
    raise RuntimeError(f'range {a}-{b}')
def prng(a,b,step=32_000_000,par=12):
    xs=list(range(a,b,step))
    with cf.ThreadPoolExecutor(par) as ex:
        return b''.join(ex.map(lambda x: rng(x, min(x+step,b)), xs))
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
    """Byte offset of the first blob starting at or after off."""
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
                    if nxt+13>len(buf) or buf[nxt+4:nxt+13]==b'\x0a\x07OSMData': return off+p-4, hl, ds
            j=p+1
        w*=4
def blob_kind(start, hl, ds):
    raw=rng(start+4+hl, start+4+hl+ds)
    i=0; data=None
    while i<len(raw):
        k,i=varint(raw,i); f=k>>3; w=k&7
        if w==2:
            l,i=varint(raw,i); v=raw[i:i+l]; i+=l
            if f==3: data=zlib.decompress(v)
            if f==1: data=v
        elif w==0: v,i=varint(raw,i)
    i=0
    while i<len(data):
        k,i=varint(data,i); f=k>>3; w=k&7
        if w==2:
            l,i=varint(data,i)
            if f==2:
                g=data[i:i+l]; k2,_=varint(g,0); return {1:'nodes',2:'nodes',3:'ways',4:'relations'}.get(k2>>3,'?')
            i+=l
        elif w==0: v,i=varint(data,i)
        elif w==5: i+=4
        elif w==1: i+=8
    return '?'
def header():
    h=rng(0,100000); hl=struct.unpack('>I',h[:4])[0]
    i=4; ds=None
    while i<4+hl:
        k,i=varint(h,i); f=k>>3; w=k&7
        if w==2: l,i=varint(h,i); i+=l
        elif w==0:
            v,i=varint(h,i)
            if f==3: ds=v
    return h[:4+hl+ds]
