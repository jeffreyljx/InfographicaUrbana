# Review jk-02-c (silla, unified-silla, balhae, hubaekje, taebong, goryeo)

Reviewer, 2026-10-19. Validator: 0 errors in all six; warnings only for Naju, Jinju (gazetteer) and the `jurchens` slug. Geometry checks were run on the H3 grid (tools/gazetteer.py, cells of 252.9 km2, so grid areas run higher than shapes.csv). No page has an infobox area (Silla, Unified Silla, Balhae, Later Baekje, Taebong and Goryeo all checked), and the notes say so; no area comparison is possible.

Convention: the schema defines vassal_start/vassal_end as suzerain-side only (the counterpart is the vassal). So Goryeo's vassalage to Liao/Jin/Yuan and Silla's to Goguryeo (400) need no event in the vassal's ledger, and Tamna needs no mirror. That follows the jk-02-b review.

## Verdicts
- silla: **fail**. It has no mirror for goguryeo's gains from silla in 468 and 489, and its 551 region double-claims Gyeonggi.
- unified-silla: **fail**. It has no 901 loss to taebong, so 35,659 km2 is drawn twice for 901-904. The Pyongyang part of the 905 loss is missing, and 11,128 km2 in the north drops out in 905 with no event.
- balhae: **thin**. The 705, 741 (+206,000 km2) and 825 (+152,000 km2) steps are confidence-1 bridges. One misquote was fixed by the reviewer.
- hubaekje: **fix** (fixed by the reviewer). Two misquoted Jinju sentences were corrected. Everything else held.
- taebong: **fix** (fixed by the reviewer). Two misquotes were corrected. The counterpart of the 905 Pyongyang gain changed from nobody to unified-silla.
- goryeo: **fail**. Naju is nobody's from 918 to 935. The 1270 and 1290 Pyongan region is about twice the land the keyframes hold. The reviewer lowered the 1108 confidence from 3 to 2.

## silla
Spot checks, all confirmed:
- 551: Jinheung page, 'allied with Baekje', 'splitting the conquered territory equally'.
- 553: Silla page, 'wrested control of the entire central western Korea region from Paekche in 553'.
- 662: Tamna infobox, 'Tributary state of Silla (662-925)'.
- 671: Silla-Tang War page, 'In 671, Silla drove Tang forces out of most of Baekje's former territory'.
- 676: Silla-Tang War page, 'In 676, Silla took all the territory south of the Taedong River', Gibeolpo in November.

Findings:
1. (blocking) The ledger has no loss mirroring goguryeo /ledger/30 (468 gain from silla, intersect Gangwon with Silla@468, 3,541 km2 on the grid) or goguryeo /ledger/33 (489 gain from silla, intersect North Gyeongsang with Silla@489, 23,267 km2). The 489 region covers nearly the whole silla_378 outline, Gyeongju included. Cliopatria's Goguryeo 480 shape does not overlap Silla's, so the two dossiers now draw the same land. The author's notes say these losses 'are in the Goguryeo dossier', but rule 3 needs both sides. Fix: agree a narrow region with the goguryeo author (the 489 'seven walled cities' on the northern frontier, not the province). Then add losses at 468 and 489, plus the regain no later than the 551 campaign, and make silla_378 'adjust'. Or, if no page supports Goguryeo holding Silla land, say so in the notes and have goguryeo narrow or drop the events. The goguryeo side is routed in the cross-checks.
2. (blocking) /ledger/3/region: the 551 gain from goguryeo is the whole Goguryeo 554-to-555 step (66,260 km2 on the grid). That includes the Gyeonggi land (14,415 km2) that baekje /ledger/14 gains from goguryeo in 551 and that silla /ledger/4 takes from baekje in 553. The note itself says Silla's half excludes the Seoul region. Fix: `{"minus": [{"minus": [{"cliopatria": "Goguryeo", "year": 554}, {"cliopatria": "Goguryeo", "year": 555}]}, {"region": "Gyeonggi"}], "text": ...}`.
3. /ledger/7/note and /keyframe_review/4/note: 'Munmu's forces attacked Baekje, and Kim Yu-sin, aided by Tang forces, conquered it' is not the page's wording. The Unified Silla page reads 'In 660, King Munmu ordered his armies to attack Baekje' and 'General Kim Yu-sin, aided by Tang forces, defeated General Gyebaek and conquered Baekje'.
4. Notes: the author says the 400-468 vassalage is on no page opened. The Silla page has 'after King Gwanggaeto's unification campaign, Silla lost its status as a sovereign country becoming a vassal of Goguryeo'. No event is needed (suzerain-side), but correct the notes.
5. Mismatch: goguryeo puts Silla's Han valley gain in 553, and silla puts it in 551 (the Jinheung page supports 551). This was already flagged by the author. Routed to goguryeo.

Thin:
- silla_555's east-coast reach to 40.1 N (7,600 km2) is unverified.
- The 378 found event is a confidence-1 bridge.

## unified-silla
Spot checks, all confirmed:
- 892: Gyeon Hwon page, 'In 892, Kyŏn Hwŏn seized the cities of Wansanju and Mujinju'.
- 905: Gungye page. Pyongyang falls 'in the same year' as the 905 Cheorwon move; 'almost two-thirds' is undated.
- 925: Tamna infobox.
- 928: Gyeon Hwon page, 'One year later he took over the city of Jinju from Silla'.
- 935: Unified Silla page, 'Handover to the Goryeo: 935'.

Findings:
1. (blocking) taebong /ledger/0, the 901 found event with counterpart unified-silla, takes a 100 km circle round Kaesong. That circle (35,659 km2) lies wholly inside unified-silla_892, which the dossier keeps 'valid 892-904', and no 901 loss exists. Fix:
   - Add a 901 loss to taebong with region `{"place": "Kaesong", "km": 100}`, source the Gungye page ('proclaim himself king of Later Goguryeo in 901'), confidence 2.
   - Add a keyframe unified-silla_901 (901-904) of minus(Unified Silla@892, Jeju, Kaesong 100 km).
   - Make unified-silla_892 valid 892-900.
2. (blocking) /ledger/3/region subtracts the Pyongyang 100 km circle. But 24,784 km2 of that circle lies inside unified-silla_892, and taebong /ledger/3 (counterpart now unified-silla, reviewer) takes it in 905. Fix: region minus(Taebong@911, Kaesong 100 km), so that Pyongyang is no longer subtracted.
3. 11,128 km2 (grid) between 39.4 and 40.1 N (south Hamgyong-namdo and north-east South Pyongan) is in Unified Silla 892, but in neither Unified Silla 911 nor Taebong 911. unified-silla_905 drops it with no event. The unified-silla_682 note already says the outline runs 'a little beyond' the Taedong-to-East-Korea-Bay line. Fix: either cut that strip from unified-silla_682 and _892, or add a 905 loss to nobody saying why.
4. /ledger/5/note and /keyframe_review/4/note: 'took Jinju one year after' is not on the page, which reads 'One year later he took over the city of Jinju from Silla'.

Thin:
- The 905 loss (/ledger/3) and the 682 found event (/ledger/0) are confidence 1.

## balhae
Spot checks, all confirmed (Balhae page):
- 698: 'Parhae was founded in 698 by Tae Choyŏng'.
- Capitals 742, 755, 785, 794.
- 818: 'In 818-820, he also invaded Liaodong and parts of Silla'. The Seon page has 'Southwest Little Goguryeo in Liaodong was absorbed into Balhae', undated.
- 926: 'In 926, the Khitans laid siege to the Parhae capital Shangjing/Sanggyeong and forced their surrender'.

On the Liaodong correction (balhae_741 minus Liaodong until 818): the pages support it. Cliopatria's Tang shapes for 741-817 do not cover that land (0 cells), so it is unclaimed until a little-goguryeo dossier exists.

Fixes:
1. (applied) /keyframe_review/1/note quoted 'roughly modern Northeast China, northern Korea, and the southeastern Russian Far East'. The page reads 'At its greatest extent it corresponded to what is today Northeast China, the northern half of the Korean Peninsula'.
2. (advisory) /identity/predecessors is empty, although goguryeo's identity.successors lists balhae. Add goguryeo, or have the goguryeo author drop balhae.
3. (advisory, routed to ea-04) The /ledger/0 counterpart is nobody, but Cliopatria's Tang shape for 698-704 covers 19,979 km2 (grid) of the Dunhua 150 km circle, and the Tang example has no 698 loss.

Thin:
- 705: page to try https://en.wikipedia.org/wiki/Go_of_Balhae
- 741: page to try https://en.wikipedia.org/wiki/Mun_of_Balhae
- 825: page to try https://en.wikipedia.org/wiki/Heishui_Mohe

## hubaekje
Spot checks, all confirmed:
- 892: Gyeon Hwon page.
- 900: 'established his capital at Wansanju in 900'.
- 910: Naju, and the failed ten-day siege.
- 928: Jinju.
- 936: Later Baekje page, 'Later Paekche thus finally fell in 936'.

Fixes (applied): the Jinju misquotes in /ledger/4/note and /keyframe_review/2/note now quote 'One year later he took over the city of Jinju from Silla'. Nothing else broke: mirrors with unified-silla (892, 928), taebong (910) and goryeo (927/930 contest, 936) all match.

## taebong
Spot checks, all confirmed (Taebong page unless noted):
- 901: 'a state established by Kung Ye on the Korean Peninsula in 901'.
- 904: Majin, 'After a suggestion by Ajitae'.
- 905: 'transferred the capital from Songak to Cheorwon in 905'.
- 905: Pyongyang (Gungye page).
- 911: 'eventually to T'aebong in 911'.
- 918: the four generals.

Fixes (applied):
- /ledger/0/note: 'first called Goryeo, after the official name of Goguryeo' replaced by the page's 'The state's initial name was Goryeo'. The 901 quote is body text, not infobox.
- /ledger/3/counterpart: nobody changed to unified-silla, because two-thirds of the Pyongyang circle lies in the Unified Silla 892 outline that unified-silla keeps to 904.

Thin, by design (1 shape, budget 1-2 pages, 3 used):
- /ledger/4: the 'two-thirds' gain is confidence 1.
- taebong_901 is a Kaesong circle, although the Gungye page has the Myeongju (Gangneung) and Paeseo aristocrats submitting before 901. Page to try https://en.wikipedia.org/wiki/Later_Three_Kingdoms_of_Korea

## goryeo
Spot checks, all confirmed unless noted:
- 935 and 936: Goryeo page ('peaceful annexation of Later Silla in 935', '87,500 soldiers').
- 938: Tamna infobox, 'Vassal state of Goryeo (938–1105)'.
- 1031: Khitan War page, 'the Liao ceded territory around the Yalu to Goryeo'.
- 1108: year confirmed by the Goryeo page ('handed back to the Jurchens'). The Yun Gwan page names only Hamheung, so confidence 3 became 2 (applied).
- 1231: '26 August 1231 ... crossed the Yalu and surrounded Hamsin-chin (Uiju)'.
- 1294: 'Goryeo regained formal control of Dongnyeong in 1290 and Jeju in 1294'.
- 1356: 'By 1356 Goryeo under King Gongmin regained its lost northern territories such as the Ssangseong Prefecture'.
- 1014: the page dates the Yalu bridge to 1014 and the attacks to 1015-1017, but not the Poju loss; the note says so.

Findings:
1. (blocking) goryeo_918 (918-921, Taebong@911) and goryeo_922 ('ok') leave out Naju, which taebong_911 holds for 911-917 (Gyeon Hwon page, 910). hubaekje_910 and hubaekje_926 keep Naju out until 936, so Naju is nobody's from 918 to 935. Fix: union `{"place": "Naju", "km": 25}` into goryeo_918, make goryeo_922 'adjust' with the same union, and add the Gyeon Hwon page to sources.
2. (blocking) /ledger/21 (1270 loss) and /ledger/23 (1290 gain) use `{"region": "Pyongan"}`, which is 63,984 km2 on the grid, Chagang (23,773) and South Pyongan included. Goryeo's keyframes held only 29,842 km2 of it: 11,633 km2 of Cliopatria 1227 plus North Pyongan. The 1290 gain therefore hands Goryeo about 34,000 km2 that goryeo_1290 does not draw. Fix: in both events, region `{"intersect": [{"region": "Pyongan"}, {"union": [{"cliopatria": "Goryeo", "year": 1227}, {"admin1": "P'yŏngan-bukto", "country": "North Korea"}]}]}`.
3. (advisory) /ledger/7: the 993 gain has counterpart nobody. The page says the land 'had been occupied by Jurchen tribes', and Cliopatria's Liao shape holds 17,956 of North Pyongan's 18,209 grid km2 for 993-1125 (Great Jin 1130 and Mongol 1260 too). Use counterpart jurchens or say why nobody. The suzerain dossiers must remove North Pyongan (routed).
4. (advisory) /identity/predecessors lists only taebong. unified-silla and hubaekje both name goryeo as successor, so add them, with the land of 935 and 936.
5. (advisory) /ledger/18: the 1258 loss of Hamgyong-namdo removes 1 grid cell, because the keyframes never reach north of 39.45 N. The Ssangseong annexation is therefore invisible. Either add the Hwaju strip to goryeo_993 through goryeo_1227 or say so in the note.

Thin:
- goryeo_1356 uses Cliopatria 1363 from 1356. Beyond goryeo_1290 plus Hamgyong-namdo, it adds 43,752 km2 (grid) in Chagang, Ryanggang, North Hamgyong and north South Pyongan with no ledger event; the note admits low confidence. Pages to try https://en.wikipedia.org/wiki/Gongmin_of_Goryeo and https://en.wikipedia.org/wiki/Ssangseong_Prefecture
- The Nine Fortresses' extent, and Goryeo-Jurchen War (page would not load).

## Cross-dossier matrix (territorial events)
Matched:
- silla/gaya 532, 562; silla/baekje 553; silla 681 / unified-silla 682.
- unified-silla/hubaekje 892, 928; unified-silla/taebong 905 (the land still differs, see finding 2); unified-silla 935 / goryeo 935.
- taebong/hubaekje 910; taebong 918 / goryeo 918; goryeo/hubaekje 936.
- silla 676 / the Tang example's 676 loss.

Missing:
- goguryeo 468 and 489 gains from silla (no silla loss).
- taebong 901 found from unified-silla (no unified-silla loss).

Mismatch:
- silla 551 against goguryeo 553 (Han valley). Both regions include Gyeonggi, which Baekje holds 551-553.
- taebong 905 Pyongyang against unified-silla 905 (land).

Exceptions:
- Counterparts whose groups have not run: tang-dynasty (ea-04: silla 671, balhae 698), liao-dynasty (ea-05: goryeo 993 overlap, 1014, 1031; balhae 926), mongol-empire (ia-02: goryeo 1258, 1270, 1290), yuan-dynasty (ea-06: 1356), joseon (1392).
- Counterparts without a dossier: jurchens, little-goguryeo, dongdan.
- Vassal events are suzerain-side only; Baekje had dissolved before the 660 occupation.
