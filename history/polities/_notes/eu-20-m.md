# eu-20-m (Europe 1789-1914, part m): what could not be settled

Six dossiers written 2026-11-01, all validate (python3 -I tools/validate_dossier.py ... --resolve): french-second-republic, italian-nationalists, hungarian-nationalists, republic-of-baden, second-french-empire, austria-hungary. Page counts: 2, 1, 2, 2, 6 (5 plus a page reused from the Republic dossier), 5.

## Cliopatria rows that are not what their label says
- italian-nationalists (1848, 76 cells): the Sicilian revolution of 12 Jan 1848 - 15 May 1849 (Kingdom of Sicily), not "Italian nationalism"; the shape is Sicily without Messina's corner, which matches "Parliament was never able to control Messina". Wikipedia field and Wikidata Q6093359 are the ideology's: dossier links "Sicilian revolution of 1848", wikidata null. Cliopatria has no 1849 shape (state lived to 15 May 1849).
- republic-of-baden (1849-1852): the Baden Revolution of May-July 1849 (provisional government, no republic proclaimed on the page), not the 1918-1945 Republic of Baden whose page and Wikidata Q690821 Cliopatria cites. The shape = grand duchy 1848 (57 of 59 cells) + 16 cells of the Bavarian Rhenish Palatinate; the page does not put the Palatinate under Baden's government. The rows run to 1852 but the rebellion ended 23 July 1849.
- hungarian-nationalists (1849-1957): two unrelated episodes. 1849-1852 = the Hungarian revolutionary state of 1848-49 (written here, December 1848 - August 1849). 1956-1957 (91,985 km2) = all Hungary in the gap of the Hungarian People's Republic row (1950-55, 1958-89); verdict wrong, the hungarian-people-s-republic dossier must draw Hungary through 1956-57. Q28513 is shared with austria-hungary and hungary: three different states, no merge.
- second-french-empire: shapes 1862-1869 hold 38-92 Mexican cells (occupation drawn as land, kept 2-3 years after the French left); 1870 omits 348 cells of north-east France (in Cliopatria's German Empire 1871 shape, far more than Alsace-Lorraine); 1856-1859 holds three Crimean cells; Reunion and French India vanish from 1856 with no page.
- austria-hungary: 1880-1907 draws occupied Bosnia and the Sanjak as land; the Sanjak stays to 1910 (page: returned 1909); 1915-1918 draw Russian-held Galicia as loss and Serbia, Montenegro, Albania, Wallachia, Italian and Ukrainian zones as land. Tianjin concession cells 1905-1917 not on any page opened.

## Not settled (per state)
- french-second-republic: page is thin (no area, no Algeria, no colonies). Rome occupation_end at 1852/12 is a dossier boundary only; second-french-empire reopens it (1853) and ends it 1870.
- italian-nationalists: Messina bombardment undated; no ruler list (Ruggero Settimo is head of state on the page).
- hungarian-nationalists: page gives no day for the April 1849 Declaration, no date for Vilagos or Komarom, no month for the Russian entry (June is a bridge, confidence 1). Found date (December 1848) chosen to match the Austrian Empire dossier's contest.
- republic-of-baden: no seat for the provisional government on the page (Karlsruhe is a reading); Palatinate government needs its own dossier.
- second-french-empire: Menton/Roquebrune (1861) confidence 1, from the Monaco dossier; Crimea evacuation date absent; Mexican occupations by town only for Veracruz, Puebla, Mexico City, Mazatlan, Guaymas (Guadalajara, Oaxaca, Chihuahua, Tampico not paired); German-held zone of 1870 unmapped; Cambodian protectorate (1863) and Cochinchina left to french-indochina / khmer-empire.
- austria-hungary: Austro-Hungarian zones in Romania, Ukraine/Moldova, Italy and northern Albania use Cliopatria's cells as the region (pages give no extent); Treaty of Bucharest border changes, Bukovina dates, Ukraine occupation dates, the Italian front line unverified (page budget). Pages for the Italian Front, Operation Faustschlag, Albania would settle them.

## Pages that failed
- https://en.wikipedia.org/wiki/Serbian_campaign_(World_War_I) (url_not_found; replaced by .../Serbian_campaign_of_World_War_I).
- https://en.wikipedia.org/wiki/Republic_of_Baden loaded but is the wrong state (1918-1945); used only for Baden's 1925 area.

## Gazetteer names needed
- place "Menton" (second-french-empire, 1861 gain; Menton and Roquebrune, Alpes-Maritimes, about 43.78 N 7.50 E).

## Counterparts without a dossier
- roman-republic-1849 (Roman Republic, 9 Feb - 3 Jul 1849; counterpart in french-second-republic and papal-states); state-of-slovenes-croats-and-serbs (Oct-Dec 1918); provisional government of the Baden Palatinate 1849 (suggested slug provisional-government-of-the-palatinate); ukrainian-people-s-republic of 1918 (Cliopatria row starts 1919); republic-of-austria, czechoslovakia, hungarian-republic (rows start 1919) as A-H successors.

## Repair pass (2026-11-01, after the reviewer's fail verdict on austria-hungary)

Only austria-hungary was touched (verdict fail; the other five were pass, fix or thin). It validates (0 errors; 2 warnings for counterpart slugs without a dossier). 44 events (was 35), 19 sources (was 5), 3 events at confidence 1. Ledger indices moved: reviewer's /ledger/3 is now /3 (redated 1902/12), /18 is /19, /20 is /21 (plus new /22 and /24), /21 is /23, /24-/26 are /29-/31, /34 is /32; the other splits are new (/33-/37).

Changed, by finding:
- BLOCKING hand-off (identity.successors, splits): the 1912 outline (2,645 cells) is now split at 1918/10 between czechoslovakia (Czechia and Slovakia, 515), republic-of-austria (331), hungarian-republic (Hungary and Carpathian Ruthenia, 418), state-of-slovenes-croats-and-serbs (455), kingdom-of-italy (Italy and Istria, 71), second-polish-republic (152), west-ukrainian-people-s-republic (eastern Galicia, 182), united-principalities-of-moldavia-and-wallachia standing for Romania (Romania and all Bukovina, 431) and serbs (Vojvodina and the Serbian bank of the Sava, 76). Checked with the gazetteer: no overlaps, 14 cells unassigned (11 on the German side of the frontier, 2 Chinese cells at Tianjin, 1 coast cell). Pages: Austria-Hungary (infobox successors; it names no lands for Romania, Galicia or Vojvodina), German-Austria, West Ukrainian People's Republic, Polish Liquidation Committee, Kingdom of Romania, Treaty of Trianon, Treaty of Saint-Germain-en-Laye (1919), Great National Assembly in Novi Sad.
- /ledger/34 (Austria split): redated 1918/10, source German-Austria page.
- /ledger/20 (Russian-held Galicia): closed at 1917/3 for russian-empire; new pair for russian-republic 1917/3 (confidence 1, a bridge) to 1917/8 (Czernowitz fell 3 August; Kerensky Offensive page).
- /ledger/18 (Romanian incursion end): 1916/10, Romanian Campaign page ('by 25 October the Romanian army was back to its initial positions'), confidence 2.
- /identity/rulers/1: Charles I now cites the Austria-Hungary page.
- Thin items worked: Tianjin gain 1902/12 and loss 1917/8 from the concession page (confidence 2 and 3); Military General Government of Lublin added (1915/9 to 1918/11, counterpart congress-poland); Montenegro occupation end 1918/10 (Kingdom of Montenegro page, confidence 3) and Albania 1918/9 (Principality of Albania page, confidence 2); Ukraine occupation start 1918/2 (Operation Faustschlag page).

Where I disagree with, or depart from, the reviewer's fix:
- Northern Bukovina goes to Romania, not to the West Ukrainian republic. The West Ukrainian page says the state 'also claimed the northern part of Bukovina and Carpathian Ruthenia' but only 'controlled most of Eastern Galicia'; the Kingdom of Romania page dates the union of Bukovina 28 November 1918, Saint-Germain gives Bukovina to Romania, and the Romanian dossier gains Bukovina whole (/ledger/27). Counting it twice would double-assign 22 cells.
- Carpathian Ruthenia (52 cells) stays with hungarian-republic, not czechoslovakia: the czechoslovakia dossier /ledger/2 gains it from hungarian-republic in April 1919.
- German-Austria page does not call 30 October a proclamation: 21 October 1918 the deputies declared they would 'form an independent German-Austrian state', 30 October the State Council was created as executive body, 12 November the republic. The split is dated 1918/10 on the strength of the 30 October State Council, confidence 2, and the note says so.
- Splits are all dated 1918/10 (the dissolution month) although the West Ukrainian republic (1 November), Serbia (24-25 November), Romania (28 November, 1 December) and Italy (3 November occupation, 1919 treaty) acted later; each note gives the true date and the successor's own dossier carries the gain.
- Romania and Serbia appear as united-principalities-of-moldavia-and-wallachia and serbs (the dossiers that carry the November-December 1918 gains), not kingdom-of-romania and yugoslavia, whose Cliopatria rows start in 1919.
- The russian-republic counterpart begins 1917/3 although that dossier starts on 14 September 1917: the russian-empire dossier dissolves into russian-republic in March 1917 (/ledger/137). The cross-checker may flag the start date; russian-republic (eu-17) may want to start in March 1917 with the Provisional Government.
- Montenegrin campaign page is silent on the end of the occupations; the end dates come from the Kingdom of Montenegro and Principality of Albania pages the two country dossiers cite.
- Crisana, Maramures (Romania), the three Montenegrin cells (given to the Slovenes-Croats-Serbs entry as the Dalmatian coast) and the extent of Istria and the Austrian Littoral rest on the researcher's reading; the pages name no such lands. The Slovenian part of the Austrian Littoral stays in the Slovenes-Croats-Serbs entry because the gazetteer has no name for it, although Saint-Germain gives the Littoral to Italy.

Still open for austria-hungary: extent of the Ukrainian, Moldovan, Wallachian and Italian zones (Cliopatria's cells; no page maps them); Isonzo strip held by Italy (Gorizia, 1916-1917) not recorded (small); Treaty of Bucharest (7 May 1918) ceded Carpathian passes to Austria-Hungary, no region named; congress-poland /ledger/8 does not name austria-hungary as the occupier of the Lublin area; ottoman-empire, qing-dynasty and republic-of-china still lack the matching Bosnia 1908 and Tianjin events (other groups).

Pages failed in this pass: https://en.wikipedia.org/wiki/Polish_Liquidation_Commission (url_not_found; replaced by Polish_Liquidation_Committee).

Counterparts needing a dossier (added): west-ukrainian-people-s-republic (1918-1919; Cliopatria lacks it); second-polish-republic and kingdom-of-romania (Cliopatria rows from 1919, other groups); military-government-of-lublin is named by congress-poland as a successor but has no dossier; German-Austria (1918-1919) is folded into republic-of-austria.
