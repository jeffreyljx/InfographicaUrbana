# Historical borders (CartaHistoria, the site mode; called EmpireMap before 1 Nov 2026)

Every state's borders from 6000 BCE to the present, year by year, for a fourth ScraperMap mode. Jeffrey's ask of 18 Oct 2026 (project thread "Historical empire borders", the master thread that runs every agent and workflow for this project). Read this file first; a thread that starts cold should not repeat work listed here.

- Master plan (the standard, the data model, the agent roster): [master-plan.md](master-plan.md) in this folder, also as a Claude Doc at https://claude.ai/code/artifact/e1b82c1d-d4e2-4aa7-bc81-e5c5439052fe
- Sources and what the container can reach: [sources/README.md](sources/README.md)

## Layout

| Path | What | Written by |
| --- | --- | --- |
| sources/ | Downloaded datasets (Cliopatria v0.2.1 zip, roster by region, historical-basemaps index) and their licences | master thread |
| data/ | Derived tables: polity table, shapes index, H3 cell grid, anchors at handoff years, gazetteer | Phase A foundation agents |
| polities/ | One dossier per state (JSON) plus notes, the research agents' output | Phase B research agents |
| compiled/ | One file per window (76 centuries, 43 decades): yearly cell changes, contests, captions | Phase D rendering agents |
| colours.json | One colour per state for life; owned by the colour agent | Phase A, then the colour agent |
| tools/ | Scripts: ingest, grid compiler, gazetteer, colour check, packer | Phase A agents |
| briefs/ | The agent briefs and the dossier schema | Phase A |
| notes/ | Working notes per phase | all |

## Rules

- Shapes of record are Cliopatria's (CC BY 4.0) until a dossier corrects them; every correction cites a page that was opened.
- Regions in dossiers are named, not drawn; the gazetteer turns names into cells.
- Colours come only from colours.json.
- Production (main) changes only with Jeffrey's go-ahead; this work lives on branch `history` until then.
