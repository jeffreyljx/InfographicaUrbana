# Review of batch eu-13-b (Italy, part b: the split of Cliopatria's Kingdom of Italy row)

Reviewer: Phase B adversarial reviewer, 2026-10-25. Dossiers: kingdom-of-the-lombards (587-774), kingdom-of-italy-medieval (855-961), kingdom-of-italy (1861-1946). Validator: 0 errors for all three. Spot checks: 7 + 10 + 14 events on 14 pages (all of them opened by the author except Battle_of_Caporetto). No confidence-3 event failed; two confidence-1 events were mis-dated and fixed in place by the reviewer.

Verdict meanings in this run: fix = fixed by the reviewer; thin = valid and honest, gaps for a gap-filler (and the unapplied fixes listed, none blocking); fail = back to the author.

## kingdom-of-the-lombards: thin

Area: infobox None (None) vs Cliopatria 219714, ratio None. Kingdom of the Lombards infobox gives no area (confirmed); the keyframe notes say so. Largest shape 755: 219,714 km2.

### Findings

- `/keyframe_review/8` (to do): The 692 shape adds 20 Apulian cells and 4 in Campania/Basilicata (172,091 to 179,820 km2) and the ledger holds no event at all between the 661 and 705 keyframes; the author's report (gaps) says confidence-1 events cover 692, but none exists.
  - Evidence: Ledger years run 645 -> 727 with nothing in 661-726; shapes.csv area 172,091 (661) vs 179,820 (692). The Kingdom of the Lombards page says 'southern Apulia' was 'never under Lombard domination'.
  - Fix: Add a 692 gain (counterpart byzantine-empire, region {minus: [Kingdom of Italy 692, Kingdom of Italy 661]}, confidence 1, note that Benevento's conquests are undated on the pages) or mark keyframe 8 adjust and remove the eastern Apulian cells; correct the report's gaps entry.
- `/keyframe_review/12` (to do): Verdict 'ok' for the 750 shape although its own note says the shape is a year early: it returns Spoleto and Benevento in 750 while the ledger keeps them out until 751 (/ledger/16, /ledger/17).
  - Evidence: Aistulf page (quoted in the note): Spoleto taken under direct control 'in the late spring or summer 751'.
  - Fix: Mark the 750 keyframe adjust with a correction that gives the 741 outline for 750 (text: years only), or move /ledger/16 and /ledger/17 to 750 with a page that dates it.
- `/identity/predecessors/0` (to do): Rule 2 (one colour for life): the Lombard kingdom 568-774 is one state cut in two dossiers at Cliopatria's 586/587 row change; lombards (480-586) names 'kingdom-of-italy' as its successor and its ledger 13 (586 dissolve) points at kingdom-of-italy, and its successor note asks for Lombard Italy 587-774 to be merged into the lombards dossier.
  - Evidence: lombards.json identity.successors[0]: 'One state to 774 on the pages ... Lombard Italy 587-774 belongs with this one.' Kingdom of the Lombards page infobox: 'Lombard migration: 568' to 'Frankish invasion: 774'.
  - Fix: No change in this dossier if the hand-over pattern (as eastern-roman-empire -> byzantine-empire) is accepted: the colour agent must give kingdom-of-the-lombards the lombards colour, and the lombards dossier must repoint successors[0] and ledger 13 from kingdom-of-italy to kingdom-of-the-lombards. Otherwise merge into lombards (orchestrator's call).

### Gaps for a gap-filler

- `/keyframe_review/8`: A dated cause for the 692 Apulian cells (Benevento's conquests of Taranto/Brindisi, if any) and whether 'southern Apulia' belongs in the shape (try https://en.wikipedia.org/wiki/Duchy_of_Benevento)
- `/ledger/4`: 628 gain (+8 cells Campania/Calabria), confidence 1, page silent (try https://en.wikipedia.org/wiki/Duchy_of_Benevento)
- `/ledger/5`: 633 gain (+1 cell Friuli), confidence 1 (try https://en.wikipedia.org/wiki/Duchy_of_Friuli)
- `/ledger/6`: 638 gain (+1 cell), confidence 1 (try https://en.wikipedia.org/wiki/Arioald)
- `/ledger/13`: 741 vassal_end of Spoleto (and /ledger/14 Benevento), confidence 1: Liutprand's campaigns against Spoleto 739-742 are not dated on the pages opened (try https://en.wikipedia.org/wiki/Duchy_of_Spoleto)
- `/ledger/15`: 741 loss of the Pentapolis and part of Umbria/Lazio, confidence 1; the Liutprand page dates the twenty-year peace only as after Gregory III's death and the four towns as undated (try https://en.wikipedia.org/wiki/Pope_Zachary)
- `/ledger/21`: 755 gain in Lazio (18 to 24 cells), confidence 1 (try https://en.wikipedia.org/wiki/Duchy_of_Rome)
- `/ledger/25`: 763 loss of Emilian cells to the papacy, confidence 1 (Desiderius page has only 'sometime in 760') (try https://en.wikipedia.org/wiki/Papal_States)
- `/ledger/1`: 587 vassal_start of Spoleto and Benevento (/ledger/2), confidence 1: the start year is Cliopatria's; also /ledger/17 (751 Benevento) and /ledger/28 (774) (try https://en.wikipedia.org/wiki/Duchy_of_Spoleto)
- `/ledger/11`: Ravenna: the Liutprand page says he 'again more certainly occupied Ravenna' in the mid-730s and byzantine-empire records a 738 loss and 740 gain of Ravenna; this dossier has only the 727-751 contest (try https://en.wikipedia.org/wiki/Liutprand,_King_of_the_Lombards)

### Spot checks

- `/ledger/7` confirmed: https://en.wikipedia.org/wiki/Rothari ('Rothari conquered Genoa in 641'; Oderzo 'in 641')
- `/ledger/8` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_the_Lombards ('He conquered Liguria (643), including the capital Genoa, Luni, and Oderzo')
- `/ledger/9` confirmed: https://en.wikipedia.org/wiki/Rothari (Scultenna, 'with the loss of 8,000 men, in 645')
- `/ledger/10` confirmed: https://en.wikipedia.org/wiki/Liutprand,_King_of_the_Lombards ('In 727, he crossed the Po and took Bologna, Osimo, Rimini and Ancona')
- `/ledger/12` confirmed: https://en.wikipedia.org/wiki/Liutprand,_King_of_the_Lombards ('gave Sutri over to the Papacy in 728')
- `/ledger/18` confirmed: https://en.wikipedia.org/wiki/Exarchate_of_Ravenna ('The exarchate fell in 751 with the Lombard conquest of Ravenna'; Perugia from the Kingdom page 'all territories south of Ravenna up to Perugia, from 750 to 751')
- `/ledger/20` confirmed: https://en.wikipedia.org/wiki/Exarchate_of_Ravenna ('In 752, the northeastern portion of the Exarchate' (Pentapolis) 'conquered by King Aistulf')

## kingdom-of-italy-medieval: thin

Area: infobox None (None) vs Cliopatria 171929, ratio None. Kingdom of Italy (Holy Roman Empire) infobox gives no area (confirmed). 936 shape 171,929 km2.

### Findings

- `/ledger/19` (APPLIED by the reviewer): 926 gain of Provence (confidence 1) is mis-dated: the Hugh page puts the de facto annexation after Louis the Blind's death on 5 June 928.
  - Evidence: Hugh of Italy page: 'Louis died on 5 June 928 and Hugh returned to Provence to sort out a succession'; '...Hugh annexed the kingdom to Italy de facto, issuing diplomata concerning Provence from his Italian chancery in a royal style.'
  - Fix: Year 926 -> 928, confidence 1 -> 2, note quoting the page.
- `/ledger/9` (to do): 898 gain from east-franks (confidence 1) leaves the kingdom's land with no holder in 897: east-franks has Italy slip away from April 896 (ledger 18-19) and its keyframe east-franks_897 excludes Italy, while this dossier loses the whole kingdom in 896 (/ledger/8) and takes it back only in 898.
  - Evidence: Berengar I page: after Arnulf left, 'the two kings met at Pavia in October and November and agreed to divide the kingdom', Berengar receiving 'the eastern half between the Adda and the Po' (year not stated; it follows the 896 campaign). east-franks.json ledger 18 (896-4 loss kingdom-of-italy) and keyframe east-franks_897.
  - Fix: Add a keyframe for 896-897 (the 892 outline, adjust, text: Lambert and Berengar hold Italy after Arnulf's departure) and move the regain to 896 (month 4, counterpart east-franks, confidence 2 on the Arnulf of Carinthia or Lambert of Italy page), or give a page that keeps Italy East Frankish through 897.
- `/keyframe_review/0` (to do): Provence is gained and lost in the ledger (863 /ledger/1, 875 /ledger/2; 928 /ledger/19, 933 /ledger/20) but appears in no keyframe: the 855-886 correction is Italy 887 + Spoleto 860 and the 922-935 correction is Italy 936.
  - Evidence: Reviewer rule 4: an event with no trace in the keyframes is fine only if small or the keyframe is adjusted for it; Provence is some 30,000 km2.
  - Fix: Split the 855 keyframe at 863 and 875 and the 922 keyframe at 928 and 933, adding {"region": "Provence"} for 863-875 and 928-933; or, if Provence is only a personal union, drop the four events and say so in notes.
- `/ledger/2` (to do): 875 loss of Provence names lower-burgundy (confidence 1), but lower-burgundy has no event in 875 (its next is Boso's election, 879-10) and west-franks records the matching gain from kingdom-of-italy in 877 (ledger 11).
  - Evidence: west-franks.json ledger 11: '877: Provence comes under the Carolingian crown. Boso became governor and count of Provence in 877'. Louis II page: the page names no successor in Provence.
  - Fix: Counterpart west-franks; align the year with west-franks (875 on Louis II's death, or 877) on a page (Boso of Provence or Charles the Bald).
- `/ledger/23` (to do): The vassalage of Berengar II to Otto I (August 952 to 961) is missing: kingdom-of-germany records vassal_start kingdom-of-italy 952-8 (c3, ledger 24) and vassal_end 961-12 (ledger 29); this dossier has only a confidence-1 contest_end and says the suzerain records it.
  - Evidence: Reviewer rule 3: a vassal_start of X is a vassal_start in X's ledger with this state as counterpart. kingdom-of-germany ledger 24: 'He and his son swore fealty at the Diet of Augsburg in August 952'.
  - Fix: Add vassal_start kingdom-of-germany 952 month 8 (region: the 952-961 keyframe) and vassal_end kingdom-of-germany 961 (before the merge), citing the Otto I page that kingdom-of-germany used.
- `/ledger/7` (to do): 894: east-franks has contest_start kingdom-of-italy in January 894 (Arnulf takes Bergamo, Milan and Pavia, ledger 13); this dossier has only a rename in 894.
  - Evidence: Berengar I page (opened by the author): 'In 894, Arnulf and Berengar defeated Guy at Bergamo and took control of Pavia and Milan.'
  - Fix: Add a 894 contest_start east-franks (Lombardy), ended with the 896 events, or note why Arnulf's 894 campaign is folded into the Spoleto contest.

### Gaps for a gap-filler

- `/ledger/9`: The year of the Berengar-Lambert partition (October-November, after Arnulf's departure) and the end of East Frankish control (try https://en.wikipedia.org/wiki/Lambert_of_Italy)
- `/ledger/2`: Who took Provence after Louis II's death and when (try https://en.wikipedia.org/wiki/Boso_of_Provence)
- `/ledger/23`: The 952 settlement (Diet of Augsburg) on a page of this dossier (try https://en.wikipedia.org/wiki/Otto_the_Great)
- `/identity/rulers`: Reign years of Charles the Bald, Carloman and Charles the Fat in Italy (875-887) and of Lambert; Lothair II's end and Berengar II's start (try https://en.wikipedia.org/wiki/King_of_Italy)
- `/keyframe_review/10`: Extent of the March of Verona ceded in 952 (read as Friuli plus 60 km around Verona) (try https://en.wikipedia.org/wiki/March_of_Verona)

### Spot checks

- `/ledger/0` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Holy_Roman_Empire) (infobox 'Treaty of Prüm ...: 19 September 855')
- `/ledger/1` confirmed: https://en.wikipedia.org/wiki/Louis_II_of_Italy ('In 863, upon the death of his brother Charles, Louis received the kingdom of Provence')
- `/ledger/8` confirmed: https://en.wikipedia.org/wiki/Berengar_I_of_Italy ('Berengar was with Arnulf's army that invaded Italy in 896')
- `/ledger/10` confirmed: https://en.wikipedia.org/wiki/Berengar_I_of_Italy ('Lambert died within days, on 15 October 898. Days later Berengar had secured Pavia and become sole ruler.')
- `/ledger/13` confirmed: https://en.wikipedia.org/wiki/Berengar_I_of_Italy (Louis blinded at Verona 'on 21 July' 905)
- `/ledger/14` confirmed: https://en.wikipedia.org/wiki/Berengar_I_of_Italy ('On 29 July 923' Fiorenzuola)
- `/ledger/19` mis-dated: https://en.wikipedia.org/wiki/Hugh_of_Italy (confidence 1; page dates the de facto annexation after 5 June 928; fixed by the reviewer)
- `/ledger/20` confirmed: https://en.wikipedia.org/wiki/Hugh_of_Italy ('He concluded a treaty with Rudolph in 933 by which Rudolf abandoned his claims to Italy in return for being handed Provence.')
- `/ledger/22` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Holy_Roman_Empire) (March of Verona annexed by Bavaria in 952)
- `/ledger/24` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Holy_Roman_Empire) ('Otto defeated the previous king and conquered Pavia in 961'; 'proclaimed king of Italy at Pavia')

## kingdom-of-italy: thin

Area: infobox 250320 (1861) vs Cliopatria 235522, ratio 0.94. Second infobox figure 310,190 km2 (1936) vs 295,325 km2 (1936 shape): ratio 0.95. Both quoted correctly in keyframes 0, 1, 15.

### Findings

- `/ledger/14` (APPLIED by the reviewer): Loss of Friuli and eastern Veneto dated 1918 at confidence 1 with no page; the Caporetto breakthrough that took the land is October-November 1917.
  - Evidence: Battle of Caporetto page: 'took place from 24 October to 19 November 1917'; infobox 'Central Powers advance 150 kilometres (93 mi) to the Piave River'.
  - Fix: Year 1918 -> 1917, month 10, source the Caporetto page (added to sources[]), confidence 1 -> 2, note quoting the page.
- `/keyframe_review/22` (to do): The 1944 keyframe (verdict wrong) uses the whole 1945 outline as its correction, contradicting its own text and the ledger: /ledger/39 gives northern Italy and Tuscany to italian-social-republic in September 1943 and /ledger/40 returns them in 1945.
  - Evidence: Correction text: 'the kingdom's holdings were the part of Italy not held by the German-backed Italian Social Republic'; region: {cliopatria: Kingdom of Italy, year: 1945}.
  - Fix: Correction {"minus": [{"cliopatria": "Kingdom of Italy", "year": 1945}, <the region of /ledger/39>]} with the same text.
- `/ledger/16` (to do): The return of Friuli and eastern Veneto is folded into a 1919 confidence-1 gain from austria-hungary; the Caporetto page places the Vittorio Veneto offensive 'on the anniversary of Caporetto' (October-November 1918). Austria-Hungary itself ends in 1918 (polities.csv 1868..1918), so a 1919 gain from it has no living counterpart.
  - Evidence: Battle of Caporetto page: 'On the anniversary of Caporetto, the Piave line served as springboard for the final Italian offensive, the Battle of Vittorio Veneto'.
  - Fix: Add a 1918 month 11 gain of the /ledger/14 region from austria-hungary (confidence 2, Caporetto page) and restrict /ledger/16 to the remaining new cells; say in notes who ceded Trentino-Alto Adige and Trieste in 1919 (Saint-Germain) or use counterpart austria-hungary with a note.
- `/keyframe_review/13` (to do): The 1919 and 1920-1931 shapes hold 3 then 11 Turkish cells (Antalya) with no gain or occupation event, and their exit is a confidence-1 loss in 1932 that the author's own note calls 'probably much earlier'; ottoman-empire ledger 235 (1922) has the Turkish National Movement force out 'the Greeks, Armenians, and Italians'.
  - Evidence: shapes.csv / keyframe notes 12-13; ottoman-empire.json ledger 235.
  - Fix: Record the Anatolian zone as occupation_start ottoman-empire 1919 and occupation_end at the Italian withdrawal on a page; mark keyframe 13 adjust (remove the Turkish cells after the withdrawal); drop /ledger/22.
- `/wars/2` (to do): The Italian front war has one zone (Trentino and Trieste) and no zone for Friuli and eastern Veneto, which changed hands in 1917-1918.
  - Evidence: Battle of Caporetto page (advance to the Piave, 24 October-19 November 1917).
  - Fix: Add a zone for Friuli and the Veneto east of the Piave (the /ledger/14 region) and cite the Caporetto page.
- `/ledger/20` (to do): 1923 Dodecanese gain names republic-of-turkey, which the republic-of-turkey dossier founds only on 29 October 1923 (its ledger 0); /ledger/19 ends the occupation against ottoman-empire, which dissolves in 1922 (ottoman-empire ledger 237).
  - Evidence: Italian Empire page: 'the 1923 Treaty of Lausanne formalized Italian administration of both Libya and the Dodecanese Islands'; republic-of-turkey.json ledger 0; ottoman-empire.json ledger 237.
  - Fix: Pick one counterpart for both events that is alive in 1923 (republic-of-turkey with month after its founding is wrong for July 1923; consider ottoman-empire for the occupation pair ended at 1922-11 and the gain from republic-of-turkey dated with Lausanne, or nobody) and say so in notes; route the mirror to me-10.

### Gaps for a gap-filler

- `/keyframe_review/13`: Start and end of the Italian zone in Anatolia (Antalya), 1919-1921/22 (try https://en.wikipedia.org/wiki/Turkish_War_of_Independence)
- `/keyframe_review/12`: The 1918-1919 expansion of the Albanian protectorate (25 to 75 cells) and the Montenegrin and Dalmatian armistice holdings (try https://en.wikipedia.org/wiki/Italian_protectorate_over_Albania_(1917–1920))
- `/ledger/12`: Dodecanese occupation dated 1912 at confidence 1 (May 1912 not on the Italian Empire page) (try https://en.wikipedia.org/wiki/Italo-Turkish_War)
- `/ledger/24`: Italian occupation zone in France dated 1940 at confidence 1 (page undated) (try https://en.wikipedia.org/wiki/Italian_invasion_of_France)
- `/ledger/28`: Extension of the Greek zone in 1942, confidence 1 (try https://en.wikipedia.org/wiki/Italian_occupation_of_Greece)
- `/ledger/38`: Who took the annexed Yugoslav lands in September 1943, confidence 1 (Axis page: Germany's Adriatic Littoral zone; NDH got the Sidraga-Ravni Kotari district) (try https://en.wikipedia.org/wiki/Axis_occupation_of_Yugoslavia)
- `/ledger/40`: The 1943-1945 front and the 1945 regain of the north (confidence 1) (try https://en.wikipedia.org/wiki/Italian_Social_Republic)

### Spot checks

- `/ledger/4` confirmed: https://en.wikipedia.org/wiki/Third_Italian_War_of_Independence (Treaty of Vienna 3 October 1866, 'modern Veneto, parts of Friuli and the city of Mantua'; 'ceded Venetia to Italy on 19 October')
- `/ledger/5` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy ('Capture of Rome: 20 September 1870')
- `/ledger/8` confirmed: https://en.wikipedia.org/wiki/Italian_Empire ('annexed the port of Massawa in Eritrea on the Red Sea from the crumbling Egyptian Empire' (the page does name the former holder, unlike the note says; the Kingdom page has 1888))
- `/ledger/11` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy ('On 7 September 1901, a concession in Tientsin was ceded to Italy by the Qing Dynasty')
- `/ledger/13` confirmed: https://en.wikipedia.org/wiki/Italian_Empire ('In June 1917, general Giacinto Ferrero proclaimed the Italian-controlled territory in Albania to be independent' under Italian protection)
- `/ledger/14` mis-dated: https://en.wikipedia.org/wiki/Battle_of_Caporetto (confidence 1; the advance to the Piave is 24 October-19 November 1917; fixed by the reviewer)
- `/ledger/15` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy ('In 1919 it annexed Trieste and Trentino-Alto Adige/Südtirol.')
- `/ledger/18` confirmed: https://en.wikipedia.org/wiki/Treaty_of_Rapallo_(1920) (signed 12 November 1920; Istria, Zadar, Cres, Lošinj, Lastovo, Palagruža)
- `/ledger/21` confirmed: https://en.wikipedia.org/wiki/Treaty_of_Rapallo_(1920) (Fiume: 'Italy annexed it under the 1924 Treaty of Rome')
- `/ledger/25` confirmed: https://en.wikipedia.org/wiki/Axis_occupation_of_Yugoslavia (Ljubljana Province, 'large sections of Dalmatia, nearly all of the Adriatic islands, the Bay of Kotor'; 'Italy annexed Kosovo')
- `/ledger/29` confirmed: https://en.wikipedia.org/wiki/Italian_Empire ('In November 1942 ... Italian-occupied France was expanded with the occupation of Corsica')
- `/ledger/35` confirmed: https://en.wikipedia.org/wiki/Axis_occupation_of_Yugoslavia ('The former Italian kingdoms of Albania and of Montenegro were placed under German occupation')
- `/ledger/39` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy ('German forces occupied northern and central Italy, established the Italian Social Republic' (region the researcher's reading, confidence 2))
- `/ledger/42` confirmed: https://en.wikipedia.org/wiki/Kingdom_of_Italy ('Monarchy abolished: 18 June 1946')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-the-lombards 587 found (lombards) | lombards 586 dissolve | matched | Hand-over; lombards names counterpart 'kingdom-of-italy': repoint to kingdom-of-the-lombards and keep one colour. |
| kingdom-of-the-lombards 587 vassal_start (duchy-of-spoleto) | - | exception | duchy-of-spoleto: no dossier yet; owner group has not run (eu-13 sibling); same for 741 vassal_end and 751 gain. |
| kingdom-of-the-lombards 587 vassal_start (duchy-of-benevento) | - | exception | duchy-of-benevento: no dossier yet; owner group has not run (eu-13 sibling); same for 741 vassal_end, 751 vassal_start, 774 vassal_end. |
| kingdom-of-the-lombards 603 gain (eastern-roman-empire) | eastern-roman-empire 603 loss | matched | ERE names 'kingdom-of-italy': repoint. |
| kingdom-of-the-lombards 628 gain (eastern-roman-empire) | - | missing | No 628 loss in eastern-roman-empire (eu-05); confidence 1 on this side. |
| kingdom-of-the-lombards 633 gain (byzantine-empire) | - | missing | No mirror in byzantine-empire (eu-05); confidence 1. |
| kingdom-of-the-lombards 638 gain (byzantine-empire) | - | missing | No mirror in byzantine-empire; confidence 1. |
| kingdom-of-the-lombards 641 gain (byzantine-empire) | - | missing | Genoa and Oderzo (Rothari page, c3): byzantine-empire has no loss 640-645. |
| kingdom-of-the-lombards 643 gain (byzantine-empire) | - | missing | Liguria (Kingdom page, c3): no mirror in byzantine-empire. |
| kingdom-of-the-lombards 645 gain (byzantine-empire) | - | missing | Modena/Scultenna (Rothari page, c2): no mirror. |
| kingdom-of-the-lombards 727 gain (byzantine-empire) | - | missing | Bologna, Osimo, Rimini, Ancona and the Pentapolis (Liutprand page, c3): byzantine-empire has no 727 loss. |
| kingdom-of-the-lombards 728 loss (papal-states) | - | exception | papal-states: no dossier yet; owner group has not run (eu-13 sibling); same for 756 and 763 losses. |
| kingdom-of-the-lombards 741 loss (byzantine-empire) | byzantine-empire 740 gain | mismatch | Years within one, land differs: this side the Pentapolis/Umbria/Lazio cells, byzantine-empire Ravenna (its 738 loss of Ravenna, c2, has no mirror here: this dossier has a 727-751 contest of Ravenna instead). |
| kingdom-of-the-lombards 751 gain (byzantine-empire) | byzantine-empire 751 loss | matched | Ravenna; repoint byzantine-empire's 'kingdom-of-italy'. |
| kingdom-of-the-lombards 752 gain (byzantine-empire) | byzantine-empire 751 loss | matched | Pentapolis, within one year of the 751 loss. |
| kingdom-of-the-lombards 755 gain (byzantine-empire) | - | missing | Lazio cells, confidence 1 on both counts; no mirror. |
| kingdom-of-the-lombards 755 contest_start (kingdom-of-the-franks) | - | missing | Pepin's 755-756 sieges of Pavia (Aistulf page, c3): kingdom-of-the-franks (eu-07) has no 755-756 contest. |
| kingdom-of-the-lombards 774 dissolve (kingdom-of-the-franks) | kingdom-of-the-franks 774 gain | matched | Franks' 773 contest_start, 774 contest_end and gain name 'kingdom-of-italy': repoint to kingdom-of-the-lombards. |
| kingdom-of-italy-medieval 855 found (middle-franks) | middle-franks 855 split | matched | Repoint middle-franks' 'kingdom-of-italy'. |
| kingdom-of-italy-medieval 863 gain (lower-burgundy) | lower-burgundy 863 loss | matched | lower-burgundy has month 1; repoint its 'kingdom-of-italy'. |
| kingdom-of-italy-medieval 875 loss (lower-burgundy) | west-franks 877 gain | mismatch | lower-burgundy has no 875 event; west-franks records Provence from kingdom-of-italy in 877: counterpart and year disagree. |
| kingdom-of-italy-medieval 889 contest_start (duchy-of-spoleto) | - | exception | duchy-of-spoleto: no dossier yet; owner group has not run; also 898 gain. |
| east-franks 894 contest_start (kingdom-of-italy-medieval) | - | missing | east-franks 894-1 contest with Italy (Arnulf takes Bergamo, Milan, Pavia) has no mirror here. |
| kingdom-of-italy-medieval 896 loss (east-franks) | east-franks 896 gain | matched | Repoint east-franks' 'kingdom-of-italy'. |
| kingdom-of-italy-medieval 898 gain (east-franks) | east-franks 896 loss | mismatch | Two years apart: east-franks loses Italy in April 896 and excludes it from its 897 keyframe; this dossier regains it in 898 (c1), so Italy has no holder in 897. |
| kingdom-of-italy-medieval 900 contest_start (lower-burgundy) | lower-burgundy 900 contest_start | matched | lower-burgundy splits it into 900-902 and 905; this side one contest 900-905. |
| kingdom-of-italy-medieval 923 contest_start (upper-burgundy) | upper-burgundy 923 contest_start | matched | Fiorenzuola: 29 July here (Berengar page), 17 July in upper-burgundy; contest_end 926 matched. |
| kingdom-of-italy-medieval 928 gain (lower-burgundy) | - | mismatch | Re-dated from 926 by the reviewer. lower-burgundy has no loss; upper-burgundy's 933 gain of Provence names lower-burgundy, not Italy, as the loser. |
| kingdom-of-italy-medieval 933 loss (upper-burgundy) | upper-burgundy 933 gain | mismatch | Same year and land (Provence); upper-burgundy names lower-burgundy as counterpart. |
| kingdom-of-italy-medieval 951 contest_start (kingdom-of-germany) | kingdom-of-germany 951 occupation_start | mismatch | Type differs (contest vs occupation). |
| kingdom-of-italy-medieval 952 loss (kingdom-of-germany) | kingdom-of-germany 952 gain | matched | March of Verona; march-of-verona also founds from 'kingdom-of-italy' in 952: repoint both. |
| kingdom-of-germany 952 vassal_start (kingdom-of-italy-medieval) | - | missing | kingdom-of-germany 952-8 vassal_start / 961-12 vassal_end of Italy (c3/c2) have no mirror here. |
| kingdom-of-italy-medieval 961 merge (kingdom-of-germany) | kingdom-of-germany 961 gain | matched | Repoint kingdom-of-germany's 'kingdom-of-italy'; holy-roman-empire also cites kingdom-of-italy. |
| kingdom-of-italy 1861 found (kingdom-of-sardinia) | - | exception | kingdom-of-sardinia: no dossier yet; owner group has not run (eu-13 sibling). |
| kingdom-of-italy 1866 gain (austrian-empire) | - | exception | austrian-empire: no dossier yet; owner group has not run. |
| kingdom-of-italy 1870 gain (papal-states) | - | exception | papal-states: no dossier yet; owner group has not run. |
| kingdom-of-italy 1885 gain (khedivate-of-egypt) | khedivate-of-egypt 1885 loss | mismatch | Year matches (Feb 1885); khedivate-of-egypt names italian-africa (founded 1890) as the gainer. |
| kingdom-of-italy 1889 gain (ethiopian-empire) | ethiopian-empire 1890 loss | mismatch | ethiopian-empire loses the land to italian-africa in 1890 (c1); this side gains it in 1889 (Wuchale). |
| kingdom-of-italy 1890 loss (italian-africa) | italian-africa 1890 found | mismatch | italian-africa's found and predecessors name ethiopian-empire only; it should take Massawa and Assab from kingdom-of-italy (route to af-08). |
| kingdom-of-italy 1901 occupation_start (qing-dynasty) | - | missing | qing-dynasty has no Tientsin concession event; the 1943 occupation_end against qing-dynasty (ended 1912) is kept only for pairing. |
| kingdom-of-italy 1912 occupation_start (ottoman-empire) | ottoman-empire 1912 loss | mismatch | Year matches; type differs (occupation here, loss there). |
| kingdom-of-italy 1917 vassal_start (albania) | - | exception | albania: no dossier yet; owner group has not run (eu-18); also 1920, 1939, 1943. |
| kingdom-of-italy 1917 loss (austria-hungary) | - | exception | austria-hungary: no dossier yet; owner group has not run (eu-17/eu-20); re-dated from 1918 by the reviewer; also the 1919 gains. |
| kingdom-of-italy 1920 gain (yugoslavia) | - | exception | yugoslavia: no dossier yet; owner group has not run (eu-21); also 1941 gain and occupation. |
| kingdom-of-italy 1923 gain (republic-of-turkey) | republic-of-turkey 1923 found | mismatch | republic-of-turkey has no Dodecanese loss and is founded October 1923, after Lausanne; ottoman-empire dissolves 1922 while the occupation_end against it is 1923. |
| kingdom-of-italy 1924 gain (Free State of Fiume) | - | exception | Listed in the author's counterparts_needing_dossiers. |
| kingdom-of-italy 1932 loss (republic-of-turkey) | - | mismatch | No mirror in republic-of-turkey; ottoman-empire ledger 235 has the Italians forced out by 1922. |
| kingdom-of-italy 1940 occupation_start (vichy-france) | - | exception | vichy-france: no dossier yet; owner group has not run; also 1942-1943. |
| kingdom-of-italy 1941 occupation_start (first-hellenic-republic) | - | exception | first-hellenic-republic (Cliopatria 1822..1940) ends before the occupation; author lists hellenic-state as needing a dossier. |
| kingdom-of-italy 1943 loss (nazi-germany) | - | exception | nazi-germany: no dossier yet; owner group has not run. |
| kingdom-of-italy 1943 loss (italian-social-republic) | - | exception | Listed in the author's counterparts_needing_dossiers; also 1945 gain. |

## Problems for the orchestrator

- No page failed to load. Validator: 0 errors for all three; the only warnings are the sibling dossiers' Cliopatria shapes (the 48 shapes are covered across the three: 17 + 8 + 23) and 'italian-social-republic' without a dossier.
- Two reviewer fixes applied in place and re-validated: kingdom-of-italy-medieval /ledger/19 (926 -> 928, c2) and kingdom-of-italy /ledger/14 (1918 -> 1917-10, c2, Battle_of_Caporetto added to sources).
- Repointing needed in other groups' dossiers that still use counterpart 'kingdom-of-italy' for the Lombard (587-774) and medieval (855-961) kingdoms: lombards, eastern-roman-empire, byzantine-empire, kingdom-of-the-franks (eu-05/06/07); middle-franks, lower-burgundy, upper-burgundy, east-franks, kingdom-of-germany, march-of-verona, holy-roman-empire (eu-07/08). The author's notes list them.
- The lombards dossier asks for Lombard Italy 587-774 to be merged into it; the author made a new slug with a hand-over. Orchestrator/colour agent: keep one colour across 586/587.
- The author's report gaps entry claims confidence-1 events for the 692 Lombard shape step; the ledger has none.
- Italy has no holder in 897: Cliopatria hands Italy to East Franks for 896-897, east-franks corrected that to 896 only, and kingdom-of-italy-medieval regains it only in 898.
