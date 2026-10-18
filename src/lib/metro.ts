"use client";
/**
 * The world's metro systems for the /metro page, read from public/metro/metro.json. That file is packed from the
 * project's metro database (metro/db: Wikipedia for the facts and opening stages, OpenStreetMap of 8 Oct 2026 for the
 * track and stations) by scripts/metro/build_metro.py. Only lines that pass the project's metro definition are in it.
 *
 * Layout of metro.json (arrays rather than objects, to keep it small):
 *   systems:  [id, name, city, country, iso2, first opened, annual riders (millions), riders year, length km, stations]
 *   lines:    [id, system, ref, name, local name, colour, opened, latest extension, closed, status, length km,
 *              mapped km, stations, mapped stations, annual riders (millions), daily riders (thousands), riders year,
 *              rolling stock, car type, cars per train, power, gauge mm, automation, technology, express (0/1),
 *              national mode, operator, termini, sources (space-separated URLs), routes (station sequences)]
 *   geom:     [line, polyline (1e-5), [year, stretches, year, stretches, …]]: each mapped run of track, cut into the
 *              years its stretches opened (a stretch takes the year of the nearest dated station-to-station segment)
 *   stations: columns name, en, lon, lat (1e-5 degrees, delta-coded), lines ([[line, year it reached the station]]), wd
 *   stages:   per line, [event, date, from, to, km]
 *   bundles:  [polyline (1e-5), [line, year, line, year, …]]: the track as drawn, one entry per piece of corridor with
 *              every line on it (where lines share track, or run right beside each other) and the year each line's
 *              stretch there opened, in stripe order (scripts/metro/build_bundles.py). Absent in older files.
 */

export interface MetroSystem {
  i: number; id: string; name: string; city: string; country: string; iso2: string; firstOpened: string;
  riders: number | null; ridersYear: string; km: number | null; stations: number | null;
  /** first year any of its lines opened (from the track) */
  first: number; lon: number; lat: number; bbox: [number, number, number, number];
  /** false for a system with neither mapped track nor stations (it still counts in the km totals) */
  placed: boolean;
}
export interface MetroLine {
  i: number; id: string; sys: number; ref: string; name: string; local: string; colour: string;
  opened: string; ext: string; closed: string; status: string; km: number | null; kmOsm: number | null;
  stations: number | null; stationsOsm: number | null; riders: number | null; ridersDaily: number | null; ridersYear: string;
  stock: string; carType: string; cars: string; power: string; gauge: string; automation: string; tech: string;
  express: boolean; nationalMode: string; operator: string; termini: string; sources: string[];
  /** mapped routes as station sequences (indices into stations), longest first */
  routes: number[][];
  openYear: number; closeYear: number; stages: MetroStage[];
  bbox: [number, number, number, number] | null;
}
export interface MetroStage { event: string; date: string; from: string; to: string; km: number | null }
export interface MetroStation {
  i: number; name: string; en: string; lon: number; lat: number; wd: string;
  /** [line, year that line reached the station], earliest first */
  lines: [number, number][];
  sys: number; slug: string;
  firstYear: number;
  /** year it became an interchange (two lines open there), 9999 if never */
  interYear: number;
  /** year its last line closed, 9999 if open */
  closeYear: number;
}
export interface MetroTrack { line: number; coords: [number, number][]; runs: { year: number; from: number; to: number; km: number }[] }
/** A piece of corridor and the lines on it, each with the year its stretch here opened, in stripe order. */
export interface MetroBundle { coords: [number, number][]; members: [number, number][] }
export interface MetroData {
  built: string; systems: MetroSystem[]; lines: MetroLine[]; stations: MetroStation[]; tracks: MetroTrack[];
  /** the track as drawn, shared track as one piece (empty when metro.json predates bundles: draw `tracks` then) */
  bundles: MetroBundle[];
  first: number; last: number;
  /** km of line opened (closed lines subtracted) per year, first..last, all systems; and per system */
  kmPerYear: number[]; kmPerYearBySys: number[][];
}

export const NEVER_YEAR = 9999;

function decodePolyline(str: string): [number, number][] {
  let i = 0, lat = 0, lng = 0;
  const out: [number, number][] = [];
  while (i < str.length) {
    let b: number, s = 0, r = 0;
    do { b = str.charCodeAt(i++) - 63; r |= (b & 31) << s; s += 5; } while (b >= 32);
    lat += (r & 1) ? ~(r >> 1) : (r >> 1);
    s = 0; r = 0;
    do { b = str.charCodeAt(i++) - 63; r |= (b & 31) << s; s += 5; } while (b >= 32);
    lng += (r & 1) ? ~(r >> 1) : (r >> 1);
    out.push([lng / 1e5, lat / 1e5]);
  }
  return out;
}

export function km(a: [number, number], b: [number, number]): number {
  const R = 6371.0088, rad = Math.PI / 180;
  const dLat = (b[1] - a[1]) * rad, dLon = (b[0] - a[0]) * rad;
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(a[1] * rad) * Math.cos(b[1] * rad) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(h));
}

const yearOf = (d: string) => /^\d{4}/.test(d) ? Number(d.slice(0, 4)) : null;

/** A line's colour as drawn: the database's colour, or a muted stand-in; near-white lines are greyed so they read on the sand map. */
const SPARE = ["#6B5B95", "#88B04B", "#955251", "#009B77", "#DD4124", "#45B8AC", "#5B5EA6", "#9B2335", "#BC243C", "#C3447A"];
function lineColour(raw: string, id: string): string {
  let c = raw.trim();
  if (!c) {
    let h = 0;
    for (const ch of id) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
    return SPARE[h % SPARE.length];
  }
  if (/^[0-9a-f]{6}$/i.test(c)) c = "#" + c;
  if (/^#[0-9a-f]{6}$/i.test(c)) c = c.toUpperCase();  // one spelling per colour: lines of one colour share a stripe
  const m = /^#([0-9a-f]{6})$/i.exec(c);
  if (m) {
    const n = parseInt(m[1], 16), r = n >> 16, g = (n >> 8) & 255, b = n & 255;
    if (0.2126 * r + 0.7152 * g + 0.0722 * b > 225) return "#9A8F8A";
  } else if (/^white$/i.test(c)) return "#9A8F8A";
  return c;
}

/** URL-safe name for a station within its system: its English name (else its own), lower-case, letters kept in any script. */
export function slugify(s: string): string {
  return s.normalize("NFKD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/['’`]/g, "")
    .replace(/[^\p{L}\p{N}]+/gu, "-").replace(/^-+|-+$/g, "") || "station";
}

type Raw = {
  built: string;
  systems: [string, string, string, string, string, string, number | null, string, number | null, number | null][];
  lines: unknown[][];
  geom: [number, string, number[]][];
  stations: { name: string[]; en: string[]; lon: number[]; lat: number[]; lines: [number, number | null][][]; wd: string[] };
  stages: [string, string, string, string, number | null][][];
  bundles?: [string, number[]][];
};

function decode(raw: Raw): MetroData {
  const s = raw.stations;
  let lon = 0, lat = 0;
  const lines: MetroLine[] = raw.lines.map((r, i) => {
    const [id, sys, ref, name, local, colour, opened, ext, closed, status, kmPub, kmOsm, st, stOsm, rid, ridD, ridY,
      stock, carType, cars, power, gauge, automation, tech, express, nationalMode, operator, termini, sources, routes] = r as [
      string, number, string, string, string, string, string, string, string, string, number | null, number | null, number | null, number | null,
      number | null, number | null, string, string, string, string, string, string, string, string, number, string, string, string, string, number[][]];
    return {
      i, id, sys, ref, name: name || local || ref || id.split(":")[1], local: local && local !== name ? local : "", colour: lineColour(colour, id),
      opened, ext, closed, status, km: kmPub, kmOsm, stations: st, stationsOsm: stOsm, riders: rid, ridersDaily: ridD, ridersYear: ridY,
      stock, carType, cars, power, gauge, automation, tech, express: !!express, nationalMode, operator, termini,
      sources: sources ? sources.split(/\s+/).filter(Boolean) : [], routes: routes ?? [],
      openYear: yearOf(opened) ?? NEVER_YEAR, closeYear: yearOf(closed) ?? NEVER_YEAR,
      stages: (raw.stages[i] ?? []).map(([event, date, from, to, k]) => ({ event, date, from, to, km: k })), bbox: null,
    };
  });

  const stations: MetroStation[] = s.name.map((name, i) => {
    lon += s.lon[i]; lat += s.lat[i];
    const ls = s.lines[i].map(([l, y]) => [l, y ?? lines[l].openYear] as [number, number]);
    return { i, name, en: s.en[i], lon: lon / 1e5, lat: lat / 1e5, wd: s.wd[i], lines: ls, sys: lines[ls[0][0]].sys, slug: "", firstYear: 0, interYear: NEVER_YEAR, closeYear: NEVER_YEAR };
  });
  // per-station years: first line to arrive, the second (an interchange from then), and when its last line closed
  for (const st of stations) {
    const open = st.lines.map(([l, y]) => [y, lines[l].closeYear]).sort((a, b) => a[0] - b[0]);
    st.firstYear = open[0][0];
    st.interYear = open.length > 1 ? open[1][0] : NEVER_YEAR;
    st.closeYear = Math.max(...open.map(o => o[1]));
  }
  // slugs, unique within each system (in station order)
  const seen = new Map<string, number>();
  for (const st of stations) {
    const base = `${st.sys}|${slugify(st.en || st.name)}`;
    const n = (seen.get(base) ?? 0) + 1;
    seen.set(base, n);
    st.slug = slugify(st.en || st.name) + (n > 1 ? `-${n}` : "");
  }

  const tracks: MetroTrack[] = raw.geom.map(([line, poly, runs]) => {
    const coords = decodePolyline(poly);
    const out: MetroTrack["runs"] = [];
    let at = 0;
    for (let k = 0; k < runs.length; k += 2) {
      const year = runs[k] ?? lines[line].openYear, n = runs[k + 1];
      let len = 0;
      for (let j = at; j < at + n; j++) len += km(coords[j], coords[j + 1]);
      out.push({ year, from: at, to: at + n, km: len });
      at += n;
    }
    return { line, coords, runs: out };
  });

  // bounding boxes of lines and systems, from the track (else the stations)
  const grow = (b: [number, number, number, number] | null, p: [number, number]): [number, number, number, number] =>
    b ? [Math.min(b[0], p[0]), Math.min(b[1], p[1]), Math.max(b[2], p[0]), Math.max(b[3], p[1])] : [p[0], p[1], p[0], p[1]];
  for (const t of tracks) for (const p of t.coords) lines[t.line].bbox = grow(lines[t.line].bbox, p);
  const mapped = new Set(tracks.map(t => t.line));
  for (const st of stations) for (const [l] of st.lines) if (!mapped.has(l)) lines[l].bbox = grow(lines[l].bbox, [st.lon, st.lat]);

  let first = NEVER_YEAR;
  for (const t of tracks) for (const r of t.runs) first = Math.min(first, r.year);
  const last = Math.max(new Date().getFullYear(), ...tracks.flatMap(t => t.runs.map(r => r.year)));
  const span = last - first + 1;
  // Lengths: OpenStreetMap often maps a line's two tracks apart, or its route doubles back over shared track, so the
  // drawn track of a line with a published length is scaled to that length (each stretch keeps its share); a line
  // with no mapped track (a demolished el, say) counts its published length from the year it opened.
  const drawnKm = new Array<number>(lines.length).fill(0);
  for (const t of tracks) for (const r of t.runs) drawnKm[t.line] += r.km;
  for (const t of tracks) {
    const pub = lines[t.line].km;
    if (pub && drawnKm[t.line] > 0) for (const r of t.runs) r.km *= pub / drawnKm[t.line];
  }
  const kmPerYearBySys = raw.systems.map(() => new Array<number>(span).fill(0));
  const add = (l: MetroLine, year: number, k: number) => {
    if (year > last) return;
    kmPerYearBySys[l.sys][Math.max(year, first) - first] += k;
    if (l.closeYear <= last && l.closeYear >= year) kmPerYearBySys[l.sys][l.closeYear - first] -= k;
  };
  for (const t of tracks) for (const r of t.runs) add(lines[t.line], r.year, r.km);
  for (const l of lines) if (!drawnKm[l.i] && l.km && l.openYear !== NEVER_YEAR) add(l, l.openYear, l.km);
  const kmPerYear = new Array<number>(span).fill(0);
  for (const arr of kmPerYearBySys) arr.forEach((v, k) => { kmPerYear[k] += v; });

  const systems: MetroSystem[] = raw.systems.map(([id, name, city, country, iso2, firstOpened, riders, ridersYear, kmW, stW], i) => {
    let b: [number, number, number, number] | null = null;
    for (const l of lines) if (l.sys === i && l.bbox) { b = grow(b, [l.bbox[0], l.bbox[1]]); b = grow(b, [l.bbox[2], l.bbox[3]]); }
    const fy = kmPerYearBySys[i].findIndex(v => v > 0);
    const bb = b ?? [0, 0, 0, 0];
    return {
      i, id, name, city, country, iso2, firstOpened, riders, ridersYear, km: kmW, stations: stW,
      first: fy >= 0 ? first + fy : yearOf(firstOpened) ?? NEVER_YEAR, lon: (bb[0] + bb[2]) / 2, lat: (bb[1] + bb[3]) / 2, bbox: bb, placed: b !== null,
    };
  });
  const bundles: MetroBundle[] = (raw.bundles ?? []).map(([poly, m]) => {
    const members: [number, number][] = [];
    for (let k = 0; k < m.length; k += 2) members.push([m[k], m[k + 1]]);
    return { coords: decodePolyline(poly), members };
  });
  return { built: raw.built, systems, lines, stations, tracks, bundles, first, last, kmPerYear, kmPerYearBySys };
}

let promise: Promise<MetroData> | null = null;
export function loadMetro(): Promise<MetroData> {
  if (!promise) promise = fetch("/metro/metro.json").then(r => { if (!r.ok) throw new Error(`metro.json: ${r.status}`); return r.json(); }).then(decode);
  return promise;
}

/** Km of line open in `year`, per system (cumulative of kmPerYearBySys). */
export function kmOpenBySystem(d: MetroData, year: number): number[] {
  const k = Math.min(year, d.last) - d.first;
  return d.kmPerYearBySys.map(arr => { let s = 0; for (let j = 0; j <= k; j++) s += arr[j]; return Math.max(0, s); });
}

/** The station's place in the URL: ?station=<system id>~<slug>. */
export function stationKey(d: MetroData, st: MetroStation): string {
  return `${d.systems[st.sys].id}~${st.slug}`;
}
export function stationByKey(d: MetroData, key: string): MetroStation | undefined {
  const [sysId, slug] = key.split("~");
  const sys = d.systems.findIndex(s => s.id === sysId);
  return sys < 0 ? undefined : d.stations.find(st => st.sys === sys && st.slug === slug);
}

/** A station's neighbours along a line (the stations either side of it on each mapped route of that line). */
export function neighbours(line: MetroLine, station: number): { prev: number | null; next: number | null }[] {
  const out: { prev: number | null; next: number | null }[] = [];
  const seen = new Set<string>();
  for (const r of line.routes) {
    const k = r.indexOf(station);
    if (k < 0) continue;
    const p = k > 0 ? r[k - 1] : null, n = k < r.length - 1 ? r[k + 1] : null;
    const key = `${p}|${n}`;
    if (seen.has(key) || seen.has(`${n}|${p}`)) continue;
    seen.add(key);
    out.push({ prev: p, next: n });
  }
  return out;
}

export const fmtKm = (v: number) => v >= 100 ? Math.round(v).toLocaleString("en-US") : v.toFixed(1);
export const fmtInt = (v: number) => Math.round(v).toLocaleString("en-US");
export function stationLabel(st: MetroStation): string { return st.en || st.name; }
export function lineLabel(l: MetroLine): string { return l.name; }
