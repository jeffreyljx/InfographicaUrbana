# Review of batch ea-06-a (2026-10-24)

Reviewer: adversarial review, Phase B. One dossier: yuan-dynasty (Cliopatria 'Yuan Dynasty', 3 shapes, 1294-1374; drawn 1294-1368). Machine copy of these findings: history/notes/phase-b/reviews/ea-06-a.json.

## yuan-dynasty: FAIL

Mechanical checks: the validator, run with --resolve, reports no errors and no warnings (38 events, 3 keyframes all marked adjust, 4 wars, 5 sources). The family 'mongol' is a key in colours.json. The capital, Dadu, lies inside the shapes' bbox. The rulers run without gaps. The found event is at 1294 and the dissolve at 1368. Certainty covers the whole life.

Area: the Yuan dynasty infobox gives '1310: 11,000,000 km2'. The shape alive in 1310, yuan-dynasty_1294, is 14,249,991 km2, a ratio of 0.77. The keyframe note acknowledges this, and the author's quoted figures match what I read.

Spot checks (12 events; the pages were opened by the reviewer):
- Red Turban Rebellions confirms /ledger/4 (Qishui, September 1351), /5 (the Wuhan cities 1352), /8 (Gaoyou by the end of 1353), /11 (Hanyang 1356), /15 (Nanjing, 10 April 1356), /22 (Kaifeng, 11 June 1358), /27 (retreat, 10 September 1359) and /29 (Hangzhou and Prince of Wu, 1363).
- Gongmin of Goryeo confirms /13 (the northern provinces retaken in 1356).
- Phagmodrupa dynasty confirms /20 (Sakya superseded 1354-1358).
- Yuan dynasty confirms /33 (fall of Dadu, 14 September 1368).
- /7 is mis-dated for one component (see fix 6).

No event was fabricated. Every confidence-3 event I checked says on its page what its note claims.

### Blocking findings (back to the author)

1. **Ispah rebellion missing** (ledger, 1357 and 1366; wars). The ispah-rebellion dossier names yuan-dynasty in five events:
   - /2: found, March 1357, Quanzhou, confidence 3.
   - /0: gain of Putian, 1357.
   - /1 and /4: the 1357-1366 contest over Quanzhou, Putian and Fuzhou.
   - /5: dissolve, 1366, with Quanzhou and Putian returned to the Yuan.

   This ledger has no mirror for any of them, and the 1363 correction keeps Fujian whole. The ispah file was written before this dossier, and the author's report says every row naming yuan-dynasty is mirrored here, but ispah-rebellion is not in that list.

   Fix:
   - Add the Ispah rebellion page to sources[].
   - Add a loss in March 1357 (Quanzhou 50 km and Putian 40 km).
   - Add a contest pair for 1357-1366.
   - Add a gain in 1366.
   - Add a war 'Ispah rebellion' 1357-1366.
2. **Zhengmian (northern Burma to Tagaung) dropped** (keyframe_review/0 and /1 corrections, ledger/0, ledger in 1303, wars). The First Mongol invasion of Burma page says:
   - infobox: 'Northern Burma to Tagaung added to the Yuan dynasty';
   - 'The Mongols continued to occupy northern Burma to Tagaung as the province of Zhengmian (Cheng-Mien)';
   - 'on 4 April 1303, the Mongols abolished the province of Zhengmian (Cheng-Mien)' and 'evacuated Tagaung, and returned to Yunnan';
   - the second invasion of 1300-1301 failed.

   mongol-empire /86 (1284 gain, confidence 3) is never lost and passes to this dossier in 1293. But this dossier's found region, Cliopatria's 1294 shape (0.4 percent of Myanmar), leaves the land out, and no event marks 1303. myinsaing-kingdom /1 and /2 (the 1300-1303 contest, confidence 3) and /3 (the 1303 gain) also name yuan-dynasty, without a mirror here.

   Fix:
   - Union the mongol-empire /86 region into the found region and the 1294 and 1352 corrections.
   - Add a loss on 4 April 1303.
   - Add the war 'Second Mongol invasion of Burma' 1300-1303 with a contest pair, zone Singu and Male.

### Other findings (the author fixes them in the same pass)

3. fang-guozhen-s-regime /1 (1356 gain of Ningbo, Taizhou, Wenzhou and Shaoxing, confidence 1) has no mirror here. Add a 1356 loss of the same region.
4. wars/3 (Kaidu) lists ilkhanate and golden-horde as belligerents and leaves out ogedeid-ulus. Its zones are empty, while ogedeid-ulus /8 and /9 draw a contest against yuan-dynasty in the Altai and western Mongolia until 1301. Set the belligerents to yuan-dynasty, ogedeid-ulus and chagatai-khanate, set the zone to the Altai and Western Mongolia, and add contest_start 1294 and contest_end 1301 against ogedeid-ulus.
5. ledger/20 (1358 loss of Ü-Tsang to tibet) removes land that the 1294 and 1352 corrections already exclude: that land is the sakya-regime's vassal land, and /21 ends the tint. Delete /20 and tell the tibet author that tibet /1 should name sakya-regime, whose /7 is the real mirror. Or choose the other model, direct Yuan land, and drop the vassal pair.
6. In ledger/7, the Wuhan circle belongs in 1352. Red Turban Rebellions says the Tianwan 'briefly held Hanyang, Hankou, and Wuchang before being driven off in 1352'. Split it into a 1352 gain at confidence 2. tianwan /4 should match.
7. keyframe_review/2/correction cuts all of Anhui from 1363, while ledger/24 retook Bozhou and Yingzhou in 1359 and no later event loses them. Keep the two circles Yuan, or add the losing event.
8. The ainu dossier (/3 and /4) carries a Sakhalin contest against yuan-dynasty from 1294 to 1308. This dossier has no war or contest for it: add one, or say in the notes why not.

### Thin (for a gap-filler)

- The 1363 shape drops some Xinjiang cells, south-west Qinghai and west Sichuan with no event, which leaves Kham and Amdo without an owner 1363-1368. Page to try: Tibet under Yuan rule.
- The Ming conquests of Shandong (late 1367), Fujian (early 1368), and Guangdong and Guangxi (1368) are undated. Pages to try: Xu Da, Chen Youding, Liao Yongzhong.
- Events at confidence 1:
  - /3 (Fang Guozhen)
  - /6, /12, /16, /17 (Tianwan)
  - /10, /30 (Zhang Shicheng)
  - /18, /23, /24, /28 (Han Song; Chaghan Temür page)
  - /19, /25 (Hongwu Emperor)
  - /32 (Xu Da)
  - /36 (Basalawarmi)
  - /2 (Tibet under Yuan rule)

### Judgements accepted

- Starting the dossier in 1294 (the Cliopatria handover from mongol-empire).
- Ending in September 1368 and not drawing Cliopatria's years 1369-1374.
- Not recording the Chagatai, Golden Horde and Ilkhanate allegiance rows as vassalage (P1: 'their subservience was nominal').
- Not recording the tributaries Annam, Burma and Champa, whose tribute is undated.
- Treating 'Great Yuan' and 'Great Mongol State' as different states that share Q7313.

## Cross-dossier routing (not yuan-dynasty's faults)

- **goryeo (jk-02):** no vassal pair with mongol-empire or yuan-dynasty, although mongol-empire /70 has vassal_start goryeo in 1259 and yuan-dynasty has 1294-1356.
- **sakya-regime (ea-06-x):** no vassal pair with the Yuan.
- **tibet (ea-06-b):** /0, the 1354 found (confidence 3), names yuan-dynasty, but the land is the sakya-regime's in 1354. /1, the 1358 gain, should name sakya-regime.
- **tianwan and ming-xia (ea-06-x):** tianwan /9 is a vassal_start of ming-xia in 1357, while ming-xia begins in 1360, and the Yuan's 1357 loss of Sichuan to tianwan has no gain to mirror it.
- **Pre-1294 events naming yuan-dynasty, which begins in 1294:** they should name mongol-empire, which mirrors them already.
  - champa /29, /30
  - ngo-dynasty /23 to /26
  - pagan-kingdom /8 to /10
  - ogedeid-ulus /8 (1289)
- **myinsaing-kingdom (se-01):** /3, the Dry Zone gain of 1303, names yuan-dynasty, though its own note says the page does not show that the Yuan held the land.
