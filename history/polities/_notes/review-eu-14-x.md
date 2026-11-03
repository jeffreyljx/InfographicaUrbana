# Review eu-14-x (2026-10-31)

Adversarial review of the 22 dossiers of eu-14-x (Baltic peoples, Livonian church states, Swedish and Danish Baltic provinces, Lübeck, Holstein). All 22 validate with --resolve (0 errors; bremen-verden keeps its Torstenson War span warning). 102 events were checked on the cited pages by WebFetch: none was fabricated or mis-dated. The verdicts turn on drawing and consistency.

Verdicts: old-prussians fail, duchy-of-livonia fix, swedish-livonia fix, swedish-estonia fix, swedish-ingria pass, swedish-pomerania thin, bremen-verden pass, danish-estonia pass, ancient-estonia pass, curonians pass, semigallians pass, livonians pass, tavastians pass, karelians fail, bishopric-of-dorpat pass, bishopric-of-osel-wiek fix, bishopric-of-courland thin, archbishopric-of-riga fail, riga fix, kexholm-county thin, free-imperial-city-of-lubeck fix, county-of-holstein thin.

## Fixes applied by the reviewer

- Riga: `{"admin1": "Riga", "country": "Latvia"}` resolves to the whole Riga planning region (30 municipalities, about 13,150 km2), not the city (304 km2). Replaced by `{"place": "Riga", "km": 8}` (the city) or `km 10` (Riga with Dünamünde, from 1621) in riga, swedish-livonia, duchy-of-livonia and archbishopric-of-riga.
- duchy-of-livonia: capital Fellin from 1582 (Russian-held 1560-1582, outside the 1561-1581 shape); Livonian War belligerent denmark-norway.
- swedish-estonia: counterpart denmark-norway for 1583 and 1645, and in the Livonian War (kingdom-of-denmark is the row 936-1406).
- free-imperial-city-of-lubeck: counterparts of Mölln 1359 and Bergedorf 1370 and 1420 set to duchy-of-saxe-lauenburg; 1420 dated August; Count's Feud belligerent denmark-norway.
- bishopric-of-osel-wiek: capital Leal (Lihula) 1228-1250 added from the infobox.
- bishopric-of-courland: found event lowered to confidence 1, as its own note says.

Each changed dossier carries a one-line "Review eu-14-x" sentence at the end of `notes`.

## old-prussians: fail

- [BLOCKING, for the author] `/keyframe_review/4 and /ledger/9`: Keyframe 1260-1276 regains the lands lost in 1253 and 1255 (drawn area 25,796 -> 52,603 km2) but the ledger holds only a contest_start in 1260; /ledger/11 then loses in 1277 land the ledger had already lost in 1253 and 1255. Evidence: Great_Prussian_Uprising: 'The major revolt began on 20 September 1260'; 'the Knights were left only with strongholds in Balga, Elbing, Culm, Thorn, and Königsberg'. Rule 4: a change of area between keyframes needs a gain or loss. Fix: Add {year 1260, month 9, type gain, counterpart teutonic-order, region = the /ledger/9 region, source Great_Prussian_Uprising, confidence 2} after /ledger/9 (the risings retook the countryside), so the 1277 loss returns it; or keep keyframe 4 equal to keyframe 3 and drop /ledger/11.
- [for the author, not blocking] `/ledger/2, /ledger/8, /ledger/11`: The teutonic-order dossier (eu-14-f) files its 1236, 1255 and 1277 gains from nobody and dates the Christburg gain 1249 against this dossier's 1253. Evidence: teutonic-order ledger rows 1236 gain nobody, 1249 gain nobody, 1255 gain nobody, 1277 gain nobody. Fix: Route to eu-14-f: set those counterparts to old-prussians; agree 1249 or 1253 (author already flagged).
- Spot checks (6): /ledger/1 confirmed; /ledger/2 confirmed; /ledger/7 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/12 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## duchy-of-livonia: fix

- [applied] `/identity/capitals/0`: Capital Fellin (Viljandi) from 1561 lay outside the 1561-1581 keyframe (Vidzeme and Pärnu) and in Russian hands. Evidence: Duchy_of_Livonia infobox: Capital Fellin; livonian-conference /ledger/7 (Viljandi page): Fellin taken by Kurbsky in 1560; Livonian_War: Jam Zapolski (1582) returned Russian-held Livonia and Dorpat. Fellin cell outside keyframe 0, inside keyframe 1. Fix: Capital from 1582 (done).
- [applied] `/keyframe_review/2-4, /ledger/4, /ledger/10, /ledger/14`: Riga drawn as {admin1: Riga, country: Latvia}, which is the whole Riga planning region (about 13,150 km2), not the city. Evidence: gazetteer: admin1 Riga resolves to the 30 municipalities of the Riga planning region (about 13,151 km2); the Riga infobox gives the city 304 km2. Fix: Replaced by {place: Riga, km: 8} for the 1581 gain of the city and {place: Riga, km: 10} (Riga with Dünamünde) from 1621 (done).
- [applied] `/wars/0/belligerents`: kingdom-of-denmark is the Cliopatria row 936-1406; the Livonian War Dane is denmark-norway. Evidence: polities.csv: kingdom-of-denmark 936..1406, denmark-norway 1526..1940. Fix: Replaced (done).
- [for the author, not blocking] `/ledger/0`: The archbishopric-of-riga dossier (this batch) files its 1561 loss and dissolve to duchy-of-livonia; this dossier's found event names livonian-conference and no gain from the archbishopric. Evidence: archbishopric-of-riga /ledger/4, /ledger/6. Fix: Either name the archbishopric in a 1561 gain here or set the archbishopric's counterpart to livonian-conference; one side, consistently.
- [for the author, not blocking] `/ledger/4`: Gain of Riga from riga in 1581, but the riga dossier (this batch) files that loss to polish-lithuanian-commonwealth. Evidence: riga /ledger/1-2 counterpart polish-lithuanian-commonwealth. Fix: Set riga /ledger/1-2 counterpart to duchy-of-livonia (the Commonwealth's Livonian province holds the land in this project), or the reverse.
- [thin] `/keyframe_review/0`: Pernau: the Livonian War page has "Eric XIV's seizure of Pernau in June 1562", yet Pärnu county stays in the 1561-1581 shape; also the Russian conquests of 1572-1577 are not modelled. Page to try: https://en.wikipedia.org/wiki/P%C3%A4rnu
- Spot checks (6): /ledger/0 confirmed; /ledger/5 confirmed; /ledger/7 confirmed; /ledger/10 confirmed; /ledger/13 confirmed; /ledger/14 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## swedish-livonia: fix

- [applied] `/keyframe_review/0-2, /ledger/1, /ledger/5, /ledger/9-10, /wars/0`: The 1621 conquest of Riga and Dünamünde was drawn as the whole Riga planning region (13,151 km2) instead of the city. Evidence: gazetteer: admin1 Riga resolves to the 30 municipalities of the Riga planning region (about 13,151 km2); the Riga infobox gives the city 304 km2. Fix: Replaced by {place: Riga, km: 10} (done); keyframe 0 is now 759 km2.
- [thin] `/ledger/13`: Ösel 1710 at confidence 1 (Arensburg capitulated in September 1710). Page to try: https://en.wikipedia.org/wiki/Capitulation_of_Estonia_and_Livonia
- Spot checks (8): /ledger/0 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/7 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/11 confirmed; /ledger/12 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## swedish-estonia: fix

- [applied] `/ledger/4, /ledger/7, /wars/0`: Counterpart kingdom-of-denmark (Cliopatria row 936-1406) for events of 1583 and 1645 and the Livonian War. Evidence: polities.csv: kingdom-of-denmark 936..1406; denmark-norway 1526..1940. Fix: Replaced by denmark-norway (done).
- [thin] `/ledger/7`: Wiek (Läänemaa) gained from Denmark in 1645 at confidence 1: Brömsebro ceded Ösel only (Swedish_Estonia: 'the island of Saaremaa (Ösel) was ceded by Denmark'); mainland Wiek was probably Swedish from 1581 (Hapsal). Page to try: https://en.wikipedia.org/wiki/Haapsalu_Castle
- [thin] `/ledger/4`: Dagö (Hiiumaa) from Denmark in 1583 at confidence 1; the page says only that Dagö was Swedish by 1583. Page to try: https://en.wikipedia.org/wiki/Hiiumaa
- [thin] `/ledger/1`: Jerwen 1562 at confidence 1 ('somewhat later' than June 1561). Page to try: https://en.wikipedia.org/wiki/Swedish_Estonia
- [thin] `/keyframe_review/4`: Narva fell to Russia in 1704 (Siege of Narva); the shape keeps Ida-Viru to 1710. Page to try: https://en.wikipedia.org/wiki/Siege_of_Narva_(1704)
- Spot checks (6): /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/8 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## swedish-ingria: pass

- [thin] `/ledger/3`: Nöteborg 1702 at confidence 1; the Great Northern War page puts Nöteborg with Erastfer 'in 1703'. Page to try: https://en.wikipedia.org/wiki/Siege_of_N%C3%B6teborg
- [thin] `/keyframe_review/2`: Jamburg and Koporye (1703) and Ivangorod (1704) are kept to 1708. Page to try: https://en.wikipedia.org/wiki/Siege_of_Narva_(1704)
- [thin] `/ledger/1`: Ingria was lost de facto in 1590 (kingdom-of-sweden dossier: February 1590) and ceded in 1595; the author flagged it. Page to try: https://en.wikipedia.org/wiki/Russo-Swedish_War_(1590%E2%80%931595)
- Spot checks (5): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## swedish-pomerania: thin

- [thin] `/wars/1`: Scanian War: Brandenburg took Wolgast, Stettin (1677) and Stralsund and Rügen (1678) and held Swedish Pomerania to 1679; only Wismar's Danish occupation is in the ledger. Page to try: https://en.wikipedia.org/wiki/Scanian_War
- [thin] `/keyframe_review/4`: Great Northern War: Stettin was sequestrated to Prussia in 1713 (Treaty of Schwedt) before the 1720 cession. Page to try: https://en.wikipedia.org/wiki/Great_Northern_War
- [thin] `/ledger/9`: Wismar back to Sweden in 1679 at confidence 1 (bridging). Page to try: https://en.wikipedia.org/wiki/Wismar
- Spot checks (10): /ledger/0 confirmed; /ledger/4 confirmed (October 1637 is the imperial army's entry; Brandenburg's enfeoffment is November 1637); /ledger/5 confirmed; /ledger/8 confirmed; /ledger/11 confirmed; /ledger/13 confirmed; /ledger/14 confirmed; /ledger/15 confirmed; /ledger/16 confirmed; /ledger/19 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## bremen-verden: pass

- [thin] `/wars/0`: Swedish de facto rule began in the Torstenson War ('the Swedes seized de facto rule in both prince-bishoprics'; Brömsebro 13 August 1645); the dossier starts 1648 and the war lies outside its life (the validator warning). An occupation from 1645 would close it. Page to try: https://en.wikipedia.org/wiki/Bremen-Verden
- Spot checks (5): /ledger/0 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/7 confirmed; /ledger/9 confirmed.
- Area: Bremen 5,325.4 km2 (1803) + Verden 1,359.7 km2 (1806) from the page; drawn 8,852 km2.

## danish-estonia: pass

- [for the author, not blocking] `/identity/capitals/0`: Capital Reval 1219-1343 spans 1227-1237, when the dossier holds no land (all lost to the Brothers in 1227, regained 1238). Evidence: Danish_Estonia: 'In 1227, the Livonian Brothers of the Sword conquered all Danish territories in northern Estonia.' Fix: Optional: split the capital 1219-1226 and 1238-1343.
- [thin] `/ledger/1`: Harria, Vironia and Jerwia 1220 at confidence 1 (page undated). Page to try: https://en.wikipedia.org/wiki/Danish_Estonia
- Spot checks (6): /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed (the page: 'and the castle at Narva in 1345'; the note's quote is a paraphrase); /ledger/7 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## ancient-estonia: pass

- [thin] `/ledger/4`: Northern Estonia to Denmark 1220 at confidence 1. Page to try: https://en.wikipedia.org/wiki/Livonian_Crusade
- Spot checks (5): /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/6 confirmed; /ledger/7 confirmed.
- Area: No Cliopatria row or infobox area; the Estonia region (57,661 km2 in cells) against modern Estonia 45,339 km2 is grid inflation, ratio 1.27.

## curonians: pass

- Spot checks (4): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## semigallians: pass

- [thin] `/ledger/3`: Order contest 1236 at confidence 1. Page to try: https://en.wikipedia.org/wiki/Semigallians
- [thin] `/ledger/4`: 1254 partial subjugation at confidence 1 (the page: 'partly subdued'). Page to try: https://en.wikipedia.org/wiki/Semigallians
- [thin] `/ledger/5`: Occupation 1254-1279 at confidence 1. Page to try: https://en.wikipedia.org/wiki/Semigallians
- Spot checks (4): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/6 confirmed; /ledger/9 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## livonians: pass

- [thin] `/ledger/4`: Idumeja and Metsepole 1208 at confidence 1. Page to try: https://en.wikipedia.org/wiki/Livonians
- [thin] `/ledger/5`: Contest end 1208 at confidence 1. Page to try: https://en.wikipedia.org/wiki/Livonian_Crusade
- Spot checks (4): /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## tavastians: pass

- Spot checks (2): /ledger/0 confirmed; /ledger/1 confirmed (traditional 1249-1250; the page also gives 1238-1239, so confidence 2 is right).
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## karelians: fail

- [BLOCKING, for the author] `/keyframe_review/0/correction`: The shape (255,176 km2, to 37.9E and 66.7N) draws the whole Republic of Karelia and Finnish North Karelia for 1143-1322; the page places the Karelians mainly on the Ladoga shore and the Isthmus and dates White Karelia to the late 14th century. Evidence: Karelians page (WebFetch): the densest settlement 'along the western shore of Lake Ladoga and the Karelian Isthmus', a smaller continuous presence in South Karelia, 'very little evidence from North Karelia in the early period'; Russian Karelians 'established control over White Karelia by the late 14th century'. {region: Karelia} resolves to admin1 Karelia (Russia), 241,520 km2. Fix: Redraw as the Karelian Isthmus and Ladoga Karelia circles plus South Karelia (drop {region: Karelia} and North Karelia, or keep them only as a later, low-confidence band); carry the same land in /ledger/0 and /ledger/5-7.
- [for the author, not blocking] `/ledger/2`: 1293 is only a contest_start, but Sweden took the western Isthmus round Vyborg that year. Evidence: Karelians page: 'the foundation of castles, in 1293 at Vyborg'; kingdom-of-sweden /ledger: 1293 gain of the western Karelian Isthmus round Vyborg (from novgorod-republic). Fix: Add a 1293 loss to kingdom-of-sweden of the Vyborg circle, and route the counterpart name to eu-14-e.
- Spot checks (4): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/5 confirmed; /ledger/6 confirmed.
- Area: No infobox area; the drawn 255,176 km2 contradicts the page's settlement description (see fixes).

## bishopric-of-dorpat: pass

- Spot checks (3): /ledger/0 confirmed; /ledger/2 confirmed (main text: Dorpat in May; a footnote swaps to July; author flagged); /ledger/3 confirmed for the year; the page gives no month (May comes from the Livonian War page).
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## bishopric-of-osel-wiek: fix

- [applied] `/identity/capitals`: Capitals began in 1251, leaving 1228-1250 without the seat the infobox lists first. Evidence: Bishopric of Ösel–Wiek infobox: 'Capitals: Leal (Lihula) Perona (Vana-Pärnu) Hapsal (Haapsalu) Arensburg (Kuressaare)'; 'Perona (Vana-Pärnu) from 1251'. Fix: Added Leal (Lihula) 23.845E 58.681N, 1228-1250 (done).
- [for the author, not blocking] `/identity/capitals/1`: Perona (Vana-Pärnu, 24.51E 58.37N) lies outside the drawn shape (bbox to 24.39E). Evidence: gazetteer cell test: outside keyframe 0. Fix: Extend the Pärnu polygon to the left bank at Vana-Pärnu, or note it.
- Spot checks (4): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/5 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## bishopric-of-courland: thin

- [applied] `/ledger/0/confidence`: Found event at confidence 2 while its own note says the land is drawn at confidence 1. Evidence: Bishopric_of_Courland: 'In 1253 the territory of Courland was divided between the Bishopric of Courland and the Livonian branch'; nothing on land before 1253. Fix: Lowered to 1 (done).
- [for the author, not blocking] `/ledger/0 and /ledger/1`: The same Ventspils area is gained twice (found 1234, gain 1253 from teutonic-order); 1234-1252 it overlaps land the curonians lost in 1230 to the Brothers. Evidence: Bishopric_of_Courland (1253 division); curonians /ledger/1; livonian-brothers-of-the-sword 1230 gain of Courland. Fix: Start keyframe 0 at 1253 (found with a token Piltene circle), or drop the 1253 gain; one land event only.
- [thin] `/keyframe_review/0`: The three enclaves (Pilten, Hasenpoth, Neuhausen) and Runö: page silent on boundaries. Page to try: https://en.wikipedia.org/wiki/Bishopric_of_Courland
- Spot checks (3): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed.
- Area: Terra Mariana and Bishopric of Courland pages: 4,500 km2; drawn 3,035 km2 (Ventspils), acknowledged as a stand-in.

## archbishopric-of-riga: fail

- [BLOCKING, for the author] `/ledger (1201) and /keyframe_review/0`: The livonians dossier (this batch) loses the Riga area to the archbishopric in 1201, but this dossier has no 1201 gain and its 1186-1206 shape is Ikšķile only, so its capital Riga (from 1202) lies outside its own shape and the land is drawn by nobody 1201-1206. Evidence: livonians /ledger/2 (1201 loss, Riga~35km, counterpart archbishopric-of-riga); Archbishopric_of_Riga: 'after its seat was moved to Riga, it became the Bishopric of Riga in 1202'. Fix: Add the 1201 gain of the Riga circle from livonians (source Livonians) and a keyframe from 1201.
- [BLOCKING, for the author] `/keyframe_review/1/correction`: The 18,000 km2 stand-in disc round 24.5E 56.9N reaches 56.2N and covers 8,096 km2 of the semigallians shape (this batch), which stays free to 1290: the land is drawn twice for 1207-1290. Evidence: gazetteer overlap of archbishopric keyframe 1 with semigallians keyframe 0: 32 cells; semigallians notes keep Semigallia free to 1254/1290. Fix: Move the disc north-east of the Daugava (the archbishop's lands round Turaida, Kokenhusen, Lemsal, Ronneburg), e.g. centre near 25.1E 57.25N, or subtract Semigallia until 1290.
- [for the author, not blocking] `/ledger/2`: 1207 gain from livonians, but livonians files its 1206 and 1208 losses to livonian-brothers-of-the-sword; no 1207 loss. Evidence: livonians /ledger/3-4. Fix: Pick one: the archbishop's two-thirds from livonians in their ledger, or this gain's counterpart livonian-brothers-of-the-sword.
- [applied] `/identity/successors, /ledger/4-5`: The city of Riga was drawn as the whole Riga planning region (13,151 km2) in the minus and in the 1561 loss to riga. Evidence: gazetteer: admin1 Riga resolves to the 30 municipalities of the Riga planning region (about 13,151 km2); the Riga infobox gives the city 304 km2. Fix: Replaced by {place: Riga, km: 8} (done).
- [thin] `/ledger/2`: The archbishop's districts and the Riga War 1297-1330 (page failed for the author). Page to try: https://en.wikipedia.org/wiki/Riga_War
- Spot checks (5): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed (2 February 1207; confidence 1 honest); /ledger/3 confirmed; /ledger/4 confirmed.
- Area: Terra Mariana: 'Archbishopric of Riga (18,000 km2)'; drawn disc 20,485 km2.

## riga: fix

- [applied] `/keyframe_review/0/correction and every region`: The free city was drawn as {admin1: Riga, country: Latvia}: 13,151 km2 against the page's 304 km2, a factor of 43, unacknowledged (the note believed it was the municipality). Evidence: gazetteer: admin1 Riga resolves to the 30 municipalities of the Riga planning region (about 13,151 km2); the Riga infobox gives the city 304 km2. Fix: Replaced by {place: Riga, km: 8} (253 km2) everywhere (done).
- [for the author, not blocking] `/ledger/1-2`: Loss to polish-lithuanian-commonwealth, while duchy-of-livonia (this batch) files the gain from riga. Evidence: duchy-of-livonia /ledger/4. Fix: Set the counterpart to duchy-of-livonia (or change the duchy side).
- Spot checks (2): /ledger/0 confirmed ('for twenty years had the status of a free imperial city'); /ledger/1 confirmed (Drohiczyn 1581; infobox Polish-Lithuanian rule from 1582).
- Area: Before the fix: 13,151 km2 (ratio 43); after: 253 km2 (ratio 0.83).

## kexholm-county: thin

- [thin] `/ledger/1`: 1721: the page says only the southern part was ceded and the remainder became Kymmenegård and Nyslott County; the whole polygon is carried as lost (confidence 2, flagged). Page to try: https://en.wikipedia.org/wiki/Kexholm_County
- [thin] `/keyframe_review/0`: The Russian capture of Kexholm in 1710 (page silent). Page to try: https://en.wikipedia.org/wiki/Siege_of_Kexholm
- Spot checks (2): /ledger/0 confirmed; /ledger/1 confirmed for the year; the page cedes only the southern part.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## free-imperial-city-of-lubeck: fix

- [applied] `/ledger/1-3/counterpart`: Counterparts were free text ('a debt-strapped Saxon duke', 'the lord of Bergedorf', 'Eric V') where a dossier exists. Evidence: Free_City_of_Lübeck: 'bought the ducal Herrschaft of Mölln from the indebted Albert V, Duke of Saxe-Bergedorf-Mölln'; Bergedorf pledged by Duke Eric III; 'Eric V to agree to the Peace of Perleberg on 23 August 1420'. duchy-of-saxe-lauenburg files the 1420 loss. Fix: Set to duchy-of-saxe-lauenburg; /ledger/3 month 8 (done).
- [applied] `/wars/1/belligerents`: Count's Feud (1534-1536) belligerent kingdom-of-denmark (row ends 1406). Evidence: polities.csv. Fix: denmark-norway (done).
- [for the author, not blocking] `/ledger/3`: Bergedorf is gained twice (1370 pledge, 1420 cession) and from 1420 was a condominium with Hamburg. Evidence: Free_City_of_Lübeck: the cities ran the lands jointly with alternating bailiffs. Fix: Make 1370 the land event and 1420 a note, or 1370 an occupation_start; mention the condominium.
- Spot checks (4): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.
- Area: No Cliopatria row; the page gives no area. cliopatria_km2 holds the dossier's own largest drawn keyframe (gazetteer cells x 253 km2).

## county-of-holstein: thin

- [for the author, not blocking] `/keyframe_review/0/correction`: The Holstein region includes the Lübeck circle, so the county and free-imperial-city-of-lubeck (this batch) draw the same 759-1,012 km2 from 1226. Evidence: gazetteer overlap: 3-4 cells. Fix: Subtract the Lübeck circle from 1226 (a second keyframe).
- [for the author, not blocking] `/identity`: 1474 is a change of title (Count to Duke of Holstein, same land), which the rules treat as a rename, not a new state. Evidence: Holstein: Frederick III 'elevated Christian I as Count of Holstein-Rendsburg to Duke of Holstein'. Fix: Orchestrator: decide whether the county dossier continues as the duchy (rename 1474) rather than asking for a new duchy-of-holstein 1474-1848.
- [thin] `/keyframe_review/0`: Wagria (east Holstein) was Wagrian until 1138-1143; the shape holds it from 1111. Also Dithmarschen and the partitions (Holstein-Rendsburg, -Plön, -Kiel). Page to try: https://en.wikipedia.org/wiki/Holstein
- Spot checks (4): /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.
- Area: Holstein page: 'It had an area of 8,385 km2'; drawn 10,875 km2, ratio 1.30.

## Cross-dossier matrix

Mismatches and missing mirrors (exceptions, with no dossier on the other side, and matched pairs are in the JSON report):

- old-prussians 1236 loss teutonic-order -> mismatch: teutonic-order 1236 gain; mirror names 'nobody' (eu-14-f)
- old-prussians 1253 loss teutonic-order -> missing: no mirror in teutonic-order (eu-14-f); teutonic-order dates the Christburg gain 1249 (counterpart nobody); author flagged 1249 vs 1253.
- old-prussians 1253 loss teutonic-order -> missing: no mirror in teutonic-order (eu-14-f); teutonic-order dates the Christburg gain 1249 (counterpart nobody); author flagged 1249 vs 1253.
- old-prussians 1255 loss teutonic-order -> mismatch: teutonic-order 1255 gain; mirror names 'nobody' (eu-14-f)
- old-prussians 1277 loss teutonic-order -> mismatch: teutonic-order 1277 gain; mirror names 'nobody' (eu-14-f)
- old-prussians 1283 loss teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- old-prussians 1283 dissolve teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- duchy-of-livonia 1561 found livonian-conference -> mismatch: livonian-conference 1560 loss; mirror names 'tsardom-of-russia' (eu-14-f); livonian-conference (eu-14-f) files its 1561 loss of Livonia to house-of-jagiellon.
- duchy-of-livonia 1581 gain riga -> mismatch: riga 1581 loss; mirror names 'polish-lithuanian-commonwealth' (this batch); riga (this batch) files the loss to polish-lithuanian-commonwealth.
- swedish-livonia 1645 gain denmark-norway -> mismatch: denmark-norway 1645 loss; mirror names 'swedish-empire' (eu-14-g)
- swedish-estonia 1561 found livonian-conference -> mismatch: livonian-conference 1560 loss; mirror names 'tsardom-of-russia' (eu-14-f); livonian-conference (eu-14-f) files the 1561 loss to kingdom-of-sweden and includes Järva and Ida-Viru in 1561 (this dossier: Järva 1562, Narva 1581).
- swedish-estonia 1562 gain livonian-conference -> mismatch: livonian-conference 1561 loss; mirror names 'kingdom-of-sweden' (eu-14-f)
- swedish-estonia 1583 gain denmark-norway -> missing: no mirror in denmark-norway (eu-14-g)
- swedish-estonia 1645 gain denmark-norway -> mismatch: denmark-norway 1645 loss; mirror names 'swedish-empire' (eu-14-g)
- swedish-pomerania 1630 found duchy-of-pomerania -> missing: no mirror in duchy-of-pomerania (eu-09)
- swedish-pomerania 1630 occupation_start duchy-of-pomerania -> mismatch: duchy-of-pomerania 1630 occupation_start; mirror names 'swedish-empire' (eu-09)
- swedish-pomerania 1637 occupation_end duchy-of-pomerania -> mismatch: duchy-of-pomerania 1637 occupation_end; mirror names 'swedish-empire' (eu-09)
- swedish-pomerania 1637 gain duchy-of-pomerania -> mismatch: duchy-of-pomerania 1637 dissolve; mirror names 'swedish-empire' (eu-09)
- swedish-pomerania 1648 loss brandenburg-prussia -> mismatch: brandenburg-prussia 1648 gain; mirror names 'holy-roman-empire-minor-states' (eu-09-k)
- swedish-pomerania 1675 occupation_start denmark-norway -> missing: no mirror in denmark-norway (eu-14-g)
- swedish-pomerania 1679 occupation_end denmark-norway -> missing: no mirror in denmark-norway (eu-14-g)
- swedish-pomerania 1679 occupation_start brandenburg-prussia -> missing: no mirror in brandenburg-prussia (eu-09-k)
- swedish-pomerania 1693 occupation_end brandenburg-prussia -> missing: no mirror in brandenburg-prussia (eu-09-k)
- swedish-pomerania 1715 occupation_start denmark-norway -> missing: no mirror in denmark-norway (eu-14-g)
- swedish-pomerania 1720 loss kingdom-of-prussia -> mismatch: kingdom-of-prussia 1720 gain; mirror names 'swedish-empire' (eu-09-k)
- swedish-pomerania 1721 occupation_end denmark-norway -> mismatch: denmark-norway 1720 occupation_end; mirror names 'holy-roman-empire-minor-states' (eu-14-g)
- swedish-pomerania 1815 dissolve kingdom-of-prussia -> mismatch: kingdom-of-prussia 1814 gain; mirror names 'Principality of Neuchâtel' (eu-09-k)
- bremen-verden 1648 found prince-archbishopric-of-bremen -> mismatch: prince-archbishopric-of-bremen 1648 dissolve; mirror names 'swedish-empire' (eu-08-x)
- bremen-verden 1648 gain prince-bishopric-of-verden -> mismatch: prince-bishopric-of-verden 1648 dissolve; mirror names 'kingdom-of-sweden' (eu-08-x)
- bremen-verden 1712 occupation_start denmark-norway -> mismatch: denmark-norway 1712 occupation_start; mirror names 'swedish-empire' (eu-14-g)
- bremen-verden 1715 occupation_end denmark-norway -> mismatch: denmark-norway 1715 occupation_end; mirror names 'swedish-empire' (eu-14-g)
- bremen-verden 1715 occupation_start electorate-of-hanover -> mismatch: electorate-of-hanover 1715 occupation_start; mirror names 'swedish-empire' (eu-09-l)
- bremen-verden 1719 occupation_end electorate-of-hanover -> mismatch: electorate-of-hanover 1719 occupation_end; mirror names 'swedish-empire' (eu-09-l)
- bremen-verden 1719 dissolve electorate-of-hanover -> mismatch: electorate-of-hanover 1719 gain; mirror names 'swedish-empire' (eu-09-l)
- danish-estonia 1227 loss livonian-brothers-of-the-sword -> mismatch: livonian-brothers-of-the-sword 1227 gain; mirror names 'kingdom-of-denmark' (eu-14-e)
- danish-estonia 1238 gain teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- danish-estonia 1345 loss teutonic-order -> mismatch: teutonic-order 1346 gain; mirror names 'danish-magnates' (eu-14-f)
- danish-estonia 1346 loss teutonic-order -> mismatch: teutonic-order 1346 gain; mirror names 'danish-magnates' (eu-14-f)
- danish-estonia 1346 dissolve teutonic-order -> mismatch: teutonic-order 1346 gain; mirror names 'danish-magnates' (eu-14-f)
- ancient-estonia 1224 loss livonian-brothers-of-the-sword -> mismatch: livonian-brothers-of-the-sword 1224 gain; mirror names 'Archbishopric of Riga' (eu-14-e); livonian-brothers-of-the-sword (eu-14-e) gains Sakala in 1211 and southern Estonia in 1218 from nobody, so 1211/1218-1224 is drawn twice.
- ancient-estonia 1227 loss livonian-brothers-of-the-sword -> mismatch: livonian-brothers-of-the-sword 1227 gain; mirror names 'kingdom-of-denmark' (eu-14-e)
- ancient-estonia 1227 dissolve livonian-brothers-of-the-sword -> mismatch: livonian-brothers-of-the-sword 1227 gain; mirror names 'kingdom-of-denmark' (eu-14-e)
- curonians 1230 loss livonian-brothers-of-the-sword -> mismatch: livonian-brothers-of-the-sword 1230 gain; mirror names 'nobody' (eu-14-e)
- curonians 1266 loss teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- curonians 1266 dissolve teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- semigallians 1254 occupation_start teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- semigallians 1279 occupation_end teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- semigallians 1290 loss teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- semigallians 1290 dissolve teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- livonians 1201 loss archbishopric-of-riga -> missing: no mirror in archbishopric-of-riga (this batch); archbishopric-of-riga (this batch) has no 1201 gain and draws only Ikšķile to 1206: fix on the archbishopric side (fail).
- livonians 1206 loss livonian-brothers-of-the-sword -> mismatch: livonian-brothers-of-the-sword 1206 gain; mirror names 'nobody' (eu-14-e)
- livonians 1208 loss livonian-brothers-of-the-sword -> missing: no mirror in livonian-brothers-of-the-sword (eu-14-e)
- livonians 1208 dissolve livonian-brothers-of-the-sword -> missing: no mirror in livonian-brothers-of-the-sword (eu-14-e)
- tavastians 1249 loss kingdom-of-sweden -> mismatch: kingdom-of-sweden 1250 gain; mirror names 'nobody' (eu-14-e)
- tavastians 1249 dissolve kingdom-of-sweden -> mismatch: kingdom-of-sweden 1250 gain; mirror names 'nobody' (eu-14-e)
- karelians 1323 loss kingdom-of-sweden -> mismatch: kingdom-of-sweden 1323 gain; mirror names 'novgorod-republic' (eu-14-e); kingdom-of-sweden (eu-14-e) takes the Vyborg isthmus in 1293 and Savonia's parishes in 1323 from novgorod-republic; this dossier gives the western land to Sweden only in 1323.
- karelians 1323 dissolve kingdom-of-sweden -> mismatch: kingdom-of-sweden 1323 gain; mirror names 'novgorod-republic' (eu-14-e); kingdom-of-sweden (eu-14-e) takes the Vyborg isthmus in 1293 and Savonia's parishes in 1323 from novgorod-republic; this dossier gives the western land to Sweden only in 1323.
- bishopric-of-dorpat 1224 found livonian-brothers-of-the-sword -> missing: no mirror in livonian-brothers-of-the-sword (eu-14-e)
- bishopric-of-osel-wiek 1228 found livonian-brothers-of-the-sword -> missing: no mirror in livonian-brothers-of-the-sword (eu-14-e)
- bishopric-of-osel-wiek 1559 vassal_start denmark-norway -> missing: no mirror in denmark-norway (eu-14-g); livonian-conference (eu-14-f) files the 26 September 1559 sale as its loss to denmark-norway and denmark-norway (eu-14-g) gains from livonian-conference; author flagged the double filing.
- bishopric-of-osel-wiek 1560 vassal_end denmark-norway -> missing: no mirror in denmark-norway (eu-14-g); denmark-norway (eu-14-g) gains Ösel-Wiek and Courland in 1559 from livonian-conference.
- bishopric-of-osel-wiek 1560 loss denmark-norway -> mismatch: denmark-norway 1559 gain; mirror names 'livonian-conference' (eu-14-g); denmark-norway (eu-14-g) gains Ösel-Wiek and Courland in 1559 from livonian-conference.
- bishopric-of-osel-wiek 1560 dissolve denmark-norway -> mismatch: denmark-norway 1559 gain; mirror names 'livonian-conference' (eu-14-g); denmark-norway (eu-14-g) gains Ösel-Wiek and Courland in 1559 from livonian-conference.
- bishopric-of-courland 1253 gain teutonic-order -> missing: no mirror in teutonic-order (eu-14-f)
- bishopric-of-courland 1560 loss denmark-norway -> mismatch: denmark-norway 1559 gain; mirror names 'livonian-conference' (eu-14-g); denmark-norway (eu-14-g) gains in 1559 from livonian-conference; the page has 1559 (lead) and 20 May 1560 (timeline).
- bishopric-of-courland 1560 dissolve denmark-norway -> mismatch: denmark-norway 1559 gain; mirror names 'livonian-conference' (eu-14-g); denmark-norway (eu-14-g) gains in 1559 from livonian-conference; the page has 1559 (lead) and 20 May 1560 (timeline).
- archbishopric-of-riga 1207 gain livonians -> mismatch: livonians 1206 loss; mirror names 'livonian-brothers-of-the-sword' (this batch); livonians (this batch) files 1206/1208 losses to the Brothers; the 1207 disc also covers 8,096 km2 of semigallians, free to 1290.
- archbishopric-of-riga 1561 loss duchy-of-livonia -> mismatch: duchy-of-livonia 1561 found; mirror names 'livonian-conference' (this batch); duchy-of-livonia (this batch) founds from livonian-conference; one side should name the other.
- archbishopric-of-riga 1561 dissolve duchy-of-livonia -> mismatch: duchy-of-livonia 1561 found; mirror names 'livonian-conference' (this batch); duchy-of-livonia (this batch) founds from livonian-conference; one side should name the other.
- free-imperial-city-of-lubeck 1226 found holy-roman-empire -> missing: no mirror in holy-roman-empire (eu-08-b)
- free-imperial-city-of-lubeck 1359 gain duchy-of-saxe-lauenburg -> missing: no mirror in duchy-of-saxe-lauenburg (eu-09)
- free-imperial-city-of-lubeck 1370 gain duchy-of-saxe-lauenburg -> missing: no mirror in duchy-of-saxe-lauenburg (eu-09)
- free-imperial-city-of-lubeck 1420 gain duchy-of-saxe-lauenburg -> mismatch: duchy-of-saxe-lauenburg 1420 loss; mirror names 'free-city-of-lubeck' (eu-09)
- swedish-ingria 1595 loss tsardom-of-russia -> mismatch: kingdom-of-sweden 1590 loss; kingdom-of-sweden (eu-14-e) files the Ingria loss in February 1590.

## Problems

- Gazetteer trap: {admin1: Riga, country: Latvia} resolves to all 30 municipalities of the Riga planning region (about 13,150 km2), because each carries 'Riga' as an alternate name. Four dossiers drew the city of Riga that way (riga at 43 times the city's 304 km2); fixed here to {place: Riga, km: 8|10}. No other dossier in polities/ uses it now; the gazetteer should drop that alternate name.
- Gazetteer: {region: Livonia} includes the Riga planning region's municipalities south and west of the Daugava (Tukums, Jūrmala, Engure, Kandava, Jaunpils, Babīte, Mārupe, Olaine, Baldone, Ķekava), which were Courland and Semigallia; swedish-livonia (1629-1709) and duchy-of-livonia (1582-1628) therefore draw part of Courland. Not fixed (a gazetteer change).
- Counterpart naming across groups: the neighbours written earlier file these events under nobody, swedish-empire, kingdom-of-sweden, kingdom-of-denmark, danish-magnates, livonian-conference, house-of-jagiellon or holy-roman-empire-minor-states, not under this batch's new slugs; 44 mismatches and 29 missing mirrors in cross_checks, routed to eu-14-e (Brothers, Sweden), eu-14-f (Teutonic Order, Livonian Conference), eu-14-g (Denmark-Norway), eu-09 (Pomerania, Brandenburg-Prussia, Prussia, Hanover, Saxe-Lauenburg), eu-08-x (Bremen, Verden), eu-08-b (Holy Roman Empire).
- Counterparts without dossiers (exceptions): tsardom-of-russia and novgorod-republic (eu-16), polish-lithuanian-commonwealth (eu-15), kingdom-of-denmark (eu-14, row 936-1406, not written), russian-empire (eu-17), duchy-of-mecklenburg, first-french-empire, free-city-of-lubeck, duchy-of-holstein (eu-20).
- The section-6 Context list of the author's brief names western and central European states (Angevin Empire, Angles, Brythons ...), not this batch's Baltic neighbours; the neighbour ledgers actually read were the counterparts named in the dossiers.
- WebFetch returns summaries; quotes in this report are the wording WebFetch returned.
