"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Map as MLMap, MapMouseEvent } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import "./timeCapsule.css";
import "./metro.css";
import "./history.css";
import {
  loadIndex, loadStates, loadGeo, loadChunk, windowFor, Timeline, areas as areasOf, capitalIn,
  FIRST_YEAR, LAST_YEAR, STATUS_NAME, ST_DIRECT, type HistIndex, type HistStates, type Chunk,
} from "@/lib/history";
import { CellGrid, xToLng, yToLat, lngToX, latToY } from "@/lib/historyGrid";
import { HistoryLayer } from "./historyLayer";
import { HistoryLabels } from "./historyLabels";
import { createHistoryMap, addHistoryLayers, setCapitals, setHistoryBasemap } from "./historyMap";
import HistoryYears from "./HistoryYears";
import HistoryPanel, { type PanelNow } from "./HistoryPanel";
import HistorySearch from "./HistorySearch";
import Nav from "./Nav";

const DEFAULT_YEAR = 1300;
function startView(): { center: [number, number]; zoom: number } {
  if (typeof window !== "undefined" && window.innerWidth <= 720) return { center: [50, 32], zoom: 0.55 };
  return { center: [45, 30], zoom: 1.75 };
}
function padding(panel: boolean) {
  const p = { top: 110, right: 40, bottom: 200, left: 40 };
  if (typeof window === "undefined") return p;
  if (window.innerWidth <= 720) { p.top = 100; p.right = 20; p.left = 20; p.bottom = panel ? Math.round(window.innerHeight * 0.6) : 180; }
  else if (panel) p.right = 440;
  return p;
}

interface Base { idx: HistIndex; st: HistStates; tl: Timeline; grid: CellGrid; layer: HistoryLayer }
interface Shown { year: number; version: number; chunk: Chunk }
interface Hover { x: number; y: number; owner: number; status: number; party: number }

/** The /history page: every state's borders, year by year, from 6000 BCE to 2026. */
export default function HistoryApp() {
  const mapEl = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MLMap | null>(null);
  const [base, setBase] = useState<Base | null>(null);
  const [failed, setFailed] = useState(false);
  const [mapReady, setMapReady] = useState(false);
  const [year, setYearState] = useState<number | null>(null);
  const [shown, setShown] = useState<Shown | null>(null);
  const [pick, setPick] = useState<number | null>(null);
  const [basemap, setBasemapState] = useState<"map" | "satellite">("map");
  const [hover, setHover] = useState<Hover | null>(null);
  const [about, setAbout] = useState(false);
  const labels = useRef<HistoryLabels | null>(null);
  const wanted = useRef<number | null>(null);
  const flyTo = useRef<number | null>(null);
  const layersAdded = useRef(false);

  const setYear = useCallback((y: number) => setYearState(Math.max(FIRST_YEAR, Math.min(LAST_YEAR, Math.round(y)))), []);

  // ---- data, then the year and state from the URL (?year=-500, ?state=<slug>) ----
  useEffect(() => {
    Promise.all([loadIndex(), loadStates(), loadGeo()]).then(([idx, st, geo]) => {
      const tl = new Timeline(geo.N);
      const grid = new CellGrid(geo);
      const layer = new HistoryLayer(geo, tl);
      layer.setStates(st);
      setBase({ idx, st, tl, grid, layer });
      // a handle for checking the map from the browser console (and the screenshot script)
      (window as unknown as { __history?: unknown }).__history = { idx, st, tl, grid, layer, loadChunk, windowFor };
      const q = new URLSearchParams(location.search);
      const ys = q.get("year");
      const s = q.get("state");
      const k = s ? st.slug.indexOf(s) : -1;
      let y = ys !== null && ys !== "" && Number.isFinite(Number(ys)) ? Number(ys) : DEFAULT_YEAR;
      if (k >= 0) {
        if (ys === null && st.first[k] !== null) y = st.first[k]!;
        setPick(k + 1); flyTo.current = k + 1;
      }
      setYear(y);
    }).catch(e => { console.error(e); setFailed(true); });
  }, [setYear]);

  // ---- map ----
  useEffect(() => {
    if (!mapEl.current || mapRef.current) return;
    const v = startView();
    const map = createHistoryMap(mapEl.current, v.center, v.zoom);
    mapRef.current = map;
    map.on("load", () => setMapReady(true));
    return () => { map.remove(); mapRef.current = null; };
  }, []);
  useEffect(() => {
    try { if (localStorage.getItem("scrapermap.basemap") === "satellite") setBasemapState("satellite"); } catch { /* storage unavailable */ }
  }, []);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !base || layersAdded.current) return;
    addHistoryLayers(map, base.layer);
    layersAdded.current = true;
    labels.current = new HistoryLabels(map, base.grid, base.st);
    return () => { labels.current?.destroy(); labels.current = null; };
  }, [mapReady, base]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !base || !layersAdded.current) return;
    setHistoryBasemap(map, base.layer, basemap);
    try { localStorage.setItem("scrapermap.basemap", basemap); } catch { /* storage unavailable */ }
  }, [mapReady, base, basemap]);

  // ---- the year: load its window, bring the timeline there ----
  useEffect(() => {
    if (!base || year === null) return;
    wanted.current = year;
    const w = windowFor(base.idx, year);
    loadChunk(w.id).then(chunk => {
      if (wanted.current !== year) return;
      base.tl.apply(chunk, year);
      base.layer.refresh();
      setShown({ year, version: base.tl.version, chunk });
      // the next window, before Play gets there
      const i = base.idx.windows.indexOf(w);
      if (i >= 0 && i + 1 < base.idx.windows.length && year - w.from > (w.to - w.from) * 0.6) loadChunk(base.idx.windows[i + 1].id);
    }).catch(e => console.error(e));
  }, [base, year]);

  const area = useMemo(() => (base && shown ? areasOf(base.tl, base.st.count) : null), [base, shown]);
  const totals = useMemo(() => {
    if (!area) return { states: 0, cells: 0 };
    let s = 0, c = 0;
    for (let i = 1; i < area.length; i++) if (area[i] > 0) { s++; c += area[i]; }
    return { states: s, cells: c };
  }, [area]);

  // labels and capitals follow the year (at most five times a second while it moves)
  const lastLabel = useRef(0);
  useEffect(() => {
    if (!base || !shown || !area || !mapReady) return;
    const run = () => {
      lastLabel.current = performance.now();
      labels.current?.update(base.tl, area);
      const map = mapRef.current;
      if (!map) return;
      const caps: [number, number, number, number, string][] = [];
      for (let i = 1; i < area.length; i++) {
        if (!area[i]) continue;
        const c = capitalIn(base.st.capitals[i - 1], shown.year);
        if (c) caps.push([c[1], c[2], area[i], i, c[0]]);
      }
      setCapitals(map, caps);
    };
    const wait = 200 - (performance.now() - lastLabel.current);
    if (wait <= 0) { run(); return; }
    const t = setTimeout(run, wait);
    return () => clearTimeout(t);
  }, [base, shown, area, mapReady]);

  // fly to a state picked from search or the URL, once its year is on the map
  useEffect(() => {
    const map = mapRef.current;
    const id = flyTo.current;
    if (!map || !base || !shown || id === null || !mapReady) return;
    flyTo.current = null;
    const { owner } = base.tl, { x, y } = base.grid.geo;
    let x0 = 2, x1 = -2, y0 = 2, y1 = -2, s0 = 2, s1 = -2, n = 0;
    for (let i = 0; i < owner.length; i++) {
      if (owner[i] !== id) continue;
      n++;
      const xx = x[i], ss = xx < 0.5 ? xx + 1 : xx;
      if (xx < x0) x0 = xx; if (xx > x1) x1 = xx; if (ss < s0) s0 = ss; if (ss > s1) s1 = ss;
      if (y[i] < y0) y0 = y[i]; if (y[i] > y1) y1 = y[i];
    }
    if (!n) return;
    if (s1 - s0 < x1 - x0) { x0 = s0; x1 = s1; }
    map.fitBounds([[xToLng(x0), yToLat(y1)], [xToLng(x1), yToLat(y0)]], { padding: padding(true), maxZoom: 6, duration: 900 });
  }, [base, shown, mapReady]);

  // ---- the picked state, on the layer, the labels and in the URL ----
  useEffect(() => {
    if (!base) return;
    base.layer.sel = pick ?? 0;
    base.layer.refresh();
    if (labels.current) { labels.current.sel = pick ?? 0; labels.current.layout(); }
  }, [base, pick]);
  useEffect(() => {
    if (!base || year === null) return;
    const t = setTimeout(() => {
      const q = new URLSearchParams();
      q.set("year", String(year));
      if (pick && base.st.slug[pick - 1]) q.set("state", base.st.slug[pick - 1]);
      history.replaceState(null, "", `/history/?${q.toString()}`);
    }, 400);
    return () => clearTimeout(t);
  }, [base, pick, year]);

  const now = useMemo<PanelNow>(() => {
    if (!base || !shown || !pick) return { cells: 0, status: "", party: 0 };
    const { owner, status, other } = base.tl;
    const byStatus = [0, 0, 0, 0, 0];
    const party = new Map<number, number>();
    let cells = 0;
    for (let i = 0; i < owner.length; i++) {
      if (owner[i] !== pick) continue;
      cells++; byStatus[status[i]]++;
      if (status[i] !== ST_DIRECT && other[i]) party.set(other[i] * 8 + status[i], (party.get(other[i] * 8 + status[i]) ?? 0) + 1);
    }
    let st = 0;
    if (byStatus[1] > cells / 2) st = 1; else if (byStatus[2] > cells / 2) st = 2; else if (byStatus[3]) st = 3; else if (byStatus[4]) st = 4;
    let best = 0, bn = 0;
    for (const [k, v] of party) if (k % 8 === st && v > bn) { bn = v; best = Math.floor(k / 8); }
    return { cells, status: STATUS_NAME[st], party: st ? best : 0 };
  }, [base, shown, pick]);

  // ---- hover and click on the map ----
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !base) return;
    let raf = 0, last: MapMouseEvent | null = null;
    const cellAt = (e: MapMouseEvent) => base.grid.find(lngToX(e.lngLat.lng), latToY(e.lngLat.lat));
    const move = (e: MapMouseEvent) => {
      last = e;
      if (raf) return;
      raf = requestAnimationFrame(() => {
        raf = 0;
        if (!last) return;
        const c = cellAt(last);
        const o = c >= 0 ? base.tl.owner[c] : 0;
        if (base.layer.hover !== o) { base.layer.hover = o; base.layer.refresh(); }
        map.getCanvas().style.cursor = o ? "pointer" : "";
        setHover(c >= 0 && o ? { x: last.point.x, y: last.point.y, owner: o, status: base.tl.status[c], party: base.tl.other[c] } : null);
      });
    };
    const out = () => { base.layer.hover = 0; base.layer.refresh(); setHover(null); };
    const click = (e: MapMouseEvent) => {
      const c = cellAt(e);
      const o = c >= 0 ? base.tl.owner[c] : 0;
      setPick(o || null);
    };
    map.on("mousemove", move);
    map.on("mouseout", out);
    map.on("click", click);
    return () => { map.off("mousemove", move); map.off("mouseout", out); map.off("click", click); cancelAnimationFrame(raf); };
  }, [mapReady, base]);

  const choose = useCallback((o: number) => {
    if (!base) return;
    const k = o - 1;
    setPick(o);
    const f = base.st.first[k], l = base.st.last[k];
    if (f !== null && l !== null && year !== null && (year < f || year > l)) setYear(f);
    flyTo.current = o;
    // already on this year: fly now
    if (shown && (f === null || year === null || (year >= f && year <= (l ?? f)))) setShown(s => s ? { ...s } : s);
  }, [base, year, shown, setYear]);

  const captions = useMemo(() => {
    if (!base || !shown || !area) return [];
    return shown.chunk.captions
      .filter(c => c.y === shown.year && c.s > 0)
      .map(c => ({ ...c, name: base.st.name[c.s - 1], colour: base.st.colour[c.s - 1], a: area[c.s] || base.st.peak[c.s - 1] / 10 }))
      .sort((a, b) => b.a - a.a);
  }, [base, shown, area]);

  const ready = !!shown && shown.year === year;
  const st = base?.st ?? null;
  const hoverText = (h: Hover) => {
    if (!st) return "";
    const name = st.name[h.owner - 1];
    const p = h.party ? st.name[h.party - 1] : "";
    return h.status === 1 && h.party && h.party !== h.owner ? `${name}, vassal of ${p}`
      : h.status === 1 ? `${name} (vassal lands)`
      : h.status === 2 && h.party ? `${name}, in ${p}`
      : h.status === 3 && h.party ? `${name}, occupied by ${p}`
      : h.status === 4 && h.party ? `${name}, contested by ${p}`
      : name;
  };

  return (
    <div className="app capsule-on metro-app history-app">
      <Nav active="history" />
      <div ref={mapEl} className="map" aria-label="Map of the world's states and their borders in the chosen year" />
      <div className="topbar">
        <HistorySearch st={st} onPick={choose} />
        <button className={"btn" + (about ? " on" : "")} onClick={() => setAbout(a => !a)} aria-expanded={about} title="How this map is made">
          <span>About</span>
        </button>
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
      {about && <About onClose={() => setAbout(false)} built={base?.idx.built} draft={base ? base.idx.windows.filter(w => w.src === "draft").length : 0} fb={st ? st.fb.filter((v, i) => v && st.slug[i]).length : 0} />}
      {hover && st && !pick && (
        <div className="h-tip" style={{ left: hover.x, top: hover.y }}>{hoverText(hover)}</div>
      )}
      {!pick && <div className="legend h-legend" aria-hidden>
        <span><i className="hl-state" />state</span>
        <span><i className="hl-vassal" />vassal (suzerain&apos;s tint)</span>
        <span><i className="hl-occupied" />occupied</span>
        <span><i className="hl-contested" />contested</span>
        <span><i className="hl-culture" />culture</span>
        <span><i className="hl-none" />nobody&apos;s land</span>
        <span><i className="hl-new" />gained this year</span>
      </div>}
      {base && year !== null && (
        <HistoryYears year={year} onYear={setYear} changed={base.idx.changed} captions={captions} statesAlive={totals.states} cellsHeld={totals.cells}
          ready={ready} onPickState={choose} panelOpen={!!pick} />
      )}
      {st && pick && year !== null && <HistoryPanel st={st} owner={pick} year={year} now={now} onYear={setYear} onPick={choose} onClose={() => setPick(null)} />}
      {!shown && <div className="loading">{failed ? "The map could not be loaded." : "Loading eight thousand years of borders…"}</div>}
    </div>
  );
}

function About({ onClose, built, draft, fb }: { onClose: () => void; built?: string; draft: number; fb: number }) {
  return (
    <div className="h-about" role="dialog" aria-label="About CartaHistoria">
      <button className="x" onClick={onClose} aria-label="Close">×</button>
      <h2>About CartaHistoria</h2>
      <p>Every state&apos;s borders from 6000 BCE to 2026, one year at a time, on a grid of 524,441 hexagons of about 253 km² each (H3 resolution 5) that covers the world&apos;s land.</p>
      <p>The borders start from <a href="https://seshat-db.com/" target="_blank" rel="noopener">Cliopatria</a>, the Seshat Global History Databank&apos;s polity shapes (CC BY 4.0), corrected, split and dated year by year from Wikipedia, read page by page; each state&apos;s page lists the pages behind it.</p>
      <p>A state keeps one colour for life, the conventional one where there is one (Rome red, France blue). A lighter tint of a state&apos;s colour is its vassal; member states (an Imperial Estate, a Soviet republic) keep their own colour inside their realm&apos;s border; hatching in a state&apos;s colour is land it occupies; a blend of two colours with a fine hatch is land they are fighting over; grey is nobody&apos;s land; dotted pastels are archaeological cultures, not states. Land a state gains is outlined in orange for its first year.</p>
      <p className="muted">Data of {built ?? "…"}{draft ? `; ${draft} of 119 windows are still drafts under review` : ""}{fb ? `, and ${fb.toLocaleString("en-US")} states have a provisional colour` : ""}. Basemap © OpenFreeMap, OpenMapTiles, OpenStreetMap contributors.</p>
    </div>
  );
}

