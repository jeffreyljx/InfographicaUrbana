# Review of batch eu-17-b (2026-10-31)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Validator: 0 errors on all five dossiers before and after the reviewer's fixes (warnings: west-ukrainian-people-s-republic has no dossier; Franz Josef Land not in the gazetteer). Machine copy: history/notes/phase-b/reviews/eu-17-b.json.

## russian-republic: pass

Found/dissolve dates and capital on the page; predecessor mirror (russian-empire dissolve 1917-3) and successor mirror (RSFSR found 1917-11 cp russian-republic); the 1918/1919 'wrong' verdicts against the RSFSR dossier's own 1918-19 keyframes; certainty covers the life. Could not break it. Lead for the RSFSR owner, not a fault here: the Russian Civil War page says 'For a time, Central Asia was completely cut off from Red Army forces in Siberia' (the Turkestan cells Cliopatria drops in 1918).

Area: infobox None km2 (year None), Cliopatria 22278223 km2, ratio None, acknowledged True. infobox has no area (confirmed); the 1918-19 shapes are verdict wrong (Soviet Russia's land, drawn by the RSFSR dossier)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Russian_Republic: confirmed: 'proclamation by the Russian Provisional Government on 1 September (14 September, N.S.) 1917'
- `/ledger/1` https://en.wikipedia.org/wiki/Russian_Republic: confirmed: 'dissolved after the Bolsheviks seized power by force on 7 November 1917'
- `/keyframe_review/1/note` https://en.wikipedia.org/wiki/Treaty_of_Brest-Litovsk: confirmed: signed 17:50 on 3 March 1918; '34% of its population, 54% of its industrial land'
- `/keyframe_review/2/correction` https://en.wikipedia.org/wiki/Russian_Civil_War: confirmed: Kazan recaptured 8 September 1918, Ufa retaken 13 March (1919)

## ukrainian-people-s-republic: fail

Area: infobox 860000 km2 (year None), Cliopatria 522688 km2, ratio 0.61, acknowledged True. 

Findings:
- `/ledger/0/region, /ledger/3/region, /keyframe_review/0/correction` (applied by reviewer): The region Ukraine minus (Eastern Galicia, Transcarpathia, Bukovina, Budjak) still contained Crimea, although the note and the correction's text say Crimea is out. Evidence: UPR page: the Third Universal 'included the governorates of ... Kherson and Taurida (except of Crimea)'; Ukrainian State page: 'with the exception of most of West Ukraine, Budjak and Crimea'. Fix: Reviewer added {"region": "Crimea"} to the subtracted union in all three places; dossier re-validated (0 errors).
- `/ledger (after /ledger/1 and /ledger/7)` (for the author): No loss event mirrors the Ukrainian SSR's gains from this state; the dossier records only contest_start (Kyiv 150 km in January 1918, the whole 1919 claim from February 1919). Evidence: ukrainian-soviet-socialist-republic ledger: 1918-1 gain of Dnipropetrovsk, Zaporizhzhia and Poltava (conf 3), 1918-2 gain of Kyiv (conf 3), 1919-1 gains of Kharkiv and Poltava/Yekaterinoslav (conf 3), 1919-2 gain of Kyiv (conf 3), 1919-3 gain of Ukraine east of Galicia and Volhynia (conf 2), all with counterpart ukrainian-people-s-republic. UPR page: 'On 5 February, the Bolshevik troops captured Kyiv'. Fix: Add loss events to ukrainian-soviet-socialist-republic for 1918-1/1918-2 (left bank and Kyiv; Civil War page 'captured the city on 26 January') and 1919-1 to 1919-3 (left bank, Kyiv on 5 February 1919, then the land east of the Zbruch-Volhynia pocket), matching the UkrSSR regions; keep contest only for the front zone. The 1918-3 return is already the gain at /ledger/3.
- `/keyframe_review/1 to /keyframe_review/2` (for the author): Between the 1919 keyframe (verdict ok, the full 522,688 km2 claim with Eastern Galicia) and the 1920 keyframe (four 60 km circles round the temporary capitals) the land falls by about 90 percent with no loss event; only the February 1919 contest_start covers it. Evidence: UPR page: 'the Galician army was defeated by Polish forces and forced to retreat to the confluence of Dniester and Zbruch river' (1919) and the Treaty of Warsaw (April 1920) 'established the Polish-Ukrainian border along the Zbruch'. Both sentences are on a page the author already cites. Fix: Add a 1919-7 loss of Eastern Galicia (the region merged at /ledger/7) to second-polish-republic (conf 2, UPR page), the Soviet-side losses above, and consider marking /keyframe_review/1 'adjust' with a note that the 1919 shape is the claim held only in early 1919.
- `/ledger/5/note` (for the author): The quoted sentence 'On 29 April, the All-Ukrainian Agrarian Congress elected' Skoropadsky is not the page's wording (date is right). Evidence: Ukrainian State page describes a landowners' congress in Kyiv on 29 April where Skoropadsky 'was elected the Hetman of all Ukraine'. Fix: Quote the page's own sentence.

Gaps for a gap-filler:
- `/keyframe_review/2`: effective extent of the UPR in 1920-21 (the four-circle pocket is the author's reading of the infobox capitals) (try https://en.wikipedia.org/wiki/Kiev_offensive_(1920))

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Ukrainian_People%27s_Republic: confirmed: Third Universal 'adopted on 20 November 1917'
- `/ledger/3` https://en.wikipedia.org/wiki/Treaty_of_Brest-Litovsk: confirmed: 3 March 1918, Russia renounced claims to Ukraine; treaty with Ukraine night of 8-9 February
- `/ledger/4` https://en.wikipedia.org/wiki/Ukrainian_People%27s_Republic: confirmed: 'on 1 March 1918 the Ukrainian army ... entered Kyiv'
- `/ledger/5` https://en.wikipedia.org/wiki/Ukrainian_State: confirmed date (Established 29 April 1918); quoted wording differs from the page
- `/ledger/8` https://en.wikipedia.org/wiki/Ukrainian_People%27s_Republic: confirmed: 'On 5 February, the Bolshevik troops captured Kyiv'
- `/ledger/2` https://en.wikipedia.org/wiki/Russian_Civil_War: confirmed: 'the Bolsheviks captured the city on 26 January'

## republics-of-the-soviet-union: fix

Area: infobox None km2 (year None), Cliopatria 21477746 km2, ratio None, acknowledged True. the Wikipedia field is a list page of the 1956-91 union republics with no area for a 1920-21 bloc

Findings:
- `/ledger/5/region` (applied by reviewer): The 1920-7 gain drew all of Belarus while its own note says only the eastern part (573 of 925 cells) lies in the shape; the Polish-held west stayed Polish at Riga. Evidence: Republics page table: Byelorussian SSR '31 July 1920' (date confirmed); Russian Civil War page: the Peace of Riga 'split disputed territories in Belarus and Ukraine'. Fix: Reviewer set the region to intersect(Belarus, Cliopatria Republics of the Soviet Union 1920) with a text; re-validated (0 errors).

Gaps for a gap-filler:
- `/ledger/0`: a page dating a 1920 start of the bloc (conf 1, Cliopatria's year) (try https://en.wikipedia.org/wiki/Russian_Soviet_Federative_Socialist_Republic)
- `/ledger/8`: a page dating the 1921 end (conf 1, Cliopatria's year) (try https://en.wikipedia.org/wiki/Treaty_on_the_Creation_of_the_USSR)

Spot checks:
- `/ledger/4` https://en.wikipedia.org/wiki/Republics_of_the_Soviet_Union: confirmed: Azerbaijan SSR 28 April 1920
- `/ledger/5` https://en.wikipedia.org/wiki/Republics_of_the_Soviet_Union: confirmed date 31 July 1920; region narrowed by reviewer
- `/ledger/7` https://en.wikipedia.org/wiki/Republics_of_the_Soviet_Union: confirmed: Armenian SSR 2 December 1920
- `/ledger/9` https://en.wikipedia.org/wiki/Republics_of_the_Soviet_Union: confirmed: Georgian SSR 25 February 1921
- `/ledger/6` https://en.wikipedia.org/wiki/Russian_Civil_War: confirmed: Wrangel evacuated to Constantinople in November 1920

## provisional-priamurye-government: thin

Area: infobox None km2 (year None), Cliopatria 344044 km2, ratio None, acknowledged True. 

Findings:
- `/identity/rulers/1, /identity/rulers/2` (applied by reviewer): Diterikhs and Pepelyayev cited no page. Evidence: Priamurye page: the Merkulovs 'were replaced by Mikhail Diterikhs'; 'The Ayano-Maysky District was controlled by Anatoly Pepelyayev'. Fix: Reviewer added the Provisional Priamurye Government page as source; re-validated (0 errors).

Gaps for a gap-filler:
- `/ledger/0`: the date Khabarovsk was taken (conf 1, no month; the event sorts before the May 1921 founding, and the 1921 keyframe draws Khabarovsk from May) (try https://en.wikipedia.org/wiki/Far_Eastern_Republic)
- `/keyframe_review/1`: the loss of Khabarovsk back to the Far Eastern Republic in early 1922: the 1922 keyframe keeps Khabarovsk all year and no loss event exists (try https://en.wikipedia.org/wiki/Battle_of_Volochayevka)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Provisional_Priamurye_Government: confirmed: 'between May 27, 1921 and June 16, 1923'; coup 'started on May 23, 1921'
- `/ledger/2` https://en.wikipedia.org/wiki/Provisional_Priamurye_Government: confirmed: 'The Merkulovs were deposed in June 1922 by the Priamurye Zemsky Sobor'
- `/ledger/3` https://en.wikipedia.org/wiki/Far_Eastern_Republic: confirmed: 'retook Vladivostok on 25 October 1922'
- `/ledger/4` https://en.wikipedia.org/wiki/Provisional_Priamurye_Government: confirmed: Ayano-Maysky District, 'surrender in June 1923'

## union-of-soviet-socialist-republics: fail

Area: infobox 22402200 km2 (year None), Cliopatria 21979888 km2, ratio 0.98, acknowledged True. infobox undated; compared with the 1953-1968 shape; the author compares every shape

Findings:
- `/ledger/23` (applied by reviewer): The loss of Ukraine to Germany was dated 1942 (conf 1, 'page silent'), but the cited page dates the fall of Kiev to September 1941; the region also lost Crimea a year before the July 1942 Crimea event. Evidence: Eastern Front (World War II) page: 'Kiev was surrendered on 19 September' and 'On 26 September, the Soviet forces east of Kiev surrendered and the Battle of Kiev ended'; 'held out until 3 July 1942' (Sevastopol). Fix: Reviewer set year 1941, month 9, confidence 2, region Ukraine minus Crimea, and rewrote the note with the page's sentences; order unchanged (between 1941-8 and 1942-7); re-validated (0 errors).
- `/ledger/29/region` (applied by reviewer): The 1944 Baltic gain at confidence 3 drew all three states, while the page says 'most' and the Courland Pocket is gained again at /ledger/38 in May 1945. Evidence: Occupation of the Baltic states page: 'In 1944, the Soviet Union recaptured most of the Baltic states'; Courland 'capitulating on 10 May 1945'. Fix: Reviewer set the region to (Estonia + Latvia + Lithuania) minus Courland; re-validated.
- `/keyframe_review/0 to /keyframe_review/10, /ledger/2-6, /ledger/31` (for the author): Tuva (1922-1944) and the Bukhara and Khorezm republics (1922-1924) are left inside the keyframes as direct Soviet land (K0-K3 verdict ok) while the ledger makes them vassals and their own dossiers draw the same cells; their absorption (1924-10, 1944-10) has no gain event. Evidence: tuvan-people-s-republic keyframes 1921-1931 and 1932-1944, dissolve 1944-10 cp this state; bukharan- and khorezm-people-s-soviet-republic keyframes 1920-1924, dissolve 1924-10 cp this state; RSFSR dossier gains Tuva 1944-10. Tuvan PR page: a 1925 treaty said the Soviet government 'did not consider Tannu-Tuva as its territory'; absorption 'ending 23 years of independence'. The dossier's own convention removes foreign occupied land from keyframes. Fix: Subtract {"admin1": "Tuva", "country": "Russia"} from K0-K10 (K0-K3 become adjust) and the Bukhara and Khorezm regions from K0 and the 1924 part of K1; add gain events 1924-10 cp bukharan-people-s-soviet-republic and khorezm-people-s-soviet-republic and 1944-10 cp tuvan-people-s-republic beside the vassal_end events.
- `/ledger/1` (for the author): Gain from the Far Eastern Republic dated December 1922, but the Far Eastern Republic had already merged into Soviet Russia on 15 November 1922; no mirror exists. Evidence: Far Eastern Republic page: 'Soviet Russia absorbed the Far Eastern Republic on 15 November 1922'; far-eastern-republic ledger: 1922-11 merge cp russian-soviet-federative-socialist-republic; RSFSR ledger: 1922-11 merge cp far-eastern-republic. Fix: Drop /ledger/1 and mark /keyframe_review/0 adjust = union(Cliopatria USSR 1922, the /ledger/1 region) with a note that the Far East came in with the RSFSR at the founding; or keep a gain with counterpart russian-soviet-federative-socialist-republic.
- `/ledger/35` (for the author): Petsamo gain dated 1945 on Cliopatria's year (conf 1); the group's RSFSR dossier dates the same land 1944-10 from a page. Evidence: russian-soviet-federative-socialist-republic ledger: 1944-10 gain cp republic-of-finland, Petsamo (Petsamo-Kirkenes offensive page); Eastern Front infobox 'Finland cedes Petsamo' (no date). Fix: Re-date to 1944 (September armistice or October offensive) citing a page that dates it, and add the Karelian Isthmus return of the same armistice (see next).
- `/wars, /ledger (1941 and 1944)` (for the author): The Continuation War (1941-1944) is missing: Finland's 1941 reconquest of the Karelian Isthmus and Ladoga Karelia and the 1944 Soviet return are drawn only as a contest with nazi-germany. Evidence: Eastern Front infobox lists the Finnish cessions; RSFSR dossier: 1944-9 gain of the Vyborg land via the Karelo-Finnish SSR; /ledger/19's contest names nazi-germany for the whole 1941-42 front. Fix: Add the Continuation War (belligerents republic-of-finland, nazi-germany) with a 1941 loss and a 1944-9 gain of the Isthmus and Ladoga Karelia, counterpart republic-of-finland.
- `/ledger (1941-7 and 1944-8)` (for the author): Romania's 1941 reconquest of Bessarabia and Northern Bukovina and the 1944 Soviet return are missing; the Moldova cells leave between K7 and K8 and return in K10 with counterpart nazi-germany only. Evidence: K10 note: '+4,960 cells ... Moldova 98'; /ledger/15 gains the same land from kingdom-of-romania in 1940; /ledger/30 returns it from nazi-germany. Fix: Add loss 1941-7 and gain 1944-8 with counterpart kingdom-of-romania (a page such as Operation Munchen / Jassy-Kishinev Offensive).
- `/ledger (1945-8), /keyframe_review/11` (for the author): The 1939 gain (/ledger/11, intersect of Second Polish Republic 1938 and USSR 1940) includes the Bialystok and Przemysl areas, which K11 onward removes with modern Poland; no loss explains it. Evidence: Shape arithmetic: /ledger/11 region vs K11 'minus Poland'; allied-occupied-germany uses republic-of-poland as the post-war Polish slug. Fix: Add a 1945-8 loss of the Bialystok area to republic-of-poland (Polish-Soviet border agreement), conf by the page found.
- `/ledger/33, /ledger/34, /ledger/51` (for the author): The occupation of the Soviet zone 1945-1949 and the Kaliningrad gain name nazi-germany, which ended in 1945; the occupation_end of 1949 is four years after its counterpart's life. Evidence: allied-occupied-germany dossier (1945-6 to 1949-10): occupation_start 1945-6 and occupation_end 1949-10 cp union-of-soviet-socialist-republics; loss of Kaliningrad 1945-8 cp union-of-soviet-socialist-republics. Fix: Use counterpart allied-occupied-germany on /ledger/33 and /ledger/51 (months 6 and 10) and on /ledger/34 (1945-8).
- `/ledger/40, /ledger/41, /ledger/46, /ledger/47` (for the author): The occupation of Manchuria and Inner Mongolia to 1946 names manchukuo and mengjiang, which both ended in August 1945; their land passed to the Republic of China. Evidence: manchukuo ledger: 1945-8 loss cp republic-of-china and dissolve; mengjiang ledger: 1945-8 dissolve cp republic-of-china, and no event naming this state. Soviet-Japanese War infobox: 'Soviet occupation of Inner Mongolia and Manchuria until 1946'. Fix: Use counterpart republic-of-china for both occupations (start and end); keep the contest with manchukuo/empire-of-japan for August 1945.
- `/ledger/32, /ledger/49` (for the author): One free-text occupation of all of Romania, Bulgaria, Hungary, Czechia, Slovakia and Austria from 1945 to 1947 (conf 1): Austria's Soviet zone was eastern Austria only and lasted to 1955, and the dates differ per country. Evidence: Both events are confidence 1 'page silent'; the counterpart is not a dossier, so no owner can mirror it. Fix: Split per country with dossier counterparts (kingdom-of-romania, czechoslovakia, the Austrian and Hungarian dossiers) and their own dates, or list the whole block as a gap.

Gaps for a gap-filler:
- `/ledger/8`: a page dating the Franz Josef Land annexation (1926 decree) (try https://en.wikipedia.org/wiki/Franz_Josef_Land)
- `/ledger/30`: a page for the 1944 clearing of Belarus and Ukraine (conf 1) (try https://en.wikipedia.org/wiki/Operation_Bagration)
- `/ledger/34, /ledger/36`: dates for Kaliningrad and Carpathian Ruthenia (conf 1) (try https://en.wikipedia.org/wiki/Kaliningrad_Oblast)
- `/ledger/50`: the end of the Soviet occupation of North Korea (conf 1, 1948) (try https://en.wikipedia.org/wiki/Soviet_Civil_Administration)
- `/identity/rulers`: ruler strip omitted (try https://en.wikipedia.org/wiki/List_of_leaders_of_the_Soviet_Union)
- `/ledger (1940-41, 1944-56)`: Hanko and Porkkala leases, Port Arthur and Dalian (to 1955) (try https://en.wikipedia.org/wiki/Porkkala_Naval_Base)

Spot checks:
- `/ledger/9` https://en.wikipedia.org/wiki/Molotov%E2%80%93Ribbentrop_Pact: confirmed: 'On 17 September, the Red Army invaded Poland'
- `/ledger/15` https://en.wikipedia.org/wiki/Molotov%E2%80%93Ribbentrop_Pact: confirmed: 'Between 28 June and 4 July, the Soviet Union occupied and annexed Bessarabia, Northern Bukovina and the Hertsa region'
- `/ledger/16` https://en.wikipedia.org/wiki/Occupation_of_the_Baltic_states: confirmed: Lithuania 3 August, Latvia 5 August, Estonia 6 August 1940
- `/ledger/24` https://en.wikipedia.org/wiki/Eastern_Front_(World_War_II): confirmed: Sevastopol 'held out until 3 July 1942'
- `/ledger/28` https://en.wikipedia.org/wiki/Eastern_Front_(World_War_II): confirmed: Kiev captured early in November (1943)
- `/ledger/23` https://en.wikipedia.org/wiki/Eastern_Front_(World_War_II): mis-dated (conf 1): page gives Kiev surrendered 19 September 1941; fixed by reviewer
- `/ledger/39` https://en.wikipedia.org/wiki/Soviet%E2%80%93Japanese_War: confirmed: invasion 9 August 1945 on three fronts
- `/ledger/54` https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union: confirmed: Lithuania 11 March 1990
- `/ledger/57` https://en.wikipedia.org/wiki/Occupation_of_the_Baltic_states: confirmed: recognition 6 September 1991
- `/ledger/7` https://en.wikipedia.org/wiki/Far_Eastern_Republic: confirmed: northern Sakhalin under Japanese occupation 'until 1925'

## Cross-dossier matrix

- russian-republic 1917 found cp russian-empire -> russian-empire 1917 dissolve: **matched** Empire dissolves 1917-3, republic proclaimed 1917-9 (the page's date); same year
- ukrainian-people-s-republic 1917 found cp russian-republic -> russian-republic 1917 successor: **matched** russian-republic lists the UPR as successor
- ukrainian-people-s-republic 1918 gain cp russian-soviet-federative-socialist-republic -> russian-soviet-federative-socialist-republic 1918 loss: **mismatch** UPR gains Ukraine (1918-3) and Polesia from the RSFSR; the RSFSR's 1918-3 loss of Ukraine and Belarus names german-empire as counterpart
- ukrainian-people-s-republic 1919 merge cp west-ukrainian-people-s-republic -> None None None: **exception** no dossier; listed in counterparts_needing_dossiers
- ukrainian-soviet-socialist-republic 1918 gain cp ukrainian-people-s-republic -> ukrainian-people-s-republic None loss: **missing** UkrSSR gains 1918-1 and 1918-2 (conf 3) have no UPR loss; UPR has contest_start 1918-1 only
- ukrainian-soviet-socialist-republic 1919 gain cp ukrainian-people-s-republic -> ukrainian-people-s-republic None loss: **missing** UkrSSR gains 1919-1 (x2), 1919-2, 1919-3 have no UPR loss; UPR has contest_start 1919-2 over the whole claim
- republics-of-the-soviet-union 1920 found cp russian-soviet-federative-socialist-republic -> russian-soviet-federative-socialist-republic None None: **exception** umbrella bloc over the RSFSR and SSR dossiers, which keep their own land
- republics-of-the-soviet-union 1920 gain cp emirate-of-bukhara -> emirate-of-bukhara 1920 contest_start/contest_end: **exception** umbrella duplicate: the land passes to bukharan-people-s-soviet-republic (found cp emirate-of-bukhara)
- republics-of-the-soviet-union 1920 gain cp khanate-of-khiva -> khanate-of-khiva None None: **exception** umbrella duplicate: the land passes to khorezm-people-s-soviet-republic (found cp khanate-of-khiva)
- republics-of-the-soviet-union 1920 gain cp azerbaijan-democratic-republic -> None None None: **exception** eu-19 not run; azerbaijan-soviet-socialist-republic found 1920-4 cp azerbaijan-democratic-republic carries the land
- republics-of-the-soviet-union 1920 gain cp second-polish-republic -> None None None: **exception** eu-21 not run
- republics-of-the-soviet-union 1920 gain cp armenia -> None None None: **exception** eu-19 not run; armenian-soviet-socialist-republic found 1920-11 cp armenia
- republics-of-the-soviet-union 1921 gain cp georgia -> None None None: **exception** eu-19 not run; georgian-soviet-socialist-republic found 1921-2 cp georgia
- provisional-priamurye-government 1921 gain cp far-eastern-republic -> far-eastern-republic 1921 loss: **matched** both conf 1, no month
- provisional-priamurye-government 1921 found cp far-eastern-republic -> far-eastern-republic 1921 loss: **matched** May 1921 both sides
- provisional-priamurye-government 1922 loss cp far-eastern-republic -> far-eastern-republic 1922 gain: **matched** October 1922 both sides
- provisional-priamurye-government 1923 dissolve cp None -> russian-soviet-federative-socialist-republic 1923 gain: **matched** RSFSR gains the Okhotsk pocket 1923-6 cp provisional-priamurye-government
- union-of-soviet-socialist-republics 1922 found cp republics-of-the-soviet-union -> republics-of-the-soviet-union 1921 dissolve: **matched** 
- union-of-soviet-socialist-republics 1922 gain cp far-eastern-republic -> far-eastern-republic 1922 merge: **mismatch** FER merged into the RSFSR on 15 November 1922; no FER event names the USSR
- union-of-soviet-socialist-republics 1922 vassal_start cp bukharan-people-s-soviet-republic -> bukharan-people-s-soviet-republic None None: **missing** BPSR has no vassal event; its dissolve 1924-10 names the USSR (matched for vassal_end)
- union-of-soviet-socialist-republics 1922 vassal_start cp khorezm-people-s-soviet-republic -> khorezm-people-s-soviet-republic None None: **missing** same as Bukhara; dissolve 1924-10 names the USSR
- union-of-soviet-socialist-republics 1922 vassal_start cp tuvan-people-s-republic -> tuvan-people-s-republic None None: **missing** TPR has no vassal event; its dissolve 1944-10 names the USSR (matched for vassal_end, but the USSR has no gain)
- union-of-soviet-socialist-republics 1925 gain cp empire-of-japan -> empire-of-japan 1925 occupation_end: **matched** northern Sakhalin
- union-of-soviet-socialist-republics 1939 gain cp second-polish-republic -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1940 gain cp republic-of-finland -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1940 gain cp kingdom-of-romania -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1940 gain cp kingdom-of-lithuania -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1940 gain cp estonia -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1945 gain cp republic-of-finland -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1945 gain cp czechoslovakia -> None None None: **exception** counterpart owned by eu-21, not run yet
- union-of-soviet-socialist-republics 1940 gain cp republic-of-latvia -> republic-of-latvia 1940 loss: **mismatch** Latvia records occupation 1940-6..8 by the USSR and the 1940-8 loss to latvian-soviet-socialist-republic
- union-of-soviet-socialist-republics 1991 loss cp republic-of-latvia -> republic-of-latvia 1991 gain: **mismatch** Latvia gains 1991-8 from latvian-soviet-socialist-republic; USSR loses 1991-9 to republic-of-latvia (group-level SSR convention)
- union-of-soviet-socialist-republics 1941 loss cp nazi-germany -> nazi-germany 1941 contest_start: **mismatch** USSR losses 1941-7 (Baltic, Belarus), 1941-9 (Ukraine), 1942-7 (Crimea) vs nazi-germany contest only; the RSFSR uses occupation_start cp nazi-germany for its own land
- union-of-soviet-socialist-republics 1943 gain cp nazi-germany -> nazi-germany 1943 contest_end: **mismatch** USSR gains 1943-1945 vs nazi-germany contest_end only
- union-of-soviet-socialist-republics 1941 occupation_start cp pahlavi-dynasty -> pahlavi-dynasty 1941 occupation_start: **matched** end 1946-5 matched too
- union-of-soviet-socialist-republics 1944 vassal_end cp tuvan-people-s-republic -> tuvan-people-s-republic 1944 dissolve: **matched** USSR lacks the gain; RSFSR has it
- union-of-soviet-socialist-republics 1945 occupation_start cp nazi-germany -> allied-occupied-germany 1945 occupation_start: **mismatch** wrong counterpart: allied-occupied-germany carries occupation 1945-6..1949-10 and the Kaliningrad loss 1945-8 cp the USSR
- union-of-soviet-socialist-republics 1945 occupation_start cp Soviet-occupied Central and Eastern Europe -> None None None: **exception** free-text counterpart; owners eu-21/eu-22 not run
- union-of-soviet-socialist-republics 1945 occupation_start cp manchukuo -> manchukuo 1945 dissolve: **mismatch** start matched (manchukuo dissolve cp USSR) but the 1946 end names a state gone since 1945-8; land went to republic-of-china
- union-of-soviet-socialist-republics 1945 occupation_start cp mengjiang -> mengjiang 1945 dissolve: **mismatch** mengjiang has no event naming the USSR; dissolve 1945-8 cp republic-of-china
- union-of-soviet-socialist-republics 1945 gain cp empire-of-japan -> empire-of-japan 1945 loss: **matched** South Sakhalin and Kurils
- union-of-soviet-socialist-republics 1948 occupation_end cp empire-of-japan -> empire-of-japan None None: **missing** no 1948 event in empire-of-japan; the 1948 counterpart is democratic-people-s-republic-of-korea
- union-of-soviet-socialist-republics 1979 occupation_start cp afghanistan -> afghanistan 1979 occupation_start: **matched** end 1989-2 matched too
- union-of-soviet-socialist-republics 1991 loss cp republic-of-lithuania -> None None None: **exception** eu-22 not run (also republic-of-estonia)

## Problems

- republics-of-the-soviet-union is typed umbrella, which the reviewer brief says is never a dossier of its own; the schema allows umbrella for associations and the RSFSR and SSR dossiers of eu-17-x already draw the 1920-21 land, so it is accepted here; the orchestrator should confirm that an umbrella dossier is the right home for a leaf Cliopatria row (umbrella=0 in polities.csv) and that its territorial events need no mirrors.
- Group-level convention clash: the RSFSR, Latvia and other dossiers use the union republics (latvian-soviet-socialist-republic etc.) as counterparts while this USSR dossier uses the USSR; and the USSR records German-held land as loss/gain while the RSFSR records it as occupation by nazi-germany and nazi-germany records only contests. One convention should be chosen for eu-17 before the mirrors can match.
- The author's notes list mengjiang as needing a dossier; history/polities/mengjiang.json exists (it names no USSR event).
- Dossiers written by the reviewer this run (small fixes, re-validated, read back): ukrainian-people-s-republic, republics-of-the-soviet-union, provisional-priamurye-government, union-of-soviet-socialist-republics.
- No page failed to load.

## Gazetteer names needed

- Franz Josef Land (region, union-of-soviet-socialist-republics)
- Petsamo (region, union-of-soviet-socialist-republics)
- Karelian Isthmus (region, union-of-soviet-socialist-republics)
- Ayano-Maysky District (region, provisional-priamurye-government)
- Hanko peninsula (place, union-of-soviet-socialist-republics)
