# Review of batch eu-11-j (2026-10-25)

Adversarial review of six dossiers (England, Scotland and Ireland, part j). All six validate with 0 errors and 0 warnings, including `--resolve`. Spot checks: 4 to 11 events per dossier, opened with WebFetch. No fabricated or mis-dated confidence-3 event was found. The reviewer applied five small fixes in place and re-validated. Nothing below calls for a `fail`.

## Verdicts

| slug | verdict | in one line |
| --- | --- | --- |
| commonwealth-of-england | fix (fixed by reviewer) | The 1653 gain of Ireland is moved to May 1652 to meet the Confederation's dissolve. Dunkirk gets a month and a page. |
| irish-catholic-confederation | thin | The 1643-1649 extent is unexplained, within its 1-2 page budget. One note's page attribution is corrected. |
| kingdom-of-scotland | thin | The Cliopatria moves are all explained. The Second War of Independence, the Rough Wooing, the Bishops' Wars occupation and the 1650 fall of Edinburgh are missing. |
| earldom-of-desmond | thin | The 1352 keyframe is set to adjust for consistency. The 1345-1349 forfeiture, on a page the author opened, is not in the ledger. |
| earldom-of-ulster | thin | The Bruce campaign of 1315-1318 is not drawn. The start year (1181, 1205 or 1263) needs deciding. |
| isle-of-man | fix (fixed by reviewer) | The found counterpart and the predecessor are now kingdom-of-england, matching Scotland's ledger. |

## Fixes applied by the reviewer

1. **commonwealth-of-england /ledger/10** (was /ledger/11): the `gain` of Ireland (island) from irish-catholic-confederation moved from September 1653 to May 1652, and its confidence from 3 to 2.
   - Why: irish-catholic-confederation dissolves in May 1652 (Confederate Ireland infobox 'Cromwellian conquest: 1652'; 'By May 1652 it had defeated the Confederate-Royalist alliance'). Its land would otherwise have had no owner for 16 months.
   - Page: the Cromwellian conquest page has the guerrilla forces 'surrendered in 1652, under terms signed at Kilkenny that May'.
   - The `contest_end` of 27 September 1653 stays, confirmed on the page: 'declared the Irish rebellion subdued on 27 September 1653'.
2. **commonwealth-of-england /ledger/13** (Dunkirk): month 6 added; source changed to Battle_of_the_Dunes_(1658), and that page added to `sources`; confidence raised from 2 to 3.
   - Page: Dunkirk 'surrendered to French forces' on 24 June 1658, and 'Cardinal Mazarin ... handed the port over to the Commonwealth'.
   - The counterpart kingdom-of-france is kept, as the pages say. See the cross-checks for the missing mirror.
3. **irish-catholic-confederation /ledger/9**: the note credited the Cloughoughter surrender (27 April 1653) and the 27 September 1653 declaration to the Confederate Ireland page. That page has neither; the Cromwellian conquest page has both. The note now says so.
4. **isle-of-man /ledger/0 and /identity/predecessors/0**: the counterpart and the predecessor changed from kingdom-of-scotland to kingdom-of-england.
   - Page: 'until the English took it for the last time in 1346'.
   - kingdom-of-scotland already loses the island to England in 1333 (/ledger/17) and has only a `contest_end` in 1346 (/ledger/19).
5. **earldom-of-desmond /keyframe_review/2** (shape of 1352): verdict changed from ok to adjust, with the same four-county correction as every other keyframe.
   - With ok, the drawn shape went from the four counties (1329-1351) to the 12,998 km2 shape with Tipperary, Kilkenny and Wexford cells (1352-1384), then back to the four counties (1385). No event explained either change.
   - Page (Earl of Desmond): 'the entirety of County Limerick' and 'large swathes of County Cork, County Kerry and County Waterford'.

## Findings not applied (non-blocking)

- **Dunkirk mirror (commonwealth-of-england /ledger/13 against kingdom-of-france).**
  - The France dossier (eu-10) has no Dunkirk event in 1658. Its /ledger/108 has Spain recapture Dunkirk in 1652.
  - Battle of the Dunes page: Dunkirk lay 'in what was then the Spanish Netherlands'.
  - Either kingdom-of-france adds a June 1658 gain from kingdom-of-spain and a loss to commonwealth-of-england, or the orchestrator makes kingdom-of-spain the counterpart here. kingdom-of-spain has no dossier yet.
- **commonwealth-of-england /ledger/11** (`contest_end` of September 1653): the counterpart irish-catholic-confederation no longer exists after May 1652. The fighting of 1652-1653 is against the Irish guerrillas. `nobody` would be more exact. This is cosmetic.
- **Page disagreement not flagged by the author.** Irish Confederate Wars puts the fall of Waterford in 1651 ('Waterford ... surrendered in 1651'). Cromwellian conquest puts it in 1650. The dossiers use 1650.

## Thin: what a gap-filler should look for

- **commonwealth-of-england**
  - Edinburgh 'fell on 7 September' 1650 and 'The English secured their hold over southern Scotland'. This is on Third_English_Civil_War, a page the author opened, but neither ledger has the gain or loss of the Lothians in 1650. Add the gain here and the loss in kingdom-of-scotland.
  - Drogheda (September 1649), Wexford (October 1649) and Ulster 1649-1650 are missing. Pages to try: Siege_of_Drogheda, Sack_of_Wexford.
- **irish-catholic-confederation**
  - The corrected 1645 keyframe still drops most of Tipperary (61k to about 54k km2) with no event.
  - Not in the ledger: Inchiquin's Cork enclave (July 1644) and the 1647 defeats at Dungan's Hill (August), Cashel and Knocknanuss (November), all on Irish_Confederate_Wars.
  - The losses of Wexford and Drogheda in 1649 are missing.
- **kingdom-of-scotland** (all missing)
  - /ledger/0 `found` and /ledger/1 `vassal_start` of the Lordship of the Isles, both at confidence 1.
  - The Second War of Independence (1332-1357): Berwick lost in 1333 (Halidon Hill) and Balliol's 1334 cession of the southern counties. Page: Second_War_of_Scottish_Independence.
  - The recovery of Berwick in 1461. Page: Berwick-upon-Tweed.
  - The English garrisons of the Rough Wooing (1547-1550). Page: Rough_Wooing.
  - The Scottish occupation of Northumberland and Durham, August 1640 to 1641. Pages: Second_Bishops'_War, Treaty_of_Ripon.
  - The 1650 fall of Edinburgh and the Lothians.
  - Rulers.
- **earldom-of-desmond**
  - Maurice FitzGerald page (opened by the author): in 1345 Desmond 'was imprisoned and his lands forfeit', was released in 1348 and pardoned in 1349. The ledger has no loss or regain. The war 'Desmond's revolt of 1345' has empty zones although ground changed hands.
  - 1459-1583 has no events.
  - Cliopatria's changes of 1352, 1385, 1395 and 1422 are corrected away, not explained.
- **earldom-of-ulster**
  - The Bruce campaign in Ireland (1315-1318; Carrickfergus besieged in 1315) has empty zones. Page: Bruce_campaign_in_Ireland.
  - Start year: the page has de Courcy 'made earl palatine of Ulster' in 1181. The dossier starts at the 1263 de Burgh grant, and nothing draws 1181-1262. Page: Hugh_de_Lacy,_1st_Earl_of_Ulster.
- **isle-of-man**
  - The lords of 1333-1399 (Montagu/Montacute, then Scrope) and the reason Cliopatria starts in 1344. Page: William_Montagu,_2nd_Earl_of_Salisbury.

## Cross-dossier matrix (summary)

- **Matched within the batch** (Commonwealth gains against Confederation losses, and Commonwealth against Scotland):
  - Waterford 1650, Kilkenny March 1650, Limerick 1651 and Galway May 1652.
  - Perth, Stirling, Fife and Dundee in September 1651; Scotland in May 1652; Scotland back to its kingdom in 1660.
  - After fix 1, the Confederation's dissolve of May 1652 against the Commonwealth's gain of May 1652.
- **Exceptions** (counterpart has no dossier because its group has not run, or counterpart is `nobody`):
  - kingdom-of-england (eu-11, another part) for:
    - Scotland: the occupations of 1296-1297 and 1304-1314, the Isle of Man events of 1313-1346, and Berwick in 1318 and 1482.
    - The Commonwealth found and dissolve.
    - The Confederation found.
    - Desmond: found in 1329, Dunamark in 1331, dissolve in 1583.
    - Ulster found in 1263.
    - Isle of Man: found in 1346 and dissolve in 1399.
  - kingdom-of-alba (eu-11): the Scotland found of 1294.
  - Lordship of the Isles (eu-11-x): 1294 and 1493.
  - kalmar-union (eu-14, not written): the Northern Isles in 1472.
  - kingdom-of-great-britain (eu-11): 1707.
  - `nobody`: the Debatable Lands in 1552 and the Ulster dissolve in 1333.
- **Mismatch:** commonwealth-of-england gains Dunkirk in 1658 from kingdom-of-france, and the France dossier has no mirror.

## Area checks

| slug | infobox | Cliopatria | ratio | acknowledged |
| --- | --- | --- | --- | --- |
| kingdom-of-scotland | 78,778 km2 (1482-1707) | 88,868 (1475 shape) | 1.13 | yes |
| isle-of-man | 574 | 767 | 1.34 | yes |
| commonwealth-of-england | none (no area in the infobox) | | | author says so |
| irish-catholic-confederation | none | | | compared with 'two-thirds of Ireland' (about 56,000 against 61,366) |
| earldom-of-desmond | none (title article) | | | compared with the four counties |
| earldom-of-ulster | none (no infobox) | | | the page's Antrim and Down are about 6,800 km2 against the 2,333 km2 shape (0.34); acknowledged and adjusted |

## For the orchestrator

These are the author's flags; the reviewer agrees with them.

- Who owns Parliament's England and Wales in 1645-1648: Cliopatria puts it under the Commonwealth row, but the state was founded on 19 May 1649 (confirmed on the page).
- Scotland is doubled with the Kingdom of England in 1609-1706 unless the England dossier subtracts it.
- kingdom-of-alba and kingdom-of-scotland are one kingdom and should share a colour.
- The Kingdom of Scotland infobox ends the kingdom on 1 May 1707 (confirmed).
