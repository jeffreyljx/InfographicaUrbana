import "server-only";
import GDP from "@/data-gdp/gdp.json";
import { mergedMembers, rawCountry } from "@/lib/countryLabels";

/** Full GDP record as stored in src/data-gdp/gdp.json (built offline; see the method page and HANDOVER). */
interface GdpRecord {
  usd: number | null;        // nominal, US$ at the year's average exchange rate
  ppp: number | null;        // international $ at the year's PPP conversion factor
  year: number;
  lcu?: number; cur?: string; // the figure as published, in local currency
  period?: string; measure?: string; area?: string; src?: string; note?: string;
  scope?: "area";            // the figure is for a larger area that contains the city (none is published for the city itself)
  scope_note?: string;        // which area, and the city's share of its population
}
interface GdpFile { meta: Record<string, unknown>; cities: Record<string, GdpRecord | null>; countries: Record<string, GdpRecord | null> }
const DATA = GDP as unknown as GdpFile;

/** What the tables need on the client: the two values, the year, and a one-line source note for the tooltip. */
export interface Gdp { usd: number | null; ppp: number | null; year: number; tip: string; area?: boolean }

function compact(r: GdpRecord | null | undefined): Gdp | null {
  if (!r || (r.usd == null && r.ppp == null)) return null;
  const tip = [r.scope_note, r.period && r.period !== "calendar" ? r.period : String(r.year), r.scope ? null : r.area, r.measure, r.src, r.note].filter(Boolean).join(" · ");
  return r.scope === "area" ? { usd: r.usd, ppp: r.ppp, year: r.year, tip, area: true } : { usd: r.usd, ppp: r.ppp, year: r.year, tip };
}

export function gdpOfCity(name: string): Gdp | null { return compact(DATA.cities[name]); }
// Countries are shown under their display label ("Taiwan, China", scripts/country-labels.json) and the GDP file is keyed by the dataset's
// own names. A country counted under another row (Taiwan under China, as Hong Kong and Macau are) adds its GDP to that row's.
export function gdpOfCountry(name: string): Gdp | null {
  const base = DATA.countries[rawCountry(name)];
  const extra = mergedMembers(name).map(m => ({ m, r: DATA.countries[m] }));
  if (!base || !extra.length) return compact(base);
  if (extra.some(({ r }) => !r || r.usd == null || r.ppp == null || r.year !== base.year) || base.usd == null || base.ppp == null) return compact(base);
  return compact({
    ...base,
    usd: base.usd + extra.reduce((s, { r }) => s + (r!.usd as number), 0),
    ppp: base.ppp + extra.reduce((s, { r }) => s + (r!.ppp as number), 0),
    note: [base.note, ...extra.map(({ m }) => m)].filter(Boolean).join(" + "),
  });
}
export function gdpMeta(): Record<string, unknown> { return DATA.meta; }
export function gdpCityCount(): number { return Object.values(DATA.cities).filter(r => r?.usd != null && r.scope !== "area").length; }
export function gdpAreaCount(): number { return Object.values(DATA.cities).filter(r => r?.usd != null && r.scope === "area").length; }
