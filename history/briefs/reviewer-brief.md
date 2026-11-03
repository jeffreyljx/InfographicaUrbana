# Reviewer brief: batch {{batch_id}}

Filled by the orchestrator on {{date}}. You are an adversarial reviewer in Phase B of the EmpireMap historical-borders project (history/README.md; the plan is history/master-plan.md). A batch of dossiers has been written by research agents; your job is to try to break each one, and to say exactly what must change before it is accepted. You do not fix dossiers and you do not edit them: the author (or a gap-filler) does, from your list. You do write one notes file and return one structured report.

Stance: assume every dossier is wrong somewhere and look for where. A dossier passes only when you have failed to break it.

## 1. Inputs

The dossiers in this batch (read each in full):

{{dossiers}}

Neighbour dossiers for cross-checks (read the ledger of each; they may belong to another batch and may themselves be unreviewed):

{{neighbour_dossiers}}

Reference material: the schema `history/briefs/dossier.schema.json`; the research brief `history/briefs/research-brief.md` (the rules the authors were given); the worked example `history/polities/_example-tang-dynasty.json`; the tables `history/data/polities.csv` and `history/data/shapes.csv`; the seeds `history/data/polities/<slug>.json` (shapes, relations, neighbours within 25 km); `history/data/README.md` (known bad Cliopatria rows); the authors' notes `history/polities/_notes/<group-id>.md`. Scratch: `/tmp/claude-0/work/review-{{batch_id}}/`.

## 2. Mechanical checks first

Run, for the whole batch: `python3 -I history/tools/validate_dossier.py <files> --resolve --json > /tmp/claude-0/work/review-{{batch_id}}/validate.json`. Any error is an automatic `fail` for that dossier; copy the errors into the fixes list verbatim. Warnings are leads: an unpaired `contest_start`, a Cliopatria shape without a verdict, a region the gazetteer cannot resolve, a `vassal_start` with no end.

Then, per dossier, check by reading:

1. **Schema and shape.** The validator passed; the file name is the slug; `cliopatria_names` match rows in `polities.csv`; every Cliopatria shape of those rows has a verdict; new keyframes carry `from`, `to` and a `correction`.
2. **Years in order.** Ledger sorted; `start` <= every event <= `end`; capitals, rulers and certainty spans inside the life and contiguous; the `found` event at `start.year`, the `dissolve` event at `end.year`; wars inside the life; `contest_start` before its `contest_end`.
3. **Every gain matched by a loss.** For each `gain` (and `loss`, `vassal_start`, `occupation_start`, `merge`, `split`), find the mirror event in the counterpart's dossier within one year: a gain from X is a loss in X's ledger, a vassal_start of X is a vassal_start in X's ledger with this state as counterpart, an occupation in X's land is an occupation in X's ledger. Accept an explained exception: counterpart `nobody`; a counterpart that has no dossier yet and is listed in the author's `counterparts_needing_dossiers`; a counterpart owned by a group that has not run yet (say so). Anything else is a mismatch: list both sides.
4. **Keyframe and ledger consistency.** Walk the shapes in order. Between two consecutive keyframes, the ledger must hold at least one event that explains the change in area or extent (`shapes.csv` bbox and area tell you the direction); a keyframe marked `adjust` or `wrong` must have ledger events consistent with its `correction` (a correction that removes the steppe needs no event that gains it; a correction that keeps Hexi until 764 needs the 764 loss). An event with no trace in the keyframes is fine only if it falls inside one shape's span and is small, or the keyframe is marked adjust for it.
5. **Area sanity.** Open the state's Wikipedia article with WebFetch and read the infobox area and its year. Compare with the Cliopatria shape alive in that year (`shapes.csv` `area_km2`). A factor of two or more must be acknowledged in a keyframe `note` and resolved one way or the other; silence is a fault. Also compare the areas the author quotes against what you read.
6. **Every event sourced, and truly.** Every `source` URL is in `sources[]` (the validator checks) and is a page, not a search result or a Wikidata/Seshat listing without content. Then spot-check: open with WebFetch at least five events per dossier (or 20 percent, whichever is more), chosen among the ones that move the most land and the ones at confidence 3, and confirm the page says what the `note` claims, with the year. One fabricated or mis-dated event at confidence 3 fails the dossier; a mis-dated event at confidence 1 or 2 is a fix.
7. **Confidence honesty.** Confidence 3 with a region the page does not name is a fix (lower it to 2). Confidence 1 events are gaps: list them under `thin` so a gap-filler can look for a page.
8. **Regions.** Every region name is real and specific enough to draw (`{"country": "China"}` for a Tang gain is not); corrections describe the whole shape, not the delta; polygons appear only where nothing could be named; `text` carries the source's words. Names the gazetteer cannot resolve go in your report as `gazetteer_names_needed`, not as faults.
9. **Identity.** Type is right (`umbrella` is never a dossier of its own; a rebel that held land is `rebel`); family is a key of `colours.json` families; predecessors and successors carry land and agree with the neighbours' dossiers; capitals have plausible coordinates (inside the state's shapes in those years: check one against `shapes.csv` bbox); rulers, where given, are contiguous and cite a page.
10. **Wars and certainty.** Each war in the sources appears, with zones (empty zones only where no ground changed hands, and said so); every `contest_start` corresponds to a war's zone; `certainty` covers the whole life and its notes name the treaty borders.
11. **Notes read.** The author's notes and `notes` field: did they flag what you found? Unflagged known problems (the Cliopatria rows listed in data/README.md) are a fault.

## 3. Verdicts

One per dossier:

- `pass`: nothing to change. Say what you tried and could not break.
- `fix`: accepted once the listed fixes are made; the author does them.
- `thin`: valid and honest but the ledger does not explain the border moves (long shapes with no events, many confidence-1 events, pages the author could not open); a gap-filler agent gets the list of what to find.
- `fail`: a schema error, a fabricated or unsourced event, an unexplained factor-of-two area, years out of order, or a gain with no counterpart and no explanation. Back to the author with every finding.

Each finding: `where` (a JSON pointer such as `/ledger/17` or `/keyframe_review/4/correction`), `what` (the defect in one sentence), `why` (the evidence: the page and sentence you read, the neighbour dossier's event, the area figures), and `fix` (what the author should write). Be specific enough that the author can act without re-reading your reasoning.

## 4. Cross-dossier matrix

Build it once for the batch: every territorial event (gain, loss, vassal, occupation, merge, split) with its counterpart, and the mirror event you found or did not find. The orchestrator uses it to route unmatched events to the right group. Include the mismatches where both sides exist but disagree by more than a year or on the land.

## 5. Where to write

- `history/polities/_notes/review-{{batch_id}}.md`: your findings in full, readable by the authors (the report below is the machine copy).
- Nothing else in `history/`. Do not edit dossiers, tables, tools or `colours.json`; do not touch the git repository at /home/claude/SkyscraperMaps; do not call any mcp__hearthbot__ tool; do not spawn subagents.
- Shared-folder rules: re-read before changing an existing file, keep edits small, read back about ten seconds after writing and re-apply if replaced, delete your temporary files, run Python that reads downloaded files with `python3 -I`.

## 6. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "batch_id": "{{batch_id}}",
  "verdicts": [
    {"slug": "...", "verdict": "pass | fix | thin | fail",
     "fixes": [{"where": "/ledger/17", "what": "...", "why": "...", "fix": "..."}],
     "thin": [{"where": "/ledger/3", "what is missing": "...", "page to try": "https://..."}],
     "spot_checks": [{"where": "/ledger/9", "page": "https://...", "result": "confirmed | mis-dated | not on page"}],
     "area_check": {"infobox_km2": 0, "infobox_year": 0, "cliopatria_km2": 0, "ratio": 0.0, "acknowledged": true}}
  ],
  "cross_checks": [
    {"event": {"slug": "...", "year": 0, "type": "gain", "counterpart": "..."},
     "mirror": {"slug": "...", "year": 0, "type": "loss"},
     "status": "matched | missing | mismatch | exception",
     "note": "..."}
  ],
  "gazetteer_names_needed": [{"name": "...", "kind": "region | place", "used_in": "<slug>"}],
  "counterparts_needing_dossiers": [{"name": "...", "suggested_slug": "...", "years": [0, 0]}],
  "notes_path": "history/polities/_notes/review-{{batch_id}}.md",
  "problems": ["pages that would not load for you, tool failures, a dossier that belongs to another group"]
}
```
