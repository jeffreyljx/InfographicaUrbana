# Review of batch me-09-f (Phase B, 2026-10-25)

Reviewer: adversarial review of the six dossiers by the me-09-f author (beylik-of-menteshe, beylik-of-sinop, eshrefids, germiyanids, kastamonu, beylik-of-saruhan). Machine copy: history/notes/phase-b/reviews/me-09-f.json.

Mechanical: all six validate with 0 errors under `--resolve`; warnings are the place Alaşehir (germiyanids; gazetteer name needed) and two deliberate empty corrections (beylik-of-sinop_1326, germiyanids_1431). Every Cliopatria shape of the six rows has a verdict (2+2+2+10+3+4). Capitals sit inside their shapes' bboxes. Family islam-west exists in colours.json. Neighbour dossiers read: ottoman-empire, byzantine-empire, ilkhanate, timurid-empire, sultanate-of-rum, beylik-of-teke, hospitaller-rhodes, chobanids. Not written yet (exceptions): beylik-of-aydin, beylik-of-hamid, beylik-of-isfendiyar, beylik-of-karaman, beylik-of-karasi, ahi-republic, republic-of-genoa, kingdom-of-georgia, qara-qoyunlu, aq-qoyunlu, shirvan.

Spot checks (WebFetch, 2026-10-25): Germiyanids, Menteshe, Sarukhanids, Manisa, Eshrefids, Timurtash, Candar dynasty, Anatolian beyliks (table rows), Sinop. Every confidence-3 event checked says what its note claims, with the year. No fabricated or mis-dated event found. No page has an infobox area, so no infobox ratio is possible for any of the six.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| beylik-of-menteshe | thin | events confirmed; missing mirror for hospitaller-rhodes 1402 (Bodrum); greatest extent undated |
| beylik-of-sinop | fix (applied) | events confirmed; reviewer added the Pervâneoğlu page the author could not find |
| eshrefids | pass | 1280, 9 Oct 1326 and the ruler table confirmed |
| germiyanids | thin | eight events confirmed; eastern-lobe cut verified on the grid; one note corrected; Philadelphia counterpart and 1314 tribute open; Ankara reach unsupported |
| kastamonu | fail | identity: the Candar realm is drawn in two dossiers from 1309; found 1305 and dissolve 1343 are Cliopatria bookkeeping by the dossier's own words |
| beylik-of-saruhan | pass | 1313, 1390, 1402 and 1412 confirmed |

## kastamonu (fail)

1. `/ledger/1` (rename 1309) and identity. The pages the author read show a conquest by another, already existing state, not a dynasty change inside one state: the Anatolian beyliks table has "Chobanid Beylik, Founder: Husam al-Din Choban, Kastamonu (preceding the Candars), 1211–1309" and "Beylik of Candar / Isfendiyarid Beylik, Eflani, later Kastamonu, last Sinop, 1291–1461"; the Candar infobox has capitals "Eflani 1291–1309; Kastamonu 1309–1398" and the text says Süleyman I "conquered the neighboring province of Kastamonu". Cliopatria's Beylik of Isfendiyar row (Wikipedia title Candar dynasty) is that Candar state at Eflani. Making kastamonu the Candar state from 1309 puts one state in two dossiers for 1309-1343 (kastamonu and beylik-of-isfendiyar), against one dossier per state. Fix: make kastamonu the Chobanid beylik only. End it in 1309 with a `loss` and a `dissolve` (counterpart beylik-of-isfendiyar, region the Kastamonu 1305 shape, confidence 2, Candar infobox and table row). Delete the rename, the 1322 Sinop gain and the 1343 loss and dissolve, which belong to the Candar dossier (beylik-of-isfendiyar). Set successors to beylik-of-isfendiyar (1309) and drop the Candar rulers. Keyframes: kastamonu_1305 becomes adjust with to=1308; kastamonu_1314, kastamonu_1333 and the new kastamonu_1323 become wrong here, with the note "Candar realm's Kastamonu province 1309-1343: reviewed in beylik-of-isfendiyar, which should list 'Kastamonu' in cliopatria_names". The orchestrator should pass this to the beylik-of-isfendiyar author.
2. `/ledger/0` and `/identity/start` (found 1305, confidence 1). The note says "1305 is Cliopatria's first year, not a founding", yet the table row the author read dates the Chobanid beylik 1211–1309. Fix: start 1211 (table row, confidence 2), counterpart sultanate-of-rum, and a new keyframe kastamonu_1211 (1211-1304) that uses the 1305 shape and is marked approximate. The other dossiers in this batch did the same.
3. `/ledger/3-4` (1343 loss and dissolve, confidence 1). The note calls them "a bookkeeping end, not a political one", and the Candar page keeps Kastamonu as the seat until 1398. Once item 1 is done they go.
4. `/keyframe_review/1`. kastamonu_1314 is verdict ok, so it keeps Cliopatria's years 1314-1332 and overlaps the new kastamonu_1323 (1323-1332). It would need adjust with to=1322. This is moot once item 1 is done.
5. Consequence for beylik-of-sinop: `/ledger/1`, `/ledger/2` and `/identity/successors/0` then name beylik-of-isfendiyar, not kastamonu. The Pervâneoğlu page says Gazi Çelebi "bequeathed his lands to the Candarids".
6. Ilkhanate (ia-02): its vassal_start 1305 and vassal_end 1335 with counterpart kastamonu should then name beylik-of-isfendiyar for 1309-1335. The Candar page has Süleyman reign "under the authority of the Ilkhanate ... until the death of their ruler Abu Sa'id".

## germiyanids (thin)

- Checked and holds: the infobox 1300 and 1429; spring 1304 Philadelphia; the 1381 dowry of the four towns and the retreat to Kula; the 1390 "entire realm" Ottoman; Timur's restoration; September 1410; Kütahya to Karaman in 1411; reinstatement in 1414; death in January 1429 and the annexation by will. The eastern lobe is real. On the H3 grid the 1344 shape has 188 cells at 28-31 E, none at 32-37 E and 606 cells at 38-48 E. The cut polygon at 35 E is clean and the 4.5x area ratio is acknowledged and resolved.
- Applied: `/keyframe_review/12/note` said "about 5,900 km2 of the eastern lobe remain at the start". The 1415 shape's bbox ends at 33.77 E, so there is no lobe. The extra 5,900 km2 is the Ankara-Çankırı area, inside the polygon. Note corrected.
- Not applied: `/ledger/1`, counterpart "Catalan Company". The page says Philadelphia "was lost to the Catalans in the spring of 1304, but the town started paying him jizya by 1314". byzantine-empire (`/ledger/187`) holds Philadelphia as "the last Byzantine town in Anatolia" until 1390 and records neither a loss in about 1300 nor a regain in 1304. The Catalans did not hold the town as a state. Fix: counterpart byzantine-empire (the Catalan Company fought in Byzantine pay), with the page's words in the note. eu-05 then needs the mirror, or else Philadelphia leaves the found region.
- Not applied: a missing event on a page the author read. Philadelphia "started paying him jizya by 1314". Add vassal_start 1314 (Alaşehir 25 km, counterpart naming the town, confidence 2) and vassal_end 1390 (Ottoman conquest, byzantine-empire /ledger/187), or say in notes why it is left out.
- Thin: `/ledger/4` (the 1363 Ankara gain, confidence 1). The page's "At that time, Yakub's realm extended as east as Ankara" sits in the paragraph on Yakub as a vassal of Kayqubad III (around 1300), not in the 1360s. The Ankara-Çankırı lobe drawn as Germiyan from 1363 to 1429 (K6, K7, K9-K12) rests on Cliopatria alone, and the 1431 shape is already marked wrong. A gap-filler should check the Ankara article for who held the city from 1354 to 1429 and cut the lobe if it was Ottoman.
- Thin: `/ledger/2-3`, the 1333 and 1344 Hamid gains (confidence 1). Who held Kütahya in 1412-1413. The Catalan interlude at Simav and Kula.
- Minor: the capital Kula runs 1381-1399 (infobox) while the dossier gives Germiyan no land from 1390 to 1402. Leave it or end it in 1390 with a note.

## beylik-of-menteshe (thin)

- Checked and holds: founding "in 1260/1290" with the ruler table from 1261; submission in 1390 and "Ottoman rule (1391–1402)"; restoration after 1402; overlordship in 1414; incorporation in 1426. Rhodes 1300 and 1311 are as stated. The page has no area. It describes the heartland as "roughly ancient Caria or Muğla Province" (Muğla Province is about 12,700 km2, against the 5,886 km2 shape). This is acknowledged in K1.
- Not applied: hospitaller-rhodes `/ledger/3` has a 1402 gain of the Halicarnassus (Bodrum) stronghold, 15 km, with counterpart beylik-of-menteshe at confidence 2. Its note admits that Menteshe is "the researcher's reading". The Menteshe page does not mention Bodrum. Either the Menteshe author adds a small 1402 loss of the Bodrum peninsula (a page needed, such as Bodrum Castle; Menteshe was restored only after July 1402), or the hospitaller author names another counterpart. Routed to both.
- Thin: the greatest extent (Elmalı, Finike, Kaş and Fethiye among its "important centers") is undated.

## beylik-of-sinop (fix, applied)

- Checked: the table row "Pervâneid | Sinop | 1277–1322"; the Candar page's undated annexation; the Sinop page (1214, 1254, 1265, bishop in 1315).
- Applied: the author's missing Pervâneid page exists at https://en.wikipedia.org/wiki/Perv%C3%A2neo%C4%9Flu. Its ruler table has Muînüddin Mehmed 1277–1297, Mühezzebüddin Mesud 1297–1300 and Gazi Çelebi 1300–1322, and it says Gazi Çelebi "bequeathed his lands to the Candarids" (overall range 1261–1326). Added to sources[], made the source of `/ledger/2`, and quoted in the notes. Re-validated.
- Pending on kastamonu item 1: the counterpart and successor become beylik-of-isfendiyar.

## eshrefids (pass)

Tried: the infobox 1280 and 1326; the Timurtash page's "drowning him in Lake Beyşehir on 9 October 1326"; the ruler table; successor coded as ilkhanate rather than the infobox "Chobanids" (explained); the shapes' years; the capital inside the bbox. I could not break it. Thin by design: territory before 1305 and after 1327, and the reach to Konya's plain.

## beylik-of-saruhan (pass)

Tried: Manisa "fell to the Beylik of Saruhan in 1313"; "for a first time until 1390"; the ruler list "Under Ottoman rule (1390–1402)" and Orhan Bey from 1402; "finally until 1412" against Manisa "in 1410", stated in the notes. The four shapes are within 1 percent of each other. I could not break it. Thin by design: who restored the beylik in 1402, Phocaea and the Smyrna crusade, the boundaries.

## Cross-dossier matrix (summary; full list in the JSON)

- ottoman-empire (me-10) is missing: the 1381 Kütahya gain, the 1390 gains of Germiyan, Saruhan and Menteshe, and vassal_start 1414 / vassal_end 1426 for Menteshe. Its 1402 loss names "Anatolian beyliks restored by Timur (Karaman, Germiyan, Aydın and others)" instead of slugs. It dates Saruhan to 1415 (1412 here) and Menteshe to 1415 (1426 here), both at its confidence 1. Its 1429 Germiyan gain matches.
- byzantine-empire (eu-05): its 1305 loss to germiyanids at Kütahya (confidence 1) conflicts with Germiyan's 1300 found from Rum. The Philadelphia question is above. Its 1314 loss to Saruhan matches the 1313 found within a year.
- ilkhanate (ia-02): its 1305 losses and vassal_starts for kastamonu, beylik-of-sinop and eshrefids are confidence 1, while Sinop started in 1277 and the Eshrefids in 1280. Its vassal_end 1335 for Sinop and the Eshrefids comes after they dissolved (1322, 1326). It lacks a 1326 gain from the Eshrefids.
- hospitaller-rhodes: Bodrum 1402 (above).
- Exceptions (not written yet): beylik-of-hamid (1333, 1344), beylik-of-karaman (1411, 1414), beylik-of-isfendiyar (1343 and the kastamonu restructure).
