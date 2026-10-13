"use client";
import type { Feature, FeatureCollection, MultiPolygon, Polygon } from "geojson";
import polygonClipping, { type Geom } from "polygon-clipping";

/**
 * Outlines for the city or district opened on the map.
 *
 * `/boundaries.json` maps each city and district to the OpenStreetMap object that is its boundary
 * (relation or way id, e.g. "R5664195"), matched offline and checked against the towers it must contain.
 * The polygon itself is fetched on demand from Nominatim's lookup endpoint, one request per place a
 * viewer opens, and cached for the session. A city with merged suburbs lists several ids; their
 * polygons are dissolved into one outline. Places without a mapped boundary simply show none.
 */
interface BoundaryIds { c: Record<string, string[]>; d: Record<string, string> }

let idsPromise: Promise<BoundaryIds | null> | null = null;
function loadIds(): Promise<BoundaryIds | null> {
  idsPromise ??= fetch("/boundaries.json").then(r => (r.ok ? r.json() : null)).catch(() => null);
  return idsPromise;
}

const cache = new Map<string, Promise<FeatureCollection | null>>();
const LOOKUP = "https://nominatim.openstreetmap.org/lookup?format=geojson&polygon_geojson=1";

type Area = Polygon | MultiPolygon;
const isArea = (g: unknown): g is Area => !!g && ((g as Area).type === "Polygon" || (g as Area).type === "MultiPolygon");

async function fetchOutline(ids: string[]): Promise<FeatureCollection | null> {
  // One polygon is lightly simplified (~20 m); several are fetched exact, so the borders they share
  // coincide and dissolve cleanly into one outline.
  const r = await fetch(`${LOOKUP}&polygon_threshold=${ids.length > 1 ? 0 : 0.0002}&osm_ids=${ids.join(",")}`);
  if (!r.ok) throw new Error("lookup " + r.status);
  const fc = (await r.json()) as FeatureCollection;
  const geoms = fc.features.map(f => f.geometry).filter(isArea);
  if (!geoms.length) return null;
  let geometry: Area = geoms[0];
  if (geoms.length > 1) {
    try {
      const [first, ...rest] = geoms.map(g => g.coordinates as Geom);
      geometry = { type: "MultiPolygon", coordinates: polygonClipping.union(first, ...rest) };
    } catch {
      geometry = { type: "MultiPolygon", coordinates: geoms.flatMap(g => (g.type === "Polygon" ? [g.coordinates] : g.coordinates)) };
    }
  }
  const feature: Feature = { type: "Feature", geometry, properties: {} };
  return { type: "FeatureCollection", features: [feature] };
}

/** Outline for a city (district null) or a district of it; null when none is mapped or the lookup fails. */
export async function boundaryFor(city: string, district: string | null): Promise<FeatureCollection | null> {
  const ids = await loadIds();
  if (!ids) return null;
  const list = district ? (ids.d[`${city}|${district}`] ? [ids.d[`${city}|${district}`]] : []) : ids.c[city] ?? [];
  if (!list.length) return null;
  const key = list.join(",");
  let p = cache.get(key);
  if (!p) {
    p = fetchOutline(list).catch(() => { cache.delete(key); return null; });   // a failed lookup may be retried later
    cache.set(key, p);
  }
  return p;
}
