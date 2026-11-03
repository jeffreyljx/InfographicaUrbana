# Review of batch am-06-c

Reviewer: Phase B adversarial reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/am-06-c.json.

All ten dossiers passed the validator with --resolve before and after review (warnings: new-netherland 11 and netherlands-antilles 4 'resolves to no cells', intended; aruba, curacao, sint-maarten and now demerara are slugs without dossiers). Spot checks were made with WebFetch on the cited pages; no confidence-3 event was found fabricated or mis-dated by more than a month.

| slug | verdict |
| --- | --- |
| france-antarctique | pass |
| jesuit-reducciones | thin |
| new-netherland | fix |
| french-colony-of-guiana | thin |
| french-louisiana | pass |
| netherlands-antilles | pass |
| dutch-suriname | thin |
| dutch-brazil | fix |
| essequibo | fix |
| berbice | thin |

## france-antarctique: pass

For the gap-filler:
- `/ledger/1` Year the colony reached Cabo Frio (1556 is Cliopatria's start, confidence 1); Henriville undated Page to try: https://en.wikipedia.org/wiki/Nicolas_Durand_de_Villegaignon

Spot checks: `/ledger/0` confirmed (1 November 1555, Serigipe); `/ledger/3` confirmed (15 March 1560, Fort Coligny destroyed); `/ledger/6` confirmed (founded 22 June 1564, sacked 20 September 1565); `/ledger/8` confirmed (20 January 1567, French expelled).

Area: infobox None km2 (None), Cliopatria 12370 km2, ratio None. page has no infobox; extent 'from Rio de Janeiro to Cabo Frio' matches the 1556 shape (10,750 km2)

## jesuit-reducciones: thin

For the gap-filler:
- `/keyframe_review/4` Gain event for the Seven Missions east of the Uruguay (San Borja 1682 to Santo Angelo 1706/07): Cliopatria's 1738 shape adds 82 Rio Grande do Sul cells over the 1640 shape with no ledger event Page to try: https://en.wikipedia.org/wiki/S%C3%A3o_Miguel_das_Miss%C3%B5es
- `/keyframe_review/0` The 1609-1628 keyframe draws Cliopatria's whole 1595 shape (about 800 cells of Itapua, Misiones and the Uruguay missions) plus Guayra, but the ledger has only the San Ignacio Guazu found (42 cells) and Guayra (657); the Parana and Uruguay missions founded 1610-1630s need dated gains Page to try: https://en.wikipedia.org/wiki/Roque_Gonz%C3%A1lez_de_Santa_Cruz
- `/ledger/6` Tape missions lost 1638 at confidence 1 (Mborore page: Tape invaded 1636-1638, destruction not stated) Page to try: https://en.wikipedia.org/wiki/Bandeirantes
- `/ledger/10` Whether the Seven Missions returned to Jesuit administration after Spain reclaimed them (1759, Treaty of El Pardo 1761) until the 1767 expulsion; Spanish and Portuguese dossiers record occupation 1756-1759 and a Spanish regain 1761 Page to try: https://en.wikipedia.org/wiki/Treaty_of_El_Pardo_(1761)

Spot checks: `/ledger/1` confirmed (15 Guayra missions over 22 years, western two-thirds of Parana, over 100,000 km2; confidence 2 honest); `/ledger/3` confirmed ('By the year 1632 ... Guayra region virtually deserted'; Itatin struck 1632); `/ledger/7` confirmed (11 March 1641, Guarani victory); `/ledger/10` confirmed (7 and 10 February 1756; missions occupied, Guarani forced out of the ceded missions).

Area: infobox None km2 (None), Cliopatria 261430 km2, ratio None. no infobox; page gives Guayra 'more than 100,000 km2'; the dossier's Guayra gain resolves to 657 cells (about 167,500 km2), ratio 1.7, under two

## new-netherland: fix

Findings:
- `/ledger/3/region` 1626 gain drew the whole of Connecticut and Massachusetts (129 cells) while keyframe 2 holds 16 Connecticut cells Evidence: cell counts: gain region 129 cells, Cliopatria 1626 shape intersect Connecticut 16 cells; the New Netherland page names only Fort Goede Hoop on the Fresh River Fix: region = intersect(Cliopatria New Netherland 1626, Connecticut); text kept; reviewer note appended (applied by the reviewer).
- `/ledger/7/region` 1650 Treaty of Hartford loss drew the whole of Connecticut and Massachusetts (129 cells) at confidence 3; keyframes 9 to 10 drop 26 cells Evidence: Treaty_of_Hartford_(1650): the Dutch gave up the Connecticut claim 'the full length of the Connecticut River ... east to Narragansett Bay'; Massachusetts is not mentioned Fix: region = intersect(Cliopatria New Netherland 1648, Connecticut + Massachusetts), 26 cells; confidence 3 kept for the Connecticut valley (applied by the reviewer).
- `/ledger/17` Loss of the Delaware (former New Sweden) dated September 1664; it fell in October Evidence: New_Sweden: the English conquest 'began on August 29, 1664' and ended with the capture of Fort Casimir in October; Conquest_of_New_Netherland gives no date ('around the same time') Fix: month 10, source New_Sweden page, event moved after the 1664/9 contest_end to keep the ledger in order (now /ledger/18) (applied by the reviewer).

For the gap-filler:
- `/keyframe_review/1` Keyframe 1 (1622-1625) keeps only 2 Cliopatria cells at Albany, smaller than the 1614 found region (Albany 30 km, 9 cells) and the May 1624 gain; no loss explains the shrink. Correction should be union(intersect(Cliopatria 1622, USA), Albany 30 km) Page to try: https://en.wikipedia.org/wiki/Albany,_New_York
- `/ledger/3` Year of Fort Goede Hoop (Fort Huys de Hoop) on the Connecticut River; 1626 is Cliopatria's year, confidence 1 Page to try: https://en.wikipedia.org/wiki/Fort_Huys_de_Hoop
- `/ledger/5` Year of Fort Nassau on the Delaware and the 1632 New Jersey cells (confidence 1) Page to try: https://en.wikipedia.org/wiki/Fort_Nassau_(South_River)
- `/ledger/6` 1636 Connecticut and Hudson cells (confidence 1) Page to try: https://en.wikipedia.org/wiki/Fort_Huys_de_Hoop
- `/wars` Kieft's War (1643-1645), the Peach War (1655) and the Esopus Wars (1659-1663) not checked for ground lost; Directors-General not listed Page to try: https://en.wikipedia.org/wiki/Kieft%27s_War

Spot checks: `/ledger/0` confirmed (Fort Nassau 1614); `/ledger/4` confirmed (Manhattan acquired 24 May 1626); `/ledger/7` confirmed (19 September 1650); region narrowed; `/ledger/10` confirmed (May 1654, Swedes take Fort Casimir); `/ledger/12` confirmed (Fort Christina surrendered 15 September 1655); `/ledger/15` confirmed (transfer 8 September 1664); `/ledger/16` confirmed (Fort Orange 24 September 1664); `/ledger/18` mis-dated (September for October 1664), fixed; `/ledger/20` confirmed (9 August 1673 N.S.); `/ledger/22` confirmed (handover 10 November 1674 N.S.).

Area: infobox None km2 (None), Cliopatria 343999.8 km2, ratio None. no infobox area (claim 'from the Delmarva Peninsula to Cape Cod'); Cliopatria's 1642 maximum is the Dutch Brazil lump; the US part is 89-95 cells (about 23,000 km2), acknowledged in keyframe notes

## french-colony-of-guiana: thin

For the gap-filler:
- `/ledger/5` The 1930 'gain from nobody' of the interior (231 cells, about 59,000 km2) is the researcher's reading: the French Guiana page says Inini 'consisted of most of the interior of French Guiana when it was created in 1930', i.e. land already counted as French Guiana, and Inini was administered apart from the colony 1930-1946. The interior's date as French land (Utrecht 1713 frontier, the 1891 Franco-Dutch and 1900 Franco-Brazilian awards) needs a page; the 1643-1929 keyframes reuse the 1791 coastal shape (unverified: page budget) Page to try: https://en.wikipedia.org/wiki/Inini
- `/keyframe_review/0` Dutch (1650s-1664), English (1667) and Dutch (1676) occupations of Cayenne; Kourou 1763 Page to try: https://en.wikipedia.org/wiki/Cayenne
- `/keyframe_review/2` The Franco-Brazilian Contestado (Counani) and the Swiss award (year not on the page) Page to try: https://en.wikipedia.org/wiki/Republic_of_Independent_Guiana

Spot checks: `/ledger/0` confirmed (Cayenne founded 1643); `/ledger/1` confirmed (15 December 1808, Oyapok and Appruage); `/ledger/3` confirmed (capitulation 11 January, entry 14 January 1809); `/ledger/4` confirmed (French fleet 8 November 1817); `/ledger/5` confirmed for the year and Inini; 'gain from nobody' not on the page (confidence 2, listed under thin).

Area: infobox 84000 km2 (2024), Cliopatria 19564.7 km2, ratio 0.23. Cliopatria's 1791 coastal shape is a quarter of the department; keyframe 3 notes the 84,000 km2 and the dossier switches to the full department in 1930 (see thin)

## french-louisiana: pass

Spot checks: `/ledger/0` confirmed (1800, Third Treaty of San Ildefonso); `/ledger/3` confirmed (30 November 1803, Spanish officials convey to France); `/ledger/4` confirmed (20 December 1803, New Orleans to the US); `/ledger/6` confirmed (9 and 10 March 1804, Upper Louisiana at St. Louis).

Area: infobox 2140000 km2 (1803), Cliopatria 107958 km2, ratio 0.05. both Cliopatria shapes marked wrong (Caribbean and Guiana fragments); the correction region 'Louisiana' resolves to 10,299 cells (about 2.63 million km2), 1.23 times the page figure

## netherlands-antilles: pass

For the gap-filler:
- `/ledger/4` Counterpart of the 1648 Sint Maarten gain: the SSS islands page says only that the island 'was split between France and the Netherlands in 1648'; Spain held it 1633-1648, so spanish-empire may be the right counterpart Page to try: https://en.wikipedia.org/wiki/Treaty_of_Concordia
- `/keyframe_review/3` Occupations of Sint Eustatius and Sint Maarten (1781 Rodney, French 1781-1784, British 1801-1802 and 1810-1816) and the 1983 SSS split Page to try: https://en.wikipedia.org/wiki/Capture_of_Sint_Eustatius

Spot checks: `/ledger/0` confirmed (van Walbeeck 1634, Spanish surrender in August); `/ledger/4` confirmed (1648 split); prior holder not on page; `/ledger/5` confirmed (British 1800-1803 and 1807-1816); `/ledger/10` confirmed (1828 merger ruled from Paramaribo, partial reversal 1845); `/ledger/16` confirmed (Aruba seceded 1 January 1986; dissolved 10 October 2010).

Area: infobox 980 km2 (1985), Cliopatria 149155.3 km2, ratio 152.2. Cliopatria's 1877-2023 shape is Suriname plus Guyana cells; keyframe 8 removes them. The islands-only shapes (2,176 km2 in Cliopatria, 6 to 11 grid cells) are about twice the 980 km2 by polygon and grid rounding of small islands; Saba and Sint Eustatius resolve to zero cells

## dutch-suriname: thin

For the gap-filler:
- `/ledger/9` The 1820 gain of the interior (444 cells, confidence 1, Cliopatria's year) disagrees with keyframe 2 (1816-1827), which stays at the 81-cell coastal belt; split keyframe 2 at 1820 or move the extent change to a dated event. The interior's status needs a page (Maroon treaties of 1760-1767, the Corantijn and Marowijne frontiers) Page to try: https://en.wikipedia.org/wiki/Ndyuka_people
- `/ledger/2` The English recapture under John Harman (October 1667) and the return to the Dutch (1668) are in the note of /ledger/1 and the war outcome but not in the ledger (occupation_start/occupation_end with english-colonial-empire) Page to try: https://en.wikipedia.org/wiki/Willoughbyland

Spot checks: `/ledger/1` confirmed (26 February 1667); `/ledger/2` confirmed (Treaty of Breda 31 July 1667); `/ledger/5` confirmed (British 1799-1802 and 1804-1816; infobox 1815); `/ledger/10` confirmed (1828 union, 1845 separation); `/ledger/13` confirmed (1975).

Area: infobox None km2 (None), Cliopatria None km2, ratio None. not a Cliopatria row; the page has no area

## dutch-brazil: fix

Findings:
- `/ledger/4/region` 1641 gain drew the whole of Maranhao and Piaui (1,913 cells) while keyframe 4 holds 286 of their cells Evidence: Dutch_Brazil: 'In 1641, the Dutch captured the captaincy of Maranhao', 'the entire coastline between the Amazon and Sao Francisco Rivers'; cell counts against the Cliopatria 1642 shape Fix: region = intersect(Cliopatria New Netherland 1642, Maranhao + Piaui) (applied by the reviewer).
- `/ledger/2/region` 1635 gain drew all of Alagoas (94 cells); no keyframe holds more than 2 Alagoas cells Evidence: Dutch_Brazil: 'In 1635, the Dutch conquered three strongholds ... Porto Calvo'; keyframes 2-3 intersect Alagoas in 2 cells Fix: region = intersect(Cliopatria New Netherland 1636, Alagoas) (applied by the reviewer).
- `/ledger/5/region` 1645 loss of Maranhao drew the whole state (1,077 cells) Evidence: mirror of the narrowed 1641 gain Fix: region = intersect(Cliopatria New Netherland 1642, Maranhao), 221 cells (applied by the reviewer).
- `/ledger/6/region` 1645 loss of Ceara and Piaui drew both whole states (1,334 cells) Evidence: keyframe 4 holds 382 of their cells Fix: region = intersect(Cliopatria New Netherland 1642, Ceara + Piaui) (applied by the reviewer).

For the gap-filler:
- `/keyframe_review/4` Keyframe 4 (Cliopatria 1642) also widens the Rio Grande do Norte and Paraiba core by about 214 cells that keyframe 5 drops again; no ledger event explains either move (a Cliopatria wobble: the correction could keep the 1636 core) Page to try: https://en.wikipedia.org/wiki/Dutch%E2%80%93Portuguese_War
- `/ledger/6` Date of the loss of Ceara (confidence 1); the Dutch garrison fell in 1644 and Fort Schoonenborch was held again from 1649 Page to try: https://en.wikipedia.org/wiki/Fortaleza
- `/ledger/9` Loss of Paraiba and Rio Grande do Norte dated 1648 from Cliopatria (confidence 1) Page to try: https://en.wikipedia.org/wiki/First_Battle_of_Guararapes
- `/ledger/0` The Dutch capture of Salvador da Bahia (8 May 1624 to 30 April 1625) is on the Dutch Brazil page but not in the ledger; also Sergipe Page to try: https://en.wikipedia.org/wiki/Dutch_Brazil

Spot checks: `/ledger/0` confirmed (Olinda 16 February 1630); `/ledger/1` confirmed (by 1634, Rio Grande do Norte to Cabo de Santo Agostinho); `/ledger/3` confirmed (Ceara 1637); `/ledger/4` confirmed (Maranhao 1641); region narrowed; `/ledger/8` confirmed (Itamaraca abandoned 13 December 1647); `/ledger/10` confirmed (26 January 1654; infobox 28 January).

Area: infobox None km2 (None), Cliopatria None km2, ratio None. not a Cliopatria row; no area on the page; maximum keyframe 967 cells (about 247,000 km2) in 1641-1644

## essequibo: fix

Findings:
- `/ledger/12/counterpart` 1812 merge recorded with british-colonial-empire; the page says it merged with Demerara Evidence: Essequibo_(colony): 'It was merged with Demerara in 1812 by the British who took control'; infobox 'Joined with Demerara to form Demerara-Essequibo: 28 April 1812' Fix: counterpart = demerara (no dossier yet; listed by the author) (applied by the reviewer).

For the gap-filler:
- `/keyframe_review/1` Keyframes 0 to 3 change by +23, +8 and -8 cells (1616-1653) with no ledger event (Cliopatria wobbles; small) Page to try: https://en.wikipedia.org/wiki/Kyk-Over-Al
- `/ledger/4` Pomeroon (Nova Zeelandia) as a colony 1658-1689 and the 1667 Bergenaar re-occupation; the loss region (all of Pomeroon-Supenaam, 192 cells) is wider than the 3 cells the keyframes drop Page to try: https://en.wikipedia.org/wiki/Pomeroon_River
- `/identity` Demerara's status before 1812 (the author reads it as a district of Essequibo; the page speaks of 'the Essequibo and Demerara colonies'); the Essequibo regions include the Demerara coast throughout Page to try: https://en.wikipedia.org/wiki/Demerara

Spot checks: `/ledger/2` confirmed (occupied by the British 1665; Zeelanders retook it 1666); `/ledger/4` confirmed (Pomeroon destroyed 1689); `/ledger/5` confirmed (privateers 24 February 1781); `/ledger/7` confirmed (French 27 February 1782 to February 1783); `/ledger/12` confirmed (28 April 1812); counterpart corrected; `/ledger/14` confirmed (13 August 1814).

Area: infobox None km2 (None), Cliopatria None km2, ratio None. not a Cliopatria row; no area on the page

## berbice: thin

Findings:
- `/wars/0/outcome` The war's outcome and note said the page gives the rebels' land no extent; the page says they held the south of the colony Evidence: Berbice: the rebels 'captured the south of the colony', while the outnumbered whites held the north; the revolt lasted 'until well into 1764' Fix: outcome and note rewritten with the page's words (zones and events left to the gap-filler) (applied by the reviewer).

For the gap-filler:
- `/wars/0/zones` Zone and a contest_start (February 1763) / contest_end (1764) pair for the rebel-held south of the colony (upper Berbice River), counterpart Coffy's rebels; a rebel dossier may be due (held land about a year) Page to try: https://en.wikipedia.org/wiki/Berbice_slave_uprising
- `/identity/capitals/0` Capital is Fort Nassau until 1785 (infobox) or 1790 (text); the entry names New Amsterdam for 1627-1814 with Fort Nassau only in its note; needs Fort Nassau's coordinates Page to try: https://en.wikipedia.org/wiki/New_Amsterdam,_Guyana

Spot checks: `/ledger/0` confirmed (1627, van Peere); `/ledger/2` confirmed (November 1712, Cassard; ransom 24 October 1714); `/ledger/5` confirmed (27 February 1781); `/ledger/10` confirmed (22 April 1796; restored 27 March 1802; British again September 1803); `/ledger/13` confirmed (ceded 1814, ratified 20 November 1815).

Area: infobox None km2 (None), Cliopatria None km2, ratio None. not a Cliopatria row; no area on the page

## Cross-dossier matrix (non-exception rows)

- france-antarctique 1560 loss with portuguese-empire: **missing**. portuguese-empire has no 1560 event: its contest with France Antarctique starts in 1565 (/ledger/21); the page dates the fall of Fort Coligny to 15 March 1560. Route to the portuguese-empire author (am-06).
- france-antarctique 1565 loss with spanish-empire: **mismatch**. spanish-empire /ledger/19 (September 1565, Fort Caroline) names kingdom-of-france as counterpart; same land and month. Agree on one counterpart (france-antarctique follows Cliopatria; a french-florida dossier is suggested).
- france-antarctique 1567 loss with portuguese-empire: **matched**. portuguese-empire /ledger/23
- jesuit-reducciones 1756 loss with portuguese-empire: **mismatch**. portuguese-empire records an occupation 1756-1759 (/ledger/58-59), spanish-empire a loss to Portugal in 1756 (/ledger/46) and a regain in 1761 (/ledger/47); the reducciones record a plain loss to Portugal and no return. Agree on loss versus occupation.
- french-colony-of-guiana 1809 occupation_start with portuguese-empire: **mismatch**. same land and year; portuguese-empire /ledger/72 names first-french-empire as the owner, not french-colony-of-guiana
- french-colony-of-guiana 1817 occupation_end with portuguese-empire: **mismatch**. portuguese-empire /ledger/75, counterpart first-french-empire
- french-louisiana 1800 occupation_start with spanish-empire: **mismatch**. spanish-empire models 1800-1803 as Spanish sovereignty (no 1800 event) and records the loss to french-louisiana on 30 November 1803 (/ledger/73); french-louisiana models French title from 1800 with Spanish administration as an occupation. One model for both.
- french-louisiana 1800 occupation_start with spanish-empire: **mismatch**. spanish-empire models 1800-1803 as Spanish sovereignty (no 1800 event) and records the loss to french-louisiana on 30 November 1803 (/ledger/73); french-louisiana models French title from 1800 with Spanish administration as an occupation. One model for both.
- french-louisiana 1803 occupation_end with spanish-empire: **mismatch**. spanish-empire /ledger/73 (30 November 1803) is a loss; same day and land, different type
- french-louisiana 1804 occupation_end with spanish-empire: **missing**. spanish-empire has no March 1804 event for Upper Louisiana (St. Louis, Three Flags Day 9 March 1804)
- netherlands-antilles 1828 merge with dutch-suriname: **matched**. dutch-suriname /ledger/10
- netherlands-antilles 1845 split with dutch-suriname: **matched**. dutch-suriname /ledger/11
- dutch-suriname 1828 merge with netherlands-antilles: **matched**. netherlands-antilles /ledger/10
- dutch-suriname 1845 split with netherlands-antilles: **matched**. netherlands-antilles /ledger/12
- dutch-brazil 1634 gain with portuguese-empire: **missing**. portuguese-empire has no matching event; it records Dutch Brazil only in 1641, 1645 and 1654 and under counterpart dutch-republic. Route to the portuguese-empire author (am-06).
- dutch-brazil 1635 gain with portuguese-empire: **missing**. portuguese-empire has no matching event; it records Dutch Brazil only in 1641, 1645 and 1654 and under counterpart dutch-republic. Route to the portuguese-empire author (am-06).
- dutch-brazil 1637 gain with portuguese-empire: **missing**. portuguese-empire has no matching event; it records Dutch Brazil only in 1641, 1645 and 1654 and under counterpart dutch-republic. Route to the portuguese-empire author (am-06).
- dutch-brazil 1641 gain with portuguese-empire: **mismatch**. portuguese-empire /ledger/29 (Sao Luis 1641) names dutch-republic, not dutch-brazil
- dutch-brazil 1645 loss with portuguese-empire: **mismatch**. portuguese-empire /ledger/32 (Sao Luis abandoned 1645) names dutch-republic, not dutch-brazil
- dutch-brazil 1645 loss with portuguese-empire: **missing**. portuguese-empire has no matching event; it records Dutch Brazil only in 1641, 1645 and 1654 and under counterpart dutch-republic. Route to the portuguese-empire author (am-06).
- dutch-brazil 1647 loss with portuguese-empire: **missing**. portuguese-empire has no matching event; it records Dutch Brazil only in 1641, 1645 and 1654 and under counterpart dutch-republic. Route to the portuguese-empire author (am-06).
- dutch-brazil 1648 loss with portuguese-empire: **missing**. portuguese-empire has no matching event; it records Dutch Brazil only in 1641, 1645 and 1654 and under counterpart dutch-republic. Route to the portuguese-empire author (am-06).
- dutch-brazil 1654 loss with portuguese-empire: **mismatch**. portuguese-empire /ledger/35 names dutch-republic, not dutch-brazil
- netherlands-antilles 1634 found with spanish-empire: **missing**. Curacao taken from Spain in August 1634 (History of Curacao); spanish-empire has no 1634 loss. Route to am-06.
- dutch-brazil 1630 found with portuguese-empire: **missing**. Olinda and Recife taken February-March 1630; portuguese-empire has no 1630 loss. Route to am-06.
- french-louisiana 1800 found with spanish-empire: **mismatch**. see the 1800 occupation entry: spanish-empire keeps Louisiana to 30 November 1803
- jesuit-reducciones 1767 dissolve with spanish-empire: **matched**. spanish-empire /ledger/57

Exceptions (counterpart nobody, or a counterpart whose group has not run: english-colonial-empire, new-sweden and united-states-of-america (am-07), british-colonial-empire (eu-11), kingdom-of-france (eu-10), netherlands, french-fourth-republic (eu-22), republic-of-suriname (am-08), or listed by the author: aruba, curacao, sint-maarten, demerara): 62 rows in the JSON.

## Other remarks

- new-netherland: keyframe 18 (new, 1673-1674) is listed before keyframe 19 (Cliopatria 1670); cosmetic. The dossier's life has an 8-year gap without land (1665-1672), handled by an empty keyframe.
- jesuit-reducciones: the 1632 loss region (all of Parana and Mato Grosso do Sul, 2,235 cells) is wider than the land held (Guayra 657 cells plus Cliopatria's Itatin cells); harmless for a loss, but the mirror should use the narrower land.
- Colour family france for the Dutch states is right: colours.json files the Netherlands rows under family france, group netherlands.
- French Louisiana: the occupation model (French title 1800, Spanish administration to 30 November 1803 and 9 March 1804) is consistent with the Louisiana Purchase page; spanish-empire should adopt it or the two must agree otherwise.
