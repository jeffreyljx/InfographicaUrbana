# Review of batch me-09-c (2026-10-25)

Reviewer: adversarial review, Phase B. Dossiers: kingdom-of-jerusalem, principality-of-antioch, county-of-tripoli, zengid-dynasty, mahdids, nabhani-dynasty. Validator (--resolve): 0 errors in all six; warnings are gazetteer unknown places (Jerusalem) and counterpart slugs without dossiers (artuqids, burid-dynasty, banu-ammar). No infobox gives an area, so no area ratio could be checked. Machine copy: history/notes/phase-b/reviews/me-09-c.json.

## Verdicts

- **kingdom-of-jerusalem**: fix
- **principality-of-antioch**: fail
- **county-of-tripoli**: thin
- **zengid-dynasty**: fail
- **mahdids**: pass
- **nabhani-dynasty**: thin

## kingdom-of-jerusalem: fix

Tried: all 36 events against the Kingdom page sentences, the keyframe chain (14.8k -> 36.9k -> 53.9k -> 19k+Transjordan -> 2.6k -> 8.9k -> 2.1k), capitals contiguity, the 1291 end against the 1293 Cliopatria overrun, mirrors in fatimid, ayyubid and mamluk ledgers. Could not break it beyond the two applied fixes; thin items are budget gaps.

Findings:
- `/ledger/5` (applied by reviewer): Sidon gain dated 1111 (Kingdom page's summary sentence) although the siege ended in December 1110; fatimid-caliphate /ledger/53 has 1110/12. Evidence: https://en.wikipedia.org/wiki/Siege_of_Sidon : siege '19 October - 5 December 1110', 'The city fell after 47 days', Sidon 'had been re-fortified by the Fatimids in 1098'. Fix: Re-dated to 1110, month 12, source Siege_of_Sidon (added to sources[]), confidence 3 (page names the place, date and the Fatimids); note keeps the Kingdom page's '1111'.
- `/ledger/22` (applied by reviewer): Confidence 3 with a region place (Ramla) the page does not name. Evidence: https://en.wikipedia.org/wiki/Sixth_Crusade : 'Frederick also received Bethlehem and Nazareth, part of Sidon district, and Jaffa and Toron'; 'cede Jerusalem to the Franks, along with a narrow corridor to the coast'. No Ramla. Fix: Confidence lowered to 2 with a reviewer note (Ramla stands in for the corridor). The author may add Toron and Bethlehem as places if wanted.

Gaps for a gap-filler:
- `/ledger/24 and /ledger/26`: The lands of the 1240-1241 restitution (Galilee, Beaufort, Safed, Tiberias, Ascalon?) and the 1247 Ayyubid reoccupation; the region is the 1175 shape minus the coast as a stand-in (confidence 2). Try: https://en.wikipedia.org/wiki/Barons%27_Crusade
- `/keyframe_review/5 (1192-1235)`: Events inside the 1192 shape: Beirut and Sidon recovered and Jaffa lost in 1197, Jaffa and Ramla returned 1204; the 1192 shape already reaches Beirut (bbox north 33.9075) though Beirut was Ayyubid until 1197. Try: https://en.wikipedia.org/wiki/Crusade_of_1197
- `/keyframe_review/3 (1169)`: The Negev and Gulf of Aqaba arm drops out of the 1169 shape with no event (Ayla taken by Saladin c. 1170); the correction restores Transjordan only. Try: https://en.wikipedia.org/wiki/Aqaba
- `/ledger/2, /ledger/4`: Previous owners of Acre (1104) and Beirut (1110) not on the pages (Fatimid at confidence 2); fatimid-caliphate has no 1104 Acre or 1110 Beirut loss to mirror them. Try: https://en.wikipedia.org/wiki/Siege_of_Acre_(1104)

Spot checks:
- `/ledger/12` on https://en.wikipedia.org/wiki/Kingdom_of_Jerusalem: confirmed ('In 1163 the chaotic situation in Egypt led to a refusal to pay tribute to Jerusalem'; /ledger/11 'reduced to a tributary state' also on the page)
- `/ledger/14` on https://en.wikipedia.org/wiki/Kingdom_of_Jerusalem: confirmed ('Saladin easily overran the entire kingdom'; 'Only the port of Tyre remained in Frankish hands')
- `/ledger/28` on https://en.wikipedia.org/wiki/Kingdom_of_Jerusalem: confirmed ('In 1265, Baibars took Caesarea, Haifa and Arsuf, and Safad and Toron in 1266'; 1268 Jaffa and Beaufort also confirmed for /ledger/27 and /ledger/29)
- `/ledger/33` on https://en.wikipedia.org/wiki/Kingdom_of_Jerusalem: confirmed ('Tyre fell without a fight the next day, Sidon fell in June, and Beirut in July')
- `/ledger/5` on https://en.wikipedia.org/wiki/Siege_of_Sidon: mis-dated (1111 on the Kingdom page, December 1110 on the siege page); fixed by reviewer
- `/ledger/22` on https://en.wikipedia.org/wiki/Sixth_Crusade: confirmed for date and places except Ramla (confidence lowered)

## principality-of-antioch: fail

Findings:
- `/ledger (missing, between /ledger/4 and /ledger/5)` (for the author): No event for the 1149 loss of the land east of the Orontes after Inab, the largest land move of the principality's middle years. Evidence: https://en.wikipedia.org/wiki/Principality_of_Antioch : 'Much of the eastern part of the Principality was lost, and Raymond was killed at the battle of Inab in 1149.' https://en.wikipedia.org/wiki/Nur_ad-Din_(died_1174) (cited in zengid-dynasty): after Inab 'he was content with capturing all Antiochene territory east of the Orontes'. Fix: Add a 1149 loss, counterpart zengid-dynasty, confidence 2, region {minus: [Principality of Antioch 1152, Principality of Antioch 1169, Harim ~10 km]} with the page text; zengid-dynasty needs the mirror gain.
- `/ledger/5 and /keyframe_review/3, /keyframe_review/4` (for the author): The 1164 event and the K3/K4 notes put all the land east of the Orontes into the 1164 loss and call the 1139 and 1152 shapes right to 1163; the pages put most of it in 1149 and only Harim in 1164. Evidence: Same two sentences as above; https://en.wikipedia.org/wiki/Battle_of_Harim : Nur ad-Din 'captured Harim a few days later' (12 August 1164); the Orontes boundary sentence on the Principality page follows Harim but the land had gone in 1149. Fix: Narrow /ledger/5 to Harim and its district (~10-15 km); mark principality-of-antioch_1139 adjust (shape as drawn, land east of the Orontes lost 1149 by ledger) and principality-of-antioch_1152 adjust with correction {minus: [Principality of Antioch 1152, the east bank except Harim]}.
- `/ledger/3 and /ledger/4 region` (for the author): The 1119 loss and the 1119 regain both use all of Idlib province plus a 25 km circle round Aleppo city; Aleppo was Ilghazi's own city, never Antiochene, so /ledger/4 hands Aleppo to Antioch from 1119 to 1164, and all of Idlib includes Harim and the Orontes valley that were not lost. Evidence: /ledger/3 text names only 'Atharib, Zerdana, Sarmin, Ma'arrat al-Numan and Kafr Tab' (Battle of Ager Sanguinis page); /ledger/4 text 'some of the lost towns (unnamed)'. Fix: Replace the union by coordinate circles (8-10 km) on the five named towns (Atharib ~36.83E 36.14N, Zerdana, Sarmin, Ma'arrat al-Numan ~36.67E 35.65N, Kafr Tab) and drop the Aleppo circle; make /ledger/4 the same towns at confidence 1 or a subset.
- `/ledger (missing)` (for the author): Antioch's own vassal events are absent although the suzerains' ledgers carry them: Jerusalem 1119-1126 (kingdom-of-jerusalem /ledger/7, /ledger/9) and Byzantium 1138- (byzantine-empire /ledger/127, /ledger/134). Evidence: https://en.wikipedia.org/wiki/Principality_of_Antioch : 'Antioch became a vassal state of Jerusalem with King Baldwin II as regent until 1126'; infobox 'Vassal of the Byzantine Empire (1138-1153, 1159-1183)', 'Vassal of the Armenian Kingdom of Cilicia (1254-1260)', 'Vassal of the Ilkhanate (1260-1268)'. Fix: Add vassal_start/vassal_end pairs: kingdom-of-jerusalem 1119/8-1126; byzantine-empire 1138-1153 and 1159-1183; armenian-kingdom-of-cilicia 1254-1260; mongol-empire 1260-1268 (the ilkhanate dossier starts in 1294).
- `/ledger/8, /ledger/9` (for the author): The Antiochene Succession war is a contest 1203-1219 here, but armenian-kingdom-of-cilicia has a 1204 gain from Antioch and an occupation 1216/2-1219; the Amanus castles Leo seized c. 1205 are on the page the author cited and not in this ledger. Evidence: https://en.wikipedia.org/wiki/War_of_the_Antiochene_Succession : Leo 'entered Antioch on 11 November' 1203; c. 1205 Leo seized Antiochene fortresses in the Amanus Mountains; 'Leo and his army entered Antioch during the night of 14 February 1216'; Raymond-Roupen consecrated prince; Bohemond IV reclaimed it in 1219. Fix: Add a c.1205 loss of the Amanus castles to armenian-kingdom-of-cilicia (confidence 2) and record 1216/2-1219 as occupation_start/occupation_end by armenian-kingdom-of-cilicia (or say in a note why a contest is kept).

Gaps for a gap-filler:
- `/ledger/7`: The 1188 shrink beyond Saone (Latakia, Jabala, Bourzey, Baghras, Darbsak taken by Saladin in July-September 1188) at confidence 1. Try: https://en.wikipedia.org/wiki/Saladin
- `/ledger/2`: The 1111 growth (Tancred's conquests; Tarsus, Latakia, Atharib) at confidence 1. Try: https://en.wikipedia.org/wiki/Tancred,_Prince_of_Galilee
- `/ledger/4`: Which towns Baldwin II recovered after Hab (confidence 1). Try: https://en.wikipedia.org/wiki/Battle_of_Hab
- `/keyframe_review/6`: The 1177 shape step, unexplained. Try: https://en.wikipedia.org/wiki/Bohemond_III_of_Antioch

Spot checks:
- `/ledger/6` on https://en.wikipedia.org/wiki/Principality_of_Antioch: confirmed ('Saone was captured by Saladin from the last lord, Matthew, in 1188')
- `/ledger/5` on https://en.wikipedia.org/wiki/Battle_of_Harim: confirmed for Harim, 12 August 1164; the 'land east of the Orontes' part is mis-dated (1149, see fixes)
- `/ledger/8` on https://en.wikipedia.org/wiki/War_of_the_Antiochene_Succession: confirmed ('he entered Antioch on 11 November' 1203)
- `/ledger/9` on https://en.wikipedia.org/wiki/War_of_the_Antiochene_Succession: confirmed (Bohemond IV reclaimed the principality in 1219)

## county-of-tripoli: thin

Every dated event checked holds; the border moves of 1126 and 1188 are unexplained within a spent 5-page budget, so thin by design. The vassal mirror is the one author-side bookkeeping fix.

Findings:
- `/ledger (missing, after /ledger/2 and before /ledger/8)` (for the author): No vassal_start/vassal_end with kingdom-of-jerusalem, although kingdom-of-jerusalem /ledger/3 (1109/7) and /ledger/30 (1289/4) carry the relation; same author, same batch. Evidence: https://en.wikipedia.org/wiki/County_of_Tripoli : 'Bertrand of Toulouse became the first count of Tripoli as a vassal of King Baldwin I of Jerusalem.' Infobox: 'Vassal of the Kingdom of Jerusalem, the Principality of Antioch and the Mongol Empire' (undated). Fix: Add vassal_start 1109/7 and vassal_end 1289/4, counterpart kingdom-of-jerusalem, region {cliopatria: County of Tripoli, year 1111} / 1285, confidence 2. Non-blocking (the suzerain side carries it), but needed for the mirror.

Gaps for a gap-filler:
- `/ledger (missing, 1104)`: Byblos (Jubayl, Gibelet) taken by Raymond in April 1104: fatimid-caliphate /ledger/52 records it as a loss to county-of-tripoli (Banu Ammar page: 'The family lost Jubayl to Raymond in April 1104'); this ledger and the new keyframe county-of-tripoli_1102 (Tartus 30 km) leave Byblos out until 1109. Try: https://en.wikipedia.org/wiki/Banu_Ammar
- `/keyframe_review/3 (1126)`: The 1126 growth from 4.2k to 6.2k km2 (Rafaniya/Montferrand and the Buqai'ah) has no gain event. Try: https://en.wikipedia.org/wiki/Pons,_Count_of_Tripoli
- `/ledger/4`: The 1188 halving (5.96k to 3.2k km2) at confidence 1: Tortosa town, Jabala, Arqa, Safita status after Saladin's 1188 campaign. Try: https://en.wikipedia.org/wiki/Saladin
- `/keyframe_review/6`: Tortosa (Templar until 1291) is outside the 1272-1285 shapes and the correction; Margat and Maraclea fell 1285; no events. Try: https://en.wikipedia.org/wiki/Tortosa_(Tartus)

Spot checks:
- `/ledger/1` on https://en.wikipedia.org/wiki/County_of_Tripoli: confirmed ('Tripoli fell on 12 July 1109')
- `/ledger/3` on https://en.wikipedia.org/wiki/Imad_ad-Din_Zengi: confirmed ('the permanent loss of the Crusader castle of Montferrand'; County page: 'In 1137, Raymond II, the reigning count, lost control of Montferrand')
- `/ledger/5` on https://en.wikipedia.org/wiki/Krak_des_Chevaliers: confirmed (army arrived 3 March, Chastel Blanc taken, surrender 'on 8 April 1271')
- `/ledger/7` on https://en.wikipedia.org/wiki/Siege_of_Tripoli_(1289): confirmed ('captured the city on 26 April'; Nephin and Le Boutron 'soon' after, /ledger/6; Peter of Gibelet 'kept his lands around Gibelet ... for about 10 more years')

## zengid-dynasty: fail

Findings:
- `/ledger (missing, 1182, between /ledger/16 and /ledger/17)` (for the author): No loss for Saladin's 1182 conquest of the Jazira (Edessa, Saruj, Raqqa, Qirqesiya, Nusaybin, Sinjar), although the page the author cites lists them and /wars/7 describes them; the 1177 -> 1188 keyframe step (300k -> 209k km2) is left unexplained and K5's note calls it 'unverified (page budget)'. Evidence: https://en.wikipedia.org/wiki/Zengid_dynasty : 'First, Edessa fell, followed by Saruj, then Raqqa, Qirqesiya and Nusaybin'; Sinjar 'fell after a 15-day siege on 30 December' (1182). Mirror already exists: ayyubid-sultanate /ledger/7 (1182 gain from zengid-dynasty, same sentence). Fix: Add a 1182 loss to ayyubid-sultanate (confidence 2; Sinjar month 12) with region {minus: [Zengid dynasty 1177, Zengid dynasty 1188]} or the named towns; K5 note to say the Jazira goes in 1182.
- `/ledger (missing, 1149, between /ledger/6 and /ledger/7)` (for the author): No gain for Inab (1149), when Nur ad-Din took all Antiochene territory east of the Orontes; /wars/3 names Inab but the ledger has no land change. Evidence: https://en.wikipedia.org/wiki/Nur_ad-Din_(died_1174) : 'he was content with capturing all Antiochene territory east of the Orontes'; Principality page: 'Much of the eastern part of the Principality was lost ... at the battle of Inab in 1149'. Fix: Add a 1149 gain from principality-of-antioch (confidence 2), region as in the Antioch fix (1152 shape minus 1169 shape minus Harim); narrow /ledger/11 to Harim.
- `/ledger/12, /ledger/13` (for the author): Egypt's vassalage starts in 1169 with counterpart ayyubid-sultanate, a dossier that starts in 1171 (its found event abolishes the Fatimids in September 1171); in 1169-1171 Egypt was still the Fatimid caliphate under Saladin as vizier. Neither fatimid-caliphate nor ayyubid-sultanate carries a mirror. Evidence: https://en.wikipedia.org/wiki/Zengid_dynasty : 'eventually seized control of Fatimid Egypt in 1169', 'bringing Egypt under formal Zengid dominion'; ayyubid-sultanate /ledger/0 '1171 found'; fatimid-caliphate /ledger/59 '1171/9 dissolve'. Fix: Write vassal_start 1169 / vassal_end 1171/9 with counterpart fatimid-caliphate, then vassal_start 1171/9 / vassal_end 1174/5 with ayyubid-sultanate; ask me-08 (Fatimid) and me-09 (Ayyubid) for the mirrors.
- `/ledger/5` (applied by reviewer): Baalbek dated to month 7 (July 1139); the page dates only the assassination of Shihab al-Din and Zengi's march on Damascus to July, not the fall of Baalbek. Evidence: https://en.wikipedia.org/wiki/Imad_ad-Din_Zengi : 'In July 1139 Zumurrud's surviving son, Shihab al-Din, was assassinated, and Zengi marched on Damascus'; 'Zengi did not keep his word to protect his captives at Baalbek in 1139'. Fix: Month removed, note amended.

Gaps for a gap-filler:
- `/ledger/16`: Hama, Homs and Baalbek lost to Saladin (Dec 1174 - spring 1175) at confidence 1. Try: https://en.wikipedia.org/wiki/Saladin
- `/ledger/19`: The Sinjar line's end: 1250 (Zengid page) against Lu'lu' holding Sinjar c. 1251 (Lu'lu' page); the 1182 Ayyubid capture of Sinjar against a Sinjar Zengid list to 1250. Try: https://en.wikipedia.org/wiki/Sinjar
- `/ledger (missing)`: Mosul as Saladin's vassal 1186-? (ayyubid-sultanate /ledger/9, /ledger/14 carry it) has no mirror here; nor the 1226 submission to Damascus or the Mongol tributary status 1243/1245-1262. Try: https://en.wikipedia.org/wiki/Badr_al-Din_Lu%27lu%27

Spot checks:
- `/ledger/1` on https://en.wikipedia.org/wiki/Zengid_dynasty: confirmed ('taking Aleppo from the squabbling Artuqids in 1128')
- `/ledger/2` on https://en.wikipedia.org/wiki/Imad_ad-Din_Zengi: confirmed ('he had Buri's son taken prisoner and seized Hama from him')
- `/ledger/5` on https://en.wikipedia.org/wiki/Imad_ad-Din_Zengi: mis-dated month (July is the assassination, not Baalbek); month removed by reviewer
- `/ledger/19` on https://en.wikipedia.org/wiki/Zengid_dynasty: confirmed ('In 1250, al-Jazira fell under the domination of An-Nasir Yusuf, the Ayyubid emir of Aleppo')
- `/ledger/20` on https://en.wikipedia.org/wiki/Zengid_dynasty: confirmed ('the Mongol siege and capture of Mosul in July 1262')
- `/ledger/8` on https://en.wikipedia.org/wiki/Nur_ad-Din_(died_1174): confirmed ('allowed Nur ad-Din to overthrow him in 1154'; 'Damascus was annexed to Zengid territory')

## mahdids: pass

Tried: the row swap against shapes.csv bboxes and both pages; the 1158/1159 start; the 1164 expansion and its counterpart; the 1174 end; the najahid-dynasty mirror (1158 dissolve, matched). Could not break it.

Gaps for a gap-filler:
- `/keyframe_review/6`: Date of the annexation of the Sulaymanid north Tihama ('attacking the Sulaymanids in northern Tihama whose territories were annexed', undated); the correction intersects the Tihama with Yemen, so the Jizan (Saudi) part of the Sulaymanid lands is left out. Try: https://en.wikipedia.org/wiki/Sulaymanids

Spot checks:
- `/ledger/0` on https://en.wikipedia.org/wiki/Zabid: confirmed ('the Mahdids took over Zabid in 1158'); Mahdids page has Ali dying 'soon after, in 1159' (noted by the author)
- `/ledger/1` on https://en.wikipedia.org/wiki/Mahdids: confirmed ('The cities Ta'izz and Ibb fell in 1164 and Aden was besieged in the same year'; conqueror unnamed, confidence 2 honest)
- `/ledger/2` on https://en.wikipedia.org/wiki/Mahdids: confirmed ('took Zabid on 13 May 1174')
- `/keyframe_review/0` on https://en.wikipedia.org/wiki/Nabhani_dynasty: confirmed swap: Nabhani page 'Country: Oman (historical)', founded 1154; shapes.csv puts mahdids_* at 55.5-59.9 E, 21.3-26.3 N (Oman) and nabhani-dynasty_1169 at 42.2-49.5 E, 12.6-18.6 N (Yemen)

## nabhani-dynasty: thin

One Cliopatria shape, 1-2 page budget, both pages used: thin by design. The row swap is right.

Findings:
- `/keyframe_review/5/correction` (for the author): nabhani-dynasty_1507 removes Muscat (30 km) from 1507 but no ledger event explains the step from nabhani-dynasty_1475; and the war W1 makes Hormuz, not the Nabhanis, the holder of Muscat in 1507. Evidence: Correction text 'Muscat, captured by the Portuguese in 1507' (Ya'rubid page); /wars/1 belligerents portuguese-empire, kingdom-of-hormuz, nabhani-dynasty; ledger has only 1154, 1475, 1624. Fix: Either add a 1507 loss (counterpart portuguese-empire, confidence 1-2) or, if Muscat was Hormuzi, drop the minus and say so in text. Small and non-blocking.

Gaps for a gap-filler:
- `/ledger (missing, 1515/4)`: The Portuguese protectorate 'imposed on 15 April 1515' (Nabhani ruler table) as vassal_start with portuguese-empire; portuguese-empire has no mirror either. Try: https://en.wikipedia.org/wiki/Portuguese_Muscat
- `/ledger/1`: The 1475 shrink to 4.4k km2 at confidence 1 (Ibadi imamate regaining Nizwa and Rustaq, undated; the page has Imam Muhammad ibn Ismail removing Suleiman bin Mudhafar in 1500). Try: https://en.wikipedia.org/wiki/Imamate_of_Oman
- `/keyframe_review/5`: The 1507-1624 bridge (whole Nabhani rump carried for 117 years) is unverified. Try: https://en.wikipedia.org/wiki/History_of_Oman

Spot checks:
- `/ledger/0` on https://en.wikipedia.org/wiki/Nabhani_dynasty: confirmed ('They were expelled in 1154, when the Nabhani dynasty came to power'; al-Fallah 'had taken control by 1154')
- `/ledger/2` on https://en.wikipedia.org/wiki/Nabhani_dynasty: confirmed ('In 1624 Nasir bin Murshid of the Ya'Aruba took over control of Oman'; 'ruled Oman as hereditary kings (muluk) from 1154 until 1624')
- `/identity/capitals/0` on https://en.wikipedia.org/wiki/Nabhani_dynasty: confirmed ('The Nabhan came to make their capital at Bahla'; seat fluctuated among Nizwa, Bahla and Maqniyat)

## Cross-dossier matrix

- kingdom-of-jerusalem 1099 found / fatimid-caliphate -> fatimid-caliphate 1099 loss: **matched**. fatimid /ledger/50 (1099/7).
- kingdom-of-jerusalem 1104 gain / fatimid-caliphate -> none: **missing**. Acre 1104: fatimid-caliphate has no 1104 Acre loss (its 1104/4 loss is Byblos to county-of-tripoli). Route to me-08.
- kingdom-of-jerusalem 1109 vassal_start / county-of-tripoli -> none: **missing**. Tripoli as Jerusalem vassal 1109-1289: county-of-tripoli has no vassal_start/vassal_end (same author). County page: Bertrand count "as a vassal of King Baldwin I".
- kingdom-of-jerusalem 1110 gain / fatimid-caliphate -> none: **missing**. Beirut (May 1110): fatimid /ledger/53 (1110/12) is Sidon; no Beirut loss on the Fatimid side. Route to me-08.
- kingdom-of-jerusalem 1110 gain / fatimid-caliphate -> fatimid-caliphate 1110 loss: **matched**. Sidon, re-dated by the reviewer from 1111 to 1110/12 (Siege of Sidon page); fatimid /ledger/53.
- kingdom-of-jerusalem 1119 vassal_start / principality-of-antioch -> none: **missing**. Antioch as Jerusalem vassal 1119-1126 (Principality page); principality-of-antioch carries no vassal events.
- kingdom-of-jerusalem 1124 gain / fatimid-caliphate -> fatimid-caliphate 1124 loss: **matched**. Tyre; fatimid /ledger/54.
- kingdom-of-jerusalem 1153 gain / fatimid-caliphate -> fatimid-caliphate 1153 loss: **matched**. Ascalon; fatimid /ledger/56.
- kingdom-of-jerusalem 1153 vassal_start / fatimid-caliphate -> none: **missing**. Egypt tributary to Jerusalem 1153-1163 (Kingdom page): fatimid-caliphate has no vassal_start/vassal_end. Route to me-08.
- kingdom-of-jerusalem 1164 loss / zengid-dynasty -> zengid-dynasty 1164 gain: **matched**. Banias; zengid /ledger/10.
- kingdom-of-jerusalem 1187 loss / ayyubid-sultanate -> ayyubid-sultanate 1187 gain: **matched**. ayyubid /ledger/11 (1187/10).
- kingdom-of-jerusalem 1189 loss / ayyubid-sultanate -> none: **missing**. Transjordan by 1189 (Oultrejordain page): no Ayyubid gain. Route to me-09.
- kingdom-of-jerusalem 1189 contest_start / ayyubid-sultanate -> ayyubid-sultanate 1187 contest_start: **mismatch**. Jerusalem contests Acre-Jaffa 1189-1192; ayyubid contest 1187/7-1192/9 (Hattin). Ends agree (1192/9); starts differ by two years over different land.
- kingdom-of-jerusalem 1191 gain / ayyubid-sultanate -> ayyubid-sultanate 1192 loss: **mismatch**. Acre retaken July 1191; ayyubid records only the 1192/9 coast loss (14 months later). Ayyubid side should add Acre 1191.
- kingdom-of-jerusalem 1192 gain / ayyubid-sultanate -> ayyubid-sultanate 1192 loss: **matched**. Treaty of Jaffa/Ramla; ayyubid /ledger/12.
- kingdom-of-jerusalem 1229 gain / ayyubid-sultanate -> ayyubid-sultanate 1229 loss: **matched**. ayyubid /ledger/16 (1229/2).
- kingdom-of-jerusalem 1239 loss / ayyubid-sultanate -> none: **missing**. Dawud retakes Jerusalem December 1239 (Kingdom page): no Ayyubid gain. Route to me-09.
- kingdom-of-jerusalem 1240 gain / ayyubid-sultanate -> none: **missing**. Theobald/Richard treaties 1240-1241: no Ayyubid loss. Route to me-09.
- kingdom-of-jerusalem 1244 loss / ayyubid-sultanate -> ayyubid-sultanate 1244 gain: **matched**. ayyubid /ledger/18.
- kingdom-of-jerusalem 1247 loss / ayyubid-sultanate -> none: **missing**. Ayyub reoccupies most of the 1239-1241 concessions by 1247: no Ayyubid gain. Route to me-09.
- kingdom-of-jerusalem 1265 loss / mamluk-sultanate -> mamluk-sultanate 1265 gain: **matched**. mamluk /ledger/8.
- kingdom-of-jerusalem 1266 loss / mamluk-sultanate -> mamluk-sultanate 1266 gain: **matched**. mamluk /ledger/9.
- kingdom-of-jerusalem 1268 loss / mamluk-sultanate -> mamluk-sultanate 1268 gain: **matched**. mamluk /ledger/10.
- kingdom-of-jerusalem 1289 vassal_end / county-of-tripoli -> none: **missing**. See 1109 vassal_start.
- kingdom-of-jerusalem 1291 loss / mamluk-sultanate -> mamluk-sultanate 1291 gain: **matched**. Acre, Tyre, Sidon, Beirut and the dissolve: mamluk /ledger/19, /ledger/20.
- principality-of-antioch 1119 loss / artuqids -> none: **exception**. artuqids has no dossier; listed in counterparts_needing_dossiers (group me-09-x, not run).
- principality-of-antioch 1164 loss / zengid-dynasty -> zengid-dynasty 1164 gain: **matched**. Harim; zengid /ledger/11. Both sides over-attribute the east bank to 1164 (lost 1149, see fixes).
- principality-of-antioch 1149 loss (missing) / zengid-dynasty -> none: **missing**. Inab 1149: neither Antioch nor zengid-dynasty records the loss of "all Antiochene territory east of the Orontes" (Nur ad-Din page). Both to add.
- principality-of-antioch 1188 loss / ayyubid-sultanate -> none: **missing**. Saone and the 1188 shrink: ayyubid-sultanate has no 1188 gain from Antioch. Route to me-09.
- principality-of-antioch 1203 contest_start / armenian-kingdom-of-cilicia -> armenian-kingdom-of-cilicia 1204 gain: **mismatch**. Cilicia: 1204 gain from Antioch, 1216/2 occupation_start, 1219 occupation_end; Antioch: contest 1203/11-1219 only. Antioch to add the c.1205 Amanus loss and the 1216-1219 occupation, or Cilicia to justify.
- principality-of-antioch 1219 contest_end / armenian-kingdom-of-cilicia -> armenian-kingdom-of-cilicia 1219 occupation_end: **mismatch**. Type differs (contest vs occupation).
- byzantine-empire 1138 vassal_start / principality-of-antioch -> none: **missing**. byzantine /ledger/127 (1138) and /ledger/134 vassal_end 1180 (confidence 1); Antioch has no mirror; the Byzantine side also lacks the 1153-1159 break and uses 1180 against the infobox 1183. Route both (Antioch: me-09-c; Byzantium: eu-05).
- principality-of-antioch 1268 loss / mamluk-sultanate -> mamluk-sultanate 1268 gain: **matched**. mamluk /ledger/11 (1268/5).
- county-of-tripoli 1109 gain / banu-ammar -> none: **exception**. banu-ammar has no dossier; listed in counterparts_needing_dossiers (me-09-x, not run).
- fatimid-caliphate 1104 loss / county-of-tripoli -> none: **missing**. fatimid /ledger/52: Byblos (Jubayl) lost to Raymond April 1104 (Banu Ammar page, which makes the Banu Ammar the loser); county-of-tripoli has no 1104 gain. Tripoli to add; Fatimid side may need counterpart banu-ammar.
- county-of-tripoli 1137 loss / zengid-dynasty -> zengid-dynasty 1137 gain: **matched**. Montferrand; zengid /ledger/3.
- county-of-tripoli 1188 loss / ayyubid-sultanate -> none: **missing**. ayyubid-sultanate has no 1188 gain from Tripoli (Tripoli event itself confidence 1). Route to me-09.
- county-of-tripoli 1271 loss / mamluk-sultanate -> mamluk-sultanate 1271 gain: **matched**. Krak; mamluk /ledger/12.
- county-of-tripoli 1289 loss / mamluk-sultanate -> mamluk-sultanate 1289 gain: **matched**. Tripoli, Batroun, Nephin and the dissolve; mamluk /ledger/18.
- zengid-dynasty 1127 found / great-seljuk-empire -> none: **exception**. great-seljuk-empire not written yet (group me-09 owns it; file absent).
- zengid-dynasty 1128 gain / artuqids -> none: **exception**. No dossier; counterparts_needing_dossiers.
- zengid-dynasty 1130 gain / burid-dynasty -> none: **exception**. No dossier; counterparts_needing_dossiers (me-09-x).
- zengid-dynasty 1138 gain / burid-dynasty -> none: **exception**. No dossier; counterparts_needing_dossiers (me-09-x).
- zengid-dynasty 1139 gain / burid-dynasty -> none: **exception**. No dossier; counterparts_needing_dossiers (me-09-x).
- zengid-dynasty 1154 gain / burid-dynasty -> none: **exception**. No dossier; counterparts_needing_dossiers (me-09-x).
- zengid-dynasty 1144 gain / county-of-edessa -> county-of-edessa 1144 loss: **matched**. edessa /ledger/9 (1144/12); edessa /ledger/11 Saruj 1145/1 falls inside the 60 km circle.
- zengid-dynasty 1150 gain / county-of-edessa -> county-of-edessa 1151 dissolve: **mismatch**. Zengid: remnants west of the Euphrates taken 1150 (Zengid page). Edessa: 1150 loss to byzantine-empire (sale of Turbessel) and 1151 dissolve with no counterpart ("fell to Nur ad-Din's captain Hassan in 1151"). Edessa (me-09) should name zengid-dynasty in 1151; Zengid could move to 1151.
- county-of-edessa 1146 contest_start / zengid-dynasty -> none: **missing**. edessa /ledger/12-13 (Joscelin's 1146 re-entry) has no Zengid contest mirror. Minor.
- zengid-dynasty 1169 vassal_start / ayyubid-sultanate -> none: **mismatch**. Counterpart ayyubid-sultanate starts in 1171; 1169-1171 Egypt was the Fatimid caliphate. No mirror in either. See zengid fixes.
- zengid-dynasty 1174 loss / ayyubid-sultanate -> ayyubid-sultanate 1174 gain: **matched**. Damascus; ayyubid /ledger/3 (1174/11).
- zengid-dynasty 1175 loss / ayyubid-sultanate -> ayyubid-sultanate 1175 gain: **matched**. Hama/Homs; ayyubid /ledger/4.
- ayyubid-sultanate 1182 gain / zengid-dynasty -> none: **missing**. ayyubid /ledger/7: Jazira 1182 (Edessa, Saruj, Raqqa, Qirqesiya, Nusaybin, Sinjar); zengid-dynasty has no loss (fix listed).
- zengid-dynasty 1183 loss / ayyubid-sultanate -> ayyubid-sultanate 1182 gain: **mismatch**. Aleppo: Zengid 1183/6 (Zengid page "Saladin conquered Aleppo in 1183", 12 June); ayyubid /ledger/8 1182/5 (Ayyubid page "In May 1182"). Thirteen months apart; Ayyubid side should follow 1183.
- ayyubid-sultanate 1186 vassal_start / zengid-dynasty -> none: **missing**. ayyubid /ledger/9 (Mosul 1186/3) and /ledger/14 vassal_end 1202: no mirror in zengid-dynasty (author left it to the suzerain).
- zengid-dynasty 1250 loss / ayyubid-sultanate -> none: **missing**. Jazira to an-Nasir Yusuf 1250: ayyubid-sultanate has no gain. Route to me-09.
- zengid-dynasty 1262 loss / mongol-empire -> none: **missing**. Mosul July 1262: mongol-empire (ia-02) has no gain (ilkhanate dossier starts 1294, so mongol-empire is the right counterpart). Route to ia-02.
- mahdids 1158 found / najahid-dynasty -> najahid-dynasty 1158 dissolve: **matched**. najahid /ledger/7.
- mahdids 1164 gain / unnamed highland lords (page silent) -> none: **exception**. Page silent on the previous holder of Ta'izz and Ibb.
- mahdids 1174 loss / ayyubid-sultanate -> ayyubid-sultanate 1174 gain: **mismatch**. ayyubid /ledger/2 (1174/5) has the gain with a free-text counterpart "Zabid, Aden and Sanaa (...)"; it should name mahdids (Zabid) and zurayid-dynasty (Aden). Route to me-09.
- nabhani-dynasty 1154 found / great-seljuk-empire -> none: **exception**. great-seljuk-empire not written yet (me-09); the page says only "the Seljuks" (Kirman Seljuks), noted by the author.
- nabhani-dynasty 1475 loss / Ibadi Imamate of Oman and Kingdom of Hormuz (page undated) -> none: **exception**. Free-text counterpart, confidence 1; both in counterparts_needing_dossiers.
- nabhani-dynasty 1624 dissolve / yarubid-dynasty -> none: **exception**. yarubid-dynasty has no dossier yet (group not run).
- nabhani-dynasty 1507 loss (missing) / portuguese-empire -> none: **missing**. Keyframe nabhani-dynasty_1507 removes Muscat; no ledger event and portuguese-empire has no 1507 Muscat gain.
- nabhani-dynasty 1515 vassal_start (missing) / portuguese-empire -> none: **missing**. Protectorate "imposed on 15 April 1515" (Nabhani page): neither side records it.

## Gazetteer names needed

Ascalon (kingdom-of-jerusalem), Arsuf (kingdom-of-jerusalem), Safed (kingdom-of-jerusalem), Beaufort Castle (kingdom-of-jerusalem), Toron (kingdom-of-jerusalem), Banias (kingdom-of-jerusalem, zengid-dynasty), Saone (principality-of-antioch), Atharib (principality-of-antioch), Zerdana (principality-of-antioch), Sarmin (principality-of-antioch), Maarrat al-Numan (principality-of-antioch), Kafr Tab (principality-of-antioch), Batroun (county-of-tripoli), Nephin (county-of-tripoli), Montferrand (county-of-tripoli, zengid-dynasty), Hama (zengid-dynasty), Baalbek (zengid-dynasty), Sinjar (zengid-dynasty), Bahla (nabhani-dynasty)

## Counterparts needing dossiers

- Artuqids (`artuqids`, 1101-1409): approximate dynasty span; used in principality-of-antioch 1119 and zengid-dynasty 1128
- Burid dynasty of Damascus (`burid-dynasty`, 1104-1154): zengid-dynasty 1130, 1138, 1139, 1154
- Banu Ammar emirate of Tripoli (`banu-ammar`, 1070-1109): county-of-tripoli 1109; also the Byblos 1104 loss (fatimid /ledger/52)
- Hamdanid sultanate of Sana'a (`hamdanids-of-sanaa`, 1099-1175): approximate; mahdids war W2; ayyubid 1175 free-text counterpart
- Kingdom of Hormuz (`kingdom-of-hormuz`, 1060-1622): approximate; nabhani-dynasty 1475 and W1
- Ibadi Imamate of Oman (medieval) (`ibadi-imamate-of-oman`, 1406-1624): approximate for the second imamate; nabhani-dynasty 1475
- Sulaymanids of the northern Tihama (`sulaymanids`, 1069-1174): approximate; annexed by the Mahdids (undated, Mahdids page)

## Problems and notes

- No page failed for me. All six infoboxes lack an area figure, so no area ratio could be computed (area_check null, acknowledged by the authors).
- Row swap confirmed: Cliopatria 'Mahdids' (mahdids_1169..1502, 55.5-59.9 E, Oman) and 'Nabhani Dynasty' (nabhani-dynasty_1169, 42.2-49.5 E, Yemen) carry each other's geometry. data/README.md should list it. The mahdids 'wrong' verdicts give the same Oman shape as correction, with text 'belongs to the Nabhani dynasty'; the compiler must read a 'wrong' verdict whose correction is the reviewed shape itself as 'do not draw for this polity' and use the new mahdids_1158/_1164 keyframes for 1169-1174.
- zurayid-dynasty (me-08) notes call the Nabhani row 'an Omani artefact'; its geometry is Yemeni (the Mahdids'). Note-only correction for me-08.
- Reviewer edits applied in place and re-validated (0 errors): kingdom-of-jerusalem /ledger/5 (Sidon 1111 -> 1110/12, source Siege_of_Sidon added), /ledger/22 (confidence 3 -> 2); zengid-dynasty /ledger/5 (month 7 removed). Read back after writing; not replaced.
- Vassal bookkeeping in this batch is suzerain-only (Jerusalem carries Tripoli and Antioch; Byzantium, Ayyubids carry Antioch and Mosul); the vassal sides have no mirrors. The orchestrator may want one rule for which side must carry vassal_start.
- Mosul under Badr al-Din Lu'lu' (1234-1262) as a rename inside zengid-dynasty follows the research brief's dynasty-change rule (same land, no break); I do not ask for a separate state.
