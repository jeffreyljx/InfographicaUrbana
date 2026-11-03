# Review of batch sa-04-a (Phase B)

Reviewer: adversarial review, 2026-10-19. Dossiers: ghurid-dynasty, kathmandu, mamluk-dynasty, pandya-empire, ceylon, kingdom-of-dambadeniya. Machine copy: history/notes/phase-b/reviews/sa-04-a.json.

Validator (--resolve): 0 errors in all six. The warnings are the resolver's unknown places (Kalinjar, Nadol, Bathinda, Anahilapataka, Nuwakot, Kirtipur) and counterpart slugs with no dossier (khalji-dynasty-of-bengal, chahamanas-of-ranastambhapura, telugu-chodas-of-nellore, kingdom-of-lalitpur), all listed by the author.

Verdicts: ghurid-dynasty **fail**, mamluk-dynasty **fail**, kathmandu **fix**, pandya-empire **fail**, ceylon **fail**, kingdom-of-dambadeniya **fail**.

## ghurid-dynasty: fail

Area: infobox 2000000 km2 (1200) vs Cliopatria 2117197.3 km2, ratio 1.06. ghurid-dynasty_1192 (1192-1201); KF3 and KF5 quote the same figures.

Findings:

- `/ledger (1206-1215)` [for the author] The dossier has no vassal_start / vassal_end for the Ghurid sultans' own status as Khwarazmian vassals from 1206 to 1215. The author leaves it to the khwarezmid-empire dossier only. Evidence: Ghurid dynasty page, coinage table: the 1206-1215 rulers are headed 'As vassals of the Khwarazmian Empire' ('Green shaded row signifies Ghurid vassalage under the Khwarazmian dynasty'). The Khwarazmian Empire page has 'sweeping aside the Ghurids in 1215, whom they vassalized after the assassination of Muhammad Ghuri'. Rule 3 needs the vassal's own vassal_start with the overlord as counterpart, as chola-empire /ledger/36 does for the Pandyas. Fix: Add vassal_start 1206 (month 3 or later) and vassal_end 1215, counterpart 'khwarezmid-empire', region = the KF6/KF7 remnant (Ghor, Bamiyan and whatever of Ghazni the Yildiz finding leaves), source Ghurid_dynasty, confidence 3. Keep the note for the khwarezmid-empire side.
- `/keyframe_review/3, /keyframe_review/5; /ledger (1198, c. 1206)` [for the author] Balkh is missing. The Ghurids held it from 1198 into 1205-1206, but the ledger has no gain or loss for it, and no keyframe draws it. Evidence: Muhammad of Ghor page: after Andkhud (1204) 'the Ghurids lost the control over most of the Khurasan except Herat and Balkh', and Muhammad's governor of Balkh besieged Tirmidh in 1205. kara-khitans /ledger/14 (1198, vassal_end): 'In 1198, Muhammad of Ghor ... seized Balkh from the vassal of the Qara Khitai' (Qara Khitai page). The KF5 note says Balkh was left out 'because no page dates its acquisition', but the neighbour's page does date it. Fix: Add a gain in 1198 (counterpart: the Qara Khitai vassal at Balkh, the same string as kara-khitans /ledger/14), source Qara_Khitai. Add a loss by 1206 to khwarezmid-empire (confidence 1 if no page dates it). Add place=Balkh to the corrections of the 1198-1205 keyframes (a new keyframe 1198-1201 inside ghurid-dynasty_1192, and ghurid-dynasty_1202).
- `/keyframe_review/6, /keyframe_review/7, /ledger/40; report counterparts_needing_dossiers` [for the author] Ghazni is in two places. KF6/KF7 keep Ghazni and Kabul Ghurid until 1215 and the dissolve takes Ghazni from the Ghurids, yet the KF6 note says Yildiz 'established himself as the king of Ghazni in 1206', and the report asks for a 'Yildiz of Ghazni' (1206-1216) dossier. That dossier would draw the same land twice. Evidence: Ghurid dynasty page: after Muhammad's assassination in March 1206, 'Tajuddin Elduz became the ruler of Ghazni'. No loss of Ghazni to Yildiz is in the ledger. Fix: Choose one reading. (a) Yildiz rules Ghazni for himself: add a 1206 loss of Ghazni and Kabul to 'Yildiz of Ghazni', cut them from KF6/KF7, and move the 1215 dissolve region to Ghor and Firozkoh. (b) Yildiz rules as a Ghurid governor: drop 'Yildiz of Ghazni' from counterparts_needing_dossiers, say so in the notes, and point mamluk-dynasty's Yildiz events at that reading.
- `/keyframe_review/0` [for the author] Verdict ok for 1152-1176, but the ledger adds Ghazni (1173, 60 km), Herat (1175, 100 km), Multan (1175, 100 km) and Uch (1176, 60 km) outside the 153k km2 shape. That is about 85k km2, more than half the shape again, so it is not small. The note itself says the shape is 'a little small for 1173-1176'. Evidence: shapes.csv: ghurid-dynasty_1152 is 152,992 km2, bbox to 70.45 E; Multan (71.5 E) and Uch (71.07 E) are outside the bbox. Ghazni and Herat are 'outside, tested against the grid' (KF0 note). Fix: Add new keyframes 1173-1174 (union of Cliopatria 1152 and Ghazni 60 km) and 1175-1176 (adding Herat, Multan and Uch), or mark KF0 adjust with from/to and the union.
- `/ledger/32/region, /ledger/36/region` [for the author] The 1205 gain and the 1206 loss of Bengal draw all of Bangladesh. The sena-dynasty dossier keeps east Bengal until 1230, and mamluk-dynasty draws the same Khalji Bengal as West Bengal, Rajshahi and Rangpur. Evidence: Ghurid dynasty page names only Lakhnauti: 'established an Islamic government in the former Sena capital of Lakhnauti in 1205'. sena-dynasty /ledger/9 loses Nadia in 1204 and the Senas last to 1230 (identity end). Fix: Use the mamluk-dynasty region (admin1 West Bengal, Rajshahi, Rangpur) in /ledger/32, in /ledger/36 (with Bihar) and in /wars/7 zones. Not blocking on its own.
- `/ledger/26/region, /ledger/29/region, /wars/6/zones` [for the author] The Khorasan region includes all of Turkmenistan: Tashauz (Khwarazm proper), Balkan and the Caspian coast. The page names only Khurasan, Nishapur, Merv and Tus. Evidence: Muhammad of Ghor page: 'The Ghurids, thus, for a short span established their sway over most of the Khurasan', with Nishapur, Merv and Tus. Fix: Replace {country: Turkmenistan} with {admin1: Mary, country: Turkmenistan} (Merv) in the ledger regions and the war zone. The keyframe minus-corrections can stay. Not blocking.
- `/ledger/14, /ledger/16, /ledger/17 counterpart` [applied by reviewer] The counterpart was 'tomara-dynasty', but that dossier ends in 1152, succeeded by chauhan-dynasty. The 1192 vassal of Delhi was a local Tomara ruler under the Chahamanas. Evidence: Qutb ud-Din Aibak page: 'He also took control of Delhi in 1192, where he initially retained the local Tomara ruler as a vassal'; 'In 1193, he deposed the Tomara ruler for treason and took direct control of Delhi.' tomara-dynasty identity end 1152. Fix: Done: counterpart = 'Tomara ruler of Delhi (Chahamana vassal)' in all three, with the same string so the pair still matches.
- `/ledger/34/source, /ledger/40/source` [applied by reviewer] These cited Khwarazmian_Empire for 'captured Herat and Ghor in 1206, and finally Ghazni in 1215', but that page has no such sentence: it never mentions Herat in the text or Ghor at all. Evidence: Read on the Khwarazmian Empire page: only 'sweeping aside the Ghurids in 1215, whom they vassalized ...'. The quoted sentence is on the Ghurid dynasty page: 'The Khwarezmians under Ala al-Din Muhammad captured Herat and Ghor in 1206, and finally Ghazni in 1215, completing the takeover of the western part of the Ghurid empire.' Fix: Done: source = https://en.wikipedia.org/wiki/Ghurid_dynasty, which is already in sources[]. Confidence 3 kept, since the event is true and the page is listed.
- `/ledger/26/confidence, /ledger/29/confidence` [applied by reviewer] Both were confidence 3 with a region (all of Turkmenistan) that the page does not name. Evidence: See the region finding above. Fix: Done: confidence 3 to 2.

Thin (for a gap-filler):

- `/ledger/0` The 1152 start is confidence 1. The Ghurid page has 'In 1152, Ala al-Din Husayn refused to pay tribute to the Seljuks' and the sack of Ghazni, which would support confidence 2 and a Seljuk vassalage before 1152. Try: https://en.wikipedia.org/wiki/Ala_al-Din_Husayn
- `/keyframe_review/1 (Sistan)` Cliopatria holds about 900 cells of Sistan from 1177, and no page opened mentions it. Try: https://en.wikipedia.org/wiki/Sistan
- `/ledger/27` The 1200 Bihar gain is confidence 1. sena-dynasty /ledger/8 cites 'He subjugated much of Bihar in 1200'. Try: https://en.wikipedia.org/wiki/Bakhtiyar_Khalji
- `/ledger/28, /ledger/33` The ends of the Anhilwara (1201) and Kalinjar (1205) occupations are confidence 1. The neighbours' pages date them: chaulukya 'back under the Chaulukya rule by 1201 CE'; chandela 'A 1205 inscription ... Kalanjaradhipati'. Try: https://en.wikipedia.org/wiki/Chaulukya_dynasty

Spot checks:

- `/ledger/26` Muhammad_of_Ghor: confirmed (1200, after Tekish's death, 'established their sway over most of the Khurasan'; the region is broader than the page, so confidence lowered)
- `/ledger/31` Muhammad_of_Ghor: confirmed (Andkhud 1204, 'lost the control over most of the Khurasan except Herat and Balkh')
- `/ledger/10` Muhammad_of_Ghor: confirmed ('ended the Ghaznavids rule in 1186 CE')
- `/ledger/34` Khwarazmian_Empire: not on page (the cited page); the sentence and year are confirmed on Ghurid_dynasty, and the source was corrected
- `/ledger/40` Khwarazmian_Empire: not on page for Ghazni 1215 (the cited page has only 'sweeping aside the Ghurids in 1215'); confirmed on Ghurid_dynasty, and the source was corrected
- `/ledger/1` Ghurid_dynasty: confirmed (1173, Ghazni from the Ghuzz Turks)
- `/ledger/24` Muhammad_of_Ghor: confirmed ('The Gahadavala capital Kanauj was annexed in 1198')
- `/ledger/16` Qutb_ud-Din_Aibak: confirmed (Tomara ruler deposed in 1193)

## mamluk-dynasty: fail

Area: infobox 1300000 km2 (1250) vs Cliopatria 1337756.5 km2, ratio 1.03. No area on the Mamluk page; the Delhi Sultanate infobox gives 1,300,000 km2 for 1250 (mamluk-dynasty_1250).

Findings:

- `/ledger/3; /keyframe_review/1, /keyframe_review/2` [for the author] The Bihar gain of 1215 (about 94k km2) leaves no trace in the keyframes. KF1 (1210-1215) and KF2 (1216-1226) do not add Bihar, and the KF2 note says Bihar 'enters the Cliopatria shape only in 1227'. Evidence: shapes.csv: mamluk-dynasty_1210 and _1216 reach only 83.90 E; Bihar runs from 83.3 to 88.3 E, and the 1227 shape reaches 87.79 E. Iltutmish page: 'Iltutmish's forces captured Bihar in the 1210s' (no year). Fix: Either add admin1 Bihar to the KF2 correction (and a 1215 keyframe or a KF1 from/to split), or move /ledger/3 to 1227, the Cliopatria year (confidence 1 either way).
- `/ledger/18, /ledger/19; /keyframe_review/5 note` [for the author] Bhilsa is drawn as a raid ('raids only and add no land'), but the page says the army occupied it. paramara-dynasty records a Mamluk occupation of Bhilsa from 1233 to 1239. Evidence: Iltutmish page: 'Iltutmish's army occupied Bhilsa, and destroyed a temple ...' (1234-35); for Ujjain the army 'made little effort to annex the Paramara territory'. paramara-dynasty /ledger/14 (1233 occupation_start mamluk-dynasty, Bhilsa) and /ledger/15 (1239 occupation_end). Fix: Split the event. Bhilsa becomes occupation_start 1234 (or 1233 to match) and occupation_end 1239 (confidence 1, mirroring paramara /ledger/15), counterpart paramara-dynasty. Ujjain stays a contest.
- `/ledger (1244-1247)` [for the author] The Odia occupation of Rarh and Gauda (Mamluk Bengal), 1244-1247, is missing. The owner records an occupation with the roles reversed. Evidence: eastern-ganga-kingdom /ledger/13 (1244 occupation_start, counterpart mamluk-dynasty: 'Rarh and Gauda remained occ[upied]') and /ledger/15 (1247 occupation_end), from the Eastern Ganga dynasty page. Fix: Add occupation_start 1244 and occupation_end 1247, counterpart 'eastern-ganga-kingdom', region Rarh and Gauda (south-west and north-west West Bengal), source Eastern_Ganga_dynasty (add it to sources). Confidence as on the neighbour.
- `/ledger/26/counterpart, /identity/successors/1` [for the author] Bengal of 1287 is handed to 'sultanate-of-bengal', but that state's Cliopatria row runs 1344-1533. Bughra Khan's independent Bengal of 1287 is a different, earlier state. Evidence: Ghiyas ud din Balban page: 'However, Bughra declared independence after Balban's death, which he maintained for 40 years.' polities.csv: sultanate-of-bengal 1344..1533. Fix: Counterpart = 'Bughra Khan's Bengal (Balbani rulers of Lakhnauti)' in /ledger/26, and the same in successors (or remove that successor entry). List the state under counterparts_needing_dossiers. I did not apply this, so that ledger and identity stay consistent.
- `/ledger (1229-1258)` [for the author] The Abbasid investiture is not in the ledger. The Iltutmish page dates it, and abbasid-caliphate /ledger/79 carries a vassal_start mamluk-dynasty from 1210 at confidence 1 ('page silent'). Evidence: Iltutmish page: recognition in 1228, and 'the embassy arrived in Delhi with a deed of investiture on 18 February 1229'. The research brief: the '(Allegiance of X to Y)' rows are 'vassalage evidence that still needs a page to confirm the years'. Fix: Either add vassal_start 1229-02 and vassal_end 1258-02 (fall of Baghdad), counterpart abbasid-caliphate, source Iltutmish, and tell the abbasid dossier to move 1210 to 1229; or keep the decision and give the page's 1229 date in the notes so the abbasid side can correct its 1210. Not blocking.
- `/ledger/6/counterpart` [applied by reviewer] The 1216-17 Lahore gain named 'Yildiz of Ghazni', and the note said the page does not name the holder. The page does name him: Qabacha. Evidence: Iltutmish page: 'Yildiz migrated eastwards, displaced Qabacha from Lahore'; after Tarain 'He did not immediately assert his control over the Punjab region, and Qabacha regained control of Lahore'; 'Iltutmish then captured Lahore in the winter of 1216-1217'. Fix: Done: counterpart = 'Qabacha of Multan', note corrected.
- `/ledger/25/source` [applied by reviewer] The source was the Mamluk dynasty page, which names the Battle of Beas River but gives no year. The 9 March 1285 date is on the Balban page. Evidence: Mamluk dynasty (Delhi) page: 'He lost his favourite son Prince Muhammad in the Battle of Beas River against the Mongols' (no year). Balban page: 'he perished in a battle against the Mongols on 9 March 1285'. Fix: Done: source = Ghiyas_ud_din_Balban (already in sources[]).

Thin (for a gap-filler):

- `/keyframe_review/1` Lahore and the Punjab are drawn Mamluk for 1210-1215, but the Iltutmish page has Qabacha holding Lahore before Yildiz 'displaced' him, with no year. Who held Lahore under Aram Shah is undated. Try: https://en.wikipedia.org/wiki/Aram_Shah
- `/keyframe_review/6, /keyframe_review/7` The Malwa, Chittor and Chhattisgarh parts of the 1236 shape and the 48k km2 growth of 1250 rest on no page (5 of 5 pages used). Try: https://en.wikipedia.org/wiki/Nasiruddin_Mahmud
- `/ledger/20` The c. 1241 Mongol sack of Lahore is confidence 1 (dated only to Bahram's reign, 1240-1242). Try: https://en.wikipedia.org/wiki/Mongol_invasions_of_India
- `/ledger/24` The end of the Tughral revolt (1280) is confidence 1; the Balban page gives no year. Try: https://en.wikipedia.org/wiki/Tughral_Tughan_Khan

Spot checks:

- `/ledger/14` Iltutmish: confirmed (Uch 'on 4 May 1228'; Qabacha drowned 26 May 1228; Multan and Uch under his governors)
- `/ledger/10` Iltutmish: confirmed (Lakhnauti captured in 1227 by Nasiruddin)
- `/ledger/15` Iltutmish: confirmed ('on 12 December 1232')
- `/ledger/26` Ghiyas_ud_din_Balban: confirmed (Bughra 'declared independence after Balban's death'; Balban died 13 January 1287); counterpart wrong, see fixes
- `/ledger/6` Iltutmish: confirmed for the year (winter 1216-1217); wrong counterpart, corrected
- `/ledger/25` Mamluk_dynasty_(Delhi): mis-sourced (no year on the cited page); confirmed on the Balban page, and the source was corrected
- `/ledger/11` Mamluk_dynasty_(Delhi): confirmed ('finally incorporated into the Delhi Sultanate in 1227')

## kathmandu: fix

Area: infobox 899 km2 (None) vs Cliopatria 660.8 km2, ratio 0.74. The Kathmandu page is a city page; 899 km2 is the metropolitan area the author quotes (not re-read by the reviewer). The valley is within a factor of two.

Findings:

- `/keyframe_review/0/verdict` [applied by reviewer] The new keyframe kathmandu_1201 (from/to 1201 with a correction) had verdict ok. New keyframes elsewhere in the batch use adjust. Evidence: Schema: a correction is 'Required for adjust and wrong (and for a new keyframe)'; ok means 'the shape is right for its years as drawn'. Fix: Done: verdict = adjust.

Thin (for a gap-filler):

- `/keyframe_review/3, /keyframe_review/4` No page explains the single-cell shape changes of 1744 (-26 km2) and 1748 (+79 km2). This is thin by design: 4 shapes, 3 of 5 pages used, and Kingdom_of_Kathmandu failed to load. Try: https://en.wikipedia.org/wiki/Kingdom_of_Kathmandu
- `/ledger/3` Nuwakot under Kantipur by 1700 is confidence 1 (acquisition undated). Try: https://en.wikipedia.org/wiki/Nuwakot_Durbar
- `/ledger/2` The 1597 union with Patan has no matching loss for the later separation. The Malla page says 'After his death, Kathmandu and Patan were given to different grandsons and again separated' (no year). The whole-valley shape also holds Patan and Bhaktapur for 1482-1768, which the author flags as a grid limit. Try: https://en.wikipedia.org/wiki/Sivasimha_Malla

Spot checks:

- `/ledger/5` Unification_of_Nepal: confirmed ('capture the hill fort on September 26, 1744')
- `/ledger/7` Unification_of_Nepal: confirmed ('Shah took the city-state of Kathmandu in 1768'; 25 September 1768 is the proclamation of the Kingdom of Nepal, as the note says)
- `/ledger/1` Malla_dynasty_(Nepal): confirmed ('seizing Kathmandu in 1484')
- `/ledger/2` Malla_dynasty_(Nepal): confirmed ('conquered it in 1597 and united it with Kathmandu')

## pandya-empire: fail

Area: infobox None km2 (None) vs Cliopatria 220109.9 km2, ratio None. The author says the Pandya Empire (Pandya dynasty) page gives no area; not re-checked by the reviewer.

Findings:

- `/ledger (1220-1245)` [for the author] There is no vassal_start / vassal_end for the Hoysala hegemony over the Pandyas, 1220-1245. The dossier's own KF1 note quotes it, and hoysala-kingdom carries it. Evidence: KF1 note, Sundara II page (Sastri): 'from about 1220 to 1245', 'Pandyan inscriptions of the period record tribute paid to the Hoysala king'. hoysala-kingdom /ledger/20 (1220 vassal_start pandya-empire) and /ledger/24 (1245 vassal_end). Fix: Add vassal_start 1220 and vassal_end 1245, counterpart 'hoysala-kingdom', region = the Pandya country of those years, source Maravarman_Sundara_Pandyan_II, confidence 2.
- `/keyframe_review/6, /keyframe_review/7; /ledger (Nellore loss)` [for the author] KF7 (1290-1311) removes Nellore, but no ledger event loses it. kakatiya-dynasty also tells a different story: the Pandyas took Nellore in 1263, Naga-deva held it under Rudrama 1271-1275, and the Kakatiyas retook it in 1290 from the Telugu Chodas, not from the Pandyas. Evidence: kakatiya-dynasty /ledger/11-12 (1263), /ledger/13 and /ledger/16 (Naga-deva 1271-1275), /ledger/18 (1290 gain from telugu-chodas-of-nellore). The KF7 note says 'loss not dated by any page opened; mirror of the kakatiya-dynasty dossier, 1290', but that mirror has a different counterpart. Fix: Add a loss of Nellore with the year and counterpart the kakatiya dossier supports (by 1271 to kakatiya-dynasty or the Telugu Chodas, confidence 1), and end Nellore in KF6 at that year (new keyframe split). Or open the Muttukuru or Telugu Chodas page and settle it.
- `/ledger/14, /ledger/16 counterpart` [for the author] The occupation of Sri Lanka (1284-1309) names 'ceylon' as owner of the Dambadeniya outline. That land is kingdom-of-dambadeniya's until 1293, and its /ledger/2-3 record the occupation 1284-1293 against pandya-empire. ceylon opens its own occupation only in 1294 (/ledger/3). Neither mirror matches. Evidence: kingdom-of-dambadeniya /ledger/2 (1284 occupation_start pandya-empire), /ledger/3 (1293 occupation_end); ceylon /ledger/3 (1294 occupation_start), /ledger/4 (1309). Pandya Empire page: 'Sri Lanka remained under Pandya control until c. 1308-1309 CE.' Fix: Split into occupation_start/end of kingdom-of-dambadeniya 1284-1293 and of ceylon 1294-1309. If the two Sri Lankan dossiers are merged (see ceylon), use one pair naming the merged slug.
- `/ledger (c. 1317-1323)` [for the author] The Kakatiya occupation of Kanchi, which is Pandya land, has no mirror here. Evidence: kakatiya-dynasty /ledger/27 (c. 1317 occupation_start, counterpart pandya-empire, Kanchi) and /ledger/30 (1323 occupation_end). Fix: Add occupation_start 1317 and occupation_end 1323, counterpart 'kakatiya-dynasty', region Kanchipuram, confidence as on the neighbour.
- `/keyframe_review/7/verdict` [applied by reviewer] The new keyframe pandya-empire_1290 (from/to 1290-1311 with a correction) had verdict ok. Evidence: Schema: a correction is required 'for a new keyframe'; the batch's other new keyframes use adjust. Fix: Done: verdict = adjust.
- `/ledger/8/confidence` [applied by reviewer] Confidence 3 for the 1258 northern gain, whose region (Cliopatria's 1250-minus-1241 delta: Chidambaram, Cuddalore, Arcot, Chennai, Kanchipuram) is much wider than the place the page names. Evidence: Jatavarman Sundara Pandyan page: 'Pandyan forces killed the Telugu Choda ruler Vijaya Gandagopala of Nellore Chodas and captured Kanchipuram in 1258'; 'annexed Kanchi, Nellore and Visayavadai' has no year. Fix: Done: confidence 3 to 2. The chola-empire mismatch (by 1250) is in cross_checks.

Thin (for a gap-filler):

- `/ledger/1 to /ledger/7` The 1216-1241 events (the 1216-1217 war, Tirunelveli and Kerala 1220, Kongu 1236, the Kaveri delta 1241) are confidence 1; only Cliopatria years. Try: https://en.wikipedia.org/wiki/Maravarman_Sundara_Pandyan
- `/ledger/22, /ledger/23` The annexation as Ma'bar (end 1325) is confidence 1. Try: https://en.wikipedia.org/wiki/Muhammad_bin_Tughluq
- `/keyframe_review/9` 'he regained control of the South Arcot region by 1314' implies a loss of South Arcot before 1314. It is undated and not drawn. Try: https://en.wikipedia.org/wiki/Pandya_Empire

Spot checks:

- `/ledger/8` Jatavarman_Sundara_Pandyan: confirmed (1258, Kanchipuram; region broader than the page, so confidence lowered)
- `/ledger/19` Pandya_Empire: confirmed ('By 1312 the Pandya control over south Kerala was also lost')
- `/ledger/20` Pandya_Empire: confirmed ('In 1323, the Jaffna kingdom declared its independence')
- `/ledger/16` Pandya_Empire: confirmed ('Sri Lanka remained under Pandya control until c. 1308-1309 CE')
- `/ledger/17` Pandya_Empire: confirmed (March 1311; 'By late April 1311 ... returned to Delhi')
- `/ledger/12` Jatavarman_Sundara_Pandyan: confirmed (Someshwara's 'counteroffensive in 1262' ended in his death)

## ceylon: fail

Area: infobox None km2 (None) vs Cliopatria 62329.0 km2, ratio None. The wikipedia field is the modern country (Sri Lanka, about 65,610 km2, ratio about 0.95 with ceylon_1352); no historical infobox area exists.

Findings:

- `/identity; /identity/capitals/0, /identity/capitals/1` [for the author] One state is written as two dossiers. The author's own notes say the Ceylon and Dambadeniya rows 'tile one realm' (0 cells overlap; Ceylon has a hole at Kurunegala), and the research brief's rule is one dossier per state, with both Cliopatria Names and both rows' shapes. Because of the split, ceylon's capitals Dambadeniya (1236-1270) and Yapahuwa (1271-1283) lie outside ceylon's own shapes, in the hole drawn by the other row. Parakramabahu II, the Magha war, the Pandya invasions and the 1284 occupation are also told twice. Evidence: Capitals at 80.12 E 7.37 N and 80.34 E 7.82 N, inside the kingdom-of-dambadeniya_1236 bbox (79.74-80.56 E, 7.28-7.97 N), which ceylon_1236/_1260 leave as a hole (author's notes). Dambadeniya page: 'The kingdom's rulers reigned from 1220-1345'; capitals Dambadeniya, Yapahuwa, Polonnaruwa, Kurunegala, then 'Capital moved to Gampola: 1345'. The same line continues in ceylon. Fix: Merge kingdom-of-dambadeniya into this dossier (or the reverse; the orchestrator picks the slug). Start 1220, list both Cliopatria Names, review both rows' shapes, use the union of both rows for 1236-1293, and keep one set of rulers, wars and occupation events.
- `/keyframe_review/1 to /keyframe_review/2; /ledger (1294)` [for the author] The shape grows by 5.2k km2 from 1260 (68.3k) to 1294 (73.5k) as the Dambadeniya hole fills, and no ceylon event explains it. kingdom-of-dambadeniya /ledger/4 dissolves to ceylon in 1293, but ceylon has no gain or merge. Evidence: shapes.csv ceylon_1260 68,313 km2, ceylon_1294 73,532 km2. Rule 4: every change between keyframes needs a ledger event. Fix: Add a 1294 merge or gain, counterpart kingdom-of-dambadeniya, region {cliopatria: Kingdom of Dambadeniya, year: 1285}, confidence 1. This is not needed if the dossiers are merged.
- `/ledger/3` [for the author] The 1294 occupation_start by pandya-empire has no mirror. pandya-empire opens its occupation in 1284 and names ceylon as owner. See pandya-empire /ledger/14. Evidence: pandya-empire /ledger/14 (1284 occupation_start ceylon) and /ledger/16 (1309). Fix: Settle together with pandya-empire (a split at 1293/1294, or one pair after a merge).
- `/ledger/1` [for the author] The 1244 gain of Polonnaruwa from jaffna-kingdom is land the 1236 shape already holds. kingdom-of-polonnaruwa ends Magha's rule at Polonnaruwa in 1236 (/ledger/9). Evidence: Parakramabahu II page: 'successfully pushed Kalinga Magha out of Polonnaruwa by 1244' (a bound). kingdom-of-polonnaruwa /ledger/9: 'expelled from Polonnaruwa in 1236'. Fix: Move the event to 1236 (confidence 1, both pages in the note), or make it a contest_start 1236 / contest_end 1244 inside the shape. Not blocking.

Thin (for a gap-filler):

- `/ledger/2, /ledger/5, /ledger/7` Three border moves rest on Cliopatria years at confidence 1: the northern plains gained 1260 (+27k km2), lost 1314 (-23k) and regained 1352 (+12k). Try: https://en.wikipedia.org/wiki/Alakeshvara
- `/ledger/13` The 1506 end is confidence 1, from the Cliopatria row. The Kotte page keeps the kingdom to 27 May 1597. Try: https://en.wikipedia.org/wiki/Portuguese_Ceylon
- `/identity/capitals` There is no capital for 1284-1301. Try: https://en.wikipedia.org/wiki/Kingdom_of_Dambadeniya

Spot checks:

- `/ledger/10` Kingdom_of_Kotte: confirmed ('In 1450, through his conquest of the Jaffna Kingdom ... unifying the entire island')
- `/ledger/12` Kingdom_of_Kotte: confirmed (1469; the page adds 'a new kingdom in the central hill country')
- `/ledger/9` Kingdom_of_Kotte: confirmed (1412; the page also says 1415, as the note admits)
- `/ledger/11` Jaffna_kingdom: confirmed ('Aryacakravarti dynasty restored: 1467'; Kotte held it 1450-1467)
- `/ledger/1` Parakramabahu_II_of_Dambadeniya: confirmed ('pushed Kalinga Magha out of Polonnaruwa by 1244')

## kingdom-of-dambadeniya: fail

Area: infobox None km2 (None) vs Cliopatria 5219.2 km2, ratio None. No area in the Dambadeniya infobox (checked).

Findings:

- `/identity` [for the author] This is the same state as ceylon, drawn by Cliopatria as a second row. One dossier per state. Evidence: The ceylon finding above; the author's notes: 'one Sinhalese realm drawn as two rows'. The Dambadeniya page runs the same line of kings to 1345, past this dossier's 1293 end. Fix: Merge with ceylon. The one merge clears this dossier's fail and ceylon's first two findings.
- `/ledger/2, /ledger/3` [for the author] The 1284-1293 occupation by pandya-empire has no matching event on the Pandya side, which names ceylon as owner for 1284-1309. Evidence: pandya-empire /ledger/14, /ledger/16. Fix: Settle with pandya-empire (see there).
- `/keyframe_review/0/verdict` [applied by reviewer] The new keyframe kingdom-of-dambadeniya_1220 (1220-1235 with a correction) had verdict ok. Evidence: Schema: a correction is required 'for a new keyframe'. Fix: Done: verdict = adjust.

Thin (for a gap-filler):

- `/keyframe_review/1, /keyframe_review/2` The 5,219 km2 outline is unverified on the pages (2 of 2 pages used, within budget). Try: https://en.wikipedia.org/wiki/Dambadeniya
- `/ledger/3` The 1293 occupation end is confidence 1, from the row boundary. The page has the relic 'recovered in 1288 by Parakramabahu III (1287-1293)'. Try: https://en.wikipedia.org/wiki/Kingdom_of_Dambadeniya

Spot checks:

- `/ledger/2` Kingdom_of_Dambadeniya: confirmed for the 1284 invasion and the Tooth Relic; the page does not call it an occupation, which rests on the Pandya page (confidence 2 is fair)
- `/ledger/1` Kingdom_of_Dambadeniya: confirmed (infobox Yapahuwa 1271-1283; text 'transferred the capital to Yapahuwa in 1273')
- `/ledger/0` Kingdom_of_Dambadeniya: confirmed ('Fall of Polonnaruwa: 1220'; Vijayabahu III 1220-1224)
- `/wars/2` Parakramabahu_II_of_Dambadeniya: confirmed ('sometime between the years 1254 and 1256')

## Cross-dossier matrix (mismatches and missing mirrors)

- ghurid-dynasty 1182 vassal_start (counterpart soomra-dynasty) -> no mirror: missing soomra-dynasty exists (1026-1351) and has no Ghurid vassalage of 1182-1206 (nor the vassal_end of 1206).
- ghurid-dynasty 1198 gain (counterpart gahadavala-dynasty) -> gahadavala-dynasty 1194 dissolve: mismatch gahadavala-dynasty ends in 1194 (Chandawar) with ghurid-dynasty as successor; ghurid annexes Kannauj only in 1198 (Muhammad of Ghor page), and its 1192-1201 shape stops at 78.4 E, so the Gahadavala country is nobody's in 1194-1197. The author flags it. Route to sa-03: extend gahadavala to 1198 (Harishchandra, 1197 inscription) or ghurid adds a 1194 gain.
- kara-khitans 1198 vassal_end (counterpart Balkh vassal (the page does not name the holder)) -> no mirror: missing kara-khitans /ledger/14: Muhammad of Ghor seized Balkh in 1198; ghurid-dynasty has no Balkh gain (finding).
- ghurid-dynasty 1205 gain (counterpart sena-dynasty) -> sena-dynasty 1204 loss: mismatch Within a year (Nadia 1204), but the land disagrees: ghurid takes all of Bangladesh, while sena-dynasty lasts to 1230 in east Bengal (finding).
- ghurid-dynasty 1206 vassal_end (counterpart soomra-dynasty) -> no mirror: missing See 1182.
- paramara-dynasty 1233 occupation_start (counterpart mamluk-dynasty) -> mamluk-dynasty 1234 contest_start: mismatch paramara has a Mamluk occupation of Bhilsa 1233-1239; mamluk has a raid (contest) 1234-1235. The Iltutmish page says the army "occupied Bhilsa" (finding on mamluk).
- eastern-ganga-kingdom 1244 occupation_start (counterpart mamluk-dynasty) -> no mirror: missing Odia occupation of Rarh and Gauda 1244-1247; no mamluk event (finding).
- abbasid-caliphate 1210 vassal_start (counterpart mamluk-dynasty) -> no mirror: mismatch abbasid has Delhi allegiance 1210-1258 at confidence 1; mamluk has none; the Iltutmish page dates the investiture to 1228-1229. The abbasid side should move to 1229.
- mamluk-dynasty 1287 loss (counterpart sultanate-of-bengal) -> no mirror: mismatch sultanate-of-bengal is Cliopatria 1344-1533; Bughra Khan's Bengal of 1287 is a different state with no dossier (finding).
- hoysala-kingdom 1220 vassal_start (counterpart pandya-empire) -> no mirror: missing Hoysala hegemony 1220-1245; no pandya-empire vassal events (finding).
- pandya-empire 1258 gain (counterpart telugu-chodas-of-nellore) -> chola-empire 1250 loss: mismatch The northern zone (Chidambaram to Kanchipuram): chola-empire /ledger/39 loses it to the Pandyas "by 1250", while pandya-empire gains it in 1258 from the Telugu Chodas (no dossier, listed). 8 years apart; the author flags it.
- pandya-empire 1258 gain (counterpart telugu-chodas-of-nellore) -> kakatiya-dynasty 1263 loss: mismatch Nellore: kakatiya-dynasty /ledger/12 loses Nellore to the Pandyas in 1263 (Muttukuru); pandya says 1258. 5 years apart; the author flags it.
- pandya-empire 1284 occupation_start (counterpart ceylon) -> kingdom-of-dambadeniya 1284 occupation_start: mismatch The year matches dambadeniya, but pandya names ceylon as owner; ceylon opens its side only in 1294 (finding).
- kakatiya-dynasty 1290 gain (counterpart telugu-chodas-of-nellore) -> no mirror: mismatch pandya-empire KF7 drops Nellore in 1290 as the "mirror" of this event, but the kakatiya side takes Nellore from the Telugu Chodas, and pandya has no loss event (finding).
- kakatiya-dynasty 1317 occupation_start (counterpart pandya-empire) -> no mirror: missing Kakatiya occupation of Kanchi c. 1317-1323; no pandya event (finding).
- kingdom-of-dambadeniya 1293 dissolve (counterpart ceylon) -> no mirror: missing ceylon has no gain or merge in 1294 for the 5.2k km2 Dambadeniya row (finding).
- ceylon 1294 occupation_start (counterpart pandya-empire) -> pandya-empire 1284 occupation_start: mismatch 10 years apart; see pandya 1284.
- kingdom-of-dambadeniya 1284 occupation_start (counterpart pandya-empire) -> pandya-empire 1284 occupation_start: mismatch Same year, but pandya names ceylon as owner.
- kingdom-of-dambadeniya 1293 occupation_end (counterpart pandya-empire) -> no mirror: mismatch pandya ends the occupation in 1309 with counterpart ceylon.

Matched: ghurid-dynasty 1192 gain/chauhan-dynasty; ghurid-dynasty 1192 vassal_start/chauhan-dynasty; ghurid-dynasty 1194 vassal_end/chauhan-dynasty; ghurid-dynasty 1197 occupation_start/chaulukya-dynasty; ghurid-dynasty 1200 gain/sena-dynasty; ghurid-dynasty 1201 occupation_end/chaulukya-dynasty; ghurid-dynasty 1203 occupation_start/chandela-kingdom; ghurid-dynasty 1205 occupation_end/chandela-kingdom; ghurid-dynasty 1206 loss/mamluk-dynasty; pandya-empire 1216 vassal_start/chola-empire; pandya-empire 1217 vassal_end/chola-empire; pandya-empire 1241 gain/chola-empire; pandya-empire 1258 vassal_start/chola-empire; pandya-empire 1262 gain/hoysala-kingdom; pandya-empire 1279 vassal_end/chola-empire; pandya-empire 1295 loss/hoysala-kingdom; pandya-empire 1309 occupation_end/ceylon; ceylon 1309 occupation_end/pandya-empire.

The other rows are exceptions: free-string local rulers, counterparts the author lists as needing dossiers, and states whose group has not run yet (see the JSON).

## Problems and routing

- ceylon and kingdom-of-dambadeniya are one state in two dossiers. The author left the merge to the orchestrator; I fail both on it. One merge (orchestrator picks the slug) clears the structural findings of both and simplifies the pandya-empire occupation fix.
- ghurid-dynasty /ledger/34 and /ledger/40 cited Khwarazmian_Empire for a sentence that is only on Ghurid_dynasty. The event is true and the page is in sources[], so I corrected the source rather than treating it as fabricated.
- Edits applied in place (each tagged '[Reviewer sa-04-a: ...]', the five edited files re-validated with 0 errors and read back): ghurid-dynasty /ledger/14,16,17 counterpart, /ledger/34,40 source, /ledger/26,29 confidence; mamluk-dynasty /ledger/6 counterpart, /ledger/25 source; kathmandu /keyframe_review/0 verdict; pandya-empire /keyframe_review/7 verdict, /ledger/8 confidence; kingdom-of-dambadeniya /keyframe_review/0 verdict. The author's report (keyframe_verdicts, low_confidence_events) is now slightly stale.
- Neighbour dossiers not yet written (counted as groups not yet run): jaffna-kingdom, gorkha-kingdom, great-seljuk-empire, khwarezmid-dynasty, khwarezmid-empire, ghaznavid-empire, hamdanid-emirates, khalji-dynasty, tughlaq-dynasty, sultanate-of-bengal, portuguese-ceylon.
- Routed to other groups: soomra-dynasty lacks the Ghurid vassalage 1182-1206; gahadavala-dynasty ends 1194, against Kannauj 1198 (sa-03); abbasid-caliphate dates the Delhi allegiance to 1210 at confidence 1, while the Iltutmish page has 1228-1229; kingdom-of-polonnaruwa successors omit ceylon (sa-03); gorkha-kingdom must hold the valley back to 1768 (sa-05).
- No page failed to load for me. Pages not re-read: Kathmandu (city), Maravarman_Sundara_Pandyan_II, Rajaraja_Chola_III, Madurai_Sultanate, Kingdom_of_Gampola (budget).

## Counterparts needing dossiers

- Qabacha of Multan (`qabacha-of-multan`) [1206, 1228] 
- Yildiz of Ghazni (`yildiz-of-ghazni`) [1206, 1216] Only if ghurid-dynasty takes reading (a) of the Ghazni finding; otherwise drop it.
- Khalji dynasty of Bengal (Iwaz) (`khalji-dynasty-of-bengal`) [1204, 1227] 
- Chahamanas of Ranastambhapura (`chahamanas-of-ranastambhapura`)  
- Telugu Chodas of Nellore (`telugu-chodas-of-nellore`)  
- Kingdom of Lalitpur (Patan) (`kingdom-of-lalitpur`) [1482, 1768] 
- Kingdom of Bhaktapur (`kingdom-of-bhaktapur`) [1482, 1769] 
- Kandyan kingdom (Senkadagala) (`kingdom-of-kandy`) [1469, 1815] 
- Bughra Khan's Bengal (Balbani rulers of Lakhnauti) (`balbani-sultanate-of-bengal`) [1287, 1327] Balban page: Bughra 'declared independence after Balban's death, which he maintained for 40 years'; replaces sultanate-of-bengal as mamluk-dynasty's 1287 counterpart.
