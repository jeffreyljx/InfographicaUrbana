# Window brief: {{window}} ({{start_year}} to {{end_year}})

Filled by the orchestrator on {{date}}. You are one of the Phase D rendering agents of the EmpireMap historical-borders project (history/README.md; the plan is history/master-plan.md): 76 century agents for 6000 BCE to 1600 and 43 decade agents for 1600 to 2029, all running in parallel because the handoff years are fixed before any of you starts. Your window is **{{window}}**: the years {{start_year}} to {{end_year}} inclusive. You turn the reviewed dossiers into the year-by-year cell ownership for those years, applying the twelve rules of the standard mechanically. You do not invent borders, you do not invent colours, and you do not move the anchors.

Your final message is data for the orchestrator (section 8), not prose for a person.

## 1. Inputs

- **The two anchors.** `history/data/anchors/{{start_anchor}}.json` is the cell ownership on 1 January of {{start_year}}; `history/data/anchors/{{end_anchor}}.json` is the ownership at the start of the year after {{end_year}} (the next window's first year; the last window uses `p2024`). Anchor stems: `m` + the absolute year, four digits, for BCE (`m0700` is 700 BCE), `p` + the year for CE (`p1790`). Format (history/data/grid/README.md): `{"year", "grid": "land_r5.txt", "owners": {slug: runs}, ...}` where runs are `"start-end"` (inclusive) or single integers indexing `history/data/grid/land_r5.txt`; `grid.from_runs` and `grid.to_runs` convert. The anchors you receive are the Phase C anchors compiled from the reviewed dossiers; their README names any keys beyond `owners` (per-cell status, open contests). Both anchors are fixed: your first year equals the start anchor cell for cell, and your last year, after every change you list, equals the end anchor cell for cell.
- **The dossiers of every state alive in your window** (`history/polities/<slug>.json`, schema `history/briefs/dossier.schema.json`, worked example `history/polities/_example-tang-dynasty.json`):

{{dossiers}}

- **The colour registry** `history/colours.json` is read-only for you and you will not need it: window files carry slugs, never colours; the packer applies colours, tints, hatches and blends at packaging time from the registry.
- **The gazetteer** `history/tools/gazetteer.py` (library: `Gazetteer().resolve(spec)` returns a set of cell indices; `python3 -I history/tools/gazetteer.py resolve '<spec>'` on the command line) turns every region spec in a dossier into cells, and `history/tools/grid.py` gives the land grid, `polity_cells(slug, year)` for Cliopatria shapes, `from_runs`, `to_runs`. `history/data/gazetteer/README.md` documents the names.
- **Resolution.** {{resolution_note}}
- **The seam partners.** The previous window is {{previous_window}} and the next is {{next_window}}; their agents run beside you and you do not talk to them. The seam checker compares your last year with their first (section 6).
- **Scratch:** `/tmp/claude-0/work/window-{{window}}/` (create it). Keep the gazetteer's cell cache there.

## 2. What you produce

`history/compiled/{{window}}.json`, one file, small (only cells that change are listed), in this shape:

```json
{
  "window": "{{window}}", "from": {{start_year}}, "to": {{end_year}},
  "grid": "land_r5.txt", "resolution": 5,
  "start_anchor": "{{start_anchor}}", "end_anchor": "{{end_anchor}}",
  "years": {
    "<year>": {
      "changes": [
        {"cells": ["401233-401240", 401242], "from": "<slug or null>", "to": "<slug or null>",
         "status": "direct | vassal | occupied | contested | neutral",
         "suzerain": "<slug, when status is vassal>", "occupier": "<slug, when occupied>",
         "claimants": ["<slug>", "<slug>"],
         "event": "<slug>/ledger/<index> | <slug>/keyframe/<shape_id> | anchor"}
      ],
      "contests": [{"cells": [...], "a": "<slug>", "b": "<slug>", "since": <year>, "war": "<name>"}],
      "captions": [{"slug": "<slug>", "year": <year>, "month": <1-12, optional>, "type": "<ledger type>", "text": "<the event's note, first sentence>", "source": "<url>"}],
      "capitals": [{"slug": "<slug>", "name": "...", "lon": 0, "lat": 0}]
    }
  },
  "handoff": {
    "end_year": {{end_year}},
    "disagreements": [{"slug": "<slug>", "cells": [...], "ours": "<what the dossiers give>", "anchor": "<what the end anchor gives>", "why": "..."}],
    "conflicts": [{"year": <year>, "cells": [...], "claimants": ["<slug>", "<slug>"], "resolved_to": "<slug>", "rule": "..."}],
    "open_contests": [...same shape as contests...],
    "open_occupations": [{"cells": [...], "owner": "<slug>", "occupier": "<slug>", "since": <year>}],
    "open_vassals": [{"vassal": "<slug or name>", "suzerain": "<slug>", "cells": [...], "since": <year>}],
    "unresolved_regions": [{"slug": "<slug>", "where": "/ledger/<i>", "spec": {...}, "error": "..."}],
    "notes": "..."
  }
}
```

- `years` holds only years in which something changes; an empty window is `"years": {}` with a handoff.
- `changes` list only cells whose owner or status changes that year. `from` is the previous owner, `to` the new one (`null` for nobody's land); `status` is the cells' status after the change. A status change without an owner change (a vassal_start over land the state holds, an occupation) has `from` equal to `to`.
- `contests` lists every contest open in that year (the same entry repeated from `contest_start` to `contest_end`), so a single year can be rendered without reading other years.
- `captions` carry the ledger's `note` (first sentence) for every event in the window, with the month when the event has one, so the player can pause on them (rule 11); include the keyframe corrections' captions only when they move land.
- `capitals` only in years when a capital moves (rule 10).
- Cells are runs of indices into `land_r5.txt`, the anchors' convention.

## 3. The twelve rules, applied mechanically

Work year by year from the start anchor. Keep the full ownership state in memory (a dict cell -> (owner, status, extras) for the cells that are not nobody's; 524,441 cells fit easily). For each year, gather every ledger event of every dossier with that year (month order within the year), every keyframe whose `from` year it is, every state whose `start.year` or `end.year` it is, and apply:

1. **Birth** (rule 1). In `identity.start.year` the state's cells are its `found` event's region (resolved), or, failing that, its first keyframe's corrected shape; `from` is whoever held them (the predecessor, by `identity.predecessors[].land`, or null), `to` the new slug, status direct; caption from the `found` note.
2. **One colour for life** (rule 2). A `rename` event changes nothing in the cells; emit its caption. A new slug is a new state, whatever the name.
3. **Expansion** (rule 3). A `gain` event: cells = the resolved region, intersected with what the counterpart holds (or nobody's land when the counterpart is `nobody`); if the counterpart is a name with no dossier, take the region's cells that are not held by any dossier state, then those held by nobody; `from` the counterpart, `to` the slug, status direct. The packer outlines these cells bright for the year from the change list itself; you do nothing more. A `loss` is the mirror; when the counterpart's own dossier carries the matching gain, apply the pair once (the gain) and do not double-move the cells.
4. **Levels of control** (rule 4). `vassal_start`: the region's cells get status vassal with `suzerain` = this slug; the owner stays the vassal's own slug when the counterpart has a dossier, otherwise the cells become this slug's with status vassal (the packer labels them from the counterpart name in the caption). `vassal_end`: status back to direct under the vassal's own slug (or, when a conqueror is named in the note and the next event is a gain, let that gain move them). `occupation_start`: owner unchanged, status occupied, `occupier` set; `occupation_end`: status back to direct. Dossiers of `type: umbrella` move no cells; ignore them for ownership.
5. **Civil war and rebellion** (rule 5). A `type: rebel` dossier is a state like any other for you: its gains move cells to its slug with status direct; the packer hatches by type. The government's `loss` to the rebel and the rebel's `gain` are one move.
6. **Contested land** (rule 6). `contest_start`: the zone's cells (resolved) keep their owner and get status contested with `claimants` = [holder, challenger]; add the contest to `contests` for every year until its `contest_end`. `contest_end`: the zone's cells go to whoever the matching `gain`/`loss` events of that year say (apply those events first), the rest revert to direct under their holder. A war with no `contest_start` shades nothing; a `wars[].zones` entry alone is not an instruction.
7. **Collapse and partition** (rule 7). In `identity.end.year`, after that year's other events, every cell the state still holds goes to its successors: for each `identity.successors[]`, the cells of its `land` (resolved, intersected with the state's cells) move to that slug with status direct; what no successor takes goes to `null` (neutral). Caption from the `dissolve` note. `split` and `merge` events are handled the same way with their `region` and `counterpart`.
8. **Nobody's land** (rule 8). Owner `null`, status neutral: never blank. Cultures (`type: culture`) are states to you; the packer styles them.
9. **Certainty** (rule 9) is not a cell property; the packer reads `certainty[]` from the dossiers. Nothing to do.
10. **Labels, capitals and rulers** (rule 10). A `capital_move` event writes a `capitals` entry for the year from `identity.capitals` (the entry whose `from` is that year) and a caption. Labels and the ruler strip are the packer's.
11. **Pacing** (rule 11). Every ledger event in the window becomes a caption; the packer computes the size of each year's change from `changes`.
12. **The state page** (rule 12) is built by the packer from the dossiers and from the per-year area it sums from your file. Nothing to do.

**Keyframes versus the ledger.** A keyframe (as corrected by its `keyframe_review` entry: apply the `correction` spec when the verdict is adjust or wrong, the Cliopatria shape when ok) is the shape of record at its `from` year; the ledger moves the border between keyframes. So, in a keyframe's `from` year, after that year's ledger events, compare the state's cells with the corrected keyframe: where they differ by more than 20 cells or 5 percent of the state, set the state to the keyframe (changes with `event: "<slug>/keyframe/<shape_id>"`, `from` the previous holders) and record the difference in `handoff.notes` as a dossier gap ("the 757 keyframe removes Hexi but no ledger event between 705 and 757 loses it"). Small differences (coastline, one cell) are ignored. A keyframe whose `text` says it only changes the status (direct to vassal) sets the status, not the cells.

**Conflicts.** When two states claim a cell in a year and no event settles it, the state with the smaller Cliopatria area that year wins (the anchor compiler's rule), and the pair goes in `handoff.conflicts`. Never leave a cell with two direct owners.

**Resolution.** Resolve each region once and cache the cells in your scratch directory; a dossier's region that the gazetteer cannot resolve goes in `handoff.unresolved_regions` and the event is skipped (say so in `notes`), never guessed.

## 4. Order of work

1. Load the two anchors, the land grid and every dossier listed. Validate the dossiers you depend on (`python3 -I history/tools/validate_dossier.py <files> --resolve`); an invalid dossier is reported, not repaired by you.
2. Collect every event, keyframe start, state start and state end that falls in {{start_year}}..{{end_year}}, sorted by (year, month).
3. Check the start: the states alive in {{start_year}} and their cells must match the start anchor. Any difference goes in `handoff.notes`; the anchor wins.
4. Walk the years; apply section 3; write each year's `changes`, `contests`, `captions`, `capitals`.
5. Check the end: after {{end_year}}'s changes, compare every cell with the end anchor. Where they differ, append one change per state in {{end_year}} with `event: "anchor"` so that your last year equals the anchor, and list every such difference in `handoff.disagreements` with why (which dossier event or keyframe gave your answer). The seam must be clean even when you believe the anchor is wrong; the orchestrator decides.
6. Write the file; re-read it; run the seam self-check: replay the start anchor through your changes and assert it reaches the end anchor cell for cell, that no year has a cell with two direct owners, and that every `contest_end`, `occupation_end` and `vassal_end` closes something open.
7. Report (section 8).

The windows share one compiler so that 119 agents apply one reading of the rules. If `history/tools/compile_window.py` exists, use it (run `python3 -I history/tools/compile_window.py {{window}}`) and do not rewrite it; if it does not, you are the first and you write it generically (window id as its argument, the rules above as its body, the self-check included), under the shared-folder rules, so the others can run it. Fixes to it are small edits with a note at the top saying what changed and why; re-read before editing, read back after.

## 5. Where effort goes

Windows with no events are nearly empty and take minutes. The busy ones (the 1200s, every decade from 1790, both World Wars) carry hundreds of events; spend your effort on applying them in order and on the seam, not on prose. Where a dossier gives a front by year (the World Wars, the Taiping, the Eastern Front), the `occupation` and `contest` events already carry the yearly zones; apply them as they are.

## 6. The seam rule

Each of the 118 seams is checked by a seam agent that compares the last year of one window with the first year of the next: the same owner and status on every cell, the same open contests, occupations and vassal relations carried over, no caption lost or doubled at the boundary year. You make your seam clean by construction: your last year equals the end anchor; your `handoff.open_*` lists are exactly the relations open on 31 December of {{end_year}}; a caption belongs to the window that contains its year. The next window starts from the same anchor and the same open lists, so the seam holds unless one of you departed from the anchor. A seam that fails is sent back to both agents with the cells listed, and the pair is re-run until it is clean; nothing is accepted with a dirty seam.

## 7. Rules for the shared folder, and don'ts

`/mnt/project-files/history/` is a network mount other agents write to in parallel. Write only `history/compiled/{{window}}.json` (and `history/tools/compile_window.py` if you are the first); scratch in `/tmp/claude-0/work/window-{{window}}/`. Before changing a file that already exists there, re-read it; keep the edit small; about ten seconds after writing an existing file, read it back and re-apply your change if another writer replaced it. Delete temporary files you created there. Run Python that reads downloaded files with `python3 -I`; the machine has 15 GB of RAM and 4 CPUs shared with other builders, so load the grid and the dossiers once and keep one process under about 4 GB. Do not edit dossiers, anchors, tables or `colours.json`; do not write colours anywhere; do not touch the git repository at /home/claude/SkyscraperMaps; do not call any mcp__hearthbot__ tool; do not spawn subagents.

## 8. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "window": "{{window}}", "file": "history/compiled/{{window}}.json",
  "years_with_changes": 0, "cells_changed": 0, "events_applied": 0, "events_skipped": 0,
  "contests": 0, "occupations": 0, "vassal_relations": 0, "captions": 0,
  "keyframe_snaps": [{"slug": "...", "shape_id": "...", "cells": 0, "note": "..."}],
  "handoff_disagreements": 0, "conflicts": 0, "unresolved_regions": 0,
  "start_matches_anchor": true, "end_matches_anchor": true, "self_check_passed": true,
  "dossiers_invalid": ["<slug>"],
  "compiler": "used history/tools/compile_window.py | wrote history/tools/compile_window.py | patched it (what)",
  "problems": ["anything the orchestrator must know"]
}
```
