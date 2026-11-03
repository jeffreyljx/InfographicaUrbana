# Review of batch eu-12-a (Iberia, part a)

Adversarial review, 2026-10-25. Eight dossiers: kingdom-of-asturias, emirate-of-cordoba, kingdom-of-pamplona, kingdom-of-sobrarbe, county-of-aragon, county-of-ribagorza, rebellion-of-umar-ibn-hafsun, banu-qasi. All validate with 0 errors and 0 warnings under `--resolve` (before and after the reviewer's edits). Neighbour dossiers read: kingdom-of-the-franks, west-franks, duchy-of-gascony, umayyad-caliphate, aquitaine, abbasid-caliphate, idrisids, fatimid-caliphate (the other Context polities are not written yet). 16 Wikipedia pages opened; every spot-checked confidence-3 event was found on a page with its year; two events cited the wrong page (fixed), one confidence-2 event quoted a sentence from a different page than the one cited (fixed, lowered to 1).

## Verdicts

### kingdom-of-asturias: thin

Area: The Asturias page infobox has no area (checked); acknowledged in keyframe 5's note.

Spot checks: /ledger/2 confirmed; /ledger/3 confirmed; /ledger/10 confirmed; /ledger/16 confirmed; /ledger/12 confirmed; /ledger/7 confirmed.

Findings:

- `/identity/rulers/7` (applied by reviewer): Bermudo I (788-791) was missing, leaving a gap between Mauregato (to 788) and Alfonso II (from 791). Evidence: Alfonso II page: 'Mauregatus was succeeded by Bermudo I, Alfonso's cousin, who abdicated after his defeat at the Battle of the Burbia River'; 'Alfonso was subsequently elected king on 14 September 791'. Fix: Inserted Bermudo I 788-791 (source Alfonso II page) and reworded the Alfonso II note.
- `/ledger/3/counterpart` (applied by reviewer): The 754 gain of León names umayyad-caliphate, whose dossier ends in 750. Evidence: umayyad-caliphate /ledger/93 gives al-Andalus in 750 to 'Fihrid governors of al-Andalus' and its identity ends 750-08. Fix: Counterpart set to 'Fihrid governors of al-Andalus' (the same string as the Umayyad dossier); note amended.
- `/keyframe_review/4 and /ledger/6` (for the author): From 825 the shape grows east from 2.93 W to 1.78 W (Álava, La Rioja, eastern Burgos), but the 825 gain names only Burgos, Palencia, Valladolid and Zamora; Álava and La Rioja are never gained yet are lost in 910 (/ledger/15). Evidence: shapes.csv: kingdom-of-asturias_755 bbox east -2.934, _825 east -1.7756. La Rioja is Banu Qasi and Pamplona land in the same years (Ordoño I's 859 fight at Albelda; banu-qasi /ledger/4 and /ledger/6; kingdom-of-pamplona /ledger/5). Fix: Either subtract La Rioja (and Álava, unless a page dates it) from keyframes 4-6, or add a confidence-1 gain for them; reconcile La Rioja with banu-qasi and kingdom-of-pamplona.
- `/ledger/6` (for the author): The 825 gain of whole Zamora and Valladolid provinces rests on 'the repopulation of parts of Galicia, León, and Castile was started'; the page names no Duero town. Evidence: Alfonso II page, sentence quoted; the Alfonso III page has Zamora as a town attacked in 901 and the place Alfonso III died in 910, i.e. the Duero line is Alfonso III's. Fix: Lower to confidence 1 or restrict the 825 gain to León/Palencia/Burgos north of the Duero and date Zamora and Valladolid later.

Gaps for a gap-filler:

- `/ledger/1`: When Cantabria joined (confidence 1; the page only says Alfonso was son of Duke Peter of Cantabria) (try https://en.wikipedia.org/wiki/Alfonso_I_of_Asturias)
- `/ledger/15`: Who held Castile, Cantabria, Álava and La Rioja in 910-924 (confidence 1) (try https://en.wikipedia.org/wiki/County_of_Castile)
- `/ledger/6`: The dated Duero resettlements (Zamora 893, Simancas, Toro, Burgos 884) (try https://en.wikipedia.org/wiki/Repopulation_of_the_Duero_valley)

### emirate-of-cordoba: fail

Area: No infobox area on the Emirate page (checked). The dossier's own c. 900 collapse to a 90 km circle (~25,000 km2) against Cliopatria's 406,844 km2 is sourced and acknowledged in keyframe 16.

Spot checks: /ledger/16 confirmed; /ledger/17 confirmed; /ledger/6 confirmed; /ledger/7 confirmed; /ledger/5 confirmed; /ledger/18 confirmed; /ledger/21 confirmed; /ledger/22 not on page (quote is on the Emirate page; fixed, confidence 1); /ledger/23 not on page (on the Banu Qasi page; fixed); /ledger/25 confirmed.

Findings:

- `/keyframe_review/0 -> /keyframe_review/1` (for the author): The 756 founding core (Córdoba and Sevilla provinces) becomes Cliopatria's 445,142 km2 shape in 757 with no ledger event: the takeover of al-Andalus from Yusuf al-Fihri is missing, and so is the war (Musarah 756). Evidence: Rule 4 of the reviewer brief: every change between consecutive keyframes needs an event. Emirate page: 'this first unification of al-Andalus ... still took more than twenty-five years to complete'. Fix: Add a 756/757 gain from 'Fihrid governors of al-Andalus' for the land the 757 shape holds (confidence by page), or dated gains (Toledo, Zaragoza) where a page gives them, and the war with Yusuf al-Fihri.
- `/ledger (872) and /keyframe_review/13-15` (for the author): No 872 loss to banu-qasi: banu-qasi /ledger/0 founds the Banu Qasi state in Zaragoza and Tudela in 872 from the emirate, while the emirate's keyframes 870, 875 and 878 ('ok') keep Zaragoza and /ledger/14 then gains Zaragoza in 884 from banu-qasi without ever having lost it. Two dossiers of this batch draw Zaragoza 872-883. Evidence: Banu Qasi page: 'In January 872, Isma'il ibn Musa entered Zaragoza ... the two of them together taking Monzon'; 'Furtun ibn Musa occupied Tudela'; 'In 884, the emir ... took Zaragoza'. Fix: Add 872 loss to banu-qasi (Zaragoza province with Monzón, and Tudela); mark keyframes 13-15 adjust without those lands from 872 (Tudela stays Banu Qasi's until the 898 vassalage).
- `/ledger/0/counterpart` (applied by reviewer): The found event names umayyad-caliphate, whose dossier ends in 750 and hands al-Andalus to the 'Fihrid governors of al-Andalus'. Evidence: umayyad-caliphate /ledger/93 and /identity/end (750). Fix: Counterpart set to 'Fihrid governors of al-Andalus'; predecessor link to umayyad-caliphate kept (that dossier lists emirate-of-cordoba as successor).
- `/ledger/22/confidence` (applied by reviewer): The 922 gain of most of al-Andalus quotes 'rapidly restored Umayyad power throughout al-Andalus' from the Abd al-Rahman III page; that sentence is on the Emirate page, and only Pechina is dated; keyframe 18 itself says 'conf 1 in the ledger'. Evidence: Abd al-Rahman III page: no 'restored'/'throughout al-Andalus'; 'Despite having defeated only some of the rebels' in 929. Emirate page: 'Abd al-Rahman III rapidly restored Umayyad power throughout al-Andalus'. Fix: Confidence 2 -> 1; note attributes the quote to the Emirate page; keyframe 18 note reworded (also: the Abd al-Rahman III page does not date Zaragoza to 937).
- `/ledger/23/source` (applied by reviewer): The 924 vassal_end cites the Abd al-Rahman III page, which does not name Tudela; the quoted words are not on any page. Evidence: Banu Qasi page: 'on his return to Tudela he removed the Banu Qasi and sent them to Córdoba' (the year after 923). Fix: Source set to the Banu Qasi page and the quote corrected.
- `/ledger/15` (for the author): vassal_start banu-qasi (898) has no mirror: banu-qasi /ledger/2 records a 'gain' from the emirate instead. Evidence: Notes: 'A vassal keeps its own land, drawn in the suzerain's lighter tint: Banu Qasi march under the Emirate 898-924 (vassal_start/end)'. Fix: Fix on the banu-qasi side (vassal_start emirate-of-cordoba 898, vassal_end 924).
- `/ledger/3, /ledger/4, /ledger/16, /ledger/18, /ledger/20-22` (for the author): Counterparts 'rebellious lords of the Upper March', 'autonomous lords of al-Andalus' and 'Banu Muhallab of Guadix and the lords of Jerez and Cádiz' are neither slugs, nobody, nor in counterparts_needing_dossiers; the 900 loss is the largest land move in the batch. kingdom-of-the-franks /ledger/59 and /ledger/65 say the Franks took and returned the Ebro cells in 778/783. Evidence: Research brief rule: every gain names a counterpart that should carry the loss, or nobody, or a state flagged as needing a dossier. Fix: List them (Banu Hajjaj of Seville, the lords of Toledo, Mérida, Badajoz, Murcia) under counterparts_needing_dossiers or use nobody; reconcile 778/783 with the Franks.
- `/ledger/16 vs /keyframe_review/16` (for the author): The collapse to Córdoba is dated c. 900 in the ledger but drawn from 898 by keyframe 16. Evidence: Emirate page '(c. 900)'. Fix: Start the circle correction in 900 or date the event 898 with the c. noted.
- `/wars/9` (for the author): The 920 campaign 'took Osma and San Esteban de Gormaz' but the ledger has no gain or contest for them. Evidence: War outcome text in the dossier. Fix: Add a 920 gain (counterpart kingdom-of-leon) or say none was held.
- `/keyframe_review/6` (for the author): Keyframe 783-787 is 'ok' though Girona was lost in 785 (/ledger/5). Evidence: Spanish March page: 'In 785 the county of Girona (with Besalú) ... was taken'. Fix: Mark adjust (without Girona from 785).

Gaps for a gap-filler:

- `/ledger/9`: 825 Duero fringe loss, confidence 1 (try https://en.wikipedia.org/wiki/Alfonso_II_of_Asturias)
- `/ledger (Mérida, Toledo)`: 9th-century revolts of Toledo and Mérida (try https://en.wikipedia.org/wiki/Toledo)

### kingdom-of-pamplona: thin

Area: Navarre page: 'an extent of about 15,000 km2' under Sancho Garcés (905-925); the infobox figure is 10,000 km2 for 1300 (outside this dossier). Compared in keyframe 0.

Spot checks: /ledger/6 confirmed; /ledger/12 confirmed; /ledger/15 confirmed; /ledger/16 confirmed; /ledger/26 confirmed; /ledger/27 confirmed; /ledger/9 confirmed (page: 'Sancho jumped on the opportunity to take his portion'); /ledger/10 confirmed in substance; 'entire county by conquest and submission' is on the County of Ribagorza page.

Findings:

- `/identity/rulers` (applied by reviewer): Rulers were not contiguous: 931-970 and 994-1004 were empty. Evidence: Kingdom of Navarre page: 'García Sánchez (931–970)'; 'during the reign of García Sánchez II'; 'the King himself killed during a raid in the year 1000'; 'ruled by his cousins Sancho and García of Viguera until the year 1004, when Sancho III would become ruling king'. Fix: Inserted García Sánchez I 931-970, García Sánchez II 994-1000 and the Viguera regents 1000-1004 (source Navarre page).
- `/ledger/0 and /identity/predecessors` (for the author): The founding names only the Franks; duchy-of-gascony /ledger/6 (conf 3) loses 'the Pamplonese' to kingdom-of-pamplona in 824 and the Navarre infobox lists the Duchy of Gascony as a predecessor. Evidence: duchy-of-gascony /ledger/6: 'The Pamplonese were definitively detached from the duchy in 824'. Fix: Add duchy-of-gascony as a predecessor and say in the found note which land came from whom.
- `/ledger/7, /ledger/9, /ledger/10` (for the author): Sobrarbe is gained three times (1015 from taifa-of-zaragoza, 1018 and 1025 from county-of-ribagorza) and Ribagorza twice; county-of-ribagorza loses only the Ribagorza circle in 1018 and 1025. Evidence: county-of-ribagorza /ledger/5 and /ledger/6 regions. Fix: 1018: William Isarn's portion only; 1025: the rest; drop Sobrarbe from both.
- `/keyframe_review/4` (for the author): Keyframe 922-965 adds all of La Rioja from 922 while /ledger/5 gains it in 923, and Arnedo (/ledger/2, 914) is absent from keyframe 866-921. Evidence: Ledger years. Fix: Start La Rioja in 923 or note it; include Arnedo from 914.

Gaps for a gap-filler:

- `/ledger (934)`: Toda's submission to Abd al-Rahman III (vassal_start caliphate-of-cordoba); the notes leave it to the caliphate ledger, but the mirror rule needs it here too (try https://en.wikipedia.org/wiki/Toda_of_Pamplona)
- `/ledger/19 and /ledger/20`: 1035 western conquests and Gascon protectorate, confidence 1 (try https://en.wikipedia.org/wiki/Sancho_III_of_Pamplona)
- `/keyframe_review/3`: 9th-century border; only the 905 extent 'to Nájera and Arba' is on the page (thin by design: 3 Cliopatria shapes, budget 1-2 pages) (try https://en.wikipedia.org/wiki/Kingdom_of_Navarre)

### kingdom-of-sobrarbe: thin

Area: The Sobrarbe page has no infobox.

Spot checks: /ledger/0 confirmed (page silent on 825; legend of 724); /ledger/1 confirmed (page silent on 829).

Findings:

- `/keyframe_review/0/correction` (for the author): The 'wrong' keyframe is corrected to the County of Aragon's own shape, so 825-829 the same 3,490 km2 are owned by kingdom-of-sobrarbe and county-of-aragon (keyframe 807-829), and kingdom-of-the-franks /ledger/92 hands the same '15 of Sobrarbe' cells to kingdom-of-pamplona in 825; no event links the three. Evidence: shapes.csv: kingdom-of-sobrarbe_825 bbox equals county-of-aragon_830; Sobrarbe page: 'legendary predecessor to the Kingdom of Aragon'. Fix: Orchestrator decision: drop the Cliopatria row (recommended by the author) or make Sobrarbe a rename inside county-of-aragon; until then the map double-draws the valleys.
- `/identity/capitals/0` (for the author): Capital Aínsa (0.138 E) lies outside the shape (bbox -1.153 to -0.124 E). Evidence: shapes.csv bbox; Sobrarbe page: 'with its capital at Aínsa'. Fix: Note the mismatch, or drop with the row.

Gaps for a gap-filler:

- `/ledger/0`: Every event is confidence 1: the page dates nothing to 825 or 829 (legend) (try https://en.wikipedia.org/wiki/Kingdom_of_Sobrarbe)

### county-of-aragon: thin

Area: No infobox area on the County of Aragon page.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.

Findings:

- `/ledger (844, 922)` (for the author): No mirror of kingdom-of-pamplona /ledger/1 (844 vassal_start county-of-aragon) and /ledger/3 (922 vassal_end). Evidence: County of Aragon page: 'Galindo was forced to make himself a vassal of Íñigo'; count list '844–867: Galindo Aznárez I ... family restored on accepting suzerainty of Pamplona'. Fix: Add vassal_start kingdom-of-pamplona 844 and vassal_end kingdom-of-pamplona 922 (confidence 3).
- `/ledger (807-820)` (for the author): The Frankish vassalage before 820 is left to the Franks' ledger, but kingdom-of-the-franks (ends 843) has no Aragon event and instead loses these cells to kingdom-of-pamplona in 825 (/ledger/92). Evidence: County of Aragon page: 'created by the Carolingians'; Aznar I was 'Charlemagne's vassal' (dossier note); count list: García the Bad 'installed as vassal by Pamplona' in 820. Fix: Add vassal_start kingdom-of-the-franks 807 and vassal_end 820; say in the 820 note that García was installed as Pamplona's vassal (before Pamplona's 824 start); route the Franks' 825 event to eu-07.
- `/keyframe_review/0` (for the author): 807-829 overlaps kingdom-of-sobrarbe's 825-829 keyframe on the same cells. Evidence: See kingdom-of-sobrarbe. Fix: Resolved by the orchestrator's decision on the Sobrarbe row.

### county-of-ribagorza: thin

Area: No infobox area; the Cliopatria shapes are Pamplona's (all 11 keyframes adjust/wrong, explained).

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/4 confirmed; /ledger/8 confirmed; /ledger/7 confirmed; /ledger/5 confirmed.

Findings:

- `/ledger (1035, 1045)` (for the author): No mirror of kingdom-of-pamplona /ledger/23 (1035 vassal_start county-of-ribagorza) and /ledger/24 (1045 vassal_end); the ledger has only the 1035 gain. Evidence: Navarre page: Gonzalo held Sobrarbe and Ribagorza 'as vassal of his eldest brother, García'. Fix: Add vassal_start kingdom-of-pamplona 1035 and vassal_end 1045.
- `/ledger/2` (for the author): The 920 recovery of the whole county from al-Tawil (confidence 1) is contradicted by the cited page, which calls Ribagorza 'mostly-overrun' at Raymond I's death. Evidence: Raymond I page: Ribagorza 'went to his two eldest, Miro and Bernard Unifred' and is 'mostly-overrun'. Fix: Keep only a remnant from 920 and date the recovery from another page, or drop the 920 gain.
- `/ledger/4/counterpart` (for the author): The 1010 split names kingdom-of-castile, which intervened but took no land; the split-off portion went to Mayor García and Raymond III of Pallars. Evidence: County of Ribagorza page: 'Partitioned following intervention by' Sancho García of Castile; Mayor García and Raymond III of Pallars (1010–1025). Fix: Counterpart 'Mayor García and Raymond III of Pallars' (or the Pallars dossier's slug) and a region for that portion.
- `/ledger/5 and /ledger/6` (for the author): 1018 and 1025 lose the same full 40 km circle twice. Evidence: Ledger regions. Fix: 1018: William Isarn's portion only; 1025: the rest.

Gaps for a gap-filler:

- `/ledger/2`: Who held Ribagorza 907-c. 950 and when it was recovered (try https://en.wikipedia.org/wiki/County_of_Ribagorza)
- `/keyframe_review/1-4`: 872-1010 holdings beyond the count lists (budget 5 pages, 4 used) (try https://en.wikipedia.org/wiki/Bernard_I_of_Ribagorza)

### rebellion-of-umar-ibn-hafsun: fix

Area: No Cliopatria row and no infobox area (biography page).

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /keyframe_review/0 confirmed.

Findings:

- `/identity/rulers/1` (applied by reviewer): 'Hafs ibn Umar 917-928' is not what the pages say: three sons continued after 917 and Hafs was the last. Evidence: Ibn Hafsun page: 'his sons Ja'far, 'Abd-ar-Rahman and Hafs tried to continue the resistance'; Abd al-Rahman III page: 'The last of the sons of Ibn Hafsun to fall was Hafs'. Fix: Renamed to 'Sons of Umar ibn Hafsun (Ja'far, Abd al-Rahman, Hafs)', source the Ibn Hafsun page.
- `/identity/capitals/1` (for the author): Advisory, not blocking: Poley (Aguilar de la Frontera, 4.65 W 37.52 N), the capital 885-891, lies outside the 883 keyframe (Málaga, Granada, Jaén). Evidence: Ibn Hafsun page: 'moved his headquarters to the town of Poley'. Fix: Add a small Poley circle to the rebel land for 885-891, or note it.

### banu-qasi: thin

Area: No Cliopatria row and no infobox area.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/6 confirmed; /ledger/7 not on page (on the Banu Qasi page; fixed); /ledger/8 confirmed (d. 929 in the leaders list).

Findings:

- `/ledger/7/source` (applied by reviewer): The 924 loss cites the Abd al-Rahman III page, which does not name Tudela; the quoted words are not on any page. Evidence: Banu Qasi page: 'on his return to Tudela he removed the Banu Qasi and sent them to Córdoba' (the year after 923). Fix: Source set to the Banu Qasi page; quote corrected.
- `/ledger/2` (for the author): 898 is recorded as a gain from emirate-of-cordoba, but the emirate records vassal_start banu-qasi (its /ledger/15) and vassal_end in 924; Tudela was already Banu Qasi land (keyframe 1). Evidence: Banu Qasi page: 'formally recognized the sovereignty of the emir, Abd Allah' for 'the formal governorship over Tudela and Tarazona'. Fix: Add vassal_start emirate-of-cordoba 898 and vassal_end emirate-of-cordoba 924; keep a gain only for Tarazona.
- `/keyframe_review/5` (for the author): Monzón and Lleida (gained 914, /ledger/3) vanish in 924 without a loss, and Ayerbe (Ayera) appears without a gain. Evidence: Keyframes 4 and 5; the note admits 'what became of Monzón' is unknown. Fix: Add confidence-1 events (loss of Monzón and Lleida, gain or retention of Ayera) or keep them in the keyframe.
- `/ledger/0/region` (for the author): The 872 land omits Monzón, which the page says Isma'il and Lubb took in January 872. Evidence: Banu Qasi page: 'the two of them together taking Monzon'. Fix: Add Monzón to the 872 region and keyframe 0.

Gaps for a gap-filler:

- `/ledger/4`: When the Rioja lands (Nájera, Viguera) became Banu Qasi (confidence 1) (try https://en.wikipedia.org/wiki/Banu_Qasi)
- `/ledger/8`: The 929 dissolve names emirate-of-cordoba, which became the caliphate in January 929 (try https://en.wikipedia.org/wiki/Abd_al-Rahman_III)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-asturias 754 gain Fihrid governors of al-Andalus | umayyad-caliphate 750 loss | exception | No dossier for the Fihrid governors (750-756); the Umayyad dossier hands al-Andalus to them in 750. Counterpart corrected from umayyad-caliphate. |
| kingdom-of-asturias 825 gain nobody | emirate-of-cordoba 825 loss | matched | Both sides nobody (Duero belt). |
| kingdom-of-asturias 868 gain emirate-of-cordoba | emirate-of-cordoba 868 loss | matched | Porto. |
| kingdom-of-asturias 878 gain nobody | emirate-of-cordoba 878 loss | matched | Both sides nobody (Viseu). |
| kingdom-of-asturias 879 gain emirate-of-cordoba | emirate-of-cordoba 879 loss | matched | Coimbra, Aveiro. |
| kingdom-of-asturias 910 loss kingdom-of-galicia | none | exception | kingdom-of-galicia: eu-12 part not run yet. |
| kingdom-of-asturias 910 loss kingdom-of-leon | none | exception | kingdom-of-leon not run yet. The eastern lands (/ledger/15, conf 1) include La Rioja, which banu-qasi (914-923) and kingdom-of-pamplona (from 923) also hold: León's dossier must reconcile. |
| kingdom-of-asturias 924 loss kingdom-of-leon | none | exception | Not run yet. |
| emirate-of-cordoba 756 found Fihrid governors of al-Andalus | umayyad-caliphate 750 loss | exception | Counterpart corrected; the 756->757 expansion over the rest of al-Andalus has no event (blocking finding). |
| emirate-of-cordoba 759 loss kingdom-of-the-franks | kingdom-of-the-franks 759 gain | matched | Narbonne/Septimania. |
| emirate-of-cordoba 760 loss kingdom-of-the-franks | none | missing | Roussillon: the Franks' ledger has only a 760 contest_start with Aquitaine (eu-07). |
| emirate-of-cordoba 778 loss rebellious lords of the Upper March | kingdom-of-the-franks 778 gain | mismatch | The Franks (conf 1) gain the 53 Ebro cells from the emirate; the emirate loses them to rebel lords. Agree on one owner (eu-07 and eu-12-a). |
| emirate-of-cordoba 783 gain rebellious lords of the Upper March | kingdom-of-the-franks 783 loss | mismatch | Same disagreement as 778. |
| emirate-of-cordoba 785 loss kingdom-of-the-franks | none | missing | Girona: no Frankish gain (eu-07). |
| emirate-of-cordoba 798 loss kingdom-of-the-franks | none | missing | Urgell and Cerdanya: no Frankish gain (eu-07). |
| emirate-of-cordoba 801 loss kingdom-of-the-franks | kingdom-of-the-franks 801 gain | matched | Barcelona. |
| emirate-of-cordoba 806 loss kingdom-of-the-franks | none | missing | No Frankish gain in 806; duchy-of-gascony /ledger/3 also loses Navarre to the Franks in 806, so two dossiers claim the same land before it. |
| banu-qasi 872 found emirate-of-cordoba | none | missing | The emirate has no 872 loss and keeps Zaragoza in its 870-878 keyframes (blocking finding on the emirate). |
| emirate-of-cordoba 883 loss rebellion-of-umar-ibn-hafsun | rebellion-of-umar-ibn-hafsun 883 found | matched | Málaga, Granada, Jaén. |
| emirate-of-cordoba 884 gain banu-qasi | banu-qasi 884 loss | matched | Zaragoza (but the emirate never lost it: see 872). |
| emirate-of-cordoba 898 vassal_start banu-qasi | banu-qasi 898 gain | mismatch | banu-qasi records a land gain, not vassalage. |
| emirate-of-cordoba 900 loss autonomous lords of al-Andalus | none | exception | Free-text counterpart; not listed as needing a dossier (Banu Hajjaj of Seville, Toledo, Mérida, Badajoz, Murcia). |
| emirate-of-cordoba 903 gain nobody | none | exception | Balearics; the page says Issam al-Khawlani 'defeated the Franks'. |
| emirate-of-cordoba 914 gain rebellion-of-umar-ibn-hafsun | rebellion-of-umar-ibn-hafsun 914 loss | matched | Same region both sides. |
| emirate-of-cordoba 924 vassal_end banu-qasi | banu-qasi 924 loss | mismatch | banu-qasi has a loss to the Tujibids, no vassal_end. |
| emirate-of-cordoba 928 gain rebellion-of-umar-ibn-hafsun | rebellion-of-umar-ibn-hafsun 928 loss | matched | Bobastro. |
| kingdom-of-pamplona 824 found kingdom-of-the-franks | kingdom-of-the-franks 825 loss | matched | Within one year; but duchy-of-gascony /ledger/6 (824 loss to kingdom-of-pamplona, conf 3) is not acknowledged by Pamplona (fix listed). |
| kingdom-of-pamplona 844 vassal_start county-of-aragon | none | missing | county-of-aragon has no vassal_start. |
| kingdom-of-pamplona 914 gain banu-qasi | banu-qasi 914 loss | matched | Arnedo. |
| kingdom-of-pamplona 922 vassal_end county-of-aragon | none | missing | county-of-aragon has no vassal_end. |
| kingdom-of-pamplona 922 gain county-of-aragon | county-of-aragon 922 loss | matched | Absorption. |
| kingdom-of-pamplona 923 gain banu-qasi | banu-qasi 923 loss | mismatch | Same year, different land: Pamplona takes the whole of La Rioja, the Banu Qasi lose a 30 km Nájera-Viguera circle; the rest of La Rioja went to kingdom-of-leon in 910 per kingdom-of-asturias /ledger/15. |
| kingdom-of-pamplona 966 loss caliphate-of-cordoba | none | exception | Not run yet. |
| kingdom-of-pamplona 1015 gain taifa-of-zaragoza | none | exception | Not run yet. |
| kingdom-of-pamplona 1017 vassal_start kingdom-of-castile | none | exception | Not run yet (also 1028 vassal_end and gain, 1035, 1054, 1076 losses). |
| kingdom-of-pamplona 1018 gain county-of-ribagorza | county-of-ribagorza 1018 loss | matched | Land differs: Pamplona adds the Sobrarbe circle it already gained in 1015. |
| kingdom-of-pamplona 1025 gain county-of-ribagorza | county-of-ribagorza 1025 loss | matched | Both sides repeat the 1018 region. |
| kingdom-of-pamplona 1028 gain kingdom-of-leon | none | exception | Not run yet (also 1033, 1034 gains and the 1035 loss). |
| kingdom-of-pamplona 1032 vassal_start duchy-of-gascony | none | missing | duchy-of-gascony (eu-10) has no 1032 vassal_start or 1035 vassal_end. |
| kingdom-of-pamplona 1035 loss county-of-ribagorza | county-of-ribagorza 1035 gain | matched | Sobrarbe and Ribagorza to Gonzalo. |
| kingdom-of-pamplona 1035 vassal_start county-of-ribagorza | none | missing | county-of-ribagorza has no vassal_start (nor the 1045 vassal_end). |
| kingdom-of-pamplona 1035 loss kingdom-of-aragon | none | exception | Not run yet (also 1076). |
| kingdom-of-pamplona 1045 gain taifa-of-zaragoza | none | exception | Calahorra; not run yet. |
| kingdom-of-sobrarbe 825 found nobody | county-of-aragon | mismatch | county-of-aragon owns the same cells 807-829 and kingdom-of-the-franks /ledger/92 gives them to kingdom-of-pamplona in 825: three claimants. |
| kingdom-of-sobrarbe 829 dissolve county-of-aragon | none | missing | county-of-aragon has no matching gain (it already holds the land). |
| county-of-aragon 807 found kingdom-of-the-franks | kingdom-of-the-franks 825 loss | mismatch | The Franks keep these cells until 825 and lose them to kingdom-of-pamplona, not to county-of-aragon. |
| county-of-ribagorza 872 found west-franks | west-franks 872 loss | matched | Raymond I. |
| county-of-ribagorza 907 loss Muhammad al-Tawil of Huesca | none | exception | Listed as needing a dossier (also the 920 gain). |
| county-of-ribagorza 920 split county-of-pallars | none | exception | Not run yet. |
| county-of-ribagorza 1010 split kingdom-of-castile | none | mismatch | Castile took no land; the portion went to Mayor García and Raymond III of Pallars. |
| county-of-ribagorza 1045 loss kingdom-of-aragon | none | exception | Not run yet. |
| banu-qasi 914 gain nobody | none | exception | Monzón and Lleida. |
| banu-qasi 924 loss Tujibids of Zaragoza | none | exception | Listed as needing a dossier. |
| fatimid-caliphate 931 loss emirate-of-cordoba | none | mismatch | fatimid-caliphate /ledger/14 and /ledger/15 (931, 933) name emirate-of-cordoba, which ends in January 929: should be caliphate-of-cordoba (me-08). |

## Counterparts needing dossiers

- Fihrid governors of al-Andalus (Yusuf al-Fihri) (fihrid-governors-of-al-andalus, 750-756): Counterpart of umayyad-caliphate /ledger/93, kingdom-of-asturias /ledger/3 and emirate-of-cordoba /ledger/0; holds Cliopatria's 751-755 'Umayyad' Iberian shapes.
- Banu Hajjaj of Seville (banu-hajjaj-of-seville, 900-913): Seville 'finally capitulated on 20 December 913' (Abd al-Rahman III page); start year not verified.
- Tujibids of Zaragoza (tujibids-of-zaragoza, 886-929)
- Muhammad al-Tawil of Huesca (muhammad-al-tawil-of-huesca, 907-911)
- Ibn Marwan's Badajoz (banu-marwan-of-badajoz, 922-930)
- County of Castile before 961 (county-of-castile, 850-961)

## Problems for the orchestrator

- kingdom-of-sobrarbe: the Cliopatria 'Kingdom of Sobrarbe' row (825-829) is legend (Sobrarbe page) and double-draws the County of Aragon's cells; the orchestrator should drop it or merge it into county-of-aragon. kingdom-of-the-franks /ledger/92 gives the same cells to kingdom-of-pamplona in 825 (eu-07).
- Cliopatria 'County of Ribagorza' (866-1084) is Pamplona/Navarre; kingdom-of-pamplona's new keyframes replace it. kingdom-of-navarre (another eu-12 part, same Wikidata id) should start at the 1134 restoration; the merge decision is the orchestrator's.
- kingdom-of-the-franks (eu-07): missing gains for Roussillon 760, Girona 785, Urgell/Cerdanya 798 and Navarre 806; 778/783 Ebro counterpart disagrees with the emirate; the 825 loss of the Aragon/Sobrarbe cells to kingdom-of-pamplona disagrees with county-of-aragon.
- duchy-of-gascony (eu-10): no 1032 vassal_start / 1035 vassal_end with kingdom-of-pamplona; its 806 loss of Navarre to the Franks overlaps emirate-of-cordoba's 806 loss of the same belt.
- fatimid-caliphate (me-08) /ledger/14 and /ledger/15 name emirate-of-cordoba in 931 and 933; the emirate ends in January 929 (caliphate-of-cordoba).
- La Rioja is claimed by kingdom-of-asturias to 910 then (conf 1) kingdom-of-leon, by banu-qasi (Nájera, Viguera 914-923) and by kingdom-of-pamplona from 923: the kingdom-of-leon author must reconcile.
- Reviewer edits applied in place and re-validated (0 errors, 0 warnings): kingdom-of-asturias (Bermudo I; 754 counterpart), emirate-of-cordoba (found counterpart; 922 confidence 1 and quote attribution; keyframe 18 note; 924 source), kingdom-of-pamplona (three ruler entries), rebellion-of-umar-ibn-hafsun (ruler name), banu-qasi (924 source).
- No page failed to load for the reviewer.

## Gazetteer names wanted (the dossiers use lon/lat circles meanwhile)

Ribagorza, Sobrarbe, Benabarre, Aínsa, Arán valley, Cerdanya, Urgell, Upper March, Nájera, Viguera, Calahorra, Tudela, Tarazona, Monzón, Lleida, Arnedo, Albelda, Ayerbe, Bobastro, Reyyo, Elvira, Poley (Aguilar de la Frontera), Guadix, Pechina, Algeciras, La Bureba, Pisuerga, Cea, Osma, San Esteban de Gormaz, Cangas de Onís, Ansó, Echo, Canfranc.
