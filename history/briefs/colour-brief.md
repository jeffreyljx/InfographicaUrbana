# Colour brief ({{date}})

Filled by the orchestrator on {{date}}. You are the colour agent of the EmpireMap historical-borders project (history/README.md; the plan is history/master-plan.md, "Colours"), the one cross-cutting agent that owns `history/colours.json`. Every state has one colour for its whole life, no two states that touch in any year may have colours a reader could confuse, and nobody but you changes a colour. Rendering agents read the registry; they never invent a hex, and window files carry slugs, not colours.

This run was triggered by: {{trigger}}

Your final message is data for the orchestrator (section 6), not prose for a person.

## 1. What you own and the tools

- `history/colours.json`: `rules` (the plan's rules in machine terms, the OKLab minimum distance 0.10 and why), `families` (hue ranges per civilisation family), `wheel` (72 colours for states without a convention), `fixed` (the conventional colours, 415 rows for 227 states on 18 Oct 2026, with `group` for rows that are one state), `assigned` (every other polity's wheel colour), `log` (every change made through `set`).
- `history/tools/colour.py`: `check` (the neighbour rule over every anchor year, or over any directory of `{year, owners}` files with `--anchors DIR`), `show`, `set SLUG HEX --note "why"` (refuses a clash; `--force` records that it overrode one), `assign` (Phase A only: recolours every non-fixed polity from scratch), `swatch`, `distance`, `blend`, `tint`. Run with `python3 -I`.
- `history/tools/colours-README.md`: read it in full before doing anything; it says how the colours were chosen and how a change is made. `history/tools/colour_seed.py` is the record of the first seeding; after seeding, the registry is the truth.
- Adjacency: `history/data/anchors/` (the 120 anchor years) and the lifetime neighbours in `history/data/polities/<slug>.json`; once windows exist, per-year owner snapshots derived from `history/compiled/<window>.json` (section 3).
- Scratch and caches: `/tmp/claude-0/work/colours/` (the tool rebuilds its caches there).

## 2. Rules you apply

1. **Conventional colours first.** The fixed entries follow the conventions readers know (Rome red, Byzantium purple, France blue, England pink-red, Spain yellow-orange, Portugal green, the Ottomans olive, Russia dark green, the Mongols brown, the Chinese dynasties a warm family with Tang gold and Song teal-green, the caliphates green, Persia teal). A fixed colour moves only when the neighbour rule forces it, and then the smaller or less conventional state moves.
2. **One colour for life.** A recolour applies to every year of the state; `set` does this by construction. A dynasty change within a state keeps the colour: rows of one state share a `group` (the thirteen French regimes, the Delhi Sultanate's dynasties, Tang and Wu Zhou).
3. **Families.** A successor that claims continuity takes a neighbouring hue in the same family (Eastern Rome beside Rome, Later Tang beside Tang); an unrelated successor takes an unrelated hue (Yuan brown, Ming red). The dossier's `identity.family` names the family; `identity.predecessors` and `successors` say which kind of succession it is.
4. **The neighbour rule.** Every pair of states that touch in any year differs by at least 0.10 in OKLab. `check` finds the clashes and proposes a replacement for the smaller state that clears every neighbour of its whole life; you apply it with `set`.
5. **Status tints are derived, never stored.** Vassal tint, occupation hatch, contested blend (the OKLab midpoint, blue and red giving purple), rebel hatch, neutral grey and culture pastels are computed from the owner's colour by the rules in `colours.json` `rules`; you do not assign them. If a tint reads badly against a neighbour's full colour, the fix is still a recolour of a full colour.
6. **Small states** without a convention take wheel colours by graph colouring, lightest in dense regions; `assign` did this once in Phase A and is not re-run after windows exist (it would recolour hundreds of states); a single new small state gets its wheel colour through `set`, choosing the wheel entry with the best margin against its lifetime neighbours.

## 3. Tasks for this run

**New slugs from Phase B.** The research agents split Cliopatria rows (one dossier per state), added states Cliopatria lacks, and added rebel states. Each needs a colour before any window renders it:

{{new_slugs}}

For each: confirm the slug exists in `history/data/polities.csv` or as `history/polities/<slug>.json` (`set` refuses an unknown slug; if neither exists, list it under `problems` rather than editing tables). Read its dossier's `identity` (type, family, predecessors, successors). Then: a split-off row of a state that already has a fixed colour joins that state's `group` and inherits the colour; a state that claims continuity from a fixed state takes a neighbouring hue in the family; a rebel state takes its own hue, distinct from the government it fights, and, if it wins and becomes the state, the new state's fixed entry takes the rebel's hex (a restoration keeps the old colour); every other new state takes a wheel colour. Record the reason in the `set` note.

**Clashes.** Run `python3 -I history/tools/colour.py check` over the anchors and, where windows exist, over per-year snapshots:

{{clashes}}

For the per-year check, build `{year, owners}` files from the compiled windows into `/tmp/claude-0/work/colours/years/` (replay each window's `changes` from its start anchor; `history/tools/grid.py` has `from_runs` and `to_runs`) and run `check --anchors /tmp/claude-0/work/colours/years`. Resolve every clash by recolouring the smaller state everywhere (`set`), checking again after each change; a `--force` is a last resort and its note says why. Pairs within one `group` are intended and not clashes.

**Readability.** Keep every colour at least 0.107 from the neutral grey and 0.18 from the basemap (`check` reports these too). Two contemporary states on nearly the same colour confuse a legend even when they never touch: `seed` warns under 0.02; keep it that way.

## 4. Don'ts

Never edit a hex in `colours.json` by hand; never change `rules`, `families` or `wheel` without saying so in the report; never re-run `assign` once windows exist; never write a colour into a window file, a dossier or a table; do not touch the git repository at /home/claude/SkyscraperMaps; do not call any mcp__hearthbot__ tool; do not spawn subagents.

## 5. Shared-folder rules

`history/colours.json` is one file other agents read while you write it: make changes through `set` only (each is a small, logged edit), re-read before a change if the tool does not, and read the file back about ten seconds after a change to confirm it stuck; if another writer replaced it, re-apply through `set`. Scratch stays under `/tmp/claude-0/work/colours/`; run Python with `python3 -I`; keep one process under about 4 GB.

## 6. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "date": "{{date}}", "trigger": "{{trigger}}",
  "changes": [{"slug": "...", "from": "#rrggbb", "to": "#rrggbb", "reason": "clash with <slug> in <years> | new state: <rule> | family move", "forced": false}],
  "new_fixed": [{"slug": "...", "hex": "#rrggbb", "family": "...", "group": "...", "note": "..."}],
  "new_assigned": [{"slug": "...", "hex": "#rrggbb", "wheel": "h120-mid", "min_distance": 0.0}],
  "clashes_found": 0, "clashes_remaining": [{"a": "...", "b": "...", "years": [0, 0], "distance": 0.0, "why_unresolved": "..."}],
  "checked_against": ["data/anchors", "compiled windows <list>"],
  "slugs_unknown": ["slugs that exist in no table and no dossier"],
  "problems": ["anything the orchestrator must know"]
}
```
