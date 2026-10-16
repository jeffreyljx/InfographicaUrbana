"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { norm } from "@/lib/client";
import type { MetroData } from "@/lib/metro";
import type { MetroPick } from "./MetroPanel";

type Hit = { pick: MetroPick; title: string; sub: string; colour?: string; key: string; rank: number };
/** Search form of a name: no accents or case, apostrophes dropped and other punctuation as spaces ("King's Cross St. Pancras" → "kings cross st pancras"). */
const fold = (s: string) => norm(s).replace(/['’`]/g, "").replace(/[^\p{L}\p{N}]+/gu, " ").trim();

/** Search the metro map: cities and systems, lines, and stations (by their English or local name). */
export default function MetroSearch({ data, onPick }: { data: MetroData | null; onPick: (p: MetroPick) => void }) {
  const [q, setQ] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const box = useRef<HTMLDivElement>(null);

  const hay = useMemo<Hit[]>(() => {
    if (!data) return [];
    const out: Hit[] = [];
    for (const s of data.systems) out.push({ pick: { kind: "system", i: s.i }, title: s.name, sub: `${s.city}, ${s.country}`, key: fold(`${s.name} ${s.city} ${s.country}`), rank: 0 });
    for (const l of data.lines) {
      const s = data.systems[l.sys];
      out.push({ pick: { kind: "line", i: l.i }, title: l.name, sub: `${s.city} · ${s.name}`, colour: l.colour, key: fold(`${l.name} ${l.local} ${s.city} ${s.name}`), rank: 1 });
    }
    for (const st of data.stations) {
      const s = data.systems[st.sys];
      out.push({ pick: { kind: "station", i: st.i }, title: st.en || st.name, sub: `${st.en && st.en !== st.name ? st.name + " · " : ""}${s.city}`, colour: data.lines[st.lines[0][0]].colour, key: fold(`${st.en} ${st.name} ${s.city}`), rank: 2 });
    }
    return out;
  }, [data]);

  const results = useMemo(() => {
    const n = fold(q);
    if (n.length < 2 || !hay.length) return [];
    const terms = n.split(" ");
    const found = hay.filter(h => terms.every(t => h.key.includes(t)));
    found.sort((a, b) => {
      const ap = fold(a.title).startsWith(n) ? 0 : 1, bp = fold(b.title).startsWith(n) ? 0 : 1;
      return ap - bp || a.rank - b.rank || a.title.length - b.title.length;
    });
    return found.slice(0, 12);
  }, [q, hay]);

  useEffect(() => { setActive(0); }, [q]);
  useEffect(() => {
    const h = (e: MouseEvent) => { if (box.current && !box.current.contains(e.target as Node)) setOpen(false); };
    document.addEventListener("mousedown", h); return () => document.removeEventListener("mousedown", h);
  }, []);
  const pick = (h: Hit) => { onPick(h.pick); setOpen(false); setQ(""); };
  const KIND = { system: "System", line: "Line", station: "Station" } as const;

  return (
    <div className="search" ref={box}>
      <input
        type="search" placeholder={data ? "Search a city, line or station…" : "Loading the metro map…"} value={q}
        onChange={e => { setQ(e.target.value); setOpen(true); }} onFocus={() => setOpen(true)}
        onKeyDown={e => {
          if (e.key === "ArrowDown") { e.preventDefault(); setActive(a => Math.min(a + 1, results.length - 1)); }
          else if (e.key === "ArrowUp") { e.preventDefault(); setActive(a => Math.max(a - 1, 0)); }
          else if (e.key === "Enter" && results[active]) pick(results[active]);
          else if (e.key === "Escape") setOpen(false);
        }}
        aria-label="Search metro systems, lines and stations" disabled={!data}
      />
      {open && results.length > 0 && (
        <ul className="results" role="listbox">
          {results.map((r, i) => (
            <li key={`${r.pick.kind}${r.pick.i}`} role="option" aria-selected={i === active} className={i === active ? "active" : ""} onMouseDown={() => pick(r)}>
              <span className="rn">{r.colour && <i className="m-sw" style={{ background: r.colour }} />}{r.title}</span>
              <span className="rm">{KIND[r.pick.kind]} · <span className="place">{r.sub}</span></span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
