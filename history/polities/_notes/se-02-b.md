# Notes, group se-02-b (Maritime part b): kahuripan, kingdom-of-janggala, kediri-kingdom, singhasari, namayan, sultanate-of-kedah

Written 2026-10-19 by the Phase B agent for se-02-b. All six dossiers validate (`validate_dossier.py --resolve`: no unknown region names). Every page was opened with WebFetch on 2026-10-19; none failed to load. No file outside the six dossiers, this note and the report was written.

## Cliopatria rows that are wrong (checked against the grid with gazetteer.py)

- **Singhasari 1227..1293** should be 1222..1292 (Ken Arok at Ganter 1222; Kertanagara killed May or June 1292). Its first shape (73,225 km2, 286 cells) is identical cell for cell to Kediri's 1139..1226 shape: Singhasari's row is Kediri's shape carried on. Its 1285 growth (+17 cells) is **Madura**, not Bali: Bali's 24 cells are in no Singhasari shape, although the Kertanagara page dates the Bali vassalage to 1284. The dossier adds Bali as vassal land in the 1285 verdict.
- **Kediri Kingdom 1046..1226**: starts 1045 (Kahuripan page; the Kediri page says 1042) and, with Janggala's end in 1136, the enlarged 1139 shape should start in 1136. The 1220 shape should end in 1221: from 1222 Kediri is Singhasari's fief. The state is kept in one dossier to 1293 because the Kediri infobox itself reads '1042 until 1222 (1292-1293 under Jayakatwang)'; 1292-1293 is a new keyframe (Cliopatria draws it as Singhasari).
- **Kingdom of Janggala 1046..1138**: 1045..1136 (Janggala page: union by marriage in 1136).
- **Kahuripan 1028..1045**: the kingdom was founded in 1019 (new keyframe 1019..1027 on the Pasuruan-Madiun core). The 1028 shape includes Bali (22 of 24 cells); both 1046 successor shapes drop it.
- **Sultanate of Kedah 1139..1910**: not split; the pages show one sultanate (1136 to the British protectorate of July 1909) with a break in territory, not in state, between Siam's annexation (November 1821) and the restoration (1842). Start 1136, end 1909 (July). The 1294..1458 shapes carry an 18-cell Satun-Songkhla strip that no page supports and no other Cliopatria polity holds; Cliopatria's Ayutthaya takes the same 18 cells in 1459. The 1842..1910 shapes lack Setul (Kedah held it 1892..1909 per the Kedah Sultanate page) and Langkawi (that cell sits in Cliopatria's Kedah-Perlis District row, group se-03).
- **Namayan 1202..1571**: the pages say 'Established: before the 11th century' (Namayan page and the History of the Philippines table), so the dossier starts at 1000 (confidence 1, the latest year that fits). The Cliopatria outline (4 to 6 grid cells, about 1,000 km2) sits south-east of the core the Santa Ana page describes (Mandaluyong, Makati, Pasay, Pandacan, Paco), so all shapes are adjusted by adding those three admin-1 units.

## Disagreements between pages

- Partition of Kahuripan: 1045 (Kahuripan, Airlangga text, Janggala infobox) versus 1042 (Kediri Kingdom page; Airlangga infobox 'Reign: ? - 1042'). 1045 used.
- Janggala's end: 1136 by marriage (infobox and text) versus Jayabaya's conquest 1135-1157 versus 'reunited under Ken Angrok' (Legge, quoted on the same page). 1136 used.
- Pamalayu expedition: 1275 (Singhasari page) versus 'around 1290' (Kertanagara page); the Srivijaya dossier (se-02-a) dates an occupation of Palembang to 1288. The Melayu vassal tint is dated c. 1290 at confidence 2.
- Reigns of Tohjaya and Visnuvardhana: infobox 1248-1250 and 1250-1268, body text 1248-1268.
- Kedah's conversion: 1136 (chronicle, infobox) versus 1474 (an Acehnese account).
- The Siamese date of Perlis's separation: 1839 or 1843 (20 May on the page, 20 April in the infobox).

## Seams with other groups

- The Bali dossier (early-balinese-kingdoms, se-02-a) records a 1284 `loss` to Singhasari; Singhasari's dossier records a vassal_start (Kertanagara page: 'subjected nearby Bali to vassalage') and a vassal_end in 1292 (Bali Kingdom page). Mataram (se-02-a) ends in 1016 and names kahuripan as successor; Kahuripan starts 1019.
- Rattanakosin (se-01) records Kedah's annexation (November 1821), restoration (1842) and the end of its suzerainty (July 1909); Kedah's dossier carries the matching `loss` and `gain`. Ayutthaya (se-01) records the 1459 gain of the Satun-Songkhla strip that Kedah's dossier records as a loss.
- Kedah's overlords before 1821 (Majapahit's Nagarakretagama, Ayutthaya's bunga mas, Malacca's 15th-century hold) are undated on the pages read; they belong to those states' ledgers. The British protectorate tint from 1909 is Britain's (eu-11).

## Counterparts and states that need a dossier

- melayu-kingdom (Melayu, Dharmasraya, Jambi): used as counterpart in singhasari (vassal c. 1290..1292); also used by the Srivijaya dossier.
- setul-mambang-segara (Kingdom of Setul, 1808..1909): used in sultanate-of-kedah (1808, 1892, 1909). Setul is read as the Satun province.
- kedah-kingdom (pre-1136 Hindu-Buddhist Kedah, 'Kedah Tua'): predecessor of sultanate-of-kedah.
- kubang-pasu (Kingdom of Kubang Pasu, born in the partition of Kedah; absorbed into Kedah, undated).
- Not mine: kedah-perlis-district (se-03) holds Perlis and, on the grid, Langkawi and a Kubang Pasu cell.

## Not settled (per state)

- kahuripan: where Watan Mas was (capital dot at Madiun is a placeholder); when Central Java and Bali were added (Cliopatria's 1028 is not on the page); whether Bali was held directly or as an ally; the date of the peace with Srivijaya.
- kingdom-of-janggala: no neighbour, boundary or vassal on the page besides Kediri; the 1049-1052 war is on the Kahuripan page only.
- kediri-kingdom: tributaries in southern Kalimantan and the Maluku and 'colonies' including Bali (c. 1225 Chinese account, Kediri page) are undated and unlocated, so no vassal tint is drawn; a Zhu Fan Zhi page would date them. The month of Jayakatwang's fall; his capital in 1292-1293 (Daha assumed).
- singhasari: which of the old Kediri land was ruled directly from Tumapel; undated submissions of Madura (kept as a gain at confidence 1, the year is Cliopatria's), Borneo, the Maluku, Sunda ('possibly'), Pahang; the Champa alliance is not territory.
- namayan: founding year, any change of extent, barangays beyond the five named, Rajah Kalamayin's domain in the 1570s; the pages mention no vassal tie to Majapahit, Brunei, Tondo or Maynila (only legends).
- sultanate-of-kedah: the 1294-1458 strip; the capital before Alor Setar (Bukit Meriam in 1136, Kota Kuala Muda, Kota Star); Kubang Pasu's absorption; the 1895 southern cell (100.62E 5.18N, Perak's in 1842-1876); Langkawi; Setul's extent.

## Pages read and not cited

- Jayabaya (read for kediri-kingdom): reign 1135-1159, 'credited with the reunification of the Kediri Kingdom following a division'; it dates no conquest of Janggala. Not cited.
