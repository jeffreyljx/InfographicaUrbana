# Review of batch me-09-g (2026-10-25)

Reviewer for Phase B, batch me-09-g. The dossiers are jalayirid-sultanate, chobanids, injuids, kartids, beylik-of-teke and beylik-of-dulkadir. The validator (--resolve) gives 0 errors; the only warning is the place 'Elbistan', which the gazetteer lacks (3 times, in beylik-of-dulkadir). Under the orchestrator's adjustments the reviewer applied four small fixes that it had checked on the page, then re-validated: 0 errors. Page budgets: 1-2 pages for chobanids, injuids and kartids, up to 5 for the others. 'thin' is judged against that budget.

Verdicts: jalayirid-sultanate **thin**, chobanids **thin**, injuids **fix**, kartids **thin**, beylik-of-teke **pass**, beylik-of-dulkadir **thin**.

## jalayirid-sultanate: thin

Area: infobox None km2 (year None), Cliopatria 711752 km2, ratio None. The infobox gives no area (confirmed); the author says so at /keyframe_review/1.

Fixes:
- `/ledger/21` [applied by reviewer] The 1423 loss of Shushtar named the person 'Ibrahim Sultan' as counterpart, not a slug, and the note said the page does not say whom he served. Evidence: Jalayirid Sultanate page: in 1423 the penultimate ruler 'was expelled from Shushtar by the Timurid Governor of Fars Ibrahim Sultan'. Fix: counterpart timurid-empire; note rewritten with the quote.
- `/ledger/16` [applied by reviewer] The 1406 gain of Tabriz named timurid-empire and October as its month, but the page has Ahmad take Tabriz from Qara Yusuf, after Qara Yusuf's October 1406 victory. Evidence: Jalayirid page: Qara Yusuf won the 'Battle of Nakhchivan (1406), taking back control of Tabriz'; Ahmad 'eventually occupied Tabriz when Qara Yusuf was away in Armenia'; 'After expelling Qara Yusuf from Tabriz, Ahmad Jalayir would hold residence there between 1406 and 1410'. timurid-empire /ledger/22 also has the Timurids lose Tabriz to the Qara Qoyunlu in October 1406. Fix: counterpart qara-qoyunlu; month removed; note rewritten.
- `/ledger/15` [applied by reviewer] The 1405 recapture of Baghdad was at confidence 3, but the cited page dates only Timur's death and Ahmad's release to 1405, not the recapture itself. Evidence: Siege of Baghdad (1401): 'When Timur died in 1405 Nasir-ad-Din Faraj released Sultan Ahmad Jalayir and Qara Yusuf'; Ahmad 'finally managed to recapture the city of Baghdad' (no year). Fix: confidence 2, with a sentence added to the note.
- `/keyframe_review/4/correction` [for the author] The 1384 loss of Soltaniyeh (/ledger/9, a 60 km disk in Zanjan province) takes land that no keyframe gives the state: the 1375 shape lacks Soltaniyeh (gazetteer check: 0 of 1 cells), and the correction adds only East and West Azarbaijan. Evidence: Jalayirid page: 'his subordinates in Soltaniyeh failed to defend the town and Timur took it' (spring 1384). Fix: Add {"place": "Soltaniyeh", "km": 60, "country": "Iran"} to the K4 union (held to 1384), or drop the 1384 event's region to a note.
- `/ledger/23/region` [for the author] The 1432 dissolve region still contains Al Hillah, which /ledger/22 already lost in October 1431. Evidence: Jalayirid page: the Qara Qoyunlu 'managed to capture al-Ḥella in October 1431'. Fix: Dissolve region = union of Wasit and Al-Basrah; the K10 text could say Hillah until October 1431.

Thin (for a gap-filler):
- `/keyframe_review/4` When Mosul was lost: it is inside the 1363 shape and outside the 1375 shape, with no event. Try: https://en.wikipedia.org/wiki/Qara_Qoyunlu
- `/keyframe_review/6` When Khuzestan was lost (in the 1375 shape, outside the 1395 shape) and when Shushtar came back before 1410 (K9 has it with no gain event). /ledger/12 loses only the 1395 shape in 1393, so about 250,000 km2 has no loss event. Try: https://en.wikipedia.org/wiki/Ahmad_Jalayir
- `/ledger/7` Year of the Shirvan vassalage (confidence 1; the Awais page has a 1364 campaign and Kavus 'later' a vassal, with his son a hostage until 1372). Try: https://en.wikipedia.org/wiki/Shirvanshah
- `/ledger/8` End of the Shirvan vassalage (confidence 1, bridged to Uways's death in 1374). Try: https://en.wikipedia.org/wiki/Shirvanshah
- `/identity/capitals/1` Tabriz is the capital to 1387 (infobox 1358-1388), but /ledger/10 loses Tabriz in 1386; Baghdad is the capital through the landless years 1402-1404. Try: https://en.wikipedia.org/wiki/Jalayirid_Sultanate

Spot checks:
- `/ledger/4` https://en.wikipedia.org/wiki/Shaikh_Awais_Jalayir: confirmed: 'Uvais conquered the area in August 1358'
- `/ledger/1` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed: 'The Jalayirids occupied the Georgian capital Tiflis in 1357-1358'
- `/ledger/9` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed: spring 1384, Soltaniyeh taken
- `/ledger/12` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed: 'captured Baghdad (1393)'
- `/ledger/13` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed: 'the successful capture of Baghdad (1394)'
- `/ledger/15` https://en.wikipedia.org/wiki/Siege_of_Baghdad_(1401): not on page: the recapture has no year (1405 is the release); confidence lowered to 2
- `/ledger/16` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: mis-dated: October and the Timurid counterpart are not on the page; Ahmad took Tabriz from Qara Yusuf (fixed)
- `/ledger/21` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed for 1423 and Shushtar; the counterpart is 'the Timurid Governor of Fars' (fixed)
- `/ledger/22` https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed: al-Hella captured in October 1431

## chobanids: thin

Area: infobox None km2 (year None), Cliopatria 207604 km2, ratio None. No infobox area (confirmed).

Fixes:
- `/ledger/1` [for the author] The 1338 gain of Azerbaijan names jalayirid-sultanate, whose dossier starts in 1340, so it has no mirror and cannot have one. Evidence: Hasan Buzurg page: in 1338 'Hasan Buzurg was defeated; his puppet khan, Muhammad, was killed'; the Jalayirid page counts Hasan's reign from 1340 ('r. 1340-1356'), while the Hasan Buzurg succession table has '1336-1356'. The author flagged the gap in the notes. Fix: Use counterpart ilkhanate (Hasan fought for his puppet Ilkhan; the ilkhanate dossier runs to 1343), or else the jalayirid-sultanate dossier moves its start to 1336 or 1337 and adds the matching 1338 loss. Pick one and make both dossiers agree.
- `/ledger/3` [for the author] The 1342 loss puts Fars and Isfahan together, but only Isfahan is dated 1342; Shiraz (Fars) fell in March 1343. Evidence: Chobanids page: 'the takeover of the city [Isfahan] by the Injuid Abu Ishaq Inju in 1342' and no year for Fars; Injuids page: 'He took Shiraz from Yagi Basti in March 1343'. Fix: Split it: 1342 loss of Isfahan (Chobanids page) and a 1343-3 loss of Fars (cite the Injuids page and add it to sources), both counterpart injuids.

Thin (for a gap-filler):
- `/keyframe_review/1` The page's Anatolian and Mesopotamian holdings and the Anatolian share won by Malik Ashraf in 1338 are not located. Try: https://en.wikipedia.org/wiki/Malek_Ashraf
- `/identity/rulers` No ruler list (Hasan Kucek 1338-1343, Malik Ashraf 1343-1357). Try: https://en.wikipedia.org/wiki/Hasan_Kuchak

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Chobanids: confirmed: infobox 'Established: 1338'; realm 'in the area around Tabriz'
- `/ledger/1` https://en.wikipedia.org/wiki/Hasan_Buzurg: confirmed: 'Peace was declared in late 1338, Hasan Buzurg lost Azerbaijan to Hasan Kuchak and Anatolia to Malik Ashraf'
- `/ledger/2` https://en.wikipedia.org/wiki/Chobanids: confirmed: Pir Husayn 'governor of ... Fars and Isfahan regions from 1339 to 1342'
- `/ledger/3` https://en.wikipedia.org/wiki/Chobanids: confirmed for Isfahan 1342; Fars undated on this page (March 1343 on the Injuids page)
- `/ledger/4` https://en.wikipedia.org/wiki/Chobanids: confirmed: the Golden Horde 'captured Tabriz in 1357'; Malek Ashraf executed; infobox 'Disestablished: 1357'

## injuids: fix

Area: infobox None km2 (year None), Cliopatria 85841 km2, ratio None. No infobox area (confirmed). The infobox start is 1335; the dossier's 1343 is argued in the notes.

Fixes:
- `/ledger/0` [applied by reviewer] The found event named ilkhanate as the counterpart, while the chobanids dossier (/ledger/3) loses Fars and Isfahan to the Injuids and the page has the land come from Chobanid hands. Evidence: Injuids page: 'He had been given Isfahan by Pir Hosayn', described as 'the Chobanid Pir Hosayn'; 'He took Shiraz from Yagi Basti in March 1343'. Fix: counterpart chobanids; a sentence added to the note.

Thin (for a gap-filler):
- `/ledger/4` Year Shiraz fell to the Muzaffarids, between the 1353 siege and 1357 (confidence 2; the page gives no year). Try: https://en.wikipedia.org/wiki/Mubariz_al-Din_Muhammad
- `/ledger/5` Year of Abu Ishaq's execution (page: after the 1357 fall of Isfahan, no separate year). Try: https://en.wikipedia.org/wiki/Abu_Ishaq_Inju

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Injuids: confirmed: 'He took Shiraz from Yagi Basti in March 1343'
- `/ledger/1` https://en.wikipedia.org/wiki/Injuids: confirmed: 'he laid siege to Shiraz in 1353'
- `/ledger/3` https://en.wikipedia.org/wiki/Injuids: confirmed: Mubariz al-Din laid siege to Isfahan 'and captured it in 1357'
- `/ledger/4` https://en.wikipedia.org/wiki/Injuids: confirmed at confidence 2: Shiraz's fall has no year on the page

## kartids: thin

Area: infobox None km2 (year None), Cliopatria 576490 km2, ratio None. No infobox area (confirmed).

Fixes:
- `/ledger (1244-1349)` [for the author] No vassal events, though the dossier's own K0 text calls the Karts 'a vassal principality of the Mongols' and the page has them pay tribute until 1349: the map will draw 105 years of vassalage as full independence. Evidence: Kart dynasty page: 'then as vassal princes within the Mongol Empire'; 'In 1349, while Togha Temür was still alive, Mu'izz-uddin Husayn stopped paying tribute to him, and ruled as an independent Sultan.' Neither mongol-empire nor ilkhanate records the vassal either. Fix: Add vassal_start 1244 (counterpart mongol-empire), vassal_end 1294 / vassal_start 1294 (ilkhanate), vassal_end 1335 or 1343 (ilkhanate), and the tribute to Togha Temür to 1349 (vassal_end 1349), each citing the Kart dynasty page, region Hirat.
- `/keyframe_review/2/note` [for the author] amirate-of-qazaghan /ledger/1-2 makes Herat a Qazaghan tributary 1351-1358 ('made Herat a tributary in 1351'), with no mirror here; the K2 note calls the 1358 attack only a raid. Evidence: amirate-of-qazaghan.json /ledger/1 vassal_start 1351 and /ledger/2 vassal_end 1358, counterpart kartids. Fix: Add vassal_start 1351 and vassal_end 1358 with counterpart amirate-of-qazaghan, or say in the notes why the tribute is not accepted. The war "Qazaghan's invasion of Khurasan" should name amirate-of-qazaghan, not chagatai-khanate, as belligerent.

Thin (for a gap-filler):
- `/keyframe_review/0` Extent 1244-1343 (the 1344 outline is used unverified). Try: https://en.wikipedia.org/wiki/Herat
- `/keyframe_review/1` Husayn's conquests (Ghor, Badghis, Farah, Sistan) that would justify the 474,000 km2 shape. Try: https://en.wikipedia.org/wiki/Herat
- `/identity/rulers` No ruler list. Try: https://en.wikipedia.org/wiki/Kart_dynasty

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kart_dynasty: confirmed: infobox 'Foundation ... 1244' (text 1245)
- `/ledger/1` https://en.wikipedia.org/wiki/Kart_dynasty: confirmed: 'seizing the city of Nishapur around 1375 or 1376'
- `/ledger/2` https://en.wikipedia.org/wiki/Kart_dynasty: confirmed: 'In April 1381, Timur arrived before the city'; 'The city fell'
- `/ledger/3` https://en.wikipedia.org/wiki/Kart_dynasty: confirmed: infobox 'Disestablished: 1381'

## beylik-of-teke: pass

Area: infobox None km2 (year None), Cliopatria 30773 km2, ratio None. No infobox area (confirmed).

Thin (for a gap-filler):
- `/ledger/2` Who retook Antalya in 1373 (confidence 2; the Antalya page gives only 'Cypriot rule between 1361 and 1373'). Try: https://en.wikipedia.org/wiki/Kingdom_of_Cyprus
- `/identity/capitals/0` The seat of the beys while Antalya was Cypriot (1361-1373) and Ottoman (1391-1402); the capital is Antalya throughout. Try: https://en.wikipedia.org/wiki/Beylik_of_Teke
- `/identity/rulers` No ruler list. Try: https://en.wikipedia.org/wiki/Beylik_of_Teke

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Beylik_of_Teke: confirmed: 'established by a branch of the Hamidid dynasty in 1321'
- `/ledger/1` https://en.wikipedia.org/wiki/Peter_I_of_Cyprus: confirmed: landing 23 August 1361, city taken 24 August 1361 from 'The emir of Antalya, Teke'
- `/ledger/2` https://en.wikipedia.org/wiki/Antalya: confirmed at confidence 2: 'Cypriot rule between 1361 and 1373', recoverer not named
- `/ledger/3` https://en.wikipedia.org/wiki/Beylik_of_Teke: confirmed: 'the Ottoman Empire annexed the beylik in 1391'
- `/ledger/4` https://en.wikipedia.org/wiki/Beylik_of_Teke: confirmed: 'during his invasion of Anatolia in 1402, Timur restored Othman to his rule'
- `/ledger/5` https://en.wikipedia.org/wiki/Beylik_of_Teke: confirmed: 'In 1423, the Ottomans definitively re-annexed the beylik'

## beylik-of-dulkadir: thin

Area: infobox 70000 km2 (year None), Cliopatria 30414 km2, ratio 0.43. Acknowledged in K1 and the notes but not resolved; listed under thin.

Fixes:
- `/ledger (1337-1515)` [for the author] No vassal events, though mamluk-sultanate /ledger/35 has vassal_start 1471 with counterpart beylik-of-dulkadir and the author's own sources describe Mamluk overlordship. The author's rule that 'vassalage events belong to the suzerain's dossier' goes against the reviewer brief (a vassal_start of X is mirrored in X's ledger). Evidence: Beylik of Dulkadir page: in 1337 Qaraja took Elbistan, 'obtaining the title of na'ib from the Mamluk Sultan Al-Nasir Muhammad'; Battle of Turnadağ page (as quoted in the dossier's war note): 'a semi-independent Anatolian beylik under the sovereignty of Mamluk Egypt'. Fix: Add vassal_start 1471 (counterpart mamluk-sultanate, to mirror the Mamluk dossier) or 1337 (na'ib title), and a vassal_end at 1515-6 or at the switch to the Ottomans, citing the Dulkadir and Mamluk Sultanate pages.
- `/keyframe_review/3, /keyframe_review/4, /keyframe_review/7` [for the author] Malatya goes out of the state in 1385 (K3 minus), back in for 1402-1462 (K4-K6 ok, shape contains it) and out again in 1463 (K7), with no ledger event at any of the three changes. Evidence: Gazetteer check: Malatya is inside the 1344 shape. Mamluk Sultanate page: Malatya under a Mamluk governor in 1389; the war page has 'the Mamluk city of Malatya' in 1485. Fix: Either remove Malatya (40 km) from every keyframe 1385-1515, which needs no event, or add a dated loss (counterpart mamluk-sultanate) and gain for each change. Also say whether Malatya was Dulkadir in 1344-1384 at all.

Thin (for a gap-filler):
- `/keyframe_review/1` The infobox area is 70,000 km2 (undated) and the shapes about 30,400 km2 (ratio 0.43). The author acknowledges this but leaves it unresolved; the towns that would account for the difference (Kayseri, Harput, Antep, Bozok) are not dated on the pages opened. Try: https://en.wikipedia.org/wiki/Kayseri
- `/ledger/1` Confidence-1 contest_start of 1485 at Malatya (the war page gives no year for the Malatya attack). Try: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Mamluk_War_(1485%E2%80%931491)
- `/ledger` Shah Suwar's war of 1467-1472 and any land it moved (the dossier lists the war with empty zones). Try: https://en.wikipedia.org/wiki/Shah_Suwar

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Beylik_of_Dulkadir: confirmed: 'taking the town in 1337'; infobox 'Established: 1337', capital Elbistan 1337-1507
- `/ledger/2` https://en.wikipedia.org/wiki/Ottoman%E2%80%93Mamluk_War_(1485%E2%80%931491): confirmed: 'a peace treaty was eventually sealed in May 1491'; boundaries 'essentially unchanged'
- `/ledger/3` https://en.wikipedia.org/wiki/Beylik_of_Dulkadir: confirmed: infobox 'Marash (1507-1522)'
- `/ledger/4` https://en.wikipedia.org/wiki/Battle_of_Turnada%C4%9F: confirmed: 13 June 1515; 'After the battle, Beylik of Dulkadir ceased to exist'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| jalayirid-sultanate 1357 occupation_start (kingdom-of-georgia) | - | exception | kingdom-of-georgia is owned by eu-19, not run yet. |
| jalayirid-sultanate 1358 gain (golden-horde) | golden-horde 1357 loss | matched | Golden Horde 1357 'Azerbaijan lost to Shaikh Uvais'; Jalayirid August 1358 (Awais page). Within a year. |
| jalayirid-sultanate 1364 vassal_start (shirvan) | - | exception | shirvan is owned by eu-19, not run yet. |
| jalayirid-sultanate 1384 loss (timurid-empire) | timurid-empire | missing | timurid-empire (ia-02, written) has no 1384 gain of Soltaniyeh. |
| jalayirid-sultanate 1386 loss (timurid-empire) | timurid-empire | missing | timurid-empire has no 1386 gain of Tabriz and Azerbaijan; its /ledger/5 is a confidence-1 gain from 'unknown' in 1395. |
| jalayirid-sultanate 1393 loss (timurid-empire) | timurid-empire | missing | timurid-empire has no 1393 gain of Baghdad. |
| jalayirid-sultanate 1394 gain (timurid-empire) | timurid-empire | missing | timurid-empire has no 1394 loss of Baghdad. |
| jalayirid-sultanate 1401 loss (timurid-empire) | timurid-empire 1401 gain | matched | timurid-empire /ledger/10, June 1401. |
| jalayirid-sultanate 1405 gain (timurid-empire) | timurid-empire 1405 loss | matched | timurid-empire /ledger/21 (confidence 1). |
| jalayirid-sultanate 1406 gain (qara-qoyunlu) | - | exception | qara-qoyunlu (me-09) is not written yet. The reviewer changed the counterpart from timurid-empire; this agrees with timurid-empire /ledger/22 (Tabriz lost to the Qara Qoyunlu in October 1406). |
| jalayirid-sultanate 1410 loss (qara-qoyunlu) | - | exception | Tabriz and Baghdad, two events; qara-qoyunlu not written yet. |
| jalayirid-sultanate 1423 loss (timurid-empire) | timurid-empire | missing | After the reviewer's fix the counterpart is timurid-empire; that dossier has no 1423 gain of Shushtar. |
| jalayirid-sultanate 1431 loss (qara-qoyunlu) | - | exception | Hillah, and the 1432 dissolve; qara-qoyunlu not written yet. |
| chobanids 1338 gain (jalayirid-sultanate) | jalayirid-sultanate | mismatch | The Jalayirid dossier starts in 1340, so it cannot lose Azerbaijan in 1338. Both dossiers are in this batch; see the chobanids /ledger/1 fix. |
| chobanids 1339 gain (ilkhanate) | ilkhanate | missing | ilkhanate (written) has no 1339 loss of Fars and Isfahan; it dissolves in 1343. |
| chobanids 1342 loss (injuids) | injuids 1343 found | matched | After the reviewer's fix the Injuid found event names chobanids. Fars should be 1343-3 (see the chobanids /ledger/3 fix). |
| chobanids 1357 loss (golden-horde) | golden-horde 1356 gain | matched | Golden Horde dates Jani Beg's Tabriz to 1356; Chobanids page 1357. Within a year; the two dossiers should agree on one year. |
| injuids 1357 loss (muzaffarids) | - | exception | Isfahan and Fars; muzaffarids (me-09) not written yet. |
| kartids 1244 found (mongol-empire) | mongol-empire | missing | Neither dossier records the Kartid vassalage of 1244-1349 (see the kartids fix); ilkhanate has none either. |
| amirate-of-qazaghan 1351 vassal_start (kartids) | kartids | missing | Qazaghan makes Herat a tributary in 1351 (vassal_end 1358); kartids has no mirror. |
| kartids 1376 gain (sarbadars) | - | exception | sarbadars (me-09) not written yet; the Kart page has 'around 1375 or 1376'. |
| kartids 1381 loss (timurid-empire) | timurid-empire 1383 gain | mismatch | timurid-empire /ledger/1 dates the gain of Herat to 1383; the Kart dynasty page has Timur before Herat in April 1381 and the city falling. timurid-empire (ia-02) should move it to 1381. |
| beylik-of-teke 1321 found (beylik-of-hamid) | - | exception | beylik-of-hamid (me-09) not written yet. |
| beylik-of-teke 1361 loss (kingdom-of-cyprus) | kingdom-of-cyprus 1361 gain | matched | kingdom-of-cyprus /ledger/2. |
| beylik-of-teke 1373 gain (kingdom-of-cyprus) | kingdom-of-cyprus 1373 loss | matched | kingdom-of-cyprus /ledger/5. |
| beylik-of-teke 1391 loss (ottoman-empire) | ottoman-empire | missing | ottoman-empire (me-10, written) has no 1391 gain of Teke. |
| beylik-of-teke 1402 gain (ottoman-empire) | ottoman-empire 1402 loss | mismatch | ottoman-empire /ledger/25 loses the Anatolian block to 'Anatolian beyliks restored by Timur (Karaman, Germiyan, Aydın and others)', not a slug, so Teke is not named. |
| beylik-of-teke 1423 loss (ottoman-empire) | ottoman-empire 1429 gain | mismatch | ottoman-empire /ledger/33 has the Teke gain in 1429 at confidence 1 (Cliopatria's year); the Teke page has 'In 1423, the Ottomans definitively re-annexed the beylik'. ottoman-empire should move it to 1423. |
| mamluk-sultanate 1471 vassal_start (beylik-of-dulkadir) | beylik-of-dulkadir | missing | beylik-of-dulkadir has no vassal events; see its fix. |
| beylik-of-dulkadir 1515 loss (ottoman-empire) | ottoman-empire 1515 gain | matched | ottoman-empire /ledger/53. |

## Problems

- The orchestrator let the reviewer apply small fixes. Four were applied and re-validated (0 errors): jalayirid-sultanate /ledger/15 (confidence), /ledger/16 (counterpart and month), /ledger/21 (counterpart slug); injuids /ledger/0 (counterpart). Read back after more than ten seconds and still present.
- Fixes needed in neighbour dossiers, by owning group: timurid-empire (ia-02): Jalayirid events 1384, 1386, 1393, 1394, 1423 missing; Herat 1383 should be 1381. ottoman-empire (me-10): Teke 1391 gain missing; 1402 loss names no slug; Teke gain 1429 should be 1423. ilkhanate and mongol-empire: Kartid vassalage 1244-1349 and the Chobanid 1339 Fars/Isfahan loss missing. golden-horde: Tabriz 1356 against the Chobanids page's 1357.
- WebFetch returns a model summary of each page; quotes above are as that summary returned them.
- Context dossiers not yet written (counted as the exception 'owned by a group that has not run yet'): beylik-of-karaman, ramadanid-emirate, sarbadars, muzaffarids, aq-qoyunlu, beylik-of-aydin, qara-qoyunlu, kingdom-of-georgia, shirvan, beylik-of-hamid, safavid-dynasty.

Gazetteer names needed: Elbistan (place, beylik-of-dulkadir).
