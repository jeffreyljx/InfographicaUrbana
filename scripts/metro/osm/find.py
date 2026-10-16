import sys
sys.path.insert(0, sys.argv[1])
from pbf import *
def first_of(kind, lo, hi):
    # lo: inside an earlier section; hi: inside kind section or later
    while hi-lo>40_000_000:
        mid=(lo+hi)//2
        s,hl,ds=align(mid); k=blob_kind(s,hl,ds)
        order={'nodes':0,'ways':1,'relations':2}
        if order[k]>=order[kind]: hi=s
        else: lo=s+4+hl+ds
    off=lo
    while True:
        s,hl,ds=align(off); k=blob_kind(s,hl,ds)
        if k==kind: return s
        off=s+4+hl+ds
fw=first_of('ways', int(SIZE*0.60), int(SIZE*0.75)); print('FIRST_WAY', fw, flush=True)
fr=first_of('relations', int(SIZE*0.97), SIZE-3_000_000); print('FIRST_REL', fr, flush=True)
