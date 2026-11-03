import sys, importlib, json
sys.path.insert(0,'.')
from lib.core import build
from lib.render import render
city=sys.argv[1]; mod=sys.argv[2]; bbox=json.loads(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3]!='-' else None
grid=float(sys.argv[4]) if len(sys.argv)>4 else 0.01
S=importlib.import_module('specs.'+mod).SPEC
core,st,zones=build(city,S)
print(json.dumps(st))
render(city,core=core,bbox=bbox,out=f'render/{mod}.png',lassos=[z['poly'] for z in S['zones']],grid=grid)
import pickle; pickle.dump((core,st),open(f'render/{mod}.pkl','wb'))
