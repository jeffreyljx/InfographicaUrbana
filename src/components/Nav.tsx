import BrandMenu from "./BrandMenu";
import { modeOf } from "@/lib/modes";

export type NavKey = "map" | "countries" | "cities" | "districts" | "skylines" | "metro" | "industry" | "industry-trade" | "industry-output" | "history" | "history-state" | "method";
/** ScraperMap's own pages, in the bar only while ScraperMap is the mode. */
const LINKS: [NavKey, string, string][] = [
  ["map", "/", "Map"],
  ["countries", "/countries/", "Countries"],
  ["cities", "/cities/", "Cities"],
  ["districts", "/districts/", "Districts"],
  ["skylines", "/skylines/", "Skylines"],
  ["method", "/method/", "Method"],
];
/** IndustryMap's pages: the map, and the figures behind it on two pages (Jeffrey, 18 Oct 2026). */
const INDUSTRY_LINKS: [NavKey, string, string][] = [
  ["industry", "/industry/", "Map"],
  ["industry-trade", "/industry/trade/", "Exports and imports"],
  ["industry-output", "/industry/output/", "Industrial output"],
];

/** Top bar: the site's mark and name (InfographicaUrbana), then the current mode's name, whose menu switches between
 *  ScraperMap, TransitMap, IndustryMap and CartaHistoria (src/lib/modes.ts),
 *  then the mode's own pages: in ScraperMap the map, the three rankings (by country, city and urban district), the
 *  skylines side by side and the method page; in IndustryMap its map and its two pages of figures. TransitMap and
 *  CartaHistoria have none (a state's page links back to the map). */
export default function Nav({ solid = false, active }: { solid?: boolean; active?: NavKey }) {
  const mode = modeOf(active);
  const links = mode.key === "scraper" ? LINKS : mode.key === "industry" ? INDUSTRY_LINKS : [];
  return (
    <nav className={"nav" + (solid ? " solid" : "") + (links.length ? "" : " solo")}>
      <BrandMenu active={active} />
      {links.map(([k, href, label]) => (
        <a key={k} href={href} className={k === active ? "on" : undefined} aria-current={k === active ? "page" : undefined}>{label}</a>
      ))}
    </nav>
  );
}
