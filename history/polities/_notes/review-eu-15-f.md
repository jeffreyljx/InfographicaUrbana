# Review of batch eu-15-f (Duchy of Opole, Duchy of Kuyavia)

Reviewer, 2026-11-01 (brief filled 2026-10-31). Pages opened with WebFetch: Duchy_of_Opole, Mieszko_I_Tanglefoot, Mieszko_II_the_Fat, Mieszko_III_the_Old, Duchy_of_Kuyavia. Both dossiers validate (`--resolve`: 5 gazetteer warnings for Opole, places Kalisz, Wieluń, Czeladź; none for Kuyavia). Neighbour ledgers read: silesia, greater-poland, sandomierz, masovia, bytom, raciborz, kalisz, kingdom-of-bohemia (wroc-aw and kievan-rus not written yet). No dossier was edited by the reviewer.

## duchy-of-opole: fail (unapplied blocking findings)

What held: every spot-checked event is on its page with its year (1201 loss, 1202 gain, 1210 gain, 1211 loss, 1234 gain, 1244 loss, 1249 loss, 1281 split). All 11 Cliopatria shapes have verdicts; the `wrong`/`adjust` reasoning for the pre-1206 shapes (Racibórz-Cieszyn, not Opole) and the 1210 High-Duke shape is sound and flagged. Capital Opole lies inside the 1206+ shapes. No infobox area exists (checked).

Findings for the author:

1. **Missing 1291 vassal_start (Bohemia).** Infobox: 'Fiefdom of Bohemia (1291–1306; 1327–1348)'. The brief needs the vassal_start in both ledgers; kingdom-of-bohemia has only Bytom 1289. Add vassal_start 1291, counterpart kingdom-of-bohemia, region the 1294 shape, confidence 2, no end inside the life (to 1306 per infobox).
2. **Missing Silesian control 1234 to 1238/39.** Mieszko II page: Henry I was 'taking the full control over Opole-Racibórz, but without denying their hereditary rights'; Mieszko took over 'probably in late 1238 or early 1239'. Silesia /ledger/15 (1234 gain) and /ledger/18 (1239 loss) have no mirror. Add vassal_start 1234 / vassal_end 1239 with duchy-of-silesia (confidence 2); Silesia should turn its gain/loss into the same vassal pair and add a 1234 loss of Kalisz and Wieluń to Opole.
3. **Bytom 1281 vs 1284; land undrawn.** K14 (1281-1284) already drops the whole Bytom shape (Gliwice, Koźle), but duchy-of-bytom draws only a 15 km disc round Bytom 1281-1283 and gains Koźle, Toszek, Gliwice, Siewierz from Opole in 1284. Those lands are nobody's in 1281-1283. The Opole page's own 'recreated for Casimir and his brother Bolko I' supports joint rule to 1284. Make /ledger/11 the Bytom 15 km disc, add a 1284 loss to duchy-of-bytom (Bytom 1285 shape minus the disc), and keep those lands in Opole's 1281-1283 keyframe.
4. **/ledger/10 region overlaps Bytom.** 1275 Opole minus 1285 Opole contains the Bytom shape too; use {cliopatria 'Duchy of Racibórz', year 1285} (Racibórz's own found region).

Thin (gap-filler): /ledger/12 confidence-1 dissolve and Bolko I's reign (Bolko_I_of_Opole); Cieszyn dropped by Cliopatria in 1272 (Duchy_of_Cieszyn); Kalisz 1239-1241, which the Mieszko II page implies went back to Henry II ('given to him by Henry II the Pious' in 1241) (Henry_II_the_Pious); Władysław Opolski's reign.

## duchy-of-kuyavia: fail (unapplied blocking finding)

What held: the 1186, 1195 and 1198 events are on the Mieszko III page with their years; the 1205 end is confidence 1 and says so; the 1202 shrink is unexplained within a 1-2 page budget (thin by design).

Findings for the author:

1. **Greater Poland's overlordship 1186-1198 missing; land drawn twice.** Mieszko III page: 'he took the Kuyavia region and annexed it to his Duchy', 'Kuyavia, held by Bolesław 1186–95', 1198 'compelled to cede Kuyavia to Casimir's sons'. duchy-of-greater-poland draws the Kuyavia 1188 shape as its own 1186-1198 (/ledger/4, keyframes _1186 and _1188) and loses it 'to duchy-of-kuyavia' in 1199 (/ledger/11), with no mirror here; Masovia's 1186 loss names Greater Poland, not Kuyavia. Add vassal_start 1186 / vassal_end 1198 with duchy-of-greater-poland, and replace the 1198 rename with a vassal_start under duchy-of-masovia (Konrad; 1199 on the Greater Poland page) left open to 1205. Greater Poland should switch its gain/loss to the same vassal pair and drop the Kuyavia union from its corrections, or the orchestrator picks one dossier to draw the land.
2. **Capital outside the shape.** Inowrocław (the 1230-1267 duchy's capital) meets the Kuyavia 1188 shape in 0 gazetteer cells; the 1188 keyframe is `ok` although the author's own check finds it misses Inowrocław and Kruszwica and holds Gostynin, Kutno and Łowicz. Mark the shapes adjust with Inowrocław/Kruszwica added, or move the capital inside with a note.

Thin: /ledger/3 1205 (Konrad_I_of_Masovia); 1202 shrink; who held Kuyavia 1195-1198.

## Cross-dossier matrix (summary; full list in notes/phase-b/reviews/eu-15-f.json)

Matched: Opole-Silesia 1172, 1201, 1202; Opole-Sandomierz 1210, 1211; Opole-Greater Poland 1249 (Wieluń); Kuyavia-Masovia 1205.
Exception: Opole 1202 merge with Racibórz (no Racibórz dossier before 1281; listed); Opole 1304 dissolve (Cliopatria end).
Missing: Sandomierz 1227 Czeladź loss; Opole 1284 loss to Bytom; Opole and Bohemia 1291 vassal_start.
Mismatch: Opole 1234 Kalisz/Wieluń vs Silesia 1234 gain of Opole and 1239 loss (and duchy-of-kalisz 1234-1238 overlap); Opole 1244 Kalisz loss names Greater Poland, Greater Poland's 1244 gain names Silesia; Opole/Racibórz and Opole/Bytom 1281 land; Kuyavia 1186 found vs Masovia 1186 loss to Greater Poland; Greater Poland 1186 gain and 1199 loss vs Kuyavia's separate state and 1198 rename.
