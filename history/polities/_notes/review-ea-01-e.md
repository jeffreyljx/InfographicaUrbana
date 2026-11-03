# Review of batch ea-01-e (zhongshan, minyue, dong-ou)

Reviewer, 2026-10-19 (brief filled 2026-10-18). Validator `--resolve`: 0 errors, 0 warnings on all three. Neighbour dossiers read (ledgers grepped for these slugs): wei, zhao, chu, qi, yan, qin, yue. Not yet written (owner group not run, ea-02): nanyue, han-dynasty, qin-dynasty, western-chu, jiujiang, linjiang, zhai. Pages opened: Zhongshan (state), King Wuling of Zhao, Minyue, History of Fujian, Qin dynasty, Emperor Wu of Han, Dong'ou (twice). None failed.

Verdicts: zhongshan **fix** (one minor finding left to the author); minyue **fail**; dong-ou **fail**. One fix applied by the reviewer (dong-ou ruler sources).

## zhongshan: fix
Spot checks (all confirmed): /ledger/0 found 381 ('in 381, Zhongshan won its independence back'; infobox 'Established: 414/381'); /ledger/3 loss 305 (Wuling page 'In the next year, parts of Zhongshan were annexed', after the 306 expedition); /ledger/5 loss 296 (Wuling 'In 296 BC, he annexed the state of Zhongshan'); /ledger/6 dissolve 296, conf 3 (infobox 'Conquered by Zhao: 296 BCE'). The 380 Lingshou capital is also on the page. Cliopatria verdicts (both wrong) and the core discs are argued and match wei and zhao. No infobox area; discs about 89 cells against Cliopatria's 62 (10,739 km2), acknowledged.

Finding (not applied, non-blocking):
- /wars/0 'Wei conquest of Zhongshan' runs -407..-381, before the life (start -381), and its 'to' is the independence year, not fighting (the page dates only 'in 407, Zhongshan was conquered by Wei troops'). Fix: drop wars[0] (the found note already quotes both sentences), or, if the start moves to 414, keep it as -407..-407.

Thin (within the 1-2 page budget): the 414-407 Duke Wu phase at Gu is not drawn (try https://en.wikipedia.org/wiki/Xianyu_(state) or https://zh.wikipedia.org/wiki/中山国); the 305 Dongyuan disc is the researcher's reading (try https://en.wikipedia.org/wiki/Zhao_(state)).

Cross-dossier: zhao /ledger/3 has a 366 loss (conf 1) of the 62 cells of Cliopatria's Zhongshan block to zhongshan; zhongshan marks that block wrong and never holds it. The zhao owner should drop or re-route that loss.

## minyue: fail
Spot checks: /ledger/1 occupation 214 confirmed (Qin page: 'In 214 BC', 'took the provinces of Fuzhou and Guilin'; Minyue not named, conf 2 right); /ledger/8 135 conf 3 confirmed for date (infobox 'Divided by the Han dynasty among the Minyue king and the Dongyue king: 135 BC'); /ledger/9 contest 111 conf 3 confirmed (History of Fujian 'Large forces approached Minyue simultaneously from four directions via land and sea in 111 BC'); /ledger/12 dissolve 110 conf 3 confirmed (infobox 'Defeated and annexed by the Han dynasty: 110 BC'). Also confirmed: 306 (infobox), 202 (Minyue text), 138 siege. No infobox area (population 400,000, 110 BC).

Findings:
1. BLOCKING. /keyframe_review/5..10 corrections, /identity/successors/0/land: the History of Fujian quote is cut. The page says 'His kingdom extended beyond the borders of contemporary Fujian into eastern Guangdong, eastern Jiangxi and southern Zhejiang.' The dossier quotes it without 'and southern Zhejiang', cuts Zhejiang, and keyframes 5 and 6 say 'No page opened ties Minyue to land outside Fujian, eastern Guangdong and eastern Jiangxi'. Cliopatria's 206 and 203 shapes hold 340 and 480 Zhejiang cells. Fix: quote the sentence in full; add southern Zhejiang to the corrections for Wuzhu's kingdom (from 206 or 202); from 192 carve out Wenzhou and Taizhou for Dong'ou with a ledger loss (or split) in 192, counterpart dong-ou, and say in dong-ou that its land came from Minyue; or argue from the page why 'southern Zhejiang' means Dong'ou's land only.
2. /ledger/8 (135, rename): the state did not change its name. The infobox and Emperor Wu page ('imposed a dual-monarchy system', 'Dongyue was ruled by Luo Yushan') describe a split. Fix: type split, counterpart dongyue, region what a gap-filler finds (the note can say the land is unnamed).
3. /ledger/3 (202, rename): not a name or dynasty change (the History of Fujian: 'he restored Minyue's status as a tributary independent kingdom'). Fix: drop it, or keep the caption in the minyue_-202 keyframe note; the han-dynasty dossier owes vassal_start 202 (counterpart minyue).
4. /ledger/10 and /ledger/11 notes put paraphrases of the Dong'ou page in quotation marks. The page: 'the aspiration for autonomous control over Dongyue gradually dissipated during the final months of 111 BC' and 'prompting the Han dynasty to eventually incorporate Dongyue and the remaining territories of the former Minyue'. Fix: quote it word for word.

Thin: /ledger/2, the end of Qin occupation in 206, is conf 1 (try https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention). Which land Dongyue held after 135 (try https://en.wikipedia.org/wiki/Baiyue). Fujian has no state in 333-307 (try https://en.wikipedia.org/wiki/Yue_(state)).

Cross-dossier: yue gives minyue as successor with land 'Cliopatria's Minyue row from 333' (Zhejiang included) from 333; minyue is founded in 306 on Fujian. The two dossiers disagree on both the land and the year.

## dong-ou: fail
Spot checks: /ledger/0 found 192 confirmed (lead 192, infobox 191); /ledger/2 contest_end 138 confirmed (Emperor Wu: the Kuaiji governor coerced 'to mobilize a large naval fleet to Dong'ou's rescue'); /ledger/3 loss 111 and /ledger/4 dissolve 111 are mis-dated: only the infobox gives 111.

Findings:
1. BLOCKING. /identity/end, /ledger/3, /ledger/4, /keyframe_review/0/to, /certainty/0/to, /identity/capitals/0/to: the text of the Dong'ou page dates the end to 138: 'During the Han campaigns against Minyue in 138 BC, the king of Dong'ou no longer wished to live in his realm after the incident, having submitted himself in an prostrating gesture ... to have him and his people's eventual fates to be absorbed into the Han empire.' Its 111 paragraph is about Dongyue and former Minyue ('the aspiration for autonomous control over Dongyue gradually dissipated during the final months of 111 BC ... both domains'). The Emperor Wu page: 'Following the successful manoeuvre against Minyue in 138 BC, Emperor Wu resettled the people of Dang'an into the region between the Yangtze and Huai Rivers.' The /ledger/3 note gives the Dongyue sentence, paraphrased, as Dong'ou's annexation. Fix: end Dong'ou in 138 (loss and dissolve 138, counterpart han-dynasty, conf 2, the infobox's 111 recorded as a disagreement; keyframe, certainty and capital to -138), or keep 111 only with a page that says Dong'ou held Wenzhou and Taizhou after 138. In either case, take the Dongyue sentence out of the /ledger/3 note.
2. APPLIED. /identity/rulers/1 and /2 had no source. The Dong'ou URL is added (infobox 'Zhenfu (貞復) 185-138', 'Wang (望) 138-138'). Re-validated: OK.
3. /identity/rulers/0: Yao starts in -191, but the life starts in -192 (infobox 191, text 192). Fix: say so in the note, or start the reign in -192.
4. If minyue's southern Zhejiang is restored, the 192 land comes from Minyue: the found note and predecessors should say so.

Thin: which state held Wenzhou and Taizhou after 138 (try https://en.wikipedia.org/wiki/Kuaiji_Commandery). Wikidata id is null (wikidata.org is unreachable from here).
