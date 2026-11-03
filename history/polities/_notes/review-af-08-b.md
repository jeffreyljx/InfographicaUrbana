# Review of batch af-08-b (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: french-africa (fail), kamerun (fix, applied by the reviewer). Validator: both valid, no warnings, before and after the reviewer's edits.

## french-africa: fail

### Findings

- `/keyframe_review/17` (blocking, for the author). Keyframe french-africa_1900 is 'ok' for 1900-1904 although the ledger gains the whole Algerian Sahara in 1903 (/ledger/35, confidence 3) and the AOF Sahara-Sahel interior in 1904 (/ledger/36): about 5.6 million km2 enter the ledger one to two years before any keyframe draws them. Evidence: shapes.csv: french-africa_1900 4,488,516 km2 (1900-1904), french-africa_1905 10,130,495 km2; the keyframe_review/18 note itself counts Algeria +5,263, Niger +4,204, Mauritania +3,990, Mali +3,681 cells in 1905. Brief rule 4: an event with no trace in the keyframes is fine only if small or the keyframe is marked adjust. Fix: Add a new keyframe french-africa_1903 (from 1903, to 1904, verdict adjust, correction = union of Cliopatria French Africa 1900 and intersect(minus(French Africa 1905, French Africa 1900), Algeria)), and mark french-africa_1900 adjust 'valid for 1900-1902'. For /ledger/36 either draw the AOF interior in the same new keyframe or re-date it to 1905 at confidence 1: the French West Africa page's 1904 sentences ('formally named French West Africa (AOF)', 'both Mauritania and Niger were classed Military Territories') date an administrative act, not an acquisition, so lower /ledger/36 to confidence 1 in either case.
- `/keyframe_review/10` (for the author). New keyframe french-africa_1881 (1881-1884) omits Guinea while /ledger/14 gains all of Guinea (about 245,000 km2) in 1884 at confidence 3. Evidence: Scramble for Africa page: 'In 1884, Germany declared Togoland, the Cameroons and South West Africa to be under its protection;' ... 'France occupied Guinea.' Cliopatria draws Guinea from 1885. Fix: Either split the keyframe (french-africa_1881 to 1883, new french-africa_1884 = 1880 shape plus Tunisia plus Guinea) or say in the note that the 1884 Guinea gain is drawn from 1885.
- `/ledger (missing, 1892 and 1907)` (blocking, for the author). No gains from republic-of-liberia, although the Liberia dossier records two losses to french-africa. Evidence: republic-of-liberia ledger: 1892-12 loss to french-africa (Franco-Liberian treaty of 8 December 1892, source https://en.wikipedia.org/wiki/Ivory_Coast%E2%80%93Liberia_border) and 1907-09 loss to french-africa (18 September 1907, source https://en.wikipedia.org/wiki/Guinea%E2%80%93Liberia_border). Fix: Add gain events 1892-12 and 1907-09, counterpart republic-of-liberia, with the same regions as the Liberia dossier's losses, citing those two pages (add them to sources).
- `/ledger/40` (blocking, for the author). Wadai is a single 1911 gain at confidence 1, while the wadai-empire dossier records a war and an occupation by french-africa with no mirror here. Evidence: wadai-empire ledger (source https://en.wikipedia.org/wiki/Wadai_War, confidence 3): contest_start 1908-05, occupation_start 1909-06, contest_end 1911-10, occupation_end and dissolve to french-africa 1912. Fix: Open the Wadai War page; add contest_start 1908-05, occupation_start 1909-06 (Abeche), contest_end 1911-10 and occupation_end 1912, move the gain to 1912 (or explain the year), and add the Wadai War to wars[] with its zone.
- `/ledger/20` (blocking, for the author). Dahomey's 1890 loss to french-africa and the two Franco-Dahomean wars have no mirror; the 1894 gain has no month. Evidence: dahomey ledger: contest_start 1890-03, loss 1890-10 and contest_end 1890-10 (First_Franco-Dahomean_War, confidence 3); contest_start 1892-07, contest_end 1894-01, loss and dissolve 1894-01 (Second_Franco-Dahomean_War / Dahomey). The Scramble for Africa page gives only 'in 1894'. Fix: Add the 1890-10 gain from dahomey and the contest pairs (or say why the wars hold no ground), give /ledger/20 month 1 from the Dahomey page, and add the First Franco-Dahomean War to wars[].
- `/ledger/13` (blocking, for the author). Porto-Novo is gained only in 1882; the French Africa page and the kingdom-of-porto-novo dossier also give the 1863 protectorate. Evidence: French Africa page list: 'Porto-Novo(protectorate) (1863–1865, 1882)'. kingdom-of-porto-novo ledger: 1863 loss and dissolve to french-africa (Porto-Novo page, confidence 3). Counterpart string 'Porto-Novo kingdom' replaced by the slug kingdom-of-porto-novo (applied, see next finding). Fix: Add the 1863 protectorate (vassal_start or gain, counterpart kingdom-of-porto-novo) and its 1865 end, keep 1882; note the disagreement with the Porto-Novo dossier, which ends the kingdom in 1863.
- `/ledger/13/counterpart, /ledger/29/counterpart, /ledger/33/counterpart, /ledger/42/counterpart` (applied by reviewer). Counterparts written as names ('Porto-Novo kingdom', 'Dar al Kuti' twice, 'Emirate of Trarza') although those dossiers now exist. Evidence: history/polities/ holds kingdom-of-porto-novo.json, dar-al-kuti.json and emirate-of-trarza.json; emirate-of-trarza records loss 1902-12 to french-africa, dar-al-kuti loss 1912-12. Fix: Replaced by the slugs kingdom-of-porto-novo, dar-al-kuti (both vassal events, so they still pair) and emirate-of-trarza; validator re-run, valid, no warnings.
- `/ledger/42` (blocking, for the author). Dar al Kuti ends as a vassal in 1912 but is never gained: the page says it was annexed. Evidence: French Equatorial Africa page: 'declaring the slaves in Dar al Kuti free and annexing the territory in 1912'. dar-al-kuti ledger: loss 1912-12 and dissolve to french-africa. Madagascar is handled correctly with vassal_end plus gain in 1897. Fix: Add a 1912 gain, counterpart dar-al-kuti, same region (admin1 Bamingui-Bangoran), source French_Equatorial_Africa, confidence 3; the Dar al Kuti dossier should add the 1897 vassal_start (it has none).
- `/ledger/63` (blocking, for the author). Tunisia is gained from nazi-germany on 13 May 1943 although the ledger never lost or occupied it in 1942. Evidence: French protectorate of Tunisia page: 'The occupation of the country in 1942 by Germany'; 'when the Axis were forced out of Tunisia in 1943'; Bey deposed 'on 13 May 1943'. No 1942 event in the ledger. Fix: Add an occupation_start 1942 (counterpart nazi-germany, the eastern Tunisian bridgehead, month from the Tunisian campaign page if opened) and change /ledger/63 to occupation_end 1943-05 with the same counterpart.
- `/ledger/60` (blocking, for the author). Djibouti is lost to british-africa in December 1942 but regained in 1943 from free-french (/ledger/61); british-africa has no mirror. Evidence: French Somaliland infobox (opened): 'British occupation: December 28, 1942' and no sentence on the return. british-africa ledger has no Djibouti event 1940-1943. Fix: Make the 1942 event an occupation by british-africa (occupation_start 1942-12, occupation_end 1943 at confidence 1) or name free-french on both sides with a page that says so; either way the 1942 and 1943 counterparts must agree, and british-africa (af-08) needs the mirror.
- `/ledger/51, /ledger/52, /ledger/54` (blocking, for the author). The mandate years end the occupation of Neukamerun, Cameroon (1919) and Togo (1922-07) without any gain, so the ledger never makes them French land though every later keyframe draws them. Evidence: Schema: occupation_end ends a hatched occupation; annexation is a gain (the dossier itself pairs vassal_end with a gain for Madagascar in 1897). /ledger/51 text also says Neukamerun became 'part of French Cameroon', but its region (French Africa 1905 minus 1911) is the slice of Gabon, Middle Congo and Ubangi-Shari that went back to the AEF. Fix: Add gain events from german-africa beside /ledger/51, /ledger/52 and /ledger/54 (same regions, same sources); correct the /ledger/51 text to the AEF colonies.
- `/wars/14` (applied by reviewer). The Algerian War ran to 1962, past the dossier's end of 1957 (brief rule 2: wars inside the life). Evidence: identity.end.year 1957; war from 1954 to 1962. Fix: Set to 1957 and prefixed the outcome with a sentence that the war continues in the french-fifth-republic dossier; validator re-run, valid.
- `/ledger/38, /ledger/53` (for the author). The 1905 'gain from ottoman-tripolitania' (534 Libyan cells, including Ghat) and the 1920 loss to italian-africa rest on no page, and ottoman-tripolitania records no loss to french-africa. Evidence: Both events confidence 1, 'page silent'; ottoman-tripolitania ledger has no event with counterpart french-africa; Ghat lies inside the block the 1920 keyframe note describes. Fix: Find a page for the Saharan frontier (the 1919 Franco-Italian frontier agreement, the Algeria-Libya border); if none shows French rule there, mark keyframes 1905-1919 adjust without the Libyan block and drop both events.

### Gaps (confidence 1, for a gap-filler)

- `/ledger/0`: Cliopatria's 1846 start (Senegal posts, Gabon, Mayotte); no page dates a French Africa entity in 1846 (try https://en.wikipedia.org/wiki/French_colonial_empire)
- `/ledger/2, /ledger/3, /ledger/4, /ledger/5, /ledger/6`: the 1849-1860 steps in Gabon, Senegal, the upper Senegal and the north bank (Faidherbe era) (try https://en.wikipedia.org/wiki/French_Senegal)
- `/ledger/8`: the 1870 Algerian step of +931 cells (about 244,000 km2) (try https://en.wikipedia.org/wiki/Southern_Territories)
- `/ledger/15, /ledger/18`: the 1885 and 1890 small steps (Ivory Coast, Central African Republic cells) (try https://en.wikipedia.org/wiki/French_Congo)
- `/ledger/22, /ledger/23`: the 1895 Gabon-Congo-Ubangi and Algerian steps (+9,754 cells in all) (try https://en.wikipedia.org/wiki/French_Congo)
- `/ledger/38, /ledger/53`: the Libyan Sahara block of 1905-1919 and its 1920 loss (try https://en.wikipedia.org/wiki/Algeria%E2%80%93Libya_border)
- `/ledger/40`: the conquest of Wadai and Chad (1908-1912) (try https://en.wikipedia.org/wiki/Wadai_War)
- `/ledger/61`: the 1943 reunion of the Free French and the Algiers command (try https://en.wikipedia.org/wiki/French_Committee_of_National_Liberation)
- `/ledger/68`: the end year: the AOF and AEF lasted to 1958 and the colonies went independent in 1960 (try https://en.wikipedia.org/wiki/French_Community)
- `/ledger (missing, 1942)`: the British invasion of Madagascar (May-November 1942) and its handover to the Free French (try https://en.wikipedia.org/wiki/Battle_of_Madagascar)

### Spot checks

- `/ledger/12` https://en.wikipedia.org/wiki/French_protectorate_of_Tunisia: confirmed. 'On 12 May 1881, forced Bey Muhammad III as-Sadiq to sign the Treaty of Bardo'; contest_start 24 April 1881 also on the page
- `/ledger/14` https://en.wikipedia.org/wiki/Scramble_for_Africa: confirmed. 'In 1884 ...' 'France occupied Guinea.' (keyframe does not draw it until 1885: see fixes)
- `/ledger/32, /ledger/35` https://en.wikipedia.org/wiki/French_conquest_of_Algeria: confirmed. 'In 1902, a French military expedition entered Hoggar Mountains and defeated Kel Ahaggar in a battle in Tit'; 'The conquest of the Saharan lands in Algeria finished in 1903'
- `/ledger/41` https://en.wikipedia.org/wiki/Scramble_for_Africa: confirmed. 'In November 1911, a compromise was reached ... in return for a slice of territory in the French Equatorial African colony of Middle Congo'
- `/ledger/42` https://en.wikipedia.org/wiki/French_Equatorial_Africa: confirmed. 'annexing the territory in 1912' (Dar al Kuti)
- `/ledger/43, /ledger/66` https://en.wikipedia.org/wiki/French_protectorate_in_Morocco: confirmed. 'officially established 30 March 1912'; 'the northern tenth of the country'; 'dissolution of the Treaty of Fez on 2 March 1956'
- `/ledger/55, /ledger/56, /ledger/59` https://en.wikipedia.org/wiki/French_Equatorial_Africa: confirmed. 'French Cameroon and the entirety of the AEF except for Gabon rallied to the Free French Forces in August 1940'; 'Gabon instead remained loyal to Vichy France until 12 November 1940'
- `/ledger/60` https://en.wikipedia.org/wiki/French_Somaliland: confirmed. infobox 'British occupation: December 28, 1942'; the page says nothing of the return
- `/ledger/62, /ledger/65` https://en.wikipedia.org/wiki/French_military_administration_in_Fezzan: confirmed. 'Free French forces moved north from Chad to take control of the territory in January 1943'; 'to form the Kingdom of Libya on 24 December 1951'
- `/ledger/36` https://en.wikipedia.org/wiki/French_West_Africa: confirmed (year), over-read. the 1904 sentences date the naming of the AOF and the Military Territories, not an acquisition: confidence should be 1
- `/ledger/64` https://en.wikipedia.org/wiki/French_West_Africa: confirmed. 'The French Empire was renamed the French Union on 27 October 1946'
- `/ledger/13` https://en.wikipedia.org/wiki/French_Africa: confirmed, incomplete. 'Porto-Novo(protectorate) (1863–1865, 1882)': the 1863-1865 phase is missing

### Area: The French Africa page has no area. Component infoboxes: French West Africa 4,689,000 km2 and French Equatorial Africa 2,500,000 km2 (both undated), Tunisia 155,000 km2 (text); with Algeria (2,381,741 km2, quoted by the author from French Algeria), Madagascar, French Morocco, Cameroon, Togo and Djibouti the sum is about 11.2 million km2 against Cliopatria's 11,095,480 km2 (1953-1955, without Fezzan) and 11,671,356 km2 (1946-1952, with Fezzan): ratio about 1.0. The author's notes quote the same component figures.

## kamerun: fix

### Findings

- `/keyframe_review/0/note` (applied by reviewer). The note says the Kamerun page 'gives no area or boundary', but its infobox gives 495,000 km2 (1910) and 790,000 km2 (1912). Evidence: Kamerun page infobox: '1910: 495,000 km2', '1912: 790,000 km2' (the German colony 1884-1916; no kamerun shape is alive in those years). Fix: Note extended: the infobox areas are the later German colony's, years in which this row has no shape. Validator re-run, valid.

### Gaps (confidence 1, for a gap-filler)

- `/ledger/1`: why the post ends in 1870 and the same patch passes to Cliopatria's German Africa row in 1871 (the page is silent on 1869-1871) (try https://en.wikipedia.org/wiki/Douala)

### Spot checks

- `/ledger/0` https://en.wikipedia.org/wiki/Kamerun: confirmed. 'The first German trading post in the Duala area on the Kamerun River delta was established in 1868 by the Hamburg trading company C. Woermann.'
- `/ledger/1` https://en.wikipedia.org/wiki/Kamerun: confirmed silent. nothing on 1869-1871, as the confidence-1 note says
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Kamerun: confirmed. 9.708 E 4.062 N lies inside the shape bbox 9.34-9.86 E, 3.89-4.34 N

### Area: The infobox areas (495,000 km2 in 1910, 790,000 km2 in 1912) are the German protectorate's; this row's only shapes are 1868-1870, so no comparison applies. Acknowledged in the keyframe note after the reviewer's fix.

## Cross-dossier matrix

- french-africa 1848 gain french-algeria -> french-algeria 1847 dissolve: matched. French Algeria dissolves to french-africa in December 1847
- french-africa 1849 gain nobody -> none: exception. counterpart nobody (also 1853, 1856, 1859, 1860, 1870, 1885, 1890, 1895 x2, 1904)
- french-africa 1868 gain Cotonou chiefdom -> none: exception. string counterpart, no dossier and not in the author's counterparts_needing_dossiers; dahomey has no 1868 loss
- french-africa 1880 gain Upper Senegal chiefdoms -> none: exception. generic string (also Guinea chiefdoms 1884, Ivory Coast and Upper Niger chiefdoms 1895, Chad local states 1900, Gadabuursi and Issa clans 1885)
- french-africa 1881 gain beylik-of-tunis -> beylik-of-tunis 1881 dissolve: matched. contest pair 1881-04/05 matches too
- french-africa 1882 gain kingdom-of-porto-novo -> kingdom-of-porto-novo 1863 loss: mismatch. Porto-Novo dossier gives its loss and dissolve to french-africa in 1863; French Africa page lists 1863-1865 and 1882
- french-africa 1885 gain merina-kingdom -> merina-kingdom 1885 loss: matched. Diego-Suarez, Treaty of Tamatave 17 December 1885
- french-africa 1890 gain dahomey -> dahomey 1890 loss: missing. dahomey records a loss to french-africa in October 1890 (First Franco-Dahomean War); french-africa has no event
- french-africa 1894 gain dahomey -> dahomey 1894 loss: matched. dahomey loss and dissolve 1894-01; french-africa gives no month
- french-africa 1894 gain Sultanate of Bangassou -> none: exception. listed by the author for af-08-x
- french-africa 1894 contest_start merina-kingdom -> merina-kingdom 1894 contest_start: matched. merina contest 1894-12 to 1895-10
- french-africa 1895 vassal_start merina-kingdom -> none: missing. merina-kingdom records no vassal_start (only rename 1896 and dissolve 1897); route to its group
- french-africa 1897 gain merina-kingdom -> merina-kingdom 1897 dissolve: matched. merina dissolves 1897 with successor french-africa
- french-africa 1897 vassal_start dar-al-kuti -> none: missing. dar-al-kuti records no 1897 protectorate; route to its group (af-08-x)
- french-africa 1899 gain Sultanate of Damagaram -> none: exception. listed by the author for af-03
- french-africa 1902 gain emirate-of-trarza -> emirate-of-trarza 1902 loss: matched. emirate-of-trarza loss and dissolve 1902-12; counterpart slug applied by the reviewer
- french-africa 1903 gain Kel Ahaggar -> none: exception. listed by the author for af-08-x
- french-africa 1905 gain Taganit confederation -> none: exception. listed by the author for af-08-x
- french-africa 1905 gain ottoman-tripolitania -> none: missing. ottoman-tripolitania has no loss to french-africa; french-africa's event is confidence 1 with no page
- french-africa 1907 gain republic-of-liberia -> republic-of-liberia 1907 loss: missing. Liberia records losses to french-africa in 1892-12 and 1907-09; french-africa has neither
- french-africa 1909 gain Emirate of Adrar -> none: exception. listed by the author for af-08-x
- french-africa 1911 gain wadai-empire -> wadai-empire 1912 dissolve: mismatch. wadai-empire: contest 1908-05 to 1911-10, occupation by french-africa 1909-06 to 1912, dissolve 1912; french-africa has only a 1911 gain at confidence 1
- french-africa 1911 loss german-africa -> none: exception. german-africa (af-08) not written yet; also the 1914-1922 contest and occupation events
- french-africa 1912 vassal_end dar-al-kuti -> dar-al-kuti 1912 loss: mismatch. dar-al-kuti records a loss to french-africa 1912-12; french-africa records only vassal_end, no gain
- french-africa 1912 gain morocco -> morocco 1912 loss: matched. 
- french-africa 1920 loss italian-africa -> none: exception. italian-africa (af-08) not written yet; also the Fezzan occupation 1943-1951
- french-africa 1940 loss free-french -> none: exception. free-french (eu-21) not written yet; also the 1943 gain
- french-africa 1942 loss british-africa -> none: missing. british-africa has no Djibouti event; and french-africa regains Djibouti from free-french in 1943, not from british-africa
- french-africa 1943 gain nazi-germany -> none: exception. nazi-germany (eu-21) not written yet; but no 1942 occupation in french-africa's own ledger (see fixes)
- french-africa 1956 loss morocco -> morocco 1956 gain: matched. 
- french-africa 1956 loss republic-of-tunisia -> none: exception. republic-of-tunisia (af-08) not written yet
- french-africa 1957 dissolve french-fifth-republic -> none: exception. french-fifth-republic (eu-22) not written yet
- sokoto-caliphate 1903 dissolve french-africa -> none: missing. sokoto-caliphate lists french-africa as successor for its Niger part (no year); french-africa has no event naming Sokoto
- kamerun 1870 dissolve german-africa -> none: exception. german-africa (af-08) not written yet

## Problems

- Context dossiers not written yet (counted as exceptions): german-africa, italian-africa, free-french, nazi-germany, republic-of-tunisia, french-fifth-republic, kingdom-of-libya, british-gold-coast.
- Dar al Kuti, Emirate of Trarza and Porto-Novo now have dossiers (dar-al-kuti, emirate-of-trarza, kingdom-of-porto-novo); the reviewer replaced the name strings with their slugs in french-africa.
- kamerun is a 1,897.5 km2 trading post continued by german-africa from 1871; the orchestrator may prefer to merge it into german-africa as its first phase (the author's suggestion).
- No page failed to load.
