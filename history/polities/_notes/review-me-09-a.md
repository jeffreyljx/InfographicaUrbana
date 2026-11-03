# Review: batch me-09-a

Adversarial review by the Phase B reviewer, 2026-10-25. Dossiers: seljuk-dynasty, great-seljuk-empire, danishmendids, khwarezmid-dynasty. The validator (with --resolve) passes all four with 0 errors; great-seljuk-empire keeps 2 warnings for kerman-seljuk-sultanate (no dossier yet, listed). The machine copy of this review is history/notes/phase-b/reviews/me-09-a.json.

Verdicts: seljuk-dynasty **thin**, great-seljuk-empire **fail**, danishmendids **thin**, khwarezmid-dynasty **thin**. Fixes marked "applied" were made by the reviewer in the dossier (each carries a "[Reviewer me-09-a ...]" note) and re-validated; the rest are for the author or a gap-filler.

## seljuk-dynasty: thin

Validates; 4 events spot-checked: 3 confirmed, 1 mis-dated at confidence 1 (the Dihistan-Nasa-Farawa cession, 1034 -> 1035, fixed by the reviewer). Reviewer also clipped the war to the dossier's end. Left thin by design (budget 1-2 pages): four confidence-1 events and an unmatched 1037 loss to oghuz-turks.

Area: infobox None km2 (None), Cliopatria 822986 km2, ratio None, acknowledged True. The Seljuk dynasty infobox gives no area; the dossier says so.

### Findings

- `/ledger/2 (was /ledger/1)` (applied by reviewer): The cession of Dihistan, Nasa and Farawa is dated 1034 (the Cliopatria shape year), but the page puts it after the 1035 events. Evidence: Battle of Dandanaqan page: the Seljuks settled in Khwarazm under Harun in 1034; in 1035 Harun was murdered and they fled to Nasa; Iltughdi's army was beaten there; then 'Ma'sud entitled the Seljuk to three cities in Khurasan: Dihistan, Nasa, and Farawa'. Fix: Year 1034 -> 1035, moved after the 1035 contest_start, note extended; confidence stays 1. ghaznavid-empire /ledger/26 (1034) stays within one year.
- `/wars/0/to` (applied by reviewer): The war runs to 1040, after the dossier's end (1039). Evidence: Brief rule: wars inside the life; the dissolve is 1039 and great-seljuk-empire carries the 1040 battle. Fix: to 1040 -> 1039.
- `/ledger/5` (NOT applied): 1037 loss of the Syr Darya range to oghuz-turks (confidence 1) has no mirror: oghuz-turks has no 1037 gain, and its own ledger has a 1034-1043 contest with seljuk-dynasty in Khwarezm that this dossier lacks. Evidence: oghuz-turks /ledger/4 (1034 contest_start, cp seljuk-dynasty), /ledger/7 (1043 contest_end, cp seljuk-dynasty, after this dossier's end); the Seljuk dynasty page has Tughril abandon Cend in 1016 and names no later holder. Fix: Either drop the counterpart to 'nobody' (the clan left the range) or route the gain to ia-01; add the 1034-1035 Khwarezm contest with oghuz-turks if a page supports it (the Dandanaqan page does not name Shah Malik).

### For a gap-filler

- `/ledger/2`: A dated page for the cession of Dihistan, Nasa and Farawa (now 1035, confidence 1). Try https://en.wikipedia.org/wiki/Chaghri_Beg
- `/ledger/5`: Who held the lower Syr Darya after the Seljuks left Cend (confidence 1). Try https://en.wikipedia.org/wiki/Oghuz_Yabgu_State
- `/ledger/6`: Contest end 1039 is a placeholder (confidence 1); the war ends at Dandanaqan 1040 in great-seljuk-empire. Try https://en.wikipedia.org/wiki/Battle_of_Dandanaqan
- `/ledger/7`: Dissolve/hand-over 1039|1040 to great-seljuk-empire is a Cliopatria cut (confidence 1); the Seljuk Empire page dates the formation to 1037. Orchestrator may merge the two rows into one dossier (same state). Try https://en.wikipedia.org/wiki/Seljuk_Empire

### Spot checks

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Seljuk_dynasty)
- `/ledger/2`: mis-dated (https://en.wikipedia.org/wiki/Battle_of_Dandanaqan)
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Seljuk_dynasty)
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Seljuk_Empire)

## great-seljuk-empire: fail

Validates; 10 events checked on 7 pages, all dated correctly, no fabricated event; two counterparts were wrong although the page names the holder (Ray 1043, Mosul 1057) and the reviewer fixed them, with the 1153-1157 Oghuz counterpart and two out-of-life years. Fails on: Iraq kept to 1194 against the page's own 'Iraq remained under Seljuk control until 1135' and abbasid-caliphate's 1160 gain; Hamadan 1046 on an opened page (Tughril) but called undated; the Levant gained in the 1072 shape with no ledger event although fatimid-caliphate records the 1073 and 1076 losses; missing mirrors with shaddadids, khwarezmid-dynasty (1141 occupation), eastern-kara-khanids.

Area: infobox 3900000 km2 (1080), Cliopatria 3124324 km2, ratio 1.25, acknowledged True. 

### Findings

- `/ledger/5/counterpart` (applied by reviewer): Ray 1043 is credited to buyid-dynasty and the note says the page names no holder. Evidence: Tughril page: Ray had been taken by Ibrahim Inal 'after the Kakuyid ruler Faramarz abandoned the city in 433 AH'; Tughril reclaimed it and made it his capital in 434 AH. Fix: counterpart -> kakuyids, note extended (kakuyids lacks the mirror loss: route to me-08).
- `/ledger/13/counterpart` (applied by reviewer): Mosul 1057 credited to 'Mosul and Sinjar (holder not named on the page)'. Evidence: Tughril page: 'Quraysh ibn Badran, leader of the Banu Uqayl tribe, ruled Mosul'; he left as Tughril approached and the Seljuks captured the city. Fix: counterpart -> uqaylid-dynasty, note extended (uqaylid-dynasty has no 1057 loss: route to me-08).
- `/ledger/39/counterpart, /ledger/40/counterpart, /wars/11/belligerents` (applied by reviewer): The 1153-1157 Oghuz revolt names oghuz-turks, the Oghuz Yabghu state whose dossier ends in 1055. Evidence: oghuz-turks identity end 1055; Ahmad Sanjar page: 'the Seljuks' own tribe, the Oghuz Turks, in 1153'. Fix: counterpart -> 'Oghuz (Ghuzz) Turk tribes in revolt'.
- `/identity/rulers/0/from, /wars/0/from` (applied by reviewer): Tughril's reign and the Dandanaqan war start in 1037 and 1035, before the dossier's start (1040). Evidence: Brief: rulers and wars inside the life; the earlier years belong to seljuk-dynasty. Fix: from -> 1040 in both.
- `/keyframe_review/16, /19, /20, /21, /22, /23, /24 and /ledger (missing, 1136-1160)` (NOT applied): Iraq (41-58% of the country) stays in every shape to 1194 with no loss, although the author quotes the page that ends Seljuk control there in 1135. Evidence: Seljuk Empire page: 'Iraq remained under Seljuk control until 1135' and al-Muqtafi (1136-1160) 'managed to restore a high degree of independence'; abbasid-caliphate /ledger/75 has a 1160 gain from great-seljuk-empire of 'a state stretching from Basra in the south to the edges of Mosul in the north'. KF16's note 'the page does not say what happened to the land, so the shape stands' is not a reason to keep it. Fix: Add a loss of Arab Iraq (Basra, Wasit, Baghdad to Tikrit) to abbasid-caliphate at the year the abbasid dossier uses (1160, or 1136/1157 with a page), and remove Iraq from the corrections of every keyframe after it (1139/1141/1147/1152 as adjust if before 1152; 1157, 1169, 1177, 1188, 1192 corrections).
- `/ledger (missing, 1046) and /keyframe_review/3, /4, /5, /6` (NOT applied): No gain of Hamadan; KF3 says the Jibal west of Rayy is left out 'because no page opened dates them', but the opened Tughril page does. Evidence: Tughril page: Ibrahim Inal captured Hamadan in 1046 after Garshasp fled; kakuyids /ledger/4 records the loss of Hamadan to great-seljuk-empire in 1047 (Garshasp I page). Fix: Add a 1046 gain of Hamadan (cp kakuyids, Tughril page), split KF3 at 1046 and add Hamadan to the 1046, 1052 and 1054 corrections.
- `/keyframe_review/10 and /ledger (missing, 1073, 1076)` (NOT applied): The 1072 shape adds Syria, Lebanon and Palestine (80/86/42%) with no ledger event, and /ledger/24 (1092 split) hands over a Levant that the ledger never gained. Evidence: fatimid-caliphate /ledger/46 (1073, Jerusalem) and /ledger/47 (1076, Damascus) record losses to great-seljuk-empire (Atsiz ibn Uwaq); the Seljuk dynasty infobox has the Damascus seat from 1076; the Malik-Shah page has northern Syria only in 1086. Fix: Add gains from fatimid-caliphate in 1073 (Palestine, Jerusalem) and 1076 (Damascus), citing the page the fatimid dossier used, and mark KF10 adjust: the Levant out until those years.
- `/ledger/11` (NOT applied): Azerbaijan 1054 is a gain from 'local rulers of Azerbaijan and Arran (Ganja)', but the page names them and describes a submission. Evidence: Tughril page: the Rawadid Vahsudan sent his son as hostage and read the khutbah; 'the ruler of Ganja, Amir Abu'l-Aswar Shaddadid, also submitted'. shaddadids has 1072 gain, 1075 loss, 1085 gain, 1086 loss with great-seljuk-empire, none mirrored here. Fix: Make it vassal_start events (cp shaddadids for Arran/Ganja; cp 'Rawadids' for Tabriz) or keep the gain with cp shaddadids, and add the 1072/1075/1085/1086 mirrors from the shaddadids ledger (Ani 1072 to Manuchihr; Ganja 1075, 1085-1086).
- `/ledger (missing, 1141-1142)` (NOT applied): No occupation events for Atsiz's occupation of Merv, Nishapur and Sarakhs. Evidence: khwarezmid-dynasty /ledger/3-4 (occupation_start 1141, occupation_end 1142, cp great-seljuk-empire); Atsiz page: he occupied Merv, Nishapur and Sarakhs in 1141 and was 'expelled from Khorasan by Sanjar' in 1142. Fix: Add occupation_start 1141 and occupation_end 1142, cp khwarezmid-dynasty, same regions.
- `/keyframe_review/7 and /ledger/14` (NOT applied): The 1056 keyframe is 'ok' and holds Fars and Khuzestan from 1056, while the ledger gains Fars only in 1062 (confidence 1, cited to the Seljuk Empire page, which does not mention Fars or 1062) and never gains Khuzestan. Evidence: Seljuk Empire page: neither 'Fars' nor '1062' appears; buyid-dynasty /ledger/19 (1062 dissolve, Fars, cp great-seljuk-empire) is the only basis. Fix: Mark KF7 adjust with Fars out until 1062 (or move the Fars gain), cite the Buyid page used by buyid-dynasty instead of the Seljuk Empire page, and add an event for Khuzestan (with Malik al-Rahim's Iraq in 1055 or with Fars in 1062).
- `/ledger/36` (NOT applied): Balkh and Tokharistan lost in 1152 (confidence 1, the shape's year), but the cited page has Balkh still Seljuk in 1153. Evidence: Ahmad Sanjar page: in 1153 'Amir Qumach was appointed its governor' (Balkh); the 1153 Oghuz rising begins there. Fix: Re-date to 1153 and tie it to the Oghuz revolt, or keep the shape's year and say the page contradicts it.
- `/ledger (missing, 1087-1092)` (NOT applied): No events with eastern-kara-khanids, which records a 1087-1089 contest and a 1089-1092 vassalage to great-seljuk-empire. Evidence: eastern-kara-khanids /ledger/2-5; Malik-Shah I page: in 1087 he took 'Bukhara, Samarkand, Balasagun, Isfijab and Kashgar'. Fix: Add contest_start 1087/contest_end 1089 and vassal_start 1089 (Kashgar, cp eastern-kara-khanids), with an end.
- `/ledger/4/counterpart` (NOT applied): Khwarezm 1042 is gained from 'Shahmalik (Jand)'; oghuz-turks records the same event as its 1043 loss to great-seljuk-empire. Evidence: Tughril page calls Shahmalik a Ghaznavid official and governor of Jand, not a yabghu; oghuz-turks /ledger/5-6 treats him as the Oghuz yabghu. Same event, two labels. Fix: Settle the holder with ia-01: either counterpart oghuz-turks here, or oghuz-turks drops its 1041-1043 Khwarezm events.
- `/ledger/3` (NOT applied): Gorgan and Tabaristan are coded as a plain gain from the Ziyarids; the page describes a governor in Gorgan and tribute from the Ziyarid ruler. Evidence: Tughril page: Mardavij ibn Basu appointed governor of Gorgan; Anushirvan 'agreed to pay tribute and have the khutbah read in Tughril's name'. ziyarid-dynasty has no event in 1041-1043. Fix: Gain of Golestan plus vassal_start of ziyarid-dynasty for Mazandaran (to 1090), and route the mirror to me-08.

### For a gap-filler

- `/keyframe_review/9`: The eastern step to 70.6 E (Tokharistan, Chaghaniyan) in 1066 has no event. Try https://en.wikipedia.org/wiki/Alp_Arslan
- `/keyframe_review/24`: The 1192 shape loses the west (38.7 -> 42.4 E, upper Jazira/Diyarbakir) with no event. Try https://en.wikipedia.org/wiki/Tughril_III
- `/ledger/21, /ledger/26`: Georgian vassalage 1079 (page gives no year) and its end at Didgori 1121 (confidence 1); kingdom-of-georgia (eu-19) not written yet. Try https://en.wikipedia.org/wiki/Battle_of_Didgori
- `/ledger/30, /ledger/37, /ledger/42, /ledger/43`: Vassal ends dated by the shapes (Zengids 1139, Khwarezm 1152, Ghaznavids 1157, Kerman 1187), all confidence 1. Try https://en.wikipedia.org/wiki/Imad_al-Din_Zengi
- `/identity/rulers`: Partial list: Berkyaruq, Malik-Shah II, Muhammad I Tapar (1092-1118) and the Iraq sultans of 1157-1174 are missing (admitted). Try https://en.wikipedia.org/wiki/Berkyaruq
- `/ledger (missing, c. 1075-1077)`: Bahrain and the Gulf coast (Artuk's campaign against the Qarmatians, undated on the Malik-Shah page), flagged by the author. Try https://en.wikipedia.org/wiki/Artuk_Bey

### Spot checks

- `/ledger/45`: confirmed (https://en.wikipedia.org/wiki/Ala_ad-Din_Tekish)
- `/ledger/31`: confirmed (https://en.wikipedia.org/wiki/Ahmad_Sanjar)
- `/ledger/22`: confirmed (https://en.wikipedia.org/wiki/Malik-Shah_I)
- `/ledger/41`: confirmed (https://en.wikipedia.org/wiki/Ahmad_Sanjar)
- `/ledger/5`: confirmed (counterpart wrong, fixed) (https://en.wikipedia.org/wiki/Tughril)
- `/ledger/13`: confirmed (counterpart wrong, fixed) (https://en.wikipedia.org/wiki/Tughril)
- `/ledger/27`: confirmed (https://en.wikipedia.org/wiki/Seljuk_Empire)
- `/ledger/28`: confirmed (https://en.wikipedia.org/wiki/Ahmad_Sanjar)
- `/ledger/36`: not on page (https://en.wikipedia.org/wiki/Ahmad_Sanjar)
- `/ledger/14`: not on page (https://en.wikipedia.org/wiki/Seljuk_Empire)

## danishmendids: thin

Validates; 5 events checked on 3 pages: 1101 Malatya, 1174 Sivas lands and the 1178 end confirmed; two confidence-3 events dated beyond the page (1146 Kayseri, 1150 Sivas) were lowered to 2 by the reviewer. Thin within the 5-page budget: Kayseri in 1099-1145 unexplained, the 1150 and 1175 vassalages to Rum (both on the pages) not coded, Elbistan undated.

Area: infobox None km2 (None), Cliopatria 85805 km2, ratio None, acknowledged True. The Danishmendids infobox gives no area; the dossier says so.

### Findings

- `/ledger/2/confidence` (applied by reviewer): Kayseri gain at confidence 3, but the page gives no year for Yağıbasan's deposition of Zinnun. Evidence: Yağıbasan page: 'Emir Gazi died in 1146 in Kayseri'; Zinnun succeeded him there and Yağıbasan deposed him, with no year. Fix: 3 -> 2, note extended.
- `/ledger/3/confidence` (applied by reviewer): Contest over Sivas dated 1150 at confidence 3; the page dates the vassalage, not the capture. Evidence: Yağıbasan page: Mesut I 'captured Sivas', and 'in 1150 Yağıbasan agreed to be a vassal of the Seljuks'. Fix: 3 -> 2, note extended.

### For a gap-filler

- `/ledger (missing, 1150)`: vassal_start of sultanate-of-rum in 1150 (Yağıbasan's submission, on the Yağıbasan page); the Rum dossier lacks it too. Try https://en.wikipedia.org/wiki/Ya%C4%9F%C4%B1basan
- `/ledger (missing, 1175)`: vassal_start of sultanate-of-rum in 1175 ('By 1175, Nasreddin Muhammed had returned to power, and ruled as a Seljuk vassal', Danishmendids page), ending at the 1178 dissolve. Try https://en.wikipedia.org/wiki/Danishmendids
- `/keyframe_review/2`: Kayseri enters the shape in 1099 with no event; the pages show it Danishmend only by 1146. Try https://en.wikipedia.org/wiki/Danishmend_Gazi
- `/ledger/5`: Elbistan captured from Rum with Byzantine help, undated (confidence 1, placed 1155); sultanate-of-rum has no mirror loss. Try https://en.wikipedia.org/wiki/Kilij_Arslan_II
- `/identity/capitals/0`: Niksar 1075-1142 is the author's assumption (confidence 1); the page says the capital was 'likely first established in Amasia'. Try https://en.wikipedia.org/wiki/Niksar

### Spot checks

- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Malatya)
- `/ledger/2`: confirmed (year not on page for the deposition; confidence lowered) (https://en.wikipedia.org/wiki/Ya%C4%9F%C4%B1basan)
- `/ledger/3`: confirmed (1150 is the vassalage year; confidence lowered) (https://en.wikipedia.org/wiki/Ya%C4%9F%C4%B1basan)
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Danishmendids)
- `/ledger/7`: confirmed (https://en.wikipedia.org/wiki/Danishmendids)

## khwarezmid-dynasty: thin

Validates; 8 events checked on 4 pages, all confirmed (1077 founding, 1138 Mangyshlak and the lower Syr Darya, Nishapur 1187, Persian Iraq June 1194, the caliph's 1195 counter-attack and the July 1196 recovery, the 1199 Mazandaran fortress, the 1200 Ghurid conquest of Khorasan). Thin: the vassalage to the Seljuks (1077-1138, again from 1143) and to the Qara Khitai (from 1142), both stated on the Anushtegin and Atsiz pages and present in the counterparts' ledgers, are not coded; Merv and the Turkmen plains enter the 1152 shape with no event; the 1201 recovery of Merv recorded by ghurid-dynasty and khwarezmid-empire has no event here.

Area: infobox None km2 (None), Cliopatria 614269 km2, ratio None, acknowledged True. The Anushtegin dynasty infobox gives no area.

### Findings

- `/ledger (missing, 1077 or 1097 to 1138; 1143)` (NOT applied): No vassal events with great-seljuk-empire, although great-seljuk-empire /ledger/34 has vassal_start (cp khwarezmid-dynasty) in 1143 and the shapes of both states overlap on Khwarezm in 1094-1146. Evidence: Anushtegin dynasty page: the dynasty ruled 'first as vassals of the Seljuks and the Qara Khitai'; Atsiz page: in 1143 Sanjar 'forced Atsïz back into vassalage'. Fix: Add vassal_start (cp great-seljuk-empire) at 1077, with vassal_end at the 1138 revolt, and vassal_start again in 1143 matching great-seljuk-empire /ledger/34 (end with great-seljuk-empire /ledger/37, or at Sanjar's death 1157).
- `/ledger (missing, 1142)` (NOT applied): No vassal_start for the Qara Khitai tribute; the author left it to the kara-khitans ledger as 'out of scope', but the mirror rule needs it here. Evidence: kara-khitans /ledger/10 (1142 vassal_start, cp khwarezmid-dynasty, confidence 3); Atsiz page: after the 1141 Qara Khitai raid Atsiz 'was forced to pay an annual tribute' until his death; Anushtegin page: Atsiz 'became a vassal to Yelü Dashi'. Fix: Add vassal_start 1142, cp kara-khitans, region Khwarezm, with no end inside the life (it continues into khwarezmid-empire to 1210).
- `/ledger/23 and /keyframe_review/12` (NOT applied): Khorasan is lost to the Ghurids in 1200 and stays out to 1201; ghurid-dynasty /ledger/31 records its loss back to khwarezmid-dynasty in 1201. Evidence: ghurid-dynasty /ledger/31 ('by 1201'); khwarezmid-empire /ledger/0 note: Muhammad II 'captured Merv in September 1201' (his page). This note cites the Seljuk Empire page for a 1204 recovery after Andkhud. Fix: Open the Muhammad II of Khwarazm page; if Merv/Nishapur were retaken in 1201 add a 1201 gain (cp ghurid-dynasty) and end KF12 in 1200; otherwise state the disagreement and ask sa-04 to move its 1201 loss.

### For a gap-filler

- `/keyframe_review/4`: Merv (90%) and the Turkmen plains enter the 1152 shape after a Khwarezm-only 1147-1151 keyframe, with no event; Merv was Sanjar's capital to 1153 (author flagged). Try https://en.wikipedia.org/wiki/Il-Arslan
- `/ledger (missing)`: Dihistan, taken by Tekish after Sultan-Shah, undated (author flagged). Try https://en.wikipedia.org/wiki/Sultan_Shah_(Khwarazmian)
- `/ledger/2`: The 1138 holder of Mangyshlak and Jand is inferred (kimek-kipchak-confederation); that dossier has no 1138 loss. Try https://en.wikipedia.org/wiki/Mangyshlak
- `/ledger/19, /ledger/20`: The 1198 Herat contest is undated on the Tekish page (it gives the caliph's 1198 appeal to the Ghurids and an undated siege of Herat); confidence 2 is right, a dated page would help. Try https://en.wikipedia.org/wiki/Ghiyath_al-Din_Muhammad
- `/ledger/24`: Dissolve into khwarezmid-empire in 1201 is a Cliopatria cut (confidence 1); same line of shahs, so the orchestrator may merge the rows. Try https://en.wikipedia.org/wiki/Anushtegin_dynasty

### Spot checks

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Anushtegin_dynasty)
- `/ledger/2`: confirmed (holder not named; the note says so) (https://en.wikipedia.org/wiki/Atsiz)
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Ala_ad-Din_Tekish)
- `/ledger/16`: confirmed (https://en.wikipedia.org/wiki/Ala_ad-Din_Tekish)
- `/ledger/17`: confirmed (https://en.wikipedia.org/wiki/Ala_ad-Din_Tekish)
- `/ledger/18`: confirmed (https://en.wikipedia.org/wiki/Ala_ad-Din_Tekish)
- `/ledger/21`: confirmed (https://en.wikipedia.org/wiki/Ala_ad-Din_Tekish)
- `/ledger/23`: confirmed (https://en.wikipedia.org/wiki/Seljuk_Empire)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| seljuk-dynasty 1035 gain (ghaznavid-empire) | ghaznavid-empire 1034 loss | matched | Dihistan, Nasa, Farawa; within one year after the reviewer's re-dating. |
| seljuk-dynasty 1037 gain (ghaznavid-empire) | ghaznavid-empire   | missing | Merv and Nishapur 1037-1038 (Seljuk Empire page); ghaznavid-empire has only the 1035-1040 contest. Route to me-08 (or accept as inside the contest). |
| seljuk-dynasty 1037 loss (oghuz-turks) | oghuz-turks   | missing | No 1037 gain in oghuz-turks; confidence 1 here. ia-01 / author. |
| oghuz-turks 1034 contest_start (seljuk-dynasty) | seljuk-dynasty   | missing | oghuz-turks has a Khwarezm contest 1034-1043 with seljuk-dynasty (end after that dossier's 1039 end); not in seljuk-dynasty. |
| great-seljuk-empire 1040 gain (ghaznavid-empire) | ghaznavid-empire 1040 loss | matched | Dandanaqan, May 1040. |
| great-seljuk-empire 1041 gain (buyid-dynasty) | buyid-dynasty 1041 loss | matched | Kerman. |
| great-seljuk-empire 1041 gain (ziyarid-dynasty) | ziyarid-dynasty   | missing | Gorgan/Tabaristan; the Tughril page describes tribute (vassalage) for Tabaristan. me-08. |
| great-seljuk-empire 1042 gain (Shahmalik (Jand)) | oghuz-turks 1043 loss | mismatch | Same Khwarezm event; oghuz-turks names great-seljuk-empire, this dossier names Shahmalik (a Ghaznavid governor of Jand on the Tughril page). Settle the holder with ia-01. |
| great-seljuk-empire 1043 gain (kakuyids) | kakuyids   | missing | Ray (counterpart corrected by the reviewer from buyid-dynasty); kakuyids has no Ray loss in 1041-1043. me-08. |
| kakuyids 1047 loss (great-seljuk-empire) | great-seljuk-empire   | missing | Hamadan (Tughril page: 1046); great-seljuk-empire lacks the gain. Author. |
| great-seljuk-empire 1052 gain (kakuyids) | kakuyids 1052 loss | matched | Isfahan. |
| kakuyids 1052 gain (great-seljuk-empire) | great-seljuk-empire   | missing | Yazd and Abarkuh granted to Faramurz in fief; small, a fief inside the Seljuk realm. Author may add a loss or a vassal_start. |
| great-seljuk-empire 1054 gain (local rulers of Azerbaijan and Arran (Ganja)) | shaddadids   | mismatch | The Tughril page names the Shaddadid ruler of Ganja and the Rawadid Vahsudan submitting; counterpart should be shaddadids (and Rawadids), probably as vassal_start. |
| great-seljuk-empire 1055 gain (buyid-dynasty) | buyid-dynasty 1055 loss | matched | Baghdad, December 1055. |
| great-seljuk-empire 1057 gain (uqaylid-dynasty) | uqaylid-dynasty   | missing | Mosul (counterpart corrected by the reviewer); uqaylid-dynasty has no 1057 loss. me-08. |
| great-seljuk-empire 1062 gain (buyid-dynasty) | buyid-dynasty 1062 dissolve | matched | Fars; confidence 1 here, the date is the Buyid dossier's. |
| great-seljuk-empire 1064 gain (byzantine-empire) | byzantine-empire 1064 loss | matched | Ani; byzantine-empire /ledger/107 (1065, Kars) is within one year. |
| great-seljuk-empire 1065 gain (Tbilisi (emirate; not named further on the page)) | none   | exception | No dossier; listed by the author as emirate-of-tbilisi. |
| shaddadids 1072 gain (great-seljuk-empire) | great-seljuk-empire   | missing | Ani sold to Manuchihr; also shaddadids 1075 loss, 1085 gain, 1086 loss (Ganja) with no mirror in great-seljuk-empire. Author. |
| fatimid-caliphate 1073 loss (great-seljuk-empire) | great-seljuk-empire   | missing | Jerusalem (Atsiz ibn Uwaq); and 1076 Damascus. great-seljuk-empire has no gain although its 1072 shape holds the Levant. Author. |
| great-seljuk-empire 1073 gain (western-karakhanid-khanate) | western-karakhanid-khanate 1073 loss | matched | Termez. |
| great-seljuk-empire 1074 vassal_start (kerman-seljuk-sultanate) | none   | exception | No dossier yet; listed in counterparts_needing_dossiers (me-09). |
| great-seljuk-empire 1079 vassal_start (kingdom-of-georgia) | kingdom-of-georgia   | exception | kingdom-of-georgia is owned by eu-19, not run yet (also the 1121 vassal_end). |
| byzantine-empire 1071 loss (great-seljuk-empire) | great-seljuk-empire   | mismatch | byzantine-empire credits its Anatolian losses of 1071, 1078 (Nicaea), 1084 (Smyrna), 1091 and its 1094 gain to great-seljuk-empire; this dossier removes Anatolia (Rum seat at Nicaea from 1077, Seljuk dynasty infobox). The Rum/Danishmend/Tzachas counterparts belong in byzantine-empire: route to eu-05. |
| great-seljuk-empire 1086 gain (uqaylid-dynasty) | uqaylid-dynasty 1086 loss | matched | Aleppo and Harran; Antioch and Edessa in the same event are not Uqaylid holdings in the uqaylid-dynasty ledger (which lists Aleppo and Harran only); the Malik-Shah page names no holders. |
| great-seljuk-empire 1087 vassal_start (western-karakhanid-khanate) | western-karakhanid-khanate 1087 contest_start | mismatch | western-karakhanid-khanate has a 1087-1089 contest and no vassal_start; this dossier has a vassal_start 1087 and vassal_end 1141 but no contest. ia-01 and author. |
| eastern-kara-khanids 1089 vassal_start (great-seljuk-empire) | great-seljuk-empire   | missing | eastern-kara-khanids contest 1087-1089 and vassalage 1089-1092 with great-seljuk-empire; none here (Malik-Shah page: Kashgar 1087). Author. |
| great-seljuk-empire 1092 split (Seljuk Syria (Tutush I; Damascus and Aleppo lines)) | none   | exception | No dossier yet; listed as seljuks-of-syria (me-09). |
| great-seljuk-empire 1127 vassal_start (zengid-dynasty) | zengid-dynasty 1127 found | mismatch | zengid-dynasty founds in 1127 from great-seljuk-empire but has no vassal_start; also no vassal_end 1139. Route to me-09 (zengid-dynasty already failed review). |
| great-seljuk-empire 1135 vassal_start (ghaznavid-empire) | ghaznavid-empire   | missing | Bahram Shah as Seljuk vassal (Sanjar page); ghaznavid-empire has no vassal events (nor the 1157 end). me-08. |
| great-seljuk-empire 1141 loss (kara-khitans) | kara-khitans 1141 vassal_start | mismatch | kara-khitans takes Transoxiana as a vassal of the Western Karakhanids (its /ledger/9), not as a gain from great-seljuk-empire, which itself held it only as a vassal (its /ledger/23). Author: keep only the vassal_end, or the keyframes must hold Transoxiana as direct land and kara-khitans needs a gain. |
| khwarezmid-dynasty 1141 occupation_start (great-seljuk-empire) | great-seljuk-empire   | missing | Merv, Nishapur, Sarakhs 1141-1142 (Atsiz page); great-seljuk-empire lacks the occupation pair. Author. |
| great-seljuk-empire 1143 vassal_start (khwarezmid-dynasty) | khwarezmid-dynasty 1143 contest_end | mismatch | khwarezmid-dynasty has no vassal_start (nor the 1152 end, nor the 1077-1138 vassalage). Author. |
| great-seljuk-empire 1152 loss (Balkh and Tokharistan (holder not named on the page)) | none   | exception | No holder; confidence 1 and contradicted by the Sanjar page (Balkh Seljuk in 1153). |
| great-seljuk-empire 1157 loss (Turkic and Turkmen rulers of Khorasan (Oghuz, Ay-Aba at Nishapur)) | none   | exception | No dossier; listed as emirate-of-nishapur. |
| ghurid-dynasty 1175 gain (great-seljuk-empire) | great-seljuk-empire   | mismatch | ghurid-dynasty takes Herat 'from the Seljuks' in 1175; this dossier has Khorasan out from 1157. Route to sa-04: name the Turkic holder of Herat, or the author adds Herat to the post-1157 shape. |
| abbasid-caliphate 1160 gain (great-seljuk-empire) | great-seljuk-empire   | missing | Arab Iraq, Basra to Mosul; great-seljuk-empire keeps Iraq to 1194. Author (blocking). |
| great-seljuk-empire 1187 vassal_end (kerman-seljuk-sultanate) | none   | exception | No dossier yet. |
| great-seljuk-empire 1194 loss (khwarezmid-dynasty) | khwarezmid-dynasty 1194 gain | matched | Persian Iraq, March/June 1194. |
| danishmendids 1101 gain (Gabriel of Melitene) | none   | exception | Minor holder, no dossier needed. |
| danishmendids 1146 gain (Zinnun (Dhu'l-Nun), Emir Gazi's elder son at Kayseri) | none   | exception | Inside the dynasty; Kayseri is already in the Danishmend shape from 1099. |
| danishmendids 1155 gain (sultanate-of-rum) | sultanate-of-rum   | missing | Elbistan, confidence 1; sultanate-of-rum has nothing between 1097 and 1174 (also no 1150-1155 contest or 1150 vassalage). me-09-b/gap-filler. |
| danishmendids 1174 loss (sultanate-of-rum) | sultanate-of-rum 1174 gain | matched | Sivas lands. |
| danishmendids 1178 loss (sultanate-of-rum) | sultanate-of-rum 1178 gain | matched | Malatya, end of the dynasty. |
| khwarezmid-dynasty 1138 gain (kimek-kipchak-confederation) | kimek-kipchak-confederation   | missing | Mangyshlak and Jand; the holder is inferred; kimek-kipchak has no 1138 loss. ia-01. |
| kara-khitans 1142 vassal_start (khwarezmid-dynasty) | khwarezmid-dynasty   | missing | Khwarezm tributary from 1142 (Atsiz and Anushtegin pages); khwarezmid-dynasty left it out. Author. (kara-khitans /ledger/19 ends it in 1210 with cp khwarezmid-dynasty, which ends in 1201: should be khwarezmid-empire, ia-01.) |
| khwarezmid-dynasty 1187 gain (Sanjar-Shah and the atabeg Mengi-Tegin) | none   | exception | Listed as part of sultan-shah-khorasan / emirate-of-nishapur. |
| khwarezmid-dynasty 1193 gain (Mahmud Sultan Shah (rival half-brother)) | none   | exception | Listed as sultan-shah-khorasan. |
| khwarezmid-dynasty 1194 gain (great-seljuk-empire) | great-seljuk-empire 1194 loss | matched | Ray (March) and Persian Iraq (June). |
| khwarezmid-dynasty 1195 loss (abbasid-caliphate) | abbasid-caliphate   | missing | Persian Iraq to the caliph's army late 1195 and back in July 1196 (Tekish page); abbasid-caliphate has neither. Route to the abbasid owner. |
| khwarezmid-dynasty 1200 loss (ghurid-dynasty) | ghurid-dynasty 1200 gain | matched | Khorasan. |
| ghurid-dynasty 1201 loss (khwarezmid-dynasty) | khwarezmid-dynasty   | missing | Khorasan recovered 'by 1201' (Merv, September 1201 per khwarezmid-empire); khwarezmid-dynasty has no gain. Author. |

## Counterparts needing dossiers

- Kerman Seljuk Sultanate (`kerman-seljuk-sultanate`, 1041-1187)
- Seljuks of Syria (Damascus and Aleppo lines) (`seljuks-of-syria`, 1076-1117)
- Eldiguzids (Atabegs of Azerbaijan) (`eldiguzids`)
- Rawadids (Tabriz, submitted to Tughril 1054) (`rawadid-dynasty`)
- Emirate of Tbilisi (`emirate-of-tbilisi`)
- Mu'ayyid Ay-Aba's emirate of Nishapur (`emirate-of-nishapur`, 1157-1174)
- Mahmud Sultan-Shah's Khorasan (`sultan-shah-khorasan`, 1172-1193)
- Artuqids (`artuqids`)
- Assassins of Alamut (Nizari Ismailis) (`nizari-ismaili-state`)

## Gazetteer names needed

- Jand (place, khwarezmid-dynasty)
- Sarakhs (place, khwarezmid-dynasty)
- Niksar (place, danishmendids)
- Persian Iraq (region, great-seljuk-empire)

## Problems

- No page failed for the reviewer: 12 WebFetch reads (Seljuk Empire, Seljuk dynasty, Battle of Dandanaqan, Tughril, Malik-Shah I, Ahmad Sanjar, Ala ad-Din Tekish, Atsiz, Anushtegin dynasty, Danishmendids, Malatya, Yağıbasan).
- One read of great-seljuk-empire.json from the mount came back truncated (JSON 'Unterminated string') a few seconds after the reviewer's write; a re-read was complete and held the edit. Treat as a transient network-mount read.
- Structure for the orchestrator: seljuk-dynasty (985-1039) and great-seljuk-empire (1040-1194) are one state on the Seljuk Empire page (formation 1037); khwarezmid-dynasty (1077-1201) and khwarezmid-empire (1202-1231) are one line of shahs. The hand-overs are clean (dissolve/found in consecutive years), so a merge is optional; the rule 'one dossier per state' favours merging under the earlier slugs.
- The Cliopatria Great Seljuk shapes of 1195-1201 belong to no state in this batch after the 1194 end; khwarezmid-dynasty covers Persian Iraq, but Azerbaijan, Fars and Khuzestan of the 1192 shape need the Eldiguzid and Salghurid dossiers (me-09-x).
- Cross-dossier mismatches to route outside this batch: byzantine-empire (eu-05) credits its 1071-1094 Anatolian losses to great-seljuk-empire; kara-khitans (ia-01) ends Khwarezm's vassalage in 1210 with cp khwarezmid-dynasty (ends 1201); oghuz-turks (ia-01) closes a contest with seljuk-dynasty in 1043, after that dossier's end; abbasid-caliphate lacks the 1195-1196 Persian Iraq events; ghaznavid-empire, kakuyids, uqaylid-dynasty and ziyarid-dynasty (me-08) lack mirrors listed in cross_checks.
