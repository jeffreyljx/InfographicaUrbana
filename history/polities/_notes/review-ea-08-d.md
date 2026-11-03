# Review of batch ea-08-d

Reviewer: Phase B adversarial reviewer, 2026-10-25. Dossiers: anti-kuomintang-coalition, communist-party-of-china, people-s-republic-of-china. All three validate (`--resolve`; CPC has 6 gazetteer warnings for Suide, Yan'an and Dabie Mountains). The reviewer applied small fixes where marked `applied: true` and re-validated; everything else is for the author or a gap-filler. Machine copy: history/notes/phase-b/reviews/ea-08-d.json.

## anti-kuomintang-coalition: FAIL

Area: infobox None km2 (None) against Cliopatria 556635 km2, ratio None, acknowledged True. The article is the war's; no area. The author's note states the 2.6x enlargement and the lack of a figure; after removing Hunan it is about 2.2x, still to be stated.

### Findings

- **/keyframe_review/0/correction (also /ledger/0/region and /identity/predecessors/0/land)** (for the author). Hunan is given to the coalition for all of 1930 on the strength of a sentence that describes early 1929, not 1930. Evidence: Central Plains War page: 'Hunan was controlled by the Guangxi clique (in addition to their other lands)' sits in the paragraph on 1929 before the Guangxi clique's March 1929 break (Chiang's protege was driven from the Hunan governorship); in 1930 'the Guangxi Army led by Li Zongren and Bai Chongxi marched northwards and captured Yueyang' in Hunan and was forced back to Guangxi, so Hunan was a front, not coalition land. The adjusted 1.4 M km2 shape therefore includes about 210,000 km2 the page does not give to the coalition. Fix: Remove {admin1 Hunan} from the union in /keyframe_review/0/correction, /ledger/0/region and /identity/predecessors/0/land; keep Hunan in the contest zone (/ledger/1, /ledger/5, /wars/0/zones); restate the adjusted area (about 1.2 M km2) in the keyframe note; optionally add Yueyang as a confidence-1 gain and loss inside May-November 1930.
- **/ledger/4/counterpart and /wars/0/belligerents** (applied by reviewer). Counterpart and belligerents were free-text clique names although the ea-08-x dossiers fengtian-clique, shanxi-clique and guominjun now exist. Evidence: history/polities/fengtian-clique.json, shanxi-clique.json and guominjun.json exist (fengtian-clique /ledger/18: 1930-9 gain of 'Peking, Tianjin and Hebei'). Fix: Set to the slugs fengtian-clique, shanxi-clique, guominjun ('Guangxi clique' stays text: no dossier).

### Thin (for a gap-filler)

- /ledger (May-November 1930): Yueyang's capture and loss (undated on the page) and the date of the Beijing government (Enlarged Conference, September 1930). Try https://en.wikipedia.org/wiki/Yan_Xishan

### Spot checks

/ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /keyframe_review/0/correction (Hunan) not on page for 1930 (the sentence describes 1929).

## communist-party-of-china: FAIL

Area: infobox 70000 km2 (1933) against Cliopatria 297451 km2, ratio 4.25, acknowledged True. Chinese Communist Party article has no area; the Chinese Soviet Republic page gives 'approximately 70,000 square kilometers' at the 1933 peak. Acknowledged and resolved in /keyframe_review/1 (scattered soviets kept).

### Findings

- **/keyframe_review/0/correction and /ledger/0/region** (for the author). The 1931 keyframe uses the Chinese Communists 1930-1931 shape, which does not contain the capital Ruijin and omits the soviets the Republic was proclaimed over, so the 1931 to 1932 growth from 38,942 to 297,451 km2 (168 to 1,330 cells: Henan 138, Hubei 180, Anhui 124, Fujian 145, Zhejiang 58, Guangdong 44, Chongqing 143) has no ledger event. Evidence: shapes.csv: chinese-communists_1930 bbox 113.58-115.28 E, 25.68-28.96 N (139 cells in Jiangxi, 29 in Hunan); the capital entry puts Ruijin at 116.03 E, outside it. Chinese Soviet Republic page names the Minzhegan, Xianggan, Xiang'egan, Honghu, Xiang'echuanqian, Eyuwan, Eyushan, Shaanxi-Gansu, Sichuan-Shaanxi and Hailufeng soviets as its territories and says the Eyuwan soviet 'failed to send delegates' to the founding conference, so they existed in November 1931. The ledger has no event between /ledger/0 (1931-11) and /ledger/1 (1933). Fix: Either make the 1931 keyframe and the found region Cliopatria's 1932 'Communist Party of China' shape (the soviets the Republic was proclaimed over, confidence 2), or keep the 1931 shape and add a 1932 gain (counterpart republic-of-china, confidence 1-2, CSR page) for the soviets outside Jiangxi; in both cases make sure Ruijin is inside the 1931 land.
- **/wars** (for the author). The Second Sino-Japanese War (1937-1945), the war in which the Communist base areas were built, is missing. Evidence: Chinese Civil War page: 'In occupied areas, the Communists established military and political bases from which it carried out guerilla warfare.' The 1938-1945 to 1945 keyframes grow from about 45,000 km2 to the 607,731 km2 proxy with only the confidence-1 /ledger/11 to explain it. Fix: Add the war (1937-1945; belligerents communist-party-of-china, empire-of-japan, with republic-of-china as ally) with zones for the base areas behind Japanese lines (Shanxi, Hebei, Shandong as in the 1945 keyframe), or explain in its note why no zone can be named.
- **/ledger/11/counterpart** (for the author). The 1945 gain of the 19 base areas names republic-of-china as counterpart, but the page puts the bases in Japanese-occupied areas. Evidence: Same sentence ('In occupied areas...'). republic-of-china has no 1945 loss to the Communists; instead it ends Japan's occupation of the same land in September 1945 (republic-of-china /ledger/73 'the rest of North China, Shandong and Shanxi', /ledger/69 'Beiping, Tianjin and Hebei'), so the two dossiers claim the base areas at once. Fix: Counterpart empire-of-japan (the occupied zone), dated within 1937-1945, and a note to ea-08-c that its September 1945 occupation_end regions should exclude the Communist base areas (or the CPC holds them as contest zones).
- **/ledger/27/counterpart** (for the author). Taiyuan is taken from republic-of-china, but the shanxi-clique dossier (ea-08-x) holds Taiyuan until April 1949 and dissolves into this state; its 1948 loss of 'most of Shanxi' to this state has no mirror here. Evidence: shanxi-clique /ledger/9 (1948, loss to communist-party-of-china, 'most of Shanxi, outside Taiyuan and Datong') and /ledger/10 (1949-4, dissolve to communist-party-of-china). The 1947 to 1948 keyframes grow Shanxi from 196 to 780 of 798 cells with no event. Fix: Counterpart shanxi-clique for /ledger/27; add a 1948 gain from shanxi-clique for Shanxi outside Taiyuan and Datong (confidence 1 unless a page dates it); consider shanxi-clique among the predecessors.
- **/keyframe_review/4/correction** (for the author). The correction removes Xinjiang and Qinghai but leaves stray cells of the same Xinjiang strip: 5 cells in Kazakhstan and 4 in Mongolia (the corrected shape is 193 cells: Shaanxi 158, Gansu 17, Inner Mongolia 2, Shanxi 1, Kazakhstan 5, Mongolia 4). Evidence: Resolved with tools/gazetteer.py against the correction as written. Fix: Subtract {country Kazakhstan} and {country Mongolia} too, or intersect the shape with Shaanxi, Gansu and Ningxia.

### Thin (for a gap-filler)

- /keyframe_review/1 to /keyframe_review/2: The ends of the Eyuwan, Xiang'exi/Honghu, Minzhegan and Hailufeng soviets: the 1932 shape's cells in Henan, Hubei, Anhui, Zhejiang, Hunan and Guangdong vanish by 1935 with no loss event (only Jiangxi-Fujian in 1934 and Sichuan-Shaanxi in 1935 are lost). Try https://en.wikipedia.org/wiki/Eyuwan_Soviet
- /ledger/11: Confidence-1 event: where and when the 19 base areas (Jin-Cha-Ji, Jin-Sui, Ji-Lu-Yu, Shandong) were won. Try https://en.wikipedia.org/wiki/Eighth_Route_Army
- /keyframe_review/7 to /keyframe_review/8: 1948 gains with no event: Inner Mongolia (1,855 to 4,348 cells), Shandong (322 to 714; Jinan, September 1948), Hebei (321 to 847), Shanxi (see the shanxi-clique fix); the recapture of Yan'an (April 1948). Try https://en.wikipedia.org/wiki/Jinan_campaign
- /keyframe_review/8 to /keyframe_review/9: 1949 gains with no event: Henan (259 to 816 cells), Hubei and Wuhan, Shanghai, Xi'an (Shaanxi 409 to 656). Try https://en.wikipedia.org/wiki/Shanghai_campaign
- /identity/capitals: No seat for 1935 (Wayaobao) or 1948 (Xibaipo). Try https://en.wikipedia.org/wiki/Xibaipo

### Spot checks

/ledger/6 confirmed; /ledger/10 confirmed; /ledger/13 confirmed; /ledger/19 confirmed; /ledger/0 confirmed; /ledger/3 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/15 confirmed; /ledger/16 confirmed; /ledger/22 confirmed; /ledger/26 confirmed; /ledger/27 confirmed.

## people-s-republic-of-china: THIN

Area: infobox 9596961 km2 (2024) against Cliopatria 9399444 km2, ratio 0.98, acknowledged True. China page infobox 'Total: 9,596,961 km2'; matches /keyframe_review/11.

### Findings

- **/ledger/13/month and /ledger/14/month (with /sources)** (applied by reviewer). Hong Kong and Macau transfers carried the year only. Evidence: Handover of Hong Kong page: the handover 'occurred at midnight on 1 July 1997'; Transfer of sovereignty over Macau page: it 'officially occurred at midnight on 20 December 1999'. Fix: month 7 and month 12, sources switched to those pages and added to sources[].
- **/ledger/4/region (with /ledger/8/region)** (for the author). The confidence-1 December 1949 gain from republic-of-china includes all 991 Xizang cells of Cliopatria's 1950 shape, among them the 361 cells of the Chamdo region that /ledger/6 occupies from Tibet only in October 1950. Evidence: Annexation of Tibet page: 'on 7 October 1950, Chinese troops advanced into eastern Tibet, crossing the border at five places'; infobox: 'U-Tsang and Chamdo Region of Kham came under the control of China'. tibet /ledger/42-43 occupy and release 'Chamdo and western Kham'; Cliopatria's Tibet 1951 shape has none of these cells, so /ledger/8 never hands Chamdo over either. Fix: Subtract {admin1 Xizang, country China} from /ledger/4 (minus [PRC 1950, union(CPC 1949, Xizang)]); make /ledger/8 the union of {cliopatria Tibet 1951} and the Xizang cells of the 1950 PRC shape; optionally widen /ledger/6-7 to those cells.

### Thin (for a gap-filler)

- /ledger/4: Confidence-1 lump: dates for Xinjiang (September-October 1949), Gansu, Qinghai, Ningxia, Yunnan, Guizhou, Guangxi, Fujian, Zhejiang. Try https://en.wikipedia.org/wiki/Incorporation_of_Xinjiang_into_the_People%27s_Republic_of_China
- /ledger (1950): Zhoushan (May 1950) and the Wanshan Islands (May-August 1950): both are on the Chinese Civil War page already opened; republic-of-china /ledger/98 carries the Zhoushan loss. Try https://en.wikipedia.org/wiki/Chinese_Civil_War
- /ledger (1955): Dachen Islands and Yijiangshan (February 1955), mirror of republic-of-china /ledger/99. Try https://en.wikipedia.org/wiki/First_Taiwan_Strait_Crisis
- /ledger (1974): Paracel Islands (January 1974), mirror of republic-of-vietnam /ledger/6. Try https://en.wikipedia.org/wiki/Battle_of_the_Paracel_Islands
- /ledger and /wars (1979, 1999): Sino-Vietnamese War contest (February-March 1979) and the 1999 land border treaty, mirrors of socialist-republic-of-vietnam /ledger/6, 7, 9. Try https://en.wikipedia.org/wiki/Sino-Vietnamese_War
- /ledger (2002-2011): Gains from kazakhstan (2002-5), kyrgyzstan (2009, gain and loss) and republic-of-tajikistan (2011-1), all already in those dossiers. Try https://en.wikipedia.org/wiki/China%E2%80%93Tajikistan_border
- /ledger/12/month: Month of the 1963 agreement (islamic-republic-of-pakistan /ledger/10 says March). Try https://en.wikipedia.org/wiki/Sino-Pakistan_Agreement
- /wars: Korean War (PLA in North Korea from October 1950), Sino-Soviet border conflict (1969); not on the China page, so not a fault, but they belong in wars. Try https://en.wikipedia.org/wiki/Chinese_People%27s_Volunteer_Army
- /ledger/9: First year of Chinese control of Aksai Chin (confidence 2, road year used). Try https://en.wikipedia.org/wiki/Aksai_Chin

### Spot checks

/ledger/8 confirmed; /ledger/6 confirmed; /ledger/5 confirmed; /ledger/3 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/12 confirmed; /ledger/13 confirmed (year; month added from Handover of Hong Kong); /ledger/14 confirmed (year; month added from Transfer of sovereignty over Macau).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| anti-kuomintang-coalition 1930 gain (republic-of-china) | republic-of-china   | missing | Jinan, 25 June 1930: no loss in republic-of-china (ea-08-c). |
| anti-kuomintang-coalition 1930 loss (republic-of-china) | republic-of-china   | missing | Jinan, 15 August 1930: no gain in republic-of-china. |
| anti-kuomintang-coalition 1930 loss (fengtian-clique) | fengtian-clique 1930 gain | mismatch | fengtian-clique /ledger/18 (1930-9) takes Peking, Tianjin and Hebei from shanxi-clique, not from the coalition: the coalition (Cliopatria row) and the ea-08-x clique dossiers shanxi-clique and guominjun cover the same land in 1930; the orchestrator should decide the layering. |
| anti-kuomintang-coalition 1930 dissolve (republic-of-china) | republic-of-china   | mismatch | republic-of-china has contest_end (1930-11) but no gain of the coalition's land; guominjun /ledger/13 dissolves into republic-of-china in November 1930, shanxi-clique continues. |
| communist-party-of-china 1931 found (chinese-communists) | chinese-communists 1931 dissolve | matched | chinese-communists /ledger/2 (1931-11). |
| communist-party-of-china 1934 loss (republic-of-china) | republic-of-china   | missing | Jiangxi-Fujian soviet, November 1934: no gain in republic-of-china. |
| communist-party-of-china 1935 loss (republic-of-china) | republic-of-china   | missing | Sichuan-Shaanxi base, March 1935: no gain in republic-of-china. |
| communist-party-of-china 1935 gain (Northern Shaanxi Soviet) | -   | exception | No dossier; listed in counterparts_needing_dossiers. |
| communist-party-of-china 1939 gain (republic-of-china) | republic-of-china   | missing | Suide, spring 1939: no loss in republic-of-china; the same page has the KMT taking 'much of eastern Gansu', which neither dossier records. |
| communist-party-of-china 1945 gain (republic-of-china) | republic-of-china 1945 occupation_end | mismatch | The base areas were in Japanese-occupied land; republic-of-china /ledger/69-77 end Japan's occupation of the same North China land in 1945-9 with no loss to the Communists. Counterpart should be empire-of-japan. |
| communist-party-of-china 1947 loss (republic-of-china) | republic-of-china 1947 gain | matched | Yan'an, republic-of-china /ledger/85 (1947-3). |
| communist-party-of-china 1948 gain (republic-of-china) | republic-of-china   | missing | Luoyang, April 1948: no loss in republic-of-china. |
| communist-party-of-china 1948 gain (republic-of-china) | republic-of-china 1948 loss | matched | Jinzhou, Changchun (1948-10) and Manchuria (1948-11) against republic-of-china /ledger/89 (1948-11). |
| shanxi-clique 1948 loss (communist-party-of-china) | communist-party-of-china   | missing | shanxi-clique /ledger/9 'most of Shanxi' has no gain here. |
| communist-party-of-china 1949 gain (republic-of-china) | republic-of-china 1949 loss | matched | Beiping, Tianjin, Hebei: republic-of-china /ledger/90 (1949-1). |
| communist-party-of-china 1949 gain (republic-of-china) | republic-of-china 1949 loss | matched | Xuzhou (1949-1) against republic-of-china /ledger/91 'east-central China: Shandong, Henan and Anhui': same month, the land differs (CPC names only Xuzhou). |
| communist-party-of-china 1949 gain (republic-of-china) | republic-of-china 1949 loss | matched | Nanjing and Jiangsu (1949-4) against republic-of-china /ledger/92, which also gives Shanghai and Zhejiang. |
| communist-party-of-china 1949 gain (republic-of-china) | shanxi-clique 1949 dissolve | mismatch | Taiyuan (1949-4): shanxi-clique /ledger/10 dissolves into communist-party-of-china; counterpart should be shanxi-clique. |
| communist-party-of-china 1949 dissolve (people-s-republic-of-china) | people-s-republic-of-china 1949 found | matched | 1 October 1949. |
| people-s-republic-of-china 1949 gain (republic-of-china) | republic-of-china 1949 loss | matched | Guangzhou, Chongqing, Chengdu and the rest (1949-10 to 12) against republic-of-china /ledger/94 (1949-10). |
| people-s-republic-of-china 1950 gain (republic-of-china) | republic-of-china 1950 loss | matched | Hainan, republic-of-china /ledger/97 (1950-4). |
| republic-of-china 1950 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | Zhoushan, republic-of-china /ledger/98 (1950-5): no gain in the PRC dossier. |
| people-s-republic-of-china 1950 occupation_start (tibet) | tibet 1950 occupation_start | matched | Chamdo, tibet /ledger/42 (1950-10); but /ledger/4 already gives the PRC the Chamdo cells in 1949-12 from republic-of-china (see the fix). |
| people-s-republic-of-china 1951 occupation_end (tibet) | tibet 1951 occupation_end | matched | tibet /ledger/43 (1951-5). |
| people-s-republic-of-china 1951 gain (tibet) | tibet 1951 dissolve | matched | tibet /ledger/44 dissolve (1951-5), successor people-s-republic-of-china. |
| republic-of-china 1955 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | Dachen and Yijiangshan, republic-of-china /ledger/99 (1955-2). |
| people-s-republic-of-china 1957 gain (republic-of-india) | republic-of-india   | mismatch | Aksai Chin: republic-of-india has no loss, and its Cliopatria shapes hold only 3-4 of the 108 cells; either counterpart nobody (India claimed but did not hold it) or India adds the loss (sa-06). |
| people-s-republic-of-china 1962 contest_start (republic-of-india) | republic-of-india 1962 contest_start | matched | republic-of-india /ledger/16-17 (1962-10 to 11). |
| people-s-republic-of-china 1963 gain (islamic-republic-of-pakistan) | islamic-republic-of-pakistan 1963 loss | matched | islamic-republic-of-pakistan /ledger/10 (1963-3); the land differs (3 cells there, the whole Karakoram strip here). |
| republic-of-vietnam 1974 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | Paracels, republic-of-vietnam /ledger/6 (1974-1). |
| socialist-republic-of-vietnam 1979 contest_start (people-s-republic-of-china) | people-s-republic-of-china   | missing | socialist-republic-of-vietnam /ledger/6-7 (1979-2 to 3). |
| socialist-republic-of-vietnam 1999 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | socialist-republic-of-vietnam /ledger/9 (1999). |
| people-s-republic-of-china 1997 gain (british-colonial-empire) | -   | exception | Hong Kong: british-colonial-empire (eu-11) not written yet. |
| people-s-republic-of-china 1999 gain (portugal) | -   | exception | Macau: portugal (eu-22) not written yet. |
| kazakhstan 2002 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | kazakhstan /ledger/2 (2002-5). |
| kyrgyzstan 2009 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | kyrgyzstan /ledger/2 (loss) and /ledger/3 (gain), 2009. |
| republic-of-tajikistan 2011 loss (people-s-republic-of-china) | people-s-republic-of-china   | missing | republic-of-tajikistan /ledger/3 (2011-1). |

## Problems and notes for the orchestrator

- No page failed to load. Pages opened: Central Plains War, Chinese Soviet Republic, Long March, Shaan-Gan-Ning Border Region, Chinese Civil War, Annexation of Tibet by the PRC, Sino-Indian War, Special administrative regions of China, China, Handover of Hong Kong, Transfer of sovereignty over Macau.
- Neighbour dossiers not yet written (counterparts owned by groups that have not run): british-colonial-empire, portugal, estado-novo, russian-federation, union-of-myanmar, union-of-soviet-socialist-republics.
- Overlap for the orchestrator: anti-kuomintang-coalition (Cliopatria row, 1930) covers the same land as the ea-08-x dossiers shanxi-clique and guominjun in 1930 (both already note the overlap); decide which layer draws 1930.
- Since the author wrote, ea-08-x created fengtian-clique, shanxi-clique and guominjun; the reviewer replaced the coalition's free-text counterpart and belligerents with those slugs. guangxi-clique still has no dossier.
- The author's report lists the Pakistan 1963 mirror as lacking in the PRC dossier, but /ledger/12 holds it; the report line is stale.

Gazetteer names needed: Yan'an (place, communist-party-of-china), Suide (place, communist-party-of-china), Dabie Mountains (region, communist-party-of-china), Ruijin (place, communist-party-of-china), Bao'an (Zhidan) (place, communist-party-of-china), Aksai Chin (region, people-s-republic-of-china).
