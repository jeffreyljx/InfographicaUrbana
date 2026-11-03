# Review of batch ea-07 (2026-10-25)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Seven dossiers; validator: 0 errors in all, 8 warnings (Ruili, ming-dynasty). Spot checks: 40 events on 20 pages, all confirmed in year; one region misplaced (ming /ledger/47-48).

| slug | verdict | fixes (applied/open) |
| --- | --- | --- |
| ming-dynasty | fix | 5/8 |
| li-zicheng | fix | 0/2 |
| southern-ming | fix | 0/5 |
| xi-dynasty | fix | 0/3 |
| wu-sangui-s-zhou | pass | 0/0 |
| jianzhou-jurchens | fix | 0/4 |
| haixi-jurchens | fix | 0/1 |

## ming-dynasty: fix

Area: infobox 3900000 (1400), Cliopatria 4941000, ratio 1.27. 1450: infobox 6,500,000 against the 1450 shape 4,960,000 (0.76), also acknowledged.

Findings:
- [APPLIED] `/ledger/16, /ledger/17, /ledger/18, /wars/0/belligerents`: Yunnan 1381-82 named northern-yuan as counterpart; the Yuan prince of Liang has his own dossier, principality-of-liang-yunnan, which records the same 1381 contest_start, 1382-01 contest_end and 1382-01 dissolve with counterpart ming-dynasty. Evidence: Ming conquest of Yunnan page: 'Basalawarmi, committed suicide on January 6, 1382, as the Ming dynasty troops overwhelmed'; Ming troops sent 'to crush the remaining Yuan-held territory in Yunnan in 1381'. principality-of-liang-yunnan /ledger/1-3. Fix: Counterpart changed to principality-of-liang-yunnan on the three events and in the war's belligerents.
- [APPLIED] `/ledger/19, /wars/0/belligerents`: Counterpart 'Duan family of Dali' (a name) while the dossier duan-governors-of-dali exists and records the 1383-02 dissolve to ming-dynasty. Evidence: Ming conquest of Yunnan page: 'The last Dali stronghold of Dengchuan fell to the Ming in February 1383'. duan-governors-of-dali /ledger/5. Fix: Counterpart changed to duan-governors-of-dali; drop duan-family-of-dali from counterparts_needing_dossiers.
- [APPLIED] `/ledger/31, /ledger/45`: Counterpart 'Qara Del (Hami)' (a name) while the dossier kara-del exists and records vassal_start 1404 and vassal_end 1513 with counterpart ming-dynasty. Evidence: Hami page: 'The Ming dynasty established this region as Kumul Hami in 1404 after the Mongol kingdom Qara Del accepted its supremacy'; 'Hami was conquered and converted to Islam in 1513.' kara-del /ledger/3, /ledger/10. Fix: Counterpart changed to kara-del; drop qara-del from counterparts_needing_dossiers.
- [APPLIED] `/ledger/50`: Counterpart portuguese-colonies has no dossier: the Cliopatria row is merged into portuguese-empire (cliopatria_names 'Portuguese Empire', 'Portuguese Colonies'), which records the 1557 Macau gain from ming-dynasty. Evidence: Ming dynasty page: 'the Portuguese gained consent from the Ming court in 1557 to settle Macau'. portuguese-empire /ledger/20. Fix: Counterpart changed to portuguese-empire.
- [APPLIED] `/ledger/47, /ledger/48`: Confidence 3 on a region the page does not name: the place Ningbo with 40 km is a disc round Ningbo city, about 58 km short of Shuangyu on Liuheng Island, which the page names. Evidence: Jiajing wokou raids page: 'Shuangyu on Liuheng Island (六橫島) off the coast of Ningbo'; 'In 1539, Fujianese traders started to guide foreign traders ... to barter in Shuangyu' ... 'started to occupy the island'; razed June 1548. Fix: Confidence lowered to 2 (applied). Author: replace the region with a small disc on Liuheng Island (about 122.13 E, 29.73 N, 15 km; 'Liuheng Island' is not in the gazetteer) and keep the text.
- `/ledger/14`: The 1372 tribute is Chuzan's, not the Ryukyu Kingdom's: ryukyu-kingdom starts in 1429 and has its own vassal_start 1429; chuzan /ledger/2 has the 1372 vassal_start and /ledger/10 the 1429 vassal_end, both naming ming-dynasty, with no mirror here. Evidence: Ryukyu Kingdom page: 'the tributary relationship with Ming dynasty China, begun by Chūzan in 1372'; 'Hashi conquered ... Nanzan in 1429, uniting the island of Okinawa'. Fix: Set /ledger/14 counterpart to chuzan; add 1429 vassal_end (counterpart chuzan) and 1429 vassal_start (counterpart ryukyu-kingdom), region Okinawa, source the Ryukyu Kingdom page, so that /ledger/69 (1644 vassal_end ryukyu-kingdom) has its start.
- `/ledger/30, /ledger/59`: The Jianzhou vassalage is one-sided and outlives its counterpart: jianzhou-jurchens (same batch) has no vassal_start 1403 or vassal_end, and the 1618 vassal_end names jianzhou-jurchens, which dissolved in 1616 into later-jin-dynasty. Evidence: Nurhaci page: 'In 1616, Nurhaci declared himself Khan and founded the Jin dynasty'; the /ledger/59 quote ('In 1618, he openly renounced the Ming overlordship') is about Nurhaci's Jin. Fix: Change /ledger/59 counterpart to later-jin-dynasty (and add a 1616 vassal_end jianzhou-jurchens / vassal_start later-jin-dynasty pair, or end the Jianzhou vassalage in 1616), and add the mirror vassal_start 1403 in jianzhou-jurchens.
- `/ledger/7, /ledger/8, /ledger/9, /ledger/15`: The 1369 gains (Hebei, Shanxi, Shaanxi) and the 1374 gain (Gansu, Ningxia, Guizhou, Hainan) name yuan-dynasty, which ended in September 1368 (its /ledger/50 dissolve to ming-dynasty, /ledger/48 split to northern-yuan). Evidence: Hongwu page: Shaanxi 'fully captured ... by September 1369, but border skirmishes with Köke Temür's troops persisted until 1370'; Köke Temür fought for the Northern Yuan. Fix: Name northern-yuan (or nobody for the 1374 bridge, which no page dates) and leave northern-yuan's missing losses to ia-02.
- `/ledger (missing, 1444)`: No Ming gain of the Mong Mao (Luchuan) lands in 1444, though shan-states /ledger/5 (1444 loss, c3) and mong-mao /ledger/3 (1444 dissolve, c3) both hand them to ming-dynasty, and this dossier's Luchuan-Pingmian contest (/ledger/41-42) ends in 1449 with no outcome. Evidence: shan-states /ledger/5 and mong-mao /ledger/3; the war note gives no territorial result. Fix: Add a 1444 gain (counterpart mong-mao or shan-states, region as in their dossiers) from the Luchuan-Pingmian campaigns page, or say in the war note why the land is not counted.
- `/ledger (missing, 1643)`: xi-dynasty /ledger/2 has Zhang abandoning Wuchang in 1643 and the Ming retaking it; there is no 1643 gain of Wuchang here. Evidence: Zhang Xianzhong page: 'abandoned the city after two months when Ming forces gathered strength'. Fix: Add a 1643 gain of Wuhan 60 km, counterpart xi-dynasty, confidence 2, source the Zhang Xianzhong page.
- `/keyframe_review/4`: The 1385 shape is marked ok though it holds Liaoning and Jilin, which the 1375 verdict removes until 1387-88; the 1387 and 1388 gains then change nothing on the map. Evidence: Hongwu page: the 1387 Manchuria campaign and, after Lan Yu's 1388 Buir Lake victory, 'The campaign also resulted in the annexation of the Liaodong Peninsula.' Fix: Mark 1385 adjust with the same minus as 1375 (to 1387), or keep both shapes ok and drop the 1375 correction; be consistent.
- `/wars/7, /ledger/43`: The Tumu Crisis has no zones and its note does not say no ground changed, while /ledger/43 records a 1450 loss to four-oirats; four-oirats /ledger/4 dates its gain from the Ming in 1447. Evidence: The /ledger/43 note itself quotes the Tumu page: 'There were no territorial changes'. Fix: Say in the war note that no ground changed; make /ledger/43 a Cliopatria bridge with counterpart nobody, or align the year with four-oirats (1447) and name the land.
- `/ledger (missing: tributaries and borders recorded by neighbours)`: Neighbour dossiers name ming-dynasty in events this ledger lacks: sultanate-of-malacca vassal_start 1405 and vassal_end 1511; kara-del occupation 1391-1404 and its 1446 changes; ai-viet 1540 loss of north-east Quang Ninh; mongol-khanate 1495 gain (against this /ledger/46, 1516, counterpart nobody); northern-yuan 1415 loss (c1). Evidence: rev scan of polities/*.json for counterpart ming-dynasty with no mirror within a year. Fix: Add the Malacca vassalage and the 1540 Mac cession (both in the group scope), and either add or answer the others in notes.

Thin (for a gap-filler):
- `/keyframe_review/5 and /ledger (no event)`: The 1402 shape adds Qinghai, Gansu and Ningxia with no ledger event; unverified: page budget. Try https://en.wikipedia.org/wiki/Xining
- `/ledger/44`: 1468 withdrawal from Qinghai and western Gansu, confidence 1. Try https://en.wikipedia.org/wiki/Jiayu_Pass
- `/ledger/43, /ledger/46`: Steppe retreats of 1450 and 1516, confidence 1; mongol-khanate dates its gain 1495. Try https://en.wikipedia.org/wiki/Dayan_Khan
- `/ledger/56`: 1600 return of the west-Yunnan tusi lands, confidence 1; first-toungoo-empire ends its vassalage of the Chinese Shan states in 1597. Try https://en.wikipedia.org/wiki/Sino-Burmese_War_(1582%E2%80%931584)
- `/ledger/7, /ledger/15, /ledger/63`: Hebei 1369, the 1374 bridge (Gansu, Ningxia, Guizhou, Hainan) and the 1622 Liaodong bridge are confidence 1. Try https://en.wikipedia.org/wiki/Liaodong_Regional_Military_Commission
- `/keyframe_review/3/correction`: The 1375 correction removes all of Liaoning; a Ming presence in southern Liaodong before 1387 (the Liaodong command) would make Cliopatria's 1375 shape partly right. Try https://en.wikipedia.org/wiki/Liaodong_Regional_Military_Commission

Spot checks: /ledger/9 confirmed; /ledger/13 confirmed; /ledger/25 confirmed (the Liaodong sentence follows the 1388 Buir Lake sentence); /ledger/18 confirmed (counterpart corrected); /ledger/27 confirmed; /ledger/34 confirmed; /ledger/31, /ledger/45 confirmed; /ledger/47 confirmed year and island; region misplaced (confidence lowered); /ledger/62 confirmed; /ledger/65 confirmed

## li-zicheng: fix

Area: infobox None (None), Cliopatria 407378, ratio None. the Wikipedia infobox gives no area

Findings:
- `/keyframe_review/4/correction, /ledger (missing)`: The 1644 keyframe takes Cliopatria's 1642 shape, which holds Henan and northern Hubei, but no event gains Henan (the 1643 keyframe excludes it) while /ledger/9 loses it in 1645. Evidence: Li Zicheng page: 'in 1643, Li Zicheng's victory against Sun Chuanting in central Henan reaffirmed his decision to march west to Xi'an'; the author's report lists 'Henan never dated as held'. Fix: Either add a 1643 gain of Henan (counterpart ming-dynasty, confidence 1 or 2, Li Zicheng page) with the Ming's mirror loss, or take Henan out of the 1644 correction and out of /ledger/9.
- `/wars/1`: The war 'Late Ming peasant rebellions' runs 1629-1644, before the state's life begins (1643). Evidence: Brief rule: wars inside the life. Fix: Set from 1643 (keep 1629 in the note) or say in the note that the span is the rebellion's.

Thin (for a gap-filler):
- `/ledger/9`: Loss of Shanxi and Henan to the Qing, confidence 1, no month. Try https://en.wikipedia.org/wiki/Battle_of_Tongguan_(1645)

Spot checks: /ledger/0 confirmed; /ledger/4 confirmed (April 1644; 24 April on the Qing conquest page); /ledger/7 confirmed (27 May 1644); /ledger/8 confirmed (6 June 1644); /ledger/10 confirmed

## southern-ming: fix

Area: infobox None (None), Cliopatria 2179980, ratio None. the Wikipedia infobox gives no area

Findings:
- `/ledger/21`: A 1661 'loss' of the whole country Myanmar: the Southern Ming never held Burma (the court was a guest at Ava) and no event gains it, so the region is wrong and the event moves no land of this state. Evidence: Southern Ming page: the Yongli Emperor 'flees into Burma'; the note itself calls it 'the Yongli court at Ava'. Fix: Drop the event or give it a 20 km disc at Ava and type it as the court's surrender (no territorial counterpart); the 1659-01 capital_move already carries the exile.
- `/ledger (missing, 1645)`: xi-dynasty /ledger/7 loses Chongqing to southern-ming in spring 1645; no gain here. Evidence: Zhang Xianzhong page: 'Chongqing was retaken by Ming loyalists in the spring of 1645.' Fix: Add a 1645 gain of Chongqing 80 km, counterpart xi-dynasty, confidence 2, source the Zhang Xianzhong page (already in sources), or agree with the Xi author on 'nobody'.
- `/ledger/13 and /ledger (missing, 1650)`: Guangxi is regained in August 1652 but never lost: the 1648 shape and the ledger keep it through 1650-52. Evidence: Southern Ming page: Li Dingguo 'retook Guilin (Guangxi province) from the Qing' in early August 1652; the page does not date Guilin's fall. Fix: Add the 1650 loss of Guilin and Guangxi to the Qing (confidence 1 if no page dates it), or make /ledger/13 a contest/occupation of Guilin only.
- `/ledger/12`: The 1650 loss is Guangzhou 150 km only, but the 1653 correction drops all of Guangdong; western Guangdong leaves with no event. Evidence: Southern Ming page: Qing armies 'reconquer ... Jiangxi, and Guangdong in 1649 and 1650'. Fix: Make the 1650 loss region Guangdong (admin1), keeping the Guangzhou text.
- `/keyframe_review/1/correction`: The 1645-1647 correction removes Fujian for the whole span and keeps Guangdong, but the ledger loses Nanjing in June 1645, Fujian in October 1646 and Guangzhou in January 1647; the note says the corrected shape 'holds from 1646'. Evidence: /ledger/2, /ledger/6, /ledger/8. Fix: Describe the shape at its start (1645 shape minus the Nanjing area after June) and let the ledger carry 1646-47, or give the keyframe from 1646.

Thin (for a gap-filler):
- `/ledger/19`: Guizhou and Guangxi to the Qing in 1659, confidence 1. Try https://en.wikipedia.org/wiki/Li_Dingguo
- `/keyframe_review/3`: How Guizhou and Yunnan came to the Southern Ming (Sun Kewang's Xi remnant, 1647-52) is not in the ledger; no xi-remnant dossier. Try https://en.wikipedia.org/wiki/Li_Dingguo

Spot checks: /ledger/2 confirmed (8 June 1645); /ledger/6 confirmed (Fuzhou 17 October 1646); /ledger/12 confirmed (24 November 1650); /ledger/13 confirmed (early August 1652); /ledger/18 confirmed (late January 1659)

## xi-dynasty: fix

Area: infobox None (None), Cliopatria None, ratio None. the Wikipedia infobox gives no area

Findings:
- `/keyframe_review/1, /ledger (missing, 1644)`: Hunan, gained in 1643 and in the 1643 keyframe, is gone from the 1644 keyframe with no loss event. Evidence: Zhang Xianzhong page: at Changsha he 'controlled much of Hunan and part of Jiangxi', then moved into Sichuan in 1644. Fix: Add a 1644 loss of Hunan (counterpart nobody or southern-ming, confidence 1) or say why Hunan drops.
- `/identity/successors`: southern-ming is missing from successors although the infobox lists it and /ledger/7 hands Chongqing to it. Evidence: Xi dynasty infobox: succeeded by 'Qing dynasty' and 'Southern Ming'. Fix: Add southern-ming with land Chongqing 80 km (1645).
- `/ledger/4, /ledger/5`: The 1644 gains of Chongqing (July) and Sichuan (September) name ming-dynasty, which ended in April 1644; the Ming ledger has no Sichuan loss (only its successors entry). Evidence: Ming dynasty infobox: 'Fall of Beijing: 25 April 1644'; Hongguang crowned 19 June 1644. Fix: Name southern-ming (with mirror losses there) or nobody; keep the note.

Spot checks: /ledger/0 confirmed; /ledger/4 confirmed (25 July 1644); /ledger/7 confirmed; /ledger/8 confirmed (October 1646); /ledger/9 confirmed (January 1647, Xichong; infobox 2 January)

## wu-sangui-s-zhou: pass

Area: infobox None (None), Cliopatria None, ratio None. the Wikipedia infobox gives no area

Thin (for a gap-filler):
- `/ledger/7, /ledger/8`: Shang Zhixin's surrender and the end of the 1676 north-west reach, confidence 1, no year on either page. Try https://en.wikipedia.org/wiki/Shang_Zhixin
- `/identity/capitals`: No seat before 1678 (Kunming as feudatory seat is likely but undated on the pages opened). Try https://en.wikipedia.org/wiki/Wu_Sangui

Spot checks: /ledger/0 confirmed (28 December 1673); /ledger/2 confirmed (7 January 1674); /ledger/12 confirmed (1680); /ledger/13 confirmed (October 1681); /ledger/14 confirmed (December 1681)

## jianzhou-jurchens: fix

Area: infobox None (None), Cliopatria None, ratio None. the Wikipedia infobox gives no area

Findings:
- `/ledger (missing, 1403 and 1616)`: No vassal events, although ming-dynasty /ledger/30 (vassal_start 1403) and /ledger/59 (vassal_end) name this state; the found event names ming-dynasty as if land came from the Ming. Evidence: Jianzhou Jurchens page: 'Ahacu ... became commander of the Jianzhou Guard in 1403'; Ming dynasty ledger /30, /59. Fix: Add vassal_start 1403 (counterpart ming-dynasty, same disc) and vassal_end 1616 (or carry it to later-jin), and set the found counterpart to nobody unless a page says the land was Ming's.
- `/ledger/2, /ledger/3, /keyframe_review/1-3/correction, /identity/successors`: The stand-in discs cover Ming-held Liaodong: Benxi 70 km reaches Shenyang (about 60 km) and Liaoyang (about 50 km), Tieling 60 km covers Tieling and Kaiyuan, and Dandong 50 km the Yalu forts, all Ming until 1618-21 (ming-dynasty /58, /60, /62; later-jin /2, /3, /6). The map would draw the Ming cities as Jianzhou land from 1591 and 1601. Evidence: Ming and Later Jin ledgers; Nurhaci page: Fushun 1618, Tieling 'in the summer of 1619', Liaoyang and Shenyang 'By May 1621'. Fix: Subtract the Ming shape of the year from each disc (minus cliopatria Ming Dynasty) or move the discs east of the Liaodong wall (Hada round 124.6 E, 42.7 N).
- `/wars/2`: 'Nurhaci's conquest of the Hulun' runs to 1619, after this state's 1616 end. Evidence: Brief rule: wars inside the life. Fix: End it 1616 here (the Yehe 1619 belongs to later-jin-dynasty) or say so in the note.
- `/wars/0`: 'Korean and Ming counterattacks on the Jianzhou' (1467-1478) has no zones and no note saying no ground changed. Evidence: Brief rule: empty zones only where no ground changed hands, and said so. Fix: Add the note or a zone.

Thin (for a gap-filler):
- `/keyframe_review/0`: The 1403-1590 disc sits at Xinbin for 188 years; the guards lay further north-east in the early 15th century (the page says only 'modern-day Liaoning and Jilin'). Try https://en.wikipedia.org/wiki/M%C3%B6ngke_Tem%C3%BCr

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (1587); /ledger/2 confirmed ('By 1591, he controlled a swathe of territory stretching from Fushun to the Yalu River'); /ledger/6 confirmed (Ula 1613); /ledger/7 confirmed (1616)

## haixi-jurchens: fix

Area: infobox None (None), Cliopatria None, ratio None. the Wikipedia infobox gives no area

Findings:
- `/ledger/0, /ledger/1, /keyframe_review/0/correction`: The Hada stand-in, Tieling 60 km, covers the Ming garrisons of Tieling and Kaiyuan and reaches the northern edge of Shenyang (Ming until 1619-21): the map would draw Ming Liaodong as Haixi land from 1520. Evidence: ming-dynasty /ledger/60 and later-jin-dynasty /ledger/3 (Tieling Ming until 1619); Haixi page: the Haixi lived in 'parts of modern-day Jilin, Heilongjiang, Liaoning, and Inner Mongolia'. Fix: Subtract the Ming shape of the year from the disc or move it north-east of Kaiyuan (about 124.6 E, 42.7 N); mirror the change in jianzhou-jurchens /ledger/3.

Thin (for a gap-filler):
- `/ledger/0`: Founding in the 1520s at confidence 1 and no capital; Ming vassalage (Wangji Wailan's peerage) undated. Try https://en.wikipedia.org/wiki/Wang_Tai

Spot checks: /ledger/0 confirmed ('in the 1520s'); /ledger/1 confirmed (1601); /ledger/2 confirmed (Hoifa 1607); /ledger/4 confirmed (1619 siege; Yehe 1619 on the Nurhaci page)

## Cross-dossier matrix (unmatched rows)

- mismatch: ming-dynasty /ledger/7 1369 gain cp=yuan-dynasty. yuan-dynasty ended 1368-09; Shanxi and Shaanxi were taken from Köke Temür (Northern Yuan). Name northern-yuan; northern-yuan (ia-02) lacks the loss.
- mismatch: ming-dynasty /ledger/8 1369 gain cp=yuan-dynasty. As /7: counterpart dead since 1368-09.
- mismatch: ming-dynasty /ledger/9 1369 gain cp=yuan-dynasty. As /7: counterpart dead since 1368-09.
- missing: ming-dynasty /ledger/11 1370 gain cp=northern-yuan. northern-yuan (ia-02) has the 1370 contest_start and 1388 contest_end but no loss of Inner Mongolia.
- missing: ming-dynasty /ledger/12 1371 vassal_start cp=tibet. tibet (ea-06) has no Ming vassal events; the vassalage is contested on the page (Goldstein).
- mismatch: ming-dynasty /ledger/14 1372 vassal_start cp=ryukyu-kingdom / mirror chuzan  1372 vassal_start. The 1372 tribute is chuzan's (chuzan /2, 1372 vassal_start; /10, 1429 vassal_end); ryukyu-kingdom starts 1429 with its own vassal_start (/2). Fix in ming-dynasty.
- mismatch: ming-dynasty /ledger/15 1374 gain cp=yuan-dynasty. 1374 bridge names yuan-dynasty, dead since 1368-09.
- missing: ming-dynasty /ledger/22 1387 gain cp=northern-yuan. Naghachu has no dossier; northern-yuan (ia-02) stands in and records no loss.
- missing: ming-dynasty /ledger/25 1388 gain cp=northern-yuan. As /22.
- missing: ming-dynasty /ledger/29 1401 vassal_start cp=joseon. joseon (jk-02) has no Ming vassal events.
- missing: ming-dynasty /ledger/30 1403 vassal_start cp=jianzhou-jurchens. Same batch: jianzhou-jurchens has no vassal_start 1403.
- exception: ming-dynasty /ledger/35 1409 vassal_start cp=Nurgan Jurchens. Nurgan Jurchens: no dossier, listed in counterparts_needing_dossiers.
- exception: ming-dynasty /ledger/40 1435 vassal_end cp=Nurgan Jurchens. As /35.
- mismatch: ming-dynasty /ledger/43 1450 loss cp=four-oirats / mirror four-oirats  1447 gain. four-oirats /4 gains from ming-dynasty in 1447; this loss is 1450 (c1, Cliopatria bridge).
- exception: ming-dynasty /ledger/47 1539 occupation_start cp=Wokou pirates. Wokou pirates: no dossier; listed in counterparts_needing_dossiers.
- exception: ming-dynasty /ledger/48 1548 occupation_end cp=Wokou pirates. Wokou pirates: no dossier; listed in counterparts_needing_dossiers.
- exception: ming-dynasty /ledger/49 1554 occupation_start cp=Wokou pirates. Wokou pirates: no dossier; listed in counterparts_needing_dossiers.
- exception: ming-dynasty /ledger/51 1559 occupation_end cp=Wokou pirates. Wokou pirates: no dossier; listed in counterparts_needing_dossiers.
- exception: ming-dynasty /ledger/52 1562 occupation_start cp=Wokou pirates. Wokou pirates: no dossier; listed in counterparts_needing_dossiers.
- mismatch: ming-dynasty /ledger/53 1563 loss cp=first-toungoo-empire / mirror first-toungoo-empire  1563 vassal_start. first-toungoo-empire records vassal_start 1563 of "Chinese Shan states" (/27), not a gain from the Ming.
- exception: ming-dynasty /ledger/54 1563 occupation_end cp=Wokou pirates. Wokou pirates: no dossier; listed in counterparts_needing_dossiers.
- missing: ming-dynasty /ledger/55 1567 vassal_end cp=tibet. As /12.
- mismatch: ming-dynasty /ledger/56 1600 gain cp=first-toungoo-empire / mirror first-toungoo-empire  1597 vassal_end. first-toungoo-empire ends that vassalage in 1597 (/60); this gain is 1600 (c1).
- mismatch: ming-dynasty /ledger/59 1618 vassal_end cp=jianzhou-jurchens. jianzhou-jurchens dissolved 1616; the 1618 renunciation is later-jin-dynasty's.
- missing: ming-dynasty /ledger/64 1637 vassal_end cp=joseon. As /29; joseon has the 1636-37 contest with later-jin only.
- mismatch: li-zicheng /ledger/8 1644 loss cp=qing-dynasty / mirror qing-dynasty  1644 gain. qing-dynasty /3 (1644-06 gain) names "Shun regime of Li Zicheng", not the slug li-zicheng (ea-08).
- missing: li-zicheng /ledger/9 1645 loss cp=qing-dynasty. qing-dynasty (ea-08) has no 1645 gains from li-zicheng.
- missing: li-zicheng /ledger/10 1645 loss cp=qing-dynasty. As /9.
- missing: li-zicheng /ledger/11 1645 dissolve cp=qing-dynasty. As /9.
- exception: southern-ming /ledger/1 1644 found cp=ming-dynasty. Successor in ming-dynasty identity (land: Cliopatria Southern Ming 1645); the Ming dissolve names li-zicheng.
- missing: southern-ming /ledger/10 1648 gain cp=qing-dynasty. qing-dynasty (ea-08) has no 1648 loss of Guangdong (Li Chengdong).
- missing: southern-ming /ledger/21 1661 loss cp=qing-dynasty. Region wrong (whole Myanmar); qing has no mirror. See the southern-ming fix.
- missing: southern-ming /ledger/22 1662 dissolve cp=qing-dynasty. qing-dynasty (ea-08) has no 1662 gain.
- missing: xi-dynasty /ledger/2 1643 loss cp=ming-dynasty. Same batch: ming-dynasty has no 1643 regain of Wuchang.
- exception: xi-dynasty /ledger/4 1644 gain cp=ming-dynasty. Counterpart ming-dynasty ended April 1644; the Ming lists xi-dynasty as successor for Sichuan. Better southern-ming or nobody.
- exception: xi-dynasty /ledger/5 1644 gain cp=ming-dynasty. As /4.
- missing: xi-dynasty /ledger/7 1645 loss cp=southern-ming. Same batch: southern-ming has no 1645 gain of Chongqing.
- mismatch: xi-dynasty /ledger/9 1647 dissolve cp=qing-dynasty / mirror qing-dynasty  1648 gain. qing-dynasty /9 gains Sichuan in 1648 (c1) from "Zhang Xianzhong's Xi regime and Ming loyalists in Sichuan", not the slug, and 1-2 years later (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/0 1673 found cp=qing-dynasty / mirror qing-dynasty /ledger/15 1673 loss. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/1 1674 gain cp=qing-dynasty / mirror qing-dynasty /ledger/17 1674 loss. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/2 1674 gain cp=qing-dynasty / mirror qing-dynasty /ledger/15 1673 loss. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/3 1674 gain cp=qing-dynasty / mirror qing-dynasty /ledger/16 1674 loss. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/4 1676 gain cp=qing-dynasty / mirror qing-dynasty /ledger/19 1676 loss. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/5 1676 loss cp=qing-dynasty / mirror qing-dynasty /ledger/22 1680 gain. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08). Years differ by 4: qing has Fujian and Guangdong back only in 1680 (c1).
- mismatch: wu-sangui-s-zhou /ledger/7 1677 loss cp=qing-dynasty / mirror qing-dynasty /ledger/22 1680 gain. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08). Years differ by 3: qing has Fujian and Guangdong back only in 1680 (c1).
- mismatch: wu-sangui-s-zhou /ledger/11 1678 loss cp=qing-dynasty / mirror qing-dynasty /ledger/20 1678 gain. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/12 1680 loss cp=qing-dynasty / mirror qing-dynasty /ledger/21 1680 gain. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/13 1681 loss cp=qing-dynasty / mirror qing-dynasty /ledger/23 1681 gain. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: wu-sangui-s-zhou /ledger/14 1681 dissolve cp=qing-dynasty / mirror qing-dynasty /ledger/23 1681 gain. qing-dynasty names southern-ming for the Three Feudatories; should be wu-sangui-s-zhou (ea-08).
- mismatch: jianzhou-jurchens /ledger/0 1403 found cp=ming-dynasty / mirror ming-dynasty  1403 vassal_start. ming-dynasty records a vassal_start (/30), not a land loss; jianzhou has no vassal events.
- mismatch: jianzhou-jurchens /ledger/7 1616 dissolve cp=later-jin-dynasty / mirror later-jin-dynasty  1616 found. later-jin-dynasty /0 (found 1616-02) names ming-dynasty and lists only ming-dynasty as predecessor (ea-08).
- mismatch: haixi-jurchens /ledger/4 1619 dissolve cp=later-jin-dynasty / mirror later-jin-dynasty  1619 gain. later-jin-dynasty /4 (1619 gain) names "Yehe (Hulun tribe)", not haixi-jurchens (ea-08).
- missing: shan-states /ledger/5 1444 loss cp=ming-dynasty. ming-dynasty has no 1444 gain of the Luchuan lands (see ming fix).
- missing: mong-mao /ledger/3 1444 dissolve cp=ming-dynasty. As above.
- missing: kara-del /ledger/1 1391 occupation_start cp=ming-dynasty. ming-dynasty has no 1391-1404 occupation of Hami.
- missing: kara-del /ledger/6 1446 occupation_start cp=ming-dynasty. ming-dynasty has no 1446 events for Hami (kara-del also has vassal_end/start 1446).
- missing: sultanate-of-malacca /ledger/1 1405 vassal_start cp=ming-dynasty. ming-dynasty has no Malacca vassalage (1405-1511).
- missing: ai-viet /ledger/2 1540 loss cp=ming-dynasty. ming-dynasty has no 1540 gain of north-east Quang Ninh (Mac cession).
- mismatch: mongol-khanate /ledger/2 1495 gain cp=ming-dynasty. ming-dynasty /46 loses the same Cliopatria delta in 1516 to nobody (c1).
- missing: northern-yuan /ledger/7 1415 loss cp=ming-dynasty. ming-dynasty has no 1415 gain from northern-yuan (c1 on their side).
- missing: chuzan /ledger/10 1429 vassal_end cp=ming-dynasty. ming-dynasty has no 1429 chuzan-to-ryukyu-kingdom transfer of the tribute.
- missing: ryukyu-kingdom /ledger/2 1429 vassal_start cp=ming-dynasty. As above; ming /14 starts the ryukyu-kingdom vassalage in 1372.
- mismatch: later-jin-dynasty /ledger/0 1616 found cp=ming-dynasty. Names ming-dynasty; the land is jianzhou-jurchens' (its /7 dissolve 1616). ea-08 to add jianzhou-jurchens as predecessor and counterpart.

Matched rows: 50 (full list in history/notes/phase-b/reviews/ea-07.json).

## Problems

- Applied by the reviewer in ming-dynasty (re-validated, 0 errors, the same 8 Ruili warnings): counterparts of /ledger/16-18 to principality-of-liang-yunnan, /ledger/19 to duan-governors-of-dali, /ledger/31 and /45 to kara-del, /ledger/50 to portuguese-empire, /wars/0 belligerents to match; confidence of /ledger/47-48 lowered to 2. The author's counterparts_needing_dossiers entries qara-del and duan-family-of-dali are void: kara-del and duan-governors-of-dali exist.
- No dossier fails: no schema errors, no fabricated or mis-dated confidence-3 event among 40 spot-checked events, no unexplained factor-of-two area (only ming-dynasty has an infobox area). The fix verdicts carry author fixes (applied false) that are not blocking.
- For ea-08 (qing-dynasty, later-jin-dynasty): qing /15-/23 name southern-ming for the Three Feudatories (should be wu-sangui-s-zhou), qing /3 names 'Shun regime of Li Zicheng' (li-zicheng), qing /9 names 'Zhang Xianzhong's Xi regime...' at 1648 (xi-dynasty, 1646-47), qing has no 1645 Shun gains, no 1648 Guangdong loss, and has Fujian and Guangdong back only in 1680 (c1) against 1676-77 here; later-jin /0 should name jianzhou-jurchens (and list it as predecessor), later-jin /4 should name haixi-jurchens.
- For ia-02 (northern-yuan, four-oirats): northern-yuan records no losses to the Ming for 1369-1388; four-oirats dates its gain 1447 against the Ming's 1450. For ea-06 (tibet) and jk-02 (joseon): no Ming vassal events. For se-01 (first-toungoo-empire): the 1563-1597 Chinese Shan states are a Toungoo vassal there and a Ming loss/gain here.
- ming-dynasty used 26 pages against a budget of 9, southern-ming 8 against 5 (flagged by the author).
- Identity question for the orchestrator: Nurhaci's Jianzhou state (1583-1616) and the Later Jin are arguably one state renamed in 1616; the split is coherent as written (dissolve 1616 into later-jin-dynasty) but later-jin-dynasty does not acknowledge it.
- No page failed to load. The Hongwu Emperor page needed a second fetch: the Liaodong annexation sentence follows the 1388 Buir Lake sentence, so /ledger/25 (1388) stands.
