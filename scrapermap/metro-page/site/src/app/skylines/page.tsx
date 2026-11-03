import type { Metadata } from "next";
import Shell from "@/components/Shell";
import SkylineControls, { type SkylineSortKey } from "@/components/SkylineControls";
import { getCitySkylines, type CitySkylines } from "@/lib/skylines";
import "@/components/skylines.css";

const CITIES = getCitySkylines();
const SKYLINES = CITIES.reduce((n, c) => n + c.skylines.length, 0);
export const metadata: Metadata = {
  title: "Skylines",
  description: `The skylines of ${CITIES.length} cities, each drawn where it stands in its city and all at one scale, to compare their shapes and sizes, each tagged with its towers of 150 m+ and its tallest building.`,
};

const fmt = (n: number) => n.toLocaleString("en-US");
const km2 = (v: number) => v.toFixed(v < 10 ? 2 : 1);
const UNFINISHED: Record<string, string> = { "Under construction": "under construction", "Architecturally topped out": "topped out", "Structurally topped out": "topped out" };

/** Position of each city under every sort (CSS `order`), so the switch reorders the drawings without re-rendering them. */
function orders(list: CitySkylines[]): Record<SkylineSortKey, number>[] {
  const by = (cmp: (a: CitySkylines, b: CitySkylines) => number) => {
    const sorted = list.map((_, i) => i).sort((i, j) => cmp(list[i], list[j]) || i - j);
    const pos = new Array<number>(list.length);
    sorted.forEach((i, k) => { pos[i] = k; });
    return pos;
  };
  const area = list.map((_, i) => i);   // the list is largest first already
  const towers = by((a, b) => b.towers - a.towers);
  const tallest = by((a, b) => (b.tallest?.status === "Completed" ? b.tallest.height : -1) - (a.tallest?.status === "Completed" ? a.tallest.height : -1));
  const city = by((a, b) => a.city.localeCompare(b.city, "en"));
  return list.map((_, i) => ({ area: area[i], towers: towers[i], tallest: tallest[i], city: city[i] }));
}

export default function SkylinesPage() {
  const maxW = Math.max(...CITIES.map(c => c.wKm));
  const pos = orders(CITIES);
  return (
    <Shell active="skylines">
      <h1>Skylines</h1>
      <p className="lead">Every city&apos;s skylines, each drawn where it stands in the city, as on the map with the map taken away, and every city at the same scale: {fmt(SKYLINES)} skylines in {CITIES.length} cities, largest first. A skyline is a pocket of five or more towers of 150 m+ standing close together, or several pockets that almost touch, joined: the same outlines the map draws with Display skyline extent.</p>
      <div className="skygrid-wrap" id="skygrid" data-sort="area" style={{ "--maxw": maxW, "--zoom": 1 } as React.CSSProperties}>
        <div className="skybar">
          <SkylineControls />
          <div className="skyscale" aria-live="polite">
            <i /><span id="skyscale-label">10 km</span>
          </div>
        </div>
        <div className="skygrid">
          {CITIES.map((c, i) => {
            const t = c.tallest;
            const names = c.skylines.flatMap(s => s.names);
            const label = c.skylines.length > 1 ? `${c.skylines.length} skylines: ${names.join(" · ")}` : names.join(" · ");
            return (
              <figure key={c.city} className="skyfig" style={{ "--w": c.wKm, "--h": c.hKm, "--o-area": pos[i].area, "--o-towers": pos[i].towers, "--o-tallest": pos[i].tallest, "--o-city": pos[i].city } as React.CSSProperties}>
                <div className="sky-frame">
                  <a className="sky-shape" href={`/?city=${encodeURIComponent(c.city)}&skyline=1`} aria-label={`Open ${c.city} on the map with its skyline extents`}>
                    <svg viewBox={`0 0 ${Math.round(c.wKm * 100)} ${Math.round(c.hKm * 100)}`} role="img" aria-label={`${c.city}: ${c.skylines.length === 1 ? "one skyline" : `${c.skylines.length} skylines`}, ${km2(c.km2)} km²`}>
                      {c.others && <path className="t2" d={c.others} />}
                      {c.skylines.map((s, k) => (
                        <path key={k} className="o" d={s.d}><title>{`${s.names.join(" · ")}: ${fmt(s.towers)} towers, ${km2(s.km2)} km²`}</title></path>
                      ))}
                      {c.dots && <path className="t" d={c.dots} />}
                    </svg>
                  </a>
                </div>
                <figcaption className="skytag">
                  {c.citySlug ? <a className="place" href={`/city/${c.citySlug}/`}>{c.city}</a> : <span className="place">{c.city}</span>}
                  <span className="tag-name" title={names.join(" · ")}>{label}</span>
                  <span className="tag-n" title={`${fmt(c.completed)} of them completed`}>{fmt(c.towers)} towers · {km2(c.km2)}&nbsp;km²</span>
                  {t && <span className="tag-top">Tallest: <a href={`/tower/${t.slug}/`}>{t.name}</a>, {Math.round(t.height)}&nbsp;m{t.status !== "Completed" && ` (${UNFINISHED[t.status] ?? t.status.toLowerCase()})`}</span>}
                </figcaption>
              </figure>
            );
          })}
        </div>
      </div>
      <p className="muted" style={{ marginTop: 36 }}>The outlines are the skyline extents drawn on the map: every group of five or more towers of 150 m+ (completed, topped out or under construction) in which each tower stands within 800 m of others, outlined 300 m out from its towers, run down to the waterfront it faces and cut back from rivers and the sea. Pockets that almost touch are joined into one skyline, named after all of them: towers up to 1.9 km apart, across rivers up to 600 m wide. Each city is drawn north up, with its skylines in their real places relative to each other and at the same scale as every other city. Dark dots are towers inside the outlines; faint dots are the city&apos;s other towers of 150 m+ in the same frame. At Fit, the city that spreads widest fills the column; zoom in to see the smaller cities larger, still all at one scale. Towers counts every tower of 150 m+ inside a city&apos;s outlines, whatever its status, as the map&apos;s extent notes do; hover the count for how many are completed, and a shape for its skyline&apos;s name. Tallest is the tallest completed tower inside, or the tallest unfinished one where none is complete yet. Areas are measured on the WGS84 ellipsoid and match the Cities table&apos;s Skyline size. Click a city to open it on the map with the skyline extents shown.</p>
    </Shell>
  );
}
