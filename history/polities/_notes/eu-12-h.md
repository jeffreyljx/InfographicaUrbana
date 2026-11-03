# Notes for eu-12-h (Iberia and the taifas, part h)

Written 2026-10-25. Six dossiers: taifa-of-seville, taifa-of-zaragoza, taifa-of-algeciras, taifa-of-saltes-and-huelva, taifa-of-santa-maria-do-algarve, county-of-pallars-jussa. Every dossier validates (0 errors). Pages were read through WebFetch, which returns a summary of the page rather than its raw text, so quotes are as WebFetch returned them. No infobox of any of the six states gives an area; Cliopatria shapes were checked by size, bbox and gazetteer overlay only (the Pallars Jussà comarca page gives 1,343 km2 against Cliopatria's 1,596-1,620).

## Cliopatria rows that are wrong or shifted

- Taifa of Zaragoza 1015-1017: 1,668 km2 on the Pallars bbox (0.63-1.19E, 41.91-42.37N), identical to the County of Pallars Jussà box and far from Zaragoza city; marked wrong, the 1018 shape applied back to 1013.
- Taifa of Zaragoza 1040-1110: every shape contains the Lleida district although both the Zaragoza and the Lérida pages put a separate Taifa of Lérida (Hudid) from c. 1040 to c. 1105/1110. Marked adjust (Lleida removed). Cliopatria has no Lérida row: a dossier taifa-of-lerida is needed or Lleida will draw as a hole.
- Taifa of Zaragoza 1066-1084 is Zaragoza plus Tortosa (Cliopatria's Tortosa 1056 shape lies wholly inside it): Tortosa to Zaragoza 1060, back to Mundhir 1081 (Tortosa page). Dénia, taken in 1076 (Lérida page), is not in any Zaragoza shape (new 1076 keyframe).
- Taifa of Algeciras 1028-1039 contains about 1,500 km2 of Morocco (the first version said 2,700) and, like every other Cliopatria 'Taifa of Algeciras' shape, is mostly Málaga province; see the review repairs below. Replaced by Algeciras and a 30 km radius.
- Taifa of Algeciras 1085-1093: no page has a taifa then; Seville held Algeciras from 1055 and handed it to the Almoravids in July 1086. Marked wrong; the shape does not contain Algeciras (Antequera and Coín country, Málaga province).
- Taifa of Algeciras 1147-1168: marked wrong after review (the Abd al-Mu'min page has the Almohads take Algeciras in 1147; the shapes lie in Málaga province); the two conf-1 events are deleted and the dossier ends in 1055. Taifa of Saltés and Huelva 1147-1151: unverified, page silent (second taifa period); kept as ok with conf-1 events. The Saltés and Huelva 1147 shape is exactly the 1015 geometry. The Tejada page (1146-1150, Huelva province) and the Niebla page (1145-1150) may be what Cliopatria draws.
- Years shifted by Cliopatria: Seville 1028 (page 1023), 1056 shape from 1051/1055, 1072 shape from 1070, 1085 shape from 1078, end 1093 (page September 1091); Saltés and Huelva and Santa Maria do Algarve end 1055 (page 1051); Pallars Jussà starts 1040 (page 1011) and ends 1191 (page 27 May 1192).

## Disagreements between pages

- Seville: 1023 (lead, infobox) against 'after its downfall in 1031' (body). Algeciras taken by Seville in 1055 (Abbad II page, Algeciras body and city page) against 1058 (Algeciras infobox, Taifa list). Arcos 1069 (Abbad II page) against 1068 (Arcos page, read by another agent). Córdoba lost 1075 (al-Mu'tamid page; Toledo page 'conquering the taifa of Córdoba in 1075') against 'The Cordoban lands were lost in 1077' (Toledo page); regained 1078 only on the al-Mu'tamid page.
- Algeciras: 'created in 1013' (body) against 1035-1058 (lead, infobox, city page); annexed to Málaga in 1035 yet Muhammad ibn al-Qasim's reign starts 1035 in the infobox and he is proclaimed in 1039 in the body. The ledger follows the body.
- Zaragoza: 1013 (infobox, rulers) against 1018 (Taifa list; the Caliphate dossier hands the land over in 1018). Tortosa 1060 (Tortosa page) against 1061 (Lérida page). Ahmad al-Muqtadir 1046 (Zaragoza page) against 'from 1049' (his own page).
- Saltés and Huelva: infobox 'Preceded by: Taifa of Badajoz' against the Caliphate dossier's 1012 loss to this taifa; same for Santa Maria do Algarve ('Preceded by: Taifa of Badajoz', no year).

## Pages

- Failed: https://en.wikipedia.org/wiki/Taifa_of_Santa_Mar%C3%ADa_do_Algarve (url_not_found; the unaccented title opened) and https://en.wikipedia.org/wiki/Ahmad_I_al-Muqtadir (url_not_found; Ahmad_al-Muqtadir opened but is a stub with one dated sentence).
- 'Pallars_Jussà' is the modern comarca, not the county; the county is at County_of_Pallars_Jussà. Al-Mu'tamid (without ibn Abbad) is the Abbasid caliph.
- Thin: Kingdom of Aragon (no conquests dated except the 1096 capital move to Huesca), Algeciras city (nothing 1100-1199), Almohad Caliphate (no Algeciras, Huelva, Saltés), Taifa article second-period list (no Algeciras, Saltés, Huelva).

## Needed from others

- Dossiers: taifa-of-lerida (Hudid Lérida, 1039/1046-1102/1110, Cliopatria lacks it); taifa-of-malaga (Hammudid then Zirid Málaga; the Taifa list gives 1026-1057/1058 and 1073-1090); taifa-of-mertola (conquered by Seville 1044-45; the Taifa list has a second Mértola taifa 1144-1145); the first Taifa of Córdoba 1031-1070 (taifa-of-cordoba starts in 1147 and the Caliphate dossier ends in 1031, so Seville's 1070 gain from Córdoba has a counterpart with no ledger).
- Castile and León dossiers: Seville a tributary from 1063 (Ferdinand I appeared before Seville; later Alfonso VI), Zaragoza's parias (1060, 1076, 1097); Barcelona: tribute from 1045 of the brothers of Zaragoza and Lérida. No event type records being a vassal, so they are not in these dossiers.
- Almoravid dossier: Algeciras from July 1086 (a base; the Almoravids landed there again in May-June 1088); Murcia 1091 (Murcia infobox 'To Seville/Almoravids: 1078-1091 / 1091-1145').
- Seville's 1085 shape grows by about 30,000 km2 over the 1072 shape; Murcia (Cliopatria 6,298 km2) and Córdoba's return explain a part; the rest is unexplained by any dated page.
- Gazetteer: Mértola (place, Portugal), Lleida (place, Spain). Saltés and La Pobla de Segur are used only as capital coordinates.

## Review repairs (2026-10-25)

Repairs after the adversarial review (taifa-of-seville, taifa-of-zaragoza, taifa-of-algeciras; the other three dossiers were not touched). All three validate with 0 errors; pages re-opened through WebFetch on 2026-10-25.

Applied:

- taifa-of-algeciras: every Cliopatria 'Taifa of Algeciras' shape is mostly Málaga province (grid cells in Málaga province: 18 of 33 in 1028, 15 of 21 in 1040, 12 of 14 in 1085, 16 of 18 in 1147-1168; only the 1040 shape touches Cádiz, 5 cells). Keyframes 1013, 1028 and 1040 now use {place Algeciras, 30 km, Spain}; ledger 0-3 and the wars use the same region. The 1147 and 1152 keyframes are 'wrong' (Abd al-Mu'min page: 'In 1147 Abd al-Mu'min sent a military force led by another Almoravid defector, Abu Ishaq Barraz, who captured Algeciras and Tarifa'; Taifa article second-period list: 'Málaga: 1145–1153 (to Almohads)', no Algeciras; Taifa of Algeciras page: no second taifa, nothing after 1058). The two conf-1 second-period events are deleted; the dossier ends in 1055 (loss plus dissolve to taifa-of-seville), identity.end, capital 'to', ruler 'to', certainty and successors moved to match. Moroccan part of the 1028 shape corrected to about 1,500 km2 (6 of 33 grid cells).
- taifa-of-seville: ledger/7 (1055 gain) and ledger/17 (July 1086 loss) now name {place Algeciras, 30 km, Spain}; the 1085 keyframe correction subtracts that district (the first version subtracted Cliopatria's Algeciras 1085 shape, which does not meet Seville's); the first war's zone matches. ledger/13 note carries the Seville page's 1071 variant ('Al-Mu'tamid seized Córdoba in 1071, with a brief interlude in 1075–1078'); 1070 kept (al-Mu'tamid and Toledo pages). Mértola note updated (Mértola page: independent taifa from 1031, conquered 1044-1045).
- taifa-of-zaragoza: the 1076 keyframe, ledger/4 (1076 gain) and ledger/8 (1081 loss) take Dénia's peninsular possessions only (the Dénia 1066 shape runs to 4.30E and holds the Balearic Islands; the Dénia page keeps the Balearic taifa independent to 1116); ledger/8 names taifa-of-tortosa as counterpart (Dénia did not become independent in 1081; Dénia infobox 'To Zaragoza/Tortosa/Almoravids: 1076–1081 / 1081–1092 / 1092–1224'). The 1066 keyframe note gives Tortosa 1056 as 6,768 km2 and records the 4,800 km2 western strip (Medinaceli country) as unverified: page budget. Huesca 1096 (ledger/9, keyframe 1099) now rests on the Battle of Alcoraz page (15 November 1096; 'Less than two weeks later, Huesca surrendered'), month 11 added.

Where I did not follow the review, and why:

- Calahorra (Zaragoza): no event or keyframe added. The Taifa of Zaragoza page does not mention Calahorra; the Calahorra page says only 'García Sánchez III of Pamplona captured the city in 1045' and names no taifa; no Zaragoza shape contains it. The kingdom-of-pamplona dossier (ledger/25, counterpart taifa-of-zaragoza, conf 2) and the caliphate-of-cordoba dossier (ledger/34, Calahorra passes to Zaragoza in 1018 'by reading') should switch to 'nobody' or add the land to Zaragoza themselves.
- Western Upper March 1046-1066 (Zaragoza): no loss event. The Ferdinand I page has the 1060 invasion take San Esteban de Gormaz, Berlanga and Vadorrey, but the first two lie outside every Zaragoza shape and the Medinaceli page is silent for the century; a conf-1 loss to Castile would be a guess (Toledo is as likely). Left as 'unverified: page budget'.
- Seville /ledger/13: 1070 kept as the date (al-Mu'tamid and Toledo pages) beside the Seville page's 1071; the note says so.
- Algeciras end year: 1055 (Abbad II and Algeciras bodies) rather than the infobox's 1058, so that the Seville gain and the Algeciras loss agree.

Thin items tried: Ibn Ammar (page has no campaigns), Jaén (Granada's under Habbus, undated; Almoravid 1091; Seville not mentioned), Lorca (independent taifa from 1042), Medinaceli (silent), Lérida (silent on who held Lleida in 1078-81 and on Yusuf's fate). Seville's Jaén, Baeza and Lorca (54 grid cells, about 13,700 km2, in the 1085 shape and 3 cells in the 1072 shape) stay unexplained; taifa-of-granada ledger/8 (1085 loss to an 'unnamed neighbour') may be the other side. Monzón and Barbastro remain inside the corrected Zaragoza 1085 and 1099 shapes while the taifa-of-lerida dossier gives them to Lérida.

Counterparts, status on 2026-10-25: taifa-of-malaga (found 1026, gain 1035 and loss 1039 against taifa-of-algeciras, 1145 gain and 1153 loss in the second period), taifa-of-mertola (found 1033, loss to Seville 1044) and taifa-of-lerida now exist. Cliopatria has no Málaga row, so the 'Taifa of Algeciras' shapes of 1028-1039, 1040-1065, 1085-1093 and 1147-1168 (all Málaga-province land) are in effect Málaga's; the taifa-of-malaga owner may want to review them. Still missing: taifa-of-cordoba for its first period (1031-1070; the existing dossier starts in 1147) and taifa-of-tortosa (named as counterpart in Zaragoza ledger/3, /7 and /8; the file is not yet there). The Almoravid dossier names Algeciras only in the 1147 loss, with no July 1086 gain; Pamplona and Caliphate owners on Calahorra (above). Gazetteer names used: Mértola, Lleida, Dénia (places).

