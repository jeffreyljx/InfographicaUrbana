"use client";
import type { Feature, FeatureCollection, LineString, Point } from "geojson";
import { Map as MLMap, AttributionControl, NavigationControl, ScaleControl, setWorkerUrl, type GeoJSONSource, type MapMouseEvent, type ExpressionSpecification } from "maplibre-gl";
import { STYLE_URL, warmBasemap, registerOwnLayer } from "./towerMap";
import { NEVER_YEAR, type MetroData } from "@/lib/metro";
import { addStructureLayers, setStructureYear, STRUCT_CLICK } from "./metroStructures";

/* The /metro map: the same warm basemap (and satellite switch) as the tower map, with every metro line drawn stretch by
 * stretch from the year it opened, station bubbles in their line's colour (an interchange is drawn larger, in ink),
 * and, zoomed out, one dot per system sized by its length in the chosen year. The year is applied with filters, so
 * moving it never rebuilds the data. Zoomed in, each station shows its structure and exits (metroStructures.ts). */

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

/** Track as features: one per run of track that opened in one year. Properties: l line, y year, x line's closing year, c colour. */
export function trackFeatures(d: MetroData): FeatureCollection<LineString> {
  const features: Feature<LineString>[] = [];
  for (const t of d.tracks) {
    const l = d.lines[t.line];
    for (const r of t.runs) {
      features.push({
        type: "Feature", geometry: { type: "LineString", coordinates: t.coords.slice(r.from, r.to + 1) },
        properties: { l: l.i, s: l.sys, y: r.year, x: l.closeYear, c: l.colour },
      });
    }
  }
  return { type: "FeatureCollection", features };
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

const lineWidth = (k: number): ExpressionSpecification =>
  ["interpolate", ["exponential", 1.4], ["zoom"], 2, 0.6 * k, 6, 1.1 * k, 10, 2.2 * k, 13, 3.6 * k, 16, 6 * k];

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
    paint: { "line-color": HALO, "line-width": ["+", lineWidth(1), 2.2], "line-opacity": ["interpolate", ["linear"], ["zoom"], 4, 0, 7, 0.85] },
  });
  map.addLayer({
    id: "metro-new", type: "line", source: "metro-track",
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": NEW_COLOR, "line-width": ["+", lineWidth(1), 9], "line-opacity": 0.45, "line-blur": 4 },
  });
  map.addLayer({
    id: "metro-lines", type: "line", source: "metro-track",
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": ["get", "c"], "line-width": lineWidth(1) },
  });
  map.addLayer({
    id: "metro-sel-line", type: "line", source: "metro-track", filter: ["==", ["get", "l"], -1],
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": ["get", "c"], "line-width": lineWidth(1.9) },
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
    const ln = map.queryRenderedFeatures(box, { layers: ["metro-sel-line", "metro-lines"] })[0];
    if (ln) { cb.onLine(ln.properties!.l as number); return; }
    const sy = map.queryRenderedFeatures(box, { layers: ["metro-systems"] })[0];
    if (sy && map.getZoom() < SYSTEM_ZOOM + 0.5) cb.onSystem(sy.properties!.s as number);
  });
  for (const l of ["metro-stations", "metro-lines", "metro-sel-line", "metro-systems"]) {
    map.on("mouseenter", l, () => { map.getCanvas().style.cursor = "pointer"; });
    map.on("mouseleave", l, () => { map.getCanvas().style.cursor = ""; });
  }
}

/** Show the network as it stood in `year`: track and stations open then, the stretches opened that year glowing.
 *  `line`: the selected line, drawn wider over the rest (which fade a little). */
export function setMetroYear(map: MLMap, year: number, line: number | null) {
  if (!map.getLayer("metro-lines")) return;
  const open: ExpressionSpecification = ["all", ["<=", ["get", "y"], year], [">", ["get", "x"], year]];
  map.setFilter("metro-lines", open);
  map.setFilter("metro-casing", open);
  map.setFilter("metro-new", ["all", ["==", ["get", "y"], year], [">", ["get", "x"], year]]);
  map.setFilter("metro-sel-line", line === null ? ["==", ["get", "l"], -1] : ["all", open, ["==", ["get", "l"], line]]);
  map.setPaintProperty("metro-lines", "line-opacity", line === null ? 1 : 0.4);
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
