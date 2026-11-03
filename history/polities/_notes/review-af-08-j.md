# Review of batch af-08-j (2026-10-24)

Adversarial review of the seven dossiers of af-08-j. Machine copy: history/notes/phase-b/reviews/af-08-j.json.

## Mechanical checks

`validate_dossier.py --resolve` on all seven: 0 errors. Warnings: three on republic-of-uganda, all the unknown region 'Kagera Salient' (gazetteer name needed). File names equal slugs; the Cliopatria Names match polities.csv and every shape has a verdict; the new keyframes (1962 Burundi, Rwanda, Uganda; 1966 Lesotho; 1964 People's Republic) carry from, to and a correction. Ledgers are in order, found/dissolve events sit at start/end, and every occupation and contest is paired.

## Verdicts

- **republic-of-burundi: thin.** Found (1 July 1962), rename (28 November 1966, 'deposing Ntare, abolishing the monarchy') and the Gitega capital (law of 4 February 2019, reference only, confidence 2) all check out on the Burundi page. Area 27,834 km2 against the shape's 24,740 km2 (0.89). Gap: the Second Congo War page says 'Burundi also retaliated, occupying a portion of northeastern Congo' with no date or extent. The author left it out and said why. A gap-filler should date it (probably South Kivu, Uvira-Fizi) and check Burundi's role in the First Congo War. No ruler strip.
- **republic-of-kenya: pass.** I tried the found and rename events (12 December 1963 and 12 December 1964, Kenya page), the coastal strip (agreement of 8 October 1963, 'simultaneously with independence for Kenya', Sultanate of Zanzibar page) and the Shifta War (state of emergency on 28 December 1963; the Arusha ceasefire on 23 October 1967 in the lead and 28 October in the body; Somalia appears only as a supporter, which the note says). I could not break them. Area 580,367 km2 against 585,506 km2 (1.01). Optional checks: whether the far-north strip is the Ilemi Triangle; Operation Linda Nchi (2011-12).
- **republic-of-rwanda: thin.** The found event, the Kivu occupation (the page has the RCD taking Bukavu and Uvira, and the note marks the zone as a reading at confidence 2), the Kisangani clashes (7 August [1999]; May and June 2000) and the end of the withdrawal (5 October [2002]) are all on the pages. Area 26,338 km2 against 25,419 km2 (0.97). Missing: the First Congo War (1996-97); the Rwandan Civil War zone, which is empty although the RPF held the north from 1990; and how far the Rwandan/RCD zone reached beyond the Kivus.
- **republic-of-uganda: thin.** These are confirmed: the republic of 9 October 1963 (infobox; the body contradicts it, and the note says so); the Kagera invasion (30 October [1978]) and the clearing of the salient ('By early January'); the crossing (21 January 1979); Kampala (10-11 April); the TPDF occupation; the Congo occupation ('invading and occupying'); the Luanda Agreement (6 September). Area 241,038 km2 against 210,012 km2 (0.87; 15 percent water). Gaps: /ledger/7, the end of the Tanzanian occupation, is at confidence 1 on the war's end date, but the TPDF stayed much longer. The text of the war page as fetched stops at 22 April 1979, so I could not settle it. Also missing: the completion of the Congo withdrawal (Ituri, 2003), the First Congo War, and the Ugandan Bush War with its NRA-held zones.
- **sultanate-of-zanzibar: pass.** The protectorate ended on 10 December 1963 (infobox), the coastal strip passed to Kenya with Kenyan independence, and the Sultan was overthrown on 12 January 1964 (Zanzibar Revolution page). The infobox gives no area. The author flags the 4,245 km2 shape as too big, and the correction draws only Unguja and Pemba. Reviewer's hint, not checked on a page: the bbox's south edge at 8.0 S matches Mafia Island.
- **lesotho: fix (applied by the reviewer).** The found event (4 October 1966), the start (deployment of 22 September 1998) and the end (May 1999, 'seven months of occupation') are confirmed. /ledger/2 was at confidence 3 with the region Maseru district, which neither page names as held. I lowered it to 2 and appended a sentence to the note. Area 30,355 km2 against 31,559 km2 (1.04). Thin item: Botswana also deployed troops ('Botswana Defence Force soldiers were also deployed', undated). A pair with republic-of-botswana is possible once a page dates it.
- **people-s-republic-of-zanzibar-and-pemba: fix (applied by the reviewer).** The found event (12 January 1964) and the merge and dissolve (April 1964; 23 April merger and 26 April announcement on the revolution page) are confirmed. Identity: the dossier said the state has no article of its own, but https://en.wikipedia.org/wiki/People%27s_Republic_of_Zanzibar exists ('a short-lived African state founded in 1964, consisting of the islands of the Zanzibar Archipelago'; infobox 'Merger with Tanganyika: 26 April', 'Capital: Zanzibar City'). I set identity.wikipedia, added 'Jamhuri ya Watu wa Zanzibar' to native_names, sourced the capital to that page (Zanzibar City (Stone Town)) and added the page to sources[]. Re-validated. Wikidata is left null: it is probably Q157535, which the older dossier people-s-republic-of-zanzibar now holds.

## Cross-dossier matrix (territorial events)

| event | mirror | status |
| --- | --- | --- |
| Burundi, Rwanda found 1962-07 from belgian-congo | belgian-congo losses 1962-07 | matched |
| Uganda found 1962-10, Kenya found 1963-12 from british-east-africa | british-east-africa losses 1962-10, 1963-12 | matched |
| Lesotho found 1966-10 from basutoland | basutoland dissolve 1966-10 | matched |
| british-east-africa loss to lesotho 1966-10 | Lesotho names basutoland | mismatch (between basutoland and british-east-africa, not lesotho) |
| Kenya gain coastal strip 1963-12 from sultanate-of-zanzibar | Sultanate loss 1963-12 | matched |
| Sultanate found 1963-12 from british-colonial-empire | no dossier yet | exception |
| Sultanate dissolve 1964-01 into the People's Republic | People's Republic found 1964-01 | matched |
| People's Republic merge into tanzania 1964-04 | tanzania not written | exception |
| Uganda occupies Kagera 1978-10 to 1979-01; Tanzania occupies Uganda 1979-04 to 06 | tanzania not written | exception |
| Rwanda occupies the Kivus 1998-08 to 2002-10; Uganda occupies Orientale and Equateur 1998-08 to 2002-09 | DR Congo has only a contest with 'RCD and MLC rebels with Rwanda and Uganda' 1998-08 to 2003-07 | mismatch: route to the DR Congo owner |
| Rwanda-Uganda contests at Kisangani 1999-08, 2000-05/06 | both sides | matched |
| Lesotho occupied by south-africa 1998-09 to 1999-05 | south-africa: none | missing: route to the south-africa owner |
| Kenya contest with Somalia 1963-12 to 1967-10 | federal-republic-of-somalia: none | missing (contest; informational) |

## Other problems

- The older dossier people-s-republic-of-zanzibar (the Sultanate to 1890) carries the Wikipedia title and Wikidata of the 1964 republic. Its owner should switch to the Sultanate of Zanzibar article.
- Rebels that held land and need dossiers: RCD-Goma and the MLC (listed by the author); the RPF 1990-94 and the NRA 1981-86 (added by the reviewer, still to be confirmed on a page).
- Gazetteer: Kagera Salient; Kenya Coastal Strip.
