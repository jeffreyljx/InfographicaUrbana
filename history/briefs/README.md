# briefs/ : the agent briefs and the dossier schema

Written 18 Oct 2026 by the Phase A briefs agent, from history/master-plan.md. Every agent of Phases B and D, and the two cross-cutting agents, is run from one of these templates; the orchestrator (the master thread, running agents as workflows sixteen at a time) fills the placeholders and sends the filled brief as the agent's task. A thread that starts cold reads history/README.md first, then the brief it was given.

## Files

| File | For | Placeholders |
| --- | --- | --- |
| `dossier.schema.json` | The schema of one state's dossier (`history/polities/<slug>.json`), JSON Schema 2020-12, every field described, `additionalProperties: false` at the top level. The region grammar is `$defs/region`. Validate with `python3 -I history/tools/validate_dossier.py <file>` (`--resolve` also resolves every region through the gazetteer; `--json` gives counts). | none |
| `../polities/_example-tang-dynasty.json` | The worked example: a real Tang dossier (618-907) built from nineteen opened pages, 60 ledger events, 33 keyframe verdicts, 11 wars, validated. Researchers copy its habits. The underscore keeps it out of the dossier set; the East Asia group replaces it with `tang-dynasty.json`. | none |
| `research-brief.md` | One Phase B research group (76 groups, the roster in master-plan.md): the twelve rules and what each needs, the schema pointer, the region grammar, the sources rule, the owned and context polity lists, states Cliopatria lacks, where to write, the shared-folder rules, failed pages, the report. | `{{group_id}}`, `{{group_name}}`, `{{date}}`, `{{owned_polities}}`, `{{context_polities}}`, `{{orchestrator_notes}}` |
| `reviewer-brief.md` | One adversarial reviewer for a batch of dossiers: mechanical checks, the eleven reading checks (years in order, every gain matched by a loss, keyframe and ledger consistency, area sanity, every event sourced and spot-checked), verdicts and fixes, the cross-dossier matrix, the report. | `{{batch_id}}`, `{{date}}`, `{{dossiers}}`, `{{neighbour_dossiers}}` |
| `window-brief.md` | One Phase D rendering agent for a century (before 1600) or a decade (from 1600): its inputs, the two anchors, the twelve rules applied mechanically, keyframes versus the ledger, the output file `history/compiled/<window>.json`, the seam rule, the shared compiler, the report. | `{{window}}`, `{{start_year}}`, `{{end_year}}`, `{{start_anchor}}`, `{{end_anchor}}`, `{{previous_window}}`, `{{next_window}}`, `{{date}}`, `{{dossiers}}`, `{{resolution_note}}` |
| `colour-brief.md` | The colour agent (cross-cutting): the registry and tools, the rules, new slugs to seed, clashes to resolve, the report. | `{{date}}`, `{{trigger}}`, `{{new_slugs}}`, `{{clashes}}` |
| `gazetteer-brief.md` | The gazetteer agent (cross-cutting): the files and tools, the dossiers to resolve, names reported missing, the tasks (find, add, check sizes, border bands, compile the resolved table, document), the report. | `{{date}}`, `{{trigger}}`, `{{dossiers}}`, `{{names_needed}}` |

## How the orchestrator fills a brief

1. Copy the template and replace every `{{placeholder}}`; nothing else in the text changes, so that every agent of a kind reads the same rules. Leave no placeholder unfilled: an empty list is written as "none".
2. `{{date}}` is the run date, YYYY-MM-DD; `{{group_id}}`, `{{batch_id}}` and `{{window}}` are short ids used in file names (`polities/_notes/<group-id>.md`, `polities/_notes/review-<batch-id>.md`, `compiled/<window>.json`), so they contain only lower-case letters, digits and hyphens.
3. `{{owned_polities}}` and `{{context_polities}}` are Markdown tables built from `history/data/polities.csv`, one row per Cliopatria Name the group owns or should read: `slug | Cliopatria Name | first..last | shapes | max area (km2) | Wikipedia title | known problems (from data/README.md)`. Umbrella rows (`rel-...`) are listed in a separate line as context, never as owned. A group's owned list is the roster's region and era split; its context list is the union of the owned polities' `neighbours[]` from `history/data/polities/<slug>.json` that belong to other groups.
4. `{{dossiers}}` and `{{neighbour_dossiers}}` are lists of paths (`history/polities/<slug>.json`), one per line. For a window, the dossiers are every state whose life overlaps the window (`identity.start.year <= end_year` and `identity.end.year >= start_year`), read from the accepted dossiers.
5. Windows: `{{window}}` is the anchor stem of the window's first year (`m0700` for the century 700 to 601 BCE; `p1790` for the decade 1790 to 1799); `{{start_anchor}}` is the same stem; `{{end_anchor}}` is the stem of the year after `{{end_year}}` (`m0600`, `p1800`), and `p2024` for the last window (2020 to 2029, where 2024 is the last year with data). 76 centuries from `m6000` to `p1500`, 43 decades from `p1600` to `p2020`. `{{previous_window}}` and `{{next_window}}` are the neighbouring stems ("none" at the ends). `{{resolution_note}}` says "H3 resolution 5 everywhere" until the resolution-6 regions are introduced, then names them.
6. `{{trigger}}` for the cross-cutting agents says what prompted the run ("Phase B batch 3 accepted: 41 new slugs" or "seam check 1790/1800: 3 clashes").
7. `{{orchestrator_notes}}` carries anything specific to the group: rows already known to be wrong, a predecessor group's report, a deadline.
8. The task message is the filled brief, verbatim, with the builder rules the orchestrator gives every agent (the shared-folder rules, the slug rule, the region grammar, the machine limits) and the sentence "Your final message is the structured report the brief asks for". The report comes back as one JSON object; the orchestrator stores it under `history/notes/<phase>/<id>.json` and routes its lists: `new_slugs` to the colour agent, `gazetteer_names_needed` to the gazetteer agent, `counterparts_needing_dossiers` to the owning group, `pages_failed` and `gaps` to the gap-fillers, `problems` to itself.

## Quality gates (master-plan.md, "Orchestration")

A dossier is accepted only after its reviewer passes it; a reviewer's `fix` goes back to the author and `thin` to a gap-filler, until a round adds nothing. A window is accepted only when both its seams are clean. The site ships only after the visual QA list has been read and every difference is explained.

## Changing a brief

The rules in the briefs are the master plan's; a change to a rule is a change to the plan first. The schema, the resolver (`history/tools/gazetteer.py`), the validator and the briefs share the region grammar and change together or not at all. Re-read a brief before editing it (other builders write to this folder), keep the edit small, and read it back about ten seconds later.
