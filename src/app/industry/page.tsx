import type { Metadata } from "next";
import IndustryApp from "@/components/IndustryApp";
import { industryMapData } from "@/lib/industry";

export const metadata: Metadata = {
  title: "IndustryMap",   // its own mode, so "IndustryMap · InfographicaUrbana"
  description: "A map of which cities and countries trade and make the most: goods exports and imports and manufacturing value added, each place a circle to scale, with every figure's source.",
};

/** IndustryMap's home: the map. The figures behind it are on /industry/trade/ and /industry/output/. */
export default function IndustryMapPage() {
  return <IndustryApp data={industryMapData()} />;
}
