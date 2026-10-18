import type { Metadata } from "next";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import MetroApp from "@/components/MetroApp";

// the counts for the description, read from the packed data the page loads (public/metro/metro.json)
const META = (() => {
  try {
    const j = JSON.parse(readFileSync(join(process.cwd(), "public/metro/metro.json"), "utf8")) as { systems: unknown[]; lines: unknown[]; stations: { lon: unknown[] } };
    return { systems: j.systems.length, lines: j.lines.length, stations: j.stations.lon.length };
  } catch { return null; }
})();

export const metadata: Metadata = {
  title: { absolute: "TransitMap · Metro history" },   // its own mode, so not "· ScraperMap"
  description: META
    ? `How the world's metro systems grew: ${META.systems} systems, ${META.lines} lines and ${META.stations.toLocaleString("en-US")} stations on one map, each stretch of line drawn from the year it opened, with a page for every station and line.`
    : "How the world's metro systems grew, each stretch of line drawn from the year it opened.",
};

export default function MetroPage() {
  return <MetroApp />;
}
