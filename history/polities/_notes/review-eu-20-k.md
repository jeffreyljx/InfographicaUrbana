# Review of batch eu-20-k (2026-10-31)

Reviewer: adversarial review, Phase B. Validator (`--resolve`) on all six dossiers: 0 errors before and after the reviewer's edits; warnings are gazetteer gaps only (Gaeta, Civitella del Tronto, Venlo, Elten, Sankt Wendel) and the slugs allied-occupied-germany and grand-duchy-of-frankfurt, which have no dossier yet.

Neighbour dossiers read (ledger greps): kingdom-of-sardinia, papal-states, electorate-of-hesse, kingdom-of-bavaria, kingdom-of-spain, denmark-norway, kingdom-of-great-britain, united-states-of-america (context list); also kingdom-of-prussia, kingdom-of-naples-napoleonic, kingdom-of-naples-bourbon, co-principality-of-andorra, kingdom-of-sweden, netherlands-antilles (counterparts named in the ledgers). Not written yet (their groups have not run): kingdom-of-belgium, luxembourg, sovereign-principality-of-the-united-netherlands, first-french-empire, kingdom-of-norway, swedish-empire, italian-nationalists, nazi-germany, federal-republic-of-germany.

| slug | verdict | in short |
| --- | --- | --- |
| kingdom-of-the-two-sicilies | fix (applied) | Calabria loss and contest_end were dated September at confidence 1; the page dates them to August. Fixed |
| netherlands | fix (applied) | 1815 gain counted Belgian Luxembourg both as direct land and as personal-union land; 2010 Caribbean gain was missing (mirror of netherlands-antilles). Both fixed |
| principality-of-andorra | pass | |
| united-kingdoms-of-sweden-and-norway | pass | |
| free-city-of-frankfurt | fail | Cliopatria's cell sits on Mainz and Rüsselsheim, not Frankfurt; all four keyframes keep it |
| principality-of-lichtenberg | fix (applied) | the notes said the page names no earlier holder; it names the Département de la Sarre. Fixed |

## kingdom-of-the-two-sicilies: fix (applied by reviewer)

- /ledger/10 and /ledger/11 (Calabria loss and contest_end) were dated 1860-09 at confidence 1, and the note said the page gives no date. The Expedition of the Thousand page says: 'On 19 August Garibaldi's men disembarked in Calabria'; Reggio was 'conquered ... by Nino Bixio on 21 August'; 'On 30 August the Bourbon army ... was disarmed in Soveria Mannelli and surrendered without a fight'. The reviewer changed both to 1860-08 at confidence 2, rewrote the notes, and updated the matching sentence in `notes`.
- Spot checks, all confirmed on the page:
  - L4: 12 January 1848 (Sicilian revolution page).
  - L5: 15 May 1849.
  - L7: Sicily lost in August 1860. 'On 6 June the Bourbon troops defending the Sicilian capital capitulated'; 'On 1 August the Bourbon fortresses of Syracuse and Augusta also capitulated, concluding the conquest of Sicily'.
  - L13: Gaeta capitulated 13 February 1861 (Siege of Gaeta page).
  - L14: Messina, 17 March 1861 (Expedition page).
  - L15 and L16: Civitella del Tronto, 20 March 1861.
- Area: the infobox gives 111,900 km2 for 1860. The whole-kingdom shape is 91,430 km2 (ratio 0.82), and the author acknowledged this.
- Advisory, not blocking: the Volturno, Capua and the siege of Gaeta (from 5 November 1860) have war zones but no contest_start/contest_end pair. Sardinia's ledger has contest_start 1860-05 and contest_end 1861-02 over the whole kingdom. A contest over Gaeta from 1860-11 to 1861-02 would mirror it.

## netherlands: fix (applied by reviewer)

- /ledger/1: the 1815 gain was `{"country": "Belgium"}`, which includes the Belgian province of Luxembourg. /ledger/2 makes the same province personal-union land (vassal_start), and keyframes 0-2 take it out of the direct outline. The reviewer rewrote the region as Belgium minus admin1 Luxembourg (Belgium), the form /ledger/6 already uses.
- Missing event /ledger/21, added by the reviewer. netherlands-antilles /ledger/19 hands Bonaire, Sint Eustatius and Saba to `netherlands` on 10 October 2010, and this ledger had no mirror. The Netherlands page (already in `sources`) gives the infobox line 'Caribbean reorganisation: 10 October 2010' and the sentence 'Bonaire, Sint Eustatius and Saba were incorporated as special municipalities'. The event is a gain at confidence 3, counterpart netherlands-antilles.
- Advisory, not applied:
  - /ledger/11 records a 1839 loss of Belgian Luxembourg to Belgium. Its own note admits the Netherlands never held this land directly; after the L1 fix it removes nothing and only gives Belgium's gain a pair. The right pair for Belgium's 1839 gain is the Grand Duchy (luxembourg), whose dossier must be extended back to 1815 (the author flagged this). Drop L11 once that dossier exists.
  - /keyframe_review/3 adds Venlo to the 1834-1839 outline. The reason given is the Duchy of Limburg page's 'minus its two major cities, Maastricht and Venlo', but that phrase is about the 1839 duchy and the German Confederation, not about who held Venlo from 1830 to 1839. The same page says Limburg was 'controlled by Belgium until 1839'. The Belgian Revolution page says only that the army 'was withdrawn to the fortresses of Maastricht, Venlo, and Antwerp' in 1830, and the Venlo page says nothing on the point. The author should check whether Belgian forces took Venlo in late 1830. If they did, drop Venlo from K3 and add it to the 1839 Limburg gain.
- Spot checks, all confirmed on the page:
  - L6: independence declared 4 October 1830 (the lead says 27 September).
  - L9: Antwerp citadel taken 23 December 1832.
  - L13 and L14: Treaty of London, 19 April 1839; the Dutch kept Maastricht and the eastern half of Limburg.
  - L19: 23 April 1949, 69 km2, Elten, Selfkant and Suderwick.
  - L20: returned 1 August 1963 under the treaty of 8 April 1960. The Duivelsberg (about 3 km2) stayed Dutch, as the K14 note says.
- Area: the infobox gives 41,865 km2 against 38,295 (ratio 0.91). The author's figure for the United Kingdom of the Netherlands is 68,095 against 71,126 (ratio 1.04).
- Thin within the 9-page budget:
  - Cliopatria's area changes in 1922, 1924, 1930 and 1936 are unexplained. The Netherlands page dates the Afsluitdijk to 1932 and says the Zuiderzee Works reclaimed 2,500 km2; Zuiderzee_Works is the page to try.
  - Rulers are not listed.

## principality-of-andorra: pass

- L0: the History of Andorra page says 'In 1814, an imperial decree reestablished the independence and economy of Andorra'.
- The 1812-1813 annexation (department of Sègre) and 'Andorra's borders have remained unchanged since 1278' are confirmed.
- W1: 'From 1936 to 1940, a French detachment was garrisoned in Andorra' is confirmed.
- Area: 380 km2 against the infobox 468 km2 (ratio 0.81), acknowledged.
- Thin: the page has 'In 1933, France occupied Andorra as a result of social unrest before elections' with no end date. The author left it out, defensibly, since France's head of state is a co-prince.
- The 1814 found event's counterpart is first-french-empire, which matches co-principality-of-andorra's 1812 loss to first-french-empire.
- The orchestrator should decide whether to merge this dossier with co-principality-of-andorra (the author flagged it).

## united-kingdoms-of-sweden-and-norway: pass

- Confirmed on the union page:
  - 4 November 1814: 'the Storting elected Sweden's king, Charles XIII, as the King of Norway'.
  - The Act of Union of 15 August 1815.
  - The Storting's declaration of 7 June 1905.
  - Lead: 'Sweden accepted the union's dissolution on 26 October'.
  - Hvaler, 27 July 1814, and the Convention of Moss, 14 August 1814 (W0).
- The infobox gives no area, confirmed. By reckoning, Sweden at about 450,000 km2 plus mainland Norway at about 324,000 km2 is about 774,000 km2 against 804,282 (ratio about 1.04).
- Nit: L0 found uses the whole union shape (Norway included) and L1 then gains Norway again. Using `{"cliopatria": "Swedish Empire", "year": 1814}` for L0, as the predecessor entry does, would be cleaner. Harmless.
- Thin by design (1-2 pages): the 1826 Norway-Russia frontier in Finnmark is not on the page.

## free-city-of-frankfurt: fail

- Blocking, /keyframe_review/1 and /2 (verdict ok), with /0 and /3 copying the same cell:
  - The Cliopatria cell has bbox 8.2607-8.4306 E, 49.98-50.113 N and centroid 8.346 E 50.046 N (shapes.csv and the seed). That places it round Mainz-Kastel and Rüsselsheim.
  - Frankfurt am Main is at 8.68 E 50.11 N (gazetteer 8.675/50.10; the dossier's own capital 8.6821/50.1109), about 25 km east of the centroid and outside the bbox.
  - Fix: verdict adjust on K1 and K2, and on all four keyframes the correction `{"place": "Frankfurt", "km": 7, "country": "Germany", "text": "the Free City: Frankfurt am Main with its eight villages and forest district"}` (or km 8, as the ledger uses). Say in each note that Cliopatria's cell is misplaced. The ledger already uses place Frankfurt and is right.
- Missing event: 'On 16 July 1866 the undefended city was occupied by the Prussian Army' is on the page and in K3's note, but there is no occupation_start 1866-07 (counterpart kingdom-of-prussia) to go with the annexation of 20 September. Add it, with occupation_end 1866-09 or let the loss close it.
- Confirmed: 'Restored: 9 July 1815' (infobox) and annexation 'by decree of the King of Prussia on 20 September' 1866. The infobox gives no area, only the forest district (4,480 ha) and the City Forest (about 40 km2).
- Cross-dossier: kingdom-of-prussia /ledger/68 gains `{"cliopatria": "Free City of Frankfurt", "year": 1820}`, the same misplaced cell. Route this to the Prussia owner.

## principality-of-lichtenberg: fix (applied by reviewer)

- /ledger/0/note and the PREDECESSOR paragraph of `notes` said the page does not name the previous holder. The page says 'The future Lichtenberger lands became part of the Département de la Sarre in 1798' (before that mostly Palatinate-Zweibrücken, with St. Wendel under the Prince-Bishops of Trier). The reviewer corrected both texts. The counterpart stays `nobody`: the page names no holder between Napoleon's fall and the 1816 grant. Optional: add first-french-empire as a predecessor once that dossier exists.
- Confirmed: possession made official 11 September 1816 ('Herrschaft Baumholder'), renamed 6 March 1819, sold to Prussia 15 August 1834, infobox area 537 km2.
- Area: the Cliopatria cell is 179 km2 (ratio 0.33). The author acknowledged it and corrected it with a 12 km circle round Sankt Wendel, which gives about 630 km2.
- Cross-dossier: kingdom-of-prussia has no 1834 gain of Lichtenberg (Kreis Sankt Wendel). Route this to the Prussia owner.

## Cross-dossier matrix (summary; the full list is in the JSON report)

- Matched:
  - Two Sicilies 1815 found and kingdom-of-naples-napoleonic 1815-05 dissolve.
  - The Sicily part and kingdom-of-naples-bourbon 1814 dissolve (within a year).
  - Two Sicilies 1860-61 losses and kingdom-of-sardinia 1860-10 gain plus 1861-02 contest_end.
  - Frankfurt 1866-09 loss and Prussia 1866-08 gain.
  - Sweden-Norway 1905 dissolve and the kingdom-of-sweden 1905 restart.
  - Netherlands 2010 gain and netherlands-antilles 2010-10 loss (added by the reviewer).
- Missing: Lichtenberg 1834-08 loss to Prussia has no gain in kingdom-of-prussia.
- Exceptions (counterpart not written yet): kingdom-of-belgium, luxembourg, sovereign-principality-of-the-united-netherlands, nazi-germany, allied-occupied-germany, federal-republic-of-germany, italian-nationalists, first-french-empire, swedish-empire, kingdom-of-norway, grand-duchy-of-frankfurt.
