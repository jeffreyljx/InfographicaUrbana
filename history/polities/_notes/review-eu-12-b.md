# Review of batch eu-12-b (Iberia and the taifas, part b)

Reviewed 2026-10-31 by the adversarial reviewer. Dossiers: county-of-urgell, county-of-pallars, county-of-rosellon, co-principality-of-andorra. The validator (--resolve) gives 0 errors. The only warnings are the expected 'shape has no verdict' ones: 14 in Urgell and 20 in Andorra, because the two dossiers share the Cliopatria row 'County of Urgell'. All 19 spot checks were opened with WebFetch on 2026-10-31, and every one matched its note. Nothing is fabricated or mis-dated. No reviewer fixes were applied.

Verdicts: county-of-urgell **fail**, county-of-pallars **pass**, county-of-rosellon **thin**, co-principality-of-andorra **fail**.

## county-of-urgell: fail

### Fixes (author)
- `/ledger/11`: The dossier ends the county's land in 1231 and keeps a landless county to 1413. Its own page says the county lasted to 1413, and the crown-of-aragon dossier expects the 18 cells to stay Urgell's until 1413.
  - Evidence: County of Urgell page: Jaume I 'acknowledged' Ponç IV of Cabrera as successor; it lists Ponç I (1236-1243) to Jaume II (1408-1413) and says 'The county of Urgell was extinguished and absorbed by the Crown of Aragon in 1413'. James I page: Aurembiaix 'agreed to hold Urgell in fief for him'. crown-of-aragon /ledger/15 (1236 gain from county-of-urgell, c1, repair note eu-12-k) says: 'subtract Cliopatria's County of Urgell 1202 shape (18 cells) from the Crown keyframes 1236-1412 and move this gain to 1413'. The author's note says Urgell cannot record a vassal_start because only the suzerain does. That is wrong: the mirror rule puts vassal_start in both ledgers, and the research brief's levels-of-control rule draws vassal land in a lighter tint.
  - Fix: Keep the 1231 loss to crown-of-aragon (James I direct hold 1231-1235). Add three things. (1) A 1236 gain from crown-of-aragon with a vassal_start (counterpart crown-of-aragon), sourced to the County of Urgell page, c2. (2) A new keyframe county-of-urgell_1236 for 1236-1412, verdict adjust, correction = the 1202 shape minus the Andorra cell (County of Urgell 1279). (3) A 1413 vassal_end plus a loss to crown-of-aragon before the dissolve. Replace the notes sentence about 'dependent title' and 'only the suzerain'. Report the Crown changes needed: remove the cells 1236-1412, add the vassal_start for 1236-1413 and move the gain to 1413.
- `/ledger/13`: The 1413 dissolve carries the 1202 shape as its region, but in this dossier the county has held no land since 1231.
  - Evidence: /ledger/11 gives the same 18 cells to crown-of-aragon in 1231. The 1413 dissolve has region {cliopatria: County of Urgell, year: 1202}.
  - Fix: Make the dissolve region match the land actually held in 1413 (the new 1236 keyframe after the fix above).
- `/keyframe_review/16`: The Andorra cell stays in Urgell to 1230, although a page the author used dates its cession to the bishop explicitly.
  - Evidence: Ermengol VI page: 'In 1133, Ermengol ceded Andorra to the Bishop of Urgell.' County page: 'Andorra was ceded to the bishop of Urgell by the count Ermengol VI of Urgell in the twelfth century.' Andorra page: 988. co-principality-of-andorra /ledger/0 names 'Bishop of Urgell' as the holder before 1278.
  - Fix: Add a 1133 loss of the Andorra cell (County of Urgell 1279 shape) at c2, counterpart the bishop's lordship (listed under counterparts_needing_dossiers). Mark keyframes 1126-1202 adjust minus that cell, and keep the 988 date as the disagreement in notes.
- `/ledger/10`: The 1149 gain circle on Lleida overlaps county-of-barcelona's 1149 gain of Lleida from almoravid-dynasty (c3), so two dossiers claim one city.
  - Evidence: county-of-barcelona /ledger/13: '1149: Lleida, Fraga and Mequinenza fall to Ramon Berenguer IV'. Urgell's own note: 'the Barcelona dossier draws the Lleida cell'.
  - Fix: Lower the event to a note, or keep it at confidence 1 with text saying it is a third share inside Barcelona's cell, so the renderer does not draw a second owner.
- `/notes`: The disagreement list leaves out the Ermengol IV page's 1102 date for Balaguer.
  - Evidence: Ermengol IV page: 'to the recapture of Balaguer, which occurred during the reign of his son, Ermengol V, in 1102.'
  - Fix: Add 1102 (Ermengol IV page) to the Balaguer disagreement (1105 Ermengol VI, 1106 Balaguer).

### Gaps (gap-filler)
- `/keyframe_review/15`: the year and owner of the cell added in 1111 (0.67 E 41.73 N, west of Balaguer) (try https://en.wikipedia.org/wiki/Balaguer)
- `/ledger/8`: the owner of Balaguer in 1105 (Almoravid wali of Lleida or the Hudids); the almoravid-dynasty dossier has no 1105 loss (try https://en.wikipedia.org/wiki/Pedro_Ansúrez)

### Spot checks
- `/ledger/2` https://en.wikipedia.org/wiki/Wilfred_the_Hairy: confirmed: 'Wilfred died in battle on 11 August 897'; 'Miró over Cerdanya and Conflent; and Sunifred over Urgell'
- `/ledger/3` https://en.wikipedia.org/wiki/Borrell_II,_Count_of_Barcelona: confirmed: 'In 948, Borrell inherited Urgell from his uncle Sunifred II.'
- `/ledger/4` https://en.wikipedia.org/wiki/County_of_Urgell: confirmed: 'Borrell II, who died in 992, gave Barcelona, Girona and Osona to Ramon Borrell'; Ermengol I 992-1010 (Borrell II page: died 993, noted)
- `/ledger/5` https://en.wikipedia.org/wiki/Ermengol_III,_Count_of_Urgell: confirmed: 'occupying, in 1050, Camarasa and Cubells after taking them from Yusuf of Lleida'
- `/ledger/6` https://en.wikipedia.org/wiki/Ermengol_IV,_Count_of_Urgell: confirmed: 'In 1076 ... taking the basin of the river Sió with the villages of Agramunt and Almenar that year and Linyola and Belcaire in 1091' (also confirms /ledger/7)
- `/ledger/11` https://en.wikipedia.org/wiki/James_I_of_Aragon: confirmed: 'On her death in 1231, James exchanged the Balearic Islands for Urgell with her widower, Peter of Portugal.'
- `/ledger/8` https://en.wikipedia.org/wiki/Ermengol_VI,_Count_of_Urgell: confirmed: 'conquered Balaguer in 1105 and made it his capital'; also /ledger/10 'In 1149, he assisted Raymond Berenguer in the conquest and repopulation of Lleida' and 'In 1133, Ermengol ceded Andorra to the Bishop of Urgell'

Area: infobox None km2 (None), Cliopatria 4836 km2, ratio None, acknowledged True. County of Urgell infobox has no area (checked); the notes say so

## county-of-pallars: pass

What I tried: All four events confirmed; the predecessor, the split and the successors all match west-franks, county-of-pallars-jussa and county-of-pallars-sobira. The five Cliopatria shapes are the same 18 cells. Sort lies inside the bbox. Certainty covers 872-1011. Four pages against a budget of five. Ribagorza's 920 split moves no Pallars cell, as the notes say.

### Spot checks
- `/ledger/0` https://en.wikipedia.org/wiki/Raymond_I_of_Pallars_and_Ribagorza: confirmed: 'the first independent count of Pallars and Ribagorza from 872 until his death'
- `/ledger/1` https://en.wikipedia.org/wiki/County_of_Pallars_Juss%C3%A0: confirmed: 'In 1011, Sunyer of Pallars died and by his testament his county was divided between his sons, the eldest, Raymond III, receiving Pallars Jussà'
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Pallars_Juss%C3%A0: confirmed: 'the younger, William II, receiving Pallars Sobirà'
- `/ledger/3` https://en.wikipedia.org/wiki/County_of_Pallars: confirmed: Sunyer I 'died in 1011'; 'Sunyer's two sons divided their inheritance'; count list incl. 'Ermengol I 992-1010' as the dossier gives it; 'Its chief city was Sort.'

Area: infobox None km2 (None), Cliopatria 4850 km2, ratio None, acknowledged True. County of Pallars page has no infobox (checked)

## county-of-rosellon: thin

### Gaps (gap-filler)
- `/keyframe_review/3`: The county page says 'Late in the 10th century, Alt Rosselló, Conflent, and inland Vallespir passed to the counts of Cerdanya' and 'Roussillon was reduced to the coastal regions of Roussillon and Vallespir'. Keyframes 990-1168 still hold Conflent and upper Vallespir (perhaps a third of the shape), and no loss is written because no year is known. Find the year, then add a loss to county-of-berga and adjust the keyframes minus Conflent. (try https://en.wikipedia.org/wiki/Conflent)
- `/identity/capitals/0`: Castellrosselló is given as the seat for 759-988, but the County page says 'Throughout the century, Empúries was the centre of comital power and the counts had their seat there' and 'Gausfred I made his capital at Castelló d'Empúries'. The united counts' seat (817-989) needs years and a capital entry at Empúries or Castelló d'Empúries. (try https://en.wikipedia.org/wiki/Gausfred_I_of_Roussillon)
- `/ledger/1`: County of Empúries page: 'From 835 to 844, Sunyer I ruled Empúries and Peralada while Alaric I ruled Roussillon and Vallespir'. This short separation of the Empúries cells has no events (split 835, merge 844). (try https://en.wikipedia.org/wiki/Sunyer_I_of_Empúries)
- `/ledger/3`: The year Giselbert moved the seat from Castellrosselló to Perpignan (c1 at 989; the page gives no year). (try https://en.wikipedia.org/wiki/Perpignan)

### Spot checks
- `/ledger/0` https://en.wikipedia.org/wiki/County_of_Roussillon: confirmed: infobox 'Establishment: 759'; text 'probably conquered ... by Pepin the Short ... in 760' (c2 right); also /ledger/4-5 'In 1014, Hugh I of Empúries invaded Roussillon, but in 1019 a pact was signed'
- `/ledger/1` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: confirmed: 'In 817, Empúries was merged with the County of Roussillon, a union which lasted until 989.'
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: confirmed: 'At the death of Gausfred I in 989, Roussillon and Empúries were separated.'
- `/ledger/6` https://en.wikipedia.org/wiki/Roussillon: confirmed: 'in his will Girard II left all his lands to Alfonso II of Aragon, who took possession in 1172.'

Area: infobox 3600 km2 (2024), Cliopatria 4056 km2, ratio 1.13, acknowledged True. 3,600 km2 is the modern Roussillon (Roussillon page); the County page has no area; the notes say so

## co-principality-of-andorra: fail

### Fixes (author)
- `/ledger`: The state's own page puts Andorra under the Crown of Aragon's Principality of Catalonia from 1278 to 1715, but the dossier records no dependency, and neither the notes nor the certainty mention it.
  - Evidence: Andorra page: 'Andorra was formed as a polity by a charter in 1278, being a lordship within the Principality of Catalonia until 1715.' Also 'The conflict was resolved in 1278 with the mediation of the king of Aragon, Peter III'. The dossier's predecessor is crown-of-aragon.
  - Fix: Add a vassal_start in 1278 (counterpart crown-of-aragon), a vassal_end and vassal_start in 1516 (crown-of-aragon to kingdom-of-spain, or follow how kingdom-of-spain books the Catalan lordships), and a vassal_end in 1715 (Nueva Planta; the Andorra page says the bishop acted 'to avoid the application of Nueva Planta to Andorra'). Source them to the Andorra page at c2 and list the mirror events the Crown and Spain need.
- `/ledger/0`: The found event names the land's holder as 'Bishop of Urgell', but /identity/predecessors names crown-of-aragon. No neighbour mirrors either, and county-of-foix books a 1278 gain of the same land.
  - Evidence: crown-of-aragon has no 1278/1279 event for Andorra, although its Cliopatria shape drops the cell in 1279. county-of-foix /ledger/1 is '1278 gain' of region {country: Andorra} from 'Bishop of Urgell' at c3, so from 1278 two dossiers own the valleys. 'Bishop of Urgell' is not in counterparts_needing_dossiers.
  - Fix: Pick one holder for 1231-1278 and use it in both places: the bishop's lordship (and list it under counterparts_needing_dossiers), or crown-of-aragon with a matching 1278 loss. Report to eu-10 that county-of-foix's 1278 event should be a co-prince relation, not a territorial gain.
- `/ledger/0/note`: The note quotes 'Andorra's borders have remained unchanged since 1278' and cites the Andorra page, but the sentence is on History of Andorra.
  - Evidence: WebFetch of the Andorra page: the phrase is not in the text. History of Andorra: 'Andorra's borders have remained unchanged since 1278.'
  - Fix: Attribute the quote to History of Andorra, which is already in sources.

### Gaps (gap-filler)
- `/ledger`: History of Andorra: 'Andorra was briefly annexed to the Crown of Aragon twice, in 1396 and 1512.' Both are whole-state occupations with no end year; find the ends and add occupation_start/end with counterpart crown-of-aragon. (try https://en.wikipedia.org/wiki/Co-princes_of_Andorra)
- `/keyframe_review/15`: The 1809-1812 keyframe rests on 'Napoleon I reestablished the Co-Principate in 1809'. The 1793-1809 French renunciation of the co-princely title is not dated or explained (Cliopatria holds the cell throughout). (try https://en.wikipedia.org/wiki/History_of_Andorra)

### Spot checks
- `/ledger/0` https://en.wikipedia.org/wiki/Andorra: confirmed: infobox 'First Paréage: 8 September 1278'; 'The conflict was resolved in 1278 with the mediation of the king of Aragon, Peter III, between the bishop and the count' (the 'borders unchanged' quote is mis-attributed; see fixes)
- `/ledger/1` https://en.wikipedia.org/wiki/History_of_Andorra: confirmed: 'In 1812–1813, the First French Empire annexed Catalonia during the Peninsular War' 'with Andorra as a part of the district of Puigcerdà in the new department of Sègre'
- `/ledger/2` https://en.wikipedia.org/wiki/History_of_Andorra: confirmed: 'In 1814, an imperial decree reestablished the independence and economy of Andorra.'
- `/keyframe_review/15` https://en.wikipedia.org/wiki/History_of_Andorra: confirmed: 'Napoleon I reestablished the Co-Principate in 1809'

Area: infobox 468 km2 (2024), Cliopatria 380 km2, ratio 0.81, acknowledged True. 

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| county-of-urgell 870 gain west-franks | west-franks 870 loss | matched | Cerdanya; west-franks /ledger/4 |
| county-of-urgell 897 loss county-of-berga | county-of-berga 897 found | matched | berga founded from county-of-urgell, Cerdanya-Conflent-Berga |
| county-of-urgell 948 loss county-of-barcelona | county-of-barcelona 948 gain | matched |  |
| county-of-urgell 992 gain county-of-barcelona | county-of-barcelona 992 loss | matched |  |
| county-of-urgell 1050 gain taifa-of-lerida | - | missing | taifa-of-lerida (eu-12, written) has no loss of Camarasa/Cubells; route to its author |
| county-of-urgell 1076 gain taifa-of-lerida | - | missing | no loss of the Sió basin/Agramunt in taifa-of-lerida; its 1093 loss to kingdom-of-aragon holds Almenar (page disagreement) |
| county-of-urgell 1091 gain taifa-of-lerida | - | missing | Linyola, Belcaire; no loss in taifa-of-lerida |
| county-of-urgell 1105 gain almoravid-dynasty | - | missing | almoravid-dynasty (af-02) has no Balaguer loss; taifa-of-lerida dissolves to the Almoravids 1102 |
| county-of-urgell 1149 gain almoravid-dynasty | almoravid-dynasty 1149 loss | mismatch | almoravid /ledger/46 books the 1149 loss to 'Castile, Aragon, Portugal and the Almohads' (c1); county-of-barcelona /ledger/13 also gains Lleida in 1149, so the city is claimed twice |
| county-of-urgell 1231 loss crown-of-aragon | crown-of-aragon 1236 gain | mismatch | Five years apart. The Crown's repair note asks for the cells to stay Urgell's 1236-1412 and the gain to move to 1413; see the Urgell fix on /ledger/11. |
| west-franks 878 loss county-of-urgell | - | mismatch | Urgell has no 878 gain (its 878/896 shapes are replaced by the 870 outline); the counterpart should be county-of-barcelona (878 gain from west-franks, matched) and county-of-besalu; route to eu-07 |
| county-of-pallars 872 found west-franks | west-franks 872 loss | matched |  |
| county-of-pallars 1011 split county-of-pallars-jussa | county-of-pallars-jussa 1011 found | matched |  |
| county-of-pallars 1011 split county-of-pallars-sobira | county-of-pallars-sobira 1011 found | matched |  |
| county-of-ribagorza 920 split county-of-pallars | - | exception | Pallars has no 920 event; both dossiers draw separate land from 872, so no cell moves, as the Pallars notes say |
| county-of-rosellon 817 gain county-of-ampuria | county-of-ampuria 817 merge | matched |  |
| county-of-rosellon 989 loss county-of-ampuria | county-of-ampuria 989 split | matched |  |
| county-of-rosellon 1014 contest_start county-of-ampuria | county-of-ampuria 1014 contest_start | matched | ends 1019 on both sides |
| county-of-rosellon 1172 loss crown-of-aragon | crown-of-aragon 1172 gain | matched |  |
| co-principality-of-andorra 1278 found Bishop of Urgell | county-of-foix 1278 gain | mismatch | county-of-foix /ledger/1 gains {country: Andorra} from 'Bishop of Urgell' at c3, so two owners from 1278; the predecessor crown-of-aragon has no 1278/1279 loss of the cell its shape drops in 1279; route to eu-10 and eu-12 |
| co-principality-of-andorra 1812 loss first-french-empire | - | exception | first-french-empire not written yet (eu-20 has not run) |

## Routing and problems

- The orchestrator's brief allows small reviewer fixes; none applied. Every finding needs a structural change (new events or keyframes) or a choice between neighbours.
- county-of-urgell and crown-of-aragon disagree on who holds the 18 Urgell cells 1236-1412. The Crown's own repair note (eu-12-k) and the County of Urgell page side with Urgell keeping them as a vassal. Both authors must change together; route to eu-12 (crown-of-aragon).
- co-principality-of-andorra overlaps county-of-foix's 1278 gain of Andorra (eu-10), and is the same state as principality-of-andorra (eu-20, not yet written). Merge or link it there.
- Mirrors still missing in written dossiers: taifa-of-lerida (Urgell gains 1050, 1076, 1091) and almoravid-dynasty, af-02 (1105 Balaguer; 1149 counterpart bundle). west-franks (eu-07) 878 loss should name county-of-barcelona and county-of-besalu.
- Scratch is at /tmp/claude-0/work/eu-12-b (validate.json copied to /tmp/claude-0/work/review-eu-12-b).

Counterparts needing dossiers: Episcopal lordship of Andorra (Bishop of Urgell, with the lords of Caboet/Castellbò from 1095) (bishopric-of-urgell, 1133-1278); Muhammad al-Tawil of Huesca (muhammad-al-tawil-of-huesca, 907-907)

Gazetteer names needed: Camarasa, Cubells, Agramunt, Balaguer, Linyola, Lleida, La Seu d'Urgell, Cerdanya, Alt Urgell, Sort, Pallars, Ribagorza, Castellrosselló, Castelló d'Empúries, Conflent, Vallespir.
