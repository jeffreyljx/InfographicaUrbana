import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import type { FeatureCollection, MultiPolygon, Position } from "geojson";
import { getIndex, getPlaces } from "./data";
import { areaKm2 } from "./geoArea";
import { towerSlug } from "./types";

/**
 * The skylines page: every city's skyline extents on the map (public/skyline-extent.geojson, one MultiPolygon per city),
 * drawn as a map of the city with the map taken away, and measured at build time, so a revised extents file shows up on
 * the next build.
 *
 * A city's extents are split into its skylines with the density rule they are drawn with (skyline-extent/tools/
 * build_density.py in the project's shared folder: DBSCAN over every tower of 150 m+, 800 m, 4 samples; groups of 5+
 * towers). The file keeps only each city's outline and its pockets' names, so the pockets are found again here with the
 * same rule: outline pieces that share a pocket's towers are one skyline (a pocket cut in two by a river stays one), and
 * pockets whose outlines ran together are one skyline too, named after all of them. Towers are counted the way the map's
 * extent popups count them: every tower of the city inside the outline, any status.
 */
const EPS = 800, MIN_SAMPLES = 4, MIN_TOWERS = 5;   // as in build_density.py
const EARTH = 6371000;
const RAD = Math.PI / 180;
const UNIT = 10;   // drawing unit, metres

export interface Skyline {
  /** names of the pockets inside, largest first, as the map's popups give them */
  names: string[];
  towers: number;
  km2: number;
  /** SVG path of the outline, in the city drawing's units */
  d: string;
}

export interface CitySkylines {
  city: string;
  citySlug: string | null;
  /** largest first */
  skylines: Skyline[];
  towers: number;
  completed: number;
  km2: number;
  tallest: { name: string; height: number; slug: string; status: string } | null;
  /** width and height of the drawing in km, north up */
  wKm: number;
  hKm: number;
  /** SVG paths of the towers inside the outlines, and of the city's other towers that fall within the drawing, in
   *  UNIT-metre units from its top-left corner */
  dots: string;
  others: string;
}

interface Pt { lat: number; lon: number }

function haversine(a: Pt, b: Pt): number {
  const s = Math.sin((b.lat - a.lat) * RAD / 2) ** 2 + Math.cos(a.lat * RAD) * Math.cos(b.lat * RAD) * Math.sin((b.lon - a.lon) * RAD / 2) ** 2;
  return 2 * Math.asin(Math.sqrt(s)) * EARTH;
}

/** DBSCAN labels (-1: noise) as scikit-learn assigns them: points in list order, each cluster grown in full before the next starts. */
function dbscan(pts: Pt[]): number[] {
  const CELL = 0.008;   // degrees; 1 cell of latitude is ~890 m, so neighbours are within one cell row
  const grid = new Map<string, number[]>();
  const cellOf = (p: Pt) => [Math.floor(p.lat / CELL), Math.floor(p.lon / CELL)];
  pts.forEach((p, n) => {
    const k = cellOf(p).join();
    const list = grid.get(k);
    if (list) list.push(n); else grid.set(k, [n]);
  });
  const nbrs = pts.map(p => {
    const [i0, j0] = cellOf(p);
    const dj = Math.ceil(1 / Math.max(Math.cos(Math.min(89, Math.abs(p.lat) + 1) * RAD), 0.02));
    const out: number[] = [];
    for (let i = i0 - 1; i <= i0 + 1; i++) for (let j = j0 - dj; j <= j0 + dj; j++)
      for (const n of grid.get(`${i},${j}`) ?? []) if (haversine(p, pts[n]) <= EPS) out.push(n);
    return out;
  });
  const label = new Array<number>(pts.length).fill(-1);
  let next = 0;
  for (let i = 0; i < pts.length; i++) {
    if (label[i] !== -1 || nbrs[i].length < MIN_SAMPLES) continue;
    const stack = [i];
    label[i] = next;
    while (stack.length) {
      const v = stack.pop()!;
      if (nbrs[v].length < MIN_SAMPLES) continue;   // a border point joins but does not extend the cluster
      for (const u of nbrs[v]) if (label[u] === -1) { label[u] = next; stack.push(u); }
    }
    next++;
  }
  return label;
}

function inRing(x: number, y: number, ring: Position[]): boolean {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if ((yi > y) !== (yj > y) && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}
const inPolygon = (x: number, y: number, [outer, ...holes]: Position[][]) => inRing(x, y, outer) && !holes.some(h => inRing(x, y, h));

/** A city's drawing: local metres (equirectangular around its middle), north up, framing every outline it has. */
function frame(polys: Position[][][]) {
  let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
  for (const p of polys) for (const [x, y] of p[0]) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
  const kx = 111_320 * Math.cos(((y0 + y1) / 2) * RAD) / UNIT, ky = 110_574 / UNIT;
  const X = (lon: number) => Math.round((lon - x0) * kx), Y = (lat: number) => Math.round((y1 - lat) * ky);
  const r2 = (v: number) => Math.round(v * 100) / 100;
  // relative moves keep the paths short; a minus sign separates numbers by itself
  const pair = (dx: number, dy: number) => `${dx}${dy < 0 ? "" : " "}${dy}`;
  return {
    wKm: r2((x1 - x0) * kx * UNIT / 1000), hKm: r2((y1 - y0) * ky * UNIT / 1000),
    inside: (p: Pt) => p.lon >= x0 && p.lon <= x1 && p.lat >= y0 && p.lat <= y1,
    outline(parts: Position[][][]): string {
      let d = "";
      for (const p of parts) for (const ring of p) {
        let px = X(ring[0][0]), py = Y(ring[0][1]);
        d += `M${px} ${py}l`;
        const steps: string[] = [];
        for (const [lon, lat] of ring.slice(1)) {
          const x = X(lon), y = Y(lat);
          if (x === px && y === py) continue;
          steps.push(pair(x - px, y - py));
          px = x; py = y;
        }
        d += steps.join(" ").replace(/ -/g, "-") + "z";
      }
      return d;
    },
    dots(pts: Pt[]): string {
      let s = "", px = 0, py = 0;
      for (const t of pts) {
        const x = X(t.lon), y = Y(t.lat);
        s += `m${pair(x - px, y - py)}h0`;
        px = x; py = y;
      }
      return s ? "M0 0" + s : "";
    },
  };
}

let cached: CitySkylines[] | null = null;

/** Every city with skyline extents, largest total area first. */
export function getCitySkylines(): CitySkylines[] {
  if (cached) return cached;
  const fc = JSON.parse(readFileSync(join(process.cwd(), "public/skyline-extent.geojson"), "utf8")) as FeatureCollection<MultiPolygon>;
  const idx = getIndex();
  const COMPLETED = idx.statuses.indexOf("Completed");
  const slugs = new Map(getPlaces().cities.map(c => [c.name, c.slug]));
  const towers = idx.rows.map(r => ({ id: r[0], name: r[1], lat: r[2], lon: r[3], height: r[4], city: idx.cities[r[5]], status: r[7] }));
  const label = dbscan(towers);
  const size = new Map<number, number>();
  for (const l of label) if (l >= 0) size.set(l, (size.get(l) ?? 0) + 1);
  const isPocket = (l: number) => l >= 0 && size.get(l)! >= MIN_TOWERS;

  const out: CitySkylines[] = [];
  for (const f of fc.features) {
    const city = String(f.properties?.city);
    const areas: string[] = f.properties?.areas ?? [];
    const mine = towers.flatMap((t, n) => (t.city === city ? [n] : []));
    // the city's pockets, largest first and ties in label order: the order build_density.py lists their names in
    const count = new Map<number, number>();
    for (const n of mine) if (isPocket(label[n])) count.set(label[n], (count.get(label[n]) ?? 0) + 1);
    const order = [...count.keys()].sort((a, b) => count.get(b)! - count.get(a)! || a - b);
    const named = order.length === areas.length;
    if (!named) console.warn(`skylines: ${city} has ${order.length} pockets but ${areas.length} names; naming by district instead`);
    const rank = new Map(order.map((l, i) => [l, i]));

    const polys = f.geometry.coordinates;
    const inside = polys.map(p => mine.filter(n => inPolygon(towers[n].lon, towers[n].lat, p)));
    // outline pieces holding towers of one pocket belong to one skyline
    const parent = polys.map((_, i) => i);
    const find = (i: number): number => (parent[i] === i ? i : (parent[i] = find(parent[i])));
    const first = new Map<number, number>();
    inside.forEach((ns, i) => {
      for (const n of ns) {
        const l = label[n];
        if (!isPocket(l)) continue;
        if (first.has(l)) parent[find(i)] = find(first.get(l)!); else first.set(l, i);
      }
    });
    const groups = new Map<number, number[]>();
    polys.forEach((_, i) => { const g = groups.get(find(i)); if (g) g.push(i); else groups.set(find(i), [i]); });

    const fr = frame(polys);
    const skylines: Skyline[] = [...groups.values()].map(parts => {
      const ns = parts.flatMap(i => inside[i]);
      const pockets = [...new Set(ns.map(n => label[n]).filter(l => rank.has(l)))].sort((a, b) => rank.get(a)! - rank.get(b)!);
      const coordinates = parts.map(i => polys[i]);
      return {
        names: named ? pockets.map(l => areas[rank.get(l)!]) : [mostCommonDistrict(ns)],
        towers: ns.length, km2: areaKm2({ type: "MultiPolygon", coordinates }), d: fr.outline(coordinates),
      };
    }).sort((a, b) => b.km2 - a.km2);
    const ins = new Set(inside.flat());
    const ts = [...ins].map(n => towers[n]);
    const done = ts.filter(t => t.status === COMPLETED);
    const top = [...(done.length ? done : ts)].sort((a, b) => b.height - a.height)[0];
    out.push({
      city, citySlug: slugs.get(city) ?? null, skylines,
      towers: ts.length, completed: done.length, km2: areaKm2(f.geometry),
      tallest: top ? { name: top.name, height: top.height, slug: towerSlug(top.name, top.id), status: idx.statuses[top.status] } : null,
      wKm: fr.wKm, hKm: fr.hKm,
      dots: fr.dots(ts), others: fr.dots(mine.filter(n => !ins.has(n)).map(n => towers[n]).filter(fr.inside)),
    });
  }
  function mostCommonDistrict(ns: number[]): string {
    const c = new Map<string, number>();
    for (const n of ns) { const d = idx.districts[idx.rows[n][6]][1]; c.set(d, (c.get(d) ?? 0) + 1); }
    return [...c].sort((a, b) => b[1] - a[1])[0]?.[0] ?? "";
  }
  return (cached = out.sort((a, b) => b.km2 - a.km2));
}
