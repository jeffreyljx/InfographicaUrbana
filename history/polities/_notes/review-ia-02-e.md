# Review of batch ia-02-e (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: astrakhan-khanate (pass), mongol-khanate (thin), kapisa (fail), eastern-chagatai-khanate (fix, fixed by the reviewer). Validator with --resolve: 0 errors in all four; one warning (mongol-khanate /ledger/9 counterpart 'khalkha' has no dossier, listed by the author). Neighbour dossiers read: golden-horde, crimean-khanate, nogai-horde, moghulistan, timurid-empire, four-oirats, east-turkestan, khanate-of-sibir, northern-yuan. Not written yet (exception): ming-dynasty, kalmyk-khanate, ottoman-empire, zaporozhian-cossacks, kazakh-khanate, sloboda-ukraine, small-horde, tumed, tsardom-of-russia, tibet, russian-empire, eastern-moghulistan, western-moghulistan, shaybanids, later-jin-dynasty, don-cossacks.

## astrakhan-khanate: pass

Area: infobox none; Cliopatria max 162,622.2 km2. No area in the infobox (checked). The author compared the shape with Astrakhan Oblast plus Kalmykia (quoted as about 112,000 km2; the official figures are about 49,000 + 75,000 = 124,000 km2): ratio under 2 either way.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Astrakhan_Khanate: confirmed: 'The khanate is said to have been founded in 1466'; infobox Established 1466
- `/ledger/2` https://en.wikipedia.org/wiki/Astrakhan_Khanate: confirmed: 'It was twice briefly occupied by Crimea' (Mehmed I Giray in 1523)
- `/ledger/4` https://en.wikipedia.org/wiki/Astrakhan_Khanate: confirmed: Sahib I Giray in 1549
- `/ledger/6` https://en.wikipedia.org/wiki/Astrakhan_Khanate: confirmed: 'In 1554 he fled the town and Russia imposed its client Dervish Ali Astrakhani'
- `/ledger/8` https://en.wikipedia.org/wiki/Don_Cossacks: confirmed (conf 3): 'On 2 June 1556 the Cossack regiment of Ataman Lyapun Filimonov ... conquered and annexed the Astrakhan Khanate'; also /ledger/9

Gaps for a gap-filler:
- `/ledger/5`: 1549 occupation_end at confidence 1: the page says only 'twice briefly occupied by Crimea' (Sahib I Giray in 1549); no end date (try https://en.wikipedia.org/wiki/Sahib_I_Giray)

## mongol-khanate: thin

Area: infobox none; Cliopatria max 5,082,632.2 km2. Mongol khanate is a disambiguation page; the Northern Yuan infobox has no area (checked). The author compared the 1521 shape with the Dayan Khan page's verbal extent.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Northern_Yuan: confirmed: 'in 1455, a series of revolts resulted in Esen's death'
- `/ledger/2` https://en.wikipedia.org/wiki/Dayan_Khan: confirmed (year): 'By 1495, Batumongke won the Three Guards (Doyin Uriankhai, Ujiyed and Fuyu guard)'; the land is the author's reading, confidence 2 is honest
- `/ledger/8` https://en.wikipedia.org/wiki/Altan_Khan_of_the_Tumed: confirmed: Bodi Alagh 'died in 1547, Altan forced Bodi Alagh's successor Darayisung Küdeng Khan to flee eastward'
- `/ledger/11` https://en.wikipedia.org/wiki/Northern_Yuan: confirmed (conf 3): Ejei 'was said to give the Imperial Seal of the Mongols to Qing emperor Hong Taiji the next year (February 1635)'; also /ledger/13
- `/ledger/5` https://en.wikipedia.org/wiki/Dayan_Khan: confirmed: after the 1500 Ordos move the Ming 'counter attack ... the next year'; 'Dayan Khan relocated to the Kherlen River' (1501 by the page's sequence)

Gaps for a gap-filler:
- `/ledger/9`: 1547 loss of the Khalkha lands (about 2.8 M km2, the largest land move of the dossier) rests on Cliopatria only (confidence 1); no page dates the Khalkha separation. Note the golden-horde dossier (KF16-21) says the 1547-1632 'Golden Horde' shapes belong to the mongol-khanate (Northern Yuan line) to 1635, contrary to this event (try https://en.wikipedia.org/wiki/Khalkha_Mongols)
- `/ledger/1`: 1481 gain of the Oirat west at confidence 1 (follows the four-oirats dossier's 1480 end; no page opened here) (try https://en.wikipedia.org/wiki/Oirats)
- `/ledger/6`: 1519 gain of the 80-91 E, 42-45 N Tian Shan/Dzungaria strip from Moghulistan at confidence 1; no page mentions Mongol rule there (Northern Yuan page silent); the moghulistan dossier has no matching loss. If no page supports it, mark mongol-khanate_1519 and _1521 adjust minus that strip instead (try https://en.wikipedia.org/wiki/Turpan_Khanate)
- `/keyframe_review/1`: 1455-1546 shapes reach Qinghai and Gansu (627,000 km2 overlapping Cliopatria's Ming shape); no page puts them under the Great Khan before the Tumed moved into north-eastern Qinghai (Northern Yuan page, undated). unverified: page budget (try https://en.wikipedia.org/wiki/T%C3%BCmed)
- `/identity/capitals`: capitals only for 1500-1517; none for 1455-1499 or 1518-1635 (Ligdan's seat) (try https://en.wikipedia.org/wiki/Ligdan_Khan)

## kapisa: fail

Area: infobox none; Cliopatria max 116,849.0 km2. Kapisa is a disambiguation page; no infobox. Babur page has no area.

Findings:
- `/ledger/3` (NOT applied, author to do): The state is kept to 1506 and dissolved into timurid-empire then, but the timurid-empire dossier gains Kabul in October 1504 (its /ledger/45, confidence 3, same Babur page), so Kabul is drawn twice from October 1504 to 1506. Evidence: Babur page: 'In October 1504, Babur was able to cross the snowy Hindu Kush mountains and capture Kabul'; infobox 'Emir of Kabul: October 1504 - 21 April 1526'; nothing about Kabul in 1506. This dossier's own /ledger/2 note says 'the Timurid line restored'. The 1506 end is Cliopatria's (confidence 1). Fix: End the state in October 1504: identity.end {year 1504, month 10}; replace /ledger/2 and /ledger/3 by one dissolve (or merge) at 1504-10, counterpart timurid-empire, region {cliopatria Kapisa 1504}, confidence 3, source Babur page; kapisa_1502 verdict adjust, correction 'the shape unchanged, valid 1502 to October 1504'; capital, certainty and successor land to 1504.
- `/ledger/0` (NOT applied, author to do): The 1475 found event takes Kabul from timurid-empire, but the timurid-empire dossier records no 1475 loss and its corrections for timurid-empire_1475, _1487 and _1497 add admin1 Kabul (Ulugh Beg II's Kabul and Ghazni) to the Timurid Empire, so Kabul is double-claimed 1475-1500. Evidence: timurid-empire keyframe_review timurid-empire_1475 correction: union with {admin1 Kabul, Afghanistan}, text 'Kabul and Ghazni (Ulugh Beg II)'; its 1502 note: 'Kabul is still outside until October 1504'. Fix: Orchestrator decision, then the author: either fold kapisa into timurid-empire (Kabul is a Timurid appanage in that dossier; kapisa would then cover at most Abd ur-Razaq/Mukim Beg 1502-October 1504) or keep kapisa and have the timurid-empire owner drop admin1 Kabul from its 1475/1487/1497 corrections and add a 1475 (or 1469) loss to kapisa.

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Babur: confirmed (conf 3): 'In October 1504, Babur was able to cross the snowy Hindu Kush mountains and capture Kabul'
- `/ledger/1` https://en.wikipedia.org/wiki/Babur: confirmed: Ulugh Beg II 'died in 1502 leaving only an infant as heir'; 'The city was then claimed by Mukim Beg of Arghun dynasty' (undated)
- `/ledger/3` https://en.wikipedia.org/wiki/Babur: not on page: nothing for Kabul in 1506 (author says so, confidence 1); the page has Babur Emir of Kabul from October 1504
- `/identity` https://en.wikipedia.org/wiki/Kapisa: confirmed: disambiguation page; only 'the 1st millennium Kingdom of Kapisa', nothing for 1400-1520

Gaps for a gap-filler:
- `/ledger/0`: start 1475 is Cliopatria's (confidence 1); the Timurid partition that gave Ulugh Beg II Kabul is 1469 on the timurid-empire dossier's Abu Sa'id page (try https://en.wikipedia.org/wiki/Ulugh_Beg_II)
- `/ledger/1`: Mukim Beg's seizure of Kabul is undated (confidence 1) (try https://en.wikipedia.org/wiki/Arghun_dynasty)

## eastern-chagatai-khanate: fix

Area: infobox none; Cliopatria max 302,996.9 km2. No area in the Moghulistan infobox (checked).

Findings:
- `/wars/0/outcome` (applied by reviewer): Said 'Mahmud was executed in 1508 after submitting'; the page gives no year for the execution, only his reign 1487-1508. Evidence: Moghulistan page: 'he eventually gave up and submitted to Muhammad Shaybani, who executed him'; 'Mahmud Khan (1487-1508)'. Fix: Reworded: 'Mahmud later submitted to Shaybani, who executed him (the page ends his reign in 1508 and gives no year for the execution).'
- `/ledger/2/note` (applied by reviewer): Same claim in the dissolve note ('ended in 1508 when Shaybani executed him'). Evidence: As above. Fix: Reworded: 'Mahmud's reign ended in 1508 (page's reign dates); Shaybani executed him after he submitted, in a year the page does not give.' Re-validated: 0 errors, 0 warnings.

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Moghulistan: confirmed: 'In 1503 he traveled west to assist his brother Mahmud Khan'; 'The brothers were defeated and captured; they were released but Tashkent was seized by the Uzbeks'
- `/ledger/2` https://en.wikipedia.org/wiki/Moghulistan: confirmed: 'by 1510-11, they had effectively driven out the Moghuls'
- `/ledger/0` https://en.wikipedia.org/wiki/Moghulistan: mis-dated vs page (1487), but flagged by the author and entered at confidence 1 to agree with the moghulistan dossier: a gap, not a fault
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Moghulistan: confirmed: Mahmud Khan 'the ruler of western Moghulistan in Tashkent'

Gaps for a gap-filler:
- `/ledger/0`: start 1492 is Cliopatria's (confidence 1); the page dates the division to 1487 (Ahmad Alaq 1487-1503, Mahmud Khan 1487-1508). Move both this dossier and moghulistan's 1492 loss to 1487 if a page supports the 1487 split of land (try https://en.wikipedia.org/wiki/Yunus_Khan)
- `/keyframe_review/2`: who held the Zhetysu 1504-1511 and that the land went to the Kyrgyz in 1510-11 (Cliopatria returns it to Moghulistan in 1512) (try https://en.wikipedia.org/wiki/Sultan_Said_Khan)

## Other observations

- astrakhan-khanate: the 1554-56 Russian client regime is drawn as contest; the page says Russia 'imposed its client Dervish Ali Astrakhani', which reads as vassalage (vassal_start 1554 / vassal_end 1556, counterpart tsardom-of-russia). Not a fault; eu-16 should pick one reading. The 1551 'nominal submission to Moscow' is not entered (nominal).
- astrakhan-khanate 1642-1768 'wrong' keyframes: the correction gives the Don Cossacks 1640 outline with text 'not to the Astrakhan Khanate'. The golden-horde dossier's convention for mislabelled rows is the shape unchanged plus text naming the real owner; either works since the years lie outside the life 1466-1556, but a renderer must not draw them as Astrakhan.
- mongol-khanate: the keyframe/ledger walk holds (1468->1475 Oirat west via KF2/KF3 and the 1481 gain; 1482->1516 via the new 1495 keyframe and the 1495 gain; 1516->1519 via the 1519 gain; 1521->1547 via the two 1547 losses; 1547-1635 unchanged apart from a 4-cell sliver). Thin rather than fail: three confidence-1 events within a 5-page budget, all flagged by the author.
- kapisa: both blocking findings come from the same overlap with timurid-empire; the author flagged the overlap in general terms ('the timurid-empire dossier treats Kabul as Timurid (seat from 1507)') but missed that timurid-empire gains Kabul in October 1504.
- eastern-chagatai-khanate: matched both ways with moghulistan (1492 and 1511/1512). Kept as its own dossier although the author calls it part of one khanate with moghulistan: a merge decision for the orchestrator, consistent either way.

## Cross-dossier matrix

- astrakhan-khanate 1466 found -> golden-horde: mismatch (mirror: golden-horde 1468 loss). Two years apart: Astrakhan page 'said to have been founded in 1466' (infobox Established 1466); golden-horde /ledger/28 uses Cliopatria's 1468, so 1466-67 is drawn twice. Route to the golden-horde owner (ia-02): move the loss to 1466.
- astrakhan-khanate 1523 occupation_start -> crimean-khanate: missing (mirror: none). crimean-khanate dossier exists and has no 1523 occupation of Astrakhan (the author says the Crimean Khanate page is silent; the Astrakhan page names Mehmed I Giray in 1523). Route to the crimean-khanate owner (ia-02); same for the 1523 occupation_end.
- astrakhan-khanate 1549 occupation_start -> crimean-khanate: missing (mirror: none). No 1549 occupation (Sahib I Giray) in crimean-khanate; route to its owner (ia-02).
- astrakhan-khanate 1556 loss -> tsardom-of-russia: exception (mirror: none). tsardom-of-russia belongs to eu-16, which has not run yet; also the 1554-56 contest (the page says Russia 'imposed its client', eu-16 may prefer vassal_start 1554).
- mongol-khanate 1455 found -> four-oirats: matched (mirror: four-oirats 1455 loss). Same land: Four Oirats 1450 minus Four Oirats 1468 on both sides.
- mongol-khanate 1481 gain -> four-oirats: matched (mirror: four-oirats 1480 dissolve). Within one year; land Four Oirats 1468 on both sides (four-oirats_1475 kept to 1480).
- mongol-khanate 1495 gain -> ming-dynasty: exception (mirror: none). ming-dynasty belongs to ea-07, not run yet; ea-07 should record the Three Guards lands (Cliopatria's 539,000 km2 of 1516) lost by 1495 and check the 627,000 km2 Qinghai/Gansu overlap of 1468-1546.
- mongol-khanate 1519 gain -> moghulistan: missing (mirror: none). moghulistan (ia-02-d) ends in 1518 with a dissolve to western-moghulistan and gives no land to mongol-khanate; both sides confidence 1 with no page. Route to moghulistan / eastern-moghulistan (ia-03) owners, or drop the strip from mongol-khanate if no page supports it.
- mongol-khanate 1547 loss -> tumed: exception (mirror: none). tumed belongs to ia-03, not run yet.
- mongol-khanate 1547 loss -> khalkha: exception (mirror: none). khalkha has no dossier and is listed in the author's counterparts_needing_dossiers. The golden-horde dossier's notes on its mislabelled 1547-1632 shapes attribute them to the mongol-khanate (Northern Yuan line) to 1635, not to Khalkha from 1547: the orchestrator should settle one reading.
- mongol-khanate 1635 loss -> later-jin-dynasty: exception (mirror: none). later-jin-dynasty belongs to ea-08, not run yet; also the 1632-35 contest and the dissolve.
- kapisa 1475 found -> timurid-empire: mismatch (mirror: none). timurid-empire has no 1475 loss and its 1475/1487/1497 corrections add admin1 Kabul (Ulugh Beg II) to the Timurid Empire: Kabul double-claimed 1475-1500. Its 1502 keyframe leaves Kabul out 1501-1503.
- kapisa 1506 dissolve -> timurid-empire: mismatch (mirror: timurid-empire 1504 gain). timurid-empire /ledger/45 gains Kabul in October 1504 (confidence 3, Babur page; counterpart written as 'Kabul (previous holder not named on the page)', should become kapisa); kapisa keeps it to 1506 at confidence 1. Kapisa should end in October 1504.
- eastern-chagatai-khanate 1492 found -> moghulistan: matched (mirror: moghulistan 1492 loss). Same land on both sides: Eastern Chagatai Khanate 1492 plus Tashkent (120 km).
- eastern-chagatai-khanate 1503 loss -> shaybanids: exception (mirror: none). shaybanids belongs to ia-03, not run yet; kazakh-khanate (ia-03) should also be checked: Cliopatria draws Tashkent as Kazakh 1483-1501.
- eastern-chagatai-khanate 1511 dissolve -> moghulistan: matched (mirror: moghulistan 1512 gain). Within one year; both confidence 1-2; the page gives the land to the Kyrgyz.
