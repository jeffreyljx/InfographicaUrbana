# Review of batch eu-11-x (written 2026-10-25)

Adversarial review of the 23 dossiers the eu-11-x author wrote for states Cliopatria lacks (Ireland, Wales, Scotland). Machine copy: history/notes/phase-b/reviews/eu-11-x.json. All 23 validated with --resolve (0 errors, 0 warnings) before and after the reviewer's edits.

Verdicts: lordship-of-ireland fail, kingdom-of-ireland fail, picts thin, kingdom-of-leinster thin, kingdom-of-connacht fix, kingdom-of-munster thin, kingdom-of-desmond thin, kingdom-of-thomond thin, kingdom-of-meath pass, ulaid fail, dyfed pass, deheubarth fail, marcher-lordships fail, principality-of-wales fail, glyndwr-s-wales fail, gododdin fix, kingdom-of-elmet pass, kingdom-of-dublin pass, lordship-of-galloway thin, earldom-of-orkney thin, lordship-of-the-isles thin, airgialla thin, tir-eoghain fail.

Convention: fail > thin > fix > pass. "fix" means the reviewer made the change (marked inside the dossier with "[Reviewer eu-11-x, 2026-10-25]"); a dossier that still has a blocking finding is "fail" even if some fixes were applied.

## Per dossier

### lordship-of-ireland: fail

Findings:

- TO DO `/keyframe_review/0/correction (also /keyframe_review/1-4 and /ledger/1/region)`: The region {"region": "Leinster"} is the gazetteer's modern province (81 H3 cells, about 20,485 km2: Dublin, Kildare, Meath, Westmeath, Longford, Louth, Offaly, Laois, Kilkenny, Carlow, Wexford, Wicklow), not Strongbow's kingdom, so the Lordship is drawn in Meath a year early and in Louth eighteen years early. Evidence: kingdom-of-meath holds Meath and Westmeath to 1171 and this dossier gains them only in 1172 (Norman invasion page: 'In early 1172, Henry allowed de Lacy to take royal troops into Meath'): 18 cells double-filled in 1171. airgialla holds Louth to 1188 (Airgialla page: Louth became 'Uriel' after the invasion): 4 cells double-filled 1171-1188. kingdom-of-leinster's own 1171 loss region is Dublin+Kildare+Wicklow+Wexford+Carlow+Laoighis+Kilkenny. Fix: Replace {"region": "Leinster"} in keyframes 0-4 and ledger 1 with the union kingdom-of-leinster uses for its 1171 loss (Dublin, Kildare, Wicklow, Wexford, Carlow, Laoighis, Kilkenny); Meath stays a 1172 gain; Louth enters only with a dated event (next fix).
- TO DO `/ledger (no 1189 event)`: airgialla's 1189 loss of Louth to lordship-of-ireland (confidence 1) has no gain here. Evidence: airgialla /ledger/4; this dossier's notes list it as a mirror gap. Airgialla page: 'the anglicisation Uriel became the name of the part of Airgialla that had extended into modern-day County Louth' (no year). Fix: Add a 1189 gain of Louth (admin1 Louth, Ireland) from airgialla at confidence 1 citing the Airgialla page, or agree a better-sourced year with that dossier; add Louth to keyframes from that year.

Gaps (for a gap-filler):

- `/ledger/4`: 1176 contest_end with Thomond is a confidence-1 bridge (Thomond page: Limerick taken by Raymond le Gros in 1175 and burned by Domhnall). Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Thomond
- `/ledger/9-10`: The Bruce contest 1315-1318 has no mirror in kingdom-of-scotland (other group). Page to try: https://en.wikipedia.org/wiki/Lordship_of_Ireland

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/7 confirmed; /ledger/11 confirmed; /ledger/12 confirmed; /ledger/13 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2. Keyframes run 21,500 km2 (1171) to 53,400 km2 (1235) to 5,300 km2 (the Pale, 1348).

### kingdom-of-ireland: fail

Findings:

- APPLIED `/ledger/3/counterpart, /ledger/5/counterpart, /wars/1/belligerents`: The Nine Years' War contest named the string "Hugh O'Neill, Earl of Tyrone (the Ulster confederacy)" while tir-eoghain carries the mirror contest pair 1593-1603. Evidence: tir-eoghain /ledger/3-4 name kingdom-of-ireland; Tir Eoghain page: Aodh Mor O Neill, Earl of Tyrone, 'fled in 1607'; Tudor conquest page: 'the Nine Years' War (1593-1603)'. Fix: Set to tir-eoghain (done, notes appended).
- APPLIED `/identity/successors/0/slug, /ledger/11/counterpart`: Successor and 1800 dissolve counterpart were kingdom-of-great-britain, whose own dossier dissolves on 1800/12 into united-kingdom. Evidence: kingdom-of-great-britain /ledger/18 (dissolve 1800/12 cp united-kingdom); united-kingdom /ledger/1 (1801/1 gain of Ireland cp kingdom-of-ireland). Kingdom of Ireland page: merged 'on 1 January 1801'. Fix: Set to united-kingdom (done); the 1801/1 gain in united-kingdom now mirrors it.
- TO DO `/keyframe_review/2/correction`: "Munster" for 1584-1602 contains Cork and Kerry, which kingdom-of-desmond holds to 1596: 26 H3 cells (about 6,600 km2) double-filled 1584-1596; the 1596 dissolve of Desmond into this state has no gain here. Evidence: Kingdom of Desmond page: 'After the death of King Donal IX MacCarthy Mor in 1596'; kingdom-of-desmond keyframe 1177-1596 and its dissolve 1596 cp kingdom-of-ireland. Fix: Draw Munster minus kingdom-of-desmond's 1177 region until 1595, add a 1596 gain cp kingdom-of-desmond and a keyframe from 1596.
- TO DO `/ledger (no 1543 event)`: kingdom-of-thomond dissolves in 1543 with this state as counterpart and successor, but there is no gain: Clare, Limerick and North Tipperary are drawn by nobody 1543-1583. Evidence: Kingdom of Thomond page: Murchadh 'agreed to surrender and regrant to the Tudor state' and was made Earl of Thomond (Parliament at Limerick 1542; infobox 1543). Fix: Add a 1543 gain cp kingdom-of-thomond (or a vassal_start if the earldom is to be a Crown vassal tint) and a keyframe from 1543.
- TO DO `/ledger (no 1585 event)`: airgialla dissolves in 1585 into this state; no gain here, so Monaghan is drawn by nobody 1585-1602. Evidence: Airgialla page: the kingdom 'came to an end in 1585 when Rossa Boy MacMahon agreed to surrender and regrant his territories'; the territory became County Monaghan. Fix: Add a 1585 gain of Monaghan cp airgialla and a keyframe from 1585.
- TO DO `/ledger/4 and /keyframe_review/3`: The 1603 whole-island gain overlaps tir-eoghain, which lives to 1607: 23 cells double-filled 1603-1606 (the author flagged it). Evidence: tir-eoghain dissolve 1607 cp kingdom-of-ireland; Plantations page: the earls 'left Ireland in the so-called 1607 Flight of the Earls'. Fix: Either subtract tir-eoghain's region 1603-1606 and add a 1607 gain cp tir-eoghain, or record tir-eoghain as this state's vassal 1603-1607 in both dossiers.
- TO DO `/identity/predecessors`: Only lordship-of-ireland is listed; kingdom-of-thomond, kingdom-of-desmond, kingdom-of-leinster, airgialla and tir-eoghain all name this state as successor with land. Evidence: Their identity.successors. Fix: Add them as predecessors with their land once the gains above exist.
- TO DO `/ledger (1707, 1800)`: kingdom-of-great-britain records a vassal_start 1707/5 and vassal_end 1800/12 with this state; no mirror here. Evidence: kingdom-of-great-britain /ledger/1 and /ledger/17. Fix: Add the mirror pair (or note that the colony type supplies the tint and ask the GB owner to drop the pair).

Gaps (for a gap-filler):

- `/keyframe_review/2`: Connacht's status 1584-1602 is a gap (Composition of Connacht 1585 not opened, per the keyframe note). Page to try: https://en.wikipedia.org/wiki/Composition_of_Connacht
- `/ledger/7-8`: The 1653-1659 merge with the Commonwealth: commonwealth-of-england gains Ireland from irish-catholic-confederation and dissolves to kingdom-of-england in 1660, so neither side matches. Page to try: https://en.wikipedia.org/wiki/Irish_Confederate_Wars

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/8 confirmed; /ledger/11 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2. The 1603 and 1660 keyframes (whole island) resolve to about 87,000 km2.

### picts: thin

Gaps (for a gap-filler):

- `/keyframe_review/1`: The 497->498 change subtracts Cliopatria's Dal Riata 644 shape (about 4,300 km2) with no ledger event; dal-riata's own found event is 498 (predecessor ulaid). Add a 498 loss to dal-riata or start the subtraction with a sourced event. Page to try: https://en.wikipedia.org/wiki/D%C3%A1l_Riata
- `/ledger`: dal-riata /ledger/1 records a 612 gain of Skye from picts (confidence 1) with no loss here. Page to try: https://en.wikipedia.org/wiki/D%C3%A1l_Riata
- `/ledger/0`: 297 is the first mention of the Picti (a panegyric), not a founding; confidence 1 is right. Page to try: https://en.wikipedia.org/wiki/Picts

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/5 confirmed.

Area: No Cliopatria shape (new state); the WebFetch result of the Picts page shows no infobox. Keyframes 54,600 / 50,300 / 43,800 km2.

### kingdom-of-leinster: thin

Gaps (for a gap-filler):

- `/ledger/4`: The 1375 gain (confidence 1) names lordship-of-ireland, but the Lordship lost that land in 1348 (its /ledger/12, to 'Gaelic Irish lordships'); the page gives only Art MacMurrough-Kavanagh's reign 'from 1375 to 1417'. Find the date of the MacMurrough recovery of Wexford, Carlow and Wicklow and align the counterpart with the Lordship's 1348 loss (or nobody). Page to try: https://en.wikipedia.org/wiki/Art_M%C3%B3r_Mac_Murchadha_Caomh%C3%A1nach
- `/keyframe_review (1171-1374)`: No land at all 1171-1374, while the Leinster page says the kingdom continued to 'control much of what is today County Wexford and County Carlow and parts of County Wicklow' after the invasion and the Diarmait page gives Domhnall Caomhanach as de iure successor. Also kingdom-of-england /ledger/56 records a 1326 loss of Leinster cells to this state with no gain here. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Leinster
- `/ledger/2`: 900 regain of Osraige is a rounding of 'In the 9th century' (confidence 1). Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Ossory

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2.

### kingdom-of-connacht: fix

Findings:

- APPLIED `/identity/successors/0/slug, /ledger/5/counterpart`: The 1474 dissolve and the successor named kingdom-of-ireland, which begins only in 1542. Evidence: Kingdom of Ireland page: 'Crown of Ireland Act: 18 June 1542'; Connacht page: kingship held by the O Conchobair 'until the death of the last king in 1474'. Fix: Set to lordship-of-ireland (done, note appended).
- APPLIED `/ledger/3, /ledger/4`: lordship-of-ireland records a vassal pair 1235-1474 with this state (Roscommon); no mirror here. Evidence: lordship-of-ireland /ledger/8 and /ledger/15; Richard Mor de Burgh page: Felim 'allowed to hold only five cantreds' in Roscommon after 1235; Connacht page: last king 1474. Fix: Added vassal_start 1235 (c2) and vassal_end 1474 (c2) cp lordship-of-ireland, region Roscommon (done).

Gaps (for a gap-filler):

- `/keyframe_review/0`: 450-1049 drawn as Roscommon only, a reading of 'By 1050, they had extended their rule from Rathcroghan in north County Roscommon'; the Kingdom of Connacht page has no infobox content and the 450 start is a bridge (confidence 1). Page to try: https://en.wikipedia.org/wiki/Connacht
- `/ledger`: kingdom-of-england /ledger/38 (1236 gain cp kingdom-of-connacht) and /ledger/40 (1272 loss cp kingdom-of-connacht) have no mirror here; this dossier gives the 1235 conquest to lordship-of-ireland. Route to the England owner. Page to try: https://en.wikipedia.org/wiki/Connacht

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/5 confirmed; /ledger/0 confirmed.

Area: No Cliopatria shape (new state); the Kingdom of Connacht page shows an empty infobox. Keyframes 2,500 / 18,200 / 2,500 km2.

### kingdom-of-munster: thin

Gaps (for a gap-filler):

- `/ledger/1, /ledger/2`: Osraige held about 600-900: both years are bridges (confidence 1) of 'brought under the control of Munster for two centuries' and 'remained a tuatha of Munster until the 9th century'. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Ossory
- `/identity/capitals/0`: Cashel 600-1118 is a bridge; the infobox gives Cork (the capital note says so). Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Munster

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2.

### kingdom-of-desmond: thin

Gaps (for a gap-filler):

- `/keyframe_review/1`: One shape 1177-1596 (Cork and Kerry minus a 60 km circle round Cork); the page gives only 'the eastern half of Desmond was conquered by the Anglo-Normans' in the late 12th century and the Callann victory of 1261, which is a war with no zones and no ledger event. Page to try: https://en.wikipedia.org/wiki/Battle_of_Callann
- `/wars/1`: The Desmond Rebellions (1569-1583) are listed with belligerents earldom-of-desmond and kingdom-of-ireland only; this state is not a belligerent. Move it to those dossiers or name this state's part. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Desmond

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /wars/0 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2.

### kingdom-of-thomond: thin

Gaps (for a gap-filler):

- `/keyframe_review/0`: One shape 1118-1543 including County Limerick and North Tipperary, while /wars/0 runs 1174-1318 (Norman invasion of Thomond, ending at Dysert O'Dea) with no loss or contest event after 1176; Limerick was captured by Raymond le Gros in 1175 (Thomond page). Page to try: https://en.wikipedia.org/wiki/Battle_of_Dysert_O%27Dea
- `/identity/capitals/1`: Clonroad from 1175: the page says Donnchadh 'moved his capital to Clonroad' with no year. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Thomond
- `/ledger/2`: 1176 contest_end is confidence 1. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Thomond

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2.

### kingdom-of-meath: pass

Gaps (for a gap-filler):

- `/ledger/0`: 400 start is a bridge (confidence 1); the page says Meath 'was a kingdom in Ireland from the 1st to the 12th century AD'. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Meath

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /keyframe_review/0 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2. Tried: region against the page extent, the Leinster and Lordship mirrors (both matched); could not break it.

### ulaid: fail

Findings:

- TO DO `/keyframe_review/0-1/correction and /ledger/1/region`: Ulster minus Cavan (minus Armagh from 450) still contains Monaghan and Fermanagh, which airgialla's 450 found region takes, and all of tir-eoghain's 465 keyframe (Tyrone, Derry, Limavady, Inishowen): 14 + 23 H3 cells double-filled 450/465-699. Evidence: airgialla /ledger/0 (450 found: Armagh, Monaghan, Fermanagh, Louth) against this /ledger/1 (450 loss: Armagh only); tir-eoghain /keyframe_review/0 from 465. Ulaid page: land lost 'to the Airgialla and the Northern Ui Neill'. Fix: Make the 450 loss match airgialla's found region (Armagh, Monaghan, Fermanagh) and agree with tir-eoghain which of the two holds Tyrone, Derry and Inishowen in each year (see tir-eoghain's fix: Inishowen first).
- TO DO `/ledger/4`: The 700 loss (confidence 1) of everything west of the Bann names airgialla, which has no 700 gain; most of that land is Cenel nEogain's (the author flagged it). Evidence: Ulaid page: 'By the 8th century the territory of the Ulaid shrunk to east of the Bann'; the page does not name the taker for this step. tir-eoghain's keyframe holds Tyrone and Derry. Fix: Split the loss: the Cenel nEogain land to tir-eoghain with a matching gain there, any remainder (Fermanagh, Monaghan) to airgialla, all at confidence 1.

Gaps (for a gap-filler):

- `/ledger/2-3`: Overlordship of Dal Riata 499-575 has no mirror in dal-riata (other group), and dal-riata /ledger/3 records a 644 loss of north-east Antrim to ulaid with no gain here. Page to try: https://en.wikipedia.org/wiki/Ulaid

Spot checks: /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed.

Area: No Cliopatria shape (new state); infobox 'Established: Before 450', no area.

### dyfed: pass

Gaps (for a gap-filler):

- `/ledger/1`: Ystrad Tywi lost 'in the late 7th century': 690 is a bridge (confidence 1); counterpart kingdom-of-seisyllwg has no dossier yet (Cliopatria row of another eu-11 part). Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Dyfed

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed.

Area: Infobox: 'an approximate area of about 2,284 square kilometres' (no year). Keyframe 690-919 resolves to about 2,300 km2 (reviewer) / 2,900 km2 (author): ratio 1.0-1.3; keyframe 410-689 about 3,200-4,000 km2: ratio 1.4-1.8. Both acknowledged in the keyframe notes.

### deheubarth: fail

Findings:

- APPLIED `/keyframe_review/2/to and new /keyframe_review/3`: The 950 keyframe ran to 1092 although the ledger gives the whole realm to Gruffydd ap Llywelyn 1055-1063 (/ledger/6-7). Evidence: Deheubarth page lineage list: 'Gruffydd ap Llywelyn, invader and prince of Gwynedd (1055-1063)'. Fix: Set the 950 keyframe to end 1054 and added deheubarth_1063 (1063-1092, same correction) (done).
- APPLIED `/keyframe_review/6/to`: The 1158 keyframe ran to 1164 while its own note says '1158-1162 Cantref Mawr only; 1163-1164 nothing' and /ledger/12 strips all lands in 1163. Evidence: Rhys ap Gruffydd page lead: 'Henry invaded Deheubarth in 1163, stripped Rhys of all his lands and took him prisoner'. Fix: Set to 1162 (done).
- APPLIED `/ledger/15, /ledger/16`: The page's subjection to Gwynedd 1234-1283 was not in the ledger. Evidence: Deheubarth page: 'From 1234 to 1283, Deheubarth was subject to the princes of Gwynedd'. kingdom-of-gwynedd dates its overlordship 1259-1277 (its /ledger/50, /ledger/58). Fix: Added vassal_start 1234 and vassal_end 1283 cp kingdom-of-gwynedd, region Carmarthenshire, c2 (done); the Gwynedd owner should reconcile 1259-1277.
- TO DO `/ledger/14 and /keyframe_review/8`: The 1197 loss of Ceredigion to marcher-lordships quotes 'Following his death, most of Deheubarth was taken over by the Normans' as if about the Lord Rhys; on the page that sentence is in the lead's paragraph about Rhys ap Tewdwr (killed 1093). Nothing on the page puts Ceredigion in Norman hands in 1197. Evidence: Rhys ap Gruffydd page (re-checked): the sentence sits in the Rhys ap Tewdwr paragraph; for 1197 the body says Rhys 'died on 28 April 1197' and Maelgwn 'took Aberystwyth' and captured Gruffudd. A misattributed quote (confidence 1). Fix: Drop the 1197 loss (and marcher-lordships /ledger/7), keep Ceredigion in the 1197 keyframe, or replace it with a sourced, dated loss of Ceredigion; then the Principality's 1283 gain of Ceredigion from this state (principality-of-wales /ledger/1) becomes consistent.

Gaps (for a gap-filler):

- `/ledger/3, /ledger/5`: Powys gained 942 and lost 950 at confidence 1 ('probably placed him in control of the Kingdom of Powys'); kingdom-of-powys names kingdom-of-seisyllwg for 942 and has no 950 event. Page to try: https://en.wikipedia.org/wiki/Hywel_Dda
- `/ledger/11-13`: The 1158, 1163 and 1165 events with angevin-empire have no mirror in that dossier (other group). Page to try: https://en.wikipedia.org/wiki/Rhys_ap_Gruffydd

Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/11 confirmed; /ledger/12 confirmed; /ledger/14 not on page.

Area: No Cliopatria shape (new state); infobox 920-1197 (the dossier runs to 1283, documented), capital Dinefwr, no area.

### marcher-lordships: fail

Findings:

- TO DO `/keyframe_review/3-7/correction and /ledger/4/region`: {"admin1": "Powys"} is the whole modern county (Montgomeryshire, Radnorshire, Brecknockshire), so the March is drawn over Powys Wenwynwyn and the Kingdom of Powys from 1100. Evidence: Overlap with kingdom-of-powys-wenwynwyn keyframes: 9-13 H3 cells in 1160-1284. Welsh Marches page: 'By about AD 1100 the March covered the areas which would later become ...' (Monmouthshire, Radnorshire, Brecknockshire, Glamorgan ...); Marcher Lord page names Montgomeryshire only among the shires formed by the 1535-1542 Acts. Fix: Use Powys minus Montgomeryshire until 1283 (needs a gazetteer name, see gazetteer_names_needed, or a polygon) and the whole county from 1284.
- TO DO `/ledger/7 and /keyframe_review/6`: The 1197 gain of Ceredigion (confidence 1) rests on the same misattributed sentence as deheubarth /ledger/14 (it is about Rhys ap Tewdwr, 1093). Evidence: Rhys ap Gruffydd page, lead paragraph on Rhys ap Tewdwr; for 1197 Maelgwn 'took Aberystwyth'. Fix: Drop the 1197 gain and Ceredigion from the 1197 keyframe (and the 1283 loss of Ceredigion at /ledger/8), or source a dated Norman gain of Ceredigion.
- TO DO `/ledger (1215-1277)`: kingdom-of-gwynedd records gains from marcher-lordships in 1215/12, 1234/6, 1257 and 1260/1 (Builth and the upper Wye, the lands beyond Gwynedd proper in Powys, Ceredigion and Carmarthenshire) and passes them to kingdom-of-england in 1277/11; none is mirrored here, so the 1197-1282 keyframe double-fills Gwynedd's 1236 shape. The author flagged it ('no page for them was opened'). Evidence: kingdom-of-gwynedd /ledger/38, /ledger/42, /ledger/48, /ledger/51, /ledger/55-57. Fix: Add the losses (and the 1277 transfers) with the pages the Gwynedd dossier cites, splitting the 1197 keyframe accordingly, or document why the March keeps the land.
- TO DO `/ledger/1, /ledger/3, /ledger/4, /ledger/5, /ledger/9`: Counterparts and years disagree with the existing Welsh dossiers: 1086 Gwent (kingdom-of-gwent dissolved 1074 into kingdom-of-morgannwg, whose 1086 loss of Gwent names norman-england); 1100 Glamorgan (kingdom-of-morgannwg dissolves 1090 to norman-england); 1100 Brecknock (kingdom-of-brycheiniog loses it 1093/4 to lordship-of-brecon, which has no dossier); 1136 Ceredigion (kingdom-of-gwynedd's 1136 gain names norman-england); 1283 Denbigh (kingdom-of-gwynedd lost the Perfeddwlad in 1277/11 to kingdom-of-england). Evidence: The named dossiers' ledgers; Deheubarth page: Rhys ap Tewdwr killed in 1093 'resisting their expansion into Brycheiniog'. Fix: Align each year and counterpart with those dossiers (Brecknock 1093 from kingdom-of-brycheiniog; Glamorgan 1090; Gwent 1086 from kingdom-of-morgannwg), or list them for their owners to rename the counterpart to marcher-lordships; say in notes how norman-england and this dossier divide the March.

Gaps (for a gap-filler):

- `/ledger/9`: 1283 gain of Denbighshire is confidence 1: the Marcher Lord page lists the shires and the 1563 Denbigh grant, no creation date. Page to try: https://en.wikipedia.org/wiki/Marcher_Lord
- `/ledger/10`: 1404 contest_start is confidence 1. Page to try: https://en.wikipedia.org/wiki/Owain_Glynd%C5%B5r

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/7 not on page; /ledger/12 confirmed.

Area: No Cliopatria shape (new state); no infobox area. The Welsh Marches page gives 'about two-thirds of Wales' by about 1100: the 1100 keyframe (about 15,200 km2) is about 73% of Wales (20,800 km2), consistent.

### principality-of-wales: fail

Findings:

- TO DO `/keyframe_review/0`: One shape 1283-1541 although /ledger/2-4 give the whole principality to glyndwr-s-wales in 1404 and back in 1408/1409: the shape double-fills glyndwr-s-wales' 1404 and 1408 keyframes (39 and 17 H3 cells). Evidence: Owain Glyndwr page: 'In 1404, Owain's forces took Aberystwyth Castle and Harlech Castle'; 'by 1408, the English regained Aberystwyth'; Harlech and Aberystwyth captured 'By 1409'. Fix: Split the keyframe at the years of the Glyndwr events (after glyndwr-s-wales is fixed), so that each year has one owner.
- TO DO `/ledger/1`: The 1283 gain of Ceredigion and Carmarthenshire names deheubarth, but deheubarth's 1197-1282 keyframe is Carmarthenshire only and marcher-lordships records the 1283 loss of Ceredigion to this state. Evidence: deheubarth /keyframe_review/8; marcher-lordships /ledger/8. Principality page: the Statute of Rhuddlan put 'Carmarthenshire and Cardiganshire' under the Justiciar of South Wales. Fix: Resolve with deheubarth's 1197 fix: if Ceredigion stays Deheubarth's, keep this event and drop marcher-lordships /ledger/8; otherwise split it.
- TO DO `/keyframe_review/0/correction, /ledger/0/region`: Flintshire is drawn in the Principality; the Principality page says Flintshire was created separately, out of the lordships of Tegeingl, Hopedale and Maelor Saesneg, while the Statute's principality counties are Anglesey, Merioneth, Caernarfon, Carmarthen and Cardigan. Evidence: Principality of Wales page, Statute of Rhuddlan section. Fix: Drop Flintshire or say in the keyframe note why it is drawn here and not with kingdom-of-england or marcher-lordships.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/5 confirmed.

Area: No Cliopatria shape (new state); infobox established 1267 (Treaty of Montgomery: the native principality, carried by kingdom-of-gwynedd per the author) and no area; the page's 'three-quarters of the surface area of modern Wales' is the 13th-century native principality, not this one.

### glyndwr-s-wales: fail

Findings:

- TO DO `/keyframe_review/2/correction, /ledger/3/region`: The 1408-1409 keyframe includes Anglesey, which the page says was lost in 1406. Evidence: Owain Glyndwr page: resistance on Anglesey 'formally ended toward the end of 1406'. Fix: Drop Anglesey from 1407 on, with a dated loss event (cp principality-of-wales) and its mirror gain there.
- TO DO `/keyframe_review/1 -> /keyframe_review/2`: 'Wales' (85 H3 cells, about 21,500 km2) for 1404-1407 shrinks to Gwynedd, Anglesey and Conwy (17 cells) in 1408 with only the Ceredigion loss in the ledger; the decline the page dates is missing. Evidence: Owain Glyndwr page: early 1405 'suffered a series of defeats'; Pwll Melyn 'in May 1405'; 'By 1405, most French forces had withdrawn'; Anglesey end 1406; 'In 1407' English strength 'began to turn the tide'. The lead gives 'the entirety of the country between 1404 and 1405'. Fix: End the all-Wales keyframe at 1405, add dated losses 1405-1407 from that page (mirrored in principality-of-wales and marcher-lordships), and keyframes to match.

Gaps (for a gap-filler):

- `/sources`: One source page (budget 2-5); the Glyndwr Rising page failed for the author. Page to try: https://en.wikipedia.org/wiki/Owain_Glynd%C5%B5r

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.

Area: No Cliopatria shape (rebel state); no infobox area.

### gododdin: fix

Findings:

- APPLIED `/identity/successors/0/slug, /ledger/1/counterpart, /wars/1/belligerents`: The 638 dissolve, the successor and the Din Eidyn siege named kingdom-of-bernicia, whose dossier ends in 634 (merged into Northumbria). Evidence: kingdom-of-bernicia /ledger/5 (634 dissolve cp kingdom-of-northumbria). Gododdin page: 'In 638, Eidyn, modern Edinburgh, was under siege and fell to the Angles'; the Gododdin 'seem to have come under the rule of Bernicia around this time'. kingdom-of-northumbria is a Cliopatria row (612-935) whose group has not run yet. Fix: Set to kingdom-of-northumbria (done, note appended); the 600 Catraeth war keeps kingdom-of-bernicia.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /wars/0 confirmed; /keyframe_review/0 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2.

### kingdom-of-elmet: pass

Gaps (for a gap-filler):

- `/ledger/0`: 450 start is a bridge (confidence 1): 'an independent polity between the 5th century and sometime after the mid-7th century'. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Elmet

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /keyframe_review/0 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2. Tried: extent against the page, end year, counterpart (kingdom-of-northumbria, not yet written); could not break it. Cliopatria's Deira 450 shape overlaps 13 of its 18 cells in 450-533 (Deira owner to subtract).

### kingdom-of-dublin: pass

Gaps (for a gap-filler):

- `/ledger`: The 988 Gaelic conquest by Mael Sechnaill and the later overlordships are not ledger events (no end dates on the page; the author says so). Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Dublin

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /keyframe_review/0 confirmed.

Area: No Cliopatria shape (new state). The infobox read with WebFetch on 2026-10-25 gives no area; nothing to compare. Keyframe areas are the reviewer's H3 cell counts x 253 km2. Tried: extent, both ends, the Leinster mirror (853 matched); could not break it.

### lordship-of-galloway: thin

Gaps (for a gap-filler):

- `/ledger/0`: 1000 start is a bridge (confidence 1): the first recorded king of the Gall-ghaidhil died in 1034 and succession is recorded only from about 1138. Page to try: https://en.wikipedia.org/wiki/Lordship_of_Galloway
- `/ledger`: Fergus resigned Galloway to Mael Coluim IV the year before his death in 1161: the Scottish overlordship from 1160 is not in the ledger. Page to try: https://en.wikipedia.org/wiki/Lordship_of_Galloway
- `/keyframe_review/0`: Dumfries and Galloway includes Annandale and Eskdale, east of the Annan, against the page's 'south and west of the Clyde and west of the River Annan' (author flagged); Carrick is left out. Page to try: https://en.wikipedia.org/wiki/Lordship_of_Galloway

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed.

Area: No Cliopatria shape (new state); the WebFetch result shows no infobox.

### earldom-of-orkney: thin

Gaps (for a gap-filler):

- `/ledger`: The earls' status as 'Norwegian vassals was formalised in 1195' (page) and is not in the ledger; old-kingdom-of-norway has no vassal pair either. Page to try: https://en.wikipedia.org/wiki/Earl_of_Orkney
- `/keyframe_review/0`: The mainland holdings (Caithness and Sutherland, 'periodically subject to the kings of Alba') are not drawn; Caithness became a separate earldom in 1455. Page to try: https://en.wikipedia.org/wiki/Earl_of_Orkney

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.

Area: No Cliopatria shape (new state); the page is a title page without area.

### lordship-of-the-isles: thin

Gaps (for a gap-filler):

- `/ledger`: The lords were 'nominal vassals of the kings of Norway, Ireland, or Scotland' (page); kingdom-of-scotland carries a vassal pair 1294-1493 naming the string 'Lordship of the Isles', but there is no vassal pair here. Page to try: https://en.wikipedia.org/wiki/Lordship_of_the_Isles
- `/ledger/5`: 1475 contest_start is confidence 1 ('In the mid-1470s'). Page to try: https://en.wikipedia.org/wiki/John_MacDonald,_Earl_of_Ross
- `/ledger (1386-1437)`: No event for Donald and Alexander (Harlaw 1411 and the Ross claim) between the pages opened (author gap). Page to try: https://en.wikipedia.org/wiki/Battle_of_Harlaw

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/7 confirmed; /ledger/8 confirmed.

Area: No Cliopatria shape (new state); the WebFetch result shows no infobox.

### airgialla: thin

Findings:

- APPLIED `/ledger/1, /ledger/2`: tir-eoghain records a vassal pair 827-1130 over this state; no mirror here. Evidence: tir-eoghain /ledger/1-2; Airgialla page: 'From 735 they fell under the dominance of the Cenel nEogain, and by 827 had become their vassals'; no end date (the 1130 end is tir-eoghain's bridge at c1). Fix: Added vassal_start 827 (c2) and vassal_end 1130 (c1) cp tir-eoghain (done).

Gaps (for a gap-filler):

- `/ledger/3, /ledger/4`: Both 1189 losses (Armagh and Fermanagh to 'Gaelic lordships of Ulster'; Louth to lordship-of-ireland) are page-silent bridges (confidence 1) and the Lordship has no matching gain. Page to try: https://en.wikipedia.org/wiki/Airg%C3%ADalla
- `/ledger/0`: 450 start instead of the infobox 331 (documented: avoids overlapping Ulaid). Page to try: https://en.wikipedia.org/wiki/Airg%C3%ADalla

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.

Area: No Cliopatria shape (new state); infobox 331-1585, no area ('roughly matched the modern dioceses of Armagh and Clogher').

### tir-eoghain: fail

Findings:

- TO DO `/keyframe_review/0/correction`: Tyrone, Derry, Limavady and Inishowen from 465 to 1606, but the page says Eoghan's territory was 'initially based in Inishowen' and the Ulaid page keeps the Ulaid west of the Bann until the 8th century: ulaid's 450 keyframe and this one double-fill all 23 cells in 465-699. Evidence: Tir Eoghain page: 'initially based in Inishowen'; 'Upon its foundation in the 5th century, Tyrone was a sub-kingdom of the larger Aileach'. Ulaid page: 'By the 8th century the territory of the Ulaid shrunk to east of the Bann'. Fix: Start with Inishowen in 465; add the move into Tyrone and Derry as a gain from ulaid (mirroring ulaid's 8th-century loss, confidence 1) with a keyframe from that year.
- TO DO `/ledger/5 (1603-1606)`: kingdom-of-ireland draws the whole island from 1603 while this state lives to 1607 (author flagged). Evidence: kingdom-of-ireland /keyframe_review/3. Fix: Settle with kingdom-of-ireland (its fix): a 1607 gain there, or a vassal pair 1603-1607 in both.

Gaps (for a gap-filler):

- `/identity`: Status 'Tuatha of Ailech (until 1185)': the Ailech overkingdom is not represented; the Ailech split is '12th century' and '13th century' on the same page. Page to try: https://en.wikipedia.org/wiki/T%C3%ADr_Eoghain
- `/ledger/2`: 1130 vassal_end over airgialla is a bridge (confidence 1). Page to try: https://en.wikipedia.org/wiki/Airg%C3%ADalla

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.

Area: No Cliopatria shape (new state); infobox 5th century-1607, no area.

## Cross-dossier matrix (not matched only)

- lordship-of-ireland 1171 gain cp kingdom-of-leinster: mismatch. Years match; land does not: this gain is the gazetteer's modern province of Leinster (with Meath, Westmeath, Longford, Louth, Offaly), the loss is the medieval kingdom.
- lordship-of-ireland 1333 loss cp Gaelic and Burke lords of Connacht and Ulster: exception. Collective Gaelic and Burke lords; no state.
- lordship-of-ireland 1348 loss cp Gaelic Irish lordships (the Gaelic resurgence): exception. Collective Gaelic lordships; no state. kingdom-of-leinster regains part of this land in 1375 naming lordship-of-ireland instead.
- kingdom-of-ireland 1556 gain cp Gaelic Irish lordships of Laois and Offaly: exception. Gaelic lordships of Laois and Offaly; no state.
- kingdom-of-ireland 1583 gain cp earldom-of-desmond: mismatch. earldom-of-desmond dissolves 1583/11 naming kingdom-of-england as counterpart and successor; it should name kingdom-of-ireland (other eu-11 part).
- kingdom-of-ireland 1603 gain cp Gaelic Irish lordships (Tyrone's confederacy and the rest): exception. Collective; but this gain also covers kingdom-of-thomond (dissolved 1543), kingdom-of-desmond (1596), airgialla (1585) and tir-eoghain (1607), none of which has a matching gain here.
- kingdom-of-ireland 1642 loss cp irish-catholic-confederation: mismatch. irish-catholic-confederation's 1642/10 found names kingdom-of-england as counterpart and predecessor.
- kingdom-of-ireland 1653 merge cp commonwealth-of-england: mismatch. commonwealth-of-england gains Ireland piecemeal from irish-catholic-confederation 1650-1652 and has no merge with kingdom-of-ireland.
- kingdom-of-ireland 1660 split cp commonwealth-of-england: mismatch. commonwealth-of-england's 1660/5 dissolve passes England, Wales and Ireland to kingdom-of-england.
- picts 741 vassal_start cp dal-riata: missing. dal-riata has contest_end 741 cp picts but no vassal_start.
- picts 850 vassal_end cp dal-riata: missing. dal-riata ends in a merge 850 cp picts (matched below) with no vassal_end; acceptable once its vassal_start exists.
- kingdom-of-leinster 1375 gain cp lordship-of-ireland: mismatch. lordship-of-ireland has no 1375 loss; it lost this land in 1348 to 'Gaelic Irish lordships (the Gaelic resurgence)'.
- kingdom-of-connacht 1050 gain cp nobody: exception. Counterpart nobody: the page names no state the Ui Briuin took it from.
- kingdom-of-munster 600 gain cp Osraige (Ossory): exception. Osraige (Ossory) has no dossier; listed under counterparts_needing_dossiers.
- ulaid 450 loss cp airgialla: mismatch. airgialla's 450 found region is Armagh, Monaghan, Fermanagh and Louth; this loss is Armagh only.
- ulaid 499 vassal_start cp dal-riata: missing. dal-riata (other group) has no vassal events with ulaid; its 498 found names ulaid as predecessor.
- ulaid 575 vassal_end cp dal-riata: missing. As above.
- ulaid 700 loss cp airgialla: missing. airgialla has no 700 gain; most of the land west of the Bann is tir-eoghain's (author flagged).
- dyfed 690 loss cp kingdom-of-seisyllwg: exception. kingdom-of-seisyllwg is a Cliopatria row (878-959) of another eu-11 part, not yet written.
- deheubarth 942 gain cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/11 names kingdom-of-seisyllwg for the 942 loss (author flagged).
- deheubarth 942 gain cp kingdom-of-powys: mismatch. kingdom-of-powys /ledger/7 names kingdom-of-seisyllwg for the 942 loss.
- deheubarth 950 loss cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/12 names kingdom-of-seisyllwg for the 950 regain.
- deheubarth 950 loss cp kingdom-of-powys: missing. kingdom-of-powys has no 950 event.
- deheubarth 1055 loss cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/14 takes Deheubarth in 1055 from brythons.
- deheubarth 1063 gain cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/18 loses it in 1063 to brythons.
- deheubarth 1158 loss cp angevin-empire: missing. angevin-empire (1147-1209) has no Deheubarth event.
- deheubarth 1163 loss cp angevin-empire: missing. As above.
- deheubarth 1165 gain cp angevin-empire: missing. As above.
- deheubarth 1234 vassal_start cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/50 dates the overlordship from 1259 (vassal_start cp deheubarth); the Deheubarth page says 1234. Reviewer-added event.
- deheubarth 1283 vassal_end cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/58 ends it 1277/11. Reviewer-added event.
- marcher-lordships 1086 gain cp kingdom-of-gwent: mismatch. kingdom-of-gwent dissolved 1074 into kingdom-of-morgannwg; morgannwg's 1086 loss of Gwent names norman-england.
- marcher-lordships 1100 gain cp kingdom-of-morgannwg: mismatch. kingdom-of-morgannwg dissolves 1090 to norman-england.
- marcher-lordships 1100 gain cp kingdom-of-brycheiniog: mismatch. kingdom-of-brycheiniog loses Brycheiniog 1093/4 to lordship-of-brecon (no dossier; folded into marcher-lordships by the author).
- marcher-lordships 1136 loss cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd /ledger/28-29 gains Ceredigion 1136-1137 from norman-england.
- marcher-lordships 1283 loss cp principality-of-wales: missing. principality-of-wales gains Ceredigion in 1283 from deheubarth, not from this state.
- marcher-lordships 1283 gain cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd lost the Perfeddwlad (Denbighshire) 1277/11 to kingdom-of-england.
- principality-of-wales 1283 gain cp deheubarth: mismatch. Ceredigion is not in deheubarth's 1197-1282 keyframe; marcher-lordships records its 1283 loss to this state.
- lordship-of-the-isles 1346 gain cp Lordship of Garmoran: exception. Lordship of Garmoran has no dossier; listed.
- lordship-of-the-isles 1350 gain cp kingdom-of-scotland: missing. kingdom-of-scotland has no 1350 loss of Knapdale and Kintyre.
- lordship-of-the-isles 1376 gain cp kingdom-of-scotland: missing. kingdom-of-scotland has no 1376 loss of Lochaber.
- lordship-of-the-isles 1438 gain cp Earldom of Ross: exception. Earldom of Ross has no dossier; listed.
- lordship-of-the-isles 1476 loss cp kingdom-of-scotland: missing. kingdom-of-scotland has no 1476 gain of Ross, Skye, Knapdale and Kintyre (author noted).
- airgialla 1189 loss cp Gaelic lordships of Ulster: exception. Collective Gaelic lordships; no state.
- airgialla 1189 loss cp lordship-of-ireland: missing. lordship-of-ireland has no 1189 gain of Louth (it draws Louth from 1171 through the modern 'Leinster' region).
- kingdom-of-thomond 1543 dissolve cp kingdom-of-ireland: missing. No 1543 gain in kingdom-of-ireland; the land is drawn by nobody 1543-1583.
- kingdom-of-desmond 1596 dissolve cp kingdom-of-ireland: mismatch. kingdom-of-ireland has no 1596 gain and already draws Cork and Kerry from 1584 (Munster keyframe).
- airgialla 1585 dissolve cp kingdom-of-ireland: missing. No 1585 gain of Monaghan in kingdom-of-ireland.
- tir-eoghain 1607 dissolve cp kingdom-of-ireland: mismatch. kingdom-of-ireland takes the whole island in 1603; four years of double fill (author flagged).
- kingdom-of-connacht 1474 dissolve cp lordship-of-ireland: mismatch. After the reviewer's counterpart fix the Lordship ends the vassalage but takes no land; Roscommon is drawn by nobody after 1474.
- kingdom-of-great-britain 1707 vassal_start cp kingdom-of-ireland: missing. No vassal pair 1707-1800 in kingdom-of-ireland.
- earldom-of-orkney 1472 dissolve cp kingdom-of-scotland: mismatch. kingdom-of-scotland's 1472 gain of Orkney and Shetland names kalmar-union.
- lordship-of-the-isles 1493 dissolve cp kingdom-of-scotland: mismatch. kingdom-of-scotland's vassal pair (1294 c1 - 1493) names the string 'Lordship of the Isles' and starts 42 years before this dossier.
- marcher-lordships 1536 dissolve cp kingdom-of-england: mismatch. kingdom-of-england's 1542 gain of 'the principality and the Marcher lordships' names principality-of-wales only, six years after this dissolve.
- principality-of-wales 1283 found cp kingdom-of-gwynedd: mismatch. kingdom-of-gwynedd dissolves 1283/6 naming kingdom-of-england as counterpart and successor.
- kingdom-of-gwynedd 1215 gain cp marcher-lordships: missing. No loss in marcher-lordships (author flagged; kingdom-of-gwynedd /ledger/38).
- kingdom-of-gwynedd 1234 gain cp marcher-lordships: missing. No loss in marcher-lordships (author flagged; kingdom-of-gwynedd /ledger/42).
- kingdom-of-gwynedd 1257 gain cp marcher-lordships: missing. No loss in marcher-lordships (author flagged; kingdom-of-gwynedd /ledger/48).
- kingdom-of-gwynedd 1260 gain cp marcher-lordships: missing. No loss in marcher-lordships (author flagged; kingdom-of-gwynedd /ledger/51).
- dal-riata 612 gain cp picts: missing. No 612 loss of Skye in picts (confidence 1 on the Dal Riata side).
- dal-riata 644 loss cp ulaid: missing. No 644 gain of north-east Antrim in ulaid.
- kingdom-of-england 1236 gain cp kingdom-of-connacht: mismatch. Connacht's 1235 loss names lordship-of-ireland; England draws Irish cells itself (author's problem 1).
- kingdom-of-england 1272 loss cp kingdom-of-connacht: missing. No 1272 gain in kingdom-of-connacht.
- kingdom-of-england 1326 loss cp kingdom-of-leinster: missing. No 1326 gain in kingdom-of-leinster (it regains land only in 1375).
- lordship-of-ireland 1315 contest_start cp kingdom-of-scotland: missing. kingdom-of-scotland has no Bruce contest pair 1315-1318 in Ireland.
- lordship-of-the-isles 1475 contest_start cp kingdom-of-scotland: missing. kingdom-of-scotland has no 1475-1476 contest pair.

## Gazetteer names that would replace coordinate circles or over-wide names

Leinster (medieval kingdom, without Meath, Westmeath, Longford and Louth) (region, lordship-of-ireland), Brecknockshire (region, marcher-lordships), Radnorshire (region, marcher-lordships), Montgomeryshire (region, marcher-lordships), Cantref Mawr (region, deheubarth), Ystrad Tywi (region, dyfed), Islay (region, lordship-of-the-isles), Mull (region, lordship-of-the-isles), Lewis (region, lordship-of-the-isles), Skye (region, lordship-of-the-isles), Kintyre (region, lordship-of-the-isles), Knapdale (region, lordship-of-the-isles), Lochaber (region, lordship-of-the-isles), Garmoran (region, lordship-of-the-isles), Earldom of Ross (region, lordship-of-the-isles), Inishowen (region, tir-eoghain), Sycharth (place, glyndwr-s-wales), Annandale (region, lordship-of-galloway), Caithness (region, earldom-of-orkney).

## Counterparts needing dossiers

- Kingdom of Osraige (Ossory) (kingdom-of-osraige): counterpart of kingdom-of-munster 600/900 and kingdom-of-leinster 900; author-listed
- Lordship of Garmoran (lordship-of-garmoran): lordship-of-the-isles 1346; author-listed
- Earldom of Ross (earldom-of-ross): lordship-of-the-isles 1438; author-listed
- Lordship of Brecon (Brecknock) (lordship-of-brecon): successor of kingdom-of-brycheiniog (its 1093/4 loss); marcher-lordships folds it in, so either write it or rename brycheiniog's counterpart
- Earldom of Carrick (earldom-of-carrick): author-listed
- Waterford (Norse) (waterford): author-listed
- Kingdom of Limerick (Norse) (kingdom-of-limerick): author-listed
- Kingdom of Breifne (kingdom-of-breifne): author-listed
- Tir Chonaill (Tyrconnell) (tir-chonaill): author-listed; also the second leader of the 1593-1603 Ulster confederacy

## Problems

- Section 6 Context table of the author's brief lists far-away polities (French counties, Ashanti, Haudenosaunee, Habsburg Monarchy ...); none is a counterpart of this batch. Cross-checks used the counterparts named in the ledgers instead: kingdom-of-england, kingdom-of-scotland, kingdom-of-gwynedd, kingdom-of-powys, kingdom-of-powys-wenwynwyn, kingdom-of-gwent, kingdom-of-morgannwg, kingdom-of-brycheiniog, dal-riata, kingdom-of-bernicia, kingdom-of-deira, angevin-empire, norman-england, earldom-of-desmond, earldom-of-ulster, irish-catholic-confederation, commonwealth-of-england, kingdom-of-great-britain, united-kingdom, old-kingdom-of-norway, brythons. Not yet written (groups not run): kingdom-of-alba, kingdom-of-northumbria, kingdom-of-seisyllwg, kalmar-union.
- Verdict convention used: fail > thin > fix > pass. A dossier where the reviewer applied fixes but blocking findings remain is 'fail' (kingdom-of-ireland, deheubarth); one where applied fixes leave only page-silent gaps is 'thin' (airgialla). Every applied fix is marked applied: true and noted inside the dossier with '[Reviewer eu-11-x, 2026-10-25]'.
- Edited and re-validated (0 errors, 0 warnings with --resolve): kingdom-of-connacht, airgialla, kingdom-of-ireland, gododdin, deheubarth. Backups of the pre-review files are in /tmp/claude-0/work/eu-11-x/backup/.
- Kingdom of Connacht page: the WebFetch result shows an empty infobox. Glyndwr rising: both 'Glyndwr_Rising' (author) and 'Glyndwr_rising' (reviewer) return url_not_found.
- No confidence-3 event was found fabricated or mis-dated (111 spot checks on 39 distinct pages, plus about 15 further pages opened for context). One confidence-1 pair (deheubarth /ledger/14 and marcher-lordships /ledger/7, 1197) cites a sentence that on the page concerns 1093.
- Regions: the gazetteer's 'Leinster' and 'Munster' are the modern provinces; 'Powys' is the modern county; 'The Pale' is a 50 km circle round Dublin (confidence 2). Several of this batch's overlaps come from those names, worth a gazetteer note.
