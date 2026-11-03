# Review of batch ia-01-f (2026-10-19)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/ia-01-f.json. Validator: 0 errors on all six dossiers (warnings: counterpart slugs with no dossier yet; Uyghur rulers 841-848 and war 841-848 outside the life; Ganzhou war 874 outside the life).

| slug | verdict | why |
| --- | --- | --- |
| uyghur-khaganate | thin | events confirmed; 2 confidence levels and 1 slug fixed by the reviewer; 757/793 steps undated, Dzungaria placeholder too wide, rulers/war after 840 |
| qarlugs | thin | the vassal pair 746-766 is missing (mirror of uyghur ledger 2/6); the 789 Dzungaria placeholder is too wide |
| kara-khanids | fail | keyframe_review/6 adds Kashgar to the 896-959 shape although the ledger gains it in 934 |
| ganzhou-kingdom | thin | the 961 Song suzerainty (dated on the page) is missing; the 874 war lies outside the life |
| qocho-kingdom | fail | 1128 is a vassalage, not a dissolution (infobox: independent 843-1132, vassal to the 14th century); keyframe_review/4 drops Kucha/Aksu from 1040, not 1096 |
| kingdom-of-khotan | thin | events confirmed; pre-851 kingdom unmapped; extent (Aksu, Alay) unverified; ruler 844 before the start |

## uyghur-khaganate: thin

Area: infobox 3100000 (800), Cliopatria max/near 3027888 km2, ratio 0.98.

Findings:
- `/ledger/3/confidence` (applied by reviewer): The 751 gain of Turfan from the Tang was confidence 2, but the page gives no year for the handover. Evidence: Uyghur Khaganate page, footnote: the area 'around Turfan came under the control of the Uighurs' after Talas; WebFetch: 'the footnote gives no separate year for Turfan'. The Tang example (L46) keeps Turfan and Beiting to c. 790, when they go to Tibet, and this ledger takes Gaochang from Tibet in 792 with no loss to Tibet in between. Fix: Lowered to 1 and the conflict noted in the event's note. The author should drop the 751 gain or make it a vassal/hegemony event, so that the Tang 790 loss to Tibet and the 792 Uyghur gain from Tibet fit together.
- `/ledger/10/confidence` (applied by reviewer): The 792 gain was confidence 3 for the region Turfan-Hami, but the page names only Gaochang. Evidence: Uyghur Khaganate page: 'In 792, the Uyghurs, led by Qutluq's son Baoyi Qaghan, defeated the Tibetans and Karluks, taking Gaochang.' Hami is not named. Fix: Lowered to 2 (brief rule 7).
- `/wars/0/belligerents, /wars/3/belligerents` (applied by reviewer): Mis-typed slug 'karluks'; the Karluk dossier is 'qarlugs'. Evidence: history/polities/qarlugs.json is the Karluk Yabghu dossier in this batch. Fix: Replaced 'karluks' with 'qarlugs' in both wars.
- `/identity/rulers/12, /identity/rulers/13, /wars/5` (for the author): Wujie (841-846), Enian (846-848) and the 841-848 Tang-Uyghur war fall outside the state's life (744-840). The validator warns about all three. Evidence: Brief check 2: rulers and wars must fall inside the life. The KF8 note itself says the remnants held no land. Fix: Move the two rulers into the keyframe_review/8 note or the notes field, and leave the 841-848 war to the tang-dynasty dossier (ea-04).
- `/ledger/8/region` (for the author): The 789 loss of the unlocated 'Futu Valley' takes away the whole of Dzungaria, Beshbalik included. Evidence: Uyghur page: 'The Karluks ... annexed Futu Valley' (789), with no location. This same ledger contests Dzungaria with Tibet in 790, and the Uyghurs beat the Karluks at Beiting in 791. The qarlugs 793 keyframe does not hold Dzungaria, and no qarlugs event loses it. Fix: Narrow the region to a small placeholder (a place radius in western Dzungaria/Tarbagatai, confidence 1, page silent on location), the same in qarlugs /ledger/3.
- `/certainty/0/note` (for the author): The certainty note does not name the 821/822 Tibet-Uyghur treaty that the sources entry cites. Evidence: The sources[] note for Tibetan_Empire mentions 'the 821/822 treaty'. Brief check 10: certainty notes name the treaty borders. Fix: Name the 821/822 treaty in the certainty note (no line is given, so the level stays soft).

Gaps for a gap-filler:
- `/keyframe_review/3`: Who or what explains the 757 step into Dzungaria and the northern Tarim (+1,759 cells, unverified: page budget), and the 793 drop of western Dzungaria and the Tianshan (-2,980 cells) (try https://en.wikipedia.org/wiki/Beiting_Protectorate)
- `/ledger/4`: A dated Turgesh submission to the Uyghurs (755 is Cliopatria's step; confidence 1). The turgesh dossier carries no matching vassal_start (try https://en.wikipedia.org/wiki/Turgesh)
- `/ledger/6`: The end of Uyghur overlordship over the Karluks (766 is a bridge; confidence 1) (try https://en.wikipedia.org/wiki/Karluks)
- `/ledger/8`: The location of the Futu (Fu-tu) valley annexed by the Karluks in 789 (try https://en.wikipedia.org/wiki/Shatuo)
- `/ledger/11`: The end of the Tibet contest (808 is the last dated gain; confidence 1). The 808 'seized Liang Province' is recorded only as a contest end (try https://en.wikipedia.org/wiki/Tibetan_Empire)
- `/ledger/0, /ledger/1`: The 744-745 founding rests on the Uyghur page alone; the Second Turkic Khaganate page was not opened (try https://en.wikipedia.org/wiki/Second_Turkic_Khaganate)

Spot checks: /ledger/1 confirmed: 'In 745, the Uyghurs killed the last khagan of the Göktürks, Kulun Beg'; /ledger/2 confirmed: Bilge Yabghu Tun Apa Yigen Chor 'submitted to the Uyghur Khaganate in 746'; /ledger/5 confirmed: 'In 758, the Uyghurs turned their attention to the northern Yenisei Kyrgyz'; /ledger/8 confirmed year (paragraph 'In 789'); no location given; /ledger/9 confirmed: 'In 790, the Uyghurs and Tang forces were defeated by Tibetan Empire at Tingzhou'; /ledger/10 confirmed year 792 (Gaochang; 803 again); the region is broader than the page, so confidence was lowered to 2; /ledger/14 confirmed: infobox 'Disestablished: 840'; 'they sacked Ordu-Baliq, razing it to the ground'; /ledger/3 footnote confirmed, but it gives no year: confidence lowered to 1

## qarlugs: thin

Area: infobox None (None), Cliopatria max/near 407815 km2, ratio None.

Findings:
- `/ledger` (for the author): The Uyghur overlordship of 746-766 is missing from this ledger, though uyghur-khaganate /ledger/2 and /ledger/6 carry it with counterpart qarlugs. Evidence: Brief check 3: a vassal_start of X must be a vassal_start in X's ledger with this state as counterpart. Karluk Yabgu page: Bilge Yabghu Tun Apa Yigen Chor 'submitted to the Uyghur Khaganate in 746'. The author's notes say this was left to the Uyghur ledger on purpose. Fix: Add a vassal_start at 746 (counterpart uyghur-khaganate, region = keyframe_review/0's homeland, confidence 3, source Karluk_Yabgu_State) and a vassal_end at 766 (confidence 1, bridging), mirroring the Uyghur events.
- `/ledger/3/region` (for the author): The 789 gain of the unlocated Futu Valley takes all of Dzungaria. No later event loses it, and the 793 keyframe does not hold it. Evidence: Uyghur page: 'annexed Futu Valley' with no location; the Karluks were beaten at Beiting in 791 (Uyghur page). Fix: Narrow to a small placeholder region (confidence 1), the same as uyghur-khaganate /ledger/8.

Gaps for a gap-filler:
- `/keyframe_review/0`: The 742-765 homeland is a proxy (East Kazakhstan plus Tacheng 200 km); the pages give 'between the Altai and the eastern shore of Lake Balkhash' / 'Kara-Irtysh and the Tarbagatai' (try https://en.wikipedia.org/wiki/Karluks)
- `/ledger`: The Fergana lands the Karluks lost after Talas ('The Arabs dislodged the Karluks from Fergana', undated) are not drawn (try https://en.wikipedia.org/wiki/Battle_of_Talas)

Spot checks: /ledger/0 confirmed: 'In 742, they were named "Saɣ Yabghu" by Basmyl khagan Ashina Shi'; /ledger/1 confirmed: 'By 766, the Karluks had forced the submission of the Turgesh'; Karluks page: overran the Türgesh in Jetisu, capital to Suyab; /ledger/3 confirmed year 789; location not on page; /ledger/4 confirmed: 'When the Yenisei Kyrgyz destroyed the Uyghur Khaganate in 840, Karluk yabghu declared himself khagan ... forming the Kara-Khanid Khanate'

## kara-khanids: fail

Area: infobox None (None), Cliopatria max/near 1310698 km2, ratio None.

Findings:
- `/keyframe_review/6/correction` (for the author): The correction adds Kashgar (200 km) to the whole 896-959 shape, so Kashgar is drawn from 896, though the ledger gains it in 934 (/ledger/2) and the correction's own text says 'from 934'. Evidence: A correction describes the whole shape for the keyframe's span (research brief, region grammar). The 896 shape has no Kashgar (bbox south edge 41.0 N, Kashgar about 39.5 N). Kara-Khanid page: Satuq Bughra Khan 'converted to Islam in 934 and then captured Kashgar'. About 125,000 km2 are drawn 38 years early, on a 409,000 km2 shape. Fix: Drop the Kashgar term from keyframe_review/6 (verdict ok, or adjust with a years-only text) and let /ledger/2 add Kashgar in 934. Alternatively split the keyframe at 934 with from/to. keyframe_review/7 (960) keeps Kashgar, which is right.

Gaps for a gap-filler:
- `/ledger`: The Kara-Khanid invasion of Khorasan (1006) and the defeat near Balkh (1008) against the Ghaznavids: an occupation pair and a war are missing; there are also no Kara-Khanid-Ghaznavid frontier events up to 1045 (try https://en.wikipedia.org/wiki/Ghaznavids)
- `/ledger/4`: The year Kashgar returned from Khotan (971 is a bridge; confidence 1) (try https://en.wikipedia.org/wiki/Tarim_Basin)
- `/ledger/9, /ledger/10`: The year of the split ('the 1040s'; 1045 is Cliopatria's, confidence 1) (try https://en.wikipedia.org/wiki/Seljuk_Empire)
- `/keyframe_review/1`: Who held Kashgar and the west Tarim 850-933 (the corrections leave them nobody's) (try https://en.wikipedia.org/wiki/Tarim_Basin)
- `/identity`: Ruler list and Uzgen/Kashgar capitals (try https://en.wikipedia.org/wiki/Kara-Khanid_Khanate)

Spot checks: /ledger/0 confirmed: infobox 'Established: 840'; /ledger/2 confirmed: 'converted to Islam in 934 and then captured Kashgar' (also 932 in the dynasty list); /ledger/5 confirmed: 'Between 990 and 992, Hasan took Isfijab, Ferghana, Ilaq, Samarkand, and the Samanid capital Bukhara'; /ledger/6 confirmed: 'by 999 Ali's son Nasr had taken Chach, Samarkand, and Bukhara'; /ledger/8 confirmed: 'In 1006, Yusuf Qadir Khan of Kashgar conquered the Kingdom of Khotan'; /ledger/9 confirmed: 'split into the Eastern and Western Khanates in the 1040s' (1045 rightly confidence 1)

## ganzhou-kingdom: thin

Area: infobox None (None), Cliopatria max/near 233037 km2, ratio None.

Findings:
- `/ledger` (for the author): The Song suzerainty of 961 is missing; it is dated on the page and the dossier's own notes give it. Evidence: Ganzhou page: 'In 961 the Ganzhou Uyghurs accepted the Song dynasty as suzerains.' Research brief rule 4: tributaries and clients are vassal events in both ledgers. northern-song exists in polities.csv (961-1138). Fix: Add a vassal_start at 961 (counterpart northern-song, region = the Cliopatria Ganzhou 926 shape, confidence 3) and a vassal_end at 1036 (confidence 2, at annexation).
- `/wars/0` (for the author): The 874 Wenmo war lies outside the state's life (894-1036) and lists ganzhou-kingdom as a belligerent before it existed. The validator warns. Evidence: Ganzhou page: the Wenmo 'drove out the Uyghurs' in 874; the kingdom was 'established' in 894. Fix: Move the war to the notes, or to the predecessor's note on identity.

Gaps for a gap-filler:
- `/ledger`: The 911 subordination of the Jinshan Kingdom to Ganzhou ('forced them into an alliance as a lesser partner'): possibly a vassal_start of jinshan-kingdom 911-914 (try https://en.wikipedia.org/wiki/Guiyi_Circuit)
- `/ledger/2`: Whether Liangzhou was held after 1009 (1010 is a bridge; confidence 1) (try https://en.wikipedia.org/wiki/Western_Xia)
- `/keyframe_review/1`: The kingdom's extent (Suzhou, Guazhou) against Cliopatria's static 978-cell shape (try https://en.wikipedia.org/wiki/Guiyi_Circuit)

Spot checks: /ledger/0 confirmed: 'In 894 the Uyghurs led by Pangteqin (Huaijian Khagan) established the Ganzhou Uyghur Kingdom in Ganzhou'; /ledger/1 confirmed: 'In 1009 the Ganzhou Uyghurs captured Liangzhou'; /ledger/3 confirmed: 'In 1028 the Ganzhou Uyghurs were defeated by the Tanguts'; /ledger/4 confirmed: 'In 1036 the Ganzhou Uyghur Kingdom was annexed by the Tanguts'; infobox 'Disestablished: 1036'

## qocho-kingdom: fail

Area: infobox None (None), Cliopatria max/near 653223 km2, ratio None.

Findings:
- `/ledger/6` (for the author): The 1128 event is typed 'dissolve' (confidence 3) and the life ends in 1128, but the page has the kingdom becoming a vassal in 1128 and lasting to the 14th century. Evidence: Qocho page: 'In 1128, the Kingdom of Qocho became a vassal of the Qara Khitai'. Infobox: 'Independent state (843–1132)', 'Vassal state of the Western Liao (1132–1209)', 'Vassal state of the Mongol Empire (1209–1335)', 'Disestablished: 14th century'; 'By the 1370s, the Kingdom of Qocho ceased to exist.' Research brief rule 4: vassals are a lighter tint, not an end. As written, Cliopatria's own Qocho shape for 1129-1138 belongs to no one. Fix: Make /ledger/6 a vassal_start (1128, counterpart kara-khitans, confidence 3; note that the infobox says 1132). Extend identity.end at least to Cliopatria's 1138, and better to the 14th century with new keyframes (the corrected 1126 shape, from/to), a vassal_end/vassal_start in 1209 to mongol-empire and later chagatai-khanate, and the dissolve at the end. Give keyframe_review/5 the whole 1126-1138 span.
- `/keyframe_review/4/correction` (for the author): The correction removes Kucha and Aksu from the whole 1040-1125 shape, while /ledger/5 dates the loss to 1096 and the note says 'from 1096'. Evidence: A correction describes the whole shape for its span. Qocho page: 'By 1096, Qocho had lost Aksu, Tumshuk, and Kucha to the Kara-Khanid Khanate.' As written, Kucha is nobody's in 1040-1095: the Kara-Khanid shapes do not overlap the Qocho shape (0 shared cells). Fix: Use the 888-style correction for keyframe_review/4 (minus Gansu, plus Hami) and let the 1096 loss remove Kucha and Aksu. keyframe_review/5 (1126) keeps the minus.
- `/keyframe_review/1` (for the author): The Cliopatria 860 keyframe overlaps the new keyframe 843-865 in 860-865; only its note says the shape holds from 866. Evidence: keyframe_review/0 has from 843, to 865. Fix: State in the correction text that the 860 shape applies from 866, keyframe 0 covering 860-865.
- `/wars/2/belligerents` (applied by reviewer): In the 1096 war the slug 'kara-khanids' (the unified khanate, ended 1045) is used where the counterpart of /ledger/5 is eastern-kara-khanids. Evidence: /ledger/5 counterpart eastern-kara-khanids; kara-khanids.json ends in 1045. Fix: Replaced with eastern-kara-khanids.

Gaps for a gap-filler:
- `/keyframe_review/1`: Who held Aksu before 1096: Cliopatria gives it to Khotan 888-1009, and the Qocho page has Qocho losing it 'by 1096' (try https://en.wikipedia.org/wiki/Tarim_Basin)
- `/ledger`: The vassal centuries 1128-1370s (Qara Khitai, Mongols 1209, Chagatai) (try https://en.wikipedia.org/wiki/Qara_Khitai)

Spot checks: /ledger/0 confirmed: 'In 843, a group of Uyghurs migrated southward under the leadership of Pangtele, and occupied' Karasahr and Kucha; /ledger/1 confirmed: 866 captures of Xizhou, Tingzhou, Changbaliq and Luntai from the Guiyi Circuit; /ledger/2 confirmed: 876 'the Kingdom of Qocho seized Yizhou'; /ledger/3 confirmed: 904 Zhang Chengfeng seized Yizhou and Xizhou; ended after 911; /ledger/5 confirmed: 'By 1096, Qocho had lost Aksu, Tumshuk, and Kucha'; /ledger/6 year confirmed (1128), but the page says vassal, not dissolution: the event is mis-typed

## kingdom-of-khotan: thin

Area: infobox None (None), Cliopatria max/near 302510 km2, ratio None.

Findings:
- `/identity/rulers/0` (for the author): Viśvānanda's reign starts in 844, before the state's 851 start. Evidence: Brief check 2: rulers inside the life. Khotan page king list: 'Viśvānanda (Viśa' Nanta) - 844'. Fix: Start the entry in 851 and keep 844 in its note, or extend the dossier backwards (see thin).

Gaps for a gap-filler:
- `/identity/start`: The kingdom before 851 (infobox 'established c. 300 BC'; 'Khotan was taken by the Tibetan Empire in 792'; infobox 'Tibet invades and conquers Khotan: 670'): the Tang and Tibetan years need keyframes and occupation/vassal events (try https://en.wikipedia.org/wiki/Kingdom_of_Khotan)
- `/keyframe_review/1`: The extent 851-1006. The page calls Khotan in the 10th century 'the only city-state in the Tarim Basin that was not yet conquered' by Qocho or the Kara-Khanids, yet the shape keeps Aksu (Qocho's before 1096 on the Qocho page) and the Alay cells (try https://en.wikipedia.org/wiki/Tarim_Basin)
- `/ledger/2`: The year Kashgar was lost again after 970 (971 is a bridge; confidence 1) (try https://en.wikipedia.org/wiki/Tarim_Basin)

Spot checks: /ledger/0 confirmed: 'Khotan was taken by the Tibetan Empire in 792' and 'would go on to gain its independence in 851'; /ledger/1 confirmed: 'Khotan briefly took Kashgar from the Kara-Khanids in 970'; /ledger/3 confirmed: 'In 1006, the Muslim Kara-Khanid ruler Yusuf Kadir (Qadir) Khan of Kashgar conquered Khotan'; /ledger/4 confirmed: infobox 'Disestablished: 1006'

## Cross-dossier matrix

- uyghur-khaganate 745 gain (second-turkic-khaganate) -> -: exception No dossier yet; listed in the author's counterparts_needing_dossiers (ia-01-c or ia-01-x).
- uyghur-khaganate 746 vassal_start (qarlugs) -> -: missing qarlugs has no vassal_start 746 / vassal_end 766 with counterpart uyghur-khaganate (same batch; fix listed).
- uyghur-khaganate 751 gain (tang-dynasty) -> -: exception tang-dynasty is ea-04 and not run yet. Disagreement to settle: the Tang example (L46) loses Dzungaria and Turfan-Hami to Tibet c. 790, not to the Uyghurs in 751. The Uyghur event was lowered to confidence 1.
- uyghur-khaganate 755 vassal_start (turgesh) -> -: missing turgesh.json (ia-01-e) has no vassal_start with counterpart uyghur-khaganate. The Uyghur side is confidence 1; route to the turgesh author or a gap-filler.
- uyghur-khaganate 758 vassal_start (yenisei-kyrgyz) -> -: missing yenisei-kyrgyz.json (ia-01-c) has no 758 vassal_start (counterpart uyghur-khaganate); its 763 loss to nobody is Cliopatria's gap. The Yenisei Kyrgyz page: 'the Kyrgyz came under the rule of the Uyghur Khaganate' (758).
- uyghur-khaganate 766 vassal_end (turgesh) -> turgesh 766 dissolve: mismatch turgesh dissolves in 766 (loss to qarlugs) but never opened the vassal relation.
- uyghur-khaganate 789 loss (qarlugs) -> qarlugs 789 gain: matched Matched in year and region (Dzungaria, both confidence 1); the region is an overreach on both sides.
- uyghur-khaganate 792 gain (tibetan-empire) -> -: exception tibetan-empire is ea-04 and not run yet.
- uyghur-khaganate 840 vassal_end (yenisei-kyrgyz) -> -: missing yenisei-kyrgyz has no vassal pair; see 758.
- uyghur-khaganate 840 loss (yenisei-kyrgyz) -> yenisei-kyrgyz 840 gain: matched Kyrgyz L2 840 gain uyghur-khaganate (Orkhon), confidence 3.
- qarlugs 766 gain (turgesh) -> turgesh 766 loss: matched turgesh L12 766 loss qarlugs, Semirechye.
- qarlugs 789 gain (uyghur-khaganate) -> uyghur-khaganate 789 loss: matched 
- kara-khanids 893 loss (samanid-empire) -> -: exception samanid-empire is me-08 and not run yet.
- kara-khanids 934 gain (nobody) -> -: exception Counterpart nobody (the page does not say who held Kashgar). The Khotan dossier leaves Kashgar out for 851-1006, which is consistent.
- kara-khanids 970 contest_start (kingdom-of-khotan) -> kingdom-of-khotan 970 contest_start: matched Pair 970-971 on both sides.
- kara-khanids 999 gain (samanid-empire) -> -: exception me-08 not run yet.
- kara-khanids 1006 gain (kingdom-of-khotan) -> kingdom-of-khotan 1006 loss: matched Khotan 1003 shape against the 1000 shape: the cells are identical.
- kara-khanids 1045 split (eastern-kara-khanids) -> -: exception eastern-kara-khanids and western-karakhanid-khanate belong to other ia-01 parts that have not run yet.
- qarlugs 840 dissolve (kara-khanids) -> kara-khanids 840 found: matched Continuity 840; the reviewer keeps two dossiers (two Wikipedia articles and Wikidata ids), but the colour agent should relate them.
- ganzhou-kingdom 1036 loss (western-xia) -> -: exception western-xia is ea-05 and not run yet; western-xia should carry a 1036 gain, the 1028-1036 contest, and the end of the northern-song vassalage.
- ganzhou-kingdom 961 vassal_start (northern-song) -> -: missing Not in either ledger: the page dates it (961); the Ganzhou fix is listed; northern-song (ea) should mirror it.
- qocho-kingdom 866 gain (guiyi-circuit) -> -: exception guiyi-circuit has no dossier and is listed in counterparts_needing_dossiers. Consistent with the Tang example: L51 has Zhang take Xizhou in 851.
- qocho-kingdom 876 gain (guiyi-circuit) -> -: exception As above.
- qocho-kingdom 904 occupation_start (guiyi-circuit) -> -: exception As above; 904-911.
- qocho-kingdom 1096 loss (eastern-kara-khanids) -> -: exception eastern-kara-khanids not run yet; it should carry a gain of Kucha and Aksu by 1096.
- qocho-kingdom 1128 dissolve (kara-khitans) -> -: mismatch This should be a vassal_start (Qocho page). kara-khitans (ia-01-g, not run) must carry a vassal_start in 1128/1132 naming qocho-kingdom.

## Other notes

- No page failed to load for the reviewer. The author's report already lists Karluk_Yabghu_State as a 404 (Karluk_Yabgu_State works).
- Neighbour dossiers read: yenisei-kyrgyz, turgesh, turks, kimek-kipchak-confederation (exist). Missing and owned by groups that have not run: samanid-empire, tibetans, abbasid-caliphate, tang-dynasty (the worked example was used for the Tang), tibetan-empire, western-xia, liao-dynasty, eastern-kara-khanids, ghaznavid-empire, lohara-dynasty, seljuk-dynasty, kashmir, kara-khitans, great-seljuk-empire, utpala-dynasty.
- Routing: yenisei-kyrgyz (ia-01-c) needs a 758-840 vassal pair with counterpart uyghur-khaganate; turgesh (ia-01-e) needs a 755-766 vassal relation to uyghur-khaganate, or the Uyghur event should be dropped.
- Qarlugs and Kara-Khanids: the Karluk Yabghu page says the 840 title change 'formed the Kara-Khanid Khanate'. The reviewer keeps two dossiers (two Wikipedia articles, two Wikidata ids, the Kara-Khanid infobox 'Established: 840') but the colour agent should give them related hues.
- Applied reviewer edits: uyghur-khaganate (ledger 3 and 10 confidence, wars 0 and 3 slug) and qocho-kingdom (wars 2 slug); both re-validated with 0 errors and read back.
