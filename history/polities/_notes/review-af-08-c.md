# Review of batch af-08-c (german-africa, british-gold-coast, british-togoland)

Reviewer, 2026-10-24. Validator: 0 errors, 0 warnings for all three (with --resolve). Spot checks: every event opened said what its note claims, with the year; nothing fabricated. All three fail on missing events (mirror and war events), not on sources.

## german-africa: fail

Area: infobox 2,710,500 km2 (1912), Cliopatria 2,671,308 km2, ratio 0.99. No single infobox for the aggregate; sum of the colony infoboxes for 1912: GEA 995,000 (opened), GSWA 835,100 (opened), Kamerun 790,000 (opened), Togoland 90,400 (opened). Cliopatria german-africa_1911 (1911-1913). The author's keyframe_review/8 gives the same sum.

### Findings

- **/ledger (1914-1919; after /ledger/20, /23, /27, /29, /30)** (blocking): The dossier keeps the occupied colonies as German land 'hatched in the occupier's colour' until 28 June 1919 (keyframe_review/9-14), but books no owner-side occupation_start/occupation_end for any of them: the only occupation events are German occupations of Kenya, Mozambique and Rhodesia. After each contest_end the land falls back to plain German colour.
  - Evidence: Schema, ledger type: occupation 'the owner records the same event with the roles reversed'. keyframe_review/9 note: 'the contest events and occupation events carry the wartime changes'. Neighbours book the occupier side: french-africa /ledger/60 occupation_start german-africa 1914/8 (Togo), /61 1915 (Neukamerun), /62 1916/2 (French zone of Kamerun); british-africa /31 1915/7 (Namibia), /32 1916 (Tanganyika minus Kigoma); south-africa /1 1915 (Namibia); belgian-congo /2 1916 (Kigoma), /4 1916/5 (Rwanda-Burundi); british-togoland /3 1914/8 (British zone of Togoland). Dates on the pages: Togoland surrendered 26 August 1914 (German Togoland); Khorab 9 July 1915 (GSWA); 'by 17 June, Burundi and Rwanda were occupied' (EAC); Kamerun campaign ended 10 March 1916.
  - Fix: Add one occupation_start per occupier at the occupation date and a matching occupation_end at 1919/6 (same counterpart string): french-africa Togo 1914/8; british-togoland the Ghana part of Togoland 1914/8; south-africa Namibia 1915/7 (decide with british-africa which of the two siblings is the occupier: both book it); french-africa the French zone of Kamerun 1916/2-3; british-africa (or british-cameroons once written) Nord-Ouest+Sud-Ouest 1916/2-3; belgian-congo Rwanda+Burundi 1916/5-6 and Kigoma 1916; british-africa Tanganyika minus Kigoma 1916 (progressively; at the latest 1917/11). Neukamerun: either an occupation by french-africa from 1914/1915 ending with the 1916 loss, or keep the 1916 loss and say why french-africa's 1915 occupation and 1919 gain are not mirrored.
- **/ledger/43/region**: The dissolve region is Cliopatria's German Africa 1914 shape ('all four colonies'), which still contains Neukamerun although /ledger/26 gives it to France in 1916.
  - Evidence: Agadir Crisis page: 'During the First World War, in 1916, Neukamerun returned to France.' keyframe_review/14 (1919) already subtracts it.
  - Fix: Use the 1919 keyframe's correction (German Africa 1914 minus (German Africa 1911 minus German Africa 1905)) as the dissolve region.
- **/identity/capitals/2**: Windhuk is a capital from 1884, but the 1884 keyframe is only 100 km round Lüderitz (Windhoek lies about 680 km inland) and the GSWA page does not support 1884.
  - Evidence: GSWA page: infobox 'Capital: Windhuk' with no year; Göring 'established his administration at Otjimbingwe'; the earliest Windhoek date on the page is a school in 1894. Rule 9: capitals inside the state's shapes in those years.
  - Fix: Start Windhuk no earlier than its founding as seat (about 1891, from a page such as the Windhoek article) with Otjimbingwe before it, or at least start the span at 1885 and say 'unverified'. Likewise Lomé (named capital only in 1895 on the German Togoland page) and Douala/Jaunde (Kamerun infobox gives only 'Capital: Jaunde', no year): mark the spans as unverified in the capital notes.
- **/ledger/4/region**: The 1885 gain of the whole of Tanganyika from 'nobody' includes the 16 km coastal strip that the event's own note says the Sultan of Zanzibar kept; no later event transfers the coast.
  - Evidence: GEA page: 'The Sultan was forced to accept the German claims on the mainland outside a 16-kilometre (10 mi)-strip along the coast'; the page names only the 1890 Heligoland-Zanzibar Treaty as the settlement.
  - Fix: Either say in the note that the coastal strip is drawn German from 1885 for want of a page, or exclude it until 1890 and add a 1890 gain of the coast with counterpart sultanate-of-zanzibar (the pre-1963 sultanate has no dossier yet; the existing sultanate-of-zanzibar.json covers only 1963-1964).

### Gaps for a gap-filler

- /ledger/3: Date and extent of the claim to the whole of South West Africa (1885, confidence 1); the GSWA page has only the April 1885 Kolonialgesellschaft, which concerns company rights (try https://en.wikipedia.org/wiki/History_of_Namibia)
- /ledger/5: Inland extension of Togoland in 1890 (confidence 1); German Togoland page: 'Germany gradually extended its control inland', no date (try https://en.wikipedia.org/wiki/Togoland_Neutral_Zone)
- /ledger/6, /ledger/10, /ledger/13: Kamerun hinterland 1890, 1895, 1905 (confidence 1) and the Nigeria/Chad slivers of the 1905 shape; the Anglo-German (1893) and Franco-German (1894) Cameroon boundary agreements (try https://en.wikipedia.org/wiki/Adamawa_Emirate)
- /ledger/11: Rwanda under German control, 1898 (confidence 1); kingdom-of-rwanda dissolves 1897 to german-africa (try https://en.wikipedia.org/wiki/Ruanda-Urundi)
- /ledger/12: Burundi under German control, 1900 (confidence 1) against kingdom-of-burundi's dissolve in 1903; the Treaty of Kiganda (1903) may settle it (try https://en.wikipedia.org/wiki/Treaty_of_Kiganda)
- /ledger/25: British retaking of Taveta, 1916 (confidence 1; the EAC page does not have it) (try https://en.wikipedia.org/wiki/Battle_of_Salaita_Hill)
- /ledger/38: Portuguese retaking of the Kionga Triangle in 1916 (an occupation 1916-1919 under rule 4) (try https://en.wikipedia.org/wiki/Kionga_Triangle)

### Spot checks

- /ledger/4: confirmed (https://en.wikipedia.org/wiki/German_East_Africa): infobox 'Established by the DOAG: 27 February 1885'; charter 'signed by Chancellor Otto von Bismarck on 27 February 1885' (but see the coastal-strip fix)
- /ledger/8: confirmed (https://en.wikipedia.org/wiki/German_South_West_Africa): 'In July of the same year [1890], as part of the Heligoland-Zanzibar Treaty ... the acquisition of the Caprivi Strip'
- /ledger/9: confirmed (https://en.wikipedia.org/wiki/German_East_Africa): 'Germany had virtually forced Portugal to cede the triangle in 1894'
- /ledger/26: confirmed (https://en.wikipedia.org/wiki/Agadir_Crisis): 'During the First World War, in 1916, Neukamerun returned to France.'
- /ledger/33: confirmed (https://en.wikipedia.org/wiki/East_African_campaign_(World_War_I)): 'The Germans returned to German East Africa and crossed into Rhodesia in August 1918'; 'On 9 November the German force reached Kasama'
- /ledger/34: confirmed (https://en.wikipedia.org/wiki/East_African_campaign_(World_War_I)): 'at 11:00 a.m. on 25 November 1918, Lettow-Vorbeck offered his surrender to the British at Abercorn'
- /ledger/17, /ledger/20: confirmed (https://en.wikipedia.org/wiki/German_Togoland): invaded 7 August 1914; 'The colony surrendered on 26 August 1914'
- /ledger/29: confirmed (https://en.wikipedia.org/wiki/East_African_campaign_(World_War_I)): Force Publique from 18 April 1916; 'by 17 June, Burundi and Rwanda were occupied'
- /ledger/43: confirmed (https://en.wikipedia.org/wiki/German_East_Africa): infobox 'Formal disestablishment: 28 June 1919'

## british-gold-coast: fail

Area: infobox 207,199 km2 (1924), Cliopatria 1,194,700 km2, ratio 5.77. Cliopatria british-gold-coast_1918 (1918-1941) is a Gold Coast + Nigeria + British Cameroons composite; keyframe notes give the ratio (5.8) and every shape is corrected to the Ghana part (1960 marked wrong).

### Findings

- **/ledger (1850) and /keyframe_review/0** (blocking): The Danish Gold Coast's incorporation in 1850 is missing: the 1821-1871 keyframe stays a 30 km circle round Cape Coast and the Danish forts (Christiansborg/Accra, Ada, Keta) never enter the colony before the 1873 Cliopatria shape.
  - Evidence: Gold Coast page infobox (the dossier's own main source): 'Incorporation of the Danish Gold Coast: 1850'; the capital later moves 'to the former Danish castle at Christiansborg in Accra' (1877). danish-gold-coast /ledger/15 dissolves 1850/3 with counterpart british-colonial-empire, which has no dossier (eu-11 has not run), so the forts have no owner in 1850-1872.
  - Fix: Add a gain at 1850 (month 3 if the Danish dossier's date holds) with counterpart danish-gold-coast, region = the danish-gold-coast dissolve region, confidence 3, source the Gold Coast page; split keyframe_review/0 at 1850 (1821-1849 Cape Coast; 1850-1871 plus the Danish forts) and carry the forts into the 1872 keyframe's correction. Ask danish-gold-coast's group to change its dissolve counterpart and successor to british-gold-coast.
- **/wars/2 and /ledger (1900)** (blocking): The War of the Golden Stool has a zone (Ashanti) but the ledger has no contest_start/contest_end, so the map draws no fighting; the dossier has no contest events at all.
  - Evidence: War of the Golden Stool page: infobox 'March - September 1900'; Hodgson reached Kumasi 'on 25 March 1900'; 'The war lasted for six months.' Rule 6/10: a war zone is drawn from contest events.
  - Fix: Add contest_start 1900/3 and contest_end 1900/9, counterpart 'Asante rebels under Yaa Asantewaa' (the string used in the war's belligerents), region the war's zone (Cliopatria Ashanti Empire 1895), confidence 3, source the War of the Golden Stool page. For the Fourth Anglo-Ashanti War (/wars/1) either add the 1895/12-1896/1 pair or empty its zones and say Kumasi was occupied without fighting.
- **/ledger/3 and /wars/0** (blocking): 1874: ashanti-empire books a contest with this state (1873 to 1874/2, its /ledger/14-15) and a loss to it of the coast and Assin country south of the Pra (/ledger/16, 1874/2); this dossier has only a rename and a Third Anglo-Ashanti War with empty zones 'no ground changed hands'.
  - Evidence: Gold Coast page: the January 1874 attack 'resulted in the occupation and burning of Kumasi'; 'The Gold Coast Colony, established on 24 July 1874, comprised the coastal areas and extended inland'; 'The subsequent peace treaty required the Asante to renounce any claim to many southern territories.' The /ledger/3 note quotes only 'comprised the coastal areas'.
  - Fix: Add the mirror contest pair (1873, 1874/2) and give /wars/0 its zone; add a gain at 1874 (2 or 7) with counterpart ashanti-empire, confidence 2, for the land ashanti-empire cedes (or agree with ashanti-empire's group that the coast was Fante land, counterpart nobody, and say so); make the 1872 and 1873 keyframes agree.
- **/ledger/9, /ledger/10**: The 1901 vassal_end and gain name ashanti-empire as counterpart, but that dossier dissolves in 1896/1 (counterpart british-gold-coast), so the gain is from a state that no longer exists and the vassal relation has no mirror.
  - Evidence: ashanti-empire /ledger/22: dissolve 1896/1, counterpart british-gold-coast. War of the Golden Stool page: 'Ashanti Order in Council 1901 made on 26 September 1901'; Gold Coast page: protectorate from 1896, colony 1901 (infobox) / 1902 (text). The author flagged the disagreement.
  - Fix: Route to ashanti-empire's group (af-04): either the Asante state continues to 1901/9 as this colony's protectorate (then vassal_start/vassal_end in both ledgers), or this dossier takes the land as a gain at 1896/1 and draws the protectorate otherwise. Not blocking for this dossier alone.
- **/ledger/7/region**: The 1897 Northern Territories gain is admin1 'Northern' only, which leaves out Upper West and Upper East, where Wa and Dagarti (named in the event's counterpart) lie; they arrive only with the 1899 'nobody' gain.
  - Evidence: Northern Territories page: treaties of 1896 'with the Chiefs of Bona, Dagarti, Wa and Mamprusi at Gambaga'; 'constituted as a district in 1897'.
  - Fix: Add Upper West (and Upper East if Mamprusi's lands are meant) to the 1897 region, or say in the note that the far north is left to 1899. Minor.

### Gaps for a gap-filler

- /keyframe_review/0: Extent of the colony 1821-1871 (30 km placeholder) and the Bond of 1844 'informal protectorate' over Fante coastal areas (a vassal_start candidate under rule 4) (try https://en.wikipedia.org/wiki/Bond_of_1844)
- /keyframe_review/2-5: Growth of the Ghana part from 40 cells (1873) to 59 (1885) and 75 (1890-1897) with no ledger event (try https://en.wikipedia.org/wiki/Fante_Confederacy)
- /ledger/8: The 1898-1899 frontier agreements with France and Germany (page: 'amicably demarcated'); the 1899 Neutral Zone/Volta Triangle outcome (try https://en.wikipedia.org/wiki/Togoland_Neutral_Zone)

### Spot checks

- /ledger/0: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): infobox 'Colony established: 1821'; 'Cape Coast (1821-1877)'
- /ledger/1: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): infobox 'Incorporation of the Dutch Gold Coast: 6 April 1872'
- /ledger/4: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): infobox 'Cape Coast (1821-1877) Accra (1877-1957)'
- /ledger/6: confirmed (https://en.wikipedia.org/wiki/War_of_the_Golden_Stool): 'Ashanti was once again occupied by British troops in January 1896'; protectorate wording is from the Gold Coast page, as the note says
- /ledger/7: confirmed (https://en.wikipedia.org/wiki/Northern_Territories_of_the_Gold_Coast): 'These treaties were made in 1896'; 'The Northern Territories were constituted as a district in 1897'
- /ledger/10: confirmed (https://en.wikipedia.org/wiki/War_of_the_Golden_Stool): 'Ashanti Order in Council 1901 made on 26 September 1901'
- /ledger/11: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): infobox 'Admission of British Togoland: 27 December 1916'
- /ledger/12: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): infobox 'Incorporation of British Togoland: 11 December 1956' (British Togoland page: 13 December 1956)
- /ledger/13: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): 'Independence as the Dominion of Ghana: 6 March 1957'

## british-togoland: fail

Area: infobox 0 km2 (0), Cliopatria 0 km2, ratio 0.0. No Cliopatria row and no infobox area on the British Togoland page; the 79-cell region (about 20,000 km2) is about two thirds of the 'one-third' of 90,400 km2 the German Togoland page gives (under 2x; acknowledged in the author's gaps).

### Findings

- **/ledger (1916/12 and 1956/12)** (blocking): british-gold-coast books British Togoland as its dependency (vassal_start 1916/12, vassal_end 1956/12, its /ledger/11-12) but this dossier has no mirror vassal events.
  - Evidence: Reviewer brief 2.3: 'a vassal_start of X is a vassal_start in X's ledger with this state as counterpart'. British Togoland page infobox: 'Admission by the Gold Coast: 27 December 1916 - 13 December 1956'; 'British Togoland was administered as part of the adjoining territory of the Gold Coast'.
  - Fix: Add vassal_start 1916/12 and vassal_end 1956/12 with counterpart 'british-gold-coast', region the 79-cell zone, confidence 3 and 2, source the British Togoland page.
- **/ledger/0/region, /ledger/3, /ledger/6**: The found event's region, an occupation_start of the same 79 cells in the same month and a 1919 gain of the same cells book the land three ways: found draws it as the state's own land from 1914/8 while the occupation and the gain say it stays German until 1919/6.
  - Evidence: Schema: 'found: the state appears on its core'; the /ledger/0 note says the land 'is drawn as occupied (hatched) over the German state until then'. german-africa books the loss only in 1919/6.
  - Fix: Keep the occupation model but say in the found note that the core is occupied land and must render as hatched (orchestrator: confirm the compiler lets occupation_start override a found region), or start the state at the 27 December 1916 partition ('effectively formed in 1916').
- **/keyframe_review/0/correction**: The territory is the Ghana part of Cliopatria's 1914 Togoland (79 cells, about 20,000 km2) while the ghana dossier takes British Togoland as the Volta Region (101 cells) in 1957.
  - Evidence: ghana /ledger/1: gain 1957/3 from british-togoland, region admin1 Volta. German Togoland page: British share 'one-third' (tagged failed verification), i.e. about 30,000 km2 of 90,400. The author flagged it in gaps.
  - Fix: Agree one region with the ghana dossier's group (af-08) once a page or map of the 1916/1919 line is found; until then keep the flag.

### Gaps for a gap-filler

- /keyframe_review/0: The Anglo-French line of 27 December 1916 / the 1919 Milner-Simon line and the zone's area (try https://en.wikipedia.org/wiki/Togoland_campaign)

### Spot checks

- /ledger/0: confirmed (https://en.wikipedia.org/wiki/British_Togoland): infobox 'Occupation: 27 August 1914'
- /ledger/2: confirmed (https://en.wikipedia.org/wiki/German_Togoland): 'The colony surrendered on 26 August 1914'
- /ledger/4: confirmed (https://en.wikipedia.org/wiki/British_Togoland): infobox 'Partitioning: 27 December 1916'
- /ledger/7: confirmed (https://en.wikipedia.org/wiki/British_Togoland): infobox 'League of Nations mandate: 20 July 1922 - 20 April 1946'
- /ledger/8: confirmed (https://en.wikipedia.org/wiki/British_Togoland): infobox 'U.N. Trust Territory: 13 December 1946 - 6 March 1957'
- /ledger/9: confirmed (https://en.wikipedia.org/wiki/British_Togoland): 'Annexed to Her Majesty's dominions to form part of the Dominion of Ghana: 6 March 1957'
- /ledger/6: confirmed (https://en.wikipedia.org/wiki/Gold_Coast_(British_colony)): 'had been linked to the Gold Coast since 1919'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| german-africa 1885 gain nobody | - | exception | GEA mainland; counterpart nobody, but the 16 km coast was Zanzibar's (pre-1963 sultanate has no dossier) |
| german-africa 1890 gain british-africa | british-africa | missing | Caprivi Strip (July 1890): british-africa has no 1890 loss to german-africa |
| german-africa 1894 gain portuguese-mozambique | portuguese-mozambique | missing | Kionga Triangle: portuguese-mozambique has no 1894 loss (its 1893/3 Cabo Delgado gain covers Kionga); route to its group |
| german-africa 1898 gain kingdom-of-rwanda | kingdom-of-rwanda 1897 dissolve | matched | both sides low confidence |
| german-africa 1900 gain kingdom-of-burundi | kingdom-of-burundi 1903 dissolve | mismatch | 3 years apart; german side confidence 1, burundi side confidence 2 (Treaty of Kiganda 1903) |
| german-africa 1911 gain french-africa | french-africa 1911 loss | matched | Neukamerun, 4 November 1911 |
| german-africa 1911 loss french-africa | french-africa | missing | the Chad 'duck's bill' ceded to France: french-africa has no 1911 gain from german-africa |
| german-africa 1914 occupation_start british-africa | british-africa | missing | Taveta (Kenya) 15 August 1914: british-africa (owner) has no occupation event |
| german-africa 1916 loss french-africa | french-africa 1919 gain | mismatch | Neukamerun: german-africa 1916 (Agadir page), french-africa occupation_start 1915 and gain 1919 |
| german-africa 1917 occupation_start portuguese-mozambique | portuguese-mozambique | missing | Lettow-Vorbeck in northern Mozambique Nov 1917-Aug 1918: no owner-side occupation in portuguese-mozambique |
| german-africa 1918 occupation_start british-africa | british-africa | missing | German column in Northern Rhodesia Aug-Nov 1918: no owner-side occupation in british-africa |
| french-africa 1914 occupation_start german-africa | german-africa | missing | Togo occupied from August 1914: no owner-side occupation in german-africa (fix /ledger 1914-1919) |
| french-africa 1915 occupation_start german-africa | german-africa | missing | Neukamerun: no owner-side occupation in german-africa |
| french-africa 1916 occupation_start german-africa | german-africa | missing | French zone of Kamerun: no owner-side occupation in german-africa |
| british-africa 1915 occupation_start german-africa | german-africa | missing | Namibia: no owner-side occupation in german-africa; south-africa books the same occupation (two siblings occupy one colony) |
| south-africa 1915 occupation_start german-africa | german-africa | missing | Namibia: no owner-side occupation in german-africa |
| british-africa 1916 occupation_start german-africa | german-africa | missing | Tanganyika minus Kigoma: no owner-side occupation in german-africa |
| belgian-congo 1916 occupation_start german-africa | german-africa | missing | Kigoma (1916) and Rwanda-Burundi (1916/5): no owner-side occupation in german-africa |
| british-togoland 1914 occupation_start german-africa | german-africa | missing | British zone of Togoland 1914/8: no owner-side occupation in german-africa (same batch) |
| german-africa 1919 loss south-africa | south-africa 1920 gain | matched | Namibia; south-africa 1920 at confidence 1; british-africa also gains Namibia 1919 (sibling double booking) |
| german-africa 1919 loss british-africa | british-africa 1922 gain | mismatch | Tanganyika: 28 June 1919 (Versailles) against the 20 July 1922 mandate; author flagged |
| german-africa 1919 loss belgian-congo | belgian-congo 1922 gain | mismatch | Rwanda-Burundi: 1919/6 against 1922/7; author flagged |
| german-africa 1919 loss portuguese-mozambique | portuguese-mozambique 1919 gain | matched | Kionga Triangle 1919/6 |
| german-africa 1919 loss british-africa | british-africa | missing | British Cameroons (Nord-Ouest, Sud-Ouest): british-africa has no gain; republic-of-cameroon takes the same land from british-gold-coast in 1961; british-cameroons has no dossier |
| german-africa 1919 loss french-africa | french-africa 1919 gain | matched | French Cameroon |
| german-africa 1919 loss british-togoland | british-togoland 1919 gain | matched | same batch |
| german-africa 1919 loss french-africa | french-africa 1922 gain | mismatch | French Togo: 1919/6 against 1922/7 |
| british-gold-coast 1850 gain danish-gold-coast | danish-gold-coast 1850 dissolve | missing | Gold Coast infobox 'Incorporation of the Danish Gold Coast: 1850'; danish-gold-coast dissolves to british-colonial-empire; no gain in british-gold-coast (fix) |
| british-gold-coast 1872 gain dutch-gold-coast | dutch-gold-coast 1872 dissolve | matched | 6 April 1872 |
| british-gold-coast 1874 vassal_start lagos-colony | lagos-colony | missing | Lagos administered by the Gold Coast 1874-1886: lagos-colony has no vassal_start/vassal_end with british-gold-coast (its notes mention it) |
| ashanti-empire 1874 loss british-gold-coast | british-gold-coast | mismatch | ashanti-empire cedes the coast and Assin south of the Pra 1874/2; british-gold-coast has only a rename (fix) |
| british-gold-coast 1896 vassal_start ashanti-empire | ashanti-empire 1896 dissolve | mismatch | protectorate in the colony, dissolve in the Asante dossier; author flagged |
| british-gold-coast 1897 gain Mamprusi, Dagarti, Wa and Bona chiefdoms | - | exception | no dossier; listed under counterparts_needing_dossiers (af-04) |
| british-gold-coast 1901 gain ashanti-empire | ashanti-empire 1896 dissolve | mismatch | gain from a state dissolved five years earlier |
| british-gold-coast 1916 vassal_start british-togoland | british-togoland | missing | same batch; british-togoland lacks vassal_start/vassal_end british-gold-coast (fix) |
| british-gold-coast 1957 dissolve  | ghana 1957 found | matched | land differs: ghana excludes admin1 Volta, this dossier the 79 Togoland cells |
| republic-of-cameroon 1961 gain british-gold-coast | british-gold-coast | mismatch | British Cameroons are not Gold Coast land (Cliopatria composite row); the counterpart should be british-cameroons (no dossier yet) |
| british-togoland 1957 loss ghana | ghana 1957 gain | matched | land differs: 79 cells against admin1 Volta (101 cells) |

## Problems

- WebFetch returns summaries; quotes above are the quotations it returned, not verbatim copies of the pages.
- Did not open the German colonization of Africa page; the german-africa area check uses the four colony infoboxes, all opened.
- No fixes applied by the reviewer: every finding is a missing event or a region/model change, outside the small-fix list; dossiers unchanged.
- Neighbours not yet written (groups not run, exception applies): kingdom-of-spain, kingdom-of-portugal, british-colonial-empire, portuguese-republic, free-french, francoist-spain, french-fifth-republic.
