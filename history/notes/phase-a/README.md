# Phase A: the foundation (18 Oct 2026, 01:56 to 04:27 UTC)

Run by the master thread as one workflow (five builders, two at a time). The builders' full reports are in [builder-reports.json](builder-reports.json) (files, numbers, problems); the summaries below are what later phases need.

| Builder | Wrote | Headline numbers |
| --- | --- | --- |
| polity-table | data/polities.csv, data/shapes.csv, data/polities/<slug>.json (1,544), data/README.md, tools/build_tables.py | 13,797 shapes, 1,637 Names (1,544 leaf + 93 umbrella/relation), 17,402 neighbour entries, 1 slug collision (han / han-2) |
| research-groups | data/research-groups.json, .md, tools/research_groups.py | 76 groups, every Name owned once; 8 groups over 45 polities (split into parts by tools/fill_briefs.py for Phase B) |
| grid | tools/grid.py, compile_anchors.py, preview.py, data/grid/land_r5.txt, data/anchors/*.json (120) | 524,441 land cells at H3 r5 (the plan's 214,699 was wrong; corrected); 120 anchors; median cell-area ratio 0.95 |
| gazetteer | data/gazetteer/*.jsonl, tools/gazetteer.py, build_gazetteer.py, regions_src.py | 257 countries, 4,588 admin-1, 1,053 rivers, 725 lakes, 7,714 places, 725 historical regions, all resolving |
| colours | colours.json, tools/colour.py, colour_seed.py, colours-README.md | 415 fixed entries (227 conventional states), 1,129 assigned from a 72-colour wheel, 0 neighbour pairs under 0.10 OKLab at any anchor |
| spec | briefs/dossier.schema.json, briefs/*.md (5 briefs + README), tools/validate_dossier.py, polities/_example-tang-dynasty.json | Tang example: 60 events, 19 pages, 33 keyframe verdicts, validates; Cliopatria's Tang row has 32 shapes, not 47 (plan corrected) |

## Review

The workflow's adversarial review agent failed on the account's usage limit (04:27 UTC, "session limit, resets 6am"). Instead the master thread checked at 06:05 UTC: the Tang's cells in the 700 anchor lie in China and the Russian Empire's in 1800 in Russia; every slug in colours.json, the anchors and the groups is in polities.csv and every leaf polity has a colour and exactly one group; the validator passes the Tang example (0 errors, 2 benign warnings) and the gazetteer resolves Khorasan to 2,206 cells. The research brief was read in full and judged followable. Not re-run: a full `colour.py check` and `gazetteer.py check` (the builders ran both, exit 0).

## Known data problems carried into Phase B

Listed per state in the filled briefs' owned tables (notes/phase-b/briefs/) and in data/README.md: reused Names spanning several states (Later Zhou, Kingdom of Italy, Georgia, Kingdom of Great Britain to 2024 with no "United Kingdom" row), shapes still containing lost territory (French Fifth Republic with Algeria, Netherlands Antilles with Suriname), mislabelled rows (Saint Kitts on Saint Croix, Ptolemaic Kingdom in Iran, Türgesh/Turks swap), 115 shared Wikidata ids, 427 gaps between consecutive shapes.

## Decisions taken here

- Phase B batches: a group with more than 16 leaf polities or 90 Cliopatria shapes is split into parts (-a, -b, ...) by founding year; 192 batches over 74 groups (xx-02 gazetteer and xx-03 wars index run later from their own briefs). The additions the scope asks for go to the lightest part.
- Each agent reads its filled brief from notes/phase-b/briefs/<id>.md and saves its report to notes/phase-b/reports/<id>.json; the reviewer's goes to notes/phase-b/reviews/<id>.json; the fixer's to reports/<id>-fixed.json.
- Lakes count as land cells (Natural Earth 50m land has no lake holes); the Caspian is a hole. Revisit at rendering if lakes should read as water.
