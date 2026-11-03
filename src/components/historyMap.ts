"use client";
import type { FeatureCollection, Point } from "geojson";
import { Map as MLMap, AttributionControl, NavigationControl, ScaleControl, setWorkerUrl, type GeoJSONSource, type LayerSpecification } from "maplibre-gl";
import { STYLE_URL, warmBasemap, registerOwnLayer } from "./towerMap";
import type { HistoryLayer } from "./historyLayer";

/* The /history map: the site's basemap (OpenFreeMap Positron, warmed by warmBasemap) reduced to water and rivers, since
 * modern borders, roads and place names are anachronistic on a map of 800; the cell layer goes under the water so
 * coasts and lakes stay crisp, and capitals are dots above everything. Without the basemap (offline, provider down)
 * a plain sea-coloured ground stands in and the cells alone draw the land. */

const SEA = "#A9BEC4";
/** nobody's land (colours.json rules.neutral) also shows where the basemap has land the grid lacks (Antarctica) */
const NEUTRAL = "#D6D0C9";
const BLANK_STYLE = {
  version: 8 as const,
  sources: {},
  layers: [{ id: "bg", type: "background" as const, paint: { "background-color": SEA } }],
};
const SAT_ID = "history-sat";
const SAT_TILES = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}";
const SAT_ATTR = 'Imagery © <a href="https://www.esri.com/" target="_blank" rel="noopener">Esri</a>, Maxar, Earthstar Geographics';
export const CAPITALS = "history-capitals";
for (const id of ["history-cells", CAPITALS, SAT_ID]) registerOwnLayer(id);

/** basemap layers kept: the sea, lakes and rivers */
const keep = (l: LayerSpecification) => l.type === "background" || ((l.type === "fill" || l.type === "line") && /water/.test(l.id) && !/name|label/.test(l.id));

let workerSet = false;
export function createHistoryMap(container: HTMLDivElement, center: [number, number], zoom: number): MLMap {
  if (!workerSet) { setWorkerUrl("/maplibre/maplibre-gl-worker.mjs"); workerSet = true; }
  const map = new MLMap({
    container, style: STYLE_URL, center, zoom, minZoom: 0.3, maxZoom: 10, attributionControl: false, hash: false,
    dragRotate: false, pitchWithRotate: false, touchPitch: false, renderWorldCopies: true,
  });
  map.touchZoomRotate.disableRotation();
  let styleFailed = false;
  map.on("style.load", () => {
    if (styleFailed) return;
    warmBasemap(map);
    plainBasemap(map);
  });
  map.on("error", (e) => {
    if (styleFailed || map.isStyleLoaded()) return;
    const err = (e as unknown as { error?: Error & { url?: string } }).error;
    if (!err?.url || !err.url.startsWith(STYLE_URL)) return;
    styleFailed = true;
    map.setStyle(BLANK_STYLE as unknown as string);
  });
  map.addControl(new AttributionControl({
    compact: true,
    customAttribution: 'Borders from <a href="https://seshat-db.com/" target="_blank" rel="noopener">Cliopatria</a> (Seshat, CC BY 4.0) and Wikipedia',
  }), "bottom-right");
  map.addControl(new ScaleControl({ maxWidth: 120, unit: "metric" }), "bottom-right");
  map.addControl(new NavigationControl({ showCompass: false }), "bottom-left");
  (window as unknown as { __map?: MLMap }).__map = map;
  return map;
}

/** Hide everything but the sea, lakes and rivers; the background becomes nobody's land. */
function plainBasemap(map: MLMap) {
  const style = map.getStyle();
  if (!style) return;
  for (const l of style.layers) {
    if (l.id.startsWith("history-")) continue;
    if (!keep(l)) map.setLayoutProperty(l.id, "visibility", "none");
    else if (l.type === "background") map.setPaintProperty(l.id, "background-color", NEUTRAL);
  }
}

/** The first basemap layer that must draw over the cells (the water), or undefined to go on top. */
function beforeWater(map: MLMap): string | undefined {
  const style = map.getStyle();
  return style?.layers.find(l => l.type === "fill" && /water/.test(l.id))?.id;
}

const EMPTY: FeatureCollection = { type: "FeatureCollection", features: [] };

export function addHistoryLayers(map: MLMap, layer: HistoryLayer) {
  if (!map.getLayer(layer.id)) map.addLayer(layer, beforeWater(map));
  if (!map.getSource(CAPITALS)) map.addSource(CAPITALS, { type: "geojson", data: EMPTY });
  if (!map.getLayer(CAPITALS)) {
    map.addLayer({
      id: CAPITALS, type: "circle", source: CAPITALS,
      filter: [">=", ["get", "c"], ["case", ["<", ["zoom"], 2.5], 300, ["<", ["zoom"], 4], 40, 0]],
      paint: {
        "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 2.2, 4, 3.4, 8, 5],
        "circle-color": "#FFF8F3",
        "circle-stroke-color": "#2B1D17",
        "circle-stroke-width": ["interpolate", ["linear"], ["zoom"], 1, 1.2, 6, 1.8],
      },
    });
  }
}

/** Capitals of the states alive in the year: [lon, lat, cells, owner]. */
export function setCapitals(map: MLMap, caps: [number, number, number, number, string][]) {
  const src = map.getSource(CAPITALS) as GeoJSONSource | undefined;
  if (!src) return;
  src.setData({
    type: "FeatureCollection",
    features: caps.map(([lon, lat, c, o, name]) => ({ type: "Feature", geometry: { type: "Point", coordinates: [lon, lat] } as Point, properties: { c, o, name } })),
  });
}

/** Map or satellite: imagery under the cells, which turn translucent; the basemap's water is hidden over it. */
export function setHistoryBasemap(map: MLMap, layer: HistoryLayer, mode: "map" | "satellite") {
  const style = map.getStyle();
  if (!style) return;
  if (mode === "satellite") {
    if (!map.getSource(SAT_ID)) map.addSource(SAT_ID, { type: "raster", tiles: [SAT_TILES], tileSize: 256, maxzoom: 19, attribution: SAT_ATTR });
    if (!map.getLayer(SAT_ID)) map.addLayer({ id: SAT_ID, type: "raster", source: SAT_ID, paint: { "raster-fade-duration": 150 } }, layer.id);
    for (const l of style.layers) if (!l.id.startsWith("history-") && keep(l)) map.setLayoutProperty(l.id, "visibility", "none");
    layer.alpha = 0.62;
  } else {
    if (map.getLayer(SAT_ID)) map.removeLayer(SAT_ID);
    if (map.getSource(SAT_ID)) map.removeSource(SAT_ID);
    for (const l of style.layers) if (!l.id.startsWith("history-") && keep(l)) map.setLayoutProperty(l.id, "visibility", "visible");
    layer.alpha = 1;
  }
  map.triggerRepaint();
}
