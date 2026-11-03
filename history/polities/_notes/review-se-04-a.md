# Review se-04-a (Modern, part a), 2026-10-19

Reviewer: adversarial review of 8 dossiers (6 owned states, 2 added rebel states). Validator (`--resolve`) passed all eight; the only warnings were two wars dated 2025 (outside the 2024 life) and three `dutch-new-guinea` counterparts (listed by the author as needing a dossier). Neighbour dossiers read: burma, empire-of-japan, united-states-of-america, dutch-east-indies, sultanate-of-aceh, papua-new-guinea, rattanakosin-kingdom, union-of-burma. Not yet written (counted as "group not run yet"): french-indochina, british-raj, british-colonial-empire, republic-of-china, republic-of-vietnam, khmer-rouge, people-s-republic-of-kampuchea, communist-laos, socialist-republic-of-vietnam, east-timor, estado-novo, malaysia.

Rule used for verdicts: "fix" = fixed by the reviewer in place (small, verified on the page, re-validated); "fail" = at least one finding the author must make (shape correction or missing events); "thin" = honest within the page budget but the border moves are not drawn; "pass" = could not break it.

## Verdicts
| slug | verdict | why |
| --- | --- | --- |
| kingdom-of-thailand | fix | counterpart `burma` (Konbaung dossier, ends 1885) changed to `british-raj` on /ledger/5, /ledger/7, /wars/1; 2025 war removed (outside life) |
| republic-of-indonesia | fail | Aceh left unowned 1945-1949 (and cut 1953-1959); missing mirror of the DEI contest Oct 1945-Nov 1946 |
| negara-islam-indonesia | pass | all four spot checks confirmed on the Darul Islam page |
| republic-of-the-philippines | pass | found event confirmed (Treaty of Manila, 4 July 1946); no border change |
| democratic-republic-of-vietnam | fail | no mirror for the Laos dossier's PAVN occupations of Attapu (1970-75) and the Bolaven Plateau (1971-75); /ledger/10 lowered 3 to 2 by reviewer |
| kingdom-of-cambodia | fix | 2025 war removed (outside life) |
| kingdom-of-laos | fix | source added to ruler Sisavang Vatthana |
| pathet-lao | thin | only Phongsali and Houaphan drawn 1953-1975; the 1962-1975 extent is missing |

## Findings to act on (author)

### republic-of-indonesia (fail)
1. /keyframe_review/0, 1, 2, 3 and 5: Aceh is missing. The Aceh page: "The ulama won, and the area remained free during the Indonesian War of Independence"; "The Dutch military itself never attempted to invade Aceh". sultanate-of-aceh (se-02) marks Cliopatria's Aceh rows 1946, 1947, 1949, 1953 and 1958 `wrong` with the text "Belongs to the republic-of-indonesia dossier". Grid check: Aceh is 184 cells (about 46,500 km2); the Indonesia 1946 shape misses 129 of them (32,600 km2) and the 1949 shape all 184, so Aceh is drawn by nobody in 1945-1949. Fix: KF0, KF1, KF2 verdict `adjust`, correction `union[{cliopatria Republic of Indonesia, year 1946 / 1947}, {admin1 Aceh, country Indonesia}]`; KF3 add Aceh to its union; KF5 (1953) add Aceh back under the existing NII contest, as for West Java and South Sulawesi (the note itself says the government held the towns); widen /ledger/0 and /ledger/2 regions likewise.
2. Missing events: dutch-east-indies /ledger/97 (contest_start 1945-10, counterpart republic-of-indonesia: British and NICA landings) and /ledger/99 (contest_end 1946-11, Linggadjati) have no mirror here. The Revolution page: "The first British troops reached Jakarta in late September 1945"; "The Battle of Surabaya was the heaviest and bloodiest single battle of the revolution". Fix: add contest_start 1945-10 and contest_end 1946-11 against dutch-east-indies with the DEI's region, source Indonesian_National_Revolution.
3. Thin: /ledger/1 (capital to Yogyakarta, conf 1; the move was 4 January 1946); PRRI/Permesta 1958; Roem-Van Roijen and the Dutch withdrawal from Yogyakarta 1949; South Kalimantan Darul Islam (the Darul Islam page gives its surrender in 1959).

### democratic-republic-of-vietnam (fail)
1. Missing events: kingdom-of-laos /ledger/6 (1970-05 occupation_start of Attapu by the DRV, "PAVN units (28th and 24A regiments) joined with North Vietnamese Army and Pathet Lao to seize Attapeu"), /ledger/7 (1971 Bolaven Plateau), /ledger/11 and /ledger/12 (their occupation_end 1975-12) have no mirror here. Only 11 of Attapu's 29 cells and none of the Bolaven circle's 40 cells lie in the 1967 strip that /ledger/6 of this dossier occupies. Fix: add the two occupation_start and two occupation_end events with the same regions, source Laotian_Civil_War (already in sources).
2. Applied by reviewer: /ledger/10 (1975-04 gain of South Vietnam) confidence 3 to 2. The North Vietnam page: the PRG "alongside the North Vietnamese Army, governed South Vietnam for the next year"; the PRG page: it "formally replaced the Republic of Vietnam to become the nominal and representative government of South Vietnam". Once a PRG dossier exists, this becomes the PRG's gain plus a DRV vassal_start.
3. Thin: /ledger/0 (Chinese arrival 1945, conf 1), /ledger/6 (1967 strip, conf 1; the trail dates from 1959), /ledger/9 (1973 PRG/PAVN zones, conf 1).

### pathet-lao (thin)
- The single keyframe (Phongsali and Houaphan, 1953-1975) does not show the 1962-1975 extent (the Pathet Lao and PAVN held most of the east after 1962); the Laotian Civil War page does not say whether the two provinces passed to the royal administration after the November 1957 coalition (/ledger/2), but the keyframe runs through 1957-1959. Pages to try: Pathet_Lao, Plain_of_Jars, International Agreement on the Neutrality of Laos (1962), Vientiane Agreement 1973.
- Advisory: /ledger/7 gains the kingdom from kingdom-of-laos, whose /ledger/13 is a dissolve with counterpart communist-laos (same month).

## Applied by the reviewer (re-validated, no errors or warnings)
- kingdom-of-thailand /ledger/5 and /ledger/7: counterpart `burma` to `british-raj`. The burma dossier is the Konbaung kingdom (1820-1885); Cliopatria's British Raj shapes for 1940-1942 and 1945-1946 reach 101.18 E and hold Burma and the Shan States. /wars/1 belligerent changed likewise. /wars/2 (2025 clashes, outside the 1932..2024 life) removed and recorded in notes.
- kingdom-of-cambodia /wars/2 (2025 conflict, outside the 1953..2024 life) removed and recorded in notes.
- democratic-republic-of-vietnam /ledger/10 confidence 3 to 2 (above).
- kingdom-of-laos /identity/rulers/1: source https://en.wikipedia.org/wiki/Kingdom_of_Laos added (infobox "1959-1975 (last): Sisavang Vatthana").

## Advisory (not blocking)
- kingdom-of-laos /keyframe_review/1 is `ok` although 35 cells (8,852 km2) of modern Laos lie outside the 1956-1966 shape (16 cells, 4,046 km2, drawn by nobody; 19 inside Thailand's shape) and 9 cells (2,276 km2) of the shape lie in Thailand. Acknowledged in notes as a Cliopatria quirk; at the next revision make it `adjust` with correction `{"country": "Laos"}` and point KF0, KF2, KF3 at it.
- kingdom-of-cambodia /ledger/1: the page says "all five of Cambodia's northeastern provinces" by April 1970; the region names four.
- kingdom-of-thailand: the author's note that Cliopatria's French Indochina row keeps Sayaboury and Battambang through 1945 is borne out: the French Indochina 1940-to-1941 drop (106 cells) lies in northern Tonkin (105.5-107.9 E, 20.5-22.4 N), not in the ceded provinces. The 1941 province list still did not load (Franco-Thai War page).
- negara-islam-indonesia /ledger/0: West Java was Dutch-held (Renville) in August 1949; dutch-east-indies has no NII event. Counterpart republic-of-indonesia is acceptable since the Republic's contest mirrors it.
- republic-of-the-philippines /keyframe_review/0 quotes "The Commonwealth ended when the United States recognized Philippine independence on July 4, 1946"; WebFetch found only "the country's independence was recognized by the United States with the Treaty of Manila" on the Philippines page. Check the quote.
- For other groups: empire-of-japan (jk-01) uses `burma` for 1942 Burma (/ledger/63, /ledger/108) although that dossier ends in 1885 (should be british-raj); it has no 1943 hand-over of Kedah, Perlis, Kelantan, Terengganu (18 October 1943) or of Kengtung to Thailand. The khmer-rouge dossier (se-04) must start by 1970-72 to carry kingdom-of-cambodia's 1972 contest and 1975 gain.

## Spot checks (all on the pages cited)
Thailand: /ledger/4, 5, 6, 7, 9 confirmed (Franco-Thai War, Thailand in World War II, Japanese occupation of Malaya). Indonesia: /ledger/2, 6, 10, 16, 19, 23, 24 confirmed. NII: /ledger/0, 3, 5, 6 confirmed. Philippines: /ledger/0 confirmed. DRV: /ledger/2, 4, 13 confirmed; /ledger/10 confirmed in fact but the page gives the land to the PRG (confidence lowered). Cambodia: /ledger/1, 3, 5, 8 confirmed. Laos: /ledger/1, 4, 6, 13 confirmed. Pathet Lao: /ledger/0, 2, 4, 5 confirmed. No fabricated or mis-dated event found.

## Area checks
Thailand 513,120 vs 521,641 (1.02); Indonesia 1,904,569 vs 2,023,107 (1.06); Philippines 300,000 vs 343,637 (1.15); North Vietnam 157,880 (1955, 1968) vs 157,593 (1.00); Cambodia 181,035 vs 184,307 (1.02); Kingdom of Laos 236,800 vs 229,137 (0.97). All acknowledged in keyframe notes.
