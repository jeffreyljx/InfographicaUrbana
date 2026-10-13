import Nav, { type NavKey } from "./Nav";
export default function Shell({ children, active }: { children: React.ReactNode; active?: NavKey }) {
  return (
    <>
      <Nav solid active={active} />
      <main className="page">{children}</main>
      <footer className="page foot">
        Building data © <a href="https://www.skyscrapercenter.com/" target="_blank" rel="noopener">CTBUH / The Skyscraper Center</a>, used with citation.
        Coordinates partly derived from <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> (ODbL).
        Basemap by <a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenMapTiles, data from OpenStreetMap; satellite imagery © <a href="https://www.esri.com/" target="_blank" rel="noopener">Esri</a>, Maxar, Earthstar Geographics and the GIS User Community.
        Photos from Wikimedia Commons, credited individually.
      </footer>
    </>
  );
}
