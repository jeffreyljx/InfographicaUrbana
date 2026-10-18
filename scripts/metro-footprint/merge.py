"""Join the per-job footprints (out/*.geojson, from fpbuild.py) into one file for the site.

Each feature is tidied for size: water holes under HOLE km2 are filled (ponds and canals; the basemap still draws
them over the fill), pieces under PIECE km2 dropped, the outline simplified to SIMP m, coordinates to 4 decimals.
area_km2 and pieces are recomputed from the final shape. Features from different jobs that overlap are reported.
Usage: python3 merge.py ../../public/metro-footprint.json   (from this folder, after runall.py)
"""
import json, glob, math, sys
from shapely.geometry import shape, mapping, MultiPolygon, Polygon
from shapely.strtree import STRtree
from shapely.validation import make_valid
from shapely.ops import unary_union
HOLE, PIECE, SIMP = 0.25, 0.25, 80

def km2(geom, lat):
    return abs(geom.area) * 111.32 * 110.57 * math.cos(math.radians(lat))

def tidy(g):
    polys = list(g.geoms) if g.geom_type == 'MultiPolygon' else [g]
    out = []
    for p in polys:
        lat = p.centroid.y
        if km2(p, lat) < PIECE: continue
        q = Polygon(p.exterior, [r for r in p.interiors if km2(Polygon(r), lat) >= HOLE])
        q = q.simplify(SIMP / 111320, preserve_topology=True)
        if q.is_empty: continue
        if not q.is_valid: q = make_valid(q)
        out += [x for x in (q.geoms if hasattr(q, 'geoms') else [q]) if x.geom_type == 'Polygon' and not x.is_empty]
    u = unary_union(out)   # parts that touch after simplification become one valid shape
    return MultiPolygon([x for x in (u.geoms if hasattr(u, 'geoms') else [u]) if x.geom_type == 'Polygon' and not x.is_empty])

def rnd(o):
    if isinstance(o, float): return round(o, 4)
    if isinstance(o, (list, tuple)): return [rnd(x) for x in o]
    if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
    return o

def main(out_path):
    feats, src = [], []
    for f in sorted(glob.glob('out/*.geojson')):
        for ft in json.load(open(f))['features']:
            g = tidy(shape(ft['geometry']))
            if g.is_empty: print('EMPTY after tidy:', f, ft['properties']['name']); continue
            p = ft['properties']
            p['area_km2'] = round(km2(g, g.centroid.y), 1); p['pieces'] = len(g.geoms)
            feats.append({'type': 'Feature', 'properties': p, 'geometry': rnd(mapping(g))}); src.append((f, g))
    # Overlaps between features from different jobs: a tower-less patch that each job attached to its own
    # nearest metro. It goes to the feature whose remainder lies nearer to it (the rule fpbuild applies within a job).
    geoms = [g for _, g in src]
    tree = STRtree(geoms)
    for i in range(len(geoms)):
        for j in sorted(int(j) for j in tree.query(geoms[i])):
            if j <= i: continue
            inter = geoms[i].intersection(geoms[j])
            if inter.is_empty or km2(inter, inter.centroid.y) < 0.01: continue
            rem_i, rem_j = geoms[i].difference(inter), geoms[j].difference(inter)
            for part in (inter.geoms if hasattr(inter, 'geoms') else [inter]):
                if part.geom_type != 'Polygon' or part.is_empty: continue
                di, dj = rem_i.distance(part), rem_j.distance(part)
                loser = j if di <= dj else i
                geoms[loser] = geoms[loser].difference(part)
                print(f'OVERLAP {km2(part, part.centroid.y):.2f} km2 between {feats[i]["properties"]["name"]} ({src[i][0]}) and '
                      f'{feats[j]["properties"]["name"]} ({src[j][0]}): given to {feats[i if loser == j else j]["properties"]["name"]}')
    for k, g in enumerate(geoms):
        if g is src[k][1]: continue
        u = unary_union(g)
        g = MultiPolygon([x for x in (u.geoms if hasattr(u, 'geoms') else [u]) if x.geom_type == 'Polygon' and km2(x, x.centroid.y) >= PIECE])
        p = feats[k]['properties']; p['area_km2'] = round(km2(g, g.centroid.y), 1); p['pieces'] = len(g.geoms)
        feats[k]['geometry'] = rnd(mapping(g)); src[k] = (src[k][0], g)
    feats.sort(key=lambda ft: -sum(c['towers'] for c in ft['properties']['cities']))
    fc = {'type': 'FeatureCollection', 'features': feats}
    s = json.dumps(fc, separators=(',', ':'), ensure_ascii=False)
    open(out_path, 'w').write(s)
    nv = sum(sum(len(p.exterior.coords) + sum(len(r.coords) for r in p.interiors) for p in g.geoms) for _, g in src)
    cities = sum(len(ft['properties']['cities']) for ft in feats)
    print(f'{len(feats)} features, {cities} cities, {nv} vertices, {len(s)/1e6:.2f} MB, {sum(ft["properties"]["area_km2"] for ft in feats):,.0f} km2 -> {out_path}')
    print('clipped:', [ft['properties']['name'] for ft in feats if ft['properties']['clipped']])
    return fc

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'merged.json')
