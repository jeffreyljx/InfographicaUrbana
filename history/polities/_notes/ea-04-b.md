# Notes for batch ea-04-b (Tibetan Empire, Nanzhao, Tibetans)

Written 2026-10-19 by the ea-04-b research agent. Dossiers: `polities/tibetan-empire.json` (45 events, 26 keyframes, 12 wars, 13 sources after the review), `polities/nanzhao.json` (21 events after the review, 10 keyframes, 6 wars, 5 sources), `polities/tibetans.json` (6 events, 12 keyframes, 4 wars, 7 sources) and one added dossier, `polities/dachanghe.json` (4 events, 1 keyframe, 2 sources; Nanzhao's direct successor, no Cliopatria row). All four validate with `--resolve`, 0 errors and 0 warnings. Each dossier's own `notes` field carries the per-state detail; this file is the summary.

## Method and page budget

- Every page was opened with WebFetch on 2026-10-19. Tibetan Empire (budget 9): Tibetan Empire, Protectorate General to Pacify the West (read three times for different years), Songtsen Gampo, Sino-Tibetan relations during the Tang dynasty (the "Tang-Tibet relations" article), Tang-Tibet Treaty Inscription, Guiyi Circuit, Uyghur Khaganate, List of emperors of Tibet, Ladakh. Nanzhao (budget 5): Nanzhao, Tianbao War, Tang-Nanzhao conflicts in Annan, Dali Kingdom, Pyu city-states. Tibetans (budget 5): Era of Fragmentation, History of Tibet, Guge, Mongol conquest of Tibet, plus Ladakh, Guiyi Circuit and the Protectorate page shared with the empire (so six to seven cited). The article Cliopatria names for the Tibetans row, "Tibetan people", was not opened.
- Pages that would not load (URL_NOT_FOUND on the exact URL, two variants tried, then a WebSearch for the title): Sino-Tibetan_Treaty_of_821%E2%80%93822, Sino-Tibetan_treaty_of_821/822, Sino-Tibetan_Treaty_of_821, and a Wikipedia full-text search URL. The WebSearch gave the real titles (Tang-Tibet Treaty Inscription; Sino-Tibetan relations during the Tang dynasty), which were then opened. The Seshat pages (cn_tibet_k, cn_nanzhao_k) were not opened.
- The WebFetch answers are summaries by a small model; quotes in notes are the sentences it returned. Where a request asked for something a page did not carry, the answer said so and the dossier records the page as silent (confidence 1) or leaves the event out.

## tibetan-empire (Cliopatria "Tibetan Empire" 623..849, 25 shapes)

- Dossier life 618..842 (infobox "Established: 618", "Disestablished: 842/848"). The 842-849 years of Cliopatria's last shape go to `tibetans` (keyframe `tibetans_842`).
- Verdicts: 15 ok, 10 adjust, 1 wrong. Corrections: 618 added as a new keyframe; 674 and 682 drop the northern Tarim, Dzungaria and Turfan that Cliopatria holds through the Tang-Tibetan swings of 670-692; 757 is wrong (Tarim, Hexi and Gansu already Tibetan in 757, pages date 763-792); 763-783 shapes are cut back to what the pages date; 793, 830, 840 lose Dzungaria and Gaochang (Uyghur 791-792). Corrected area 3.59 M km2 for 793-841 against the infobox 4.6 M km2 for c. 800 (ratio 0.78; Cliopatria's own 3.86 M km2 gives 0.84).
- Ledger covers the Sumpa and Zhangzhung conquests, the Tuyuhun (663), the Tarim swings (670, 673, 677, 679, 687, 692, then 763-792), Gilgit as a vassal (710-722, 737-747), the Stone City, the Nanzhao alliance (754-794), Chang'an (October 763), Hexi (764), the 783 treaty, Shazhou (786), Beiting and Gaochang (790-792) and the end (842). Four events are confidence 1 (628, 638, 656, 757; page silent).
- Disagreements between pages are listed in the dossier's notes and in the events (Tuyuhun 663/669/670; Khotan 665-670 or 792; Zhangzhung 634 or 645; Hexi 760 or 764; Shazhou 770s/780s/786; Langdarma 842 or 846; Chang'an October or 18 November 763).

## nanzhao (Cliopatria "Nanzhao" 741..910, 9 shapes)

- Dossier life 738..902 (the page: United the Six Zhao 737, Tang title 738; Zheng Maisi's coup 902). Cliopatria's 902-910 belongs to Dachanghe (new dossier, 902..937).
- Verdicts: 3 ok, 7 adjust (including one new keyframe for 738-740). The 830-860 shapes lose the Chengdu plain (the page: attacked Chengdu in 829 and withdrew), keep Yuesui (captured 756). The 755-865 lands in Guizhou, Guangxi and the Vietnamese marches have no page and are kept unverified until a single 866 loss event.
- Nothing on the pages gives an infobox area, so no area ratio was possible. The Pyu (upper Irrawaddy "by 763", Halin 832) are in a war entry with no zone because the page says nothing of Nanzhao holding the land afterwards.

## tibetans (Cliopatria "Tibetans" 850..1259, 11 shapes)

- A people, not a state: one plateau polygon, identical in all shapes 850-1249, over an age the pages describe as having "no central authority" (842-1247). Typed `state` for want of a fitting type; no capital (none on the pages); soft certainty. Life 842..1249; the 1250-1259 10-cell remnant is verdict wrong because Cliopatria's Mongol Empire takes the plateau in 1250.
- Events are only the losses on the edge (Shazhou and Guazhou 848, Ganzhou, Suzhou and Yizhou and the Tarim 850, Liangzhou 861) and the end (1249). The Ngari kingdom (c. 912), the division of c. 930 and Guge are not subtracted from the polygon because no dossier yet takes that land (it would become neutral grey); listed under counterparts needing dossiers.

## dachanghe (added; no Cliopatria row)

- Zheng Maisi's Great Changhe 902, renamed Datianxing 928 and Dayining 929, ending with Duan Siping's Dali Kingdom 937. One state with two `rename` events. Cliopatria leaves 911-946 empty between its Nanzhao row (to 910) and its Kingdom of Dali row (from 947). The shape is Nanzhao's 900 shape carried forward; no page gives any territory for these regimes.

## For the other groups

- tang-dynasty (ea-04-a): the Tang ledger's 851 gain of Xizhou (Gaochang) with counterpart `tibetans` is not supported here (Uyghurs took Gaochang in 792; the Guiyi page names no previous holder). Its Chang'an occupation is dated 18 November 763 where the Tang-Tibet relations page has October 763. Its 794 and 902 Nanzhao vassal events agree with this dossier (794, 902 are the same years).
- kashmir (sa-03): has 656, 661, 747 and 748 events against `tibetan-empire` that this dossier does not mirror (the Ladakh page says only that Baltistan and Ladakh were at the centre of the Tang-Tibet struggle, with no Kashmir dates).
- kamarupa-kingdom (sa-02): the 656 southern edge step is recorded here at confidence 1.
- uyghur-khaganate (ia-01): 790 contest_start, 792 gain and 808 contest_end are mirrored (790, 792, 808).
- kingdom-of-khotan (ia-01): its 851 "found" from `tibetan-empire` is after this dossier's end (842); the Tibetan hold of Khotan between 665-670 or 792 is a page disagreement, recorded.
- colours: no Tibetan family exists; `india` was used for tibetan-empire and tibetans, `southeast-asia` for nanzhao and dachanghe.

## Counterparts without a dossier

Guiyi Circuit (848-1036; suggested guiyi-circuit), Guge / Kyide Nyimagon's kingdom in Ngari (c. 912-1630; guge), Maryul / Ladakh (c. 930; maryul), Xiliangfu (Liangzhou, by 906), Zhangzhung (to 634/645), Lesser Bolu / Gilgit, Sumpa (to c. 627), the Pyu city-states (Sri Ksetra, Halin), the White and Black Mywa peoples.

## Gazetteer

All region names used resolve. Wanted for later precision: region Zhangzhung (Ngari, western Tibet); places Charklik (Ruoqiang, the Stone City; approximated by a 300 km disc around Qiemo intersected with the Tarim Basin), Songzhou (Songpan), Yuesui (Xichang area; Xichang used), Annan / Songping (Hanoi used), Halin; region Wakhan. The two Dali entries share aliases (Taihe, Yangjumie): the Yunnan one is reached as "Tali" (used in no region, the coordinate is in the capitals).

## Revision after the review (ea-04-b, 2026-10-19)

Reviewer: `polities/_notes/review-ea-04-b.md` (tibetan-empire fail, nanzhao fail, tibetans thin, dachanghe pass). tibetans and dachanghe were not touched. tibetan-empire and nanzhao validate with `--resolve`, 0 errors, 0 warnings. Pages re-opened with WebFetch on 2026-10-19: Guiyi Circuit, Nanzhao, Tianbao War, Tang-Nanzhao conflicts in Annan.

### tibetan-empire
- Applied by the reviewer and checked on the file: Tarim-only region of the 670, 673, 679, 687 and 692 swings (/ledger/8, 10, 12, 13, 14); counterpart `Yutian (Kingdom of Khotan)` for the 666 gain (/ledger/7; the Kingdom of Khotan dossier begins 851, so the earlier kingdom is a counterpart without a dossier); counterpart `tuyuhun` for the 638 step (/ledger/4; the Tuyuhun page is in sources[]); confidence 2 for the 790 gain (/ledger/36).
- Applied by me, the blocking finding: Shazhou and Guazhou (Dunhuang) came with the 764 gain and with the 768, 772 and 783 corrections, 22 years before the Guiyi Circuit page dates them (page re-read: 'Around the 770s or the 780s, Shazhou, otherwise known as Dunhuang, was occupied by the Tibetans'; 'From the beginning of Tibetan rule over Dunhuang (786)'; it gives no date for Guazhou, only the 848 uprising that took 'Shazhou and Guazhou from the Tibetans'). A 200 km disc around Dunhuang is now subtracted: /ledger/31 is `minus(intersect(...), union(Tibetan Empire 751, Dunhuang 200 km))` (the validator's minus takes two terms, so the two subtrahends are a union) and keyframes 20-22 are `minus(Tibetan Empire <year>, union(minus(Tarim+Dzungaria+Turfan-Hami, 751+Karashahr), Dunhuang 200 km))`. Checked with the gazetteer: a 60 km Dunhuang disc now has 0 cells in the 764 gain and in each correction (it had all 42 before), the 786 gain (/ledger/34) has its 479 cells, the corrections lose 334 cells (about 84,000 km2, 2.79 M to 2.71 M km2), the 764 gain is 442 cells. The 764 and 786 notes and the three correction notes say so. No disagreement with the reviewer; the Hexi cities between Liangzhou (764) and Shazhou (786) are still undated on every opened page.
- Routed to ea-04-a (not mine): tang-dynasty mirrors for the 717-749 Aksu/Stone City contest (/ledger/18, 22), the 747 Gilgit loss, the 749 Stone City loss, the 757 Gilgit gain (/ledger/26), the 763 Yanqi gain (/ledger/27) and the 786 Dunhuang gain (/ledger/34).
- Thin, still open (the pages tried so far are silent; the reviewer's suggested pages Sumpa, Songtsen Gampo, Kamarupa, Palola Shahis, Hexi Corridor and Ralpacan were not re-opened within this revision, whose scope was the failed findings): the 628, 638, 656 and 757 events stay confidence 1; the Hexi cities of 764-786; the courses of the 783 and 821/822 borders.

### nanzhao
- Applied, the blocking finding: six vassal events, 738 vassal_start tang-dynasty (c2), 751 vassal_end tang-dynasty (c2), 754 vassal_start tibetan-empire (c2), 794 vassal_end tibetan-empire (c3), 794 vassal_start tang-dynasty (c2), 902 vassal_end tang-dynasty (c2), each with Nanzhao's own shape of the year (741, 750, 755, 755, 755, 900) and a quote from the Nanzhao or Tianbao War page. They mirror tang-dynasty /ledger/51, 52, 71, 85 and tibetan-empire /ledger/25, 42. Convention question: the schema says the counterpart of a vassal event is the vassal, so in this dossier the counterpart is the suzerain and the region is Nanzhao itself (as the reviewer specified). A renderer must not read these as 'Nanzhao's vassals'; see the dossier's notes.
- Disagreements, with the pages: the Nanzhao page does not call the 738 relation tributary (Tang name and title 'Prince of Yunnan' only; 'amicable tributary relationship' is said of the later kingdom), so 738 is confidence 2; the Tianbao War page's fighting starts in 750 ('In 750, Geluofeng raised an army to capture 32 native counties of Yunnan') and the Nanzhao page has the Tang attack in 751, so the break may be 750; 751 is kept only to pair with tang-dynasty /ledger/52; the Tibetan Empire page has Nanzhao under Tibet from 750 where the Nanzhao page says 'By the end of 754'.
- Applied: the /ledger/11 note and the dossier notes now quote 'Prior to Li Hu's arrival, Nanzhao had already seized Bozhou' and 'Li Hu retook Songping on 21 July but Nanzhao's forces moved around and seized Yongzhou' instead of the phrase 'at various points', which the Annan page does not carry (re-read).
- Routed to ea-04-a: Annan 863-866 is occupation_start/occupation_end here and loss/gain in tang-dynasty (/ledger/79, 80), so the types disagree and tang's should become occupation events; tang-dynasty has no mirror for Nanzhao's 750 gain and contest, 755 and 756 gains, 829-830 Chengdu contest and 873-875 Sichuan occupation.
- Thin, still open: the 755 step (376,000 km2) and the Guizhou/Guangxi/Vietnamese lands of 755-865 (Geluofeng and Gao Pian pages not opened in this revision); the Pyu war still has no zone (Halin page not opened).

### Counterparts without a dossier (added to the list above)
Yutian / the Kingdom of Khotan before 851 (used as the name `Yutian (Kingdom of Khotan)`; kingdom-of-khotan, ia-01, starts in 851 and founds from tibetan-empire, which ended 842, so it should name `tibetans` or the Khotan loss of 850 should be mirrored there); Guiyi Circuit (848-1036, suggested guiyi-circuit, tang-dynasty and tibetans both name it), Guge, Maryul, Xiliangfu, Pyu city-states.
