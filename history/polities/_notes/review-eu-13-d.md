# Review of batch eu-13-d (papal-states), 2026-10-25

Reviewer: adversarial review, Phase B. Dossier: history/polities/papal-states.json (56 Cliopatria shapes, page budget 14, all 14 spent by the author).
Neighbour dossiers read (ledger grep for papal-states and the years of each event): byzantine-empire, kingdom-of-the-lombards, exarchate-of-ravenna, kingdom-of-the-franks, duchy-of-spoleto, duchy-of-benevento, norman-italy, kingdom-of-sicily, holy-roman-empire, holy-roman-empire-minor-states, comtat-venaissin, capetian-house-of-anjou, kingdom-of-france, kingdom-of-naples, kingdom-of-naples-napoleonic, habsburg-monarchy, kingdom-of-sardinia, kingdom-of-italy. Not on disk yet (group not run / sibling part): republic-of-venice, republic-of-florence, duchy-of-milan, italian-republic, first-french-empire, french-directory, cispadane-republic, cisalpine-republic, revolutionary-roman-republic, roman-republic-1849, united-provinces-of-central-italy, austrian-empire, kingdom-of-the-two-sicilies and the others of the Context table.

## Verdict: thin

Valid (0 errors, 10 warnings, all counterpart slugs without dossiers that the author lists). No fabricated or mis-dated event found: 11 events checked on 5 pages, all confirmed. Area fine (infobox 44,000 km2 before 1859 against Cliopatria 1815 shape 39,316 km2, ratio 0.89, acknowledged in /keyframe_review/53). Keyframe walk: every area change between consecutive shapes has a ledger event or an adjust verdict. One-state decision (no split) is sound and argued. What is missing are events, several of them recorded on the neighbours' side or on a page the author already opened; they go to a gap-filler.

## Fix applied by the reviewer

- /ledger/5/confidence: 2 -> 1. Papal States page: "Some later claimed that in 781, Charlemagne extended the regions over which the pope would be temporal sovereign" (a later claim, as the note itself says), and the region drawn (the south Tuscan strip of Cliopatria's 783 shape) is not among the lands that sentence names. Re-validated: valid.

## Findings left for the author or gap-filler (non-blocking)

1. Missing 1663 and 1668 French occupations of Avignon and the Comtat. The Comtat Venaissin page (already source 4 of the dossier) has the infobox 'French occupation: 1663, 1668, 1768-1774'; comtat-venaissin /ledger/3-6 and kingdom-of-france /ledger/113-114 record them. The dossier has only 1768-1774 (/ledger/28-29). Add occupation_start/occupation_end 1663 and 1668, counterpart kingdom-of-france, region union Comtat Venaissin + Avignon, as for 1768.
2. Missing Benevento (and Pontecorvo) enclave. duchy-of-benevento /ledger/26 (1081 loss papal-states, c3: 'Finally, in 1081, Guiscard returned the title to the papacy with little but the city remaining') and norman-italy /ledger/19 (1081 loss papal-states) have no mirror here. The Papal States page (read by the reviewer) says the state 'also included the small enclaves of Benevento and Pontecorvo' and that 'Bologna, Ferrara, Umbria, the Marches, Benevento and Pontecorvo were all formally annexed by November' 1860, yet /ledger/45 draws only Marche + Umbria. Add a 1081 gain {place: Benevento} from duchy-of-benevento (page: Principality of Benevento) and put Benevento and Pontecorvo into the 1860 loss region; Pontecorvo's acquisition year and the 1806-1815 Napoleonic principalities need a page.
3. /ledger/21 (1509 contest_end) says Agnadello 'led to the papal recovery of territory' from Venice (Faenza, Rimini and other towns), but no gain from republic-of-venice is recorded and no earlier loss; the shapes keep Ravenna, Rimini and Faenza papal throughout. Add the 1509 gain (Ravenna, Cervia, Rimini, Faenza) and the earlier losses to Venice (Faenza and Rimini after Cesare Borgia's fall in 1503; Ravenna, Venetian from the fifteenth century) from a page (War of the League of Cambrai, Ravenna). The Papal States page is silent on this (checked).
4. duchy-of-spoleto /ledger/11-12: Lambert I seized Rome 877-878 (occupation of papal-states, c2/c1). No mirror here. Add occupation_start 877 / occupation_end 878 on {place: Rome} if a page confirms (Lambert I of Spoleto).
5. kingdom-of-sicily /ledger/6: 1144 gain from papal-states (frontier fixed by a truce with the pope, c2). No mirror here; find what land (page: Roger II of Sicily) or ask the Sicily author to drop the counterpart.
6. kingdom-of-naples-napoleonic /ledger/5 and /ledger/9: Murat's army held Bologna and the Marche April-May 1815 (occupation of papal-states). No mirror here; and /keyframe_review/52 (1814 shape with Marche and Legations, 'unverified: page budget') is contradicted by it for the Marche. Add occupation events and, with a page (Neapolitan War), date the return of the Marche and the Legations (1815).
7. /ledger/36 (June 1800 gain, counterpart revolutionary-roman-republic): the author's own note quotes the Roman Republic page lead that the republic ended with the Neapolitan invasion of 30 September 1799. Rome was then held by Naples until the restoration; the counterpart of the June 1800 gain is the Neapolitan occupation, not the republic. Either set the counterpart to the Bourbon Kingdom of Naples or add an occupation 1799-1800. Not verified by the reviewer.

## Thin (confidence-1 events and gaps, with pages to try)

- /ledger/3 (763 gain Emilia, c1): Desiderius page (envoys of Pepin c. 760 had Desiderius return cities; see kingdom-of-the-lombards /ledger/25).
- /ledger/4 (775 loss) and /ledger/5 (781 gain, now c1): Pope Adrian I page.
- /ledger/6 (793 loss, c1): no page known; Cliopatria shape year.
- /ledger/9 (1272 Umbria gain, c1): Pope Innocent III (the recuperations of 1198: Spoleto, Perugia, Assisi) and Duchy of Spoleto later history.
- /ledger/16 (1503 vassal_end Romagna, c1): Cesare Borgia page.
- /ledger/19 (1507 gain, c1): Bentivoglio family / Giovanni II Bentivoglio page.
- Rulers strip (popes): List of popes.
- Urbino as a fief before 1631: Duchy of Urbino.
- Wars of Castro (1641-1644, 1649) missing from wars[]; the 1649 gain has no war: Wars of Castro.
- French garrison in Rome 1849-1870 and Austrian occupation of the Legations/Ancona 1849-1859: Pope Pius IX page.

## Cross-dossier matrix

| papal-states event | counterpart | mirror | status |
| --- | --- | --- | --- |
| 756 found | byzantine-empire | byzantine-empire 756 loss papal-states | matched |
| 756 gain | kingdom-of-the-lombards | 756 loss papal-states | matched |
| 757 gain (Ferrara pledge) | kingdom-of-the-lombards | none; duchy-of-spoleto has 757 loss papal-states (c1) instead | missing / mismatch |
| 763 gain | kingdom-of-the-lombards | 763 loss papal-states | matched |
| 775 loss | kingdom-of-the-franks | 775 gain papal-states | matched |
| 781 gain | kingdom-of-the-franks | none | missing (franks side) |
| 793 loss | kingdom-of-the-franks | none | missing (franks side) |
| 1198 gain Marche | holy-roman-empire | none | missing (HRE side) |
| 1208 vassal_start | duchy-of-ferrara | no dossier | exception (listed) |
| 1272 gain | holy-roman-empire-minor-states | 1272 loss papal-states | matched |
| 1278 gain Romagna | holy-roman-empire-minor-states | 1279 loss papal-states | matched (1 yr) |
| 1274 vassal_start | comtat-venaissin | comtat found 1274 from county-of-toulouse, no vassal_start | mismatch |
| 1348 gain Avignon | capetian-house-of-anjou | none; comtat-venaissin also gains Avignon in 1348 | missing + double claim |
| 1500/1503 vassal | duchy-of-romagna | no dossier | exception (listed) |
| 1507 gain | Bentivoglio/Baglioni (text) | none | exception |
| 1512 gain | duchy-of-milan | sibling eu-13 part not on disk | exception |
| 1545 loss | duchy-of-parma-and-piacenza | no dossier | exception (listed) |
| 1597 gain / vassal_end | duchy-of-ferrara | no dossier | exception |
| 1631 gain | duchy-of-urbino | no dossier | exception |
| 1649 gain | duchy-of-castro | no dossier | exception |
| 1768/1774 occupation | kingdom-of-france | France 1768/1774 occupation of comtat-venaissin | matched (via vassal) |
| 1791 vassal_end | comtat-venaissin | comtat dissolve 1791, no vassal_end | mismatch |
| 1791 loss Avignon | kingdom-of-france | France 1791 gain from comtat-venaissin | mismatch (counterpart) |
| 1796-1814 events | french-directory, cispadane-republic, revolutionary-roman-republic, italian-republic, first-french-empire | eu-20 not run | exception |
| 1849 loss/gain | roman-republic-1849 | no dossier | exception (listed) |
| 1859 loss | united-provinces-of-central-italy | no dossier | exception (listed) |
| 1860-09 loss Ancona, 1860-11 loss | kingdom-of-sardinia | 1860-09 contest, 1860-11 gain papal-states | matched |
| 1870 dissolve | kingdom-of-italy | 1870-09 gain papal-states | matched |
| (none) | comtat-venaissin, kingdom-of-france | 1663, 1668 occupations | missing (papal side) |
| (none) | duchy-of-benevento, norman-italy | 1081 loss papal-states | missing (papal side) |
| (none) | duchy-of-spoleto | 877-878 occupation of papal-states | missing (papal side) |
| (none) | kingdom-of-sicily | 1144 gain from papal-states | missing (papal side) |
| (none) | kingdom-of-naples-napoleonic | 1815 occupation of papal-states | missing (papal side) |
| (none) | kingdom-of-the-lombards, exarchate-of-ravenna | 728 (Sutri), 740 losses to papal-states | mismatch: before papal-states starts (756); those authors should name the Duchy of Rome / papacy differently |
