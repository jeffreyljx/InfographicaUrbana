"use client";
import type { FeatureCollection } from "geojson";
import { Popup, type Map as MLMap, type MapLayerMouseEvent, type LayerSpecification } from "maplibre-gl";
import { registerOwnLayer, type Basemap } from "./towerMap";
import { areaKm2 } from "@/lib/geoArea";

/**
 * "Display metro footprint": the built-up land around every city on the map, drawn as a mauve area with a
 * thin outline. `/metro-footprint.json` (made by scripts/metro-footprint/, from ESA WorldCover 2021) holds one
 * multipolygon per metropolitan area: every contiguous patch of built-up land that holds a tower of 150 m+,
 * with the cities in it. Cities whose patches touch share one feature (Tokyo with Kawasaki and Yokohama,
 * the Pearl River Delta cities). It is fetched the first time the footprints are shown.
 *
 * The fill sits under the skyline extents (when those are shown) and under the basemap's buildings, roads
 * and labels, with a copy of the basemap's water fill over it so rivers keep their colour on the vector map.
 * Clicking inside a footprint (but not on a pin, and not inside a shown skyline extent, whose own note wins)
 * opens a short note.
 */
const SRC = "metro-fp";
const FILL = "metro-fp-fill";
const LINE = "metro-fp-line";
const FILL_COLOR = "#8E6BB3";
const LINE_COLOR = { map: "#5E3F86", satellite: "#E2CCFF" } as const;
const DATA_URL = "/metro-footprint.json";
const ATTRIBUTION = 'Built-up land © <a href="https://esa-worldcover.org/" target="_blank" rel="noopener">ESA WorldCover</a> 2021';

interface FootprintProps {
  name: string;
  /** JSON in a clicked feature's properties: [{ city, towers, towers_in_city }] by towers, most first */
  cities: string | { city: string; towers: number; towers_in_city: number }[];
  area_km2: number;
  pieces: number;
  clipped: boolean;
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

/** Show or hide the metro footprints. The first call that shows them fetches the data and adds the layers. */
export function setFootprint(map: MLMap, on: boolean, basemap: Basemap) {
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
  // Basemap layers are the ones below the site's own (the first of which is the boundary outline), leaving
  // out the skyline extent's layers, which also sit down there.
  const firstOwn = layers.findIndex(l => l.id === "boundary-line");
  const base = (firstOwn < 0 ? layers : layers.slice(0, firstOwn)).filter(l => l.id !== "esri-imagery" && !l.id.startsWith("skyline-"));
  const ownAnchor = firstOwn < 0 ? undefined : "boundary-line";
  // fill: under the skyline extent if it is there, else under the first label, building, road or rail layer
  const fillBefore = map.getLayer("skyline-fill") ? "skyline-fill" : base.find(l => l.type === "symbol" || l.type === "fill-extrusion"
    || (l.type === "line" && !/water/.test(l.id)) || /building/.test(l.id))?.id ?? ownAnchor;
  // outline: under the skyline outline, else under the run of label layers at the top of the basemap
  let lastShape = -1;
  base.forEach((l, i) => { if (l.type !== "symbol") lastShape = i; });
  const lineBefore = map.getLayer("skyline-line") ? "skyline-line" : base[lastShape + 1]?.id ?? ownAnchor;

  // measured from the full outline here, since a clicked feature's geometry is clipped to its map tile
  const areas = new Map(fc.features.map(f => [String(f.properties?.name), areaKm2(f.geometry)]));
  map.addSource(SRC, { type: "geojson", data: fc, attribution: ATTRIBUTION });
  map.addLayer({
    id: FILL, type: "fill", source: SRC, layout: { visibility: "none" },
    paint: { "fill-color": FILL_COLOR, "fill-opacity": ["interpolate", ["linear"], ["zoom"], 4, 0.36, 9, 0.28, 14, 0.16] },
  }, fillBefore);
  registerOwnLayer(FILL);

  waterIds = [];
  base.forEach((l, i) => {
    if (l.type !== "fill" || !/water/.test(l.id)) return;
    const id = `metro-fp-m${i}`;   // no "water" in the id: the skyline extent copies the basemap's water fills by that word
    const { visibility: _v, ...layout } = (l.layout ?? {}) as Record<string, unknown>;
    map.addLayer({ ...l, id, layout: { ...layout, visibility: "none" } } as LayerSpecification, fillBefore);
    registerOwnLayer(id);
    waterIds.push(id);
  });

  map.addLayer({
    id: LINE, type: "line", source: SRC,
    layout: { visibility: "none", "line-join": "round" },
    paint: {
      "line-color": LINE_COLOR.map,
      "line-opacity": 0.8,
      "line-width": ["interpolate", ["linear"], ["zoom"], 4, 0.8, 9, 1.2, 14, 1.8],
    },
  }, lineBefore);
  registerOwnLayer(LINE);

  map.on("click", FILL, (e: MapLayerMouseEvent) => {
    const above = ["clusters", "pins", "tower-icons", "capsule-lost", "skyline-fill"].filter(id => map.getLayer(id));
    if (map.queryRenderedFeatures(e.point, { layers: above }).length) return;   // the pin's or the skyline extent's own click wins
    const p = e.features?.[0]?.properties as unknown as FootprintProps | undefined;
    if (!p) return;
    popup?.remove();
    popup = new Popup({ className: "sky-popup fp-popup", maxWidth: "340px", focusAfterOpen: false })
      .setLngLat(e.lngLat).setHTML(popupHtml(p, areas.get(p.name) ?? p.area_km2)).addTo(map);
  });
}

const esc = (s: string) => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]!);
function popupHtml(p: FootprintProps, km2: number): string {
  const n = (x: number) => Number(x).toLocaleString("en-US");
  const cities = typeof p.cities === "string" ? JSON.parse(p.cities) as Exclude<FootprintProps["cities"], string> : p.cities;
  const towers = cities.reduce((s, c) => s + c.towers, 0);
  const inside = cities.filter(c => c.towers), outside = cities.filter(c => !c.towers);
  const list = inside.map(c => `${esc(c.city)} (${n(c.towers)})`).join(", ");
  // a city with none inside: its towers stand on ground that was not built-up in 2021 (a construction site, a tower
  // by the shore or in a park); the footprint is the nearest built-up land, or the city proper (Cairo)
  const outsideNote = outside.length ? `${outside.map(c => esc(c.city)).join(", ")}: ${outside.length === 1 && outside[0].towers_in_city === 1 ? "its tower stands" : "their towers stand"}`
    + ` on ground that was not built-up in 2021 (a construction site, or by the shore or in a park); the footprint shown is the city's established built-up land.` : "";
  return `<h3><span class="place">${esc(p.name)}</span> metro footprint</h3>`
    + `<p class="sky-n">${n(Math.round(km2))} km² of built-up land · ${n(towers)} ${towers === 1 ? "tower" : "towers"} of 150 m+ in it`
    + (p.pieces > 1 ? ` · ${n(p.pieces)} pieces` : "") + `</p>`
    + `<p>${inside.length ? `${cities.length > 1 ? "Cities in it, with their towers inside: " : "Towers inside: "}${list}. ` : ""}${outsideNote}</p>`
    + `<p class="sky-note">Built-up land in ESA WorldCover 2021 (10 m): buildings, roads and other paved ground, with gaps up to 700 m `
    + `and open ground under 0.5 km² taken in; larger parks, fields and water left out.`
    + (p.clipped ? " The outer edge is cut off at the limit of the area that was mapped." : "") + `</p>`;
}
