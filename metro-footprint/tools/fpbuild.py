"""Metro built-up footprints from ESA WorldCover 2021.
Cells of 1/2400 deg (~46 m): built when >= T of their 25 pixels are class 50. Opening removes strips narrower than
2*OPEN (highways), closing bridges gaps up to 2*CLOSE, holes under HOLE km2 fill. Pieces holding a tower of 150 m+
are a city's footprint; cities sharing a piece share a feature. Water (class 80, >= 50% of a cell) is cut last."""
import os, sys, math, json, time, argparse
import numpy as np, pandas as pd
from scipy import ndimage as ndi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fp
from shapely.geometry import shape, mapping, MultiPolygon, Polygon
from shapely.ops import unary_union
from rasterio import features as rfeat
from rasterio.transform import from_origin

D = pd.read_csv('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv').dropna(subset=['lat', 'lon'])
CPD = fp.CPD
# A city whose towers all stand outside its established built-up land claims the piece under each anchor point as
# well: Cairo's towers of 150 m+ are all in the New Administrative Capital, bare ground in 2021, 45 km east of Cairo.
ANCHORS = {'Cairo': [(31.2357, 30.0444)]}

def edt(m, cy, cx):
    return ndi.distance_transform_edt(m, sampling=(cy, cx))
def erode(m, r, cy, cx):  return edt(m, cy, cx) > r
def dilate(m, r, cy, cx): return edt(~m, cy, cx) <= r
def opening(m, r, cy, cx): return dilate(erode(m, r, cy, cx), r, cy, cx)
def closing(m, r, cy, cx): return erode(dilate(m, r, cy, cx), r, cy, cx)

def fill_small_holes(m, cx, cy, hole_km2):
    holes = ~m
    lab, n = ndi.label(holes)
    if not n: return m
    sizes = ndi.sum(holes, lab, range(1, n + 1)) * cx * cy / 1e6
    border = np.zeros(n + 1, bool)
    border[np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]])] = True
    small = np.r_[False, sizes < hole_km2] & ~border
    return m | small[lab]

def cells_bbox(lon0, lat0, lon1, lat1):
    c0, r1 = fp.cell_of(lon0, lat0); c1, r0 = fp.cell_of(lon1, lat1)
    return c0, c1 + 1, r0, r1 + 1

def run_job(cities, P, log=print):
    """cities: list of city names whose footprints this job builds. Returns (features, info)."""
    t = D[D.city.isin(cities)]
    anchors = [(c, lon, lat) for c in cities for lon, lat in ANCHORS.get(c, [])]
    lons = list(t.lon) + [a[1] for a in anchors]; lats = list(t.lat) + [a[2] for a in anchors]
    lat_mid = float(np.mean(lats))
    kmlat = 1 / 110.574; kmlon = 1 / (111.32 * math.cos(math.radians(lat_mid)))
    lon0, lon1 = min(lons) - P.pad * kmlon, max(lons) + P.pad * kmlon
    lat0, lat1 = min(lats) - P.pad * kmlat, max(lats) + P.pad * kmlat
    cy = 110574 / CPD; cx = 111320 * math.cos(math.radians(lat_mid)) / CPD
    for it in range(8):
        c0, c1, r0, r1 = cells_bbox(lon0, lat0, lon1, lat1)
        t0 = time.time(); built, water = fp.read_cells(c0, c1, r0, r1); tr = time.time() - t0
        t0 = time.time()
        m = built >= round(P.T * 25)
        if P.open: m = opening(m, P.open, cy, cx)
        if P.close: m = closing(m, P.close, cy, cx)
        m = fill_small_holes(m, cx, cy, P.hole)
        lab, n = ndi.label(m, structure=np.ones((3, 3)))
        # every tower in the box (any city) names the piece it stands in
        tb = D[(D.lon >= lon0) & (D.lon <= lon1) & (D.lat >= lat0) & (D.lat <= lat1)]
        rc = np.array([fp.cell_of(r.lon, r.lat) for r in tb.itertuples()]).reshape(-1, 2)
        cc = np.clip(rc[:, 0] - c0, 0, lab.shape[1] - 1); rr = np.clip(rc[:, 1] - r0, 0, lab.shape[0] - 1)
        tlab = lab[rr, cc] if len(tb) else np.array([], int)
        # a city claims a piece that holds at least 3 of its towers, or a tenth of them (so a city with few
        # towers claims with 1 or 2); a stray tower or two in another city's patch does not merge the two
        count = {}
        for L, city in zip(tlab, tb.city):
            if L: count[(int(L), city)] = count.get((int(L), city), 0) + 1
        ncity = tb.city.value_counts()
        piece_cities = {}
        for (L, city), k in count.items():
            if k >= min(3, math.ceil(0.1 * int(D.city.eq(city).sum()))): piece_cities.setdefault(L, set()).add(city)
        for city, lon, lat in anchors:
            ac, ar = fp.cell_of(lon, lat); L = int(lab[ar - r0, ac - c0]) if 0 <= ar - r0 < lab.shape[0] and 0 <= ac - c0 < lab.shape[1] else 0
            if L: piece_cities.setdefault(L, set()).add(city); log(f"  {city}: claims the piece under its anchor point")
        # a job city whose towers stand on no built-up piece (a construction site in 2021, a tower by the shore or in
        # a park) claims the nearest piece of P.attach_km2 or more within P.fallback metres of one of its towers
        sizes = ndi.sum(m, lab, range(1, n + 1)) * cx * cy / 1e6
        bigs = [L for L in range(1, n + 1) if sizes[L - 1] >= P.attach_km2]
        claimed = {c for L, cs in piece_cities.items() if L in bigs for c in cs}   # a claim on a patch of a few cells does not count
        for city in cities:
            if city in claimed or not (tb.city == city).any(): continue
            big = np.isin(lab, bigs)
            if not big.any(): continue
            dist, (iy, ix) = ndi.distance_transform_edt(~big, sampling=(cy, cx), return_indices=True)
            sel = (tb.city == city).values
            d = dist[rr[sel], cc[sel]]
            if d.min() <= P.fallback:
                k = np.argmin(d); L = int(lab[iy[rr[sel][k], cc[sel][k]], ix[rr[sel][k], cc[sel][k]]])
                piece_cities.setdefault(L, set()).add(city)
                log(f"  {city}: no piece holds its towers; claims the nearest piece, {d.min():.0f} m away")
        kept_ids = [L for L, cs in piece_cities.items() if cs & set(cities)]
        kept = np.isin(lab, kept_ids)
        tm = time.time() - t0
        # does a kept piece reach the edge of the box? then widen that side
        E = 3
        grow = dict(w=kept[:, :E].any(), e=kept[:, -E:].any(), s=kept[-E:].any(), n=kept[:E].any())
        wkm = (lon1 - lon0) / kmlon; hkm = (lat1 - lat0) / kmlat
        log(f"  it{it}: box {wkm:.0f}x{hkm:.0f} km, read {tr:.0f}s, morph {tm:.0f}s, {n} pieces, kept {len(kept_ids)}, grow {''.join(k for k, v in grow.items() if v) or '-'}")
        if not any(grow.values()) or max(wkm, hkm) >= P.maxkm: break
        if grow['w']: lon0 -= P.step * kmlon
        if grow['e']: lon1 += P.step * kmlon
        if grow['s']: lat0 -= P.step * kmlat
        if grow['n']: lat1 += P.step * kmlat
    clipped = any(grow.values())
    # tower-less pieces within P.attach metres of a kept piece (across water, or a gap the closing did not bridge)
    attached = {}
    if P.attach and kept_ids:
        sizes = ndi.sum(m, lab, range(1, n + 1)) * cx * cy / 1e6
        dist, (iy, ix) = ndi.distance_transform_edt(~kept, sampling=(cy, cx), return_indices=True)
        for L in range(1, n + 1):
            if L in piece_cities or sizes[L - 1] < P.attach_km2: continue
            sel = lab == L
            d = dist[sel]
            if d.min() <= P.attach:
                k = np.argmin(d); ys, xs = np.nonzero(sel)
                near = lab[iy[ys[k], xs[k]], ix[ys[k], xs[k]]]
                attached[L] = int(near)
    # water cut and small-piece cleanup for the drawn shape
    final = (kept | np.isin(lab, list(attached))) & ~(water >= 13)
    # drop slivers under P.sliver km2 (after the water cut)
    lab2, n2 = ndi.label(final, structure=np.ones((3, 3)))
    if n2:
        s2 = ndi.sum(final, lab2, range(1, n2 + 1)) * cx * cy / 1e6
        final &= np.r_[False, s2 >= P.sliver][lab2]
    # group pieces into features: pieces sharing a city share a feature
    parent = {}
    def find(x):
        while parent.get(x, x) != x: x = parent[x]
        return x
    def union(a, b): parent[find(a)] = find(b)
    city_piece = {}
    for L in kept_ids:
        for c in piece_cities[L]:
            if c in city_piece: union(L, city_piece[c])
            else: city_piece[c] = L
    for L, near in attached.items(): union(L, near)
    groups = {}
    for L in list(kept_ids) + list(attached):
        groups.setdefault(find(L), []).append(L)
    # vectorise: label array of final cells carrying the piece id (water-cut pieces keep their label)
    transform = from_origin(-180 + c0 / CPD, 90 - r0 / CPD, 1 / CPD, 1 / CPD)
    src = np.where(final, lab, 0).astype(np.int32)
    polys = {}
    for geom, val in rfeat.shapes(src, mask=final, transform=transform, connectivity=8):
        polys.setdefault(int(val), []).append(shape(geom))
    feats = []
    for root, Ls in groups.items():
        geoms = [g for L in Ls for g in polys.get(L, [])]
        if not geoms: continue
        g = unary_union(geoms).simplify(P.simplify / 111320, preserve_topology=True)
        parts = [p for p in (g.geoms if hasattr(g, 'geoms') else [g]) if p.geom_type == 'Polygon']
        cells = sum(int((src == L).sum()) for L in Ls)
        cs = {}
        for L in Ls:
            for c in piece_cities.get(L, ()): cs.setdefault(c, 0)
        for c in cs:
            tc = D[D.city == c]
            rc = np.array([fp.cell_of(r.lon, r.lat) for r in tc.itertuples()]).reshape(-1, 2)
            inb = (rc[:, 0] >= c0) & (rc[:, 0] < c1) & (rc[:, 1] >= r0) & (rc[:, 1] < r1)
            inside = np.isin(lab[rc[inb, 1] - r0, rc[inb, 0] - c0], Ls)
            cs[c] = {'towers': int(inside.sum()), 'towers_in_city': int(len(tc))}
        order = sorted(cs, key=lambda c: -cs[c]['towers'])
        feats.append({'type': 'Feature', 'properties': {
            'name': ' · '.join(order[:3]) + (f' and {len(order) - 3} more' if len(order) > 3 else ''),
            'cities': [{'city': c, **cs[c]} for c in order],
            'area_km2': round(cells * cx * cy / 1e6, 1), 'pieces': len(parts), 'clipped': bool(clipped),
        }, 'geometry': mapping(MultiPolygon(parts))})
    info = dict(box=[round(float(x), 4) for x in (lon0, lat0, lon1, lat1)], cells=lab.shape, pieces=n, kept=len(kept_ids), attached=len(attached), clipped=clipped)
    return feats, info, (built, water, lab, final, kept, (lon0, lat0, lon1, lat1), cx, cy)

def render(city_label, state, out, D=D):
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    built, water, lab, final, kept, (lon0, lat0, lon1, lat1), cx, cy = state
    H, W = final.shape
    fig, ax = plt.subplots(figsize=(12, 12 * H / W * cy / cx), dpi=90)
    img = np.zeros(final.shape + (3,), np.float32) + np.array([0.96, 0.94, 0.90])
    img[built >= 5] = [0.75, 0.72, 0.68]
    img[final] = [0.62, 0.45, 0.75]
    img[water >= 13] = [0.6, 0.75, 0.85]
    ax.imshow(img, extent=[lon0, lon1, lat0, lat1], interpolation='nearest', aspect=cy / cx)
    tb = D[(D.lon >= lon0) & (D.lon <= lon1) & (D.lat >= lat0) & (D.lat <= lat1)]
    ax.scatter(tb.lon, tb.lat, s=3, c='#8b0000', lw=0)
    ax.set_title(city_label); fig.tight_layout(); fig.savefig(out); plt.close(fig)

def rnd(o):
    if isinstance(o, (list, tuple)): return [rnd(x) for x in o]
    if isinstance(o, float): return round(o, 4)
    return o

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cities', nargs='+'); ap.add_argument('--T', type=float, default=0.2)
    ap.add_argument('--open', type=float, default=100); ap.add_argument('--close', type=float, default=350)
    ap.add_argument('--hole', type=float, default=0.5); ap.add_argument('--pad', type=float, default=20)
    ap.add_argument('--step', type=float, default=25); ap.add_argument('--maxkm', type=float, default=300)
    ap.add_argument('--attach', type=float, default=1500); ap.add_argument('--attach_km2', type=float, default=1.0)
    ap.add_argument('--sliver', type=float, default=0.1); ap.add_argument('--simplify', type=float, default=40)
    ap.add_argument('--fallback', type=float, default=3000)
    ap.add_argument('--out', default='out'); ap.add_argument('--png', action='store_true')
    P = ap.parse_args()
    os.makedirs(P.out, exist_ok=True)
    tag = P.cities[0].replace(' ', '_')
    t0 = time.time()
    feats, info, state = run_job(P.cities, P)
    fc = {'type': 'FeatureCollection', 'features': [{**f, 'geometry': {'type': 'MultiPolygon', 'coordinates': rnd(f['geometry']['coordinates'])}} for f in feats]}
    s = json.dumps(fc, ensure_ascii=False, separators=(',', ':'))
    open(f'{P.out}/{tag}.geojson', 'w').write(s)
    for f in feats:
        print(f"  {f['properties']['name']}: {f['properties']['area_km2']} km2, {f['properties']['pieces']} pieces, cities {[(c['city'], c['towers']) for c in f['properties']['cities']]}")
    print(f"{tag}: {len(s)/1e6:.2f} MB, {sum(len(r) for f in feats for p in f['geometry']['coordinates'] for r in p)} vertices, {time.time()-t0:.0f}s, {info}")
    if P.png: render(f"{tag} T={P.T} open={P.open} close={P.close}", state, f'{P.out}/{tag}.png')
