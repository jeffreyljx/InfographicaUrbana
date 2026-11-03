# Notes, batch eu-13-g (Italy part g): republic-of-genoa

One dossier: `history/polities/republic-of-genoa.json` (after the repair pass of 2026-10-31: 79 events, 39 keyframes, 19 wars, 38 pages listed in sources, validates with `--resolve`, 2 warnings: the Capraia disc resolves to no cells; before the repair: 50 events, 15 wars, 14 pages, 0 warnings). Page budget for a 38-shape state: 14. All 14 were spent; the Republic of Genoa article was read twice with different questions.

## Cliopatria row: one state, but three shapes before it begins
- The page dates the Republic "from the years 1099 to 1797" (infobox: established 1099, disestablished 14 June 1797). Shapes 1010, 1034 and 1040 (1010..1098) are marked `wrong`; the state starts in 1099. Judgment call: the Genoa page also has a 958 diploma of Berengar II ("full legal freedom") and a joint defence of Sardinia with Pisa in 1016, so a city-state could be started earlier. The Holy Roman Empire dossier (eu-08) has a 1010 loss of the Ligurian coast to Genoa that should move to 1099 (or 1200, the page's "all of Liguria by the end of the 12th century").
- The row is one continuous state, not successive states: no split. The row ends in 1795, the Republic in June 1797: new keyframe `republic-of-genoa_1796` carries the 1794 shape through 1797. The Ligurian Republic (slug `ligurian-republic`, Cliopatria 1797..1814) has no dossier yet.

## Cliopatria shapes corrected (verdict adjust or wrong)
- Lesbos (1363..1525) and Lemnos (1453..1525): the Gattilusio family's lordship, granted by John V in 1355 and taken by the Ottomans in 1456/1462; the Gattilusio page does not make them vassals of Genoa. Removed.
- Rhodes (1250..1259): not on the Genoa page; the Domain of Rhodes dossier has the Genoese there 1248 to early 1250. Removed (unverified: page budget).
- Caffa missing 1266..1307 and 1308..1313 (granted 1266, lost to Toqta 1308, regained 1313): added by correction and ledger.
- North-west Sardinia (1260..1351): Doria and Malaspina lordships, "influence" per the Genoa page; drawn as a vassal tint under the counterpart string `Doria and Malaspina lordships (Sardinia)`, ended 1354 (Alghero occupied by the Catalans).
- Chios: Genoa's own land 1275..1304 only (Cliopatria draws 1272..1631); 1304..1329 the Zaccaria lordship (lordship-of-chios), 1329..1346 Byzantine, 1346..1566 the Maona of Chios as a vassal tint (maona-of-chios). See the repair pass below.
- Ligurian core absent in 1402..1414, 1422..1439 and 1540..1563: restored (the Republic continued under French domination, Milanese lordship and the 1528 constitution). Corsica absent 1375..1384: restored; absent 1422..1449: Aragon (ledger).
- Black Sea cells run to 1525 but end in 1475; Corsica runs to 1793 but ends 1768 (interior lost in 1755).

## Disagreements between pages
- Battle of Ponza page: Genoa overthrew Milan on 27 December 1435; the Duchy of Milan dossier (eu-13 part) has the Peace of Cremona of 20 November 1441 recognising independence. Cliopatria returns the core in 1440.
- Inside the Genoa article: Caffa 1255 or 1266; Corsica 1284 or "formally annexed in 1347"; Chios "from 1261 to 1566" or "granted in 1275"; Cyprus tributary 1372..1426 (Kingdom of Cyprus infobox) or "granted" at the end of the 14th century; Gazaria lost 1474 or 1475; Sforza dates marked "clarification needed".

## Pages that gave nothing
Duchy of Milan, Filippo Maria Visconti, Battle of Ponza (disambiguation; the 1435 article was then opened). Thin: History of Genoa, Judicate of Logudoro, Famagusta, Kingdom of Cyprus (one infobox line each).

## Not reached (page budget)
Bonifacio's founding (the 1202 Corsican tip is confidence 1), the Maona of Corsica, Smyrna 1261 (no end date, so no event), Phocaea, Samos (1352 cells at confidence 1), Samsun, Trebizond/Leonkastron, Pera/Galata, Levant quarters (Acre, Tyre, Gibelet, Antioch: no cells), Rhodes 1248..1250, Finale and Savona, the one-cell Riviera shifts of 1632..1748 (verdict ok, unverified), the Bank of Saint George's takeovers, the Spanish capture of 1522, the Spanish protectorate after 1528 (the Kingdom of Spain dossier may want a vassal_start), and the doge list (`identity.rulers` omitted).

## Mirrors for other groups
French domination/occupation 1394..1409, 1458..1461 and 1499..1528 are written from Genoa's side as `occupation_start/_end` (Genoa the occupied party); the Kingdom of France dossier should carry the mirror. Gains from the Golden Horde (Caffa 1266, Taman 1305, Tana 1316, Gothia coast 1375), Hafsid Dynasty (Tabarka 1540) and Beylik of Tunis (Tabarka 1742) have no mirror checked (Chios and Samos are now carried through the Maona, see the repair pass). Duchy of Milan has no 1499 loss.

## Gazetteer
Names wanted: Bonifacio, Caffa (Feodosia), Alghero, Phocaea, Samos, Lemnos, Tabarka (written as a coordinate), Lesbos (alias of Mitilini). Specs built from Cliopatria shapes intersected with the Corsica, Sardinia, Crimea regions and radii around Azov and Kerch stand in for them.

## Counterparts needing dossiers
`ligurian-republic` (1797..1805/1814, in polities.csv, no dossier); the Doria and Malaspina lordships of Sardinia (1259..1354, the vassal counterpart is a plain string, no slug); the Genoese Gazaria is kept inside this dossier. The Gattilusio lordship (`gattilusi`) and the Maona of Chios (`maona-of-chios`) now have dossiers and are no longer wanted.

## Repair pass (2026-10-31, after the review in review-eu-13-g.md)

Every date below was read again on the page named; nothing was fixed from memory.

### Changed
- **Chios (blocking finding, applied).** Ledger: 1275 gain kept (Republic page; the Chios page instead says authority 'was ceded to the Republic of Genoa (1261)' and never mentions 1275); new 1304 loss to `lordship-of-chios` (confidence 2; Chios page: 'the Genovese Benedetto I Zaccaria (1304)', 'a renewable concession'); the 1329 loss and the 1346 gain deleted; 12 September 1346 is now a `vassal_start` and April 1566 a `vassal_end` with counterpart `maona-of-chios`. Wars 'Genoese conquest of Chios and Phocaea' and 'Ottoman conquest of Chios' list `maona-of-chios`. Chios (and Samos from 1352) is subtracted from the corrections of the shapes 1305 to 1564; the shapes 1352, 1526 and 1529 changed from ok to adjust for that.
- **Samos.** The Samos page says the island 'became the property of the Genoese family Giustiniani (1346-1566; 1475 interrupted by an Ottoman period)'. The 1352 gain (confidence 1, from the shape alone) is deleted and Samos is folded into the 1346 vassal region. The `maona-of-chios` dossier draws Chios only; its owner may want Samos added.
- **Soldaia.** Sudak page: 'on 19 July 1365, the Genoese from Kaffa seized the city'. New 1365-07 gain from `golden-horde`, confidence 3; the 1375 Gothia event now covers the rest of the coast (Cembalo) at confidence 1, and the 1363 shape correction adds the Soldaia cell.
- **Milan 1421** raised to confidence 2: Wars in Lombardy page footnote 'Milan controlled Genoa since 1421'.
- **Corsica 1768** now dated 15 May 1768 (Treaty of Versailles page).
- Mirrors added (events with counterpart): Rhodes 1248-1250 (occupation, `domain-of-rhodes`; contest, `nicaean-empire`), Trebizond (contest 1306-1314, Kerasus occupation 1347-1349 at confidence 1, Leonkastron 1349), Tripoli 1354 and 1355, Livorno 1405 and 28 August 1421, Cembalo contest February 1433 to June 1434, Monaco 1297-1419 (nine events), Finale 1713, Capraia 1767 and May 1768, and Elba 1284-1292. These sub-cell events are drawn from the ledger, not from the keyframe corrections.

### Not mirrored, and why
- **Crete 1206-1217.** Kingdom of Candia page: 'Pescatore was largely left unsupported by Genoa'; the Pescatore page calls him a corsair and privateer and does not say the Commune backed him; the treaty of 11 May 1217 is 'the war with Genoa' but its signatories are not named. Recorded as a war entry with no zones. The `kingdom-of-candia` contest with `republic-of-genoa` reads the Commune into a private venture.
- **Elba 1548.** Elba page: the Appiani, Lords of Piombino, held it; 'In 1546, part of the island was handed over to Cosimo I'; the only Genoese holding is the one after Meloria (1284) to 1292. The Florence dossier's 1548 gain 'from the Republic of Genoa' (Grand Duchy of Tuscany page) does not match the Elba page; its counterpart should probably be Piombino.
- **Theodoro 1423.** Theodoro page: 'In 1423 prince Alexios attacked and the Genoese had to spend a large sum of money to repel him'. No Genoese land changed hands on the page, so the `principality-of-theodoro` 1423 gain from Genoa (confidence 1) has no mirror. Cembalo is a contest, not a loss: the page says only that Alexios supported a Greek rebellion there.

### Disagreements with the review
- The reviewer's Livorno note has a 1407 Genoese purchase; the Livorno page says 'in 1405 it was sold to the Republic of Genoa' and names no seller (the seller is read as Milan, confidence 2). The page also contradicts itself on 1421 ('bought by the Republic of Florence' against 'bought from Florence' in the fortress section).
- The reviewer calls the Monaco events sub-cell. They are mirrored anyway because the dates are on the List of rulers of Monaco page; the Monaco page itself (not opened) is said by the Monaco dossier to have the Grimaldi buying Monaco from the Crown of Aragon in 1419.

### Still thin (pages opened, silent)
- 1202 Bonifacio (Bonifacio, Corse-du-Sud page: founded 828, nothing on Genoa), 1305 Taman (Matrega page: Genoese archdiocese 'canonically established on 1349.02.21', no acquisition date), 1375 Cembalo, 1422 and 1450 Corsica (Alfonso V page: 'in possession of much of Corsica by the 1420s'), 1464 Famagusta (James II and Charlotte pages silent; Charlotte's page has Louis taking Famagusta in 1460).
- `identity.rulers` still omitted: the List of doges of Genoa page gives 47 rows, 1339 to 1527, with many dates not printed and the Doge cells empty for 1528-1797, which is not a list the ruler strip can rest on. (The title 'List of doges of the Republic of Genoa' returned url_not_found.)
- Finale 1713: both pages (Marquisate of Finale: 'ceded to the Republic of Genoa on 20 August 1713'; Finale Ligure: 'acquired by the Republic of Genoa in 1713') name no cedent; counterpart `kingdom-of-spain` is a bridge (Spanish since 1602 on the page) at confidence 2.

### Gazetteer
Capraia (9.83 E 43.05 N, a 12 km disc resolves to no cells, as in the corsican-republic dossier), Finale Ligure (8.34 E 44.17 N, written as a disc), Cembalo/Balaklava (33.6 E 44.5 N), Elba (a disc at 10.3 E 42.78 N).
