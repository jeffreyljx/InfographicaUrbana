# Review of batch eu-22-b (Europe 1945-2026, part b)

Reviewer, 2026-11-01. Machine copy: history/notes/phase-b/reviews/eu-22-b.json. All six dossiers validate (0 errors; Austria's 8 warnings were the two unknown regions Mühlviertel and East Tyrol). Eighteen events were opened on their pages (4 to 6 per dossier); every one says what the note claims, with the year. No fabricated or mis-dated event. The three fails are structural.

| slug | verdict | why |
| --- | --- | --- |
| second-republic-of-austria | fix (applied by reviewer) | Carinthia 1945 counterpart was the SFRY, which only exists from November 1945; set to `yugoslavia` |
| socialist-federal-republic-of-yugoslavia | fail | three events before the state's start (1945-11); anachronistic counterpart republic-of-italy for 1945 |
| hungary | fail | renames across 1949-1989 while hungarian-people-s-republic holds the same land: two states on one land |
| kingdom-of-bulgaria | fail | a second dossier for the Tsardom that principality-of-bulgaria already carries |
| people-s-republic-of-bulgaria | pass | (takes over the 'Kingdom of Bulgaria' row if kingdom-of-bulgaria is withdrawn) |
| socialist-republic-of-romania | pass | |

## second-republic-of-austria: fix (applied)
- /ledger/0, /ledger/1, /wars/0/belligerents: counterpart `socialist-federal-republic-of-yugoslavia` changed to `yugoslavia`. Carinthia page: Yugoslav troops took Klagenfurt after 'the Allied forces did not reach Carinthia before May 8, 1945' and were 'soon forced to withdraw by the British forces'; SFRY page: the Federal People's Republic was proclaimed on 29 November 1945. The author's own SFRY note says the troops were the Yugoslav Army before the federal republic; yugoslav-partisans hands its land to `yugoslavia` in 1945-03. Re-validated, 0 errors.
- Checked and holding: found 27 April 1945; zones 9 July 1945 (provinces as the page lists them; Vienna drawn in the Soviet hatch, said in the note); end of occupation 25 October 1955; area 85,349 km2 (1947 shape) against 83,879 km2 infobox; the 1946 shape (59,811 km2) correctly marked adjust.
- Thin (not blocking): the Carinthia events have no month, so /ledger/0 sorts before the 1945-04 found although it happened after 8 May.
- For other groups: united-kingdom and union-of-soviet-socialist-republics have no Austrian zone events (USA and French Fourth Republic match); nazi-germany names `republic-of-austria` as successor, not `second-republic-of-austria`.

## socialist-federal-republic-of-yugoslavia: fail
1. /ledger/0, /ledger/1 (Carinthia, May 1945) precede the start 1945-11. Delete them here; they belong to the yugoslavia dossier (eu-21, not written). Austria now names `yugoslavia`. Alternative: move the start to March 1945 and treat Democratic Federal Yugoslavia as this state (rename at 1945-11); then say so, and the orchestrator restores Austria's counterpart and changes yugoslav-partisans' successor.
2. /ledger/2 occupation_start 1945-06 (Morgan Line, confirmed on the Free Territory of Trieste page) also precedes the start and names republic-of-italy, which was founded in 1946-06. Open the occupation at 1945-11 (inherited; say so) with counterpart kingdom-of-italy, close it at 1946-06, reopen with republic-of-italy to 1947-09. Neither Italian dossier has a mirror.
3. /wars/1: Croatian War of Independence `to` 1995 lies outside the life (end 1991). Set 1991, keep 1995 in outcome.
4. /identity/successors: add republika-srpska (found 1992-01 from the SFRY) and croatian-republic-of-herzeg-bosnia (found 1991-11 from the SFRY), or explain.
- Holding: 1947 gain (Istria, Fiume, Zara, Gorizia, Pola; in force 15 September 1947), Zone B 1954-10 (London Memorandum 5 October 1954), rename 1963, Vukovar August 1991, Badinter 'in the process of dissolution'. The 1991 end matches Cliopatria and the successors' 1992 founds fall within a year. Area 250,252 km2 against 255,804 km2.
- Thin: /ledger/13 contest_end at confidence 1 (try Badinter Arbitration Committee, Sarajevo Agreement); Ten-Day War day dates.

## hungary: fail
- One structural finding. The dossier lives 1946-2024 and calls 1949 and 1989 renames, but hungarian-people-s-republic (eu-22) is a separate dossier for 1949-08 to 1989-10 with hungary as predecessor and successor. A rename means 'colour and dossier continue' (schema), and the capital (Budapest 1946-2024) and certainty (sharp 1947-2024) assert the state through those years: two states on one land for forty years. The HPR page gives predecessor 'Second Hungarian Republic' and successor 'Third Hungarian Republic', and the batch elsewhere writes one dossier per regime (PRB / Republic of Bulgaria, SRR / Romania).
- Fix: split the Cliopatria row 'Hungary': a new dossier `second-hungarian-republic` (1946-02 to 1949-08, found from hungarian-republic, the 1947 village loss, dissolve to hungarian-people-s-republic, reviews hungary_1947) and this dossier as the Third Republic from 1989-10 (found from hungarian-people-s-republic, reviews hungary_1990 onward); HPR's predecessor changes. Or, if the orchestrator rules the People's Republic a rename, merge the HPR row here and withdraw that dossier. Either needs the other eu-22 part.
- Holding: 1 February 1946; the three villages to Czechoslovakia (Paris treaty, in force 15 September 1947); 20 August 1949; 23 October 1989. Area 91,985 km2 against 93,011 km2 (1947). czechoslovakia (eu-21) still lacks the matching 1947 gain.

## kingdom-of-bulgaria: fail
- principality-of-bulgaria already carries the Tsardom: alt_names 'Kingdom of Bulgaria', 'Tsardom of Bulgaria'; /ledger/5 rename 1908-10, /ledger/31 the same 1940 Southern Dobruja gain, /ledger/40 dissolve 1946-09 to people-s-republic-of-bulgaria. This dossier repeats all three and draws nothing (its one shape is marked wrong). The schema has no alias type: the state gets two pages and two copies of the 1940 gain against one Romanian loss.
- Fix: withdraw kingdom-of-bulgaria.json. In people-s-republic-of-bulgaria, add 'Kingdom of Bulgaria' to cliopatria_names, turn the new keyframe people-s-republic-of-bulgaria_1946 into the review of shape kingdom-of-bulgaria_1947 (adjust, 1946-1947, same correction), and drop kingdom-of-bulgaria from predecessors. The colour agent drops the slug. If the orchestrator wants a file for every Cliopatria slug, it must define an alias form.
- Holding: 5 October 1908, 7 September 1940 (Craiova), 15 September 1946; area note (122,134 km2 for 1915 against the 1947 shape's 110,018 km2) acknowledged.

## people-s-republic-of-bulgaria: pass
- 15 September 1946, 15 November 1990, 'the same borders as present-day Bulgaria', Paris treaty 'borders of 1 January 1941' all on the pages; the Pirin Macedonia sentence is on the page and rightly not applied. Area 109,564 km2 against 110,994 km2. Founds and dissolves mirror principality-of-bulgaria/40 and republic-of-bulgaria/0. Only change pending: the kingdom-of-bulgaria withdrawal above.

## socialist-republic-of-romania: pass
- 30 December 1947, 21 August 1965, 28 December 1989 on the page; the page has no area (checked). One outline throughout, identical to the Kingdom's 1947 and Romania's 1990 shapes; romania/0 mirrors the end. kingdom-of-romania (eu-21) is still unwritten.
