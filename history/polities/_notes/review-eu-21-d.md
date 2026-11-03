# Review eu-21-d (2026-11-01)

Adversarial review of six dossiers by the eu-21-d author. Validator: 0 errors for all six (eire: 6 gazetteer warnings for Cobh, Castletownbere, Buncrana). One fix applied by the reviewer (francoist-spain). Machine copy: history/notes/phase-b/reviews/eu-21-d.json.

| slug | verdict |
| --- | --- |
| spanish-nationalists | thin |
| eire | pass |
| francoist-spain | fix |
| free-french | thin |
| vichy-france | thin |
| independent-state-of-croatia | fail |

## spanish-nationalists: thin

Area: infobox None (None), Cliopatria 338687, ratio None. Nationalist faction page has no infobox area; Cliopatria 1938 shape 338,687 km2 is plausible for the post-Aragon front.

Findings:

- `/ledger/5 (and /ledger/4, /ledger/8 zones)` (for the author, not blocking). The June 1937 gain includes Gipuzkoa, which the cited page dates to September 1936. Evidence: War_in_the_North: 'In September, after the fall of Irun and then of San Sebastián' (1936, before the 1937 campaign 'to capture the province of Biscay' begun 31 March 1937). The Cliopatria 1936-37 shape has no Gipuzkoa (author's overlay), so Gipuzkoa is Republican on the map until June 1937. Fix: Make /ledger/5 Bizkaia only; add a gain 1936-09 {admin1: Gipuzkoa} (most of the province; Eibar-Deba stayed Republican to 1937) from second-spanish-republic, source War_in_the_North, confidence 3; drop Gipuzkoa from the 1937 contest zone. second-spanish-republic (eu-21-c) needs the mirror loss.
- `/ledger/2/region` (for the author, not blocking). admin1 Baleares includes Menorca, which stayed Republican to February 1939; the note itself says Menorca is not named. Evidence: Spanish_Civil_War: 'Goded and Franco immediately took control of the islands to which they were assigned' (no island named); Menorca is not mentioned on the page. Fix: Region = Baleares minus Menorca (gazetteer needs 'Menorca'); add a 1939-02 gain of Menorca once a page dates it (gap list).
- `/keyframe_review/0/note and history/polities/_notes/eu-21-d.md` (for the author, not blocking). The notes call the 1936-1937 shape 'the end-of-1936 front', but by the author's own overlay it lacks Huelva, Badajoz, Toledo, Gipuzkoa and Málaga (under 5 percent each): it is the July 1936 coup zone, so /ledger/9 (confidence 1, 1938) lumps land taken in August-September 1936 and February 1937 into 1938. Evidence: Overlay figures quoted in /ledger/9's note (Huelva 95 against under 2, Badajoz 77 against 4, Toledo 64 against under 2, Málaga 92 against under 2 percent); Badajoz, Toledo and the Gipuzkoa campaign are 1936 events, Málaga February 1937. Fix: Correct the notes to 'July 1936 coup zone' and keep /ledger/9 at confidence 1 until a gap-filler dates its parts (thin list).

Gaps for a gap-filler:

- `/ledger/9`: Dates for the 1936-1937 conquests lumped into 1938: Huelva and Badajoz/Extremadura (Aug 1936), Toledo and the Tagus valley (Sept 1936), Málaga (Feb 1937), the Madrid sector. Try https://en.wikipedia.org/wiki/Battle_of_Badajoz_(1936)
- `/ledger/9`: Toledo / Tagus valley, September 1936. Try https://en.wikipedia.org/wiki/Siege_of_the_Alc%C3%A1zar
- `/ledger/9`: Málaga, February 1937. Try https://en.wikipedia.org/wiki/Battle_of_M%C3%A1laga_(1937)
- `/ledger/13`: Month of the Catalonia conquest (Barcelona January 1939, French border February 1939). Try https://en.wikipedia.org/wiki/Catalonia_Offensive
- `/ledger/2`: Menorca's surrender (February 1939). Try https://en.wikipedia.org/wiki/Menorca
- `/ledger (no event)`: When Spanish Guinea, Ifni, Cape Juby and the Spanish Sahara passed to the Nationalists (1936); they appear only in the Francoist 1939 shape. Try https://en.wikipedia.org/wiki/Spanish_Guinea

Spot checks:

- `/ledger/1` on https://en.wikipedia.org/wiki/Spanish_Morocco: confirmed ('which began in Spanish Morocco ... by an uprising of the Spanish Army of Africa stationed there', 1936)
- `/ledger/5` on https://en.wikipedia.org/wiki/War_in_the_North: confirmed for Biscay ('entered the city on 19 June'); Gipuzkoa part mis-dated (fell September 1936)
- `/ledger/7` on https://en.wikipedia.org/wiki/War_in_the_North: confirmed ('By 21 October, the Nationalists had occupied Gijón and completed the conquest of the northern zone')
- `/ledger/10-12` on https://en.wikipedia.org/wiki/Aragon_Offensive: confirmed (7 March - 19 April 1938; Vinaròs 15 April; Lleida and Gandesa in April)
- `/ledger/14` on https://en.wikipedia.org/wiki/Spanish_Civil_War: confirmed ('Franco entered the capital and declared victory on 1 April 1939')
- `/ledger/2, /ledger/13` on https://en.wikipedia.org/wiki/Spanish_Civil_War: confirmed (quotes present; no island or month named)

## eire: pass

Tried: Treaty Port dates, the 1949 rename, the irish-free-state handover (matched 1937-12), the area, family (no Ireland family in colours.json; britain acceptable). Could not break. The occupation pairs have no mirror in united-kingdom (eu-11), routed in cross_checks; the dossier's notes still say united-kingdom 'has no dossier yet', which is now out of date (cosmetic).

Area: infobox 70273 (2024), Cliopatria 74947, ratio 1.07. Éire page has no infobox; 70,273 km2 is the Republic of Ireland infobox figure the author cites (not re-opened). Shapes 1938-2024 constant.

Spot checks:

- `/ledger/4` on https://en.wikipedia.org/wiki/Treaty_Ports_(Ireland): confirmed (Spike Island handed over 11 July 1938)
- `/ledger/5` on https://en.wikipedia.org/wiki/Treaty_Ports_(Ireland): confirmed (Berehaven 29 September 1938)
- `/ledger/6` on https://en.wikipedia.org/wiki/Treaty_Ports_(Ireland): confirmed (Lough Swilly 3 October 1938)
- `/ledger/7` on https://en.wikipedia.org/wiki/Republic_of_Ireland_Act_1948: confirmed ('came into force on 18 April 1949, Easter Monday')

## francoist-spain: fix

Area: infobox 856045 (1940), Cliopatria 854137, ratio 1.0. 

Findings:

- `/ledger/5 and /wars/0/from` (applied by reviewer). The Ifni War contest_start was dated 1958; the war began on 23 November 1957. Evidence: Ifni_War: infobox '23 November 1957 – 30 June 1958'; 'On 23 November 1957, two villages on the outskirts of Sidi Ifni, Goulimine and Bouizakarne, were occupied'. The Spanish Morocco page only says 'the 1958 Ifni War'. Fix: Applied by reviewer: /ledger/5 year 1957, month 11, source Ifni_War (added to sources[]), note rewritten; /wars/0 from 1957. Re-validated: 0 errors, 0 warnings.

Gaps for a gap-filler:

- `/ledger/10`: Mauritania's share (Tiris al-Gharbiyya) and the date Spanish administration ended (February 1976); morocco and mauritania dossiers disagree with this loss (see cross_checks). Try https://en.wikipedia.org/wiki/Madrid_Accords

Spot checks:

- `/ledger/4` on https://en.wikipedia.org/wiki/Spanish_Morocco: confirmed ('The northern zone became part of independent Morocco on 7 April 1956')
- `/ledger/5` on https://en.wikipedia.org/wiki/Ifni_War: mis-dated (1958 for 23 November 1957); fixed by reviewer
- `/ledger/6` on https://en.wikipedia.org/wiki/Spanish_Morocco: confirmed (Treaty of Angra de Cintra 1 April 1958)
- `/ledger/9` on https://en.wikipedia.org/wiki/Spanish_Morocco: confirmed ('On 5 January 1969 Morocco and Spain signed the treaty ceding Ifni to Morocco')
- `/ledger/10` on https://en.wikipedia.org/wiki/Spanish_Sahara: confirmed as far as the note claims (Madrid Accords 14 November 1975 in infobox; no partition or withdrawal date on page; confidence 2 honest)

## free-french: thin

Area: infobox None (None), Cliopatria 2377926, ratio None. Free France page has no infobox area; corrections (add Chad, drop Gabon in 1940) are explained in keyframe notes.

Findings:

- `/ledger/1/region` (for the author, not blocking). The found event (1940-06) gives Free France Chad, Cameroon, the Congo and Ubangi-Shari two months before they rallied; its own note says 'it held no land until August', and /ledger/2-5 then gain the same land in 1940-08. Evidence: Free_France: 'On 26 August ... Éboué pledged his colony's allegiance'; Vichy_France: 'French Chad on 26 August 1940, French Congo on 29 August 1940, and Ubangi-Shari on 30 August 1940', Cameroun 27 August. Fix: Either start the polity at 1940-08 with Chad as the found region (keep the 18 June appeal in the found note and drop /ledger/2), or keep 1940-06 with a found region that carries no African land; do not draw the four colonies before August.
- `/ledger/0` (for the author, not blocking). Gain with no month (1940) sorts before the found event (1940-06), counterpart vichy-france has no matching loss (explained in the vichy dossier), and Pondicherry is held on the map by french-india (dossier to 1954, no 1940 event). Evidence: Free_France: 'French India and the French South Pacific colonies of New Caledonia, French Polynesia and the New Hebrides' joined 'in summer 1940'. Fix: Give a month after June (summer 1940: July-September; the author should take it from a page) so it follows the found event; drop Pondicherry or route it to french-india as a tint; say in the note which row draws New Caledonia and Polynesia in 1940 (none).
- `/ledger/11, /ledger/18` (for the author, not blocking). The Syria-Lebanon vassal pair has no mirror in french-mandate-for-syria-and-lebanon (which records a 1941-07 rename), and it keeps Lebanon under the tint to 1944-06 though the mandate dossier loses Lebanon to lebanon in 1943-11. Evidence: french-mandate-for-syria-and-lebanon /ledger/13 rename 1941-7, /ledger/14 loss to lebanon 1943-11. Fix: End the Lebanese part of the tint in 1943-11 (or make the region Syria only after it); route the vassal mirror to the mandate dossier's group.
- `/ledger/14` (for the author, not blocking). Djibouti 1942-12 is a gain from french-africa here, but french-africa records it as an occupation by british-africa (1942-12, confidence 3) and a 1943 occupation_end. Evidence: Free_France: 'On 28 December, after a prolonged blockade, the Vichy forces in French Somaliland were ousted.' french-africa /ledger/76-77. Fix: Agree with af-08 on one reading (Free French takeover per French_Somaliland, or British occupation); routed in cross_checks.

Gaps for a gap-filler:

- `/ledger/16`: Confidence-1 bridge: the 1943 return of the equatorial colonies and Djibouti to French Africa under the CFLN. Try https://en.wikipedia.org/wiki/French_Committee_of_National_Liberation
- `/ledger (no event)`: Madagascar (handed to Free French administration after November 1942), Réunion (November 1942). Try https://en.wikipedia.org/wiki/Battle_of_Madagascar
- `/ledger (no event)`: Corsica liberated September-October 1943 (gain from vichy-france/nazi-germany occupation). Try https://en.wikipedia.org/wiki/Liberation_of_Corsica
- `/ledger (no event)`: French West Africa and North Africa after Operation Torch (to the CFLN in 1943); New Hebrides 20 July 1940 (condominium). Try https://en.wikipedia.org/wiki/Operation_Torch

Spot checks:

- `/ledger/0` on https://en.wikipedia.org/wiki/Free_France: confirmed ('summer 1940'; no month)
- `/ledger/2` on https://en.wikipedia.org/wiki/Free_France: confirmed (26 August 1940)
- `/ledger/4, /ledger/5` on https://en.wikipedia.org/wiki/Vichy_France: confirmed (Congo 29 August, Ubangi-Shari 30 August 1940; Cameroun 27 August)
- `/ledger/7` on https://en.wikipedia.org/wiki/Vichy_France: confirmed (Gabon 'occupied by military force between 27 October and 12 November 1940')
- `/ledger/12` on https://en.wikipedia.org/wiki/Free_France: confirmed (24 December 1941)
- `/ledger/15` on https://en.wikipedia.org/wiki/Free_France: confirmed ('finally joined Free France in the first months of 1943'; Martinique 'holding out until July 1943')

## vichy-france: thin

Area: infobox None (None), Cliopatria 356691, ratio None. Vichy France page has no infobox area; the correction to all metropolitan France minus Alsace-Moselle is explained in /keyframe_review/0.

Findings:

- `/ledger/3/region and /ledger/4/region` (for the author, not blocking). The German occupation of 11 November 1942 (confidence 3) covers the whole free zone including Corsica and the Riviera, which /ledger/4 gives to Italy: two occupiers on the same land 1942-11 to 1943-09; /ledger/4 is also smaller than kingdom-of-italy's mirror (/ledger/29: Corsica plus the Cliopatria Italy 1943-minus-1942 strip of France). Evidence: Case_Anton: 'The Italian 4th Army occupied the French Riviera'; 'an Italian division landed on Corsica'. nazi-germany /ledger/44 subtracts an area from its own 1942 region. Fix: Use one Italian-zone region in /ledger/4 (the kingdom-of-italy /ledger/29 spec), subtract it from /ledger/3, and add a 1943-09 German occupation_start over the former Italian zone (Corsica only until its liberation in October 1943) to pair with a 1944 end.
- `/ledger (no event)` (for the author, not blocking). No event for Saint-Pierre and Miquelon (free-french /ledger/12 gains it from vichy-france 1941-12) or for Corsica's liberation (September-October 1943). Evidence: Free_France: Saint-Pierre and Miquelon 'joined the Free French after an "invasion" on 24 December 1941'; 'the liberation of Corsica from Italian occupation began' September 1943. Fix: Add a 1941-12 loss of Saint-Pierre and Miquelon to free-french if the corrected shape (French Third Republic 1939) contains it, else say so; add the 1943 loss of Corsica once dated (thin list).

Gaps for a gap-filler:

- `/ledger/8, /ledger/9`: Confidence-1 liberation dates (June-September 1944; Paris 25 August). Try https://en.wikipedia.org/wiki/Liberation_of_France
- `/ledger (no event)`: Corsica liberated September-October 1943. Try https://en.wikipedia.org/wiki/Liberation_of_Corsica

Spot checks:

- `/ledger/0` on https://en.wikipedia.org/wiki/Vichy_France: confirmed (10 July 1940, 569 votes to 80)
- `/ledger/3` on https://en.wikipedia.org/wiki/Case_Anton: confirmed (11 November 1942; infobox 10-27 November 1942)
- `/ledger/5` on https://en.wikipedia.org/wiki/Free_France: confirmed (Americas 'first months of 1943')
- `/ledger/10` on https://en.wikipedia.org/wiki/Vichy_France: confirmed ('10 July 1940 – 9 August 1944'; Pétain 'until 20 August 1944')

## independent-state-of-croatia: fail

Area: infobox 115133 (1941), Cliopatria 96150, ratio 0.84. 

Findings:

- `/keyframe_review/0/correction, /ledger/1/region, /ledger/4/region, /keyframe_review/2/correction` (blocking). The correction removes all of Dalmatia from the NDH for May 1941 - September 1943, but the Cliopatria 1941 shape already lacks the Italian-annexed coast and islands and holds only the Dalmatian hinterland the NDH kept; /ledger/1 (confidence 3) loses 'Dalmatia' whole where the page says a central portion. Evidence: Independent_State_of_Croatia: 'Italy annexed a significant central portion of Dalmatia and various Adriatic Islands'. Point test on grid.polity_cells('independent-state-of-croatia', 1942): Split, Šibenik, Zadar, Benkovac, Dubrovnik, Korčula, Hvar, Brač are outside the shape; Knin, Drniš, Sinj, Imotski, Makarska, Metković, Senj (and Trogir) are inside. The correction therefore strips about 28 res-5 cells (~7,000 km2) of land the NDH held. Fix: Keep the Cliopatria 1941 shape (verdict ok, or adjust only for Trogir); make /ledger/1 the annexed coast and islands (Split, Šibenik, Trogir, the islands, the Bay of Kotor; 'significant central portion of Dalmatia and various Adriatic Islands') at confidence 2; /ledger/4 regains that region minus Zadar; the 1945 keyframe removes only what the Partisans took.
- `/ledger (no vassal events)` (blocking). No vassal_start/vassal_end: nazi-germany /ledger/28 (vassal_start 1941-4, confidence 3) and /ledger/82 (vassal_end 1945-5) name this state and have no mirror; the Italian protectorate is not recorded either. Evidence: Independent_State_of_Croatia: 'It was a protectorate of Fascist Italy from 1941 to 1943, and a puppet state of Nazi Germany from 1941 to 1945.' Fix: Add vassal_start nazi-germany 1941-4 and vassal_end 1945-5; vassal_start kingdom-of-italy 1941-5 and vassal_end 1943-9; region the state's land; source the NDH page; confidence 3 for the years.
- `/ledger/9, /ledger/10 (and /ledger/6)` (blocking). Sarajevo (1945-4) and the end of the Syrmian contest (1945-4) name yugoslav-partisans, whose dossier dissolves into yugoslavia in 1945-3; the partisans dossier also names nazi-germany, not this state, for the Syrmian front, and has no Mostar or Sarajevo event. Evidence: yugoslav-partisans identity end 1945-3, /ledger/16 dissolve; /ledger/13-14 Syrmian contest with nazi-germany. Fix: Name yugoslavia for /ledger/9; close the /ledger/6 contest with yugoslav-partisans in 1945-3 and open one with yugoslavia to 1945-4 (or end it in 1945-3); ask eu-21 to mirror Mostar.
- `/ledger/2, /ledger/3` (for the author, not blocking). Bihać 1942-11 to 1943 is a contest here but a gain and a loss in yugoslav-partisans (/ledger/4, /ledger/5). Evidence: World_War_II_in_Yugoslavia: the Partisans 'took Bihać and neighbouring towns on 4 November 1942'; Operation Weiss pushed them out of western Bosnia January-April 1943. Fix: Agree one model with the partisans dossier: loss 1942-11 and gain 1943-1 here (the partisans held the town), or contest on both sides.

Gaps for a gap-filler:

- `/ledger/3`: Confidence-1 end of the Bihać Republic (January 1943, Operation Weiss). Try https://en.wikipedia.org/wiki/Case_White
- `/ledger/5`: Confidence-1 1944 Partisan gains (Cliopatria's year only). Try https://en.wikipedia.org/wiki/Yugoslav_Partisans
- `/ledger (no event)`: Hungarian annexation of Međimurje and southern Baranja (1941); the German-Italian demarcation line. Try https://en.wikipedia.org/wiki/Axis_occupation_of_Yugoslavia

Spot checks:

- `/ledger/1` on https://en.wikipedia.org/wiki/Independent_State_of_Croatia: date confirmed (Treaties of Rome 18 May 1941); region over-reaches ('a significant central portion of Dalmatia')
- `/ledger/2` on https://en.wikipedia.org/wiki/World_War_II_in_Yugoslavia: confirmed (4 November 1942)
- `/ledger/4` on https://en.wikipedia.org/wiki/Independent_State_of_Croatia: confirmed (10 September 1943; Zara refused by Germany)
- `/ledger/8, /ledger/9` on https://en.wikipedia.org/wiki/World_War_II_in_Yugoslavia: confirmed ('left Mostar on 12 February 1945'; 'did not leave Sarajevo until 15 April')
- `/ledger/11` on https://en.wikipedia.org/wiki/Independent_State_of_Croatia: confirmed ('Government dissolved: 8 May 1945')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| spanish-nationalists 1936 gain (second-spanish-republic) | second-spanish-republic 1936 loss | matched | Spanish Morocco, Canaries+Balearics, coup zone: SSR /ledger/1-3; both sides include Menorca. |
| spanish-nationalists 1937 gain (second-spanish-republic) | second-spanish-republic 1937 loss | matched | Bizkaia+Gipuzkoa 1937-6, Cantabria 1937-8, Asturias 1937-10 against one SSR loss 1937 (Basque Country, Cantabria, Asturias); both sides date Gipuzkoa to 1937 though it fell in September 1936. |
| spanish-nationalists 1938 gain (second-spanish-republic) | second-spanish-republic 1938 loss | matched | /ledger/9 (conf 1) and /ledger/11 Aragon against SSR /ledger/9 (conf 1). |
| spanish-nationalists 1939 gain (second-spanish-republic) | second-spanish-republic 1939 loss | matched | Catalonia (both 1939, no month) and the rest: SN 1939-4, SSR 1939-3. |
| eire 1937 occupation_start (united-kingdom) | united-kingdom   | missing | Three Treaty Port occupation pairs (1937-12 to 1938-7/9/10); united-kingdom (eu-11) exists and has no Treaty Port event; the Free State dossier has none either. |
| francoist-spain 1940 occupation_start (tangier-international-zone) | tangier-international-zone 1940 occupation_start | matched | Pair 1940-6 to 1945-10 on both sides. |
| francoist-spain 1956 loss (morocco) | morocco 1956 gain | matched | Spanish Morocco 1956-4. |
| francoist-spain 1958 loss (morocco) | morocco 1958 gain | matched | Cape Juby 1958-4. |
| francoist-spain 1968 loss (equatorial-guinea) | equatorial-guinea 1968 found | matched | Found event of Equatorial Guinea names francoist-spain. |
| francoist-spain 1969 loss (morocco) | morocco 1969 gain | matched | Ifni 1969-1. |
| francoist-spain 1975 loss (morocco) | morocco 1975 contest_start | mismatch | Morocco has only a contest 1975-11 to 1976 naming francoist-spain, then an occupation of SADR land; no gain. mauritania /ledger/2 gains Tiris al-Gharbiyya in 1976 from francoist-spain, which dissolved in 1975-11. Route to af-02/af-08 and kingdom-of-spain's group: one owner for the 1975-1976 Saharan transfer. |
| francoist-spain 1975 dissolve (kingdom-of-spain) | kingdom-of-spain 1975 gain | matched | kingdom-of-spain /ledger/89. |
| free-french 1940 gain (vichy-france) | vichy-france   | exception | Pacific colonies and Pondicherry: no Vichy shape holds them (explained in both dossiers); Pondicherry overlaps french-india (to 1954, no 1940 event). |
| free-french 1940 gain (french-africa) | french-africa 1940 loss | matched | Chad, Cameroon, Congo, Ubangi-Shari 1940-8; Gabon 1940-11 with contest pair. |
| free-french 1941 vassal_start (french-mandate-for-syria-and-lebanon) | french-mandate-for-syria-and-lebanon 1941 rename | missing | Mandate records contest 1941-6/7 and a rename, no vassal_start; Lebanon leaves the mandate 1943-11 but the tint runs to 1944-6. |
| free-french 1941 gain (vichy-france) | vichy-france   | missing | Saint-Pierre and Miquelon 1941-12: no loss in vichy-france. |
| free-french 1942 gain (french-africa) | french-africa 1942 occupation_start | mismatch | Djibouti 1942-12: french-africa has an occupation by british-africa (conf 3), not a loss to free-french. |
| free-french 1943 gain (vichy-france) | vichy-france 1943 loss | matched | French Guiana, Guadeloupe, Martinique 1943. |
| free-french 1943 loss (french-africa) | french-africa 1943 gain | matched | Both confidence 1. |
| free-french 1944 dissolve (french-fourth-republic) | french-fourth-republic 1945 found | exception | Gap 1944-6 to 1945: Provisional Government of the French Republic has no dossier (author's counterparts_needing_dossiers). |
| vichy-france 1940 occupation_start (nazi-germany) | nazi-germany 1940 occupation_start | matched | NG /ledger/23 1940-6, /ledger/59 end 1944-8. |
| vichy-france 1940 occupation_start (kingdom-of-italy) | kingdom-of-italy 1940 occupation_start | matched | Italy /ledger/24 (conf 1), end /ledger/33 1943-9. |
| vichy-france 1942 occupation_start (nazi-germany) | nazi-germany 1942 occupation_start | matched | NG /ledger/44 1942-11 and /ledger/60 1944-8; vichy's region overlaps the Italian zone. |
| vichy-france 1942 occupation_start (kingdom-of-italy) | kingdom-of-italy 1942 occupation_start | mismatch | Dates agree (1942-11 to 1943-9) but land differs: vichy Corsica+Alpes-Maritimes; Italy Corsica plus the Cliopatria 1943-minus-1942 strip of France. |
| vichy-france 1944 dissolve (french-fourth-republic) | french-fourth-republic 1945 found | exception | french-fourth-republic names only free-french as predecessor; PGFR dossier needed. |
| independent-state-of-croatia 1941 found (yugoslavia) | yugoslavia   | exception | yugoslavia (1919-1945) is owned by eu-21-b, which has not reported yet. |
| independent-state-of-croatia 1941 loss (kingdom-of-italy) | kingdom-of-italy 1941 gain | mismatch | Italy /ledger/25 gains Dalmatia from yugoslavia, not from the NDH; region also disagrees (see NDH fix). |
| independent-state-of-croatia 1941 vassal_start (nazi-germany) | nazi-germany 1941 vassal_start | missing | NG /ledger/28 vassal_start and /ledger/82 vassal_end name the NDH; NDH has no vassal events. |
| independent-state-of-croatia 1942 contest_start (yugoslav-partisans) | yugoslav-partisans 1942 gain | mismatch | Bihać: contest here, gain/loss (1942-11, 1943) in the partisans dossier. |
| independent-state-of-croatia 1943 gain (kingdom-of-italy) | kingdom-of-italy 1943 loss | mismatch | Italy /ledger/38 loses the Dalmatian annexation to nazi-germany in 1943-9, not to the NDH. |
| independent-state-of-croatia 1944 loss (yugoslav-partisans) | yugoslav-partisans 1944 gain | matched | 1944 conf 1 both sides; Dalmatia 1944-12 both sides. |
| independent-state-of-croatia 1945 loss (yugoslav-partisans) | yugoslav-partisans   | mismatch | Mostar 1945-2 has no partisans event; Sarajevo and the Syrmian contest end 1945-4 name yugoslav-partisans after its 1945-3 dissolution (should be yugoslavia, eu-21-b). |
| independent-state-of-croatia 1945 dissolve (yugoslavia) | yugoslavia   | exception | eu-21-b not yet run. |

## Problems

- Whole-folder mirror scan of history/polities timed out on the network mount; cross-checks used the 25 existing Context dossiers plus irish-free-state, united-kingdom, kingdom-of-spain, french-mandate-for-syria-and-lebanon, french-india. hungarian-republic and unitary-state-of-brazil have no dossier yet (exception).
- yugoslavia (predecessor and successor of the NDH) is owned by eu-21-b, which has no report yet.
- No infobox area on the Nationalist faction, Éire, Free France and Vichy France pages; Éire area taken from the author's Republic of Ireland citation.
- Spanish Civil War page (as fetched) dates none of the 1936-1937 southern conquests, so the 1938 lump in spanish-nationalists stays confidence 1 pending a gap-filler.
- Applied one fix in place: history/polities/francoist-spain.json (/ledger/5, /wars/0, sources[]); re-validated 0 errors, 0 warnings; read back after the write.
