# Review of batch ia-03-x (reviewer, 2026-10-19)

Adversarial review of the 21 new dossiers of the Central Asian additions batch. Validator: 21 valid, 0 errors, one warning pair (khanate-of-kalat, expected). 27 Wikipedia pages opened; every confidence-3 event that moves land was checked where the budget allowed. The machine copy is history/notes/phase-b/reviews/ia-03-x.json.

Verdict meanings in this run: pass = nothing to change; fix = accepted, the reviewer applied the small fixes in place (marked applied); thin = valid, but the ledger leaves border moves unexplained or a non-blocking fix remains for the author or a gap-filler; fail = an unapplied blocking finding, back to the author.

| slug | verdict | what decides it |
| --- | --- | --- |
| russian-turkestan | fix | war clipped to 1867; Khiva protectorate month removed; contest pair for Kokand 1918 and colony-vs-empire pairing left to author/orchestrator |
| turkestan-assr | thin | Basmachi war zones added; keyframes keep Fergana that the ledger gives the Basmachi 1918-1924 |
| bukharan-people-s-soviet-republic | fix | Basmachi war zones added; East Bukhara 1921/11 c1 can be 1922 from its own page |
| khorezm-people-s-soviet-republic | thin | Junaid Khan's April 1922 capture (infobox) not in the ledger |
| turkestan-autonomy | pass | all dates confirmed; seat-only shape by design |
| alash-autonomy | fail | BLOCKING: whole-Kazakhstan shape overlaps Russian Turkestan / Turkestan ASSR (about 584,000 km2) and contradicts its own text |
| transcaspian-provisional-government | pass | all dates confirmed |
| tuvan-people-s-republic | fix | found counterpart re-pointed to republics-of-the-soviet-union |
| basmachi-movement | thin | overlapping keyframes fixed (1918 keyframe now ends 1920); Fergana after 1924, land after 1925 and the Kokand capital left to the author |
| principality-of-herat | thin | the 1851 Farah gain misreads the page (Lash-Joveyn seceded in 1851; Farah was Kandahar's 1851-1853) |
| principality-of-kandahar | fix | gap keyframe 1839-1841 deleted; war and last ruler clipped to 1855; Farah 1851-1853 missing |
| maimana-khanate | thin | first ruler clipped to 1747; keyframe runs through the 1876-79 annexation; May-Nov 1879 annexation and 1888 reductions missing |
| kumul-khanate | fail | BLOCKING: no Qing (1696-1912) or Republic of China (1912-1930) vassal events although the infobox gives both |
| bukey-horde | pass | all confirmed; capital coordinates are the flagged Zhanibek stand-in |
| yettishar | thin | page-dated Ottoman vassalage of 1873 missing; Turfan and Urumqi not events |
| ili-sultanate | fix | war clipped to 1871; 1864 found already takes the land of the 1866 gains |
| khalkha-khanates | fix | keyframe extended to the 1688 end |
| dughlat-emirate | thin | Khotan enters the 1480 keyframe with no event |
| tashkent-state | pass | all confirmed |
| emirate-of-afghanistan-1929 | fix | war clipped to 1929; all six events confirmed |
| first-east-turkestan-republic | pass | both events confirmed; end choice (6 Feb vs 16 Apr 1934) documented |

## Findings per dossier

### russian-turkestan: fix

- `/wars/0/from` (applied by the reviewer). The Russian conquest of Central Asia war started in 1865, before the colony's start (23 July 1867). Evidence: Brief section 2: wars inside the life; the 1865-66 campaigns belong to russian-empire. Fix: from set to 1867.
- `/ledger/5/month` (applied by the reviewer). The Khiva vassal_start carried month 6 at confidence 3, but the page it cites gives only the year. Evidence: Russian_conquest_of_Central_Asia: 'The Khanate of Khiva became a Russian protectorate and remained so until the Russian Revolution' (1873); the only June date is the khan's peace overture 'on 4 June'. The khanate-of-khiva dossier dates the protectorate to the treaty of 24 August 1873. Fix: Month removed (year 1873 kept). The author may set month 8 if the treaty page is opened.
- `/ledger (1918/2)` (for the author (non-blocking)). No contest pair for the Turkestan (Kokand) Autonomy, whose ledger contests Kokand against russian-turkestan in February 1918. Evidence: turkestan-autonomy /ledger/1-2: contest_start and contest_end 1918/2, counterpart russian-turkestan; Kokand_Autonomy: shelling of the palace 13 February 1918, surrender 22 February 1918. Fix: Add contest_start and contest_end 1918/2, counterpart turkestan-autonomy, region Kokand within 50 km, confidence 3, source Kokand_Autonomy (add it to sources).
- `/ledger/2, /ledger/4, /ledger/6 (counterpart pairing)` (for the author (non-blocking)). The gains from Bukhara (1868), Khiva (1873) and Kokand (1876) pair with losses that the neighbours give to russian-empire, not to russian-turkestan. Evidence: emirate-of-bukhara /ledger/7 (1868/5 loss, counterpart russian-empire); khanate-of-khiva /ledger/20 (1873/8, russian-empire); khanate-of-kokand /ledger/25-26 (1876, russian-empire). Fix: Orchestrator decision: either the neighbours re-point those losses to russian-turkestan, or this dossier's gains are recorded with russian-empire as the holder. Land and years agree.
- thin `/ledger/0`: 1867 Khujand, Jizzakh and Ura-Tepe bridged at confidence 1 (the page dates the captures only to 1866 and says Jizzakh was taken 'from Bukhara'; Khujand's holder is not named) (try https://en.wikipedia.org/wiki/Khujand)
- thin `/ledger/11, /ledger/12`: 1918/4 vassal_end of Bukhara and Khiva at confidence 1; neither neighbour dossier has a vassal pair at all (try https://en.wikipedia.org/wiki/Emirate_of_Bukhara)
- spot checks: /ledger/2 confirmed, /ledger/3 confirmed, /ledger/4 confirmed, /ledger/5 mis-dated, /ledger/6 confirmed, /ledger/7, /ledger/10 confirmed, /ledger/9 confirmed
- area: infobox 1707003 (1897), Cliopatria None, ratio 1.38; No Cliopatria row; compared with the author's gazetteer estimate of about 1,236,000 km2 for the 1899-1918 keyframe (infobox/estimate 1.38), acknowledged in /keyframe_review/6/note.

### turkestan-assr: thin

- `/wars/1/zones` (applied by the reviewer). The Basmachi revolt war had empty zones although the ledger moves Fergana and the Tashkent countryside. Evidence: Basmachi_movement: by the end of 1918 bands 'controlled Ferghana and the countryside surrounding Tashkent'; /ledger/2. Fix: zones set to the /ledger/2 region (Fergana and Tashkent within 80 km).
- `/keyframe_review/1/correction, /keyframe_review/2/correction` (for the author (non-blocking)). The 1919 and 1920-1924 keyframes keep the Fergana region that /ledger/2 loses to the Basmachi in 1918/12 and /ledger/6 regains only in 1924. Evidence: /ledger/2 note: 'A rebel overlay on the nominal extent'. Check 4: a keyframe must agree with the ledger; basmachi-movement draws Fergana as its own keyframe for the same years. Fix: Either take Fergana out of the 1919 and 1920 keyframes (and split the 1920 keyframe at 1924 to put it back), or say in both keyframe notes that the ledger carves Fergana out for 1918/12-1924. Same for the Tashkent radius to 1920.
- thin `/ledger/3`: 1920 recovery of the Tashkent countryside at confidence 1, no page dates it (try https://en.wikipedia.org/wiki/Basmachi_movement)
- thin `/keyframe_review/0-2`: White and Cossack control of northern Semirechye (1918-1920) and the Fergana front are on no page opened; the extent is Russian Turkestan's (try https://en.wikipedia.org/wiki/Semirechye_Oblast)
- spot checks: /ledger/0 confirmed, /ledger/2 confirmed, /ledger/4 confirmed, /ledger/5 confirmed, /ledger/7 confirmed
- area: infobox None (None), Cliopatria None, ratio None; The page gives no area; keyframe notes compare with the Russian Turkestan infobox (1,707,003 km2, 1897).

### bukharan-people-s-soviet-republic: fix

- `/wars/0/zones` (applied by the reviewer). The Basmachi revolt war had empty zones although /ledger/1 loses East Bukhara to the Basmachi. Evidence: Bukharan_People's_Soviet_Republic: 'In 1922, most of the territory of the republic (East Bukhara, roughly from Hisor to West Pamir) was controlled by Basmachi.' Fix: zones set to the /ledger/1 region (Khatlon and Dushanbe).
- `/keyframe_review/0` (for the author (non-blocking)). The single 1920-1924 keyframe keeps East Bukhara that /ledger/1 loses in 1921/11 and that the republic never regains before 1924. Evidence: /ledger/1; basmachi-movement /keyframe_review/1 draws Khatlon and Dushanbe 1921-1925. Fix: Say in the keyframe note that the ledger carves East Bukhara out from 1921/22, or split the keyframe.
- thin `/ledger/1`: 1921/11 loss of East Bukhara at confidence 1; the republic's own page dates Basmachi control of East Bukhara to 1922 (confidence 2 or 3 available; basmachi-movement /ledger/3 and /keyframe_review/1 would move with it) (try https://en.wikipedia.org/wiki/Bukharan_People%27s_Soviet_Republic)
- spot checks: /ledger/0 confirmed, /ledger/1 mis-dated, /ledger/2 confirmed, /ledger/3 confirmed
- area: infobox 182193 (1920), Cliopatria 218997, ratio 0.83; Cliopatria emirate-of-bukhara_1919 is 218,997 km2 in shapes.csv (the author quotes about 186,000 km2 from the gazetteer); within a factor of two and acknowledged.

### khorezm-people-s-soviet-republic: thin

- thin `/wars/0/zones, /ledger`: The war with Junaid Khan has empty zones and no event, yet the infobox gives 'Brief capture of Khorezm by Junaid Khan: April 1922' (a loss and a regain in 1922) (try https://en.wikipedia.org/wiki/Khorezm_People%27s_Soviet_Republic)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed
- area: infobox 62200 (1920), Cliopatria 384764, ratio 0.16; The Cliopatria khanate-of-khiva_1919 shape (384,764 km2) is replaced by the Khorezm and Tashauz admin-1s (about 69,000 km2, ratio 0.90); acknowledged in /keyframe_review/0/note.

### turkestan-autonomy: pass

- spot checks: /ledger/0 confirmed, /ledger/1-2 confirmed, /ledger/3 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; only the seat is drawn, by design for a 1-2 page state. Tried: dates, capital, claim; could not break it. The matching contest pair is missing in russian-turkestan (listed there).

### alash-autonomy: fail

- `/keyframe_review/0/correction, /ledger/0/region, /ledger/1/region` (BLOCKING, for the author). BLOCKING: the region is the whole of Kazakhstan, which contradicts its own text ('the Turkestan Autonomy to the south') and draws the Syr-Darya and Semirechye oblasts twice: Qyzylorda, South Kazakhstan, Zhambyl and Almaty are 2,308 cells (about 584,000 km2) that russian-turkestan (to 1918/4) and turkestan-assr (1918-1924) hold in the same years. Evidence: Alash_Autonomy: 'The political entity bordered Russian territories to the north and west, the Turkestan Autonomy to the south, and China to the east.' russian-turkestan /keyframe_review/6 and turkestan-assr /keyframe_review/0-2 include those four admin-1s. Fix: Write the shape as {"minus": [{"country": "Kazakhstan"}, {"union": [{"admin1": "Qyzylorda", "country": "Kazakhstan"}, {"admin1": "South Kazakhstan", "country": "Kazakhstan"}, {"admin1": "Zhambyl", "country": "Kazakhstan"}, {"admin1": "Almaty", "country": "Kazakhstan"}]}]} with the same text, in the keyframe and in both ledger regions; or, if a page shows Alash holding Kazakh districts of Syr-Darya or Semirechye, record them as a contest with turkestan-assr.
- thin `/keyframe_review/0`: No oblast list and no Western Alash Orda (Zhympity, Uralsk) on the pages; the 1919 Soviet takeover is not an event (try https://en.wikipedia.org/wiki/Alash_Orda)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; the claim shape is Kazakhstan (about 2.3 M km2 in the gazetteer) and is noted as the claim.

### transcaspian-provisional-government: pass

- thin `/ledger`: The fall of Merv, Ashgabat and Krasnovodsk to the Red Army is not dated on the page (the lead ends the government in July 1919, the infobox in February 1920), so the whole oblast stays to February 1920 (try https://en.wikipedia.org/wiki/Malleson_mission)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; the oblast floor (Ahal, Balkan, Mary, about 269,000 km2) is noted.

### tuvan-people-s-republic: fix

- `/ledger/0/counterpart` (applied by the reviewer). The 1921 founding took the land from russian-empire, which ended in 1917; the page says the Bolsheviks held all of Tuva before the declaration. Evidence: Tuvan_People's_Republic: the Bolsheviks 'had, by March 1921, seized all of Tuva'; Cliopatria's Republics of the Soviet Union row covers 1920-1921. Fix: counterpart set to republics-of-the-soviet-union, with a sentence added to the note.
- `/ledger/2/region` (for the author (non-blocking)). The 1932 gain from Mongolia names the whole Tuva region, so the gain cannot be drawn as the strip it was. Evidence: Tuvan_People's_Republic: 'In July 1932, Tuva gained a substantial territory from Mongolia, including Dus-Dag mountain'. Fix: Name the strip when a gazetteer entry exists for Dus-Dag (listed under gazetteer_names_needed); until then lower the region to a radius round Dus-Dag or keep it and say in the note that it is a placeholder.
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed, /ledger/3 confirmed
- area: infobox 170500 (1944), Cliopatria None, ratio 1.07; No Cliopatria row after 1913; the Tuva region is about 159,600 km2 (infobox/region 1.07), noted in /keyframe_review/0/note.

### basmachi-movement: thin

- `/keyframe_review/0/to` (applied by the reviewer). The 1918 keyframe ran to 1924 and overlapped the 1921 keyframe (1921-1925), drawing two shapes for 1921-1924. Evidence: /ledger/2 drops the Tashkent countryside in 1920 and /keyframe_review/1 starts in 1921. Fix: to set to 1920.
- `/keyframe_review/1` (for the author (non-blocking)). The 1921-1925 keyframe keeps Fergana after /ledger/4 loses it in 1924. Evidence: Basmachi_movement: 'A Basmachi presence remained in the Ferghana Valley until 1924'. Fix: Split it: 1921-1923 as now, and a new keyframe basmachi-movement_1924 (1924-1925) of Khatlon and Dushanbe only.
- `/ledger/6/region, /identity/end` (for the author (non-blocking)). The movement holds no land after the 1925 loss of East Bukhara, yet the 1934 dissolve names Khatlon and Dushanbe and the life runs to 1934 with no keyframe after 1925. Evidence: /ledger/5 (1925 loss); Basmachi_movement: 'The Basmachi movement had ended by 1934'; Ibrahim Bek raided from Afghanistan from 1926. Fix: Either keep 1934 and give the dissolve region a note that nothing is drawn after 1925, or end the territorial life in 1925.
- `/identity/capitals/0` (for the author (non-blocking)). Kokand 1918-1924 is not a Basmachi capital on any page (its own note says 'unverified'); the Red Army took Kokand in February 1918. Evidence: Turkestan_Autonomous_Soviet_Socialist_Republic and Kokand_Autonomy: Kokand surrendered to the Soviet on 22 February 1918. Fix: Drop the capital or keep it with to 1918.
- thin `/ledger/2`: 1920 loss of the Tashkent countryside at confidence 1 (try https://en.wikipedia.org/wiki/Madamin_Bek)
- thin `/ledger/3`: 1921/11 spread to East Bukhara at confidence 1; the Bukharan republic's page dates it to 1922 (try https://en.wikipedia.org/wiki/Bukharan_People%27s_Soviet_Republic)
- thin `/ledger`: Junaid Khan's Khiva front (April 1922 capture of Khorezm) is not drawn (try https://en.wikipedia.org/wiki/Khorezm_People%27s_Soviet_Republic)
- spot checks: /ledger/1 confirmed, /ledger/3 confirmed, /ledger/4 confirmed, /ledger/6 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; floors noted in the keyframe notes.

### principality-of-herat: thin

- `/ledger/3` (for the author (non-blocking)). The 1851 gain of the Farah admin-1 is not what the page says: Lash-Joveyn was reconquered early in 1851 and seceded the same year on Yar Mohammad's death, and Farah was under Kandahar from 1851. Evidence: Principality_of_Herat: 'Yar Mohammad Khan was able to reconquer Lash-Joveyn along with the lands of the Sanjarani tribe'; his death in 1851 was 'allowing Lash-Joveyn to secede'; in 1853 Sa'id Mohammad Khan seized 'Farah, which had been under Qandahar since 1851'. Fix: Keep the 1851 gain at confidence 2 but add a 1851 loss of Lash-Joveyn (counterpart nobody); add a 1853 gain of Farah from principality-of-kandahar (confidence 3, HR) and the later loss (1856/10, DM 'controlled by the Barakzai Emirs since 30 October 1856', or 1862/3, HR 'captured Farah ... on 11 March 1862'), with the 1851-1853 years out of the shape; principality-of-kandahar needs the mirror events.
- `/keyframe_review/0/correction, /ledger/0/region` (for the author (non-blocking)). The 1818 keyframe holds Hirat, Badghis, Farah and Ghor while the found event names only Hirat; the page names Badghis only as a battle (1826) and Ghor only as a campaign against the Taymanis. Evidence: Principality_of_Herat (spot check 6). Fix: Either make the found region match the keyframe, or add the dated campaigns (Ghor, the Aimaq lands, the Chahar Wilayat) as gains and keep Farah out until 1853.
- thin `/keyframe_review/0`: Farah's owner 1818-1851 and the extent of the Chahar Wilayat and Aimaq expansion are not on the page; 'tributary to Qajar Iran for much of the period' is undated (try https://en.wikipedia.org/wiki/Anglo-Persian_War)
- spot checks: /ledger/1-2 confirmed, /ledger/3 not on page, /ledger/4 confirmed, /ledger/5-6 confirmed, /ledger/7 confirmed, /ledger/8 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; floor of four admin-1s (about 147,000 km2) noted.

### principality-of-kandahar: fix

- `/keyframe_review/1 (deleted)` (applied by the reviewer). The 1839-1841 'gap' keyframe had a correction (the Kandahar admin-1) and so drew the principality during the Shah Shuja years that /ledger/5-6 take away; its own note said 'the principality is not drawn'. Evidence: Principality_of_Kandahar: 'Fall of Kandahar: 8 May 1839'; 'Liberation of Kandahar: 9 August 1842'. durrani-dynasty /ledger/1-3 holds the land 1839-1842. Fix: Keyframe principality-of-kandahar_1839 deleted; the 1818-1838 and 1842-1855 keyframes stand (the old /keyframe_review/2 is now /keyframe_review/1).
- `/wars/0/to` (applied by the reviewer). The war ran to 1856, past the end (1855/11). Evidence: Dost_Mohammad_Khan: 'In November 1855, he conquered Kandahar.' Fix: to set to 1855.
- `/identity/rulers/4/to` (applied by the reviewer). Rahim Dil Khan's reign ran to 1856, past the end (1855/11). Evidence: The dossier follows DM's November 1855 for the end; KD's September 1856 is recorded in the ruler's note. Fix: to set to 1855.
- `/ledger (1851-1853)` (for the author (non-blocking)). No event for Farah, which the Herat page puts under Kandahar from 1851 to 1853. Evidence: Principality_of_Herat: 'Farah, which had been under Qandahar since 1851', seized by Herat in 1853. Fix: Add a 1851 gain of Farah (counterpart principality-of-herat or nobody, confidence 2) and a 1853 loss to principality-of-herat (confidence 3), source Principality_of_Herat.
- thin `/ledger/1-2`: Tribute of Sindh and Balochistan from 1818 at confidence 1 (page: 'paid tribute and were dependent', undated) (try https://en.wikipedia.org/wiki/Principality_of_Kandahar)
- spot checks: /ledger/0 confirmed, /ledger/3-4 confirmed, /ledger/5 confirmed, /ledger/6 confirmed, /ledger/7 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; floor of about 135,000 km2 noted.

### maimana-khanate: thin

- `/identity/rulers/0/from` (applied by the reviewer). The first ruler started in 1731, before the khanate's founding in 1747. Evidence: Maimana_Khanate: 'founded in 1747 with the death of Nader Shah'. Fix: from set to 1747, with the list's 1731 kept in the ruler's note.
- `/keyframe_review/2` (for the author (non-blocking)). The 1845-1892 keyframe draws Maimana through the Afghan annexations that /ledger/3-4 record (March 1876 to February 1879), and a second annexation of May to November 1879 is missing. Evidence: Maimana_Khanate: 'From March 1876 to February 1879 the Maimana Khanate was annexed into Afghanistan'; 'annexed again from May to November 1879'. Fix: Split the keyframe at 1876 and 1879 (no shape 1876-1878), add a loss 1879/5 and a gain 1879/11 (counterpart emirate-of-afghanistan, confidence 3).
- `/ledger/2` (for the author (non-blocking)). The 1845 loss names the Badghis admin-1, which no keyframe or gain ever gives the khanate. Evidence: Maimana_Khanate: 'The Aimaq tribes of the Murghab broke away from Maimana by 1845'; /keyframe_review/0 is Faryab and Sari Pul only. Fix: Either add the Murghab Aimaq lands to the 1747 keyframe or drop the region to a note; keep confidence 2.
- thin `/keyframe_review/2`: By 1888 Daulatabad went to Aqcha and Darzab and Gurziwan were lost ('territory had been greatly reduced'); no events (try https://en.wikipedia.org/wiki/Maimana_Khanate)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/3 confirmed, /ledger/5 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; floor noted.

### kumul-khanate: fail

- `/ledger` (BLOCKING, for the author). BLOCKING: no vassal events, so the khanate would be drawn as an independent state for 234 years, while the page gives it as a Qing banner (1696-1912) and a vassal of the Republic of China (1912-1930). Evidence: Kumul_Khanate infobox: 'Banner of the Qing dynasty (1696–1912)', 'Vassal of the Republic of China (1912–1930)'; 'The title "Jasak Tarkhan" was granted to Abdullah Beg' in 1696. dzungar-khanate /ledger/10 gives Hami to qing-dynasty in 1696; the author's notes ask ea-08 for a 'Kumul vassal pair' that this dossier itself lacks. Fix: Add vassal_start 1696 and vassal_end 1912 (counterpart qing-dynasty, confidence 3) and vassal_start 1912 and vassal_end 1930/6 (counterpart republic-of-china, confidence 3), source Kumul_Khanate.
- `/identity/rulers (last entry)` (for the author (non-blocking)). Nasir 1930-1934 is listed after the abolition of June 1930. Evidence: Kumul_Khanate: abolished by Jin Shuren after 'Maqsud Shah's death on 6 June 1930'; the table's later names are claimants. Fix: Drop Nasir or end him in 1930 and say claimant in the note.
- `/wars/0` (for the author (non-blocking)). The Kumul Rebellion is dated 1930-1930 with empty zones; the page gives no start date and says only that the abolition 'set off' it. Evidence: Kumul_Khanate (spot check 4). Fix: Keep it with a note that the rebellion falls after the khanate's end, or drop it.
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page ('located in present-day Hami prefecture'); 120 km radius floor noted.

### bukey-horde: pass

- thin `/identity/capitals/0`: Capital coordinates are Zhanibek's (the author's stand-in, flagged in the note), not Khan Ordasy's (today's Urda, West Kazakhstan); the gazetteer lacks Urda (try https://en.wikipedia.org/wiki/Urda,_Kazakhstan)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed
- area: infobox 71000 (None), Cliopatria None, ratio 1.0; Page: 'about 71,000 square kilometers'; the 150 km radius is 70,700 km2. Tried: dates, area, status, capital; nothing broken beyond the flagged capital stand-in.

### yettishar: thin

- `/ledger (1873)` (for the author (non-blocking)). The page-dated Ottoman suzerainty is missing from this dossier although the author's notes cite it for ottoman-empire. Evidence: Yettishar: 'In 1873, the Ottoman Empire recognised Yettishar as a vassal state and Yakub Beg as its emir.' Fix: Add vassal_start 1873 and vassal_end 1877/12 (counterpart ottoman-empire, confidence 3, empty region), or say in notes why a nominal suzerainty is left out.
- thin `/ledger/1`: 1866 conquest of the Tarim Basin cities at confidence 1 (the page dates no city) (try https://en.wikipedia.org/wiki/Yakub_Beg)
- thin `/keyframe_review/1`: The keyframe note mentions Turfan, but no event takes Turfan or Urumqi or loses them before Kashgar falls (the page says only that 'Qing forces entered Ürümqi unopposed') (try https://en.wikipedia.org/wiki/Qing_reconquest_of_Xinjiang)
- spot checks: /ledger/0 confirmed, /ledger/2 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; the Tarim Basin region (about 942,000 km2) is noted as an over-reach.

### ili-sultanate: fix

- `/wars/0/to` (applied by the reviewer). The Russian occupation war ran to 1883, past the sultanate's end in 1871. Evidence: Treaty_of_Saint_Petersburg_(1881): 'In 1871, Russia occupied the Ili territory'; 'March 1883, Russia evacuated the province' (russian-empire's years). Fix: to set to 1871.
- `/ledger/0/region` (for the author (non-blocking)). The 1864 founding already takes the whole valley (150 km round Yining) that /ledger/1-2 gain in January and March 1866. Evidence: Dungan_Revolt_(1862–1877): the rising of 10 November 1864 at Ningyuan and Huiyuan; Huiyuan fell 8 January 1866; the citadel on 3 March (1866), 'the temporary end ... of Qing rule in the Ili Valley'. Fix: Give the 1864 found a smaller region (Ningyuan, the Taranchi Kulja: about 30 km round Yining) so the 1866 gains add land.
- thin `/identity`: No sultan, capital or end of the Ili state on any page opened (Ili Sultanate redirects to the Dungan Revolt) (try https://en.wikipedia.org/wiki/Taranchi)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed, /ledger/3 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on either page.

### khalkha-khanates: fix

- `/keyframe_review/0/to` (applied by the reviewer). The only keyframe ended in 1687 although the state lives to the dissolve of 1688. Evidence: Northern_Yuan_dynasty: 'Galdan led 30,000 Dzungar troops into Outer Mongolia in 1688'; dzungar-khanate /ledger/8 gains Khalkha in August 1688. Fix: to set to 1688.
- thin `/wars/0, /wars/1`: The two war spans are the author's: the page has a 1647 battle ('Gombodorj met the Qing in battle with 50,000 cavalry') and 1655 Qing interference, and only 'Siberian Cossacks ... defeated a Khalkha army of 10,000 near Lake Baikal' undated (try https://en.wikipedia.org/wiki/Khalkha)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; replaces 15 Golden Horde rows that golden-horde marks wrong (checked: 15 keyframes there name khalkha).

### dughlat-emirate: thin

- `/keyframe_review/1/correction` (for the author (non-blocking)). Khotan enters the shape in 1480 with no event. Evidence: Mirza_Abu_Bakr_Dughlat: his kingdom 'included Khotan and Kashgar', no date for Khotan. Fix: Add a gain of Khotan (Hotan within 100 km) at 1480, confidence 1, counterpart moghulistan.
- thin `/ledger/3`: 1500 recovery of Kashgar at confidence 1 ('later', undated; Ahmad Alaq 'could not hold it') (try https://en.wikipedia.org/wiki/Ahmad_Alaq)
- thin `/keyframe_review/1-3`: Undated conquests (Ladakh, Balur, Badakhshan, districts of Tibet) left out (try https://en.wikipedia.org/wiki/Mirza_Abu_Bakr_Dughlat)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed, /ledger/4 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page.

### tashkent-state: pass

- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the pages. Tried: dates, borders, end conflict; could not break it. Neighbour kazakh-khanate keeps Shymkent and Turkestan to 1809 (see cross-checks).

### emirate-of-afghanistan-1929: fix

- `/wars/0/from` (applied by the reviewer). The civil war started in 1928, before the emirate's founding in January 1929. Evidence: Afghan_Civil_War_(1928–1929): first Saqqawist assault on Kabul 14 December 1928; Kabul taken 17 January 1929. Fix: from set to 1929.
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed, /ledger/2 confirmed, /ledger/3 confirmed, /ledger/4 confirmed, /ledger/5 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the pages; the page 'never gives a full list' of land, as the keyframe note says.

### first-east-turkestan-republic: pass

- thin `/ledger/1`: The dissolve is the flight from Kashgar of 6 February 1934; the infobox ends the state on 16 April 1934 and the army retreated toward Yarkand and Hotan, so the Hotan and Aksu radii may belong to the state to April (try https://en.wikipedia.org/wiki/First_East_Turkestan_Republic)
- spot checks: /ledger/0 confirmed, /ledger/1 confirmed
- area: infobox None (None), Cliopatria None, ratio None; No area on the page; infobox caption: controlled the Kashgar, Kizilsu, Khotan and Aksu prefectures, matching the three radii.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| russian-turkestan 1867 gain (emirate-of-bukhara) | emirate-of-bukhara 1866 loss | mismatch | Bukhara loses Jizzakh and Ura-Tepe to russian-empire in 1866; RT bridges them in at 1867 (confidence 1). Khujand's holder is on no page. Counterpart naming: route to the orchestrator (colony vs empire). |
| russian-turkestan 1868 gain (emirate-of-bukhara) | emirate-of-bukhara 1868 loss | mismatch | Land and year agree (Samarkand, 1868/5 vs 1868/7); Bukhara names russian-empire as the gainer. |
| russian-turkestan 1868 vassal_start (emirate-of-bukhara) | - | missing | emirate-of-bukhara has no vassal_start at all (its /ledger/7 note says 'remained a semi-independent vassal'); route to Bukhara's owner (ia-03). |
| russian-turkestan 1873 gain (khanate-of-khiva) | khanate-of-khiva 1873 loss | mismatch | Amu Darya Division: Khiva /ledger/20 (1873/8) names russian-empire. |
| russian-turkestan 1873 vassal_start (khanate-of-khiva) | - | missing | khanate-of-khiva has no vassal_start ( /ledger/20 note: 'becomes a Russian protectorate'); route to Khiva's owner (ia-03). |
| russian-turkestan 1876 gain (khanate-of-kokand) | khanate-of-kokand 1876 loss | mismatch | Fergana: Kokand /ledger/25-26 name russian-empire. |
| russian-turkestan 1882 loss (Governor-Generalship of the Steppes) | - | exception | Internal Russian unit, no dossier and not listed by the author; could be recorded against russian-empire (eu-17, not run). |
| russian-turkestan 1897 gain (russian-empire) | - | exception | russian-empire (eu-17) not written yet. |
| russian-turkestan 1899 gain (Governor-Generalship of the Steppes) | - | exception | As 1882. |
| russian-turkestan 1918 vassal_end (emirate-of-bukhara) | - | missing | No vassal pair in emirate-of-bukhara. |
| russian-turkestan 1918 vassal_end (khanate-of-khiva) | - | missing | No vassal pair in khanate-of-khiva. |
| turkestan-autonomy 1918 contest_start (russian-turkestan) | - | missing | russian-turkestan has no contest pair for Kokand 1918/2 (fix listed there). |
| turkestan-assr 1918 loss (transcaspian-provisional-government) | transcaspian-provisional-government 1918 found | matched | 1918/7 both sides. |
| turkestan-assr 1918 loss (basmachi-movement) | basmachi-movement 1918 gain | matched | 1918/12 both sides, Fergana and the Tashkent radius. |
| turkestan-assr 1920 gain (basmachi-movement) | basmachi-movement 1920 loss | matched | Both confidence 1. |
| turkestan-assr 1920 gain (transcaspian-provisional-government) | transcaspian-provisional-government 1920 dissolve | matched | 1920/2 both sides. |
| turkestan-assr 1924 gain (basmachi-movement) | basmachi-movement 1924 loss | matched | Fergana, 1924. |
| bukharan-people-s-soviet-republic 1921 loss (basmachi-movement) | basmachi-movement 1921 gain | matched | Both 1921/11 at confidence 1; the BP page supports 1922 for both. |
| bukharan-people-s-soviet-republic 1920 found (emirate-of-bukhara) | emirate-of-bukhara 1920 dissolve | matched | 1920/9 dissolve vs 1920/10 found. |
| khorezm-people-s-soviet-republic 1920 found (khanate-of-khiva) | khanate-of-khiva 1920 dissolve | matched | 1920/2 both. |
| basmachi-movement 1925 loss (union-of-soviet-socialist-republics) | - | exception | No union dossier yet (eu-17 not run). |
| alash-autonomy 1917 found (russian-republic) | - | mismatch | Overlap, not pairing: alash-autonomy's Kazakhstan shape covers the Qyzylorda, South Kazakhstan, Zhambyl and Almaty admin-1s held by russian-turkestan (to 1918/4) and turkestan-assr (1918-1924) in the same batch; about 584,000 km2 drawn twice 1917-1920. russian-republic itself: eu-17 not run. |
| tuvan-people-s-republic 1932 gain (mongolian-people-s-republic) | - | missing | mongolian-people-s-republic has no 1932 event (nor 1944 ratification); route to its owner. |
| tuvan-people-s-republic 1921 found (republics-of-the-soviet-union) | - | exception | Counterpart corrected by the reviewer from russian-empire; eu-17 not run. |
| principality-of-herat 1818 found (durrani-empire) | durrani-empire 1818 loss | matched |  |
| principality-of-herat 1851 gain (Lash-Joveyn local rulers) | - | exception | String counterpart; but the page has Lash-Joveyn seceding again in 1851 and Farah under Kandahar 1851-1853 (fix listed). |
| principality-of-herat 1856 occupation_start (qajar-dynasty) | - | exception | qajar-dynasty (me-10) not written yet; the 1837-38 and 1856 contests likewise. |
| principality-of-herat 1863 dissolve (emirate-of-afghanistan) | emirate-of-afghanistan 1863 gain | matched | 1863/5 both. |
| principality-of-kandahar 1818 found (durrani-empire) | durrani-empire 1818 loss | matched | 1818/8 both. |
| principality-of-kandahar 1818 vassal_start (talpur-dynasty) | - | exception | No talpur-dynasty dossier yet (South Asia group). |
| principality-of-kandahar 1818 vassal_start (khanate-of-kalat) | - | exception | Listed in the author's counterparts_needing_dossiers. |
| principality-of-kandahar 1839 loss (durrani-dynasty) | durrani-dynasty 1839 gain | matched | Months differ (1839/5 vs 1839/8); KD infobox gives 8 May 1839. |
| principality-of-kandahar 1842 gain (durrani-dynasty) | durrani-dynasty 1842 loss | matched | 1842/8 both. |
| principality-of-kandahar 1855 dissolve (emirate-of-afghanistan) | emirate-of-afghanistan 1855 gain | matched | 1855/11 both. |
| maimana-khanate 1814 loss (Sar-i Pul) | - | exception | Listed in counterparts_needing_dossiers (sar-i-pul-khanate). |
| maimana-khanate 1845 loss (nobody) | - | exception |  |
| maimana-khanate 1876 loss (emirate-of-afghanistan) | - | missing | emirate-of-afghanistan (ia-03-e) has no Maimana event 1874-1895. |
| maimana-khanate 1879 gain (emirate-of-afghanistan) | - | missing | As above; the second annexation of May-November 1879 is missing on both sides. |
| maimana-khanate 1892 dissolve (emirate-of-afghanistan) | - | missing | emirate-of-afghanistan has no 1892 gain of Maimana. |
| kumul-khanate 1696 found (dzungar-khanate) | dzungar-khanate 1696 loss | mismatch | dzungar-khanate /ledger/10 gives Hami to qing-dynasty; adding the Qing vassal_start to kumul-khanate reconciles them. |
| kumul-khanate 1930 dissolve (republic-of-china) | - | exception | republic-of-china (ea-08) not written yet. |
| yettishar 1866 gain (Tarim Basin rebel regimes) | - | exception | String counterpart, not listed under counterparts_needing_dossiers; qing-dynasty (ea-08) not written yet for the found and dissolve. |
| ili-sultanate 1866 gain (qing-dynasty) | - | exception | qing-dynasty (ea-08) not written yet (both 1866 gains). |
| ili-sultanate 1871 dissolve (russian-empire) | - | exception | russian-empire (eu-17) not written yet; it should carry occupation_start 1871 and occupation_end 1883/3. |
| khalkha-khanates 1636 found (mongol-khanate) | mongol-khanate 1635 dissolve | mismatch | mongol-khanate's 1635/2 dissolve names later-jin-dynasty only; it carries no Khalkha successor. |
| khalkha-khanates 1688 dissolve (dzungar-khanate) | dzungar-khanate 1688 gain | mismatch | dzungar-khanate /ledger/8 (1688/8) names the string 'Khalkha Mongols'; re-point to khalkha-khanates. |
| dughlat-emirate 1465 found (moghulistan) | - | missing | moghulistan has no Dughlat event; its 1470 gain from east-turkestan takes the whole Tarim, so Yarkand is drawn twice 1470-1514. |
| dughlat-emirate 1480 gain (moghulistan) | - | missing | No 1479-1481 Kashgar loss in moghulistan. |
| dughlat-emirate 1499 loss (eastern-chagatai-khanate) | - | missing | eastern-chagatai-khanate has no Kashgar event. |
| dughlat-emirate 1500 gain (eastern-chagatai-khanate) | - | missing | As above. |
| dughlat-emirate 1514 dissolve (eastern-moghulistan) | eastern-moghulistan 1514 found | mismatch | eastern-moghulistan's 1514/5 found names moghulistan; moghulistan /ledger/5 says the land was taken 'from Mirza Abu Bakr Dughlat'. |
| tashkent-state 1784 found (kazakh-khanate) | kazakh-khanate 1784 loss | mismatch | kazakh-khanate /ledger/37 names the string 'Tashkent state (Yunus Khoja)'; re-point to tashkent-state. |
| tashkent-state 1798 gain (kazakh-khanate) | - | missing | kazakh-khanate keeps the Shymkent-Turkestan lands to its 1809 loss to Kokand (/ledger/39). |
| tashkent-state 1809 dissolve (khanate-of-kokand) | khanate-of-kokand 1809 gain | matched | Kokand /ledger/7; its /ledger/8 also takes the Syr Darya lands to Turkestan from kazakh-khanate in 1809, which tashkent-state holds from 1798. |
| emirate-of-afghanistan-1929 1929 found (kingdom-of-afghanistan) | kingdom-of-afghanistan 1929 loss | mismatch | kingdom-of-afghanistan /ledger/1 names the string 'Emirate of Afghanistan (1929)'; same for /ledger/2-4; re-point to emirate-of-afghanistan-1929. |
| emirate-of-afghanistan-1929 1929 gain (kingdom-of-afghanistan) | - | missing | Ghazni (1929/5): no loss in kingdom-of-afghanistan (ia-03-f). |
| emirate-of-afghanistan-1929 1929 gain (kingdom-of-afghanistan) | kingdom-of-afghanistan 1929 loss | mismatch | Kandahar (1929/6): matched on land and month; string counterpart. |
| emirate-of-afghanistan-1929 1929 gain (kingdom-of-afghanistan) | - | missing | Balkh / Mazar-i Sharif (1929/6): no loss in kingdom-of-afghanistan. |
| emirate-of-afghanistan-1929 1929 loss (kingdom-of-afghanistan) | kingdom-of-afghanistan 1929 gain | mismatch | Kandahar (1929/9): matched; string counterpart. |
| emirate-of-afghanistan-1929 1929 dissolve (kingdom-of-afghanistan) | kingdom-of-afghanistan 1929 gain | mismatch | 1929/10: kingdom-of-afghanistan regains only Kabul; Ghazni and Balkh never return on its side. |
| first-east-turkestan-republic 1933 found (republic-of-china) | - | exception | republic-of-china (ea-08) not written yet. |
| bukey-horde 1801 found (russian-empire) | - | exception | russian-empire (eu-17) not written yet. |

## Gazetteer names needed

- Urda (Khan Ordasy, Khanskaya Stavka) (place, bukey-horde)
- Dus-Dag (place, tuvan-people-s-republic)
- Lash-Joveyn (Lash wa Juwayn) (place, principality-of-herat)
- Sibi (place, principality-of-kandahar)
- Pishin (place, principality-of-kandahar)
- Shorawak (place, principality-of-kandahar)

## Counterparts needing dossiers

- Khanate of Kalat: khanate-of-kalat [1818, 1826]
- Sar-i Pul chiefdom: sar-i-pul-khanate [1814, 1814]
- Khotan Emirate: khotan-emirate [1933, 1934]
- Outer Mongolia under the Qing: outer-mongolia-qing [1696, 1911]
- Governor-Generalship of the Steppes: steppe-governor-generalship [1882, 1899]

## Problems

- No page failed to load for the reviewer (27 WebFetch calls).
- Ten dossiers edited in place by the reviewer (russian-turkestan, turkestan-assr, bukharan-people-s-soviet-republic, tuvan-people-s-republic, basmachi-movement, principality-of-kandahar, maimana-khanate, ili-sultanate, khalkha-khanates, emirate-of-afghanistan-1929); all re-validated with 0 errors and read back unchanged after the write. principality-of-kandahar's /keyframe_review indices shift by one after the deletion of the 1839 gap keyframe.
- Context neighbours with a dossier (astrakhan-khanate, crimean-khanate, eastern-chagatai-khanate, empire-of-japan, golden-horde, kapisa, khanate-of-sibir, moghulistan, mongol-khanate, nogai-horde) were checked where a batch event names them; the others carry no counterpart of this batch. All other context neighbours (russian-empire, qing-dynasty, republic-of-china, qajar-dynasty, ottoman-empire, afsharid-iran, republics-of-the-soviet-union) have no dossier yet: counted as groups not yet run.
- Mirrors routed to other owners: emirate-of-bukhara and khanate-of-khiva (no Russian vassal pair), khanate-of-kokand and both of those (losses named russian-empire, not russian-turkestan), emirate-of-afghanistan (Maimana 1876, 1879, 1892), kingdom-of-afghanistan (string counterpart; Ghazni and Balkh missing), dzungar-khanate (string 'Khalkha Mongols'), kazakh-khanate (string Tashkent; 1798 loss missing), moghulistan and eastern-chagatai-khanate (no Dughlat events), mongolian-people-s-republic (1932 Tuva cession).
