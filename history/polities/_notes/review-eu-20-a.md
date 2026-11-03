# Review of batch eu-20-a

Reviewer: adversarial review, 2026-10-31. Six dossiers, all valid (0 errors before and after the reviewer's edits). Verdicts: french-first-republic thin, batavian-republic thin, french-directory thin, cisalpine-republic thin, grand-duchy-of-tuscany thin, ligurian-republic thin.

No confidence-3 event that was spot-checked turned out fabricated or mis-dated. Every dossier is honest about its gaps, and every one lacks events that its neighbours already record against it. Those missing events are the main work left; they are routed below. The reviewer applied small, page-verified fixes, listed with applied: true. Everything else is for the author or a gap-filler.

## french-first-republic: thin

Area: infobox 3000000 km2 (1800), Cliopatria 644860 km2, ratio 0.21, acknowledged True. The infobox figure (1800, 'including colonies') is not comparable; both keyframe notes say so. Cliopatria for 1800 (french-consulate) is 671,882 km2.

Findings:
- `/ledger/8/region` (APPLIED by reviewer): The 1794 Rhineland occupation used the gazetteer region 'Rhineland', which includes the right bank. Evidence: The gazetteer region 'Rhineland' is Rheinland-Pfalz + Saarland + all of Nordrhein-Westfalen, so it paints the right bank (Westphalia, Berg, the Ruhr) French; the pages give only the left bank. The 1794 Cliopatria shape stops at the Rhine. Fix: Region set to {'intersect': [{'region': 'Rhineland'}, {'cliopatria': 'French First Republic', 'year': 1794}]} with the text kept.
- `/identity/end` (for the author): Ends 1795-11 while french-directory starts 1795-10, so both dossiers draw France for about a week. Evidence: French First Republic page: 'On 3 November 1795, the Directory was established.' French Directory page: Formation '26/31 October 1795'. The author's notes flag the overlap. Fix: The orchestrator picks one changeover date (26 October 1795, the Convention's last sitting, or 3 November) and the author aligns end/dissolve here with found in french-directory.
- `/ledger (new, 1793)` (for the author): The annexation of Monaco is missing although its dossier records it. Evidence: principality-of-monaco L14: 1793 loss to french-first-republic, c=3, 'From 1793 to 1814 Monaco was taken over by France'. Territorial evolution page: 'The County of Nice and several small enclaves (1793)'. Fix: Add a 1793 gain, counterpart principality-of-monaco, region {place: Monaco, km 5} (Monaco, Menton, Roquebrune), confidence 2.
- `/ledger and /wars (new)` (for the author): The War of the Pyrenees occupations are missing: no occupation pairs and no zones in Spain. Evidence: kingdom-of-spain L57-L60: occupation_start french-first-republic Gipuzkoa 1794-08 (c=3) and Figueres/Roses 1794-11 (c=2), both ended 1795-07 (Basel). Spain is a belligerent in /wars/0, but its zones are only Belgium, the Rhineland and Savoy. Fix: Add occupation_start/occupation_end pairs with counterpart kingdom-of-spain (1794-08 to 1795-07 Gipuzkoa, 1794-11 to 1795-07 Figueres and Roses), and a zone or a separate war entry.
- `/ledger (1794-1795)` (for the author): The Dutch conquests of 1794 have no event here, though dutch-republic records them. Evidence: dutch-republic L43 (1794, Generality lands, c=1) and L44 (1794-11, Maastricht, 'Prince Frederick capitulated on 4 November', c=3) are losses to french-first-republic. This ledger gains the same land only by the treaty of 1795-05 (L15), from batavian-republic. Fix: Add occupation_start dutch-republic 1794-11 for Maastricht and States-Flanders, ended by the 1795-05 gain, or explain the choice in the note.
- `/ledger/4` (for the author): Nice: dated here as a 1793 annexation, but kingdom-of-sardinia records an occupation from 1792-09 and a cession to french-directory in 1796-05. Evidence: Territorial evolution page (opened): 'The County of Nice and several small enclaves' (1793), which is confirmed. kingdom-of-sardinia L11 occupation_start 1792-09, L13/L14 1796-05. Fix: Add occupation_start kingdom-of-sardinia 1792-09 for Nice, ended by this 1793 gain. Route the cession-date disagreement to eu-13 (Sardinia's L13 also names french-first-republic in 1796).
- `/ledger/6` (for the author): The second Liège occupation is at confidence 1 with no month, though the Liège dossier dates it. The first occupation (1792-11 to 1793-03) is missing. Evidence: prince-bishopric-of-liege L13-L14 (1792-11 to 1793-03, c=3) and L15 (1794-07, c=3). Fix: Add occupation_start/occupation_end prince-bishopric-of-liege 1792-11 to 1793-03, and give L6 month 7 once the Liège page is cited.

Thin (for a gap-filler):
- `/ledger`: The War in the Vendée and the federalist revolts of 1793 (rebel-held land), and Toulon 1793 (try https://en.wikipedia.org/wiki/War_in_the_Vend%C3%A9e)
- `/ledger`: The colonies drawn in the shapes: british-colonial-empire L56 (Tobago 1793) and L58 (Martinique 1794), and haiti L3 (1794-05) name this state as counterpart (try https://en.wikipedia.org/wiki/French_colonial_empire)
- `/ledger`: The Treaty of Basel left-bank cession: kingdom-of-prussia L23 (1795-04, loss to french-first-republic) has no mirror; the Rhineland occupation names only holy-roman-empire-minor-states (try https://en.wikipedia.org/wiki/Peace_of_Basel)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Territorial_evolution_of_France: confirmed: 'The Duchy of Savoy' (1792)
- `/ledger/4` https://en.wikipedia.org/wiki/Territorial_evolution_of_France: confirmed: 'The County of Nice and several small enclaves' (1793)
- `/ledger/5` https://en.wikipedia.org/wiki/Territorial_evolution_of_France: confirmed: 'the County of Montbéliard' (1793)
- `/ledger/9` https://en.wikipedia.org/wiki/Anglo-Corsican_Kingdom: confirmed: 'Established: 15−19 June 1794'
- `/ledger/15` https://en.wikipedia.org/wiki/Treaty_of_The_Hague_(1795): confirmed: 'signed on May 16, 1795'; 'the territories of Maastricht, Venlo, and Zeelandic Flanders'
- `/ledger/17` https://en.wikipedia.org/wiki/Austrian_Netherlands: confirmed: 'On 1 October 1795 the departments were activated and the definitive annexation started'
- `/identity/end` https://en.wikipedia.org/wiki/French_First_Republic: confirmed: 'On 3 November 1795, the Directory was established.'

## batavian-republic: thin

Area: infobox None km2 (None), Cliopatria 35837 km2, ratio None, acknowledged True. Neither the Batavian nor the Kingdom of Holland infobox gives an area (population only). The 1796 shape's 259,681 km2 includes Indonesia and is marked adjust.

Findings:
- `/ledger (new, 1795-01)` (for the author): The Republic's client status under France is missing, so french-first-republic L14 and french-directory L1 (vassal_start batavian-republic) have no mirror. Evidence: Batavian Republic page: infobox status 'Sister republic of the French First Republic and First French Empire'; it 'became a client state, the first of the sister republics'. Other dossiers record the overlord as counterpart (anglo-corsican-kingdom L1). Fix: Add vassal_start 1795-01, counterpart french-first-republic, region the whole state, confidence 2. Carry the relation on (french-directory from 1795-10; the Consulate and Empire when those dossiers exist) or close it in 1810-07.
- `/ledger/7/note` (for the author): The note does not report the page's own 1809 wording for the surrender south of the Rhine. Evidence: Kingdom of Holland page: 'In 1809, after the Walcheren Campaign, Holland had to surrender all territories south of the River Rhine to France.' The same page also has 'the treaty of March 1810'. The 1810-03 date at confidence 2 is supported. Fix: Quote both sentences in the note; no date change.
- `/ledger/5` (for the author): Prussia is inferred as counterpart and has no mirror for East Frisia; Jever's holder is unknown. Evidence: kingdom-of-prussia has no loss of East Frisia in 1806-1807 (its 1807-07 Tilsit losses: L37-L41). The Kingdom of Holland page: 'In 1807, the adjacent German regions of East Frisia and Jever were added to the kingdom' (no giver). Fix: Route the missing Prussia loss to eu-09. Find Jever's holder on the Jever or Lordship of Jever page and split the region if it differs.
- `/ledger (1796-1806)` (for the author): Other dossiers name batavian-republic as counterpart in events this ledger lacks. Evidence: british-colonial-empire L60 (1796-04 Demerara, Essequibo, Berbice), L62, L63 (1802-03 Amiens), L65, L67. sultan-of-yogyakarta L3/L4 and surakarta-sunanate L4/L5 record vassal_start/end batavian-republic 1800-1806. Fix: Either add the colonial and vassal events here, or have those dossiers name the colony dossiers (dutch-east-indies; a Dutch Guiana dossier). Orchestrator routing.

Thin (for a gap-filler):
- `/ledger`: The colonies seized by Britain from 1795 to 1806, and Amiens (1802) (try https://en.wikipedia.org/wiki/Treaty_of_Amiens)
- `/ledger/5`: East Frisia's and Jever's previous holders and the 1807 instrument (try https://en.wikipedia.org/wiki/Lordship_of_Jever)
- `/ledger/7`: The exact lands ceded in March 1810 (try https://en.wikipedia.org/wiki/Treaty_of_Paris_(1810))

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Treaty_of_The_Hague_(1795): confirmed: 16 May 1795; Maastricht, Venlo and Zeelandic Flanders
- `/ledger/2` https://en.wikipedia.org/wiki/Batavian_Republic: confirmed: 'From October 1801 onward, it was known as the Batavian Commonwealth.'
- `/ledger/3` https://en.wikipedia.org/wiki/Batavian_Republic: confirmed: 'On 10 May 1805, Schimmelpenninck was therefore inaugurated as Raadpensionaris'
- `/ledger/5` https://en.wikipedia.org/wiki/Kingdom_of_Holland: confirmed (year): 'In 1807, the adjacent German regions of East Frisia and Jever were added to the kingdom.' No giver named; confidence 2 is right.
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_Holland: confirmed with caveat: 'the treaty of March 1810' and 'Napoleon incorporated the Dutch territories between the Meuse and the Scheldt'; the surrender sentence itself opens 'In 1809, after the Walcheren Campaign'
- `/ledger/8` https://en.wikipedia.org/wiki/Kingdom_of_Holland: confirmed: 'Annexed by France: 9 July 1810'; abdication 1 July (Batavian page: 2 July 1810)

## french-directory: thin

Area: infobox None km2 (None), Cliopatria 685238 km2, ratio None, acknowledged True. The French Directory infobox has no area (confirmed).

Findings:
- `/ledger/2/region; /ledger/9/region; /ledger/10/region` (APPLIED by reviewer): The Rhineland occupation and the 1797 gain used the gazetteer region 'Rhineland', which includes the right bank. Evidence: The gazetteer region 'Rhineland' is Rheinland-Pfalz + Saarland + all of Nordrhein-Westfalen, so it paints the right bank (Westphalia, Berg, the Ruhr) French; the pages give only the left bank. French Directory page: 'France received the left bank of the Rhine as far south as Andernach'. Fix: Regions set to an intersect of Rhineland with Cliopatria's left-bank shape (French First Republic 1794 for L2 and L9, French Directory 1797 for L10), text kept.
- `/ledger/10/confidence` (APPLIED by reviewer): Confidence 3 for the whole left bank, while the page names only the left bank 'as far south as Andernach'. Evidence: French Directory page, Campo Formio sentence (quoted above). Territorial evolution: 'The German states on the left bank of the Rhine' (1797). Fix: Confidence lowered to 2.
- `/ledger (1796-1799, new)` (for the author): Occupations that neighbours record against this state are missing. They would also explain the 1796 shape's 19 Emilia and 10 Veneto cells, which keyframe_review/1 calls unexplained. Evidence: papal-states L32-L33: the Legations of Bologna, Ferrara, Ravenna and Forlì occupied by french-directory from 1796 to 1797-02. republic-of-venice L159-L160: 'Venetian territory up to the Adige' occupied from 1796 to 1797-05. republic-of-lucca L9: occupation from 1799-01 (c=3). principality-of-liechtenstein L1-L2: 'France invaded the country on 6 March 1799', liberated 'by 14 May' (c=3). holy-roman-empire-minor-states L103-L104: contest in Swabia and Franconia, 1796. Fix: Add the occupation_start/occupation_end pairs with those counterparts and the 1796 contest zone, citing the neighbours' pages (Papal States, Republic of Venice, Republic of Lucca, Liechtenstein, Rhine campaign of 1796).
- `/keyframe_review/1` (for the author): Verdict ok, but the note says the shape's 17 Liguria cells are unexplained. Genoa was a neutral republic until June 1797, and republic-of-genoa records no 1796 occupation. Evidence: The KF1 note itself: 'the page does not mention Emilia, Liguria or the Veneto'. Fix: Mark it adjust with {'minus': [{'cliopatria': 'French Directory', 'year': 1796}, {'admin1': 'Liguria', 'country': 'Italy'}]}, or add 'unverified: page budget' to the note.
- `/ledger/4` (for the author): The Lombardy occupation names habsburg-monarchy, but state-of-milan has its own dossier and records the 1796 loss to french-directory. Evidence: state-of-milan L8: 1796 loss to french-directory, c=3; L9: dissolve, successor cisalpine-republic. habsburg-monarchy L110 also claims a 1796 loss of Lombardy to french-directory (c=1). Fix: Use counterpart state-of-milan for L4 and L6, and route the double claim on Lombardy (state-of-milan versus habsburg-monarchy) to eu-09/eu-13.
- `/ledger/20` (for the author): The end of the Piedmont occupation has no month, though the counterpart dates it. Evidence: kingdom-of-sardinia L18: occupation_end french-directory 1799-06. Fix: Add month 6 if the Italian campaigns page or the Suvorov page dates the fall of Turin (26 May 1799 to June).

Thin (for a gap-filler):
- `/ledger`: Naples in 1799 as an occupation, and the months when the Roman and Parthenopean republics collapsed (try https://en.wikipedia.org/wiki/Parthenopean_Republic)
- `/keyframe_review/3`: The 10 added Savoy cells and the Swiss cells of the 1799 shape (try https://en.wikipedia.org/wiki/Helvetic_Republic)
- `/ledger/13`: The month of the capture of Malta (June 1798) (try https://en.wikipedia.org/wiki/French_occupation_of_Malta)

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/Anglo-Corsican_Kingdom: confirmed: 'British evacuation: 11 October 1796'; French 'reconquered Bastia' on 19 October 1796
- `/ledger/10` https://en.wikipedia.org/wiki/French_Directory: confirmed date (17 October 1797); region wider than the page ('as far south as Andernach'), fixed
- `/ledger/11` https://en.wikipedia.org/wiki/French_Directory: confirmed: 'the Ionian Islands that had belonged to the Republic of Venice', Campo Formio 17 October 1797
- `/ledger/12` https://en.wikipedia.org/wiki/Territorial_evolution_of_France: confirmed: 'the Republic of Mulhouse' (1798)
- `/ledger/13` https://en.wikipedia.org/wiki/French_Directory: confirmed (year only): 'The French fleet stopped briefly at Malta, capturing the island'; sailed 19 May 1798
- `/ledger/16` https://en.wikipedia.org/wiki/French_Directory: confirmed: Alexandria captured 'on 2 July'
- `/ledger/17` https://en.wikipedia.org/wiki/French_Directory: confirmed: 'On 26 August 1798, Geneva was detached from the new republic and made part of France.'
- `/ledger/19` https://en.wikipedia.org/wiki/French_Directory: confirmed: '6 December 1798' French soldiers forced Charles Emmanuel IV out of Piedmont

## cisalpine-republic: thin

Area: infobox 42500 km2 (1797), Cliopatria 41872 km2, ratio 0.985, acknowledged True. 

Findings:
- `/ledger/6/type; /ledger/7/type` (APPLIED by reviewer): The Austro-Russian occupation of 1799-1800 was recorded as a loss and a gain of the whole state, against the dossier's own KF1 note ('an occupation, not an annexation') and the Habsburg mirror. Evidence: Cisalpine page infobox: 'Occupied by Austria: 27 April 1799', 'Restored by France: 2 June 1800'. habsburg-monarchy L112/L114 record occupation_start/occupation_end with counterpart cisalpine-republic. Fix: Types changed to occupation_start and occupation_end (counterpart habsburg-monarchy).
- `/ledger/2` (for the author): Modena and Reggio are gained in 1797-06 from duchy-of-modena-and-reggio, but the page puts them in Transpadania on 19 May 1797, so they arrive with the found event (L1, whose text already says 'with the former Duchy of Modena'). The duchy had not held them since 1796. Evidence: Cisalpine page: 'on 19 May 1797, Napoleon moved the former Duchy of Modena into Transpadania'. The L2 note itself says so. The cispadane-republic predecessor's land also lists Modena and Reggio Emilia, which the page sends to Transpadania. Fix: Delete L2, or make it part of L1. Drop Modena and Reggio from the cispadane predecessor's land. holy-roman-empire-minor-states L105 (1797 loss of Modena, Reggio, Parma and Mantua to cisalpine-republic, c=1) then needs re-routing (eu-09).
- `/ledger/0` (for the author): The Romagna is gained from papal-states, but papal-states records its loss to cispadane-republic. Evidence: papal-states L34: 1797-02 loss of 'Romagna, Ferrara and Bologna, the Papal Legations' to cispadane-republic, c=3. The Cisalpine page does not name the Romagna (Rubicone department only). Fix: Fold the Romagna into the L3 merge with cispadane-republic (1797-07) and delete L0, or keep L0 at confidence 1 with counterpart cispadane-republic.
- `/ledger/5` (for the author): Mantua is gained in 1798 from habsburg-monarchy, but the Habsburg ledger lost Lombardy, Mantua included, to french-directory in 1796 and records no loss in 1797-1798. Evidence: Cisalpine page: Mincio (Mantua) added '7 Prairial (26 May)' 1798 (confirmed). habsburg-monarchy L110: 1796 loss to french-directory 'Lombardy: Mantua, Cremona, Milan, Varese, Como'. Fix: Counterpart french-directory (the occupier, which handed Mantua over), or note the Campo Formio cession (17 October 1797).
- `/ledger (new, 1797-06)` (for the author): The client relation to France is missing, so french-directory L7 (vassal_start 1797-06) and L22 (vassal_end 1799-04) have no mirror. Evidence: Cisalpine page: established by Napoleon as a sister republic, 29 June 1797. Fix: Add vassal_start 1797-06 with counterpart french-directory and vassal_end 1799-04; after 1800, the Consulate when that dossier exists.
- `/ledger/8` (for the author): Novara is dated 1800-10 here (confirmed), but kingdom-of-sardinia dates the loss 1802-09, to italian-republic. Evidence: Cisalpine page: Napoleon ordered Novara annexed on '21 Vendémiaire (13 October)' year IX. kingdom-of-sardinia L24: 1802-09 loss to italian-republic, c=2. Fix: No change here. Route to eu-13 so Sardinia's L24 reads 1800-10 with counterpart cisalpine-republic (and its 1800 Piedmont occupation by french-consulate).
- `/ledger (new)` (for the author): Gains of Venetian land are missing: Bergamo, Brescia, Crema, and Verona west of the Adige with the Polesine (all in the 1797 shape). So is the Lunéville Adige frontier. Evidence: Cisalpine page: Brescia (Mella) and Bergamo (Serio) are department seats; after 'the Treaty of Lunéville' of '9 February 1801' the frontier moved to the River Adige 'without the exceptions agreed in Campo Formio'. republic-of-venice lists cisalpine-republic among its successors. Fix: Add gains from republic-of-venice (or the provisional republics of Bergamo and Brescia) in 1797, and a 1801-02 gain at the Adige.

Thin (for a gap-filler):
- `/ledger/0`: The date of the Treaty of Tolentino and the route of the Romagna (try https://en.wikipedia.org/wiki/Treaty_of_Tolentino)
- `/ledger`: Bergamo, Brescia and Crema leaving Venice in 1797 (try https://en.wikipedia.org/wiki/Republic_of_Bergamo)
- `/keyframe_review/0`: The northern Marche (Pesaro e Urbino) cells, which papal-states keeps to 1808 (L37) (try https://en.wikipedia.org/wiki/Treaty_of_Campo_Formio)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Cisalpine_Republic: confirmed: 'Established: 29 June 1797'
- `/ledger/2` https://en.wikipedia.org/wiki/Cisalpine_Republic: mis-read: on 19 May 1797 the former Duchy of Modena was moved into Transpadania; it is not a June gain from the duchy
- `/ledger/4` https://en.wikipedia.org/wiki/Cisalpine_Republic: confirmed: union of the Valtellina announced '1 Brumaire (22 October)' 1797
- `/ledger/5` https://en.wikipedia.org/wiki/Cisalpine_Republic: confirmed: Mincio (Mantua) added '7 Prairial (26 May)' 1798
- `/ledger/6` https://en.wikipedia.org/wiki/Cisalpine_Republic: confirmed: 'Occupied by Austria: 27 April 1799' (type fixed)
- `/ledger/8` https://en.wikipedia.org/wiki/Cisalpine_Republic: confirmed: Novara annexed '21 Vendémiaire (13 October)', year IX (1800)

## grand-duchy-of-tuscany: thin

Area: infobox 21710 km2 (1852), Cliopatria 24632 km2, ratio 1.13, acknowledged True. No Cliopatria Tuscany shape is alive in 1852; the 1848 shape (24,632) is carried to 1859 by the new keyframe. The five 1797-1847 shapes (938-1,032 km2) are marked wrong.

Findings:
- `/ledger/8 and /ledger/9 (were 9 and 8)` (APPLIED by reviewer): The 1849 restoration (gain, no month, confidence 1) came before the February 1849 flight it reverses. Evidence: Leopold II page: 'On the 18th of February 1849, a republic was proclaimed and on that same day Leopold sailed for Gaeta'; 'In April, the municipal council usurped the powers of the assembly and invited him to return'; Austrians entered Florence on 25 May; 'On the 28th of July, Leopold himself returned.' Fix: Gain given month 4 and confidence 2, moved after the 1849-02 loss, source changed to the Leopold II page (added to sources).
- `/keyframe_review/3/correction; /keyframe_review/4/correction; /keyframe_review/2` (for the author): The wrong-verdict corrections for 1803-1805 and 1806-1813 give the Kingdom of Etruria's shape, while the ledger has the grand duchy holding nothing from 1801-03 (L1) to 1814-05 (L2). Read as 'the shape to use', they would draw Tuscany on top of kingdom-of-etruria. Evidence: Schema: 'wrong: the shape should not be used for these years; correction gives the shape to use instead, or the years it belongs to'. Correction texts: 'belongs to the Kingdom of Etruria', 'Etruria to 1807, then annexed to France'. Fix: State plainly that this dossier draws nothing in these years: the correction text names the years and the owner dossiers, and the region is the Cliopatria Grand Duchy shape unchanged rather than another state's shape. Likewise for 1801-1802 in KF2. Do the same for certainty /certainty/1 (1801-1813), which covers years the state did not exist.
- `/ledger/4` (for the author): The Presidi are gained in 1815 from state-of-the-presidi, whose dossier ended in 1801-09 (to kingdom-of-etruria). Evidence: state-of-the-presidi L3/L4: 1801-09 loss and dissolve to kingdom-of-etruria. kingdom-of-etruria L1/L2: 1807-12 to first-french-empire. Fix: Counterpart first-french-empire (or nobody, with a note on the 1814 interregnum).
- `/ledger/3` (for the author): Piombino's counterpart principality-of-lucca-and-piombino ended in 1814. Evidence: Piombino page: timeline 'Luigi I Boncompagni-Ludovisi' 1814-15 after French Lucca; 'Granted to Tuscany: 1815'. Fix: Note the 1814-15 restoration; keep the counterpart or use nobody.
- `/identity/start` (for the author): The 1737 start splits one state at a dynasty change (Medici to Lorraine), against the rule 'one dossier per state, not per dynasty'. The Wikipedia Grand Duchy (Q154849) runs 1569-1859. Evidence: The Grand Duchy page infobox: 'End of Medici rule: 9 July 1737' is a dynasty event. The republic-of-florence dossier renames to the Grand Duchy in 1569-08 and dissolves in 1737-07 to this dossier, so the two agree and the map is consistent. Fix: Orchestrator decision. Either keep the cut (both dossiers agree, the colour changes in 1737), or merge: republic-of-florence continues to 1859 with a 1737 rename, or this dossier takes 1569-1859.
- `/ledger (new)` (for the author): Occupations of Tuscany that neighbours record are missing. Evidence: kingdom-of-naples-napoleonic L7/L11: occupation_start grand-duchy-of-tuscany 1815-04 (Florence, c=2) and occupation_end 1815-05. kingdom-of-great-britain L12: 1796 occupation of Portoferraio on Elba ('owner page silent'; Portoferraio was Tuscan). The author's gaps list the French occupations of 1796 (Livorno) and of March to July 1799. Fix: Add the occupation pairs with counterparts kingdom-of-naples-napoleonic, kingdom-of-great-britain and french-directory once a page dates them.

Thin (for a gap-filler):
- `/ledger`: The French occupation of Livorno in 1796 and of Tuscany from March to July 1799 (try https://en.wikipedia.org/wiki/Ferdinand_III,_Grand_Duke_of_Tuscany)
- `/ledger`: Elba: Portoferraio was Tuscan before 1801; the whole island went to Tuscany in 1815 (try https://en.wikipedia.org/wiki/Elba)
- `/ledger`: 1737-1796 (Lorraine regency, no ruler strip) and the 1859 provisional government (try https://en.wikipedia.org/wiki/Francis_I,_Holy_Roman_Emperor)
- `/ledger/5; /ledger/6`: A page giving the 1844 Treaty of Florence and the 1847 cession dates (try https://en.wikipedia.org/wiki/Treaty_of_Florence_(1844))

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Grand_Duchy_of_Tuscany: confirmed: 'Abolished during Napoleonic Wars: 21 March 1801'
- `/ledger/2` https://en.wikipedia.org/wiki/Grand_Duchy_of_Tuscany: confirmed: 'Re-establishment: 30 May 1814'
- `/ledger/3` https://en.wikipedia.org/wiki/Principality_of_Piombino: confirmed (year): 'Granted to Tuscany: 1815'; month from the Lucca page's 'Congress of Vienna: 9 June 1815'
- `/ledger/5; /ledger/6` https://en.wikipedia.org/wiki/Grand_Duchy_of_Tuscany: confirmed (year from context): 'Tuscany in turn ceded its Lunigiana domains either to Modena (Vicariate of Fivizzano) or to Parma (Vicariate of Pontremoli ...)'
- `/ledger/7` https://en.wikipedia.org/wiki/Duchy_of_Lucca: confirmed: 'Reversion to Tuscany: 17 December 1847'
- `/ledger/8 (was 9)` https://en.wikipedia.org/wiki/Grand_Duchy_of_Tuscany: confirmed: 'In February 1849, Leopold II had to abandon Tuscany to republicans'
- `/ledger/9 (was 8)` https://en.wikipedia.org/wiki/Leopold_II,_Grand_Duke_of_Tuscany: mis-ordered (fixed): restoration in April 1849, return 28 July 1849
- `/ledger/11` https://en.wikipedia.org/wiki/Grand_Duchy_of_Tuscany: confirmed: 'Merged to form the United Provinces of Central Italy: 8 December 1859'

## ligurian-republic: thin

Area: infobox None km2 (None), Cliopatria 2339 km2, ratio None, acknowledged True. No infobox area (confirmed). The correction to the Liguria region (6,070 km2 in the gazetteer) is 2.6 times the 1797 shape; that is acknowledged in every keyframe note and rests on 'most of the Ligurian region'.

Findings:
- `/ledger/5` (for the author): The 1814-07 dissolve hands the land to kingdom-of-sardinia, but the page dates the Sardinian annexation to 3 January 1815; the five months between are unaccounted. Evidence: Ligurian Republic page: 'the republic was briefly restored between 28 April and 28 July' (1814); 'Following the Congress of Vienna, it was awarded to Piedmont-Sardinia and annexed on 3 January 1815.' kingdom-of-sardinia L27: 1814 gain of 'Liguria, taken from the Republic of Genoa', counterpart republic-of-genoa. Fix: Quote the 3 January 1815 annexation in the dissolve note and the successor land text. Say who held Genoa from August to December 1814 if a page gives it (the British under Bentinck; the page is silent). Route to eu-13 so Sardinia's L27 names ligurian-republic and reads 1815-01.
- `/ledger/1; /ledger/2` (for the author): The 1800 events are typed as a contest, but the page says 'occupied'. Evidence: Ligurian Republic page: 'The Republic was briefly occupied by Austrian forces in 1800'. habsburg-monarchy has no 1800 event naming ligurian-republic. Fix: Use occupation_start/occupation_end with counterpart habsburg-monarchy (the siege of Genoa can stay as a contest before them). Route the mirror to eu-09.
- `/ledger (new, 1797-06)` (for the author): The client relation to France is missing, so french-directory L8 (vassal_start ligurian-republic 1797-06) has no mirror. Evidence: Ligurian page: the republic was proclaimed 'under the watchful care of Republican France' (quoted in the dossier's predecessor note). Fix: Add vassal_start 1797-06 with counterpart french-directory, carried to 1805-06.
- `/certainty/1` (for the author): Certainty covers 1806-1813, when the republic did not exist (annexed 4 June 1805, restored 28 April 1814). Evidence: Ligurian page infobox: 'Annexed by France: 4 June 1805'. Fix: State in the note that the span is a gap (no land), or end certainty at the annexation and resume in 1814.

Thin (for a gap-filler):
- `/keyframe_review/3`: What extended the 1803 shape west to 7.47E (Oneglia and Loano, the Savoyard enclaves, or the western Riviera) (try https://en.wikipedia.org/wiki/Oneglia)
- `/identity/predecessors`: The Republic of Noli (infobox predecessor) and the Imperial fiefs (try https://en.wikipedia.org/wiki/Republic_of_Noli)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Ligurian_Republic: confirmed: 'Napoleon announced the founding of the Ligurian Republic on 6 June 1797'; the lead gives 14 June 1797
- `/ledger/3` https://en.wikipedia.org/wiki/Ligurian_Republic: confirmed: 'Annexed by France: 4 June 1805'
- `/ledger/4` https://en.wikipedia.org/wiki/Ligurian_Republic: confirmed: 'briefly restored between 28 April and 28 July' (1814)
- `/ledger/5` https://en.wikipedia.org/wiki/Ligurian_Republic: partly confirmed: the end of the restoration on 28 July is on the page; the land goes to Sardinia only on 3 January 1815
- `/keyframe_review/0` https://en.wikipedia.org/wiki/Ligurian_Republic: confirmed: 'which covered most of the Ligurian region'; 'the small Imperial fiefs owned by the House of Savoy inside its territory'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| french-first-republic 1792 found kingdom-of-france | kingdom-of-france 1792 dissolve | matched | 1792-09 both |
| french-first-republic 1792 gain kingdom-of-sardinia | kingdom-of-sardinia 1792 loss | matched | Savoy |
| french-first-republic 1793 gain kingdom-of-sardinia | kingdom-of-sardinia 1792 occupation_start | mismatch | Nice: FFR annexes in 1793 (Territorial evolution page); Sardinia L11 occupation from 1792-09, L14 cession to french-directory 1796-05 |
| french-first-republic 1793 gain duchy-of-wurttemberg | duchy-of-wurttemberg 1793 loss | matched | Montbéliard, 1793-11 on the Württemberg side |
| french-first-republic 1794 occupation_start prince-bishopric-of-liege | prince-bishopric-of-liege 1794 occupation_start | matched | Liège gives 1794-07, c=3; it also records a 1792-11 to 1793-03 occupation that FFR lacks |
| french-first-republic 1795 gain prince-bishopric-of-liege | prince-bishopric-of-liege 1795 dissolve | matched |  |
| french-first-republic 1794 occupation_start holy-roman-empire-minor-states | holy-roman-empire-minor-states 1794 loss | mismatch | Type: HRE minor states L102 records a 1794 loss (79 left-bank cells), FFR an occupation; the electorates (Cologne, Trier, Mainz, Bavaria, Jülich-Berg) record occupations to 1801-02 |
| french-first-republic 1794 loss anglo-corsican-kingdom | anglo-corsican-kingdom 1794 found | matched | 1794-06 |
| french-first-republic 1794 occupation_start habsburg-netherlands | habsburg-netherlands 1794 occupation_start | matched | 1794-06 |
| french-first-republic 1795 gain habsburg-netherlands | habsburg-netherlands 1795 dissolve | matched | 1795-10 |
| french-first-republic 1795 vassal_start batavian-republic | - | missing | batavian-republic has no vassal_start |
| french-first-republic 1795 gain batavian-republic | batavian-republic 1795 loss | matched | 1795-05 Treaty of The Hague; dutch-republic L44 has Maastricht lost to FFR in 1794-11 (conquest) as well |
| dutch-republic 1794 loss french-first-republic | - | missing | Generality lands (c=1) and Maastricht 1794-11 (c=3); FFR has only the 1795-05 cession from batavian-republic |
| kingdom-of-prussia 1795 loss french-first-republic | - | missing | Treaty of Basel left-bank lands; FFR names only holy-roman-empire-minor-states |
| principality-of-monaco 1793 loss french-first-republic | - | missing | Monaco annexed 1793, c=3 |
| kingdom-of-spain 1794 occupation_start french-first-republic | - | missing | Gipuzkoa 1794-08 and Figueres/Roses 1794-11 to 1795-07 |
| british-colonial-empire 1793 gain french-first-republic | - | missing | Tobago 1793, Martinique 1794, the 1802 return; colonies are not in FFR's ledger (gap) |
| haiti 1794 gain french-first-republic | - | missing | 1794-05 |
| french-first-republic 1795 dissolve french-directory | french-directory 1795 found | mismatch | FFR ends 1795-11, FD starts 1795-10: about a week of overlap; the pages differ (3 November against 26 October) |
| batavian-republic 1795 found dutch-republic | dutch-republic 1795 dissolve | matched | 1795-01 |
| batavian-republic 1807 gain kingdom-of-prussia | - | missing | Prussia has no East Frisia loss in 1806-1807 (eu-09) |
| batavian-republic 1810 loss first-french-empire | - | exception | first-french-empire is owned by an eu-20 part that has not run yet |
| batavian-republic 1810 dissolve first-french-empire | - | exception | as above |
| sultan-of-yogyakarta 1800 vassal_start batavian-republic | - | missing | also surakarta-sunanate 1800-1806; decide overlord: batavian-republic or dutch-east-indies |
| british-colonial-empire 1796 gain batavian-republic | - | missing | Demerara, Essequibo, Berbice 1796-04; Guiana 1799; Amiens 1802-03; 1803 |
| french-directory 1795 found french-first-republic | french-first-republic 1795 dissolve | matched | overlap noted above |
| french-directory 1795 vassal_start batavian-republic | - | missing | batavian-republic has no vassal events |
| french-directory 1796 occupation_start kingdom-of-sardinia | kingdom-of-sardinia 1796 occupation_start | matched | 1796-04 fortresses; ended 1798-12 both sides |
| french-directory 1796 occupation_start habsburg-monarchy | habsburg-monarchy 1796 loss | mismatch | Lombardy: Habsburg L110 records a loss (c=1); state-of-milan L8 also records a 1796 loss to french-directory (c=3) and dissolves to cisalpine-republic |
| french-directory 1796 gain anglo-corsican-kingdom | anglo-corsican-kingdom 1796 dissolve | matched | 1796-10 |
| french-directory 1797 vassal_start cisalpine-republic | - | missing | cisalpine-republic has no vassal events |
| french-directory 1797 vassal_start ligurian-republic | - | missing | ligurian-republic has no vassal events |
| french-directory 1797 gain holy-roman-empire-minor-states | holy-roman-empire-minor-states 1794 loss | mismatch | The HRE side records the left bank lost in 1794 and nothing in 1797; the electorates end their occupations in 1801-02 (Lunéville) |
| french-directory 1797 gain republic-of-venice | republic-of-venice 1797 dissolve | matched | Ionian Islands: Venice dissolves 1797-05 with french-directory among its successors; FD dates the gain to Campo Formio, 1797-10 |
| republic-of-venice 1796 occupation_start french-directory | - | missing | Venetian territory up to the Adige, 1796 to 1797-05 |
| papal-states 1796 occupation_start french-directory | - | missing | Legations, 1796 to 1797-02 |
| holy-roman-empire-minor-states 1796 contest_start french-directory | - | missing | Swabia and Franconia, 1796 |
| republic-of-lucca 1799 occupation_start french-directory | - | missing | 1799-01, c=3 |
| principality-of-liechtenstein 1799 occupation_start french-directory | - | missing | 1799-03 to 1799-05, c=3 |
| duchy-of-arenberg 1798 occupation_start french-directory | - | exception | covered by FD's left-bank occupation in aggregate |
| french-directory 1798 gain republic-of-mulhouse | - | exception | no dossier; listed in counterparts_needing_dossiers |
| french-directory 1798 gain order-of-saint-john | - | exception | no dossier; listed |
| french-directory 1798 vassal_start revolutionary-roman-republic | - | exception | owned by an eu-20 part that has not run yet |
| french-directory 1798 vassal_start helvetic-republic | - | exception | owned by an eu-20 part that has not run yet |
| french-directory 1798 gain mamluk-beys-of-egypt | mamluk-beys-of-egypt 1798 loss | matched | 1798-07; ottoman-empire L155 also records a 1798 loss of Egypt to french-directory |
| french-directory 1798 gain republic-of-geneva | - | exception | no dossier; listed (swiss-confederation L41 ends its Geneva relation 1798-04) |
| french-directory 1798 occupation_start kingdom-of-sardinia | kingdom-of-sardinia 1798 occupation_start | matched | 1798-12; end 1799 (Sardinia 1799-06) |
| french-directory 1799 vassal_start parthenopean-republic | - | exception | no dossier; listed |
| cisalpine-republic 1797 found transpadane-republic | - | exception | no dossier; listed |
| cisalpine-republic 1797 gain papal-states | papal-states 1797 loss | mismatch | Romagna: papal-states L34 gives it to cispadane-republic in 1797-02 |
| cisalpine-republic 1797 gain duchy-of-modena-and-reggio | holy-roman-empire-minor-states 1797 loss | mismatch | Modena/Reggio: the page puts them in Transpadania on 19 May 1797; HRE L105 claims a 1797 loss to cisalpine-republic (c=1); duchy-of-modena-and-reggio not yet written |
| cisalpine-republic 1797 merge cispadane-republic | - | exception | owned by an eu-20 part that has not run yet |
| cisalpine-republic 1797 gain three-leagues | swiss-confederation 1797 vassal_end | exception | three-leagues has no dossier (listed); the Swiss side ends its relation to the Valtellina in 1797-10, consistent |
| cisalpine-republic 1798 gain habsburg-monarchy | - | mismatch | Mantua: Habsburg L110 lost it to french-directory in 1796; no 1798 loss |
| cisalpine-republic 1799 occupation_start habsburg-monarchy | habsburg-monarchy 1799 occupation_start | matched | after the reviewer's type fix; 1799-04 |
| cisalpine-republic 1800 occupation_end habsburg-monarchy | habsburg-monarchy 1800 occupation_end | matched | 1800-06 against 1800-05 |
| cisalpine-republic 1800 gain kingdom-of-sardinia | kingdom-of-sardinia 1802 loss | mismatch | Novara: the Cisalpine page has 13 October 1800; Sardinia L24 has 1802-09 to italian-republic |
| cisalpine-republic 1802 dissolve italian-republic | italian-republic 1802 found | matched | 1802-01 |
| state-of-milan 1796 dissolve cisalpine-republic | - | mismatch | state-of-milan dissolves to cisalpine-republic in 1796, a year before it exists (its issue; route eu-13) |
| grand-duchy-of-tuscany 1737 found republic-of-florence | republic-of-florence 1737 dissolve | matched | 1737-07; dynasty split, see fixes |
| grand-duchy-of-tuscany 1801 loss kingdom-of-etruria | kingdom-of-etruria 1801 found | matched | 1801-03 |
| grand-duchy-of-tuscany 1814 gain first-french-empire | - | exception | first-french-empire not yet written (eu-20) |
| grand-duchy-of-tuscany 1815 gain principality-of-lucca-and-piombino | - | exception | no dossier; listed |
| grand-duchy-of-tuscany 1815 gain state-of-the-presidi | state-of-the-presidi 1801 loss | mismatch | the Presidi dossier ends in 1801-09 (to Etruria); in 1815 the land came from France's collapse |
| grand-duchy-of-tuscany 1847 loss duchy-of-modena-and-reggio | - | exception | owned by an eu-20 part that has not run yet |
| grand-duchy-of-tuscany 1847 loss duchy-of-parma-and-piacenza | - | exception | owned by an eu-20 part that has not run yet |
| grand-duchy-of-tuscany 1847 gain duchy-of-lucca | - | exception | no dossier; listed |
| grand-duchy-of-tuscany 1859 dissolve united-provinces-of-central-italy | - | exception | no dossier; listed |
| kingdom-of-naples-napoleonic 1815 occupation_start grand-duchy-of-tuscany | - | missing | Florence 1815-04 to 1815-05 |
| ligurian-republic 1797 found republic-of-genoa | republic-of-genoa 1797 dissolve | matched | 1797-06 |
| ligurian-republic 1800 contest_start habsburg-monarchy | - | missing | habsburg-monarchy has no 1800 Genoa event; the page says 'occupied' |
| ligurian-republic 1805 loss first-french-empire | - | exception | first-french-empire not yet written |
| ligurian-republic 1814 gain first-french-empire | - | exception | first-french-empire not yet written |
| ligurian-republic 1814 dissolve kingdom-of-sardinia | kingdom-of-sardinia 1814 gain | mismatch | Sardinia L27 names republic-of-genoa; the page has the annexation on 3 January 1815 |

## Gazetteer names needed

- Montbéliard (place): french-first-republic
- Venlo (place): french-first-republic; batavian-republic
- Piombino (place): grand-duchy-of-tuscany
- Orbetello (place): grand-duchy-of-tuscany
- Fivizzano (place): grand-duchy-of-tuscany
- Pontremoli (place): grand-duchy-of-tuscany
- Rhineland (left bank) (region): french-first-republic; french-directory (now an intersect); the gazetteer's 'Rhineland' includes all of Nordrhein-Westfalen and the right bank, so a 'Left bank of the Rhine' region would help every Revolutionary-era dossier

## Problems and routing

- Reviewer edits applied on the mount and re-validated (0 errors): cisalpine-republic L6/L7 types; grand-duchy-of-tuscany 1849 gain (month, order, source added); french-first-republic L8 and french-directory L2/L9/L10 regions narrowed to the left bank; french-directory L10 confidence 3 to 2. Backups are in /tmp/claude-0/work/review-eu-20-a/bak/.
- Gazetteer: the region 'Rhineland' = Rheinland-Pfalz + Saarland + all of Nordrhein-Westfalen. Any dossier that uses it for the French left bank (1794-1814) paints Westphalia and Berg French. Worth a gazetteer 'Left bank of the Rhine' region and a sweep of the french-consulate and first-french-empire dossiers when they are written.
- The satellite dossiers (batavian, cisalpine, ligurian) carry no vassal_start toward France, while french-first-republic and french-directory do. The convention in other dossiers (anglo-corsican-kingdom) is that the client records the overlord as counterpart; the orchestrator may want one rule for all sister republics.
- Neighbour-side defects found while cross-checking (not this batch's files): kingdom-of-sardinia L13 names french-first-republic in 1796-05 and L24 dates Novara 1802; L27 names republic-of-genoa for Liguria in 1814. state-of-milan dissolves to cisalpine-republic in 1796. Both state-of-milan and habsburg-monarchy claim the 1796 loss of Lombardy. electorate-of-trier L18 and free-imperial-city-of-cologne L4 name french-first-republic for 1801 and 1796. kingdom-of-prussia lacks the 1807 East Frisia loss.
- WebFetch returns model summaries, not raw text; the quotes in this report are the summaries' quotations. All pages loaded.
