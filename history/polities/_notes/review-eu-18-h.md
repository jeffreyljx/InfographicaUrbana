# Review of batch eu-18-h (2026-10-25)

Adversarial review of principality-of-bulgaria, cretan-state and albania. Validator: all three valid, 0 errors (one warning: unknown slug eastern-rumelia). Machine copy: history/notes/phase-b/reviews/eu-18-h.json.

## principality-of-bulgaria: fail

Area: infobox 122134 km2 (1915), Cliopatria 111800 km2, ratio 0.92; acknowledged. Kingdom_of_Bulgaria infobox; Cliopatria 1913-1915 shape; also 114,424 km2 on the World War I page (0.98). Principality page gives no area.

Findings (BLOCKING marks what makes the verdict fail; 'applied' means the reviewer made the change):

- `/ledger/17/region` (not applied): BLOCKING. The 1915 Ottoman cession is drawn on the wrong bank of the Maritsa: intersect(river Maritsa 20 km, Turkey) is the east-bank land (Edirne, Uzunkopru, Ipsala, Enez) that stayed Ottoman, while the land ceded lies west of the river, today in Greece (Didymoteicho, Orestiada) and Karaagac. Evidence: https://en.wikipedia.org/wiki/Bulgaria_during_World_War_I: the 6 September 1915 agreement 'granted Bulgaria the possession of the remaining Ottoman lands west of the river Maritsa', including 'a 2-kilometer stretch on its eastern bank', 'some 2,587 square kilometers'. The event's own note quotes 'west of the river Maritsa' but the region contradicts it. Fix: region = {"union": [{"minus": [{"intersect": [{"river": "Maritsa", "km": 20}, {"country": "Greece"}]}, {"cliopatria": "Principality of Bulgaria", "year": 1913}]}, {"intersect": [{"river": "Maritsa", "km": 2}, {"country": "Turkey"}]}], "text": "the Ottoman land west of the Maritsa with a 2-km strip of its eastern bank"}; keep confidence 2.
- `/ledger/22/region` (not applied): BLOCKING (same defect). The 1915 land is never lost again: the 1919 loss to Greece is (1913 shape minus 1919 shape) intersect Greece, which cannot contain land outside the 1913 shape, so a ledger-driven map keeps the Maritsa strip Bulgarian after Neuilly. Evidence: https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria: under Neuilly (27 November 1919) 'Bulgaria lost its Aegean coastline'; https://en.wikipedia.org/wiki/Bulgaria_during_World_War_I: Neuilly stipulated 'the return of all conquered territories'. Fix: Add the corrected /ledger/17 region to the union of the 1919-11 loss (counterpart first-hellenic-republic for the Greek part; the Turkish-bank strip may go to first-hellenic-republic too, Greece holding it 1920-1923).
- `/ledger (missing vassal_start 1878-7 and vassal_end 1908-10, counterpart ottoman-empire)` (not applied): BLOCKING. The principality is drawn fully independent from 1878, but it was under Ottoman suzerainty until the declaration of independence of 5 October 1908; the Ottoman dossier carries the relation and this dossier has no mirror. Evidence: https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria: 'the establishment of the Principality of Bulgaria (subject to Ottoman suzerainty) in 1878'; 'Bulgaria had only acknowledged the overlordship of the sultan formally'. ottoman-empire.json /ledger/192 vassal_start principality-of-bulgaria 1878-7 (c3) and /ledger/205 vassal_end principality-of-bulgaria 1908 (c2). Fix: Add {year 1878, month 7, type vassal_start, counterpart ottoman-empire, region {cliopatria Principality of Bulgaria, year 1880}, confidence 3, source Kingdom_of_Bulgaria} and {year 1908, month 10, type vassal_end, counterpart ottoman-empire, region {cliopatria Principality of Bulgaria, year 1885}, confidence 3, source Principality_of_Bulgaria}; say in the 1885 gain note that Eastern Rumelia stayed an Ottoman province under the prince (Tophane Agreement) inside the same relation.
- `/ledger/24` (not applied): Southern Dobruja is lost twice: /ledger/13 loses it in 1913, it is only occupied in 1916-1918 (/ledger/19, ended by /ledger/21), and /ledger/24 loses it again in 1919 without any gain in between. Evidence: Ledger order 13 (loss 1913-8), 19 (occupation_start 1916-9), 21 (occupation_end 1919-11), 24 (loss 1919-11); the 1913 and 1919 Cliopatria shapes both exclude Southern Dobruja (1913 to 1919 difference of about 7,600 km2 is all Greece and Macedonia per keyframe 8's note). Fix: Delete /ledger/24, or add the Treaty of Bucharest (7 May 1918) cession of Southern Dobruja as a 1918-5 gain from a page that states it (Treaty_of_Bucharest_(1918)) and keep /ledger/24.
- `/ledger/6, /ledger/11, /ledger/15` (not applied): Losses of land that was never gained: /ledger/15 returns Adrianople, Lozengrad and Lyule Burgas to the Ottomans in 1913-9 but /ledger/6 (Treaty of London) gains only the 1913 shape minus the 1885 shape; /ledger/11 loses Greek Macedonia that was only contested (/ledger/8, /ledger/12). Evidence: https://en.wikipedia.org/wiki/Balkan_Wars (quoted in /ledger/15): the regions 'reverted to the Ottomans', i.e. they had been ceded at London; ottoman-empire.json /ledger/218 gains Edirne and Kirklareli from principality-of-bulgaria in 1913-9. Fix: Union intersect((1912 shape minus 1913 shape), Turkey) into /ledger/6's region; drop /ledger/11 (the contest_end at /ledger/12 already closes Greek Macedonia) or gain that land at /ledger/6 too.
- `/ledger/2/region, /ledger/3/region, /wars/0/zones` (not applied): The Serbo-Bulgarian War zone is only Pirotski; the fighting was mainly inside Bulgaria. Evidence: https://en.wikipedia.org/wiki/Unification_of_Bulgaria: Serbia declared war 14 November 1885 and was defeated at the Battle of Slivnitsa (west of Sofia); Bulgarian forces then advanced to Pirot. Fix: Union {"place": "Slivnitsa", "km": 30} into the contest regions and the war zone.
- `/ledger/21/confidence` (applied): Confidence 2 for an end date (1919-11) that no page gives. Evidence: https://en.wikipedia.org/wiki/Bulgaria_during_World_War_I does not say when Bulgarian forces left Dobruja; https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria gives only the September 1916 seizure. Fix: Lowered to 1 and noted in the event (reviewer). A gap-filler should date the evacuation (late 1918).

Gaps for a gap-filler:

- `/keyframe_review/5-7`: Greek Eastern Macedonia (Kavala, Drama, Serres), in the 1916-1917 shapes (keyframe 7 note: 5,600 km2 of Greek Macedonia), has no occupation_start/_end with first-hellenic-republic (1916-8 to 1918-9). Try https://en.wikipedia.org/wiki/Macedonian_front
- `/keyframe_review/6, /ledger/21`: Northern Dobruja 1917-1918 and the Treaty of Bucharest of 7 May 1918; date of the evacuation of Dobruja. Try https://en.wikipedia.org/wiki/Treaty_of_Bucharest_(1918)
- `/keyframe_review/13`: The 1943 extension of the Bulgarian occupation zone (about 6,800 km2 in Greek Central Macedonia and western North Macedonia) has no event. Try https://en.wikipedia.org/wiki/Bulgaria_in_World_War_II
- `/ledger/26-29`: Months of the 1941 occupation (Bulgarian troops entered in April 1941) and of the 1944 withdrawal (confidence 1); the Kingdom page has only 1 March 1941 (Tripartite Pact) and 'In August 1944 ... troops were hastily withdrawn'. Try https://en.wikipedia.org/wiki/Bulgaria_in_World_War_II
- `/keyframe_review/9`: Reason for the 2,500 km2 drop between the 1919 and 1920 shapes along the southern border. Try https://en.wikipedia.org/wiki/Treaty_of_Neuilly-sur-Seine
- `/identity/rulers`: Rulers leave 1878-1879 (Russian provisional administration) and 1886-1887 (regency) uncovered. Try https://en.wikipedia.org/wiki/Principality_of_Bulgaria

Spot checks:

- `/ledger/1` on https://en.wikipedia.org/wiki/Unification_of_Bulgaria: confirmed: coup '18 September [O.S. 6 September] 1885'; Eastern Rumelia 'between the Balkan Mountains and the Rila and Rhodope Mountains'; Tophane Agreement 5 April 1886
- `/ledger/17` on https://en.wikipedia.org/wiki/Bulgaria_during_World_War_I: date confirmed (6 September 1915, 2,587 km2); region not on page: page says land WEST of the Maritsa plus a 2-km east-bank strip, region draws 20 km on the Turkish (east) side
- `/ledger/22` on https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria: confirmed: Neuilly 27 November 1919 (infobox), 'Bulgaria lost its Aegean coastline'
- `/ledger/25` on https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria: confirmed: 'On 7 September 1940 Bulgaria succeeded in negotiating the recovery of Southern Dobruja'
- `/ledger/19, /ledger/30 (read on the same page)` on https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria: confirmed: Dobruja seized September 1916; monarchy abolished 15 September 1946
- `/ledger/24 (same page)` on https://en.wikipedia.org/wiki/Kingdom_of_Bulgaria: on page ('Southern Dobruja was returned to the Kingdom of Romania') but a second loss of land already lost in 1913

## cretan-state: fail

Area: infobox None km2 (None), Cliopatria 5499 km2, ratio None; acknowledged. No infobox area; the author compares with admin-1 Kriti (gazetteer 6,828 km2; the island is about 8,300 km2): Cliopatria about 0.66 of the island, acknowledged and corrected to the whole of Kriti.

Findings (BLOCKING marks what makes the verdict fail; 'applied' means the reviewer made the change):

- `/ledger (missing vassal_start 1898-12 and vassal_end 1908-10, counterpart ottoman-empire)` (not applied): BLOCKING. The state's defining status, autonomy under Ottoman suzerainty, is not in the ledger: the author's note says the vassal_start 'belongs to the suzerain's dossier', but the mirror rule wants it in both ledgers, and the Ottoman dossier does not carry it either (it has a 1900 loss). Evidence: https://en.wikipedia.org/wiki/Cretan_State infobox 'Status: Autonomous state of the Ottoman Empire'; lead: 'under de jure suzerainty of the Ottoman Empire but with de facto independence secured by European Great Powers'; the Sultan gave up his rights at the Treaty of London (May 1913). The dossier's own /ledger/0 note says 'founded under Ottoman suzerainty'. Fix: Add {year 1898, month 12, type vassal_start, counterpart ottoman-empire, region {admin1 Kriti, country Greece}, confidence 3, source Cretan_State} and {year 1908, month 10, type vassal_end, counterpart ottoman-empire, same region, confidence 2, note: unilateral union of 7 October 1908, Ottoman rights renounced only 30 May 1913}; drop the sentence in notes that defers it to the suzerain.
- `/wars/0` (not applied): The Cretan Revolt (1897-1898) starts before the state's life (1898-12) and lists cretan-state as a belligerent in 1897. Evidence: Reviewer brief 2.2 (wars inside the life); identity start is 1898-12. Fix: Drop the war (keep it in the predecessors note) or set from 1898 and name the belligerent 'Cretan insurgents'.
- `/ledger/1` (not applied): Orchestrator decision, not a fault: the dissolve is at the unilateral union of 7 October 1908, which the page says Greece 'did not recognize ... internationally'; the page dates the state to 1913 (union 1 December 1913). The author flagged it and matched Cliopatria's Greek shape, which holds Crete from 1908. Evidence: https://en.wikipedia.org/wiki/Cretan_State infobox: 'Unilateral union with Greece: 7 October 1908', 'Treaty of London: 30 May 1913', 'Union with Greece: 1 December 1913'. Fix: Keep 1908 if the Greek dossier (eu-18) also takes Crete in 1908; otherwise move the dissolve to 1913-12 and extend the 1908 keyframe.

Gaps for a gap-filler:

- `/ledger`: The Great Powers' occupation/protection of the island inside the state's life: the page says troops of five powers occupied the key cities from late March-April 1897 and their withdrawal began after September 1906 (the author's notes say the pages are silent); no occupation or protectorate event. Try https://en.wikipedia.org/wiki/Cretan_State
- `/keyframe_review/0`: Island area for the infobox comparison (Cretan State page gives none). Try https://en.wikipedia.org/wiki/Crete

Spot checks:

- `/ledger/0` on https://en.wikipedia.org/wiki/Cretan_State: confirmed: 'Proclamation: 9 December 1898'; Ottoman forces expelled November 1898; Prince George arrived 13 or 21 December 1898
- `/ledger/1` on https://en.wikipedia.org/wiki/Cretan_State: confirmed: 'Unilateral union with Greece: 7 October 1908' (not recognised; formal union 1 December 1913)

## albania: thin

Area: infobox 30145 km2 (1916), Cliopatria 5420 km2, ratio 0.18; acknowledged. Principality_of_Albania infobox; Cliopatria 1916 and 1919 shapes are southern Albania only, marked wrong and replaced by the 1913 shape (27,676 km2, ratio 0.92).

Findings (BLOCKING marks what makes the verdict fail; 'applied' means the reviewer made the change):

- `/ledger/6, /ledger/13` (not applied): Italy's occupation starts only at 11 November 1918, although the page has Italy occupying Vlore in the 1914 passage, and Italy's dossier records a protectorate (vassal) over the Italian-held land from June 1917 to 1920: type and start disagree. Evidence: https://en.wikipedia.org/wiki/Principality_of_Albania: 'Italy occupied Vlore' (same passage as 'In late October 1914, Greek forces entered Albania'); kingdom-of-italy.json /ledger/13 vassal_start albania 1917-6 (c3, Ferrero's proclamation) and /ledger/17 vassal_end albania 1920. Fix: Add occupation_start kingdom-of-italy 1914 (Vlore 30 km, confidence 1 until a page dates it, December 1914) and agree the 1917-1920 status with eu-13 (vassal from 1917-6 over the Italian-held land, or occupation in both ledgers).
- `/ledger/16, /ledger/18` (not applied): 1939-1943 is an occupation here but a vassal tie in Italy's dossier (kingdom-of-italy.json /ledger/23 and /ledger/32); the mirror rule wants the same type in both. Evidence: https://en.wikipedia.org/wiki/Albania_in_World_War_II: Italy invaded on 7 April 1939, parliament voted on 12 April 'to unite the country with Italy' in 'personal union'; Italy had set Albania up as a 'protectorate or puppet state'. Fix: Change to vassal_start/vassal_end with counterpart kingdom-of-italy (and update the 1939 keyframe note), or have eu-13 change Italy's side; one of the two.
- `/ledger/3, /ledger/6, /ledger/7, /ledger/8` (not applied): Overlapping occupations 1918-1920: Italy's region is the whole 1913 shape while France (Korce, Shkoder), Serbia (Kukes, Diber) and Greece (Gjirokaster county) occupy parts of it at the same time; the page has Greece holding only 'a sliver' by 11 November 1918. Evidence: https://en.wikipedia.org/wiki/Principality_of_Albania: 'When the war ended on November 11, 1918, Italy's army had occupied most of Albania'; 'French forces occupied Korce and Shkoder'; 'Serbia held much of the country's northern mountains'; 'Greece occupied a sliver of land within Albania's 1913 borders'. Fix: Italy's 1918-11 region = 1913 shape minus the French, Serbian and Greek regions; shrink the Greek region (or end the Gjirokaster occupation when Italy and France took the south, with a page).
- `/ledger/4/region` (not applied): Austria-Hungary occupies the whole 1913 shape, overlapping Italian Vlore and the Greek south; the page says 'about two-thirds of the country', with Bulgarian forces. Evidence: https://en.wikipedia.org/wiki/Principality_of_Albania: 'Austro-Hungarian and Bulgarian forces then occupied about two-thirds of the country.' Fix: Restrict to northern and central Albania (admin1 Shkoder, Lezhe, Durres, Tirane, Elbasan, Kukes, Diber) and keep confidence 1.

Gaps for a gap-filler:

- `/ledger/4`: Date of the Austro-Hungarian and Bulgarian occupation (January-February 1916) and the Bulgarian share, absent from both this dossier and the Bulgarian one. Try https://en.wikipedia.org/wiki/Albania_during_World_War_I
- `/ledger/9-11`: Dates of the Greek, French and Serbian withdrawals (confidence 1). Try https://en.wikipedia.org/wiki/Albania_during_World_War_I
- `/ledger/17, /ledger/20, /keyframe_review/7`: Extent of Greater Albania beyond Kosovo (western Macedonia, Ulcinj-Plav-Gusinje) and northern Kosovo left to Serbia; date Kosovo returned (confidence 1). Try https://en.wikipedia.org/wiki/Greater_Albania
- `/ledger/13`: Italy kept Sazan island after September 1920 ('withdrew its forces from all of Albania except Sazan Island'); no loss event. Try https://en.wikipedia.org/wiki/Sazan_Island

Spot checks:

- `/ledger/3` on https://en.wikipedia.org/wiki/Principality_of_Albania: confirmed: 'In late October 1914, Greek forces entered Albania'
- `/ledger/13` on https://en.wikipedia.org/wiki/Principality_of_Albania: confirmed: 'In September 1920, after the Battle of Vlora' Italy 'withdrew its forces from all of Albania except Sazan Island'
- `/ledger/16` on https://en.wikipedia.org/wiki/Albania_in_World_War_II: confirmed: invasion 7 April 1939, union vote 12 April
- `/ledger/21` on https://en.wikipedia.org/wiki/Albania_in_World_War_II: confirmed: 'liberated Albania from German occupation on 29 November 1944'
- `/ledger/17, /ledger/19 (same page)` on https://en.wikipedia.org/wiki/Albania_in_World_War_II: confirmed: Kosovo united in spring 1941 (no month, c2 right); Germany from September 1943

## Cross-dossier matrix

- principality-of-bulgaria 1878 vassal_start (missing) / ottoman-empire -> ottoman-empire 1878 vassal_start: mismatch. Ottoman /ledger/192 has the relation; Bulgaria has only its found event.
- principality-of-bulgaria 1908 vassal_end (missing) / ottoman-empire -> ottoman-empire 1908 vassal_end: mismatch. Bulgaria has only the rename.
- principality-of-bulgaria 1885 gain / eastern-rumelia -> eastern-rumelia None None: exception. No dossier; listed in counterparts_needing_dossiers (eu-18-x). Ottoman /ledger/202 has a vassal_end 'Eastern Rumelia' in 1885 (c1).
- principality-of-bulgaria 1913 gain / ottoman-empire -> ottoman-empire 1913 loss: matched. Ottoman /ledger/216 (1913-5, Western Thrace only); Bulgaria's land also covers Pirin Macedonia and should add the Thracian land later returned.
- principality-of-bulgaria 1913 loss / ottoman-empire -> ottoman-empire 1913 gain: matched. Ottoman /ledger/218 (1913-9, Edirne and Kirklareli).
- principality-of-bulgaria 1913 loss / first-hellenic-republic -> first-hellenic-republic None None: exception. Owned by eu-18 (parallel part), not written yet; the Bulgarian event is itself questionable (land only contested).
- principality-of-bulgaria 1913 loss / united-principalities-of-moldavia-and-wallachia -> united-principalities-of-moldavia-and-wallachia None None: exception. eu-18 parallel part, not written yet.
- principality-of-bulgaria 1915 gain / ottoman-empire -> ottoman-empire 1915 loss: missing. Ottoman dossier (me-10) has no 1915 cession to Bulgaria; Bulgarian region also wrong (east bank).
- principality-of-bulgaria 1915 occupation_start / serbs -> serbs None None: exception. eu-18 parallel part, not written yet (also /ledger/20 occupation_end 1918).
- principality-of-bulgaria 1916 occupation_start / united-principalities-of-moldavia-and-wallachia -> united-principalities-of-moldavia-and-wallachia None None: exception. Not written yet; end at /ledger/21 1919-11 (now c1).
- principality-of-bulgaria 1919 loss / first-hellenic-republic -> first-hellenic-republic None None: exception. Not written yet.
- principality-of-bulgaria 1919 loss / yugoslavia -> yugoslavia None None: exception. eu-21 has not run.
- principality-of-bulgaria 1919 loss / kingdom-of-romania -> kingdom-of-romania None None: exception. eu-21 has not run; the Bulgarian event is a double loss (see fixes).
- principality-of-bulgaria 1940 gain / kingdom-of-romania -> kingdom-of-romania None None: exception. eu-21 has not run.
- principality-of-bulgaria 1941 occupation_start / first-hellenic-republic -> first-hellenic-republic None None: exception. Not written yet (end 1944).
- principality-of-bulgaria 1941 occupation_start / yugoslavia -> yugoslavia None None: exception. eu-21 has not run (end 1944).
- cretan-state 1898 found (vassal_start missing) / ottoman-empire -> ottoman-empire 1900 loss: mismatch. Ottoman /ledger/204 loses Crete in 1900 at c1 (Cliopatria's year); it should be a vassal_start cretan-state 1898-12 in both ledgers (me-10 and this dossier).
- cretan-state 1908 dissolve / first-hellenic-republic -> first-hellenic-republic None None: exception. Greek dossier (eu-18) not written yet; it must take Crete in the same year this dossier ends (1908 or 1913).
- albania 1913 gain / ottoman-empire -> ottoman-empire 1913 loss: matched. Ottoman /ledger/217 (1913-8, credits the Treaty of Bucharest); Albania 1913-7.
- albania 1914 occupation_start / first-hellenic-republic -> first-hellenic-republic None None: exception. Not written yet.
- albania 1916 occupation_start / austria-hungary -> austria-hungary None None: exception. eu-20 has not run.
- albania 1918 occupation_start / kingdom-of-italy -> kingdom-of-italy 1917 vassal_start: mismatch. Italy /ledger/13 vassal_start albania 1917-6; type differs and the dates are 17 months apart; Italy held Vlore from 1914 in neither ledger.
- albania 1920 occupation_end / kingdom-of-italy -> kingdom-of-italy 1920 vassal_end: mismatch. Year matches, type differs.
- albania 1918 occupation_start / french-third-republic -> french-third-republic None None: exception. eu-20 has not run.
- albania 1918 occupation_start / serbia -> serbia None None: exception. eu-21 has not run.
- albania 1939 occupation_start / kingdom-of-italy -> kingdom-of-italy 1939 vassal_start: mismatch. Italy /ledger/23; same year, type differs.
- albania 1943 occupation_end / kingdom-of-italy -> kingdom-of-italy 1943 vassal_end: mismatch. Italy /ledger/32; same month, type differs.
- albania 1941 gain / yugoslavia -> yugoslavia None None: exception. eu-21 has not run.
- albania 1943 occupation_start / nazi-germany -> nazi-germany None None: exception. eu-21 has not run (end 1944-11).
- albania 1944 loss / yugoslav-partisans -> yugoslav-partisans None None: exception. eu-21 has not run.

## Problems

- ottoman-empire (me-10) needs: a vassal_start/vassal_end with cretan-state 1898-12..1908-10 (or 1913) instead of the c1 'loss cretan-state' of 1900, and a 1915-9 loss to principality-of-bulgaria (the strip west of the Maritsa).
- kingdom-of-italy (eu-13) and albania disagree on type (vassal vs occupation) for 1917/1918-1920 and 1939-1943; the orchestrator should pick one for both.
- Neighbour dossiers present for cross-checks: ottoman-empire, kingdom-of-italy, republic-of-turkey, kingdom-of-great-britain (the last two have no events touching this batch); all other Context polities are unwritten (eu-18 parallel parts, eu-20, eu-21, eu-22).
- No page failed to load for the reviewer.
