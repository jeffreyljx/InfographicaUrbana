# Review of batch eu-22-h (kosovo, republic-of-serbia), 2026-11-01

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Pages opened (WebFetch): Kosovo, Kosovo War, Serbia and Montenegro, Serbia. None failed.
Validator (--resolve --json): both dossiers valid, 0 errors, 0 warnings, all regions resolve.
Neighbour dossiers read (ledger rows from 1990 mentioning Kosovo or Serbia): former-yugoslav-republic-of-macedonia, montenegro, republic-of-albania, people-s-socialist-republic-of-albania, bosnia-and-herzegovina, hungary, republic-of-bulgaria, republic-of-croatia, romania, serbia-montenegro.

## kosovo: pass

What I tried and could not break:
- /ledger/0 found June 1999 (counterpart serbia-montenegro): Kosovo page infobox "UN Administration: 10 June 1999"; "On 10 June 1999, the UN Security Council passed" Resolution 1244. Confirmed. Mirror: serbia-montenegro /ledger/3 loss 1999-06, counterpart kosovo. Matched.
- /ledger/1 rename Feb 2008: "unilaterally declared its independence" 17 February 2008; Steering Group supervision ended 10 September 2012; ICJ opinion 22 July 2010; recognition 110 (infobox) and 118 as of 19 December 2025 (text). All confirmed.
- /keyframe_review/0 (new kosovo_1999, adjust, Cliopatria 2000 shape applied to 1999): consistent with the found event and with shapes.csv (serbia-montenegro_1996 runs 1996-1999 and includes Kosovo; serbia-montenegro_2000 is 11,130 km2 smaller).
- /wars/0 Kosovo War: infobox 28 February 1998 - 11 June 1999; Kumanovo Agreement 9 June 1999; NATO bombing from 24 March 1999; KLA "ran a territory based in the village of Glodjane" (April 1998) and "captured Orahovac" in mid-July 1998; territorial changes "No de jure changes to Yugoslav borders according to Resolution 1244". Confirmed.
- Keyframes: kosovo_2000 11,248.5 km2 -> kosovo_2006 11,296.4 (same bbox, +0.4 percent) -> kosovo_2024 identical. No border move to explain.
- Area: infobox 10,887 km2 (current) vs Cliopatria 11,296.4 (2024): ratio 1.04, acknowledged in keyframe notes.
- Capital Pristina 42.667N 21.167E (infobox 42°40'N 21°10'E), inside the kosovo bbox.
- Certainty 1999-2007 and 2008-2024: contiguous, covers the life.

Observations (not blocking):
- /wars/0 begins in 1998, before the dossier's start (June 1999). It is the war that produced the entity, the dossier's war note says so, and the contest pair lives in serbia-montenegro; I accept it.
- North Kosovo: the Kosovo page says North Kosovo "was in practice largely controlled by institutions of Serbia" before the 19 April 2013 Brussels Agreement. The author kept this in keyframe notes and drew no contest or occupation; defensible within a 1-2 page budget (Cliopatria draws one outline). Optional lead for a gap-filler: https://en.wikipedia.org/wiki/North_Kosovo and https://en.wikipedia.org/wiki/North_Kosovo_crisis_(2011%E2%80%932013).
- Border demarcation with Montenegro (agreement 2015, ratified by Kosovo 2018) and North Macedonia (2009) are not on the Kosovo page; small at map scale. Optional lead: https://en.wikipedia.org/wiki/Kosovo%E2%80%93Montenegro_border.

## republic-of-serbia: pass

What I tried and could not break:
- /ledger/0 found June 2006 (confidence 2): Serbia and Montenegro page "Montenegro's parliament formally declared independence on 3 June 2006"; "on 5 June 2006, Serbia's parliament did the same, effectively dissolving the union"; referendum 21 May 2006, 55.5 percent. Confirmed. Mirror: serbia-montenegro /ledger/6 dissolve 2006-06, counterpart republic-of-serbia. Matched. Confidence 2 is honest (the page names Serbia, not its limits).
- /keyframe_review/0 area: Serbia infobox total 88,499 km2, excluding Kosovo 77,589 km2; Cliopatria 76,541.2 (ratio 0.99). Acknowledged. shapes.csv: serbia-montenegro_2000 (90,685) less montenegro_2006 (13,931) = 76,754, matching the predecessor land spec.
- /certainty/0 quote: "Serbia opposed the move, considering it illegal and illegitimate, and continues to regard Kosovo as its province". Confirmed.
- Capital Belgrade 44.8N 20.467E (infobox 44°48'N 20°28'E), inside the bbox.
- Serbia page reports no change of Serbia's borders after 2006; no wars after 2006. The infobox formation list also has 7th century, 1217 and 1346 entries; the dossier quotes only the later ones, which is not a misstatement.

Observations (not blocking):
- Certainty note says the outer line is an international frontier "on every side except Kosovo". The Croatia-Serbia Danube border dispute (since 1991) is not on the Serbia page and not in the croatia dossier. Optional lead: https://en.wikipedia.org/wiki/Croatia%E2%80%93Serbia_border_dispute.
- Native names are conventional forms, flagged by the author as not read from the page; they are correct.

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| kosovo 1999-06 found, counterpart serbia-montenegro | serbia-montenegro 1999-06 loss, counterpart kosovo | matched |
| republic-of-serbia 2006-06 found, counterpart serbia-montenegro | serbia-montenegro 2006-06 dissolve, counterpart republic-of-serbia | matched |
| serbia-montenegro 1998-07 contest_start / 1999-06 contest_end, counterpart kosovo | none in kosovo (before its June 1999 start) | exception, explained in both dossiers |

Predecessors/successors agree: serbia-montenegro lists republic-of-serbia, montenegro and kosovo as successors; both dossiers name serbia-montenegro as predecessor.

## For the orchestrator
- End year: both dossiers end in 2024 (Cliopatria's last year), as do most living states in the project (194 dossiers), while the schema says "for a state alive today, the current year" and some eu-22 dossiers use 2026. Normalise project-wide; not a fault of this batch.
