"""Run fpbuild.py for every job in jobs.json (three at a time), writing out/<first city>.geojson, .png and .log. Jobs whose
geojson exists are skipped; pass job indices to rerun some."""
import json, sys, os, time, subprocess, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__))
jobs = json.load(open('jobs.json'))
only = sys.argv[1:]  # optional: job indices
os.makedirs('out', exist_ok=True)
def run(i):
    j = jobs[i]; tag = j[0].replace(' ', '_').replace('/', '_')
    if os.path.exists(f'out/{tag}.geojson') and not only: return i, 'skip'
    t0 = time.time()
    p = subprocess.run([sys.executable, os.path.join(HERE, 'fpbuild.py'), *j, '--png'], capture_output=True, text=True)
    open(f'out/{tag}.log', 'w').write(p.stdout + p.stderr)
    return i, f'{"ok" if p.returncode == 0 else "FAIL"} {time.time()-t0:.0f}s'
idx = [int(x) for x in only] if only else range(len(jobs))
with cf.ThreadPoolExecutor(3) as ex:
    for i, st in ex.map(run, idx):
        print(i, jobs[i][0], st, flush=True)
