# Review of batch eu-17-x (Russian Empire and USSR, additions)

Reviewer, 2026-10-25. 24 new dossiers (all `cliopatria_names: []`). The machine copy of this review is `history/notes/phase-b/reviews/eu-17-x.json`. All pages were read on 2026-10-25 with WebFetch; about 40 pages, 4-6 events checked per dossier, weighted to confidence 3 and to the events that move the most land.

Mechanical check: all 24 validate with `--resolve`; the only warning is `state-of-buryat-mongolia` (FER found counterpart, no dossier, flagged by the author). Every file re-validated after the reviewer's edits.

## Verdicts

| dossier | verdict |
| --- | --- |
| russian-state | thin (one fix applied) |
| far-eastern-republic | fix (applied) |
| south-russia | **fail** |
| ukrainian-soviet-socialist-republic | **fail** |
| russian-soviet-federative-socialist-republic | **fail** (one fix applied) |
| kazakh-soviet-socialist-republic | thin (two fixes applied) |
| byelorussian-soviet-socialist-republic | fix (applied) |
| grand-duchy-of-finland | pass |
| congress-poland | pass |
| transcaucasian-socialist-federative-soviet-republic | pass |
| georgian / armenian / azerbaijan SSR | fix (applied: keyframe split) |
| estonian-soviet-socialist-republic | fix (applied) |
| latvian-soviet-socialist-republic | pass |
| lithuanian-soviet-socialist-republic | thin |
| moldavian-soviet-socialist-republic | pass |
| moldavian-autonomous-soviet-socialist-republic | fix (applied) |
| karelo-finnish-soviet-socialist-republic | thin |
| uzbek / turkmen SSR | pass |
| tajik / kirghiz SSR | fix (applied) |
| russian-eastern-outskirts | fix (applied) |

No fabricated event was found: every confidence-3 event I opened is on a page, with the year. One set of three confidence-3 events (russian-eastern-outskirts /ledger/1-3) cited a page that does not give the dates; the dates are on the Eastern Okraina page, and the source was corrected.

## Edits the reviewer made (all re-validated, read back after 10 s)

- **far-eastern-republic** /ledger/1 (was /ledger/0): the Amur gain had year only and sorted before the April 1920 founding. Month 7 (the page: "summer" 1920, next to the 15 July truce), confidence 3 to 2, moved after the found event.
- **russian-state** /ledger/8 and /ledger/21: the Transbaikal vassal pair named `russian-eastern-outskirts` from December 1918, but that state was founded 16 January 1920 (Eastern Okraina infobox), after this one ended. Counterpart now "Grigory Semyonov's Transbaikal regime" on both.
- **russian-eastern-outskirts** /ledger/1-3: source moved from the Far Eastern Republic page (which has only "By October Semenov had been expelled") to the Eastern Okraina page ("on October 19 the Reds began to advance on Chita, which they captured on October 22").
- **byelorussian-soviet-socialist-republic**: start, found event, Smolensk capital and the first certainty span moved from 1918-12 to 1919-01. The page: the conference met "on 30-31 December 1918" and "The next day, the Soviet Socialist Republic of Byelorussia was proclaimed in Smolensk"; the infobox does not give 31 December as the capital note claimed.
- **estonian-soviet-socialist-republic** /ledger/1: month 7 ("the Wehrmacht reached Estonia in July 1941").
- **kazakh-soviet-socialist-republic** /keyframe_review/2: verdict ok to adjust (a new keyframe). /ledger/1 and /ledger/6: vassal_start 1920.8 and vassal_end 1936.12 with counterpart the RSFSR, mirroring the RSFSR's events (Kazakh ASSR page: "an autonomous republic within the Russian Socialist Federative Soviet Republic"; Kazakh SSR page: union republic 5 December 1936).
- **kirghiz-soviet-socialist-republic** /ledger/1, /ledger/4: vassal pair with the RSFSR (1924.10, 1936.12).
- **tajik-soviet-socialist-republic** /ledger/1, /ledger/3: vassal pair with the Uzbek SSR (1924.10 confidence 2; 1929.12 confidence 3, "In December 1929, Tajik ASSR was detached from the Uzbek SSR").
- **moldavian-autonomous-soviet-socialist-republic** /ledger/1, /ledger/5: vassal pair with the Ukrainian SSR (1924.10, 1940.8).
  The convention (the vassal records `vassal_start` with the overlord as counterpart) is the one manchukuo and empire-of-japan use.
- **georgian / armenian / azerbaijan SSR** /keyframe_review/0: the single keyframe held the country from 1920/1921 to 1991 although the ledger hands the whole land to the Transcaucasian SFSR from March 1922 to December 1936 and that dossier's 1922-1936 keyframe draws it: two owners for 15 years. Each keyframe now ends in 1921 and a new `<slug>_1937` keyframe (1937-1991) carries the same correction, as the author's own model says ("The land is drawn as the federation").
- **russian-soviet-federative-socialist-republic** /ledger/2: confidence 3 to 2: the Brest-Litovsk page says "The territory of the Kingdom of Poland was not mentioned in the treaty", and Poland is in the region.

## Failed: what the author must change

### russian-soviet-federative-socialist-republic

1. /keyframe_review/0 (1917-1939) draws all of Russia for the Civil War: Siberia, the Urals and the Volga (russian-state 1918-1919), the Don, Kuban and North Caucasus (south-russia 1919-1920) and the Far East (russian-eastern-outskirts 1920, far-eastern-republic 1920-1922). The note says "the ledger carries those losses and gains", but the ledger has no 1918 loss of Siberia, the Urals or the Volga (the land russian-state is founded on) and no loss of the Far East before the 1922 merge. Split the keyframe for the Civil War (for example 1917, 1918, 1919, 1920-1922, 1923-1939) to the Soviet-held land, and add the summer-1918 losses (Czechoslovak Legion revolt, Komuch, Provisional Siberian Government) and the 1920 Far East.
2. /ledger/10: Omsk is inside a gain from south-russia; it was taken from russian-state (Kolchak page: "Omsk was evacuated on 14 November"). Split it out with counterpart russian-state.
3. /ledger/14: the October 1920 gain of Chita from the FER contradicts its own note ("the Far Eastern Republic ... takes the land, not the RSFSR itself") and the FER ledger. Delete it.
4. Missing mirrors: russian-state /ledger/14 (Perm, Izhevsk, Sarapul, Votkinsk, 1919.7) and /ledger/19 (Western Siberia, 1919.12); south-russia /ledger/0 (Tsaritsyn and Kursk, 1919) and /ledger/15 (Northern Taurida, 1920.6); byelorussian SSR /ledger/4 (Vitebsk and Mogilev, 1919.2), /ledger/10 (1924.3) and /ledger/11 (Gomel, 1926.12); uzbek SSR /ledger/8 (Karakalpakstan, 1936.12). The Belarus and Karakalpak transfers also change this dossier's land in 1919-1926 and 1930-1936.
5. No occupation events for the German occupation of RSFSR land in 1941-1944 (Smolensk, Bryansk, Oryol, Kursk, Belgorod, Rostov, Krasnodar, Stavropol, the North Caucasus, the Crimea) and no war entry for the German-Soviet war; every other republic in the batch has them.
6. Counterparts that disagree with the neighbours (route to the orchestrator): empire-of-japan records its 1945 Sakhalin and Kuril losses to union-of-soviet-socialist-republics, not to the RSFSR; Kaliningrad is gained from nazi-germany in April 1946, a year after that state ended. Tuva's dossier dissolves to the USSR.
7. Thin: Petsamo (Finnish 1920-1944) is inside the 1917-1939 shape; Salla, Rybachy and Hanko are not placed.

### ukrainian-soviet-socialist-republic

1. /keyframe_review/0 to /keyframe_review/1: the shape grows from a Kharkiv radius (1917-1918) to 469,382 km2 (1919) with no gain event. Add the 1919 gains from the Ukrainian People's Republic (Kiev, February 1919) and the 1918 loss to the Central Powers, or shrink the 1919 keyframe to the land held.
2. /keyframe_review/1: the 1919-1938 shape is "the Soviet claim, not control" for 1919-1920 and double-draws the south-russia 1919 keyframe and Poland's 1920 hold of Kiev. Draw held land: losses to south-russia in August-October 1919 (Southern Front page: "relinquishing Kiev, Odessa, Kursk, Voronezh, and Orel between August and October"), regains in December 1919 to February 1920, Kiev lost to Poland and regained in May-June 1920.
3. /ledger/2: the Kyiv loss has year only and sorts before March and May 1919; month 8.
4. Mirrors to add: south-russia /ledger/5 (1919.10) and /ledger/9 (1920.2); the eastern Moldavian ASSR districts returned in August 1940 (MASSR /ledger/4).
5. /ledger/19 and /ledger/20 (confidence 2): the German occupation starts in June 1941, not October (the page: "By October, the Germans had captured Kharkiv and Stalino"; the whole territory by 27 July 1942); the Romanian hold of Odesa and Chernivtsi ended "in early 1944" (Bessarabia page), not August.

### south-russia

1. /ledger/0: a gain from the Ukrainian SSR of Tsaritsyn, Kiev and Kursk with year only (sorted before the January 1919 founding). Tsaritsyn (Volgograd) and Kursk are RSFSR land, so two of the three cities have the wrong counterpart. Split: Tsaritsyn 1919.5-6 from the RSFSR (Southern Front page: the May offensive "forced the front to retreat from ... Tsaritsyn"), Kursk 1919.9 from the RSFSR and Kiev 1919.8 from the Ukrainian SSR ("between August and October"), confidence 2.
2. /ledger/5, /ledger/9 (Ukrainian oblasts, confidence 1) and /ledger/15 (Northern Taurida, confidence 1) have no mirrors; keep them flagged and have the Ukrainian SSR and RSFSR authors add them.
3. /ledger/12 and /ledger/17 notes claim more than the Government of South Russia page says (Denikin's resignation; the list Simferopol to Yalta). Trim or cite.

## Thin (for a gap-filler)

- russian-state: /ledger/8 (Semyonov's subordination, confidence 1), /ledger/14 (Perm and the Udmurt towns, summer 1919), /ledger/19 (Western Siberia, November 1919 to January 1920: the largest move in the dossier at confidence 1). Also the 1920 keyframe covers 4 days of 1920 for the whole year.
- far-eastern-republic: /ledger/6 (Maritime Province joining), /ledger/7 (Priamurye enclave growth).
- kazakh: /ledger/2 (the 1924 Syr Darya and Semirechye transfer, confidence 1 on about 0.6 M km2); the Karakalpak AO inside the Kazak ASSR to 1930 (the Kazakh ASSR page names it) is drawn by nobody 1925-1936; the Orenburg lands and capital of 1920-1925 (Ak-Mechet is outside the 1920-1924 shape).
- byelorussian: /ledger/16 (liberation 1944, confidence 1), Bialystok 1939-1945.
- georgian: /ledger/2 (Artvin, confidence 1) is probably wrong: the invasion page says Turkey demanded the evacuation of Artvin and Ardahan on 23 February 1921 and the Moscow treaty awarded them to Turkey; drop it and date the cession to March 1921.
- armenian: Zangezur was held by Nzhdeh until 15 July 1921 (Armenian SSR page), inside the 1920-1921 shape.
- lithuanian: Klaipeda Region German until January 1945, drawn as Soviet from 1940.
- karelo-finnish: the 1941 occupation region leaves out the Isthmus with Vyborg; Salla not placed.
- moldavian ASSR: /ledger/4 (confidence 1).
- congress-poland: /ledger/2 (end of the November Uprising, about October 1831).

## Area checks

No area differs by a factor of two. The keyframe areas run 0.85 to 1.27 of the infobox figures; the gazetteer is high for the Baltic and Belarus and low for Kazakhstan, Uzbekistan and Tajikistan, and each note says so. The FER note calls 1,900,000 km2 an infobox figure; it is in the body text. The Kolchak page's "over 300,000 km2" is rejected in the russian-state 1919 note, rightly.

## Cross-dossier matrix, in short

Matched: the Civil War pairs between russian-state, south-russia, the FER, russian-eastern-outskirts and the RSFSR except those listed above; all six TSFSR pairs; the Baltic strips; the Karelian pairs; the Crimea 1954; the Moldavian pair; the Tajik and Khujand pairs; the vassal pairs once the reviewer added the vassal side.

Routed to other groups: turkestan-assr, bukharan and khorezm (ia-03) record only a dissolve to the USSR, so the 1924 gains of the Uzbek, Turkmen and Kazakh SSRs and the RSFSR's Turkestan vassal pair have no mirror there. ottoman-empire (me-10) has no 1921 gain of Artvin. empire-of-japan (jk-01) and tuvan-people-s-republic name the USSR, not the RSFSR. Counterparts in eu-17 (Cliopatria part), eu-19, eu-20 and eu-21 (russian-empire, provisional-priamurye-government, georgia, german-empire, second-polish-republic, kingdom-of-romania, nazi-germany, czechoslovakia, republic-of-finland) have not run; kingdom-of-sweden (eu-14) is not written yet.
