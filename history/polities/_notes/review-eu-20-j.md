# Review of batch eu-20-j (reviewer run 2026-11-01, brief filled 2026-10-31)

Five dossiers. All validate with --resolve (0 errors). The warnings are unresolved gazetteer places and counterparts with no dossier. Spot checks used WebFetch on Treaty of Paris (1815), Bourbon Restoration in France, French conquest of Algeria, German Confederation (two reads), Free City of Cracow, Treaty of Florence (1844), Duchy of Modena and Reggio, and Duchy of Parma and Piacenza. No event checked was fabricated or mis-dated.

In the verdicts below, fix means fixed by the reviewer, thin means it goes to a gap-filler, and fail means it goes back to the author.

Common cause of the two fails on occupation: the authors left occupation events to the occupier. The schema (ledger type description) says for occupation_start/_end: 'the owner records the same event with the roles reversed'.

## bourbon-kingdom-of-france: fail

Area: infobox 0 km2 (no year), Cliopatria 628140 km2, ratio 0.0, acknowledged True. no area in the Restoration or July Monarchy infobox (checked on the Restoration page)

Findings:
- `/ledger (after /ledger/2)` (author to do): The allied military occupation of north-eastern France (November 1815 to 1818) is missing from the ledger, although the author opened two pages that state it. Evidence: Treaty of Paris (1815) page: 'parts of France were to be occupied by up to 150,000 soldiers for five years', 'in the eastern border territories of France, from the English Channel to the border with Switzerland', 'the foreign troops withdrew from France in 1818'. Restoration page: 'Until 1818, France was occupied by 1.2 million foreign soldiers'. The schema says for occupation_start/_end: 'the owner records the same event with the roles reversed'. The author's notes give the opposite rule ('occupation events belong to the occupiers'). Fix: Add occupation_start 1815-11 and occupation_end 1818, both with the same counterpart string (for example 'Seventh Coalition army of occupation' naming austrian-empire, kingdom-of-prussia, russian-empire and the British forces in the note). Region: France's eastern and northern border departments from the Channel to Switzerland, with the page's words in text. Confidence 3 for the start, 2 for the end year. Correct the sentence in /notes.
- `/wars` (author to do): The French invasion of Spain in 1823 (Hundred Thousand Sons of Saint Louis) is missing from wars, although the source's infobox gives it. Evidence: Bourbon Restoration in France infobox: 'Invasion of Spain: 6 April 1823'. Rule 10 asks that each war in the sources appears. The notes list the expedition as 'not recorded for lack of an opened page', but the page was opened. Fix: Add a war entry (1823, belligerents bourbon-kingdom-of-france and kingdom-of-spain, zone Spain) citing the Restoration page. Add occupation_start 1823-4 with counterpart kingdom-of-spain if a page dates the end; the end (1828) needs another page (see thin).

Thin (for a gap-filler):
- `/keyframe_review/0/correction`: The 1814 outline adds back only Landau, Saarlouis and Bouillon. Under the 1814 treaty France also held the Chambéry and Annecy part of Savoy, Saarbrücken, Philippeville and Mariembourg, which it lost in November 1815. kingdom-of-sardinia/ledger/29 records the Savoy gain from this state at confidence 1, and this dossier has no matching loss. Try: https://en.wikipedia.org/wiki/Treaty_of_Paris_(1814)
- `/ledger/1/counterpart`: The counterpart is free text ('Allied powers'). Landau went to Austria (then kingdom-of-bavaria in 1816), Saarlouis to kingdom-of-prussia, and Bouillon to the Netherlands' Luxembourg. No neighbour dossier carries a 1815 gain from this state. Try: https://en.wikipedia.org/wiki/Saarlouis
- `/ledger/6`: Antwerp siege start at confidence 1; the netherlands dossier has no French contest. Try: https://en.wikipedia.org/wiki/Siege_of_Antwerp_(1832)
- `/ledger/13`: The Gabon protectorate end at confidence 1, closed only at the state's end. Try: https://en.wikipedia.org/wiki/French_Gabon
- `/ledger (1844-1846)`: Tahiti: kingdom-of-tahiti/ledger/3-4 has contest_start 1844-3 and contest_end 1846-12 against this state at confidence 3, with no mirror here. Try: https://en.wikipedia.org/wiki/Franco-Tahitian_War
- `/ledger (1823-1828)`: End of the French occupation of Spain (troops stayed until 1828) Try: https://en.wikipedia.org/wiki/Hundred_Thousand_Sons_of_Saint_Louis
- `/keyframe_review/2..8`: Overseas cells are unverified (page budget). The Ivory Coast cells of 1815-1841 come before the French posts at Grand-Bassam, and the 1846-1847 shape has no Senegal. Try: https://en.wikipedia.org/wiki/Grand-Bassam

Spot checks: /ledger/0 confirmed (6 April 1814); /ledger/1 confirmed (Bouillon, Landau, Saarlouis; 20 November 1815); /ledger/2 confirmed (six communes of the Pays de Gex to Geneva); /ledger/3 confirmed (14 June 1830); /ledger/4 confirmed (5 July 1830); /ledger/12 confirmed (December 1847 surrender)

## duchy-of-modena-and-reggio: thin

Area: infobox 0 km2 (no year), Cliopatria 6816 km2, ratio 0.0, acknowledged True. the page gives no area, only an 1846 population

Findings:
- `/identity/predecessors/0/slug and /ledger/0/counterpart` (APPLIED by reviewer): Mis-typed slug: kingdom-of-italy-napoleonic does not exist. The Napoleonic Kingdom of Italy is the dossier italian-republic (1802-1814, alt name 'Kingdom of Italy (Napoleonic)'). Evidence: history/polities/italian-republic.json identity.alt_names include 'Kingdom of Italy (Napoleonic)' and 'Napoleonic Kingdom of Italy'; it ends 1814-4. Fix: Changed both to italian-republic, removed the slug from the notes' 'Counterparts without a dossier' list and added a reviewer sentence to /notes. Validates.
- `/ledger/1/confidence` (APPLIED by reviewer): Confidence 3 on a region the page does not name. The page says 'the former imperial fiefs in Lunigiana' and does not list them, while the region drawn is the whole of Lunigiana. Evidence: Duchy of Modena and Reggio page: 'In December 1815 he obtained the transfer from his mother Maria Beatrice d'Este of the former imperial fiefs in Lunigiana' (no fiefs named). The whole region includes the Tuscan enclaves Pontremoli, Bagnone and Fivizzano (Treaty of Florence page) and Sardinian Sarzana. Fix: Lowered to 2, with a reviewer sentence in the note. Validates.

Thin (for a gap-filler):
- `/ledger/1/region`: Name the Este fiefs (Aulla and neighbours). The whole of Lunigiana overlaps Tuscany's Pontremoli, Bagnone and Fivizzano enclaves from 1815 to 1847 and Parma's Pontremoli from 1847. Try: https://en.wikipedia.org/wiki/Lunigiana
- `/ledger (1847-12)`: The Enza border exchange with Parma. Treaty of Florence page: 'the two Emilian duchies would rationalize their borders by mutually exchanging territories along the Enza River'. It is in neither duchy's ledger. Try: https://en.wikipedia.org/wiki/Treaty_of_Florence_(1844)
- `/ledger (1815-4..5)`: Neapolitan occupation of Modena. kingdom-of-naples-napoleonic/ledger/6 and /10 have it at confidence 1, with no mirror here. Try: https://en.wikipedia.org/wiki/Neapolitan_War
- `/identity (scope)`: The duchy of 1452-1796 has no dossier. cispadane-republic (predecessor, 1796 events), cisalpine-republic (1797 gain) and duchy-of-ferrara (successor) all name this slug outside its 1814-1859 life. Either a separate dossier is needed or this one should say why not. Try: https://en.wikipedia.org/wiki/Duchy_of_Modena_and_Reggio

Spot checks: /ledger/1 confirmed date (December 1815); region overstated, confidence lowered to 2; /ledger/2 confirmed (Massa and Carrara, 1829); /ledger/3 confirmed (Guastalla from Parma, effective 17 December 1847); /ledger/4 confirmed (Tuscan vicariate of Fivizzano to Modena); /ledger/5 confirmed (December 1859, United Provinces)

## duchy-of-parma-and-piacenza: thin

Area: infobox 5660 km2 (1852), Cliopatria 7460 km2, ratio 1.32, acknowledged True. 

Thin (for a gap-filler):
- `/ledger/4`: 1848 loss to kingdom-of-sardinia at confidence 1. The Parma page says only 'an uprising in 1848 which temporarily drove them out'. Try: https://en.wikipedia.org/wiki/First_Italian_War_of_Independence
- `/ledger/5`: 1848-8 return from kingdom-of-sardinia at confidence 1. The Austrian occupation that followed is not recorded either. Try: https://en.wikipedia.org/wiki/First_Italian_War_of_Independence
- `/ledger (1847-12)`: The Enza exchange with Modena (Treaty of Florence page). Try: https://en.wikipedia.org/wiki/Treaty_of_Florence_(1844)
- `/identity (scope)`: The duchy of 1545-1802/1808 has no dossier. papal-states/ledger/23 (1545 loss), french-consulate/ledger/9 (1802 gain) and first-french-empire/ledger/20 (1808 gain) name this slug before its 1814 start. Try: https://en.wikipedia.org/wiki/Duchy_of_Parma_and_Piacenza

Spot checks: /ledger/0 confirmed (infobox 'Restored: 11 April 1814'); /ledger/1 confirmed (Guastalla to Modena, 17 December 1847); /ledger/2 confirmed (Lunigiana enclaves except Fivizzano: Pontremoli, Bagnone and others); /ledger/6 confirmed (infobox 'Ceded to the United Provinces of Central Italy: 8 December 1859')

## free-city-of-krakow: fail

Area: infobox 1188.8 km2 (no year), Cliopatria 1645 km2, ratio 1.38, acknowledged True. 

Findings:
- `/ledger (1815-5 and 1846-11)` (author to do): The protectorate is missing. The Free City was a protectorate of Austria, Prussia and Russia, but the ledger has no vassal events, and austrian-empire/ledger/18 (vassal_start 1815-6, confidence 3) and /26 (vassal_end 1846-11) have no mirror. Evidence: Free City of Cracow infobox: 'City-state and protectorate of Austria, Prussia, and Russia'; text: 'approved and guaranteed by Article VII of the Treaty between Austria, Prussia, and Russia of 3 May 1815'. This is the author's own first source. Fix: Add vassal_start 1815-5 and vassal_end 1846-11 with counterpart austrian-empire (and the same for kingdom-of-prussia and russian-empire, or one joint string explained in the note), region the Free City, confidence 3.
- `/ledger (1836, 1841)` (author to do): The Austrian occupation of 1836-1841 is only in /keyframe_review/2/note, not in the ledger. austrian-empire/ledger/24 and /25 have occupation_start 1836 and occupation_end 1841 with this state as counterpart. Evidence: Free City of Cracow page: 'Cracow was subsequently occupied by the Austrian army from 1836 to 1841.' Schema: 'the owner records the same event with the roles reversed'. Fix: Add occupation_start 1836 and occupation_end 1841, counterpart austrian-empire, region the Free City, confidence 3.
- `/ledger (1846-2..11)` (author to do): The 1846 occupations (Russian troops first, then Austrian) are given in /wars/1/outcome but not as ledger events. Evidence: /wars/1/outcome quotes the Kraków Uprising page: Kraków 'occupied first by Russians (3 March) and by Austrians'. Fix: Add occupation_start 1846-3 with counterpart russian-empire and its end, and occupation_start with counterpart austrian-empire ending at the 16 November 1846 annexation, citing the Kraków Uprising page.

Thin (for a gap-filler):
- `/keyframe_review/1`: No page explains the 1830-1833 shape being 5 percent larger (1,734 against 1,645 km2). Small, and kept ok under the page budget. Try: https://en.wikipedia.org/wiki/Free_City_of_Cracow

Spot checks: /ledger/0 confirmed (infobox 'Established: 3 May 1815'; created from the Duchy of Warsaw); /ledger/1 confirmed ('annexed by Austria on 16 November 1846'); /ledger/2 confirmed ('as the Grand Duchy of Kraków', 16 November 1846)

## german-confederation: fail

Area: infobox 0 km2 (no year), Cliopatria 281949 km2, ratio 0.0, acknowledged True. no Confederation total area on the page; all 11 shapes marked wrong (they are Prussia's provinces)

Findings:
- `/keyframe_review/0..10/correction, /ledger/0/region, /ledger/13/region` (author to do): The membership outline leaves out Carniola and the Littoral except Istria, which the page lists as members. The notes and the author's report say 'Austria's lands are not listed on the page', which is false. Evidence: German Confederation page, member table: 'Only included the Lands of the Bohemian Crown – Bohemia, Moravia and Austrian Silesia –' and 'Austrian lands – Austria, Carinthia, Carniola and the Littoral except Istria'. The corrections hold country Austria and Czechia only, with no Slovenia and no Gorizia or Trieste. Fix: Add the Austrian member lands to every correction and to the found and dissolve regions: Slovenia without Prekmurje and the Istrian coast, and Italy's Gorizia and Trieste. Check Tyrol south of the Brenner (Trentino-South Tyrol) on a page before adding it. Correct /notes.
- `/ledger (1850)` (author to do): The removal of the Duchies of Auschwitz and Zator is missing. /ledger/5 adds them in 1818, but no loss follows. Evidence: German Confederation page: 'the Duchies of Auschwitz and Zator, parts of the Kingdom of Galicia and Lodomeria, were only included from 1818 to 1850.' Fix: Add a loss in 1850 (no month), counterpart austrian-empire, with the region of /ledger/5, confidence 3.
- `/ledger/1/region, /keyframe_review/0..5/correction, /ledger (1839)` (author to do): Luxembourg is drawn as the modern country. Until 1839 the member Grand Duchy also held the present Belgian Province of Luxembourg, and its departure in 1839 is not recorded. Evidence: German Confederation page: 'the larger province of Luxembourg had left the Confederation at its accession to Belgium in 1839' and 'In 1839, as compensation to the Netherlands for the loss of part of its province of Luxemburg to Belgium, the Duchy of Limburg was created'. Fix: Region for 1815-1839: country Luxembourg plus the Belgian province of Luxembourg. Add a loss in 1839 (counterpart kingdom-of-belgium, region the Belgian Province of Luxembourg) beside /ledger/6.
- `/ledger (1863-12, 1864)` (author to do): The federal execution in Holstein is missing. duchy-of-holstein/ledger/9 has occupation_start 1863-12 (confidence 3) and /11 occupation_end 1864-10 with german-confederation as counterpart, and no mirror is here. The notes say 'no dates on the pages'. Evidence: German Confederation page: 'In 1863, the Confederation ordered the execution of the duke of Holstein (the Danish king).' Fix: Add occupation_start 1863-12 and occupation_end 1864, counterpart duchy-of-holstein, region Holstein (and Lauenburg if a page says so), and match duchy-of-holstein's months.

Thin (for a gap-filler):
- `/keyframe_review/*/correction`: Farther Pomerania (the western part of today's Pomeranian Voivodeship: Słupsk, Lębork, Bytów) was in Prussia's Province of Pomerania, a member, and is not in the outline. Try: https://en.wikipedia.org/wiki/Province_of_Pomerania_(1815–1945)
- `/ledger/11, /ledger/12`: The 1866 contest names kingdom-of-prussia over Hanover, Saxony and Hesse land that belongs to members. kingdom-of-prussia has no mirror contest. Consider leaving the contests to the member states' dossiers. Try: https://en.wikipedia.org/wiki/Austro-Prussian_War

Spot checks: /ledger/4 confirmed (Hesse-Homburg joined 7 July 1817); /ledger/5 confirmed for 1818; the same sentence ends the inclusion in 1850, which is missing; /ledger/6 confirmed (Limburg joined 5 September 1839); /ledger/7 confirmed (admitted 11 April 1848); /ledger/9 confirmed (removed 30 May 1851); /ledger/13 confirmed (Peace of Prague 23 August 1866; confirmed by members the next day)

## Cross-dossier matrix

- bourbon-kingdom-of-france 1814 found (first-french-empire) -> first-french-empire 1814 dissolve: **matched**. both April 1814
- bourbon-kingdom-of-france 1815 loss (Allied powers (Austria, Great Britain, Prussia, Russia)) -> -  : **mismatch**. Free-text counterpart. Saarlouis went to kingdom-of-prussia (prussia/ledger/48 gains Sarre etc. from first-french-empire, 1815-6), Landau to austrian-empire then kingdom-of-bavaria (1816), Bouillon to the Netherlands-Luxembourg. No dossier has a gain from this state.
- kingdom-of-sardinia 1815 gain (bourbon-kingdom-of-france) -> bourbon-kingdom-of-france  loss: **missing**. sardinia/ledger/29: the Annecy and Chambéry part of Savoy, confidence 1. France has no loss, and its 1814 keyframe lacks the land. Thin item for France.
- bourbon-kingdom-of-france 1815 loss (swiss-confederation) -> swiss-confederation 1815 gain: **matched**. Pays de Gex communes, 1815-11 on both sides
- bourbon-kingdom-of-france 1830 contest_start (regency-of-algiers) -> regency-of-algiers 1830 contest_start: **matched**. 1830-6 on both sides; contest_end 1830-7 matched too
- bourbon-kingdom-of-france 1832 contest_start (netherlands) -> netherlands  contest_start: **missing**. netherlands records the Antwerp citadel as occupation_end 1832-12 against kingdom-of-belgium, with no contest against France
- bourbon-kingdom-of-france 1836 contest_start (emirate-of-abdelkader) -> emirate-of-abdelkader 1836 contest_start: **matched**. 1836-1 on both sides; 1837-5 contest_end matched; 1839 restart matched
- bourbon-kingdom-of-france 1847 contest_end (emirate-of-abdelkader) -> emirate-of-abdelkader 1846 contest_end: **mismatch**. The emirate ends the contest in 1846 at confidence 1. The French conquest of Algeria page: surrender in December 1847. The emirate should move to 1847-12.
- kingdom-of-tahiti 1844 contest_start (bourbon-kingdom-of-france) -> bourbon-kingdom-of-france  contest_start: **missing**. tahiti/ledger/3-4, 1844-3 to 1846-12, confidence 3. France has no mirror (page budget). Thin item.
- bourbon-kingdom-of-france 1838 vassal_start (Gabon coastal chiefs) -> -  : **exception**. free-text vassal; gabon.json starts 1960
- bourbon-kingdom-of-france 1848 dissolve (french-second-republic) -> french-second-republic 1848 found: **matched**. 1848-2 on both sides
- duchy-of-modena-and-reggio 1814 found (italian-republic) -> italian-republic 1814 dissolve: **mismatch**. Counterpart corrected by the reviewer from kingdom-of-italy-napoleonic. italian-republic/ledger/8-9 give all its land to austrian-empire in 1814-4 and name no Modena successor. Route to italian-republic.
- duchy-of-modena-and-reggio 1815 gain (duchy-of-massa-and-carrara) -> -  : **exception**. No dossier yet; in counterparts_needing_dossiers. eu-20-x declined to write it. The 1829 gain is the same case.
- duchy-of-modena-and-reggio 1847 gain (duchy-of-parma-and-piacenza) -> duchy-of-parma-and-piacenza 1847 loss: **matched**. Guastalla, 1847-12 on both sides
- duchy-of-modena-and-reggio 1847 gain (grand-duchy-of-tuscany) -> grand-duchy-of-tuscany 1847 loss: **matched**. Fivizzano; tuscany/ledger/5 has no month
- duchy-of-modena-and-reggio 1859 dissolve (united-provinces-of-central-italy) -> united-provinces-of-central-italy 1859 gain: **matched**. 1859-12
- kingdom-of-naples-napoleonic 1815 occupation_start (duchy-of-modena-and-reggio) -> duchy-of-modena-and-reggio  occupation_start: **missing**. naples/ledger/6 and /10 (1815-4 to 1815-5, confidence 1). Modena has no mirror. Thin.
- cispadane-republic 1796 gain (duchy-of-modena-and-reggio) -> duchy-of-modena-and-reggio  loss: **mismatch**. The event falls before this dossier starts (1814). The pre-1796 duchy has no dossier; the same goes for cisalpine-republic 1797 and duchy-of-ferrara's successor link.
- duchy-of-parma-and-piacenza 1814 found (first-french-empire) -> first-french-empire 1814 loss: **matched**. first-french-empire/ledger/72, 1814-4
- duchy-of-parma-and-piacenza 1847 gain (grand-duchy-of-tuscany) -> grand-duchy-of-tuscany 1847 loss: **matched**. Pontremoli; tuscany/ledger/6
- duchy-of-parma-and-piacenza 1848 loss (kingdom-of-sardinia) -> kingdom-of-sardinia 1848 gain: **matched**. Confidence 1 on the Parma side, 2 on Sardinia's. The 1848-8 return is matched too.
- duchy-of-parma-and-piacenza 1859 dissolve (united-provinces-of-central-italy) -> united-provinces-of-central-italy 1859 gain: **matched**. 1859-12
- papal-states 1545 loss (duchy-of-parma-and-piacenza) -> duchy-of-parma-and-piacenza  gain: **mismatch**. 1545 is before this dossier starts (1814). The same applies to french-consulate/ledger/9 (1802) and first-french-empire/ledger/20 (1808). The pre-1802 duchy has no dossier.
- free-city-of-krakow 1815 found (duchy-of-warsaw) -> duchy-of-warsaw 1815 loss: **matched**. 1815-5 here, 1815-6 there; within a year
- austrian-empire 1815 vassal_start (free-city-of-krakow) -> free-city-of-krakow  vassal_start: **missing**. austrian-empire/ledger/18 (confidence 3) and /26 vassal_end 1846-11. Kraków has no protectorate events. Kraków fix.
- austrian-empire 1836 occupation_start (free-city-of-krakow) -> free-city-of-krakow  occupation_start: **missing**. austrian-empire/ledger/24-25, 1836 to 1841. Kraków fix.
- free-city-of-krakow 1846 loss (austrian-empire) -> austrian-empire 1846 gain: **matched**. 1846-11. kingdom-of-galicia-and-lodomeria/ledger/6 also gains the city, which matches the dissolve, so two Austrian dossiers both take it.
- german-confederation 1815 gain (netherlands) -> netherlands  : **exception**. Umbrella membership, not a transfer of land. The same holds for /ledger/2, 3, 5, 6, 7 and 9: the member keeps its land, so no mirror is expected.
- german-confederation 1817 gain (landgraviate-of-hesse-homburg) -> -  : **exception**. No dossier; in counterparts_needing_dossiers (eu-20-x declined it)
- german-confederation 1848 contest_start (kingdom-of-denmark-1814-1940) -> kingdom-of-denmark-1814-1940  contest_start: **missing**. For 1848-1851 Denmark records only a loss to duchy-of-holstein (the rebels), with no contest against german-confederation.
- kingdom-of-denmark-1814-1940 1864 contest_start (german-confederation) -> german-confederation  contest_start: **mismatch**. denmark/ledger/4-8 (1864 contests and loss) name german-confederation. The German Confederation page says the war was 'foreign to the Confederation, which took no part in it'. Denmark should name austrian-empire and kingdom-of-prussia.
- duchy-of-holstein 1863 occupation_start (german-confederation) -> german-confederation  occupation_start: **missing**. holstein/ledger/9 (1863-12, confidence 3) and /11 (1864-10). german-confederation fix.
- german-confederation 1866 contest_start (kingdom-of-prussia) -> kingdom-of-prussia  contest_start: **missing**. Prussia records gains from Hanover, Hesse, Nassau and Frankfurt but no contest with the Confederation
- german-confederation 1866 dissolve (north-german-confederation) -> north-german-confederation 1867 found: **mismatch**. The NGC found (1867-7) names kingdom-of-prussia and lists only Prussia as predecessor. The years are within one; the counterparts disagree.
- german-confederation 1815 found (confederation-of-the-rhine) -> confederation-of-the-rhine 1813 dissolve: **matched**. confederation-of-the-rhine lists german-confederation as successor; the gap 1813-1815 is historical

## Problems for the orchestrator

- Reviewer edit: duchy-of-modena-and-reggio.json changed in place (predecessor and /ledger/0 counterpart kingdom-of-italy-napoleonic -> italian-republic; /ledger/1 confidence 3 -> 2; reviewer sentences in /ledger/1/note and /notes). It validates and was read back. Drop kingdom-of-italy-napoleonic from the author's counterparts_needing_dossiers: italian-republic.json covers the Napoleonic Kingdom of Italy.
- Pre-restoration duchies: no dossier exists for the Duchy of Modena and Reggio before 1796 or the Duchy of Parma and Piacenza before 1802. cispadane-republic, cisalpine-republic, duchy-of-ferrara, papal-states, french-consulate and first-french-empire point their events at the 1814 slugs, outside those dossiers' lives. The orchestrator must decide between new slugs and extending the dossiers.
- kingdom-of-denmark-1814-1940 names german-confederation as counterpart of its 1864 contests and loss. The German Confederation page says the Confederation took no part, so route the fix to Denmark's owner.
- emirate-of-abdelkader ends its contest with France in 1846 at confidence 1; the conquest page gives December 1847.
- italian-republic gives all its 1814 land to austrian-empire and names no successor in Modena (or Parma via first-french-empire).
- The research brief and the authors' notes read occupation events as belonging only to the occupier. The schema says the owner records them too. This misreading caused the France and Kraków failures and may recur in other batches.
- Kingdom of Monaco was not written (merged into principality-of-monaco by another group), as the author reported; not reviewed here.

Gazetteer names needed: Landau (place), Gex (place), Guastalla (place), Fivizzano (place), Massa (place), Lunigiana (region), Pontremoli (place).
Counterparts needing dossiers: duchy-of-massa-and-carrara [1473, 1829], landgraviate-of-hesse-homburg [1622, 1866], duchy-of-modena-and-reggio-1452 [1452, 1796], duchy-of-parma-and-piacenza-1545 [1545, 1802].
