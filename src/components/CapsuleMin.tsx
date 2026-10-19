"use client";
import { useEffect, useState } from "react";

/**
 * Collapsing the time capsule (ScraperMap) or the year dock (TransitMap) into a short bar, so that dragging the map
 * can't catch the slider. With a storage key the choice is remembered in this browser.
 */
export function useCapsuleMin(storageKey?: string): [boolean, (min: boolean) => void] {
  const [min, setMinState] = useState(false);
  useEffect(() => {
    if (!storageKey) return;
    try { if (localStorage.getItem(storageKey) === "min") setMinState(true); } catch { /* storage unavailable */ }
  }, [storageKey]);
  const setMin = (v: boolean) => {
    setMinState(v);
    if (storageKey) try { localStorage.setItem(storageKey, v ? "min" : "open"); } catch { /* storage unavailable */ }
  };
  return [min, setMin];
}

/** The dock's top-right button: a bar to collapse it, a chevron to open it again. */
export default function CapsuleMin({ min, onToggle, what }: { min: boolean; onToggle: () => void; what: string }) {
  const label = min ? `Expand the ${what}` : `Collapse the ${what}`;
  return (
    <button className="x cap-min" onClick={onToggle} aria-label={label} title={label} aria-expanded={!min}>
      <svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true">
        {min
          ? <path d="M3 8.8 7 4.8l4 4" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
          : <path d="M3 7h8" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />}
      </svg>
    </button>
  );
}
