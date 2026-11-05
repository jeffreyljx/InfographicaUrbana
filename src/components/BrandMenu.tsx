"use client";
import { useEffect, useRef, useState } from "react";
import type { NavKey } from "./Nav";
import { MODES, SITE_NAME, modeOf } from "@/lib/modes";
import { BrandMark, BrandName } from "./Logo";

/** The top left of the bar: the site's mark and name, InfographicaUrbana (to the map), then the current mode's name, with
 *  the modes in a menu below it, each with a link to its guide (a mode not open yet is greyed out and not a link). A mouse opens the menu by hovering
 *  over any of it (a click still follows the link); a first tap on a touch screen opens it, and the small arrow opens and
 *  closes it from the keyboard. Escape, or a click elsewhere, closes it. On narrow screens the name gives way to the
 *  mark (globals.css). */
export default function BrandMenu({ active }: { active?: NavKey }) {
  const mode = modeOf(active);
  const [open, setOpen] = useState(false);
  const wrap = useRef<HTMLDivElement>(null);
  const timer = useRef<number | undefined>(undefined);
  const pointer = useRef("mouse");

  const show = () => { window.clearTimeout(timer.current); setOpen(true); };
  const tapped = (e: React.PointerEvent) => { pointer.current = e.pointerType; };
  const firstTap = (e: React.MouseEvent) => { if (pointer.current !== "mouse" && !open) { e.preventDefault(); show(); } };
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
      <a className="brand" href="/" aria-label={`${SITE_NAME} home`} onPointerDown={tapped} onClick={firstTap}>
        <BrandMark /><BrandName />
      </a>
      <a className="brand-mode" href={mode.href} aria-label={`${mode.name} home`} onPointerDown={tapped} onClick={firstTap}>{mode.name}</a>
      <button type="button" className="brand-caret" aria-expanded={open} aria-controls="site-modes" aria-label="Switch mode"
        onClick={() => (open ? hide(0) : show())}>
        <svg width="10" height="6" viewBox="0 0 10 6" aria-hidden="true"><path d="M0 0h10L5 6z" /></svg>
      </button>
      <div className="brand-drop" id="site-modes">
        <ul>
          {MODES.map(m => (
            <li key={m.key}>
              {m.soon ? (
                <span className="soon" aria-disabled="true"><span>{m.name}</span><small>{m.blurb}</small></span>
              ) : (
                <>
                  <a href={m.href} aria-current={m.key === mode.key ? "true" : undefined} tabIndex={open ? undefined : -1}>
                    <span>{m.name}</span><small>{m.blurb}</small>
                  </a>
                  <a className="mode-guide" href={m.guide} tabIndex={open ? undefined : -1} aria-label={`${m.name} guide`}>Guide</a>
                </>
              )}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
