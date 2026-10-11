"use client";
import type { FeatureCollection } from "geojson";
import { Popup, type Map as MLMap, type MapLayerMouseEvent, type LayerSpecification, type GeoJSONSource, type FilterSpecification } from "maplibre-gl";
import { registerOwnLayer, type Basemap } from "./towerMap";
import { areaKm2 } from "@/lib/geoArea";

/**
 * "Display skyline extent": the urban core of each city with more than 50 towers, drawn as a gold
 * area with a solid outline. `/skyline-extent.geojson` holds one (multi)polygon per city, the areas it
 * covers, a short rationale and its tower counts; it is fetched the first time the extents are shown.
 *
 * The fill sits above the basemap's land and water fills and below its buildings, roads and labels.
 * A copy of the basemap's water fill is drawn over it, so rivers and harbours inside a core keep their
 * colour (hidden in satellite mode, where the basemap's own fills are hidden too). The outline sits above
 * the roads and under the place labels. Clicking inside a core (but not on a pin) opens a short note.
 *
 * With the time capsule on, the same layers show `/skyline-extent-years.geojson` instead (made by
 * scripts/skyline-years/build.py, fetched the first time a year is set): each core trimmed to the area
 * around the towers completed by the selected year, one feature per city and keyframe, shown while
 * from <= year < to. From the year of a core's latest tower on it is the drawn core itself (that keyframe
 * comes without geometry and takes the core's).
 */
const SRC = "skyline";
const FILL = "skyline-fill";
const LINE = "skyline-line";
const FILL_COLOR = "#E9A825";
const LINE_COLOR = { map: "#8A5A00", satellite: "#FFD166" } as const;
const DATA_URL = "/skyline-extent.geojson";
const YEARS_URL = "/skyline-extent-years.geojson";

interface SkylineProps {
  city: string;
  rationale: string;
  towers_in_core: number;
  completed_in_core: number;
  towers_in_city: number;
  area_km2: number;
}

/** One keyframe of a city's extent in the time capsule (see scripts/skyline-years/build.py). */
interface YearProps {
  city: string;
  from: number;          // first year shown
  to: number;            // first year not shown (9999: up to today)
  n: number;             // towers in today's core completed by `from`
  total: number;         // completed towers in today's core (with a known year)
  tallest: string;       // tallest of those `n`, "Name (484 m, 2010)"
}

const fetchJson = (url: string) => fetch(url).then(r => (r.ok ? r.json() : null)).catch(() => null) as Promise<FeatureCollection | null>;
let dataPromise: Promise<FeatureCollection | null> | null = null;
function load(): Promise<FeatureCollection | null> {
  dataPromise ??= fetchJson(DATA_URL);
  return dataPromise;
}
let yearsPromise: Promise<FeatureCollection | null> | null = null;
let cores: FeatureCollection | null = null;
let years: FeatureCollection | null = null;

/** The last state asked for; applied once the data has arrived if the layers are not there yet. */
let want: { on: boolean; basemap: Basemap; year: number | null } = { on: false, basemap: "map", year: null };
let shown: "cores" | "years" = "cores";
let waterIds: string[] = [];
let popup: Popup | null = null;

/**
 * Show or hide the skyline extents. The first call that shows them fetches the data and adds the layers.
 * `year` is the time capsule's year: each city's extent as it was then (null: today's drawn cores).
 */
export function setSkyline(map: MLMap, on: boolean, basemap: Basemap, year: number | null = null) {
  if (year !== want.year) popup?.remove();
  want = { on, basemap, year };
  sync(map);
}

function sync(map: MLMap) {
  const needYears = want.on && want.year !== null && !years;
  if (map.getSource(SRC) && !needYears) { apply(map); return; }
  if (!want.on) return;
  // a city's last keyframe has no geometry of its own: it is the drawn core, taken from the cores file
  if (needYears) yearsPromise ??= Promise.all([fetchJson(YEARS_URL), load()]).then(([fc, base]) => {
    if (!fc || !base) return null;
    const core = new Map(base.features.map(f => [f.properties?.city, f.geometry]));
    fc.features = fc.features.filter(f => (f.geometry ??= core.get(f.properties?.city)!));
    return (years = fc);
  });
  Promise.all([load(), needYears ? yearsPromise : null]).then(([fc]) => {
    if (!fc) return;
    try {
      if (!map.getSource(SRC)) addLayers(map, fc);
      apply(map);
    } catch { /* the map was removed while the file loaded */ }
  });
}

function apply(map: MLMap) {
  const byYear = want.year !== null;
  // until the year file has arrived (or if it failed to), show nothing rather than today's cores for a past year
  const vis = want.on && (!byYear || years) ? "visible" : "none";
  map.setLayoutProperty(FILL, "visibility", vis);
  map.setLayoutProperty(LINE, "visibility", vis);
  for (const id of waterIds) map.setLayoutProperty(id, "visibility", vis === "visible" && want.basemap === "map" ? "visible" : "none");
  map.setPaintProperty(LINE, "line-color", LINE_COLOR[want.basemap]);
  if (!want.on) popup?.remove();
  if (vis === "none") return;
  const mode = byYear ? "years" : "cores";
  if (mode !== shown) {
    (map.getSource(SRC) as GeoJSONSource).setData((mode === "years" ? years : cores)!);
    shown = mode;
  }
  const filter: FilterSpecification | null = byYear
    ? ["all", ["<=", ["get", "from"], want.year!], [">", ["get", "to"], want.year!]] : null;
  map.setFilter(FILL, filter);
  map.setFilter(LINE, filter);
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

  // measured from the full outline here, since a clicked feature's geometry is clipped to its map tile
  const areas = new Map(fc.features.map(f => [String(f.properties?.city), areaKm2(f.geometry)]));
  cores = fc;
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
    const towerLayers = ["clusters", "pins", "tower-icons"].filter(id => map.getLayer(id));
    if (map.queryRenderedFeatures(e.point, { layers: towerLayers }).length) return;   // the pin's own click wins
    const props = e.features?.[0]?.properties;
    if (!props) return;
    let html: string;
    if (shown === "years" && want.year !== null) {
      const p = props as unknown as YearProps;
      const full = years?.features.find(f => f.properties?.city === p.city && f.properties?.from === p.from);
      html = yearPopupHtml(p, want.year, full ? areaKm2(full.geometry) : null, areas.get(p.city) ?? null);
    } else {
      const p = props as unknown as SkylineProps;
      html = popupHtml(p, areas.get(p.city) ?? p.area_km2);
    }
    popup?.remove();
    popup = new Popup({ className: "sky-popup", maxWidth: "340px", focusAfterOpen: false })
      .setLngLat(e.lngLat).setHTML(html).addTo(map);
  });
}

const esc = (s: string) => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]!);
function popupHtml(p: SkylineProps, km2: number): string {
  const n = (x: number) => Number(x).toLocaleString("en-US");
  return `<h3><span class="place">${esc(p.city)}</span> skyline extent</h3>`
    + `<p class="sky-n">${n(p.towers_in_core)} of the city's ${n(p.towers_in_city)} towers of 150 m+ (${n(p.completed_in_core)} completed) · ${km2.toFixed(2)} km²</p>`
    + `<p>${esc(p.rationale)}</p>`;
}

function yearPopupHtml(p: YearProps, year: number, km2: number | null, coreKm2: number | null): string {
  const n = (x: number) => Number(x).toLocaleString("en-US");
  const today = p.to === 9999;
  const size = km2 === null ? "" : today || coreKm2 === null ? ` · ${km2.toFixed(2)} km²`
    : ` · ${km2.toFixed(2)} of today's ${coreKm2.toFixed(2)} km²`;
  return `<h3><span class="place">${esc(p.city)}</span> skyline extent in ${year}</h3>`
    + `<p class="sky-n">${n(p.n)} of the ${n(p.total)} completed towers in today's core had been built${size}</p>`
    + `<p>Tallest then: ${esc(p.tallest)}.</p>`
    + (today ? "" : `<p class="sky-note">Today's core, trimmed to the area around the towers built by ${year}.</p>`);
}
