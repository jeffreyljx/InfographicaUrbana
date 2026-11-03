# Review of batch eu-06-g (magna-frisia, carantania), 2026-10-25

Reviewer: adversarial review, Phase B. Validator (`--resolve`): both dossiers valid, no errors. magna-frisia has 8 warnings 'region resolves to no cells', all on the frisia-kingdom keyframes 9-16 whose correction is the shape minus itself (intended 'draw nothing', flagged by the author). carantania: no warnings. No dossier edits were made by the reviewer.

Neighbour dossiers read: bavarians, avar-khaganate, saxons, duchy-of-thuringia, burgundian-kingdom, aquitaine (context list, written); frisia and kingdom-of-alamannia (named by the author). Not written: kingdom-of-the-franks (eu-07), kingdom-of-italy (eu-13), samo-s-empire (eu-15): Cliopatria rows owned by groups that have not run yet.

Pages opened: Frisian Kingdom, Radbod King of the Frisians, Battle of the Boarn, Battle of Dorestad, Carantania. All loaded.

## magna-frisia: verdict fix (one keyframe/ledger fix for the author; not applied by the reviewer)

Spot checks (all confirmed, quotes match the notes and years):
- /ledger/1 689 loss: Radbod page 'In 689, however, Radbod was defeated by Pepin of Herstal in the battle of Dorestad', 'compelled to cede Frisia Citerior (Nearer Frisia, from the Scheldt to the Vlie)'; 'Between 690 and 692, Utrecht fell into the hands of Pepin.'
- /ledger/2 714 gain: Frisian Kingdom page 'After Pepin died, in 714, Redbad ... regained southern Frisia.'
- /ledger/5 719 loss: Frisian Kingdom page, after Redbad's death of illness in 719, 'Charles Martel not only annexed Frisia Citerior' and crossed the Rhine to annex 'farther' Frisia to the Vlie. No separate year, as the note says (confidence 2 is right).
- /ledger/6 733 contest_start: 'There was a rebellion against Frankish rule in the region of Westergo in 733, which Charles put down.'
- /ledger/7 and /ledger/8 (confidence 3): Boarn page 'In 734 a Frankish army commanded by Majordomo Charles Martel invaded Friesland', 'the Frisian army was beaten and Poppo killed', 'The Franks gained control of the Frisian lands west of the Lauwers estuary'.
- /keyframe_review/2 note: Battle of Dorestad page 'around 695', 'from south of the Oude Rijn to the coast', 'by the capital city of the Frisians close to the Rhine'.
- Rulers: infobox 'c. 650 - c. 680: Aldgisl', 'c. 680-719: Redbad', '719-734: Poppo'. Confirmed.

Cell counts re-done: Magna Frisia 617 = 80 cells (Niedersachsen 19, Friesland 15, Noord-Holland 11, Groningen 10, Zeeland 7, Zuid-Holland 7, Flevoland 2, Overijssel 2, Drenthe 1, Noord-Brabant 1, 5 unassigned coast cells). The author's 14 (689), 27 (719) and 20 (734) removed cells are right.

Finding (applied: false, non-blocking, author to do):
- /keyframe_review/0, /keyframe_review/1/correction, /keyframe_review/3/correction and /identity/capitals/0. The Cliopatria Magna Frisia shapes of 602 and 617 hold no cell of the province of Utrecht (0 of 80) and no cell within 15 km of Dorestad (5.34 E, 51.97 N) or Utrecht (5.12 E, 52.09 N). The dossier's capital Dorestad therefore lies outside the drawn kingdom, and the ledger's 689 loss and 714 gain of Utrecht (/ledger/1, /ledger/2, /ledger/3) have no trace in the keyframes. Evidence: Frisian Kingdom infobox 'Capital: Dorestad Traiectum (Utrecht)'; 'the Frisian kingship reached its maximum geographic development with its center of power in Dorestad'; 'Dorestad and Utrecht fell into the hands of Pepin'; Radbod page 'Between 690 and 692, Utrecht fell into the hands of Pepin'. Fix: keyframe 0 verdict adjust with correction {"union": [{"cliopatria": "Magna Frisia", "year": 602}, {"admin1": "Utrecht", "country": "Netherlands"}]}; keyframes 1 and 3 correction {"union": [{"cliopatria": "Magna Frisia", "year": 617}, {"admin1": "Utrecht", "country": "Netherlands"}]} with text quoting the capital line; keyframe notes updated (87 cells). The 689 and 719 corrections already remove Utrecht and need no change.

Accepted after trying to break them:
- Frisia Kingdom row (612-717) merged here with all 8 shapes wrong and empty: shapes.csv confirms the geometry (7.06-11.11 E, 46.87-50.51 N, same bbox and 37 vertices as kingdom-of-alamannia_724, 57,195 vs 57,419 km2). kingdom-of-alamannia draws that land with its new keyframe 496-723; frisia does not list the row, so it is reviewed once. Documented in notes.
- 734 'rename' with no counterpart marks the end of the kingship; the free Frisians east of the Lauwers continue in Cliopatria's 741-771 shapes. Defensible; the note could name the new style ('free Frisians') but this is not required.
- The 782 end (confidence 1) is a bridge to frisia, whose found event (783, counterpart magna-frisia) and predecessor entry match.
- Area: the Frisian Kingdom page has no infobox area; Cliopatria 21,798 km2 (617). Nothing to compare.

Thin (within a 5-page budget, all flagged by the author): /ledger/10 (782 dissolve, confidence 1); the year of the Vlie annexation (/ledger/5); Frankish overlordship of Westergo before 733 (/ledger/6); the 602-649 extent (/keyframe_review/0).

## carantania: verdict fail (missing vassal mirrors; one blocking finding, not applied)

Spot checks (all confirmed on the Carantania page):
- /ledger/0 661 found: 'In 658 Samo died and his Tribal Union disintegrated'; 'The name Carantania itself begins to appear in historical sources soon after 660.'
- /ledger/1 828 dissolve (confidence 3): 'In 828, Carantania finally became a margraviate of the Carolingian Empire'; 'By 828, internal autonomy of the principality was abolished'; infobox 'Integration to Franks: 828'.
- /wars/0: 'When about 740 Prince Boruth asked the Bavarian duke Odilo for help', 'Carantania lost its independence'; 'the Avars, who had regained eastern parts of Carantania between 745 and 795'.
- /keyframe_review/1 note: infobox 'Tributary to Franks: 745'. Capital: 'Carantania's capital was most likely Karnburg'; the coordinates (14.38 E, 46.70 N) fall inside the 661 and 749 shapes.

Finding (applied: false, blocking):
- /ledger. The ledger has no vassal_start or vassal_end, although bavarians /ledger/6 (vassal_start 743, counterpart carantania, confidence 2, Duchy of Bavaria page 'At around 743, the Bavarian duke Odilo vassalised the Slavic princes of Carantania') and /ledger/7 (vassal_end 788, counterpart carantania) carry the Bavarian overlordship, and the Carantania page itself says Carantania 'lost its independence' about 740, lists it 'Tributary to Franks: 745' and says Boruth's successors 'had to accept the overlordship of Bavaria'. The author's note says the tint belongs to the suzerains; reviewer brief check 3 (and the practice of earlier reviews, e.g. kingdom-of-bulungan in se-03-a) requires the vassal's own mirror. Fix: add vassal_start 743, counterpart bavarians, region {"cliopatria": "Carantania", "year": 741}, confidence 2, quoting the Carantania 'about 740' sentence and the Duchy of Bavaria 'around 743' sentence (add that page to sources); vassal_end 788, counterpart bavarians, confidence 1 (Tassilo III deposed; mirror of bavarians /ledger/7); vassal_start 788, counterpart kingdom-of-the-franks, and vassal_end 828, counterpart kingdom-of-the-franks, before the 828 dissolve (infobox 'Tributary to Franks: 745'; '828 ... margraviate').

Accepted: the 750-827 new keyframe (Cliopatria lets bavarians_750 absorb the 749 shape; bavarians draws it as a vassal, consistent); the shape kept whole although larger than the page's regions (soft certainty, said); no infobox area (Cliopatria 45,562 km2). Within the 1-2 page budget the dossier is otherwise thin by design.

Thin: /wars/0 zones (which eastern parts the Avars held 745-795; try https://en.wikipedia.org/wiki/Pannonian_Avars); the date of Ljudevit Posavski's rebellion and the deposition of the princes (try https://en.wikipedia.org/wiki/Ljudevit_Posavski); no rulers (the page names only Boruth and Valuk; try https://en.wikipedia.org/wiki/List_of_rulers_of_Carinthia).

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| magna-frisia 689 loss to kingdom-of-the-franks | none | exception: eu-07 not run |
| magna-frisia 714 gain from kingdom-of-the-franks | none | exception: eu-07 not run |
| magna-frisia 719 loss to kingdom-of-the-franks | none | exception: eu-07 not run |
| magna-frisia 734 loss to kingdom-of-the-franks | none | exception: eu-07 not run |
| magna-frisia 782 dissolve to frisia | frisia 783 found, counterpart magna-frisia | matched |
| bavarians 743 vassal_start carantania | none in carantania | missing |
| bavarians 788 vassal_end carantania | none in carantania | missing |
| carantania 828 dissolve to kingdom-of-the-franks | none | exception: eu-07 not run |
| carantania 661 found from samo-s-empire | none | exception: eu-15 not run |

## Other
- The author's counterparts_needing_dossiers lists kingdom-of-the-franks and samo-s-empire; both are Cliopatria rows (polities.csv) owned by eu-07 and eu-15, not new dossiers.
- colours.json still seeds frisia-kingdom, which has no dossier (author flagged).
- Gazetteer: no names needed.
