# Review of batch se-01-e (Phase B, 2026-10-19)

Dossiers: shan-states, kingdom-of-pinya, sagaing-kingdom, ayutthaya-kingdom. All four validate with --resolve (0 errors, 0 warnings) before and after the reviewer's edits. Neighbour dossiers read: khmer-empire, post-angkor-cambodia, lavo-kingdom, sukhothai-kingdom, lan-na-kingdom, hanthawaddy-kingdom, myinsaing-kingdom, pagan-kingdom (the other Context polities have no file yet).

Verdicts: shan-states fix (fixed by the reviewer), kingdom-of-pinya pass, sagaing-kingdom fix (fixed by the reviewer), ayutthaya-kingdom fail (back to the author: missing Khmer, Cambodian and Sawankhalok events and an unexplained Patani drop).

## shan-states: fix

Area: infobox none km2 (year n/a), Cliopatria 387847 km2, ratio n/a, acknowledged True. Shan States infobox gives no area (the dossier says so); max Cliopatria shape 1529 is 387,847 km2.

Findings:
- `/ledger/3` (applied by reviewer): contest_start dated 1436 at confidence 3; the page body gives 1437 for the first ground taken and 1438 for the first Ming campaign. Evidence: Mong Mao page: 'Si Renfa continued to expand, invading Nandian in 1437'; 'The first campaign was sent in 1438'. 1436 appears only in the title of a cited source ('The Luchuan-Pingmian Campaigns (1436-1449)'); the quoted 'prompted the Ming to prepare a campaign' is not on the page (it says the Ming 'prepared a campaign'). Fix: year 1437; note quotes the 1437 Nandian sentence. Applied by the reviewer; war W2 keeps 1436-1449 (the cited source's span).
- `/keyframe_review/15` (applied by reviewer): shan-states_1547 marked ok through 1555 although the ledger loses Ava's land (about 83,000 km2, the drop to the 1556 shape) on 22 January 1555. Evidence: Kingdom of Ava: 'In January 1555, King Bayinnaung of the Taungoo dynasty conquered Ava'; infobox 'Toungoo conquest: 22 January 1555'. A large ledger event inside one shape's span needs the keyframe marked adjust. Fix: verdict adjust, correction = the 1547 outline unchanged, holding 1547 to January 1555; source Kingdom_of_Ava. Applied by the reviewer.
- `/ledger/8` (applied by reviewer): The note quotes 'Prome was taken in 1533', which is not on the Shan States page (same quote in /keyframe_review/11 and /keyframe_review/12). Evidence: Shan States page: 'The enlarged Confederation extended its authority down to Prome (Pyay) in 1533 by defeating their erstwhile ally Prome Kingdom.' The event and year stand. Fix: Quote replaced with the page's sentence in the three places. Applied by the reviewer.

Gaps for a gap-filler:
- `/ledger/9`: 1542 loss of Prome to Toungoo is confidence 1 (sidebar 'Prome kingdom 1482-1542' only); the siege and fall of Prome in 1542 and the Confederation's relief armies need a page. Try https://en.wikipedia.org/wiki/Toungoo%E2%80%93Ava_War_(1538%E2%80%931545)
- `/wars`: No war or event for Mong Mao's fighting with the Yuan in Yunnan (Si Kefa, c. 1335-1350s; infobox 'Si Kefa becomes ruler of Mong Mao: c. 1335') although the 1294-1384 outline holds 106 Yunnan cells. Try https://en.wikipedia.org/wiki/Mong_Mao
- `/keyframe_review/16`: 1557-1563 the Shan states are Toungoo vassals (Bayinnaung page tables, Mohnyin 6 March 1557 ...); the vassal_start events belong to first-toungoo-empire, which has no dossier yet. Try https://en.wikipedia.org/wiki/Bayinnaung

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/Shan_States: confirmed ('Mong Mao was finally defeated in 1444'; royal family moved to Mong Yang)
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_Ava: confirmed (verbatim sentence; infobox 'Start of Shan period: 14 March 1527')
- `/ledger/8` https://en.wikipedia.org/wiki/Shan_States: confirmed in substance (1533), quote not verbatim; corrected
- `/ledger/11` https://en.wikipedia.org/wiki/Kingdom_of_Ava: confirmed (infobox 'Toungoo conquest: 22 January 1555')
- `/ledger/13` https://en.wikipedia.org/wiki/Bayinnaung: confirmed ('By March 1557 ... cis-Salween Shan states'; Mohnyin 6 March, Mogaung 11 March 1557)
- `/ledger/14` https://en.wikipedia.org/wiki/Bayinnaung: confirmed (Kengtung 16 December 1562; nominal suzerainty over the Chinese Shan states after the 1563 Taping campaign)
- `/ledger/1` https://en.wikipedia.org/wiki/Mong_Mao: confirmed (Jingdong 'the following year' after August 1384; 1387 expedition; surrender 1388)
- `/ledger/3` https://en.wikipedia.org/wiki/Mong_Mao: mis-dated (1436; page 1437/1438); fixed

## kingdom-of-pinya: pass

Area: infobox 140000 km2 (year 1313), Cliopatria 193597 km2, ratio 1.38, acknowledged True. No infobox area; the body's 'at least 140,000 km2' at the founding; KF0 quotes the ratio 1.38. 1326: 95,056 vs 'about 100,000' (0.95).

Gaps for a gap-filler:
- `/ledger/5`: Extent of the 1358 Toungoo secession is an 80 km radius sized to the page's 100,000 -> 80,000 km2 (author's reading, confidence 2); a Toungoo page could bound it. Try https://en.wikipedia.org/wiki/Taungoo

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Pinya_Kingdom: confirmed ('On 7 February 1313, Thihathu ... was crowned king'; new capital at Pinya; 'at least 140,000 km2')
- `/ledger/4` https://en.wikipedia.org/wiki/Pinya_Kingdom: confirmed ('formally seceded in 1325 after Thihathu's death'; claim about 100,000 km2 after 1325)
- `/ledger/5` https://en.wikipedia.org/wiki/Pinya_Kingdom: confirmed ('Theingaba of Toungoo outright revolted during the Maw Shan raid of 1358-59'; about 80,000 km2 after 1358)
- `/ledger/6` https://en.wikipedia.org/wiki/Pinya_Kingdom: confirmed ('He took Pinya in September 1364'; Maw sacked Sagaing April 1364 and Pinya in May)
- `/wars/1` https://en.wikipedia.org/wiki/Pinya_Kingdom: confirmed ('Ramanya attacked Prome in 1330'; 'Arakan raided Thayet in 1333-34'; Toungoo and Prome 'practically independent')

Tried and could not break: the founding date, the 1325 and 1358 area figures, the September 1364 fall, the matched 1364 loss/gain with Sagaing, the Myinsaing hand-over of 7 February 1313, contiguous rulers, the 1.38 area ratio (acknowledged). The capital point is the gazetteer's Ava point, flagged by the author as approximate.

## sagaing-kingdom: fix

Area: infobox none km2 (year n/a), Cliopatria 98185 km2, ratio n/a, acknowledged True. No infobox area. The page's effective control 'no more than half today's Sagaing Region' (about 47,000 km2) is about half the 98,185 km2 outline; KF1 says so and keeps the outline as the claim.

Findings:
- `/keyframe_review/3/note` (applied by reviewer): The union's areas are given as 'about 66,000 + 87,000 km2', which matches neither shape. Evidence: shapes.csv: sagaing-kingdom_1326/1363 = 98,185 km2 for the 345 cells; kingdom-of-pinya_1363 = 95,056 km2 for 324 cells, 262 of which remain without Toungoo (about 76,900 km2 per the Pinya dossier's KF2 note). Fix: about 98,000 + 77,000 km2 with the shapes.csv figures. Applied by the reviewer.

Gaps for a gap-filler:
- `/wars/1`: The 'Sagaing-Pinya hostilities and the 1351 truce' end year: the page dates the truce only to Tarabya II's reign (1349-1352), not to 1351; harmless, no zone. Try https://en.wikipedia.org/wiki/Sagaing_Kingdom

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sagaing_Kingdom: confirmed ('In 1315, the teenage prince walked out of the Pinya Palace, never to return'; footnotes 26 March 1316 and 684 ME)
- `/ledger/2` https://en.wikipedia.org/wiki/Sagaing_Kingdom: confirmed ('fought for autonomy ... in 1315-17'; 'breather in 1317 when Toungoo and Taungdwin revolted')
- `/ledger/3` https://en.wikipedia.org/wiki/Sagaing_Kingdom: confirmed ('In September 1364, Thado Minbya seized Pinya, and claimed himself king of Sagaing and Pinya')
- `/ledger/4` https://en.wikipedia.org/wiki/Sagaing_Kingdom: confirmed ('In 1365, Thado Minbya founded the kingdom of Ava'; inscription of 8 July 1365)
- `/keyframe_review/1` https://en.wikipedia.org/wiki/Sagaing_Kingdom: confirmed ('claimed all the way to the border of Manipur'; effective control 'no more than half today's Sagaing Region'; Tagaung 225 km)

## ayutthaya-kingdom: fail

Area: infobox 400000 km2 (year n/a), Cliopatria 450375 km2, ratio 1.13, acknowledged True. Infobox 'Total: 400,000 km2' without a year; the shapes from 1450 run 382,305-450,375 km2 (0.96-1.13), quoted in the keyframe notes. The 1352-1374 shape (7,488 km2) is corrected upward (Suphanburi, Phetchaburi).

Findings:
- `/ledger (1353-1357, missing)` (for the author): No occupation of Angkor in 1353-1357 although khmer-empire records occupation_start 1353 / occupation_end 1357 with counterpart ayutthaya-kingdom; the occupier must record the same event (schema, occupation_*), and war /wars/0 has empty zones. Evidence: khmer-empire /ledger/29-30 (Khmer Empire page: 'Uthong besieged Angkor' in 1352, captured 'the next year', Siamese princes installed until Suryavamsa Rajadhiraja retook it in 1357). Ayutthaya page: Ramathibodi's forces 'captured Nakhon Thom (Yasodharapura), taking captives and goods rather than annexing the city' (undated). Fix: Add occupation_start 1353 and occupation_end 1357, counterpart khmer-empire, region Angkor/Yasodharapura (place Angkor with a radius), source the Khmer Empire page (add to sources); give /wars/0 that zone and run it to 1357; or say in notes why the Khmer page's occupation is rejected.
- `/wars and /ledger (1393-1394, missing)` (for the author): Ramesuan's siege and capture of Angkor in 1393-1394 is missing (no war, no contest); khmer-empire carries contest_start 1393 / contest_end 1394 with ayutthaya-kingdom. Evidence: khmer-empire /ledger/33-34 ('1393: Ramesuan of Ayutthaya besieges Angkor'; '1394: Angkor is captured by Ayutthaya'). Fix: Add a war 'Siamese capture of Angkor (1393-1394)' with a zone round Angkor and the paired contest_start 1393 / contest_end 1394 (or an occupation if the page gives a span), source the Khmer Empire page.
- `/ledger (1594-1618, missing)` (for the author): Ayutthaya's suzerainty over Cambodia after the 1594 sack of Longvek is missing: no vassal_start/vassal_end for post-angkor-cambodia, no war; the suzerain carries vassal events (schema). Evidence: Ayutthaya page: Songtham 'lost suzerainty over Lan Na, Cambodia, and Tavoy'; it also 'fought the Nguyen Lords ... for control of Cambodia from around 1715'. post-angkor-cambodia /ledger/2-3 (Post-Angkor period page): 'In 1594, Longvek was successfully captured and sacked by Siamese forces'; in 1618 Chey Chettha II 'stopped sending tribute to Ayutthaya and reasserted Cambodian independence'. Fix: Add vassal_start 1594 / vassal_end 1618, counterpart post-angkor-cambodia, region {cliopatria: Khmer Empire, year: 1594}, sources Post-Angkor period and the Siamese-Cambodian war page; add the war (1591-1594) and, if a page supports it, the c. 1715 contest with the Nguyen lords over Cambodia.
- `/ledger/11 and /ledger/14` (for the author): Sawankhalok is drawn as all of Sukhothai province and is lost to Lan Na twice (1451, 1459) with no gain between or after, so by the ledger Sukhothai province is Lan Na's from 1459 while /ledger/21 loses it again to Toungoo in 1563. Evidence: Ayutthaya-Lan Na War page: 'In 1451, Sawankhalok broke away from Ayutthaya and joined Lan Na'; 'In 1459, Lan Na captured Sawankhalok, which had in the meantime rejoined Ayutthaya' (undated return; no later recapture on the page). KF7 says no Cliopatria shape shows these moves. Fix: Narrow both regions to Sawankhalok / Si Satchanalai (a place with a ~30 km radius, or a polygon; Sawankhalok is in gazetteer_names_needed); add a confidence-1 gain from lan-na-kingdom between 1452 and 1458 for the undated return; add or explain the regain after 1459 (at latest by 1563, when /ledger/21 has Sawankhalok Ayutthaya's).
- `/ledger/20 and /keyframe_review/14` (for the author): The Patani region is gained as direct land in 1512 (confidence 1) and leaves the outline in 1572 (new keyframe 1572, then the 1588 shape) with no loss or vassal_end: an unexplained keyframe change. Evidence: shapes.csv: ayutthaya-kingdom_1564 bbox south 5.62 N, ayutthaya-kingdom_1588 south 6.26 N; KF14/KF16 notes: the Patani cells drop out 'because Cliopatria's Patani row begins in 1572'. Patani Kingdom page (as quoted in /ledger/20): Patani 'founded c. 1400', attacked Ayutthaya in 1563, acknowledged Siamese authority in 1584. Fix: Either make /ledger/20 a vassal_start patani-kingdom 1512 with a vassal_end at 1563 (Patani's attack), drawing the strip as a tint, or add a confidence-1 loss to patani-kingdom in 1563 or 1572 explaining the drop.
- `/ledger (1375, lavo-kingdom)` (for the author): Lavo records a 1375 loss to Ayutthaya (lavo-kingdom /ledger/12, confidence 1), but Ayutthaya's 1375 gains name only khmer-empire and nobody, although KF2 counts 13 of the 909 new cells inside Lavo's outline. Evidence: lavo-kingdom /ledger/12; ayutthaya KF2 note '212 in the Khmer Empire's, 13 in Lavo's'. Fix: Add a confidence-1 gain lavo-kingdom 1375 for the 13 cells ({intersect: [Ayutthaya 1375, Lavo 1374]}), or agree with lavo-kingdom's author that the cells were Ayutthaya's from 1351.
- `/keyframe_review/4` (for the author): Keyframe ayutthaya-kingdom_1388 (new, 1388-1394) sits after ayutthaya-kingdom_1395; keyframe_review should be in shape (year) order. Evidence: Order of /keyframe_review: 1351, 1352, 1375, 1395, 1388, 1438, ... Fix: Move the 1388 entry before the 1395 entry.
- `/ledger/34/region` (applied by reviewer): The 1618 loss included Bago and Yangon, which the dossier's own corrections (KF17, KF18) remove from Ayutthaya's land as never held. Evidence: KF17/KF18 corrections minus Bago and Yangon; 1593-1600 war page: Pegu besieged and abandoned, never held; the region's own text said 'which Naresuan besieged but did not take'. Fix: Region reduced to the Mon and Kayin union; note adjusted. Applied by the reviewer.
- `/ledger/5/note` (applied by reviewer): Quote 'Ramesuan recovers Ayutthaya from Thong Lan; Lavo is fully incorporated' is not on the page. Evidence: Ayutthaya Kingdom page: he 'recovered it from Thong Lan in 1388'; 'Lavo was not fully incorporated into Ayutthaya's political order until 1388'. Event and year confirmed. Fix: Quote replaced with the page's words. Applied by the reviewer.
- `/ledger/30/note` (applied by reviewer): Quote 'regained Lan Na and Tanintharyi region' (as the war infobox) is not on the page. Evidence: 1593-1600 war page: Naresuan sought to 'regain some territories including Lan Na and Tanintharyi region'; infobox result 'Inconclusive'. Ayutthaya page: in 1614 Burma 'invaded Lan Na, then a vassal of Ayutthaya', which supports the vassalage at confidence 2. Fix: Note quotes both pages' actual words. Applied by the reviewer.

Gaps for a gap-filler:
- `/ledger/2`: 1375 gain of the Khmer western strip, confidence 1, page silent. Try https://en.wikipedia.org/wiki/Ramathibodi_I
- `/ledger/3`: 1375 gain of the Khorat plateau, peninsula and Tenasserim (the jump from 7,488 to 288,685 km2), confidence 1. Try https://en.wikipedia.org/wiki/Borommarachathirat_I
- `/ledger/15`: 1459 gain of Songkhla/Satun/Pattani from Kedah, confidence 1. Try https://en.wikipedia.org/wiki/Borommatrailokkanat
- `/ledger/20`: 1512 Patani region, confidence 1 (see fixes). Try https://en.wikipedia.org/wiki/Patani_Kingdom
- `/ledger/34`: Date of the loss of the Mon provinces (1613 with Anaukpetlun's restoration?), confidence 1. Try https://en.wikipedia.org/wiki/Anaukpetlun
- `/ledger/41`: Lopburi move 'early 1680s', placeholder 1680, confidence 1. Try https://en.wikipedia.org/wiki/Narai
- `/wars/1`: 1430s attack on Angkor 'installed a short-lived puppet ruler' (Ayutthaya page): possibly a brief vassal or occupation; no zone. Try https://en.wikipedia.org/wiki/Borommarachathirat_II

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/Ayutthaya_Kingdom: confirmed (1388), quote not verbatim; corrected
- `/ledger/7` https://en.wikipedia.org/wiki/Ayutthaya_Kingdom: confirmed ('The Suphannabhum line regained the throne under Intharacha in 1408')
- `/ledger/11` https://en.wikipedia.org/wiki/Ayutthaya-Lan_Na_War: confirmed ('In 1451, Sawankhalok broke away from Ayutthaya and joined Lan Na')
- `/ledger/14` https://en.wikipedia.org/wiki/Ayutthaya-Lan_Na_War: confirmed (1459; 'had in the meantime rejoined Ayutthaya', undated)
- `/ledger/16` https://en.wikipedia.org/wiki/Ayutthaya-Lan_Na_War: confirmed ('A year later, Ayutthaya reconquered Phrae Province')
- `/ledger/21` https://en.wikipedia.org/wiki/Bayinnaung: confirmed (Kamphaeng Phet taken 4 December 1563)
- `/ledger/22` https://en.wikipedia.org/wiki/Bayinnaung: confirmed (surrender 18 February 1564); the western cession is not on the page, honestly at confidence 2
- `/ledger/27` https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1593%E2%80%931600): confirmed (Tenasserim 15 days, Tavoy 20 days, 'Early in 1593'; Mergui)
- `/ledger/28` https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1593%E2%80%931600): confirmed (1594; 'The Mon provinces then became subject to Siam')
- `/ledger/29` https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1593%E2%80%931600): confirmed ('In January 1595, Naresuan led an army of 120,000 men')
- `/ledger/32` https://en.wikipedia.org/wiki/Ayutthaya_Kingdom: confirmed (1613 'took Tavoy')
- `/ledger/33` https://en.wikipedia.org/wiki/Ayutthaya_Kingdom: confirmed (1618 treaty: 'Burma gained control of Lan Na, while Ayutthaya retained southern Tanintharyi, south of Tavoy')
- `/ledger/47` https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1765%E2%80%931767): confirmed ('Siam lost Tenaserim to Burma for perpetuity in 1765'; Mergui and Tenasserim taken 11 January 1765)
- `/ledger/50` https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1765%E2%80%931767): confirmed (fell 7 April 1767; siege February 1766 - April 1767)

## Cross-dossier matrix

- pagan-kingdom 1287 loss -> shan-states: mirror shan-states 1287 found; **matched**. Shan found 1287 with predecessor pagan-kingdom; both c1/c2.
- shan-states 1444 loss -> ming-dynasty: mirror none; **exception**. ming-dynasty (group ea-07) has no dossier yet; also contests 1385-1388 and 1437-1449.
- shan-states 1527 gain -> ava-kingdom: mirror none; **exception**. ava-kingdom (another se-01 part) not written yet; it should end its 1527-1528 shapes or mark them Shan.
- shan-states 1533 gain -> prome-kingdom: mirror none; **exception**. prome-kingdom (se-01) not written yet; Cliopatria keeps Prome to 1546.
- shan-states 1542 loss -> first-toungoo-empire: mirror none; **exception**. first-toungoo-empire (se-01) not written yet; Shan side is confidence 1.
- shan-states 1545 loss -> first-toungoo-empire: mirror none; **exception**. first-toungoo-empire not written yet.
- shan-states 1555 loss -> first-toungoo-empire: mirror none; **exception**. first-toungoo-empire not written yet; it should also carry vassal_start for the Shan states 1557-1563.
- kingdom-of-pinya 1313 found -> myinsaing-kingdom: mirror myinsaing-kingdom 1313 dissolve; **matched**. Myinsaing dissolve 7 February 1313, successor kingdom-of-pinya.
- kingdom-of-pinya 1317 vassal_start -> sagaing-kingdom: mirror sagaing-kingdom None None; **exception**. Schema: the suzerain carries vassal events; Sagaing has contest 1315-1317 and its own 1315-1325 keyframe.
- kingdom-of-pinya 1325 vassal_end -> sagaing-kingdom: mirror sagaing-kingdom None None; **exception**. As above.
- kingdom-of-pinya 1358 loss -> Toungoo: mirror none; **exception**. Toungoo listed in counterparts_needing_dossiers (toungoo-principality).
- kingdom-of-pinya 1364 loss -> sagaing-kingdom: mirror sagaing-kingdom 1364 gain; **matched**. Both September 1364, same region (Pinya 1363 less Toungoo).
- sagaing-kingdom 1365 dissolve -> ava-kingdom: mirror none; **exception**. ava-kingdom not written yet; it should start 1365 with both as predecessors (Cliopatria gap 1365-1374).
- lavo-kingdom 1351 loss -> ayutthaya-kingdom: mirror ayutthaya-kingdom 1351 found; **matched**. Ayutthaya found 1351 with counterpart lavo-kingdom.
- ayutthaya-kingdom 1375 gain -> khmer-empire: mirror khmer-empire 1375 loss; **matched**. Both confidence 1; khmer successor land = the 1375 western strip.
- lavo-kingdom 1375 loss -> ayutthaya-kingdom: mirror ayutthaya-kingdom None None; **missing**. Ayutthaya's 1375 gains name khmer-empire and nobody only; 13 Lavo cells per KF2. Both sides c1.
- ayutthaya-kingdom 1375 gain -> nobody: mirror none; **exception**. nobody; consistent with sukhothai-kingdom, which loses those cells c. 1300 and 1319.
- ayutthaya-kingdom 1378 vassal_start -> sukhothai-kingdom: mirror sukhothai-kingdom None None; **exception**. Suzerain carries the vassal span 1378-1438 (schema).
- ayutthaya-kingdom 1388 gain -> lavo-kingdom: mirror lavo-kingdom 1388 dissolve; **matched**. Lavo dissolve 1388, successor ayutthaya-kingdom.
- ayutthaya-kingdom 1438 gain -> sukhothai-kingdom: mirror sukhothai-kingdom 1438 loss; **matched**. Both c2; the Phitsanulok-core disagreement in the author's notes remains for the two authors.
- khmer-empire 1353 occupation_start -> ayutthaya-kingdom: mirror ayutthaya-kingdom None None; **missing**. Ayutthaya has no occupation 1353-1357 (fix routed to ayutthaya-kingdom).
- khmer-empire 1357 occupation_end -> ayutthaya-kingdom: mirror ayutthaya-kingdom None None; **missing**. As above.
- khmer-empire 1393 contest_start -> ayutthaya-kingdom: mirror ayutthaya-kingdom None None; **missing**. Ayutthaya has no 1393-1394 contest or war.
- post-angkor-cambodia 1594 vassal_start -> ayutthaya-kingdom: mirror none; **missing**. Neither dossier records Cambodia's tribute to Ayutthaya 1594-1618; the suzerain (ayutthaya-kingdom) should.
- ayutthaya-kingdom 1441 contest_start -> lan-na-kingdom: mirror lan-na-kingdom 1451 contest_start; **mismatch**. Ten years apart; the war infobox runs 1441-1474, so lan-na-kingdom should move its start to 1441.
- ayutthaya-kingdom 1451 loss -> lan-na-kingdom: mirror lan-na-kingdom None None; **missing**. lan-na-kingdom has only contest_start 1451, no gain of Sawankhalok.
- ayutthaya-kingdom 1452 occupation_start -> lan-na-kingdom: mirror lan-na-kingdom 1452 occupation_start; **matched**. Chiang Mai 1452, both sides.
- ayutthaya-kingdom 1459 loss -> lan-na-kingdom: mirror lan-na-kingdom None None; **missing**. No 1459 gain of Sawankhalok in lan-na-kingdom.
- ayutthaya-kingdom 1460 gain -> lan-na-kingdom: mirror lan-na-kingdom None None; **missing**. No 1460 loss of Phrae in lan-na-kingdom.
- ayutthaya-kingdom 1474 contest_end -> lan-na-kingdom: mirror lan-na-kingdom 1474 contest_end; **matched**. Both 1474.
- ayutthaya-kingdom 1459 gain -> sultanate-of-kedah: mirror none; **exception**. sultanate-of-kedah (group se-02) not written yet; c1.
- ayutthaya-kingdom 1512 gain -> patani-kingdom: mirror none; **exception**. patani-kingdom (se-02) not written yet, and its Cliopatria row starts only 1572; see the fix on the 1572 drop.
- ayutthaya-kingdom 1584 vassal_start -> patani-kingdom: mirror none; **exception**. se-02 not run; vassal_end 1688.
- ayutthaya-kingdom 1563 loss -> first-toungoo-empire: mirror none; **exception**. first-toungoo-empire not written; also 1564 loss, 1584/1593/1594 gains, 1613/1618 losses; it should carry Ayutthaya's vassalage 1564-1568 and 1569-1584.
- ayutthaya-kingdom 1600 vassal_start -> lan-na: mirror none; **exception**. lan-na (se-01, 1600-1761) not written; vassal_end 1618; occupation of Chiang Mai 1663 also awaits it.
- ayutthaya-kingdom 1760 loss -> konbaung-dynasty: mirror none; **exception**. konbaung-dynasty (se-01) not written; also 1765 loss.

## Problems

- No page failed to load. Fetches were via WebFetch's summariser; quotes were checked by asking for verbatim excerpts.
- The reviewer brief's rule 3 asks for a vassal_start mirror on the vassal's side, but the schema has the suzerain carry both vassal events; vassal events were treated as exceptions when only the suzerain records them (as in the se-01-b to se-01-d reviews).
- Many counterparts (ava-kingdom, prome-kingdom, first-toungoo-empire, lan-na, konbaung-dynasty, ming-dynasty, patani-kingdom, sultanate-of-kedah) have no dossier yet; their mirrors must be checked when those groups run.
- Reviewer edits applied in place and re-validated (0 errors, 0 warnings): shan-states /ledger/3, /keyframe_review/15, the Prome quote in /ledger/8 and /keyframe_review/11-12; sagaing-kingdom /keyframe_review/3 note; ayutthaya-kingdom /ledger/5 note, /ledger/30 note, /ledger/34 region and note.
