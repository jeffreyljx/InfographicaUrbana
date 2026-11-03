# Review of batch se-01-d (Phase B)

Reviewer: adversarial review, 2026-10-18. Machine copy: history/notes/phase-b/reviews/se-01-d.json. Validator: 0 errors on all seven dossiers (before and after the reviewer's edits). No Wikipedia infobox for these states gives an area (checked for Ngô dynasty, Hồ dynasty, Sukhothai, Hanthawaddy, Lan Na, Myinsaing, Phayao).

## ngo-dynasty: thin

Thin (for a gap-filler):
- `/keyframe_review/2`: The 970 shape doubles the area (62,155 to 135,575 km2; the bbox reaches 23.3 N and 103 E) and no ledger event explains it. Marked 'Unverified: pages silent', which is acceptable within the 9-page budget. A gap-filler should find what the Đinh held in the northern highlands, or mark the uplands as claimed (vassal/soft) (try https://en.wikipedia.org/wiki/%C4%90inh_B%E1%BB%99_L%C4%A9nh)
- `/ledger/30`: 1363 loss of the western uplands to lan-xang at confidence 1, dated only by Cliopatria (19,000 km2) (try https://en.wikipedia.org/wiki/Tr%E1%BA%A7n_Ngh%E1%BB%87_T%C3%B4ng)
- `/ledger/6, /ledger/11, /ledger/29, /ledger/36`: Confidence-1 bridges: 989 end of the Indrapura occupation, 1069 end of the first Cham vassalage, 1326 end of the second, 1406 return of the 1402 cession (try https://en.wikipedia.org/wiki/Champa%E2%80%93%C4%90%E1%BA%A1i_Vi%E1%BB%87t_War_(1367%E2%80%931390))

Spot checks:
- `/ledger/12` https://en.wikipedia.org/wiki/L%C3%BD%E2%80%93Song_War: confirmed: autumn 1075 fleet 'captured Qinzhou and Lianzhou prefectures'; Yongzhou breached 1 March 1076; after the war 'Đại Việt held control of the Yong, Qin and Lian prefectures'
- `/ledger/16-17` https://en.wikipedia.org/wiki/L%C3%BD%E2%80%93Song_War: confirmed: 1082 Lý Nhân Tông returned Yong, Qin and Lian 'along with their prisoners of war'; Song relinquished four prefectures and a county including Quảng Nguyên; talks 6 July-8 August 1084
- `/ledger/18` https://en.wikipedia.org/wiki/Khmer%E2%80%93Cham_wars: confirmed: 'In 1132, he persuaded Cham king Jaya Indravarman III to join forces with him to attack Đại Việt'; Nghệ An briefly seized
- `/ledger/37, /ledger/39` https://en.wikipedia.org/wiki/H%E1%BB%93_dynasty: confirmed: 'On 11 May 1406, the Yongle Emperor sent two forces for an invasion'; 'The Hồ dynasty was conquered by the Chinese Ming dynasty in 1407'

Area: Ngô dynasty and Hồ dynasty infoboxes give no area (checked); no comparison possible

## sukhothai-kingdom: fail

Findings:
- `/keyframe_review/2, /keyframe_review/3, /keyframe_review/4` (for the author): The 395,000 km2 greatest-extent outline is marked ok for 1294-1362, but the dossier's own source says the empire fell apart soon after 1298 and names the parts that left. Evidence: Sukhothai Kingdom page: 'The tributaries fell away quickly after his death' (Ram Khamhaeng, 1298); 'The dominions north of Uttaradit, among them the Lao kingdoms of Muang Sua and Vieng Chan Vieng Kham ... broke free'; 'In 1319, Martaban in the west broke away'; 'To the south, Suphannaphum Kingdom and Nakhon Si Thammarat left early in Loe Thai's reign ... The kingdom was soon back to what it had been, a small local power.' The keyframe note itself quotes this and keeps the outline anyway ('nothing on the pages replaces it'), but the page names every region that left. Fix: Set sukhothai-kingdom_1294 to adjust with 'applies 1294-1298'. Add new keyframes: c. 1299-1318 = the 1294 shape minus the dominions north of Uttaradit (the 406 cells inside Cliopatria's Lan Xang of 1363, i.e. Muang Sua and Vieng Chan); 1319 onward also minus Martaban and Tenasserim; from early in Loe Thai's reign (before 1323) also minus Suphannaphum and Nakhon Si Thammarat (the peninsula), which leaves about the 1375 core. Mark sukhothai-kingdom_1344, _1352 and _1363 wrong or adjust to match, with the page's sentences in the corrections.
- `/ledger/8` (for the author): The 1363 loss to lan-xang (406 cells, about 118,000 km2) is mis-dated and attributed to the wrong counterpart. Evidence: Sukhothai page: Muang Sua and Vieng Chan 'broke free' right after Ram Khamhaeng's death (1298). Lan Xang page: in the 1360s war Lan Xang was 'victorious in defense of their territory' and the page does not say Lan Xang took land from Sukhothai; Vientiane was taken in 1357 ('In 1357 he took Vientiane and the surrounding plains'). Fix: Move the loss to c. 1299 at confidence 2 (Sukhothai page). Counterpart: the breakaway Lao mueang ('Muang Sua and Vieng Chan', no dossier). Region: the dominions north of Uttaradit. Lan Xang's later gains belong in the lan-xang ledger.
- `/ledger/9` (for the author): The 1375 loss to ayutthaya-kingdom (680 cells, about 214,000 km2, confidence 1) contradicts the page, which dates the loss of the south to early in Loe Thai's reign and to different counterparts. Evidence: Sukhothai page: 'To the south, Suphannaphum Kingdom and Nakhon Si Thammarat left early in Loe Thai's reign' (Loe Thai reigned 1298-1323); Ayutthaya's 1349 invasion and the 1378 submission made Sukhothai 'a tributary' and 'a vassal', with no territorial transfer. Fix: Replace it with losses dated within Loe Thai's reign (c. 1300-1323, confidence 2): the peninsula to Nakhon Si Thammarat (tambralinga, no dossier) and the lower Chao Phraya to Suphannaphum. Add a loss of Tenasserim with Martaban's breakaway in 1319. Record Ayutthaya's 1378-1438 overlordship only as the suzerain's tint.
- `/keyframe_review/1` (for the author): The 1241 shape (271,851 km2) is kept as ok for a newly founded city-state, about 4.3 times the core the page describes. Evidence: The page says the kingdom 'expanded to its greatest extent' only under Ram Khamhaeng (1279-1298), and that after him it was 'soon back to what it had been, a small local power'. That core is the 1375 shape (63,192 km2, 215 cells). The note calls the 1241 shape 'probably a generous claim' but does not resolve it. Rule 5 requires a factor of two or more to be resolved, not only acknowledged. Fix: Mark sukhothai-kingdom_1241 adjust or wrong. Its correction for 1238-1278 should be the Sukhothai and Si Satchanalai core (the 1375 shape or the Sukhothai/Phitsanulok/Uttaradit provinces), with the expansion dated within Ram Khamhaeng's reign as gains (or tributary tints).
- `/ledger/4` (for the author): Sukhothai's vassal_start over hanthawaddy-kingdom is dated 1294 (Cliopatria's year, confidence 1), but the Wareru page dates the acknowledgement by 1287. Its region, the 1294 three-province shape, includes Pegu, which Tarabya held to 1296. Evidence: Wareru page: 'The king of Sukhothai acknowledged Gadu as a vassal king' (after his mission 'By 1287'); 'Still in 1293, Wareru received assurance from Sukhothai of its continued support'. The end (L6, 1319) is confirmed on the Sukhothai page; the Hanthawaddy page gives 'formally independent of Sukhothai in 1330'. Fix: Set year 1287 at confidence 2 with region Mon and Kayin (the Martaban kingdom) and add a note on the extension to the three provinces from c. 1296. Keep 1319 for the end and note the 1330 conflict.

Thin (for a gap-filler):
- `/ledger/1, /ledger/2, /ledger/3`: 1294 gains (peninsula, Tenasserim) and the Phrae and Muang Sua tributary start are at confidence 1 with Cliopatria's year. The pages give only Ram Khamhaeng's reign (1279-1298) (try https://en.wikipedia.org/wiki/Ram_Khamhaeng_inscription)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sukhothai_Kingdom: confirmed: infobox 'Kingdom established: 1238'
- `/ledger/6` https://en.wikipedia.org/wiki/Sukhothai_Kingdom: confirmed: 'In 1319, Martaban in the west broke away'
- `/ledger/7` https://en.wikipedia.org/wiki/Maha_Thammaracha_I: confirmed: 'During the year 1363, due to the pressure from Ayutthaya kingdom ...' the move to Phitsanulok (the Sukhothai infobox gives Song Khwae 1347-1438; the conflict is noted by the author)
- `/ledger/10` https://en.wikipedia.org/wiki/Sukhothai_Kingdom: confirmed: 'Sukhothai existed as an independent polity until 1438'
- `/ledger/8` https://en.wikipedia.org/wiki/Lan_Xang: not on page: the Lan Xang page does not say Lan Xang took land from Sukhothai, and the Sukhothai page dates the northern breakaway to just after 1298 (mis-dated at confidence 1)

Area: No infobox area. The page's own description of a 'small local power' before 1279 and after c. 1323 is about 63,000 km2 (the 1375 core) against 272,000 km2 (1241) and 395,000 km2 (1294-1362). See fixes.

## hanthawaddy-kingdom: thin

Findings:
- `/ledger/1` (applied by reviewer): The gain of Pegu and the delta was dated 1294 (Cliopatria's year, confidence 1) from pagan-kingdom; the Wareru page dates it c. 1296 and takes it from Tarabya, the self-proclaimed king of Pegu. The note's 'Page silent on the year' was wrong. Evidence: Wareru page: 'Tarabya, who had gained control of both Pegu and Dala'; 'By late 1296, the relationship had deteriorated to the point of war'; Wareru 'emerged as the sole ruler of three Mon-speaking provinces of Bassein, Pegu and Martaban c. 1296'. Fix: Year 1296, confidence 2, counterpart 'Tarabya of Pegu', note rewritten with the quotes. keyframe_review/0 'to' changed from 1293 to 1295 and keyframe_review/1 to 'applies 1296-1362'. Applied and re-validated (0 errors, 0 warnings).
- `/identity/capitals/0` (for the author): Martaban is the capital to 1368, but the dossier's own keyframe hanthawaddy-kingdom_1363 and the mottama-rebels dossier put Martaban in rebel hands from 1363 (the rebels' capital is also Martaban 1363-1388). Evidence: Hanthawaddy page: 'Mottama was in open rebellion from 1363 to 1388'. Wareru page footnote: the capital was 'moved to Hanthawaddy Pegu in 1369/70'. Neither page names the seat for 1363-1368. Fix: End Martaban at 1362 and add the seat for 1363-1368 from a page (Donwun in the Burmese chronicles; try the Binnya U article), with a capital_move in 1363 or 1364.

Thin (for a gap-filler):
- `/identity/capitals`: The royal seat for 1363-1369 (see fixes) (try https://en.wikipedia.org/wiki/Binnya_U)
- `/keyframe_review/4-7`: The 1429, 1450, 1487 and 1507 shapes are unverified because of the page budget, which is acceptable; they are 1-3 cells apart (try https://en.wikipedia.org/wiki/Binnya_Ran_I)
- `/ledger`: The 1550-1552 revival (Hanthawaddy page: 'briefly revived in 1550', defeated 'in March 1552') has no extent and needs a rebel dossier (try https://en.wikipedia.org/wiki/Smim_Htaw)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Wareru: mis-dated: the page gives c. 1296 and Tarabya (fixed by reviewer)
- `/ledger/2` https://en.wikipedia.org/wiki/Hanthawaddy_Kingdom: confirmed: 'Mottama was in open rebellion from 1363 to 1388'
- `/ledger/4` https://en.wikipedia.org/wiki/Forty_Years%27_War: confirmed: the war began 'c. December 1385'; truce 1391 to 1401; 'Ava forces withdrew in early 1424' (L12)
- `/ledger/13` https://en.wikipedia.org/wiki/Toungoo%E2%80%93Hanthawaddy_War: confirmed: invasion 'in late 1538'; 'Toungoo forces took Pegu without firing a shot'
- `/ledger/17` https://en.wikipedia.org/wiki/Toungoo%E2%80%93Hanthawaddy_War: confirmed: attack 'In November 1540'; fall 'In May 1541, seven months into the siege'

Area: Hanthawaddy Kingdom infobox gives no area (checked)

## lan-na-kingdom: fail

Findings:
- `/ledger/11, /ledger/12, /identity/end, /keyframe_review/8` (for the author): Lan Na is ended on 2 April 1558 with a loss of all its land to first-toungoo-empire and a dissolve, both at confidence 3. The page describes vassalage, not the end of the state, and K8 cuts Cliopatria's own 1556-1563 shape at 1558. The note on L11 itself says 'Not annexation'. Evidence: Lan Na page: 'Mekuti surrendered on 2 April 1558' and Lan Na 'became a vassal state of the Toungoo dynasty in 1558'; Mekuti stayed king until 'captured by Burmese forces in November 1564'; the infobox runs the kingdom to 1775 with 'Tributary of Burma (1st): 1558-1596'. Schema: vassalage is the suzerain's vassal_start (a tint); the vassal keeps its land. A 'loss' plus 'dissolve' hands the land to Toungoo directly, which contradicts the page and the note. Fix: Remove the 1558 loss; first-toungoo-empire carries vassal_start over lan-na-kingdom in 1558. Continue the dossier at least to the end of its Cliopatria row (1563) or Mekuti's capture (November 1564), with K8 'applies 1556-1563'. Preferably, as section 6 of the author's brief says for two rows of one state (Q1059707), take 'Lan Na' (1600-1761) into cliopatria_names and run the dossier to 1775. The orchestrator must confirm that, because 'lan-na' is also listed for another part; that dossier does not exist yet.
- `/ledger/3/region` (for the author): The gain of Phayao takes the whole Phayao shape, although its text says 'minus its eastern cities that went to Nan'. Evidence: Phayao page: 'the eastern cities of Phayao along the upper Yom basin was annexed into Nan'. The phayao-kingdom dossier's 1338 events now subtract that area (reviewer fix). Fix: Region {"minus": [{"cliopatria": "Phayao Kingdom", "year": 1332}, {"lon": 100.28, "lat": 19.05, "km": 20}], "text": ...}. Note that the 1344 keyframe still includes those 2-3 cells.

Thin (for a gap-filler):
- `/ledger`: Tilokaraj's westward expansion to the Shan States of Laihka, Hsipaw, Mong Nai and Yawnghwe is undated on the page and not drawn (it belongs to shan-states as vassal tints) (try https://en.wikipedia.org/wiki/Tilokaraj)

Spot checks:
- `/ledger/3` https://en.wikipedia.org/wiki/Lan_Na: confirmed: infobox 'Annexation of Phayao: 1338' (the body's 1456 conflict is noted by the author)
- `/ledger/4` https://en.wikipedia.org/wiki/Lan_Xang: confirmed at confidence 2: the Chiang Saen battle and cession sit in the paragraph opening 'In 1353 Fa Ngum was crowned'; the battle itself is undated
- `/ledger/5-8` https://en.wikipedia.org/wiki/Ayutthaya%E2%80%93Lan_Na_War_(1441%E2%80%931474): confirmed: 'In 1451, Sawankhalok broke away from Ayutthaya and joined Lan Na'; 'Ayutthaya captured Chiang Mai in 1452, but was compelled to withdraw'; 1474 'Lan Na then retook the city, putting an end to the conflict'
- `/ledger/11` https://en.wikipedia.org/wiki/Lan_Na: date confirmed ('Mekuti surrendered on 2 April 1558'); the event type is wrong (vassalage, not loss; see fixes)

Area: Lan Na infobox gives no area (checked)

## myinsaing-kingdom: thin

Findings:
- `/ledger/3/region` (for the author): The 1303 gain has region 'Upper Burma', which is not specific enough for 'the Kyaukse, Minbu and Mu granaries' and Tagaung, and it leaves no trace in the keyframes (the 1297-1304 shape already holds all of it). Evidence: Myinsaing page: after the Mongol withdrawal of '4 April 1303' 'the brothers were able to bring all three main granaries of the country, Kyuakse, Minbu and Mu, under their rule' and 'took over Tagaung but could not go any farther north'. Fix: Region: a union of Minbu, the Mu valley (Shwebo) and Tagaung. Either add a keyframe for 1297-1302 without the Mu valley, Minbu and Tagaung, or say in keyframe_review/0 why the 1297 shape already holds them. Add month 4 and the 4 April 1303 date to the note.
- `/keyframe_review/0, /keyframe_review/1` (for the author): The shape keeps 193 Shan-State cells (about 29% of the 672 cells) that the page assigns to the Shan states. This is acknowledged in the author's notes but not corrected. Evidence: Myinsaing page: the brothers 'could not go any farther north' because 'several Shan states now dominated the entire arc surrounding the Irrawaddy valley'. The author's cell count lists Shan 193. Fix: Correction {"minus": [{"cliopatria": "Myinsaing Kingdom", "year": 1294}, {"admin1": "Shan", "country": "Myanmar"}]}, verdict adjust on both keyframes. Tell the kingdom-of-pinya author, because its 1314 shape is identical.

Thin (for a gap-filler):
- `/identity/capitals/0`: Capital coordinates (21.2 N, 95.85 E) are unsourced. The infobox lists Myinsaing, Mekkhaya and Pinle (the three brothers' seats), and only Myinsaing is given (try https://en.wikipedia.org/wiki/Myinsaing)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Myinsaing_Kingdom: confirmed: 'they overthrew Kyawswa on 17 December 1297'
- `/ledger/1` https://en.wikipedia.org/wiki/Myinsaing_Kingdom: confirmed: 'In January 1300, the Burmese army led by Athinkhaya seized lightly manned southernmost Mongol garrisons in Singu and Male'
- `/ledger/2` https://en.wikipedia.org/wiki/Myinsaing_Kingdom: confirmed: full Mongol withdrawal from northern Burma '4 April 1303'
- `/ledger/4` https://en.wikipedia.org/wiki/Myinsaing_Kingdom: confirmed: infobox 'Pinya founded: 7 February 1313'

Area: Myinsaing Kingdom infobox gives no area (checked)

## phayao-kingdom: thin

Findings:
- `/ledger/1` (applied by reviewer): The note quoted the page as 'Mangrai annexed Thoeng and Chiang Kham (1261 campaign)'. The page does not say that: 1261 is Mangrai's accession and the annexation is undated. Evidence: Phayao page: 'When Mangrai ascended to the throne of Ngoenyang in 1261' and 'Mangrai annexed the city of Thoeng and Chiang Kham from the Phayao kingdom' (no year). Mangrai page: 'conquering Chiang Kham and Thoeng, which belonged to the Phayao kingdom' (no year). Fix: Confidence lowered from 2 to 1, and the note and region text rewritten with the true quotes (a bridge at the accession year). Applied.
- `/ledger/3, /identity/successors/1/land` (applied by reviewer): The loss to Nan was drawn as Phrae province, which lies outside Phayao's shape and was not 'of Phayao'. The counterpart was the string 'Nan' while successors use the slug nan-kingdom. Evidence: Phayao page: 'the eastern cities of Phayao along the upper Yom basin was annexed into Nan'. Phrae province lies south of Phayao's bbox (18.86-19.70 N). The Yom headwaters inside Phayao are Pong and Chiang Muan. Fix: Region {lon 100.28, lat 19.05, km 20} with the page's words, counterpart 'nan-kingdom', the same land in successors. Applied; validates (warning only: nan-kingdom has no dossier yet, listed by the author).
- `/ledger/2/region` (applied by reviewer): The loss to Lan Na took the whole shape although its text says 'minus the eastern cities that went to Nan'. Evidence: As above. Fix: Region is now a minus of the same radius from the Phayao 1332 shape. Applied.

Thin (for a gap-filler):
- `/keyframe_review/1`: The page's own extent (the Yonok basin) is larger than Cliopatria's 18 cells. This is thin by design within the 1-2 page budget. The capital (99.90 E) lies about 4 km west of the shape's bbox edge (99.94 E); a 10 km radius around Phayao could be added to the correction (try https://en.wikipedia.org/wiki/Phayao)
- `/ledger/1`: A dated source for Mangrai's annexation of Thoeng and Chiang Kham (now confidence 1) (try https://en.wikipedia.org/wiki/Ngam_Mueang)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Ngoenyang: confirmed: infobox 'Secession of Phayao: 1094'
- `/ledger/1` https://en.wikipedia.org/wiki/Phayao_Kingdom: not on page as quoted: the annexation is undated and 1261 is Mangrai's accession (fixed: confidence 1)
- `/ledger/2` https://en.wikipedia.org/wiki/Phayao_Kingdom: confirmed: 1338 Khamfu 'annexed Phayao into Lanna'
- `/ledger/3` https://en.wikipedia.org/wiki/Phayao_Kingdom: confirmed (year); region wrong, fixed: 'the eastern cities of Phayao along the upper Yom basin was annexed into Nan'

Area: Phayao Kingdom infobox has no area (checked)

## mottama-rebels: thin

Thin (for a gap-filler):
- `/identity/capitals/0`: The seat (Martaban) is assumed. No leader and no boundary are given. This is thin by design: two sentences on two pages (try https://en.wikipedia.org/wiki/Byattaba)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Hanthawaddy_Kingdom: confirmed: 'Mottama was in open rebellion from 1363 to 1388'
- `/ledger/2` https://en.wikipedia.org/wiki/Forty_Years%27_War: confirmed: Razadarit's 'successful capture of Donwun and rest of the northern Martaban province by late 1388'

Area: No Wikipedia article and no Cliopatria row

## Cross-dossier matrix

- ngo-dynasty 982 occupation_start champa -> champa 982 occupation_start: matched (champa L15)
- ngo-dynasty 983 vassal_start champa -> none: missing (champa has no vassal event with ngo-dynasty for 983-1069; schema has the suzerain carry it, reviewer brief rule 3 asks a mirror: orchestrator to fix the convention)
- ngo-dynasty 989 occupation_end champa -> champa 989 occupation_end: matched (both confidence 1)
- ngo-dynasty 1069 gain champa -> champa 1069 loss: matched (same regions)
- ngo-dynasty 1069 vassal_end champa -> none: missing (as 983)
- ngo-dynasty 1075 occupation_start northern-song -> none: exception (northern-song (ea-05) counterpart dossier not written yet (group has not run / part not reached); 'song' in polities/ is the Zhou-era state)
- ngo-dynasty 1077 loss northern-song -> none: exception (northern-song counterpart dossier not written yet (group has not run / part not reached))
- ngo-dynasty 1082 gain northern-song -> none: exception (northern-song counterpart dossier not written yet (group has not run / part not reached))
- ngo-dynasty 1132 contest_start khmer-empire -> khmer-empire 1132 contest_start: matched (khmer L12-L13, end 1136 both sides)
- ngo-dynasty 1258 occupation_start mongol-empire -> none: exception (mongol-empire (ia-02) counterpart dossier not written yet (group has not run / part not reached))
- ngo-dynasty 1285 occupation_start yuan-dynasty -> none: exception (yuan-dynasty (ea-06) counterpart dossier not written yet (group has not run / part not reached) (1285, 1288))
- ngo-dynasty 1306 gain champa -> champa 1306 loss: matched
- ngo-dynasty 1312 vassal_start champa -> none: missing (champa has no 1312-1326 vassal event)
- ngo-dynasty 1363 loss lan-xang -> none: exception (lan-xang (se-01) counterpart dossier not written yet (group has not run / part not reached))
- ngo-dynasty 1371 contest_start champa -> champa 1371 contest_start: matched (end 1390 both sides)
- ngo-dynasty 1402 gain champa -> champa 1402 loss: matched
- ngo-dynasty 1406 loss champa -> champa 1406 gain: matched (ngo confidence 1, champa 2)
- ngo-dynasty 1407 loss ming-dynasty -> none: exception (ming-dynasty (ea-07) counterpart dossier not written yet (group has not run / part not reached))
- sukhothai-kingdom 1238 found khmer-empire -> khmer-empire 1238 loss: matched (khmer L28)
- sukhothai-kingdom 1294 gain Tambralinga -> none: exception (no dossier; listed by the author (tambralinga))
- sukhothai-kingdom 1294 gain pagan-kingdom -> none: missing (pagan-kingdom has no loss of Tenasserim; its 1287 loss of 'Lower Burma' goes to hanthawaddy-kingdom, whose Wareru page says Wareru 'did not control' Tavoy, Mergui, Tenasserim)
- sukhothai-kingdom 1294 vassal_start hanthawaddy-kingdom -> none: mismatch (no mirror in hanthawaddy-kingdom; Wareru page dates the acknowledgement by 1287, not 1294 (sukhothai fix))
- sukhothai-kingdom 1319 vassal_end hanthawaddy-kingdom -> none: mismatch (no mirror; Hanthawaddy page: 'formally independent of Sukhothai in 1330')
- sukhothai-kingdom 1363 loss lan-xang -> none: exception (lan-xang counterpart dossier not written yet (group has not run / part not reached); the event itself is mis-dated (sukhothai fail))
- sukhothai-kingdom 1375 loss ayutthaya-kingdom -> none: exception (ayutthaya-kingdom counterpart dossier not written yet (group has not run / part not reached); the event contradicts the page (sukhothai fail))
- sukhothai-kingdom 1438 loss ayutthaya-kingdom -> none: exception (ayutthaya-kingdom counterpart dossier not written yet (group has not run / part not reached))
- hanthawaddy-kingdom 1287 found pagan-kingdom -> pagan-kingdom 1287 loss: mismatch (pagan L14 gives all 'Lower Burma' to hanthawaddy in 1287; Wareru page: in 1287 'he did not yet control Pegu'; Pegu and Dala were Tarabya's until c. 1296: pagan should split its 1287 loss (Martaban to hanthawaddy, Pegu and the delta to Tarabya of Pegu))
- hanthawaddy-kingdom 1296 gain Tarabya of Pegu -> none: exception (was 1294 from pagan-kingdom (no mirror); reviewer fix; Tarabya's Pegu 1287-1296 has no dossier (listed below))
- hanthawaddy-kingdom 1363 loss mottama-rebels -> mottama-rebels 1363 gain: matched
- hanthawaddy-kingdom 1388 gain mottama-rebels -> mottama-rebels 1388 loss: matched
- hanthawaddy-kingdom 1412 vassal_start Arakan (Launggyet kingdom) -> none: exception (no dossier; listed by the author (launggyet-kingdom))
- hanthawaddy-kingdom 1415 occupation_start ava-kingdom -> none: exception (ava-kingdom counterpart dossier not written yet (group has not run / part not reached))
- hanthawaddy-kingdom 1538 loss first-toungoo-empire -> none: exception (first-toungoo-empire counterpart dossier not written yet (group has not run / part not reached) (1538, 1539, 1541))
- lan-na-kingdom 1292 gain haripunjaya -> haripunjaya 1292 dissolve: matched (haripunjaya L8 dissolves to lan-na-kingdom)
- lan-na-kingdom 1292 found ngoenyang -> none: exception (no dossier; listed by the author)
- lan-na-kingdom 1338 gain phayao-kingdom -> phayao-kingdom 1338 loss: mismatch (same year; land differs by the eastern cities (phayao now minus them, lan-na whole shape): lan-na fix)
- lan-na-kingdom 1353 loss lan-xang -> none: exception (lan-xang counterpart dossier not written yet (group has not run / part not reached))
- lan-na-kingdom 1452 occupation_start ayutthaya-kingdom -> none: exception (ayutthaya-kingdom counterpart dossier not written yet (group has not run / part not reached))
- lan-na-kingdom 1558 loss first-toungoo-empire -> none: exception (first-toungoo-empire counterpart dossier not written yet (group has not run / part not reached); the event should be the suzerain's vassal_start, not a loss (lan-na fail))
- myinsaing-kingdom 1297 found pagan-kingdom -> pagan-kingdom 1297 dissolve: matched (pagan ends 1297-12 with myinsaing-kingdom among successors)
- myinsaing-kingdom 1303 gain yuan-dynasty -> none: exception (yuan-dynasty counterpart dossier not written yet (group has not run / part not reached))
- phayao-kingdom 1094 found ngoenyang -> none: exception (no dossier; listed by the author)
- phayao-kingdom 1261 loss ngoenyang -> none: exception (no dossier; listed by the author)
- phayao-kingdom 1338 loss nan-kingdom -> none: exception (no dossier; listed by the author (counterpart string fixed from 'Nan'))

## Problems

- Vassal mirror convention: reviewer brief rule 3 asks the vassal to carry a vassal_start with the suzerain as counterpart, but the schema says counterpart is 'the vassal itself in both events' (suzerain's ledger), so a vassal-side mirror would read reversed; champa (for ngo-dynasty 983-1069, 1312-1326) and hanthawaddy-kingdom (for sukhothai 1287-1319) are listed as missing pending the orchestrator's convention.
- lan-na-kingdom and Cliopatria's 'Lan Na' (slug lan-na, assigned to another part, not yet written) are one state (Q1059707; infobox to 1775): the orchestrator must decide the merge before the lan-na-kingdom fail can be fixed in full; the minimum fix (no 1558 loss, run to 1563/1564) does not need it.
- kingdom-of-pinya (not yet written) inherits Myinsaing's identical 672-cell shape with 193 Shan-State cells the Myinsaing page gives to 'several Shan states'.
- pagan-kingdom (se-01-c, written) gives all Lower Burma to hanthawaddy-kingdom in 1287; the Wareru page puts Pegu and the delta under Tarabya until c. 1296: route to the pagan author.
- WebFetch returns a model's summary: the Hanthawaddy infobox capital rows came back as year ranges without names, so the 1363-1369 seat could not be read from the page.
- Reviewer edits applied in place (re-validated, read back): hanthawaddy-kingdom /ledger/1, /keyframe_review/0, /keyframe_review/1; phayao-kingdom /ledger/1, /ledger/2, /ledger/3, /identity/successors/1.
