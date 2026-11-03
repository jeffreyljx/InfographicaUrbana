# Review of batch eu-08-x (Holy Roman Empire to 1250, additions)

Reviewed 2026-10-25 by the adversarial reviewer. Machine copy: history/notes/phase-b/reviews/eu-08-x.json. All 20 dossiers validate (0 errors) before and after review. Spot checks: every page named below was opened with WebFetch in this review.

Verdicts: stem-duchy-of-saxony **fail**, stem-duchy-of-bavaria **fail**, stem-duchy-of-swabia **fail**, stem-duchy-of-franconia **pass**, margraviate-of-austria **fail**, duchy-of-carinthia **fix**, march-of-verona **fail**, march-of-styria **fail**, lutici **thin**, landgraviate-of-thuringia **fix**, margraviate-of-meissen **fix**, lombard-league **fix**, duchy-of-lower-lorraine **fail**, northern-march **fix**, duchy-of-zahringen **fix**, archbishopric-of-magdeburg **thin**, prince-bishopric-of-liege **fix**, prince-archbishopric-of-salzburg **thin**, prince-bishopric-of-utrecht **fix**, prince-archbishopric-of-bremen **fix**

Convention: *applied* = edited in place by the reviewer and re-validated; *blocking* = must be done before acceptance; other unapplied items are non-blocking or routing notes for another group.

## stem-duchy-of-saxony: fail

- [BLOCKING] `/keyframe_review/0/correction (and /keyframe_review/1, /keyframe_review/2, /ledger/0, /ledger/12)`: Old Saxony is drawn over land two other dossiers of this batch draw at the same time: the Altmark (northern-march, 965-1157) and the Aachen and Cologne circles (duchy-of-lower-lorraine, 959-1180); no ledger on either side records a loss or a vassal relation. Evidence: Gazetteer 'Old Saxony' = Niedersachsen + Sachsen-Anhalt + Nordrhein-Westfalen + Bremen + Hamburg + Schleswig-Holstein; northern-march /keyframe_review/0-2 hold an Altmark circle (11.9 E 52.6 N, 55 km) inside Sachsen-Anhalt; duchy-of-lower-lorraine /keyframe_review/0-4 hold 45 km circles at Aachen and Cologne inside Nordrhein-Westfalen. The keyframe note concedes the Rhineland is 'too much' but leaves it in. Fix: Subtract the Aachen and Cologne circles (better: the Rhineland west of the Rhine) from every Saxony shape and region. For the Altmark, do as for the Billung March: vassal_start northern-march 965 and vassal_end 1157 here (northern-march adds the mirror), or carve the Altmark out from 965 with a loss to northern-march.
- [non-blocking] `/identity/successors`: The 1180 break-up omits archbishopric-of-magdeburg and prince-archbishopric-of-bremen, which both open with a 1180 found event naming stem-duchy-of-saxony. Evidence: archbishopric-of-magdeburg /ledger/0 and prince-archbishopric-of-bremen /ledger/0; Duchy of Saxony page: 'Since 1180, the ancient stem duchy of Saxony was partitioned in some dozens of territories of imperial immediacy by Barbarossa.' Fix: Add both as successors with the land their found events draw (Magdeburg, Börde and Jerichow circles; the Elbe-Weser land around Vörde and Stade).
- [non-blocking] `/ledger/10`: The 1180 Ascanian rump goes to house-of-ascania, whose dossier (eu-09) starts in 1260, so the land has no holder 1180-1259. Evidence: house-of-ascania /ledger/0 is a 1260 found with counterpart null. Fix: Routing: eu-09 should start house-of-ascania (or a Saxe-Wittenberg/Lauenburg dossier) in 1180 with a found from stem-duchy-of-saxony; nothing for this author beyond keeping the slug.
- [non-blocking] `/ledger/1, /ledger/3, /ledger/7, /ledger/8, /ledger/11`: The Obotrite counterpart is the eu-07 dossier obotrites, which ends in 946 and has no 936 vassal event; the 983 vassal_end and the 1160 gain fall after its end, and Pribislav's restored Mecklenburg is a free string. Evidence: obotrites identity end 946 (dissolve c1, 'the pages date no end of the Obotrites'); Billung March page: march 'formed in 936', 'finally abandoned following the uprising of the Obotrites and Veleti'; Niklot page: Pribislav 'recovered his inheritance as Prince of Mecklenburg in 1167 as a Saxon vassal'. Fix: Routing: eu-07 extends obotrites to 1167 (or a new Obotrite principality dossier), and a lordship-of-mecklenburg dossier from 1167; then set /ledger/8 and /ledger/11 to that slug.
- [non-blocking] `/ledger/7/region and /keyframe_review/1/correction`: Region 'Mecklenburg' is all of Mecklenburg-Vorpommern, including Vorpommern east of the Peene, while the note and the Niklot page say 'Mecklenburg up to the Peene River'. Evidence: Gazetteer Mecklenburg = admin1 Mecklenburg-Vorpommern; Niklot page: 'Niklot's death ended Slavic control in Mecklenburg up to the Peene River.' Land east of the Peene is Pomeranian (pomerania, eu-15). Fix: Use Mecklenburg minus a polygon east of the Peene, and say so in text.
- [thin] `/ledger/10`: The land of the Ascanian rump duchy in 1180 (confidence 1). Try: https://en.wikipedia.org/wiki/Saxe-Wittenberg
- [thin] `/ledger/11`: The end of Saxon overlordship over Mecklenburg in 1180 (confidence 1). Try: https://en.wikipedia.org/wiki/Pribislav_of_Mecklenburg
- Spot checks: `/ledger/3` confirmed (formed 936; abandoned after the 983 rising); `/ledger/7` confirmed (August 1160, Werle; 'up to the Peene'); `/ledger/8` confirmed (1167, 'as a Saxon vassal'); `/ledger/9` confirmed (1180 grant to Philip of Heinsberg; the page does not name Arnsberg or the Sauerland for the grant, so confidence 2 is right); `/ledger/4-6` confirmed (1106, 1138, 1142)
- Area: Duchy of Saxony infobox gives no area; acknowledged in /keyframe_review/0/note.

## stem-duchy-of-bavaria: fail

- [BLOCKING] `/keyframe_review/0-2/correction, /ledger/0, /ledger/19, /identity/predecessors/0`: admin1 Bayern contains Franconia (Nuremberg, Würzburg, Bamberg) and Bavarian Swabia west of the Lech, which this batch draws as stem-duchy-of-franconia (906-939) and stem-duchy-of-swabia (915-1268): both are double-drawn for the whole life. Evidence: Gazetteer Franconia = circles of 90/70/60 km at Nuremberg/Würzburg/Bamberg; Swabia = Baden-Württemberg + 80 km at Augsburg; Duchy of Franconia page: the duchy 'stretched along the valley of the River Main'. Fix: Bavaria = Bayern minus region Franconia and minus the Augsburg country west of the Lech (keep the Nordgau), in every keyframe and region of this dossier.
- [BLOCKING] `/keyframe_review/2 and /ledger`: prince-archbishopric-of-salzburg is founded in 1213 with counterpart stem-duchy-of-bavaria, but Bavaria keeps admin1 Salzburg until 1255 and records no loss: 1213-1255 double-drawn. Evidence: prince-archbishopric-of-salzburg /ledger/0 (1213 found, cp stem-duchy-of-bavaria); Prince-Archbishopric of Salzburg page: 'Archbishop Eberhard II of Regensberg was made a prince of the Empire in 1213'. Fix: Add a 1213 loss (country Austria, admin1 Salzburg, cp prince-archbishopric-of-salzburg) and split keyframe 976-1255 at 1213; or, if the author prefers immediacy only in 1275, a vassal_start/vassal_end pair here and in Salzburg.
- [BLOCKING] `/ledger/18`: A 1180 loss of Styria to duchy-of-styria, a land no Bavaria keyframe ever draws; duchy-of-styria (eu-09) founds itself from march-of-styria, not from Bavaria. The march's Bavarian years (before 970 to 976) are not recorded at all. Evidence: March of Styria page: 'Created sometime before 970, it was broken off the larger March of Carinthia, itself a march of the Duchy of Bavaria'; 'In 976, it was transferred to the jurisdiction of the newly created Duchy of Carinthia'. duchy-of-styria /ledger/0: found 1180 cp march-of-styria. Fix: Add vassal_start march-of-styria 970 and vassal_end 976 (mirrored in march-of-styria); turn /ledger/18 into a vassal_end cp march-of-styria (if Bavaria is kept as overlord after 1122, with the matching vassal_start) or drop it and keep the 1180 separation as the rename caption.
- [non-blocking] `/identity/successors`: Successor duchy-of-bavaria (eu-09) starts in 1260 with predecessor holy-roman-empire, so Upper Bavaria is undrawn 1255-1259. Evidence: duchy-of-bavaria identity start 1260, /ledger/0 found cp holy-roman-empire ('after the partition of 1255'). Fix: Routing: eu-09 to start duchy-of-bavaria at 1255 with predecessor stem-duchy-of-bavaria; no change here.
- [thin] `/keyframe_review/2`: The separation of the Trent and Brixen counties (1004/1027) and of the Tyrolean Inn valley, and the Traungau going with Styria in 1180; admin1 Tirol and Oberösterreich stay Bavarian to 1255. Try: https://en.wikipedia.org/wiki/Prince-Bishopric_of_Brixen
- Spot checks: `/ledger/1` confirmed (911, 'uniting Bavaria and Carinthia'); `/ledger/2-3` confirmed (916 invasion; 919 return); `/ledger/8` confirmed (952, March of Verona); `/ledger/10` confirmed (976); `/ledger/15` confirmed (Privilegium Minus 17 September 1156); `/ledger/19` confirmed (1255 division)
- Area: No infobox area on Duchy of Bavaria; acknowledged.

## stem-duchy-of-swabia: fail

- [BLOCKING] `/keyframe_review/1/correction`: Swabia keeps admin1 Zürich (whole life) and Schaffhausen while duchy-of-zahringen draws Zürich as a vassal 1098-1173 and directly 1173-1218, and Schaffhausen 1198-1218; Swabia records no loss. Evidence: duchy-of-zahringen /ledger/1, /ledger/5, /ledger/6; House of Zähringen page: 'jurisdiction over Zürich' alongside the Lenzburg counts 'until 1173'; 'Schaffhausen (acquired 1198)'. Fix: Split keyframe 1096-1268 at 1173 and 1198 with losses of Zürich (cp duchy-of-zahringen) and Schaffhausen; Zähringen then names stem-duchy-of-swabia as counterpart of its 1173 and 1198 gains.
- [BLOCKING] `/end, /ledger/8, /identity/successors/0`: Swabia runs to 1268 although house-of-hohenstaufen (eu-09, Cliopatria row 1260-1271) draws the same duchy from 1260: 1260-1268 double-drawn. The successor note sees the overlap but leaves it. Evidence: house-of-hohenstaufen /ledger/0: '1260: the last Hohenstaufen hold the Duchy of Swabia'; /ledger/1 dissolve 1268. Fix: End this dossier in 1260 (dissolve, successor house-of-hohenstaufen taking the land) and move the Conradin war to that dossier, or have the orchestrator retire the Cliopatria row; one of the two must go.
- [non-blocking] `/ledger/7`: Mirror off by two years: the Breisgau loss is 1096 here, the Zähringen found is 1098. Evidence: Duchy of Swabia page: 'to whom he ceded the Breisgau in 1096'; House of Zähringen page: 'In 1098, he reconciled with Frederick, renounced all claims to Swabia'. Fix: Keep 1096 if the cession is the event, but note the 1098 settlement in both notes so the reviewer of either side sees why; or move this loss to 1098.
- [thin] `/keyframe_review/0`: When Alsace joined Swabia (drawn from 915) and the Basel lands of 926. Try: https://en.wikipedia.org/wiki/Alsace
- Spot checks: `/ledger/0` confirmed (Erchanger proclaimed 915); `/ledger/2-3` confirmed (919 Battle of Winterthur); `/ledger/7` confirmed (Breisgau ceded 1096); `/ledger/8` confirmed (1268, Conradin)
- Area: No infobox area; the author compares the gazetteer 70,000 km2 with Cliopatria's 1260 Hohenstaufen shape.

## stem-duchy-of-franconia: pass

- Spot checks: `/ledger/0` confirmed (906 dux Franconiae); `/ledger/1` confirmed (December 918); `/ledger/2` confirmed (rebellion 938); `/ledger/3-4` confirmed (2 October 939, Andernach)
- Area: Infobox has no area (906-1168); acknowledged, and the 1168 end is explained as the Würzburg lordship. Tried and could not break: years, the 939 end against the 1168 infobox date, counterparts in life (east-franks to 911, kingdom-of-germany 911-962). Its overlap with Bavaria is Bavaria's fault.

## margraviate-of-austria: fail

- [BLOCKING] `/ledger`: No vassal_start/vassal_end with stem-duchy-of-bavaria, the mirror of Bavaria's /ledger/9 (960) and /ledger/15 (1156). Evidence: Margraviate of Austria page: 'Austria was elevated to a duchy independent from Bavaria by the Privilegium Minus' (1156); stem-duchy-of-bavaria /ledger/9 and /ledger/15. Fix: Add vassal_start 960 and vassal_end 1156 (month 9), counterpart stem-duchy-of-bavaria, region the march.
- [BLOCKING] `/keyframe_review/0/correction`: The single shape 960-1282 is all of Niederösterreich and Wien, but the cited page gives the first extent as 'between the river Enns and the Vienna Woods (Wienerwald)' and dates the Thaya colonisation to 1055-1075; the Leitha/March frontier is undated. Evidence: Margraviate of Austria page, read 2026-10-25. Fix: Draw 960 to the eastward expansion as the Enns-Wienerwald strip only, then later keyframe(s) with gain events (counterpart principality-of-hungary/kingdom-of-hungary) for the Vienna basin and the Weinviertel; if no page dates them, keep one later keyframe at confidence 1 and say so.
- [non-blocking] `/ledger/5`: vassal_start duchy-of-styria (1192) is never ended (validator warning) although Styria passed to Hungary in 1254 and to Ottokar in 1260; duchy-of-styria (eu-09) records 1192 as a rename, not a relation with Austria. Evidence: Duchy of Austria page: Frederick 'killed at the 1246 Battle of the Leitha River, whereby the Babenberg line became extinct'; duchy-of-styria /ledger/1-4. Fix: Add vassal_end 1246 (or 1254), and agree one model of the personal union with duchy-of-styria.
- [non-blocking] `/identity/capitals`: Melk to 1144 skips Klosterneuburg. Evidence: Margraviate of Austria page: 'The margraves' residence later was moved down the Danube to Klosterneuburg until 1145'. Fix: Add Klosterneuburg before Vienna (start year as the page allows, confidence noted).
- [thin] `/keyframe_review/0`: Dated steps of the eastward expansion to the Leitha and the March (Thaya) frontier. Try: https://en.wikipedia.org/wiki/Adalbert,_Margrave_of_Austria
- Spot checks: `/ledger/0` confirmed ('by about 960, he appointed Burchard'); `/ledger/3` confirmed (Vienna 1145); `/ledger/5` confirmed (1186 pact, 1192 Styria); `/ledger/6-8` confirmed (1246 extinction, Ottokar 1251-1276, 1282 Diet of Augsburg)
- Area: No infobox area on either page; acknowledged.

## duchy-of-carinthia: fix

- [applied] `/ledger/5/counterpart`: Free string 'March of Carniola (Poppo)' instead of the slug the author listed in counterparts_needing_dossiers. Evidence: Author report counterparts_needing_dossiers: march-of-carniola 1040-1364; Duchy of Carinthia page: 'split off the Carniolan march the following year and granted it to Margrave Poppo of Istria'. Fix: Set to march-of-carniola.
- [non-blocking] `/ledger`: Dynastic changes after 1122 (Ottokar II 1269, Habsburg 1276, Meinhard of Gorizia-Tyrol 1286) are not recorded as renames; no land moves. Evidence: Duchy of Carinthia page (1335 Habsburg grant confirmed). Fix: Optional renames; not required for acceptance.
- Spot checks: `/ledger/0` confirmed (976; marches of Styria, Carniola and Istria); `/ledger/5` confirmed (1040, Poppo); `/ledger/8` confirmed (1151, Henry V divested); `/ledger/9` confirmed for the 1180 elevation; the page says independence from the Carinthian dukes came gradually after 1122; `/ledger/10` confirmed (1335)
- Area: Infobox 10,327 km2 is the 1910 crown land; gazetteer Kärnten about 9,600 km2; acknowledged in /keyframe_review/0 and /1.

## march-of-verona: fail

- [BLOCKING] `/ledger`: No vassal events for its overlords: Bavaria 952-976 and Carinthia 976-1151, the mirrors of stem-duchy-of-bavaria /ledger/8, /ledger/11 and duchy-of-carinthia /ledger/2, /ledger/8. Evidence: March of Verona page: 'Seized by King Otto I of Germany in 952, it was held by the Dukes of Bavaria'; 'In 1151 the Hohenstaufen King Conrad III of Germany finally divested Duke Henry V of Carinthia' and enfeoffed Herman III of Baden. Fix: Add vassal_start 952 / vassal_end 976 cp stem-duchy-of-bavaria and vassal_start 976 / vassal_end 1151 cp duchy-of-carinthia, region as the keyframe of each year.
- [applied] `/ledger/1/counterpart and /ledger/2/counterpart`: Free strings 'Bishopric of Trent' and 'March of Istria' instead of the slugs listed in counterparts_needing_dossiers. Evidence: Author report: prince-bishopric-of-trent, march-of-istria; page: Trent lands 'from 1004', Istria 'in 1070 ... detached from Verona'. Fix: Set to prince-bishopric-of-trent and march-of-istria.
- [non-blocking] `/identity/successors/0`: The successor is lombard-league, typed umbrella (an association, 'never territory' by research-brief rule 4), so the Veronese land has no territorial holder after 1167. Evidence: lombard-league identity type umbrella; March of Verona page: 'In 1167, the Veronese cities joined the Lombard League; this constituted the de facto end of the march.' Fix: Name the territorial successor the compiler will draw (kingdom-of-italy or the commune), keeping lombard-league in the note.
- [non-blocking] `/ledger/3/counterpart`: patriarchate-of-aquileia exists in polities.csv only from 1260 and has no dossier. Evidence: polities.csv patriarchate-of-aquileia 1260-1449; page: Friuli 'separated' in 1077 to create the Patriarchate. Fix: Routing: the owning group (eu-13) should start the Patriarchate in 1077.
- Spot checks: `/ledger/0` confirmed (952); `/ledger/1` confirmed (from 1004); `/ledger/2` confirmed (1070); `/ledger/3` confirmed (1077); `/ledger/5` confirmed (1167)
- Area: No infobox area; acknowledged.

## march-of-styria: fail

- [applied] `/ledger/0/counterpart and /identity/predecessors/0/slug`: Founded in 970 from duchy-of-carinthia, a duchy created only in 976. Evidence: March of Styria page: 'Created sometime before 970, it was broken off the larger March of Carinthia, itself a march of the Duchy of Bavaria.' Fix: Set both to stem-duchy-of-bavaria (done, with a reviewer note).
- [applied] `/ledger/2/year`: Gain dated 1043 opens keyframe march-of-styria_1042. Evidence: March of Styria page: 'In 1042/43 further territory east of the Mur up to Pitten and the Leitha river was conquered.' Fix: Year set to 1042 (done).
- [BLOCKING] `/ledger`: No vassal events for its overlords: Bavaria before 970-976 and Carinthia 976-1180, the mirror of duchy-of-carinthia /ledger/1 and /ledger/9 (and of the Bavarian events that dossier must add). Evidence: March of Styria page: 'In 976, it was transferred to the jurisdiction of the newly created Duchy of Carinthia'; the Otakars 'gradually gained independence from the Carinthian dukes'. Fix: Add vassal_start 970 / vassal_end 976 cp stem-duchy-of-bavaria and vassal_start 976 / vassal_end 1180 cp duchy-of-carinthia (or an earlier end if the author dates the independence).
- [thin] `/sources`: One page used of a 2-5 budget; the Otakar acquisitions (Traungau 1180 with the ducal elevation, Pitten 1158) are not drawn. Try: https://en.wikipedia.org/wiki/Duchy_of_Styria
- Spot checks: `/ledger/0` confirmed year, wrong counterpart (fixed); `/ledger/1` confirmed (1035); `/ledger/2` mis-dated by a year against its keyframe (page '1042/43'; fixed to 1042); `/ledger/3` confirmed (1056); `/ledger/4` confirmed (1180)
- Area: No infobox; acknowledged (gazetteer Steiermark about 17,000 km2).

## lutici: thin

- [non-blocking] `/ledger/1-2 against holy-roman-empire /ledger/5 and /ledger/10`: The Lutici-Empire contest is 991-993 here and 985-1003 in holy-roman-empire (eu-08-b). Evidence: Lutici page: 'In 991 ... the temporary reconquest of Brandenburg', 'In 992 ... the subsequent siege'; holy-roman-empire /ledger/5: 'From 985, several princes of the Empire carried out annual campaigns'. Fix: Agree one span with eu-08-b (985-1003 covers both pages); non-blocking.
- [non-blocking] `/ledger/5/note`: The note says the infobox lists the Margraviate of Brandenburg from 1157; the 1157 date is in the Brandenburg navbox, the infobox has 'Conquest of Rethra, collapse: 12th century'. Evidence: Lutici page read 2026-10-25. Fix: Reword the note; the confidence 2 end year stays.
- [non-blocking] `/ledger/3-4/counterpart`: The 1093-1128 contest names obotrites, whose eu-07 dossier ends in 946. Evidence: obotrites identity end 946. Fix: Routing: same Obotrite gap as stem-duchy-of-saxony.
- [thin] `/keyframe_review/0`: The federation's disintegration in the 1050s civil war and the piecemeal partition between Obotrites, Pomerania and Brandenburg in the 12th century; one page used of a 2-5 budget. Try: https://en.wikipedia.org/wiki/Rethra
- Spot checks: `/ledger/0` confirmed (first recorded with the 983 uprising); `/ledger/1-2` confirmed (991-992 Brandenburg); `/ledger/3` confirmed (1093); `/ledger/4` confirmed (1128)
- Area: No infobox area; polygon about 23,800 km2 between the Warnow, Havel and Oder as the page bounds it; acknowledged.

## landgraviate-of-thuringia: fix

- [non-blocking] `/identity/predecessors/0`: Predecessor duchy-of-thuringia is the eu-07 dossier that ends in 719, 412 years before this state; the found event names holy-roman-empire. Evidence: duchy-of-thuringia identity 567-719; /ledger/0 found cp holy-roman-empire; Landgraviate page: Louis I 'was appointed Landgrave of Thuringia in 1131'. Fix: Make holy-roman-empire the predecessor carrying the land; mention the old duchy in the note only. Non-blocking.
- Spot checks: `/ledger/0` confirmed (1131); `/ledger/1` confirmed (Ludovingians died out 1247); `/ledger/5` confirmed (1264, Henry of Meissen); `/ledger/6` confirmed (Hesse to Sophie's son Henry I)
- Area: No infobox area; acknowledged.

## margraviate-of-meissen: fix

- [non-blocking] `/keyframe_review/8/correction`: Keyframe 1264-1423 draws all of admin1 Thüringen, including Orlamünde and Weimar, which house-of-ascania (eu-09) holds until it loses them to margraviate-of-meissen in 1344 and 1372; this dossier has no matching gains. Evidence: house-of-ascania /ledger/4 ('Orlamünde was sold to the Wettins on April 25, 1344') and /ledger/8 (Weimar annexed after Herman VI, 1372). Fix: Add gains 1344 (Orlamünde) and 1372 (Weimar) cp house-of-ascania and carve both out of the shape before those years; or end the dossier where the group's era allows and leave the later years to eu-09. Non-blocking for this batch (post-1250), routed to both sides.
- [non-blocking] `/ledger/8/counterpart`: duchy-of-bohemia's Cliopatria row ends in 1002 and has no dossier yet; the 1076 counterpart is outside its life. Evidence: polities.csv duchy-of-bohemia 896-1002; Margraviate of Meissen page: Egbert II 'had to renounce the Milceni lands to Duke Vratislaus II of Bohemia in 1076'. Fix: Routing: eu-15 must carry Bohemia 1002-1198; keep the slug.
- [non-blocking] `/ledger/1/counterpart and /ledger/3/counterpart`: Free strings 'March of Merseburg and Zeitz' and 'Slavic rebels (Great Slav Rising)' that are neither slugs nor listed in counterparts_needing_dossiers. Evidence: Margraviate of Meissen page: 978 Rikdag 'incorporated the marches of Merseburg and Zeitz'; 983 the March of Zeitz was overrun and the Germans pushed back west of the Elbe. Fix: Use nobody for both (no dossier will exist for either) and keep the names in the notes.
- [thin] `/keyframe_review/6`: Lower Lusatia and the Osterland under the Wettins 1089-1242 (the shape is a 60 km circle at Meissen for 167 years). Try: https://en.wikipedia.org/wiki/March_of_Lusatia
- Spot checks: `/ledger/1` confirmed (978); `/ledger/5` confirmed (1018 Bautzen, Milceni); `/ledger/6` confirmed (1031); `/ledger/8` confirmed (1076); `/ledger/10` confirmed (1243 Pleisseland in pawn); `/ledger/13` confirmed (1264)
- Area: No infobox area; acknowledged. Overlap with electorate-of-saxony from 1363 flagged by the author.

## lombard-league: fix

- [non-blocking] `/identity/type`: A dossier typed umbrella: research-brief rule 4 asks for type umbrella for associations, the reviewer brief says an umbrella is never a dossier of its own. The orchestrator must rule; nothing else in the dossier is wrong. Evidence: Lombard League page: 'a military alliance', 'one of the first examples of confederation in Europe'. Fix: Orchestrator decision; if umbrella dossiers are not allowed, drop it and give march-of-verona a territorial successor. Non-blocking for the author.
- [thin] `/keyframe_review/0`: Membership changes (Peace of Constance 1183; the later league) and cities that stayed imperial; the shape is three whole regions for 83 years. Try: https://en.wikipedia.org/wiki/Peace_of_Constance
- Spot checks: `/ledger/0` confirmed (oath of Pontida, 7 April 1167); `/ledger/1` confirmed ('dissolved in 1250 when Frederick II died')
- Area: No infobox; acknowledged.

## duchy-of-lower-lorraine: fail

- [BLOCKING] `/keyframe_review/0-4/correction, /ledger/0, /ledger/9`: The shape takes all of Belgium, so Crown Flanders west of the Scheldt (a French fief: county-of-flanders, kingdom-of-france) is drawn as Lower Lorraine 959-1058 and partly after; Luxembourg, which the page includes, is left out. Evidence: Duchy of Lower Lorraine page lead: 'almost all of modern Netherlands, Belgium, Luxembourg, and parts of modern Germany and France'; Duchy of Brabant page: only 'Imperial lands up to the Schelde river in the west came under the rule of the French Counts Baldwin V of Flanders by 1059'. Fix: Correction = Belgium minus West Flanders and Oost-Vlaanderen west of the Scheldt, plus country Luxembourg, plus the Netherlands and the Aachen/Cologne circles.
- [BLOCKING] `/ledger`: No loss when prince-bishopric-of-liege (found 980) and prince-bishopric-of-utrecht (found 1024) take their lands, which stay inside this shape to 1190: double-drawn within the batch. Evidence: prince-bishopric-of-liege /ledger/0 (980, Huy) and prince-bishopric-of-utrecht /ledger/0 (1024; Nedersticht, Overijssel, Drenthe, part of Groningen); Duchy of Lower Lorraine page lists both prince-bishoprics among the fiefs that came to imperial immediacy in its area. Fix: Add losses 980 (cp prince-bishopric-of-liege) and 1024 (cp prince-bishopric-of-utrecht) with new keyframes; those found events then name duchy-of-lower-lorraine. If the author holds that the bishoprics stayed under the duke, use vassal_start/vassal_end on both sides instead.
- [applied] `/ledger/7/counterpart`: Free string 'Bishopric of Liège' while prince-bishopric-of-liege carries the 1096 gain. Evidence: prince-bishopric-of-liege /ledger/2; Duchy of Lower Lorraine page: 'the bishopric was further expanded with the Duchy of Bouillon in 1096'. Fix: Set to prince-bishopric-of-liege (done).
- [non-blocking] `/ledger/3/counterpart and /ledger/4/counterpart`: duchy-of-lorraine exists (Cliopatria row) but starts in 1431; Upper Lorraine 959-1431 has no dossier and the author's suggested slug is taken. Evidence: duchy-of-lorraine identity start 1431. Fix: Routing: new dossier for Upper Lorraine under a free slug (for example duchy-of-upper-lorraine), then point these two events at it.
- [non-blocking] `/identity/successors`: county-of-brabant and county-of-holland (eu-10 dossiers) begin in 1260; the land is undrawn 1190-1259. Evidence: county-of-brabant and county-of-holland identity start 1260. Fix: Routing to eu-10 / Low Countries batch.
- Spot checks: `/ledger/0` confirmed (959); `/ledger/3` confirmed (1033-1044); `/ledger/5` confirmed ('by 1059'); `/ledger/7` confirmed (1096); `/ledger/9` confirmed (1190, Schwäbisch Hall)
- Area: No infobox area; acknowledged (gazetteer about 87,000 km2).

## northern-march: fix

- [applied] `/ledger/4/counterpart`: Free string 'Hevelli (Pribislav-Henry)' instead of the slug listed in counterparts_needing_dossiers. Evidence: Author report: hevelli 928-1157; Northern March page: 'In 1150, Albert formally inherited Brandenburg from its last Hevelli ruler'. Fix: Set to hevelli (done).
- [non-blocking] `/keyframe_review/0-2`: The Altmark circle lies inside stem-duchy-of-saxony's shape; once Saxony records the relation (blocking there), add the mirror here. Evidence: See stem-duchy-of-saxony finding 1. Fix: Mirror whatever Saxony adds (vassal_start/vassal_end with stem-duchy-of-saxony, or found from it). Non-blocking here.
- [non-blocking] `/ledger/1`: lutici's found event names holy-roman-empire, not this march, as the 983 loser; holy-roman-empire also records a 983 loss to lutici. Evidence: lutici /ledger/0; holy-roman-empire /ledger/4. Fix: Nothing here; lutici's note should mention the Northern March.
- Spot checks: `/ledger/0` confirmed (after Gero's death in 965); `/ledger/1` confirmed (983); `/ledger/3` confirmed (1134); `/ledger/4` confirmed (1150); `/ledger/5` confirmed (1157)
- Area: No extent or area on the page; acknowledged.

## duchy-of-zahringen: fix

- [non-blocking] `/ledger/5/counterpart and /ledger/6/counterpart`: The 1173 gain (Zürich, cp 'Counts of Lenzburg') and the 1198 gain (Ortenau and Schaffhausen, cp holy-roman-empire) take land that stem-duchy-of-swabia still draws; Swabia must record the losses (blocking there) and these events should then name stem-duchy-of-swabia. Evidence: stem-duchy-of-swabia /keyframe_review/1 keeps Baden-Württemberg, Zürich and Schaffhausen to 1268; House of Zähringen page: Lenzburg extinction 1173, 'Schaffhausen (acquired 1198)'. Fix: Set both counterparts to stem-duchy-of-swabia once Swabia adds the losses; keep the Lenzburg counts and Philip's payment in the notes.
- [non-blocking] `/ledger/3`: The 1156 loss is of 'the lands south of Lake Geneva', which no keyframe or vassal region of this dossier ever drew (the rectorate region is Bern, Fribourg, Vaud); county-of-savoy exists in polities.csv only from 1260 and has no dossier. Evidence: House of Zähringen page: 'The territories south of Lake Geneva were conceded to Savoy and Provence in 1156.' Fix: Either add the land to the rectorate vassal region 1127-1156 and make this a vassal_end, or keep it as a caption with the note saying so; routing: the Savoy owner must start before 1156.
- Spot checks: `/ledger/0` confirmed (1098); `/ledger/2` confirmed (1127 rectorate); `/ledger/3` confirmed (1156, Savoy and Provence); `/ledger/5` confirmed (1173); `/ledger/6` confirmed for Schaffhausen 1198; the Ortenau and Breisach are from the Berthold V page, not re-opened; `/ledger/8` confirmed (1218, Urach and Kyburg)
- Area: No area on the House page; the Duchy of Zähringen page did not load for the author either; acknowledged.

## archbishopric-of-magdeburg: thin

- [non-blocking] `/ledger/0`: The 1180 found from stem-duchy-of-saxony has no matching successor entry in Saxony. Evidence: See stem-duchy-of-saxony finding 2. Fix: Nothing here; Saxony adds the successor.
- [thin] `/keyframe_review/0`: One shape for 1180-1647 with no territorial event: the submission of Halle (1478) and the cession of the exclaves to Saxony, which the Peace of Prague page may date to 1635 rather than 1648. Try: https://en.wikipedia.org/wiki/Peace_of_Prague_(1635)
- [thin] `/keyframe_review/0`: Temporal lands before 1180 (the author's start is the 1180 immediacy, confidence 2). Try: https://en.wikipedia.org/wiki/Wichmann_von_Seeburg
- Spot checks: `/ledger/0` confirmed ('Gained immediacy at breakup of Saxony: 1180'); `/ledger/1` confirmed (Halle 'from 1503' in the infobox); `/ledger/2` confirmed (1635, August of Saxe-Weissenfels); `/ledger/3` confirmed (the Jüterbog page has 1648); `/ledger/4` confirmed (1680)
- Area: No area on the page ('rather small'); acknowledged.

## prince-bishopric-of-liege: fix

- [applied] `/ledger/4/confidence`: Confidence 3 for the 1213 annexation of Moha, but the page gives no year for it. Evidence: Battle of Steppes page: 'In 1212, Albert II, Count of Dagsburg, the last ruler of the County of Moha, died without a son'; battle 'on 13 October 1213'; 'Moha was annexed to Liège' (undated). Fix: Lowered to 2 with a reviewer note (done).
- [applied] `/ledger/2/counterpart`: Free string 'Godfrey of Bouillon' while duchy-of-lower-lorraine carries the 1096 loss of Bouillon. Evidence: duchy-of-lower-lorraine /ledger/7; Prince-Bishopric of Liège infobox: 'Purchased Lordship of Bouillon: 1096'. Fix: Set to duchy-of-lower-lorraine (done).
- [applied] `/ledger/3, /ledger/7, /ledger/8 counterpart`: Free string 'County of Loon' instead of the slug listed in counterparts_needing_dossiers (the vassal pair kept the same string). Evidence: Author report: county-of-loon 1040-1366; Liège page: 'In 1366, the county of Loon was annexed to the bishopric.' Fix: Set to county-of-loon (done).
- [non-blocking] `/ledger/11`: Bouillon is modelled as a permanent loss to kingdom-of-france in 1551, but the note itself says Henry II held it 1551-1559 and confirmed Robert IV de La Marck as duke; kingdom-of-france (eu-10) has no 1551 gain. Evidence: Note of /ledger/11 quoting the Duchy of Bouillon page; kingdom-of-france ledger 1540-1560 has no Bouillon event. Fix: occupation_start kingdom-of-france 1551 and, in 1559, occupation_end plus loss to duchy-of-bouillon (in counterparts_needing_dossiers). Non-blocking (confidence 2).
- [thin] `/ledger/1`: The 1040 Haspinga grant is confidence 1 (extent disputed). Try: https://en.wikipedia.org/wiki/Hesbaye
- Spot checks: `/ledger/0` confirmed ('Secular powers obtained: 980'); `/ledger/2` confirmed (1096); `/ledger/4` year not on page: annexation undated (confidence lowered to 2); `/ledger/8` confirmed (1366); `/ledger/12` confirmed (1568); `/ledger/17` confirmed (1795)
- Area: No area on the page; acknowledged.

## prince-archbishopric-of-salzburg: thin

- [applied] `/ledger/1/counterpart`: The 1275 Rupertiwinkel gain names stem-duchy-of-bavaria, which ends in 1255; the page names Duke Louis II, i.e. Upper Bavaria, the dossier duchy-of-bavaria. Evidence: Rupertiwinkel page: 'acknowledged by Duke Louis II of Bavaria in 1275'; duchy-of-bavaria /ledger/0: 'Louis II's Upper Bavaria'. Fix: Set to duchy-of-bavaria with a reviewer note (done); routing: duchy-of-bavaria (eu-09) has no 1275 loss.
- [non-blocking] `/ledger/0`: The 1213 found from stem-duchy-of-bavaria has no matching loss in Bavaria (blocking there). Evidence: See stem-duchy-of-bavaria finding 2. Fix: Nothing here unless the author switches to a vassal model.
- [thin] `/keyframe_review/1`: Three events in 590 years: the Mühldorf exclave (Salzburg until 1802), the Carinthian and Styrian possessions (Friesach), the Zillertal, and the 1611 Berchtesgaden outcome are not drawn. Try: https://en.wikipedia.org/wiki/M%C3%BChldorf
- Spot checks: `/ledger/0` confirmed (Eberhard II prince in 1213); `/ledger/1` confirmed year; counterpart corrected; `/ledger/2` confirmed (1803 Electorate)
- Area: No area; the page says the territory was 'roughly congruent with the present-day Austrian state of Salzburg' (about 7,150 km2), which is what is drawn.

## prince-bishopric-of-utrecht: fix

- [non-blocking] `/ledger/5/counterpart and /identity/successors/0`: The 1528 successor is habsburg-monarchy (Cliopatria's Austrian Habsburg row) while the page and the author's own counterparts list put the Sticht into the Habsburg Netherlands as the Lordships of Utrecht and Overijssel. Evidence: Prince-Bishopric of Utrecht page: sold 'to Holy Roman Emperor Charles V' in 1527, 'conquered by Habsburg troops in 1528', 'the southern part of the Oversticht was transformed into the Lordship of Overijssel'; author report: habsburg-netherlands 1482-1795. Fix: Use habsburg-netherlands (and lordship-of-overijssel) as successors. Non-blocking.
- [thin] `/ledger/4`: The 1528 end of the Groningen and Drenthe fiefs is confidence 1 (the page gives 1528 in a footnote and 1536 in the body). Try: https://en.wikipedia.org/wiki/Lordship_of_Groningen
- Spot checks: `/ledger/0` confirmed (1024); `/ledger/1` confirmed (1141 fiefs); `/ledger/2` confirmed (28 July 1227); `/ledger/3` confirmed (1233); `/ledger/5` confirmed (1527 sale, 1528 conquest)
- Area: No area; acknowledged.

## prince-archbishopric-of-bremen: fix

- [non-blocking] `/identity/capitals/0`: Capital Bremen 1180-1313 lies outside the drawn shape from 1186 (keyframe 1186-1524 removes the city). Evidence: Prince-Archbishopric of Bremen page: infobox seat at Vörde 'from 1219'; body: the archbishop moved to Vörde after the city refused his residence 'from 1313'; the city was de facto out from 1186 and de jure part until 1646. Fix: Either end Bremen as capital in 1218 and start Bremervörde in 1219 (infobox), or keep 1313 and say in the note that the capital is de jure. Non-blocking.
- Spot checks: `/ledger/0` confirmed (1180); `/ledger/1` confirmed (1186 Gelnhausen); `/ledger/2-3` confirmed (Christmas 1229; 1234 Altenesch); `/ledger/5-7` confirmed (9 August 1524; 1525 Treaty of Stade); `/ledger/8-9` confirmed (summer 1627; 10 May 1632); `/ledger/12` confirmed (15 May 1648)
- Area: No area; the page says 'about a third of the diocesan territory'; acknowledged.

## Cross-dossier matrix (mismatches and missing mirrors)

- missing: stem-duchy-of-saxony 936 vassal_start cp obotrites: obotrites (eu-07) ends 946 and has no 936 vassal event.
- mismatch: stem-duchy-of-saxony 983 vassal_end cp obotrites: after obotrites ends (946); Obotrite polity 946-1167 has no dossier.
- mismatch: stem-duchy-of-saxony 1160 gain cp obotrites: after obotrites ends (946).
- mismatch: stem-duchy-of-saxony 1180 loss cp house-of-ascania: house-of-ascania (eu-09) starts 1260 with found cp null.
- mismatch: stem-duchy-of-saxony 1180 dissolve cp - / archbishopric-of-magdeburg 1180 found: Magdeburg and Bremen found from Saxony; Saxony lists neither as successor.
- mismatch: stem-duchy-of-saxony 1180 dissolve cp - / prince-archbishopric-of-bremen 1180 found: as above.
- mismatch: stem-duchy-of-saxony 965 (overlap) cp northern-march / northern-march 965 found: Altmark drawn by both 965-1157, no relation recorded on either side.
- mismatch: stem-duchy-of-saxony 959 (overlap) cp duchy-of-lower-lorraine / duchy-of-lower-lorraine 959 found: Aachen and Cologne circles drawn by both 959-1180.
- missing: stem-duchy-of-bavaria 911 gain cp kingdom-of-germany: kingdom-of-germany (eu-08-a) has no 911 loss of Carinthia; the Carinthia page has Carinthia a Bavarian march from 889, so the gain may be a caption.
- missing: stem-duchy-of-bavaria 952 vassal_start cp march-of-verona: march-of-verona has no vassal_start.
- missing: stem-duchy-of-bavaria 960 vassal_start cp margraviate-of-austria: margraviate-of-austria has no vassal_start.
- missing: stem-duchy-of-bavaria 976 vassal_end cp march-of-verona: march-of-verona has no vassal_end.
- mismatch: stem-duchy-of-bavaria 1156 vassal_end cp margraviate-of-austria / margraviate-of-austria 1156 rename: Austria records a rename, no vassal_end.
- mismatch: stem-duchy-of-bavaria 1180 loss cp duchy-of-styria / duchy-of-styria 1180 found: duchy-of-styria (eu-09) founds from march-of-styria; Styria never in a Bavaria keyframe.
- missing: prince-archbishopric-of-salzburg 1213 found cp stem-duchy-of-bavaria: Bavaria keeps admin1 Salzburg to 1255 with no loss.
- mismatch: stem-duchy-of-bavaria 907 (overlap) cp stem-duchy-of-franconia / stem-duchy-of-franconia 906 found: admin1 Bayern contains region Franconia 906-939.
- mismatch: stem-duchy-of-bavaria 915 (overlap) cp stem-duchy-of-swabia / stem-duchy-of-swabia 915 found: admin1 Bayern contains the Augsburg circle of region Swabia 915-1255.
- mismatch: stem-duchy-of-swabia 1096 loss cp duchy-of-zahringen / duchy-of-zahringen 1098 found: two years apart; both pages give their year (1096 Breisgau cession, 1098 settlement).
- missing: duchy-of-zahringen 1173 gain cp Counts of Lenzburg / stem-duchy-of-swabia None None: Zürich stays in Swabia shape; Swabia records no loss.
- missing: duchy-of-zahringen 1198 gain cp holy-roman-empire / stem-duchy-of-swabia None None: Ortenau and Schaffhausen stay in Swabia shape; HRE draws all Germany so no change there.
- mismatch: stem-duchy-of-swabia 1260 (overlap) cp house-of-hohenstaufen / house-of-hohenstaufen 1260 found: same duchy drawn by both 1260-1268.
- mismatch: margraviate-of-austria 1192 vassal_start cp duchy-of-styria / duchy-of-styria 1192 rename: no vassal_end on Austria side; Styria models a rename.
- missing: duchy-of-carinthia 976 vassal_start cp march-of-styria: march-of-styria has no vassal_start.
- missing: duchy-of-carinthia 976 vassal_start cp march-of-verona: march-of-verona has no vassal_start.
- mismatch: duchy-of-carinthia 1151 vassal_end cp march-of-verona / march-of-verona 1151 rename: Verona records a rename only.
- mismatch: duchy-of-carinthia 1180 vassal_end cp march-of-styria / march-of-styria 1180 dissolve: no vassal_end on the march side.
- mismatch: lutici 991 contest_start cp holy-roman-empire / holy-roman-empire 985 contest_start: HRE contest 985-1003; Lutici 991-993.
- mismatch: lutici 1093 contest_start cp obotrites: after obotrites ends (946).
- missing: house-of-ascania 1344 loss cp margraviate-of-meissen: Meissen has no 1344 gain (Orlamünde).
- missing: house-of-ascania 1372 loss cp margraviate-of-meissen: Meissen has no 1372 gain (Weimar).
- mismatch: duchy-of-lower-lorraine 1033 gain cp duchy-of-lorraine: duchy-of-lorraine dossier starts 1431; Upper Lorraine needs its own slug.
- mismatch: duchy-of-lower-lorraine 1044 loss cp duchy-of-lorraine: as above.
- missing: prince-bishopric-of-liege 980 found cp holy-roman-empire / duchy-of-lower-lorraine None None: Liège land stays inside Lower Lorraine shape to 1190.
- missing: prince-bishopric-of-utrecht 1024 found cp holy-roman-empire / duchy-of-lower-lorraine None None: Utrecht land stays inside Lower Lorraine shape to 1190.
- mismatch: northern-march 983 loss cp lutici / lutici 983 found: lutici found names holy-roman-empire.
- missing: prince-bishopric-of-liege 1551 loss cp kingdom-of-france: kingdom-of-france (eu-10) has no 1551 gain; the land went to the La Marck dukes in 1559.
- missing: prince-archbishopric-of-salzburg 1275 gain cp duchy-of-bavaria: duchy-of-bavaria (eu-09) has no 1275 loss.

Matched: 5; exceptions (counterpart listed for a dossier or owned by a group that has not run): 24. Full list in the JSON.

## Counterparts needing dossiers (in addition to the author's list)

- Obotrite principality (continuation of the Obotrites after 946): obotrites (extend, eu-07) or principality-of-the-obotrites [946, 1167]
- Lordship of Mecklenburg (Pribislav and the Niklotings): lordship-of-mecklenburg [1167, 1348]
- Ascanian Duchy of Saxony 1180-1259 (earlier phase of house-of-ascania): house-of-ascania (extend, eu-09) [1180, 1259]
- Duchy of Upper Lorraine (the author's suggested slug duchy-of-lorraine is taken by the 1431 row): duchy-of-upper-lorraine [959, 1431]
- Patriarchate of Aquileia before 1260: patriarchate-of-aquileia (extend, eu-13) [1077, 1259]
- Duchy of Bohemia 1002-1198: duchy-of-bohemia (extend, eu-15) [1002, 1198]
- County of Savoy before 1260: county-of-savoy (extend) [1003, 1259]

## Problems

- Brief conflict: research-brief rule 4 asks for type umbrella for associations (lombard-league follows it); reviewer brief section 2.9 says an umbrella is never a dossier of its own. Orchestrator to rule.
- Nesting design: the stem duchies, marches and prince-bishoprics are drawn inside kingdom-of-germany / holy-roman-empire with no vassal relation to the crown; I treated that as intended (the group scope asks for internal states). Within the batch, though, nesting is handled inconsistently: Austria, Verona and Styria are vassal tints on the overlord side only, the Northern March and the prince-bishoprics simply overlap their duchies. Most fails in this batch come from that.
- Reviewer edits applied in place (14 field changes in 7 dossiers: march-of-styria, prince-archbishopric-of-salzburg, prince-bishopric-of-liege, duchy-of-lower-lorraine, duchy-of-carinthia, march-of-verona, northern-march); all re-validate with 0 errors and were read back unchanged. New validator warnings are only 'looks like a slug but no dossier' for slugs the author listed in counterparts_needing_dossiers.
- Every page opened loaded; WebFetch returns model extractions, so quotes are as returned. The Jüterbog page dates the exclave's passage to Saxony 1648; the Peace of Prague (1635) page was not opened and may date it 1635.
- Findings carry applied (done by the reviewer) and blocking (holds the dossier back); a 'fix' verdict here means accepted, with every remaining applied:false finding either non-blocking or a routing note for another group.
