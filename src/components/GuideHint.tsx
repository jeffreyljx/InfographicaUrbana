"use client";
import { useEffect, useState } from "react";
import { modeByKey, type Mode } from "@/lib/modes";

/**
 * A small note on a mode's map, pointing a first-time visitor to the mode's guide (Jeffrey, 4 Nov 2026). It shows once
 * per mode in a browser, a moment after the map opens, and never on a link to a particular view (a URL with a query or a
 * tower's page), where the visitor came for something already. Following it or closing it stops it for good.
 */
export default function GuideHint({ mode, skip = false }: { mode: Mode; skip?: boolean }) {
  const m = modeByKey(mode);
  const key = `infographica.guide-seen.${mode}`;
  const [show, setShow] = useState(false);
  useEffect(() => {
    if (skip || location.search) return;
    try { if (localStorage.getItem(key)) return; } catch { return; }
    const t = setTimeout(() => setShow(true), 1500);
    return () => clearTimeout(t);
  }, [key, skip]);
  const seen = () => { setShow(false); try { localStorage.setItem(key, "1"); } catch { /* storage unavailable */ } };
  if (!show) return null;
  return (
    <div className="guide-hint" role="note">
      <a href={m.guide} onClick={seen}>New to {m.name}? <b>See what it shows and how to use it</b></a>
      <button className="x" onClick={seen} aria-label="Dismiss">×</button>
    </div>
  );
}
