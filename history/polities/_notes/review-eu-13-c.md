# Review of batch eu-13-c

Reviewer: adversarial review, 2026-10-31. Dossiers: republic-of-venice (verdict FAIL), republic-of-saint-titus (verdict FIX, fixed by the reviewer). Machine copy: history/notes/phase-b/reviews/eu-13-c.json.

Mechanical: both files validate with no errors. Venice has 74 resolve warnings: 5 for the counterpart slug duchy-of-ferrara and the rest for place names the gazetteer lacks. Saint Titus has none. Pages opened by the reviewer: Republic of Venice, Stato da Màr, War of the League of Cambrai, Cretan War (1645-1669), Ottoman-Venetian War (1714-1718), Treaty of Zadar, Kingdom of Candia and Revolt of Saint Titus.

## republic-of-venice: fail

Area: The reviewer confirmed the infobox has no area (only a 16th-century population estimate of 2,500,000). Cliopatria's largest shape is 65,312 km2 (1687-1690). The author's notes acknowledge the missing area.

### Findings

- `/keyframe_review/54/correction`: BLOCKING. The 1509-1511 correction ('the 1507 shape without Verona') keeps Brescia, Bergamo, Crema and Cremona Venetian after Agnadello. Evidence: War of the League of Cambrai page: after 14 May 1509 'Louis proceeded to occupy Venetian territory as far east as Brescia without encountering any significant resistance'; in February 1512 Brescia 'had rebelled against the French', so it was French in 1509-1511. The dossier's own 1509 note quotes Venice losing 'all the territory that they had accumulated in northern Italy'. Fix: Correction for 1509-1511: the 1507 shape minus Verona, Brescia, Bergamo, Crema and Cremona (admin1 Verona, Brescia, Bergamo, Cremona; Crema lies in Cremona province), text from the page. Re-check the 1512 keyframe the same way (Bergamo and Crema need their own return dates).
- `/ledger (new event, 1509-05)`: BLOCKING. No event records the loss of the Lombard Terraferma (Brescia, Bergamo, Crema, Cremona) to France in May 1509. Evidence: Same Cambrai sentence ('occupy Venetian territory as far east as Brescia'); the ledger only loses Padua, Verona and Vicenza to Maximilian (/ledger/74) and Ravenna and the Polesine. Fix: Add {year 1509, month 5, type loss, counterpart kingdom-of-france, region union admin1 Brescia, Bergamo, Cremona, text 'Venetian territory as far east as Brescia', source the Cambrai page, confidence 3}; add returns (Bergamo, Crema, Brescia 1512-1516) only with a page that dates them.
- `/ledger/77`: Brescia's loss to France is dated February 1512 at confidence 3, but Brescia was French from 1509; February 1512 is a brief Venetian-backed rebellion crushed by the French sack. Evidence: Cambrai page: '18 February 1512: Sack of Brescia'; Brescia 'had rebelled against the French and garrisoned itself with Venetian troops'. Fix: Fold into the new 1509 loss; if kept, write the rebellion as a February 1512 gain and the sack (18 February 1512) as the loss, both counterpart kingdom-of-france.
- `/ledger/78`: Cremona's loss bridged to December 1516 (confidence 1); it went to France with the rest of Lombardy in 1509. Evidence: Cambrai page (French occupation as far east as Brescia, 1509); the Treaty of Brussels clause 'except for Cremona' (6 December 1516) only confirms it was not returned. Fix: Move Cremona into the 1509-05 loss to kingdom-of-france and delete this bridging event.
- `/keyframe_review/62/correction and /keyframe_review/63/correction`: BLOCKING. The Crete keyframes over-draw Venetian Crete: 1647 is drawn as the whole island without Chania and Rethymno, and the 1648-1668 shape keeps about 3,500 km2 of central Crete; no ledger event loses the Cretan countryside. Evidence: Cretan War page: 'By the beginning of 1648, the Ottomans held all of Crete except Candia and a few strongholds, such as Gramvousa'; the dossier's own /ledger/98 note says that by 1647 the Ottomans held most of eastern Crete 'except the fortress of Siteia'. Areas: the 1645 shape is 49,682 km2 and the 1648 shape 44,836 km2, while Crete is about 8,300 km2, so about 3,500 km2 of Crete stays in. Fix: Add a loss {year 1647, counterpart ottoman-empire, region Kriti minus Candia (Iraklio km 15), Sitia, Souda, Spinalonga, Gramvousa, source Cretan War page}; 1645 keyframe for 1647 = 1645 shape minus Crete plus those places; 1648 keyframe = 1648 shape minus Crete plus Candia, Sitia (to 1651), Souda, Spinalonga and Gramvousa.
- `/ledger/72`: The Polesine (Rovigo) is lost to Ferrara in 1509 and never regained, yet Venice held Rovigo until 1797 and the 1512-1525 and 1517 keyframes are taken as drawn. Evidence: Unpaired loss in the ledger (Rovigo: 1482+, 1484+, 1509-). The Cambrai page says only that d'Este 'seized the Polesine'. Fix: Add the Venetian recovery of the Polesine, dated from a page (Rovigo or Polesine article), counterpart duchy-of-ferrara.
- `/ledger/71` (APPLIED by reviewer): Ravenna is lost in 1509, but no event ever gains it (Ravenna 1441, Faenza and Rimini 1503), and the source page does not say Ravenna was Venetian. Evidence: Cambrai page: 'Julius invaded the Romagna and captured Ravenna with the assistance of Alfonso d'Este'; the main page has no sentence putting Ravenna, Faenza or Rimini under Venice. The note itself says the page does not say Ravenna was Venetian. Fix: Reviewer lowered the confidence to 2 (applied). Author: add the 1441 Ravenna and 1503 Romagna gains from a page, or drop the loss.
- `/ledger/13 and /ledger/82, /ledger/83, /ledger/86, /ledger/92, /ledger/93`: The 1207 Cyclades gain (direct Venetian rule) and its later losses duplicate the land of the Duchy of the Archipelago, which has its own dossier (1207-1579) with no Venetian relation. The keyframes do not draw the islands before 1385, so the 1207 gain has no keyframe trace. Evidence: Stato da Mar page: the Cyclades were held mostly 'as the Duchy of the Archipelago'; duchy-of-the-archipelago.json: 1207 found (Marco Sanudo), 1566 rename, 1579 dissolve. Fix: Re-code it as a relation with the duchy (vassal_start or vassal_end, with years from a page) and keep direct gains and losses only for islands a page puts under direct Venetian rule (Tinos and Mykonos after 1390, Kythira). Then re-check the 1385-1563 Aegean polygons that Cliopatria draws for Venice.
- `/ledger/49`: Euboea is lost in 1470 but never gained. Cliopatria draws it as Venetian in 1210-1474 (keyframes ok), and the negroponte dossier keeps the island as its own state until July 1470. Evidence: negroponte.json: '1390 rename, counterpart republic-of-venice: the last triarch's lands pass to Venice and Negroponte becomes a Venetian colony'. The keyframe note at /keyframe_review/20 cites 'Euboea (the Venetian share after 1204 on the main page)'. Fix: Add the gain of Euboea (1390, a merge or gain from negroponte, with a page such as Triarchy of Negroponte) and a vassal relation for 1209-1390, or mark the 1210-1389 keyframes adjust to remove Euboea; agree with the eu-05 Negroponte dossier on who holds the island in 1390-1470.
- `/ledger/36`: Patras is gained in 1408 and never lost. Evidence: Stato da Mar list (read by the reviewer): 'Patras (Patraso/Patrasso), 1408–1430 and 1687–1715'; despotate-of-the-morea.json has a 1430 gain of Patras from republic-of-venice. Fix: Add {year 1430, type loss, counterpart despotate-of-the-morea, place Patra km 15, source Stato da Mar, confidence 3}.
- `/ledger/28, /ledger/30, /ledger/35, /ledger/11`: Counterparts given as readings disagree with neighbour dossiers that cite pages. Evidence: lordship-of-argos-and-nauplia.json: Nauplia sold to Venice on 12 December 1388. despotate-of-the-morea.json: Argos lost to Venice in June 1394. despotate-of-arta.json: Naupactus lost to Venice in 1407. principality-of-achaea.json: Modon and Coron lost to Venice in June 1209. Fix: Set the counterparts to lordship-of-argos-and-nauplia (month 12), despotate-of-the-morea (month 6) and despotate-of-arta. For Modon and Coron, reconcile 1207 against 1209 and the counterpart (Achaea or the Byzantine Empire) with the Achaea dossier.
- `/keyframe_review/36 and /keyframe_review/37`: The Attica-Boeotia polygon (1395-1406) is left 'ok, unverified'. A neighbour dossier explains it, and the ledger has no event for it. Evidence: acciaioli-duchy-of-athens.json: 22 May 1390 Megara ceded to Venice; 18 March 1395 'The Venetian Senate acknowledged the annexation of Athens'; contest 1402-1403; 1403 Antonio I regains Athens. Fix: Add gains of Megara (1390) and Athens/Attica (1395-03) from acciaioli-duchy-of-athens, the 1402-1403 contest and the 1403 loss; mark the 1402 keyframe adjust (no Attica from 1403).
- `/ledger/121/region`: Aegina is lost in 1715 (/ledger/123) but never gained; the 1699 gain's text names Aegina while its region is only the Peloponnese. Evidence: /ledger/121 note: 'Venice kept the Morea, Aegina and Kephalonia'. Fix: Add place Aegina (km 15) to the union of /ledger/121 (or a 1687 gain if a page dates it).
- `/ledger/84`: The northern Sporades are lost in 1538, but their 1453 gain is missing. Evidence: Stato da Mar: 'Skyros (Sciro), 1207–1270s and 1453–1538'. Fix: Add a 1453 gain (Skiathos, Skopelos, Skyros), source Stato da Mar, holder not named by the page.

### Gaps for a gap-filler

- `/ledger (Thessalonica)`: Venetian Thessalonica, 1423-1430: byzantine-empire.json loses it to Venice in September 1423 and ottoman-empire.json gains it from Venice in 1430; this ledger has neither. Page to try: https://en.wikipedia.org/wiki/Siege_of_Thessalonica_(1422%E2%80%931430)
- `/keyframe_review/11-16`: Dalmatia in 1018-1133. kingdom-of-croatia.json loses the Dalmatian cities to Venice in 1018 and 1085, and kingdom-of-hungary.json and croatia-in-union-with-hungary.json record a Venetian seizure in 1116 and a Hungarian recovery of all but Zadar in 1133. The Venice keyframes hold Dalmatia from 1000 to 1186 without a break. Page to try: https://en.wikipedia.org/wiki/Croatia_in_personal_union_with_Hungary
- `/ledger (Istria)`: The western Istrian coast in the 13th century: patriarchate-of-aquileia.json loses it to Venice in 1291. The ledger's only Istria event is in 1000. Page to try: https://en.wikipedia.org/wiki/Patriarchate_of_Aquileia_(state)
- `/ledger (Rovigo 1395-1438)`: The main page (read by the reviewer) says: 'In 1481, Venice retook nearby Rovigo, which it had held previously from 1395 to 1438'. The ledger has no 1395 gain and no 1438 loss. Page to try: https://en.wikipedia.org/wiki/Republic_of_Venice
- `/ledger (Lefkada 1715-1716)`: The 1714-1718 war page says the Ottomans 'occupied the island of Lefkada (Santa Maura), which the Venetians had taken in 1684'. The ledger has no loss, and no regain is dated. Page to try: https://en.wikipedia.org/wiki/Lefkada
- `/ledger (Lombardy 1447-1454, Crema)`: ambrosian-republic.json loses Lodi and Piacenza to Venice in 1447, and duchy-of-milan.json regains them in 1453 (both confidence 1). Crema (Venetian from 1449) and the 1454 Peace of Lodi line are not in the ledger. Page to try: https://en.wikipedia.org/wiki/Peace_of_Lodi
- `/ledger/54`: Confidence 1: the loss of Imbros, Thasos and Samothrace is bridged to 1479. Page to try: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Venetian_War_(1463%E2%80%931479)
- `/ledger/79`: Confidence 1: Brescia's return to Venice is bridged to 1517 (it returned in 1516), and Bergamo's and Crema's returns are missing. Page to try: https://en.wikipedia.org/wiki/Brescia
- `/keyframe_review/19-36`: Cliopatria polygons the author left unverified: the Crimea (Sudak/Soldaia) 1206-1278 and 1305-1374, near Kos 1206-1325, Vlore 1326-1332, the Euboea dip 1279-1284, the Dalmatia dips 1169-1187 and 1440-1449, Tenedos 1377-1381, Chios 1694, and the 1537-1540 war. Page to try: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Venetian_War_(1537%E2%80%931540)
- `/identity/rulers`: There is no rulers strip (no list of doges was opened). Page to try: https://en.wikipedia.org/wiki/List_of_doges_of_Venice

### Spot checks

- `/ledger/3` (Republic_of_Venice): confirmed ('in the year 1000 he managed to subjugate the coastal cities of Istria and Dalmatia')
- `/ledger/32 and /ledger/33` (Republic_of_Venice): confirmed ('Vicenza, Belluno, and Feltre were acquired in 1404, and Padua, Verona, and Este in 1405')
- `/ledger/62` (Republic_of_Venice): confirmed ('In February 1489, the island of Cyprus ... was added to Venice's holdings')
- `/ledger/64` (Republic_of_Venice): confirmed (1499, 'gaining Cremona')
- `/ledger/11, /ledger/17, /ledger/34, /ledger/36, /ledger/55, /ledger/67` (Stato_da_M%C3%A0r): confirmed (Methoni 1207-1500; Kythira 1238-1715; Ulcinj 1405-1571; Patras 1408-1430; Zakynthos 1479-1797; Cephalonia 1500-1797). Patras's 1430 end is not in the ledger
- `/ledger/13` (Stato_da_M%C3%A0r): confirmed as a list entry, but the page says the Cyclades were held 'as the Duchy of the Archipelago' (see fixes)
- `/ledger/74, /ledger/80` (War_of_the_League_of_Cambrai): confirmed (Padua, Verona and Vicenza surrendered to Maximilian, 1509; Verona surrendered to Venice in January 1517)
- `/ledger/77` (War_of_the_League_of_Cambrai): mis-dated: Brescia was French from 1509 ('occupy Venetian territory as far east as Brescia'); 18 February 1512 is the sack after its rebellion against the French
- `/ledger/71, /ledger/72` (War_of_the_League_of_Cambrai): confirmed as quoted. The page does not say Ravenna was Venetian; confidence lowered to 2 by the reviewer
- `/ledger/22` (Treaty_of_Zadar): confirmed (18 February 1358; 'from the Kvarner to the Bay of Kotor'; kept 'the Istrian coast and the Treviso region')
- `/ledger/95, /ledger/96, /ledger/99-103` (Cretan_War_(1645%E2%80%931669)): confirmed (Chania 22 August 1645; Rethymno 20 October 1646; Tenedos and Lemnos 1656-1657; Candia 5 September 1669, and Venice kept Tinos, Kythera, Spinalonga, Gramvousa and Souda). The page also says that by early 1648 the Ottomans held all of Crete except Candia and a few strongholds, which the keyframes ignore
- `/ledger/123, /ledger/124, /ledger/127, /ledger/128, /ledger/130` (Ottoman%E2%80%93Venetian_War_(1714%E2%80%931718)): confirmed (Tinos and Aigina; Nauplia 20 July 1715; 'within a hundred days' after the 25 June entry; Souda and Spinalonga capitulated; Preveza and Arta 1717). The page also has the 1715 Ottoman occupation of Lefkada, which is not in the ledger

## republic-of-saint-titus: fix

Area: There is no Cliopatria row and no infobox area; the drawn land is Crete (about 8,300 km2).

### Findings

- `/identity/wikipedia and /sources` (APPLIED by reviewer): wikipedia was null, but the revolt has its own article. Evidence: https://en.wikipedia.org/wiki/Revolt_of_Saint_Titus exists (title 'Revolt of Saint Titus', infobox August 1363-1364, body: Venetian rule consolidated over the whole island in 1368). Fix: Set identity.wikipedia to 'Revolt of Saint Titus' and add the page to sources[] (done by the reviewer; the file re-validates with no errors or warnings).

### Gaps for a gap-filler

- `/keyframe_review/1`: The stages of the Venetian reconquest in 1364-1368 are undated. The revolt article says that after May 1364 'the entire western part of Crete was in the hands of the insurgents' and that they gained 'most of the countryside'; the keyframe 'Crete outside Candia' is a fair reading, but the 1367 capture of the Kallergis brothers in Sfakia and the end in 1368 have no regions. Page to try: https://en.wikipedia.org/wiki/Revolt_of_Saint_Titus

### Spot checks

- `/ledger/0` (Kingdom_of_Candia): confirmed (feudal lords rose on 9 August 1363 and declared the 'Republic of Saint Titus'; the revolt 'spread quickly to the rest of the island')
- `/ledger/1` (Kingdom_of_Candia): confirmed (Candia surrendered on 9 May 1364)
- `/ledger/2` (Kingdom_of_Candia): confirmed (infobox 'Revolt of St. Titus: 1363–1368'; the Kallergis brothers captured in April 1367). The quoted sentence is a paraphrase, not verbatim
- `/ledger/3` (Revolt_of_Saint_Titus): confirmed (Venetian rule consolidated over the whole island in 1368)

## Cross-dossier matrix (summary)

### mismatch (12)

- republic-of-venice 1000 gain / kingdom-of-croatia -> kingdom-of-croatia 1018 loss: /ledger/3 the coastal cities of Istria and Dalmatia and the : Croatia dossier: contest 1000-1018, loss of the Dalmatian cities to Venice in 1018, then a contest in 1075-1085 and a loss in 1085. Venice gains in 1000 and holds the cities without a break.
- republic-of-venice 1202 gain / kingdom-of-hungary -> kingdom-of-hungary 1202 contest_start: /ledger/6 Zara recaptured with the Fourth Crusade: Hungary records only a contest_start in 1202, with no loss of Zara.
- republic-of-venice 1207 gain / byzantine-empire -> principality-of-achaea 1209 loss: /ledger/11 Methoni (Modon) and Koroni (Coron): Achaea loses Modon and Coron to Venice in June 1209 (Treaty of Sapienza). Venice dates the gain 1207 and reads the Byzantine Empire as the loser.
- republic-of-venice 1207 gain / byzantine-empire -> duchy-of-the-archipelago 1207 found: /ledger/13 Syros, Paros, Antiparos, Mykonos, Naxos, Milos, An: The Cyclades are the Duchy of the Archipelago's land (found 1207); Venice's direct gain double-claims it.
- republic-of-venice 1388 gain / principality-of-achaea -> lordship-of-argos-and-nauplia 1388 loss: /ledger/28 Nafplio (Nauplia): 1388-1540: The Lordship of Argos and Nauplia sells Nauplia to Venice on 12 December 1388. The Venice counterpart is Achaea.
- republic-of-venice 1394 gain / principality-of-achaea -> despotate-of-the-morea 1394 loss: /ledger/30 Argos: 1394-1462: The Despotate of the Morea loses Argos to Venice in June 1394. The Venice counterpart is Achaea.
- republic-of-venice 1407 gain / albanian-principalities -> despotate-of-arta 1407 loss: /ledger/35 Nafpaktos (Lepanto): 1390, 1407-1499: The Despotate of Arta loses Naupactus to Venice in 1407. The Venice counterpart is albanian-principalities (no dossier).
- republic-of-venice 1409 gain / kingdom-of-hungary -> kingdom-of-hungary 1415 loss: /ledger/37 Zara (Zadar): 1409-1797: Hungary: contest_start 1409 and loss in 1415 (confidence 1, from Cliopatria cells). croatia-in-union-with-hungary loses Dalmatia to Venice in 1409, which matches.
- republic-of-venice 1420 gain / kingdom-of-hungary -> kingdom-of-hungary 1415 loss: /ledger/40 Traù, Spalato and the other Dalmatian cities: Hungary's Dalmatian loss is dated 1415 (confidence 1); Venice dates Trau and Spalato to 1420.
- republic-of-venice 1470 loss / ottoman-empire -> negroponte 1470 dissolve: /ledger/49 Negroponte: 'the whole island then came under Otto: Ottoman dossier has no 1470 Negroponte event against Venice. The negroponte dossier holds the island until July 1470 after its 1390 'rename' to Venetian rule, while the Venice ledger never gains it.
- republic-of-venice 1509 loss / papal-states -> papal-states 1509 contest_start: /ledger/71 Ravenna: 'Julius took Ravenna with Alfonso d'Este': Papal States: contest_start and contest_end in May 1509 for the Romagna, with no gain. Venice never gains Ravenna.
- holy-roman-empire-minor-states 1407 loss / republic-of-venice -> republic-of-venice - -: 48 Veneto cells lost to Venice in 1407 (confidence 1). Venice has the 1404-1405 gains from the Carrara and unnamed lords: a mismatch of years and counterpart.

### missing (72)

- republic-of-venice 1186 loss / kingdom-of-hungary -> kingdom-of-hungary - -: /ledger/5 Zara (Zadar): 998-1186: Hungary's dossier has no gain of Zara in 1186.
- republic-of-venice 1207 gain / byzantine-empire -> byzantine-empire - -: /ledger/12 Corfu (Kerkyra): 1207-1214: The Byzantine 1204 loss names 'many ports and islands ... including Crete', three years earlier and without Corfu.
- republic-of-venice 1278 loss / byzantine-empire -> byzantine-empire - -: /ledger/18 Lemnos: 1207-1278: no mirror in byzantine-empire.
- republic-of-venice 1386 gain / house-of-anjou-sicily -> house-of-anjou-sicily - -: /ledger/27 Corfu: 'came under permanent Venetian rule in 1386: no mirror in house-of-anjou-sicily.
- republic-of-venice 1408 gain / principality-of-achaea -> principality-of-achaea - -: /ledger/36 Patras: 1408-1430: Patras is never lost in the Venice ledger; despotate-of-the-morea gains it from Venice in 1430.
- republic-of-venice 1463 loss / ottoman-empire -> ottoman-empire - -: /ledger/44 Argos: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1464 gain / ottoman-empire -> ottoman-empire - -: /ledger/46 Lemnos: 1464-1479: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1466 gain / ottoman-empire -> ottoman-empire - -: /ledger/47 Imbros, Thasos and Samothrace: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1473 vassal_start / kingdom-of-cyprus -> kingdom-of-cyprus - -: /ledger/51 the Kingdom of Cyprus under the Cornaro queen: The Cyprus dossier has no vassal_start with Venice in 1473.
- republic-of-venice 1479 loss / ottoman-empire -> ottoman-empire - -: /ledger/53 Lemnos: 1464-1479: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1479 loss / ottoman-empire -> ottoman-empire - -: /ledger/54 Imbros, Thasos and Samothrace: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1479 gain / despotate-of-epirus -> despotate-of-epirus - -: /ledger/55 Zakynthos (Zante): 1479-1797: no mirror in despotate-of-epirus.
- republic-of-venice 1479 loss / ottoman-empire -> ottoman-empire - -: /ledger/56 Shkodra, ceded in the Treaty of Constantinople: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1489 vassal_end / kingdom-of-cyprus -> kingdom-of-cyprus - -: /ledger/63 Cyprus: Cyprus ends with a dissolve in February 1489 (counterpart Venice), with no vassal_end. The 1489 gain is matched.
- republic-of-venice 1499 gain / duchy-of-milan -> duchy-of-milan - -: /ledger/64 Cremona: Milan has no 1499 loss of Cremona to Venice.
- republic-of-venice 1499 loss / ottoman-empire -> ottoman-empire - -: /ledger/65 Lepanto: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1500 loss / ottoman-empire -> ottoman-empire - -: /ledger/66 Modon and Coron: 1207-1500: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1500 gain / ottoman-empire -> ottoman-empire - -: /ledger/67 Cephalonia: 1500-1797: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1501 loss / ottoman-empire -> ottoman-empire - -: /ledger/68 Pylos (Navarino): 1417-1501: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1501 loss / ottoman-empire -> ottoman-empire - -: /ledger/69 Durazzo (Durres): 1392-1501: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1503 gain / ottoman-empire -> ottoman-empire - -: /ledger/70 Ithaca: 1503-1797: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1509 loss / holy-roman-empire -> holy-roman-empire - -: /ledger/74 Padua, Verona and Vicenza, 'left undefended and su: no mirror in holy-roman-empire.
- republic-of-venice 1509 gain / holy-roman-empire -> holy-roman-empire - -: /ledger/75 Padua: no mirror in holy-roman-empire.
- republic-of-venice 1509 gain / holy-roman-empire -> holy-roman-empire - -: /ledger/76 Vicenza: no mirror in holy-roman-empire.
- republic-of-venice 1512 loss / kingdom-of-france -> kingdom-of-france - -: /ledger/77 Brescia: no mirror in kingdom-of-france.
- republic-of-venice 1516 loss / kingdom-of-france -> kingdom-of-france - -: /ledger/78 Cremona: no mirror in kingdom-of-france.
- republic-of-venice 1517 gain / kingdom-of-france -> kingdom-of-france - -: /ledger/79 Brescia: no mirror in kingdom-of-france.
- republic-of-venice 1517 gain / holy-roman-empire -> holy-roman-empire - -: /ledger/80 Verona: no mirror in holy-roman-empire.
- republic-of-venice 1522 loss / ottoman-empire -> ottoman-empire - -: /ledger/82 Syros: 1207-1522: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1537 loss / ottoman-empire -> ottoman-empire - -: /ledger/83 Paros, Antiparos and Mykonos: 1207-1537: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1538 loss / ottoman-empire -> ottoman-empire - -: /ledger/84 Skiathos, Skopelos, Alonnisos and Skyros: 1453-153: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1566 loss / ottoman-empire -> ottoman-empire - -: /ledger/86 Naxos, Milos, Andros, Ios, Amorgos, Kimolos, Sikin: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1571 loss / ottoman-empire -> ottoman-empire - -: /ledger/89 Ulcinj (Dulcigno): 1405-1571: The Ottoman 1571 gain is Cyprus only; no Ulcinj.
- republic-of-venice 1576 loss / ottoman-empire -> ottoman-empire - -: /ledger/92 Santorini: 1301-1576: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1617 loss / ottoman-empire -> ottoman-empire - -: /ledger/93 Kythnos and Sifnos: 1207-1617: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1645 loss / ottoman-empire -> ottoman-empire - -: /ledger/95 Chania (Canea), fallen after a siege of 56 days: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1646 loss / ottoman-empire -> ottoman-empire - -: /ledger/96 Rethymno: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1647 gain / ottoman-empire -> ottoman-empire - -: /ledger/97 Novigrad, Klis and (briefly) Knin: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1651 loss / ottoman-empire -> ottoman-empire - -: /ledger/98 Sitia: ca.1210-1651: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1656 gain / ottoman-empire -> ottoman-empire - -: /ledger/99 Tenedos: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1656 gain / ottoman-empire -> ottoman-empire - -: /ledger/100 Lemnos: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1657 loss / ottoman-empire -> ottoman-empire - -: /ledger/101 Lemnos: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1657 loss / ottoman-empire -> ottoman-empire - -: /ledger/102 Tenedos: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1684 gain / ottoman-empire -> ottoman-empire - -: /ledger/105 Santa Maura (Lefkada), captured 6 August 1684: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1685 gain / ottoman-empire -> ottoman-empire - -: /ledger/107 Coron: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1686 gain / ottoman-empire -> ottoman-empire - -: /ledger/111 Sinj: The Ottoman 1687 loss is 'the Morea, with Athens' (confidence 1); there is no Dalmatian event.
- republic-of-venice 1687 gain / ottoman-empire -> ottoman-empire - -: /ledger/114 Herceg Novi (Castelnuovo): 1687-1797: The Ottoman 1687 loss is the Morea only; no Herceg Novi.
- republic-of-venice 1688 gain / ottoman-empire -> ottoman-empire - -: /ledger/115 Risan: 1688-1797: The Ottoman 1687 loss is the Morea only; no Risan.
- republic-of-venice 1688 loss / ottoman-empire -> ottoman-empire - -: /ledger/116 Athens and Attica, evacuated: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1688 gain / ottoman-empire -> ottoman-empire - -: /ledger/117 Knin: The Ottoman 1687 loss is the Morea only; no Knin.
- republic-of-venice 1690 gain / ottoman-empire -> ottoman-empire - -: /ledger/118 Monemvasia: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1690 gain / ottoman-empire -> ottoman-empire - -: /ledger/120 Vrgorac: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1699 gain / ottoman-empire -> ottoman-empire - -: /ledger/121 the Morea, organised as the Kingdom of the Morea, : no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1699 loss / ottoman-empire -> ottoman-empire - -: /ledger/122 Popovo polje, Klek and Sutorina, given up 'to keep: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1715 loss / ottoman-empire -> ottoman-empire - -: /ledger/123 Tinos and Aegina: The Ottoman 1715 gain is 'the Morea' (confidence 2); Tinos and Aegina appear only in its 1714-1718 contest zone.
- republic-of-venice 1715 loss / ottoman-empire -> ottoman-empire - -: /ledger/124 Souda and Spinalonga, the last Venetian outposts o: The Ottoman 1715 gain is the Morea only; no Souda or Spinalonga.
- republic-of-venice 1715 loss / ottoman-empire -> ottoman-empire - -: /ledger/125 Kythira (Cerigo): 1238-1715, 1718-1797: The Ottoman 1715 gain is the Morea only; no Kythira.
- republic-of-venice 1717 gain / ottoman-empire -> ottoman-empire - -: /ledger/130 Preveza: no mirror in the Ottoman dossier (me-10).
- republic-of-venice 1718 gain / ottoman-empire -> ottoman-empire - -: /ledger/131 Kythira (Cerigo): 1718-1797: no mirror in the Ottoman dossier (me-10).
- acciaioli-duchy-of-athens 1390 loss / republic-of-venice -> republic-of-venice - -: Megara ceded to Venice on 22 May 1390; no Venice gain.
- acciaioli-duchy-of-athens 1395 loss / republic-of-venice -> republic-of-venice - -: Venice annexes Athens on 18 March 1395; no Venice gain (the Attica polygon of /keyframe_review/36 is left unexplained).
- acciaioli-duchy-of-athens 1403 gain / republic-of-venice -> republic-of-venice - -: Antonio I retakes Athens from Venice in 1403; no Venice loss.
- byzantine-empire 1423 loss / republic-of-venice -> republic-of-venice - -: Thessalonica handed to Venice in September 1423; no Venice gain.
- ottoman-empire 1430 gain / republic-of-venice -> republic-of-venice - -: Thessaloniki taken from Venice in 1430; no Venice loss.
- despotate-of-the-morea 1430 gain / republic-of-venice -> republic-of-venice - -: Patras taken from Venice in 1430; no Venice loss (Stato da Mar: Patras 1408-1430).
- negroponte 1390 rename / republic-of-venice -> republic-of-venice - -: The last triarch's lands pass to Venice in 1390; no Venice gain of Euboea.
- kingdom-of-hungary 1116 loss / republic-of-venice -> republic-of-venice - -: Venice seizes Biograd, Split, Trogir, Sibenik and Zadar in 1116; Venice holds them from 1000 with no event (croatia-in-union-with-hungary has the same).
- kingdom-of-hungary 1133 gain / republic-of-venice -> republic-of-venice - -: Bela II wins back the cities except Zadar in 1133; no Venice loss (croatia-in-union-with-hungary has the same).
- patriarchate-of-aquileia 1291 loss / republic-of-venice -> republic-of-venice - -: The western Istrian coast passes to Venice in 1291; no Venice gain.
- ambrosian-republic 1447 loss / republic-of-venice -> republic-of-venice - -: Lodi and Piacenza go to Venice in 1447 (confidence 1); no Venice gain.
- duchy-of-milan 1453 gain / republic-of-venice -> republic-of-venice - -: Lodi and Piacenza are retaken from Venice in 1453 (confidence 1); no Venice loss.
- duchy-of-milan 1429 loss / republic-of-venice -> republic-of-venice - -: Crema goes to Venice in 1429 with Bergamo; the Venice 1428 gain has Bergamo only.

### exception (19)

- republic-of-venice 1030 loss / republic-of-ragusa -> republic-of-ragusa - -: /ledger/4 Ragusa (Dubrovnik): 1000-1030: No dossier yet: owned by eu-18, whose part has not run.
- republic-of-venice 1205 gain / republic-of-ragusa -> republic-of-ragusa - -: /ledger/8 Ragusa (Dubrovnik): 1205-1358: No dossier yet: owned by eu-18, whose part has not run.
- republic-of-venice 1238 gain / holder not named by the page -> holder not named by the page - -: /ledger/17 Kythira (Cerigo) and Antikythera (Cerigotto): 1238: The page names no previous holder (author's exception).
- republic-of-venice 1337 gain / Scaliger rulers at Verona -> Scaliger rulers at Verona - -: /ledger/19 the Mestre mainland: No dossier: listed in counterparts_needing_dossiers.
- republic-of-venice 1339 gain / Scaliger rulers at Verona -> Scaliger rulers at Verona - -: /ledger/20 Treviso and Bassano del Grappa: No dossier: listed in counterparts_needing_dossiers.
- republic-of-venice 1392 gain / albanian-principalities -> albanian-principalities - -: /ledger/29 Durazzo (Durres): 1392-1501: No dossier yet: owned by eu-18, whose part has not run.
- republic-of-venice 1396 gain / albanian-principalities -> albanian-principalities - -: /ledger/31 Scutari (Shkoder): 1396-1479: No dossier yet: owned by eu-18, whose part has not run.
- republic-of-venice 1404 gain / holder not named by the page -> holder not named by the page - -: /ledger/32 Vicenza, Belluno and Feltre: The page names no previous holder (author's exception).
- republic-of-venice 1405 gain / Carrara lordship of Padua -> Carrara lordship of Padua - -: /ledger/33 Padua, Verona and Este: No dossier: listed in counterparts_needing_dossiers.
- republic-of-venice 1405 gain / holder not named by the page -> holder not named by the page - -: /ledger/34 Ulcinj (Dulcigno): 1405-1571: The page names no previous holder (author's exception).
- republic-of-venice 1417 gain / holder not named by the page -> holder not named by the page - -: /ledger/38 Pylos (Navarino): 1417-1501: The page names no previous holder (author's exception).
- republic-of-venice 1420 gain / Commune of Kotor (page names no ruler) -> Commune of Kotor (page names no ruler) - -: /ledger/41 Kotor (Cattaro) and Perast: 1420-1797: The page names no ruler; no polity.
- republic-of-venice 1464 gain / holder not named by the page -> holder not named by the page - -: /ledger/45 Monemvasia: 1464-1540: The page names no previous holder (author's exception).
- republic-of-venice 1482 gain / duchy-of-ferrara -> duchy-of-ferrara - -: /ledger/59 Rovigo: No dossier: listed in the author's counterparts_needing_dossiers (eu-13-x).
- republic-of-venice 1484 gain / duchy-of-ferrara -> duchy-of-ferrara - -: /ledger/60 the town of Rovigo and a broad swath of the fertil: No dossier: listed in the author's counterparts_needing_dossiers (eu-13-x).
- republic-of-venice 1509 loss / duchy-of-ferrara -> duchy-of-ferrara - -: /ledger/72 the Polesine, seized by Alfonso d'Este: No dossier: listed in the author's counterparts_needing_dossiers (eu-13-x).
- republic-of-venice 1796 occupation_start / french-directory -> french-directory - -: /ledger/132 Venetian territory up to the Adige: French Directory row exists in polities.csv but no dossier yet (owner group not run).
- republic-of-venice 1797 occupation_end / french-directory -> french-directory - -: /ledger/133 Venetian territory up to the Adige: French Directory row exists in polities.csv but no dossier yet (owner group not run).
- habsburg-monarchy 1797 gain / republic-of-venice -> republic-of-venice - -: Habsburg gains Venice and its lands in October 1797 with Venice as counterpart, after Venice's dissolve in May 1797. An exception: a successor hand-over, recorded in Venice's successors.

### matched (23)

- republic-of-venice 1205 gain / byzantine-empire -> byzantine-empire 1204 loss: /ledger/7 Dyrrhachium, the province of Dyrrhachium and Arban
- republic-of-venice 1205 gain / byzantine-empire -> byzantine-empire 1204 loss: /ledger/9 Crete, bought from Boniface of Montferrat
- republic-of-venice 1213 loss / despotate-of-epirus -> despotate-of-epirus 1213 gain: /ledger/15 Durazzo (Durres): 1205-1213
- republic-of-venice 1214 loss / despotate-of-epirus -> despotate-of-epirus 1213 gain: /ledger/16 Corfu (Kerkyra): 1207-1214
- republic-of-venice 1358 loss / kingdom-of-hungary -> kingdom-of-hungary 1358 gain: /ledger/22 all Venetian possessions in Dalmatia 'from the Kva
- republic-of-venice 1363 loss / republic-of-saint-titus -> republic-of-saint-titus 1363 found: /ledger/24 Crete, taken by the rebel 'Republic of Saint Titus
- republic-of-venice 1364 gain / republic-of-saint-titus -> republic-of-saint-titus 1364 loss: /ledger/25 Candia, retaken by Venice on 9 May 1364
- republic-of-venice 1368 gain / republic-of-saint-titus -> republic-of-saint-titus 1368 loss: /ledger/26 the rest of Crete after the revolt
- republic-of-venice 1420 gain / patriarchate-of-aquileia -> patriarchate-of-aquileia 1419 loss: /ledger/39 the Friulian territories of the Imperial Patriarch
- republic-of-venice 1426 gain / duchy-of-milan -> duchy-of-milan 1426 loss: /ledger/42 Brescia
- republic-of-venice 1428 gain / duchy-of-milan -> duchy-of-milan 1429 loss: /ledger/43 Bergamo
- republic-of-venice 1489 gain / kingdom-of-cyprus -> kingdom-of-cyprus 1489 dissolve: /ledger/62 'In February 1489, the island of Cyprus, previousl
- republic-of-venice 1540 loss / ottoman-empire -> ottoman-empire 1540 gain: /ledger/85 Nauplia and Monemvasia: 'Nafplio 1388-1540; Monemv
- republic-of-venice 1570 loss / ottoman-empire -> ottoman-empire 1571 gain: /ledger/88 Nicosia
- republic-of-venice 1571 loss / ottoman-empire -> ottoman-empire 1571 gain: /ledger/90 Famagusta and the rest of Cyprus: 'with ammunition
- republic-of-venice 1669 loss / ottoman-empire -> ottoman-empire 1669 gain: /ledger/103 Crete, except the island fortresses of Souda, Gram
- republic-of-venice 1686 gain / ottoman-empire -> ottoman-empire 1687 loss: /ledger/108 Navarino (old surrendered the day after the 2 June
- republic-of-venice 1686 gain / ottoman-empire -> ottoman-empire 1687 loss: /ledger/109 Modon
- republic-of-venice 1686 gain / ottoman-empire -> ottoman-empire 1687 loss: /ledger/110 Nauplia
- republic-of-venice 1687 gain / ottoman-empire -> ottoman-empire 1687 loss: /ledger/112 Corinth
- republic-of-venice 1687 gain / ottoman-empire -> ottoman-empire 1687 loss: /ledger/113 Athens
- republic-of-venice 1715 loss / ottoman-empire -> ottoman-empire 1715 gain: /ledger/127 Nauplia, stormed on 20 July 1715 after nine days
- republic-of-venice 1715 loss / ottoman-empire -> ottoman-empire 1715 gain: /ledger/128 the whole Peloponnese retaken 'within a hundred da

## Notes on the author's notes

The author's notes flag the Attica polygon, Thessalonica, Dalmatia 1102-1133, Ravenna/Crema, the Istrian coast, the Cyclades and Duchy overlap, and the missing area, which is honest. They do not flag four things: the Lombard loss of 1509 (the 1509 keyframe contradicts the Cambrai page), the Cretan countryside in 1647-1668, the unpaired Polesine, Euboea, Patras, Aegina and Sporades events, or the neighbour dossiers (Acciaioli Athens, Lordship of Argos and Nauplia, Despotate of the Morea, Despotate of Arta, Negroponte) that already give page-cited counterparts. A one-state dossier for Venice (697-1797, not split) is accepted: one article, one Wikidata id, and no break in the state.
