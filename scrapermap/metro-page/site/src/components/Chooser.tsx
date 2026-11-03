"use client";
import { useEffect, useRef } from "react";
import type { Tower } from "@/lib/types";
import { fmtHeight } from "@/lib/format";

interface Props { towers: Tower[]; at: { x: number; y: number }; onPick: (id: number) => void; onClose: () => void }

/** Dropdown for pins where several towers share one coordinate. */
export default function Chooser({ towers, at, onPick, onClose }: Props) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const h = (e: MouseEvent) => { if (ref.current && !ref.current.contains(e.target as Node)) onClose(); };
    const k = (e: KeyboardEvent) => { if (e.key === "Escape") onClose(); };
    setTimeout(() => document.addEventListener("mousedown", h), 0);
    document.addEventListener("keydown", k);
    return () => { document.removeEventListener("mousedown", h); document.removeEventListener("keydown", k); };
  }, [onClose]);
  // keep inside the viewport
  const w = 300, h = Math.min(56 + towers.length * 44, 360);
  const left = Math.min(Math.max(8, at.x - w / 2), (typeof window !== "undefined" ? window.innerWidth : 1000) - w - 8);
  const top = at.y + 14 + h > (typeof window !== "undefined" ? window.innerHeight : 800) ? at.y - h - 14 : at.y + 14;
  return (
    <div className="chooser" ref={ref} style={{ left, top, width: w }} role="menu">
      <div className="ch-head">{towers.length} towers at this point</div>
      <ul>
        {towers.map(t => (
          <li key={t.id}><button role="menuitem" onClick={() => onPick(t.id)}>
            <span className="rn">{t.name}</span>
            <span className="rm">{fmtHeight(t.height)} · {t.floors} fl{t.year ? ` · ${t.year}` : ""}</span>
          </button></li>
        ))}
      </ul>
    </div>
  );
}
