# Review of batch eu-10-e (2026-10-25)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. All four dossiers validate with --resolve (0 errors, 0 warnings). No page gives an area for any of the four states, so no infobox comparison was possible (the authors say so). Spot checks on 11 pages, weighted to confidence-3 and land-moving events; none fabricated or mis-dated. No fix was applied by the reviewer.

## duchy-of-burgundy: fail

Findings:
- `/ledger/15` (blocking): vassal_start names 'County of Auxerre' as the vassal in 1435, but no County of Auxerre existed then: the author's own report gives it years 1002-1370 (sold to the king in 1370) and royal-domain-of-france records 'gain County of Auxerre' in 1371. Evidence: Treaty of Arras (1435) page: 'the following domains became vassal states of the Duke of Burgundy: The County of Auxerre and the County of Boulogne...' (wording confirmed), but in 1435 Auxerre was crown land; report counterparts_needing_dossiers: County of Auxerre years [1002, 1370]. Fix: Record Auxerre as a gain from kingdom-of-france (September 1435, region place Auxerre km 30-40, note quoting the page's 'vassal states' wording and Philip's exemption from homage) and its loss to kingdom-of-france in 1477 (inside the 1477 contest/occupation), as burgundian-state and royal-domain-of-france do; delete /ledger/15 and /ledger/28.
- `/ledger/18` (blocking): vassal_start names county-of-vermandois, a state whose dossier ends in June 1213, and draws the whole 1210 Cliopatria Vermandois shape (19,510 km2) for 'the Vermandois, with its capital Saint-Quentin'. Evidence: county-of-vermandois identity end {year: 1213, month: 6}; shapes.csv county-of-vermandois_1210 area 19,509.6 km2; royal-domain-of-france /ledger/43 records the 1435 cession of the Somme towns, Ponthieu and Saint-Quentin as a loss to burgundian-state, i.e. the land was the crown's. Fix: Make it a gain from kingdom-of-france in September 1435 with region {place: Saint-Quentin, km: 25} (text 'the Vermandois, with its capital Saint-Quentin'), and a matching loss in 1477; delete /ledger/18 and /ledger/31.
- `/ledger/17` (blocking): One vassal_start with counterpart county-of-ponthieu covers both Ponthieu and the royal Somme towns and Péronne (admin1 Somme); the Somme towns were never Ponthieu's, and county-of-ponthieu records 1435 as a rename, not as a vassal_start. Evidence: Treaty of Arras page lists 'The Somme towns and Péronne' and 'Ponthieu' as separate items; county-of-ponthieu /ledger/6 is 'rename' (1435-09), /ledger/7-8 rename and dissolve 1477. Fix: Split: the Somme towns and Péronne as a gain from kingdom-of-france (Sept 1435, region the Somme minus Ponthieu, or place Amiens/Péronne discs); Ponthieu as vassal_start county-of-ponthieu (place Abbeville km 35) and ask the county-of-ponthieu owner (eu-10) for the mirror vassal_start 1435 / vassal_end 1477 (see cross_checks).
- `/ledger/16` (blocking): vassal_start names county-of-boulogne, which the same author's county-of-boulogne dossier makes dormant (merged into county-of-auvergne) from 1259 to 1477, so the vassal has no ledger to mirror it; county-of-auvergne keeps Boulogne in every keyframe 1260-1476 with no 1435 event. Evidence: county-of-boulogne /ledger/6 merge county-of-auvergne 1259 and /ledger/7 note 'recorded in the Duchy of Burgundy dossier'; county-of-auvergne keyframes 1416-1476 include Boulogne, ledger has only 1260 gain and 1477 loss. Fix: Either (preferred) gain from county-of-auvergne in Sept 1435 and loss to kingdom-of-france in 1477 (French forces seized Boulogne in early 1477, War of the Burgundian Succession page), routing the Auvergne mirror to eu-10; or keep vassal_start with counterpart county-of-auvergne and region Boulogne-sur-Mer km 20, and route the mirror. Fix /ledger/29 the same way.
- `/keyframe_review/2` (blocking): The 1003 to 1010 shapes fall from 31,613 to 18,169 km2 (-43%: the Nièvre and most of the Auxerrois leave) and no ledger event explains it; meanwhile county-of-nevers (same author) founds Nevers out of this duchy in 989 and draws the Nièvre 989-1009 while this dossier's 918-1002 and 1003-1009 keyframes also draw it: a 21-year double claim with no vassal, loss or split event. Evidence: shapes.csv duchy-of-burgundy_1003 31,612.9 km2, _1010 18,168.6 km2; county-of-nevers /ledger/0 found duchy-of-burgundy 989 and /keyframe_review/0 note 'this keyframe overlaps the duchy's 918-1002 and 1003 shapes; the county was Landry's, held under the duke'; Landry page: 'Around 990, Landry was granted the County of Nevers by his father-in-law Count Otto-William of Burgundy ... with the consent of Duke Henry I of Burgundy and King Hugh Capet'. Fix: Pick one model and write it in both dossiers: (a) Nevers as the duke's vassal: vassal_start county-of-nevers 989 (region admin1 Nièvre) here and the mirror vassal_start in county-of-nevers, with vassal_end in 1005 (Robert II's settlement) or 1010; adjust keyframes 918 and 1003 to minus the Nièvre from 989; or (b) loss to county-of-nevers in 989 here with the 918 keyframe ending 988 and a new 989-1002 keyframe minus the Nièvre, 1003 adjusted likewise. Either way add the event that explains the Auxerrois leaving by 1010 (Robert II page: Landry 'renouncing the Counties of Avallon and Auxerre' in 1005, to the king).
- `/ledger/5` (non-blocking): 1361-1363 is recorded as two renames, but the Duchy page says the duchy 'reverted to King John II' in 1361 and was ceded to Philip in 1363, and kingdom-of-france and royal-domain-of-france both record gain duchy-of-burgundy 1361 and loss 1364: unmatched. Evidence: Duchy of Burgundy page: 'the duchy reverted to King John II of France and the royal House of Valois'; 'when King John II ceded the duchy to his younger son Philip'; kingdom-of-france /ledger/43 gain 1361, /ledger/45 loss 1364. Fix: Add merge (or loss) to kingdom-of-france Dec 1361 and gain from kingdom-of-france Sept 1363, or state in notes why the duchy is drawn as continuous and route the France side to drop its 1361/1364 pair; the France side's 1364 should in any case be 1363.
- `/ledger/32` (non-blocking): contest_start for the duchy and Picardy in January 1477 does not mirror kingdom-of-france, which records occupation_start duchy-of-burgundy 1477 to occupation_end 1482 for the same land. Evidence: kingdom-of-france /ledger/64 and /ledger/68; War of the Burgundian Succession page speaks of 'all French-occupied Burgundian territories' and 'Already on 29 January, the assembly of the Duchy of Burgundy acknowledged the full reincorporation into the French realm'. Fix: Record occupation_start (counterpart kingdom-of-france) January 1477 for Burgundy and Picardy with occupation_end Dec 1482, keeping contest_start/_end for Franche-Comté and Artois (as house-of-habsburg does).
- `/ledger/13` (non-blocking): No occupation_start for Hainaut in 1428 although county-of-hainaut records occupation_start duchy-of-burgundy in July 1428 (Treaty of Delft) ending 1432. Evidence: county-of-hainaut /ledger/6-7. Fix: Add occupation_start county-of-hainaut 1428-07 and occupation_end 1432 here if a page supports Delft (the Burgundian Netherlands table: 'Offered position after victory of the Hollandic cities in the Hook and Cod wars'), or route the Hainaut side.
- `/ledger/3` (non-blocking): Counterpart 'Bishop of Langres' is not listed in the report's counterparts_needing_dossiers (only the notes name it). Evidence: report counterparts_needing_dossiers lists Namur, Auxerre, Rethel only. Fix: Either list it or record the 1016 Dijon transfer as small and inside the 1010 shape (it is: Dijon 5.04 E 47.32 N lies inside the 1010 bbox) with counterpart 'nobody'-style explanation in the note.
- `/identity/rulers` (non-blocking): Ruler strip not contiguous: Otto-William to 1004 and Robert II from 1005; Robert I to 1076 and Philip of Rouvres from 1349 (acknowledged). Evidence: identity.rulers. Fix: Close 1004-1005 (Robert II page: Beaune besieged 1004, settlement 1005) and fill the Capetian dukes 1076-1349 from a list page.

Gaps for a gap-filler:
- `/keyframe_review/3`: 366-year bridge 1018-1384 with no boundary event (Capetian acquisitions such as the county of Chalon and Auxonne, 1237). Try: https://fr.wikipedia.org/wiki/Liste_des_ducs_de_Bourgogne
- `/keyframe_review/5`: 1395 and 1402 shape changes (Charolais purchase c. 1390). Try: https://en.wikipedia.org/wiki/Charolais
- `/ledger/24`: Confidence 1: the 1475 invasion of Lorraine and capture of Nancy (the duchy-of-lorraine dossier has it as November 1475 at confidence 3); the Charles the Bold and Burgundian Wars pages give no date. Try: https://en.wikipedia.org/wiki/Duchy_of_Lorraine
- `/ledger/17`: Somme towns redeemed by Louis XI 1463, retaken at Conflans 1465, Péronne 1468, Amiens and Saint-Quentin 1471: the vassal tint runs unchanged 1435-1477. Try: https://en.wikipedia.org/wiki/Treaty_of_Conflans
- `/ledger/15`: Mâcon (ceded at Arras with Auxerre in most accounts) is absent; the English Arras page does not name it. Try: https://fr.wikipedia.org/wiki/Trait%C3%A9_d%27Arras_(1435)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Duchy_of_Burgundy: confirmed ('by 918 count Richard was titled as Duke of Burgundy'; infobox Established 'c. 918')
- `/ledger/15-18` https://en.wikipedia.org/wiki/Treaty_of_Arras_(1435): confirmed: 'the following domains became vassal states of the Duke of Burgundy', signed 20/21 September 1435; counterparts wrong (see fixes)
- `/ledger/13-14` https://en.wikipedia.org/wiki/Burgundian_Netherlands: confirmed ('seized the Counties of Hainaut, Holland and Zeeland in 1432')
- `/ledger/22` https://en.wikipedia.org/wiki/Charles_the_Bold: confirmed (Arnold died February 1473 and bequeathed the duchy; 'On 9 June 1473, he entered Maastricht')
- `/ledger/32-35` https://en.wikipedia.org/wiki/War_of_the_Burgundian_Succession: confirmed (29 January 1477; French seizures; Arras 1482 annexation of the duchy, Franche-Comté and Artois as Margaret's dowry)
- `/ledger/1,/ledger/3` https://en.wikipedia.org/wiki/Robert_II_of_France: confirmed (spring 1003 failure before Auxerre; 1016 the new bishop 'ceded Dijon and his county to the King')

## county-of-nevers: thin

Findings:
- `/ledger/0` (non-blocking): Nevers is founded out of duchy-of-burgundy in 989 but the duchy's dossier draws the Nièvre to 1009 with no loss or vassal event: double claim 989-1009 (also Auxerre, gained here in 1002 and inside the duchy's 1003 shape). Evidence: See duchy-of-burgundy /keyframe_review/2 finding; this dossier's /keyframe_review/0 note flags the overlap. Fix: Do together with the duchy-of-burgundy fix: if Nevers is the duke's vassal, add the mirror vassal_start (counterpart duchy-of-burgundy) here; if the duchy loses the Nièvre in 989, nothing changes here.
- `/ledger/13` (non-blocking): The 1539 'dissolve' is a change of title (the page: 'The count was raised to duke in 1539'), which the schema calls a rename; the state did not end, and kingdom-of-france has no event taking Nevers in 1521 or 1539. Evidence: County of Nevers page; schema: 'rename: the state changes its name ... colour and dossier continue'. Fix: Orchestrator decision (flagged in the author's notes): end at 1520/1521 with Cliopatria, or continue as the Duchy of Nevers with a rename in 1539; do not dissolve at the elevation.
- `/identity/rulers` (non-blocking): Ruler strip has a gap 1028-1031 (Landry to 1028, Renaud I from 1031). Evidence: Landry page: 'first hereditary Count of Nevers from 989 to 1028'; author notes Renaud I 1028/1031 disagreement. Fix: Start Renaud I in 1028 with a note on the List page's 1031, or explain the interregnum.

Gaps for a gap-filler:
- `/keyframe_review/5`: 1056 shape loses 15% (Yonne and Loiret cells); no event. Try: https://fr.wikipedia.org/wiki/Comt%C3%A9_de_Nevers
- `/keyframe_review/11`: Auxerre left the Nevers line after 1262 (author's notes) yet every shape to 1520 keeps it marked ok; Auxerre was sold to the crown in 1370 and ceded to Burgundy in 1435. Try: https://fr.wikipedia.org/wiki/Comt%C3%A9_d%27Auxerre
- `/keyframe_review/13`: Rethel appears in the 1285 shape and leaves in 1519 with no dated event. Try: https://en.wikipedia.org/wiki/County_of_Rethel

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Landry,_Count_of_Nevers: confirmed ('first hereditary Count of Nevers from 989 to 1028')
- `/ledger/2` https://en.wikipedia.org/wiki/Robert_II_of_France: confirmed (spring 1003, 'failed in front of Auxerre and Saint-Germain d'Auxerre')
- `/ledger/3` https://en.wikipedia.org/wiki/Landry,_Count_of_Nevers: confirmed ('Robert II agreed to peace with Landry in 1005')
- `/ledger/11` https://en.wikipedia.org/wiki/Burgundian_Netherlands: confirmed ('both held by Philip's younger son Philip II from 1407')
- `/ledger/13` https://en.wikipedia.org/wiki/County_of_Nevers: confirmed year ('The count was raised to duke in 1539'); event type questioned (see fixes)

## angevins: pass

Gaps for a gap-filler:
- `/ledger/3`: Confidence 1 dissolve in 1146 (Cliopatria's row end; Geoffrey ruled Anjou to 1151). Try: https://en.wikipedia.org/wiki/Angevin_Empire

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Geoffrey_Plantagenet,_Count_of_Anjou: confirmed (succession box 'Count of Maine 1126–1151'; Anjou 'Reign: 1129'; confidence 2 is honest)
- `/ledger/1` https://en.wikipedia.org/wiki/Geoffrey_Plantagenet,_Count_of_Anjou: confirmed ('When his father in law, King Henry I of England, died in 1135, Geoffrey supported Matilda in entering Normandy')
- `/ledger/2` https://en.wikipedia.org/wiki/Geoffrey_Plantagenet,_Count_of_Anjou: confirmed ('on 14 January 1144, he crossed the Seine and entered Rouen')

## county-of-boulogne: thin

Gaps for a gap-filler:
- `/ledger/0`: Confidence 1 start at Cliopatria's 1188: the county is older (page: infobox 'acquisition by the House of Flanders: 896', Eustace II in 1066); find when it became a county of its own. Try: https://fr.wikipedia.org/wiki/Comt%C3%A9_de_Boulogne
- `/ledger/6`: Confidence 1 passage to Adelaide of Brabant and the Auvergne line (county-of-auvergne has 1260). Try: https://en.wikipedia.org/wiki/Matilda_II,_Countess_of_Boulogne
- `/ledger/7`: Burgundian hold of Boulogne 1435-1477 (and from c. 1419 in fact) is drawn nowhere on the Boulogne/Auvergne side; see duchy-of-burgundy /ledger/16. Try: https://en.wikipedia.org/wiki/Treaty_of_Arras_(1435)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Boulogne: confirmed ('It was merged into the County of Artois by Philip II of France in 1212')
- `/ledger/4` https://en.wikipedia.org/wiki/County_of_Boulogne: confirmed ('Boulogne passed under nominal royal control in 1223')
- `/ledger/7` https://en.wikipedia.org/wiki/County_of_Boulogne: confirmed ('Bertrand V de la Tour succeeded to the counties of Auvergne and of Boulogne in 1437')
- `/ledger/8` https://en.wikipedia.org/wiki/County_of_Boulogne: confirmed ('In 1477, Bertrand II dealt with Louis XI, exchanging the county of Boulogne with the county of Lauragais'; infobox 1477)

## Cross-dossier matrix

- duchy-of-burgundy 1016 gain Bishop of Langres <-> None None None: **exception** no dossier; Dijon lies inside the 1010 shape; not listed in counterparts_needing_dossiers
- duchy-of-burgundy 1384 gain county-of-flanders <-> county-of-flanders 1384 merge: **matched** 
- duchy-of-burgundy 1384 gain free-county-of-burgundy <-> free-county-of-burgundy 1384 dissolve: **matched** dissolve with successor duchy-of-burgundy
- duchy-of-burgundy 1384 gain county-of-nevers <-> county-of-nevers 1384 merge: **matched** 
- duchy-of-burgundy 1407 loss county-of-nevers <-> county-of-nevers 1407 gain: **matched** 
- duchy-of-burgundy 1429 gain County of Namur <-> None None None: **exception** listed in counterparts_needing_dossiers
- duchy-of-burgundy 1430 gain county-of-brabant <-> county-of-brabant 1430 dissolve: **matched** 
- duchy-of-burgundy 1432 gain county-of-hainaut <-> county-of-hainaut 1432 dissolve: **matched** but county-of-hainaut also has occupation_start duchy-of-burgundy 1428-07 that Burgundy lacks
- county-of-hainaut 1428 occupation_start duchy-of-burgundy <-> duchy-of-burgundy None None: **missing** Treaty of Delft occupation not in duchy-of-burgundy; add it there or drop it in county-of-hainaut (eu-09)
- duchy-of-burgundy 1432 gain county-of-holland <-> county-of-holland 1433 loss: **matched** one year apart; pages disagree 1432/1433
- duchy-of-burgundy 1435 vassal_start County of Auxerre <-> royal-domain-of-france 1371 gain: **mismatch** County of Auxerre ended 1370 (sold to the crown); in 1435 the land was the crown's: should be a gain from kingdom-of-france
- duchy-of-burgundy 1435 vassal_start county-of-boulogne <-> county-of-boulogne None None: **missing** county-of-boulogne is dormant inside county-of-auvergne 1259-1477; county-of-auvergne has no 1435 event
- duchy-of-burgundy 1435 vassal_start county-of-ponthieu <-> county-of-ponthieu 1435 rename: **mismatch** Ponthieu records a rename, not a vassal_start; county-of-ponthieu owner (eu-10) to add vassal_start 1435 / vassal_end 1477 with counterpart duchy-of-burgundy
- duchy-of-burgundy 1435 vassal_start county-of-vermandois <-> county-of-vermandois 1213 dissolve: **mismatch** counterpart ended 1213; royal-domain-of-france /ledger/43 and burgundian-state /ledger/7 treat the Somme towns and Saint-Quentin as crown land ceded in 1435
- duchy-of-burgundy 1443 gain duchy-of-luxembourg <-> duchy-of-luxembourg 1443 loss: **matched** 
- duchy-of-burgundy 1469 occupation_start house-of-habsburg <-> house-of-habsburg 1469 occupation_start: **matched** end 1474 matched both sides
- duchy-of-burgundy 1473 vassal_start duchy-of-lorraine <-> duchy-of-lorraine 1473 rename: **missing** duchy-of-lorraine (eu-09) has no vassal_start duchy-of-burgundy for the 1473 protectorate
- duchy-of-burgundy 1473 gain duchy-of-guelders <-> duchy-of-guelders 1473 occupation_start: **mismatch** Burgundy: annexation 1473, loss 1477; Guelders: occupation 1473-1492 by duchy-of-burgundy (Burgundy dissolves 1482). Burgundian Netherlands page: 'in 1473 annexed the Duchy of Guelders'; route the Guelders side
- duchy-of-burgundy 1475 occupation_start duchy-of-lorraine <-> duchy-of-lorraine 1475 occupation_start: **matched** end 1476-10 both; Burgundy at confidence 1 without month, Lorraine 1475-11
- duchy-of-burgundy 1477 contest_start kingdom-of-france <-> kingdom-of-france 1477 occupation_start: **mismatch** France models an occupation of Burgundy and Picardy 1477-1482; Burgundy a contest
- duchy-of-burgundy 1482 loss kingdom-of-france <-> kingdom-of-france 1482 gain: **matched** both losses (Burgundy+Picardy; Franche-Comté+Artois) mirrored
- kingdom-of-france 1361 gain duchy-of-burgundy <-> duchy-of-burgundy 1361 rename: **mismatch** France and royal-domain-of-france record the 1361 reversion and 1364 regrant; Burgundy records renames only
- kingdom-of-france 1034 loss duchy-of-burgundy <-> duchy-of-burgundy 1032 rename: **mismatch** France holds the duchy 1018-1033 (gain 1018 c1, loss 1034 c3); Burgundy draws the duchy itself from 1018 and dates Robert I's grant 1032 (Duchy page)
- kingdom-of-france 1003 loss duchy-of-burgundy <-> duchy-of-burgundy None None: **mismatch** France 1003 loss and 1018 gain are Cliopatria-artefact events at confidence 1 with no Burgundy mirror; France has no contest for the 1003-1005 war that Burgundy and Nevers record
- county-of-nevers 989 found duchy-of-burgundy <-> duchy-of-burgundy None None: **missing** double claim of the Nièvre 989-1009; see the duchy-of-burgundy blocking finding
- county-of-nevers 1002 gain County of Auxerre <-> None None None: **exception** listed in counterparts_needing_dossiers; Auxerre also inside the duchy-of-burgundy 1003 shape
- county-of-nevers 1003 contest_start kingdom-of-france <-> kingdom-of-france None None: **missing** France has no contest for the Auxerre sieges of 1003-1005
- county-of-nevers 1322 merge county-of-flanders <-> county-of-flanders 1322 gain: **matched** 
- angevins 1126 found county-of-anjou <-> county-of-anjou 1126 merge: **matched** 
- angevins 1135 contest_start norman-england <-> norman-england 1141 contest_start: **mismatch** six years apart and on different land (Angevins: Calvados, Manche, Orne, Eure; Norman England: Eure only); Geoffrey page supports 1135; route to eu-11
- angevins 1146 dissolve None <-> angevin-empire 1147 merge: **matched** 
- county-of-boulogne 1188 found county-of-flanders <-> county-of-flanders None None: **missing** county-of-flanders has no 1188 event for Boulogne; the start is a Cliopatria artefact at confidence 1
- county-of-boulogne 1259 merge county-of-auvergne <-> county-of-auvergne 1260 gain: **matched** both confidence 1
- county-of-boulogne 1477 dissolve None <-> royal-domain-of-france 1478 gain: **matched** county-of-auvergne also has loss kingdom-of-france 1477 for Boulogne

## Problems

- No page failed; WebFetch returns a model summary, so quotes are the tool's quotes.
- No fix was applied by the reviewer: every finding needs a modelling choice (counterparts, keyframe corrections) rather than a one-field correction; no dossier was edited.
- Context dossiers not yet written (group has not run): county-of-savoy; counterparts without dossiers: county-of-namur, county-of-auxerre, county-of-rethel, kingdom-of-portugal (Boulogne 1236-1240 note only).
- Duplication for the orchestrator (flagged by the author): burgundian-state (eu-10-x, 1363-1482) and duchy-of-burgundy carry the same 1384-1482 gains; the two disagree on 1435 (gain from France vs vassal_start) and 1469 (gain/loss vs occupation).
- Identity for the orchestrator (flagged by the author): angevins is the County of Anjou under Geoffrey (same polygon as county-of-anjou 1111-1125, same house); by the one-dossier-per-state rule it could be folded into county-of-anjou with 'Angevins' in its cliopatria_names.
- Routed mismatches on other groups' dossiers: kingdom-of-france (1003/1018/1034, 1361/1364, 1477 occupation), duchy-of-lorraine (1473 protectorate), duchy-of-guelders (1473-1492 occupation), county-of-ponthieu (1435 vassal), county-of-hainaut (1428 occupation), county-of-auvergne (Boulogne 1435), county-of-flanders (Boulogne 1188), norman-england (1135 contest).
