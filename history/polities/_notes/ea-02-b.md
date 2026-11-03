# ea-02-b: notes (Qin and Han, part b: six Eighteen Kingdoms rows)

Written 2026-10-19. Dossiers: han-2, henan, jiaodong, jiujiang, liaodong, linjiang. All six validate (0 errors); `--resolve` gives no warnings for henan, jiaodong, jiujiang, liaodong, linjiang. han-2 shows nine "no verdict" warnings that are not its own (see below).

## Cross-cutting

- **Wikidata Q5349053 is not one state.** It is the Eighteen Kingdoms item shared by twelve Cliopatria rows (chang-shan, dai, han-2, henan, jiaodong, jibei, jiujiang, liaodong, linjiang, sai, yin, yong). Each row is a separate kingdom with its own king (Han Cheng, Shen Yang, Tian Fu, Ying Bu, Han Guang, Gong Ao), so none is merged; each keeps its own dossier. Slug `han-2` is "Hán" (Han Cheng); slug `han` is "Han" (Warring States, ea-01). Liu Bang's Hàn is `kingdom-of-han` (ea-02-a).
- **Validator quirk.** `slugify("Hán")` is `han`, so the validator counts the nine shapes of `han` (-404..-203) as unreviewed for `han-2` ("Cliopatria shape han_-404 has no verdict" ... `han_-203`). They belong to the ea-01 `han` dossier; harmless.
- **Pages.** The Eighteen Kingdoms page is thin (no capitals, no dates of fates, "Liaodong: Surrendered to Liu Bang" contradicted by the Zang Tu page). Dated facts came from the Timeline of the Chu-Han Contention, the Chu-Han Contention page, and each king's own article. The Chinese Wikipedia page for the eighteen kingdoms did not load (two URL spellings). Pages opened and found silent for the question asked: Zhang Liang (Han Cheng's capital), Luoyang (Henan's capital), Feast at Swan Goose Gate (list of kingdoms with capitals), Shen Yang (disambiguation), Chu-Han Contention (Linjiang), a Kiwix mirror of the old "18 Kingdoms" article (identical to the Eighteen Kingdoms table; not cited).
- **Year conflicts between pages** (the Timeline page tends to give 206 where others give 205): Hán Xin's conquest of Hán (Timeline 206; Zheng Chang, Xin of Han and Chu-Han 205), Shen Yang's surrender (Timeline 206; Shen Yang and Chu-Han 205), Tian Rong's killing of Tian Fu (Tian Rong page 205; Timeline 206, Chu-Han "six months after Qin's collapse"). The majority year is used and the other recorded in each note.
- **Cuts to Cliopatria's years.** All six rows run -206..-204. Henan is cut to 205, Jiaodong and Liaodong to 206 (Jiaodong and Liaodong land goes to Qi and Yan), Jiujiang stays to 204 (fall year uncertain: late 205 or 204). Two kingdoms outlive the row: Linjiang to 202 (Timeline: conquered by Liu Bang's forces) and Hán to 201 (Xin of Han: Hán Xin's vassal kingdom around Yingchuan, then Taiyuan, then defection).

## Matching entries other dossiers need (the orchestrator's cross-check list)

- **qi** (ea-01): gain of the Jiaodong cells in 206 (Tian Rong conquers Jiaodong and Jibei). Cliopatria's Qi shape (central and western Shandong) does not cover eastern Shandong. The jibei dossier already records its loss to qi in 206; qi has no matching gain from jibei or jiaodong.
- **yan** (ea-01): has the matching gain from liaodong in 206 (confidence 2). Cliopatria's Yan shape for 206-204 does not include the Liaodong Peninsula; the compiler must add those cells.
- **kingdom-of-han** (ea-02-a): no gain from henan in 205 (Shen Yang surrenders; Henan Commandery of the Hàn Empire), and no vassal_start for han-2 (Hán Xin as King of Hán from 205; the Xin of Han page calls it his "vassal kingdom").
- **han-dynasty** (another part): matching gain of linjiang in 202 and of the Hán lands in 201.
- **western-chu** (ea-02-a): its 203 gains from jiujiang and linjiang are dated by Cliopatria only. This part dates the Jiujiang fall to 204 (confidence 1, year from "late 205 BC" plus "months later"); it keeps Linjiang standing until 202, so Western Chu's 203 shape overlaps about half of Linjiang's outline for 203-202. Choose one in the compiler; the Timeline page says Linjiang still stood.
- **Kingdom of Huainan** (Ying Bu, 203-196 BC, made king by Liu Bang): no Cliopatria row, no dossier; needs one from the additions batch.

## Per state

- **han-2.** Capital in Han Cheng's reign is not on any page; Yangzhai comes from the Xin of Han page (for Hán Xin). The end in 201 and the keyframes for 203-201 rest on that one page; the relocation to Taiyuan is undated in the sentence quoted. Gazetteer: Yangzhai (Yuzhou, Henan) missing; Yingchuan Commandery not a region.
- **henan.** (Repair pass, 2026-10-19: see the section at the end.) Capital Luoyang is verified by the zh 申阳 page ('建都洛阳'). No month for anything. Cliopatria's Henan outline is displaced and not used.
- **jiaodong.** Capital Jimo comes from the page on the later Han-dynasty kingdom of that name; unverified for 206. Place and month of Tian Fu's death not on any page. Tian Fu = Tian Shi (Chu-Han page).
- **jiujiang.** Capital Liu (Lu'an) is the page's for the later Huainan, unverified for Jiujiang. Ying Bu's infobox tenure "207 - c.August 203" covers Jiujiang and Huainan together.
- **liaodong.** Wuzhong is named only as the place Han Guang was killed; the capital and its modern location (Ji County, Tianjin) are the researcher's, unverified. Gazetteer's alias "Wuzhong" points to Suzhou, the wrong place.
- **linjiang.** Who conquered Linjiang in 202 is not on the pages. The Gong Ao page's fief (Nan Commandery, northern Hubei) is smaller than the table's "western Hubei, northern Hunan", which the Cliopatria shape follows.

## Gazetteer names needed

Yangzhai (place, Yuzhou, Henan), Wuzhong (place, Ji County, Tianjin; the alias "Wuzhong" currently resolves to Suzhou), Jimo (ancient site, Pingdu, Shandong), Jiangling (place, Jingzhou, Hubei), Yingchuan (region, central Henan).

## Repair pass (2026-10-19): henan

The adversarial reviewer failed henan (blocking: the Cliopatria outline is in the wrong place). Pages reopened: zh Wikipedia 申阳, en Shen Yang (Eighteen Kingdoms), en Henan Commandery (new). Re-validated with --resolve: 0 errors, 0 warnings.

Changed:
- **keyframe_review/0 (henan_-206):** verdict adjust -> wrong. The Cliopatria Henan polygon lies on Henei (Zhaoge, Yin's seat), not on Luoyang; the earlier note 'with Luoyang inside' was false (the bbox contains Luoyang, the polygon does not; reviewer's polygon test: Luoyang is 60 km outside, 11 percent of a 90 km Luoyang disc lies in the shape against 95 percent of a 90 km Zhaoge disc). Correction: {"place": "Luoyang", "km": 90} with the zh text '建都洛阳 ... 其地成为河南郡', soft; years 206-205. The note says the Cliopatria Henan cells belong to Yin (yin, ea-02-c, not yet written).
- **ledger 0-2, wars[0].zones, identity predecessors/successors land:** the same Luoyang disc replaces the Cliopatria reference. Notes of ledger 0-2 now cite the zh 申阳 page ('建都洛阳'; '汉二年（前205年）十一月 ... 其地成为河南郡') and the Henan Commandery page ('in 205 BC, Sanchuan was renamed Henan', seat Luoyang).
- **certainty and notes:** reworded (soft; Luoyang disc is a proxy; capital now verified); sources[] gains the Henan Commandery page.
- Already applied by the reviewer and kept: capital source (zh 申阳), war name 'Chu-Han Contention'.

Where I did not take the reviewer's wording: the review suggests the region of 'Qin Sanchuan, the later Henan Commandery' and a possible 'north-west part of Cliopatria's Hán 206 shape'. The zh 申阳 page does not mention Sanchuan (only the Henan Commandery page links Sanchuan to Henan, and it does not mention Shen Yang), so the dossier quotes the two pages separately and does not assert that Shen Yang's kingdom equalled Qin's Sanchuan Commandery. The Hán-shape alternative is not used because the gazetteer resolves {"cliopatria": "Hán"} to the shapes of both `han` and `han-2` (slugify('Hán') == 'han'), so a reference to it matches two shapes in 206, Hán (86,684 km2) and the `han` row's han_-206 shape (Liu Bang's Han, 454,874 km2), and cannot isolate the Hán outline. The 90 km radius is the reviewer's figure; the Henan Commandery page lists 22 counties from Luoyang and Xingyang (east) and its western half became Hongnong in 113 BC, so the true extent may be larger than the disc. No page bounds the kingdom.

Still owed elsewhere (not done here, the verdicts fix/thin are not touched in this pass):
- **han-2:** its keyframes still hold Luoyang (89 percent of a Luoyang disc, 22 percent of the Hán shape); minus the same disc, plus the vassal events 205-201 (kingdom-of-han, then han-dynasty).
- **yin (ea-02-c):** Cliopatria's Henan polygon covers Zhaoge and Henei; Yin's own polygon sits in southern Hebei.
- **kingdom-of-han (ea-02-a):** a gain from henan in 205 (the Luoyang disc), mirrored by henan's loss.
- **qin-dynasty (ea-02-a):** henan, jiujiang and linjiang as successors.
