# Review of batch g-eu-b (gap round: German, Low Countries, French and post-1918 gaps)

Reviewer, 2026-11-01. Validator (--resolve): all six valid, no errors; two warnings in principality-of-luneburg (counterparts principality-of-grubenhagen and principality-of-calenberg have no dossier; both listed in the author's counterparts_needing_dossiers, so accepted). No fix applied by the reviewer. Machine copy: history/notes/phase-b/reviews/g-eu-b.json.

| slug | verdict | why |
| --- | --- | --- |
| principality-of-luneburg | pass | 5 events checked on two pages, all confirmed (1617 Grubenhagen, 1665 cession, 28 Aug 1705, 1370/1388 war). Overlap with duchy-of-brunswick-luneburg flagged by the author. |
| county-of-namur | pass | 5 events confirmed (1256, 1264 x2, 1305, 1429). Area: no infobox; the page says the modern province is larger than the old county (acknowledged as a modern-province reading). |
| county-of-sens | thin | 2 confidence-3/2 events confirmed; 3 of 5 events at confidence 1 (987 start, 1003 Champagne block, 1015 bridge); the fr page cited for 1003 does not mention 1003. |
| state-of-slovenes-croats-and-serbs | fail | occupation region and 1918 shape wrong (below). |
| central-lithuania | fail | the vassalage to Poland is missing (below). |
| west-ukrainian-people-s-republic | pass | 5 events confirmed on two pages (1 Nov, 21 Nov, 22 Jan, war start). |

## state-of-slovenes-croats-and-serbs: fail

1. /ledger/1/region (also /ledger/3, the war zone): the Italian occupation of 4 Nov 1918 draws the whole region "Dalmatia" (Split-Dalmatia, Zadar, Šibenik-Knin, Dubrovnik-Neretva) and leaves out western Carniola. Villa Giusti page: evacuation of "Istria, western Carniola, and part of Dalmatia"; SHS page: Italy "occupied Istria and much of Dalmatia". The note quotes "part of Dalmatia" and the dossier notes say "Dalmatia and western Carniola". Fix: draw northern Dalmatia only (e.g. Zadarska + Šibensko-Kninska, or the armistice line if a page gives it) plus western Carniola (e.g. place Postojna 30 km), confidence 2.
2. /keyframe_review/0/correction (same spec in /ledger/0, /ledger/4, predecessor and successor land): the shape includes Prekmurje and Međimurje, Hungarian-held in Oct-Dec 1918. SHS page: Prekmurje "annexed by Hungary" (footnote); in Međimurje loyal units "fought the Hungarian garrison" in November 1918. yugoslavia/ledger/4 gains Medimurska and Murska Sobota from hungarian-republic in 1920/6. Prekmurje is not flagged. Fix: subtract {"admin1":"Murska Sobota","country":"Slovenia"} and {"admin1":"Medimurska","country":"Croatia"}.
3. /ledger/2/region (not blocking alone): Syrmia drawn as Vukovarsko-Srijemska at confidence 3. The page: "the region of Syrmia, which had become part of the State ... seceded" on 24 Nov. Serbian Syrmia (Sremski) is outside this state's shape because austria-hungary/ledger/36 gives it to serbs in October; serbs/ledger/28 gains Sremski on 24 Nov from austria-hungary. Fix: add Sremski to the 1918 shape and to this loss, confidence 2; the serbs group should set the counterpart to this slug.

Thin: Fiume/Rijeka, Maribor and the Carinthian front are not on the pages opened (flagged by the author).

## central-lithuania: fail

1. /ledger: no vassal_start or vassal_end with second-polish-republic. Infobox: "Puppet state of the Second Polish Republic"; second-polish-republic/ledger/11 (1920 vassal_start) and /ledger/20 (1922/3 vassal_end) name this slug and were listed in the author's brief as lines to mirror. Fix: add vassal_start 1920/10 (counterpart second-polish-republic, region place Vilnius 60 km, confidence 3, source the Republic page) and vassal_end 1922/3 before the dissolve.

Checked and confirmed: 12 Oct 1920 founding, 7 Nov advance, 21 Nov 9 a.m. ceasefire, Sejm acceptance 22 March 1922 (infobox incorporation 18 April 1922). Area: infobox 13,490 km2, 60 km disc about the same. Thin: the disc is round; the state reached Lida, Braslaw and Švenčionys; three dossiers use three discs (47, 60, 100 km).

## county-of-sens: thin

- /ledger/0 987 start: a bridge, confidence 1. Try fr:Renard Ier de Sens.
- /ledger/1 1003 loss to county-of-champagne: Cliopatria only. The cited fr page does not mention 1003. It names Montereau, ceded by Renard II to the count of Troyes, and a county of Joigny "vassal des comtes de Troyes", first attested between 996 and 1080. Try fr:Comté de Joigny.
- /ledger/3: a bridge contest_end, by design.
- Extent: Yonne without Auxerre; the fr page says portions of the Yonne, Loiret, Seine-et-Marne and Aube.
- Cross: county-of-champagne/ledger/4 also hands the Sens-Joigny block to "kingdom-of-france" in 1055, while this dossier's dissolve region still holds that block. Fix: give the dissolve region the 1003 keyframe correction (minor).

## Leads for the passing dossiers

- principality-of-luneburg: the page says only that Grubenhagen was "acquired" in 1617. The holder before that may be Brunswick-Wolfenbüttel (the Grubenhagen line died out in 1596; unverified), so the counterpart may need to change once a Grubenhagen page is opened.
- county-of-namur: the 12th-century losses (Dinant to Liège, annexations by Brabant, Hainaut and Liège) are undated, and so is the Hainaut and Courtenay interval. Try Philip I, Marquis of Namur.
- west-ukrainian-people-s-republic: Przemyśl and the western front are not drawn; the page gives no date for them.

## Cross-dossier mismatches routed elsewhere

- kingdom-of-italy and yugoslavia: no Italian occupation of northern Dalmatia and western Carniola for 1918-1921.
- serbs/ledger/28: the counterpart should be state-of-slovenes-croats-and-serbs. austria-hungary/ledger/36 hands Sremski to serbs in October 1918.
- second-polish-republic: no gain of Lviv on 21 Nov 1918. The Eastern Galicia contest names ukrainian-people-s-republic before 22 Jan 1919. Central Lithuania is drawn with a 100 km disc (central-lithuania uses 60, kingdom-of-lithuania 47).
- ukrainian-people-s-republic/ledger/10: the merge includes Lviv, which was Polish from 21 Nov 1918.
- kingdom-of-galicia-and-lodomeria/ledger/9: hands all of Galicia, Eastern Galicia included, to Poland in November 1918, on top of the loss to the WUPR.
- county-of-flanders: draws Namur as a 25 km disc where this batch uses the whole province.
- house-of-luxembourg: starts in 1260 with Namur already inside it, while the page puts the seizure in 1256.
- burgundian-state/ledger/4 and duchy-of-burgundy/ledger/16: both gain Namur in 1429, and both name the county instead of using the slug.
- duchy-of-brunswick-luneburg: overlaps principality-of-luneburg from 1269 to 1705.
