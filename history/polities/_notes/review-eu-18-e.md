# Review: batch eu-18-e (2026-11-01)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/eu-18-e.json.
Validator (`--resolve`): 0 errors in all five; 3 warnings, all the region 'Pokuttya' (principality-of-moldavia), a gazetteer gap.
Vassal events: the schema puts vassal_start/vassal_end in the suzerain's ledger (counterpart = the vassal), so their absence here is correct.

| slug | verdict |
| --- | --- |
| despotate-of-dobruja | pass |
| despotate-of-vidin | pass |
| principality-of-moldavia | thin (one reviewer fix applied) |
| albanian-principalities | thin |
| serbian-despots | fail |

## despotate-of-dobruja: pass
Spot checks confirmed: 1368 Pangalia (Dobruja page), 1386 capital to Varna, 1388 'most of the Dobrujan forts', 1388/1389 Dristra to Mircea, 'Varna fell to the Ottomans in 1389'. No infobox area. The end in 1389 against the page's 1411 and Cliopatria's 1394 is argued in the notes; the infobox does list Ivanko '1393-1399', so a later reviewer could prefer 1394.
Thin: /ledger/1 (1366 cession, confidence 1; the page puts it in the 1366 account, 2 would be fair), /ledger/3 (Anchialos and Mesembria: no year, previous holder is a guess).
Cross: ottoman-empire gains Dobruja only in 1395 (confidence 1); the pages give 1388-1389 (me-10). principality-of-wallachia has no Dristra gain in 1388/1389 (eu-18). Together these leave Dobruja with no holder on the map in 1390-1394.

## despotate-of-vidin: pass
Confirmed: 1356 proclamation, 1 May / 2 June 1365 Hungarian capture, autumn 1369 restoration, Vidin seized 'by the end of 1396 or the beginning of 1397'. The Tsardom of Vidin infobox has no area; 'Established 1369, Disestablished 1396', Constantine II '1396-1422'. Mirrors: second-bulgarian-empire 1356, kingdom-of-hungary 1365/1369, ottoman-empire 1396 all match.

## principality-of-moldavia: thin (one fix applied by the reviewer)
Applied: /ledger/1 (1392 gain) counterpart 'nobody' changed to 'kingdom-of-hungary'. The note said the page does not name the holder, but the Moldavia page reads 'His brother Roman I conquered the Hungarian-ruled Cetatea Albă in 1392'. The note now quotes the full sentence. Re-validated with 0 errors and read back.
Confirmed: Chilia 1448 / January 1465 / 14-15 July 1484, Cetatea Alba 3 August 1484, Pokuttia 1490 (Stephen the Great), Bukovina October 1774 and the Convention of Pera, 7 May 1775 (Bukovina, 10,442 km2), Bucharest 28 May 1812, Paris 30 March 1856. Area: no infobox area. The text gives 94,862 km2 for the late 15th century, against 99,177 km2 for the 1468-1486 shape and 82,069 km2 for 1487-1506, so the ratio is within 2.
Open (for the author or a gap-filler):
- /ledger/23: the Russian occupation ends in 1856 at confidence 1. russian-empire dates the withdrawal to 26 July 1854 (Crimean War page, confidence 3).
- The Austrian occupation of 1854-1856 is missing; austrian-empire records it with this slug as the counterpart.
- The Russian occupations russian-empire records for 1848-1851 and 1791-1792 are missing here, and so are those of 1739 and 1788-1791.
- 1538 Tighina (/ledger/9): the 1540-1806 keyframes are all 'ok' and keep the Bender cells. Mark them adjust or explain in a note.
- golden-horde has a 1362 loss of 'the Moldavian lands between the Carpathians and the Dniester' to this state, but this dossier draws them from 1359 with no gain.
- The six confidence-1 occupation bridges (1769, 1806, 1812, 1828, 1834, 1856) are listed with pages to try.
Cross: kingdom-of-hungary lacks 1359, 1392, 1448 and 1465; house-of-jagiellon lacks Hotin 1465 and Pokuttia 1490/1531; ottoman-empire has the Budjak in 1487 (confidence 1) against 1484, and lacks 1538. It also ends Moldavia's vassalage in 1878, 19 years after the 1859 union. russian-empire names ottoman-empire, not principality-of-moldavia, as the owner in its occupations and in the 1812 gain.

## albanian-principalities: thin
Confirmed: Durres to Venice 1392; Gropa 'ruled until 1395'; Berat 1417; Rovine '17 May 1395', with Marko's lands annexed into a province centred on Kyustendil. The page has no infobox.
Open:
- despotate-of-epirus /ledger/50 has a 1380 gain from this row (Dryinopolis and the Gjirokaster area, confidence 2) with no loss here.
- serbian-despots loses Lezhe and the Drin to Pal Dukagjini in the late 1380s with this row as counterpart, but there is no gain here.
- Epirus's 1399-1400 Zenebishi occupation names this row as counterpart. Either mirror it here or re-point it to principality-of-gjirokaster.
- Confidence-1 events: the 1375 found (serbian-empire says 'by 1371'), the 1385 Durres loss, the 1385 Epirus cells and the 1421 end. Thopia's 1415 end has no event.
'Louis of Durazzo' (1376-1383) is a free-text counterpart with no dossier. That is acceptable for one city.

## serbian-despots: fail
1. /ledger/1: the quoted sentence 'Lezhe, the Drin area, Onogost (Niksic), and Durres-area lands were lost to rivals and the Venetians' is not on the Đurađ II Balšić page, and 'the page names no rivals or dates' is false. The page says:
   - 'Pal Dukagjini broke off allegiance to Đurađ, taking Lezhë and the Drin area.'
   - 'Finally the Jonima family seceded with their own lands between Durrës and the Drin'
   - 'Nikola Sakat, the castellan of Budva, and his brother Andrija seceded the city after 1386 and Vuk Branković took Peć and Prizren.'
   - 'The area of Onogošt (Nikšić) seceded to the Venetians.'

   The counterpart for Niksic is therefore wrong. Split the event by holder. Keyframe 1's note repeats the invented quote.
2. Area 29,468 km2 (1375-1384) falls to about 7,000 km2 (new 1385 keyframe) with no event explaining it. The page the author couldn't open exists as https://en.wikipedia.org/wiki/Bal%C5%A1i%C4%87_noble_family. It says 'The Balšić holdings declined at the end of the 1370s', 'Vuk Branković took Prizren and other land in Kosovo', and Tvrtko I 'annexed the coastal territories between Dubrovnik and the Bay of Kotor'. Add those losses (district-of-brankovic; Bosnia) c.1378-1379 and end keyframe 0 there.
3. Durres 1385: albanian-principalities /ledger/3 and /ledger/5 name this dossier, but neither mirror is here.
4. No keyframe covers 1371-1374, although the dossier starts in 1371.
5. identity.wikipedia 'Serbian Despotate' / Q878319 belong to moravian-serbia. For the orchestrator: use 'Balšić noble family' (infobox 'Lordship of Zeta (1355–1421)') and wikidata null.
6. Kotor 1391: kingdom-of-bosnia has the 1391 loss going to Hungary, and this dossier never loses Kotor.

Confirmed: 1391 Kotor, early-1393 Ottoman occupation, April 1396 Scutari to Venice, 1405 Ulcinj/Bar/Budva, 1412 Bar, 1418 Shkoder, 1421 to Stefan Lazarević (Balša III died 28 April 1421).
Cross: republic-of-venice records Scutari 1396 with counterpart albanian-principalities and lacks Bar and Budva 1405, Bar 1412 and Shkoder 1418 (eu-13). ottoman-empire uses serbian-despots for Lazar's and the Lazarević Serbia (1386 Niš, the 1390 vassalage, 1459), which should be moravian-serbia (me-10).
