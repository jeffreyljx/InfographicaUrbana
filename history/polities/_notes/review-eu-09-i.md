# Review of batch eu-09-i (2026-10-25)

Adversarial review of habsburg-monarchy, bohemian-confederacy and confederated-estates-of-hungary. All three validate (`--resolve`): 0 errors; 1 warning (habsburg-monarchy /ledger/43, Transylvania vassal with no end). Page budget: habsburg-monarchy 63 shapes, up to 14 pages (15 cited); the two rebels 1-2 pages each. Fixes marked applied were made by the reviewer in the dossier and re-validated.

## habsburg-monarchy: fail

### Fixes

- **/ledger/10/note, /ledger/10/region/text, /keyframe_review/9/note, /keyframe_review/9/correction/text, /wars/0/zones/0/text** (applied by reviewer). Quoted text 'the west and north stayed under a Habsburg king' / '1541 (Buda): After Buda fell to the Turks...' is not on the Ottoman-Habsburg wars page.
  - Why: WebFetch of https://en.wikipedia.org/wiki/Ottoman%E2%80%93Habsburg_wars: the phrase does not occur; the page reads 'After the seizure of Buda by the Turks in 1541, west and north Hungary recognized a Habsburg as king' and 'the central and southern counties were occupied by the Sultan'.
  - Fix: Quote replaced with the page's words in all five places; dossier re-validated (0 errors).
- **/ledger/20/note, /keyframe_review/18, /keyframe_review/19, /keyframe_review/20 (corrections)** (for the author). Lusatia is carved out of the 1622, 1626 and 1629 shapes on the claim that Saxony 'received' it in July 1620; the page does not say so, and Lusatia is then drawn by nobody until electorate-of-saxony gains it in 1636.
  - Why: Thirty Years' War page: 'In July 1620 ... John George of Saxony backed Ferdinand in return for the cession of Lusatia' (a promise). Electorate of Saxony page: 'In September 1620 Saxon troops marched into the two Lusatian territories and occupied them' for the emperor; 'he had to give him the two Lusatias as a pledge in 1623'; 'in an appendix to the treaty the next year gained possession of Lusatia'. electorate-of-saxony /ledger/15 (occupation_start 1620-09, c3), /ledger/17 (occupation_end 1636, c3), /ledger/18 (gain from habsburg-monarchy 1636, c3) have no mirror here.
  - Fix: Keep Lusatia in the 1620 gain from bohemian-confederacy and in the 1622/1626/1629/1632 corrections (as Habsburg land under Saxon occupation); add occupation_start 1620-09 (counterpart electorate-of-saxony, Electorate of Saxony page), occupation_end 1636 and loss 1636 to electorate-of-saxony (Peace of Prague (1635) page); correct the /ledger/20 note to the page's words.
- **/ledger/56** (for the author). Sardinia 1717-1720 is booked as a 1718 loss to kingdom-of-spain (c1), contradicting the neighbours' sourced events, and the 1720 loss of Sardinia to Savoy is missing.
  - Why: kingdom-of-spain /ledger/52: 'In August 1717, Spanish forces landed on Sardinia' (occupation_start, c3), /ledger/54 occupation_end 17 February 1720; house-of-savoy /ledger/32 gain of the Kingdom of Sardinia from habsburg-monarchy, February 1720 (c3).
  - Fix: Replace /ledger/56 by occupation_start 1717-08 (counterpart kingdom-of-spain) and add occupation_end 1720-02 and loss 1720-02 of Sardinia to house-of-savoy (Treaty of The Hague (1720) page); hatch Sardinia in the 1718 keyframe (adjust).
- **/ledger/48, /ledger/52** (for the author). The Spanish Netherlands 1706-1713 are booked as a Habsburg occupation (c1, page silent) while kingdom-of-spain books the same land as occupied by the dutch-republic (Anglo-Dutch condominium).
  - Why: kingdom-of-spain /ledger/43 (c3): 'in 1706 the Habsburg Netherlands became an Anglo-Dutch condominium'. Two occupiers for one land.
  - Fix: Drop the occupation pair here (the 1706/1709 corrections already leave the Low Countries out) or agree the occupier with eu-12; keep the 1713 gain.
- **/ledger (missing events)** (for the author). Territorial events that neighbour dossiers book against habsburg-monarchy from pages have no mirror here.
  - Why: duchy-of-bavaria /ledger/21-23 (Austrian administration of Bavaria 1704-1714, end c3) and /ledger/25-27 (occupation 1742 to October 1744, c2/c3); kingdom-of-sardinia /ledger/1-3 (Franco-Sardinian occupation of the Milanese 1733-1738 and cession of Novara and Tortona, November 1738, c2) and /ledger/19-20 (Austrian occupation of Piedmont 1799-1800, c2); kingdom-of-france /ledger/158 (Utrecht, April 1713: Ypres, Tournai, Menen, Veurne, Fort Knokke, Warneton to Austria, c3); house-of-savoy /ledger/24 (Alessandria and part of Lomellina, April 1713, c2); kingdom-of-spain /ledger/44 (Naples seized 1707, c2); kingdom-of-naples-bourbon /ledger/0-1 (Naples and Sicily 1735; Presidi May 1735); ottoman-empire /ledger/77 (Temesvar 1552, c2), /ledger/93 (Eger 1596, c3; the author's own Ottoman-Habsburg wars page: 'In 1596 Eger fell to the Ottomans.'), /ledger/94 (Kanizsa 1600, c2), /ledger/134 (Banat 1716, c2).
  - Fix: Add the mirror events (occupation pairs for Bavaria 1704-1714 and 1742-1744 and Piedmont 1799-1800; losses to kingdom-of-sardinia 1738 and to house-of-savoy 1713; gain from kingdom-of-france 1713; gain of Naples 1707; losses of Eger 1596, Kanizsa 1600 and Temesvar 1552; a 1716 gain or occupation of the Banat), each from a page; change /ledger/61's counterpart to kingdom-of-naples-bourbon.
- **/ledger/74, /keyframe_review/46, /keyframe_review/47** (for the author). The Worms cession is booked on 13 September 1743 (kingdom-of-sardinia /ledger/4 agrees) but the 1741 and 1744 keyframes, verdict ok, still draw the ceded lands until Cliopatria's 1748 shape; the 1733-1738 occupation and the 1738 cession of Novara and Tortona are absent.
  - Why: War of the Austrian Succession page confirms 'On 13 September' Worms and 'the Austrians ceded all their territories west of the river Ticino and Lake Maggiore ... along with lands south of the Po'; kingdom-of-sardinia /ledger/1-3 (c2) book the 1733 occupation and the November 1738 cession.
  - Fix: Mark 1741 and 1744 adjust (from 1743 without the lands west of the Ticino and south of the Po); add occupation_start 1733-10 / occupation_end 1738-11 and a 1738-11 loss of Novara and Tortona to kingdom-of-sardinia, from the Treaty of Vienna (1738) or War of the Polish Succession page.
- **/keyframe_review/23, /keyframe_review/27, /keyframe_review/33, /keyframe_review/46** (for the author). Keyframes marked ok whose extent contradicts the ledger: 1640 drops the Sundgau that /ledger/31 cedes only in 1648; 1653 (1653-1669) keeps Nove Zamky that /ledger/32 loses in 1663; 1696 draws Transylvania, Slavonia and the rest of Hungary that /ledger/42-43 gain only in January 1699; 1741 adds 33 Modena/Reggio/Parma cells with no ledger event.
  - Why: The author's own notes on 1640 ('Cliopatria's 1640 is early for Alsace') and 1696 ('Cliopatria's 1696 is early') say so; holy-roman-empire-minor-states /ledger/90 books the 1741 Modena cells as lost to habsburg-monarchy.
  - Fix: Mark these adjust with corrections that match the ledger (or move the events to the de facto dates with a page: Transylvania occupied 1687-1691, Breisach and the Sundgau 1638-1639), and add an occupation of Modena 1742-1748.
- **/ledger/43** (for the author). Transylvania is a vassal from January 1699 to 1805 with no vassal_end (validator warning), drawn on top of land Cliopatria already gives the Habsburgs directly from 1696.
  - Why: Karlowitz gave 'overlordship of Transylvania' (Ottoman-Habsburg wars page, confirmed); the principality ended with Rakoczi's war (page title Principality of Transylvania (1570-1711)); afterwards Transylvania was a Habsburg crown land, not a vassal state.
  - Fix: Add vassal_end in 1711 (Treaty of Szatmar) with the Principality of Transylvania (1570-1711) page, or drop the vassal tint and treat the land as direct as Cliopatria does.
- **/identity/capitals/0** (for the author). Vienna is the capital for 1487-1506, when the dossier's shape is the Burgundian Netherlands only (Vienna was Hungarian-held 1485-1490).
  - Why: shapes.csv habsburg-monarchy_1487..1502 bbox lies in Belgium, the Netherlands and France; the capital note admits the Netherlands' seat is not named.
  - Fix: Give 1487-1506 the Netherlands' seat (Mechelen or Brussels) from a page, or explain in the note why the capital lies outside the shape.
- **/ledger/0, /ledger/18, /ledger/19** (for the author). Small consistency points: the 1487 found event has no counterpart though house-of-habsburg /ledger/31 records a split into this row; the contest with bohemian-confederacy starts in May 1618, 14 months before that state exists (31 July 1619); the loss to it is dated 19 August 1619, after its foundation.
  - Why: house-of-habsburg /ledger/31; Frederick V page: 'on 31 July 1619 at Prague, these states formed the Bohemian Confederacy'.
  - Fix: Set /ledger/0 counterpart house-of-habsburg; start the contest at 1619-07 (or keep 1618 and say in the note that the counterpart is the rebellion that becomes the Confederacy); align /ledger/19 to 1619-07.

### Thin (for a gap-filler)

- /ledger/22: 1622 loss of north-east Hungary to Transylvania (c1, page silent). Try https://en.wikipedia.org/wiki/Peace_of_Nikolsburg
- /ledger/27, /ledger/28, /ledger/30: Silesia 1632-1635 and north Bohemia 1639-1642 (c1, c2); counterparts are guesses. Try https://en.wikipedia.org/wiki/Thirty_Years%27_War
- /ledger/34, /ledger/37: Thokoly's Upper Hungary 1683-1686 (c1). Try https://en.wikipedia.org/wiki/Principality_of_Upper_Hungary
- /ledger/61: 1734 loss of Naples and Sicily (c1); counterpart should be kingdom-of-naples-bourbon. Try https://en.wikipedia.org/wiki/War_of_the_Polish_Succession
- /ledger/63, /ledger/64, /keyframe_review/44: 1738 Tuscany and Parma (c1); Tuscany under Francis Stephen was a separate grand duchy, not Habsburg monarchy land: check before drawing it as such. Try https://en.wikipedia.org/wiki/Treaty_of_Vienna_(1738)
- /ledger/75, /ledger/78, /ledger/79: Bohemian cells 'lost' to Prussia 1744 and 1757-1763 (c1): these were campaign occupations of months, not cessions; book occupations or mark the keyframes adjust. Try https://en.wikipedia.org/wiki/Seven_Years%27_War
- /ledger/82-85, /ledger/89, /keyframe_review/55: 1778 +178 Bavarian cells explained only by a contest_start; Nicobar cells (c1). Try https://en.wikipedia.org/wiki/War_of_the_Bavarian_Succession
- /ledger/95, /keyframe_review/64: 1800 gain of Lombardy (c1): the Austro-Russian reconquest was 1799 and Lombardy was lost after Marengo (June 1800); the 1800-1802 shape is probably wrong. Try https://en.wikipedia.org/wiki/Treaty_of_Lun%C3%A9ville
- /ledger/96, /ledger/97, /keyframe_review/65: 1803 losses of Lombardy, Tuscany and the Breisgau (c1); the Breisgau has no event. Try https://en.wikipedia.org/wiki/German_mediatisation
- /ledger/55, /ledger/60: 1716 war start and 1720 Sicily dated from other dossiers (c1). Try https://en.wikipedia.org/wiki/Austro-Turkish_War_(1716%E2%80%931718)
- /ledger/2, /ledger/5, /ledger/12, /ledger/33, /ledger/46, /ledger/49, /ledger/50: Cliopatria-dated cell changes (Franche-Comte 1497 and 1519, north-east Hungary 1572, Trento 1673, Cremona 1702, Milan 1706, Mantua 1709), all c1. Try https://en.wikipedia.org/wiki/Treaty_of_Senlis
- /keyframe_review (17 wholly unverified shapes): 30 keyframes carry 'unverified: page budget'; not a fault under the 14-page budget. Try https://en.wikipedia.org/wiki/War_of_the_Spanish_Succession

### Spot checks

- /ledger/15: confirmed ('in the summer of 1597 ... taking Papa, Tata, Raab (Gyor) and Veszprem') (https://en.wikipedia.org/wiki/Ottoman%E2%80%93Habsburg_wars)
- /ledger/42: confirmed ('the rest of Hungary and overlordship of Transylvania for the Austrians', 1699) (https://en.wikipedia.org/wiki/Ottoman%E2%80%93Habsburg_wars)
- /ledger/10: misquoted, substance right (fixed by reviewer) (https://en.wikipedia.org/wiki/Ottoman%E2%80%93Habsburg_wars)
- /ledger/57, /ledger/58: confirmed (21 July 1718; Banat, northern Serbia with Belgrade, Posavina, Oltenia; crown lands) (https://en.wikipedia.org/wiki/Treaty_of_Passarowitz)
- /ledger/74: confirmed (13 September; west of the Ticino and Lake Maggiore, south of the Po); the year 1743 is from the link title only (https://en.wikipedia.org/wiki/War_of_the_Austrian_Succession)
- /ledger/68, /ledger/69, /ledger/70, /ledger/73, /ledger/76: confirmed (16 December 1740; Linz 14 September; Prague 26 November 1741; recaptured December; 18 October 1748) (https://en.wikipedia.org/wiki/War_of_the_Austrian_Succession)
- /ledger/80, /ledger/91: confirmed (5 August and 22 September 1772, 81,900 km2; 24 October 1795, 47,000 km2, Lublin and Krakow) (https://en.wikipedia.org/wiki/Partitions_of_Poland)
- /ledger/90: confirmed (Sprimont 18 September 1794; de facto end 1795; Campo Formio 1797) (https://en.wikipedia.org/wiki/Habsburg_Netherlands)
- /ledger/11, /ledger/9: confirmed (infobox 'Inherited by Habsburg Spain: 1556'; Groningen 1536 in a footnote) (https://en.wikipedia.org/wiki/Habsburg_Netherlands)
- /ledger/23, /ledger/24, /ledger/25: confirmed (by the end of 1627 Mecklenburg, Pomerania, Jutland; June 1629 Lubeck) (https://en.wikipedia.org/wiki/Thirty_Years%27_War)
- /ledger/20: not on page: the page has Saxony back Ferdinand 'in return for the cession of Lusatia', not receive it (c2; see fixes) (https://en.wikipedia.org/wiki/Thirty_Years%27_War)
- /ledger/13, /ledger/17, /ledger/99: confirmed (Prague 1583-1611; 'From 1804 it was referred to as the Austrian Empire'); no area on the page (https://en.wikipedia.org/wiki/Habsburg_monarchy)

Area: The Habsburg monarchy page gives no area (checked). The author compared Cliopatria's increments with the pages: Galicia 77,933 vs 81,900 km2 (0.95), Bukovina 11,271 vs 10,442 (1.08), Third Partition about 49,000 vs 47,000 (1.04); the partition figures are confirmed on the Partitions of Poland page. Cliopatria maximum 752,168 km2 (1721-1733) is plausible.

## bohemian-confederacy: fix

### Fixes

- **/ledger/1 (month, source, note), /keyframe_review/1/note, /wars/0/outcome, /identity/successors/1/note, /notes, /sources** (applied by reviewer). Lusatia was booked as lost to Saxony in July 1620 on the claim that the Thirty Years' War page has Saxony 'receive' it then; the page gives only the July 1620 agreement.
  - Why: Thirty Years' War page: 'In July 1620 ... John George of Saxony backed Ferdinand in return for the cession of Lusatia'. Electorate of Saxony page: 'In September 1620 Saxon troops marched into the two Lusatian territories and occupied them without major resistance.' electorate-of-saxony /ledger/15 is also September 1620.
  - Fix: Month 7 -> 9; source and note moved to the Electorate of Saxony page (added to sources); keyframe note, war outcome, successor note and notes reworded to the pages' words. Re-validated: 0 errors, 0 warnings.

### Thin (for a gap-filler)

- /keyframe_review/0: Upper Austria ('joined in the revolt by much of Upper Austria') and Lower Austria are not drawn; the lands actually held are undated. Try https://en.wikipedia.org/wiki/Bohemian_Revolt
- /ledger/2, /ledger/3: Surrender of Silesia and Moravia: the Frederick V page has him 'forced to leave Silesia in early 1621'; the state may outlive White Mountain in Silesia. Try https://en.wikipedia.org/wiki/Battle_of_White_Mountain

### Spot checks

- /ledger/0: confirmed ('on 31 July 1619 at Prague, these states formed the Bohemian Confederacy'; Bohemia, Silesia, Lusatia, Moravia) (https://en.wikipedia.org/wiki/Frederick_V,_Elector_Palatine)
- /ledger/1: mis-dated (July is the agreement; occupation September 1620 per the Electorate of Saxony page); fixed by reviewer (https://en.wikipedia.org/wiki/Thirty_Years%27_War)
- /ledger/2: confirmed ('Battle of White Mountain, near Prague, on 8 November 1620') (https://en.wikipedia.org/wiki/Bohemian_Revolt)
- /ledger/3, /identity/capitals/0: confirmed (fled to Breslau 9 November 1620; elected 26 August 1619; crowned in St. Vitus Cathedral 4 November 1619) (https://en.wikipedia.org/wiki/Frederick_V,_Elector_Palatine)

Area: Rebel state with no Cliopatria row and no area on the pages; drawn from the Habsburg 1600 shape minus 1619.

## confederated-estates-of-hungary: pass

### Thin (for a gap-filler)

- /keyframe_review/0-2: Transdanubia ('He continued by soon conquering Transdanubia', undated) and Transylvania are not drawn. Try https://en.wikipedia.org/wiki/Francis_II_R%C3%A1k%C3%B3czi
- /identity/capitals, /wars/0/belligerents: No seat; principality-of-transylvania as belligerent is not supported by the one page cited (it names only Rakoczi's father as prince of Transylvania). Try https://en.wikipedia.org/wiki/Francis_II_R%C3%A1k%C3%B3czi
- /ledger/2: Treaty of Szatmar undated on the page. Try https://en.wikipedia.org/wiki/Treaty_of_Szatm%C3%A1r

### Spot checks

- /ledger/0: confirmed ('controlled most of Kingdom of Hungary east and north of the Danube by late September 1703'; 15 June 1703) (https://en.wikipedia.org/wiki/R%C3%A1k%C3%B3czi%27s_War_of_Independence)
- /ledger/1: confirmed (Szecseny, September 1705, ruling prince of the Confederated Estates; Onod 13 June 1707) (https://en.wikipedia.org/wiki/R%C3%A1k%C3%B3czi%27s_War_of_Independence)
- /ledger/2: confirmed (infobox 15 June 1703 - 1 May 1711; left for Poland 21 February 1711) (https://en.wikipedia.org/wiki/R%C3%A1k%C3%B3czi%27s_War_of_Independence)
- /ledger/3: confirmed (Trencsen 3 August 1708, 'The defeat was fatal for the uprising') (https://en.wikipedia.org/wiki/R%C3%A1k%C3%B3czi%27s_War_of_Independence)

Area: Rebel state with no Cliopatria row; the page gives no area. Tried: dates of rising, Szecseny, Onod, Trencsen and the end against the page (all confirmed); the found and dissolve events mirror habsburg-monarchy /ledger/47 and /ledger/51 to the month; keyframes and the Habsburg 1703/1706/1709b corrections use the same region; certainty and the war cover 1703-1711. Thin within its 1-2 page budget only.

## Cross-dossier matrix (unmatched and mismatched only)

- habsburg-monarchy 1519 gain kingdom-of-spain (/ledger/5) -> kingdom-of-spain 1516 gain /ledger/1: mismatch. Franche-Comte is double-drawn: kingdom-of-spain /ledger/1 takes 'the Habsburg Netherlands and the Free County of Burgundy' in March 1516 (counterpart habsburg-netherlands); this dossier gains Franche-Comte from kingdom-of-spain in 1519 (c1, page silent). Route to eu-12 and the orchestrator: one owner for the Netherlands and Franche-Comte 1516-1555.
- habsburg-monarchy 1536 gain holy-roman-empire-minor-states (/ledger/9) -> holy-roman-empire-minor-states 1540 loss /ledger/46: mismatch. Groningen and Drenthe: this dossier 1536 (c2, page footnote), holy-roman-empire-minor-states 1540 (c1, Cliopatria date). Four years apart; the HRE side should move to 1536.
- habsburg-monarchy 1556 loss kingdom-of-spain (/ledger/11) -> no mirror: mismatch. kingdom-of-spain has the Netherlands and Franche-Comte from March 1516 and no 1556 gain; this dossier draws them (corrected 1529-1555) and loses them to Spain in 1556. Overlap 1529-1555 to be settled between eu-09 and eu-12.
- habsburg-monarchy 1597 gain ottoman-empire (/ledger/15) -> no mirror: missing. ottoman-empire has no 1597 loss of Papa, Tata, Gyor and Veszprem (its 1596 event is the gain of Eger from this state, which this dossier lacks). Missing on the ottoman-empire side; the Eger loss is missing here.
- habsburg-monarchy 1648 loss kingdom-of-france (/ledger/31) -> kingdom-of-france 1648 gain /ledger/106: mismatch. France books its 1648 Alsace gains from holy-roman-empire, not from habsburg-monarchy; the Sundgau was Habsburg Further Austrian land. Route to eu-10 (France) to name habsburg-monarchy for the Sundgau.
- habsburg-monarchy 1688 gain ottoman-empire (/ledger/39) -> no mirror: missing. Belgrade 1688 (c3, Great Turkish War page): ottoman-empire has no loss of Belgrade in 1688. Missing on the ottoman-empire side (me-10).
- habsburg-monarchy 1690 loss ottoman-empire (/ledger/40) -> no mirror: missing. Belgrade retaken 1690 (c3): ottoman-empire has no 1690 gain from this state (its 1691 /ledger/121 is a loss to it). Missing on the ottoman-empire side.
- habsburg-monarchy 1702 gain kingdom-of-spain (/ledger/46) -> no mirror: missing. Cremona and Landau cells 1702 (c1, Cliopatria): kingdom-of-spain has no 1702 loss. Page silent on both sides; for a gap-filler.
- habsburg-monarchy 1706 occupation_start kingdom-of-spain (/ledger/48) -> no mirror: mismatch. kingdom-of-spain /ledger/43 (c3) has the Spanish Netherlands occupied from May 1706 by dutch-republic (Anglo-Dutch condominium), not by habsburg-monarchy; this dossier's occupation (c1) claims the Habsburgs as occupier. Two occupiers for one land.
- habsburg-monarchy 1713 occupation_end kingdom-of-spain (/ledger/52) -> kingdom-of-spain 1713 occupation_end /ledger/47: mismatch. Same occupier conflict as 1706: kingdom-of-spain ends the dutch-republic occupation in 1713.
- habsburg-monarchy 1718 loss kingdom-of-spain (/ledger/56) -> kingdom-of-spain 1717 occupation_start /ledger/52: mismatch. Sardinia: kingdom-of-spain books an occupation from August 1717 (c3) ending 17 February 1720 (/ledger/54), and house-of-savoy /ledger/32 gains Sardinia from habsburg-monarchy in February 1720 (c3). This dossier has a 1718 loss to Spain (c1) and no 1720 loss to Savoy.
- habsburg-monarchy 1734 loss kingdom-of-spain (/ledger/61) -> no mirror: mismatch. kingdom-of-spain has no 1734 gain from this state; kingdom-of-naples-bourbon /ledger/0 is founded in 1735 with counterpart habsburg-monarchy (Naples and Sicily) and /ledger/1 gains the Presidi in May 1735. The counterpart here should be kingdom-of-naples-bourbon.
- habsburg-monarchy 1791 gain ottoman-empire (/ledger/88) -> no mirror: missing. Orsova 1791 (c3, Sistova): ottoman-empire has no 1791 loss to this state. Small; missing on the ottoman-empire side.
- bohemian-confederacy 1620 loss electorate-of-saxony (/ledger/1) -> electorate-of-saxony 1620 occupation_start /ledger/15: mismatch. After the reviewer's fix both sides are September 1620 (Electorate of Saxony page). Saxony books it as an occupation for the emperor with counterpart habsburg-monarchy, which is the right reading for Saxony; the rebel side is a loss to Saxony. Accept as explained; habsburg-monarchy must add the matching occupation (see its fixes).
- electorate-of-saxony 1620 occupation_start habsburg-monarchy (/ledger/15) -> no mirror: missing. c3. habsburg-monarchy has no Saxon occupation of Lusatia; it carves Lusatia out of its 1622, 1626 and 1629 corrections instead.
- electorate-of-saxony 1636 gain habsburg-monarchy (/ledger/18) -> no mirror: missing. c3 (Peace of Prague page, Traditionsrezess 1636). habsburg-monarchy has no 1635/1636 loss of Lusatia, nor the occupation_end (/ledger/17).
- duchy-of-bavaria 1704 occupation_start habsburg-monarchy (/ledger/21) -> no mirror: missing. Austrian administration of Bavaria 1704-1714 (end c3, /ledger/23); not in habsburg-monarchy.
- duchy-of-bavaria 1742 occupation_start habsburg-monarchy (/ledger/25) -> no mirror: missing. Bavaria occupied by Maria Theresa's troops 1742 to October 1744 (end c3, /ledger/27); not in habsburg-monarchy.
- holy-roman-empire-minor-states 1552 loss habsburg-monarchy (/ledger/48) -> no mirror: missing. c1, 17 cells (Flevoland, Gelderland, Noord-Holland, Utrecht); habsburg-monarchy keyframe 1552 shows the +18 cells with no ledger event.
- holy-roman-empire-minor-states 1713 gain habsburg-monarchy (/ledger/87) -> no mirror: missing. c1, 25 cells (Liege, Limburg, Namur); no habsburg-monarchy loss in 1713. Cliopatria artefact on both sides; for a gap-filler.
- holy-roman-empire-minor-states 1741 loss habsburg-monarchy (/ledger/90) -> no mirror: missing. c1, 31 cells (Modena, Reggio, Parma); habsburg-monarchy keyframe 1741 shows +33 Modena/Reggio/Parma cells with no ledger event (an occupation of Modena in the Austrian Succession war).
- house-of-habsburg 1487 split habsburg-monarchy (/ledger/31) -> habsburg-monarchy 1487 found /ledger/0: mismatch. habsburg-monarchy's found event carries no counterpart; it should name house-of-habsburg.
- house-of-savoy 1713 gain habsburg-monarchy (/ledger/24) -> no mirror: missing. c2, 'the Milanese districts (Alessandria, part of Lomellina) ceded in 1713'; habsburg-monarchy has no loss.
- house-of-savoy 1720 gain habsburg-monarchy (/ledger/32) -> no mirror: missing. c3, the Kingdom of Sardinia, 17 February 1720; habsburg-monarchy has no 1720 loss of Sardinia.
- kingdom-of-france 1713 loss habsburg-monarchy (/ledger/158) -> no mirror: missing. c3, Utrecht: Ypres, Tournai, Menen, Veurne, Fort Knokke, Warneton to Austria; habsburg-monarchy has no gain from kingdom-of-france in 1713.
- kingdom-of-naples-bourbon 1735 gain habsburg-monarchy (/ledger/1) -> no mirror: missing. c2, the Presidi, May 1735; habsburg-monarchy has neither the Presidi nor a loss to kingdom-of-naples-bourbon.
- kingdom-of-sardinia 1799 occupation_start habsburg-monarchy (/ledger/19) -> no mirror: missing. c2, Austrian occupation of Piedmont June 1799 to June 1800 (/ledger/20); not in habsburg-monarchy.
- kingdom-of-spain 1707 loss habsburg-monarchy (/ledger/44) -> no mirror: missing. c2, Naples seized by imperial troops in 1707; habsburg-monarchy gains Naples only in 1713.
- ottoman-empire 1552 gain habsburg-monarchy (/ledger/77) -> no mirror: missing. c2, the Banat of Temesvar; habsburg-monarchy has no 1551-1552 Temesvar events.
- ottoman-empire 1596 gain habsburg-monarchy (/ledger/93) -> no mirror: missing. c3, Eger. The Ottoman-Habsburg wars page, which habsburg-monarchy cites, says 'In 1596 Eger fell to the Ottomans.' Missing loss in habsburg-monarchy.
- ottoman-empire 1600 gain habsburg-monarchy (/ledger/94) -> no mirror: missing. c2, Kanizsa; habsburg-monarchy has no loss.
- ottoman-empire 1716 loss habsburg-monarchy (/ledger/134) -> habsburg-monarchy 1718 gain /ledger/57: mismatch. Banat of Temesvar: Ottoman side 1716 (conquest), Habsburg side 1718 (treaty). Two years apart; add a 1716 occupation or gain in habsburg-monarchy.
- kingdom-of-sardinia 1733 occupation_start habsburg-monarchy (/ledger/1) -> no mirror: missing. c2, Franco-Sardinian occupation of the Milanese October 1733 to November 1738 (/ledger/2); not in habsburg-monarchy.
- kingdom-of-sardinia 1738 gain habsburg-monarchy (/ledger/3) -> no mirror: missing. c2, Treaty of Vienna, November 1738: Novara and Tortona; habsburg-monarchy has no 1738 loss to kingdom-of-sardinia.

Totals: exception 45, matched 30, mismatch 11, missing 23. Exceptions are counterpart nobody, three named duchies without dossiers, and polities.csv slugs whose owner groups have not written them yet.

## Problems

- No page failed to load. The Ottoman-Habsburg wars page was fetched three times to confirm that the quoted '1541 (Buda) ... stayed under a Habsburg king' text is absent before the reviewer replaced it.
- Cross-group routing: Netherlands and Franche-Comte 1516-1555 are drawn both here and by kingdom-of-spain (eu-12); France's 1648 Alsace gain names holy-roman-empire not habsburg-monarchy (eu-10); the 1733-1738 occupation and 1738 Novara/Tortona cession booked by kingdom-of-sardinia (eu-13; that dossier was updated during this review and now books Worms in 1743 too); the 1597, 1688, 1690 and 1791 Habsburg events have no mirror in ottoman-empire (me-10).
- Lusatia 1620-1636: the reviewer chose the electorate-of-saxony reading (Saxon occupation for the emperor from September 1620, cession 1636); bohemian-confederacy was fixed accordingly; habsburg-monarchy must add the occupation pair and the 1636 loss.
- Counterpart dossiers not yet written (exception): 20 polities.csv slugs owned by eu-09 (kingdom-of-prussia part), eu-13, eu-14, eu-15, eu-18 and eu-20.
