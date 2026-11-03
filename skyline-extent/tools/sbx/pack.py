import tarfile,io,base64,os,sys
# pack selected layer files, brotli or xz compress, base64
import lzma,json,glob
data={}
for f in sorted(glob.glob('out/*.json')):
    data[os.path.basename(f)[:-5]]=json.load(open(f))
raw=json.dumps(data,separators=(',',':')).encode()
x=lzma.compress(raw,preset=9|lzma.PRESET_EXTREME)
open('geo.json.xz.b64','w').write(base64.b64encode(x).decode())
print('raw',len(raw),'xz',len(x),'b64',len(base64.b64encode(x)))
