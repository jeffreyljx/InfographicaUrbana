# Review of batch ea-02-d (reviewer, 2026-10-19)

One dossier: protectorate-of-the-western-regions (-60..439, colony, 12 Cliopatria shapes, 5 new keyframes, 19 events, 5 pages). Verdict: **fix** (fixed by the reviewer; the remaining items are thin by page budget and cross-dossier mismatches routed to other owners).

## Mechanical
Validator --resolve: 0 errors; 4 warnings, all the unknown place 'Loulan' (gazetteer request, not a fault). After the reviewer's edits: 0 errors. All 12 Cliopatria shapes (117..592) have verdicts; new keyframes carry from/to/correction; ledger sorted; found at -60, dissolve at 439; contest_start 73 / contest_end 89 paired and inside the Han-Xiongnu war entry 73-89 with a zone; family 'china' is a colours.json family.

## Spot checks (all confirmed, nothing fabricated)
- /ledger/0 -60 found: protectorate page 'officially established in 59 or 60 BCE', Zheng Ji, Wulei HQ.
- /ledger/1 -51 Wusun: 'During the peak of the protectorate's power in 51 BCE, the Wusun nation was brought under Han submission.'
- /ledger/6, /ledger/7 74 Khotan, Kashgar (conf 3): Ban Chao page 'The kingdoms of Khotan and Kashgar came under Chinese rule by 74 CE.'
- /ledger/11 91 capital Qiuci (conf 3): Ban Chao page 'stationed at Qiuci'.
- /ledger/12 94 Yanqi (conf 3): 'In 94 CE, Chao proceeded to again attack and defeat Yanqi'.
- /ledger/13 107-07 loss (conf 3): protectorate page 'On 29 July 107 ... Duan Xi was killed and the post was abandoned.'
- /ledger/14 123: 'restored from 123 to 124'. /ledger/15 176: Chief Official page 'last seen in 175'.
- /ledger/16, /ledger/17 335: Former Liang page 'in 335 his forces marched across the sands ... forcing several oasis states in the Western Regions like Kucha to submit'; protectorate page 'revived in 335 by Former Liang ... headquartered in Gaochang'.
- /ledger/8 89: Western Regions page 'a heavily contested region during the Han-Xiongnu War until 89 AD'. /ledger/18 439: 'until the end of the Sixteen Kingdoms period in 439 AD'.

## Area
No infobox and no area figure on the protectorate page (confirmed). The author acknowledges in keyframe 0 that the named Tarim Basin + Turfan-Hami (4045 cells, about 1.02 M km2; I re-resolved it) is 3.7x Cliopatria's 117 shape (944 cells, about 0.24 M km2). Acknowledged; no fault.

## Fixes applied by the reviewer
1. /ledger/10 (91, rest of the basin): confidence 1 -> 2. The Ban Chao page dates it: 'In 91 CE, Ban Chao finally succeeded in pacifying the Western Regions and was awarded the title of Protector General and stationed at Qiuci (Kucha).' Quote added to the note.
2. /identity/capitals/0 (Wulei): to 90 -> 22. Wulei lies outside the 73 and 74-90 keyframes (Loulan, Hotan, Kashgar radii), the state is not drawn 23-72, and no page gives a seat for 73-90 ('Chen Mu was killed by the rebellious troops of Yanqi and Qiuci', undated; the Ban Chao page names no base before 91). Note added.
3. /identity/rulers/1..14: added the source (protectorate page; Ban Chao page for Ban Chao); every name and year checked against the page's list ('Han Xuan 48-45 BCE' ... 'Li Chong 13-23 CE'; 'Ban Chao was succeeded by Ren Shang and Duan Xi'). The gaps in the list are the page's 'Unknown' holders.
4. /notes: overlords by era now name Xin for 9-23 (Han ended in 9; Dan Qin and Li Chong served under Wang Mang).

## Not applied, not blocking (for the author or a gap-filler)
- /keyframe_review/8 (306 shape kept for 335-386): it keeps the western Tarim to 73.1 E and 125 cells of Kyrgyzstan (Naryn/At-Bashy side, 39.5-42.2 N), the same extent the author rejected for 184 'with no page behind it'. The Former Liang page names only 'several oasis states ... like Kucha'. Either say why the western end is kept or trim it (minus the Kyrgyzstan cells).
- /keyframe_review/5 (117 shape for 123-175): the west edge is 78.2 E, so Kashgar and Yarkand are out after Ban Yong's restoration while they were in for 94-106; the note should say so (Kushan held Kashgar as a client 117-127 in kushan-empire, which this happens to match).

## Thin (within the 5-page budget; for a gap-filler)
- 376-439: no event. Former Qin's conquest of Former Liang (376), Lü Guang's Tarim expedition (383-385, Kucha), Later Liang (386-397), Western Liang at Gaochang (400-421) and Northern Liang (421-439/442). Pages: Lü Guang, Former Qin, Later Liang, Northern Liang, Western Liang.
- /keyframe_review/9 (387): west edge 73.1 E -> 77.5 E with no event ('unverified: page budget').
- /ledger/2 (23, Wusun tie ends, conf 1) and /ledger/15 (176 loss, conf 1).
- 74-90: Chen Mu's death and the 76 recall (Ban Chao page: 'Ban Chao was recalled to Luoyang, but then sent again ... four years later', undated) are not in the ledger; the han-dynasty dossier ends the tie in 77.
- 123-175 extent and seat (Ban Yong at Liuzhong): Ban Yong page.

## Cross-dossier matrix (summary; the JSON report has every row)
- Matched: xiongnu -60 vassal_end/contest_end (found -60); xiongnu 23 vassal_start 'Tarim oasis states' (loss 23); xiongnu 74 vassal_end (gains 74); xiongnu 91 vassal_end Hami-Turfan (gain 91); han-dynasty 74, 91, 107, 123 vassal events with this slug.
- Mismatch, han-dynasty (ea-02): Han models the protectorate as its vassal; this dossier has no vassal events with Han (colony convention). Years disagree: Han vassal_end 8 vs loss 23 here; Han vassal_end 77 (conf 1) vs the three oases kept to 90 here; Han vassal_end 125 (conf 1) vs loss 176 here. Han's /ledger/33 (-77 vassal_start of Loulan/Shanshan with counterpart protectorate-of-the-western-regions) names a protectorate that did not exist until -60.
- Missing mirror: kingdom-of-kucha (ia-01) has only found -150 and dissolve 648; this dossier gains Kucha in 91 and 335 and loses it in 107 and 439. Both are drawn over Kucha then.
- Missing mirror: wusun (ia-01) has no event for the -51 submission or the 23 end.
- Exceptions: Shanshan, Khotan, Shule, Yanqi, Jushi (no dossiers; listed by the author); 'Tarim city-states' (group); former-liang and northern-liang (ea-03, not run); xin-dynasty has no Tarim relation.
- Khotan: the author suggests slug kingdom-of-khotan for the Han-era kingdom, but that slug exists (851-1006). Its owner should extend it back or a new slug is needed.
- Kushan 117-127 Kashgar client: no overlap with the 117 shape (checked by cells).
