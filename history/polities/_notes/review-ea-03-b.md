# Review of batch ea-03-b (Three Kingdoms to Sui, part b)

Reviewer: adversarial reviewer, 2026-10-19. Dossiers: tuyuhun, cheng-han, former-zhao, former-liang, former-yan, later-zhao. Machine copy: history/notes/phase-b/reviews/ea-03-b.json.

All six validate (`--resolve`): no errors. Warnings: tuyuhun /wars/4 (Dafeichuan 670 after the 663 end); ran-wei and duan-qi counterparts with no dossier (listed by the author).

Context dossiers present and read: western-jin (Western and Eastern Jin), protectorate-of-the-western-regions, goguryeo, rouran-khaganate, gokturk-khaganate, eastern-gokturks, western-gokturks; also buyeo and kingdom-of-kucha (not in the context list, but counterparts). Not written yet (exception: their groups have not run): former-qin, western-qin, sui-dynasty, tang-dynasty, tibetan-empire, northern-wei and the other ea-03 parts.

Verdicts: cheng-han **fix** (fixed by the reviewer); tuyuhun, former-zhao, former-liang, former-yan, later-zhao **thin**. No fail: no fabricated event; every confidence-3 event spot-checked is on its page, except two that were misdated or overstated, which I fixed.

## Fixes applied by the reviewer (re-validated, read back)
- former-yan /ledger/8 and /ledger/9: Duan Qi (Shandong) conquest 357 -> **356**. Murong_Jun page: 'In 356 ... Murong Ke sieged [Guanggu], and after Duan's food supplies ran out, he was forced to surrender'; executed 357. /ledger/7 note corrected (the page has the 355 decision, not a 355-357 siege).
- former-zhao /ledger/6: split of the Later Zhao 318 -> **319** (Han-Zhao page: 'the Later Zhao founded by Shi Le in 319'; later-zhao founds in 319).
- former-zhao /ledger/11 and later-zhao /ledger/3: Henan 328, confidence 3 -> **2**. The Han-Zhao page says only that Liu Yao 'led his forces to secure the Henan region from Later Zhao'; later-zhao's quote 'Liu Yao secured Henan' was not the page's wording and has been restored.
- cheng-han /keyframe_review/2 and notes: 'Liang Province (Gansu)' corrected. The Li Xiong page puts Liang Province (梁州) in southern Shaanxi (Hanzhong) and warns it is not Liangzhou (涼州); it 'reverted several times between Jin and Cheng-Han rule' under Li Xiong, so the Hanzhong gain of 314 was held only on and off until 334.

## Open items for the author or a gap-filler (non-blocking)
### tuyuhun (22 shapes, 9-page budget used)
- Confidence-1 steps: 439 (+28,000 km2), 469 (+49,000), 476 (+160,000), 638 (-37,600), 641 (-160,600). They are honest but undated. The Tibetan Empire page has 'In 635-36, the Emperor attacked and defeated the Tuyuhun', which can date the southern loss. The 445 Northern Wei invasion (Muliyan's flight west; the page says the realm reached 'as far as Hotan') is missing.
- /wars/4 Dafeichuan (670) is outside the life; ruler Nuohebo runs to 672 (exile). End both at 663 or move them to notes.
- Area: there is no infobox area, only the 1,500 x 1,000 km extent, which is compared in /keyframe_review/12.
### cheng-han
- Ning Province extent after 333 (confidence 2). Dates of the Hanzhong reversals.
### former-zhao
- Capital Liting (113.2 E, 36.3 N, 305-308) is about 230 km from the only land drawn for 306-308 (100 km disc at Lishi). Add Liting to the 306 correction or flag the placement.
- 327: the Zhang Jun page says Liu Yin 'captured all Former Liang territory south of the Yellow River'. Write it as a gain/loss, not a contest (both dossiers).
- The 319 split hands over Hebei, Henan and Shandong, which the ledger never gains: Shi Le's 310-318 conquests under the Han are undated on the Han-Zhao page (try the Shi Le page).
- Area: 2.0 M km2 (316) against 647,071 (ratio 0.32). This is acknowledged in /keyframe_review/1 and resolved as an inflated infobox.
### former-liang
- No vassal pairs for its own submissions: Jin 317-323 (western-jin /ledger/22-23), Former Zhao 323-329 (former-zhao /ledger/8, 12), Later Zhao 330-351 (later-zhao /ledger/6, 13). The author wrote the suzerain side only (see problems: the schema wording supports that). Former Qin vassalage ('forced to submit to them as vassals', no year) is in neither ledger.
- 327 contest should be a loss to former-zhao; as written, /ledger/4 regains in 329 land the ledger never lost.
- The report says 353-376 are 'page silent', but the Former Liang page has: 'Several pro-Eastern Jin rebellions broke out in 356 and they once more lost all their territory south of the Yellow River' (after Chonghua 'attempted to reclaim' it). Add the 356 loss and note that the regain is undated.
- Kucha counterpart: kingdom-of-kucha.json now exists. Use the slug. protectorate-of-the-western-regions /ledger/16 records the same 335 submission as its own gain; reconcile the two (ea-02).
- Capital Guzang from 301 (page: Zhang Gui 'had already made Guzang his main base'); the 317 capital_move is a formalisation.
### former-yan
- No vassal pair with the Jin. western-jin carries 289 vassal_start and 352 vassal_end. The Former Yan page says Huang 'continued to consider himself as a Jin vassal', and the Murong Jun page dates the break to winter 352.
- Buyeo: buyeo.json has contest_start c. February 347 with former-yan, and the Former Yan page has 'in 346, they invaded Buyeo'. Add the contest pair.
- /wars/6 Fangtou has no zone while /ledger/15-16 draw a contest at Anyang. Add the zone.
- 344 Yuwen destruction has no gain. The 353 shape's Shanxi (182,000 km2) and Anhui/Jiangsu (66,000 km2) are unexplained; the author flagged both. goguryeo.json has no 342 event (route to jk-02).
### later-zhao
- Missing the 350 loss to former-yan that mirrors former-yan /ledger/3 and /ledger/5 (Murong Jun page: Jicheng in spring 350, Ji Province commanderies in winter 350).
- /ledger/1 counterpart 'Cao Ni' is neither a slug nor listed. List it under counterparts_needing_dossiers, or use western-jin if a page shows he held Qing for the Jin. western-jin has no 323 loss.
- Who took the Duan land in 338; Dai and Duan vassalage without years; lands on the Huai and Han.
- Area: 2.5 M km2 (329) against 661,773 for later-zhao_337 (ratio 0.26). This is acknowledged in /keyframe_review/3; the corrected extent is about 1.0 M km2.

## Cross-dossier mismatches to route
- western-jin (ea-03): its 304 loss to cheng-han already gives away Chongqing, Hanzhong and Ning, while Cheng-Han gains them in 310, 314 and 333; there is no 333 loss. Its 304 loss to former-zhao is the whole Cliopatria shape, against Former Zhao's 100 km disc. Its 317 confidence-1 loss to former-zhao has no gain on the other side. On Henan in 365 it loses only Luoyang.
- goguryeo (jk-02): no 342 submission to former-yan.
- kingdom-of-kucha / protectorate-of-the-western-regions (ea-02): the 335 Former Liang submission.
- buyeo (jk-02): the year of the Former Yan attack is 346 (Former Yan page) or c. February 347 (buyeo.json).

## Spot checks (pages opened)
Tuyuhun, Emperor_Yang_of_Sui, Murong_Fuyun, Western_Qin, Tibetan_Empire, Cheng-Han, Li_Xiong, Han-Zhao (twice), Former_Liang (twice), Zhang_Jun_(Former_Liang), Former_Yan, Murong_Jun (twice), Later_Zhao. Each check is listed in the JSON report: 36 events checked, 2 misdated (fixed) and 2 overstated (confidence lowered); the rest are confirmed.
