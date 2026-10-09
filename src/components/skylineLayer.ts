"use client";
import type { FeatureCollection } from "geojson";
import { Popup, type Map as MLMap, type MapLayerMouseEvent, type LayerSpecification } from "maplibre-gl";
import { registerOwnLayer, type Basemap } from "./towerMap";

/**
 * "Display skyline extent": the urban core of each city with more than 50 towers, drawn as a gold
 * area with a solid outline. `/skyline-extent.geojson` holds one (multi)polygon per city, the areas it
 * covers, a short rationale and its tower counts; it is fetched the first time the extents are shown.
 *
 * The fill sits above the basemap's land and water fills and below its buildings, roads and labels.
 * A copy of the basemap's water fill is drawn over it, so rivers and harbours inside a core keep their
 * colour (hidden in satellite mode, where the basemap's own fills are hidden too). The outline sits above
 * the roads and under the place labels. Clicking inside a core (but not on a pin) opens a short note.
 */
const SRC = "skyline";
const FILL = "skyline-fill";
const LINE = "skyline-line";
const FILL_COLOR = "#E9A825";
const LINE_COLOR = { map: "#8A5A00", satellite: "#FFD166" } as const;
const DATA_URL = "/skyline-extent.geojson";

interface SkylineProps {
  city: string;
  rationale: string;
  towers_in_core: number;
  completed_in_core: number;
  towers_in_city: number;
  area_km2: number;
}

let dataPromise: Promise<FeatureCollection | null> | null = null;
function load(): Promise<FeatureCollection | null> {
  dataPromise ??= fetch(DATA_URL).then(r => (r.ok ? r.json() : null)).catch(() => null);
  return dataPromise;
}

/** The last state asked for; applied once the data has arrived if the layers are not there yet. */
let want: { on: boolean; basemap: Basemap } = { on: false, basemap: "map" };
let waterIds: string[] = [];
let popup: Popup | null = null;

/** Show or hide the skyline extents. The first call that shows them fetches the data and adds the layers. */
export function setSkyline(map: MLMap, on: boolean, basemap: Basemap) {
  want = { on, basemap };
  if (map.getSource(SRC)) { apply(map); return; }
  if (!on) return;
  load().then(fc => {
    if (!fc) return;
    try {
      if (!map.getSource(SRC)) addLayers(map, fc);
      apply(map);
    } catch { /* the map was removed while the file loaded */ }
  });
}

function apply(map: MLMap) {
  const vis = want.on ? "visible" : "none";
  map.setLayoutProperty(FILL, "visibility", vis);
  map.setLayoutProperty(LINE, "visibility", vis);
  for (const id of waterIds) map.setLayoutProperty(id, "visibility", want.on && want.basemap === "map" ? "visible" : "none");
  map.setPaintProperty(LINE, "line-color", LINE_COLOR[want.basemap]);
  if (!want.on) popup?.remove();
}

function addLayers(map: MLMap, fc: FeatureCollection) {
  const layers = map.getStyle().layers;
  // Basemap layers are the ones below the site's own (the first of which is the boundary outline).
  const firstOwn = layers.findIndex(l => l.id === "boundary-line");
  const base = (firstOwn < 0 ? layers : layers.slice(0, firstOwn)).filter(l => l.id !== "esri-imagery");
  const ownAnchor = firstOwn < 0 ? undefined : "boundary-line";
  // fill: under the first label, building, road or rail layer
  const fillBefore = base.find(l => l.type === "symbol" || l.type === "fill-extrusion"
    || (l.type === "line" && !/water/.test(l.id)) || /building/.test(l.id))?.id ?? ownAnchor;
  // outline: under the run of label layers at the top of the basemap
  let lastShape = -1;
  base.forEach((l, i) => { if (l.type !== "symbol") lastShape = i; });
  const lineBefore = base[lastShape + 1]?.id ?? ownAnchor;

  map.addSource(SRC, { type: "geojson", data: fc });
  map.addLayer({
    id: FILL, type: "fill", source: SRC, layout: { visibility: "none" },
    paint: { "fill-color": FILL_COLOR, "fill-opacity": ["interpolate", ["linear"], ["zoom"], 6, 0.5, 10, 0.34, 15, 0.22] },
  }, fillBefore);
  registerOwnLayer(FILL);

  waterIds = [];
  for (const l of base) {
    if (l.type !== "fill" || !/water/.test(l.id)) continue;
    const id = `skyline-mask-${l.id}`;
    const { visibility: _v, ...layout } = (l.layout ?? {}) as Record<string, unknown>;
    map.addLayer({ ...l, id, layout: { ...layout, visibility: "none" } } as LayerSpecification, fillBefore);
    registerOwnLayer(id);
    waterIds.push(id);
  }

  map.addLayer({
    id: LINE, type: "line", source: SRC,
    layout: { visibility: "none", "line-join": "round" },
    paint: {
      "line-color": LINE_COLOR.map,
      "line-opacity": 0.9,
      "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1.6, 10, 1.8, 15, 2.6],
    },
  }, lineBefore);
  registerOwnLayer(LINE);

  map.on("click", FILL, (e: MapLayerMouseEvent) => {
    const towerLayers = ["clusters", "pins"].filter(id => map.getLayer(id));
    if (map.queryRenderedFeatures(e.point, { layers: towerLayers }).length) return;   // the pin's own click wins
    const p = e.features?.[0]?.properties as unknown as SkylineProps | undefined;
    if (!p) return;
    popup?.remove();
    popup = new Popup({ className: "sky-popup", maxWidth: "340px", focusAfterOpen: false })
      .setLngLat(e.lngLat).setHTML(popupHtml(p)).addTo(map);
  });
}

const esc = (s: string) => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]!);
function popupHtml(p: SkylineProps): string {
  const n = (x: number) => Number(x).toLocaleString("en-US");
  return `<h3><span class="place">${esc(p.city)}</span> skyline extent</h3>`
    + `<p class="sky-n">${n(p.towers_in_core)} of the city's ${n(p.towers_in_city)} towers of 150 m+ (${n(p.completed_in_core)} completed) · ${p.area_km2} km²</p>`
    + `<p>${esc(p.rationale)}</p>`;
}
