# Review sa-04-x (reviewer, 2026-10-19)

Batch: 15 new dossiers by group sa-04-x (Delhi Sultanate additions), none with a Cliopatria row. Mechanical check: all 15 validate with 0 errors (--resolve warnings are the gazetteer places listed at the end). Spot checks: 4-8 events per dossier, weighted to confidence 3 and the largest land moves, each opened with WebFetch on 2026-10-19. Keyframe areas and overlaps were computed with tools/gazetteer.py (missing places replaced by coordinates for the computation only).

Verdicts: gujarat-sultanate **fix**, malwa-sultanate **fix**, gajapati-kingdom **fix**, reddi-kingdom **fail**, ahom-kingdom **fix**, khandesh-sultanate **thin**, madurai-sultanate **pass**, langah-sultanate **pass**, kingdom-of-mewar **fail**, kingdom-of-marwar **fail**, musunuri-nayaks **fail**, recherla-nayaks **thin**, kingdom-of-kandy **thin**, kingdom-of-sitawaka **fail**, kingdom-of-kotte **fail**.

Reviewer edits applied in place (each annotated '[Reviewer sa-04-x, 2026-10-19: ...]' and re-validated): ahom-kingdom (Guwahati 1648 -> 1658, keyframes 5-6, a source added), gajapati-kingdom (two confidence 3 -> 2), reddi-kingdom (war belligerent slug recherla-velamas -> recherla-nayaks), gujarat-sultanate (Khandesh vassalage confidence 3 -> 2), kingdom-of-marwar (Jalore confidence 3 -> 2). Every other finding is for the author (applied: false); the ones marked BLOCKING are why a dossier fails.

## gujarat-sultanate: fix
Area: infobox None (None), ratio None. No area on the page and no Cliopatria row; keyframes resolve to 61,500-99,700 km2 (254,000 with Malwa 1531-1536) with coordinate stand-ins for the missing gazetteer places.

Findings:
- `/ledger/8`: APPLIED. vassal_start 1437 of Khandesh at confidence 3, but the page gives no year. Evidence: Khandesh_Sultanate: 'He accepted the suzerainty of Gujarat sultanate' sits in Miran Adil Khan I's reign (1437-1441) with no date; 1437 is his accession. Fix: Confidence 3 to 2 (done by the reviewer; note annotated).
- `/ledger/28`: 1537 loss of the whole Malwa region to malwa-sultanate, but malwa-sultanate /ledger/13 gains only a 120 km circle round Mandu; the rest of Malwa belongs to no one in either dossier. Evidence: Malwa_Sultanate: Qadir Shah 'regained control over a part of the erstwhile kingdom' (1537). Fix: Split the loss: {place Mandu, km 120} to malwa-sultanate and the rest of {region Malwa} to nobody (or widen Malwa's gain), so both ledgers name the same land.
- `/ledger/8, /ledger/17, /ledger/20, /ledger/29`: The vassal events of Khandesh (1437-1573) and Malwa (1518-1531) exist only on the suzerain's side. Evidence: Reviewer brief rule 3: a vassal_start of X is a vassal_start in X's ledger with this state as counterpart; the author followed the Tang example's suzerain-only practice (notes). Fix: Nothing to change here; the mirrors go in khandesh-sultanate and malwa-sultanate (see those findings).
- `/ledger/24`: Daman ceded in December 1534 here, while portuguese-empire /ledger/18 gains Daman from Gujarat in 1539 (5 years apart). Evidence: Bahadur_Shah_of_Gujarat: the Treaty of Bassein (23 December 1534) gave Bassein 'as well as its territories, islands, and seas which included Daman and Bombay islands too'. Fix: Keep 1534 here; the portuguese-empire owner (am-06) should reconcile its 1539 Daman gain (cross-check row).

Thin (for a gap-filler):
- `/keyframe_review/0-9`: Saurashtra and Kutch are excluded except 70 and 60 km circles round Junagadh and Dwarka, for the whole life; the pages give no extent and Sorath after 1470 is likely Gujarat's. Try: https://en.wikipedia.org/wiki/Mahmud_Begada
- `/ledger/18, /ledger/22`: Idar contest with Mewar 1519-1532 at confidence 1 (no end on the page). Try: https://en.wikipedia.org/wiki/Rana_Sanga
- `/ledger/23`: Diu bridged to 1534 at confidence 1; portuguese-empire has 1535. Try: https://en.wikipedia.org/wiki/Diu_Fort

Spot checks: `/ledger/21` Bahadur_Shah_of_Gujarat: confirmed (Mandu fell 28 March 1531; Malwa page says 25 May 1531, noted by the author); `/ledger/24` Bahadur_Shah_of_Gujarat: confirmed (Treaty of Bassein, 23 December 1534, with Daman and Bombay); `/ledger/25` Gujarat_Sultanate: confirmed ('Humayun attacked Gujarat in 1535 and briefly occupied it'; the same page and the Bahadur page also say 1532, noted); `/ledger/30` Gujarat_Sultanate: confirmed ('The end of the sultanate came in 1573'); `/ledger/11` Gujarat_Sultanate: confirmed (infobox 'Conquest of Junagadh: 1467-1470'); `/ledger/8` Khandesh_Sultanate: not on page for the year (confidence lowered to 2)

## malwa-sultanate: fix
Area: infobox None (None), ratio None. No area on the page; region Malwa resolves to 154,600 km2.

Findings:
- `/ledger (1518, 1531)`: Missing vassal_start 1518 and vassal_end 1531 with counterpart gujarat-sultanate (mirror of gujarat-sultanate /ledger/17 and /ledger/20). Evidence: Malwa_Sultanate: 'Since 1518, Mahmud Shah II was a vassal of the Gujarat Sultan.' Bahadur_Shah_of_Gujarat: Mandu fell 28 March 1531 and 'Malwa was annexed'. Fix: Add vassal_start 1518 (region Malwa, confidence 3, Malwa page) and vassal_end 1531 month 3 (confidence 2, Bahadur page).
- `/keyframe_review/3`: Gagron (40 km) is Malwa's 1444-1530, but kingdom-of-mewar /ledger/2 gains Gagron from malwa-sultanate in 1468 (confidence 1): both draw it 1468-1530. Evidence: Rana_Sanga: the 1519 Battle of Gagron was fought against the Malwa Sultanate, so Malwa (Medini Rai) held Gagron then. Fix: Keep Gagron here; the Mewar dossier should drop its 1468 Gagron gain (see Mewar).
- `/ledger/10`: 1519 contest over the whole region with Mewar, while kingdom-of-mewar /ledger/5 records a gain of 'eastern Malwa' (Bhopal, 100 km) from Malwa that has no loss here: about 46,000 km2 drawn by both states 1519-1527. Evidence: Malwa_Sultanate: after Gagron (1519) 'Rana Sanga ... appointed one of his vassals, Medini Rai, to rule over the Sultanate'. Fix: Agree one model with the Mewar dossier: contest only (Mewar drops its gain), or a Malwa loss of {place Bhopal, km 100} in 1519 and its return in 1528.
- `/keyframe_review/5`: The 120 km circle round Mandu (1537-1541) takes in about 7,000 km2 (28 cells) of khandesh-sultanate's shape. Evidence: Gazetteer resolve of both keyframes; the page names no towns for Qadir Shah's 'part of the erstwhile kingdom'. Fix: Use {minus: [{place Mandu, km 120}, {region Khandesh}]} (also for /ledger/13 and /ledger/14).
- `/keyframe_review/0-3, /keyframe_review/7`: The gazetteer regions Malwa and Mewar share about 26 cells (6,600 km2), so Malwa and Mewar draw the same land 1401-1562. Evidence: Gazetteer resolve of {region Malwa} and {region Mewar}. Fix: Subtract {region Mewar} from Malwa's corrections, or ask the gazetteer agent to make the two regions disjoint (listed under problems).

Thin (for a gap-filler):
- `/ledger/3`: capital move to Mandu dated 1410 at confidence 1 Try: https://en.wikipedia.org/wiki/Hoshang_Shah
- `/ledger/11`: end of the Mewar hold bridged to 1528 at confidence 1 Try: https://en.wikipedia.org/wiki/Medini_Rai
- `/keyframe_review/4, /keyframe_review/6`: Malwa has no land 1531-1536 and 1542-1554 while alive; a gap-filler may split the state (author's note). Try: https://en.wikipedia.org/wiki/Qadir_Shah_of_Malwa

Spot checks: `/ledger/12` Malwa_Sultanate: confirmed with the page's 25 May 1531 (the Bahadur page has 28 March; month 3 used, noted); `/ledger/14` Malwa_Sultanate: confirmed ('in 1542, Sher Shah Suri conquered the kingdom'); `/ledger/15` Malwa_Sultanate: confirmed ('Baz Bahadur, declared himself independent in 1555'); `/ledger/16` Malwa_Sultanate: confirmed (Sarangpur, 29 March 1561); `/ledger/18` Malwa_Sultanate: confirmed ('In 1562, Akbar sent another army'); `/ledger/9` Mahmud_Khalji: confirmed (Mandalgarh 'captured ... in October 1457'); `/ledger/8` Mahmud_Khalji: confirmed at confidence 2 (besieged February 1444; the capture is implied, not stated)

## gajapati-kingdom: fix
Area: infobox None (None), ratio None. No area on the page; keyframes 143,000-222,000 km2.

Findings:
- `/ledger/11`: APPLIED. Confidence 3 with a region the page does not name: the Tirupati circle (Chandragiri) and the besieger. Evidence: Prataparudra_Deva: 'they had to surrender finally in the year 1514' (Udayagiri only). Fix: Confidence 3 to 2 (done by the reviewer).
- `/ledger/13`: APPLIED. Confidence 3 with Rajahmundry in the region, which the page does not name. Evidence: Prataparudra_Deva: Quli Qutb Shah 'captured many forts along with the regional administrative center of Kondapalli on 20 March 1531'. Fix: Confidence 3 to 2 (done by the reviewer).
- `/ledger/13`: golconda-sultanate (sa-04-d) has no 1531 gain from the Gajapatis. Evidence: golconda-sultanate ledger: no event in 1531. Fix: Nothing here; route to the golconda-sultanate owner (cross-check row).
- `/identity/predecessors/0`: eastern-ganga-kingdom (sa-03) names its successor 'suryavamsha-dynasty', not gajapati-kingdom. Evidence: eastern-ganga-kingdom /ledger/21 dissolve 1434 counterpart 'suryavamsha-dynasty'. Fix: Nothing here; the eastern-ganga owner should rename the slug (the author flagged it).

Thin (for a gap-filler):
- `/ledger/5, /ledger/6, /ledger/7`: Bahmani and Saluva losses of 1472 and the 1476 return at confidence 1 (bridged). Try: https://en.wikipedia.org/wiki/Purushottama_Deva
- `/keyframe_review/4`: 'By 1464 ... an empire stretching from the Ganges in the north to Tiruchirappalli in the south along the coast' (Gajapati page) is not drawn. Try: https://en.wikipedia.org/wiki/Hamvira_Deva

Spot checks: `/ledger/1` Kapilendra_Deva: confirmed (Gopinathpur inscription of 1447; Gar Mandaran); `/ledger/4` Kapilendra_Deva: confirmed (Udayagiri and Chandragiri 'in the year 1460 CE'); `/ledger/8` Prataparudra_Deva: confirmed ('reached the banks of river Krishna on 4 November 1500 AD'); `/ledger/11` Prataparudra_Deva: confirmed for Udayagiri 1514; region wider than the page (confidence lowered); `/ledger/13` Prataparudra_Deva: confirmed (Kondapalli, 20 March 1531; confidence lowered for Rajahmundry)

## reddi-kingdom: fail
Area: infobox None (None), ratio None. No area on the page; keyframes 23,000-57,000 km2.

Findings:
- `/keyframe_review/0, /keyframe_review/1`: BLOCKING. The 130 km circle round Guntur shares about 31,000 km2 (124 cells, 78 percent of the Reddi shape) with musunuri-nayaks /keyframe_review/1-2 in 1336-1367, and 9,000-12,000 km2 with recherla-nayaks (Telangana) in 1368-1434: the circle reaches Khammam and the Krishna-Godavari country. Evidence: Musunuri_Nayaks: Prolaya 'took control of the region between the Krishna and Godavari rivers'; Reddy_dynasty: the first capitals Addanki and Kondavidu lie south of the Krishna. Gazetteer resolve of the keyframes. Fix: Redraw the Reddi kingdom south of the Krishna before 1395 (for example {minus: [{place Guntur, km 130}, {union: [{place Khammam, km 120}, {place Vijayawada, km 40}, {region 'Telangana (region)'}]}]}) and agree the line with the Musunuri shape; then re-run the overlap.
- `/wars/2/belligerents`: APPLIED. Belligerent slug 'recherla-velamas' does not exist; the state's dossier is recherla-nayaks. Evidence: history/polities/recherla-nayaks.json. Fix: Slug corrected (done by the reviewer).

Thin (for a gap-filler):
- `/identity/rulers`: No ruler strip (the infobox reign ranges have no names). Try: https://en.wikipedia.org/wiki/Prolaya_Vema_Reddy
- `/ledger/1`: capital move to Kondavidu at confidence 1 (undated on the page) Try: https://en.wikipedia.org/wiki/Kondavidu_Fort
- `/keyframe_review/0`: 'At its maximum extent, the Reddi Kingdom stretched from Cuttack ... Kanchi ... Srisailam' is undated and not drawn. Try: https://en.wikipedia.org/wiki/Reddy_dynasty

Spot checks: `/ledger/0` Reddy_dynasty: confirmed ('established by Prolaya Vema Reddy in 1325'); `/ledger/2` Reddy_dynasty: confirmed ('Another subsidiary branch ... was established in 1395 at Rajahmundry'); `/ledger/3` Reddy_dynasty: confirmed ('In 1424, Kondavidu was annexed by the Vijayanagara Empire'); `/ledger/5` Kapilendra_Deva: confirmed ('brought under the sway of Kapilendra before A. D. 1448')

## ahom-kingdom: fix
Area: infobox 41957.8 (1826), ratio 1.22. No Cliopatria row; the 1682-1826 keyframe resolves to about 51,100 km2 (with a coordinate for Nagaon), acknowledged in its note.

Findings:
- `/ledger/13`: APPLIED. Gain of Guwahati and Kamrup dated 1648 at confidence 3; the page does not date the event to 1648 (that is Jayadhwaj's accession) and ties it to Shah Jahan's illness. Evidence: Ahom-Mughal_conflicts: Jayadhwaj Singha (1648-1663) acted 'taking advantage of the emperor Shah Jahan's illness and the war of succession'; Jayadhwaj_Singha: 'After the Mughal emperor Shah Jahan fell sick in 1658', the Ahoms 'pushed west and took control of the region up to the Sankosh river'. Fix: Year 1658, confidence 2; keyframe 5 now ends 1657 and keyframe 6 is ahom-kingdom_1658 from 1658; war outcome and source notes updated; Jayadhwaj_Singha added to sources (done by the reviewer).
- `/ledger/27`: Burmese occupation from June 1822 only; konbaung-dynasty /ledger/44 gains 'Ahom Assam, occupied from 1817' (5 years apart). Evidence: Burmese_invasions_of_Assam: 'The Burmese army left Assam in April 1817'; in 1819 'the Burmese army was able to occupy the capital' and 'Chandrakanta was reinstated as the king on March 9, 1819'. Fix: Keep 1822 here; consider a 1819-1821 vassal or occupation pair (the Burmese-installed Chandrakanta); the konbaung owner should move its gain to 1822 or 1819 (cross-check row).
- `/ledger`: No loss of the Assam Duars to Bhutan; kingdom-of-bhutan /ledger/13 gains them from ahom-kingdom in 1790 (confidence 1). Evidence: Ahom_kingdom page: Bhutan and the Duars are not mentioned. Fix: Add a confidence-1 loss of the Kamrup and Darrang Duars to kingdom-of-bhutan if a page supports it, or ask the Bhutan owner to drop it (cross-check row).

Thin (for a gap-filler):
- `/wars/3`: Koch-Ahom conflicts 1543-1568 have no zones or result. Try: https://en.wikipedia.org/wiki/Koch_dynasty
- `/keyframe_review/0`: early boundary 1228-1511 (a 90 km circle; page silent) Try: https://en.wikipedia.org/wiki/Sukaphaa
- `/identity/rulers`: no ruler strip although the page lists swargadeos Try: https://en.wikipedia.org/wiki/List_of_Ahom_kings
- `/ledger/28`: Matak tract tribute end bridged to 1826 at confidence 1 Try: https://en.wikipedia.org/wiki/Matak_Rajya

Spot checks: `/ledger/11-12` Ahom%E2%80%93Mughal_conflicts: confirmed ('a treaty of peace was signed in February 1639'; east of the Barnadi); `/ledger/13` Ahom%E2%80%93Mughal_conflicts: mis-dated (1648 not on the page for the event; 1658 per Jayadhwaj_Singha; fixed); `/ledger/14` Ahom%E2%80%93Mughal_conflicts: confirmed (Mir Jumla 1662; Pandu, Guwahati and Kajali fell); `/ledger/17` Ahom%E2%80%93Mughal_conflicts: confirmed (2 November 1667); `/ledger/18` Ahom%E2%80%93Mughal_conflicts: confirmed (March 1679, Laluk Sola); `/ledger/19` Ahom%E2%80%93Mughal_conflicts: confirmed (Itakhuli, September 1682; the Manas boundary); `/ledger/8` Ahom_kingdom: confirmed ('In 1536 ... up to the Kolong River in Nagaon'); `/ledger/27` Burmese_invasions_of_Assam: confirmed (Tilwa, June 1822)

## khandesh-sultanate: thin
Area: infobox None (None), ratio None. No area on the page; keyframes 36,000-46,000 km2.

Findings:
- `/ledger (1437, 1573)`: Missing vassal_start 1437 and vassal_end 1573 with counterpart gujarat-sultanate (mirror of gujarat-sultanate /ledger/8 and /ledger/29). Evidence: Khandesh_Sultanate: Miran Adil Khan I 'accepted the suzerainty of Gujarat sultanate' (reign 1437-1441, no year). Fix: Add vassal_start 1437 (confidence 2) and vassal_end 1573 (confidence 1, bridged to Gujarat's end), region Khandesh with Burhanpur.

Thin (for a gap-filler):
- `/ledger/4`: Berar lost in 1437 at confidence 1 (the page has the Bahmani army crushing Nasir Khan at Laling, undated). Try: https://en.wikipedia.org/wiki/Nasir_Khan_Faruqi
- `/keyframe_review/1`: one shape for 1400-1601: the 1508 succession war, the Ahmadnagar and Gujarat interventions and the 1574 Berar question are not on the pages opened (budget 2 pages). Try: https://en.wikipedia.org/wiki/Burhanpur

Spot checks: `/ledger/2` Khandesh_Sultanate: confirmed ('Soon after his accession in 1400, he captured the fort of Asirgarh'); `/ledger/3` Khandesh_Sultanate: confirmed ('In 1435, Nasir Khan ... attacked and captured Berar'; the gazetteer's Vidarbha carries the alias Berar); `/ledger/5` Khandesh_Sultanate: confirmed ('On April 8, 1599, Akbar reached Burhanpur'); `/ledger/6-7` Khandesh_Sultanate: confirmed ('Asirgarh fell to the Mughals only on January 17, 1601', citation needed on the page, noted)

## madurai-sultanate: pass
Area: infobox None (None), ratio None. No area on the page; shape about 39,000 km2. Tried: the founding and end years, the region against the page's 'Madurai, Tiruchirapalli and parts of South Arcot', the ruler list (the 1345-1356 gap is the page's), counterparts (tughlaq-dynasty mirrors the 1335 loss).

Spot checks: `/ledger/0` Madurai_Sultanate: confirmed ('proclaimed in 1335 in Madurai'; 'Madurai, Tiruchirapalli and parts of South Arcot'); `/ledger/1` Madurai_Sultanate: confirmed (Bowman: conquered and destroyed in 1370); `/ledger/2-3` Madurai_Sultanate: confirmed ('formally made Madurai to be its possession ... in 1378 CE'); `/wars/0` Madurai_Sultanate: confirmed (Ballala killed in 1343 at Kannanur Koppam; no land change)

## langah-sultanate: pass
Area: infobox None (None), ratio None. No area on the page; the 170 km circle is about 84,000 km2 and is called a reading in its note.

Thin (for a gap-filler):
- `/ledger/1`: Arghun move on Multan bridged to 1525 at confidence 1. Try: https://en.wikipedia.org/wiki/Shah_Husayn_Arghun

Spot checks: `/ledger/0` Langah_Sultanate: confirmed ('In 1445, Rai Sahra ... arrested Sheikh Yousaf and proclaimed himself sultan'); `/ledger/2-3` Langah_Sultanate: confirmed ('Multan fell in 1528 after an extended siege'; the 1527, 1530 and 1541 variants are noted by the author); `/keyframe_review/0` Langah_Sultanate: confirmed ('the lower Doab tract with Multan at its centre'; Chiniot and Shorkot)

## kingdom-of-mewar: fail
Area: infobox 33517 (1941), ratio 1.0. 1615-1949 keyframe resolves to 33,400 km2; the body's 14,000 km2 is noted by the author.

Findings:
- `/keyframe_review/1-5`: BLOCKING. Ajmer (60 km) is drawn as Mewar's from 1433 to 1567, against two pages the author opened; kingdom-of-marwar draws Ajmer too in 1534-1556 (with Sirohi/Jalore and Pali/Mewar, 11,600-17,000 km2 shared). Evidence: Mahmud_Khalji: 'Sultan Mahmud Khalji invaded and captured the fort of Ajmer' (undated, in the 1442-1457 wars); Maldeo_Rathore: Maldeo took Ajmer 'from Biram dev' after 1534. Fix: Add a loss of Ajmer to malwa-sultanate (confidence 1, bridged inside 1442-1457, Mahmud Khalji page) and drop Ajmer from keyframes 2-5 and from /ledger/13; Malwa mirrors the gain.
- `/ledger/2`: BLOCKING. 1468 gain of Gagron (and Ranthambore) from malwa-sultanate at confidence 1; malwa-sultanate keeps Gagron 1444-1530 with no loss, so both draw it 1468-1530 (and Gujarat's Malwa 1531-1536). Evidence: Rana_Sanga and Malwa_Sultanate: the 1519 Battle of Gagron was fought against the Malwa Sultanate, so Gagron was not Mewar's in 1519. Fix: Drop Gagron from /ledger/2 and keyframes 3-5 (keep Ranthambore only if a page gives it; Mewar page names none), or source a Malwa loss and a Mewar loss before 1519.
- `/keyframe_review/1`: Ajmer and Mandalgarh appear in 1433 with no ledger event. Evidence: Rana_Kumbha (as quoted in the note): Kumbha 'inherited' them in 1433, so they were Mewar's before 1433 and keyframe 0 lacks them. Fix: Add them to keyframe 0 from a sourced year, or a confidence-1 gain in 1433 'page silent'.
- `/ledger/4-5`: 1519: a contest_start and a gain over the same 'eastern Malwa' circle; malwa-sultanate records only a contest, so 46,000 km2 is drawn by both 1519-1527. Evidence: Rana_Sanga: 'After the 1519 Battle of Gagron ... he captured much of eastern Malwa' (Chanderi, Raisen, Sarangpur); Malwa page: Medini Rai ruled 'under the lordship' of the Rana. Fix: Keep one model shared with Malwa: either the contest (drop /ledger/5 and /ledger/8) or a gain matched by a Malwa loss.
- `/ledger/8`: 1528 loss of the Bhopal circle to mughal-empire (confidence 2): the page has Babur capturing Chanderi only, which lies outside the circle, and Raisen stayed with Silhadi (gujarat-sultanate /ledger/19 gains Raisen from 'Raisen' in 1531). Evidence: Rana_Sanga: 'Babur captured Chanderi, earlier ruled by Rai, after his victory' (no year); 'Raisen and Sarangpur (where Silhaditya Tomar established rule)'. Fix: Counterpart for the Raisen-Sarangpur country: Silhadi of Raisen (a name) or malwa-sultanate; mughal-empire only for {place Chanderi} if drawn.
- `/ledger (1615, 1818)`: No vassal events: Mewar is drawn sovereign 1615-1949 although the 1615 treaty made it a Mughal tributary and the 13 January 1818 treaty a British protectorate. Evidence: Kingdom_of_Mewar: 'In February 1615, Khurram and Amar Singh met in Gogundah'; 'the Treaty of Friendship, Alliances and Unity was concluded between Mewar and EIC on 13 January 1818'. Fix: Add vassal_start 1615 month 2 (mughal-empire) with an end, and vassal_start 1818 month 1 (british-empire or east-india-company) ending 1947/1949.
- `/ledger/0`: found 1326 with counterpart tughlaq-dynasty, but tughlaq-dynasty /ledger/15 loses Mewar to kingdom-of-mewar in 1336. Evidence: Kingdom_of_Mewar: Hammir 'attempted to regain control of Mewar' in 1326 and 'later recaptured Chittorgarh' (no year). Fix: Agree the year with the tughlaq-dynasty owner (cross-check row).

Thin (for a gap-filler):
- `/identity/rulers`: no ruler strip for 600 years Try: https://en.wikipedia.org/wiki/List_of_rulers_of_Mewar
- `/ledger/2, /ledger/3, /ledger/13`: Kumbha's conquests and their loss bridged at confidence 1 Try: https://en.wikipedia.org/wiki/Rana_Kumbha

Spot checks: `/ledger/1` Mahmud_Khalji: confirmed (Mandalgarh captured October 1457); `/ledger/12` Maharana_Pratap: confirmed ('the loss of the fertile eastern belt of Mewar to the Mughals'); `/ledger/15` Maharana_Pratap: confirmed (Haldighati 18 June 1576; September 1576 campaign: Gogunda, Udaipur, Kumbhalgarh); `/ledger/16` Maharana_Pratap: confirmed ('From 1585 till his death, the Rana had recovered a large part of Mewar'); `/ledger/5` Rana_Sanga: confirmed ('he captured much of eastern Malwa')

## kingdom-of-marwar: fail
Area: infobox 93424 (None), ratio 1.32. Body area 93,424 km2 (no year); region Marwar (1583-1678) resolves to 70,600 km2; the 1710-1949 shape cannot resolve until Nagaur, Jalore, Pokhran, Phalodi and Barmer are in the gazetteer.

Findings:
- `/ledger/12`: BLOCKING. 1557 loss of Ajmer and Nagaur to mughal-empire at confidence 3, but the same page says Marwar no longer held them: Haji Khan held them from 1544. Keyframes 5-6 keep them Marwar's 1545-1556. Evidence: Maldeo_Rathore: 'Haji Khan was a slave of Sher Shah Suri and became the lord of Ajmer and Nagaur after the Battle of Sammel'; 'Maldeo reoccupied his lost territories in 1545' names neither; 'The Mughals conquered Ajmer and Nagaur in 1557' (from Haji Khan). Fix: Add a 1544 loss of Ajmer and Nagaur to sur-empire (confidence 3); take them out of /ledger/10 (occupation_end 1545) and of keyframes 5 (from 1544) and 6; delete /ledger/12.
- `/ledger/3`: BLOCKING. 1453 'regain' of Mandore from nobody at confidence 3, of land the dossier already holds (keyframes 1 and 2 are the same circles): the loss of 1438 is missing. Evidence: Marwar_Kingdom: 'by 1453, he was able to regain Mandore'; Ranmal was 'assassinated in 1438' by Kumbha's party and Jodha fled Mewar. Fix: Add a loss of the Mandore-Jodhpur circle to kingdom-of-mewar in 1438 (confidence 2), split keyframe 1 at 1438, and give /ledger/3 the counterpart kingdom-of-mewar; Mewar mirrors both.
- `/ledger/6`: APPLIED. Jalore 1538 at confidence 3; the page dates only the attack. Evidence: Maldeo_Rathore: 'In 1538 he ... sent Bida Rathore to attack Jalore'; the conquest is undated. Fix: Confidence 3 to 2 (done by the reviewer).
- `/ledger/16`: 1583 restores Marwar 'as a Mughal state' but no vassal event; the 6 January 1818 British treaty is also missing. Evidence: Marwar_Kingdom: 'In 1583, Akbar formally recognized ... Udai Singh as the ruler of Marwar as a Mughal state.' Fix: Add vassal_start 1583 (mughal-empire) with an end, and vassal_start 1818 (british-empire) ending 1947/1949.
- `/ledger/2`: Mandore 1395 from 'nobody', but the page says it came as dowry from the Parihars. Evidence: Marwar_Kingdom: Chunda 'received the city of Mandore as Dowry'. Fix: Counterpart 'Parihars of Mandore' (a name), and say dowry in the note.

Thin (for a gap-filler):
- `/keyframe_review/0`: Pali circle 1243-1394 (page silent on the early extent) Try: https://en.wikipedia.org/wiki/Rao_Siha
- `/identity`: Bikaner split from Marwar undated Try: https://en.wikipedia.org/wiki/Bikaner_State

Spot checks: `/ledger/3` Marwar_Kingdom: event confirmed ('by 1453 ... regain Mandore'); prior loss missing; `/ledger/8` Maldeo_Rathore: confirmed (Bikaner, battle of Sohaba 1542); `/ledger/9-10` Maldeo_Rathore: confirmed (Jodhpur occupied 1544; 'reoccupied his lost territories in 1545'); `/ledger/12` Maldeo_Rathore: contradicted (Haji Khan lord of Ajmer and Nagaur after Sammel); `/ledger/16` Marwar_Kingdom: confirmed (1583 'as a Mughal state'); `/ledger/21-23` Marwar_Kingdom: confirmed (1707 Jodhpur captured; February 1708 Bahadur Shah; 1710 recognition); `/ledger/6` Maldeo_Rathore: year of conquest not on page (confidence lowered)

## musunuri-nayaks: fail
Area: infobox None (None), ratio None. No area on the page; keyframes 19,000-106,000 km2.

Findings:
- `/keyframe_review/1-2`: BLOCKING. The 80 km circle round Vijayawada crosses the Krishna and takes in Kondavidu (80.25 E, 16.25 N), the Reddi capital 1328-1423, and Guntur: about 31,000 km2 shared with reddi-kingdom 1336-1367. Evidence: Musunuri_Nayaks: Prolaya 'took control of the region between the Krishna and Godavari rivers'. Fix: Keep the coast north of the Krishna (for example {minus: [{place Vijayawada, km 80}, {place Guntur, km 60}]}) and agree the line with the Reddi shape.
- `/ledger/4`: The 1368 dissolve hands the coastal circles (Rajahmundry, Vijayawada) to recherla-nayaks, whose only shape is the Telangana region; the coastal land goes to no one. Evidence: Recherla_Nayaks: 'the Recherlas got control of Telangana'; recherla-nayaks /keyframe_review/0. Fix: Dissolve region = the Telangana part to recherla-nayaks; the coastal part to nobody (or a sourced holder).
- `/identity/rulers/0-1`: Ruler spans 1330-1332 and 1333-1368 start before the state's 1335 start (validator warning). Evidence: Musunuri_Nayaks: Prolaya appeared at Rekapalle 'around 1330'; infobox 1335-1368. Fix: Clip the spans to 1335, or start the state c. 1333 with a note.

Thin (for a gap-filler):
- `/ledger/3`: Golconda cession bridged to 1361 at confidence 1 (the page dates only the Turquoise throne gift) Try: https://en.wikipedia.org/wiki/Bahmani_Sultanate

Spot checks: `/ledger/1` Musunuri_Nayaks: confirmed ('took control of Warangal from Malik Maqbul in 1336'); `/ledger/4` Musunuri_Nayaks: confirmed ('In 1368, the Recherla Nayakas subsequently annexed the territories'); `/ledger/3` Musunuri_Nayaks: confirmed at confidence 1 (Golconda ceded, undated); `/identity/capitals/0` Musunuri_Nayaks: confirmed (Rekapalle, near Bhadrachalam)

## recherla-nayaks: thin
Area: infobox None (None), ratio None. No infobox; Telangana region 111,000 km2. The overlap with reddi-kingdom is fixed on the Reddi side.

Thin (for a gap-filler):
- `/ledger`: No event between 1368 and 1435: the Bahmani attacks 'in the 1420s' and the Pangal war of 1419 left no contest or loss. Try: https://en.wikipedia.org/wiki/Recherla_Nayaks
- `/keyframe_review/0`: The whole Telangana region is a reading; the page places the strongholds 'at Rachakonda and Devarakonda in the Nalgonda district'. Try: https://en.wikipedia.org/wiki/Rachakonda_Fort
- `/identity/rulers`: one entry (1368-1375) for a dynasty dated 1375-1435 Try: https://en.wikipedia.org/wiki/Recherla_Nayaks

Spot checks: `/ledger/0` Recherla_Nayaks: confirmed (Bhimavaram 1368, 'got control of Telangana'); `/ledger/1` Recherla_Nayaks: confirmed ('captured Warangal as well as Rachakonda by 1435'); `/wars/0` Recherla_Nayaks: confirmed (Pangal 1419)

## kingdom-of-kandy: thin
Area: infobox None (None), ratio None. No area on the page; keyframes 12,900-25,000 km2 from modern districts.

Findings:
- `/keyframe_review/2`: The 1592 keyframe already holds Kegalle (the Four Korales), which /ledger/4 gains in 1594, and the Trincomalee and Batticaloa circles, which no event gains. Evidence: Kingdom_of_Kandy province table: Satara Korale '~1594-1815'; the ports appear only as lost in 1665. Fix: Start the Kegalle part in 1594 (a 1592-1593 keyframe without it) and add a confidence-1 gain of the east-coast ports, or drop them before 1665.
- `/ledger/2-3`: Kandy regains the uplands in 1592 while kingdom-of-sitawaka loses them in 1593: 24,800 km2 drawn by both in 1592. Evidence: Kingdom_of_Sitawaka: 'In 1593, he defeated Rajasinha I at Balane and Mawela, effectively securing Kandy's independence'; Kandy infobox: 'Ascension of Vimaladharmasuriya I: 1592'. Fix: Use one year in both dossiers (1593 for the land, keeping 1592 for the accession in the note).

Thin (for a gap-filler):
- `/ledger/5-6`: Portuguese capture of Kandy 1611-1612 at confidence 1 (the page gives no year) Try: https://en.wikipedia.org/wiki/Portuguese_conquest_of_the_Jaffna_kingdom
- `/ledger/9`: the 1675 return of Sabaragamuwa at confidence 1 Try: https://en.wikipedia.org/wiki/Rajasinghe_II
- `/ledger/11`: 1765/1766: the treaty returned 'not only the border districts but all of Kandy's coastal provinces'; the region names only Matara and Hanwella Try: https://en.wikipedia.org/wiki/Treaty_of_Batticaloa

Spot checks: `/ledger/1` Kingdom_of_Kandy: confirmed (infobox 'Conquest by Sitawaka: 1581'; the Sitawaka page has 1582, noted); `/ledger/7-8` Kingdom_of_Kandy: confirmed (1665: 'large parts of Sabaragamuwa', Kalpitiya, Kottiyar, Batticaloa, Trincomalee); `/ledger/10` Kingdom_of_Kandy: confirmed ('annexing Matara and Hanwella'); `/ledger/11` Kingdom_of_Kandy: confirmed ('By 1765 the Dutch were in a position to force a treaty'; table 1766, noted); `/ledger/12` Kingdom_of_Kandy: confirmed (Kandyan Convention 2 March 1815)

## kingdom-of-sitawaka: fail
Area: infobox None (None), ratio None. No area on the page; keyframes 5,000-6,000 km2 and 51,000 km2 in 1581-1592.

Findings:
- `/keyframe_review/0-4 (also /ledger/0, /ledger/9, /identity/predecessors, /identity/successors)`: BLOCKING. The 40 km circle round Avissawella (80.21 E, 6.95 N) takes in Kotte (79.92 E, 6.89 N, about 33 km away) and Colombo, so from 1521 Sitawaka's shape swallows the capital of the surviving Kotte kingdom, and kingdom-of-kotte /keyframe_review/4 resolves to one cell. Evidence: Kingdom_of_Sitawaka: 'The kingdom of Sitawaka initially covered a relatively small area including Kosgama, Ruwanwella, Yatiyanthota', Hanwella, Padukka, Ehaliyagoda, Kuruwita and Rathnapura, all within about 25 km of Avissawella or round Ratnapura. Fix: Use km 25 for this circle everywhere in both dossiers (Sitawaka and Kotte), then check that every Kotte keyframe resolves to land round Kotte and Colombo.
- `/keyframe_review/2`: The 1564 gain adds almost nothing (6,000 km2 before and after) because the circle already holds the land. Evidence: Gazetteer resolve of keyframes 1 and 2. Fix: Resolves with the radius fix; re-check.

Thin (for a gap-filler):
- `/ledger/7`: 1593 loss of the south and east to 'nobody' at confidence 1 Try: https://en.wikipedia.org/wiki/Rajasinghe_I
- `/keyframe_review/0`: extent before 1564 (circles and one district) Try: https://en.wikipedia.org/wiki/Mayadunne_of_Sitawaka

Spot checks: `/ledger/0` Kingdom_of_Sitawaka: confirmed (1521; the initial area list includes Hanwella, Padukka, Kuruwita, Ratnapura); `/ledger/1` Kingdom_of_Sitawaka: confirmed (Raigama 'annexed following the death of Raigam Bandara ... in 1538'); `/ledger/3` Kingdom_of_Sitawaka: confirmed (1574: 'Sitawaka garrisons at Nagalagama and Mapane expelled'); `/ledger/5` Kingdom_of_Sitawaka: confirmed ('the entirety of Sri Lanka into the Sitawakan fold ... with the exception of the Jaffna kingdom and Portuguese holdings in the south'); `/ledger/6` Kingdom_of_Sitawaka: confirmed (Balane and Mawela, 1593); `/ledger/9` Kingdom_of_Sitawaka: confirmed ('In 1594 the Portuguese forces sacked the city')

## kingdom-of-kotte: fail
Area: infobox None (None), ratio None. No area on the page and no Cliopatria row; keyframes range from 250 km2 (1521-1563, a resolver fault) to 60,500 km2 (1450-1466); the 1521-1563 collapse is not acknowledged.

Findings:
- `/identity, /ledger/0-6`: BLOCKING. Kotte is one state in two dossiers for 1412-1506: ceylon (sa-04-a, merged on 2026-10-19) lists 'Kingdom of Kotte' among its alt_names and carries the same events (ceylon /ledger/12 1412 rename to Kotte, 14 Jaffna 1450, 15 1467, 16 Kandy 1469), and jaffna-kingdom /ledger/3-4 mirror 1450 and 1467 with ceylon, not with this dossier. Evidence: history/polities/ceylon.json and jaffna-kingdom.json ledgers; Kingdom_of_Kotte: 'In 1412, Parakramabahu VI established Kotte as his capital city' and the kingdom lasts to 27 May 1597. Fix: One dossier per state, settled with sa-04-a: end ceylon in 1412 with successor kingdom-of-kotte (its 1450-1506 events move here and its 1506 dissolve to portuguese-ceylon goes), or start this dossier in 1507 as ceylon's successor. The first is closer to the page (ceylon's own /ledger/17 says the Kotte page keeps the kingdom to 1597).
- `/keyframe_review/4`: BLOCKING. The 1521-1563 shape resolves to one H3 cell (about 250 km2): Colombo, Gampaha and Kalutara minus the 40 km Sitawaka circle minus Kalutara; the capital Kotte (1529-1564) lies outside it. Evidence: Gazetteer resolve; Kingdom_of_Kotte: the 1521 division created 'Kotte, Sitawaka, and the Principality of Raigama', and Kotte survived to 1597. Fix: Redraw after the Sitawaka radius fix (km 25): Colombo and Gampaha minus the Sitawaka circle, plus whatever coast a page gives Kotte; re-run the resolver.
- `/identity/capitals/0`: Capital list starts in 1415 while the state starts in 1412. Evidence: Kingdom_of_Kotte: 'In 1412, Parakramabahu VI established Kotte as his capital city' (also 1415). Fix: Start the first capital in 1412.

Thin (for a gap-filler):
- `/ledger/6, /keyframe_review/3`: 1469-1520 Kotte is drawn as three districts (3,500 km2) after a confidence-1 loss of the rest of the island to 'nobody', smaller than its 1521 break-away Sitawaka; the extent is page-silent. Try: https://en.wikipedia.org/wiki/Parakramabahu_VIII
- `/ledger/4`: Jaffna lost in 1467 at confidence 1 (the Kotte page gives no year; jaffna-kingdom has 1467 at confidence 3) Try: https://en.wikipedia.org/wiki/Jaffna_Kingdom

Spot checks: `/ledger/2` Kingdom_of_Kotte: confirmed ('In 1450 ... unifying the entire island under his rule'); `/ledger/5` Kingdom_of_Kotte: confirmed (rebellion 'against the Kotte Kingdom in 1469'); `/ledger/13` Kingdom_of_Kotte: confirmed ('after the downfall of Sitawaka in 1594, these areas were re-annexed'); `/ledger/14` Kingdom_of_Kotte: confirmed (infobox 'Disestablishment: 27 May 1597')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| gujarat-sultanate 1394 found (tughlaq-dynasty) | tughlaq-dynasty 1394 loss | matched |  |
| gujarat-sultanate 1407 occupation_start (malwa-sultanate) | malwa-sultanate 1407 occupation_start | matched | 1407-1409 pair matched |
| gujarat-sultanate 1437 vassal_start (khandesh-sultanate) | - | missing | khandesh-sultanate has no vassal events (finding on Khandesh) |
| gujarat-sultanate 1518 vassal_start (malwa-sultanate) | - | missing | malwa-sultanate has no 1518-1531 vassal pair (finding on Malwa) |
| gujarat-sultanate 1531 gain (malwa-sultanate) | malwa-sultanate 1531 loss | matched |  |
| gujarat-sultanate 1534 loss (portuguese-empire) | portuguese-empire 1534 gain | matched | Bassein and Bombay; Daman: Gujarat 1534, portuguese-empire /ledger/18 1539 (mismatch for Daman, route to am-06) |
| gujarat-sultanate 1534 loss (portuguese-empire) | portuguese-empire 1535 gain | matched | Diu, within a year (Gujarat confidence 1) |
| gujarat-sultanate 1535 occupation_start (mughal-empire) | mughal-empire 1535 occupation_start | mismatch | years match; land differs: Gujarat names mainland Gujarat and Malwa, mughal-empire /ledger/4 names the forts Mandu and Champaner |
| gujarat-sultanate 1537 loss (malwa-sultanate) | malwa-sultanate 1537 gain | mismatch | Gujarat loses all Malwa; Malwa gains only Mandu/120 (finding on Gujarat) |
| gujarat-sultanate 1573 dissolve (mughal-empire) | mughal-empire 1573 gain | matched | mughal-empire has month 9 |
| gujarat-sultanate 1431 gain (bahmani-sultanate) | - | exception | bahmani-sultanate (sa-04-c) not written yet |
| gujarat-sultanate 1470 gain (chudasama-dynasty) | - | exception | listed in the author's counterparts_needing_dossiers |
| malwa-sultanate 1401 found (tughlaq-dynasty) | - | missing | tughlaq-dynasty has no 1401 loss of Malwa (its 1352 loss to nobody covers Madhya Pradesh); route to the tughlaq owner |
| malwa-sultanate 1457 gain (kingdom-of-mewar) | kingdom-of-mewar 1457 loss | matched | Mandalgarh |
| malwa-sultanate 1542 loss (sur-empire) | - | exception | sur-empire (sa-05-b) not written yet |
| malwa-sultanate 1562 dissolve (mughal-empire) | mughal-empire 1561 gain | matched | within a year (mughal contest 1560-1561 vs Malwa 1561-1562) |
| kingdom-of-mewar 1468 gain (malwa-sultanate) | - | missing | Malwa keeps Gagron to 1530 (finding on Mewar) |
| kingdom-of-mewar 1519 gain (malwa-sultanate) | malwa-sultanate 1519 contest_start | mismatch | gain vs contest; 46,000 km2 drawn by both 1519-1527 |
| kingdom-of-mewar 1528 loss (mughal-empire) | - | missing | mughal-empire has no 1528 gain; the page has Chanderi only (finding) |
| kingdom-of-mewar 1326 found (tughlaq-dynasty) | tughlaq-dynasty 1336 loss | mismatch | 10 years apart |
| kingdom-of-mewar 1568 loss (mughal-empire) | mughal-empire 1568 gain | matched | Chittor and the eastern belt |
| kingdom-of-mewar 1576 occupation_start (mughal-empire) | - | missing | mughal-empire has no 1576-1585 occupation or the 1615 return; route to sa-05-a |
| kingdom-of-marwar 1438 loss (missing) (kingdom-of-mewar) | - | missing | neither dossier has Mewar's hold on Mandore 1438-1453 (finding on Marwar) |
| kingdom-of-marwar 1544 occupation_start (sur-empire) | - | exception | sur-empire (sa-05-b) not written yet |
| kingdom-of-marwar 1557 loss (mughal-empire) | - | mismatch | mughal-empire models 1562-1583 as a contest (/ledger/22, /ledger/38) with no gain of Jodhpur in 1564 and no 1583 vassalage; Marwar's 1557 loss is contradicted by its page (finding) |
| kingdom-of-marwar 1583 gain (mughal-empire) | mughal-empire 1583 contest_end | mismatch | type differs; the vassal relation is on neither side |
| kingdom-of-marwar 1679 loss (mughal-empire) | - | missing | mughal-empire has no 1679-1710 Marwar events; route to sa-05-a |
| kingdom-of-marwar 1542 gain (bikaner) | - | exception | listed in counterparts_needing_dossiers |
| gajapati-kingdom 1434 found (eastern-ganga-kingdom) | eastern-ganga-kingdom 1434 dissolve | mismatch | eastern-ganga names its successor 'suryavamsha-dynasty'; should be gajapati-kingdom (sa-03) |
| gajapati-kingdom 1448 gain (reddi-kingdom) | reddi-kingdom 1448 dissolve | matched |  |
| gajapati-kingdom 1531 loss (golconda-sultanate) | - | missing | golconda-sultanate (sa-04-d) has no 1531 gain (Kondapalli, 20 March 1531) |
| gajapati-kingdom 1453 gain (vijayanagara-empire) | - | exception | vijayanagara-empire (sa-04-c) not written yet; also 1460, 1472, 1476, 1514, 1516 |
| gajapati-kingdom 1447 gain (sultanate-of-bengal) | - | exception | sultanate-of-bengal (sa-04-c) not written yet |
| reddi-kingdom 1325 found (kakatiya-dynasty) | - | exception | kakatiya-dynasty ends 1323 to tughlaq-dynasty and 'musunuri-nayakas' (a typo for musunuri-nayaks); no mirror expected for a found two years later, but the successor slug should be fixed by sa-03 |
| reddi-kingdom 1424 loss (vijayanagara-empire) | - | exception | not written yet |
| musunuri-nayaks 1336 gain (tughlaq-dynasty) | tughlaq-dynasty 1336 loss | matched | Warangal |
| musunuri-nayaks 1368 dissolve (recherla-nayaks) | recherla-nayaks 1368 found | mismatch | years match; the coastal circles go to no one (finding on Musunuri) |
| madurai-sultanate 1335 found (tughlaq-dynasty) | tughlaq-dynasty 1335 loss | matched |  |
| madurai-sultanate 1343 war (hoysala-kingdom) | hoysala-kingdom 1342 contest_start | exception | hoysala-kingdom names the counterpart 'Madurai Sultanate' (a name) instead of the slug; Madurai records the war with no land change |
| khandesh-sultanate 1382 found (tughlaq-dynasty) | - | missing | tughlaq-dynasty has no 1382 loss of Khandesh; route to the tughlaq owner |
| khandesh-sultanate 1599 occupation_start (mughal-empire) | - | missing | mughal-empire has only the 1601 gain (/ledger/53); the 1599-1601 occupation is not mirrored |
| khandesh-sultanate 1601 dissolve (mughal-empire) | mughal-empire 1601 gain | matched |  |
| ahom-kingdom 1639 gain (mughal-empire) | - | missing | mughal-empire carries none of the Ahom wars (1639, 1658, 1662-1663, 1667, 1679, 1682); route to sa-05-a |
| ahom-kingdom 1822 occupation_start (konbaung-dynasty) | konbaung-dynasty 1817 gain | mismatch | konbaung /ledger/44 gains Assam in 1817 (the Burmese left in April 1817); Konbaung's row ends 1819 |
| kingdom-of-bhutan 1790 gain (ahom-kingdom) | - | missing | the Ahom ledger has no loss of the Duars |
| ahom-kingdom 1512 gain (chutia-kingdom) | - | exception | listed in counterparts_needing_dossiers (also kachari, matak, moamoria) |
| kingdom-of-kandy 1469 found (kingdom-of-kotte) | kingdom-of-kotte 1469 loss | matched | ceylon /ledger/16 also loses Kandy in 1469 to the name 'Senasammata Vikramabahu (Kandy)': part of the Kotte/ceylon duplication |
| kingdom-of-kandy 1581 loss (kingdom-of-sitawaka) | kingdom-of-sitawaka 1581 gain | matched |  |
| kingdom-of-kandy 1592 gain (kingdom-of-sitawaka) | kingdom-of-sitawaka 1593 loss | matched | within a year; 24,800 km2 double-drawn in 1592 (finding on Kandy) |
| kingdom-of-kandy 1665 loss (dutch-ceylon) | - | exception | dutch-ceylon, portuguese-ceylon, british-ceylon (sa-06) not written yet |
| kingdom-of-sitawaka 1521 found (kingdom-of-kotte) | kingdom-of-kotte 1521 loss | matched |  |
| kingdom-of-sitawaka 1564 gain (kingdom-of-kotte) | kingdom-of-kotte 1564 loss | matched |  |
| kingdom-of-sitawaka 1594 loss (kingdom-of-kotte) | kingdom-of-kotte 1594 gain | matched |  |
| kingdom-of-sitawaka 1538 gain (principality-of-raigama) | - | exception | listed in counterparts_needing_dossiers |
| kingdom-of-kotte 1412 found (ceylon) | ceylon 1412 rename | mismatch | ceylon renames itself to Kotte in 1412 and continues to 1506: the same state in two dossiers (blocking finding on Kotte) |
| kingdom-of-kotte 1450 gain (jaffna-kingdom) | jaffna-kingdom 1450 loss | mismatch | jaffna-kingdom names ceylon as counterpart, not kingdom-of-kotte; same for 1467 |
| langah-sultanate 1445 found (sayyid-dynasty) | - | exception | sayyid-dynasty (sa-04-b) not written yet; the page says the inhabitants chose Shaikh Yousaf Qureshi in 1438 |
| langah-sultanate 1528 dissolve (arghun-dynasty) | - | exception | listed in counterparts_needing_dossiers |

## Overlaps between dossiers of this batch (gazetteer resolve)

- reddi-kingdom 1336-1367 x musunuri-nayaks: 124 cells (about 31,000 km2); reddi x recherla-nayaks 1368-1434: 37-47 cells (9,000-12,000 km2).
- malwa-sultanate 1457-1530 x kingdom-of-mewar 1519-1527: 183 cells (46,000 km2); 1468-1530: 52 cells (Gagron, 13,000 km2); 1401-1530: 26-31 cells (the gazetteer regions Malwa and Mewar overlap).
- kingdom-of-mewar 1528-1567 x kingdom-of-marwar 1534-1563: 34-67 cells (8,600-17,000 km2: Ajmer, Sirohi/Jalore, Pali); 1583-1949: 12-13 cells (gazetteer regions).
- gujarat-sultanate 1531-1536 (Malwa) x kingdom-of-mewar 1528-1567: 53 cells (Gagron, Ranthambore and the Malwa region).
- malwa-sultanate 1537-1541 (Mandu 120 km) x khandesh-sultanate: 28 cells (7,000 km2).
- kingdom-of-kandy 1592 x kingdom-of-sitawaka 1581-1592: 98 cells in 1592 (a one-year date disagreement).
- kingdom-of-kotte 1521-1563 resolves to 1 cell (the Sitawaka 40 km circle covers Kotte and Colombo).

## Gazetteer names needed
Champaner (gujarat-sultanate), Junagadh (gujarat-sultanate), Idar (gujarat-sultanate), Thane (gujarat-sultanate), Dwarka (gujarat-sultanate), Raisen (gujarat-sultanate), Vasai (gujarat-sultanate), Dhar (gujarat-sultanate), Kherla (malwa-sultanate), Gagron (malwa-sultanate), Mandalgarh (malwa-sultanate), Nagaon (ahom-kingdom), Sirohi (kingdom-of-mewar), Ranthambore (kingdom-of-mewar), Nagaur (kingdom-of-marwar), Jalore (kingdom-of-marwar), Pokhran (kingdom-of-marwar), Merta (kingdom-of-marwar), Bhadrajun (kingdom-of-marwar), Phalodi (kingdom-of-marwar), Barmer (kingdom-of-marwar), Hanwella (kingdom-of-kandy), Wattala (kingdom-of-sitawaka).

## Problems and routing
- No tool failures; every page opened. Other agents wrote tughlaq-dynasty, mughal-empire and jaffna-kingdom during this review (about 23:30-23:50); their ledgers were read for the cross-checks.
- Verdict 'fix' here means the reviewer applied what is marked applied: true; malwa-sultanate has only applied: false items, all non-blocking cross-dossier edits for the author. Blocking findings carry blocking: true.
- Convention question for the orchestrator: the author put vassal events only in the suzerain's ledger (the Tang example's practice); the reviewer brief (rule 3) and the sa-04-d review require the vassal's ledger to carry them. Affects Malwa, Khandesh, Mewar (1615, 1818) and Marwar (1583, 1818).
- Cross-group identity conflict: ceylon (sa-04-a, merged 2026-10-19) and kingdom-of-kotte (this batch) both draw the Kotte kingdom 1412-1506; one of the two groups must give way (recommended: ceylon ends 1412 with successor kingdom-of-kotte).
- Gazetteer: the regions Malwa and Mewar overlap by about 26 cells (6,600 km2); the regions Marwar and Mewar by about 12 cells (3,000 km2).
- Routing for other owners: konbaung-dynasty 1817 gain of Assam (Burmese left April 1817); kingdom-of-bhutan 1790 Duars gain with no Ahom page; golconda-sultanate lacks the 1531 Kondapalli gain; portuguese-empire Daman 1539 against the 1534 treaty; eastern-ganga-kingdom successor slug 'suryavamsha-dynasty'; kakatiya-dynasty successor slug 'musunuri-nayakas'; hoysala-kingdom counterpart 'Madurai Sultanate' (name, not slug); tughlaq-dynasty lacks the 1382 Khandesh and 1401 Malwa losses and has Mewar 1336 against 1326; mughal-empire lacks the Ahom wars, the Mewar occupation 1576-1585 and return 1615, the Khandesh occupation 1599-1601 and Marwar 1679-1710.
