# se-02-f research notes (Maritime, part f), 2026-10-19

Six dossiers written, all validate (python3 -I tools/validate_dossier.py, also with --resolve). Pages are Wikipedia pages opened with WebFetch on 2026-10-19; a page whose summary was thin is said so in the dossier's `sources[]`. Quoted text in notes is the text WebFetch returned inside quotation marks; anything it returned unquoted is paraphrased.

## Cliopatria rows that are wrong (and what the dossier does)

- sultanate-of-maguindanao: the 1521-1608 shape (332 cells, 106,474 km2) lies cell for cell inside Cliopatria's Sultanate of Brunei 1521 shape; the 1612-1852 shape is one cell in Davao del Norte. Both marked `wrong`; replaced by the Cotabato valley (Maguindanao + Cotabato + Sultan Kudarat provinces, plus the Sarangani islands from 1625). The row ends 1852 but the sultanate lasted to the American occupation of Cotabato (December 1899): new keyframe 1862-1899. Cliopatria's Spanish Empire/Kingdom of Spain shapes cover the valley from the 1600s; the pages do not support that. The Brunei dossier should be told its Mindanao interior is not backed by any page here.
- kingdom-of-pajana (Pajang): the Wikipedia title Cliopatria gives, "Lontara script", and Wikidata Q1074947 are a mismatch for a Central Java kingdom; the article is "Pajang Sultanate". The 1572-1587 shapes are the same 175-cell polygon as Demak 1551 and Mataram 1588; 59 East Java cells cut (neither page names a Pajang holding there). Foundation is 1568 (Demak page), not 1572.
- sultanate-of-johor: Pahang (117 cells) is inside the 1529-1622 shapes though Pahang was a separate sultanate until the 1623 union; 100 Jambi cells are inside the 1529-1669 shapes though Jambi was independent (a Mataram vassal to 1663/64); Terengganu leaves in 1727 in Cliopatria, 1722 on the page; Riau-Lingga leaves in 1820, the Anglo-Dutch Treaty is 17 March 1824; the Pahang separation is drawn in 1853, the Johor page has the 1861 treaty.
- sultanate-of-banten: the Dutch gain of 66 West Java cells is drawn in 1677, the pages put it at the end of the civil war (Ageng surrendered March 1683); Lampung, south Sumatra and Bengkulu stay in Banten to 1808 though the Dutch annexed them in 1752; 1526-1528 missing.
- sultanate-of-perak: a flat province shape for 348 years; not represented: Reman (Siamese tributary) holding Hulu Perak from about 1819, the Dindings and Pangkor ceded to Britain.
- sultanate-of-banjar: row ends 1859, the Dutch dissolved the sultanate in 1860 (war to 1863); only 34 percent of South Kalimantan is in the shape although the page says Banjar controlled all of it.

## Pages that did not load

- https://en.wikipedia.org/wiki/Johor%E2%80%93Jambi_War returned URL_NOT_FOUND (no such article); the Jambi Sultanate page covers the war.
- "Perak Sultanate" resolves to the ruler list "Sultan of Perak"; History_of_Perak resolves to the article on Perak. The Aceh Sultanate page has nothing on Perak beyond a family tree.

## Per state: what is unsettled

- Johor (5 pages): 1884 end (dissolve at confidence 1; the British Colonial Empire 1885 shape contains all 61 cells of the last shape; no page opened gives an event); 1784 and 1818 Dutch Riau; Abu Bakar and the 1885 treaty; Siak's separation after Raja Kecil; when the Sumatran shore left (Cliopatria 1820, page 1824); 3 north-Sumatra cells lost in 1626 (Aceh); the Sultanate of Malacca row (1459-1861) overlaps these years. Needs dossiers: Pahang Sultanate 1470-1623, Siak Sultanate, Jambi Kingdom before 1670.
- Banten (5 pages): the east of the Sunda lands after 1579 (Cliopatria: Cirebon, page: Banten took "most"); date of Banten's Lampung conquest inside 1550-1570; when Sunda Kelapa passed to Banten; 1659 and 1684 treaty terms; Banten as VOC client 1683-1808 belongs to the Dutch Republic dossier as vassal_start with counterpart sultanate-of-banten; Landak (vassal 1661-1752) has no dossier.
- Perak (5 pages): ledger is short because the pages are; Aceh's authority over Perak 1612-c.1653 belongs in the Aceh dossier as vassal_start with counterpart sultanate-of-perak; the British dossier should carry the Pangkor Treaty (1874) as vassal_start for Perak and the Perak War; Reman (Hulu Perak 1819-1909) needs a dossier; Dindings cession 1826 (History page) or 1874 (Pangkor page).
- Maguindanao (2 pages): Buayan vassal pair at confidence 1 (page undated); Lanao's secession and the Davao/Iranun/Maranao tribute zones undated, so no events; capital sites approximate; the 1705 "Palawan" sentence on the page is garbled.
- Banjar (2 pages): Negara Daha (predecessor) has no dossier; the tribute ring (Kotawaringin to Sulu) is undated, no vassal events; rebel land 1860-1863 not mapped; the 1787 Dutch protectorate belongs to the Dutch dossiers.
- Pajang (2 pages): capital, area and reign years are not on the pages, no rulers list; Demak ends 1551 (Cliopatria) or 1568 (page); Mataram starts 1586 (Pajang page) or 1588 (Cliopatria); Jipang has no dossier.

## Area checks

None of the pages opened gives an infobox area for any of the six states (Johor: 220,000 km2 with no year, against Cliopatria's 208,008, ratio 0.95), so no area ratio could be taken for the others.
