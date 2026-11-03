# The colour registry and the colour tools

Written 18 Oct 2026 by the Phase A colours builder. The registry is `history/colours.json`; the
tools are `tools/colour.py` and its seed table `tools/colour_seed.py`. The rules the registry
implements are the master plan's (master-plan.md, "Colours"). Colours come only from the
registry: rendering agents read it, the colour agent changes it, nobody invents a hex.

## Files

| File | What |
| --- | --- |
| `colours.json` | The registry: `rules`, `families`, `wheel`, `fixed`, `assigned`, `assigned_meta`, `log` (below). |
| `tools/colour.py` | The library and the commands: OKLab maths, `seed`, `assign`, `check`, `set`, `show`, `swatch`, `synthetic`. No external package for the maths; `assign` and `check` need h3 (installed) and use numpy when present. Run with `python3 -I`. |
| `tools/colour_seed.py` | The seed table: the ~230 conventional states as OKLCH values with family, group and the note that says why; the families and the wheel spec; the minimum distance and its justification. `colour.py seed` turns it into the registry's `rules`, `families`, `wheel` and `fixed`. It is the record of the first seeding; after that the registry is the truth and `set` is how a colour changes. |
| `/tmp/claude-0/work/colours/` | Caches (the H3 neighbour table, the per-anchor adjacency, the polity table's neighbours) and the swatch sheet. Rebuilt automatically when missing or stale. |

## colours.json

- `rules`: the plan's colour rules in machine terms. `oklab_min_distance` (0.10) with `why`; the neighbour rule; the lifetime rule; `vassal` (tint: OKLCH chroma x0.55, lightness +0.12, own outline and label); `occupied` (owner's fill, occupier's hatch at 45 degrees, 7 px spacing, 2.5 px); `contested` (fill = OKLab midpoint of the two claimants, fine hatch at -45 degrees, 4 px spacing, 1 px, in the fill darkened by 0.18 L); `rebel` (own colour at the vassal tint, hatched in its own colour); `neutral` (nobody's land, warm grey `#d6d0c9`, OKLCH 0.86 / 0.012 / 75); `culture` (chroma x0.40, lightness +0.15, dotted fill, labelled as a culture); `expansion_outline`, `label` and `basemap`.
- `families`: `{family: {hue: [start, end], note}}`, OKLCH hue in degrees; `end < start` wraps through 0. A family is the hue range a state's successors and relatives draw from (Rome red to Byzantium Tyrian purple; the Chinese dynasties warm; Persia teal; the caliphates green). Families overlap in hue because they never touch (China and Rome both hold reds); the neighbour rule, not the family, keeps neighbours apart. A fixed entry whose hue sits outside its family's range says why in its note.
- `wheel`: 24 hues (every 15 degrees from 0) in three lightness variants, light (L 0.80, C 0.10), mid (L 0.70, C 0.12) and deep (L 0.58, C 0.13), chroma clipped to the sRGB gamut per hue; 72 colours with ids like `h120-mid`. Used for every polity without a fixed colour.
- `fixed`: one entry per Cliopatria row of a state whose colour follows convention: `{slug, name, hex, family, oklch, group?, note}`. 415 entries for 227 states. `group` names the state when several Cliopatria rows are one state (the thirteen French regimes, the Delhi Sultanate's four dynasties, the British colonial rows, Eastern Rome and Byzantium, the Northern and Southern Song): rows of one group share the colour and are never reported as a clash with each other.
- `assigned`: `{slug: {hex, wheel, min, neighbours, short?}}` for every other leaf polity in `data/polities.csv` (1,129): the wheel colour it took, its distance to the closest coloured neighbour over its whole life (`min`, null when it has none) and the number of distinct neighbours; `short: true` would mark a polity for which no wheel colour reached the minimum (none at present). `assigned_meta` records how the assignment was run.
- `log`: every change made through `set`: date, slug, from, to, note, and whether it was forced over a clash.

Slugs are `tools/slug.py` slugs as they stand in `data/polities.csv` (with the `-2` suffix where that table disambiguates: `han-2` is Liu Bang's Kingdom of Han). A rendering agent looks a colour up by slug in `fixed` first, then `assigned`; `colour.colour_of(slug)` does that.

## How the colours were chosen

Conventional colours first, as the plan says: Rome red, Byzantium Tyrian purple (a red-purple, so it neighbours Rome's red on the wheel), France blue for every French regime, England and Britain pink-red, Spain and Castile yellow-orange, Portugal green, the Ottomans olive (moved from green because Russia is dark green and they are neighbours), Russia dark green from Moscow to the Federation, the Mongols warm brown with the Golden Horde ochre and the Blue and White Hordes by name, the Chinese dynasties a warm family (Han vermilion, Tang gold, Song teal-green, Ming deep red, Qing imperial yellow, the PRC vermilion-red), the caliphates green with the Umayyads pale (white banner) and the Abbasids dark grey-green (black banner), Persia teal from the Medes to the Islamic Republic, the USSR deep red, Japan deep crimson, the USA navy-indigo, and so on through the families. Successors that claim continuity take a neighbouring hue of the same family (Western Rome crimson-orange beside Rome's red, Later Tang a deeper gold, the Nicaean Empire a lighter Byzantine purple); a dynasty change within a state keeps the colour (Tang and Wu Zhou, Han and Xin, the Delhi Sultanate's dynasties); an unrelated successor takes an unrelated hue (Yuan brown, Ming red).

Then the neighbour rule. `check` was run over every anchor year and the fixed palette tuned until every neighbouring pair cleared 0.10, moving the smaller or less conventional state each time; every move is recorded in the entry's note ("Hungary violet: the flag's green and red both collide with neighbours"; "Japan deep crimson: the USSR, the PRC, Austria's Tianjin concession and the British colonies hold the lighter reds and pinks around it"). Finally `assign` coloured the remaining 1,129 polities from the wheel.

Two states that never touch may share a colour (Rome and the Han are both red), but two contemporary states on one colour would confuse a legend, so `seed` also warns when two states whose lifetimes overlap are closer than 0.02 (none at present; 82 pairs sit between 0.02 and 0.03, printed as a count). A state in such a pair was moved within its family and the note says so (the Blue Horde deep slate blue because Sweden and Joseon hold the mid blues; the Kingdom of Jerusalem pale gold because Novgorod holds the pale rose).

## The commands

Run everything with `python3 -I` from any directory; the tool finds `history/` from its own path.

```
python3 -I tools/colour.py check                 # the neighbour rule over every anchor year
python3 -I tools/colour.py check --year 1600     # one year
python3 -I tools/colour.py check --ring 2        # also neighbours two cells apart (across a strait)
python3 -I tools/colour.py check --min 0.12      # a stricter trial threshold (the rule is not changed)
python3 -I tools/colour.py check --json out.json # the clash list as data
python3 -I tools/colour.py check --anchors DIR   # against another directory of {year, owners} files (the compiled windows)
python3 -I tools/colour.py show tang-dynasty     # colour, OKLCH, family, group, note and the tints
python3 -I tools/colour.py set SLUG '#rrggbb' --note "why"   # change one colour (refuses a clash; --force logs it)
python3 -I tools/colour.py assign                # recolour every non-fixed polity from the wheel
python3 -I tools/colour.py swatch [file.html]    # a swatch sheet of everything
python3 -I tools/colour.py distance A B | blend A B | tint HEX vassal | oklch HEX | hex L C H
```

`check` reports, for every pair of polities that touch in any anchor year and whose colours are closer than the minimum: the distance, the years, both colours, which is the smaller (by cells owned) and a concrete replacement for it (a fixed polity keeps its lightness and chroma and turns its hue inside its family; a wheel polity takes the best wheel colour), with the margin that replacement would have against every neighbour of its whole life. Pairs within one group are listed as intended. The exit code is 1 when there are clashes, so a window build can run it as a gate. It reads the anchors in `data/anchors/` (and, for the lifetime graph, the polity table's 25 km neighbours in `data/polities/*.json`); when the compiled windows exist, the same check runs against them by pointing it at a directory of `{year, owners}` files (`--anchors DIR`).

`assign` colours every polity without a fixed colour by greedy graph colouring over the union of every anchor year's adjacency graph (two polities are adjacent in a year when they own land cells that share an H3 edge, found with `h3.grid_ring(cell, 1)`), largest polity first (max cells over the anchors, else Cliopatria area), one colour for life. The lightness variant follows crowding: light for a small polity (under 150 cells) with four or more neighbours a year, deep for a large (3,000 cells or more) or isolated one, mid otherwise; within the variant the hue with the best margin against the already-coloured neighbours wins, ties to the least-used hue, and the other variants are tried before a polity is marked short. The fixed colours are pre-coloured nodes, so a wheel colour never clashes with a convention. Re-running `assign` recolours every non-fixed polity from scratch, so it is a Phase A tool: once the windows are being compiled, colours change only through `set`.

## How the colour agent changes a colour

Only through the tools, never by editing a hex in `colours.json` by hand and never in a window file (`compiled/*.json` carries slugs, not colours; the packer reads colours from the registry at packaging time).

1. `check` names the clash, the smaller state and a replacement that clears every neighbour of that state's whole life.
2. `set SLUG HEX --note "why"` makes the change. It refuses a hex that would clash with any lifetime neighbour and prints them; `--force` overrides and records that it did. A fixed entry keeps its family and group and gets the change appended to its note; an assigned entry becomes `wheel: "manual"`. Every change goes into `log`.
3. `check` again. A recoloured state is recoloured everywhere, in every year, so the colour-for-life rule holds; a window agent that already rendered that state re-reads the registry at the next packaging pass.

A state that is split by the research agents (Cliopatria's Kingdom of Italy 587..1946, Georgia 567..2024, Later Zhou -750..960) needs a fixed entry per new slug: add it to `fixed` with `set` after the new slug exists in `polities.csv` (`set` on an unknown slug is refused), or, before Phase B closes, add it to `colour_seed.py` and re-run `seed --force` then `assign`. Rows of one state share a `group`; put a new row of an existing state into that group so it inherits the colour and is never reported against its siblings.

The seed is the record of the first colouring. After `seed`, the registry is the truth: `seed --force` rewrites `rules`, `families`, `wheel` and `fixed` from the table and keeps `assigned` and `log`, so run it only when the seed table itself has been corrected, then `check`.

## The minimum distance

0.10 in OKLab (see `rules.why` for the full measurement). About five just-noticeable differences; Tableau 10's closest pair is 0.084; on the wheel, neighbouring hues (15 degrees) are 0.025 to 0.038 apart, hues 60 degrees apart 0.10 to 0.13, and the lightness variants 0.10 to 0.12 apart, so 0.10 means a different hue family or a clearly different lightness. The wheel holds 17 mutually distinct colours at 0.10; the greedy colouring clears 0.10 for every polity (and 0.12 for all but 3), while the conventional palette would lose 57 neighbouring pairs at 0.12. Every fixed and wheel colour keeps at least 0.107 from the neutral grey and 0.18 from a pale basemap, and the vassal tint sits 0.12 to 0.15 from its suzerain.

## Known limits

- Adjacency is sampled at the 120 anchor years plus the polity table's 25 km neighbour spans; a border that exists only between anchors is covered by the second source but not checked year by year until the compiled windows exist.
- Cliopatria artefacts make some neighbours: the Tianjin concessions put Austria-Hungary, Japan, Italy and Russia side by side in 1910; the Kingdom of Italy row runs from the Lombards to 1946; the Chinese Communist Party row of 1938-45 overlaps the USSR. The palette clears them anyway; splitting those rows will loosen it.
- The check compares full colours. A vassal tint against a neighbour's full colour, or two contested blends side by side, is not checked; the hatch and the outline carry that case.
- `assign` is deterministic for a given registry and anchor set; a changed anchor set can change many wheel colours, which is why it is a Phase A tool.
