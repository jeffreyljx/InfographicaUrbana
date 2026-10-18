"use client";
import type { FeatureCollection, Point } from "geojson";
import { Map as MLMap, AttributionControl, NavigationControl, ScaleControl, Popup, setWorkerUrl, type GeoJSONSource, type MapMouseEvent, type ExpressionSpecification } from "maplibre-gl";
import { STYLE_URL, warmBasemap, registerOwnLayer } from "./towerMap";

/* The IndustryMap map (/industry/): one circle per place or country on the tower map's warm basemap, its area to scale
 * with the figure shown (goods trade or manufacturing value added, US$). The circles keep one scale at any zoom and
 * grow a little as you zoom in, so the legend redraws its reference circles for the zoom (radiusAt). */

const LAND = "#E6D6CF";
const BLANK_STYLE = {
  version: 8 as const,
  glyphs: "https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf",
  sources: {},
  layers: [{ id: "bg", type: "background" as const, paint: { "background-color": LAND } }],
};
const INK = "#2B1D17";
const HALO = "#FAF4F1";

/** A circle on the map: `s` its radius in pixels at zoom 2, `v` the figure it is drawn for. */
export interface IndPoint { key: string; lonlat: [number, number]; v: number; s: number; c: string; hollow: boolean; pale: boolean; name: string; value: string; tag: string }

/** How much the circles grow with zoom, relative to zoom 2: slower than the map, so a region's circles still fit when
 *  zoomed in. Pairs of [zoom, factor], read by both the map and the legend. */
const GROWTH: [number, number][] = [[1, 0.72], [2, 1], [4, 1.6], [6, 2.4], [9, 3.4], [12, 4]];
export function radiusAt(s: number, zoom: number): number {
  const g = GROWTH;
  if (zoom <= g[0][0]) return s * g[0][1];
  for (let i = 1; i < g.length; i++) {
    if (zoom <= g[i][0]) { const [z0, f0] = g[i - 1], [z1, f1] = g[i]; return s * (f0 + ((zoom - z0) / (z1 - z0)) * (f1 - f0)); }
  }
  return s * g[g.length - 1][1];
}
const radius: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], ...GROWTH.flatMap(([z, f]) => [z, ["max", 2, ["*", ["get", "s"], f]]])] as ExpressionSpecification;

const LAYERS = ["ind-fill", "ind-sel", "ind-labels"];
for (const id of LAYERS) registerOwnLayer(id);

let workerSet = false;
export function createIndustryMap(container: HTMLDivElement, center: [number, number], zoom: number): MLMap {
  if (!workerSet) { setWorkerUrl("/maplibre/maplibre-gl-worker.mjs"); workerSet = true; }
  const map = new MLMap({ container, style: STYLE_URL, center, zoom, minZoom: 0, maxZoom: 12, attributionControl: false, hash: false, renderWorldCopies: false });
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
    customAttribution: 'Figures from national statistics offices, customs agencies and port authorities: sources on the <a href="/industry/trade/">Exports and imports</a> and <a href="/industry/output/">Industrial output</a> pages',
  }), "bottom-right");
  map.addControl(new ScaleControl({ maxWidth: 120, unit: "metric" }), "bottom-right");
  map.addControl(new NavigationControl({ showCompass: false }), "bottom-left");
  // a phone has no room for the sources line open over the legend: start it folded to its ⓘ button
  if (window.innerWidth <= 720) map.once("load", () => {
    const a = container.querySelector(".maplibregl-ctrl-attrib");
    a?.classList.remove("maplibregl-compact-show");
    a?.removeAttribute("open");
  });
  (window as unknown as { __map?: MLMap }).__map = map;
  return map;
}

function features(points: IndPoint[]): FeatureCollection<Point> {
  return {
    type: "FeatureCollection",
    features: points.map(p => ({
      type: "Feature", geometry: { type: "Point", coordinates: p.lonlat },
      properties: { k: p.key, v: p.v, s: p.s, c: p.c, h: p.hollow ? 1 : 0, p: p.pale ? 1 : 0, lab: `${p.name}\n${p.value}` },
    })),
  };
}

export function addIndustryLayers(map: MLMap, points: IndPoint[], onPick: (key: string) => void) {
  map.addSource("ind", { type: "geojson", data: features(points) });
  map.addLayer({
    id: "ind-fill", type: "circle", source: "ind",
    layout: { "circle-sort-key": ["-", 0, ["get", "v"]] },   // the smaller circle on top, so every one can be clicked
    paint: {
      "circle-radius": radius,
      "circle-color": ["get", "c"],
      "circle-opacity": ["case", ["==", ["get", "h"], 1], 0.06, ["==", ["get", "p"], 1], 0.22, 0.5],
      "circle-stroke-color": ["get", "c"],
      "circle-stroke-width": ["case", ["==", ["get", "h"], 1], 2, 1.2],
      "circle-stroke-opacity": 0.95,
    },
  });
  map.addLayer({
    id: "ind-sel", type: "circle", source: "ind", filter: ["==", ["get", "k"], ""],
    paint: { "circle-radius": ["+", radius, 3] as ExpressionSpecification, "circle-color": "rgba(0,0,0,0)", "circle-stroke-width": 2.5, "circle-stroke-color": INK },
  });
  // names and figures inside the bigger circles; a smaller circle's label appears once zooming in makes room for it
  const shown = (min: number): ExpressionSpecification => ["case", [">=", ["get", "s"], min], 11.5, 0];
  map.addLayer({
    id: "ind-labels", type: "symbol", source: "ind",
    layout: {
      "text-field": ["get", "lab"], "text-font": ["Noto Sans Regular"], "text-line-height": 1.15, "text-max-width": 9,
      "text-size": ["step", ["zoom"], shown(15), 3, shown(10), 4.5, shown(6.5), 6, shown(3.5), 7.5, 11.5],
      "symbol-sort-key": ["-", 0, ["get", "v"]],   // the biggest circles are labelled first
    },
    paint: { "text-color": INK, "text-halo-color": HALO, "text-halo-width": 1.4 },
  });

  // hover: the place and its figure; click: the panel
  const tip = new Popup({ closeButton: false, closeOnClick: false, className: "ind-tip", offset: 10, maxWidth: "260px" });
  // of the circles under the pointer, the one it is nearest the middle of (for its size); the smaller of two centred alike
  const under = (e: MapMouseEvent) => {
    const z = map.getZoom();
    return map.queryRenderedFeatures(e.point, { layers: ["ind-fill"] }).map(f => {
      const c = map.project((f.geometry as Point).coordinates as [number, number]);
      const r = Math.max(2, radiusAt(f.properties!.s as number, z));
      return { f, r, d: Math.hypot(c.x - e.point.x, c.y - e.point.y) / r };
    }).sort((a, b) => a.d - b.d || a.r - b.r)[0]?.f;
  };
  map.on("mousemove", (e) => {
    const f = under(e);
    map.getCanvas().style.cursor = f ? "pointer" : "";
    if (!f) { tip.remove(); return; }
    const [name, value] = String(f.properties!.lab).split("\n");
    const el = document.createElement("div");
    const b = document.createElement("b"); b.textContent = name;
    el.append(b, document.createElement("br"), value);
    tip.setLngLat(e.lngLat).setDOMContent(el).addTo(map);
  });
  map.on("mouseout", () => tip.remove());
  map.on("click", (e) => {
    const f = under(e);
    if (f) { tip.remove(); onPick(f.properties!.k as string); }
  });
}

export function setIndustryPoints(map: MLMap, points: IndPoint[]) {
  (map.getSource("ind") as GeoJSONSource | undefined)?.setData(features(points));
}

export function setIndustrySelected(map: MLMap, key: string | null) {
  if (map.getLayer("ind-sel")) map.setFilter("ind-sel", ["==", ["get", "k"], key ?? ""]);
}
