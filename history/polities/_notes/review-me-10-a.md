# Review of batch me-10-a (ottoman-empire)

Reviewer run of 2026-10-25 (adversarial review, Phase B). One dossier: `history/polities/ottoman-empire.json`. Verdict: **fail** - back to the author for the unapplied findings below. Not broken: no fabricated or mis-dated confidence-3 event was found in 28 confidence-3 spot checks on seven pages; the validator gives 0 errors; areas are within a factor 1.5 of the infobox.

## Reviewer edits applied in place

Six year fixes, each verified on the page named, with four sources added (14 to 18) and the ledger re-sorted (old /ledger/74 is now /ledger/78, old 123 is 122, old 195 is 194). Pointers in this file refer to the edited dossier. Re-validated: 0 errors, the same 2 vassal-pairing warnings.

- `/ledger/194`: Bulgarian independence dated 1912 at confidence 1 ('page silent'); it was declared in 1908. Evidence: Balkan Wars page (already the event's source), 1908 paragraph: 'Bulgaria declared independence as it had done in 1878, but this time the independence was internationally recognized'; Ottoman recognition 'in April 1909'. Done: Year 1908, confidence 2, note rewritten with the quote; event moved from /ledger/195 to keep the ledger sorted.
- `/ledger/83`: Ottoman gain of Tunisia from hafsid-dynasty dated 1572 (Cliopatria's year, confidence 1). Evidence: Hafsid dynasty page: 'The Ottomans again conquered Tunis in 1569 and held it for four years'; 'Don Juan of Austria recaptured it in 1573'; 'the final Ottoman conquest of Tunis in 1574 put an end to their reign.' The hafsid-dynasty dossier dissolves in 1574 with counterpart ottoman-empire. Done: Year 1574, confidence 2, source https://en.wikipedia.org/wiki/Hafsid_dynasty (added to sources[]), note rewritten.
- `/ledger/78`: Massawa gain dated 1554 from the Eyalet table (confidence 2); the conquest was 1557. Evidence: Ethiopian Empire page: 'From 1557, the Ottoman Empire occupied parts of Ethiopia, establishing Habesh Eyalet'; 'It was constituted by the conquest of Massawa'. ethiopian-empire /ledger/20 has the 1557 loss. Done: Year 1557, source https://en.wikipedia.org/wiki/Ethiopian_Empire (added to sources[]), note rewritten; event moved from /ledger/74.
- `/ledger/122`: Beylik of Tunis vassal_start dated 1706 (Cliopatria's year, confidence 1); the Husainid coup was July 1705. Evidence: Beylik of Tunis page: 'on 10 July 1705 of a coup of Al-Husayn I ibn Ali' (infobox 15 July 1705); 'formally part of the Ottoman Empire'. beylik-of-tunis found is July 1705. Done: Year 1705, month 7, confidence 2, source https://en.wikipedia.org/wiki/Beylik_of_Tunis (added to sources[]); event moved from /ledger/123.
- `/ledger/124`: Karamanli vassal_start dated 1713 (Cliopatria's year, confidence 1); the coup was 1711. Evidence: Karamanli dynasty page: 'murdered the Ottoman governor of Tripolitania and seized the throne in the 1711 Karamanli coup'; Tripolitania 'continued to pay nominal tribute to the Ottoman padishah'. karamanli-dynasty found 1711. Done: Year 1711, confidence 2, source https://en.wikipedia.org/wiki/Karamanli_dynasty (added to sources[]).
- `/ledger/172`: Karamanli vassal_end dated 1836 (Cliopatria's year, confidence 1); Ali II was deposed in May 1835. Evidence: Karamanli dynasty page: Mahmud II 'deposed and exiled Ali II, marking the end of both the Karamanli dynasty and an independent Tripolitania'; Ali II's reign ends 26 May 1835 in its ruler list (the infobox's 1832 conflicts). karamanli-dynasty dissolves 1835. Done: Year 1835, month 5, confidence 2, source Karamanli dynasty page.

## Findings for the author (not applied)

- `/keyframe_review/46/correction`: The 1609 correction (Cliopatria 1609 plus Iraq) keeps Yerevan, Tbilisi and Shirvan/Baku, which the ledger loses in 1604 (/ledger/93: 'Yerevan and Shirvan'); /ledger/95 then loses the same Caucasus block a second time in 1612 as C1611 minus C1612.
  - Evidence: H3 check with tools/grid.py: Cliopatria 1609 contains the Yerevan, Tbilisi and Baku cells (Tabriz, Baghdad, Basra removed); 1612 drops them. The correction and the ledger disagree for 1609-1611 and the land is lost twice.
  - Fix: Make them agree: either subtract Erevan and Shirvan (and whatever else the 1604-1607 Safavid reconquest took) from the 1609 correction and limit /ledger/95 to what was still Ottoman in 1611 (Georgia/Childir), or narrow /ledger/93 to the Yerevan fortress and say in the note that Cliopatria keeps the rest to 1612. Each piece of land must be lost once.
- `/keyframe_review/20`: The Morea's conquest (May 1460) is missing: the 1463 keyframe adds about 73 Peloponnese cells (none in 1458, 6 in 1459) with no ledger event, and its note names only Bosnia and Trebizond. In the same stretch /ledger/43 (1459, confidence 1, a C1459 minus C1458 difference) gives the 48 Greek cells it adds (Attica and Boeotia, the Duchy of Athens taken 1456-58) to serbian-despots.
  - Evidence: byzantine-empire /ledger/199: '29 May 1460: the Morea falls ... infobox Ottoman conquest: 29 May 1460' (loss to ottoman-empire, confidence 3), with no Ottoman mirror. Grid counts from tools/grid.py: Peloponnese cells 0 (1458), 6 (1459), 79 (1463).
  - Fix: Add a gain of the Peloponnese from byzantine-empire in 1460 (month 5), citing a page that dates it (Byzantine Empire or Despotate of the Morea); say in the 1459 keyframe note that the Morea is Ottoman from 1460 though Cliopatria adds it in 1463; split the Greek part out of /ledger/43 as a 1456/1458 gain from the Duchy of Athens (already in counterparts_needing_dossiers).
- `/ledger/115`: 1696 loss of 'Podolia and the Azov coast' to polish-lithuanian-commonwealth (confidence 1, Cliopatria's year) duplicates /ledger/119 (Podolia, 1699) and /ledger/121 (Azov to tsardom-of-russia, 1700), and gives Azov to the wrong state.
  - Evidence: The event's own note: 'The Eyalet page ends Podolia in 1699 and the Russo-Turkish wars page has Russia gaining Azov in 1700, so the date is the shape's, not a page's.' Podolia and Azov are lost twice in the ledger.
  - Fix: Delete /ledger/115, or keep only Azov as a 1696 loss to tsardom-of-russia (Peter's capture, from a page that dates it) and make /ledger/121 the 1700 cession note; mark /keyframe_review/60 (1696) adjust with Podolia kept to 1699; explain the 45 Croatian cells Cliopatria drops in 1696 or say they are unexplained.
- `/keyframe_review/75`: The 1772 keyframe drops the 10 Crimean-coast cells (the Kaffa Eyalet); the correction restores only a 60 km disc at Kerch and no ledger event gives the rest away.
  - Evidence: crimean-khanate /ledger/10 (confidence 3): 'November 1772: the khanate takes the former Kaffa Eyalet ... Treaty of Karasu Bazaar', a gain from ottoman-empire with no Ottoman mirror. Grid: Crimea-box cells 10 (1769), 0 (1772).
  - Fix: Add a 1772 (November) loss of the Kaffa Eyalet (southern Crimean coast minus Kerch and Yenikale) to crimean-khanate, citing the Crimean Khanate page, or explain why the coast stays Ottoman to 1774.
- `/wars/34`: Russo-Turkish War (1828-1829) has empty zones and no ledger events although its own outcome says Russia 'receives the Black Sea coast of the Caucasus and western Georgia'.
  - Evidence: Brief section 2 item 10: empty zones only where no ground changed hands. The outcome text (from the Russo-Turkish wars page) names ceded land; the ledger has no 1828 contest_start, 1829 contest_end or 1829 loss.
  - Fix: Add contest_start 1828 / contest_end 1829 and a 1829 loss to russian-empire (Akhaltsikhe and Akhalkalaki, Anapa, Poti, the Danube delta) with zones; Cliopatria does not draw these as Ottoman, so say so in the note.
- `/ledger/31`: Wallachia has vassal_start in 1395 (/ledger/21) and again in 1419 with no vassal_end between (validator warning).
  - Evidence: Rise page: 'Mehmed wrested the region back in 1419 ... forcing Wallachia back into vassalage' - the vassalage lapsed after Ankara (1402).
  - Fix: Add a vassal_end with principality-of-wallachia about 1402 (confidence 2, Rise page) so the pairs read 1395-1402 and 1419-1878.
- `/ledger/122`: The Beylik of Tunis vassal relation has no end (validator warning); the author says no page dated the French protectorate.
  - Evidence: Beylik of Tunis page (now in sources[]): 'On 12 May 1881, the protectorate was formalized ... signed the Bardo Treaty'; infobox 'Protectorate established: 12 May 1881'.
  - Fix: Add vassal_end 1881, month 5, counterpart beylik-of-tunis, region Tunisia, confidence 3, source https://en.wikipedia.org/wiki/Beylik_of_Tunis.
- `/keyframe_review/45`: The 1602-1608 keyframe is 'ok' but spans the 1603 loss of the Tabriz block (/ledger/92, about 1,141 cells) and the 1604 Yerevan/Shirvan loss; likewise /keyframe_review/47 (1612-1625, 'ok') spans the January 1624 loss of Baghdad and Iraq.
  - Evidence: Brief section 2 item 4: an event inside one shape's span is fine only if small or the keyframe is marked adjust for it; these are large.
  - Fix: Mark both adjust with a note that the shape lags the ledger (Tabriz lost 1603, Baghdad 14 January 1624), or say in the note that the ledger overrides the shape for those years.
- `/notes`: The infobox areas were not compared anywhere in the dossier.
  - Evidence: Infobox: 1481 1,220,000 km2; 1521 3,400,000; 1683 5,200,000; 1913 2,550,000. Cliopatria alive then: 905k (1475-1481), 2,783k (1521-1525), 3,593k (1683-1686), 1,930k (1913-1914); ratios 1.35, 1.22, 1.45, 1.32 - under two, so not a fault, but brief item 5 asks for the comparison.
  - Fix: Add one sentence with these figures to the notes or the 1683 keyframe note.

## Gaps for a gap-filler (thin)

- `/identity/rulers`: No rulers list (author's gap). Try: https://en.wikipedia.org/wiki/List_of_sultans_of_the_Ottoman_Empire
- `/ledger/149`: Egypt's return dated 1803 (Cliopatria's year, confidence 1); the French evacuated Egypt in 1801. Try: https://en.wikipedia.org/wiki/French_campaign_in_Egypt_and_Syria
- `/ledger/159`: Serbia back in the Ottoman shape 1814 (confidence 1); the First Serbian Uprising was crushed in 1813. Try: https://en.wikipedia.org/wiki/First_Serbian_Uprising
- `/ledger/176`: Yemen regained 1873 (Cliopatria's year, confidence 1); Sana'a was taken in 1872. Try: https://en.wikipedia.org/wiki/Yemen_Vilayet
- `/ledger/177`: Al-Hasa, Qatar and Kuwait gained 1873 (confidence 1); the Ottoman al-Hasa expedition was 1871. Try: https://en.wikipedia.org/wiki/Ottoman_expedition_to_al-Hasa
- `/ledger/192`: Kuwait lost 1900 (confidence 1); the Anglo-Kuwaiti Agreement is 1899. Try: https://en.wikipedia.org/wiki/Anglo-Kuwaiti_Agreement_of_1899
- `/ledger/193`: Crete lost 1900 (confidence 1); the Cretan State dates from 1898. Try: https://en.wikipedia.org/wiki/Cretan_State
- `/ledger/52`: Moldavian coast gained 1487 (confidence 1); Kilia and Akkerman fell in 1484. Try: https://en.wikipedia.org/wiki/Stephen_the_Great
- `/ledger/58`: Yemen gained 1517 (Eyalet table grouping, confidence 1); the conquest ran 1538-1547 (Aden 1538). Try: https://en.wikipedia.org/wiki/Ottoman_Yemen
- `/ledger/23`: Sivas block gained 1395 (confidence 1, no page); Bayezid took Sivas after Kadi Burhan al-Din's death (1398). Try: https://en.wikipedia.org/wiki/Kadi_Burhan_al-Din
- `/ledger/9`: Ankara (Ahi) block gained 1363 (Cliopatria difference, confidence 1); Orhan took Ankara about 1354. Try: https://en.wikipedia.org/wiki/Orhan
- `/ledger/49`: 1475 Cliopatria difference (confidence 1) gives Euboea (Negroponte, Venetian until 1470) as well as Caffa to republic-of-genoa; a 1470 gain of Negroponte from republic-of-venice is missing. Try: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Venetian_War_(1463%E2%80%931479)
- `/ledger/63`: 1526 Cliopatria difference (confidence 2) includes Rhodes, which fell to the Ottomans from the Knights Hospitaller in 1522; no Rhodes event. Try: https://en.wikipedia.org/wiki/Siege_of_Rhodes_(1522)
- `/ledger/83`: The Ottoman occupations of Tunis 1534-1535 and 1569-1573 that hafsid-dynasty records are absent (small, inside the Hafsid shape). Try: https://en.wikipedia.org/wiki/Hafsid_dynasty
- `/keyframe_review/84`: Cliopatria drops 530 Arabian cells in 1796 (keyframe 'unverified: page budget'); no event. Try: https://en.wikipedia.org/wiki/Emirate_of_Diriyah
- `/ledger/133`: The 1727 Persian block (about 1,213 cells, confidence 1) is undated on any page; the Treaty of Hamadan (1727) is the likely source. Try: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Hotaki_War_(1726%E2%80%931727)
- `/ledger/223`: Eastern Thrace to Greece 1920 and Smyrna recovered 1922 (/ledger/225) are confidence 1 on the Partition page, which is silent on both. Try: https://en.wikipedia.org/wiki/Greco-Turkish_War_(1919%E2%80%931922)
- `/ledger/213`: Palestine (1917, confidence 2) and Iraq (1917, /ledger/214, confidence 1): the Partition page names neither Baghdad nor Jerusalem. Try: https://en.wikipedia.org/wiki/Mesopotamian_campaign
- `/ledger/191`: Eastern Rumelia's union with Bulgaria 1885 at confidence 1. Try: https://en.wikipedia.org/wiki/Unification_of_Bulgaria
- `/keyframe_review`: 33 keyframe verdicts 'Unverified: page budget' (1482-1512, 1645-1662, 1727, 1776-1828, 1853-1911); not faults under this run's rules, but the 1796 and 1825 drops in them are unexplained. Try: https://en.wikipedia.org/wiki/Ottoman_Empire

## Spot checks

- `/ledger/98` (Ottoman%E2%80%93Safavid_War_(1623%E2%80%931639)): confirmed: 'the Persians besieged Baghdad and took it on 14 January 1624'
- `/ledger/97` (Ottoman%E2%80%93Safavid_War_(1623%E2%80%931639)): confirmed (same sentence)
- `/ledger/68` (Ottoman_Empire): confirmed: 'the Ottoman Turks took Baghdad from the Persians in 1535'
- `/ledger/171` (Ottoman_Empire): confirmed: Convention of Kütahya 'signed on 5 May 1833'; vali of Crete, Aleppo, Tripoli, Damascus and Sidon; t
- `/ledger/211` (Ottoman_Empire): confirmed: 'the revolt was officially initiated at Mecca on 10 June 1916'
- `/ledger/221` (Ottoman_Empire): confirmed: 'In May 1919, Greece also took control of the area around Smyrna'
- `/ledger/106` (Ottoman_Empire): confirmed: 'the conquest of Crete completed in 1669'
- `/ledger/82` (Ottoman_Empire): confirmed: Nicosia besieged 22 July 1570; Famagusta 'fell to the Ottomans in August 1571'
- `/ledger/156` (Muhammad_Ali_of_Egypt): confirmed: 'a second attack was launched in 1812 that succeeded in recapturing Hejaz'
- `/ledger/152` (Muhammad_Ali_of_Egypt): confirmed: 'in 1805 he was named Wāli (governor) of Egypt'
- `/ledger/15` (Rise_of_the_Ottoman_Empire): confirmed: 'Murad captured Niš in 1386'
- `/ledger/21` (Rise_of_the_Ottoman_Empire): confirmed: 'Mircea accepted vassalage under Bayezid' (1395)
- `/ledger/31` (Rise_of_the_Ottoman_Empire): confirmed: 'Mehmed wrested the region back in 1419 ... forcing Wallachia back into vassalage'
- `/ledger/14` (Rise_of_the_Ottoman_Empire): confirmed: 'in 1385 Murad took Sofia'
- `/ledger/16` (Rise_of_the_Ottoman_Empire): confirmed: 'took and occupied Thessaloniki in 1387'
- `/ledger/1` (Rise_of_the_Ottoman_Empire): confirmed: 'Bursa (Prusa) was conquered in 1326'
- `/ledger/17` (Rise_of_the_Ottoman_Empire): confirmed: Stefan Lazarević 'concluded a vassal agreement with Bayezid in 1390'
- `/ledger/24` (Rise_of_the_Ottoman_Empire): confirmed: after Nicopolis, 'With Vidin's fall, Bulgaria ceased to exist'
- `/ledger/220` (Partition_of_the_Ottoman_Empire): confirmed: 'occupied Kars on 19 April 1919'; 'placed Kars province under Armenian rule'
- `/ledger/215` (Partition_of_the_Ottoman_Empire): confirmed: 'The Mutawakkilite Kingdom of Yemen became independent in 1918'
- `/ledger/117` (Ottoman%E2%80%93Habsburg_wars): confirmed: Karlowitz 'secured ... the rest of Hungary and overlordship of Transylvania for the Austrians'
- `/ledger/131` (Ottoman%E2%80%93Habsburg_wars): confirmed: Passarowitz gave 'the Banat of Temeswar, Serbia and Oltenia'
- `/ledger/139` (Ottoman%E2%80%93Habsburg_wars): confirmed: Belgrade 1739 ceded 'Serbia (including Belgrade), the southern part of the Banat of Temeswar and no
- `/ledger/104` (Ottoman%E2%80%93Habsburg_wars): confirmed: in 1663 the Ottomans 'conquered the fortress of Nové Zámky'
- `/ledger/112` (Ottoman%E2%80%93Habsburg_wars): confirmed: 'The Christian forces reconquered Buda' in 1686
- `/ledger/89` (Ottoman%E2%80%93Habsburg_wars): confirmed: 'In 1596 Eger fell to the Ottomans'
- `/ledger/70` (Ottoman%E2%80%93Habsburg_wars): confirmed: 'the seizure of Buda by the Turks in 1541'
- `/ledger/207` (Balkan_Wars): confirmed: the Ottomans 'advanced in Thrace, regaining Adrianople' (Second Balkan War, 1913)
- `/ledger/194` (Balkan_Wars): mis-dated (confidence 1): the page puts Bulgarian independence in 1908, not 1912; fixed by the reviewer

## Area check

Infobox 5,200,000 km2 in 1683 against Cliopatria 3,593,000 km2 (ratio 1.45); 1481: 1,220,000 vs 905,000 (1.35); 1521: 3,400,000 vs 2,783,000 (1.22); 1913: 2,550,000 vs 1,930,000 (1.32); all under two. Not acknowledged in the dossier (a fix, not a fault).

## Cross-dossier matrix

Existing counterpart dossiers checked: byzantine-empire, crimean-khanate, ethiopian-empire, hafsid-dynasty, regency-of-algiers, beylik-of-tunis, karamanli-dynasty, emirate-of-diriyah, afsharid-iran, mamluk-sultanate, empire-of-trebizond, despotate-of-epirus. Context polities with no dossier yet count as exceptions (their groups have not written them).

- **matched** - byzantine-empire: 1326 gain /ledger/1 <-> 1326 loss /ledger/169; 1331 gain /ledger/2 <-> 1331 loss /ledger/171; 1354 gain /ledger/6 <-> 1354 loss /ledger/181; 1370 gain /ledger/10 <-> 1369 loss /ledger/184; 1387 gain /ledger/16 <-> 1387 loss /ledger/186; 1402 loss /ledger/26 <-> 1403 gain /ledger/189; 1453 gain /ledger/40 <-> 1453 loss /ledger/197
- **matched** - despotate-of-epirus: 1431 gain /ledger/37 <-> 1430 loss /ledger/59
- **matched** - empire-of-trebizond: 1461 gain /ledger/45 <-> 1461 loss /ledger/39
- **matched** - mamluk-sultanate: 1516 gain /ledger/56 <-> 1516 loss /ledger/41; 1516 gain /ledger/57 <-> 1516 loss /ledger/41; 1517 gain /ledger/58 <-> 1516 loss /ledger/41; 1517 gain /ledger/59 <-> 1516 loss /ledger/41; 1517 gain /ledger/60 <-> 1516 loss /ledger/41
- **matched** - ethiopian-empire: 1557 gain /ledger/78 <-> 1557 loss 
- **matched** - hafsid-dynasty: 1574 gain /ledger/83 <-> 1574 dissolve 
- **matched** - afsharid-iran: 1736 loss /ledger/136 <-> 1736 gain /ledger/0
- **matched** - emirate-of-diriyah: 1803 loss /ledger/150 <-> 1802 gain /ledger/10; 1805 loss /ledger/151 <-> 1804 gain /ledger/15
- **mismatch** - 1363 gain /ledger/7 with byzantine-empire: Adrianople: the Rise page dates it 1362-3 (ottoman /ledger/7, conf 2); the byzantine-empire dossier has 'Adrianople succumbing to the Ottomans in 1369' (/ledger/184, conf 3) and matches it against ottoman /ledger/10 (1370). Sources disagree; one date should be chosen in both and the other noted.
- **missing** - 1371 vassal_start /ledger/11 with byzantine-empire: byzantine-empire has no vassal_start with ottoman-empire after the Maritsa (1371); its own note mentions the vassal status. Route to eu-05.
- **missing** - 1453 vassal_end /ledger/41 with byzantine-empire: byzantine-empire has no vassal_end with ottoman-empire in 1453 (it records the 1453 loss and runs to 1460 in the Morea). Route to eu-05.
- **missing** - 1475 vassal_start /ledger/50 with crimean-khanate: crimean-khanate has no vassal_start with ottoman-empire (1475/1478). Route to ia-02.
- **mismatch** - 1705 vassal_start /ledger/122 with beylik-of-tunis: Year now agrees (reviewer moved 1706 to July 1705). beylik-of-tunis records a found event, not a vassal_start; and the Ottoman side lacks the vassal_end of 12 May 1881 (Bardo).
- **mismatch** - 1706 vassal_start /ledger/123 with regency-of-algiers: regency-of-algiers records its 1706 start as a found event with counterpart ottoman-empire, not a vassal_start. Route to the regency's group to add the vassal relation 1706-1830.
- **mismatch** - 1711 vassal_start /ledger/124 with karamanli-dynasty: Year now agrees (reviewer moved 1713 to 1711). karamanli-dynasty records found (1711) and a 1713 'gain from ottoman-empire' (Cyrenaica, conf 1), not a vassal_start.
- **missing** - 1774 vassal_end /ledger/144 with crimean-khanate: crimean-khanate has no vassal_end with ottoman-empire in 1774 (it has the 1772 Karasubazar gain and the 1774 Kerch loss to Russia). Route to ia-02.
- **mismatch** - 1812 gain /ledger/156 with emirate-of-diriyah: emirate-of-diriyah gives Medina (1812), Mecca (1813) and the Hejaz to muhammad-ali-dynasty, not to ottoman-empire; the Ottoman dossier draws the Hejaz as direct Ottoman land from 1812 with Egypt as a vassal. Group me-10 must pick one holder for the Hejaz 1812-1840 in both dossiers.
- **mismatch** - 1818 gain /ledger/162 with emirate-of-diriyah: emirate-of-diriyah dissolves in 1818 with counterpart muhammad-ali-dynasty; the Ottoman dossier gains Najd itself. Same holder question as 1812.
- **mismatch** - 1830 vassal_end /ledger/167 with regency-of-algiers: regency-of-algiers ends in 1830 with loss/dissolve to french-algeria; no vassal_end with ottoman-empire.
- **mismatch** - 1835 vassal_end /ledger/172 with karamanli-dynasty: Year now agrees (reviewer moved 1836 to May 1835). karamanli-dynasty ends with loss/dissolve to ottoman-tripolitania, not a vassal_end with ottoman-empire.
- **missing** - byzantine-empire 1460 loss /ledger/199: 29 May 1460, the Morea, conf 3. The Ottoman ledger has no gain of the Morea; its 1463 keyframe adds 73 Peloponnese cells without an event (finding B2).
- **missing** - crimean-khanate 1772 gain /ledger/10: November 1772, the former Kaffa Eyalet (Treaty of Karasubazar), conf 3. The Ottoman ledger has no 1772 loss to crimean-khanate; its 1772 keyframe drops the 10 Crimean coast cells and restores only Kerch (finding B5).
- **exception** - 1556 gain /ledger/77 with regency-of-algiers: Counterpart anachronistic: the regency-of-algiers dossier starts in 1706 (found, counterpart ottoman-empire), so a 1556 gain 'from' it has no mirror. The 1556 date is Cliopatria's; the author should use counterpart nobody or the state Barbarossa took Algiers from, and the page-dated year (Algiers eyalet from 1517 on the Eyalet page).
- **exception** - beylik-of-karasi [1346 g]; ahi-republic [1363 g]; beylik-of-saruhan [1415 g]; beylik-of-menteshe [1415 g]; beylik-of-teke [1429 g]; germiyanids [1429 g]; beylik-of-isfendiyar [1462 g]; beylik-of-karaman [1468 g]; beylik-of-dulkadir [1515 g]; ramadanid-emirate [1515 g]: counterpart dossiers not written yet (group me-09 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - serbian-empire [1371 g]; second-bulgarian-empire [1376 vs,1385 g,1393 ve,1393 g]; serbian-despots [1386 g,1390 vs,1459 g,1459 ve]; principality-of-wallachia [1395 vs,1419 vs,1878 ve]; despotate-of-dobruja [1395 g]; despotate-of-vidin [1396 g]; albanian-principalities [1422 g]; kingdom-of-bosnia [1463 g,1482 g]; principality-of-moldavia [1487 g,1526 vs,1878 ve]; serbs [1805 l,1814 g,1815 l,1830 vs,1878 ve,1913 l]; first-hellenic-republic [1829 l,1881 l,1913 l,1919 l,1920 l,1922 g]; principality-of-bulgaria [1878 vs,1908 ve,1913 l,1913 g]; montenegro [1878 l]; united-principalities-of-moldavia-and-wallachia [1878 l]; cretan-state [1900 l]; albania [1913 l]: counterpart dossiers not written yet (group eu-18 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - republic-of-venice [1430 g,1540 g,1571 g,1669 g,1687 l,1715 g]; republic-of-genoa [1475 g]; kingdom-of-italy [1912 l]: counterpart dossiers not written yet (group eu-13 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - safavid-dynasty [1516 g,1535 g,1555 g,1578 g,1585 g,1603 l,1604 l,1612 l,1624 l,1625 l,1638 g,1727 g]; qasimids [1636 l]; muhammad-ali-dynasty [1805 vs,1833 vs,1840 ve,1914 ve]; emirate-of-nejd [1824 l,1873 g,1913 l]; imamate-of-yemen [1873 g]; kuwait [1900 l]; kingdom-of-hejaz [1916 l]; north-yemen [1918 l]; asir [1919 l]: counterpart dossiers not written yet (group me-10 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - kingdom-of-hungary [1521 g,1526 g,1529 g,1541 g]; principality-of-transylvania [1526 vs,1699 ve]; polish-lithuanian-commonwealth [1672 g,1696 l,1699 l]: counterpart dossiers not written yet (group eu-15 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - habsburg-monarchy [1552 g,1596 g,1600 g,1663 g,1685 l,1686 l,1691 l,1699 l,1716 l,1718 l,1739 g]: counterpart dossiers not written yet (group eu-09 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - kingdom-of-imereti [1555 g]; armenia [1919 l]: counterpart dossiers not written yet (group eu-19 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - zaporozhian-cossacks [1677 l]; tsardom-of-russia [1700 l,1713 g]: counterpart dossiers not written yet (group eu-16 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - russian-empire [1739 l,1774 l,1792 l,1812 l,1878 l,1916 l]; russian-republic [1918 g]: counterpart dossiers not written yet (group eu-17 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - french-directory [1798 l]; french-consulate [1803 g]; austria-hungary [1878 l]; french-third-republic [1919 l]: counterpart dossiers not written yet (group eu-20 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - kingdom-of-great-britain [1878 l]; british-colonial-empire [1917 l,1917 l,1918 l]: counterpart dossiers not written yet (group eu-11 has not run for them); g=gain l=loss vs/ve=vassal start/end
- **exception** - Greek lords of Thessaly (the page names none) [1394 g]; Anatolian beyliks of the Sivas region (no page opened names them) [1395 g]; Anatolian beyliks restored by Timur (Karaman, Germiyan, Aydın and others) [1402 l]; Balkan successor lords (the page names none) [1402 l,1430 g]; Musa Çelebi (Interregnum rival) [1412 g]; Knights of St John (Tripoli; no dossier) [1551 g]; Bani Khalid and the Gulf coast (page names none) [1560 g]; Eastern Rumelia [1878 vs,1885 ve]: no slug: named in the author's counterparts_needing_dossiers or an unnamed party the page does not name

## Problems

- Verdict fail: nine findings stay with the author (seven blocking: the 1609 correction, the missing 1460 Morea gain, the duplicated 1696 loss, the 1772 Kaffa coast, the 1828-29 war, the Wallachia and Tunis vassal_end events; plus keyframes 45/47 and the area note). No fabricated or mis-dated confidence-3 event in 28 confidence-3 spot checks.
- Reviewer applied six verified year fixes to history/polities/ottoman-empire.json (ledger now re-sorted: old /ledger/74 is /ledger/78, old 123 is 122, old 195 is 194; pointers in this report are to the edited file), added four sources (14 to 18); re-validated: 0 errors, the same 2 vassal-pairing warnings.
- Neighbour dossiers read for cross-checks: byzantine-empire, crimean-khanate, ethiopian-empire, hafsid-dynasty, regency-of-algiers, beylik-of-tunis, karamanli-dynasty, emirate-of-diriyah, afsharid-iran, mamluk-sultanate, empire-of-trebizond, despotate-of-epirus (all existing). The other Context polities (safavid-dynasty, habsburg-monarchy, republic-of-venice, russian-empire, principality-of-wallachia, kingdom-of-hungary and others) have no dossier yet: their mirrors are exceptions.
- Group me-10 must decide who holds the Hejaz and Najd 1812-1840: emirate-of-diriyah gives them to muhammad-ali-dynasty, this dossier to ottoman-empire.
- No page failed to load; WebFetch read all pages opened.
