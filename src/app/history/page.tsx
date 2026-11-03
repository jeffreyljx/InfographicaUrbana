import type { Metadata } from "next";
import HistoryApp from "@/components/HistoryApp";
import { historyStates } from "@/lib/historyServer";

const COUNT = (() => { try { return historyStates().slug.filter(Boolean).length; } catch { return 0; } })();

export const metadata: Metadata = {
  title: "CartaHistoria · Every state's borders since 6000 BCE",   // its own mode, so "CartaHistoria · … · InfographicaUrbana"
  description: `Every state's borders on one map, year by year from 6000 BCE to 2026${COUNT ? `: ${COUNT.toLocaleString("en-US")} states, empires, dynasties and cultures` : ""}, with vassals, occupations and contested land, and a page for every state. Borders from Cliopatria (Seshat, CC BY 4.0), corrected from Wikipedia.`,
  alternates: { canonical: "/history/" },
};

export default function HistoryPage() {
  return <HistoryApp />;
}
