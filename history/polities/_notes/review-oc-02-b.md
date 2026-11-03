# Review of batch oc-02-b (2026-10-18)

Reviewer: adversarial review of republic-of-fiji, solomon-islands, vanuatu, micronesia, palau. Machine copy: history/notes/phase-b/reviews/oc-02-b.json.

Mechanical: all five validate with 0 errors and 0 warnings under --resolve, before and after the reviewer's fixes. Keyframes: each dossier adds one gap keyframe from independence to the year before Cliopatria's row starts and marks both Cliopatria shapes adjust (corrected to the Natural Earth country or admin-1 units); gazetteer resolves confirmed the author's cell counts for Fiji (73 vs 83) and Micronesia (2 vs 5). Capitals fall inside the shapes' bboxes (Ngerulmud is 600 m east of the 2-cell Cliopatria bbox but inside the corrected country). Certainty covers each life. Family 'pacific' exists in colours.json.

Pages opened by the reviewer: Fiji, History of Fiji, Solomon Islands, History of the Solomon Islands, Vanuatu, Coconut War (twice), Federated States of Micronesia, Trust Territory of the Pacific Islands (twice), Palau, Ngerulmud, Palikir, Kolonia, Regional Assistance Mission to Solomon Islands. Failed: Ethnic_violence_in_Solomon_Islands (URL not found).

## republic-of-fiji: pass
- All four ledger events confirmed on the pages with their years and months: independence 10 Oct 1970 and the Union Jack lowered 9 Oct; republic declared 10 Oct 1987 (History of Fiji, 'the seventeenth anniversary'), infobox 6 Oct 1987; 1997 'Republic of the Fiji Islands'; 'reverted to Republic of Fiji in February 2011'.
- Area: infobox 18,274 km2 (no year) vs Cliopatria 21,696 (ratio 1.19). Rotuma '220 nautical miles' and the Lau Group confirmed.
- Optional for a gap-filler: Minerva Reefs / Conway Reef (no land at the grid).

## solomon-islands: fix (applied by the reviewer)
- Applied: removed 'British Solomon Islands Protectorate' from identity.alt_names; it is the 1893-1978 predecessor that the author's report routes to oc-02-x.
- Confirmed: independence 7 July 1978; Bougainville 'does not form part of the nation'; March and June 1893 both on the page; 1898-1899 additions and the 1899 Tripartite Convention; 'Malaitan enclave' and 'on 5 June 2000 the MEF seized the parliament by force' (History page); RAMSI July 2003 (Solomon Islands page) vs August (History page). The RAMSI article settles it: 'began arriving on 24 July 2003'.
- Area: 28,896 vs 37,719 (ratio 1.31).
- Thin by design (budget 1-2 pages): the 1998-2003 war has empty zones; try Isatabu_Freedom_Movement and Malaita_Eagle_Force for ground held. The dedicated tension article does not seem to exist.
- The Coconut War infobox lists Solomon Islands as a belligerent; optional war entry with empty zones.

## vanuatu: pass
- Confirmed: independence 30 July 1980; Coconut War 'Beginning in June 1980', 'State of Vemerana' (no date), surrender 28 August 1980, 'about 12 weeks', infobox 'Vanuatuan, Papua New Guinean and Solomon Islander victory'; Vanuatu page 'in January', 'Republic of Vemarana', surrender '1 September'. The contest_start at the birth month (confidence 2) is the right reading, since the uprising predates the state.
- Area: 12,189 (body 12,274) vs 16,885 (ratio 1.39). Matthew and Hunter 'claimed and controlled by France': no event needed.
- For oc-02-a: new-hebrides has no contest on Sanma for June-July 1980 ('On 8 June 1980, the New Hebrides government asked Britain and France to send troops', Coconut War page); papua-new-guinea lacks the Coconut War entry.
- Belligerents 'United Kingdom' and 'France' are names, allowed while no dossier exists; switch to slugs once the UK and french-fifth-republic dossiers exist.

## micronesia: fix (applied by the reviewer)
- Applied: capitals were Palikir 1986-2024. Palikir page: 'It was declared the capital of Micronesia in 1989'; Kolonia page: 'the former FSM capital before being replaced by Palikir in 1989'. Now Kolonia 1986-1988 (placed 8 km NE of Palikir from the Palikir page, since the Kolonia page has no coordinates) and Palikir 1989-2024; both pages added to sources; the notes sentence updated.
- Applied: the predecessor land text quoted 'The Mariana Islands and the other districts soon followed on November 3, 1986', not on the Trust Territory page; replaced by its sentence 'The termination of US administration of the Chuuk, Yap, Kosrae, Pohnpei, and the Mariana Islands districts of the TTPI soon followed on November 3, 1986.'
- Confirmed: 'became a sovereign state after attaining independence on November 3, 1986'; the Compact in force that day; trusteeship 'formalized on 2 April 1947' (FSM page) vs 18 July 1947 (TTPI page). The TTPI page dates the formal end of the trusteeship to 22 December 1990 (Resolution 683): am-07 should know.
- Area: 702 vs 459 (ratio 0.65); the Pohnpei-only shape is acknowledged and corrected.
- wikidata Q3359409 is kept per the schema (Cliopatria's id); the site should map the state's own id.

## palau: pass
- Confirmed: Compact 'entered into force on 1 October 1994, concluding Palau's transition from trusteeship to independence'; Republic 1 January 1981; UN admission 15 December 1994; sixteen states and the Southwest Islands 'some 604 kilometers'; Ngerulmud 'replaced Koror City as the capital in October 2006', opened 7 October 2006; 'The previous capital of Palau was located provisionally in Koror'. TTPI page: trusteeship ended 25 May 1994 (Resolution 956).
- Area: infobox 459 (body 466) vs 659 (ratio 1.43).

## Cross-checks
- vanuatu found 1980-07 <- new-hebrides dissolve 1980-07: matched.
- Fiji and Solomon Islands found <- british-colonial-empire (eu-11, not run); Micronesia and Palau found <- united-states-of-america (am-07, not run): exceptions; both rows still contain these islands after independence (author flagged).
- State of Vemerana: no dossier, under the one-year threshold, explained.
- Not this batch: the commonwealth-of-australia 1946-2023 Cliopatria shape reaches 4.99S and is a 25 km neighbour of the Solomons; it probably keeps part of PNG after 1975 (for the oc-02-a review).
