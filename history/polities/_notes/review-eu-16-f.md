# Review of batch eu-16-f (reviewer, 2026-11-01; brief filled 2026-10-31)

Dossiers: grand-principality-of-moscow, nizhny-novgorod, principality-of-beloozero, principality-of-pinsk, principality-of-turov. Validator (--resolve): 0 errors in all five; Moscow has 5 unknown-slug warnings (counterparts without dossiers, listed by the author) and 2 gazetteer warnings (Pereslavl-Zalessky). Pages opened: Principality of Moscow, Battle of Shelon, Muscovite-Lithuanian Wars, Vasili III, Ivan III (twice), Nizhny Novgorod, Principality of Beloozero, Pinsk, Principality of Turov, ru.wikipedia Суздальско-Нижегородское княжество (two en titles failed).

Summary: Moscow **fail** (one unexplained ~22,000 km2 step in 1304 and five missing mirror sets: Dvina 1397-1398, Kazan 1444-1445 and 1487, Gomel 1503-1535; every confidence-3 event I opened is on its page). Nizhny Novgorod **thin** (and a duplicate-dossier proposal to withdraw). Beloozero **thin**. Pinsk **fix**, fixed by the reviewer (war start 1274 -> 1294; re-validated OK). Turov **thin** (all confidence 1, within its one-page budget).

## grand-principality-of-moscow: fail

Area: infobox 39000 (1462) vs Cliopatria 317907; ratio 8.15; acknowledged True. The Principality of Moscow page has no infobox area; the figure is the Ivan III page's 'more than 15,000 square miles (39,000 square kilometres) at the end of Vasily II's reign' against the 1453-1462 shape. Keyframe notes acknowledge it (page figure = Moscow's own domain) and the 'tripled' (x6.7) and 'nearly doubled' (x4.8) ratios. War page figures match: 1494 87,000 km2, 1503 210,000 km2 (author: 677 cells ~170,000 km2).

Findings:
- `/keyframe_review/4/correction` (not applied): BLOCKING (not applied). The new 1304 keyframe takes Cliopatria's whole 1314 shape (46,883 km2), so besides Mozhaysk (21 cells, ledger/3) about 95 cells (~22,000 km2: Dmitrov, Klin and the rest of Cliopatria's 1305 step from Vladimir-Suzdal, plus the Kolomna/Serpukhov cells beyond the two 30 km discs) enter Moscow in 1304 with no ledger event; the 1302-1303 keyframe is only about 19,700 km2. The author's report and notes list 'Dmitrov and Klin (1305)' as a confidence-1 event, but the ledger has no 1305 event. Evidence: shapes.csv: grand-principality-of-moscow_1305 42,338 km2, _1314 46,883 km2; keyframe 3 = Moscow 1294 (10,246 km2) + three discs; ledger/3 region = Moscow 1314 minus Moscow 1305 (Mozhaysk only). principality-of-vladimir-suzdal /ledger/2 has 'loss 1305 -> grand-principality-of-moscow' (Pereslavl and its neighbours, c1) with no Moscow event within a year. Fix: Add a gain (1305, or 1304 to match the keyframe; c1, counterpart principality-of-vladimir-suzdal, region {minus:[{cliopatria: Grand Principality of Moscow, year:1305},{union:[{cliopatria: Grand Principality of Moscow, year:1294},{place:Kolomna,km:30},{place:Serpukhov,km:30},{place:Pereslavl-Zalessky,km:35}]}]}, text 'Dmitrov, Klin and the rest of Cliopatria's 1305 step') and, if dated 1305, make keyframe 4 (1304) = union(keyframe 3, Mozhaysk) instead of the whole 1314 shape.
- `/ledger (1397, 1398)` (not applied): BLOCKING (not applied). No mirror for the Novgorod dossier's confidence-3 pair: Moscow annexes the Dvina Lands in 1397 and Novgorod recovers them in 1398. Evidence: novgorod-republic /ledger/19 loss 1397 -> grand-principality-of-moscow (c3, '1397: Moscow annexed the Dvina Lands') and /ledger/20 gain 1398 from grand-principality-of-moscow (c3). Moscow's own ledger/13 note mentions it but records only a 1398 gain from nobody of the Sukhona/Ustyug cells. Fix: Add gain 1397 (counterpart novgorod-republic, region the Dvina Lands as the Novgorod dossier draws them, c2/c3 citing the Novgorod Republic page) and loss 1398 (same region, counterpart novgorod-republic), with a one-year keyframe 1397 if the Dvina Lands lie outside the 1395 shape.
- `/ledger (1487) and /identity notes on Kazan` (not applied): BLOCKING (not applied). Moscow's 1487 capture and vassalage of Kazan is missing: no occupation pair mirroring the Kazan dossier, and no vassal_start khanate-of-kazan although the Ivan III page the dossier cites dates it. The dossier's note says 'no page opened for this dossier dates Kazan's break from Moscow, so no Kazan vassal pair is recorded' - the start is dated on that page. Evidence: Ivan III page (opened 2026-11-01): 'In 1487, Ivan reduced the Khanate of Kazan, one of the offshoots of the Horde, to the condition of a vassal state' and 'though in his later years, it broke away from his suzerainty' (undated). khanate-of-kazan /ledger/5 occupation_start 1487-06 and /ledger/6 occupation_end 1487-07, counterpart grand-principality-of-moscow. Schema: vassalage is recorded by the suzerain; occupation 'the owner records the same event with the roles reversed'. Fix: Add occupation_start 1487-06 / occupation_end 1487-07 (counterpart khanate-of-kazan, region Kazan as in the Kazan dossier) and vassal_start 1487-07 (counterpart khanate-of-kazan, c3, Ivan III page) with a vassal_end at the break (c1, e.g. 1496 or 1505 with the page's 'in his later years'; or find the Khanate of Kazan page's year). Add the Russo-Kazan wars (1467-1469, 1487, 1505-1507) to wars[].
- `/ledger (1444-1445)` (not applied): BLOCKING (not applied). No mirror for Kazan's occupation of Nizhny Novgorod, which is Moscow's land from 1392 in this dossier. Evidence: khanate-of-kazan /ledger/1 occupation_start 1444 (c2, 'in 1444-45 Ulugh Muhammad occupied Nizhny Novgorod') and /ledger/2 occupation_end 1445 (c1), counterpart grand-principality-of-moscow. Fix: Add occupation_start 1444 / occupation_end 1445 with counterpart khanate-of-kazan and region {place: Nizhny Novgorod, km: 42} (roles reversed: Moscow is the owner), citing the Kazan dossier's page.
- `/ledger (1503, 1535) and /keyframe_review/34..42` (not applied): BLOCKING (not applied). Gomel is Muscovite from 1503 to 1535 in the Jagiellon dossier (and on the war page: Lithuania regained Homel in 1535-1537, 'Gained 20,000 km2' in 1537), but Moscow neither gains nor loses it; the note's reason is only that Cliopatria's Moscow shape lacks Gomel's cells. Evidence: house-of-jagiellon /ledger/19 loss 1503 -> grand-principality-of-moscow (Gomel, c2) and /ledger/28 gain 1535 from grand-principality-of-moscow (Gomel, c3). Muscovite-Lithuanian Wars page: 'launched a powerful counterattack and took Gomel and Starodub'; truce 'in which Homel stayed under the king's control, while Moscow kept Sebezh and Zavoloche'; table '1537: Gained 20,000 km2 - Fifth war with Russia'. Fix: Add gain 1503-03 (counterpart house-of-jagiellon, region Gomel as the Jagiellon dossier draws it, c2) and loss 1535 (same region, c3), and add the Gomel region to keyframes 34-42 for 1503-1534 (minus it from 1535).
- `/ledger/15/counterpart` (not applied): Counterpart principality-of-vladimir-suzdal is dead in 1415: that dossier dissolves in May 1389 and hands Bezhetsk to principality-of-uglich (its /ledger/10, 'the Uglich and Bezhetsk lands stay outside Moscow's own domain'). Evidence: principality-of-vladimir-suzdal identity.end 1389-05; its successors list principality-of-uglich (proposed) for 'the Uglich and Bezhetsk lands'. Fix: Use the holder the pages support for Bezhetsk in 1415 (principality-of-uglich as the Vladimir-Suzdal dossier reads it, or novgorod-republic for Bezhetsky Verkh) and say so in the note; not applied because no page I opened names the holder.
- `/ledger/14` (not applied): Mis-dated confidence-1 event: the Kaluga and Oka cells are dated 1402 (Cliopatria's year) although the dossier's own page dates Kaluga 1397-1398. Evidence: ledger/14 note: 'The Vasily I page dates Kaluga to 1397-1398'; ledger/13 quotes 'In 1397-1398 Kaluga, Vologda, Veliki Ustyug and the lands of the Komi peoples were annexed'. No golden-horde loss mirrors the 1402 gain either. Fix: Move the Kaluga gain to 1398 (c2, citation-needed caveat in the note) and include its cells in keyframe 14 (1398-1401), or explain why the 66 cells are not Kaluga.
- `/keyframe_review/23` (not applied): Rostov is removed for the whole Cliopatria span 1463-1474 but the gain is dated 1474 (ledger/21); the shape shows Rostov only from 1475. The note says 'taken out for 1463-1473'. Evidence: shapes.csv grand-principality-of-moscow_1463 runs 1463-1474; no new keyframe for 1474. Fix: Add a one-year keyframe 1474 (the 1463 shape with Rostov plus the two discs) or set keyframe 23's to = 1473.
- `/keyframe_review/26, /keyframe_review/37, /keyframe_review/39, /keyframe_review/40` (not applied): Keyframe steps with no ledger event: 1482 adds Uglich (26 cells) and 76 unclaimed cells; 1512 adds 120 unclaimed cells in the south (36-37 E, 51-52 N); 1516 drops 42 cells and 1519 drops 22 cells on the Lithuanian side. Each is small (about 1 percent of the shape) but the author added confidence-1 'nobody' events for comparable steps in 1344, 1502 and 1503 and not for these. Evidence: Keyframe notes 26 ('Uglich 26, 76 unclaimed'), 37 ('120 unclaimed cells in the south'), 39 ('42 cells ... dropped'), 40 ('22 cells dropped'). Fix: Add confidence-1 gain/loss events (Cliopatria's year, counterpart nobody / principality-of-uglich / house-of-jagiellon) or correct the keyframes to keep the cells unchanged.
- `/ledger/34, /ledger/41, /keyframe_review/34` (not applied): The Novgorod-Seversk protectorate (vassal_start 1503, c1, 'no page says so') overlaps land that ledger/32 and keyframe 34 already give Moscow outright from 1503, so the same ground is both direct and vassal 1503-1522; Starodub (annexed 1523, Vasili III page) has no event. Evidence: ledger/32 region = Jagiellon 1502 cells that enter Moscow's 1507 shape, which include Novgorod-Seversky; keyframe 34 draws them as Moscow's. Fix: Either draw the Seversk princes' lands as a vassal (minus them from keyframes 34-41 until 1522/1523) or drop the vassal pair; add Starodub 1523.
- `/wars (Tver)` (not applied): The Tver dossier has a contest pair with Moscow 1368-1375 (zone drawn) and another in 1485; Moscow's Tver war runs 1370-1375 with empty zones and there is no 1485 war entry. Evidence: tver /ledger/3 contest_start 1368 ('by 1368 ... the Muscovite army invaded Tver'), /ledger/4 contest_end 1375; /ledger/5-6 contest 1485. Fix: Align the war's years with the Tver dossier (1368) or explain; add the 1485 campaign.
- `/keyframe_review/11` (not applied): The 1389-1391 keyframe gives Moscow Suzdal, Shuya and their neighbours (Vladimir-Suzdal 1375 minus 1395) three years before the Suzdal-Nizhny Novgorod principality fell in 1392; Suzdal was one of that principality's centres. Evidence: ru.wikipedia Суздальско-Нижегородское княжество: formed October 1341, centres 'Суздаль, Юрьевец, Городец', 1392 Vasily I took Nizhny Novgorod. Fix: Move Suzdal and its cells to the 1392 gain from nizhny-novgorod (with the nizhny-novgorod dossier extended to them), or note why they are Vladimir's in 1389.

Thin (for a gap-filler):
- `/ledger/4,/ledger/5-8,/ledger/9,/ledger/10,/ledger/15,/ledger/17,/ledger/30,/ledger/33,/ledger/38`: Confidence-1 events at Cliopatria's years (1333, 1344 x4, 1363, 1375, 1415, 1463 Novgorod cells, 1502, 1503 unclaimed, 1519): a page dating Ivan I's purchases (Uglich, Galich, Beloozero), the Smolensk border 1363, Yuryev-Polsky, Bezhetsk, and the 1518-1519 Lithuanian border. Page: https://en.wikipedia.org/wiki/Ivan_I_of_Moscow
- `/ledger (1452)`: Moscow's suzerainty over the Qasim Khanate from 1452 (suzerain side; the qasim-khanate dossier's found event names Moscow). Page: https://en.wikipedia.org/wiki/Qasim_Khanate
- `/identity/rulers/0`: Rulers start 1282 although the life starts 1263 (Daniel held Moscow as a minor from 1263). Page: https://en.wikipedia.org/wiki/Daniel_of_Moscow

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Moscow: confirmed ('Daniel defeated Ryazan in 1301, after which Kolomna and Serpukhov were incorporated into the Moscow principality')
- `/ledger/3` https://en.wikipedia.org/wiki/Principality_of_Moscow: confirmed ('his sons seized Mozhaysk in 1304')
- `/ledger/12` https://en.wikipedia.org/wiki/Principality_of_Moscow: confirmed ('In 1392 ... Vasily was given permission to take the throne of Nizhny Novgorod')
- `/ledger/19, /ledger/22` https://en.wikipedia.org/wiki/Battle_of_Shelon: confirmed (Korostyn: 'patrimony of the grand prince', 'retained its autonomy'; 'direct control of the city-state in January 1478')
- `/ledger/27` https://en.wikipedia.org/wiki/Muscovite%E2%80%93Lithuanian_Wars: confirmed (5 February 1494; Vyazma and upper Oka; 87,000 km2)
- `/ledger/32` https://en.wikipedia.org/wiki/Muscovite%E2%80%93Lithuanian_Wars: confirmed (25 March 1503; Chernigov, Novgorod-Seversk, Starodub; 210,000 km2, a third of the Grand Duchy)
- `/ledger/35` https://en.wikipedia.org/wiki/Vasili_III_of_Russia: confirmed ('On 13 January, the veche bell was removed')
- `/ledger/37` https://en.wikipedia.org/wiki/Vasili_III_of_Russia: confirmed ('On 31 July, the residents of Smolensk swore allegiance ... Vasily entered the city on 1 August')
- `/ledger/16, /ledger/21, /ledger/24, /ledger/25` https://en.wikipedia.org/wiki/Ivan_III_of_Russia: confirmed ('the Principality of Yaroslavl in 1463, Rostov in 1474, Tver in 1485, and Vyatka 1489')
- `/ledger/39` https://en.wikipedia.org/wiki/Vasili_III_of_Russia: confirmed ('the principality of Ryazan in 1521')

## nizhny-novgorod: thin

Area: infobox None (None) vs Cliopatria 5416; ratio None; acknowledged True. City article, no state area; the author notes the disc is displaced ~90 km and moves it.

Findings:
- `/notes and the author's counterparts_needing_dossiers` (not applied): Not applied, non-blocking. One state, two dossiers: this dossier already carries the Suzdal-Nizhny Novgorod principality from 1350 (rename) to 1392, while the author's report asks eu-16-x to write principality-of-suzdal-nizhny-novgorod for 1350-1392 on the same land. Evidence: nizhny-novgorod /ledger/1 rename 1350 ('From here the polity is the capital of the Suzdal-Nizhny Novgorod principality'); report counterparts_needing_dossiers 'Principality of Suzdal-Nizhny Novgorod' 1350-1392. Fix: Withdraw the proposal and make this dossier the Nizhny Novgorod-Suzdal principality: rename in October 1341 (its formation), capital Nizhny Novgorod from 1350, land Suzdal, Gorodets, Yuryevets and Nizhny Novgorod to 1392 (ru.wikipedia page below); the Moscow and Vladimir-Suzdal dossiers then hand Suzdal over in 1392, not 1389.

Thin (for a gap-filler):
- `/keyframe_review/0-1`: The extent 1341-1392 is a 42 km disc at the city; the principality held Suzdal, Gorodets and Yuryevets (formed October 1341; seat moved to Nizhny Novgorod 1350; restored 1393, 1411-1414, 1425, 1446-1447). Page: https://ru.wikipedia.org/wiki/%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%BE-%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE
- `/ledger/0`: Start 1294 is Cliopatria's (c1); the city was the Gorodets prince Andrey's and then the grand princes' until 1341, so the state's real start is 1341. Page: https://ru.wikipedia.org/wiki/%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%BE-%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Nizhny_Novgorod: confirmed ('the seat of the powerful Suzdal Principality was moved there from Gorodets in 1350')
- `/ledger/2` https://en.wikipedia.org/wiki/Nizhny_Novgorod: confirmed ('After the city's incorporation into the Grand Principality of Moscow in 1392, the local princes took the name Shuysky')
- `/ledger/0` https://en.wikipedia.org/wiki/Nizhny_Novgorod: confirmed as page-silent: the page has founding 4 February 1221 and incorporation into Vladimir-Suzdal in 1264, nothing for 1294 (c1 is honest)

## principality-of-beloozero: thin

Area: infobox None (None) vs Cliopatria 10010; ratio None; acknowledged True. Infobox has no area.

Findings:
- `/keyframe_review/1` (not applied): Not applied, minor. Lake Kubenskoye is in the 1238-1293 keyframe and dropped from 1294 with no ledger event; the region adds the lake surface only, about 50 km east of the Cliopatria shape, so it draws as a detached blob. Evidence: keyframe 0 correction union(Beloozero 1294, lake Kubenskoye); keyframe 1 verdict ok without it; shapes.csv bbox east edge 38.87 E. Fix: Keep the lake in all three keyframes (the page names it for Gleb's time only, so a c1 loss in 1294 also works) and join it to the shape with the Sheksna/Kubena land, e.g. a place disc, so it does not float.

Thin (for a gap-filler):
- `/ledger/1-2`: End 1343 is Cliopatria's (c1). The page gives namestniks under Ivan Kalita (d. 1340), 'In 1389, it was subjugated by Muscovy', and formal annexation 1485/1486; a page dating the namestniks or the Ivan I purchase would turn the end into c2. Page: https://en.wikipedia.org/wiki/Ivan_I_of_Moscow

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Beloozero: confirmed (infobox 'Established: 1238'; 'detached from the Principality of Rostov in 1238'; Gleb ca. 1238-1278; Lake Beloye, lower Sheksna, Lake Kubenskoye)
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Beloozero: confirmed as page-silent on the year (namestniks 'instead of the princes', 1389 subjugation, 1485/1486 annexation); c1 honest

## principality-of-pinsk: fix

Area: infobox None (None) vs Cliopatria 34431; ratio None; acknowledged True. Neither the Turov nor the Pinsk page gives an area.

Findings:
- `/wars/0/from` (APPLIED): The war 'Pinsk against Lithuania' started in 1274, twenty years before the dossier's start (1294). Evidence: Pinsk page: 'In 1274, Pinsk along with Ruthenian princes and Tatars fought against Lithuania'; reviewer brief 2.2: wars inside the life. Fix: from: 1294, with the 1274 fighting kept in the note.

Thin (for a gap-filler):
- `/ledger/0`: Start 1294 is Cliopatria's (c1); the Turov page has 'A semi-independent Principality of Pinsk was created' with no year. Page: https://en.wikipedia.org/wiki/Principality_of_Turov
- `/wars/0, /identity/successors`: The Pinsk page has Pinsk 'captured by Lithuanian duke Erdvilas' and 'a fief of Lithuania' after 1274, before the 1320 incorporation: a Lithuanian vassalage (suzerain side, grand-duchy-of-lithuania) that no dossier draws; no year. Page: https://en.wikipedia.org/wiki/Narimantas

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Pinsk: confirmed ('By 1320, Pinsk was incorporated into the Grand Duchy of Lithuania')
- `/wars/0` https://en.wikipedia.org/wiki/Pinsk: confirmed (1274 fighting; capture by Erdvilas, fief of Lithuania, undated)
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Turov: confirmed as page-silent ('A semi-independent Principality of Pinsk was created', no year); c1 honest

## principality-of-turov: thin

Area: infobox None (None) vs Cliopatria 29467; ratio None; acknowledged True. Infobox has no area.

Thin (for a gap-filler):
- `/ledger/1-2`: End 1325 is Cliopatria's (c1); the page has only 'In the early 14th century the Principality non-violently joined the Grand Duchy' and lists 'Gediminas (1320- ?)' among the princes, which points to 1320 as for Pinsk. Page: https://en.wikipedia.org/wiki/Gediminas
- `/ledger/0`: Start 1294 is Cliopatria's (c1); the princes' list has 'Dmitry Yuryevich (1292-)'. Page: https://en.wikipedia.org/wiki/Principality_of_Turov

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Turov: confirmed as page-silent ('In the early 14th century the Principality non-violently joined the Grand Duchy'; infobox 'Incorporation into the Grand Duchy of Lithuania: 14th century'); c1 honest
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Turov: confirmed ('Dmitry Yuryevich (1292-)'; 'Hleb Narymunt ... was already ruler of Pinsk, while Turov and Haradok were still ruled by Rurikids')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| grand-principality-of-moscow 1263 found -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal - - | exception | Vladimir-Suzdal dossier starts 1294; Cliopatria lacks the principalities 1240-1294 (group scope, eu-16-x). |
| grand-principality-of-moscow 1301 gain -> ryazan | ryazan - - | exception | ryazan dossier starts 1453; Ryazan 1240-1453 listed in counterparts_needing_dossiers. |
| grand-principality-of-moscow 1302 gain -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1305 loss | mismatch | Moscow dates Pereslavl to 1302 (Daniel page); VS dates the whole 111-cell step (Pereslavl, Dmitrov, Klin) to 1305 (c1). VS should add a 1302 Pereslavl loss; Moscow should add the Dmitrov/Klin gain (see Moscow fix 1). |
| grand-principality-of-moscow 1304 gain -> principality-of-smolensk | principality-of-smolensk 1304 loss | matched | Mozhaysk. |
| grand-principality-of-moscow 1333 gain -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1333 loss | matched |  |
| grand-principality-of-moscow 1344 gain -> principality-of-beloozero | principality-of-beloozero 1343 loss | matched | one year apart, both c1 at Cliopatria years. |
| grand-principality-of-moscow 1344 gain -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1344 loss | matched |  |
| grand-principality-of-moscow 1344 gain -> novgorod-republic | novgorod-republic 1344 loss | matched |  |
| grand-principality-of-moscow 1363 gain -> principality-of-smolensk | principality-of-smolensk - - | missing | Smolensk dossier (eu-16) has no 1363 loss of the 14 border cells. |
| grand-principality-of-moscow 1375 gain -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1375 loss | matched | Yuryev-Polsky. |
| grand-principality-of-moscow 1389 gain -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1389 merge | matched | May 1389. |
| grand-principality-of-moscow 1392 gain -> nizhny-novgorod | nizhny-novgorod 1392 loss | matched |  |
| grand-principality-of-moscow 1402 gain -> golden-horde | golden-horde - - | missing | Golden Horde dossier (ia-02) has no 1402 loss of the Kaluga/Oka cells; Moscow should also re-date to 1398 (Moscow fix 7). |
| grand-principality-of-moscow 1415 gain -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1389 dissolve | mismatch | Counterpart dissolved in 1389 and handed Bezhetsk to principality-of-uglich (proposed, no dossier). |
| grand-principality-of-moscow 1463 gain -> principality-of-yaroslavl | principality-of-yaroslavl - - | exception | no dossier; listed. |
| grand-principality-of-moscow 1463 gain -> novgorod-republic | novgorod-republic 1463 loss | matched |  |
| grand-principality-of-moscow 1471 vassal_start -> novgorod-republic | novgorod-republic 1471 contest_end | exception | Suzerain side only, as the schema prescribes; Novgorod has the 1471 contest pair. |
| grand-principality-of-moscow 1474 gain -> principality-of-rostov | principality-of-rostov - - | exception | no dossier; listed. |
| grand-principality-of-moscow 1478 gain -> novgorod-republic | novgorod-republic 1478 merge | matched | January 1478. |
| grand-principality-of-moscow 1485 gain -> tver | tver 1485 loss | matched | September 1485. |
| grand-principality-of-moscow 1489 gain -> vyatka-land | vyatka-land - - | exception | no dossier; listed. |
| grand-principality-of-moscow 1494 gain -> house-of-jagiellon | house-of-jagiellon 1494 loss | matched | February 1494. |
| grand-principality-of-moscow 1503 gain -> house-of-jagiellon | house-of-jagiellon 1503 loss | matched | March 1503. |
| grand-principality-of-moscow 1503 vassal_start -> principality-of-novgorod-seversk | principality-of-novgorod-seversk - - | exception | no dossier; listed (c1 reading). |
| grand-principality-of-moscow 1510 gain -> pskov-republic | pskov-republic 1510 loss | matched | January 1510. |
| grand-principality-of-moscow 1514 gain -> house-of-jagiellon | house-of-jagiellon 1514 loss | matched | July 1514. |
| grand-principality-of-moscow 1519 gain -> house-of-jagiellon | house-of-jagiellon - - | missing | Jagiellon dossier (eu-15) has no 1519 loss of the 94 cells. |
| grand-principality-of-moscow 1521 gain -> ryazan | ryazan 1521 loss | matched |  |
| grand-principality-of-moscow 1546 dissolve -> tsardom-of-russia | tsardom-of-russia 1547 found | matched | January 1547. |
| novgorod-republic 1397 loss -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Dvina Lands; Moscow lacks the 1397 gain (Moscow fix 2). |
| novgorod-republic 1398 gain -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Moscow lacks the 1398 loss. |
| principality-of-vladimir-suzdal 1305 loss -> grand-principality-of-moscow | grand-principality-of-moscow 1302 gain | mismatch | Only Pereslavl is mirrored (1302); the Dmitrov/Klin cells have no Moscow event. |
| golden-horde 1294 vassal_start -> grand-principality-of-moscow | grand-principality-of-moscow - - | exception | Suzerain side (schema); vassal_end 1480 likewise. |
| khanate-of-kazan 1444 occupation_start -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Kazan occupies Nizhny Novgorod 1444-1445; the owner (Moscow) must record it (Moscow fix 4). |
| khanate-of-kazan 1487 occupation_start -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Moscow takes Kazan 1487; Moscow lacks the occupation pair and the vassal_start the Ivan III page dates (Moscow fix 3). |
| house-of-jagiellon 1503 loss -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Gomel; Moscow never draws it (Moscow fix 5). |
| house-of-jagiellon 1535 gain -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Gomel retaken; Moscow has no loss. |
| qasim-khanate 1452 found -> grand-principality-of-moscow | grand-principality-of-moscow - - | missing | Moscow (suzerain) has no vassal_start qasim-khanate; thin item. |
| tver 1368 contest_start -> grand-principality-of-moscow | grand-principality-of-moscow - - | mismatch | Moscow war 1370-1375 with empty zones; Tver draws a zone from 1368. Contest, not territorial; minor. |
| nizhny-novgorod 1294 found -> principality-of-vladimir-suzdal | principality-of-vladimir-suzdal 1294 found | exception | Both rows start at Cliopatria 1294. |
| principality-of-beloozero 1238 found -> principality-of-rostov-suzdal | principality-of-rostov-suzdal - - | missing | Rostov-Suzdal dossier (eu-16, ends 1240) has no 1238 loss/split for Beloozero ("detached from the Principality of Rostov in 1238"). |
| principality-of-pinsk 1320 loss -> grand-duchy-of-lithuania | grand-duchy-of-lithuania 1326 gain | mismatch | Six years apart; the Pinsk page says "By 1320"; the Grand Duchy (eu-15) gain is c1 at Cliopatria 1326 and should move to 1320, else 1321-1325 is a hole. |
| principality-of-turov 1325 loss -> grand-duchy-of-lithuania | grand-duchy-of-lithuania 1326 gain | matched | both c1. |

## Gazetteer names needed

- Pereslavl-Zalessky (place, grand-principality-of-moscow)

## Counterparts needing dossiers

- Principality of Yaroslavl: `principality-of-yaroslavl` [1218, 1463]
- Principality of Rostov: `principality-of-rostov` [1389, 1474]
- Principality of Uglich (Uglich and Bezhetsk): `principality-of-uglich` [1389, 1493]
- Vyatka Land: `vyatka-land` [1489]
- Principality of Novgorod-Seversk (Seversk princes, with Starodub): `principality-of-novgorod-seversk` [1503, 1523]
- Ryazan 1240-1453 (extend the ryazan dossier back, or a new slug): `ryazan` [1240, 1453]
- NOT a new dossier: Principality of Suzdal-Nizhny Novgorod belongs in nizhny-novgorod (see its fix): `nizhny-novgorod` [1341, 1392]

## Problems

- WebFetch answers come from a small model summarising the page; quotes were requested verbatim and are consistent with the authors' notes.
- en.wikipedia titles Nizhny_Novgorod-Suzdal_Principality and Grand_Principality_of_Nizhny_Novgorod-Suzdal are url_not_found; the ru.wikipedia article loaded and is given as the page to try.
- Moscow fails on missing mirror events and one unexplained ~22,000 km2 step (1304); the Vladimir-Suzdal, Smolensk, Golden Horde, Jagiellon, Grand Duchy and Rostov-Suzdal dossiers each owe a mirror (cross_checks).
- Vassalage counted on the suzerain side only, as the schema prescribes (Golden Horde over Moscow, Moscow over Novgorod).
