# Review of batch eu-11-g (2026-10-25)

Reviewer: adversarial Phase B review. Dossiers: kingdom-of-northumbria, strathclyde, cornwall, danelaw, kingdom-of-seisyllwg, kingdom-of-alba. All six pass the validator with --resolve (0 errors; danelaw's two intended "resolves to no cells" warnings). The machine copy of this review is history/notes/phase-b/reviews/eu-11-g.json.

Verdict rule: a finding that needs the author to change what the dossier already says (a keyframe correction or verdict that contradicts the dossier's own confirmed ledger, a mis-typed event) is blocking and gives fail. A finding that only adds missing events, mirrors or years within the page budget gives thin.

| slug | verdict | why |
| --- | --- | --- |
| kingdom-of-northumbria | fail | keyframes 926-954 keep the Carlisle cells the 900 loss gives away; Eamont 927 coded as a rename against England's vassal pair |
| strathclyde | fail | Kyle (c3 loss in 750) is inside every shape from 750 on, and the note says it is not; the 870 correction adds Cumbria 30 years early; the Cumbria cells don't match Northumbria's |
| cornwall | thin | thin by design (2 shapes, 1-2 pages); Wessex vassal tie unmirrored |
| danelaw | thin | one reviewer fix applied (area figure); Five Boroughs 940-942 missing |
| kingdom-of-seisyllwg | thin | 918 vassal tie to Wessex missing; start 878 vs page 872 / c. 680 |
| kingdom-of-alba | thin | Moray, Cumbria 1034-1092, vassal mirrors, 1266 counterpart, no capital |

## kingdom-of-northumbria: fail
Spot checks, all confirmed: 638 Gododdin (Gododdin page), 867 York (21 March 867), 671/674/679/685 (Ecgfrith page), 656/659 (Oswiu page), 633/634 and 927 (Bernicia page), 954 (Northumbria infobox). The infobox has no area.

Blocking:
1. /keyframe_review/15 (926-935, verdict ok) and /keyframe_review/16/correction (936-954, 935 shape) keep the 6 Cumbrian cells near Carlisle (intersect(Northumbria 900, Cumbria) = 6 cells, about 1,517 km2) that /ledger/24 gives to Strathclyde in 900. Keyframe 14's text says "minus the Cumbrian cells" but no spec removes them. Fix: keyframe 15 becomes adjust with the 926 shape minus admin1 Cumbria; keyframe 16 gets the same minus on the 935 shape.
2. /ledger/25 codes the Eamont submission as a rename. kingdom-of-england has vassal_start kingdom-of-northumbria 927 (c3) and vassal_end 954. Bernicia page: "In 927 Ealdred accepted West Saxon overlordship"; infobox: "Bernicia accepts the rule of King Æthelstan: 927". Fix: make it a vassal_start (counterpart kingdom-of-england, month 7) and add a vassal_end at 954 before the dissolve.

Also:
3. A gain of Kyle in 750 is missing. Strathclyde /ledger/1 (c3, confirmed: "Kyle was taken from Alt Clut by Eadberht of Northumbria") has no mirror here, and no Northumbria shape holds East Ayrshire. Add the gain and an adjust on keyframe 11.
4. The Wessex dossier has a vassal tie 829-830 (Dore) with no mirror here. The Northumbria page is silent: add the tie from the Egbert of Wessex page, or explain why there is none.
5. Gaps (confidence 1): 626 Dunoting, 647 Rheged (page: "some time before AD 730"), 705 (+2 cells), 750 (-1 cell). There are no rulers.

## strathclyde: fail
Spot checks: 750 Kyle confirmed (Óengus I page). 750 Dál Riata is not on the page (c1, said so in the note). 900 Cumbria confirmed (Rheged page). The 1033 end is confirmed: the Strathclyde page says conquered by the Scots between 1018 and 1054, most likely under Máel Coluim (d. 1034), and the infobox says c. 1030. The capitals Dumbarton and then Govan are confirmed. The infobox has no area.

Blocking:
1. /keyframe_review/2 and the later shapes: intersect(East Ayrshire, Strathclyde 750) = 6 of East Ayrshire's 7 cells. Kyle is therefore inside the shape, and the note's claim that it is not is false. /ledger/1 (c3) removes it with no keyframe trace. Fix: keyframe 2 becomes adjust with the 750 shape minus East Ayrshire. Carry the same minus into the 870-1028 corrections, unless a page returns Kyle. Correct the two notes.
2. /keyframe_review/3/correction adds Cumbria from 870, but the ledger dates the Cumbria gain c. 900. A correction is the shape at the keyframe's first year. Fix: give the Clyde shape alone and let the ledger carry the 900 gain, or add a new keyframe for 900-959.
3. /ledger/3 and the 960/980/1028 corrections take Cumbria as intersect(Cumbria, Brythons 900) = 20 cells. Northumbria's 900 loss hands Strathclyde 6 other cells, and neither dossier draws them. Fix: use the union of both, or the whole admin1 Cumbria.

Also:
4. The /ledger/4 dissolve region is the 1033 shape without the Cumbria that keyframe 6 adds, and it names no counterpart. Name kingdom-of-alba and use the corrected shape.
5. Gaps: the 750 Dál Riata loss (c1); the 927 Eamont vassal tie and its 937 end, mirroring England /ledger/4 and /ledger/8; the 945 grant to Malcolm I (Edmund I page: "in return for a pledge to defend it"); no rulers.

## cornwall: thin (by design)
Confirmed: Æthelstan page (Exeter and the Tamar, "an improbable story"); Cornwall page (Tamar 936; 815, 825, 838, 875). Area: the infobox gives 3,562 km2 for the modern county against Cliopatria's 4,538.5 km2. That is a ratio of 1.27, and the author acknowledges it. The 946 dissolve is not on the page (c1, honest).

Gaps:
- Found 710 and dissolve 946 are both confidence 1.
- Wessex /ledger/13 has a vassal tie to Cornwall from 825 with no mirror here and no end on the Wessex side. Add a vassal_start (838, Hingston Down, has the better support) with a vassal_end at 946, or have Wessex drop its tie.
- The land east of the Tamar before 936 is not drawn. There is no capital and there are no rulers.

## danelaw: thin
Fix applied by the reviewer: /keyframe_review/0/note quoted 49,568 km2, which is the 196-cell count. shapes.csv gives 45,806.7 km2, so the note now reads "45,807 km2 in shapes.csv (about 49.6 thousand by cell count)". Re-validated with 0 errors and read back.

Confirmed:
- Edward the Elder page: 915, 917 and 918 events; Lincoln unclear.
- Æthelstan page: 927 and 939.
- Kingdom of York page: 944, 947, 950-952 and 954.
- Danelaw page: the 878-890 treaty, Guthrum settled, and the 954 end.

The infobox has no area.

Gaps:
- **Five Boroughs, 940 and 942.** Olaf Guthfrithson gained the Five Boroughs in 940 and Edmund recovered them in 942. Edmund I page: "They arranged a treaty at Leicester which surrendered the Five Boroughs"; "In 942, he recovered the Five Boroughs." The ledger and keyframes need these: a gain from kingdom-of-england in 940, a loss in 942, and a new keyframe for 940-941.
- **880 gain.** It is confidence 1. The Mercia dossier dates the partition to 877 (c3); try the Ceolwulf II of Mercia page.
- **Capital span.** York runs 878-954 without a break through the no-land years 927-938 and 944-946. Split the span (non-blocking).

## kingdom-of-seisyllwg: thin
Confirmed:
- Cadell page: Dyfed 904-905; death 909.
- Seisyllwg page: merger in 920; it gives Cadell's death as 911, and the note records the difference.
- Found 878: Cadell page as described; the year is Cliopatria's, as the note says.

The infobox has no area.

Gaps:
- Wessex /ledger/37 (918 vassal_start kingdom-of-seisyllwg, c3) has no mirror. Edward the Elder page: "Three Welsh kings, Hywel Dda, Clydog and Idwal Foel ... gave their allegiance to Edward" (918). Add a vassal_start in 918 and a vassal_end at the 920 merger.
- The life starts at Cliopatria's 878. Cadell was king from 872 (Cadell infobox "Reign 872-909"), and the kingdom dates from the 7th or 8th century (infobox: changed name from Ceredigion, 680). dyfed /ledger/1 names this slug in 690. Extend the start or re-target Dyfed.
- There is no capital and there are no rulers.

## kingdom-of-alba: thin
Confirmed:
- Alba page: 900-1286; Moray excluded "until the early 13th century".
- Bernicia page: 973 Lothian.
- David I page: January and February 1136; 9 April 1139.
- Treaty of Perth page: 2 July 1266; Largs 1263.
- Malcolm IV page: 1157.
- Strathclyde page: 1034.

The Alba page has no infobox, so there is no area to compare.

Gaps:
- **Moray.** All shapes from 900 hold Moray and 67 Highland cells, 79 of the 173 cells in the 900 shape, all with verdict ok, against the page. This needs a Moray dossier and a dated cut or vassal tint (try the Province of Moray page).
- **Cumbria 1034-1092.** No Alba shape has Cumbria in 1034-1091, but Strathclyde holds it to 1033 and norman-england /ledger/4 (1092, c3) takes it from Alba. Add it to the 1034 gain and the 1034/1072 keyframes, and add a 1092 loss.
- **Vassal mirrors.** These neighbour ties have no mirror here:
  - England, 927-937. Æthelstan page: Constantine II at Eamont on 12 July 927; in 934 Æthelstan "forced Constantine II to submit".
  - North Sea Empire, 1031-1035.
  - Angevin Empire, 1174-1189 (Falaise and Canterbury).
- **1099.** The gain is confidence 1 and has no Isles mirror.
- **1266 counterpart.** The gain names old-kingdom-of-norway, which has no loss; kingdom-of-the-isles /ledger/7 holds the loss to Alba. Re-target, or have Norway add a loss. The Isle of Man is in no Alba shape.
- **Capital and rulers.** There is no capital (Scone) and there are no rulers.

## Neighbour-side defects (route to their authors)
- **kingdom-of-england:** the York interlude of 939-944 is missing. The 927 vassal_start and 959 vassal_end with kingdom-of-seisyllwg should name deheubarth: the Æthelstan page says "Hywel Dda of Deheubarth".
- **kingdom-of-wessex:** /ledger/40 gains from the Danelaw in 927, which duplicates England /ledger/1. The 825 Cornwall vassal tie has no end.
- **brythons:** /ledger/20 (638) duplicates the Gododdin loss. /ledger/24 (900) duplicates Strathclyde's gain of Cumbria. /ledger/25 and /ledger/27 (911 and 960) name kingdom-of-seisyllwg, which has no mirror (911) or has already ended (960).
- **dyfed:** has no 905 loss to Seisyllwg (Cadell page: conquered 904-905). /ledger/1 (690) predates Seisyllwg's start.
- **kingdom-of-mercia:** /ledger/10 is a contest in 674, where the Ecgfrith page has Ecgfrith seize Lindsey.
- **picts:** has no Northumbrian overlordship for 671-685.
- **kingdom-of-gwynedd and kingdom-of-powys:** the 942-960 events should name deheubarth.
- **kingdom-of-lindsey:** dissolves in 625 with no counterpart.
- **kingdom-of-gwynedd:** gives Anglesey as 629, against Northumbria's 627.
- **dal-riata:** /ledger/2 (642) names strathclyde before it starts.
- **old-kingdom-of-norway:** has no 1266 loss.
- **norman-england:** has no pair for the occupation of January-February 1136.
