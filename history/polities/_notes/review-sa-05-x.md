# Review of batch sa-05-x (Mughals and Marathas, additions)

Reviewer: Phase B adversarial reviewer, 2026-10-25. Inputs: the author's report (history/notes/phase-b/reports/sa-05-x.json) and notes (history/polities/_notes/sa-05-x.md), the 25 dossiers, and the neighbour dossiers that exist (mughal-empire, maratha-empire, nawab-of-awadh, hyderabad-state, nepal, nawabs-of-bengal, kingdom-of-marwar, gorkha-kingdom, durrani-empire, portuguese-empire, ahmadnagar-sultanate, sikh-empire, tibet; the other Context polities are unwritten or have no event touching this batch).

Mechanical: `validate_dossier.py --resolve` gives 0 errors on all 25; warnings are the unwritten successor slugs the author listed (madhya-bharat, matsya-union, vindhya-pradesh, travancore-cochin, rampur-state, gohad-state, gond-kingdom-of-deogarh, venad) and garhwal-kingdom KF4, empty by design (Gorkha occupation 1804-1814, documented). Keyframe areas were recomputed with tools/gazetteer.py and compared with each page's infobox; all ratios are between 0.8 and 1.2 except Baroda (page figure 3,239 km2, flagged by the author as wrong). Overlaps between sibling shapes were computed cell by cell.

Spot checks: 4-7 events per dossier (all events for the two- and three-event dossiers), weighted to confidence 3 and to the events that move most land. No fabricated or mis-dated confidence-3 event was found; four notes quoted the page in words it does not use (fixed in place, see below).

Verdicts: gwalior-state fail, indore-state thin, baroda-state thin, kingdom-of-nagpur fix, rohilkhand-state fix, bharatpur-state thin, jaipur-state fix, kalhora-dynasty fail, travancore fix, kolhapur-state thin, janjira-state thin, kingdom-of-cochin thin, bikaner-state thin, garhwal-kingdom fix, alwar-state thin, bhopal-state thin, satara-state pass, cutch-state pass, jaisalmer-state thin, kumaon-kingdom thin, rewa-state thin, jhansi-state fix, kota-state fix, bundi-state pass, jhalawar-state fix.
Meaning here: fail = a shape that draws a written neighbour's land twice (back to the author); fix = reviewer-applied fixes (applied true) and/or non-blocking author fixes (applied false); thin = honest but the ledger does not explain the border moves, mostly by the 2-5 page budget; pass = nothing to change.

## gwalior-state: fail

Area: page 68291 km2 (1947) vs drawn about 70600 km2, ratio 1.03; acknowledged True.

Fixes:
- `/keyframe_review/2/correction, /keyframe_review/3/correction, /ledger/4/region, /ledger/9/region` (for the author): The Doab is drawn as the gazetteer's whole {"region": "Doab"} (135,554 km2, east to 81.82 E at Allahabad), which takes in the lower Doab (Kora, Allahabad, the Etawah-Kanpur side) that nawab-of-awadh holds from 1775 to its 1801 cession to the British; KF2/KF3 (1788-1802) and the 1803 loss therefore lie on Awadh's land with no event between the two dossiers. Evidence: gwalior KF3 resolves to 769 cells; 174 of them (about 44,000 km2) fall inside Cliopatria's 'Nawab of Awadh' 1790 shape and about 253 (64,000 km2) inside the nawab-of-awadh dossier's 1788-1800 keyframes; nawab-of-awadh /ledger/8 (1775 gain of 'the Doab districts of Kora, Allahabad and Fatehpur-Kanpur-Etawah side') and /ledger/10 (1801 loss to british-empire). The Second Anglo-Maratha War page says only that Scindia ceded the 'Ganges-Jamuna Doab' (his share). L4 is confidence 1. Fix: Restrict the Doab in KF2, KF3, L4 and L9 to Scindia's upper Doab, e.g. {"minus": [{"region": "Doab"}, {"cliopatria": "Nawab of Awadh", "year": 1790}], "text": "the upper Ganges-Jamuna Doab (Aligarh, Meerut, Saharanpur side)"}, and restate the KF2/KF3 areas in their notes.
- `/keyframe_review/3, /keyframe_review/7..9/correction` (for the author): The circles overlap three sibling dossiers of this batch with no event: KF3 (1790-1802) covers about 7,300 km2 of bharatpur-state (the Agra 70 km circle over the Bharatpur 60 km circle, while Bharatpur was independent and resisted the 1805 siege); KF7-KF9 cover about 7,300 km2 of indore-state's KF1 (Ujjain 55 km, Mandsaur and Shajapur circles over Indore 52 km and Mehidpur); KF9 covers about 4,300 km2 of bhopal-state (the Bhilsa circle). Evidence: Cell intersections computed with tools/gazetteer.py: gwalior KF3 x bharatpur KF2 = 29 cells; gwalior KF9 x indore KF1 = 29 cells; gwalior KF9 x bhopal KF0 = 17 cells. Fix: Subtract the neighbours in the Gwalior corrections and events, e.g. {"minus": [<Agra circle>, {"place": "Bharatpur", "km": 60}]}, and minus indore-state's Indore/Mehidpur circles and bhopal-state's polygon from the Malwa circles.

Thin (for a gap-filler):
- `/ledger/4`: Date of Scindia's acquisition of Delhi-Agra, the upper Doab and the Haryana towns (confidence 1, bridged to 1788). Try: https://en.wikipedia.org/wiki/Daulat_Rao_Scindia
- `/ledger/6`: The Rajput lands taken in 1790 (Ajmer) are confidence 1. Try: https://en.wikipedia.org/wiki/Battle_of_Merta
- `/ledger/15`: Isagarh, Bhilsa, Narwar and Sheopur zilas dated 1818 by reading (confidence 1). Try: https://en.wikipedia.org/wiki/Treaty_of_Gwalior
- `/ledger/18`: The 1844 Chanderi cession is undated on the page (confidence 1). Try: https://en.wikipedia.org/wiki/Gwalior_campaign

Spot checks: /ledger/1 (Gohad_State) confirmed: 'Maharani committed Jauhar on 27 February 1783 and the Marathas occupied the fort'; /ledger/5 (Mahadji_Shinde) confirmed: 'on 2 October 1788, Mahadji Scindia ... captured Delhi'; /ledger/9 (Second_Anglo-Maratha_War) confirmed: 30 December 1803, Hisar, Panipat, Rohtak, Rewari, Gurgaon, the Doab, Delhi-Agra, parts of Bundelkhand, Broach and Gujarat districts (Gwalior State page agrees); /ledger/11 (Gwalior_State) confirmed: 'In 1805 ... Gohad and Gwalior were restored', Chambal the northern boundary; /ledger/13 (Gwalior_State) confirmed: 'In 1811, Daulat Rao annexed the neighboring kingdom of Chanderi.'; /ledger/19 (Gwalior_State) confirmed: 1858 grants 'including the portion of Chanderi District west of the Betwa River'; /ledger/20 (Jhansi_State) confirmed: 'In 1861, the city and a dependent territory were ceded to Gwalior State'.

## indore-state: thin

Area: page 25646 km2 (1931) vs drawn about 26800 km2, ratio 1.04; acknowledged True.

Fixes:
- `/keyframe_review/1/from` (for the author): The shape grows from about 8,300 km2 (KF0) to about 27,000 km2 at 1767 with no gain in the ledger: the only 1767 event is the capital move to Maheshwar. Evidence: KF0 = 33 cells, KF1 = 106 cells; ledger /ledger/1 is capital_move. The KF1 note calls the shape a floor of the 1931 districts. Fix: Add a bridging gain at 1767 (confidence 1, the Khargone/Maheshwar, Mehidpur and Rampura-Bhanpura circles, counterpart maratha-empire or the Malwa chiefs) or start the floor at 1732 and say so in both keyframe notes.
- `/ledger/4, /ledger/7` (for the author): L4 (Tonk, Rampura, Bundi, 1805) and L7 (1818) remove land the keyframes never drew, so neither changes the map. Evidence: KF1 holds only the 1931 districts; the L7 note itself says it removes nothing. Fix: Say so in the KF1 note, or draw the pre-1818 Holkar holdings so the losses bite (see thin).

Thin (for a gap-filler):
- `/keyframe_review/1`: The Holkar dominion 1732-1818 (Malwa, Nimar, Tonk, Rampura) and the terms of the Treaty of Mandsaur. Try: https://en.wikipedia.org/wiki/Malhar_Rao_Holkar
- `/ledger/7`: 1818 loss is confidence 1 with no region. Try: https://en.wikipedia.org/wiki/Third_Anglo-Maratha_War

Spot checks: /ledger/0 (Indore_State) confirmed: 'On 29 July 1732, Bajirao Peshwa-I granted Holkar State by granting 28 and a half parganas'; /ledger/1 (Indore_State) confirmed: capital to Maheshwar in 1767; /ledger/4 (Second_Anglo-Maratha_War) confirmed: Treaty of Rajghat 24 December 1805, Tonk, Rampura and Bundi; /ledger/8 (Indore_State) confirmed: 'moved from Maheshwar to Indore on 3 November 1818'.

## baroda-state: thin

Area: page 3239 km2 (1911) vs drawn about 22000 km2, ratio 6.79; acknowledged True. body-text figure (no infobox area); the author flags it as implausible and sizes to the districts.

Fixes:
- `/keyframe_review/1/correction, /ledger/2` (for the author): KF1 draws Okhamandal from 1802 though L2 gains it in 1808, and the page's 1808 sentence is about bonds from the Okhamandal chiefs renouncing piracy, not an acquisition. Evidence: Baroda State page: British and Barodan forces 'approached Kathiawad in 1808, and eventually obtained bonds from the chiefs of Okha-mandal'. Fix: Drop Okhamandal from KF1 (draw it from L2's year) and say in the L2 note that the page has no acquisition date (keep confidence 1).

Thin (for a gap-filler):
- `/ledger/1`: Dates of the Kadi, Navsari and Amreli prants (bridged to 1802, confidence 1). Try: https://en.wikipedia.org/wiki/Gaekwad_dynasty
- `/ledger/2`: Okhamandal acquisition date (confidence 1). Try: https://en.wikipedia.org/wiki/Okhamandal

Spot checks: /ledger/0 (Baroda_State) confirmed: 'the Baroda State was founded in 1721, when ... Pilaji Gaekwad conquered Songadh from the Mughals'; /ledger/3 (Baroda_State) confirmed: 'in 1813, the Barodan government acquired the parganah of Kodinar'; /ledger/4 (Baroda_State) confirmed: 'Pethapur on 1 February 1940'; /ledger/5 (Baroda_State) confirmed: 'Finally on 1 May 1949'.

## kingdom-of-nagpur: fix

Area: page 217560 km2 (no year) vs drawn about 180000 km2, ratio 0.83; acknowledged True. infobox gives no year; KF3 (1785-1803) about 180,000 km2.

Fixes:
- `/keyframe_review/4/correction, /keyframe_review/5/correction, /ledger/12/region` (for the author): L8 removes 'southern Berar' (Akola 60 km and Amravati 50 km circles) in 1803 and KF4-KF5 hold no Berar, yet L12 removes the same two circles again in 1818, so the 1818 cession of 'the remaining portion of Berar' has no land in the keyframes. Evidence: Kingdom of Nagpur page: 'the remaining portion of Berar and the territories in the Narmada valley were ceded to the British' (1818); hyderabad-state /ledger/7 describes the 1803-04 cession as the territories 'south of Gawilgarh and Narnala and east of the Wardha'. Fix: Keep the Gawilgarh-Narnala (Melghat, Ellichpur) tract in KF4 and KF5 and make it L12's Berar part instead of the Akola/Amravati circles.
- `/ledger/8/source` (for the author): The cited Treaty of Deogaon page names only 'the province of Cuttack' (with Balasore); southern Berar is not on it. Evidence: Treaty of Deogaon page: Raghoji II 'gave up the province of Cuttack'; the Kingdom of Nagpur page mentions 'the 1803 cession of southern Berar'. Fix: Split L8 into Cuttack (Treaty_of_Deogaon, confidence 3) and southern Berar (Kingdom_of_Nagpur, confidence 2), or cite both in the note.

Spot checks: /ledger/3 (Maratha_invasions_of_Bengal) confirmed: war April 1742-March 1751, treaty May or June 1751 ceding Orissa, Subarnarekha boundary; /ledger/7 (Kingdom_of_Nagpur) confirmed: 'In 1785 Mandla and the upper Narmada valley were added ... by treaty with the Peshwa'; /ledger/9 (Kingdom_of_Nagpur) confirmed: 'Sambalpur was not relinquished until 1806'; /ledger/12 (Kingdom_of_Nagpur) confirmed (year and lands; see fix 1 for the region); /ledger/13 (Kingdom_of_Nagpur) confirmed: died without a male heir in 1853, annexed under the doctrine of lapse; /ledger/8 (Treaty_of_Deogaon) partly: 17 December 1803 and Cuttack confirmed; Berar not on this page.

## rohilkhand-state: fix

Area: page 0 km2 (no year) vs drawn about 26500 km2, ratio 0.0; acknowledged True. no area on the page; KF1 about 26,500 km2.

Fixes:
- `/ledger/5/region, /ledger/6, /ledger/8/region` (for the author): L5 (23 April 1774) removes the whole of Rohilkhand including Rampur; L6 (7 October) then splits Rampur off land the state no longer holds, and L8 dissolves the same whole region a second time, leaving the state empty from April to October. Evidence: Rohilla War page: defeat at Miranpur Katra on 23 April 1774, 'Rohilkhand fell to Awadh'; 'on 7 October 1774 Faizullah signed an amicable treaty of Lal Dang' creating Rampur State. nawab-of-awadh's mirror gain (/ledger/5) is dated October 1774. Fix: Either give L5 and L8 the region {"minus": [<Rohilkhand union>, <Rampur circle>]} so Rampur passes only by the split, or keep L5 as the contest and move the land loss to October (L8 only).

Thin (for a gap-filler):
- `/keyframe_review/0`: KF0 draws the full 90 km Rohilkhand (about 25,000 km2) from 1721 while L0's region is a 50 km circle at Aonla; the growth 1721-1748 is undated (the Rohilkhand infobox also has 'State established: 1690'). Try: https://en.wikipedia.org/wiki/Hafiz_Rahmat_Khan_Barech

Spot checks: /ledger/1 (Kumaon_Kingdom) confirmed: 'In 1742 Ali Mohammed Khan of Rohilkhand invaded Kumaon and annexed Kashipur, Rudrapur, and two other Kumaoni parganas.'; /ledger/3 (Rohilkhand) confirmed: 1773 'the Marathas were forced to retreat'; /ledger/5 (Rohilla_War) confirmed: 23 April 1774, Miranpur Katra; /ledger/6 (Rohilla_War) confirmed: 7 October 1774, treaty of Lal Dang, Rampur State.

## bharatpur-state: thin

Area: page 0 km2 (no year) vs drawn about 10600 km2, ratio 0.0; acknowledged True. no area on the page (author says so).

Thin (for a gap-filler):
- `/ledger/1`: Extent of Suraj Mal's conquests dated to 1761 by reading (confidence 1); the page lists the districts without a year. Try: https://en.wikipedia.org/wiki/Jawahar_Singh_(Bharatpur)
- `/ledger/3`: Loss of the Jat districts after 1774 undated (confidence 1). Try: https://en.wikipedia.org/wiki/Mirza_Najaf_Khan
- `/keyframe_review/2`: The 60 km circle is about 10,600-11,300 km2; no page figure was found (the princely state was about half that); a gap-filler should find an area and resize. Try: https://en.wikipedia.org/wiki/Matsya_Union

Spot checks: /ledger/0 (Bharatpur_State) confirmed: infobox 'Established: 18 November 1722'; /ledger/2 (Suraj_Mal) confirmed: 'Suraj Mal captured Agra Fort on 12 June 1761'; /ledger/4 (Bharatpur_State) confirmed: 'On 18 February 1774, the Mughal Commander Mirza Najaf Khan re-captured Agra'; /ledger/8 (Bharatpur_State) confirmed: 'On 18 January 1826 its fortress was stormed and captured'.

## jaipur-state: fix

Area: page 0 km2 (no year) vs drawn about 23800 km2, ratio 0.0; acknowledged True. no area on the page (author says so).

Fixes:
- `/ledger/3/region, /ledger/4/region` (for the author): L3 (to alwar-state) and L4 (to bharatpur-state) remove the identical region (the 90 km circle intersected with the 'eastern Dhundhar' 45 km circle), so the same cells are lost twice to two owners; L4 (confidence 1) has no mirror gain in bharatpur-state, written in the same batch. Evidence: Both regions are {"intersect": [{"place": "Jaipur", "km": 90}, {"lon": 76.75, "lat": 27.3, "km": 45}]}; bharatpur-state's ledger has no 1774-1776 gain from jaipur-state. Fix: Split the band (the north-east part to alwar-state, the east part to bharatpur-state) and add the matching confidence-1 gain to bharatpur-state, or drop L4 and say in L3's note that the Jat share is unplaced.
- `/keyframe_review/2/correction` (for the author): KF2 overlaps alwar-state's shape by about 1,260 km2 (1775-1948). Evidence: jaipur KF2 x alwar KF0 = 5 cells. Fix: Subtract alwar-state's region from KF2.

Thin (for a gap-filler):
- `/keyframe_review/0`: KF0 draws the 60 km Dhundhar circle from 1028 while L0's region is a 30 km circle at Dausa; Amber's capture and the Mughal-era growth (Shekhawati, Bundi, Rampura) are undated. Try: https://en.wikipedia.org/wiki/Kingdom_of_Amber
- `/ledger/4`: The Jat annexation from Jaipur is confidence 1. Try: https://en.wikipedia.org/wiki/Jawahar_Singh_(Bharatpur)

Spot checks: /ledger/0 (Jaipur_State) confirmed: 'they migrated to Rajputana in 1028 AD', Dausa; /ledger/1 (Jaipur_State) confirmed: 'by October 1708, Amber had also been taken over and Jai Singh restored'; Sambhar captured and jointly ruled; /ledger/4 (Jaipur_State) partly: the page has 'the Jats of Bharatpur and the Kachwaha chief of Alwar declared themselves independent from Jaipur'; the note's quoted words 'each annexed part of Jaipur's eastern territory' were not returned; /ledger/7 (Jaipur_State) confirmed: accession signed 7 April 1949.

## kalhora-dynasty: fail

Area: page 0 km2 (no year) vs drawn about 179000 km2, ratio 0.0; acknowledged True. no area on the page; Sind admin1 about 141,000 km2 plus about 38,000 km2 of Kutch.

Fixes:
- `/keyframe_review/1/correction, /ledger/1/region, /ledger/3/region, /ledger/4/region` (for the author): 'The northern half of Kutch district' is drawn as {"region": "Kutch"} cut by the box 23.4-25 N, 68-72 E, which takes the northern Kutch mainland (Banni, Khavda) that cutch-state holds throughout 1549-1948: the two dossiers overlap by about 9,100 km2 (43 percent of Cutch) for 1736-1783 with no gain, loss or occupation in either. Evidence: kalhora KF1 x cutch-state KF1 = 36 cells. Kalhora dynasty page: 'The northern half of Kutch district was also under the Kalhora Dynasty' (undated); Cutch State page: Kalhora attacks 'once in 1763-64' and 'in 1765', the battle near Jara, no cession. Fix: Limit the Kutch part to land outside cutch-state's polygon (the Great Rann), e.g. {"minus": [<current Kutch part>, <cutch-state KF1 correction>]}, or drop it and say why; if a page shows Kalhora rule on the mainland, add the loss/gain pair to both dossiers.

Thin (for a gap-filler):
- `/ledger/1`: The spread over all of Sindh is dated to 1736 by reading (confidence 1). Try: https://en.wikipedia.org/wiki/Noor_Muhammad_Kalhoro
- `/wars`: Nader Shah's invasion ('The Kalhora dynasty succumbed to the invasion of Nader Shah', undated) is not in wars or ledger. Try: https://en.wikipedia.org/wiki/Nader_Shah%27s_invasion_of_the_Mughal_Empire

Spot checks: /ledger/0 (Kalhora_dynasty) confirmed: Established 1701, 'made subahdar of upper Sindh by royal decree'; /ledger/1 (Kalhora_dynasty) confirmed as quoted (independence 1736); extent undated, confidence 1 is right; /ledger/2 (Kalhora_dynasty) confirmed: Khudabad 1701-1768, then Hyderabad (infobox has Khudabad from 1710); /ledger/4 (Kalhora_dynasty) confirmed: 'Abdul Nabi Kalhoro was the last Kalhora ruler, being overthrown in 1783'.

## travancore: fix

Area: page 19844 km2 (1941) vs drawn about 18970 km2, ratio 0.96; acknowledged True.

Fixes:
- `/ledger/1/region, /ledger/3/region, /ledger/4/region, /ledger/5/region` (for the author): Each gain's region is the whole cumulative band (Kerala south of 9.05, 9.3, 9.8 or 10.2 N plus Kanyakumari), which already holds Venad and the earlier gains, while its text names only the chiefdom annexed. Evidence: L1 region = Kerala south of 9.05 N + Kanyakumari with text 'Kollam (Quilon) and Kottarakkara'; same pattern in L3-L5. Fix: Make each region the delta: {"minus": [<this band>, <previous band>]} with the same text.

Spot checks: /ledger/1 (Marthanda_Varma) confirmed: 'In 1731, the port of Kollam(Quilon)'; /ledger/2 (Marthanda_Varma) confirmed: 1741, Kottarakkara annexed after the Dutch defeat; /ledger/3 (Marthanda_Varma) confirmed: by 1746 'Travancore now extended from Kanyakumari to Kayamkulam'; /ledger/5 (Marthanda_Varma) confirmed: 'Ambalapuzha, Kottayam and Changanassery were also annexed to Travancore by 1753'; /ledger/6 (Marthanda_Varma) confirmed: Karappuram and Alangad ceded in 1753; Mavelikkara 15 August 1753; /ledger/8 (Travancore) confirmed: 'On 1 July 1949 the kingdom of Travancore was merged with the kingdom of Cochin'.

## kolhapur-state: thin

Area: page 8332 km2 (1901) vs drawn about 8350 km2, ratio 1.0; acknowledged True.

Thin (for a gap-filler):
- `/ledger`: No territorial event 1710-1949 (the page names no cession; the 1812 treaty and 1844 aftermath are undated). Try: https://en.wikipedia.org/wiki/Shivaji_II
- `/ledger/0`: Founding 1710 against maratha-empire's split of 1707 (/ledger/11); the page has both 'came into being in 1707' and 'By 1710 ... an established fact'. Try: https://en.wikipedia.org/wiki/Tarabai

Spot checks: /ledger/0 (Kolhapur_State) confirmed: 'By 1710, two separate principalities had become an established fact' (also 1707); /ledger/1 (Kolhapur_State) confirmed: 'merged into Bombay State on 1 March 1949'.

## janjira-state: thin

Area: page 839 km2 (1931) vs drawn about 1000 km2, ratio 1.19; acknowledged True.

Thin (for a gap-filler):
- `/ledger/5`: Gain of Murud and Shrivardhan from maratha-empire in 1745 is a confidence-1 reading with no mirror in maratha-empire. Try: https://en.wikipedia.org/wiki/Siddi

Spot checks: /ledger/0 (Janjira_State) confirmed: infobox 'Established: 1489'; /ledger/1 (Janjira_State) confirmed: Bajirao's campaign against the Siddis of Janjira in 1733; /ledger/3 (Murud-Janjira) confirmed: 'Peace was brokered in September 1736, but the Siddis were confined to only Janjira, Gowalkot, and Anjanvel'; /ledger/4 (Murud-Janjira) confirmed: 'captured by Tulaji Angre in 1745'.

## kingdom-of-cochin: thin

Area: page 0 km2 (no year) vs drawn about 4300 km2, ratio 0.0; acknowledged True. no area on the page.

Fixes:
- `/keyframe_review/0/correction` (for the author): The capital Cochin (Kochi) of 1405-1949 lies outside KF0 (1100-1502), which holds only the Perumpadappu and Mahodayapuram circles. Evidence: identity.capitals: Cochin from 1405 at 76.27 E 9.96 N; KF0 = 25 km circles at 75.95/10.77 and 76.2/10.22. Kingdom of Cochin page: 'In 1405, Perumpadapu Swaroopam changed their capital from Mahodayapuram to Cochin' (also 1341). Fix: Split KF0 at 1405 and add Kochi to the later part (or start KF1 in 1405).

Thin (for a gap-filler):
- `/keyframe_review/1`: The 1503 step (Kochi, Thrissur, Chittur appear) has no ledger event; the Zamorin's oath of vassalage and the Mysore conquest (infobox 1766-1799) are not in the ledger. Try: https://en.wikipedia.org/wiki/Zamorin_of_Calicut
- `/ledger/0`: Founding at 1100 is confidence 1 (page: 'originated in the early part of the 12th century'). Try: https://en.wikipedia.org/wiki/Perumpadappu_Swaroopam

Spot checks: /ledger/0 (Kingdom_of_Cochin) confirmed as a rounding: 'Established: 12th century CE' (confidence 1 right); /ledger/1 (Marthanda_Varma) confirmed: Karappuram and Alangad ceded to Travancore in 1753; /ledger/2 (Kingdom_of_Cochin) confirmed: 'Disestablished: 1 July 1949'.

## bikaner-state: thin

Area: page 61355 km2 (no year) vs drawn about 58700 km2, ratio 0.96; acknowledged True.

Thin (for a gap-filler):
- `/ledger`: The 1542 annexation of the whole kingdom by Maldeo of Marwar and its recovery are missing; kingdom-of-marwar /ledger/9 has the 1542 gain from Bikaner (Maldeo Rathore page: 'Rao Maldeo took advantage of this situation to annex the entire kingdom of Bikaner'). Try: https://en.wikipedia.org/wiki/Maldeo_Rathore
- `/ledger`: Bhatner (1805) and other changes; the Bikaner page has none. Try: https://en.wikipedia.org/wiki/Rao_Kalyan_Mal
- `/ledger/1`: The state is dissolved at the accession of 7 August 1947 although it lasted until the Rajasthan merger (not on the page). Try: https://en.wikipedia.org/wiki/Rajasthan#Integration

Spot checks: /ledger/0 (Bikaner_State) confirmed: 'The state of Bikaner was founded in 1465.'; /ledger/1 (Bikaner_State) confirmed: 'The accession to the Indian Union was signed by the Maharaja on 7 August 1947.'.

## garhwal-kingdom: fix

Area: page 10826 km2 (1901) vs drawn about 12000 km2, ratio 1.11; acknowledged True. body text 4,180 sq mi.

Fixes:
- `/ledger/2/note` (applied by the reviewer): The quoted words 'Rohilla invasion, 1757: Najib-ud-daula captured Dehradun.' are not on the page. Evidence: Garhwal Kingdom page: Najib-ud-daula 'invaded in 1757 along with his Rohilla Army and captured Dehradun' (marked citation needed). Fix: Note rewritten with the page's words (applied by the reviewer; validator 0 errors).
- `/ledger/3/note` (applied by the reviewer): The quoted words 'Garhwali forces retook the Dun region in 1770.' are not on the page. Evidence: Garhwal Kingdom page: in 1770 the Garhwali forces defeated the Rohillas and 'retrieved possession of the Dun region'. Fix: Note rewritten with the page's words (applied by the reviewer; validator 0 errors).

Spot checks: /ledger/0 (Garhwal_Kingdom) confirmed: 'founded in 823 AD'; /ledger/1 (Garhwal_Kingdom) confirmed: 'In 1358, the 37th ruler, Ajay Pal, brought all the minor principalities'; /ledger/2 (Garhwal_Kingdom) confirmed (wording fixed); /ledger/3 (Garhwal_Kingdom) confirmed (wording fixed); /ledger/4 (Pradyumna_Shah) confirmed: 'reigned over Garhwal from 1785 to 14 May 1804', Battle of Khurbura; /ledger/6 (Garhwal_Kingdom) confirmed: 'acceded to the Union of India in August 1949 CE' (citation needed).

## alwar-state: thin

Area: page 8332 km2 (no year) vs drawn about 8600 km2, ratio 1.03; acknowledged True. text '3,217 square miles', no year.

Thin (for a gap-filler):
- `/ledger`: No territorial event 1775-1948 (lands granted after the 1803 alliance; Rajgarh and Swarup Singh's estates undated); no capital table beyond Alwar. Try: https://en.wikipedia.org/wiki/Bakhtawar_Singh

Spot checks: /ledger/0 (Alwar_State) confirmed: 'He established the State of Alwar in 1775.'; /ledger/1 (Alwar_State) confirmed: 'merged on 18 March 1948 with three other princely states'.

## bhopal-state: thin

Area: page 17876 km2 (1901) vs drawn about 17200 km2, ratio 0.96; acknowledged True.

Thin (for a gap-filler):
- `/keyframe_review/0`: One 1707-1949 keyframe is the 1901 extent (17,876 km2) while L0 is a 30 km circle; 'He also annexed several other territories in Malwa' is undated. Try: https://en.wikipedia.org/wiki/Dost_Mohammad_Khan
- `/wars/1`: The Nizam's March 1724 invasion 'forcing Khan to cede much of his territory' has no loss (counterpart hyderabad-state). Try: https://en.wikipedia.org/wiki/Asaf_Jah_I

Spot checks: /ledger/0 (Bhopal_State) confirmed: 'The state was founded in 1707'; /ledger/1 (Bhopal_State) confirmed: 'In 1709, he took on the lease of the Berasia estate.'; /ledger/2 (Bhopal_State) confirmed: Islamnagar 1728-1742; /ledger/4 (Bhopal_State) confirmed: 'taken over by the Union Government of India on 1 June 1949'.

## satara-state: pass

Area: page 7924 km2 (1848) vs drawn about 8850 km2, ratio 1.12; acknowledged True.

Spot checks: /ledger/0 (Satara_State) confirmed: created after the fall of the Maratha Confederacy in 1818, Pratap Singh installed by the British; /ledger/1 (Satara_State) confirmed: the page has both 1849 (introduction, infobox) and 1848 (body); confidence 2 and the note say so.

## cutch-state: pass

Area: page 19725 km2 (1901) vs drawn about 21000 km2, ratio 1.06; acknowledged True.

Spot checks: /ledger/0 (Cutch_State) confirmed: 'founded around 1147 by Lakho Jadani'; /ledger/2 (Cutch_State) confirmed: 'integrated Cutch into one large dominion in 1549'; /ledger/3 (Cutch_State) confirmed: Anjar 'came under British occupation on 25 December 1815'; /ledger/4 (Cutch_State) confirmed: 'till 25 December 1822, when it was territory reverted to Cutch'; /ledger/5 (Cutch_State) confirmed: infobox 'Merged into India as Kutch State: 1 June 1948' (4 May 1948 in the text, noted).

## jaisalmer-state: thin

Area: page 41600 km2 (1931) vs drawn about 41200 km2, ratio 0.99; acknowledged True.

Thin (for a gap-filler):
- `/ledger`: The page says the Mughals 'controlled the fort until 1762' (the capital) with no start; no occupation pair is in the ledger. Try: https://en.wikipedia.org/wiki/Jaisalmer_Fort
- `/keyframe_review/0`: Pokhran, taken by Marwar in 1650 (kingdom-of-marwar /ledger/19), stays inside the 115 km circle; no loss in this ledger. Try: https://en.wikipedia.org/wiki/Marwar_Kingdom

Spot checks: /ledger/0 (Jaisalmer_State) confirmed: Rawal Jaisal moved the capital to Jaisalmer in 1156; /ledger/1 (Jaisalmer_State) confirmed at confidence 2: infobox 1156-1947, 1949 merger, 'Greater Rajasthan in 1950'.

## kumaon-kingdom: thin

Area: page 0 km2 (no year) vs drawn about 28000 km2, ratio 0.0; acknowledged True. no area on the page.

Thin (for a gap-filler):
- `/ledger/0`: Founding about 700 is confidence 1. Try: https://en.wikipedia.org/wiki/Katyuri_dynasty
- `/ledger/3, /ledger/5`: Terai gains of 1638 and 1673 are confidence-1 readings (the Baz Bahadur Chand page has only the October 1665 capture and the October 1673 pardon). Try: https://en.wikipedia.org/wiki/Chand_dynasty
- `/keyframe_review/1..5`: Doti is drawn 1450-1791 from 'unified the region, including Doti, in the 15th century', but nepal /ledger/13 annexes Doti from a separate Doti in 1790; when Doti left Kumaon is not on the pages. Try: https://en.wikipedia.org/wiki/Doti_Kingdom

Spot checks: /ledger/1 (Kumaon_Kingdom) confirmed: 'unified the region, including Doti, in the 15th century'; /ledger/4 (Baz_Bahadur_Chand) confirmed: 'captured Terai and the emperor's rule was established there (October. 1665)'; /ledger/5 (Baz_Bahadur_Chand) confirmed as described: only the October 1673 pardon (bridging, confidence 1); /ledger/6 (Kumaon_Kingdom) confirmed: 1742, Kashipur, Rudrapur and two other parganas; /ledger/7 (Kumaon_Kingdom) confirmed: 'in 1791 the Kingdom of Nepal invaded Kumaon'.

## rewa-state: thin

Area: page 33670 km2 (1901) vs drawn about 33900 km2, ratio 1.01; acknowledged True.

Thin (for a gap-filler):
- `/ledger/2, /ledger/3`: Sohagpur and Amarkantak: 'seized by the Marathas in the beginning of the century' and restored after 1857, both confidence 1; the page does not name the Maratha power (probably Nagpur, which would make kingdom-of-nagpur the counterpart). Try: https://en.wikipedia.org/wiki/Shahdol_district
- `/keyframe_review/0`: KF0 is the 1901 outline from 1140 while L0 is a 40 km circle at Bandhavgarh. Try: https://en.wikipedia.org/wiki/Bandhavgarh_Fort

Spot checks: /ledger/0 (Rewa_State) confirmed: Bandhavgarh, Vyaghra Dev, 1140 CE; /ledger/1 (Rewa_State) confirmed: 'In 1617, Maharaja Vikramaditya Singh Baghel moved his capital to Rewa'; /ledger/2 (Rewa_State) confirmed as described (undated on the page, confidence 1); /ledger/3 (Rewa_State) confirmed as described (restored after the 1857 uprisings).

## jhansi-state: fix

Area: page 4059 km2 (1804) vs drawn about 4300 km2, ratio 1.06; acknowledged True.

Fixes:
- `/ledger/1` (for the author): A contest_start in 1853 with no fighting: four years of British administration are drawn as a war zone, and the contest does not match the war 'Siege of Jhansi' (1857-1858). Evidence: Jhansi State page: 1853, 'the British authorities took over the state under the terms of the Doctrine of Lapse'; 'In March 1854, Lakshmibai was given a pension ... and ordered to leave the palace and the fort'; 'From August 1857 to January 1858 Jhansi under the Rani's rule was at peace'; Siege of Jhansi: 24 March-5 April 1858. Fix: Replace L1 with occupation_start (counterpart british-empire) in 1853 or 1854-3 and occupation_end in 1857, then contest_start 1858-3 (24 March) before the existing contest_end and dissolve; or end the state in 1853 and say so.

Spot checks: /ledger/0 (Jhansi_State) confirmed: 'Founded: 1728'; /ledger/1 (Jhansi_State) year confirmed, event type not supported (see fix); /ledger/2 (Siege_of_Jhansi) confirmed: 'on 5 April the defenders abandoned the fort'; /ledger/3 (Siege_of_Jhansi) confirmed: siege 24 March-5 April 1858.

## kota-state: fix

Area: page 14828 km2 (1931) vs drawn about 14900 km2, ratio 1.0; acknowledged True.

Fixes:
- `/ledger/2/note` (applied by the reviewer): The quoted sentence ('The British decided in 1897 to break up the state. Most of it went back to Kota, and Shahabad and Chaumahla became a new state in 1899, with an area of 810 sq mi') is not the page's wording. Evidence: Jhalawar State page: 'the British resolved in 1897 to break up the state, restoring the greater part to Kota, but forming the two districts of Shahabad and the Chaumahla into a new state of area 810 square miles (2,100 km2), which came into existence in 1899'. Fix: Quote replaced with the page's sentence (applied by the reviewer; validator 0 errors).
- `/keyframe_review/2/correction, /ledger/2/region` (for the author): The page names the 1899 Jhalawar as 'the two districts of Shahabad and the Chaumahla', yet KF2 subtracts a 26 km circle around Jhalawar town, so Kota keeps Shahabad and the Chaumahla after 1899; the note says 'the parganas are not named', which the quoted sentence contradicts. Evidence: Jhalawar State page as quoted; Shahabad lies in the north-east of the old Jhalawar tract, the Chaumahla in the south (Gangdhar). Fix: Build the 1899 cut from the two named districts (coordinates with text until the gazetteer has them), together with the capital if a page places it there, in KF2 and L2; the same in jhalawar-state.

Spot checks: /ledger/0 (Kota_State) confirmed: 'In 1631, Rao Raja Ratan Singh of Bundi partitioned the province of Kota'; /ledger/1 (Jhalawar_State) confirmed: 'it was resolved in the year 1838 ... to dismember the state'; /ledger/2 (Jhalawar_State) confirmed: 1897 decision, new state 1899; /ledger/3 (Kota_State) confirmed: 'On 18 April 1948, the Maharao merged his state'.

## bundi-state: pass

Area: page 5750 km2 (no year) vs drawn about 6070 km2, ratio 1.06; acknowledged True.

Spot checks: /ledger/0 (Bundi_State) confirmed: 'Rao Deva, who took over Bundi in 1241'; /ledger/1 (Kota_State) confirmed: 1631 partition of Kota from Bundi; /ledger/2 (Bundi_State) confirmed: accession signed 7 April 1949.

## jhalawar-state: fix

Area: page 2106 km2 (1901) vs drawn about 2000 km2, ratio 0.95; acknowledged True.

Fixes:
- `/ledger/1/note` (applied by the reviewer): The quoted sentence is not the page's wording (same as kota-state /ledger/2). Evidence: Jhalawar State page: 'the British resolved in 1897 to break up the state, restoring the greater part to Kota, but forming the two districts of Shahabad and the Chaumahla into a new state of area 810 square miles (2,100 km2), which came into existence in 1899'. Fix: Quote replaced with the page's sentence (applied by the reviewer; validator 0 errors).
- `/keyframe_review/1/correction, /ledger/1/region, /ledger/2/region` (for the author): KF1 (1899-1949) is a 26 km circle at Jhalawar town, while the page forms the new state from 'the two districts of Shahabad and the Chaumahla'; the note's 'the parganas are not named' is wrong. Evidence: Jhalawar State page as quoted (810 sq mi; infobox 2,106 km2 in 1901). Fix: Draw the 1899 state from Shahabad and the Chaumahla (plus the capital if a page places it there), sized to 2,106 km2, in KF1, L1 and L2.

Spot checks: /ledger/0 (Jhalawar_State) confirmed: 1838; rulers table from 8 April 1838; /ledger/1 (Jhalawar_State) confirmed: 1897 decision, new state 1899; /ledger/2 (Jhalawar_State) confirmed at confidence 2: infobox 'Indian independence: 1949'.

## Cross-dossier matrix

- rohilkhand-state 1742 gain <- kumaon-kingdom: mirror kumaon-kingdom 1742 loss: **matched**. same batch; same two circles
- rohilkhand-state 1774 loss <- nawab-of-awadh: mirror nawab-of-awadh 1774 gain: **matched**. April here, October in Awadh; see rohilkhand fix on the April-October order
- rohilkhand-state 1774 dissolve <- nawab-of-awadh: mirror nawab-of-awadh 1774 gain: **matched**. dissolve repeats the April loss
- rohilkhand-state 1721 found <- mughal-empire: mirror mughal-empire 1720 loss: **matched**. Mughal counterpart string 'Rohilla Afghans (Rohilkhand)'
- rohilkhand-state 1774 split <- rampur-state: mirror none: **exception**. rampur-state listed by the author under counterparts_needing_dossiers
- garhwal-kingdom 1804 loss <- nepal: mirror nepal 1804 gain: **matched**. 
- kumaon-kingdom 1791 dissolve <- nepal: mirror nepal 1791 gain: **matched**. 
- kumaon-kingdom 1790 keyframe (Doti held 1450-1791) <- nepal: mirror nepal 1790 gain: **mismatch**. nepal /ledger/13 takes Doti from a separate 'Doti' in 1790 while kumaon-kingdom draws Doti until 1791; one of the two needs a page on when Doti left Kumaon
- kumaon-kingdom 1665 loss <- mughal-empire: mirror mughal-empire: **missing**. no 1665 Terai gain in mughal-empire (sa-05 sibling)
- kumaon-kingdom 1638 gain <- mughal-empire: mirror mughal-empire: **missing**. confidence 1 reading; no Mughal event
- kumaon-kingdom 1673 gain <- mughal-empire: mirror mughal-empire: **missing**. confidence 1 reading; no Mughal event
- travancore 1753 gain <- kingdom-of-cochin: mirror kingdom-of-cochin 1753 loss: **matched**. same batch
- alwar-state 1775 found <- jaipur-state: mirror jaipur-state 1775 loss: **matched**. same batch
- kota-state 1631 found <- bundi-state: mirror bundi-state 1631 loss: **matched**. same batch
- kota-state 1838 loss <- jhalawar-state: mirror jhalawar-state 1838 found: **matched**. same batch
- kota-state 1899 gain <- jhalawar-state: mirror jhalawar-state 1899 loss: **matched**. same batch; both regions need the Shahabad/Chaumahla fix
- janjira-state 1736 loss <- maratha-empire: mirror maratha-empire 1736 gain: **matched**. 
- janjira-state 1745 gain <- maratha-empire: mirror maratha-empire: **missing**. confidence 1; maratha-empire has no 1745 loss
- janjira-state 1745 loss <- Tulaji Angre (Maratha navy): mirror maratha-empire: **missing**. the Angre navy is the Maratha Empire's; maratha-empire has no 1745 gain of Gowalkot and Anjanvel
- bharatpur-state 1761 gain <- mughal-empire: mirror mughal-empire 1761 loss: **matched**. Mughal counterpart string 'Jats' (Agra)
- bharatpur-state 1774 loss <- mughal-empire: mirror mughal-empire 1774 gain: **matched**. Mughal counterpart string 'Jats' (confidence 1)
- jaipur-state 1775 loss <- bharatpur-state: mirror bharatpur-state: **missing**. same batch: bharatpur-state has no gain from jaipur-state
- jaipur-state 1708 gain <- mughal-empire: mirror mughal-empire 1707 loss: **mismatch**. mughal-empire's 1707/1710 losses name kingdom-of-marwar (Marwar region), none names jaipur-state or Sambhar
- kingdom-of-nagpur 1751 gain <- nawabs-of-bengal: mirror nawabs-of-bengal 1752 loss: **mismatch**. nawabs-of-bengal /ledger/5 gives Orissa to maratha-empire (which also gains it, /ledger/28); confederacy-member overlap the author flagged
- kingdom-of-nagpur 1803 loss <- british-empire: mirror hyderabad-state 1804 gain: **exception**. british-empire not written (sa-06); hyderabad-state /ledger/7 gains Berar 'south of Gawilgarh and Narnala' from british-empire in 1804, consistent; see nagpur fix 1 on the 1818 remainder
- kingdom-of-nagpur 1785 gain <- maratha-empire: mirror maratha-empire: **missing**. maratha-empire has no 1785 loss of Mandla (page: 'by treaty with the Peshwa')
- kingdom-of-nagpur 1739 found <- gond-kingdom-of-deogarh: mirror none: **exception**. listed under counterparts_needing_dossiers
- gwalior-state 1788 gain <- mughal-empire: mirror nawab-of-awadh 1775 gain: **mismatch**. the Doab gained here (confidence 1) includes Awadh's lower Doab held 1775-1801 (nawab-of-awadh /ledger/8, /ledger/10): about 44,000-64,000 km2 drawn twice; mughal-empire has no 1788 loss either
- gwalior-state 1790 keyframe overlap <- bharatpur-state: mirror bharatpur-state: **mismatch**. gwalior KF3 covers about 7,300 km2 of bharatpur-state 1790-1802 with no event
- gwalior-state 1858 keyframe overlap <- indore-state: mirror indore-state: **mismatch**. gwalior KF7-KF9 and indore KF1 share about 7,300 km2 (circles)
- gwalior-state 1858 keyframe overlap <- bhopal-state: mirror bhopal-state: **mismatch**. gwalior KF9 and bhopal KF0 share about 4,300 km2 (Bhilsa circle)
- gwalior-state 1818 gain <- maratha-empire: mirror maratha-empire 1817 loss: **mismatch**. confidence 1; maratha-empire's 1817-1818 losses all go to british-empire
- gwalior-state 1783 gain <- gohad-state: mirror maratha-empire 1783 gain: **exception**. gohad-state listed under counterparts_needing_dossiers; maratha-empire /ledger/39 also gains Gwalior from Gohad in 1783 (confederacy overlap)
- gwalior-state 1784 vassal_start <- mughal-empire: mirror none: **exception**. suzerain-side record (the vassal is the counterpart); nothing required in mughal-empire
- gwalior-state 1803 loss <- british-empire: mirror none: **exception**. british-empire (sa-06) not written; same for gwalior 1805, 1818, 1844, 1858, indore 1805, 1818, nagpur 1806, 1818, 1853, garhwal 1815, cutch 1815/1822 occupation, rewa 1858, satara 1848, jhansi 1858
- gwalior-state 1861 gain <- british-raj: mirror none: **exception**. british-raj not written (group not run); also 1885 exchange
- kolhapur-state 1710 found <- maratha-empire: mirror maratha-empire 1707 split: **mismatch**. three years apart; the Kolhapur page has both 1707 and 'By 1710'
- satara-state 1818 found <- maratha-empire: mirror maratha-empire 1818 loss: **mismatch**. maratha-empire's 1818 land goes to british-empire; Satara was carved out by the British; acceptable if british-empire later records the grant
- jhansi-state 1728 found <- maratha-empire: mirror maratha-empire: **missing**. no Jhansi event in maratha-empire (inside its shape)
- rewa-state 1800 loss <- maratha-empire: mirror maratha-empire: **missing**. confidence 1; the seizer was probably Nagpur (kingdom-of-nagpur has no Sohagpur gain either)
- baroda-state 1802 gain <- maratha-empire: mirror maratha-empire: **missing**. confidence 1 bridging
- bhopal-state 1709 gain <- mughal-empire: mirror mughal-empire: **missing**. small (Berasia lease)
- kalhora-dynasty 1736 gain <- mughal-empire: mirror mughal-empire: **missing**. mughal-empire's Sindh loss is 1752 to durrani-empire
- kalhora-dynasty 1736 keyframe overlap <- cutch-state: mirror cutch-state: **mismatch**. about 9,100 km2 of the Kutch mainland drawn in both 1736-1783; see kalhora fix
- kalhora-dynasty 1783 loss <- talpur-dynasty: mirror none: **exception**. talpur-dynasty is a sa-05 sibling's Cliopatria row (1820-1894) not yet written; its dossier must start in 1783
- kalhora-dynasty 1749 (vassal of durrani-empire) <- durrani-empire: mirror durrani-empire 1749 vassal_start: **matched**. suzerain record exists (1749-1783); author's note says 1748-1750
- bikaner-state 1542 (missing loss) <- kingdom-of-marwar: mirror kingdom-of-marwar 1542 gain: **missing**. marwar /ledger/9 annexes Bikaner in 1542 (counterpart string 'bikaner'); bikaner-state has no event; marwar's 1564 loss to the Mughals still includes Bikaner
- jaisalmer-state 1650 (missing loss) <- kingdom-of-marwar: mirror kingdom-of-marwar 1650 gain: **missing**. marwar /ledger/19 takes Pokhran from 'jaisalmer'; Jaisalmer's circle still holds it
- gwalior-state 1731 found <- mughal-empire: mirror mughal-empire 1738 loss: **mismatch**. Malwa goes from mughal-empire to maratha-empire in 1738; the Maratha members (gwalior 1731, indore 1732, baroda 1721, bhopal 1707, bharatpur 1722, kalhora 1701) found on Mughal land with no Mughal loss; the confederacy/tint question is the orchestrator's
- garhwal-kingdom 1757 loss <- Najib-ud-daula (Rohilla): mirror none: **exception**. free-text counterpart; Najib-ud-daula's Saharanpur/Najibabad holding has no dossier

## Gazetteer names needed (in addition to the author's list)

Upper Doab (region, gwalior-state), Gawilgarh (place, kingdom-of-nagpur), Narnala (place, kingdom-of-nagpur), Ellichpur (place, kingdom-of-nagpur), Shahabad (Baran, Rajasthan) (place, jhalawar-state), Chaumahla (region, jhalawar-state), Great Rann of Kutch (region, kalhora-dynasty), Jhalrapatan (place, jhalawar-state).

## Counterparts needing dossiers (in addition to the author's list)

Doti Kingdom (doti-kingdom, 1400-1790), Chanderi State (chanderi-state, 1500-1811).

## Problems

- No page failed to load for the reviewer.
- hyderabad-state /ledger/7 changed counterpart (maratha-empire to british-empire) between two reads during this review: another agent is editing it.
- Reviewer edits applied in place and re-validated (0 errors): garhwal-kingdom /ledger/2 and /ledger/3 notes, kota-state /ledger/2 note, jhalawar-state /ledger/1 note (quotes replaced with the page's words). The files were re-serialised with json indent 1 (the authors' format).
- Verdict 'fix' here covers both reviewer-applied fixes (applied true) and non-blocking author fixes (applied false); 'fail' (gwalior-state, kalhora-dynasty) marks wrong shape corrections that draw a written neighbour's land twice.
- Structural, already flagged by the author: the Maratha confederacy members lie inside maratha-empire's shape until 1818 and found on Mughal land with no Mughal loss; the orchestrator must decide sub-units versus tints.
- The new-state page budget (2-5 pages) explains most thin verdicts: alwar, kolhapur, satara, bikaner, jaisalmer, bundi and jhalawar have only found and dissolve plus the page's own changes.
