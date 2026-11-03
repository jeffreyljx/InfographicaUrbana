# Review of batch eu-14-e (Scandinavia and the Baltic, part e)

Reviewer, 2026-10-25. Validator with --resolve on all six: 0 errors, 0 warnings before review. Author's report and notes read first. Neighbour dossiers read (ledger greps): old-kingdom-of-norway, viking-settlements, kalmar-union, teutonic-order, scandinavian-minor-kingdoms, livonian-conference, denmark-norway, grand-duchy-of-finland, kingdom-of-england. Not yet written (exception "group has not run yet"): kingdom-of-denmark, novgorod-republic, tsardom-of-russia, kingdom-of-alba, principality-of-jersika, kingdom-of-norway, swedish-empire, and the other context slugs.

Verdicts: kingdom-of-sweden FAIL; north-sea-empire PASS; denmark-england PASS; norway-denmark FAIL; norse-greenland FIX (applied by reviewer); livonian-brothers-of-the-sword FIX (applied by reviewer).

## kingdom-of-sweden: fail

Spot checks, all confirmed on the page with the year: Noteborg 12 August 1323 (Savilahti, Jaaski, Aeyraepaeae, 18 border points); Scania 1332 (Duke Johan of Holstein, 34,000 marks); Noteborg taken August 1348 and lost February 1349; Scania retaken 1360; Kalmar 17 June 1397; Gustav Vasa 6 June 1523; Estonia June 1561; Plussa 1583; Ingria and Kexholm ceded 1590; Teusina 1595; Second Crusade 1249-1250. Area: infobox 450,295 km2 against the 1905-2024 shapes' 458,353 km2 (1.02), acknowledged. The no-break decision is supported by the infobox itself ("Swedish Empire: 1611-1721" as an era of Sweden).

Blocking:
1. Gotland 1361 is missing. The Magnus IV page the dossier cites: "He went on to conquer Gotland in 1361." / "On 27 July 1361, outside the city of Visby ... It ended in a complete victory for Valdemar." The dossier's own war /wars/3 names it. Gotland has 15 cells in the 1344 shape, 0 in the 1375 shape; the new 1360-1374 keyframe keeps it. Write a loss 1361-7 (Gotland, counterpart kingdom-of-denmark, confidence 3), end keyframe _1360 at 1360, add _1361 (1361-1374) without Gotland, add Gotland to /wars/3 zones.
2. Kalmar Union breaks. kalmar-union (conf 3, its own pages) has Sweden leave and rejoin: loss 1448-6, gain 1457-6, loss 1464-6, gain 1497-10, loss 1501-8, gain 1520-11, contest 1521-1..1523-6, dissolve 1523-6; its keyframes cut Sweden out for 1448-1456, 1464-1496 and 1501, and its last keyframe ends in 1523. The Sweden ledger has only merge 1397 and a confidence-1 split in 1502 (a split means part of this state becomes the counterpart: the wrong direction). Result: Sweden is drawn by nobody in 1448-1456, 1464-1496, 1501 and June 1523-1525. Write the mirrors (counterpart kalmar-union, citing kalmar-union's pages), replace /ledger/20 with a gain 1501-8, add keyframes 1448-1456, 1464-1496, 1501 ({cliopatria Kingdom of Sweden, 1502}) and 1523-1525, end the 1502 shape at 1520.
3. /wars/4 (Gustav Vasa) has empty zones although ground changed hands (kalmar-union contests Sweden 1521-1523); give it zones and the contest pair.

Non-blocking:
4. /ledger/28: a 1905 loss of Norway in a ledger that never gained Norway (the dossier calls 1814-1905 a personal union). Drop it, or keep it only if 1814-1905 is represented; kingdom-of-norway (eu-20) mirrors whatever stays.
5. 1612-1904 has no keyframe and no event; grand-duchy-of-finland's 1809-9 gain from kingdom-of-sweden has no mirror. Orchestrator: merge swedish-empire here or pause this dossier with explicit hand-overs.

Thin (gap-filler):
- Northern Seven Years' War, opened by the reviewer (https://en.wikipedia.org/wiki/Northern_Seven_Years%27_War): "In 1564 the Swedes marched under Claude Collart and re-occupied Jemtland ... as well as Herjedalen and Trondelag, including the city of Trondheim"; "These provinces were later regained by Denmark-Norway following the peace process in 1570"; "peace was finally reached on 13 December 1570 with the Treaty of Stettin". This explains Jamtland in the 1564 shape and the 55 k km2 drop of 1572. Write occupation_start 1564 / occupation_end 1570-12 with denmark-norway (which already has contest 1563..1570-12 with Sweden) and the war.
- 1526 shape +217 k km2 to 70.02N unexplained (page budget); Finnish conquests 1220-1314 at confidence 1; Ingria and Kexholm before 1588; the 980 core, 1003 handover, Blekinge 1360; no ruler strip (List of Swedish monarchs).

Cross-dossier: teutonic-order's 1398 gain of Gotland names kingdom-of-sweden, but Sweden lost Gotland in 1361; that owner should name the 1398 holder from its own page.

## north-sea-empire: pass

Tried: Cnut king of Denmark 1018; "Cnut claimed the crown of Norway in Trondheim in 1028"; "In 1031, Malcolm II of Scotland also submitted to him"; died 12 November 1035 at Shaftesbury; Swein fled Norway in autumn 1035; capital Winchester (infobox). All confirmed. Norway occupation 1028/1035 mirrors old-kingdom-of-norway exactly; England's 1018 merge in kingdom-of-england mirrors the found. The infobox has no area and gives 1013-1042; the dossier's 1018-1035 with denmark-england for 1040-1042 is explained. Alba (kingdom-of-alba, eu-11) not written: exception. Thin: the 1035 end of the Scottish tie (confidence 1).

## denmark-england: pass

Tried: Harthacnut landed at Sandwich 17 June 1040; died 8 June 1042; successors Edward the Confessor (England) and Magnus I (Denmark). Confirmed. Mirrors: kingdom-of-england gain 1042-6 matches; norway-denmark found 1042 matches. Mismatch on England's side: kingdom-of-england has England merged in the North Sea Empire to 1042 with no 1035 or 1040 event, so England 1035-11..1040-6 is drawn by nobody; kingdom-of-england should regain England in 1035-11 (Harold Harefoot) and merge into denmark-england in 1040-6. Thin: unsourced bridging capital.

## norway-denmark: fail

Spot checks confirmed (crowned in Denmark 1042; Wendish invasion and Lyrskov Heath 1043; "by late 1046, Magnus had driven Sweyn out of Denmark"; died 25 October 1047). Blocking: /keyframe_review/0 (1042-1045) draws Denmark as {country Denmark} (50,327 km2) and so leaves out Scania, Halland, Blekinge and southern Schleswig: 0 cells of Skane, Halland and Blekinge, against 56, 26 and 13 in both neighbouring Cliopatria shapes (Denmark-England 1040 and Norway-Denmark 1046). Nobody draws them 1042-1045. Fix: correction = {"cliopatria": "Norway-Denmark", "year": 1046}, same spec for /ledger/0/region. Cross-dossier: old-kingdom-of-norway has no 1042 merge or 1047 split and keeps drawing Norway, so Norway is drawn twice 1042-1047 (orchestrator to pick the side that pauses).

## norse-greenland: fix (applied by the reviewer)

Spot checks confirmed: "established after 986 CE"; "subordinated itself to the Norwegian crown in 1261"; "The Western Settlement was abandoned around 1350"; "After a marriage was recorded in 1408, no written records mention the settlers". Gazetteer confirms the author's shape error: 0 cells of a 70 km disk round Qaqortoq inside the 1072 shape (and 0 in old-kingdom-of-norway's 1272 Greenland). Applied: /ledger/1 rename became vassal_start, counterpart old-kingdom-of-norway (both pages say subordinated / accepted the overlordship), region the corrected colony; a sentence added to notes; re-validated (1 allowed warning: the tie lasts to 1408). Old-kingdom-of-norway still records a gain and draws Greenland 1261-1397: its owner should make it a vassal_start with counterpart norse-greenland. viking-settlements already gives Greenland to this dossier (author's point (b) settled). Thin: founding and end at confidence 1.

## livonian-brothers-of-the-sword: fix (applied by the reviewer)

Spot checks confirmed: founded 1202; southern Estonia "until 1218, when they conquered southern Estonia"; headquarters at Fellin 1224; Talava "in 1224 was finally divided between the Archbishopric and the Order"; "In 1227, the Livonian Brothers of the Sword conquered all Danish territories in northern Estonia"; "In 1230, Kurland was conquered and converted by the order"; incorporated into the Teutonic Order 1237. No infobox area. Applied: /ledger/10 (Saaremaa 1227) confidence 3 to 2, because the page credits "a combined attack" by the Brothers, Riga and the Bishop; /ledger/13, /ledger/14 and /identity/successors/0/land now use the dossier's own corrected 1230-1237 keyframe instead of Cliopatria's uncorrected shape (Semigallia was not the Order's: "partly subdued the Semigallians in 1254", resistance "until 1290"). Re-validated: 0 errors, 0 warnings. Cross-dossier: teutonic-order /ledger/2 (1237 gain) still uses Cliopatria's uncorrected 1237 shape; align it. Thin: 1206 and 1210 at confidence 1.
