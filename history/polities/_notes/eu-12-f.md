# Notes for group eu-12-f (Iberia and the taifas, part f)

Run of 2026-10-31. Six dossiers written and validated (python3 -I tools/validate_dossier.py, with and without --resolve: 0 errors, 0 warnings each): taifa-of-toledo, taifa-of-tortosa, taifa-of-valencia, kingdom-of-aragon, taifa-of-albarracin, taifa-of-almeria. The longer per-state notes are in each dossier's `notes` field; this file lists what the reviewer and gap-fillers need first.

## Cliopatria rows that are wrong or misdated

- Kingdom of Aragon 1015-1027 (12 cells) is exactly the County of Pallars Sobirà shape; Aragon was a county inside Pamplona until 1035. Shape marked wrong. Rows 1040/1046/1085/1126/1139 are redated against the pages (1035, 1043, 1076, 1126 only, 1134); the 1126 shape (399 cells) includes Alfonso I's Castilian possessions, which the page does not place, so the 1126 gain is confidence 1. Kingdom ends 1162 (the Crown of Aragon dossier starts then), Cliopatria 1168.
- Taifa of Toledo 1085-1093 (47,127 km2) has no support: the taifa ended in 1085 (6 May on its page, 25 May on Alfonso VI's page). Cliopatria's 1010 row is eight years before the page's 1018 independence. Córdoba 1075-1077 and the Badajoz interlude 1080-1081 are not in Cliopatria (new keyframe and loss/gain pair).
- Taifa of Valencia 1147-1151 (53,704 km2, reaching Lleida) is unsupported; from August 1147 Valencia lies in Ibn Mardanish's Murcian realm. 1241-1249 is not the taifa (it ended 29 September 1238). The 1040 row (Valencia + Almería + Murcia) holds from 1038 to 1040/41 on the pages, not 1040-1045. New keyframes for 1041-1045, 1099-1102, 1145-1147, 1228-1235.
- Taifa of Almería 1236-1240 and 1241-1249 lie in the Jaén and Granada uplands, not at Almería, and no page lists an Almería taifa after 1147: marked wrong. 1015-1033 omits Murcia, which the Murcia page gives to Almería from 1014; 1040-1045 gap filled with a new keyframe (Almería independent again from 1041). Second taifa 1145-1147 rests on the Taifa overview page only.
- Taifa of Tortosa: 1056 row cut at 1060; the 1085-1098 row includes 17 cells of Dénia (matches the Dénia infobox 'To Tortosa: 1081-1092') and is cut at 1091; 1099-1110 row cut at 1099 (page: 'from 1081 to 1099'; its ruler list runs to c. 1115, the Taifa overview ends it 1092).
- Taifa of Albarracín: rows are one-cell variants of an 8,800 km2 shape; the page dates 1012-1104 (Cliopatria 1015-1110).

## Pages that failed or were useless

- https://en.wikipedia.org/wiki/Conquest_of_Almería and .../Conquest_of_Almer%C3%ADa_(1147): url_not_found (the 1147 capture is sourced from the Almería city and Alfonso VII pages).
- https://en.wikipedia.org/wiki/Banu_Razin: url_not_found.
- https://en.wikipedia.org/wiki/Ibn_Mardanish is a disambiguation page; the article is Muhammad_ibn_Sa'd_ibn_Mardanish (opened).

## Disagreements between pages

- Toledo: 1064 (Toledo page) or 1065 (Valencia page) for the annexation of Valencia; 6 May or 25 May 1085 for the fall of Toledo.
- Valencia: surrender 29 September 1238 (Valencia page), 28 September (Crown of Aragon dossier), James I enters the city 9 October (Kingdom of Valencia page). Almería belonged to Valencia 1038-1041 (text) or 1038-1042 (infobox).
- Tortosa: acquired by Zaragoza 1060 (Tortosa page) or 1061 (Lérida page).
- Almería: Almoravid period 1091-1140 (infobox) against second taifa from 1145 (Taifa overview).
- Aragon: Crown created 1150 (Kingdom page, the wedding) or 1162 (infobox); Petronilla's abdication 18 June or 18 July 1164.

## Events other dossiers should carry (mirror or missing)

- kingdom-of-castile: no vassal_start for al-Qadir's Valencia 1086-1092 (counterpart taifa-of-valencia; ends with Ibn Jahhaf's coup, October 1092), and the Barcelona suzerainty over Valencia in 1017/18 is not recorded by county-of-barcelona. Toledo's parias from 1062 are in the Castile dossier.
- taifa-of-murcia: the Valencian period 1038-1065 and the 1145-1147 'To Valencia' infobox line should agree with the Valencia and Almería keyframes; the 1172 Almohad annexation of Valencia is there, not in the Valencia dossier.
- taifa-of-badajoz: mirror of Toledo's 1080 loss / 1081 gain; taifa-of-seville: Córdoba 1075/1077 versus its own 1075/1078 (Toledo page 1077, Córdoba page 1078).
- almoravid-dynasty: Almería 1091 (with Almería page months 'June to October or November 1091'), Albarracín 1104 (Cliopatria 1110), Tortosa 1099.
- crown-of-aragon: Valencia 1238 date and the 1239-1245 Muslim remnant south of Valencia (Cliopatria's Valencia 1241 shape).
- Córdoba 1070-1078 (Seville, Toledo): the jahwarid-taifa-of-cordoba dossier now exists (another part of eu-12); the Toledo dossier's 1075/1077 events use taifa-of-seville as counterpart, following the Toledo and Córdoba pages.

## Region names the gazetteer lacks

Alcalá de Henares, Talamanca (de Jarama), Almenara, Puig (de Santa Maria), Sangüesa, Graus, Monzón, Tudela, Calatayud, Barbastro, Albarracín, Dénia, Daroca, Fraga, Mequinenza (places); Sobrarbe, Ribagorza (regions). Coordinate radii stand in for the places used in specs.

## Page budget

Toledo 5, Tortosa 5, Almería 5, Albarracín 3 (two titles failed), Valencia 5, Aragon 6 (the sixth, Taifa of Lérida, was open for Tortosa). Shared pages (Taifa of Valencia, Murcia, Almería, Taifa overview, Lérida, Alfonso VI) are listed in each dossier that cites them.

## Repair of kingdom-of-aragon (2026-10-31, after the reviewer's verdict fail)

This section supersedes the Aragon lines above (the Cliopatria line, the Barbastro and Peter I points, the page count). Validates with 0 errors and 0 warnings, with and without --resolve.

What changed, and why (pages reopened with WebFetch, none from memory):
- Huesca (blocking): new gain 1096-11 from taifa-of-zaragoza. Battle of Alcoraz page: 'took place on 15 November 1096', siege 'nearly two and a half years' from 1094, 'Less than two weeks later, Huesca surrendered'. The 10 cells Cliopatria adds in its 1099 shape (42.0-42.4 N, 0.28-1.05 W) are this conquest; the Huesca cell (42.17 N, 0.41 W) is cut from the 1076 gain and from the 1076-1095 shapes. New war 'Siege of Huesca and Battle of Alcoraz'. I disagree with the Peter I page, which puts Alcoraz in 1095 and Huesca on 27 November 1095: the Alcoraz page, the Kingdom page (capital moved 1096) and the Zaragoza dossier (1096-11) have 1096. The capital_move is now month 11 (read from the surrender; the Kingdom page gives only the year), so it follows the gain.
- Graus-Barbastro cells (blocking): seven cells of Cliopatria's 1046 shape (42.09-42.25 N plus the cell at 42.19 N, 0.21 W east of Huesca) are cut from 1043-1082; the 1043 gain no longer carries them. The keyframes are now stepped to match the ledger: 1040 (without the two Sangüesa cells, which Cliopatria already had in 1040), 1046, 1085, new 1083 (Graus), 1089 (Monzón), the 1099 shape drawn 1096-1099, new 1100 (Barbastro), 1105, 1107, then 1111. I checked by grid that every gain region lies in the shape of its year and not in the shape before it (1043 to 1146).
- 1099 to 1111 (the reviewer asked to check): Cliopatria's 1111 shape has 19 cells more than its 1099 shape; 7 are round Barbastro and Monzón, 12 are not. The Alfonso I page dates 1105 ('conquered Ejea and Tauste and refortified Castellar and Juslibol') and 1107 ('took Tamarite de Litera and San Esteban de Litera'); two new gains and keyframes carry them, counterpart taifa-of-zaragoza (a reading: the pages name no holder). The page has the Battle of Valtierra in 1106, not 1110. One cell of the 1099 shape (42.0 N, 0.67 W) is missing in Cliopatria's 1111 and 1118-base shapes and back in 1126; I keep it.
- Notes of keyframe 1099 and of the Barbastro gain rewritten: Barbastro and the Cinca are 1100 (Lérida page; Peter I page 'Barbastro fell in 1100'); Sariñena, Pomar de Cinca and Albalate de Cinca lie south of Cliopatria's 1111 shape and are named, not drawn.
- Tudela: counterpart almoravid-dynasty; dated 25 February 1119 from es.wikipedia Tudela ('reconquistada definitivamente ... el 25 de febrero de 1119'), confidence 3. The Tudela area (5 cells outside the 1111 shape) is now in the 1118 keyframe; the 1126 gain region no longer repeats it. Alfonso I page: Tudela is listed without a year and the page does not name the holder.
- Peter I: 1094-1104 (Peter I page: 'He reigned until his death in 1104', late September).
- Thin items. Castilian possessions: the Urraca page has the marriage in October or November 1109, Urraca's grant of her land in December 1109 and, after the fall 1112 truce, 'Alfonso occupied a significant portion of Castile'; it names no town and no end year. Not enough to draw an extent, so 1126 stays a bridge (confidence 1). Sangüesa: the Ramiro I page (en) has it after Tafalla within 1036-1043; the es.wikipedia page has the war from spring or summer 1043, Tafalla soon after, a reconciliation in 1044, 'el castillo de Sangüesa' in the alliance of c. October 1057 and Ramiro reigning 'desde Vadoluengo (término de Sangüesa) hasta Ribagorza' in 1049. The pages disagree; 1043 kept at confidence 1. The es page also has Sobrarbe and Ribagorza 'a partir de 1043' and, in its introduction, 'por muerte de su medio hermano Gonzalo en 1045', which explains the 1043 against 1045 mismatch with county-of-ribagorza. Barbastro 1064-1065: Siege of Barbastro page, crusade of August 1064, 'Armengol III of Urgel ... was entrusted with the government of the city', retaken 17 April 1065; not an Aragonese gain, so a contest (1064-08 to 1065-04, counterpart taifa-of-lerida) and a war. Tauste 1146: the Kingdom of Navarre page is silent; the García Ramírez page ('In 1146, he occupied Tauste, which belonged to Aragon'; Alfonso VII mediated) is the Navarre dossier's own source; contest_start and contest_end 1146 (counterpart kingdom-of-navarre) and a war added.
- Monzón: the Peter I page gives 24 June 1089; the Sancho Ramírez page (the event's source) only the year, so no month was added.

Cross-dossier items for their owners: taifa-of-zaragoza has no 1105 (Ejea, Tauste) or 1107 (La Litera) loss to kingdom-of-aragon and no Barbastro/Tauste contests; taifa-of-lerida should move Monzón to 1089 and add the 1064-1065 Barbastro contest; almoravid-dynasty needs the 1119 Tudela loss; kingdom-of-castile needs the 1126 loss and 1127 gain (still bridged).

Pages opened in the repair (seven, over the budget of five, at the reviewer's request): Battle of Alcoraz, Peter I of Aragon and Navarre, Siege of Barbastro, Urraca of León and Castile, es.wikipedia Ramiro I de Aragón, es.wikipedia Tudela (Navarra), García Ramírez of Navarre; the Kingdom of Navarre page (thin item) was silent on Tauste and Alfonso I was reopened for 1104-1111. Gazetteer additions: Huesca (as a place; only the province is in admin1), Tauste, Ejea, Tamarite de Litera.
