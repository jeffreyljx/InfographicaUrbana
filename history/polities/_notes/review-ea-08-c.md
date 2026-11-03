# Review of batch ea-08-c (Qing to the People's Republic, part c)

Reviewed 2026-10-20 by the adversarial reviewer (brief filled 2026-10-19). Machine copy: history/notes/phase-b/reviews/ea-08-c.json. All six dossiers validate (0 errors) before and after the reviewer's small fixes.

| dossier | verdict |
| --- | --- |
| taiping-heavenly-kingdom | thin |
| panthay-rebellion | thin |
| republic-of-china | fail |
| empire-of-china | fix |
| kuomintang | fail |
| chinese-communists | thin |

Fixes marked "applied" were made by the reviewer in place (orchestrator rule: small fixes verified on the page) and re-validated; the others are for the author. A dossier with an unapplied fix is "fail".

## taiping-heavenly-kingdom: thin

Area: infobox None (None), Cliopatria 347846, ratio None. Neither infobox gives an area (checked on Taiping_Heavenly_Kingdom); the author says so in notes and checks the peak against the 30 million people.

Thin (for a gap-filler):
- `/keyframe_review/6`: The 1861 shape grows from 283,395 to 347,846 km2 and reaches west to 113.5 E and south to 27.2 N (Li Xiucheng's western campaign into Jiangxi and Hubei); only Ningbo and Hangzhou (December 1861) are in the ledger, so the western gain and its loss before the 1862 shape (west edge 116.8 E) have no events. Page to try: https://en.wikipedia.org/wiki/Li_Xiucheng
- `/ledger/8`: Hangzhou is gained on 19 March 1860 and gained again on 31 December 1861 with no loss between; the 1860 withdrawal from Hangzhou needs an event (or Hangzhou leaves the 1860 gain). Page to try: https://en.wikipedia.org/wiki/Li_Xiucheng
- `/ledger/15`: Confidence 1: the Qing recapture of Suzhou, Changzhou and Hangzhou is put in 1864 without a page; if Suzhou fell in 1863 it belongs inside the 1862-1863 shape. Page to try: https://en.wikipedia.org/wiki/Charles_George_Gordon

Spot checks:
- `/ledger/1` Taiping_Rebellion: confirmed (Wuchang, December 1852)
- `/ledger/3` Taiping_Rebellion: confirmed (Nanjing, 19 March 1853)
- `/ledger/5` Taiping_Rebellion: confirmed (Wuchang retaken December 1856)
- `/ledger/6` Taiping_Rebellion: confirmed (Jiujiang May 1858, rest of Jiangxi by September)
- `/ledger/8` Taiping_Rebellion: confirmed (Hangzhou 19 March, Changzhou 26 May, Suzhou 2 June 1860)
- `/ledger/11` Taiping_Rebellion: confirmed (Ningbo 9 December, Hangzhou 31 December 1861)
- `/ledger/13` Taiping_Rebellion: confirmed (Ningbo reclaimed 10 May 1862)
- `/ledger/9` Taiping_Heavenly_Kingdom: confirmed (attempt on Shanghai August 1860)

## panthay-rebellion: thin

Area: infobox None (None), Cliopatria 408545, ratio None. Panthay_Rebellion infobox has no area (checked); all four shapes (342-409 thousand km2, as large as Yunnan) are adjusted to western Yunnan in the corrections.

Fixes:
- `/ledger/2 (original numbering; removed)` (applied by reviewer): The 1863 rename event ("the rebels take the name Pingnan") misreads the page: the Pingnan title of 1863 is Ma Dexin's, at Kunming, not a rename of Du Wenxiu's Dali state. Evidence: Ma_Rulong_(Qing_general) and Du_Wenxiu: "In 1863 Ma Dexin declared himself King-Who-Pacifies-the-South (Pingnan Wang)", after rebels under Ma Rong and Ma Liansheng stormed Kunming; Panthay_Rebellion: "The rebels identified their nation as Pingnan Guo" (undated) and the Du Wenxiu infobox styles him "Sultan of Pingnan Guo (Dali)". The page gives no 1863 name change of the Dali state. Fix: Remove the rename event; the name Pingnan Guo stays in native_names (undated). Done by the reviewer; dossier re-validated (5 events).
- `/wars/0/to` (applied by reviewer): The Panthay Rebellion war ran to 1873, past the dossier's end (December 1872); wars must lie inside the life. Evidence: identity.end is 1872-12; the war was 1856-1873. Fix: Set to 1872 (the 1873 capture of Dali is already in the successor note). Done by the reviewer.

Thin (for a gap-filler):
- `/keyframe_review/2`: The 1868-1870 correction adds Tengyue (Tengchong, the Sladen mission's Momien, May-July 1868) but no ledger event gains it, and the 1859-1867 correction leaves it out; either date its conquest or put it in the 1859-67 correction too. Page to try: https://en.wikipedia.org/wiki/Tengchong
- `/keyframe_review/3`: The 1871-1872 correction shrinks to the Dali basin, but no loss event takes Lijiang, Zhongdian, Heqing or Tengyue back for the Qing; only the 1871 contest_start covers it. Page to try: https://en.wikipedia.org/wiki/Cen_Yuying
- `/ledger/1`: Confidence 2: the 1860 peak is dated but the towns are not (Yongchang, Chuxiong, Lijiang); the Kunming changes of hands (rebels under Ma Rong and Ma Liansheng stormed Kunming after Ma Rulong left) are not in the ledger. Page to try: https://en.wikipedia.org/wiki/Cen_Yuying

Spot checks:
- `/ledger/0` Du_Wenxiu: confirmed (generalissimo 23 October 1856 after the Hui took Dali)
- `/ledger/1` History_of_Yunnan: confirmed ("high-water mark ... in 1860")
- `/ledger/2 (original)` Ma_Rulong_(Qing_general): not on page as claimed (the 1863 Pingnan Wang is Ma Dexin at Kunming); confidence 2, removed
- `/ledger/3 (original; now /ledger/2)` History_of_Yunnan: confirmed ("By 1871, it was directing a campaign...")
- `/ledger/4 (original; now /ledger/3)` Du_Wenxiu: confirmed (Dali encircled 25 December 1872; reign ends 26 December)

## republic-of-china: fail

Area: infobox 11364389 (1912), Cliopatria 8440208, ratio 0.74. Read on Republic_of_China_(1912-1949): 11,364,389 km2 (1912) and 9,665,354 km2 (1946, Cliopatria 6,451,821, ratio 0.67); both within a factor of two and explained in /keyframe_review/0 and /19 (the infobox counts Outer Mongolia and Tibet).

Fixes:
- `/ledger/60/counterpart` (applied by reviewer): The loss of Nanjing, Jiangsu, Shanghai and Zhejiang in April 1949 was given to people-s-republic-of-china, which did not exist until 1 October 1949. Evidence: https://en.wikipedia.org/wiki/Chinese_Civil_War: "On 23 April, they captured the KMT's capital, Nanjing"; "On 1 October 1949, Mao Zedong officially proclaimed the People's Republic of China". The January 1949 losses (/ledger/58-59) already use communist-party-of-china. Fix: Counterpart communist-party-of-china. Done by the reviewer; re-validated.
- `/ledger/15` (author): Mis-dated (confidence 2): Shaanxi and Henan are lost to the Nationalist side in 1928, but the page has Feng Yuxiang's Guominjun leaving its Shaanxi base and taking Luoyang on 28 May 1927. Evidence: https://en.wikipedia.org/wiki/Northern_Expedition: "the Guominjun took Luoyang" (28 May 1927), after leaving its Shaanxi base; the 1928 division of realms the note quotes is the end state, not the date of the change. Fix: Date the loss 1927-05 (mirror kuomintang /ledger/20), and either take Shaanxi and (western) Henan out of the 1927 keyframe correction (/keyframe_review/8) or say in its note that they left in May 1927.
- `/keyframe_review/4` (author): Yunnan, Guizhou and Guangxi are outside the restored Republic in the 1916 keyframe (/keyframe_review/3) and back inside it in 1917 (/keyframe_review/4: the 1914 outline less Guangdong), with no ledger event between: about 0.8 million km2 unexplained. Evidence: https://en.wikipedia.org/wiki/National_Protection_War: on 14 July 1916 "the National Protection War was ended, with the provinces rescinding their declarations of independence"; /keyframe_review/3 itself says they were independent "till the war ended on 14 July". Fix: Add a 1916-07 gain, counterpart "National Protection Army (Yunnan, Guizhou, Guangxi)", region the union of the three provinces, confidence 3, source National_Protection_War (add it to sources[]).
- `/ledger (1938-1945 occupations)` (author): Five Japanese occupations of the Republic's land that empire-of-japan records have no mirror here, although the Republic mirrors the other five with the same region specs: Shandong and Shanxi 1938-03 (empire-of-japan /ledger/49, end /ledger/92), Kaifeng and the Henan plain 1938-06 (/ledger/50, end /ledger/93), the Guangdong coast and Canton 1938-10 (/ledger/52, end /ledger/96), Hainan 1939 (/ledger/53, end /ledger/97), Guangxi 1944-09 (/ledger/73, end /ledger/99). Evidence: Rule 3 of the reviewer brief: an occupation in X's land is an occupation in X's ledger. /keyframe_review/13 explains the 1938-1939 fall (4.47 to 4.19 million km2) by Hainan, Nanchang and Nanning, none of which is in the ledger; the author's notes list these as "see empire-of-japan". Fix: Add the five occupation_start and five occupation_end events (counterpart empire-of-japan), copying empire-of-japan's region specs and years; confidence 2, source Second_Sino-Japanese_War (or the page empire-of-japan cites, added to sources[]).
- `/ledger (1922)` (author): No gain of Tsingtao (Qingdao) and the Kiautschou leased territory, which empire-of-japan gives back to the Republic in December 1922 (empire-of-japan /ledger/37, confidence 3). Evidence: Mirror rule; empire-of-japan /ledger/37: loss, counterpart republic-of-china, 1922-12, region Qingdao 30 km within its 1915 shape. Fix: Add a 1922-12 gain from empire-of-japan with the same region, confidence 2, citing empire-of-japan's page.
- `/keyframe_review/10/note` (author): The note says Rehe leaves "in steps that the ledger dates to 1933 and the East Hebei and Mengjiang events of 1935-36", but the ledger has no East Hebei event. Evidence: empire-of-japan /ledger/44 (1935-11 vassal_start east-hebei-autonomous-council, eastern Hebei) and /ledger/48 (1938-02 vassal_end); nothing in this ledger between 1933-03 and 1936-05. Fix: Add a 1935-11 loss of eastern Hebei to east-hebei-autonomous-council (region as empire-of-japan /ledger/44; counterpart needs a dossier, ea-08-x), or correct the note.
- `/ledger (1945-08)` (author): Inner Mongolia (lost to mengjiang 1936-05, /ledger/36) and Rehe (lost to manchukuo 1933-03, /ledger/35) never come back, though the 1946 shape holds Inner Mongolia and Japan ends both vassals in August 1945 (empire-of-japan /ledger/85, /ledger/87). Evidence: Mirror rule and keyframe consistency: /keyframe_review/18 to /19 grows by 1.0 million km2 and only Taiwan, Penghu and the occupation ends explain it. Fix: Add 1945-08 gains from mengjiang (the region of /ledger/36) and from manchukuo (Rehe, the region of /ledger/35), confidence 2, source Manchukuo (dissolution 20 August 1945) and Second_Sino-Japanese_War.
- `/ledger (Tibet 1912-1933)` (author): tibet records a Republican occupation of Kham west of the Dri river 1912-08 to 1918 (tibet /ledger/33, /ledger/36) and the Sino-Tibetan War contest 1930-05 to 1933 (tibet /ledger/37, /ledger/38) with this state as counterpart; none is here. Evidence: Mirror rule (both dossiers exist). Fix: Add occupation_start 1912-08 and occupation_end 1918 (counterpart tibet, the region of tibet /ledger/33, confidence 1-2) and contest_start 1930-05 / contest_end 1933 (counterpart tibet, the region of tibet /ledger/37), and the Sino-Tibetan War in wars[].
- `/ledger (Xinjiang 1912-1946)` (author): Three Xinjiang neighbours have no mirror: kumul-khanate is a vassal of the Republic 1912 to 1930-06 and then abolished into it (kumul-khanate /ledger/3-5); first-east-turkestan-republic is founded on the Republic's land 1933-11 and dissolved back into it 1934-02 (/ledger/0-1, Kashgar, Aksu, Hotan); east-turkestan-republic contests the Manasi front 1945-09 to 1946-01 (/ledger/2-3). Evidence: Mirror rule (all three dossiers exist). Fix: Add vassal_start 1912 and vassal_end 1930-06 (counterpart kumul-khanate, Hami 120 km) with a 1930-06 gain of Hami; a 1933-11 loss and 1934-02 gain (counterpart first-east-turkestan-republic, its region); contest_start 1945-09 and contest_end 1946-01 (counterpart east-turkestan-republic, Shihezi 120 km). Confidence 2, citing the neighbours' pages.
- `/ledger (1945-1947 outside China)` (author): Three more mirrors are missing: the Nationalist occupation of northern Vietnam 1945-08 to 1946-06 (democratic-republic-of-vietnam /ledger/0, /ledger/2), the return of Guangzhouwan by French Indochina in 1945 (french-indochina /ledger/31) and the Baitag Bogd occupation 1947-06 to 1947-07 (mongolian-people-s-republic /ledger/5-6). Evidence: Mirror rule (all three dossiers exist). Fix: Add occupation_start/occupation_end with counterpart democratic-republic-of-vietnam (its region spec), a 1945 gain from french-indochina (Guangzhouwan, its region spec) and occupation_start/occupation_end with counterpart mongolian-people-s-republic (Baitag Bogd 60 km).

Thin (for a gap-filler):
- `/ledger/6`: Confidence 1 (Outer Mongolia 1919): great-mongol-state dates it 1919-11 at confidence 3; raise to 2 with month 11 and cite its page. Page to try: https://en.wikipedia.org/wiki/Occupation_of_Mongolia
- `/ledger/7`: Confidence 1 (Outer Mongolia lost 1921): great-mongol-state has 1921-02 (Urga) and 1921-03 (rest). Page to try: https://en.wikipedia.org/wiki/Occupation_of_Mongolia
- `/ledger/20-25, /ledger/30, /ledger/32`: Confidence 1: the 1930 return of the Cliopatria row, the four allied realms as vassals, the Ruijin loss and the 1931 end of the Central Plains War contest and of the Fengtian relation. Page to try: https://en.wikipedia.org/wiki/Central_Plains_War
- `/ledger/45`: Confidence 1: the Ili rising, from east-turkestan-republic (1944-11, confidence 2). Page to try: https://en.wikipedia.org/wiki/Ili_Rebellion
- `/ledger/52`: Confidence 1, and the counterpart is doubtful: the Nationalists took the southern Manchurian cities from the withdrawing Soviet army (/ledger/53), not from the communists. Page to try: https://en.wikipedia.org/wiki/Soviet_occupation_of_Manchuria
- `/ledger (1955)`: The loss of the Dachen and Yijiangshan islands (1955) is not in the ledger; the 1951-2023 keyframe ignores them. Page to try: https://en.wikipedia.org/wiki/First_Taiwan_Strait_Crisis
- `/keyframe_review/0`: Tibet 1912-1913 (the 1912 shape holds 23 percent of Xizang) is not explained; mirror the tibet dossier once the Kham events are in. Page to try: https://en.wikipedia.org/wiki/Tibet_(1912%E2%80%931951)

Spot checks:
- `/ledger/9` Northern_Expedition: confirmed (Hunan under complete KMT control after Yuezhou, 22 August 1926)
- `/ledger/10` Northern_Expedition: confirmed (Wuchang surrendered 10 October 1926)
- `/ledger/14` Northern_Expedition: confirmed (Shanghai 22 March, Nanjing 24 March 1927)
- `/ledger/15` Northern_Expedition: mis-dated (Guominjun took Luoyang 28 May 1927; confidence 2: fix listed)
- `/ledger/17` Northern_Expedition: confirmed (Beijing 6 June 1928)
- `/ledger/18` Northern_Expedition: confirmed (Zhang Xueliang 29 December 1928)
- `/ledger/33` Manchukuo: confirmed (established 1 March 1932)
- `/ledger/35` Manchukuo: confirmed (Rehe annexed 4 March 1933)
- `/ledger/43` Sheng_Shicai: confirmed (October 1943)
- `/ledger/55` Chinese_Civil_War: confirmed (Yan'an, March 1947)
- `/ledger/57` Chinese_Civil_War: confirmed (Liaoshen; Shenyang 1 November 1948)
- `/ledger/60` Chinese_Civil_War: confirmed (Nanjing 23 April 1949; counterpart corrected)
- `/ledger/65` Chinese_Civil_War: confirmed (Hainan April 1950)
- `/ledger/66` Chinese_Civil_War: confirmed (Zhoushan May 1950)

## empire-of-china: fix

Area: infobox None (None), Cliopatria 8439386, ratio None. No infobox area (checked); the shape is the 1914-15 Republic outline, and the correction removes Yunnan.

Fixes:
- `/wars/0/from` (applied by reviewer): The National Protection War starts in 1915, before the dossier's start (January 1916); wars must lie inside the life. Evidence: identity.start is 1916-01; Yunnan's rising (25 December 1915) is already the loss at the start. Fix: Set from to 1916. Done by the reviewer; re-validated.

Spot checks:
- `/ledger/0` Empire_of_China_(1915%E2%80%931916): confirmed (declared 12 December 1915; accession rites delayed to 1 January 1916)
- `/ledger/1` National_Protection_War: confirmed (Kunming, 25 December 1915)
- `/ledger/2` National_Protection_War: confirmed at confidence 2 (Guizhou and Guangxi "between January" and "March 1916", no day)
- `/ledger/3` Empire_of_China_(1915%E2%80%931916): confirmed (abandoned 22 March; Republic restored 23 March 1916; 83 days)

## kuomintang: fail

Area: infobox None (None), Cliopatria 8097454, ratio None. Kuomintang is a party article without an area (checked). The 1917-1924 shapes (5.0-6.6 million km2) are marked wrong and corrected to Guangdong, in the notes.

Fixes:
- `/keyframe_review/1` (author): The 1918-1919 correction gives Guangdong to this state, while the ledger says Guangdong was lost to the Old Guangxi clique in May 1918 (/ledger/1) and only regained in November 1920 (/ledger/3): keyframe and ledger contradict each other for two and a half years. Evidence: https://en.wikipedia.org/wiki/Constitutional_Protection_Movement: after Sun left in 1918 "The Guangzhou Military Government was now headed by Cen Chunxuan", the southern government "effectively under the influence of the Old Guangxi clique"; "Chen Jiongming expelled the Guangxi clique from Guangzhou allowing Sun to return by the end of November" (1920). Fix: Decide what the state is. If it is the Guangzhou government, it kept Guangdong: drop the 1918 loss and the 1920 gain (keep the 1920 events as a contest or in notes). If it is Sun's party, the 1918-1919 verdict stays wrong but its correction must not be Guangdong (the years belong to the Old Guangxi clique's Guangzhou government, ea-08-x) and /keyframe_review/2 starts with the November 1920 gain.
- `/ledger/25` (author): The 1928 rename does not mirror republic-of-china /ledger/19, which records the Beiyang Republic as merged into this state in 1928-12; and no event of this ledger brings in the provinces between the 1927 correction (south-east China) and the 1928 shape marked ok (7.2 million km2): Anhui, Jiangsu outside Nanjing-Shanghai, Shandong beyond Jinan, Hebei, Sichuan, Yunnan, Guizhou, Gansu, Qinghai, Xinjiang, Inner Mongolia. Evidence: Reviewer brief rule 3 (merge mirrors merge) and rule 4 (a keyframe change needs an event). https://en.wikipedia.org/wiki/Northern_Expedition: on 6 June 1928 the NRA "marched into Beijing, ending the Beiyang government". Fix: Make it a merge with counterpart republic-of-china and the region of republic-of-china's 1927 keyframe (its /keyframe_review/8 correction), and agree a single date with republic-of-china /ledger/19 (June 1928, the end of the Beiyang government, or 29 December 1928).
- `/ledger/20` (author): Mis-dated (confidence 2): the Guominjun's Shaanxi and Henan become a Nationalist realm in 1928, but the page has the Guominjun leaving its Shaanxi base and taking Luoyang on 28 May 1927. Evidence: https://en.wikipedia.org/wiki/Northern_Expedition: "the Guominjun took Luoyang" on 28 May 1927. Fix: Move to 1927-05 (re-sort the ledger) together with republic-of-china /ledger/15.
- `/wars/3/to` (applied by reviewer): The Chinese Civil War (opening) ran to 1949, past the dossier's end (1929); wars must lie inside the life. Evidence: identity.end is 1929-12. Fix: Set to 1929; the rest of the war is in republic-of-china. Done by the reviewer; re-validated.

Thin (for a gap-filler):
- `/ledger/21`: Confidence 1: the 1928 communist base is Cliopatria's row only. Page to try: https://en.wikipedia.org/wiki/Jinggang_Mountains
- `/ledger/26-31`: Confidence 1: the 1929 vassal ends and the dissolve are Cliopatria's row change. Page to try: https://en.wikipedia.org/wiki/Central_Plains_War
- `/keyframe_review/4`: The National Government at Guangzhou (July 1925), the unification of Guangxi under Li Zongren and its pledge to the KMT are undated; Guangxi is drawn from 1926 only. Page to try: https://en.wikipedia.org/wiki/New_Guangxi_clique

Spot checks:
- `/ledger/0` Constitutional_Protection_Movement: confirmed (generalissimo elected 1 September 1917)
- `/ledger/1` Constitutional_Protection_Movement: confirmed for the date (Sun left Guangzhou in 1918); the loss of land is the author's reading, see fix
- `/ledger/3` Constitutional_Protection_Movement: confirmed (Guangxi clique expelled, Sun back by end of November 1920)
- `/ledger/6` Constitutional_Protection_Movement: confirmed (palace shelled 16 June 1922)
- `/ledger/7` Constitutional_Protection_Movement: confirmed (Guangzhou retaken 1923)
- `/ledger/12` Northern_Expedition: confirmed (Nanchang retaken by 9 November 1926)
- `/ledger/14` Northern_Expedition: confirmed (Fuzhou 9 December 1926)
- `/ledger/15` Northern_Expedition: confirmed (Zhejiang by 23 February 1927)
- `/ledger/20` Northern_Expedition: mis-dated (Luoyang 28 May 1927)
- `/ledger/22` Northern_Expedition: confirmed (Jinan 30 April 1928)

## chinese-communists: thin

Area: infobox 70000 (1933), Cliopatria 38942, ratio 0.56. No infobox area; the body gives "approximately 70,000 square kilometers" and "peak in 1933". Within a factor of two, noted in /keyframe_review/0.

Fixes:
- `/wars/0/to` (applied by reviewer): The encirclement campaigns run to 1934, past the dossier's end (November 1931); wars must lie inside the life. Evidence: identity.end is 1931-11. Fix: Set to 1931; the fourth and fifth campaigns belong to communist-party-of-china. Done by the reviewer; re-validated.

Thin (for a gap-filler):
- `/ledger/0`: Confidence 1: the founding of the Jinggang Mountains base is Cliopatria's 1928; the page gives no date. Page to try: https://en.wikipedia.org/wiki/Jinggang_Mountains
- `/ledger/1`: Confidence 1: the move to the Jiangxi-Fujian border around Ruijin is bridged from Cliopatria's 1930 row; if the base was left early in 1929 the 1928-1929 shape (/keyframe_review/0) is wrong for 1929. Page to try: https://en.wikipedia.org/wiki/Jiangxi_Soviet

Spot checks:
- `/ledger/2` Chinese_Soviet_Republic: confirmed (proclaimed 7 November 1931 at Ruijin)
- `/ledger/1` Chinese_Soviet_Republic: confirmed as quoted ("they moved into the border region between Jiangxi and Fujian provinces"; "Beginning in 1929, soviets began to be created"), undated, so confidence 1 is honest
- `/ledger/0` Chinese_Soviet_Republic: confirmed as quoted (base in the Jinggang Mountains), undated

## Cross-dossier matrix: problems only

- mismatch: republic-of-china 1928 merge (counterpart kuomintang). kuomintang /ledger/25 is a rename with no counterpart; it should be a merge with republic-of-china and the Beiyang land
- missing: empire-of-japan 1922 loss (counterpart republic-of-china). empire-of-japan /ledger/37: Qingdao returned 1922-12; no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1938 occupation_start (counterpart republic-of-china). empire-of-japan /ledger/49 Shandong, Shanxi 1938-03 (end /ledger/92); no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1938 occupation_start (counterpart republic-of-china). empire-of-japan /ledger/50 Henan plain 1938-06 (end /ledger/93); no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1938 occupation_start (counterpart republic-of-china). empire-of-japan /ledger/52 Guangdong coast 1938-10 (end /ledger/96); no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1939 occupation_start (counterpart republic-of-china). empire-of-japan /ledger/53 Hainan (end /ledger/97); no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1944 occupation_start (counterpart republic-of-china). empire-of-japan /ledger/73 Guangxi 1944-09 (end /ledger/99); no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1935 vassal_start (counterpart republic-of-china). empire-of-japan /ledger/44 East Hebei 1935-11 (end 1938-02): the Republic has no loss of eastern Hebei; no mirror in republic-of-china (fix listed there)
- missing: empire-of-japan 1945 vassal_end (counterpart republic-of-china). empire-of-japan /ledger/85, /87: Rehe and Mengjiang end 1945-08; the Republic has no gain; no mirror in republic-of-china (fix listed there)
- missing: tibet 1912 occupation_start (counterpart republic-of-china). tibet /ledger/33 (1912-08) and /36 (1918): Republican occupation of western Kham; no mirror in republic-of-china (fix listed there)
- missing: tibet 1930 contest_start (counterpart republic-of-china). tibet /ledger/37-38: Sino-Tibetan War 1930-05 to 1933; no mirror in republic-of-china (fix listed there)
- missing: kumul-khanate 1912 vassal_start (counterpart republic-of-china). kumul-khanate /ledger/3-5: vassal 1912 to 1930-06, then abolished into the Republic; no mirror in republic-of-china (fix listed there)
- missing: first-east-turkestan-republic 1933 found (counterpart republic-of-china). first-east-turkestan-republic /ledger/0-1: founded 1933-11 on the Republic's land, dissolved into it 1934-02; no mirror in republic-of-china (fix listed there)
- missing: east-turkestan-republic 1945 contest_start (counterpart republic-of-china). east-turkestan-republic /ledger/2-3: Manasi front 1945-09 to 1946-01; no mirror in republic-of-china (fix listed there)
- missing: democratic-republic-of-vietnam 1945 occupation_start (counterpart republic-of-china). democratic-republic-of-vietnam /ledger/0, /2: Nationalist occupation of the north 1945-08 to 1946-06; no mirror in republic-of-china (fix listed there)
- missing: french-indochina 1945 loss (counterpart republic-of-china). french-indochina /ledger/31: Guangzhouwan to the Republic; no mirror in republic-of-china (fix listed there)
- missing: mongolian-people-s-republic 1947 occupation_start (counterpart republic-of-china). mongolian-people-s-republic /ledger/5-6: Baitag Bogd 1947-06 to 1947-07; no mirror in republic-of-china (fix listed there)

Matched: the Empire/Republic pair, the Northern Expedition losses and gains (republic-of-china and kuomintang), great-mongol-state 1919 and 1921, east-turkestan-republic 1944, the five Japanese occupation pairs the Republic carries, Taiwan 1945, chinese-communists with kuomintang (1928) and republic-of-china (1930). Exceptions: qing-dynasty, communist-party-of-china, people-s-republic-of-china, anti-kuomintang-coalition, union-of-soviet-socialist-republics, manchukuo, mengjiang and the warlord cliques (not written yet).

## Other notes

- Per the orchestrator, the reviewer applied small verified fixes in place (all re-validated with 0 errors): republic-of-china /ledger/60 counterpart; panthay-rebellion rename event removed and war end 1872; kuomintang /wars/3 end 1929; chinese-communists /wars/0 end 1931; empire-of-china /wars/0 start 1916.
- Neighbour dossiers not yet written (exceptions in the matrix): qing-dynasty (ea-08-b), communist-party-of-china and people-s-republic-of-china (ea-08), anti-kuomintang-coalition (ea-08), union-of-soviet-socialist-republics (eu-17), manchukuo and mengjiang (ea-08-x), british-raj and the other context states with no Chinese border event.
- east-hebei-autonomous-council is used by empire-of-japan and named in the republic-of-china notes but was missing from the author's counterparts_needing_dossiers; added here.
- No page failed to load for the reviewer. The author's failed page (Cen_Yuying) was not retried.
- Taiping Heavenly Kingdom: every confidence-3 event checked against Taiping_Rebellion and Taiping_Heavenly_Kingdom held; the dossier is thin only where the author said it was (1861 west, 1863-64 reconquest).
- Ledger order, found/dissolve years, capitals, rulers and certainty spans were checked by script for all six; the only defects were the four wars running outside the life (all clipped).
