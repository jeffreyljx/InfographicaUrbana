# Review of batch eu-12-h (Iberia and the taifas, part h)

Reviewed 2026-10-25 by the adversarial reviewer. Validator: 0 errors in all six dossiers (warnings: unknown slugs taifa-of-mertola, taifa-of-lerida, taifa-of-malaga; gazetteer places Mértola and Lleida). Pages were read with WebFetch (summaries). The Cliopatria shapes were tested with point-in-polygon and overlap tests on the grid feature cache (tools/grid.py load_features), since no infobox gives an area. No dossier was edited by the reviewer.

Verdicts: taifa-of-seville **fail**, taifa-of-zaragoza **fail**, taifa-of-algeciras **fail**, taifa-of-saltes-and-huelva **thin**, taifa-of-santa-maria-do-algarve **pass**, county-of-pallars-jussa **pass**.

## The main finding: Cliopatria's 'Taifa of Algeciras' is mostly Málaga

Point tests: the 1028 shape holds Ronda, Coín and Vélez-Málaga and reaches Morocco; the 1040 shape is about 72 percent east of 5.25W (Málaga province: Coín and Vélez-Málaga inside, Málaga city 2 km off the coast edge); the 1085, 1147 and 1152 shapes lie wholly in Málaga province (Antequera, Coín, Vélez inside) and do not contain Algeciras (80 km and 36 km away). The Abd al-Mu'min page: 'In 1147 Abd al-Mu'min sent a military force led by another Almoravid defector, Abu Ishaq Barraz, who captured Algeciras and Tarifa before moving west to Niebla, Badajoz, and the Algarve.' This breaks the Algeciras dossier's 1040, 1147 and 1152 keyframes and its second taifa, and the two Seville events that cite those shapes as 'Algeciras and its district' (1055 gain, 1086 loss), plus Seville's 1085 correction, which subtracts a shape that does not touch Seville's.

## taifa-of-seville: fail

All dated events confirmed on their pages (10 checked), but the two Algeciras events draw the wrong land: the Cliopatria 'Taifa of Algeciras' shapes they cite lie mostly or wholly in Málaga province, so Seville gains the Málaga hinterland in 1055, the Almoravids take land near Antequera in 1086, and the 1085 keyframe's correction subtracts a shape it does not touch (Algeciras stays Seville's to 1091). Mechanical to fix.

Findings (all applied: false):

- `/ledger/7/region`: The region {cliopatria: Taifa of Algeciras, 1040} is about 72 percent Málaga province, not Algeciras: Coín and Vélez-Málaga are inside it, Málaga city 2 km off its coast edge, only 28 percent lies west of 5.25W. Evidence: Point and overlap tests on the Cliopatria geometry (grid feature cache). Seville's own 1056 keyframe (adjust, 'shape unchanged') does not hold that land: Coín is 53 km outside it, Vélez-Málaga 118 km. The Abbad II page names only 'Algeciras (1055)'. Málaga was a separate Hammudid taifa (the author's own counterparts list: taifa-of-malaga 1026-1057). Fix: Use {"place": "Algeciras", "km": 30, "country": "Spain", "text": "Algeciras and its district"} (or {"intersect": [{"cliopatria": "Taifa of Algeciras", "year": 1040}, {"admin1": "Cádiz", "country": "Spain"}]}); make the same change in taifa-of-algeciras /ledger/3 so both sides stay matched.
- `/ledger/17/region`: The region {cliopatria: Taifa of Algeciras, 1085} contains no Algeciras: that shape lies wholly in Málaga province (Antequera and Coín inside, Algeciras city 80 km outside, Tarifa 99 km). Evidence: Almoravid page: Algeciras was to 'be surrendered to him so he could use it as a base for his troops'; 'They did so in July 1086 without encountering resistance.' The page names Algeciras, the region draws the Antequera country. Fix: Use {"place": "Algeciras", "km": 30, "country": "Spain", "text": "Algeciras and its district"} (or {"intersect": [{"cliopatria": "Taifa of Algeciras", "year": 1040}, {"admin1": "Cádiz", "country": "Spain"}]}).
- `/keyframe_review/6/correction`: The correction {minus: [Seville 1085, Algeciras 1085]} removes nothing: the two Cliopatria shapes do not intersect (intersection area 0), while Algeciras city lies inside the Seville 1085 shape, so Algeciras stays drawn as Seville's from July 1086 to 1091. Evidence: Geometry test on the grid feature cache; same evidence as /ledger/17. Fix: {"minus": [{"cliopatria": "Taifa of Seville", "year": 1085}, {"place": "Algeciras", "km": 30, "country": "Spain"}], "text": "the 1085 shape without Algeciras, ceded to the Almoravids in July 1086; it holds 1078-1091"} (the after-1086 part could also be a new keyframe 1086-1091 with the 1078-1086 years left whole).
- `/ledger/13/note`: Minor, not blocking: the Seville page itself has 'Al-Mu'tamid seized Córdoba in 1071' and 'a brief interlude in 1075–1078'; the note quotes 1070 from the al-Mu'tamid and Toledo pages only. Evidence: Taifa of Seville page, read 2026-10-25. Fix: Add the 1071 variant to the note; keep 1070.

Thin (for a gap-filler):

- `/keyframe_review/6`: The 1085 shape adds Jaén, Baeza (the upper Guadalquivir) and Lorca besides Murcia (all four inside by point test, none in the 1072 shape); no event explains Jaén and Baeza, which is most of the unexplained +30,000 km2 the author flagged. Try: https://en.wikipedia.org/wiki/Ibn_Ammar
- `/ledger/3`: Mértola 1044-45: whom it was taken from (a taifa of Mértola has no page or dossier). Try: https://en.wikipedia.org/wiki/M%C3%A9rtola

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Taifa_of_Seville: confirmed ('It was established in 1023'; body also 'after its downfall in 1031')
- `/ledger/7` https://en.wikipedia.org/wiki/Abbad_II_al-Mu%27tadid: confirmed ('Algeciras (1055)'); region wrong, see fixes
- `/ledger/9` https://en.wikipedia.org/wiki/Abbad_II_al-Mu%27tadid: confirmed ('Ronda (1065)')
- `/ledger/12` https://en.wikipedia.org/wiki/Abbad_II_al-Mu%27tadid: confirmed ('Arcos (1069)'; death 28 February 1069)
- `/ledger/13` https://en.wikipedia.org/wiki/Al-Mu%27tamid_ibn_Abbad: confirmed ('Córdoba, was taken in 1070, lost in 1075, and regained in 1078'; Seville page has 1071)
- `/ledger/14` https://en.wikipedia.org/wiki/Taifa_of_Toledo: confirmed ('helped Al-Mamun of Toledo in conquering the taifa of Córdoba in 1075')
- `/ledger/15` https://en.wikipedia.org/wiki/Al-Mu%27tamid_ibn_Abbad: confirmed ('regained in 1078')
- `/ledger/16` https://en.wikipedia.org/wiki/Taifa_of_Murcia: confirmed ('From 1078 until 1091 it was under the forcible control of Seville')
- `/ledger/17` https://en.wikipedia.org/wiki/Almoravid_dynasty: confirmed (July 1086); region wrong, see fixes
- `/ledger/21` https://en.wikipedia.org/wiki/Almoravid_dynasty: confirmed ('In September 1091, al-Mu'tamid surrendered Seville')

Area: infobox None, Cliopatria 92473 km2. No area on the Taifa of Seville page (checked); the author says so.

## taifa-of-zaragoza: fail

Dated events confirmed (6 checked) and the 1015 Pallars-box shape correctly marked wrong, but the 1076 Dénia keyframe and events take Cliopatria's whole Dénia 1066 shape, Balearic Islands included, which the Dénia dossier gives to the Taifa of Majorca in 1076; the 1081 Dénia loss names a counterpart that never regains it; a ~5,200 km2 western loss between the 1046 and 1066 shapes is not mentioned.

Findings (all applied: false):

- `/keyframe_review/9/correction`: The union with {cliopatria: Taifa of Denia, 1066} paints the Balearic Islands as Zaragoza's 1076-1080: that shape's bbox runs to 4.30E (Majorca, Menorca) and it misses the town of Dénia. Evidence: taifa-of-denia /ledger/9-11: 1076 vassal_end and loss of the 'Balearic Islands' to taifa-of-majorca, and the 1076 loss to Zaragoza drawn as {minus: [{union: [Dénia 1066, Dénia 20 km]}, Balearic Islands]} ('Dénia's peninsular possessions'); Dénia's 1066 keyframe note: the shape 'misses the town of Dénia'. Fix: Replace the Dénia part of the union with {"minus": [{"union": [{"cliopatria": "Taifa of Dénia", "year": 1066}, {"place": "Dénia", "km": 20, "country": "Spain"}]}, {"region": "Balearic Islands"}], "text": "Dénia's peninsular possessions"}.
- `/ledger/4/region`: Same defect as /keyframe_review/9: the 1076 gain takes the Balearic Islands. Evidence: As above; the Lérida page says only that al-Muqtadir 'acquired ... the ṭāʾifa of Denia in 1076'. Fix: Use the Dénia dossier's 1076 region (peninsular possessions, Balearics removed).
- `/ledger/8`: The 1081 loss of Dénia names counterpart taifa-of-denia and the Balearic-inclusive shape; Dénia did not become independent in 1081 and its dossier has no 1081 gain. Evidence: Lérida page: al-Mundhir 'was already governing Denia and Tortosa as his father's ḥājib' and the ṭāʾifa 'was divided between his two sons' in late 1081; the Dénia infobox quoted in taifa-of-denia /keyframe_review: 'To Zaragoza/Tortosa/Almoravids: 1076–1081 / 1081–1092'. Fix: Counterpart taifa-of-tortosa (al-Mundhir's realm, as /ledger/7) or fold Dénia into the /ledger/7 loss; region as in the /ledger/4 fix.
- `/keyframe_review/7/note`: The note explains the 1066 shape as Zaragoza plus Tortosa only, but the shape also loses about 5,200 km2 against the 1046 shape (west edge from 3.29W to 2.12W; Medinaceli is inside the 1018-1046 shapes and outside from 1066); and it gives Tortosa 1056 as 7,334 km2 where shapes.csv has 6,768. Evidence: shapes.csv bboxes and a difference of the two Cliopatria geometries (1046 minus 1066 about 5,200 km2; 1066 minus 1046 about 7,200 km2, which is Tortosa). Fix: Acknowledge the western loss in the note and either add a dated loss (Castile or Toledo) or mark it 'unverified: page budget'; correct the area to 6,768 km2.
- `/ledger (Calahorra)`: No event for Calahorra, which kingdom-of-pamplona /ledger/25 takes from taifa-of-zaragoza in 1045 (conf 2, 'Calahorra was wrested from the Moors') and which caliphate-of-cordoba /ledger/34 hands to Zaragoza in 1018; no Zaragoza shape contains Calahorra. Evidence: Point test: Calahorra (1.965W, 42.305N) is outside every Taifa of Zaragoza shape. Pamplona is not in the author's context list, so this is a routing gap rather than negligence. Fix: Either add Calahorra to the 1013-1045 keyframes (adjust) with a 1045 loss to kingdom-of-pamplona, or say in the notes that Calahorra was not Zaragoza's so the Pamplona and Caliphate owners can change their counterparts.

Thin (for a gap-filler):

- `/keyframe_review/7`: Who took the western Upper March (Medinaceli country) between 1046 and 1066. Try: https://en.wikipedia.org/wiki/Ferdinand_I_of_Le%C3%B3n
- `/ledger/9`: Huesca 1096 rests on the Aragon page's capital move; Monzón (Aragonese from 1089) and Barbastro (1064/1065, 1100) are not dated and stay inside the 1099 shape. Try: https://en.wikipedia.org/wiki/Battle_of_Alcoraz
- `/ledger/5`: Who held Lleida after the 1078-81 civil war and before the late-1081 division. Try: https://en.wikipedia.org/wiki/Taifa_of_L%C3%A9rida

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Taifa_of_Zaragoza: confirmed (infobox 'Downfall of Caliphate of Cordoba: 1013'; '1013–1038')
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_L%C3%A9rida: confirmed ('In 1039, it was taken from them, along with Zaragoza, by al-Mustaʿīn')
- `/ledger/3` https://en.wikipedia.org/wiki/Taifa_of_Tortosa: confirmed ('To Zaragoza: 1060–1081 or 2/3'; Lérida page 1061)
- `/ledger/4` https://en.wikipedia.org/wiki/Taifa_of_L%C3%A9rida: confirmed ('the ṭāʾifa of Denia in 1076'); region wrong, see fixes
- `/ledger/9` https://en.wikipedia.org/wiki/Kingdom_of_Aragon: confirmed as stated (capital 'from Jaca to Huesca (1096)'; no conquest dated; conf 2 is right)
- `/ledger/10` https://en.wikipedia.org/wiki/Almoravid_dynasty: confirmed ('On 30 May, Ibn al-Hajj entered the city'; Zaragoza page 'May 1110')

Area: infobox None, Cliopatria 38868 km2. No area on the Taifa of Zaragoza page (checked).

## taifa-of-algeciras: fail

The first-period events are confirmed, but the Cliopatria 'Taifa of Algeciras' shapes are mostly Málaga: the 1040 shape is ~72 percent Málaga province and was passed as 'right for the taifa'; the 1147 and 1152 shapes, passed as ok, do not contain Algeciras (36 km away) and lie around Coín, Antequera and Vélez-Málaga; the Abd al-Mu'min page has the Almohads capture Algeciras and Tarifa in 1147, so the conf-1 second taifa is contradicted.

Findings (all applied: false):

- `/keyframe_review/2`: Verdict adjust (years only) keeps a shape that is about 72 percent Málaga province (Coín and Vélez-Málaga inside, Málaga city 2 km off its coast edge; 28 percent lies west of 5.25W). Evidence: Point and overlap tests on the Cliopatria geometry. The page: 'Yahya al-Mu'tali, a cousin, annexed Algeciras to the taifa of Málaga in 1035' and Muhammad ibn al-Qasim 'was proclaimed emir of Algeciras' in 1039, i.e. Algeciras apart from Málaga; the author lists taifa-of-malaga (1026-1057) as a separate counterpart, and caliphate-of-cordoba /ledger/37 gives admin1 Málaga to the Taifa of Málaga in 1026. Fix: Correction {"place": "Algeciras", "km": 30, "country": "Spain", "text": "Algeciras and its district"} or {"intersect": [{"cliopatria": "Taifa of Algeciras", "year": 1040}, {"admin1": "Cádiz", "country": "Spain"}]}, text 'Algeciras and the Campo de Gibraltar without the Málaga country'; apply the same restriction to /keyframe_review/0 and /keyframe_review/1 (the 1028 shape minus Morocco is still mostly Málaga province) and to the regions of /ledger/0-3.
- `/keyframe_review/4`: The 1147 shape is passed as ok though it does not contain Algeciras (36 km outside) or Tarifa (55 km); 98 percent of it lies east of 5.25W around Coín, Antequera and Vélez-Málaga. Evidence: Abd al-Mu'min page: 'In 1147 Abd al-Mu'min sent a military force led by another Almoravid defector, Abu Ishaq Barraz, who captured Algeciras and Tarifa before moving west to Niebla, Badajoz, and the Algarve.' almohad-caliphate /ledger/9 (1147 gain of Algeciras and Tarifa from almoravid-dynasty, conf 3) and almoravid-dynasty /ledger/40 agree. almoravid-dynasty /ledger/35 quotes the Taifa page 'Malaga: 1145-1153'. Fix: Verdict wrong: the shape is Málaga's (second-period taifa of Málaga) or Almohad, not Algeciras.
- `/keyframe_review/5`: Same as /keyframe_review/4 for the identical 1152 shape (1152-1168). Evidence: As above. Fix: Verdict wrong.
- `/ledger/4`: Conf-1 gain of a second taifa in 1147 from the Almoravids is contradicted by the Abd al-Mu'min page (Almohads capture Algeciras in 1147) and by both neighbour dossiers. Evidence: As above. Fix: Delete; also delete /ledger/5 (1168 dissolve, page silent), end the dossier at 1055 with a dissolve to taifa-of-seville (or 1058 per the infobox), and move identity.end, the capital's 'to', certainty, rulers and successors (taifa-of-seville, not almohad-caliphate) accordingly.
- `/identity/capitals/0`: Algeciras (5.456W, 36.141N) is given to 1168 but lies outside the 1147-1168 shapes. Evidence: Point test: 36 km outside both shapes. Fix: Follows from the /ledger/4 fix: capital to 1055.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Taifa_of_Algeciras: confirmed ('created in 1013'; lead and infobox 1035-1058, flagged by the author)
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_Algeciras: confirmed ('annexed Algeciras to the taifa of Málaga in 1035')
- `/ledger/2` https://en.wikipedia.org/wiki/Taifa_of_Algeciras: confirmed ('In 1039 Muhammad ibn al-Qasim ... was proclaimed emir of Algeciras')
- `/ledger/3` https://en.wikipedia.org/wiki/Taifa_of_Algeciras: confirmed ('In 1055 al-Mu'tamid ibn Abbad ... appeared under Algeciras' walls'; infobox 1058)
- `/ledger/4` https://en.wikipedia.org/wiki/Abd_al-Mu%27min: not on page: the page has the Almohads capture Algeciras and Tarifa in 1147 (conf 1, page-silent event contradicted)

Area: infobox None, Cliopatria 6000 km2. No infobox area. The 1028 shape's African part is about 1,500 km2 by my split at 35.9N (the note says about 2,700); the unacknowledged problem is the Málaga share, not Africa.

## taifa-of-saltes-and-huelva: thin

The first taifa (1012-1051) is confirmed and the 1051 end is right; the second taifa 1147-1151 rests on Cliopatria alone (two conf-1 events, keyframe ok 'unverified: page silent'), while the neighbours give the Huelva country to Niebla's second taifa from 1145 and to Tejada 1146-1150.

Thin (for a gap-filler):

- `/ledger/2`: Any page for a second Saltés-and-Huelva taifa in 1147-1151 (the Saltés page says nothing after 1091; the Tejada page does not name Saltés or Huelva city). almoravid-dynasty /ledger/32 gives admin1 Huelva to taifa-of-niebla in 1145; the Abd al-Mu'min page has the Almohads move 'west to Niebla' in 1147. If nothing is found, mark /keyframe_review/4 wrong, drop /ledger/2-3 and end the dossier in 1051 with a dissolve to taifa-of-seville. Try: https://es.wikipedia.org/wiki/Taifa_de_Huelva
- `/ledger/3`: Who ended the second taifa and when (conf 1; almohad-caliphate /ledger/14 bridges it to 1152, also conf 1). Try: https://en.wikipedia.org/wiki/Abd_al-Mu%27min

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Taifa_of_Salt%C3%A9s_and_Huelva: confirmed (infobox 'Established: 1012'; ruler '1012/3–1051/2 or 53')
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_Salt%C3%A9s_and_Huelva: confirmed (infobox 'Conquered by Seville: 1051'; 'From 1051 until 1091')
- `/ledger/2` https://en.wikipedia.org/wiki/Taifa_of_Tejada: confirmed as stated: page silent on Saltés and Huelva (1146-1150 taifa in the Province of Huelva only)
- `/identity/predecessors` https://en.wikipedia.org/wiki/Taifa_of_Salt%C3%A9s_and_Huelva: infobox 'Preceded by: Taifa of Badajoz' against the Caliphate (flagged by the author)

Area: infobox None, Cliopatria 4445 km2. No area on the page (checked).

## taifa-of-santa-maria-do-algarve: pass

Tried: found and end years, the Seville conquest year, the ruler years, the capital inside the shape, overlap with Saltés (1 percent) and the mirror events. Nothing broke; the 1018 found from Badajoz has no mirror in taifa-of-badajoz, which is Badajoz's gap (routed in cross_checks).

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Taifa_of_Santa_Maria_do_Algarve: confirmed (infobox 'Established: 1018'; 'Sa'id: c. 1018–1041/2')
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_Santa_Maria_do_Algarve: confirmed ('Conquered by the Taifa of Seville: 1051')
- `/ledger/2` https://en.wikipedia.org/wiki/Taifa_of_Santa_Maria_do_Algarve: confirmed ('existed from 1018 to 1051')
- `/identity/rulers` https://en.wikipedia.org/wiki/Taifa_of_Santa_Maria_do_Algarve: confirmed ('Muhammad al-Mu'tasim: 1041/2–1051')

Area: infobox None, Cliopatria 2252 km2. No area on the page (checked).

## county-of-pallars-jussa: pass

Tried: the 1011 division, the 27 May 1192 donation, the count list, the capital and Tremp inside every shape, the comarca area (1,343 km2 against 1,596-1,620, ratio 1.2). Nothing broke within a 1-2 page budget. identity.wikipedia 'Pallars Jussà' is the comarca, but the schema asks for Cliopatria's field, so it stays.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/County_of_Pallars_Juss%C3%A0: confirmed ('In 1011, Sunyer of Pallars died and by his testament his county was divided')
- `/ledger/1` https://en.wikipedia.org/wiki/County_of_Pallars_Juss%C3%A0: confirmed ('On 27 May 1192, she donated the county to Alfonso and the Crown of Aragon')
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Pallars_Juss%C3%A0: confirmed (Dulce de So 1182–1192 last in the count list)
- `/identity/rulers` https://en.wikipedia.org/wiki/County_of_Pallars_Juss%C3%A0: confirmed (Raymond III 1011–1047 to Dulce de So 1182–1192; Arnold and Peter Raymond co-rulers 1098–1112)

Area: infobox None, Cliopatria 1596 km2. The county page has no area; the author compares the modern comarca (1,343 km2, ratio 1.19), not opened by me.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| taifa-of-seville 1023 found caliphate-of-cordoba | caliphate-of-cordoba 1023 loss | matched | /ledger/35 |
| taifa-of-seville 1044 gain taifa-of-mertola | - | exception | no dossier; listed in the author's counterparts_needing_dossiers |
| taifa-of-seville 1051 gain taifa-of-saltes-and-huelva | taifa-of-saltes-and-huelva 1051 loss | matched |  |
| taifa-of-seville 1051 gain taifa-of-santa-maria-do-algarve | taifa-of-santa-maria-do-algarve 1051 loss | matched |  |
| taifa-of-seville 1053 gain taifa-of-niebla | taifa-of-niebla 1053 loss | matched |  |
| taifa-of-seville 1055 gain taifa-of-algeciras | taifa-of-algeciras 1055 loss | mismatch | years agree; both sides draw the Cliopatria Algeciras 1040 shape, ~72 percent Málaga province; both should use Algeciras only |
| taifa-of-seville 1063 gain taifa-of-silves | taifa-of-silves 1063 loss | matched |  |
| taifa-of-seville 1065 gain taifa-of-ronda | taifa-of-ronda 1065 loss | matched |  |
| taifa-of-seville 1066 gain taifa-of-carmona | taifa-of-carmona 1066 loss | matched |  |
| taifa-of-seville 1066 gain taifa-of-moron | taifa-of-moron 1066 loss | matched |  |
| taifa-of-seville 1069 gain taifa-of-arcos | taifa-of-arcos 1068 loss | matched | within one year; pages disagree (Abbad II 1069, Arcos 1068), flagged by the author |
| taifa-of-seville 1070 gain taifa-of-cordoba | - | exception | taifa-of-cordoba exists but starts in 1147; the first Córdoba taifa 1031-1070 is listed in the author's counterparts_needing_dossiers; caliphate-of-cordoba /ledger/39 also dissolves into taifa-of-cordoba in 1031: route to the taifa-of-cordoba owner |
| taifa-of-seville 1075 loss taifa-of-toledo | - | exception | taifa-of-toledo not written yet (eu-12 part not run) |
| taifa-of-seville 1078 gain taifa-of-toledo | - | exception | taifa-of-toledo not written yet (eu-12 part not run) |
| taifa-of-seville 1078 gain taifa-of-murcia | taifa-of-murcia 1078 loss | matched |  |
| taifa-of-seville 1086 loss almoravid-dynasty | - | missing | almoravid-dynasty (af-02) has no 1086 gain of Algeciras (the Almoravid page: July 1086); route to af-02; Seville's region must also change to Algeciras |
| taifa-of-seville 1091 loss almoravid-dynasty | almoravid-dynasty 1091 gain | matched | /ledger/15 Córdoba |
| taifa-of-seville 1091 dissolve almoravid-dynasty | almoravid-dynasty 1091 gain | matched | /ledger/17 Seville, September |
| kingdom-of-castile 1063 vassal_start taifa-of-seville | - | missing | Abbad II page: 'In 1063, when Ferdinand I appeared with an army on the outskirts of Seville', al-Mu'tadid had to acknowledge his suzerainty and pay tribute; neither kingdom-of-castile nor kingdom-of-leon records it (the schema puts vassal_start in the overlord's ledger) |
| taifa-of-zaragoza 1013 found caliphate-of-cordoba | caliphate-of-cordoba 1018 loss | mismatch | five years apart: Zaragoza page 1013 (infobox), Taifa list 1018; flagged by the author |
| taifa-of-zaragoza 1040 loss taifa-of-lerida | - | exception | no dossier; listed in the author's counterparts_needing_dossiers |
| taifa-of-zaragoza 1060 gain taifa-of-tortosa | - | exception | taifa-of-tortosa not written yet (eu-12 part not run) |
| taifa-of-zaragoza 1076 gain taifa-of-denia | taifa-of-denia 1076 loss | mismatch | years agree; land differs: Zaragoza takes the whole Dénia 1066 shape with the Balearic Islands, Dénia gives only its peninsular possessions (Balearics to taifa-of-majorca 1076) |
| taifa-of-zaragoza 1081 loss taifa-of-tortosa | - | exception | taifa-of-tortosa not written yet |
| taifa-of-zaragoza 1081 loss taifa-of-denia | - | mismatch | taifa-of-denia has no 1081 gain; Dénia passed to al-Mundhir's Lérida-Tortosa realm ('To Zaragoza/Tortosa/Almoravids: 1076–1081 / 1081–1092'); Zaragoza should name taifa-of-tortosa |
| taifa-of-zaragoza 1096 loss kingdom-of-aragon | - | exception | kingdom-of-aragon not written yet (eu-12 part not run) |
| taifa-of-zaragoza 1110 dissolve almoravid-dynasty | almoravid-dynasty 1110 gain | matched | /ledger/25 |
| kingdom-of-pamplona 1015 gain taifa-of-zaragoza | - | missing | Sobrarbe around Aínsa; Aínsa is 36 km outside every Zaragoza shape and Zaragoza has no event; probably Pamplona's counterpart to revisit (route to the kingdom-of-pamplona owner) |
| kingdom-of-pamplona 1045 gain taifa-of-zaragoza | - | missing | Calahorra; caliphate-of-cordoba /ledger/34 hands it to Zaragoza in 1018 but no Zaragoza shape or event has it; Zaragoza must add it or the two neighbours change counterpart |
| kingdom-of-castile 1060 vassal_start taifa-of-zaragoza | - | exception | vassal_start lives in the overlord's ledger per the schema (also 1076, 1097); nothing needed in Zaragoza |
| taifa-of-algeciras 1013 found caliphate-of-cordoba | - | missing | caliphate-of-cordoba has no Algeciras entry (flagged by the author); route to its owner |
| taifa-of-algeciras 1035 loss taifa-of-malaga | - | exception | no dossier; listed in the author's counterparts_needing_dossiers; caliphate-of-cordoba uses the string 'Taifa of Málaga' for the same state, so the two strings must be reconciled when the dossier is written |
| taifa-of-algeciras 1039 gain taifa-of-malaga | - | exception | as above |
| taifa-of-algeciras 1055 loss taifa-of-seville | taifa-of-seville 1055 gain | mismatch | years agree; land wrong on both sides (see Seville 1055) |
| taifa-of-algeciras 1147 gain almoravid-dynasty | almoravid-dynasty 1147 loss | mismatch | almoravid-dynasty /ledger/40 loses Algeciras and Tarifa in 1147 to almohad-caliphate, not to this taifa; almohad-caliphate /ledger/9 (conf 3) agrees; the Abd al-Mu'min page confirms |
| taifa-of-algeciras 1168 dissolve almohad-caliphate | - | missing | no Almohad event; falls with the 1147 fix |
| taifa-of-saltes-and-huelva 1012 found caliphate-of-cordoba | caliphate-of-cordoba 1012 loss | matched | /ledger/28 |
| taifa-of-saltes-and-huelva 1051 loss taifa-of-seville | taifa-of-seville 1051 gain | matched |  |
| taifa-of-saltes-and-huelva 1147 gain almoravid-dynasty | - | missing | no Almoravid loss; almoravid-dynasty /ledger/32 gives admin1 Huelva to taifa-of-niebla in 1145 instead (overlapping land) |
| taifa-of-saltes-and-huelva 1151 dissolve almohad-caliphate | almohad-caliphate 1152 gain | matched | within one year; both conf 1 |
| taifa-of-santa-maria-do-algarve 1018 found taifa-of-badajoz | - | missing | taifa-of-badajoz has no 1018 loss; the Santa Maria infobox has 'Preceded by: Taifa of Badajoz'; route to the Badajoz owner |
| taifa-of-santa-maria-do-algarve 1051 loss taifa-of-seville | taifa-of-seville 1051 gain | matched |  |
| county-of-pallars-jussa 1011 found county-of-pallars | - | exception | county-of-pallars not written yet (eu-12 part not run); Cliopatria's Pallars row ends 1014, the division is 1011 (county-of-pallars-sobira also founds in 1011) |
| county-of-pallars-jussa 1192 loss crown-of-aragon | - | exception | crown-of-aragon not written yet (eu-12 part not run) |

## Routing

- https://en.wikipedia.org/wiki/Abd_al-Mu'min with a raw apostrophe returned url_not_found; the %27 form opened.
- No infobox of the five taifas gives an area, so area checks used shape geometry (point-in-polygon and overlap tests on the grid feature cache) instead.
- Fixes needed in neighbour dossiers owned by other groups: almoravid-dynasty (af-02) 1086 Algeciras; kingdom-of-castile or kingdom-of-leon 1063 Seville tribute; kingdom-of-pamplona 1015 and 1045 counterparts; taifa-of-badajoz 1018 Santa Maria; caliphate-of-cordoba Algeciras 1013; taifa-of-cordoba first period 1031-1070.
- No dossier edits were applied by the reviewer: every finding needs geometry or ledger restructuring by the author.

Counterparts needing dossiers: Taifa of Lérida (taifa-of-lerida, 1039-1110); Taifa of Málaga (Hammudid, and the second-period taifa 1145-1153 that Cliopatria draws as 'Taifa of Algeciras' 1085 and 1147-1168) (taifa-of-malaga, 1026-1153); Taifa of Mértola (taifa-of-mertola, 1033-1045); Taifa of Córdoba, first period (Jahwarid) (taifa-of-cordoba, 1031-1070).

Gazetteer names: Mértola (place, Portugal), Lleida (place, Spain).
