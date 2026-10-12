"use client";
import type { FeatureCollection, Point } from "geojson";
import { Map as MLMap, AttributionControl, NavigationControl, ScaleControl, setWorkerUrl, type GeoJSONSource, type MapMouseEvent } from "maplibre-gl";
import type { TowerIndex, TowerRow } from "@/lib/types";
import { BAND_COLORS, BAND_STROKE, CLUSTER_COLORS } from "@/lib/colors";

export const STYLE_URL = process.env.NEXT_PUBLIC_MAP_STYLE || "https://tiles.openfreemap.org/styles/positron";
/** The site's pale sand background; the basemap's land is drawn in exactly this colour. */
const LAND = "#E6D6CF";
/** Used if the basemap style cannot be fetched: pins still render on a plain ground. */
const BLANK_STYLE = {
  version: 8 as const,
  glyphs: "https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf",
  sources: {},
  layers: [{ id: "bg", type: "background" as const, paint: { "background-color": LAND } }],
};
export const CLUSTER_MAX_ZOOM = 15;

/** Satellite basemap: Esri World Imagery raster tiles under the same tower layers. */
export type Basemap = "map" | "satellite";
const SAT_ID = "esri-imagery";
const SAT_TILES = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}";
const SAT_ATTR = 'Imagery © <a href="https://www.esri.com/" target="_blank" rel="noopener">Esri</a>, Maxar, Earthstar Geographics';
const TOWER_LAYERS = new Set(["clusters", "cluster-count", "glow", "pins", "capsule-new-clusters", "capsule-new", "capsule-lost", "selected", "labels", "capsule-lost-label"]);
/** Time capsule: ring colour for towers completed in the chosen year (reads on the sand map and on imagery). */
const NEW_COLOR = "#E2560F";
/** Time capsule: the ghost ring left where a tower came down, in the year it did. */
const GHOST_COLOR = "#5E4E47";
const NEVER: NonNullable<Parameters<MLMap["setFilter"]>[1]> = ["==", ["get", "id"], -1];
/** Outline of the city or district opened on the map (red dashed line, drawn under the pins). */
const BOUNDARY_ID = "boundary";
const OWN_LAYERS = new Set([...TOWER_LAYERS, "boundary-line"]);
const EMPTY: FeatureCollection = { type: "FeatureCollection", features: [] };

export interface MapCallbacks {
  onSelect: (id: number) => void;
  onChoose: (ids: number[], at: { x: number; y: number }) => void;
  onMoveEnd?: () => void;
}

/** `gone` (time capsule): lost towers' ids -> the year they came down, kept as `g` for their labels. */
export function rowsToGeoJSON(rows: TowerRow[], gone?: Map<number, number>): FeatureCollection {
  return {
    type: "FeatureCollection",
    features: rows.map(r => ({
      type: "Feature",
      id: r[0],
      geometry: { type: "Point", coordinates: [r[3], r[2]] },
      properties: { id: r[0], n: r[1], h: r[4], b: r[4] >= 400 ? 3 : r[4] >= 300 ? 2 : r[4] >= 200 ? 1 : 0, p: r[11], sp: r[12], y: r[8] ?? 0, g: gone?.get(r[0]) ?? 0 },
    })),
  };
}

let workerSet = false;
export function createMap(container: HTMLDivElement, center: [number, number], zoom: number): MLMap {
  if (!workerSet) { setWorkerUrl("/maplibre/maplibre-gl-worker.mjs"); workerSet = true; }
  const map = new MLMap({
    container,
    style: STYLE_URL,
    center, zoom,
    minZoom: 1.2,
    maxZoom: 19,
    attributionControl: false,
    hash: false,
  });
  // If the style fails (offline, provider down), fall back to a blank ground so the data still shows.
  let styleFailed = false;
  // Positron is all neutral greys; re-tint it to the site's warm palette as soon as the style is parsed (before tiles draw).
  map.on("style.load", () => warmBasemap(map));
  map.on("error", (e) => {
    if (styleFailed || map.isStyleLoaded()) return;
    const err = (e as unknown as { error?: Error & { url?: string } }).error;
    const isStyle = !!err?.url && err.url.startsWith(STYLE_URL);
    if (!isStyle) return;
    styleFailed = true;
    console.warn("Basemap style failed, using blank ground:", err?.message);
    map.setStyle(BLANK_STYLE as unknown as string);
  });
  map.addControl(new AttributionControl({
    compact: true,
    customAttribution: 'Building data © <a href="https://www.skyscrapercenter.com/" target="_blank" rel="noopener">CTBUH</a> · Coordinates and boundaries partly © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors',
  }), "bottom-right");
  // Distance scale in m / km, redrawn by MapLibre on every move and zoom; added after the attribution, so it sits just above it.
  map.addControl(new ScaleControl({ maxWidth: 120, unit: "metric" }), "bottom-right");
  map.addControl(new NavigationControl({ showCompass: false }), "bottom-left");
  (window as unknown as { __map?: MLMap }).__map = map;
  return map;
}

/* ---- warm basemap ----
 * Every colour in the (neutral grey) Positron style is re-mapped by its lightness onto a warm brown ramp whose
 * land tone is exactly the site background; water gets a light slate blue (rendered about #9CB4BC). Expressions (zoom interpolations)
 * are walked so every colour inside them is mapped too. */
type RGBA = { r: number; g: number; b: number; a: number };
function parseColor(c: string): RGBA | null {
  const s = c.trim().toLowerCase();
  let m = /^#([0-9a-f]{3,8})$/.exec(s);
  if (m) {
    let h = m[1];
    if (h.length === 3 || h.length === 4) h = [...h].map(x => x + x).join("");
    const n = (i: number) => parseInt(h.slice(i, i + 2), 16);
    return { r: n(0) / 255, g: n(2) / 255, b: n(4) / 255, a: h.length === 8 ? n(6) / 255 : 1 };
  }
  m = /^rgba?\(([^)]+)\)$/.exec(s);
  if (m) {
    const p = m[1].split(",").map(x => parseFloat(x));
    return { r: p[0] / 255, g: p[1] / 255, b: p[2] / 255, a: p[3] ?? 1 };
  }
  m = /^hsla?\(([^)]+)\)$/.exec(s);
  if (m) {
    const p = m[1].split(",").map(x => parseFloat(x));
    const [h, sat, l] = [p[0], p[1] / 100, p[2] / 100];
    const k = (n: number) => (n + h / 30) % 12, a = sat * Math.min(l, 1 - l);
    const f = (n: number) => l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
    return { r: f(0), g: f(8), b: f(4), a: p[3] ?? 1 };
  }
  return null;
}
const RAMP: [number, number][] = [[0, 0.12], [0.4, 0.34], [0.7, 0.6], [0.85, 0.74], [0.945, 0.857], [1, 0.955]];
function rampL(l: number) {
  for (let i = 1; i < RAMP.length; i++) {
    const [x0, y0] = RAMP[i - 1], [x1, y1] = RAMP[i];
    if (l <= x1) return y0 + (y1 - y0) * (l - x0) / (x1 - x0);
  }
  return RAMP[RAMP.length - 1][1];
}
function warmColor(c: string, water: boolean): string {
  const v = parseColor(c);
  if (!v) return c;
  const max = Math.max(v.r, v.g, v.b), min = Math.min(v.r, v.g, v.b), l = (max + min) / 2, d = max - min;
  const srcS = d === 0 ? 0 : d / (1 - Math.abs(2 * l - 1));
  let hue = 18, sat = 0.32;                                   // the hue and saturation of the sand background
  if (water) { hue = 200; sat = 0.18; }
  else if (srcS > 0.15) {                                     // a coloured source (blue water labels): keep its hue
    const hr = max === v.r ? ((v.g - v.b) / d) % 6 : max === v.g ? (v.b - v.r) / d + 2 : (v.r - v.g) / d + 4;
    hue = (hr * 60 + 360) % 360; sat = Math.min(srcS, 0.35);
  }
  const L = rampL(l);
  if (L < 0.4 && !water) sat = Math.min(sat, 0.28);
  return `hsla(${hue.toFixed(0)},${(sat * 100).toFixed(0)}%,${(L * 100).toFixed(1)}%,${+v.a.toFixed(3)})`;
}
function warmValue(v: unknown, water: boolean): unknown {
  if (typeof v === "string") return warmColor(v, water);
  if (Array.isArray(v)) return v.map(x => warmValue(x, water));
  return v;
}
export function warmBasemap(map: MLMap) {
  const style = map.getStyle();
  if (!style) return;
  for (const l of style.layers) {
    if (OWN_LAYERS.has(l.id) || l.id === SAT_ID || !("paint" in l) || !l.paint) continue;
    const water = /water/.test(l.id) && l.type !== "symbol";
    for (const [prop, val] of Object.entries(l.paint as Record<string, unknown>)) {
      if (!prop.endsWith("color")) continue;
      const key = prop as Parameters<MLMap["setPaintProperty"]>[1];
      map.setPaintProperty(l.id, key, (l.type === "background" ? LAND : warmValue(val, water)) as Parameters<MLMap["setPaintProperty"]>[2]);
    }
  }
}

export function addTowerLayers(map: MLMap, data: FeatureCollection, cb: MapCallbacks) {
  map.addSource(BOUNDARY_ID, { type: "geojson", data: EMPTY });
  map.addLayer({
    id: "boundary-line", type: "line", source: BOUNDARY_ID,
    layout: { "line-join": "round", "line-cap": "butt" },
    paint: {
      "line-color": "#B42318",
      "line-opacity": 0.8,
      "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1.4, 10, 2, 15, 2.6],
      "line-dasharray": [3, 2],
    },
  });
  map.addSource("towers", {
    type: "geojson",
    data,
    cluster: true,
    clusterRadius: 34,
    clusterMaxZoom: CLUSTER_MAX_ZOOM,
    clusterProperties: { maxb: ["max", ["get", "b"]], maxy: ["max", ["get", "y"]] },
    promoteId: "id",
  });

  map.addLayer({
    id: "clusters", type: "circle", source: "towers", filter: ["has", "point_count"],
    paint: {
      "circle-color": ["step", ["get", "point_count"], CLUSTER_COLORS[0], 10, CLUSTER_COLORS[1], 50, CLUSTER_COLORS[2], 200, CLUSTER_COLORS[3]],
      "circle-radius": ["step", ["get", "point_count"], 14, 10, 18, 50, 23, 200, 29, 600, 36],
      "circle-stroke-width": 2,
      "circle-stroke-color": ["match", ["get", "maxb"], 3, BAND_COLORS[3], 2, BAND_COLORS[2], 1, BAND_COLORS[1], BAND_COLORS[0]],
      "circle-opacity": 0.92,
    },
  });
  map.addLayer({
    id: "cluster-count", type: "symbol", source: "towers", filter: ["has", "point_count"],
    layout: { "text-field": ["get", "point_count_abbreviated"], "text-font": ["Noto Sans Bold"], "text-size": 12, "text-allow-overlap": true },
    paint: { "text-color": "#FFF6F0" },
  });
  // glow under supertalls
  map.addLayer({
    id: "glow", type: "circle", source: "towers", filter: ["all", ["!", ["has", "point_count"]], [">=", ["get", "b"], 2]],
    paint: {
      "circle-radius": ["interpolate", ["linear"], ["zoom"], 8, 10, 14, 18],
      "circle-color": ["match", ["get", "b"], 3, BAND_COLORS[3], BAND_COLORS[2]],
      "circle-opacity": 0.22, "circle-blur": 1,
    },
  });
  map.addLayer({
    id: "pins", type: "circle", source: "towers", filter: ["!", ["has", "point_count"]],
    paint: {
      "circle-radius": ["interpolate", ["linear"], ["zoom"], 8, ["match", ["get", "b"], 3, 6, 2, 5, 1, 4, 3.5], 15, ["match", ["get", "b"], 3, 10, 2, 9, 1, 7.5, 6.5]],
      "circle-color": ["case", ["==", ["get", "p"], 4], "rgba(0,0,0,0)", ["match", ["get", "b"], 3, BAND_COLORS[3], 2, BAND_COLORS[2], 1, BAND_COLORS[1], BAND_COLORS[0]]],
      "circle-stroke-width": ["case", ["==", ["get", "p"], 4], 2, 1.25],
      "circle-stroke-color": ["case", ["==", ["get", "p"], 4],
        ["match", ["get", "b"], 3, BAND_COLORS[3], 2, BAND_COLORS[2], 1, BAND_COLORS[1], BAND_COLORS[0]],
        ["match", ["get", "b"], 3, BAND_STROKE[3], 2, BAND_STROKE[2], 1, BAND_STROKE[1], BAND_STROKE[0]]],
      "circle-opacity": 0.95,
    },
  });
  // time capsule: rings around the towers (and the clusters holding towers) completed in the chosen year; see setCapsuleYear
  map.addLayer({
    id: "capsule-new-clusters", type: "circle", source: "towers", filter: NEVER,
    paint: {
      "circle-radius": ["step", ["get", "point_count"], 19, 10, 23, 50, 28, 200, 34, 600, 41],
      "circle-color": "rgba(0,0,0,0)", "circle-stroke-width": 2.5, "circle-stroke-color": NEW_COLOR, "circle-stroke-opacity": 0.95,
    },
  });
  map.addLayer({
    id: "capsule-new", type: "circle", source: "towers", filter: NEVER,
    paint: {
      "circle-radius": ["interpolate", ["linear"], ["zoom"], 8, 9, 15, 14],
      "circle-color": "rgba(226,86,15,0.16)", "circle-stroke-width": 2.2, "circle-stroke-color": NEW_COLOR,
    },
  });
  // time capsule: a ghost ring where a tower came down in the chosen year; see setCapsuleLost
  map.addSource("capsule-lost", { type: "geojson", data: EMPTY });
  map.addLayer({
    id: "capsule-lost", type: "circle", source: "capsule-lost",
    paint: {
      "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 7, 15, 12],
      "circle-color": "rgba(94,78,71,0.1)", "circle-stroke-width": 2, "circle-stroke-color": GHOST_COLOR, "circle-stroke-opacity": 0.9,
    },
  });
  map.addLayer({
    id: "selected", type: "circle", source: "towers", filter: ["==", ["get", "id"], -1],
    paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 8, 11, 15, 16], "circle-color": "rgba(0,0,0,0)", "circle-stroke-width": 2.5, "circle-stroke-color": "#2B1D17" },
  });
  map.addLayer({
    id: "labels", type: "symbol", source: "towers", filter: ["!", ["has", "point_count"]], minzoom: 14.2,
    layout: {
      // a tower that has since come down (time capsule) says until when it stood
      "text-field": ["case", [">", ["get", "g"], 0], ["concat", ["get", "n"], "\n(until ", ["to-string", ["get", "g"]], ")"], ["get", "n"]],
      "text-font": ["Noto Sans Regular"], "text-size": 11.5,
      "text-offset": [0, 1.15], "text-anchor": "top", "text-optional": true, "text-max-width": 9,
      "symbol-sort-key": ["-", 900, ["get", "h"]],
    },
    paint: { "text-color": "#2B1D17", "text-halo-color": "#FAF4F1", "text-halo-width": 1.4 },
  });
  map.addLayer({
    id: "capsule-lost-label", type: "symbol", source: "capsule-lost", minzoom: 11,
    layout: {
      "text-field": ["concat", ["get", "n"], "\n", ["get", "how"], " ", ["to-string", ["get", "g"]]], "text-font": ["Noto Sans Regular"], "text-size": 11.5,
      "text-offset": [0, 1.2], "text-anchor": "top", "text-optional": true, "text-max-width": 10,
    },
    paint: { "text-color": GHOST_COLOR, "text-halo-color": "#FAF4F1", "text-halo-width": 1.4 },
  });

  const src = map.getSource("towers") as GeoJSONSource;

  map.on("click", "clusters", async (e: MapMouseEvent) => {
    const f = map.queryRenderedFeatures(e.point, { layers: ["clusters"] })[0];
    if (!f) return;
    const clusterId = f.properties!.cluster_id as number;
    const zoom = await src.getClusterExpansionZoom(clusterId);
    if (zoom > CLUSTER_MAX_ZOOM) {
      // Cannot be split further: towers share one point. Offer a list.
      const leaves = await src.getClusterLeaves(clusterId, 100, 0);
      const ids = leaves.map(l => (l.properties as { id: number }).id);
      cb.onChoose(ids, { x: e.point.x, y: e.point.y });
      return;
    }
    const [lng, lat] = (f.geometry as Point).coordinates;
    map.easeTo({ center: [lng, lat], zoom: Math.min(zoom + 0.4, 17), duration: 500 });
  });

  map.on("click", "pins", (e: MapMouseEvent) => {
    const feats = map.queryRenderedFeatures(e.point, { layers: ["pins"] });
    const ids = [...new Set(feats.map(f => f.properties!.id as number))];
    if (ids.length > 1) cb.onChoose(ids, { x: e.point.x, y: e.point.y });
    else if (ids.length === 1) cb.onSelect(ids[0]);
  });

  map.on("click", "capsule-lost", (e: MapMouseEvent) => {
    const f = map.queryRenderedFeatures(e.point, { layers: ["capsule-lost"] })[0];
    if (f) cb.onSelect(f.properties!.id as number);
  });

  for (const l of ["clusters", "pins", "capsule-lost"]) {
    map.on("mouseenter", l, () => { map.getCanvas().style.cursor = "pointer"; });
    map.on("mouseleave", l, () => { map.getCanvas().style.cursor = ""; });
  }
  if (cb.onMoveEnd) map.on("moveend", cb.onMoveEnd);
}

/**
 * Switch between the vector map and satellite imagery. In satellite mode the imagery sits below
 * everything, the basemap's fills and lines are hidden, and its place/road labels stay on top of
 * the imagery for orientation. Tower layers, clusters and clicks are untouched.
 */
export function setBasemap(map: MLMap, mode: Basemap) {
  const style = map.getStyle();
  if (!style) return;
  const base = style.layers.filter(l => !OWN_LAYERS.has(l.id) && l.id !== SAT_ID);
  if (mode === "satellite") {
    if (!map.getSource(SAT_ID)) {
      map.addSource(SAT_ID, { type: "raster", tiles: [SAT_TILES], tileSize: 256, maxzoom: 19, attribution: SAT_ATTR });
    }
    if (!map.getLayer(SAT_ID)) {
      map.addLayer({ id: SAT_ID, type: "raster", source: SAT_ID, paint: { "raster-fade-duration": 150 } }, base[0]?.id ?? style.layers.find(l => OWN_LAYERS.has(l.id))?.id);
    }
    for (const l of base) {
      const keep = l.type === "symbol" && !/housenumber|poi|aeroway|transit/i.test(l.id);
      // remember the style's own visibility the first time, so switching back restores it exactly
      if (!origVis.has(l.id)) origVis.set(l.id, (l.layout as { visibility?: "visible" | "none" } | undefined)?.visibility ?? "visible");
      map.setLayoutProperty(l.id, "visibility", keep ? origVis.get(l.id)! : "none");
    }
  } else {
    if (map.getLayer(SAT_ID)) map.removeLayer(SAT_ID);
    if (map.getSource(SAT_ID)) map.removeSource(SAT_ID);
    for (const l of base) {
      const v = origVis.get(l.id);
      if (v) map.setLayoutProperty(l.id, "visibility", v);
    }
  }
}
const origVis = new Map<string, "visible" | "none">();

/** Time capsule: ring the towers completed in `year` (and the clusters that hold one); null clears the rings. */
export function setCapsuleYear(map: MLMap, year: number | null) {
  if (!map.getLayer("capsule-new")) return;
  map.setFilter("capsule-new", year === null ? NEVER : ["all", ["!", ["has", "point_count"]], ["==", ["get", "y"], year]]);
  map.setFilter("capsule-new-clusters", year === null ? NEVER : ["all", ["has", "point_count"], ["==", ["get", "maxy"], year]]);
}

/** Time capsule: ghost rings for the towers that came down in the chosen year (`rows`, with `how` per id); none clears them. */
export function setCapsuleLost(map: MLMap, rows: TowerRow[], gone: Map<number, number>, how: (id: number) => string) {
  const src = map.getSource("capsule-lost") as GeoJSONSource | undefined;
  if (!src) return;
  const data = rowsToGeoJSON(rows, gone);
  for (const f of data.features) f.properties!.how = how(f.properties!.id as number);
  src.setData(data);
}

export function setSelected(map: MLMap, id: number | null) {
  if (!map.getLayer("selected")) return;
  map.setFilter("selected", ["==", ["get", "id"], id ?? -1]);
}

/** Show (or clear, with null) the outline of the opened city or district. */
export function setBoundary(map: MLMap, data: FeatureCollection | null) {
  const src = map.getSource(BOUNDARY_ID) as GeoJSONSource | undefined;
  if (src) src.setData(data ?? EMPTY);
}

/** Layers added by other modules (the skyline extent) that the basemap re-tint and the satellite switch must leave alone. */
export function registerOwnLayer(id: string) {
  OWN_LAYERS.add(id);
}

export function setTowerData(map: MLMap, data: FeatureCollection) {
  const src = map.getSource("towers") as GeoJSONSource | undefined;
  if (src) src.setData(data);
}

export function idxFromRows(idx: TowerIndex): Map<number, TowerRow> {
  const m = new Map<number, TowerRow>();
  for (const r of idx.rows) m.set(r[0], r);
  return m;
}
