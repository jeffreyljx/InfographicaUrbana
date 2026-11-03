# Review of batch oc-01 (Polynesian and Melanesian states), Phase B

Reviewer run of 2026-10-18. Inputs: the 16 dossiers, the author's report (history/notes/phase-b/reports/oc-01.json) and notes (history/polities/_notes/oc-01.md). The Context list of the author's brief is empty, and no counterpart outside the batch has a file in history/polities/ yet, so every outside counterpart counts as 'group not run'.

## Summary

Mechanical checks: `validate_dossier.py --resolve` gives 0 errors on all 16. The warnings are the gazetteer's (Moorea) and the new slugs colony-of-new-zealand and kingdom-of-oahu, which the author lists. 29 Wikipedia pages were opened. Every spot-checked event is on its page with its year. No event was fabricated or mis-dated at confidence 3.

| slug | verdict |
| --- | --- |
| kingdom-of-hawai-i | fix |
| kingdom-of-fiji | fix |
| kingdom-of-tonga | fix |
| tu-i-tonga-empire | thin |
| provisional-government-of-hawaii | pass |
| kingdom-of-tahiti | fix |
| kingdom-of-bau | fail |
| tovata-confederacy | thin |
| kingdom-of-samoa | fix |
| united-tribes-of-new-zealand | pass |
| maori-king-movement | fail |
| rapa-nui | thin |
| pohnpei-chiefdoms | pass |
| yapese-empire | thin |
| kingdom-of-maui | pass |
| kingdom-of-kauai | pass |

Two dossiers go back to their author: kingdom-of-bau (its land includes Rewa, its enemy) and maori-king-movement (the King Country appears with no event). The reviewer made the small fixes in six dossiers itself (listed under each one). Each was re-validated and read back after more than ten seconds.

## kingdom-of-hawai-i: fix

- **/wars/0/from** (applied by the reviewer). The Unification of Hawaii war began in 1782, nine years before the dossier's start (1791).
  - Evidence: Reviewer brief check 2: wars lie inside the life; the war's own note dates its start to Kalaniʻōpuʻu's death and Mokuʻōhai (1782).
  - Fix: 'from' set to 1791; a sentence added to the war's note saying the war began in 1782.
- **/ledger (1795), /identity/capitals/1** (for the author). The court's 1795 move to Honolulu/Waikīkī is in identity.capitals but has no capital_move event (the 1812, 1820 and 1845 moves do).
  - Evidence: Hawaiian Kingdom infobox: 'Waikīkī / Honolulu / Kailua-Kona' following Kamehameha I's movements (1795-1820).
  - Fix: Add a capital_move 1795 (confidence 2, source Hawaiian_Kingdom) or say in the capital's note why there is none.
- Gap (/notes): Cliopatria's relation row (Allegiance of Kingdom of Hawaiʻi to British Empire) 1811-1819 is confirmed by no page opened; no vassal event recorded. Page to try: https://en.wikipedia.org/wiki/George_Vancouver
- Spot checks: /ledger/1 confirmed (Unification_of_Hawaii); /ledger/3 confirmed (Kaumuali%CA%BBi); /ledger/5 confirmed (Hawaiian_Kingdom); /ledger/8 confirmed (Paulet_affair); /ledger/9 confirmed (Paulet_affair); /ledger/11 confirmed (Hawaiian_Kingdom).
- Area: infobox None km2, Cliopatria 24849.7 km2, ratio None, acknowledged True. No infobox area; the notes say so and call Cliopatria's 24,850 km2 (1811-1893) and 11,830 km2 (1791) plausible.

## kingdom-of-fiji: fix

- **/ledger/1/region/union/1, /identity/predecessors/1/land/union/1** (applied by the reviewer). Ma'afu's Lau was drawn as Natural Earth's Eastern Division, which also holds Lomaiviti (Bau's, in kingdom-of-bau) and Kadavu (Burebasaga).
  - Evidence: Gazetteer: Fiji admin1 'Eastern' (FJ-E) is the Eastern Division (Lau, Lomaiviti, Kadavu); tovata-confederacy draws the same land as the Lau circle plus the Northern Division; Enele Maʻafu page: the Tovata 'covering most of northern and eastern Fiji', Tovata page: 'Bua, Macuata and Cakaudrove on Vanua Levu, plus the Lau Islands'.
  - Fix: Replaced admin1 Eastern by {"lon": -178.8, "lat": -18.3, "km": 160} (the Lau stand-in tovata-confederacy uses), text kept, so the merge land equals tovata-confederacy's dissolve land.
- **/identity/predecessors/0/land** (for the author). Bau's handover land is the Central Division, which holds Rewa, Namosi and Serua as well as Tailevu and Naitasiri (see the kingdom-of-bau finding).
  - Evidence: Kubuna page: 'It consists of the provinces of Tailevu, Naitasiri, Lomaiviti, Ra, Rotuma, and parts of the western province of Ba'.
  - Fix: Copy the corrected kingdom-of-bau land here once the Bau author fixes it.
- Gap (/ledger/1): Merge of the Tovata at confidence 1: no page opened dates Ma'afu's adhesion to Cakobau's kingdom. Page to try: https://en.wikipedia.org/wiki/Lau_Islands
- Spot checks: /ledger/0 confirmed (Kingdom_of_Fiji); /ledger/2 confirmed (Kingdom_of_Fiji); /ledger/1 not on page (declared a bridging event at confidence 1; the page names Ma'afu only as a signatory of the 1874 cession) (Kingdom_of_Fiji).
- Area: infobox None km2, Cliopatria 21695.7 km2, ratio None, acknowledged True. No infobox area; notes compare Cliopatria's 21,696 km2 with Fiji's land and accept it.

## kingdom-of-tonga: fix

- **/ledger/1/region, /ledger/2/region** (applied by the reviewer). The Lau claim of 1848-1868 was drawn as the whole Eastern Division (Lau, Lomaiviti, Kadavu), so Lomaiviti is a Tongan vassal while kingdom-of-bau holds it (1852-1868).
  - Evidence: Enele Maʻafu page: 'Ma'afu established himself at Lakeba as leader of the Tongan community in the Lau Islands in 1848' (Lau only); gazetteer FJ-E is the Eastern Division.
  - Fix: Replaced admin1 Eastern by {"lon": -178.8, "lat": -18.3, "km": 160} (the Lau stand-in tovata-confederacy uses), text kept.
- **/ledger/2/month** (applied by the reviewer). The Tongan disclaimer had no month.
  - Evidence: Enele Maʻafu page: 'Ma'afu was faced with a crisis in June 1868, when the Tongan government disclaimed all sovereignty over Fijian territory'.
  - Fix: Month 6 added.
- **/ledger/1, /ledger/2 (counterpart 'Lau Islands (Ma'afu)')** (for the author). From February 1867 the same Lau land is tovata-confederacy's (found, counterpart nobody), while this dossier keeps it as a Tongan vassal until June 1868; neither dossier says so.
  - Evidence: Tovata page: conceived '14 February 1867 by the Tui Lau, Ma'afu'; Maʻafu page: the June 1868 disclaimer, after which he 'lost his authority as a Tongan prince over Lau' (author's quote).
  - Fix: Say in the note of /ledger/2 (and in tovata-confederacy /ledger/0) that from 1867 the vassal is Ma'afu's Tovata, or end the vassal tint in 1867.
- Gap (/ledger/1): Lau as a Tongan vassal from 1848 at confidence 1: the page says Ma'afu led the Tongan community, not that Tonga held suzerainty. Page to try: https://en.wikipedia.org/wiki/Lau_Islands
- Spot checks: /ledger/0 confirmed (George_Tupou_I); /ledger/1 confirmed (Enele_Ma%CA%BBafu); /ledger/2 confirmed (Enele_Ma%CA%BBafu); /wars/0 confirmed (George_Tupou_I).
- Area: infobox 748 km2, Cliopatria None km2, ratio None, acknowledged True. New keyframe (country Tonga); keyframe note quotes the infobox's 748 km2.

## tu-i-tonga-empire: thin

- **/ledger/3/region, /ledger/8/region** (applied by the reviewer). 'Parts of Fiji: the Lau Islands' was drawn as the whole Eastern Division (Lau, Lomaiviti, Kadavu).
  - Evidence: History of Tonga lists 'parts of Fiji'; the event's text names the Lau Islands; gazetteer FJ-E is the whole Eastern Division.
  - Fix: Replaced admin1 Eastern by {"lon": -178.8, "lat": -18.3, "km": 160} (the Lau stand-in tovata-confederacy uses), text kept.
- **/wars/1/to** (applied by the reviewer). The Tongan civil war ran to 1845, 46 years past the state's end (1799).
  - Evidence: Reviewer brief check 2 (wars inside the life); the war's note concedes it 'lies after this state's end'.
  - Fix: 'to' set to 1799; a sentence added to the note saying the war ran to the 1845 unification.
- Gap (/ledger/1, /ledger/2, /ledger/3, /ledger/4, /ledger/5, /ledger/6, /ledger/8, /ledger/9, /ledger/10): Nine confidence-1 placings of oral chronology (pages give centuries: 12th century extent, '13th or 14th century' Samoan expulsion, '15th and 16th centuries' ʻUvea-Futuna, decline after 1535). Page to try: https://en.wikipedia.org/wiki/Malietoa
- Gap (/ledger/6, /ledger/10): ʻUvea and Futuna: years of the Tongan hold. Page to try: https://en.wikipedia.org/wiki/Wallis_and_Futuna
- Spot checks: /ledger/0 confirmed (Tu%CA%BBi_Tonga_Empire); /ledger/5 confirmed (Tu%CA%BBi_Tonga_Empire); /ledger/7 confirmed (Tu%CA%BBi_Tonga_Empire); /ledger/11 confirmed (History_of_Tonga); /ledger/12 confirmed (History_of_Tonga).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area; new keyframes (Tongatapu, then the Tongan group).

## provisional-government-of-hawaii: pass

- Spot checks: /ledger/0 confirmed (Provisional_Government_of_Hawaii); /ledger/1 confirmed (Provisional_Government_of_Hawaii).
- Area: infobox None km2, Cliopatria 24849.7 km2, ratio None, acknowledged True. No infobox area; the shape is the kingdom's 1890 shape for 1893-1894. Tried: dates (17 January 1893, 4 July 1894), the handover to and from the kingdom and the Republic, the capital, the president (the infobox's Lorrin A. Thurston conflicts with the text's Dole; the dossier follows the text).

## kingdom-of-tahiti: fix

- **/keyframe_review/0/note** (applied by the reviewer). The 1808-1815 loss of Tahiti island, most of the kingdom's land, falls inside keyframe 0 (1788-1842) and the keyframe did not mention it.
  - Evidence: Kingdom of Tahiti page: 'forced to take refuge in Moʻorea 22 December 1808'; 'the decisive Battle of Te Fe'i Pī, on 12 November 1815'. Reviewer brief check 4: an event with no trace in the keyframes must be small or flagged in the keyframe.
  - Fix: Sentence added to the keyframe note pointing to /ledger/1 and /ledger/2.
- **/ledger (1843-1847)** (for the author). France's annexation of November 1843 to February 1847 is drawn as neither an occupation nor a loss; only the 1844-1846 contest is recorded.
  - Evidence: Franco-Tahitian War page: 'In November 1843, Dupetit Thouars deposed the queen for her continued resistance and formally annexed the islands'; 'In February 1847, Queen Pōmare IV returned from her exile and acquiesced to rule under the protectorate'.
  - Fix: Add occupation_start 1843-11 / occupation_end 1847-02 with counterpart bourbon-kingdom-of-france (the owner's side of rule 4), or say in keyframe 1's note why the annexation is not drawn.
- Gap (/keyframe_review/1): The Kingdom page's lead says the kingdom 'eventually annexed the Tuamotus, and the Austral Islands'; undated and not drawn (the notes name only the Tuamotus). Page to try: https://en.wikipedia.org/wiki/Austral_Islands
- Gap (/ledger/1): The rebel chiefs who held Tahiti in 1808-1815 are not named on the page (counterpart is a string with no dossier). Page to try: https://en.wikipedia.org/wiki/P%C5%8Dmare_II
- Spot checks: /ledger/1 confirmed (Kingdom_of_Tahiti); /ledger/2 confirmed (Kingdom_of_Tahiti); /ledger/3 confirmed (Franco-Tahitian_War); /ledger/4 confirmed (Franco-Tahitian_War); /ledger/6 confirmed (Kingdom_of_Tahiti).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area; the keyframe note gives about 1,260 km2 of cells for Tahiti and Moʻorea.

## kingdom-of-bau: fail

- **/keyframe_review/0/correction, /ledger/0/region, /ledger/2/region, /identity/successors/0/land** (for the author, blocking). Bau's land is drawn as Natural Earth's Central Division, which besides Tailevu and Naitasiri holds Rewa, Namosi and Serua: the Burebasaga side, with Rewa Bau's enemy in these years. The text equates the division with 'Tailevu and Naitasiri', which is wrong.
  - Evidence: Kubuna page: 'It consists of the provinces of Tailevu, Naitasiri, Lomaiviti, Ra, Rotuma, and parts of the western province of Ba' and 'The capital of the confederacy is the chiefly island of Bau in Tailevu'. The keyframe note itself: 'Rewa, in the Central Division, is the rival chiefdom of the Bau-Rewa wars'. kingdom-of-tonga /wars/0 has 'Rewa and the Bauan rebels' fighting Bau at Kaba in 1855.
  - Fix: Replace admin1 Central by a stand-in for Tailevu and Naitasiri only (for example a circle of about 35 km at 178.45 E, 17.75 S, or Central minus a circle over the Rewa delta, Suva, Namosi and Serua), keep the Lomaiviti circle, and copy the same land into kingdom-of-fiji /identity/predecessors/0/land.
- **/wars** (for the author). The Battle of Kaba (1855), where Tonga fought for Cakobau, is not in Bau's wars, though kingdom-of-tonga lists kingdom-of-bau as a belligerent.
  - Evidence: Cakobau page: 'Cakobau crushed the rebellion with the aid of the King of Tonga'; George Tupou I page: 'Tupou defeated Cakobau's enemies at the Battle of Kaba in 1855'.
  - Fix: Add a war 'Battle of Kaba', 1855-1855, belligerents kingdom-of-bau, kingdom-of-tonga, 'Rewa and the Bauan rebels', zones [] (no ground recorded as changing hands), source George_Tupou_I (add it to sources).
- Gap (/ledger): The Bau-Rewa wars, Bau's extent in 1852-1871 and Cakobau's title in 1869-1871 are on no page opened. Page to try: https://en.wikipedia.org/wiki/Ratu_Tanoa_Visawaqa
- Spot checks: /ledger/0 confirmed (Seru_Epenisa_Cakobau); /ledger/1 confirmed (Seru_Epenisa_Cakobau); /ledger/2 confirmed (Seru_Epenisa_Cakobau).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area (Bau Island page; Kingdom of Bau does not exist).

## tovata-confederacy: thin

- **/ledger/0/note** (for the author). The Lau core is founded on nobody's land in February 1867 while kingdom-of-tonga keeps Lau as a Tongan vassal until June 1868.
  - Evidence: Enele Maʻafu page: 'a crisis in June 1868, when the Tongan government disclaimed all sovereignty over Fijian territory'.
  - Fix: Say in the note that Ma'afu held Lau as a Tongan prince until June 1868 (the same note as kingdom-of-tonga /ledger/2).
- Gap (/ledger/2): The adhesion to the Kingdom of Fiji (June 1871) is bridged at confidence 1. Page to try: https://en.wikipedia.org/wiki/Lau_Islands
- Gap (/ledger/1): Macuata's joining is undated (placed with Cakaudrove and Bua in May 1869). Page to try: https://en.wikipedia.org/wiki/Macuata_Province
- Spot checks: /ledger/0 confirmed (Tovata); /ledger/1 confirmed (Enele_Ma%CA%BBafu); /ledger/2 not on page (declared a bridging event at confidence 1) (Kingdom_of_Fiji).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area.

## kingdom-of-samoa: fix

- **/wars/0 (new)** (applied by the reviewer). The infobox's 'War between Pulefou and Taimua and Faipule: 1879-1881' was not in wars (the notes mention it as 'named only in the infobox').
  - Evidence: Kingdom of Samoa infobox, read by the reviewer. Reviewer brief check 10: each war in the sources appears, with empty zones where no ground changed hands.
  - Fix: Added as /wars/0 with zones [] and a note; the First and Second Samoan Civil Wars are now /wars/1 and /wars/2.
- **/wars/1/from** (for the author). The First Samoan Civil War starts in 1886, a year neither infobox gives.
  - Evidence: Kingdom of Samoa infobox: 'First Samoan Civil War: 1889-1894'; First Samoan Civil War page infobox: '1887–1889' and '1893–1894'. The war's note says the body text gives 1886-1894 (not verified by the reviewer).
  - Fix: Quote the body sentence for 1886 in the note, or use 1887 and cite First_Samoan_Civil_War.
- **/ledger (1882, 1887)** (for the author). The capital returns to Mulinuʻu in 1882 and moves to Leulumoega in 1887 in identity.capitals, with no capital_move events.
  - Evidence: Infobox: 'Mulinu'u (1873-1887)', 'Leulumoega 1880-1881', 'Leulumoega (1887-1888)', 'Mulinu'u (1889-1899)'.
  - Fix: Add capital_move 1882 and 1887 (confidence 2, source Kingdom_of_Samoa).
- Gap (/wars/2): Mataʻafa's 1899 rebel government at Aele and its land are not drawn. Page to try: https://en.wikipedia.org/wiki/Second_Samoan_Civil_War
- Spot checks: /ledger/0 confirmed (Kingdom_of_Samoa); /ledger/1 confirmed (Kingdom_of_Samoa); /ledger/2 confirmed (Kingdom_of_Samoa); /ledger/3 confirmed (Kingdom_of_Samoa).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area.

## united-tribes-of-new-zealand: pass

- Spot checks: /ledger/0 confirmed (United_Tribes_of_New_Zealand); /ledger/1 confirmed (United_Tribes_of_New_Zealand).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. Infobox gives no area; Northland stand-in for 'the north of the North Island' ('52 signatories from Northland'). Tried: the dates, the land, the end at the 21 May 1840 proclamation against the February 1840 treaty, the successor (Colony of New South Wales then Colony of New Zealand, both in the infobox, both in the notes).

## maori-king-movement: fail

- **/keyframe_review/1, /keyframe_review/0/correction, /ledger/0/region** (for the author, blocking). The King Country (70 km circle, about 15,400 km2) appears in keyframe 1 (1864) with no ledger event bringing it in: between the keyframes the ledger holds only the Waikato loss (/ledger/4), yet the drawn area doubles (keyframe 0 is a 50 km circle, about 7,850 km2).
  - Evidence: Māori King Movement page: the 'first circle' of supporters was Waikato, Maniapoto and Hauraki; King Country page: 'the Kingite forces retreated southwards from the Waikato after the battle at Ōrākau in April 1864' into Ngāti Maniapoto land. Reviewer brief check 4.
  - Fix: Either add the King Country to the 1858 found region and keyframe 0's correction (union of the Hamilton 50 km circle and the King Country stand-in, Maniapoto being in the movement from its founding), or add a gain 1864-04 (counterpart nobody, source King_Country) of the King Country; and say which in keyframe 1's note.
- **/keyframe_review/1/correction, /ledger/5/region, /identity/successors/0/land** (for the author). The King Country circle (175.1 E, 38.5 S, 70 km) reaches 37.87 S, north of the aukati on the Pūniu near Kihikihi (about 38.04 S), and so re-draws Te Awamutu and Ōrākau, which are in the Waikato lost in April 1864 (/ledger/4, a Hamilton 50 km circle).
  - Evidence: King Country page: 'a line of pā alongside the Puniu River near Kihikihi'; its north edge is 'Kawhia Harbour and the town of Ōtorohanga'.
  - Fix: Move the circle south or shrink it so its north edge stays at the Pūniu (for example 175.1 E, 38.6 S, 55 km), or subtract the Hamilton 50 km circle.
- Gap (/identity/capitals/1): The king's seat 1864-1883 is not named. Page to try: https://en.wikipedia.org/wiki/T%C4%81whiao
- Spot checks: /ledger/0 confirmed (M%C4%81ori_King_Movement); /ledger/1 confirmed (Invasion_of_the_Waikato); /ledger/2 confirmed (Invasion_of_the_Waikato); /ledger/3 confirmed (Invasion_of_the_Waikato); /ledger/5 confirmed (King_Country).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area; the Invasion page's confiscation ('about 12,000 km2', '486,500 hectares') is quoted in /ledger/4.

## rapa-nui: thin

- Gap (/ledger/0): Start 1200 at confidence 1: the page gives settlement estimates from 400 to 1300 CE ('current best estimate ... 12th century'). Page to try: https://en.wikipedia.org/wiki/Hotu_Matu%CA%BBa
- Gap (/identity/capitals): No seat for the ariki mau. Page to try: https://en.wikipedia.org/wiki/Anakena
- Spot checks: /ledger/0 confirmed (Easter_Island); /ledger/1 confirmed (Easter_Island); /wars/1 confirmed (Easter_Island).
- Area: infobox 163.6 km2, Cliopatria None km2, ratio 1.55, acknowledged True. One grid cell (about 253 km2) against the infobox's 163.6 km2; stated in the keyframe note.

## pohnpei-chiefdoms: pass

- Spot checks: /ledger/0 confirmed (Saudeleur_dynasty); /ledger/1 confirmed (Saudeleur_dynasty); /ledger/2 confirmed (Pohnpei).
- Area: infobox 334 km2, Cliopatria None km2, ratio 1.5, acknowledged True. Two grid cells (about 506 km2) against the page's 334 km2; stated in the keyframe note. Tried: start (c. 1100-1200), the c. 1628 rename against the legend's 1500s (noted), the end (Pohnpei page: 'Spanish period 1886–1899', 'By 1886 the Spaniards claimed the Caroline Islands'), Nan Madol's coordinates, the successor slug kingdom-of-spain (polities.csv 1516-2024).

## yapese-empire: thin

- Gap (/ledger/1): End 1899 (sale to Germany) bridged at confidence 1. The batch's own pohnpei-chiefdoms ends the Carolines' independence at Spain's claim 'by 1886' (Pohnpei page: 'Spanish period 1886–1899'), so Yap more likely passes to kingdom-of-spain about 1885-1886, then to german-empire in 1899. Page to try: https://en.wikipedia.org/wiki/Caroline_Islands
- Spot checks: /ledger/0 confirmed (Sawei); /ledger/1 confirmed (Yap).
- Area: infobox 100 km2, Cliopatria None km2, ratio 2.5, acknowledged True. One grid cell (about 253 km2) against the infobox's 100 km2 of land: a grid-resolution limit, stated in the keyframe note.

## kingdom-of-maui: pass

- Gap (/identity/capitals): No capital (empty list); Kahekili's seat on Maui is on no page opened. Page to try: https://en.wikipedia.org/wiki/Wailuku,_Hawaii
- Spot checks: /ledger/0 confirmed (Kahekili_II); /ledger/1 confirmed (Unification_of_Hawaii); /ledger/2 confirmed (Unification_of_Hawaii); /ledger/3 confirmed (Unification_of_Hawaii); /ledger/4 confirmed (Unification_of_Hawaii); /ledger/6 confirmed (Unification_of_Hawaii).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No article (Kingdom of Maui does not exist on Wikipedia), no area. Tried: each dated event of 1765-1795 against the Kahekili II and Unification pages, the 1794 loss and gain pair against kingdom-of-kauai, the 1795 transfer against kingdom-of-hawai-i.

## kingdom-of-kauai: pass

- Gap (/identity/capitals): No capital (empty list). Page to try: https://en.wikipedia.org/wiki/Waimea,_Kauai_County,_Hawaii
- Spot checks: /ledger/0 confirmed (Kamakahelei); /ledger/1 confirmed (Unification_of_Hawaii); /ledger/2 confirmed (Kamakahelei); /ledger/3 confirmed (Kaumuali%CA%BBi).
- Area: infobox None km2, Cliopatria None km2, ratio None, acknowledged True. No infobox area; keyframe note compares about 1,430 km2 with about 1,000 km2 of cells. Tried: the 1770 start, the 1794 pair with kingdom-of-maui, the 1810-1824 tributary span (recorded by the suzerain kingdom-of-hawai-i), the 26 May 1824 end.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-hawai-i 1795 gain (kingdom-of-maui) | kingdom-of-maui 1795 loss | matched | Maui Nui by loss, Oʻahu by Maui's dissolve, both to kingdom-of-hawai-i; same circles. |
| kingdom-of-hawai-i 1810 vassal_start (kingdom-of-kauai) | kingdom-of-kauai 1770 found | matched | Schema: vassal events live in the suzerain's ledger only; kingdom-of-kauai runs to 1824 so the tint has land. |
| kingdom-of-hawai-i 1824 vassal_end (kingdom-of-kauai) | kingdom-of-kauai 1824 dissolve | matched | May 1824 both sides. |
| kingdom-of-hawai-i 1824 gain (kingdom-of-kauai) | kingdom-of-kauai 1824 dissolve | matched | Kauaʻi's dissolve names kingdom-of-hawai-i as successor (Lihue 100 km both sides). |
| kingdom-of-hawai-i 1843 occupation_start (kingdom-of-great-britain) | none | exception | kingdom-of-great-britain (polities.csv 1709-2024) has no dossier yet: its group has not run; it should record occupation_start 1843-02 / occupation_end 1843-07 of kingdom-of-hawai-i. |
| kingdom-of-hawai-i 1843 occupation_end (kingdom-of-great-britain) | none | exception | As above. |
| kingdom-of-fiji 1871 merge (tovata-confederacy) | tovata-confederacy 1871 dissolve | matched | June 1871 both sides; land now identical (Northern Division plus the Lau circle) after the reviewer's fix to kingdom-of-fiji. |
| kingdom-of-fiji 1871 found (kingdom-of-bau) | kingdom-of-bau 1871 dissolve | matched | June 1871; the handed-over land (Central Division plus Lomaiviti) is wrong on both sides and is fixed with the kingdom-of-bau finding. |
| kingdom-of-tonga 1848 vassal_start (Lau Islands (Ma'afu)) | none | exception | String counterpart with no dossier (Ma'afu's Tongan community in Lau). |
| kingdom-of-tonga 1868 vassal_end (Lau Islands (Ma'afu)) | tovata-confederacy 1867 found | mismatch | Tovata founds itself on the same Lau land in February 1867 with counterpart nobody while Tonga's vassal tint runs to June 1868; overlap of 16 months, unexplained on both sides (non-blocking note in both dossiers). |
| tu-i-tonga-empire 1100 gain (nobody) | none | exception | nobody. |
| tu-i-tonga-empire 1100 vassal_start (Samoa (Malietoa)) | tu-i-tonga-empire 1250 vassal_end | exception | String counterpart, no dossier for the pre-1873 Samoan districts; kingdom-of-samoa starts 1873. |
| tu-i-tonga-empire 1100 vassal_start (Lau Islands (Fiji)) | none | exception | String counterpart, no dossier; region now the Lau circle. |
| tu-i-tonga-empire 1100 vassal_start (Niue, Rotuma and Tokelau) | none | exception | String counterpart, no dossier. |
| tu-i-tonga-empire 1450 vassal_start (ʻUvea and Futuna) | none | exception | String counterpart, no dossier. |
| kingdom-of-tahiti 1808 loss (Tahitian rebel chiefs) | none | exception | Unnamed rebel chiefs on the page; no dossier possible from the pages opened (thin). |
| kingdom-of-tahiti 1815 gain (Tahitian rebel chiefs) | none | exception | As above. |
| bourbon-kingdom-of-france 1842 vassal_start (kingdom-of-tahiti) | kingdom-of-tahiti 1788 found | exception | Missing on the suzerain side: bourbon-kingdom-of-france, french-second-republic, second-french-empire and french-third-republic have no dossiers yet (group not run); they must carry the protectorate 9 September 1842 - 29 June 1880. |
| kingdom-of-great-britain 1900 vassal_start (kingdom-of-tonga) | kingdom-of-tonga 1845 found | exception | Missing on the suzerain side (Treaty of Friendship 18 May 1900 - 4 June 1970, Tonga infobox); british-colonial-empire / kingdom-of-great-britain group not run. |
| kingdom-of-maui 1783 gain (kingdom-of-oahu) | none | exception | kingdom-of-oahu has no dossier; listed in the author's counterparts_needing_dossiers. |
| kingdom-of-maui 1794 loss (kingdom-of-kauai) | kingdom-of-kauai 1794 gain | matched | July 1794 both sides, Maui Nui circle. |
| kingdom-of-maui 1794 gain (kingdom-of-kauai) | kingdom-of-kauai 1794 loss | matched | December 1794 both sides (Kāʻeokūlani killed 12 December 1794). |
| kingdom-of-maui 1790 contest_start (kingdom-of-hawai-i) | none | mismatch | Counterpart kingdom-of-hawai-i starts in 1791, so in 1790 it does not exist; its war 'Unification of Hawaii' now starts 1791. Not blocking: Kamehameha's pre-1791 domain on Hawaiʻi island has no dossier; consider naming the 1790 counterpart 'Kamehameha (Kona, Kohala, Hāmākua)' or noting it. |
| maori-king-movement 1864 loss (colony-of-new-zealand) | none | exception | colony-of-new-zealand has no dossier or Cliopatria row (New Zealand starts 1948); listed in the author's counterparts_needing_dossiers. |
| tovata-confederacy 1869 gain (nobody) | none | exception | nobody. |

## Gazetteer names needed

- Moorea (place): kingdom-of-tahiti
- King Country (Rohe Pōtae) (region): maori-king-movement
- Waikato (region): maori-king-movement
- Lau Islands (region): tovata-confederacy; kingdom-of-fiji; kingdom-of-tonga; tu-i-tonga-empire
- Lomaiviti (region): kingdom-of-bau
- Tailevu (region): kingdom-of-bau (needed for the fix)
- Naitasiri (region): kingdom-of-bau (needed for the fix)
- Rewa (region): kingdom-of-bau (to subtract)
- Bau (place): kingdom-of-bau
- Easter Island (Rapa Nui) (region): rapa-nui
- Yap outer islands (Ulithi, Woleai, Satawal, Lamotrek, Elato) (region): yapese-empire
- Maui Nui (region): kingdom-of-maui; kingdom-of-hawai-i; kingdom-of-kauai
- Oʻahu (region): kingdom-of-maui; kingdom-of-hawai-i
- Kauaʻi and Niʻihau (region): kingdom-of-kauai; kingdom-of-hawai-i
- Hawaiʻi island (region): kingdom-of-hawai-i
- Manuʻa Islands (region): tu-i-tonga-empire; kingdom-of-samoa (admin1 Manu's has 0 cells)
- Niuas (region): tu-i-tonga-empire

## Counterparts needing dossiers

- Colony of New Zealand (colony-of-new-zealand, years [1841])
- Kingdom of Oʻahu (Kahahana) (kingdom-of-oahu, years [1783])
- Keōua Kūʻahuʻula's Kaʻū and Puna chiefdom (kau-and-puna-chiefdom, years [1790, 1791])
- Burebasaga Confederacy (Rewa) (burebasaga-confederacy, years [])
- Leeward Islands kingdoms (Raiatea-Tahaa, Huahine, Bora Bora) (leeward-islands-kingdoms, years [1847, 1897])
- Tuʻi Manuʻa (Manuʻa chiefdom) (tui-manua, years [1904])
- Faitasiga (Samoan confederacy) (faitasiga, years [1873])

## Problems

- No page failed to load for the reviewer (29 Wikipedia pages opened).
- Neighbour dossiers: the author brief's Context list is empty ('none within 25 km in this era'); every counterpart outside the batch (kingdom-of-great-britain, british-colonial-empire, bourbon-kingdom-of-france and the later French states, german-empire, united-states-of-america, republic-of-chile, kingdom-of-spain, republic-of-hawai-i) has no file in history/polities/ yet: counted as 'group not run'.
- Reviewer edits (orchestrator's small-fix rule; each re-validated with 0 errors and read back after more than 10 s): kingdom-of-fiji (Lau region in /ledger/1 and /identity/predecessors/1), kingdom-of-tonga (/ledger/1-2 Lau region, /ledger/2 month 6), tu-i-tonga-empire (/ledger/3 and /ledger/8 Lau region, /wars/1/to 1799), kingdom-of-hawai-i (/wars/0/from 1791), kingdom-of-tahiti (/keyframe_review/0/note), kingdom-of-samoa (new /wars/0; later wars shift by one).
- kingdom-of-bau's land fix must be copied into kingdom-of-fiji /identity/predecessors/0/land (kingdom-of-fiji is otherwise accepted).
- republic-of-hawai-i (another group) should start in July 1894, where provisional-government-of-hawaii ends; Cliopatria's row starts 1895.
