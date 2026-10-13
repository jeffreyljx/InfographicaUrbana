"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import type { TowerIndex } from "@/lib/types";

interface Props { idx: TowerIndex | null; onPick: (id: number) => void; norm: (s: string) => string }

export default function Search({ idx, onPick, norm }: Props) {
  const [q, setQ] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const box = useRef<HTMLDivElement>(null);

  const hay = useMemo(() => idx ? idx.rows.map(r => ({ id: r[0], name: r[1], h: r[4], city: idx.cities[r[5]], district: idx.districts[r[6]][1], key: norm(r[1] + " " + idx.cities[r[5]] + " " + idx.districts[r[6]][1]) })) : [], [idx, norm]);

  const results = useMemo(() => {
    const n = norm(q.trim());
    if (n.length < 2 || !hay.length) return [];
    const terms = n.split(/\s+/);
    const out: typeof hay = [];
    for (const t of hay) {
      if (terms.every(term => t.key.includes(term))) out.push(t);
    }
    // prefer name-prefix matches, then taller
    out.sort((a, b) => {
      const ap = norm(a.name).startsWith(n) ? 0 : 1, bp = norm(b.name).startsWith(n) ? 0 : 1;
      return ap - bp || b.h - a.h;
    });
    return out.slice(0, 10);
  }, [q, hay, norm]);

  useEffect(() => { setActive(0); }, [q]);
  useEffect(() => {
    const h = (e: MouseEvent) => { if (box.current && !box.current.contains(e.target as Node)) setOpen(false); };
    document.addEventListener("mousedown", h); return () => document.removeEventListener("mousedown", h);
  }, []);

  const pick = (id: number) => { onPick(id); setOpen(false); setQ(""); };

  return (
    <div className="search" ref={box}>
      <input
        type="search" placeholder={idx ? `Search ${idx.rows.length.toLocaleString("en-US")} towers, cities, districts…` : "Loading…"} value={q}
        onChange={e => { setQ(e.target.value); setOpen(true); }} onFocus={() => setOpen(true)}
        onKeyDown={e => {
          if (e.key === "ArrowDown") { e.preventDefault(); setActive(a => Math.min(a + 1, results.length - 1)); }
          else if (e.key === "ArrowUp") { e.preventDefault(); setActive(a => Math.max(a - 1, 0)); }
          else if (e.key === "Enter" && results[active]) pick(results[active].id);
          else if (e.key === "Escape") setOpen(false);
        }}
        aria-label="Search towers" disabled={!idx}
      />
      {open && results.length > 0 && (
        <ul className="results" role="listbox">
          {results.map((r, i) => (
            <li key={r.id} role="option" aria-selected={i === active} className={i === active ? "active" : ""} onMouseDown={() => pick(r.id)}>
              <span className="rn">{r.name}</span>
              <span className="rm"><span className="place">{r.city}</span> · <span className="place">{r.district}</span> · {r.h}{"\u00a0"}m</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
