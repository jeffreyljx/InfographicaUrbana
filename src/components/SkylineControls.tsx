"use client";
import { useEffect, useState } from "react";

export type SkylineSortKey = "area" | "towers" | "tallest" | "city";
const SORTS: [SkylineSortKey, string][] = [["area", "Area"], ["towers", "Towers"], ["tallest", "Tallest"], ["city", "City"]];
/** zoom factor over Fit (the widest city fills the column), and the scale bar's length in km at that zoom */
const ZOOMS: [number, string, number][] = [[1, "Fit", 10], [2, "2×", 5], [4, "4×", 2], [8, "8×", 1]];

/** Sort and zoom switches for the skylines page. Each drawing carries its position under every sort as a CSS variable and
 *  its size in km, so these only flip data-sort and --zoom on the wrapper; the choices are mirrored into ?sort= and ?zoom=
 *  (the defaults leave the URL clean). */
export default function SkylineControls() {
  const [sort, setSort] = useState<SkylineSortKey>("area");
  const [zoom, setZoom] = useState(1);
  useEffect(() => {
    const q = new URLSearchParams(location.search);
    const s = q.get("sort") as SkylineSortKey | null, z = Number(q.get("zoom"));
    if (s && SORTS.some(([k]) => k === s)) setSort(s);
    if (ZOOMS.some(([k]) => k === z)) setZoom(z);
  }, []);
  useEffect(() => {
    const wrap = document.getElementById("skygrid");
    const bar = ZOOMS.find(([k]) => k === zoom)![2];
    if (wrap) {
      wrap.dataset.sort = sort;
      wrap.style.setProperty("--zoom", String(zoom));
      wrap.style.setProperty("--bar", String(bar));
    }
    const label = document.getElementById("skyscale-label");
    if (label) label.textContent = `${bar} km`;
    const url = new URL(location.href);
    if (sort === "area") url.searchParams.delete("sort"); else url.searchParams.set("sort", sort);
    if (zoom === 1) url.searchParams.delete("zoom"); else url.searchParams.set("zoom", String(zoom));
    history.replaceState(null, "", url);
  }, [sort, zoom]);
  return (
    <div className="skyctl">
      <div className="threshold skysort" role="group" aria-label="Sort cities by">
        <span className="lbl" style={{ margin: 0 }}>Sort by</span>
        <div className="chips">
          {SORTS.map(([k, label]) => (
            <button key={k} type="button" className={"chip" + (k === sort ? " on" : "")} aria-pressed={k === sort} onClick={() => setSort(k)}>{label}</button>
          ))}
        </div>
      </div>
      <div className="threshold skysort" role="group" aria-label="Zoom">
        <span className="lbl" style={{ margin: 0 }}>Zoom</span>
        <div className="chips">
          {ZOOMS.map(([k, label]) => (
            <button key={k} type="button" className={"chip" + (k === zoom ? " on" : "")} aria-pressed={k === zoom} onClick={() => setZoom(k)}>{label}</button>
          ))}
        </div>
      </div>
    </div>
  );
}
