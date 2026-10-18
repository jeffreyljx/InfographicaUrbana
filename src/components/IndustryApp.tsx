"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { LngLatBounds, type Map as MLMap } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import "./industry.css";
import Nav from "./Nav";
import { setBasemap, type Basemap } from "./towerMap";
import { createIndustryMap, addIndustryLayers, setIndustryPoints, setIndustrySelected, radiusAt, type IndPoint } from "./industryMap";
import { money, moneyK, site } from "@/lib/industryFormat";
import type { IndustryMapData, MapTrade, MapMfg, MapCountryTrade, MapCountryMfg } from "@/lib/industry";

/** The IndustryMap map (Jeffrey, 18 Oct 2026): every place's goods trade or manufacturing output as a circle to scale,
 *  for cities or added up by country, with a panel of each one's figures and sources. The view lives in the URL:
 *  ?show=output, ?by=country, ?flow=ex|im, ?place=<key>. */

type Show = "trade" | "output";
type By = "city" | "country";
type Flow = "total" | "ex" | "im";

const COLOR = { total: "#7F2F16", ex: "#0B5E57", im: "#C07A2C", output: "#A80F2F" };
/** pixels of radius per √(US$bn) at zoom 2: $1tn of trade is 36 px across the radius, $100bn of value added 26 px */
const K = { trade: 1.15, output: 2.6 };
const FLOW_NAME = { total: "exports plus imports", ex: "exports", im: "imports" };
const WORLD: { center: [number, number]; zoom: number } = { center: [10, 30], zoom: 1.9 };
const PHONE: { center: [number, number]; zoom: number } = { center: [75, 30], zoom: 0.9 };
/** the old one-page infographic's sections, now on the two pages */
const OLD_HASH: Record<string, string> = {
  "#trade": "/industry/trade/#trade", "#exports": "/industry/trade/#exports", "#ports": "/industry/trade/#ports",
  "#manufacturing": "/industry/output/#manufacturing", "#per-worker": "/industry/output/#per-worker", "#method": "/industry/trade/#method",
};

const short = (name: string) => name.replace(/\s*\(.*\)$/, "").replace(" International Airport", " Airport");
const tradeValue = (r: { ex: number | null; im: number | null; total: number | null }, flow: Flow) =>
  flow === "ex" ? r.ex : flow === "im" ? r.im : r.total;
const yearSpan = (ys: string[]) => ys.length > 1 ? `${ys[0]} to ${ys[ys.length - 1]}` : ys[0];

function points(d: IndustryMapData, show: Show, by: By, flow: Flow): IndPoint[] {
  const out: IndPoint[] = [];
  const add = (key: string, lonlat: [number, number], name: string, v: number | null, c: string, hollow = false, pale = false, tag = "") => {
    if (v == null || v <= 0) return;
    out.push({ key, lonlat, v, s: K[show] * Math.sqrt(v), c, hollow, pale, name: short(name), value: money(v), tag });
  };
  if (show === "trade" && by === "city") {
    // with exports plus imports shown, a place that publishes only exports is drawn hollow at its exports
    for (const r of d.trade) {
      const v = tradeValue(r, flow) ?? (flow === "total" ? r.ex : null);
      add(r.key, r.lonlat, r.name, v, COLOR[flow], flow === "total" && r.total == null, r.kind === "gateway");
    }
  } else if (show === "trade") {
    for (const c of d.tradeCountries) add(c.key, c.lonlat, c.country, flow === "total" ? c.total ?? c.ex : flow === "ex" ? c.ex : c.im, COLOR[flow], flow === "total" && c.total == null);
  } else if (by === "city") {
    for (const r of d.output) add(r.key, r.lonlat, r.name, r.va, COLOR.output, r.upper);
  } else {
    for (const c of d.outputCountries) add(c.key, c.lonlat, c.country, c.va, COLOR.output);
  }
  return out;
}

const small = () => window.innerWidth <= 720;
/** Keep the picked place clear of the panel (right, or the bottom sheet on a phone) and of the controls. */
function padding() {
  if (small()) return { top: 150, right: 30, bottom: Math.round(window.innerHeight * 0.6), left: 30 };
  return { top: 150, right: 460, bottom: 60, left: 60 };
}

export default function IndustryApp({ data }: { data: IndustryMapData }) {
  const mapEl = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MLMap | null>(null);
  const [mapReady, setMapReady] = useState(false);
  const [show, setShow] = useState<Show>("trade");
  const [by, setBy] = useState<By>("city");
  const [flow, setFlow] = useState<Flow>("total");
  const [pick, setPick] = useState<string | null>(null);
  const [zoom, setZoom] = useState(WORLD.zoom);
  const [basemap, setBasemapState] = useState<Basemap>("map");
  /** move the map to the pick: "zoom" in to it (from a list or the URL), or just "pan" it clear of a phone's panel */
  const [fly, setFly] = useState<"zoom" | "pan" | null>(null);
  const layersAdded = useRef(false);

  // ---- the view from the URL (and the old page's section links, sent on to the two pages) ----
  useEffect(() => {
    if (OLD_HASH[location.hash]) { location.replace(OLD_HASH[location.hash]); return; }
    const q = new URLSearchParams(location.search);
    if (q.get("show") === "output") setShow("output");
    if (q.get("by") === "country") setBy("country");
    const f = q.get("flow");
    if (f === "ex" || f === "im") setFlow(f);
    if (q.get("place")) { setPick(q.get("place")); setFly("zoom"); }
  }, []);

  // ---- map ----
  useEffect(() => {
    if (!mapEl.current || mapRef.current) return;
    const map = createIndustryMap(mapEl.current, WORLD.center, WORLD.zoom);
    mapRef.current = map;
    // start with every place in view, clear of the controls above and the legend below; a phone held upright is too
    // narrow for that (the map can't zoom out past filling its height), so it starts on Europe to Japan
    const all = [...data.trade, ...data.output].map(r => r.lonlat);
    if (small()) map.jumpTo(PHONE);
    else map.fitBounds(all.reduce((b, p) => b.extend(p), new LngLatBounds(all[0], all[0])), { padding: { top: 170, bottom: 140, left: 50, right: 50 }, duration: 0 });
    map.on("load", () => setMapReady(true));
    map.on("zoom", () => setZoom(map.getZoom()));
    setZoom(map.getZoom());
    return () => { map.remove(); mapRef.current = null; };
  }, [data]);
  useEffect(() => {
    try { if (localStorage.getItem("scrapermap.basemap") === "satellite") setBasemapState("satellite"); } catch { /* storage unavailable */ }
  }, []);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;
    setBasemap(map, basemap);
    try { localStorage.setItem("scrapermap.basemap", basemap); } catch { /* storage unavailable */ }
  }, [mapReady, basemap]);

  // ---- circles for the view ----
  const pts = useMemo(() => points(data, show, by, flow), [data, show, by, flow]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;
    if (!layersAdded.current) { addIndustryLayers(map, pts, k => { setPick(k); setFly(small() ? "pan" : null); }); layersAdded.current = true; }
    else setIndustryPoints(map, pts);
  }, [mapReady, pts]);

  // a pick that isn't in the new view (a place with no output figure, say) is dropped
  const keys = useMemo(() => new Set(pts.map(p => p.key)), [pts]);
  const picked = pick && keys.has(pick) ? pick : null;
  useEffect(() => { if (pick && !keys.has(pick) && layersAdded.current) setPick(null); }, [pick, keys]);
  useEffect(() => {
    const map = mapRef.current;
    if (map && mapReady) setIndustrySelected(map, picked);
  }, [mapReady, picked, pts]);

  // ---- flying: in to a place picked from a list or the URL; a click on the map only pans, on a phone, clear of the panel ----
  const lonlatsOf = useCallback((key: string): [number, number][] => {
    if (by === "city") { const r = (show === "trade" ? data.trade : data.output).find(x => x.key === key); return r ? [r.lonlat] : []; }
    const c = (show === "trade" ? data.tradeCountries : data.outputCountries).find(x => x.key === key);
    if (!c) return [];
    const names = new Set(c.parts.map(p => p.place));
    return (show === "trade" ? data.trade : data.output).filter(r => names.has(r.name)).map(r => r.lonlat);
  }, [data, show, by]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !picked || !fly) return;
    setFly(null);
    if (fly === "pan") {
      const p = pts.find(x => x.key === picked);
      if (p) map.easeTo({ center: p.lonlat, padding: padding(), duration: 600 });
      return;
    }
    const ll = lonlatsOf(picked);
    if (ll.length === 1) map.easeTo({ center: ll[0], zoom: Math.max(map.getZoom(), 4.5), padding: padding(), duration: 900 });
    else if (ll.length > 1) {
      const b = ll.reduce((bb, p) => bb.extend(p), new LngLatBounds(ll[0], ll[0]));
      map.fitBounds(b, { padding: padding(), maxZoom: 5, duration: 900 });
    }
  }, [mapReady, picked, fly, lonlatsOf, pts]);
  const goPlace = useCallback((key: string) => { setBy("city"); setPick(key); setFly("zoom"); }, []);

  // ---- the URL follows the view ----
  useEffect(() => {
    const q = new URLSearchParams();
    if (show !== "trade") q.set("show", show);
    if (by !== "city") q.set("by", by);
    if (show === "trade" && flow !== "total") q.set("flow", flow);
    if (picked) q.set("place", picked);
    const s = q.toString();
    history.replaceState(null, "", `/industry/${s ? "?" + s : ""}`);
  }, [show, by, flow, picked]);

  const ranked = useMemo(() => [...pts].sort((a, b) => b.v - a.v).map(p => p.key), [pts]);
  const rank = picked ? ranked.indexOf(picked) + 1 : 0;
  const what = show === "trade" ? `goods ${FLOW_NAME[flow]}` : "manufacturing value added";

  return (
    <div className="app ind-app">
      <Nav active="industry" />
      <div ref={mapEl} className="map" aria-label={`Map of ${what} by ${by === "city" ? "city" : "country"}`} />
      <div className="ind-top">
        <div className="ind-controls">
          <Seg label="Figure" value={show} onChange={setShow} options={[["trade", "Trade"], ["output", "Industrial output"]]} />
          <Seg label="Places" value={by} onChange={setBy} options={[["city", "Cities"], ["country", "Countries"]]} />
          {show === "trade" && <Seg label="Trade flow" value={flow} onChange={setFlow} options={[["total", "Exports + imports"], ["ex", "Exports"], ["im", "Imports"]]} />}
          <button className={"btn basemap" + (basemap === "satellite" ? " on" : "")} onClick={() => setBasemapState(b => b === "satellite" ? "map" : "satellite")}
            aria-pressed={basemap === "satellite"} title={basemap === "satellite" ? "Switch to the map" : "Switch to satellite imagery"}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
              {basemap === "satellite"
                ? <path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2Zm0 0v14m6-12v14" strokeLinejoin="round" />
                : <><circle cx="12" cy="12" r="9" /><path d="M3.5 9h17M3.5 15h17M12 3c2.5 2.6 3.6 5.6 3.6 9s-1.1 6.4-3.6 9c-2.5-2.6-3.6-5.6-3.6-9S9.5 5.6 12 3Z" /></>}
            </svg>
            <span className="bm-label">{basemap === "satellite" ? "Map" : "Satellite"}</span>
          </button>
        </div>
        {!picked && (
          <div className="map-hint ind-hint">
            {by === "city"
              ? <>Each circle&apos;s area is to scale with a place&apos;s {what}, in US dollars, for 2025 or the latest year published. </>
              : <>Each circle adds up the {what} of a country&apos;s places on this map, Hong Kong with China. These are sums of the listed places, not national totals. </>}
            Click a circle for its figures and sources.
          </div>
        )}
      </div>
      <Legend show={show} by={by} flow={flow} zoom={zoom} hidden={!!picked} />
      {picked && (
        <aside className="panel ind-panel" aria-label="Figures for the selected place">
          <button className="x" onClick={() => setPick(null)} aria-label="Close">×</button>
          {show === "trade" && by === "city" && <TradePanel r={data.trade.find(x => x.key === picked) as MapTrade} flow={flow} rank={rank} of={pts.length}
            also={data.output.find(x => x.key === picked)} onShow={() => setShow("output")} />}
          {show === "output" && by === "city" && <MfgPanel r={data.output.find(x => x.key === picked) as MapMfg} rank={rank} of={pts.length}
            also={data.trade.find(x => x.key === picked)} onShow={() => setShow("trade")} />}
          {show === "trade" && by === "country" && <CountryTradePanel c={data.tradeCountries.find(x => x.key === picked) as MapCountryTrade} flow={flow} rank={rank} of={pts.length}
            data={data} onPlace={goPlace} also={data.outputCountries.find(x => x.key === picked)} onShow={() => setShow("output")} />}
          {show === "output" && by === "country" && <CountryMfgPanel c={data.outputCountries.find(x => x.key === picked) as MapCountryMfg} rank={rank} of={pts.length}
            data={data} onPlace={goPlace} also={data.tradeCountries.find(x => x.key === picked)} onShow={() => setShow("trade")} />}
        </aside>
      )}
    </div>
  );
}

function Seg<T extends string>({ label, value, onChange, options }: { label: string; value: T; onChange: (v: T) => void; options: [T, string][] }) {
  return (
    <div className="seg" role="group" aria-label={label}>
      {options.map(([v, text]) => (
        <button key={v} className={v === value ? "on" : undefined} aria-pressed={v === value} onClick={() => onChange(v)}>{text}</button>
      ))}
    </div>
  );
}

/** Reference circles for the current zoom (about 6, 15 and 30 px across the radius, at round dollar values), and what a
 *  hollow or pale circle means in this view. */
function Legend({ show, by, flow, zoom, hidden }: { show: Show; by: By; flow: Flow; zoom: number; hidden: boolean }) {
  const f = radiusAt(1, zoom), k = K[show];
  const nice = (x: number) => {
    const m = 10 ** Math.floor(Math.log10(x));
    return [1, 2, 5, 10].map(a => a * m).reduce((best, c) => Math.abs(Math.log(c / x)) < Math.abs(Math.log(best / x)) ? c : best);
  };
  const vals = [...new Set([30, 15, 6].map(r => nice((r / (k * f)) ** 2)))];
  const rs = vals.map(v => k * Math.sqrt(v) * f);
  const R = rs[0], W = 2 * R + 64, H = 2 * R + 4;
  const c = show === "trade" ? COLOR[flow] : COLOR.output;
  const fmt = (v: number) => v >= 1000 ? `$${v / 1000}tn` : `$${v}bn`;
  return (
    <div className={"ind-legend" + (hidden ? " under-panel" : "")} aria-hidden="true">
      <div className="il-title">{show === "trade" ? `Goods ${FLOW_NAME[flow]}` : "Manufacturing value added"}{by === "country" ? ", by country" : ""}</div>
      <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`}>
        {vals.map((v, i) => {
          const r = rs[i], cy = H - 2 - r, top = H - 2 - 2 * r;
          return (
            <g key={v}>
              <circle cx={R + 2} cy={cy} r={r} fill={c} fillOpacity={0.12} stroke={c} strokeWidth={1.2} />
              <line x1={R + 2} x2={2 * R + 10} y1={top} y2={top} stroke="#5A433A" strokeWidth={0.8} strokeDasharray="2 2" />
              <text x={2 * R + 13} y={top + 4} fontSize="11.5" fill="#2B1D17">{fmt(v)}</text>
            </g>
          );
        })}
      </svg>
      {show === "trade" && flow === "total" && <div className="il-key"><i className="hollow" style={{ borderColor: c }} />only exports published</div>}
      {show === "trade" && by === "city" && <div className="il-key"><i className="pale" style={{ borderColor: c, background: c }} />Japan: by customs port or airport</div>}
      {show === "output" && by === "city" && <div className="il-key"><i className="hollow" style={{ borderColor: c }} />upper bound, includes construction</div>}
    </div>
  );
}

/* ---- the panel ---- */

const Sources = ({ urls }: { urls: string[] }) => (
  <p className="ind-psrc">Sources: {urls.map((u, i) => <span key={i}>{i > 0 && ", "}<a href={encodeURI(u)} target="_blank" rel="noopener">{site(u)}</a></span>)}</p>
);
const Head = ({ kicker, color }: { kicker: string; color: string }) => (
  <div className="ind-head" style={{ background: color }}><span className="ind-kind">{kicker}</span></div>
);
const Fact = ({ dt, children, wide }: { dt: string; children: React.ReactNode; wide?: boolean }) => (
  <div className={wide ? "wide" : undefined}><dt>{dt}</dt><dd>{children}</dd></div>
);
const none = <span className="muted">not published</span>;

function Also({ label, value, onShow }: { label: string; value: string; onShow: () => void }) {
  return <button className="ind-also" onClick={onShow}>{label}: <b>{value}</b> <span aria-hidden="true">›</span></button>;
}

function TradePanel({ r, flow, rank, of, also, onShow }: { r: MapTrade; flow: Flow; rank: number; of: number; also?: MapMfg; onShow: () => void }) {
  return (
    <>
      <Head kicker={r.kind === "gateway" ? "Customs gateway" : "Goods trade"} color={COLOR[flow]} />
      <div className="body">
        <h1>{r.name}</h1>
        <p className="where"><span className="place">{r.country}</span> · {r.unit}</p>
        <dl className="facts ind-facts">
          <Fact dt="Exports">{r.ex == null ? none : money(r.ex)}</Fact>
          <Fact dt="Imports">{r.im == null ? none : money(r.im)}</Fact>
          <Fact dt="Exports + imports">{r.total == null ? none : money(r.total)}</Fact>
          <Fact dt="Year">{r.year}</Fact>
          <Fact dt="Rank on this map" wide>#{rank} of {of} by {FLOW_NAME[flow]}{flow === "total" && r.total == null ? " (by its exports)" : ""}</Fact>
        </dl>
        {(r.caveat || r.note) && <p className="ind-pnote">{r.caveat && <span className="pill">{r.caveat}</span>}{r.caveat && r.note && " "}{r.note}</p>}
        <p className="ind-how"><b>How counted:</b> {r.how}.</p>
        <Sources urls={r.source} />
        {also && <Also label="Industrial output" value={(also.upper ? "up to " : "") + money(also.va)} onShow={onShow} />}
        <div className="actions">
          {r.slug && <a className="btn" href={`/city/${r.slug}/`}>Skyscrapers in {r.name}</a>}
          <a className="btn" href={r.kind === "exports" ? "/industry/trade/#exports" : r.kind === "gateway" ? "/industry/trade/#ports" : "/industry/trade/#trade"}>All trade figures</a>
        </div>
      </div>
    </>
  );
}

function MfgPanel({ r, rank, of, also, onShow }: { r: MapMfg; rank: number; of: number; also?: MapTrade; onShow: () => void }) {
  const t = also ? also.total ?? also.ex : null;
  return (
    <>
      <Head kicker="Industrial output" color={COLOR.output} />
      <div className="body">
        <h1>{r.name}</h1>
        <p className="where"><span className="place">{r.country}</span> · {r.unit}</p>
        <dl className="facts ind-facts">
          <Fact dt="Value added">{r.upper ? "up to " : ""}{money(r.va)}</Fact>
          <Fact dt="Year">{r.year}</Fact>
          <Fact dt="Manufacturing jobs">{r.jobs == null ? none : r.jobs.toLocaleString("en-US")}</Fact>
          <Fact dt="Per job">{r.perJob == null ? none : moneyK(r.perJob)}</Fact>
          <Fact dt="Rank on this map" wide>#{rank} of {of}</Fact>
        </dl>
        {r.upper && <p className="ind-pnote">Only secondary-industry value added is published here, which adds construction, so this is an upper bound.</p>}
        {r.inside && <p className="ind-pnote">Inside {r.inside}, so it is left out of {r.country}&apos;s sum.</p>}
        {r.note && <p className="ind-pnote">{r.note}</p>}
        <p className="ind-how"><b>Measure:</b> {r.how}.</p>
        <Sources urls={r.source} />
        {also && t != null && <Also label={also.total == null ? "Exports" : "Exports + imports"} value={money(t)} onShow={onShow} />}
        <div className="actions">
          {r.slug && <a className="btn" href={`/city/${r.slug}/`}>Skyscrapers in {short(r.name)}</a>}
          <a className="btn" href="/industry/output/#manufacturing">All output figures</a>
        </div>
      </div>
    </>
  );
}

function PartList({ items, onPlace }: { items: { key: string | null; name: string; value: string; year: string; note?: string }[]; onPlace: (key: string) => void }) {
  return (
    <ol className="ind-parts">
      {items.map(p => (
        <li key={p.name}>
          {p.key ? <button className="link" onClick={() => onPlace(p.key as string)}>{p.name}</button> : <span>{p.name}</span>}
          <span className="ip-v">{p.value}{p.year !== "2025" && <small> {p.year}</small>}{p.note && <small> {p.note}</small>}</span>
        </li>
      ))}
    </ol>
  );
}

function CountryTradePanel({ c, flow, rank, of, data, onPlace, also, onShow }: {
  c: MapCountryTrade; flow: Flow; rank: number; of: number; data: IndustryMapData; onPlace: (key: string) => void; also?: MapCountryMfg; onShow: () => void;
}) {
  const keyOf = (name: string) => data.trade.find(r => r.name === name)?.key ?? null;
  const totalOnly = c.parts.filter(p => p.ex == null && p.total != null).map(p => p.place);
  const n = c.parts.length;
  return (
    <>
      <Head kicker="Goods trade by country" color={COLOR[flow]} />
      <div className="body">
        <h1>{c.country}</h1>
        <p className="where">The sum of its {n} place{n > 1 ? "s" : ""} on this map, not a national total</p>
        <dl className="facts ind-facts">
          <Fact dt="Exports">{c.ex ? money(c.ex) : none}</Fact>
          <Fact dt="Imports">{c.im ? money(c.im) : none}</Fact>
          <Fact dt="Exports + imports">{c.total == null ? none : money(c.total)}</Fact>
          <Fact dt={c.years.length > 1 ? "Years" : "Year"}>{yearSpan(c.years)}</Fact>
          <Fact dt="Rank on this map" wide>#{rank} of {of} countries by {FLOW_NAME[flow]}</Fact>
        </dl>
        {c.parts.some(p => p.place === "Hong Kong") && <p className="ind-pnote">Hong Kong is counted as part of China. Much of its trade, and Singapore&apos;s, is re-exports.</p>}
        {totalOnly.length > 0 && <p className="ind-pnote">{totalOnly.join(" and ")} publish{totalOnly.length === 1 ? "es" : ""} only a total, so {totalOnly.length === 1 ? "it counts" : "they count"} in exports plus imports but not in either alone.</p>}
        {c.total == null && <p className="ind-pnote">Only exports are published for {c.country === "United States" ? "US metro areas" : "these places"}.</p>}
        {c.parts.some(p => p.kind === "gateway") && <p className="ind-pnote">Japan publishes trade only by the port or airport where goods clear customs, so its places are its {n} busiest customs gateways.</p>}
        <h2 className="ind-h">Places added up</h2>
        <PartList onPlace={onPlace} items={c.parts.map(p => {
          const v = tradeValue(p, flow) ?? (flow === "total" ? p.ex : null);
          return { key: keyOf(p.place), name: p.place, year: p.year, value: v == null ? "–" : money(v), note: flow === "total" && p.total == null && p.ex != null ? "exports" : "" };
        })} />
        {also && <Also label="Industrial output" value={money(also.va)} onShow={onShow} />}
        <div className="actions"><a className="btn" href="/industry/trade/#countries">All countries</a></div>
      </div>
    </>
  );
}

function CountryMfgPanel({ c, rank, of, data, onPlace, also, onShow }: {
  c: MapCountryMfg; rank: number; of: number; data: IndustryMapData; onPlace: (key: string) => void; also?: MapCountryTrade; onShow: () => void;
}) {
  const keyOf = (name: string) => data.output.find(r => r.name === name)?.key ?? null;
  const counted = c.parts.filter(p => !p.inside), n = counted.length;
  const t = also ? also.total ?? also.ex : null;
  return (
    <>
      <Head kicker="Industrial output by country" color={COLOR.output} />
      <div className="body">
        <h1>{c.country}</h1>
        <p className="where">The sum of its {n} place{n > 1 ? "s" : ""} on this map, not a national total</p>
        <dl className="facts ind-facts">
          <Fact dt="Value added">{money(c.va)}</Fact>
          <Fact dt={c.years.length > 1 ? "Years" : "Year"}>{yearSpan(c.years)}</Fact>
          <Fact dt="Manufacturing jobs">{c.jobs == null ? none : <>{c.jobs.toLocaleString("en-US")}{c.jobPlaces < n && <small className="muted"> in {c.jobPlaces} of {n} places</small>}</>}</Fact>
          <Fact dt="Per job">{c.perJob == null ? none : <>{moneyK(c.perJob)}{c.jobPlaces < n && <small className="muted"> in those places</small>}</>}</Fact>
          <Fact dt="Rank on this map" wide>#{rank} of {of} countries</Fact>
        </dl>
        {c.upper > 0 && <p className="ind-pnote">{money(c.upper)} of it is upper bounds: cities that publish only secondary-industry value added, which adds construction.</p>}
        {c.parts.filter(p => p.inside).map(p => <p key={p.place} className="ind-pnote">{p.place} is inside {p.inside}, so it is left out of the sum.</p>)}
        {c.country === "Ireland" && <p className="ind-pnote">Ireland&apos;s figures are inflated by multinational profits booked there.</p>}
        <h2 className="ind-h">Places added up</h2>
        <PartList onPlace={onPlace} items={c.parts.map(p => ({
          key: keyOf(p.place), name: p.place, year: p.year, value: (p.upper ? "up to " : "") + money(p.va), note: p.inside ? `inside ${short(p.inside)}, not added` : "",
        }))} />
        {also && t != null && <Also label={also.total == null ? "Exports" : "Exports + imports"} value={money(t)} onShow={onShow} />}
        <div className="actions"><a className="btn" href="/industry/output/#countries">All countries</a></div>
      </div>
    </>
  );
}
