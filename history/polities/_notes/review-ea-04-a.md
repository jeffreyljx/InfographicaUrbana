# Review of batch ea-04-a (tang-dynasty, gao-kaidao)

Reviewer, 2026-10-19. Inputs: the author's brief, report and notes for ea-04-a; both dossiers; neighbour dossiers that exist (champa, uyghur-khaganate, balhae, goguryeo, turgesh, ganzhou-kingdom, yenisei-kyrgyz, tuyuhun, turks, western-gokturks, unified-silla, silla, kashmir, karkota-dynasty, turk-shahis, eastern-gokturks, sui-dynasty) and the ea-03 warlord, Tarim and Korean dossiers the Tang ledger names. Not yet written: tibetan-empire, nanzhao, tibetans, later-liang-dynasty (ea-04 parts), abbasid-caliphate, rashidun-caliphate.

Mechanical: both validate with --resolve, no errors, no warnings. Pages opened: Protectorate General to Pacify the West, Guiyi Circuit, Silla-Tang War, Transition from Sui to Tang, Gao Kaidao, Tang dynasty. Shape membership tested with tools/grid.py polity_cells at sample years (H3 res 5 cells, about 250 km2 each).

No fabricated or mis-dated event was found: 16 Tang events and all 4 Gao Kaidao events were confirmed on their pages. The Tang fails on keyframe/ledger consistency: several Cliopatria shapes are accepted as ok although they contradict the ledger, and three large gains are never undone. These faults come from the Phase A example and are in _example-tang-dynasty.json too.

## tang-dynasty: fail

Area: infobox 5400000 km2 (715), Cliopatria 4028116.2 km2, ratio 0.75, acknowledged True.

### Findings

- `/keyframe_review/16` (for the author): tang-dynasty_705 (705-749) is verdict ok and its note says 'The Beiting protectorate north of the Tianshan is inside the shape', but the shape lacks Beiting, the Turpan basin, Hami, Suyab and Liaodong, all of which the ledger holds as Tang in those years.
  - Evidence: shapes.csv bbox 73.08,17.77,122.71,42.76 (max lat 42.76 N; Beshbalik/Beiting is at 44.08 N, Gaochang 42.85 N, Turpan 42.94 N, Liaoyang 123.18 E). Cell test (tools/grid.py polity_cells, year 720): Turpan, Gaochang, Beshbalik, Hami, Liaoyang all absent. Ledger: Turfan gained 640 (/ledger/19), Dzungaria 657 (/ledger/25), lost only in 790 (/ledger/63); Goguryeo land gained 668 (/ledger/29), never lost. Anxi page: 'In 702 Wu Zetian set up the Beiting Protectorate in Ting Prefecture'.
  - Fix: Verdict adjust; correction = union of Cliopatria Tang 705 with Turfan-Hami and Dzungaria (Beiting) and with whatever Manchurian land the ledger still holds; delete the false sentence from the note; add the ledger losses that explain the eastern retreat (see /ledger/29).
- `/keyframe_review/13` (for the author): tang-dynasty_674 (674-681) correction removes only Baekje, but the shape also lacks the Tarim, the Turpan basin, Hami and Beiting while the ledger has the Tang holding the Tarim 673-677 and 679-687 and Turfan-Hami throughout.
  - Evidence: Cell diff 673->674: 5460 cells removed, median 41.2 N 84.1 E (Tarim, Dzungaria, Semirechye). Cell test at 678: Kuqa, Hotan, Turpan, Gaochang, Beshbalik, Hami absent. Ledger /ledger/33 673 gain Tarim, /ledger/37 679 gain Tarim; Anxi page: 'The Tang also captured Qiuci and established control over the Western Regions in the same year' (673) and 'In 679 the Tang general, Pei Xingjian, defeated Ashina Duzhi as well as the Tibetans'.
  - Fix: Correction = (Cliopatria Tang 674 minus Baekje) plus Turfan-Hami and the Beiting/Tingzhou area for the whole span, plus the Tarim Basin for 674-676 and 679-681 (or split the keyframe at 677 and 679).
- `/keyframe_review/14` (for the author): tang-dynasty_682 (682-691) is verdict ok, but the shape lacks the Tarim (the ledger holds it until the 686 withdrawal/687 loss) and the Turpan basin, Hami and Beiting (held throughout), and drops Pyongyang with no ledger event.
  - Evidence: Cell test at 685: Kuqa, Hotan, Turpan, Gaochang, Beshbalik, Hami, Pyongyang absent, Liaoyang present. Anxi page: 'In 686 Tang troops withdrew from the Four Garrisons'; 'In 687 the Tibetan Empire established control over the Western Regions' (/ledger/39).
  - Fix: Verdict adjust; correction adds the Tarim Basin for 682-686 and Turfan-Hami and Beiting for the span; either add Pyongyang back or add a dated loss of northern Korea.
- `/keyframe_review/15` (for the author): tang-dynasty_692 (692-704) is verdict ok but lacks the Turpan basin, Hami and Beiting, which the ledger holds as Tang.
  - Evidence: Cell test at 695: Kuqa and Hotan present; Turpan, Gaochang, Beshbalik, Hami absent. Shape bbox max lat 43.34 N (Beshbalik 44.08 N).
  - Fix: Verdict adjust; correction = Cliopatria Tang 692 plus Turfan-Hami and (from 702 at least) the Beiting area.
- `/ledger/29` (for the author): The 668 gain of Goguryeo's land (Manchuria and northern Korea) is never undone: the ledger has no loss of Pyongyang, Liaodong or Manchuria, so the map keeps them Tang to 907 while Balhae is founded there in 698.
  - Evidence: Cliopatria drops Pyongyang in the 682 shape and Liaodong in the 705 shape (cell diff 704->705: 1265 cells, about 320,000 km2, median 41.0 N 125.5 E); both keyframes are verdict ok with no event. Silla-Tang War page: 'The Tang were forced to relocate the seat of the Protectorate General to Pacify the East to ... Liaoyang' (676), then Xincheng (677), and 'Later, most of the land north of the Taedong River went to Balhae' (no year). balhae.json /ledger/0: 698 found, counterpart nobody. The 676 loss (/ledger/35) says the Tang kept the land north of the Taedong.
  - Fix: Add the losses with a page that dates them (Protectorate General to Pacify the East; Balhae): northern Korea around Pyongyang (c. 676-682) and Manchuria/Liaodong (c. 698-705, counterpart balhae or nobody), and make keyframes 682 and 705 consistent with them. Also say in the 666 keyframe correction that Goguryeo's land enters from 668 (Cliopatria adds it only in 674).
- `/ledger/25` (for the author): The 657 gain of Semirechye is never undone, and no Cliopatria Tang shape contains Suyab, so the corrections from 757 on drop Semirechye with no event.
  - Evidence: Anxi page (opened by the author): 'In 719 the Turgesh captured Suiye'; also 'The protectorate's seat was moved to Suyab' in 670. turgesh.json /ledger/1: 703 gain from tang-dynasty (Semirechye, Dzungaria, Chach). Cell test: Suyab absent from the Tang shapes at 672, 678, 695, 720 and 750.
  - Fix: Add a loss of Semirechye (Suyab) to turgesh, dated from the Anxi page (719, or 703 if a page gives it), and decide whether the 674-691 shapes need Suyab added (seat 670-, garrison 679-719).
- `/keyframe_review/23` (for the author): tang-dynasty_830 (830-849) is verdict ok, but the shape has lost Chengdu and western Sichuan (about 205,000 km2) while the note itself says Nanzhao 'withdrew the following year'; the 850 correction (/keyframe_review/24) also leaves Sichuan out.
  - Evidence: Cell diff 829->830: 812 cells removed, lat 26.1-36.3, lon 101.0-107.0, median 29.4 N 103.6 E; Chengdu, Ya'an, Leshan, Xichang, Kangding absent at 835 and 850, present at 829 and 862. Area 3.09 M -> 2.89 M km2. Nanzhao page quoted in the note: 'In 829, Wang Cuodian attacked Chengdu, but withdrew the following year'.
  - Fix: 830: verdict adjust, correction = union(Cliopatria Tang 830, Cliopatria Tang 829 within the Sichuan Basin); 850: add the same Sichuan land to its union. No ledger event is needed if no land changed hands.
- `/keyframe_review/1/correction` (for the author): The 623-625 correction adds only Jingzhou 200 km and Yangzhou 150 km, though the ledger gives the Tang Jiangxi and Guangdong (622, /ledger/11), the page says most of Xiao Xian's state was annexed in 621, and li-zitong-s-wu dissolves into the Tang with Zhejiang in 621.
  - Evidence: Transition page: 'Xiao ... surrendered, and most of his state was annexed by Tang'; xiao-xian-s-liang /ledger/4 dissolve 621 (Hubei, Hunan, ...); li-zitong-s-wu /ledger/3 dissolve 621 (Zhejiang). Keyframe and ledger disagree (rule 4).
  - Fix: Widen /ledger/7 to the xiao-xian-s-liang dissolve land, add Zhejiang to /ledger/8 (or a second gain), and make the 623 correction the union of the 621-622 gains (or the 626 shape minus Fu Gongshi's Song until 624).
- `/ledger (619, missing)` (for the author): No 619 loss of Shanxi to Liu Wuzhou, although the Transition page records it; the author's gaps list says 'page silent'.
  - Evidence: Transition page: 'Liu Wuzhou made a major attack south, taking over much of modern Shanxi, which Tang had controlled' and 'By summer 620, Li Shimin had defeated Liu'. liu-wuzhou-s-dingyang /ledger/1: 619 gain Taiyuan from tang-dynasty. The Tang found event (/ledger/1) includes Shanxi.
  - Fix: Add 619 loss, counterpart liu-wuzhou-s-dingyang, region Taiyuan 100 km or central Shanxi, confidence 2, source Transition_from_Sui_to_Tang; make the 620 gain (/ledger/3) cover the same land plus Datong.
- `/ledger/0` (for the author): The 618 Qin annexation has no month and sorts before the found event of June 618, though it came after it (xue-ju-s-qin dissolves in December 618).
  - Evidence: Transition page: Xue Ju 'died in early 618'; Li Shimin then 'defeated and killed Xue Rengao, annexing his Qin state into Tang' (no month). xue-ju-s-qin /ledger/4: 618-12 dissolve.
  - Fix: Give month 11 or 12 from a page that dates it (Xue Rengao) and move the event after /ledger/1.
- `/ledger/22` (for the author): Counterparts 'Tiele and Uyghur tribes (Yanran Protectorate)' (/ledger/22, /ledger/38) and 'Sogdian and Tokharistan principalities' (/ledger/27, /ledger/47) are names without a dossier and are not in counterparts_needing_dossiers; xueyantuo.json dissolves into the Tang in 646-08 and no Tang event names it.
  - Evidence: xueyantuo /ledger/3: 646-08 dissolve, counterpart tang-dynasty. Brief section 2.3: a counterpart without a dossier is an exception only when listed.
  - Fix: Use xueyantuo as the 647 counterpart or list both collective counterparts in counterparts_needing_dossiers (or as nobody with a note).
- `/ledger (803, 809, missing)` (for the author): champa.json records a 803 gain from and 809 loss to the Tang (Nghe An, Ha Tinh); the Tang ledger has neither.
  - Evidence: champa /ledger/12 and /ledger/13.
  - Fix: Open the Champa or Annan page and add the mirror loss (803) and gain (809), or record why not.
- `/ledger/74, /keyframe_review/26/correction, /keyframe_review/27/correction` (applied by reviewer): Yizhou was drawn as a bare coordinate (93.5 E 42.8 N) and listed in gazetteer_names_needed, but the gazetteer has it: place Hami, alt name Yizhou.
  - Evidence: data/gazetteer/places.jsonl: Hami, lon 93.515, lat 42.827, alt_names include 'Yizhou'; /ledger/67 already uses {place: Hami}.
  - Fix: Replaced {lon 93.5, lat 42.8, km 150} with {place: Hami, km 150} in the three places and corrected the ledger note; re-validated with --resolve (valid, 0 warnings).
- `/ledger/30/note` (applied by reviewer): The note said 'Cliopatria keeps the Tarim in the Tang shape until 681'; the 674-681 shape lacks it.
  - Evidence: Cell test at 678: Kuqa, Hotan absent; bbox west edge 87.68 E.
  - Fix: Now reads 'until 673 (its 674-681 shape lacks the Tarim, the Turpan basin and Beiting)'.

### Thin (for a gap-filler)

- `/ledger/11`: Lin Shihong's Chu (622) is confidence 1: no page gives its land at the Tang annexation. Try https://en.wikipedia.org/wiki/Lin_Shihong
- `/ledger/27`: 661 vassal tint west of the Pamirs is confidence 1, from the Cliopatria shape; no page dates the Anxi/Pacify-the-West jimi prefectures in Sogdia and Tokharistan. Try https://en.wikipedia.org/wiki/Protectorate_General_to_Pacify_the_West
- `/ledger/63`: End of the Beiting protectorate (790, confidence 1) and its land. Try https://en.wikipedia.org/wiki/Beiting_Protectorate
- `/ledger/59`: Dates for the fall of Ganzhou, Suzhou, Guazhou and Shazhou after Liangzhou (764); the whole Hexi Corridor is placed in 764. Try https://en.wikipedia.org/wiki/Hexi_Corridor
- `/ledger/29`: Dated losses of Pyongyang/northern Korea and Liaodong/Manchuria (Andong protectorate retreat, Balhae). Try https://en.wikipedia.org/wiki/Protectorate_General_to_Pacify_the_East
- `/ledger (803-809)`: Champa's capture and loss of the Hoan/Ai prefectures of Annan. Try https://en.wikipedia.org/wiki/Champa

### Spot checks

- `/ledger/19` confirmed, `/ledger/20` confirmed, `/ledger/30` confirmed, `/ledger/33` confirmed, `/ledger/36` confirmed, `/ledger/29` confirmed, `/ledger/32` confirmed, `/ledger/35` confirmed, `/ledger/66` confirmed, `/ledger/67` confirmed, `/ledger/74` confirmed, `/ledger/79` confirmed, `/ledger/12` confirmed, `/ledger/14` confirmed, `/ledger/15` confirmed, `/ledger/16` confirmed

## gao-kaidao: fail

Area: infobox 0 km2 (0), Cliopatria 81783 km2, ratio 0.0, acknowledged True.

### Findings

- `/ledger (620, 621, missing)` (for the author): The Tang ledger has gao-kaidao as a vassal 620-621 (/ledger/4 vassal_start, /ledger/5 vassal_end in tang-dynasty.json) but gao-kaidao.json has no mirror vassal_start/vassal_end with counterpart tang-dynasty; the notes say the pair lives only in the Tang ledger.
  - Evidence: Brief section 2.3: 'a vassal_start of X is a vassal_start in X's ledger with this state as counterpart'. Gao Kaidao page: submission in winter 620 (Gaozu made him commandant at Wei Prefecture, Prince of Beiping, gave him the Li surname); renewed rebellion in winter 621.
  - Fix: Add {year 620, type vassal_start, counterpart tang-dynasty, region {cliopatria: Gao Kaidao, year 623}, confidence 3, source Gao_Kaidao} and {year 621, type vassal_end, counterpart tang-dynasty, same region, confidence 3, source Gao_Kaidao}.

### Spot checks

- `/ledger/0` confirmed, `/ledger/1` confirmed, `/ledger/2` confirmed, `/ledger/3` confirmed

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| tang-dynasty 618 gain xue-ju-s-qin | xue-ju-s-qin 618 dissolve | matched | Tang event has no month; the Qin dissolve is 618-12. |
| tang-dynasty 618 found sui-dynasty | sui-dynasty 618 split | matched | sui 618-05 split and 617 loss of Guanzhong. |
| tang-dynasty 619 gain Li Gui (Liang of Hexi) |    | exception | No dossier; in the author's counterparts_needing_dossiers. |
| liu-wuzhou-s-dingyang 619 gain tang-dynasty | tang-dynasty  loss | missing | Tang lacks the 619 loss of Shanxi; the Transition page records it (fix on the Tang side). |
| tang-dynasty 620 gain liu-wuzhou-s-dingyang | liu-wuzhou-s-dingyang 620 dissolve | matched |  |
| tang-dynasty 620 vassal_start gao-kaidao | gao-kaidao  vassal_start | missing | gao-kaidao lacks the vassal pair (fix on the gao-kaidao side). |
| tang-dynasty 621 vassal_end gao-kaidao | gao-kaidao  vassal_end | missing | as above |
| tang-dynasty 621 gain wang-shichong-s-zheng | wang-shichong-s-zheng 621 dissolve | matched |  |
| tang-dynasty 621 gain xiao-xian-s-liang | xiao-xian-s-liang 621 dissolve | mismatch | Tang gains Jingzhou 200 km; the Liang dissolves with Hubei, Hunan and more. |
| tang-dynasty 621 gain li-zitong-s-wu | li-zitong-s-wu 620 loss | mismatch | Yangzhou matches (620 loss); Wu's 621 dissolve with Zhejiang has no Tang gain. |
| tang-dynasty 621 gain dou-jiande-s-xia | dou-jiande-s-xia 621 dissolve | matched | both 621-05 |
| dou-jiande-s-xia 619 gain tang-dynasty | tang-dynasty  loss | missing | Liyang (Hebi); the Transition page does not mention it; the author flagged it. |
| tang-dynasty 622 loss Liu Heita (Handong) |    | exception | No dossier; listed (ea-03). |
| tang-dynasty 622 gain lin-shihong-s-chu | lin-shihong-s-chu 622 dissolve | matched | Tang event confidence 1. |
| liang-shidu-s-liang 622 loss tang-dynasty | tang-dynasty  gain | missing | eastern city of Shuofang; small; Transition page silent. |
| du-fuwei-s-regime 620 dissolve tang-dynasty | tang-dynasty  gain | missing | Transition page: Du 'submitted to Tang and was created the Prince of Wu' (no year); not modelled in the Tang ledger. |
| tang-dynasty 624 gain Fu Gongshi (Song) |    | exception | No dossier; listed (ea-03). |
| tang-dynasty 624 gain gao-kaidao | gao-kaidao 624 loss | matched | plus gao-kaidao 624 dissolve |
| tang-dynasty 628 gain liang-shidu-s-liang | liang-shidu-s-liang 628 dissolve | matched |  |
| tang-dynasty 630 gain eastern-gokturks | eastern-gokturks 630 loss | matched |  |
| tang-dynasty 630 vassal_start eastern-gokturks | eastern-gokturks 630 gain | mismatch | eastern-gokturks models the Ordos settlement as a 630 gain from the Tang (and 639 gain/loss, 642 gain), no vassal_start; Tang models a vassal tint 630-645. One side must change (ia-01 or Tang). |
| tang-dynasty 645 vassal_end eastern-gokturks | eastern-gokturks 645 dissolve | matched |  |
| tang-dynasty 634 vassal_start tuyuhun | tuyuhun  vassal_start | missing | tuyuhun has only the 634-635 contest with the Tang; no vassal_start (ea-03 side). |
| tang-dynasty 663 vassal_end tuyuhun | tuyuhun 663 dissolve | matched | the relation ends with the state (dissolve to tibetan-empire). |
| tang-dynasty 640 gain kingdom-of-gaochang | kingdom-of-gaochang 640 dissolve | matched | both 640-09 |
| tang-dynasty 644 gain Karasahr (Tarim oasis kingdom) |    | exception | No dossier; listed. |
| xueyantuo 646 dissolve tang-dynasty | tang-dynasty 647 vassal_start | mismatch | Tang's 647 vassal_start names 'Tiele and Uyghur tribes', not xueyantuo. |
| tang-dynasty 648 gain western-gokturks | western-gokturks 648 loss | matched |  |
| tang-dynasty 648 gain kingdom-of-kucha | kingdom-of-kucha 648 dissolve | matched |  |
| tang-dynasty 657 gain western-gokturks | western-gokturks 657 loss | matched | plus 657 dissolve |
| tang-dynasty 660 gain baekje | baekje 660 dissolve | matched | baekje's dissolve has an empty counterpart (jk-02 side). |
| tang-dynasty 668 gain goguryeo | goguryeo 668 dissolve | matched | goguryeo's dissolve has an empty counterpart (jk-02 side). |
| tang-dynasty 671 loss silla | silla 671 gain | matched |  |
| tang-dynasty 676 loss silla | silla 676 gain | matched |  |
| turks 666 vassal_start tang-dynasty | tang-dynasty  vassal_start | mismatch | turks.json has Tang vassal spans 666-677 and 685-690, a 677 gain of Kucha from the Tang and 679/698 losses to it; the Tang ledger has none and gives Kucha 677 to tibetan-empire (Anxi page: 'In 677 the Tibetan Empire captured Qiuci'). Route to ia-01 and Tang. |
| tang-dynasty 682 vassal_end Tiele and Uyghur tribes (Yanran Protectorate) | second-turkic-khaganate 682 found | matched | second-turkic-khaganate founds from tang-dynasty in 682; counterpart names differ. |
| balhae 698 found nobody | tang-dynasty  loss | mismatch | Tang ledger never loses the Goguryeo land gained in 668, so it overlaps Balhae from 698 (fix on the Tang side). |
| turgesh 703 gain tang-dynasty | tang-dynasty  loss | missing | Semirechye/Dzungaria/Chach; the Anxi page has 'In 719 the Turgesh captured Suiye' (fix on the Tang side; years differ). |
| turgesh 736 loss tang-dynasty | tang-dynasty  gain | missing | Beshbalik; Tang ledger has no gain (Tang already holds Dzungaria in its own ledger). |
| turgesh 745 loss tang-dynasty | tang-dynasty  gain | missing | Tang ledger has no gain. |
| uyghur-khaganate 751 gain tang-dynasty | tang-dynasty  loss | missing | Turfan (uyghur side confidence 1); Tang keeps Turfan to 790. |
| champa 803 gain tang-dynasty | tang-dynasty  loss | missing | Nghe An, Ha Tinh; and champa 809 loss to tang with no Tang gain. |
| tang-dynasty 670 loss tibetan-empire | tibetan-empire   | exception | tibetan-empire not written yet (ea-04 part running in parallel); same for the 673-792 Tibet events, 763 occupation, 764-783 contest, 848 gain. |
| tang-dynasty 738 vassal_start nanzhao | nanzhao   | exception | nanzhao not written yet (ea-04); same for 751, 794, 863, 866, 902. |
| tang-dynasty 850 gain tibetans | tibetans   | exception | tibetans not written yet (ea-04); same for 851 and 861. |
| tang-dynasty 755 loss Yan (An Lushan) |    | exception | No dossier; listed (yan-an-lushan, ea-04-x); all Yan events 755-763. |
| tang-dynasty 881 loss Qi (Huang Chao) |    | exception | No dossier; listed (qi-huang-chao); 881 and 883. |
| tang-dynasty 851 vassal_start Guiyi Circuit (Zhang Yichao) |    | exception | No dossier; listed (guiyi-circuit); and the 907 vassal_end. |
| tang-dynasty 866 loss qocho-kingdom | qocho-kingdom  gain | missing | qocho-kingdom.json has no 866 gain of Xizhou, 876 gain of Yizhou or 904 loss of both (Guiyi page dates all three); fix on the qocho side. |
| tang-dynasty 907 dissolve later-liang-dynasty | later-liang-dynasty   | exception | later-liang-dynasty not written yet (ea-04 part). |
| sui-dynasty 617 loss gao-kaidao | gao-kaidao 619 gain | mismatch | two years apart: the Gao Kaidao page has the siege of Beiping from 617 and its capture around the new year 619; the Sui side should move to 618-619 or the Gao side record the 617 occupation. |

## Problems

- tibetan-empire, nanzhao, tibetans and later-liang-dynasty (ea-04 parts running in parallel) and abbasid-caliphate (me-08), rashidun-caliphate (me-07) have no dossier yet; their mirror checks are deferred (recorded as exceptions).
- Shape membership was tested with tools/grid.py polity_cells (local Cliopatria cell cache) at sample years and named places; numbers in the findings are cell counts at H3 resolution 5 (about 250 km2 per cell).
- The Manchuria, Semirechye, Turfan-Hami/Beiting and Sichuan-830 faults are inherited from the Phase A example polities/_example-tang-dynasty.json, which has the same ledger and keyframe verdicts for those years; the example should not be used as a reference for them.
- Reviewer edits applied to tang-dynasty.json (re-validated, read back): Hami place for Yizhou in /ledger/74 and /keyframe_review/26, /keyframe_review/27 corrections; /ledger/30 note. The author's gazetteer request 'Yizhou (Hami)' is withdrawn: the gazetteer already has Hami with alt name Yizhou.
- gao-kaidao fails on one finding only (the missing 620-621 vassal pair, two events verified on the Gao Kaidao page); everything else held.
