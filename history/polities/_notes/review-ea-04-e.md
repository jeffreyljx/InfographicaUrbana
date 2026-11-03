# Review of batch ea-04-e (Later Tang, Later Shu, Later Han, Northern Han, Southern Tang)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/ea-04-e.json. No dossier was edited by the reviewer.

Mechanical: all five validate with 0 errors (`--resolve`); southern-tang has 3 warnings (counterpart `wuping-circuit` has no dossier; listed as needing one). Every Cliopatria shape has a verdict; new keyframes carry from/to/correction; capitals fall inside the shapes' bboxes. No infobox of the five pages gives an area (checked each), so no factor-of-two test is possible; the author says so. Judged against the page budget (all five: up to 3 shapes, 1-2 pages).

Verdicts: later-tang **fail**, later-shu **fail**, later-han **pass**, northern-han **thin**, southern-tang **thin**.

## The blocking finding (later-tang and later-shu)

The Qin, Feng, Cheng and Jie Prefectures (Xiongwu circuit) are moved from the Later Tang to the Later Shu in 934 (later-tang /ledger/11, later-shu /ledger/2, both confidence 1), with notes saying the page is silent on when they passed. The cited Meng Chang page dates it: "Around the new year 947, with a major Khitan Liao dynasty invasion force ... approaching the Later Jin capital Kaifeng, the Later Jin emperor Shi Chonggui... surrendered to Liao"; the Xiongwu governor He Chongjian refused to submit to Liao and "surrendered his circuit (including Qin, Jie, and Cheng Prefectures) to Later Shu"; "Later Shu forces also attacked Feng Prefecture ... Shi Fengjun ... also surrendered that prefecture to Later Shu." The region as drawn is about 40,464 km2; 30,854 km2 of it lies inside Cliopatria's Later Shu 936 shape.

Fixes (not applied: they rewrite corrections, beyond a small fix):

- later-tang: delete /ledger/11; /keyframe_review/4/correction, /ledger/13/region, /ledger/14/region and /identity/successors/0/land become `{"minus":[{"cliopatria":"Later Tang","year":926},{"minus":[{"cliopatria":"Later Shu","year":936},{"union":[{"place":"Tianshui","km":70},{"lon":105.7,"lat":33.7,"km":90}]}]}]}` (the four prefectures pass to the Later Jin in January 937).
- later-shu: replace /ledger/2 with a 947 gain (month 1 as sort key), counterpart later-jin, same region, confidence 2, Meng Chang page; /keyframe_review/0/correction and /keyframe_review/1 (verdict ok -> adjust) become `{"minus":[{"cliopatria":"Later Shu","year":936},{"union":[{"place":"Tianshui","km":70},{"lon":105.7,"lat":33.7,"km":90}]}]}` for 934-946. Optionally a war for the 947 seizure.
- later-tang also: add the 923 gain of Yun Prefecture from later-liang-dynasty (later-liang /ledger/9 has the loss). The Zhuangzong page, which the author opened, says "Li Siyuan was shortly thereafter able to capture Yun in a surprise attack" after the spring 923 proclamation. Region about 116.47 E 35.94 N, 50 km; confidence 2.

## Spot checks (WebFetch, 2026-10-19)

- later-tang: /ledger/1 (Later Liang page, 19 November 923), /ledger/3 and /ledger/5 (Zhuangzong page: Qi 924, Former Shu late 925), /ledger/9 and /ledger/10 (Meng Zhixiang page: 16 March 934; Shannan West and Wuding surrender, 'region south of the Qinling'), /ledger/13 (Later Tang infobox 11 January 937) confirmed. /ledger/11 mis-dated (above).
- later-shu: /ledger/0, /ledger/1, /ledger/3 (955), /ledger/4 (964, two fronts via Feng and Gui), /ledger/6 (reign end 23 February 965) confirmed; /ledger/2 mis-dated.
- later-han: /ledger/0, /ledger/2 (Taiyuan, 10 March 947), /ledger/3, /ledger/4 and /ledger/5 (1-2 January 951; de jure 13 February 951) confirmed.
- northern-han: /ledger/0 (951), /ledger/1 (979, siege from June, two months), rulers, /wars/0 (Liu Chong page: Gaoping 954) confirmed.
- southern-tang: /ledger/0, /ledger/1, /ledger/4, /ledger/5, /ledger/7, /ledger/10, /ledger/13, /ledger/14, /ledger/17 confirmed (October and 11 November 937; February 939; 2 October 945; Ma Xi'e vassal 951, deposed December 951; Bian Hao fled Tanzhou 1 December 952; Huainan 956-958; November 974; January 976).

## Thin items (for a gap-filler)

- later-tang: the Jingnan vassal pair 924-926 (confidence 1; try Gao_Jixing, Jingnan); the 936 loss drawn as all of Shanxi, though southern Shanxi stayed Later Tang to January 937 (a Hedong/Taiyuan region would be closer); Mingzong-era wars (Jingnan 927-928, Wang Du at Dingzhou 928-929, Xiazhou 933).
- later-shu: month of the 964 Song invasion; Later Shu's 947-948 Guanzhong intervention.
- later-han (pass; optional): month of the entry into Bian; the 948-949 rebellions.
- northern-han: no prefecture list; the 26,506 km2 outline (37.5-39.1 N) is 'unverified: page budget' and looks small for a realm that held Fen, Liao and Shi to the south and west; land results of Gaoping/954 and of the 968-976 Song campaigns; month of the 979 surrender.
- southern-tang: Qingyuan (Liu Congxiao's Quan and Zhang) as a Southern Tang vassal is on the page ("maintained de facto autonomy from the Southern Tang until forcible incorporation into the Song dynasty") and in the min dossier, but not in this ledger and not flagged: add a vassal pair with qingyuan-circuit (no year on the page). /ledger/15 Changzhou/Runzhou (confidence 1): the page puts "Changzhou and Runzhou were seized" right after "Quan Chu joined his suzerain in attacking the Southern Tang" (Wuyue, no year). Capitals: the infobox lists "Jinling, Guangling (briefly Nanchang)"; only Jinling is recorded.

## Cross-dossier matrix: what is missing elsewhere

- later-jin (ea-04): a 947 loss of Qin/Feng/Cheng/Jie to later-shu; its 937-946 shape should hold them.
- later-zhou (ea-01): the 955 gain of Qin, Feng, Cheng, Jie from later-shu (Meng Chang page).
- wuyue (ea-04): Changzhou/Runzhou 975. Its notes say the Southern Tang page mentions only the Jinling siege, but the page names the seizure.
- northern-song, liao-dynasty (ea-05, not run): Song conquests of later-shu 965, southern-tang 976, northern-han 979; the vassal relations of southern-tang 960-976 and northern-han 951-979.
- Matched: Later Liang 923, Qi 924, Former Shu 925, Later Shu 934 (found, Hanzhong), Later Jin 936/937, Later Han/Later Zhou/Northern Han 951, Southern Wu 937, Min 945, Chu 951, Later Zhou 956-958.

Needing dossiers: wuping-circuit (952-963), qingyuan-circuit (Quan and Zhang, about 945-978).
