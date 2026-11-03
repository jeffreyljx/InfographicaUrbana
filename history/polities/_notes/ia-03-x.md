# ia-03-x notes (additions batch: Central Asian, Mongolian and Afghan states Cliopatria lacks)

Final version, 2026-10-19. 21 new dossiers (no Cliopatria row owned; every `cliopatria_names` is empty, every keyframe is new with verdict adjust), 105 ledger events, 51 source entries after the review repairs below (42 Wikipedia pages opened with WebFetch in this run; six fetches failed). All 21 validate with 0 errors; `--resolve` shows no unknown region names and one warning pair (below). Per-state reasoning is in each dossier's `notes` field; this file holds only what crosses dossiers.

## Written

Russian rule and Soviet successors: russian-turkestan (colony, 1867-1918), turkestan-assr (1918-1924), bukharan-people-s-soviet-republic (1920-1924), khorezm-people-s-soviet-republic (1920-1924), turkestan-autonomy (1917-1918), alash-autonomy (1917-1920), transcaspian-provisional-government (rebel, 1918-1920), basmachi-movement (rebel, 1918-1934), tuvan-people-s-republic (1921-1944), bukey-horde (colony, 1801-1845).

Afghanistan: principality-of-herat (1818-1863), principality-of-kandahar (1818-1855), maimana-khanate (1747-1892), emirate-of-afghanistan-1929 (rebel, 1929).

Xinjiang, Mongolia and the Tarim: kumul-khanate (1696-1930), yettishar (1864-1877), ili-sultanate (rebel, 1864-1871), first-east-turkestan-republic (1933-1934), khalkha-khanates (1636-1688), dughlat-emirate (1465-1514), tashkent-state (1784-1809).

Not duplicated on purpose: the Yarkent Khanate (eastern-moghulistan covers it), the three Kazakh zhuzes (kazakh-khanate) and the 1978-2002 Afghan conflicts (afghanistan, taliban, mujahideen).

## Date conflicts (the choice made; the page that lost is named in the dossier)

- Tashkent state ends 1809 (TK; matches the khanate-of-kokand dossier's gain of 1809) against 1808 (YK) and 1807 (TK infobox).
- Principality of Kandahar ends 1855/11 (Dost Mohammad page; matches emirate-of-afghanistan, ia-03-e) against September 1856 (Kandahar page).
- Principality of Herat starts 1818 (matches durrani-empire, ia-03-e) although the Herat page also gives 1793/1801; Farah is 1862 on one page and 30 October 1856 on the other.
- Khalkha khanates end 1688 (Galdan's conquest, NY) against 1691 (Outer Mongolia page) and the dzungar-khanate dossier's 1696 Qing takeover.
- Turkestan Autonomy: 25-27 November 1917 (own page) against February 1918 (Turkestan ASSR page). Transcaspian government: lead says to July 1919, infobox February 1920 (followed).
- Alash Autonomy: the body gives 13 September 1917 and 5-13 December 1917 for different acts; the party page says December 1917 and July 1917 for the founding and the first congress.
- Bukey Horde ends 1845 in the text, 1849 in the infobox (1845 followed). Russian Turkestan: the Transcaspian Oblast joined in 1897 on the page (other works 1899, not opened).

## Counterparts and matching events other groups must carry

- kingdom-of-afghanistan (ia-03-f) has matching 1929 losses for Kabul, Kandahar and the autumn towns but none for Ghazni and Mazar-i Sharif, which the civil-war page supports.
- qing-dynasty (ea-08) and republic-of-china (ea-08): Kumul vassal pair (qing-dynasty 1696 to 1912, republic-of-china 1912 to 1930/6; kumul-khanate now carries its side, see Review repairs), Yettishar's conquest 1864-1877, the Ili occupation (russian-empire occupation_start 1871, occupation_end 1883/3, counterpart ili-sultanate), and the First East Turkestan Republic loss and gain in 1933-34.
- ottoman-empire (me-10): the page-dated vassalage of Yettishar from 1873.
- russian-empire (eu-17) and union-of-soviet-socialist-republics: the Uzbek SSR, Turkmen SSR, Tajik ASSR, Kara-Kirghiz AO and Karakalpak AO of 1924 have no dossiers, so the successor entries of turkestan-assr, bukharan-people-s-soviet-republic and khorezm-people-s-soviet-republic point to the union dossier; re-point them if such dossiers are written.
- kazakh-khanate (ia-03-a) lists Tashkent under the suggested slug tashkent-state-of-yunus-khoja; the Kokand dossier and this batch use tashkent-state. It also names the Bukey Horde as needed (written here).
- golden-horde (ia-02-x) marks 15 mislabelled rows 1636-1695 wrong; khalkha-khanates supplies the corrected shape. moghulistan (ia-02-d) and turpan-khanate ask for a Dughlat emirate (written).
- Basmachi pairs: matching gain/loss events were added to turkestan-assr and bukharan-people-s-soviet-republic so the rebel zones pair up.
- Only validator warning: principality-of-kandahar names khanate-of-kalat (vassal events 1818/8 and 1826/8); no dossier has it. talpur-dynasty is a known polity.

## Gaps

- khanate-of-kunduz not written (the Wikipedia page failed to load; Mir Murad Beg too). Merv and the Tekke Turkmen, the Mirdom of Badakhshan, the Altishahr Khojas and the Kyrgyz khanate were not written (Kyrgyz page failed; others page silent or out of the page budget).
- No Khotan Emirate (1933-34) dossier; no Outer Mongolia (Qing, 1696-1911) colony dossier. The Ili Sultanate and Taranchi material is thin (the Ili Sultanate title redirects to the Dungan Revolt article).
- Gazetteer: Sibi, Pishin and Shorawak are named on the Kandahar page but not drawn; no region name is needed by the 21 dossiers.

## Review repairs (2026-10-19, after review-ia-03-x.md)

Two dossiers failed review; both were repaired and validate (alash-autonomy 0 errors 0 warnings; kumul-khanate 0 errors, 1 warning explained below). Every other dossier of the batch is untouched.

alash-autonomy (BLOCKING, applied). The claim was the whole of Kazakhstan, which drew the Qyzylorda, South Kazakhstan, Zhambyl and Almaty admin-1s (2,308 cells, about 584,000 km2) twice, because russian-turkestan (to 1918/4) and turkestan-assr (1918-1924) hold them in the same years and the page says the entity bordered 'the Turkestan Autonomy to the south'. The keyframe and both ledger regions are now {"minus": [Kazakhstan, union of those four admin-1s]}, 6,820 cells (about 1.72 M km2), with the same text; I also gave the predecessor and successor `land` the same shape for consistency (not asked). No contest with turkestan-assr is recorded: the Alash_Autonomy page (re-opened) and the Alash_Orda page (opened now) name no oblast and no district of Syr-Darya or Semirechye and describe no dispute. Thin finding (oblast list, Western Alash Orda, 1919 Soviet takeover): Alash_Orda repeats Alash_Autonomy's borders sentence and lists no oblasts, no Western Alash Orda, Uralsk or Zhympity; it dates the takeover only as 'By 1919 ... effectively dismantled by Soviet forces' and 'By 1920, the Bolsheviks ... occupied Kazakhstan'. I did not add a Soviet-takeover event: no month, no region and no counterpart dossier beyond the dissolve at 1920/8 that already hands the land to the Soviet republics; an occupation pair at confidence 1 would only bridge a silence. The Western Alash Orda stays a gap (page silent).

kumul-khanate (BLOCKING, applied; two non-blocking fixes applied). Added vassal_start 1696 and vassal_end 1912 with counterpart qing-dynasty and vassal_start 1912 and vassal_end 1930/6 with counterpart republic-of-china (confidence 3, region Hami 120 km, source Kumul_Khanate re-opened: infobox 'Banner of the Qing dynasty (1696-1912)', 'Vassal of the Republic of China (1912-1930)', 'after submitting to the Qing as a vassal'; the page gives no month for 1912). Nasir (1930-1934) is dropped from identity.rulers, with the reason on Maqsud Shah's entry: the table lists him and a later Bashir (1934-1949) after the abolition of 6 June 1930, and the page says only that Yulbars Khan 'attempted to restore the heir Nasir'. The Kumul Rebellion war was dated 1930-1930 without a page; the Kumul_Rebellion page (opened now, second page, budget 1-2) gives '20 February 1931 - July 1934', so the war is 1931-1934 with no zone (the page dates no held ground), and the validator warns that the span lies outside the state's life 1696..1930; kept on purpose because the rebellion is the khanate's loyalist reaction and no other dossier carries it (first-east-turkestan-republic has only 1933-34 Ma Zhongying), and the reviewer allowed keeping it with a note.

Where I disagree. The reviewer's fix writes the vassal events in Kumul's own dossier with the suzerain as counterpart. The schema (`ledger[].type` description) defines vassal_start as 'region becomes this state's vassal ... counterpart is the vassal itself', i.e. the suzerain's event, which is how the Tang example and the Tang's Nanzhao and Tuyuhun events are written. I applied the reviewer's direction because the finding is blocking and the matrix expects a vassal-side mirror, and each note says 'Recorded from the vassal's side'. If the compiler reads the schema's direction, these four events draw Hami wrongly and should be dropped while qing-dynasty and republic-of-china (ea-08, neither dossier exists on 2026-10-19) carry vassal_start/vassal_end with counterpart kumul-khanate (1696/1912 and 1912/1930-6). The orchestrator should rule; the same question is open for the other vassal states of this batch (yettishar with the Ottomans, 1873-1877; Bukhara and Khiva with russian-turkestan). The Kumul_Khanate page does not call Nasir or the later Bashir claimants; that reading is the reviewer's and mine from the Kumul_Rebellion and Kumul_Khanate sentences quoted above.
