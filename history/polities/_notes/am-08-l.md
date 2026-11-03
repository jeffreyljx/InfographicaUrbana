# am-08-l notes (Dominica, Saint Lucia, Belize, Brazil 1987-2024), written 2026-10-25

Three dossiers written, all validate with 0 errors and 0 warnings (also with --resolve): commonwealth-of-dominica, saint-lucia, belize. The fourth owned slug, republic-of-brazil, gets NO dossier of its own: it is already inside brazilian-republic (see below). Pages opened: Dominica, Saint Lucia, West Indies Associated States, Belize, History of Belize, Brazil, History of Brazil (1985-present). One page group failed (Belize-Guatemala dispute article, four URL variants).

## Conventions used

- Family `americas`, as the am-08-k siblings (grenada, saint-vincent, antigua-and-barbuda, jamaica, barbados).
- Start year: the Associated State date (1 March 1967) for Dominica and Saint Lucia, as the siblings do; independence (21 September 1981) for Belize, whose colony is the separate dossier british-honduras. Independence of an Associated State is a `rename` (status change); the state does not change colour.
- Associated-State client relation to the UK (UK kept external affairs and defence): coded NOT here but left to the suzerain dossier, as the schema says ('counterpart is the vassal itself'). eu-11's british-colonial-empire should carry vassal_start/vassal_end naming commonwealth-of-dominica (1 Mar 1967 .. 3 Nov 1978) and saint-lucia (1 Mar 1967 .. 22 Feb 1979).
- Every Cliopatria shape of the three islands is a rough 7-vertex (Belize 34-vertex) polygon that resolves to fewer 253 km2 grid cells than Natural Earth's outline (Dominica 2 vs 3, Saint Lucia 2 vs 4, Belize 75 vs 84), so all verdicts are `adjust` with the country outline as the correction. For Saint Lucia the polygon omits the north of the island, where Castries lies.

## Per state

- commonwealth-of-dominica: 2 pages (Dominica, West Indies Associated States). Infobox 750 km2 vs Cliopatria 1,262.9 (ratio 1.68). New keyframe 1967-1978; Cliopatria 1979-2023 and 2024 adjusted. Events: found 1967-03 (Associated State), rename 1978-11 (independence). No wars: the 1981 coup attempts and mercenary plot and the Aves Island maritime dispute with Venezuela were considered and left out (no land border effect; the page dates the dispute only by its June 2006 end).
- saint-lucia: 2 pages (Saint Lucia, West Indies Associated States). Infobox 617 km2 vs Cliopatria 790.6 (ratio 1.28). Events: found 1967-03, rename 1979-02. The page records no dispute or border change after 1979.
- belize: 2 pages (Belize, History of Belize). Infobox 22,966 km2 vs Cliopatria 22,878.8 (ratio 1.00). Events: found 1981-09 (counterpart british-honduras). One war entry, 'Guatemalan claim to Belize (no war)' 1981-2008, with no zones: there was no campaign, so no contest_start. Disagreement: year of Guatemala's recognition of Belize (Belize page implies 1991, History page says 1992). Capital Belmopan from 1981; neither page dates the move (british-honduras dossier has 1971 from its own page).
- republic-of-brazil: NO dossier. Four Cliopatria rows share Wikidata Q155 (Brazilian Republic, Unitary State of Brazil, Federated Republic of Brazil, Republic of Brazil) and the same land; the group's other part already wrote ONE dossier, brazilian-republic.json (validates, 0 errors, 0 warnings), listing all four Names and reviewing republic-of-brazil_1987 and republic-of-brazil_2024 as `ok`, with rename events for 1985 and 5 October 1988 and a note that these slugs should not get dossiers. A second dossier would review the same two shapes twice, so none was written. The two pages opened for this slug agree with that dossier: Brazil infobox 8,510,346 km2 (body 8,515,767 km2) against Cliopatria 8,530,587.4 km2 (ratio 1.00); 'Civilians returned to power in 1985 when' Sarney assumed the presidency; Constitution 'promulgated on 5 October 1988'; the 1988 constitution 'abolished the last three' territories (Amapa and Roraima gained statehood; Fernando de Noronha became a state district of Pernambuco), an internal change with no border effect; History of Brazil (1985-present): 'The Constituent Assembly began deliberations in February 1987' and the New Republic ran from Sarney's 1985 inauguration to Collor's 1990 (the page is silent on Tocantins and on any change of territory after 1985). Neither page says why Cliopatria's 'Republic of Brazil' label starts in 1987. Observation from the shape table, not from a page: the Cliopatria bbox ends at -34.84 lon, so Fernando de Noronha (about -32.4) is outside the shape; negligible (26 km2). The Bolivia and Peru entries in the shape's modern_countries are border-cell overlap.

## Cliopatria rows to correct elsewhere

- british-colonial-empire (eu-11): still touches Dominica and Saint Lucia 1979-1995 and Belize 1983-1995; release the three islands/colony in 1967 (as Associated States, vassal tint), 1978-79 and 1981 respectively.

## Needs a dossier from another group

- Colony of Dominica (British from 1763; suggested slug colony-of-dominica) and Colony of Saint Lucia (French crown colony 1674, British from 1814, one of the Windward Islands; suggested slug colony-of-saint-lucia): predecessors of the two states, Cliopatria lacks them (am-08-x or eu-11). Used as counterpart: british-colonial-empire.
- british-honduras exists (type colony); belize points to it as predecessor and found counterpart.

## Pages that failed

- https://en.wikipedia.org/wiki/Belize%E2%80%93Guatemala_territorial_dispute (url_not_found; retried with a literal en dash, a hyphen, and the titles Guatemala-Belize and Guatemalan-Belizean territorial dispute, all url_not_found). History of Belize was opened instead.

## Gazetteer names wanted

None: every region resolves ({"country": ...} only).
