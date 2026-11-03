# Review of batch me-10-b (2026-10-25)

Dossiers: safavid-dynasty (fail), yarubid-dynasty (thin), qasimids (thin). Machine copy: history/notes/phase-b/reviews/me-10-b.json.

The validator (`--resolve`) reports 0 errors. Its only warnings are three for Julfar, a place missing from the gazetteer (yarubid-dynasty).

## safavid-dynasty: fail

Spot checks (Abbas I, Tahmasp I, Safavid Iran, Treaty of Constantinople (1724), Campaigns of Nader Shah):
- Confirmed: 1590 cession, Bahrain 1602, Hormuz 1622, Khorasan 1510, Kandahar 1558, partition of 12 June 1724, Yerevan June 1604, Mashhad April 1598.
- Area check: 2.9 M km2 (1630) against Cliopatria's 2.81 M km2 (ratio 0.97). The author acknowledged it.

Blocking findings, not applied:
1. **Kandahar 1595-1622.** No loss to the Mughals is entered, so Kandahar is gained twice (1558 and 1622). Keyframes 16-19 keep it until 1621. The notes say no page dates the loss, but the author's own Abbas I page says "In 1590 ... Akbar seized Kandahar", and mughal-empire /ledger/58 has 18 April 1595 at confidence 3. Cliopatria's Mughal shapes for 1595-1625 reach 64.6 E, so Kandahar is drawn twice. Fix: add the 1595-04 loss and subtract Kandahar in keyframes 16-19; set /ledger/39 to month 6.
2. **Kandahar 1638-1653.** The 1638 loss (Ali Mardan Khan), the 22 February 1649 recapture and the Mughal sieges of 1649-1653 are missing (mughal-empire /ledger/73 and /ledger/79-81, page Mughal-Safavid war (1649-1653)). Keyframes 21-23 hold Kandahar through 1638-1648. Fix: add the events and the war, and subtract Kandahar from those keyframes.
3. **/keyframe_review/30.** The correction for 1729-1733 is the whole Hotaki 1727 shape, which contains the Hotaki 1734 shape (Kandahar, Sistan and Baluchistan, 552,000 km2) that hotaki-dynasty keeps after 1729. Fix: minus [Hotaki 1727, Hotaki 1734], which matches hotaki /ledger/17 and the dossier's own /ledger/58.
4. **1606-1612.** The land ceded in 1590 (Karabakh, Shirvan, Dagestan, West Azarbaijan, Lorestan) is never regained, yet Shirvan, Baku and Derbent are lost again in 1723. The Abbas I page has Abbas regain "South Caucasus and Dagestan" by the end of the 1603-1618 war. ottoman-empire /ledger/100 (June 1606: Ganja, Baku, Shirvan, Shamakhi) and /ledger/102 (Nasuh Pasha, 20 November 1612) are the mirrors. Keyframe 18 (+459,000 km2) is marked ok without them. Fix: add the 1606-06 and 1612-11 gains, and extend war /wars/5 to 1618.

Other fixes:
- /ledger/64, mis-dated at confidence 2. Tabriz was retaken on 12 August 1730, and Hamadan and Kermanshah in the same campaign; Tahmasp's treaty kept them (Campaigns of Nader Shah). Only the Caucasus came back in 1734-1735. Fix: split into a 1730-08 gain and a 1735 gain.
- /ledger/22, **applied by the reviewer.** Month 6 removed: the Tahmasp I page gives only "the Peace of Amasya in 1555". Re-validated: 0 errors.
- /ledger/3: the counterpart is free text. Use "nobody".

Thin (for a gap-filler):
- Confidence 1 events: Ottoman annexation 1516, Shirvan 1501 and 1539, Tabriz 1514, Khorasan 1589.
- Ottoman conquests of 1578-1585 (the dossier has only the 1590 treaty).
- The 1713 drop of 547,000 km2 and the 1718 change (hotaki /ledger/3 and /ledger/4); Abdali Herat 1716/17-1732.
- Merv 1593-1600 (khanate-of-bukhara /ledger/14 and /ledger/21).
- Balkh and Khwarezm 1510-1511 (shaybanids; khanate-of-khiva).
- Bahrain lost to the Ya'rubids about 1717.
- Kandahar 1545.

## yarubid-dynasty: thin

Spot checks:
- Confirmed: Julfar 1633, Sohar 1643, Fort Jesus 13 December 1698 and the coast with Zanzibar and Pemba, Muscat to the Persians 1743, Bal'arab's death 1749, Portuguese expelled from Oman 1650 (confidence 2).
- No infobox area, so the area check could not be made. The author says so.

Keyframes and ledger agree: Muscat explains 1653, the Swahili coast explains 1700, and keyframes 1741 and 1744 are adjusted with events.

Thin:
- Bahrain taken "from the Persians" and held "for several years". This is on the author's own Ya'rubids page, undated, with no event and no Safavid mirror.
- Mombasa 1728/1729: there is no regain.
- 1744: the Swahili coast passes at confidence 1.
- No seat is given for 1719-1742.
- Predecessors are empty.

Fix: /wars/2 (civil war 1718-1724) has empty zones without saying that no ground changed hands.

Cross-check: portuguese-empire (am-06) records the 1698 loss to yarubid-dynasty, while this dossier names kingdom-of-portugal (eu-12, which the seed also names). The orchestrator should settle which one owns the posts.

## qasimids: thin

Spot checks:
- Confirmed: highlands 1608, Sana'a 1628, Zabid 1634, Aden 1644, Hadramawt 1654, Dhofar suzerainty 1658, Lahej "1728 or 1731".
- No infobox area. The author says so.

Thin:
- **/keyframe_review/8.** The 1683 shape (166,000 km2, east edge 45.82 E) is 47,000 km2 smaller than the direct land of 1645-1658 (213,000 km2, 47.06 E). Land east of 45.8 E (Yafa', al-Bayda, Bayhan) is lost with no event; the dossier has only the vassal_end events of Hadramawt and Dhofar.
- Confidence 1 events: 1597, 1683 (two) and 1813.
- No capital is given for 1597-1627.

Fixes:
- /wars/2 has empty zones without a note.
- The "Dhofar (local rulers)" counterpart is not listed.

Cross-check: ottoman-empire puts the loss of Yemen in 1636, against the Qasimid gains of 1608, 1628 and 1634.

## Mirrors missing in neighbour dossiers (for routing)

- **ottoman-empire:** Yerevan 1635/1636; the 1724 partition at 1727 (confidence 1); the 1735/1736 recovery named afsharid-iran; Yemen 1608-1634.
- **portuguese-empire:** Bahrain 1602; Hormuz 1622.
- **khanate-of-bukhara:** Khorasan 1524 and 1528.

Not yet written (counted as exceptions): eu-19 (the Georgian kingdoms, shirvan), eu-12 (kingdom-of-portugal, iberian-union) and eu-17 (russian-empire).
