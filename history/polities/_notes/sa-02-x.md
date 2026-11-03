# Notes, research batch sa-02-x (Maurya to Gupta, additions)

Seventeen new dossiers written on 2026-10-19, all states Cliopatria lacks (cliopatria_names []): nagas-of-padmavati, abhira-dynasty, traikutaka-dynasty, andhra-ikshvaku, chutu-dynasty, aulikara-dynasty, ruhuna, western-ganga-dynasty, vishnukundina-dynasty, salankayana-dynasty, ananda-gotrika-dynasty, nala-dynasty, davaka, kuninda-kingdom, kalachuris-of-mahishmati, mathara-dynasty, later-gupta-dynasty. All validate (python3 -I tools/validate_dossier.py --resolve: 0 errors; the only warnings are the counterpart slugs pitrbhakta-dynasty and pushyabhuti-dynasty, which have no dossier). 32 distinct Wikipedia pages are cited (34 were opened; Mitra_dynasty is a list of several dynasties and Samatata is 4th-13th century, neither became a dossier). WebFetch returns a model-written extract of the page, not the raw text: quotation marks in the notes are the extract's own where it used them; other statements are paraphrase. Overlap numbers (cells of Cliopatria shapes under each region) were computed with the gazetteer library from the regions written in the dossiers.

## What other dossiers need from these (not edited here)

- kadamba-empire (sa-02-d): the Banavasi founding in 345 should list chutu-dynasty as predecessor (the Chutu page: "The Kadambas occupy Banavasi, which ends Chutu rule there").
- satavahana-dynasty (sa-02-b): vassal_start c. 125 and vassal_end c. 225 for chutu-dynasty (the Chutus were Satavahana feudatories; Cliopatria draws their land as Satavahana to 223).
- gupta-empire (sa-02-d): Cliopatria draws the Gupta shape over Kalinga (all 149 cells around Vishakhapatnam) from 347; the Mathara page says Samudragupta's forces had withdrawn from the region and the Matharas rose from c. 350. Also over the Andhra coast (Salankayana, Ananda Gotrika).
- late-pallava-empire (sa-02-d): matching gain from andhra-ikshvaku at c. 325 (Ikshvaku page: the Pallavas conquered the dynasty); the Pallava page has Simhavarman I already in Palnadu c. 275-300.
- rashtrakuta-dynasty (sa-03-d): vassal_start for western-ganga-dynasty from 819 (to 973), after the contest 780-819 recorded in western-ganga-dynasty.
- kamarupa-kingdom (sa-02-e): the 422 gain from davaka matches davaka's dissolve.
- alchon-huns (ia-01): the counterpart "Aulikara dynasty of Malwa (Prakashadharma)" is now the slug aulikara-dynasty (gain of Malwa c. 515, confidence 2, the page's footnote "fl. 515-516").
- anuradhapura (sa-02-a): its -161 gain from ruhuna matches ruhuna's merge and dissolve in -161; ruhuna uses six districts (Gālla, Mātara, Hambantŏṭa, Badulla, Mŏṇarāgala, Ampāra) against anuradhapura's four.

## nagas-of-padmavati (210-347)

Pages: Nagas of Padmavati, Samudragupta (2 of 2-5). Bharashiva_dynasty, Pawaya and Padmavati_(ancient_city) did not load (not found). The page gives three dates only (Bhima-naga c. 210-230, Bhava-naga c. 310-335 as an assumption, Ganapati "mid-4th century"). The Mathura and Ujjain extension is undated and recorded in 280 at confidence 1 (a bridge); the end 347 is the gupta-empire dossier's bridge. Nagas of Vindhyatabi (asked for by sa-02-c) are not treated by the page: no dossier. Capital coordinates approximate.

## abhira-dynasty (203-370)

Pages: Abhira dynasty, Ishwarsena, Satavahana dynasty, Traikutaka dynasty (4). The dates conflict: infobox 203 to "roughly 270 or 370", Ishwarsena's era 249 (the page also prints 284), the Satavahana page puts the capture of Nashik in Yajna's last years (before 199) while the Abhira page says they rose "after the demise of the Satavahanas". Start 203 follows the infobox and satavahana-dynasty's loss; end 370 is the page's "roughly till 370". Not drawn: Malwa ("may"), the Saurashtra branch (the page's "second half of the 10th century A.D." is a slip), the Vakataka seizure, the defeat by Mayurasarman, the Allahabad Pillar tribute (all undated).

## traikutaka-dynasty (388-550)

Pages: Traikutaka dynasty, Harishena, Abhira dynasty (3). The end differs by page: infobox c. 456, Harishena page c. 495, Traikutaka text "around AD 550" (Vikramasena dated 533); 550 used. Cliopatria draws the Konkan as Western Satraps (to 409), Gupta (410-450, 163 of 368 cells), Vakataka (from 451, 202 cells) and Maitraka (from 476, 72 cells), so the Traikutakas overlap Cliopatria shapes. The Vishnukundina vassalage is undated and not drawn. Successor slugs mauryas-of-puri needs a dossier.

## andhra-ikshvaku (227-325)

Pages: Andhra Ikshvaku, Ikshvaku dynasty (thin: the mythical dynasty), Satavahana dynasty, Pallava dynasty (4). Two chronologies on the page (Krishna Murthy, Singh) and the page mixes them for Rudrapurushadatta; end 325 is Singh's. The page's Abhira occupation of Vijayapuri ("30th regnal year of the Abhira king" Vasusena) is uncertain and not drawn. The Pallava page does not say how the Ikshvakus were displaced.

## chutu-dynasty (125-345)

Pages: Chutu dynasty, Satavahana dynasty (2). The page itself gives both c. 345 (Kadamba occupation of Banavasi) and "around 250-275" for the end; 345 is the one with a dated event. Konkan and Goa subordinates (Bhojas), Anantapur and southern Telangana coin finds are not drawn.

## aulikara-dynasty (350-545)

Pages: Aulikara dynasty, Yashodharman (2). Cliopatria and the Gupta dossier draw Malwa as Gupta (410+) and Vakataka (451+); the Aulikara page says the house "was never a Gupta feudatory". The 350 start is the infobox span (the date labels are garbled in the extract). Inscriptions of 404/405 and 436 (Bandhuvarman) are not on the page. The Kalachuri conquest of Malwa is undated. Yashodharman's claimed empire (Lauhitya to the Western Ocean) is a panegyric and not drawn.

## ruhuna (-205 to -161)

Pages: Ruhuna, Kavan Tissa of Ruhuna, Dutthagamani (3). The dossier ends in -161 because no page opened dates anything of Ruhuna after that; the later Ruhuna (the refuge of Mahinda V in 993, Vijayabahu I's rebellion, annexation by Parakramabahu I) needs its own pages (sa-03, Polonnaruwa). The Ruhuna page says "founded around 200 BC"; Kavan Tissa's reign is 205-161.

## western-ganga-dynasty (350-999)

Pages: Western Ganga dynasty, Rashtrakuta dynasty, Rajaraja I (3). Dates disagree (page: sovereignty "from about 350 to 550", infobox 1004, text "around the year 1000", Rajaraja page 998 and 1004); end 999 is the last listed ruler's last year (Rachamalla V, 986-999), loss 998 (Rajaraja page: confidence 3). The Rashtrakuta episode is drawn as a contest 780-819 because two pages date it; afterwards the Gangas are feudatories. Cliopatria draws Gangavadi as Pallava (350), Kadamba (400-550), Chalukya (600-700), Pallava (700-800), Rashtrakuta (780-950), Western Chalukya (990-1004). Years 550-780 are silent on the pages opened. The founder's name (Konganivarma Madhava; infobox Dadiga Madhava 350-370) is unexplained, so no ruler strip.

## vishnukundina-dynasty (420-624)

Pages: Vishnukundina dynasty, Pulakeshin II, Salankayana (3). The reign table has gaps (460-508) and the conquests of Madhava Varma II have no year (440 used, the start of his reign, confidence 1). The loss of Vengi "by about 616" is the Vishnukundina page's; the Pulakeshin II page does not date the conquest (Pishtapura "around or before" 617-618). Counterpart ananda-gotrika-dynasty and salankayana-dynasty now exist; eastern-chalukyas does not.

## salankayana-dynasty (300-440) and ananda-gotrika-dynasty (335-425)

Pages: Salankayana + Vishnukundina; Ananda Gotrika + Vishnukundina. Both thin. The Ananda Gotrika page names the Salankayanas as the conquerors, the Vishnukundina page names Madhava Varma II (c. 440-460); the land has no holder 425-440. Samudragupta's capture and release of Hastivarman of Vengi (Salankayana page) is undated and not drawn.

## nala-dynasty (440-580)

Pages: Nala dynasty, Narendrasena, Kirtivarman I (3). The Nala page gives only the "6th century"; the Narendrasena page has Bhavadattavarman invade Vidarbha around 445 (but dates Narendrasena c. 455-480). Both ends are confidence-1 bridges (440 before the war; 580 the middle of Kirtivarman I's 566-592). Successors panduvamshi-dynasty and sharabhapuriya-dynasty need dossiers.

## davaka (350-422)

Page: Davaka (1 of 2-5). Dates are bridges: the Allahabad Pillar (4th century) and the start of Kalyana Varman's reign (422). The page records a Davaka embassy to China in 428, after the end year.

## kuninda-kingdom (-150 to 250)

Page: Kuninda Kingdom (1). Thin: no capital, wars or overlord; both ends are bridges (2nd century BCE; 3rd century CE). Cliopatria draws the same foothills as Shunga, Indo-Greek, Kanva and Kushan land. May be a republic (Panini: Ayudhajivi Sangha).

## kalachuris-of-mahishmati (550-625)

Page: Kalachuris of Mahishmati (1). Successor to the Vakataka, Traikutaka (northern Konkan) and Aulikara lands; Ujjain around 597 (Shankaragana), Vidisha around 608 (Buddharaja), end "before 630" (Chalukya control of Nashik). The page's footnote dating the Maitraka loss of Ujjain to 616-617 contradicts 597. Counterpart later-gupta-dynasty is now a dossier.

## mathara-dynasty (350-499)

Page: Mathara dynasty (1). All dates are the page's "mid-4th century to the end of the 5th century". Cliopatria draws all of its land as Gupta from 347. Successors pitrbhakta-dynasty and vasishtha-dynasty have no dossier.

## later-gupta-dynasty (490-750)

Pages: Later Gupta dynasty, Mahasenagupta, Kalachuris of Mahishmati (3). A ruler strip is given from the page's list (Kumaragupta II, the first Devagupta and Madhavagupta overlap on it; the strip has the Magadha line from 606). Land: Magadha 490-574; Malwa 575-596 (Mahasenagupta's "rump state"); Malwa without Ujjain 597-604; Magadha restored from c. 606 under Harsha; Bihar, Jharkhand and West Bengal for Adityasena's extent (655, confidence 1). The Maukhari wars have only years (554, 560, 575). sa-03 should check against maukhari-dynasty, harsha-s-empire, gauda-kingdom, kannauj-varman-dynasty.

## States Cliopatria lacks that were not reached (or have no usable page)

Mitra dynasties of Kaushambi, Mathura, Kosala and Panchala (the Wikipedia page is a list: Kosambi c. 100 BCE-350 CE, Mathura c. 150-50 BCE), Maghas, Malavas, Arjunayanas, Audumbaras, Trigarta, Kota dynasty, Parivrajaka, Sharabhapuriya, Pitrbhakta, Vasishtha, Brihatphalayana, Samatata (page opened: 4th-13th centuries, mostly sa-03), Pushyabhuti (sa-03). Not states: the Mauryan provinces; the Vatsagulma Vakatakas (inside vakataka-kingdom). The Sri Lankan Chola occupations (Elara, 993-1070) belong to the anuradhapura and chola-empire dossiers.

## Gazetteer names needed

Lata and Ashmaka (regions), Kongu and Gangavadi (regions), Vengi (region), Bastar and Koraput (regions), Kopili valley (region), Garhwal (region); places Padmavati/Pawaya, Vidisha, Narwar, Kantipuri, Anjaneri, Thalner, Trikuta, Nagarjunakonda/Vijayapuri, Banavasi, Dashapura/Mandsaur, Magama/Tissamaharama, Talakad, Hassan, Erode, Manne, Channapatna, Pedavegi, Amarapura, Denduluru, Indrapalanagara, Kandarapura/Chejerla, Pushkari, Nandivardhana, Davaka, Mahishmati, Anandapura, Simhapura, Pishtapura; rivers Lauhitya (Brahmaputra), Mahaganga, Gomati. The dossiers use radii around gazetteer places or coordinates, so all regions resolve; these names appear only as text, capitals or coordinate radii.

## Repair after review (2026-10-19): western-ganga-dynasty, salankayana-dynasty, later-gupta-dynasty

Pages re-opened with WebFetch for the repair: Western Ganga dynasty (three times), Rashtrakuta dynasty, Chalukya dynasty, Kalabhra dynasty, Durvinita, Sripurusha, Talakad, Salankayana, Samudragupta, Later Gupta dynasty, Kalachuris of Mahishmati, Mahasenagupta, Harsha. Failed: https://en.wikipedia.org/wiki/Adityasena and https://en.wikipedia.org/wiki/Adityasena_Gupta (both url_not_found), so the 655 widening of the Later Guptas stays a confidence-1 bridge. All three dossiers validate with --resolve (western-ganga 0 warnings, salankayana 0, later-gupta 1: the old pushyabhuti-dynasty counterpart).

Convention: the schema says the counterpart of vassal_start/vassal_end is the vassal itself; the reviewer asked for the vassal's own ledger to name the suzerain (the mirror rule other batches followed). The new vassal events here are in that direction: the state is the vassal, the counterpart the suzerain. A renderer reading the schema literally must ignore them here and draw the tints from the suzerain's ledger. The occupation events are the owner's record with the occupier as counterpart.

### western-ganga-dynasty
Applied: (1) the 470 gain is split. Kongu inside Cliopatria's Kalabhra 353 shape (109 cells; with Mandya/Hassan 110 of the 205) names kalabhra-dynasty, confidence 1; the remaining 96 cells (nine Kongu cells, Mandya, Hassan) stay nobody, confidence 2. The union of the two equals the old region. Neither the Western Ganga page nor the Kalabhra page says who held Kongu (both silent); the counterpart rests on the geometry only. The Ganga page also says Kongu control began "starting from the 6th century rule of King Avinita", and the Durvinita page has a [citation needed] sentence about Kongudesa; the page's 470 is kept. (2) vassal_start chalukya-dynasty 550 (confidence 1) and vassal_end 753 (confidence 2): the Ganga page says "The Western Ganga sovereignty lasted from about 350 to 550 CE", "the Gangas accepted Chalukya overlordship" after the rise of the Badami Chalukyas (no year) and "The Chalukyas were replaced by the Rashtrakutas ... in 753"; the Chalukya page has the dynasty established in 543. The reviewer proposed "6th century"; 550 is the page's own span. (3) The 780-819 contest_start/contest_end became occupation_start (780, confidence 1: it is Dhruva's accession, the Sripurusha page has the Ganga king ruling to 788) and occupation_end (819, confidence 2), because the Rashtrakuta page says Dhruva "brought the Eastern Chalukyas and Gangas of Talakad under his control" and the Ganga page says only "partial control" returned by 819; the war stays in /wars/0 with a rewritten outcome. (4) vassal_start rashtrakuta-dynasty 819 (confidence 1: the peace and "staunch allies" are undated within Amoghavarsha I's reign) and vassal_end 982 (confidence 1). Disagreement: the first version and the earlier notes said the tie lasted to 973; no page opened gives 973 (the Rashtrakuta page lists Indra IV 973-982 and says the main line ended with his death, and gives no year for Tailapa II's independence), so 982 is used and flagged.
Thin gaps re-tried: Durvinita (r. 529-579; victories at Anderi, Alattur, Porulare and Pernagra undated; calls the Chalukya tie an alliance, not vassalage), Sripurusha (r. 726-788; 731 victory over Nandivarman II, place not given; capital moved to Manne, undated; victories against Krishna I undated) and Talakad (Harivarma 247-266 by the chronicle against the Ganga page's 390; no year for the capital; Cholas at "the beginning of the eleventh century"). None dates a change of land, so no event was added; the 390 Talakad gain stays a confidence-1 bridge.
Routing: kalabhra-dynasty (sa-02-e) needs a loss of the Kongu cells to western-ganga-dynasty in 470, or an objection that its Cliopatria shape was never over Kongu; chalukya-dynasty (sa-03) vassal events with counterpart western-ganga-dynasty 550-753; rashtrakuta-dynasty (sa-03-d) occupation 780-819 and vassal 819-982 with counterpart western-ganga-dynasty (this supersedes the entry in "What other dossiers need": the vassal_end is 982, not 973); chola-empire's 998 gain as before.

### salankayana-dynasty
Applied: the radius shape (Vijayawada 100 km + Rajahmundry 80 km, 160 cells) is replaced by the Godavari-Krishna doab north of the Krishna, a 12-point polygon of 49 cells (about 12,300 km2, a quarter of the old area; the polygon is the grammar's fallback, used because no named region fits). It follows the page's "Their territory was located between the Godavari and the Krishna rivers" and puts the capital Vengi (Pedavegi near Eluru) inside. Until 324 the 38 cells that andhra-ikshvaku draws are excluded (found 300 on the other 11 cells), and a 325 gain of those 38 cells names andhra-ikshvaku, confidence 1: the page calls the Salankayanas the Ikshvakus' "successors, whose rule possibly overlapped with them" and gives the Ikshvaku last inscription as c. 325, but not a conquest. andhra-ikshvaku is also now a predecessor. The capital is outside the drawn shape for 300-324 (stated in the capital note).
Disagreement: the reviewer's example fix was to subtract the Guntur 100 km disc. That disc is ananda-gotrika-dynasty /keyframe_review/0 (Guntur 100 km + Ongole 70 km) and it reaches Eluru (86 km from Guntur), so subtracting it would take Vengi out of the Salankayana shape, against the page. 28 cells of the doab are still in common with ananda-gotrika-dynasty_335 (335-425); the Ananda Gotrika shape should be restricted to the south of the Krishna (for example minus the polygon used here). That dossier (verdict thin) was not touched. Also open: andhra-ikshvaku /ledger/1 gives its whole 325 loss to late-pallava-empire and late-pallava-empire has no gain from it, so the 325 Salankayana gain has no mirror (andhra-ikshvaku passed and was not touched).
Thin gap: the Samudragupta page says Samudragupta "captured and released several kings of Dakshinapatha, including Hasti-varman of Vengi" and dates neither the campaign nor the release (reign c. 335-375); the Salankayana page says the king "may have become a tributary", so no vassal event was drawn.

### later-gupta-dynasty
Applied: (1) the 606-749 keyframe is split into 606-654 (Magadha) and 655-749 (the Bihar-Jharkhand-West Bengal union); the 655 gain is reduced to the land beyond Magadha (778 cells), and the dissolve and the successor land use the 655 shape. (2) The Mahishmati disc {lon 75.6, lat 22.2, km 100} is subtracted from the 575 and 597 keyframes, the 575 gain, the 605 loss and the 605 war zone; the 597 Ujjain loss loses the 43 cells of the Ujjain disc that lie in it. The Kalachuri page (re-read) has the capital "at Mahishmati in the Malwa region", Krishnaraja c. 550-575 and Shankaragana "conquered western Malwa, which was formerly under the Gupta authority" (undated). (3) Vassal events: gupta-empire 490 (confidence 2) to 525 (confidence 1), harsha-s-empire 606 (confidence 2) to 647 (confidence 1). Disagreement on the first end: the reviewer proposed c. 550; the Later Gupta page says Jivitagupta I, whose reign begins in 525, "was likely the first king of the Later Gupta dynasty to claim independent status", which is the only page statement about independence, so 525. The vassalage itself is "likely" on the page and the end of Harsha's overlordship is "after Harsha's death" (647 from the Harsha page). The Harsha page does not name the Later Guptas, Madhavagupta or Magadha; the vassal statements come from the Later Gupta and Mahasenagupta pages. (4) The 606 gain names maukhari-dynasty (confidence 1) as the 575 loss did; the Mahasenagupta page has Sharvavarman of Kannauj conquering "a part of the already crumbling empire of Magadha" and Kirttivarman I subduing Magadha (both undated) and names no ruler of Magadha after 575, so the holder at 606 is a reading; harsha-s-empire is the alternative if sa-03 finds Harsha held it. (5) Capitals: Ujjain ends 596; Vidisha is a flagged stand-in for 597-605 (the Mahasenagupta page: no seat named; Devagupta held "certainly East Malwa"). (6) pushyabhuti-dynasty is kept as the 605 counterpart; a note says Rajyavardhana was Harsha's elder brother, so sa-03 should decide whether it is harsha-s-empire's early years.
Routing: gupta-empire (sa-02-d) vassal_start 490 / vassal_end 525 with counterpart later-gupta-dynasty over Magadha; harsha-s-empire (sa-03) the matching 606-647 events; maukhari-dynasty (sa-03-a) a loss of Magadha in 606 if it held it; kalachuris-of-mahishmati: its 597 gain of the whole Ujjain 100 km disc overlaps its own Mahishmati disc by 43 cells (cosmetic).
