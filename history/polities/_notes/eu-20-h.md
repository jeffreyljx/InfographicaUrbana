# Notes, batch eu-20-h (written 2026-11-01)

Seven dossiers written for the six owned states (the Free City of Danzig is two states). All validate with 0 errors (`--resolve`: no unresolved region names). 14 pages opened (11 English Wikipedia, 3 German Wikipedia); no event rests on a snippet or on memory. Page budget: Reuss-Gera 3 of 5, Waldeck 2 of 5, Saxe-Altenburg 3 of 5, Confederation of the Rhine 1 of 1-2, Duchy of Warsaw 2 of 1-2, Danzig 3 across both dossiers (of 5).

## Findings the orchestrator must act on

1. **Cliopatria's "Confederation of the Rhine" rows are Prussia's territory.** The 1809-1813 shape (170,588 km2) holds Berlin, Breslau, Stettin, Königsberg and Tilsit and shares no cell with Bavaria, Saxony or Westphalia (gazetteer check); the 1814 shape (258,129 km2) holds Berlin, Cologne, Münster, Magdeburg, Leipzig, Kassel, Hannover. The page says "Prussia itself was not a member". Cliopatria's Kingdom of Prussia has only a 1,787 km2 strip for 1807-1808, an 87 km2 sliver for 1814 and 594 km2 for 1815-1833. The Prussia group (eu-09) should take these two shapes (1809-1814) for Prussia; the Confederation dossier marks both `wrong`.
2. **The Confederation is filed as `umbrella`** (an association of sovereign states under Napoleon's protection; rule 4). The `gain` events are dated accessions of members, not land. Its keyframes give the union of the members' Cliopatria shapes only as the extent a state page may quote. colours.json already assigns it a colour as if territory; the colour/render owner should decide.
3. **Saxe-Altenburg**: Cliopatria's 1806-1825 shapes are Saxe-Gotha-Altenburg (3,007 km2 in 1800), already carried by `duchy-of-saxe-gotha-altenburg` (1735-1825 keyframe). This dossier starts at the division of 12 November 1826 and marks the earlier shapes `wrong`. The 1828-1870 shapes hold Gotha, Eisenberg and Eisenach cells but not Altenburg; replaced by the Ostkreis/Westkreis radii. This settles the open question of the Gotha-Altenburg dossier.
4. **Free City of Danzig is two states in one Cliopatria row**: the Napoleonic city (21 July 1807 to 2 January 1814; new slug `free-city-of-danzig-1807-1814`, reviews the 1809 shape) and the interwar city (15 November 1920 to 1 September 1939; keeps `free-city-of-danzig`, reviews 1919-1939). Each lists Cliopatria Name "Free City of Danzig", so the validator warns that the other's shapes have no verdict (expected).
5. **Cliopatria's 1919-1935 Danzig shapes include the Memel Territory** (1,952 + 2,657 = 4,609 km2 against 4,828 and 4,912). The Memel Territory (Klaipėda Region) was German, then under French administration from 15 February 1920, annexed by Lithuania 19 January 1923. Needs a dossier (suggested `klaipeda-region`, eu-21) and a check that Cliopatria's Kingdom of Lithuania row carries it.
6. **Waldeck's six shapes are misplaced** about 27 km west of the real Waldeck and omit Pyrmont; replaced by radii at Arolsen, Korbach, Wildungen and Pyrmont (the districts named on the German page).
7. **Reuss-Gera's shapes also carry the Elder Line (Greiz)**; no Cliopatria row or dossier exists for Reuss-Greiz. Suggested `principality-of-reuss-greiz`, 1778-1918. The Gera cell is missing from every shape and is added; the 1815-1819 shape (3,180 km2) holds Saalfeld/Rudolstadt cells and is `wrong`.
8. **End years** for the German states follow the sibling dossiers (1871, the German Empire row takes over); the real endings are 1918 (Reuss, Altenburg) and 1929 (Waldeck). The Duchy of Warsaw ends 9 June 1815 (Congress of Vienna) although Cliopatria stops in 1813; 1814-1815 is a new keyframe under Russian occupation.

## Per state

**confederation-of-the-rhine** (umbrella, 1806-07 to 1813-11). Page: Confederation of the Rhine. Member accession dates are the page's table (Würzburg 23 Sep 1806, Saxony 11 Dec 1806, Saxon duchies 15 Dec 1806, Anhalt/Lippe/Reuss/Waldeck 11 and 18 Apr 1807, Westphalia 15 Nov 1807, Mecklenburg 18 Feb and 22 Mar 1808, Oldenburg 14 Oct 1808, Oldenburg and Salm annexed 13 Dec 1810); dissolved 4 Nov 1813. Hanseatic towns: [corrected 2026-11-01 after the review] the page lists "the Free Hansa towns of Hamburg, Lübeck, and Bremen" among the lands "not included in the Confederation", so leaving them out of the unions is right and the gap is void. Not settled: founders without a Cliopatria shape (Arenberg, Isenburg, Leyen, Liechtenstein, Salm, Hohenzollern-Hechingen, Schaumburg-Lippe, Schwarzburg, Saxe-Coburg, Saxe-Meiningen); the infobox 325,700 km2 has no year. The only war entry is the Battle of Leipzig (Leipzig and Sixth Coalition pages not opened).

**duchy-of-warsaw** (1807-07 to 1815-06). Pages: Duchy of Warsaw; Austro-Polish War. Cliopatria's 1809 shape (100,411 km2) is the pre-Schönbrunn duchy (page: about 104,000 km2); the treaty of 14 Oct 1809 enlarged it to about 155,000 km2, but Cliopatria enlarges only in 1811, so 1810 is a new keyframe. Not opened: Treaty of Schönbrunn, Tilsit, French invasion of Russia. The 1815 successor regions (Greater Poland, a 19 km radius at Kraków, the remainder) are readings. Białystok district went to Russia at Tilsit, not to the duchy.

**free-city-of-danzig** (interwar). Pages: Free City of Danzig; Klaipėda Region. The date the Versailles clause took effect is on neither page (the Klaipėda infobox says "10 January 1919", sic). Annexation 1 September 1939 (infobox) vs "October 1939" (text) is unresolved on the page. No ruler list.

**free-city-of-danzig-1807-1814** (Napoleonic). Page: Free City of Danzig (Napoleonic), the URL that loaded. Area 478 km2 against Cliopatria's 1,192 km2 (ratio 0.40, grid cause). The French governor (Rapp) is recorded as an occupation event in the city's own ledger (the Westphalia/Saxe-Coburg convention). Infobox says "under the protection of Saxony and Prussia"; [Corrected 2026-11-01 after the review] the infobox Status reads "Client state of the French Empire under the protection of Saxony and Prussia", so France is named; the occupation pair (governor Rapp) is kept as a defensible reading, a vassal pair with first-french-empire would fit equally (the French side has no Danzig event yet).

**principality-of-reuss-gera** (1806-04 to 1871). Pages: Principality of Reuss-Gera (= Reuss Junior Line); House of Reuss; German "Reuß jüngerer Linie". Treated as one state with the 1824 and 1848 unions as `merge` events inside the Junior Line. Neither English page dates the 1807 Confederation accession (the Confederation page does: 11 and 18 April 1807).

**principality-of-waldeck-and-pyrmont** (1806 to 1871). Pages: English article; German "Waldeck und Pyrmont". Pyrmont a separate principality 1806-1812 (reunion month from the ruler table, 24 Sep 1812). Memberships (Rheinbund 18 Apr 1807, German Confederation 1815, North German Confederation, Prussian treaty Oct 1867) are not ledger events.

**saxe-altenburg** (1826-11 to 1871). Pages: Saxe-Altenburg; Saxe-Gotha-Altenburg; German "Sachsen-Altenburg". Only two ledger events: no page opened dates any Altenburg border change after 1826. Wars: none on the pages (the 4 February 1867 military convention with Prussia and the 1866 war are not treated).

## Pages that would not load

- https://en.wikipedia.org/wiki/Polish%E2%80%93Austrian_War (retried as Austro-Polish_War: loaded)
- https://en.wikipedia.org/wiki/Free_City_of_Danzig_(1807%E2%80%931814) (loaded as Free_City_of_Danzig_(Napoleonic))
- https://de.wikipedia.org/wiki/Waldeck_(Staat) and https://de.wikipedia.org/wiki/Waldeck_(Territorium) (loaded as Waldeck_und_Pyrmont)

## Gazetteer names wanted (radii use coordinates until added)

Altenburg (12.44E 50.99N), Eisenberg (Thuringia) (11.90E 50.97N), Roda/Stadtroda and Kahla (11.64E 50.82N), Lobenstein/Ebersdorf (11.70E 50.47N), Arolsen/Bad Arolsen (9.01E 51.38N), Korbach (8.87E 51.27N), Wildungen/Bad Wildungen (9.12E 51.12N), Pyrmont/Bad Pyrmont (9.26E 51.98N).

## Counterparts needing dossiers

Principality of Reuss-Greiz (Reuss Elder Line), Klaipėda Region / Memel Territory, Congress Poland (Kingdom of Poland 1815), Saxe-Hildburghausen, Grand Duchy of Frankfurt, Principality of Schaumburg-Lippe; minor Confederation founders (Salm, Isenburg, Leyen, Liechtenstein, Hohenzollern-Hechingen) have no Cliopatria shape. Kingdom of Prussia needs 1807-1833 shapes.

## Repair 2026-11-01 (returning to the review of eu-20-h)

Only duchy-of-warsaw was failed; the other six were pass or fix (the reviewer edited confederation-of-the-rhine and free-city-of-danzig-1807-1814 /notes itself; their wording above is brought in line). Validation after the repair: all seven dossiers 0 errors; duchy-of-warsaw 0 warnings with `--resolve`.

**duchy-of-warsaw: what I changed**
1. Added `vassal_start` 1807-07, counterpart first-french-empire, confidence 3 (page: infobox Status "Satellite state of the French Empire, Personal union with the Kingdom of Saxony"; "was a French client state established by Napoleon Bonaparte in 1807"; "formally an independent duchy, allied to France"). Mirrors first-french-empire /ledger/12.
2. Added `vassal_end` 1813-01, counterpart first-french-empire, confidence 2: the Russian occupation of January 1813 ("most of the territory of the Duchy of Warsaw was occupied by Russia in January 1813"; "the existence of the duchy in anything but name came to an end"). The page does not say that French control ended in that month, hence 2. Mirrors first-french-empire /ledger/54, which already carries 1813-01 at confidence 2 (no month to pass on to its owner).
3. Thin, /ledger/8 (loss to Prussia, 1815-06): the region was Greater Poland only. Pages opened: Duchy of Warsaw ("The Kulmerland and Gdańsk (Danzig) became part of the Province of West Prussia"; the rest "reconstituted into the Grand Duchy of Posen"), Grand Duchy of Posen ("subdivided into two government districts: Posen and Bromberg"; "In 1817, the Culmerland (Chełmno Land) was moved to West Prussia"), Chełmno Land ("Between 1807 and 1815 Chełmno Land was a part of the Polish Duchy of Warsaw"; "In 1815 it was annexed by Prussia again, first it became part of the Grand Duchy of Posen"; Toruń its largest city). The region is now the 1812 outline intersected with Greater Poland, a 50 km radius at Bydgoszcz (the Bromberg district) and a 50 km radius at 18.7E 53.2N (the Chełmno Land, Toruń inside). /ledger/10 (loss to Russia) and the two successors in `identity` were changed to the same cut. Check: the remainder is about 122,700 km2 in gazetteer cells against 128,500 km2 for the Congress kingdom on the Congress Poland page (ratio 0.95).
4. Thin, keyframe duchy-of-warsaw_1814: Congress Poland page opened; it is silent on the occupation and on the 1814 extent (only the post-Vienna 128,500 km2 and about 3.3 million people). The Duchy page says "The rest of the duchy was restored to Prussia" without date or place. The 1812 outline stays as a confidence-1 bridge; note extended.
5. Sources: 3 added (Grand Duchy of Posen, Chełmno Land, Congress Poland), 5 in all. Page budget (1-2) exceeded by three on purpose, because the review asked for them.

**What I do not follow the reviewer on**
- Toruń and the Kuyavian part of the cession. The reviewer asked for Toruń, the Chełmno Land and the Bydgoszcz department, and notes that kingdom-of-prussia /ledger/46 gives "Greater Poland, Kuyavia and the Chełmno Land". None of the three pages opened here names Kuyavia or Toruń as a transfer (the Chełmno Land page implies Toruń by calling it the land's largest city). Only the Kuyavian ground inside the Bydgoszcz radius is drawn. Adding the gazetteer's whole Kuyavia region would draw about 5,600 km2 of cells more (it reaches 19.56E) and leave 117,100 km2 for the Congress kingdom (ratio 0.91). The reviewer's matrix entry "Warsaw-Prussia 1815 land" therefore stays a partial mismatch until the Prussia owner and this dossier cite one page for Kuyavia.
- The Chełmno Land went into the Grand Duchy of Posen first and into West Prussia in 1817; the Warsaw page (West Prussia) and the other two pages (Posen, then West Prussia) differ. The ledger takes the Prussian side either way.

**Gazetteer names wanted** (new): Chełmno Land (region, about 18.7E 53.2N: Toruń, Chełmno, Grudziądz, Brodnica) and Toruń (place, 18.60E 53.01N; "Torun", "Thorn", "Toruń" all return nothing from `gazetteer.py names`). The Chełmno ground is a coordinate radius until then.

**Counterparts**: congress-poland.json now exists in history/polities (struck from the list above); added principality-of-pyrmont (1806-1812, reviewer's request); free-city-of-krakow is still unwritten (eu-20, another part), and Warsaw's /ledger/9 loss names it.

