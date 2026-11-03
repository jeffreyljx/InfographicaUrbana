# Review of batch eu-15-i (2026-10-25)

Reviewer: adversarial pass, Phase B. Machine copy: history/notes/phase-b/reviews/eu-15-i.json.
All five dossiers validate (`--resolve`): 0 errors. Warnings are only the unknown places Toszek and Cieszyn, and the not-yet-written slugs duchy-of-cieszyn and duchy-of-courland-and-semigallia.

| slug | verdict | why |
| --- | --- | --- |
| duchy-of-bytom | thin | 5 spot checks confirmed; 1305-1471 carried forward by design; reviewer fixed two notes (ledger 3, 4) |
| duchy-of-raciborz | thin | 4 spot checks confirmed; 1305-1520 carried forward by design; the page says there were "several territorial changes" before 1521 |
| margraviate-of-moravia | pass | 5 spot checks confirmed; drawing outside 1385-1414 left to the orchestrator |
| house-of-jagiellon | fail | the Starodub gain of 1537 is not on its page; the Livonia/Courland gain of 1561 is mis-drawn; the Moldavian vassalage is missing |
| eastern-hungarian-kingdom | fail | the 1552 loss and the 1551 keyframes contradict the cited Temeşvar Eyalet page and both neighbours |

## house-of-jagiellon (fail)

1. **Starodub, ledger 24 and keyframes 18-23.** The Muscovite-Lithuanian Wars page has the 1534-1537 counterattack "took Gomel and Starodub". It then says the 1537 truce was one "in which Homel stayed under the king's control, while Moscow kept Sebezh and Zavoloche". Starodub is not in the truce. The note's "Lithuania keeps Gomel and Starodub" is therefore not on the page, and keyframe 18's own note concedes "Starodub's later status is not on the page". The 60 km Starodub disc is added to _1537, _1540, _1547, _1556, _1561 and _1564, all inside Moscow's 1540 shape (50 of 50 cells).
   Fix: drop the disc everywhere, and use the gazetteer place "Gomel" (it resolves) for ledger 22-24. Gomel is already in Cliopatria's 1503-1536 shapes, so either cut it there, citing a page that dates its 1503 loss, or keep the 1537 gain as a confirmation and say so.
2. **Livonia, ledger 27 and keyframes 22-23.** The gain region (the 1564 shape minus the 1556 shape) is 86 of 109 cells Courland. That is the vassal duchy of ledger 28, so it is drawn both direct and vassal. The Duchy of Livonia (the page's table: "1561 | Gained 85,000 km2 | Gained Duchy of Livonia by the Treaty of Vilnius") is mostly absent. The factor of 3.1 is explained by Estonia and Ösel-Wiek, which were never Lithuanian.
   Fix: subtract Courland from the direct shape (it keeps the vassal tint of ledger 28) and add Livonia as far as it was held. Or keep Cliopatria's shape with a correct reason.
3. **Moldavia.** The Kingdom of Poland (1385-1569) page has Petru I "becoming a vassal of Władysław II on September 26, 1387" under the heading "Principality of Moldavia (1387–1497)". The notes say no page gives the end.
   Fix: add vassal_start 1450 and vassal_end 1497 at confidence 2, or explain why the heading is not enough.
4. Small fixes: ledger 28's note quotes the Kingdom of Poland page but names the Livonian War page. Certainty 0 is "soft" while its note calls the Prussian line sharp from 1466.
5. Thin: ledger 15 (confidence 1, steppe to nobody); the Polish-Teutonic War of 1519-1521 is not in wars; the small cell changes and the Oświęcim and Zator purchases are within the page budget.

Confirmed on the pages:
- Thorn, 10 October 1466: Pomerelia, Royal Prussia, Warmia, and the Order as a fief.
- 5 February 1494, about 87,000 km2.
- 25 March 1503, about 210,000 km2, Chernigov, Novgorod-Seversk and Starodub.
- Smolensk fell in July 1514.
- Union of Lublin, 1 July 1569.
- Courland from 1562.

## eastern-hungarian-kingdom (fail)

1. **Ledger 8 (1552 loss to ottoman-empire).** The Temeşvar Eyalet page, which the event cites, says: "Upon the initial dissolution of the Eastern Hungarian Kingdom in the summer of 1551, much of its territory, including Temes County, was integrated into the Habsburg Kingdom of Hungary, which provoked an Ottoman invasion". So the note's "The pages do not say whether John II or Ferdinand held them in 1552" is wrong. habsburg-monarchy ledger 11 (July 1552, Temesvár lost to the Ottomans) and ottoman-empire ledger 77 (1552 gain from habsburg-monarchy) already have Habsburg as the loser.
   Fix: remove ledger 8 and move Temes County into the 1551 handover.
2. **Ledger 7, keyframes 5-6.** The 1551 loss covers Transylvania only, and _1551 and _1552 keep the Partium and the Temesköz in the kingdom.
   Fix: make the 1551 loss "much of its territory", and draw 1551-1555 as the pages allow (nothing, or only what a page names). Make the 1556 gain the land the 1556 shape draws, not Transylvania only.
3. Thin: ledger 6 (1547, confidence 1; the page's county list also has Csongrád); the 1526-1528 extent.

Confirmed on the EHK page:
- Treaty of Nagyvárad, 24 February 1538.
- Nyírbátor, 1549, ceding Transylvania.
- The 1556 recall.
- Speyer, 16 August 1570, "thus ending the Eastern Hungarian Kingdom".

## duchy-of-bytom (thin)

Confirmed on the pages:
- The 1281 partition ("about 1281").
- 1284: Bytom, Koźle, Toszek, Gliwice and Siewierz (Casimir page).
- 1355: the north with Koźle to Konrad I of Oleśnica, the rest to Casimir I of Cieszyn.
- 1472: Corvinus annexes Bytom and pledges it to Jan of Zierotin.
- 1498: merged into Opole.

Reviewer-applied fixes:
- Ledger 3's note said the page does not name Hungary. It does: "Matthias Corvinus of Hungary, then self-declared King of Bohemia".
- Ledger 4's note now says the 1498 land comes from the 1472 pledge, so the holder in 1497 (kingdom-of-hungary on this ledger) must carry the 1498 loss to Opole.

Thin by design:
- 1305-1471 is carried forward. The 1355-1459 division is not drawn, and Siewierz is kept to 1471 although the page never mentions it after 1284 (try the Duchy of Siewierz page).
- No rulers.

## duchy-of-raciborz (thin)

Confirmed on the pages: 1281, 1290 (Cieszyn page), 1337 and 1521.

Thin by design:
- 1305-1520 is carried forward, although the page says "The Duchy would suffer several territorial changes until in 1521".
- 1337 is a rename, but the page says "forming the united Duchy of Opava and Racibórz" (try the Duchy of Opava page).

## margraviate-of-moravia (pass)

Confirmed on the Margraviate page:
- 1182 (Barbarossa).
- 1469 occupation and the 1479 Peace of Olomouc ("retained the rule over the Moravian lands").
- 1526 incorporation into the Habsburg monarchy.
- Capitals: Olomouc 1182-1641, Brno 1641-1918.
- Raids 1599-1711.

Also checked: the margrave table, and that there is no infobox area ("about half" of Bohemia, consistent with 22,847 km2).

Left open:
- Drawing outside 1385-1414 is for the orchestrator.
- Ruler gaps (1191-1197, 1411-1419, 1617-1916): the page is silent.
- Hussite Wars and Thirty Years' War not in wars.

## Cross-dossier routing

- **eu-09, habsburg-monarchy:** needs the 1551 gain and 1556 loss of Transylvania (and Temes County in 1551) with eastern-hungarian-kingdom. Its 1572 gain names eastern-hungarian-kingdom after that state's end in 1570; it should be principality-of-transylvania.
- **eu-09, duchy-of-prussia:** no vassal_start naming the Jagiellon realm (suzerain-side convention).
- **me-10, ottoman-empire:** ledger 68 names principality-of-transylvania from 1526. The EHK fealty is 19 August 1529 and the state lasts to 1570.
- **eu-15, kingdom-of-hungary (not yet written):**
  - Bytom: 1472 gain, 1498 loss to Opole.
  - Moravia: 1479 gain, 1490 loss.
  - EHK: 1538 and 1547 losses.
- **eu-15, duchy-of-opole (not yet written):** 1284 loss to Bytom; 1498 and 1521 merges.
- **eu-16, Moscow:** must not lose Starodub in 1537.
