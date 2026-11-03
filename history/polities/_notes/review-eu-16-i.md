# Review of batch eu-16-i (zaporozhian-cossacks, sloboda-ukraine)

Reviewer, 2026-10-25. Validator (--resolve): both dossiers 0 errors; zaporozhian-cossacks 1 warning (gazetteer: 'Danube Delta' unknown, successor land). Pages opened: Zaporozhian Sich, Zaporozhian Cossacks, New Serbia (historical province), Treaty of Andrusovo, Sloboda Ukraine. Neighbour dossiers present: ottoman-empire, crimean-khanate, astrakhan-khanate; absent (groups not run yet): tsardom-of-russia, polish-lithuanian-commonwealth, russian-empire, pro-swedish-poland, swedish-empire, cossack-hetmanate, danubian-sich, new-serbia.

## zaporozhian-cossacks: fix (author; non-blocking)
Tried and could not break: every ledger event checked against the pages. Sich page: infobox 'c. 1552', vassal status by period (Poland-Lithuania 1583-1654, Muscovy 1654-1709, Ottoman Empire 1711-1734, Russian Empire 1734-1775), seat table (Tomakivka c.1564-1593, Bazavluk 1593-1638, Mykytyn 1639-1652, Chortomlyk 1652-1709, Kamianka 1709-1711 and c.1728-1734, Oleshky 1711-1728, Nova 1734-1775), 'Tekeli surrounded the Sich' 5 June 1775, 'officially disbanded by the 3 August 1775 manifesto'. New Serbia page: 'settled in 1752', 'on the land of the Zaporizhian Sich', 'mostly in ... Kirovohrad Oblast' with parts of Cherkasy, Poltava and Dnipropetrovsk; matches the 1752 drop of 91 cells. Andrusovo page: condominium sentence, 9 Feb [O.S. 30 Jan] 1667, Kiev two years, 146,000 rubles. Cossacks page: Peter's retaliatory destruction after Poltava, Oleshky 'under Crimean-Ottoman protection', 1734 'regained all of their former lands', 7 May / 15 May-8 June 1775. Capitals contiguous, capital_move years equal the new seats' from years. Area: no infobox area on either page (acknowledged).
The vassal relations are correctly left to the suzerains (schema: vassal_start sits in the overlord's ledger with the vassal as counterpart).

Finding (not applied, author):
- /keyframe_review/0/correction: the 100 km core round Zaporizhzhia (127 land cells) overlaps the Crimean Khanate's Cliopatria shape on 37 cells in the 1600-1640 anchors and 36 in 1650-1660 (data/anchors p1600..p1660); neither keyframe note nor ledger mentions it (the note discusses only the Commonwealth). Fix: subtract the khanate's shape from the core ({"minus": [core, {"cliopatria": "Crimean Khanate", "year": 1600}]}) or say in the note why the Sich takes those cells; tell ia-02 if the khanate's 1595 northern-steppe loss should reach the rapids.

Thin (gap-filler, within page budget 5 for 8 shapes):
- /wars: the Zaporozhian Cossacks page (opened) names the Khmelnytsky Uprising (1648) and the Cossacks' part in the Russo-Turkish War before 1775; neither is a war entry. Try https://en.wikipedia.org/wiki/Khmelnytsky_Uprising and https://en.wikipedia.org/wiki/Russo-Turkish_War_(1768%E2%80%931774).
- /keyframe_review/1..5: 1662-1751 outline unverified; it runs to 49.85 N with 46 Poltava Oblast cells, which may be Hetmanate (Poltava/Myrhorod regiment) land rather than the Liberties. Try https://en.wikipedia.org/wiki/Cossack_Hetmanate.
- /identity/capitals/5 and /7 (Kamianka Sich, 34.42 E 47.49 N): this point is Kamianka-Dniprovska on the left bank and falls in crimean-khanate cells in the 1700-1760 anchors; the page puts the Sich 'at the mouth of the Kamianka River'. Coordinates approximate (author says so); verify. Try https://en.wikipedia.org/wiki/Kamianka_Sich.
- 1711-1734 status (Treaty of Adrianople 1713, Treaty of Lubny 1734) and Slavo-Serbia (1753) not drawn; try https://en.wikipedia.org/wiki/Slavo-Serbia.

## sloboda-ukraine: fix (applied by reviewer)
Tried and could not break: all three events confirmed on the Sloboda Ukraine page ('From 1650 to 1765 ... increasingly organized'; 'the Sloboda Ukraine Cossack capital was located in Sumy until 1743'; 'converted into the Sloboda Ukraine Governorate', 'decree of July 28, 1765'). Infobox capital Kharkiv, no area, no dates. Shapes 1670/1752/1763 differ by under 0.5%; end 1765 (1763 adjust, years only) sound. No overlap with zaporozhian-cossacks in any anchor (no conflict rows). Not merged with ukraine: correct.

Fix applied:
- /identity/capitals/0/to and /identity/capitals/1/from: Sumy to 1743 and Kharkiv from 1744 disagreed with the ledger's capital_move at 1743 (the author's own convention in zaporozhian-cossacks is move year = new seat's from year). Now Sumy 1650-1742, Kharkiv 1743-1765. Re-validated: 0 errors, 0 warnings.

Thin (budget 1-2 pages, 3 shapes):
- /keyframe_review/0 (1650-1669): the 1670 outline carried back at confidence 1; the region was settled progressively. Regiment founding years and the Belgorod/Izium lines are needed. Try https://en.wikipedia.org/wiki/Belgorod_Line.
- /identity/capitals/0: Sumy from 1650 is the dossier's start year, not a page's; the town itself may be younger. Try https://en.wikipedia.org/wiki/Sumy.

## Cross-dossier matrix
- zaporozhian-cossacks 1752 loss to russian-empire (New Serbia): exception, russian-empire (eu-17) not written.
- zaporozhian-cossacks 1775 dissolve, successor russian-empire: exception, eu-17 not run.
- ottoman-empire 1677 loss of right-bank Ukraine to zaporozhian-cossacks (conf 1): MISMATCH. No Zaporozhian gain; the Zaporozhian shape gains 2 cells in 1677. Route to me-10: the counterpart is unsupported (the Ottoman event's own source says only that Bakhchisarai 'established the Russo-Turkish border on the Dnieper River', and no Zaporozhian page records a gain); find the page that says who took the land, or drop the event.
- ottoman-empire 1739 loss of 'Azov ... and the Zaporozhye region' to russian-empire: exception (Russia not written); on the Zaporozhian side the Sich is under Russia from 1734, so me-10 should record a vassal_end for zaporozhian-cossacks in 1734 rather than (or besides) a 1739 land cession.
- Vassal relations from the Sich infobox (confirmed): polish-lithuanian-commonwealth 1583-1654 (eu-15 not run), tsardom-of-russia 1654-1709 (eu-16 not written), russian-empire 1734-1775 (eu-17 not run): exceptions. ottoman-empire 1711-1734: MISSING, the dossier exists and has no vassal_start/vassal_end with counterpart zaporozhian-cossacks (route to me-10; crimean-khanate, ia-02, may carry it instead since Oleshky lay in the khanate).
- zaporozhian-cossacks 1552-1661 core vs crimean-khanate shape: overlap of 36-37 cells with no event either side (see finding).
- sloboda-ukraine 1650 found (predecessor tsardom-of-russia) and 1765 dissolve (successor russian-empire): exceptions, neither written.
