// Skyline extents through time, for the time capsule slider: every city's drawn urban core
// (public/skyline-extent.geojson), trimmed for each year to the area around the towers that stood by then.
// Run by scripts/prebuild.mjs after the dataset is unpacked, so a revised cores file or new tower data is picked up
// on the next build; it writes public/skyline-extent-years.geojson (git-ignored) and skips the work when its inputs
// have not changed since the last run.
//
// A tower stands in year Y if it is completed and its completion year is Y or earlier (completed towers with no
// year are left out). The dataset holds only towers standing today; towers that have since come down (the original
// World Trade Center and others) come from src/lib/lostTowers.json and stand from their completion year until the
// year they came down. Only towers inside a core count. For each city:
//
//   1. Each tower claims the core within R metres of it from its completion year.
//   2. The rest of the core (the "gaps": parks, low-rise blocks, waterfront more than R from every tower) is cut
//      into G-metre squares. A square joins once its K nearest towers stand, and any other tower within NEAR
//      metres of the nearest one's distance, and only where it touches the extent already drawn, so gaps fill
//      in from the edges of the built-up area rather than appearing as islands. A polygon of a core with no
//      tower of its own (a runway, a pier) takes the core's towers for this and needs no neighbour to start.
//   3. The result is closed by C metres (grown, then shrunk) so towers close together read as one district,
//      and clipped to the core, so an extent never reaches past today's line.
//   4. A city has an extent only once MIN_TOWERS of its core's towers stand.
//
// So an extent only grows with time, and from the year of its core's latest completed tower onwards it is the
// drawn core itself. The one exception is a lost tower: from the year it came down, the city's extent is worked
// out again from the towers still standing, as if the lost tower had never been built (see framesWithLosses).
// The output has one feature per city and keyframe: `from` is the first year it is shown and `to` the first year
// it is not (9999 for the last), so the map filters on from <= year < to. The last keyframe has no geometry of
// its own: the map uses the city's drawn core from skyline-extent.geojson.
import { createHash } from "node:crypto";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import ArrayList from "jsts/java/util/ArrayList.js";
import Coordinate from "jsts/org/locationtech/jts/geom/Coordinate.js";
import Envelope from "jsts/org/locationtech/jts/geom/Envelope.js";
import GeometryFactory from "jsts/org/locationtech/jts/geom/GeometryFactory.js";
import STRtree from "jsts/org/locationtech/jts/index/strtree/STRtree.js";
import RectangleIntersects from "jsts/org/locationtech/jts/operation/predicate/RectangleIntersects.js";
import { GeoJSONReader, GeoJSONWriter } from "jsts/org/locationtech/jts/io.js";
import BufferOp from "jsts/org/locationtech/jts/operation/buffer/BufferOp.js";
import SnapIfNeededOverlayOp from "jsts/org/locationtech/jts/operation/overlay/snap/SnapIfNeededOverlayOp.js";
import UnaryUnionOp from "jsts/org/locationtech/jts/operation/union/UnaryUnionOp.js";
import TopologyPreservingSimplifier from "jsts/org/locationtech/jts/simplify/TopologyPreservingSimplifier.js";
import "jsts/org/locationtech/jts/monkey.js";

const R = 400;          // metres of core each tower claims around itself
const G = 150;          // gap square size, metres
const K = 4;            // a gap square waits for its K nearest towers
const NEAR = 300;       // ... and for every tower within (distance to its nearest tower + NEAR)
const C = 300;          // closing distance, metres
const MIN_TOWERS = 5;   // towers standing in the core before the city's extent appears
const SIMPLIFY = 10;    // metres
const QUAD_SEGS = 6;    // segments per quarter circle in buffers

// jsts 2.12.1's ArrayList iterator removes the element after the one last returned, which breaks OverlayOp's
// collapsed-edge step whenever an overlay needs snapping; remove the right one, as java.util.Iterator does
Object.getPrototypeOf(new ArrayList().iterator()).remove = function () { this.arrayList.array.splice(--this.position, 1); };

const gf = new GeometryFactory();
const reader = new GeoJSONReader(gf), writer = new GeoJSONWriter();
const point = (x, y) => gf.createPoint(new Coordinate(x, y));
const buffer = (g, d) => BufferOp.bufferOp(g, d, QUAD_SEGS);
const intersection = (a, b) => SnapIfNeededOverlayOp.intersection(a, b);
const difference = (a, b) => SnapIfNeededOverlayOp.difference(a, b);
const polygons = g => {
  const type = g.getGeometryType();
  if (type === "Polygon") return g.isEmpty() ? [] : [g];
  if (type !== "MultiPolygon" && type !== "GeometryCollection") return [];
  const out = [];
  for (let i = 0; i < g.getNumGeometries(); i++) out.push(...polygons(g.getGeometryN(i)));
  return out;
};
// union of a list of geometries, as Polygon / MultiPolygon only
const union = gs => {
  const list = new ArrayList();
  for (const g of gs) for (const p of polygons(g)) list.add(p);
  if (list.isEmpty()) return gf.createMultiPolygon([]);
  return gf.createMultiPolygon(polygons(UnaryUnionOp.union(list)));
};
const mapCoords = (c, fn) => typeof c[0] === "number" ? fn(c) : c.map(x => mapCoords(x, fn));

// local equirectangular metres around (lon0, lat0); plenty at city scale
function projector(lon0, lat0) {
  const kx = 111_320 * Math.cos(lat0 * Math.PI / 180), ky = 110_574;
  return {
    fwd: ([x, y]) => [(x - lon0) * kx, (y - lat0) * ky],
    inv: ([x, y]) => [Math.round((x / kx + lon0) * 1e5) / 1e5, Math.round((y / ky + lat0) * 1e5) / 1e5],   // ~1 m
  };
}

// Map of year -> areas added that year, for one polygon of a core; `towers` are the core's
function partGrowth(part, towers, years) {
  const own = towers.filter(t => part.distance(point(t.x, t.y)) <= 1);
  const pts = new Map();   // towers sharing a point: the first to stand counts
  for (const t of own.length ? own : towers) {
    const x = Math.round(t.x * 10) / 10, y = Math.round(t.y * 10) / 10, k = `${x},${y}`;
    const p = pts.get(k);
    if (p) p.year = Math.min(p.year, t.year); else pts.set(k, { x, y, year: t.year });
  }
  const keys = [...pts.values()];
  const added = new Map();
  const add = (y, gs) => added.set(y, (added.get(y) ?? []).concat(gs));
  if (!keys.length) return added;
  const discs = own.length ? keys.map(k => buffer(point(k.x, k.y), R)) : [];
  discs.forEach((d, i) => add(keys[i].year, [intersection(d, part)]));

  // gap squares, each with the year it may join and the first year a disc it touches stands. Which towers a
  // square waits for is judged against all of the core's towers, so a polygon with only a few old towers of its
  // own (an old downtown) does not fill in long before the rest of the core
  const gap = discs.length ? difference(part, union(discs)) : part;
  const sq = [], ready = [], touch = [];
  if (!gap.isEmpty()) {
    const env = gap.getEnvelopeInternal();
    const nx = Math.ceil((env.getMaxX() - env.getMinX()) / G), ny = Math.ceil((env.getMaxY() - env.getMinY()) / G);
    for (let i = 0; i < nx; i++) for (let j = 0; j < ny; j++) {
      const gx = env.getMinX() + i * G, gy = env.getMinY() + j * G;
      const box = gf.toGeometry(new Envelope(gx, gx + G, gy, gy + G));
      if (!RectangleIntersects.intersects(box, gap)) continue;
      for (const piece of polygons(intersection(gap, box))) {
        if (piece.getArea() < 1) continue;
        const c = piece.getCentroid(), cx = c.getX(), cy = c.getY();
        const dist = towers.map(t => Math.hypot(t.x - cx, t.y - cy));
        const sorted = [...dist].sort((a, b) => a - b);
        const reach = Math.max(sorted[Math.min(K, sorted.length) - 1], sorted[0] + NEAR);
        let r = -Infinity;
        dist.forEach((d, n) => { if (d <= reach && towers[n].year > r) r = towers[n].year; });
        sq.push(piece); ready.push(r);
        if (own.length) {
          const pe = piece.getEnvelopeInternal();
          let first = 9999;
          for (const k of keys) {
            if (k.year >= first || k.x < pe.getMinX() - R - 1 || k.x > pe.getMaxX() + R + 1
              || k.y < pe.getMinY() - R - 1 || k.y > pe.getMaxY() + R + 1) continue;
            if (piece.distance(point(k.x, k.y)) <= R + 0.5) first = k.year;
          }
          touch.push(first);
        } else touch.push(r);
      }
    }
  }
  const tree = new STRtree();
  sq.forEach((s, i) => tree.insert(s.getEnvelopeInternal(), i));
  const nbrs = sq.map(s => {
    const b = BufferOp.bufferOp(s, 0.5);
    return tree.query(b.getEnvelopeInternal()).toArray().filter(j => b.intersects(sq[j]));
  });

  const reached = sq.map(() => false);
  for (const y of years) {
    const queue = [];
    sq.forEach((_, i) => {
      if (!reached[i] && ready[i] <= y && (touch[i] <= y || nbrs[i].some(j => reached[j]))) queue.push(i);
    });
    for (const i of queue) reached[i] = true;
    const fresh = [...queue];
    while (queue.length) {
      const i = queue.pop();
      for (const j of nbrs[i]) if (!reached[j] && ready[j] <= y) { reached[j] = true; queue.push(j); fresh.push(j); }
    }
    if (fresh.length) add(y, fresh.map(i => sq[i]));
  }
  return added;
}

// [{year, n, area, tallest}] for one city, one per year from the year MIN_TOWERS of its towers stand
// (`towers` all stand from their year on: none of them comes down)
function cityFrames(parts, towers, years) {
  const growth = parts.map(p => partGrowth(p, towers, years));
  const acc = parts.map(() => null), closed = parts.map(() => null);
  const frames = [];
  for (const y of years) {
    growth.forEach((g, i) => {
      if (!g.has(y)) return;
      acc[i] = union((acc[i] ? [acc[i]] : []).concat(g.get(y)));
      closed[i] = null;
    });
    const stood = towers.filter(t => t.year <= y);
    if (stood.length < MIN_TOWERS) continue;
    acc.forEach((a, i) => { if (a && !closed[i]) closed[i] = intersection(buffer(buffer(a, C), -C), parts[i]); });
    const tallest = stood.reduce((a, b) => b.height > a.height ? b : a);
    frames.push({ year: y, n: stood.length, area: union(closed.filter(Boolean)), tallest });
  }
  return frames;
}

// cityFrames for a city whose towers include lost ones (`gone` < 9999): the years are cut at each year a tower came
// down, and each stretch is grown from the towers that still stand in it (or are built later), so an extent can
// shrink when a tower comes down, and a city whose standing towers drop below MIN_TOWERS loses its extent
function framesWithLosses(parts, towers) {
  const yearsOf = ts => [...new Set(ts.map(t => t.year))].sort((a, b) => a - b);
  const cuts = [...new Set(towers.filter(t => t.gone < 9999).map(t => t.gone))].sort((a, b) => a - b);
  if (!cuts.length) return cityFrames(parts, towers, yearsOf(towers));
  const bounds = [-Infinity, ...cuts, Infinity], out = [];
  for (let k = 0; k + 1 < bounds.length; k++) {
    const from = bounds[k], until = bounds[k + 1];
    const ts = towers.filter(t => t.gone > from);
    const frames = cityFrames(parts, ts, yearsOf(Number.isFinite(from) ? ts.concat({ year: from }) : ts))
      .filter(fr => fr.year >= from && fr.year < until);
    if (Number.isFinite(from) && out.length && frames[0]?.year !== from) {   // too few towers left: no extent
      const stood = ts.filter(t => t.year <= from);
      out.push({ year: from, n: stood.length, area: gf.createMultiPolygon([]),
        tallest: stood.length ? stood.reduce((a, b) => b.height > a.height ? b : a) : null });
    }
    out.push(...frames);
  }
  return out;
}

export function buildSkylineYears({ cores: coresPath = "public/skyline-extent.geojson",
  towers: towersPath = "src/data/towers.json", lost: lostPath = "src/lib/lostTowers.json",
  out = "public/skyline-extent-years.geojson" } = {}) {
  if (!existsSync(coresPath) || !existsSync(towersPath)) return console.log("skyline years: no cores or tower data, skipped");
  const coresRaw = readFileSync(coresPath), towersRaw = readFileSync(towersPath);
  const lostRaw = existsSync(lostPath) ? readFileSync(lostPath) : Buffer.from("[]");
  const inputs = createHash("sha1").update(coresRaw).update(towersRaw).update(lostRaw).update(readFileSync(new URL(import.meta.url))).digest("hex");
  if (existsSync(out)) {
    try { if (JSON.parse(readFileSync(out)).inputs === inputs) return console.log(`skyline years: ${out} is up to date`); } catch {}
  }
  const t0 = Date.now();
  const cores = JSON.parse(coresRaw), idx = JSON.parse(towersRaw);
  const sch = Object.fromEntries(idx.schema.map((k, i) => [k, i]));
  const completed = idx.statuses.indexOf("Completed");
  const lostByCity = new Map();
  for (const t of JSON.parse(lostRaw)) lostByCity.set(t.city, (lostByCity.get(t.city) ?? []).concat(t));
  const byCity = new Map();
  for (const r of idx.rows) {
    const city = idx.cities[r[sch.city]];
    if (!byCity.has(city)) byCity.set(city, []);
    byCity.get(city).push(r);
  }

  const feats = [], report = [];
  for (const f of cores.features) {
    const city = f.properties.city;
    const c = reader.read(f.geometry).getCentroid();
    const { fwd, inv } = projector(c.getX(), c.getY());
    const core = reader.read({ type: f.geometry.type, coordinates: mapCoords(f.geometry.coordinates, fwd) });
    const towers = [];   // completed towers with a year inside the core, and lost towers (gone < 9999) inside it
    for (const r of byCity.get(city) ?? []) {
      if (r[sch.status] !== completed || r[sch.year] == null) continue;
      const [x, y] = fwd([r[sch.lon], r[sch.lat]]);
      if (core.distance(point(x, y)) <= 1) towers.push({ year: Math.trunc(r[sch.year]), gone: 9999, height: r[sch.height_m], name: r[sch.name], x, y });
    }
    for (const t of lostByCity.get(city) ?? []) {
      const [x, y] = fwd([t.lng, t.lat]);
      if (core.distance(point(x, y)) <= 1) towers.push({ year: t.completed, gone: t.gone, height: t.height, name: t.name, x, y });
    }
    towers.sort((a, b) => a.year - b.year || a.height - b.height || (a.name < b.name ? -1 : a.name > b.name ? 1 : 0) || a.x - b.x || a.y - b.y);
    const standing = towers.filter(t => t.gone === 9999);
    const years = [...new Set(towers.map(t => t.year))];
    const parts = polygons(core);
    let frames;
    try {
      frames = framesWithLosses(parts, towers);
    } catch (e) {   // never fail the build over one city: show its drawn core once it has MIN_TOWERS towers
      console.warn(`skyline years: ${city} failed (${e.message ?? e}); showing its drawn core throughout`);
      const y = standing[MIN_TOWERS - 1]?.year;
      frames = y == null ? [] : [{ year: y, n: standing.filter(t => t.year <= y).length, area: core,
        tallest: standing.filter(t => t.year <= y).reduce((a, b) => b.height > a.height ? b : a) }];
    }
    frames.forEach((fr, k) => {
      const last = k + 1 === frames.length, t = fr.tallest;
      let geometry = null;   // last keyframe: the drawn core itself, filled in by the map
      if (!last) {
        const g = writer.write(TopologyPreservingSimplifier.simplify(fr.area, SIMPLIFY));
        geometry = { type: g.type, coordinates: mapCoords(g.coordinates, inv) };
      }
      feats.push({ type: "Feature", properties: {
        city, from: fr.year, to: last ? 9999 : frames[k + 1].year, n: fr.n, total: standing.length,
        tallest: t ? `${t.name} (${Math.round(t.height)} m, ${t.year})` : "",
        area_km2: Math.round((last ? core : fr.area).getArea() / 1e4) / 100,
        core_km2: Math.round(core.getArea() / 1e4) / 100,
      }, geometry });
    });
    report.push([city, standing.length, years[0] ?? "-", frames[0]?.year ?? "-", frames.length,
      frames.length ? (frames.at(-1).area.getArea() / core.getArea()).toFixed(3) : "0"]);
  }
  const text = JSON.stringify({ type: "FeatureCollection", inputs, features: feats });
  writeFileSync(out, text);
  console.log(`skyline years: ${out}, ${feats.length} keyframes for ${cores.features.length} cities, ${(text.length / 1e6).toFixed(2)} MB, ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  if (process.env.SKYLINE_YEARS_REPORT) {
    console.log("  city            towers  first  shown from  keyframes  computed/drawn core at the end");
    for (const [a, b, c, d, e, g] of report)
      console.log(`  ${String(a).padEnd(15)} ${String(b).padStart(6)}  ${String(c).padStart(5)}  ${String(d).padStart(10)}  ${String(e).padStart(9)}  ${g}`);
  }
}

if (import.meta.url === `file://${process.argv[1]}`) buildSkylineYears();
