# Notes, batch ea-01-c (Shang to Warring States, part c): song, teng, wey, wu, xu, yan

Written 2026-10-18 by the Phase B research agent. All six dossiers validate (`validate_dossier.py`, errors 0). Years are the BC number negated (863 BC = -863), as in the other ea-01 dossiers.

## Read first

1. **Possible one-year offset in Cliopatria's BCE years.** Cliopatria's last Song year is -285 (pages: 286 BC), its last Warring States Yan year -223 (pages: 222 BC). If Cliopatria numbers years astronomically (1 BC = 0), every Cliopatria BCE year is one more than the BC number the pages give. The dossiers keep the page's BC number in ledger and wars and say so where it shows (Song keyframe 291, Yan keyframe 226). The orchestrator should settle this before the compiler matches events to shapes.
2. **Cliopatria's Yue row (-500..) overlaps Wu's core by 539 cells** from 500 to 481, although the Wu page has Yue conquering the capital in 482 and annexing Wu in 473. Yue's first shape should begin 482/473 (Yue group).
3. **Chu and Wu both claim Xu in 512.** chu.json has "gain xu 512" from the Chu page's list; the Xu page and the Spring and Autumn table give Wu, and Xu's exiles went to Chu. Wu's dossier takes the conquest.
4. WebFetch answers come from a summariser and often said "not on the page" for sentences that other agents quote from the same pages (Warring States period, Qi (state)). Thin pages here may be truncation, not silence; gap-fillers should try the pages with `offset`.

## yan (Yan (state), -1046..-202)
- Cliopatria 'Yan' (-750..-204) is one state with a gap (222 Qin conquest, 209 revival by Han Guang, 206 Zang Tu's Yan). One dossier; the 221-210 gap has no keyframe; the 222 end is a `loss`, the real end is the 202 `dissolve` (Zang Tu captured). Wikidata Q1472004 is shared with Former Yan (a CE state): different state.
- Keyframes (11, after the repair): new -1046 (the 750 shape carried back, without the State of Ji), 750 (adjust: same cut, to -651), new -650 (the 750 shape, Ji included), 404 (adjust: the 60-cell Ji block restored, to -301), new -300 (the 291 shape plus the block, to -292), 291 (adjust: block added; 226-222 replaced by the new keyframe 226, Liaodong only), new -209 (one year before Cliopatria's revived Yan), 208 (adjust: block added), 206 (adjust: Yan plus Liaodong after Zang Tu killed Han Guang), new 203-202.
- Unsettled: Han Guang's extent (page: 'the former Yan state'); Xiadu (undated, and outside every Cliopatria Yan shape); the end of the Qi occupation of 314 (312 on the Yan list, 311 on the King Zhao page, neither dates the revolt); the extent of the Donghu land and the dates of the Great Wall of Yan and the five commanderies ('At the turn of the 3rd century BC'); Zhao-Yan wars (undated). The 284 date comes from the King Min of Qi page, the 279 restoration from Warring States period.
- Overlap to fix elsewhere: 'liaodong' (ea-02, -206..-204) should end in 206 if the Zang Tu page is right; the Qi dossier has no 314 occupation of Yan (and no 312 end); the Gojoseon dossier (jk-02-a; Cliopatria row starts -197) must reach back to c. 300 for the Liaodong loss.
- Counterparts without dossiers: 'Ji (state)' (ea-01-x), 'Donghu' (ia-01). 'gojoseon' exists only for -197..-92.
- Pages: 11 opened in the first run against a budget of 5, nine more in the repair run (Yan, Ji x2, Zhao, King Zhao of Yan, Donghu people, Han Guang, Modu Chanyu, Xiadu).

### Repair run (reviewer verdict fail, 2026-10-18)
What I changed, finding by finding:
1. **Blocking: the Ji block.** Cliopatria's Yan shapes of 404, 291 and 208 all begin at 116.70E and drop 60 cells (about 10,400 km2, 115.9-117.1E, 38.6-40.1N) that the 750 shape holds, among them Ji (116.37E, 39.89N), the capital this dossier keeps to 227. Done as the reviewer asked: yan_-404, yan_-291 and yan_-208 are now `adjust` with the block added (union with minus(Yan 405, Yan 404)); the 'loss to Zhao 404' ledger line is deleted; the block is added to the regions of the 226 loss (and the Qin conquest war zone), the 209 gain, the successor land for Qin, and the 314 Qi occupation (the Qi invasion war zone too). The Zhao page (opened) has no Yan loss in 404: only 'annexing territory from the neighbouring states of Wei, Yan, and Qin', undated and unplaced, and no mention of Beijing, Ji or Zhuo; it dates Zhao's recognition to 403.
   **Cliopatria rows over the block (for those groups):** Zhao 404 holds 59 of the 60 cells, Zhongshan 366-301 59, Wei 291 58, Qin 222 58, Zhai 208 50, Dai 208 8, Xiongnu 208 1. They are wrong over Ji for the years Yan held it (to 226, and from 209). Zhongshan and Wei cannot be checked here; the Zhao page does say Zhao took some Yan land at an unknown date, so the rest of the block may have changed hands later.
2. **Not blocking: c. 300.** New keyframe yan_-300 (-300..-292) with the 291 shape plus the block; yan_-404 now applies 404-301. The Donghu people page gives 'In 300 BCE' (the Qin Kai page 'around 300 BC'); the Donghu-land event (ledger) now cites it, confidence 1 to 2 (year the page's, land my reading). Neither page gives the extent, the walls or the commanderies a date.
3. **Not blocking: Ji absorbed in the 7th century.** I took the reviewer's first option: the Ji circle (30 km round Beijing, cut to the 750 shape, 7 cells) is cut from yan_-1046 and yan_-750 and put back by the new keyframe yan_-650; the -650 gain has the same region. The Ji page ('Ji (state in modern Beijing)': 'At about the 7th century BC, Ji was absorbed by neighboring Yan, which made the City of Ji, its capital'; infobox 'c. 7th century BC') gives no year, so -650 remains a placeholder at confidence 1. I did not enlarge the shape for Liulihe: it lies about 11 km (one cell) outside the 750 shape, inside its bounding box (the earlier note said only 'inside the bbox').
Thin items:
- /ledger/3 (Zhao 404): no page; event deleted (see 1).
- /ledger/5 (Qi driven out): King Zhao of Yan page: 'Qi was unable to put down the rebellion ... and had to withdraw', no year; reign '311 BC until his death in 279'. Kept -312 (Yan page list), confidence 1, 311 in the note; the ruler strip note says the same.
- /ledger/7 (Donghu land): see 2.
- /ledger/13 (Han Guang): Han Guang page infobox 'King of Yan 209 BC - 206 BC', 'nominated by the people of Yan to be their king' after the uprising of 209, 'the former Yan state'. The gain moves from 208 to 209 (confidence 2) with a new one-year keyframe yan_-209; the Yan page's 207 is the Qin collapse. The 'capital Ji (Beijing)' entry for the revived Yan starts in 209.
- /ledger/14 (5 cells to the Xiongnu in 208): Modu Chanyu page names no Yan land (Yan appears only in 195, Lu Wan fleeing); the Donghu were 'defeated by 208'. Event deleted and the cells simply stay out of the shape (Cliopatria's); xiongnu.json needs no mirror.
- /ledger/1-2 (year of the absorption of Ji): Ji page, 'c. 7th century BC' only (see 3).
Where I disagree: nothing in the findings; two points I could not follow to the letter: Xiadu is not added to the shapes (the reviewer's fix does not ask for it and the Xiadu page, opened, gives Yi County, Baoding, 'one of the capitals of Yan during the Warring States period', 30 km2 and no dates; the coordinates on the page, 39.617N 116.056E, sit near Liulihe and not in Yi County, so I did not draw a circle from them), and the Donghu counterpart's years in my report now end 208 (Modu page: 'By 208 BCE, the Donghu had been defeated').

## song (Song (state), -1046..-286)
- Wikidata Q7462 is shared with Northern and Southern Song (960-1279 CE): different states, not merged.
- Cliopatria never gives Song the land of Cao (destroyed by Song 487, per the Cao page and cao.json); the corrected shapes add it. Cliopatria's 450 gain includes 15 Teng cells (Teng lived to 297, so they are removed) and 20 cells of its Xu row (page-silent, kept). Teng's annexation in 297 is added in a new keyframe.
- The 286 partition among Qi, Chu and Wei: no page divides the land; all three are listed as successors with the same shape.
- Page conflicts: royal title 328 (Song page) against 318 (King Kang page); Ticheng 369-329 (ruler list) against 355 (text).
- Not opened: the Battle of the Hong River page, Zheng-Song wars, Xue.

## teng (Teng (state), -1046..-297)
- The Teng page contradicts itself: lead/infobox 'conquered by Yue in 414 (1046-414 BC)', text and table 'annihilated by Song in 297'. The dossier ends in 297 and records Yue's 414 conquest as an occupation (counterpart yue). Switch to an end in 414 if the 414 reading is preferred.
- Cliopatria's Teng shape lies west of Tengzhou; a 25 km circle at Tengzhou is added. Cliopatria ends Teng in 451 (wrong on both readings). The page says Teng was Lu's vassal (undated): a `vassal_start` for the Lu dossier.

## wey (Wey (state), -1040..-209)
- Cliopatria's Wey shape (~5,800 km2) is about four times 'the county of Puyang', all that the page leaves Wey 'by 320'; shapes after 320 are replaced by Puyang (to 242) and, from 241, a circle at Yewang. The end is 209 (Shiji, infobox) with a modern 221 alternative.
- The Wey page says Wei made Wey a dependency (252) and Qin a nominal suzerain (after 241): `vassal_start` belongs in the Wei and Qin dossiers.
- Xing (destroyed by Wey in 635; 632 in the Spring and Autumn table) lay about 40 km outside Cliopatria's Wey shape; the page does not say how long Wey held it, so the shape is not extended. Needs a dossier or a name: 'xing'.
- The small Cliopatria moves (Jin 550 and 450, Wei 404, Zhao 366) are recorded at confidence 1. The ruler table on the page was garbled: no ruler strip.

## wu (Wu (state), -1100..-473)
- Wikidata Q274488 is shared with Eastern Wu (222-280 CE): different state. 'Wu rose to power in the 6th century', so Cliopatria's 193 k km2 shape for 750-551 is replaced by a Wuxi-Suzhou core up to 585; its shape is kept from 584 as unverified. The remnant shape from 480 is valid only to 474.
- The start year -1100 is a placeholder for 'the 12th century BC'. The location of Zhoulai (584) is the researcher's reading.
- Pages: 4 against a budget of 1-2 (Boju and Xu were needed for 506 and 512).

## xu (Xu (state), -1042..-512)
- The Xu page ends the state with the Wu conquest of 512 ('Hereby, Xu was extinguished') and mentions no Warring States Xu, so Cliopatria's rows 450, 404 and 291 are marked wrong (their corrections are intentionally empty: three 'region resolves to no cells' warnings). Cliopatria's second Xu sits on Teng and Zhu land.
- Cliopatria's first shape lies north of the Huai and misses the capital Sihong; the correction adds Sihong and Pizhou.
- No area on any page, so no sanity check was possible for any of the six states (no infobox gives an area).

## Gazetteer names wanted
Sihong, Pizhou, Tengzhou, Yewang, Zhaoge, Chuqiu, Liulihe, Xiadu (Yi County, Baoding; the page's own coordinate is doubtful), Qinyang (all replaced by coordinates in this batch); regions 'Huai River valley' (the river 'Huai' exists).

## Pages that failed
https://en.wikipedia.org/wiki/Battle_of_Jixi (URL_NOT_FOUND on the single try; the 284 events were taken from King Min of Qi and Warring States period instead).
