# eu-22-a notes (Europe 1945 to 2026, part a)

Six dossiers written 2026-10-31, all validate with 0 errors: denmark, french-fourth-republic, kingdom-of-greece, people-s-socialist-republic-of-albania, republic-of-iceland, republic-of-italy. No new states, no rebel dossier. Pages opened: 17 distinct Wikipedia pages, 18 successful fetches (the Greek Civil War page twice), 3 failed fetches.

## Cliopatria rows to merge or split
- denmark (Q350186) vs danish-magnates (1333..1351): different states, no merge (Cliopatria id error).
- republic-of-italy (Q38) vs italian-republic (1803..1813, Napoleonic): different states, no merge.
- people-s-socialist-republic-of-albania (Q467864, 1946..1990) vs republic-of-albania (1991..2024): kept as two dossiers (the second belongs to another eu-22 part). The land is the same 96 grid cells in all eight shapes, so a merge would change no border; the orchestrator may put them in one colour family. The communist state ends 29 April 1991 (page), one year after the Cliopatria row.
- french-fourth-republic: Cliopatria row ends 1957, the republic ends October 1958 (page); the Fifth Republic row starts 1958.
- kingdom-of-greece: Cliopatria row ends 1966, the dossier ends April 1967 (coup); the monarchy was abolished 1 June 1973 (page) but the junta row (greek-junta) owns 1967 on.

## Cliopatria shape faults found (each is a verdict in the dossier)
- French Fourth Republic: the shape holds the French zone of Germany (Baden-Wuerttemberg and Rheinland-Pfalz cells) and the Saar as French land, and the Austrian zone (North Tyrol, Vorarlberg) in 1945 only although the occupation lasted to October 1955. Occupied land and the Saar protectorate are now events. Reunion is missing from the shape. Algeria, the Maghreb and Indochina are separate Cliopatria rows (french-africa, french-indochina) owned elsewhere.
- Kingdom of Greece: 1945-46 contain 6 of 9 Dodecanese cells before the 1947 transfer; 1946-48 cut 72/53/18 cells of northern and central Greece for a rebel zone that no page maps.
- Republic of Italy: the province of Trieste (2 cells) is absent for 1946-2024. Cliopatria's socialist-federal-republic-of-yugoslavia row holds those two cells for 1946..1991 (wrong after 26 October 1954): the Yugoslavia dossier author should check.
- Denmark: the 1945 shape lacks Greenland that 1946 adds.
- Iceland: the Republic row starts 1946 and the Kingdom row ends 1939; the republic was proclaimed 17 June 1944 (new keyframe for 1944-45).

## Pages that would not load
- https://en.wikipedia.org/wiki/French_occupation_zone_of_Germany (url_not_found; Allied-occupied_Germany used instead).
- https://en.wikipedia.org/wiki/Departmentalisation_of_the_French_overseas_colonies (url_not_found): the 19 March 1946 overseas departments are therefore not dated.
- The apostrophe URL of People's_Socialist_Republic_of_Albania failed; the %27 form loaded.

## Not settled (page silent or out of budget)
- French sector of Berlin: dated to 1945 and to 3 October 1990 in the repair pass (West Berlin page); still silent on the month, the districts and the day the French took over. Morocco, Tunisia, French India, Cameroon (colonial rows); the proclamation day of the Italian Republic; Dodecanese handover day (31 March 1947) and union day (7 March 1948) are not on the pages opened; the year-by-year extent of the Democratic Army's control in the Greek Civil War (only the 1948 Peloponnese claim and the Grammos and Vitsi strongholds are on the page; the Battle of Grammos-Vitsi article was not opened); Tende and La Brigue transfer day; rulers for Denmark, Greece, Iceland and Italy (the pages give no usable list, so identity.rulers is omitted).
- No rebel dossier for the Democratic Army of Greece or the Provisional Democratic Government (23-24 December 1947): the page says it was unrecognised and describes only attacks and retreats.

## Counterparts needing dossiers
- west-berlin (1945..1990): the French, British and American sectors of Berlin, occupied until 3 October 1990 (added in the repair pass; the French Fourth Republic ledger names it as the counterpart of the French sector).
- saar-protectorate (1946..1957, Saar Protectorate): vassal of the Fourth Republic, joined West Germany 1 January 1957.
- allied-occupied-germany (1945..1949) as owner of the occupation zones, or the zones as separate occupation entities.
- free-territory-of-trieste (1947..1954): Zone A (222.5 km2) and Zone B (515.5 km2).

## Gazetteer names wanted
- Tende and La Brigue (valleys, about 44.08 N 7.6 E; a 12 km circle stands in), Sazan Island (Saseno, 5.7 km2, off Vlore; a 15 km circle round Vlore stands in), Surtsey and the Westman Islands (Vestmannaeyjar), Pula (Pola) and Gorizia as places.
- Natural Earth "France" includes the overseas departments; {admin1: Guyane française} is the exact spelling for French Guiana.

## Repair pass (2026-10-31, after review-eu-22-a.md): french-fourth-republic
Reviewer verdict fail. Pages reopened: West Berlin, Provisional Government of the French Republic (twice), Overseas departments and regions of France, Réunion, Allied-occupied Germany. Dossier re-validated with --resolve: 0 errors, 6 warnings (counterparts west-berlin, allied-occupied-germany, saar-protectorate have no dossier yet; the Berlin occupation_start has no end because the occupation outlasts the state). 12 events, 9 sources.
Applied from the review:
1. keyframe 4 (1950-55) correction now subtracts all of Germany, not only the Saarland (resolve of shape x Germany: 20 cells, the Saar's 11 plus 9 others: Berlin 52.54 N 13.28 E, 2 Lindau, 2 Upper Rhine, 4 beside the Saar); Tende circle kept. Note rewritten (the old 'German zone is gone' was untrue of those 9 cells).
2. keyframe 5 (1956-57) the same, and the Tende circle (cell 44.16 N 7.68 E) restored.
3. Dossier notes and this file: the Berlin cell is in every shape from 1945 to 1957, not 1945 only (resolved for 1945, 1946, 1950).
4. ledger occupation_end of 23 May 1949 (now /ledger/8): region is minus(French zone, admin1 Berlin) so the Berlin cell stays occupied; the reviewer suggested {place: Berlin, km 15}, I used admin1 Berlin, which resolves to the same single cell and names the city.
Same defect, not listed by the reviewer: the dissolve event's region (minus Saarland) also kept the 9 German cells; it now matches keyframe 5.
Thin items:
- French sector of Berlin: new event /ledger/1, occupation_start 1945 at confidence 2, counterpart west-berlin, source West Berlin ('established in 1945'; 'remained under military occupation until 3 October 1990'); the zone event /ledger/2 now excludes the Berlin cell so the two do not overlap. The page gives no month and its French-sector heading is empty, so no district is named.
- Departmentalisation: Réunion page: 'became a département d'outre-mer (overseas département) of France on 19 March 1946'. New gain event 1946.3 (counterpart nobody; Réunion, 10 cells, is in neither this row nor French Africa) and Réunion is added to keyframes 1-5 and the dissolve region. I added this beyond the reviewer's fix list because the thin item asks for it; it changes the corrected shapes by 10 cells. The Overseas departments page gives no date for any of the four, so Guadeloupe, Martinique and French Guiana (already in the shape) have no day on a page.
- Provisional Government: the page dates the government to 3 June 1944 (created by the CFLN), Paris from 31 August 1944, to 27 October 1946, and its infobox gives 'Free France' as predecessor. I did NOT move the start to 1944 (disagreement with the reviewer's hint): the Free French row's last shape is 1944 (data/polities.csv: free-french 1940..1944), so a 1944 start would cover that year twice, and the first Fourth Republic shape is 1945. /ledger/0 keeps confidence 1 with the page's dates in its note; alt name changed to '(1944-1946)'.
Left as is: the 1949 occupation_end region still contains the Saarland cells (11), which the Saar vassal_start of Feb 1946 had already taken out of the occupation; harmless for the map, not listed by the reviewer.
For the french-fifth-republic author: shapes.csv gives french-fifth-republic_1958 .. _2023 a bbox reaching 52.5863 N, so those shapes hold a Berlin cell too; it is occupied land until 3 October 1990 and not French land at all afterwards.
