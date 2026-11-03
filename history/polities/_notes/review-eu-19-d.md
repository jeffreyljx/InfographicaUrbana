# Review of batch eu-19-d (2026-10-31)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (small verified fixes applied in place). Validator: 0 errors on all three (kingdom-of-georgia 4 warnings for counterparts without dossiers; kingdom-of-kartli-kakheti 34 'no verdict' warnings expected for a split row).

## kingdom-of-vaspurakan: fix

Area: infobox 40870 km2, Cliopatria 41512.6 km2. Kingdom page infobox has no area; the Vaspurakan region page gives 'Vaspurakan's territory was 40,870 km2 ... divided into 35 cantons' (no year), compared with the 911 shape.

Findings:
- `/identity/predecessors` (applied by reviewer): The predecessor note says 'both slugs are given as counterparts' (abbasid-caliphate and bagratid-armenia) but only abbasid-caliphate was listed, so the bagratid-armenia 908 loss to this kingdom had no mirror in identity. Evidence: shapes.csv: bagratid-armenia_886/892/898 (886-910) span 41.6-47.1E, 37.6N and cover the Van basin; bagratid-armenia /ledger/7 is '908 loss kingdom-of-vaspurakan'; Kingdom of Vaspurakan page: 'Gagik I Artsruni was recognized as king by the Sajid ruler Yusuf' and allied with him to attack the Bagratuni kingdom. Fix: Added a second predecessor {slug: bagratid-armenia, land: Cliopatria Kingdom of Vaspurakan 911}; re-validated, 0 errors.

Thin (for a gap-filler):
- `/keyframe_review/1`: The Artsruni hold on parts of Ayrarat, Taron and Korchayk 'temporarily in the 910s' (page has no year) is neither a ledger pair nor a keyframe; thin by page budget (5 of 5 used). Try: https://en.wikipedia.org/wiki/Gagik_I_of_Vaspurakan
- `/keyframe_review/5`: The Antzevatsik (Andzevatsik) cadet lordship from 991 and the -1.6% shape change at 990 are unexplained; page silent. Try: https://en.wikipedia.org/wiki/Artsruni_dynasty

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Vaspurakan: confirmed
- `/ledger/1` https://en.wikipedia.org/wiki/Basil_II: confirmed
- `/keyframe_review/1/note` https://en.wikipedia.org/wiki/Vaspurakan: confirmed

## kingdom-of-georgia: fail

Area: infobox None km2, Cliopatria 197401.8 km2. Kingdom of Georgia infobox gives no area (confirmed: 'Area: not on page'); author says so in each keyframe. Factor-of-2.5 change 1216->1227 between consecutive keyframes is the unexplained move in /keyframe_review/18.

Findings:
- `/ledger/38` (applied by reviewer): The split of western Georgia (counterpart kingdom-of-imereti) was dated 1247, the year Güyük made David VII and David VI co-kings of one kingdom; the page dates the separation to 1259-1260. Evidence: Mongol invasions of Georgia page: 'In 1259–1260, Georgian nobles, led by David Narin, rose against the Mongols' and 'succeeded in separating Imereti (western Georgia) from the Mongol-controlled eastern Georgia'; the 1247 sentence is about co-kings 'in eastern and western parts of the kingdom'. The dossier's own war 'Georgian rebellion against the Ilkhanate' is 1259-1260. Fix: Year changed 1247 -> 1259 and note rewritten with the page's words (confidence 2 kept); ledger order unchanged; re-validated, 0 errors.
- `/keyframe_review/20` (NOT applied, for the author): The new keyframe kingdom-of-georgia_1241 (1241-1329) draws the 1236 outline, Imereti and Samtskhe included, for the whole span, contradicting the dossier's own split of Imereti (/ledger/38, 1259) and loss of Samtskhe (/ledger/39, 1266), which are not undone until /ledger/41 (1330) and /ledger/43 (1334); and no keyframe covers 1330-1332 (1241 keyframe ends 1329, the 1333 shape starts 1333). Evidence: Keyframe text: 'the 1236 outline is reused (Samtskhe's virtual independence from 1266 not subtracted)'; Mongol invasions page dates both the Imereti separation (1259-1260) and Samtskhe's 'virtual independence from the Georgian crown' under Abaqa (1266). Year coverage computed from keyframe_review: 1330, 1331, 1332 uncovered. Fix: Replace with new keyframes: 1241-1258 = Cliopatria 1236 outline; 1259-1265 = {minus: [1236 outline, {region: Imereti}]}; 1266-1329 = {minus: [1236 outline, {region: Imereti}, {region: Samtskhe}]}; 1330-1333 = {minus: [{cliopatria: Kingdom of Georgia, year: 1333}, {region: Samtskhe}]} (Samtskhe back in 1334), so that the 1333 shape stands from 1334.
- `/keyframe_review/18` (NOT applied, for the author): The 1227 correction (Georgia proper plus Ani and Kars, about 75 k km2 against 191 k km2 in the 1216 shape) removes about 105 k km2 of Zakarid Armenia and the Erzurum-side districts with no ledger event except the 40-km Dvin loss (/ledger/32), and it contradicts the keyframe's own evidence; the notes and gaps do not flag it (they list 1210, 1344, 1375, 1385 only). Evidence: shapes.csv kingdom-of-georgia_1216 = 191,182.6 km2, _1227 = 61,603.9 km2. The note quotes Zakarid Armenia 'Under Georgian overlordship since 1199-1200', 'Kars and Ani did not surrender', and the Mongols attacking 'Georgia and its vassal Armenian princedoms' in 1236, i.e. the Zakarid lands other than Dvin were still in the Georgian orbit until 1236-1239. Fix: Either keep the Zakarid lands to 1236-1238 ({minus: [{cliopatria: Kingdom of Georgia, year: 1216}, {place: Dvin circle}]} as the 1227 correction, and widen /ledger/36 (1239, mongol-empire) or add a 1236 loss to cover the Armenian princedoms, Mongol invasions page), or add a dated 1225-1226 loss of the Armenian lands to khwarezmid-empire from a page that says so; in either case write the choice in notes and gaps.
- `/ledger/54` (NOT applied, for the author): Split of Kakheti dated 1463 (confidence 2) although the counterpart dossier and its page found the Kingdom of Kakheti in 1466; with keyframe 1463 drawing only the Kartli rump, Kakheti belongs to no state on the map in 1463-1465. Evidence: kingdom-of-kakheti /ledger/0 quotes its page: 'The kingdom emerged in 1466 from the division of Georgia, after George VIII was captured in 1465'; this event's own note says the Kartli page 'does not date the Kakheti kingdom'. kingdom-of-kakheti's first keyframe is kingdom-of-kakheti_1466 (1466-1467). Fix: Move the split to 1466 (or 1465 with a page) and draw 1463-1465 as {union: [{cliopatria: Kingdom of Georgia, year: 1468}, {region: Kakheti}]} (new keyframe 1463-1465; the 1468 outline alone from 1466).
- `/ledger/17-19` (NOT applied, for the author): The 1130 settlement takes eastern Shirvan and Ani out of the outline (keyframe kingdom-of-georgia_1130, 197 k -> 148 k km2) with only vassal_start events; there is no loss event for the land gained in 1124 (/ledger/15, /ledger/16), and shirvan records a 1130 gain from this kingdom, shaddadids a 1125 gain. Evidence: Demetrius I page (opened): 'Manuchihr was appointed as the emir of eastern Shirvan and recognized Georgia's vassalage'; 'In 1130, the ruler of the Shah-Armens launched an attempt to oust Georgians' ... 'Demetrius had to come to terms and give up Ani to the Shaddadids on terms of vassalage'; 'In 1125 ... Manuchihr ... regained control of western Shirvan'. Schema: vassal_start names the vassal's land, it does not remove own land. Fix: Add '1130 loss shirvan' (Shirvan east of the Tetritsqali) and '1130 loss shaddadids' (Ani, 40 km) before the two vassal_start events, confidence 3, source Demetrius_I_of_Georgia.
- `/ledger/50` (NOT applied, for the author): The 1406 gain of Ganja and Nakhchivan is never lost and leaves no trace in the keyframes (the 1402 keyframe runs to 1414 without them; the 1415/1422 shapes stop at 39.7 N, north of Nakhchivan). Evidence: Timur's invasions of Georgia page: 'He conquered Nakhchivan and Ganja'; 'George succeeded in expanding Georgia's borders temporarily to their former extent'; when they were lost is not on the page. Fix: Add a confidence-1 loss of Nakhchivan and Ganja (e.g. 1410, counterpart qara-qoyunlu, whose dossier has 'Armenia came under Qara Qoyunlu control' in 1410) and a new keyframe 1406-1409 = {union: [1402 keyframe, Ganja circle, Nakhchivan]}, or record the gain only in the note.
- `/ledger/5 and /keyframe_review/2-4` (NOT applied, for the author): Javakheti, ceded in 1023, stays inside the 1010, 1046 and 1072 outlines and no event ever regains it; the note's reason (the gazetteer cannot split Javakheti from Samtskhe) does not hold, since the event itself uses a drawable 40-km circle. Evidence: /ledger/5 region {lon 43.49, lat 41.4, km 40}; keyframe_review/2 note: 'Javakheti lost in the treaty after 1022-23 is not removed'. Basil II page: 'George agreed to a treaty that handed over Tao, Phasiane, Kola, Artaan and Javakheti'. Fix: Subtract the same circle from the corrections for 1023 onward until a dated return (new keyframe 1023-1045 or a note in each), and add the gain that brings Javakheti back (page needed: George II or Bagrat IV).
- `/ledger (1357-1358)` (NOT applied, for the author): Missing occupation_start / occupation_end jalayirid-sultanate for Tiflis; the owner records the occupier's event with roles reversed (schema). Evidence: jalayirid-sultanate /ledger/1-2: 'The Jalayirids then occupied Tiflis in 1357-1358' (confidence 2), counterpart kingdom-of-georgia. Fix: Add 1357 occupation_start and 1358 occupation_end, counterpart jalayirid-sultanate, region {place: Tbilisi, km: 35}, confidence 2, citing the Jalayirid page.
- `/ledger/38, /ledger/41, /ledger/46-47, /ledger/39, /ledger/43, /ledger/51, /ledger/55` (NOT applied, for the author): Counterparts outside their dossiers' lives and not reported: kingdom-of-imereti (dossier 1463-1810) is used for 1259, 1330 and 1387-1389; samtskhe-saatabago (Cliopatria 1468..1506, no dossier yet) for 1266, 1334, 1414, 1463; neither is in the report's counterparts_needing_dossiers. Evidence: kingdom-of-imereti identity.start 1463; its first keyframe kingdom-of-imereti_1463. Fix: List both in counterparts_needing_dossiers (the first western Georgian kingdom 1259-1330 and the Samtskhe principality from 1266) and say in notes which slug carries them.

Thin (for a gap-filler):
- `/keyframe_review/16`: 1210 shape +31 k km2 into Turkey left as drawn, unexplained (page budget 14 of 14 used). Try: https://en.wikipedia.org/wiki/Zakarid_Armenia
- `/keyframe_review/23`: 1375 shape -12 k km2 on the Erzurum side, unexplained. Try: https://en.wikipedia.org/wiki/Bagrat_V_of_Georgia
- `/keyframe_review/27`: The 1415 outline's Kars-Ardahan-Artvin-Erzurum districts are explained by no event (only Samtskhe 1414 and the 1406 gain); 'unverified: page budget'. Try: https://en.wikipedia.org/wiki/Samtskhe-Saatabago
- `/ledger/7`: 1099 recovery of Imereti and Kartli at confidence 1 (only the end of tribute is dated). Try: https://en.wikipedia.org/wiki/Georgian–Seljuk_wars
- `/ledger/24`: 1175 loss of Ani to the Shaddadids at confidence 1; the shaddadids dossier has no 1174 loss or 1175 gain either. Try: https://en.wikipedia.org/wiki/Ani
- `/ledger/25, /ledger/31`: 1190 and 1225 ends of the Shirvan vassalage at confidence 1. Try: https://en.wikipedia.org/wiki/Shirvanshah
- `/ledger/35`: 1236 move of the court to Kutaisi at confidence 1. Try: https://en.wikipedia.org/wiki/Rusudan_of_Georgia
- `/ledger/42`: 1330 gain of Klarjeti and the Armenian lands at confidence 1, against the ilkhanate's 1333 loss. Try: https://en.wikipedia.org/wiki/George_V_of_Georgia
- `/ledger/48`: 1395 loss to Timur at confidence 1 (what Georgia lost is not on the page). Try: https://en.wikipedia.org/wiki/Timur's_invasions_of_Georgia
- `/ledger/56`: 1463 loss of the southern marches at confidence 1, taker unnamed. Try: https://en.wikipedia.org/wiki/Battle_of_Chikhori
- `/identity/rulers`: No ruler strip. Try: https://en.wikipedia.org/wiki/List_of_monarchs_of_Georgia

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Georgia: confirmed
- `/ledger/15` https://en.wikipedia.org/wiki/David_IV_of_Georgia: confirmed
- `/ledger/18` https://en.wikipedia.org/wiki/Demetrius_I_of_Georgia: confirmed
- `/ledger/19` https://en.wikipedia.org/wiki/Demetrius_I_of_Georgia: confirmed
- `/ledger/29` https://en.wikipedia.org/wiki/Tamar_of_Georgia: confirmed
- `/ledger/36` https://en.wikipedia.org/wiki/Mongol_invasions_of_Georgia: confirmed
- `/ledger/38` https://en.wikipedia.org/wiki/Mongol_invasions_of_Georgia: mis-dated
- `/ledger/41` https://en.wikipedia.org/wiki/Mongol_invasions_of_Georgia: confirmed
- `/ledger/50` https://en.wikipedia.org/wiki/Timur's_invasions_of_Georgia: confirmed
- `/ledger/52` https://en.wikipedia.org/wiki/Alexander_I_of_Georgia: confirmed
- `/ledger/6, 8, 9, 10, 11, 14, 16` https://en.wikipedia.org/wiki/David_IV_of_Georgia: confirmed
- `/ledger/21, 39, 45, 49, 51` Kingdom_of_Georgia / Mongol_invasions / Timur's_invasions / Alexander_I pages: confirmed

## kingdom-of-kartli-kakheti: fix

Area: infobox None km2, Cliopatria 55276.0 km2. No area on the page (map caption only); the 1763 shape (55.3 k km2) equals Cliopatria's 1762 Kartli (31.5 k) plus Kakheti (23.4 k), as the author notes.

Findings:
- `/keyframe_review/1/note and /certainty/0/note` (applied by reviewer): The notes said the kingdom's page names 'subordinate khanates' of Kartli-Kakheti (Erivan, Ganja, Karabakh) that are 'tributary, not drawn'; on the page the 'subordinate khans of Erivan and Ganja' are Agha Mohammad Khan's. Evidence: Kingdom of Kartli-Kakheti page: 'after a turn of events by which he gathered more support from his subordinate khans of Erivan and Ganja, he sent Heraclius a last ultimatum'; the page names no khanate tributary to Heraclius II (Karabakh appears only as the khanate Agha Mohammad had just taken). Fix: Reworded both notes to say no page opened names a khanate tributary to the kingdom and that the quoted khans were Agha Mohammad Khan's; re-validated, 0 errors.

Thin (for a gap-filler):
- `/certainty/0`: No page gives the kingdom's frontier or its tributary khanates (Ganja, Erivan) of the 1750s-1780s; the outline rests on Cliopatria only. Try: https://en.wikipedia.org/wiki/Heraclius_II_of_Georgia

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Kartli-Kakheti: confirmed
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Kartli-Kakheti: confirmed
- `/ledger/2` https://en.wikipedia.org/wiki/Battle_of_Krtsanisi: confirmed
- `/ledger/4` https://en.wikipedia.org/wiki/Kingdom_of_Kartli-Kakheti: confirmed

## Cross-dossier matrix

- kingdom-of-vaspurakan 908 found (abbasid-caliphate) <-> bagratid-armenia 908 loss: **matched**. bagratid-armenia records the 908 loss to Vaspurakan; reviewer added bagratid-armenia to Vaspurakan predecessors. abbasid-caliphate has no Vaspurakan event (its shapes do not hold Van).
- kingdom-of-vaspurakan 1021 dissolve (byzantine-empire) <-> byzantine-empire 1021 gain: **matched**. Both 1021 (Vaspurakan December).
- bagratid-armenia 902 loss (kingdom-of-vaspurakan) <-> kingdom-of-vaspurakan None None: **mismatch**. Nakhchavan to Ashot Artsruni in 902 and back in 904 (bagratid-armenia /ledger/4, /ledger/6) name kingdom-of-vaspurakan, which starts in 908; the Artsruni principality before 908 has no dossier. Route to eu-19 (bagratid-armenia owner): counterpart should be the Artsruni principality or the note should say so.
- sajid-dynasty 909 vassal_start (kingdom-of-vaspurakan) <-> none: **exception**. Suzerain records vassalage (schema); Vaspurakan needs no mirror.
- kingdom-of-the-iberians 1008 dissolve (kingdom-of-georgia) <-> kingdom-of-georgia 1008 found: **matched**. 
- kingdom-of-georgia 1010 gain (kingdom-of-kakheti-hereti) <-> none: **exception**. No dossier; listed in counterparts_needing_dossiers (eu-19-x).
- kingdom-of-georgia 1014 loss (kingdom-of-kakheti-hereti) <-> none: **exception**. As above.
- byzantine-empire 1015 loss (kingdom-of-georgia) <-> kingdom-of-georgia 1015 contest_start: **mismatch**. Byzantium records Tao lost to Georgia 1015; Georgia records only a contest over Erzurum/Artvin/Ardahan 1015-1023 and no gain. Either Georgia adds a 1015 gain of Tao (and 1022/1023 loss of it) or Byzantium turns its loss into a contest. Route eu-05 / eu-19.
- kingdom-of-georgia 1023 loss (byzantine-empire) <-> byzantine-empire 1022 gain: **matched**. Within one year; Byzantium gains Tao, Phasiane, Kola, Artaan and Javakheti, Georgia records only Javakheti (the rest was outside its outline).
- kingdom-of-georgia 1080 loss (great-seljuk-empire) <-> great-seljuk-empire 1079 vassal_start: **mismatch**. Seljuk dossier makes all Georgia a vassal 1079-1121 (vassal_end 1121, confidence 1) with no 1080 gain; Georgia records a 1080 loss of Imereti and Kartli and a 1099 gain. Route me-09.
- kingdom-of-georgia 1099 gain (great-seljuk-empire) <-> great-seljuk-empire 1121 vassal_end: **mismatch**. 22 years apart; no Seljuk loss in 1099.
- kingdom-of-georgia 1104 gain (kingdom-of-kakheti-hereti) <-> none: **exception**. No dossier (eu-19-x).
- kingdom-of-georgia 1115 gain (great-seljuk-empire) <-> none: **missing**. Rustavi: no Seljuk loss. Route me-09.
- kingdom-of-georgia 1118 gain (kingdom-of-tashir-dzoraget) <-> none: **exception**. No dossier; listed (validator warns).
- kingdom-of-georgia 1122 gain (great-seljuk-empire) <-> none: **missing**. Tbilisi: no Seljuk loss; the author lists emirate-of-tbilisi (1008-1122) as needing a dossier but names great-seljuk-empire as the 1122 counterpart. Choose one.
- kingdom-of-georgia 1124 gain (great-seljuk-empire) <-> none: **missing**. Dmanisi (March 1124): no Seljuk loss. Route me-09.
- kingdom-of-georgia 1124 gain (shaddadids) <-> shaddadids 1124 loss: **matched**. Ani.
- kingdom-of-georgia 1124 gain (shirvan) <-> shirvan 1124 loss: **matched**. September 1124.
- shirvan 1130 gain (kingdom-of-georgia) <-> none: **missing**. Georgia has only vassal_start shirvan in 1130, no loss of eastern Shirvan (fix in kingdom-of-georgia /ledger/17-19). Also shirvan ends its contest in 1124-09, Georgia in 1130.
- shaddadids 1125 gain (kingdom-of-georgia) <-> kingdom-of-georgia 1130 vassal_start: **mismatch**. Ani back to the Shaddadids: 1125 in shaddadids, 1130 (vassal terms, Demetrius page) in Georgia, and Georgia has no loss event.
- kingdom-of-georgia 1161 gain (shaddadids) <-> shaddadids 1161 loss: **matched**. 
- kingdom-of-georgia 1164 loss (shaddadids) <-> shaddadids 1164 gain: **matched**. 
- kingdom-of-georgia 1174 gain (shaddadids) <-> none: **missing**. shaddadids /ledger/11 says Shahanshah ruled Ani until 1174 but records no 1174 loss.
- kingdom-of-georgia 1175 loss (shaddadids) <-> none: **missing**. Confidence 1 bridging; no shaddadids gain.
- kingdom-of-georgia 1199 gain (shaddadids) <-> shaddadids 1199 loss: **matched**. 
- eldiguzids 1195 loss (kingdom-of-georgia) <-> none: **mismatch**. eldiguzids records a 1195 loss to Georgia (Shamkor/Ganja) and 1196 regain; Georgia says Shamkor "moved no border" and the capital went to "a Georgian protege". Route me-09: counterpart should be the protege or a vassal event.
- kingdom-of-georgia 1203 gain (Dvin's Muslim holders (the page does not name them)) <-> none: **exception**. Unnamed holder; no slug.
- kingdom-of-georgia 1206 gain (saltukids) <-> saltukids 1202 loss: **mismatch**. saltukids dossier ends 1202 (Rum ends the dynasty); Tamar page calls the emir of Kars a "vassal of the Saltukids in Erzurum". Either saltukids extends past 1202 or the counterpart becomes sultanate-of-rum (Erzurum under Tughrilshah). Route me-09.
- kingdom-of-georgia 1226 loss (khwarezmid-empire) <-> none: **missing**. Dvin: no khwarezmid gain. Route me-09.
- kingdom-of-georgia 1239 loss (mongol-empire) <-> none: **missing**. Ani and Kars: mongol-empire has no 1239 gain. Route ia-02.
- mongol-empire 1243 vassal_start (kingdom-of-georgia) <-> none: **exception**. Suzerain records vassalage.
- kingdom-of-georgia 1259 split (kingdom-of-imereti) <-> kingdom-of-imereti 1463 found: **mismatch**. Year moved from 1247 by the reviewer. kingdom-of-imereti starts in 1463, so the first western kingdom (1259-1330) has no dossier.
- kingdom-of-georgia 1266 loss (samtskhe-saatabago) <-> none: **exception**. No dossier yet (eu-19, not run); it must start in 1266, not 1468.
- kingdom-of-georgia 1330 merge (kingdom-of-imereti) <-> none: **mismatch**. Outside kingdom-of-imereti life (1463-1810).
- kingdom-of-georgia 1330 gain (ilkhanate) <-> ilkhanate 1333 loss: **mismatch**. 3 years apart; the ilkhanate holds Georgia as its own land to 1333 while kingdom-of-georgia_1241 draws Georgia as Georgian 1241-1329: double claim. Route ia-02 / orchestrator.
- kingdom-of-georgia 1334 gain (samtskhe-saatabago) <-> none: **exception**. No dossier yet.
- jalayirid-sultanate 1357 occupation_start (kingdom-of-georgia) <-> none: **missing**. Georgia lacks the owner-side occupation events (fix listed).
- kingdom-of-georgia 1395 loss (timurid-empire) <-> timurid-empire 1395 gain: **matched**. Timurid counterpart is "unknown (page silent)".
- timurid-empire 1403 vassal_start (kingdom-of-georgia) <-> none: **exception**. Suzerain records.
- kingdom-of-georgia 1406 gain (timurid-empire) <-> timurid-empire 1405 loss: **matched**. Ganja and Nakhchivan; never lost again in Georgia (fix listed).
- kingdom-of-georgia 1414 gain (samtskhe-saatabago) <-> none: **exception**. No dossier yet.
- kingdom-of-georgia 1431 gain (qara-qoyunlu) <-> none: **missing**. Lori: no qara-qoyunlu loss; no event records Lori leaving Georgia either. Route me-09.
- kingdom-of-georgia 1463 split (kingdom-of-imereti) <-> kingdom-of-imereti 1463 found: **matched**. 
- kingdom-of-georgia 1463 split (kingdom-of-kakheti) <-> kingdom-of-kakheti 1466 found: **mismatch**. 3 years apart; Kakheti unowned 1463-1465 (fix listed).
- kingdom-of-georgia 1463 loss (samtskhe-saatabago) <-> none: **exception**. No dossier yet.
- kingdom-of-georgia 1463 loss (qara-qoyunlu) <-> none: **missing**. Confidence 1, no qara-qoyunlu gain.
- kingdom-of-georgia 1478 dissolve (kingdom-of-kartli) <-> kingdom-of-kartli 1478 found: **matched**. 
- empire-of-trebizond 1230 loss (kingdom-of-georgia) <-> none: **missing**. Confidence 1 in Trebizond; nothing in Georgia (keyframe note: Trebizond an ally, not a dependency). Its 1282-1283 occupation by "King David" is David VI Narin of the western kingdom, not this state. Route eu-05.
- afsharid-iran 1744 vassal_start (kingdom-of-georgia) <-> none: **mismatch**. Teimuraz II's Kartli in 1744 is kingdom-of-kartli; kingdom-of-georgia ends 1478. Route me-10.
- kingdom-of-kartli-kakheti 1762 found (kingdom-of-kartli) <-> kingdom-of-kartli 1762 dissolve: **matched**. Kartli and Kakheti dossiers now name kingdom-of-kartli-kakheti (the author note saying kingdom-of-georgia is out of date).
- kingdom-of-kartli-kakheti 1762 merge (kingdom-of-kakheti) <-> kingdom-of-kakheti 1762 merge: **matched**. 
- russian-empire 1783 vassal_start (kingdom-of-kartli-kakheti) <-> none: **missing**. Treaty of Georgievsk (24 July 1783) protectorate not in russian-empire. Route eu-17.
- qajar-dynasty 1795 contest_start (kingdom-of-georgia) <-> kingdom-of-kartli-kakheti 1795 contest_start: **mismatch**. qajar-dynasty uses kingdom-of-georgia and ends the contest in 1801-09; Kartli-Kakheti ends it 1795-09. Route me-10.
- kingdom-of-kartli-kakheti 1801 dissolve (russian-empire) <-> russian-empire 1801 gain: **mismatch**. Year matches; russian-empire names counterpart kingdom-of-georgia, should be kingdom-of-kartli-kakheti. Route eu-17.

## Counterparts needing dossiers

- Kingdom of Kakheti-Hereti (kingdom-of-kakheti-hereti, 1010-1105): author list, eu-19-x
- Emirate of Tbilisi (emirate-of-tbilisi, 1008-1122): author list; not yet used as a counterpart (1122 gain names great-seljuk-empire)
- Kingdom of Abkhazia (kingdom-of-abkhazia, 978-1008): author list (predecessor)
- Kingdom of Tashir-Dzoraget (kingdom-of-tashir-dzoraget, 1118-1118): author list; validator warns
- First Kingdom of Imereti (western Georgia under David VI Narin and successors) (kingdom-of-imereti (extend start to 1259) or a new slug, 1259-1330): new: kingdom-of-georgia /ledger/38, /ledger/41 name kingdom-of-imereti, whose dossier starts 1463
- Samtskhe-Saatabago (virtually independent from 1266) (samtskhe-saatabago, 1266-1468): new: Cliopatria row starts 1468; kingdom-of-georgia uses it from 1266 (eu-19, not written yet)

## Problems

- Orchestrator allowed small reviewer fixes, so three dossiers were edited in place (kingdom-of-georgia /ledger/38 year; kingdom-of-vaspurakan /identity/predecessors; kingdom-of-kartli-kakheti two notes); all re-validated with 0 errors and read back.
- The author's notes say kingdom-of-kartli and kingdom-of-kakheti name kingdom-of-georgia as their 1762 successor; both now name kingdom-of-kartli-kakheti (fixed by their owners).
- Other groups still use the slug kingdom-of-georgia for post-1478 states: russian-empire 1801 gain (eu-17), qajar-dynasty 1795-1801 contest (me-10), afsharid-iran 1744-1747 vassalage of Teimuraz II's Kartli (me-10).
- shaddadids, saltukids and eldiguzids dossiers now exist (other groups); the author's report lists them as needing dossiers. saltukids ends 1202, before Georgia's 1206 Kars gain that names it.
- Double claim 1294-1333: ilkhanate holds Georgia as own land until its 1333 loss, while kingdom-of-georgia_1241 (1241-1329) draws Georgia as Georgian; the orchestrator should pick one (Georgia as an Ilkhanid vassal seems to fit the pages).
- All WebFetch pages loaded; the answers come from a summariser, so only quoted sentences were used.
