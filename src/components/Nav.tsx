export type NavKey = "map" | "countries" | "cities" | "districts" | "skylines" | "method";
const LINKS: [NavKey, string, string][] = [
  ["map", "/", "Map"],
  ["countries", "/countries/", "Countries"],
  ["cities", "/cities/", "Cities"],
  ["districts", "/districts/", "Districts"],
  ["skylines", "/skylines/", "Skylines"],
  ["method", "/method/", "Method"],
];

/** Top bar: the map, the three rankings (by country, city and urban district), the skylines side by side, and the method page. */
export default function Nav({ solid = false, active }: { solid?: boolean; active?: NavKey }) {
  return (
    <nav className={"nav" + (solid ? " solid" : "")}>
      <a className="brand" href="/" aria-label="ScraperMap home"><span className="mark">▲</span><span className="brand-name">ScraperMap</span></a>
      {LINKS.map(([k, href, label]) => (
        <a key={k} href={href} className={k === active ? "on" : undefined} aria-current={k === active ? "page" : undefined}>{label}</a>
      ))}
    </nav>
  );
}
