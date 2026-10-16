import DATA from "./industry.json";
import placesJson from "@/data/places.json";
export { money, moneyK, site } from "./industryFormat";

/** The Industry and Exports page's data: goods trade and manufacturing by city, packed from the City trade and
 *  manufacturing research (16 Oct 2026) by scripts/industry/build_industry.py. US$ at Federal Reserve G.5A annual
 *  averages; every row carries its source URLs. */

export interface TradeRow { place: string; country: string; unit: string; basis: string; year: string; exports_usd_bn: number | null; imports_usd_bn: number | null; total_usd_bn: number | null; caveat: string; note: string; source: string[] }
export interface ExportRow { place: string; country: string; unit: string; basis: string; year: string; exports_usd_bn: number; caveat: string; note: string; source: string[] }
export interface PortTradeRow { port: string; year: string; exports_usd_bn: number; imports_usd_bn: number; total_usd_bn: number; source: string[] }
export interface ContainerRow { port: string; country: string; year: string; teu_million: number; note: string; source: string[] }
export interface MfgRow { place: string; country: string; unit: string; measure: string; year: string; va_usd_bn: number; employment: number | null; va_per_worker_usd_k: number | null; upper_bound: boolean; note: string; source: string[] }
export interface FxRow { currency: string; code: string; year: string; per_usd: number }

const D = DATA as unknown as {
  trade: TradeRow[]; exports_only: ExportRow[]; japan_ports: PortTradeRow[]; container_ports: ContainerRow[];
  manufacturing: MfgRow[]; exchange_rates: FxRow[];
};
const byDesc = <T,>(v: (r: T) => number | null) => (a: T, b: T) => (v(b) ?? -1) - (v(a) ?? -1);

export const TRADE = [...D.trade].sort(byDesc(r => r.total_usd_bn));
export const EXPORTS_ONLY = [...D.exports_only].sort(byDesc(r => r.exports_usd_bn));
/** Exports from both tables in one list, largest first. */
export const ALL_EXPORTS: ExportRow[] = [
  ...D.trade.filter(r => r.exports_usd_bn != null).map(r => ({ ...r, exports_usd_bn: r.exports_usd_bn as number })),
  ...D.exports_only,
].sort(byDesc(r => r.exports_usd_bn));
export const JAPAN_PORTS = [...D.japan_ports].sort(byDesc(r => r.total_usd_bn));
export const CONTAINER_PORTS = [...D.container_ports].sort(byDesc(r => r.teu_million));
export const MFG = [...D.manufacturing].sort(byDesc(r => r.va_usd_bn));
export const FX = D.exchange_rates;

export type Region = "ea" | "na" | "eu";
export const REGION_NAME: Record<Region, string> = { ea: "Asia", na: "North America", eu: "Europe and Turkey" };
export const region = (country: string): Region =>
  ["China", "Japan", "Singapore", "South Korea", "Taiwan, China"].includes(country) ? "ea" : country === "United States" ? "na" : "eu";

/** The ScraperMap city page for a place, where the site has one: the same city under a wider or narrower unit counts. */
const ALIAS: Record<string, string> = {
  "Aichi prefecture (Nagoya, Toyota City)": "Nagoya", "Nagoya city": "Nagoya", "Osaka prefecture": "Osaka", "Tokyo 23 wards": "Tokyo",
  "Barcelona province": "Barcelona", "Milan province": "Milan", "Ile-de-France (Paris region)": "Paris",
  "Dallas-Fort Worth": "Dallas", "San Francisco-Oakland": "San Francisco", "New York": "New York City",
  "Guangzhou (Nansha only)": "Guangzhou", "Ningbo-Zhoushan": "Ningbo", "Johor": "Johor Bahru", "Xi'an": "Xi’an",
};
const SLUGS = new Map((placesJson as unknown as { cities: { name: string; slug: string }[] }).cities.map(c => [c.name, c.slug]));
export function citySlug(place: string): string | null {
  return SLUGS.get(ALIAS[place] ?? place) ?? null;
}

/** "2023" or "re-export hub" or both: what sets a row apart from the 2025 figures around it. */
export const tag = (caveat: string, year: string, base = "2025") => [caveat, year !== base ? year : ""].filter(Boolean).join(", ");

/** A round step and top for a bar scale reaching `max`, about `n` gridlines. */
export function niceScale(max: number, n = 5): { top: number; step: number } {
  const raw = max / n, mag = 10 ** Math.floor(Math.log10(raw));
  const step = [1, 2, 2.5, 5, 10].map(m => m * mag).find(s => s >= raw) ?? 10 * mag;
  return { top: Math.ceil(max / step) * step, step };
}
