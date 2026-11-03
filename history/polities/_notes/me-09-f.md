# Notes for batch me-09-f (Phase B, written 2026-10-25)

Six dossiers: beylik-of-menteshe, beylik-of-sinop, eshrefids, germiyanids, kastamonu, beylik-of-saruhan. All validate with 0 errors; the only `--resolve` warnings are the place name Alasehir (germiyanids) and two deliberate empty-region corrections (beylik-of-sinop_1326, germiyanids_1431). Every page was read through WebFetch on 2026-10-25; the Anatolian beyliks table was read as a paraphrase by the fetch tool (the tool said it restated the rows), so its dates are cited as "table rows".

Convention used in `keyframe_review`: an existing Cliopatria shape whose years must change keeps its shape_id, gives the shape unchanged (or corrected) in `correction`, and carries `from`/`to` (the validator accepts them) plus a note saying "years only". New keyframes use `<slug>_<from year>` ids. A "wrong" verdict whose shape should not exist at all uses {"minus": [S, S]} (the empty region), which resolves to no cells by design.

## Rows and Wikidata ids

- beylik-of-sinop (Q2096678, shared with beylik-of-isfendiyar): on the pages opened it is a different state from the Candars: the Pervaneid emirate of Sinop (descendants of Mu'in al-Din Suleyman), table dates 1277-1322, annexed by Suleyman I of the Candar dynasty (counterpart and successor beylik-of-isfendiyar after the review fix). Do not merge with beylik-of-isfendiyar. The shared id is the Candar dynasty article that Cliopatria attached to both rows.
- kastamonu (Q155915, the city): after the review fix this dossier is the Chobanid (Cobanogullari) beylik at Kastamonu only, 1211-1309. The Candar state that conquered Kastamonu in 1309 (seat 1309-1398) is Cliopatria's Beylik of Isfendiyar row (same Wikipedia article, Eflani/Safranbolu), so from 1309 the Candar realm is one state in the beylik-of-isfendiyar dossier, which should list 'Kastamonu' in cliopatria_names.
- beylik-of-saruhan (Q1968654, shared with `han`): `han` is the Warring States state of Han (-404..-203). Different states; the id is Cliopatria's error. Kept as given in `wikidata`; the link agent should check it.

## beylik-of-menteshe (Menteshe, Anatolian beyliks, Battle of Ankara)

- Start 1261 (ruler table and beyliks table; the text says 1260/1290); end 1426 (text; the tables say 1424). Cliopatria begins 1305 and ends 1414.
- Cliopatria keeps one 5,886 km2 shape to 1406 and ignores: the 1390 submission to Bayezid I, Ottoman rule 1391-1402, the 1402 restoration under Ilyas Bey (Timur), the 1414 Ottoman overlordship and the 1426 incorporation. The dossier codes them as loss 1390, gain 1402, loss and dissolve 1426, and new keyframes for 1261-1304 and 1402-1406.
- The page has no area. Its undated list of "important centers" (Elmali, Finike, Kas, Fethiye, Mugla, Cameli, Acipayam, Tavas, Bozdogan, Cine) reaches far beyond the Milas-Mugla shape: the maximum extent is not settled.
- For the Ottoman dossier (me-10): gain 1390 and 1426, loss 1402, vassal_start 1414 / vassal_end 1426 with counterpart beylik-of-menteshe. For the Timurid dossier: the 1402 restoration.
- Not coded: the 1300 conquest of part of Rhodes and the 1311 attack (no holder is named; listed as a war with empty zones).

## beylik-of-sinop (Candar dynasty, Anatolian beyliks, Sinop)

- End 1322 rests on one table row ("Pervaneid ... Sinop ... 1277-1322"); the Candar page annexes Sinop without a year; Cliopatria ends the row in 1332 and draws the land inside Kastamonu from 1333. The 1326 shape is marked wrong. The Sinop page has the bishop leave in 1315 "because of the Isfendiyars", so Candar pressure is older.
- Start 1277 (table; the Sinop page says independent emirates began after 1265).
- No page on the Pervaneid line could be opened (three title guesses failed); a gap-filler should find it.

## eshrefids (Eshrefids, Timurtash, Karamanids, Anatolian beyliks)

- Start 1280 (infobox); end 9 October 1326 (Timurtash page: Suleyman II drowned in Lake Beysehir), not 1325 as in Cliopatria. The Eshrefids page contradicts itself on who was executed (Mubariz al-Din Mehmed in the lead; Suleyman II in the ruler table and on the Timurtash page).
- Successor coded as ilkhanate (Timurtash was the Ilkhanid viceroy 1314-1327); the infobox's "Chobanids" is the viceroy's family, not Cliopatria's Chobanids (Tabriz, 1344-1362). Land after December 1327 (Karamanids, Eretna) is not on any page opened.
- The 1305 shape reaches Konya's western plain; the Karamanids page dates "Conquest of Konya: 1308". Unchecked.

## germiyanids (Germiyanids, Kutahya, Hamidids, Anatolian beyliks, Battle of Ankara)

- Cliopatria's polygon from 1344 to 1414 is a composite: 47.5-52.9 thousand km2 in western Anatolia plus an eastern lobe east of 38 E (in 1344: Diyarbakir, Mardin, Sanliurfa, Van, Bitlis, Hakkari, Hasakah, Raqqa, Dihok; 165 thousand km2 in 1344, 67 thousand in 1375, 38 thousand in 1407) that overlaps no other Cliopatria shape and no Germiyan source supports. Keyframes cut it with a western polygon (27-35 E, 35-43 N). Whose land the lobe is (Artuqid or Kurdish emirates, which Cliopatria lacks, are the likeliest) is not settled: for the me-09-x additions batch.
- The 1431-1439 shape (Ankara-Cankiri, 5,350 km2) outlives the dynasty by ten years; marked wrong. End is January 1429 (Yakub II's will, annexation by Murad II); the Kutahya article says 1428 for the Ottoman conquest of the city.
- Dated by the page: 1304 (Philadelphia lost to the Catalans), 1381 (dowry: Kutahya, Simav, Egrigoz, Tavsanli; court to Kula), 1390 (whole realm Ottoman), 1402 (Timur restores), Sept 1410 war with Karaman, 1411 (Kutahya lost), 1414 (Mehmed Celebi reinstates Yakub), 1429. New keyframes: 1300-1304, 1381-1389, 1402-1406, 1411-1413.
- Confidence-1 entries (page silent): 1333 and 1344 gains from beylik-of-hamid (Egirdir-Isparta, then Denizli and Afyon) and the 1363 Ankara reach. The page puts "Denizli and Karahisar" in Yakub I's domain (to 1340) without a date, so Cliopatria's 1344 may be late.
- Not settled: the Catalan interlude at Simav and Kula (undated, Mehmed retook Kula from them in 1340-1361); who held Kutahya in 1412-1413; whether Germiyan was an Ilkhanate vassal in the 1330s; the Ankara reach (undated).
- Mirrors wanted: ottoman-empire (gains 1381, 1390, 1429; loss 1402), beylik-of-karaman (gain Kutahya 1411, loss 1414), beylik-of-hamid (losses 1333, 1344), timurid-empire (1402 restoration).

## kastamonu (Anatolian beyliks, Candar dynasty, Kastamonu Province, Kastamonu city, Chobanids; rewritten after the review)

- The state is the Chobanid beylik at Kastamonu: 'Chobanid Beylik, Founder: Husam al-Din Choban | Kastamonu (preceding the Candars) | 1211-1309' (beyliks table). `found` 1211 (confidence 2, counterpart sultanate-of-rum), `loss` and `dissolve` 1309 (counterpart beylik-of-isfendiyar, confidence 2). Keyframes: kastamonu_1211 (new, 1211-1304, the 1305 shape projected back, approximate), kastamonu_1305 adjusted to 1305-1308; kastamonu_1314, kastamonu_1323 (new pointer) and kastamonu_1333 are wrong here with the note 'Candar realm 1309-1343: reviewed in beylik-of-isfendiyar'. No rulers (the Chobanid rulers are on no page opened).
- 1309 is the Candar infobox's capital change ('Eflani 1291-1309; Kastamonu 1309-1398', reign table Suleyman I 1309-1339) plus the table's end of the Chobanids. The text says only 'his son Suleyman I conquered the neighboring province of Kastamonu' and 'The province had previously been under the rule of the Cobanogullari', with no year or manner. The Kastamonu Province page (tried for the date) has only 'Cobanoglu and Jandarid beyliks' undated and the Ottoman conquest of 1392; it gives an area of 13,064 km2 for the modern province (Cliopatria's 19,765 km2 shape, ratio 0.66).
- For the beylik-of-isfendiyar author: list 'Kastamonu' in cliopatria_names; review the 1309-1313 years of kastamonu_1305, kastamonu_1314 (1314-1332) and kastamonu_1333 (1333-1343); the Sinop annexation (1322 on the beyliks table; beylik-of-sinop names beylik-of-isfendiyar as counterpart); the union of Kastamonu 1314 and Beylik of Sinop 1326 equals Cliopatria's 1333 shape within 0.2 percent; Cliopatria's Kastamonu row ends in 1343 without any event on the Candar page (Kastamonu stays the seat to 1398).
- For the Ilkhanate dossier (ia-02): its loss and vassal_start 1305 and vassal_end 1335 name kastamonu; for 1309-1335 they should name beylik-of-isfendiyar (Candar page: Suleyman 'reigned under the authority of the Ilkhanate ... until the death of their ruler Abu Sa'id'). The Chobanids here are not Cliopatria's Chobanids (Tabriz, 1344-1362).

## beylik-of-saruhan (Sarukhanids, Manisa, Anatolian beyliks, Battle of Ankara)

- Start 1313 (Manisa fell to Saruhan), the page's "about 1300" for the founding; end 1412 (Sarukhanids text), against 1410 (Manisa page; table) and Cliopatria's 1414. Cliopatria ignores the 1390-1402 Ottoman interval.
- Shapes 1314/1326/1344/1407 differ by under 1 percent (grid noise); one 14.4-14.6 thousand km2 core around Manisa. No area on the page.
- Not covered by any page opened: boundaries with Aydin, Karasi and Germiyan, the Ilkhanate, Phocaea, the 1344 Smyrna crusade, the wars with Genoa and Naxos (undated, "regularly battled"), who restored the beylik in 1402.
- Mirrors wanted: ottoman-empire (gains 1390 and 1412, loss 1402).

## Gazetteer names needed

- Place: Alasehir (Philadelphia), used in germiyanids (found, 1304 loss, war zone, keyframe 1300). Capitals and text mention Milas, Kula, Simav, Tavsanli, Egrigoz, Eflani, Safranbolu, Seydisehir, Beysehir town; none is used as a region.

## Pages that failed

- https://en.wikipedia.org/wiki/Mu%27in_al-Din_Suleyman
- https://en.wikipedia.org/wiki/Mu%C4%B1n_al-Din_S%C3%BCleyman_Pervane
- https://en.wikipedia.org/wiki/Mu%27in_al-Din_Suleyman_Pervane
- a Wikipedia search URL (not allowed by the fetch tool)

## Review fixes (2026-10-25, author returning to the failed dossier)

Applied (kastamonu, verdict fail): (1) the 1309 rename, the 1322 Sinop gain and the 1343 loss/dissolve are deleted; kastamonu is the Chobanid beylik only, ending in 1309 with loss + dissolve to beylik-of-isfendiyar, successors beylik-of-isfendiyar, Candar rulers dropped; (2) start moved from 1305 to 1211 with a found event (table row, confidence 2, counterpart sultanate-of-rum) and the new keyframe kastamonu_1211; (3) the 1343 events are gone; (4) kastamonu_1305 adjusted to 1308, kastamonu_1314 and kastamonu_1333 wrong, kastamonu_1323 kept as a wrong pointer; (5) beylik-of-sinop: loss 1322, dissolve 1322 and the successor now name beylik-of-isfendiyar, plus its 1326 correction text and notes. Pages reopened for the dates: Anatolian beyliks (table rows), Candar dynasty (infobox, conquest sentence, Ilkhanate sentence), Kastamonu Province (the thin item: no conquest date there). Both dossiers re-validated with --resolve: 0 errors; the only warnings are the deliberate empty corrections (kastamonu: 3, beylik-of-sinop: 1).

Disagreements and limits: (a) counterpart sultanate-of-rum for the 1211 found follows the reviewer; no page opened says Rum held Kastamonu in 1211 (Kastamonu Province: 'hegemony of the Seljuq dynasty', placed in the 11th century), so it is a confidence-2 reading. (b) A new keyframe with verdict wrong (kastamonu_1323) is unusual; it is kept only because the review asked for it and because it records the 1323-1332 union for the isfendiyar author. (c) The date and manner of the Candar conquest of Kastamonu stay thin: 1309 is the infobox and the table, not a sentence. (d) beylik-of-isfendiyar is not written yet (another me-09 part); until it lists 'Kastamonu', the Candar land of 1309-1343 and Sinop after 1322 has no dossier carrying Cliopatria's kastamonu shapes. (e) The other review items (germiyanids Philadelphia counterpart, the 1314 jizya vassalage and the Ankara reach; menteshe Bodrum 1402 mirror) were not part of this repair and are untouched.
