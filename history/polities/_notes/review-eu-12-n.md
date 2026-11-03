# Review of batch eu-12-n (iberian-union, catalonia, pro-habsburg-spain)

Reviewer, 2026-10-31. Machine copy: history/notes/phase-b/reviews/eu-12-n.json.

Validator (`--resolve --json`): all three valid, 0 errors, 0 warnings, before and after the reviewer's edits.

Verdicts: iberian-union **fail** (two small fixes applied by the reviewer, three blocking findings left for the author or orchestrator); catalonia **pass** (one cross-dossier mismatch to settle on the neighbours' side); pro-habsburg-spain **pass**.

## iberian-union: fail

Applied by the reviewer (re-validated):

1. `/ledger/21`: Lower Palatinate occupation moved from October 1619 to **August 1620**. The Thirty Years' War page does say "October 1619", but the Palatinate campaign page says "In August 1620, Spinola entered the Lower Palatinate through Brussels" and that the "Spanish occupation of Palatinate wouldn't end until 1652". Source changed to https://en.wikipedia.org/wiki/Palatinate_campaign (added to `sources[]`).
2. `/ledger/31`-`/ledger/32`: the 1636 `contest_end` (Aisne, Somme, Oise) came before its own `contest_start` (1636, month 8). The start now comes first, without a month, because the page's "August" is when the incursion reached Corbie. The page gives no month for the retreat.

Left for the author (blocking):

3. **Parma's reconquest of 1585 is missing** (`/ledger/9`, `/keyframe_review/2`). Cliopatria's Dutch Republic row holds Ghent, Brussels and Antwerp from 1582 to 1587, and the union's 1588 shape adds them (+13,000 km2). The dossier folds them into a 1588 gain at confidence 1, describes it as "mostly the north-east", and calls the page silent. The Eighty Years' War page, which the author opened and quotes, says "Parma's reconquests more or less stalled after the Fall of Antwerp (1585)". dutch-republic and habsburg-netherlands both date the block to 1585. Fix: add a 1585 gain (confidence 2) and a new keyframe iberian-union_1585 (1585-1587), and keep the 1588 gain for the north-east only.
4. **Oldenzaal and Groenlo are lost twice** (`/ledger/14` in 1597, then `/ledger/24`-`/ledger/25` in 1626-1627) and never regained in between. Spinola's campaign of 1605-1606 is on the same page ("Spain recorded successes ... during Spinola's campaign of 1605-1606"). The 1609 keyframe accepts Cliopatria's re-added Twente and Achterhoek cells with no event. habsburg-netherlands `/ledger/23` and dutch-republic `/ledger/12` carry the 1606 mirror. Fix: add a 1606 gain (confidence 2) and adjust the 1604 keyframe.
5. **Low Countries ownership.** habsburg-netherlands (eu-09, 1482-1795) draws the same land, and dutch-republic pairs every Dutch-front event with habsburg-netherlands. None of the union's 14 Dutch-front events has a mirror naming the union. The author flagged this. The orchestrator has to choose. Recommended: habsburg-netherlands keeps the Low Countries; the union subtracts them from its keyframes and drops the Dutch-front events, keeping only the war.

Thin (for a gap-filler): the Cardinal-Infante's recapture of Venlo and Roermond in 1637 is missing (Cardinal-Infante Ferdinand page; dutch-republic `/ledger/22`, habsburg-netherlands `/ledger/31`). Palatinate cells: dropped in 1632 and restored in 1636, both at confidence 1. The occupation lasted to 1652 per the Palatinate campaign page, so the 1632 drop needs a page. The confidence-1 bridging and closing events are `/ledger/5` and `/ledger/36`-`/ledger/38`. The Cork cell 1602-1608 is probably too long: the Spanish at Kinsale surrendered in January 1602. Bahrain to 1608 is also probably too long: it was lost in 1602. The Livorno-province cells from 1600 are probably Porto Longone (1603, Stato dei Presidi). The Italian dominions have no events.

Spot checks: 1590, 1591, 1625, 1632 and 1637 confirmed on the Eighty Years' War page; 1581 (Tomar) and 1 December 1640 confirmed on the Iberian Union page; May 1635 and Corbie in August 1636 confirmed on the Franco-Spanish War page; 1619 mis-dated (fixed). Area: the Iberian Union infobox has no area (checked). Cliopatria's 797,000-814,000 km2 is plausible for the composite monarchy.

Cross-dossier: yarubid-dynasty `/ledger/1` (1633) takes Julfar from iberian-union, but the union has no matching loss, and its 1600 grid shape does not cover Julfar. Route to me-10. electoral-palatinate `/ledger/7` dates the occupation to 1621 with counterpart kingdom-of-spain; it should be iberian-union in 1620.

## catalonia: pass

Spot checks on the Reapers' War page:

- May 1640, the Bloody Corpus: confirmed.
- 17 January 1641, the Catalan Republic: confirmed.
- 23 January 1641, Louis XIII as Count of Barcelona: confirmed.
- 26 January 1641, Montjuic: confirmed.

The Franco-Spanish War page confirms the 1641 recognition. Area: infobox 32,113.86 km2 against Cliopatria's 33,801 km2 (ratio 1.05, acknowledged). Capital, rulers, wars and certainty are consistent.

Cross-dossier mismatch: kingdom-of-france (eu-10) makes catalonia a vassal from 1641 to 1652, and kingdom-of-spain ends its contest with catalonia in 1652, yet this dossier ends in January 1641 with a dissolve into France. The Catalonia page says "Within a brief period France took full control of Catalonia", which supports this dossier. Recommended fix on the neighbours' side: France records a gain from catalonia in 1641 and a loss to kingdom-of-spain in 1652. kingdom-of-spain points its 1652 contest_end at kingdom-of-france. If the orchestrator prefers the vassal model instead, catalonia must run to 1652 with new keyframes.

Thin: Roussillon is drawn Catalan in 1640-1641, though Perpignan, Collioure and Salses held for Philip IV until 1642. Tarragona fell to Los Velez in December 1640, and Tortosa stayed royalist. Minor: in May 1640 the crown's side was still the iberian-union, not kingdom-of-spain (contest counterpart).

## pro-habsburg-spain: pass

Spot checks:

- 1705 Valencia: confirmed on the Almansa page ("the Allied capture of Barcelona and Valencia", in its 1705 context).
- 25 April 1707: confirmed on the Almansa page.
- 11 September 1714: confirmed on the Catalonia page.
- June 1715: confirmed on the War of the Spanish Succession page.
- 10 December 1710, Villaviciosa: confirmed on the War of the Spanish Succession page.

Area: the Wikipedia title "Habsburg Spain" is the 1516-1700 monarchy, so no infobox applies. 102,000-108,000 km2 matches the Crown of Aragon with the Balearics.

Settled for the kingdom-of-spain owner:

- Valencia went over in 1705, not 1706.
- Catalonia fell on 11 September 1714. Only the Balearics held out to June 1715. kingdom-of-spain `/ledger/51` should be split.
- kingdom-of-spain has no occupation events for Madrid in 1706 and Madrid and Zaragoza in 1710.

Thin:

- The Balearics are dated 1706 at confidence 1.
- Menorca was British from 1708.
- Charles III's ruler span ends in 1711 although the state runs to 1715.
