# Notes, batch eu-19-c (Caucasus, part c), read 2026-10-25

Five dossiers written and validated (python3 -I tools/validate_dossier.py, 0 errors): kingdom-of-lazica, principality-of-iberia, kingdom-of-the-iberians, shirvan, bagratid-armenia. All pages are English Wikipedia, opened with WebFetch on 2026-10-25. No dossier existed beforehand; no sibling eu-19 dossier existed when this batch finished.

## Cross-cutting

- Colour family: `near-east` for the four Georgian/Armenian states, `persia` for Shirvan. The families list has no Caucasus entry; the colour agent may prefer one shared family for the group.
- Slugs used as counterparts that no dossier has yet (validator warns, by design): emirate-of-tbilisi (736-1122), kingdom-of-abkhazia (778-1008, Cliopatria's Georgia row), kingdom-of-syunik (987-1170), kingdom-of-tashir-dzoraget (979-1118), kingdom-of-artsakh, principality-of-kakheti, kingdom-of-kars (to 1065). Another batch of eu-19 (eu-19-x, or the georgia split) should write them.
- Vassal relations in which one of my states is the vassal belong in the suzerain's dossier (vassal_start/vassal_end with counterpart = the vassal's slug); I could not write them. List: Lazica to the Byzantine Empire (562-c. 697, patricius) and to the Arabs (c. 697 on); Iberia to the Umayyads/Abbasids (640s, 724 on); Shirvan to the Seljuks (1063-1194), Georgia (1120-1130s, 1190s), Khwarazmshah (1225), Mongols/Ilkhanate (1206-1368), Jalayirids (1335-), Timur (1386-1405), Safavids (Dec 1500-1538). The Bagratid side of Syunik (885-987, 988-1045) and Tashir-Dzoraget (979-1045) is in bagratid-armenia.
- Page budget exceeded only where a page was shared between dossiers: principality-of-iberia (4 pages for a 1-2 budget; the Emirate of Tbilisi, Arab-Khazar wars and Kingdom of the Iberians pages are also the sources of its neighbours).

## kingdom-of-lazica (638-777, 6 shapes)

- One state with `lazica` (-63..545): same Wikipedia article, same Wikidata Q136884. Not merged because the earlier slug belongs to another batch. If merged, drop this dossier, put both Names in lazica's cliopatria_names and take the three events and six verdicts here. The 546-637 gap (except Georgia 567-576) is unverified by anyone.
- The page ends the kingdom in 697 (infobox; last Patricius acknowledged Arab suzerainty c. 696/697); Cliopatria and the Kingdom of Abkhazia page ('Leon II ... acquire Lazica in the 770s') carry it to 777/778. Kept 777.
- The only shape change (724, -21 percent) has no page: ledger event at confidence 1. Pages thin: Lazica, Kingdom of Abkhazia, Abasgia (silent), Arab-Khazar wars.

## principality-of-iberia (588-813, 3 Cliopatria shapes)

- Cliopatria covers 682-740 only; two new keyframes (588-681 Kartli, 736-813 Kartli without Tbilisi). The page runs the principality to 888; this dossier ends in 813 when Ashot I settles in Klarjeti and hands the line to kingdom-of-the-iberians (Cliopatria's 814-999 row). Reasons in the dossier; the alternative is to end here at 888 and move the 814-887 shapes.
- Kartli outside Tbilisi 814-887: no page opened says who held it. The georgia dossier (eu-19) draws a large 888-910 shape; reconcile there.
- Dates differ: Arabs take Tiflis 724 (Arab-Khazar wars), Marwan II takes it 735 (Emirate text) or 736 (infobox).

## kingdom-of-the-iberians (813-1008, 6 shapes)

- Cliopatria row is Tao-Klarjeti only; Kartli under Gurgen and Bagrat III (976-1008) is in Cliopatria's Georgia row. Start 813 (page: 'Principality (c. 813-888)'), rename 888, end 1008 against Cliopatria's 999.
- Tao lost to Byzantium in 1001 (or 1000; pages disagree; scope disputed; the Bagrat III page says the emperor 'completed the conquest of Tao-Klarjeti'). 'Tao' and 'Klarjeti' are not in the gazetteer.
- 903-904: the Kingdom page (Adarnase dispossessed by Constantine III in 904) and the Smbat I page (Smbat annexes Klarjeti and Ardahan in 903) do not agree; both dossiers record what their page says.

## shirvan (861-1538, 16 shapes)

- One state (Shirvanshahs). First shape (825-839, 113 k km2) is not Shirvanshah land: verdict wrong. Gaps 840-860, 1085-1125, 1236-1343, 1385-1414 filled with new keyframes (confidence 1-2). Row does not need splitting. Start 861 (Shirvanshah page) against 'from 809' (Shirvan page).
- 1126-1138 shape (5.7 k km2) lies west of Shamakhi; the page gives western Shirvan to Georgia in 1124. Treated as the annexed part; eastern Shirvan is the 1139 shape minus it. Verify against the gazetteer cells.
- The Layzan page is the village of Lahij, silent; the Mongol page is silent on Shirvan. Rus raids of 913-943 and the Sallarid period are not on the pages opened.
- Capitals: Shamakhi to 1190, Baku from 1191 (approximate; Ibrahim I died at Shamakhi in 1417).

## bagratid-armenia (885-1045, 11 shapes)

- Start 885 (infobox Ashot I 885-890, Bagaran) against Cliopatria 886; found keyframe is a radius around Ani.
- 1000, 1010 and 1028 shape changes rest on Cliopatria and silence (confidence 1). The 898 shape is split at 908 (Vaspurakan's crown), three years before Cliopatria's 911.
- Overlap with kingdom-of-the-iberians: Klarjeti and Ardahan (903 annexation on the Smbat I page; Cliopatria draws them in the Iberians row to 999).
- Bagaran and Shirakavan coordinates are approximate; Dvin is not in the gazetteer (Artashat stands in).
- Page budget (5) spent; David III of Tao, Vaspurakan and Seshat pages not opened for this dossier.

## Gazetteer names needed

Tao (region, Upper Tao/Tayk, Erzurum-Artvin-Ardahan uplands); Klarjeti (region; read as Artvin province); Phasiane (place, Pasinler plain, 39.99N 41.68E); Dvin (place, near Artashat 39.96N 44.58E); Bagaran and Shirakavan (places, Bagratid capitals); Tao-Klarjeti (region).


## Repair 2026-10-31 (bagratid-armenia, verdict fail; the other four dossiers were thin or pass and are untouched)

Pages opened again or for the first time (all English Wikipedia, 2026-10-31): Smbat I of Armenia, Bagratid Armenia, Kingdom of Syunik, Gagik I of Armenia (reopened); Yusuf ibn Abi'l-Saj, Sajid dynasty, Shaddadids, Kingdom of Kars, Hovhannes-Smbat III, Basil II (new). None failed. The dossier validates with 0 errors; the 12 warnings are counterpart slugs with no dossier yet.

Changed:
- 903 Klarjeti/Ardahan (blocking): Artvin dropped; Ardahan kept (conf 2) with a new 911 loss (conf 1, bridged to Cliopatria's 911 shape); keyframes _898 (to 901), _902, _903, _904, _908, _909 now follow the ledger. Gazetteer test: every Kingdom of the Iberians shape 814-999 holds all 32 Artvin and all 20 Ardahan cells, and no Bagratid shape holds any Ardahan, Artvin or Nakhchivan cell.
- 1022 Dvin (blocking): loss to shaddadids (conf 3, Shaddadids page), keyframes _1022, _1028, _1034, _1040 minus Dvin. 901: no pair, reasons in the 892 event (the Smbat I sentence dates Yusuf's succession, not the capture; no recovery year; the Yusuf and Sajid pages are silent).
- 909: loss of Nakhchivan to sajid-dynasty (conf 3, Yusuf page). Syunik's vassalage not ended: the Yusuf page says Yusuf gained Siunikh 'together with Gagik', the Smbat I page that he entered Syunik, the Syunik page is silent, and Cliopatria's 911-1027 shapes keep Syunik; the contest 909-914 covers it.
- 886/885: found region and the 885 keyframe are now Cliopatria's 886 shape (the reviewer's first option), because no page supports a fivefold expansion in a year.
- 963: vassal_start kingdom-of-kars (conf 2; Kars page 'formed in the year 963'), vassal_end 1045; kingdom-of-kars added as a successor.
- 1001 (was 1000): western strip to Byzantium, Basil II page 'In 1001 ... Basil inherited Tao, Phasiane and Speri'; the strip reaches Phasiane. byzantine-empire has the gain from David III, not from the Bagratids; unsettled.
- 1021 (was 1028): the loss to Syunik (conf 1) is replaced by the division with Ashot IV (Hovhannes-Smbat III page: Ashot rebelled in 1021 and after a compromise ruled 'further Armenian provinces closer to Persia and Georgia'), counterpart 'ashot-iv' (a co-king of the same house, not a state; no dossier asked), keyframes _1021 onward. The compromise has no year.
- 885 Syunik vassal_start now conf 2 (Syunik page: 'in 885, Syunik became part of the administrative territory of the emirate'; I read the emirate as Ashot's realm). 988 conf 2 (already applied by the reviewer). 989 and 1045 Syunik stay at conf 1: the Syunik and Gagik I pages give no year (reign 989-1020 only) and no end of the overlordship.

Where I differ from the reviewer:
- Ardahan is not clear of the Iberians: it lies wholly inside their Cliopatria shape, so the overlap with kingdom-of-the-iberians remains for 903-910 even after Artvin is dropped. I could not write the mirror (that dossier is thin and untouched); it would need a 903 loss and 911 return of Ardahan at confidence 2, or its author may reject the Smbat I claim.
- Klarjeti: the Smbat I page does say Klarjeti, and I left it undrawn rather than record a gain from kingdom-of-the-iberians without its mirror; the Kingdom of the Iberians page has Adarnase dispossessed by Constantine III in 904, not by Smbat.
- Gugark (Georgian-held, 'reunified with Armenia' by Smbat) has no year on the Smbat I page, and its land is already inside the shapes; no event.
- Dvin 914-1022: the pages conflict (see the 1022 event); I kept Cliopatria's drawing (Dvin inside every shape) until 1022.
- Gagik I's union of Nakhichevan, Khachen and Dvin (Gagik I and Syunik pages, no year) is not recorded as gains: no date, and the shapes show none.
- The 1028 and 1000 cuts: dated by pages now (1021, 1001) a few years or one year away from Cliopatria; the keyframes follow the pages.

Counterparts needing dossiers: kingdom-of-kars (963-1065); kingdom-of-syunik, kingdom-of-tashir-dzoraget, kingdom-of-artsakh and kingdom-of-abkhazia as before. Gaps left: who held Dvin 914-1022; the date of the Ashot IV compromise and of his lot's extent; Syunik's status 1021-1045; Klarjeti 903-904 against the Iberians dossier.
