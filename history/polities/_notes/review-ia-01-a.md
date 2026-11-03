# Review: batch ia-01-a (Scythia, Yuezhi, Xiongnu, Zhizhi Xiongnu), 2026-10-18

Reviewer: adversarial reviewer, Phase B. Dossiers: xiongnu, zhizhi-xiongnu, yuezhi, scythia. Neighbour dossiers from the author's Context list that exist: greek-city-states, cimmerian-bosporus (eu-01); also odrysian-kingdom. None has an event with these states. Every other counterpart (han-dynasty, wusun, xianbei, southern-xiongnu, greco-bactrian-kingdom, kushan-empire, median-kingdom, neo-assyrian-empire, kingdom-of-urartu) belongs to a group that has not run yet.

Mechanical: validate_dossier.py --resolve: all four valid, 0 errors (warnings only for the sakas and sarmatians counterparts, which are listed for ia-01-x). Still 0 errors after the reviewer's edits. Geometry checked with tools/gazetteer.py (cell differences between keyframes, and overlaps across dossiers).

Pages opened: Xiongnu, Han-Xiongnu_War, Modu_Chanyu, Battle_of_Ikh_Bayan, Zhizhi_Chanyu, Yuezhi, Scythians, Sarmatians. All four infoboxes have no area figure, so no area ratio applies.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| xiongnu | fail | 13 spot checks all confirmed (no fabrication). Fails on keyframe/ledger consistency: see X1-X7. |
| zhizhi-xiongnu | fix | 4 spot checks confirmed; reviewer fixed the war start year. |
| yuezhi | thin | 6 spot checks confirmed; three border moves have no event (within the page budget). |
| scythia | fix | 7 spot checks confirmed; reviewer narrowed the Assyrian vassalage to West Asia, corrected the Urartu slug, a war year and three misquotes. |

## xiongnu (fail, back to the author)

- X1 /keyframe_review/11 (xiongnu_-66) is marked ok, but its own note explains the drop of the north by the 49 BCE loss to Zhizhi. Of the 1.11 M km2 that the -91 shape has and the -66 shape lacks, 0.33 M km2 lie in Khakassia+Tuva+Transbaikal, the region of /ledger/19 (-49). The keyframe and the ledger disagree for 66-49 BCE. Fix: mark it adjust with correction union(Xiongnu -66, Xiongnu -91 ∩ (Khakassia ∪ Tuva ∪ Transbaikal)) until -49, or date the loss to c. -66 with a page. A further 0.07 M km2 of the -49 region stays inside the -50 shape after the loss; if you narrow the region, use the same region in zhizhi-xiongnu /ledger/1, /ledger/4 and /keyframe_review/1.
- X2 /keyframe_review/5 (xiongnu_-170): the note says the westward extension is the Tarim plus Hexi. In fact, of its 0.89 M km2, 0.53 M lie outside the Tarim Basin, Turfan-Hami and Hexi (0.35 M in Dzungaria), and no gain event covers them. Fix: add a c. -178/-176 gain of the Dzungarian part (counterpart wusun or nobody; Modu page "In 178 BCE, the Xiongnu overran the Yuezhi and Wusun in Gansu and the Tarim Basin"), and correct the note.
- X3 /ledger/3 vs yuezhi /ledger/2: the same land (intersect(Yuezhi -203, Xinjiang) = 0.57 M km2, of which 0.55 M is Tarim Basin) is a Yuezhi loss to the Xiongnu in yuezhi.json, but an oasis-states vassalage in xiongnu.json, with no gain from the Yuezhi. Pick one reading and write it on both sides.
- X4 /keyframe_review/7 (xiongnu_-144) keeps the westward extension "as drawn" from -144, although the note says this is the Ili, taken only in 132. 0.17 M km2 of that extension lie in Semirechye, and no event covers 144-132. Fix: minus Semirechye for -144..-133. The land then enters as Wusun tributary land with /ledger/5.
- X5 /ledger/2: the -203 Ordos gain is "from qin-dynasty", but the Qin row ends at -209 (polities.csv). The Xiongnu page puts the recovery under Modu ("Modu also retook the original homeland of Xiongnu on the Yellow River ... which had previously been taken by the Qin general Meng Tian"). Fix: change the counterpart to nobody at 203 (c1), or date the gain c. -209/-207 and mark the -208/-206 keyframes adjust.
- X6 /identity/rulers/0: Touman (-220..-209) lies outside the life. Drop him or move him to the notes.
- X7 /ledger/33: the 119 capture of Yiwu adds land that /keyframe_review/22 and /23 already give the remnant from 91 (Hami 100 km lies wholly inside their Hami 200 km circle). Exclude the 100 km circle from the 91-118 correction.
- Thin (confidence 1, for a gap-filler): /ledger/2, /ledger/10 (the east beyond 114 E), /ledger/11, /ledger/21, /ledger/28 and /ledger/31, and the unexplained growth in /keyframe_review/10.
- End year: Battle of Ikh Bayan says the state ended in 93 ("ending the Xiongnu state"). The Xiongnu page records the Huyan King to 151. 151 is accepted; the author flagged the choice.

## zhizhi-xiongnu (fix, done by reviewer)

- /wars/1/from changed from -57 to -56 (the war started before the life; the page has Zhizhi's revolt in 56 BCE). Re-validated.
- Spot checks confirmed for 56, 49, 44 and 36 BCE on the Zhizhi Chanyu page. The extents are flagged as the researcher's readings. Tuva is not named on the page; see X1 for the region.

## yuezhi (thin)

- Confirmed: -178 (Modu), -176 (Xiongnu), c. 165 to the Ili and displacing the Sakas, "In 132 BC the Wusun, in alliance with the Xiongnu", 132-130 to north-west Bactria and Sogdia, "Circa 30 CE ... the Kushana, become dominant".
- The homeland correction (Hexi plus the Xinjiang part of the drawn shape) is supported by "between Dunhuang and Qilian", "the grasslands to the north of the Tian Shan" and "the Tarim Basin and possibly much of central Asia".
- Gaps: the founding year (c1, Cliopatria's); the -144 westward extension (+0.07 M km2) has no event; neither does the -110 southern extent to 33.9 N. Also X3, which needs the two dossiers to agree.

## scythia (fix, done by reviewer)

- /ledger/3 and /ledger/7: the page says "Thus Scythia in West Asia became a vassal and nominal extension of Assyria". The vassal tint over the whole Pontic steppe was over-broad, so the region is now the Sakez base only, with the quote corrected.
- /ledger/5 counterpart Urartu changed to kingdom-of-urartu (Cliopatria row -800..-551, group eu-19), also in /wars/0/belligerents. Urartu does not need a new dossier.
- /wars/0/from changed from -680 to -679 (inside the life).
- The quotes in /ledger/8, /ledger/11 and /keyframe_review/3 were paraphrases; they are replaced with the page's words. Years and regions are unchanged.
- Confirmed: 652 hegemony on Media, c. 635 Urartu, c. 590s/600 withdrawal, c. 550-500 Sauromatians in Ciscaucasia, c. 480 Istros border, 339/313 defeats then the Sarmatians crossing the Don. The infobox ruler list matches the dossier, gaps included.
- Thin: the Sakez date (/ledger/2, c1; /keyframe_review/0 draws Sakez from -679), the Kamianka move (/ledger/9, c1), and the end year (/ledger/16 and /ledger/17, c1). On the end year, the infobox gives "Sarmatian invasion of Scythia: c. 3rd century BC" and the lead "3rd to 2nd centuries BC", so 224 is inside the range.
- The median-kingdom counterpart at -652 comes before the Median row (-615). me-05 must start the Medes by -652 (the author flagged this).

## Cross-dossier matrix

This is the JSON report's cross_checks. Matched: xiongnu -176 / yuezhi -176 (Hexi); xiongnu -49 / zhizhi -49; xiongnu -56 contest / zhizhi -56 found. Mismatches: xiongnu -178 vassal vs yuezhi -178 loss (X3); xiongnu -203 vs qin-dynasty (X5). All other counterparts are exceptions: no row and listed, counterpart nobody, or a group that has not run yet.
