# Review of batch ia-02-d

Reviewer run 2026-10-19 (adversarial reviewer, Phase B). Dossiers: crimean-khanate, nogai-horde, qasim-khanate, east-turkestan, moghulistan. The validator (--resolve) gives 0 errors and 0 warnings for all five, before and after the reviewer's edits.

Verdicts: crimean-khanate **fix**, nogai-horde **fail**, qasim-khanate **pass**, east-turkestan **fix**, moghulistan **thin**.

Reviewer edits were applied in place under the orchestrator's small-fix rule; they are marked applied below. Unapplied findings go back to the author.

## crimean-khanate: fix

Findings:
- `/ledger/1` (applied by reviewer): The 1449 move to Qirq Yer was at confidence 3, and its note quoted words that are not on the page ('moved the capital to Qırq Yer in 1449'). Evidence: Crimean Khanate page: Hacı Giray had to fight rivals 'before he could ascend the throne of the khanate in 1449' ... 'after which he moved its capital to Qırq Yer (today part of Bahçeseray)'. The page dates the accession, not the move. Fix: Confidence lowered to 2 and the quote replaced with the page's words; the same quote in /identity/capitals/1/note corrected. Re-validated: 0 errors, 0 warnings.

Gaps (thin, for a gap-filler):
- `/ledger/3`: 1572 loss of the Azov-Kuban strip (confidence 1, Cliopatria's step); see the nogai-horde finding on the 1557-1571 double claim Try: https://en.wikipedia.org/wiki/Nogais
- `/ledger/4`: 1595 loss of the northern steppe to nobody (confidence 1); no page dates it Try: https://en.wikipedia.org/wiki/Don_Cossacks
- `/ledger/6`: 1737 end of the Russian campaigns in Crimea (confidence 1); withdrawal date Try: https://en.wikipedia.org/wiki/Peter_Lacy
- `/ledger/7`: 1738 gain of the Kuban strip (confidence 1, Cliopatria's step) Try: https://en.wikipedia.org/wiki/Treaty_of_Ni%C5%A1_(1739)
- `/ledger/9`: November 1772 end of the first Russian occupation (confidence 1; the page says troops stayed at Yeni-Kale and Kerch) Try: https://en.wikipedia.org/wiki/Russo-Turkish_War_(1768%E2%80%931774)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Hac%C4%B1_I_Giray: confirmed: 'In March 1441, Genoese sources name him as the new khan'; '1441 is often taken as the official start of his reign and the foundation of the Crimean Khanate'; 'Vasary says that the traditionally accepted date is August 1449'
- `/ledger/1` https://en.wikipedia.org/wiki/Crimean_Khanate: mis-dated at confidence 3: the page dates the accession (1449), and the move only follows it ('after which he moved its capital to Qırq Yer'). Lowered to 2 (applied)
- `/ledger/2` https://en.wikipedia.org/wiki/Crimean_Khanate: confirmed: 'Later, the capital was moved a short distance to Bahçeseray, founded in 1532 by Sahib I Giray' (confidence 2 is right)
- `/ledger/8` https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Empire: confirmed: 'In July 1771, the Russian army marched into Kaffa'
- `/ledger/10` https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Empire: confirmed: the November 1772 treaty proclaimed an independent state 'including the former Kaffa Eyalet'; the page adds it 'could not come into effect without Ottoman recognition', which came in 1774 (the note already gives the 1774 alternative)
- `/ledger/11` https://en.wikipedia.org/wiki/Treaty_of_K%C3%BC%C3%A7%C3%BCk_Kaynarca: confirmed: signed '21 July [O.S. 10 July] 1774'; Article XIX gives Jenicale and Kertsch 'full, perpetual, and incontestable' Russian dominion
- `/ledger/12` https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Empire: confirmed: 'Catherine gave an order to invade Crimea in November 1776'; 'Her forces quickly gained control of Perekop'
- `/ledger/14` https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Empire: confirmed: 'Catherine issued a formal proclamation of annexation on 19 April [O.S. 8 April] 1783'

Area: The infobox gives no area (checked on the page). The Cliopatria peak is 1450 (222,809 km2), corrected to the 135,385 km2 1468 shape. The author says no area could be compared. Cliopatria peak 222,809 km2.

## nogai-horde: fail

Findings:
- `/ledger/4` (NOT applied: author to do): The 1557 gain of the Kuban and Azov steppe has counterpart 'nobody' and is drawn from 1557 (new keyframe /keyframe_review/7). But about 51,000 km2 of that strip is inside Cliopatria's Crimean Khanate shapes up to 1571, and the crimean-khanate dossier keeps the strip until its 1572 loss to nogai-horde (crimean-khanate /ledger/3). This ledger has no mirror gain for that loss, so both states draw the strip from 1557 to 1571. Evidence: shapes.csv: crimean-khanate_1468..1552 reach east to 42.48E (bbox 31.82-42.48E, 44.65-49.18N); small-horde_1564 starts at 36.75E. The author's own notes give '51,000 km2 of it overlapping the Crimean shape in 1564-1571', and /keyframe_review/7 carries the Small Horde 1564 shape back to 1557. The Crimean Khanate page: 'The Nogay pastoral nomads north of the Black Sea were nominally subject to the Crimean Khan'. Fix: Pick one owner for 1557-1571 and make the two ledgers mirror each other. Either (a) Crimean until 1571: set the 1557 gain's region to {'minus':[{'cliopatria':'Small Horde','year':1564},{'cliopatria':'Nogai Horde','year':1563},{'cliopatria':'Crimean Khanate','year':1552}]}, add an adjust to small-horde_1564 that removes the Crimean Khanate 1552 shape for 1564-1571, and add a 1572 gain from crimean-khanate (region: the crimean-khanate /ledger/3 region intersected with Small Horde 1572, confidence 1); or (b) Nogai from 1557: split the 1557 gain into the part from nobody and the part from crimean-khanate, and ask for crimean-khanate's loss to move to 1557 with crimean-khanate_1552 split at 1557.
- `/identity` (NOT applied: author to do): Not blocking. The merge of the Lesser Nogai Horde into the Nogai Horde goes against the page, which treats them as two states; only Cliopatria's Small Horde row supports the merge. Evidence: Nogai Horde infobox: 'Successors: Lesser Nogai Horde; Kalmyk Khanate', 'Conquered by the Kalmyk Khanate: 1634'. The body says Qazi Mirza 'founded the Lesser Nogai Horde on the steppe of the North Caucasus'. /ledger/5 (the 1564 rename) is confidence 1. Fix: Say in /notes that the merge follows Cliopatria's Small Horde row, which draws both hordes as one shape from 1564, and that the page has the Lesser Horde as a successor. Make sure the ia-03-c owner of small-horde does not write a second dossier.

Gaps (thin, for a gap-filler):
- `/ledger/0`: 1450 start is Cliopatria's (confidence 1); the infobox gives 'Established: 1480' and the lead 'about 1500' Try: https://en.wikipedia.org/wiki/Nogais
- `/ledger/8`: 1572 loss to the Kazakhs (confidence 1); the pages give the Emba battle as 1570 (Haqnazar page) or 1568 (Kazakh Khanate page) Try: https://en.wikipedia.org/wiki/Nogais
- `/ledger/9`: 1588 losses of the Middle Volga steppe to Russia and to nobody (confidence 1) Try: https://en.wikipedia.org/wiki/Nogais
- `/ledger/13`: 1636 loss to the Kalmyks (confidence 1); the pages say 1634 Try: https://en.wikipedia.org/wiki/Kalmyk_Khanate
- `/ledger/14`: 1737 end of the Kuban Nogai row (confidence 1) Try: https://en.wikipedia.org/wiki/Nogais

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Kazakh_Khanate: confirmed: 'Kasym successfully captured the Nogai capital Saray-Juk in 1520, pushing the Nogai Horde to the Astrakhan Khanate'
- `/ledger/3` https://en.wikipedia.org/wiki/Nogai_Horde: confirmed: '1521 Nogais, driven west by the Kazakhs, cross the Volga and attack Astrakhan.'
- `/ledger/4` https://en.wikipedia.org/wiki/Nogai_Horde: confirmed: '1557 Mirza Kazy crosses the Volga and founds Small Horde along the Kuban'; the body has him found 'the Lesser Nogai Horde'
- `/ledger/6` https://en.wikipedia.org/wiki/Haqnazar_Khan: confirmed: 'In 1570, Haqnazar defeated the Nogai Horde at the Battle of Emba'. The Kazakh Khanate page dates the Emba victory to 1568, so the note could give both years
- `/ledger/11` https://en.wikipedia.org/wiki/Nogai_Horde: confirmed: 'The first group was broken up circa 1632 by the Kalmyks'; '1634 major defeat of Nogais by Kalmyks'

Area: The infobox gives no area, only a map 'at the end of the 15th century' (checked on the page). Cliopatria peak 704,705 km2.

## qasim-khanate: pass

Tried: Years against the infobox; the 1552-1681 new keyframe against the page; the capital Kasimov (41.39E, 54.94N) inside the bbox; the Moscow vassal tint routed to eu-16. Found nothing to break.

Gaps (thin, for a gap-filler):
- `/ledger/1`: 1502 gain of a 1,264 km2 sliver (confidence 1; the page is silent) Try: https://en.wikipedia.org/wiki/Kasimov

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Qasim_Khanate: confirmed: infobox 'Established 1452'; 'The khanate was established in the lands which Grand Prince Vasily II of Moscow (r. 1425-1462) presented in 1452'; also 'dated to no later than 1456'
- `/ledger/2` https://en.wikipedia.org/wiki/Qasim_Khanate: confirmed: 'After the death of khanbika (queen) Fatima Soltan in 1681, the Khanate was abolished'; infobox 'Disestablished 1681', 'Succeeded by: Tsardom of Russia'

Area: The infobox gives no area. The infobox gives 'Preceded by: Golden Horde', while the dossier names Moscow, the grantor, from the body text (see cross_checks). Cliopatria peak 24,701 km2.

## east-turkestan: fix

Findings:
- `/ledger/0/note` (applied by reviewer): The quote is not the page's wording: 'consolidated control of the settled lands of Eastern Moghulistan (Uyghurstan) and resided at Aksu'. Evidence: Yunus Khan page: 'Dost Mohammad however consolidated his hold on all settled lands in Eastern Moghulistan, known at the time as Uyghurstan'; 'He became the ruler of that region and took up residence in the town of Aksu'. Fix: Quote replaced with the page's words, and the same quote in /identity/capitals/0/note corrected. Re-validated.
- `/ledger/1/note` (applied by reviewer): The quote is not the page's wording: 'Dost Muhammad died in 1469. Afterward, Yunus Khan reunited the khanate'. Evidence: Moghulistan page: 'After the death of Dost Muhammad in 1469, Yunus Khan reunited the khanate.' Fix: All three occurrences in the file replaced with the page's sentence. Re-validated.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Esen_Buqa_II: confirmed: 'Esen Buqa died of natural causes in 1462, after a khanship of thirty-three years'; 'in the west Yunus Khan gained power, while in the east Esen Buqa's son Dost Muhammad became khan'
- `/ledger/1` https://en.wikipedia.org/wiki/Moghulistan: confirmed: 'After the death of Dost Muhammad in 1469, Yunus Khan reunited the khanate'; the Yunus Khan page has 'in 1468 or 1469'

Area: East_Turkestan is a region article ('a loosely defined geographical region in the northwestern part of the People's Republic of China') with no infobox area and nothing on the 1460s, as the author says. Cliopatria peak 1,080,074 km2.

## moghulistan: thin

Findings:
- `/ledger/1/note` (applied by reviewer): The quote is not the page's wording: 'Dost Muhammad died in 1469. Afterward, Yunus Khan reunited the khanate'. Evidence: Moghulistan page: 'After the death of Dost Muhammad in 1469, Yunus Khan reunited the khanate.' Fix: All three occurrences in the file replaced with the page's sentence (/ledger/1, /keyframe_review/1, /keyframe_review/2). Re-validated.
- `/ledger/2/note` (applied by reviewer): The quote is not the page's wording: 'let him take Tashkent'. Evidence: Yunus Khan page: 'In 1484, Yunus Khan took advantage of one of the periodic conflicts' between Sultan Ahmad and Umar Shaikh Mirza II 'to take possession of Tashkent'. Fix: Replaced with 'to take possession of Tashkent' here and in /keyframe_review/4/note. Re-validated.

Gaps (thin, for a gap-filler):
- `/keyframe_review/1`: No ledger event explains the 1468 step. moghulistan_1463 (464,954 km2, west edge 70.11E) shrinks to moghulistan_1468 (302,142 km2, west edge 71.39E), a loss of 162,800 km2. Cliopatria's Kazakh Khanate row begins the same year with a 161,350 km2 shape whose bbox (70.11-76.61E, 41.65-46.41N) starts at the same 70.11E edge, so this is the land Moghulistan drops. Needed: a 1468 loss to kazakh-khanate with region {'minus':[{'cliopatria':'Moghulistan','year':1463},{'cliopatria':'Moghulistan','year':1468}]}, confidence 1 or 2. The pages already opened support it: the Esen Buqa II page has him give refuge to 'two brothers, Jani Beg and Kerei'; the Yunus Khan page has Yunus on good terms with 'Janybek Khan and Karai Khan, the founders of the Kazakh Horde' (1465-1466); the Moghulistan infobox lists the Kazakh Khanate as a successor. Try: https://en.wikipedia.org/wiki/Kazakh_Khanate
- `/ledger/3`: 1492 split of the Zhetysu into the Eastern Chagatai Khanate row (confidence 1, Cliopatria's year; the pages date the division to 1487) Try: https://en.wikipedia.org/wiki/Sultan_Mahmud_Khan
- `/ledger/4`: 1512 re-absorption of the Zhetysu (confidence 1). The Moghulistan page has the Kyrgyz 'effectively driven out the Moghuls' by 1510-11, against the shape Try: https://en.wikipedia.org/wiki/Sultan_Said_Khan
- `/ledger/6`: 1518 end (confidence 1, Cliopatria's year) Try: https://en.wikipedia.org/wiki/Yarkent_Khanate

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Esen_Buqa_II: confirmed: died 1462; 'in the west Yunus Khan gained power'
- `/ledger/1` https://en.wikipedia.org/wiki/Moghulistan: confirmed: reunion after Dost Muhammad's death in 1469; 1470 is a bridging year at confidence 2
- `/ledger/2` https://en.wikipedia.org/wiki/Yunus_Khan: confirmed: 'In 1484, Yunus Khan took advantage of one of the periodic conflicts' ... 'to take possession of Tashkent'. The Moghulistan page also says 'took Tashkent in 1482', and the note gives both
- `/ledger/5` https://en.wikipedia.org/wiki/Moghulistan: confirmed: Said Khan 'conquered the western Tarim Basin from Mirza Abu Bakr Dughlat in 1514'; 'Thereafter the Moghulistan khanate was permanently divided'

Area: The infobox gives no area (checked); its dates are 'Formation 1347' and 'split into two parts: 1462'. Cliopatria peak 1,383,470 km2.

## Cross-dossier matrix

- crimean-khanate 1441 found (golden-horde) -> golden-horde 1449 loss: **mismatch**. golden-horde /ledger/24 (confidence 3) has Crimea leave the Horde in August 1449, while crimean-khanate starts in March 1441 (Hacı I Giray page: '1441 is often taken as the official start'), so Crimea is drawn by both states in 1441-1449. Route to golden-horde: move its loss to 1441 (confidence 2), or say in notes why it keeps 1449. The crimean-khanate author flagged this.
- crimean-khanate 1572 loss (nogai-horde) -> nogai-horde 1557 gain (from nobody): **mismatch**. nogai-horde has no 1572 gain from crimean-khanate. It takes the same Kuban/Azov strip in 1557 from 'nobody', so about 51,000 km2 is drawn by both states in 1557-1571. The fix is assigned to nogai-horde (blocking).
- crimean-khanate 1595 loss (nobody) -> none: **exception**. Counterpart nobody.
- crimean-khanate 1738 gain (nogai-horde) -> nogai-horde 1737 dissolve: **matched**. nogai-horde dissolves in 1737 with crimean-khanate as successor (Small Horde 1737 land).
- crimean-khanate 1771 occupation_start (russian-empire) -> none: **exception**. russian-empire (eu-17) has not run; the author's problems list asks for the occupations of 1771-1772 and 1776-1783.
- crimean-khanate 1772 gain (ottoman-empire) -> none: **exception**. ottoman-empire (me-10) has not run; it should carry the 1772 (or 1774) loss of the Kefe coast and the vassal pair for 1475-1774, counterpart crimean-khanate.
- crimean-khanate 1774 loss (russian-empire) -> none: **exception**. russian-empire (eu-17) has not run; it should carry the 1774 gain of Kerch and Yenikale.
- crimean-khanate 1776 occupation_start (russian-empire) -> none: **exception**. russian-empire (eu-17) has not run.
- crimean-khanate 1783 dissolve (russian-empire) -> none: **exception**. russian-empire (eu-17) has not run; it should carry the 1783 gain.
- golden-horde 1502 dissolve (crimean-khanate) -> crimean-khanate None None: **mismatch**. golden-horde /ledger/31 names crimean-khanate as the counterpart of its 1502 dissolution, but Cliopatria's Crimean shape does not grow in 1502 and the Great Horde page names no land that passed to Crimea, so crimean-khanate rightly has no gain. Route to golden-horde: its successor land in 1502 is not Crimean.
- nogai-horde 1450 found (golden-horde) -> golden-horde 1450 loss: **matched**. golden-horde /ledger/25 (confidence 1).
- nogai-horde 1521 loss (kazakh-khanate) -> none: **exception**. kazakh-khanate (ia-03) has not run.
- nogai-horde 1557 gain (nobody) -> crimean-khanate 1572 loss: **mismatch**. Part of the 1557 gain is inside the Crimean shape until 1572; see above.
- nogai-horde 1572 loss (kazakh-khanate) -> none: **exception**. kazakh-khanate (ia-03) has not run.
- nogai-horde 1588 loss (tsardom-of-russia) -> none: **exception**. tsardom-of-russia (eu-16) has not run.
- nogai-horde 1588 loss (nobody) -> none: **exception**. Counterpart nobody.
- nogai-horde 1636 loss (kalmyk-khanate) -> none: **exception**. kalmyk-khanate (ia-03) has not run.
- nogai-horde 1737 dissolve (crimean-khanate) -> crimean-khanate 1738 gain: **matched**. 
- qasim-khanate 1452 found (grand-principality-of-moscow) -> golden-horde 1453 loss: **mismatch**. golden-horde /ledger/26 (confidence 1) loses land to qasim-khanate in 1453, while qasim-khanate names Moscow, the grantor, as the land's source (page text: lands 'which Grand Prince Vasily II of Moscow ... presented in 1452'; infobox 'Preceded by: Golden Horde'). One year apart, but the counterparts disagree. grand-principality-of-moscow (eu-16) has not run. Not blocking: the authors of golden-horde and eu-16 should agree whose land the 1453 shape takes.
- qasim-khanate 1502 gain (golden-horde) -> golden-horde 1502 dissolve (counterpart crimean-khanate): **missing**. golden-horde has no 1502 loss to qasim-khanate, and its successors leave out qasim-khanate. The 1,264 km2 sliver is confidence 1. Route to golden-horde.
- qasim-khanate 1681 dissolve (tsardom-of-russia) -> none: **exception**. tsardom-of-russia (eu-16) has not run; it should also carry the vassal tint for 1452/1552-1681, counterpart qasim-khanate.
- east-turkestan 1463 found (chagatai-khanate) -> chagatai-khanate 1462 dissolve: **mismatch**. chagatai-khanate /ledger/16 dissolves into moghulistan only, and its successors list only moghulistan. It should also name east-turkestan (land: East Turkestan 1463). Minor; route to the chagatai-khanate author.
- east-turkestan 1469 dissolve (moghulistan) -> moghulistan 1470 gain: **matched**. 
- moghulistan 1463 found (chagatai-khanate) -> chagatai-khanate 1462 dissolve: **matched**. 
- moghulistan 1468 loss (missing) (kazakh-khanate) -> none: **missing**. Not in the ledger: Cliopatria's 1468 step hands 162,800 km2 to the Kazakh Khanate row, which starts in 1468. kazakh-khanate (ia-03) has not run. Listed under thin.
- moghulistan 1470 gain (east-turkestan) -> east-turkestan 1469 dissolve: **matched**. 
- moghulistan 1484 gain (timurid-empire) -> timurid-empire None None: **missing**. timurid-empire has no 1484 loss of Tashkent; its only Tashkent event is in 1405. Route to the timurid-empire author: 1484 loss of Tashkent to moghulistan (Yunus Khan page).
- moghulistan 1492 loss (eastern-chagatai-khanate) -> none: **exception**. eastern-chagatai-khanate (another ia-02 part) is not written yet.
- moghulistan 1512 gain (eastern-chagatai-khanate) -> none: **exception**. eastern-chagatai-khanate is not written yet.
- moghulistan 1514 loss (eastern-moghulistan) -> none: **exception**. No eastern-moghulistan dossier yet. Its Cliopatria row begins in 1519, so the dossier has to start in 1514 to receive this land (the author flagged this).
- moghulistan 1518 dissolve (western-moghulistan) -> none: **exception**. No western-moghulistan dossier yet.

## For the orchestrator

- Reviewer edits (authorised by the orchestrator as small fixes verified on the page): crimean-khanate /ledger/1 confidence 3 to 2 and quote corrected, plus /identity/capitals/1/note; east-turkestan quotes corrected (/ledger/0, /ledger/1, /identity/capitals/0, keyframe notes); moghulistan quotes corrected (/ledger/1, /ledger/2, keyframe notes). All three re-validate with 0 errors and 0 warnings. Backups are in /tmp/claude-0/work/ia-02-d-rev/bak/.
- Blocking item for nogai-horde: the Kuban/Azov strip is drawn by both nogai-horde (from 1557) and crimean-khanate (to 1571). Whichever option the author picks, both ledgers must mirror each other.
- golden-horde (another ia-02 part, already written) dates the Crimean secession to August 1449, while crimean-khanate founds in March 1441: Crimea is double-drawn in 1441-1449. golden-horde also names crimean-khanate as the counterpart of its 1502 dissolution with no matching land, and has no 1502 loss to qasim-khanate.
- timurid-empire lacks the 1484 loss of Tashkent to moghulistan; chagatai-khanate's successors lack east-turkestan.
- small-horde is merged into nogai-horde here; ia-03-c also lists small-horde. The orchestrator should make sure only one dossier exists.
- eastern-moghulistan should start in 1514 (not 1519) to receive the Tarim Basin from moghulistan.
- No page failed to load. Neighbour dossiers read: golden-horde, khanate-of-kazan, khanate-of-sibir, timurid-empire, four-oirats (plus chagatai-khanate as the predecessor). The other 23 context polities have no dossier yet (groups not run). khanate-of-kazan, khanate-of-sibir and four-oirats have no territorial events with this batch, and none was expected from the pages read.

Gazetteer names needed: Perekop (place, crimean-khanate), Staryi Krym (place, crimean-khanate), Saraichik (place, nogai-horde), Yedisan (region, crimean-khanate), Moghulistan (region, moghulistan).
Counterparts needing dossiers: Turpan Khanate (turpan-khanate), Dughlat emirate of Kashgar, Yarkand and Khotan (dughlat-emirate).
