import "server-only";
import index from "@/data/towers.json";
import details from "@/data/details.json";
import places from "@/data/places.json";
import { decodeDetail, type TowerIndex, type DetailsFile, type Tower, type Places, type TowerRow } from "./types";
import { computeRanks } from "./ranks";

const IDX = index as unknown as TowerIndex;
const DET = details as unknown as DetailsFile;
const PLACES = places as unknown as Places;
const RANKS = computeRanks(IDX);

export function getIndex(): TowerIndex { return IDX; }
export function getPlaces(): Places { return PLACES; }

export function resolve(row: TowerRow): Tower {
  const [id, name, lat, lon, height, city, district, status, year, floors, fn, precision, sharesPoint, hasPhoto] = row;
  return {
    id, name, lat, lon, height,
    city: IDX.cities[city],
    district: IDX.districts[district][1],
    status: IDX.statuses[status],
    year, floors,
    fn: IDX.functions[fn],
    precision: IDX.precisions[precision],
    sharesPoint,
    hasPhoto: !!hasPhoto,
    detail: decodeDetail(id, name, DET.rows[String(id)], { global: RANKS.global.get(id)!, city: RANKS.city.get(id)!, district: RANKS.district.get(id)! })!,
  };
}

let bySlug: Map<string, Tower> | null = null;
export function allTowers(): Tower[] { return IDX.rows.map(resolve); }
export function towerBySlug(slug: string): Tower | undefined {
  if (!bySlug) {
    bySlug = new Map();
    for (const r of IDX.rows) { const t = resolve(r); bySlug.set(t.detail.slug, t); }
  }
  return bySlug.get(slug);
}
export function towersInCity(city: string): Tower[] {
  const ci = IDX.cities.indexOf(city);
  return IDX.rows.filter(r => r[5] === ci).map(resolve);
}
export function towersInDistrict(city: string, district: string): Tower[] {
  const ci = IDX.cities.indexOf(city);
  const di = IDX.districts.findIndex(d => d[0] === ci && d[1] === district);
  return IDX.rows.filter(r => r[6] === di).map(resolve);
}
