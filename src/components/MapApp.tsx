"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Map as MLMap } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import "./timeCapsule.css";
import { towerSlug, type Tower, type TowerIndex, type TowerRow, type DetailsFile } from "@/lib/types";
import { loadIndex, loadDetails, resolveRow, norm, detailFor } from "@/lib/client";
import { createMap, addTowerLayers, rowsToGeoJSON, setTowerData, setSelected, setBasemap, setBoundary, setCapsuleYear, setCapsuleLost, setTowersVisible, type Basemap } from "./towerMap";
import { boundaryFor } from "@/lib/boundary";
import { setSkyline } from "./skylineLayer";
import { addTowerIcons } from "./towerIcons";
import Panel from "./Panel";
import Chooser from "./Chooser";
import Filters, { type FilterState, DEFAULT_FILTERS, applyFilters } from "./Filters";
import Search from "./Search";
import TimeCapsule from "./TimeCapsule";
import { capsuleRange, standingIn, lostIn, perYear } from "@/lib/timeCapsule";
import { lostRows, resolveLost } from "@/lib/lostTowers";
import Legend from "./Legend";
import Nav from "./Nav";
import placesJson from "@/data/places.json";
import type { Places } from "@/lib/types";
const PLACES = placesJson as unknown as Places;

export interface MapAppProps {
  /** Pre-resolved tower for /tower/<slug> pages: panel renders before any data loads. */
  initialTower?: Tower;
  /** Initial camera for city/district deep links. */
  initialView?: { center: [number, number]; zoom: number; city?: string; district?: string };
}

const WORLD: { center: [number, number]; zoom: number } = { center: [60, 22], zoom: 1.9 };
/** Keep the selected pin centred in the part of the map the panel doesn't cover. */
function panelPadding(): { top: number; right: number; bottom: number; left: number } {
  const p = { top: 0, right: 0, bottom: 0, left: 0 };
  if (typeof window === "undefined") return p;
  if (window.innerWidth <= 720) p.bottom = Math.round(window.innerHeight * 0.55); else p.right = 420;
  return p;
}

export default function MapApp({ initialTower, initialView }: MapAppProps) {
  const mapEl = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MLMap | null>(null);
  const [idx, setIdx] = useState<TowerIndex | null>(null);
  const detailsRef = useRef<DetailsFile | null>(null);
  const [detailsReady, setDetailsReady] = useState(false);
  const rowsById = useMemo(() => { const m = new Map<number, TowerRow>(); idx?.rows.forEach(r => m.set(r[0], r)); return m; }, [idx]);

  const [filters, setFilters] = useState<FilterState>(() => ({
    ...DEFAULT_FILTERS,
    city: initialView?.city ?? null,
    district: initialView?.district ?? null,
  }));
  const [selected, setSelectedTower] = useState<Tower | null>(initialTower ?? null);
  const [chooser, setChooser] = useState<{ ids: number[]; at: { x: number; y: number } } | null>(null);
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [mapReady, setMapReady] = useState(false);
  const [basemap, setBasemapState] = useState<Basemap>("map");
  const [skyline, setSkylineOn] = useState(false);
  /** "Hide towers": every tower marker off, leaving the basemap and the skyline extents (?towers=0 opens the map this way). */
  const [towersHidden, setTowersHidden] = useState(false);
  const [zoomedOut, setZoomedOut] = useState(true);
  /** Time capsule: null while it is off, otherwise the chosen year (only towers standing then are shown). */
  const [asOf, setAsOf] = useState<number | null>(null);
  const asOfRef = useRef(asOf);
  asOfRef.current = asOf;
  /** Towers that have since come down, shown only in the time capsule. */
  const lost = useMemo(() => idx ? lostRows(idx) : null, [idx]);
  const pendingFit = useRef<[number, number, number, number] | null>(null);

  // ---- data ---------------------------------------------------------------
  useEffect(() => {
    loadIndex().then(setIdx);
    // deep links from city / district pages: /?city=…&district=…
    const q = new URLSearchParams(location.search);
    const qc = q.get("city"), qd = q.get("district");
    if (qc && !initialView) {
      setFilters(f => ({ ...f, city: qc, district: qd }));
      const agg = qd ? PLACES.districts.find(x => x.city === qc && x.name === qd) : PLACES.cities.find(x => x.name === qc);
      if (agg) pendingFit.current = agg.bbox;
    }
    const kick = () => loadDetails().then(d => { detailsRef.current = d; setDetailsReady(true); });
    if ("requestIdleCallback" in window) (window as Window & { requestIdleCallback: (cb: () => void) => void }).requestIdleCallback(kick);
    else setTimeout(kick, 1200);
  }, []);

  const resolveId = useCallback((id: number): Tower | null => {
    if (!idx) return null;
    const gone = lost?.byId.get(id);
    if (gone) return resolveLost(idx, lost!.rows.find(r => r[0] === id)!, gone);
    const row = rowsById.get(id);
    if (!row) return null;
    return resolveRow(idx, row, detailFor(detailsRef.current, id, row[1]));
  }, [idx, rowsById, lost]);

  // Once details arrive, upgrade the selected tower (unless it came pre-resolved).
  useEffect(() => {
    if (detailsReady && selected && !selected.lost && !selected.detail?.slug) {
      const t = resolveId(selected.id); if (t) setSelectedTower(t);
    }
  }, [detailsReady, selected, resolveId]);

  // ---- filtered rows ------------------------------------------------------
  const capsuleOn = asOf !== null;
  const range = useMemo(() => idx && lost ? capsuleRange(idx, lost.rows) : null, [idx, lost]);
  // time capsule: completed towers with a year that pass the other filters, and the lost towers that pass them;
  // the chosen year then cuts them down to the ones standing
  const capsuleBase = useMemo(() => idx && lost && capsuleOn
    ? applyFilters(idx, filters, true).concat(applyFilters({ ...idx, rows: lost.rows }, filters, true)) : null, [idx, lost, filters, capsuleOn]);
  const filteredRows = useMemo(() => !idx ? [] : capsuleBase && asOf !== null ? standingIn(capsuleBase, asOf, lost?.gone) : applyFilters(idx, filters), [idx, lost, filters, capsuleBase, asOf]);
  /** Lost towers that came down in the chosen year: a ghost ring marks where they stood. */
  const capsuleLost = useMemo(() => capsuleBase && lost && asOf !== null ? lostIn(capsuleBase, asOf, lost.gone) : [], [capsuleBase, lost, asOf]);
  const capsuleCounts = useMemo(() => capsuleBase && range ? perYear(capsuleBase, range.first, range.last) : [], [capsuleBase, range]);
  const capsuleTallest = useMemo(() => {
    if (!idx || !capsuleOn) return null;
    let t: TowerRow | null = null;
    for (const r of filteredRows) if (!t || r[4] > t[4]) t = r;
    return t ? { id: t[0], name: t[1], height: t[4], city: t[5] >= 0 ? idx.cities[t[5]] : lost?.byId.get(t[0])?.city ?? "" } : null;
  }, [idx, lost, capsuleOn, filteredRows]);

  // ---- select / URL -------------------------------------------------------
  const select = useCallback((id: number, fly = true) => {
    const t = resolveId(id);
    if (!t) return;
    setSelectedTower(t);
    setChooser(null);
    const map = mapRef.current;
    if (map) {
      setSelected(map, id);
      map.flyTo({ center: [t.lon, t.lat], zoom: fly ? Math.max(map.getZoom(), 15.2) : map.getZoom(), padding: panelPadding(), duration: fly ? 900 : 450, essential: true });
    }
    // a lost tower has no page of its own: link to the time capsule in a year it stood (or the year it came down)
    if (t.lost) history.replaceState(null, "", `/?year=${Math.min(t.lost.gone, Math.max(t.lost.completed, asOfRef.current ?? t.lost.gone - 1))}&id=${id}`);
    else history.replaceState(null, "", `/tower/${towerSlug(t.name, id)}/`);
  }, [resolveId]);

  const close = useCallback(() => {
    setSelectedTower(null);
    if (mapRef.current) { setSelected(mapRef.current, null); mapRef.current.easeTo({ padding: { top: 0, right: 0, bottom: 0, left: 0 }, duration: 300 }); }
    history.replaceState(null, "", "/");
  }, []);

  // ---- map ----------------------------------------------------------------
  useEffect(() => {
    if (!mapEl.current || mapRef.current) return;
    const view = initialTower ? { center: [initialTower.lon, initialTower.lat] as [number, number], zoom: 15.4 } : (initialView ?? WORLD);
    const map = createMap(mapEl.current, view.center, view.zoom);
    mapRef.current = map;
    map.on("load", () => setMapReady(true));
    return () => { map.remove(); mapRef.current = null; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  // initialView prop is only used for the first camera; deps intentionally empty.

  // ---- basemap: vector map or satellite imagery (remembered per browser) ----
  useEffect(() => {
    try { if (localStorage.getItem("scrapermap.basemap") === "satellite") setBasemapState("satellite"); } catch { /* storage unavailable */ }
  }, []);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;
    setBasemap(map, basemap);
    try { localStorage.setItem("scrapermap.basemap", basemap); } catch { /* storage unavailable */ }
  }, [mapReady, basemap]);

  // ---- skyline extent: every dense pocket of 5+ towers, in any city (remembered per browser; ?skyline=1 turns it on) ----
  useEffect(() => {
    const q = new URLSearchParams(location.search).get("skyline");
    if (q === "1" || q === "0") { setSkylineOn(q === "1"); return; }
    try { if (localStorage.getItem("scrapermap.skyline") === "1") setSkylineOn(true); } catch { /* storage unavailable */ }
  }, []);
  const toggleSkyline = useCallback(() => {
    const on = !skyline;
    setSkylineOn(on);
    try { localStorage.setItem("scrapermap.skyline", on ? "1" : "0"); } catch { /* storage unavailable */ }
  }, [skyline]);
  // ---- hide towers: per visit, not remembered, so the map never opens empty by surprise ----
  useEffect(() => {
    if (new URLSearchParams(location.search).get("towers") === "0") setTowersHidden(true);
  }, []);
  const toggleTowers = useCallback(() => {
    setTowersHidden(h => !h);
    setChooser(null);
  }, []);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;
    const check = () => setZoomedOut(map.getZoom() < 7);
    check();
    map.on("zoomend", check);
    return () => { map.off("zoomend", check); };
  }, [mapReady]);

  // ---- time capsule: off by default; ?year=1931 opens it at that year ----
  useEffect(() => {
    if (!range) return;
    const q = Number(new URLSearchParams(location.search).get("year"));
    if (q) setAsOf(Math.min(range.last, Math.max(range.first, Math.round(q))));
  }, [range]);
  const toggleCapsule = useCallback(() => {
    if (range) setAsOf(y => y === null ? range.last : null);
  }, [range]);
  const closeCapsule = useCallback(() => setAsOf(null), []);

  const layersAdded = useRef(false);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !idx) return;
    const data = rowsToGeoJSON(filteredRows, lost?.gone);
    if (!layersAdded.current) {
      addTowerLayers(map, data, {
        onSelect: id => select(id, false),
        onChoose: (ids, at) => setChooser({ ids, at }),
      });
      addTowerIcons(map, id => select(id, false));
      layersAdded.current = true;
      if (initialTower) { setSelected(map, initialTower.id); map.jumpTo({ center: [initialTower.lon, initialTower.lat], zoom: 15.4, padding: panelPadding() }); }
      if (pendingFit.current) { const b = pendingFit.current; map.fitBounds([[b[0], b[1]], [b[2], b[3]]], { padding: 60, duration: 0, maxZoom: 14 }); pendingFit.current = null; }
      // deep link: /?id=123
      const q = new URLSearchParams(location.search).get("id");
      if (q && !initialTower) setTimeout(() => select(Number(q)), 300);
    } else {
      setTowerData(map, data);
    }
  }, [mapReady, idx, lost, filteredRows, select, initialTower]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !layersAdded.current) return;
    setTowersVisible(map, !towersHidden);
  }, [mapReady, idx, towersHidden]);

  // skyline layers go in under the tower layers, so they wait for those; with the time capsule on they follow its year
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !layersAdded.current) return;
    setSkyline(map, skyline, basemap, asOf);
  }, [mapReady, idx, skyline, basemap, asOf]);

  // time capsule: ring the towers completed in the chosen year, and leave a ghost ring where one came down
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !layersAdded.current) return;
    setCapsuleYear(map, asOf);
  }, [mapReady, idx, asOf]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !layersAdded.current || !lost) return;
    setCapsuleLost(map, capsuleLost, lost.gone, id => lost.byId.get(id)?.how ?? "");
  }, [mapReady, idx, lost, capsuleLost]);

  // outline of the opened city / district (red dashed line); cleared when no place is open
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !layersAdded.current) return;
    setBoundary(map, null);
    if (!filters.city) return;
    let live = true;
    boundaryFor(filters.city, filters.district).then(fc => { if (live && mapRef.current) setBoundary(mapRef.current, fc); });
    return () => { live = false; };
  }, [mapReady, idx, filters.city, filters.district]);

  // keep the panel open when the selected tower is filtered out (or not yet built in the time capsule's year);
  // just leave its ring off, and put it back when the tower is shown again
  useEffect(() => {
    if (selected && idx && mapRef.current) setSelected(mapRef.current, filteredRows.some(r => r[0] === selected.id) ? selected.id : null);
  }, [filteredRows, selected, idx]);

  const chooserTowers = useMemo(() => chooser ? chooser.ids.map(resolveId).filter((t): t is Tower => !!t).sort((a, b) => b.height - a.height) : [], [chooser, resolveId]);

  // picking a tower from search (or the time capsule's tallest) brings the towers back, so the pick can be seen
  const onSearchPick = useCallback((id: number) => { setTowersHidden(false); select(id, true); }, [select]);

  const flyToPlace = useCallback((bbox: [number, number, number, number]) => {
    mapRef.current?.fitBounds([[bbox[0], bbox[1]], [bbox[2], bbox[3]]], { padding: 60, duration: 900, maxZoom: 14 });
  }, []);

  return (
    <div className={"app" + (capsuleOn ? " capsule-on" : "")}>
      <Nav active="map" />
      <div ref={mapEl} className="map" aria-label="Map of skyscrapers" />
      <div className="topbar">
        <Search idx={idx} onPick={onSearchPick} norm={norm} />
        <button className={"btn" + (filtersOpen ? " on" : "")} onClick={() => setFiltersOpen(o => !o)} aria-expanded={filtersOpen}>
          Filters{idx ? <span className="count">{filteredRows.length.toLocaleString()}</span> : null}
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
        <button className={"btn skyline" + (skyline ? " on" : "")} onClick={toggleSkyline} aria-pressed={skyline}
          title={skyline ? "Hide the skyline extents" : "Display skyline extent: wherever 5 or more towers stand close together"}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round" aria-hidden="true">
            <path d="M2 21h20M4 21V12h3V7h3v14m0-9h3V3h3v18m0-11h2V8h3v13" />
          </svg>
          <span className="sk-label sk-long">Display skyline extent</span><span className="sk-label sk-short">Skyline extent</span>
        </button>
        <button className={"btn towers" + (towersHidden ? " on" : "")} onClick={toggleTowers} aria-pressed={towersHidden}
          title={towersHidden ? "Show the towers again" : "Hide the towers: just the map and the skyline extents"}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z" /><circle cx="12" cy="12" r="3" />
            {!towersHidden && <path d="M4 4l16 16" />}
          </svg>
          <span className="tw-label">{towersHidden ? "Show towers" : "Hide towers"}</span>
        </button>
      </div>
      {skyline && zoomedOut && (
        <div className="map-hint">{asOf === null
          ? "Skyline extents are drawn wherever 5 or more towers stand close together. Zoom in on a city to see them."
          : `Skyline extents in ${asOf}: each city's core, trimmed to the towers built by then. Zoom in on a city to see it.`}</div>
      )}
      {filtersOpen && idx && (
        <Filters idx={idx} state={filters} onChange={setFilters} onClose={() => setFiltersOpen(false)} shown={filteredRows.length} onFlyTo={flyToPlace} capsule={capsuleOn} />
      )}
      <Legend skyline={skyline} capsuleYear={asOf} lostThisYear={capsuleLost.length > 0} towers={!towersHidden} />
      {idx && range && asOf === null && (
        <button className={"btn capsule-open" + (selected ? " with-panel" : "")} onClick={toggleCapsule} title={`Time capsule: show only the towers standing in a chosen year, from ${range.first} to today`}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round" strokeLinecap="round" aria-hidden="true">
            <path d="M6 3h12M6 21h12M7 3c0 4.5 5 6 5 9s-5 4.5-5 9M17 3c0 4.5-5 6-5 9s5 4.5 5 9M9.5 18.5h5" />
          </svg>
          Time capsule
        </button>
      )}
      {asOf !== null && range && (
        <TimeCapsule first={range.first} last={range.last} year={asOf} onYear={setAsOf} onClose={closeCapsule}
          perYear={capsuleCounts} shown={filteredRows.length} lost={capsuleLost.map(r => r[1])} tallest={capsuleTallest} onPick={onSearchPick} panelOpen={!!selected} />
      )}
      {chooser && chooserTowers.length > 0 && (
        <Chooser towers={chooserTowers} at={chooser.at} onPick={id => select(id, false)} onClose={() => setChooser(null)} />
      )}
      {selected && <Panel tower={selected} onClose={close} />}
      {!idx && <div className="loading">Loading {PLACES.totals.towers.toLocaleString("en-US")} towers…</div>}
    </div>
  );
}
