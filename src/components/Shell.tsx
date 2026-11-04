import Nav, { type NavKey } from "./Nav";
/** A page of text under the top bar. The footer credits ScraperMap's sources unless the page gives its own (`foot`). */
export default function Shell({ children, active, foot }: { children: React.ReactNode; active?: NavKey; foot?: React.ReactNode }) {
  return (
    <>
      <Nav solid active={active} />
      <main className="page">{children}</main>
      <footer className="page foot">
        {foot ?? <>
          Building data © <a href="https://www.skyscrapercenter.com/" target="_blank" rel="noopener">CTBUH / The Skyscraper Center</a>, used with citation.
          Coordinates partly derived from <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> (ODbL).
          Basemap by <a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenMapTiles, data from OpenStreetMap; satellite imagery © <a href="https://www.esri.com/" target="_blank" rel="noopener">Esri</a>, Maxar, Earthstar Geographics and the GIS User Community.
          Metro footprints derived from <a href="https://esa-worldcover.org/" target="_blank" rel="noopener">ESA WorldCover</a> 2021 (© ESA WorldCover project, CC BY 4.0).
          Photos from Wikimedia Commons, credited individually.
        </>}
      </footer>
    </>
  );
}
