# Review of batch am-08-d (Phase B, 2026-10-19)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Machine copy: history/notes/phase-b/reviews/am-08-d.json.

Mechanical: all seven dossiers validate with `--resolve` (0 errors); the only warning is the unresolved region 'Puna de Atacama' (bolivia /ledger/5, argentine-confederation /ledger/22). Neighbour dossiers read (ledgers grepped): republic-of-peru, republic-of-chile, paraguay, empire-of-brazil, spanish-empire, rio-de-la-plata, gran-colombia. Not yet written (am-08 parts not run): peru-bolivian-confederation, brazilian-republic, state-of-buenos-aires, granadine-confederation, argentine-republic, venezuela, republic-of-colombia. The authors' counterpart exceptions for those are accepted.

| slug | verdict |
| --- | --- |
| bolivia | fail |
| oriental-republic-of-uruguay | pass |
| argentine-confederation | fix |
| republic-of-ecuador | fix |
| republic-of-new-granada | thin |
| republic-of-acre | fix |
| gobierno-del-cerrito | pass |

## bolivia: fail
1. **Blocking. Presidente Hayes is drawn twice, 1878-1935.** Keyframes 5-10 (bolivia_1877 to bolivia_1929) are 'ok' or 'shape unchanged', but the Cliopatria shape holds 313 of the 323 gazetteer cells of Paraguay's Presidente Hayes department (about 78,000 km2). The Paraguay dossier draws that land as Paraguayan from the 1878 Hayes award (its /ledger/16 and the paraguay_1877 correction). Bolivia's 1935 loss (/ledger/16, 1,057 cells) takes those 313 cells from Bolivia a second time, while Paraguay's matching gain (/ledger/19) covers only Boquerón and Alto Paraguay. The Chaco War page the dossier cites gives no ground for a Bolivian presence on the Paraguay River opposite Asunción: Bolivia founded Puerto Pacheco in 1885 and 'Paraguay evicted the Bolivians from it in 1888'; its Pilcomayo outposts date from 1905; Paraguayan and Argentine ranchers and the 1920s Mennonite colonies held the east. Fix: make keyframes 5-10 'adjust' with the correction minus {admin1 Presidente Hayes, Paraguay} from 1878. In keyframes 0-4, say who held that bank before 1878 (Villa Occidental; the Argentine occupation 1869-1879). Restrict /ledger/14-16 and the Chaco War zone to Boquerón plus Alto Paraguay.
2. **/ledger/5, the Puna in 1899 (confidence 2).** The cited page says the 1899 lawsuit 'originated from transfers between Bolivia and Argentina of land occupied by Chile during the Pacific war'. The note's quote leaves out the words after 'Argentina'. Bolivia held no Puna land after 14 February 1879 (/ledger/4), and the 1899 award was between Argentina and Chile. Fix: delete the event, or redate it to the Bolivia-Argentina cession (1889, unverified) with a page that gives the date.
3. **/ledger/10, applied by the reviewer.** The Abunã disk was 60 km (44 cells, about 11,000 km2) for land the Treaty of Petrópolis page sizes at 'over 3,000 km2'. It is now km 31 (12 cells), and the file re-validates.
4. **/ledger/6-8, the Acre contest (not blocking).** The contest runs unbroken from July 1899 to November 1903, but Bolivia held Acre from 15 March 1900 to 6 August 1902, except for the short rising of November-December 1900. Fix: split the contest, mirrored in republic-of-acre.
5. **Gaps (thin):** the year of the La Paz seat (/ledger/7, confidence 1); the 1841-1842 war with Peru; the 1866 and 1874 boundary treaties with Chile; the year Tarija was incorporated. The 1909 Madre de Dios loss is confirmed on the Bolivia page, but republic-of-peru has no matching gain.

Spot checks: /ledger/13, 9, 10, 4, 11 (year only; the page has no month), 15 and 6 are confirmed; /ledger/5 is only partly on its page. Area: the infobox gives 1,098,581 km2 and the 2024 shape is 1,085,071 km2 (ratio 0.99).

## oriental-republic-of-uruguay: pass
I tried all six events on four pages and could not break any. Cisplatine War: 27 August 1828. Uruguay page: siege of Montevideo from February 1843. Uruguayan Civil War: Oribe defeated in 1851. Uruguayan War: Cerro Largo invaded 14 October 1864; accord of 20 February 1865. The 1828 gain matches empire-of-brazil /ledger/11, and the Cerrito contest matches gobierno-del-cerrito. Area: 176,215 km2 in the infobox against 180,732 km2 in the shape (ratio 1.03). Still open for other dossiers: empire-of-brazil has no 1864-1865 contest, and the date the Brazilian forces left is a gap.

## argentine-confederation: fix
1. **/ledger/22, the Puna (confidence 2).** The counterpart should be republic-of-chile, the occupier: the page says the Puna was 'land occupied by Chile during the Pacific war'. Quote the whole sentence. Chile's dossier then needs the matching loss.
2. **/ledger/19-20, the 1881 treaty.** These gains name republic-of-chile, and Chile's /ledger/23 names argentine-confederation for the same treaty, so each side gains from the other and neither loses. The page gives the line (23 July 1881, 68°34' W) but does not say that either state held the land it received. Fix: counterpart 'nobody' on both sides (Chile already uses 'nobody' for Aysén in its /ledger/24), or add the mirror losses in both dossiers.
3. **/ledger/0 and keyframe 0, the overlap with rio-de-la-plata (the author's flag).** This dossier starts on 4 January 1831 (infobox 'Federal Pact: 4 January 1831'), while rio-de-la-plata runs to 1833. The orchestrator decides which one yields.
4. **Gaps (thin):** /ledger/10 (confidence 1, 1866): the page puts the expulsion from Corrientes 'in subsequent months' after the September 1865 surrender at Uruguaiana, which probably means late 1865; paraguay /ledger/8 has the same date. Also: the Buenos Aires frontier advances of 1840 (/ledger/3, confidence 1) and 1868 (keyframe 10, no event); the Hayes award year (/ledger/16, confidence 1); the 1862 capital (/ledger/8, confidence 1); the date of control of Santa Cruz.

Spot checks: /ledger/9 and 15 (Paraguayan War), /ledger/1, 17, 18 and 21 (Conquest of the Desert) and /ledger/4 and 6 (State of Buenos Aires) are confirmed. /ledger/19 is confirmed apart from its counterpart; /ledger/22 is misquoted. The keyframe corrections (Chaco removed to 1872, Formosa to 1876) agree with the ledger. Area: the infobox has no area (I read it), and the 1905-1929 shape is modern Argentina (2.79 M km2).

## republic-of-ecuador: fix
1. **Missing: Ecuador's hold on Cauca, 1830-1832.** The author's gap says 'page silent', but the cited Ecuador page says Ecuador 'annexed the Department of Cauca on 20 December 1830' and that 'The Treaty of Pasto of 1832 was signed by which the Department of Cauca was turned over to New Granada'. Fix: add a 1830-12 gain and a 1832 loss to republic-of-new-granada (confidence 2), and adjust keyframe 0 to match. New Granada needs the mirror event.
2. **Thin.** The territorial-dispute page gives a real transfer of possessed land in 1942: 'Ecuador ceded 18,552 km2 of previously possessed territory to Peru' and Peru ceded 5,072 km2, both measured against the 1936 status quo line. The author keeps this in the notes because the modern-Ecuador shape never holds the land; a gap-filler should look for the line (try the Rio Protocol page). /ledger/6 (confidence 1, Loja and Zamora) is also a gap.

Spot checks: /ledger/4, 5 and 7 (the 1941 war; El Oro vacated 12 February 1942), /ledger/3 (Mapasingue, 'February 25, 1860') and /ledger/1 (Galápagos in 1832, year only) are confirmed. Area: 283,561 km2 in the infobox against 262,773 km2 in the shape (ratio 0.93).

## republic-of-new-granada: thin (by the 1-2 page budget)
Both events are confirmed (20 October 1831; renamed in 1858, constitution of 11 April 1858). Area: 1,331,250 km2 in the infobox against 1,423,060 km2 in the 1834 shape (ratio 1.07), acknowledged. Unexplained:
- the 1853 drop of 199,712 km2;
- the 1832 gain of Cauca from Ecuador, while the 1831-1833 keyframe gives Cauca to New Granada throughout;
- Panama's 1840 breakaway ('tried unsuccessfully to break away ... in 1840 and 1850') and the zones of the War of the Supremes, which are empty;
- the 0.2 M km2 difference from gran-colombia's handover (the author's flag).

## republic-of-acre: fix
All seven events are confirmed on the Acre War and Treaty of Petrópolis pages (14 July 1899; 15 March 1900; 6 August 1902; 24 and 27 January 1903; 17 November 1903).
- Fix: the contest runs unbroken from 1899 to 1903 although the dossier's own /ledger/2 ends the republic in March 1900. Split it 1900-03 to 1902-08, mirrored in bolivia.
- Thin: Brazil's military occupation in 1903 (preliminary treaty of 21 March 1903; a military government under Olímpio da Silveira, undated on the page) is missing, and so is the November-December 1900 republic.
- The capital, Puerto Alonso, lies inside the 80 km keyframe.

## gobierno-del-cerrito: pass
The events are confirmed: February 1843 (Uruguay page); 1843-1851 and 'the rest of the country' (Uruguayan Civil War page). The capital at Cerrito de la Victoria shares a grid cell with Montevideo, which the region removes. That is a resolution artifact and I accept it.

## Cross-dossier work for other authors
- paraguay: the Argentine occupation 1869-1876; the Misiones contest 1838-1876; whether Presidente Hayes is Paraguayan before 1878.
- republic-of-chile: the counterpart of /ledger/23 for the 1881 treaty; a Puna loss in 1899.
- republic-of-peru: the 1909 Madre de Dios gain; the 1859-1860 occupation of Guayaquil.
- empire-of-brazil: the 1864-1865 invasion of Uruguay.
- rio-de-la-plata: its end year (overlap 1831-1833).
- republic-of-new-granada and republic-of-ecuador: the 1832 Cauca pair.
