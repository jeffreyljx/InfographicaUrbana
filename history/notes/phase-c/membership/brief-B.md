# Membership sweep (1 Nov 2026)

You are one of two membership-sweep agents of the CartaHistoria historical-borders project (the fourth mode of the InfographicaUrbana site). Read `history/README.md` once for the layout, and the "hierarchy.csv (1 Nov 2026)" section of `history/data/README.md`.

## Why

`history/data/hierarchy.csv` says which state sat inside which. The compiler (rule R3) draws a child row of confidence 2 or 3 in its parent's tint over **all** of the child's land in those years: a vassal in the parent's vassal tint, a constituent (member state) at half that tint. The 305 rows so far came only from pairs whose drawn shapes overlapped, so many real members are drawn as independent states: in 1500 the small Imperial Estates sit in the Holy Roman Empire's colour, but Bohemia, Brandenburg, Saxony and Bavaria do not; Hyderabad and Mysore in 1800-1947 show no tie to the Company or the Raj. Your job is to find those missing rows.

## Your parents

Asia: `mongol-empire` (its uluses while the empire was united), `maratha-empire` (the confederacy's houses), `mughal-empire` (Rajput and other vassal kingdoms), `east-india-company` and `british-raj` (the princely states: Hyderabad, Mysore, Travancore, the Rajputana and Central India states, Kashmir and the rest with dossiers), `qing-dynasty` (Outer Mongolia, Tibet and other dependencies it administered, not tributaries), `achaemenid-empire`, `neo-assyrian-empire`, `han-dynasty` and `tang-dynasty` (protectorates and client kingdoms, only where real control is documented). Check every slug exists; a parent with no dossier is reported under problems.

For each parent, find the states with a dossier in `history/polities/` that were its members or vassals, and the years. Start from the parent's own dossier (its notes and ledger) and from grep over the dossiers for the parent's slug and name and for words such as "Imperial Estate", "imperial immediacy", "Prince-elector", "princely state", "subsidiary alliance", "vassal", "tributary", "client". Each dossier is read-only; read it with a short script that prints identity, notes and the ledger lines that name the parent; never print a whole dossier.

## What counts

- **constituent:** a member of a composite state or federation that period maps draw inside it (an Imperial Estate in the Holy Roman Empire, a state of the German Empire, a republic of Yugoslavia, a crown of the Commonwealth or of Aragon, a realm of the Kalmar Union, an ulus of the united Mongol Empire).
- **vassal:** its own ruler under the parent's real overlordship (a Roman client kingdom, a Danubian principality or the Crimean Khanate under the Ottomans, a princely state under the Company or the Raj, a Maratha house under the Peshwa's confederacy).
- **Not a row:** nominal or tribute-only ties (the Zhou king over the Warring States, the Abbasid caliph over the Samanids, Ming or Qing tribute from Korea or Siam), alliances, personal unions of two sovereign crowns where maps draw both apart, and anything the dossiers and pages leave unclear.
- **Skip a child that held much land outside the parent in those years** (the Habsburg monarchy with Hungary, Brandenburg-Prussia with Ducal Prussia, Denmark with Holstein, Sweden with its German lands): the tint covers all the child's land, so it would paint the outside land too. List these under `skipped_outside_land` in your report. A child whose land lay inside the parent (Bohemia, Saxony, Bavaria) is fine.
- **Skip pairs already in hierarchy.csv** for overlapping years, and children that already have a row under another parent in the same years (list those under `clashes`).

Dates: `from` and `to` are whole years, the span of the tie, clipped to the years both dossiers exist (identity start and end). Confidence 3 = both dossiers say so; 2 = one dossier says so and a page you opened confirms it. Never write confidence 1, and never date from memory: when the dossiers do not give the years, open the state's Wikipedia article with WebFetch (budget about 25 pages in all) and quote it. The `evidence` column quotes or closely paraphrases the dossier line or page sentence, with its file or URL.

## Where to write

- `history/notes/phase-c/membership/B.csv`, header `child,parent,from,to,kind,confidence,evidence` (the hierarchy.csv format; quote fields with commas). The orchestrator reviews and merges it; do **not** edit `data/hierarchy.csv`.
- `history/notes/phase-c/membership/B.json`, your report (below).
- Scratch: `/tmp/claude-0/work/membership-B/`.

Shared-folder rules: `/mnt/project-files/history/` is a network mount other agents write to in parallel (a dossier-fix round is editing dossiers right now, so read dossiers fresh and never write them). Touch only your two files. Run Python as `python3 -I -B` from your scratch directory. WebFetch is the only route to Wikipedia; curl is refused. Do not touch the git repository at /home/claude/SkyscraperMaps, do not call any mcp__hearthbot__ tool, do not spawn subagents. Keep your context small: grep for what you need.

## Report

Save and return one JSON object:

```json
{"id": "B", "rows": 0, "by_parent": {"<slug>": 0}, "skipped_outside_land": [{"child": "...", "parent": "...", "why": "..."}],
 "clashes": [{"child": "...", "existing_parent": "...", "parent": "...", "years": [0, 0]}],
 "not_rows": [{"child": "...", "parent": "...", "why": "nominal | unclear | ..."}], "pages_opened": 0, "problems": []}
```
