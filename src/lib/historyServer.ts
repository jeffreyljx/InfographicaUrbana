import "server-only";
import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import type { HistStates } from "./history";
import type { StateFile } from "@/components/HistoryPanel";

/** CartaHistoria's packed data as the build reads it (public/history/, written by scripts/history/pack.py). */
const DIR = join(process.cwd(), "public", "history");
let states: HistStates | null = null;

export function historyStates(): HistStates {
  return (states ??= JSON.parse(readFileSync(join(DIR, "states.json"), "utf8")) as HistStates);
}
/** every state with a record, for the static pages */
export function historySlugs(): string[] {
  try {
    return readdirSync(join(DIR, "state")).filter(f => f.endsWith(".json")).map(f => f.slice(0, -5)).sort();
  } catch { return []; }
}
export function historyState(slug: string): StateFile | null {
  try { return JSON.parse(readFileSync(join(DIR, "state", `${slug}.json`), "utf8")) as StateFile; } catch { return null; }
}
export function historyIndexBuilt(): { built: string; drafts: number } {
  try {
    const j = JSON.parse(readFileSync(join(DIR, "index.json"), "utf8")) as { built: string; windows: { src: string }[] };
    return { built: j.built, drafts: j.windows.filter(w => w.src === "draft").length };
  } catch { return { built: "", drafts: 0 }; }
}
