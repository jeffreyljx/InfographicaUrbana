# Review of batch eu-20-e (reviewer, 2026-11-01)

Seven dossiers: duchy-of-mecklenburg, mecklenburg-strelitz, duchy-of-nassau, duchy-of-oldenburg, free-city-of-bremen, free-city-of-lubeck, grand-duchy-of-baden. All validate (0 errors). Every spot-checked event (4-5 per dossier, 31 in all) is on its page with its year: no fabricated or mis-dated ledger event. The failures are all keyframe geometry: the reviewer tested Cliopatria's polygons (local v0.2.1 GeoJSON) against towns, and five dossiers draw their state partly or wholly in the wrong place while calling the shapes ok or correcting only something else.

Verdicts: duchy-of-mecklenburg **fail**, mecklenburg-strelitz **fail**, duchy-of-nassau **fail**, duchy-of-oldenburg **fail**, free-city-of-bremen **fail**, free-city-of-lubeck **fix**, grand-duchy-of-baden **pass**.

Reviewer edits (applied, re-validated, read back): duchy-of-mecklenburg /wars/0/to 1808 -> 1807 (War of the Fourth Coalition page: 9 October 1806 - 9 July 1807) with the page added to sources; free-city-of-lubeck /ledger/3 and /ledger/4 confidence 3 -> 2 (the region includes Bergedorf, which the Lübeck page does not name for 1811-1813).

## duchy-of-mecklenburg: fail

Area: reference 13161 km2, Cliopatria 11340 km2 (1820), ratio 0.86; Within a factor of two and acknowledged, but the 1,800 km2 gap is the missing southern strip (see fixes), not outline noise.

Findings:
- `/wars/0/to` (applied by reviewer): War of the Fourth Coalition ended in 1807, not 1808. Evidence: War of the Fourth Coalition page infobox: '9 October 1806 - 9 July 1807'. Fix: Set to 1807, append reviewer note, add the page to sources (done by reviewer; re-validated 0 errors).
- `/keyframe_review/0..10 (all eleven verdicts 'ok')` (for the author): Every Cliopatria shape omits the southern strip of Mecklenburg-Schwerin, so the 'ok' verdicts are wrong and the dossier draws a hole where the residence town lies. Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e: Ludwigslust (11.50 E 53.33 N), Parchim (11.85, 53.43), Grabow (11.56, 53.28), Neustadt-Glewe (11.59, 53.38), Lübz (12.03, 53.46), Röbel (12.60, 53.38) and Dömitz (11.25, 53.14) fall outside all eleven duchy-of-mecklenburg shapes; in 1806-1808 they lie inside Cliopatria's Kingdom of Prussia shape and in 1830 only inside the German Confederation umbrella (no state). The area gap matches: 11,340 km2 against 13,161 km2 (Grand Duchy infobox) and 13,304 km2 (German Confederation table). The kingdom-of-prussia dossier already marks a 473 km2 Prussian 'artefact in Mecklenburg (11.1-11.9 E, 53.2-53.6 N)' in its 1863 shape. Fix: Mark the eleven keyframes adjust with correction {'union': [{'cliopatria': 'Duchy of Mecklenburg', 'year': Y}, <the southern strip round Ludwigslust, Parchim, Grabow, Lübz and Dömitz>]}, e.g. lon/lat circles (Ludwigslust 11.50/53.33, Parchim 11.85/53.43, Lübz 12.03/53.46, Dömitz 11.25/53.14, about 15 km each) or a polygon on the Elde line, with text naming the towns; add a note that the strip is Prussian in Cliopatria's 1806 shape and no state's later.
- `/identity/wikidata` (for the author): Advisory (non-blocking): Q109252949 is the id Cliopatria gives its 'Duchy of Mecklenburg' row, whose Wikipedia article the dossier itself says is the medieval duchy, not Mecklenburg-Schwerin. Evidence: polities.csv row duchy-of-mecklenburg: wikipedia 'Duchy of Mecklenburg', wikidata Q109252949; the dossier's wikipedia field is 'Grand Duchy of Mecklenburg-Schwerin'. Fix: Keep the Cliopatria id only if it names Mecklenburg-Schwerin; otherwise set the Grand Duchy's id or null and say so in notes.

Gaps (for a gap-filler):
- `/ledger/2`: End of the French occupation, bridged to the 22 March 1808 accession at confidence 1; the duke's restoration (after Tilsit, 1807, per general histories) is on none of the pages opened. Try https://de.wikipedia.org/wiki/Friedrich_Franz_I._(Mecklenburg)
- `/identity/capitals`: Ludwigslust as the ducal residence (about 1765-1837) is on no page opened; only Schwerin is given. Try https://de.wikipedia.org/wiki/Ludwigslust
- `/ledger/0`: found at Cliopatria's first year, confidence 1 (convention, not a gap in substance). Try https://en.wikipedia.org/wiki/Duchy_of_Mecklenburg-Schwerin

Spot checks: `/ledger/1` confirmed ('In 1806 the territory was overrun by the First French Empire'); `/ledger/2` confirmed (table: 'Duchy of Mecklenburg-Schwerin | 22 Mar 1808'; Grand Duchy page 'treaty of 22 March 1808'); `/ledger/3` confirmed (infobox 'Congress of Vienna: 14 June 1815'); `/ledger/4` confirmed ('In 1867 he joined the North German Confederation'; both Mecklenburgs 'became states of the German Empire'); `/wars/0` mis-dated (to 1808; the war ended 9 July 1807); fixed by reviewer

## mecklenburg-strelitz: fail

Area: reference 2929 km2, Cliopatria 2551 km2 (1806), ratio 0.87; No infobox area; German Confederation table used. The near-match hides an over-drawn Ratzeburg part and a missing south-east Stargard.

Findings:
- `/keyframe_review/0..4/correction` (for the author): The corrections (Cliopatria 'Free City of Lübeck' row minus a Lübeck circle) leave out most of the south and east of the Lordship of Stargard, so they do not draw what their text says ('the Lordship of Stargard round Neustrelitz'). Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e: the row's eastern part is 12.68-13.55 E, 53.33-53.73 N, about 1,667 km2; Fürstenberg (13.14 E 53.18 N), Wesenberg (12.97, 53.28), Mirow (12.81, 53.27), Feldberg (13.43, 53.34), Woldegk (13.58, 53.46), Strasburg (13.74, 53.51) and Friedland (13.55, 53.66) lie outside it and in 1830 inside no state's shape (German Confederation umbrella only). The western part is 875 km2 against a Principality of Ratzeburg of a few hundred km2. German Confederation table: 2,929 km2. The Duchy page puts Stargard 'in the southeast of Mecklenburg'; 2,929 km2 minus the Ratzeburg part leaves well over 2,000 km2 for Stargard against the 1,667 km2 drawn. Fix: Add the missing Stargard land to every correction (union of lon/lat circles round Fürstenberg, Mirow/Wesenberg, Feldberg, Woldegk/Strasburg and Friedland, or a polygon), say in the note that the Ratzeburg part is over-drawn, and keep the Lübeck subtraction.

Gaps (for a gap-filler):
- `/ledger/0`: found at Cliopatria's first year, confidence 1 (convention). Try https://en.wikipedia.org/wiki/Duchy_of_Mecklenburg-Strelitz
- `/identity/wikidata`: wikidata null; the id is on no page opened. Try https://de.wikipedia.org/wiki/Mecklenburg-Strelitz

Spot checks: `/ledger/1` confirmed ('recognized both Mecklenburg-Strelitz and Mecklenburg-Schwerin as grand duchies'); `/ledger/2` confirmed ('both Mecklenburg-Schwerin and Mecklenburg-Strelitz became States of the German Empire'); `/ledger/0` confirmed (Section 2 of the 1701 treaty; infobox independent duchy 1806-1808); `/keyframe_review/0/note` confirmed text ('two detached parts', Ratzeburg bordering Lübeck); geometry incomplete (see fixes)

## duchy-of-nassau: fail

Area: reference 4700 km2, Cliopatria 11345 km2 (1806), ratio 2.41; 1806/1809/1811 lobes acknowledged and cut; but the 1807-1865 shapes (ratio 1.08-1.22) are misplaced (see fixes).

Findings:
- `/keyframe_review/1,4,5,6,7 (verdicts 'ok') and /keyframe_review/0,2,3,8/correction (built on the 1807 and 1865 shapes)` (for the author): Cliopatria's Nassau outline sits about 30 km too far west: it leaves out the duchy's Lahn and Taunus core, including the capital Weilburg, and takes in the left bank of the Rhine, so the 'ok' verdicts and the corrections built on it are wrong. Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e: outside the 1807 and 1820 shapes: Weilburg (capital 1806-1816, 8.26 E 50.49 N), Limburg (8.06, 50.39), Idstein (8.27, 50.22), Usingen (8.54, 50.33), Königstein (8.47, 50.18), Höchst (8.54, 50.10) and Hachenburg (7.82, 50.66), and of the 1815 acquisitions Dillenburg, Herborn, Hadamar and Diez; in 1830 Weilburg, Limburg and Idstein lie in Cliopatria's Grand Duchy of Hesse. Inside the shapes: Koblenz, Boppard, Andernach and Bingen on the left bank (French to 1814, then Prussian or Hessian), and, after 1815, Neuwied and (1820 shape) Altenkirchen, both Prussian from 1815. The polygon's east edge runs at 7.92 E from 50.25 to 50.51 N and its west edge at 7.07-7.34 E. The bbox alone (7.07-8.26 E) already excludes Höchst, Königstein and Cronberg, which the 1807 note lists as Nassau land. Fix: Mark the 1807, 1814, 1815, 1820 and 1865 keyframes adjust (and rebuild the other corrections) as {'union': [{'minus': [{'cliopatria': 'Duchy of Nassau', 'year': Y}, <the left bank of the Rhine, and from 1815 Neuwied and Altenkirchen>]}, <circles round Weilburg, Limburg/Diez/Hadamar, Idstein/Usingen and Königstein/Höchst; from 1815 Dillenburg/Herborn and Hadamar/Diez>]}, with text in the pages' words; note in the area check that the 5,093-5,756 km2 shapes match the 4,700 km2 table only by accident.
- `/ledger/1 and /ledger/2` (for the author): Advisory (non-blocking): Katzenelnbogen town is inside every Cliopatria shape from 1806, and the Siegen and Wetzlar circles lie almost wholly outside the duchy, so neither 1815 event changes the drawn duchy. Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e; the dossier's own note records the 1803/1815 Katzenelnbogen conflict. Fix: Say in /keyframe_review/5/note that Katzenelnbogen town is already drawn from 1806, and move the loss circles onto the Nassau side of the border (or shrink them).

Gaps (for a gap-filler):
- `/keyframe_review/6`: The +441 km2 step from the 1815 to the 1820 shape is explained by no page (author flagged). Try https://de.wikipedia.org/wiki/Nassau-Oranien
- `/wars/1`: The Prussian occupation of the duchy in July 1866 (the Duchy page: 'After being occupied and annexed into the Kingdom of Prussia in 1866') has no occupation_start in the ledger. Try https://en.wikipedia.org/wiki/Austro-Prussian_War

Spot checks: `/ledger/0` confirmed ('merged to form the Duchy of Nassau on 30 August 1806'); `/ledger/1` confirmed ('erhielt die Niedergrafschaft Katzenelnbogen', tied to the 31 May 1815 handover); `/ledger/2` confirmed ('Grenzstreifen nahe Siegen und Wetzlar an Preußen abgab'); `/ledger/3` confirmed (infobox 'Weilburg (1806-1816) Wiesbaden (1816-1866)'); `/ledger/4` confirmed ('Annexed by Prussia 20 September 1866'; Duchy infobox says 23 August, noted by author)

## duchy-of-oldenburg: fail

Area: reference 6420 km2, Cliopatria 4895 km2 (1820), ratio 0.76; Author compared with the 1939 figure 5,375 km2 (ratio 0.91); within a factor of two either way, but the shortfall is the missing Delmenhorst/Vechta/Weser land (see fixes).

Findings:
- `/keyframe_review/0..10/correction and /ledger/0/region` (for the author): The corrections claim 'the Duchy of Oldenburg round Oldenburg, Delmenhorst and the Münsterland' but only add Eutin to Cliopatria's outline, which leaves out Delmenhorst, Vechta, Wildeshausen and the Weser bank (Brake, Elsfleth). Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e: every Oldenburg shape stops at 8.47 E (bbox) and its south-east edge runs from 8.47/52.92 to 8.05/52.65; Delmenhorst (8.63 E 53.05 N) lies inside Cliopatria's 'Free City of Bremen' shapes, while Vechta (8.29, 52.73), Wildeshausen (8.43, 52.90) and Brake (8.48, 53.33) lie inside Cliopatria's Kingdom of Hanover (1803, 1840) and, in 1830, Kingdom of Great Britain shapes. The German Confederation table gives Oldenburg 6,420 km2 (with Birkenfeld and Eutin) against Cliopatria's 4,393-4,895 km2. Fix: Add to every correction (and the found and dissolve regions) Delmenhorst (e.g. the Cliopatria 'Free City of Bremen' shape of the same year minus the Bremen admin1, or a lon/lat circle at 8.63/53.05) and the Vechta-Wildeshausen and Wesermarsch land (circles round Vechta 8.29/52.73, Wildeshausen 8.43/52.90, Brake 8.48/53.33), with text from the pages; coordinate with the free-city-of-bremen fix so that Delmenhorst is drawn once, as Oldenburg.
- `/keyframe_review/0/note` (for the author): Advisory (non-blocking): the area check uses the 1939 figure (5,375 km2) instead of the German Confederation table. Evidence: German Confederation table: 'Grand Duchy of Oldenburg | 6,420 | 250,000'. Fix: Quote 6,420 km2 (ratio 0.68-0.76) and say it includes Birkenfeld and Eutin.

Gaps (for a gap-filler):
- `/ledger/0`: found at Cliopatria's first year, confidence 1. Try https://en.wikipedia.org/wiki/Duchy_of_Oldenburg
- `/keyframe_review/1`: Eutin's fate 1810-1813 (no keyframe for 1811-1812, and the 1810 loss region leaves Eutin out). Try https://en.wikipedia.org/wiki/Principality_of_L%C3%BCbeck
- `/ledger/3`: Who ceded Birkenfeld and whether possession began in 1815 or 1817. Try https://en.wikipedia.org/wiki/Principality_of_Birkenfeld

Spot checks: `/ledger/1` confirmed ('Duchy of Oldenburg | 14 Oct 1808 | Annexed by France on 13 December 1810'); `/ledger/2` confirmed (infobox '1785-1810 (restored 1813-23): William I'; confidence 2 apt); `/ledger/3` confirmed ('In 1815, the Duchy acquired the Principality of Birkenfeld and became a grand duchy'); `/ledger/5` confirmed ('fully annexed by Oldenburg in 1818'); `/ledger/6` confirmed ('In 1871, Oldenburg joined the German Empire')

## free-city-of-bremen: fail

Area: reference 256 km2, Cliopatria 517 km2 (1840), ratio 2.02; Acknowledged as grid noise, but the shape is misplaced (see fixes); the comparison must be redone on the corrected spec.

Findings:
- `/keyframe_review/0,3,6,7 (verdicts 'ok') and /keyframe_review/1,2,4,5/correction; /ledger/0,1,2,4/region` (for the author): Cliopatria's Bremen shapes do not contain the city of Bremen: they sit about 12 km west, on Delmenhorst (Oldenburg's town), so every keyframe and every ledger region built on them draws Bremen in the wrong place. Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e: the city (capital coordinate 8.80 E 53.08 N, gazetteer Bremen 8.80/53.08) is outside all five shapes, as are Vegesack (8.62, 53.17; Bremish per the Vegesack page) and Bremerhaven (8.58, 53.55); the shapes contain Delmenhorst (8.63, 53.05). The shapes' bbox ends at 8.73 E, west of the capital the dossier itself gives, and the 1806 note's claim 'the city and its immediate land' is wrong. In 1830 the city lies inside Cliopatria's Kingdom of Great Britain shape (in 1803-1804 and 1840 inside Kingdom of Hanover). Fix: Mark all eight keyframes wrong/adjust and draw Bremen from the gazetteer: 1806-1826 {'minus': [{'admin1': 'Bremen', 'country': 'Germany'}, {'place': 'Bremerhaven', 'km': 10}]} (or {'place': 'Bremen', 'km': 9} plus a Vegesack circle), from 1827 {'admin1': 'Bremen', 'country': 'Germany'}, text from the pages; use the same specs in /ledger/0, 1, 2 and 4; leave Delmenhorst to duchy-of-oldenburg; redo the area check (admin1 Bremen is about 420 km2 with Bremerhaven against 256 km2 in the table).

Gaps (for a gap-filler):
- `/ledger/0`: found at Cliopatria's first year, confidence 1; Bremen's 1806-1810 status and the 1815 recognition. Try https://de.wikipedia.org/wiki/Freie_Hansestadt_Bremen

Spot checks: `/ledger/1` confirmed ('annexed Bremen in 1811, as capital of the Département de Bouches-du-Weser'); `/ledger/2` confirmed ('In 1813, following their defeat at the Battle of Leipzig, the French withdrew'); `/ledger/3` confirmed ('In 1827, Bremen Mayor Smidt succeeded in purchasing a strip of land from the Kingdom of Hanover'); `/ledger/4` confirmed (North German Confederation after 1866; German Empire 1871)

## free-city-of-lubeck: fix

Area: reference 298 km2, Cliopatria 2669 km2 (1814), ratio 8.96; Row is Mecklenburg-Strelitz-shaped; marked wrong/adjust and replaced by a 10 km circle plus Bergedorf. Confirmed by geometry: two parts, 12.68-13.55 E (Stargard) and 10.45-11.22 E (Ratzeburg land).

Findings:
- `/ledger/3/confidence` (applied by reviewer): Confidence 3 on a region that includes the Bergedorf share, which the page does not name for 1811. Evidence: Free City of Lübeck page: the annexation sentence names only Lübeck; Bergedorf appears only for 1370, 1420 and the 1868 sale. Fix: Lowered to 2 with a reviewer note (re-validated 0 errors).
- `/ledger/4/confidence` (applied by reviewer): Same for the 1813 restoration. Evidence: 'Lübeck reassumed its pre-1811 status in 1813' names Lübeck only. Fix: Lowered to 2 with a reviewer note.
- `/keyframe_review/*/correction (the 10 km Lübeck circle)` (for the author): Advisory (non-blocking): the circle round the gazetteer point leaves out Travemünde, Lübeck's port about 16 km down the Trave, which therefore stays inside mecklenburg-strelitz's drawing (whose 12 km minus-circle does not reach it). Evidence: Point-in-polygon test on Cliopatria v0.2.1 geometry (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson) by reviewer eu-20-e: Travemünde (10.87 E 53.96 N) is inside every 'Free City of Lübeck' row shape; it is about 16 km from the Lübeck point. The Lübeck page does not mention Travemünde, so this rests on the map, not a page. Fix: Add a small Travemünde circle (or move the circle's centre north-east) and widen the minus-circle in mecklenburg-strelitz to match, once a page names Travemünde.

Gaps (for a gap-filler):
- `/ledger/2`: End of the French occupation, bridged to the 1811 annexation at confidence 1. Try https://de.wikipedia.org/wiki/Geschichte_der_Hansestadt_L%C3%BCbeck
- `/keyframe_review/0`: Lübeck's Landgebiet and Travemünde: the page names no territory. Try https://de.wikipedia.org/wiki/Travem%C3%BCnde

Spot checks: `/ledger/1` confirmed ('occupied neutral Lübeck after a battle against Blücher on 6 November 1806'); `/ledger/3` confirmed ('from 1811 to 1813, Lübeck was formally annexed'); confidence lowered (Bergedorf unnamed); `/ledger/4` confirmed ('reassumed its pre-1811 status in 1813'); confidence lowered; `/ledger/5` confirmed (joined the NGC 1867; 'The following year' sold its Bergedorf share to Hamburg)

## grand-duchy-of-baden: pass

Area: reference 15082 km2, Cliopatria 14354 km2 (1870), ratio 0.95; German Confederation table 15,269 km2. Geometry: 19 of 23 tested Baden towns inside; edge cells miss Baden-Baden, Pforzheim, Konstanz, Bretten, Sinsheim, Tauberbischofsheim, Breisach and Wertheim and take in Speyer and Tuttlingen, which is within the grid's precision for a state 30-40 km wide.

Gaps (for a gap-filler):
- `/ledger/8`: End of the Prussian occupation, bridged to 1852 at confidence 1. Try https://de.wikipedia.org/wiki/Badische_Revolution
- `/ledger/2`: The page ties the Württemberg accessions to Schönbrunn 1809; the boundary treaty itself (Paris, 1810), which would explain Cliopatria's 1811 date, is on no page opened. Try https://de.wikipedia.org/wiki/Gro%C3%9Fherzogtum_Baden
- `/keyframe_review/4,8`: The 1815 drop (-270 km2) and the 1870 growth (+178 km2) are unexplained (author flagged; within one grid cell). Try https://de.wikipedia.org/wiki/Gro%C3%9Fherzogtum_Baden

Spot checks: `/ledger/2` confirmed ('rewarded with accessions of territory at the expense of the Kingdom of Württemberg', Treaty of Schönbrunn 1809); `/ledger/3` confirmed ('That same night of 13/14 May Grand Duke Leopold flees'); `/ledger/5` confirmed ('The Prussians march into Freiburg unopposed', 7 July); `/ledger/6` confirmed ('After being surrounded for three weeks Rastaat surrenders to Groeben', 23 July); `/ledger/9` confirmed (infobox German Unification 18 January 1871)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| duchy-of-mecklenburg 1806 found <- mecklenburg | mecklenburg 1805 dissolve | matched | mecklenburg (eu-09-x) ends 1805 with dissolve to duchy-of-mecklenburg; holy-roman-empire-minor-states also gives 47 cells to duchy-of-mecklenburg in 1806/8 (double claim on the HRE side, Cliopatria re-cut). |
| duchy-of-mecklenburg 1806 occupation_start <- first-french-empire | - | missing | first-french-empire (eu-20) has no occupation of Mecklenburg-Schwerin; route to its owner. |
| duchy-of-mecklenburg 1808 occupation_end <- first-french-empire | - | missing | As above. |
| mecklenburg-strelitz 1806 found <- mecklenburg | mecklenburg 1805 dissolve | mismatch | mecklenburg's dissolve and successors name only duchy-of-mecklenburg, although its successor land includes a circle at 13.26 E 53.56 N (Neubrandenburg, Strelitz land); mecklenburg's owner (eu-09-x) should add mecklenburg-strelitz as a successor. |
| duchy-of-nassau 1806 found <- county-of-nassau | county-of-nassau 1806 dissolve | matched | Also holy-roman-empire-minor-states 1806/7 loss to duchy-of-nassau of 47 cells (North Rhine-Westphalia 21, Rhineland-Palatinate 19): the NRW cells are the northern lobe the Nassau dossier cuts; that land needs another owner (Berg, Arenberg, Salm) on the HRE side. |
| duchy-of-nassau 1815 gain <- kingdom-of-prussia | - | missing | kingdom-of-prussia (eu-09) has no 1815 loss of the Niedergrafschaft Katzenelnbogen to Nassau. |
| duchy-of-nassau 1815 loss <- kingdom-of-prussia | - | missing | kingdom-of-prussia has no 1815 gain of the strips near Siegen and Wetzlar (its L50 mentions only the Orange-Nassau lands). |
| duchy-of-nassau 1866 dissolve <- kingdom-of-prussia | kingdom-of-prussia 1866 gain | matched | Prussia dates the annexation 23 August 1866 (Peace of Prague), Nassau 20 September 1866 (annexation law); both on pages, same year. |
| duchy-of-oldenburg 1806 found <- county-of-oldenburg | county-of-oldenburg 1805 dissolve | mismatch | Matched in slug and year, but county-of-oldenburg's successor land includes a Jever circle (7.9 E 53.57 N) in 1805, while Jever came to Oldenburg only in 1818 (Lordship of Jever page); route to eu-09-x. |
| duchy-of-oldenburg 1810 loss <- first-french-empire | first-french-empire 1810 gain | matched | Both 13 December 1810. |
| duchy-of-oldenburg 1813 gain <- first-french-empire | first-french-empire 1814 loss | mismatch | first-french-empire has no 1813 loss to Oldenburg; its 30 May 1814 loss goes to german-confederation. Route to the FFE owner. |
| duchy-of-oldenburg 1815 gain <- principality-of-birkenfeld | - | exception | No dossier; listed in the author's counterparts_needing_dossiers. |
| duchy-of-oldenburg 1818 gain <- lordship-of-jever | - | exception | No dossier; listed. Note batavian-republic 1807 gain of Jever names kingdom-of-prussia as counterpart, against the Jever page (Russian 1793-1807). |
| free-city-of-bremen 1806 found <- free-imperial-city-of-bremen | - | exception | No dossier; listed in counterparts_needing_dossiers (eu-09). |
| free-city-of-bremen 1811 loss <- first-french-empire | first-french-empire 1811 gain | mismatch | FFE's 1811 gain names free-city-of-hamburg as counterpart and Bremen only in its note; it needs a separate event (or counterpart) for Bremen. |
| free-city-of-bremen 1813 gain <- first-french-empire | first-french-empire 1814 loss | mismatch | FFE has no 1813 loss to Bremen; its 1814 loss goes to german-confederation. |
| free-city-of-bremen 1827 gain <- kingdom-of-hanover | - | missing | kingdom-of-hanover (eu-20, written) has no 1827 loss of the Bremerhaven strip; route to its owner. |
| free-city-of-lubeck 1806 found <- free-imperial-city-of-lubeck | free-imperial-city-of-lubeck 1806 dissolve | matched |  |
| free-city-of-lubeck 1806 occupation_start <- first-french-empire | - | missing | FFE has no occupation of Lübeck (6 November 1806). |
| free-city-of-lubeck 1811 occupation_end <- first-french-empire | - | missing | As above. |
| free-city-of-lubeck 1811 loss <- first-french-empire | first-french-empire 1811 gain | mismatch | FFE's 1811 gain has counterpart free-city-of-hamburg and names Lübeck only in its note. |
| free-city-of-lubeck 1813 gain <- first-french-empire | first-french-empire 1814 loss | mismatch | FFE has no 1813 loss to Lübeck; its 1814 loss goes to german-confederation. |
| free-city-of-lubeck 1868 loss <- free-city-of-hamburg | - | exception | free-city-of-hamburg is owned by an eu-20 part that has not run yet (no file). |
| grand-duchy-of-baden 1806 found <- electorate-of-baden | electorate-of-baden 1805 dissolve | matched |  |
| grand-duchy-of-baden 1806 gain <- holy-roman-empire-minor-states | holy-roman-empire-minor-states 1806 loss | matched | HRE L117, 1806/7, 15 cells. |
| grand-duchy-of-baden 1809 gain <- kingdom-of-wurttemberg | - | missing | kingdom-of-wurttemberg (eu-20, written) has no 1809/1810 loss to Baden; route to its owner. |
| grand-duchy-of-baden 1849 loss <- republic-of-baden | - | exception | republic-of-baden is owned by an eu-20 part that has not run yet; the contest_start/contest_end and the July gain wait for it too. |
| grand-duchy-of-baden 1849 gain <- republic-of-baden | - | exception | As above. |
| grand-duchy-of-baden 1849 occupation_start <- kingdom-of-prussia | - | missing | kingdom-of-prussia (eu-09) has no occupation of Baden 1849-1852. |
| grand-duchy-of-baden 1852 occupation_end <- kingdom-of-prussia | - | missing | As above. |
| duchy-of-nassau 1807 keyframe <- grand-duchy-of-hesse | - | mismatch | Geometry: Cliopatria draws Nassau's Weilburg, Limburg and Idstein inside its Grand Duchy of Hesse shapes (1830 test); grand-duchy-of-hesse (eu-20, not yet written) must cut them when Nassau is redrawn. |
| free-city-of-bremen 1830 keyframe <- kingdom-of-hanover | - | mismatch | Geometry: Bremen city, Vegesack and Bremerhaven, and Oldenburg's Vechta, Wildeshausen and Brake lie inside Cliopatria's Kingdom of Hanover (1803, 1840) and Kingdom of Great Britain (1820-1839) shapes; the kingdom-of-hanover dossier (1815 keyframe applies the 1840 outline) should cut them. |
| free-city-of-lubeck 1830 keyframe <- denmark-norway | - | mismatch | Geometry: Lübeck city lies inside Cliopatria's 'Denmark-Norway' shape in 1830 (Holstein); the dossier that takes that row after 1814 (Denmark/Holstein) should cut the Lübeck circle. |
| duchy-of-mecklenburg 1806 keyframe <- kingdom-of-prussia | - | mismatch | Geometry: Cliopatria's 1806 Kingdom of Prussia shape covers southern Mecklenburg-Schwerin (Ludwigslust, Parchim, Grabow, Lübz, Dömitz); the Prussia dossier should cut it from its 1806 keyframe as it did for 1863. |

## Gazetteer names wanted

Katzenelnbogen (duchy-of-nassau), Siegen (duchy-of-nassau), Wetzlar (duchy-of-nassau), Weilburg (duchy-of-nassau), Limburg an der Lahn (duchy-of-nassau), Idstein (duchy-of-nassau), Dillenburg (duchy-of-nassau), Eutin (duchy-of-oldenburg), Birkenfeld (duchy-of-oldenburg), Jever (duchy-of-oldenburg), Delmenhorst (duchy-of-oldenburg), Vechta (duchy-of-oldenburg), Wildeshausen (duchy-of-oldenburg), Brake (duchy-of-oldenburg), Vegesack (free-city-of-bremen), Bergedorf (free-city-of-lubeck), Travemünde (free-city-of-lubeck), Ludwigslust (duchy-of-mecklenburg), Parchim (duchy-of-mecklenburg), Neustrelitz (mecklenburg-strelitz), Fürstenberg/Havel (mecklenburg-strelitz), Friedland (Mecklenburg) (mecklenburg-strelitz)

## Problems

- No page failed to load for the reviewer (16 fetches).
- Keyframe geometry was checked by point-in-polygon on the local Cliopatria v0.2.1 GeoJSON (/tmp/claude-0/dl/clio/cliopatria_polities_only_v021.geojson); the authors had only shapes.csv bbox and area, so the Mecklenburg, Strelitz and Vechta findings were not visible to them from bbox alone (the Bremen, Nassau and Delmenhorst ones were).
- Reviewer applied fixes in duchy-of-mecklenburg (/wars/0/to 1808 -> 1807, source added) and free-city-of-lubeck (/ledger/3 and /ledger/4 confidence 3 -> 2); both re-validated with 0 errors and read back.
- free-city-of-bremen and duchy-of-oldenburg must be fixed together: Delmenhorst is drawn as Bremen in Cliopatria and belongs to Oldenburg.
- first-french-empire (eu-20) carries no events for the 1806 occupations of Mecklenburg-Schwerin and Lübeck, lumps the 1811 annexations of Bremen and Lübeck under counterpart free-city-of-hamburg, and has no 1813 losses to Oldenburg, Bremen or Lübeck.
- german-empire has no dossier yet; all seven dissolve events point to it.
