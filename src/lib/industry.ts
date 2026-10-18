import DATA from "./industry.json";
import placesJson from "@/data/places.json";
export { money, moneyK, site } from "./industryFormat";

/** IndustryMap's data: goods trade and manufacturing by city, packed from the City trade and
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
const CITIES = new Map((placesJson as unknown as { cities: { name: string; slug: string; lat: number; lon: number }[] }).cities.map(c => [c.name, c]));
export function citySlug(place: string): string | null {
  return CITIES.get(ALIAS[place] ?? place)?.slug ?? null;
}

/** Where a place sits on the IndustryMap, [lon, lat]: its ScraperMap city where the site has one, else the city itself or,
 *  for a region, the main city it counts (Cork for Cork & Kerry, Ciudad Juárez for Chihuahua state, Shah Alam for Selangor).
 *  Japan's customs gateways sit at their port or airport. */
const LONLAT: Record<string, [number, number]> = {
  "Bac Ninh": [106.076, 21.186], "Selangor": [101.518, 3.073], "Hamburg": [9.994, 53.551], "Jinhua": [119.647, 29.079],
  "Hai Phong": [106.688, 20.845], "Asan": [127.002, 36.790], "Chihuahua state (Ciudad Juarez)": [-106.424, 31.690],
  "Corpus Christi": [-97.396, 27.801], "El Paso": [-106.487, 31.762], "Jamnagar": [70.058, 22.470],
  "Cork & Kerry": [-8.471, 51.898], "San Jose (Silicon Valley)": [-121.886, 37.338], "Region Stuttgart": [9.183, 48.776],
  "Munich (city + district)": [11.575, 48.137], "Dublin": [-6.260, 53.350], "Copenhagen suburbs": [12.450, 55.700],
  "Wolfsburg": [10.787, 52.423], "Ingolstadt": [11.426, 48.766],
  "Narita International Airport": [140.393, 35.772], "Tokyo Port": [139.790, 35.620], "Nagoya Port": [136.850, 35.050],
  "Yokohama Port": [139.660, 35.450], "Kobe Port": [135.200, 34.670], "Kansai International Airport": [135.244, 34.434],
  "Osaka Port": [135.430, 34.650], "Hakata Port": [130.400, 33.610], "Chiba Port": [140.080, 35.580],
  "Mikawa Port": [137.330, 34.730], "Kawasaki Port": [139.750, 35.500], "Shimizu Port": [138.500, 35.010],
  "Yokkaichi Port": [136.640, 34.960], "Chubu Centrair Airport": [136.805, 34.858], "Sakai-Senboku Port": [135.430, 34.550],
};
export function placeLonLat(place: string): [number, number] | null {
  if (LONLAT[place]) return LONLAT[place];
  const c = CITIES.get(ALIAS[place] ?? place);
  return c ? [c.lon, c.lat] : null;
}

/** Where a country's circle sits on the IndustryMap, [lon, lat]: a point well inside it, near where its listed places are. */
export const COUNTRY_LONLAT: Record<string, [number, number]> = {
  "China": [112.5, 31.0], "Singapore": [103.82, 1.35], "United Arab Emirates": [54.3, 23.9], "France": [2.4, 46.6],
  "Malaysia": [101.9, 4.0], "Vietnam": [106.3, 16.2], "United Kingdom": [-1.6, 52.8], "Germany": [10.4, 51.1],
  "South Korea": [127.9, 36.4], "United States": [-98.4, 39.5], "Mexico": [-102.5, 23.9], "Turkey": [35.0, 39.0],
  "India": [79.0, 22.5], "Japan": [138.5, 36.3], "Ireland": [-8.0, 53.2], "Spain": [-3.6, 40.2], "Italy": [12.6, 42.8],
  "Denmark": [9.3, 56.0],
};

/* ---- by country: every listed place added into the country it belongs to (Hong Kong into China), at Jeffrey's
 * 18 Oct 2026 ask. These are sums of the places on the page, not national totals. */

/** A place counted inside another listed place, left out of its country's sum so it isn't counted twice. */
export const INSIDE: Record<string, string> = { "Nagoya city": "Aichi prefecture (Nagoya, Toyota City)" };

export interface TradePart { place: string; kind: "trade" | "exports" | "gateway"; year: string; ex: number | null; im: number | null; total: number | null }
export interface CountryTrade {
  country: string; parts: TradePart[]; years: string[];
  exSplit: number; imSplit: number;   // places that publish both
  totalOnly: number;                  // places that publish only a total (Dubai, Chengdu)
  exOnly: number;                     // places that publish only exports (US metros, Istanbul, Chihuahua, Jamnagar)
  ex: number; im: number;             // every place's exports, every place's imports
  total: number | null;               // exports plus imports where published; null where only exports are
}
const yearsOf = (ys: string[]) => [...new Set(ys)].sort();
function countryTrade(): CountryTrade[] {
  const parts: (TradePart & { country: string })[] = [
    ...D.trade.map(r => ({ place: r.place, country: r.country, kind: "trade" as const, year: r.year, ex: r.exports_usd_bn, im: r.imports_usd_bn, total: r.total_usd_bn })),
    ...D.exports_only.map(r => ({ place: r.place, country: r.country, kind: "exports" as const, year: r.year, ex: r.exports_usd_bn, im: null, total: null })),
    ...D.japan_ports.map(r => ({ place: r.port, country: "Japan", kind: "gateway" as const, year: r.year, ex: r.exports_usd_bn, im: r.imports_usd_bn, total: r.total_usd_bn })),
  ];
  const by = new Map<string, (TradePart & { country: string })[]>();
  for (const p of parts) by.set(p.country, [...(by.get(p.country) ?? []), p]);
  return [...by].map(([country, ps]) => {
    const sum = (f: (p: TradePart) => number | null | false) => ps.reduce((a, p) => a + (f(p) || 0), 0);
    const split = (p: TradePart) => p.ex != null && p.im != null;
    const exSplit = sum(p => split(p) && p.ex), imSplit = sum(p => split(p) && p.im);
    const totalOnly = sum(p => !split(p) && p.total), exOnly = sum(p => p.im == null && p.total == null && p.ex);
    const hasTotal = ps.some(p => p.total != null);
    return {
      country, parts: ps.map(({ country: _c, ...p }) => p).sort((a, b) => (b.total ?? b.ex ?? 0) - (a.total ?? a.ex ?? 0)),
      years: yearsOf(ps.map(p => p.year)), exSplit, imSplit, totalOnly, exOnly,
      ex: exSplit + exOnly, im: imSplit, total: hasTotal ? exSplit + imSplit + totalOnly : null,
    };
  }).sort((a, b) => (b.total ?? b.ex) - (a.total ?? a.ex));
}
export const COUNTRY_TRADE = countryTrade();

export interface MfgPart { place: string; year: string; va: number; jobs: number | null; upper: boolean; inside?: string }
export interface CountryMfg {
  country: string; parts: MfgPart[]; years: string[];
  va: number;                         // value added, places inside another left out
  upper: number;                      // the part of it that is an upper bound (secondary industry, with construction)
  jobs: number | null; vaWithJobs: number; perJob: number | null;   // from the places that publish jobs
  jobPlaces: number;
}
function countryMfg(): CountryMfg[] {
  const by = new Map<string, MfgRow[]>();
  for (const r of D.manufacturing) by.set(r.country, [...(by.get(r.country) ?? []), r]);
  return [...by].map(([country, rs]) => {
    const counted = rs.filter(r => !INSIDE[r.place]);
    const withJobs = counted.filter(r => r.employment != null);
    const jobs = withJobs.reduce((a, r) => a + (r.employment ?? 0), 0), vaWithJobs = withJobs.reduce((a, r) => a + r.va_usd_bn, 0);
    return {
      country, years: yearsOf(rs.map(r => r.year)),
      parts: rs.map(r => ({ place: r.place, year: r.year, va: r.va_usd_bn, jobs: r.employment, upper: r.upper_bound, inside: INSIDE[r.place] }))
        .sort((a, b) => b.va - a.va),
      va: counted.reduce((a, r) => a + r.va_usd_bn, 0), upper: counted.filter(r => r.upper_bound).reduce((a, r) => a + r.va_usd_bn, 0),
      jobs: withJobs.length ? jobs : null, vaWithJobs, perJob: withJobs.length ? (vaWithJobs * 1e6) / jobs : null, jobPlaces: withJobs.length,
    };
  }).sort((a, b) => b.va - a.va);
}
export const COUNTRY_MFG = countryMfg();

/** "2023" or "re-export hub" or both: what sets a row apart from the 2025 figures around it. */
export const tag = (caveat: string, year: string, base = "2025") => [caveat, year !== base ? year : ""].filter(Boolean).join(", ");

/** A round step and top for a bar scale reaching `max`, about `n` gridlines. */
export function niceScale(max: number, n = 5): { top: number; step: number } {
  const raw = max / n, mag = 10 ** Math.floor(Math.log10(raw));
  const step = [1, 2, 2.5, 5, 10].map(m => m * mag).find(s => s >= raw) ?? 10 * mag;
  return { top: Math.ceil(max / step) * step, step };
}

/* ---- the IndustryMap map's data, built on the server and handed to the page as props ---- */

/** A place's or country's key in the IndustryMap URL (?place=hong-kong). */
export const mapKey = (name: string) => name.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
interface MapBase { key: string; name: string; country: string; lonlat: [number, number]; slug: string | null; year: string; unit: string; how: string; caveat: string; note: string; source: string[] }
export interface MapTrade extends MapBase { kind: "trade" | "exports" | "gateway"; ex: number | null; im: number | null; total: number | null }
export interface MapMfg extends MapBase { va: number; jobs: number | null; perJob: number | null; upper: boolean; inside?: string }
export interface MapCountryTrade extends CountryTrade { key: string; lonlat: [number, number] }
export interface MapCountryMfg extends CountryMfg { key: string; lonlat: [number, number] }
export interface IndustryMapData { trade: MapTrade[]; output: MapMfg[]; tradeCountries: MapCountryTrade[]; outputCountries: MapCountryMfg[] }

export function industryMapData(): IndustryMapData {
  const at = (place: string) => {
    const ll = placeLonLat(place);
    if (!ll) throw new Error(`IndustryMap: no position for ${place}`);   // a new place needs a LONLAT entry or a ScraperMap city
    return ll;
  };
  const base = (place: string, country: string, year: string, unit: string, how: string, caveat: string, note: string, source: string[]): MapBase =>
    ({ key: mapKey(place), name: place, country, lonlat: at(place), slug: citySlug(place), year, unit, how, caveat, note, source });
  const trade: MapTrade[] = [
    ...D.trade.map(r => ({ ...base(r.place, r.country, r.year, r.unit, r.basis, r.caveat, r.note, r.source), kind: "trade" as const, ex: r.exports_usd_bn, im: r.imports_usd_bn, total: r.total_usd_bn })),
    ...D.exports_only.map(r => ({ ...base(r.place, r.country, r.year, r.unit, r.basis, r.caveat, r.note, r.source), kind: "exports" as const, ex: r.exports_usd_bn, im: null, total: null })),
    ...D.japan_ports.map(r => ({
      ...base(r.port, "Japan", r.year, "Customs port or airport", "Japan counts trade where goods clear customs", "customs gateway", "", r.source),
      slug: null, kind: "gateway" as const, ex: r.exports_usd_bn, im: r.imports_usd_bn, total: r.total_usd_bn,
    })),
  ];
  const output: MapMfg[] = D.manufacturing.map(r => ({
    ...base(r.place, r.country, r.year, r.unit, r.measure, "", r.note, r.source),
    va: r.va_usd_bn, jobs: r.employment, perJob: r.va_per_worker_usd_k, upper: r.upper_bound, inside: INSIDE[r.place],
  }));
  const where = (c: string) => { const ll = COUNTRY_LONLAT[c]; if (!ll) throw new Error(`IndustryMap: no position for ${c}`); return ll; };
  return {
    trade, output,
    tradeCountries: COUNTRY_TRADE.map(c => ({ ...c, key: mapKey(c.country), lonlat: where(c.country) })),
    outputCountries: COUNTRY_MFG.map(c => ({ ...c, key: mapKey(c.country), lonlat: where(c.country) })),
  };
}
