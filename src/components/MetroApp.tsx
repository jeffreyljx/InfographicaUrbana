"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Map as MLMap } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import "./timeCapsule.css";
import "./metro.css";
import { loadMetro, kmOpenBySystem, stationKey, stationByKey, type MetroData } from "@/lib/metro";
import { setBasemap, type Basemap } from "./towerMap";
import { createMetroMap, addMetroLayers, setMetroYear, setSystemDots, setSelectedStation, SYSTEM_ZOOM, NEW_COLOR } from "./metroMap";
import MetroYears from "./MetroYears";
import MetroPanel, { type MetroPick } from "./MetroPanel";
import MetroSearch from "./MetroSearch";
import Nav from "./Nav";

const WORLD: { center: [number, number]; zoom: number } = { center: [40, 28], zoom: 1.9 };
/** Keep what was picked clear of the panel (right, or bottom sheet on a phone) and of the year dock. */
function padding(panel: boolean) {
  const p = { top: 110, right: 40, bottom: 190, left: 40 };
  if (typeof window === "undefined") return p;
  if (window.innerWidth <= 720) { p.top = 100; p.right = 20; p.left = 20; p.bottom = panel ? Math.round(window.innerHeight * 0.6) : 190; }
  else if (panel) p.right = 440;
  return p;
}

/** The /metro page: the world's metro lines on the warm basemap, growing year by year, with station, line and system panels. */
export default function MetroApp() {
  const mapEl = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MLMap | null>(null);
  const [data, setData] = useState<MetroData | null>(null);
  const [failed, setFailed] = useState(false);
  const [mapReady, setMapReady] = useState(false);
  const [year, setYear] = useState<number | null>(null);
  const [pick, setPick] = useState<MetroPick | null>(null);
  const [basemap, setBasemapState] = useState<Basemap>("map");
  const [zoomedOut, setZoomedOut] = useState(true);
  const layersAdded = useRef(false);

  // ---- data, and the first year / pick from the URL (?year=1900, ?station=<system>~<name>, ?line=<id>, ?system=<id>) ----
  useEffect(() => {
    loadMetro().then(d => {
      setData(d);
      const q = new URLSearchParams(location.search);
      const y = Number(q.get("year"));
      setYear(y ? Math.min(d.last, Math.max(d.first, Math.round(y))) : d.last);
      const st = q.get("station"), ln = q.get("line"), sy = q.get("system");
      if (st) { const s = stationByKey(d, st); if (s) setPick({ kind: "station", i: s.i }); }
      else if (ln) { const l = d.lines.find(x => x.id === ln); if (l) setPick({ kind: "line", i: l.i }); }
      else if (sy) { const s = d.systems.find(x => x.id === sy); if (s) setPick({ kind: "system", i: s.i }); }
    }).catch(() => setFailed(true));
  }, []);

  // ---- map ----
  useEffect(() => {
    if (!mapEl.current || mapRef.current) return;
    const map = createMetroMap(mapEl.current, WORLD.center, WORLD.zoom);
    mapRef.current = map;
    map.on("load", () => setMapReady(true));
    const check = () => setZoomedOut(map.getZoom() < SYSTEM_ZOOM);
    map.on("zoomend", check);
    return () => { map.remove(); mapRef.current = null; };
  }, []);

  // basemap: vector map or satellite, shared with the tower map's choice
  useEffect(() => {
    try { if (localStorage.getItem("scrapermap.basemap") === "satellite") setBasemapState("satellite"); } catch { /* storage unavailable */ }
  }, []);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;
    setBasemap(map, basemap);
    try { localStorage.setItem("scrapermap.basemap", basemap); } catch { /* storage unavailable */ }
  }, [mapReady, basemap]);

  // ---- the year: km open per system, the dock's figures ----
  const scopeSys = useMemo(() => {
    if (!data || !pick) return null;
    return pick.kind === "system" ? pick.i : pick.kind === "line" ? data.lines[pick.i].sys : data.stations[pick.i].sys;
  }, [data, pick]);
  const kmBySys = useMemo(() => data && year !== null ? kmOpenBySystem(data, year) : [], [data, year]);
  const perYear = useMemo(() => !data ? [] : scopeSys === null ? data.kmPerYear : data.kmPerYearBySys[scopeSys], [data, scopeSys]);
  /** the longest stretch of new line in each year: [line, km] */
  const newByYear = useMemo(() => {
    const m = new Map<number, Map<number, number>>();
    if (!data) return m;
    for (const t of data.tracks) for (const r of t.runs) {
      const ym = m.get(r.year) ?? new Map<number, number>();
      ym.set(t.line, (ym.get(t.line) ?? 0) + r.km);
      m.set(r.year, ym);
    }
    return m;
  }, [data]);
  const newest = useMemo(() => {
    if (!data || year === null) return null;
    let best: [number, number] | null = null;
    for (const [l, k] of newByYear.get(year) ?? []) {
      if (scopeSys !== null && data.lines[l].sys !== scopeSys) continue;
      if (data.lines[l].closeYear <= year) continue;
      if (!best || k > best[1]) best = [l, k];
    }
    if (!best) return null;
    const l = data.lines[best[0]];
    return { line: l.i, name: l.name, city: data.systems[l.sys].city, colour: l.colour };
  }, [data, year, newByYear, scopeSys]);

  // ---- picking: fly there, open the panel, put it in the URL ----
  const fly = useCallback((p: MetroPick, d: MetroData, instant = false) => {
    const map = mapRef.current;
    if (!map) return;
    const pad = padding(true), duration = instant ? 0 : 900;
    if (p.kind === "station") {
      const st = d.stations[p.i];
      map.flyTo({ center: [st.lon, st.lat], zoom: Math.max(map.getZoom(), 14.2), padding: pad, duration, essential: true });
    } else {
      const b = p.kind === "line" ? d.lines[p.i].bbox : d.systems[p.i].placed ? d.systems[p.i].bbox : null;
      if (b) map.fitBounds([[b[0], b[1]], [b[2], b[3]]], { padding: pad, duration, maxZoom: 13.5 });
    }
  }, []);
  const choose = useCallback((p: MetroPick) => {
    setPick(p);
    if (data) fly(p, data);
  }, [data, fly]);
  const close = useCallback(() => setPick(null), []);

  // the URL follows the pick and (after a pause, so Play doesn't flood the history) the year
  useEffect(() => {
    if (!data || year === null) return;
    const t = setTimeout(() => {
      const q = new URLSearchParams();
      if (pick?.kind === "station") q.set("station", stationKey(data, data.stations[pick.i]));
      if (pick?.kind === "line") q.set("line", data.lines[pick.i].id);
      if (pick?.kind === "system") q.set("system", data.systems[pick.i].id);
      if (year !== data.last) q.set("year", String(year));
      const s = q.toString().replace(/%7E/g, "~").replace(/%3A/g, ":");
      history.replaceState(null, "", `/metro/${s ? "?" + s : ""}`);
    }, 400);
    return () => clearTimeout(t);
  }, [data, pick, year]);

  // ---- layers ----
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !data || year === null || layersAdded.current) return;
    addMetroLayers(map, data, kmOpenBySystem(data, year), year, {
      onStation: i => setPick({ kind: "station", i }),
      onLine: i => setPick({ kind: "line", i }),
      onSystem: i => { setPick({ kind: "system", i }); fly({ kind: "system", i }, data); },
    });
    layersAdded.current = true;
    if (pick) fly(pick, data, true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mapReady, data, year]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !layersAdded.current || year === null) return;
    setMetroYear(map, year, pick?.kind === "line" ? pick.i : null);
  }, [mapReady, data, year, pick]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !layersAdded.current || !data) return;
    setSystemDots(map, data, kmBySys);
  }, [mapReady, data, kmBySys]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !layersAdded.current) return;
    setSelectedStation(map, pick?.kind === "station" ? pick.i : null);
  }, [mapReady, data, pick]);

  const kmOpen = scopeSys === null ? kmBySys.reduce((a, b) => a + b, 0) : kmBySys[scopeSys] ?? 0;
  const systemsOpen = useMemo(() => !data ? 0 : new Set(kmBySys.flatMap((k, i) => k > 0.05 ? [data.systems[i].city] : [])).size, [data, kmBySys]);
  const scope = data && scopeSys !== null ? data.systems[scopeSys].city : null;

  return (
    <div className="app capsule-on metro-app">
      <Nav active="metro" />
      <div ref={mapEl} className="map" aria-label="Map of the world's metro lines" />
      <div className="topbar">
        <MetroSearch data={data} onPick={choose} />
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
      {data && zoomedOut && !pick && year !== null && (
        <div className="map-hint">Each dot is a city&apos;s metro in {year}, sized by its length. Zoom in, or search, to see the lines and stations; Play to watch them grow from {data.first}.</div>
      )}
      <div className="legend metro-legend" aria-hidden>
        <span><i className="m-st" />station</span>
        <span><i className="m-st inter" />interchange</span>
        {year !== null && <span><i className="m-new" style={{ background: NEW_COLOR }} />opened in {year}</span>}
      </div>
      {data && year !== null && (
        <MetroYears first={data.first} last={data.last} year={year} onYear={setYear} perYear={perYear} kmOpen={kmOpen} systemsOpen={systemsOpen}
          newest={newest} onPickLine={i => choose({ kind: "line", i })} scope={scope}
          playFrom={scopeSys !== null ? data.systems[scopeSys].first - 1 : undefined} panelOpen={!!pick} />
      )}
      {data && pick && year !== null && <MetroPanel data={data} pick={pick} year={year} onPick={choose} onClose={close} />}
      {!data && <div className="loading">{failed ? "The metro map could not be loaded." : "Loading the world's metro lines…"}</div>}
    </div>
  );
}
