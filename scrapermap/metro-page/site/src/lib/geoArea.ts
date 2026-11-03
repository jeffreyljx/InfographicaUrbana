import type { Geometry } from "geojson";

/**
 * Area of a GeoJSON polygon or multipolygon on the WGS84 ellipsoid, in km². Latitudes are mapped to authalic
 * latitudes, which carry the ellipsoid's area onto a sphere of equal surface (the authalic sphere) without
 * distortion, and each polygon's area there is its spherical excess, summed edge by edge. Holes are subtracted.
 * For outlines like the skyline extents (edges of a few km at most) this agrees with Karney's geodesic polygon
 * area on the ellipsoid to well under 0.001 km².
 */
const A = 6378137, F = 1 / 298.257223563, E2 = F * (2 - F), E = Math.sqrt(E2);
const q = (s: number) => (1 - E2) * (s / (1 - E2 * s * s) - Math.log((1 - E * s) / (1 + E * s)) / (2 * E));
const QP = q(1);
const R2 = (A * A * QP) / 2;   // square of the authalic radius, m²
const RAD = Math.PI / 180;

/** tan(β/2) of the authalic latitude β at a geodetic latitude in degrees */
function tanHalfAuthalic(lat: number): number {
  const s = Math.max(-1, Math.min(1, q(Math.sin(lat * RAD)) / QP));
  return Math.tan(Math.asin(s) / 2);
}

/** Unsigned area of one ring, m² */
function ringArea(ring: number[][]): number {
  let excess = 0;
  for (let i = 0; i < ring.length; i++) {
    const [lon1, lat1] = ring[i], [lon2, lat2] = ring[(i + 1) % ring.length];
    let dl = (lon2 - lon1) * RAD;
    if (dl > Math.PI) dl -= 2 * Math.PI; else if (dl < -Math.PI) dl += 2 * Math.PI;
    const t1 = tanHalfAuthalic(lat1), t2 = tanHalfAuthalic(lat2);
    excess += 2 * Math.atan2(Math.tan(dl / 2) * (t1 + t2), 1 + t1 * t2);
  }
  return Math.abs(excess) * R2;
}

export function areaKm2(geometry: Geometry): number {
  const polys = geometry.type === "Polygon" ? [geometry.coordinates] : geometry.type === "MultiPolygon" ? geometry.coordinates : [];
  let m2 = 0;
  for (const [outer, ...holes] of polys) m2 += ringArea(outer) - holes.reduce((s, h) => s + ringArea(h), 0);
  return m2 / 1e6;
}
