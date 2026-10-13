import type { Metadata } from "next";
import Shell from "@/components/Shell";
import CitiesTable from "@/components/CitiesTable";
import { getPlaces } from "@/lib/data";
import { gdpOfCity } from "@/lib/gdp";
export const metadata: Metadata = { title: "Cities", description: `${getPlaces().totals.cities} cities ranked by completed skyscrapers — switch the height threshold between 150 m, 200 m and 300 m.` };

export default function CitiesPage() {
  const { cities, totals } = getPlaces();
  return (
    <Shell active="cities">
      <h1>Cities</h1>
      <p className="lead">{totals.cities} cities, {totals.districts} districts, {totals.towers.toLocaleString()} towers. Ranked by completed buildings at the height you choose; the default is 150 m, the usual definition of a skyscraper.</p>
      <CitiesTable cities={cities} gdp={Object.fromEntries(cities.map(c => [c.slug, gdpOfCity(c.name)]))} />
    </Shell>
  );
}
