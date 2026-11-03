# Notes, group eu-12-e (Iberia and the taifas, part e)

Written 2026-10-25 by the Phase B research agent. Five dossiers: county-of-osona, county-of-ampuria, taifa-of-alpuente, taifa-of-badajoz, taifa-of-denia. All validate with 0 errors. Every claim cites a page opened in this run; Wikipedia pages were read through WebFetch, whose small model sometimes returns paraphrase, so the key sentences were re-fetched verbatim where a note quotes them.

## Cliopatria problems found by the gazetteer (not by the pages)

- taifa-of-alpuente: all five Cliopatria shapes (same bbox) lie about 15 km north of the town of Alpuente and do not contain it. Every correction adds a 25 km district round the town.
- taifa-of-denia: the shapes of 1010, 1015, 1040 and 1066 stop at 0.10 E and miss the town of Dénia (0.11 E). Corrections add a 20 km district.
- taifa-of-badajoz: the 1147-1151 shape (16 cells round Évora-Estremoz-Elvas) does not contain the city of Badajoz, where the page puts the second taifa. Correction adds the city.

## Per state

### county-of-osona (798-1111)
- Start 798 comes from the infobox; Cliopatria starts 990. The page also says Osona 'was considered to be part of the County of Barcelona' in the tenth century. If the Barcelona dossier or the colour agent treats Osona before 990 as Barcelona's, drop the new keyframe county-of-osona_798 and the 827 rename. Cliopatria's Barcelona shapes of 898/950/989 do not overlap Osona.
- Cliopatria has no shape 1028-1039; filled with the 1003 outline (new keyframe _1028).
- Manresa: the western part of the shape comes and goes in Cliopatria (in 990-1002 and 1040-1055, out 1003-1027 and 1056-1098). The page says only that Osona 'was augmented by the addition of the County of Manresa, which was subsumed within Osona', undated and after the 1035-1054 interval. Three confidence-1 events (1003, 1040, 1056) bridge it and may be wrong in direction.
- The Guisla de Lluçà page (https://en.wikipedia.org/wiki/Guisla_de_Llu%C3%A7%C3%A0) did not load; the Vic disambiguation page is empty.
- The page's list gives Ximena 1107-1149, which conflicts with the text; 1111 (infobox) kept.
- Gazetteer: Berguedà (region) is not in it.
- Counterpart without a Cliopatria row: County of Manresa (fix pass: the English County of Manresa page treats it as Osona's western extremity, so no dossier is needed; see the fix section below).

### county-of-ampuria (813-1410)
- Start 813 (infobox 812). 817-989 the page has Empúries 'merged' with Roussillon; Cliopatria's County of Rosellón (896-999) contains all three cells of Empúries, so the dossier models merge (817) and split (989) and draws nothing of its own between. county-of-rosellon should cut the land from 989 (Cliopatria cuts it from 1000).
- End: infobox says annexed to the Principality of Catalonia in 1402; the text says 'escheated to the crown between 1410 and 1436' and lists counts to 1410. 1410 kept (rename at 1402); Cliopatria runs to 1414. No gap-filling needed unless the Catalonia dossier wants 1402.
- No page opened makes Empúries a vassal of Barcelona or Aragon, so no vassal tint is entered; the 1341 apanage is a rename.
- The small shape changes (1028, 1040, 1126, 1169, 1177, 1188, 1236, 1279, 1344) are outline noise of about 100 km2 and carry no events. Cliopatria's Ampuria outline is only three H3 cells (about 760 km2), smaller than the historic comarca of Empordà.
- Capital 1079 (two town pages) against Gausfred I in the late tenth century (Roussillon page).
- The Catalan Wikipedia article (https://ca.wikipedia.org/wiki/Comtat_d%27Empúries) did not load.
- Counterparts: County of Girona (the 785 predecessor; probably Cliopatria's County of Barcelona row, whose Wikipedia title is 'Girona'). County of Peralada (Pedralbes) was struck in the fix pass (the page has Peralada inside Empúries from 813).

### taifa-of-alpuente (1010-1106)
- The article has no territorial history; the ledger is found 1010 and the Almoravid end. End 1106 (taifa article) against 1103 (town page) against Cliopatria 1110.
- No page opened gives vassalage to Valencia, Toledo or Zaragoza, or the frontier with Albarracín.
- Gazetteer: Alpuente (place).

### taifa-of-badajoz (1009-1094, 1144-1150)
- One Cliopatria Name, two lives (1010-1093 and 1147-1151) in one dossier. The 1094-1143 gap is the Almoravid period.
- The page's 1055 sentence puts the land lost 'south of the Mondego River (south of Coimbra)', probably garbled for the land north of it; the 1055 loss region is read from Cliopatria's 1066 shape (confidence 2). Coimbra itself is 1064 (Siege of Coimbra page).
- The tributary relation of 1055 (rule 4) belongs to kingdom-of-leon (vassal_start for taifa-of-badajoz); the page says 'León-Castile', and Cliopatria shows Castile as the neighbour 1046-1065.
- The rulers table is internally inconsistent; identity.rulers omitted.
- The Abbadid (Seville) conquests of Badajoz territory are undated on every page opened; Cliopatria's 1028, 1034, 1040, 1056 changes carry no events.
- Counterpart without a Cliopatria row: Taifa of Lisbon (Banu Sabur), 1022.

### taifa-of-denia (1010-1076, 1224-1227)
- Cliopatria draws Dénia in 1066-1125, 1147-1151 and 1236-1249; the taifa article has no state in those years after 1076 (and before 1224). 1066 is cut at 1076; 1147-1151 and 1236-1249 are verdict 'wrong'. THE LAND OF THOSE TWO SHAPES now has no owner in any dossier of this batch (south-east Murcia and Alicante in 1147-1151; the Dénia-Alicante-Orihuela belt in 1236-1249). The taifa-of-murcia, taifa-of-valencia, crown-of-aragon and crown-of-castile dossiers should claim it, or the map will have holes. The town page has Dénia conquered by the Christians in 1244, the Xàtiva page has Xàtiva taken in 1244, the Kingdom of Valencia page lists Denia among four taifas wiped out by the conquest, and the Almizra page puts the Aragon-Castile line at Biar-Busot-Villajoyosa on 26 March 1244.
- End: 1227 on the taifa article (infobox 'Remnants conquered by Aragon: 1227') against 1244 on the town page. 1227 kept.
- Balearic Islands: autonomy 1050 (Dénia page), independence 1076 (Majorca page); entered as a client tint 1050-1075 then loss to taifa-of-majorca, which has no dossier (Taifa of Majorca 1076-1116 and 1147-1203 needs one).
- After 1076 the land passes to Zaragoza (1076-1081), Tortosa (1081-1092) and the Almoravids (1092-1224) on the infobox; the town page says Zaragoza until the Almoravid invasion of 1091.
- Sardinia 1015-1016 is an occupation (hatched), not territory; the Cliopatria shape that carries Sardinia for 25 years is corrected.
- Gazetteer: Dénia, Xàtiva, Alzira (places).

## Gazetteer names to add
Berguedà (region); Alpuente, Dénia, Xàtiva, Alzira (places). All others resolve.

## Page budget
Osona 5 of 5 (one disambiguation, one failed). Ampuria 8 of 9. Alpuente 7 of 5 and Dénia 9 of 5 (the later Cliopatria rows needed the Majorca, Valencia, Almizra, Dénia-town, Kingdom of Valencia and Xàtiva pages; most pages were shared across states). Badajoz 6 of 5 (the Almoravid page is shared).

## Fix pass 2026-10-25 (author, after review-eu-12-e.md)

Four dossiers failed review (county-of-osona, county-of-ampuria, taifa-of-badajoz, taifa-of-denia); taifa-of-alpuente passed and was not touched. All four were repaired, re-read from the mount, and validate with 0 errors (python3 -I tools/validate_dossier.py --resolve). Each blocking finding was checked against a page opened again with WebFetch before the fix. The reviewer's three in-place fixes (Osona /ledger/0 counterpart nobody; Dénia /ledger/2 and /ledger/11 confidence 2) are kept.

### county-of-osona
- Blocking finding applied. The County of Osona page: 'After the rebellion of 826, during which Guillemó and Aissó succeeded in taking it with help from the Emirate of Córdoba'; 'Osona remained depopulated and outside of Frankish control until 879'; 'In 879, Wilfred the Hairy began the repopulation of the county with free minores'; list: Aissó and Guillemó 826-827, counts of Barcelona 827-939. Added: loss 826 (counterpart 'Aissó and Guillemó (rebels)', confidence 3), gain 879 (nobody, confidence 3), the war 'Revolt of Aissó and Guillemó' 826-827, new keyframe county-of-osona_879 (879-989, same outline as _798), and the 'counts of Barcelona' rename moved from 827 to 879. Nothing is drawn 826-878.
- Small difference from the review: keyframe county-of-osona_798 ends in 825, not 826, so that the loss year (826) is the first year not drawn, as 990 and the Berga loss are (the _798 keyframe ends 989).
- The Aissó page (https://en.wikipedia.org/wiki/Aisso; the title /Aizo is a song) dates the revolt 'in Barcelona, Ausona, and Girona in 826 to 827', Ubayd Allah at Zaragoza in May 827, Girona attacked 10 October 827. It says nothing of how Osona was lost, so the 826 loss rests on the Osona page. No contest events are entered (the land is lost outright).
- Thin item (Manresa 1003, 1040, 1056, confidence 1): https://ca.wikipedia.org/wiki/Comtat_de_Manresa returned url_not_found twice, as did https://ca.wikipedia.org/wiki/Comte_d'Osona. The English https://en.wikipedia.org/wiki/County_of_Manresa loads: it dates no union, says 'The County of Ausona was thus born and to it Wilfred attached the Moianés and Bages', calls Manresa 'the western extremity of the County of Osona, divided into the Moianès and Bages', and says 'it never had a viscount'. So the page does not support a separate county that Osona 'added'; the Cliopatria coming-and-going of the western part stays unexplained, the three events stay at confidence 1, and 'County of Manresa' needs no dossier. Its castle 'dates from the last quarter of the ninth century', so the Manresa end of the 798 outline is probably too early (noted on the _798 keyframe).
- Guisla de Lluçà (1035-1054): still one page only.

### county-of-ampuria
- Blocking finding applied. The page: 'Around 813, Empúries, with Peralada, became a separate county under Ermenguer'; lead 'enclosing the Catalan region of Peralada'; the December 1002 'county of Pedralbes' 'is probably to be identified with the Peralada region in the north of Empúries'. Keyframe county-of-ampuria_1000 is now 'adjust' with the 1003 outline (Empúries with Peralada); the 1003 gain from 'County of Peralada (Pedralbes)' is deleted. Cliopatria's two-cell shape of 1000-1002 is treated as its error.
- 1014-1019 contest zone (events and war): border_band width 2 between county-of-ampuria and county-of-rosellon in 1014 (8 cells in the gazetteer); confidence 2.
- Rulers: the page lists William 848-850 and Odalric 852-858 and says nothing about 850-852; noted on Odalric, gap left open.
- Thin item: the Ramon Berenguer III page (https://en.wikipedia.org/wiki/Ramon_Berenguer_III,_Count_of_Barcelona) does not mention Empúries; it says he 'incorporated into his realm almost all of the Catalan counties (except Urgell and Peralada)'. The 'conquered part of the County of Empúries' sentence of the County of Barcelona page therefore stays undated; no event. The other small shape changes remain outline noise.

### taifa-of-badajoz
- Blocking findings applied. Keyframe taifa-of-badajoz_1056 is 'adjust' with the reviewer's whole shape (the 1056 outline within the 1066 outline, plus a 40 km district round Coimbra); the 1055 loss region is the 1055 shape minus the 1066 shape minus the Coimbra district (113 cells, about 28,600 km2), so Coimbra is lost once, in July 1064.
- Not settled, and where I differ a little from the review's tone: the Ferdinand I of León page (https://en.wikipedia.org/wiki/Ferdinand_I_of_Le%C3%B3n) dates Lamego 29 November 1057, Viseu 25 July 1058 and Coimbra 25 July 1064 (the Siege page says 9 July), and only says 'it is possible that as early as 1055 Ferdinand attacked the taifa of Badajoz'. The 1055 year is the Taifa of Badajoz page's and is kept (confidence 2), but the strip may have gone in 1055-1058; the page's 'south of the Mondego' is still read as the land north of it. The Ferdinand page also reads 'Seville, and probably Badajoz also, paid a ransom' in 1063: no Abbadid conquest of Badajoz land is dated, so Cliopatria's 1018, 1028, 1034, 1040, 1056 changes stay without events.
- Thin item, Lisbon (1022, confidence 1): the Aftasid dynasty page does not mention Lisbon or Sabur's sons, so it stays a bridge.
- Page budget: 5 allowed, now 8 opened (Ferdinand I, Aftasid and a re-read of the main page were named or implied by the review).

### taifa-of-denia
- Blocking finding applied. The page: 'The taifa settled a military camp in the north of the island for one year.' Sardinia occupation is now two pairs of events, counterparts giudicato-of-logudoro (Sardinia within Cliopatria's Logudoro of 1015, 12 cells) and giudicato-of-gallura (2 cells), 1015 to 1016; the war's zone and belligerents and the 1015 keyframe note are corrected (the shape carries the whole island, 83 cells, not 'the north'). The review gave 27 and 14 cells for the judicates; the gazetteer gives 12 and 2 for their 1015 shapes (14 together). eu-13's Logudoro and Gallura dossiers need the mirror events.
- 1015 Balearic gain: counterpart caliphate-of-cordoba, confidence lowered to 2. Neither the Dénia page nor the Taifa of Majorca page says who held the islands before 1015; the evidence is Cliopatria's Caliphate shape (19 Balearic cells in every year 1010-1014, none in 1015). caliphate-of-cordoba needs a 1015 loss to taifa-of-denia.
- 1017-1021 Valencia occupation: region is now Cliopatria's Valencia shape of 1017 within 35 km of Alzira and Xàtiva (the page: 'capture the southern part of that kingdom, which he held for two years', 'In the 1020s'; the rulers list gives 1017-1021, kept). I disagree with the review on one point: Alzira and Xàtiva are not in the gazetteer (neither is Dénia; the resolver says unknown place), so the region gives resolve warnings until the gazetteer agent adds them.
- taifa-of-majorca is listed from 1050 (client of Dénia) in the report.
- Page budget: Dénia pages were re-read (Dénia, Taifa of Majorca); no new page.

### Report
The fixed report is history/notes/phase-b/reports/eu-12-e-fixed.json.
