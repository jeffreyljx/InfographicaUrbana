# Review of batch am-08-l (2026-10-24)

Dossiers: commonwealth-of-dominica, saint-lucia, belize. republic-of-brazil was not written on purpose: its two shapes (republic-of-brazil_1987, _2024) are reviewed `ok` inside brazilian-republic.json, whose cliopatria_names list all four Q155 rows. Confirmed; no dossier is missing.

Mechanical: validate_dossier.py --resolve, 0 errors and 0 warnings for all three (before and after the reviewer fix). Every Cliopatria shape has a verdict; the new keyframes (1967-1978 for Dominica and Saint Lucia, 1981-1982 for Belize) carry from, to and a correction. found events at start.year; no dissolve (alive in 2024). Capitals inside the shapes' bboxes (Roseau, Castries, Belmopan). Family `americas` exists in colours.json.

Neighbour dossiers present and read: british-honduras, guatemala, mexico, venezuela (the only ones that touch these three). british-colonial-empire (eu-11) and french-fifth-republic (eu-22) are not written yet.

## commonwealth-of-dominica: pass

Spot checks (Dominica, West Indies Associated States pages): /ledger/0 confirmed ('became an associated state of the United Kingdom in 1967'; infobox 'West Indies Associated States: 1 March 1967'; WIAS table 'Dominica | 1 March 1967 | 3 November 1978'); /ledger/1 confirmed ('On 3 November 1978, Dominica was granted independence as a republic'); /keyframe_review/1 area confirmed (infobox 750 km2); predecessor 1763 Treaty of Paris confirmed. Area: infobox 750 km2 against Cliopatria 1,262.9 km2, ratio 1.68, acknowledged in the keyframe note. Aves Island: the page gives only the June 2006 end of the claim; left out correctly (sea). Could not break it.

## saint-lucia: pass

Spot checks (Saint Lucia, WIAS): /ledger/0 confirmed ('In 1967, Saint Lucia became one of the six members of the West Indies Associated States, with internal self-government'; infobox 1 March 1967); /ledger/1 confirmed ('On 22 February 1979, Saint Lucia became an independent state'); /keyframe_review/1 area confirmed (617 km2); 1814 British control confirmed. Area ratio 790.6/617 = 1.28, acknowledged. Minor, not a fault: the capital note says the page gives no coordinates; the infobox does give 'Castries 13°53'N 60°58'W', which is the island's centre rather than the town, so the gazetteer point used (14.002, -61.0) is the better one.

## belize: fix (applied by the reviewer)

Spot checks: /ledger/0 confirmed on both pages ('Belize achieved its independence from the United Kingdom on 21 September 1981'; History: 'Independence came to Belize on 21 September 1981 after the Belize Act 1981, without reaching an agreement with Guatemala'); the 1,500-troop and 1994 quotes are on the Belize and History pages; /keyframe_review/1 area confirmed (infobox 22,966 km2, body 22,970 km2; ratio 1.00); capital sentence confirmed (no date for the move on the page).

Finding, applied: /wars/0 ended in 2008 and its outcome said the referendums 'have not taken place as of March 2019' (a stale sentence of History of Belize). The Belize page the author opened reports the Guatemalan referendum of April 2018 and the Belizean one of May 2019, and the dedicated article, which does exist at https://en.wikipedia.org/wiki/Belizean%E2%80%93Guatemalan_territorial_dispute (the author tried 'Belize–Guatemala ...' titles only; guatemala.json and british-honduras.json already cite it), says 'Guatemala recognised Belize's independence in 1991', the Special Agreement 'was signed on 8 December 2008', referendums 15 April 2018 and 8 May 2019, and the case was still before the ICJ (written phase closed June 2023). guatemala.json's matching war runs 1859-2024. Changed: /wars/0/to 2008 -> 2024; outcome rewritten from the dispute page; /wars/0/source -> the dispute page; reviewer sentence appended to /wars/0/note and /notes; the page added to /sources. Re-validated: 0 errors, 0 warnings.

## Cross-dossier matrix

- belize 1981-09 found (cp british-honduras) <-> british-honduras 1981-09 dissolve (cp belize), successors/predecessors agree: matched.
- commonwealth-of-dominica 1967-03 found (cp british-colonial-empire): exception, eu-11 has not run; british-colonial-empire should release the island in 1967 and carry vassal_start/vassal_end with counterpart commonwealth-of-dominica (1967-03 .. 1978-11).
- saint-lucia 1967-03 found (cp british-colonial-empire): exception, as above (1967-03 .. 1979-02).
- belize /wars/0 1981-2024 <-> guatemala /wars/4 1859-2024 (after the fix): matched; both have no zones, which the dispute page supports ('never occupied any part of Belize').

## For the orchestrator

- Convention clash with batch am-08-k: grenada, saint-vincent and saint-kitts carry vassal_start/vassal_end in their own ledgers with counterpart british-colonial-empire, which by the schema wording ('counterpart is the vassal itself') reads as Britain being their vassal. am-08-l followed the schema and left the relation to the suzerain's dossier. One convention should be chosen before eu-11 writes british-colonial-empire.
