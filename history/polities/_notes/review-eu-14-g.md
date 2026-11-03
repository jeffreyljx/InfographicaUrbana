# Review of batch eu-14-g (Denmark-Norway), 2026-10-25

Reviewer: adversarial review, Phase B. Dossiers: `denmark-norway` (1526 to January 1814) and `kingdom-of-denmark-1814-1940` (new slug, split from the same Cliopatria row). Machine copy: `history/notes/phase-b/reviews/eu-14-g.json`.

Verdicts: **denmark-norway: fix** (4 fixes applied by the reviewer; 4 non-blocking items for the author or the owning groups; gaps listed). **kingdom-of-denmark-1814-1940: fix** (2 fixes applied; the 1940 end needs an orchestrator decision; wikidata to check).

## Mechanical

`validate_dossier.py --resolve`: 0 errors before and after the reviewer's edits. The only warnings are 8 and 22 "has no verdict" warnings, one per shape of the other half of the split row (expected). Years are ordered. Each dossier's found and dissolve events fall on its start and end. Wars and certainty lie inside each life. Capitals (Copenhagen) are inside the shapes; family `nordic` is in colours.json.

## Spot checks (all pages opened by the reviewer)

denmark-norway. Brömsebro, 13 August 1645, with the ceded list and Halland for 30 years: confirmed. Roskilde, 26 Feb (OS) / 8 Mar (NS) 1658, with the ceded list: confirmed. Copenhagen 1660, Trøndelag and Bornholm: confirmed. Bremen-Verden, occupied 1712 and sold 1715: confirmed. Holstein-Gottorp, 1658/1660 sovereignty in Schleswig and the 1773 Oldenburg exchange: confirmed; no year for the Great Northern War occupation, so confidence 1 is correct. Lübeck, September 1627 invasion and 22 May 1629: confirmed. Frederiksborg, 3 July 1720, 'full control over Schleswig': confirmed. Kiel, 14 January 1814: confirmed. Denmark-Norway infobox, 1537 and area: confirmed. No fabricated or mis-dated event was found.

kingdom-of-denmark-1814-1940. Lauenburg 1815 (Kiel page, no exact date): confirmed. First Schleswig War, March 1848 and 1 April 1851: confirmed. Second Schleswig War, 30 October 1864: confirmed. Kingdom of Iceland, 1 December 1918: confirmed. The 1920 reunification is confirmed; the Denmark page dates it 10 July 1920. The 1940 invasion date is confirmed, but the page does not support a dissolution (below).

## Fixes applied by the reviewer (re-validated)

1. denmark-norway `/identity/successors/1`: the successor was `united-kingdoms-of-sweden-and-norway`, with the claim that Norway has no shape in 1814. That is wrong: Cliopatria's Kingdom of Norway row (1814-2024) has `kingdom-of-norway_1814`. Now `kingdom-of-norway` with land `{cliopatria: Kingdom of Norway, year: 1814}`. The author's request for a `kingdom-of-norway-1814` dossier is void.
2. denmark-norway `/notes` and the 1526 keyframe note, and kingdom-of-denmark-1814-1940 `/notes`: these said Greenland is in no Cliopatria shape. Cliopatria has a separate **Greenland** row (1734-1940, 24 shapes; 102,479 km2 in 1788-1804, 2,219,796 km2 from 1936). The texts now point to it.
3. denmark-norway `/ledger/24`, `/ledger/26`, keyframe `denmark-norway_1659` note: the Roskilde page says 'Trøndelag then included Nordmøre and Romsdal', so the 46 Møre og Romsdal cells are named after all. Added `intersect(minus(DN 1645, DN 1659), admin1 Møre og Romsdal)` to the 1658 loss and the 1662/1659 equivalent to the 1660 gain (46 cells each).
4. denmark-norway `/identity/rulers/0`: Frederick I's span now starts in 1526, inside the life; the note keeps the 1523 accession.
5. kingdom-of-denmark-1814-1940 `/ledger/11`: month 7 and source `Denmark` ('On 10 July 1920, Northern Schleswig was recovered by Denmark'), added to sources[]; the 1920 keyframe note is updated.

## Open findings (not applied, not blocking)

- denmark-norway keyframe `denmark-norway_1564` (adjust): it keeps Cliopatria's removal of about 330 Jämtland, Härjedalen and Idre-Särna cells for 1564-1569, but the ledger holds only the 1563-1570 contest. Elsewhere (1629, 1713-1720) the dossier keeps occupied land in the owner's base. Either add occupation_start 1564 / occupation_end 1570-12 (counterpart kingdom-of-sweden) and an Älvsborg occupation pair (Denmark occupies, 1563 to 1571) and restore the cells, or say in the note that the contest blend stands in for the occupation.
- denmark-norway `/ledger/14`, `/ledger/16` (Holstein and Jutland 1627-1629, contest against habsburg-monarchy): habsburg-monarchy records an **occupation** (1627 to 1629-6, counterpart denmark-norway). The Lübeck page speaks of 'the imperial occupation forces'. Add the occupation pair so that the two ledgers mirror.
- denmark-norway `/ledger/13`, `/ledger/15` (Lower Saxon contest, counterpart habsburg-monarchy): holy-roman-empire-minor-states records the same contest with denmark-norway (its /ledger/57-58), and the land is its own. Align the counterpart.
- denmark-norway `/ledger/37` (Norway lost to swedish-empire, January 1814): this follows the Kiel page, but in 1814 Cliopatria draws Norway as kingdom-of-norway. Note this so that the Swedish group does not draw a gain, or change the counterpart.
- kingdom-of-denmark-1814-1940 `/ledger/12` (dissolve 1940-4, confidence 3): the cited page says the government 'remained functioning de jure until the end of the war'. The Danish kingdom of 1814 is also the same state as Cliopatria's **Denmark** row (1945-2024, another group). Orchestrator decision: preferably one dossier (both Names, from 1814) with a German occupation 1940-4 to 1945-5. At minimum, make the dissolve an occupation pair and extend the end to 1945-5.
- kingdom-of-denmark-1814-1940 `/identity/wikidata` Q350186: data/README.md lists it as shared by Danish Magnates / Denmark (the Danish Magnates row's page is Christopher II of Denmark). Use Q35 after checking, or omit it.

## Gaps (for a gap-filler)

denmark-norway, confidence-1 events: the 1526 start; the 1572 losses of Wiek and Pilten (Pilten was sold to Poland in 1585); the 1595 East Finnmark gain (Treaty of Teusina); the 1619 Älvsborg ransom (Treaty of Knäred); the 1622 lower-Elbe cells; the 1713 Gottorp occupation; the 1807 3 cells; the 1809 Finnmark cell.

Missing from the ledger:
- the Torstenson War's Swedish occupation of Jutland and Scania (1643-1645);
- the Scanian War (1675-1679; the page says Denmark-Norway 'invaded Sweden in 1675');
- Danish-held Swedish Pomerania and Rügen, 1715-1720 (Frederiksborg page: 'Danish-held areas of Swedish Pomerania were returned to Sweden');
- Bremen-Verden under a Danish administrator, 1635-1645 (Brömsebro page: 'from Danish to Swedish control');
- Heligoland, occupied by Britain in 1807 and ceded at Kiel (Kiel page: George III 'granted full and unlimited sovereignty'); it is in neither this nor the united-kingdom ledger;
- the relation to the Greenland colony row.

kingdom-of-denmark-1814-1940: Denmark under German occupation, 1940-1945; the Faroes under British occupation from 12 April 1940; the exact year of the Lauenburg handover (1815 or 1816).

## Area checks

- denmark-norway: the infobox gives 2,655,567 km2 (1800), of which Greenland is 2,166,086. The Cliopatria shape for 1775-1806 is 526,384 km2, a ratio of 5.04. The ratio is acknowledged in the 1526 keyframe note: without Greenland, 489,481 against 526,384.
- kingdom-of-denmark-1814-1940: the Denmark infobox (modern) gives 43,094 km2, plus 1,399 km2 for the Faroes, against 53,400 km2 for shape `denmark-norway_1922` (0.83). The Second Schleswig War page puts the 1864 loss at 40%; Cliopatria gives about 27-32% without Iceland. Both are well inside a factor of two.

## Cross-dossier matrix (summary; full list in the JSON)

- holy-roman-empire-minor-states (eu-09), Gottorp Schleswig 1658: DN 1658, HRE 1662. Mismatch.
- holy-roman-empire-minor-states, Oldenburg 1667: DN 1667, HRE 1670. Mismatch.
- holy-roman-empire-minor-states, Gottorp Schleswig 1713-1720: DN has an occupation in 1713 and a gain in 1720; HRE has a loss in 1713 and nothing in 1720. Mismatch.
- holy-roman-empire-minor-states, Oldenburg 1773: DN 1773, HRE 1775. Mismatch.
- holy-roman-empire-minor-states has no mirror for the 1622 lower-Elbe gain or for the 1773 ducal-Holstein gain. Missing.
- habsburg-monarchy, 1627-1629: Habsburg records an occupation where DN records a contest. Mismatch.
- habsburg-monarchy and holy-roman-empire-minor-states, Lower Saxon contest: the counterparts disagree. Mismatch.
- electorate-of-hanover, Bremen-Verden 1715: matched.
- All Swedish, Russian, Polish-Lithuanian, French, Prussian, German Confederation, Austrian, Holstein, Iceland and Weimar counterparts: exceptions, because their dossiers are not written yet.
