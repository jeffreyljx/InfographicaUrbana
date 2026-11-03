# Review: batch eu-12-d (Caliphate of Córdoba, Kingdom of León, Kingdom of Castile)

Reviewed 2026-10-25 by the Phase B adversarial reviewer. Machine copy: history/notes/phase-b/reviews/eu-12-d.json. All three dossiers validate with --resolve (0 errors, 0 warnings). Spot checks were weighted to confidence-3 events and the largest moves; every event checked said what its note claims, with the year, except where listed below.

## Verdicts

- caliphate-of-cordoba: **fail** (two blocking findings on the African side; one small fix applied by the reviewer).
- kingdom-of-leon: **fix** (author to make the listed fixes; thin items for a gap-filler).
- kingdom-of-castile: **fix** (author to make the listed fixes; thin items for a gap-filler).

## The León-Castile union

 Union decision (asked for in the author's notes): 1038-1065 is drawn per crown, not as one Castile shape. Castile was a county until 1065 (Kingdom of Castile infobox 'Established: 1065'; the Castile dossier's own /ledger/10 rename), Ferdinand I was crowned king in León on 22 June 1038, Cliopatria itself draws León and Castile apart under the same king in 1040-1045, no page dates any change in 1046 (both 1046 events are confidence 1), and taifa-of-badajoz already names kingdom-of-leon for the Mondego. 1072-1125 and 1139-1157 keep Cliopatria's allocation (Castile row), as both dossiers now do; neighbours that name kingdom-of-leon in those years (almoravid-dynasty 1094) rename to kingdom-of-castile. 1126-1138 stays León as drawn.

## caliphate-of-cordoba (fail)

### Findings

- `/ledger/9` (applied by reviewer): Confidence 3 on a region the page does not name (the 973 contest zone is the Moroccan and western Algerian part of the 980 shape).
  - Evidence: Almanzor page: 'In 973, he undertook the logistical, administrative and diplomatic aspects of the caliphal campaign against the Idrisids' - no land named.
  - Fix: Lowered to 2 by the reviewer; dossier re-validated (0 errors, 0 warnings).
- `/ledger/11` (applied by reviewer): Confidence 3 on a region the page does not name (974 contest_end, same zone).
  - Evidence: Almanzor page: 'Achieving victory against the Idrisids, Ibn Abi Amir returned sick to the Cordoban court in September 974' - no land named.
  - Fix: Lowered to 2 by the reviewer; dossier re-validated.
- `/keyframe_review/2/correction, /keyframe_review/3/correction, /keyframe_review/4/correction, /keyframe_review/5`: [blocking] Ceuta (gained 931, /ledger/2) and Tangier (gained 951, /ledger/8) are never lost in the ledger but are missing from every keyframe from 932 to 979; only the 980, 990 and 1010 corrections add them back, and the 961 verdict says the shape "correctly shows no Africa".
  - Evidence: shapes.csv: the 936, 947 and 961 shapes end at 36.03 N (Ceuta 35.89 N, Tangier 35.77 N) and the corrections are the bare Iberian shapes. Caliphate page: 'Abd al-Rahman III secured Melilla in 927, Ceuta in 931, and Tangier in 951'; the Almanzor page has troops sent to hold Ceuta in September 979, so it stayed caliphal.
  - Fix: Add {'admin1':'Ceuta','country':'Spain'} to the 932, 936, 947 and 961 corrections (text: Ceuta from 931); add the Tangier 60 km circle to 961 and to 947 (text: from 951); 961 becomes adjust. Consider Melilla (927, same sentence) in the founding region and keyframes.
- `/ledger (after /ledger/8); /keyframe_review/4; /keyframe_review/5; /wars/1`: [blocking] The occupation of northern Morocco from 949 to 958 is missing, although the page opened says so and fatimid-caliphate already gives that land to this state.
  - Evidence: Caliphate page: 'The Umayyads besieged Tangier in 949 and defeated Abul-Aish, forcing him to retreat ... and then occupied the rest of northern Morocco.' The dossier's own 961 note quotes the Abd al-Rahman III page: influence 'disappeared after a Fatimid offensive in 958'. fatimid-caliphate /ledger/20: 948 loss to caliphate-of-cordoba, 'Morocco outside the Rif and Jbala country' (c2). With no event here that land has no holder on the map 948-958.
  - Fix: Add a 949 vassal_start (or gain, if read as direct rule) of northern Morocco, counterpart as the page names it (the Idrisids of Abul-Aish / the Zenata clients), region the Morocco-only spec used for the 974 tint, conf 2, source Caliphate_of_Cordoba; close it in 958 (vassal_end or loss, counterpart fatimid-caliphate, source Abd_al-Rahman_III); add the zone to /wars/1. me-08 should add the 958 recovery to fatimid-caliphate.
- `/ledger/12, /ledger/13`: [non-blocking] The September 979 relief of Ceuta is recorded as an occupation pair with fatimid-caliphate, i.e. as this state occupying Fatimid land; Ceuta was already this state's own land (/ledger/2), the second event is a confidence-1 filler and the note says nothing changes on the map.
  - Evidence: Schema: 'occupation_start / occupation_end: this state occupies region belonging to counterpart without annexing it'. Almanzor page: 'In September 979, he sent troops from Algeciras to the aid of Ceuta', threatened by Buluggin ibn Ziri - a defence, not an occupation. fatimid-caliphate has no 979 event.
  - Fix: Delete both events (mention the relief in the note of /wars/1 or /wars/2), or, if a page shows Buluggin taking ground, record a contest pair over that ground with the Zirid/Fatimid counterpart.
- `/ledger/9, /ledger/10, /ledger/11, /ledger/29, /wars/2/zones/0`: [non-blocking] The client tint and contest zone include western Algeria (and Morocco south to 31.3 N), contrary to the dossier's own notes ("nothing supports Algeria").
  - Evidence: Caliphate page: 'much of northern Morocco also came directly within the sphere of influence'; 'By 974, Al-Hassan II was taken to Córdoba, and the remaining Idrisids recognized Umayyad rule' - Morocco only.
  - Fix: Use {'intersect':[{'cliopatria':'Caliphate of Córdoba','year':980},{'country':'Morocco'}]} (or a northern-Morocco region) in these five places and in the new 949-958 events.
- `/keyframe_review/7; /ledger (990); /wars/3/outcome`: [non-blocking] Cliopatria's 990 shape is 11,512 km2 larger than the 980 shape (the Mondego: Coimbra, Aveiro) and kingdom-of-leon /ledger/7 loses exactly that land to this state in 990, but this ledger has no gain between 980 and 990, and /wars/3 says the campaigns "took no land".
  - Evidence: shapes.csv 980 553,201.6 vs 990 564,713.5 km2 (Africa unchanged); Leon 961 144,144.6 vs 990 132,744.8 km2; kingdom-of-leon /ledger/7 (990 loss, counterpart caliphate-of-cordoba, c1).
  - Fix: Add a 990 gain from kingdom-of-leon with Leon's /ledger/7 region, conf 1 (987 for Coimbra if a page dates it), and correct /wars/3 (zone: the Mondego; outcome: Coimbra and the Mondego held from 987/990).
- `/ledger (931, 934)`: [non-blocking] No mirror of emirate-of-nekor /ledger/4 (931 vassal_start, counterpart caliphate-of-cordoba, 'the Umayyad's vassal') and /ledger/7 (934 vassal_end).
  - Evidence: Schema: in vassal events the counterpart is the vassal itself; the overlord records vassal_start/vassal_end naming emirate-of-nekor.
  - Fix: Add vassal_start 931 and vassal_end 934, counterpart emirate-of-nekor, region Nekor, conf as the Nekor dossier (2/1), citing its page; or tell af-02 the Nekor events are wrong.
- `/ledger (966)`: [non-blocking] No mirror of kingdom-of-pamplona /ledger/6 (966 loss of Calahorra and the Cidacos valley to caliphate-of-cordoba, c3).
  - Evidence: kingdom-of-pamplona ledger read; this ledger has no event between 951 and 973.
  - Fix: Add a 966 gain of Calahorra from kingdom-of-pamplona citing the Pamplona dossier's page, or record the disagreement in notes.
- `/keyframe_review/8/correction`: [non-blocking] The 1010 correction already removes Murcia and Almería, whose losses the ledger dates 1011 (/ledger/20, /ledger/21).
  - Evidence: Correction 'minus' Murcia and Almería with text 'applied by the 1011-1013 events'.
  - Fix: Keep Murcia and Almería in the 1010 keyframe and let the 1011 events remove them, or redate the events.

### Thin (for a gap-filler)

- `/ledger/15, /ledger/16, /ledger/17`: Badajoz, Toledo and Tortosa taifa years (conf 1); the Taifa page lists no date (https://en.wikipedia.org/wiki/Taifa_of_Toledo)
- `/ledger/29`: the year the Moroccan clients fell away (bridge 1015, conf 1) and the loss of Ceuta (https://en.wikipedia.org/wiki/Hammudid_dynasty)
- `/ledger/13`: conf-1 filler (see fixes: delete) (https://en.wikipedia.org/wiki/Buluggin_ibn_Ziri)
- `/keyframe_review/9-11`: the Mértola/Beja strip in the 1018-1033 shapes is undated (https://en.wikipedia.org/wiki/Taifa_of_Mértola)

### Spot checks

- `/ledger/1`: confirmed ('the surrender of Ibn Marwan of Badajoz in 930') (https://en.wikipedia.org/wiki/Abd_al-Rahman_III)
- `/ledger/3`: confirmed ('surrendered on 2 August 932, after a siege of two years') (https://en.wikipedia.org/wiki/Abd_al-Rahman_III)
- `/ledger/8`: confirmed (Tangier 951; the same passage has the 949-958 occupation the dossier omits) (https://en.wikipedia.org/wiki/Caliphate_of_Cordoba)
- `/ledger/9, /ledger/11`: confirmed (973 campaign; return September 974); region not named on page -> conf lowered to 2 (https://en.wikipedia.org/wiki/Almanzor)
- `/ledger/10`: confirmed ('By 974 ... the remaining Idrisids recognized Umayyad rule') (https://en.wikipedia.org/wiki/Caliphate_of_Cordoba)
- `/ledger/12`: confirmed date (September 979); event type misused (https://en.wikipedia.org/wiki/Almanzor)
- `/ledger/4, /ledger/6, /ledger/7`: confirmed (937 Zaragoza, Simancas 939, peace with Ordoño III 951) (https://en.wikipedia.org/wiki/Abd_al-Rahman_III)

Area: No infobox area on the page; body: 'Around 1000 CE, the caliphate occupied some four hundred thousand square kilometers'. Ratio 0.71 with Africa, 1.08 against the author's corrected 369,491 km2; acknowledged in /keyframe_review/7.

## kingdom-of-leon (fix)

### Findings

- `/ledger/8; /keyframe_review/10; new keyframe kingdom-of-leon_1046`: [required] Union years 1046-1065 are drawn as Castile, leaving León with no land for twenty years (see the union decision).
  - Evidence: Union decision (asked for in the author's notes): 1038-1065 is drawn per crown, not as one Castile shape. Castile was a county until 1065 (Kingdom of Castile infobox 'Established: 1065'; the Castile dossier's own /ledger/10 rename), Ferdinand I was crowned king in León on 22 June 1038, Cliopatria itself draws León and Castile apart under the same king in 1040-1045, no page dates any change in 1046 (both 1046 events are confidence 1), and taifa-of-badajoz already names kingdom-of-leon for the Mondego.
  - Fix: Drop /ledger/8 (1046 loss to Castile, c1). Add keyframe kingdom-of-leon_1046 (1046-1065) = the León 1040 shape plus Lamego (Nov 1057), Viseu (Jul 1058) and Coimbra (Jul 1064) from their dates; move Castile's /ledger/5, /ledger/6, /ledger/9 here as gains from taifa-of-badajoz (taifa-of-badajoz /ledger/4-7 already name kingdom-of-leon); replace /ledger/9 (1065/12 gain from Castile) by a 1065/12 loss of Galicia and the Portuguese lands to kingdom-of-galicia (moved from Castile /ledger/12). The Toledo parias (1062) go with the crown the Ferdinand I page gives them to in 1065.
- `/keyframe_review/8; /ledger (1028-1035)`: [non-blocking] No mirror of kingdom-of-pamplona /ledger/13 (1028 gain of the Pisuerga-Cea land from kingdom-of-leon, c2), /ledger/15 (1033/3 Zamora and the west, c3), /ledger/16 (1034 the city of León, c3) and /ledger/19 (1035 loss back to León); the dossier keeps the 1010 shape unchanged to 1037.
  - Evidence: This dossier's own page, Kingdom of León: 'Sancho III of Navarre (1004-1035) took over Castile in the 1020s, and managed León in the last year of his life' (the author quoted only the first half).
  - Fix: Add a 1034 loss (or occupation pair) of the city of León and the west to kingdom-of-pamplona and a 1035 recovery on Sancho's death (18 October 1035), conf 2, Kingdom_of_Le%C3%B3n; add the 1028 Pisuerga-Cea loss at conf 1 citing the Pamplona dossier's page, or ask eu-12-a to lower its 1033 event. Make kingdom-of-leon_1034 adjust accordingly.
- `/keyframe_review/12; /ledger/12`: [non-blocking] 1126-1138: the León 1126 shape holds the Portuguese lands that county-of-portugal draws as its own land from 1096 (overlap on the map); this dossier gives them up only in 1139 (conf 1).
  - Evidence: county-of-portugal: found 1096, keyframe county-of-portugal_1096 (1096-1138, adjust); the eu-12-i review asks that dossier for a dependency on León. Alfonso VII page: Portugal 'recognized as independent de jure in 1143'.
  - Fix: Mark kingdom-of-leon_1126 adjust minus the county's land (county-of-portugal_1139 shape) and record the county as a vassal: vassal_start 1126/3 (inherited) and vassal_end 1143, counterpart county-of-portugal; drop /ledger/12.
- `/ledger/16`: [non-blocking] almohad-caliphate /ledger/35 gains Trujillo and Montánchez (Cáceres) from kingdom-of-leon in 1195 (c2), inside León's 1188 shape, but León loses its Extremadura cells only in 1202 (conf 1).
  - Evidence: almohad-caliphate ledger read; Leon /ledger/15-16 are both conf-1 bridges on Cliopatria years.
  - Fix: Redate /ledger/16 to 1195-1196 (after Alarcos) to agree with the Almohad gain, or have af-02 change its counterpart; say which in notes.
- `/ledger/18/region`: [non-blocking] The 1230 merge region is the León 1227 shape, which /keyframe_review/19 itself corrects to the 1202 shape; the dissolve (/ledger/19) and Castile's merge (/ledger/44 there) use the 1202 shape plus Mérida and Badajoz.
  - Evidence: /keyframe_review/19 correction: the 1202 shape for 1227-1229.
  - Fix: Use /ledger/19's region in /ledger/18.
- `/wars/1/zones`: [non-blocking] Almanzor's campaigns have no zone, but /ledger/7 loses the Mondego to the Caliphate in that war.
  - Evidence: Rule 10: empty zones only where no ground changed hands.
  - Fix: Add the /ledger/7 region as the zone.

### Thin (for a gap-filler)

- `/identity/rulers`: rulers omitted (fetch kept only some reigns) (https://en.wikipedia.org/wiki/List_of_Leonese_monarchs)
- `/ledger/7`: the Mondego loss is conf 1 and dated by Cliopatria (Coimbra fell to Almanzor in 987) (https://en.wikipedia.org/wiki/Coimbra)
- `/ledger/15, /ledger/16; /keyframe_review/15`: Extremadura 1188-1201 (Cáceres) unverified; conf-1 bridges (https://en.wikipedia.org/wiki/Ferdinand_II_of_Le%C3%B3n)
- `/wars/4`: the 1205/1207/1209 treaties ceded territory to Castile; no land named (https://en.wikipedia.org/wiki/Berengaria_of_Castile)
- `/ledger/12, /ledger/13`: 1139 transfers are conf-1 bookkeeping on Cliopatria's re-drawing (no event that year) (https://en.wikipedia.org/wiki/Alfonso_VII_of_Le%C3%B3n_and_Castile)

### Spot checks

- `/ledger/1`: confirmed ('When García died in 914 ... ruled both León and Galicia') (https://en.wikipedia.org/wiki/Kingdom_of_Le%C3%B3n)
- `/ledger/3`: confirmed ('The County of Castile split off in 931') (https://en.wikipedia.org/wiki/Kingdom_of_Le%C3%B3n)
- `/ledger/5`: confirmed (Simancas 939; 'advance of the Leonese border of the Duero to the Tormes', undated: conf 2 right) (https://en.wikipedia.org/wiki/Ramiro_II_of_Le%C3%B3n)
- `/ledger/17`: confirmed ('capturing Mérida and Badajoz in 1230') (https://en.wikipedia.org/wiki/Alfonso_IX_of_Le%C3%B3n)
- `/ledger/18, /ledger/19`: confirmed ('Permanent union of Castile and León: 10 December 1230') (https://en.wikipedia.org/wiki/Kingdom_of_Le%C3%B3n)
- `/keyframe_review/8`: page says Sancho III 'managed León in the last year of his life'; dossier quotes only the Castile half (https://en.wikipedia.org/wiki/Kingdom_of_Le%C3%B3n)

Area: The Kingdom of León page gives no area (infobox or body); the author says so in /keyframe_review/0. Shapes 59,553-192,464 km2 are plausible for the kingdom.

## kingdom-of-castile (fix)

### Findings

- `/ledger/3; /ledger/5; /ledger/6; /ledger/9; /ledger/11; /ledger/12; /keyframe_review/5`: [required] Union years 1046-1065 are drawn as one Castile shape: León and Galicia are labelled with the County of Castile, which became a kingdom only in 1065 (this dossier's own /ledger/10).
  - Evidence: Union decision (asked for in the author's notes): 1038-1065 is drawn per crown, not as one Castile shape. Castile was a county until 1065 (Kingdom of Castile infobox 'Established: 1065'; the Castile dossier's own /ledger/10 rename), Ferdinand I was crowned king in León on 22 June 1038, Cliopatria itself draws León and Castile apart under the same king in 1040-1045, no page dates any change in 1046 (both 1046 events are confidence 1), and taifa-of-badajoz already names kingdom-of-leon for the Mondego.
  - Fix: Drop /ledger/3 (1046 gain, c1). /keyframe_review/5 becomes adjust: correction = the Castile 1040 shape plus La Bureba (Sept 1054). Move /ledger/5, /ledger/6, /ledger/9 (Lamego, Viseu, Coimbra) to kingdom-of-leon. Drop /ledger/11 (1065/12 loss to León) and move /ledger/12 (loss of Galicia) to León. 1060 Zaragoza parias stay with Castile (Sancho II's share).
- `/ledger/42; /keyframe_review/21; /keyframe_review/22; /keyframe_review/23; /keyframe_review/24`: [non-blocking] Baeza and Úbeda are drawn as Castilian from July 1212 to 1235, but the page cited says Baeza was evacuated after the battle, and the Ferdinand III page (also opened) dates Úbeda to 1233 and has Castile occupying Baeza only in 1225 (/ledger/43 gains Baeza a second time with no loss between). /keyframe_review/22 marks the 1216 shape (northern Jaén 32 of 54 cells) ok while quoting that 1225 sentence.
  - Evidence: Las Navas de Tolosa page: 'Shortly after the battle, the Castilians took Baeza and then conquered Úbeda'; 'Baeza was evacuated and its people moved to Úbeda'; 'Alfonso laid siege, killing 60,000 Muslims and enslaving many more.' Ferdinand III page: 'Cazorla in 1231, Úbeda in 1233'; 'the Castilians remained in occupation of al-Bayyasi's holdings in Andújar, Baeza and Martos' (1225).
  - Fix: Replace /ledger/42 by a 1212 contest_start/contest_end pair over Baeza and Úbeda (or drop it); remove the two circles from the 1212 correction; mark 1216 and 1227 adjust (northern Jaén out until the 1225 gain); add gains Cazorla 1231 and Úbeda 1233 (Ferdinand III page, conf 3) and show them in /keyframe_review/24. Tell af-02 to recast almohad-caliphate /ledger/39 (1212 loss, c3) the same way.
- `/ledger/25; /keyframe_review/8; /keyframe_review/9`: [non-blocking] Lisbon, Sintra and Santarém are lost in November 1094 but were never gained: no 1093 event, and the 1085 and 1094 shapes end at 39.45 N (Santarém 39.24 N, Lisbon 38.72 N).
  - Evidence: Alfonso VI page: 'As the price for this alliance, Alfonso VI had obtained Lisbon, Sintra, and Santarém, but lost them in November 1094'. shapes.csv bbox of kingdom-of-castile_1085 and _1094: south 39.4496.
  - Fix: Add a 1093 gain of the same region from taifa-of-badajoz (the cession; conf 2 on this page, the year from a page that dates it), and note in /keyframe_review/8 that the 1093-1094 cession sits on top of the shape.
- `/ledger/31/region`: [non-blocking] Santarém is lost twice: to the Almoravids in November 1094 (/ledger/25) and again to the County of Portugal in 1111.
  - Evidence: /ledger/25 region includes the Santarém 50 km circle; /ledger/31 region includes it again with no gain in between.
  - Fix: Remove the Santarém circle from /ledger/31 (and see the next finding on the year).
- `/ledger/31; /keyframe_review/9; /keyframe_review/10`: [non-blocking] The Portuguese lands stay in Castile to 1111 (conf 1, Cliopatria) while county-of-portugal holds them from 1096: overlap on the map 1096-1110.
  - Evidence: county-of-portugal /ledger/0: found 1096 (counterpart kingdom-of-galicia, which in 1096 was part of Alfonso VI's realm, i.e. this dossier). Alfonso VI page: 'he gave Henry and Teresa the government of the County of Portugal'.
  - Fix: Move /ledger/31 to 1096 (loss, or vassal_start of county-of-portugal per the eu-12-i decision that the county was a dependency) and mark the 1094 and 1099 keyframes adjust minus the county from 1096; ask eu-12 to change the county's founding counterpart to kingdom-of-castile.
- `/ledger/20; /ledger/34`: [non-blocking] Coria is gained twice (1079 from taifa-of-badajoz, 1142 from almoravid-dynasty) with no loss between.
  - Evidence: Alfonso VI page: 'In 1079, he conquered Coria.' Alfonso VII page: 'In 1142, Alfonso besieged Coria a second time and took it.'
  - Fix: Add a conf-1 loss of Coria to almoravid-dynasty in the Urraca years (bridge; a page that dates it would raise it), and check that the 1111 and 1139 keyframes agree.
- `/ledger (1017-1028; 1134-1136; 1157; 1173-1177; 1199-1200)`: [non-blocking] Missing mirrors of neighbour events: kingdom-of-pamplona /ledger/8 (1017 vassal_start, Castile as vassal, c3) and /ledger/11 (1028 vassal_end); kingdom-of-navarre /ledger/1 (1135 Zaragoza as Castile's fief), /ledger/2 (1136 La Rioja surrendered to Castile, c3 - this ledger never loses La Rioja to Aragon), /ledger/6 (1157 Artajona returned), /ledger/7-8 (1173-1177 contest over Rioja and Bureba) and /ledger/9, /ledger/11 (1199-1200 contest).
  - Evidence: Neighbour ledgers read; none has a counterpart event here.
  - Fix: Add vassal_start/vassal_end 1017-1028 (counterpart kingdom-of-pamplona); the loss of La Rioja to Alfonso I of Aragon and its recovery 1134-1136 (Urraca years, see thin); the 1173-1177 and 1199-1200 contest pairs; or say in notes which neighbour events are wrong.
- `/keyframe_review/22`: [non-blocking] almohad-caliphate /ledger/40 loses to Castile in 1216 (conf 1) the cells Cliopatria's 1216 shape adds, but this ledger has no 1216 event; the +39,400 km2 is unexplained.
  - Evidence: shapes.csv: 1202 116,987 km2, 1216 156,417 km2; no ledger event in 1213-1224.
  - Fix: Add a conf-1 1216 gain from almohad-caliphate for the non-Jaén part (Albacete, southern Cuenca) mirroring the Almohad event, until a page dates Alcaraz (1213) and the rest.

### Thin (for a gap-filler)

- `/wars/5; 1109-1126`: Urraca's reign: the wars with Alfonso I of Aragon, his hold on La Rioja and the eastern march (zones empty) (https://en.wikipedia.org/wiki/Urraca_of_Le%C3%B3n_and_Castile)
- `/keyframe_review/22`: the 1216 increment: Alcaraz (1213), southern Cuenca, the Córdoba cells (https://en.wikipedia.org/wiki/Alcaraz)
- `/identity/rulers`: rulers omitted (https://en.wikipedia.org/wiki/List_of_Castilian_monarchs)
- `/ledger/41; /keyframe_review/14`: the Calatrava step (1147) and its 1212 restoration are conf 1 (https://en.wikipedia.org/wiki/Calatrava_la_Vieja)
- `/ledger/17, /ledger/23, /ledger/24`: Zaragoza and Granada paria ends 1076/1086 are conf 1 (https://en.wikipedia.org/wiki/Taifa_of_Zaragoza)
- `/ledger/45`: 1235 end into crown-of-castile is Cliopatria's year (conf 1); the pages date the union 1230 (https://en.wikipedia.org/wiki/Crown_of_Castile)

### Spot checks

- `/ledger/0`: confirmed ('In 931 the county was reunified by Count Fernán González') (https://en.wikipedia.org/wiki/Kingdom_of_Castile)
- `/ledger/1`: confirmed ('García was assassinated in 1028 while in León') (https://en.wikipedia.org/wiki/Kingdom_of_Castile)
- `/ledger/10`: confirmed (infobox 'Established: 1065') (https://en.wikipedia.org/wiki/Kingdom_of_Castile)
- `/ledger/21`: confirmed ('finally fell on 25 May 1085') (https://en.wikipedia.org/wiki/Alfonso_VI_of_Le%C3%B3n_and_Castile)
- `/ledger/25`: confirmed ('lost them in November 1094'); the prior gain is missing (https://en.wikipedia.org/wiki/Alfonso_VI_of_Le%C3%B3n_and_Castile)
- `/ledger/28`: confirmed (evacuation 'in March and April' 1102) (https://en.wikipedia.org/wiki/Alfonso_VI_of_Le%C3%B3n_and_Castile)
- `/ledger/20`: confirmed ('In 1079, he conquered Coria') (https://en.wikipedia.org/wiki/Alfonso_VI_of_Le%C3%B3n_and_Castile)
- `/ledger/16`: annexation of Álava, Vizcaya, part of Guipúzcoa and La Bureba is on the page but undated; 1076 at conf 2 acceptable (https://en.wikipedia.org/wiki/Alfonso_VI_of_Le%C3%B3n_and_Castile)
- `/ledger/42`: taking confirmed, holding not: 'Baeza was evacuated'; Ferdinand III page dates Úbeda 1233 (https://en.wikipedia.org/wiki/Battle_of_Las_Navas_de_Tolosa)
- `/ledger/43`: confirmed (1225, Andújar, Baeza and Martos) (https://en.wikipedia.org/wiki/Ferdinand_III_of_Castile)
- `/ledger/44`: confirmed (Benavente, 11 December 1230) (https://en.wikipedia.org/wiki/Ferdinand_III_of_Castile)

Area: The Kingdom of Castile infobox gives no area (status entries only). No figure to compare.

## Cross-dossier mismatches and missing mirrors

- emirate-of-nekor 931 vassal_start -> caliphate-of-cordoba: **missing**. no 931-934 vassal pair in the Caliphate
- fatimid-caliphate 948 loss -> caliphate-of-cordoba: **missing**. Morocco outside the Rif and Jbala: the Caliphate has no 948/949 gain or vassal_start and no 958 end (blocking finding); the Fatimid side also lacks a 958 recovery
- caliphate-of-cordoba 951 gain -> idrisids: **missing**. idrisids (af-02) has no 951 Tangier loss
- kingdom-of-pamplona 966 loss -> caliphate-of-cordoba: **missing**. Calahorra (pamplona /ledger/6, c3); no Caliphate gain
- caliphate-of-cordoba 974 vassal_start -> idrisids: **mismatch** (mirror idrisids 974 loss). idrisids records a loss and dissolves into the Caliphate in 974; the Caliphate keeps a vassal tint of "idrisids" to 1015 (vassal of a dissolved state). One side must give; the Caliphate page supports clients ("the remaining Idrisids recognized Umayyad rule")
- caliphate-of-cordoba 979 occupation_start -> fatimid-caliphate: **missing**. no Fatimid 979 event; recommended deletion (Ceuta was the Caliphate's own land)
- kingdom-of-leon 990 loss -> caliphate-of-cordoba: **missing**. the Mondego; no Caliphate gain although its 990 shape grows by the same 11.5k km2
- kingdom-of-pamplona 1028 gain -> kingdom-of-leon: **missing**. Pisuerga-Cea land; no Leon loss
- kingdom-of-pamplona 1034 gain -> kingdom-of-leon: **missing**. 1033/3 and 1034 gains and the 1035 loss back have no Leon mirror; the Leon page says Sancho "managed León in the last year of his life", so Leon should add them
- taifa-of-badajoz 1055 loss -> kingdom-of-leon: **mismatch** (mirror kingdom-of-castile 1057 gain). Badajoz names León (1055 Mondego; 1064 Coimbra), Castile carries Lamego 1057, Viseu 1058, Coimbra 1064; resolved by moving the three gains to León (union decision); Badajoz should split its 1055 loss by the page dates
- almoravid-dynasty 1094 gain -> kingdom-of-leon: **mismatch** (mirror kingdom-of-castile 1094 loss). same land and month; the 1072-1125 union is in the Castile dossier, so almoravid-dynasty should name kingdom-of-castile
- kingdom-of-leon 1139 loss -> county-of-portugal: **mismatch** (mirror county-of-portugal 1096 found). the county founds in 1096 and holds the land throughout; Leon 1126-1138 and Castile 1096-1110 overlap it
- almohad-caliphate 1195 gain -> kingdom-of-leon: **missing**. Trujillo and Montánchez; Leon loses Extremadura only in 1202
- kingdom-of-leon 1230 gain -> almohad-caliphate: **missing**. almohad-caliphate has no 1230 loss of Mérida and Badajoz
- kingdom-of-pamplona 1017 vassal_start -> kingdom-of-castile: **missing**. Castile as Pamplona's vassal 1017-1028 (c3); no Castile pair
- kingdom-of-castile 1057 gain -> taifa-of-badajoz: **mismatch** (mirror taifa-of-badajoz 1055 loss). see the 1055 row: counterpart and two years apart; move to León
- kingdom-of-castile 1064 gain -> taifa-of-badajoz: **mismatch** (mirror taifa-of-badajoz 1064 loss). same month; Badajoz names León; move to León
- kingdom-of-castile 1079 gain -> taifa-of-badajoz: **missing**. taifa-of-badajoz has no 1079 Coria loss
- kingdom-of-castile 1094 loss -> almoravid-dynasty: **mismatch** (mirror almoravid-dynasty 1094 gain). almoravid names kingdom-of-leon; Castile also lacks the 1093 gain from taifa-of-badajoz
- kingdom-of-castile 1102 loss -> almoravid-dynasty: **missing**. almoravid-dynasty has no 1102 Valencia gain
- kingdom-of-castile 1111 loss -> county-of-portugal: **mismatch** (mirror county-of-portugal 1096 found). county founds 1096 from kingdom-of-galicia; overlap 1096-1110
- kingdom-of-navarre 1135 gain -> kingdom-of-castile: **missing**. Zaragoza as Castile's fief; no Castile event
- kingdom-of-navarre 1136 loss -> kingdom-of-castile: **missing**. La Rioja surrendered to Castile (c3); Castile never lost it to Aragon in its ledger
- kingdom-of-castile 1142 gain -> almoravid-dynasty: **missing**. no Almoravid loss of Coria; Castile also lacks the earlier loss
- kingdom-of-navarre 1157 gain -> kingdom-of-castile: **missing**. Artajona returned; no Castile event
- kingdom-of-navarre 1173 contest_start -> kingdom-of-castile: **missing**. 1173-1177 contest over Rioja and Bureba; no Castile pair
- kingdom-of-castile 1186 gain -> kingdom-of-navarre: **missing**. kingdom-of-navarre has no 1186 loss (its 1177 contest_end says the land was confirmed Castilian)
- kingdom-of-castile 1195 loss -> almohad-caliphate: **mismatch** (mirror almohad-caliphate 1195 gain). the Almohad 1195 gain names kingdom-of-leon (Trujillo, Montánchez); no Almohad gain of the Calatrava country from Castile
- almohad-caliphate 1216 loss -> kingdom-of-castile: **missing**. conf 1 on both sides would do; Castile has no 1216 event
- county-of-ribagorza 1010 split -> kingdom-of-castile: **mismatch**. Ribagorza names Castile in a 1010 split; Castile has no 1010 event (already flagged by the eu-12-a review)

Matched pairs and exceptions are in the JSON copy.

## Routing

- Routing to groups that have run: af-02 idrisids (951 Tangier loss; 974 loss vs vassal tint), af-02 almohad-caliphate (1195 counterpart; 1212 Baeza/Úbeda c3 contradicted; 1212 Calatrava; 1230 Mérida and Badajoz loss to León), af-02 almoravid-dynasty (1094 counterpart -> kingdom-of-castile; 1102 Valencia gain; Coria gain c.1113 and 1142 loss), af-02 emirate-of-nekor (931-934 vassal: Caliphate to add), me-08 fatimid-caliphate (958 recovery of Morocco; nothing for 979), eu-12 taifa-of-badajoz (1055 loss split by dates; 1079 Coria; 1093 cession of Lisbon, Sintra, Santarém), eu-12 kingdom-of-navarre (1186 loss of part of La Rioja), eu-12 county-of-portugal (founding counterpart in 1096 = kingdom-of-castile), eu-12 kingdom-of-pamplona (keep 1034-1035; León adds the mirrors), eu-12 kingdom-of-galicia not yet written (end 914).
