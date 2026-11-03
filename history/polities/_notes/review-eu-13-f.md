# Review of eu-13-f (Sardinian judicates and Amalfi)

Reviewed 2026-10-25. All four dossiers pass the validator with `--resolve` (0 errors, 0 warnings). All their events are confidence 3 or lower. Pages opened by the reviewer: Judicate of Cagliari (twice), Mujahid al-Amiri, Judicate of Gallura, Taifa of Dénia, Adelasia of Torres, Judicate of Logudoro, History of Sardinia, Duchy of Amalfi, Amalfi, and it.wikipedia Giudicato di Cagliari. Every event checked says on its page what the note claims, with the year. No fabrication was found. The quotations the author marks as quotations are on the pages.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| giudicato-of-cagliari | thin | William I's control of Arborea is missing from the ledger |
| giudicato-of-gallura | fail | the 1258 gain from the Cagliari partition is missing |
| giudicato-of-logudoro | fix (applied by reviewer) | note on Cliopatria's Arborea 1066 shape |
| republic-of-amalfi | fix (applied by reviewer) | tiny-shape flag from data/README.md |

## giudicato-of-gallura: fail

- **Missing gain, 1258.** The Judicate of Cagliari page says the territory was "partitioned in three parts", "assigned to the Della Gherardesca family, Arborea and Gallura". The batch's own Cagliari dossier lists giudicato-of-gallura as a successor, and the author's notes say Gallura should carry the gain, but the Gallura ledger has no 1258 event. it.wikipedia (Giudicato di Cagliari) names the part: the north-east, "l'Ogliastra e il Sarrabus". Fix: add a `gain` in 1258 against giudicato-of-cagliari. The region is the 1187 Cagliari shape intersected with admin1 Ogliastra plus a place-based Sarrabus (Muravera, for example). Use confidence 2 and add the source page to `sources[]`.
- **Keyframe /keyframe_review/4** (giudicato-of-gallura_1210, 1210-1287) keeps the 1206 outline to the end. End it in 1257 and add giudicato-of-gallura_1258 (1258-1287, adjust) as the union of the Gallura 1206 outline and the 1258 part.
- **The 1287 dissolve region and Pisa's successor land** should be the enlarged outline.
- Gazetteer: "Sarrabus" is not a name in it; Ogliastra is (admin1).

## giudicato-of-cagliari: thin

- The page says William I "arrested and imprisoned the judge of Arborea, Peter I and ruled Arborea in his name", with no years; it.wikipedia dates the war on Arborea to 1195. The ledger has no occupation or vassal event for it, and the war "William I of Cagliari's wars" has `zones: []` although its own outcome says Arborea came under Cagliari. Page to try: Peter I of Arborea. The Arborea dossier needs the mirror.
- Successor lands for 1258 are the whole shape for each successor. it.wikipedia gives the parts: Gallura the north-east (Ogliastra, Sarrabus); Arborea the centre-north; the Della Gherardesca the west (Sulcis-Iglesiente); Pisa Castel di Castro directly, to 1326.
- The founding year 866 is at confidence 1 (infobox 1020). The author flagged it.
- Checked and confirmed: the 1188 rename (William I 1188-1214; History of Sardinia "In 1188, Cagliari was conquered by the House of Massa from the Republic of Pisa"); the 1258 dissolve and partition; the 1015-1016 Mujahid occupation ("occupied the southern coastal plain", "In May 1016"); the 1206-1207 contest with Gallura. The capital at Santa Igia lies inside the shape's bbox.

## giudicato-of-logudoro: fix (applied)

- Applied: /keyframe_review/3/note now says that Cliopatria's giudicato-of-arborea_1066 (1066-1071, 12,248 km2, bbox 8.15-9.43 E, 39.58-41.13 N) is Arborea plus Logudoro. Cliopatria therefore hands Logudoro to Arborea in the years the author filled with a new Logudoro keyframe. The pages have no union then, so the keyframe stands and the Arborea dossier should mark its 1066 shape adjust. The dossier re-validates clean.
- Thin: the founding year (866, confidence 1); the years of the capital moves (Torres to Ardara bridged 1099/1100, Sassari not drawn); the 1259 partition lines. Page to try: it.wikipedia Giudicato di Torres.
- Checked and confirmed: the 1259 dissolve (Adelasia page: "She died in 1259, without heirs"; Doria, Malaspina, Spinola "held it from Genoa"; Arborea "some land"); the 1015 Denia camp; Barisone I "from about 1038 to 1073"; Ardara as the "judicial palace" on 26 June 1132.

## republic-of-amalfi: fix (applied)

- Applied: /keyframe_review/1/note now flags the data/README.md "Shapes with tiny area" listing (96.36 km2, under one H3 cell at resolution 5). The dossier re-validates clean.
- Thin: /ledger/7, the end of the Salernitan control, is at 1073 with confidence 1. The Amalfi page says "a brief period of Salernitan dependency under Guaimar IV", so it ended by his death. Page to try: Guaimar IV of Salerno.
- Area: the infobox gives 5.7 km2 for the modern comune; Cliopatria has 96.4 km2 (ratio 16.9). This is acknowledged in the keyframe note.
- Checked and confirmed: 958 (Sergius I first duke; infobox Mastalus II); 981-983 rule of Salerno; 1034 Capua and 1039 Salerno; 1073 Robert Guiscard; 1096 revolt put down in 1101; 1130 revolt and 1131 subjection (Emir John, George of Antioch; Amalfi page "reduced by Roger II of Sicily").
- Modelling note, not a fault: 1073-1131 is written as occupation, although the page says Guiscard "conquered the city". This is defensible given the 1096 and 1130 revolts under Amalfi's own doge.

## Cross-dossier

- **Taifa of Dénia (eu-12).** There is no occupation against Cagliari, although the Mujahid page puts the 1015 landing on "the southern coastal plain" and the 1016 battle against the judge of Cagliari. For Gallura and Logudoro, Dénia hatches the remnants (`intersect` of Sardinia with the 1015 reduced shapes) while these dossiers hatch Cliopatria's cut-outs. The years agree but the land does not. Route to eu-12.
- **Not yet written** (another part of eu-13): republic-of-pisa (1258 Castel di Castro and the Della Gherardesca part; 1287 Gallura), giudicato-of-arborea (1258 Cagliari centre-north; 1259 Logudoro land; William I's control of Arborea; its 1066 shape), republic-of-genoa (1259), principality-of-salerno (981-983, 1039-), principality-of-capua (1034-1039), norman-italy or kingdom-of-sicily (1073-1131).
- **Compiler.** The judicates' reduced 1015 Cliopatria shapes run to 1017, while the ledgers end the occupation in 1016. Use the ledger's end.
