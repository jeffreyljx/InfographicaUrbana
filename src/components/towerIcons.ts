"use client";
import type { Map as MLMap, MapLayerMouseEvent, ExpressionSpecification } from "maplibre-gl";
import { registerOwnLayer } from "./towerMap";

/**
 * Tower icons: a small elevation drawing of each of the tallest towers, standing on its pin once the map is
 * zoomed in far enough that the pin is no longer part of a cluster. The drawings are SVGs in /tower-icons/,
 * made by scripts/tower-icons/gen.py at one shared scale (so heights compare truthfully) and listed in
 * /tower-icons/index.json. Each is rasterised once at the screen's pixel density and drawn by a symbol layer
 * on the clustered "towers" source, so an icon only shows where its tower is a single pin and it follows the
 * filters like the pin does. The layer sits on top of the tower layers: MapLibre's collision detection then
 * hides an icon that would overlap a taller tower's icon and keeps tower names from being drawn over one.
 */
const LAYER = "tower-icons";
const DIR = "/tower-icons/";
const IMAGE_PREFIX = "tower-icon-";
const MIN_ZOOM = 12;
const SIZE: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], MIN_ZOOM, 0.7, 15, 1, 18, 1.35];
/** Bitmaps are drawn this much larger than icon-size 1, so they stay sharp at the largest size. */
const OVERSAMPLE = 1.4;
/** How far above the pin's centre the tower's ground line stands, in px at icon-size 1. */
const STAND = 5;

interface IconEntry { id: number; name: string; height: number; w: number; h: number; base: number }
interface IconIndex { pxPerMetre: number; icons: IconEntry[] }

/** Load the icons and add their layer above the tower layers. Call once, after addTowerLayers. */
export async function addTowerIcons(map: MLMap, onSelect: (id: number) => void) {
  let index: IconIndex;
  try {
    const r = await fetch(DIR + "index.json");
    if (!r.ok) return;
    index = await r.json();
  } catch { return; }
  const scale = (window.devicePixelRatio || 1) * OVERSAMPLE;
  const loaded = await Promise.all(index.icons.map(async icon => {
    try {
      const img = await rasterise(`${DIR}${icon.id}.svg`, icon.w, icon.h, scale);
      if (!map.hasImage(IMAGE_PREFIX + icon.id)) map.addImage(IMAGE_PREFIX + icon.id, img, { pixelRatio: scale });
      return icon;
    } catch { return null; }   // a missing or broken drawing just leaves that tower without an icon
  }));
  const icons = loaded.filter((x): x is IconEntry => x !== null);
  if (!icons.length || !map.getSource("towers") || map.getLayer(LAYER)) return;
  // Every drawing has the same padding under its ground line, so one offset stands them all on their pins.
  const base = icons[0].base;

  map.addLayer({
    id: LAYER, type: "symbol", source: "towers", minzoom: MIN_ZOOM,
    filter: ["all", ["!", ["has", "point_count"]], ["in", ["get", "id"], ["literal", icons.map(i => i.id)]]],
    layout: {
      "icon-image": ["concat", IMAGE_PREFIX, ["to-string", ["get", "id"]]],
      "icon-anchor": "bottom",
      "icon-offset": [0, base - STAND],
      "icon-size": SIZE,
      "icon-padding": 1,
      "symbol-sort-key": ["-", 900, ["get", "h"]],   // taller towers are placed first
    },
  });
  registerOwnLayer(LAYER);

  map.on("click", LAYER, (e: MapLayerMouseEvent) => {
    const id = e.features?.[0]?.properties?.id;
    if (typeof id === "number") onSelect(id);
  });
  map.on("mouseenter", LAYER, () => { map.getCanvas().style.cursor = "pointer"; });
  map.on("mouseleave", LAYER, () => { map.getCanvas().style.cursor = ""; });
}

async function rasterise(url: string, w: number, h: number, scale: number): Promise<ImageData> {
  const img = new Image();
  img.src = url;
  await img.decode();
  const canvas = document.createElement("canvas");
  canvas.width = Math.ceil(w * scale);
  canvas.height = Math.ceil(h * scale);
  const ctx = canvas.getContext("2d")!;
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  return ctx.getImageData(0, 0, canvas.width, canvas.height);
}
