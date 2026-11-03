# Review of batch eu-20-i (Phase B)

Reviewed 2026-11-01 (brief filled 2026-10-31) by the adversarial reviewer. Dossiers: kingdom-of-westphalia, bessarabia, duchy-of-brunswick, free-city-of-hamburg, kingdom-of-norway, sovereign-principality-of-the-united-netherlands. Validator with --resolve: 0 errors, 1 warning (Lüneburg). Neighbour dossiers read: every Context polity of brief section 6 with a file in history/polities/ plus the counterparts named in the ledgers (denmark-norway, swedish-empire, united-kingdoms-of-sweden-and-norway, greenland, nazi-germany, netherlands, first-french-empire, kingdom-of-hanover, kingdom-of-prussia, electorate-of-hesse, duchy-of-brunswick-luneburg, county-of-stolberg, free-city-of-lubeck, free-city-of-bremen, duchy-of-oldenburg, russian-empire, ottoman-empire, british-colonial-empire, dutch-suriname). Not yet written (group not run): principality-of-moldavia, german-empire, german-confederation, confederation-of-the-rhine and the other eu-20 Context rows without files.

Verdict meaning in this run: fix = fixed by the reviewer (any unapplied item left is non-blocking); fail = at least one unapplied blocking finding, back to the author.

## kingdom-of-westphalia: fail

Area: infobox 63652 km2 (1810) vs Cliopatria 43140 km2, ratio 0.68, acknowledged True. 1809: 37,883 vs 43,140 (1.14); 1812: 45,427 vs 38,231 (0.84); all within a factor of two and noted in keyframes.

Findings:
- `/ledger` (not applied; blocking): The dossier has no vassal_start/vassal_end with first-french-empire, though the page calls Westphalia a client state of France and first-french-empire records both ends of the relation against this slug. Evidence: Kingdom of Westphalia page: infobox status 'Client state of the French Empire'; lead 'a client state of France in present-day Germany that existed from 1807 to 1813'; 'The state was a member of the Confederation of the Rhine.' first-french-empire /ledger/4 vassal_start 1807-11 and /ledger/21 vassal_end 1813-10 both name kingdom-of-westphalia and have no mirror here. Fix: Add vassal_start 1807 (month 7, or 11 to match first-french-empire /ledger/4) and vassal_end 1813-10, counterpart first-french-empire, region {cliopatria: Kingdom of Westphalia, year: 1809}, source the Kingdom of Westphalia page, confidence 3 for the status (the start month is the author's choice; say so in the note).
- `/ledger/5` (not applied; non-blocking): The 1810 gain covers only Hanover, but /ledger/7 then loses Nord and Niederelbe (Stade, Lüneburg) in December 1810, land the ledger never gained; the 1810 extent (infobox 63,652 km2) is drawn nowhere. Evidence: Page: 'In December 1810, the short-lived coastal and northern départements Nord ("North", capital Stade) and Niederelbe ("Lower Elbe", capital Lüneburg) were ceded to the French Empire'; department table 'Aller | Hanover | 1810-1813'. kingdom-of-hanover /ledger/3 already says the rest of the Hanoverian realm went to Westphalia and France in 1810. Fix: Widen /ledger/5's region to the union of Hanover, Lüneburg and Stade (the Aller, Niederelbe and Nord departments), still counterpart kingdom-of-hanover at confidence 2, so the December 1810 loss returns land that was gained.
- `/ledger/4` (not applied; non-blocking): Osnabrück (Weser department 1807-1810, Hanoverian since 1803) is lost in /ledger/6 but never gained; the 1807 gain from Hanover covers only Göttingen and Grubenhagen. Evidence: Page original territories: 'The principalities of Brunswick-Wolfenbüttel, Hildesheim, Halberstadt, Quedlinbourg, Osnabrück, Paderborn and Minden'; table 'Weser | Osnabrück | 1807-1810'. Fix: Add Osnabrück (place, about 40 km) to /ledger/4's region (union with Göttingen), counterpart kingdom-of-hanover, confidence 2.
- `/ledger` (not applied; non-blocking): There is no 1807 gain from county-of-stolberg, though that dossier dissolves into Westphalia in 1807 and this page lists the county among the original territories. Evidence: Page: 'The counties of Mansfeld, Stolberg, Ravensberg, Rietberg' among the original lands; county-of-stolberg /ledger/8 dissolve 1807 counterpart kingdom-of-westphalia ('mediatised in 1807 and made part of the Kingdom of Westphalia'). Fix: Add a 1807 gain, counterpart county-of-stolberg, region {place: Wernigerode, km: 20}, confidence 2, source the Kingdom of Westphalia page.

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Westphalia: confirmed (lead: territories ceded by Prussia at Tilsit 'including the Altmark, the part of the Duchy of Magdeburg west of the Elbe'; list: Halberstadt, Hildesheim, Quedlinbourg, Paderborn, Minden)
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_Westphalia: confirmed (December 1810, Nord capital Stade and Niederelbe capital Lüneburg ceded to the French Empire)
- `/ledger/8` https://en.wikipedia.org/wiki/Kingdom_of_Westphalia: confirmed (Chernyshyov took Cassel 'on the night of 28 to 29 September'; French retook it on 7 October)
- `/ledger/10` https://en.wikipedia.org/wiki/Kingdom_of_Westphalia: confirmed ('Prussian troops occupied Westphalia on 26 October'; 'the status quo of 1806 was restored'; Prussia in 1815)

## bessarabia: thin

Area: infobox 45630 km2 (1812) vs Cliopatria 42009 km2, ratio 0.92, acknowledged True. No infobox area on the Bessarabia page; 45,630 km2 is the Treaty of Bucharest page. The Cliopatria shape is the wrong land (west of the Prut: bbox 25.02-28.24E excludes Chișinău at 28.86E), verdict wrong, correction region Bessarabia.

Findings:
- `/ledger/1` (not applied; non-blocking): The May 1812 gain of the Budjak from the Ottomans is also recorded by russian-empire, so two dossiers gain the same land in the same month; the Ottoman loss names russian-empire. Evidence: russian-empire /ledger/56 gain 1812-5 cp ottoman-empire ('Russia gained the eastern half of Moldavia ... which it renamed Bessarabia'); ottoman-empire /ledger/165 loss 1812 cp russian-empire. The author's own notes say the land lies inside Cliopatria's Russian Empire shape from 1811. Fix: Orchestrator decision: either retire this dossier (the Cliopatria row is the wrong land and Bessarabia was a Russian province, not a separate polity) or keep it as a province drawn over Russian land and drop the duplicated gain from the renderer's land accounting. Nothing for the author to research.
- `/ledger/0/region` (not applied; non-blocking): The found event takes the whole region 'Bessarabia' from Moldavia, which already includes the Budjak that /ledger/1 then gains from the Ottomans; predecessors[0] correctly uses Bessarabia minus Budjak. Evidence: identity/predecessors[0].land = minus [Bessarabia, Budjak]; Bessarabia page: Ottoman 'direct rule only in Budjak and Khotyn'. Fix: Set /ledger/0's region to {minus: [{region: Bessarabia}, {region: Budjak}]} as in predecessors[0].

Thin:
- `/ledger/2`: The 1813 dissolve is Cliopatria's row end, not an event (confidence 1); Bessarabia stays Russian. A date for the 1812 provisional administration (oblast) would let the row end on an event or be retired. Page to try: https://en.wikipedia.org/wiki/Bessarabia_Governorate
- `/identity/predecessors/1`: Khotyn (Ottoman direct rule) after 1812 is on no page opened. Page to try: https://en.wikipedia.org/wiki/Khotyn

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Treaty_of_Bucharest_(1812): confirmed ('signed on 28 May 1812, in Manuc's Inn in Bucharest, and ratified on 5 July 1812'; area 45,630 km2)
- `/ledger/1` https://en.wikipedia.org/wiki/Treaty_of_Bucharest_(1812): confirmed ('the Budjak and the eastern half of the Principality of Moldavia, between Prut and Dniester' ceded by the Ottoman Empire)
- `/ledger/2` https://en.wikipedia.org/wiki/Bessarabia: confirmed as stated: page silent on 1813; oblast 1818, guberniya 1873
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Bessarabia: confirmed ('Chișinău, the former capital of the Russian Bessarabia Governorate'; no 1812 date, as the note says)

## duchy-of-brunswick: fix

Area: infobox 3672 km2 (1910) vs Cliopatria 4704 km2, ratio 1.28, acknowledged True. Same 3,672 km2 in the States of the German Empire table.

Findings:
- `/identity/rulers/1 and /identity/rulers/2` (applied by reviewer; non-blocking): Rulers Charles II and William VIII cited no page. Evidence: Duchy of Brunswick page, rulers list: '1815-1830: Charles II, son of Frederick William. Forced to flee Brunswick in 1830'; '1830-1884: William VIII. Brother of Charles II.' Fix: Added source https://en.wikipedia.org/wiki/Duchy_of_Brunswick to both; revalidated (0 errors, 0 warnings).
- `/keyframe_review/0/correction` (not applied; non-blocking): The new 1813 keyframe already draws the Thedinghausen and Calvörde exclaves, which /ledger/2 gains only in 1814, from kingdom-of-westphalia, a state dissolved in October 1813. Evidence: German page: '1813 wurde Herzog Friedrich Wilhelm restituiert' and the duchy was set up 1814 'in den alten Grenzen des Fürstentums Braunschweig-Wolfenbüttel'; the parts 'um 1814' include Amt Calvörde and Amt Thedinghausen. kingdom-of-westphalia ends 1813-10. Fix: Either date /ledger/2 1813-10 with the restoration (the exclaves were old Wolfenbüttel lands) or drop the two circles from keyframe 0; the counterpart may stay kingdom-of-westphalia (within one year of its dissolve).

Thin:
- `/keyframe_review/2`: Cliopatria's 1814 to 1820 change (+477 km2, edge cells) and 1864 to 1866 change (-174 km2) have no event; the pages opened (budget 5 of 5 used) record no cession, and the German page names only the failed Hildesheim claim. Thin by design; likely redrawing. Page to try: https://de.wikipedia.org/wiki/Kommunionharz

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Frederick_William,_Duke_of_Brunswick-Wolfenb%C3%BCttel: confirmed (second reign '26 October 1813 - 16 June 1815'; returned in December 1813 'after Prussia had ended French domination')
- `/ledger/1` https://en.wikipedia.org/wiki/Duchy_of_Brunswick: confirmed ('The Wolfenbüttel principality had from 1807 to 1813 been held as part of the Kingdom of Westphalia.')
- `/ledger/3` https://en.wikipedia.org/wiki/Duchy_of_Brunswick: confirmed ('recognized as a sovereign state by the Congress of Vienna in 1815')
- `/ledger/4` https://en.wikipedia.org/wiki/Duchy_of_Brunswick: confirmed ('It joined first the North German Confederation and in 1871 the German Empire')

## free-city-of-hamburg: fail

Area: infobox 414 km2 (1910) vs Cliopatria 1436 km2, ratio 3.47, acknowledged False. The Hamburg infobox gives only the modern 755 km2 (2016); 414 km2 is the States of the German Empire table (Empire period, year not stated). 1814 shape 751 km2 = 1.81.

Findings:
- `/identity/start` (not applied; blocking): The dossier starts in 1814, but the page makes Hamburg a sovereign state from 1806 that 're-assumed its pre-1811 status' in 1814, the same state; first-french-empire annexes 'free-city-of-hamburg' in 1811 with no mirror here, and Hamburg 1806-1810 is drawn by no dossier. Evidence: Hamburg page: after the dissolution of the Holy Roman Empire in 1806 Hamburg 'became a sovereign state with the official title of the Free and Hanseatic City of Hamburg'; 'Hamburg re-assumed its pre-1811 status as a city-state in 1814'. first-french-empire /ledger/13 gain 1811 counterpart free-city-of-hamburg. Sibling dossiers free-city-of-lubeck, free-city-of-bremen and duchy-of-oldenburg all start in 1806 and carry the French annexation as loss/gain. The dossier's own notes say 'the 1806-1813 years belong to the First French Empire here', which first-french-empire contradicts for 1806-1810. The war 'Siege of Hamburg' (from 1813) also lies before the current start. Fix: Start in 1806 (found 1806, counterpart holy-roman-empire or nobody), add a new keyframe 1806-1813 from the 1814 shape plus Ritzebüttel (adjust), a French occupation from November 1806 if a page supports it (free-city-of-lubeck models one), loss 1811 to first-french-empire (Bergedorf page: annexed to the Bouches de l'Elbe département 1811-1813), and turn the 1814 'found' into a gain from first-french-empire; keep the Ritzebüttel event and certainty spans consistent.
- `/keyframe_review/2/note` (not applied; blocking): The 1820-1870 shapes (1,436-1,479 km2) are about 3.5 times Hamburg's area before 1937, and the 1814 shape (751 km2) 1.8 times; the notes compare only with the 2016 city (755 km2) and leave the question open. Evidence: States of the German Empire page, table: 'Hamburg | Hamburg | Free City | 414 | ...' (km2; Bremen 256, Lübeck 298, Brunswick 3,672). The 1820 bbox reaches 8.37E, west of Neuwerk (8.50E), so the polygon likely includes the Elbe estuary. Fix: Cite the 414 km2 figure (add the page to sources) and resolve: adjust the 1820-1870 keyframes to the city with Bergedorf, Geesthacht and the Ritzebüttel circle, or state why Cliopatria's outline is kept (grid granularity).

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Hamburg: confirmed ('Russian forces under General Bennigsen finally freed the city in 1814'; 're-assumed its pre-1811 status as a city-state in 1814')
- `/ledger/1` https://en.wikipedia.org/wiki/Cuxhaven: confirmed as stated at confidence 2 ('belonged to Hamburg from the 13th century until 1937'; page silent on the French years)
- `/ledger/2` https://en.wikipedia.org/wiki/Bergedorf: confirmed (sale of Lübeck's share for 200,000 Prussian thaler, 'Effective of 1 January 1868')
- `/ledger/3` https://en.wikipedia.org/wiki/Hamburg: confirmed (member of the North German Confederation 1866-1871 and the German Empire 1871-1918)

## kingdom-of-norway: pass

Area: infobox 385207 km2 (2024) vs Cliopatria 420717 km2, ratio 1.09, acknowledged True. Page: 385,207 km2 including Svalbard and Jan Mayen, 323,808 without. Tried and could not break: dates of the union, 1905, Jan Mayen, Svalbard, the East Greenland claim and the occupation; every territorial event mirrored by united-kingdoms-of-sweden-and-norway, greenland and nazi-germany; keyframe corrections (Greenland strip removed, 1941 Jan-Mayen-only shape replaced) match the ledger; capitals and certainty cover 1814-2024.

Spot checks:
- `/ledger/3` https://en.wikipedia.org/wiki/Union_between_Sweden_and_Norway: confirmed (Storting adopted the amendments 'on 4 November and unanimously elected Charles XIII King of Norway, rather than acknowledging him as such')
- `/ledger/6` https://en.wikipedia.org/wiki/Jan_Mayen: confirmed ('annexed the middle part of the island for Norway in 1922', whole island 1926, de jure 27 February 1930, 377 km2)
- `/ledger/7` https://en.wikipedia.org/wiki/Svalbard: confirmed (treaty 9 February 1920 'granting full sovereignty to Norway', 'took effect on 14 August 1925'; 62,045 km2)
- `/ledger/8` https://en.wikipedia.org/wiki/Erik_the_Red%27s_Land: confirmed (flag at Myggbukta June 1931; proclamation 10 July 1931, 71°30' to 75°40'N; awarded to Denmark 5 April 1933)
- `/ledger/0` https://en.wikipedia.org/wiki/Norway: confirmed (infobox 'State re-established: 25 February 1814'; 'Kingdoms of Sweden-Norway (personal union): 4 November 1814'; 'Union dissolved: 7 June 1905')

## sovereign-principality-of-the-united-netherlands: pass

Area: infobox None km2 (None) vs Cliopatria 35750 km2, ratio None, acknowledged True. No area on the page (population 2,233,000 in 1815 only); stated in the keyframe note. The 1814 keyframe stays ok for the Northern Netherlands with the August 1814 Belgian gain carried by the ledger (year-resolution keyframes cannot split 1814; the note says so). The page infobox does date the Anglo-Dutch Treaty (13 August 1814), contrary to the author's gap entry, but gives no content; the colonies belong to other dossiers.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sovereign_Principality_of_the_United_Netherlands: confirmed (Triumvirate 'formally took control over the liberated country on 20 November'; Scheveningen 30 November 1813; Sovereign Prince 2 December)
- `/ledger/1` https://en.wikipedia.org/wiki/Sovereign_Principality_of_the_United_Netherlands: confirmed (Allied military government February 1814; Treaty of Paris 30 May 1814, Meuse left bank; Eight Articles 21 June 1814; 'He became Governor-General of Belgium on 1 August')
- `/ledger/2` https://en.wikipedia.org/wiki/Sovereign_Principality_of_the_United_Netherlands: confirmed ('the reunification was finalised on 16 March 1815 when William Frederick was proclaimed King')
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Sovereign_Principality_of_the_United_Netherlands: confirmed (infobox capital Amsterdam)

## Cross-dossier matrix

- kingdom-of-westphalia 1807 gain (cp kingdom-of-prussia) / mirror: kingdom-of-prussia 1807 loss / **matched**: /ledger/1 vs prussia /ledger/38 (1807-7).
- kingdom-of-westphalia 1807 gain (cp electorate-of-hesse) / mirror: electorate-of-hesse 1807 loss / **matched**: /ledger/2 vs hesse /ledger/5 (1807-7).
- kingdom-of-westphalia 1807 gain (cp duchy-of-brunswick-luneburg) / mirror: duchy-of-brunswick-luneburg 1807 dissolve / **matched**: /ledger/3 vs brunswick-luneburg /ledger/12.
- kingdom-of-westphalia 1807 gain (cp kingdom-of-hanover) / mirror: kingdom-of-hanover 1807 loss / **matched**: /ledger/4 vs hanover /ledger/2; Osnabrück missing from the Westphalia region (fix).
- county-of-stolberg 1807 dissolve (cp kingdom-of-westphalia) / mirror: none / **missing**: county-of-stolberg /ledger/8 dissolves into Westphalia; Westphalia has no gain (fix listed, eu-20-i).
- first-french-empire 1807 vassal_start (cp kingdom-of-westphalia) / mirror: none / **missing**: first-french-empire /ledger/4 (1807-11); Westphalia has no vassal_start (blocking fix, eu-20-i).
- kingdom-of-westphalia 1810 gain (cp kingdom-of-hanover) / mirror: kingdom-of-hanover 1810 loss / **matched**: /ledger/5 vs hanover /ledger/3.
- kingdom-of-westphalia 1810 loss (cp first-french-empire) / mirror: none / **missing**: /ledger/6 (Osnabrück, inferred recipient, confidence 2): first-french-empire records no 1810 gain from Westphalia.
- kingdom-of-westphalia 1810 loss (cp first-french-empire) / mirror: kingdom-of-hanover 1810 loss / **mismatch**: /ledger/7 (Nord, Niederelbe, 1810-12): kingdom-of-hanover /ledger/4 loses the same departments to first-french-empire in 1810-12 itself; first-french-empire records neither (its /ledger/13 1811 North Sea coast gain names free-city-of-hamburg). One of Westphalia/Hanover must hold the land in 1810 (Westphalia per its page); route to eu-20 (first-french-empire, kingdom-of-hanover).
- kingdom-of-westphalia 1813 contest_start (cp russian-empire) / mirror: none / **missing**: /ledger/8 (Chernyshyov's raid on Cassel): russian-empire has no event; minor, route to eu-17 or accept.
- first-french-empire 1813 vassal_end (cp kingdom-of-westphalia) / mirror: none / **missing**: first-french-empire /ledger/21 (1813-10); Westphalia has no vassal_end (blocking fix, eu-20-i).
- kingdom-of-westphalia 1813 dissolve (cp kingdom-of-prussia) / mirror: kingdom-of-prussia 1815 gain / **mismatch**: Westphalia dissolves 1813-10; kingdom-of-prussia /ledger/44 gains from kingdom-of-westphalia on 1815-6, 20 months after it ceased to exist. Route to eu-09: the 1815 Prussian gains should name the 1813-1815 holders (Hanover, Hesse, Brunswick or nobody).
- kingdom-of-westphalia 1813 dissolve (cp kingdom-of-prussia) / mirror: electorate-of-hesse 1813 gain / **matched**: hesse /ledger/9 (1813-11), kingdom-of-hanover /ledger/6 (1813-10) and duchy-of-brunswick /ledger/1 (1813-10) take their lands back from the dissolving kingdom.
- bessarabia 1812 found (cp principality-of-moldavia) / mirror: none / **exception**: principality-of-moldavia has no dossier yet (eu-18 not run).
- bessarabia 1812 gain (cp ottoman-empire) / mirror: ottoman-empire 1812 loss / **mismatch**: ottoman-empire /ledger/165 loses Bessarabia to russian-empire, and russian-empire /ledger/56 gains it in 1812-5: the land is gained twice (orchestrator decision on the bessarabia row).
- bessarabia 1813 dissolve (cp russian-empire) / mirror: none / **exception**: Cliopatria row end, confidence 1; russian-empire holds the land throughout.
- duchy-of-brunswick 1813 gain (cp kingdom-of-westphalia) / mirror: kingdom-of-westphalia 1813 dissolve / **matched**: /ledger/1 vs Westphalia /ledger/10 (1813-10).
- duchy-of-brunswick 1814 gain (cp kingdom-of-westphalia) / mirror: kingdom-of-westphalia 1813 dissolve / **matched**: /ledger/2 (exclaves) within a year of Westphalia's dissolve; the 1813 keyframe already draws them (non-blocking fix).
- duchy-of-brunswick 1871 dissolve (cp german-empire) / mirror: none / **exception**: german-empire belongs to a part of eu-20 not written yet.
- first-french-empire 1811 gain (cp free-city-of-hamburg) / mirror: none / **missing**: first-french-empire /ledger/13; the Hamburg dossier starts in 1814 (blocking fix: start 1806, loss 1811).
- free-city-of-hamburg 1814 found (cp first-french-empire) / mirror: first-french-empire 1814 dissolve / **matched**: first-french-empire /ledger/24 (1814-4) and /ledger/27 (1814-5, German states to german-confederation, no dossier yet). After the Hamburg fix this becomes a gain from first-french-empire.
- free-city-of-hamburg 1814 gain (cp first-french-empire) / mirror: first-french-empire 1814 dissolve / **matched**: Ritzebüttel, confidence 2; same mirror as above.
- free-city-of-hamburg 1868 gain (cp free-city-of-lubeck) / mirror: free-city-of-lubeck 1868 loss / **matched**: Bergedorf; Lübeck /ledger/5. Bergedorf is drawn by both cities until 1868 (flagged by the author).
- free-city-of-hamburg 1871 dissolve (cp german-empire) / mirror: none / **exception**: german-empire not written yet.
- kingdom-of-norway 1814 found (cp denmark-norway) / mirror: denmark-norway 1814 dissolve / **mismatch**: denmark-norway /ledger/38 dissolve 1814-1 matches, but /ledger/37 gives Norway to swedish-empire in 1814-1 and swedish-empire records no gain; Norway's dossier (sourced) holds Norway Feb-Nov 1814. Route to eu-14: /ledger/37's counterpart should be kingdom-of-norway or the land nobody's until February 1814.
- kingdom-of-norway 1814 contest_start (cp swedish-empire) / mirror: none / **missing**: /ledger/1-2 (Swedish invasion 27 July, Convention of Moss 14 August): swedish-empire has no contest events. Route to eu-14.
- kingdom-of-norway 1814 loss (cp united-kingdoms-of-sweden-and-norway) / mirror: united-kingdoms-of-sweden-and-norway 1814 gain / **matched**: union /ledger/1 (1814-11).
- kingdom-of-norway 1905 gain (cp united-kingdoms-of-sweden-and-norway) / mirror: united-kingdoms-of-sweden-and-norway 1905 loss / **matched**: union /ledger/2 (1905-6).
- kingdom-of-norway 1922 gain (cp nobody) / mirror: none / **exception**: Jan Mayen; 1925 Svalbard likewise nobody.
- kingdom-of-norway 1931 contest_start (cp greenland) / mirror: greenland 1931 contest_start / **matched**: greenland /ledger/26; contest_end 1933-4 vs greenland /ledger/27 matched.
- greenland 1933 gain (cp kingdom-of-norway) / mirror: none / **mismatch**: greenland /ledger/28 gains the East Greenland strip from Norway in 1933-4, but Norway's 1932 keyframe correction never draws it as Norwegian (contest only), so there is nothing to lose. Route to the greenland owner: drop the gain (keep the contest).
- kingdom-of-norway 1940 occupation_start (cp nazi-germany) / mirror: nazi-germany 1940 occupation_start / **matched**: nazi-germany /ledger/14, /20, /21, /80 mirror the contest_start 1940-4, contest_end 1940-6, occupation_start 1940-6 and occupation_end 1945-5.
- sovereign-principality-of-the-united-netherlands 1813 found (cp first-french-empire) / mirror: first-french-empire 1813 loss / **matched**: first-french-empire /ledger/20.
- sovereign-principality-of-the-united-netherlands 1814 gain (cp first-french-empire) / mirror: none / **exception**: Belgium (1814-8) was under Allied military government from February 1814 and first-french-empire ended 1814-4; the author lists the optional allied-military-government-of-belgium dossier.
- sovereign-principality-of-the-united-netherlands 1815 dissolve (cp netherlands) / mirror: netherlands 1815 found / **mismatch**: netherlands /ledger/0 found matches, but netherlands /ledger/1 gains the southern Netherlands from nobody in 1815-3 although the principality's dissolve already passes Belgium on. Route to the netherlands owner: drop or re-counterpart that gain.
- british-colonial-empire 1814 loss (cp sovereign-principality-of-the-united-netherlands) / mirror: none / **mismatch**: british-colonial-empire /ledger/77 returns Suriname and the Dutch Caribbean to the principality, which draws no colonies; dutch-suriname /ledger/8 ends the British occupation in 1816 against british-colonial-empire. Route to the british-colonial-empire owner: counterpart dutch-suriname (and the island colonies' dossiers).
- british-colonial-empire 1814 gain (cp sovereign-principality-of-the-united-netherlands) / mirror: none / **mismatch**: british-colonial-empire /ledger/76 (Demerara, Essequibo, Berbice): the principality draws no colonies and there is no Dutch Guiana dossier; route to the british-colonial-empire owner (counterpart nobody or an occupation already running since 1803).

## Problems

- No page failed to load. Extra page opened for the area check: https://en.wikipedia.org/wiki/States_of_the_German_Empire (Hamburg 414 km2, Brunswick 3,672 km2).
- Reviewer applied one fix: duchy-of-brunswick.json /identity/rulers/1-2 source URL added; revalidated 0 errors, read back after the write.
- Validator (--resolve) on the batch: 0 errors; 1 warning (Westphalia /ledger/7/region, unknown place Lüneburg).
- Cross-dossier mismatches to route outside eu-20-i: eu-14 (denmark-norway /ledger/37, swedish-empire contest 1814), eu-09 (kingdom-of-prussia /ledger/44 gain from Westphalia in 1815), eu-20 (first-french-empire and kingdom-of-hanover over Nord/Niederelbe 1810), greenland /ledger/28, netherlands /ledger/1, british-colonial-empire /ledger/76-77, russian-empire /ledger/56 vs bessarabia.
- Bessarabia: orchestrator decision needed on whether a Russian province with a wrong Cliopatria shape keeps its own dossier (double gain with russian-empire).
