"use client";
import { useEffect, useRef, useState } from "react";
import type { NavKey } from "./Nav";

/** Every page of the site, listed in the menu that drops down from the ScraperMap name. */
const PAGES: [NavKey, string, string, string][] = [
  ["map", "/", "Map", "Every skyscraper of 150 m+ on the map"],
  ["countries", "/countries/", "Countries", "Countries ranked by their towers"],
  ["cities", "/cities/", "Cities", "Cities ranked by their towers"],
  ["districts", "/districts/", "Districts", "Districts ranked by their towers"],
  ["skylines", "/skylines/", "Skylines", "Every city's skyline at one scale"],
  ["industry", "/industry/", "Industry and Exports", "Which cities trade and make the most"],
  ["method", "/method/", "Method", "How the map was made"],
];

/** The ScraperMap name in the top bar, with the site's pages in a menu below it. A mouse opens the menu by hovering
 *  over the name (a click still goes to the map); a first tap on a touch screen opens it, and the small arrow opens and
 *  closes it from the keyboard. Escape, or a click elsewhere, closes it. */
export default function BrandMenu({ active }: { active?: NavKey }) {
  const [open, setOpen] = useState(false);
  const wrap = useRef<HTMLDivElement>(null);
  const timer = useRef<number | undefined>(undefined);
  const pointer = useRef("mouse");

  const show = () => { window.clearTimeout(timer.current); setOpen(true); };
  const hide = (delay: number) => { window.clearTimeout(timer.current); timer.current = window.setTimeout(() => setOpen(false), delay); };

  useEffect(() => {
    if (!open) return;
    const away = (e: PointerEvent) => { if (!wrap.current?.contains(e.target as Node)) setOpen(false); };
    const key = (e: KeyboardEvent) => {
      if (e.key !== "Escape") return;
      setOpen(false);
      wrap.current?.querySelector<HTMLElement>(".brand-caret")?.focus();
    };
    document.addEventListener("pointerdown", away);
    document.addEventListener("keydown", key);
    return () => { document.removeEventListener("pointerdown", away); document.removeEventListener("keydown", key); };
  }, [open]);
  useEffect(() => () => window.clearTimeout(timer.current), []);

  return (
    <div ref={wrap} className={"brandmenu" + (open ? " open" : "")}
      onPointerEnter={e => { pointer.current = e.pointerType; if (e.pointerType === "mouse") show(); }}
      onPointerLeave={e => { if (e.pointerType === "mouse") hide(220); }}
      onBlur={e => { if (!wrap.current?.contains(e.relatedTarget as Node)) hide(0); }}>
      <a className="brand" href="/" aria-label="ScraperMap home"
        onPointerDown={e => { pointer.current = e.pointerType; }}
        onClick={e => { if (pointer.current !== "mouse" && !open) { e.preventDefault(); show(); } }}>
        <span className="mark">▲</span><span className="brand-name">ScraperMap</span>
      </a>
      <button type="button" className="brand-caret" aria-expanded={open} aria-controls="site-pages" aria-label="Site pages"
        onClick={() => (open ? hide(0) : show())}>
        <svg width="10" height="6" viewBox="0 0 10 6" aria-hidden="true"><path d="M0 0h10L5 6z" /></svg>
      </button>
      <div className="brand-drop" id="site-pages">
        <ul>
          {PAGES.map(([k, href, label, blurb]) => (
            <li key={k}>
              <a href={href} aria-current={k === active ? "page" : undefined} tabIndex={open ? undefined : -1}>
                <span>{label}</span><small>{blurb}</small>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
