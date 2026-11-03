# Review of batch eu-10-g (France part g), 2026-10-25

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Validator (--resolve): 0 errors in all five dossiers before and after the reviewer's edits; warnings only for gazetteer names (Nébouzan, Faucigny). Reviewer edits are marked '[Reviewer eu-10-g ...]' in the notes of the events they touch.

Verdicts: county-of-foix **fail**, county-of-artois **pass**, capetian-house-of-anjou **fix**, dauphine **thin**, principality-of-orange **fix**

## county-of-foix: fail

Area: infobox/body 2466 km2 (year 1789), Cliopatria 4585.8 km2, ratio 1.86, acknowledged True. No infobox area; body: 'as it existed just before the French Revolution, had a land area of 2,466 km2'. No Cliopatria shape is alive in 1789; compared with the Foix-proper shape of 1236 (keyframe 0 note).

Findings:
- `/ledger/13` (NOT applied, for the author): The 1479 gain of Navarre from kingdom-of-navarre has no mirror: kingdom-of-navarre records a rename in 1479 and keeps Navarre (keyframe kingdom-of-navarre_1463, 1463-1511), so the 33 Navarra cells are drawn by two states 1479/1482-1511; the overlap is not flagged in the notes or report. Evidence: kingdom-of-navarre /ledger/16 (1479 rename), its keyframe 1463-1511 holds Navarre; gazetteer check: Cliopatria County of Foix 1482 shape holds 33 of 33 Navarra cells. Kingdom of Navarre page: Lower Navarre 'survived as an independent kingdom which passed by inheritance'. Fix: Treat 1479-1512 as a personal union, not a gain: subtract the Navarra cells from keyframes /keyframe_review/10, 11, 12, 13, 14 and 15 (corrections 'minus' {admin1: Navarra}), drop /ledger/13, and move the Navarre events /ledger/18-23 to notes (kingdom-of-navarre already carries the 1512 loss and Lower Navarre to 1620); or, if the orchestrator decides Foix draws Navarre, kingdom-of-navarre must record the 1479 loss. Say which in notes.
- `/ledger/4/counterpart` (applied by reviewer): Counterpart was county-of-bearn, a dossier that starts in 1347, so the 1290 gain could not have a mirror. Evidence: county-of-bearn identity.start 1347; Roger-Bernard III page: 'when he died in 1290, Roger-Bernard immediately took possession of his counties (May)'; County of Foix page: 'he inherited Béarn and Nébouzan from his father-in-law in 1290'. Fix: counterpart 'Viscounty of Béarn (Gaston VII, father-in-law)'.
- `/ledger/23/region` (applied by reviewer): The 1530 gain of Lower Navarre used region 'Navarre', which the gazetteer resolves to Spanish Navarra (Upper Navarre, 33 cells), so the event drew Upper Navarre back into Foix. Evidence: Henry II of Navarre page: 'In 1530, after the Treaty of Cambrai ... Charles V evacuated' Lower Navarre, 'allowing Henry to seize it'; regions.jsonl: Navarre = {admin1: Navarra, country: Spain}. Fix: region {intersect: [Pyrénées-Atlantiques, disk -1.15/43.22 25 km]} with text 'Lower Navarre ...' (6 cells).
- `/ledger/15/counterpart` (NOT applied, for the author): The 1484 Périgord/Limousin gain names county-of-perigord, whose dossier dissolves into county-of-foix in 1481 (c1); the page puts Périgord with the Albret from 1470, so the land came to Foix with the Albret marriage of 1484. Evidence: House of Albret page: 'In 1470, they inherited the County of Périgord and the Viscounty of Limoges'; Jean d'Albret 'became King of Navarre by his marriage with Catherine of Foix ... in 1484'. county-of-perigord /ledger/8: 1481 dissolve to county-of-foix. Fix: counterpart 'Lordship of Albret' (merge /ledger/15 into /ledger/16 or keep separate with that counterpart); county-of-perigord's group should move its successor to the Albret (1470). Not blocking on this side.

Gaps (thin):
- `/ledger/0`: found 1236 at confidence 1 (Cliopatria's first shape); the county dates from the mid-11th century (Roger I, d. c.1064); no ruler strip (try https://en.wikipedia.org/wiki/List_of_counts_of_Foix)
- `/keyframe_review/8`: 1453 shape grows 12,642 -> 16,425 km2 (Bigorre and Haute-Garonne cells), no event (try https://en.wikipedia.org/wiki/Gaston_IV,_Count_of_Foix)
- `/keyframe_review/14`: 1502 shape loses about 4,000 km2 (Haute-Garonne, Ariège, half of Hautes-Pyrénées), no event; probably the Foix succession dispute with the Narbonne branch (try https://en.wikipedia.org/wiki/Gaston_of_Foix,_Duke_of_Nemours)
- `/keyframe_review/3`: Marsan and Gabardan (held by 1364) and Castelbon not dated or drawn (try https://en.wikipedia.org/wiki/Gaston_III,_Count_of_Foix)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Roger-Bernard_III,_Count_of_Foix: confirmed (paréage 8 September 1278)
- `/ledger/4` https://en.wikipedia.org/wiki/Roger-Bernard_III,_Count_of_Foix: confirmed (May 1290); counterpart corrected
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Foix: confirmed (Béarn and Nébouzan from his father-in-law in 1290)
- `/ledger/11` https://en.wikipedia.org/wiki/County_of_Foix: confirmed (1447 bought the viscounty of Narbonne)
- `/ledger/17` https://en.wikipedia.org/wiki/County_of_Foix: confirmed (1507 exchanged Narbonne with Louis XII for Nemours)
- `/ledger/13` https://en.wikipedia.org/wiki/Kingdom_of_Navarre: confirmed (Eleanor reigned 15 days, left the crown to Francis Phoebus)
- `/ledger/15` https://en.wikipedia.org/wiki/House_of_Albret: confirmed for 1484 (marriage); page dates the Albret acquisition of Périgord to 1470
- `/ledger/20` https://en.wikipedia.org/wiki/Kingdom_of_Navarre: confirmed (18 July 1512 invasion; towns captured by September)
- `/ledger/21` https://en.wikipedia.org/wiki/Henry_II_of_Navarre: confirmed (Pamplona May 1521, Noain June 1521)
- `/ledger/23` https://en.wikipedia.org/wiki/Henry_II_of_Navarre: confirmed year 1530; region was wrong (fixed)
- `/ledger/24` https://en.wikipedia.org/wiki/Henry_II_of_Navarre: confirmed (died at Hagetmau 24 May 1555; succeeded by Jeanne III and Antoine)

## county-of-artois: pass

Area: infobox/body 4000 km2 (year None), Cliopatria 7566.3 km2, ratio 1.89, acknowledged True. No infobox area; body 'around 4,000 square kilometres' (present day). Acknowledged in /keyframe_review/0.

Gaps (thin):
- `/ledger/3`: dissolve 1332 is Cliopatria's date (c2); the page has Joan III inheriting in 1330 and Artois joining the Duchy of Burgundy in 1384, reverting to Margaret in 1361; the county 1333-1659 is in no written dossier (free-county-of-burgundy 1333-1384 not written yet) (try https://en.wikipedia.org/wiki/County_of_Artois)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Robert_I_of_Artois: confirmed ('on attaining his majority in 1237', will of his father; Count of Artois 1237-1250)
- `/ledger/1` https://en.wikipedia.org/wiki/County_of_Artois: confirmed (Mahaut's death 1329, Artois to Joan II)
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Artois: confirmed (Joan II died 1330, Artois and Franche-Comté to Joan III, married Odo IV 1330)
- `/ledger/3` https://en.wikipedia.org/wiki/County_of_Artois: not on page (Cliopatria end date, confidence 2, acknowledged in notes)

## capetian-house-of-anjou: fix

Area: infobox/body None km2 (year None), Cliopatria 59625.8 km2, ratio None, acknowledged True. Dynasty article and Provence page have no area (confirmed on the dynasty page); nothing to compare.

Findings:
- `/ledger/1/region` (applied by reviewer): The 1251 Provence gain used the gazetteer region Provence, which includes Alpes-de-Haute-Provence (26 cells), the Forcalquier land that /ledger/2 gains again in November 1256. Evidence: Charles I of Anjou page: Beatrice of Savoy claimed Forcalquier; in November 1256 'Louis IX persuaded her to return Forcalquier to Charles'. Fix: region {minus: [Provence, Alpes-de-Haute-Provence]}.

Gaps (thin):
- `/keyframe_review/4`: what the Angevins held in Piedmont after the Col de Tende defeat (1276); the shape keeps Cuneo/Turin cells to 1374 with no event (Angevin Piedmont was regained in the early 14th century and lost in 1382) (try https://en.wikipedia.org/wiki/Cuneo)
- `/keyframe_review/2`: the 42 Drôme/Ardèche cells of the 1260-1271 shape, which the author's own reading of the Provence page assigns to Alphonse of Poitiers's marquisate; kept 'unverified: page budget' (try https://en.wikipedia.org/wiki/Marquisate_of_Provence)
- `/identity/rulers`: no ruler strip; the Capetian House of Anjou page's ruler table gives Joanna I 20 January 1343 - 12 May 1382 (try https://en.wikipedia.org/wiki/Capetian_House_of_Anjou)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Capetian_House_of_Anjou: confirmed ('invested in August 1246 ... as Count of Anjou and Maine')
- `/ledger/1` https://en.wikipedia.org/wiki/Charles_I_of_Anjou: confirmed (Arles first town to surrender, April 1251)
- `/ledger/2` https://en.wikipedia.org/wiki/Charles_I_of_Anjou: confirmed (Forcalquier returned, November 1256)
- `/ledger/4` https://en.wikipedia.org/wiki/Charles_I_of_Anjou: confirmed (Cuneo sought protection July 1259)
- `/ledger/5` https://en.wikipedia.org/wiki/Charles_I_of_Anjou: confirmed (early 1276, Col de Tende)
- `/ledger/7` https://en.wikipedia.org/wiki/Capetian_House_of_Anjou: confirmed (Joanna I reign ends 12 May 1382; left the county to Louis I of Valois-Anjou)

## dauphine: thin

Area: infobox/body None km2 (year None), Cliopatria 9104.7 km2, ratio None, acknowledged True. No area on the Dauphiné page (checked); the corrections make the shape about 1.6 times Cliopatria's, acknowledged in notes and report.

Findings:
- `/identity/rulers` (applied by reviewer): The ruler strip had a gap 1307-1318 ('no dauphin listed' in the notes), but the page lists John II. Evidence: Dauphin of Viennois page: John II 'Baron of La Tour du Pin, Dauphin of Viennois, ruled 1307–1318'. Fix: insert John II 1307-1318 with that source.
- `/identity/rulers/0/from` (applied by reviewer): Guigues VII started in 1237, before the dossier's start (1260); rulers must lie inside the life. Evidence: identity.start 1260. Fix: from 1260, note 'reigned from 1237'.
- `/ledger/3` (NOT applied, for the author): Dissolve in 1351 (c1, Cliopatria date) while kingdom-of-france gains the Dauphiné in 1349 (c3) and kingdom-of-arles loses it to France in 1349: two-year overlap. Evidence: Humbert II page: relinquished 'his lands and titles on 16 July' 1349; Dauphiné page: sold in 1349, autonomy kept 'only until 1457'. Fix: Either end the dossier on 16 July 1349 (dissolve at confidence 3 from the Humbert II page, matching kingdom-of-france /ledger/38) or keep the Dauphiné as a distinct polity and ask the kingdom-of-france author to move the gain; the orchestrator should pick one. Not blocking: the author flagged it.

Gaps (thin):
- `/ledger/0`: found 1260 at confidence 1 (Cliopatria start); the Dauphins ruled from the 12th century (try https://en.wikipedia.org/wiki/Dauphin_of_Viennois)
- `/ledger/3`: dissolve 1351 at confidence 1; see the fix on the same pointer (try https://en.wikipedia.org/wiki/Dauphin%C3%A9)
- `/keyframe_review/2`: whether the Gapençais was held 1269-1349 (John I's titles omit Gap; the Dauphiné page says Humbert's Gapençais title passed to France in 1349); corrections add the whole Hautes-Alpes (try https://en.wikipedia.org/wiki/Gap,_Hautes-Alpes)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Faucigny: confirmed ('Their daughter, Béatrix, inherited the province in 1268'; married Guigues VII)
- `/ledger/2` https://en.wikipedia.org/wiki/Humbert_II_of_Viennois: confirmed (16 July 1349; 'a distinctive feudal polity, not integrated into the French realm' - the author's quote says 'incorporated')
- `/ledger/0` https://en.wikipedia.org/wiki/Dauphin_of_Viennois: confirmed for the land (Guigues VII 1237-1269, Count of Briançon, Embrun and Gap); the 1260 date is Cliopatria's (c1)
- `/ledger/3` https://en.wikipedia.org/wiki/Dauphin%C3%A9: not on page (page: 1349 sale, 1457 full integration); confidence 1 acknowledged

## principality-of-orange: fix

Area: infobox/body 280 km2 (year None), Cliopatria 140.5 km2, ratio 0.5, acknowledged True. Infobox 280 km2 (no year), body 180 km2; Cliopatria 234 km2 (1260-1271) and 140.5 km2 (1272-1571). Ratio 0.50 at the factor-of-two edge, acknowledged in /keyframe_review/2.

Findings:
- `/ledger/3/region` (applied by reviewer): The 1672-1713 contest used the 1260 shape (234 km2), which reaches outside the 1564 shape (140.5 km2) drawn for 1564-1713; same in /ledger/4/region and /wars/0/zones/0. Evidence: shapes.csv: principality-of-orange_1260 234.2 km2, _1564 140.5 km2; Principality of Orange page: the principality was captured in 1672 and again in August 1682. Fix: cliopatria year 1564 in all three.

Gaps (thin):
- `/keyframe_review/2`: the 1272 shrink from 234 to 140.5 km2 and Cliopatria's 1571 end are unexplained (one page of the 5-page budget unused) (try https://en.wikipedia.org/wiki/Orange,_Vaucluse)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Orange: confirmed (principality status 1163, Frederick I)
- `/ledger/1` https://en.wikipedia.org/wiki/Prince_of_Orange: confirmed ('Baux, in 1173, and of Chalons, in 1393'); the House of Baux page's 1417 is flagged in notes
- `/ledger/2` https://en.wikipedia.org/wiki/Principality_of_Orange: confirmed (William the Silent inherited 1544)
- `/ledger/3` https://en.wikipedia.org/wiki/Principality_of_Orange: confirmed (captured 1672 and August 1682; 1702 enfeoffed to Conti)
- `/ledger/5` https://en.wikipedia.org/wiki/Principality_of_Orange: confirmed (ceded to France, Treaty of Utrecht, 1713); Prince of Orange page names both Frederick I and Frederick William I, as the notes say

## Cross-dossier matrix

- county-of-foix 1278 gain <- Bishop of Urgell | mirror: None None None | **exception**: Andorra paréage; co-principality-of-andorra listed in counterparts_needing_dossiers.
- county-of-foix 1290 gain <- Viscounty of Béarn (was county-of-bearn) | mirror: county-of-bearn 1347 found | **mismatch**: county-of-bearn starts in 1347 and draws Béarn (Pau area) 1347-1555 while Foix holds Béarn from 1290 (Cliopatria 1294 shape): Béarn double-drawn 1347-1555. Flagged by the author; orchestrator must reconcile county-of-foix, county-of-bearn and house-of-bourbon. Counterpart changed by reviewer.
- county-of-foix 1290 gain <- Nébouzan (father-in-law's lordship) | mirror: None None None | **exception**: inheritance; no polity dossier expected.
- county-of-foix 1379 gain <- County of Comminges | mirror: None None None | **exception**: county-of-comminges listed in counterparts_needing_dossiers.
- county-of-foix 1379 gain <- Bigorre (the communities of Bigorre) | mirror: county-of-bearn 1379 gain | **mismatch**: county-of-bearn /ledger/1 records the same Bigorre gain (and the 1390 loss and 1407 gain): both dossiers draw Bigorre 1379-1390 and from 1407.
- county-of-foix 1390 loss <- kingdom-of-france | mirror: kingdom-of-france None None | **missing**: kingdom-of-france has no 1390 gain of Bigorre.
- county-of-foix 1407 gain <- county-of-armagnac | mirror: county-of-armagnac 1407 loss | **matched**: Armagnac /ledger/11 at confidence 1.
- county-of-foix 1447 gain <- Viscounty of Narbonne | mirror: None None None | **exception**: viscounty-of-narbonne listed in counterparts_needing_dossiers.
- county-of-foix 1479 gain <- kingdom-of-navarre | mirror: kingdom-of-navarre 1479 rename | **mismatch**: Navarre records a dynastic rename and keeps Navarre 1463-1511: Navarra (33 cells) double-drawn 1479/1482-1511. Unflagged by the author. Orchestrator: decide whether Foix or kingdom-of-navarre draws Navarre during the personal union (kingdom-of-france /ledger/100 gains Lower Navarre from kingdom-of-navarre in 1620).
- county-of-foix 1484 gain <- county-of-perigord | mirror: county-of-perigord 1481 dissolve | **mismatch**: 3 years apart; House of Albret page: Albret inherited Périgord in 1470, joined to Foix by the 1484 marriage. Counterpart should be the Lordship of Albret.
- county-of-foix 1484 gain <- Lordship of Albret | mirror: None None None | **exception**: lordship-of-albret listed in counterparts_needing_dossiers.
- county-of-foix 1507 loss <- kingdom-of-france | mirror: kingdom-of-france None None | **missing**: kingdom-of-france has no 1507 gain of Narbonne.
- county-of-foix 1512 loss <- crown-of-castile | mirror: kingdom-of-navarre 1512 loss | **mismatch**: crown-of-castile not written (eu-12); kingdom-of-navarre /ledger/18 records the same 1512 loss of Upper Navarre to Castile: the loss is counted twice.
- county-of-foix 1530 gain <- kingdom-of-spain | mirror: kingdom-of-navarre 1527 gain | **mismatch**: kingdom-of-spain not written (eu-12). kingdom-of-navarre regains Lower Navarre from crown-of-castile in 1527 (after a 1525 loss); Foix gains it in 1530 (Henry II page). Both dossiers hold Lower Navarre to 1555.
- county-of-foix 1555 dissolve <- house-of-bourbon | mirror: house-of-bourbon 1555 gain | **matched**: house-of-bourbon /ledger/14.
- county-of-artois 1237 found <- kingdom-of-france | mirror: kingdom-of-france 1237 loss | **matched**: kingdom-of-france /ledger/22.
- county-of-artois 1332 dissolve <- free-county-of-burgundy | mirror: None None None | **exception**: free-county-of-burgundy (Cliopatria row 1333-1384) not written yet.
- capetian-house-of-anjou 1246 found <- kingdom-of-france | mirror: kingdom-of-france 1250 loss | **mismatch**: 4 years apart: kingdom-of-france /ledger/25 dates the loss of Anjou, Maine (and Touraine) to 1250 at confidence 1 from the shape; the dynasty page gives August 1246. France's side should move.
- capetian-house-of-anjou 1251 gain <- County of Provence | mirror: kingdom-of-arles 1246 loss | **exception**: kingdom-of-arles loses Provence in 1246 to county-of-provence (no dossier). The author lists county-of-provence for 1246-1487, which would double-draw Provence with this dossier and house-of-valois-anjou; it should end at 1246 (pre-Angevin county).
- capetian-house-of-anjou 1256 gain <- Dowager countess of Provence | mirror: None None None | **exception**: a person's claim; no dossier.
- capetian-house-of-anjou 1257 gain <- Marseille (the viscounty and commune) | mirror: None None None | **exception**: commune; no dossier.
- capetian-house-of-anjou 1259 gain <- Communes of Piedmont | mirror: None None None | **exception**: communes; no dossier.
- capetian-house-of-anjou 1276 loss <- Ghibelline League | mirror: None None None | **exception**: league; no dossier.
- capetian-house-of-anjou 1290 loss <- county-of-anjou | mirror: county-of-anjou 1290 gain | **matched**: county-of-anjou /ledger/12. But kingdom-of-france /ledger/32 gains Anjou and Maine 'from capetian-house-of-anjou' in 1322: wrong counterpart on France's side (should be county-of-anjou).
- capetian-house-of-anjou 1382 dissolve <- house-of-valois-anjou | mirror: house-of-valois-anjou 1382 gain | **matched**: house-of-valois-anjou /ledger/3.
- dauphine 1268 gain <- county-of-savoy | mirror: None None None | **exception**: county-of-savoy not written (eu-13 not run).
- dauphine 1351 dissolve <- kingdom-of-france | mirror: kingdom-of-france 1349 gain | **mismatch**: 2 years apart; kingdom-of-france /ledger/38 (c3) and kingdom-of-arles /ledger/7 use 1349.
- principality-of-orange 1713 dissolve <- kingdom-of-france | mirror: kingdom-of-france 1713 gain | **matched**: kingdom-of-france /ledger/159.

## Problems

- Navarre is double-drawn: county-of-foix (Cliopatria's Foix-Navarre-Albret composite) holds Upper Navarre 1479/1482-1511 and Lower Navarre 1530-1555 while kingdom-of-navarre (eu-12) holds Navarre 1463-1511 and Lower Navarre 1512-1620; both record the 1512 loss to Castile. The orchestrator must assign Navarre during the Foix-Albret personal union to one dossier.
- Béarn and Bigorre are double-drawn by county-of-foix (from 1290/1294) and county-of-bearn (1347-1555, with the same 1379, 1390 and 1407 Bigorre events); flagged by the author; needs one decision across county-of-foix, county-of-bearn and house-of-bourbon.
- kingdom-of-france (eu-10) lacks mirrors for Foix's 1390 Bigorre loss and 1507 Narbonne loss, dates the Anjou appanage to 1250 (c1) instead of 1246, and names capetian-house-of-anjou instead of county-of-anjou for its 1322 gain of Anjou and Maine.
- kingdom-of-navarre.json was malformed JSON on first read (another agent writing it at about 11:09); re-read later and valid. It uses place 'Saint-Jean-Pied-de-Port', which the gazetteer cannot resolve.
- WebFetch answers through a summariser; spot-check quotes are as the tool returned them.

## Gazetteer names needed

- Nébouzan (region, county-of-foix)
- Faucigny (region, dauphine)
- Lower Navarre (region, county-of-foix)
- Orange (France) (place, principality-of-orange)
- Saint-Jean-Pied-de-Port (place, kingdom-of-navarre)

## Counterparts needing dossiers

- County of Comminges: county-of-comminges [1375, 1379]
- County of Bigorre: county-of-bigorre [1194, 1607]
- Viscounty of Narbonne: viscounty-of-narbonne [1447, 1507]
- Lordship of Albret: lordship-of-albret [1358, 1550]
- County of Provence (pre-Angevin, to 1246; the author's 1246-1487 would overlap capetian-house-of-anjou and house-of-valois-anjou): county-of-provence [1112, 1246]
- Viscounty of Béarn before 1290 (or extend county-of-bearn back): viscounty-of-bearn [1000, 1290]
- Barony of Faucigny: barony-of-faucigny [1253, 1355]
- Co-principality of Andorra: co-principality-of-andorra [1278, 1815]
