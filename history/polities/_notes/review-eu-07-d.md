# Review of batch eu-07-d (2026-10-25)

Adversarial review of east-franks, middle-franks, kingdom-of-brittany, obotrites and frisians. Validator (--resolve): 0 errors in all five; warnings only for the missing kingdom-of-lotharingia slug and the frisians war outside the life. Neighbour dossiers read: west-franks, upper-burgundy, saxons, lower-burgundy, aquitaine (plus frisia, magna-frisia, breton-kingdoms by grep); the other Context polities are not written yet (groups not run). Cell counts come from tools/grid.py (H3 res 5).

Verdicts: east-franks fail, middle-franks fail, kingdom-of-brittany fail, obotrites thin, frisians thin. Findings marked applied were fixed by the reviewer in place (small, verified on the page, re-validated, read back).

## east-franks: fail

- **/keyframe_review/8/correction (east-franks_882) and /ledger (no 888 event)** (blocking). The 882-886 keyframe (Cliopatria East Franks 887) drops the 116 Transjurane (Upper Burgundy) cells that the corrected 876-881 keyframes hold, and no ledger event removes them; upper-burgundy's 888 found names east-franks as counterpart but this ledger has no 888 loss. Evidence: Grid count: (East Franks 880 + the 342-cell union) minus East Franks 887 = 125 cells, 116 of them inside upper-burgundy_887 (171 cells; 117 of them are inside east-franks_870, the Meerssen gain). Upper Burgundy page: in 888 the magnates 'assembled at the Abbey of St. Maurice, Agaunum and elected and crowned the Transjuran margrave Rudolph I as King'; after Meerssen 'Upper Burgundy was to be politically close to East Francia'. Charles the Fat page: after the deposition 'In Upper Burgundy, one Rudolph, a dux of the region, was elected as king'. Fix: Set the east-franks_882 correction to {"union": [{"cliopatria": "East Franks", "year": 887}, {"intersect": [{"cliopatria": "Upper Burgundy", "year": 887}, {"cliopatria": "East Franks", "year": 870}]}]} with to 887 (east-franks_887 adjust for 887 alike), and add an 888 loss (or split) with counterpart upper-burgundy, region = Upper Burgundy 887 intersect East Franks 870, text 'Transjurania, Rudolph I elected and crowned at St. Maurice', source https://en.wikipedia.org/wiki/Upper_Burgundy (add to sources), confidence 2.
- **/keyframe_review/14/correction (east-franks_899), /keyframe_review/10 (892-895), /keyframe_review/13 (898)** (blocking). Zwentibold's Lotharingia (538 cells) is drawn twice in 895-900: the 899 correction unions Middle Franks 899 into East Francia and the 892 and 898 shapes keep the same cells as direct land, while middle-franks draws them as its own keyframes (895-898 new, 899) after a 895 gain from east-franks. Evidence: Schema: vassal_start means 'region becomes this state's vassal ... drawn in the lighter tint', the vassal keeps its own outline; a cell has one owner and one status (master plan, compiled layer). middle-franks /keyframe_review/2-3 hold Middle Franks 899 for 895-900 and /ledger/4 is a gain from east-franks, which has no loss or split here (only vassal_start 895-5). Fix: Decide with middle-franks (see its finding). If Zwentibold's kingdom stays a separate state: east-franks keyframes 895-5 to 899 minus {"cliopatria": "Middle Franks", "year": 899} (new keyframe for May 895-897, 898 adjust, 899 verdict ok without the union) and a 895-5 split with counterpart (the Zwentibold slug) next to the vassal_start. If not: keep the land here as direct land and drop the vassal_start/vassal_end pair and middle-franks' 895-900 phase.
- **/ledger/14 and /ledger/15 (were /ledger/13-14 before the fix)** (applied). The 896 loss of Italy and the 896 contest_end had no month and so sorted before the 896-2 gain: the ledger lost Italy before gaining it. Evidence: Arnulf of Carinthia page: after the February coronation 'Arnulf had a stroke'; 'That same year Pope Formosus died, leaving Lambert once again in power', Lambert and Berengar killed 'any officials who had been appointed by Arnulf', 'For the rest of his life Arnulf exercised very little control in Italy'. Pope Formosus page: 'On 4 April 896, Formosus died.' Fix: Applied by the reviewer: month 4 on both events (earliest the pages allow), ledger re-sorted (gain 896-2 now precedes them), notes requoted. Re-validated: 0 errors.
- **/ledger/14/note, /keyframe_review/11/note** (applied). The quote 'Arnulf's control of Italy largely ended' is not on the Arnulf of Carinthia page. Evidence: The page reads 'For the rest of his life Arnulf exercised very little control in Italy' and 'Italy was lost'. Fix: Applied by the reviewer: replaced with the page's words in both notes.
- **/ledger (888-894)** (not blocking). upper-burgundy's contest_start 888 / contest_end 894 against east-franks over Lorraine and Alsace has no mirror here (flagged by the author). Evidence: Lotharingia page: 'Rudolph had intended to make himself king over the whole of Lothair II's former kingdom, but had to be content with Burgundia' (no years); upper-burgundy cites Rudolf I of Burgundy for 888-894. Fix: Add contest_start 888 / contest_end 894, counterpart upper-burgundy, region {union: Lorraine, Alsace} as in upper-burgundy, source https://en.wikipedia.org/wiki/Rudolph_I_of_Burgundy (open it for the years), confidence 2.
- Thin, /ledger/9: 892 vassal_end of Great Moravia is a bridging year (confidence 1); no page says the 884 Kaumberg oath was broken. Page to try: https://en.wikipedia.org/wiki/Svatopluk_I_of_Moravia
- Thin, /ledger/16: 900 loss of Transdanubia/Slavonia dated by the shape only (confidence 1); the counterpart may be magyars rather than principality-of-hungary (Cliopatria gives the cells to its Magyars row). Page to try: https://en.wikipedia.org/wiki/Hungarian_conquest_of_the_Carpathian_Basin
- Thin, /ledger/19, /ledger/20: 911 vassal_end of the Obotrites and Bohemia are drawing ends (confidence 1). Page to try: https://en.wikipedia.org/wiki/Duchy_of_Bohemia

Spot checks:
- /ledger/13 (896-2 gain): confirmed: 'take the city by force on 21 February 896'; crowned 22 February 896 (https://en.wikipedia.org/wiki/Arnulf_of_Carinthia)
- /ledger/14 (896 loss): confirmed in substance, mis-ordered and misquoted; fixed (month 4, page quote) (https://en.wikipedia.org/wiki/Arnulf_of_Carinthia)
- /ledger/7 (880-2 gain): confirmed: 'concluded in the city of Ribemont in February 880', whole of Lotharingia incl. the western part (https://en.wikipedia.org/wiki/Treaty_of_Ribemont)
- /ledger/11, /ledger/12 (895 Bohemia, 895-5 Zwentibold): confirmed: 'In 895, the Duchy of Bohemia broke away from Great Moravia and became Arnulf's vassal state'; Zwentibold crowned at the Diet of Worms, May 895 (https://en.wikipedia.org/wiki/Arnulf_of_Carinthia)
- /ledger/17, /ledger/18 (900-8): confirmed: 'overthrown and killed by Reginar on August 13, 900. The kingdom then ceased to exist and became a duchy.' (https://en.wikipedia.org/wiki/Lotharingia)
- /ledger/1 (844 vassal_start): confirmed: 'he compelled the Obotrites to accept his authority in 844 and put their prince, Gozzmovil, to death' (https://en.wikipedia.org/wiki/Louis_the_German)
- /ledger/8 (884 vassal_start): confirmed: Svatopluk 'in 884 at Kaumberg took an oath of fidelity to Charles' (https://en.wikipedia.org/wiki/Charles_the_Fat)
- /ledger/21 (911-9 dissolve): confirmed: 'When Louis died in 911, Duke Conrad I ... was elected to replace him on 10 November' (https://en.wikipedia.org/wiki/East_Francia)

Area: infobox None km2, Cliopatria 730939 km2, ratio None. East Francia infobox gives no area (Established: Treaty of Verdun 843; Disestablished 962); the author's notes say so.

## middle-franks: fail

- **/identity/start, /identity/end, /ledger/1-6, /keyframe_review/2-3, /certainty/0** (blocking). One dossier joins two different states, Lothair I's Middle Francia (843-855) and Zwentibold's Lotharingia (895-900), into a 843-900 life with a 39-year hole: the three 855 splits leave nothing of the state, yet there is no dissolve until 900, certainty 843-900 covers years when the state did not exist, and the capital stops in 855. Evidence: Middle Francia page: infobox Established 843, Disestablished 855; 'In 855 on his deathbed at Prum Abbey, Emperor Lothair I with the Treaty of Prum divided Middle Francia among his three sons.' Lotharingia page: Zwentibold appointed king of Lotharingia in 895, killed 13 August 900 (a kingdom of Lothair II's successor line, not Middle Francia). Research brief section 6 rule: where Cliopatria has one row for successive states, split it, one dossier per state, each reviewing only the shapes of its own years. The author flagged this as a design choice. Fix: End middle-franks in 855 with a dissolve (successors kingdom-of-italy, lower-burgundy, kingdom-of-lotharingia; the three splits may stay); review middle-franks_899 as verdict wrong with a correction saying the years 895-900 belong to Zwentibold's kingdom; move /keyframe_review/2, /ledger/4-6 and Zwentibold to that dossier (suggested slug kingdom-of-lotharingia-zwentibold, or kingdom-of-lotharingia if the orchestrator wants one Lotharingian dossier). The orchestrator should pick the slug.
- **/ledger/4 (895-5 gain from east-franks), /keyframe_review/2-3** (blocking). The 895 gain from east-franks has no mirror loss or split in east-franks, which keeps the same 538 cells in its own keyframes as vassal land; the cells are drawn by both dossiers in 895-900. Evidence: east-franks /ledger/12 is a vassal_start (no loss); east-franks /keyframe_review/10, /13 and /14 (union with Middle Franks 899) hold the land. Fix: Resolve together with the east-franks finding: either the new Zwentibold dossier keeps the land (east-franks subtracts it and records a split) or the land stays East Frankish and the 895-900 phase is dropped.
- **/notes** (not blocking). The boundary quoted as 'Aachen, Andernach, Louvain, Saint-Quentin and Alsace' (Lotharingia page) is not a list on that page tied to Zwentibold. Evidence: Lotharingia page: the places appear in different paragraphs; no sentence lists Zwentibold's territory. Fix: Drop the quote marks or the attribution.

Spot checks:
- /ledger/1-3 (855 splits): confirmed: Treaty of Prum 855; Louis II Italy, Lothair II the north (Lotharingia), Charles Provence and Burgundy (https://en.wikipedia.org/wiki/Middle_Francia)
- /ledger/4 (895-5 gain): confirmed: Zwentibold crowned king of Lotharingia at the Diet of Worms, May 895 (https://en.wikipedia.org/wiki/Arnulf_of_Carinthia)
- /ledger/5, /ledger/6 (900-8): confirmed: killed by Reginar on 13 August 900; 'The kingdom then ceased to exist and became a duchy.' (https://en.wikipedia.org/wiki/Lotharingia)
- /ledger/0 (843-8 found): confirmed: 'created in 843 by the Treaty of Verdun' (the month is from the East Francia page) (https://en.wikipedia.org/wiki/Middle_Francia)

Area: infobox 350000 km2, Cliopatria 384683 km2, ratio 1.1. Infobox gives 350,000 km2 with no year (text: 300,000 to 350,000); compared with middle-franks_850; acknowledged in /keyframe_review/1.

## kingdom-of-brittany: fail

- **/keyframe_review/12, /keyframe_review/13/correction, /ledger/7/region, /ledger (933)** (blocking). The Avranchin and Cotentin (the 29 cells gained in 867, /ledger/5) went to Normandy in 933 and were never recovered, but the ledger has no 933 loss, /ledger/7 hands the whole 911 shape back in 937, and the new keyframe kingdom-of-brittany_937 says 'The outline is unchanged'. Evidence: Duchy of Normandy page: William Longsword 'supported Rudolph and in 933 in return was granted Avranchin and the heavily Norse Cotentin', lands 'which were in practice outside effective Carolingian control and so had to be forcibly taken from the Duchy of Brittany'. Kingdom of Brittany page: 'By 937, he had recovered most of Brittany'. The dossier's own successor note quotes the infobox listing the Duchy of Normandy as a successor. Grid: Kingdom of Brittany 911 minus 866 = 29 cells. Fix: Add {year 933, type loss, counterpart duchy-of-normandy, region {"intersect": [{"cliopatria": "Kingdom of Brittany", "year": 870}, {"cliopatria": "West Franks", "year": 866}], "text": "Avranchin and the heavily Norse Cotentin"}, source https://en.wikipedia.org/wiki/Duchy_of_Normandy (add to sources), confidence 3}; split kingdom-of-brittany_919 at 933 (933-936 = the 911 shape minus that region, still occupied) and give kingdom-of-brittany_937 and /ledger/7 the 911 shape minus that region.
- **/identity/rulers/0** (applied). Ruler Wihomarc began in 822, before the dossier's start (825). Evidence: Rulers must lie inside the life; Kingdom of Brittany page gives his reign as 822-825. Fix: Applied by the reviewer: from 825, note records the 822-825 reign. Re-validated: 0 errors.
- Thin, /ledger/0 (825 found, confidence 1): No page dates a founding in 825; the Kingdom of Brittany infobox gives 'Established: 851' (Erispoe's claim to kingship), so 825-850 rests on Cliopatria (Nominoe's principality under Louis the Pious). Page to try: https://en.wikipedia.org/wiki/Nomino%C3%AB
- Thin, /identity/capitals/0: Vannes is unverified; no page names a capital. Page to try: https://en.wikipedia.org/wiki/Vannes
- Thin, /ledger (826-840, 913-918): No events; the Norse overrunning after 907 is undated before 919. Page to try: https://en.wikipedia.org/wiki/Viking_occupation_of_Brittany

Spot checks:
- /ledger/2, /ledger/3 (851-9): confirmed: battle 22 August 851; 'Charles recognized the authority of Breton rulers over the areas around Rennes, Nantes, and Pays de Retz'; Treaty of Angers September 851 (https://en.wikipedia.org/wiki/Battle_of_Jengland)
- /ledger/4 (863 gain): confirmed: peace 'whereby western Anjou was recognised as a part of Brittany' (863) (https://en.wikipedia.org/wiki/Salomon_of_Brittany)
- /ledger/5 (867 gain): confirmed: 'In 867, he was granted the counties of Avranches and Coutances' (https://en.wikipedia.org/wiki/Salomon_of_Brittany)
- /ledger/6 (919 occupation_start): confirmed: 'From 919, Brittany was completely occupied by the Norsemen' (https://en.wikipedia.org/wiki/Kingdom_of_Brittany)
- /ledger/7 (937 occupation_end): confirmed for the year ('By 937, he had recovered most of Brittany'); region overstated (Cotentin and Avranchin lost in 933) (https://en.wikipedia.org/wiki/Kingdom_of_Brittany)
- /ledger/8 (939-8 dissolve): confirmed: Battle of Trans-la-Foret 1 August 939, Alan II (938-939) last king (https://en.wikipedia.org/wiki/Kingdom_of_Brittany)

Area: infobox None km2, Cliopatria 47425 km2, ratio None. Kingdom of Brittany infobox gives no area or capital; status 'short-lived vassal-state', established 851.

## obotrites: thin

- Thin, /ledger/0 (793 found, confidence 1): 793 is Cliopatria's start; the page says 'Formed: 8th century' with Witzlaus as first ruler. Page to try: https://en.wikipedia.org/wiki/Witzlaus
- Thin, /ledger/7 (946 dissolve, confidence 1): 946 is a drawing end; the Billung March page says nothing of 946 (Hermann Billung given 'rule over the West Slavic Obotrite tribes' in 936; march abandoned after the 983 uprising) and the Obotrites page has the Obotrites independent to 1167 ('Accepted Saxon suzerainty: 1167'; Hamburg destroyed by Mstivoj in 983). The orchestrator should decide whether to end at 936 as a kingdom-of-germany vassal or extend the dossier. Page to try: https://en.wikipedia.org/wiki/Great_Slav_Rising
- Thin, /ledger (826-935), /identity/rulers: No events between 814 and 936 in this ledger (the 844 submission is on the east-franks side) and no ruler list. Page to try: https://en.wikipedia.org/wiki/List_of_Obotrite_rulers

Spot checks:
- /ledger/1, /ledger/2 (798-804): confirmed: the Obotrites under Thrasco 'defeated the Saxons in the Battle of Bornhoved (798)' (https://en.wikipedia.org/wiki/Obotrites)
- /ledger/3 (804 gain): confirmed: 'the part of their former land in Holstein north of Elbe was awarded to the Obotrites in 804' (https://en.wikipedia.org/wiki/Obotrites)
- /ledger/6 (814 loss): confirmed: 'After Charlemagne's death in 814, the Nordalbingian Saxons were pardoned and their land restored to them from the Obotrites.' (https://en.wikipedia.org/wiki/Nordalbingia)
- /ledger/7 (946 dissolve): not on page (declared confidence 1 drawing end; no fault) (https://en.wikipedia.org/wiki/Billung_March)

Area: infobox None km2, Cliopatria 15438 km2, ratio None. Obotrites infobox gives no area.

## frisians: thin

- **/wars/0** (not blocking). The only war (Frankish conquest of Frisia, 734-785) lies wholly outside the life 793-799 (validator warning). Evidence: Brief check 2: wars inside the life. Fix: Remove it (it belongs to frisia/magna-frisia) or, if the row is kept, replace it with a page-backed 793-799 war; settle together with the row's fate.
- Thin, /ledger/0, /ledger/1 (793 found, 799 dissolve, both confidence 1): No page attests a Frisian polity in 793-799. The reviewer also opened the Saxon Wars page: Frisians appear only in the infobox; 'The Eastphalians and Nordalbingians joined them in 793, but the insurrection ... was completely put down by 794' (no Frisians). Frisia page: 'Frankish troops conquered the area east of the Lauwers in 785'. Recommend the orchestrator drop the row and leave the land to kingdom-of-the-franks unless a page turns up. Page to try: https://en.wikipedia.org/wiki/Frisian%E2%80%93Frankish_wars

Spot checks:
- /ledger/0 (793 found): not on page (declared confidence 1, 'unverified'); 785 conquest and 734 Boarn quotes confirmed (https://en.wikipedia.org/wiki/Frisia)
- /ledger/0 (793 found): not on page: no Frisian rising 793-799 (https://en.wikipedia.org/wiki/Saxon_Wars)

Area: infobox None km2, Cliopatria 8792 km2, ratio None. Frisians is an ethnic-group article; no area.

## Cross-dossier matrix

- east-franks 844 vassal_start / obotrites -> none: **exception**. Schema records vassalage on the suzerain's side only; obotrites has no event type for it.
- east-franks 870 gain / kingdom-of-lotharingia -> none: **exception**. No dossier yet; listed under counterparts_needing_dossiers (eu-07-x).
- east-franks 880 gain / west-franks -> west-franks 880 loss: **matched**. Both 880-2 (Ribemont).
- east-franks 884 vassal_start / great-moravia -> none: **exception**. Suzerain-side event; great-moravia (eu-15) not run yet.
- east-franks 892 vassal_end / great-moravia -> none: **exception**. Suzerain-side event; eu-15 not run yet.
- east-franks 895 vassal_start / duchy-of-bohemia -> none: **exception**. Suzerain-side event; eu-15 not run yet.
- east-franks 895 vassal_start / middle-franks -> middle-franks 895 gain: **mismatch**. middle-franks takes the land as a gain from east-franks; east-franks has no loss/split and keeps the cells in its keyframes (double ownership 895-900).
- east-franks 896 gain / kingdom-of-italy -> none: **exception**. kingdom-of-italy (eu-13) not run yet.
- east-franks 896 loss / kingdom-of-italy -> none: **exception**. kingdom-of-italy (eu-13) not run yet; month fixed to 4 by the reviewer.
- east-franks 900 loss / principality-of-hungary -> none: **exception**. eu-15 not run yet; Cliopatria gives the cells to its Magyars row, so eu-15 should check magyars vs principality-of-hungary.
- east-franks 900 gain / middle-franks -> middle-franks 900 loss: **matched**. Both 900-8.
- east-franks 911 vassal_end / obotrites -> none: **exception**. Suzerain-side bridging end.
- east-franks 911 vassal_end / duchy-of-bohemia -> none: **exception**. Suzerain-side bridging end; eu-15 not run yet.
- upper-burgundy 888 found / east-franks -> east-franks None None: **missing**. upper-burgundy founds on east-franks land (116 cells East Frankish since 870) but east-franks has no 888 loss/split and drops the cells in 882 instead.
- upper-burgundy 888 contest_start / east-franks -> east-franks None None: **missing**. Contest 888-894 over Lorraine and Alsace not mirrored in east-franks (author flagged).
- middle-franks 855 split / kingdom-of-italy -> none: **exception**. kingdom-of-italy (eu-13) not run yet.
- middle-franks 855 split / lower-burgundy -> lower-burgundy 855 found: **matched**. lower-burgundy found 855-9 with counterpart middle-franks.
- middle-franks 855 split / kingdom-of-lotharingia -> none: **exception**. No dossier yet; listed (eu-07-x).
- middle-franks 895 gain / east-franks -> east-franks 895 vassal_start: **mismatch**. See east-franks 895 vassal_start.
- middle-franks 900 loss / east-franks -> east-franks 900 gain: **matched**. Both 900-8.
- kingdom-of-brittany 851 gain / west-franks -> west-franks 851 loss: **matched**. Brittany 851-9, west-franks 851 (no month).
- kingdom-of-brittany 863 gain / west-franks -> west-franks None None: **missing**. west-franks has no 863 loss of western Anjou (Salomon page: 863 peace 'whereby western Anjou was recognised as a part of Brittany'); route to the west-franks owner.
- kingdom-of-brittany 867 gain / west-franks -> west-franks 867 loss: **matched**. Avranches and Coutances.
- kingdom-of-brittany 919 occupation_start / viking-settlements -> none: **exception**. viking-settlements (eu-14) not run yet.
- kingdom-of-brittany 937 occupation_end / viking-settlements -> none: **exception**. eu-14 not run yet.
- kingdom-of-brittany 933 loss (missing) / duchy-of-normandy -> none: **missing**. Neither side records the 933 grant of Avranchin and Cotentin to William Longsword (Duchy of Normandy page); duchy-of-normandy has no dossier yet (Cliopatria row 922-1071).
- breton-kingdoms 824 dissolve / kingdom-of-brittany -> kingdom-of-brittany 825 found: **matched**. Consecutive years.
- obotrites 804 gain / saxons -> saxons 804 dissolve: **matched**. saxons dissolve 804 with obotrites as counterpart and successor.
- obotrites 814 loss / kingdom-of-the-franks -> none: **exception**. kingdom-of-the-franks (eu-07, another part) not written yet.
- saxons 798 contest_start / obotrites -> obotrites 798 contest_start: **matched**. Contest 798-804 on both sides.

## Counterparts needing dossiers

- Kingdom of Lotharingia (Lothair II): kingdom-of-lotharingia [855, 869]
- Kingdom of Lotharingia under Zwentibold (if middle-franks is split): kingdom-of-lotharingia-zwentibold [895, 900]
- Duchy of Normandy (933 Avranchin and Cotentin gain from Brittany): duchy-of-normandy [911, 1071]

## Problems and decisions

- No page failed to load. The Arnulf of Carinthia page lacks the author's quote 'Arnulf's control of Italy largely ended' (paraphrase, substance confirmed; quote replaced).
- Reviewer edits (orchestrator-allowed small fixes, re-validated with 0 errors, read back): east-franks months on the 896 loss and contest_end plus re-sort and two requoted notes; kingdom-of-brittany ruler Wihomarc from 825.
- Design decisions for the orchestrator: middle-franks must be split (Middle Francia 843-855 vs Zwentibold's Lotharingia 895-900) and the split decides how east-franks draws Lotharingia in 895-900; the obotrites 946 end and the frisians row (no page attests it) need a decision.
- The reviewer brief's mirror rule for vassal_start (a vassal_start in the vassal's ledger) conflicts with the schema (vassal events on the suzerain's side only); vassal events were treated as exceptions.
