# Review of batch eu-12-x (Iberia additions)

Reviewer eu-12-x, 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-12-x.json.

Mechanical: all 13 dossiers validate with 0 errors; --resolve warnings are only gazetteer gaps (Lleida, Graus, Monzón, Barbastro, Albarracín, Ciudad Real, Alcañiz, Monfragüe, Mértola). None has a Cliopatria row, so every keyframe is new (adjust) and the area check is against infobox figures (only Gibraltar has one) or neighbouring Cliopatria shapes.

## Verdicts

### taifa-of-malaga: pass

Spot checks: /ledger/1 confirmed ('annexed Algeciras to the taifa of Málaga in 1035'; 1039 Muhammad ibn al-Qasim proclaimed emir (ledger/2) also on page); /ledger/5 confirmed ('In 1090, the taifa was conquered by the Islamic Almoravid dynasty'); /ledger/7 confirmed (self-ruled 'for eight years starting from 1145'; Almohads, suicide in 1153); /ledger/9 confirmed (infobox 'Conquered by Granada: 1239' (text 1238, noted by the author); ledger/3 1056 follows the Granada page, the Málaga page says 1057, disagreement recorded in notes).

Area: No infobox area on the Taifa of Málaga page; no Cliopatria row. Keyframes are Málaga province (c. 7,300 km2) plus a 40 km Algeciras circle 1035-1038.

### taifa-of-lerida: pass

Spot checks: /ledger/6 confirmed ('In 1083, they took Graus'); /ledger/9 confirmed (Peter took Estada, Monzón and Almenar between 1087 and 1093); /ledger/10 confirmed ('In 1100, Peter, now king of Aragon, captured Barbastro', Sariñena the same year); /ledger/11 confirmed (Pomar de Cinca and Albalate de Cinca 1101); /ledger/12 confirmed ('appears to have fallen to the Almoravids that year' (1102), others 1110).

Area: No infobox and no area on the Taifa of Lleida page; two 45 km circles (under 12,700 km2) carved from Cliopatria's Zaragoza shapes (36-38 thousand km2), stated in keyframe 0.

- TO DO /ledger/3: Advisory, not blocking: the 1081 gain of Lérida from taifa-of-zaragoza re-gains land this dossier never lost: keyframe 0 (1040-1082) holds Lleida throughout and no loss precedes the gain. Evidence: Taifa of Lleida page: the brothers 'fought a civil war in 1078-81' and at al-Muqtadir's death the realm 'was divided between his two sons', al-Mundhir 'inherited Lérida also'; taifa-of-zaragoza /ledger/6 books only a contest_end with taifa-of-lerida in 1081, no loss. Fix: Either drop /ledger/3 and put al-Mundhir's succession in the note of /ledger/2 (contest_end), or book Yusuf's loss of Lérida to taifa-of-zaragoza (c. 1078-1081, confidence 1-2) before the 1081 gain and mark keyframe 0 accordingly.

- TO DO /ledger/4: Advisory, not blocking: Tortosa and Denia are drawn as Lérida's vassals (vassal tint) although the page has al-Mundhir rule them himself. Evidence: Taifa of Lleida page: al-Mundhir 'was already governing Denia and Tortosa as his father's ḥājib' and inherited Lérida also; the Zaragoza dossier books Denia's 1081 loss with counterpart taifa-of-tortosa (its /ledger/8), so the three dossiers disagree on who held Denia 1081-1090. Fix: Keep the vassal reading only if a page says Tortosa and Denia kept their own rulers; otherwise book them as gains (1081) and losses (1090/1092). Route the Zaragoza /ledger/8 counterpart string to its owner.

### taifa-of-majorca: pass

Spot checks: /ledger/1 confirmed ('The Crusaders invested Palma de Majorca in August 1114'); /ledger/2 confirmed ('In 1115 they were reconquered by the Almoravids of peninsular Iberia'; ledger/3 April 1115 capitulation also on page); /ledger/4 confirmed ('the second taifa (1147-1203), under the Banu Ghaniya dynasty'); /ledger/5 confirmed ('the Almohads retook the islands in 1185'; 1187 recapture and 1203 execution (ledger/6, ledger/7) also on page).

Area: No area on the Taifa of Mallorca page (infobox span 1018-1203; the 1076 start is explained in notes). Region Balearic Islands (c. 5,000 km2).

### gibraltar: fix

Spot checks: /ledger/0 confirmed ('In 1704, Anglo-Dutch forces captured Gibraltar from Spain'); /ledger/5 confirmed ('ceded to Great Britain in perpetuity under the Treaty of Utrecht in 1713'); /ledger/6 confirmed (besieged 'from June 1779 to February 1783' (infobox 24 June 1779; the 16 June declaration sentence is on the page)); /ledger/7 confirmed ('The siege was finally lifted on 7 February 1783'); /ledger/10 confirmed ('declared a crown colony on 25 June 1830').

Area: No Cliopatria row; the keyframe is the Natural Earth country Gibraltar, about the infobox 6.8 km2.

- APPLIED /identity/end: The dossier ended in 2026 with a confidence-1 vassal_end and a dissolve (old /ledger/11-12) that its own notes say did not happen ('Not a dissolution'). Evidence: Gibraltar page: still a British Overseas Territory; living states in this project close at 2024 without a dissolve (united-kingdom and kingdom-of-spain end {year: 2024}, no dissolve), and Gibraltar's suzerain united-kingdom ends in 2024. Fix: end {year: 2024}; capital, keyframe 0 and certainty to 2024; the two 2026 events removed; the notes sentence rewritten. Validates (one expected warning: the 1801 vassal_start lasts to the end).

- TO DO /ledger/2: Advisory, not blocking: double-booking: the metropole dossiers book Gibraltar as direct land in 1713 and carry no vassal_start gibraltar for 1704 (kingdom-of-england), 1707 (kingdom-of-great-britain) or 1801 (united-kingdom). Evidence: kingdom-of-great-britain /ledger/5 '1713 gain kingdom-of-spain {country: Gibraltar}'; kingdom-of-spain /ledger/49 1713 loss to kingdom-of-great-britain; kingdom-of-england has no event near 1704. The author flagged this (report problems, notes item 1). Fix: Reconciler: keep gibraltar (type colony). In kingdom-of-great-britain replace the Gibraltar part of /ledger/5 by vassal_start gibraltar (1707, as heir to England's 1704 holding); in kingdom-of-spain give the 1713 Gibraltar loss the counterpart gibraltar; add vassal_start gibraltar 1704 to kingdom-of-england and vassal_start 1801 to united-kingdom.

### lordship-of-albarracin: pass

Spot checks: /ledger/0 confirmed (1167 Ibn Mardanis 'ceded the Taifa of Albarracín to a vassal of Sancho VI of Navarre'; infobox 'Established: 1167'); /ledger/2 confirmed (1172 consolidation and independence); /ledger/3 confirmed (ruler table: Alvar Pérez d'Azagra to 1260, Juan Núñez I de Lara from 1260); /ledger/6 confirmed (conquered by Aragon in 1284 'after a lengthy siege lasting from April to September' (ledger/4-5 also); infobox 'Disestablished: 1300', the author's 1284 choice is explained).

Area: No infobox area; a 35 km circle (c. 3,850 km2) is the stated reading; Cliopatria's earlier Taifa of Albarracín shapes were 8.7-8.8 thousand km2.

### banu-marwan-of-badajoz: fix

Spot checks: /ledger/0 confirmed ('The official foundation of Badajoz was laid by the Muladi nobleman Ibn Marwan, around 875'; 'autonomous rebel state which was quenched only in the 10th century'); /ledger/1 confirmed ('Between 876 and 877 he also erected the Castle of Marvão'); /ledger/2 confirmed ('he achieved the surrender of Ibn Marwan of Badajoz in 930'); /ledger/3 confirmed ('His dynasty lasted until 930').

Area: No area on the pages; the two-province reading (c. 28,000 km2) is stated as rough in keyframe 0.

- APPLIED /wars/0/from: The war began in 868, seven years before the state (start 875): wars must lie inside the life. Evidence: Ibn Marwan page: 'In 868 ... he rebelled'; Badajoz page: founded 'around 875'. Fix: from 875, with the 868 start kept in the war note.

- TO DO /ledger/1: Advisory, not blocking: the 877 gain of Marvão (Portalegre) from emirate-of-cordoba adds land the found event (/ledger/0) and keyframe 0 (875-929) already include (admin1 Portalegre). Evidence: Ibn Marwan page: 'Between 876 and 877 he also erected the Castle of Marvão'; /ledger/0 region is union[Badajoz, Portalegre]. Fix: Found on admin1 Badajoz only and split keyframe 0 at 877 (875-876 Badajoz; 877-929 Badajoz + Portalegre), or drop the gain.

### order-of-calatrava: pass

Spot checks: /ledger/0 confirmed ('Thus a new order was created in 1157'); /ledger/2 confirmed ('abandoned their bulwark of Calatrava to the Almohads (1195)'; Salvatierra 1198 (ledger/3) also on page); /ledger/4 confirmed ('the reconquest of Calatrava (1212)'; Calatrava la Nueva 1218 (ledger/5) and Monfragüe 1221 (ledger/6) also on page); /ledger/7 confirmed (1487, Padilla's death and Innocent VIII's bull: 'Thus ended the political autonomy of the Order of Calatrava').

Area: No area on the Order page; circles around Ciudad Real (35 km), Alcañiz (15 km) and Monfragüe (20 km) are stated readings.

- TO DO /ledger/7: Advisory, not blocking: the 1487 loss books Alcañiz, the Aragonese encomienda, to crown-of-castile, while identity.successors gives crown-of-aragon for it. Evidence: Order of Calatrava page: Alcañiz came after service in the Kingdom of Aragon; the 1487 bull gave Ferdinand the administration of the whole Order. Fix: Split /ledger/7 and /ledger/8: Ciudad Real and Monfragüe to crown-of-castile, Alcañiz to crown-of-aragon.

- TO DO /identity/capitals: Advisory, not blocking: all three seats use the Ciudad Real stand-in coordinates (38.99 N, 3.93 W) although capitals take lat/lon directly; Salvatierra (1198-1209) then lies outside the drawn land (keyframe 2 is Alcañiz only). Evidence: Calatrava la Nueva is near Aldea del Rey, some 35-40 km south of Ciudad Real; the stand-in is needed only for gazetteer region names, not for capitals. Fix: Give each seat its own coordinates from its page (Calatrava la Vieja, Salvatierra, Calatrava la Nueva) and widen the region circle if the 1218 seat falls outside it.

- TO DO /ledger/6/counterpart: Advisory, not blocking: 'Order of Monfragüe' is neither a slug nor listed in counterparts_needing_dossiers. Evidence: The page: 'In 1221 the Order of Monfragüe was merged into that of Calatrava'. Fix: List it (or say in notes that it needs no dossier).

### taifa-of-mertola: pass

Spot checks: /ledger/1 confirmed ('From 1044 until 1091 it was under the forcible control of the Taifa of Seville'); /ledger/2 confirmed (periods 'from 1144 to 1145, and from 1146 to 1151'; infobox 'Seville/Almoravids: 1044-1091 / 1091-1144'); /ledger/3 confirmed (infobox 'To Badajoz: 1145-1146'; ledger/4 'restored 1146-1151' in the ruler list); /ledger/5 confirmed ('ended in 1151, when it was finally conquered by the Almohad Caliphate').

Area: No area on the Taifa of Mértola page; a 20 km circle matches the municipality's 1,292.87 km2, stated in keyframe 0.

### bonapartist-spain: pass

Spot checks: /ledger/2 confirmed ('on 1 August Joseph evacuated the capital for Old Castile'); /ledger/3 confirmed ('Madrid surrendered on 1 December and Joseph Bonaparte was restored to his throne'); /ledger/4 confirmed (infobox: 'Military governments dependent on Paris (since 1810): Biscay, Navarre and Aragon' and Catalonia); /ledger/5 confirmed ('The French invaded Andalusia on 19 January 1810'); /ledger/6 confirmed (Valencia forced to surrender 'on 9 January 1812 after a brief siege'); /ledger/7 confirmed ('King Joseph Bonaparte abandoned Madrid on 11 August'; 17 March 1813 (ledger/9) and Vitoria 21 June (ledger/10) also on page).

Area: No area on Spain under Joseph Bonaparte; keyframes are differences of Cliopatria Kingdom of Spain shapes, stated.

- TO DO /ledger/2/region: Advisory, not blocking: the August 1808 loss is Madrid province only, while the December gain (/ledger/3) restores the whole centre and north. Evidence: Peninsular War page: 'on 1 August Joseph evacuated the capital for Old Castile' and the French withdrew behind the Ebro; the gain re-books land the loss never removed. Fix: Make /ledger/2 the land south of the Ebro that the French left (or the /ledger/3 region minus Old Castile and the Ebro line).

- THIN /ledger/8: Joseph's return to Madrid in late 1812 (confidence 1; the Peninsular War page says only that he 'planned to recapture Madrid'). Page to try: https://en.wikipedia.org/wiki/Joseph_Bonaparte

### fihrid-governors-of-al-andalus: thin

Spot checks: /ledger/0 confirmed ('definitively overthrown in 750'; malik 'January 750 - May 756'); /ledger/1 confirmed (landed at Almuñécar 'in September 755'); /ledger/2 confirmed (defeated at Musarah 'just outside Córdoba in March 756'); /ledger/4 confirmed ('large swathes remaining in the hands of Yusuf ibn Abd al-Rahman al-Fihri's supporters until 779' (Toledo, Zaragoza, Barcelona)).

Area: No area on the pages; keyframes are Cliopatria Umayyad 751 (473.6 thousand km2) and Emirate 757 minus Andalusia, stated.

- THIN /keyframe_review/1: Septimania is drawn as Fihrid land through 778 (Cliopatria Emirate 757 shape minus Andalusia keeps it), but Narbonne capitulated to the Franks in 759 and Roussillon in 760; the dossier needs 759 and 760 losses to kingdom-of-the-franks and keyframe 1 split at 759 (minus region Septimania). The author flagged it; the page was beyond the budget. emirate-of-cordoba /ledger/2-3 book these losses itself, so the reconciler must move them here. Page to try: https://en.wikipedia.org/wiki/Septimania

- THIN /identity/capitals/1: Toledo 756-779: Yusuf died in 759 (Yusuf page infobox); who held Toledo and the north 759-779 for the Fihrids is not on the pages opened (the Abd al-Rahman I page says only 'Yusuf's supporters until 779'). Page to try: https://en.wikipedia.org/wiki/Toledo

### jahwarid-taifa-of-cordoba: fail

Spot checks: /ledger/0 confirmed (infobox 'Córdoba organized into a republic: 1031'; Abu 'l-Hazm 'led Córdoba from 1031 until his death in 1043'); /ledger/1 confirmed ('In 1070, after defeating the Toledan army, al-Mu'tamid captured Córdoba and deposed Abd al-Malik').

Area: Acknowledged in the keyframe note, but on a false description of the Cliopatria shape; see fixes.

- TO DO /keyframe_review/0: The keyframe draws a 35 km circle (c. 3,850 km2) and justifies it by saying Cliopatria's 1031-1071 Córdoba shapes are 'drawn as a wider (Hammudid-era) realm'; they are not: they are a Córdoba-sized shape that the neighbour dossier hands to this state, so the area differs by a factor of 2.5 on a false premise. Evidence: shapes.csv: caliphate-of-cordoba_1034 (1034-1065) 9,813 km2, bbox -5.82..-3.97 E, 37.38..38.55 N; caliphate-of-cordoba_1066 (1066-1071) 9,788 km2, same bbox. caliphate-of-cordoba.json keyframe_review marks both 'wrong', correction 'the same shape, to be drawn as the Taifa of Córdoba (the Jahwarid republic) 1031-1069'; taifa-of-seville gains the whole province in 1070. Taifa of Córdoba page: only 'Córdoba and its vicinity'. Fix: Use {"cliopatria": "Caliphate of Córdoba", "year": 1034} (with text 'Córdoba and its vicinity') for keyframe 0, /ledger/0-2, /wars/0/zones/0 and the predecessor and successor land, and rewrite the keyframe note; or keep a smaller reading and say why the remaining 6,000 km2 of the handed-over shape belongs to someone else 1031-1070.

### banu-qasi: thin

Spot checks: /ledger/1 confirmed ('In 884, the emir sent two military campaigns into the region and took Zaragoza'); /ledger/3 confirmed (898 Lubb 'formally recognized the sovereignty of the emir, Abd Allah' for Tudela and Tarazona); /ledger/5 confirmed (914 Muhammad ibn Lubb 'was able to reclaim the city for his family, as well as Lleida' (the note's 'regains' is a paraphrase)); /ledger/10 confirmed (924 removed at Tudela, 'placing their old rivals the Tujibids of Zaragoza in their place'; 923 Viguera and Nájera (ledger/8) and 929 end (ledger/11) also on page).

Area: No Cliopatria row; circles around Tudela, Monzón, Lleida and Nájera are stated readings.

- APPLIED /wars/0/from: The war began in 840, 32 years before the state (start 872): wars must lie inside the life. Evidence: identity.start 872; Banu Qasi page dates the state's land from January 872. Fix: from 872, with the 840s revolts kept in the war note.

- TO DO /ledger/11/counterpart: Advisory, not blocking: the 929 dissolve names emirate-of-cordoba, which became the caliphate on 16 January 929 (emirate-of-cordoba /ledger/32). Evidence: Banu Qasi page: 'The death of Muhammad ibn Lubb marked the end of the Banu Qasi in the Ebro valley'; infobox 'conquest by Córdoba and Navarre in 929'. Fix: caliphate-of-cordoba (and kingdom-of-pamplona for Ayerbe if a page says so).

- THIN /keyframe_review/5: Monzón and Lleida (gained 914, /ledger/5) vanish in 924 with no loss event, and Ayera/Ayerbe appears with no gain; the page says only 'leaving him only Ayera in 928'. Carried over from the eu-12-a review. Page to try: https://en.wikipedia.org/wiki/Muhammad_ibn_Lubb_ibn_Qasi

- THIN /ledger/2: 884 loss of Monzón (confidence 1): date and taker not on the page. Page to try: https://en.wikipedia.org/wiki/Monz%C3%B3n

- THIN /ledger/6: 914 Rioja gain (Nájera, Viguera; confidence 1): acquisition undated. Page to try: https://en.wikipedia.org/wiki/Viguera

### rebellion-of-umar-ibn-hafsun: fix

Spot checks: /ledger/0 confirmed ('By 883, he had become the leader of the rebels in the provinces to the south and the west of the Emirate of Córdoba'); /ledger/1 confirmed ('He finally arrived at Algeciras on 1 June 914', Málaga taken 'after one day'; 70 castles by the end of 914 on the Umar ibn Hafsun page); /ledger/2 confirmed ('Hafs surrendered Bobastro in 928'; Abd al-Rahman III page: 'surrendered in 928 and had his life spared').

Area: No Cliopatria row; the three provinces (c. 34,000 km2) are the Abdallah page's 'Reyyo, Elvira, Jaén'.

- APPLIED /wars/0/from: The war began in 882, a year before the state (start 883): wars must lie inside the life. Evidence: Umar ibn Hafsun page: 'By 883, he had become the leader of the rebels'; he fought the emir in 882 (the dossier's own note). Fix: from 883, with 882 kept in the war note.

- TO DO /identity/capitals/1: Advisory, not blocking: Poley (Aguilar de la Frontera, 37.52 N 4.65 W), capital 885-891, lies outside the 883 keyframe (Málaga, Granada, Jaén); carried over unaddressed from the eu-12-a review. Evidence: Umar ibn Hafsun page: around 885 he moved to 'the town of Poley, which is now Aguilar de la Frontera'; back to Bobastro after the 891 defeat. Fix: Add a Poley circle to keyframe 0 for 885-891 (a gain and a 891 loss to emirate-of-cordoba), or say in the capital's note that the seat lay outside the held provinces.

## Cross-dossier matrix

- taifa-of-malaga 1035 gain taifa-of-algeciras -> matched [taifa-of-algeciras 1035 loss]: taifa-of-algeciras /ledger/1
- taifa-of-malaga 1039 loss taifa-of-algeciras -> matched [taifa-of-algeciras 1039 gain]: taifa-of-algeciras /ledger/2
- taifa-of-malaga 1056 loss taifa-of-granada -> matched [taifa-of-granada 1056 gain]: taifa-of-granada /ledger/6
- taifa-of-malaga 1073 gain taifa-of-granada -> matched [taifa-of-granada 1073 loss]: taifa-of-granada /ledger/7
- taifa-of-malaga 1090 loss almoravid-dynasty -> missing: almoravid-dynasty (af-02) has 1090 gain from taifa-of-granada only; Málaga under its own Zirid 1073-1090 is absent there
- taifa-of-malaga 1145 gain almoravid-dynasty -> missing: almoravid-dynasty books its 1145 losses to other taifas and the Almohads, none to taifa-of-malaga
- taifa-of-malaga 1153 loss almohad-caliphate -> missing: almohad-caliphate (af-02) has 1152 gains from other taifas, none from taifa-of-malaga
- taifa-of-malaga 1229 gain almohad-caliphate -> missing: almohad-caliphate has 1227-1228 losses to Portugal, Murcia, Valencia; none to taifa-of-malaga
- taifa-of-malaga 1239 loss emirate-of-granada -> missing: emirate-of-granada has 1238 gain from taifa-of-almeria and 1238/1239 gains from 'nobody'; one of those should name taifa-of-malaga
- taifa-of-lerida 1078 contest_start taifa-of-zaragoza -> matched [taifa-of-zaragoza 1078 contest_start]: taifa-of-zaragoza /ledger/5
- taifa-of-lerida 1081 contest_end taifa-of-zaragoza -> matched [taifa-of-zaragoza 1081 contest_end]: taifa-of-zaragoza /ledger/6
- taifa-of-lerida 1081 gain taifa-of-zaragoza -> mismatch [taifa-of-zaragoza 1081 contest_end]: Zaragoza books no loss of Lérida; this dossier never lost it either (see lerida fix /ledger/3)
- taifa-of-lerida 1081 vassal_start taifa-of-tortosa -> exception: taifa-of-tortosa is a Cliopatria row with no dossier yet (group not run); taifa-of-zaragoza /ledger/7 books Tortosa's 1081 loss to taifa-of-tortosa
- taifa-of-lerida 1081 vassal_start taifa-of-denia -> missing: taifa-of-denia has nothing 1080-1092; taifa-of-zaragoza /ledger/8 books Denia's 1081 loss with counterpart taifa-of-tortosa
- taifa-of-lerida 1083 loss kingdom-of-aragon -> exception: kingdom-of-aragon (Cliopatria 1015-1168) has no dossier yet; same for the 1093, 1100 and 1101 losses
- taifa-of-lerida 1090 vassal_end taifa-of-denia -> missing: as the 1081 vassal_start
- taifa-of-lerida 1102 loss almoravid-dynasty -> missing: almoravid-dynasty has 1102 gain from taifa-of-valencia only
- taifa-of-majorca 1114 contest_start republic-of-pisa -> exception: republic-of-pisa is a Cliopatria row with no dossier yet (Italy group); 1115 contest_end likewise
- taifa-of-majorca 1115 loss almoravid-dynasty -> mismatch [almoravid-dynasty 1115 gain]: almoravid-dynasty /ledger/26 1115 gain names the string 'Balearic Islands (last local ruler Mubashir al-Dawla)'; map it to taifa-of-majorca
- taifa-of-majorca 1147 gain almoravid-dynasty -> missing: almoravid-dynasty keeps the Balearics to 1203; it should cede them in 1147 (author's notes item 6)
- taifa-of-majorca 1185 loss almohad-caliphate -> mismatch [almohad-caliphate 1185 gain]: almohad-caliphate /ledger/29 1185 gain names almoravid-dynasty (the Banu Ghaniya) instead of taifa-of-majorca
- taifa-of-majorca 1187 gain almohad-caliphate -> mismatch [almohad-caliphate 1187 loss]: almohad-caliphate /ledger/30 1187 loss names almoravid-dynasty
- taifa-of-majorca 1203 loss almohad-caliphate -> mismatch [almohad-caliphate 1203 gain]: almohad-caliphate /ledger/37 1203 gain names almoravid-dynasty
- gibraltar 1704 contest_start kingdom-of-spain -> missing: kingdom-of-spain has nothing for Gibraltar 1704; it keeps it to its 1713 loss
- gibraltar 1704 vassal_start kingdom-of-england -> missing: kingdom-of-england (eu-11) has no vassal_start gibraltar
- gibraltar 1707 vassal_start kingdom-of-great-britain -> mismatch [kingdom-of-great-britain 1713 gain]: kingdom-of-great-britain /ledger/5 books Gibraltar as a direct 1713 gain from kingdom-of-spain (double-booking, author's notes item 1)
- gibraltar 1713 contest_end kingdom-of-spain -> mismatch [kingdom-of-spain 1713 loss]: kingdom-of-spain /ledger/49 1713 loss of Gibraltar and Menorca names kingdom-of-great-britain; the Gibraltar part should name gibraltar
- gibraltar 1779 contest_start kingdom-of-spain -> missing: no Great Siege contest in kingdom-of-spain; 1783 contest_end likewise
- gibraltar 1801 vassal_start united-kingdom -> missing: united-kingdom has no vassal_start gibraltar
- lordship-of-albarracin 1167 found taifa-of-murcia -> mismatch [taifa-of-murcia 1168 loss]: taifa-of-murcia /ledger/10 1168 loss names the string 'Pedro Ruiz de Azagra'; map it to lordship-of-albarracin
- lordship-of-albarracin 1167 vassal_start kingdom-of-navarre -> missing: kingdom-of-navarre has no vassal_start lordship-of-albarracin (nor the 1172 vassal_end)
- lordship-of-albarracin 1284 loss crown-of-aragon -> missing: crown-of-aragon has 1282 and 1285 events only; the 1284 gain (and the contest) is absent
- banu-marwan-of-badajoz 875 found emirate-of-cordoba -> missing: emirate-of-cordoba has no 875 loss (author's notes item 3)
- banu-marwan-of-badajoz 877 gain emirate-of-cordoba -> missing: emirate-of-cordoba 878 loss to nobody and 879 to kingdom-of-asturias; none to banu-marwan-of-badajoz
- banu-marwan-of-badajoz 930 loss caliphate-of-cordoba -> mismatch [caliphate-of-cordoba 930 gain]: caliphate-of-cordoba /ledger/1 930 gain names the string 'Ibn Marwan of Badajoz'; map it
- order-of-calatrava 1157 found kingdom-of-castile -> missing: kingdom-of-castile has no 1157 loss of Calatrava
- order-of-calatrava 1179 gain crown-of-aragon -> missing: crown-of-aragon has nothing near 1179
- order-of-calatrava 1195 loss almohad-caliphate -> missing: almohad-caliphate /ledger/35 1195 gain names kingdom-of-leon
- order-of-calatrava 1212 gain almohad-caliphate -> missing: almohad-caliphate /ledger/39 1212 loss names kingdom-of-castile
- order-of-calatrava 1221 merge Order of Monfragüe -> exception: no dossier; a small order absorbed in 1221
- order-of-calatrava 1487 loss crown-of-castile -> missing: crown-of-castile has 1485-1487 gains from emirate-of-granada only
- taifa-of-mertola 1044 loss taifa-of-seville -> matched [taifa-of-seville 1044 gain]: taifa-of-seville /ledger/3
- taifa-of-mertola 1144 gain almoravid-dynasty -> mismatch [almoravid-dynasty 1144 loss]: almoravid-dynasty /ledger/29 1144 loss names the string 'Muridun of Ibn Qasi (Silves, Mertola, Beja, Evora)'; map to taifa-of-mertola (and taifa-of-silves)
- taifa-of-mertola 1145 loss taifa-of-badajoz -> missing: taifa-of-badajoz has 1144 gain from almoravid-dynasty only; no 1145 gain or 1146 loss
- taifa-of-mertola 1151 loss almohad-caliphate -> missing: almohad-caliphate has 1149 and 1152 gains, none from taifa-of-mertola
- bonapartist-spain 1808 vassal_start first-french-empire -> exception: first-french-empire (Cliopatria 1805-1814) has no dossier yet; 1810 loss and 1813 vassal_end likewise
- bonapartist-spain 1808 gain kingdom-of-spain -> mismatch [kingdom-of-spain 1808 loss]: kingdom-of-spain /ledger/64 1808, /65 1810, /67 1812, /69 1813 name first-french-empire; replace by bonapartist-spain where Joseph's kingdom is meant (author's notes item 2)
- fihrid-governors-of-al-andalus 750 found umayyad-caliphate -> mismatch [umayyad-caliphate 750 loss]: umayyad-caliphate /ledger/93 750 loss uses the string 'Fihrid governors of al-Andalus'; map it
- fihrid-governors-of-al-andalus 756 loss emirate-of-cordoba -> mismatch [emirate-of-cordoba 756 found]: emirate-of-cordoba /ledger/0 756 found names the string 'Fihrid governors of al-Andalus'; map it
- fihrid-governors-of-al-andalus 779 loss emirate-of-cordoba -> mismatch [emirate-of-cordoba 757 gain]: emirate-of-cordoba /ledger/1 books the centre and north as a 757 gain (confidence 1, 'no page dates any of it'); the Abd al-Rahman I page has Yusuf's supporters hold them 'until 779'; move it to 779, and its 759/760 Septimania losses belong to this dossier
- jahwarid-taifa-of-cordoba 1070 loss taifa-of-seville -> mismatch [taifa-of-seville 1070 gain]: taifa-of-seville /ledger/13 1070 gain names taifa-of-cordoba (the Cliopatria 1147-1249 row); map it to jahwarid-taifa-of-cordoba, and its land (the province) disagrees with this dossier's 35 km circle
- banu-qasi 884 loss emirate-of-cordoba -> matched [emirate-of-cordoba 884 gain]: emirate-of-cordoba /ledger/21
- banu-qasi 884 loss nobody -> exception: counterpart nobody (confidence 1); 914 gains from nobody likewise
- banu-qasi 898 vassal_start emirate-of-cordoba -> matched [emirate-of-cordoba 898 vassal_start]: emirate-of-cordoba /ledger/22
- banu-qasi 898 gain emirate-of-cordoba -> missing: the emirate books no 898 loss of Tarazona (its /ledger/23 is a loss to 'autonomous lords of al-Andalus')
- banu-qasi 914 loss kingdom-of-pamplona -> matched [kingdom-of-pamplona 914 gain]: kingdom-of-pamplona /ledger/2
- banu-qasi 923 loss kingdom-of-pamplona -> matched [kingdom-of-pamplona 923 gain]: kingdom-of-pamplona /ledger/5
- banu-qasi 924 vassal_end emirate-of-cordoba -> matched [emirate-of-cordoba 924 vassal_end]: emirate-of-cordoba /ledger/30
- banu-qasi 924 loss Tujibids of Zaragoza -> exception: listed in counterparts_needing_dossiers (tujibids-of-zaragoza)
- rebellion-of-umar-ibn-hafsun 914 loss emirate-of-cordoba -> matched [emirate-of-cordoba 914 gain]: emirate-of-cordoba /ledger/26
- rebellion-of-umar-ibn-hafsun 928 loss emirate-of-cordoba -> matched [emirate-of-cordoba 928 gain]: emirate-of-cordoba /ledger/31

## Problems

- No page failed to load for the reviewer; 18 pages opened with WebFetch.
- Reviewer-applied fixes (validated with 0 errors): gibraltar end 2026 -> 2024 and two confidence-1 2026 events removed; war start clamped to the state's start in banu-marwan-of-badajoz (868->875), banu-qasi (840->872) and rebellion-of-umar-ibn-hafsun (882->883).
- banu-qasi and rebellion-of-umar-ibn-hafsun were kept from eu-12-a (reviewed there: thin and fix); banu-qasi.json was repaired after that review and is re-reviewed here; the eu-12-a thin items (Monzón/Lleida 924, Ayerbe) remain.
- Most mirrors are missing because the counterpart dossiers (almoravid-dynasty, almohad-caliphate af-02; kingdom-of-great-britain, kingdom-of-england, united-kingdom eu-11; emirate-of-cordoba, caliphate-of-cordoba, kingdom-of-spain, taifa-of-seville, taifa-of-badajoz, taifa-of-denia, taifa-of-murcia, kingdom-of-castile, crown-of-castile, crown-of-aragon, kingdom-of-navarre, emirate-of-granada eu-12) predate these new states; route the cross_checks to their owners. Counterpart strings to map: 'Ibn Marwan of Badajoz', 'Fihrid governors of al-Andalus', 'Balearic Islands (last local ruler Mubashir al-Dawla)', 'Muridun of Ibn Qasi (Silves, Mertola, Beja, Evora)', 'Pedro Ruiz de Azagra', and taifa-of-cordoba in taifa-of-seville 1070.
- Not written yet (exceptions): kingdom-of-aragon, taifa-of-tortosa, republic-of-pisa, first-french-empire.
- bonapartist-spain (1808-1813) lies outside group eu-12's era (to 1789); written on eu-12-m's request.
