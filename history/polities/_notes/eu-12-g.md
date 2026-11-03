# Notes, batch eu-12-g (Iberia and the taifas, part g)

Written 2026-10-25 by the Phase B research agent. States: taifa-of-arcos, taifa-of-carmona, taifa-of-granada, taifa-of-moron, taifa-of-murcia, taifa-of-niebla. All six dossiers validate (`validate_dossier.py --resolve`: 0 errors; Granada has 2 warnings, the counterpart slug `taifa-of-malaga`, which needs a dossier). Every page was opened with WebFetch; the Wikipedia pages for the minor taifas are short and give no area, no boundary and almost no towns, so most Cliopatria outlines are unverified (verdict ok or adjust with that said).

## Rows to split, merge or reassign

- No Cliopatria row needs splitting or merging in this batch. No new slugs were created.
- Taifa of Málaga (Hammudid 1026-1057, Zirid 1057-1073, Tamim 1073-1090, later Almohad and Nasrid) has no Cliopatria row and no dossier in this batch; Granada's ledger names it as `taifa-of-malaga` (1056 gain, 1073 loss). It should be written by the additions batch eu-12-x. The Taifa of Málaga page (opened) gives its rulers and dates; its infobox area is empty.
- Taifa of Tejada and the Order of Santiago appear only in notes (Tejada: Yusuf al-Bitruyi, Niebla's second-taifa ruler, was "in Tejada 1146-1150"; the Order of Santiago threatened Murcia in early 1243, per the Treaty of Alcaraz page).

## Cliopatria rows that are wrong or displaced (details in each keyframe_review)

- Taifa of Murcia: 1015-1033 and 1066-1084 draw an independent state where the page has a dependency of Almería and Valencia (1014-1065) and a Sevillan occupation (1078-1091); 1152-1176 (77,869 and 70,031 km2) are about 2.5-2.8 times the land the page names (Murcia, Valencia, Dénia = 27,800 km2) and run to 1176 though the Almohads took Murcia in 1172; there is no shape for 1177-1235 (Almohad, then Ibn Hud's rebellion of 1228) or 1250-1266 (Castilian vassal).
- Taifa of Granada: 1015-1065 includes the Jaén district before Habbus's push of c. 1028-1029 and omits Málaga until 1066 (the pages say 1056/57); 1072-1084 keeps Málaga after Tamim took it in 1073; 1085-1093 runs three years past the Almoravid capture of September 1090.
- Taifa of Carmona: 1066-1071 draws a Carmona state after Seville's conquest (1066 or 1067); 1147-1151 does not contain Carmona (it lies on the northern Sevilla and Córdoba provinces) and runs past the Almohad conquest of 1150.
- Taifa of Arcos: the four shapes are one outline; the row stops in 1071, but the page has the first taifa to 1068 (the city page says Seville took it in 1053) and a second one 1143-1145.
- Taifa of Morón: two identical shapes; the page runs c. 1010-1066 (Cliopatria 1015-1065).
- Taifa of Niebla: the 1015-1017 shape precedes the taifa (established 1023); all five shapes are one outline in Huelva province 22-35 km north of the town of Niebla, which they do not contain; the row ends in 1249 but the third taifa lasted to 1262.

## Disagreements between pages

- Murcia: the downfall of the Caliphate is 1011 (infobox) or 1031 (text); independence 1011-1014, 1065-1078, 1145, 1147-1172, 1228-1266 (text) against the infobox "To Valencia: 1145-1147"; annexation by Castile 1243 (treaty), 1266 (infobox), 1304 (Torrellas).
- Granada: Málaga annexed 1056 (Granada page, conquest page) or 1057 (Taifa of Málaga page); governor Buluggin (son) or Tamim (brother); the Écija battle of 1039 is a Zirid victory (Granada page) or a Malagan victory with Granadan help (Málaga page); Almería a "vassal state for several years" after al-Funt (Granada page) against a Valencian occupation 1038-1042 (Almería page).
- Carmona: the first taifa ends 1066 (Carmona page), by 1067 (city page) or 1091 (overview table).
- Arcos: Seville's takeover 1068 (Taifa page, table) or 1053 (city page); the Almoravids from 1101 (Taifa page) or 1091 (city page).
- Niebla and Saltés/Huelva: Seville took Niebla in 1053 and its neighbour in 1051.

## Not settled (page silent) and pages not opened

- Murcia: the extent of Ibn Mardanish's realm and the dates of his gains of Valencia and Dénia (the Ibn Mardanish page is thin); Jaén, Granada and Carmona under him are on no page opened. Pages not opened for want of budget: Battle of Fahs al-Jullab, Conquest of Murcia in 1243, Conquest of Murcia (1265-1266), Taifa of Almería (as Murcia's owner), Taifa of Valencia. A gap-filler should open a fuller Ibn Mardanish source first.
- Granada: what land the Zirids took from Almería in 1038 and "to the west" in 1039; when and to whom Granada lost its northern and eastern edges by 1085; the parias to Alfonso VI (1080s, no years; the Castile dossier should carry vassal_start with counterpart taifa-of-granada). Not opened: Siege of Granada (1018), Battle of al-Funt, Battle of Arjona, Battle of Cabra.
- Carmona: any town or district beyond the capital; the second taifa's ruler; the Birzalid article (not found under "Birzalids").
- Arcos: the frontier; who held it 1068-1143 beyond Seville and the Almoravids.
- Morón: the founder, the extent, any war before 1066.
- Niebla: the founding dynasty; the third taifa's ruler and its relation to Castile in 1248-1262 (tributary or not); the Ibn Mahfuz article did not load.
- No infobox area on any of the pages (all six states); no factor-of-two comparison was possible except Murcia's 1152 shape against the three named provinces (computed with the gazetteer, not from a page).

## Convention used for vassalage from the vassal's side

The schema's vassal_start/end have the suzerain as the author. Murcia's 1243 vassalage to Castile (Treaty of Alcaraz) is carried in Murcia's dossier as a `rename` caption event with the page's words; Castile's dossier should carry `vassal_start` (counterpart `taifa-of-murcia`, April 1243) and `vassal_end` (1266), and the gains of Lorca and Mula (1244) and Cartagena (1245). Granada's 1038 vassalage of Almería is a proper `vassal_start`/`vassal_end` (Granada being the suzerain).

## Mirrors the neighbouring dossiers should carry

- Seville: gains of Morón 1066, Carmona 1066/67, Arcos 1068 (or 1053), Niebla 1053; Murcia 1078; the 1036-1039 contest with Granada.
- Almoravids: losses of Carmona c. 1143, Arcos 1143, Niebla 1145, Murcia 1145; gain of Granada September 1090.
- Almohads: gains of Murcia 1172, Niebla 1150, Carmona 1150, Arcos 1145; losses of Murcia 1228 and Niebla 1234.
- Castile (crown-of-castile, kingdom-of-castile): Córdoba 1236, Lorca and Mula 1244, Cartagena 1245, Murcia 1266, Niebla 1262; the Jerez contest 1231-1236.
- Emirate of Granada: Jaén district 1232 (Ibn Nasr) and Granada 1237 from Ibn Hud's Murcia.
- Valencia, Dénia: the 1152 gains by Ibn Mardanish (dates are Cliopatria's).
- Almería: Granada's 1038-1041 suzerainty; Murcia 1014-1065.

## Gazetteer names needed (all used as lon/lat circles in the dossiers)

Niebla, Carmona, Arcos de la Frontera, Morón de la Frontera, Jerez de la Frontera, Medina Sidonia, Mula, Écija, Cabra, Aznalcázar, Dénia, Tejada (places); "Al-Andalus" would be a better name than "Andalusia" for Ibn Hud's 1228-1235 realm (region, most of the south of Iberia).

## Repair of taifa-of-murcia (2026-10-25, after the adversarial review; supersedes the Murcia statements above)

Verdict was fail; all nine findings applied after re-opening: Ibn Hud, Taifa of Valencia, Taifa of Murcia, Muhammad ibn Sa'd ibn Mardanish, Muhammad ibn Mardanis (es), Muhammad I of Granada, Almería, Taifa (overview list), History of Seville, Siege of Seville and Treaty of Alcaraz. The dossier validates with --resolve (0 errors, 0 warnings; 30 events, 18 keyframes, 12 sources). Taifa of Seville (opened) is silent after 1091. The other five dossiers (Arcos, Carmona, Granada, Morón, Niebla) were not touched (verdicts fix, thin, pass).

What changed:
- /ledger/14 (May 1228): the region is the Murcia core only. Ibn Hud page: 'seize most of al-Andalus relatively unopposed, except Valencia, where he was opposed by Zayyan ibn Mardanish'; Taifa of Valencia page: Zayyan 'remained independent of Ibn Hud'. The 1228 Andalusia gain (/ledger/12) excludes Valencia and Castile's 1225 gains (Andújar, Baeza, Martos).
- /ledger/19 ('nobody' 1236) deleted. Dated losses instead: Jaén 1232, Niebla 1234 (Taifa overview list: 'Niebla: 1234-1262'), Córdoba 1236, Granada May 1237, Almería 1238 (Almería page: 'After Ibn Hud's assassination in Almería in 1238 ... Emirate of Granada'), Málaga 1239 (Muhammad I page), and Seville with the south-west in 1238 to 'Banu al-Bajji' at confidence 1. NOT SETTLED: no page opened says who held Seville and the west between January 1238 and the Castilian conquest of 23 November 1248; the Banu al-Bajji (named by the Muhammad I page only for 1234) are a placeholder.
- /ledger/4 (1091 to the Almoravids) deleted; it is Seville's loss (Almoravid dossier ledger/18 should name taifa-of-seville).
- /ledger/7: Valencia dated to August 1147 (Taifa of Valencia page), confidence 2, with Castellón (castle of Montornés, 1147/8). /keyframe_review/4 now adjust, includes Valencia and Castellón (1147-1148); new keyframe 1149-1151 adds Alicante.
- /ledger/8: Dénia/Alicante dated to June 1149 at the latest (Genoese funduqs 'at Valencia and Dénia'), counterpart almoravid-dynasty, confidence 1; the page gives no date for the gain. Cliopatria's 1152 is not supported.
- /keyframe_review/5 and 6: the cut to 27,800 km2 is WITHDRAWN. I disagree with my first pass: Cliopatria's 1152 outline holds Castellón, Albacete, Cuenca, most of Teruel and the eastern edges of Jaén, Granada and Almería, and the Spanish article gives Ibn Mardanish Segura, Baza, Guadix, Úbeda (Jaén district, 1159), so a cut to three provinces had no page behind it. Kept as Cliopatria draws it, unverified, with a confidence-1 bridging gain in 1152 for the part no page dates. Albarracín is ceded by 1168 (es: 'entre 1165 y 1168', to Pedro Ruiz de Azagra), removed by a new 1168 keyframe; the 1169 north-east strip (8,350 km2, wholly inside Cliopatria's Crown of Aragon 1169) is a confidence-1 loss to crown-of-aragon, while the es article dates Tortosa to 1148 and Lérida and Fraga to 1149.
- /ledger/11 (1172): confidence 2; Taifa of Valencia page added in the note and in sources[]; region is Cliopatria's 1169 outline without Albarracín.
- /keyframe_review/9 (1241): verdict ok, outline unchanged; the cut is carried by /ledger Lorca and Mula 1244, Cartagena 1245 and the 1250 keyframe. The Taifa overview list has 'Lorca: 1240-1265 (to Castile)' and 'Orihuela: 1239/1240-1249/1250', which sits uneasily with the Treaty of Alcaraz page (Lorca, Mula and Cartagena refused the treaty in 1243); the treaty page is followed.
- /ledger/18: contest at Jerez closes in 1235 (the Kingdom of Castile dossier ends then), confidence 1; Córdoba is the 1236 loss to crown-of-castile.
- 1228-1239 keyframes are now yearly where the border moves (1228, 1232, 1234, 1236, 1237, 1238, 1239), built from the same region specs as the events so that events and frames agree.

Not recorded (page range or fate vague): Écija and Carmona 1158-1160 ('conquistó Écija y Carmona (1158-1160)', Carmona lost 1161; outside the Cliopatria outline), Almería under Ibn Mardanish (Almería page 1165-1169, es article defection in 1171), Quesada lost 1171, Lorca, Elche, Baza and Alcira in revolt in 1171.

Mirrors for other dossiers (flagged, not edited): af-02, Almohad ledger/17 (Dénia 1152 from taifa-of-denia; Dénia was Ibn Mardanish's from 1149 at the latest to 1172) and ledger/46 (gives Murcia the whole rest of Almohad Spain and Portugal in October 1228, wider than the Andalusia drawn here); Niebla ledger/4 (1234 gain should name taifa-of-murcia); Valencia (Ibn Mardanish 1147-1172, Zayyan 1228/9-1238, Valencia stays outside Ibn Hud); Emirate of Granada (gains from taifa-of-murcia: Jaén 1232, Granada May 1237, Almería 1238, Málaga 1239); Crown of Aragon (1169 strip). Counterparts without dossiers: Pedro Ruiz de Azagra and the Lordship of Albarracín (1168), Banu al-Bajji of Seville (1238-1248).
Gazetteer names added to the list: Albarracín (place, Teruel; used as a 25 km circle at -1.44, 40.41).
