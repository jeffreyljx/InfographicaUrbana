# Review of eu-07-x (Franks and Carolingians, additions)

Reviewer: Phase B adversarial reviewer, 2026-10-25. The machine copy is history/notes/phase-b/reviews/eu-07-x.json. All nine dossiers validate with `--resolve` and give no errors or warnings, before and after the reviewer's edits. Verdict meanings: fix means the reviewer fixed everything listed; thin means a gap-filler gets the list; fail means the dossier goes back to the author.

| slug | verdict |
| --- | --- |
| kingdom-of-austrasia | thin |
| merovingian-neustria | fail |
| kingdom-of-lotharingia | pass |
| spanish-march | fail |
| duchy-of-francia | thin |
| march-of-pannonia | fix |
| principality-of-lower-pannonia | fail |
| duchy-of-lotharingia | thin |
| duchy-of-alsace | thin |

## Batch-wide

- Batch-wide: all nine dossiers are sub-units (sub-kingdoms, marches, duchies) of states that other dossiers draw as one shape (kingdom-of-the-franks, west-franks, east-franks, kingdom-of-germany). Their found/gain/loss events with those parents have no mirrors, and the parents double-book some of the same moves (Thuringia 532, Barcelona 801, Lotharingia 911/925). The author flagged this in notes. The orchestrator must decide the drawing: subtract the sub-units from the parents, or turn them into vassal pairs in both ledgers. Until then those cross-checks are 'missing' by design and are not counted against these dossiers.
- Reviewer-applied edits (each re-validated with --resolve, no errors or warnings, and read back): merovingian-neustria capital Soissons to=598; spanish-march KF4 correction text; duchy-of-francia western-Anjou circle moved to (-1.0, 47.65, 30 km) in 4 places; march-of-pannonia Aribo to=907, Szombathely->Vas (8 places), Nagykanizsa->Zala (2 places) and the notes sentence; principality-of-lower-pannonia Nagykanizsa->Zala (7 places); duchy-of-alsace war 0 to=742.
- Gazetteer trap: the urban counties Szombathely and Nagykanizsa (1 cell each) list 'Vas megye' / 'Zala megye' among their alt_names, so authors can pick them for the counties. Other batches using Hungarian urban counties may have the same slip.
- WebFetch returns a model summary. The decisive Chlothar II sentence (Guntram holding the Neustrian lands between the Loire and the Seine) was re-fetched and asked for word for word before it was used against merovingian-neustria.
- No page failed to load.

## kingdom-of-austrasia: thin

For a gap-filler:
- `/ledger (missing, 610)`: Austrasia's 610 gain of Alsace from Burgundy. Francia: 'In 610 Theudebert extorted the Duchy of Alsace'; Duchy of Alsace: 'in 610 Theudebert II ... forced Alsace' cession to him only to lose it two years later to Burgundy again'. It mirrors frankish-burgundy /ledger/3 (610 loss of Alsace, Champagne, Thurgau, which names kingdom-of-the-franks). Add gain 610, counterpart frankish-burgundy, region Alsace, confidence 3, and put Alsace into the 612 loss region (/ledger/8). Page to try: https://en.wikipedia.org/wiki/Duchy_of_Alsace
- `/ledger/10`: The 623 Alsace gain (confidence 1) is dated to the year the page says Alsace was kept out: 'In 623, when Chlothar II granted Austrasia to Dagobert, he excluded Alsace, the Vosges, and the Ardennes', conceded 'shortly after' with no year. Move the bridge to the concession year (traditionally 625/626) and add the Vosges and Ardennes, or take Alsace out of KF7 (623-628). Page to try: https://en.wikipedia.org/wiki/Dagobert_I
- `/keyframe_review (717-720)`: Chlothar IV, king in Austrasia 717-720 (Austrasia page king list; 'appointed Chlothar IV to rule in Austrasia'). It is not drawn and is left to kingdom-of-the-franks and kingdom-of-neustria. Coordinate with those dossiers (eu-07-b, eu-07-c) and either draw Austrasia for 717-720 or say in notes why not. Page to try: https://en.wikipedia.org/wiki/Chlothar_IV
- `/ledger/2`: Counterpart of the 555 loss. Francia: 'on Theudebald's death in 555 all the lands passed to Chlothar', and Chlothar I was then king at Soissons (merovingian-neustria /identity/rulers/0). Either name merovingian-neustria and add a 555 gain there, or end merovingian-neustria in 555 too. As written, Chlothar's kingdom keeps only the Soissons share 555-557 while Austrasia goes to the realm. Page to try: https://en.wikipedia.org/wiki/Chlothar_I
- `/ledger/4`: 567 gain of Tours and Poitiers (confidence 1): no page says how they came to Sigebert I. Page to try: https://en.wikipedia.org/wiki/Sigebert_I
- `/ledger/7`: 599 gain of the northern cities at Dormelles (confidence 1): the Chlothar II page says only that the rest was 'split between the two brothers'. Page to try: https://en.wikipedia.org/wiki/Theudebert_II

Spot checks: `/ledger/2` confirmed: 'on Theudebald's death in 555 all the lands passed to Chlothar'; `/ledger/6` confirmed: 587, 'the treaty brought about the cession of Tours by Guntram to Childebert'; `/ledger/12` confirmed: 'grant his son Sigebert III to them as a sub-king in 633'; `/ledger/16` confirmed: 'When Dagobert II died in 679, Theuderic received Austrasia as well'; `/ledger/17` confirmed: 'gave Austrasia, Alemannia, and Thuringia to Carloman' (741); `/ledger/14` confirmed: 673, Childeric II invited 'to become king of the whole realm'; `/ledger/15` confirmed: king list Dagobert II 675-679

Area: No infobox area on the Austrasia page (infobox 481-751, capitals Reims and Metz). Cliopatria has no Austrasia shape, so nothing to compare.

## merovingian-neustria: fail

Findings:
- `/ledger/6 and /keyframe_review/3-5` (NOT applied, author to do). The Seine-Loire land that KF3-KF5 (584-598) add to Neustria rests on a misreading. KF3 grows from 196 to 913 land cells on this reading alone. Evidence: Chlothar II page, in full: 'Guntram then attempted to weaken Fredegund's influence by swaying some of the Neustrian aristocracy to his side, and keep Neustrian lands he held between the Loire and Seine by rallying Duke Beppolène.' The lands were held by Guntram (Burgundy), not by Neustria, yet the notes of /ledger/6 and /keyframe_review/3 say this sentence 'shows Neustria then holding the land between the Seine and the Loire'. Fix: Take the Seine-Loire land out of /ledger/6, KF3-KF5 and the 599 loss (/ledger/10), or source a Neustrian holding on another page (Chilperic I's 567 share of Charibert's kingdom, Fredegund) and book it at the year that page gives. Rewrite both notes to say what the page says.
- `/ledger/4, /ledger/5` (NOT applied, author to do). The 578-584 vassal pair names breton-kingdoms, but that dossier (eu-06) starts in 587 and has no 578 or 584 event. Evidence: breton-kingdoms /identity/start = 587; its /ledger/0 is the 587 found event. Fix: Name a counterpart that is alive in 578: Waroch II's Vannetais (Broërec), listed under counterparts_needing_dossiers. Or ask eu-06 to start breton-kingdoms by 578 and add the mirror vassal_start and vassal_end.
- `/identity/capitals/0/to` (applied by reviewer). Soissons was the capital to 613, but KF6 (599-612, 'the regions of Beauvais, Amiens and Rouen') does not contain it. Evidence: Chlothar II page: the Dormelles treaty 'reduced his kingdom to the regions of Beauvais, Amiens and Rouen'. The resolved KF6 cells do not contain Soissons. Fix: Set to 598 (done, with a reviewer note).

For a gap-filler:
- `/ledger (missing, 524)`: Chlothar I's share of Chlodomer's kingdom. Francia: 'On the death of Chlodomer in 524 ... divided between the surviving brothers'. Page to try: https://en.wikipedia.org/wiki/Chlodomer
- `/ledger (missing, 567)`: Chilperic I's share of Charibert's kingdom. Chilperic I page: 'Chilperic's estates were augmented when the brothers divided Charibert's kingdom among themselves'. Page to try: https://en.wikipedia.org/wiki/Charibert_I
- `/ledger/0, /ledger/5, /ledger/7, /ledger/11`: Confidence-1 events: the 511 outline, the 584 vassal end, the 584 loss of Tours and Poitiers, and the 599 northern cities. Page to try: https://en.wikipedia.org/wiki/Fredegund

Spot checks: `/ledger/1` confirmed: 'With the death of Childebert in 558, the entire Frankish realm was reunited under the rule of Clothar'; `/ledger/2` confirmed: Soissons, Amiens, Arras, Cambrai, Thérouanne, Tournai and Boulogne 'fell to Chilperic's share' (561); `/ledger/6` not on page: the page has Guntram, not Neustria, holding 'Neustrian lands ... between the Loire and Seine' (confidence 1); `/ledger/8` confirmed: 'In 587, he [Guntram] managed to capture the towns of Angers, Saintes, and Nantes'; the losing side is inferred, as the note says; `/ledger/10` confirmed: 599, Dormelles, 'reduced his kingdom to the regions of Beauvais, Amiens and Rouen'; `/ledger/12` confirmed: 613, 'the entire realm was delivered into Chlothar's hands'

Area: No infobox area on the Neustria page (infobox capital Soissons). Not in Cliopatria.

## kingdom-of-lotharingia: pass

Spot checks: `/ledger/0` confirmed: 'established in 855 by the Treaty of Prüm'; Lothair II page: Lothair I died 19 September 855; `/ledger/1` confirmed: Charles of Provence died 24 January 863, 'Lothair received the Lyonnais and the Viennois'. Grenoble is lower-burgundy's addition, which the note says; `/ledger/2` confirmed: 8 August 870; Charles got Lower Burgundy with Lyon and Vienne and a small western part of Upper Burgundy with Besançon; line 'Meuse, Ourthe, Moselle, Saone and Rhone'; `/ledger/3` confirmed: Louis got the east 'with both Aachen and Metz' and most of Frisia

Area: No infobox area on the Lotharingia page. Cliopatria draws the realm only as Lower Burgundy 860-869, which the notes acknowledge.

## spanish-march: fail

Findings:
- `/keyframe_review/3/correction, /ledger/4/region, /ledger/6/region` (NOT applied, author to do). {admin1: Huesca} draws the whole province of Huesca for 'a number of castles ... in Aragon between 798 and 802'. That adds 58 land cells (about 14,700 km2, +51 percent of the march) for 802-819. Evidence: The province includes Huesca city, which the KF3 note says the Franks failed to take (807, 812). The Spanish March page says 'Navarre and Aragon were not formally part of the march' (they came under Carolingian overlordship as part of the Duchy of Vasconia). Cliopatria's County of Aragon is at most 3,585 km2. Fix: Draw the Aragon valley only: {"cliopatria": "County of Aragon", "year": 830} or {"place": "Jaca", "km": 30}, in KF3, /ledger/4 and /ledger/6. Or move Aragon out of the march, since the page says it was not part of it.
- `/ledger/2, /ledger/5` (NOT applied, author to do). The 798-816 vassal pair makes Pamplona a vassal of the Spanish March. Evidence: The Spanish March page says Navarre was 'not formally part of the march' and was under Carolingian overlordship via the Duchy of Vasconia. kingdom-of-pamplona's Cliopatria row starts 825, and the author did not list it under counterparts_needing_dossiers. kingdom-of-the-franks /ledger/92 books Pamplona as Frankish land lost in 825, so the two Frankish dossiers disagree on type and year. Fix: Drop the pair here and leave Pamplona to kingdom-of-the-franks, or reconcile with that dossier and list kingdom-of-pamplona (798-825) under counterparts_needing_dossiers.
- `/keyframe_review/4/correction/text` (applied by reviewer). The 820-897 correction text was copied from KF2 ('the above with Barcelona and Ausona (801)'). Evidence: KF4 is KF3 minus Aragon. Fix: Text rewritten to describe the 820 outline (done).

For a gap-filler:
- `/keyframe_review/4`: Ausona (Osona) is drawn 820-897, but it was lost or depopulated after Aizo's revolt (826-827) until Wilfred 're-created the County of Ausona' (Wilfred the Hairy page, 886). Page to try: https://en.wikipedia.org/wiki/Aizo

Spot checks: `/ledger/0` confirmed: 'established in c. 795 by Charlemagne'; `/ledger/1` confirmed: Urgell and Cerdanya 'were added in 798'; `/ledger/3` confirmed: surrender 'On April 4, 801'; Bera first count; `/ledger/4` confirmed: castles in Aragon 'between 798 and 802', but the page says Aragon was not formally part of the march; `/ledger/6` confirmed: County of Aragon broke away 'shortly thereafter in 820'; `/ledger/7` confirmed: 'Wilfred died in battle on 11 August 897'; first to pass his holdings to his sons

Area: No infobox on the Spanish March page and no area. Not in Cliopatria.

## duchy-of-francia: thin

Findings:
- `/ledger/1/region, /keyframe_review/1-2/correction, /wars/0/zones` (applied by reviewer). The western-Anjou subtraction circle (lon -0.9, lat 47.65, 35 km) contained Angers, the dossier's own capital for 861-885, so KF1 (863-885) excluded the capital. Evidence: Angers (-0.55, 47.48) is about 32 km from the circle centre. Robert the Strong was 'Count of Anjou' (Robert the Strong page), and Entrammes ceded only 'western Anjou' (Breton March page). Fix: Circle moved to lon -1.0, lat 47.65, 30 km, about 39 km from Angers, in all 4 places (done). Angers now resolves inside KF1.

For a gap-filler:
- `/ledger/2`: 886 gain of the Seine-Loire land (confidence 1). The Duchy of Francia page dates no Robertian acquisition of Paris, Orléans or Tours. Page to try: https://en.wikipedia.org/wiki/Odo_of_France
- `/ledger/4`: 936 loss of Anjou (confidence 1). Hugh the Great's page only excludes Anjou in 936. Page to try: https://en.wikipedia.org/wiki/Fulk_I,_Count_of_Anjou
- `/ledger/6`: 953 loss of Laon (confidence 1). The page does not say Laon went back. Page to try: https://en.wikipedia.org/wiki/Louis_IV_of_France

Spot checks: `/ledger/3` confirmed: title revived for Hugh the Great 'between 936 and 943'; 943 investiture (Flodoard); `/ledger/5` confirmed: Louis released in 946 'on condition that he should surrender the fortress of Laon'; `/ledger/7` confirmed: 960, 'made Hugh a duke, and added for him the country of Poitou'; `/ledger/8` confirmed: title 'fell into abeyance' after Hugh Capet became king in 987

Area: No infobox on the Duchy of Francia page. Not in Cliopatria.

## march-of-pannonia: fix

Findings:
- `/identity/rulers/1/to` (applied by reviewer). Aribo ran to 909, past the state's end (907). Evidence: March of Pannonia page: Aribo 871-909. Dossier end 907/7. Fix: Capped at 907, with a reviewer note (done).
- `/keyframe_review/0/correction and every region using {admin1: Szombathely} or {admin1: Nagykanizsa}` (applied by reviewer). Szombathely and Nagykanizsa are one-cell urban counties in the gazetteer, not the Vas and Zala counties the notes say they stand for ('Szombathely = Vas county', 'Nagykanizsa = Zala county'). Evidence: admin1.jsonl: Szombathely and Nagykanizsa have type 'Urban county', 1 cell each; Vas has 12 cells, Zala 13. Zalavár lies in Zala. Fix: Replaced with {admin1: Vas} (8 places) and {admin1: Zala} (2 places, in the vassal regions), and the notes sentence updated (done). Validates with --resolve and no warnings.

Spot checks: `/ledger/0` confirmed: '828 Imperial Diet', Baldric deposed, 'set apart as a frontier march against Moravia'; `/ledger/1` confirmed: Duchy of Lower Pannonia 'established in 839', residence at Zalavár; `/ledger/3` confirmed: 4-6 July 907, Luitpold 'lost the March of Pannonia to them'; `/ledger/4` confirmed: after Pressburg (907) 'all East Frankish lands beyond the Enns river were lost'

Area: No infobox on the March of Pannonia page. Not in Cliopatria.

## principality-of-lower-pannonia: fail

Findings:
- `/ledger (missing vassal_start 838/839 and vassal_end 900)` (NOT applied, author to do). march-of-pannonia /ledger/1 (839 vassal_start) and /ledger/2 (900 vassal_end) name this state as the vassal, but this ledger has no vassal events. The notes say the overlord was the March. Evidence: Brief section 2.3: a vassal_start of X is a vassal_start in X's ledger with this state as counterpart. Both dossiers are in this batch. The Lower Pannonia page: the Franks installed Pribina in 838 and Frankish domination 'lasted until the Magyar conquest (c. 900)'. Fix: Add vassal_start at 838 (or 839, to match the March page), counterpart march-of-pannonia, and vassal_end at 900. Alternatively make east-franks the overlord on both sides: the page calls Kocel's polity a vassal of the Frankish Empire. Align the year with march-of-pannonia.
- `/keyframe_review/0/correction and all regions` (applied by reviewer). {admin1: Nagykanizsa} is a one-cell urban county, so Zala county (Zalavár, the capital) was missing and the capital fell outside the shape. Evidence: admin1.jsonl: Nagykanizsa has 1 cell (its alt_names include 'Zala megye'); Zala has 13. The capital check showed Zalavár outside KF0. Fix: Replaced with {admin1: Zala} in 7 places (done). The capital now resolves inside KF0.

Spot checks: `/ledger/0` confirmed: 'In 838 ... Frankish count Radbod ... deposed Ratimir' and the Franks installed Pribina; `/ledger/1` confirmed: Frankish domination 'lasted until the Magyar conquest (c. 900)'; Braslav 884-896

Area: No infobox or area on the page. Not in Cliopatria.

## duchy-of-lotharingia: thin

For a gap-filler:
- `/ledger (missing overlord events)`: The overlord changes its own pages date are not booked: under East Francia from 903; 911 'Lotharingian nobles under the new duke Reginar voted to attach their duchy to West Francia'; 923 Henry the Fowler 'invaded Lotharingia (including Alsace)'; 925 'Lotharingians under Gilbert elected Henry the Fowler'; 939 Gilbert's revolt, Andernach. west-franks books 911 gain / 925 loss of the duchy as direct land, and kingdom-of-germany books 925 gain and 939 contest_start/contest_end against 'Gilbert of Lotharingia (rebel duke)'. Add vassal_start/vassal_end pairs (east-franks 903-911, west-franks 911-925, kingdom-of-germany 925-959) and contest events for 923-925 and 939, in line with the orchestrator's decision on sub-units, and have kingdom-of-germany name duchy-of-lotharingia. Page to try: https://en.wikipedia.org/wiki/Lotharingia
- `/identity/rulers`: Reginar (duke from 911 per the Lotharingia page) is missing. Rulers break between 939 and 954 (Otto of Verdun, Conrad the Red). Page to try: https://en.wikipedia.org/wiki/Conrad,_Duke_of_Lorraine
- `/identity/successors/0`: duchy-of-lorraine starts in 1431, so Upper Lorraine 959-1431 has no dossier and the successor link leaves a 472-year gap. Page to try: https://en.wikipedia.org/wiki/Duchy_of_Lorraine

Spot checks: `/ledger/0` confirmed: 'Since 903 it was organized as a duchy'; `/ledger/1` confirmed: duchy 'existed up to 959 or 965'; 'initiated in 959, by subdividing ducal governance into two distinctive jurisdictions'; `/wars/0` confirmed: 923 invitation to Henry I, 924 switch to Rudolf, 925 Henry occupied Lotharingia; `/wars/1` confirmed: 939 revolt, Andernach, died 2 October 939, Lorraine given to Henry I, Duke of Bavaria

Area: No infobox area on the Lotharingia page. Not in Cliopatria for 903-959.

## duchy-of-alsace: thin

Findings:
- `/wars/0/to` (applied by reviewer). The war ran to 746, past the duchy's end (742). Evidence: Brief section 2.2: wars inside the life. Duchy of Alsace page: 'dissolved in 742'. Fix: Capped at 742, with a note that Carloman's campaign went on to 746 (done).

For a gap-filler:
- `/keyframe_review (867 phase)`: The 867 revival is not drawn. Duchy of Alsace page: 'In 867, he created the first Duke of Alsace in over a century' (Hugh, Lothair II's son); Meerssen 870 attached Alsace to East Francia. Extend the dossier (one state, rule 2) with the phase's end. Page to try: https://en.wikipedia.org/wiki/Hugh,_Duke_of_Alsace
- `/identity/predecessors/0`: The predecessor is kingdom-of-austrasia, but the found event names kingdom-of-the-franks, and the Austrasia dossier is hollow in 629-632 and books no 630 loss of Alsace. Make them agree. Page to try: https://en.wikipedia.org/wiki/Duchy_of_Alsace
- `/identity/rulers`: No rulers between Gundoin (630) and Eticho (662 or 673). Page to try: https://en.wikipedia.org/wiki/Etichonids

Spot checks: `/ledger/0` confirmed: 'Sometime probably between 629 and 631 Dagobert granted it as a dukedom to Gundoin'; `/ledger/1` confirmed: 'dissolved in 742 when a successor for the deceased Duke Liutfrid was not named'

Area: No infobox on the Duchy of Alsace page. Not in Cliopatria.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-austrasia 511 found / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 532 gain / kingdom-of-thuringia | kingdom-of-thuringia 532 loss | mismatch | kingdom-of-thuringia /ledger/3 names kingdom-of-the-franks; kingdom-of-the-franks /ledger/3 also books the 532 gain of Thuringia (double-booked) |
| kingdom-of-austrasia 555 loss / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); the page gives the land to Chlothar I, king at Soissons (merovingian-neustria), which has no 555 gain |
| kingdom-of-austrasia 561 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); kingdom-of-the-franks /ledger/11 splits only Burgundy in 561 |
| kingdom-of-austrasia 567 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); Charibert's kingdom of Paris has no dossier |
| kingdom-of-austrasia 575 loss / merovingian-neustria | merovingian-neustria 575 gain | matched | merovingian-neustria /ledger/3 |
| kingdom-of-austrasia 587 gain / frankish-burgundy | - | missing | frankish-burgundy (eu-07, exists) has no 587 loss of Tours (Treaty of Andelot) |
| kingdom-of-austrasia 599 gain / merovingian-neustria | merovingian-neustria 599 loss | matched | merovingian-neustria /ledger/11 (both confidence 1) |
| kingdom-of-austrasia 612 loss / frankish-burgundy | frankish-burgundy 612 gain | mismatch | frankish-burgundy /ledger/6 names kingdom-of-the-franks as the loser of Austrasia |
| frankish-burgundy 610 loss / kingdom-of-the-franks | - | missing | frankish-burgundy /ledger/3 (Alsace, Champagne, Thurgau to Theudebert II); kingdom-of-austrasia has no 610 gain (see its thin list) and kingdom-of-the-franks has no 610 gain |
| kingdom-of-austrasia 623 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 629 loss / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 633 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 640 loss / duchy-of-thuringia | duchy-of-thuringia 641 gain | mismatch | duchy-of-thuringia /ledger/4 (eu-06) names kingdom-of-the-franks; Sigebert III of Austrasia was the king defeated |
| kingdom-of-austrasia 673 loss / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 675 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 679 loss / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 741 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| kingdom-of-austrasia 742 gain / duchy-of-alsace | duchy-of-alsace 742 dissolve | matched | duchy-of-alsace /ledger/1 with successor kingdom-of-austrasia |
| kingdom-of-austrasia 751 dissolve / kingdom-of-the-franks | kingdom-of-the-franks 751 rename | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| merovingian-neustria 511 found / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| merovingian-neustria 558 loss / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| merovingian-neustria 561 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| merovingian-neustria 575 gain / kingdom-of-austrasia | kingdom-of-austrasia 575 loss | matched | kingdom-of-austrasia /ledger/5 |
| merovingian-neustria 578 vassal_start / breton-kingdoms | - | mismatch | breton-kingdoms (eu-06) starts in 587, so it has no 578 event |
| merovingian-neustria 584 vassal_end / breton-kingdoms | - | mismatch | breton-kingdoms starts in 587 |
| merovingian-neustria 584 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); the same Seine-Loire land is frankish-burgundy's 600 gain from kingdom-of-the-franks, and the cited page has Guntram holding it |
| merovingian-neustria 584 loss / frankish-burgundy | - | missing | frankish-burgundy has no 584 gain of Tours and Poitiers |
| merovingian-neustria 587 loss / frankish-burgundy | - | missing | frankish-burgundy has no 587 gain of Angers, Saintes and Nantes |
| merovingian-neustria 596 gain / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| merovingian-neustria 599 loss / frankish-burgundy | frankish-burgundy 600 gain | mismatch | frankish-burgundy /ledger/2 is dated 600 and names kingdom-of-the-franks |
| merovingian-neustria 599 loss / kingdom-of-austrasia | kingdom-of-austrasia 599 gain | matched | kingdom-of-austrasia /ledger/7 |
| merovingian-neustria 613 dissolve / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); kingdom-of-the-franks /ledger/17 takes 613 from frankish-burgundy only |
| kingdom-of-lotharingia 855 found / middle-franks | middle-franks 855 split | matched | middle-franks /ledger/3 |
| kingdom-of-lotharingia 863 gain / lower-burgundy | lower-burgundy 863 loss | matched | lower-burgundy /ledger/1 |
| kingdom-of-lotharingia 870 loss / west-franks | west-franks 870 gain | matched | west-franks /ledger/6 |
| kingdom-of-lotharingia 870 loss / east-franks | east-franks 870 gain | matched | east-franks /ledger/4 |
| spanish-march 795 found / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| spanish-march 798 gain / emirate-of-cordoba | - | exception | owner eu-12 has not run (no file) |
| spanish-march 798 vassal_start / kingdom-of-pamplona | - | mismatch | no dossier (eu-12 not run), but the Cliopatria row starts in 825 and the author did not list it as needed; kingdom-of-the-franks /ledger/92 books Pamplona as Frankish land lost in 825 |
| spanish-march 801 gain / emirate-of-cordoba | - | exception | eu-12 not run; kingdom-of-the-franks /ledger/87 also books the 801 gain of Barcelona (double-booked, overlap) |
| spanish-march 802 gain / nobody | - | exception | counterpart nobody |
| spanish-march 816 vassal_end / kingdom-of-pamplona | - | mismatch | see 798; kingdom-of-the-franks has a 825 loss instead |
| spanish-march 820 loss / county-of-aragon | - | exception | eu-12 not run; the Cliopatria row starts in 830, so the eu-12 author must start it in 820 or the years will disagree |
| duchy-of-francia 861 found / west-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| duchy-of-francia 863 loss / kingdom-of-brittany | kingdom-of-brittany 863 gain | mismatch | kingdom-of-brittany /ledger/4 names west-franks |
| duchy-of-francia 886 gain / west-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| duchy-of-francia 936 loss / county-of-anjou | - | exception | listed in the author's counterparts_needing_dossiers (the Cliopatria row starts in 990) |
| duchy-of-francia 946 gain / west-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| duchy-of-francia 953 loss / west-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| duchy-of-francia 960 gain / duchy-of-aquitaine | - | exception | listed in counterparts_needing_dossiers (the row starts in 990) |
| duchy-of-francia 987 dissolve / kingdom-of-france | kingdom-of-france 987 found | mismatch | kingdom-of-france /ledger/0 names west-franks, not duchy-of-francia, as predecessor |
| march-of-pannonia 828 found / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint) |
| march-of-pannonia 839 vassal_start / principality-of-lower-pannonia | - | missing | principality-of-lower-pannonia (same batch) has no vassal_start; it is in that dossier's fail list |
| march-of-pannonia 900 vassal_end / principality-of-lower-pannonia | - | missing | same: no vassal_end in principality-of-lower-pannonia |
| march-of-pannonia 907 loss / principality-of-hungary | - | exception | no dossier; the Cliopatria row (900-999) is owned by a group that has not run yet |
| principality-of-lower-pannonia 838 found / nobody | - | exception | counterpart nobody |
| principality-of-lower-pannonia 900 loss / principality-of-hungary | - | exception | group not run yet |
| duchy-of-lotharingia 903 found / east-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); east-franks /ledger/22 takes Lotharingia in 900 as direct land |
| west-franks 911 gain / kingdom-of-germany | - | mismatch | west-franks /ledger/24 and /ledger/30 (925 loss) and kingdom-of-germany /ledger/6 (925 gain) book the duchy as direct land; duchy-of-lotharingia has no vassal events for 911 or 925 |
| kingdom-of-germany 939 contest_start / Gilbert of Lotharingia (rebel duke) | - | mismatch | kingdom-of-germany /ledger/16-17 should name duchy-of-lotharingia, which has no 939 contest events |
| duchy-of-lotharingia 959 dissolve / duchy-of-lorraine | - | exception | duchy-of-lorraine (eu-09) starts in 1431; Upper and Lower Lorraine 959-1431 have no dossiers |
| duchy-of-alsace 630 found / kingdom-of-the-franks | - | missing | flagged by the author: the parent dossier draws the whole realm and does not book this sub-unit (orchestrator to decide subtraction or vassal tint); the predecessor field names kingdom-of-austrasia, which is hollow in 629-632 |
| duchy-of-alsace 742 dissolve / kingdom-of-austrasia | kingdom-of-austrasia 742 gain | matched | kingdom-of-austrasia /ledger/18 |

## Counterparts needing dossiers

- Duchy of Upper Lorraine (959-1431, before the duchy-of-lorraine dossier's 1431 start) (duchy-of-upper-lorraine, 959-1431)
- Duchy of Lower Lorraine (duchy-of-lower-lorraine, 959-1190)
- Broërec (Waroch II's Vannetais), vassal of Neustria 578-584, or breton-kingdoms extended back from 587 (broerec, 577-587)
- Kingdom of Pamplona before its 825 Cliopatria start, only if the 798-816 vassal pair is kept (kingdom-of-pamplona, 798-825)

## Gazetteer names wanted

- Saintes (place, merovingian-neustria)
- Saintes (place, kingdom-of-austrasia)
- Vannes (place, merovingian-neustria)
- Zalavár (Mosapurc) (place, principality-of-lower-pannonia)
- Pallars (region, spanish-march)
- Ribagorza (region, spanish-march)
- Urgell (region, spanish-march)
- Cerdanya (region, spanish-march)
- Osona (Ausona) (region, spanish-march)
- Austrasia (region, kingdom-of-austrasia)
- Neustria (region, merovingian-neustria)
- Lower Pannonia (region, principality-of-lower-pannonia)
