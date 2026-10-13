import type { Metadata } from "next";
import Shell from "@/components/Shell";
import CountriesTable, { type CountryRow, type TopCity } from "@/components/CountriesTable";
import { getPlaces } from "@/lib/data";
import { gdpOfCountry } from "@/lib/gdp";
import { countryGroup } from "@/lib/countryLabels";
import { countsAt, type CityAgg, type Threshold } from "@/lib/types";
export const metadata: Metadata = { title: "Countries", description: `${getPlaces().totals.countries} countries ranked by completed skyscrapers — switch the height threshold between 150 m, 200 m and 300 m.` };

function countries(cities: CityAgg[]): CountryRow[] {
  const by = new Map<string, CityAgg[]>();
  // a country counted under another row (Taiwan under China) is grouped with it; see scripts/country-labels.json
  for (const c of cities) { const g = countryGroup(c.country); by.set(g, [...(by.get(g) ?? []), c]); }
  const sum = (cs: CityAgg[], f: (c: CityAgg) => number) => cs.reduce((s, c) => s + f(c), 0);
  const top = (cs: CityAgg[], m: Threshold): TopCity | null => {
    const best = cs.map(c => ({ c, n: countsAt(c, m).completed })).filter(x => x.n > 0)
      .sort((a, b) => b.n - a.n || a.c.name.localeCompare(b.c.name))[0];
    return best ? { name: best.c.name, slug: best.c.slug, completed: best.n } : null;
  };
  return [...by].map(([name, cs]) => {
    // a city's tallest is its tallest completed building when it has one; use those first
    const pool = cs.some(c => c.completed > 0) ? cs.filter(c => c.completed > 0) : cs;
    const t = pool.reduce((a, b) => (b.tallest_h > a.tallest_h ? b : a));
    return {
      name,
      completed: sum(cs, c => c.completed), count: sum(cs, c => c.count),
      completed200: sum(cs, c => c.completed200), count200: sum(cs, c => c.count200),
      completed300: sum(cs, c => c.completed300), count300: sum(cs, c => c.count300),
      cities: cs.length, cities200: cs.filter(c => c.count200 > 0).length, cities300: cs.filter(c => c.count300 > 0).length,
      districts: sum(cs, c => c.districts), districts200: sum(cs, c => c.districts200), districts300: sum(cs, c => c.districts300),
      top: { 150: top(cs, 150), 200: top(cs, 200), 300: top(cs, 300) },
      tallest_name: t.tallest_name, tallest_h: t.tallest_h, tallest_city: t.name, tallest_slug: t.slug,
      gdp: gdpOfCountry(name),
    };
  });
}

export default function CountriesPage() {
  const { cities, totals } = getPlaces();
  return (
    <Shell active="countries">
      <h1>Countries</h1>
      <p className="lead">{totals.countries} countries and territories, {totals.cities} cities, {totals.towers.toLocaleString()} towers. Ranked by completed buildings at the height you choose; the default is 150 m, the usual definition of a skyscraper.</p>
      <CountriesTable countries={countries(cities)} />
    </Shell>
  );
}
