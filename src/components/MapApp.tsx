"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Map as MLMap } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import { towerSlug, type Tower, type TowerIndex, type TowerRow, type DetailsFile } from "@/lib/types";
import { loadIndex, loadDetails, resolveRow, norm, detailFor } from "@/lib/client";
import { createMap, addTowerLayers, rowsToGeoJSON, setTowerData, setSelected, setBasemap, setBoundary, type Basemap } from "./towerMap";
import { boundaryFor } from "@/lib/boundary";
import { setSkyline } from "./skylineLayer";
import Panel from "./Panel";
import Chooser from "./Chooser";
import Filters, { type FilterState, DEFAULT_FILTERS, applyFilters } from "./Filters";
import Search from "./Search";
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
  const [zoomedOut, setZoomedOut] = useState(true);
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
    const row = rowsById.get(id);
    if (!row) return null;
    return resolveRow(idx, row, detailFor(detailsRef.current, id, row[1]));
  }, [idx, rowsById]);

  // Once details arrive, upgrade the selected tower (unless it came pre-resolved).
  useEffect(() => {
    if (detailsReady && selected && !selected.detail?.slug) {
      const t = resolveId(selected.id); if (t) setSelectedTower(t);
    }
  }, [detailsReady, selected, resolveId]);

  // ---- filtered rows ------------------------------------------------------
  const filteredRows = useMemo(() => idx ? applyFilters(idx, filters) : [], [idx, filters]);

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
    const slug = towerSlug(t.name, id);
    if (slug) history.replaceState(null, "", `/tower/${slug}/`);
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

  // ---- skyline extent: the urban core of each city with more than 50 towers (remembered per browser; ?skyline=1 turns it on) ----
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
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;
    const check = () => setZoomedOut(map.getZoom() < 7);
    check();
    map.on("zoomend", check);
    return () => { map.off("zoomend", check); };
  }, [mapReady]);

  const layersAdded = useRef(false);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !idx) return;
    const data = rowsToGeoJSON(filteredRows);
    if (!layersAdded.current) {
      addTowerLayers(map, data, {
        onSelect: id => select(id, false),
        onChoose: (ids, at) => setChooser({ ids, at }),
      });
      layersAdded.current = true;
      if (initialTower) { setSelected(map, initialTower.id); map.jumpTo({ center: [initialTower.lon, initialTower.lat], zoom: 15.4, padding: panelPadding() }); }
      if (pendingFit.current) { const b = pendingFit.current; map.fitBounds([[b[0], b[1]], [b[2], b[3]]], { padding: 60, duration: 0, maxZoom: 14 }); pendingFit.current = null; }
      // deep link: /?id=123
      const q = new URLSearchParams(location.search).get("id");
      if (q && !initialTower) setTimeout(() => select(Number(q)), 300);
    } else {
      setTowerData(map, data);
    }
  }, [mapReady, idx, filteredRows, select, initialTower]);

  // skyline layers go in under the tower layers, so they wait for those
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !layersAdded.current) return;
    setSkyline(map, skyline, basemap);
  }, [mapReady, idx, skyline, basemap]);

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

  // keep selected tower visible even if filtered out: clear selection if it drops out
  useEffect(() => {
    if (selected && idx && !filteredRows.some(r => r[0] === selected.id)) {
      // don't auto-close; just leave the ring off
      if (mapRef.current) setSelected(mapRef.current, null);
    }
  }, [filteredRows, selected, idx]);

  const chooserTowers = useMemo(() => chooser ? chooser.ids.map(resolveId).filter((t): t is Tower => !!t).sort((a, b) => b.height - a.height) : [], [chooser, resolveId]);

  const onSearchPick = useCallback((id: number) => { select(id, true); }, [select]);

  const flyToPlace = useCallback((bbox: [number, number, number, number]) => {
    mapRef.current?.fitBounds([[bbox[0], bbox[1]], [bbox[2], bbox[3]]], { padding: 60, duration: 900, maxZoom: 14 });
  }, []);

  return (
    <div className="app">
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
          title={skyline ? "Hide the skyline extents" : "Display skyline extent: the urban core of each city with more than 50 towers"}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round" aria-hidden="true">
            <path d="M2 21h20M4 21V12h3V7h3v14m0-9h3V3h3v18m0-11h2V8h3v13" />
          </svg>
          <span className="sk-label sk-long">Display skyline extent</span><span className="sk-label sk-short">Skyline extent</span>
        </button>
      </div>
      {skyline && zoomedOut && (
        <div className="map-hint">Skyline extents are drawn for the 38 cities with more than 50 towers. Zoom in on one to see its core.</div>
      )}
      {filtersOpen && idx && (
        <Filters idx={idx} state={filters} onChange={setFilters} onClose={() => setFiltersOpen(false)} shown={filteredRows.length} onFlyTo={flyToPlace} />
      )}
      <Legend skyline={skyline} />
      {chooser && chooserTowers.length > 0 && (
        <Chooser towers={chooserTowers} at={chooser.at} onPick={id => select(id, false)} onClose={() => setChooser(null)} />
      )}
      {selected && <Panel tower={selected} onClose={close} />}
      {!idx && <div className="loading">Loading {PLACES.totals.towers.toLocaleString("en-US")} towers…</div>}
    </div>
  );
}
