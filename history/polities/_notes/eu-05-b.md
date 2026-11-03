# eu-05-b - research notes (written 2026-10-19)

One owned state: **byzantine-empire** (Cliopatria "Byzantine Empire", 633..1474, 91 shapes, Wikidata Q112039853). Dossier: `history/polities/byzantine-empire.json` (633-1460; 182 events, 95 keyframe verdicts = 91 shapes + 4 new keyframes: 87 ok / 6 adjust / 2 wrong; 39 wars; 14 sources; validates, 0 resolve warnings, 1 deliberate warning). Fourteen pages were opened (the brief's ceiling); 47 of the 182 events are confidence 1 (Cliopatria shape-year bridges the pages do not date), 41 are confidence 2, 94 are confidence 3.

## Byzantine Empire (byzantine-empire, 633-1460)

### One state, three rows; the 1204-1261 interlude
- "Roman Empire", "Eastern Roman Empire" (395..632) and "Byzantine Empire" (633..1474) are one polity (rule 2). The dossier starts as a hand-over from eastern-roman-empire (confidence 1; the Heraclian page opens the Arab wars in 633) and ends in May 1460.
- 1204-1261 is a `split` to nicaean-empire (April 1204) and a `merge` back (25 July 1261, Reconquest of Constantinople page); the Latin Empire, Venice and Achaea take the losses. Cliopatria's Byzantine row has no shape for 1227-1278 and holds twelve island cells for 1206-1226 ('wrong'); its "Nicaean Empire" 1260 and 1272 shapes are the restored empire, so new keyframes `byzantine-empire_1261` (1261-1271) and `_1272` (1272-1278) point at them, as the nicaean-empire dossier asks. Epirus and Trebizond are their own dossiers.
- End year 1460, not 1453: the main page ends the empire with Constantinople on 29 May 1453, but the emperor's brothers held the Morea until May 1460 (Despotate of the Morea page; new keyframe `_1453` = the Morea alone). Cliopatria's 1440-1467 shape keeps Constantinople to 1467; its 1468-1474 shape is two Lemnos cells ('wrong').

### Cliopatria rows to correct (keyframe_review)
- **647-655 adjust**: the Exarchate of Africa is missing for nine years. The Arab-Byzantine page: invaded 647, took Tripolitania and Sufetula, accepted a tribute and left (647-648), Carthage 'lost in 698'. Correction: Cliopatria's own 656 shape minus Cyrenaica and Tripolitania.
- **1407 adjust** and new `_1402`: the 1402-1406 years are a hole in the row; after Ankara the Byzantines 'were able to recover Thessalonika and much of the Peloponnese' (treaty undated), which the 36-cell shapes of 1395-1430 omit. Correction: the 1407 shape plus Thessalonica.
- Dropped too early or kept too long (verdict 'ok', ledger carries the dated event): Damascus kept to 637 (634); Egypt dropped 641 (Alexandria 642, retaken 645, lost 646); Cyrenaica kept to 665 (643-644); Tripolitania to 673 (647-648); Africa to 704 (Carthage 698); Ravenna absent 741-749 (taken c. 738 for a time, fell 751); Rome absent from 768 (Papal States 756); eastern Bulgaria (971) only in 980; Vaspurakan (1021) in 1028; Ani (1045) in 1046; Bithynia dropped 1305 though Bursa/Nicaea/Nicomedia fell 1326/1331/1337 (drawn as a contest 1301-1337); Thessalonica kept to 1394 (fell 1387).
- Cyprus is inside 875-885 while Cliopatria also draws a Cyprus Condominium row (692-959); the ledger keeps Cyprus out from 653 to 960. Southern Crimea (Chersonesos) is inside every shape from 633 although the Basil II page has the Byzantines 'occupied southern Crimea' only after 1016. Both flagged, not corrected.

### Pages that would not load
- https://en.wikipedia.org/wiki/Byzantine%E2%80%93Arab_wars (URL_NOT_FOUND: wrong title). The correct page, Arab%E2%80%93Byzantine_wars, opened and is the one cited.

### Disagreements between pages
- Armenia lost: Heraclian page 691 ('with them went Armenia to the enemy'), Arab-Byzantine page 692. Dossier: 691, confidence 2.
- Cyprus lost: Arab-Byzantine page 653 ('captured in 653'); Heraclian page has the Arab fleet raiding 'the Byzantine island of Cyprus' in 657. Dossier: 653, confidence 2.
- Smyrna: lost by 1084, recovered by John Doukas in 1097 (Seljuk wars page); Komnenian page 'Between 1097 and 1101 Alexios managed to recover Nicaea, Rhodes, and Ephesus'; Cliopatria's shape returns the west in 1099. Dossier: 1097.
- Antioch: the principality was a Byzantine vassal from 1138 (Byzantine Empire page; Komnenian page places the first vassalage in 1097-1101). Dossier: 1138, confidence 3.

### What could not be settled
- 47 confidence-1 events: dates and takers of Cliopatria's undated shape changes, listed in the report under `gaps`. Examples: Corsica 732, Balearics and Ceuta 718, Sardinia 840, Brindisi 1056, Calabria 1066, Zeta and Raska 1056/1066, Cilicia 1139/1147, Cyprus 1192, Skopje 1285, Kutahya 1305, Manisa 1314, Serres 1385, Thessalonica 1403/1431.
- The Anatolian frontier of 718-724, 926 and 1111, the western Balkan lobe of 970-979 (about 175 cells in Bosnia and Serbia), the Karaman plateau in 1192 and Denizli/Paphlagonia in 1202 are marked 'unverified: page budget'.
- Mystras as the seat 1454-1460 is confidence 1 (the Despotate page extract named the despots, not the seat).
- Certainty: all five eras are soft. Sharp lines would need treaty pages not opened (Thracian border 815 and 927 are mentioned in notes only).

### Pages that would help a gap-filler (not opened here)
Byzantine Empire under the Palaiologos dynasty; Byzantine Empire under the Komnenos dynasty; Muslim conquest of the Levant; Muslim conquest of the Maghreb; Exarchate of Africa; Muslim conquest of Armenia; Cyprus in the Middle Ages; Catepanate of Italy; Norman conquest of southern Italy; Theme of Dalmatia; Siege of Thessalonica (1422-1430); Treaty of Gallipoli; Anatolian beyliks; Empire of Nicaea; Latin Empire.

### Counterparts that need a dossier or a slug
Emirate of Melitene (conquered in the 930s), Kingdom of Kars (Gagik-Abas; ceded c. 1064, taken 1065), Philaretos Brachamios's Antioch (1078-1084), Peter II Delyan's revolt (1040-1041), the Zaccaria lordship of Chios (recaptured 1329), David III of Tao / Tao-Klarjeti (1001). All appear as strings in ledger counterparts. `kingdom-of-cyprus` (Cliopatria, from 1192) stands for the 1192 Cyprus loss on Cliopatria's authority only. Existing slugs used as counterparts that have a Cliopatria row but no dossier yet: rashidun-caliphate, umayyad-caliphate, first-bulgarian-empire, second-bulgarian-empire, kingdom-of-italy, papal-states, emirate-of-crete, aghlabid-dynasty, emirate-of-sicily, abbasid-caliphate, hamdanid-emirates, fatimid-caliphate, kingdom-of-georgia, kingdom-of-vaspurakan, bagratid-armenia, norman-italy, great-seljuk-empire, sultanate-of-rum, principality-of-antioch, armenian-kingdom-of-cilicia, kingdom-of-hungary, republic-of-venice, serbian-empire, ottoman-empire and others (the validator raised no unknown-slug warning).

### Gazetteer
Names that had to be replaced by lon/lat discs are listed in the report (`gazetteer_names_needed`). Quirks met: 'Philadelphia' and 'Syracuse' resolve to US cities; 'Pentapolis' resolves to Libyan Cyrenaica; an empty `minus` operand raises a NoneType error; 'Edessa' is unknown.

## Repair pass (2026-10-19, after the review verdict 'fail')

Figures above are the first draft's. After the repair the dossier has 201 events (45 confidence 1, 61 confidence 2, 95 confidence 3), 95 keyframe verdicts (86 ok, 7 adjust, 2 wrong), 32 sources, and validates with two deliberate warnings (the Ghassanid vassal_end of 633, and the empty-shape correction of keyframe byzantine-empire_1206 that resolves to no cells). Eighteen further pages were opened for the repair (listed in sources with 'Repair pass' notes): Constantine XI Palaiologos, Centurione II Zaccaria, Barony of Karytaina, Battle of Prinitza, Muslim conquest of Sicily, Siege of Thessalonica (1422-1430), Muslim conquest of Armenia, Alexios I of Trebizond, David Komnenos, Michael I Komnenos Doukas, Kingdom of Thessalonica, Duchy of Athens, Latin Empire, Despotate of Epirus, Nikephoros I Komnenos Doukas, Nicholas Orsini, John II Orsini, Michael Monomachos. No page failed.

### What changed, per finding
- **1428 (blocking)**: the confidence-3 'last remnants of Achaea' event is gone. Replaced by 1428/5 Glarentza from despotate-of-epirus (Constantine XI page, c3), 1429 Chalandritsa (Centurione II page, c2), 1430/7 Patras (Constantine XI page, c3), 1432 Arcadia (Centurione II page, c2). /ledger 1430 'entire peninsula' kept. Keyframe _1415 note rewritten (it quoted the undated phrase).
- **1204-1205 hand-over**: added losses to latin-empire (Thrace outside the capital, c2, using the latin-empire dossier's own founding region), empire-of-trebizond (three events: Trebizond and Chaldia April 1204, Sinope-Samsun-Limnia, Paphlagonia; all c2), kingdom-of-thessalonica (1204, c2), despotate-of-epirus (c. 1205, c2), duchy-of-athens (1205, c2). Crete added to the Venice loss on the Latin Empire page's words ('including Crete and other islands'). Checked on the 1202 shape (1,326 cells): after all these, 420 cells (106 k km2) are still not handed to anyone: Bulgaria 145, Turkey (inner Anatolia) 118, Greece 67, North Macedonia 48, Kosovo 21, Albania 10. My reading, not checked on a page: the Bulgarian and northern Balkan cells are land of the Second Bulgarian Empire from 1185-1188 (Cliopatria's 1202 shape is generous there) and the Anatolian cells are inner Anatolia. Left as a gap, not invented.
- **1261**: /ledger 'gain of Constantinople from latin-empire' dropped; the merge region is now the Nicaean 1260 shape plus the 45 km disc of Constantinople, as keyframe _1261 draws it.
- **Keyframe _1206**: the correction is the empty shape ({"minus": [Byzantine 1206, Byzantine 1206]}, resolves to 0 cells), no longer the Nicaean shape. The schema has no empty-shape spelling; the validator warns that it resolves to no cells (deliberate).
- **Keyframe _1415**: verdict adjust, 1415 shape plus a 40 km disc at Thessalonica for 1415-1423. The 1431 loss to the Ottomans is replaced by 14 September 1423 loss to republic-of-venice (Siege of Thessalonica page, c3); the 1403 gain is raised to c2 on the same page ('Ottoman control from 1387 to 1403', returned under the Treaty of Gallipoli). Notes of keyframes _1402, _1407, _1431 updated.
- **Armenia**: gain added in 657 (c2; counterpart rashidun-caliphate) from the Muslim conquest of Armenia page.
- **Arcadia**: 1326 gain moved to 1320 at c3 (Barony of Karytaina page); keyframe _1326's note says so.
- **Achaea**: 1264 gain (rest of Laconia, c2) and 1418 gain (Messenia and Elis, c2) added; the 1262 event (Mystras, Monemvasia, Mani) re-sourced to the Prinitza page and raised from c1 to c3.
- **Epirus**: added c. 1280 gain (Albania, c1), 1318 gain (Ioannina, c2), c. 1325 loss (c1), 1339 loss (c2) and 1340 gain (c2). Keyframe _1294's note ties its 45 Adriatic cells to the 1280 event.
- **Sicily**: the 859, 878, 902 losses, and also the 880 regain of Taranto and the 900 loss of Catania, now name aghlabid-dynasty (Sicily was an Aghlabid province until 909); months added (1, 5, 8) from the Muslim conquest of Sicily page, which is now their source. Added 840 loss of Taranto (c2) and 29 August 870 loss of Malta (c3).
- Reviewer's small fixes (Philippopolis 836, Philippi 837, Zagora 863 to c2; Cilicia 962 to c1; Mystras capital move to c2) kept unchanged.

### Where I differ from the reviewer, and why
- **Armenia date and confidence**: the reviewer suggested c. 658-661 at c1 from Cliopatria's 661 shape. The Muslim conquest of Armenia page dates the return to Byzantine overlordship to 657 ('with the First Fitna, Mamikonian returned to Byzantine overlordship almost immediately'), and the same page has the princes re-submitting to Mu'awiya in 661, the very year Cliopatria adds Armenia. I kept 657 at c2 and left the 691 loss (Heraclian page) in place; the pages disagree and the dossier says so. The 657 gain precedes the shape by four years (keyframe _661 note).
- **1264 'Laconia, Mani'**: the Battle of Prinitza page puts the Mani (with Monemvasia and Mystras) in early 1262, not 1264; 1264 is the rest of Laconia ('By 1264, only Lacedaemon appears to have remained in Frankish hands'). So the 1262 event was raised and the 1264 gain is Laconia without the Mani.
- **Chalandritsa 1429 at c2**: the Centurione II Zaccaria page dates the siege (1429) but not the surrender; the Achaea dossier has c3.
- **Ioannina 1318 at c2 (Achaea/Epirus dossier has c3)**: the Nicholas Orsini page dates the murder (1318) and says Ioannina declared for the emperor 'as soon as the murder of Thomas became known', with no year on that sentence.
- **Trebizond 'Kerasous, Cide'**: the empire-of-trebizond dossier quotes a David Komnenos sentence naming Kerasous, Cide, Amasra and Heraclea Pontica; the page as opened has 'Amastris, Tios and Heraclea Pontica' and no Kerasous or Cide. My event quotes what I found; the Trebizond author may have used another page.
- **Albania c. 1280 (not 1281, no Berat)**: Nikephoros I's page says only 'soon after' Charles of Anjou's defeat and does not name Berat; I kept c. 1280 at c1 rather than take 1281 from memory.
- **1325 Epirus**: kept as a loss at c1 as asked, but the John II Orsini page describes suzerainty ('allowed to establish his control over all of Epirus in exchange for recognizing Byzantine suzerainty') with no year; a vassal_start would be truer.
- **Duchy of Athens 1205, not 1204**: the page's infobox says 'Fourth Crusade: 1204', 'Duchy established: 1205'; I used 1205.
- **Latin Empire page and Thrace**: the page lists no Thracian places at the founding (its list is 'areas of Greece, divided into vassal fiefs' and 'the Duchy of Philippopolis in north Thrace'); the Thrace loss is c2 and rests on the latin-empire dossier's region.

### Still open
- Counterpart dossiers that do not exist yet: kingdom-of-thessalonica and duchy-of-athens (eu-05, other part), republic-of-venice (eu-13; mirror of the 1204 and 1423 losses), aghlabid-dynasty (af-02: needs 900 Catania, 880 Taranto regain), emirate-of-sicily (eu-13). The Aghlabid against emirate-of-sicily convention for 850-909 still needs an orchestrator ruling.
- The thin items are untouched except those named above.
