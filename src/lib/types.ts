export type TowerRow = [
  id: number, name: string, lat: number, lon: number, height: number,
  city: number, district: number, status: number, year: number | null, floors: number,
  fn: number, precision: number, sharesPoint: number, hasPhoto: number
];

export interface TowerIndex {
  /** Build-time facts that are not per-tower (e.g. towers left off the map). Optional for old data. */
  meta?: { unplaced: number; unplaced_top: [string, number][]; added_2026_09?: number };
  schema: string[];
  cities: string[];
  districts: [cityIdx: number, name: string][];
  statuses: string[];
  functions: string[];
  precisions: string[];
  rows: TowerRow[];
}

export interface Photo {
  thumb: string;      // Commons thumbnail URL (~800px)
  page: string;       // Commons file page URL
  author: string | null;
  license: string | null;
  license_url: string | null;
  complex: boolean;   // photo shows the tower's complex (matched on the development's name), not the tower alone
}

export interface TowerDetail {
  slug: string;
  country: string;
  sub_area: string | null;
  material: string | null;
  address: string | null;
  ctbuh_url: string;
  rank_city: number;
  rank_district: number;
  rank_global: number;
  height_confirmed: boolean;
  precision: string;
  coord_source: string | null;
  coord_note: string | null;
  osm_way: number | null;
  photo: Photo | null;
}

export type DetailRow = [
  country: string, sub_area: string | null, material: string | null, address: string | null, ctbuh_slug: string | null,
  height_confirmed: 0 | 1, coord_note: string | null, osm_way: number | null,
  photo: [thumb: string, page: string, author: string | null, license: string | null, license_url: string | null, scope?: "complex"] | null
];
export interface DetailsFile { schema: string[]; rows: Record<string, DetailRow> }

/** Same rule as scripts/build_data.py: NFKD, drop non-ASCII, lowercase, runs of non-alphanumerics → "-". */
export function slugify(s: string): string {
  const a = s.normalize("NFKD").replace(/[^\x00-\x7F]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");
  return a || "x";
}
export function towerSlug(name: string, id: number): string { return `${slugify(name)}-${id}`; }

export function decodeDetail(id: number, name: string, r: DetailRow | undefined, ranks: { global: number; city: number; district: number }): TowerDetail | undefined {
  if (!r) return undefined;
  return {
    slug: towerSlug(name, id), country: r[0], sub_area: r[1], material: r[2], address: r[3],
    ctbuh_url: `https://www.skyscrapercenter.com/building/${r[4] ?? slugify(name)}/${id}`,
    rank_city: ranks.city, rank_district: ranks.district, rank_global: ranks.global, height_confirmed: r[5] === 1,
    precision: "", coord_source: null, coord_note: r[6], osm_way: r[7],
    photo: r[8] ? { thumb: r[8][0], page: r[8][1], author: r[8][2], license: r[8][3], license_url: r[8][4], complex: r[8][5] === "complex" } : null,
  };
}

/** A fully resolved tower, convenient for rendering. */
export interface Tower {
  id: number;
  name: string;
  lat: number;
  lon: number;
  height: number;
  city: string;
  district: string;
  status: string;
  year: number | null;
  floors: number;
  fn: string;
  precision: string;
  sharesPoint: number;
  hasPhoto: boolean;
  detail: TowerDetail;
}

export interface PlaceAgg {
  name: string;
  slug: string;
  country: string;
  count: number;
  completed: number;
  supertall: number;      // all statuses, ≥300 m (kept for compatibility; equals count300)
  count200: number;       // all statuses, ≥200 m
  completed200: number;   // completed only, ≥200 m
  count300: number;
  completed300: number;
  skyline: number;        // aggregate skyline height: completed towers ≥150 m, heights added up (m)
  skyline200: number;     // the same for completed towers ≥200 m
  skyline300: number;
  tallest_id: number;
  tallest_name: string;
  tallest_h: number;
  lat: number;
  lon: number;
  bbox: [number, number, number, number];
  rank: number;
}
export interface CityAgg extends PlaceAgg {
  districts: number;      // districts with any tower ≥150 m (all statuses)
  districts200: number;
  districts300: number;
  rank200: number;        // rank by completed towers ≥200 m; 0 when the city has none
  rank300: number;
}
export type Threshold = 150 | 200 | 300;
export const THRESHOLDS: Threshold[] = [150, 200, 300];
/** Completed / all-status counts of a place at a height threshold. */
export function countsAt(p: PlaceAgg, min: Threshold): { completed: number; count: number } {
  return min === 300 ? { completed: p.completed300, count: p.count300 }
    : min === 200 ? { completed: p.completed200, count: p.count200 }
    : { completed: p.completed, count: p.count };
}
/** Aggregate skyline height of a place at a height threshold: the completed towers' heights added up (m). */
export function skylineAt(p: PlaceAgg, min: Threshold): number {
  return min === 300 ? p.skyline300 : min === 200 ? p.skyline200 : p.skyline;
}
/** A city's rank and district count at a height threshold. */
export function cityAt(c: CityAgg, min: Threshold): { rank: number; districts: number } {
  return min === 300 ? { rank: c.rank300, districts: c.districts300 }
    : min === 200 ? { rank: c.rank200, districts: c.districts200 }
    : { rank: c.rank, districts: c.districts };
}
export interface DistrictAgg extends PlaceAgg { city: string; city_slug: string }
export interface Places {
  cities: CityAgg[];
  districts: DistrictAgg[];
  totals: { towers: number; completed: number; cities: number; districts: number; countries: number; supertall: number; with_photo: number };
}
