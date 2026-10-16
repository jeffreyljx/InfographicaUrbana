"""Packs the city trade and manufacturing tables into src/lib/industry.json for the Industry and Exports page.

Usage: python3 scripts/industry/build_industry.py <folder with trade.csv, exports_only.csv, japan_ports.csv,
container_ports.csv, manufacturing.csv and exchange_rates.csv>

The CSVs come from the City trade and manufacturing research (16 Oct 2026): US$ at Federal Reserve G.5A annual
averages, a source URL (or several, separated by " ; ") on every row. Country names follow the site's own labels."""
import csv, json, os, re, sys

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "src", "lib", "industry.json")
COUNTRY = {"Hong Kong SAR": "China", "UAE": "United Arab Emirates", "Taiwan": "Taiwan, China"}
NUM = {"exports_usd_bn", "imports_usd_bn", "total_usd_bn", "teu_million", "va_usd_bn", "employment",
       "va_per_worker_usd_k", "per_usd"}


def read(name):
    with open(os.path.join(SRC, name + ".csv"), newline="", encoding="utf-8") as f:
        rows = []
        for r in csv.DictReader(f):
            out = {}
            for k, v in r.items():
                v = (v or "").strip()
                if k in NUM:
                    out[k] = None if v == "" else (int(float(v)) if k == "employment" else float(v))
                elif k == "source":
                    out[k] = [u.strip() for u in re.findall(r"https?://[^;()]+", v)]   # some URLs hold spaces
                elif k == "upper_bound":
                    out[k] = v == "yes"
                elif k == "country":
                    out[k] = COUNTRY.get(v, v)
                else:
                    out[k] = v
            rows.append(out)
        return rows


data = {name: read(name) for name in ("trade", "exports_only", "japan_ports", "container_ports", "manufacturing", "exchange_rates")}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
print({k: len(v) for k, v in data.items()}, os.path.getsize(OUT), "bytes")
