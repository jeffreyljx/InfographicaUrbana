# Review of batch me-08-x (2026-10-19)

Adversarial review of the 15 additions dossiers (states Cliopatria lacks). Validator: 0 errors for all 15 with --resolve; 2 warnings (ikhshidid-dynasty, counterpart 'sharifate-of-mecca' has no dossier yet, listed by the author). Area: only the Tahirid infobox gives an area (1,000,000 km2, 800 est.; drawn 821 shape 1,021,210 km2, ratio 1.02, acknowledged); no other page has an infobox area. Spot checks: 4 to 9 events per dossier, weighted to confidence 3 and the largest moves; none was fabricated. Overlaps between batch dossiers were computed with tools/gazetteer.py on every pair of keyframes alive in the same year.

Verdicts: tahirid-dynasty thin, ikhshidid-dynasty thin, uqaylid-dynasty pass, marwanids-of-diyar-bakr thin, mirdasid-dynasty fail, banu-mazyad thin, sallarid-dynasty thin, shaddadids thin, rawadid-dynasty thin, khurramites pass, yufirid-dynasty thin, numayrid-dynasty fix, hasanwayhids thin, annazids thin, kakuyids fail.

Reviewer-applied fixes (re-validated, read back): sallarid-dynasty /ledger/4 and /ledger/5 and rawadid-dynasty /ledger/1 confidence 3 to 2; numayrid-dynasty /ledger/1 counterpart 'local rulers of Raqqa' to hamdanid-emirates; marwanids-of-diyar-bakr /ledger/4 counterpart byzantine-empire to numayrid-dynasty (Numayrid page added to sources); ikhshidid-dynasty /identity/capitals/0/to 970 to 969. Each changed event note ends with a '[Reviewer me-08-x, 2026-10-19: ...]' tag.

## tahirid-dynasty: thin

Area: No Cliopatria row: compared with the drawn 821 keyframe (gazetteer, 4038 cells). The infobox figure is for '800 est.'; K0's note quotes it.

Findings:
- `/ledger (no event)` abbasid-caliphate holds a vassal_start (L22, 821, counterpart tahirid-dynasty, 'Khorasan, with Tabaristan a dependency of Khorasan') and a vassal_end (L32, 873) that have no mirror here. Why: Rule 3: a vassal_start of X needs a vassal_start in X's ledger with this state as counterpart. Tahirid page: 'In 821, Tahir was made governor of Khorasan'; 'in 873 he was finally overthrown by the Saffarid dynasty'. The dossier writes the Abbasid tie only as the found counterpart and in a predecessors note. Fix: Add vassal_start (821, counterpart abbasid-caliphate, region Khorasan, confidence 3, source Tahirid_dynasty) and vassal_end (873, same counterpart and region). Gap-filler work; it moves no land.
- `/keyframe_review/0-5 and /ledger/1` Transoxiana is drawn as Tahirid land in every keyframe and at the same time tinted as a Samanid vassal (vassal_start 821, confidence 1), while abbasid-caliphate L21 makes the Samanids the caliph's own vassal from 819. Why: Samanid_Empire page (cited by the author): Tahirid authority over the Samanids is stated without a year; no page gives the 821 start. Two suzerains for one vassal in two dossiers. Fix: Decide one reading: either Transoxiana stays Tahirid land with no vassal tint, or the Samanid tint is the only claim and the keyframes drop Transoxiana; align with abbasid-caliphate L21 (route to me-08-a/me-08-b).

For a gap-filler:
- `/ledger/1, /ledger/13` Year of Samanid subordination to the Tahirids (821 and 873 are bridging, confidence 1). Page to try: https://en.wikipedia.org/wiki/Nasr_I
- `/ledger/5` Year Sistan was lost (861 is the Saffarid infobox year; the Tahirid page says only 'during his governorship', Tahir II 845-862). Page to try: https://en.wikipedia.org/wiki/Ya%27qub_ibn_al-Layth_al-Saffar
- `/ledger (no event)` Abbasid vassal mirror 821-873 (see fixes). Page to try: https://en.wikipedia.org/wiki/Tahirid_dynasty

Spot checks: /ledger/0 confirmed (Tahirid_dynasty); /ledger/2 confirmed (Tahirid_dynasty); /ledger/4 confirmed (Mazyar); /ledger/6 confirmed (Tahirid_dynasty); /ledger/9 confirmed (Saffarid_dynasty); /ledger/12 confirmed (Saffarid_dynasty)

## ikhshidid-dynasty: thin

Area: Infobox has no area (checked). Largest drawn keyframe 936-938/942-943 about 1.06 million km2, mostly Egypt.

Findings:
- `/identity/capitals/0/to` (applied by the reviewer) Fustat was the capital to 970, but Jawhar took Fustat on 6 July 969 and the 969 and 970 keyframes no longer include Egypt. Why: Fatimid_conquest_of_Egypt page: 'took possession of the city on 6 July'; capital's own note says the same. Fix: Set to 969.
- `/ledger (no event)` abbasid-caliphate L63 (vassal_start 935/8, Egypt), L64 (vassal_start 944, Syria and the Hijaz), L71 and L72 (vassal_end 969), all with counterpart ikhshidid-dynasty, have no mirror here. Why: Ikhshidid page: ibn Tughj was appointed governor and in 944 'the governorships of Egypt, Syria and Hijaz were awarded for 30 years' to his family; Muhammad ibn Tughj page: recognition at Raqqa in September 944. Fix: Add vassal_start (935/8, counterpart abbasid-caliphate, Egypt, confidence 3) and vassal_end (969/7). The 944 Syria/Hijaz Abbasid tint should be reconciled with this dossier's own 936 and 942 gains of Syria from abbasid-caliphate and its Hejaz tint (route to me-08-a).
- `/ledger/1, /ledger/3, /ledger/5` Syria is gained from (936, 942) and lost to (939) abbasid-caliphate, which has no matching loss or gain; the Abbasid dossier treats Syria as an Ikhshidid vassal only from 944. Why: abbasid-caliphate ledger 930-948 has only L63, L64 and L66-L68 for this region. Fix: Route to me-08-a: either the Abbasid dossier writes loss/gain events for 936, 939 and 942 (counterpart ikhshidid-dynasty or Muhammad ibn Ra'iq), or both sides agree on a vassal reading.

For a gap-filler:
- `/ledger/10` 946 Damascus loss to the Hamdanids is bridging (confidence 1); the Ikhshidid page has Abu'l-Qasim fighting Sayf al-Dawla at Damascus, the Kafur page Damascus secured in 947. Page to try: https://en.wikipedia.org/wiki/Sayf_al-Dawla
- `/keyframe_review/6` Lebanon and the Syrian coast, Homs after 945 and the Qarmatian tribute of 968 are on no page opened. Page to try: https://en.wikipedia.org/wiki/Abu_al-Misk_Kafur

Spot checks: /ledger/1 confirmed (Muhammad_ibn_Tughj_al-Ikhshid); /ledger/5 confirmed (Muhammad_ibn_Tughj_al-Ikhshid); /ledger/7 confirmed (Muhammad_ibn_Tughj_al-Ikhshid); /ledger/11 confirmed (Ikhshidid_dynasty); /ledger/12 confirmed (Abu_al-Misk_Kafur); /ledger/16 confirmed (Fatimid_conquest_of_Egypt); /ledger/18 confirmed (Fatimid_conquest_of_Egypt); /ledger/19 confirmed (Fatimid_conquest_of_Egypt)

## uqaylid-dynasty: pass

Area: Infobox has no area (checked).

For a gap-filler:
- `/ledger/2` Year Kufa was finally lost (1007 is bridging, confidence 1). Page to try: https://en.wikipedia.org/wiki/Qirwash_ibn_al-Muqallad
- `/keyframe_review/4` Tikrit, Anbar, al-Mada'in, Hit and the Nusaybin and Jazirat ibn Umar branches are undated; the Nusaybin circle overlaps the Marwanid bridging shape 1011-1085 (see marwanids-of-diyar-bakr). Page to try: https://en.wikipedia.org/wiki/Uqaylid_dynasty

Spot checks: /ledger/0 confirmed (Uqaylid_dynasty); /ledger/1 confirmed (Uqaylid_dynasty); /ledger/5 confirmed (Uqaylid_dynasty); /ledger/6 confirmed (Uqaylid_dynasty); /ledger/7 confirmed (Uqaylid_dynasty); /ledger/8 confirmed (Uqaylid_dynasty)

## marwanids-of-diyar-bakr: thin

Area: Infobox has no area (checked); infobox dates 983/990-1085.

Findings:
- `/ledger/4/counterpart` (applied by the reviewer) The 1026 gain of Edessa named byzantine-empire as the loser, but the Byzantines held no Edessa before 1031. Why: Marwanid page: 'Nasr al-Dawla took the city of Edessa in 1026' and 'the city was retaken by the Byzantine general George Maniakes in 1031' (no previous holder named). Numayrid page: 'the Numayrids also controlled Edessa until the Byzantines conquered it in the early 1030s', and Nasr al-Dawla 'killed Utayr and captured the city' (dated 1030 there). byzantine-empire has no Edessa loss in 1026. Fix: Counterpart set to numayrid-dynasty, note extended, Numayrid page added to sources[]. numayrid-dynasty still needs the matching loss (it keeps Edessa to 1030; dates conflict 1026/1030).
- `/keyframe_review/3-7` Nisibis (Nusaybin) and Cizre are drawn Marwanid from 1011 to 1085 as bridging, on the same ground uqaylid-dynasty draws from 990 (7,587 km2 overlap, 40.9-42.0E 36.7-37.9N); the overlap is not flagged in the notes. Why: Marwanid page lists the towns without dates (K3 note); Uqaylid page: 'Mosul and the Diyar Rabi'a was occupied in 989', Nusaybin being Diyar Rabi'a's chief town, and the Uqaylid branch at Nusaybin. Fix: Drop Nusaybin (and Cizre unless a page dates it) from K3-K7 or date the Marwanid holding; otherwise flag the overlap in notes. Gap-filler work.

For a gap-filler:
- `/ledger/1` Lake Van towns (Malazgirt, Ercis, Ahlat) are undated on the Marwanid page; 984 is bridging (confidence 1). Page to try: https://en.wikipedia.org/wiki/Badh_ibn_Dustak
- `/keyframe_review/3` Dates for Siirt, Cizre and Nisibis. Page to try: https://en.wikipedia.org/wiki/Nasr_al-Dawla_Ahmad_ibn_Marwan

Spot checks: /ledger/0 confirmed (Marwanids_(Diyar_Bakr)); /ledger/3 confirmed (Marwanids_(Diyar_Bakr)); /ledger/4 confirmed (counterpart wrong, fixed) (Marwanids_(Diyar_Bakr)); /ledger/5 confirmed (Marwanids_(Diyar_Bakr)); /ledger/6 confirmed (Marwanids_(Diyar_Bakr)); /ledger/7 confirmed (Marwanids_(Diyar_Bakr))

## mirdasid-dynasty: fail

Area: Main page not opened by the reviewer; the author reports no area on any page.

Findings:
- `/ledger/13, /keyframe_review/8-11/correction, /ledger/18/region` BLOCKING. Acre, Beirut and Jubayl are drawn as Mirdasid land from January 1058 to June 1080, but the page says Thimal never controlled them and lost even the title in 1060. Why: Thimal_ibn_Salih page: the Fatimids 'compensated him with the governorships or appendages of the coastal towns of Acre, Beirut, and Jubayl (Byblos)'; 'Thimal's rule over the three coastal towns was evidently a tributary arrangement, as he did not exercise control over them'; after Mahmud took Aleppo in 1060 'Caliph al-Mustansir stripped Thimal of his holdings along the Syrian coast'. The K8 note says 'The pages do not say when he lost the coastal towns; they stay drawn to 1080 as bridging', which the page contradicts. The coast adds roughly 5,000 km2 for 22 years with no basis. Fix: Drop the 1058 gain (mention the grant in the note of /ledger/12), remove Acre, Beirut and Byblos from K8, K9, K10, K11 and from the dissolve region; K8 1058-1059 becomes al-Rahba and Raqqa only (al-Rahba to the Numayrids in 1059).
- `/ledger/2, /ledger/8, /ledger/10 (counterpart)` Raqqa is gained from, lost to and regained from 'Numayrid emirs of Raqqa', a free-text name for numayrid-dynasty, whose dossier (same batch) holds Raqqa 1007-1062 with no such events; the two dossiers draw Raqqa at once in 1022-1037 and 1040-1061 (7,081 km2). Why: Salih_ibn_Mirdas page: 'By 1022, Salih had extended his rule to the Euphrates twin towns of Raqqa and al-Rafiqah'. Thimal page: after Thimal's brother-in-law died 'she inherited the twin cities of al-Raqqa and al-Rafiqa and subsequently entrusted them with Thimal' (1039/40). Numayrid page: Raqqa conquered 1007 'from its Hamdanid governor', 'Atiyya ibn Salih, took over Raqqa in 1062'. numayrid-dynasty /ledger/5 loses Raqqa to mirdasid-dynasty in 1062, which has no 1062 gain. Fix: Use the slug numayrid-dynasty, then reconcile with numayrid-dynasty: give one owner per year (for example Mirdasid 1022 to about 1029/1038 with a Numayrid loss and regain written there, Thimal 1040 to 1062 with the Numayrid feud as a contest) and make the 1062 event a pair in both ledgers.
- `/identity/capitals` Aleppo is the capital 1042-1080 although Aleppo is outside the shapes from January 1058 to September 1060, and no capital covers 1038-1039. Why: K8 and K9 drop Aleppo (Thimal 'stepped down on 23 January 1058'; Mahmud took it in September 1060); capitals run al-Rahba 1014-1024, Aleppo 1025-1037, Raqqa 1040-1041, Aleppo 1042-1080. Fix: Split Aleppo into 1042-1057 and 1060-1080; give 1038-1039 and 1058-1059 the capital the pages support (al-Rahba or Raqqa) or say in the note that none is known.

For a gap-filler:
- `/ledger/1` Year of Manbij and Balis (1015 bridging, confidence 1). Page to try: https://en.wikipedia.org/wiki/Mirdasid_dynasty
- `/ledger/8` Year Raqqa left Mirdasid hands before 1039/40 (1038 bridging, confidence 1). Page to try: https://en.wikipedia.org/wiki/Shabib_ibn_Waththab

Spot checks: /ledger/0 confirmed (Salih_ibn_Mirdas); /ledger/2 confirmed (Salih_ibn_Mirdas); /ledger/4 confirmed (Salih_ibn_Mirdas); /ledger/6 confirmed (Salih_ibn_Mirdas); /ledger/9 confirmed (Thimal_ibn_Salih); /ledger/11 confirmed (Thimal_ibn_Salih); /ledger/13 not on page: the grant is there, the control the gain draws is denied (Thimal_ibn_Salih); /ledger/15 confirmed (Thimal_ibn_Salih); /ledger/16 confirmed (Thimal_ibn_Salih)

## banu-mazyad: thin

Area: Infobox has no area (checked); infobox c.961-c.1160, text 1163.

For a gap-filler:
- `/keyframe_review/0` One shape for 202 years: Sadaqa I's expansion (1086-1108), the Seljuk occupations of Hilla ('several times', undated) and Dubays II's losses are unwritten; the four pages opened name only Kufa, Hit and Hilla. Page to try: https://en.wikipedia.org/wiki/Hilla
- `/identity/capitals/0` Kufa as capital 961-1085 is the researcher's reading; the page names no capital before Hilla. Page to try: https://en.wikipedia.org/wiki/Banu_Mazyad
- `/keyframe_review/0` The Uqaylid page gives al-Muqallad 'Mosul, Kufa and Jami'yan' in 996: Kufa is drawn in both dossiers 996-1006 (7,587 km2, flagged in the author's notes). Page to try: https://en.wikipedia.org/wiki/Qirwash_ibn_al-Muqallad

Spot checks: /ledger/0 confirmed (Banu_Mazyad); /ledger/1 confirmed (year bridging, confidence 2 right) (Sadaqa_ibn_Mansur); /ledger/2 confirmed (Banu_Mazyad); /ledger/3 confirmed (Banu_Mazyad)

## sallarid-dynasty: thin

Area: Infobox has no area (checked); 919-1062.

Findings:
- `/ledger/4/confidence, /ledger/5/confidence` (applied by the reviewer) The 948 losses to the Rawadids and Shaddadids were confidence 3 though the page does not date them to 948. Why: Sallarid page: the paragraph after its 948 entry says Marzuban's capture 'allowed the Rawadids and Shaddadids to take control of the areas to the northeast of Tabriz and Dvin, respectively'; the Shaddadid page: 'In 951, Muhammad established himself at Dvin'. Fix: Lowered to 2, with a reviewer note.
- `/keyframe_review/1-4` Tabriz is drawn Sallarid (East Azarbaijan) 941-978 while rawadid-dynasty draws Tabriz (60 km) from 900 to 1054; 11,633 km2 overlap 941-947 and 8,599 km2 948-978, not flagged. Why: Sallarid page: Marzuban 'captured Ardabil and Tabriz' (no year); it calls them 'the Rawadids of Tabriz' when they overran the province c. 979. Rawadid page: 'initially controlled Tabriz and north-eastern Azerbaijan'. Fix: Either write the Rawadids as Sallarid vassals (vassal_start 941 or 942 and vassal_end 979 in both ledgers, counterpart each other) or cut the Tabriz circle out of the Sallarid keyframes; say which in notes.
- `/ledger (no event)` shaddadids /ledger/1 loses Dvin to sallarid-dynasty in 952 (confidence 1), but no Sallarid regain of Dvin is written and K3 leaves Dvin out. Why: Shaddadid page: 'Unable to hold Dvin against Musafirid incursion, he fled to the Armenian Kingdom of Vaspurakan' (no year). Fix: Add a gain of Dvin (952, confidence 1, counterpart shaddadids) and keep Dvin in K3 from 952, or drop the Shaddadid loss; the pair must agree.

For a gap-filler:
- `/ledger/8, /ledger/9` 979 loss of Arran and Derbent and the end of Shirvan's tribute are bridging (confidence 1). Page to try: https://en.wikipedia.org/wiki/Ibrahim_I_ibn_Marzuban_I
- `/keyframe_review/5` 989-996 the dynasty holds no land on any page; the 984 'last holding' has no place. Page to try: https://en.wikipedia.org/wiki/Sallarid_dynasty

Spot checks: /ledger/1 confirmed (Sallarid_dynasty); /ledger/2 confirmed (undated, confidence 2 right) (Sallarid_dynasty); /ledger/4 confirmed, year implied (confidence lowered) (Sallarid_dynasty); /ledger/5 confirmed, year implied (confidence lowered) (Sallarid_dynasty); /ledger/6 confirmed (Sallarid_dynasty); /ledger/7 confirmed (Sallarid_dynasty); /ledger/10 confirmed (Sallarid_dynasty); /ledger/11 confirmed (Sallarid_dynasty); /ledger/12 confirmed (Sallarid_dynasty)

## shaddadids: thin

Area: Infobox has no area (checked); 951-1199.

Findings:
- `/keyframe_review/8, /ledger/11-12` Ani is drawn Shaddadid without a break from 1164 to 1198, but the page has George III occupy Ani in 1174; the dossier quotes the 1174 capture in its notes and writes no event. Why: Shaddadids page: 'in 1174 King George took the Shahanshah as a prisoner and occupied Ani once again'; 'In the year 1199, Georgia's Queen Tamar captured Ani' (which implies an undated Shaddadid return). Fix: Add a loss of Ani in 1174 (counterpart kingdom-of-georgia, confidence 3) and end K8 in 1173; add the return before 1199 as a gain at confidence 1 if a page dates it, or leave Ani undrawn 1174-1198 with a note.

For a gap-filler:
- `/ledger/1` Year Dvin was lost to the Musafirids (952 bridging, confidence 1); sallarid-dynasty has no matching gain. Page to try: https://en.wikipedia.org/wiki/Muhammad_ibn_Shaddad
- `/keyframe_review/6-8` Ganja branch 1086-1143 and Fadl V 1155-1161 undated and undrawn. Page to try: https://en.wikipedia.org/wiki/Shaddadids
- `/keyframe_review/8` Who held Ani between 1174 and 1199. Page to try: https://en.wikipedia.org/wiki/Ani

Spot checks: /ledger/0 confirmed (Shaddadids); /ledger/2 confirmed (Shaddadids); /ledger/3 confirmed (Shaddadids); /ledger/4 confirmed (Shaddadids); /ledger/5 confirmed (page's 1075; confidence 2 right) (Shaddadids); /ledger/6 confirmed (Shaddadids); /ledger/8 confirmed (Shaddadids); /ledger/9 confirmed (Shaddadids); /ledger/12 confirmed (Shaddadids)

## rawadid-dynasty: thin

Area: Infobox has no area (checked).

Findings:
- `/ledger/1/confidence` (applied by the reviewer) The 948 gain was confidence 3 though its page does not date it to 948. Why: Sallarid page (the source): the Rawadid gain of 'the areas to the northeast of Tabriz' is in the paragraph after its 948 entry, not in it. Fix: Lowered to 2, with a reviewer note.
- `/keyframe_review/0-1` Tabriz overlaps the Sallarid Azerbaijan 941-978 (see sallarid-dynasty), not flagged. Why: Sallarid page: Marzuban 'captured Ardabil and Tabriz'. Fix: Agree a vassal pair with sallarid-dynasty or cut Tabriz there; note it here.

For a gap-filler:
- `/identity/end, /ledger/3-4` End set at the 1054 conquest; the page has Mamlan reigning until Alp Arslan 'deposed Mamlan' in 1071 (infobox 900-1070/1116): 1054-1071 is a vassal period the ledger does not write. Page to try: https://en.wikipedia.org/wiki/Wahsudan
- `/keyframe_review/2` Armenian parts of the realm and Wahsudan's 1020-1059 holdings undated. Page to try: https://en.wikipedia.org/wiki/Rawadid_dynasty

Spot checks: /ledger/0 confirmed (Rawadid_dynasty); /ledger/1 confirmed, year implied (confidence lowered) (Sallarid_dynasty); /ledger/2 confirmed (Rawadid_dynasty); /ledger/3 confirmed (Rawadid_dynasty)

## khurramites: pass

Area: No infobox area (rebel movement).

For a gap-filler:
- `/keyframe_review/0` The page gives Babak's influence 'eastward to the Caspian Sea and the Shamakhi district and Shirvan'; the drawn zone stops west of the Caspian. Defensible (both pages say influence, the Babak page names only Badd as a possession) and explained in the K0 note. Page to try: https://en.wikipedia.org/wiki/Babak_Khorramdin

Spot checks: /ledger/0 confirmed (Khurramites); /ledger/1 confirmed (Khurramites); /ledger/2 confirmed (Khurramites); /ledger/4 confirmed (14 March 838; Babak page January 838, noted by the author) (Khurramites)

## yufirid-dynasty: thin

Area: Infobox has no area (checked); 847-997.

For a gap-filler:
- `/keyframe_review/3` Sanaa is drawn Yufirid without a break 916-997 although the page says it was lost to rival takeovers (the notes name the Zaydi imams in 901 and 956); no loss or contest is written. Page to try: https://en.wikipedia.org/wiki/Al-Hadi_ila%27l-Haqq_Yahya
- `/ledger (no event)` Vassal ties on the page are unwritten: Muhammad 'paid formal deference to the Ziyadid dynasty in the Tihama lowland' and the dynasty 'nominally acknowledged the suzerainty of the Abbasid caliphs' (diploma in 873). Page to try: https://en.wikipedia.org/wiki/Ziyadid_dynasty
- `/keyframe_review/1` Hadramawt is the whole modern governorate (about 190,000 of the 255,935 km2 drawn 872-904), for 'ruled over ... Hadramawt'; a narrower Wadi Hadramawt reading would be safer. Page to try: https://en.wikipedia.org/wiki/Hadhramaut

Spot checks: /ledger/0 confirmed (Yu%27firids); /ledger/1 confirmed (no year on the page; 872 from the succession, confidence 2 right) (Yu%27firids); /ledger/3 confirmed (Yu%27firids); /ledger/4 confirmed (Yu%27firids); /ledger/5 confirmed (Yu%27firids)

## numayrid-dynasty: fix

Area: Infobox has no area (checked).

Findings:
- `/ledger/1/counterpart` (applied by the reviewer) The 1007 gain of Raqqa named 'local rulers of Raqqa'. Why: Numayrid page: 'in 1007, he conquered Raqqa from its Hamdanid governor'. Fix: Counterpart set to hamdanid-emirates (me-08-d, not written yet), note extended.

For a gap-filler:
- `/ledger/2` Edessa: the page has the Numayrids hold it 'until the Byzantines conquered it in the early 1030s' but also Nasr al-Dawla killing Utayr and capturing it (1030); marwanids-of-diyar-bakr now gains it from this dossier in 1026 and no Numayrid loss to the Marwanids is written (flagged conflict). Page to try: https://en.wikipedia.org/wiki/George_Maniakes
- `/keyframe_review/1-4` Raqqa 1022-1062 is also Mirdasid in mirdasid-dynasty (flagged conflict); the reconciliation is listed under mirdasid-dynasty. Page to try: https://en.wikipedia.org/wiki/Shabib_ibn_Waththab

Spot checks: /ledger/0 confirmed (Numayrid_dynasty); /ledger/1 confirmed (counterpart fixed) (Numayrid_dynasty); /ledger/2 confirmed (Numayrid_dynasty); /ledger/5 confirmed (Numayrid_dynasty); /ledger/6 confirmed (Uqaylid_dynasty)

## hasanwayhids: thin

Area: Infobox has no area (checked); 959-1015.

Findings:
- `/ledger/3/region` The 1015 loss hands Kermanshah (admin1) to the Annazids, but annazids' 1015 gain leaves Kermanshah out, so Kermanshah belongs to no one from 1015. Why: Annazids page: the Annazids 'occupied Qarmisin (Kermanshah)' about 1014 but were 'quickly defeated' and only 'again occupied Kermanshah' in 1039; who held it between is not said. Fix: Make the two 1015 regions the same land: drop Kermanshah from this loss (and write where it went, Buyid Shams al-Dawla or nobody) or add it to the Annazid gain.

For a gap-filler:
- `/ledger/1` Holdings under Badr are undated (979 bridging, confidence 1); buyid-dynasty has no matching loss. Page to try: https://en.wikipedia.org/wiki/Badr_ibn_Hasanwayh
- `/ledger (no event)` Vassalage on the page is unwritten: in December 970 Ibn al-'Amid 'granted Hasanwayh autonomy in exchange for tribute', and Badr 'was a vassal of Mu'ayyad al-Dawla'. Page to try: https://en.wikipedia.org/wiki/Hasanwayhids
- `/keyframe_review/1` Dinavar and Shapurkhast are gained by annazids in 1007 from this dossier, which keeps them to 1015 with no loss (12,392 km2 overlap, flagged). Page to try: https://en.wikipedia.org/wiki/Annazids

Spot checks: /ledger/0 confirmed (Hasanwayhids); /ledger/1 confirmed undated (confidence 1 right) (Hasanwayhids); /ledger/2 confirmed (Hasanwayhids); /ledger/3 confirmed (Badr killed 1014) (Hasanwayhids)

## annazids: thin

Area: Infobox has no area (checked); 990/991-1117.

For a gap-filler:
- `/keyframe_review/6` The Seljuk overrun of 1045-1047 and the 1050 reinstatement as vassals ('pay homage to Tughril Bek, who received him kindly and reinstalled the Annazids') are not drawn: no occupation or vassal events. Page to try: https://en.wikipedia.org/wiki/Annazids
- `/keyframe_review/6` After 1055 'there were no more mentions of the Annazids in historical sources'; the shape is held to 1116 as bridging (flagged). Page to try: https://en.wikipedia.org/wiki/Khorshidi_dynasty
- `/keyframe_review/3-6` The Kakuyid Hamadan circle (80 km) covers Asadabad and part of Nahavand drawn Annazid since 1015: 8,852 km2 overlap 1023-1047; shrink one circle or note it. Page to try: https://en.wikipedia.org/wiki/Kakuyids

Spot checks: /ledger/0 confirmed (Annazids); /ledger/1 confirmed (Annazids); /ledger/4 confirmed (Annazids); /ledger/5 confirmed (Annazids); /ledger/6 confirmed (Annazids); /ledger/7 confirmed (infobox 1117, confidence 2 right) (Annazids)

## kakuyids: fail

Area: Infobox has no area (checked). Largest drawn keyframe is the Yazd fief, 124,427 km2, not acknowledged; see the blocking fix.

Findings:
- `/keyframe_review/5/correction, /ledger/6/region, /ledger/7/region` BLOCKING. The Seljuk fief of 'Yazd and Abarkuh' (two towns) is drawn as the whole modern Yazd province, 124,427 km2 reaching 58.1E and 35.2N (the Tabas district and the desert), for 89 years: four times the Isfahan state it replaces. Why: Kakuyids page: 'Faramurz was given Yazd and Abarkuh in fief by the Seljuks'; gazetteer resolve of K5 gives 492 cells, bbox [52.87, 29.83, 58.1, 35.16]. Fix: Replace admin1 Yazd with a circle at Yazd (place Yazd, about 60-70 km) plus Abarkuh (lon 53.28, lat 31.13, about 30 km) in K5, the 1052 gain and the 1141 dissolve; keep the text.
- `/ledger/1` buyid-dynasty L14/L15 make the Kakuyids Buyid vassals 1023-1029 under the counterpart 'kakuyid-dynasty' (not this slug); this dossier writes the 1023 Hamadan event as an outright gain from the Buyids and no vassal pair. Why: Kakuyids page: Ala al-Dawla was 'a Daylamite military leader under the service of the Buyid amirate of Jibal' who 'over time ... effectively became independent of Buyid control' (no dates). Fix: Route to me-08-c: buyid-dynasty should use the slug kakuyids; agree with it whether 1008-1029 is a vassal period (then add the vassal pair here) or not.

For a gap-filler:
- `/ledger/4` Who took Hamadan from Garshasp I and when (1048 bridging, confidence 1). Page to try: https://en.wikipedia.org/wiki/Garshasp_I
- `/keyframe_review/1` Hulwan, taken from the Annazids after 1023 and given up under pressure from Musharrif al-Dawla, is not written. Page to try: https://en.wikipedia.org/wiki/Kakuyids

Spot checks: /ledger/0 confirmed (Kakuyids); /ledger/1 confirmed (Kakuyids); /ledger/4 page does not say who took Hamadan (confidence 1 right) (Kakuyids); /ledger/5 confirmed (Kakuyids); /ledger/6 confirmed (Kakuyids); /ledger/7 confirmed (Kakuyids)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| tahirid-dynasty 821 vassal_start (samanid-empire) | - | exception | counterpart owned by me-08-b, which has not run yet |
| tahirid-dynasty 861 loss (saffarid-dynasty) | - | exception | counterpart owned by me-08-b, which has not run yet |
| tahirid-dynasty 864 loss (zaydi-alid-dynasties) | - | exception | counterpart owned by me-08-b, which has not run yet |
| tahirid-dynasty 870 loss (saffarid-dynasty) | - | exception | counterpart owned by me-08-b, which has not run yet |
| tahirid-dynasty 873 loss (saffarid-dynasty) | - | exception | counterpart owned by me-08-b, which has not run yet |
| tahirid-dynasty 873 vassal_end (samanid-empire) | - | exception | counterpart owned by me-08-b, which has not run yet |
| tahirid-dynasty 828 gain (Kharijites of Sistan) | - | exception | listed in counterparts_needing_dossiers (kharijites-of-sistan) |
| tahirid-dynasty 839 gain (Mazyar of Tabaristan (Qarinvandids)) | - | exception | listed (bavandid-dynasty / Qarinvandids) |
| abbasid-caliphate 821 vassal_start (tahirid-dynasty) | - | missing | No vassal_start of abbasid-caliphate in tahirid-dynasty (fix listed there). |
| abbasid-caliphate 873 vassal_end (tahirid-dynasty) | - | missing | No vassal_end in tahirid-dynasty. |
| ikhshidid-dynasty 936 gain (abbasid-caliphate) | - | missing | abbasid-caliphate (me-08-a) has no loss of Syria in 936; it has Syria only as an Ikhshidid vassal from 944. |
| ikhshidid-dynasty 939 loss (abbasid-caliphate) | - | missing | No Abbasid (Ibn Ra'iq) gain in 939; the winner was Muhammad ibn Ra'iq, an Abbasid commander. |
| ikhshidid-dynasty 942 gain (abbasid-caliphate) | - | missing | No Abbasid loss in 942. |
| abbasid-caliphate 935 vassal_start (ikhshidid-dynasty) | - | missing | Egypt 935/8; no mirror in ikhshidid-dynasty. |
| abbasid-caliphate 944 vassal_start (ikhshidid-dynasty) | - | missing | Syria and the Hijaz 944; no mirror; ikhshidid-dynasty instead tints the Hejaz as its own vassal (sharifate-of-mecca). |
| abbasid-caliphate 969 vassal_end (ikhshidid-dynasty) | - | missing | Two vassal_end events (L71, L72); no mirror. |
| ikhshidid-dynasty 944 vassal_start (sharifate-of-mecca) | - | exception | listed; fatimid-caliphate writes the same counterpart as 'Sharifate of Mecca': one string is needed. |
| ikhshidid-dynasty 944 loss (hamdanid-emirates) | - | exception | counterpart owned by me-08-d, which has not run yet |
| ikhshidid-dynasty 946 loss (hamdanid-emirates) | - | exception | counterpart owned by me-08-d, which has not run yet |
| ikhshidid-dynasty 947 gain (hamdanid-emirates) | - | exception | counterpart owned by me-08-d, which has not run yet |
| ikhshidid-dynasty 969 loss (fatimid-caliphate) | fatimid-caliphate 969 gain | matched | Egypt, 969/7 on both sides. |
| ikhshidid-dynasty 970 loss (fatimid-caliphate) | fatimid-caliphate 970 gain | matched | Palestine 970/5 here, Damascus and Ramla 970/11 there: same year, months differ; Damascus 970/11 matches exactly. |
| buyid-dynasty 989 loss (uqaylid-dynasty) | uqaylid-dynasty 990 found | matched | Mosul and Diyar Rabi'a: Buyid loss 989, Uqaylid found 990 (infobox 990, text 989). |
| uqaylid-dynasty 996 gain (buyid-dynasty) | - | missing | buyid-dynasty (me-08-c, reviewed thin) has no 996 loss of Mosul (it already lost Mosul in 989). |
| uqaylid-dynasty 1007 loss (buyid-dynasty) | - | missing | No Buyid gain of Kufa. |
| uqaylid-dynasty 1008 gain (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no loss of al-Rahba. |
| uqaylid-dynasty 1014 loss (mirdasid-dynasty) | mirdasid-dynasty 1014 found | mismatch | mirdasid-dynasty founds at al-Rahba in 1014 with counterpart null; the Salih page has Salih seizing al-Rahba in 1008, the Qirwash page Qirwash in 1008/9. One reading needed. |
| uqaylid-dynasty 1080 gain (mirdasid-dynasty) | mirdasid-dynasty 1080 loss | matched | Aleppo, June 1080. |
| uqaylid-dynasty 1081 gain (numayrid-dynasty) | numayrid-dynasty 1081 loss | matched | Harran (and Saruj). |
| uqaylid-dynasty 1086 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| uqaylid-dynasty 990 found (buyid-dynasty) | marwanids-of-diyar-bakr 1011 gain | mismatch | Land overlap, not flagged: Nusaybin/Cizre drawn by both from 1011 to 1085 (7,587 km2); Marwanid side is bridging. |
| marwanids-of-diyar-bakr 984 gain (local Armenian and Arab lords of the Lake Van shore) | - | exception | no state; nobody-like |
| marwanids-of-diyar-bakr 991 gain (hamdanid-emirates) | - | exception | counterpart owned by me-08-d, which has not run yet |
| marwanids-of-diyar-bakr 1011 gain (Ibn Dimne of Amid) | - | exception | the dynasty's own vassal; no dossier needed |
| marwanids-of-diyar-bakr 1026 gain (numayrid-dynasty) | numayrid-dynasty 1030 loss | mismatch | Counterpart corrected by the reviewer from byzantine-empire. numayrid-dynasty keeps Edessa to 1030 and loses it to byzantine-empire; its page has Nasr al-Dawla capture Edessa in 1030. Both sides draw Edessa 1026-1030 (4,805 km2), flagged in the author notes. |
| marwanids-of-diyar-bakr 1031 loss (byzantine-empire) | - | missing | byzantine-empire (eu-05) has no Edessa events 1026-1036; it gains Edessa from abbasid-caliphate in 944 (L69, confidence 2) and never loses it, while the Numayrid page has Edessa Numayrid until the early 1030s. Route to eu-05. |
| marwanids-of-diyar-bakr 1032 gain (byzantine-empire) | - | missing | byzantine-empire (eu-05) has no Edessa events 1026-1036; it gains Edessa from abbasid-caliphate in 944 (L69, confidence 2) and never loses it, while the Numayrid page has Edessa Numayrid until the early 1030s. Route to eu-05. |
| marwanids-of-diyar-bakr 1033 loss (byzantine-empire) | - | missing | byzantine-empire (eu-05) has no Edessa events 1026-1036; it gains Edessa from abbasid-caliphate in 944 (L69, confidence 2) and never loses it, while the Numayrid page has Edessa Numayrid until the early 1030s. Route to eu-05. |
| marwanids-of-diyar-bakr 1085 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| mirdasid-dynasty 1015 gain (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1025 gain (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1029 loss (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1038 loss (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1042 gain (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1058 loss (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1058 gain (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1060 gain (fatimid-caliphate) | - | missing | fatimid-caliphate (me-08-c) has no event with counterpart mirdasid-dynasty; route to me-08-c (the 1058 coastal gain should go, see the mirdasid fail). |
| mirdasid-dynasty 1022 gain (Numayrid emirs of Raqqa) | numayrid-dynasty | mismatch | Free-text counterpart for numayrid-dynasty, which holds Raqqa 1007-1062 with no matching event; overlap 7,081 km2 1022-1061 (flagged). |
| mirdasid-dynasty 1038 loss (Numayrid emirs of Raqqa) | numayrid-dynasty | mismatch | Free-text counterpart for numayrid-dynasty, which holds Raqqa 1007-1062 with no matching event; overlap 7,081 km2 1022-1061 (flagged). |
| mirdasid-dynasty 1040 gain (Numayrid emirs of Raqqa) | numayrid-dynasty | mismatch | Free-text counterpart for numayrid-dynasty, which holds Raqqa 1007-1062 with no matching event; overlap 7,081 km2 1022-1061 (flagged). |
| numayrid-dynasty 1062 loss (mirdasid-dynasty) | mirdasid-dynasty | mismatch | mirdasid-dynasty has Raqqa from 1040 and writes no 1062 gain. |
| mirdasid-dynasty 1059 loss (numayrid-dynasty) | numayrid-dynasty 1059 gain | matched | al-Rahba. |
| mirdasid-dynasty 1061 gain (numayrid-dynasty) | numayrid-dynasty 1061 loss | matched | al-Rahba, August 1061. |
| banu-mazyad 1163 loss (abbasid-caliphate) | abbasid-caliphate 1162 gain | mismatch | abbasid-caliphate L76 names the counterpart 'mazyadids'; the slug is banu-mazyad (route to me-08-a). Years 1162/1163 within one. |
| banu-mazyad 961 found (buyid-dynasty) | uqaylid-dynasty 996 gain | mismatch | Kufa drawn by both 996-1006 (7,587 km2), flagged in the author notes. |
| sallarid-dynasty 941 gain (sajid-dynasty) | - | exception | counterpart owned by me-08-b, which has not run yet |
| sallarid-dynasty 942 gain (sajid-dynasty) | - | exception | counterpart owned by me-08-b, which has not run yet |
| sallarid-dynasty 942 vassal_start (shirvan) | - | exception | counterpart owned by eu-19, which has not run yet |
| sallarid-dynasty 979 vassal_end (shirvan) | - | exception | counterpart owned by eu-19, which has not run yet |
| sallarid-dynasty 979 loss (local rulers of Arran and Derbent) | - | exception | no state named by the page |
| sallarid-dynasty 948 loss (rawadid-dynasty) | rawadid-dynasty 948 gain | matched | NE of Tabriz. |
| sallarid-dynasty 948 loss (shaddadids) | shaddadids 951 found | mismatch | Sallarid page implies 948, Shaddadid page says 951 (flagged). |
| sallarid-dynasty 971 loss (shaddadids) | shaddadids 971 gain | matched | Ganja. |
| sallarid-dynasty 979 loss (rawadid-dynasty) | rawadid-dynasty 979 gain | matched | Azerbaijan. |
| sallarid-dynasty 989 loss (buyid-dynasty) | - | missing | buyid-dynasty has no gain of Shamiran/Tarom (me-08-c). |
| sallarid-dynasty 997 gain (buyid-dynasty) | - | missing | buyid-dynasty has no loss in 997. |
| sallarid-dynasty 941 gain (sajid-dynasty) | rawadid-dynasty 900 found | mismatch | Land overlap, not flagged: Tabriz drawn by both 941-978 (11,633 then 8,599 km2). |
| shaddadids 952 loss (sallarid-dynasty) | - | missing | sallarid-dynasty writes no 952 regain of Dvin. |
| shaddadids 971 gain (sallarid-dynasty) | sallarid-dynasty 971 loss | matched | Ganja. |
| shaddadids 1022 gain (bagratid-armenia) | - | exception | counterpart owned by eu-19, which has not run yet |
| shaddadids 1072 gain (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| shaddadids 1075 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| shaddadids 1085 gain (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| shaddadids 1086 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| shaddadids 1124 loss (kingdom-of-georgia) | - | exception | counterpart owned by eu-19, which has not run yet |
| shaddadids 1125 gain (kingdom-of-georgia) | - | exception | counterpart owned by eu-19, which has not run yet |
| shaddadids 1161 loss (kingdom-of-georgia) | - | exception | counterpart owned by eu-19, which has not run yet |
| shaddadids 1164 gain (kingdom-of-georgia) | - | exception | counterpart owned by eu-19, which has not run yet |
| shaddadids 1199 loss (kingdom-of-georgia) | - | exception | counterpart owned by eu-19, which has not run yet |
| rawadid-dynasty 1054 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| abbasid-caliphate 825 loss (khurramites) | khurramites 816 found | mismatch | Abbasid loss of 'Armenia and Azerbaijan' in 825 (confidence 1, from a Cliopatria step) against a Khurramite zone of the Badd highlands from 816; flagged by the author; route to me-08-a. |
| khurramites 837 loss (abbasid-caliphate) | abbasid-caliphate 837 gain | matched | Badd 837. |
| yufirid-dynasty 872 gain (local rulers of Hadramawt) | - | exception | no state named |
| yufirid-dynasty 905 loss (Ismaili da'is of Ali ibn al-Fadl al-Jayshani) | - | exception | listed (ismaili-dais-of-sanaa) |
| yufirid-dynasty 916 gain (Ismaili da'is of Ali ibn al-Fadl al-Jayshani) | - | exception | listed |
| numayrid-dynasty 1007 gain (hamdanid-emirates) | - | exception | counterpart owned by me-08-d, which has not run yet (counterpart corrected by the reviewer) |
| numayrid-dynasty 1030 loss (byzantine-empire) | - | missing | byzantine-empire has Edessa from 944 and no 1030-1032 gain; route to eu-05. |
| numayrid-dynasty 1081 loss (uqaylid-dynasty) | uqaylid-dynasty 1081 gain | matched | Harran. |
| hasanwayhids 979 gain (buyid-dynasty) | - | missing | buyid-dynasty has no loss of the Jibal holdings (and no Hasanwayhid vassal tint). |
| hasanwayhids 1013 loss (annazids) | annazids 1013 gain | matched | Shahrizor. |
| hasanwayhids 1015 loss (annazids) | annazids 1015 gain | mismatch | Same year; the Hasanwayhid loss includes Kermanshah, the Annazid gain does not. |
| annazids 1007 gain (hasanwayhids) | hasanwayhids | missing | No Hasanwayhid loss of Dinavar and Shapurkhast; both draw them 1007-1015 (12,392 km2, flagged). |
| annazids 1039 gain (Quhi Kurds) | - | exception | listed (quhi-kurds) |
| annazids 1040 loss (kakuyids) | kakuyids 1040 gain | matched | Kermanshah and Dinavar. |
| annazids 1047 gain (kakuyids) | kakuyids 1047 loss | matched | Kermanshah and Dinavar. |
| annazids 1015 gain (hasanwayhids) | kakuyids 1023 gain | mismatch | Land overlap, not flagged: the Kakuyid Hamadan circle covers Annazid Asadabad/Nahavand 1023-1047 (8,852 km2). |
| kakuyids 1023 gain (buyid-dynasty) | buyid-dynasty 1023 vassal_start | mismatch | buyid-dynasty L14/L15 write a Kakuyid vassal tint 1023-1029 under the counterpart 'kakuyid-dynasty'; this dossier writes an outright gain of Hamadan. Slug and reading to agree (route to me-08-c). |
| kakuyids 1048 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| kakuyids 1052 loss (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |
| kakuyids 1052 gain (great-seljuk-empire) | - | exception | counterpart owned by me-09-a, which has not run yet |

## Routing and problems

- No page failed to load for the reviewer; WebFetch returns a model summary, so quoted sentences are the fetch tool's. Years under counterparts_needing_dossiers are given only where the author's pages gave them.
- Reviewer applied 5 small verified fixes (re-validated, read back): sallarid-dynasty /ledger/4-5 and rawadid-dynasty /ledger/1 confidence 3 to 2; numayrid-dynasty /ledger/1 counterpart to hamdanid-emirates; marwanids-of-diyar-bakr /ledger/4 counterpart to numayrid-dynasty (+ Numayrid page in sources[]); ikhshidid-dynasty /identity/capitals/0/to 970 to 969.
- Neighbour dossiers in the author's Context list mostly lie far from this batch; the ones read for cross-checks are byzantine-empire and oghuz-turks (Context) plus abbasid-caliphate, buyid-dynasty and fatimid-caliphate (the actual counterparts). hamdanid-emirates (me-08-d), saffarid/samanid/zaydi/sajid (me-08-b), great-seljuk-empire (me-09-a) and shirvan/kingdom-of-georgia/bagratid-armenia (eu-19) are not written: those events are exceptions.
- Routing for other groups: abbasid-caliphate (me-08-a) should use banu-mazyad not 'mazyadids' (L76) and reconcile its 825 Khurramite loss and its 936-944 Syria reading with ikhshidid-dynasty; buyid-dynasty (me-08-c) should use kakuyids not 'kakuyid-dynasty' (L14-L15) and has no events for the Uqaylid 996, Sallarid 989/997, Hasanwayhid, Annazid or Banu Mazyad transfers; fatimid-caliphate (me-08-c) has no Mirdasid events and no al-Rahba 1008 loss; byzantine-empire (eu-05) holds Edessa from 944 with no loss before 1031 although the Numayrid page has it Numayrid until the early 1030s.
- Systematic author choice: vassal ties are left to the suzerain's dossier (Abbasid tints of the Tahirids and Ikhshidids, Buyid tints of the Kakuyids and Hasanwayhids, Seljuk tints of the Annazids and Rawadids); rule 3 asks for both sides.

Gazetteer names needed (all drawn as coordinates today): Rahba (al-Rahba, Mayadin), Mayyafariqin (Silvan), Ercis, Cizre (Jazirat ibn Umar), Hasankeyf (Hisn Kayfa), Hit, Dvin, Ani, Tarom (Tarum), Shamiran, Hulwan (Sar-e Pol-e Zahab), Dinavar, Nahavand, Asadabad, Abarkuh, Shibam Kawkaban, Badd (Babak Castle), Balis, Rafaniyya.
