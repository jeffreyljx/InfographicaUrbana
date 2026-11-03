import sys,time
b=open(sys.argv[1]).read(); n=1800
for i in range(0,len(b),n):
    sys.stdout.write('#%05d:%s\n'%(i//n,b[i:i+n])); sys.stdout.flush(); time.sleep(float(sys.argv[2]) if len(sys.argv)>2 else 0.12)
print('#END',len(b),flush=True)
