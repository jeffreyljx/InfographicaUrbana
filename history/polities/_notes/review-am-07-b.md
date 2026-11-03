# Review of batch am-07-b (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: new-france, new-sweden. Both validate (`--resolve`: new-france has 5 "resolves to no cells" warnings, all on the deliberately empty keyframes 1629-1631 and 1763-1791; new-sweden none).

## new-sweden: fix (fixed by the reviewer)

Spot checks (4), all confirmed on the page: /ledger/0 (Fort Christina page: "the Swedes arrived in Delaware Bay (Fort Christina) on March 29, 1638"), /ledger/1 (New Sweden page: Fort Nya Elfsborg on the east bank; "Settlements were established on both sides of the Delaware River"), /ledger/3 ("In May 1654, soldiers from New Sweden led by Governor Johan Risingh captured Fort Casimir"), /ledger/6 ("surrendered on September 15, 1655"). Neither page gives an area (confirmed); the 2,841 km2 shape stands.

Applied: /identity/rulers/1-5 had no `source`; the New Sweden infobox lists the governors with exactly these years (Kling 1638-1640, Ridder 1640-1643, Printz 1643-1653, Papegoja 1653-1654, Risingh 1654-1655). Added `"source": "https://en.wikipedia.org/wiki/New_Sweden"` to each; re-validated OK.

Advisory, not applied, not blocking: new-netherland /ledger/8 gains Fort Casimir (15 km disk) in 1651 from `nobody`, while new-sweden keeps those 3 cells in its 1640 and 1653 keyframes from 1640 to 1655 (the 1640 keyframe note admits it). The two dossiers both hold the fort 1651 to May 1654. Either add a 1651 loss of the Fort Casimir disk to new-netherland here (New Sweden page: "In 1651, the Dutch West India Company abandoned Fort Nassau and established" Fort Casimir) and change new-netherland's 1651 counterpart to new-sweden, or leave it as the contested edge the certainty note describes.

## new-france: thin

Nothing fabricated found. Spot checks (13 events on 9 pages), all confirmed with the year and month: /ledger/0 (Acadia: Saint Croix Island 1604), /ledger/5 (Treaty of Saint-Germain-en-Laye page: "On 19 July 1629 ... surrender of Quebec"), /ledger/6 (signed March 29, 1632), /ledger/8 and /ledger/13 (Acadia: "again from 1654 until 1670"), /ledger/9 (Cape Breton Island: "lasted only one generation, until Nicolas Denys left in 1659"), /ledger/22 (HBC: "In March 1686 the French sent a raiding party under the Chevalier de Troyes"), /ledger/27 (HBC: Battle of Hudson's Bay 5 September 1697), /ledger/30 (Louisiana (New France): "In January, ... Bienville founds Mobile", 1702), /ledger/31 (Acadia: "conquered in 1710 during Queen Anne's War"), /ledger/32 (Cape Breton: communities and Louisbourg "re-established in 1713"), /ledger/49 (La Verendrye: Fort La Reine "(October 1738)"), /ledger/58 (Fontainebleau 1762; November from the Treaty of Paris page's "three months earlier"), /ledger/62 (Treaty of Paris: signed 10 February 1763, Article IV "Canada, with all its dependencies").

Area: the New France infobox has no area field and the body gives no km2 figure (confirmed); the author said so. Cliopatria's max is 249,126 km2 (1757, including the overseas pieces).

Scope handling is sound: the overseas cells of the composite Cliopatria row are cut with `intersect Canada/United States`, the 1629-1631 Saint Martin shape (known problem) is marked wrong, and the 1763-1791 shapes are marked wrong with empty corrections.

### Unapplied findings (author or gap-filler; none blocking)

1. /ledger/58/region vs /ledger/64/note. Note 64 says Louisiana's Florida parishes north of the Iberville "are treated as part of this land" (to Britain), but region 64 is Mississippi+Alabama+Illinois only, while region 58 (to spanish-louisiana) takes all of the Louisiana admin1 cells of the 1762 shape: 23 of its 105 Louisiana cells lie east of 91.0 W and north of 30.3 N, i.e. the east bank above the Iberville, which Article VII of the Treaty of Paris (line "along the middle of the River Mississippi ... to the river Iberville") gives to Britain. Fix: subtract the east bank north of the Iberville/Lake Maurepas from region 58 and add it to region 64 (Isle of Orleans stays with 58).
2. /wars/3/from = 1710. Queen Anne's War began in 1702; the author admits the pages opened do not give the start. Fix: 1702 after opening https://en.wikipedia.org/wiki/Queen_Anne%27s_War.
3. /identity/successors/2 (kingdom-of-france, Saint Pierre and Miquelon). The Treaty of Paris page says France "reacquired" the islands from Britain; they were ceded in 1713 and were not New France land in 1763, and no ledger event or keyframe of this dossier holds them. The note's "kept" is wrong. Fix: drop this successor (keep the remark in `notes`) or reword it as land received from Britain, not from New France.

### Thin: border moves the ledger does not explain

- The 11 confidence-1 events: /ledger/7 (1642, Saint Lawrence; Ville-Marie/Montreal 1642), /ledger/16 (1673 Green Bay), /ledger/17 (1677), /ledger/20 (1683), /ledger/24 and /ledger/25 (Texas 1687-1691, Fort Saint Louis), /ledger/41 (1718 Alabama, Michigan-Indiana: Fort Toulouse 1717, Fort Ouiatenon 1717), /ledger/42 (1721 Ile Saint-Jean), /ledger/43 (1721 Louisiana), /ledger/48 (1734 claim fill), /ledger/50 (1741 Manitoba). Pages to try are in the JSON report.
- 1734, Lake Champlain: Cliopatria's 1734 shape adds 16 cells in New York (west shore of Lake Champlain; Fort Saint-Frederic) that no event explains (/ledger/48 covers Maine, New Brunswick and Quebec only). haudenosaunee /ledger/25 already records a 1734 loss of these cells to new-france. Add a 1734 gain (counterpart haudenosaunee) and, from the same page, the 1759 loss of Carillon/Saint-Frederic.
- King George's War (1744-1748) is missing from /wars; the Acadia page dates its declarations reaching Louisbourg "on May 3, 1744", and the author's own notes say the Ile-Royale page tabulates the 1745-1748 British hold of Louisbourg. Add the war and occupation_start (June 1745) / occupation_end (1749 handover after Aix-la-Chapelle) on Ile Royale.
- Father Rale's War (Acadia page: Shute "officially declared war on 22 July 1722") is missing from /wars.
- Beaver Wars: haudenosaunee lists new-france as a belligerent (1609-1701); new-france has no war entry.
- East Texas: viceroyalty-of-new-spain holds a contest with new-france 1716-1762 (Sabine-Red River); new-france has no matching contest events and no entry for the 1719 French capture of Pensacola (War of the Quadruple Alliance).
- 1758-1759 forts: Fort Frontenac (August 1758), Fort Duquesne (November 1758), Fort Niagara and Carillon (July 1759) fall inside the 1757 shape span and are carried only by the 1760 occupation; individual losses would sharpen the 1758-1760 map.
- 1690: Phips's capture of Port-Royal (King William's War) is not on the Acadia page body; https://en.wikipedia.org/wiki/Battle_of_Port_Royal_(1690).

## Cross-dossier matrix (summary)

Matched: new-france 1629, 1629-07, 1632-03 with english-colonial-empire; new-france 1697-09 with english-colonial-empire 1696 loss (within a year, but that event is confidence 1 and in the wrong year: the HBC page dates the capture to September 1697 and says the company recovered the fort after 1694, so the English side should read 1697-09); new-france 1762-11 with spanish-louisiana found 1762-11 and spanish-empire gain 1762-11. New Sweden 1654-05, 1655 and 1655-09 with new-netherland.

Missing on the other side (am-07-a, which has run): english-colonial-empire has no events for Acadia 1654 (gain) and 1670 (loss), nor for the James Bay posts 1686 (loss, contest) and the 1713 contest end; the author flagged these.

Mismatch: haudenosaunee 1734 loss to new-france (Lake Champlain) has no gain here; viceroyalty-of-new-spain 1716/1762 contest with new-france has no events here; new-netherland 1651 gain of Fort Casimir from nobody overlaps new-sweden's shape 1651-1654.

Exceptions: every british-colonial-empire counterpart (1710, 1713, 1755, 1758-1763; group eu-11, no dossier yet); gains from `nobody` in Indigenous land (Lenape, Quapaw, Illinois etc.; listed by the author for am-05).
