# Review of batch eu-13-a (Duchy of Benevento, Duchy of Spoleto, Duchy of Tuscia)

Reviewer, 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-13-a.json.

Mechanical: all three validate with 0 errors and 0 warnings (--resolve), before and after the reviewer's edits. Neighbour dossiers read: kingdom-of-the-lombards, kingdom-of-italy-medieval, kingdom-of-italy (1861-1946), lombards, eastern-roman-empire, byzantine-empire, holy-roman-empire, kingdom-of-the-franks (plus capua, catepanate-of-italy). Not yet written (eu-13 groups that have not run): papal-states, principality-of-salerno, principality-of-capua, norman-italy, duchy-of-naples.

Pages opened by the reviewer: Pandulf Ironhead, Principality of Benevento, Principality of Salerno, Catepanate of Italy, Duchy of Benevento, Duchy of Spoleto, Lambert (Holy Roman Emperor), Guy III of Spoleto, Aistulf, Duchy of Tuscia, Kingdom of the Lombards. No infobox gives an area for any of the three states (confirmed).

## Edits made by the reviewer (applied, re-validated)
- All three: `kingdom-of-italy` (the 1861-1946 dossier) re-pointed. Lombard-era uses -> `kingdom-of-the-lombards` (Benevento /ledger/2-3, /wars/1; Spoleto /ledger/1-3, /wars/1-4; Tuscia successor). Berengar-era uses -> `kingdom-of-italy-medieval` (Spoleto successor, /ledger/10-11, /wars/6-7).
- Benevento /ledger/14: counterpart 'Thrasimund IV of Camerino' (a person) -> `holy-roman-empire` (Otto II disposed of Spoleto in 981, as Otto I did in the 967 gain).
- Spoleto /ledger/11 (898 dissolve): confidence 3 -> 1. Lambert's death on 15 October 898 is on the page, but the duchy goes on ('He was succeeded in Spoleto by Guy IV'; Alberic I, Boniface I, Theobald on the Spoleto page).

## duchy-of-benevento: thin
Spot checks, all confirmed on the page with the year: 774 princeps, 840 Siconulf (Salerno infobox 840-851), 899 Atenulf, 967 Spoleto and Camerino, 978 Salerno, March 981 partition, 981 Spoleto to Thrasimund IV, 1022 Henry II, 1040 Guaimar IV, 1078 Guiscard, 1081 return to the papacy. No fabricated events found.
Open findings (non-blocking):
- No keyframe for 788-792. Cliopatria's row skips those years and kingdom-of-the-franks_788 holds 152 Benevento cells; every other gap got a keyframe. Add duchy-of-benevento_788 (788-792, adjust, the 778 shape, Frankish suzerainty per the Principality infobox).
- /ledger/5 Chieti 778: the Principality page puts the annexation after the 788 invasion. Confidence 1 is honest, but the year contradicts the page. Find the year (try Grimoald III of Benevento) and move the event; the keyframes 778 and 793 then need Chieti until that year.
- Confidence-1 gaps for a gap-filler: 741 growth, 880 Apulia, the Capua shuttles of 990/1010/1015, the 1034 and 1040 slivers, the end of Guaimar's hold in 1047, the Byzantine hold of 891-895.

## duchy-of-spoleto: fail (back to the author)
Spot checks confirmed: found 571, 757-759 Desiderius, 776 Charlemagne, 877 Rome, 883 Camerino (Guy III page), 896 partition, 15 October 898.
Blocking:
1. Aistulf's direct rule is missing. Spoleto page: Aistulf took the duchy from Lupus, 'governing it directly through appointed officials'. Aistulf page: 'In the late spring or summer 751, Aistulf placed Spoleto under his direct control without naming a replacement duke' (Duke of Spoleto 751-756, then Alboin). kingdom-of-the-lombards /ledger/16 has the 751 gain at confidence 3. The 750-774 keyframe overrides Cliopatria's kingdom shape for years where Cliopatria is right. Add the 751 loss and the 756/757 gain back to/from kingdom-of-the-lombards, and split keyframe 750.
2. The Chieti gain is missing. Benevento /ledger/5 gives Chieti to Spoleto, but Spoleto has no gain. Its shape grows about 3.7k km2 (east edge 14.06 -> 14.77 E) between keyframes 778-841 and 842-859 with no event. Add the gain (same year as Benevento) and widen the 778-841 correction from that year.
Non-blocking:
- No event for the 775 loss of the northern strip (22,755 -> 19,694 km2). Add a confidence-1 loss or a thin note.
- The 571 start overlaps eastern-roman-empire, which loses the land in 577. Say so in the 571 keyframe note, or start in 576/577.
- The duchy runs to 1201-1226 on the page; extension after 898 is a gap-filler task.

## duchy-of-tuscia: fix (done by the reviewer)
Found 576, Lucca, and Gummarito 576-585 are confirmed on the Tuscia page. The 586 end is Cliopatria's: the Kingdom of the Lombards page has Authari crowned in 584. Confidence 1 is honest and thin by design for a 1-shape state.

## Cross-dossier routing
- byzantine-empire (eu-05): no mirror for Benevento 741 gain or 880 loss (Apulia).
- holy-roman-empire (eu-08): 970 loss should be 967; 990 gain should be 981 (Pandulf Ironhead page).
- kingdom-of-italy-medieval (eu-13): add a 896 loss to duchy-of-spoleto (Lambert's share after the Adda-Po partition); its 898-10 gain already mirrors the end.
- kingdom-of-the-franks (eu-07): its 778 gain of Spoleto and Spoleto's 778-859 gap keyframes double-claim the land. Make the 778 event a vassal_start (imperial fief, infobox 776-1201), or drop Spoleto's gap keyframes.
- kingdom-of-the-lombards: 751 gain of Spoleto awaits Spoleto's mirror (fix 1); the 577-741 growth of Spoleto has no KoL loss.
- Owed by eu-13 groups not yet run: principality-of-salerno, principality-of-capua, norman-italy, papal-states.
