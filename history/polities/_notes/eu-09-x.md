# Notes, group eu-09-x (additions batch, written 2026-10-25, Phase B research agent)

Dossiers written (88, all state Cliopatria lacks, cliopatria_names []): electoral-palatinate, duchy-of-wurttemberg, landgraviate-of-hesse, landgraviate-of-hesse-kassel, landgraviate-of-hesse-darmstadt, habsburg-netherlands, electorate-of-cologne, electorate-of-mainz, prince-bishopric-of-munster, county-of-tyrol, duchy-of-brunswick-luneburg, margraviate-of-baden, prince-bishopric-of-wurzburg, prince-bishopric-of-bamberg, duchy-of-julich-berg, duchy-of-cleves, duchy-of-guelders, county-of-hainaut, duchy-of-pomerania, county-of-oldenburg, prince-bishopric-of-hildesheim, prince-bishopric-of-osnabruck, prince-bishopric-of-paderborn, principality-of-ansbach, principality-of-bayreuth, county-of-east-frisia, mecklenburg, united-belgian-states, palatinate-neuburg, landgraviate-of-hesse-marburg, landgraviate-of-hesse-rheinfels, county-of-hanau, county-of-katzenelnbogen, county-of-schaumburg, swabian-circle, franconian-circle, further-austria, prince-bishopric-of-augsburg, prince-bishopric-of-constance, prince-bishopric-of-strasbourg, prince-bishopric-of-eichstatt, prince-bishopric-of-halberstadt, prince-abbey-of-fulda, prince-bishopric-of-trent, prince-bishopric-of-brixen, prince-bishopric-of-passau, prince-bishopric-of-speyer, prince-bishopric-of-verden, prince-bishopric-of-minden, county-of-nassau, principality-of-anhalt, county-of-lippe, duchy-of-berg, county-of-mark, county-of-ravensberg, burgraviate-of-nuremberg, free-imperial-city-of-nuremberg, free-imperial-city-of-ulm, free-imperial-city-of-cologne, county-of-henneberg, county-of-waldeck, county-of-mansfeld, county-of-hoya, county-of-diepholz, prince-bishopric-of-freising, prince-bishopric-of-worms, prince-bishopric-of-lubeck, county-of-schwerin, principality-of-rugen, duchy-of-saxe-lauenburg, county-of-oettingen, prince-provostry-of-berchtesgaden, princely-abbey-of-corvey, quedlinburg-abbey, principality-of-hohenzollern-hechingen, duchy-of-schleswig, county-of-zutphen, county-of-montbeliard, principality-of-nassau-orange-fulda, duchy-of-saxe-weimar, duchy-of-saxe-gotha-altenburg, duchy-of-saxe-coburg-saalfeld, duchy-of-saxe-weissenfels, duchy-of-saxe-merseburg, duchy-of-saxe-zeitz, duchy-of-arenberg, county-of-wied, county-of-stolberg. All validate with 0 errors; 585 ledger events, 179 page sources in total. Page budget: states are checked against 2-5 pages each, Habsburg Netherlands 14. Every dated quote in a ledger note is the page's own words as the WebFetch extract returned them.

Pages that failed: https://en.wikipedia.org/wiki/Treaty_of_Kaaden, https://en.wikipedia.org/wiki/Duchy_of_Mecklenburg-G%C3%BCstrow, https://en.wikipedia.org/wiki/Palatinate-Zweibr%C3%BCcken, https://en.wikipedia.org/wiki/Duchy_of_Zweibr%C3%BCcken, https://en.wikipedia.org/wiki/Duchy_of_Palatinate-Zweibr%C3%BCcken.

Gaps and problems:
- Habsburg Netherlands is one state with renames in 1549 (Seventeen Provinces), 1556 (Spanish Netherlands) and 1714 (Austrian Netherlands); Franche-Comte is excluded and flagged as a counterpart. The dossier used 14 pages, which is the top of the budget.
- Several counterpart slugs used in ledgers have no dossier yet (validator warns 'looks like a slug but no dossier'): see counterparts_needing_dossiers. These are warnings, not errors.
- Pre-1250 spans for the Palatinate, Wurttemberg, Cologne and Mainz are thin: the pages opened gave few dated events before 1250.
- Shapes are radius readings (place and lon/lat circles), soft, because the gazetteer lacks most historical towns; each dossier's notes lists the circles used.
- Slug duchy-of-mecklenburg is taken by eu-20 (Cliopatria 1806-1870), so the earlier Mecklenburg and Pomerania are not mine; Cliopatria's pomerania row covers only 1139-1187.
- Brunswick-Lüneburg and Baden are each drawn as one state with their cadet lines (Calenberg, Lüneburg, Wolfenbüttel; Baden-Baden and Baden-Durlach) kept inside, as the pages do; the electorate-of-hanover dossier (other group) names principality-of-calenberg and principality-of-luneburg as predecessors, so the orchestrator should pick one structure.
- County of Tyrol ends 1363 (to house-of-habsburg, whose Cliopatria row takes Tyrol that year); the Bavarian row of duchy-of-bavaria (eu-09-a) also holds Tyrol 1352-1362, so one of the two dossiers should drop it.
- Prince-Bishoprics of Würzburg and Bamberg: the pages give dates but almost no territory (Würzburg: no area at all), so the shapes are stand-in circles at the capital; the Bamberg one is calibrated to the page's 3,580 km2.
- electorate-of-brandenburg's 1614 gain names the counterpart `julich-cleves-berg`; this batch writes duchy-of-julich-berg (loses Ravensberg 1614) and duchy-of-cleves (dissolves into electorate-of-brandenburg 1614), so the orchestrator should map `julich-cleves-berg` to those two (the United Duchies of 1521 are a personal union, not a territory).
- duchy-of-pomerania (1188-1637) continues the Cliopatria row `pomerania` (1139-1187, eu-15-e): same state, so the orchestrator may merge them into one dossier. Its first keyframes take Schlawe-Stolp and the Uckermark out of Cliopatria's 1187 outline (the page dates Schlawe-Stolp to 1317).
- Osnabrück and Paderborn pages are thin (no area, no districts, almost no territorial events); the dossiers carry start, end and one stand-in circle each, so the colour agent has a state but the reviewer should read them as page-limited, not unfinished.
- mecklenburg (1170-1805) is the Lordship/Duchy before Cliopatria's Duchy of Mecklenburg row (1806-1870, slug duchy-of-mecklenburg taken by eu-20): same state, merge advised. The Mecklenburg pages gave no area, so the outline under-draws the south.
- Hesse-Marburg and Hesse-Rheinfels got the slugs landgraviate-of-hesse-marburg and landgraviate-of-hesse-rheinfels; the counterpart strings `hesse-marburg` and `hesse-rheinfels` in landgraviate-of-hesse, -kassel and -darmstadt were changed to match. The pages' other periods (Hesse-Marburg 1458-1500 and Hesse-Rotenburg-Rheinfels to 1834) are not dossiers.
- duchy-of-brunswick-luneburg's 1370-1388 Luneburg war counterpart was changed from `duchy-of-saxe-wittenberg` to `electorate-of-saxony`: the electorate-of-saxony dossier of another part starts in 1356 from the Ascanian Saxe-Wittenberg, so no separate Saxe-Wittenberg dossier is written.
- county-of-schaumburg: the page's 1640 three-way partition (Hesse-Cassel's eastern part, Schaumburg-Lippe the largest, a part to Lüneburg) conflicts with landgraviate-of-hesse-kassel's 1648 gain of 'most of the County of Schaumburg' (a different page); neither locates the shares, so both are stand-ins on the same Rinteln circle and the orchestrator should settle them when a Schaumburg-Lippe dossier is written.
- swabian-circle and franconian-circle are written as type umbrella (rule 4: associations are never territory) because the brief's scope names them; the shapes are coarse stand-ins (Baden-Wurttemberg + Augsburg less Franconia; the gazetteer's Franconia region) for the reviewer, and the other eight Imperial Circles are not written.
- The en.wikipedia article for Palatinate-Zweibrücken could not be fetched under three titles (Palatinate-Zweibrücken, Duchy_of_Zweibrücken, Duchy_of_Palatinate-Zweibrücken: url_not_found), so no dossier is written for it; the lines Palatinate-Zweibrücken, -Veldenz, -Simmern, -Birkenfeld remain counterparts.
- Free imperial cities: only Nuremberg, Ulm and Cologne are written (types state); the city articles for Augsburg and Cologne do not describe the city-state, so Augsburg (1276-1803) is not written and Cologne rests on the city article's few dated sentences. Frankfurt, Hamburg, Bremen and Lübeck have Cliopatria rows from 1806 or later in other parts and their pre-1806 phase is left to those parts.
- Date conflicts between sibling dossiers, each left as its own page gives it: Schwerin ends 1368 (Treaty of Pluschow; county-of-schwerin) but Mecklenburg dates the acquisition 1358; Diepholz ends 1585 (county-of-diepholz) but Brunswick-Luneburg dates the gain 1584; the Palatinate-Neuburg and Julich-Berg pairs are noted in their own notes.
- county-of-oldenburg was edited after publication to add the 1803 gain of the Principality of Lubeck (Eutin) from the Prince-Bishopric of Lubeck page (its source list and notes updated; revalidated, 0 errors).
- duchy-of-saxe-lauenburg covers the first existence only (1296-1803, the page's lead); the restored duchy of 1814-1876 is not entered.
- Montbeliard (county-of-montbeliard) is ended at 1444 although its page runs the county to 1793: the Wurttemberg dossier draws Montbeliard inside Wurttemberg from 1444 to 1793, and a second shape would double-draw the land. Zutphen (county-of-zutphen) is likewise ended at 1138 (page: personal union with Guelders) while the Guelders dossier draws the land from 1127. The later phases are in notes.
- Holstein and Schleswig: only the Duchy of Schleswig is written. The Duchy of Holstein is a Cliopatria row (1848-52) owned by eu-20, so its pre-1848 life (county 1111-1474, duchy 1474-1866) is not covered by this batch; the Holstein page was opened and is cited by the Schleswig dossier only.
- Hohenzollern: only the Principality of Hohenzollern-Hechingen (1576-1850) is written; the Swabian County of Hohenzollern before 1576 is not, because the page opened for it is the dynasty's article.
- Saxon duchies: Cliopatria's Saxe-Weimar-Eisenach (1806-70), Saxe-Altenburg (1806-70), Saxe-Meiningen (1820-70) and Saxe-Coburg and Gotha (1836-39) rows start after the pre-1806 duchies; duchy-of-saxe-gotha-altenburg and duchy-of-saxe-coburg-saalfeld run to 1826 (the pages' end) and overlap those rows for 1806-26, and Cliopatria leaves 1826-36 empty. duchy-of-saxe-weimar is ended at 1805 (the page says merged 1809) to meet Cliopatria's row, as the Mecklenburg dossier does.

Unwritten states: imperial-circles (The other eight Imperial Circles (Bavarian, Austrian, Burgundian, Electoral Rhenish, Upper Rhenish, Lower Rhenish-Westphalian, Upper Saxon, Lower Saxon) not written; Swabian and Franconian are written as type umbrella: rule 4: associations of estates, never territory; the two named in the brief's scope are done, the rest not reached: context); free-imperial-cities (Other free imperial cities (Augsburg, Frankfurt, Regensburg, Strasbourg, Aachen, Hamburg, Bremen, Lubeck and about forty more) not written; Nuremberg, Ulm and Cologne are written: not reached: context; the Augsburg article is the modern city; Hamburg, Bremen, Lubeck and Frankfurt have Cliopatria rows from 1806-1820 in other parts); saxon-duchies (Saxe-Eisenach (1596-1809, intermittent), Saxe-Altenburg (1603-72), Saxe-Jena, Saxe-Meiningen, Saxe-Hildburghausen, Saxe-Romhild, Saxe-Eisenberg and Saxe-Coburg (1572-1699) not written; Weimar, Gotha-Altenburg, Coburg-Saalfeld, Weissenfels, Merseburg and Zeitz are written: Saxe-Eisenach existed at three separate times and Weimar/Gotha dossiers carry its lands in the gaps; the others not reached: context)

Counterparts needing dossiers (years are rough hints, not read from an opened page): Palatinate-Zweibrücken [palatinate-zweibrucken]; Swabian League [swabian-league]; Abbey of Hersfeld [abbey-of-hersfeld]; Franche-Comté (Habsburg period) [franche-comte]; Lordship of Groningen [lordship-of-groningen]; Albertine Saxony [albertine-saxony]; County of Arnsberg [county-of-arnsberg]; City of Mainz [city-of-mainz]; City of Erfurt [city-of-erfurt]; Principality of Aschaffenburg [principality-of-aschaffenburg]; County of Vechta [county-of-vechta]; Anabaptist Kingdom of Münster [anabaptist-kingdom-of-munster]; Lordship of Ahaus [lordship-of-ahaus]; County of Gorizia [county-of-gorizia]; Principality of Lüneburg [principality-of-luneburg]; Principality of Brunswick-Wolfenbüttel [principality-of-brunswick-wolfenbuttel]; Principality of Grubenhagen [principality-of-grubenhagen]; Lordship of Lahr-Mahlberg [lordship-of-lahr-mahlberg]; County of Eberstein [county-of-eberstein]; Electorate of Baden [electorate-of-baden]; Grand Duchy of Würzburg [grand-duchy-of-wurzburg]; United Duchies of Jülich-Cleves-Berg (umbrella) [julich-cleves-berg]; Lordship of Varel [lordship-of-varel]; County of Delmenhorst [county-of-delmenhorst]; Lordship of Jever [lordship-of-jever]; Lordship of Harlingerland (Esens, Stedesdorf, Wittmund) [lordship-of-harlingerland]; Lordship of Rostock [lordship-of-rostock]; Lordship of Stargard [lordship-of-stargard]; Palatinate-Sulzbach (Sulzbach line, separated 1614) [palatinate-sulzbach]; Barony of Lichtenberg (Lower Alsace, half inherited 1480) [barony-of-lichtenberg]; County of Schaumburg-Lippe [county-of-schaumburg-lippe]; Duchy of Modena (Ercole III d'Este, Breisgau 1801-1803) [duchy-of-modena]; County of Schwalenberg [county-of-schwalenberg]; County of Tecklenburg [county-of-tecklenburg]; County of Sternberg (Lippe) [county-of-sternberg]; County of Pyrmont [county-of-pyrmont]; Duchy of Saxe-Eisenach [duchy-of-saxe-eisenach]; Duchy of Saxe-Altenburg (1603-1672) [duchy-of-saxe-altenburg]; Duchy of Saxe-Meiningen (pre-1806) [duchy-of-saxe-meiningen]; County of Hohnstein [county-of-hohnstein]

Gazetteer names wanted: Upper Palatinate (electoral-palatinate); Amberg (electoral-palatinate); Neuburg an der Donau (electoral-palatinate); Lower Palatinate (electoral-palatinate); Bergstrasse (electoral-palatinate); Montbéliard (duchy-of-wurttemberg); Tübingen (duchy-of-wurttemberg); Bad Urach (duchy-of-wurttemberg); Marburg (landgraviate-of-hesse); Katzenelnbogen (landgraviate-of-hesse); St. Goar (landgraviate-of-hesse); Biedenkopf (landgraviate-of-hesse); Rinteln (landgraviate-of-hesse-kassel); Hanau (landgraviate-of-hesse-kassel); Bad Hersfeld (landgraviate-of-hesse-kassel); Darmstadt (landgraviate-of-hesse-darmstadt); Heppenheim (landgraviate-of-hesse-darmstadt); Buchsweiler (landgraviate-of-hesse-darmstadt); Arnsberg (landgraviate-of-hesse-darmstadt); Duchy of Westphalia (landgraviate-of-hesse-darmstadt); Ypres (habsburg-netherlands); Breda (habsburg-netherlands); Lier (habsburg-netherlands); Amersfoort (habsburg-netherlands); Menen (habsburg-netherlands); Dendermonde (habsburg-netherlands); Courtrai (habsburg-netherlands); Oudenaarde (habsburg-netherlands); Tournai (habsburg-netherlands); Veurne (habsburg-netherlands); Charleroi (habsburg-netherlands); Ath (habsburg-netherlands); Douai (habsburg-netherlands); Armentières (habsburg-netherlands); Bergues (habsburg-netherlands); Valenciennes (habsburg-netherlands); Cambrai (habsburg-netherlands); Maubeuge (habsburg-netherlands); Saint-Omer (habsburg-netherlands); Aire-sur-la-Lys (habsburg-netherlands); Cassel (habsburg-netherlands); Montmédy (habsburg-netherlands); Dunkirk (habsburg-netherlands); Diksmuide (habsburg-netherlands); Leuven (habsburg-netherlands); Maastricht (habsburg-netherlands); Venlo (habsburg-netherlands); Roermond (habsburg-netherlands); 's-Hertogenbosch (habsburg-netherlands); Hulst (habsburg-netherlands); Mechelen (habsburg-netherlands); Lille (habsburg-netherlands); Soest (electorate-of-cologne); Neuss (electorate-of-cologne); Vest Recklinghausen (electorate-of-cologne); Aschaffenburg (electorate-of-mainz); Eichsfeld (electorate-of-mainz); Erfurt (electorate-of-mainz); Rheingau (electorate-of-mainz); Meppen (prince-bishopric-of-munster); Vechta (prince-bishopric-of-munster); Cloppenburg (prince-bishopric-of-munster); Ahaus (prince-bishopric-of-munster); Wildeshausen (prince-bishopric-of-munster); Meran (county-of-tyrol); Lienz (county-of-tyrol); Brixen (county-of-tyrol); Salorno (county-of-tyrol); Braunschweig (duchy-of-brunswick-luneburg); Lüneburg (duchy-of-brunswick-luneburg); Celle (duchy-of-brunswick-luneburg); Einbeck (duchy-of-brunswick-luneburg); Nienburg (duchy-of-brunswick-luneburg); Diepholz (duchy-of-brunswick-luneburg); Hameln (duchy-of-brunswick-luneburg); Bodenwerder (duchy-of-brunswick-luneburg); Hildesheim (duchy-of-brunswick-luneburg); Göttingen (duchy-of-brunswick-luneburg); Baden-Baden (margraviate-of-baden); Rastatt (margraviate-of-baden); Pforzheim (margraviate-of-baden); Durlach (margraviate-of-baden); Emmendingen (margraviate-of-baden); Lörrach (margraviate-of-baden); Lahr (margraviate-of-baden); Offenburg (margraviate-of-baden); Villach (prince-bishopric-of-bamberg); Feldkirchen (prince-bishopric-of-bamberg); Wolfsberg (prince-bishopric-of-bamberg); Tarvis (prince-bishopric-of-bamberg); Kirchdorf an der Krems (prince-bishopric-of-bamberg); Jülich (duchy-of-julich-berg); Düren (duchy-of-julich-berg); Bielefeld (duchy-of-julich-berg); Berg (duchy-of-julich-berg); Cleves (duchy-of-cleves); Wesel (duchy-of-cleves); Hamm (duchy-of-cleves); Zutphen (duchy-of-guelders); Roermond (duchy-of-guelders); Venlo (duchy-of-guelders); Nijmegen (duchy-of-guelders); Veluwe (duchy-of-guelders); Betuwe (duchy-of-guelders); Valenciennes (county-of-hainaut); Avesnes-sur-Helpe (county-of-hainaut); Mons (county-of-hainaut); Stolp (duchy-of-pomerania); Prenzlau (duchy-of-pomerania); Rügen (duchy-of-pomerania); Lauenburg (duchy-of-pomerania); Bütow (duchy-of-pomerania); Oldenburg (county-of-oldenburg); Varel (county-of-oldenburg); Delmenhorst (county-of-oldenburg); Hildesheim (prince-bishopric-of-hildesheim); Peine (prince-bishopric-of-hildesheim); Hameln (prince-bishopric-of-hildesheim); Ansbach (principality-of-ansbach); Bayreuth (principality-of-bayreuth); Kulmbach (principality-of-bayreuth); Aurich (county-of-east-frisia); Emden (county-of-east-frisia); Jever (county-of-east-frisia); Esens (county-of-east-frisia); Leer (county-of-east-frisia); Schwerin (mecklenburg); Wismar (mecklenburg); Rostock (mecklenburg); Neubrandenburg (mecklenburg); Güstrow (mecklenburg); Neuburg an der Donau (palatinate-neuburg); Sulzbach (palatinate-neuburg); Hilpoltstein (palatinate-neuburg); Marburg (landgraviate-of-hesse-marburg); Nidda (landgraviate-of-hesse-marburg); Eppstein (landgraviate-of-hesse-marburg); Biedenkopf (landgraviate-of-hesse-marburg); St. Goar (landgraviate-of-hesse-rheinfels); Braubach (landgraviate-of-hesse-rheinfels); Rheinfels (landgraviate-of-hesse-rheinfels); Hanau (county-of-hanau); Babenhausen (county-of-hanau); Buchsweiler (county-of-hanau); Katzenelnbogen (county-of-katzenelnbogen); Rüsselsheim (county-of-katzenelnbogen); Darmstadt (county-of-katzenelnbogen); Rinteln (county-of-schaumburg); Stadthagen (county-of-schaumburg); Schaumburg (county-of-schaumburg); Ensisheim (further-austria); Breisgau (further-austria); Sundgau (further-austria); Tettnang (further-austria); Fricktal (further-austria); Dillingen an der Donau (prince-bishopric-of-augsburg); Füssen (prince-bishopric-of-augsburg); Meersburg (prince-bishopric-of-constance); Reichenau (prince-bishopric-of-constance); Saverne (prince-bishopric-of-strasbourg); Molsheim (prince-bishopric-of-strasbourg); Benfeld (prince-bishopric-of-strasbourg); Rouffach (prince-bishopric-of-strasbourg); Oberkirch (prince-bishopric-of-strasbourg); Ettenheim (prince-bishopric-of-strasbourg); Oppenau (prince-bishopric-of-strasbourg); Eichstätt (prince-bishopric-of-eichstatt); Hirschberg (prince-bishopric-of-eichstatt); Halberstadt (prince-bishopric-of-halberstadt); Aschersleben (prince-bishopric-of-halberstadt); Hornburg (prince-bishopric-of-halberstadt); Osterwieck (prince-bishopric-of-halberstadt); Brixen (prince-bishopric-of-brixen); Bruneck (prince-bishopric-of-brixen); Klausen (prince-bishopric-of-brixen); Passau (prince-bishopric-of-passau); Bruchsal (prince-bishopric-of-speyer); Philippsburg (prince-bishopric-of-speyer); Deidesheim (prince-bishopric-of-speyer); Herxheim (prince-bishopric-of-speyer); Lauterburg (prince-bishopric-of-speyer); Verden (prince-bishopric-of-verden); Rotenburg (Wümme) (prince-bishopric-of-verden); Minden (prince-bishopric-of-minden); Lübbecke (prince-bishopric-of-minden); Hameln (prince-bishopric-of-minden); Nassau (county-of-nassau); Weilburg (county-of-nassau); Idstein (county-of-nassau); Wiesbaden (county-of-nassau); Dillenburg (county-of-nassau); Siegen (county-of-nassau); Herborn (county-of-nassau); Haiger (county-of-nassau); Dessau (principality-of-anhalt); Bernburg (principality-of-anhalt); Köthen (principality-of-anhalt); Zerbst (principality-of-anhalt); Plötzkau (principality-of-anhalt); Aschersleben (principality-of-anhalt); Detmold (county-of-lippe); Lemgo (county-of-lippe); Lippstadt (county-of-lippe); Blomberg (county-of-lippe); Horn (county-of-lippe); Rheda (county-of-lippe); Schwalenberg (county-of-lippe); Düsseldorf (duchy-of-berg); Solingen (duchy-of-berg); Wipperfürth (duchy-of-berg); Burg an der Wupper (duchy-of-berg); Hamm (county-of-mark); Altena (county-of-mark); Unna (county-of-mark); Iserlohn (county-of-mark); Bielefeld (county-of-ravensberg); Herford (county-of-ravensberg); Vlotho (county-of-ravensberg); Halle (Westf.) (county-of-ravensberg); Borgholzhausen (county-of-ravensberg); Nuremberg (burgraviate-of-nuremberg); Lauf (free-imperial-city-of-nuremberg); Hersbruck (free-imperial-city-of-nuremberg); Altdorf (free-imperial-city-of-nuremberg); Wöhrd (free-imperial-city-of-nuremberg); Deutz (free-imperial-city-of-cologne); Schleusingen (county-of-henneberg); Meiningen (county-of-henneberg); Suhl (county-of-henneberg); Schmalkalden (county-of-henneberg); Römhild (county-of-henneberg); Coburg (county-of-henneberg); Ilmenau (county-of-henneberg); Korbach (county-of-waldeck); Arolsen (county-of-waldeck); Bad Wildungen (county-of-waldeck); Pyrmont (county-of-waldeck); Mansfeld (county-of-mansfeld); Eisleben (county-of-mansfeld); Heldrungen (county-of-mansfeld); Allstedt (county-of-mansfeld); Artern (county-of-mansfeld); Hoya (county-of-hoya); Nienburg (Weser) (county-of-hoya); Diepholz (county-of-diepholz); Barnstorf (county-of-diepholz); Goldenstedt (county-of-diepholz); Drebber (county-of-diepholz); Lemförde (county-of-diepholz); Colnrade (county-of-diepholz); Auburg (county-of-diepholz); Freising (prince-bishopric-of-freising); Garmisch-Partenkirchen (prince-bishopric-of-freising); Innichen (prince-bishopric-of-freising); Škofja Loka (prince-bishopric-of-freising); Oberwölz (prince-bishopric-of-freising); Ladenburg (prince-bishopric-of-worms); Eutin (prince-bishopric-of-lubeck); Bergen auf Rügen (principality-of-rugen); Garz (principality-of-rugen); Loitz (principality-of-rugen); Wolgast (principality-of-rugen); Sławno (principality-of-rugen); Ratzeburg (duchy-of-saxe-lauenburg); Lauenburg/Elbe (duchy-of-saxe-lauenburg); Neuhaus (Elbe) (duchy-of-saxe-lauenburg); Otterndorf (duchy-of-saxe-lauenburg); Bergedorf (duchy-of-saxe-lauenburg); Geesthacht (duchy-of-saxe-lauenburg); Steinhorst (duchy-of-saxe-lauenburg); Oettingen in Bayern (county-of-oettingen); Nördlingen (county-of-oettingen); Wallerstein (county-of-oettingen); Harburg (Schwaben) (county-of-oettingen); Spielberg (county-of-oettingen); Berchtesgaden (prince-provostry-of-berchtesgaden); Höxter (princely-abbey-of-corvey); Corvey (princely-abbey-of-corvey); Duderstadt (quedlinburg-abbey); Hechingen (principality-of-hohenzollern-hechingen); Zutphen (county-of-zutphen); Montbéliard (county-of-montbeliard); Weingarten (principality-of-nassau-orange-fulda); Dietkirchen (principality-of-nassau-orange-fulda); Weimar (duchy-of-saxe-weimar); Altenburg (duchy-of-saxe-weimar); Gotha (duchy-of-saxe-weimar); Eisenach (duchy-of-saxe-weimar); Jena (duchy-of-saxe-weimar); Saalfeld (duchy-of-saxe-gotha-altenburg); Coburg (duchy-of-saxe-gotha-altenburg); Eisenberg (Thüringen) (duchy-of-saxe-gotha-altenburg); St. Wendel (duchy-of-saxe-coburg-saalfeld); Weissenfels (duchy-of-saxe-weissenfels); Querfurt (duchy-of-saxe-weissenfels); Jüterbog (duchy-of-saxe-weissenfels); Dahme/Mark (duchy-of-saxe-weissenfels); Burg bei Magdeburg (duchy-of-saxe-weissenfels); Barby (duchy-of-saxe-weissenfels); Merseburg (duchy-of-saxe-merseburg); Lübben (duchy-of-saxe-merseburg); Zeitz (duchy-of-saxe-zeitz); Naumburg (Saale) (duchy-of-saxe-zeitz); Haynsburg (duchy-of-saxe-zeitz); Schleusingen (duchy-of-saxe-zeitz); Suhl (duchy-of-saxe-zeitz); Aremberg (duchy-of-arenberg); Recklinghausen (duchy-of-arenberg); Meppen (duchy-of-arenberg); Dülmen (duchy-of-arenberg); Neuwied (county-of-wied); Dierdorf (county-of-wied); Runkel (county-of-wied); Stolberg (Harz) (county-of-stolberg); Kelbra (county-of-stolberg); Heringen (Helme) (county-of-stolberg); Wernigerode (county-of-stolberg); Königstein im Taunus (county-of-stolberg); Rochefort (county-of-stolberg)

## electoral-palatinate (Electoral Palatinate, 1085-1777)
Written 2026-10-25 for batch eu-09-x (7 pages opened). New state: Cliopatria has no Palatinate row; its lands sit inside 'Holy Roman Empire Minor States' (1260..1806) and, from 1777, Bavaria.

SCOPE CHOICE. The dossier starts at 1085 (the page's 'From about 1085/86') and ends 30 December 1777, the infobox 'Subsumed by Bavaria'. The electorate lived on as a separate member of the Empire in personal union with Bavaria until 1803 (left bank annexed by France 1795, Lunéville 9 February 1801, right bank to Baden 27 April 1803); those steps are left to the Bavarian dossier because Cliopatria and the sibling HRE-minor-states ledger already give the Palatinate to Bavaria from 1777.

SHAPES ARE RADIUS READINGS. The gazetteer has no 'Upper Palatinate' or 'Amberg'; the Bergstrasse is a 20 km circle at 8.62E 49.66N, the Upper Palatinate is a 70 km circle at 11.86E 49.44N and the Neuburg lands a 35 km circle at 11.18E 48.73N. Gazetteer names wanted: 'Upper Palatinate' (region, Oberpfalz, centred on Amberg), 'Lower Palatinate' (region), 'Neuburg an der Donau' (place), 'Amberg' (place). The Lower Palatinate is the Rhineland-Palatinate region within 75 km of Mannheim plus a 35 km circle at Heidelberg (about 11,000 km2), a stand-in: the real electorate was scattered and the left bank included Kaiserslautern, Alzey and Neustadt (the page names only Alzey).

NOT SETTLED. (1) The early-16th-century cadet principalities Simmern, Kaiserslautern, Zweibrucken (Lower Palatinate) and Neuburg, Sulzbach (Upper Palatinate) are named on the page; Palatinate-Zweibrucken and Palatinate-Simmern are separate states that need dossiers (they held land for centuries) and are not subtracted from the keyframes. (2) Jülich-Berg, held by the Neuburg line from 1653, is a personal union drawn nowhere here; it needs its own dossier. (3) The Landshut War of 1503-1505 (Palatine losses and the creation of Neuburg) and the Palatine Neumarkt line were not on the pages opened. (4) The 1329 Pavia sentence says 'returned the Palatinate to his nephews': the pages do not say when Louis IV had taken it, so the 1294 Nordgau acquisition is recorded in a note only. (5) Heidelberg is the infobox capital 1085-1690, but the text dates the move from Stahleck to about 1182, hence the Stahleck span at confidence 1. (6) Rulers: the page lists only the first (Henry of Laach, 1085-1095) and the last elector (Maximilian Joseph, 1799-1803); a ruler list was not opened, so none is given.

COUNTERPARTS FOR OTHER GROUPS: palatinate-neuburg, duchy-of-palatinate-zweibrucken, julich-berg (the 1777 hand-over of Jülich and Berg to Bavaria is in the eu-09-c ledger), kingdom-of-spain (the Spanish Netherlands army that occupied the west 1621-1652).

## duchy-of-wurttemberg (Duchy of Württemberg, 1081-1803)
Written 2026-10-25 for batch eu-09-x (7 pages opened). New state: Cliopatria has no pre-1803 Württemberg row (its lands are in 'Holy Roman Empire Minor States'); the 1803..1805 Electorate of Württemberg row belongs to eu-20.

ONE STATE, TWO NAMES. The county (1081-1495) and the duchy (1495-1803) are one state with a rename event (rule 2). The dossier ends in February 1803 where Cliopatria's electorate starts.

SHAPES ARE RADIUS READINGS. No page gives the county's or the duchy's boundary. The 52 km circle round Stuttgart (8,850 km2) is checked against the Duchy page's 'over 8,000 square kilometres' (ratio 1.1); the 40 km and 18 km circles for the county are guesses at soft edges. Montbéliard is a 20 km circle at 6.80E 47.51N. Gazetteer names wanted: 'Montbéliard' (place), 'Tübingen' (place), 'Bad Urach' (place), 'Wirtemberg' (castle).

NOT SETTLED. (1) 1397 (betrothal, County page) against 1407 (marriage, Montbéliard page): the 1444 passage is the only dated step used. (2) Montbéliard was a cadet appanage from 1617 to 1723; drawn as Württemberg throughout. (3) Austrian suzerainty over Württemberg from the Treaty of Kaaden (June 1534): the pages opened do not say when it ended, so no vassal_start/vassal_end is recorded; the Treaty of Kaaden page did not load (WebFetch url_not_found for https://en.wikipedia.org/wiki/Treaty_of_Kaaden), so the terms come from the Ulrich page and a gap-filler should find the right title. (4) The Imperial occupation of 1634-1648 is dated only at its start; the end is confidence 1. (5) Other acquisitions (Böblingen, Urach, Tübingen, Heidenheim, the Black Forest) were not on the pages. (6) Rulers: the Duchy page gives only Eberhard I (1495-1496) and Frederick III (1797-1803) and calls the first duke Eberhard I in the infobox, Eberhard V in the text; a list of dukes of Württemberg was not opened, so none is given. (7) The Peace of Westphalia and the Peace of Prague (May 1635) change no Württemberg land on the pages opened.

COUNTERPARTS FOR OTHER GROUPS: county-of-montbeliard (Montbéliard, a Württemberg possession 1444-1793), margraviate-of-baden (the 1251 Stuttgart marriage and the neighbour to the west), swabian-league (the 1519-1520 buyer), electorate-of-wurttemberg (eu-20).

## landgraviate-of-hesse (Landgraviate of Hesse, 1264-1567)
Written 2026-10-25 for batch eu-09-x (3 pages opened; page budget 2-5). New state: Cliopatria lacks Hesse before 1803 (its lands are in 'Holy Roman Empire Minor States').

SHAPES ARE RADIUS READINGS: Kassel 55 km, Marburg (8.77E 50.81N) 40 km, Giessen 40 km, Darmstadt (8.65E 49.87N) 30 km, St. Goar/Rheinfels (7.71E 50.15N) 14 km. Gazetteer names wanted: 'Marburg', 'Darmstadt', 'St. Goar', 'Katzenelnbogen' (places).

NOT SETTLED. (1) The page gives no area and no year for the end of the Thuringian war (the 1264 date is the infobox's). (2) 1292 (prince status), the Reformation (1526 Synod of Homberg) and Philip's reign are not territorial. (3) The Schmalkaldic War and Philip's capture in 1547 are not on the page. (4) The lower county of Katzenelnbogen is not said to pass to Hesse in 1479 on the Katzenelnbogen page; the keyframe includes it because Hesse-Rheinfels existed in 1567. (5) Nassau-Siegen disputed the inheritance 1500-1557 (Katzenelnbogen page). (6) Rulers: only Henry I and Philip I are given by the page.

COUNTERPARTS NEEDING DOSSIERS: landgraviate-of-hesse-marburg (1567-1604), landgraviate-of-hesse-rheinfels (1567-1583), county-of-katzenelnbogen (1095/1138-1479), plus Hesse-Kassel and Hesse-Darmstadt, written in this batch.

## landgraviate-of-hesse-kassel (Landgraviate of Hesse-Kassel, 1567-1803)
Written 2026-10-25 for batch eu-09-x (4 pages opened for this dossier, with the Landgraviate of Hesse page shared with the sibling dossier). New state: Cliopatria's 'Electorate of Hesse' starts only in 1803.

SHAPES ARE RADIUS READINGS: Kassel 44 km (matching the footnote's 6,100 km2), Marburg 30 km, Rinteln 22 km for Schaumburg, Bad Hersfeld 18 km for the abbey, Hanau 22 km, St. Goar 14 km for the Rheinfels share. Gazetteer names wanted: 'Marburg', 'Hanau', 'Rinteln', 'Bad Hersfeld', 'St. Goar'.

NOT SETTLED. (1) The Imperial invasion of Hesse-Kassel in the Thirty Years' War is undated on the page. (2) The Treaty of Westphalia's Hersfeld clause is undated on the page (placed in 1648). (3) The page does not name the land ceded in 1627 or 1801; Marburg and the Rheinfels lands are readings. (4) Cadet lines (Hesse-Rotenburg, Philippsthal, Barchfeld) and the 1736 Hanau-Münzenberg inheritance details are not on the Kassel page; the Hanau page supplied 1736. (5) Rulers not given: the page lists only William IV by name; no ruler list was opened. (6) The 1801 land ceded and the French 1806-1813 Kingdom of Westphalia belong to the electorate dossier (eu-20).

COUNTERPARTS NEEDING DOSSIERS: landgraviate-of-hesse-rheinfels, landgraviate-of-hesse-marburg, county-of-schaumburg (1110-1640, partitioned 1647-1648), county-of-hanau (1429-1736), abbey-of-hersfeld.

## landgraviate-of-hesse-darmstadt (Landgraviate of Hesse-Darmstadt, 1567-1806)
Written 2026-10-25 for batch eu-09-x (4 pages opened for this dossier; the Hanau-Lichtenberg page is new here). New state: Cliopatria's 'Grand Duchy of Hesse' starts only in 1806.

SHAPES ARE RADIUS READINGS: Darmstadt 30 km, Giessen 30 km, Biedenkopf (8.53E 50.91N) 15 km, Marburg 30 km, Buchsweiler/Bouxwiller (7.48E 48.82N) 25 km, Arnsberg (8.06E 51.40N) 40 km for the Duchy of Westphalia, Heppenheim (8.65E 49.64N) 25 km for the Mainz and Worms lands. Gazetteer names wanted: 'Darmstadt', 'Biedenkopf', 'Arnsberg', 'Heppenheim', 'Buchsweiler' (Bouxwiller), 'Duchy of Westphalia' (region).

NOT SETTLED. (1) Hanau-Lichtenberg (the Hessian Alsace) was under French sovereignty from 1680; whether it should be drawn as Darmstadt land, a French vassal or neither is open. (2) The 1622 Homburg and 1627 Rotenburg secessions are on the page without saying from which house; not recorded. (3) The 1803 gain from Mainz and Worms has no named places on the page. (4) The Westphalia hand-over is placed in 1803 by the page; the year of the Duchy's transfer to Hesse-Darmstadt within 1803 is not stated. (5) Rheinhessen and the Worms right bank are not on the Darmstadt page (the mediatisation page gives 'Worms: right bank'). (6) 1704-1713 and the French occupations of the Rhineland are not on the pages opened.

COUNTERPARTS NEEDING DOSSIERS: county-of-hanau-lichtenberg (Hanau-Lichtenberg, 1456/80-1736), landgraviate-of-hesse-marburg, county-of-hanau.

## habsburg-netherlands (Habsburg Netherlands, 1482-1795)
Written 2026-10-25 for batch eu-09-x (13 pages opened for this dossier, over the nominal budget of 9 because the dossier spans 313 years and about 17 shape changes; the Nine Years' War page is the Palatinate dossier's). New state: Cliopatria has no Habsburg Netherlands row.

ONE STATE, THREE NAMES. Habsburg Netherlands (1482-1556), Spanish Netherlands (1556-1714) and Austrian Netherlands (1714-1795) are one state on the same land with two rename events (rule 2); the three Wikipedia articles are the sources. The Dutch Republic (eu-09-j) and Union of Utrecht dossiers already name 'habsburg-netherlands' as counterpart; the 1579-1590 and 1590-1645 events here are their mirror images.

SHAPES ARE MODERN-UNIT READINGS: Belgium minus Liège province, Luxembourg, Nord (French Flanders and Hainaut), the Artois region, Dutch provinces; circles for towns. Areas: 77,000 km2 (1543-1578) against 70,000 (1560, Spanish Netherlands infobox), 53,000 km2 plus the Meuse towns (1585-1628) against 46,000 (1600). Gazetteer names wanted (places, all drawn as lon/lat circles): Ypres (Ieper), Breda, Lier, Amersfoort, Menen, Dendermonde, Courtrai (Kortrijk), Oudenaarde, Tournai, Veurne, Charleroi, Ath, Douai, Armentières, Bergues, Valenciennes, Cambrai, Maubeuge, Saint-Omer, Aire-sur-la-Lys, Cassel, Montmédy, Dunkirk (Dunkerque), Diksmuide, Leuven, Maastricht, Venlo, Roermond, 's-Hertogenbosch, Hulst, Mechelen, Lille.

NOT SETTLED. (1) Franche-Comté (Free County of Burgundy), ceded at Arras in 1482, returned at Senlis in 1493, French in 1674-1678, was ruled by the same Habsburgs but is not drawn here; it needs a dossier of its own (the eu-09-g free-county-of-burgundy dossier ends in 1384). (2) The Prince-Bishopric of Liège, Stavelot-Malmedy and Cambrai (as ecclesiastical lands) are not part of the shape; Liège is its own dossier. (3) Tournai (1521 acquisition from France) and the 1501-1559 Habsburg expansion beyond what the infobox dates are not on the pages. (4) The pages do not trace Ypres, Tournai, Oudenaarde and Veurne after 1678; the 1697 event assumes they returned (confidence 2). The 1713 loss of Spanish Guelders (Venlo, Echt to the Republic, Geldern to Prussia) is in the Dutch dossier, not on a page opened here; the 1637 Spanish retaking of Venlo and Roermond likewise. (5) The Reunions page reports only the surrender of Luxembourg city (3 June 1684); the whole duchy is drawn lost (confidence 2). (6) Exact dates: the Union's June 1579 joins and the Treaty of Aix's 1668 towns use the pages' dates; the 1677 conquests have no month. (7) The Eighty Years' War page's own start date was not extracted.

COUNTERPARTS NEEDING DOSSIERS: united-belgian-states (January-December 1790), franche-comte (Habsburg Franche-Comté 1493-1678), duchy-of-guelders, lordship-of-groningen, albertine-saxony (Duke George of Saxony, seller of Friesland in 1524).

## electorate-of-cologne (Electorate of Cologne, 953-1803)
Written 2026-10-25 for batch eu-09-x (6 pages opened; the mediatisation page is shared with other dossiers). New state: Cliopatria has no Cologne row.

SCOPE. The dossier starts at 953 (the page's first secular power) and ends in February 1803. Pre-1250 events beyond 953 and 1180 were not on the pages.

SHAPES ARE RADIUS READINGS: Bonn 28 km (Oberstift), Neuss 30 km (Niederstift), Cologne 12 km, northern Westphalia (7.95E 51.55N) 25 km, southern Sauerland (8.35E 51.15N) 28 km, Arnsberg 20 km, Soest 15 km. Gazetteer names wanted: 'Soest', 'Arnsberg', 'Neuss', 'Duchy of Westphalia' (region), 'Vest Recklinghausen' (region).

NOT SETTLED. (1) The page gives no area. (2) Vest Recklinghausen (named at 1803) and the Rhine strip of Brühl, Zons and Kempen are not drawn separately. (3) Free Imperial City status of Cologne in 1475 is the page's date; the 1288 independence is the one used. (4) The Cologne War's first campaign date (autumn 1583) is not on the page; Bonn changed hands in 1587 and 1588. (5) Capital 1288-1596 is an inference (confidence 1). (6) The Cologne infobox's 'technically from 1238 and permanently from 1263 until 1803' sentence is undated for territory and not used. (7) No ruler list was opened. (8) Left-bank loss: the Cologne page says only 'occupied by France' after 1795; Lunéville (1801) is the researcher's date for the formal loss (confidence 2).

COUNTERPARTS NEEDING DOSSIERS: free-imperial-city-of-cologne (1288/1475-1794), county-of-arnsberg (Werl-Arnsberg), duchy-of-cleves (Cleves-Mark, Soest 1444), gebhard-truchsess's-faction (not a state), duchy-of-arenberg (Vest Recklinghausen 1803), stem-duchy-of-saxony (exists).

## electorate-of-mainz (Electorate of Mainz, 780-1803)
Written 2026-10-25 for batch eu-09-x (6 pages opened; the mediatisation page is shared). New state: Cliopatria has no Mainz row.

SCOPE AND SHAPES. The dossier runs from 780 (the page's 'Gained territory, elevated to archbishopric: 780') to 1803. Shapes are radius readings: Mainz 30 km, Aschaffenburg (9.15E 49.98N) 25 km, Eichsfeld (10.20E 51.42N) 35 km, Erfurt (11.03E 50.98N) 25 km, Bergstrasse (8.62E 49.66N) 20 km, Rheingau 15 km. The page gives no area. Gazetteer names wanted: 'Aschaffenburg', 'Eichsfeld' (region), 'Erfurt' (place), 'Bergstrasse' (region), 'Rheingau' (region).

NOT SETTLED. (1) The acquisition dates of Aschaffenburg and the Bergstrasse are not on the pages (confidence 1 with the 1022 Eichsfeld event); the Eichsfeld page's 1342-1434 Untereichsfeld passage is not clearly Mainz. (2) The Mainz page says only that the left bank went to France; 1801 (Lunéville) is the mediatisation page's treaty date. (3) The 1797 Campo Formio is in the Mainz infobox without a territorial clause. (4) The 1803 split of the right bank between Hesse-Darmstadt, Nassau and Dalberg is not detailed on the page. (5) The Siege of Mainz (April-July 1793) has no dates on the page. (6) No ruler list was opened; Diether of Isenburg and Adolf of Nassau (1461-1475) are named by the Feud page only. (7) Mainz was an archbishopric of great extent in the Middle Ages (Thuringia, Hesse) that the dossier does not describe.

COUNTERPARTS NEEDING DOSSIERS: city-of-mainz (Free City 1242-1462), city-of-erfurt, principality-of-aschaffenburg (Dalberg 1803-1810), kingdom-of-the-franks (exists in eu-07?).

## prince-bishopric-of-munster (Prince-Bishopric of Münster, 1180-1803)
Written 2026-10-25 for batch eu-09-x (4 pages opened; budget 5). New state: Cliopatria has no Münster row.

SHAPES ARE RADIUS READINGS: Münster 45 km, Meppen (7.29E 52.69N) 35 km, Vechta (8.29E 52.73N) 25 km, Cloppenburg (8.05E 52.85N) 20 km, Ahaus (7.01E 52.08N) 15 km, Wildeshausen (8.43E 52.90N) 15 km. Gazetteer names wanted: 'Meppen', 'Vechta', 'Cloppenburg', 'Ahaus', 'Wildeshausen'.

NOT SETTLED. (1) The infobox says 'Secularised to Prussia: 1802' and the text 1803; the dossier ends in February 1803 (Final Recess) and records a 1802 Prussian occupation. (2) The Galen conquests of Bremen-Verden (page: 'gained parts' in 1650-1678) are undated and not drawn; the 1679 pledge renewal for Wildeshausen is a loan to Sweden, not a gain. (3) The 1661 occupation of the city of Münster by Galen is internal and not an event. (4) The sellers in 1403 and 1406 are not named by the page. (5) The 1569 transfer of western Frisian territory to the bishoprics of Groningen and Deventer is ecclesiastical, not drawn. (6) The personal unions with Paderborn, Osnabrück and Cologne are only general periods on the page. (7) No ruler list was opened.

COUNTERPARTS NEEDING DOSSIERS: county-of-vechta, county-of-oldenburg, anabaptist-kingdom-of-munster (rebel state, February 1534-June 1535, under a year but a notable state), duchy-of-arenberg (Meppen 1803), Lordship of Ahaus.

## county-of-tyrol (County of Tyrol, 1140-1363)
Written 2026-10-25 for batch eu-09-x (3 pages opened; budget 5). New state: Cliopatria has no Tyrol row.

SCOPE. The dossier ends in 1363, when Tyrol became Habsburg land and Cliopatria's House of Habsburg row takes it (its area grows by 15.8 k km2 that year). The county itself continued as a crown land to 1919 (infobox 'Partitioned by Treaty of St Germain: September 10, 1919'; Trent and Brixen added 1803; Bavarian 1805-1814; Vorarlberg attached 1814); that later story belongs to house-of-habsburg / habsburg-monarchy. If the orchestrator wants Tyrol drawn as its own colour after 1363, extend this dossier: the gains of Kufstein, Kitzbuehel and Rattenberg (1504-1505, Landshut War, see duchy-of-bavaria) and of Lienz and the Puster valley (1500, page: 'In 1500 he also acquired the remaining Gorizia territories') are on opened pages but fall after 1363.

SHAPES. Tyrol 1271-1362 = Tirol (Austria) + Bozen (Italy) - a 30 km circle at 12.6E 46.85N (East Tyrol, Gorizia land to 1500), about 20 k km2 against 15.8-16.8 k in Cliopatria. Core 1140-1270 = a 35 km circle at Meran (11.16E 46.67N). Gazetteer names wanted: 'Meran' (place; Merano), 'Lienz', 'Brixen', 'Salorno'.

NOT SETTLED. (1) The 1140 date is 'about'. (2) Meinhard II's valley gains are undated within 1271-1295. (3) The page does not date Meinhard's Trent/Brixen struggle. (4) Carinthia and Carniola: 'In 1286 he was enfeoffed with the Duchy of Carinthia and the adjacent March of Carniola'; the Carinthia dossier (eu-09) treats Carinthia as a separate state to 1335, so this is a personal union and is not a Tyrol gain (rule 4). (5) 1335: Louis gave Carinthia to Albert II of Austria; Margaret kept Tyrol; the extract does not say what else changed. (6) The 1342-1363 Wittelsbach period: eu-09-a's duchy-of-bavaria dossier keeps Tyrol inside the Bavarian outline (Cliopatria's 1352-1362 shape includes it) and flags it; Tyrol is drawn here as a separate state, so one of the two should take Tyrol out. (7) Margaret's bequest has no month on any opened page; the Habsburg takeover is dated 1363 only.

COUNTERPARTS NEEDING DOSSIERS: county-of-gorizia (Lienz and the Puster valley), prince-bishopric-of-trent and prince-bishopric-of-brixen (Trent/Brixen were separate states to 1803).

## duchy-of-brunswick-luneburg (Duchy of Brunswick-Lüneburg, 1235-1692)
Written 2026-10-25 for batch eu-09-x (5 pages opened; budget 5). New state: Cliopatria has no Brunswick-Lüneburg row; the Welf lands sit inside Holy Roman Empire Minor States.

WHAT THE STATE IS. The Duchy of Brunswick-Lüneburg (1235) was divided into 'subordinate principalities' under one dynasty: Brunswick (later Wolfenbüttel) and Lüneburg (Celle) 1267/1269 (Lüneburg page; the Duchy page says 1269), Grubenhagen 1291-1596, Göttingen 1345 (the Duchy table gives 1291-1463 elsewhere), Calenberg 1432, Harburg 1527, Gifhorn 1539, Dannenberg 1569, and reunions (Grubenhagen to Lüneburg 1617; Calenberg-Göttingen under Wolfenbüttel 1584-1634, independent again 1635). They are drawn here as one state with one colour, as the Duchy page does (infobox area 21,170 km2 for 1635); the internal divisions are not ledger events because no land crosses the outer border. If the orchestrator wants the principalities as states, principality-of-luneburg and principality-of-brunswick-wolfenbuttel are the natural slugs and the electorate-of-hanover dossier already names principality-of-calenberg and principality-of-luneburg as predecessors.

SHAPES are circles (gazetteer lacks the towns): Brunswick 10.52E 52.27N 35 km; Lüneburg 10.41E 53.25N 42 km; Celle 10.08E 52.62N 38 km; Hanover/Calenberg 9.73E 52.37N 30 km; Göttingen 9.93E 51.53N 30 km; Einbeck/Grubenhagen 9.87E 51.82N 25 km; Hoya (Nienburg) 9.20E 52.64N 25 km; Diepholz 8.37E 52.61N 20 km; Hameln-Bodenwerder 9.45E 52.03N 18 km; the Hildesheim ring 9.95E 52.15N 28 km minus 8 km. Gazetteer names wanted: 'Brunswick' and 'Lüneburg' if absent, 'Celle', 'Einbeck', 'Nienburg', 'Diepholz', 'Hameln', 'Bodenwerder', 'Hildesheim' (as radius places).

NOT SETTLED. (1) The first-year extent of the duchy: the page names no land. (2) Division dates: 1267 or 1269. (3) The Peace of Hanover is 1373 in most places and 1374 in one. (4) The Wittenberg rule: the Lüneburg War page gives no period (the Duchy page has them ruling the principality 1373-1388). (5) Hoya: only 'the larger part' went to Calenberg in 1582; who took the rest is not on the page; Diepholz 1584 on this page, 'earlier-acquired' on the Hanover page. (6) The Great Stift as a ring is a stand-in; which Ämter stayed after 1643 is not given. (7) Thirty Years' War occupations (Danish, Imperial, Swedish) are not entered: no page opened dates them. (8) Dissolution 1692: Lüneburg joined the electorate only in 1705 and Wolfenbüttel stayed apart to 1806; the page's Hanover successor is therefore partial.

COUNTERPARTS NEEDING DOSSIERS: electorate-of-saxony (Ascanian, to 1422), prince-bishopric-of-hildesheim, county-of-hoya, county-of-diepholz, principality-of-luneburg (to 1705), principality-of-brunswick-wolfenbuttel (to 1806/1814), principality-of-grubenhagen (1291-1596).

## margraviate-of-baden (Margraviate of Baden, 1112-1803)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Baden row before the Electorate of Baden (1803-1805).

SCOPE. One state for the Margraviate of Baden with its cadet lines (Hachberg, Sausenberg, Pforzheim; Baden-Baden and Baden-Durlach 1535-1771), as the Baden page treats it; the divisions are internal and not ledger events. Ends 1803 when the electorate (Cliopatria's Electorate of Baden, eu-20) begins; its additions of 1803 (Constance, Palatine districts) are theirs.

SHAPES are circles (gazetteer lacks the towns): Rastatt 8.20E 48.86N 18 km; Pforzheim 8.70E 48.89N 13 km; Durlach 8.40E 48.99N 10 km; Emmendingen 7.85E 48.12N 10 km; Müllheim-Lörrach 7.65E 47.75N 15 km; Lahr-Mahlberg 7.84E 48.31N 10 km. Gazetteer names wanted: 'Baden-Baden', 'Rastatt', 'Pforzheim', 'Durlach', 'Emmendingen', 'Lörrach', 'Lahr', 'Offenburg' (the gazetteer has Karlsruhe only).

NOT SETTLED. (1) The Hachberg and Sausenberg lands: the page gives the lines' dates (Hachberg 1190-1418; Sausenberg reverting to Baden-Baden in 1503; the Pforzheim line 1291-1361 as a note) but not their territory or heirs, so the 1190 gain is a bridge at confidence 2 with counterpart 'nobody'. (2) The 1462 surrender to the Palatinate and its allies: no lands, no year of surrender on the page. (3) The left-bank cession to France: the Baden page's year for it is 1792 (the usual Treaty of Basel / Paris dates are later), no lands named; not entered. (4) The Ortenau: Baden-Baden received the rights to the Landvogtei of Offenburg in 1701 and it reverted to the Emperor under the 1765 treaty (Baden-Baden page); not entered (rights, not territory). (5) The Eberstein county was de facto Baden-Baden until 1660 (Gernsbach); not entered. (6) The Baden-Baden and Baden-Durlach shapes are not separated. (7) The Peace of Westphalia restored the 1550 situation; no map change recorded.

COUNTERPARTS NEEDING DOSSIERS: lordship-of-lahr-mahlberg (to 1442 and 1629), county-of-eberstein, margraviate-of-baden-hachberg (1190-1418) if the cadet lines are wanted as states, electorate-of-baden (eu-20).

## prince-bishopric-of-wurzburg (Prince-Bishopric of Würzburg, 1168-1803)
Written 2026-10-25 for batch eu-09-x (4 pages; budget 5). New state: Cliopatria has no Würzburg row before the Grand Duchy of Würzburg (1806-1814).

THIN PAGES. The Prince-Bishopric page gives dates but no territory (no area, no towns, no acquisitions or losses); the Grand Duchy page gives no area either, only that Schweinfurt was added in 1810. The 40 km circle at Würzburg (9.93E 49.79N) is therefore a stand-in, not a reading of the page. Gazetteer has the place 'Würzburg'.

NOT SETTLED. (1) Area and boundary. (2) The ducal title: infobox 1441, text 1442. (3) The Swedish occupation: the 1633 grant is on the Bernhard page ('citation needed'); the Swedish capture of Würzburg (1631 or 1632) and the exact end are not on pages opened. (4) 1802: Bavarian occupation of the bishopric is on the Bamberg page; the Würzburg page does not date it. (5) The Würzburg territory of 1803-1805 (Bavarian), 1806-1814 (Grand Duchy, Ferdinand III) is in Cliopatria's Grand Duchy row and duchy-of-bavaria.

COUNTERPARTS NEEDING DOSSIERS: grand-duchy-of-wurzburg exists in Cliopatria (eu-20); county-of-henneberg (to 1583), county-of-wertheim.

## prince-bishopric-of-bamberg (Prince-Bishopric of Bamberg, 1245-1803)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Bamberg row.

SHAPES. Bamberg 10.89E 49.89N 34 km (3,630 km2 against the page's 3,580); the Carinthian circles Villach 13.85E 46.61N 14 km, Wolfsberg 14.84E 46.84N 14 km, Tarvis 13.58E 46.51N 8 km, Kirchdorf an der Krems 14.12E 47.91N 10 km are coordinates of the named towns with arbitrary radii (the page gives no size of the estates). Gazetteer names wanted: 'Villach', 'Feldkirchen', 'Wolfsberg', 'Tarvis', 'Kirchdorf an der Krems'.

NOT SETTLED. (1) Start year: the page's 1245 is 'about'; the diocese is 1007 and the princely rank may be earlier. (2) Which of the Carinthian estates the bishops held before 1245 is not on the page. (3) Territorial gains and losses inside Franconia (Forchheim, Hallstadt, Kronach, Lichtenfels, Bayreuth lands) are not on the page. (4) The infobox says 'Mediatised to Bavaria in 1802', the text 1803; the dossier ends 25 February 1803 and records the 1802 Bavarian occupation. (5) The Swedish occupation start is not dated beyond the bishop's flight in 1631.

COUNTERPARTS NEEDING DOSSIERS: none new (habsburg-monarchy, duchy-of-bavaria, swedish-empire exist elsewhere).

## duchy-of-julich-berg (Duchy of Jülich-Berg, 1003-1806)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Jülich or Berg row (Grand Duchy of Berg is 1806 on).

SCOPE. One state for Jülich and Berg: the Jülich page's infobox, Berg's union in 1423 (the Berg page also says 1348). The County of Berg itself (1101, duchy 1380) before the union is not drawn: no dossier for duchy-of-berg 1101-1423 exists. The United Duchies of Jülich-Cleves-Berg (1521-1614) are a personal union of this state with duchy-of-cleves and are not territory (rule 4); the electorate-of-brandenburg dossier names them `julich-cleves-berg` as the counterpart of its 1614 gain: the Cleves-Mark part is this batch's duchy-of-cleves, the Ravensberg part is the loss recorded here.

SHAPES are circles (gazetteer lacks the towns): Jülich 6.37E 50.93N 32 km; Berg 7.10E 51.10N 28 km; Ravensberg (Bielefeld) 8.53E 52.02N 20 km. Gazetteer names wanted: 'Jülich', 'Düren', 'Bielefeld' (radius places); 'Berg' / 'Bergisches Land' (region).

NOT SETTLED. (1) No area on either page. (2) Berg's first union with Jülich: 1348 or 1423. (3) Ravensberg's earlier union with Berg is undated. (4) Ravenstein (Brabant) went to Neuburg in 1614 and is not drawn; Brandenburg gave up its claim in 1671 (JS page). (5) The 1614 occupations: the Dutch and Spanish held Cleves, Mark, Wesel, Neuss and Mülheim in 1614 without dates on the page; not entered. (6) The French annexation of Jülich: 1794 occupation, Lunéville 1801 (no month on this page). (7) From 1685 the Neuburg line also held the Electoral Palatinate, from 1777 Bavaria; both are personal unions (electoral-palatinate dossier has the 1685 Neuburg gain of the Upper Palatinate district).

COUNTERPARTS NEEDING DOSSIERS: duchy-of-berg (1101-1423), county-of-ravensberg, palatinate-neuburg, julich-cleves-berg (as an umbrella, 1521-1614).

## duchy-of-cleves (Duchy of Cleves, 1092-1614)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Cleves row.

SCOPE. The state is Cleves with Mark from 1391, ending when the electorate of Brandenburg takes both at Xanten in 1614 (infobox). The Cleves page has the final incorporation into Brandenburg-Prussia in 1666 and French annexation of the left bank in 1795 (Peace of Basel); those are Brandenburg-Prussia's events. The county of Mark before 1391 (Berg-Altena 1160; the page puts the seat at Altena, then Burg Mark near Hamm in the 1220s; Hamm founded 1226) is county-of-mark, not drawn here.

SHAPES are circles (gazetteer lacks the towns): Cleves 6.40E 51.72N 28 km; Mark 7.55E 51.52N 31 km. Gazetteer names wanted: 'Cleves' (Kleve), 'Wesel', 'Hamm'.

NOT SETTLED. (1) The union with Mark: 1391 on the infobox and Cleves text, 1394 on the Mark page. (2) The extent of Cleves before 1391 and the towns it held (Duisburg, Rees, Xanten, Emmerich only as 'towns' on the page). (3) The 1614 Dutch and Spanish occupations are undated on the page; the Dutch held 'large parts of the Duchy of Cleves' until 1672. (4) The Cleves page does not mention a 1666 treaty (the War of the Jülich Succession page has the Treaty of Cleves 1666). (5) The Soest Feud (1444-1449) and the loss of Soest are not on any page opened: the Mark page 'does not mention' it; electorate-of-cologne has Soest. (6) The United Duchies (1521) are a personal union and not drawn.

COUNTERPARTS NEEDING DOSSIERS: county-of-mark (to 1391), palatinate-neuburg, julich-cleves-berg (umbrella).

## duchy-of-guelders (Duchy of Guelders, 1096-1543)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Guelders row (the Union of Utrecht row covers the northern quarters from 1579).

SCOPE. County 1096, duchy 1339, ends at the Treaty of Venlo (7 September 1543), where habsburg-netherlands (the dossier of this batch) records the matching 1543 gain with counterpart `duchy-of-guelders`. Later: the Upper Quarter stays Spanish/Austrian Guelders until 1795 (France), the three northern quarters sit in the Union of Utrecht row; those are not this state's events.

SHAPES. Geldern 6.32E 51.52N 22 km; Zutphen 6.20E 52.14N 28 km; from 1339 the gazetteer region 'Guelders' (about 9,100 km2). Gazetteer names wanted: 'Zutphen', 'Roermond', 'Venlo', 'Nijmegen', 'Veluwe', 'Betuwe' (the region 'Guelders' exists).

NOT SETTLED. (1) The acquisition years of Veluwe, Nijmegen, Betuwe, Roermond and Venlo (the page gives none; confidence-1 event at 1339). (2) 1473-1492 is entered as a Burgundian occupation; the Egmond claimants held out, the page does not say how much of the duchy the Burgundians actually held. (3) 1538: the page gives the end of Charles of Egmond's reign and not William's succession year or title. (4) The Guelders Wars page says Charles controlled 'Guelders, Groningen, and Frisia'; no Groningen or Frisia years are given there. (5) The 1581 date for the Act of Abjuration (northern quarters) against 1579 for the Union: the Duchy page does not mention 1579. (6) The page gives no area.

COUNTERPARTS NEEDING DOSSIERS: county-of-zutphen (before 1127), duchy-of-burgundy (eu-10, exists), duchy-of-julich-berg (this batch).

## county-of-hainaut (County of Hainaut, 880-1432)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Hainaut row. eu-09-a's notes (county-of-holland, county-of-brabant) asked for a county-of-hainaut dossier for at least 1260-1433.

SCOPE. 880 to 1432 (infobox 'Absorbed into the Burgundian Netherlands: 1432'). The Holland dossier (eu-09-a) ends in 1433 on the Holland page; this one follows the Hainaut infobox. After 1432 the land is part of the Burgundian and then Habsburg Netherlands (habsburg-netherlands, which includes Belgian Hainaut in its shapes). The French cessions of the south (1659 Treaty of the Pyrenees, 1679 Nijmegen: Valenciennes, Le Quesnoy, Avesnes) and the 1797 cession of the north are not dated beyond that by the page and belong to the Habsburg Netherlands and France.

SHAPES. Belgian province of Hainaut (admin1) with a 25 km circle at Valenciennes (3.52E 50.36N) and a 15 km circle at Avesnes (3.93E 50.12N). Gazetteer names wanted: 'Valenciennes', 'Avesnes-sur-Helpe', 'Mons'.

NOT SETTLED. (1) Start: ±880 (infobox) against the 870 Meerssen mention; the early extent. (2) 1432 (infobox, Hainaut text) against 1433 (succession table; Jacqueline infobox 12 April 1433; Easter 1433 treaty of The Hague) against 1436 (Jacqueline's death, when the page says Philip 'inherited Hainaut and Holland'). (3) The Wittelsbach succession (Louis IV's wife Margaret, 1345) is not on this page; the 1356 rename is the page's union date. (4) The 1051/1067/1071 sequence: the page has Baldwin VI ruling both from 1067 and the union ending 1071; 'the unification of Hainaut as an Imperial fief' after Arnulf's defeat in 1071. (5) Treaty dates of 1659 and 1679 (the page says 1679 for Nijmegen, 1797 for the northern cession against 1795 annexation). (6) Humphrey of Gloucester's recognition in December 1424 is an episode of the Jacqueline conflict and is not entered as a territorial event.

COUNTERPARTS NEEDING DOSSIERS: county-of-flanders (exists, Cliopatria), duchy-of-burgundy (exists, eu-10), west-franks (exists).

## duchy-of-pomerania (Duchy of Pomerania, 1188-1637)
Written 2026-10-25 for batch eu-09-x (5 pages; budget 5). New state: Cliopatria's Pomerania row covers only 1139-1187 (dossier `pomerania`, eu-15-e); this dossier is the continuation 1188-1637 that eu-15-e, electorate-of-brandenburg and the group scope ask for. It could be merged into `pomerania` (same state, one colour).

SHAPES. From Cliopatria's pomerania_1187 outline (28.3 k km2 in the grid) with 40 km at Stolp (16.95E 54.46N), 30 km at Prenzlau (13.86E 53.32N), 35 km at Rügen (13.40E 54.43N) and 25 km at Lauenburg-Bütow (17.6E 54.35N). Gazetteer names wanted: 'Stolp' (Slupsk), 'Prenzlau', 'Rügen' (island), 'Lauenburg' (Lebork), 'Bütow' (Bytow).

NOT SETTLED. (1) The Schlawe and Stolp lands: the page dates their acquisition to 1317, but Cliopatria's 1139 shape already reaches them (eu-15-e says the same); the first keyframes remove them. (2) The Uckermark loss is undated on the page; 1250 is the page's treaty year. (3) Rügen came with two wars against Mecklenburg (undated on the page); the Mecklenburg share of the inheritance is not on it. (4) Lauenburg-Bütow: 1455 (Duchy page, Poland's promise) against 1466 (Peace of Thorn grant) against 1526 (fief). (5) Overlordships (Poland 1121-1138, Denmark 1185-1227, Brandenburg's claim 1236/1250/1529, Empire 1181 and 1227-1637) are vassal ties of the suzerains' ledgers. (6) Treaty of Grimnitz (1529), Pyritz (1493), Soldin (1466) and the 1569 Stettin/Wolgast division are not on any page opened. (7) 1637-1648: the Swedes held the land; Brandenburg's inheritance claim ('a pact between the two families in 1464') was settled only at Westphalia. (8) The 1295 partition into Wolgast and Stettin and the 1478/1532 reunion and division are internal and not drawn. (9) No area on any page.

COUNTERPARTS NEEDING DOSSIERS: principality-of-rugen (1168-1325), teutonic-order (Cliopatria), kingdom-of-poland (exists elsewhere), margraviate-of-brandenburg (exists), swedish-empire, duchy-of-mecklenburg (the earlier state: the slug is Cliopatria's 1806-1870 row).

## county-of-oldenburg (County of Oldenburg, 1108-1805)
Written 2026-10-25 for batch eu-09-x (3 pages; budget 5). New state: Cliopatria has no Oldenburg row before the Duchy of Oldenburg (1806-1870, eu-20). The prince-bishopric-of-munster dossier of this batch names `county-of-oldenburg` as counterpart of its 1403 Cloppenburg gain and `duchy-of-oldenburg` for the 1803 loss; this dossier answers both, as the same state.

SHAPES. Circles: Oldenburg 8.21E 53.14N 24 km; Jever 7.90E 53.57N 12 km; Varel 8.13E 53.40N 12 km; Delmenhorst 8.63E 53.05N 12 km; Vechta 8.29E 52.73N 25 km; Cloppenburg 8.05E 52.85N 20 km. Gazetteer names wanted: 'Oldenburg', 'Varel', 'Delmenhorst' (the Münster dossier already lists Vechta and Cloppenburg).

NOT SETTLED. (1) Jever: this page says only 'before 1603'; the East Frisia page (county-of-east-frisia, this batch) gives 1575 and is cited for the gain; Butjadingen and Stadland, Wildeshausen (the page says Gerhard II 'sold his patrimony' to Hoya, year printed '13844'), and the 1403 loss of the Cloppenburg district to Münster (the Münster page, no seller named) are not on this page. (2) Jever's later history and the 1814-1818 changes are not on any page opened. (3) The infobox name 'Created on breakup of Saxony: 1108' sits before the 1180 breakup; 1108 is the page's year of first mention. (4) 1805 is a hand-over year, not an event.

COUNTERPARTS NEEDING DOSSIERS: county-of-delmenhorst (appanage), lordship-of-varel, lordship-of-jever (Frisian), the Kalmar union (1448-1454 personal union, rule 4).

ADDED LATER (same batch): the 1803 gain of the Principality of Lübeck (Eutin), from the Prince-Bishopric of Lübeck page, entered as an exclave circle; the Oldenburg page itself does not mention it.

## prince-bishopric-of-hildesheim (Prince-Bishopric of Hildesheim, 1235-1803)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 5). New state: Cliopatria has no Hildesheim row. The duchy-of-brunswick-luneburg dossier of this batch carries the mirror events (1523 gain, 1643 loss) with counterpart `prince-bishopric-of-hildesheim`.

SHAPES. Hildesheim 9.95E 52.15N 28 km, Hameln-Bodenwerder 9.45E 52.03N 18 km, Peine 10.23E 52.32N 8 km. Gazetteer names wanted: 'Hildesheim' (as a radius place), 'Peine', 'Hameln'.

NOT SETTLED. (1) No area, boundary or ruler list; the shape is a stand-in. (2) The 1523 loss mirrors the Brunswick gain (including the Hameln-Bodenwerder seats), but the page names only 'Ämter' and a few towns. (3) 1643: the Prince-Bishopric page gives no 'Main Treaty' and no Thirty Years' War; the name is from the feud page. (4) The Wittelsbach union with Cologne (1573-1761) is a personal union. (5) The 1802 Prussian occupation is not on this page (Münster and Bamberg pages have 1802 occupations); 1803 is the page's year. (6) Goslar and the Hanover share after 1815 are not drawn.

COUNTERPARTS NEEDING DOSSIERS: none new (duchy-of-brunswick-luneburg is in this batch; kingdom-of-prussia is Cliopatria).

## prince-bishopric-of-osnabruck (Prince-Bishopric of Osnabrück, 1225-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 5, thin page). New state: Cliopatria has no Osnabrück row.

SHAPE. A 30 km circle at Osnabrück (8.05E 52.28N); the gazetteer has the place 'Osnabrück'. The page names no district and no acquisition.

NOT SETTLED. (1) Area, boundary and acquisitions (Vörden, Fürstenau, Wiedenbrück, Reckenberg, Bramsche, Quakenbrück and Melle are not on the page). (2) The 1236 Tecklenburg renunciation concerns jurisdiction over the town. (3) The 1802 Hanoverian occupation is not on the page. (4) Cliopatria's Kingdom of Hanover row (1803) is the successor row for 1803.

## prince-bishopric-of-paderborn (Prince-Bishopric of Paderborn, 1281-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 5, thin page). New state: Cliopatria has no Paderborn row.

SHAPE. A 28 km circle at Paderborn (8.75E 51.72N); the gazetteer has the place 'Paderborn' (population None). The page names no district and no acquisition.

NOT SETTLED. (1) Area, boundary and acquisitions. (2) Start: 1281 (infobox) against c. 1200 (bailiwick returned to the bishops) against 1180. (3) End: infobox 1802 against the Final Recess of 25 February 1803; the Münster dossier of this batch uses the 1802 Prussian occupation and the 1803 secularisation. (4) The page does not describe a Wittelsbach union with Cologne; Ferdinand of Bavaria (1618-50) and Clemens August (1719-61) are listed as also Elector of Cologne. (5) The Soest Feud (1444-1449) is the only war on the page.

COUNTERPARTS NEEDING DOSSIERS: none new.

## principality-of-ansbach (Principality of Ansbach, 1398-1791)
Written 2026-10-25 for batch eu-09-x (1 page; budget 5, thin page). New state: Cliopatria has no Ansbach row.

SHAPE. A 28 km circle at Ansbach (10.57E 49.30N). Gazetteer names wanted: 'Ansbach'.

NOT SETTLED. (1) Area, boundary and acquisitions (the Kulmbach inheritance of 1603 and the Sayn-Altenkirchen inheritance of 1741 are not on the page). (2) 1603: the page mentions no partition; Joachim Ernst's accession is the only 1603 item. (3) The personal union with Bayreuth (1769-1791) is not territory. (4) End: the sale is 2 December 1791, the formal annexation 28 January 1792. (5) 1806 (Bavaria) is not on the page.

COUNTERPARTS NEEDING DOSSIERS: burgraviate-of-nuremberg (the predecessor, to 1398).

## principality-of-bayreuth (Principality of Bayreuth, 1398-1791)
Written 2026-10-25 for batch eu-09-x (1 page; budget 5, thin page). New state: Cliopatria has no Bayreuth row.

SHAPE. A 32 km circle at Bayreuth (11.58E 49.94N) and a 20 km circle at Kulmbach (11.45E 50.10N). Gazetteer names wanted: 'Bayreuth', 'Kulmbach'.

NOT SETTLED. (1) Area, boundary and acquisitions (Hof, Wunsiedel, the Unterland territories added by the 1541 House Treaty of Regensburg). (2) The page calls the territory officially Brandenburg-Kulmbach until 1806 without a date for the name. (3) The personal union with Ansbach 1769-1791 (not territory). (4) After 1791: French occupation (no year), Tilsit 1807, Bavaria 1810: Bayreuth is not listed in the Cliopatria rows between 1791 and 1810 as a separate state; Prussian and then Bavarian dossiers carry it. (5) Ansbach's page dates the annexation to 28 January 1792; this page gives only the sale date.

COUNTERPARTS NEEDING DOSSIERS: burgraviate-of-nuremberg (the predecessor, to 1398).

## county-of-east-frisia (County of East Frisia, 1464-1744)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 5). New state: Cliopatria has no East Frisia row.

SHAPES. Aurich 7.48E 53.47N 24 km (1,810 km2 against the infobox 1,800 km2 of 1800); Jever 7.90E 53.57N 12 km; Esens 7.61E 53.65N 15 km; Emden 7.20E 53.37N and Leerort 7.45E 53.23N 6 km for the garrisons. Gazetteer names wanted: 'Aurich', 'Emden', 'Jever', 'Esens', 'Leer'. The modern region East Frisia is 3,142 km2 (East Frisia page) which includes Harlingerland and the Jeverland.

NOT SETTLED. (1) The 1464 date is the imperial elevation; Norden was recognised on 14 June 1463. (2) The county's extent before 1575 and when East Frisia held the Jeverland (page: it 'definitively lost' it). (3) The Dutch garrisons: Emden (from 1595 humiliations / the 1603 Hague agreement / 1611 Osterhusen accord) and Leerort; the page says only 'until 1744'. (4) The personal union with Prussia (1744-1807) and the Kingdom of Holland (1806 on the East Frisia page, 9 July 1807 on the County page) are later states' events. (5) The East Frisia page does not give 1464 or 1581; the County page gives 1581 only as Enno III's marriage.

COUNTERPARTS NEEDING DOSSIERS: lordship-of-harlingerland (Esens, Stedesdorf, Wittmund; to 1600), the Jeverland / lordship-of-jever (Oldenburg 1575), dutch-republic (exists).

## mecklenburg (Mecklenburg, 1170-1805)
Written 2026-10-25 for batch eu-09-x (5 pages; budget 5). New state: Cliopatria's Duchy of Mecklenburg row is 1806..1870 only (and its slug `duchy-of-mecklenburg` is eu-20's), so this dossier covers the Lordship and Duchy before it and is named `mecklenburg`, the counterpart name the other eu-09 notes already use.

SCOPE AND SHAPES. One state for the Mecklenburg duchies; the partitions (Mecklenburg-Schwerin, -Stargard and -Güstrow; 1520, 1621, 1658; the Strelitz line in 1701; the united duchy 1471-1520 and 1695-1701) are internal. Circles: 11.55E 53.80N 35 km (core); Wismar 11.46E 53.89N 15 km; Rostock 12.14E 54.09N 30 km; Stargard (Neubrandenburg) 13.26E 53.56N 35 km; Schwerin 11.41E 53.63N 28 km. Gazetteer names wanted: 'Schwerin', 'Wismar', 'Rostock', 'Neubrandenburg', 'Güstrow'.

NOT SETTLED. (1) No area on any page; the south (Güstrow, Parchim, the Werle lands) has no dated acquisition. (2) 1170: the princely recognition on the Mecklenburg page; the 1167 restoration of Pribislav is not on it. (3) 1312: 'by 1312'; the page gives no separate years for Stargard and Rostock. (4) The Peace of Westphalia terms for Mecklenburg (Schwerin and Ratzeburg bishoprics secularised to Mecklenburg, Poel and Neukloster) are not on the Güstrow page; the Wismar page gives only Wismar and the Poel and Neukloster districts. (5) The Duchy of Mecklenburg-Schwerin page's 1701 Treaty of Hamburg and the Strelitz recreation of the Stargard lordship. (6) Wismar: 1301 'came under the rule', 1648, 1803 and the 1903 renunciation; the 1803 deal is a cession with a redemption right, not a pledge.

COUNTERPARTS NEEDING DOSSIERS: lordship-of-rostock, lordship-of-stargard, county-of-schwerin, lordship-of-werle (not in this dossier), swedish-empire (exists).

## united-belgian-states (United Belgian States, 1790-1790)
Written 2026-10-25 for batch eu-09-x (1 page; budget 2-5). New state, type rebel: Cliopatria has no row for the confederation of 1790. It is a 11-month state, and the Habsburg Netherlands dossier of this batch carries the matching events (contest from the Battle of Turnhout, 27 October 1789; loss in January 1790; gain and contest end in December 1790) with counterpart `united-belgian-states`.

DATES FROM THE PAGE. 'On 11 January 1790 they signed a pact, establishing a confederation' (infobox 'Treaty of Union: 11 January 1790'); 'It existed from January to December 1790.' Infobox: Manifesto of Brabant 24 October 1789, Battle of Falmagne 22 September 1790, Surrender of Brussels 2 December 1790. 'On 24 October 1790 imperial troops took the city of Namur. Two days later, the province of West Flanders followed suit.' 'By December the entire territory was again in imperial hands.' The page also says Brabant 'declared that it no longer recognized the Emperor's rule' in 'January 1789' in its body, which contradicts the infobox's 24 October 1789 and the January 1790 treaty; I took the infobox dates and treat the body's 1789 as a slip of the page.

SHAPE. The page names no province but Brabant, Flanders and Namur, says all others 'except Luxembourg' followed, and gives 'the western and central part of present-day Belgium'. Drawn as gazetteer 'Belgium' minus the Liege province minus the Luxembourg province (about 26,300 km2). The Republic of Liege (1789-1791 on the page's timeline) 'joined the United Belgian States in a semblance of an alliance': not territory, so not drawn. The eight provinces are not named on the page.

NOT SETTLED. (1) The page says nothing of Ghent, Bruges, Mons or Tournai in 1790 and nothing of the Convention of The Hague (Habsburg-Dutch-British agreement of late 1790), so no event is entered for them. (2) Namur and West Flanders are entered as province-sized losses though the page speaks of 'the city of Namur' and 'the province of West Flanders'. (3) The Battle of Falmagne appears only in the infobox, undescribed. (4) The page gives no area or population.

COUNTERPARTS NEEDING DOSSIERS: none new (habsburg-netherlands is in this batch).

## palatinate-neuburg (Palatinate-Neuburg, 1505-1685)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 1-2). New state: Cliopatria has no Palatinate-Neuburg row.

SCOPE. 30 July 1505 (arbitration of Cologne after the Landshut War, 1503-1505) to the merger with the Electoral Palatinate in 1685 (infobox). The page also says 'The Duchy of Palatinate-Neuburg was abolished in 1808' and 'existed until 1799 or 1808'; after 1685 the Neuburg line held the electorate, so the Danube lands are drawn inside the electoral-palatinate dossier (gain 1685 with counterpart `palatinate-neuburg`, loss to Bavaria 1777). Counterpart of the founding is `duchy-of-bavaria` (Bavaria-Landshut sat inside that Cliopatria row).

DYNASTY. Otto Henry and Philip (1505), Wolfgang (1557), Philipp Ludwig (1569), Wolfgang Wilhelm (1614-53), Philip William (1653-90). Wolfgang Wilhelm 'also Duke of Jülich and Berg from 1614' (page): a personal union, covered by duchy-of-julich-berg (the page does not date the Treaty of Xanten; the War of the Jülich Succession page in the Cleves dossier gives 12 November 1614). Not territory of this state (rule 4). Rule 2: dynasty steps are not new states.

SHAPE. 35 km circle at Neuburg an der Donau (11.18E 48.73N), the same as in electoral-palatinate; the page area 2,750 km2 would be a 30 km circle (about 2,830 km2), so the circle is 1.4 times too large. The page names no town but Neuburg and nothing about Sulzbach's lands, so the 1614 Sulzbach separation is a `rename` (no region needed) at confidence 2. Gazetteer names wanted: 'Neuburg an der Donau' (not in the gazetteer), 'Sulzbach', 'Hilpoltstein'.

COUNTERPARTS NEEDING DOSSIERS: palatinate-sulzbach (1614-1742 line; it later inherited the Palatinate, hence Charles Theodore).

## landgraviate-of-hesse-marburg (Landgraviate of Hesse-Marburg, 1567-1604)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Hesse-Marburg row.

SCOPE. 1567 (Philip I's four-way partition) to 1604 (Louis IV's bequest). The page's infobox lists two periods, 1458-1500 and 1567-1604 (the text: 'existed between 1458 and 1500, and between 1567 and 1604/1650'). The first (Upper Hesse as an appanage of Henry III's line) is in landgraviate-of-hesse as the 1458 'split' event and is not a separate dossier; the 1604/1650 ambiguity is the dispute with Darmstadt (Hessian War 1645-48, settled 1648: Marburg to Kassel, Giessen and Biedenkopf to Darmstadt, per the Darmstadt page cited in those dossiers).

SHAPES. Marburg 8.77E 50.81N 30 km, Gießen (gazetteer place) 30 km, Nidda 9.01E 50.41N 12 km, Eppstein 8.39E 50.14N 8 km; the same Marburg circle is the 1604 gain in landgraviate-of-hesse-kassel and the Gießen circle is the Darmstadt gain. Gazetteer names wanted: 'Marburg', 'Nidda', 'Eppstein', 'Biedenkopf' (Gießen exists).

NOT SETTLED. (1) The page gives no month for 1567 or 1604 and no death date for Louis IV. (2) No area, no capital in the text. (3) Eppstein's fate in 1604 is not on the page. (4) The Marburg circle also covers Biedenkopf and some of the Giessen circle, so the 1604 pieces overlap at the join.

COUNTERPARTS NEEDING DOSSIERS: none new.

## landgraviate-of-hesse-rheinfels (Landgraviate of Hesse-Rheinfels, 1567-1583)
Written 2026-10-25 for batch eu-09-x (1 page of its own plus the Kassel page already read for landgraviate-of-hesse-kassel; budget 1-2). New state: no Cliopatria row.

SCOPE. 1567 to 1583 (Philip II's reign as given on the Rheinfels page; the Kassel page footnote gives the line's end in 1583 and the sharing). The page's later 'Hesse-Rheinfels' for Ernest (landgrave 1627-1658, Rheinfels and the lower county of Katzenelnbogen as inheritance of Maurice's younger sons, with Eschwege, Rotenburg and Wanfried added after 1655/1658) and 'Hesse-Rheinfels-Rotenburg', which 'survived till 1834', are cadet apanages inside Hesse-Kassel, not sovereign states in the sense of this atlas; the page gives no dates for their land changes, so no events are entered. Hesse-Rotenburg, Hesse-Eschwege and Hesse-Wanfried are not dossiers.

SHAPE. Same 14 km circle as the Kassel gain (7.71E 50.15N). The Amt of Rheinfels on the left bank and Braubach, Reichenberg and Hohenstein on the right bank are named; the lower county of Katzenelnbogen is larger than the circle. No area, no capital on the page. Gazetteer names wanted: 'St. Goar', 'Braubach', 'Rheinfels'.

NOT SETTLED. (1) No month for 1567 or 1583; (2) the page gives no division of 1583 (the Kassel footnote says three-way, the Landgraviate of Hesse page says Kassel); (3) the three-way sharing between Kassel, Marburg and Darmstadt is not drawn.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-hanau (County of Hanau, 1429-1736)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 1-2). New state: Cliopatria has no Hanau row.

SCOPE. The page starts the county in 1429 ('Established: 1429-1736 (with interruptions)'); the lordship before is page-silent, so the usual earlier date for the Lords of Hanau (my hint in the report: 1166) is not entered. Hanau-Münzenberg and Hanau-Lichtenberg are drawn as one state (the two lines kept inside it, as for Baden and Brunswick): the page's own dates are the division 1456/1458-1642 and the last reunion in 1712. The Lichtenberg half-barony is a Lower Alsace exclave from 1480 and under French sovereignty from 1680.

SHAPES. Hanau 8.92E 50.13N 22 km; Buchsweiler (Bouxwiller) 7.48E 48.82N 25 km. These are the two circles the Kassel and Darmstadt dossiers use for their 1736 gains. No area in either page. Gazetteer names wanted: 'Hanau', 'Babenhausen', 'Buchsweiler' / 'Bouxwiller'.

NOT SETTLED. (1) The lordship of Hanau before 1429; (2) the page gives no month for any event; (3) the 1642/1643 steps: Hanau-Lichtenberg's page says the 1643 treaty 'finally secured' the inheritance after Johann Ernst's death, but the reunion of the two counties is described only as 'for a last time in 1712'; I enter the 1642 step as a dynastic rename; (4) no Thirty Years' War dates on either page; (5) the French sovereignty (1680) is entered as a vassal_start with no matching end because it lasted past 1736.

COUNTERPARTS NEEDING DOSSIERS: barony-of-lichtenberg (Lower Alsace, the half inherited in 1480; French/Alsace group).

## county-of-katzenelnbogen (County of Katzenelnbogen, 1095-1479)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Katzenelnbogen row.

SCOPE. 1095 (infobox 'First mentioned') to 1479 (Count Philipp's death). The text of the page conflicts with the infobox: Diether I 'was first mentioned about 1070'; the comital title was vested in 1138. I used the infobox year. The 1260 partition into two lines is a rename inside one state: the page gives no lands. The War of the Katzenelnbogen Succession (1500-1557, Hesse against Nassau-Siegen) lies after the state and is not entered here.

SHAPES. Darmstadt 8.65E 49.87N 30 km and St. Goar 7.71E 50.15N 14 km, the same two circles landgraviate-of-hesse uses for its 1479 gain and (the 14 km one) landgraviate-of-hesse-rheinfels and -kassel use for 1567/1583. The page names no towns but Darmstadt (as a region), Katzenelnbogen (capital), Burg Rheinfels, Auerbach Castle and Rüsselsheim ('In 1435, Count John IV ... was building his last castle in Rüsselsheim'), and dates no acquisition. Gazetteer names wanted: 'Katzenelnbogen', 'Darmstadt' (as a place for the circle), 'Rüsselsheim', 'Auerbach'.

NOT SETTLED. (1) The early extent (the Kraichgau bequest of 1138 is not described as land); (2) all acquisitions, including Darmstadt and Rheinfels (the page gives only castle-building dates); (3) the heir: the text says the Landgraves of Hesse, the infobox says Hesse-Marburg; (4) the page gives no area.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-schaumburg (County of Schaumburg, 1110-1640)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Schaumburg row.

SCOPE. Infobox 1110 to 1640. The page is thin: it dates only 1106 (first Lord of Schauenburg, 'probably'), 1110 (appointment to Holstein and Stormarn), 1559 (Reformation) and 1640 (Otto V dies, partition). Holstein and Stormarn, and Holstein-Pinneberg 'until 1640', are Holstein topics; only the Weser county is drawn. The founding event is therefore confidence 1 for the land.

SHAPE. Rinteln 9.08E 52.19N 22 km, as in landgraviate-of-hesse-kassel's 1648 Schaumburg gain. No area on the page. Gazetteer names wanted: 'Rinteln', 'Stadthagen', 'Schaumburg'.

NOT SETTLED. (1) The 1640 shares: the page says three parts (Hesse-Cassel's eastern portion, the largest portion as Schaumburg-Lippe, a part of the Principality of Lüneburg) and does not locate them; the Kassel dossier of this batch has a 1648 gain of 'most of the County of Schaumburg' from a different page, which conflicts with Schaumburg-Lippe holding the largest portion. The Westphalia terms (1648) are not on this page. (2) The page gives no date for Stadthagen, Rinteln or the castle. (3) The Münster share some sources mention is not on the page.

COUNTERPARTS NEEDING DOSSIERS: county-of-schaumburg-lippe (1640-1806 and later; suggested slug), none beyond that (stem-duchy-of-saxony exists).

## swabian-circle (Swabian Circle, 1500-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New association (type umbrella): Cliopatria has no row for the Imperial Circles, and the brief names the Swabian and Franconian Circles. Rule 4: an association of estates is never territory; the shape below is a coarse reading of its member lands for the reviewer, not for colouring. The member territories with their own dossiers (Wurttemberg, Baden, Konstanz, Augsburg ...) carry the land.

SHAPE. Gazetteer Baden-Wurttemberg plus a 40 km circle at Augsburg, minus the gazetteer's Franconia region: about 39,700 km2 against the page's 34,314 km2 (1801). Gazetteer names wanted: none new (Augsburg, Baden-Wurttemberg and Franconia resolve).

DATES. 1500 (page; infobox 'Established: 1500'), 1803 (Bishop of Constance replaced by Baden as director) and 1806 (Rheinbundakte, 'to seven' members; infobox 'Disestablished: 1808' is not used). The page dates the army at Kehl ('from 1694 on even maintained its own army based at the Kehl fortress') but no war of the circle; no war entry.

NOT SETTLED. (1) The page's member list is selected, and the 88 territories of 1792 are not listed; (2) no creation month or Reichstag; (3) the infobox end (1808) against the text (1806).

COUNTERPARTS NEEDING DOSSIERS: none new.

## franconian-circle (Franconian Circle, 1500-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New association (type umbrella), named in the brief's scope. Rule 4: never territory; the member lands with their own dossiers in this batch (Bamberg, Wurzburg, Ansbach, Bayreuth) carry the land.

SHAPE. The gazetteer's Franconia region (about 38,200 km2). The page gives no area and no population, and not the directors or the seat of the circle's diet (Nuremberg appears only as a member imperial city), so no capital is entered.

NOT SETTLED. (1) No area; (2) the page's table lists 25 members and no total; (3) no war or military event on the page (it mentions only a Landfrieden union that 'disintegrated in the face of opposition from cities and princes').

COUNTERPARTS NEEDING DOSSIERS: none new (Eichstatt, Nuremberg and the Teutonic Order's bailiwick are not written here).

## further-austria (Further Austria, 1278-1805)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Further Austria row (the lands sit inside House of Habsburg to 1515 and Holy Roman Empire Minor States).

SCOPE. 1278 (infobox) to 1805 (Peace of Pressburg). The page is thin on territory: it dates the Breisgau only as 'after 1368', the Sundgau loss (1648), Tettnang (1780), the Fricktal's end (1797), the Lunéville grant (1801) and the 1805 dissolution. It does not date Alsace, Hohenberg (1381), Feldkirch (1375), Bregenz or the Ortenau (1556), and says the Aargau and other southern holdings were 'already lost in the 14th century to the expanding Swiss Confederacy' (Morgarten 1315, Sempach 1386): those are not drawn, because the page names no boundary or year for them. Also: the Leopoldian line took Tyrol and Further Austria at the Treaty of Neuberg (1379); Tyrol and Further Austria were ruled together under Frederick IV (1406-1439); the Tyrol dossier of this batch is county-of-tyrol (to 1363).

SHAPES. Mulhouse 30 km (6.96-7.63E, 47.5-47.9N), Freiburg 30 km, Tettnang 9.59E 47.67N 15 km, Fricktal 8.00E 47.52N 12 km. These are soft stand-ins. The gazetteer has no 'Ensisheim', 'Sundgau', 'Breisgau', 'Fricktal' or 'Tettnang'.

NOT SETTLED. (1) The 1278 holdings; (2) the 1803 return of the Breisgau (the page says only that Ercole died two years after 1801) and the 1805 division among Baden, Württemberg, Bavaria, Hohenzollern-Sigmaringen and Hesse; (3) where the Swabian Austria (Burgau) and Vorarlberg lands lay in time; (4) the page gives no area.

COUNTERPARTS NEEDING DOSSIERS: duchy-of-modena (Ercole III d'Este, 1801-1803), if not already written elsewhere.

## prince-bishopric-of-augsburg (Prince-Bishopric of Augsburg, 888-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Augsburg row.

SCOPE. Infobox 'c. 888' (imperial immediacy) to 25 February 1803 (mediatised to Bavaria). The page's 'Bishopric established: 4th century' is the diocese, not the state. The free imperial city of Augsburg (1276) is not part of the prince-bishopric and is not drawn. The 1537 Dillingen move and the infobox 'Capital: Augsburg, to 1276' conflict; the text event is used.

SHAPES. Dillingen 10.32E 48.57N 22 km; Fussen 10.70E 47.57N 14 km (about 2,135 km2 against 2,365 km2 on the page). Gazetteer names wanted: 'Dillingen an der Donau', 'Fussen'. Straubing is named as a gift of Bishop Bruno (1006-1020) and is not drawn (the Straubing in the page is not placed).

NOT SETTLED. (1) Both acquisitions are dated by episcopate only (confidence 1); (2) the page gives the Reformation losses ('about 250 parishes, 24 monasteries, and over 500 benefices', no year) and the Westphalia losses (1648) without land, so none is drawn; (3) whether the Swedish occupation covered the bishop's lands (the page speaks of Augsburg city); (4) Bavarian possession 1 December 1802 against the infobox's 25 February 1803.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-constance (Prince-Bishopric of Constance, 1155-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Constance row.

SCOPE. 1155 (infobox 'Prince-Bishopric: 1155') to 1803. The page notes: the imperial city of Constance lost its free status and was 'incorporated into their Further Austrian possessions in 1548' (the bishop's sovereignty there 'limited to a small area around the cathedral'); the Landgraviate of Thurgau 'was conquered by the Swiss Confederacy in 1460' (a neighbour, not the bishop's land); the bishopric joined the Swabian Circle in 1500; the diocese was dissolved in 1821. None is a territorial event of the prince-bishopric.

SHAPE. 22 km circle at 9.10E 47.70N between Konstanz, Reichenau and Meersburg. Gazetteer names wanted: 'Meersburg', 'Reichenau', 'Konstanz' (the last may resolve as 'Constance').

NOT SETTLED. (1) No area or acquisition dates on the page ('Acquisitions: not on page'); (2) the page's succession box says 'Electorate of Baden' while the text says 'Margraviate of Baden'; the counterpart slug is electorate-of-baden, the Cliopatria row that follows the margraviate in 1803 (the Baden dossier of this batch ends in 1803 with that successor); (3) the part of the lands on the Swiss shore is not distinguished.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-strasbourg (Prince-Bishopric of Strasbourg, 982-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Strasbourg bishopric row (France's rows and Holy Roman Empire shapes cover the land).

SCOPE. 982 (infobox 'Imperial immediacy') to 1803. The page gives no 1262 war with the city, no 1648 date and no 1789/1790 date; the left bank is shown as French from 1681 ('Annexation recognised by the Holy Roman Empire: 1697').

SHAPES. Left bank (Molsheim) 7.49E 48.54N 25 km; Mundat (Rouffach) 7.30E 47.96N 15 km; right bank 7.95E 48.40N 22 km. Gazetteer names wanted: 'Saverne', 'Molsheim', 'Benfeld', 'Rouffach', 'Oberkirch', 'Ettenheim', 'Oppenau'.

NOT SETTLED. (1) No area; (2) Strasbourg city's relation to the bishops (free city) is not on the page; (3) the dating of the infobox 'Gained autonomy: 775 982'; (4) the page gives 'from the 13th century' for the prince-bishopric against 982 for immediacy.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-eichstatt (Prince-Bishopric of Eichstätt, 1305-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Eichstätt row.

SCOPE. 1305 (infobox) to 1802 (infobox 'Mediatised to Salzburg: 1802'; the text says 1803 and the compensation of Archduke Ferdinand, Elector of Salzburg from 1803). The 1805 passage to Bavaria and the 1817-1855 Principality of Eichstätt as a Bavarian fief are later steps and not entered here. The page's 1855 population is not a date of the state.

SHAPE. 19 km circle at Eichstätt 11.18E 48.89N, matching the page's 1,100 km2; the fragments inside Brandenburg-Ansbach are not located. Gazetteer names wanted: 'Eichstätt', 'Hirschberg'.

NOT SETTLED. (1) The page gives the diocese as 746 against 741 in the infobox (irrelevant to the state); (2) the year of the Hirschberg inheritance is not given; (3) 1802 against 1803 for the secularisation.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-halberstadt (Prince-Bishopric of Halberstadt, 1180-1648)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Halberstadt row.

SCOPE. 1180 ('From 1180, the bishops or administrators of Halberstadt ruled a state within the Holy Roman Empire') to the Peace of Westphalia, 1648; the page has no infobox dates. After 1648 it is the Principality of Halberstadt of Brandenburg-Prussia (and in 1815 of the Prussian Province of Saxony); those belong to brandenburg-prussia and kingdom-of-prussia. Other page items are not territorial events of the state: 968 (loss of the eastern half of the diocese to Magdeburg), 1142 (Brunswick passes to Henry the Lion), 1540 (Lutheran), 1623 (Christian of Brunswick resigned), 1821 (merged into the Diocese of Paderborn).

SHAPE. Halberstadt 11.05E 51.90N 25 km; Aschersleben 11.46E 51.76N 12 km. Gazetteer names wanted: 'Halberstadt', 'Aschersleben', 'Hornburg', 'Osterwieck'. The page names Oschersleben, Egeln, Gröningen and Harzburg nowhere.

NOT SETTLED. (1) No area; (2) the page gives no date for any other acquisition; (3) the 'Magdeburg Hochstift war' is not on the page.

COUNTERPARTS NEEDING DOSSIERS: none new (the Aschersleben lands were Anhalt's: principality-of-anhalt, written in this batch).

## prince-abbey-of-fulda (Prince-Abbey of Fulda, 1221-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Fulda row.

SCOPE. 1221 (page and infobox) to 1802 (infobox; the text says the principality was secularised in 1803). The page dates the monastery to 744 (12 March, Saint Sturm), the Prince-Bishopric to 1752, and after 1803: Nassau-Orange-Fulda, the Grand Duchy of Frankfurt (1810), Austrian occupation (1813), Prussian (1815) and the Electorate of Hesse (1815). The page does not mention Hesse-Kassel as a recipient or the Hessian looting dates (Thirty Years' War), so no occupation event is entered.

SHAPE. Gazetteer place 'Fulda' with 25 km. Names wanted: 'Hunfeld', 'Hammelburg', 'Bruckenau' (none on the page).

NOT SETTLED. (1) No area, no towns, no acquisitions; (2) 1220 against 1221 (the page says 1221); (3) the 1802 / 1803 end.

COUNTERPARTS NEEDING DOSSIERS: principality-of-nassau-orange-fulda (1803-1806).

## prince-bishopric-of-trent (Prince-Bishopric of Trent, 1027-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Trent row (the lands sit in Holy Roman Empire Minor States).

SCOPE. 1027 to 1803. The page also dates: the killing of Bishop Adelpreto at Arco (20 September 1172, by the Castelbarco lords); the deposition of the bishops by Frederick II (1236); Margaret Maultasch ceding her lands to Rudolf IV of Austria (1363, Tyrol, not Trent); the war of 1509 with Venice, the peasant war 1525-1526, the bombing of Trent in September 1703 and the Napoleonic invasion of 1796. Under Bishop Clesio (1514-1539) 'the seignory of Castelbarco and Rovereto' was gained, undated; 1516 'reduced the principality to an enclave'; Ferdinand I occupied Rovereto and 'in 1567 [declared] the Confederation Treaty over'. None can be placed within the pages' information, so no region events are entered for them.

NOT SETTLED. (1) No area; (2) the 1511 'perpetual confederate' status is read as a light vassalage and may be only an alliance; (3) the end: the lead says 1803, the infobox the Empire's end in 1806.

COUNTERPARTS NEEDING DOSSIERS: none new (march-of-verona exists).

## prince-bishopric-of-brixen (Prince-Bishopric of Brixen, 1027-1803)
Written 2026-10-25 for batch eu-09-x (1 page plus the Trent page already opened for prince-bishopric-of-trent; budget 1-2). New state: Cliopatria has no Brixen row.

SCOPE. 1027 (imperial immediacy; the infobox 'Prince-Bishopric: 1179' is the title of prince) to 1803. The page notes the Counts of Tyrol 'constantly grew in power' at the bishopric's expense, Duke Frederick IV compelled the bishops to acknowledge his authority (undated), Archduke Sigismund won his struggle with Nicholas of Cusa (undated), the synod of 1080 and a peasants' uprising of 1525 under Bishop Georg III. Bavarian rule after Pressburg (1805), Austria again in 1814.

SHAPES. Brixen 11.66E 46.72N 20 km; Bruneck 11.94E 46.80N 20 km. Gazetteer names wanted: 'Brixen' / 'Bressanone', 'Bruneck', 'Klausen', 'Innichen' (the last two are not on the page's body).

NOT SETTLED. (1) No area; (2) the 1165 loss and the grants to the Tyrol counts are not drawn; (3) the 1511 status is borrowed from the Trent page and may be only an alliance; (4) the page says 'Austria' in the text and 'Tyrol' in the infobox for 1803.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-passau (Prince-Bishopric of Passau, 1217-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Passau row.

SCOPE. The page has no infobox dates; I start at the January 1217 recognition as a prince of the empire (not 739, the seat of the diocese, nor 999, the market privilege) and end at the secularisation of February 1803. Diocese matters on the page are not state events: 1469 (Vienna diocese from Passau territory), 1722, 1784 (Linz bull, 28 January) and 1783-1795 (Joseph II took 'two-thirds of the diocese'), the Peace of Passau (summer 1552), 1189 (Third Crusade).

SHAPE. 20 km circle at Passau. Gazetteer names wanted: 'Passau'. NOT SETTLED: (1) no area and no lands; (2) the page names no town but Passau (Wels, Ybbs, Ilzstadt, Freistadt are not on it); (3) the Bavarian and Salzburg shares of 1803 are not located.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-speyer (Prince-Bishopric of Speyer, 888-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Speyer row.

SCOPE. 888 (infobox 'Gained territory') to 1803. The page's 'Established: 3rd or 4th century' is the diocese. Residences: Speyer to the 14th century, Udenheim from 1371 (text) or 1379 (infobox) to 1723, then Bruchsal. The page gives the French occupation of the 1790s only as the 1801/1802 conquest of the left bank; the 1815 division of the French part between Bavaria and Hesse-Darmstadt is after the state.

SHAPES. Bruchsal-Philippsburg 8.53E 49.18N 15 km; Deidesheim 8.19E 49.41N 9 km; Herxheim 8.20E 49.14N 10 km; Lauterburg 8.18E 48.98N 8 km; Philippsburg 8.46E 49.24N 6 km. Gazetteer names wanted: 'Bruchsal', 'Philippsburg', 'Deidesheim', 'Herxheim', 'Lauterburg'. The page does not name Kirrweiler.

NOT SETTLED. (1) Which left-bank parts were annexed in 1681; (2) the 1801 French conquest is entered at 1801 although the page gives '1801/1802'; (3) the 1371 / 1379 date for Udenheim.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-verden (Prince-Bishopric of Verden, 1180-1648)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Verden row.

SCOPE. 1180 to 15 May 1648 (infobox). After that: the Swedish Principality of Verden (to 1712, 'disestablished'), part of the Duchies of Bremen-Verden; the page does not date the Danish occupation or the 1715 Hanover purchase (the prince-archbishopric-of-bremen dossier of another part covers Bremen). Reformation: Lutheran from 1558, church ordinance of 1568 (Eberhard von Holle); a Catholic bishop returned in 1630 under the Edict of Restitution 'until 1634'.

SHAPE. Circle 15.5 km at 9.30E 53.00N, between Verden and Rotenburg, tuned to the page's 730 km2. Gazetteer names wanted: 'Verden', 'Rotenburg (Wumme)'.

COUNTERPARTS NEEDING DOSSIERS: none new (the Bremen-Verden duchies are in the Bremen dossier's successors).

## prince-bishopric-of-minden (Prince-Bishopric of Minden, 1180-1648)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Minden row.

SCOPE. 1180 (Reichsfreiheit) to 1648 (Peace of Westphalia). After 1648: the Principality of Minden of Brandenburg-Prussia (administered with Ravensberg after 1719), ceded to Westphalia 1807-1814, Prussian again 1814; those steps belong to the Prussian dossiers. The Swedish occupation in the Thirty Years' War is mentioned without a year, so no occupation event.

SHAPE. Minden-Lübbecke circle 8.77E 52.30N 19 km; Hamelin 9.36E 52.10N 8 km (1259-1277). Gazetteer names wanted: 'Minden', 'Lübbecke', 'Hameln'.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-nassau (County of Nassau, 1159-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Nassau row before the Duchy of Nassau (1806-1865).

SCOPE. 1159 (recognition of the title; infobox '1125/1159') to the declaration of the Duchy in 1806. The Walramian and Ottonian lines are kept inside one state. Other dated items on the page, none drawn: the Reichshof Wiesbaden ('end of the 12th century'), Nassau-Hadamar (Elder) to Nassau-Dillenburg in 1394, Diez 'recovered to Nassau-Siegen in 1530', Breda inherited in 1504 by Henry III of Nassau-Dillenburg, Orange after the death of Rene of Chalon in 1544, 'From 1557 he obtained the County of Katzenelnbogen' (no share given), the cession of a part of the county to the Protestant branch in 1648; Nassau-Saarbrucken annexed by France (1797 entry) and Nassau annexed to Prussia in 1866.

SHAPES. Southern circle 8.05E 50.28N 28 km; northern circle 8.20E 50.77N 22 km. Gazetteer names wanted: 'Nassau', 'Weilburg', 'Idstein', 'Wiesbaden', 'Dillenburg', 'Siegen', 'Herborn', 'Haiger'.

NOT SETTLED. (1) No area; (2) the page does not say Idstein was the place of the division; (3) Vianden is assigned to two heirs on the page; (4) war entries: none on the page; (5) the Netherlands estates are Dutch-group matters.

COUNTERPARTS NEEDING DOSSIERS: none new.

## principality-of-anhalt (Principality of Anhalt, 1212-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria's Duchy of Anhalt starts in 1806.

SCOPE. 1212 (Anhalt split off Saxony) to 1806 (elevation of the remaining lines to duchies). All lines are kept in one state: the page's partitions (1252, 1396 Zerbst split with Dessau and Kothen, 1562 Köthen surrendered to Dessau, 1570 reunion, 1603 mini-states, 1665 Köthen extinct, 1793 Zerbst) are dynastic steps. The page also dates Henry I's title (1218), Bernhard as Duke of Saxony (1180), Wolfgang of Köthen co-signing the Augsburg Confession (1530) and being put under the imperial ban after Mühlberg (1547), 'joined Council of Princes: 1582', and the Thirty Years' War ravages (undated); none moves land.

SHAPES. Anhalt 12.00E 51.82N 27 km; Aschersleben 11.46E 51.76N 12 km. The Aschersleben event mirrors the Halberstadt dossier of this batch (whose counterpart name is `principality-of-anhalt`). Gazetteer names wanted: 'Dessau', 'Bernburg', 'Köthen', 'Zerbst', 'Plötzkau', 'Aschersleben'.

NOT SETTLED. (1) The page gives the Aschersleben line's extent no area; (2) no 1252 land per son; (3) the page gives no end year for the principality (it describes the duchies); 1806 is the year the page dates.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-lippe (County of Lippe, 1123-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria's Principality of Lippe starts in 1806.

SCOPE. 1123 (first documentary evidence) to 1806 (a placeholder: the page says nothing of 1806; confidence 1). The infobox 'Established: 1413' is the imperial immediacy date, not the state's start. Other dated items: Lippstadt as a Samtherrschaft with Mark from about the mid-15th century and shared with Brandenburg-Prussia 1666-1850; the partition of 1613 (Lippe-Brake, Lippe-Alverdissen, Lippe-Detmold) and Alverdissen gaining part of Schaumburg in 1644; the Brake line's extinction in 1709; the failed attack on Gemen castle in 1776; the Thirty Years' War losses of population. No area, no war dates on the page.

SHAPES. Lippe 8.90E 51.97N 20 km; Lippstadt 8.34E 51.67N 8 km; Rheda 8.30E 51.85N 8 km; Schwalenberg 9.11E 51.89N 10 km; Sternberg 9.10E 52.05N 10 km. Gazetteer names wanted: 'Detmold', 'Lemgo', 'Lippstadt', 'Blomberg', 'Horn', 'Rheda', 'Schwalenberg'.

NOT SETTLED. (1) The 1123 land; (2) Schwalenberg is entered at 1332 with confidence 1 (a range); (3) Everstein 'fell to Brunswick-Lüneburg' after the feud of 1408 (Lippe's loss is not stated); (4) the 1806 end.

COUNTERPARTS NEEDING DOSSIERS: county-of-schwalenberg, county-of-tecklenburg, county-of-sternberg (small counties; suggested slugs).

## duchy-of-berg (Duchy of Berg, 1101-1423)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Berg row before the Grand Duchy of Berg (1806-1813).

SCOPE. 1101 to 1423, the year duchy-of-julich-berg takes Berg (that dossier's 1423 gain has the same circle and counterpart `duchy-of-berg`). The page continues: Jülich-Cleves-Berg after 1511/1521, the French occupation of Jülich 1794-1801 and annexation 1801, the Grand Duchy of Berg from 15 March 1806 (under Murat) and its end with Napoleon's defeat in 1813; none of that is in this state's life. 1085 and the Dusseldorf Cow War are not dated on the page.

SHAPES. Berg 7.10E 51.10N 28 km; Mark 7.55E 51.52N 31 km (the Mark dossier's circle). Gazetteer names wanted: 'Düsseldorf', 'Solingen', 'Wipperfürth', 'Burg an der Wupper'.

NOT SETTLED. (1) Whether the Altena lands were Berg's from 1101: the page says the territory split in 1160, which I read as one county before; (2) the page's 1348 and 1423 unions: this dossier ends at 1423 as the sibling dossier does; (3) no area.

COUNTERPARTS NEEDING DOSSIERS: none new (county-of-mark and duchy-of-julich-berg are in this batch).

## county-of-mark (County of Mark, 1160-1391)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Mark row.

SCOPE. 1160 to 1391. From 1368 the Count of the Mark also held Cleves (personal union, rule 4); after 1391 the Mark is inside duchy-of-cleves (dissolves 1614 into electorate-of-brandenburg per that dossier). The page also dates: 1807 Tilsit (Mark to France), 1808 Grand Duchy of Berg, 'To Prussia: 1815'. The 1444-1449 Soest feud and the dates of Unna, Iserlohn, Luenen, Hoerde, Luedenscheid and Wetter are not on the page.

SHAPE. 31 km circle at 7.55E 51.52N. Gazetteer names wanted: 'Hamm', 'Altena', 'Unna', 'Iserlohn'.

NOT SETTLED. (1) The Higher Mark gained from Münster in the 14th century (undated); (2) the 1226 capital move is confidence 1; (3) the Worringen opponent is taken from the Berg page.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-ravensberg (County of Ravensberg, 1140-1437)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Ravensberg row.

SCOPE. 1140 to 1437, where duchy-of-julich-berg takes it (the Jülich-Berg dossier's 1437 gain has the same circle and counterpart). The page's later dates are outside this state: 1521 (United Duchies), 1614 (Xanten, to Brandenburg), 1719-1807 (administered within Minden-Ravensberg), 1807 (Tilsit), 'Disestablished: 1810' (the body text and infobox differ). The 'War of the Jülich succession' is named without dates, and the 1647 Westphalia clause is not on the page.

SHAPE. 20 km circle at Bielefeld, 8.53E 52.02N. Gazetteer names wanted: 'Bielefeld', 'Herford', 'Vlotho', 'Halle', 'Borgholzhausen'.

NOT SETTLED. (1) 1346 against 1348 for the union with Berg; (2) the Jülich-Berg dossier's Berg page note 'Berg in union with Ravensberg (except 1404-1437)'; (3) no area.

COUNTERPARTS NEEDING DOSSIERS: none new.

## burgraviate-of-nuremberg (Burgraviate of Nuremberg, 1105-1398)
Written 2026-10-25 for batch eu-09-x (3 pages: its own plus the Ansbach and Bayreuth pages already opened for those dossiers; budget 1-2). New state: Cliopatria has no row for the burgraviate.

SCOPE. 1105 (infobox, House of Raabs) to 21 January 1398 (death of Frederick V, from the Ansbach and Bayreuth pages, whose dossiers found their principalities that day). The Burgraviate page itself dates the partition to 1440 and the sale of the burgraviate to the city (except the Blutgericht) to 1427/1440 (infobox '1427 1440'); the page also says Frederick VI was 'Margrave of Brandenburg-Kulmbach from 1420', 'Elector of Brandenburg from 1415, Margrave of Brandenburg from 1417', so the later steps are the Hohenzollern margraviates. The 1398 end follows the two principality pages; the 1440 date is flagged here.

SHAPES. The union of the Ansbach and Bayreuth circles. The page gives no town but Nuremberg. Gazetteer names wanted: 'Nuremberg' (circle not drawn), 'Cadolzburg' (not on the page).

NOT SETTLED. (1) 1398 against 1440 for the partition; (2) the burgraviate's land in 1105 and 1192; (3) 1427 against 1440 for the sale of the office; (4) no area; (5) the Second Margrave War, the 1388 Städtekrieg and the 1449 conflict are not on the page.

COUNTERPARTS NEEDING DOSSIERS: none new.

## free-imperial-city-of-nuremberg (Free Imperial City of Nuremberg, 1219-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Nuremberg row (the city sits in Holy Roman Empire Minor States and, after 1806, in the Kingdom of Bavaria).

SCOPE. 1219 to 8 September 1806 (the date the page gives for the handover to Bavaria after the Confederation of the Rhine of 12 July 1806). Page items not turned into events: the Second Margrave War of 1552 (Nuremberg tried to buy neutrality for 100,000 guilders; Albrecht Alcibiades 'attacked the city without declaring war and forced the conclusion of a disadvantageous peace', no separate year), 1632 (the city 'occupied by the forces of Gustavus Adolphus of Sweden' besieged by Wallenstein; no end date), 1790/91 (Charles Theodore's Bavarian Sequestrations of the Landshut lands) and 1796 (Prussia 'claimed and occupied part of the territory'; no end date and no land named).

SHAPES. Nuremberg 11.08E 49.45N with 8 km (to 1426), 12 km (1427-1503) and 19.5 km (1504-1805). Gazetteer names wanted: 'Nuremberg', 'Lauf', 'Hersbruck', 'Altdorf', 'Wohrd'.

NOT SETTLED. (1) The page's two areas (about 1,200 km2 and '25 sq mi (65 km2)' of Landshut gains); (2) the infobox lists the Großen Freiheitsbrief next to 1427, a formatting error against the body's 1219; (3) the counterparts of the 1504 gain; (4) the extent of the 1790s losses.

COUNTERPARTS NEEDING DOSSIERS: none new.

## free-imperial-city-of-ulm (Free Imperial City of Ulm, 1181-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Ulm row.

SCOPE. 1181 (infobox) to 1802 (text; the infobox says 1803). Further steps on the page: 'ceded to Kingdom of Württemberg in 1810' (infobox 1809), the Swabian Leagues which the city led several times in the 14th-15th centuries (no years), and the Truce of Ulm of 1647 in the Thirty Years' War. The page names no village or town of the Landgebiet, and dates no acquisition (Lauterbach 1377, Geislingen 1396 and Blaubeuren are not on it).

SHAPE. 15.8 km circle at Ulm, tuned to 780 km2. Gazetteer names wanted: 'Ulm'.

NOT SETTLED. (1) 1181 against 1155; (2) 1802 against 1803 and 1809 against 1810; (3) the early district.

COUNTERPARTS NEEDING DOSSIERS: none new.

## free-imperial-city-of-cologne (Free Imperial City of Cologne, 1288-1796)
Written 2026-10-25 for batch eu-09-x (the Cologne article, which the site serves under 'Free Imperial City of Cologne', plus the Worringen page already opened for electorate-of-cologne; budget 1-2). New state: Cliopatria has no Cologne city row.

SCOPE. 5 June 1288 (independence of the city after Worringen; the Cologne page: 'after the Battle of Worringen in 1288') to the annexation by France on 28 May 1796 (the page's sentence; the Cologne dossier of this batch, electorate-of-cologne, has the archbishop's lands French from 1794 and annexed in 1801 by Lunéville). The page's 1475 formal status date is a rename. The Cologne War (1583-1588) and the Thirty Years' War are mentioned without dates; no war entries. The page is the article on the city of Cologne in general (100,000 characters, read to the 100,000th character), so no territory beyond the city and Deutz is known.

SHAPE. 12 km circle at 6.96E 50.94N. Gazetteer names wanted: 'Köln' / 'Cologne' (resolves as a place), 'Deutz'.

NOT SETTLED. (1) The city-state's extramural territory; (2) 1796 (this page) against 1801 (the mediatisation page used in the Cologne dossier); (3) the exact day of the 1794 occupation.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-henneberg (County of Henneberg, 1037-1583)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Henneberg row.

SCOPE. The infobox span is c. 1037-1660; the county's last count died in 1583, and 1583-1660 is a Wettin condominium, so the state ends at 1583 with the Saxon rows as counterpart (flagged at confidence 2). Other dated items, all inside the circle: Ilmenau purchased 1343, Meiningen (a Würzburg fief) acquired 1542, the 1554 inheritance treaty with John Frederick II of Saxony. The 1815 passage of the Albertine parts round Schleusingen and Suhl to Prussia's Province of Saxony is after the state. Counterpart years for Schmalkalden are those of the Henneberg page; the Hesse-Kassel named there is the landgraviate-of-hesse of the time.

SHAPES. Main circle 10.65E 50.55N 28 km; Coburg 10.96E 50.26N 12 km; Schmalkalden 10.45E 50.72N 10 km. Gazetteer names wanted: 'Schleusingen', 'Meiningen', 'Suhl', 'Schmalkalden', 'Römhild', 'Coburg', 'Ilmenau'.

NOT SETTLED. (1) The 1037 start has no event on the page; (2) no area; (3) the page's 1353 and 1291 Coburg dates are not on it (the 1347 transfer is); (4) the War of the Thuringian Succession is named without dates.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-waldeck (County of Waldeck, 1180-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria's Principality of Waldeck and Pyrmont starts in 1806.

SCOPE. 1180 to 1806 (a placeholder: the page says only that Waldeck joined the Confederation of the Rhine in 1807). Later dates on the page, outside the state: 1849 (legal union of Waldeck and Pyrmont), 1866 and 1870 wars, 1918 (monarchy abolished, 13 November) and 1929 (statehood abolished, 1 April). Lines: 1397 two lines, 1486 Wildungen and Eisenberg, Landau ended 1495; the Eisenberg line inherited Culemborg in 1639. Waldeck supplied a battalion to Britain in 1775-1783.

SHAPES. Waldeck 8.90E 51.25N 18.9 km; Pyrmont 9.25E 51.99N 8 km. Gazetteer names wanted: 'Korbach', 'Arolsen', 'Bad Wildungen', 'Pyrmont'.

NOT SETTLED. (1) 1625 against 1626 for Pyrmont; (2) the page's capital is not stated; (3) the 1806 end year.

COUNTERPARTS NEEDING DOSSIERS: county-of-pyrmont (small; suggested slug).

## county-of-mansfeld (County of Mansfeld, 1069-1580)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Mansfeld row.

SCOPE. Infobox 1069-1580. The county joined the Upper Saxon Circle in 1512 as an immediate Imperial estate; the lines Hinterort, Mittelort and Vorderort (15th century, tables 1540 and 1560-1580) are kept inside one state; Mittelort and Hinterort died out in 1602 and 1666 and the Vorderort line in 1780 ('their fiefs fell back to the Electorate of Saxony and the Prussian Duchy of Magdeburg'). The Peasants' War of 1525 and Frankenhausen (Albert VII on the imperial side) are named without a boundary effect. The Mansfeld Feud of 1479 and the Hettstedt, 1420 and 1501 items are not on the page.

SHAPES. Mansfeld 11.50E 51.55N 22 km; Heldrungen 11.27E 51.30N 8 km; Allstedt 11.39E 51.40N 8 km. Gazetteer names wanted: 'Mansfeld', 'Eisleben', 'Heldrungen', 'Allstedt', 'Artern'.

NOT SETTLED. (1) No area, no capital; (2) the end: 1579 (confiscation) against 1580 (footnote); (3) the share of the Archbishopric of Magdeburg in 1580 is not drawn; (4) the Bohemian possessions (Dobris, 1630) are outside.

COUNTERPARTS NEEDING DOSSIERS: none new (archbishopric-of-magdeburg exists).

## county-of-hoya (County of Hoya, 1202-1582)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Hoya row.

SCOPE. 1202 to 1582 (the page's infobox ends 'Part of Prussia: 1866'; the county was absorbed in 1582). Not drawn: the Hodenberg estates (to 1313), Brunswick-Lüneburg's occupation of estates in 1512 (no end, no land named), the Hesse-Cassel and Lüneburg shares of 1582 (not located; Brunswick's dossier draws the whole 25 km circle as the Calenberg gain).

SHAPES. Hoya 9.15E 52.80N 15 km; Nienburg 9.20E 52.64N 25 km. Gazetteer names wanted: 'Hoya', 'Nienburg (Weser)'.

NOT SETTLED. (1) No area; (2) Upper and Lower Hoya are not on the page; (3) the 1582 shares.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-diepholz (County of Diepholz, 1070-1585)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Diepholz row; the Brunswick-Luneburg dossier named it as a counterpart.

SCOPE. Infobox 'ca. 1070/1085-1585'; the start year 1070 is the infobox's first figure and is confidence 1 (the page is silent on a founding act). The page gives no capital (the field is blank), so none is entered.

SHAPES. Two 12 km circles at 8.37E 52.74N and 8.37E 52.50N (about 870 km2) for the sixteenth-century extent (47 km by 22 km); Sudholte circle 8.45E 52.69N 12 km; Auburg stand-in 8.55E 52.55N 6 km. Gazetteer names wanted: 'Diepholz', 'Barnstorf', 'Goldenstedt', 'Drebber', 'Lemforde', 'Colnrade', 'Auburg'.

CONFLICT WITH THE BRUNSWICK DOSSIER. This page ends the county in 1585 (lead 'until 1585'; Friedrich II 'died in 1585'); the Calenberg page cited in duchy-of-brunswick-luneburg says 'acquired Diepholz in 1584'. The two years are left as each page gives them. The page also says the sovereignty ceded in 1521 was 'that had not already been abdicated to the Dukes of Brunswick-Calenberg', which sits oddly with the 1510 abdication to Brunswick-Luneburg.

NOT SETTLED. (1) The founding year; (2) where Auburg lay; (3) the extent before the sixteenth century; (4) the Bronkhorst claim of 1553 is a claim only; (5) the 1441 dowry (Wagenfeld, Bokel, Struten) has no counterpart on the page.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-freising (Prince-Bishopric of Freising, 1294-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Freising row.

SCOPE. The state starts at 1294, the year the page makes the bishop a prince and an imperial estate; the earlier acquisitions are drawn inside the first keyframe. The Thirty Years' War is named ('it paid the ransom demanded by the Swedish King Gustavus Adolphus in 1632', Swedes again in 1646); the page names no battle or treaty, so no war entry and no occupation event is written. The 1821 absorption of the diocese into the Archdiocese of Munich and Freising is after the state.

SHAPES. Circles: Freising 11.75E 48.40N 14 km; Werdenfels 11.10E 47.49N 14 km; Innichen 12.28E 46.735N 7 km; Bischoflack 14.31E 46.165N 14 km; Wolz and Katsch 14.2E 47.15N 12 km. Burgrain (808) and the Yserrain towns are named without a place and are not drawn. Gazetteer names wanted: 'Freising', 'Garmisch-Partenkirchen' (Werdenfels), 'Innichen', 'Skofja Loka' (Bischoflack), 'Oberwolz'.

NOT SETTLED. (1) The Yserrain sale: 'Duke Ludwig of Bavaria sold several towns along the Isar River to the bishop', a few years after 1294, no year; (2) Werdenfels is 'late 13th century' with no year, so it sits inside the 1294 keyframe; (3) who took Innichen and Cadore in 1802 is not on the page; (4) no area.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-worms (Prince-Bishopric of Worms, 861-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Worms row.

SCOPE. The start year 861 is the infobox's 'Gained Reichsfreiheit', confidence 2: the page names no land or counterpart for it, and an imperial-immediacy year of 861 for a prince-bishopric is the page's figure only. The Worms massacre of 1096 is a massacre, not a war (Bishop Adalbert II 'attempted to protect the city's Jewish community'). The page is silent on wars and on the Palatinate's enclosure beyond 'largely surrounded by the Electorate of the Palatinate'.

SHAPES. Worms-left-bank circle 8.36E 49.63N 12 km (too large: it holds the city, which was not the bishop's); Ladenburg circle 8.61E 49.47N 9 km. Gazetteer names wanted: 'Ladenburg' (Worms resolves, to a one-cell point).

NOT SETTLED. (1) No area, no town list; (2) the left bank was 'occupied and annexed' in 1795, and the formal cession date is not on the page; (3) the Palatinate shows as predecessor in the infobox on a reading that is not clear, so the Empire is entered.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-bishopric-of-lubeck (Prince-Bishopric of Lübeck, 1180-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Lübeck bishopric row (the Free City of Lübeck is a separate state in polities.csv).

SCOPE. The state starts at 1180, the year the page gives the bishopric imperial status after the fall of Henry the Lion, confidence 2 (the land is only an area). The page's other dated items: dioceses of Ratzeburg and Schwerin split off 1052; the seat moved from Oldenburg to Lübeck 'in 1160' (body) or 1180 (infobox); the city of Lübeck gained imperial immediacy in 1226; the diocese 'Joined Lower Saxon Circle: 1500' (an association, not territory); the principality was enlarged by Ahrensbok 'in 1867'; annexed to France 1810-14; joined Prussia's Schleswig-Holstein 1937. All after 1803 are after the state. The Peace of Westphalia is named (Lübeck 'one of only two Protestant prince-bishoprics') without a war entry.

SHAPES. Eutin circle 10.62E 54.14N 13.1 km (541 km2). Gazetteer names wanted: 'Eutin', and 'Lübeck' if absent.

NOT SETTLED. (1) The territory was in several parts, and the page names none; (2) 1160 against 1180 for the move to Lübeck; (3) no wars.

COUNTERPARTS NEEDING DOSSIERS: none new (the stem duchy of Saxony is a Cliopatria row; county-of-oldenburg is this batch's dossier for Oldenburg to 1805).

## county-of-schwerin (County of Schwerin, 1161-1368)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Schwerin row; the Mecklenburg dossier names county-of-schwerin as the counterpart of its 1358 gain.

CONFLICT. This page ends the county in 1368 (infobox; the Treaty of Pluschow on 7 December 1368); the page behind the Mecklenburg dossier says Albrecht 'acquired the former County of Schwerin in 1358'. Both are kept as each page gives them. The infobox also names 'Henry IV' where the body names Albrecht II. The 1471 date is the reunion of the lands of the county into the duchy, after the state.

SHAPES. Place circle Schwerin, 25 km (the gazetteer resolves Schwerin). Page silent on area, towns and on Pribislav's mainland ('Henry returned the other conquered lands to Nikolot's son, Pribislav', no year).

NOT SETTLED. (1) No area or town list; (2) the 1358 against 1368 sale; (3) no vassalage or wars on the page.

COUNTERPARTS NEEDING DOSSIERS: none new.

## principality-of-rugen (Principality of Rügen, 1168-1325)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Rügen row; the Pomerania dossier names principality-of-rugen as the counterpart of its 1325 gain.

SCOPE. 1168 to 1325 as in the lead and the infobox. The Rani were a tribe, not a state, so there is no predecessor. Wars named without a state-sized stake and not entered: the Battle of Bornhoved in 1227 (the Danes 'again lost all Wendish lands except for Rügen'), a Danish and Rani victory over the Pomeranian navy in the Bay of Greifswald in 1184, Rugian troops in Danish raids and conquests (1177, 1219, 1259), the destruction of Stralsund in 1249 and its siege in 1316 by Duke Eric I of Saxe-Lauenburg, and the two Rugian inheritance wars with Mecklenburg after 1325 (no dates). After the state: Danish attempts to reacquire Rügen (1625 offer) and Danish occupations (1675-79, 1715-21) belong to Swedish Pomerania.

SHAPES. Island circle 13.40E 54.42N 20 km; mainland circle 13.0E 54.25N 14 km; Wolgast 13.77E 54.05N 10 km; Loitz 13.12E 53.97N 12 km; Schlawe 16.68E 54.36N 14 km. Gazetteer names wanted: 'Bergen auf Rügen', 'Garz', 'Loitz', 'Wolgast', 'Slawno' (Schlawe).

NOT SETTLED. (1) No area; (2) 1273 or 1275 for Loitz; (3) the date Wolgast was lost ('before 1250'); (4) the 1240 Ryck boundary says where Pomerania began and not what changed; (5) the infobox's 'Acquired by Swedish Pomerania: 1648' is after the state.

COUNTERPARTS NEEDING DOSSIERS: none new (the Rani are a tribe).

## duchy-of-saxe-lauenburg (Duchy of Saxe-Lauenburg, 1296-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Saxe-Lauenburg row.

SCOPE. The page says the duchy 'existed from 1296 to 1803 and again from 1814 to 1876'. This dossier covers the first existence, to 1803, the project's era; the second (1814-76: Hanover, Prussia, Sweden, Denmark, then the Prussian district) is not entered, and the successor named is Prussia. The page's 1803 end is its lead only: nothing dated 1803 is described except the French occupation 1803-05, so the dissolve is confidence 1.

Items on the page left out of the ledger: Danish conquest 1203 and reversion to Albert I of Saxony 1227 (before the state); the election of two kings in 1314; the 1401 succession of Eric IV; the Thirty Years' War (Augustus 'always remained neutral'); the 1689-93 succession conflict between Celle and Danish Holstein (no war entry: the page names no battle); the 1731 cession of Hadeln to Bremen-Verden.

SHAPES. Circles: heartland 10.70E 53.55N 22 km; Darzing 10.90E 53.28N 12 km; Hadeln 8.85E 53.66N 15 km; Bergedorf 10.20E 53.48N 12 km; Steinhorst 10.50E 53.62N 6 km. Gazetteer names wanted: 'Ratzeburg', 'Lauenburg/Elbe', 'Neuhaus', 'Otterndorf' (Hadeln), 'Bergedorf', 'Geesthacht', 'Steinhorst'.

NOT SETTLED. (1) No area; (2) the 1370 pawn is not a loss (the land is drawn to 1419); (3) Bergedorf's 1370-1420 status; (4) the Hamburg settlement of 1693 is a dynastic step; (5) the 1803 end.

COUNTERPARTS NEEDING DOSSIERS: none new (free-city-of-lubeck and stem-duchy-of-saxony are Cliopatria rows).

## county-of-oettingen (County of Oettingen, 1147-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Oettingen row.

SCOPE. The page covers a family and its partitions (Oettingen-Oettingen, -Wallerstein, -Spielberg, -Baldern, -Katzenstein); they are kept inside one state (rule 2). The start year 1147 is the first documentary mention, confidence 1. The page is silent on wars. The imperial ban of May 1310 against a count over a dispute with the Prince-Bishopric of Eichstatt ('which stripped him of his property') names no land and is not entered.

SHAPES. A single circle at 10.55E 48.90N, 16.4 km (850 km2) for 1806; The gazetteer has neither Oettingen nor Nördlingen, hence the coordinate circle. Gazetteer names wanted: 'Oettingen in Bayern', 'Nördlingen', 'Wallerstein', 'Harburg', 'Spielberg'.

NOT SETTLED. (1) No early area; (2) the page's dates conflict: Wallerstein 1418 or 1423, Baldern extinct 1789 (text) or 1798 (infobox), the principality 1674, 1734 or 1774; (3) the 1810 split with Württemberg; (4) who held the lands in the 13th and 14th centuries beyond 'the largest secular territory in East Swabia'.

COUNTERPARTS NEEDING DOSSIERS: none new.

## prince-provostry-of-berchtesgaden (Prince-Provostry of Berchtesgaden, 1194-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Berchtesgaden row.

SCOPE. The infobox span is 1194-1803. The page names no capital, area or acquisition dates ('a number of estates further afield'). 1802/1803 are both on the page for the secularisation; the dossier ends at 1803 (the infobox). The occupation of 1611 is a one-year episode (start and end the same year; the page gives no month).

SHAPES. A 12 km circle at 13.00E 47.63N. Gazetteer names wanted: 'Berchtesgaden'.

NOT SETTLED. (1) No area; (2) 1802 against 1803; (3) the page lists no wars apart from 1611.

COUNTERPARTS NEEDING DOSSIERS: none new.

## princely-abbey-of-corvey (Princely Abbey of Corvey, 826-1803)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Corvey row.

SCOPE. The page is the article of the abbey. The state starts in 826, 'an independent abbey' (confidence 2: the page names no secular territory), and ends in 1803, when 'Corvey had ceased to exist as a political state'. The page gives the imperial status only as 'from the Late Middle Ages' (no year); it lists a 1265 attack on the town of Corvey by Hoxter and the Bishop of Paderborn ('their troops destroyed the town of Corvey') and the 1634 sack by imperial troops, neither with land at stake, so no war or occupation entry. After the state: 1807 Kingdom of Westphalia, 1815 Prussia, 1820 Victor Amadeus of Hesse-Rotenburg, 1834 Victor von Hohenlohe-Schillingfurst.

SHAPES. A 15 km circle at 9.40E 51.78N. Gazetteer names wanted: 'Hoxter', 'Corvey'.

NOT SETTLED. (1) No area; (2) the imperial-immediacy year; (3) the successor Nassau-Orange-Fulda had no Cliopatria row (a dossier is wanted).

COUNTERPARTS NEEDING DOSSIERS: principality-of-nassau-orange-fulda (1803-1806).

## quedlinburg-abbey (Quedlinburg Abbey, 936-1802)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Quedlinburg row.

SCOPE. An abbey of secular canonesses and an Imperial Estate whose abbess 'had a seat and voice at the Imperial Diet'. The page's dated gifts: Soltau 936, the church of Saint Michael 956, Duderstadt 974, Potsdam 3 July 993 (deed of Otto III), Gera 999 ('the provincia of Gera came into the hands of the abbey'; in 1209 'the abbess appointed the Vogte of Weida as administrators of the territory'). Potsdam and Gera are not drawn: the page dates no loss for them, and they would otherwise stay drawn for centuries. 'Later acquisitions totalled more than 150 estates.' The 1802/3 disestablishment is given as two years; 1802 is used (as the Quedlinburg row ends the abbey), with confidence 2. The page's disputes with the Bishops of Halberstadt carry no years.

SHAPES. Quedlinburg 11.15E 51.79N 8 km; Duderstadt 10.25E 51.51N 6 km. Gazetteer names wanted: 'Duderstadt'.

NOT SETTLED. (1) No territory; (2) the loss of Duderstadt (derived, 1236); (3) the page's end years.

COUNTERPARTS NEEDING DOSSIERS: none new.

## principality-of-hohenzollern-hechingen (Principality of Hohenzollern-Hechingen, 1576-1850)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Hechingen row.

SCOPE. The page is silent on wars and on any territory change between 1576 and 1849. The Swabian County of Hohenzollern before 1576 is not written: the page opened for it (County_of_Hohenzollern) is the dynasty's article, with the Franconian and Brandenburg lines mixed in and no clear county period. Items on it: Graf title 1111, county from 1204/1218, Hohenberg held to 1486, Haigerloch sold to Austria in 1381, Sigmaringen and Veringen received as imperial fiefs in 1535, castle destroyed in 1423. The three Swabian branches (Hechingen, Haigerloch, Sigmaringen) date from 1576; Haigerloch was integrated into Sigmaringen in 1634-81 and again after 1767.

SHAPES. A 10 km circle at 8.97E 48.35N. Gazetteer names wanted: 'Hechingen'.

NOT SETTLED. (1) No area; (2) the county before 1576; (3) the Hohenzollern-Sigmaringen row of Cliopatria begins at 1806 and is another group's.

COUNTERPARTS NEEDING DOSSIERS: none new.

## duchy-of-schleswig (Duchy of Schleswig, 1058-1866)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 1-2). New state: Cliopatria has no row for the Duchy of Schleswig. The Duchy of Holstein (Cliopatria 1848-52) belongs to eu-20; its pre-1848 life is not written by this batch.

SCOPE. 1058 to 1866 as the infobox gives; the page is silent on the founding event, so confidence 1. The fief to Denmark is entered at the start year (confidence 1) and ended in 1864. Danish slugs: Cliopatria's kingdom-of-denmark row ends 1406 and denmark-norway covers 1526-1940; the string kingdom-of-denmark is used throughout for pairing. Items on the pages not entered: the Treaty of Heiligen 811 and Conrad II's border at the Eider 1027 (before the state); the 1230s appanage; 1713 (Danish royal troops conquered the estates of the Gottorp dukes in Schleswig) and the 1720 Treaty of Frederiksborg (ceded to Denmark); the First Schleswig War 1848-52 (not a war entry: Schleswig-Holsteiners' rebel government, disbanded 1851; the London Protocol of 1852); 1920 plebiscites after the state.

SHAPES. Polygon [[8.6,54.28],[9.95,54.28],[9.95,55.45],[8.6,55.45]] intersected with Schleswig-Holstein plus Syddanmark. About 12,000 km2 in gazetteer cells against the page's extent of 130 km north-south. The gazetteer's own 'Schleswig' region is a coarser reading of the same land.

NOT SETTLED. (1) The founding event; (2) when the fief began; (3) Als, Fehmarn and the Gottorp parts are not drawn separately; (4) the Danish rows' date ranges.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-zutphen (County of Zutphen, 1046-1138)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Zutphen row; the Guelders dossier named county-of-zutphen as the counterpart of its 1127 gain.

SCOPE. The infobox runs the county 1046-1581 (a personal union with Guelders from 1138); the state is ended at 1138 here, when the counts' own rule ends, because the Guelders dossier draws the land inside Guelders afterwards (rule 4: a personal union is never territory). The page's timeline table gives 'Duchy of Guelders (1046-1543)', which conflicts with the infobox's 1339-1581. The page is silent on wars.

SHAPES. A single 18 km circle at 6.20E 52.14N. Gazetteer names wanted: 'Zutphen'.

NOT SETTLED. (1) 1127 (Guelders dossier) against 1138 (this page); (2) no area; (3) the Utrecht fief 'until 1182'.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-montbeliard (County of Montbéliard, 1042-1444)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Montbéliard row; the Wurttemberg dossier named county-of-montbeliard as a counterpart for other groups.

SCOPE. The page runs the county on to 1793 (occupied by the First French Republic in November 1793, ceded 1796), but the page also says it 'was not a vassalage of Wurttemberg'. This dossier ends the state at 1444, when Wurttemberg took it, because the Wurttemberg dossier draws Montbéliard inside Wurttemberg from 1444 to 1793 ('drawn as Wurttemberg throughout') and a second shape would put two states on one land. Later items on the page, for the reviewer: raised to duchy 1495 (the Principality of Montbéliard); separated for Ludwig Frederick in 1617 and 'fell back to Wurttemberg in 1723'; the 'Four Lands' annexed by Louis XV in 1748; occupied by France in 1793 (forty townships and Mandeure annexed, linked to Haute-Saone); Wurttemberg renounced all rights in 1796; the cantons went to the department Mont-Terrible in 1797, to Haut-Rhin in 1800 and Montbéliard to Doubs in 1814. The only war on the page is the War of the First Coalition in 1796.

SHAPES. A 20 km circle at 6.80E 47.51N. Gazetteer names wanted: 'Montbéliard'.

NOT SETTLED. (1) No area; (2) the end at 1444 is a modelling choice, not the page's; (3) the 1450s-1480s annexation by Eberhard V is undated beyond that range.

COUNTERPARTS NEEDING DOSSIERS: none new.

## principality-of-nassau-orange-fulda (Principality of Nassau-Orange-Fulda, 1803-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no row for Nassau-Orange-Fulda; the Fulda, Corvey and Nassau-related dossiers of this batch name it as a counterpart.

SCOPE. 25 February 1803 to 27 October 1806 (infobox). The prince-abbey of Fulda ends in 1802 in its own dossier (Prussian occupation of October 1802, William Frederick in Fulda on 6 December 1802), so the land has no entry in 1802-03. The four divisions (Fulda, Corvey, Dortmund, Weingarten) appear on the page only as a list; areas, populations and towns are not given.

SHAPES. Fulda 25 km (gazetteer place, country Germany); Corvey 9.40E 51.78N 15 km (as in princely-abbey-of-corvey); Dortmund 12 km (place); Weingarten 9.64E 47.81N 10 km; Dietkirchen 8.05E 50.38N 6 km. Gazetteer names wanted: 'Weingarten', 'Dietkirchen' (Limburg an der Lahn).

NOT SETTLED. (1) The giver for Dortmund, Weingarten and Dietkirchen is not on the page; (2) the page does not say which of Berg and Nassau took which Nassau territory; (3) no area; (4) the Dortmund, Corvey and Fulda dispositions of 1807-1815 are after the state.

COUNTERPARTS NEEDING DOSSIERS: none new (Dortmund, Weingarten and Dietkirchen are free text).

## duchy-of-saxe-weimar (Duchy of Saxe-Weimar, 1572-1805)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 1-3). New state: Cliopatria's Saxon-duchy rows begin in 1806 (Saxe-Weimar-Eisenach 1806-70, Saxe-Altenburg 1806-70), so the pre-1806 Ernestine duchies have no row.

SCOPE. 1572 (Division of Erfurt) to 1805; the page's merger year 1809 is shortened to the start of Cliopatria's row (as the Mecklenburg dossier does). Saxe-Eisenach (1596-1638, 1640-44, 1662-1809) is intermittent and is not written: the Eisenach lands are drawn here only for 1638-39 and 1644-61 and then they go out. In 1741 'Duke Ernest Augustus I of Saxe-Weimar ... inherited Saxe-Eisenach; he then ruled both duchies in personal union' until 1809: rule 4, a personal union is never territory, so no event is entered and the Eisenach land is not drawn inside Weimar for 1741-1805. Other dates: 1547 loss of the electoral dignity by John Frederick I (Capitulation of Wittenberg), the 1566 Grumbach revolt, the 1620 Battle of White Mountain, the 1635 Peace of Prague, 1758 regency of Anna Amalia, 1806 Battle of Jena-Auerstedt: none changes land, and no war entry is written.

SHAPES. Weimar 11.33E 50.98N 22.6 km (1,612 km2, the page's 1800 area); Altenburg 12.43E 50.99N 20 km; Gotha 10.72E 50.95N 20 km; Eisenach 10.32E 50.98N 18 km; Jena 11.59E 50.93N 12 km. Gazetteer names wanted: 'Weimar', 'Altenburg', 'Gotha', 'Eisenach', 'Jena'.

NOT SETTLED. (1) The Weimar page puts both Jena and Eisenach at 1672, the Eisenach page puts Eisenach at 1662 (Weimar loss entered at 1662); (2) the shares of 1644; (3) the lands of 1572; (4) the page's typo 'Johann II (1602-1505)'.

COUNTERPARTS NEEDING DOSSIERS: Saxe-Eisenach (intermittent), Saxe-Altenburg (1603-1672), Saxe-Jena (1672-1690), grand-duchy-of-saxe-weimar-eisenach is a Cliopatria row.

## duchy-of-saxe-gotha-altenburg (Duchy of Saxe-Gotha-Altenburg, 1640-1826)
Written 2026-10-25 for batch eu-09-x (2 pages; budget 1-3). New state: Cliopatria has no pre-1806 Saxon-duchy rows.

SCOPE. The state starts with Saxe-Gotha in 1640 and ends in 1826, when the arbitration of the King of Saxony redistributed the lands (the line was extinct in 1825). Cliopatria's saxe-altenburg (1806-70) and saxe-coburg-and-gotha (1836-39) rows overlap the last twenty years, and the reviewer should decide which side carries 1806-26. The page is silent on wars; the 1675 division and the five other shares of 1680 (Coburg, Meiningen, Romhild, Eisenberg, Hildburghausen) are not named on the Gotha page; the Coburg-Saalfeld page names Saalfeld alone.

SHAPES. Gotha 10.72E 50.95N 20 km; Altenburg 12.43E 50.99N 20 km; Saalfeld 11.37E 50.65N 12 km; Coburg 10.96E 50.26N 10 km; Eisenberg 11.90E 50.97N 10 km. About 3,140 km2 for the 1707 shape. Gazetteer names wanted: 'Gotha', 'Altenburg', 'Saalfeld', 'Coburg', 'Eisenberg (Thuringia)'.

NOT SETTLED. (1) 1672 or 1675 for Altenburg; (2) the unnamed territories of 1699 and 1707; (3) the 1826 redistribution is stated in two sentences only; (4) the Coburg page's infobox gives 11 February 1826 and its text 12 November 1826.

COUNTERPARTS NEEDING DOSSIERS: Saxe-Altenburg (1603-1672 and after 1826), Saxe-Hildburghausen, Saxe-Meiningen and the other 1680 duchies.

## duchy-of-saxe-coburg-saalfeld (Duchy of Saxe-Coburg-Saalfeld, 1680-1826)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-3). New state: Cliopatria has no pre-1836 Saxe-Coburg row.

SCOPE. 1680 (Saxe-Saalfeld) to 1826, when the duchy lost Saalfeld and gained Gotha; the page's lead calls the line 'established in 1699'. A 1811 border treaty with Bavaria swapped four villages each way (Furth am Berg, Hof an der Steinach, Niederfullbach, Triebsdorf to Coburg; Gleussen, Buch am Forst, Herreth and a mill to Bavaria) and is not drawn. The page: the Principality 'underwent from 1773 onwards a forced management of debts by an Imperial Debit Commission until 1802'. Wars: Frederick Josias fought in the Austro-Turkish War and the War of the First Coalition (no years), and the Principality fought on the Allied side in 1813; no war entries.

SHAPES. Saalfeld 11.37E 50.65N 12 km; Coburg 10.96E 50.26N 10 km; Lichtenberg 7.12E 49.47N 15 km. Gazetteer names wanted: 'Saalfeld', 'Coburg', 'St. Wendel' (Lichtenberg).

NOT SETTLED. (1) The page's 1699 date; (2) the 1735 shares (Sonneberg, Neuhaus am Rennweg to Meiningen; Sonnefeld to Hildburghausen; one-third of Romhild and five-twelfths of Themar stayed with Coburg); (3) 11 February against 12 November 1826; (4) Cliopatria's Saxe-Coburg and Gotha row starts in 1836 and leaves 1826-36 empty.

COUNTERPARTS NEEDING DOSSIERS: Saxe-Meiningen before 1820 and Saxe-Hildburghausen.

## duchy-of-saxe-weissenfels (Duchy of Saxe-Weissenfels, 1656-1746)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Saxe-Weissenfels row.

SCOPE. A secundogeniture of the Albertine Wettins: Imperial State and 'member of the Upper Saxon Circle, though without a vote in the Reichstag'. The page is silent on wars; the 1635 Peace of Prague is the only treaty named. The infobox's predecessor and successor fields are garbled on the page, so the Electorate of Saxony is entered from the text.

SHAPES. Circles: Weissenfels 11.97E 51.20N 20 km; Querfurt 11.60E 51.38N 12 km; Jüterbog 13.07E 51.99N 10 km; Dahme 13.43E 51.87N 8 km; Burg 11.85E 52.27N 8 km; Barby 11.88E 51.99N 10 km. Gazetteer names wanted: 'Weissenfels', 'Querfurt', 'Jüterbog', 'Dahme (Mark)', 'Burg bei Magdeburg', 'Barby'.

NOT SETTLED. (1) The years of Querfurt, Jüterbog, Dahme and Burg (entered at the start, confidence 1); (2) no area; (3) the Brandenburg slug for 1687 is the electorate's dossier.

COUNTERPARTS NEEDING DOSSIERS: none new (County of Barby is free text).

## duchy-of-saxe-merseburg (Duchy of Saxe-Merseburg, 1657-1738)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Saxe-Merseburg row.

SCOPE. An Albertine secundogeniture, 1657 to 1738. The estates of the former Bishopric of Merseburg ('secularised in 1565' in one sentence, 1562 in another) and Lower Lusatia are named without years of acquisition, so the first keyframe holds both. The page is silent on wars. The infobox's predecessor and successor fields are garbled on the page.

SHAPES. Merseburg 11.99E 51.36N 28 km; Lubben 13.90E 51.94N 22 km. Gazetteer names wanted: 'Merseburg', 'Lübben'.

NOT SETTLED. (1) No area; (2) 1562 against 1565 for the secularisation of the bishopric; (3) the Spremberg and Bad Lauchstadt appanages are named without dates.

COUNTERPARTS NEEDING DOSSIERS: none new.

## duchy-of-saxe-zeitz (Duchy of Saxe-Zeitz, 1657-1718)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Saxe-Zeitz row.

SCOPE. An Albertine secundogeniture (1657-1718), the first of three to die out; the only male heir, Prince Christian August, 'joined the clergy'. The Henneberg inheritance (Schleusingen, Suhl, Kuhndorf) is the 1660 acquisition; the county-of-henneberg dossier of this batch ends the county in 1583 (a Wettin condominium followed), and its page says the estates were divided in 1660 among Saxe-Weimar, Saxe-Gotha and Maurice of Saxe-Zeitz. The page is silent on wars.

SHAPES. Zeitz 12.14E 51.05N 22 km; Schleusingen and Suhl 10.72E 50.56N 16 km. Gazetteer names wanted: 'Zeitz', 'Naumburg (Saale)', 'Haynsburg', 'Schleusingen', 'Suhl'.

NOT SETTLED. (1) No area; (2) the year of Suhl and Kuhndorf; (3) the Henneberg-Weimar-Gotha shares in 1660 are in the other dossiers.

COUNTERPARTS NEEDING DOSSIERS: none new.

## duchy-of-arenberg (Duchy of Arenberg, 1549-1810)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Arenberg row.

SCOPE. 1549 to 1810 as the infobox gives. The page is silent on the capital and on any founding year, and describes no war by name. The French occupation of the west bank 'around 1798' is an occupation entry at confidence 1; the home lands are dropped from the duchy in 1803 at confidence 1 because the page gives the 1803 compensation and no cession. The occupation is paired under the Directory (Cliopatria's French Directory row, 1796-99) and the 1803 loss is entered against the Consulate. The Confederation of the Rhine membership has no year on the page. 1814: 'the former Arenberg territories were divided between the Kingdom of Prussia and the Kingdom of Hanover'; Hanover's share became the duchy of Arenberg-Meppen in 1826.

SHAPES. Aremberg 6.82E 50.40N 11.5 km (413 km2); Recklinghausen 7.20E 51.61N 15 km; Meppen 7.29E 52.69N 18 km. Gazetteer names wanted: 'Aremberg', 'Recklinghausen', 'Meppen', 'Dülmen'.

NOT SETTLED. (1) The 1798 and 1803 steps; (2) Dulmen's year; (3) no capital; (4) the Meppen circle takes in Emsland guesswork.

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-wied (County of Wied, 1093-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Wied row.

SCOPE. 1093 to 1806; the page is silent on wars, on rank changes and on any territory. The partitions of 1631 and 1698 are kept inside one state (rule 2). After 1806 the page gives the Duchy of Nassau, then Prussia in 1815 and Rhineland-Palatinate since 1946.

SHAPES. A 16 km circle at 7.47E 50.50N. Gazetteer names wanted: 'Neuwied', 'Dierdorf', 'Runkel'.

NOT SETTLED. (1) No area or town list; (2) the infobox gives Nassau-Weilburg and the lead the Duchy of Nassau for 1806 (the Cliopatria row Duchy of Nassau begins in 1806).

COUNTERPARTS NEEDING DOSSIERS: none new.

## county-of-stolberg (County of Stolberg, 1210-1806)
Written 2026-10-25 for batch eu-09-x (1 page; budget 1-2). New state: Cliopatria has no Stolberg row.

SCOPE. The page is silent on how the county ended, on area, on territory lost and on wars. The end at 1806 is a convention (confidence 1): the lines Stolberg-Stolberg, Stolberg-Wernigerode and Stolberg-Rochefort continued; the Reformation came in 1539 and membership of the Upper Saxon Circle in 1512 (an association). The exclaves Konigstein (Taunus) and Rochefort (Ardennes) are drawn as small circles because the page names them as acquisitions.

SHAPES. Stolberg 10.95E 51.57N 18 km; Kelbra 11.05E 51.43N 10 km; Hohnstein 10.80E 51.50N 14 km; Wernigerode 10.79E 51.83N 14 km; Konigstein 8.47E 50.18N 8 km; Rochefort 5.22E 50.16N 10 km. Gazetteer names wanted: 'Stolberg (Harz)', 'Kelbra', 'Heringen (Helme)', 'Wernigerode', 'Königstein im Taunus', 'Rochefort (Belgium)'.

NOT SETTLED. (1) The end; (2) the givers of every acquisition; (3) 1413 or 1417 for Kelbra and Heringen.

COUNTERPARTS NEEDING DOSSIERS: county-of-hohnstein (no row).


---

# REPAIR RUN 2026-10-25 (author returning to the 14 dossiers the reviewer failed)

Fourteen dossiers were reopened (verdict fail): electoral-palatinate, habsburg-netherlands, electorate-of-mainz, duchy-of-brunswick-luneburg, duchy-of-cleves, landgraviate-of-hesse-rheinfels, county-of-schaumburg, swabian-circle, franconian-circle, county-of-henneberg, duchy-of-saxe-gotha-altenburg, duchy-of-saxe-weissenfels, duchy-of-saxe-merseburg, county-of-stolberg. Each also carries a dated REVISION paragraph at the end of its own `notes`. Dossiers with verdict pass, fix or thin were not touched, so every mirror edit that would land in one of them is listed below as NOT DONE. All 14 validate with 0 errors (habsburg-netherlands 16 resolve warnings, all unknown Dutch place names; electorate-of-mainz 4 and county-of-schaumburg 1, all unknown counterpart slugs).

## electoral-palatinate
CHANGED: (1) Upper Palatinate circle 70 -> 55 km (the 70 km circle was 1.6 times the region). (2) 1623 loss of the Bergstrasse to electorate-of-mainz (Heppenheim page: 'an interruption from 1461 to 1623 when the fief was pledged to the Electorate of the Palatinate'), confidence 2; the Bergstrasse circle is cut from 20 to 12 km (20 km reached Worms) and subtracted from the Lower Palatinate before 1461/63 and after 1623, because the 35 km Heidelberg circle also covers it (found event, K0, K1, K3-K5, occupation/contest events from 1648, dissolve, successor land). (3) 1463 gain stays confidence 2 with the Heppenheim page named: pledge 1461, treaty 1463. (4) K2 'to' 1622 was already applied by the reviewer.
DISAGREE: none.

## electorate-of-mainz
CHANGED: 1623 gain of the Bergstrasse from electoral-palatinate; K4 split at 1581 and 1623; Bergstrasse circle in K5-K7; 1581 gain of Königstein from county-of-stolberg (Königstein page 'By 1581, Königstein belonged to the Electorate of Mainz'; confidence 2; the Mainz 30 km circle covers Königstein, so it is cut out until 1580); the single 1803 loss to Hesse-Darmstadt is split into a loss of the Rheingau and Königstein area to county-of-nassau (Duchy of Nassau page: 'from Mainz, Höchst, Königstein, Cronberg, Lahnstein and the Rheingau') and a loss of the Bergstrasse and the Main lands to landgraviate-of-hesse-darmstadt.
DISAGREE / PAGES DISAGREE: the Rheingau page says the Rheingau 'was given to the Duchy of Nassau' when the archbishopric 'was dissolved in 1806'; the Duchy of Nassau page gives the 1803 award to Nassau-Usingen; 1803 used. The Electorate of Mainz page itself does not name the Rheingau; the Main-lands circle (8.42E 50.0N, 12 km) is the author's reading.
NOT DONE: county-of-nassau (verdict thin, not touched) has no mirror gain of the Rheingau, Höchst, Königstein, Cronberg and Lahnstein in 1803; add from the Duchy of Nassau page.

## county-of-stolberg
CHANGED: 1581 loss of Königstein to electorate-of-mainz, K4 split at 1581; the end moves from the 1806 convention to 1807 on the Stolberg-Wernigerode page ('mediatised in 1807 and made part of the Kingdom of Westphalia'; Prussia 1815), counterpart kingdom-of-westphalia, successor filled; Rochefort: the Rochefort (Belgium) page was opened and is silent on the Counts of Stolberg, the Stolberg-Wernigerode page does not mention Rochefort, so it stays drawn to 1806 with no loss.
DISAGREE: the page covers only the Wernigerode line; Stolberg-Stolberg and Stolberg-Rossla are assumed to follow.

## duchy-of-cleves
CHANGED: Soest added: contest 1444 (5 June) to 1449 against electorate-of-cologne, 1449 gain (Duchy of Westphalia page), K1 split at 1449, Soest circle in K1b, K2, dissolve and Brandenburg successor land, Soest Feud in wars.
PAGES DISAGREE: the Soest Feud page says only that Soest took John I of Cleves-Mark as suzerain and implies 27 April 1449 as the end (bibliography); the Westphalia page says Soest 'remained part of the Duchy of Cleves'; the latter is used.

## landgraviate-of-hesse-rheinfels
CHANGED: shape is the St. Goar circle joined to a 15 km right-bank circle at 7.85E 50.22N (Braubach, Reichenberg, Hohenstein) in the keyframe, found, dissolve, predecessor and successor.
DISAGREE: the reviewer's ratio 0.29 rests on about 2,700 km2 for 'about an eighth' of old Hesse; the page gives only the fraction and no area, so the ratio is not confirmed and the shape stays near 1,010 km2 on the grid.
NOT DONE: landgraviate-of-hesse-kassel (fix, not touched) still draws the single 14 km circle for its 1583 gain.

## county-of-schaumburg
CHANGED: 22 km Rinteln circle -> 15 km circle at 9.15E 52.27N; start 1106 (Adolf I, Count of Holstein page: 'first Count of Schauenburg from 1106'; County page 'probably ... in 1106'), infobox 1110 is the Holstein appointment, which the Adolf I page dates 1111; the 1640 partition is drawn as a loss to Hesse-Kassel, a loss to Brunswick-Lüneburg and a dissolve to Schaumburg-Lippe.
DISAGREE: the reviewer's 676 km2 is not on the County or the district page (area fields blank); the pages say the county was 'more or less congruent with the present district Landkreis Schaumburg'. The page 'Adolf I, Count of Schauenburg and Holstein' does not exist.
PAGES DISAGREE: Hesse-Kassel dates 'most of the County of Schaumburg' 1648 (Westphalia) while this page dates the partition 1640 and makes Schaumburg-Lippe the largest portion; 1640 used here.
NOT DONE: landgraviate-of-hesse-kassel (fix) keeps the 22 km circle, the 1648 date and 'most of'.

## duchy-of-brunswick-luneburg
CHANGED: no longer dissolved in 1692. 1692 loss to electorate-of-hanover of Calenberg-Göttingen, Grubenhagen, the Hameln-Dassel seats, Hoya and Diepholz ('The old Principality of Calenberg thus adopted the new name of Electorate of Hanover'); 1705 loss of Lüneburg; the rest continues as the Wolfenbüttel line to 1807 (kingdom-of-westphalia; 'The Wolfenbüttel Line retained its independence, except from 1807 to 1813'). I chose this over ending the dossier at 1269 because the principalities have no dossiers and ending at 1269 would leave the map empty for 1269-1692.
PAGES DISAGREE: the Brunswick-Lüneburg infobox ends 1806 ('The end of the Holy Roman Empire'); its text and the Duchy of Brunswick page give 1807 for Wolfenbüttel. 1807 used. The Duchy of Brunswick page gives 1754 (temporary) for the move of the residence to Brunswick, the other page 1753/1754.
NOT DONE: electorate-of-hanover names principality-of-luneburg (no dossier) as counterpart of its 1705 gain; it should name duchy-of-brunswick-luneburg.

## county-of-henneberg
CHANGED: the 1360 loss of Schmalkalden to landgraviate-of-hesse is removed and replaced by a 1583 loss to landgraviate-of-hesse-kassel (Schmalkalden page: 'When the Counts of Henneberg became extinct in 1583, their share was inherited by William IV, Landgrave of Hesse-Kassel'); keyframes 1347-1359 and 1360-1582 merged; Schmalkalden cut out of the shape before 1247; 1037 stays confidence 1.
PAGES DISAGREE: the County page says Schmalkalden 'fell to Landgrave William IV ... according to an inheritance treaty of 1360'; the German page on the House of Henneberg calls 1360 the start of a Henneberg-Hesse condominium and does not mention 1037 (Poppo I 1078 chronicle, 1096 charter; county founded 'toward the end of the 11th century').
NOT DONE: landgraviate-of-hesse-kassel (fix) has no 1583 gain of Schmalkalden.

## duchy-of-saxe-gotha-altenburg
CHANGED: 1735 loss (month 8, confidence 1) of the Coburg stand-in to duchy-of-saxe-coburg-saalfeld, K4 split at 1735, Coburg circle out of the 1826 hand-over. The Saxe-Coburg page does not say what Gotha received in 1699 ('the usual inheritance disputes'; a 35-year Meiningen-Saalfeld dispute), so the share could not be moved to a better place.
GAP: Coburg, Meiningen, Römhild, Eisenberg and Hildburghausen undrawn 1672-1680 (K1 note says why: no page dates or locates the shares; none of the duchies has a dossier here).
NOT DONE: duchy-of-saxe-coburg-saalfeld (fix) names 'Saxe-Coburg (extinct 1699; no dossier)' for its 1735 gain, not this dossier.

## duchy-of-saxe-weissenfels
CHANGED: six Ämter circles added (Freyburg, Sachsenburg/Oldisleben, Sangerhausen, Eckartsberga, Weissensee, Langensalza; about 5,800 km2 on the grid, was 2,800); the 1656 gain from archbishopric-of-magdeburg deleted and folded into the found event (counterpart electorate-of-saxony; the lordships were 'adjudicated to Saxony by the 1635 Peace of Prague'). The page gives no area.

## duchy-of-saxe-merseburg
CHANGED: shape is now the four-circle union of electorate-of-saxony's 1657 loss (Merseburg-Lützen, Delitzsch-Bitterfeld, Lower Lusatia west and east) in K0, found, dissolve, predecessor, successor. The page gives no area.
NOT DONE: electorate-of-saxony names the counterparts 'saxe-merseburg', 'saxe-weissenfels' and 'saxe-zeitz', but the dossiers are duchy-of-saxe-merseburg, duchy-of-saxe-weissenfels and duchy-of-saxe-zeitz (slug mismatch to resolve).

## habsburg-netherlands
CHANGED: Ryswick (1697) limited to Luxembourg, Mons and Kortrijk (Ryswick page: 'French forces also evacuated Catalonia, Luxembourg, Mons and Kortrijk'); Ypres, Tournai, Oudenaarde and Veurne stay French until a 1713 gain at confidence 1; Mons (8 April 1691) and Namur (June 1692 to 5 September 1695) lost and regained; Diksmuide regained 1694 (Nine Years' War page, confidence 2); Nine Years' War zones added. 1637: Breda lost, Venlo and Roermond regained (Cardinal-Infante page), kept to 1713, Venlo lost to the Dutch in 1713 (Spanish Guelders page), Roermond Austrian to 1795. North-east: the city of Groningen regained 3 March 1580 (George van Lalaing page), the eastern towns gained in 1588 (confidence 1), lost 1591, 1592, 1594, 1597; Groenlo and Oldenzaal regained 1606 (confidence 2) and lost 1626/1627. War starts 1568; contest in Holland and Zeeland from April 1572 to January 1579. Dunkirk: lost June 1658 to commonwealth-of-england (Battle of the Dunes page). Breda is out of north Brabant 1590-1624 and from 1637 in the shapes.
DISAGREE: the reviewer's wish for 'the later losses' of Groningen, Drenthe and Overijssel as provinces is met only for towns; the pages name towns (Rennenberg page: 'the rest of the province remained loyal to the rebel cause'). Ath and Charleroi (French captures of 1697 and 1693) are not entered because no page says Ryswick returned them. Thin items (Courtrai 1678, end of the Barrier 1781): the Treaties of Nijmegen and Barrier Treaty pages are silent; both stay confidence 1.
PAGES DISAGREE: Venlo and Roermond: the Eighty Years' War page has the Dutch conquest of 1632 but not the 1637 recapture; the Cardinal-Infante page has it without a month. The dutch-republic dossier's 1588 and 1606 events are Cliopatria cells, here town circles.
NOT DONE: dutch-republic (not touched) 1713 gain is Venlo and Echt, here Venlo only.

## swabian-circle, franconian-circle
Orchestrator decision, not taken here: both are type umbrella (an association of estates, never territory) and the reviewer asks to drop them or keep them only if the compiler skips umbrellas. Left in place; the only change is the found/dissolve counterpart holy-roman-empire (dossier ends 1259) -> holy-roman-empire-minor-states. The reviewer's remark that the Swabian shape 'includes region:Franconia' reads the shape the wrong way: Franconia is subtracted in it.
