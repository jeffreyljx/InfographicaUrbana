#!/usr/bin/env python3
"""Gazetteer resolver for EmpireMap: a region named in words -> H3 resolution-5 land cells.

Library:
    from gazetteer import Gazetteer, GazetteerError
    g = Gazetteer()
    cells = g.resolve({"region": "Khorasan"})          # set of int indices into data/grid/land_r5.txt
    h3s   = g.to_h3(cells)                              # the same as H3 cell strings
    g.trace                                             # what the last resolve matched, one line per name

Command line (run from a scratch directory):
    python3 -I tools/gazetteer.py resolve '<json spec>'    cell count, bbox and the names matched
    python3 -I tools/gazetteer.py resolve '<json spec>' --cells   also print the cell indices (runs)
    python3 -I tools/gazetteer.py check --counts                 also print every region's cell count and bbox
    python3 -I tools/gazetteer.py check                    resolve every entry of regions.jsonl, list failures
    python3 -I tools/gazetteer.py names <text>             search every name list for a string

The region spec grammar (shared with the dossier schema and the briefs). A spec is one of
    {"country": name}
    {"admin1": name, "country": name}        name may also be a Natural Earth "region" value
                                             (an Italian region, a Latvian planning region, ...)
    {"place": name, "km": radius}            optional "country" when the name is ambiguous
    {"lon": x, "lat": y, "km": r}
    {"cliopatria": Name, "year": y}          that polity's Cliopatria shape in that year (tools/grid.py)
    {"region": historical-region-name}       an entry of data/gazetteer/regions.jsonl
    {"polygon": [[lon, lat], ...]}           at most 12 points; fallback only
    {"border_band": {"a": slug, "b": slug, "year": y, "width": cells}}
    {"union": [...]}, {"minus": [A, B]}, {"intersect": [...]}
plus two gazetteer extensions:
    {"river": name, "km": r}                 the cells a river passes through, widened by r km (r may be 0)
    {"lake": name}                           the cells of a lake (lakes are land cells in this grid)
Any spec may carry "text" (the source's own words), which is ignored here.

Names are matched ignoring case, diacritics, hyphens and apostrophes, against the name and the
alt_names of every entry. An unknown name raises GazetteerError listing the closest matches.
Country and admin-1 spellings follow Natural Earth 10m (data/gazetteer/README.md).
"""
import difflib
import json
import math
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import h3

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

HIST = HERE.parent
DATA = HIST / "data" / "gazetteer"
GRID_FILE = HIST / "data" / "grid" / "land_r5.txt"
ANCHOR_DIR = HIST / "data" / "anchors"
RES = 5
MAX_POLYGON_POINTS = 12


class GazetteerError(ValueError):
    """A name that cannot be resolved, or a malformed spec."""


# ----------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------

def norm(s):
    """Normalised key: NFKD, no combining marks, lower case, no hyphens or apostrophes, single spaces."""
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("'", "").replace("`", "").replace("’", "").replace("-", " ").replace("_", " ")
    s = s.replace(".", " ").replace(",", " ")
    return " ".join(s.split())


def _keys(name):
    """The lookup keys tried for a name, most exact first."""
    k = norm(name)
    out = [k]
    if k.startswith("the "):
        out.append(k[4:])
    if "(" in k:
        out.append(" ".join(k.split("(")[0].split()))
    return out


def from_runs(runs):
    out = []
    for r in runs:
        if isinstance(r, str):
            a, b = r.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(r))
    return out


def to_runs(indices):
    idx = sorted(set(int(i) for i in indices))
    out = []
    i = 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and idx[j + 1] == idx[j] + 1:
            j += 1
        out.append(idx[i] if i == j else "%d-%d" % (idx[i], idx[j]))
        i = j + 1
    return out


def haversine_km(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = 0.5 - math.cos((lat2 - lat1) * p) / 2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((lon2 - lon1) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))


def _read_jsonl(path):
    if not path.exists():
        raise GazetteerError("missing gazetteer file %s (run tools/build_gazetteer.py)" % path)
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


# ----------------------------------------------------------------------------
# The gazetteer
# ----------------------------------------------------------------------------

class Gazetteer:
    def __init__(self, data_dir=DATA, grid_file=GRID_FILE):
        self.data_dir = Path(data_dir)
        self.grid_file = Path(grid_file)
        self._tables = {}
        self._index = {}
        self._land = None        # list of H3 strings, index order
        self._land_index = None  # {h3: index}
        self.trace = []

    # ---- loading ------------------------------------------------------------

    def table(self, name):
        if name not in self._tables:
            self._tables[name] = _read_jsonl(self.data_dir / (name + ".jsonl"))
        return self._tables[name]

    def index(self, name):
        """{normalised name or alt_name: [rows]} for a table."""
        if name not in self._index:
            idx = defaultdict(list)
            for row in self.table(name):
                for n in [row["name"]] + list(row.get("alt_names", [])):
                    for k in _keys(n):
                        if row not in idx[k]:
                            idx[k].append(row)
            self._index[name] = idx
        return self._index[name]

    def land(self):
        if self._land is None:
            if not self.grid_file.exists():
                raise GazetteerError("missing land grid %s" % self.grid_file)
            with open(self.grid_file) as f:
                self._land = [line.strip() for line in f if line.strip()]
            self._land_index = {c: i for i, c in enumerate(self._land)}
        return self._land

    def land_index(self):
        self.land()
        return self._land_index

    def to_h3(self, cells):
        land = self.land()
        return {land[i] for i in cells}

    def from_h3(self, h3cells):
        li = self.land_index()
        return {li[c] for c in h3cells if c in li}

    # ---- name matching ------------------------------------------------------

    def _lookup(self, table, name, kind, rows_filter=None, extra_hint=""):
        idx = self.index(table)
        for k in _keys(name):
            rows = idx.get(k, [])
            if rows_filter is not None:
                rows = [r for r in rows if rows_filter(r)]
            if rows:
                # a row whose own name is the key beats one that only carries it as an alias or as a
                # parenthesised variant ("Great Lakes region" must not pick "Great Lakes region (Africa)")
                def rank(r):
                    if norm(r["name"]) == k:
                        return 0
                    if any(norm(a) == k for a in r.get("alt_names", [])):
                        return 1
                    return 2
                return sorted(rows, key=rank)
        pool = idx.keys() if rows_filter is None else {k for k, rows in idx.items() if any(rows_filter(r) for r in rows)}
        close = difflib.get_close_matches(norm(name), list(pool), n=6, cutoff=0.55)
        names = []
        for c in close:
            for r in idx[c]:
                if rows_filter is None or rows_filter(r):
                    label = r["name"] + (" (%s)" % r["country"] if "country" in r else "")
                    if label not in names:
                        names.append(label)
        hint = ("; closest: " + ", ".join(names[:8])) if names else ""
        raise GazetteerError("unknown %s %r%s%s" % (kind, name, extra_hint, hint))

    def country(self, name):
        rows = self._lookup("countries", name, "country")
        if len(rows) > 1:
            rows = sorted(rows, key=lambda r: -r["n_cells"])
        return rows[0]

    def admin1(self, name, country=None):
        """Rows for an admin-1 name: the unit's own name first, then a Natural Earth "region" value
        (an Italian region, a Latvian planning region, a Belgian community), then alt_names."""
        if country is not None:
            c = self.country(country)
            cn = norm(c["name"])
            alts = {norm(a) for a in c["alt_names"]}
            flt = lambda r: r["adm0_a3"] == c["adm0_a3"] or norm(r["country"]) == cn or norm(r["country"]) in alts  # noqa: E731
            keys = _keys(name)
            own = [r for r in self.table("admin1") if flt(r) and norm(r["name"]) in keys]
            # a Natural Earth "region" value names a group of units (an Italian region, a Latvian planning
            # region, a Russian federal district); when a unit carries the same name (Riga city inside
            # the Riga region) both are taken, since the region contains the unit
            rows = [r for r in self.table("admin1") if flt(r) and r.get("region") and norm(r["region"]) in keys]
            if own or rows:
                return own + [r for r in rows if r not in own], c
            try:
                return self._lookup("admin1", name, "admin1", flt, " in %s" % c["name"]), c
            except GazetteerError as e:
                # is it a unit of another country? say so
                anywhere = self.index("admin1").get(norm(name), [])
                if anywhere:
                    raise GazetteerError(str(e) + "; found in: " + ", ".join(sorted({r["country"] for r in anywhere})))
                raise
        rows = self._lookup("admin1", name, "admin1")
        countries = sorted({r["country"] for r in rows})
        if len(countries) > 1:
            raise GazetteerError("admin1 %r is ambiguous without a country: %s" % (name, ", ".join(countries)))
        return rows, None

    def place(self, name, country=None):
        flt = None
        if country is not None:
            c = self.country(country)
            names = {norm(c["name"])} | {norm(a) for a in c["alt_names"]}
            flt = lambda r: norm(r["country"]) in names  # noqa: E731
        rows = self._lookup("places", name, "place", flt, (" in %s" % country) if country else "")
        # exact-name matches before alias matches, then the most populous, then the Natural Earth row
        kn = _keys(name)[0]
        rows = sorted(rows, key=lambda r: (0 if norm(r["name"]) == kn else 1,
                                           -(r["pop"] or 0), 0 if r.get("source") == "ne" else 1))
        return rows[0]

    def region(self, name):
        rows = self._lookup("regions", name, "region")
        return rows[0]

    def river(self, name):
        return self._lookup("rivers", name, "river")[0]

    def lake(self, name):
        return self._lookup("lakes", name, "lake")[0]

    # ---- geometry -----------------------------------------------------------

    def disk(self, lat, lon, km):
        """Land cells whose centre lies within km of the point."""
        li = self.land_index()
        c0 = h3.latlng_to_cell(lat, lon, RES)
        k = int(math.ceil(km / 11.0)) + 1
        out = set()
        for c in h3.grid_disk(c0, k):
            if c in li:
                clat, clon = h3.cell_to_latlng(c)
                if haversine_km(lat, lon, clat, clon) <= km:
                    out.add(li[c])
        if not out and c0 in li:
            out.add(li[c0])
        if not out:
            # 1 Nov 2026: a coastal or island point whose own cell is at sea takes the nearest land
            # cell within 3 rings (about 30 km), so small radii (3-20 km) do not resolve empty.
            best = None
            for c in h3.grid_disk(c0, 3):
                if c in li:
                    clat, clon = h3.cell_to_latlng(c)
                    d = haversine_km(lat, lon, clat, clon)
                    if best is None or d < best[0]:
                        best = (d, li[c])
            if best is not None:
                out.add(best[1])
        return out

    def widen(self, cells, km):
        """Add every land cell within km of any cell centre of the set."""
        if km <= 0:
            return set(cells)
        land = self.land()
        li = self._land_index
        k = int(math.ceil(km / 11.0)) + 1
        out = set(cells)
        for i in cells:
            c0 = land[i]
            lat, lon = h3.cell_to_latlng(c0)
            for c in h3.grid_disk(c0, k):
                j = li.get(c)
                if j is not None and j not in out:
                    clat, clon = h3.cell_to_latlng(c)
                    if haversine_km(lat, lon, clat, clon) <= km:
                        out.add(j)
        return out

    def polygon(self, points):
        from shapely.geometry import Polygon
        import grid
        if len(points) > MAX_POLYGON_POINTS:
            self.trace.append("polygon: %d points, more than the %d the grammar allows" % (len(points), MAX_POLYGON_POINTS))
        poly = Polygon([(float(x), float(y)) for x, y in points])
        if not poly.is_valid:
            poly = poly.buffer(0)
        return self.from_h3(grid.shape_cells(poly, RES))

    def cliopatria(self, name, year):
        import grid
        from slug import slugify
        slug = name if (name == slugify(name)) else slugify(name)
        year = int(year)
        feats = [ft for ft in grid.load_features() if ft["slug"] == slug]
        if not feats:
            slugs = sorted({ft["slug"] for ft in grid.load_features()})
            close = difflib.get_close_matches(slug, slugs, n=6, cutoff=0.6)
            raise GazetteerError("unknown Cliopatria polity %r (slug %s)%s" % (
                name, slug, ("; closest: " + ", ".join(close)) if close else ""))
        alive = [ft for ft in feats if ft["from"] <= year <= ft["to"]]
        if not alive:
            spans = sorted({(ft["from"], ft["to"]) for ft in feats})
            raise GazetteerError("Cliopatria polity %s has no shape in %d; its shapes cover %s" % (
                slug, year, ", ".join("%d..%d" % s for s in spans[:12]) + (" ..." if len(spans) > 12 else "")))
        self.trace.append("cliopatria: %s in %d (%d shape%s)" % (slug, year, len(alive), "" if len(alive) == 1 else "s"))
        return self.from_h3(grid.polity_cells(slug, year, RES, land_only=True))

    def polity_cells(self, slug, year):
        """Cells of a polity in a year: from the anchor file when the year is an anchor, else Cliopatria."""
        import grid
        if year in grid.ANCHOR_YEARS:
            path = ANCHOR_DIR / (grid.anchor_name(year) + ".json")
            if path.exists():
                with open(path) as f:
                    anchor = json.load(f)
                runs = anchor.get("owners", {}).get(slug)
                if runs is not None:
                    self.trace.append("anchor %s: %s" % (path.stem, slug))
                    return set(from_runs(runs))
        return self.cliopatria(slug, year)

    def border_band(self, a, b, year, width=1):
        land = self.land()
        li = self._land_index
        ca = self.polity_cells(a, int(year))
        cb = self.polity_cells(b, int(year))
        if not ca or not cb:
            raise GazetteerError("border_band: %s or %s has no cells in %s" % (a, b, year))
        ha = {land[i] for i in ca}
        hb = {land[i] for i in cb}
        front_a = {c for c in ha if any(n in hb for n in h3.grid_ring(c, 1))}
        front_b = {c for c in hb if any(n in ha for n in h3.grid_ring(c, 1))}
        if not front_a:
            raise GazetteerError("border_band: %s and %s do not touch in %s" % (a, b, year))
        band_a, band_b = set(front_a), set(front_b)
        for _ in range(max(int(width), 1) - 1):
            band_a |= {n for c in band_a for n in h3.grid_ring(c, 1) if n in ha}
            band_b |= {n for c in band_b for n in h3.grid_ring(c, 1) if n in hb}
        self.trace.append("border_band: %s|%s in %s, %d+%d front cells, width %s" % (a, b, year, len(front_a), len(front_b), width))
        return {li[c] for c in band_a | band_b}

    # ---- the resolver -------------------------------------------------------

    def resolve(self, spec, _depth=0):
        """Resolve a region spec to a set of land-cell indices. Resets self.trace at depth 0."""
        if _depth == 0:
            self.trace = []
        if _depth > 20:
            raise GazetteerError("region specs nested more than 20 deep (a cycle?)")
        if isinstance(spec, str):
            spec = json.loads(spec)
        if not isinstance(spec, dict):
            raise GazetteerError("a region spec is a JSON object, got %r" % (spec,))
        keys = set(spec) - {"text", "note", "confidence"}
        if "union" in keys:
            out = set()
            for s in spec["union"]:
                out |= self.resolve(s, _depth + 1)
            return out
        if "intersect" in keys:
            parts = [self.resolve(s, _depth + 1) for s in spec["intersect"]]
            if not parts:
                return set()
            out = parts[0]
            for p in parts[1:]:
                out = out & p
            return out
        if "minus" in keys:
            parts = spec["minus"]
            if not isinstance(parts, list) or len(parts) < 1:
                raise GazetteerError('"minus" takes a list [A, B, ...]: A minus the rest')
            out = self.resolve(parts[0], _depth + 1)
            for p in parts[1:]:
                out = out - self.resolve(p, _depth + 1)
            return out
        if "region" in keys:
            row = self.region(spec["region"])
            self.trace.append("region: %s (confidence %s)" % (row["name"], row.get("confidence", "?")))
            return self.resolve(row["spec"], _depth + 1)
        if "admin1" in keys:
            rows, c = self.admin1(spec["admin1"], spec.get("country"))
            self.trace.append("admin1: %s (%s)" % (" + ".join(sorted({r["name"] for r in rows})), rows[0]["country"]))
            out = set()
            for r in rows:
                out.update(from_runs(r["cells"]))
            return out
        if "place" in keys:  # before "country": a place spec may carry "country" to disambiguate
            if "km" not in spec:
                raise GazetteerError('a "place" spec needs "km"')
            row = self.place(spec["place"], spec.get("country"))
            self.trace.append("place: %s (%s, %.2f %.2f) within %s km" % (row["name"], row["country"], row["lon"], row["lat"], spec["km"]))
            return self.disk(row["lat"], row["lon"], float(spec["km"]))
        if "country" in keys:
            row = self.country(spec["country"])
            self.trace.append("country: %s (%s)" % (row["name"], row["iso_a3"]))
            return set(from_runs(row["cells"]))
        if "lon" in keys and "lat" in keys:
            km = float(spec.get("km", 0))
            self.trace.append("point: %.3f %.3f within %s km" % (float(spec["lon"]), float(spec["lat"]), km))
            return self.disk(float(spec["lat"]), float(spec["lon"]), km)
        if "cliopatria" in keys:
            if "year" not in spec:
                raise GazetteerError('a "cliopatria" spec needs "year"')
            return self.cliopatria(spec["cliopatria"], spec["year"])
        if "polygon" in keys:
            self.trace.append("polygon: %d points" % len(spec["polygon"]))
            return self.polygon(spec["polygon"])
        if "border_band" in keys:
            bb = spec["border_band"]
            return self.border_band(bb["a"], bb["b"], bb["year"], bb.get("width", 1))
        if "river" in keys:
            row = self.river(spec["river"])
            km = float(spec.get("km", 0))
            self.trace.append("river: %s (%d cells) widened %s km" % (row["name"], row["n_cells"], km))
            return self.widen(set(from_runs(row["cells"])), km)
        if "lake" in keys:
            row = self.lake(spec["lake"])
            self.trace.append("lake: %s (%d cells)" % (row["name"], row["n_cells"]))
            return set(from_runs(row["cells"]))
        raise GazetteerError("unknown region spec keys %s; expected one of country, admin1, place, lon/lat, "
                             "cliopatria, region, polygon, border_band, river, lake, union, minus, intersect"
                             % sorted(keys))

    # ---- reporting ----------------------------------------------------------

    def bbox(self, cells):
        if not cells:
            return None
        land = self.land()
        lats, lons = [], []
        for i in cells:
            lat, lon = h3.cell_to_latlng(land[i])
            lats.append(lat)
            lons.append(lon)
        return [round(min(lons), 2), round(min(lats), 2), round(max(lons), 2), round(max(lats), 2)]

    def search(self, text):
        """Every entry of every table whose name or alt_names contain the text."""
        k = norm(text)
        hits = []
        for table in ("countries", "admin1", "regions", "places", "rivers", "lakes"):
            try:
                rows = self.table(table)
            except GazetteerError:
                continue
            for r in rows:
                names = [r["name"]] + list(r.get("alt_names", []))
                if any(k in norm(n) for n in names):
                    extra = r.get("country", "")
                    if table == "places":
                        extra = "%s, pop %s" % (r["country"], r.get("pop"))
                    hits.append((table, r["name"], extra, ", ".join(a for a in r.get("alt_names", [])[:6])))
        return hits


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def _cmd_resolve(g, spec_text, show_cells=False):
    try:
        spec = json.loads(spec_text)
    except json.JSONDecodeError as e:
        print("not JSON: %s" % e)
        return 2
    try:
        cells = g.resolve(spec)
    except GazetteerError as e:
        print("error: %s" % e)
        return 1
    print("cells: %d (about %d km2)" % (len(cells), round(len(cells) * 252.9)))
    print("bbox: %s" % (g.bbox(cells),))
    for line in g.trace:
        print("matched: " + line)
    if show_cells:
        print("runs: " + json.dumps(to_runs(cells)))
    return 0


def _cmd_check(g, show_counts=False):
    rows = g.table("regions")
    ok, failed, empty = 0, [], []
    counts = {}
    for r in rows:
        try:
            cells = g.resolve(r["spec"])
        except GazetteerError as e:
            failed.append((r["name"], str(e)))
            continue
        except Exception as e:  # noqa: BLE001
            failed.append((r["name"], "%s: %s" % (type(e).__name__, e)))
            continue
        counts[r["name"]] = len(cells)
        if show_counts:
            print("COUNT %6d  conf %s  %-32s bbox %s" % (len(cells), r.get("confidence", "?"), r["name"], g.bbox(cells)))
        if not cells:
            empty.append(r["name"])
        else:
            ok += 1
    print("regions: %d, resolve: %d, empty: %d, failed: %d" % (len(rows), ok, len(empty), len(failed)))
    for name, err in failed:
        print("FAIL %s: %s" % (name, err))
    for name in empty:
        print("EMPTY %s" % name)
    names = {norm(r["name"]) for r in rows}
    dup = [r["name"] for r in rows if sum(1 for q in rows if norm(q["name"]) == norm(r["name"])) > 1]
    if dup:
        print("DUPLICATE names: %s" % sorted(set(dup)))
    for r in rows:
        for a in r.get("alt_names", []):
            if norm(a) in names and norm(a) != norm(r["name"]):
                print("NOTE alt_name %r of %s is also a region name" % (a, r["name"]))
    return 1 if failed else 0


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    g = Gazetteer()
    cmd = argv[1]
    if cmd == "resolve":
        if len(argv) < 3:
            print("usage: gazetteer.py resolve '<json>' [--cells]")
            return 2
        return _cmd_resolve(g, argv[2], "--cells" in argv[3:])
    if cmd == "check":
        return _cmd_check(g, "--counts" in argv[2:])
    if cmd == "names":
        text = " ".join(argv[2:])
        for table, name, extra, alts in g.search(text)[:60]:
            print("%-9s %-40s %-30s %s" % (table, name, extra, alts))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
