# Review of batch sa-03-c (Phase B), 2026-10-19

Dossiers: `gurjara-pratihara-dynasty` (verdict **fail**), `kannauj-varman-dynasty` (verdict **thin**). Machine copy: `history/notes/phase-b/reviews/sa-03-c.json`.

Mechanical: both validate with `--resolve`, 0 errors, 0 warnings. Neighbour dossiers read: karkota-dynasty, kashmir, chalukya-dynasty (and harsha-s-empire for the predecessor). Not yet written: rashtrakuta-dynasty, sind-habbari-dynasty, chandela-kingdom, pala-empire, paramara-dynasty, tibetan-empire, chaulukya-dynasty.

Spot checks (WebFetch): every event opened says what its note claims, with the year. Pratihara: /ledger/13, 27, 30 (confidence 3), 18, 24, 16, 2, 8. Kannauj: /ledger/3, 7, 8 (confidence 3), 0, 1. No fabrication found. Area: neither the Pratihara, Yashovarman nor Ayudha page has an infobox area; the authors say so.

Reviewer edit applied: gurjara-pratihara-dynasty /wars/0/from 723 -> 730 (the war began before the state's 730 start; note extended). Re-validated.

## gurjara-pratihara-dynasty: fail (keyframe corrections contradict the ledger)

Shares below are the reviewer's gazetteer resolution of each corrected keyframe.

1. **Doab dropped in 860 with no event** (/keyframe_review/15, 17, 18, 19). Keyframes 825-850 hold 100% of the Doab (the 816 gain, confidence 3, gives the whole Doab); from 860 to 959 the corrections hold 31%, so about 94,000 km2 leaves at Bhoja's peak and nothing in the ledger explains it. Fix: union `{"region": "Doab"}` into the 860 and 926 corrections and mark 936 and 947 adjust with it, or shrink the 816 gain and the 825-850 corrections to Cliopatria's partial Doab.
2. **922 drops Malwa, Gwalior and Bundelkhand without an event** (/keyframe_review/16). Malwa 86% -> 8%, Gwalior 100% -> 0%, Bundelkhand 67% -> 0%, all back in 926; the 916-926 contest covers Kannauj and the Doab only, and the Indra III page names only Kannauj in the Doab. Fix: the 922 correction = the 860 land without Kannauj (plus Kutch, plus the Doab per item 1, contested by /ledger/18), or a page for the Malwa loss.
3. **788 keeps Dhruva's raid as a loss to 792** (/keyframe_review/7). Malwa, Gwalior and Bundelkhand are out 788-792 (655,000 -> 321,000 -> 541,000 km2), although the note says Dhruva only raided and left in 790; Bundelkhand is not in the contest zone and nothing regains it in 793. Fix: restore the three in the 788 correction and let the 786-790 contest draw the fighting, or ledger a loss and gain with a page.
4. **936 marked ok, but the ledger gives Gujarat, Saurashtra and Kutch away in 940** (/keyframe_review/18, /ledger/22). Align: date the loss 936 or mark 936 adjust (years only).
5. **947 marked ok, but Gwalior and Bundelkhand go to the Chandelas c. 950** (/keyframe_review/19, /ledger/24). Mark adjust or add a 950-959 keyframe.
6. **Bundelkhand is both vassal and direct land** (/ledger/15, 23, 24): vassal_start 836 while keyframes 840-947 draw 49-78% of Bundelkhand as Pratihara land, and two events end it in 950. Pick one. The Pratihara page also lists the Chandelas among the feudatories that broke away under Mahipala I (912-944); say so in /ledger/23.
7. **Bari outside the shape** (/identity/capitals/2): 80.55 E is east of the 980/1034 shapes (edge 80.04 E). Add a disk round Bari to the late keyframe(s).
8. Applied by the reviewer: /wars/0 from 723 -> 730.

Gaps for a gap-filler (confidence 1): /ledger/3-5 (750, 772, 783 gains, 'unrecorded'), 6, 10, 11 (Lata 806), 15, 17 (the 860 Saurashtra part is named as Rashtrakuta though the dossier's own keyframes make it Saindhava land), 19, 20-22, 25-26, 28; no ruler strip. Pages to try: Nagabhata I, Vatsaraja, Dantidurga, Govinda III, Paramara dynasty, Habbari dynasty, Chavda dynasty, Chahamanas of Shakambhari.

## kannauj-varman-dynasty: thin

Spot checks all confirmed. The extension to 816 (Ayudha rename in 770) is sourced and coherent with the Pratihara 816 gain, which it mirrors. Open items (not applied; non-blocking):

1. No vassal pair for Pratihara overlordship 785-791 although gurjara-pratihara-dynasty /ledger/6 and /ledger/9 name this state. The author follows the schema (vassal events belong to the suzerain); the reviewer brief asks for a mirror. Orchestrator to rule once.
2. Lalitaditya: this dossier has a 740-741 contest with `karkota-dynasty`; `kashmir` has vassal_start 736 / vassal_end 749 with this state, and karkota-dynasty has nothing. Agree on the slug (kashmir as things stand), the relation and the years (within one year).
3. The Kannauj keyframes from 725 hold about 24,500 km2 of the Himachal/Jammu hills that kashmir /ledger/4 gives to 'nobody' in 732. One side must change.
4. Predecessor: harsha-s-empire lists `arunasva-kannauj` as successor; this dossier lists harsha-s-empire with counterpart 'Arunasva'. Settle the slug.

Gaps: /ledger/4 (771: about 413,000 km2 dropped with no taker), /keyframe_review/1-5 (extent rests on the Gaudavaho; Ayudha extent a minimal reading), /ledger/2 and /ledger/5 (bridging years). Pages to try: Jayapida, Lalitaditya Muktapida, Dhruva Dharavarsha.
