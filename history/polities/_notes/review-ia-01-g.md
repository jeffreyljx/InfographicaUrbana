# Review of batch ia-01-g (Eastern Kara-Khanids, Western Karakhanid Khanate, Cuman-Kipchak Confederation, Kara-Khitans)

Reviewed 2026-10-19. Validator: all four dossiers 0 errors, 0 warnings (also with --resolve), before and after the reviewer's three small edits. Pages opened through WebFetch: Kara-Khanid Khanate, Qara Khitai, Malik-Shah I, Yelu Dashi, Qocho, Cumans, Cumania, Kuchlug. No page failed. Every confidence-3 event checked was on its page with its year; no fabricated event was found. The failures are about geometry: cells claimed twice, or cells that move with no event. I found them by counting cells with tools/gazetteer.py.

Neighbour dossiers read: kimek-kipchak-confederation, qocho-kingdom, kara-khanids. The other context polities (great-seljuk-empire, khwarezmid-dynasty/-empire, lohara-dynasty, ghurid-dynasty, mongol-empire, liao-dynasty, halych-volhynia-occupation and the rest) are not written yet. Their mirrors count as the exception for a counterpart whose group has not run.

## eastern-kara-khanids: fail

Area: infobox None (None), Cliopatria 984464 km2, ratio None, acknowledged True. The Kara-Khanid Khanate infobox has no area (checked); the author says so.

Findings:

- **/ledger/6**: The 1134 loss names only Semirechye (1,306 cells), but keyframe_review/6 to /7 removes 1,860 cells: 554 cells (about 140,000 km2; the Tian Shan interior, the Alay and the Pamir edge, bbox 69.7-83.2 E, 35.8-46.8 N) leave the Eastern shape in 1134 with no event, lie in no dossier in 1134-1138 and reach kara-khitans only with its Cliopatria 1139 shape. Evidence: Cell count with gazetteer.resolve: corrected 1126 shape 3,109 cells, keyframe_review/7 1,249, Semirechye takes 1,306 of the 1,860 dropped; kara-khitans_1134 and _1137 corrections hold none of the other 554, and kara-khitans /ledger/7 (1139 gain from nobody) subtracts the whole Eastern 1126 shape, so no event gains them either. Fix: Make the 1134 loss region the whole non-Tarim part: {"minus":[{"union":[{"cliopatria":"Eastern Kara-Khanids","year":1126},{"place":"Kuqa","km":60}]},{"intersect":[{"union":[{"cliopatria":"Eastern Kara-Khanids","year":1126},{"place":"Kuqa","km":60}]},{"region":"Tarim Basin"}]}]} (text: Balasagun, Zhetysu and the Tian Shan), and have kara-khitans add the same cells to its 1134 gain and its 1134 and 1137 corrections; or keep the 554 cells in this dossier until 1139 and lose them then (confidence 1).
- **/ledger (missing events)**: The Qara Khitai overlordship of 1141-1211 has no vassal_start/vassal_end here, though kara-khitans /ledger/8 (1141) and /ledger/22 (1211) record it and keyframe_review/7 calls the rump a vassal. Evidence: Kara-Khanid infobox: 'Qara Khitai vassal (1141-1212)'; the mirror rule wants the vassal's own ledger to carry the pair with the overlord as counterpart. Fix: Add vassal_start 1141 (counterpart kara-khitans, region = keyframe_review/7's region, confidence 3, source Kara-Khanid_Khanate) and vassal_end 1211 (counterpart kara-khitans, same region, confidence 3) before the dissolve. Optionally add the short Seljuk vassalage (Malik-Shah I page: at Uzkand Hasan ibn Suleiman 'agreed to be his vassal and pay taxes'; 1089) as vassal_start 1089 / vassal_end with a bridging year, counterpart great-seljuk-empire.
- **/identity/rulers/0**: Ebu Shuca Sulayman starts in 1042, before the state's 1046 start, and the list leaves 1056-1059 empty before Mahmud. Evidence: Rulers must lie inside the life and be contiguous (reviewer brief 2.2). Fix: Start Sulayman at 1046 (say in note that he reigned from 1042 in the undivided khanate) and close the 1056-1059 gap or say in a note that the page leaves it empty.
- **/ledger/1/note** (applied by the reviewer): The note quoted only half of the page's sentence on Fergana and called the page silent; the page says the West took Fergana under Ibrahim. Evidence: Kara-Khanid Khanate page: 'When the two states were formed, Fergana fell into realm of the Eastern Khanate, but was later captured by Ibrahim and became part of the Western Khanate.' Fix: Appended the quote and the bound (before 1068) to the note; confidence stays 1 because the year is Cliopatria's. keyframe_review/2's note still says 'in tension with the pages' and should be aligned by the author.

Spot checks:

- /ledger/9: confirmed, 'The Eastern Khanate ended in 1211'; the prince 'was killed in Kashgar by the rebels in 1211' (https://en.wikipedia.org/wiki/Kara-Khanid_Khanate)
- /ledger/7: confirmed, 'In 1204, a rebellion of the Eastern Kara-Khanid in Kashgar was suppressed by the Kara-Khitai'; Qara Khitai page: 'put down a rebellion in Khotan and Kashgar' (https://en.wikipedia.org/wiki/Kara-Khanid_Khanate)
- /ledger/5: confirmed, infobox 'Balasagun (942-1130); Kashgar (1130-1211)' (https://en.wikipedia.org/wiki/Kara-Khanid_Khanate)
- /ledger/4: confirmed, 'By 1096, Qocho had lost Aksu, Tumshuk, and Kucha to the Kara-Khanid Khanate' (https://en.wikipedia.org/wiki/Qocho)
- /ledger/6: confirmed, 'In 1134 he conquered the Karakhanid city of Balasaghun'; the land is too narrow (fix 1), the date is right (https://en.wikipedia.org/wiki/Qara_Khitai)

For the gap-filler:

- /ledger/1: the year Ibrahim Tamghach Khan took Fergana from the East (before 1068) (try https://en.wikipedia.org/wiki/Ibrahim_Tamghach_Khan)
- /keyframe_review/7: the extent of the Kashgar rump 1134-1211 (Aksu, Kucha, Khotan) and who held Kashgar after the 1211 killing (try https://en.wikipedia.org/wiki/Kuchlug)

## western-karakhanid-khanate: thin

Area: infobox None (None), Cliopatria 326270 km2, ratio None, acknowledged True. No area in the Kara-Khanid infobox.

Findings:

- **/ledger (missing events)**: Neither overlordship is in the ledger: no vassal_start/vassal_end for the Seljuks (1089-1141) or the Qara Khitai (1141-1210), though kara-khitans /ledger/9 (1141-09) and /ledger/18 (1210) record the second and keyframe_review/4-6 describe the state as a vassal. Evidence: Kara-Khanid infobox: 'Seljuk vassal (1089-1141); Qara Khitai vassal (1141-1212)'; Kara-Khanid page: 'In 1089 ... the Seljuks entered and took control of Samarkand'; 'In 1210, the Khwarezm-Shah took Samarkand after the Qara Khitai retreated'. Fix: Add vassal_start 1089 and vassal_end 1141 (month 9) with counterpart great-seljuk-empire, and vassal_start 1141 (month 9, source Battle_of_Qatwan) and vassal_end 1210 with counterpart kara-khitans, region = the keyframe region of those years, confidence 3 for the infobox years.
- **/ledger/7**: The 1210-1212 Khwarazmian hold on Samarkand is typed as a contest, but the page describes a takeover followed by an alliance, not fighting between the two until the 1212 revolt. Evidence: Kara-Khanid page: 'In 1210, the Khwarezm-Shah took Samarkand after the Qara Khitai retreated'; 'Muhammad then formed an alliance with the Western Karakhanid ruler Uthman ibn Ibrahim'; 'In 1212, the population of Samarkand staged a revolt against the Khwarezmians'. Fix: Retype /ledger/7 and /ledger/8 as vassal_start 1210 / vassal_end 1212 (counterpart khwarezmid-empire, Samarkand), keeping the 1212 dissolve; or keep the contest and say in the note why an allied overlordship is drawn as a fighting zone.
- **/identity/rulers/0**: Ibrahim Tamghach Khan starts in 1040, before the state's 1046 start. Evidence: Rulers must lie inside the life (reviewer brief 2.2). Fix: Start at 1046 with a note on the earlier reign.
- **/ledger/1/note** (applied by the reviewer): The note quoted only half of the page's sentence on Fergana and called the page silent; the page says the West took Fergana under Ibrahim. Evidence: Kara-Khanid page: 'Fergana fell into realm of the Eastern Khanate, but was later captured by Ibrahim and became part of the Western Khanate.' Fix: Appended the quote and the bound (before 1068); confidence stays 1 (the year is Cliopatria's). The notes field's item (2) on Fergana should be aligned by the author.

Spot checks:

- /ledger/3: confirmed, 1087: 'Malik-Shah attacked Samarkand and conquered the city'; 'Ahmed was captured by the Seljuks after the capture of Samarkand'; 1089: Turkistan 'brought under Seljuk rule' (https://en.wikipedia.org/wiki/Malik-Shah_I)
- /ledger/2: confirmed, 1073: 'he headed towards Termez and captured Termez' (https://en.wikipedia.org/wiki/Malik-Shah_I)
- /ledger/5: confirmed, 'In May 1137 he defeated a Western Karakhanid ruler at Khujand'; Qara Khitai page: 'annexed Fergana and Tashkent' (https://en.wikipedia.org/wiki/Yel%C3%BC_Dashi)
- /ledger/6: confirmed, 'In 1207, Muhammad II entered Bukhara' (https://en.wikipedia.org/wiki/Qara_Khitai)
- /ledger/7: confirmed, 1210 date confirmed; the typing is questioned in fixes (https://en.wikipedia.org/wiki/Kara-Khanid_Khanate)
- /ledger/9: confirmed, 'In 1212 ... recaptured Samarkand and executed Uthman'; 'finally extinguished the Western Karakhanid state' (https://en.wikipedia.org/wiki/Kara-Khanid_Khanate)

For the gap-filler:

- /ledger/1: the year of Ibrahim's capture of Fergana (try https://en.wikipedia.org/wiki/Ibrahim_Tamghach_Khan)
- /keyframe_review/0-2: Ghaznavid frontier on the Oxus 1046-1065 and the 1056 Pamir-edge step (unverified: page budget) (try https://en.wikipedia.org/wiki/Ghaznavids)

## cuman-kipchak-confederation: fail

Area: infobox None (None), Cliopatria 315 km2, ratio None, acknowledged True. Cumania infobox has no area; the single 315 km2 Cliopatria shape is marked wrong.

Findings:

- **/keyframe_review/2/correction**: From 1072 the dossier's steppe overlaps the kimek-kipchak-confederation dossier on 447 cells (about 113,000 km2): the region 'Pontic Steppe minus Kimek 1056' is fixed to the Kimek row's 1056 edge, but that row (and the Kimek dossier, its /ledger/5 1072 gain) grows into it in 1072, so two dossiers claim the land 1072-1241. The overlap is not acknowledged. Evidence: gazetteer.resolve: the region holds 1,815 cells; the Kimek-Kipchak Cliopatria shapes of 1072-1235 hold 447 of them (0 in 1056-1071). Fix: Split keyframe_review/2 at 1072 and subtract {"cliopatria":"Kimek-Kipchak confederation","year":1072} from 1072 on, with a 1072 loss to kimek-kipchak-confederation (confidence 1) matching the Kimek dossier's 1072 gain (which would then name this dossier instead of nobody); or ask ia-01-e to drop the 447 cells from the Kimek keyframes. Apply the same region to /ledger/2-4.
- **/notes, /identity/predecessors/0/land/text, /ledger/0/region/text**: The texts say the steppe is 'west of the area the Kimek-Kipchak row already holds (it stops at 38 E)', but 855 of the 1,815 cells lie east of 38.5 E, out to 48.9 E (lower Don, Kalmyk and Kuban steppe). Evidence: Cell centroids of the resolved region: longitude 38.5-48.9 E for 855 cells. Fix: Describe the region as the Pontic-Caspian steppe outside the Kimek row (Dnieper-Danube steppe plus the lower Don, Kuban and Kalmyk steppe), or trim it to 38 E with a polygon or a minus of the Volga and Caspian lowland if only the western steppe is meant.
- **/identity/capitals/0**: The capital is Sarai (45.35 E, 48.68 N), the Golden Horde's later seat, and it lies outside every shape of this dossier. Evidence: None of the 3 cells of Sarai (15 km) is in the region; the author's own note says Sarai is later than the confederation. Reviewer brief 2.9: capitals inside the state's shapes in those years. Fix: Drop the capital (the confederation had no documented seat) or, if one is required, use a label point inside the steppe with a note that it is not a seat.
- **/identity/predecessors/0, /ledger/0**: The predecessor kimek-kipchak-confederation is given land it never held, and the Kimek dossier has no split or successor for this dossier: it continues itself as 'the Cuman-Kipchak confederation' from its 1055 rename (its /ledger/2), so two dossiers carry the same confederation on either side of a seam. Evidence: kimek-kipchak-confederation.json: successors = [mongol-empire] only; /ledger/2 1055 'rename' with the note 'the confederation continues here under its Kipchak-Cuman names'. Cumania infobox: 'Preceded by Kimek-Kipchak confederation; Khazaria'. Fix: Orchestrator decision with ia-01-e: either one dossier for the confederation (both Cliopatria names), or a 1055 split in the Kimek dossier naming cuman-kipchak-confederation; in the meantime give the 1055 found event the land's previous holders (pechenegs, oghuz-turks) in the note.
- **/ledger/1**: The Bugeac is gained from 'nobody', though the Cumans page has the Cuman advance push the Oghuz west and the Pechenegs west of the Dnieper. Evidence: Cumans page: the Cuman entry 'pressed the Oghuz Turks to shift west', which moved the Pechenegs 'west of the Dnieper'; the author lists pechenegs under counterparts_needing_dossiers. Fix: Counterpart pechenegs (confidence stays 2), or keep nobody and say in the note why the Pechenegs had left.

Spot checks:

- /ledger/0: confirmed, 'The Cumans first encountered the Rus' in 1055, when they advanced towards the Rus' Pereyaslavl principality' (https://en.wikipedia.org/wiki/Cumans)
- /ledger/1: confirmed, 'The Cumans first entered the Bugeac (Bessarabia) at some point around 1068-1078' (https://en.wikipedia.org/wiki/Cumans)
- /ledger/2: confirmed, 'A direct attack on Cumania came only in 1238-1239' (https://en.wikipedia.org/wiki/Cumans)
- /ledger/4: confirmed, infobox 'Disestablished: 1241'; Cumans page: 'The final blow came in 1241, when Cuman control over the Pontic steppes ended' (https://en.wikipedia.org/wiki/Cumania)

For the gap-filler:

- /keyframe_review/1-2: any page drawing the Cuman frontier (Dnieper, Danube, Don) with years (try https://en.wikipedia.org/wiki/Pechenegs)
- /wars: Kalka (1223) is only a note in the Mongol war; it could be its own war with empty zones (try https://en.wikipedia.org/wiki/Battle_of_the_Kalka_River)

## kara-khitans: fail

Area: infobox 1000000 (1130), Cliopatria 376585 km2, ratio 2.66, acknowledged True. keyframe_review/1 (marked wrong) acknowledges the 2.7x gap and reads the 1130 figure as the later realm. Infobox 1,500,000 km2 (1210) against Cliopatria 2,059,424 km2 (ratio 1.37) and the corrected 1.10 M km2 by cells (0.73), acknowledged in keyframe_review/10.

Findings:

- **/keyframe_review/6/correction (and /7-/9)**: The 1147-1209 corrections keep as direct Qara Khitai land 972 cells (about 245,000 km2; 60.5-68.5 E, 40.1-46.2 N: the Kyzylkum, the lower Syr Darya and Khwarazm's edge) that Cliopatria's Khwarezmid Dynasty row held in 1146 and drops in 1147; no ledger event gains them and no counterpart is named, and 73 of them (about 18,000 km2) lie inside the Khwarezm region that /ledger/10 draws as a vassal from 1142. Evidence: gazetteer.resolve: Kara-Khitans 1147 minus 1139 = 2,545 cells, of which 1,278 are the Western shape (removed as vassal land), 292 the Kimek row (/ledger/11) and 975 the Khwarezmid Dynasty 1146 shape; the corrected 1147 shape keeps 972 of those, and 73 of the vassal region {region: Khwarezm}. Fix: Either subtract {"cliopatria":"Khwarezmid Dynasty","year":1146} from the 1147-1209 corrections (consistent with drawing Khwarazm as a vassal) or add a 1147 gain from khwarezmid-dynasty (confidence 1, Cliopatria's step) and list the matching loss for me-09; in both cases subtract the Khwarezm region from the direct shape.
- **/ledger/7, /ledger/3, /keyframe_review/3-5**: 554 cells of the Eastern Kara-Khanid shape (about 140,000 km2; Tian Shan, Alay, Pamir edge) enter the direct shape in 1139 with no event: the 1139 gain from nobody subtracts the whole Eastern 1126 shape, and the 1134 gain (/ledger/3) is only Semirechye. Evidence: Same count as eastern-kara-khanids fix 1: the cells are in no dossier in 1134-1138 and in kara-khitans_1139's correction from 1139. Fix: Widen the 1134 gain to the non-Tarim part of the Eastern shape and add those cells to the 1134 and 1137 corrections, in step with the eastern-kara-khanids fix.
- **/keyframe_review/10/correction**: The 1210-1215 correction keeps the Tarim rump (1,122 cells, about 283,000 km2) as direct land from 1210, while eastern-kara-khanids holds it to 1211 and /ledger/22 ends the vassalage in 1211, so two dossiers draw it in 1210-1211. Evidence: Overlap of the two corrected shapes in 1210 and 1211: 1,122 cells. Fix: Subtract the Tarim rump (eastern-kara-khanids keyframe_review/7 region) until 1211: split the 1210 keyframe at 1212.
- **/keyframe_review/5-11/correction**: The corrections subtract Cliopatria's Qocho 1126 shape, but qocho-kingdom's own keyframe for 1139-1369 adds Hami (120 km): 109 cells (about 27,000 km2) are drawn both as direct Qara Khitai land and as Qocho. Evidence: qocho-kingdom.json keyframe_review/6 correction includes {place: Hami, km: 120}; overlap 109-111 cells in 1140-1218. Fix: Subtract {"place":"Hami","km":120} as well, or settle with ia-01-f which side holds Hami (the 1139 gain names Hami at confidence 1).
- **/keyframe_review/2-4**: The Emil base (Tacheng, 120 km) overlaps the kimek-kipchak-confederation shapes in 1130-1138 (58 cells in 1131, 127 in 1134-1138) with no gain from that dossier. Evidence: Overlap of the corrected shapes with the Kimek dossier's Cliopatria 1094 shape. Fix: Add a 1130 gain from kimek-kipchak-confederation (confidence 2, the Emil base) or trim the disk to the Kimek edge.
- **/ledger/1**: The Qocho vassalage starts in 1130 here and in 1128 in qocho-kingdom /ledger/6: two years apart. Evidence: Qocho page: 'In 1128, the Kingdom of Qocho became a vassal of the Qara Khitai' and infobox 'Vassal state of the Western Liao (1132-1209)'; Qara Khitai page: 'Within a year, he had established himself as suzerain of Qocho' after the 1130 move; Yelu Dashi page: 'At about the same time' (c. 1130). Fix: Keep 1130 (both Qara Khitai pages; 1128 precedes the move west) and have ia-01-f move qocho-kingdom's vassal_start to 1130 with the page conflict in its note.
- **/ledger/13**: The 1165 Balkh-Andkhud gain is drawn as direct land, but the page has the Ghurids take Balkh in 1198 'from the vassal of the Qara Khitai'. Evidence: Qara Khitai page: 'In 1198, Muhammad of Ghor ... seized Balkh from the vassal of the Qara Khitai'; 'In 1165, the Qara Khitai participated in Mas'ud Tabghach Khan's invasion of Balkh and Andkhud'. Fix: Make 1165-1198 a vassal_start/vassal_end pair (counterpart the Balkh ruler) and the 1198 event the Ghurid conquest, or keep the gain and quote the 'vassal' sentence in the note.
- **/ledger/14/confidence** (applied by the reviewer): Confidence 3 for Balkh and Andkhud in 1198, but the page names only Balkh for that year. Evidence: Qara Khitai page: 'In 1198, Muhammad of Ghor ... seized Balkh from the vassal of the Qara Khitai'. Fix: Lowered to 2 and the sentence added to the note.

Spot checks:

- /ledger/9: confirmed, 'The Battle of Qatwan took place ... on 9 September 1141' (https://en.wikipedia.org/wiki/Qara_Khitai)
- /ledger/10: confirmed, 'After this battle, Khwarazm became a vassal state of the Khitans'; Erbuz sent to Khwarazm (1142) (https://en.wikipedia.org/wiki/Qara_Khitai)
- /ledger/14: confirmed, Balkh 1198 confirmed; Andkhud not named for 1198, confidence lowered to 2 (https://en.wikipedia.org/wiki/Qara_Khitai)
- /ledger/15: confirmed, 'In 1204, the Qara Khitai put down a rebellion in Khotan and Kashgar' (https://en.wikipedia.org/wiki/Qara_Khitai)
- /ledger/24: confirmed, 'In 1216, Genghis Khan dispatched his general Jebe to pursue Kuchlug' (https://en.wikipedia.org/wiki/Kuchlug)
- /ledger/27: confirmed, 'The Mongols fully conquered the former territories of the Qara-Khitai in 1220'; infobox 'All former territories fully absorbed into Mongol Empire: 1220' (https://en.wikipedia.org/wiki/Qara_Khitai)
- /ledger/21: confirmed, 'in 1211 ... he was ambushed and captured by Kuchlug'; infobox 'Kuchlug usurps power: 1211' (https://en.wikipedia.org/wiki/Kuchlug)
- /ledger/1: confirmed, 'Within a year, he had established himself as suzerain of Qocho' (c. 1130-1131) (https://en.wikipedia.org/wiki/Qara_Khitai)

For the gap-filler:

- /ledger/7: date and holder of Dzungaria and Hami (1139, confidence 1) (try https://en.wikipedia.org/wiki/Naiman)
- /ledger/11: date of the middle Syr Darya steppe (1147, confidence 1) (try https://en.wikipedia.org/wiki/Kankalis)
- /ledger/12: any page for 55,000 km2 of Pamir cells at 62-76 E going to the Lohara row in 1152 (confidence 1; a Kashmiri dynasty that far west is unlikely, probably a Cliopatria artefact to report in data/README.md) (try https://en.wikipedia.org/wiki/Lohara_dynasty)
- /ledger/25: date of Khwarazm's hold on Samarkand, Fergana and Tashkent (1216, confidence 1) (try https://en.wikipedia.org/wiki/Khwarazmian_Empire)

## Cross-dossier matrix

- eastern-kara-khanids 1046 found (counterpart kara-khanids) -> kara-khanids 1045 split: matched. within one year; kara-khanids splits the East and 'dissolves' into the West in 1045
- western-karakhanid-khanate 1046 found (counterpart kara-khanids) -> kara-khanids 1045 dissolve: matched. kara-khanids types the western half as dissolve, the eastern as split (ia-01-f)
- eastern-kara-khanids 1066 loss (counterpart western-karakhanid-khanate) -> western-karakhanid-khanate 1066 gain: matched. Fergana, confidence 1 on both sides
- eastern-kara-khanids 1096 gain (counterpart qocho-kingdom) -> qocho-kingdom 1096 loss: mismatch. year matches, land does not: qocho-kingdom keyframe qocho-kingdom_1040 (to 1125) still holds Kucha, 39 cells overlap the Eastern 1094-1125 shape; ia-01-f to remove Kucha from 1096
- eastern-kara-khanids 1134 loss (counterpart kara-khitans) -> kara-khitans 1134 gain: mismatch. both name Semirechye only; 554 further cells leave the Eastern shape in 1134 and reach kara-khitans only in 1139 with no event on either side
- kara-khitans 1141 vassal_start (counterpart eastern-kara-khanids) -> no mirror: missing. eastern-kara-khanids has no vassal_start (Kara-Khanid infobox 'Qara Khitai vassal (1141-1212)')
- kara-khitans 1211 vassal_end (counterpart eastern-kara-khanids) -> no mirror: missing. eastern-kara-khanids has no vassal_end; it dissolves in 1211
- kara-khitans 1141 vassal_start (counterpart western-karakhanid-khanate) -> no mirror: missing. western-karakhanid-khanate has no vassal events
- kara-khitans 1210 vassal_end (counterpart western-karakhanid-khanate) -> no mirror: missing. western-karakhanid-khanate has no vassal events
- western-karakhanid-khanate 1137 loss (counterpart kara-khitans) -> kara-khitans 1137 gain: matched. Fergana and Chach, month 5 both sides
- western-karakhanid-khanate 1073 loss (counterpart great-seljuk-empire) -> no mirror: exception. great-seljuk-empire (me-09) not run yet; Termez
- western-karakhanid-khanate 1089 vassal_start (missing) (counterpart great-seljuk-empire) -> no mirror: exception. me-09 not run; the West itself should also carry the 1089-1141 pair
- western-karakhanid-khanate 1207 loss (counterpart khwarezmid-empire) -> no mirror: exception. me-09 not run; Bukhara
- western-karakhanid-khanate 1212 dissolve (counterpart khwarezmid-empire) -> no mirror: exception. me-09 not run
- kara-khitans 1130 vassal_start (counterpart qocho-kingdom) -> qocho-kingdom 1128 vassal_start: mismatch. two years apart; pages: Qocho 1128 (text) and 1132 (infobox), Qara Khitai and Yelu Dashi c. 1130; suggest 1130 on both sides
- kara-khitans 1209 vassal_end (counterpart qocho-kingdom) -> qocho-kingdom 1209 vassal_end: matched. 
- kara-khitans 1137 gain (counterpart western-karakhanid-khanate) -> western-karakhanid-khanate 1137 loss: matched. 
- kara-khitans 1139 gain (counterpart nobody) -> qocho-kingdom 1139 keyframe: mismatch. the 1139 gain draws Hami as direct land while qocho-kingdom_1139 (1139-1369) adds Hami to Qocho: 109 cells double-drawn
- kara-khitans 1147 gain (counterpart kimek-kipchak-confederation) -> kimek-kipchak-confederation 1147 loss: matched. 292 cells, confidence 1 both sides
- kara-khitans 1147 gain (missing) (counterpart khwarezmid-dynasty) -> no mirror: missing. 972 cells of the Khwarezmid Dynasty 1146 shape enter the direct shape in 1147 with no event; me-09 not run
- kara-khitans 1130 gain (missing) (counterpart kimek-kipchak-confederation) -> kimek-kipchak-confederation None None: missing. the Emil base overlaps the Kimek dossier's shape 1130-1138 (58-127 cells) with no event on either side
- kara-khitans 1134 vassal_start (counterpart Karluks of Almaliq) -> no mirror: exception. listed under counterparts_needing_dossiers (ia-01-x)
- kara-khitans 1142 vassal_start (counterpart khwarezmid-dynasty) -> no mirror: exception. me-09 not run
- kara-khitans 1152 loss (counterpart lohara-dynasty) -> no mirror: exception. sa-03 not run; confidence 1 and implausible extent
- kara-khitans 1165 gain (counterpart Khorasan emirs (page silent on the holder)) -> no mirror: exception. no dossier; holder unnamed on the page
- kara-khitans 1198 loss (counterpart ghurid-dynasty) -> no mirror: exception. sa-04 not run
- kara-khitans 1210 loss (counterpart khwarezmid-empire) -> no mirror: exception. me-09 not run
- kara-khitans 1216 loss (counterpart khwarezmid-empire) -> no mirror: exception. me-09 not run
- kara-khitans 1210 keyframe (counterpart eastern-kara-khanids) -> eastern-kara-khanids 1211 dissolve: mismatch. kara-khitans_1210 holds the Tarim rump from 1210 while the Eastern dossier holds it to 1211: 1,122 cells double-drawn in 1210-1211
- kara-khitans 1124 found (counterpart liao-dynasty) -> no mirror: exception. liao-dynasty (ea group) not run; it should lose or split the Orkhon Valley in 1124
- kara-khitans 1220 dissolve (counterpart mongol-empire) -> no mirror: exception. ia-02 not run
- cuman-kipchak-confederation 1055 found (counterpart kimek-kipchak-confederation) -> kimek-kipchak-confederation 1055 rename: mismatch. the Kimek dossier renames itself the Cuman-Kipchak confederation in 1055 and lists no split or successor for this dossier
- cuman-kipchak-confederation 1072 keyframe (counterpart kimek-kipchak-confederation) -> kimek-kipchak-confederation 1072 gain: mismatch. Kimek's 1072 gain from nobody takes 447 cells this dossier holds 1055-1241: double claim 1072-1241
- cuman-kipchak-confederation 1078 gain (counterpart nobody) -> no mirror: exception. nobody; pechenegs suggested (no dossier, ia-01-x)
- cuman-kipchak-confederation 1241 dissolve (counterpart mongol-empire) -> no mirror: exception. ia-02 not run

## Problems

- WebFetch returns a model-written extract of each page, not the page text; quotes in this review are the extract's wording.
- Battle of Qatwan page not opened; /ledger/9 of kara-khitans confirmed on the Qara Khitai page instead.
- Applied three small fixes and re-validated (0 errors, 0 warnings with --resolve): eastern-kara-khanids /ledger/1 note, western-karakhanid-khanate /ledger/1 note, kara-khitans /ledger/14 confidence 3 to 2.
- Cuman and Kimek-Kipchak dossiers describe the same confederation on either side of a seam (Kimek /ledger/2 rename in 1055); needs an orchestrator decision with ia-01-e.
- qocho-kingdom (ia-01-f) keeps Kucha in its 1040-1125 keyframe despite its own 1096 loss (39 cells overlap eastern-kara-khanids) and adds Hami from 1139 (109 cells overlap kara-khitans).
- Pairs of a vassal's own ledger with its overlord's: the schema says counterpart is the vassal in the overlord's ledger; the authors put the vassal events only there. Earlier ia-01 reviews asked for the mirror in the vassal's ledger too; this review does the same.
