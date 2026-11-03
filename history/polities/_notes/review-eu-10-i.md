# Review of batch eu-10-i (2026-10-25)

One dossier: principality-of-monaco. Verdict: **fail** (one blocking finding, unapplied). Machine copy: history/notes/phase-b/reviews/eu-10-i.json.

## Mechanical
validate_dossier.py --resolve: 0 errors; 14 warnings, all for the gazetteer's lack of the places Menton and Roquebrune-Cap-Martin (gazetteer_names_needed). The merge of 'Kingdom of Monaco' into this dossier is right (same Q235, rows alternate, same polygons); all 9 Cliopatria shapes have verdicts; the 1642-2024 shapes are well handled (oversized, the post-1848 ones displaced west, flagged).

## Fix 1 (blocking, back to the author): Grimaldi rule was interrupted 1301-1419
Keyframes 0-2 and the ledger draw the Grimaldi holding the Rock without a break from 1297 to 1641. The Monaco page the author cited says 'Francesco was evicted a few years later by the Genoese forces, and the struggle over "the Rock" continued for another century', 'The House of Grimaldi has ruled Monaco, with brief interruptions, since 1297', 'in the late 1300s Genoa lost Monaco after fighting the Crown of Aragon' and 'In 1419, the Grimaldi family purchased Monaco from the Crown of Aragon and became the official and undisputed rulers'. List of rulers of Monaco (https://en.wikipedia.org/wiki/List_of_rulers_of_Monaco) gives the spans: Genoese control 10 April 1301 to 12 September 1331 (Charles I 'retook the Rock'); 15 August 1357 to January 1395 (Rainier II 'Yielded Monaco to the besieging Genoese for 20,000 fl. but retained Menton and Roquebrune'); 19 December 1395 to 11 May 1397; 5 November 1402 to 5 June 1419 (the sons of Rainier II 'bought back Monaco from Genoa'); and 'occupied by the Duchy of Milan ... from 3 October to November 1436'.

What to write: losses to republic-of-genoa 1301-04, 1357-08 (Rock only), 1395-12, 1402-11; gains 1331-09, 1395-01, 1397-05, 1419-06 (seller: Genoa on the list page, the Crown of Aragon on the Monaco page; choose and note it); occupation_start 1436-10 / occupation_end 1436-11 with duchy-of-milan. Re-cut the new keyframes to the spans (Rock 1297-1300; nothing 1301-1330, or start at 1331 and say why; Rock 1331-1345; plus Menton 1346-1354; three places 1355-1356; Menton and Roquebrune only 1357-1394, 1396, 1402-1418; three places 1395, 1397-1401, 1419-1641). Correct keyframe 0's 'Under Genoese sovereignty until the Spanish authority of 1524' and the capital span (the seat cannot be the Rock while Genoa held it).

## Fix 2 (applied by the reviewer)
The dossier's notes quoted the Monaco page as 'roughly tenfold'; the page says 'increasing its territory by almost ten times'. Changed in the dossier; re-validated (0 errors, 0 warnings). The same phrase in _notes/eu-10-i.md is yours to change.

## Spot checks (all confirmed)
1297 (Monaco infobox 8 January 1297), 1346 Menton, 1355 Roquebrune, 1612 style of Prince, 1793 French takeover, 17 May 1814 restoration, 1848 secession, 2 February 1861 renunciation (4 million francs), 11 November 1942 Italian occupation, 3 September 1944 liberation. Area: infobox 2.084 km2 against Cliopatria 94.1 km2 in 2024 (ratio 45), acknowledged and corrected.

## Thin (for a gap-filler)
Sellers of Menton (1346) and Roquebrune (1355): try https://en.wikipedia.org/wiki/Charles_I,_Lord_of_Monaco. Ruler list: List of rulers of Monaco has every reign date.

## Cross-dossier
- kingdom-of-italy lacks the occupation of Monaco (add occupation_start 1942-11 and occupation_end 1943-09, counterpart principality-of-monaco).
- kingdom-of-sardinia has vassal_start 1817 / vassal_end 1860-03 of Monaco; History of Monaco gives the Congress of Vienna, 1815 for the start (Stupinigi 1817 confirms it). Sardinia's author may move the start to 1815.
- kingdom-of-france lacks the French protectorate (vassal_start 1641-09, Treaty of Péronne); kingdom-of-spain lacks the Spanish one (1524-1641).
- duchy-of-milan has no 1436 occupation of Monaco; republic-of-genoa (not written) must mirror the Genoese periods above.
- second-french-empire (not written) should take Menton and Roquebrune in 1860 (plebiscite 15-16 April 1860) and note Monaco's 1861 renunciation; Monaco's 1861 loss moves no land because its 1848 loss already removed it.
- Exceptions (counterpart not written yet): french-first-republic 1793, first-french-empire 1814, nazi-germany 1943-1944, the free cities of Menton and Roquebrune 1848 (listed for a stub).

## For the orchestrator
The eu-20 briefs still list kingdom-of-monaco as owned: that batch must not write it.
