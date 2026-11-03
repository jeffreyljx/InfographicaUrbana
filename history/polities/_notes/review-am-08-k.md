# Review of batch am-08-k (Caribbean and Guianas, 1966-2024), 2026-10-19

Reviewer: adversarial review, Phase B. Inputs: the six dossiers, the author's report (notes/phase-b/reports/am-08-k.json) and notes (_notes/am-08-k.md); neighbour dossiers read: venezuela, netherlands-antilles (context list), plus dutch-suriname and united-states-of-america (counterparts named or implied). republic-of-brazil, federated-republic-of-brazil, french-fifth-republic and british-colonial-empire are not written yet (groups not run): their pairs are exceptions.

Mechanical: validate_dossier.py --resolve: 0 errors, 0 warnings for all six, before and after the reviewer's fixes.

Pages opened (11): Guyana, Ankoko Island, New River Triangle, West Indies Associated States, Anguilla, Saint Kitts and Nevis, Saint Vincent and the Grenadines, The Bahamas, Grenada, United States invasion of Grenada, Suriname. All loaded. Every quoted date I checked is on its page; no fabricated or mis-dated event found.

## Verdicts

| slug | verdict | summary |
| --- | --- | --- |
| guyana | fix (applied by reviewer) | 1967-1969 contest counterpart was republic-of-suriname (born 1975); changed to dutch-suriname |
| saint-kitts | fix (author, non-blocking) | the 1980 'loss' of Anguilla repeats land already lost in May 1967 |
| saint-vincent | pass | |
| commonwealth-of-the-bahamas | pass | |
| grenada | fix (applied by reviewer) | occupation_end Dec 1983 raised from confidence 1 to 2: the Grenada page dates the withdrawal |
| republic-of-suriname | fix (applied by reviewer) | predecessor and found counterpart were netherlands-antilles; the dossier of Dutch Suriname is dutch-suriname |

## guyana

- Applied: /ledger/2 and /ledger/3 (contest_start Dec 1967, contest_end 1969, New River Triangle) and /wars/1 belligerents named `republic-of-suriname`, which starts on 25 Nov 1975. The New River Triangle page: in 1969 'Suriname was still a constituent state of the Kingdom of the Netherlands' and the posts were 'established by the Surinamese army'. The land of Suriname before 1975 is the dossier dutch-suriname (1667-1975). Counterpart changed to `dutch-suriname` in both events and the war; notes extended. dutch-suriname has no 1967-1969 contest or war: routed to its group (am-06) in the matrix.
- Spot checks (confirmed): /ledger/1 Ankoko Oct 1966 ('Venezuelan troops began their occupation of Ankoko Island in October 1966'); /ledger/2 12 Dec 1967 Oronoque; /ledger/3 1969 GDF 'seized full control', 19 Aug 1969 Camp Tigri; /ledger/0 and /ledger/4 26 May 1966 and 23 Feb 1970 (Guyana infobox).
- Area: infobox 214,969 km2 (undated) vs Cliopatria 212,448 km2: 0.99, acknowledged.
- Thin (within budget): /ledger/5 occupation_end 2024 at confidence 1 only closes an ongoing occupation (the Ankoko page: 'The island remains under Venezuelan administration'); Venezuela's dossier has no occupation_end (validator warning on venezuela /ledger/7), so the pair disagrees. The Rupununi uprising (Jan 1969) has no held ground on the pages read; a gap-filler could open the Rupununi uprising page to see whether Lethem was held.

## saint-kitts

- Not applied (non-blocking, for the author): /ledger/3 is a second `loss` of Anguilla (Dec 1980, counterpart british-colonial-empire) after /ledger/2 already lost it on 30 May 1967 to 'Anguilla'. The state did not hold Anguilla in 1980 (Anguilla page: 'British control restored: 18 March 1969'; 'Formal secession from Saint Kitts and Nevis: 16 December 1980'), so the event invites eu-11 to record a 1980 gain from saint-kitts when Britain took the island in March 1969 from the Anguillan secessionists. Fix: drop /ledger/3 and carry the 1980 formal separation in the /ledger/2 note and the certainty note (as now 'outside the state in fact from 1967, formally until 1980'); the 1969 British takeover belongs to the anguilla and british-colonial-empire dossiers.
- Identity: `wikipedia` 'Saint Kitts' and `wikidata` Q204989 are the island's, as the author says; the schema asks for Cliopatria's fields, so left as is. The site's link will open the island article.
- Spot checks (confirmed): /ledger/0 27 Feb 1967 (WIAS table 'Saint Christopher-Nevis-Anguilla | 27 February 1967 | 19 September 1983'); /ledger/2 30 May 1967 police ejected (Anguilla page); /ledger/3 16 Dec 1980 (Anguilla infobox; WIAS footnote 29 Oct 1980), /ledger/4 19 Sep 1983 (Saint Kitts and Nevis page).
- Area: infobox 261 km2 vs Cliopatria 501 km2 (polygon on Saint Croix): 1.92, acknowledged; both shapes 'wrong', correction the country. Correct.

## saint-vincent

- Pass. Tried: 27 Oct 1969 associate statehood and 27 Oct 1979 independence (both on the page and the WIAS table); Union Island rebellion Dec 1979 (page: 'the revolt was swiftly put down and Charles was arrested', nothing on held ground, zones [] said so); the Grenadines list (page names Young Island, Bequia, Mustique, Canouan, Union Island, Mayreau, Petit St Vincent, Palm Island). Area infobox 389 km2 vs 565 km2: 1.45, acknowledged. Capital inside the shape's box. Nothing broke.

## commonwealth-of-the-bahamas

- Pass. Tried: 10 Jul 1973 ('The Order came into force on 10 July 1973'), 7 Jan 1964 autonomy, 1718 crown colony, no boundary dispute on the page; area infobox 13,880 km2 vs 18,694 km2: 1.35, acknowledged. Nassau inside the box. One event is all the page supports.

## grenada

- Applied: /ledger/6 occupation_end Dec 1983 was confidence 1 on the invasion page ('page gives no withdrawal date'). The Grenada page says 'When US troops withdrew from Grenada in December 1983'. Source changed to the Grenada page, confidence 2 (the invasion page says some forces stayed on in Operation Island Breeze), note and notes field updated.
- Spot checks (confirmed): /ledger/0 3 Mar 1967; /ledger/2 7 Feb 1974; /ledger/4 13 Mar 1979 coup; /ledger/5 25 Oct 1983 ('invaded the island nation of Grenada at dawn on 25 October 1983', 'military occupation within a few days', Carriacou landing 1 Nov).
- Minor (no change asked): /wars/0 zones [] although the whole island was fought over; the occupation events carry it.
- Area: infobox 344 km2 vs 482 km2: 1.40, acknowledged.

## republic-of-suriname

- Applied: /identity/predecessors/0 and /ledger/0 named netherlands-antilles. The netherlands-antilles dossier (am-06) already subtracts Suriname from Cliopatria's 1877-2023 shape and has no 1975 event; the dossier dutch-suriname (1667-1975) dissolves on 25 Nov 1975 with republic-of-suriname as counterpart and successor. Predecessor slug and found counterpart changed to dutch-suriname; the predecessor land changed from the Netherlands Antilles shape (which also holds the six islands) to {"country": "Suriname"}; notes updated. The author's report problem 1 (am-06 must hand the land over) is obsolete.
- Spot checks (confirmed): /ledger/0 25 Nov 1975; /ledger/1 25 Feb 1980 coup; /wars/0 page text 'begun in 1986' with no end; certainty note (Marowijne and Corantijn disputed, PCA 20 Sep 2007).
- Thin (within budget): /wars/0 Interior War 1986 'to' 1986 and zones []: the war ran to the 1992 peace and the Jungle Commando held ground in the east; a gap-filler should open https://en.wikipedia.org/wiki/Surinamese_Interior_War. `native_names` 'Republiek Suriname' is not on the page (author flagged).
- Area: infobox 165,940 km2 (district table 163,820) vs 146,979 km2: 0.89, acknowledged.

## Cross-dossier matrix

- guyana 1966 occupation_start venezuela: matched (venezuela /ledger/7, Oct 1966).
- guyana 2024 occupation_end venezuela: missing in venezuela (no occupation_end; validator warning there). Route to am-08 (venezuela).
- guyana 1967/1969 contest with dutch-suriname: no mirror and no war in dutch-suriname. Route to am-06.
- republic-of-suriname 1975 found from dutch-suriname: matched (dutch-suriname /ledger/13 dissolve 1975-11) after the fix.
- grenada 1983 occupation_start/end united-states-of-america: missing; the USA dossier has no Grenada event or war. Route to the USA dossier's group.
- saint-kitts 1967 loss to Anguilla: exception (Anguilla in counterparts_needing_dossiers).
- saint-kitts 1980 loss to british-colonial-empire: exception (eu-11 not run) and see the fix above.
- vassal_start/vassal_end with british-colonial-empire (saint-kitts 1967/1983, saint-vincent 1969/1979, grenada 1967/1974) and the found events of all six from british-colonial-empire: exceptions (eu-11 not run). eu-11 must release Guyana 1966, the Bahamas 1973 and Grenada 1967/1974 from the BCE shapes (author's report).

## Gazetteer

Ankoko Island (place), New River Triangle / Tigri Area (region), Guayana Esequiba (region) as the author lists; admin-1 'East Berbice-Corentyne' resolving near Georgetown is a gazetteer problem worth a look.
