# Review of batch sa-04-b (Khalji, Tughlaq, Kashmir, Samma, Jaffna, Kampili)

Adversarial review, 2026-10-19/20. Mechanical checks: all six dossiers validate (0 errors). The 9 `--resolve` warnings are slugs of counterparts that do not have dossiers yet. Spot checks were made with WebFetch on the pages cited. Areas of corrected keyframes were computed with tools/gazetteer.py (cells x 252.9 km2). The fixes the reviewer applied are marked 'applied'. Everything else goes back to the author or to a gap-filler.

## Verdicts

- **tughlaq-dynasty**: fail
- **khalji-dynasty**: fix
- **kashmiri-sultanate**: thin
- **sind-samma-dynasty**: thin
- **jaffna-kingdom**: thin
- **kampili-kingdom**: thin

## tughlaq-dynasty: fail

Area: infobox 2800000 (1350); Cliopatria 1886333; ratio 0.67; corrected 1618000. The Tughlaq page has no area. The 1350 comparison is inside a factor of two. The 1352-1394 corrected outline (0.76 M km2) is 0.27 of the 1350 figure. The KF12 note acknowledges this, but its resolution is the Malwa finding.

Findings:
- `/keyframe_review/12, /keyframe_review/13, /keyframe_review/14, /keyframe_review/15, /keyframe_review/16, /ledger/19` [NOT applied] Malwa (611 cells, about 0.155 M km2) is dropped in 1352 as part of a confidence-1 loss to 'nobody' and stays out of every keyframe to 1414. But the malwa-sultanate dossier has Malwa held for the Tughlaqs until 1401. Malwa is nobody's land on the map for 49 years. Evidence: malwa-sultanate identity.predecessors: tughlaq-dynasty, 'Malwa, governed by Dilawar Khan for the Tughlaqs'. malwa-sultanate /ledger/0 (1401 found, counterpart tughlaq-dynasty): Dilawar Khan 'had ceased to pay tribute to Delhi after 1392' and 'in 1401, made Malwa an independent realm'. Resolver: 611 of 611 {region: Malwa} cells lie outside the KF12 correction. No page opened gives the 1352 loss (KF12 note: 'the rest is not [explained] by any page opened'; /ledger/19 note: 'Page silent'). The Delhi Sultanate infobox gives 2,800,000 km2 for 1350; the corrected 1347-1350 outline is 1.62 M km2 and the corrected 1352 outline 0.76 M km2 (ratio 0.27). The factor-of-3.6 drop is acknowledged, but the only 'resolution' is Cliopatria's shape, and a sourced neighbour contradicts it. The author's notes file says the opposite of the dossier: '[the dossier] keeps them and puts the Deccan, Bengal and Sind losses on page dates'. Fix: Add {"region": "Malwa"} to the corrections of KF12-KF15. Make KF16 (tughlaq-dynasty_1395, now ok) 'adjust' with Malwa added for 1395-1400. Cut Malwa out of the /ledger/19 region. Add a 1401 loss of Malwa to malwa-sultanate (source https://en.wikipedia.org/wiki/Malwa_Sultanate), with a note on the 1392 tribute stop. For the rest of the 1352 drop (Rajasthan with Ajmer, Bundelkhand, eastern Uttar Pradesh), either find a page (the Tughlaq page has 'The Rajput states also expelled the governor of Ajmer', undated) or keep it in /ledger/19 at confidence 1. Make the KF12 note and _notes/sa-04-b.md say the same thing.
- `/ledger/15; /keyframe_review/4, /keyframe_review/5, /keyframe_review/6` [NOT applied] The Tughlaq outline keeps Mewar until 1336, while kingdom-of-mewar is founded on the same land in 1326 with tughlaq-dynasty as counterpart. Both dossiers claim 1326-1335. Evidence: kingdom-of-mewar /ledger/0: 1326 found, counterpart tughlaq-dynasty, 'c. 1326: Hammir Singh began regaining Mewar'. Resolver: all 132 cells of kingdom-of-mewar_1326 lie inside tughlaq-dynasty_1327. The 1336 date is right: Muhammad bin Tughluq page, 'Rana Hammir Singh liberated the strategic Rajputana following the victory in Battle of Singoli in 1336'. Fix: Add contest_start 1326 and contest_end 1336 (counterpart kingdom-of-mewar, region Mewar, source Muhammad_bin_Tughluq) so that 1326-1336 is drawn as contested. The orchestrator should ask sa-03 to record the matching contest in kingdom-of-mewar or to move its found to 1336.
- `/keyframe_review/0 to /keyframe_review/11, /ledger/18` [NOT applied] Sind is Tughlaq land in 1320-1351 (inherited through the Khalji 1314 outline, and put back by the 1344 correction), while soomra-dynasty draws the same cells as Soomra land in 1202-1351. Also, sind-samma-dynasty takes Sind from soomra-dynasty, not from tughlaq-dynasty, so the 1351 loss has no mirror. Evidence: Resolver: soomra-dynasty_1202 (562 cells) shares 387 cells with tughlaq-dynasty_1320 and khalji-dynasty_1314, and 483 with tughlaq-dynasty_1344. sind-samma-dynasty /ledger/0: found 1351, counterpart soomra-dynasty. soomra-dynasty /ledger/1: dissolve 1351 to sind-samma-dynasty. Samma page: 'Mohammad bin Tughlaq made an expedition against Sindh in 1351 and died at Sondha'; 'Following this, the Sammas became independent'. Fix: Settle one owner per cell with the soomra-dynasty and sind-samma-dynasty authors. Either Delhi holds upper Sind (Multan, Bhakkar, Sehwan) and lower Sind is a Soomra/Samma vassal of Delhi (a vassal_start here, with the Soomra and Samma mirrors), or the Sind cells come out of the Khalji and Tughlaq corrections. Then make /ledger/18, sind-samma-dynasty /ledger/0 and soomra-dynasty /ledger/1 name the same parties.
- `/identity/rulers` [applied] Rulers were not contiguous: nobody was listed between Firuz Shah (to 1388) and Mahmud Shah (from 1394). Evidence: Tughlaq dynasty page, ruler table: Ghiyath-ud-din Tughluq Shah (Tughluq Khan) '1388–1389', Abu Bakr Shah '1389–1390', Muhammad Shah '1390–1394', Ala-ud-din Sikandar Shah '1394'. Fix: Inserted the four rulers with source Tughlaq_dynasty (done by the reviewer).
- `/identity/rulers/1, /identity/rulers/2, /identity/rulers/7, /identity/rulers/8` [applied] Four rulers cited no page. Evidence: Tughlaq dynasty ruler table: Muhammad 1325–1351, Feroze 1351–1388, Mahmud 1394–1412/1413. Delhi Sultanate page: Mahmud and Nusrat 'both called themselves Sultan from 1394 to 1397'. Fix: Added source Tughlaq_dynasty to Muhammad bin Tughluq, Firuz Shah and Mahmud Shah, and Delhi_Sultanate to Nusrat Shah (done by the reviewer).

Gaps for a gap-filler:
- `/ledger/7` 1326 gain of Tamil Nadu (Ma'bar) from pandya-empire is confidence 1; no page gives the year (try https://en.wikipedia.org/wiki/Madurai_Sultanate)
- `/ledger/22, /ledger/23` 1388 vassal_end of the Eastern Gangas and the Sammas: confidence 1 bridges to Firuz's death; eastern-ganga-kingdom ends its side in 1359 (try https://en.wikipedia.org/wiki/Eastern_Ganga_dynasty)
- `/ledger/24, /ledger/25` 1394 losses of Jaunpur and Gujarat: confidence 1 (the breakaways are undated on the Nasir-ud-Din page) (try https://en.wikipedia.org/wiki/Jaunpur_Sultanate)
- `/ledger/30` 1402 loss of the Punjab to the Timurids: confidence 1, Cliopatria's year (try https://en.wikipedia.org/wiki/Khizr_Khan)
- `/ledger/31` 1407 loss of the north-west and west to the Khokhars and Mewat: confidence 1, Cliopatria's year (try https://en.wikipedia.org/wiki/Daulat_Khan_Lodi)

Spot checks:
- `/ledger/3` Muhammad_bin_Tughluq: confirmed. 'In 1323, the future sultan successfully laid siege upon the Kakatiya capital in Warangal.'
- `/ledger/10` Muhammad_bin_Tughluq: confirmed. 'In 1330, he annexed Munger to his empire from Bengal.'
- `/ledger/11` Delhi_Sultanate: confirmed. 'In 1335, Jalaluddin Ahsan Khan, a Sayyid from Kaithal ... founded the Madurai Sultanate'
- `/ledger/13` Tughlaq_dynasty: confirmed. 'In 1336 Kapaya Nayak of the Musunuri Nayak defeated the Tughlaq army and reconquered Warangal'
- `/ledger/15` Muhammad_bin_Tughluq: confirmed. Singoli 1336
- `/ledger/16` Tughlaq_dynasty: confirmed. 'By 1339, the eastern regions under local Muslim governors ... had revolted' (Bengal not named; confidence 2 is right)
- `/ledger/17` Delhi_Sultanate: confirmed. 'By 1347, the Bahmani Sultanate had become independent through the rebellion of Ismail Mukh'
- `/ledger/20` Firuz_Shah_Tughlaq: confirmed. 'in 1360 invaded the region'; 'the Rai of Odisha had surrendered and promised an annual tribute of 20 elephants'
- `/ledger/21` Firuz_Shah_Tughlaq: confirmed. 'In 1363, Firuz ... launching a surprise assault on Thatta'; 'annual tribute of 400,000 Tankas'
- `/ledger/32` Tughlaq_dynasty: confirmed. 'entered Delhi victoriously on 6 June 1414'

## khalji-dynasty: fix

Area: infobox 1500000 (1300); Cliopatria 839846; ratio 0.56; corrected 712000. The Khalji page has no area. Acknowledged and resolved after the reviewer's note fix. For 1312: 3.2 M km2 against 1.03 M km2 corrected (1.87 M km2 with the vassals).

Findings:
- `/keyframe_review/1/note, /keyframe_review/7/note, /keyframe_review/9/note` [applied] The area check was misapplied. KF1 compares Cliopatria's uncorrected 839,845 km2 with the 1.5 M km2 of 1300 ('ratio 0.56, inside a factor of two'), but the corrected outline is 2,814 cells, about 0.71 M km2: ratio 0.47, a factor of 2.1, unacknowledged. KF9 compares the 1314 shape with the 3.2 M km2 of 1312, but 1312 is carried by KF7, whose corrected outline is about 1.03 M km2: ratio 0.32. Evidence: Delhi Sultanate infobox: '1300: 1,500,000 km2', '1312: 3,200,000 km2'. Project resolver on the corrections: KF0/KF1 2,814 cells; KF7 4,081 cells; KF7 plus the Yadava, Kakatiya and Hoysala 1314 outlines (the 1308-1311 vassals) 1.87 M km2; KF9 7,915 cells, 2.0 M km2. Fix: Rewrote the three ratio sentences with the corrected figures. KF1 keeps the author's resolution (the Rajput forts, Gujarat and Malwa are conquests of 1301-1311, and no Khalji hold on Bengal). KF7 states the 1312 comparison with and without the vassal tint (done by the reviewer).
- `/ledger/1/counterpart, /ledger/2/counterpart, /ledger/1/note, /wars/5/belligerents` [applied] The Sivistan contest of 1298-1299 named chagatai-khanate as counterpart, and the note said 'The invaders are Duwa's Chagatai Mongols'. The page does not say that. Evidence: Alauddin Khalji page: 'In 1298–99, another Mongol army (possibly Neguderi fugitives) invaded Sindh, and occupied the fort of Sivistan.' Duwa is named for the 1299 Qutlugh Khwaja march on Delhi, not for Sivistan. chagatai-khanate has no mirror event. Fix: Counterpart set to 'Neguderi Mongols' on both events, the note sentence corrected, and 'Neguderi Mongols' added to the belligerents of 'Mongol invasions of India under Alauddin' (done by the reviewer).
- `/identity/rulers/1, /identity/rulers/2, /identity/rulers/3` [applied] Three rulers cited no page. Evidence: Khalji dynasty infobox list: '1296–1316: Alauddin Khalji', '1316: Shihab-ud-din Omar', '1316–1320: Qutb ad-Din Mubarak'. Fix: Added source Khalji_dynasty (done by the reviewer).

Gaps for a gap-filler:
- `/ledger/20` 1316 loss of Devagiri to the Yadavas: confidence 1 (the Mubarak Shah page has the rising undated) (try https://en.wikipedia.org/wiki/Harapaladeva)
- `/ledger/22, /ledger/23` 1320 vassal_end of the Kakatiyas and the Hoysalas: confidence 1; hoysala-kingdom ends the tribute in 1318 (try https://en.wikipedia.org/wiki/Prataparudra)
- `/keyframe_review/9` The Uttar Pradesh, Chhattisgarh, Jharkhand and Bihar cells of the 1314 shape: 'unverified: page budget' (not a fault) (try https://en.wikipedia.org/wiki/Malik_Kafur)

Spot checks:
- `/ledger/3` Alauddin_Khalji: confirmed. 'conquered the fort in July 1301'
- `/ledger/4` Alauddin_Khalji: confirmed. Chittor after an eight-month siege, 1303
- `/ledger/5` Alauddin_Khalji: confirmed. 'In 1304 ... annexation of the Vaghela kingdom'
- `/ledger/6` Alauddin_Khalji: confirmed. 'In 1305, he launched an invasion of Malwa ... death of the Paramara king Mahalakadeva'
- `/ledger/10` Alauddin_Khalji: confirmed. Sitaladeva 'killed in November 1308'
- `/ledger/17` Alauddin_Khalji: confirmed. 'In 1311, Alauddin's general Malik Kamaluddin Gurg captured the Jalore fort'
- `/ledger/19` Alauddin_Khalji: confirmed. 'Malik Kafur invaded Devagiri again in 1313 ... became the governor of Devagiri'
- `/ledger/1` Alauddin_Khalji: not on page. The event (Mongols hold Sivistan, 1298-99) is on the page, but the counterpart is not. Fixed by the reviewer.

## kashmiri-sultanate: thin

Area: infobox 222236 (1342); Cliopatria 201742; ratio 0.91; corrected 80675. No Cliopatria shape is alive in 1342 (the row starts in 1344). KF0 acknowledges the factor of 2.5-2.75 and gives reasons. The 1389 figure of 250,000 km2 against 211,000-232,000 km2 for KF3/KF4 is inside a factor of two.

Gaps for a gap-filler:
- `/ledger/1, /ledger/2, /ledger/3, /ledger/4` Shihab-ud-Din's conquests of Pakhli, Swat, Gilgit, Baltistan and Ladakh (291 cells, the largest land move) are confidence 1 at 'around 1370'. The Kashmir Sultanate page names them but gives no year ('Shihab'ud-Din returned to Srinagar around 1370'). (try https://en.wikipedia.org/wiki/History_of_Ladakh)
- `/ledger/11` Baltistan leaves in 1585 by inference from the Maqpon alliance with the Mughals: confidence 1 (try https://en.wikipedia.org/wiki/Maqpon_dynasty)
- `/ledger/15` 1589: the lands outside the Valley go to 'page silent': confidence 1 (try https://en.wikipedia.org/wiki/Kashmir_Subah)
- `/keyframe_review/6` The undated lapse behind Zayn al-Abidin's 're-annexation' of Ladakh and Baltistan ('it was not until the reigns of Zayn al-Abidin and Hasan Shah that Baltiyul again came under the authority of the Sultan') (try https://en.wikipedia.org/wiki/Baltistan)

Spot checks:
- `/ledger/0` Kashmir_Sultanate: confirmed. 'The Shah Miris ruled from 1339 until they were deposed by the Chak warlords and nobles in 1561.'
- `/ledger/5` Kashmir_Sultanate: confirmed. 'The Mughals again marched onto Kashmir, with Kamran Mirza as their commander in 1531'; 'Srinagar was sacked'
- `/ledger/7, /ledger/8` Kashmir_Sultanate: confirmed. Infobox 'Mughal Interregnum: December 1540–October 1551'; 'Kashmir was formally annexed in December 1540'
- `/ledger/13` Kashmir_Sultanate: confirmed. Infobox 'Fall of Srinagar: 14 October 1586'
- `/ledger/10` Kashmir_Sultanate: confirmed. Infobox 'Mughal Invasion: 20 December 1585–8 August 1589' (the dossier cites Mughal_conquest_of_Kashmir, not reopened)
- `/ledger/1` Kashmir_Sultanate: confirmed. 'he first occupied Pakhli and went on to add Swat to his realm' (no year; confidence 1 is honest)

## sind-samma-dynasty: thin

Area: infobox None (None); Cliopatria 123201; ratio None; corrected -. The Samma page infobox has no area.

Findings:
- `/ledger (1363, 1388)` [NOT applied] The vassal's own vassal_start and vassal_end are missing for the Tughlaq tribute that tughlaq-dynasty /ledger/21 and /ledger/23 record (1363-1388, counterpart sind-samma-dynasty). Evidence: Firuz Shah Tughlaq page: 'In 1363, Firuz ... launching a surprise assault on Thatta', 'causing the rulers to submit to Firuz with an annual tribute of 400,000 Tankas'. Samma page: Firuz 'attacked Sindh in 1365 and 1367, unsuccessfully' and 'later obtained Banbhiniyo's surrender'. The /wars entry already describes this, but the ledger has no event. The reviewer brief's rule 3 wants the mirror (precedent: the sa-04-a review). Fix: Add vassal_start 1363 and vassal_end 1388 (or the Samma page's date of Banbhiniyo's surrender), counterpart tughlaq-dynasty, region = the Samma outline, source Firuz_Shah_Tughlaq.
- `/ledger/0/counterpart, /identity/predecessors` [NOT applied] The 1351 found takes Sind from soomra-dynasty, but tughlaq-dynasty /ledger/18 records the same land as its 1351 loss to the Sammas, and soomra-dynasty also draws it as Soomra land to 1351. Evidence: Samma page: 'Following this [Muhammad's death at Sondha, 1351], the Sammas became independent' (independent of Delhi). Resolver: soomra-dynasty_1202 and tughlaq-dynasty_1344 share 483 cells. Fix: Settle this together with the tughlaq-dynasty Sind finding. If the Sammas were Delhi's subjects to 1351, name tughlaq-dynasty as the found's counterpart and list it among the predecessors, beside the Soomras overthrown 'soon after 1335'.

Gaps for a gap-filler:
- `/keyframe_review/1` 1352-1520: 168 years with no territorial event; the Kutch, Bhakkar and Gujarat ties are undated (thin by design within the 1-2 page budget) (try https://en.wikipedia.org/wiki/Jam_Nizamuddin_II)
- `/ledger/0` The start is uncertain: 1336 (monarchy row), 'soon after 1335', 1344 (Cliopatria), 1351 (infobox) (try https://en.wikipedia.org/wiki/Soomra_dynasty)

Spot checks:
- `/ledger/0` Samma_dynasty: confirmed. Infobox 'Samma dynasty begins: 1351'; 'the Sammas became independent'
- `/ledger/1` Arghun_dynasty: confirmed. 'In 1520, ... he invaded Sindh'
- `/ledger/2` Arghun_dynasty: confirmed. 'Shah Beg defeated Jam Feroz's army and proceeded to sack Thatta.'
- `/ledger/3` Arghun_dynasty: confirmed. 'This marked the end of Samma rule in Sindh'; infobox 'Arghun dynasty begins: 1520' (the Samma infobox says 1524 and the text 1519; the author flags this)

## jaffna-kingdom: thin

Area: infobox None (None); Cliopatria 22777; ratio None; corrected -. The Jaffna page infobox has no area, only map captions (circa 1350, 1619).

Gaps for a gap-filler:
- `/ledger/1` 1314 gain of the Vanni, Anuradhapura, Trincomalee and Puttalam country: confidence 1, Cliopatria's year (the page has 'greatest extent (circa 1350)') (try https://en.wikipedia.org/wiki/Gampola_Kingdom)
- `/ledger/2` 1352 loss of Anuradhapura and Puttalam: confidence 1, Cliopatria's year (try https://en.wikipedia.org/wiki/Alagakkonara)
- `/ledger (1258-1323, 1440s, 1591-1619)` The Jaffna side has no vassal events. The Pandya tribute (1258-1323) is recorded by pandya-empire /ledger/13 and /ledger/24. The Vijayanagara vassalage ('becoming a vassal of the Vijayanagara Empire in 1440's') and the Portuguese client status after 1591 ('nominally a client', Portuguese conquest page) are in no ledger. (try https://en.wikipedia.org/wiki/Vijayanagara_Empire)

Spot checks:
- `/ledger/3` Jaffna_kingdom: confirmed. 'It was the second invasion dated to 1450 that eventually was successful.'
- `/ledger/4` Jaffna_kingdom: confirmed. 'It gained independence from kingdom of Kotte control in 1467'
- `/ledger/5` Portuguese_conquest_of_the_Jaffna_kingdom: confirmed. 'failed to subdue the kingdom but captured Mannar Island' (1560)
- `/ledger/6` Portuguese_conquest_of_the_Jaffna_kingdom: confirmed. The Jaffna page has 'bringing the kingdom's independent existence to an end in 1619'.

## kampili-kingdom: thin

Area: infobox None (None); Cliopatria 5836; ratio None; corrected -. The fetched page has no infobox.

Gaps for a gap-filler:
- `/ledger/0` The 1285 found is confidence 1 (Cliopatria's year). The page has Singeya Nayaka III reigning '1280 CE–1300 CE' and declaring independence 'in 1294 CE'. A minor state within its budget, thin by design. Also, the capital point (76.915 E, 15.15 N, Ballari town) is about 1.5 km north of the Cliopatria bbox (max lat 15.137); Kammata Durga itself is not located on any page. (try https://en.wikipedia.org/wiki/Kummata_Durga)

Spot checks:
- `/ledger/1` Kampili_Kingdom: confirmed. 'The Kampili kingdom then fell to the invasion in 1327 CE from the north by the forces of Muhammad bin Tughluq'; 'a Jauhar ... in 1327 CE'
- `/identity/predecessors/0` Kampili_Kingdom: confirmed. 'The founder of the kingdom was a Hoysala commander, Singeya Nayaka-III (1280 CE–1300 CE)'
- `/identity/successors (1336)` Kampili_Kingdom: confirmed. 'The Vijayanagara Empire emerged in 1336 CE from the remains of this kingdom'

## Cross-dossier matrix (mismatches and missing only; the full matrix is in reviews/sa-04-b.json)

- tughlaq-dynasty 1336 loss (kingdom-of-mewar): mismatch against kingdom-of-mewar 1326 found. Mewar is founded in 1326 with tughlaq-dynasty as counterpart; all 132 of its cells are inside the Tughlaq outline to 1336. Ten years are double-claimed.
- tughlaq-dynasty 1351 loss (sind-samma-dynasty): mismatch against sind-samma-dynasty 1351 found (counterpart soomra-dynasty). The Samma found names soomra-dynasty, and soomra-dynasty_1202 holds 483 of the same cells to 1351. Sind is triple-claimed (soomra, khalji 1314-1320, tughlaq 1320-1351).
- tughlaq-dynasty 1352 loss (nobody): mismatch against malwa-sultanate 1401 found (counterpart tughlaq-dynasty). malwa-sultanate has Malwa governed for the Tughlaqs to 1401; the Tughlaq dossier drops it to nobody in 1352
- tughlaq-dynasty 1360 vassal_start (eastern-ganga-kingdom): mismatch against eastern-ganga-kingdom 1358 vassal_start. eastern-ganga-kingdom has 1358-1359 (Firuz's invasion 'between 1353 and 1358'); the Tughlaq side has 1360-1388 (Firuz page: 1360). Agree on 1360 and on an end year.
- tughlaq-dynasty 1363 vassal_start (sind-samma-dynasty): missing. sind-samma-dynasty has no vassal_start/vassal_end with tughlaq-dynasty
- tughlaq-dynasty 1388 vassal_end (eastern-ganga-kingdom): mismatch against eastern-ganga-kingdom 1359 vassal_end. 29 years apart, both confidence 1
- tughlaq-dynasty 1388 vassal_end (sind-samma-dynasty): missing. See 1363
- tughlaq-dynasty 1407 loss (page silent: the Khokhars of the Punjab, the chiefs of Mewat and local governors): mismatch against timurid-empire 1407 loss (counterpart tughlaq-dynasty). timurid-empire /ledger/23 gives the Punjab back to tughlaq-dynasty in 1407, but the Tughlaq outline shrinks in 1407 and has no gain. The Timurid counterpart should be Khizr Khan / the Khokhars, or nobody (ia-02).
- khalji-dynasty 1290 found (mamluk-dynasty): mismatch against mamluk-dynasty 1290 dissolve. Matched on year, not on land: mamluk-dynasty hands over 'Mamluk 1285 minus Bengal' (1.34 M km2); the Khalji found takes 0.71 M km2. Flagged by the author; route to sa-04-a.
- khalji-dynasty 1308 vassal_start (yadava-dynasty): missing. yadava-dynasty has contest_end 1308 but no vassal_start with khalji-dynasty (sa-03)
- khalji-dynasty 1310 vassal_start (kakatiya-dynasty): missing. kakatiya-dynasty has contest 1310 only; no vassal_start/vassal_end with khalji-dynasty (sa-03)
- khalji-dynasty 1313 vassal_end (yadava-dynasty): missing against yadava-dynasty 1313 loss. Yadava records the 1313 annexation as a loss but no vassal_end
- khalji-dynasty 1320 vassal_end (kakatiya-dynasty): missing. See 1310
- khalji-dynasty 1320 vassal_end (hoysala-kingdom): mismatch against hoysala-kingdom 1318 vassal_end. Two years apart, both confidence 1
- kashmiri-sultanate 1531 occupation_start (mughal-empire): missing. mughal-empire has no 1531 occupation of Kashmir (sa-05); the author flags it
- kashmiri-sultanate 1540 occupation_start (mughal-empire): missing. mughal-empire has no 1540-1551 occupation (Haidar Dughlat for Humayun) (sa-05)
- kashmiri-sultanate 1586 occupation_start (mughal-empire): mismatch against mughal-empire 1585 contest_start. Kashmir draws an occupation from 14 October 1586; the Mughal side draws contest 1585-1589. Both sides need the same type.
- ceylon 1236 gain (jaffna-kingdom): mismatch. ceylon /ledger/2 (1236) and /ledger/3 (1260) gain land from jaffna-kingdom, but jaffna-kingdom starts in 1258 with no predecessor. Either Jaffna back-dates its start to the infobox's 1215 (Kalinga Magha), or ceylon names Magha's kingdom (sa-04-a).
- pandya-empire 1258 vassal_start (jaffna-kingdom): missing. The suzerain side (pandya /ledger/13, /ledger/24: 1258-1323) is present; the jaffna-kingdom side has no vassal events

## Problems

- None of the six Wikipedia pages (Tughlaq, Khalji, Samma, Jaffna, Kampili, Kashmir) gives an area for the state itself, except Kashmir. Delhi Sultanate infobox areas were used for Khalji and Tughlaq.
- Neighbour dossiers not on disk (exceptions): vijayanagara-empire, sultanate-of-bengal, bahmani-sultanate, jaunpur-sultanate, sayyid-dynasty, lodi-dynasty, portuguese-ceylon, yuan-dynasty, sur-empire.
- Mismatches to route to other groups: kingdom-of-mewar 1326 (sa-03), soomra-dynasty Sind to 1351 (sa-03?), malwa-sultanate 1401, eastern-ganga-kingdom vassal years (sa-03), timurid-empire /ledger/23 1407 (ia-02), mughal-empire occupations of Kashmir 1531 and 1540-1551 and the 1586-1589 type (sa-05), mamluk-dynasty 1290 handover area and ceylon 1236/1260 counterparts (sa-04-a), yadava and kakatiya vassal mirrors (sa-03).
- Reviewer edits applied to khalji-dynasty.json and tughlaq-dynasty.json (re-validated, 0 errors). The files were re-serialised with the same one-space indent plus a trailing newline.
