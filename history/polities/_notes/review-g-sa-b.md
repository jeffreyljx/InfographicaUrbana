# Review of gap batch g-sa-b (2026-11-01)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. All six dossiers validate (`--resolve`: one warning, the `tarkhan-dynasty` counterpart, which has no dossier yet). Every neighbour named in the author's brief has a dossier, and each was cross-checked. Spot checks: 22 events; every page said what the note claims, with the year. No fabricated or mis-dated event was found.

Verdicts: arghun-dynasty thin; chahamanas-of-ranastambhapura thin; chalukyas-of-lata thin; hunza-and-nagar thin (one unapplied shape fix); kangra-state **fail** (shape over Chamba and Nurpur, 1789 counterpart, no capital); panduvamshi-dynasty fix (applied by the reviewer).

Convention note: the schema puts vassal_start/vassal_end in the suzerain's ledger, with the vassal as counterpart. The authors did not mirror them in the vassal's ledger. Missing mirrors are listed as thin, not as faults.

## arghun-dynasty: thin
- Confirmed: 1520 invasion and defeat of Jam Feroz (Arghun page); December 1520 reign start (Shah Beg page infobox: '21 December 1520'); Multan 'fell in 1528 after an extended siege'; Tarkhan election 'as their ruler in 1554', with the infobox ending in 1554.
- Gap: the 1530 Multan loss (/ledger/6) is a confidence-1 bridge to a non-slug counterpart. mughal-empire has no Multan gain around 1530, and sur-empire/ledger/5 gains Multan in 1541 from an unnamed holder, so nobody holds Multan 1530-1541. Try the Kamran Mirza page.
- Mismatch: sur-empire/ledger/7 (confidence 1, placed in 1544) gains 'upper Sindh as far as Sehwan' (150 km round 68.4 E, 27.0 N, which includes Bukkur) from unnamed rulers. The Arghun keyframe for 1530-1554 keeps all of Sindh. One of the two must change: the Arghuns record a loss, or the Sur event names arghun-dynasty or is dropped.
- Area: no infobox area. The Samma 1521 shape (123,201 km2) is used, as acknowledged.

## chahamanas-of-ranastambhapura: thin
- Confirmed: established 1192; Iltutmish 'captured the fort in 1226 CE'; recapture under Razia (r. 1236-1240), honestly kept at confidence 1; fall in July 1301 (siege page; Firishta gives 10 July 1301).
- Missing: 'Balhana is recorded as a vassal of the Delhi Sultan Iltumish in 1215 CE'. Neither this dossier nor mamluk-dynasty records it. mamluk-dynasty also lacks the c. 1236 loss of Ranthambore.
- Chauhan's 1194 dissolve against this 1192 found: a 2-year overlap that R2 settles.

## chalukyas-of-lata: thin
- Confirmed: c. 970 to c. 1070 (infobox), 'feudatories of the Western Chalukyas in their early years'; Bhoja's invasion 'around 1018 CE'; Kirtiraja 'regained control of the region within a short time' (Chaulukya page, undated, so confidence 1 is right).
- KF0 (970-1017) claims Lata from 970, but the ledger gains it only in 1009 with no loss in between. Compiler rule R2 gives 970-1008 to the Chaulukyas, so the map is right, but the dossier contradicts itself. Start KF0 in 1009, or model 970-1008 as a vassalage.
- Missing: the vassalage to western-chalukya-empire (the Chaulukya page: Kirtiraja 'a vassal of the Kalyani Chalukyas') and Bhoja's brief overlordship; no capital.

## hunza-and-nagar: thin
- Confirmed: Hunza 'established in around 1200'; Nagar 'established in the 14th century' (infobox c. 1300); 'Hunza acceded to Pakistan on 3 November, followed by Nagar on 18 November' (Gilgit-Baltistan page).
- Area: Hunza infobox 3,900 sq mi (10,100 km2) against the 56 km disc of 9,850 km2. Fine.
- Unapplied fix: the 70 km disc (KF1, /ledger/1, /ledger/2) contains Gilgit town, 59 km south-west of the centre. Gilgit was Kashmir's, not Hunza's or Nagar's. Use `{"minus": [{"lon": 74.7, "lat": 36.35, "km": 70}, {"place": "Gilgit", "km": 25}]}` (48 cells).
- Missing mirrors: vassal_start 1891 / vassal_end 1947 of british-raj and kashmir-and-jammu. Nagar page: 'Between 1891 and 1947, it maintained a subsidiary alliance with British India'.
- Missing on both sides: Qing tribute 'from around 1760' (last in 1938) and the Dogra tribute of 1860.
- Note: the states lasted inside Pakistan until 1972 (Nagar) and 1974 (Hunza). Ending at accession matches the neighbours.

## kangra-state: fail
1. /keyframe_review/0 and /keyframe_review/2: the 60 km disc takes in the seats of Chamba (32.56 N 76.13 E) and Nurpur (32.30 N 75.88 E), and Guler. 8 of its 39 cells lie within 30 km of Chamba or 20 km of Nurpur, and 5 lie outside Himachal Pradesh on the Punjab plain. The dossier's own 1794 event treats Chamba as a separate state ('Chamba's Raja Raj Singh was killed'). Fix: `{"minus": [{"minus": [{"intersect": [{"lon": 76.27, "lat": 32.1, "km": 60}, {"admin1": "Himachal Pradesh", "country": "India"}]}, {"lon": 76.13, "lat": 32.56, "km": 30}]}, {"lon": 75.88, "lat": 32.30, "km": 20}]}` (27 cells). Draw KF1 as the same minus the 25 km fort disc, and use the same region in /ledger/0.
2. /ledger/2 (1789 gain from mughal-empire, confidence 3): the Kangra State page has Sansar Chand oust the Mughal governor Saif Ali Khan in 1783, 'aided by the Kanhaiya misl', and recover the fort 'in 1789'. Record the Mughal exit in 1783. Give 1789 the counterpart sikh-confederacy (Kanhaiya misl) or nobody, at confidence 2.
3. /identity/capitals is empty. Add Kangra fort (76.27 E, 32.10 N), noting that the page names 'the fortress of Kangra', not a capital.
- Confirmed: the fort surrendered 'in November, 1620'; 1789 recovery; Battle of Rehlu 1794 (fought 'near present-day Rait village', which can be the region of /ledger/3); Jawalamukhi 1809 and the Sikh annexation (infobox 1810).
- Gaps: founding (11th century, confidence 1); Mughal vassalage of the Katoch rajas 1620-1783 (mughal-empire has no Kangra event at all); Sansar Chand's undated expansion.

## panduvamshi-dynasty: fix (applied)
- Applied: /ledger/0 confidence 1 -> 2. The page says 'Shastri dates the beginning of the Panduvamshi rule in Dakshina Kosala to c. 620 CE'. Re-validated and read back.
- Confirmed: the reign list (Shastri, Indrabala c. 620-640 to Balarjuna c. 730-790); 'no record of Panduvamshis after Balarjuna'; capital Sirpur. The 790 end stays at confidence 1, thin by design.
- Cross-dossier: nala-dynasty (successor Panduvamshi, Bastar and Koraput, 580) and somavamshi-dynasty (found 882, counterpart panduvamshi-dynasty, Sambalpur) both disagree with this page's chronology and land. Their owners should revisit.
