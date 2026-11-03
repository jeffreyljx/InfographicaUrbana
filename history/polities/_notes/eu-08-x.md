# eu-08-x: notes (additions batch of Holy Roman Empire to 1250)

Written 2026-10-25 by the Phase B agent for batch eu-08-x. 20 new dossiers, all validating (0 errors); 180 events, 62 sources. Cliopatria names reviewed: none (an additions batch owns no Cliopatria row). Every keyframe is new (verdict adjust). All dates and lands come from English Wikipedia pages opened with WebFetch in this run; WebFetch returns a small-model extraction, so quoted sentences are as returned. Where a page was silent the event carries confidence 1 or 2 and says so.

## Where the dossiers sit

- Stem duchies: stem-duchy-of-saxony, stem-duchy-of-bavaria, stem-duchy-of-swabia, stem-duchy-of-franconia, duchy-of-lower-lorraine, duchy-of-zahringen (a ducal title with no stem), duchy-of-carinthia.
- Marches and eastern states: margraviate-of-austria, march-of-verona, march-of-styria, northern-march, margraviate-of-meissen, landgraviate-of-thuringia, lutici (Slavic federation).
- Italy: lombard-league (type umbrella).
- Prince-bishoprics: archbishopric-of-magdeburg, prince-bishopric-of-liege, prince-archbishopric-of-salzburg, prince-bishopric-of-utrecht, prince-archbishopric-of-bremen.

Marches, vassal states and personal unions are drawn as vassal tints (rule 4): Austria and Verona inside Bavaria, Styria inside Carinthia, the Burgundian Rectorate inside Zähringen. Dynasty changes are `rename` events with no land.

## Open points that cross dossiers

- Pages disagree on whether the Styrian march belonged to Bavaria or to Carinthia; Bavaria's shape leaves Styria out and Carinthia and march-of-styria carry it from 976, with Bavaria's 1180 loss as a caption (confidence 2).
- duchy-of-lower-lorraine names a successor land 'Lotharingia minus Lorraine' that would include Alsace (eu-07 Lotharingia); eu-07 should trim it.
- The Duchy of Lower Lorraine page and the Brabant page disagree on the first duke.
- margraviate-of-meissen overlaps Cliopatria's Electorate of Saxony from 1363; eu-09 should trim one of them.
- The Lutici end date is 1157, following the infobox and eu-08-b.
- The page https://en.wikipedia.org/wiki/Duchy_of_Z%C3%A4hringen did not load; House_of_Z%C3%A4hringen and Berthold V were used.
- Three further pages failed to load (Eberhard II of Regensburg, Eberhard II of Salzburg, Sack of Liège); the bishopric titles Archbishopric_of_Salzburg and Bishopric_of_Utrecht are disambiguation pages, so the Prince-Archbishopric and Prince-Bishopric pages were used.
- A footnote on the Prince-Bishopric of Utrecht page lists Bouillon 1096, Loon 1366 and Horne 1568, matching the Liège page; they are used for Liège only.
- The Prince-Archbishopric of Bremen page puts Dithmarschen in its territory 1145-1526, but the Dithmarschen page says the peasants rejected Bremen's overlordship from 1187; it is not drawn.
- WebFetch returns a small-model extraction of each page, so quotes in ledgers are as returned and may not be verbatim.
- The gazetteer lacks many places (Halle, Jüterbog, Bouillon, Berchtesgaden, Stade and others), so coordinate circles are used; see gazetteer_names_needed.
- Salzburg's start (1213 prince; late 13th century immediacy; 1328 infobox) and Magdeburg's start (968 archdiocese; 1180 principality) are the researcher's choices.

## Not written (see gaps in the report)

- margraviate-of-brandenburg: Brandenburg 1157-1259 (Albert the Bear to the Johannine and Ottonian lines) has no dossier (out of scope (slug taken by Cliopatria row 1260-1414)).
- duchy-of-lorraine: Upper Lorraine 959-1431 (the earlier phase of duchy-of-lorraine) (out of scope (slug taken by Cliopatria row 1431-1768)).
- hevelli: Hevelli of Brandenburg an der Havel, 928-1157, only described inside the Lutici dossier (not reached: budget (20 dossiers against a 6-10 target)).
- prince-bishoprics: Cologne, Mainz, Trier before 1250 (eu-09 electorates), Würzburg, Bamberg, Passau, Regensburg, Augsburg, Strasbourg, Constance, Halberstadt, Verden, Paderborn, Münster, Hildesheim (not reached: budget (five prince-bishoprics written: Magdeburg, Liège, Salzburg, Utrecht, Bremen)).
- stem-duchy-of-swabia: The Basel estates of 926 are not drawn (page silent).
- stem-duchy-of-bavaria: The Bavarian ruler strip is omitted (page silent (duke list incomplete)).
- duchy-of-carinthia: Carinthia's border and extent (page silent).
- prince-bishopric-of-liege: The Burgundian period 1468-1477 and the end of Liège's hold on Bouillon (page failed (Sack of Liège) and page silent).
- prince-archbishopric-of-salzburg: Dated acquisitions inside the territory (Friesach, Gastein, the Zillertal), the end of the 1800 occupation and the 1611 Berchtesgaden outcome (page silent).
- archbishopric-of-magdeburg: Temporal lands before 1180 and the 1478 submission of Halle (page silent).

## Pages that failed

- https://en.wikipedia.org/wiki/Duchy_of_Z%C3%A4hringen
- https://en.wikipedia.org/wiki/Eberhard_II_of_Regensburg
- https://en.wikipedia.org/wiki/Eberhard_II_of_Salzburg
- https://en.wikipedia.org/wiki/Sack_of_Li%C3%A8ge

## Per state: what could not be settled

### Stem Duchy of Saxony (stem-duchy-of-saxony, 911-1180)

Pages: Duchy_of_Saxony; Henry_the_Lion; Billung_March; Duchy_of_Westphalia; Niklot.

Five pages opened (budget 2-5). Cliopatria has no Saxony row; the East Franks (850-910) and Kingdom of Germany (911-961) rows draw all Germany as one shape, so the stem duchy is drawn from the gazetteer region 'Old Saxony' (confidence 1; it includes the Rhineland part of North Rhine-Westphalia and Sachsen-Anhalt east of the Saale, both too much) minus the Danish land north of Holstein. Not settled: (a) what Saxony lost in Northalbingia/Wagria in 983 and regained later (Duchy page dates only the rising); (b) the Ascanian rump of 1180 and Bernhard of Anhalt's lands (page silent; region read from 1296); (c) the Northern March and the Billung March after 983 (Brandenburg, Holstein under Adolf of Schauenburg are other states); (d) Henry the Lion's deposition year, 1180 in the infobox against 1181 in the text. The page-fetch tool returns an extraction by a small model, so quoted sentences are as returned. Gazetteer lacks Arnsberg, Lauenburg and Lüneburg (coordinates used). Counterparts needing dossiers: duchy-of-westphalia (Cologne), duchy-of-brunswick-luneburg.

### Stem Duchy of Bavaria (stem-duchy-of-bavaria, 907-1255)

Pages: Duchy_of_Bavaria; Privilegium_Minus; Arnulf,_Duke_of_Bavaria; Duchy_of_Carinthia; Otto_I,_Duke_of_Bavaria; Margraviate_of_Austria.

Six pages opened (budget 2-5; the sixth, Margraviate of Austria, was opened for the Austria dossier and is cited here for the Eastern March). Cliopatria has no stem-duchy row; Cliopatria's Duchy of Bavaria starts 1260 (eu-09). Not settled: (a) Styria 976-1180: the Bavaria and Otto I pages say it was separated from Bavaria in 1180, the Carinthia and March of Styria pages put it under Carinthia from 976, so the shape leaves it out and the 1180 loss is a caption (confidence 2); (b) the extent of the March of Verona (see march-of-verona); (c) the Duchy of Bavaria page gives no area and no complete list of dukes (the extraction gave only appointment years), so no ruler strip is given; (d) 1255-1259 are drawn by no Cliopatria row; (e) Carinthia joined Bavaria in 911 (Bavaria page) or 889 (Carinthia page). The Henry the Lion personal union 1156-1180 is in stem-duchy-of-saxony. The Eastern March (c. 960-1155, margraviate-of-austria), the March of Verona (952-975, march-of-verona) and Carinthia (to 976, duchy-of-carinthia) are separate dossiers written in this batch; Styria, now clarified by the March of Styria page (under Carinthia from 976), is march-of-styria. Counterparts needing dossiers: duchy-of-lower-bavaria. Gazetteer lacks Landshut and Burghausen (coordinates used).

### Stem Duchy of Swabia (stem-duchy-of-swabia, 915-1268)

Pages: Duchy_of_Swabia; Burchard_II,_Duke_of_Swabia; House_of_Z%C3%A4hringen; Conradin; Alsace.

Five pages opened (budget 2-5). No capital is given (infobox lists none), so identity.capitals is empty; no complete list of dukes is on the pages (the extraction gave partial reigns), so no ruler strip. Cliopatria's only Swabian shape is House of Hohenstaufen 1260..1271 (50,823 km2), eu-09's. Not settled: Alsace's entry into Swabia (undated; Lotharingia held it before), Basel 926 (see kingdom-of-germany), when Baden separated, what the Zähringen held in Zürich (advocacy or ownership), and the 1266 pledge of the Swabian inheritance to Ulrich II of Württemberg (Conradin page silent; not drawn). Counterparts needing dossiers: Zähringen duchy (1098-1218, Breisgau, Zürich and the Burgundian rectorate) and Ulrich II of Württemberg's county.

### Stem Duchy of Franconia (stem-duchy-of-franconia, 906-939)

Pages: Duchy_of_Franconia; Eberhard_of_Franconia.

Two pages opened (budget 2). The stem duchy is short and thinly sourced: no capital is given on either page, so identity.capitals is empty; the extent is the Duchy of Franconia page's description turned into gazetteer regions (Franconia region, Hesse, Mainz-Speyer-Worms circles), confidence 1-2. Not drawn: the Salian lands of Rhenish Franconia (Conrad II became Germany's king in 1024; the page says Rhenish Franconia was governed as small states after 1039; Henry of Laach received the Salian territories in Rhenish Franconia as a fief in 1093, the later Electoral Palatinate) and the Bishopric of Würzburg's 'Duchy of Franconia' of 1168. Eberhard was regent of Lotharingia 926-928; that is not a Franconian gain. Gap: whether 939-1039 should be a 'direct imperial possession' shape of its own.

### Margraviate of Austria (margraviate-of-austria, 960-1282)

Pages: Margraviate_of_Austria; Privilegium_Minus; Duchy_of_Austria.

Three pages opened (budget 2-5). The dossier runs from the Eastern March (c. 960) to the Habsburg grant of 1282 so that it covers the years 1251-1282 that Cliopatria draws only from 1279; eu-09 (Habsburg Austria) can chain from its end. Not settled: the start (960 by 'about 960', c. 970 by the infobox, first margrave 970 by the sources) and the earliest border; the Hungarian March and Thaya colonisation (1055-1075, no border given); the date of the growth west of the Enns to Linz (page undated, so Upper Austria is not drawn; Bavaria's keyframe keeps Oberösterreich until 1255); the 1246-1251 interregnum and its claimants; the margraves 976-1141 (the pages give no list, so the ruler strip is partial). The Margraviate is a Bavarian dependency to 1156: the Bavaria dossier draws it as a vassal tint. The Third Crusade, Wiener Neustadt and the Georgenberg Pact (1186) are on the Duchy page without territorial effect.

### Duchy of Carinthia (duchy-of-carinthia, 976-1335)

Pages: Duchy_of_Carinthia; March_of_Verona; March_of_Styria.

Three pages opened (budget 2-5). Cliopatria has no Carinthia row. Not settled: the 976 extent (the page does not map Carinthia; Carniola is read in from the 1040 split), which marches stayed under the duke after 1040, the Carniolan margraves, why the Bavarian pages say Styria was separated from Bavaria in 1180 although the March of Styria page puts it under Carinthia from 976 (the Bavaria dossier leaves Styria out), the Sponheim and later dukes 1122-1335, and Carinthia's southern edge (Friuli, Gorizia). No complete list of dukes is on the page, so no ruler strip. The Verona page's 1061 enfeoffment of Berthold with Carinthia and Verona is not given its own event. Counterparts needing dossiers: march-of-styria, march-of-verona (both in this batch), March of Carniola, March of Istria.

### March of Verona (march-of-verona, 952-1167)

Pages: March_of_Verona; Lombard_League.

Two pages opened (budget 2). Cliopatria has no Verona march; its Kingdom of Italy row draws north Italy. Not settled: the march's real extent (the page lists parts, not a map; Padua, Treviso and Vicenza are read in from the Veronese League; Treviso, Belluno and the rest of the Veneto are not drawn); the exact month of 952; which lord held it 976-1151 beyond 'a Carinthian march'; the Bavarian and Carinthian dossiers draw it as a vassal tint (vassal events counterpart march-of-verona). Counterparts needing dossiers: Bishopric of Trent (1004-1803), March of Istria, patriarchate-of-aquileia (Cliopatria 1260-1449, eu-13/eu-09).

### March of Styria (march-of-styria, 970-1180)

Pages: March_of_Styria.

One page opened (budget 2-5; thin). The March of Styria page has no infobox and no area. The Bavaria pages (Duchy of Bavaria, Otto I of Bavaria) say 'Styria was separated from Bavaria in 1180'; this page puts the march under Carinthia from 976 and gives the Otakars as its margraves with no Bavarian suzerainty, so the Bavaria dossier leaves Styria out of its shape and records 1180 as a caption. Not settled: the exact start (before 970), when the Otakars became effectively independent of Carinthia (the ledger keeps the vassal tint in duchy-of-carinthia until 1180), the eastern border after 1043 (Hungary's side), the capital (Steyr is a guess from 'Margraves of Steyr' 1074 and is not given), and the personal union with Austria after 1192 (duchy-of-styria, eu-09).

### Lutici (lutici, 983-1157)

Pages: Lutici.

One page opened (budget 2-5; the page is long and dated). The Lutici page has no area; the polygon is the researcher's reading of its river description. The end year 1157 follows the infobox's Margraviate of Brandenburg date and eu-08-b's Holy Roman Empire ledger (gain from Lutici 1157); the page itself dates the federation's disintegration 1056/57, Obotrite domination 1093, Lothair's destruction of Radgosc 1126/27 and the partition 'in the first half of the 12th century'. The Hevelli (Brandenburg an der Havel, Havelberg) are an associate tribe, not core, and are drawn only as the 991-993 contest circle; a Hevelli dossier is optional (eu-08-a). Gazetteer lacks Brandenburg an der Havel, Havelberg and Rethra/Radgosc (coordinates used). Whether the Lutici were an empire tributary after 1035 is not drawn (no vassal event in a vassal's own ledger).

### Landgraviate of Thuringia (landgraviate-of-thuringia, 1131-1264)

Pages: Landgraviate_of_Thuringia; War_of_the_Thuringian_Succession.

Two pages opened (budget 2-5). The landgraviate is drawn as modern Thuringia plus a Kassel circle, both low confidence (1-2); the pages do not map it. Not settled: the Landgrave's Hessian holdings (Gudensberg inheritance 1122, Marburg, Kassel), the Palatinate of Saxony and Saalfeld (not on the page), the exact steps of the war (1249 Weißenfels, 1263) which neither page has, and whether Thuringia 1264 is whole or 'the bulk'. The ledger puts both contests under one war entry. Counterparts needing dossiers: landgraviate-of-hesse (eu-09), margraviate-of-meissen (this batch). Gazetteer lacks Eisenach and Wartburg.

### Margraviate of Meissen (margraviate-of-meissen, 965-1423)

Pages: Margraviate_of_Meissen; Landgraviate_of_Thuringia.

Two pages opened (budget 2-5). The Meissen page has no area or capital and no dates for the Milceni's later status or Merseburg and Zeitz after 983; Cliopatria's Electorate of Saxony (1363..) overlaps this dossier's last 60 years (eu-09). Not settled: the true border (all circles), who held Merseburg and Zeitz after 983 (they were recovered, undated), Lusatia (Lower and Upper) beyond the Milceni circle, the Burgraviate of Meissen (1068, 1426 or 1298), the pledge of the Pleissenland, and the Hessian part of the Ludowingian heritage. The Great Slav Rising rebels are not named on the page. Counterparts needing dossiers: March of Gero (Marca Geronis), March of Merseburg and Zeitz, landgraviate-of-hesse (eu-09), duchy-of-bohemia (eu-15). Gazetteer lacks Bautzen, Zeitz, Merseburg and Altenburg (coordinates used).

### Lombard League (lombard-league, 1167-1250)

Pages: Lombard_League.

One page opened (budget 1-2). An umbrella: the dossier carries the association, its dates and wars only; no land should be coloured from it. The page has no infobox and no territory; the whole-region stand-in is coarse (the League's real land was its members' contadi, held by the communes, eu-13). Not settled: whether the League of 1226 was a re-founded second league (the page does not say so); membership by date; the 1183 end of the first league. Gazetteer names used: Lombardia, Veneto, Emilia-Romagna (Natural Earth provinces and regions).

### Duchy of Lower Lorraine (duchy-of-lower-lorraine, 959-1190)

Pages: Duchy_of_Lower_Lorraine; Duchy_of_Brabant.

Two pages opened (budget 2-5). The two pages disagree on the first duke (Godfrey of Mons (Hainaut) on the Lower Lorraine page, Godfrey of Jülich on the Brabant page) and the Lower Lorraine page has no area, capital or dukes before 1012. eu-07's duchy-of-lotharingia dossier gave the successor land as Lotharingia minus Lorraine, which includes Alsace in the gazetteer; this dossier uses Belgium, the Netherlands and circles at Aachen and Cologne instead. Not settled: the Rhineland border (Cologne, Aachen, Jülich, Cleves), Frisia and Utrecht's status, the dukes 959-1012, Hainaut and Namur as counties inside the duchy, the Brabant landgraviate of 1085. wars is empty: no war on the pages moved the border. Counterparts needing dossiers: duchy-of-lorraine (Upper Lorraine before 1431; eu-09 starts at 1431), county-of-flanders (eu-10), Bishopric of Liège. Gazetteer lacks Bouillon and Ghent (coordinates used).

### Northern March (northern-march, 965-1157)

Pages: Northern_March; Albert_the_Bear.

Two pages opened (budget 2-5). The Northern March page has no extent, area or capital; both circles are the researcher's. The page's infobox gives 965-983 as the march itself and treats 983-1157 as a titular and rump period; the dossier keeps the rump to 1157 so that Brandenburg's start is continuous. The 1157 Brandenburg period to 1259 (Cliopatria's Margraviate of Brandenburg begins 1260) has no dossier: eu-09's margraviate-of-brandenburg dossier should start from this one's end and cover Albert's expansion (Havelland, Teltow, Barnim, Uckermark: undated on the Albert page). Not settled: Altmark vs Brandenburg after 983; Hevelli (Pribislav-Henry) as a state; 1114-1130 margrave gap. Counterparts needing dossiers: March of Gero, Hevelli, margraviate-of-brandenburg (eu-09). Gazetteer lacks Stendal, Salzwedel and Brandenburg an der Havel (coordinates used).

### Duchy of Zähringen (duchy-of-zahringen, 1098-1218)

Pages: House_of_Z%C3%A4hringen; Berthold_V,_Duke_of_Z%C3%A4hringen.

Two pages opened (budget 2-5). The Duchy of Zähringen has no article of its own (it redirects to the House); the dossier's Wikipedia title is 'House of Zähringen'. The Zähringer 'duchy' was a title without a territorial duchy (the Breisgau, Ortenau, Zürich and the Burgundian rectorate); the Rectorate lands are a reading and the 1156 cession is as vague as the page. Not settled: Zürich's status (advocacy 1098 vs acquisition 1173 on the same page), the Ortenau and Schaffhausen dates (1198 as a consolidation), and what Berthold IV held in Burgundy before 1186. The 1096 loss in stem-duchy-of-swabia names 'Berthold II of Zähringen' as counterpart. Counterparts needing dossiers: county-of-kyburg, county-of-urach (Fürstenberg), county-of-savoy (Cliopatria from 1260). Gazetteer lacks Offenburg.

### Archbishopric of Magdeburg (archbishopric-of-magdeburg, 1180-1680)

Pages: Archbishopric_of_Magdeburg; Wichmann_von_Seeburg; J%C3%BCterbog; Halle_(Saale).

Four pages opened (budget 2-5). The archdiocese dates from 968 (Synod of Ravenna 967), but the page gives the temporal state only from 1180, so the dossier starts then; earlier temporalities (Halle from the 10th century) are not drawn. The infobox 'Conquered Jüterbog 1157-1180' reads as the conquest of 1157 (Wichmann and Jüterbog pages), and the region is drawn from 1180 only. The page gives no area; the circles around Magdeburg, Jerichow, Halle, Oebisfelde and Jüterbog are the researcher's. Halberstadt, administered by the Magdeburg archbishops from 1480 (page), is not drawn because the page gives no end date or extent and Halberstadt has no dossier. Not settled: the 1478 'Subdued Halle' (infobox only; the Halle page is silent), the Sigismund 1552/1557 succession inconsistency, and the exact extent of the Jerichow Land and Börde.

### Prince-Bishopric of Liège (prince-bishopric-of-liege, 980-1795)

Pages: Prince-Bishopric_of_Li%C3%A8ge; Notker_of_Li%C3%A8ge; County_of_Loon; Duchy_of_Bouillon; Battle_of_Steppes; Li%C3%A8ge_Revolution.

Six pages opened (one over the 2-5 budget, because the state lived 815 years). The pages give no area and no border: the 30 km circle round Liège is the researcher's reading of the core; the final form 'included most of the present Belgian provinces of Liège and Limburg' (main page), and the page does not date the growth of the Liège province part. Not settled: the Burgundian period of 1468-1477 (the page names the pillage of the episcopal city in the 15th century only; the page for the sack failed to load), the Haspinga extent, the date and manner of the end of Liège's hold on Bouillon (1551/1559 against a footnote of 1678), the Bouillon sale year (1095 against 1096), the 1791 return date (12 January against 12 February), and the Horne terms. The Liège page says the diocese was larger than the princedom until 1559; the diocese is not drawn. Needs dossiers or counterpart slugs: County of Loon, County of Moha (small), Duchy of Bouillon (1095-1795).

### Prince-Archbishopric of Salzburg (prince-archbishopric-of-salzburg, 1213-1803)

Pages: Prince-Archbishopric_of_Salzburg; Archbishopric_of_Salzburg; Rupertiwinkel; Wolf_Dietrich_von_Raitenau; Electorate_of_Salzburg.

Five pages opened (one is the disambiguation page; the Eberhard II pages failed to load). The pages disagree on the start: 1213 (Eberhard II made a prince), late 13th century (immediacy) and 1328 (infobox, 'secular jurisdiction between 1328 and 1803'); the dossier starts at 1213, the earliest dated princely act, with confidence 2. The secular territory is drawn as the modern Land of Salzburg because the page calls it 'roughly congruent'; the pages date no acquisition inside it and say nothing of Friesach, Gastein, the Zillertal or other exclaves, so none is drawn. The Rupertiwinkel is drawn from 1275 only because that is the only dated acknowledgement. Not settled: the outcome of the 1611 Berchtesgaden clash, the end of the 1800 occupation, Colloredo's end year (the succession list gives 1772-1812; the text and the Electorate page give 1803).

### Prince-Bishopric of Utrecht (prince-bishopric-of-utrecht, 1024-1528)

Pages: Prince-Bishopric_of_Utrecht; Battle_of_Ane; Bishopric_of_Utrecht; County_of_Zutphen.

Four pages opened. The pages give no area or border: the Nedersticht is drawn as the modern province of Utrecht, Overijssel and Drenthe as modern provinces, and 'part of Groningen' as a circle. Not settled: when the Oversticht came to the bishops (1024 on the main page, 'mid-11th century' on the Battle of Ane page), who held Groningen after 1141, the County of Zutphen (a fief of the bishop, 'Utrecht included County of Zutphen (until 1182)' in a footnote; the Zutphen page gives no grant date, so it is not drawn), the 1512 against 1548 Burgundian Circle entry, and the end year of Henry of the Palatinate (1528 against 1529). A footnote on the main page also lists the Duchy of Bouillon in 1096, the county of Loon in 1366 and the county of Horne in 1568; these match the Liège page and are not Utrecht events, so they are not used. The Guelders Wars have infobox dates only.

### Prince-Archbishopric of Bremen (prince-archbishopric-of-bremen, 1180-1648)

Pages: Prince-Archbishopric_of_Bremen; Stedingers; Dithmarschen; Land_Wursten.

Four pages opened. The page gives no area or border: the circle between the Weser and the Elbe (45 km round Vörde, with Stade inside it) is the researcher's reading of 'about a third of the diocesan territory'; Land Hadeln (a Saxe-Lauenburg exclave in 1567) falls inside it and is not subtracted. Disagreements between pages: the Bremen infobox puts Dithmarschen in the territory 1145-1526, the Dithmarschen page says it was ceded after 1180 and rejected Bremen's overlordship, so it is not drawn; the seat moves to Vörde in 1219 (seats paragraph) or 1313 (narrative); Tilly's conquest is 1627 or 1628; the Swedish seizure is 1645 (infobox) or 1643-1645. Not settled: who held Stedingen after 1234, the location of Bederkesa, Verden's relation (a separate prince-bishopric, 1631 conquest), and the border of the diocesan territory. Needs dossiers: Duchy of Bremen (1648-1823), Land Wursten (small), Prince-Bishopric of Verden.


## Repair of the review failures (2026-10-25, author of eu-08-x)

Seven dossiers failed the adversarial review (review-eu-08-x.md, notes/phase-b/reviews/eu-08-x.json): stem-duchy-of-saxony, stem-duchy-of-bavaria, stem-duchy-of-swabia, margraviate-of-austria, march-of-verona, march-of-styria, duchy-of-lower-lorraine. All seven were repaired, re-validate with 0 errors (python3 -I tools/validate_dossier.py --resolve) and carry a "Repair of 2026-10-25" paragraph in their own notes. The other thirteen dossiers (pass, fix or thin) were not touched, so mirror edits that belong on their side are listed at the end. Pages were re-opened with WebFetch for every date, region or source finding; WebFetch returns a small-model extraction, so quotes are as returned. Every page below loaded.

### What changed, per dossier

- stem-duchy-of-saxony (keyframes 3 -> 4, events 13 -> 16, sources 5 -> 8): Aachen and Cologne 45 km circles removed from every shape and region; the Altmark leaves in 965 as a loss to northern-march (Duchy of Saxony page: after 965 Otto I entrusted the defence of the 'northeastern Saxon regions', 'later known as Altmark', to Count Thiadricus), so keyframes are 911-964, 965-1159, 1160-1166, 1167-1179; Mecklenburg is cut at the Peene by a polygon (Usedom, Anklam and the Uecker valley out); magdeburg and bremen added as successors with 1180 losses; the 1167 vassal pair and the 1180 end now name lordship-of-mecklenburg; the Ascanian rump of 1180 is confidence 2 now (see disagreements). Pages added: Northern_March, Saxe-Wittenberg, Pribislav_of_Mecklenburg.
- stem-duchy-of-bavaria (keyframes 3 -> 4, events 20 -> 22, sources 6 -> 9): Bavaria is Bayern minus Franconia (the Nordgau polygon kept) and minus a polygon west of the Lech, in every shape and region; 1213 loss of Salzburg to prince-archbishopric-of-salzburg with the 976 keyframe split at 1213; the 1180 loss of Styria is dropped and folded into the 1180 Wittelsbach rename as a caption; vassal pair 970-976 with march-of-styria added; the 960 vassal tint is the Enns-Wienerwald strip and the 1156 end is the whole march. Pages added: Prince-Archbishopric_of_Salzburg, March_of_Styria, Prince-Bishopric_of_Brixen.
- stem-duchy-of-swabia (keyframes 2 -> 4, events 9 -> 12): the dossier ends in 1260 (dissolve there, successor house-of-hohenstaufen) instead of 1268; losses of Zürich (1173), Schaffhausen and the Ortenau (1198) to duchy-of-zahringen with new keyframes; the 1096 loss keeps its year with the 1098 settlement noted; the gazetteer 'Swabia' (Baden-Württemberg plus an 80 km circle at Augsburg) is replaced by Baden-Württemberg plus Bayern west of the same Lech polygon Bavaria subtracts (the circle reached Munich and still overlapped Bavaria by 36 cells after Bavaria's fix); the Conradin war (1267-1268) is removed from wars[] because it lies outside the life and belongs to house-of-hohenstaufen (details are in the dossier's notes).
- margraviate-of-austria (keyframes 1 -> 3, events 9 -> 15, sources 3 -> 6): vassal_start 960 and vassal_end 1156 (month 9) with stem-duchy-of-bavaria, recorded from the vassal's side (counterpart = the overlord); the first shape is the Enns-Wienerwald strip, then a 1043 gain of the Vienna basin, Marchfeld and southern Weinviertel (confidence 1) and a 1055 gain of the northern Waldviertel and Weinviertel (colonisation to the Thaya, 1055-1075); vassal_end 1246 for duchy-of-styria; Klosterneuburg added between Melk and Vienna. Pages added: Adalbert,_Margrave_of_Austria, Duchy_of_Styria, Leopold_III,_Margrave_of_Austria.
- march-of-verona (events 6 -> 10): vassal_start/vassal_end pairs for Bavaria (952-976) and Carinthia (976-1151), from the vassal's side; successor changed from the umbrella lombard-league to holy-roman-empire (the Cliopatria shape draws north Italy; kingdom-of-italy has no Cliopatria shape between 970 and 1861), with the League in the note.
- march-of-styria (events 5 -> 9, sources 1 -> 2): vassal pairs for Bavaria (970-976) and Carinthia (976-1180) from the vassal's side. Page added: Duchy_of_Styria.
- duchy-of-lower-lorraine (keyframes 5 -> 7, events 10 -> 12, sources 2 -> 4): shape is Belgium minus Crown Flanders (West Flanders and East Flanders west of the Scheldt) plus Luxembourg, the Netherlands and the Aachen and Cologne circles; losses of Liège (980) and Utrecht (1024) with new keyframes; the 1033 gain and 1044 loss name duchy-of-upper-lorraine; Brabant and Holland successors carry a routing note. Pages added: Prince-Bishopric_of_Li%C3%A8ge, Prince-Bishopric_of_Utrecht.

### Where I disagree or the page does not carry the fix (page named)

- Altmark and Saxony: the Northern_March page is silent on whether the margraves answered to the Saxon duke or to the king, so I used the review's second option (a 965 loss) at confidence 2 on the Duchy_of_Saxony sentence, not a vassal tint (which would assert an overlordship no page states).
- Ascanian rump (thin finding): Saxe-Wittenberg says Bernhard of Ballenstedt 'only ruled over small, mostly Eastphalian fringes of the old duchy' and names Lauenburg and Wittenberg only in the 1212 division; the Duchy_of_Saxony page says the Ascanians held 'only the easternmost, comparably small, territories along the river Elbe around Lauenburg upon Elbe and around Wittenberg upon Elbe'. The two pages disagree; I kept the Wittenberg and Lauenburg circles at confidence 2 on the Duchy page. Nothing on either page makes Ballenstedt a region I could draw.
- Pribislav (thin finding): Pribislav_of_Mecklenburg says 'Henry restored Pribislav to power in 1167 as the Prince of Mecklenburg, Kessin, and Rostock' (it does not call him a vassal; the Niklot page does) and is silent on his status after 1180; the 1180 end of the Saxon overlordship stays a bridge (confidence 1).
- Mecklenburg and the Peene: neither Niklot nor Pribislav names a place relative to the river, so the cut east of the Peene is a polygon (lower Peene and Peenestrom, 13.70 E and east of it) that is the researcher's geography; Rügen and the Müritz country stay inside the gazetteer's Mecklenburg and are soft.
- Salzburg 1213: Prince-Archbishopric_of_Salzburg dates the princely title to 1213 but says the archbishops 'gradually reached the status of Imperial immediacy and independence from the Bavarian dukes' from the late 13th century and is silent on Bavaria and on 1275; Duchy_of_Bavaria has the Bavarian duke's domination recognised in 1275. The 1213 loss follows the princely title and the Salzburg dossier's own founding year; it is soft (confidence 2). It is a choice, not something the page states.
- Styria in Bavaria: Duchy_of_Bavaria says Styria was separated 'when it was raised to the Duchy of Styria in 1180'; March_of_Styria puts it under Carinthia from 976. I followed March_of_Styria and kept the 1180 line as a caption in the Wittelsbach rename, as the review allowed; the March of Styria page does not say the duchy was released from Bavaria.
- Traungau, Trent, Brixen (thin findings): the Prince-Bishopric_of_Brixen page gives immediacy for Brixen in 1027 and the Puster Valley in 1091 but is silent on Trent and on any detachment from Bavaria; neither March_of_Styria nor Duchy_of_Styria names the Traungau, Steyr or the Pitten inheritance of 1158. Tirol and Oberösterreich therefore stay Bavarian and none of these is drawn.
- Austria 1043: no page dates the March/Morava and Leitha frontier (Adalbert, margrave 1018-1055, 'extended the border as far as the rivers Morava/March and Leitha'). 1043 is a bridge from the March of Styria page's 1042/43 conquest to the Leitha (confidence 1). The Margraviate page also says the Hungarian March was merged into Austria under Ernest the Brave (1055-1075), with no border; I did not give it a separate event.
- Klosterneuburg: neither the Margraviate page ('until 1145') nor the Leopold III page dates the move; 1108 is the foundation of the monastery, used as the earliest dated trace (confidence 1).
- Verona's successor: the review suggested kingdom-of-italy or the commune; kingdom-of-italy (eu-13) has no Cliopatria shape between 970 and 1861 and no dossier yet, so holy-roman-empire holds the land. The March_of_Verona page lists the Patria del Friuli and the Lombard League as successor entities, and only nominal imperial vicars and later the Scaliger as lords.
- Swabia's end: Duchy_of_Swabia puts the abeyance in 1268 and is silent on 1260; the 1260 end is only a hand-over to the Cliopatria House of Hohenstaufen row (eu-09), so that 1260-1268 is drawn once. If the orchestrator would rather keep 1268, trim the Hohenstaufen row instead.
- Swabia 1096 and 1098: Duchy_of_Swabia ('ceded the Breisgau in 1096') and House_of_Zähringen ('In 1098, he reconciled') each give their own year; the cession stays at 1096, so the Breisgau is undrawn 1096-1097.
- Zürich, Schaffhausen, Ortenau: House_of_Zähringen gives 'Zürich (acquired 1173)' and 'Schaffhausen (acquired 1198)' and is silent on the Ortenau in 1198 and on whether Zürich was ever Swabian; Duchy_of_Swabia is silent on all three and says only that Philip bought support with 'large cessions of Swabian lands' in 1198. The Ortenau loss is confidence 1.
- Lower Lorraine: Duchy_of_Lower_Lorraine is silent on the Scheldt, on Aachen and on any French-held Flanders, and lists Liège and Utrecht among fiefs that came to imperial immediacy without a date; the Liège page (secular powers 980) and the Utrecht page (princes 1024) give the dates, and neither mentions the duke. The cut along the Scheldt is the researcher's polygon, based on the Duchy_of_Brabant sentence 'Imperial lands up to the Schelde river in the west came under the rule of the French Counts Baldwin V of Flanders by 1059'. The Tournaisis and Zeeuws-Vlaanderen are not cut.

### Open overlaps this repair did not resolve

- march-of-styria's 1042 circle (16.0 E 47.7 N, 45 km) covers about 15 of the 78 cells of Lower Austria that margraviate-of-austria also draws (Pitten, Wiener Neustadt, the southern Vienna basin); the review did not flag it and the circle is coarse.
- The gazetteer's Franconia circles (Nuremberg 90 km) still overlap the Bavarian Nordgau by about 30 cells in 907-938 and the Württemberg-Franken part of Baden-Württemberg by about 26 cells in 915-939 (stem-duchy-of-franconia passed review and was not touched).
- The Allgäu west of the Lech is now Swabian in Swabia's shape; the Franconian lands after 939 and the Altmark after 1157 are drawn by nobody in this batch.

### Mirror edits needed in dossiers I did not touch

- northern-march: found 965 names 'March of Gero'; a loss mirror from stem-duchy-of-saxony (Altmark circle 11.9 E 52.6 N, 55 km) is now on the Saxon side.
- prince-bishopric-of-liege (found 980) and prince-bishopric-of-utrecht (found 1024) name holy-roman-empire and should name duchy-of-lower-lorraine; Liège and Utrecht's regions are the ones the losses copy.
- duchy-of-zahringen: the 1173 gain names 'Counts of Lenzburg' and the 1198 gain holy-roman-empire; both should also name stem-duchy-of-swabia (the Swabian losses copy its Zürich, Schaffhausen and Ortenau regions); found 1098 versus the 1096 cession.
- duchy-of-carinthia: vassal_end 1151 (march-of-verona) still carries the 976 extent with Trentino, Friuli and Istria.
- prince-archbishopric-of-salzburg (found 1213, counterpart stem-duchy-of-bavaria) already matches the new Bavarian loss; its 1275 gain names duchy-of-bavaria, which has no 1275 loss.
- house-of-ascania, duchy-of-bavaria, county-of-brabant and county-of-holland (eu-09, eu-10) must start earlier than 1260 (1180, 1255, 1190, 1190); obotrites (eu-07) must run to 1167 with a lordship-of-mecklenburg dossier; patriarchate-of-aquileia (eu-13) must start in 1077; a duchy-of-upper-lorraine dossier is needed; house-of-hohenstaufen should take the Conradin war (1267-1268) and carry the duchy to 1268 or lose it to Swabia.
