# Review of batch af-01-c (Majeerteen, Hobyo, Mahdist State, Ethiopia, TPLF)

Reviewed 2026-10-18 by the adversarial reviewer. Validator with --resolve: 0 errors in all five dossiers; warnings only for unresolved gazetteer names (Suakin, Abu Hamed, Haud, Badme) and the not-yet-existing slug anglo-egyptian-sudan. Neighbour dossiers read: ethiopian-empire (af-01-b) only; every other Context polity is unwritten. Overlaps were measured with tools/grid.py polity_cells (H3 res 5, about 250 km2 a cell).

Verdicts: majeerteen-sultanate **thin**, sultanate-of-hobyo **fail**, mahdist-state **fail**, ethiopia **fail**, tigray-people-s-liberation-front **fail**.

## majeerteen-sultanate: thin
Area: infobox 124320 km2, Cliopatria 91653 km2, ratio 0.74 (infobox gives no year; ratio against the 1856 shape, acknowledged in keyframe_review/0).

Thin (gaps for a gap-filler):
- `/ledger/0`: Founding at confidence 1: the infobox says 'Established 15th-16th century' and the dossier starts at Cliopatria's 1856; no pre-1856 extent or founding year. Thin by design (2 pages of a 1-2 page budget). Try: https://en.wikipedia.org/wiki/Osman_Mahamuud
- `/keyframe_review/3`: Borders of the protectorate years 1890-1927 are the 1885 shape at confidence 1; the new keyframe also overlaps Cliopatria's British Africa shape from 1890 by 15 H3 res-5 cells (about 3,800 km2) on the western edge (British Somaliland), an overlap that did not exist while Cliopatria's Majeerteen row ran (0 cells in 1885). Try: https://en.wikipedia.org/wiki/Italian_Somaliland

Spot checks:
- `/ledger/1` confirmed: 'establish the separate Sultanate of Hobyo in 1878' (https://en.wikipedia.org/wiki/Majeerteen_Sultanate)
- `/ledger/2` confirmed: 'On April 7, 1889, it became a protectorate of Italy after a treaty' (https://en.wikipedia.org/wiki/Majeerteen_Sultanate)
- `/ledger/3` confirmed: landings at Haafuun and Alula, then 'on 7 October the Governor instructed Coronaro to order the Sultan to surrender' and the seizure of merchant boats near Alula; the month is read from the 7 October order (https://en.wikipedia.org/wiki/Campaign_of_the_Sultanates)
- `/ledger/5` confirmed: 'Italians were not able to entirely capture Majeerteenia until late 1927'; 'eventually directly annexed to the Italian colony of Somalia' (https://en.wikipedia.org/wiki/Campaign_of_the_Sultanates)

## sultanate-of-hobyo: fail
Area: infobox None km2, Cliopatria 134617 km2, ratio None (no infobox area on the Hobyo page (verified)).

Findings:
- `/keyframe_review/3/correction` (blocking): The new 1895..1925 keyframe keeps the whole 1890 shape, of which 91 H3 res-5 cells (about 20,000 km2, the part in eastern Ethiopia) lie inside the ethiopian-empire dossier's 1900 and 1908 shapes, so from 1900 to 1925 two dossiers draw the same land; the author noted the 22,000 km2 in Ethiopia but did not resolve it against ethiopian-empire. Evidence: Grid overlap (tools/grid.py polity_cells): sultanate-of-hobyo 1890 x ethiopian-empire 1898 = 0 cells, x 1900 = 91, x 1908 = 91; ethiopian-empire /ledger/39 gains the Ogaden in 1891 from 'nobody' and its keyframe 1900 note says the shape reaches 47.9 E (the Ogaden). Cliopatria avoids the overlap only because its Hobyo row ends in 1894. Fix: Either add a keyframe sultanate-of-hobyo_1900 (1900..1925) with correction {minus:[{cliopatria:'Sultanate of Hobyo',year:1890},{cliopatria:'Ethiopian Empire',year:1900}]} and a 1900 loss with counterpart ethiopian-empire (confidence 1, bridged from the Ethiopian Empire shape), or keep the land and route a matching loss to af-01-b's ethiopian-empire; say which in the note.
- `/ledger/3/note` (non-blocking): The note says the 1890 shape loses 30,000 km2; shapes.csv gives 134,617.4 - 107,741.4 = 26,876 km2. Evidence: shapes.csv rows sultanate-of-hobyo_1880 and _1890. Fix: Write 'about 27,000 km2' in /ledger/3 and /keyframe_review/2 notes.

Thin (gaps for a gap-filler):
- `/ledger/3`: The 1890 loss of about 27,000 km2 in the south-west to italian-africa is at confidence 1 (no page names the land or year); thin by design within the 1-2 page budget (3 pages used). Try: https://en.wikipedia.org/wiki/Italian_Somaliland
- `/keyframe_review/3`: Borders of the protectorate years 1895-1925 are the 1890 shape at confidence 1. Try: https://en.wikipedia.org/wiki/Italian_Somaliland
- `/identity/predecessors/1`: hiraab-imamate is a predecessor with no row and no page; years unknown. Try: https://en.wikipedia.org/wiki/Hiraab_Imamate

Spot checks:
- `/ledger/0` confirmed: Majeerteen page: 'establish the separate Sultanate of Hobyo in 1878'; Hobyo page: 'established between the 1870s and 1884 by Yusuf Ali Kenadid' (https://en.wikipedia.org/wiki/Majeerteen_Sultanate)
- `/ledger/2` confirmed: infobox 'Protectorate treaty with the Kingdom of Italy: 8 February 1889' (https://en.wikipedia.org/wiki/Sultanate_of_Hobyo)
- `/ledger/4` confirmed: 'on 1 October three columns of dubats' entered the sultanate, 'deposing the ruler' (1925) (https://en.wikipedia.org/wiki/Campaign_of_the_Sultanates)
- `/ledger/5` confirmed: the page says 'integrated into the colony of Italian Somaliland in 1927'; the October 1925 end is the deposition, acknowledged in the note (https://en.wikipedia.org/wiki/Sultanate_of_Hobyo)

## mahdist-state: fail
Area: infobox None km2, Cliopatria 2327420 km2, ratio None (no infobox area on the Mahdist State page (verified)).

Findings:
- `/keyframe_review/3` (blocking): The 1890 keyframe is 'ok' and draws Wadi Halfa and Suakin as Mahdist, which the dossier's own 1885 keyframe removes as Anglo-Egyptian; no ledger event gains them between 1885 and 1890, and K4, K5 and K6 keep them too. Evidence: Mahdist State page: 'only Sawakin, reinforced by Indian army troops, and Wadi Halfa on the northern frontier remained in Anglo-Egyptian hands'; nothing on either page says the Ansar took them later. Rule 4: an area increase between keyframes needs an event. Fix: Set keyframe_review/3 verdict 'adjust' with correction {minus:[{cliopatria:'Mahdist State',year:1890},{union:[{place:'Wadi Halfa',km:50},{place:'Suakin',km:50}]}]}, and add the same two places to the minus of the 1895, 1898 and 1899 corrections.
- `/ledger/6/region` (blocking): The 1883 keyframe (Kordofan plus Darfur, about 0.67 M km2) grows to the 1885 keyframe (about 2.30 M km2), but the 1885 gains are 80 km circles around Khartoum, Kassala and Sennar plus the South Sudan part: about 1 M km2 of the northern and eastern Sudan (Berber, Dongola, the Red Sea hills, the Gezira, the Blue Nile) is gained by no event. Evidence: Areas: Sultanate of Darfur 1873 shape 293,978 km2; mahdist-state_1890 2,327,420 km2; the page gives the extent in one sentence ('only Sawakin ... and Wadi Halfa ... remained in Anglo-Egyptian hands'). Fix: Give the fall-of-Khartoum gain (or a new 1885 gain, counterpart khedivate-of-egypt, confidence 2, source the Mahdist State page) the region {minus:[<the 1885 keyframe correction>,{union:[{region:'Kordofan'},{cliopatria:'Sultanate of Darfur',year:1873}]}]} so the ledger carries what the keyframe adds.
- `/notes` (non-blocking): The new 1885..1889 keyframe lies almost wholly under Cliopatria's British Africa 1885-1889 shape (8,627 of 8,635 H3 cells), and the notes flag only the Khedivate overlap of 1881-1884. Evidence: Grid overlap british-africa 1885 x mahdist-state 1890 shape = 8,627 cells; british-africa_1885 lists Sudan first in modern_countries; from 1890 the overlap is 0. Fix: Add to the notes and problems that the British Africa dossier (af-08) must trim the Sudan from its 1885 shape.

Thin (gaps for a gap-filler):
- `/ledger/5`: The 1885 southern gain is at confidence 1 ('by the end of 1885, the Ansar had begun to move into the southern region'); the Bahr al-Ghazal fell in 1884, Equatoria held out under Emin Pasha to 1888-1889. Try: https://en.wikipedia.org/wiki/Equatoria
- `/ledger/4`: Capital move to Omdurman at confidence 1, year bridged from Khartoum. Try: https://en.wikipedia.org/wiki/Omdurman
- `/ledger/10`: The 1895 southern loss to belgian-congo (about 25,000 km2) at confidence 1; the Mahdist War infobox has 'Congo secures the Lado Enclave until 1910' with no year. Try: https://en.wikipedia.org/wiki/Lado_Enclave
- `/keyframe_review/6`: The Khalifa's 1899 remnant is drawn as the 1898 shape less 100 km around Omdurman (over 2 M km2); no page gives its extent. Try: https://en.wikipedia.org/wiki/Battle_of_Umm_Diwaykarat
- `/ledger/1`: El Obeid's fall: the page gives 'early in 1882' and a four-month siege but no year of the surrender (it is usually dated January 1883); the 1882 gain is the author's reading. Try: https://en.wikipedia.org/wiki/Muhammad_Ahmad
- `/keyframe_review/1`: 1884 is drawn as Kordofan and Darfur only; the fall of Berber and the Bahr al-Ghazal and Osman Digna's east (1883-1884) are on no page opened. Try: https://en.wikipedia.org/wiki/Siege_of_Khartoum

Spot checks:
- `/ledger/6` confirmed: infobox 'Fall of Khartoum 26 January 1885' (https://en.wikipedia.org/wiki/Mahdist_State)
- `/ledger/9` confirmed: the Mahdists 'had lost [Kassala] to the Italians in 1894' (https://en.wikipedia.org/wiki/Mahdist_War)
- `/ledger/13` confirmed: Abu Hamed captured 'on 7 August 1897' (https://en.wikipedia.org/wiki/Mahdist_War)
- `/ledger/14` confirmed: the Anglo-Egyptians 'reached Omdurman, the Mahdist capital, on 2 September' 1898 (https://en.wikipedia.org/wiki/Mahdist_War)
- `/ledger/17` confirmed: infobox ends 25 November 1899; Mahdist State infobox: Battle of Umm Diwaykarat 24 November 1899 (https://en.wikipedia.org/wiki/Mahdist_War)
- `/ledger/7` confirmed: 'In January 1886, a Mahdist army invaded Ethiopia, seized Dembea' (https://en.wikipedia.org/wiki/Mahdist_War)

## ethiopia: fail
Area: infobox 1104300 km2, Cliopatria 1127752 km2, ratio 1.02 (infobox has no year; compared with the 2014-2024 shape; also 1.13 M for 1942-1952).

Findings:
- `/ledger` (blocking): Missing: the Tigray Defense Forces' occupation of Amhara and Afar land from July to December 2021 (outside the Tigray contest zone, so it is drawn nowhere). Evidence: Tigray War page: 17-19 July the TDF attacked Afar; 'the city of Weldiya was captured by the TDF on 12 August 2021'; Lalibela seized 5 August; 30 October 'Dessie had fallen to the TDF'; 31 October Kombolcha; 6 December government forces recaptured Dessie and Kombolcha; 20 December 2021 the TPLF 'had withdrawn its troops from Amhara and Afar back into Tigray'. Fix: Add occupation_start 2021-7 and occupation_end 2021-12 with counterpart tigray-people-s-liberation-front, region {union:[{place:'Lalibela',km:50},{place:'Dessie',km:50},{place:'Weldiya',km:50},{place:'Kombolcha',km:30}]} (North Wollo and South Wollo, Amhara Region; Weldiya and Kombolcha need gazetteer entries) plus the Afar edge, confidence 2, source the Tigray War page; mirror in the TPLF dossier.
- `/wars/0` (blocking): The Eritrean War of Independence has zone country=Eritrea but the ledger has no contest_start/contest_end for it, so the 30-year contest is not drawn. Evidence: Federation of Ethiopia and Eritrea page: Hamid Idris Awate 'began armed resistance on 1 September 1961, marking the start of the Eritrean War of Independence'; Eritrean-Ethiopian War page: 'From 1961 until 1991, Eritrea fought a 30-year war of independence against Ethiopia'. Fix: Add contest_start 1961-9 and contest_end 1991 (counterpart 'Eritrean independence fighters', the war's belligerent string, region country=Eritrea, confidence 2-3), sources the two pages already in sources[].
- `/ledger/19/confidence` (applied by reviewer): Confidence 3 with a region (Tigray less the Eritrean band) that includes Western Tigray, which the page says Amhara held. Evidence: Tigray War infobox: 'Western Tigray ceded and occupied by neighboring Amhara regional authorities'; text: 'Amhara Region forces took over and occupied Western Tigray' (November 2020). Fix: Lowered to 2 by the reviewer (note appended); re-validated 0 errors.
- `/ledger/19/region` (non-blocking): The region still includes Western Tigray, which stayed under Amhara (Ethiopian) control. Evidence: Same infobox sentence. Fix: Once the gazetteer has 'Western Tigray', subtract it from /ledger/19, /ledger/21 and the TPLF dossier's regions.
- `/ledger/21/region` (non-blocking): The 2023-3 gain is admin1 Tigray, while the mirror TPLF /ledger/4 loss is Tigray less the Eritrean band: the two sides disagree on the land. Evidence: tigray-people-s-liberation-front /ledger/4 region. Fix: Use the TPLF /ledger/4 region in /ledger/21.
- `/ledger/1` (non-blocking): 1941 is drawn as a sovereign Ethiopia with only the Ogaden and the Haud occupied, but the page says the 1942 agreement ended British military occupation of most of Ethiopia. Evidence: Ogaden War page: on 31 January 1942 the second Anglo-Ethiopian Agreement, 'ending British military occupation in most of Ethiopia except Ogaden'; Cliopatria's British Africa 1941 shape also covers all of Ethiopia. Fix: Either extend the 1941 occupation by british-africa to the whole 1942 shape, ending 1942-1 for all but the Ogaden and Haud, or explain in keyframe_review/0 why the restoration of 1941 is drawn as sovereign.
- `/ledger` (non-blocking): Missing: the October 2022 federal-Eritrean offensive inside Tigray ('On 17 October 2022, the strategic city of Shire was taken by Eritrea and Ethiopia'). Evidence: Tigray War page. Fix: Add a gain 2022-10 from tigray-people-s-liberation-front around Shire (place needs a gazetteer entry), confidence 2; mirror as a TPLF loss.

Thin (gaps for a gap-filler):
- `/ledger/22`: Eritrea's occupation of northern Tigray is closed at 2024 at confidence 1; the page says only 'largely continued to occupy parts of Tigray as of 2023'. Try: https://en.wikipedia.org/wiki/Eritrea%E2%80%93Ethiopia_relations
- `/ledger/1`: Start of the Ogaden/Haud administration at confidence 1. Try: https://en.wikipedia.org/wiki/Ogaden
- `/ledger/2`: The page gives 1948 for both the Haud and the Ogaden; the Haud and the Reserved Area are usually dated to the 1954 Anglo-Ethiopian agreement (not on the pages opened). Try: https://en.wikipedia.org/wiki/Haud
- `/wars/2`: Ethiopia's occupation of 'about a quarter of Eritrea's territory' by the end of May 2000 is not located or ended on the page. Try: https://en.wikipedia.org/wiki/Temporary_Security_Zone
- `/wars/0`: EPLF- and TPLF-held land in the Ethiopian Civil War (Eritrea from the late 1970s, Tigray from 1989) is not in the ledger (budget 5 of 5 pages used). Try: https://en.wikipedia.org/wiki/Ethiopian_Civil_War
- `/wars`: The 1964 Ethiopian-Somali Border War is not listed. Try: https://en.wikipedia.org/wiki/1964_Ethiopian%E2%80%93Somali_Border_War
- `/identity/rulers`: Rulers omitted. Try: https://en.wikipedia.org/wiki/List_of_heads_of_state_of_Ethiopia

Spot checks:
- `/ledger/2` confirmed: the British 'gave the Haud and the Ogaden regions to Ethiopia' in 1948; 'Ethiopian administration resumed in Jijiga for the first time in 13 years' (https://en.wikipedia.org/wiki/Ogaden_War)
- `/ledger/3` confirmed: 'Eritrea formally became a constituent state of the federation of Ethiopia and Eritrea on 15 September 1952' (https://en.wikipedia.org/wiki/Federation_of_Ethiopia_and_Eritrea)
- `/ledger/7` confirmed: infobox '13 July 1977 - 23 March 1978' (also /ledger/8) (https://en.wikipedia.org/wiki/Ogaden_War)
- `/ledger/14` confirmed: 'on 22 February 1999, Ethiopia launched a massive military offensive to recapture Badme' (https://en.wikipedia.org/wiki/Eritrean%E2%80%93Ethiopian_War)
- `/ledger/19` confirmed: 'on 28 June 2021, the Tigray Defense Forces (TDF) retook Mekelle'; ICG 'the TDF now controlled most of the Tigray region'; region overstated (Western Tigray), confidence lowered to 2 (https://en.wikipedia.org/wiki/Tigray_war)

## tigray-people-s-liberation-front: fail
Area: infobox None km2, Cliopatria None km2, ratio None (rebel state without a Cliopatria row or infobox area).

Findings:
- `/ledger` (blocking): Missing: the TDF occupation of Amhara and Afar land, July-December 2021 (mirror of the Ethiopia finding). Evidence: Tigray War page: Weldiya 'captured by the TDF on 12 August 2021', Lalibela 5 August, Dessie 30 October, Kombolcha 31 October; on 20 December 2021 the TPLF 'had withdrawn its troops from Amhara and Afar back into Tigray'. Fix: Add occupation_start 2021-7 and occupation_end 2021-12 with counterpart ethiopia and the same region as the Ethiopia dossier, confidence 2.
- `/ledger/2/confidence` (applied by reviewer): Confidence 3 with a region that includes Western Tigray, which Amhara held from November 2020. Evidence: Tigray War infobox: 'Western Tigray ceded and occupied by neighboring Amhara regional authorities'. Fix: Lowered to 2 by the reviewer (note appended); re-validated 0 errors.
- `/ledger` (non-blocking): Missing: the October 2022 loss of Shire ('On 17 October 2022, the strategic city of Shire was taken by Eritrea and Ethiopia'). Evidence: Tigray War page. Fix: Add a loss 2022-10 to ethiopia around Shire, confidence 2.
- `/keyframe_review/1/correction` (non-blocking): The TDF area includes Western Tigray (Amhara-held). Evidence: Tigray War infobox, as above. Fix: Subtract 'Western Tigray' from keyframe 1 and /ledger/2, /ledger/4, /ledger/5 once the gazetteer has it.
- `/identity/wikipedia` (non-blocking): wikipedia is null although the party has an English Wikipedia article (not opened by the author; not verified by the reviewer). Evidence: Author's notes: no TPLF article opened. Fix: Open https://en.wikipedia.org/wiki/Tigray_People%27s_Liberation_Front and fill wikipedia (and wikidata from it).

Thin (gaps for a gap-filler):
- `/ledger/4`: Who held Tigray between the 2 November 2022 cessation of hostilities and the 23 March 2023 interim administration is not on the page. Try: https://en.wikipedia.org/wiki/Pretoria_Agreement

Spot checks:
- `/ledger/0` confirmed: infobox '3 November 2020 - 3 November 2022' (https://en.wikipedia.org/wiki/Tigray_war)
- `/ledger/1` confirmed: 'Federal allied forces captured Mekelle, the capital of the Tigray Region, on 28 November' (https://en.wikipedia.org/wiki/Tigray_war)
- `/ledger/2` confirmed: 'on 28 June 2021, the Tigray Defense Forces (TDF) retook Mekelle'; region overstated, confidence lowered to 2 (https://en.wikipedia.org/wiki/Tigray_war)
- `/ledger/3` confirmed: 'On 2 November 2022, Ethiopia and the TPLF announced that they had signed an agreement for a cessation of hostilities', effective 3 November (https://en.wikipedia.org/wiki/Tigray_war)
- `/ledger/4` confirmed: infobox 'Interim Regional Administration of Tigray formed on 23 March 2023' (https://en.wikipedia.org/wiki/Tigray_war)

## Cross-dossier matrix
- majeerteen-sultanate 1878 loss / sultanate-of-hobyo -> sultanate-of-hobyo 1878 gain: **matched**. same region (760 km2 strip)
- majeerteen-sultanate 1927 loss / italian-africa -> italian-africa None None: **exception**. counterpart dossier not written yet (af-08 has not run); italian-africa also needs vassal_start 1889-4 / vassal_end 1927 for the protectorate
- majeerteen-sultanate 1925 contest_start / italian-africa -> italian-africa None None: **exception**. counterpart dossier not written yet (af-08)
- sultanate-of-hobyo 1890 loss / italian-africa -> italian-africa None None: **exception**. counterpart dossier not written yet (af-08); confidence 1
- sultanate-of-hobyo 1925 loss / italian-africa -> italian-africa None None: **exception**. counterpart dossier not written yet (af-08); italian-africa also needs vassal_start 1889-2 / vassal_end 1925-10
- sultanate-of-hobyo 1900 overlap / ethiopian-empire -> ethiopian-empire 1891 gain: **mismatch**. Hobyo's new 1895..1925 keyframe and ethiopian-empire's 1900/1908 shapes share 91 H3 cells (~20,000 km2, Ogaden); ethiopian-empire /ledger/39 gains the Ogaden from 'nobody' in 1891; one side must give it up (af-01-c or af-01-b)
- mahdist-state 1882 gain / khedivate-of-egypt -> khedivate-of-egypt None None: **exception**. counterpart dossier not written yet (me-10 owns khedivate-of-egypt); also the 1883 and 1885 gains (Darfur, Kassala, Sennar, the south, Khartoum)
- mahdist-state 1886 contest_start / ethiopian-empire -> ethiopian-empire None None: **missing**. ethiopian-empire (af-01-b) has no contest_start/contest_end with mahdist-state for 1886-1889, only a war 'Ethiopian-Mahdist War' 1889-1889; Mahdist War page: Dembea January 1886, Gondar January 1888
- mahdist-state 1894 loss / italian-africa -> italian-africa None None: **exception**. counterpart dossier not written yet (af-08): Italian Africa needs a 1894 gain of Kassala and its 1897 handover
- mahdist-state 1895 loss / belgian-congo -> belgian-congo None None: **exception**. counterpart dossier not written yet (af-08); confidence 1
- mahdist-state 1896 loss / british-africa -> british-africa None None: **exception**. counterpart dossier not written yet (af-08); also 1897-8 Abu Hamed, 1898-9 Omdurman and the 1896-1898 contest
- mahdist-state 1885 overlap / british-africa -> british-africa 1885 None: **mismatch**. british-africa_1885 (1885-1889) covers 8,627 of the 8,635 cells of the Mahdist 1885 keyframe; af-08 must trim the Sudan out of British Africa 1885
- mahdist-state 1899 loss / anglo-egyptian-sudan -> anglo-egyptian-sudan None None: **exception**. listed in counterparts_needing_dossiers (af-08)
- ethiopia 1941 occupation_start / british-africa -> british-africa None None: **exception**. counterpart dossier not written yet (af-08); also the 1948 end; British Africa 1941 shape covers all of Ethiopia (author flagged)
- ethiopia 1952 gain / british-africa -> british-africa None None: **exception**. counterpart dossier not written yet (af-08): Eritrea, BMA to federation
- ethiopia 1977 contest_start / federal-republic-of-somalia -> federal-republic-of-somalia None None: **exception**. counterpart dossier not written yet (af-08)
- ethiopia 1991 loss / state-of-eritrea -> state-of-eritrea None None: **exception**. counterpart dossier not written yet (af-08); Cliopatria's Eritrea starts 1992, so af-08 must start it in 1991 or the EPLF rebel dossier (counterparts_needing_dossiers) must carry 1991
- ethiopia 1999 occupation_start / state-of-eritrea -> state-of-eritrea None None: **exception**. counterpart dossier not written yet (af-08); Badme 1999-2020
- ethiopia 2020 occupation_start / state-of-eritrea -> state-of-eritrea None None: **exception**. counterpart dossier not written yet (af-08); northern Tigray 2020-2024
- ethiopia 2020 contest_start / tigray-people-s-liberation-front -> tigray-people-s-liberation-front 2020 contest_start: **matched**. 2020-11 both; contest_end 2022-11 both
- ethiopia 2021 loss / tigray-people-s-liberation-front -> tigray-people-s-liberation-front 2021 gain: **matched**. 2021-6 both, same region
- ethiopia 2023 gain / tigray-people-s-liberation-front -> tigray-people-s-liberation-front 2023 loss: **mismatch**. 2023-3 both, but Ethiopia gains all of admin1 Tigray while TPLF loses Tigray less the Eritrean band
- tigray-people-s-liberation-front 2021 occupation_start / ethiopia -> ethiopia None None: **missing**. the July-December 2021 TDF occupation of Amhara and Afar is in neither dossier

## Problems
- Only one Context neighbour dossier exists (ethiopian-empire, af-01-b); the other 18 Context polities and khedivate-of-egypt (me-10) are not written yet, so their mirrors are exceptions.
- Cliopatria british-africa_1885 (1885-1889) covers the whole Mahdist 1885-1889 keyframe (8,627 of 8,635 H3 cells); route to af-08.
- The new Hobyo 1895..1925 keyframe overlaps ethiopian-empire's 1900 and 1908 shapes by 91 cells; the new Majeerteen 1890..1927 keyframe overlaps british-africa from 1890 by 15 cells.
- The schema has no vassal-side event: both Somali dossiers mark the Italian protectorate with 'rename' events (1889); italian-africa (af-08) must carry vassal_start/vassal_end for both.
- https://en.wikipedia.org/wiki/Siege_of_El_Obeid is the 2023 siege, not the 1882-1883 one; the El Obeid date was left as thin.
- Reviewer edits applied: ethiopia /ledger/19 and tigray-people-s-liberation-front /ledger/2 confidence 3 to 2 (both re-validated 0 errors, read back). Both dossiers still fail on unapplied findings.

Gazetteer names needed: Suakin (place, mahdist-state), Abu Hamed (place, mahdist-state), Haud (region, ethiopia), Badme (place, ethiopia), Western Tigray (region, ethiopia), Weldiya (place, ethiopia), Kombolcha (place, ethiopia), Shire (place, tigray-people-s-liberation-front).
