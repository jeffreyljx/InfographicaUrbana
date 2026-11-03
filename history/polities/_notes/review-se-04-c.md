# Review of batch se-04-c (2026-10-19 brief, reviewed 2026-10-20)

Reviewer: adversarial reviewer, Phase B. Dossiers: socialist-republic-of-vietnam, people-s-republic-of-kampuchea, east-timor. (union-of-myanmar was deliberately not written by the author: covered by union-of-burma.json, se-01-j; not reviewed here.)

Neighbour dossiers read: kingdom-of-thailand, united-states-of-america, kingdom-of-cambodia, republic-of-indonesia (Context rows with a file), plus democratic-republic-of-vietnam (predecessor) and portuguese-empire (Timor). Not yet written (groups not run): communist-laos, khmer-rouge, republic-of-vietnam (se-04-b), people-s-republic-of-china (ea-08-d), people-s-republic-of-bangladesh, republic-of-india (sa-06), estado-novo (eu-21-c).

Mechanical: `validate_dossier.py --resolve` 0 errors, 0 warnings on all three, before and after the reviewer's edits.

## Verdicts

| slug | verdict | reviewer-applied fixes | open non-blocking items |
| --- | --- | --- | --- |
| socialist-republic-of-vietnam | fix (fixed by reviewer) | /ledger/2 month 1 -> 12 and note; /ledger/7 quote corrected | predecessor republic-of-vietnam; 1999 loss region size |
| people-s-republic-of-kampuchea | fix (fixed by reviewer) | /wars/0/from 1978 -> 1979 | khmer-rouge counterpart life after 1978; Pailin vs kingdom 1993 |
| east-timor | fix (fixed by reviewer) | /identity/capitals split (Dili 1975 and 1999-2024) | estado-novo counterpart (README row) |

## socialist-republic-of-vietnam

Spot checks (pages opened by the reviewer): /ledger/3 (25 Dec 1978, 13 divisions, 150,000; Kratie 21 Dec) confirmed; /ledger/4 (7 Jan 1979 PAVN enters Phnom Penh, KR retreat to Thai border) confirmed; /ledger/6 (17 Feb 1979, ~200,000, Cao Bang/Lao Cai/Lang Son, 15-20 km, Mong Cai) confirmed; /ledger/9 (1999 border pact, "part of its land which was lost during the battle", Ai Nam Quan gate, no day or area) confirmed. Also confirmed: /ledger/0 (2 July 1976), /ledger/1 (Sept 1977 Dong Thap, Tay Ninh; 30 April 1977 An Giang/Chau Doc), /ledger/5 (8 Jan 1979, "ten-year Vietnamese occupation"), /ledger/8 (21-26 Sept 1989, 26,000).

Area: infobox 331,344.82 km2 vs shape 337,618 km2, ratio 1.02, acknowledged.

Findings:
1. /ledger/2 (applied). The contest_end of the 1977-78 border contest was dated January 1978, but the Cambodian-Vietnamese War page says "Small-scale fighting continued between the two countries throughout 1978" (KRA overrunning outposts in Ha Tien in January, the Ba Chuc massacre in April, Vietnamese bombing of KRA border positions in June; "KRA forces still held portions of Vietnamese territory"). Month moved to 12 (the border contest hands over to the invasion contest of /ledger/3) and the note rewritten with these quotes. Confidence 2, so a fix, not a fail.
2. /ledger/7 (applied). The note quoted "China declared that its punitive mission had been accomplished"; the page reads "China declared that the gate to Hanoi was open and that their punitive mission had been achieved". Quote corrected.
3. /identity/predecessors/1 (not applied, non-blocking). republic-of-vietnam is listed as a predecessor carrying "South Vietnam, the southern half of the merger", but the democratic-republic-of-vietnam dossier gains the South from republic-of-vietnam in April 1975 (/ledger/12) and dissolves into this state in July 1976; its successor note names the merger partner as the Republic of South Vietnam (PRG), not the Saigon government. The land would be counted as passing twice. Fix: drop the republic-of-vietnam predecessor (keep the sentence in the DRV predecessor's note) or re-point it to the PRG dossier once written (provisional-revolutionary-government-of-the-republic-of-south-vietnam).
4. /ledger/9 (not applied, non-blocking). The 1999 loss draws 3 frontier cells near Lang Son (about 850 km2 at this grid) for a transfer the author says is far below one cell. Fix: shrink to a single cell (a small circle on the Friendship Pass once the gazetteer has it) so the map does not show a visible chunk of Lang Son province passing to China.

Thin by design (budget 1-2 pages, 3 used): the 1980s Chinese-held border hills (Vi Xuyen / Laoshan, 1984), Vietnamese forces in Laos (1977 treaty to 1988), the 1985 Cambodian border treaty. Pages to try: Sino-Vietnamese conflicts (1979-1991); Laos-Vietnam relations.

## people-s-republic-of-kampuchea

Spot checks: /ledger/0 (KPRC government 8 Jan 1979; renaming "10 or 19 January 1979") confirmed; /ledger/3 (State of Cambodia: infobox 30 April 1989, body 29-30 April, lead "May 1989") confirmed; /ledger/4 (remaining 26,000 left 21-26 Sept 1989; "probably they did not leave until 1990") confirmed; /ledger/5 (KR attacked Pailin 17 Sept 1989, claimed it 24 Oct 1989) confirmed; /ledger/7 ("finally dissolved with the restoration of the Kingdom of Cambodia in September 1993") confirmed. /ledger/1 and /wars/0 zone quote ("from the refugee camps and from hidden military outposts along the Thai border") confirmed.

Area: infobox 181,035 km2 (1980) vs shape 184,307 km2, ratio 1.02, acknowledged.

Findings:
1. /wars/0/from (applied). The war started in 1978 in this dossier, before the state's life (start 1979-01); brief check 2 requires wars inside the life. Set to 1979.
2. /ledger/2 note (optional). The PRK page reads "controlled the major population centres and most of the countryside from 1979 to September 1989"; the quote stops at "population centres", which undersells the support for hatching the whole outline. Optional wording fix.
3. Counterpart khmer-rouge after 1978 (not a fault here; routed). /ledger/0, /ledger/1, /ledger/5, /ledger/6 name khmer-rouge as counterpart in 1979-1991, but Cliopatria's Khmer Rouge row ends in 1978. The se-04-b author of khmer-rouge must either keep that dossier alive to 1993 (Democratic Kampuchea / the CGDK rump on the Thai frontier) or these counterparts must be re-pointed to the CGDK dossier the author asked for.
4. Pailin (routed to kingdom-of-cambodia). This dossier loses Pailin to the Khmer Rouge in October 1989 and never regains it; kingdom-of-cambodia /ledger/10 gains "the whole of Cambodia" from this state in September 1993. The kingdom dossier should take the PRK outline minus Pailin in 1993 and gain Pailin from the Khmer Rouge later (when a page dates it). The PRK author flagged this; the kingdom dossier did not.

Thin: extent of the KR/CGDK zone 1979-1991 (confidence 2 strip), how long Pailin stayed with the KR. Pages to try: Coalition Government of Democratic Kampuchea; K5 Plan; Pailin.

## east-timor

Spot checks: /ledger/0 (Fretilin "declared an independent East Timor on 28 November 1975") confirmed; /ledger/1 (7 December 1975 invasion, Operasi Seroja "the largest military operation ever carried out by that nation") confirmed; /ledger/2-3 (17 July 1976 annexation as 27th province, on both pages) confirmed; /ledger/4 (INTERFET entered Dili 20 September, last Indonesian troops left by 31 October 1999; UNTAET end of October / 25 October 1999) confirmed; /ledger/5 (20 May 2002 recognised as independent; UN member 27 September 2002) confirmed. Batugade 8 October 1975 and Balibo/Maliana eight days later (keyframe 0 note) confirmed.

Area: lead 15,007 km2 (geography section 14,874) vs east-timor_2006 18,567 km2, ratio 1.24, acknowledged. The East Timor infobox values did not come through for the reviewer either.

Design: start 28 November 1975 with no land July 1976 to October 1999, coordinated with republic-of-indonesia (se-04-a), whose contest/gain/loss all mirror this ledger month for month. Accepted.

Findings:
1. /identity/capitals (applied). Dili was given 1975-2024 although the state holds no land from July 1976 to October 1999 (and Dili fell in December 1975), so the capital dot would sit in Indonesian territory for 23 years. Split into Dili 1975-1975 (occupation page) and Dili 1999-2024 (East Timor page), as kingdom-of-cambodia does for its 1975-1993 gap.
2. /identity/predecessors/0 and /ledger/0 counterpart estado-novo (not applied, non-blocking). data/README.md lists the "Estado Novo" row as wrong (the regime ended in 1974; eu-21-c is told to fix its end year and give Portugal a dossier to 2024). Portuguese Timor in 1974-75 was ruled by post-revolution Portugal, so once eu-21-c runs, the found counterpart and predecessor slug should be re-pointed to its Portugal dossier, and that dossier needs a 1975 loss of Timor to east-timor. The dossier did not flag the README note.
3. Observation only: keyframe east-timor_1975 ends in 1975 while the loss is dated 1976-07; this matches Indonesia's Cliopatria shape (East Timor from 1976) and is within year resolution.

Thin: Fretilin's interior zones 1975-78; the 2005 and 2012-13 land-boundary agreements. Pages to try: Indonesian invasion of East Timor; East Timor-Indonesia border.

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| SRV 1976-07 found (democratic-republic-of-vietnam) | DRV 1976-07 dissolve (SRV) | matched |
| SRV predecessor republic-of-vietnam (land 1976) | DRV 1975-04 gain from republic-of-vietnam | mismatch (land counted twice) |
| SRV 1977-09 / 1978-12 / 1978-12 / 1979-01 contests (khmer-rouge) | khmer-rouge not written (se-04-b) | exception |
| SRV 1979-01 occupation_start (PRK) | PRK 1979-01 occupation_start (SRV) | matched |
| SRV 1989-09 occupation_end (PRK) | PRK 1989-09 occupation_end (SRV) | matched |
| SRV 1979-02 / 1979-03 contest (people-s-republic-of-china) | not written (ea-08-d) | exception |
| SRV 1999 loss (people-s-republic-of-china) | not written (ea-08-d): needs a 1999 gain | exception |
| PRK 1979-01 found (khmer-rouge) | not written (se-04-b): needs 1979 loss to PRK | exception |
| PRK 1979-01..1991-10 contest (khmer-rouge) | not written (se-04-b); KR row ends 1978 | exception |
| PRK 1989-10 loss Pailin (khmer-rouge) | not written (se-04-b) | exception |
| PRK 1993-09 dissolve (kingdom-of-cambodia) | kingdom-of-cambodia 1993-09 gain (PRK) | matched in date; land mismatch (Pailin) |
| ET 1975-11 found (estado-novo) | not written (eu-21-c); Estado Novo row known wrong | exception |
| ET 1975-12 contest_start / 1976-07 contest_end (Indonesia) | republic-of-indonesia /ledger/28, /ledger/29 | matched |
| ET 1976-07 loss (Indonesia) | republic-of-indonesia /ledger/30 gain | matched |
| ET 1999-10 gain (Indonesia) | republic-of-indonesia /ledger/31 loss | matched |

kingdom-of-thailand and united-states-of-america carry no events with this batch's slugs, and this batch carries none with them.

## Gazetteer
Wanted: place "Friendship Pass (Ai Nam Quan / Huu Nghi Quan)", used in socialist-republic-of-vietnam /ledger/9.
