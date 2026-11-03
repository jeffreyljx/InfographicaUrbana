# Review of batch am-03 (Toltec and Aztec), 2026-10-18

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/am-03.json. All eight dossiers validate (0 errors) before and after the reviewer's edits. No confidence-3 event was found fabricated or mis-dated; one confidence-2 event was mis-dated (aztec /ledger/24, Soconusco) and is fixed.

Verdicts: toltec fix, texcoco fix, michoacan fix, tenochtitlan fix, aztec-triple-alliance fix, azcapotzalco fix, tlaxcala thin, tututepec fix.

## toltec: fix

- TO DO `/identity/predecessors/0`: The teotihuacan predecessor does not agree with teotihuacan.json and carries no land in a dated event. Evidence: teotihuacan.json (am-01) ends in 750 with successors []; this entry's own note says no land passes and quotes Cliopatria's 704 end, 125 years before the 875 start. Fix: Remove the predecessor and keep the cultural link in notes; if it is kept, change 704 to the teotihuacan dossier's 750 and ask am-01 to list toltec as a successor.
- THIN `/ledger/0`: Founding year: 875 is Cliopatria's (confidence 1); the Toltec page gives no year (infobox c. 950-1168) and the Tula page only 'Tula Chico was abandoned between 850 and 900CE'. Page to try: https://en.wikipedia.org/wiki/Mesoamerican_chronology
- Spot checks: `/ledger/0` confirmed (page silent on the year, as the note says; infobox 'c. 950-1168 AD'); `/ledger/1` confirmed ('reached its height between 900 and 1150'; 'Its political sphere is thought to include most of the present state of Hidalgo'); `/ledger/2` confirmed ('Tula fell around 1150'); `/keyframe_review/2` confirmed ('The chronology dates the destruction of Tula to around 1179')
- Area: No infobox area. The Hidalgo correction resolves to 72 cells, about 18,200 km2 (3.2 x Cliopatria; the keyframe note says 20,800 km2, 3.7 x), acknowledged in /keyframe_review/1 as a soft sphere.

## texcoco: fix

- APPLIED `/keyframe_review/0/correction, /keyframe_review/1/correction, /keyframe_review/2/correction, /ledger/0/region, /ledger/3/region, /ledger/4/region, /wars/0/zones`: The 30 km Texcoco disc contained the Mexico City cell, Tenochtitlan's only cell, so two independent states owned it from 1325 to 1428. Evidence: gazetteer resolve: {"place":"Texcoco","km":30} = 12 cells, bbox west edge -99.14, including the single cell (-99.14, 19.46) that {"place":"Mexico City","km":15} (tenochtitlan's correction) resolves to. Acolhua page: 'The Acolhua settled most of the eastern Basin of Mexico, an area known as Acolhuacan'; Tenochtitlan was a separate island city. Fix: Replaced by {"minus":[{"place":"Texcoco","km":30},{"place":"Mexico City","km":15}]} (11 cells, about 2,780 km2), text kept, reviewer note appended.
- APPLIED `/ledger/5/region, /ledger/6/region, /identity/successors/0/land`: The 1428 merge, dissolve and successor land used {"cliopatria":"Texcoco","year":1428}, the shape this dossier itself marks misplaced. Evidence: That shape resolves to 7 cells at 18.93-19.36 N (Xochimilco, Chalco), only one within 25 km of Texcoco; /keyframe_review/2 replaces it with the disc. Fix: Replaced by the corrected disc {"minus":[{"place":"Texcoco","km":30},{"place":"Mexico City","km":15}]}, text kept.
- Spot checks: `/ledger/0` confirmed ('arrived in the Valley of Mexico in or around the year 1200 CE'; 'first capital was Coatlinchan'); `/ledger/1` confirmed ('In or about 1337, the Acolhua, with Tepanec help, expelled Chichimecs from Tetzcoco'); `/ledger/3` confirmed ('In 1418, Ixtlilxochitl I, the tlatoani (ruler) of Tetzcoco, was dethroned by Tezozomoc of Azcapotzalco'); `/ledger/5` confirmed ('founded in 1428 when the rulers of Tenochtitlan, Texcoco, and Tlacopan formed an alliance'); `/identity/rulers` confirmed (Quinatzin 1298-1357, Techotlalatzin 1357-1409, Ixtlilxochitl 1409-1418, Nezahualcoyotl 1420-1472)
- Area: No infobox area (the city 'occupied an area of 450 hectares'); the corrected disc (about 2,780 km2) is within a factor of two of Cliopatria.

## michoacan: fix

- APPLIED `/ledger/9/region, /wars/0/zones/1`: The 1480 gain drew the whole of Jalisco and Colima where the page says 'parts of'. Evidence: Tarascan state page: 'Between 1480 and 1510, the Iréchikwa occupied parts of present day Colima and Jalisco'. The union resolves to about 72,000 km2 (Jalisco alone 264 cells, 66,800 km2), almost the whole empire's 75,000 km2; the cells Cliopatria actually adds (and /keyframe_review/6-7 remove) are 49 cells, about 12,400 km2. Fix: Region now {"intersect":[{"cliopatria":"Michoacán","year":1482},{"union":[Jalisco, Colima]}]}, text kept, reviewer note appended.
- APPLIED `/ledger/4/region, /ledger/6/region, /wars/1/zones`: The Toluca Valley contest zone (60 km disc) reached the Mexico City cell, making the Aztec capital a contested zone for 1455-1472. Evidence: {"place":"Toluca","km":60} = 40 cells, bbox east edge -99.14 (the Mexico City cell); {"place":"Toluca","km":50} = 27 cells, east edge -99.28, no Mexico City cell. Aztec Empire page names only 'the Toluca Valley'. Fix: Radius cut to 50 km in both dossiers (aztec /ledger/13, /ledger/17, /wars/3 too).
- TO DO `/ledger (no 1472 loss)`: The 1472 Aztec gain from michoacan has no mirror: michoacan records only a contest_end in 1472, and never a gain of the Toluca Valley. Evidence: aztec-triple-alliance /ledger/18 (gain, 1472, counterpart michoacan, confidence 3). Aztec Empire page: 'In 1472, Axayacatl re-conquered the region and successfully defended it from Purépecha's attempts to take it back'; Tarascan state page: 'In 1460 the Iréchikwa reached the Pacific coast at Zacatula, advanced into the Toluca Valley'. No Cliopatria Michoacán shape reaches the Toluca disc. Fix: Add a gain of the Toluca Valley (1460, the Tarascan page's year, confidence 2) and a 1472 loss to aztec-triple-alliance with the region of aztec /ledger/18; or, if the Tarascans held no ground there, the aztec author changes /ledger/18's counterpart (e.g. 'Matlatzinca (Toluca Valley)') and keeps the Purépecha claim as the contest.
- TO DO `/identity/wikipedia`: The Wikipedia title is the modern state 'Michoacán', not the polity's article. Evidence: The dossier's own main source is https://en.wikipedia.org/wiki/Tarascan_state (infobox c. 1300-1530, capital Tzintzuntzan); the author's notes say Cliopatria's field points at the modern state. Fix: Set identity.wikipedia to 'Tarascan state' (Cliopatria's field stays in polities.csv).
- TO DO `/keyframe_review/7/note`: The 1475-1481 correction removes Jalisco and Colima through 1481 while /ledger/9 gains them in 1480. Evidence: Keyframe 7 spans 1475-1481; the gain is dated 1480 (page); the 1482 keyframe (ok) holds them. Fix: Say in the keyframe note that 1480-1481 follow the ledger's 1480 gain (or give keyframe 7 'to': 1479 if the schema allows a narrowed Cliopatria keyframe).
- THIN `/ledger/2`: Year of Hiripan's Cuitzeo conquests (1429 is Cliopatria's, confidence 1). Page to try: https://en.wikipedia.org/wiki/Tzintzuntzan
- THIN `/ledger/3`: Year of the 1440 threefold growth ('between 1401 and 1450', confidence 1). Page to try: https://en.wikipedia.org/wiki/Tzintzuntzan
- THIN `/ledger/7`: Year of Axayacatl's capture of the frontier towns ('In the 1470s', confidence 1). Page to try: https://en.wikipedia.org/wiki/Axayacatl
- THIN `/identity/rulers`: No ruler list (Tariacuri, Hiripan, Tangaxuan I, Tzitzipandaquare, Zuangua, Tangaxuan II); the Tangaxoan II page failed for the author. Page to try: https://en.wikipedia.org/wiki/Tarascan_state
- Spot checks: `/ledger/0` confirmed ('founded in the early 14th century'; infobox c. 1300-1530); `/ledger/5` confirmed ('In 1460 the Iréchikwa reached the Pacific coast at Zacatula, advanced into the Toluca Valley'); `/ledger/6` confirmed ('In 1472, Axayacatl re-conquered the region'); `/ledger/9` confirmed year ('Between 1480 and 1510 ... parts of present day Colima and Jalisco'); region overstated, fixed; `/ledger/14` confirmed ('the king was executed on February 14, 1530'; 'lost its independence to the Spanish in 1530')
- Area: Body text, not infobox: 'By A.D. 1450 ... an empire that spanned 75,000 square kilometers'; within a factor of two of the 1450 shape and quoted in the keyframe notes.

## tenochtitlan: fix

- TO DO `/ledger (no vassal events)`: Azcapotzalco's vassalage of Tenochtitlan (1325-1428) has no mirror in this ledger. Evidence: azcapotzalco /ledger/1 vassal_start 1325 and /ledger/6 vassal_end 1428, counterpart tenochtitlan. Azcapotzalco page: after 1323 'they were subject to military, economic and strategic decisions of the Tepanecas'; Itzcoatl page (quoted by the author): 'the Mexica of Tenochtitlan broke free from Tepanec domination'. Fix: Add vassal_start 1325 and vassal_end 1428 with counterpart azcapotzalco (confidence 1 and 2, the sentences above), as the other Phase B reviews ask of a vassal's dossier.
- TO DO `/ledger/4/region, /ledger/5/region, /identity/successors/0/land`: The 1428 merge, dissolve and successor land use {"cliopatria":"Tenochtitlan","year":1428}, the shape this dossier marks misplaced. Evidence: That shape resolves to 8 cells at 98.84-98.43 W, 19.00-19.49 N, east of the lake, without the Mexico City cell; /keyframe_review/1 replaces it with {"place":"Mexico City","km":15}. Fix: Use {"place":"Mexico City","km":15} with the same text (also in aztec /ledger/1 and /identity/predecessors/0/land).
- TO DO `/ledger/1/region`: The 1337 split region is the state's whole land: {"place":"Mexico City","km":6} and the state's correction {"place":"Mexico City","km":15} resolve to the same single H3 cell. Evidence: gazetteer resolve: both are 1 cell, (-99.14, 19.46). Drawn as written, Tlatelolco's split leaves Tenochtitlan with no land from 1337 to 1428. Fix: Keep the event and say in its note that Tlatelolco is sub-cell (2 km north) and takes no cell; the orchestrator needs a renderer rule (see problems).
- THIN `/identity/rulers`: Acamapichtli, Huitzilihuitl, Chimalpopoca, Itzcoatl (1427) and the domain before 1428 (flagged by the author). Page to try: https://en.wikipedia.org/wiki/Acamapichtli
- Spot checks: `/ledger/0` confirmed (infobox 'Foundation: 1325'; 'the date 13 March 1325 was chosen in 1925'); `/ledger/1` confirmed ('built another city on an island north of Tenochtitlan in 1337'); confidence 3 honest; `/ledger/2` confirmed via the Tepanec_War redirect ('In 1427, Tenochtitlan, Texcoco, Tlacopan, and Huexotzinco went to war against Azcapotzalco, emerging victorious in 1428'); `/ledger/4` confirmed (infobox 'Formation of the Aztec Empire: 1428')
- Area: No infobox area; the city 'covered an estimated 8 to 13.5 km2'; the correction is one cell (about 253 km2), the factor against Cliopatria acknowledged in /keyframe_review/0.

## aztec-triple-alliance: fix

- APPLIED `/ledger/24`: The Soconusco gain was dated 1486 at confidence 2, but no page dates it, and the 1487 keyframe does not hold Soconusco. Evidence: Aztec Empire page: Ahuitzotl 'began a new wave of conquests including the Oaxaca Valley and the Soconusco Coast', no year beyond his 1486 accession; Ahuitzotl page: years only for accession (1486) and death (1502), no Soconusco. Cliopatria adds the Tapachula cells in the 1492 shape. Fix: Year 1492, confidence 1, reviewer note appended.
- APPLIED `/ledger/23/confidence`: The Oaxaca Valley gain is at confidence 2 on Ahuitzotl's accession year, not a conquest year. Evidence: Same pages: no year for the Oaxaca Valley conquest. Fix: Confidence 1, reviewer note appended.
- APPLIED `/ledger/13/region, /ledger/17/region, /wars/3/zones`: The Toluca contest zone (60 km) reached the Mexico City cell, the capital itself. Evidence: See michoacan: 60 km = 40 cells to -99.14 W; 50 km = 27 cells, east edge -99.28. Fix: Radius cut to 50 km.
- APPLIED `/ledger/32/region`: The February 1521 loss of Texcoco used Cliopatria's Texcoco 1428 shape, which lies south of the lake. Evidence: texcoco /keyframe_review/2 marks it misplaced; it resolves to 7 cells at 18.93-19.36 N. Spanish conquest page: 'Texcoco becomes the base of operations for the campaign against Tenochtitlan' (February 1521). Fix: Region now {"minus":[{"place":"Texcoco","km":30},{"place":"Mexico City","km":15}]}, text kept.
- TO DO `/keyframe_review/3..12/correction`: From 1450 the corrected shapes still hold 6 of the 7 cells of cholula.json's own land (901-1521, {"place":"Cholula","km":25}); neither dossier records a conquest, vassalage or alliance. Evidence: gazetteer: intersect(minus(Aztec 1482, Tlaxcala), Cholula 25 km) = 6 cells, about 1,500 km2; cholula.json (am-01) holds them to its 1521 dissolve. The author's notes record that cholula.json exists and that Cholula's status is not on the pages read. Fix: Subtract {"place":"Cholula","km":25,"country":"Mexico"} from the 1450-1519 corrections as for Tlaxcala (Cholula fought the Aztecs in the flower wars with Tlaxcala and Huexotzinco), or add a dated vassal_start from a page and ask am-01 to mirror it.
- TO DO `/ledger/18`: The 1472 gain from michoacan (confidence 3) has no loss in michoacan.json. Evidence: See michoacan finding; michoacan has only a contest_end in 1472. Fix: Agree the counterpart with the michoacan fix (michoacan adds the 1472 loss, or this counterpart becomes the Matlatzinca).
- TO DO `/ledger/1/region, /ledger/2/region, /identity/predecessors/0/land, /identity/predecessors/1/land`: The 1428 merges use the Cliopatria Tenochtitlan and Texcoco shapes that both predecessor dossiers mark misplaced. Evidence: tenochtitlan /keyframe_review/1 and texcoco /keyframe_review/2 replace them with discs. Fix: Use {"place":"Mexico City","km":15} and {"minus":[{"place":"Texcoco","km":30},{"place":"Mexico City","km":15}]}.
- THIN `/ledger/5`: Coyoacan 1429 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Itzcoatl
- THIN `/ledger/10`: Growth of the 1450 shape over Hidalgo and Puebla, undated (confidence 1). Page to try: https://en.wikipedia.org/wiki/Moctezuma_I
- THIN `/ledger/11`: Gulf Coast 1453, undated (confidence 1). Page to try: https://en.wikipedia.org/wiki/Totonac
- THIN `/ledger/12`: Cempoala client status from 1453 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Totonac
- THIN `/ledger/16`: Northern Guerrero (Tlapan) 1459, undated (confidence 1). Page to try: https://en.wikipedia.org/wiki/Moctezuma_I
- THIN `/ledger/20`: Axayacatl's Michoacán frontier towns 1475 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Axayacatl
- THIN `/ledger/22`: Tizoc's 1482 growth (24,300 km2), undated (confidence 1). Page to try: https://en.wikipedia.org/wiki/Tizoc
- THIN `/ledger/23`: Year of the Oaxaca Valley conquest under Ahuitzotl (now confidence 1). Page to try: https://en.wikipedia.org/wiki/Ahuitzotl
- THIN `/ledger/24`: Year of the Soconusco conquest (now 1492, confidence 1). Page to try: https://en.wikipedia.org/wiki/Soconusco
- THIN `/ledger/25`: Guerrero growth 1497, undated (confidence 1). Page to try: https://en.wikipedia.org/wiki/Ahuitzotl
- THIN `/keyframe_review/11`: The 1502 shape adds about 30,900 km2; /ledger/26 (Oaxaca, 1504) explains about 19,700 km2; about 11,000 km2 in Veracruz and Puebla has no event, and the Oaxaca increment shows from 1502 while the event is 1504. Page to try: https://en.wikipedia.org/wiki/Moctezuma_II
- Spot checks: `/ledger/4` confirmed ('The Tepanec lands were carved up among the three cities'); `/ledger/14` confirmed ('In about 1458, Moctezuma led an expedition into Mixtec territory against the city-state of Coixtlahuaca'); `/ledger/15` confirmed ('In the 1450s, Aztec forces under Moctezuma would invade the Valley of Oaxaca'; fitted to the 1459 shape, confidence 2 fair); `/ledger/18` confirmed ('In 1472, Axayacatl re-conquered the region and successfully defended it from Purépecha's attempts to take it back'); confidence 3 honest; `/ledger/24` mis-dated (no year on the Ahuitzotl or Aztec Empire page for Soconusco); fixed to 1492 at confidence 1; `/ledger/29` confirmed ('On 8 November 1519 ... Cortés and his forces entered Tenochtitlan'); `/ledger/30` confirmed (timeline '30 June - La Noche Triste'; narrative '10 July 1520', as the note says); `/ledger/34` confirmed (infobox Spanish conquest 13 August 1521; conquest page 'final victory on 13 August 1521')
- Area: Infobox 220,000 km2 for 1520 against the 1519 shape; quoted in the dossier.

## azcapotzalco: fix

- APPLIED `/ledger/4/region, /ledger/7/region`: The Texcoco contest zone (30 km disc) contained the Mexico City cell. Evidence: As in texcoco. Fix: Replaced by {"minus":[{"place":"Texcoco","km":30},{"place":"Mexico City","km":15}]}, text kept.
- TO DO `/ledger/3/region, /keyframe_review/2/correction`: The 1414 gain of the 'Valley of Mexico' takes Texcoco's whole disc and capital as Azcapotzalco's own land while texcoco.json holds it as its own until the contest starts in 1418: two owners for 11 cells in 1414-1417, with no texcoco event. Evidence: Azcapotzalco page: 'Between 1414-1418, Azcapotzalco controlled the entire Valley of Mexico, thanks to the decisive contribution of Aztec and mercenary forces'; Texcoco page: 'In 1418, Ixtlilxochitl I ... was dethroned'. The gazetteer's Valley of Mexico is the Distrito Federal plus México state (81 cells, about 20,500 km2, the Toluca Valley included). Fix: Start the texcoco-azcapotzalco contest in 1414 in both dossiers, citing the 1414-1418 sentence (the 1418 dethronement stays in the note), or subtract {"minus":[{"place":"Texcoco","km":30},{"place":"Mexico City","km":15}]} from the 1414 region until 1418; counterpart 'Valley of Mexico altepetl' should name texcoco for that part.
- THIN `/ledger/1`: Start of the Mexica tributary status: 1325 is Tenochtitlan's founding (confidence 1). The page has 1318 ('attacked the Aztecs ... resulted in an increased tribute') and, after 1323, 'they were subject to military, economic and strategic decisions of the Tepanecas'; quote them in the note. Page to try: https://en.wikipedia.org/wiki/Tepanecs
- THIN `/ledger/0/region`: Azcapotzalco's own land 995-1384 is {"place":"Mexico City","km":12}, the same single H3 cell as Tenochtitlan (vassal) and Tlatelolco; at resolution 5 they cannot be separated (problems). Page to try: https://en.wikipedia.org/wiki/Azcapotzalco_(altepetl)
- Spot checks: `/ledger/0` confirmed ('Azcapotzalco was founded by Chichimecs in the year 995 AD'); `/ledger/2` confirmed ('Tezozómoc forced the Aztecs to fight with him and together conquered the city of Colhuacan in 1385'; the partner is the Aztecs); `/ledger/3` confirmed ('Between 1414-1418, Azcapotzalco controlled the entire Valley of Mexico'); `/ledger/9` confirmed ('The Tepanec lands were carved up among the three cities'); confidence 3 honest; `/ledger/10` confirmed (infobox 'Incorporated into Aztec Empire: 1428'; 'Together they attacked and sacked Azcapotzalco in 1428')
- Area: No infobox area; not in Cliopatria.

## tlaxcala: thin

- TO DO `/wars/0`: The flower wars run 1454-1519 here and 1450-1519 in aztec-triple-alliance /wars/2. Evidence: Neither page read gives a start year (Moctezuma I page: no start year). Fix: Use one span in both dossiers.
- THIN `/ledger/0`: Founding: the infobox puts '1348' beside the 'Tlaxcaltec migration to Central Mexico' (confidence 1; 2 would be honest for the year). Page to try: https://en.wikipedia.org/wiki/Tlaxcala
- THIN `/ledger/1`: End: infobox 1348-1520; the page gives no incorporation year (the four fiefdoms date from 1545); 1521 is a bridge (confidence 1). Page to try: https://en.wikipedia.org/wiki/Tlaxcala
- THIN `/keyframe_review/0`: Territory: the modern state is an assumption (11 cells, about 2,780 km2); the page says only 'Tlaxcala was completely surrounded by Aztec lands'. Page to try: https://en.wikipedia.org/wiki/Tlaxcala
- Spot checks: `/ledger/0` confirmed (article 'Confederacy of Tlaxcala', infobox '1348-1520', '1348' for the migration); `/ledger/1` confirmed page silent (no end year beyond the infobox's 1520; 'was never conquered by the Aztec Empire'); `/identity/successors/0` confirmed ('On 23 September 1519, Cortés arrived in Tlaxcala and was greeted with joy by the rulers')
- Area: No infobox area; not in Cliopatria; Aztec corrections cut the same admin1 out, consistent.

## tututepec: fix

- TO DO `/keyframe_review/1/correction`: The 89 km disc is said to be 'about 25,000 km2', but Tututepec is on the coast: about half the disc is sea. Evidence: gazetteer: {"lon":-97.62,"lat":16.15,"km":89} (the capital's coordinates; 'Tututepec' does not resolve) = 55 land cells, about 13,900 km2, against the page's 'more than 25,000 km2' (undated) and its possible reach 'as far west as Cahuitan'. Fix: Widen the sphere inland and west along the coast toward Cahuitan (e.g. a union of the disc with a coastal place near the Guerrero border), or correct the area claim in the note to about 13,900 km2.
- TO DO `/keyframe_review/1/correction`: Tilantongo is held from 1098 to 1522 with no page support after Eight Deer, and overlaps the Aztec shape from 1502 (7 cells). Evidence: Tututepec page: 'After Eight Deer conquered Tilantongo he never returned to Tututepec'; no later history of Tilantongo. Aztec Mixteca campaigns: Coixtlahuaca c. 1458 (Moctezuma I page), Achiotlan 1504 (Moctezuma II page, quoted in aztec /ledger/26). Fix: Add a loss of Tilantongo at confidence 1 (Eight Deer's death, or the Aztec Mixteca campaign of 1504 with counterpart aztec-triple-alliance) and end the union there.
- THIN `/keyframe_review/1`: Date of the 25,000 km2 sphere (Late Postclassic, undated on the page). Page to try: https://en.wikipedia.org/wiki/Mixtec
- Spot checks: `/ledger/0` confirmed ('founds Tututepec in 1083'); confidence 3 honest; `/ledger/1` confirmed (Four Jaguar's Toltec delegation in 1097 'aiding him in conquering Tilantongo the next year'); `/ledger/2` confirmed ('in January 1522, arriving in Tututepec in February'); `/ledger/4` confirmed ('conquering it by March 4')
- Area: Body text, undated: 'more than 25,000 km2'; not in Cliopatria; the drawn disc is about 13,900 km2 of land (ratio 0.56), which the note misstates as about 25,000.

## Cross-dossier matrix

- texcoco 1428 merge -> aztec-triple-alliance: matched. 
- tenochtitlan 1428 merge -> aztec-triple-alliance: matched. 
- aztec-triple-alliance 1428 gain -> azcapotzalco: matched. 
- michoacan 1475 loss -> aztec-triple-alliance: matched. both confidence 1, Cliopatria year
- aztec-triple-alliance 1472 gain -> michoacan: mismatch. michoacan has no loss and never gains the Toluca Valley; same author, routed to both
- azcapotzalco 1325 vassal_start -> tenochtitlan: missing. tenochtitlan has no vassal events; same batch
- azcapotzalco 1428 vassal_end -> tenochtitlan: missing. tenochtitlan has no vassal events; same batch
- azcapotzalco 1414 gain -> Valley of Mexico altepetl: mismatch. the region includes texcoco land texcoco holds as its own until 1418
- texcoco 1418 contest_start -> azcapotzalco: matched. contest pair matched (ends 1428 both)
- tenochtitlan 1427 contest_start -> azcapotzalco: matched. contest pair matched (ends 1428 both)
- michoacan 1455 contest_start -> aztec-triple-alliance: matched. ends 1472 both; also 1476-1515 matched
- aztec-triple-alliance 1450 gain -> nobody: mismatch. Aztec corrected shapes from 1450 hold 6 of 7 cells of cholula.json (am-01) own land; no event on either side
- toltec 875 predecessor -> teotihuacan: mismatch. teotihuacan.json ends 750 with no successors; toltec names it as predecessor
- tlaxcala 1454 war -> aztec-triple-alliance: mismatch. flower-war spans differ by four years
- tenochtitlan 1337 split -> Tlatelolco: exception. no dossier; listed by the author
- aztec-triple-alliance 1473 gain -> Tlatelolco: exception. no dossier; listed
- aztec-triple-alliance 1428 merge -> Tlacopan: exception. no dossier; listed
- aztec-triple-alliance 1453 vassal_start -> Cempoala (Totonacs): exception. no dossier; listed (vassal_end 1519 too)
- aztec-triple-alliance 1458 gain -> Coixtlahuaca: exception. listed as Mixteca Alta kingdoms
- aztec-triple-alliance 1459 gain -> Mixtec and Zapotec polities: exception. free text; also 1486 and 1504; Mixteca Alta listed
- tututepec 1098 gain -> Tilantongo: exception. listed as Mixteca Alta kingdoms
- aztec-triple-alliance 1429 gain -> Coyoacan: exception. free-text altepetl, not in the author list; added to counterparts_needing_dossiers here (also Xochimilco 1430, Mixquic 1432, Cuitlahuac 1433, Cuauhnahuac 1439)
- azcapotzalco 1385 gain -> Colhuacan: exception. free-text altepetl, added here
- aztec-triple-alliance 1519 occupation_start -> spanish-empire: exception. am-06 has not run (also occupation_end 1520, contest 1520-1521, losses 1521)
- michoacan 1530 loss -> spanish-empire: exception. am-06 has not run (contest 1522-1530 too)
- tututepec 1522 loss -> spanish-empire: exception. am-06 has not run
- tlaxcala 1521 dissolve -> spanish-empire: exception. am-06 has not run

## Problems

- WebFetch summarises pages; the quotes above are the tool's returned sentences. https://en.wikipedia.org/wiki/Coyotlatelco_culture does not exist (URL_NOT_FOUND).
- Resolution limit: Azcapotzalco ({"place":"Mexico City","km":12}), Tenochtitlan (15 km), Tlatelolco (6 km), Tlacopan (aztec /ledger/3, 12 km) all resolve to the one H3 cell (-99.14, 19.46); the 1337 split takes Tenochtitlan's only cell and Azcapotzalco's own land equals its vassal's. The renderer needs a rule (sub-cell events take no cell; a vassal on its suzerain's cell keeps the suzerain's colour) or the Valley of Mexico states need hand-placed neighbouring cells.
- The gazetteer's 'Valley of Mexico' is the Distrito Federal plus México state (81 cells, about 20,500 km2, the Toluca Valley included), as the am-01 review also found; used by azcapotzalco and aztec /ledger/31.
- Tututepec and Tilantongo do not resolve: the tututepec dossier draws nothing until the gazetteer adds them.
- The aztec capital note quotes 'the other capitals of the Triple Alliance, Tlacopan and Texcoco' from the Spanish conquest page; the tool did not find that phrase (capital note only, not an event).
- Reviewer edits applied and re-validated (0 errors): texcoco (10 regions), azcapotzalco (2), michoacan (5), aztec-triple-alliance (6); each changed note carries '[Reviewer am-03, 2026-10-18: ...]'.

## Gazetteer names needed

Metztitlán, Xochimilco, Mixquic, Cuitlahuac, Cempoala, Coixtlahuaca, Colhuacan, Tututepec, Tilantongo, Azcapotzalco
