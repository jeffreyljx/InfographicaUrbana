# Review of batch eu-16-x (Rus and Russia to 1721, additions)

Reviewer run 2026-11-01 (brief filled 2026-10-31). Seven new dossiers; none has a Cliopatria row, so the page budget is 2-5 pages per state (section 10 of the author's brief). The validator (with --resolve) passed all seven with 0 errors and 0 warnings before and after the reviewer's edits. Machine copy: history/notes/phase-b/reviews/eu-16-x.json.

Verdicts: cossack-hetmanate **fail**, principality-of-murom **thin**, tmutarakan **thin**, principality-of-yaroslavl **fail**, principality-of-zvenyhorod **thin**, principality-of-novgorod-seversk **thin**, great-perm **fix**.

## cossack-hetmanate: fail

Findings:
- `/keyframe_review/1/correction (also /keyframe_review/2,3,4, /identity/predecessors/0/land, /identity/successors/0/land, every ledger region and war zone that contains {"region": "Chernigov"})` (not applied, for the author). {"region": "Chernigov"} resolves to the Chernihiv, Bryansk and Kursk oblasts (417 cells, about 105,500 km2), so the Hetmanate is drawn over all of Kursk oblast (123 cells) and all of Bryansk oblast (154 cells) from 1649 to 1764. That land was Muscovite throughout, and no keyframe note mentions it. Evidence: Gazetteer trace: region Chernigov = admin1 Chernihiv + Bryansk + Kursk. Anchors p1650: Kursk 108/123 cells tsardom-of-russia, Bryansk 82/154 tsardom-of-russia; p1700: Bryansk 153/154 tsardom-of-russia. Kursk page: 'The revival of Kursk is associated with the construction of a new fortress in 1596 during the reign of Feodor I of Russia' (Belgorod Line, 'southern Russia'). The tsardom-of-russia 1654 vassal_start for this state is Chernihiv + Poltava + Kiev admin1 only. The region's own text is 'the Chernihiv voivodeship', and the Chernihiv Voivodeship page divides that into just 'two counties: Czernihow and Nowogrod Siewierski'. Anchors p1700 also give 42 of 104 Sumy cells to sloboda-ukraine. Fix: Replace {"region": "Chernigov"} with {"admin1": "Chernihiv", "country": "Ukraine"} plus {"lon": 32.767, "lat": 52.583, "km": 60, "text": "Starodub regiment"} everywhere it occurs (or a Starodub place once the gazetteer has it). Consider removing Cliopatria's Sloboda Ukraine from Sumy. Then redo the area comparison in the keyframe notes. The corrected left bank resolves to about 114,600 km2 (453 cells) against the infobox's 208,000 for 1686-1764 (ratio 0.55), and the corrected both-banks shape to about 237,000 km2 against 312,000 (0.76). Say in the note why the drawn left bank is about half the infobox figure. Do not restore Kursk to make the numbers fit.
- `/ledger/11, /ledger/13 (with /keyframe_review/4)` (not applied, for the author). The right bank leaves the keyframes in 1672 (KF4 is left bank only), but the ledger records only an occupation (occupation_start 1672, occupation_end 1699) and never a loss. By the ledger, the right bank stays Hetmanate land under hatching and goes back to the Hetmanate in 1699, yet the 1699 note says the land 'returns to the Commonwealth, not to the Hetmanate'. Evidence: Schema: occupation_* means 'occupies region belonging to counterpart without annexing it'. The ledger's last right-bank ownership event is the 1668 gain. Hetmanate page: the right bank 'was temporarily occupied by the Ottoman Empire in the period of 1672-1699' and 'on the right bank, the Poles abolished the Cossack self-government and the regimental system in 1699'. The Treaty of Perpetual Peace (1686, already in sources) gives the right bank to the Commonwealth. ottoman-empire records 1672 gain/1699 loss of Podolia against polish-lithuanian-commonwealth, not an occupation of this state's land. Fix: Choose one. (a) Make /ledger/11 a 'loss' to ottoman-empire (1672, same region and quotes) and delete /ledger/13; this matches KF4 and the ottoman-empire 1672 gain. (b) Add a keyframe for 1672-1685 that keeps the right bank (hatched by the occupation), add a 1686 'loss' to polish-lithuanian-commonwealth of the right bank citing https://en.wikipedia.org/wiki/Treaty_of_Perpetual_Peace_(1686), end the occupation in 1686, and start KF4 in 1686, which also matches the infobox's 1686-1764 area. Either way the right bank must leave the Hetmanate through a loss event.
- `/identity/rulers/9/to` (applied by reviewer). Danylo Apostol's entry was 1727-1727, with a note saying 'the page gives no end year'. Evidence: Hetmanate page: elected '1 October 1727'; 'After Apostol's death in 1734, power in the Hetmanate was transferred' to the Governing Council of the Hetman Office. Fix: to: 1734; note rewritten with the quote (done by the reviewer; validator OK).
- `/ledger/18/month` (not applied, for the author). Non-blocking: the text gives 21 October 1764 and the infobox '21 (10) November 1764'. The dossier takes October without recording the disagreement. Evidence: Hetmanate page, read 2026-11-01. Fix: Add the infobox date to the /ledger/18 note (no change of month needed).

Thin (for a gap-filler):
- `/identity/rulers`: Pavlo Teteria (right bank) and Ivan Briukhovetsky (left bank) for 1663-1668 are absent, leaving a gap from 1663 to 1665. The 1734-1750 interregnum (Governing Council of the Hetman Office) is not stated. The Hetmanate page gives no years for Teteria or Briukhovetsky. Try: https://en.wikipedia.org/wiki/Ivan_Briukhovetsky
- `/ledger (1672-1686)`: The right bank under Doroshenko as an Ottoman client (1669-1676), Doroshenko's surrender of Chyhyryn (1676), and the Bakhchisarai neutral zone (1681) are not dated from a war or treaty page (budget: 5 pages used). Try: https://en.wikipedia.org/wiki/Polish%E2%80%93Ottoman_War_(1672%E2%80%931676)
- `/identity/wikidata`: Wikidata id is null because wikidata.org could not be reached. Try: https://en.wikipedia.org/wiki/Cossack_Hetmanate

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Khmelnytsky_Uprising: confirmed ('on 19 August 1649 the hetman agreed to the Treaty of Zboriv'; the Hetmanate page says 18 August, as the author notes)
- `/ledger/3` https://en.wikipedia.org/wiki/Khmelnytsky_Uprising: confirmed ('provided autonomy to Cossack-held voivodeships of Kyiv, Bratslav and Chernihiv')
- `/ledger/6` https://en.wikipedia.org/wiki/Russo-Polish_War_(1654%E2%80%931667): confirmed ('Towards the end of 1663, the Polish-Lithuanian King crossed the Dnieper and invaded Left-bank Ukraine')
- `/ledger/7` https://en.wikipedia.org/wiki/Russo-Polish_War_(1654%E2%80%931667): confirmed ('Peace negotiations dragged on from 1664 until January 1667')
- `/ledger/8` https://en.wikipedia.org/wiki/Cossack_Hetmanate: confirmed ('secured 10 regiments of left-bank Ukraine for Russia, including Kyiv, while the other six stayed in right-bank Ukraine')
- `/ledger/11` https://en.wikipedia.org/wiki/Cossack_Hetmanate: confirmed ('In 1672, Ottoman troops captured Podillia, the Bratslav region, and the southern Kyiv region'; occupied '1672-1699')
- `/ledger/12` https://en.wikipedia.org/wiki/Cossack_Hetmanate: confirmed ('according to the Treaty of Eternal Peace of 1686 it was nominally dependent both on the hetman and the tsar')
- `/ledger/14` https://en.wikipedia.org/wiki/Cossack_Hetmanate: confirmed (sack of Baturyn by Muscovite troops on 13 November 1708)
- `/ledger/17` https://en.wikipedia.org/wiki/Cossack_Hetmanate: confirmed ('The decisive battle of Poltava, which took place on 8 July 1709')
- `/ledger/18` https://en.wikipedia.org/wiki/Cossack_Hetmanate: confirmed ('According to a decree issued on 21 October 1764, the hetman's post was officially liquidated'; infobox '21 (10) November 1764')

Area: No Cliopatria row. Infobox 312,000 km2 (1649-1667) and 208,000 km2 (1686-1764) confirmed. The author's ratios (0.95 and 0.84 at 173,995 km2) count Kursk and Bryansk oblasts. Without them the shapes come to about 237,000 km2 (0.76) and 114,600 km2 (0.55).

## principality-of-murom: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: The page gives no extent. The 80 km disk is a reading over 265 years with no events. The page says the principality 'bordered the territory of Gorokhovets to the northwest and the Pra to the west', but the disk reaches 56.23 N, Gorokhovets's latitude, so Gorokhovets may sit inside a land the page puts outside. Only 1 of the 2-5 page budget was used. Try: https://en.wikipedia.org/wiki/Principality_of_Ryazan
- `/ledger/0`: The Murom-Ryazan union of 1127-1129 and the later split from Ryazan are undated ('By the end of the 12th century, the family had split into two'). The disk overlaps Cliopatria's Ryazan row (37 of 80 cells in 1100-1200), and principality-of-chernigov records its 1127 loss against principality-of-ryazan, not this state. Try: https://ru.wikipedia.org/wiki/%D0%9C%D1%83%D1%80%D0%BE%D0%BC%D1%81%D0%BA%D0%BE%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Murom: confirmed ('In 1127, it became a separate principality'; 'The youngest, Yaroslav, ruled in Murom and Ryazan from 1127'; the page's ruler list gives Yaroslav 1097-1129)
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Murom: confirmed ('In 1392, Vasily I of Moscow obtained a patent from Tokhtamysh authorizing the annexation of the Murom principality')
- `/wars/0` https://en.wikipedia.org/wiki/Principality_of_Murom: confirmed ('Murom was destroyed or at least devastated by the Mongol invasion of 1237-1238')
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Principality_of_Murom: confirmed (capital Murom; infobox 1127-1392, successor Grand Principality of Moscow)

Area: No area on the page and no Cliopatria row; the keyframe note says so.

## tmutarakan: thin

Findings:
- `/ledger/0/confidence` (applied by reviewer). The found event was at confidence 3, but the cited Kievan Rus' page gives the division list ('Principality of Chernigov and Tmutarakan, for Sviatoslav II of Kiev') without a year; 1054 comes from Yaroslav's death in the rus dossier. Evidence: Kievan Rus' page, read 2026-11-01: the list sits in a passage saying Yaroslav 'assigned priority to the major principalities' and is not dated to 1054. Fix: confidence 2, with a bracketed reviewer remark at the head of the note (done by the reviewer; validator OK).

Thin (for a gap-filler):
- `/ledger/1`: The end of Rus rule is a confidence-1 bridge at Oleg's departure. The Tmutarakan page says only 'in 1094, like Mstislav before him, he returned to Rus to claim the throne of Chernigov', and its 'last recorded mention was in a scroll of 1378'. Try: https://ru.wikipedia.org/wiki/%D0%A2%D0%BC%D1%83%D1%82%D0%B0%D1%80%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE
- `/identity/type`: Identity decision: the Kievan Rus' page calls it 'the Black Sea port of Tmutarakan belonging to Chernigov', and principality-of-chernigov's 1054 gain names Tmutarakan in its note but does not draw it. The orchestrator should decide whether Tmutarakan stays a separate dossier or becomes a Chernigov exclave (the author raises this too). Try: https://en.wikipedia.org/wiki/Principality_of_Chernigov

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kievan_Rus%27: confirmed for the land and the 'belonging to Chernigov' sentence; the year is not on the page (confidence lowered to 2)
- `/ledger/1` https://en.wikipedia.org/wiki/Tmutarakan: confirmed as a bridge: Oleg left in 1094; no page dates the end (confidence 1, honest)
- `/wars/0` https://en.wikipedia.org/wiki/Tmutarakan: confirmed ('in 1064 he was displaced by the rival Rus prince Rostislav Vladimirovich'; poisoned 'on 3 February 1066')
- `/keyframe_review/0/correction/text` https://en.wikipedia.org/wiki/Tmutarakan: confirmed ('trading town that controlled the Cimmerian Bosporus, the passage from the Black Sea to the Sea of Azov')

Area: No area on the page; the infobox describes the archaeological site.

## principality-of-yaroslavl: fail

Findings:
- `/keyframe_review/0/correction (also /ledger/0/region, /ledger/1/region, /identity/predecessors/0/land, /identity/successors/0/land)` (not applied, for the author). The Yaroslavl-oblast proxy covers the seats of three other principalities for the whole 1218-1463 life: Rostov Veliky (18 of the 21 cells of a 40 km disk), Uglich (11 of 12 cells of a 30 km disk) and Pereslavl-Zalessky (7 of 7 cells of a 25 km disk). Evidence: The Yaroslavl page bounds the land only by the Volga 'with its feeders - the Mologa, the Yukhot', the Ikhra, the Sit', the Sheksna and Lake Kubenskoye' and names none of the three towns. grand-principality-of-moscow records a separate 1474 gain of principality-of-rostov ('Rostov in 1474', Ivan III page) at Rostov Veliky 40 km. principality-of-vladimir-suzdal lists principality-of-rostov and principality-of-uglich as successors beside this state. Anchors p1400: the Pereslavl disk is 7/7 grand-principality-of-moscow, the Rostov disk 12 vladimir-suzdal and 9 moscow. Fix: {"minus": [{"union": [<current union>]}, {"place": "Rostov Veliky", "km": 40}, {"place": "Uglich", "km": 30}, {"lon": 38.85, "lat": 56.74, "km": 30, "text": "Pereslavl-Zalessky, Muscovite from 1302"}], "text": ...}. Take the Pereslavl coordinates from its page (the gazetteer lacks the name), and say in the keyframe note that the southern oblast belongs to Rostov, Uglich and Moscow.

Thin (for a gap-filler):
- `/identity/rulers`: Only the first of 11 rulers cites a page, and the entries overlap around 1257-1299 (the author notes it). The page gives no year for Aleksandr Bryukhaty's renunciation. Try: https://en.wikipedia.org/wiki/Ivan_III_of_Russia
- `/ledger`: No events between 1218 and 1463: the Mongol tribute, the 1262 rising, and Moscow's purchases are not dated as land moves (2 pages used). Try: https://ru.wikipedia.org/wiki/%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D1%81%D0%BA%D0%BE%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Yaroslavl: confirmed ('Established: 1218'; 'Vsevolod Konstantinovich (r. 1218-1238)'; 'separated from Vladimir-Suzdal when the sons of Konstantin Vsevolodovich divided his lands upon his death')
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Yaroslavl: confirmed ('existed from 1218 until 1463 (de jure until 1471)'; Bryukhaty 'was forced to sign away the succession to Ivan III', no year)
- `/wars/0` https://en.wikipedia.org/wiki/Principality_of_Yaroslavl: confirmed (Battle of the Sit River, March 4, 1238, Vsevolod killed)
- `/keyframe_review/0/correction/text` https://en.wikipedia.org/wiki/Principality_of_Yaroslavl: confirmed (river list quoted verbatim; the page names no town of the territory)

Area: No area on the page. The resolved 53,100 km2 includes the Rostov, Uglich and Pereslavl lands (see the fix).

## principality-of-zvenyhorod: thin

Thin (for a gap-filler):
- `/keyframe_review/0 and /identity/capitals/0`: The page places the principality only 'in the west of modern Ukraine' and does not locate Zvenyhorod. The disk and the capital point are Lviv's, not Zvenyhorod's. 1 of the 2-5 page budget was used. Try: https://uk.wikipedia.org/wiki/%D0%97%D0%B2%D0%B5%D0%BD%D0%B8%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D1%8C%D0%BA%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B7%D1%96%D0%B2%D1%81%D1%82%D0%B2%D0%BE
- `/ledger/1`: The end year disagrees with the Halych dossier: this page has 1141 for the union, and principality-of-halych's 1145 gain cites Ivan Berladnyk. The Peremyshl and Terebovlia dossiers support 1141. The Halych owner (eu-16-d) should reconcile. Try: https://en.wikipedia.org/wiki/Principality_of_Halych

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Zvenyhorod: confirmed ('Around the year of 1084, the principalities of Zvenyhorod, Terebovlia and Peremyshl were founded within the Principality of Volhynia'; 'Zvenyhorod went to Volodar Rostyslavych')
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Zvenyhorod: confirmed ('In 1141 the principality united with Peremyshl and Terebovlia'; the union is not named on the page, as the note says)
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Principality_of_Zvenyhorod: page gives no location; Lviv coordinates are the author's acknowledged approximation

Area: No infobox on the page.

## principality-of-novgorod-seversk: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: One disk is drawn as a state for 1097-1503, but the page says it 'was taken by the principality of Briansk after the Mongol invasions' and then 'by the Lithuanians when the power of the Golden Horde began to decline' (undated). Anchors give golden-horde 137/137 cells in 1300 and grand-duchy-of-lithuania 137/137 in 1400. The Briansk and Lithuanian periods need dated events or a status (vassal) change. 2 of the 2-5 page budget were used. Try: https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4-%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D1%81%D0%BA%D0%BE%D0%B5_%D0%BA%D0%BD%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE
- `/ledger/1`: The end conflicts with grand-principality-of-moscow: Moscow has vassal_start principality-of-novgorod-seversk in 1503 and vassal_end plus gain in 1522 ('Novgorod-Seversk (1522)', Vasili III page), so it keeps the principality alive as a vassal until 1522. Either extend this dossier to 1522 as a Moscow vassal, or Moscow turns its 1503 vassal_start into a gain. The page's 'Disestablished: 1503' supports this dossier. Try: https://en.wikipedia.org/wiki/Vasili_III_of_Russia
- `/wars/0`: The war has a zone, but the ledger has no contest_start/contest_end for 1500-1503 (non-blocking; the page does not mention the Shemyachich defection of 1500). Try: https://en.wikipedia.org/wiki/Muscovite%E2%80%93Lithuanian_Wars

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Novgorod-Seversk: confirmed (infobox 'Established: 1097'; 'Personal union with the Principality of Chernigov'; confidence 2 fits)
- `/ledger/1` https://en.wikipedia.org/wiki/Muscovite%E2%80%93Lithuanian_Wars: confirmed ('a six-year truce was concluded on the Feast of the Annunciation (March 25) in 1503'; Lithuania lost 'Chernigov, Novgorod-Seversk, Starodub, and lands around the upper Oka River'; the N-S infobox has 'Disestablished: 1503')
- `/wars/1` https://en.wikipedia.org/wiki/Principality_of_Novgorod-Seversk: confirmed (1185 campaign 'ended in defeat for Prince Igor of Novgorod-Seversk')
- `/keyframe_review/0/note` https://en.wikipedia.org/wiki/Principality_of_Novgorod-Seversk: confirmed (Briansk and Lithuania undated; the Lithuanian claim is tagged citation needed)

Area: No area on the page.

## great-perm: fix

Findings:
- `/ledger/3 (also /wars/0/outcome, /identity/successors/0/note, /notes)` (applied by reviewer). The contest_end was dated 1478 as 'Moscow annexes Great Perm'. The page's 1478 annexation is Novgorod's, not Great Perm's. Evidence: Great Perm page, sentence in full: 'Although Novgorod claimed the territory, it had little control and formally gave up its rights in 1471 before it was ultimately annexed by Moscow in 1478'. The subject is Novgorod, which the novgorod-republic and grand-principality-of-moscow dossiers annex in January 1478. The page dates the war 1472: 'In 1472, Ivan III dispatched Fyodor Paletsky for a campaign against Great Perm'; he 'founded the settlement of Pokcha, which became a stronghold for Moscow'. Fix: Year 1478 changed to 1472 (confidence 2 kept). The note is rewritten to end the fighting with Paletsky's campaign and to say why the year moved. The war outcome, the successor note and the notes field are corrected to match (done by the reviewer; validator OK).

Thin (for a gap-filler):
- `/identity/rulers`: The strip ends in 1481 (Matvey Mikhailovich 1481-1481) but the state runs to 1505; the page is silent on 1481-1505. Try: https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B0%D1%8F_%D0%9F%D0%B5%D1%80%D0%BC%D1%8C
- `/identity/capitals`: Coordinates for Cherdyn and Pokcha are not from a page (the author says so). Try: https://en.wikipedia.org/wiki/Cherdyn
- `/ledger/0`: The found event names counterpart 'nobody', but the predecessor is novgorod-republic, Cliopatria's Novgorod shape holds 221 of the 586 cells in 1400, and the page says the land was 'formally dependent on Novgorod until 1471, after which it was dependent on Moscow'. The vassal pairs (Novgorod 1451-1471, Moscow 1471-1505) belong in those two ledgers. Route this. Try: https://en.wikipedia.org/wiki/Great_Perm
- `/keyframe_review/0/correction`: Perm Krai runs about 200 km south of the page's southern limit (the Chusovaya-Kama confluence). The author acknowledges this; a minus of the southern districts would fit the page better. Try: https://en.wikipedia.org/wiki/Great_Perm

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Great_Perm: confirmed (Vasily II 'appointed Mikhail Yermolayevich as the prince of Great Perm in 1451'; lead 'Principality of Perm (1451-1505)')
- `/ledger/1` https://en.wikipedia.org/wiki/Great_Perm: confirmed ('In 1472, Ivan III dispatched Fyodor Paletsky for a campaign against Great Perm')
- `/ledger/2` https://en.wikipedia.org/wiki/Great_Perm: confirmed (infobox 'Pokcha (1472-1535)')
- `/ledger/3` https://en.wikipedia.org/wiki/Great_Perm: not on page as claimed: the 1478 annexation is Novgorod's; re-dated to 1472 (confidence 2, so a fix, not a fail)
- `/ledger/4` https://en.wikipedia.org/wiki/Great_Perm: confirmed ('finally incorporated into the Russian state in 1505 when Ivan III appointed a Russian prince, Vasily Kovrov, as the governor')

Area: No area on the page; the infobox's 1324-1708 is the wider Perm Land (the author notes it).

## Cross-dossier matrix

- cossack-hetmanate 1648 found (counterpart polish-lithuanian-commonwealth) -> polish-lithuanian-commonwealth 1648 contest_start: **mismatch**. PLC writes the rising against zaporozhian-cossacks and records no land leaving until 1654. Route to eu-15: the counterpart should be cossack-hetmanate (the author flags this).
- cossack-hetmanate 1649 gain (counterpart polish-lithuanian-commonwealth) -> polish-lithuanian-commonwealth 1649 vassal_start: **mismatch**. Same land (the Zboriv voivodeships), but PLC has a vassal_start of zaporozhian-cossacks where this dossier has a gain. PLC's 1651 narrowing to Kyiv voivodeship has no counterpart here (the author keeps the Zboriv extent from the infobox). Route to eu-15.
- polish-lithuanian-commonwealth 1654 loss (counterpart zaporozhian-cossacks) -> cossack-hetmanate None None: **mismatch**. PLC loses the left bank to zaporozhian-cossacks in January 1654. This dossier already holds that land from 1649 and has no 1654 event. Route to eu-15 to retarget the counterpart to cossack-hetmanate (or tsardom-of-russia).
- tsardom-of-russia 1654 vassal_start (counterpart cossack-hetmanate) -> tsardom-of-russia None vassal_end: **missing**. No vassal_end in tsardom-of-russia (ends 1721) or russian-empire. It needs 1764, or the 1721 hand-over. Route to the Tsardom/Russian Empire owners.
- cossack-hetmanate 1667 loss (counterpart polish-lithuanian-commonwealth) -> polish-lithuanian-commonwealth None gain: **missing**. PLC's 1667 events are all against tsardom-of-russia; it records no gain of the right bank from this state. Route to eu-15.
- cossack-hetmanate 1668 gain (counterpart polish-lithuanian-commonwealth) -> polish-lithuanian-commonwealth None loss: **missing**. PLC has no 1668 loss: it keeps the right bank until the Ottoman cession of 1672. The page does not say the Commonwealth ceded it (confidence 2). Route to eu-15.
- cossack-hetmanate 1672 occupation_start (counterpart ottoman-empire) -> ottoman-empire 1672 gain: **mismatch**. ottoman-empire gains Podolia from polish-lithuanian-commonwealth, and PLC loses Braclaw, Podole and part of Kiev voivodeship to the Ottomans in October 1672. Neither treats the right bank as Hetmanate land. See the blocking fix on /ledger/11 and /ledger/13.
- cossack-hetmanate 1686 vassal_start (counterpart zaporozhian-cossacks) -> zaporozhian-cossacks None None: **missing**. The zaporozhian-cossacks ledger has no 1686 or 1709 event naming the hetman. Route to the eu-16 owner of zaporozhian-cossacks.
- cossack-hetmanate 1699 occupation_end (counterpart ottoman-empire) -> ottoman-empire 1699 loss: **mismatch**. ottoman-empire loses Podolia to polish-lithuanian-commonwealth (PLC gain 1699). See the blocking fix on /ledger/13.
- cossack-hetmanate 1709 vassal_end (counterpart zaporozhian-cossacks) -> zaporozhian-cossacks None None: **missing**. See the 1686 row.
- cossack-hetmanate 1764 dissolve (counterpart russian-empire) -> russian-empire None gain: **missing**. russian-empire has no 1764 event: no gain of the left bank and no vassal_end. Route to the Russian Empire owner.
- principality-of-murom 1127 found (counterpart principality-of-chernigov) -> principality-of-chernigov 1127 loss: **mismatch**. Chernigov loses Murom-Ryazan in 1127 to principality-of-ryazan, not to this state. Murom also overlaps Cliopatria's Ryazan row (37 of 80 cells). Route to eu-16-b/c.
- principality-of-murom 1392 dissolve (counterpart grand-principality-of-moscow) -> grand-principality-of-moscow 1392 gain: **missing**. Moscow's 1392 gain is of nizhny-novgorod only. Murom (page: 'the same patent') needs a gain of principality-of-murom. Route to the Moscow owner.
- tmutarakan 1054 found (counterpart rus) -> rus 1054 dissolve: **exception**. rus dissolves in 1054 without tmutarakan among its successors. principality-of-chernigov's 1054 gain names Tmutarakan in its note but does not draw it, so the land is consistent; add tmutarakan to the rus successors.
- tmutarakan 1094 dissolve (counterpart nobody) -> None None None: **exception**. Counterpart nobody (confidence-1 bridge).
- principality-of-yaroslavl 1218 found (counterpart principality-of-rostov-suzdal) -> principality-of-rostov-suzdal None split: **missing**. principality-of-rostov-suzdal (1054-1240) has no 1218 split or loss. Route to its eu-16 owner.
- principality-of-vladimir-suzdal 1389 loss (counterpart principality-of-yaroslavl) -> principality-of-yaroslavl None gain: **mismatch**. Vladimir-Suzdal 'loses' the Yaroslavl lands in 1389 (confidence 1, a carving device for the Cliopatria overlap). This dossier holds them from 1218 with no 1389 event; consistent in land, but the event type should be a note, not a loss. Route to eu-16-g.
- principality-of-yaroslavl 1463 dissolve (counterpart grand-principality-of-moscow) -> grand-principality-of-moscow 1463 gain: **matched**. Moscow's gain is of principality-of-yaroslavl ('Principality of Yaroslavl in 1463', Ivan III page). Its region is a 50 km disk; its separate 1463 gains from vladimir-suzdal (Rybinsk/Mologa) and novgorod-republic (Vologda side) cover the rest.
- principality-of-zvenyhorod 1084 found (counterpart principality-of-volhynia) -> principality-of-volhynia None split: **missing**. Volhynia has no 1084 event. principality-of-peremyshl splits off Terebovlia in 1084 but not Zvenyhorod, and Cliopatria's Peremyshl draws 32 of the 33 Zvenyhorod cells in 1100. Route to eu-16-d.
- principality-of-zvenyhorod 1141 dissolve (counterpart principality-of-halych) -> principality-of-halych 1145 gain: **mismatch**. Four years apart. Peremyshl and Terebovlia both merge 'with Zvenyhorod' in 1141; Halych's 1145 gain cites Ivan Berladnyk. Route to eu-16-d.
- principality-of-novgorod-seversk 1097 found (counterpart principality-of-chernigov) -> principality-of-chernigov None split: **missing**. Chernigov has no 1097 event (personal union per the infobox, so the land is shared). Route to eu-16-b.
- principality-of-novgorod-seversk 1503 dissolve (counterpart grand-principality-of-moscow) -> grand-principality-of-moscow 1503 vassal_start: **mismatch**. Moscow keeps Novgorod-Seversk as a vassal 1503-1522 (vassal_start at confidence 1; vassal_end and gain in 1522 at confidence 3). This dossier ends in 1503 (infobox). One side must give way.
- great-perm 1451 found (counterpart nobody) -> novgorod-republic None vassal_start: **mismatch**. The predecessor is novgorod-republic and the page says 'formally dependent on Novgorod until 1471'. Novgorod has no 1451 or 1471 event for Great Perm, though its Cliopatria shape covers 221 of 586 cells in 1400. Route to eu-16-b.
- great-perm 1505 dissolve (counterpart grand-principality-of-moscow) -> grand-principality-of-moscow None gain: **missing**. Moscow has no 1505 gain of great-perm, and no 1471/1472 vassal_start for it. Route to the Moscow owner.

## Problems

- WebFetch answers paraphrase in places; quotes in this report are the tool's verbatim extracts.
- Three dossiers edited in place by the reviewer (cossack-hetmanate /identity/rulers/9; tmutarakan /ledger/0 confidence; great-perm /ledger/3 year plus three matching sentences); all re-validated OK and read back after writing.
- The cossack-hetmanate cross-dossier conflicts with polish-lithuanian-commonwealth (eu-15: zaporozhian-cossacks named for the Hetmanate 1648-1654; the right bank 1667-1672) need an orchestrator decision on which slug carries the 1649-1654 autonomy.
- No Cliopatria rows in this batch, so the area checks compare the infobox against the resolved region; only the Hetmanate page gives an area.
