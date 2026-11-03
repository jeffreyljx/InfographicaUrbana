# eu-16-a: Rus and Russia to 1721 (part a), notes for the reviewer and the gap-fillers

Written 2026-10-25. Dossiers: rus (the merged Cliopatria rows "Rus'" and "Kievan Rus'"), volga-bulgaria, halych-volhynia-occupation. All validate with 0 errors; every region name resolves except the deliberately empty corrections of halych-volhynia-occupation (10 resolve warnings, by design). No page failed to load.

## rus (Kievan Rus', 880-1054)

- Rows merged: "Rus'" 880-881 and "Kievan Rus'" 882-1240 share Wikidata Q1108445 and one ruler (Oleg: Novgorod 879, Kiev 882). One dossier under the earlier slug `rus`, cliopatria_names holds both. There is NO kievan-rus.json. khazaria.json (965, 969) and the principality dossiers that name the counterpart `kievan-rus` mean this dossier; the orchestrator should alias kievan-rus to rus, or the counterparts be renamed.
- End decided: 20 February 1054 (Yaroslav dies, his sons divide the land; Kievan Rus' page, Yaroslav page). The pages also give 1132 (Principality of Kiev page: the semi-autonomous states "de facto independent" after Mstislav's death; Kievan Rus' page: Mstislav the last ruler to keep a united state) and 1240 (Kievan Rus' page: the siege of Kiev is "generally understood as the end"). Reason for 1054: Cliopatria draws the principalities of Kiev, Pereyaslavl, Novgorod, Chernigov, Rostov-Suzdal, Smolensk, Volhynia and Polotsk from 1056, and subtracting them from the "Kievan Rus'" 1040-1235 shape leaves 267 cells (about 68,000 km2) in 1056 and 352 in 1100: the 1.2 M km2 shape is almost wholly double-drawn. If the principality dossiers start in 1132 instead (the Principality of Kiev infobox says established 1132), the end should move to 1132. Year 1055 belongs to this dossier's 1040 shape (the principalities start 1056 in Cliopatria); the kievan-rus_1040 shape is limited to 1040-1054 in the verdict.
- Kiev prince's nominal seniority over the other princes (1054-1240) is not territory and is not drawn.
- Unsettled: the 896 and 900 southward growth (confidence 1, no page); the 972-980 war of Sviatoslav's sons; whether Chersonesos was returned in 988-989 (occupation_end is confidence 1); what Poland took in 1018 (loss is confidence 1; the Yaroslav page dates only the 1031 reconquest); Cliopatria steps the western fringe back in 1028 where the page says 1031 (verdict adjust); the left-bank division of 1024-1036 is a loss/gain pair against principality-of-chernigov, whose dossier begins 1056, so the pair has no matching event on that side; Vyatichi and Radimichs are subdued several times (885, 966, 981-982, 984) and the pages do not reconcile them; Tartu (1030) is outside every Cliopatria shape.
- Cliopatria row to drop: kievan-rus_1236 (1,068 km2 at Tmutarakan) is not Rus' land (verdict wrong).
- No dossier for the pre-Kiev Rus' Khaganate ("a hypothetical polity", seat "actively disputed"); predecessors is empty. Askold and Dir (Kiev), the Drevlians, Yotvingians and Estonian tribes of Tartu are counterparts without dossiers (tribal, not states).
- Page budget: rus 1-2 plus kievan-rus up to 9 = 11 for the merged state; 10 pages opened (Kievan Rus', Oleg of Novgorod, Rus' Khaganate, Rus, Sviatoslav I of Kiev, Vladimir the Great, Yaroslav the Wise, Mongol invasion of Kievan Rus', Principality of Kiev, Tmutarakan).

## volga-bulgaria (674-1241)

- Start 674 is Cliopatria's (inside Kotrag's reign 665 - c. 700); the Volga Bulgaria infobox says "late 9th century". The 4,158 km2 pocket of 674-681 lies near Penza, not on the Volga; replaced by the Volga-Kama shape from 674 (verdict adjust).
- End 1241 is the page's arithmetic ("In 1236, the Mongols returned and in five years had subjugated the whole country"); Cliopatria ends 1235; the infobox says the 1240s. contest 1236-1241 with mongol-empire needs a partner event in the Mongol Empire dossier (ia-02).
- Not on the pages opened: the Rus' campaigns of 985 (in the rus dossier, Vladimir page), 1088, 1164, 1172, 1183; the move of the capital to Bilar (a century only: 12th); the Bilar coordinates (a reading of "150 km from Kazan" on the Small Cheremshan). Khazar suzerainty: mirrored here in the repair round (see below).
- The Cliopatria shape (44,000 km2, Tatarstan) is a core; the pages describe a country "around the confluence of the Volga and Kama" and give no area. A fuller extent (Bashkiria, Suar, the Kama) is not settled.
- Page budget 5, used 5 (Volga Bulgaria, Kotrag, Mongol invasion of Volga Bulgaria, Bolghar, Bilyar).

### volga-bulgaria, repair round (2026-10-25, after review eu-16-a: verdict fail)

Changed (pages re-opened with WebFetch, not fixed from memory; validates with --resolve, 0 errors, 0 warnings, 8 events):
- Added the Khazar vassalage: `vassal_start` 890 (confidence 1) and `vassal_end` 969 (confidence 2), counterpart khazaria, Volga Bulgaria page. The page gives the span only in the infobox ('Vassals of the Khazars (late 9th century-969)'); the body has 'came under the overlordship of Khazars' with no year and 'complete independence was reached after Khazaria's destruction and conquest by Sviatoslav in the late 10th century'. 890 is the mid-point of 'late 9th century', the same reading as khazaria.json /ledger/12; 969 is the infobox's year and appears nowhere in the body. Both mirror khazaria /ledger/12 and /ledger/14.
- Added the 1232 Mongol occupation: `occupation_start` 1232 (confidence 2) and `occupation_end` 1236 (confidence 1), counterpart mongol-empire, Mongol invasion page: 'In 1232 the Mongol cavalry subjugated the southeastern part of the Bashkiria' and 'occupied southern portions of Volga Bulgaria'. The page names no city or river for it. Region: the part of the 1227 shape south of 55.5 N (85 of 159 cells, about 21,500 km2; a polygon because no named region fits): a reading. Corrected the note of keyframe 3 (verdict stays ok: an occupied land stays the state's own and is hatched by the event, not cut from the shape) and the note of the war 'Mongol invasion of Volga Bulgaria'.
- Source notes of the two pages updated. No new page opened; budget 5, used 5.

Disagreements and judgement calls:
- End of the occupation: the reviewer allowed 1236-1241 or the 1241 dissolve. I closed it in 1236, the year the contest over the whole country opens, because the 1236-1241 contest zone already covers the south and a hatched layer under a blend would double-draw it; the Mongol invasion page does not say whether the occupation lasted or the Bulgars regained the land ('The page doesn't say'), so the end is confidence 1.
- The Volga Bulgaria page is silent on 1229 and 1232; only the Mongol invasion page has them. The 1229 step (Ural River frontier guards defeated, 'the upper Ural valley' occupied) is outside the Volga-Kama shape and is only in the war's note.
- The vassalage starts in the late 9th century while the dossier starts in 674 (Cliopatria's first shape; the infobox says 'Established: late 9th century'): so 674-889 carries no suzerain, because no page opened gives one. Not a disagreement with the reviewer, a limit of the pages.

For other owners:
- mongol-empire (ia-02): no `occupation_start` for this land in 1232 (the mirror of /ledger/ here), and its /ledger/25 makes 1236 a gain of Volga Bulgaria where this dossier has a contest 1236-1241 and the dissolve in 1241; the reviewer asked for the gain to move to 1241 with a contest_start in 1236.

Still thin (not applied: they are for gap-fillers and the page budget is spent): a page that dates the foundation on the Volga (the Kotrag page, opened, gives only his reign '665 - around 700'); an extent beyond the 44,000 km2 Tatarstan core (the Bilyar page, opened, gives none); the Rus' campaigns of 1088, 1164, 1172, 1183 and the peace of 1220-1221 (try the Andrey Bogolyubsky page; not opened here).

## halych-volhynia-occupation (1056-1240): a mis-attributed Cliopatria row

- The ten shapes (277,000-452,000 km2) lie on the Pontic steppe between the Dniester, the lower Danube and the Don, with Wallachia and Moldavia (to 22.5 E) in 1066-1205. They overlap no neighbouring Cliopatria polity (checked against Peremyshl, Terebovlia, Halych, Volhynia, Galicia-Volhynia, Kiev, Pereyaslavl, Chernigov, Hungary, the Byzantine Empire, the Second Bulgarian Empire; 2,000 km2 with Kievan Rus' in 1100). They read as a fill of land no other row covers.
- No page opened puts Halych, Volhynia or the Kingdom of Galicia-Volhynia on this land (the Kingdom page, the Principality of Halych page, the Bolokhoveni page are silent; the Cumania page puts the Cumans from Ukraine "to southern Moldavia"). All ten shapes are verdict wrong with an empty correction (so the resolve warnings). Dossier type umbrella, no capitals: no colour should be seeded.
- Shares Wikidata Q239502 with principality-of-galicia-volhynia and galicia-volhynia: different things, not merged.
- For the compile stage: cuman-kipchak-confederation already claims about 830 cells of the same steppe (29-39 E) and pechenegs the 1043-1090 steppe. The Wallachia/Moldavia part (22.5-29 E) is outside the Cuman dossier's "Pontic Steppe" region and would be nobody's land: the Cuman agent (ia-01) should add it ("White Cumania ... eastern Wallachia, Black Cumania ... Moldavia", Cumania page).
- Facts for principality-of-halych / principality-of-galicia-volhynia agents: Galician influence on the lower Dniester, Prut and Danube under Osmomysl (1152-1187, undated); Roman's Cuman campaigns 1201-02 and 1203-04; "briefly controlled the Brodnici on the Black Sea" (flagged as needing a citation); Daniel and the Bolokhoveni 1231-1257; Daniel took Kiev in 1239; Halych and Volodymyr devastated 1240.
- Page budget 5, used 5 (Kingdom of Galicia-Volhynia, Cumania, Principality of Halych, Bolokhoveni, Mongol invasion of Kievan Rus').

## Gazetteer names wanted
"Cherven Cities" (region around Przemysl, Chelm, Volodymyr; places Przemysl and Volodymyr used), "Yotvingia" (Sudovia; region Podlachia used), "Vyatichi land" (upper Oka; admin1 Kaluga, Tula, Orel used), "Bilyar" (place, about 50.4 E 54.65 N, Tatarstan).

## Method note
WebFetch returns a model's summary of each page; sentences in quotation marks in the dossiers are those the summary gave in quotation marks; other page content is paraphrased without quotes.
