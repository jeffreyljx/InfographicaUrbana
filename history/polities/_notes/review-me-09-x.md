# Review of batch me-09-x (Turks, Crusaders, Mamluks, part x: additions)

Reviewer: adversarial review, Phase B, 2026-10-25. Twenty-one dossiers, all states Cliopatria lacks (no shapes, every keyframe new). The validator passes all 21 with no errors (warnings are unknown gazetteer places only). Spot checks: every dossier had at least its confidence-3 and largest-land events opened on the pages cited (four or more per dossier where the ledger has that many). No fabricated event was found; two events were mis-dated (khorshidi-dynasty Mandali, fixed; burhan-al-din-state Amasya, left to the author).

Verdict meaning here: `pass` nothing to change; `fix` the listed findings with applied: false are for the author (none is blocking), findings with applied: true were made by the reviewer and re-validated; `thin` honest but the ledger leaves border moves unexplained within the page budget (gap-filler list).

No article in this batch gives an infobox area and no state has a Cliopatria shape, so the area checks are empty by necessity.

## Verdicts

| slug | verdict | fixes (applied/total) | thin items |
| --- | --- | --- | --- |
| artuqids | fix | 0/2 | 2 |
| nizari-ismaili-state | fix | 0/2 | 3 |
| eldiguzids | fix | 1/2 | 2 |
| kerman-seljuk-sultanate | fix | 2/4 | 2 |
| salghurids | pass | 0/0 | 2 |
| burid-dynasty | pass | 0/0 | 2 |
| seljuks-of-syria | fix | 1/1 | 2 |
| kingdom-of-hormuz | fix | 0/2 | 4 |
| saltukids | pass | 0/0 | 1 |
| mengujekids | pass | 0/0 | 2 |
| qutlugh-khanids | fix | 0/2 | 1 |
| eretnids | thin | 0/0 | 5 |
| burhan-al-din-state | fix | 0/2 | 1 |
| atabegs-of-yazd | pass | 0/0 | 1 |
| ahlatshahs | pass | 0/0 | 1 |
| nasrid-dynasty-of-sistan | thin | 0/0 | 2 |
| mihrabanids | fix | 0/1 | 2 |
| hazaraspids | fix | 0/1 | 3 |
| khorshidi-dynasty | fix | 1/1 | 1 |
| banu-munqidh | fix | 0/2 | 2 |
| ahmadilis | fix | 0/2 | 1 |

## artuqids: fix

Findings:

- `/ledger (new events after /ledger/14)`: No vassal_start 1384 / vassal_end 1409 with counterpart qara-qoyunlu, although qara-qoyunlu/ledger/1 (1384 vassal_start) and /ledger/7 (1409 vassal_end) hold the Artuqids of Mardin as its vassal. Evidence: Reviewer brief rule 3 (a vassal_start of X is mirrored in X's ledger); the dossier's own /ledger/15 note: 'Qara Muhammad had received the submission of Majd al-Din Isa in 1384'. Fix: Add vassal_start 1384 (region as keyframe artuqids_1234: Mardin and Mayyafariqin; counterpart qara-qoyunlu; confidence 2; source the Artuqids page or qara-qoyunlu's page) and vassal_end 1409 with the same counterpart; qara-qoyunlu should replace its counterpart string 'Artuqids of Mardin' with 'artuqids'.
- `/ledger/1 and /keyframe_review/0`: Mardin is booked as a 1108 gain from Ibrahim ibn Sokmen, an Artuqid, so land already in the dynasty enters the map as if from outside; keyframe artuqids_1102 leaves Mardin out. Evidence: Ilghazi page: 'Ilghazi took Mardin from him in 1108' (him = Sokmen's son Ibrahim); Artuqids page: 'Ilghazi succeeded Sokmen in Mardin' and 'Ilghazi's branch ruled from Mardin and Mayyafariqin between 1106 and 1186'. Fix: Either add Mardin to artuqids_1102 as Sokmen's line (confidence 1 bridge) and turn /ledger/1 into a note on the hand-over between branches, or keep the gain and state in the keyframe note that pre-1108 Mardin is deliberately undrawn; the counterpart string should then be 'nobody' or explained.

Thin (for a gap-filler):

- `/ledger/5`: Which of the five towns Baldwin II recovered after Hab (all returned at confidence 1) (try https://en.wikipedia.org/wiki/Battle_of_Hab)
- `/keyframe_review/4`: When the Artuqids first held Harput (drawn only from 1185) (try https://en.wikipedia.org/wiki/Harput)

Spot checks: `/ledger/1` confirmed (Ilghazi); `/ledger/2` confirmed (Ilghazi); `/ledger/7` confirmed (Artuqids); `/ledger/9` confirmed (Artuqids); `/ledger/14` confirmed (Artuqids); `/ledger/15` confirmed (Artuqids).

## nizari-ismaili-state: fix

Findings:

- `/keyframe_review/1 to /keyframe_review/11 and /ledger/3`: Quhistan (with Tabas), the Nizari state's largest territory, is in no keyframe, while the 1101-1118 contest zone includes Tabas, land the state never holds on the map. Evidence: Nizari Ismaili state page: the Ismailis had 'a strong presence' in Quhistan, whose governors (muhtasham) were appointed from Alamut, and 'The Mongols kept putting pressure on the Nizaris of Quhistan and Qumis'; Order of Assassins page: in 1101/02 Sanjar was 'to attack Assassin strongholds in Quhistan' and the Assassins were 'soon reestablished at both Quhistan and Tabas'. Fix: Add Quhistan (a region spec for Qohestan, e.g. South Khorasan with Tabas and Qa'in, text 'Quhistan') to the keyframes from 1101 at the latest (gain from great-seljuk-empire, confidence 1 for the year: page silent) to 1256 (loss to ulus-of-hulegu, 'Mongols kept putting pressure on the Nizaris of Quhistan'); or, if it stays out, drop Tabas from the contest zone and say in every keyframe note that Quhistan is deliberately undrawn.
- `/ledger/10 and /ledger/11`: The Shaizar occupation names the counterpart string 'Banu Munqidh (Shaizar)' although banu-munqidh is a dossier in this batch, and banu-munqidh/ledger/7 hands Shaizar straight to zengid-dynasty in 1157 with no Assassin step. Evidence: Order of Assassins page: 'Nur ad-Din would again foil the Assassins in 1158, incorporating a castle at Shaizar that they had occupied after the 1157 earthquake into his territory'; Banu Munqidh page: Shayzar 'was soon after seized by Nur al-Din' and names no Assassins in 1157. Fix: Use counterpart 'banu-munqidh' on both occupation events (the pair must keep one string), or better model it as a 1157 gain from banu-munqidh and a 1158 loss to zengid-dynasty, and add the Assassin step to banu-munqidh's note; zengid-dynasty should carry the 1158 Shaizar gain.

Thin (for a gap-filler):

- `/ledger/12`: Year of al-'Ullaiqah and ar-Rusafa (confidence 1 at 1162) (try https://en.wikipedia.org/wiki/Rashid_ad-Din_Sinan)
- `/ledger/15`: Fate of Rudkhan after 1096 (closed with Alamut at confidence 1) (try https://en.wikipedia.org/wiki/Rudkhan_Castle)
- `/keyframe_review`: Quhistan, Qumis and the Ziyarid/Sallarid handovers undated (try https://en.wikipedia.org/wiki/Quhistan)

Spot checks: `/ledger/0` confirmed (Nizari_Ismaili_state); `/ledger/1` confirmed (Order_of_Assassins); `/ledger/8` confirmed (Order_of_Assassins); `/ledger/14` confirmed (Nizari_Ismaili_state); `/ledger/20` confirmed (Order_of_Assassins); `/ledger/21` confirmed (Order_of_Assassins).

## eldiguzids: fix

Findings:

- `/ledger/4/counterpart` (applied by reviewer): Counterpart 'Ahmadilis (Maragheh)' was not a slug although ahmadilis is a dossier in this batch. Evidence: Eldiguz page: 'Tabriz was also gained from Ahmadilis in 1174'. Fix: Counterpart set to 'ahmadilis' (reviewer). The ahmadilis dossier still lacks the 1174 loss of Tabriz (see its fixes).
- `/ledger (new events at 1217 and 1225)`: No vassal_start 1217 / vassal_end 1225 with counterpart khwarezmid-empire, although khwarezmid-empire/ledger/16 (1217 vassal_start, Azerbaijan, Arran and Derbent) and /ledger/26 (1225 vassal_end) name eldiguzids. Evidence: Reviewer brief rule 3; khwarezmid-empire ledger 16 and 26. Fix: Add vassal_start 1217 (region: the 1196-1225 keyframe, counterpart khwarezmid-empire, source as khwarezmid-empire's, confidence 2) and vassal_end 1225 before the 1225 loss.

Thin (for a gap-filler):

- `/ledger/12`: When Shirvan left Eldiguzid authority (confidence 1 at 1195) (try https://en.wikipedia.org/wiki/Akhsitan_I)
- `/ledger/2`: Persian Iraq 1160-1194 is a vassal tint here but direct Seljuk land in great-seljuk-empire; one reading must win (try https://en.wikipedia.org/wiki/Arslan-Shah)

Spot checks: `/ledger/1` confirmed (Eldiguz); `/ledger/2` confirmed (Eldiguz); `/ledger/3` confirmed (Eldiguz); `/ledger/4` confirmed (Eldiguz); `/ledger/7` confirmed (Qizil_Arslan); `/ledger/13` confirmed (Eldiguzids).

## kerman-seljuk-sultanate: fix

Findings:

- `/identity/successors/0/slug` (applied by reviewer): Successor slug 'oghuz-turks' names the Cliopatria Oghuz state of 750-1055, not the Ghuzz of Kerman who took Kerman in 1186; the author's own note said so. Evidence: Kerman Seljuk Sultanate page: 'The Ghuzz chief Malik Dinar quickly seized control of Kerman in his place' (1186); oghuz-turks ends in 1055. Fix: Slug set to 'ghuzz-turks-of-kerman', the slug the author's report proposes under counterparts_needing_dossiers (reviewer).
- `/ledger/0/note` (applied by reviewer): The note quoted 'established his own sultanate in 1041' from the Qavurt page, which says the sultanate was founded 'in around 1048'. Evidence: Qavurt page: 'he defeated the Buyid ruler's army in Kerman and Makran in around 1041' and 'he laid the foundations of his own new sultanate in around 1048'; the 1041 year rests on the Kerman page infobox 'Established: 1041 (429 AH)', which the note also quotes. Fix: Quote corrected in the note (reviewer); year and confidence 2 unchanged.
- `/ledger (new events at 1074 and 1187)`: No vassal_start 1074 / vassal_end 1187 with counterpart great-seljuk-empire, although great-seljuk-empire/ledger/26 and /ledger/62 name kerman-seljuk-sultanate. Evidence: Reviewer brief rule 3; great-seljuk-empire ledger 26 (1074 vassal_start, 'Kerman (Bardsir), the Kerman Seljuk line') and 62 (1187 vassal_end). Fix: Add vassal_start 1074 and vassal_end 1187 with counterpart great-seljuk-empire and the Kerman region, confidence 2, source as great-seljuk-empire's.
- `/sources/2`: Source 'Malik_Dinar' is the Basran scholar, used for nothing (the entry says so). Evidence: Author's pages_failed list and the source's own note. Fix: Remove the entry from sources[].

Thin (for a gap-filler):

- `/keyframe_review/0`: Fars: 'Shiraz and its surroundings were handed over to Qavurt Bey' in 1062 (Qavurt page); end of tenure unknown, so not drawn (try https://en.wikipedia.org/wiki/Qavurt)
- `/ledger/3`: The Ghuzz of Kerman (Malik Dinar, 1186-1196) need a dossier (try https://en.wikipedia.org/wiki/Malik_Dinar_(Ghuzz))

Spot checks: `/ledger/0` confirmed (Kerman_Seljuk_Sultanate); `/ledger/1` confirmed (Kerman_Seljuk_Sultanate); `/ledger/3` confirmed (Kerman_Seljuk_Sultanate); `/ledger/4` confirmed (Kerman_Seljuk_Sultanate).

## salghurids: pass

Thin (for a gap-filler):

- `/ledger/5`: When the Salghurids left Bahrain (confidence 1 at 1253) (try https://en.wikipedia.org/wiki/Usfurid_dynasty)
- `/keyframe_review/1`: Undated vassalage to the Seljuks, the Khwarazm Shahs and the Mongols (the Salghurids page gives no years) (try https://en.wikipedia.org/wiki/Sa%27d_I)

Spot checks: `/ledger/0` confirmed (Salghurids); `/ledger/1` confirmed (Salghurids); `/ledger/3` confirmed (Abu_Bakr_ibn_Sa%27d); `/ledger/4` confirmed (Abu_Bakr_ibn_Sa%27d); `/ledger/6` confirmed (Salghurids).

## burid-dynasty: pass

Thin (for a gap-filler):

- `/ledger/4`: When the Burids took Hama (confidence 1 at 1128) (try https://en.wikipedia.org/wiki/Hama)
- `/certainty/0`: Banias and the Hauran frontier not drawn (try https://en.wikipedia.org/wiki/Banias)

Spot checks: `/ledger/0` confirmed (Burid_dynasty); `/ledger/1` confirmed (Toghtekin); `/ledger/2` confirmed (Toghtekin); `/ledger/3` confirmed (Toghtekin); `/ledger/6` confirmed (Imad_ad-Din_Zengi); `/ledger/7` confirmed (Imad_ad-Din_Zengi).

## seljuks-of-syria: fix

Findings:

- `/ledger/8/counterpart` (applied by reviewer): Aleppo's 1094 holder was named 'Aq Sunqur (governor of Aleppo)', a person, although the dossier's own /ledger/5 books the same Aleppo land as great-seljuk-empire's from 1086. Evidence: Tutush I page: in 1086 Malik-Shah's armies advanced and Aq Sunqur was made governor; in 1094 Aq Sunqur and Bozan had switched to Berkyaruq and were defeated 'at Tell Sultan in June-July 1094'. Fix: Counterpart set to 'great-seljuk-empire' (reviewer). great-seljuk-empire has no 1094 loss of Aleppo; its 1092 split names 'Seljuk Syria (Tutush I; Damascus and Aleppo lines)' instead of seljuks-of-syria (routed in cross_checks).

Thin (for a gap-filler):

- `/ledger/2`: Year Tutush annexed Sidon, Tiberias, Ramla, Jaffa and Jerusalem (confidence 1 at 1086; only Jerusalem drawn) (try https://en.wikipedia.org/wiki/Artuk_Bey)
- `/ledger/5`: Fate of Manbij, Azaz and the 1080 belt in 1086 (confidence 1) (try https://en.wikipedia.org/wiki/Aq_Sunqur_al-Hajib)

Spot checks: `/ledger/0` confirmed (Tutush_I); `/ledger/1` confirmed (Tutush_I); `/ledger/3` confirmed (Tutush_I); `/ledger/8` confirmed (Tutush_I); `/ledger/11` confirmed (Ridwan_of_Aleppo); `/ledger/12` confirmed (Ridwan_of_Aleppo).

## kingdom-of-hormuz: fix

Findings:

- `/ledger (new events at 1515 and 1622)`: The kingdom's vassalage to Portugal is not recorded: the ledger has only the loss of the island in 1515. Evidence: Kingdom of Hormuz infobox: 'Vassal state of Portugal (1515-1622)'; text: the kings became 'vassals of the Portuguese state' and 'The Portuguese occupied Ormuz from 1515 to 1622'. Fix: Add vassal_start 1515 / vassal_end 1622 with counterpart portuguese-empire over the remaining kingdom; consider booking the island as occupation_start 1515 / occupation_end 1622 instead of the /ledger/6 loss (the kings stayed on the island).
- `/ledger/8/region`: The 1622 dissolve region includes the island of Hormuz, which /ledger/6 lost in 1515 and keyframe kingdom-of-hormuz_1515 leaves out; the 1622 loss (/ledger/7) has Minab and Qalhat only. Evidence: Keyframe kingdom-of-hormuz_1515 correction: Old Hormuz and Qalhat, without the island. Fix: Make the dissolve region equal the last keyframe (Minab and Qalhat), unless the island is re-booked as an occupation (fix 1), in which case keep it and add it to the 1515 keyframe and the 1622 loss.

Thin (for a gap-filler):

- `/ledger/0`: Foundation year (confidence 1 at 1055; the page says only 11th century) (try https://en.wikipedia.org/wiki/Hormuz_Island)
- `/ledger/1`: When Qalhat was developed or held (confidence 1 at 1300) (try https://en.wikipedia.org/wiki/Qalhat)
- `/ledger/2`: The Jarun acquisition from Kish (confidence 1 at 1301) (try https://en.wikipedia.org/wiki/Kish_Island)
- `/keyframe_review/1`: Extent: the page says the kingdom 'extended as far as Bahrain in the west at its zenith' and Muscat was 'previously a dependency of Hormuz'; neither is drawn (try https://en.wikipedia.org/wiki/Muscat)

Spot checks: `/ledger/3` confirmed (Kingdom_of_Hormuz); `/ledger/4` confirmed (Kingdom_of_Hormuz); `/ledger/6` confirmed (Kingdom_of_Hormuz); `/ledger/8` confirmed (Kingdom_of_Hormuz).

## saltukids: pass

Thin (for a gap-filler):

- `/ledger/3`: When Bayburt and Kars were added (confidence 1 at 1132) (try https://en.wikipedia.org/wiki/Bayburt)

Spot checks: `/ledger/0` confirmed (Saltukids); `/ledger/1` confirmed (Saltukids); `/ledger/2` confirmed (Saltukids); `/ledger/4` confirmed (Saltukids).

## mengujekids: pass

Thin (for a gap-filler):

- `/ledger/2`: Who held Sebinkarahisar and when it passed (confidence 1 at 1228) (try https://en.wikipedia.org/wiki/%C5%9Eebinkarahisar)
- `/keyframe_review/0`: Rum overlordship undated: 'By 1178, Behramshah ... had proved their allegiance to the Rum Seljuks through marriage'; the Divrigi branch's coins recognised Rum; Kemah not drawn (try https://en.wikipedia.org/wiki/Kemah)

Spot checks: `/ledger/0` confirmed (Mengujekids); `/ledger/1` confirmed (Mengujekids); `/ledger/3` confirmed (Mengujekids); `/ledger/2` confirmed (Mengujekids).

## qutlugh-khanids: fix

Findings:

- `/identity/predecessors/1`: kara-khitans is given as a predecessor carrying Kerman province, but the Qara Khitai never held Kerman; the infobox line is the founder's origin, not a land hand-over. Evidence: Qutlugh-Khanids infobox 'Preceded by: Qara Khitai'; the dossier's own note: the founder 'emigrated from the Qara Khitai'; the kara-khitans dossier holds no Kerman land. Fix: Remove the kara-khitans entry from predecessors and keep the origin in notes (khwarezmid-empire remains the land predecessor).
- `/ledger (new events)`: The Khwarazmian vassalage is not recorded, although khwarezmid-empire/ledger/25 has a 1224 vassal_start for Kerman (under the counterpart string 'Burak Hajib of Kerman (Qara Khitai of Kerman)'). Evidence: Qutlugh-Khanids page: 'ruled as vassals of the Khwarazmian Empire, the Mongol Empire and the Ilkhanate' (undated); khwarezmid-empire ledger 25. Fix: Add vassal_start 1224 / vassal_end (Khwarazmian collapse, 1231, confidence 1) with counterpart khwarezmid-empire; khwarezmid-empire should rename its counterpart to 'qutlugh-khanids' and close its vassal_start.

Thin (for a gap-filler):

- `/keyframe_review/0`: Start of Mongol and Ilkhanid suzerainty (undated on the page) (try https://en.wikipedia.org/wiki/Baraq_Hajib)

Spot checks: `/ledger/0` confirmed (Qutlugh-Khanids); `/ledger/1` confirmed (Qutlugh-Khanids); `/ledger/2` confirmed (Qutlugh-Khanids).

## eretnids: thin

Thin (for a gap-filler):

- `/ledger/4`: When the Karamanids regained Konya (confidence 1 at 1352; beylik-of-karaman has no Konya events) (try https://en.wikipedia.org/wiki/Karamanids)
- `/ledger/5`: Year the capital moved from Sivas to Kayseri (confidence 1 at 1352) (try https://en.wikipedia.org/wiki/Eretna)
- `/ledger/8`: Whether the Karamanids kept Nigde and Aksaray after they 'invaded' them (confidence 1 at 1366) (try https://en.wikipedia.org/wiki/Karamanids)
- `/ledger/12`: Court back at Kayseri in 1378 (confidence 1) (try https://en.wikipedia.org/wiki/Kadi_Burhan_al-Din)
- `/keyframe_review/0`: Undated incorporations (Canik, Zile, Develi, Urgup) and who kept Malatya in 1362 (try https://en.wikipedia.org/wiki/Eretna)

Spot checks: `/ledger/1` confirmed (Eretnids); `/ledger/2` confirmed (Eretnids); `/ledger/3` confirmed (Eretnids); `/ledger/6` confirmed (Eretnids); `/ledger/9` confirmed (Kadi_Burhan_al-Din); `/ledger/11` confirmed (Kadi_Burhan_al-Din); `/ledger/13` confirmed (Eretnids).

## burhan-al-din-state: fix

Findings:

- `/ledger/1`: Amasya is gained in 1381 at confidence 2, but the page dates the Amasya campaign to 1384 and says only that Haji Shadgeldi was defeated in 1381. Evidence: Kadi Burhan al-Din page: 'Later that year, Burhan al-Din defeated his main rival, Haji Shadgeldi of Amasya, and declared his sovereignty in Sivas' (1381) and 'launched a campaign against Amasya, defeating its rulers consecutively (1384)'. Fix: Move the Amasya gain to 1384 (split the keyframe: 1381-1383 without Amasya) or keep 1381 at confidence 1 with the 1384 sentence in the note; name the counterpart 'emirate-of-amasya' if that dossier is created.
- `/wars`: The Battle of Kirkdilim (1391/92) on the page is not among the wars. Evidence: Kadi Burhan al-Din page: 'In 1391/92, the Battle of Kirkdilim took place.' Fix: Add it (zones [] if no ground changed hands, and say so), source the Kadi Burhan al-Din page.

Thin (for a gap-filler):

- `/keyframe_review/0`: Kirsehir, Malatya and the advance 'as far as Ankara and Sivrihisar' are undated and not drawn (try https://en.wikipedia.org/wiki/Kadi_Burhan_al-Din)

Spot checks: `/ledger/0` confirmed (Kadi_Burhan_al-Din); `/ledger/1` mis-dated (Kadi_Burhan_al-Din); `/ledger/2` confirmed (Kadi_Burhan_al-Din); `/ledger/3` confirmed (Kadi_Burhan_al-Din).

## atabegs-of-yazd: pass

Thin (for a gap-filler):

- `/keyframe_review/0`: Extent beyond Yazd (Abarkuh, Meybod) and the undated Seljuk/Ilkhanid suzerainty (try https://en.wikipedia.org/wiki/Sam_ibn_Wardanruz)

Spot checks: `/ledger/0` confirmed (Atabegs_of_Yazd); `/ledger/1` confirmed (Atabegs_of_Yazd); `/ledger/2` confirmed (Atabegs_of_Yazd); `/ledger/3` confirmed (Atabegs_of_Yazd).

## ahlatshahs: pass

Thin (for a gap-filler):

- `/identity/rulers`: Rulers before 1128 (Sokmen el-Kutbi from 1100) not in the strip (try https://en.wikipedia.org/wiki/S%C3%B6kmen_el-Kutb%C3%AE)

Spot checks: `/ledger/0` confirmed (Ahlatshahs); `/ledger/1` confirmed (Ahlatshahs); `/keyframe_review/0` confirmed (Ahlatshahs).

## nasrid-dynasty-of-sistan: thin

Thin (for a gap-filler):

- `/ledger`: Three events in 196 years: no rulers 1073-1225, no suzerainty (Ghaznavid, Seljuk, Ghurid, Khwarazmian), start 1029 (infobox, Sistan page) against 1068 (Nasrid page text) (try https://en.wikipedia.org/wiki/Saffarid_dynasty)
- `/keyframe_review/0`: Extent of the realm beyond the Sistan region (try https://en.wikipedia.org/wiki/Zaranj)

Spot checks: `/ledger/0` confirmed (Sistan); `/ledger/1` confirmed (Sistan); `/ledger/2` confirmed (Nasrid_dynasty_(Sistan)).

## mihrabanids: fix

Findings:

- `/ledger (new events)`: Three dated overlordships on the pages opened are missing from the ledger (the notes only ask the suzerains to carry them). Evidence: Mihrabanids page: 'After the foundation of the Ilkhanate by Hulegu Khan in 1256 the maliks recognized the Ilkhans as their overlords'; Sistan page: '1383 Tamerlane conquered Sistan and forced Mihrabanids to become vassals', 'Overlordship of Timurids was ended in 1507 due to Uzbek invasion', 'Uzbeks were driven in 1510 and Mihrabanids became vassals of Safavids until 1537'. Fix: Add vassal_start 1256 (counterpart ulus-of-hulegu) with vassal_end 1335 (confidence 1, the Ilkhanate's collapse), vassal_start 1383 / vassal_end 1507 (timurid-empire), vassal_start 1510 / vassal_end 1537 (safavid-dynasty), region Sistan (plus Quhistan after 1289).

Thin (for a gap-filler):

- `/identity/rulers`: Rulers 1255-1495 (try https://en.wikipedia.org/wiki/Mihrabanids)
- `/wars/1`: Uzbek hold of Sistan 1507-1510 (war only, no occupation events) (try https://en.wikipedia.org/wiki/Sistan)

Spot checks: `/ledger/0` confirmed (Sistan); `/ledger/1` confirmed (Mihrabanids); `/ledger/2` confirmed (Sistan); `/ledger/3` confirmed (Mihrabanids).

## hazaraspids: fix

Findings:

- `/ledger (new events)`: The infobox dates two vassalages that the ledger does not carry. Evidence: Hazaraspids infobox: 'Vassal of the Ilkhanate (1256-1335)' and 'Vassal of Timurid Empire (1393-1424)'. Fix: Add vassal_start 1256 / vassal_end 1335 (counterpart ulus-of-hulegu) and vassal_start 1393 / vassal_end 1424 (counterpart timurid-empire) over the keyframe land, confidence 3 for the years, source the Hazaraspids page.

Thin (for a gap-filler):

- `/ledger/1`: Year of Yusuf Shah I's additions (confidence 1 at 1274) (try https://en.wikipedia.org/wiki/Yusuf_Shah_I)
- `/ledger/2`: Year of Yusuf Shah II's annexation of Shushtar, Hoveizeh and Basra (confidence 1 at 1330) (try https://en.wikipedia.org/wiki/Hoveyzeh)
- `/wars/1`: Muzaffarid capture of Idaj ('temporarily fell into their hands') undated (try https://en.wikipedia.org/wiki/Muzaffarids)

Spot checks: `/ledger/0` confirmed (Hazaraspids); `/ledger/1` confirmed (Hazaraspids); `/ledger/2` confirmed (Hazaraspids); `/ledger/3` confirmed (Hazaraspids).

## khorshidi-dynasty: fix

Findings:

- `/ledger/3/year, /keyframe_review/0/to, /keyframe_review/1` (applied by reviewer): The Mandali gain was placed at 1574 (start of Murad III's reign), before the moment the page gives for the submission. Evidence: Khorshidi dynasty page: 'After the deaths of Shah Tahmasp and Shah Ismail II, he submitted to Sultan Murad III' (Ismail II died November 1577). Fix: Moved to 1578 (reviewer): ledger year 1578 at confidence 1, keyframe khorshidi-dynasty_1184 to 1577, keyframe renamed khorshidi-dynasty_1578 from 1578, notes updated; validates.

Thin (for a gap-filler):

- `/ledger/3`: Exact year of the Murad III territories (still confidence 1); Badra, Jassan and Tursaq not in the gazetteer (try https://en.wikipedia.org/wiki/Ottoman%E2%80%93Safavid_War_(1578%E2%80%931590))

Spot checks: `/ledger/0` confirmed (Khorshidi_dynasty); `/ledger/1` confirmed (Khorshidi_dynasty); `/ledger/2` confirmed (Khorshidi_dynasty); `/ledger/3` mis-dated (Khorshidi_dynasty); `/ledger/5` confirmed (Khorshidi_dynasty).

## banu-munqidh: fix

Findings:

- `/identity/capitals/0`: Kafartab is placed at Shayzar's coordinates (36.5667 E, 35.2678 N), about 20 km south of the town. Evidence: Kafartab page: 'about 4.0 km northwest of Khan Shaykhun' (no coordinates on the page); artuqids/ledger/4 draws Kafr Tab at 36.5953 E, 35.4592 N. Fix: Set Kafartab to about 36.60 E, 35.46 N (a source with coordinates, or the artuqids point), and add Kafartab to the gazetteer request (P:Kafartab is unresolved).
- `/ledger (new events)`: The infobox dates the overlords, which the ledger does not carry. Evidence: Banu Munqidh infobox: 'Country: Mirdasid Emirate (1025-1080); Seljuk Empire (1080-1127); Zengid Atabegate (1127-1157)'. Fix: Add vassal_start/vassal_end pairs: mirdasid-dynasty 1025-1080, great-seljuk-empire 1080-1127 (or seljuks-of-syria for the Syrian Seljuk years if preferred, said in the note), zengid-dynasty 1127-1157, over the keyframe land, confidence 2.

Thin (for a gap-filler):

- `/ledger/1`: When Latakia, Apamea and Kafartab were gained inside Ali's reign (confidence 1 at 1059) (try https://en.wikipedia.org/wiki/Shaizar)
- `/ledger/6`: Fate of Latakia after 1091 (confidence 1 at 1096) (try https://en.wikipedia.org/wiki/Latakia)

Spot checks: `/ledger/0` confirmed (Banu_Munqidh); `/ledger/2` confirmed (Banu_Munqidh); `/ledger/3` confirmed (Banu_Munqidh); `/ledger/4` confirmed (Banu_Munqidh); `/ledger/5` confirmed (Banu_Munqidh); `/ledger/7` confirmed (Banu_Munqidh).

## ahmadilis: fix

Findings:

- `/keyframe_review/0 and /ledger (new 1174 loss)`: Tabriz is not drawn as Ahmadili and there is no 1174 loss, although eldiguzids/ledger/4 gains Tabriz from the Ahmadilis in 1174 and the eldiguzids keyframes 1136-1173 leave out 'Tabriz and Maragheh, held by the Ahmadilis'. Evidence: Eldiguz page: 'Tabriz was also gained from Ahmadilis in 1174'; Eldiguzids page: 'In 1174, Qizil Arslan captured Tabriz'. The Ahmadilis page does not mention Tabriz. Fix: Split the keyframe: 1112-1173 Maragheh plus Tabriz (place Tabriz 40 km, confidence 2, source the Eldiguz page), 1174-1225 Maragheh; add a 1174 loss of Tabriz with counterpart eldiguzids.
- `/identity/rulers`: The ruler strip has gaps 1116-1122 and 1169-1173. Evidence: Ahmadilis page list: 'Aq Sunqur I, 1122-1134', 'Ak Sunkur II, 1134-1169', 'Ala al-Din Korpe Arslan and Rukn al-Din, 1134-1173', 'Falak al-Din, 1173-1189'. Fix: Fill 1169-1173 with Ala al-Din Korpe Arslan and Rukn al-Din (page list) and say in the note that 1116-1122 has no ruler on the page.

Thin (for a gap-filler):

- `/ledger/0`: Start 1111/12 (Maragheh page) against the infobox 1122 (try https://en.wikipedia.org/wiki/Aq_Sunqur_Ahmadili)

Spot checks: `/ledger/0` confirmed (Maragheh); `/ledger/1` confirmed (Ahmadilis); `/ledger/2` confirmed (Ahmadilis); `/wars/2` confirmed (Maragheh).

## Cross-dossier matrix

Territorial events only (gain, loss, vassal, occupation, split). Exceptions are counterparts that are not dossier slugs (unnamed holders, local lords) or owned by eu-19, which has not run.

| event | counterpart | mirror | status | note |
| --- | --- | --- | --- | --- |
| artuqids /ledger/1 1108 gain | Ibrahim ibn Sökmen (Artuqid of Hasankeyf) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| artuqids /ledger/2 1117 gain | seljuks-of-syria | seljuks-of-syria 1117 loss | matched |  |
| artuqids /ledger/3 1118 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| artuqids /ledger/4 1119 gain | principality-of-antioch | principality-of-antioch 1119 loss | matched |  |
| artuqids /ledger/5 1119 loss | principality-of-antioch | principality-of-antioch 1119 gain | matched |  |
| artuqids /ledger/6 1120 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| artuqids /ledger/7 1128 loss | zengid-dynasty | zengid-dynasty 1128 gain | matched |  |
| artuqids /ledger/8 1185 gain | Kara Arslan's line of Hasankeyf-Diyarbakir (Artuqid) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| artuqids /ledger/9 1198 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| artuqids /ledger/11 1232 loss | ayyubid-sultanate | - | missing | ayyubid-sultanate (me-09) has no mirror within a year; route to that group. |
| artuqids /ledger/12 1232 loss | ayyubid-sultanate | - | missing | ayyubid-sultanate (me-09) has no mirror within a year; route to that group. |
| artuqids /ledger/14 1234 loss | sultanate-of-rum | - | missing | sultanate-of-rum (me-09) has no mirror within a year; route to that group. |
| artuqids /ledger/15 1409 loss | qara-qoyunlu | qara-qoyunlu 1409 gain | mismatch | qara-qoyunlu/ledger/6 gains Mardin under the counterpart string 'Artuqids of Mardin'; it should read 'artuqids'. |
| nizari-ismaili-state /ledger/1 1096 gain | great-seljuk-empire | - | missing | great-seljuk-empire (me-09) has no mirror within a year; route to that group. |
| nizari-ismaili-state /ledger/2 1100 gain | great-seljuk-empire | - | missing | great-seljuk-empire (me-09) has no mirror within a year; route to that group. |
| nizari-ismaili-state /ledger/4 1102 gain | great-seljuk-empire | - | missing | great-seljuk-empire (me-09) has no mirror within a year; route to that group. |
| nizari-ismaili-state /ledger/6 1133 gain | Saif al-Mulk ibn Amrun (emir of al-Kahf) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| nizari-ismaili-state /ledger/7 1138 gain | Banu Amrun (Saif's son Musa) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| nizari-ismaili-state /ledger/8 1140 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| nizari-ismaili-state /ledger/9 1141 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| nizari-ismaili-state /ledger/10 1157 occupation_start | Banu Munqidh (Shaizar) | - | mismatch | counterpart string 'Banu Munqidh (Shaizar)' should be banu-munqidh; banu-munqidh/ledger/7 hands Shaizar to zengid-dynasty in 1157 with no Assassin step, and zengid-dynasty has no 1158 Shaizar gain. |
| nizari-ismaili-state /ledger/11 1158 occupation_end | Banu Munqidh (Shaizar) | - | mismatch | see 1157 occupation_start. |
| nizari-ismaili-state /ledger/12 1162 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| nizari-ismaili-state /ledger/14 1256 loss | ulus-of-hulegu | ulus-of-hulegu 1256 gain | matched |  |
| nizari-ismaili-state /ledger/15 1256 loss | ulus-of-hulegu | ulus-of-hulegu 1256 gain | matched |  |
| nizari-ismaili-state /ledger/16 1257 loss | ulus-of-hulegu | ulus-of-hulegu 1256 gain | matched |  |
| nizari-ismaili-state /ledger/17 1270 loss | mamluk-sultanate | mamluk-sultanate 1271 gain | matched |  |
| nizari-ismaili-state /ledger/18 1270 loss | ulus-of-hulegu | - | missing | ulus-of-hulegu (ia-02) has no mirror within a year; route to that group. |
| nizari-ismaili-state /ledger/20 1271 loss | mamluk-sultanate | mamluk-sultanate 1271 gain | matched |  |
| nizari-ismaili-state /ledger/21 1273 loss | mamluk-sultanate | - | missing | mamluk-sultanate (me-09) has no mirror within a year; route to that group. |
| eldiguzids /ledger/1 1137 gain | great-seljuk-empire | - | missing | great-seljuk-empire (me-09) has no mirror within a year; route to that group. |
| eldiguzids /ledger/2 1160 vassal_start | great-seljuk-empire | - | mismatch | great-seljuk-empire draws Persian Iraq as direct Seljuk land to 1194 and has no vassal event naming eldiguzids; one reading must be chosen (flagged by the author). |
| eldiguzids /ledger/3 1169 gain | Inanch (atabeg of Rey) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| eldiguzids /ledger/4 1174 gain | ahmadilis | - | mismatch | ahmadilis has no 1174 loss of Tabriz and never draws Tabriz (fix listed under ahmadilis). |
| eldiguzids /ledger/7 1191 vassal_start | shirvan | - | exception | shirvan is owned by eu-19, which has not run yet (no dossier). |
| eldiguzids /ledger/9 1194 vassal_end | great-seljuk-empire | - | mismatch | see eldiguzids 1160 vassal_start. |
| eldiguzids /ledger/11 1195 loss | kingdom-of-georgia | - | exception | kingdom-of-georgia is owned by eu-19, which has not run yet (no dossier). |
| eldiguzids /ledger/12 1195 vassal_end | shirvan | - | exception | shirvan is owned by eu-19, which has not run yet (no dossier). |
| eldiguzids /ledger/13 1196 gain | kingdom-of-georgia | - | exception | kingdom-of-georgia is owned by eu-19, which has not run yet (no dossier). |
| eldiguzids /ledger/14 1225 loss | khwarezmid-empire | khwarezmid-empire 1225 gain | matched |  |
| kerman-seljuk-sultanate /ledger/1 1053 vassal_start | Oman (Seljuk suzerainty) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| kerman-seljuk-sultanate /ledger/2 1154 vassal_end | Oman (Seljuk suzerainty) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| kerman-seljuk-sultanate /ledger/3 1186 loss | Ghuzz Turks of Kerman (Malik Dinar) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| salghurids /ledger/1 1203 occupation_start | holder of Isfahan (not named by the page) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| salghurids /ledger/2 1204 occupation_end | holder of Isfahan (not named by the page) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| salghurids /ledger/3 1230 gain | Kish (ruler not named by the page) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| salghurids /ledger/4 1236 occupation_start | uyunid-emirate | - | missing | uyunid-emirate (me (Arabia)) has no mirror within a year; route to that group. |
| salghurids /ledger/5 1253 occupation_end | uyunid-emirate | - | missing | uyunid-emirate (me (Arabia)) has no mirror within a year; route to that group. |
| burid-dynasty /ledger/1 1110 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| burid-dynasty /ledger/2 1122 gain | fatimid-caliphate | fatimid-caliphate 1124 loss | mismatch | fatimid-caliphate keeps Tyre to 1124 and loses it to kingdom-of-jerusalem; the Toghtekin page has the Fatimids selling Tyre to Toghtekin in 1122. fatimid-caliphate should lose Tyre to burid-dynasty in 1122. |
| burid-dynasty /ledger/3 1124 loss | kingdom-of-jerusalem | kingdom-of-jerusalem 1124 gain | mismatch | kingdom-of-jerusalem/ledger/8 gains Tyre from fatimid-caliphate; it should name burid-dynasty (Toghtekin page: Franks took it from Toghtekin's garrison on 7 July 1124). |
| burid-dynasty /ledger/4 1128 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| burid-dynasty /ledger/5 1130 loss | zengid-dynasty | zengid-dynasty 1130 gain | matched |  |
| burid-dynasty /ledger/6 1138 loss | zengid-dynasty | zengid-dynasty 1138 gain | matched |  |
| burid-dynasty /ledger/7 1139 loss | zengid-dynasty | zengid-dynasty 1138 gain | matched |  |
| burid-dynasty /ledger/8 1154 loss | zengid-dynasty | zengid-dynasty 1154 gain | matched |  |
| seljuks-of-syria /ledger/1 1080 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| seljuks-of-syria /ledger/2 1086 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| seljuks-of-syria /ledger/3 1086 occupation_start | holder of Aleppo (not named by the page) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| seljuks-of-syria /ledger/4 1086 occupation_end | holder of Aleppo (not named by the page) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| seljuks-of-syria /ledger/5 1086 loss | great-seljuk-empire | - | missing | great-seljuk-empire (me-09) has no mirror within a year; route to that group. |
| seljuks-of-syria /ledger/6 1092 occupation_start | holders not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| seljuks-of-syria /ledger/7 1093 occupation_end | holders not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| seljuks-of-syria /ledger/8 1094 gain | great-seljuk-empire | - | missing | great-seljuk-empire has no 1094 loss of Aleppo; its 1092 split names 'Seljuk Syria (Tutush I; Damascus and Aleppo lines)' instead of seljuks-of-syria. |
| seljuks-of-syria /ledger/10 1098 loss | fatimid-caliphate | fatimid-caliphate 1098 gain | mismatch | fatimid-caliphate/ledger/49 names 'Artuqids' (the governors) as counterpart; it should be seljuks-of-syria, whose governors they were (artuqids starts 1102). |
| seljuks-of-syria /ledger/11 1104 loss | burid-dynasty | burid-dynasty 1104 found | matched |  |
| seljuks-of-syria /ledger/12 1117 loss | artuqids | artuqids 1117 gain | matched |  |
| kingdom-of-hormuz /ledger/1 1300 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| kingdom-of-hormuz /ledger/2 1301 gain | Kish (Neyn, King of Keys) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| kingdom-of-hormuz /ledger/6 1515 loss | portuguese-empire | portuguese-empire 1515 gain | mismatch | portuguese-empire/ledger/10 uses the counterpart string 'Hormuz (Huwala state)'; it should read 'kingdom-of-hormuz' (and a vassal pair 1515-1622 is missing on both sides). |
| kingdom-of-hormuz /ledger/7 1622 loss | safavid-dynasty | safavid-dynasty 1622 gain | mismatch | safavid-dynasty/ledger/42 gains Hormuz from portuguese-empire only; no gain of the mainland kingdom from kingdom-of-hormuz. |
| saltukids /ledger/1 1077 loss | byzantine-empire | - | missing | byzantine-empire (eu-05) has no mirror within a year; route to that group. |
| saltukids /ledger/2 1079 gain | byzantine-empire | - | missing | byzantine-empire (eu-05) has no mirror within a year; route to that group. |
| saltukids /ledger/3 1132 gain | holder not named by the page | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| saltukids /ledger/4 1202 loss | sultanate-of-rum | sultanate-of-rum 1202 gain | matched |  |
| mengujekids /ledger/1 1228 loss | sultanate-of-rum | - | missing | sultanate-of-rum (me-09) has no mirror within a year; route to that group. |
| mengujekids /ledger/2 1228 loss | sultanate-of-rum | - | missing | sultanate-of-rum (me-09) has no mirror within a year; route to that group. |
| mengujekids /ledger/3 1277 loss | ulus-of-hulegu | - | missing | ulus-of-hulegu (ia-02) has no mirror within a year; route to that group. |
| qutlugh-khanids /ledger/1 1306 loss | ulus-of-hulegu | - | missing | ulus-of-hulegu (ia-02) has no mirror within a year; route to that group. |
| eretnids /ledger/1 1338 loss | beylik-of-dulkadir | - | missing | beylik-of-dulkadir (me-09) has no mirror within a year; route to that group. |
| eretnids /ledger/2 1343 gain | Mongol warlords competing to restore the Ilkhanate (Hasan Kuchak's army under Suleiman Khan) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| eretnids /ledger/3 1350 gain | beylik-of-karaman | - | missing | beylik-of-karaman (me-09) has no mirror within a year; route to that group. |
| eretnids /ledger/4 1352 loss | beylik-of-karaman | - | missing | beylik-of-karaman (me-09) has no mirror within a year; route to that group. |
| eretnids /ledger/6 1361 loss | ottoman-empire | ottoman-empire 1363 gain | mismatch | ottoman-empire/ledger/9 gains Ankara in 1363 from 'ahi-republic'; the Eretnids page has Murad I take Ankara Castle from the Eretnids in 1361. |
| eretnids /ledger/7 1365 loss | Ahi Ayna (local ruler of Erzincan, Erzurum and Bayburt) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| eretnids /ledger/8 1366 loss | beylik-of-karaman | - | missing | beylik-of-karaman (me-09) has no mirror within a year; route to that group. |
| eretnids /ledger/9 1375 loss | beylik-of-karaman | - | missing | beylik-of-karaman (me-09) has no mirror within a year; route to that group. |
| eretnids /ledger/11 1378 gain | beylik-of-karaman | - | missing | beylik-of-karaman (me-09) has no mirror within a year; route to that group. |
| eretnids /ledger/13 1381 loss | burhan-al-din-state | burhan-al-din-state 1381 found | matched |  |
| burhan-al-din-state /ledger/1 1381 gain | Haji Shadgeldi of Amasya | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| burhan-al-din-state /ledger/2 1398 loss | ottoman-empire | ottoman-empire 1395 gain | mismatch | ottoman-empire/ledger/23 gains the Sivas region in 1395 from 'Anatolian beyliks of the Sivas region (no page opened names them)'; the Kadi Burhan al-Din page puts the Ottoman takeover after his death in July-August 1398 ('the Ottomans soon captured Sivas'). |
| atabegs-of-yazd /ledger/1 1297 occupation_start | ulus-of-hulegu | - | missing | ulus-of-hulegu (ia-02) has no mirror within a year; route to that group. |
| atabegs-of-yazd /ledger/2 1315 occupation_end | ulus-of-hulegu | - | missing | ulus-of-hulegu (ia-02) has no mirror within a year; route to that group. |
| atabegs-of-yazd /ledger/3 1319 loss | muzaffarids | muzaffarids 1319 gain | matched |  |
| ahlatshahs /ledger/1 1207 loss | ayyubid-sultanate | - | missing | ayyubid-sultanate (me-09) has no mirror within a year; route to that group. |
| nasrid-dynasty-of-sistan /ledger/1 1225 loss | khwarezmid-empire | - | missing | khwarezmid-empire (me-09) has no mirror within a year; route to that group. |
| mihrabanids /ledger/1 1289 gain | holders of Quhistan (the page names none) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| mihrabanids /ledger/2 1537 loss | safavid-dynasty | - | missing | safavid-dynasty (me-10) has no mirror within a year; route to that group. |
| hazaraspids /ledger/1 1274 gain | holders of Khuzestan, Kuhgiluya, Firuzan and Golpayegan (the page names none) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| hazaraspids /ledger/2 1330 gain | holders of Basra and Shushtar (the page names none) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| hazaraspids /ledger/3 1424 loss | timurid-empire | - | missing | timurid-empire (ia-02) has no mirror within a year; route to that group. |
| khorshidi-dynasty /ledger/1 1395 occupation_start | timurid-empire | - | missing | timurid-empire (ia-02) has no mirror within a year; route to that group. |
| khorshidi-dynasty /ledger/2 1405 occupation_end | timurid-empire | - | missing | timurid-empire (ia-02) has no mirror within a year; route to that group. |
| khorshidi-dynasty /ledger/3 1578 gain | ottoman-empire | - | missing | ottoman-empire (me-10) has no mirror within a year; route to that group. |
| khorshidi-dynasty /ledger/4 1597 loss | safavid-dynasty | - | missing | safavid-dynasty (me-10) has no mirror within a year; route to that group. |
| banu-munqidh /ledger/1 1059 gain | holders of Latakia, Apamea and Kafartab (the page names none) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| banu-munqidh /ledger/2 1081 gain | byzantine-empire | - | missing | byzantine-empire (eu-05) has no mirror within a year; route to that group. |
| banu-munqidh /ledger/3 1086 loss | great-seljuk-empire | - | missing | great-seljuk-empire (me-09) has no mirror within a year; route to that group. |
| banu-munqidh /ledger/4 1091 gain | Aq Sunqur al-Hajib (Seljuk governor of Aleppo) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| banu-munqidh /ledger/5 1096 loss | Khalaf ibn Mula'ib (former lord of Homs) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| banu-munqidh /ledger/6 1096 loss | holder of Latakia (the page names none) | - | exception | counterpart is not a dossier slug (unnamed holder, local lord or a state listed under counterparts_needing_dossiers); accepted. |
| banu-munqidh /ledger/7 1157 loss | zengid-dynasty | - | missing | zengid-dynasty (me-09) has no mirror within a year; route to that group. |
| ahmadilis /ledger/1 1225 loss | khwarezmid-empire | - | missing | khwarezmid-empire (me-09) has no mirror within a year; route to that group. |
| great-seljuk-empire /ledger/26 1074 vassal_start | kerman-seljuk-sultanate | - | missing | kerman-seljuk-sultanate carries no vassal_start (fix listed). |
| great-seljuk-empire /ledger/62 1187 vassal_end | kerman-seljuk-sultanate | - | missing | kerman-seljuk-sultanate carries no vassal_end (fix listed). |
| khwarezmid-empire /ledger/16 1217 vassal_start | eldiguzids | - | missing | eldiguzids carries no vassal_start (fix listed). |
| khwarezmid-empire /ledger/26 1225 vassal_end | eldiguzids | - | missing | eldiguzids carries no vassal_end (fix listed). |
| khwarezmid-empire /ledger/25 1224 vassal_start | Burak Hajib of Kerman (Qara Khitai of Kerman) | - | mismatch | should name qutlugh-khanids and be closed with a vassal_end; qutlugh-khanids carries no vassal events (fix listed). |
| qara-qoyunlu /ledger/1 1384 vassal_start | Artuqids of Mardin | - | mismatch | should name artuqids; artuqids carries no 1384 vassal_start (fix listed). |
| great-seljuk-empire /ledger/40 1092 split | Seljuk Syria (Tutush I; Damascus and Aleppo lines) | - | mismatch | should name seljuks-of-syria, which starts in 1078 at Damascus (found from great-seljuk-empire, unmirrored). |

## Gazetteer names needed

Hasankeyf (artuqids), Mayyafariqin (artuqids), Alamut (nizari-ismaili-state), Masyaf (nizari-ismaili-state), Gerdkuh (nizari-ismaili-state), Qadmus (nizari-ismaili-state), Rudkhan (nizari-ismaili-state), Lambsar (nizari-ismaili-state), Kahf (nizari-ismaili-state), Khawabi (nizari-ismaili-state), Shaizar (nizari-ismaili-state), Ullaiqah (nizari-ismaili-state), Tabas (nizari-ismaili-state), Kish (salghurids), Mayyafariqin (seljuks-of-syria), Minab (kingdom-of-hormuz), Qalhat (kingdom-of-hormuz), Divriği (mengujekids), Şebinkarahisar (mengujekids), Şebinkarahisar (eretnids), Şebinkarahisar (burhan-al-din-state), Kafartab (banu-munqidh).

## Problems

- WebFetch returns model-summarised page text; quoted sentences are as the tool returned them.
- No article in this batch has an infobox area and none of the 21 states has a Cliopatria shape, so every area_check is empty by necessity (ratio null).
- The Kafartab page gives no coordinates, so the banu-munqidh capital fix was left to the author.
- Reviewer edits applied and re-validated (no errors): eldiguzids (/ledger/4 counterpart), seljuks-of-syria (/ledger/8 counterpart), kerman-seljuk-sultanate (/identity/successors/0 slug, /ledger/0 note), khorshidi-dynasty (Mandali 1574 to 1578: /ledger/3, /keyframe_review/0-1, notes). Pre-edit copies are in /tmp/claude-0/work/me-09-x/bak/.
- Most unmatched mirrors sit in other groups' dossiers (great-seljuk-empire, khwarezmid-empire, ulus-of-hulegu, ayyubid-sultanate, sultanate-of-rum, beylik-of-karaman, beylik-of-dulkadir, timurid-empire, safavid-dynasty, ottoman-empire, byzantine-empire, zengid-dynasty, mamluk-sultanate, uyunid-emirate): see cross_checks with status missing or mismatch.
- kingdom-of-georgia and shirvan (eu-19) have no dossiers yet; the eldiguzids events naming them are exceptions.
