import type { Metadata } from "next";
import Shell from "@/components/Shell";
import DistrictsTable, { type DistrictRow } from "@/components/DistrictsTable";
import { getPlaces } from "@/lib/data";
export const metadata: Metadata = { title: "Districts", description: "The world's urban districts, boroughs and wards ranked by completed skyscrapers of 150 m and taller — a building-by-building count." };

export default function DistrictsPage() {
  const { districts, totals } = getPlaces();
  const top = districts.filter(d => d.completed >= 5);
  // only the fields the table shows go to the client
  const rows: DistrictRow[] = top.map(d => ({
    rank: d.rank, name: d.name, slug: d.slug, city: d.city, city_slug: d.city_slug, completed: d.completed,
    pipeline: d.count - d.completed, supertall: d.supertall, tallest_name: d.tallest_name, tallest_h: d.tallest_h,
  }));
  return (
    <Shell active="districts">
      <h1>Districts with the most skyscrapers</h1>
      <p className="lead">Every district, borough or ward with at least five completed buildings of 150 m or taller — {top.length} of {totals.districts.toLocaleString()} units across {totals.cities} cities. Each tower was placed individually and assigned by point-in-polygon against administrative boundaries; the count is what is standing today, not what is planned.</p>
      <div className="kpis">
        <div className="kpi"><b>{totals.completed.toLocaleString()}</b><span>completed towers</span></div>
        <div className="kpi"><b>{totals.districts.toLocaleString()}</b><span>districts</span></div>
        <div className="kpi"><b>{totals.supertall}</b><span>300 m and taller</span></div>
        <div className="kpi"><b>{totals.countries}</b><span>countries</span></div>
      </div>
      <DistrictsTable rows={rows} />
      <p className="muted" style={{ marginTop: 18 }}>Pipeline = under construction or topped out. Cities without a formal district tier (Dubai, Doha, Kuala Lumpur, Miami) use their commonly-used neighbourhood names. New York City is counted by borough; Manhattan is one unit. Click a column&apos;s ▼ to sort by it, most first; click again for least first — the # column keeps each district&apos;s rank by completed towers.</p>
    </Shell>
  );
}
