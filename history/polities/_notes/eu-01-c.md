# Notes for batch eu-01-c (Greece, part c)

Written 2026-10-18 by the eu-01-c research agent. Six states: three kept from an earlier run (validated again, unchanged), three written in this run.

## Dossiers

| slug | status | years | events | sources |
| --- | --- | --- | --- | --- |
| peloponnesian-league | kept from an earlier run | -800..-192 | 61 | 20 |
| odrysian-kingdom | kept from an earlier run | -480..-281 | 21 | 11 |
| cimmerian-bosporus | kept from an earlier run | -480..527 | 25 | 19 |
| sacred-band-of-thebes | written now | -379..-362 | 17 | 6 |
| second-athenian-league | written now | -378..-338 | 19 | 5 |
| thebans | written now | -361..-338 | 6 | 6 |

Their own notes (history/polities/<slug>.json, field `notes`) carry the details for the kept three.

## Cliopatria rows that are not what their names say

- **Sacred Band of Thebes (-366..-351, 33,821 km2)** is the Theban sphere of the hegemony (Boeotia, central and western Greece, Euboea, Arcadia, Messenia, Thessaly, plus a Byzantium and an Izmir cell). The Sacred Band is a corps of 300 (Sacred Band page: founded 378/379, destroyed at Chaeronea 338). Dossier = the Theban state, -379 (liberation) to -362 (Mantinea).
- **Thebans (-350..-338)** is the same Theban state, Boeotia only. Kept as a second dossier because the brief lists both slugs, but the split between them is moved from Cliopatria's -351/-350 to Mantinea (-362/-361), where the Theban hegemony page ends the hegemony. The Cliopatria hegemony shape is not used after -362; -361..-351 is a new Boeotia-only keyframe in `thebans`. If the reviewer prefers one state: merge `thebans` into `sacred-band-of-thebes` with both Names in `cliopatria_names` (greek-city-states /ledger/42 would then name `sacred-band-of-thebes`).
- **Second Athenian League (-366..-338)** is Athens and its allies. Written as the Athenian state (Attica direct, allies as client tint) so that Attica is drawn. The league page ends the alliance in 355; the Chaeronea page dissolves the league in 338; Cliopatria's end (338) is kept and 355-338 is Athens's rump.

## Disagreements between pages

- Second Athenian League ends 355 (league page: "The alliance lasted until 355 BC") against dissolved after Chaeronea 338 (Chaeronea page).
- Plataea destroyed 373 (Theban hegemony page) against 372 (Second Athenian League page).
- Third Sacred War: "Amphictyonic League victory" with Thebes on the winning side (war page) against "Thebes lost its predominance in central Greece" (Thebes page).
- Restoration of the Boeotian League: "in short order" after 379 (Epaminondas page) against "In 374 BC, Pelopidas restored Theban dominance" (Boeotian League page).
- The Social War page says nothing on which allies stayed; the league page says "most of the allied cities became independent".

## Neighbour dossiers to reconcile (not edited by this batch)

- greek-city-states /ledger/31 (-366 loss to sacred-band-of-thebes of Messenia, Arcadia, Thessaly; confidence 1) and /ledger/37 (-350 gain; confidence 1): the pages date the Theban reach to -369..-362 and the end to -362 (vassal events in sacred-band-of-thebes).
- greek-city-states /ledger/28 (-377 loss to second-athenian-league): the league page's year is 378.
- greek-city-states /ledger/42 (-337 gain from thebans): thebans dissolves in August 338.
- macedonian-empire has no event for the Macedonian garrison at Thebes after Chaeronea (Chaeronea page: "installed a Macedonian garrison").
- odrysian-kingdom -360 gain and -357 loss against second-athenian-league are mirrored in the league's ledger (-360 loss at confidence 1 because the Cotys I page was not opened here; -357 gain at confidence 2 because the Cersobleptes page hedges: "seems to have been finally ceded").
- peloponnesian-league -370 contest_start / -369 contest_end against sacred-band-of-thebes are mirrored (no month: the page says "late in 370").

## Page budget

The brief allowed 1-2 pages for each of the three new states. Opened: Thebes (Greece), Theban hegemony, Epaminondas, Pelopidas, Sacred Band of Thebes, Boeotian League, Third Sacred War, Battle of Chaeronea (338 BC), Second Athenian League, Social War (357-355 BC), Cersobleptes: eleven pages for three states, because the Thebes, Theban hegemony and Boeotian League pages are silent on territory, dates of the alliances and area. Unverified (page budget): Argos, Tegea and Mantinea cells of the Theban shape; the Thracian and Chalcidian cells of the Athenian -366 shape (Abdera, Cardia, Torone, Amphipolis, Corfu); Mytilene and the Cyclades after 355; the year Euboea returned to Athens; when Phocis took the Boeotian cities (bridge date -347, confidence 1).

## Areas

No page opened gives an area for any of the three states (the Thebes infobox gives only the modern municipality, 830 km2; the Boeotian League infobox is garbled; the league page has no infobox figure). Cell counts instead: corrected Theban hegemony shape 95 cells (about 24,000 km2) against Cliopatria's 111 cells (33,821 km2); Boeotia 14 cells (about 3,500 km2) against the Thebans shape's 18 cells (5,164 km2); Athenian -366 shape corrected 104 cells; rump 38 cells.

## States needing a dossier from another group

athens (a state in its own right; the league dossier carries Attica only for -378..-338), phocis (held Delphi 356 and Boeotian cities c. 347-346), messene (-369 onward), arcadian-league (-369..-362), thessalian-league / Pherae of Alexander (-369..-364), the Euboean league or cities (-370..-338), and Chios, Rhodes, Kos and Byzantion (independent from 355, in the greek-city-states aggregate).

## Gazetteer names to add

Regions: Arcadia, Messenia, Laconia, Elis, Argolid, Thyreatis, Chalcidice. Places: Orchomenus, Coronea, Chaeronea (new in this batch); Tegea, Mantineia, Sikyon, Epidaurus, Phlius, Troezen, Megara, Decelea, Megalopolis, Gytheio (peloponnesian-league). The Athenian dossier uses only names that resolve.

## Pages that failed

None.
