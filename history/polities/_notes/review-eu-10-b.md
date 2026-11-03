# Review of batch eu-10-b (county-of-flanders, county-of-blois, county-of-champagne)

Reviewer, 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-10-b.json.

Mechanical: all three validate with 0 errors (--resolve); warnings are unknown gazetteer places and the not-yet-written slugs county-of-namur, county-of-rethel, county-of-sens. Ledgers sorted, found/dissolve at start/end, wars and certainty inside the life, family `france` exists, capitals inside the shape bboxes. None of the three infoboxes gives an area, so no area ratio (the authors say so). All verdicts are **thin**; the reviewer applied four small fixes (re-validated) and lists the rest for the author or a gap-filler.

## county-of-flanders: thin

Spot checks (all opened): 1167 Vermandois inherited (Philip I page) confirmed; 1186 cession confirmed on the Philip I page; 1322 Nevers (Louis I page) confirmed; 1357 Antwerp and Mechelen and 1369 return of Romance Flanders (Louis II page, 19 June 1369) confirmed; 1191 Artois 'removed from Flanders in 1191' (Flanders page) confirmed.

Applied by the reviewer:
- /ledger/5: confidence 3 -> 2, note extended. The County of Vermandois page says 'the count of Flanders kept the county of Vermandois until his death, in 1191'.

For the author (not applied):
- Vermandois and Amiens, /ledger/4-5 against /keyframe_review/5-6: the ledger loses Amiens in 1185 and Vermandois in March 1186, but the 1169 keyframe holds both to 1187 and the 1188 keyframe drops Vermandois for 1188-1190, while county-of-vermandois and royal-domain-of-france date the land move 1191. Preferred fix: move the Vermandois loss to August 1191, counterpart county-of-vermandois. Add Vermandois (minus Amiens) back into county-of-flanders_1188 for 1188-1190, and add a 1185-1187 keyframe without Amiens. Otherwise keep 1186, add a 1186-1187 keyframe and explain why.
- 1382: Louis II became 'Count of Artois and Burgundy (9 May 1382 - 30 January 1384)' (Louis II page). It is missing from the ledger and the notes. free-county-of-burgundy records it as a rename. Add a notes line, or a gain if personal unions are drawn as Nevers is in 1322.

Gaps for a gap-filler: Rethel 1326 (confidence 1); Mons cells 1260-1304 (Margaret II held Flanders and Hainaut to 1278/1280, so the cells are probably right to 1280 and wrong after); ten Cambrai-Douai-Valenciennes cells 1169-1187; Baldwin V's imperial lands at the Scheldt (duchy-of-lower-lorraine records a loss to Flanders by 1059, with no mirror here); wars missing (Vermandois war 1181-1185, which county-of-vermandois records as a contest 1183-1186; Bouvines 1213-1214; the succession war began in 1244); no events 1216-1259; Pontoise 1312.

## county-of-blois: thin

Spot checks: 1022 Champagne (Odo II page, 'from 1022') confirmed; 1044 Touraine at Nouy (Theobald III page, Blois page) confirmed; 1286 Chartres sale (County of Chartres page) confirmed; 1063 reunion and 1152 division (Blois page) confirmed; 1397 (Crown lands page, 1392 entry) confirmed; 1037 division (Theobald III page) confirmed.

Applied: /notes item (7). The Beauvais title is on the Odo II page, not the Blois page.

Gaps: c. 940 gain (confidence 1, undated on the page); 1294 Châteaudun loss on Cliopatria only, with no counterpart (the Blois-Châtillon counts may have kept Dunois to the sale); 1401 dissolve is Cliopatria's year (royal-domain-of-france takes Blois from duchy-of-orleans in 1498, so a merge into duchy-of-orleans may fit better); Sancerre in no shape.

## county-of-champagne: thin

Spot checks: 1284 merge (Crown lands and Champagne pages) confirmed; 1125 (Theobald II page) confirmed; 1037 (Theobald III page) confirmed; 1089/1093 confirmed in substance; 1055 Sens annexation on the Crown lands page, but not as Champagne's land (confidence 1, honest).

Applied: /keyframe_review/1 (county-of-champagne_1003) was verdict ok for 1003-1027, though it is valid only to 1021 and nothing in this dossier supersedes it, so Champagne and county-of-blois_1022 were both drawn in 1022-1027. It is now adjust with a years-only correction. /ledger/6 and /keyframe_review/5: the misquoted 1093 sentence is replaced by the page's words ('died in 1093, leaving the possessions to his brother Hugh').

Gaps: the 990 start (confidence 1; the Herbertian counts of Troyes and Meaux); the Sens block 1003-1055 (confidence 1; the France dossiers take Sens from its own counts); Henry the Liberal's expansion undated. Note: the Champagne infobox gives 1066 (not 1063) for the second Blois union and 1305 for absorption into France.

## Cross-dossier matrix (summary)

- Matched: Flanders-Vermandois 1167; Flanders-royal domain 1185; Flanders-France 1191 (Artois; France names no holder); all six Blois-Champagne passings; Blois-Anjou 1044; Champagne-France 1284.
- Mismatch:
  - Flanders 1186 against Vermandois and the royal domain 1191.
  - Blois 1286 against France and the royal domain 1284 (Chartres, seller named as county-of-chartres).
  - Champagne 1055 against France and the royal domain 1055, which take Sens from the County of Sens.
  - The HRE's 1033-1034 contest with Blois has no contest in Blois.
  - royal-domain-of-france takes Blois from duchy-of-orleans in 1498, but neither duchy-of-orleans nor Blois records the transfer.
- Missing in other dossiers:
  - France and the royal domain for Flanders 1305 and 1369.
  - HRE for Valenciennes 1013.
  - county-of-brabant for 1357.
  - west-franks for 898 and c. 940.
- Missing in Flanders: the gain matching duchy-of-lower-lorraine's 1059 loss.
- Exceptions:
  - county-of-namur, county-of-rethel and county-of-sens have no dossiers yet (listed).
  - county-of-nevers and duchy-of-burgundy are owned by an eu-10 part that has not written them yet. burgundian-state already records the 1384 gain from Flanders; the two slugs should be agreed.
