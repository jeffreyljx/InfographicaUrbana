import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Shell from "@/components/Shell";
import TowerTable from "@/components/TowerTable";
import DistrictsTable from "@/components/DistrictsTable";
import { getPlaces, towersInCity } from "@/lib/data";

export const dynamicParams = false;
export function generateStaticParams() { return getPlaces().cities.map(c => ({ city: c.slug })); }
export async function generateMetadata({ params }: { params: Promise<{ city: string }> }): Promise<Metadata> {
  const { city } = await params; const c = getPlaces().cities.find(x => x.slug === city);
  return c ? { title: `${c.name} skyscrapers`, description: `${c.completed} completed skyscrapers of 150 m+ in ${c.name}, by district, each on the map.` } : {};
}

export default async function CityPage({ params }: { params: Promise<{ city: string }> }) {
  const { city } = await params;
  const places = getPlaces();
  const c = places.cities.find(x => x.slug === city);
  if (!c) notFound();
  const districts = places.districts.filter(d => d.city === c.name);
  const towers = towersInCity(c.name).sort((a, b) => b.height - a.height);
  return (
    <Shell active="cities">
      <div className="crumbs"><a href="/cities/">Cities</a> › <span className="place">{c.name}</span></div>
      <h1>{c.name}</h1>
      <p className="lead">#{c.rank} in the world with {c.completed} completed skyscrapers of 150 m and taller, {c.count - c.completed} more in the pipeline, across {districts.length} districts. Tallest: {c.tallest_name}, {c.tallest_h}{"\u00a0"}m.</p>
      <p className="muted">
        {c.completed200
          ? <>{c.completed200} completed at 200 m+ (<a href="/cities/?min=200">#{c.rank200} in the world</a>){c.count200 > c.completed200 ? `, ${c.count200 - c.completed200} more in the pipeline` : ""}.</>
          : c.count200 ? <>No completed 200 m+ building yet; {c.count200} in the pipeline.</> : <>No building of 200 m or taller.</>}{" "}
        {c.completed300
          ? <>{c.completed300} completed at 300 m+ (<a href="/cities/?min=300">#{c.rank300}</a>){c.count300 > c.completed300 ? `, ${c.count300 - c.completed300} more in the pipeline` : ""}.</>
          : c.count300 ? <>No completed 300 m+ building yet; {c.count300} in the pipeline.</> : <>No building of 300 m or taller.</>}
      </p>
      <div className="heroactions"><a className="btn primary" href={`/?city=${encodeURIComponent(c.name)}`}>Open {c.name} on the map</a></div>
      <h2>Districts</h2>
      <DistrictsTable showCity={false} rankLabel="World #" rows={districts.map(d => ({
        rank: d.rank, name: d.name, slug: d.slug, city: d.city, city_slug: d.city_slug, completed: d.completed,
        pipeline: d.count - d.completed, supertall: d.supertall, tallest_name: d.tallest_name, tallest_h: d.tallest_h,
      }))} />
      <h2>All {towers.length} towers</h2>
      <TowerTable towers={towers} />
    </Shell>
  );
}
