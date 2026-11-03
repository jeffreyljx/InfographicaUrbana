# Review of batch eu-20-h (2026-11-01)

Reviewer brief filled 2026-10-31. Seven dossiers; validator (`--resolve`): 0 errors; the only warnings are the expected cross-verdict warnings between the two Danzig dossiers (one Cliopatria Name split into two states). Eleven pages opened (8 English, 3 German Wikipedia), all loaded. Machine copy: history/notes/phase-b/reviews/eu-20-h.json.

## Verdicts

| slug | verdict | in short |
| --- | --- | --- |
| principality-of-reuss-gera | pass | 4 of 5 events confirmed (9 Apr 1806, 1824, 1848, 1871); Greiz-inside acknowledged |
| principality-of-waldeck-and-pyrmont | pass | Pyrmont 1806-1812 and the 24 Sep 1812 reunion confirmed; shapes misplaced west (bbox east edge 8.83E, Korbach 8.87E, Arolsen 9.01E) |
| saxe-altenburg | pass | 12 Nov 1826, Ostkreis/Westkreis, 1,323 km2 (1905) confirmed; Cliopatria 1828-1870 shapes lack Altenburg (bbox east edge 11.96E) |
| confederation-of-the-rhine | fix (applied) | seven accession dates confirmed; note on the Hanseatic towns corrected; umbrella question escalated |
| duchy-of-warsaw | fail | dates all confirmed, but the French satellite relation is missing (first-french-empire has it) |
| free-city-of-danzig | pass | 15 Nov 1920, 1 Sep 1939, 1,952 km2 (1928) confirmed; Memel inside the 1919-1935 shapes handled |
| free-city-of-danzig-1807-1814 | fix (applied) | 21 Jul 1807, siege late Jan-29 Nov 1813, 2 Jan 1814, 478 km2 confirmed; note on France corrected |

## Findings

### duchy-of-warsaw (fail: back to the author, two events to add)

1. Missing `vassal_start` 1807-07, counterpart `first-french-empire`. The page's infobox Status reads "Satellite state of the French Empire, Personal union with the Kingdom of Saxony"; the text: "was a French client state established by Napoleon Bonaparte in 1807". first-french-empire /ledger/3 already has `vassal_start duchy-of-warsaw` 1807-07 with no mirror. Add it with the found region (Cliopatria Duchy of Warsaw 1809), confidence 3.
2. Missing `vassal_end` 1813-01, counterpart `first-french-empire` (the Russian occupation, "most of the territory of the Duchy of Warsaw was occupied by Russia in January 1813"). first-french-empire /ledger/18 has the end at 1813, confidence 1.
3. Thin: /ledger/8 (1815 loss to Prussia) names Greater Poland only; Prussia's mirror (/ledger/46) has Greater Poland and Kuyavia. Check Toruń, the Chełmno Land and the Bydgoszcz department on the Grand Duchy of Posen or Congress of Vienna page.

Everything else held: Tilsit 7 and 9 July 1807 and the constitution of 22 July 1807; Toruń de facto capital April-May 1809; invasion 14 April 1809 (infobox 10 April, noted); Schönbrunn 14 October 1809 and the ceded districts; January 1813 occupation; Congress of Vienna 9 June 1815 and its three successors. Areas: about 104,000 km2 (Cliopatria 100,411) and about 155,000 km2 (Cliopatria 1811: 146,802).

### confederation-of-the-rhine (fix, applied by the reviewer)

- /notes: the note said the page counts the three Hanseatic towns among the 1808 members; the page lists "the Free Hansa towns of Hamburg, Lübeck, and Bremen" among the lands "not included in the Confederation". Rewritten; leaving them out of the unions is right, and the gap in the author's report is void.
- Escalated to the orchestrator (not the author's fault): the dossier is `type: umbrella`. The reviewer brief (2.9) says an umbrella is never a dossier of its own; the research brief (rule 4) tells authors to use `umbrella` for associations, and the slug was assigned as owned. If it is kept, its member-accession `gain` events are exceptions in the matrix and first-french-empire's `vassal_start`/`vassal_end` on the umbrella (/ledger/2, /ledger/22) need a mirror here or a move onto the members. If it is dropped, kingdom-of-prussia should list "Confederation of the Rhine" in `cliopatria_names` so that the two shapes (Prussian land 1809-1814: bbox 11.1-22.8E, 49.5-55.9N, 170,588 km2, against Prussia's post-Tilsit size) keep their `wrong` verdicts. Prussia's dossier already draws 1809-1813 from its own new keyframe.
- Confirmed: Würzburg 23 Sep 1806, Saxony 11 Dec 1806, Anhalt/Lippe/Reuss/Schwarzburg 11 Apr and Waldeck 18 Apr 1807, Westphalia 15 Nov 1807, Mecklenburg 18 Feb and 22 Mar 1808, Oldenburg 14 Oct 1808, annexation of Oldenburg and Salm 13 Dec 1810, dissolution 4 Nov 1813, Napoleon "Protector of the Confederation". Infobox 325,700 km2 (no year).

### free-city-of-danzig-1807-1814 (fix, applied by the reviewer)

- /notes: the note said France's protection is not on the page; the infobox Status reads "Client state of the French Empire under the protection of Saxony and Prussia". Rewritten. The occupation pair (governor Rapp, the French garrison) is a defensible reading and is kept; a `vassal_start`/`vassal_end` pair with first-french-empire would fit the page equally. The author's notes file still has the old wording.
- first-french-empire has no Danzig event to mirror the occupation; kingdom-of-prussia names `free-city-of-danzig` (the interwar slug) at 1807-07 and 1815-06 and dates the return to 1815 instead of 1814 (Free City disestablished 2 January 1814). Routed to those owners.

### Passes

- **principality-of-reuss-gera**: the infobox gives 9 April 1806; the German page gives 1824 (Heinrich LIV, Lobenstein extinct) and 1848 (Heinrich LXXII abdicates in favour of Reuss-Schleiz), with Bundesstaat status in 1871. Area: 827 km2 (1905) against 2,186 km2 is a factor of 2.6. It is acknowledged in the keyframe notes: the Elder Line (Greiz) sits inside the shape, and the cells are coarse. When principality-of-reuss-greiz exists (eu-20-x), every correction must subtract Greiz.
- **principality-of-waldeck-and-pyrmont**: "from 1806 until 1812, Pyrmont was a separate principality"; the ruler table gives 24 September 1812; the 1866 war on the Prussian side is confirmed. The German page also names Hesse-Kassel's Lehnshoheit over Waldeck, ended in 1847, a nominal feudal tie. county-of-waldeck carries a `vassal_start landgraviate-of-hesse` 1431 with no end, so its owner may want to close it. Pyrmont 1806-1812 has no dossier, so the reviewer lists `principality-of-pyrmont` under counterparts needing dossiers.
- **saxe-altenburg**: "Erbteilungsvertrag vom 12. November 1826"; the Ostkreis (Altenburg, Schmölln, Gößnitz, Lucka, Meuselwitz) and the Westkreis (Eisenberg, Kahla, Orlamünde, Roda) are confirmed, with 1,323 km2 for 1905. The pre-1826 shapes are correctly left to duchy-of-saxe-gotha-altenburg. Mismatch on that dossier's side: its 1826 loss names "Saxe-Hildburghausen (no dossier)" instead of saxe-altenburg, and its dissolve gives Eisenberg to saxe-coburg-and-gotha. Thin: 1866 not treated (the pages are silent).
- **free-city-of-danzig**: established 15 November 1920; annexed 1 September 1939 (the text says "formally annexed ... in October 1939", which is noted); 1,952 km2 in 1928. Weimar's loss is dated 1920-01, so January to November 1920 is undrawn; this is in the author's gaps.

## Cross-dossier matrix (summary)

Matched: Warsaw-Prussia 1807, Warsaw-Austria 1809, Warsaw-Russia 1813/1815 (three events), Danzig-Weimar 1920, Danzig-Nazi Germany 1939, Waldeck-county of Waldeck 1806. Missing: first-french-empire vassal pair for Warsaw (Warsaw side), first-french-empire vassal pair for the Confederation (decision), first-french-empire occupation pair for Napoleonic Danzig (French side). Mismatch: Warsaw-Prussia 1815 land; Napoleonic Danzig-Prussia slug and 1814/1815 date; Saxe-Altenburg-Saxe-Gotha-Altenburg counterpart and Eisenberg. Exceptions: the Confederation's member accessions and its Oldenburg loss; the Reuss internal unions; Pyrmont (no dossier); free-city-of-krakow (eu-20 part not yet written).
