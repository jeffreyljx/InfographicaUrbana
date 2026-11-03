# Notes, group eu-15-e (Poland: Sandomierz, Silesia, Pomerania, Wrocław)

Written 2026-10-25. Dossiers written: duchy-of-sandomierz, duchy-of-silesia (with the Cliopatria row "Duchy of Wrocław" merged in), pomerania. No dossier duchy-of-wroc-aw exists. All validate (`validate_dossier.py`, errors 0); `--resolve` leaves only the unknown place names listed at the end. Pages were read with WebFetch on 2026-10-25; 19 distinct pages, 23 source entries.

## Row decisions

- **Duchy of Silesia + Duchy of Wrocław = one state.** Both rows carry Wikidata Q568638, the Cliopatria Wikipedia title "Duchy of Wrocław" is not an article of its own (Duchy_of_Wroc%C5%82aw and Duchy_of_Wrocław returned url_not_found; Duchy_of_Breslau returned the Duchy of Silesia article; Duchy_of_Wroclaw returned an article on the title Duke of Silesia). One dossier under the earlier slug, `cliopatria_names: ["Duchy of Silesia", "Duchy of Wrocław"]`, all 17 shapes reviewed.
- **But the three Wrocław-row shapes are not Wrocław.** They lie on Upper Silesia (96% of their cells in the Upper Silesia region; they hold Opole, Bytom and, in 1169-1176, Racibórz). The pages put Wrocław in Lower Silesia (Bolesław I, 1163-1201) and send Racibórz to Mieszko Tanglefoot and an Opole strip to Jarosław in the partition of 1172 (Silesia page; 1173 on the Bolesław I page). Verdicts: 1169 adjust (Silesian to 1171), 1177 and 1192 wrong (use the Duchy of Silesia shape). Upper Silesia 1172-1201 then has only Cliopatria's Duchy of Opole row (1177-1201, 6.5 thousand km2); a Duchy of Racibórz dossier for 1172-1284 is needed.
- **Duchy of Sandomierz big shapes.** The 1188-1201, 1206-1209, 1216-1226 and 1250-1278 shapes (113-142 thousand km2) are the realm of the High Duke from the Sandomierz line (Casimir II, Leszek the White, Bolesław V), with Pomerelia, Kuyavia and half of Masovia thrown in. The pages support Sandomierz + Lesser Poland (+ Masovia 1186-c. 1200), so these are `adjust`. The Seniorate is drawn by Cliopatria under other rows in other years (Masovia 1147-1176, Greater Poland 1177-1187, 1202-1205 and 1227-1235, Opole 1210-1215, Silesia 1139-1146 and 1236-1249): the Masovia, Greater Poland and Opole dossiers should agree on the hand-over years in the Sandomierz and Silesia ledgers (1177, 1186, 1198, 1199, 1206, 1210, 1211, 1228-1232, 1241, 1243).
- **Pomerania** is the Griffin Duchy of Pomerania (Wikipedia "Duchy of Pomerania"; the Cliopatria Wikipedia field points to the regional article "Pomerania", which has nothing for 1138-1187). Start 1138 (Polish overlordship ends), end 1187 (Bogislaw I dies; Cliopatria folds the land into its Danish realm 1188-1228, the Empire by 1240). The duchy itself continued to 1637.

## What could not be settled

### duchy-of-sandomierz
- Ends in 1304 (last Cliopatria shape); the page says 1320 (infobox 1320, title bar 1304-1333). 1305-1320 belongs to Cliopatria's Kingdom of Poland row (covers Sandomierz and Lublin 1305-1334), so an Elbow-high Sandomierz would double-draw.
- The 1294 shape drops 22 cells (about 4,900 km2) in the east, all inside Cliopatria's Galicia-Volhynia shape of 1294; no page opened dates it (ledger loss at confidence 1; the Leo I of Galicia page has nothing on Lublin Land).
- Cliopatria's outline ends about 35 km north of Wiślica, which the page lists among the twelve castellanies; the found event adds it. Radom stays inside the outline all along (lost 1235, back 1239 at confidence 1).
- Ruler list conflicts (Bolesław V 1227-1279 vs regencies of Grzymisława, Henry the Bearded 1231-1234 and Henry II 1238-1239; "Bolesław I of Masovia 1229-1232" on no other page); the 1194 succession split vs the division "ca. 1200".
- Henry the Bearded's and Henry II's regencies of Sandomierz are carried in the Silesia dossier as vassal_start/vassal_end.
- Not carried: Leszek's lost "small area between the Narew and Bug" (1218, holder not named), Casimir II's Kalisz and Gniezno 1177-1182, Mieszko III's occupation of Kuyavia after 1186, a dated vassal tie of Pomerelia (no page dates it).
- Ten pages opened against a budget of 9 (the Wenceslaus II page was thin; the Leo I of Galicia page was a targeted attempt on Lublin Land that came back empty).

### duchy-of-silesia
- Ends in 1304 with the Cliopatria row; the page runs the Wrocław duchy of Henry VI the Good to 1335 (1327 treaty with John of Bohemia, Trentschin 1335, Namysłów 1348). Cliopatria draws Wrocław in its Duchy of Legnica row 1305-1313 and in Bohemia from 1314. A one-keyframe extension (the 1304 shape for 1305-1335) is the gap-filler's job.
- No territory 1147-1162: Bolesław IV "took control" in 1146 and the sons returned in 1163; Cliopatria's Masovia row carries it.
- Partition dates: infobox 1172, Bolesław I page "beginning of 1173", the Duke of Silesia table 1163 (Opole-Racibórz) and 1173. Głogów returned c. 1185 (infobox) or 1190 (text, Bolesław I page): 1190 used. Lubusz: "regained" (Silesia page) vs "took" on 6 May 1210 and "held until 1218" (Henry I page); the 1218-1229 holder is on no page; the 1248-1250 sale to Brandenburg (Silesia page) or half to the Archbishop of Magdeburg (Henry III page).
- The Cliopatria 1279 outline gains 28 cells (6.3 thousand km2) that lie in the Duchy of Głogów's 1278 shape; no page explains it (confidence 1).
- Not carried for want of a dated end or extent: Kalisz seized 1284 and later traded for Ołobok, Wieluń ceded by Przemysł II in February 1281, Santok reclaimed 1239, the Bohemian guardianship under Ottokar II (1270-1273), the Nysa bishopric (1290), the 1296 partition of Henry V's heritage (the sons' shares are on no page opened).
- The Henry II page calls the 1241-1248 duke Bolesław II "the Horned"; the Silesia page "the Bald".
- Eleven pages opened (budget 9 + 2); two are aliases (Duchy of Breslau, Duke of Silesia).

### pomerania
- The dossier ends at the Cliopatria row (1187); the duchy goes on (Denmark 1185-1227, Empire 1227-1637 per the infobox). A dossier "duchy-of-pomerania" for 1188-1637 is needed; Cliopatria shows Danish and then imperial shapes over the land.
- The 1169 trim of the west (12 cells, about 2,650 km2, Demmin-Tribsees) has no page behind it (ledger loss at confidence 1, counterpart the Holy Roman Empire whose Cliopatria shape covers Demmin from 1169).
- Vassal ties of Pomerania (Poland 1121-1138, Saxony 1164-1181, Empire 1181-1185, Denmark 1185-1227) are on the page but no event type records a state as a vassal; the suzerains' dossiers (Poland, Holy Roman Empire, Denmark; Saxony has no Cliopatria row before 1363) should carry them.
- The 1155 partition into Pomerania-Demmin and Pomerania-Stettin is internal (one row). No area on either page opened, so no infobox comparison was possible for any of the four rows.

## Counterparts needing dossiers

- Duchy of Racibórz 1172-1284 (slug duchy-of-raciborz exists for 1285-1304), including Bytom, Oświęcim and Pszczyna from c. 1177 (Casimir II page).
- Duchy of Legnica 1248-1278 (slug exists for 1279-1313) and 1305-1335 for Wrocław; Duchy of Głogów 1177-1190 (slug exists for 1250-1313).
- Duchy of Wiślica 1166-1173 (Casimir II's appanage; probably not worth a dossier).
- Margraviate of Lusatia (Konrad II, to 1210) and Landgraviate of Thuringia (Lubusz claims 1218-1230): counterparts of Lubusz events in the Silesia ledger.
- Duchy of Pomerania 1188-1637.

## Gazetteer names needed (places, all in Poland)

Wiślica, Radom, Głogów, Racibórz, Legnica, Świdnica, Środa Śląska, Strzegom, Kłodzko. (Przemyśl resolves as "Przemysl".) The Demmin-Tribsees strip of Pomerania is a coordinate radius (13.0 E, 53.95 N, 45 km).
