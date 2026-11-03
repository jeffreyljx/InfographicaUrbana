# Review: batch me-09-h (Phase B, 2026-10-25)

Reviewer: adversarial review of qara-qoyunlu, aq-qoyunlu, muzaffarids, sarbadars, ramadanid-emirate, hashemite-arab-federation. Validator (--resolve): 0 errors in all six; one warning (muzaffarids: atabegs-of-yazd has no dossier, listed by the author). Neighbour dossiers read (ledgers grepped): timurid-empire, jalayirid-sultanate, mamluk-sultanate, ottoman-empire, beylik-of-dulkadir, injuids, kartids, ilkhanate, kingdom-of-iraq, armenian-kingdom-of-cilicia, empire-of-trebizond, bahrani-dynasty, kingdom-of-cyprus, golden-horde, white-horde, chobanids, germiyanids, chagatai-khanate. Not written yet (counted as groups not run): beylik-of-karaman, kingdom-of-georgia, shirvan, samtskhe-saatabago, beylik-of-isfendiyar, safavid-dynasty, kingdom-of-kartli, iraqi-republic.

Pages opened (WebFetch): Qara_Yusuf, Qara_Qoyunlu, Jahan_Shah, Jalayirid_Sultanate, Uzun_Hasan, Aq_Qoyunlu, Muzaffarids_(Iran), Injuids, Sarbadars, Ramadanid_Emirate, Arab_Federation. All loaded.

Fixes applied by the reviewer are marked [applied]; the rest are for the author or a gap-filler. [blocking] marks what must change before acceptance.

## qara-qoyunlu: fix

Area: infobox 520000 km2 (year None), Cliopatria 516574 km2, ratio 0.99, acknowledged True. Infobox gives no year; author ties it to a 1458 map; the 1440-1462 shape is 516,574 km2. The corrected 1453-1462 extent (with central Iran) is larger, as the author notes.

Findings:
- [applied] [blocking] `/keyframe_review/6 and new /keyframe_review/7 (qara-qoyunlu_1432)`: The c3 gain of lower Iraq in 1432 (/ledger/18) had no trace in the keyframes: qara-qoyunlu_1415 (ok, 1415-1439) omits Hillah, Wasit and Basra, and the Cliopatria 'Hashemite Arab Federation' shapes that drew that land are marked wrong, so lower Iraq was blank 1432-1439. Evidence: Jalayirid Sultanate page: Aspan 'managed to capture al-Hella in October 1431', Husayn II killed 9 November 1431, dynasty eliminated 'by the Qara Qoyunlu in 1432'; capital Basra 1411-1432. Fix: Applied: qara-qoyunlu_1415 set to adjust ('unchanged for 1415-1431; superseded from 1432'); new keyframe qara-qoyunlu_1432 (1432-1439) = union(Cliopatria Qara Qoyunlu 1415, the /ledger/18 lower-Iraq region), source Jalayirid page. Validates.
- [applied] `/ledger/8`: 1409 gain of Sultaniyya/Zanjan at confidence 2, but the cited page gives no outcome for the expedition. Evidence: Qara Yusuf page: 'Another invasion force was sent to capture Sultaniyya and Qazvin under the command of Rustam Beg' (1409 section); no result stated. Fix: Applied: confidence 1 and a reviewer sentence quoting the page.
- [applied] `/ledger/20/counterpart`: The note said the Jahan Shah page names no previous holder of Baghdad; it does. Evidence: Jahan Shah page: Ispend, Jahan Shah's brother, 'had ruled over Baghdad and its environs for twelve years' before dying in 1445; 'Baghdad was captured on 9 June 1446'. Fix: Applied: counterpart "Ispend's line at Baghdad (Qara Qoyunlu appanage)" and the note rewritten with the quote.
- `/ledger/29 and /ledger/30 region`: The 1468 loss and dissolve name only the raw Cliopatria 1467 shape, which (per this dossier's own qara-qoyunlu_1453/_1463 corrections) lacks Hamadan, Qazvin and central Iran; the central-Iranian land therefore passes to no one in 1468, and aq-qoyunlu picks it up only in 1475 'from qara-qoyunlu'. Evidence: Qara Qoyunlu page: 'by 1468, the Aq Qoyunlu defeated the Qara Qoyunlu and conquered Iraq, Azerbaijan, and western Iran'; keyframe qara-qoyunlu_1463 correction adds Hamadan, Qazvin and central Iran. Fix: Make /ledger/29's region the corrected 1463 extent (the union used in qara-qoyunlu_1463), so it pairs with the re-dated aq-qoyunlu gain (see aq-qoyunlu /ledger/11).
- `/ledger/3, /ledger/4, /ledger/11 against timurid-empire /ledger/22 and jalayirid-sultanate /ledger/16`: Azerbaijan 1406-1410 is modelled three ways: timurid-empire loses Azerbaijan and Armenia to qara-qoyunlu on 14 October 1406 (c3); this dossier gains only Van in 1406 (c1), keeps Tabriz contested 1406-1408 and gains Armenia in 1410 from 'nobody'; jalayirid-sultanate gains Tabriz from qara-qoyunlu in 1406, which has no mirror here. Iranian Azerbaijan outside the Tabriz radius and Armenia are drawn by nobody 1406-1410. Evidence: Qara Yusuf page: 'defeated the Timurid Abu Bakr at the Battle of Nakhchivan on 14 October 1406 and reoccupied Tabriz'; the agreement in prison gave 'Azerbaijan' to Qara Yusuf; Sardrud (20 April 1408) 'nullified the results of Timur's conquests in the West'; 'In 1409 he entered Tabriz'. Qara Qoyunlu page: 'In 1410, Armenia fell under the control of the Qara Qoyunlu' (no previous holder). Fix: Agree one version with the timurid-empire (ia-02) and jalayirid-sultanate owners: either gain Azerbaijan/Armenia (minus the Tabriz radius held by Ahmad) from timurid-empire in 1406 or 1408 with a keyframe for 1408-1409, or ask ia-02 to move its loss; give the 1410 Armenia gain a real counterpart (timurid-empire per its 1406 loss) instead of 'nobody'.

Thin (for a gap-filler):
- `/ledger/3`: Year and extent of Qara Yusuf's return to Van (c1, bridged at 1406) (try https://en.wikipedia.org/wiki/Qara_Iskander)
- `/ledger/8`: Outcome of the 1409 expedition to Sultaniyya and Qazvin (now c1) (try https://en.wikipedia.org/wiki/Qara_Iskander)
- `/ledger/23`: Date of the Kerman conquest (c1; 'Qasim Beg was assigned to Kerman', undated) (try https://en.wikipedia.org/wiki/Jahan_Shah)
- `/ledger/26`: Start of Pir Budaq's revolt at Baghdad (a rebel holding a city; perhaps a rebel dossier if he held it a year or more) (try https://en.wikipedia.org/wiki/Jahan_Shah)

Spot checks:
- `/ledger/1` on https://en.wikipedia.org/wiki/Qara_Qoyunlu: confirmed (invaded Mardin in 1384, Artuqid submission)
- `/ledger/14` on https://en.wikipedia.org/wiki/Qara_Yusuf: confirmed (Ahmad defeated near Tabriz 30 August 1410, executed next day)
- `/ledger/20` on https://en.wikipedia.org/wiki/Jahan_Shah: confirmed (9 June 1446 after a seven-month siege); counterpart corrected
- `/ledger/21` on https://en.wikipedia.org/wiki/Qara_Qoyunlu: confirmed (Sultaniya, Hamadan, Qazvin after Shah Rukh's 1447 death)
- `/ledger/22` on https://en.wikipedia.org/wiki/Jahan_Shah: confirmed (1452-1453: Savah, Qumm, Isfahan, Shiraz, Yazd)
- `/ledger/24` on https://en.wikipedia.org/wiki/Jahan_Shah: confirmed (summer 1458, occupation of Herat for six months)
- `/ledger/29` on https://en.wikipedia.org/wiki/Qara_Qoyunlu: confirmed (by 1468 Aq Qoyunlu took Iraq, Azerbaijan, western Iran)
- `/ledger/8` on https://en.wikipedia.org/wiki/Qara_Yusuf: not on page as a gain: force sent, no outcome (confidence lowered to 1)
- `/ledger/18` on https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed (al-Hilla October 1431, elimination 1432)

## aq-qoyunlu: fail

Area: infobox None km2 (year None), Cliopatria 1701512 km2, ratio None, acknowledged True. The Aq Qoyunlu infobox has no area figure; the author says so.

Findings:
- [blocking] `/ledger/11 and /keyframe_review/8`: The largest land move in the batch, the conquest of Hamadan, Qazvin, Isfahan, Fars, Yazd and Kerman, is a gain 'from qara-qoyunlu' dated 1475, seven years after qara-qoyunlu dissolved (1468); qara-qoyunlu has no 1475 loss, and aq-qoyunlu_1468 is 'ok' without that land, so about a million km2 of central Iran that qara-qoyunlu held to 1468 is drawn by nobody 1468-1474. Evidence: Qara Qoyunlu page: 'by 1468, the Aq Qoyunlu defeated the Qara Qoyunlu and conquered Iraq, Azerbaijan, and western Iran'. Aq Qoyunlu page: Battle of Qarabagh 1469 against Abu Sa'id, who came with Hasan Ali's help; 'conquered most of mainland Iran', Khalil governor of Fars (no year). Uzun Hasan page: 'took the kingdom of Persia from Causa [Hasan Ali], whom he put to death' (no year). Shapes: aq-qoyunlu_1468 697,815 km2 to 49.6 E; aq-qoyunlu_1475 1,701,512 km2. Fix: Re-date the gain to 1468 (pairing with qara-qoyunlu's 1468 loss/dissolve) or 1469 (Hasan Ali's end), counterpart qara-qoyunlu, region the central-Iranian provinces of qara-qoyunlu_1453 (Hamadan, Qazvin, Markazi, Qom, Esfahan, Fars, Yazd, Kerman), confidence 2; set aq-qoyunlu_1468 to adjust = union(Cliopatria Aq Qoyunlu 1468, those provinces) from that year; ask that qara-qoyunlu /ledger/29 name the same land.
- `/keyframe_review/9`: aq-qoyunlu_1475 is 'ok' although its own note says no page confirms Mazandaran, Semnan, Tehran, Gilan or the reach to 61 E. Evidence: Author's note on the keyframe; Aq Qoyunlu page names Isfahan, Fars, Kerman, Iraq-i Ajam only. Fix: Either adjust (minus Gilan, Mazandaran, Golestan and the Sistan/South Khorasan reach) or say why the generous shape is kept.

Thin (for a gap-filler):
- `/ledger/3`: Who held Raqqa and Hasakah before 1415 and whether the Aq Qoyunlu took them (c1, counterpart guessed) (try https://en.wikipedia.org/wiki/Mamluk_Sultanate)
- `/ledger/12 and /ledger/15`: Years of Hormuz's recognition of Aq Qoyunlu suzerainty (c1 pair 1475-1503) (try https://en.wikipedia.org/wiki/Kingdom_of_Ormus)
- `/keyframe_review/4`: Aq Qoyunlu holdings 1435-1452 and the Mamluk suzerainty of 1433 that mamluk-sultanate records but these notes only mention (try https://en.wikipedia.org/wiki/Uzun_Hasan)

Spot checks:
- `/ledger/1` on https://en.wikipedia.org/wiki/Aq_Qoyunlu: confirmed ('Timur granted them all of Diyar Bakr', 1402)
- `/ledger/4` on https://en.wikipedia.org/wiki/Uzun_Hasan: confirmed ('In 1465, Hassan attacked and captured Harput from the Beylik of Dulkadir')
- `/ledger/7` on https://en.wikipedia.org/wiki/Qara_Qoyunlu: confirmed (by 1468: Iraq, Azerbaijan, western Iran)
- `/ledger/9` on https://en.wikipedia.org/wiki/Aq_Qoyunlu: confirmed (Herat temporarily captured July 1470)
- `/ledger/14` on https://en.wikipedia.org/wiki/Aq_Qoyunlu: confirmed (Iraq-Ajami, Fars and Kerman, summer 1503)
- `/ledger/17` on https://en.wikipedia.org/wiki/Aq_Qoyunlu: confirmed (Mesopotamia, autumn 1508)
- `/ledger/11` on https://en.wikipedia.org/wiki/Uzun_Hasan: not on page as dated: no year for the conquest of central Iran (c1); counterpart dissolved

## muzaffarids: fix

Area: infobox None km2 (year None), Cliopatria 369514 km2, ratio None, acknowledged True. No area in the infobox.

Findings:
- [applied] [blocking] `/keyframe_review/7 and new /keyframe_review/8 (muzaffarids_1387)`: The 1387 loss of Isfahan to Timur (/ledger/14, matched by timurid-empire's 1387 gain of Esfahan) had no trace in the keyframes: muzaffarids_1385 kept Isfahan (about 107,000 km2) to 1393. Evidence: Muzaffarids (Iran) page: 'a slaughter of the populace, in the Sacking of Isfahan (1387)'; timurid-empire /ledger/3 gains Esfahan from muzaffarids in 1387. Fix: Applied: muzaffarids_1385 text limited to 1385-1386; new keyframe muzaffarids_1387 (1387-1393) = union(Kerman, Yazd, Fars). Validates (the atabegs-of-yazd warning remains, listed under counterparts).

Thin (for a gap-filler):
- `/keyframe_review`: Persian Iraq and Azerbaijan 'at the zenith', Bam, Hormuz and Khuzestan holdings, undated on the page (try https://www.iranicaonline.org/articles/mozaffarids)

Spot checks:
- `/ledger/2` on https://en.wikipedia.org/wiki/Muzaffarids_(Iran): confirmed ('permanently gained control of Kirman in late 1340')
- `/ledger/5` on https://en.wikipedia.org/wiki/Injuids: confirmed ('Fars was absorbed by 1357 into the expanding Muzaffarid state')
- `/ledger/6` on https://en.wikipedia.org/wiki/Injuids: confirmed (Isfahan 'captured it in 1357')
- `/ledger/10` on https://en.wikipedia.org/wiki/Muzaffarids_(Iran): confirmed (Shah Mahmud captured Shiraz 1364; Jalayirid page: Uways occupied Shiraz)
- `/ledger/11` on https://en.wikipedia.org/wiki/Muzaffarids_(Iran): confirmed ('would not be able to reconquer his capital until 1366')
- `/ledger/8` on https://en.wikipedia.org/wiki/Jalayirid_Sultanate: confirmed (Azerbaijan and Arran for four months, Tabriz)
- `/ledger/16` on https://en.wikipedia.org/wiki/Muzaffarids_(Iran): confirmed (Battle of Shiraz 1393; Disestablished 1393)

## sarbadars: thin

Area: infobox None km2 (year None), Cliopatria 418562 km2, ratio None, acknowledged True. No area in the infobox; all Cliopatria shapes corrected to the small core.

Findings:
- `/keyframe_review/3`: sarbadars_1352 (1352-1362) includes Tus (Mashhad) for 1352, a year before the 1353 gain of Tus (/ledger/5). Evidence: Sarbadars page: Tus among the gains after Togha Temur's death in late 1353. Fix: Say in the note that Tus is drawn a year early, or give the 1352 keyframe without Mashhad.
- `/keyframe_review/6`: sarbadars_1375 removes Nishapur from 1375, a year before the c. 1376 loss (/ledger/9). Evidence: Sarbadars page: 'At about the same time, Nishapur was conquered by the Kartids' (c. 1376); kartids /ledger/1 dates it 1376. Fix: Acceptable within the c. 1375-76 range; mention it in the note.

Thin (for a gap-filler):
- `/ledger/6`: How long the 1353 gains (Ray, Astarabad, Shasman) lasted (c1) (try https://en.wikipedia.org/wiki/Togha_Temur)
- `/ledger/10`: End year: the page says the Sarbadars reigned 'until Khwaja Ali-yi Mu'ayyad submitted to Timur in 1381'; the dossier runs to 1386 ('my choice') and timurid-empire has no vassal_start sarbadars 1381 or gain of Sabzevar (try https://www.iranicaonline.org/articles/sarbedarids)
- `/keyframe_review/5`: Sarbadar holdings 1354-1375 beyond Sabzevar, Nishapur and Tus (3 of 5 budget pages used) (try https://www.iranicaonline.org/articles/sarbedarids)

Spot checks:
- `/ledger/1` on https://en.wikipedia.org/wiki/Sarbadars: confirmed ('in the summer of 1337 took possession of Sabzavar')
- `/ledger/2` on https://en.wikipedia.org/wiki/Sarbadars: confirmed (1340, Arghun Shah 'forced to abandon Nishapur and retreat to Tus')
- `/ledger/3` on https://en.wikipedia.org/wiki/Sarbadars: confirmed (Jajarm, Damghan, Simnan, Gurgan)
- `/ledger/4` on https://en.wikipedia.org/wiki/Sarbadars: confirmed (1344 campaign 'ended in disaster', Mas'ud executed, most conquests lost)
- `/ledger/5` on https://en.wikipedia.org/wiki/Sarbadars: confirmed (Ray area, Tus, Astarabad, Shasman after late 1353)
- `/ledger/7` on https://en.wikipedia.org/wiki/Sarbadars: confirmed (Astarabad 1365/6-1368/9)

## ramadanid-emirate: thin

Area: infobox 15000 km2 (year None), Cliopatria 24029 km2, ratio 1.6, acknowledged True. 

Thin (for a gap-filler):
- `/ledger/1`: Year the Mamluks authorised the emirate to administer Cilicia (c1 at 1375; mamluk-sultanate puts the protectorate at c. 1385, the infobox at 1352) (try https://en.wikipedia.org/wiki/Mamluk_Sultanate)
- `/keyframe_review/3-5`: Dates of the battle of Belen, the Karaman alliance, Yilboga's capture of Misis and Ali Bey's capture of Tarsus (all undated on the page); shapes 1402-1512 'unverified: page budget' (thin by design, 5 shapes) (try https://en.wikipedia.org/wiki/Karamanids)

Spot checks:
- `/ledger/0` on https://en.wikipedia.org/wiki/Ramadanid_Emirate: confirmed (1352 settlement at Camili, Cairo visit 'later that year'; Established 1352)
- `/ledger/1` on https://en.wikipedia.org/wiki/Ramadanid_Emirate: confirmed as undated: 'In 1375, the Mamluks gained control of the remaining areas of Cilicia'; authorisation year not on page (c1 honest)
- `/ledger/2` on https://en.wikipedia.org/wiki/Ramadanid_Emirate: confirmed ('Selim I incorporated the beylik', 1516; Ottoman protectorate 1517-1608)
- `/ledger/3` on https://en.wikipedia.org/wiki/Ramadanid_Emirate: confirmed (as /ledger/2)

## hashemite-arab-federation: pass

Area: infobox 533314 km2 (year 1958), Cliopatria None km2, ratio 0.96, acknowledged True. No Cliopatria shape is alive in 1958 (the row's shapes are 1415-1439, 223,626 km2, marked wrong); the new 1958 keyframe (Iraq+Jordan+West Bank, about 511,000 km2) against the infobox gives 0.96.

Spot checks:
- `/ledger/0` on https://en.wikipedia.org/wiki/Arab_Federation: confirmed (14 February 1958, 'as a response to the formation of the United Arab Republic'; capital Baghdad)
- `/ledger/1` on https://en.wikipedia.org/wiki/Arab_Federation: confirmed (Faisal II 'deposed by a military coup on 14 July')
- `/ledger/2` on https://en.wikipedia.org/wiki/Arab_Federation: confirmed ('the new Iraqi government officially dissolved the Federation on 2 August 1958')
- `/keyframe_review/2` on https://en.wikipedia.org/wiki/Arab_Federation: confirmed (area 533,314 km2; confederal: 'united foreign policy and defense' only)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| qara-qoyunlu 1384 vassal_start (Artuqids of Mardin) | - | exception | Listed in counterparts_needing_dossiers (me-09-x); vassal_end 1409 likewise. |
| qara-qoyunlu 1400 loss (timurid-empire) | - | missing | timurid-empire (ia-02, written) has no 1400 gain from qara-qoyunlu (Timur's defeat of the Qara Qoyunlu, Qara Qoyunlu page). |
| qara-qoyunlu 1406 gain (timurid-empire) | timurid-empire 1406 loss | mismatch | Years match; land does not: timurid-empire /ledger/22 loses Iranian Azerbaijan, Armenia and Azerbaijan (c3), qara-qoyunlu gains only Van (c1). See qara-qoyunlu fixes. |
| jalayirid-sultanate 1406 gain (qara-qoyunlu) | - | missing | Ahmad takes Tabriz from Qara Yusuf in 1406; qara-qoyunlu never holds Tabriz in 1406 (contest with timurid-empire instead), so no loss mirror. |
| qara-qoyunlu 1409 gain (timurid-empire) | - | missing | Sultaniyya/Zanjan (now c1); no loss in timurid-empire. |
| qara-qoyunlu 1410 gain (jalayirid-sultanate) | jalayirid-sultanate 1410 loss | matched | Baghdad (jalayirid /ledger/19) and Tabriz/Azerbaijan (jalayirid /ledger/18). |
| qara-qoyunlu 1410 gain (nobody) | timurid-empire 1406 loss | mismatch | Armenia from 'nobody' while timurid-empire loses Armenia to qara-qoyunlu in 1406. |
| qara-qoyunlu 1432 gain (jalayirid-sultanate) | jalayirid-sultanate 1431 loss | matched | Hillah October 1431 / 1432; land now drawn by the reviewer-added keyframe qara-qoyunlu_1432. |
| qara-qoyunlu 1446 gain (Ispend's line at Baghdad (Qara Qoyunlu appanage)) | - | exception | Not a separate state; counterpart corrected from 'unnamed holder' by the reviewer. |
| qara-qoyunlu 1447 gain (timurid-empire) | timurid-empire 1447 loss | matched | Also timurid vassal_start 1435 / vassal_end 1447 of qara-qoyunlu, consistent with the Qara Qoyunlu and Jahan Shah pages (suzerain-side events). |
| qara-qoyunlu 1453 gain (timurid-empire) | timurid-empire 1453 loss | matched | Central Iran and (c1) Kerman. |
| qara-qoyunlu 1458 occupation_start (timurid-empire) | timurid-empire 1458 loss | mismatch | Herat: qara-qoyunlu records an occupation (six months, Jahan Shah page); timurid-empire records loss + gain. The owner should record occupation_start/_end (ia-02). |
| qara-qoyunlu 1464 gain (Pir Budaq (rebel governor of Baghdad)) | - | exception | Rebel governor; start of revolt undated; no dossier. |
| qara-qoyunlu 1468 loss (aq-qoyunlu) | aq-qoyunlu 1468 gain | matched | Year matches; the central-Iranian part is the aq-qoyunlu 1475 mismatch below. |
| aq-qoyunlu 1475 gain (qara-qoyunlu) | - | mismatch | Counterpart dissolved in 1468; blocking finding in aq-qoyunlu. |
| aq-qoyunlu 1402 gain (timurid-empire) | - | missing | Timur's grant of Diyar Bakr: timurid-empire has neither a loss nor a vassal_start aq-qoyunlu in 1402 (ia-02). |
| aq-qoyunlu 1415 gain (mamluk-sultanate) | - | missing | c1 guess from Cliopatria; no mirror in mamluk-sultanate. |
| aq-qoyunlu 1465 gain (beylik-of-dulkadir) | - | missing | Harput: beylik-of-dulkadir (me-09-g) has no 1465 loss; the Uzun Hasan page confirms the capture. |
| aq-qoyunlu 1470 occupation_start (timurid-empire) | - | missing | Herat July 1470: no occupation in timurid-empire (ia-02). |
| aq-qoyunlu 1475 vassal_start (Kingdom of Hormuz) | - | exception | Listed in counterparts_needing_dossiers; c1. |
| aq-qoyunlu 1501 loss (safavid-dynasty) | - | exception | safavid-dynasty owned by me-10, not run yet (also 1503, 1507, 1508). |
| mamluk-sultanate 1433 vassal_start (aq-qoyunlu) | - | exception | Suzerain-side event (schema); the Aq Qoyunlu page neither confirms nor denies it (calls Qaitbay a 'loyal peer' in 1469). aq-qoyunlu notes mention it; vassal_end 1472 likewise. |
| empire-of-trebizond 1355 loss (aq-qoyunlu) | - | mismatch | 1355 is before aq-qoyunlu's start (1378); the Aq Qoyunlu page dates the Turkmen raids on Trebizond to 1340 and 1348. eu-05 should use 'nobody' or a pre-state Turkmen label, or the event stays c1 without a dossier counterpart. |
| muzaffarids 1319 gain (atabegs-of-yazd) | - | exception | Listed in counterparts_needing_dossiers. |
| muzaffarids 1340 gain (ilkhanate) | - | missing | Kerman from the Mongol governor Qutb al-Din b. Nasir: ilkhanate (ia-02, written, ends 1343) has no 1340 loss. |
| muzaffarids 1357 gain (injuids) | injuids 1357 loss | matched | Fars and Isfahan (injuids /ledger/3-4). |
| muzaffarids 1387 loss (timurid-empire) | timurid-empire 1387 gain | matched | Isfahan; keyframe added by the reviewer. |
| muzaffarids 1393 loss (timurid-empire) | timurid-empire 1393 gain | matched | Fars, Kerman. |
| sarbadars 1337 gain (ilkhanate) | - | missing | Sabzevar: no 1337 loss in ilkhanate (ia-02). |
| sarbadars 1340 gain (Togha Temur's khanate (Astarabad, Mazandaran, Gurgan)) | - | exception | Listed in counterparts_needing_dossiers (also 1344 loss, 1353 gain; Ja'un-i Qurban 1340; Amir Vali 1354, 1366, 1369). |
| sarbadars 1376 loss (kartids) | kartids 1376 gain | matched | Nishapur. |
| sarbadars 1386 dissolve () | - | missing | Submission to Timur 1381 and the end in 1386: timurid-empire has no vassal_start sarbadars 1381 and no gain of Sabzevar (ia-02). |
| ramadanid-emirate 1375 gain (mamluk-sultanate) | mamluk-sultanate 1385 vassal_start | mismatch | Mamluk side models the plain as a protectorate from c. 1385 (c1); Ramadanid page infobox has the Mamluk protectorate 1352-c. 1397 and the 1375 Mamluk conquest; route to the mamluk-sultanate owner (me-09). |
| ramadanid-emirate 1516 loss (ottoman-empire) | ottoman-empire 1515 gain | matched | Within one year; the Ramadanid page says 1516 (author flagged). |
| hashemite-arab-federation 1958 loss (iraqi-republic) | - | exception | iraqi-republic owned by me-10, not run yet; the land change is kingdom-of-iraq's dissolve (1958/7, successor iraqi-republic), so iraqi-republic needs no gain from this umbrella. |

## Other notes

- No page failed to load; 12 Wikipedia pages opened with WebFetch.
- Reviewer applied fixes in qara-qoyunlu (new keyframe qara-qoyunlu_1432, /ledger/8 confidence 1, /ledger/20 counterpart) and muzaffarids (new keyframe muzaffarids_1387); both re-validate with 0 errors and were read back after writing.
- aq-qoyunlu fails on one blocking finding (central Iran gained 'from qara-qoyunlu' in 1475, seven years after qara-qoyunlu dissolved, leaving 1468-1474 blank); the matching qara-qoyunlu /ledger/29 region change is listed as a non-blocking fix there.
- hashemite-arab-federation is type umbrella; reviewer brief rule 9 says umbrella is never a dossier of its own, but the schema defines umbrella as an association and the Cliopatria row needs a file; accepted as other reviewers accepted league-of-corinth.
- Routing for other groups: ia-02 (timurid-empire: 1400 gain, 1402 Diyar Bakr, 1406 land, 1409, 1458 and 1470 Herat as occupations, Sarbadar vassalage 1381-1386; ilkhanate: 1337 Sabzevar and 1340 Kerman losses); me-09 (mamluk-sultanate Ramadanid protectorate year; beylik-of-dulkadir 1465 Harput); eu-05 (empire-of-trebizond 1355 counterpart predates aq-qoyunlu); me-10 (iraqi-republic, safavid-dynasty not yet written).
- Hashemite Arab Federation: the replacement regions for the wrong 1415-1439 shapes (Hillah r60, Wasit, Basra) are smaller than the shape; Dhi Qar, Maysan and Qadisiyyah stay undrawn in 1415-1439 unless the jalayirid-sultanate and qara-qoyunlu lower-Iraq regions are widened (the Jalayirid page names only Hillah, Wasit and Basra). Not a fault of this dossier.
- Gazetteer names wanted (text only in the dossiers): Meybod, Shasman, Erciş, Harput, Yüreğir, Persian Iraq.
