# Blob-aligned ~1 GB chunk boundaries for a section: bounds.py DIR A B OUTNAME
import sys, json
sys.path.insert(0, sys.argv[1])
from pbf import *
A,B=int(sys.argv[2]),int(sys.argv[3]); CH=1_000_000_000
b=[A]; x=A+CH
while x<B:
    b.append(align(x)[0]); x=b[-1]+CH
b.append(B)
json.dump(b, open(sys.argv[1]+'/data/'+sys.argv[4],'w')); print(len(b)-1,'chunks')
