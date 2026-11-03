#!/usr/bin/env python3
"""Validate EmpireMap dossiers (history/polities/<slug>.json) against briefs/dossier.schema.json
and the checks the schema cannot express.

Usage (run from any directory):
    python3 -I tools/validate_dossier.py polities/tang-dynasty.json [more files...]
    python3 -I tools/validate_dossier.py polities/*.json --json        # machine-readable summary
    python3 -I tools/validate_dossier.py FILE --resolve                # also resolve every region
                                                                       #   through tools/gazetteer.py
    python3 -I tools/validate_dossier.py FILE --schema PATH            # another schema file

Exit code 1 when any file has an error; warnings do not fail the run.

What is checked:
  schema    JSON Schema 2020-12 through the `jsonschema` package when it is importable, otherwise
            a built-in checker for the subset the schema uses (type, enum, const, required,
            properties, additionalProperties, items, min/max items, minLength, pattern, minimum,
            maximum, exclusiveMinimum, $ref, oneOf, allOf, if/then, not).
  identity  file name == slug (files whose name starts with "_" are exempt), start <= end.
  ledger    sorted by (year, month); events inside the state's life (warning); found at the
            start year and dissolve at the end year (warning); every source URL listed in
            sources; a contest/vassal/occupation start matched by a later end with the same
            counterpart (warning); counterparts that look like slugs but exist nowhere (warning).
  keyframes shape ids belong to this dossier's slug or one of its cliopatria_names; ids absent
            from data/shapes.csv are new keyframes and need from/to; shapes of the slug that
            are not reviewed (warning); from <= to.
  wars, capitals, rulers, certainty: from <= to; certainty covers the life without gaps or
            overlaps (warning).
  regions   with --resolve, every region spec is resolved by the gazetteer; a name it does not
            know, or a region with no cells, is a warning (the gazetteer agent fixes names).
  places    a {"place": ...} without "country" whose name matches gazetteer places in more than one
            country (warning, with the place the gazetteer takes: the exact name first, then the most
            populous; Memphis is Tennessee and Roma is in Australia without "country").
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

HIST = HERE.parent
SCHEMA_PATH = HIST / "briefs" / "dossier.schema.json"
SHAPES_CSV = HIST / "data" / "shapes.csv"
POLITIES_CSV = HIST / "data" / "polities.csv"
POLITIES_DIR = HIST / "polities"

SLUG_RE = re.compile(r"^(rel-)?[a-z0-9]+(-[a-z0-9]+)*$")

try:
    from slug import slugify
except Exception:  # pragma: no cover
    slugify = None


# ----------------------------------------------------------------------------
# Built-in schema checker (used only when `jsonschema` is not installed)
# ----------------------------------------------------------------------------

def _resolve_ref(ref, root):
    if not ref.startswith("#/"):
        raise ValueError("only local $ref supported: " + ref)
    node = root
    for part in ref[2:].split("/"):
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def _type_ok(value, typ):
    if isinstance(typ, list):
        return any(_type_ok(value, t) for t in typ)
    if typ == "object":
        return isinstance(value, dict)
    if typ == "array":
        return isinstance(value, list)
    if typ == "string":
        return isinstance(value, str)
    if typ == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if typ == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if typ == "boolean":
        return isinstance(value, bool)
    if typ == "null":
        return value is None
    return True


def _check(value, schema, root, path, out):
    """Append (path, message) tuples to out; returns True when value is valid."""
    if schema is True:
        return True
    if schema is False:
        out.append((path, "no value allowed here"))
        return False
    start = len(out)
    if "$ref" in schema:
        _check(value, _resolve_ref(schema["$ref"], root), root, path, out)
    if "type" in schema and not _type_ok(value, schema["type"]):
        out.append((path, "expected %s, got %s" % (schema["type"], type(value).__name__)))
        return False
    if "enum" in schema and value not in schema["enum"]:
        out.append((path, "%r is not one of %s" % (value, schema["enum"])))
    if "const" in schema and value != schema["const"]:
        out.append((path, "%r is not %r" % (value, schema["const"])))
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            out.append((path, "string shorter than %d" % schema["minLength"]))
        if "pattern" in schema and not re.search(schema["pattern"], value):
            out.append((path, "%r does not match %s" % (value, schema["pattern"])))
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            out.append((path, "%r is below the minimum %r" % (value, schema["minimum"])))
        if "maximum" in schema and value > schema["maximum"]:
            out.append((path, "%r is above the maximum %r" % (value, schema["maximum"])))
        if "exclusiveMinimum" in schema and value <= schema["exclusiveMinimum"]:
            out.append((path, "%r must be greater than %r" % (value, schema["exclusiveMinimum"])))
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                out.append((path, "missing required key %r" % key))
        props = schema.get("properties", {})
        for key, sub in props.items():
            if key in value:
                _check(value[key], sub, root, path + "/" + key, out)
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    out.append((path, "unexpected key %r" % key))
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            out.append((path, "fewer than %d items" % schema["minItems"]))
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            out.append((path, "more than %d items" % schema["maxItems"]))
        if "items" in schema:
            for i, item in enumerate(value):
                _check(item, schema["items"], root, "%s/%d" % (path, i), out)
    if "allOf" in schema:
        for sub in schema["allOf"]:
            _check(value, sub, root, path, out)
    if "oneOf" in schema:
        matches = 0
        for sub in schema["oneOf"]:
            trial = []
            if _check(value, sub, root, path, trial) and not trial:
                matches += 1
        if matches != 1:
            keys = sorted(value.keys()) if isinstance(value, dict) else type(value).__name__
            out.append((path, "matches %d forms of the region grammar instead of 1 (keys: %s)"
                        % (matches, keys)))
    if "not" in schema:
        trial = []
        if _check(value, schema["not"], root, path, trial) and not trial:
            out.append((path, "must not match %s" % json.dumps(schema["not"])))
    if "if" in schema:
        trial = []
        if _check(value, schema["if"], root, path, trial) and not trial:
            if "then" in schema:
                _check(value, schema["then"], root, path, out)
        elif "else" in schema:
            _check(value, schema["else"], root, path, out)
    return len(out) == start


def schema_errors(doc, schema):
    """[(path, message)] from jsonschema when available, else from the built-in checker."""
    try:
        import jsonschema  # noqa: F401
        from jsonschema import Draft202012Validator
    except Exception:
        out = []
        _check(doc, schema, schema, "", out)
        return sorted(set(out))
    validator = Draft202012Validator(schema)
    out = []
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path)):
        path = "/" + "/".join(str(p) for p in err.absolute_path)
        if err.validator == "oneOf":
            keys = sorted(err.instance.keys()) if isinstance(err.instance, dict) else "?"
            msg = "region spec matches no single form of the grammar (keys: %s)" % keys
        elif err.validator == "additionalProperties":
            msg = err.message
        else:
            msg = err.message
            if len(msg) > 200:
                msg = msg[:200] + "..."
        out.append((path if path != "/" else "/", msg))
    return out


# ----------------------------------------------------------------------------
# Semantic checks
# ----------------------------------------------------------------------------

def load_shapes():
    """{slug: [shape_id, ...]} from data/shapes.csv, or None when the table is absent."""
    if not SHAPES_CSV.exists():
        return None
    table = {}
    with open(SHAPES_CSV, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            table.setdefault(row["slug"], []).append(row["shape_id"])
    return table


_GAZ = None


def ambiguous_place(name):
    """A warning for a place name, given without a country, that matches gazetteer places in more than
    one country (data/gazetteer/places.jsonl, matched as tools/gazetteer.py matches names), else None.
    None as well when the gazetteer cannot be loaded."""
    global _GAZ
    if _GAZ is None:
        try:
            import gazetteer as G
            g = G.Gazetteer()
            g.index("places")
            _GAZ = (G, g)
        except Exception:  # pragma: no cover
            _GAZ = False
    if not _GAZ or not isinstance(name, str):
        return None
    G, g = _GAZ
    idx = g.index("places")
    rows = []
    for k in G._keys(name):
        rows = idx.get(k, [])
        if rows:
            break
    countries = sorted({r.get("country") or "?" for r in rows})
    if len(countries) < 2:
        return None
    try:
        r = g.place(name)
        took = "%s in %s" % (r["name"], r.get("country"))
    except Exception:  # pragma: no cover
        took = "?"
    return ("place %r has no \"country\" and matches places in %d countries (%s); the gazetteer takes %s"
            % (name, len(countries), ", ".join(countries), took))


def load_known_slugs():
    known = set()
    if POLITIES_CSV.exists():
        with open(POLITIES_CSV, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                known.add(row["slug"])
    if POLITIES_DIR.exists():
        for p in POLITIES_DIR.glob("*.json"):
            if not p.name.startswith("_"):
                known.add(p.stem)
    return known


def _collect_spec(spec, path, out):
    """Append (path, spec) for a region spec and, below it, the parts of a combinator."""
    if not isinstance(spec, dict):
        return
    out.append((path, spec))
    for k in ("union", "minus", "intersect"):
        if k in spec and isinstance(spec[k], list):
            for i, sub in enumerate(spec[k]):
                _collect_spec(sub, "%s/%s/%d" % (path, k, i), out)


def walk_regions(doc, path, out):
    """Collect (path, spec) for every region spec in the dossier, from the places the schema puts
    them: identity.predecessors[].land, identity.successors[].land, keyframe_review[].correction,
    ledger[].region and wars[].zones[]. (A ledger event is itself a dict with a key named
    "region", so the specs cannot be found by looking for grammar keys.)"""
    ident = doc.get("identity") or {}
    for key in ("predecessors", "successors"):
        for i, h in enumerate(ident.get(key) or []):
            if isinstance(h, dict) and "land" in h:
                _collect_spec(h["land"], "/identity/%s/%d/land" % (key, i), out)
    for i, k in enumerate(doc.get("keyframe_review") or []):
        if isinstance(k, dict) and "correction" in k:
            _collect_spec(k["correction"], "/keyframe_review/%d/correction" % i, out)
    for i, ev in enumerate(doc.get("ledger") or []):
        if isinstance(ev, dict) and "region" in ev:
            _collect_spec(ev["region"], "/ledger/%d/region" % i, out)
    for i, w in enumerate(doc.get("wars") or []):
        if isinstance(w, dict):
            for j, z in enumerate(w.get("zones") or []):
                _collect_spec(z, "/wars/%d/zones/%d" % (i, j), out)


def semantic_checks(doc, file_path, shapes, known_slugs, resolve):
    errors, warnings = [], []
    E = lambda p, m: errors.append((p, m))  # noqa: E731
    W = lambda p, m: warnings.append((p, m))  # noqa: E731

    ident = doc.get("identity") or {}
    slug = ident.get("slug")
    stem = Path(file_path).stem
    if isinstance(slug, str) and not stem.startswith("_") and stem != slug:
        E("/identity/slug", "file is named %r but the slug is %r" % (stem, slug))
    if slugify and isinstance(ident.get("name"), str) and isinstance(slug, str) \
            and not ident.get("cliopatria_names") and slugify(ident["name"]) != slug:
        W("/identity/slug", "a state Cliopatria lacks should take slugify(name) = %r"
          % slugify(ident["name"]))

    start = (ident.get("start") or {}).get("year")
    end = (ident.get("end") or {}).get("year")
    if isinstance(start, int) and isinstance(end, int) and start > end:
        E("/identity", "start year %d is after end year %d" % (start, end))

    def span_check(items, path, lo="from", hi="to"):
        for i, it in enumerate(items or []):
            a, b = it.get(lo), it.get(hi)
            if isinstance(a, int) and isinstance(b, int):
                if a > b:
                    E("%s/%d" % (path, i), "%s %d is after %s %d" % (lo, a, hi, b))
                if isinstance(start, int) and isinstance(end, int) and (b < start or a > end):
                    W("%s/%d" % (path, i), "span %d..%d lies outside the state's life %d..%d"
                      % (a, b, start, end))

    span_check(ident.get("capitals"), "/identity/capitals")
    span_check(ident.get("rulers"), "/identity/rulers")
    span_check(doc.get("wars"), "/wars")
    span_check(doc.get("certainty"), "/certainty")

    # certainty coverage
    cert = sorted([c for c in doc.get("certainty") or [] if isinstance(c.get("from"), int)
                   and isinstance(c.get("to"), int)], key=lambda c: c["from"])
    if cert and isinstance(start, int) and isinstance(end, int):
        if cert[0]["from"] > start:
            W("/certainty", "no certainty level for %d..%d" % (start, cert[0]["from"] - 1))
        if cert[-1]["to"] < end:
            W("/certainty", "no certainty level for %d..%d" % (cert[-1]["to"] + 1, end))
        for a, b in zip(cert, cert[1:]):
            if b["from"] > a["to"] + 1:
                W("/certainty", "gap %d..%d" % (a["to"] + 1, b["from"] - 1))
            elif b["from"] <= a["to"]:
                W("/certainty", "overlap %d..%d" % (b["from"], a["to"]))

    # sources
    source_urls = [s.get("url") for s in doc.get("sources") or [] if isinstance(s, dict)]
    seen = set()
    for i, u in enumerate(source_urls):
        if u in seen:
            W("/sources/%d" % i, "duplicate url %s" % u)
        seen.add(u)

    def source_listed(url, path):
        if isinstance(url, str) and url not in seen:
            E(path, "source %s is not listed in sources[]" % url)

    for i, k in enumerate(doc.get("keyframe_review") or []):
        source_listed(k.get("source"), "/keyframe_review/%d/source" % i)
    for i, w in enumerate(doc.get("wars") or []):
        source_listed(w.get("source"), "/wars/%d/source" % i)
    for i, c in enumerate(ident.get("capitals") or []):
        if "source" in c:
            source_listed(c["source"], "/identity/capitals/%d/source" % i)
    for i, r in enumerate(ident.get("rulers") or []):
        if "source" in r:
            source_listed(r["source"], "/identity/rulers/%d/source" % i)

    # ledger
    ledger = doc.get("ledger") or []
    prev = None
    opens = {}
    found_years, dissolve_years = [], []
    for i, ev in enumerate(ledger):
        p = "/ledger/%d" % i
        y, m, t = ev.get("year"), ev.get("month"), ev.get("type")
        source_listed(ev.get("source"), p + "/source")
        if isinstance(y, int):
            key = (y, m if isinstance(m, int) else 0)
            if prev and key < prev:
                E(p, "ledger is not in (year, month) order: %s after %s" % (key, prev))
            prev = key
            if isinstance(start, int) and isinstance(end, int) and (y < start or y > end):
                W(p, "year %d lies outside the state's life %d..%d" % (y, start, end))
        if t == "found":
            found_years.append(y)
        if t == "dissolve":
            dissolve_years.append(y)
        cp = ev.get("counterpart")
        if isinstance(t, str) and t.endswith("_start"):
            opens.setdefault((t[:-6], cp), []).append(i)
        if isinstance(t, str) and t.endswith("_end"):
            lst = opens.get((t[:-4], cp))
            if lst:
                lst.pop(0)
            else:
                W(p, "%s with no earlier %s_start for counterpart %r" % (t, t[:-4], cp))
        if isinstance(cp, str) and SLUG_RE.match(cp) and cp not in known_slugs \
                and cp != "nobody" and known_slugs:
            W(p + "/counterpart", "%r looks like a slug but no polity or dossier has it "
              "(a new state? make sure a dossier will exist)" % cp)
    for (kind, cp), lst in opens.items():
        for i in lst:
            if kind == "vassal" and isinstance(end, int) and ledger[i].get("year") is not None:
                W("/ledger/%d" % i, "vassal_start for %r has no vassal_end (fine only if the "
                  "relation lasts to the state's end in %d)" % (cp, end))
            else:
                W("/ledger/%d" % i, "%s_start for %r has no later %s_end" % (kind, cp, kind))
    if ledger and not found_years:
        W("/ledger", "no 'found' event (rule 1: the state's birth needs a caption)")
    for y in found_years:
        if isinstance(start, int) and y != start:
            W("/ledger", "found event in %d but identity.start.year is %d" % (y, start))
    for y in dissolve_years:
        if isinstance(end, int) and y != end:
            W("/ledger", "dissolve event in %d but identity.end.year is %d" % (y, end))
    if isinstance(end, int) and end < 2024 and ledger and not dissolve_years:
        W("/ledger", "the state ends in %d but has no 'dissolve' event" % end)

    # keyframes
    own_slugs = {slug} if isinstance(slug, str) else set()
    if slugify:
        for n in ident.get("cliopatria_names") or []:
            if isinstance(n, str):
                own_slugs.add(slugify(n))
    reviewed = set()
    for i, k in enumerate(doc.get("keyframe_review") or []):
        p = "/keyframe_review/%d" % i
        sid = k.get("shape_id")
        if not isinstance(sid, str):
            continue
        reviewed.add(sid)
        kslug = sid.rsplit("_", 1)[0]
        if own_slugs and kslug not in own_slugs:
            E(p + "/shape_id", "shape %r does not belong to this dossier (%s)"
              % (sid, ", ".join(sorted(own_slugs))))
        if shapes is not None:
            if sid not in shapes.get(kslug, []):
                if not (isinstance(k.get("from"), int) and isinstance(k.get("to"), int)):
                    E(p, "shape %r is not in data/shapes.csv, so it is a new keyframe and "
                      "needs 'from' and 'to'" % sid)
                if "correction" not in k:
                    E(p, "a new keyframe needs a 'correction' describing the shape")
        if isinstance(k.get("from"), int) and isinstance(k.get("to"), int) and k["from"] > k["to"]:
            E(p, "from %d is after to %d" % (k["from"], k["to"]))
    if shapes is not None:
        for s in own_slugs:
            for sid in shapes.get(s, []):
                if sid not in reviewed:
                    W("/keyframe_review", "Cliopatria shape %s has no verdict" % sid)
    elif doc.get("keyframe_review"):
        W("/keyframe_review", "data/shapes.csv not found: shape ids not checked")

    # regions
    regions = []
    walk_regions(doc, "", regions)
    for path, spec in regions:
        if "place" in spec and not spec.get("country"):
            amb = ambiguous_place(spec.get("place"))
            if amb:
                W(path, amb)
    top = [r for r in regions if not re.search(r"/(union|minus|intersect)/\d+$", r[0])]
    if resolve:
        try:
            from gazetteer import Gazetteer, GazetteerError
            g = Gazetteer()
        except Exception as exc:  # pragma: no cover
            W("", "gazetteer not available (%s): regions not resolved" % exc)
            g = None
        if g is not None:
            for path, spec in top:
                try:
                    cells = g.resolve(spec)
                    if not cells:
                        W(path, "region resolves to no cells")
                except GazetteerError as exc:
                    W(path, "gazetteer: %s" % exc)
                except Exception as exc:
                    W(path, "gazetteer failed: %s" % exc)
    return errors, warnings, regions


def summarize(doc):
    ident = doc.get("identity") or {}
    ledger = doc.get("ledger") or []
    return {
        "slug": ident.get("slug"),
        "name": ident.get("name"),
        "start": (ident.get("start") or {}).get("year"),
        "end": (ident.get("end") or {}).get("year"),
        "ledger_events": len(ledger),
        "events_by_type": {t: sum(1 for e in ledger if e.get("type") == t)
                           for t in sorted({e.get("type") for e in ledger if isinstance(e, dict)})},
        "low_confidence_events": sum(1 for e in ledger if e.get("confidence") == 1),
        "keyframes_reviewed": len(doc.get("keyframe_review") or []),
        "keyframe_verdicts": {v: sum(1 for k in doc.get("keyframe_review") or []
                                     if k.get("verdict") == v) for v in ("ok", "adjust", "wrong")},
        "wars": len(doc.get("wars") or []),
        "sources": len(doc.get("sources") or []),
        "capitals": len(ident.get("capitals") or []),
        "rulers": len(ident.get("rulers") or []),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="dossier JSON files")
    ap.add_argument("--schema", default=str(SCHEMA_PATH), help="schema path (default: briefs/dossier.schema.json)")
    ap.add_argument("--resolve", action="store_true", help="resolve every region through tools/gazetteer.py")
    ap.add_argument("--json", action="store_true", help="print a JSON summary instead of text")
    ap.add_argument("--quiet", action="store_true", help="print only the per-file verdict lines")
    args = ap.parse_args(argv)

    with open(args.schema, encoding="utf-8") as fh:
        schema = json.load(fh)
    shapes = load_shapes()
    known = load_known_slugs()

    report = []
    any_error = False
    for f in args.files:
        entry = {"file": f, "errors": [], "warnings": []}
        try:
            with open(f, encoding="utf-8") as fh:
                doc = json.load(fh)
        except Exception as exc:
            entry["errors"].append(["", "cannot read JSON: %s" % exc])
            report.append(entry)
            any_error = True
            continue
        errs = schema_errors(doc, schema)
        sem_e, sem_w, regions = semantic_checks(doc, f, shapes, known, args.resolve)
        entry["errors"] = [list(e) for e in errs + sem_e]
        entry["warnings"] = [list(w) for w in sem_w]
        entry["regions"] = len(regions)
        entry["summary"] = summarize(doc)
        entry["valid"] = not entry["errors"]
        any_error = any_error or bool(entry["errors"])
        report.append(entry)

    if args.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
    else:
        for entry in report:
            s = entry.get("summary") or {}
            print("%s %s  (%d errors, %d warnings; %s events, %s sources, %s keyframes, %s regions)" % (
                "OK  " if entry.get("valid") else "FAIL", entry["file"], len(entry["errors"]),
                len(entry["warnings"]), s.get("ledger_events", "?"), s.get("sources", "?"),
                s.get("keyframes_reviewed", "?"), entry.get("regions", "?")))
            if not args.quiet:
                for p, m in entry["errors"]:
                    print("  E %s: %s" % (p or "/", m))
                for p, m in entry["warnings"]:
                    print("  W %s: %s" % (p or "/", m))
    return 1 if any_error else 0


if __name__ == "__main__":
    sys.exit(main())
