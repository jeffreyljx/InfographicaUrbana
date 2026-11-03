# Review of batch eu-07-e (West Francia and the Burgundies)

Reviewer, 2026-10-24. Dossiers: west-franks, lower-burgundy, upper-burgundy. All three validate (0 errors); `--resolve` warnings are the author's intentional empty corrections and the `kingdom-of-lotharingia` slug. No dossier was edited by the reviewer. No neighbour dossier exists yet (none of the Context polities of the author's brief is in history/polities/), so every counterpart outside the batch is an exception "group has not run yet". Pages opened: West Francia, Treaty of Meerssen (twice), Boso of Provence, Lotharingia, Treaty of Saint-Clair-sur-Epte, Charles the Simple, Odo of France, Treaty of Ribemont, Charles the Fat, Charles of Provence, Hugh of Italy (twice), Upper Burgundy, Rudolf II of Burgundy, Lower Burgundy, Louis the Blind, Charles the Bald. No infobox gives an area.

Every confidence-3 event checked was confirmed on its page with its year (and month where given). Nothing fabricated was found. The failures are in the shapes.

## west-franks: fail

1. **Blocking: the Aquitaine subtraction, 896-989** (`/keyframe_review/14`-`/21`). The corrections subtract Cliopatria's whole Aquitaine 895 shape. That shape is all of southern France: Toulouse (13 cells within 30 km), Narbonne and Septimania (8), Bordeaux and Gascony (11), and Auvergne. The base shape therefore stops at 45.5-45.65 N. In cells, 896-910 is 750 cells (189,675 km2; Cliopatria 375,679), and 926-989 is 661-663 cells (about 167,000 km2; Cliopatria 354,017, ratio 0.47).
   - The batch notes say Toulouse, Septimania, Gascony and the Spanish March "are inside the base shape". That is false for 888-989.
   - The page sentence relied on names Aquitaine only: "Although Aquitaine did not become a separate kingdom, it was largely outside the control of the West Frankish kings."
   - Nothing owns the removed land in 896-989. The vassal counterpart is `aquitaine`, a Cliopatria row that ends in 895, while the report asks for `duchy-of-aquitaine` 896-989.
   - The vassal region also overlaps County of Rosellón 896 (16 cells) and County of Berga 898 (3 cells).
   - **Fix**, one of two:
     - (a), recommended, the author's own fallback: revert the eight corrections to the Cliopatria shapes, keeping the 936 union with Upper Burgundy 936.
     - (b) Subtract only the duchy proper (Poitou, Limousin, Auvergne, Berry) and keep Toulouse, Septimania and Gascony.
   - In either case, point the vassal pair at the slug that will own the land, and correct the notes sentence.
2. **Missing war, 978-980.** Lothair's invasion captured Aachen, Otto II counter-attacked to the walls of Paris, and Lothair renounced Lotharingia in 980 (Lotharingia page; West Francia page: "in 978 Lothair attacked the old imperial capital Aachen"). Add it with empty zones and say that no border moved.
3. **San Marino cell, 860-880.** One San Marino cell (12.41 E) survives the minus-union of Italy, Slovenia and Croatia in the seven corrections 860-880. Add `{"country": "San Marino"}` to the union.
4. **Thin items, for the gap-filler:**
   - 870 Breton cells (c1): Entrammes 863 and Compiègne 867, on the Salomon of Brittany page.
   - 926 Norman cells (c1): the grants of 924 (Bessin, Maine) and 933 (Cotentin, Avranchin). Cliopatria's Normandy grows again in 936 and West Francia has no event for it. Page: William I Longsword.
   - Urgell 870 and 878, Pallars and Ribagorza 875 (c1).
   - vassal_end 989 (c1).
   - The 52 Alpine/French cells (860) and 67 Frisian cells (886).
   - Lothair's capture of Verdun (984-985), which is on neither opened page.
5. **Checked, not broken:**
   - Meerssen, 8 August 870 (Lyon, Vienne, Besançon).
   - The 869 coronation at Metz.
   - Andernach, 8 October 876.
   - Boso count of Provence in 877 (c2 is honest: the page does not name the king).
   - Ribemont, February 880.
   - "Ranulf … submitted by 889".
   - Saint-Clair-sur-Epte, autumn 911, Upper Normandy (Seine-Maritime and Eure are a fair reading).
   - Lotharingia crowned in early November 911; Henry's invasion of 923; Lotharingia lost in 925.
   - Charles the Fat's West Frankish reign: from 12 December 884, with 20 May 885 as the crowning, so 885 is defensible.
   - The Iceland fragment in Cliopatria's bbox 860-935 resolves to no cells.

## lower-burgundy: fail

1. **Blocking: Lyon and Vienne missing, 855-862** (`/keyframe_review/0` and `/1/correction`, `/ledger/0/region`, `/identity/predecessors/0/land`).
   - "Lower Burgundy 860 minus Lower Burgundy 866" resolves to 211 cells. It holds 0 of the 37 Lyonnais cells and 4 of the 48 cells within 60 km of Vienne, because Cliopatria's 866 polygon (Lothair II's kingdom) contains them.
   - The note says "Provence, Lyon, Vienne". The Charles of Provence page says that on Charles's death "Lothair received the bishoprics of Lyon, Vienne and Grenoble", so they were his.
   - The 863 loss therefore removes land the keyframes never held.
   - **Fix:** union the Lyonnais and Vienne (60 km) back into all four specs.
2. **Blocking: no keyframe for the 931 loss** (`/ledger/14`). kingdom-of-lower-burgundy_926 keeps the Viennois and Lyonnais to 935. That gives a 57-cell double claim with upper-burgundy_931 (931-932). Add a new keyframe lower-burgundy_931 (931-933): Lower Burgundy 925 minus the Lyonnais and Vienne 60 km.
3. **The 880 Saône-et-Loire pair moves land no keyframe holds.** Lower Burgundy 880 has 2 of 35 cells; West Francia keeps 33. Either add Saône-et-Loire (Mâcon) to the 879 transfer with a 879-880 keyframe, or shrink the pair to the 2 cells.
4. **One dossier or two (orchestrator's call).** The dossier joins Charles of Provence's kingdom (855-863) and Boso's (879-933) across a 16-year gap. The Lower Burgundy page dates the state from 879 and presents Boso's realm as new.
5. **Vienne after 882.** The 882-886 keyframes keep the county of Vienne, while the pages say Richard took the city in September 882. This is defensible on the undated "restricted to the county of Vienne"; say so in the note.
6. **Checked, not broken:**
   - The 863 division: 25 January 863; Lyon, Vienne and Grenoble to Lothair; Arles, Aix and Embrun to Louis.
   - Mantaille, 15 October 879.
   - May 887.
   - Pavia, 12 October 900; 902; blinding at Verona, 21 July 905.
   - 931 "gift of the Viennois and Lyonnais".
   - The 933 treaty: "in return for being handed Provence". The Lower Burgundy page also has "In 932-933, Hugh made peace with Rudolph … by giving him the Lower Burgundy".

## upper-burgundy: thin

1. **The 911 c1 gain "from west-franks"** of a 40 km disc round Besançon. This is land the dossier already holds: 18 of the 19 cells are in the 888 shape, and the Upper Burgundy page puts "the Burgundian comital estates around Besançon and Dole" in the kingdom from its foundation. Cliopatria's 911 change is only 2 cells, and West Francia has no mirror loss. Drop the event, or make it the 2-cell delta with counterpart `nobody`.
2. **Keyframes inside another keyframe's span.** The new keyframes 931-932 and 933-935 sit inside upper-burgundy_926 (926-935). Say in the 926 note that they supersede it, and the orchestrator should confirm the compiler rule.
3. **Thin items:**
   - No page names a capital; Saint-Maurice is a placeholder.
   - Basel 916-926: the page dates the defeat at Winterthur to 919, and the exchange is "926 or 935", so holding Basel to 926 is unconfirmed.
   - dissolve 935 is c1.
4. **Checked, not broken:**
   - 888 election at St. Maurice.
   - "in 916 occupied the city of Basel".
   - King of Italy 922-926 (Fiorenzuola, 17 July 923).
   - "In 933, Rudolph II acquired the Kingdom of Lower Burgundy".
   - The 933-935 union (485 cells) matches Kingdom of Arles 936.

## Cross-dossier matrix (batch-internal)

These pairs between this batch's own dossiers match by year:

- west-franks ↔ lower-burgundy: 879, 880, 882 and 887.
- lower-burgundy ↔ upper-burgundy: 931 and 933.

One pair is missing: upper-burgundy's 911 gain from west-franks has no loss in west-franks.

All other counterparts are exceptions, either groups that have not run or listed needed dossiers: kingdom-of-lotharingia, aquitaine/duchy-of-aquitaine, kingdom-of-italy, east-franks, kingdom-of-brittany, the Catalan counties, duchy-of-normandy, kingdom-of-germany and Duchy of Swabia.
