"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { norm } from "@/lib/client";
import { yearsSpan, TYPE_LABEL, type HistStates } from "@/lib/history";

const fold = (s: string) => norm(s).replace(/['’`ʻʼ]/g, "").replace(/[^\p{L}\p{N}]+/gu, " ").trim();

/** Find a state by any of its names (English, native, other spellings, Cliopatria's); picking one jumps to it. */
export default function HistorySearch({ st, onPick }: { st: HistStates | null; onPick: (owner: number) => void }) {
  const [q, setQ] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const box = useRef<HTMLDivElement>(null);

  const hay = useMemo(() => {
    if (!st) return [];
    const out: { i: number; key: string; name: string; alt: string }[] = [];
    for (let k = 0; k < st.count; k++) {
      if (!st.slug[k] || st.first[k] === null) continue;   // only states drawn on the map
      out.push({ i: k + 1, key: fold([st.name[k], ...st.alt[k]].join(" | ")), name: fold(st.name[k]), alt: st.alt[k].join(" ") });
    }
    return out;
  }, [st]);

  const results = useMemo(() => {
    const n = fold(q);
    if (n.length < 2 || !st) return [];
    const terms = n.split(" ");
    const found = hay.filter(h => terms.every(t => h.key.includes(t)));
    const score = (h: (typeof hay)[number]) => (h.name === n ? 0 : h.name.startsWith(n) ? 1 : h.name.includes(n) ? 2 : 3);
    found.sort((a, b) => score(a) - score(b) || st.peak[b.i - 1] - st.peak[a.i - 1]);
    return found.slice(0, 12);
  }, [q, hay, st]);

  useEffect(() => { setActive(0); }, [q]);
  useEffect(() => {
    const h = (e: MouseEvent) => { if (box.current && !box.current.contains(e.target as Node)) setOpen(false); };
    document.addEventListener("mousedown", h); return () => document.removeEventListener("mousedown", h);
  }, []);
  const pick = (i: number) => { onPick(i); setOpen(false); setQ(""); };

  return (
    <div className="search" ref={box}>
      <input
        type="search" placeholder={st ? "Search a state, empire, dynasty or culture…" : "Loading the states…"} value={q}
        onChange={e => { setQ(e.target.value); setOpen(true); }} onFocus={() => setOpen(true)}
        onKeyDown={e => {
          if (e.key === "ArrowDown") { e.preventDefault(); setActive(a => Math.min(a + 1, results.length - 1)); }
          else if (e.key === "ArrowUp") { e.preventDefault(); setActive(a => Math.max(a - 1, 0)); }
          else if (e.key === "Enter" && results[active]) pick(results[active].i);
          else if (e.key === "Escape") setOpen(false);
        }}
        aria-label="Search states by name" disabled={!st}
      />
      {open && st && results.length > 0 && (
        <ul className="results" role="listbox">
          {results.map((r, i) => {
            const k = r.i - 1;
            return (
              <li key={r.i} role="option" aria-selected={i === active} className={i === active ? "active" : ""} onMouseDown={() => pick(r.i)}>
                <span className="rn"><i className="m-sw" style={{ background: st.colour[k] }} />{st.name[k]}</span>
                <span className="rm">{TYPE_LABEL[st.type[k]] ?? "State"} · {yearsSpan(st.first[k], st.last[k])}{r.alt ? <span className="muted"> · {r.alt.slice(0, 60)}</span> : null}</span>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
