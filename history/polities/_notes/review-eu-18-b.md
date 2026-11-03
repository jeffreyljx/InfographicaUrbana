# Review of batch eu-18-b (Balkans, part b)

Reviewer, 2026-10-31. Validator: all five dossiers 0 errors, 0 warnings (--resolve). Spot checks weighted to confidence-3 events and the largest land moves; no fabricated or mis-dated event found. None of the five main articles has an infobox area.

Reviewer edits applied in place (re-validated): principality-of-serbia and grand-principality-of-serbia capital point moved to the Stari Ras page's coordinates (20.4156E 43.1283N; the gazetteer's 20.6E lay outside every shape); kingdom-of-croatia /ledger/9 and /ledger/11 confidence 3 -> 2 (regions broader than the pages').

## principality-of-serbia: fix

Findings:
- `/identity/capitals/0` (applied by reviewer): The capital point (gazetteer Stari Ras, 20.6E 43.12N) lay east of every Cliopatria shape of the state (max east 20.5029E in shapes.csv). Evidence: Stari Ras page: coordinates 43°7′42″N 20°24′56″E, 'some 10-11 kilometers west of modern-day city of Novi Pazar'; the gazetteer point is about 15 km east of the site. Fix: lon 20.4156, lat 43.1283, with a sentence in the capital note naming the page.

Gaps (thin, within the page budget):
- `/ledger/1`: 850 gain of Bosnia and Hum is confidence 1 (Vlastimir page gives no year; year is Cliopatria's). Try: https://en.wikipedia.org/wiki/Vlastimir_of_Serbia
- `/ledger/3`: 922 gain (+24 thousand km2, Bosna valley and Narentines) is confidence 1; the main page puts Petar Gojnikovic's expansion in 892-917 without a year; his own page failed to load under three titles. Try: https://en.wikipedia.org/wiki/Narentines
- `/ledger/8`: 960 end of the overlordship of the Dalmatian duchies is confidence 1. Try: https://en.wikipedia.org/wiki/%C4%8Caslav_of_Serbia
- `/identity/rulers`: Rulers gap 924-933 is the Bulgarian interval (fine); rulers before 830 (Viseslav, Radoslav, Prosigoj) undated. Try: https://en.wikipedia.org/wiki/Principality_of_Serbia_(early_medieval)

Spot checks: /ledger/2 confirmed; /ledger/5 confirmed (main page: 'The principality was annexed in 924 by Simeon I'; the cited Simeon page was not opened); /ledger/6 confirmed; /ledger/7 confirmed

Area: No infobox area on the page (author says so in /keyframe_review/0). Cliopatria max 61327.9 km2.

## kingdom-of-croatia: fail

Findings:
- `/ledger/7/region, /keyframe_review/9/correction, /ledger/9/region` (for the author): The 1018 loss to Venice (and the 1018-1059 corrected keyframe) removes a 30 km circle round Zadar labelled 'Zadar, Biograd and Nin', which takes the royal capital Biograd (25 km from Zadar; identity.capitals Biograd 969-1074) and Nin (15 km) out of the kingdom for 1018-1059. Evidence: Main page: in 1000 Orseolo took 'Zadar, Trogir, and Split' and Kresimir III 'tried to restore the Dalmatian cities and had some success until 1018'; no page names Biograd or Nin for 1018. Biograd stays the capital to 1074 (Peter Kresimir IV page: in 1075 he gave up 'both capitals'). Distances computed from the gazetteer's Zadar (15.2623E 44.1201N) and the dossier's Biograd and Nin points. Fix: For 1018 (ledger/7 and keyframe_review/9) and 1060 (ledger/9) use Zadar alone (place Zadar, km about 10, text 'Zadar') plus Split and Trogir; keep the 30 km union only for the 1074 Norman ransom (ledger/13, keyframe_review/11) and the 1075-1085 Venetian events, where the page says both capitals were given up.
- `/ledger/11/region` (for the author): The 1069 gain from Byzantium uses the gazetteer region 'Dalmatia' (the four admin-1 units Zadarska, Sibensko-Kninska, Splitsko-Dalmatinska, Dubrovacko-Neretvanska), which adds Ragusa, Peljesac and the Neretva delta to the kingdom from 1069 to 1102, outside every keyframe (the 1018 shape stops at 43.02N). Evidence: Peter Kresimir IV page: 'he had the Byzantine Empire recognize him as supreme ruler of the parts of Dalmatia' it had held: the theme's cities and islands, not the Croatian hinterland or Ragusa. Fix: Region: the Byzantine Dalmatian towns and islands (Zadar, Split, Trogir, and the Kvarner islands Krk, Rab, Cres-Osor as places/circles), text 'the parts of Dalmatia Byzantium had controlled'.
- `/ledger/9/confidence` (applied by reviewer): Confidence 3 with a region the page does not name ('Zadar, Biograd and Nin'; the page says 'the Dalmatian city-states'). Evidence: Kingdom of Croatia (925-1102) page: 'only from 1060 when king Peter Kresimir IV gained control over the Dalmatian city-states'. Fix: Confidence 2.
- `/ledger/11/confidence` (applied by reviewer): Confidence 3 with a region broader than the page's ('Dalmatia' for 'the parts of Dalmatia' Byzantium held). Evidence: Peter Kresimir IV page, as above. Fix: Confidence 2.

Gaps (thin, within the page budget):
- `/ledger/4, /keyframe_review/6`: The 980 jump from 55.0 to 90.3 thousand km2 (Bosnia filled in) is a confidence-1 event with counterpart 'nobody'; no page dates or explains it; shapes 936-1000 'unverified: page budget'. Try: https://en.wikipedia.org/wiki/Stephen_Dr%C5%BEislav_of_Croatia
- `/keyframe_review/12`: The 1085 shape drops 20 thousand km2 in the east; the only 1085 event is the transfer of the Dalmatian cities to Venice. Try: https://en.wikipedia.org/wiki/Demetrius_Zvonimir_of_Croatia
- `/ledger/12`: 1074 recovery of Kvarner and eastern Istria by Zvonimir is confidence 1 (page: 'eventually liberated', no year). Try: https://en.wikipedia.org/wiki/Demetrius_Zvonimir_of_Croatia
- `/identity/rulers, /identity/capitals`: Rulers 928-949 and 997-1000 missing; capitals 928-948 and 998-1057 not on the pages (author flagged). Try: https://en.wikipedia.org/wiki/Trpimirovi%C4%87_dynasty

Spot checks: /ledger/7 confirmed (year and Venice; region overstated, see fixes); /ledger/8 confirmed; /ledger/9 confirmed (year; region overstated); /ledger/10 confirmed; /ledger/11 confirmed (year; region overstated); /ledger/16 confirmed ('in 1085, the Byzantines transferred their rights in Dalmatia to Venice'); /ledger/17 confirmed; /ledger/19 confirmed

Area: The page's infobox has no area. Cliopatria max 92789.2 km2.

## great-principality-of-duklja: pass

Gaps (thin, within the page budget):
- `/ledger/4`: 1066 gain of Rascia: page says only 'in the 1060s' (confidence 1 honest). Try: https://en.wikipedia.org/wiki/Mihailo_I_of_Duklja
- `/ledger/6`: 1085 gain of Bosnia (+22 thousand km2): no year on any page; Chronicle of Dioclea disputed. Try: https://en.wikipedia.org/wiki/Constantine_Bodin
- `/ledger/8`: 1091 loss of Zahumlje and Bosnia to 'nobody' is confidence 1 ('probably broke free'); they went to local princes, not stateless land. Try: https://en.wikipedia.org/wiki/Zahumlje
- `/keyframe_review/7`: 1139-1185 outline kept whole although 'By 1166, much of Duklja was occupied by Rascia'; the lands are not named. Try: https://en.wikipedia.org/wiki/Radoslav_of_Duklja

Spot checks: /ledger/3 confirmed ('In 1042, another Byzantine attack was defeated'; cited Vojislav page not opened); /ledger/4 confirmed ('Michael conquered Rascia from the Byzantines in the 1060s'); /ledger/5 confirmed (infobox 'Elevated to the status of kingdom: 1077'); /ledger/11 confirmed ('Stefan Nemanja annexed Duklja in its entirety after defeating the last Doclean prince', 1186; infobox 'Conquered by Grand Principality of Serbia: 1186/9')

Area: The page's infobox has no area. Cliopatria max 49994.3 km2.

## grand-principality-of-serbia: fail

Findings:
- `/identity/end, /ledger/5, /ledger/6` (for the author): The dossier ends in 1168 with a confidence-1 'dissolve' only because Cliopatria's row ends; the state continues to 1217, nothing draws it in 1169-1187 (no Cliopatria shape in any row), and the Duklja dossier's 1186 contest_end and loss name grand-principality-of-serbia as the counterpart, 18 years after this dossier ends its side of the contest (1168, confidence 1). Evidence: Grand Principality page infobox 'Established: 1091', 'Disestablished: 1217'; Duklja page infobox 'Conquered by Grand Principality of Serbia: 1186/9'; great-principality-of-duklja /ledger/10-11 (1186, counterpart grand-principality-of-serbia). The kingdom-of-serbia dossier that is meant to take over (Cliopatria row from 1188) is not written. Fix: Extend the dossier to 1187: new keyframe 1169-1187 (the 1152 shape, text from the Nemanja page: Kotor 1166/67, Skadar c. 1184, part of Zeta and the Neretva region), contest with great-principality-of-duklja kept open to 1186 and a 1186 gain of the Doclean remainder (counterpart great-principality-of-duklja), dissolve at 1187 written as a hand-over to kingdom-of-serbia (whose Cliopatria row starts 1188); or run to 1217 if the eu-18 kingdom-of-serbia author agrees. If the orchestrator instead assigns 1169-1217 to kingdom-of-serbia, Duklja's /ledger/9-11 must be rewritten with a hand-over (contest_end 1168 against this slug, contest_start 1169 and the 1186 events against kingdom-of-serbia).
- `/identity/capitals/0` (applied by reviewer): The capital point (gazetteer Stari Ras, 20.6E) lay east of the state's shapes (max east 20.5795E). Evidence: Stari Ras page: 43°7′42″N 20°24′56″E. Fix: lon 20.4156, lat 43.1283.
- `/identity/rulers` (for the author): Rulers are not contiguous: nothing between Vukan (to 1112) and Tihomir (1166), and Tihomir 1166-1167 overlaps Nemanja from 1166. Evidence: The Grand Principality page lists the grand princes of 1112-1166 (Uros I, Uros II, Belos, Desa). Fix: Add the rulers of 1112-1166 from the Grand Principality page, and make Tihomir end where Nemanja begins.

Gaps (thin, within the page budget):
- `/ledger/1`: 1150 gain of Zahumlje and Travunija from 'nobody' (Desa as dux in a charter of 1150; the page does not say how he came to hold them). Try: https://en.wikipedia.org/wiki/Desa,_Grand_Prince_of_Serbia
- `/ledger/4`: Kotor counterpart 'Kotor (city commune)'; the Nemanja page later calls it 'Byzantine Kotor' (counterpart may be byzantine-empire). Try: https://en.wikipedia.org/wiki/Kotor

Spot checks: /ledger/0 confirmed ('In 1091 or 1092, Vukan became independent'); /ledger/1 confirmed ('In 1150, Desa was mentioned in a charter as dux of Duklja, Travunija and Zahumlje'); /ledger/3 confirmed ('Stefan Nemanja (r. 1166-1196)'); the Nemanja page dates the overthrow of Tihomir to 1168; /ledger/4 confirmed ('In 1166 or 1167, Nemanja first expanded his territories and conquered Kotor')

Area: No infobox area (author says so in /keyframe_review/0). Cliopatria max 28937.6 km2.

## banate-of-bosnia: fail

Findings:
- `/wars, /ledger (1363)` (for the author): The Hungarian invasion of Bosnia in 1363 is missing: no war, no contest events, no mention anywhere in the dossier, although both pages the author used describe it and the kingdom-of-hungary dossier has contest_start 1363 (confidence 3) and contest_end 1367 with counterpart banate-of-bosnia. Evidence: Banate of Bosnia page: 'In 1363, a conflict broke out between the two men'; 'An army led by Louis himself attacked Donji Kraji'; a month later a Hungarian army under Palatine Nicholas Kont 'struck Usora'; Srebrenik and Soko Grad held. Tvrtko I page: Vlatko Vukoslavic defected and gave up Kljuc; 'The successful defense of Srebrenik marked Tvrtko's first victory against Hungary.' Fix: Add a war 'Hungarian invasion of Bosnia (Louis I)' 1363, belligerents kingdom-of-hungary and banate-of-bosnia, zones Donji Kraji (Kljuc, Soko Grad) and Usora (Srebrenik); add contest_start 1363 and contest_end (1363, or 1366/1367 to meet Hungary's end) with counterpart kingdom-of-hungary over those zones.
- `/ledger/11/region, /keyframe_review/12` (for the author): The 1366 gain from Hungary re-adds Usora and Soli, which the ledger never lost after 1324, and the 1357-1365 keyframe removes Donji Kraji although the 1363 campaign has Bosnian magnates holding Kljuc and Soko Grad there; the 1366 recovery was from the rebel magnates and Vuk, with probable Hungarian help. Evidence: Tvrtko I page: in February 1366 'the magnates revolted against Tvrtko and dethroned him'; he returned in March and 'reestablished control over a part of the country by the end of the month', including Donji Kraji, Rama, Hum and Usora. Fix: Drop Usora and Soli from /ledger/11 (or add their 1366 loss to the rebels); say in /keyframe_review/12 how long Donji Kraji stayed Hungarian (the 1363 campaign suggests it was back under Bosnian lords before 1363) and adjust the keyframe span.

Gaps (thin, within the page budget):
- `/ledger/3`: 1241 loss of the west and north is confidence 1; kingdom-of-hungary dates its gain of northern Usora and Soli to 1253 (confidence 2). Try: https://en.wikipedia.org/wiki/Prijezda_I,_Ban_of_Bosnia
- `/ledger/7`: c. 1326 gain of Zavrsje (Livno, Duvno, Glamoc) from 'nobody'; the page names no holder (Croatian lords under the Hungarian crown); kingdom-of-hungary records the loss in 1333 (confidence 1). Try: https://en.wikipedia.org/wiki/Zavr%C5%A1je
- `/ledger/13`: Early-1377 gain of Trebinje, Konavli and Dracevica has counterpart 'nobody' although the land had a holder (page: Tvrtko 'plotted with the Travunians'; Djuradj I Balsic had seized coastal zupas); 'nobody' means stateless. Try: https://en.wikipedia.org/wiki/%C4%90ura%C4%91_I_Bal%C5%A1i%C4%87
- `/identity/start`: The Banate page's infobox has 'First known Ban (Ban Boric): 1154'; the dossier starts at Kulin's independence in 1180 (Bosnia then a Hungarian, from 1167 Byzantine, dependency). Defensible; say so in notes. Try: https://en.wikipedia.org/wiki/Ban_Bori%C4%87

Spot checks: /ledger/5 confirmed (Skradin 1322); /ledger/6 confirmed ('fully incorporated' 1324, after Milutin's death in 1321; formerly held by Dragutin and Vladislav II); /ledger/8 confirmed ('By 1326 ... conquered Zahumlje (or Hum)', from the Serbian vassal Branivojevic family); /ledger/9 confirmed (1329 campaign; 'the Ban managed to add Nevesinje and Zagorje'); /ledger/10 confirmed (1357 dowry); /ledger/12 confirmed (autumn 1373: upper Podrinje, Gacko, part of Polimlje with Mileseva); /ledger/13 confirmed for year and land ('In early 1377'); holder not named; /ledger/14 confirmed (coronation fall 1377, probably 26 October)

Area: No infobox area (author says so in /keyframe_review/15). Cliopatria max 48972.9 km2.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| principality-of-serbia 850 gain (nobody) | - | exception | counterpart nobody |
| principality-of-serbia 917 contest_start (first-bulgarian-empire) | - | exception | first-bulgarian-empire (eu-18, another part) not written yet |
| principality-of-serbia 922 gain (nobody) | - | exception | counterpart nobody; confidence 1 |
| principality-of-serbia 924 loss (first-bulgarian-empire) | - | exception | first-bulgarian-empire not written yet; it must gain Serbia 924 and lose it 933 |
| principality-of-serbia 933 gain (first-bulgarian-empire) | - | exception | first-bulgarian-empire not written yet |
| principality-of-serbia 933 vassal_start (Dalmatian duchies (Zahumlje, Travunia, Pagania)) | - | exception | overlord side recorded here; duchies listed in counterparts_needing_dossiers |
| principality-of-serbia 960 dissolve (successor byzantine-empire) | byzantine-empire - gain | missing | byzantine-empire has no gain of Serbia / Catepanate of Ras (page: c. 969-971, Catepanate c. 971-976); route to the byzantine-empire author |
| kingdom-of-croatia 925 found (duchy-of-croatia) | - | exception | duchy-of-croatia (eu-18, another part) not written yet |
| kingdom-of-croatia 925 gain (nobody) | - | exception | former Pannonian duchy (Sisak) as nobody; confidence 2 |
| kingdom-of-croatia 926 contest_start (first-bulgarian-empire) | - | exception | first-bulgarian-empire not written yet |
| kingdom-of-croatia 980 gain (nobody) | - | exception | confidence 1, Cliopatria-driven; Bosnia is hardly stateless land |
| kingdom-of-croatia 1000 contest_start (republic-of-venice) | republic-of-venice 1000 gain | mismatch | Venice records a gain from Croatia in 1000 (c3, Istrian and Dalmatian cities); Croatia records a contest 1000-1018 and the loss only in 1018 |
| kingdom-of-croatia 1018 loss (republic-of-venice) | republic-of-venice - gain | mismatch | no Venetian event in 1018; the cities were Byzantine-Dalmatian, Venice took them in 1000 (Venice /ledger/3); one side must move |
| byzantine-empire 1018 vassal_start (kingdom-of-croatia) | byzantine-empire 1025 vassal_end | matched | overlord side: byzantine-empire /ledger/94 and /ledger/97 (1018-1025); Croatia rightly records nothing |
| kingdom-of-croatia 1050 vassal_start (Narentine duchy (Pagania)) | - | exception | listed in counterparts_needing_dossiers |
| kingdom-of-croatia 1060 gain (Dalmatian city-states) | - | exception | listed; note that by Croatia's own ledger the cities were Venetian from 1018 |
| kingdom-of-croatia 1067 loss (Margraviate of Carniola (Ulric I)) | - | exception | listed (eu-08); holy-roman-empire has no 1067 event |
| kingdom-of-croatia 1069 gain (byzantine-empire) | byzantine-empire - loss | missing | byzantine-empire has no 1069 loss of Dalmatian towns to Croatia; route to the byzantine-empire author |
| kingdom-of-croatia 1074 gain (Margraviate of Carniola (Ulric I)) | - | exception | listed; confidence 1 |
| kingdom-of-croatia 1074 loss (Normans of Apulia (Count Amico of Giovinazzo)) | norman-italy - gain | missing | author proposes a new slug norman-apulia, but norman-italy (1030-1130) exists and has no Dalmatian events; counterpart should probably be norman-italy, which then needs a 1074 gain and 1075 loss |
| kingdom-of-croatia 1075 contest_start (republic-of-venice) | republic-of-venice - contest_start | missing | republic-of-venice has no event 1075-1085 for Dalmatia |
| kingdom-of-croatia 1085 loss (republic-of-venice) | republic-of-venice - gain | missing | Venice should gain the Byzantine rights in Dalmatia in 1085 (Croatia page) |
| kingdom-of-croatia 1091 loss (kingdom-of-hungary) | kingdom-of-hungary 1091 gain | matched | Slavonia, both confidence 3 |
| kingdom-of-croatia 1091 contest_start (kingdom-of-hungary) | kingdom-of-hungary 1091 contest_start | matched |  |
| kingdom-of-croatia 1097 contest_end (kingdom-of-hungary) | kingdom-of-hungary 1102 contest_end | mismatch | Croatia ends the contest at Gvozd 1097; Hungary at the 1102 coronation |
| kingdom-of-croatia 1102 dissolve (successor croatia-in-union-with-hungary) | croatia-in-union-with-hungary 1102 found | matched | kingdom-of-hungary /ledger/12 also records a 1102 gain of the same land from kingdom-of-croatia (double claim, for the Hungary author) |
| kingdom-of-croatia 1102 vassal_end (Narentine duchy (Pagania)) | - | exception |  |
| great-principality-of-duklja 1034 found (byzantine-empire) | byzantine-empire 1056 loss | mismatch | Duklja found 1034 and gain 1040 (Vojislav, pages); byzantine-empire loses Duklja only in 1056 (c1, Cliopatria year) and has no war with Vojislav (1034-1042) |
| great-principality-of-duklja 1040 gain (byzantine-empire) | byzantine-empire 1056 loss | mismatch | as above; 16 years apart |
| great-principality-of-duklja 1066 gain (byzantine-empire) | byzantine-empire 1066 loss | matched | Rascia; both confidence 1 |
| great-principality-of-duklja 1085 gain (nobody) | - | exception | Bosnia; confidence 1 |
| great-principality-of-duklja 1091 loss (grand-principality-of-serbia) | grand-principality-of-serbia 1091 found | matched | Rascia breaks away under Vukan |
| great-principality-of-duklja 1091 loss (nobody) | - | exception | Zahumlje and Bosnia break away; confidence 1 |
| great-principality-of-duklja 1150 contest_start (grand-principality-of-serbia) | grand-principality-of-serbia 1150 contest_start | matched |  |
| great-principality-of-duklja 1186 contest_end (grand-principality-of-serbia) | grand-principality-of-serbia 1168 contest_end | mismatch | grand-principality-of-serbia closes its side in 1168 (c1, dossier boundary); Duklja closes in 1186 |
| great-principality-of-duklja 1186 loss (grand-principality-of-serbia) | grand-principality-of-serbia - gain | mismatch | grand-principality-of-serbia ends in 1168, so the 1186 loss has no living counterpart; see the GP fix |
| grand-principality-of-serbia 1150 gain (nobody) | - | exception | Zahumlje and Travunija; the same lands Duklja lost to nobody in 1091 |
| grand-principality-of-serbia 1167 gain (Kotor (city commune)) | - | exception | name counterpart; the Nemanja page calls Kotor Byzantine |
| byzantine-empire 1128 vassal_start (grand-principality-of-serbia) | byzantine-empire 1168 vassal_end | matched | overlord side only (byzantine-empire /ledger/126, /ledger/132) |
| grand-principality-of-serbia 1168 dissolve (successor kingdom-of-serbia) | - | exception | kingdom-of-serbia (eu-18, another part) not written yet; no Cliopatria shape 1169-1187 |
| banate-of-bosnia 1180 found (byzantine-empire) | byzantine-empire 1188 loss | mismatch | Bosnia independent from Byzantium in 1180 (Kulin); byzantine-empire loses Sirmium, Bosnia and Dalmatia to kingdom-of-hungary in 1188 (c1) |
| banate-of-bosnia 1235 contest_start (kingdom-of-hungary) | kingdom-of-hungary 1235 contest_start | matched |  |
| banate-of-bosnia 1241 contest_end (kingdom-of-hungary) | kingdom-of-hungary 1241 contest_end | matched |  |
| banate-of-bosnia 1241 loss (kingdom-of-hungary) | kingdom-of-hungary 1253 gain | mismatch | Bosnia c1 in 1241 (Cliopatria); Hungary c2 in 1253 (northern Usora and Soli under Bela IV) |
| banate-of-bosnia 1299 contest_start (Subic of Bribir) | - | exception | listed in counterparts_needing_dossiers |
| banate-of-bosnia 1324 gain (kingdom-of-serbia) | kingdom-of-hungary 1324 loss | mismatch | Usora and Soli: Bosnia names kingdom-of-serbia (Stephen II page: after Milutin's death), kingdom-of-hungary /ledger/48 records the loss to Bosnia in 1324 (c3), kingdom-of-syrmia /ledger/7 in 1325 (c2); three dossiers, three givers |
| banate-of-bosnia 1324 gain (kingdom-of-serbia) | kingdom-of-syrmia 1325 loss | mismatch | as above |
| banate-of-bosnia 1326 gain (nobody) | kingdom-of-hungary 1333 loss | mismatch | Zavrsje: Bosnia says nobody (c2, c. 1326), Hungary records a loss to Bosnia in 1333 (c1) |
| banate-of-bosnia 1326 gain (kingdom-of-serbia) | - | exception | kingdom-of-serbia not written yet (Hum, from the Branivojevici) |
| banate-of-bosnia 1329 gain (kingdom-of-serbia) | - | exception | kingdom-of-serbia not written yet (Nevesinje, Zagorje) |
| banate-of-bosnia 1357 loss (kingdom-of-hungary) | kingdom-of-hungary - gain | missing | kingdom-of-hungary has no 1357 gain of Donji Kraji and western Hum (its 1358 events are the Treaty of Zadar with Venice) |
| kingdom-of-hungary 1363 contest_start (banate-of-bosnia) | banate-of-bosnia - contest_start | missing | Bosnia has no 1363 war or contest; see the Bosnia fix |
| banate-of-bosnia 1366 gain (kingdom-of-hungary) | kingdom-of-hungary 1367 loss | matched | one year apart (Tvrtko page implies March 1366; Banate page ambiguous) |
| kingdom-of-hungary 1367 contest_end (banate-of-bosnia) | banate-of-bosnia - contest_end | missing | paired with the missing 1363 contest |
| banate-of-bosnia 1373 gain (Nicholas Altomanovic) | - | exception | listed in counterparts_needing_dossiers |
| banate-of-bosnia 1377 gain (nobody) | - | exception | nobody, but the land had a holder (Travunian nobles / Balsici); see thin |
| banate-of-bosnia 1377 dissolve (successor kingdom-of-bosnia) | - | exception | kingdom-of-bosnia (eu-18, another part) not written yet |

## Problems and routing

- Gazetteer: 'Stari Ras' (places.jsonl, source 'knowledge') is at 20.6E 43.12N; the Stari Ras page gives 43°7′42″N 20°24′56″E (20.4156E 43.1283N), about 15 km west. The two Serbian capitals were corrected in the dossiers; the gazetteer row should be fixed by its owner.
- None of the five main articles has an infobox area; area sanity could not be checked against a page figure.
- Pages not opened (budget): Simeon_I_of_Bulgaria, Stefan_Vojislav, Mihailo_I_of_Duklja, Matej_Ninoslav, Ban_Kulin, Tomislav_of_Croatia, Coloman,_King_of_Hungary; the spot-checked claims they carry were confirmed on the main articles instead.
- Structural decision for the orchestrator: grand-principality-of-serbia ends at Cliopatria's 1168 while the state runs to 1217 and Cliopatria's Kingdom of Serbia row starts 1188; either the GP dossier extends (recommended, at least to 1187) or the eu-18 kingdom-of-serbia author starts at 1169 and Duklja's 1186 events are re-pointed. Tell the kingdom-of-serbia author either way.
- Routing for other authors: byzantine-empire lacks Serbia 960/971, Duklja 1034-1042 and Croatia 1069; republic-of-venice lacks Croatia 1018, 1075-1085; kingdom-of-hungary lacks Bosnia 1357 and double-claims Croatia 1102; Usora and Soli 1324-1325 are claimed from three givers (Bosnia, Hungary, Syrmia).
