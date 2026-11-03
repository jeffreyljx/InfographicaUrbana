"use client";
import { useEffect, useState } from "react";
import { THRESHOLDS, type Threshold } from "@/lib/types";

/** Height-threshold switch (150 / 200 / 300 m) shared by the Countries and Cities tables.
 *  The choice is mirrored into ?min= so a view can be linked; 150 m is the default and leaves the URL clean. */
export function useThreshold(): [Threshold, (m: Threshold) => void] {
  const [min, setMin] = useState<Threshold>(150);
  useEffect(() => {
    const m = Number(new URLSearchParams(location.search).get("min"));
    if (m === 200 || m === 300) setMin(m);
  }, []);
  const pick = (m: Threshold) => {
    setMin(m);
    const u = new URL(location.href);
    if (m === 150) u.searchParams.delete("min"); else u.searchParams.set("min", String(m));
    history.replaceState(null, "", u.toString());
  };
  return [min, pick];
}

export function ThresholdSwitch({ min, pick, label }: { min: Threshold; pick: (m: Threshold) => void; label: string }) {
  return (
    <div className="threshold" role="group" aria-label="Minimum height">
      <span className="lbl" style={{ margin: 0 }}>{label}</span>
      <div className="chips">
        {THRESHOLDS.map(m => (
          <button key={m} type="button" className={"chip" + (m === min ? " on" : "")} aria-pressed={m === min} onClick={() => pick(m)}>{m} m</button>
        ))}
      </div>
    </div>
  );
}
