# Review of batch am-08-j (2026-10-19)

Dossiers: jamaica, republic-of-trinidad-and-tobago, antigua-and-barbuda, barbados. Each has 2 Cliopatria shapes, a 1-2 page budget, and used 2 pages. Validator (--resolve): 0 errors and 0 warnings before and after the reviewer's edits. Verdict for all four: **fix** (the reviewer made the fixes, listed below, and re-validated). Machine copy: history/notes/phase-b/reviews/am-08-j.json.

## What I tried and could not break
- Every ledger event (7) and every quoted infobox date was checked against the cited page: Jamaica 6 Aug 1962; T&T 31 Aug 1962 and republic 1 Aug 1976; Antigua associated state 27 Feb 1967 and independence 1 Nov 1981 (also in the West Indies Associated States table); Barbados 30 Nov 1966 and republic 30 Nov 2021. The quotes are on the pages. No fabricated or misdated event found.
- Areas: infobox 10,991 / 5,131 / 440 / 439 km2 against Cliopatria 13,346 / 6,177 / 586 / 735 (ratios 1.21 / 1.20 / 1.33 / 1.67). All below a factor of two, and each keyframe note gives the ratio.
- Antigua adjust: the Cliopatria bbox (16.94-17.19 N) leaves out Barbuda. The page gives the Barbuda union (1 Aug 1860) and Redonda (26 Mar 1872, parish of Saint John, about 40 km SW). The correction is correct.
- New keyframes for 1962 (Jamaica, T&T) and 1966 (Barbados) fill the year that Cliopatria misses. British Colonial Empire shapes 1958-1962, 1963-1968 and 1969-1995 agree with the author's overlap claims.
- All capitals lie inside the shape bbox, and their coordinates match the infoboxes. Each certainty span covers the whole life. No wars: correct, no ground changed hands.

## Fixes applied by the reviewer
1. All four: `west-indies-federation` was taken out of `identity.predecessors`. The schema defines predecessors as "the states whose land this state took at its birth". The Federation was disestablished on 31 May 1962 (Federation infobox), before every one of these births. For T&T, the province had already ended on 14 Jan 1962 (T&T infobox). The west-indies-federation dossier hands Jamaica to colony-of-jamaica and the remaining islands to british-colonial-empire. Its successors never listed barbados or antigua-and-barbuda. The membership facts and quotes now sit in a sentence tagged "Reviewer am-08-j" at the end of each `notes`.
2. antigua-and-barbuda: "Associated State of Antigua" was added to `alt_names`. The 1981 rename note now also records the change of name from Antigua to Antigua and Barbuda. Sources: the page has "the Associated State of Antigua", and the WIAS table has the row "Antigua".

## For other groups
- west-indies-federation (owner unknown, written in parallel): drop republic-of-trinidad-and-tobago from `successors`. T&T took its land from the British colony on 31 Aug 1962, three months after the Federation ended.
- british-colonial-empire (eu-11), not yet run. Its dossier should carry:
  - a loss of Jamaica and of Trinidad and Tobago in 1962-08 (Jamaica's mirror is in colony-of-jamaica);
  - a loss of Barbados in 1966-11;
  - a loss of Antigua in 1967-02, then vassal_start 1967-02 and vassal_end 1981-11 with counterpart `antigua-and-barbuda`, since the schema puts vassal events in the suzerain's ledger;
  - an adjust of british-colonial-empire_1963, which still holds Barbados and Antigua to 1968. Barbuda and Redonda are in no British shape.
- am-08-x: colony-of-trinidad-and-tobago, colony-of-barbados and colony-of-antigua (the author's list). When they exist, the found events' counterpart should move from british-colonial-empire to them.

## Not faults
- No maritime boundaries are coded: Venezuela-T&T, the 2006 Barbados-T&T arbitration, Pedro Bank. None moves land, and the pages are silent on them.
- The Cayman/Turks detachment date (1959 or 1962) is flagged by the author. It sits in colony-of-jamaica, outside this batch.
