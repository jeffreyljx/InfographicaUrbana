# data/patches/: the window agents' corrections

Each of the 119 window agents (76 centuries up to 1599, 43 decades from 1600) reviews its window's
draft (`compiled/_draft/<window>.json`) against sources and the picture (`tools/render_year.py`), and
records its corrections here, in **one file per window**: `data/patches/<window>.json`. The window ids
are the drafts' file names: `m6000-m5901` ... `m0100-m0001`, `p0000-p0099` ... `p1500-p1599`,
`p1600-p1609` ... `p2020-p2029`.

Corrections cannot go into the dossiers (`polities/<slug>.json`): 119 agents writing to the same shared
dossiers would collide. Instead `tools/compile_dossiers.py` reads every patch file on each compile and
applies it on top of the dossiers, in memory; nothing is written back. Seams between windows stay clean
by construction: the compile runs once over all years, and its self-check replays every window to its
end anchor.

Write only your own window's file. A file that does not exist is fine (no corrections); this README is
not a patch.

## The file

```json
{
  "window": "p1200-p1299",
  "events": [ ... ],
  "keyframe_overrides": [ ... ],
  "rulings": [ ... ]
}
```

Every key is optional. `"window"` is informational (the file name decides); `"note"` may hold free text.
Entries are referred to by kind and position: `data/patches/p1200-p1299.json: events/0` is the first
event. Do not reorder or delete entries others may cite; to withdraw one, replace it by a corrected one
and say so in its note or why.

### events: extra ledger events

A ledger event exactly as in a dossier (`briefs/dossier.schema.json`, `ledger` items), plus `slug`, the
dossier it belongs to: `{slug, year, month?, type, counterpart, region, note, source, confidence}`. It is
applied exactly as if it were in that dossier's ledger, after the dossier's own events of the same year
and month (an event without a month takes the month of the dossier's last event that year).

- `type`: any ledger type except `found` and `dissolve` (a state's life span belongs to its dossier; ask
  for a dossier fix instead).
- `year` must lie inside the state's life (`identity.start.year` .. `identity.end.year`).
- `region`: a region spec with `text`, resolved through `tools/gazetteer.py`; a spec that does not
  resolve rejects the event (try a spec with `python3 -I tools/gazetteer.py resolve '<json spec>'`; `names <text>`
  searches the name lists).
- `counterpart`: the other party's slug (or name, or `nobody`), as in a dossier.
- `source`: the URL of the page the event rests on (it need not be in the dossier's `sources`).

Example: Batu's conquest of Volga Bulgaria, which the ulus of Jochi's ledger lacks.

```json
{"slug": "ulus-of-jochi", "year": 1236, "month": 10, "type": "gain", "counterpart": "volga-bulgaria",
 "region": {"region": "Volga Bulgaria", "text": "Batu's army 'crossed the Volga and invaded Volga Bulgaria in 1236'"},
 "note": "Bilär and the Bulgar towns fell in the autumn of 1236; the land passed to Jochi's ulus.",
 "source": "https://en.wikipedia.org/wiki/Mongol_invasion_of_Volga_Bulgaria", "confidence": 3}
```

### keyframe_overrides: replace a keyframe verdict

A `keyframe_review` entry as in a dossier, plus `slug`, with `why` in place of `note`:
`{slug, shape_id, verdict, correction, source, why}` (and `from`, `to` for a new keyframe). It replaces
that dossier's entry for the same `shape_id`; when the dossier has none, it is added as a new keyframe.

- `verdict`: `ok` (the Cliopatria shape as drawn), `adjust` or `wrong` (both need `correction`, the whole
  corrected shape as a region spec with `text`).
- `shape_id` must belong to the dossier (its slug or one of its `cliopatria_names`); an id absent from
  `data/shapes.csv` is a new keyframe and needs `from`, `to` and `correction`. A replaced entry keeps its
  `from` and `to` when the override gives none.
- When two windows override the same keyframe, the first file in window order wins and the other is
  reported. A keyframe often spans several windows: agree with the neighbouring window before
  overriding one that starts outside yours.

Example: the 1241 shape of the ulus of Jochi drawn without the North Caucasus.

```json
{"slug": "ulus-of-jochi", "shape_id": "ulus-of-jochi_1241", "verdict": "adjust",
 "correction": {"union": [{"region": "Kazakh Steppe"}, {"region": "Volga region"}, {"region": "Pontic Steppe"},
                          {"region": "Crimea"}, {"region": "Urals"}, {"region": "Khwarezm"}],
                "text": "the steppe from the Irtysh to the Dniester; the North Caucasus was raided, not held, until 1245"},
 "source": "https://en.wikipedia.org/wiki/Golden_Horde",
 "why": "The dossier's correction adds the North Caucasus from 1241; the page dates its submission to 1245."}
```

### rulings: settle a pair's conflict

`{years: [first, last], a, b, winner, status?, suzerain?, region?, source, why}`. Two states both claim
cells (a `found` or keyframe of one against land the other holds: the draft's `handoff.conflicts` and
the window packet list them); a ruling names the winner for those years.

- `a`, `b`: the two dossiers (order does not matter); `winner`: `a` or `b`.
- `years`: inclusive. The ruling acts only in years where the two actually conflict.
- `region` (optional): a region spec (gazetteer); the ruling then applies only to the conflict's cells
  inside it, otherwise to every cell both claim. Of several rulings for one pair and year, those with a
  region apply first (to their cells), then one without.
- `status` (optional): `vassal` or `constituent` (with `suzerain`, the overlord's slug), `occupied`
  (with `suzerain` = the occupier), or `contested` (blended with the loser). The cells the winner gets or
  keeps under the ruling take that status, in a relation flagged `"ruling"` that closes at the start of
  the year after `years[1]` (or when a party ends). This overrides a vassal tint the dossiers give those
  cells while it lasts.
- `source`: the URL the ruling rests on; `why`: one or two sentences.

Order in the conflict rule (`notes/phase-c/README.md`): an event of the same year that moved the cell
settles it first; then R2 (succession), **then rulings**, then R3 (hierarchy), rule 4 (a vassal keeps its
land), R1 (colonies) and the size rule. So a ruling cannot overturn a successor's claim (R2); everything
below it, it can.

Example: after the Treaty of Paris (1259) Henry III held Gascony as a vassal of the King of France; the
size rule gives it to France whenever France's keyframe claims it.

```json
{"years": [1259, 1293], "a": "kingdom-of-england", "b": "kingdom-of-france", "winner": "kingdom-of-england",
 "status": "vassal", "suzerain": "kingdom-of-france",
 "region": {"region": "Gascony", "text": "the duchy of Gascony"},
 "source": "https://en.wikipedia.org/wiki/Treaty_of_Paris_(1259)",
 "why": "Henry III kept Gascony as a fief of Louis IX from 1259 until the confiscation of 1294."}
```

## How the compiler checks a patch

Every entry is checked as `tools/validate_dossier.py` checks a dossier: the schema of a ledger event or a
`keyframe_review` entry (with `slug`, and `why` for `note`), the semantic checks that apply (the year in
the state's life, the shape's owner, `from` and `to` for a new keyframe), and every region spec through
the gazetteer. The `slug`, `a`, `b`, `winner` and `suzerain` must be dossiers the compile uses (one that
fails validation is left out of the compile, and its patches with it). **A bad entry is skipped and
reported, never fatal**; so is an unreadable file or a file whose name is not a window id. Entries dated
outside their window are applied, with a note.

## Where the results show

- `notes/phase-c/patches_check.csv`: every entry, applied or skipped and why; for a ruling, the
  cell-years it settled (or that it settled nothing).
- `notes/phase-c/windows/<window>.md`: the window's packet lists its patch entries and the rulings in
  force.
- The draft: a change made by a patch event has `"event": "data/patches/<window>.json: events/<k>"`,
  its caption `"patch": "<window>"`; a keyframe override shows as
  `<slug>/keyframe/<shape_id> [data/patches/<window>.json: keyframe_overrides/<k>]` in changes and
  `keyframe_snaps` (`"patch"`); a conflict a ruling settled has the rule
  `ruling of data/patches/<window>.json: rulings/<k>: <why>`, and a status it set comes with a relation
  flagged `"ruling"` in `open_vassals`, `open_occupations` or `open_contests`.
- `tools/render_year.py <year>` draws the result.

A patch takes effect at the next compile (`python3 -I tools/compile_dossiers.py`, run by the
coordinator). Before that, check it yourself (next section).

## Checking your patch

Three commands. Run them from the history folder (from anywhere else, give the tools' full path). None
of them writes into the history folder: each writes only into the folder you give it, and caches under
`/tmp/claude-0/work/` (the compiler's shared caches there are read, never written), so four window
agents can run them at once, each with its own folder.

The window argument is a window id such as `p1910-p1919`, meaning `data/patches/p1910-p1919.json`, or
the path of a file named `<window>.json` kept elsewhere (your draft in your own folder), which then
stands in for that window's file. `--patches DIR` reads another patches folder.

**1. Check the entries**: a few seconds, no compile.

```
python3 -I tools/compile_dossiers.py --check-patch p1910-p1919
python3 -I tools/compile_dossiers.py --check-patch /tmp/claude-0/work/<you>/p1910-p1919.json
```

It loads the one file and checks every entry as the compile would (above), against the dossiers as they
are now. One line per entry, then a summary:

```
events/0                 tibet                                    ok
events/1                 tibet                                    ok (note: year 1700 is outside the window 1910..1919)
events/2                 no-such-state                            REJECTED: slug 'no-such-state' is not a compiled dossier (...)
keyframe_overrides/0     russian-state                            REJECTED: a new keyframe needs a correction describing the shape
rulings/0                french-equatorial-africa|german-africa   ok
.../p1910-p1919.json: 5 entries, 3 ok, 2 rejected; checked in 2.9 s (rejected entries are skipped by the compile)
```

A line `note: dossier <slug> fails tools/validate_dossier.py` names a dossier your entries use that the
compile leaves out. Exit code 0 when every entry is ok; 1 when one is rejected (or the file is not
JSON, or its name is not a window id); 2 when there is no such file. It does not tell you the effect
(whether a ruling settles anything, where a keyframe lands): for that, the trial.

**2. Trial compile**: about 75 s and 1.1 GB for a late window, less for an early one.

```
python3 -I tools/compile_dossiers.py --trial p1910-p1919 --stage /tmp/claude-0/work/<you>/stage
python3 -I tools/compile_dossiers.py --trial /tmp/claude-0/work/<you>/p1910-p1919.json --stage /tmp/claude-0/work/<you>/stage
```

It compiles from the start (-6000) to the window's last year, with every patch file of the folder (your
file in place of the window's own) and the dossiers as they are now, and writes only into the stage
folder DIR (which must be outside the history folder):

- `DIR/compiled/_draft/<window>.json`: the window's draft;
- `DIR/data/anchors-c/<start>.json` and `<end>.json`: the anchors at the window's start and at
  1 January after its last year;
- `DIR/notes/phase-c/patches_check.csv`: every entry of every patch file, applied or skipped and why,
  and the cell-years each ruling settled;
- `DIR/notes/phase-c/windows/<window>.md`: the window's packet;
- `DIR/polities/` (its copy of the dossiers) and `DIR/cache/` (what the shared caches lack).

It prints the window's patch entries (applied or skipped; for a ruling, the cell-years it settled), then
what changed against the published draft, before and after: the conflict pairs and the keyframe snaps
whose figures differ, and how many cells of the end anchor change owner or status. Dossier edits made
since the published compile show there too, not only your patch. It never publishes. Reuse the same DIR
for the next trial: its earlier outputs are replaced, its copy of the dossiers is refreshed (only what
changed; `--no-sync` skips that) and its caches kept.

**3. Draw it**: a few seconds.

```
python3 -I tools/render_year.py 1914 --from /tmp/claude-0/work/<you>/stage --bbox 5,-8,25,12 --highlight german-africa,french-equatorial-africa
```

`--from DIR` reads the stage's anchors and draft instead of the published ones, so it draws the years
of the trial's window (`--jan1` of its first year uses the start anchor). The image goes to
`DIR/render/<year>.png` unless `--out` says otherwise; the path is printed. The other options are in
`python3 -I tools/render_year.py --help`.
