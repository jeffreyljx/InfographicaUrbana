# Review: batch sa-06-a (Portuguese Ceylon)

Reviewer, 2026-10-25. One dossier: history/polities/portuguese-ceylon.json. portuguese-colonies has no dossier by design (merged into portuguese-empire, am-06) and is not reviewed here. No edits were made to the dossier.

## Verdict: portuguese-ceylon: thin

Validator (--resolve): 0 errors; 3 warnings, the empty corrections of the post-1658 shapes (expected). Years in order; found 1505, dissolve 1658-06; capitals and rulers inside the life.

What I tried and could not break:
- The main claim, that all eleven Cliopatria shapes are wrong. Gazetteer: the 1600 shape (186 cells) holds 7 cells of a 25 km Kandy disc and none of Colombo; the 1640 shape holds neither Galle nor the Jaffna region. The verdicts are right.
- Ten spot checks across the five pages the author opened (I opened them again). All confirmed: 1560 Mannar Island, 1582 tribute and 1619 conquest (Jaffna_kingdom); 1505 arrival and 27 May 1597 cession (Kingdom_of_Kotte); 1611 capture of Kandy (Kingdom_of_Kandy); 1639 Batticaloa, 1640 Galle, 1656 Colombo (Dutch–Portuguese_War); June 1658 Jaffna (Portuguese_Ceylon infobox). Nothing was fabricated or mis-dated, and confidence is honest.
- Area: the page has no area. Cliopatria's 1600 shape is 54,463 km2. The correction is 28 cells (about 7,081 km2) and the author calls it a minimum.

Fixes (non-blocking, not applied):
1. /keyframe_review/0-1, /ledger/0, capital: for 1505-1564 a 25 km Colombo disc (4 cells, 79.88-80.03E 6.76-7.08N) is drawn as Portuguese territory. It takes in the Kotte capitals (Kotte, Kelaniya) and overlaps Kotte's shape for 60 years. The page gives only an arrival and a trade agreement, and the author's own note says no land was taken. Fix: draw 1 cell ({"place":"Colombo","km":15}) as a trading post, or date the Colombo fort from a page; keep the disc from 1565.
2. /identity/predecessors/0: ceylon hands over "the island's Sinhalese kingdoms". The infobox's predecessors are Kotte, Jaffna and Sitawaka, and kingdom-of-kotte is founded in 1507 from ceylon. Fix: drop ceylon, and ceylon's owner names kingdom-of-kotte as the successor.
3. /ledger/11: the 1639 loss is to dutch-ceylon, but dutch-ceylon (sa-06-b) starts 1640-03. Fix: dutch-ceylon starts 1639, or the counterpart becomes dutch-republic (eu-09).
4. /ledger/12: dutch-ceylon founds itself on Galle and Negombo (February 1640), while this dossier loses Galle only and keeps Negombo (Gampaha) to 1658, an overlap. Fix: reconcile.
5. /ledger/13: contest_start 1654-03 is a sea battle. Minor: move it to the start of the land siege once a page dates it.

Thin (for a gap-filler; the 5-page budget was spent):
- The extent 1597-1658. Kotte page: "after the downfall of Sitawaka in 1594, these areas were re-annexed to the Kotte kingdom", so the 1597 cession included the lowlands. dutch-ceylon takes Matara and the Kalutara coast in 1658, and this dossier never draws them. Try Sinhalese–Portuguese_War.
- /ledger/4: the 1597 gain of Galle, Batticaloa and Trincomalee from nobody is a confidence-1 bridge and doubtful. Try Fort_Frederick_(Sri_Lanka), Batticaloa and Galle fort pages.
- /ledger/8: the 1612 end of the occupation of Kandy is a bridge. Try Senarat_of_Kandy.
- Randeniwela (2 August 1630) and the 1639-1640 inland losses to Kandy are not placed. Try Battle_of_Randeniwela.
- Missing although on a page opened: the 1592 brief occupation of Kandy and the Danture campaign. Try Campaign_of_Danture.
- kingdom-of-sitawaka has a 1574 loss to portuguese-ceylon (the Wattala garrisons) with no gain here.
- /ledger/17: Mannar and the lowland forts 1656-1658 are undated. Try Dutch_Ceylon.

## Cross-dossier matrix
| event | mirror | status |
| --- | --- | --- |
| 1560 gain jaffna-kingdom | jaffna-kingdom 1560 loss | matched |
| 1565 vassal_start kingdom-of-kotte | none | missing (sa-04) |
| 1582 vassal_start jaffna-kingdom | none | missing (sa-04) |
| 1597 gain nobody (c1) | - | exception (doubtful) |
| 1597-05 gain / vassal_end kingdom-of-kotte | kotte 1597-05 dissolve | matched |
| 1611/1612 occupation kingdom-of-kandy | kandy 1611/1612 | matched |
| 1619 gain jaffna-kingdom | jaffna 1619 dissolve | matched |
| 1639 loss dutch-ceylon | none (dutch-ceylon starts 1640-03) | mismatch |
| 1640 loss dutch-ceylon (Galle) | dutch-ceylon 1640-03 found (Galle + Negombo) | mismatch (land) |
| 1656 loss dutch-ceylon | dutch-ceylon 1656 gain | matched |
| 1658-06 loss and dissolve to dutch-ceylon | dutch-ceylon 1658 gain (includes Matara) | matched (land wider there) |
| sitawaka 1574 loss portuguese-ceylon | none here | missing |
| ceylon 1506 dissolve to portuguese-ceylon | predecessor ceylon | mismatch (Cliopatria artefact) |
| portuguese-empire 1656/1658 Ceylon losses | same losses here | exception (double drawing; compile picks one) |

Gazetteer: "Mannar Island" (place).
