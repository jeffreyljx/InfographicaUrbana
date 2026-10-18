import BrandMenu from "./BrandMenu";
import { modeOf } from "@/lib/modes";

export type NavKey = "map" | "countries" | "cities" | "districts" | "skylines" | "metro" | "industry" | "method";
/** ScraperMap's own pages, in the bar only while ScraperMap is the mode. */
const LINKS: [NavKey, string, string][] = [
  ["map", "/", "Map"],
  ["countries", "/countries/", "Countries"],
  ["cities", "/cities/", "Cities"],
  ["districts", "/districts/", "Districts"],
  ["skylines", "/skylines/", "Skylines"],
  ["method", "/method/", "Method"],
];

/** Top bar: the current mode's name, whose menu switches between ScraperMap, TransitMap and IndustryMap (src/lib/modes.ts),
 *  then, in ScraperMap only, the map, the three rankings (by country, city and urban district), the skylines side by side
 *  and the method page. */
export default function Nav({ solid = false, active }: { solid?: boolean; active?: NavKey }) {
  const mode = modeOf(active);
  return (
    <nav className={"nav" + (solid ? " solid" : "") + (mode.key !== "scraper" ? " solo" : "")}>
      <BrandMenu active={active} />
      {mode.key === "scraper" && LINKS.map(([k, href, label]) => (
        <a key={k} href={href} className={k === active ? "on" : undefined} aria-current={k === active ? "page" : undefined}>{label}</a>
      ))}
    </nav>
  );
}
