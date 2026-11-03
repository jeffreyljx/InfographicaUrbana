# Review of batch eu-20-d (Europe 1789-1914, part d), 2026-10-31

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator adjustments (spot checks weighted to confidence 3 and large moves; thin judged against the page budget; small verified fixes applied in place and re-validated). Validator: all five dossiers valid, 0 errors before and after the reviewer edits.

| slug | verdict | why |
| --- | --- | --- |
| kingdom-of-hanover | thin | spot checks hold; 2 small fixes applied (Hildesheim, Denmark slug); Prussian 1805-1806 episode and 1815 c1 counterparts are page-budget gaps; 5 minor fixes left for the author |
| first-french-colonial-empire | thin | 1805 occupation date not on page (lowered to c1, applied); capture years, Guiana occupier and Santo Domingo disagree with neighbours |
| first-french-empire | fail | 1813-1814 collapse only partly explained (~100,000 km2 without loss events), Lower Saxony drawn for Oldenburg at c3, many neighbour transfers and occupations with no mirror, events after the dissolve |
| austrian-empire | fail | 1814 keyframe holds +157,000 km2 that the ledger only gains in June 1815 (neighbours date 1814); 1849 Novara campaign and occupation missing; 2 counterpart fixes applied |
| duchy-of-anhalt | thin | all four spot checks confirmed; unexplained Cliopatria steps (1814-1819, 1864-1865, 1866-1867) are page-budget gaps |

## kingdom-of-hanover: thin

Area: infobox None (None), Cliopatria 38488, ratio None, acknowledged True. The Kingdom page has no area; the author says so.

Findings:

- `/ledger/3/region` [applied by reviewer] The 1810 loss to Westphalia included Hildesheim, which was not Hanoverian in 1810. Evidence: Kingdom of Westphalia page lists Hildesheim among the 'territories ceded by the Kingdom of Prussia in the Peace of Tilsit' (1807); Hanover gains it only in 1815 (/ledger/10). Fix: Region reduced to {place: Hanover, km: 40} with the original text; reviewer note appended.
- `/ledger/11/counterpart` [applied by reviewer] Counterpart denmark-norway ends January 1814; the 1815 Lauenburg cession goes to the post-Kiel kingdom. Evidence: denmark-norway dossier end 1814/1; kingdom-of-denmark-1814-1940 /ledger/1 gains Lauenburg in 1815 (c3). Congress page: Hanover 'gave up the Duchy of Lauenburg to the Kingdom of Denmark'. Fix: Counterpart set to kingdom-of-denmark-1814-1940.
- `/ledger/2/region and /keyframe_review/2/correction` [for the author] Goslar is drawn as a Hanoverian loss of 1807, but no page makes it Hanoverian. Evidence: Kingdom of Westphalia page lists Goslar among the 1807 units without a previous holder (it names Hanover only as a source territory); the Kingdom of Hanover page does not list Goslar among Hanoverian lands. Author's note: 'Land is my reading of the unit list'. Fix: Drop Goslar from the 1807 loss and the 1807 keyframe correction, or cite a page that makes it Hanoverian in 1803-1807.
- `/ledger/4/counterpart` [for the author] The December 1810 transfer of the Nord and Niederelbe departments (Bremen-Verden, Lüneburg) is recorded as Hanover to France, while the Westphalia page and dossier make them Westphalian departments ceded to France. Evidence: Westphalia page: 'In December 1810, the short-lived coastal and northern départements Nord and Niederelbe were ceded to the French Empire'; kingdom-of-westphalia /ledger/7 (1810/12 loss to first-french-empire, c3) has no matching gain from Hanover; first-french-empire has neither side. Fix: Make /ledger/4 a 1810 loss to kingdom-of-westphalia alongside /ledger/3 (and ask eu-20 to add the gain to Westphalia and the December 1810 gain to first-french-empire), or keep it and have Westphalia drop its loss; the three dossiers must agree.
- `/ledger/5/counterpart` [for the author] The occupation that ends in December 1810 is credited to french-consulate, which ended on 18 May 1804. Evidence: first-french-empire starts 1804/5 with a found event from french-consulate; the Artlenburg occupation began under the Consulate in June 1803. Fix: Close the french-consulate occupation at 1804/5 and open an occupation_start by first-french-empire at 1804/5, ending in 1810 (and give first-french-empire the mirror events).
- `/ledger/6/region` [for the author] The 1813 regain from Westphalia uses the whole 1803 outline, which also contains Bremen-Verden and Lüneburg regained from France in /ledger/7. Evidence: Westphalia held Göttingen, Grubenhagen, Osnabrück (1807) and the Aller department (1810), not the northern departments after December 1810. Fix: Region: minus[Kingdom of Hanover 1803, union[Bremen-Verden, Lüneburg]].
- `/ledger (1827)` [for the author] No event for the Bremerhaven cession. Evidence: free-city-of-bremen /ledger/3: 1827 gain from kingdom-of-hanover, 'a strip of land at the mouth of the Weser' (c3). Fix: Add a small 1827 loss to free-city-of-bremen, sourced from the page the Bremen dossier cites.

Gaps for a gap-filler:

- `/ledger (1805-1806)` Prussian occupation (1805) and annexation (February 1806) of Hanover: kingdom-of-prussia /ledger/28, 30, 31 (c2) have no mirror here; notes flag it. Try: https://en.wikipedia.org/wiki/Electorate_of_Hanover
- `/ledger/10` Previous holders and date of Hildesheim, Lingen, northern Münster and Bentheim (c1; Bentheim was not Prussian). Try: https://en.wikipedia.org/wiki/County_of_Bentheim
- `/ledger/0` found at confidence 1 (hand-over year from Cliopatria). Try: https://en.wikipedia.org/wiki/Electorate_of_Hanover
- `/keyframe_review/7` 1853 Jade Treaty / Wangerooge (-174 km2 in 1864) unexplained. Try: https://en.wikipedia.org/wiki/Wilhelmshaven

Spot checks:

- `/ledger/3` Kingdom_of_Westphalia: not on page (Hildesheim was a Prussian cession of 1807); Aller 1810-1813 confirmed; fixed
- `/ledger/6` Kingdom_of_Westphalia: confirmed (26 October 1813; 'status quo of 1806 was restored')
- `/ledger/9` Congress_of_Vienna: confirmed ('formerly Prussian East Frisia'; Final Act 9 June 1815)
- `/ledger/11` Congress_of_Vienna: confirmed ('gave up the Duchy of Lauenburg to the Kingdom of Denmark')
- `/ledger/12` Austro-Prussian_War: confirmed (invaded 15 June; Langensalza 27 June 1866; surrender two days later)
- `/ledger/14` Kingdom_of_Hanover: confirmed (infobox 'Annexed by Prussia: 20 September 1866')

## first-french-colonial-empire: thin

Area: infobox None (None), Cliopatria 438.6, ratio None, acknowledged True. No area on the page; both Cliopatria shapes verdict wrong (a 438.6 km2 sliver), replaced by about 93,000 km2 of colonies.

Findings:

- `/ledger/1/confidence` [applied by reviewer] Occupation dated 1805 at confidence 2 although the page gives no year for any capture. Evidence: Page: 'when war resumed in 1803, the British soon recaptured them'; no year for Martinique, Guadeloupe, Guiana, Réunion or Mauritius. Research brief: 2 = year is the page's. Fix: Confidence lowered to 1; reviewer note appended.
- `/ledger/1 and /ledger/2` [for the author] Capture years and occupier disagree with the neighbours: the whole empire is drawn British-occupied from 1805. Evidence: british-colonial-empire /ledger/70-72: Martinique 1809/2, Mauritius 1810, Réunion 1810/7 (c3, as gains); portuguese-empire /ledger/72, 75: French Guiana occupied by Portugal 1809-1817 (c3/c2). Fix: Split the occupation per colony with the neighbours' dates (Martinique 1809, Guadeloupe 1810, Guiana 1809 by portuguese-empire, Senegal 1809, Mascarenes 1810) once a page is opened; until then keep confidence 1.
- `/keyframe_review/0/correction` [for the author] Santo Domingo (French 1795/1801-1809) is left out although neighbours hold it as French at confidence 3. Evidence: spanish-empire /ledger/74-76 (contest 1808/11-1809/7, gain 1809/7 from first-french-empire, c3); haiti /ledger/15-16 (contest 1805/2-3, c3); Treaty of Paris page: 'Santo Domingo returned to Spain (Art. VIII)'. Author's notes: 'not drawn'. Fix: Add Santo Domingo to the 1805 correction with a 1809/7 loss to spanish-empire (and the 1805 contest with haiti), or explain in notes why it is excluded; ask the spanish-empire, haiti and portuguese-empire authors to use first-french-colonial-empire as counterpart.

Gaps for a gap-filler:

- `/ledger/1` Year of each British capture (Martinique, Guadeloupe, Senegal, Guiana). Try: https://en.wikipedia.org/wiki/Invasion_of_Martinique_(1809)
- `/ledger/2` Mascarene capture (c1, 1811; the British dossier has 1810). Try: https://en.wikipedia.org/wiki/Mauritius_campaign_of_1809%E2%80%931811
- `/ledger/0` found 1805 at confidence 1 (Cliopatria's row start). Try: https://en.wikipedia.org/wiki/French_colonial_empire
- `/keyframe_review/0` Santo Domingo 1805-1809. Try: https://en.wikipedia.org/wiki/Siege_of_Santo_Domingo_(1808%E2%80%931809)

Spot checks:

- `/ledger/1` First_French_colonial_empire: not on page (no capture years; 'soon recaptured'); confidence lowered to 1
- `/ledger/3` First_French_colonial_empire: confirmed ('existed until 1814')
- `/ledger/4` Treaty_of_Paris_(1814): confirmed (30 May 1814; Guadeloupe Art. IX; restored list on the colonial page)
- `/ledger/5` Treaty_of_Paris_(1814): confirmed (Tobago, Saint Lucia, Seychelles, Mauritius 'handed over to British control')

## first-french-empire: fail

Area: infobox 2100000 (1812), Cliopatria 1064742, ratio 1.97, acknowledged True. Infobox figure is peak control including satellites; author notes it.

Findings:

- `/keyframe_review/7 to /keyframe_review/8` [for the author] About 100,000 km2 of the 1813-1814 collapse has no loss event: Belgium and Luxembourg, Catalonia and Andorra, the North Sea and Hanseatic departments, and the left-bank Rhine recipients. Evidence: Corrected 1812/1813 outline about 0.85-0.89 M km2 against 0.50 M km2 in 1814; the ledger loses only the Netherlands, Illyria, Valais, 'Italy' and the 1806-outline German cells. Neighbours record the other side: sovereign-principality-of-the-united-netherlands /ledger/1 (Belgium, 1814/8), principality-of-andorra /ledger/0 (found 1814 from FFE), free-city-of-hamburg /ledger/0 (1814), free-city-of-bremen /ledger/2, free-city-of-lubeck /ledger/4, duchy-of-oldenburg /ledger/2 (1813 gains from FFE), kingdom-of-hanover /ledger/7 (1813/10), kingdom-of-prussia /ledger/48 (1815/6 Lower Rhine). Fix: Add a dated loss for each block to its recipient (Belgium, Catalonia/Andorra, each Hanseatic city, Oldenburg, the Hanoverian north, the Rhineland), using the neighbours' dates and the pages already opened.
- `/ledger/12/region` [for the author] Region admin1 Niedersachsen (all of Lower Saxony, about 47,600 km2) at confidence 3 for the annexation of Oldenburg and Salm. Evidence: Confederation of the Rhine page: Oldenburg and Salm 'Annexed by France on 13 December 1810'; it names no other land. Duchy of Oldenburg is about 5,000 km2. Fix: Region: the Duchy of Oldenburg outline (cliopatria 'Duchy of Oldenburg') plus Salm; the Hanoverian north belongs to a separate event from kingdom-of-westphalia.
- `/ledger (1806-1810)` [for the author] Gains recorded by neighbours are missing: Westphalia's Weser department (1810) and Nord and Niederelbe (December 1810), Arenberg's Meppen and Dülmen (1810), Ragusa (occupied 1806/5, annexed 1808/1), Bayreuth (held to 1810), the Ionian Islands (1807-1814). Evidence: kingdom-of-westphalia /ledger/6-7 (c2/c3; Westphalia page: Nord and Niederelbe 'were ceded to the French Empire' in December 1810); duchy-of-arenberg /ledger/7 (c3); republic-of-ragusa /ledger/8, 11, 12 (c3); kingdom-of-bavaria /ledger/7 (1810 Bayreuth from FFE, c2); united-states-of-the-ionian-islands /ledger/0 (found 1815/11 from FFE). Fix: Add the gains (and later losses) with those counterparts.
- `/ledger/13/counterpart` [for the author] The 1811 North Sea and Lübeck annexation has one counterpart (free-city-of-hamburg) for land of Bremen, Lübeck and Oldenburg; Hamburg's dossier starts in 1814. Evidence: free-city-of-bremen /ledger/1 (1811 loss to FFE, c3), free-city-of-lubeck /ledger/3 (1811, c2); Oldenburg is already annexed in /ledger/12. Fix: One event per counterpart (Bremen, Lübeck, Hamburg); drop Oldenburg from this event; flag that no dossier holds Hamburg 1806-1811.
- `/ledger/5/region` [for the author] Etruria is drawn as admin1 Firenze (one province) plus Parma, which /ledger/6 annexes again. Evidence: Territorial evolution page: 'The Kingdom of Etruria and the Duchy of Parma (1808)'; Etruria is Tuscany; the gazetteer has region 'Tuscany'. Fix: Region {region: Tuscany}; leave Parma to /ledger/6.
- `/ledger/26` [for the author] All Italian cells are lost to kingdom-of-sardinia, while four other restored states record gains from FFE. Evidence: papal-states /ledger/39 (1814), ligurian-republic /ledger/4 (1814/4), grand-duchy-of-tuscany /ledger/2 (1814/5, c3), principality-of-monaco /ledger/15 (1814/5, c3); Sardinia /ledger/26, 28 gain only Piedmont, Savoy and Nice. Fix: Split the Italian loss per recipient.
- `/ledger/25-27 and /identity/end` [for the author] Three losses dated May 1814 follow the dissolve of April 1814 (end 1814/4); /ledger/27's counterpart german-confederation was founded in 1815. Evidence: /ledger/24: dissolve 1814/4 ('lasted from 18 May 1804 to 6 April 1814'); Treaty of Paris signed 30 May 1814; Confederation page: the Treaty 'declared the German states independent'. Fix: Date the losses at or before the dissolve (the territories were evacuated in April 1814) or move the end to 1814/5; use the actual recipients (Prussia, Bavaria, Hesse-Darmstadt, Swiss cantons) instead of german-confederation.
- `/ledger/8, /ledger/19, /ledger/14` [for the author] Joseph's Spain is drawn as a vassal of kingdom-of-spain from 1809 (c1), while the bonapartist-spain dossier exists. Evidence: bonapartist-spain /ledger/1 (vassal_start of FFE 1808/6), /ledger/11 (vassal_end 1813/6), /ledger/4 (1810 loss of Biscay, Navarre, Aragon and Catalonia to FFE, c3). Fix: Counterpart bonapartist-spain, 1808/6 to 1813/6; reconcile Catalonia (page 1812, bonapartist-spain 1810).
- `/ledger/15/counterpart` [for the author] Andorra is taken from principality-of-andorra, a dossier that begins in 1814. Evidence: co-principality-of-andorra /ledger/5: 1812 loss to first-french-empire (c2). Fix: Counterpart co-principality-of-andorra.
- `/ledger (occupations)` [for the author] Occupations that neighbours record with counterpart first-french-empire are missing. Evidence: electorate-of-hesse /ledger/2-6 (1806-1810), electorate-of-saxony /ledger/33-34 (1806), duchy-of-mecklenburg /ledger/1-2 (1806-1808), duchy-of-saxe-coburg-saalfeld /ledger/2-3 (1806-1807), swedish-pomerania /ledger/16-17 (1807-1810), kingdom-of-portugal /ledger/32-33 (1810/8-1811/4), free-city-of-lubeck /ledger/1-2 (1806/11-1811). Fix: Add the occupation_start/occupation_end pairs, or explain why the empire's ledger does not carry them.
- `/wars/0 and /wars/5` [for the author] The War of the Third Coalition lists austrian-empire (starts 1806) and has no zones; the War of the Sixth Coalition has no zones although ground changed hands. Evidence: habsburg-monarchy dossier ends 1805/12; the 1805 keyframe note attributes the extra German and Austrian cells to the Austerlitz campaign. Fix: Belligerent habsburg-monarchy for 1805; give both wars zones (Austria and Bavaria 1805; Germany 1813, eastern France 1814).

Gaps for a gap-filler:

- `/identity/end` The Hundred Days (20 March to 7 July 1815): the First French Empire page says the empire existed 'again briefly from 20 March 1815 to 7 July 1815'. Try: https://en.wikipedia.org/wiki/Hundred_Days
- `/ledger/17` End of the Russian occupation (c1). Try: https://en.wikipedia.org/wiki/French_invasion_of_Russia
- `/ledger/3, /ledger/18` Duchy of Warsaw vassal end (c1). Try: https://en.wikipedia.org/wiki/Duchy_of_Warsaw

Spot checks:

- `/ledger/0` First_French_Empire: confirmed (18 May 1804)
- `/ledger/7` Territorial_evolution_of_France: confirmed ('The Papal States, including Rome (1809)')
- `/ledger/10` Territorial_evolution_of_France: confirmed ('The Kingdom of Holland and the Valais (1810)')
- `/ledger/13` Territorial_evolution_of_France: confirmed year 1811 (Hanover, Oldenburg, Bremen, Hamburg; Lübeck 1811)
- `/ledger/14` Territorial_evolution_of_France: confirmed ('Catalonia and Andorra (1812)')
- `/ledger/9` First_French_Empire: confirmed (14 October 1809, Illyrian Provinces)
- `/ledger/12` Confederation_of_the_Rhine: date confirmed (13 December 1810); region not on page (page names Oldenburg and Salm, dossier draws all of Lower Saxony)
- `/ledger/2` Confederation_of_the_Rhine: confirmed (12 July 1806, 16 states)
- `/ledger/22` Confederation_of_the_Rhine: confirmed (4 November 1813)
- `/ledger/16` First_French_Empire: confirmed (24 June 1812)

## austrian-empire: fail

Area: infobox 698700 (None), Cliopatria 691307, ratio 1.01, acknowledged True. Infobox gives no year; compared with the 1815-1819 shape.

Findings:

- `/ledger/9/counterpart` [applied by reviewer] Ragusa and Dalmatia are gained in 1815 from republic-of-ragusa, which the republic-of-ragusa dossier dissolves into the French Empire in January 1808. Evidence: republic-of-ragusa /ledger/11-12 (1808/1, c3); italian-republic /ledger/7 (1810/6: Dalmatia and Ragusa to the Illyrian Provinces). Fix: Counterpart set to first-french-empire; reviewer note appended.
- `/ledger/27, /ledger/28, /ledger/29, /wars/5` [applied by reviewer] Counterpart denmark-norway ends January 1814. Evidence: kingdom-of-denmark-1814-1940 /ledger/9: 1864/10 loss to austrian-empire (c3). Fix: Counterparts and the Second Schleswig War belligerent set to kingdom-of-denmark-1814-1940.
- `/keyframe_review/5 and /ledger/6-9` [for the author] No ledger event explains the +157,000 km2 between the 1812-1813 shape (531,067 km2) and the 1814 shape (688,430 km2, verdict ok); the gains are dated 9 June 1815, when the French Empire no longer existed. Evidence: Keyframe 5 note: 'Austria holds the former Illyrian Provinces, Dalmatia and northern Italy' in 1814. Neighbours: italian-republic /ledger/8-9 (1814/4 loss and dissolve to austrian-empire), kingdom-of-bavaria /ledger/10 (Tyrol 1814/5), first-french-empire /ledger/23 (Illyria 1814); Bavaria /ledger/13 has Salzburg returned 1816/4 (Treaty of Munich, c3). Congress page gives no dates other than the Final Act. Fix: Add 1814 events (occupation_start or gain) for Lombardy-Venetia, the Illyrian Provinces with Dalmatia and Ragusa, and Tyrol with the neighbours' months, keeping 1815/6 as the formal confirmation; date Salzburg's return 1816/4; or mark keyframe 5 adjust with a correction.
- `/ledger (1849)` [for the author] The 1849 campaign against Sardinia is missing: the Novara contest and the occupation of Lomellina and Alessandria. Evidence: kingdom-of-sardinia /ledger/39-42: contest 1849/3 (c3), occupation_start by austrian-empire 1849/3 (c3), occupation_end 1849/8 (c2); the author opened the First Italian War of Independence page and the war entry runs to 1849. Fix: Add contest_start/contest_end 1849/3 and occupation_start 1849/3, occupation_end 1849/8 with the page's dates.
- `/ledger/14-16` [for the author] Sardinia records gains of Lombardy (1848/6) and Venice (1848/7) from Austria and their loss (1848/8); Austria records contests only. Evidence: kingdom-of-sardinia /ledger/34-37. Fix: Agree a model with eu-13: either Austria adds the loss and regain, or Sardinia converts its gains to contest events.
- `/ledger (reverse mirrors)` [for the author] Smaller transfers recorded by neighbours are missing here. Evidence: kingdom-of-bavaria /ledger/4 (1809/10 Innviertel and Hausruckviertel, c2) and /ledger/14 (1816/4 left-bank Palatinate from Austria, c3); kingdom-of-prussia /ledger/60 (1865/9 Lauenburg bought from Austria at Gastein, c2); duchy-of-cieszyn /ledger/6-7 (1849 merge into austrian-empire, c2). Fix: Add the matching events or tell the neighbours' authors why not.

Gaps for a gap-filler:

- `/ledger/12-13` Kraków annexation (1846 at c1, Cliopatria's year). Try: https://en.wikipedia.org/wiki/Free_City_of_Krak%C3%B3w
- `/wars` Neapolitan War 1815 (kingdom-of-naples-napoleonic /ledger/4, 8: contest with Austria 1815/3-5) is missing. Try: https://en.wikipedia.org/wiki/Neapolitan_War
- `/ledger/31-34` Prussian occupation of Bohemia (June-August 1866) not drawn as a contest zone. Try: https://en.wikipedia.org/wiki/Austro-Prussian_War
- `/ledger/0` found 1806 at c1 (page proclaims the empire 11 August 1804). Try: https://en.wikipedia.org/wiki/Austrian_Empire

Spot checks:

- `/ledger/2` Treaty_of_Sch%C3%B6nbrunn: confirmed (14 October 1809, Salzburg to Bavaria)
- `/ledger/3` Treaty_of_Sch%C3%B6nbrunn: confirmed (Gorizia, Trieste, Carniola, Istria, western Carinthia, Croatia south of the Sava to France)
- `/ledger/4` Treaty_of_Sch%C3%B6nbrunn: confirmed (West Galicia to the Duchy of Warsaw)
- `/ledger/7` Congress_of_Vienna: confirmed text ('regained control ... of the former Illyrian Provinces'); date is the Final Act's, inconsistent with the 1814 keyframe
- `/ledger/8` Congress_of_Vienna: confirmed text ('received Lombardy-Venetia in Italy and Ragusa in Dalmatia')
- `/ledger/18` Hungarian_Revolution_of_1848: confirmed (Világos capitulation after 11 August 1849; infobox end 4 October 1849)
- `/ledger/35` Austro-Prussian_War: confirmed (Holstein invaded 9 June; Peace of Prague 23 August 1866)
- `/ledger/36` Austrian_Empire: confirmed (Compromise of 1867: 30 March 1867)

## duchy-of-anhalt: thin

Area: infobox 3800 (None), Cliopatria 1990, ratio 1.91, acknowledged True. Text gives 2,300 km2 (ratio 1.16); the author compares both.

Gaps for a gap-filler:

- `/keyframe_review/2, /keyframe_review/5` Cliopatria's 1,552 km2 outline in 1814-1819 and 1866-1867 (438 km2 below 1820-1863 and 1868-1870) has no event; likely digitisation, unverified: page budget. Try: https://de.wikipedia.org/wiki/Herzogtum_Anhalt
- `/keyframe_review/4` -88 km2 in 1864-1865 unexplained. Try: https://de.wikipedia.org/wiki/Herzogtum_Anhalt
- `/ledger/4` dissolve 1871 at c1 (project convention; the duchy lasted to 1918). Try: https://en.wikipedia.org/wiki/Duchy_of_Anhalt

Spot checks:

- `/ledger/0` Duchy_of_Anhalt: confirmed ('In 1806, Napoleon elevated the remaining states ... to duchies'); Dessau page says 1807, noted by the author
- `/ledger/1` Anhalt-Bernburg: confirmed ('Anhalt-Zeitz-Hoym partitioned away: 1718-1812'; 'in 1812 the two parts of the territory were united')
- `/ledger/2` Anhalt-K%C3%B6then: confirmed ('united to Anhalt-Dessau by patent of 22 May 1853')
- `/ledger/3` Anhalt-Dessau: confirmed (last Duke of Anhalt-Bernburg died 19 August 1863)

## Cross-dossier matrix (non-matched rows)

- kingdom-of-hanover 1803 occupation_start (counterpart french-consulate) -> exception: french-consulate not written yet (eu-20, other part).
- kingdom-of-hanover 1810 loss (counterpart first-french-empire) -> mismatch: Nord and Niederelbe: Westphalia /ledger/7 loses them to FFE 1810/12; FFE has no gain from either Hanover or Westphalia. Mirror: kingdom-of-westphalia 1810 loss.
- kingdom-of-hanover 1810 occupation_end (counterpart french-consulate) -> mismatch: Consulate ended 1804/5; occupier in 1810 is first-french-empire, which has no occupation of Hanover.
- kingdom-of-hanover 1813 gain (counterpart kingdom-of-westphalia) -> mismatch: Westphalia dissolves with counterpart kingdom-of-prussia only; no loss to Hanover. Mirror: kingdom-of-westphalia 1813 dissolve.
- kingdom-of-hanover 1813 gain (counterpart first-french-empire) -> missing: FFE has no 1813 loss of the Hanoverian north.
- kingdom-of-hanover 1815 gain (counterpart kingdom-of-prussia) -> missing: Hildesheim, Lingen, Münster, Bentheim at c1; Prussia has no matching loss.
- kingdom-of-hanover 1815 loss (counterpart kingdom-of-denmark-1814-1940) -> mismatch: Denmark gains Lauenburg from kingdom-of-prussia; Prussia has no Lauenburg events in 1815 (counterpart fixed from denmark-norway). Mirror: kingdom-of-denmark-1814-1940 1815 gain.
- kingdom-of-prussia 1806 gain (counterpart kingdom-of-hanover) -> missing: Prussia /ledger/28-31: occupation 1805 and annexation 1806/2 of Hanover; no mirror in Hanover.
- free-city-of-bremen 1827 gain (counterpart kingdom-of-hanover) -> missing: Bremerhaven strip; no loss in Hanover.
- first-french-empire 1806 vassal_start (counterpart confederation-of-the-rhine) -> exception: no dossier yet (eu-20).
- first-french-empire 1807 vassal_start (counterpart duchy-of-warsaw) -> exception: no dossier yet (eu-20).
- first-french-empire 1807 vassal_start (counterpart kingdom-of-westphalia) -> missing: Westphalia dossier has no vassal_start to FFE.
- first-french-empire 1808 gain (counterpart duchy-of-parma-and-piacenza) -> exception: no dossier yet; the row starts 1815.
- first-french-empire 1809 vassal_start (counterpart kingdom-of-spain) -> mismatch: bonapartist-spain is the client (1808/6-1813/6); kingdom-of-spain records losses to FFE 1808/12. Mirror: bonapartist-spain 1808 vassal_start.
- first-french-empire 1810 gain (counterpart Republic of Valais) -> exception: listed in counterparts_needing_dossiers; Swiss dossier uses unwritten slug sieben-zenden for the Valais in 1815.
- first-french-empire 1811 gain (counterpart free-city-of-hamburg) -> mismatch: Bremen (and Lübeck /ledger/3) lose to FFE in 1811 but FFE names only Hamburg, whose dossier starts 1814. Mirror: free-city-of-bremen 1811 loss.
- first-french-empire 1812 gain (counterpart kingdom-of-spain) -> mismatch: bonapartist-spain loses Catalonia to FFE in 1810; page has 1812. Mirror: bonapartist-spain 1810 loss.
- first-french-empire 1812 gain (counterpart principality-of-andorra) -> mismatch: wrong slug: principality-of-andorra starts 1814. Mirror: co-principality-of-andorra 1812 loss.
- first-french-empire 1812 occupation_start (counterpart russian-empire) -> mismatch: type differs (Russia c1 loss/gain 1812-1813). Mirror: russian-empire 1812 loss.
- first-french-empire 1813 vassal_end (counterpart kingdom-of-westphalia) -> missing: 
- first-french-empire 1814 loss (counterpart austrian-empire) -> mismatch: Austria dates Illyria 1815/6, after FFE end 1814/4; Austria 1814 keyframe already holds it. Mirror: austrian-empire 1815 gain.
- first-french-empire 1814 loss (counterpart swiss-confederation) -> mismatch: Swiss gain the Valais 1815/8 from sieben-zenden, not from FFE. Mirror: swiss-confederation 1815 gain.
- first-french-empire 1814 loss (counterpart kingdom-of-sardinia) -> mismatch: Sardinia gains only Piedmont, Savoy, Nice; papal-states, ligurian-republic, grand-duchy-of-tuscany, principality-of-monaco gain from FFE in 1814 without a mirror. Mirror: kingdom-of-sardinia 1814 gain.
- first-french-empire 1814 loss (counterpart german-confederation) -> mismatch: german-confederation not written and founded 1815; Prussia gains the Lower Rhine from FFE 1815/6. Mirror: kingdom-of-prussia 1815 gain.
- republic-of-ragusa 1808 dissolve (counterpart first-french-empire) -> missing: No mirror in first-french-empire: annexed 1808/1 after occupation from 1806/5.
- kingdom-of-westphalia 1810 loss (counterpart first-french-empire) -> missing: No mirror in first-french-empire: Weser department 1810; Nord and Niederelbe 1810/12.
- duchy-of-arenberg 1810 loss (counterpart first-french-empire) -> missing: No mirror in first-french-empire: Meppen and Dülmen.
- free-city-of-lubeck 1806 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: occupation 1806/11-1811, loss 1811, regain 1813.
- electorate-of-hesse 1806 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1806-1810.
- electorate-of-saxony 1806 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1806.
- duchy-of-mecklenburg 1806 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1806-1808.
- duchy-of-saxe-coburg-saalfeld 1806 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1806/11-1807/7.
- swedish-pomerania 1807 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1807-1810.
- kingdom-of-portugal 1810 occupation_start (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1810/8-1811/4.
- kingdom-of-bavaria 1810 gain (counterpart first-french-empire) -> missing: No mirror in first-french-empire: Bayreuth from FFE.
- grand-duchy-of-tuscany 1814 gain (counterpart first-french-empire) -> missing: No mirror in first-french-empire: Tuscany restored 1814/5.
- principality-of-monaco 1814 gain (counterpart first-french-empire) -> missing: No mirror in first-french-empire: 1814/5.
- united-states-of-the-ionian-islands 1815 found (counterpart first-french-empire) -> missing: No mirror in first-french-empire: Ionian Islands from FFE.
- duchy-of-oldenburg 1813 gain (counterpart first-french-empire) -> missing: No mirror in first-french-empire: restored duchy.
- free-city-of-bremen 1813 gain (counterpart first-french-empire) -> missing: No mirror in first-french-empire: restored city.
- austrian-empire 1809 loss (counterpart duchy-of-warsaw) -> exception: no dossier yet (eu-20).
- austrian-empire 1815 gain (counterpart kingdom-of-bavaria) -> mismatch: Tyrol 1814/5 (13 months); Salzburg 1816/4. Mirror: kingdom-of-bavaria 1814 loss.
- austrian-empire 1815 gain (counterpart italian-republic) -> mismatch: 1814/4 vs 1815/6 (14 months). Mirror: italian-republic 1814 loss.
- austrian-empire 1815 gain (counterpart first-french-empire) -> mismatch: Illyria and (after fix) Ragusa/Dalmatia; FFE ends 1814/4. Mirror: first-french-empire 1814 loss.
- austrian-empire 1815 vassal_start (counterpart free-city-of-krakow) -> exception: no dossier yet (eu-20).
- austrian-empire 1846 gain (counterpart free-city-of-krakow) -> exception: no dossier yet; c1.
- austrian-empire 1854 occupation_start (counterpart principality-of-moldavia) -> exception: no dossier yet (eu-18).
- kingdom-of-sardinia 1848 gain (counterpart austrian-empire) -> mismatch: Sardinia gains Lombardy and Venice 1848/6-7 and loses them 1848/8; Austria has contests only.
- kingdom-of-sardinia 1849 occupation_start (counterpart austrian-empire) -> missing: Lomellina and Alessandria 1849/3-8, and the Novara contest; missing in Austria.
- kingdom-of-prussia 1865 gain (counterpart austrian-empire) -> missing: Lauenburg bought at Gastein 1865/9.
- kingdom-of-bavaria 1816 gain (counterpart austrian-empire) -> missing: left-bank Palatinate 1816/4.
- kingdom-of-bavaria 1806 gain (counterpart austrian-empire) -> mismatch: Pressburg cession of Tyrol is habsburg-monarchy 1805/12; Bavaria should name habsburg-monarchy (same for kingdom-of-wurttemberg 1806 and electorate-of-salzburg 1805/12). Mirror: habsburg-monarchy 1805 loss.
- kingdom-of-naples-napoleonic 1815 contest_start (counterpart austrian-empire) -> missing: Neapolitan War 1815/3-5.
- duchy-of-cieszyn 1849 merge (counterpart austrian-empire) -> missing: minor.
- first-french-colonial-empire 1805 occupation_start (counterpart british-colonial-empire) -> mismatch: British dates: Martinique 1809/2, Mauritius 1810, Réunion 1810/7 (as gains); French Guiana occupied by portuguese-empire 1809-1817. Mirror: british-colonial-empire 1809 gain.
- first-french-colonial-empire 1814 loss (counterpart british-colonial-empire) -> mismatch: Britain records Mauritius as a 1810 gain; no 1814 event for Saint Lucia, Tobago, Seychelles. Mirror: british-colonial-empire 1810 gain.
- spanish-empire 1809 gain (counterpart first-french-empire) -> missing: Santo Domingo 1809/7 (and haiti 1805 contest): counterpart should be first-french-colonial-empire, which does not draw it.
- portuguese-empire 1809 occupation_start (counterpart first-french-empire) -> mismatch: French Guiana: counterpart should be first-french-colonial-empire, which records a British occupation instead.
- duchy-of-anhalt 1812 gain (counterpart Anhalt-Zeitz-Hoym) -> exception: internal line, no dossier.
- duchy-of-anhalt 1853 merge (counterpart Anhalt-Köthen) -> exception: internal line, no dossier.
- duchy-of-anhalt 1863 merge (counterpart Anhalt-Bernburg) -> exception: internal line, no dossier.

Matched rows are in the JSON report (history/notes/phase-b/reviews/eu-20-d.json).

## Problems and routing

- No page failed to load. Pages opened: Kingdom_of_Hanover, Kingdom_of_Westphalia, Congress_of_Vienna, Territorial_evolution_of_France, First_French_Empire, Confederation_of_the_Rhine, Treaty_of_Schönbrunn, Austrian_Empire, Austro-Prussian_War, Hungarian_Revolution_of_1848, First_French_colonial_empire, Treaty_of_Paris_(1814), Duchy_of_Anhalt, Anhalt-Köthen, Anhalt-Dessau, Anhalt-Bernburg.
- The authors used denmark-norway (ends 1814/1) as post-1814 Denmark; kingdom-of-denmark-1814-1940 exists. Reviewer re-pointed the counterparts in kingdom-of-hanover and austrian-empire.
- Reviewer edits applied and re-validated (python3 -I history/tools/validate_dossier.py, 0 errors): kingdom-of-hanover /ledger/3, /ledger/11; austrian-empire /ledger/9, /ledger/27-29, /wars/5; first-french-colonial-empire /ledger/1.
- Routing for other groups: kingdom-of-westphalia (eu-20) lacks a vassal_start to FFE, a 1810 gain of Nord and Niederelbe and a 1813 loss to Hanover; kingdom-of-bavaria /ledger/2, kingdom-of-wurttemberg /ledger/0 and electorate-of-salzburg /ledger/5, 7 name austrian-empire for the Pressburg cessions that habsburg-monarchy records in 1805/12; spanish-empire /ledger/74-76, haiti /ledger/15-16 and portuguese-empire /ledger/72, 75 name first-french-empire for colonial land (Santo Domingo, French Guiana) that belongs to first-french-colonial-empire.
- No dossier holds Hamburg between 1806 and 1811: free-city-of-hamburg starts in 1814 with a found event from first-french-empire.
- Reviewer brief section 1 says reviewers do not edit dossiers; this run followed the orchestrator adjustment that allows small verified fixes.

Gazetteer names needed: East Frisia (region), Grubenhagen (region), Bremen-Verden (region), Saxe-Lauenburg (region), Lingen (place), Parma (region), Dessau (place), Bernburg (place), Köthen (place), Hoym (place).
Counterparts needing dossiers: Republic of Valais (1802-1810), republic-of-the-valais, [1802, 1810]; Republic of San Marco, republic-of-san-marco, [1848, 1849].
