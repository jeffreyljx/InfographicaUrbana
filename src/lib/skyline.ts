import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import type { FeatureCollection } from "geojson";
import { areaKm2 } from "./geoArea";

/** Skyline size: the area of each city's skyline extent (public/skyline-extent.geojson, the cores drawn on the map), km² by city name. */
export function skylineSizes(): Record<string, number> {
  const fc = JSON.parse(readFileSync(join(process.cwd(), "public/skyline-extent.geojson"), "utf8")) as FeatureCollection;
  return Object.fromEntries(fc.features.map(f => [String(f.properties?.city), areaKm2(f.geometry)]));
}
