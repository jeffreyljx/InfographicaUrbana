# Review of batch eu-13-j (Italy, part j), 2026-10-25

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/eu-13-j.json.

The validator gave 0 errors on all five dossiers, before and after the reviewer's edits; its warnings are by design (unknown-slug counterparts, sub-cell islands, the two Naples dossiers each leaving the other's shapes unreviewed). Spot checks were weighted to confidence-3 and land-moving events. No article has an infobox area.

## Verdicts

### house-of-savoy: FAIL

Findings:

- `/ledger/2` (applied by reviewer): Lake Geneva restitution dated 1572 at confidence 1 (Cliopatria's shape year) against swiss-confederation's 1564 loss. Evidence: Republic of Geneva page: 'only in the Treaty of Lausanne of 1564 did Savoy recover the lands around Geneva'; swiss-confederation /ledger/32 is the 1564 loss to house-of-savoy. Fix: Re-dated to 1564, confidence 2, source Republic_of_Geneva added to sources[]; region kept (the 10 cells Cliopatria adds late in 1572).
- `/keyframe_review/13/correction` (NOT applied, for the author): The correction holds Cliopatria's 1709 gain (7 cells at lon 8.1-8.6 E, lat 44.3-45.3 N: Casale, Acqui, i.e. Montferrat) back to 1713 as 'parts of the Duchy of Milan'. Montferrat passed to Savoy in 1708, so the correction moves correct land to a wrong date. Evidence: Duchy of Montferrat page: 'the remainder passed to Savoy in 1708'; infobox 'Annexed by Duchy of Savoy: 1708'. The Duchy of Savoy infobox line 'Acquired Sicily and parts of Duchy of Milan: 11 April 1713' is about Milanese land (Alessandria, Valenza, Lomellina, Valsesia), not Montferrat. Victor Amadeus II page: in 1702 the emperor 'promised him the Duchy of Montferrat'. Fix: Verdict ok for house-of-savoy_1709 (Cliopatria a year late). Add a 1708 gain of Montferrat from duchy-of-mantua (source https://en.wikipedia.org/wiki/Duchy_of_Montferrat, confidence 2, region the 1709-minus-1706 cells). Keep /ledger/17 only for land that was Milanese, with a page that names it (the 1707 handover of Alessandria, Valenza, Lomellina and Valsesia under the 1703 treaty), or drop its region to the cells Cliopatria actually changes in 1713.
- `/ledger/17` (NOT applied, for the author): Region is the Montferrat cells (see /keyframe_review/13), labelled 'parts of the Duchy of Milan'; counterpart habsburg-monarchy has no matching loss (its /ledger/52 is the 1713 gain of Milan from Spain). Evidence: Duchy of Montferrat page, as above; habsburg-monarchy ledger has no 1707-1713 loss to house-of-savoy. Fix: Re-assign as in the keyframe fix: Montferrat 1708 from duchy-of-mantua; the Milanese districts from habsburg-monarchy with their own region and year.
- `/ledger/14` (NOT applied, for the author): The occupation of the western cells including Nice is ended in 1706 (confidence 1), but kingdom-of-france has the County of Nice occupied 1707-1713. Evidence: kingdom-of-france /ledger/153 and /ledger/157 (County of Nice page: 'the county was subjected to French occupation twice (1691-1697 and 1707-1713)'). Fix: Take the County of Nice cells out of the /ledger/13-14 region and give them their own occupation_start (1705-1707, page County_of_Nice) and occupation_end 1713 with kingdom-of-france.
- `/ledger (1713)` (NOT applied, for the author): No loss of the Ubaye (Barcelonnette) valley to France and no gain of the Dauphine valleys east of the watershed at Utrecht. Evidence: kingdom-of-france /ledger/160: 1713 gain of the Ubaye Valley from house-of-savoy (War of the Spanish Succession page). The Treaty of Utrecht page (this dossier's source) does not name the valleys; I opened it. Fix: Add the 1713 loss of the Ubaye to kingdom-of-france and the gain of Exilles, Fenestrelle, Oulx and Chateau-Dauphin, from a page that names them (War_of_the_Spanish_Succession or Barcelonnette).

Gaps for a gap-filler:

- `/ledger (1630)`: The French occupation of Savoy in 1630, which ended with Cherasco. Both pages the author opened have it: the Duchy of Savoy infobox 'Occupied by France: ... 1630' and the Charles Emmanuel I page: 'in 1630, Richelieu ordered a French army to march into Savoy'. The notes call these pages silent. (try https://en.wikipedia.org/wiki/War_of_the_Mantuan_Succession)
- `/ledger/13`: Places and dates of the 1703-1706 French hold on western Piedmont (confidence 1 on both ends). (try https://en.wikipedia.org/wiki/Siege_of_Turin)
- `/keyframe_review/4`: Shapes 1595, 1642 and 1645 are unverified (page budget); one- to two-cell changes. (try https://en.wikipedia.org/wiki/Duchy_of_Savoy)

Spot checks:

- `/ledger/16` https://en.wikipedia.org/wiki/Duchy_of_Savoy: confirmed: 'At the end of the war in 1713, Victor Amadeus II received the Kingdom of Sicily'; infobox 'Acquired Sicily and parts of Duchy of Milan: 11 April 1713'
- `/ledger/22` https://en.wikipedia.org/wiki/War_of_the_Quadruple_Alliance: confirmed: infobox 'Savoy cedes Sicily to Austria', 'Austria cedes Sardinia to Savoy' (/ledger/23 too), Hague 17 February 1720; /ledger/18-19 dates also confirmed
- `/ledger/5` https://en.wikipedia.org/wiki/Charles_Emmanuel_I,_Duke_of_Savoy: confirmed: 'with the Treaty of Lyon (17 January 1601), Saluzzo went to Savoy in exchange for Bresse, Bugey, and Gex' (/ledger/3, /ledger/6 too)
- `/ledger/11` https://en.wikipedia.org/wiki/Treaty_of_Turin_(1696): confirmed: signed 29 August 1696, 'All Savoyard territories occupied by France would be returned, including Pinerolo'; the page also gives 'occupied again between 1704 and 1714' (noted by the author)
- `/ledger/2` https://en.wikipedia.org/wiki/Republic_of_Geneva: mis-dated: the page has 1564, the dossier 1572 (confidence 1); fixed by the reviewer
- `/keyframe_review/13` https://en.wikipedia.org/wiki/Duchy_of_Montferrat: not on page: the page has Montferrat annexed by Savoy in 1708, against the correction's 1713

Area: Neither Duchy of Savoy nor House of Savoy has an infobox area (I checked Duchy of Savoy); the author says so. The 1691 (ratio 0.47) and 1702 (0.67) drops are acknowledged and corrected as occupation.

### kingdom-of-sardinia: FAIL

Findings:

- `/ledger/28` (applied by reviewer): The 5 July 1848 Venetian vote is drawn as all of Veneto at confidence 3, but by then Austria had retaken the Venetian mainland. Evidence: First Italian War of Independence page: Vicenza retaken 11 June, Padua and Treviso 13 June; Venice was 'the only city in Lombardy-Venetia which remained in the hands of the insurgents'. Fix: Region narrowed to {admin1 Venezia, Italy}, confidence 2, reviewer note appended.
- `/ledger/40` (applied by reviewer): The end of the Monaco protectorate was dated 1861 at confidence 1 with no page. Evidence: Monaco page: 'Monaco remained in this position until 1860 when, by the Treaty of Turin, the Sardinian forces pulled out'. Fix: Moved to 1860 month 3 (Treaty of Turin, 24 March 1860), confidence 2, source Monaco added to sources[]; the event moved from /ledger/46 to /ledger/40 to keep the order.
- `/ledger/25` (NOT applied, for the author): Parma is gained in spring 1848 and never lost: no loss follows the Salasco armistice, while the 1849 keyframe (/keyframe_review/13, ok) drops it. The ledger leaves Parma Sardinian from 1848 to 1860. Evidence: First Italian War of Independence page: after the Salasco armistice 'Prince Franz de Paula of Liechtenstein marched on Parma and Modena to restore the deposed dukes'. Fix: Add a loss in August 1848 (after 9 August) of the /ledger/25 region to duchy-of-parma-and-piacenza (or an occupation by austrian-empire), confidence 2, source First_Italian_War_of_Independence.
- `/ledger/4` (NOT applied, for the author): The Milanese gain west of the Ticino is dated 1748 (Aix-la-Chapelle). habsburg-monarchy dates the cession to Worms, 13 September 1743 (confidence 3). The two disagree by five years. Evidence: War of the Austrian Succession page: at Worms (13 September 1743) 'the Austrians ceded all their territories west of the river Ticino and Lake Maggiore, along with lands south of the Po'; habsburg-monarchy /ledger/72. Fix: Date the gain 1743-09 from War_of_the_Austrian_Succession and mark keyframe_review/2 (1738) adjust to add the 1748 cells from 1743. Or keep 1748 with a page saying the land was handed over only then, and route the disagreement to eu-09.

Gaps for a gap-filler:

- `/ledger/21`: Return of Savoy and Nice in 1814 (confidence 1). The dossier's own page says the Congress of Vienna 'returned the region of Savoy to its borders after it had been annexed by France in 1792'. The First Treaty of Paris left part of Savoy (Chambery, Annecy) French until November 1815. (try https://en.wikipedia.org/wiki/Treaty_of_Paris_(1814))
- `/ledger (1792)`: French occupation of the County of Nice from September 1792 (annexed 1793). The dossier loses Nice only at the 1796 treaty, with no occupation before it. (try https://en.wikipedia.org/wiki/County_of_Nice)
- `/wars/1`: The Sardinian front of the War of the Austrian Succession ran 1742-1748: the Spanish occupation of Savoy from 1742 and the Franco-Spanish invasion of Nice (the War of the Austrian Succession page has Villefranche 'then part of Savoy' captured in 1744). The war is entered as 1748-1748 with no occupation events. (try https://en.wikipedia.org/wiki/War_of_the_Austrian_Succession)
- `/ledger/9`: Return or merger of the 1796 fortress districts (confidence 1 bridging). (try https://en.wikipedia.org/wiki/Piedmontese_Republic)
- `/keyframe_review/11`: Nine Piedmontese cells added in 1815 and the 1853 cell (/keyframe_review/14) are unverified (page budget). (try https://en.wikipedia.org/wiki/Congress_of_Vienna)

Spot checks:

- `/ledger/22` https://en.wikipedia.org/wiki/Kingdom_of_Sardinia_(1720-1861): confirmed: 'In 1814, the Crown of Savoy enlarged its territories with the addition of the former Republic of Genoa'
- `/ledger/24` https://en.wikipedia.org/wiki/Kingdom_of_Sardinia_(1720-1861): confirmed: Treaty of Stupinigi (1817) protectorate over Monaco; /ledger/5 (Maddalena 1767-1769), /ledger/6 (Savoy 1792), /ledger/23 (Carouge 1816) also confirmed
- `/ledger/27` https://en.wikipedia.org/wiki/First_Italian_War_of_Independence: confirmed: Milan's referendum annexation 8 June; /ledger/33 Vignale terms confirmed
- `/ledger/28` https://en.wikipedia.org/wiki/First_Italian_War_of_Independence: confirmed date (5 July 1848), region overstated (only Venice held out); fixed by the reviewer
- `/ledger/44` https://en.wikipedia.org/wiki/Expedition_of_the_Thousand: confirmed: 21 October plebiscite; /ledger/42 (11 September), /ledger/43 (Ancona 29 September), /ledger/45 (November), /ledger/46 (13 February 1861) also confirmed
- `/ledger/39` https://en.wikipedia.org/wiki/Unification_of_Italy: confirmed: Savoy and Nice to France at the Treaty of Turin, 24 March 1860; /ledger/38 (22 March 1860) confirmed

Area: The Kingdom of Sardinia (1720-1861) page has no infobox area, only population (1821, 1858). The 1848 shape (134,622 km2, 1.73 times 1815) is explained month by month in the ledger, but the ledger never loses Parma (see fixes).

### corsican-republic: PASS

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Corsican_Republic: confirmed: 'proclaimed in July 1755 by Pasquale Paoli'; 'drove the Genoese from the whole island except for a few coastal towns'
- `/ledger/1` https://en.wikipedia.org/wiki/Corsican_Republic: confirmed: 'In 1767, Corsica took the island of Capraia from the Genoese'
- `/ledger/3` https://en.wikipedia.org/wiki/Treaty_of_Versailles_(1768): confirmed: concluded 15 May 1768; 'In September 1768, France began its conquest of Corsica'; Capraia 'would return' to Genoa (/ledger/2, confidence 2, honest)
- `/ledger/5` https://en.wikipedia.org/wiki/Corsican_Republic: confirmed: infobox 'Conquered: 9 May 1769', Ponte Novu May 1769; mirrored by kingdom-of-france /ledger/171

Area: No infobox area. Cliopatria's 11,217 km2 against the island's 8,680 (1.29) is cell overshoot, noted in /keyframe_review/1.

### kingdom-of-naples-napoleonic: THIN

Findings:

- `/ledger/2` (applied by reviewer): The fall of Gaeta was confidence 1, with the month read from 'almost five months'. Evidence: Siege of Gaeta (1806) infobox '26 February - 18 July 1806'; the white flag went up 'On the morning of 18 July'. Fix: Confidence 3, month 7, source Siege_of_Gaeta_(1806) added to sources[], note rewritten.

Gaps for a gap-filler:

- `/ledger (1806, 1808)`: No vassal_start/vassal_end with first-french-empire, although the dossier's own page has the infobox 'Status: Client state of the French Empire (until 1808)' and 'a French client state in southern Italy'. Rule 4 (levels of control) needs the client tint. (try https://en.wikipedia.org/wiki/Kingdom_of_Naples_(Napoleonic))
- `/ledger/5`: Murat's hold on Papal land before April 1815: he sided with Austria on 11 January 1814 (on the dossier's page) and held the Marche and Rome from 1814. In 1815 his Guard divisions crossed the Papal States, 'forcing the Pope to flee to Genoa' (Neapolitan War page). The ledger starts the Marche occupation in April 1815 and has nothing for Rome or Lazio. (try https://en.wikipedia.org/wiki/Joachim_Murat)
- `/wars/0`: Calabria is a war zone but the ledger has no contest or occupation events. The page has 'British troops defended Calabria and even scored a victory at Maida on 4 July', and Reggio and Scilla were held against the French until 1808. (try https://en.wikipedia.org/wiki/Battle_of_Maida)
- `/ledger/6`: Modena occupation start and the Modena and Florence ends (/ledger/10, /ledger/11) are confidence 1 with no dates. (try https://en.wikipedia.org/wiki/Treaty_of_Casalanza)
- `/keyframe_review/2/note`: The note says Murat's change of side is not on the page, but the page has 'Murat signed a treaty with the Austrians on 11 January 1814'. (try https://en.wikipedia.org/wiki/Kingdom_of_Naples_(Napoleonic))

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Naples_(Napoleonic): confirmed: 'On 30 March 1806, Napoleon signed an act at the Tuileries'; Capua 6 February, Joseph in Naples 15 February
- `/ledger/3` https://en.wikipedia.org/wiki/Kingdom_of_Naples_(Napoleonic): confirmed: 'In October 1808, General Jean Maximilien Lamarque captured the island of Capri from the British'
- `/ledger/5` https://en.wikipedia.org/wiki/Neapolitan_War: confirmed: headquarters at Ancona, Bologna taken 3 April; /ledger/7 Florence 'by 8 April' confirmed
- `/ledger/12` https://en.wikipedia.org/wiki/Neapolitan_War: confirmed: 'On 23 May, the main Austrian army entered Naples'; /ledger/8 Tolentino 2 May and /ledger/4 15 March confirmed
- `/ledger/2` https://en.wikipedia.org/wiki/Siege_of_Gaeta_(1806): confirmed July (18 July 1806); confidence raised by the reviewer

Area: No infobox area. All three Cliopatria shapes wrongly hold Sicily (76 cells); the corrections remove it and the Bourbon dossier carries it. Noted in keyframe_review.

### kingdom-of-naples-bourbon: THIN

Findings:

- `/ledger/5` (applied by reviewer): capital_move back to Naples (10 July 1799) at confidence 3, but the page has the king entering the Bay of Naples on a frigate, not the court returning (it stayed in Palermo until 1802). Evidence: Parthenopean Republic page: 'On 10 July 1799, King Ferdinand entered the Bay of Naples on a Neapolitan frigate, the Sirena.' Fix: Confidence lowered to 2 with a reviewer note.

Gaps for a gap-filler:

- `/identity/capitals`: capitals has Naples continuously 1735-1805, though /ledger/2 and /ledger/5 move the court to Palermo (December 1798) and back. The court's return to Naples (1802) is not on any page opened. (try https://en.wikipedia.org/wiki/Ferdinand_I_of_the_Two_Sicilies)
- `/ledger (1798)`: The Neapolitan occupation of Rome in November-December 1798. The Kingdom of Naples page has Ferdinand 'briefly occupying Rome, but was expelled from it by French Revolutionary forces within the year'. (try https://en.wikipedia.org/wiki/Kingdom_of_Naples)
- `/keyframe_review/0`: Extent 1735-1761 bridged from the 1762 shape (confidence 1; Presidi diploma of 11 December 1736 on the Presidi page). (try https://en.wikipedia.org/wiki/Charles_III_of_Spain)

Spot checks:

- `/ledger/6` https://en.wikipedia.org/wiki/State_of_the_Presidi: confirmed: 'By the Treaty of Florence of 28 March 1801, the king of Naples ceded the Presidi to the French Republic', with 'his rights on Elba (Porto Longone)'
- `/ledger/1` https://en.wikipedia.org/wiki/State_of_the_Presidi: confirmed: Spanish and allied conquest, preliminary peace October 1735 (diploma 11 December 1736)
- `/ledger/4` https://en.wikipedia.org/wiki/Parthenopean_Republic: confirmed: 'existed from 21 January to 13 June 1799'; Ruffo reached Naples 13 June; /ledger/3 'On 21 or 23 January 1799' confirmed
- `/ledger/8` https://en.wikipedia.org/wiki/Kingdom_of_Naples_(Napoleonic): confirmed: Capua 6 February, Joseph in Naples 15 February 1806; /ledger/7 Palermo 'new capital' confirmed
- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Naples: confirmed: 'on 23 December 1798, Ferdinand fled Naples to Palermo'; /ledger/0 'installed as King of Naples and Sicily from 1735' confirmed

Area: Kingdom of Naples infobox has population (c. 1600: 3,000,000), no area.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| house-of-savoy 1564 gain (swiss-confederation) | swiss-confederation 1564 loss | matched | Savoy event re-dated from 1572 by the reviewer to match swiss /ledger/32 (Republic of Geneva page). |
| house-of-savoy 1588 occupation_start (kingdom-of-france) | kingdom-of-france - - | missing | France (eu-10) has no Savoyard occupation of Saluzzo 1588-1601 (Charles Emmanuel I page: 'In the autumn of 1588 ... he occupied the Marquisate of Saluzzo'). |
| house-of-savoy 1601 occupation_end (kingdom-of-france) | kingdom-of-france - - | missing | Pair of the 1588 entry; France has only the 1601 exchange (/ledger/97-98). |
| house-of-savoy 1601 gain (kingdom-of-france) | kingdom-of-france 1601 loss | matched | Saluzzo, Treaty of Lyon (France /ledger/97). |
| house-of-savoy 1601 loss (kingdom-of-france) | kingdom-of-france 1601 gain | matched | Bresse, Bugey, Gex (France /ledger/98, Ain). |
| house-of-savoy 1631 gain (duchy-of-mantua) | duchy-of-mantua - - | exception | No dossier; listed under counterparts_needing_dossiers (eu-13-x). |
| house-of-savoy 1631 loss (kingdom-of-france) | kingdom-of-france - - | missing | France (eu-10) has no 1631 gain of Pinerolo (Cherasco). |
| house-of-savoy 1690 occupation_start (kingdom-of-france) | kingdom-of-france 1690 occupation_start | matched | France /ledger/140. |
| house-of-savoy 1696 occupation_end (kingdom-of-france) | kingdom-of-france 1696 occupation_end | matched | France /ledger/142. |
| house-of-savoy 1696 gain (kingdom-of-france) | kingdom-of-france 1696 occupation_end | mismatch | Pinerolo: Savoy has a gain (Treaty of Turin 1696); France closes only an occupation and has no loss of Pinerolo (it never records the 1631 gain). |
| house-of-savoy 1703 occupation_start (kingdom-of-france) | kingdom-of-france 1703 occupation_start | matched | France /ledger/149-150 (Savoy; Piedmont). |
| house-of-savoy 1706 occupation_end (kingdom-of-france) | kingdom-of-france 1706 occupation_end | mismatch | Matched for Piedmont (France /ledger/152), but France has Nice occupied 1707-1713 (/ledger/153, /ledger/157, County of Nice page), and Savoy ends its Nice cells in 1706. |
| house-of-savoy 1713 occupation_end (kingdom-of-france) | kingdom-of-france 1713 occupation_end | matched | France /ledger/156. |
| kingdom-of-france 1713 gain (house-of-savoy) | house-of-savoy - - | missing | France /ledger/160 gains the Ubaye from Savoy at Utrecht; Savoy has no loss (nor the Dauphine valleys gain). |
| kingdom-of-france 1559 occupation_end (county-of-savoy) | house-of-savoy 1559 found | mismatch | France /ledger/92 names county-of-savoy for the 1559 restoration; house-of-savoy begins 1559 with found (counterpart kingdom-of-france). Orchestrator to decide which slug holds 1536-1559. |
| house-of-savoy 1713 gain (kingdom-of-spain) | kingdom-of-spain 1713 loss | matched | Sicily (Spain /ledger/50). |
| house-of-savoy 1713 gain (habsburg-monarchy) | habsburg-monarchy - - | missing | habsburg-monarchy (eu-09, written during this review) has no loss to Savoy. The Savoy event is also wrong: Montferrat 1708 from Mantua (see fixes). |
| house-of-savoy 1718 occupation_start (kingdom-of-spain) | kingdom-of-spain 1718 occupation_start | matched | Spain /ledger/53. |
| house-of-savoy 1719 occupation_end (kingdom-of-spain) | kingdom-of-spain 1720 occupation_end | matched | Within one year (Spain /ledger/55 dates it to The Hague). |
| house-of-savoy 1719 occupation_start (habsburg-monarchy) | habsburg-monarchy - - | missing | Habsburg has no 1719-1720 occupation of Sicily, only the 1720 gain (/ledger/58). |
| house-of-savoy 1720 loss (habsburg-monarchy) | habsburg-monarchy 1720 gain | matched | Sicily (habsburg /ledger/58, confidence 1). |
| house-of-savoy 1720 gain (habsburg-monarchy) | habsburg-monarchy 1718 loss | mismatch | Sardinia: habsburg /ledger/54 loses Sardinia to kingdom-of-spain in 1718 (confidence 1) and has no 1720 cession to Savoy; Spain /ledger/54 returns it to habsburg-monarchy in 1720. Route to eu-09. |
| kingdom-of-sardinia 1733 occupation_start (habsburg-monarchy) | habsburg-monarchy - - | missing | Habsburg has no 1733-1738 Franco-Sardinian occupation of the Milanese. |
| kingdom-of-sardinia 1738 gain (habsburg-monarchy) | habsburg-monarchy - - | missing | Habsburg has no 1738 loss of Novara and Tortona (Treaty of Vienna). |
| kingdom-of-sardinia 1748 gain (habsburg-monarchy) | habsburg-monarchy 1743 loss | mismatch | Worms 13 September 1743 (habsburg /ledger/72, confidence 3; War of the Austrian Succession page) against Aix-la-Chapelle 1748 (sardinia /ledger/4). |
| kingdom-of-sardinia 1799 occupation_start (habsburg-monarchy) | habsburg-monarchy - - | missing | Habsburg has no 1799-1800 occupation of Piedmont. |
| kingdom-of-sardinia 1767 gain (nobody) | nobody - - | exception | Maddalena archipelago; the page names no prior owner. |
| kingdom-of-sardinia 1792 loss (french-first-republic) | french-first-republic - - | exception | eu-20 has not run; the 1796 Nice loss, the fortress-district occupations, and the 1798-1802 French entries (french-directory, french-consulate, italian-republic) are in the same position. |
| kingdom-of-sardinia 1814 gain (first-french-empire) | first-french-empire - - | exception | eu-20 has not run (two events: Piedmont; Savoy and Nice). |
| kingdom-of-sardinia 1814 gain (republic-of-genoa) | republic-of-genoa - - | exception | eu-13 republic-of-genoa not written. Cliopatria's Genoa row ends 1795 and its Ligurian Republic row runs to 1814; unless republic-of-genoa covers the restored republic of 1814, the counterpart should be ligurian-republic or first-french-empire. |
| kingdom-of-sardinia 1816 loss (swiss-confederation) | swiss-confederation 1816 gain | matched | Carouge (swiss /ledger/50). |
| kingdom-of-sardinia 1817 vassal_start (principality-of-monaco) | principality-of-monaco - - | exception | eu-10 not written; the Monaco page has the protectorate from the Congress of Vienna 1815 (Stupinigi 1817 on the Sardinia page); end now 1860. |
| kingdom-of-sardinia 1848 gain (duchy-of-parma-and-piacenza) | duchy-of-parma-and-piacenza - - | exception | eu-20 not written. The Sardinian loss of Parma in August 1848 is also missing (see fixes). |
| kingdom-of-sardinia 1848 gain (austrian-empire) | austrian-empire - - | exception | eu-20 not written. Lombardy and Venice 1848, the 1849 occupation and Lombardy 1859 are in the same position. |
| kingdom-of-sardinia 1860 gain (united-provinces-of-central-italy) | united-provinces-of-central-italy - - | exception | Listed under counterparts_needing_dossiers. |
| kingdom-of-sardinia 1860 loss (second-french-empire) | second-french-empire - - | exception | eu-20 not written. |
| kingdom-of-sardinia 1860 gain (kingdom-of-the-two-sicilies) | kingdom-of-the-two-sicilies - - | exception | eu-20 not written; papal-states (eu-13) for the Marche and Umbria is not written either. |
| kingdom-of-sardinia 1861 dissolve (kingdom-of-italy) | kingdom-of-italy 1861 found | matched | kingdom-of-italy /ledger/0, 17 March 1861. |
| corsican-republic 1767 gain (republic-of-genoa) | republic-of-genoa - - | exception | eu-13 republic-of-genoa not written (also the 1768 Capraia loss). |
| corsican-republic 1769 loss (kingdom-of-france) | kingdom-of-france 1769 gain | matched | France /ledger/171. |
| kingdom-of-naples-napoleonic 1808 gain (kingdom-of-great-britain) | kingdom-of-great-britain - - | exception | eu-11 not written (Capri). |
| kingdom-of-naples-napoleonic 1815 occupation_start (papal-states) | papal-states - - | exception | eu-13 papal-states, eu-20 duchy-of-modena-and-reggio and grand-duchy-of-tuscany not written. |
| kingdom-of-naples-bourbon 1735 found (habsburg-monarchy) | habsburg-monarchy 1734 loss | mismatch | habsburg /ledger/59 loses Naples and Sicily (352 cells) to kingdom-of-spain in 1734 (confidence 1); Spain's dossier has no 1734 gain; the Bourbon kingdom is founded 1735 from habsburg-monarchy. The habsburg counterpart should be kingdom-of-naples-bourbon. |
| kingdom-of-naples-bourbon 1735 gain (habsburg-monarchy) | habsburg-monarchy - - | missing | Presidi: habsburg has no loss of the Presidi. |
| kingdom-of-naples-bourbon 1799 loss (parthenopean-republic) | parthenopean-republic - - | exception | Listed under counterparts_needing_dossiers (eu-20). |
| kingdom-of-naples-bourbon 1801 loss (french-consulate) | french-consulate - - | exception | eu-20 not written. |
| kingdom-of-naples-bourbon 1806 loss (kingdom-of-naples-napoleonic) | kingdom-of-naples-napoleonic 1806 found | matched | The successor's found event (counterpart kingdom-of-naples-bourbon) mirrors the loss. |

## Problems for the orchestrator

- Reviewer edits applied and re-validated (0 errors, warnings unchanged): house-of-savoy /ledger/2 (1564, source Republic_of_Geneva added); kingdom-of-sardinia /ledger/28 (Venezia, confidence 2) and the Monaco vassal_end (1861 to 1860, now /ledger/40, source Monaco added; later events shift by one); kingdom-of-naples-napoleonic /ledger/2 (Gaeta 18 July 1806, source Siege_of_Gaeta_(1806) added); kingdom-of-naples-bourbon /ledger/5 (confidence 3 to 2).
- habsburg-monarchy.json did not exist when I listed history/polities and was written during this review (13:24); I cross-checked it anyway (it may be unreviewed). It has mismatches with this batch: the 1734 Naples loss goes to kingdom-of-spain instead of kingdom-of-naples-bourbon; Sardinia goes to Spain in 1718 with no 1720 cession to Savoy; it has no losses to Savoy or Sardinia for 1707-1713, 1733-1738 or 1738, and no Presidi loss. Route to eu-09.
- kingdom-of-france (eu-10) lacks mirrors for the Savoyard occupation of Saluzzo (1588-1601) and for the 1631 Pinerolo cession, and closes the 1696 Pinerolo return only as an occupation_end. Route to eu-10.
- Identity: house-of-savoy says it is the same state as county-of-savoy and kingdom-of-sardinia, but the batch splits it at Cliopatria row boundaries with dissolve/found instead of one dossier with rename events. No Savoyard dossier covers the rump duchy (Nice, Aosta, Vercelli) between county-of-savoy's row end (1539) and house-of-savoy's 1559 start. France /ledger/92 names county-of-savoy for 1559. Orchestrator decision.
- Identity: kingdom-of-naples-bourbon (new slug) shares Wikidata Q173065 and the 'Kingdom of Naples' article (1282-1816) with kingdom-of-naples (eu-13, Cliopatria 1285..1501, not yet written). Group scope asks for Spanish and Austrian rule as occupations, which suggests kingdom-of-naples may run to 1816. kingdom-of-sicily (eu-13) may also claim Sicily 1735-1814. Risk of duplicate dossiers; orchestrator to assign.
- None of the five Wikipedia articles has an infobox area, so area_check ratios are null.
- Pages that would not load for me: none.

## Gazetteer names needed

- Chambery (place, house-of-savoy)
- Saluzzo (place, house-of-savoy)
- Marquisate of Saluzzo (region, house-of-savoy)
- Pinerolo (place, house-of-savoy)
- Alba (place, house-of-savoy)
- Trino (place, house-of-savoy)
- Montferrat (region, house-of-savoy)
- Ubaye Valley (region, house-of-savoy)
- County of Nice (region, house-of-savoy)
- Lomellina (region, kingdom-of-sardinia)
- La Maddalena (place, kingdom-of-sardinia)
- Carouge (place, kingdom-of-sardinia)
- Corte (place, corsican-republic)
- Capraia (place, corsican-republic)
- Gaeta (place, kingdom-of-naples-napoleonic)
- Capri (place, kingdom-of-naples-napoleonic)
- State of the Presidi (region, kingdom-of-naples-bourbon)

## Counterparts needing dossiers

- Duchy of Mantua (with Montferrat): duchy-of-mantua [1612, 1708]
- Parthenopean Republic: parthenopean-republic [1799, 1799]
- United Provinces of Central Italy: united-provinces-of-central-italy [1859, 1860]
