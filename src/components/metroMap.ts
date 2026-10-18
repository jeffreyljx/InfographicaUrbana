"use client";
import type { Feature, FeatureCollection, LineString, Point } from "geojson";
import { Map as MLMap, AttributionControl, NavigationControl, ScaleControl, setWorkerUrl, type GeoJSONSource, type MapMouseEvent, type ExpressionSpecification } from "maplibre-gl";
import { STYLE_URL, warmBasemap, registerOwnLayer } from "./towerMap";
import { NEVER_YEAR, type MetroData } from "@/lib/metro";
import { addStructureLayers, setStructureYear, STRUCT_CLICK } from "./metroStructures";

/* The /metro map: the same warm basemap (and satellite switch) as the tower map, with every metro line drawn stretch by
 * stretch from the year it opened, station bubbles in their line's colour (an interchange is drawn larger, in ink),
 * and, zoomed out, one dot per system sized by its length in the chosen year. The year is applied with filters and
 * paint expressions, so moving it never rebuilds the data. Zoomed in, each station shows its structure and exits
 * (metroStructures.ts).
 *
 * Where lines share track (or run right beside each other) the map draws one bundle, not each line on top of the
 * others: a single line, thickened by half a line's width for each further line open there, with lines of one colour
 * as one stripe and other colours as stripes side by side. The bundle's members and their opening years ride on each
 * feature (l0…, y0…, x0…), so its width and each stripe's offset follow the year. */

const LAND = "#E6D6CF";
const BLANK_STYLE = {
  version: 8 as const,
  glyphs: "https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf",
  sources: {},
  layers: [{ id: "bg", type: "background" as const, paint: { "background-color": LAND } }],
};
/** stretches opened in the chosen year glow in the time capsule's new-this-year orange */
export const NEW_COLOR = "#E2560F";
const INK = "#2B1D17";
const HALO = "#FAF4F1";
/** below this zoom the systems show as dots; lines and dots cross-fade around it */
export const SYSTEM_ZOOM = 6.5;

const LAYERS = ["metro-systems", "metro-casing", "metro-new", "metro-lines", "metro-sel-line", "metro-stations", "metro-sel-station", "metro-station-labels", "metro-system-labels"];
for (const id of LAYERS) registerOwnLayer(id);

let workerSet = false;
export function createMetroMap(container: HTMLDivElement, center: [number, number], zoom: number): MLMap {
  if (!workerSet) { setWorkerUrl("/maplibre/maplibre-gl-worker.mjs"); workerSet = true; }
  const map = new MLMap({ container, style: STYLE_URL, center, zoom, minZoom: 1.2, maxZoom: 19, attributionControl: false, hash: false });
  let styleFailed = false;
  map.on("style.load", () => warmBasemap(map));
  map.on("error", (e) => {
    if (styleFailed || map.isStyleLoaded()) return;
    const err = (e as unknown as { error?: Error & { url?: string } }).error;
    if (!err?.url || !err.url.startsWith(STYLE_URL)) return;
    styleFailed = true;
    map.setStyle(BLANK_STYLE as unknown as string);
  });
  map.addControl(new AttributionControl({
    compact: true,
    customAttribution: 'Metro lines and stations © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors · opening dates from Wikipedia',
  }), "bottom-right");
  map.addControl(new ScaleControl({ maxWidth: 120, unit: "metric" }), "bottom-right");
  map.addControl(new NavigationControl({ showCompass: false }), "bottom-left");
  (window as unknown as { __map?: MLMap }).__map = map;
  return map;
}

/** One drawn stripe: the lines on its piece of corridor as [line, year its stretch there opened, year the line closed],
 *  in stripe order, and the members g0 ≤ k < g1 it draws (the lines of one colour). Feature id = index here. */
interface Stripe { m: [number, number, number][]; g0: number; g1: number }
let stripes: Stripe[] = [];
/** what each stripe shows now, as set in its feature state (a year change sets only the stripes that change) */
interface StripeState { on: number; f: number; g: number; nw: number; sel: number; dim: number }
let states: (StripeState | undefined)[] = [];

/** Track as features: one per stripe of a bundle (lines of one colour on one piece of corridor), carrying only its
 *  colour; what it shows in a year (width, offset, glow) is set as feature state by setMetroYear. Without bundles in
 *  the data, each line's own runs of track, as one-line bundles. */
export function trackFeatures(d: MetroData): FeatureCollection<LineString> {
  const pieces: { coords: [number, number][]; members: [number, number][] }[] = d.bundles.length ? d.bundles
    : d.tracks.flatMap(t => t.runs.map(r => ({ coords: t.coords.slice(r.from, r.to + 1), members: [[t.line, r.year]] as [number, number][] })));
  stripes = []; states = [];
  const features: Feature<LineString>[] = [];
  for (const p of pieces) {
    const m = p.members.map(([l, y]) => [l, y, d.lines[l].closeYear] as [number, number, number]);
    for (let g0 = 0; g0 < m.length;) {
      const c = d.lines[m[g0][0]].colour;
      let g1 = g0 + 1;
      while (g1 < m.length && d.lines[m[g1][0]].colour === c) g1++;
      features.push({ type: "Feature", id: stripes.length, geometry: { type: "LineString", coordinates: p.coords }, properties: { c } });
      stripes.push({ m, g0, g1 });
      g0 = g1;
    }
  }
  return { type: "FeatureCollection", features };
}

/** A stripe in `year`: shown if any of its lines is open; the bundle is one line wide plus half a line for each further
 *  line open on the piece, shared equally, so f is this stripe's width and g its centre right of the corridor's centre
 *  line, both in line widths; nw: one of its lines opened here this year; sel: it carries the selected line. */
function stripeState(s: Stripe, year: number, line: number | null): StripeState {
  let n = 0, before = 0, own = 0, nw = 0, sel = 0;
  s.m.forEach(([l, y, x], k) => {
    if (y > year || x <= year) return;
    n++;
    if (k < s.g0) before++;
    else if (k < s.g1) { own++; if (y === year) nw = 1; if (l === line) sel = 1; }
  });
  const dim = line === null ? 0 : 1;
  if (!own) return { on: 0, f: 0, g: 0, nw: 0, sel: 0, dim };
  const share = (n + 1) / (2 * n);
  return { on: 1, f: own * share, g: (before + own / 2 - n / 2) * share, nw, sel, dim };
}

const fs = (k: keyof StripeState): ExpressionSpecification => ["number", ["feature-state", k], 0];
/** a line width scaled by a feature-state expression, plus `add` pixels */
const ZOOMS: [number, number][] = [[2, 0.6], [6, 1.1], [10, 2.2], [13, 3.6], [16, 6]];
const scaled = (k: ExpressionSpecification, add = 0): ExpressionSpecification =>
  ["interpolate", ["exponential", 1.4], ["zoom"], ...ZOOMS.flatMap(([z, w]) => [z, add ? ["+", ["*", w, k], add] : ["*", w, k]])] as ExpressionSpecification;

/** the year and line last shown (a click on a stripe picks the line it means with them) */
let shownYear = NEVER_YEAR, shownLine: number | null = null;
/** the line a click on stripe `id` means: the selected line if the stripe carries it, else its first line open now;
 *  null for a stripe not shown this year */
function lineOfStripe(id: number): number | null {
  const s = stripes[id];
  if (!s || !states[id]?.on) return null;
  let first: number | null = null;
  for (let k = s.g0; k < s.g1; k++) {
    const [l, y, x] = s.m[k];
    if (y > shownYear || x <= shownYear) continue;
    if (l === shownLine) return l;
    first ??= l;
  }
  return first;
}

/** Stations: i index, y first year, y2 year it became an interchange, x closing year, c colour of its first line, n label. */
export function stationFeatures(d: MetroData): FeatureCollection<Point> {
  return {
    type: "FeatureCollection",
    features: d.stations.map(st => ({
      type: "Feature", id: st.i, geometry: { type: "Point", coordinates: [st.lon, st.lat] },
      properties: { i: st.i, y: st.firstYear, y2: st.interYear, x: st.closeYear, c: d.lines[st.lines[0][0]].colour, n: st.en || st.name },
    })),
  };
}

/** Systems as dots for the world view, sized by the km open in the chosen year (none drawn before a system opens). */
export function systemFeatures(d: MetroData, kmBySys: number[]): FeatureCollection<Point> {
  return {
    type: "FeatureCollection",
    features: d.systems.filter(s => s.placed && kmBySys[s.i] > 0.05).map(s => ({
      type: "Feature", geometry: { type: "Point", coordinates: [s.lon, s.lat] },
      properties: { s: s.i, k: kmBySys[s.i], n: s.city },
    })),
  };
}

export interface MetroCallbacks {
  onLine: (line: number) => void;
  onStation: (station: number) => void;
  onSystem: (system: number) => void;
}

export function addMetroLayers(map: MLMap, d: MetroData, kmBySys: number[], year: number, cb: MetroCallbacks) {
  map.addSource("metro-track", { type: "geojson", data: trackFeatures(d), tolerance: 0.25 });
  map.addSource("metro-stations", { type: "geojson", data: stationFeatures(d), promoteId: "i" });
  map.addSource("metro-systems", { type: "geojson", data: systemFeatures(d, kmBySys) });

  map.addLayer({
    id: "metro-systems", type: "circle", source: "metro-systems", maxzoom: SYSTEM_ZOOM + 1,
    paint: {
      "circle-radius": ["interpolate", ["linear"], ["sqrt", ["get", "k"]], 0, 2.5, 10, 9, 30, 22],
      "circle-color": "#7F2F16",
      "circle-opacity": ["interpolate", ["linear"], ["zoom"], 4, 0.55, SYSTEM_ZOOM, 0.4, SYSTEM_ZOOM + 1, 0],
      "circle-stroke-width": 1, "circle-stroke-color": HALO,
      "circle-stroke-opacity": ["interpolate", ["linear"], ["zoom"], SYSTEM_ZOOM, 0.8, SYSTEM_ZOOM + 1, 0],
    },
  });
  map.addLayer({
    id: "metro-casing", type: "line", source: "metro-track", minzoom: 4,
    layout: { "line-join": "round", "line-cap": "round" },
    paint: {
      "line-color": HALO, "line-width": scaled(fs("f"), 2.2), "line-offset": scaled(fs("g")),
      "line-opacity": ["interpolate", ["linear"], ["zoom"], 4, 0, 7, ["*", 0.85, fs("on")]],
    },
  });
  map.addLayer({
    id: "metro-new", type: "line", source: "metro-track",
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": NEW_COLOR, "line-width": scaled(fs("f"), 9), "line-offset": scaled(fs("g")), "line-opacity": ["*", 0.45, fs("nw")], "line-blur": 4 },
  });
  map.addLayer({
    id: "metro-lines", type: "line", source: "metro-track",
    layout: { "line-join": "round", "line-cap": "round" },
    paint: {
      "line-color": ["get", "c"], "line-width": scaled(fs("f")), "line-offset": scaled(fs("g")),
      "line-opacity": ["*", fs("on"), ["case", [">", fs("dim"), 0], 0.4, 1]],
    },
  });
  map.addLayer({
    id: "metro-sel-line", type: "line", source: "metro-track",
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": ["get", "c"], "line-width": scaled(["+", fs("f"), 0.9] as ExpressionSpecification), "line-offset": scaled(fs("g")), "line-opacity": fs("sel") },
  });
  map.addLayer({
    id: "metro-stations", type: "circle", source: "metro-stations", minzoom: 9.5,
    paint: {
      "circle-radius": ["interpolate", ["linear"], ["zoom"], 9.5, 1.8, 12, 3.4, 15, 6],
      "circle-color": "#FFFFFF",
      "circle-stroke-width": ["interpolate", ["linear"], ["zoom"], 9.5, 1, 13, 1.8, 16, 2.6],
      "circle-stroke-color": ["get", "c"],
      "circle-opacity": ["interpolate", ["linear"], ["zoom"], 9.5, 0, 10.2, 1],
      "circle-stroke-opacity": ["interpolate", ["linear"], ["zoom"], 9.5, 0, 10.2, 1],
    },
  });
  map.addLayer({
    id: "metro-sel-station", type: "circle", source: "metro-stations", filter: ["==", ["get", "i"], -1],
    paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 8, 8, 15, 13], "circle-color": "rgba(0,0,0,0)", "circle-stroke-width": 2.5, "circle-stroke-color": INK },
  });
  map.addLayer({
    id: "metro-station-labels", type: "symbol", source: "metro-stations", minzoom: 12.8,
    layout: {
      "text-field": ["get", "n"], "text-font": ["Noto Sans Regular"], "text-size": 11.5,
      "text-offset": [0, 0.9], "text-anchor": "top", "text-optional": true, "text-max-width": 9,
      "symbol-sort-key": ["get", "y"],
    },
    paint: { "text-color": INK, "text-halo-color": HALO, "text-halo-width": 1.4 },
  });
  map.addLayer({
    id: "metro-system-labels", type: "symbol", source: "metro-systems", minzoom: 3.2, maxzoom: SYSTEM_ZOOM + 0.5,
    layout: {
      "text-field": ["get", "n"], "text-font": ["Noto Sans Regular"], "text-size": 11,
      "text-offset": [0, 0.8], "text-anchor": "top", "text-optional": true, "symbol-sort-key": ["-", 0, ["get", "k"]],
    },
    paint: { "text-color": INK, "text-halo-color": HALO, "text-halo-width": 1.3 },
  });
  addStructureLayers(map, d);
  setMetroYear(map, year, null);

  // clicks: a station (its bubble, an exit or its box) beats a line, which beats a system dot
  map.on("click", (e: MapMouseEvent) => {
    const pad = 6;
    const box: [[number, number], [number, number]] = [[e.point.x - pad, e.point.y - pad], [e.point.x + pad, e.point.y + pad]];
    const st = map.queryRenderedFeatures(box, { layers: ["metro-stations"] })[0];
    if (st) { cb.onStation(st.properties!.i as number); return; }
    const sx = map.queryRenderedFeatures(box, { layers: STRUCT_CLICK.filter(l => map.getLayer(l)) })[0];
    if (sx) { cb.onStation(sx.properties!.i as number); return; }
    const li = map.queryRenderedFeatures(box, { layers: ["metro-sel-line", "metro-lines"] })
      .map(f => lineOfStripe(f.id as number)).find(l => l !== null);
    if (li !== undefined && li !== null) { cb.onLine(li); return; }
    const sy = map.queryRenderedFeatures(box, { layers: ["metro-systems"] })[0];
    if (sy && map.getZoom() < SYSTEM_ZOOM + 0.5) cb.onSystem(sy.properties!.s as number);
  });
  for (const l of ["metro-stations", "metro-systems"]) {
    map.on("mouseenter", l, () => { map.getCanvas().style.cursor = "pointer"; });
    map.on("mouseleave", l, () => { map.getCanvas().style.cursor = ""; });
  }
  // track not open in the chosen year is still there, transparent: only a stripe shown this year takes the pointer
  let overLine = false;
  map.on("mousemove", "metro-lines", (e) => {
    const on = !!e.features?.some(f => states[f.id as number]?.on);
    if (on !== overLine) { overLine = on; map.getCanvas().style.cursor = on ? "pointer" : ""; }
  });
  map.on("mouseleave", "metro-lines", () => { if (overLine) { overLine = false; map.getCanvas().style.cursor = ""; } });
}

/** Show the network as it stood in `year`: track and stations open then, the stretches opened that year glowing.
 *  `line`: the selected line, drawn wider over the rest (which fade a little). */
export function setMetroYear(map: MLMap, year: number, line: number | null) {
  if (!map.getLayer("metro-lines")) return;
  shownYear = year; shownLine = line;
  // each stripe's width, place in its bundle and glow, as feature state: only the stripes that change are touched,
  // and nothing is re-tiled, so stepping through the years stays quick
  for (let id = 0; id < stripes.length; id++) {
    const st = stripeState(stripes[id], year, line), was = states[id];
    if (was && was.on === st.on && was.f === st.f && was.g === st.g && was.nw === st.nw && was.sel === st.sel && was.dim === st.dim) continue;
    if (!was && !st.on) { states[id] = st; continue; }
    map.setFeatureState({ source: "metro-track", id }, st as unknown as Record<string, number>);
    states[id] = st;
  }
  const open: ExpressionSpecification = ["all", ["<=", ["get", "y"], year], [">", ["get", "x"], year]];
  map.setFilter("metro-stations", open);
  map.setFilter("metro-station-labels", open);
  // a station two open lines meet at is drawn as an interchange: larger, with an ink ring
  map.setPaintProperty("metro-stations", "circle-stroke-color", ["case", ["<=", ["get", "y2"], year], INK, ["get", "c"]]);
  setStructureYear(map, year);
  map.setPaintProperty("metro-stations", "circle-radius", ["interpolate", ["linear"], ["zoom"],
    9.5, ["case", ["<=", ["get", "y2"], year], 2.6, 1.8], 12, ["case", ["<=", ["get", "y2"], year], 4.6, 3.4], 15, ["case", ["<=", ["get", "y2"], year], 8, 6]]);
}

export function setSystemDots(map: MLMap, d: MetroData, kmBySys: number[]) {
  (map.getSource("metro-systems") as GeoJSONSource | undefined)?.setData(systemFeatures(d, kmBySys));
}

export function setSelectedStation(map: MLMap, station: number | null) {
  if (map.getLayer("metro-sel-station")) map.setFilter("metro-sel-station", ["==", ["get", "i"], station ?? -1]);
}

export { NEVER_YEAR };
