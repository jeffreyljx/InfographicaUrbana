"use client";
import type { Feature, FeatureCollection, Geometry, Point } from "geojson";
import { Popup, type Map as MLMap, type GeoJSONSource, type ExpressionSpecification, type MapMouseEvent } from "maplibre-gl";
import { registerOwnLayer } from "./towerMap";
import type { MetroData } from "@/lib/metro";

/* Station structures and exits on the /metro map, zoomed in: each line's station box in the line's colour, halls and
 * concourses, underground passages, and lettered exits. They come from OpenStreetMap (planet of 15 Oct 2026), packed
 * one file per system by scripts/metro/build_structures.py, and are fetched only for the systems in view.
 *
 * public/metro/structures/<system id>.json, coordinates in 1e-6 degrees:
 *   boxes: [station, line, approximate (0/1), ring]   areas: [station, line, ring, estimated?]
 *   paths: [station, line, line string, estimated?]    exits: [station, x, y, label, name]
 * A path marked estimated (1) joins an exit that no mapped passage reaches to its station, in a straight line; an
 * area marked estimated is a concourse guessed around the exits where OpenStreetMap maps no hall (drawn dashed, lighter).
 * Halls and passages take the colour of the nearest line's box, as Baidu Maps draws them; exits are blue rounded squares
 * with their label in white (plain where the exit has no label), haloed in white so they read against every line colour. */

/** structures show from this zoom (and are fetched just before it) */
export const STRUCT_ZOOM = 14;
const INK = "#2B1D17";

type Pt = [number, number];
export interface StructureFile {
  v: number;
  boxes: [number, number, number, Pt[]][];
  areas: ([number, number, Pt[]] | [number, number, Pt[], number])[];
  paths: ([number, number, Pt[]] | [number, number, Pt[], number])[];
  exits: [number, number, number, string, string][];
}

const files = new Map<number, Promise<StructureFile | null>>();
const ready = new Map<number, StructureFile>();

/** The structures of one system (cached; null if it has none or the file fails). */
export function loadStructures(d: MetroData, sys: number): Promise<StructureFile | null> {
  let p = files.get(sys);
  if (!p) {
    p = fetch(`/metro/structures/${d.systems[sys].id}.json`)
      .then(r => (r.ok ? r.json() : null))
      .then((f: StructureFile | null) => { if (f) ready.set(sys, f); return f; })
      .catch(() => null);
    files.set(sys, p);
  }
  return p;
}

const pt = (p: Pt): Pt => [p[0] / 1e6, p[1] / 1e6];

function features(d: MetroData): FeatureCollection {
  const out: Feature<Geometry>[] = [];
  for (const f of ready.values()) {
    for (const [i, l, a, ring] of f.boxes) {
      const st = d.stations[i], ln = d.lines[l];
      const y = st.lines.find(([x]) => x === l)?.[1] ?? st.firstYear;
      out.push({ type: "Feature", geometry: { type: "Polygon", coordinates: [ring.map(pt)] }, properties: { k: "box", i, l, a, c: ln.colour, y, x: ln.closeYear } });
    }
    for (const [i, l, ring, a] of f.areas) {
      const st = d.stations[i];
      out.push({ type: "Feature", geometry: { type: "Polygon", coordinates: [ring.map(pt)] }, properties: { k: "area", i, a: a ? 1 : 0, c: d.lines[l].colour, y: st.firstYear, x: st.closeYear } });
    }
    for (const [i, l, line, a] of f.paths) {
      const st = d.stations[i];
      out.push({ type: "Feature", geometry: { type: "LineString", coordinates: line.map(pt) }, properties: { k: "path", i, a: a ? 1 : 0, c: d.lines[l].colour, y: st.firstYear, x: st.closeYear } });
    }
    for (const [i, x, y, r, n] of f.exits) {
      const st = d.stations[i];
      out.push({
        type: "Feature", geometry: { type: "Point", coordinates: [x / 1e6, y / 1e6] },
        properties: { k: "exit", i, r, n, y: st.firstYear, x: st.closeYear },
      });
    }
  }
  return { type: "FeatureCollection", features: out };
}

const LAYERS = ["metro-st-area", "metro-st-area-line", "metro-st-area-approx", "metro-st-path", "metro-st-path-approx", "metro-st-box", "metro-st-box-line", "metro-st-box-approx", "metro-st-exit-dot", "metro-st-exit"];
/** exits are blue, smooth-cornered squares: plain where OpenStreetMap gives the exit no label, with the label in white */
const EXIT_BLUE = "#1F63D0";
/** a rounded square, drawn as a signed-distance image so its colour can be set per layer; its middle stretches, so a
 * square fitted around a two- or three-character label (A1, 东1北) keeps round corners instead of being squashed */
const BADGE_N = 48, BADGE_R = 11, BADGE_IN = 5;      // size and corner radius in image pixels (2 per screen pixel), inset for the halo
function badge(): { width: number; height: number; data: Uint8Array } {
  const n = BADGE_N, r = BADGE_R, h = n / 2 - BADGE_IN - r, data = new Uint8Array(n * n * 4);
  for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
    const dx = Math.max(Math.abs(x + 0.5 - n / 2) - h, 0), dy = Math.max(Math.abs(y + 0.5 - n / 2) - h, 0);
    const dist = Math.hypot(dx, dy) - r;            // < 0 inside
    const a = Math.max(0, Math.min(255, Math.round(192 - dist * 16)));
    data.set([0, 0, 0, a], (y * n + x) * 4);
  }
  return { width: n, height: n, data };
}
const BADGE_OPTS = (() => {
  // only the straight middle stretches; the label fits just inside the drawn edge
  const lo = BADGE_IN + BADGE_R, hi = BADGE_N - BADGE_IN - BADGE_R, c0 = BADGE_IN + 2, c1 = BADGE_N - BADGE_IN - 2;
  return { sdf: true, pixelRatio: 2, stretchX: [[lo, hi]] as [number, number][], stretchY: [[lo, hi]] as [number, number][], content: [c0, c0, c1, c1] as [number, number, number, number] };
})();
for (const id of LAYERS) registerOwnLayer(id);
/** layers a click on opens the station they belong to */
export const STRUCT_CLICK = ["metro-st-exit", "metro-st-exit-dot", "metro-st-box"];

const fadeIn = (to: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"], STRUCT_ZOOM, 0, STRUCT_ZOOM + 0.6, to];

/** Add the structure layers under the station bubbles (exits above them), and fetch structures as the view moves. */
export function addStructureLayers(map: MLMap, d: MetroData) {
  map.addSource("metro-structures", { type: "geojson", data: { type: "FeatureCollection", features: [] }, tolerance: 0.1 });
  const below = "metro-stations";
  map.addLayer({
    id: "metro-st-area", type: "fill", source: "metro-structures", minzoom: STRUCT_ZOOM, filter: ["==", ["get", "k"], "area"],
    // an estimated concourse (guessed around the exits) is lighter than a mapped hall
    paint: { "fill-color": ["get", "c"], "fill-opacity": ["interpolate", ["linear"], ["zoom"], STRUCT_ZOOM, 0, STRUCT_ZOOM + 0.6, ["case", ["==", ["get", "a"], 1], 0.14, 0.3]] },
  }, below);
  map.addLayer({
    id: "metro-st-area-line", type: "line", source: "metro-structures", minzoom: STRUCT_ZOOM, filter: ["all", ["==", ["get", "k"], "area"], ["!=", ["get", "a"], 1]],
    paint: { "line-color": ["get", "c"], "line-width": 0.8, "line-opacity": fadeIn(0.6) },
  }, below);
  map.addLayer({
    id: "metro-st-area-approx", type: "line", source: "metro-structures", minzoom: STRUCT_ZOOM, filter: ["all", ["==", ["get", "k"], "area"], ["==", ["get", "a"], 1]],
    paint: { "line-color": ["get", "c"], "line-width": ["interpolate", ["linear"], ["zoom"], 14, 0.7, 18, 1.4], "line-opacity": fadeIn(0.8), "line-dasharray": [2, 1.5] },
  }, below);
  map.addLayer({
    id: "metro-st-path", type: "line", source: "metro-structures", minzoom: STRUCT_ZOOM + 0.8, filter: ["all", ["==", ["get", "k"], "path"], ["==", ["get", "a"], 0]],
    layout: { "line-cap": "round", "line-join": "round" },
    // about 6 m wide on the ground at every zoom
    paint: { "line-color": ["get", "c"], "line-width": ["interpolate", ["exponential", 2], ["zoom"], 14.8, 2, 19, 36], "line-opacity": 0.45 },
  }, below);
  // an estimated passage (an exit joined to its station in a straight line): thinner and dashed, like an approximate box
  map.addLayer({
    id: "metro-st-path-approx", type: "line", source: "metro-structures", minzoom: STRUCT_ZOOM + 0.8, filter: ["all", ["==", ["get", "k"], "path"], ["==", ["get", "a"], 1]],
    layout: { "line-join": "round" },
    paint: { "line-color": ["get", "c"], "line-width": ["interpolate", ["exponential", 2], ["zoom"], 14.8, 1, 19, 14], "line-opacity": 0.55, "line-dasharray": [1.2, 0.8] },
  }, below);
  map.addLayer({
    id: "metro-st-box", type: "fill", source: "metro-structures", minzoom: STRUCT_ZOOM, filter: ["==", ["get", "k"], "box"],
    paint: { "fill-color": ["get", "c"], "fill-opacity": ["interpolate", ["linear"], ["zoom"], STRUCT_ZOOM, 0, STRUCT_ZOOM + 0.6, ["case", ["==", ["get", "a"], 1], 0.36, 0.55]] },
  }, below);
  map.addLayer({
    id: "metro-st-box-line", type: "line", source: "metro-structures", minzoom: STRUCT_ZOOM, filter: ["all", ["==", ["get", "k"], "box"], ["==", ["get", "a"], 0]],
    paint: { "line-color": ["get", "c"], "line-width": ["interpolate", ["linear"], ["zoom"], 14, 0.8, 18, 2], "line-opacity": fadeIn(1) },
  }, below);
  map.addLayer({
    id: "metro-st-box-approx", type: "line", source: "metro-structures", minzoom: STRUCT_ZOOM, filter: ["all", ["==", ["get", "k"], "box"], ["==", ["get", "a"], 1]],
    paint: { "line-color": ["get", "c"], "line-width": ["interpolate", ["linear"], ["zoom"], 14, 0.8, 18, 1.6], "line-opacity": fadeIn(0.9), "line-dasharray": [2, 1.5] },
  }, below);
  if (!map.hasImage("m-exit")) map.addImage("m-exit", badge(), BADGE_OPTS);
  const exitPaint = {
    "icon-color": EXIT_BLUE, "icon-halo-color": "#FFFFFF", "icon-halo-width": 1.2, "text-color": "#FFFFFF",
    "icon-opacity": ["interpolate", ["linear"], ["zoom"], 14.6, 0, 15.1, 1] as ExpressionSpecification,
  };
  const exitSize: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], 14.6, 0.4, 16, 0.75, 18, 1.1];
  map.addLayer({
    id: "metro-st-exit-dot", type: "symbol", source: "metro-structures", minzoom: STRUCT_ZOOM + 0.6, filter: ["all", ["==", ["get", "k"], "exit"], ["==", ["get", "r"], ""]],
    layout: { "icon-image": "m-exit", "icon-size": exitSize, "icon-allow-overlap": true, "icon-ignore-placement": true },
    paint: exitPaint,
  });
  // a lettered exit is a dot until its letter fits, then a badge around the letter
  map.addLayer({
    id: "metro-st-exit", type: "symbol", source: "metro-structures", minzoom: STRUCT_ZOOM + 0.6, filter: ["all", ["==", ["get", "k"], "exit"], ["!=", ["get", "r"], ""]],
    layout: {
      "icon-image": "m-exit", "icon-size": exitSize, "icon-allow-overlap": true, "icon-ignore-placement": true,
      "text-field": ["step", ["zoom"], "", 15.4, ["get", "r"]], "text-font": ["Noto Sans Bold"],
      "text-size": ["interpolate", ["linear"], ["zoom"], 15.4, 9.5, 17, 12, 19, 14], "text-allow-overlap": true, "text-ignore-placement": true,
      "icon-text-fit": ["step", ["zoom"], "none", 15.4, "both"], "icon-text-fit-padding": [2, 3.5, 2, 3.5],
    },
    paint: exitPaint,
  });

  // fetch the structures of the systems in view once zoomed in close enough
  const refresh = () => {
    if (map.getZoom() < STRUCT_ZOOM - 0.5) return;
    const b = map.getBounds();
    const want = d.systems.filter(s => s.placed && s.bbox[0] - 0.02 <= b.getEast() && s.bbox[2] + 0.02 >= b.getWest() && s.bbox[1] - 0.02 <= b.getNorth() && s.bbox[3] + 0.02 >= b.getSouth());
    const missing = want.filter(s => !files.has(s.i));
    if (!missing.length) return;
    Promise.all(missing.map(s => loadStructures(d, s.i))).then(() => {
      (map.getSource("metro-structures") as GeoJSONSource | undefined)?.setData(features(d));
    });
  };
  map.on("moveend", refresh);
  refresh();

  // an exit's name on hover
  const pop = new Popup({ closeButton: false, closeOnClick: false, offset: 10, className: "m-exit-pop" });
  const hover = (e: MapMouseEvent & { features?: { properties: Record<string, unknown>; geometry: Geometry }[] }) => {
    const f = e.features?.[0];
    if (!f) return;
    const st = d.stations[f.properties.i as number];
    const r = String(f.properties.r || ""), n = String(f.properties.n || "");
    const head = r ? `Exit ${r}` : "Exit";
    const node = document.createElement("div");
    const b = document.createElement("b"); b.textContent = head; node.appendChild(b);
    node.appendChild(document.createTextNode(` · ${st.en || st.name}`));
    if (n && n !== r) { const s = document.createElement("div"); s.className = "muted"; s.textContent = n; node.appendChild(s); }
    pop.setLngLat((f.geometry as Point).coordinates as [number, number]).setDOMContent(node).addTo(map);
  };
  for (const l of ["metro-st-exit", "metro-st-exit-dot"]) {
    map.on("mousemove", l, hover);
    map.on("mouseleave", l, () => pop.remove());
  }
  for (const l of STRUCT_CLICK) {
    map.on("mouseenter", l, () => { map.getCanvas().style.cursor = "pointer"; });
    map.on("mouseleave", l, () => { map.getCanvas().style.cursor = ""; });
  }
}

/** Structures follow the year like the stations: drawn only while their line (or station) is open. */
export function setStructureYear(map: MLMap, year: number) {
  if (!map.getLayer("metro-st-box")) return;
  const open: ExpressionSpecification = ["all", ["<=", ["get", "y"], year], [">", ["get", "x"], year]];
  const kind = (k: string): ExpressionSpecification => ["==", ["get", "k"], k];
  map.setFilter("metro-st-area", ["all", kind("area"), open]);
  map.setFilter("metro-st-area-line", ["all", kind("area"), ["!=", ["get", "a"], 1], open]);
  map.setFilter("metro-st-area-approx", ["all", kind("area"), ["==", ["get", "a"], 1], open]);
  map.setFilter("metro-st-path", ["all", kind("path"), ["==", ["get", "a"], 0], open]);
  map.setFilter("metro-st-path-approx", ["all", kind("path"), ["==", ["get", "a"], 1], open]);
  map.setFilter("metro-st-box", ["all", kind("box"), open]);
  map.setFilter("metro-st-box-line", ["all", kind("box"), ["==", ["get", "a"], 0], open]);
  map.setFilter("metro-st-box-approx", ["all", kind("box"), ["==", ["get", "a"], 1], open]);
  map.setFilter("metro-st-exit", ["all", kind("exit"), ["!=", ["get", "r"], ""], open]);
  map.setFilter("metro-st-exit-dot", ["all", kind("exit"), ["==", ["get", "r"], ""], open]);
}

/** What the station panel says about a station's structure: its exits' labels and whether its boxes are mapped. */
export function stationStructure(f: StructureFile | null, i: number) {
  if (!f) return null;
  const exits = f.exits.filter(e => e[0] === i).map(e => e[3]);
  const boxes = f.boxes.filter(b => b[0] === i);
  const estPaths = f.paths.filter(p => p[0] === i && p[3] === 1).length;
  const estAreas = f.areas.filter(a => a[0] === i && a[3] === 1).length;
  return { exits, labelled: exits.filter(Boolean).sort((a, b) => a.localeCompare(b, "en", { numeric: true })), mapped: boxes.filter(b => b[2] === 0).length, approx: boxes.filter(b => b[2] === 1).length, estPaths, estAreas };
}
