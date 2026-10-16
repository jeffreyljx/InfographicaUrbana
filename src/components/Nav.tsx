import BrandMenu from "./BrandMenu";

export type NavKey = "map" | "countries" | "cities" | "districts" | "skylines" | "industry" | "method";
const LINKS: [NavKey, string, string][] = [
  ["map", "/", "Map"],
  ["countries", "/countries/", "Countries"],
  ["cities", "/cities/", "Cities"],
  ["districts", "/districts/", "Districts"],
  ["skylines", "/skylines/", "Skylines"],
  ["method", "/method/", "Method"],
];

/** Top bar: the ScraperMap name, whose menu lists every page (Industry and Exports is reached only from there), then the map,
 *  the three rankings (by country, city and urban district), the skylines side by side, and the method page. */
export default function Nav({ solid = false, active }: { solid?: boolean; active?: NavKey }) {
  return (
    <nav className={"nav" + (solid ? " solid" : "")}>
      <BrandMenu active={active} />
      {LINKS.map(([k, href, label]) => (
        <a key={k} href={href} className={k === active ? "on" : undefined} aria-current={k === active ? "page" : undefined}>{label}</a>
      ))}
    </nav>
  );
}
