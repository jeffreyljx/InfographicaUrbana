# Review of batch eu-22-x (2026-10-31)

Thirteen new dossiers (states Cliopatria lacks; no Cliopatria shapes, so every keyframe is new and the budget is 2-5 pages). All validated with 0 errors and 0 warnings (`--resolve`) before review. Spot checks: 4-5 events per dossier, on the cited Wikipedia pages; no event was fabricated or mis-dated. Keyframe areas were measured with tools/gazetteer.py (cells x 253 km2).

| slug | verdict | why |
| --- | --- | --- |
| allied-occupied-germany | pass | events confirmed (Potsdam 1-2 Aug 1945, Saar 16 Feb 1946, FRG May 1949, GDR 7 Oct 1949); occupier mismatches are on the UK/US/USSR side |
| west-berlin | fix (applied) | 1990 French occupation_end named french-fourth-republic (ended Oct 1958) |
| saar-protectorate | fix (applied) | vassal mirror of french-fourth-republic was missing; 1947 exchange left thin |
| free-territory-of-trieste | pass | dates, zones and the 1954 split confirmed; 5 cells vs 738 km2 acknowledged |
| transnistria | **fail** | shape is 5 cells (~1,265 km2) vs infobox 4,163 km2; 1990-91 shape 1 cell; note falsely says within a factor of two |
| republika-srpska | thin | Dayton shape for 1992-95; 1992 gains and 1995 losses missing; capital |
| croatian-republic-of-herzeg-bosnia | pass | dates confirmed; 11,132 vs 12,937 km2 |
| republic-of-serbian-krajina | pass | dates confirmed incl. Western Slavonia joining on 19 Dec 1991 |
| donetsk-people-s-republic | thin (one fix applied) | front lines as circles; Debaltseve double-counted; Aug 2014 Azov strip missing |
| luhansk-people-s-republic | thin | 2014 front and Sept 2022 losses missing |
| autonomous-province-of-western-bosnia | pass | dates confirmed; 506 vs 420 km2 |
| vatican-city | pass | Lateran Treaty 11 Feb / 7 Jun 1929 confirmed |
| san-marino | **fail** | 1503 Borgia and 1739-40 papal occupations on the page but not in the ledger; "Allied forces" placeholder counterpart |

## Fixes applied by the reviewer

- west-berlin `/ledger/9` (was /ledger/7): counterpart `french-fourth-republic` -> `french-fifth-republic`; hand-over pair added at 1958-10 (`/ledger/5` occupation_end french-fourth-republic, `/ledger/6` occupation_start french-fifth-republic), source French_Fourth_Republic ("The Fourth Republic was dissolved on 5 October 1958"), added to sources[].
- saar-protectorate `/ledger/1` vassal_start french-fourth-republic 1946-02 and `/ledger/5` vassal_end 1957-01, mirroring french-fourth-republic /ledger/4 and /ledger/10; page: "On 16 February 1946, France disentangled the Saar from the Allied zones of occupation", "a French protectorate", Saarland a West German state on 1 January 1957.
- donetsk-people-s-republic `/ledger/0`: confidence 3 -> 2 (region adds Kramatorsk, Mariupol and Debaltseve circles that no page says were held in April 2014).

## Failures (back to the author)

### transnistria
- `/keyframe_review/1/correction`: `{admin1: Transnistria}` resolves to one cell (116414) and `{admin1: Bender}` to four, so the 1992-2026 shape is ~1,265 km2 against the infobox 4,163 km2 (ratio 0.30), with the northern left bank (Rîbnița, Camenca) missing; the note says "within a factor of two", which is false. Redraw with circles along the left bank (e.g. 28.70E 48.03N, 29.00E 47.77N, 29.17E 47.45N, 29.30E 47.15N, 29.64E 46.84N, 29.80E 46.65N, 12-15 km, intersected with Moldova: 12-14 cells) or a <=12-point polygon; restate the measured ratio.
- `/keyframe_review/0/correction`: same problem, 1 cell for 1990-91.
- `/ledger/0`: counterpart republic-of-moldova in 1990 (Moldavian SSR); keep only if the Moldova dossier starts in 1990 (not blocking).

### san-marino
- Missing occupation 1503 (San Marino page: "In 1503, Cesare Borgia, the son of Pope Alexander VI, occupied the Republic for six months"); counterpart papal-states.
- Missing occupation 17 October 1739 to 5 February 1740 by the papal legate of Ravenna; counterpart papal-states, confidence 3.
- `/ledger/5`, `/ledger/6`, `/wars/0`: "Allied forces" is not a slug; open the Battle of San Marino page and use the army's state (expected united-kingdom).

## Thin (for a gap-filler)
- republika-srpska: 1992 gains (about 70% of Bosnia per the Bosnian War page) and 1995 losses (Operations Mistral 2 and Sana), Srebrenica and Zepa (July 1995); wartime seat Pale, not Banja Luka.
- donetsk-people-s-republic: Debaltseve is in the April 2014 found region and gained again in 2015-02 with no 2014 loss; the August 2014 Ilovaisk/Novoazovsk offensive (Azov strip) is not drawn; the 2022 gains are one 55% event.
- luhansk-people-s-republic: July 2014 Ukrainian recapture of Sievierodonetsk and Lysychansk; September 2022 losses (whole oblast held only "approximately two months").
- saar-protectorate: the 1947-06 gain names all of Saarland for 13 municipalities; the return of 61 municipalities (1947) is missing on both sides; the July 1946 extent is under-drawn.
- allied-occupied-germany: capital Berlin lies outside its own shape (Berlin split to west-berlin from 1945); say so or keep Berlin until 1948.
- west-berlin: Steinstuecken; area ratio 2.6 acknowledged as a grid limit.
- san-marino: previous holder of the 1463 castles (Malatesta of Rimini); Allied departure month.
- croatian-republic-of-herzeg-bosnia (optional): central Bosnian and Posavina pockets.

## Cross-dossier routing
- UK (/ledger/25, /ledger/28), USA (/ledger/115, /ledger/122), USSR (/ledger/33, /ledger/34, /ledger/51) record the German occupation and Kaliningrad against nazi-germany; switch to allied-occupied-germany. None of them has the West Berlin (1945-1990) or Trieste Zone A (1947-1954) occupations.
- nazi-germany: successors lack allied-occupied-germany; no September 1944 occupation of San Marino.
- eu-22-a french-fourth-republic: needs occupation_end west-berlin at 1958-10. eu-22-c french-fifth-republic: occupation of west-berlin 1958-10 to 1990-10.
- eu-22-e bosnia-and-herzegovina: no events for Western Bosnia (1993-09 loss, 1994 gain and loss, 1995-08 gain). federated-republic-of-germany: west-berlin missing as predecessor/merge in 1990-10.
- kingdom-of-italy: no 1929 loss to vatican-city.
- Unwritten owners (exceptions): eu-22-b SFRY; eu-22-c FRG, GDR, Poland, French Fifth Republic; eu-22-f Croatia, Moldova; eu-22-g Ukraine, Russian Federation.

Machine copy: history/notes/phase-b/reviews/eu-22-x.json.
