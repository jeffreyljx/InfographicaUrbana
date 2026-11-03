# Review of batch sa-03-f (Chaulukya, Chandela, Utpala, Chauhan, Paramara, Western Chalukya)

Reviewer, 2026-10-19. Validator: 0 errors for all six (warnings: unknown gazetteer places and counterpart slugs with no dossier yet). Spot checks: 35 events on 13 pages (Western Chalukya Empire, Vikramaditya VI, Chaulukya dynasty, Vaghela dynasty, Chandelas of Jejakabhukti, Kalinjar Fort, Chahamanas of Shakambhari, Prithviraj Chauhan, Second Battle of Tarain, Paramara dynasty, Utpala dynasty, Didda, Seuna (Yadava) dynasty). Every date checked is on its page: no fabricated or mis-dated event. None of the six articles gives an infobox area, so the area check rests on the authors' cell counts (they match shapes.csv). Overlaps were measured with the gazetteer resolver (H3 r5 cells).

Verdicts: chaulukya-dynasty fail, chandela-kingdom fail, utpala-dynasty thin, chauhan-dynasty thin (2 fixes applied by the reviewer), paramara-dynasty fail (1 fix applied by the reviewer), western-chalukya-empire fail.

The failures share one cause: the batch's dossiers disagree with each other, and with the Pratihara dossier, over Lata, Konkan and the Chandela vassalage. Each date is right; the land the dossiers draw is not consistent.

## Fixes applied by the reviewer (validated afterwards)

- paramara-dynasty /ledger/13, /ledger/14, /wars/8/zones/0: the region was a 150 km disc round Ujjain, which the page does not name and which lies 200 km from Bhilsa. It is now a 60 km disc at Bhilsa (lon 77.81, lat 23.52). Paramara page: 'captured Bhilsa during 1233-34 CE, but Devapala ... regained control of Bhilsa'.
- chauhan-dynasty /ledger/11: confidence 3 changed to 2. The cited pages name Delhi but not Haryana (Second Tarain infobox: 'Muhammad Ghuri conquers much of northwestern India including Delhi').
- chauhan-dynasty /ledger/12: the type changed from loss to vassal_start (counterpart ghurid-dynasty). Second Tarain page: 'The Ghurids then appointed his son Govindaraja IV on the throne of Ajmer as their vassal'. With a loss, the dossier held no land between 1192 and its 1194 dissolve. The vassal records the vassal_start in its own ledger too (brief 2.3).

## Lata, one timeline for three dossiers (chaulukya, paramara, western-chalukya)

Lata here is the union of a 120 km disc at Vadodara and an 80 km disc at Surat: 206 cells, about 52,000 km2. The Chaulukya 960 shape (verdict ok, 960-1110) holds 192 of those cells, and its 1111 shape holds 59.
- Chaulukya ledger: loss 1007 (WC), gain 1008, loss 1064 (Kalachuris, c1), gain 1074 (c3), loss 1077 (Trivikramapala). No later event regains Lata, but the keyframes draw it every year from 960 to 1304. /ledger/4's own note says Kirtiraja 'regained control of the region within a short time, before being defeated by the Paramara king Bhoja'. Yet the ledger keeps Lata Chaulukya from 1008 to 1064.
- Paramara: /ledger/1 gains Lata in 1018 and K2 draws it for 1018-1055. K3 (1056, ok) drops it, and no event loses it. Chaulukya and Paramara therefore both claim Lata for 1018-1055.
- WC: /ledger/21 gains 62 Lata cells from chaulukya-dynasty in 1111 (c1). Chaulukya has no matching 1111 loss.
What the authors should write: Chaulukya loses Lata c. 1009 to chalukyas-of-lata (Kirtiraja). Paramara gains it in 1018 and loses it c. 1055-56; the Paramara page says that after Bhoja 'the Chaulukya king Bhima I and the Kalachuri king Karna attacked his kingdom', and the Chaulukya page says 'Meanwhile, the Kalachuris managed to capture the Lata region'. The Kalachuri hold ends in 1074, when Karna 'evicted the Kalachuris'. Chaulukya loses Lata again in 1077. The Chaulukya K2 and K3 are cut to these spans, and K3 gets an event for its 59 Lata cells or a correction.

## Konkan (paramara, western-chalukya)

Upper Konkan here is a 100 km disc at Mumbai, 68 cells. 67 of them lie inside the WC shapes of 1010, 1034 and 1040, which WC keeps through 1020-1055. Paramara K2 adds the same cells for 1018-1055 (Bhoja page: 'captured Konkana sometime between 1018 and 1020'). WC /ledger/11 then gains them back from the Paramaras in 1055, although the WC keyframes already draw them. WC should add a loss c. 1020 to paramara-dynasty, or adjust K4-K6 to drop Konkan for 1020-1054. Paramara should check its counterpart: if the Shilaharas were Chalukya feudatories, it is western-chalukya-empire, not shilahara-dynasty.

## chaulukya-dynasty: fail

- /keyframe_review/2-3 and /ledger/3-8: the Lata contradictions above.
- /keyframe_review/3: the 1111 shape gains 240 cells and loses 170, a net gain of 33,000 km2, and no event from 1077 to 1136 explains it. The Sind border (56 cells), western Rajasthan, and the 31 south-Rajasthan cells that paramara /ledger/8 loses to chaulukya-dynasty in 1111 have no gain; the 67 Lata cells that WC /ledger/21 gains from chaulukya-dynasty in 1111 have no loss. Add c1 bridges for 1111, citing the Jayasimha sentences the K3 note already quotes ('defeated ... Sindhuraja'; control 'extended to parts of present-day Rajasthan').
- /ledger/1 (947 gain from chavda-dynasty) against gurjara-pratihara /ledger/27 (942 loss of Gujarat and Kutch to chaulukya-dynasty): the two disagree on the year and the counterpart. The Pratihara dossier is being reworked (sa-03-c fail); agree one year with it (the page says 'around 940').
- Thin (gaps): /ledger/1, /ledger/2, /ledger/5, /ledger/6, /ledger/24 and /ledger/25 are c1. The Guhila (Mewar) revolt of 1207-1227 is not drawn. The Vaghela extent for 1250-1304 is unknown. /ledger/18 is a contest, but the Seuna page says Kholeshvara 'captured Lata' in 1220, which may be a loss.
- Spot checks, all confirmed: 940 (/ledger/0), 1074 (/7), 1135-36 (/9), 4 February 1197 (/16), 1201 (/17), 1304 (/23, Vaghela page).

## chandela-kingdom: fail

- The Pratihara vassalage is missing. gurjara-pratihara /ledger/18 has vassal_start 836 (chandela-kingdom) and /ledger/30 vassal_end c. 950; K0's note quotes Yashovarman, who 'continued to acknowledge the Pratihara suzerainty'. Add vassal_start (836, or 831) and vassal_end 950.
- Gwalior: gurjara-pratihara /ledger/31 records a 950 loss of Gwalior to chandela-kingdom ('the Chandelas captured the strategic fortress of Gwalior ... around 950'), but no Chandela keyframe draws Gwalior: the 960 shape's bbox starts at 78.82 E, and Gwalior is at 78.18 E. Add a gain, or agree with the Pratihara group to change the counterpart.
- /ledger/2 against /keyframe_review/1: K1 draws the whole Cliopatria 960 shape from 950, but the ledger gains the rest of that shape only in 960 and Kalinjar in 954. Move /ledger/2 to 950 (Dhanga's accession, the K1 start and the Pratihara vassal_end). K0's 80 km Khajuraho disc also holds Kalinjar, 59 km away, from 831; but the Kalinjar Fort page has Kalinjar Pratihara by 836 and taken from the Kalachuris only 'before 954'. Shrink K0 to leave Kalinjar out.
- Thin: K6 and K7 grow by 6 and 24 cells (northern Baghelkhand, about 6,000 km2) with no event. The page has 'Madanavarman defeated the Kalachuri king Gaya-Karna, and possibly annexed the northern part of the Baghelkhand region': a c1 or c2 gain under Madanavarman (1128-1164) would explain them. /ledger/4 (1060) and /ledger/5 (1085, Gahadavala) are c1. The Khalji end in 1315 is not dated on any page.
- Spot checks, all confirmed: 831 (/0), before 954 'from the Kalachuris' (/1), 1182-83 (/6), 27 April 1203 (/8, Kalinjar Fort page: 'on 27 April 1203, the fort's garrison surrendered'), 1315 (/10).

## utpala-dynasty: thin

- Identity, for the orchestrator to decide: the schema says 'a dynasty that merely succeeds another on the same land without a break is not a new dossier'. kashmir (625-1339) already draws the same land with renames in 855 and 1003, so the Valley is painted twice for 855-1003. Either add 'Utpala Dynasty' to kashmir's cliopatria_names, carrying these three 'wrong' verdicts, and retire this dossier, or have the compiler draw only kashmir. The author flagged this.
- Thin: /ledger/1 (860, c1), and the extent outside the Valley (Shankaravarman's 'swath of territory', the Udabhanda expedition).
- Spot checks, all confirmed: 855 (/0), Didda's death on 8 August 1003 (/2), 'frontier territories remained outside Kashmir sovereignty' (K0), the capital Avantipur.
- Area: Cliopatria 174,993 km2; the correction resolves to 61,960 km2 (245 cells), a ratio of 2.8, which is acknowledged and reasoned (verdict wrong).

## chauhan-dynasty: thin (fixes applied)

- Applied: /ledger/11 and /ledger/12 (see above).
- Thin: /ledger/4 (1056 loss to the Ghaznavids, c1) is the largest unexplained move: 189 Rajasthan cells, a quarter of the shape. /ledger/1 (980, c1) disagrees with gurjara-pratihara /ledger/32, which loses all of Rajasthan to chauhan-dynasty in 960. /ledger/3 (1056) is c1. Hariraja's partial recovery of 1192-1194 is missing (Chahamana page: 'dethroned him, and regained control of a part of his ancestral kingdom'), and the extent for 980-1150 is unknown.
- Spot checks, all confirmed: c. 1040 (/2), 1182-83 (/7), 1190-91 (/9), 1192 (/10, /11, /12), 1194 (/13).

## paramara-dynasty: fail (1 fix applied)

- /keyframe_review/3 and /ledger: the Lata loss is missing (see Lata above). The Konkan double claim with WC is described above.
- /ledger/11: the counterpart 'Ballala (usurper)' is free text and not in counterparts_needing_dossiers, so no dossier holds Malwa for 1143-1150. List Ballala, or set the counterpart to 'nobody' and keep the name in the note (the same goes for chaulukya /ledger/12).
- Cross-check: gurjara-pratihara /ledger/25 (936) and /ledger/33 (960) lose Malwa to paramara-dynasty, which starts only in 948 (infobox 'Established: 948'). The Pratihara side should move.
- Thin: K5, the rump of 1136-1177 outside Malwa, is unconfirmed. /ledger/5, /8, /14 and /15 are c1. The 1236-1304 extent is unknown. Naravarman's losses to the Chandelas (Madanavarman's Bhilsa) are undated.
- Spot checks, all confirmed: 1018 and 1018-1020 (/1, /2), 1135-36 (/9), 1142 (/10), 1233-34 (/13, region fixed), 1305 (/16), 24 November 1305 (/17).

## western-chalukya-empire: fail

- /ledger/17 (1088, c2): the region is the whole Vengi union (218 cells, 55,000 km2), but the page says only 'conquer parts of Vengi in 1088' and 'held the Kollipakei-7000 province'. K6 has no Vengi (1 of the 218 cells) until 1093, and /ledger/19 gains the same region again in 1093. Narrow the region to the Kollipakei province (Kollipaka, Nalgonda; a gazetteer place is needed), or record a contest instead.
- /ledger/11 and K4-K6: Konkan (see above).
- Cross-checks with chola-empire, mostly for the Chola side, which is being reworked (sa-03-e fail): the Chola contest starts in 1003 against WC's 1007. The Chola dossier has no mirror for 1010, 1034, 1040, 1052, 1066-68, Kanchi 1085-89, or Vengi 1088 and 1093-1099. The Chola dossier keeps Vengi from 1075 to 1118, while the Vikramaditya VI page has 'Vengi came under his rule again from 1093 to 1099'.
- Thin: /ledger/4, /6 and /7 (the 1010-1040 southern strip, c1). The 980-1009 Mysore-plateau strip overlaps Chola Gangapadi (998), and the +22,000 km2 of 990 has no event. /ledger/18 (1089), /21 (1111), /24 (1126) and /27 (1177) are c1. The Chola-Chalukya wars page failed for the author in both encodings; try https://en.wikipedia.org/wiki/Jayasimha_II_(Western_Chalukya) and https://en.wikipedia.org/wiki/Someshvara_I instead.
- Spot checks, all confirmed: 1042 (/8), 1085 (/16, 'seized Kanchi from the Cholas in 1085'), 1093 and 1099 (/19, /20), 1118 (/22), 1133 (/25), 1157 (/26), c. 1187 (/29).

## Gazetteer names needed

Anahilapataka (Patan), Mount Abu, Nadol, Khajuraho, Kalinjar, Baghelkhand (region), Bathinda, Ranthambore, Basavakalyan, Vidisha (Bhilsa; now a lon/lat disc), Kolanupaka (Kollipaka; for the WC fix).
