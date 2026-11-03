# Review of batch af-08-n (Phase B, 2026-10-24)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (small verified fixes applied in place; 4 spot checks per dossier, weighted to confidence 3). Validator: all five dossiers valid, no errors, before and after the fixes. Machine copy: history/notes/phase-b/reviews/af-08-n.json.

| slug | verdict | fixes applied | thin items |
| --- | --- | --- | --- |
| republic-of-zimbabwe | fix | 1 | 0 |
| namibia | fix | 4 | 1 |
| state-of-eritrea | thin | 1 | 3 |
| south-sudan | thin | 0 | 3 |
| state-of-libya | thin | 1 | 3 |

## republic-of-zimbabwe: fix

Tried: independence date (both 11 and 18 April 1980 are on the Zimbabwe page, as the author says), area, capital renaming (gazetted 18 April 1982), Mugabe's 21 November 2017 resignation, capital inside the bbox, the handover from zimbabwe-rhodesia (dissolve 1979-12, found 1980-04, within a year). No border change exists to explain; the one-event ledger is right for a static state.

Area: infobox 390,757 km2 against Cliopatria 392,765 km2 (ratio 1.005), acknowledged in the keyframe note.

Fixes (applied by the reviewer unless marked otherwise):
- `/keyframe_review/0/note`: The note attributes the 18 April 1980 end of Zimbabwe Rhodesia to the Zimbabwe Rhodesia infobox, which has no such field. Evidence: Zimbabwe Rhodesia page: the infobox lists 'British-supervised transition: 11-12 December 1979' and 'Lancaster House Agreement: 21 December 1979'; '18 April 1980 ... became the independent Republic of Zimbabwe' is body text. Fix: Applied by the reviewer: '(infobox)' changed to '(body text)' and the 11-12 December 1979 date credited to the infobox.

Spot checks: /ledger/0 confirmed; /identity/predecessors/0/land/text confirmed; /identity/capitals/1 confirmed; /identity/rulers/0 confirmed.

## namibia: fix

Walvis Bay handled correctly on both sides (south-africa loses it 1994-03, namibia gains it 1994-03; namibia_1990 adjusted minus the enclave, new namibia_1994 keyframe). The 25 km disc (about 1,960 km2 with sea) stands for a 1,124 km2 enclave and misses the Penguin Islands, which lie far to the south: acceptable at this scale.

Area: infobox 825,615 km2 against Cliopatria 832,435 km2 (ratio 1.008), acknowledged in the keyframe note.

Fixes (applied by the reviewer unless marked otherwise):
- `/ledger/0/note`: The quotation 'On 21 March 1990, Sam Nujoma was sworn in as the first President, at a ceremony attended by Nelson Mandela' is not on the Namibia page; it merges two sentences. Evidence: Namibia page: 'The country officially became independent on 21 March 1990. Sam Nujoma was sworn in as the first President of Namibia at a ceremony attended by Nelson Mandela of South Africa.' Fix: Applied by the reviewer: the two sentences quoted as the page has them.
- `/identity/rulers/0/note`: Same merged quotation as /ledger/0. Evidence: As above. Fix: Applied by the reviewer: quoted as the page has it.
- `/identity/rulers/1..3/source`: Pohamba, Geingob and Mbumba cite no page. Evidence: Namibia page: 'President Hifikepunye Pohamba ... had served the maximum two terms'; 'On 4 February 2024, President Hage Geingob died'; 'he was immediately succeeded by vice-president Nangolo Mbumba'. Fix: Applied by the reviewer: source https://en.wikipedia.org/wiki/Namibia added to each.
- `/wars/0/to`: Second Congo War ends in 1998, the year of deployment only; the schema wants the last year of fighting or the treaty year. Evidence: Second Congo War page infobox: '2 August 1998 - 18 July 2003'; Namibia among the 'Pro-government' belligerents with deployments in 1999 and 2000-2001. Fix: Applied by the reviewer: to = 2003, note updated, Second Congo War added to sources[].

For a gap-filler:
- `/ledger`: Optional: Kasikili/Sedudu Island, claimed by Namibia and awarded to Botswana by the ICJ in 1999 (tiny; no Cliopatria shape moves). Page to try: https://en.wikipedia.org/wiki/Kasikili/Sedudu_Island

Spot checks: /ledger/0 confirmed (date; quotation corrected); /ledger/1 confirmed; /keyframe_review/0 confirmed; /wars/1 confirmed; /wars/0 mis-dated (end year; fixed).

## state-of-eritrea: thin

Every 1998-2000 event checked is on the war page with its date (6 May 1998, 22 February 1999, 16 March 1999, May 2000, 25 May 2000, 12 December 2000; infobox 'until the 2020 Tigray War'; 14 April 2002 ruling as the page has it). Matches the ethiopia and EPLF dossiers for 1991 and 1998-2020. Thin only for the missing mirror of the Eritrean occupation of Tigray and the Red Sea islands, both outside the 1-2 page budget.

Area: infobox 120,000 km2 against Cliopatria 126,704 km2 (ratio 1.056), acknowledged in the keyframe note.

Fixes (applied by the reviewer unless marked otherwise):
- `/wars/1/to`: Tigray War ends in 2021; the war ran to November 2022. Evidence: Tigray War page: 'lasted from 3 November 2020 to 3 November 2022'; cessation of hostilities signed 2 November 2022; 'Eritrea was not a party to the agreement'. Fix: Applied by the reviewer: to = 2022, note updated, Tigray War added to sources[].

For a gap-filler:
- `/ledger (after /ledger/10)`: Mirror of ethiopia /ledger/22 (occupation_start, counterpart state-of-eritrea, 2020-11, northern Tigray inside a border band) and ethiopia /ledger/33 (occupation_end 2024, confidence 1): Eritrea's ledger has no occupation of Ethiopian land. Add occupation_start 2020-11 counterpart ethiopia with the Ethiopia dossier's region, and its end. The author flagged it (notes item 4). Page to try: https://en.wikipedia.org/wiki/Tigray_War
- `/ledger`: Hanish Islands: Eritrean seizure of Greater Hanish from Yemen (December 1995) and the 1998 arbitration award; Doumeira clash with Djibouti (2008). Page silent within budget. Page to try: https://en.wikipedia.org/wiki/Hanish_Islands_conflict
- `/ledger/4`: When Ethiopian troops left Barentu and western Eritrea after May 2000 (the Temporary Security Zone 'within Eritrea' of 31 July 2000); the contest on the Western front is closed only at the December 2000 peace. Page to try: https://en.wikipedia.org/wiki/Temporary_Security_Zone

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/10 confirmed; /wars/1 mis-dated (end year; fixed).

## south-sudan: thin

Independence (9 July 2011, 98.83%), the Abyei seizure (May 2011, about 5,000 soldiers, 20 June deal, UN force from 27 June), Heglig (10 April claim, 20 April withdrawal order, 1931 line, 26/27 September agreements) all on the pages as quoted. The South Sudan page says March 2012 and 'withdrew on 20 March' for Heglig; the author noted the disagreement and followed the Heglig Crisis page, matching the Sudan dossier. Thin by design: the civil war's rebel land is not drawn.

Area: infobox 644,329 km2 against Cliopatria 616,190 km2 (ratio 0.956), acknowledged in the keyframe note.

For a gap-filler:
- `/wars/2`: Land held by the SPLM-IO in the 2013-2018 civil war (Malakal, Bentiu, Bor and parts of Upper Nile, Unity and Jonglei): no zone or contest event; needs the rebel dossier listed under counterparts_needing_dossiers. Page to try: https://en.wikipedia.org/wiki/South_Sudanese_Civil_War
- `/ledger`: Kafia Kingi (disputed with Sudan) and the Ilemi Triangle (disputed with Kenya): the page dates neither; certainty notes name them but no contest is drawn. Page to try: https://en.wikipedia.org/wiki/Ilemi_Triangle
- `/ledger`: Jau, the 14-Mile area and Kiir Adem border incidents (2011-2012). Page to try: https://en.wikipedia.org/wiki/Sudan%E2%80%93South_Sudan_relations

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.

## state-of-libya: thin

Dates check out (4 April 2019, 23 October 2020, GNC at the beginning of 2014, December 2017 name notice, March 2022 dual governments, the 32,000 km2 claim on Algeria). Handover from libyan-arab-republic (dissolve 2013, found 2014) consistent. Thin by design: the de facto partition, the state's main territorial story after 2014, is undrawn; the author says so and lists the counterpart dossiers needed.

Area: infobox 1,759,541 km2 against Cliopatria 1,614,019 km2 (ratio 0.917), acknowledged in the keyframe note.

Fixes (applied by the reviewer unless marked otherwise):
- `/ledger/1/note`: The note names the April 2019 advance 'Operation Flood of Dignity', which neither cited page says. Evidence: Second Libyan Civil War page: 'On 4 April 2019, Khalifa Haftar ... called on his military forces to advance' in 'the 2019-20 Western Libya campaign'; the Libyan National Army page does not mention 'Flood of Dignity' either. Fix: Applied by the reviewer: the operation name replaced by the page's campaign name.

For a gap-filler:
- `/ledger/0`: The found event is confidence 1: no page dates a break in 2014; the real break is the end of the Jamahiriya in October 2011 (libyan-arab-republic carries the rename then and dissolves in 2013 to match Cliopatria's row). Page to try: https://en.wikipedia.org/wiki/National_Transitional_Council
- `/keyframe_review/0`: The 2014-2020 division between the House of Representatives/LNA (east, then centre and south) and the GNC/GNA (Tripoli) is not drawn: dated captures of Benghazi (2014-2017), Derna (2018), the oil crescent (2016), Fezzan and Sabha (2019), Sirte (January 2020). Page to try: https://en.wikipedia.org/wiki/Second_Libyan_Civil_War
- `/ledger/2`: The Tripoli front collapsed when the GNA took Tarhuna in June 2020; the contest is closed only at the 23 October 2020 ceasefire. A month for the Tarhuna capture would let the contest end earlier. Page to try: https://en.wikipedia.org/wiki/Second_Libyan_Civil_War

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (date; operation name not on page, removed); /ledger/2 confirmed; /keyframe_review/0 confirmed.

## Cross-dossier matrix

- republic-of-zimbabwe 1980 found (counterpart zimbabwe-rhodesia) / zimbabwe-rhodesia 1979 dissolve: **matched**. zimbabwe-rhodesia dissolves 1979-12 to republic-of-zimbabwe, this state is founded 1980-04: within a year. The four months of British Southern Rhodesia (11-12 December 1979 to 18 April 1980) belong to no dossier; the Zimbabwe notes still say zimbabwe-rhodesia 'should end in 1980', which that dossier no longer needs.
- namibia 1990 found (counterpart south-africa) / south-africa 1990 loss: **matched**. south-africa /ledger/11 loss namibia 1990-03 minus Walvis Bay; /ledger/10 occupation_end namibia 1990-03.
- namibia 1994 gain (counterpart south-africa) / south-africa 1994 loss: **matched**. south-africa /ledger/12 loss namibia 1994-03, Walvis Bay 25 km, same region spec.
- state-of-eritrea 1991 found (counterpart eritrean-people-s-liberation-front) / eritrean-people-s-liberation-front 1991 dissolve: **matched**. EPLF /ledger/6 dissolve 1991-05 to state-of-eritrea.
- ethiopia 1991 loss (counterpart state-of-eritrea) / state-of-eritrea 1991 found: **mismatch**. Ethiopia loses Eritrea to state-of-eritrea, while the EPLF dossier gains it from ethiopia (1991-05) and hands it to state-of-eritrea. Route to af-01: ethiopia /ledger/14 counterpart should be eritrean-people-s-liberation-front, or the EPLF gain removed. Land agrees.
- state-of-eritrea 1998 contest_start (counterpart ethiopia) / ethiopia 1998 contest_start: **matched**. ethiopia /ledger/17 1998-05 border band; Eritrea uses the named places (Badme 50 km).
- state-of-eritrea 1999 occupation_start (counterpart ethiopia) / ethiopia 1999 occupation_start: **matched**. ethiopia /ledger/18 1999-02 Badme 60 km (Eritrea 50 km).
- state-of-eritrea 1999 contest_start (counterpart ethiopia) / ethiopia 1998 contest_start: **matched**. Tsorona front lies on the border, covered by Ethiopia's 1998-2000 border-band contest.
- state-of-eritrea 2000 contest_start (counterpart ethiopia) / ethiopia 1998 contest_start: **mismatch**. Barentu (Western front, May 2000) lies well inside Eritrea; Ethiopia's border band (width 2) probably does not reach it and Ethiopia has no event for its May 2000 offensive. Route to af-01 to check the band or add a contest/occupation on the Western front.
- state-of-eritrea 2000 contest_start (counterpart ethiopia) / ethiopia 1998 contest_start: **matched**. Zalambessa lies on the border, inside Ethiopia's border-band contest.
- state-of-eritrea 2000 contest_end (counterpart ethiopia) / ethiopia 2000 contest_end: **matched**. ethiopia /ledger/19 2000-12; Eritrea closes its four zones 2000-12.
- state-of-eritrea 2020 occupation_end (counterpart ethiopia) / ethiopia 2020 occupation_end: **matched**. ethiopia /ledger/20 2020.
- ethiopia 2020 occupation_start (counterpart state-of-eritrea) / state-of-eritrea - occupation_start: **missing**. ethiopia /ledger/22 (2020-11) and /ledger/33 (occupation_end 2024): Eritrean occupation of northern Tigray; state-of-eritrea has no mirror (author flagged; listed under thin for a gap-filler).
- south-sudan 2011 found (counterpart republic-of-sudan) / republic-of-sudan 2011 loss: **matched**. republic-of-sudan /ledger/16 loss south-sudan 2011-07; Sudan keyframe republic-of-sudan_2011 matches south-sudan_2011.
- south-sudan 2011 contest_start (counterpart republic-of-sudan) / republic-of-sudan 2011 contest_start: **matched**. Abyei: Sudan opens 2011-05, South Sudan 2011-07, same coordinates (28.43E 9.6N, 60 km); both open to 2024 by design.
- south-sudan 2012 contest_start (counterpart republic-of-sudan) / republic-of-sudan 2012 contest_start: **matched**. Heglig 2012-04, same coordinates.
- south-sudan 2012 contest_end (counterpart republic-of-sudan) / republic-of-sudan 2012 contest_end: **matched**. Heglig 2012-04.
- state-of-libya 2014 found (counterpart libyan-arab-republic) / libyan-arab-republic 2013 dissolve: **matched**. libyan-arab-republic dissolves 2013 (confidence 1) with successor state-of-libya; row boundary, not a break in the state.
- state-of-libya 2019 contest_start (counterpart libyan-national-army) / libyan-national-army - contest_start: **exception**. No dossier yet; listed in the author's counterparts_needing_dossiers (af-08-x).
- state-of-libya 2020 contest_end (counterpart libyan-national-army) / libyan-national-army - contest_end: **exception**. As above.

## Gazetteer names needed

Badme (state-of-eritrea), Tsorona (state-of-eritrea), Barentu (state-of-eritrea), Zalambessa (state-of-eritrea), Tarhuna (state-of-libya), Abyei (south-sudan), Heglig (south-sudan).

## Counterparts needing dossiers

- Libyan National Army (House of Representatives, Tobruk): `libyan-national-army`, 2014-2024
- General National Congress (Libya Dawn, Tripoli): `general-national-congress`, 2014-2016
- Government of National Accord: `government-of-national-accord`, 2016-2021
- Sudan People's Liberation Movement-in-Opposition: `sudan-people-s-liberation-movement-in-opposition`, 2013-2020

## Problems

- Reviewer applied small verified fixes in place (orchestrator's adjustment): republic-of-zimbabwe keyframe note attribution; namibia quotation, ruler sources and Second Congo War end year (+ source); state-of-eritrea Tigray War end year (+ source); state-of-libya unsupported operation name removed. All five re-validate with no errors.
- Pages opened beyond the authors' budget to verify fixes: Second_Congo_War, Tigray_War, Libyan_National_Army (re-read). No page failed to load for the reviewer.
- The GNC and GNA years given here (2014-2016, 2016-2021) are the rival-government span; the author's report gives 2012-2015 and 2015-2021 (GNC elected 2012, Skhirat agreement December 2015). The gap-filler should take the years from the pages.
- Two routing items for af-01 (ethiopia): /ledger/14 counterpart for the 1991 loss, and whether the 1998-2000 border band covers Barentu.
