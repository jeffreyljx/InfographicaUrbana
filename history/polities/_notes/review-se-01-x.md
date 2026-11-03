# Review of batch se-01-x (2026-10-19)

Adversarial review of 16 additions dossiers (mainland South-east Asia). The validator with --resolve gives 0 errors and 0 warnings on all 16. Each dossier got 4 to 7 spot checks (every event in the two- and three-event dossiers) with WebFetch on the cited pages, 66 in all, and every one was found on the page; no fabricated event. Verdicts: 2 fail, 9 thin, 5 pass. The reviewer applied one change: restored-hanthawaddy-kingdom /ledger/10-11, confidence 3 to 2, re-validated.

## restored-hanthawaddy-kingdom: fail

- **Fix** `/keyframe_review/0/correction (also /keyframe_review/1-4 and /ledger/0/region)`: KF0-KF4 and the found region include admin1 Mon, Kayin and Tanintharyi (the Martaban and Tavoy country, cut by the First Toungoo 1738 outline), but the page says these rulers went over to Siam, and the dossier's own notes say this land is 'not counted as Mon land after 1740'. Evidence: Restored_Hanthawaddy_Kingdom: 'The rulers of Martaban (Mottama) and Tavoy (Dawei) sought and received Siamese protection.' KF5 (1755) then drops Mon/Kayin/Tanintharyi with no ledger event: /ledger/15 (1755-5) loses only Ayeyarwady and Yangon. This land could be well over a third of the 1740 shape (Mon 12k + Kayin 30k + Tanintharyi 43k km2 before the intersect). Do: Remove {admin1: Mon}, {admin1: Kayin} and {admin1: Tanintharyi} from the union inside KF0-KF4 and /ledger/0 (keep the 60 km Pegu circle and Bago for the Sittaung). Tell first-toungoo-empire to trim its 1740-11 loss region to match. If the author keeps them, add a dated loss with a page between 1754 and 1755 so that KF4 to KF5 is explained.
- **Fix (applied by reviewer)** `/ledger/10 and /ledger/11`: Confidence 3 for the 1754 seizure of Prome, but the war page's sentence has no year, and the note's quote added 'in 1754'. Evidence: Konbaung–Hanthawaddy_War: 'Meanwhile, Burman refugees who had escaped general slaughter by the delta Mons seized Prome (Pyay) ... and shut the gates to the retreating Hanthawaddy armies' (no year; it follows the 1754 retreat). Do: Lower confidence to 2 and quote the sentence as written.
- Thin `/keyframe_review/4-6`: When Toungoo was lost: KF4-KF6 keep the Bago region (Toungoo) Mon to 1757 at confidence 1, and the war page only has an army marching 'from Toungoo' in September 1756 (try https://en.wikipedia.org/wiki/Alaungpaya)
- Thin `/notes`: The 1740s Mon-Siamese border at Martaban and Tavoy (needed to settle the fix above) (try https://en.wikipedia.org/wiki/Binnya_Dala)
- Area: No infobox area on Restored_Hanthawaddy_Kingdom; the KF0 note says so. Cliopatria has no row of its own (stray Konbaung Dynasty row 1741-1751, 116,345 km2).
- Spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/7 confirmed; /ledger/12 confirmed; /ledger/15 confirmed; /ledger/16 confirmed; /ledger/11 confirmed (town); year not in the sentence, confidence lowered to 2

## dvaravati: pass

- Thin `/ledger/2`: 913 handover of the western valley to Suphannabhum is confidence 1 (Dvaravati page silent; Suphannaphum page: Nakhon Pathom 'fell to Phetchaburi in 913') (try https://en.wikipedia.org/wiki/Nakhon_Pathom)
- Thin `/keyframe_review/1`: 648-912 shape (Nakhon Pathom, Suphan Buri, Ratchaburi, Phetchabun) lies inside lavo-kingdom_806 (126,430 km2); the author flagged it, and a gap-filler must clip one of them
- Area: No infobox area (Dvaravati infobox: established 6th century, disestablished 11th century); acknowledged in the keyframe note.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed

## suphannaphum-kingdom: pass

- Thin `/ledger/2`: Year of the break from Sukhothai (page: 'after the death of Sukhothai's Ram Khamhaeng in 1298 ... began to break away rapidly'; tributary 1283-1298); 1300 is a bridge (try https://en.wikipedia.org/wiki/Loe_Thai)
- Area: No infobox area (only the moat, 1900x3600 m); acknowledged.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed (no year on page; confidence 1 is honest); /ledger/3 confirmed (joined Lavo 'to establish a confederated polity seat in Ayodhya in 1351'; full annexation 1438 noted by the author)

## mon-city-states: pass

- Thin `/ledger/0`: 825 start is the navbox's '825?-1057?' (confidence 1); the page says only 'probably came into existence some time in the 9th century' (try https://en.wikipedia.org/wiki/Mon_kingdoms)
- Thin `/keyframe_review/0`: Extent: the page calls Thaton 'essentially a city-state centered on the city of Thaton', but the keyframe draws all of Lower Burma (to match pagan-kingdom's 1057 gain). The author acknowledged it; a gap-filler should find a page that bounds it (try https://en.wikipedia.org/wiki/Hanthawaddy_Kingdom)
- Area: No area on Thaton_Kingdom; acknowledged.
- Spot checks: /ledger/0 confirmed (c1); /ledger/1 confirmed (Manuha surrendered 'on 17 May 1057'); /ledger/2 confirmed in substance (the quoted sentence is a paraphrase; the page has 'conquered the fabled kingdom in 1057')

## ngoenyang: thin

- **Fix** `/identity/capitals/3 and /identity/capitals/4`: The capitals Fang (19.92N 99.21E, 1275-1285) and Wiang Kum Kam (18.76N 99.02E, 1286-1292) lie outside every keyframe: KF3 is Chiang Rai province plus a 30 km circle at Thoeng, and Fang and Wiang Kum Kam are in Chiang Mai province. Evidence: Ngoenyang infobox: 'Fang (1275-1286); Wiang Kum Kam (1286-1292)' and 'Annexation of Haripunjaya: 1281'; KF3 = Chiang Rai admin1 + circle(19.62,100.25,30 km). The notes flag the dates, not the geometry. Do: Add a Fang circle (about 30 km) to KF3, with a gain event (the Mangrai page puts him in the Fang area about 1262). Then either end the Wiang Kum Kam capital (the Mangrai page founds it in 1294) or follow the infobox's 1281 annexation of Haripunjaya, and agree that year with haripunjaya and lan-na-kingdom.
- Thin `/ledger/3`: 1261 gain of Thoeng and Chiang Kham is confidence 1 (Mangrai page undated) (try https://en.wikipedia.org/wiki/Phayao_Kingdom)
- Thin `/ledger/6`: 1286 Wiang Kum Kam capital, confidence 1, against the Mangrai page's 1294 (try https://en.wikipedia.org/wiki/Wiang_Kum_Kam)
- Thin `/ledger/1`: 662 split of Haripunjaya against haripunjaya's c. 750 found (Ping basin unowned 662-749) (try https://en.wikipedia.org/wiki/Haripunjaya)
- Area: No area on Ngoenyang (only the city, about 1.5 by 7 km); acknowledged.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/5 confirmed; /ledger/7 confirmed

## launggyet-kingdom: thin

- **Fix** `/ledger (1412, 1421)`: Missing vassal_start 1412 and vassal_end 1421 with counterpart hanthawaddy-kingdom; the sibling carries the pair with counterpart 'Arakan (Launggyet kingdom)'. Evidence: Forty_Years'_War infobox (a page this dossier cites): 'Arakan tributary of Pegu (1412-1421)'; Min_Saw_Mon: Pegu 'placed its nominees in Launggyet and Sandoway (Thandwe)'. hanthawaddy-kingdom /ledger/8 and /ledger/11. Do: Add vassal_start 1412 and vassal_end 1421, counterpart hanthawaddy-kingdom, source Forty_Years%27_War, confidence 3, region = the KF0 region.
- **Fix** `/ledger (1237-1287)`: pagan-kingdom keeps Arakan as a tributary 1066-1287 (vassal_end 1287, counterpart 'arakan'), but launggyet-kingdom (from 1237) carries no vassalage to Pagan. Evidence: pagan-kingdom /ledger/7 and /ledger/11; the author's notes mention it but add no event. Do: Add vassal_end 1287, counterpart pagan-kingdom, and a vassal_start at 1237 (inherited), if a page supports it (Pagan_Kingdom: 'Arakan stopped paying tribute'). Ask pagan-kingdom to use counterpart launggyet-kingdom for 1287.
- Area: No area on Launggyet_Kingdom; acknowledged. KF0 = Mrauk U 1429 shape (84,574 km2) minus a 70 km Sandoway circle.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed

## muang-phuan: thin

- **Fix** `/ledger (1707)`: Missing vassal_start 1707 with counterpart kingdom-of-luang-phrabang; the sibling carries it with counterpart muang-phuan. Evidence: Muang_Phuan: 'In 1707 when Lan Xang was divided between the Kingdoms of Vientiane and Luang Prabang, Muang Phuan entered into tributary relations with the Kingdom of Luang Prabang.' kingdom-of-luang-phrabang /ledger/1. Do: Add vassal_start 1707, counterpart kingdom-of-luang-phrabang, confidence 3, with the end year from the page (tributary to Vientiane from 1751) as vassal_end, plus vassal_start with vientiane.
- Thin `/ledger`: The page's vassal statuses are not in the ledger: 'In 1434, Muang Phuan entered into a tributary relationship with the Dai Viet'; tributary to Vientiane 'for the next 37 years' from 1751; 'Principality under the Kingdom of Vientiane (1802-1828)'; 'Vassal to Siam (1848-1893)'; French protection 1893. The scope asks for the Lao principalities' Siamese vassalage as tints (try https://en.wikipedia.org/wiki/Muang_Phuan)
- Thin `/ledger/0`: 13th-century start at confidence 1 (try https://en.wikipedia.org/wiki/Xiangkhouang_province)
- Thin `/ledger/1`: Mid-14th-century incorporation into Lan Xang at confidence 1; lan-xang dates it 1363 (counterpart ngo-dynasty), and the page also has 'Autonomous principality (14th century-1791)', so a vassal tint may be the better picture (try https://en.wikipedia.org/wiki/Fa_Ngum)
- Thin `/ledger/4`: 1848 at confidence 1; the infobox gives 'Nguyễn dynasty province (1828-1848)', which could support confidence 2 (try https://en.wikipedia.org/wiki/Muang_Phuan)
- Area: No area on Muang_Phuan; acknowledged.
- Spot checks: /ledger/1 confirmed (c1, no year); /ledger/2 confirmed; /ledger/3 confirmed ('In 1832 the Dai Viet annexed Muang Phuan and named the region Tran Ninh'; the author's report wrongly lists 1832 as undated); /ledger/5 confirmed

## ha-tien: thin

- Thin `/ledger`: The infobox statuses 'Cambodian protectorate (1707-1736) Vietnamese protectorate (1707-1832) Siamese protectorate (1785-1809)' are not in the ledger. As drawn, Hà Tiên is independent for its whole life while the nguyen-lords and nguyen-dynasty shapes cover it. Needs vassal_start 1707 with nguyen-lords (continued by nguyen-dynasty), 1707-1736 with post-angkor-cambodia and 1785-1809 with rattanakosin-kingdom, mirrored in those dossiers (try https://en.wikipedia.org/wiki/Principality_of_Hà_Tiên)
- Thin `/keyframe_review/0`: The 80 km circle stands for the seven districts; no page lists them (try https://en.wikipedia.org/wiki/Mạc_Thiên_Tứ)
- Thin `/identity/rulers/1-7`: Rulers 2-8 carry no source (gaps 1777-1785, 1792-1800 and 1809-1816 are interregna) (try https://en.wikipedia.org/wiki/Principality_of_Hà_Tiên)
- Area: No area on Principality_of_Hà_Tiên; acknowledged.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed ('completely devastated by Siamese troops in 1771'); /ledger/2 confirmed; /ledger/3 confirmed

## kengtung: thin

- **Fix** `/ledger/1 and /ledger/2`: Kengtung records the Chiang Mai period as occupation_start 1802 and occupation_end 1814, while chiangmai records vassal_start 1802 and vassal_end 1813 with counterpart kengtung: the types do not mirror. Evidence: Kengtung_State: 'In 1802 Kengtung came under the rule of Chiang Mai' [citation needed]; 'the former ruling dynasty was reinstated in 1814'. chiangmai /ledger/8 and /ledger/11. Do: Agree one type with chiangmai (vassal if Kengtung kept its own rulers, occupation if Chiang Mai governed it) and one end year (1813 or 1814).
- **Fix** `/ledger (1562-1597)`: Missing vassal_start 1562 and vassal_end 1597 with first-toungoo-empire, which carries the pair with counterpart 'Kengtung'. Evidence: first-toungoo-empire /ledger/26 ('The southernmost trans-Salween state of Kengtung submitted ... on 16 December 1562') and /ledger/59 (1597). Do: Add vassal_start 1562-12 and vassal_end 1597, counterpart first-toungoo-empire, citing the page first-toungoo-empire used (Bayinnaung). Ask that dossier to use the slug kengtung.
- Thin `/ledger/3`: 1895 end at confidence 1; the page also says 'The last ruler of Kengtung abdicated in 1959' and records the Thai Phayap Army occupation from 27 May 1942 to 1945 (try https://en.wikipedia.org/wiki/Shan_States)
- Thin `/ledger`: Burmese (Konbaung) suzerainty before 1802 and after 1814 is not drawn as a tint (try https://en.wikipedia.org/wiki/Kengtung_State)
- Area: Infobox '1901: 31,079 km2'. No Cliopatria row; the 100 km keyframe circle is 31,416 km2. The KF0 note quotes both.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (tagged citation needed on the page); /ledger/2 confirmed; /ledger/3 confirmed (lead '1243 to 1895', c1 honest)

## mong-mao: thin

- Thin `/keyframe_review/0`: The same Yunnan cells are claimed by shan-states up to 1444 (shan-states /ledger/5, 1444 loss of 'the Yunnan lands of Möng Mao' to the Ming). The author flagged it; a gap-filler must drop them from one dossier
- Thin `/ledger`: Yuan and Ming overlordship is not drawn: 'Establishment of the Luchuan Route: 1276' (infobox) and Si Lunfa's submission to the Ming in 1382 and surrender in 1388. Vassal tints are needed once yuan-dynasty and ming-dynasty exist (try https://en.wikipedia.org/wiki/Möng_Mao)
- Area: No area on Möng_Mao (only the Baiyi Zhuan's '10,000 li' claim); nothing to compare.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed

## muang-sua: thin

- **Fix** `/ledger (1294-1299)`: No mirror for sukhothai-kingdom's vassal_start 1294 and vassal_end 1298 (counterpart 'Phrae and Muang Sua') or for its 1299 loss (counterpart 'Muang Sua and Vieng Chan'). Evidence: Muang_Sua infobox: 'Sukhothai vassal: 1286-1297' and 'Muang Sua as a vassal to Sukhothai in 1293'; sukhothai-kingdom /ledger/5, /ledger/7 and /ledger/8. Do: Add vassal_start and vassal_end with counterpart sukhothai-kingdom (agree 1286/1293/1294 and 1297/1298 with se-01-d), and have sukhothai-kingdom drop its 1299 loss or turn it into the vassal_end, since muang-sua keeps the land throughout.
- Thin `/ledger`: The infobox statuses '1st Khmer vassal: 1070-1128', '1st Dependency of Mongol: 1250s-1271' and '2nd Dependency of Mongol: 1297-1300s' are not drawn (try https://en.wikipedia.org/wiki/Muang_Sua)
- Thin `/ledger/2`: End of Nanzhao's hold c. 800, confidence 1 (try https://en.wikipedia.org/wiki/Nanzhao)
- Area: No area on Muang_Sua; acknowledged.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed

## nan-kingdom: thin

- Thin `/ledger`: Infobox 'Under Phayao rule: 1263-1323' (and the body: 'liberating the Nan kingdom from the Phayao kingdom') is not drawn: vassal_start 1282 and vassal_end 1323 with phayao-kingdom are needed in both dossiers (try https://en.wikipedia.org/wiki/Nan_Kingdom)
- Thin `/ledger/5`: lan-na-kingdom has no 1449 gain of Nan (the infobox has a Lan Na vassal, Phasaeng, 1450-1461 or 1459) (try https://en.wikipedia.org/wiki/Tilokaraj)
- Area: No area on Nan_Kingdom; acknowledged.
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed (Hung won in 1400; Sukhothai's help came 'one year later'); /ledger/5 confirmed

## portuguese-syriam: pass

- Thin `/ledger`: Subject status under Ayutthaya ('becoming a subject of the Kingdom of Ayutthaya') and recognition from Goa are undated on the page, so not drawn; the author noted it (try https://en.wikipedia.org/wiki/Filipe_de_Brito_e_Nicote)
- Area: No area on either page; one city, acknowledged.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed (April 1613)

## sip-song-chau-tai: thin

- Thin `/ledger/0`: c. 1600 start at confidence 1 (page: 'formalized since at least the 17th century'); 1600-1948 has no events (try https://en.wikipedia.org/wiki/Đèo_Văn_Trị)
- Thin `/ledger`: Tribute to Luang Prabang and the French protectorate from 7 April 1889 are not drawn. kingdom-of-luang-phrabang /ledger/6 loses 'the Sipsong Chau Tai' to France on 7 April 1889, so both dossiers draw the same land up to 1889 (try https://en.wikipedia.org/wiki/Sip_Song_Chau_Tai)
- Thin `/keyframe_review/0`: The page does name the provinces ('situated in the modern-day provinces of Điện Biên, Lai Châu, Sơn La') and lists 'the original twelve chau muang', so the notes' 'no canton list' is wrong and the region could rise to confidence 2 (try https://en.wikipedia.org/wiki/Sip_Song_Chau_Tai)
- Area: No area on Sip_Song_Chau_Tai; acknowledged.
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed

## van-lang: pass

- Thin `/ledger/0`: -1000 start is the Đông Sơn date at confidence 1 (Văn Lang page: traditional 2524-258 BC only) (try https://en.wikipedia.org/wiki/Hồng_Bàng_dynasty)
- Area: No area on Văn_Lang (15 regions, borders named as seas, a lake and kingdoms); nothing to compare.
- Spot checks: /ledger/0 confirmed (c1); /ledger/1 confirmed

## tambralinga: fail

- **Fix** `/keyframe_review/0`: No keyframe shows the Lavo holding that /ledger/2 (927 gain, region {cliopatria: Lavo Kingdom, year 806}) and /ledger/3 (960 loss) assert. KF0 runs unchanged from 150 to 1276 and its note does not mention Lavo, while lavo-kingdom gives the land up from 928 to 946, so nobody draws it. Evidence: shapes.csv: lavo-kingdom_806 is 126,430 km2, almost four times KF0 (Nakhon Si Thammarat + Surat Thani + Chumphon + Krabi, about 33,500 km2). lavo-kingdom /ledger/3 (928 loss) and /ledger/4 (946 gain). Do: Split KF0. Add a keyframe tambralinga_927 (from 927 to the agreed end) = KF0 ∪ {cliopatria: Lavo Kingdom, year 806}, and set KF0's to and a later keyframe's from around it. Or, if the author reads the Lavo infobox ('Tambralinga vassal: 927-946') as vassalage, turn /ledger/2-3 into vassal_start and vassal_end and agree that with lavo-kingdom.
- **Fix** `/ledger/3`: The end of the Lavo holding is 960 with counterpart lavo-kingdom, but lavo-kingdom has the 946 gain, and the page gives the 960 annexation to 'Siamese from Ayodhya', not to Lavo's own line. Evidence: Tambralinga: 'Later in 960, Lavapura was annexed by Siamese from Ayodhya, who also shared a political relation with Tambralinga kingdom.' lavo-kingdom /ledger/4 (946, Lavo infobox 'Tambralinga vassal: 927-946'). Do: Use 946 to match lavo-kingdom (Lavo infobox), or keep 960 with a counterpart naming Ayodhya and route lavo-kingdom to move its gain. Either way, both dossiers carry the same year.
- Thin `/ledger/0`: 2nd-century start at confidence 1 (try https://en.wikipedia.org/wiki/Tambralinga)
- Thin `/ledger/5`: 1277 fall against sukhothai-kingdom's 1294 gain and 1300 loss with counterpart 'Tambralinga' (after this state's end); the successor Nakhon Si Thammarat has no dossier (try https://en.wikipedia.org/wiki/Nakhon_Si_Thammarat_Kingdom)
- Thin `/ledger`: Pagan's suzerainty 1130-1176 (Wyatt, on the page) and the 1244 'largest extent' are not drawn (try https://en.wikipedia.org/wiki/Chandrabhanu)
- Area: No area on Tambralinga (only the town walls, about 1 km2); acknowledged.
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed (infobox war 927; 'took advantage of the situation to occupy Lavo'); /ledger/3 confirmed (quote on page; counterpart is the author's reading); /ledger/5 confirmed

## Cross-dossier matrix (unmatched and mismatched only)

- missing: restored-hanthawaddy-kingdom 1754 loss cp=konbaung-dynasty. konbaung-dynasty has no 1754 Prome gain (Prome taken by Burman refugees and relieved by Alaungpaya in Feb 1755); route to se-01 Konbaung author.
- missing: dvaravati 946 loss cp=khmer-empire. khmer-empire has only a 946 vassal_start over lavo-kingdom ('Rāmaññadesa'), nothing for Si Thep (Phetchabun); route to khmer-empire.
- exception: haripunjaya 750 found cp=dvaravati. Lamphun was never in a dvaravati keyframe; Dvaravati is a cultural predecessor, no land handed over.
- mismatch: suphannaphum-kingdom 1283 loss cp=sukhothai-kingdom / mirror sukhothai-kingdom 1294 gain. sukhothai's 1294 gain ('Suvarnabhumi (likely Suphan Buri)', c1) names counterpart 'Tambralinga'; Suphannaphum page: 'annexed to the Sukhothai Kingdom in 1283'. Route: sukhothai to add a 1283 gain from suphannaphum-kingdom.
- mismatch: suphannaphum-kingdom 1351 merge cp=ayutthaya-kingdom / mirror ayutthaya-kingdom 1351 found. ayutthaya's found names only lavo-kingdom; it should also name suphannaphum-kingdom (merge of the four port polities).
- mismatch: ngoenyang 662 loss cp=haripunjaya / mirror haripunjaya 750 found. 88 years apart, and haripunjaya's found names dvaravati. Ngoenyang page: 662; Haripunjaya page: c. 750. The author flagged it; a gap-filler must pick one.
- missing: hanthawaddy-kingdom 1412 vassal_start cp=Arakan (Launggyet kingdom). Not in launggyet-kingdom (fix listed). Forty Years' War infobox: 'Arakan tributary of Pegu (1412-1421)'.
- missing: hanthawaddy-kingdom 1421 vassal_end cp=Arakan (Launggyet kingdom). As above.
- missing: pagan-kingdom 1287 vassal_end cp=arakan. launggyet-kingdom (1237-1429) carries no Pagan vassalage; pagan should name launggyet-kingdom from 1237.
- mismatch: muang-phuan 1353 loss cp=lan-xang / mirror lan-xang 1363 gain. lan-xang's 1363 gain ('He took Muang Phuan and then Xam Neua') names ngo-dynasty, 10 years later. One year and one counterpart needed.
- missing: kingdom-of-luang-phrabang 1707 vassal_start cp=muang-phuan. Not in muang-phuan (fix listed).
- missing: muang-phuan 1832 loss cp=nguyen-dynasty. nguyen-dynasty has no Tran Ninh gain; route to se-01 Nguyen author (Muang_Phuan: 'In 1832 the Dai Viet annexed Muang Phuan').
- missing: muang-phuan 1848 gain cp=nguyen-dynasty. nguyen-dynasty has no 1848 loss; route.
- exception: muang-phuan 1899 dissolve cp=french-indochina. french-indochina belongs to se-03, which has not run.
- missing: ha-tien 1707 found cp=post-angkor-cambodia. post-angkor-cambodia has no 1707 loss of Hà Tiên; route. (The page also keeps a Cambodian protectorate until 1736.)
- mismatch: ha-tien 1771 occupation_start cp=thonburi-kingdom / mirror thonburi-kingdom 1771 contest_start. thonburi records 'the Siamese take Hà Tiên' (Nov 1771) as a contest with counterpart nguyen-lords; it should be occupation_start with counterpart ha-tien.
- mismatch: ha-tien 1773 occupation_end cp=thonburi-kingdom / mirror thonburi-kingdom 1773 contest_end. As above.
- missing: ha-tien 1832 dissolve cp=nguyen-dynasty. nguyen-dynasty has no 1832 event for Hà Tiên; route.
- mismatch: kengtung 1802 occupation_start cp=chiangmai / mirror chiangmai 1802 vassal_start. Same year, different type (fix listed in kengtung).
- mismatch: kengtung 1814 occupation_end cp=chiangmai / mirror chiangmai 1813 vassal_end. One year apart, different type.
- missing: first-toungoo-empire 1562 vassal_start cp=Kengtung. Not in kengtung (fix listed); FTE uses the plain name 'Kengtung'.
- missing: first-toungoo-empire 1597 vassal_end cp=Kengtung. As above.
- exception: kengtung 1895 dissolve cp=british-raj. british-raj belongs to sa-06, which has not run.
- mismatch: mong-mao 1444 dissolve cp=ming-dynasty / mirror shan-states 1444 loss. ming-dynasty (ea-07) has not run. Both shan-states and mong-mao hand the same Yunnan land to the Ming in 1444, so the land is claimed twice to 1444; drop it from one.
- exception: muang-sua 709 occupation_start cp=nanzhao. nanzhao belongs to ea-04, which has not run.
- missing: sukhothai-kingdom 1294 vassal_start cp=Phrae and Muang Sua. Not in muang-sua (fix listed); Muang Sua page: 'Sukhothai vassal: 1286-1297'.
- missing: sukhothai-kingdom 1298 vassal_end cp=Phrae and Muang Sua. As above.
- mismatch: sukhothai-kingdom 1299 loss cp=Muang Sua and Vieng Chan. muang-sua has no 1299 gain and keeps its land throughout; sukhothai's 1294 'uplands' gain overlaps muang-sua's keyframe.
- exception: nan-kingdom 1399 occupation_start cp=Mueang Phrae. Phrae has no dossier; listed in counterparts_needing_dossiers.
- missing: nan-kingdom 1449 dissolve cp=lan-na-kingdom. lan-na-kingdom has no 1449 gain of Nan; route (the author flagged it).
- exception: thonburi-kingdom 1775 vassal_start cp=nan. The later Nan principality (1558-1931) has no dossier; listed.
- mismatch: portuguese-syriam 1603 found cp=kingdom-of-mrauk-u / mirror kingdom-of-mrauk-u 1603 occupation_end. mrauk-u's March 1603 occupation_end of Syriam names first-toungoo-empire; it should name portuguese-syriam.
- mismatch: kingdom-of-luang-phrabang 1889 loss cp=french-indochina / sip-song-chau-tai. Luang Prabang loses 'the Sipsong Chau Tai' to France on 7 April 1889, so it draws that land as its own, while sip-song-chau-tai draws it 1600-1954: a double claim. Needs a vassal tint (LPB suzerain) instead of direct land on one side.
- exception: sip-song-chau-tai 1954 dissolve cp=democratic-republic-of-vietnam. democratic-republic-of-vietnam belongs to se-04, which has not run.
- exception: tambralinga 775 occupation_start cp=srivijaya. srivijaya belongs to se-02, which has not run.
- mismatch: tambralinga 960 loss cp=lavo-kingdom / mirror lavo-kingdom 946 gain. 14 years apart; the page gives 960 to 'Siamese from Ayodhya'.
- mismatch: tambralinga 1277 dissolve cp=sukhothai-kingdom / mirror sukhothai-kingdom 1294 gain. sukhothai gains from 'Tambralinga' in 1294 and loses to 'Tambralinga' in 1300, after the state's 1277 end; it should use 1277/1278 or name the successor (Nakhon Si Thammarat, no dossier).

## Batch problems

- Two fails, both on keyframe vs ledger: restored-hanthawaddy-kingdom draws Martaban and Tavoy 1740-1754, against its page and its own notes, and drops them in 1755 with no event; tambralinga's ledger takes Lavo (126,430 km2) 927-960, but no keyframe draws it.
- Applied by the reviewer: restored-hanthawaddy-kingdom /ledger/10-11 confidence 3 to 2 (re-validated: 0 errors, 0 warnings). No other dossier was edited.
- No fabricated event: all 66 spot checks were found on the cited page. Several notes put paraphrases inside quotation marks (mon-city-states /ledger/2, restored-hanthawaddy /ledger/10).
- The author's report is wrong in two places. It says muang-phuan's 1832 annexation is undated, but the dossier and page have 1832. The notes say Sip Song Chau Tai has no canton list, but the page names the three provinces and the twelve chau muang.
- The batch leaves vassalage to the suzerains' dossiers throughout (ha-tien, muang-phuan, muang-sua, nan-kingdom, kengtung, launggyet-kingdom, mong-mao), but rule 3 needs the mirror on both sides, and siblings already carry several (luang-phrabang 1707, first-toungoo 1562, hanthawaddy 1412, sukhothai 1294, chiangmai 1802). These go to a gap-filler.
- Plain-name counterparts in sibling dossiers should become the new slugs: ava-kingdom and kingdom-of-mrauk-u ('Launggyet ...'), lan-xang ('Muang Sua'), sukhothai-kingdom ('Suphannaphum Kingdom', 'Tambralinga', 'Phrae and Muang Sua'), first-toungoo-empire ('Kengtung', 'Portuguese Syriam'), hanthawaddy-kingdom ('Arakan (Launggyet kingdom)'), pagan-kingdom ('arakan').
- Double claims for a gap-filler: dvaravati/lavo-kingdom 648-912, mong-mao/shan-states Yunnan cells to 1444, sip-song-chau-tai/kingdom-of-luang-phrabang to 1889, ha-tien inside the nguyen-lords and Cambodia shapes, kengtung inside the konbaung, burma and british-raj shapes.
- Keyframe 'to' conventions vary: some end at end.year (ha-tien, kengtung) and some at end.year-1 (launggyet, muang-sua, nan, van-lang). Not a fault, but the compiler should treat them the same.
- Of the Context polities in section 6 of the author's brief, only han-dynasty, mongol-empire and new-caledonia have dossiers, and none touches this batch's events. The cross-checks used the se-01 sibling dossiers that exist, plus pagan-kingdom, hanthawaddy-kingdom and kingdom-of-luang-phrabang. The rest of the Context list counts as 'not run yet'.
