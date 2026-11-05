import BrandMenu from "./BrandMenu";
import { modeOf } from "@/lib/modes";

export type NavKey = "map" | "countries" | "cities" | "districts" | "skylines" | "method" | "guide"
  | "metro" | "metro-guide" | "industry" | "industry-trade" | "industry-output" | "industry-guide" | "history" | "history-state" | "history-guide";
/** ScraperMap's own pages, in the bar only while ScraperMap is the mode. */
const LINKS: [NavKey, string, string][] = [
  ["map", "/", "Map"],
  ["countries", "/countries/", "Countries"],
  ["cities", "/cities/", "Cities"],
  ["districts", "/districts/", "Districts"],
  ["skylines", "/skylines/", "Skylines"],
  ["method", "/method/", "Method"],
  ["guide", "/guide/", "Guide"],
];
/** IndustryMap's pages: the map, and the figures behind it on two pages (Jeffrey, 18 Oct 2026). */
const INDUSTRY_LINKS: [NavKey, string, string][] = [
  ["industry", "/industry/", "Map"],
  ["industry-trade", "/industry/trade/", "Exports and imports"],
  ["industry-output", "/industry/output/", "Industrial output"],
  ["industry-guide", "/industry/guide/", "Guide"],
];
/** TransitMap and CartaHistoria: the map and its guide. */
const TRANSIT_LINKS: [NavKey, string, string][] = [["metro", "/metro/", "Map"], ["metro-guide", "/metro/guide/", "Guide"]];
const HISTORY_LINKS: [NavKey, string, string][] = [["history", "/history/", "Map"], ["history-guide", "/history/guide/", "Guide"]];
const MODE_LINKS = { scraper: LINKS, industry: INDUSTRY_LINKS, transit: TRANSIT_LINKS, history: HISTORY_LINKS };

/** Top bar: the site's mark and name (InfographicaUrbana), then the current mode's name, whose menu switches between
 *  ScraperMap, TransitMap, IndustryMap and CartaHistoria (src/lib/modes.ts),
 *  then the mode's own pages: in ScraperMap the map, the three rankings (by country, city and urban district), the
 *  skylines side by side and the method page; in IndustryMap its map and its two pages of figures. Every mode ends with
 *  its guide (Jeffrey, 4 Nov 2026); TransitMap and CartaHistoria have just the map and the guide (.nav.few, which keeps
 *  the mode's name in view on narrow screens). */
export default function Nav({ solid = false, active }: { solid?: boolean; active?: NavKey }) {
  const mode = modeOf(active);
  const links = MODE_LINKS[mode.key];
  return (
    <nav className={"nav" + (solid ? " solid" : "") + (links.length <= 2 ? " few" : "")}>
      <BrandMenu active={active} />
      {links.map(([k, href, label]) => (
        <a key={k} href={href} className={k === active ? "on" : undefined} aria-current={k === active ? "page" : undefined}>{label}</a>
      ))}
    </nav>
  );
}
