# Review of batch ea-08-a (2026-10-24)

Reviewer: adversarial review, Phase B. Dossier: later-jin-dynasty. Verdict: **fix** (all fixes applied by the reviewer; the dossier re-validates with 0 errors and the one known warning, the 1637 Joseon vassal_start that outlasts the dossier). Machine copy: history/notes/phase-b/reviews/ea-08-a.json.

## What was tried

- Validator with --resolve: valid; 85 regions resolve.
- Keyframes resolved on the grid against Cliopatria (1619 275 cells to 1640 12,270): each step is carried by a ledger gain (1618-1622 Liaodong, 1635 Inner Mongolia, 1636 Heilongjiang, 1640 Outer Manchuria, 1642 Liaoxi). The Korean strip removal of 1636-1639 agrees with the joseon dossier, which marks its own 1636 keyframe wrong for the same reason.
- Pages opened: Nurhaci, Later Jin (1616-1636), Qing invasion of Joseon, Hong Taiji. Confirmed: Fushun 1618, Tieling summer 1619, Liaoyang and Shenyang by May 1621, capitals (Hetu Ala 1616-1622, Tungking 1622-1625, Shenyang from April 1625), Ejei Khan's submission 1635, February 1627 Yalu crossing, the 1636-1637 dates and the tributary terms without cession, the 1640 Evenk conquest. No fabricated or mis-dated event found.
- Area: the Later Jin infobox has no area (confirmed); the author says so.

## Fixes applied by the reviewer

1. Liaoxi region (7 places: /keyframe_review/3, /6, /7 corrections; /ledger/21, /24, /25; /wars/7 zone). The gazetteer's Liaoxi is Liaoning minus the Liaodong polygon and so also holds 110 cells north and east of the Liao (Kaiyuan, Xifeng, Changtu). Subtracting it cut Jin land held since 1619 out of the 1626-1628 and 1636-1641 shapes, and the 1642 gain gave it from the Ming again. Each spec is now `{"intersect":[{"region":"Liaoxi"},{"polygon":[[118.5,38.5],[122.6,38.5],[122.6,42.55],[118.5,42.55]]}]}` (255 cells; Guangning, Jinzhou, Xingcheng, Suizhong in, Kaiyuan out). The gazetteer entry itself should be narrowed; donghu, duan-liaoxi, northern-wei, second-turkic-khaganate and xianbei also use it.
2. /ledger/25 confidence 1 to 2: the Later Jin page does give the result ("to resoundingly defeat Ming forces in a series of battles from 1640 to 1642 for the territories of Songshan and Jinzhou"). Same correction in /wars/7/outcome and the notes of keyframes 7 and 8.
3. /ledger/18 and /19 confidence 3 to 2: the zone (all of North Korea plus Gyeonggi) is the researcher's reading, as the note says.
4. /identity/rulers: Shunzhi Emperor 1643-1644 added from the Hong Taiji infobox ("Successor: Shunzhi Emperor").

## Thin (for a gap-filler; within the 5-page budget, not faults)

- /ledger/16 Heilongjiang 1636 (confidence 1): Hurha, Daur and Solon submissions before the Amur expeditions. Try Bombogor, Daur people.
- /ledger/7 Liaodong peninsula 1622 (confidence 1): try Battle of Shen-Liao; the Later Jin page's "entire eastern part of Liao[dong]" may date it to 1621.
- /ledger/11 end of the 1627 invasion (confidence 1): try Later Jin invasion of Joseon.
- /ledger/25: whether Ningyuan and the Shanhai corridor stayed Ming to 1644 (Wu Sangui); try Battle of Song-Jin, Battle of Shanhai Pass.
- /ledger/26: the 1644 dissolve is a Cliopatria row boundary; merge question for the orchestrator.
- /keyframe_review/6: the kept 1636 Cliopatria shape reaches 100.6 E (Ordos, part of Alxa) and holds 89 cells of Gansu and Ningxia, 336 of northern Hebei and 14 of Mongolia; no page opened supports the Ordos/Alxa or the Gansu/Ningxia cells in 1636, and the note is silent.
- Kaiyuan (occupied 1619 per the Nurhaci page, undated sentence) lies outside the corrected 1619-1625 shapes.
- The eastern Inner Mongolian submissions before 1635 (Khorchin 1624-1626, Kharachin 1628) are left out as associations.

## Cross-checks

- mongol-khanate: 1632 contest, 1635 contest_end, loss and dissolve all mirror this dossier.
- joseon: 1627 and 1636-1637 contests match (1627 start month differs: February here from the Hong Taiji page, January there from its own page). Missing: joseon has no vassal_start for the 1637 tributary tie; jk-02 should add it.
- ming-dynasty, li-zicheng (ea-07), qing-dynasty (ea-08-b): not written yet; the Ming needs losses in 1618 (Fushun), 1619 (Tieling), May 1621 (Liaoyang, Shenyang), 1622 (peninsula) and 1642 (Liaoxi west of the Liao).
- Yehe 1619: in the author's counterparts_needing_dossiers.
