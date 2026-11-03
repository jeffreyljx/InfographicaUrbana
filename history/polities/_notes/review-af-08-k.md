# Review of batch af-08-k (2026-10-25)

Reviewer: adversarial review, Phase B. Dossiers: malawi, republic-of-botswana, republic-of-the-gambia, rhodesia, zambia, equatorial-guinea. Neighbour dossiers read (ledger and wars): british-east-africa, zimbabwe-rhodesia, republic-of-zimbabwe, mozambique, people-s-republic-of-angola, south-africa, namibia, gabon, republic-of-cameroon, democratic-republic-of-the-congo, zaire. Not written yet (exception: group not run or not reached): tanzania, republic-of-senegal, estado-novo, francoist-spain.

## Mechanical
Validator (--resolve): 0 errors, 0 warnings, 0 resolve warnings for all six. Every Cliopatria shape of the six rows has a verdict (malawi 3, botswana 3, gambia 2, rhodesia 2, zambia 2, equatorial-guinea 2); new keyframes carry from, to and correction. Ledgers sorted, found at start year, dissolve at end year (rhodesia), capitals contiguous and inside the shape bboxes (Zomba, Lilongwe, Lusaka, Gaborone, Banjul, Salisbury, Malabo), certainty spans cover each life.

## Spot checks (every ledger event of the batch, 11, plus capital and war claims)
All confirmed on the pages, with the years and months: Malawi (6 July 1964; republic 6 July 1966; infobox 118,484 km2, 20.6% water), Lilongwe (capital 1975, decision 1965, last offices 2005, coordinates), Zambia (24 October 1964; 752,617 km2; border closed 1973; Lumpa undated), Botswana (30 September 1966; 581,730 km2; Gaborone 1965; Kasikili ruling December 1999), The Gambia (18 February 1965; republic 24 April 1970; 11,300 km2; coup 29 July 1981, Senegalese troops 31 July and 6 August; Senegambia dissolved 30 September 1989), Rhodesia (UDI 11 November 1965; republic 2 March 1970; Muzorewa PM 1 June 1979 and rename; infobox 390,580 km2), Equatorial Guinea (12 October 1968; 28,050 km2; capital Ciudad de la Paz since January 2026; Annobón 155 km south of the equator; ICJ 19 May 2025 on Mbanié, Cocoteros, Conga; Gabon claims since 1972), Spanish Guinea (12 October 1968 in text, 13 October in the infobox; Treaty of Paris 1900), Rhodesian Bush War (4 July 1964 - 12 December 1979; bases in Zambia and Botswana; Westlands farm October 1978; cease-fire 21 December 1979; Operation Dingo November 1977). Nothing fabricated, nothing mis-dated.

## Areas
Cliopatria / infobox: malawi 93,031 / 118,484 = 0.785 (acknowledged: the shape leaves out Lake Malawi, 20.6% water); botswana 0.993; gambia 0.993; rhodesia 1.006; zambia 0.993; equatorial-guinea 1.018. No factor of two.

## Cross-dossier matrix
- malawi found 1964-07 <- british-east-africa loss 1964-07: matched.
- zambia found 1964-10 <- british-east-africa loss 1964-10: matched.
- republic-of-the-gambia found 1965-02 <- british-east-africa loss 1965-02: matched.
- rhodesia found 1965-11 <- british-east-africa loss 1965-11: matched.
- republic-of-botswana found 1966-09 <- british-east-africa loss 1966-09: matched. The british-east-africa keyframes 1964-1967 subtract these countries year by year, so the 1967-1968 overlap of its Cliopatria shape is already resolved there.
- equatorial-guinea found 1968-10 <- francoist-spain: exception, francoist-spain (eu-21) not written yet; its Cliopatria shape keeps Spanish Guinea to 1972 (author flagged it), so that dossier needs a 1968-10 loss to equatorial-guinea and an adjust on francoist-spain_1961.
- rhodesia dissolve 1979-06 -> zimbabwe-rhodesia found 1979-06 (counterpart rhodesia): matched; zimbabwe-rhodesia -> republic-of-zimbabwe 1979-12/1980-04 continues the chain.
- War, not territory: mozambique's Mozambican Civil War (1977-1992) names rhodesia and malawi as belligerents; neither dossier carries the war. Non-blocking (no ground of theirs changed hands); listed under thin.

## Fixes applied by the reviewer (re-validated, 0 errors 0 warnings)
- rhodesia /wars/0/from: 1964 -> 1965 (the Bush War began 4 July 1964, before the state's start, 11 November 1965; brief check 2, wars inside the life). Note extended to say so.
- republic-of-botswana /wars/1/from: 1964 -> 1966 (same war, before independence on 30 September 1966).
- equatorial-guinea /wars/0/to: 2025 -> 2024 (the dossier ends 2024; the ICJ ruling of 19 May 2025 stays in the outcome).

## Verdicts
- malawi: pass. Tried: dates, capital move, area, overlap with british-east-africa, lake. Thin by design within the 1-2 page budget: no lake frontier (Lake Malawi dispute with Tanzania) and no Mozambican Civil War entry.
- zambia: pass. Tried: date, area, Bush War claims, frontier statements. Barotseland Agreement and Lumpa date not on the pages (author flagged).
- republic-of-the-gambia: pass. Tried: dates, area, coup war entry, Senegambia handling (correctly not territory). Bathurst/Banjul rename undated (it was 1973; page silent, no map effect).
- republic-of-botswana: fix (applied). W1 lists Botswana as a belligerent of the Bush War although the author says it was not a combatant; acceptable as a no-zone record but could be dropped by the author.
- rhodesia: fix (applied). Optional: the Rhodesia infobox reads 'Zimbabwe Rhodesia: 1 June 1979', so /ledger/2 could stand at confidence 3 (the note says the page does not tie the rename to the date). Mozambican Civil War (Rhodesian backing of RENAMO from 1977) not in wars.
- equatorial-guinea: fix (applied). Annobón still 0 cells: the region grammar allows {"lon": 5.63, "lat": -1.43, "km": r} for an island with no gazetteer place; the gazetteer agent should decide.

## For the orchestrator
- Senegambia Confederation (1982-1989): an association, not territory (no Cliopatria row). The author asks for an umbrella dossier; under the rules umbrellas never get a dossier of their own, so at most a relation entry; nothing for the map.
