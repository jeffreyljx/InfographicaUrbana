# Review of batch eu-18-x (2026-11-01)

Adversarial review of the thirteen new-state dossiers of eu-18-x (Balkans and Ottoman Europe additions). Mechanical check: the validator passes all thirteen (two warnings: pashalik-of-berat and muzaka-despotate-of-berat have no dossier yet, both listed by the author). Overlaps between neighbouring keyframes were measured with the gazetteer on the r5 cell grid. Pages opened for spot checks: Kara Mahmud Bushati, Mustafa Pasha Bushati, Pashalik of Scutari, Pashalik of Yanina, Ali Pasha of Ioannina, Parga, Military Frontier, Prince-Bishopric of Montenegro, Bay of Kotor, Venetian Dalmatia, Morean War, Pashalik of Belgrade, Banat of Temeswar, Eastern Rumelia, Kingdom of Serbia (1718-1739), Kingdom of Albania (medieval), Principality of Albania (medieval), Bosnia Eyalet, Herzegovina Eyalet. No spot-checked event was fabricated; the failures are shapes that contradict the cited page or overlap a neighbour in this batch, and mirror events missing between dossiers of this batch.

Small fixes applied by the reviewer (validated, read back): see each dossier's list, items marked APPLIED. Each edited note ends with '[reviewer eu-18-x, 2026-11-01]'.

| slug | verdict |
| --- | --- |
| pashalik-of-scutari | fail |
| pashalik-of-yanina | fail |
| habsburg-military-frontier | fail |
| prince-bishopric-of-montenegro | fail |
| venetian-dalmatia | fail |
| pashalik-of-belgrade | thin |
| eastern-rumelia | fail |
| bosnia-eyalet | fail |
| herzegovina-eyalet | fail |
| kingdom-of-albania | fail |
| principality-of-albania-thopia | thin |
| banat-of-temeswar | fix |
| kingdom-of-serbia-1718-1739 | pass |

## pashalik-of-scutari: fail

Findings:

- TO DO `/ledger (missing, 1796)`: No 1796 loss to prince-bishopric-of-montenegro mirrors that dossier's 1796/9 gain of the Bjelopavlici and Piperi, and KF2-KF4 keep drawing Podgorica municipality, which overlaps Montenegro's KF1/KF3 (3 cells) for 1796-1831. Evidence: prince-bishopric-of-montenegro /ledger/4: 1796/9 gain, counterpart pashalik-of-scutari, region U[Danilovgrad, (19.1,42.65)/25]; Prince-Bishopric infobox: 'Unification of (old) Montenegro and the Hills (1796)'. Kara Mahmud page: he was killed at Krusi, 22 September 1796. Fix: Add {year 1796, month 9, type loss, counterpart prince-bishopric-of-montenegro, region the same union as Montenegro's ledger/4, source Kara_Mahmud_Bushati, confidence 2} and subtract that union from the corrections of KF2, KF3 and KF4 (split KF2 at 1796).
- TO DO `/keyframe_review/2/correction`: Bar and Podgorica enter the shape in 1795 with no ledger event (L5 names only Kosovo, L6 only Diber/Debar/Tetovo). Evidence: KF1 1780-1794 = Shkoder, Lezhe, Kukes, Ulcinj, Durres, Tirane; KF2 1795 adds Bar and Podgorica; the KF2 note cites only the Pashalik page's undated 'including southern Montenegro'. Fix: Either add Bar and Podgorica to the found region (they were in the Sanjak of Scutari) or add a dated gain for them; if neither page dates it, record it at confidence 1 and say so.
- TO DO `/ledger/9`: 1820 gain of Berat from pashalik-of-yanina has no mirror: Yanina records no loss and its KF10 keeps Berat to 1822 (5 cells drawn by both states 1820-1822). Evidence: Mustafa Pasha Bushati page: 'In 1820, the sanjak of Berat was appropriated to him.' pashalik-of-yanina /keyframe_review/10 (1812-1822) still contains Berat. Fix: Fix on the Yanina side (see its finding); keep this event.
- APPLIED `/ledger/2`: Month 6 and confidence 3 not supported: the page dates the tax-farming quarrel to June 1780 and says only that Mahmud 'eventually took possession of Durres'. Evidence: Kara_Mahmud_Bushati: 'In June 1780, Mahmud and Ahmet Kurt Pasha were again in conflict over the control of the tax-farming of Durres ... Mahmud eventually took possession of Durres.' Fix: Month removed, confidence 2 (done by reviewer).
- TO DO `/ledger/13/region and /identity/successors/0/land`: Dissolve region and successor land omit Ulcinj, Bar, Podgorica, Debar, Tetovo, Berat, Elbasan and Ohrid, all inside KF4 (1824-1831). Evidence: KF4 correction is the 15-member union; ledger/13 has 7 members. Fix: Use the KF4 union (minus the 1796 Montenegrin land) for both.

Gaps for a gap-filler:

- `/ledger/4 and /ledger/8`: Venetian tribute (harac) to Kara Mahmud: start and end undated on both pages; recording it as vassalage of Kotor is a stretch. (try https://en.wikipedia.org/wiki/Albania_Veneta)
- `/ledger/6`: date of the Diber/Debar/Tetovo march (confidence 1) (try https://en.wikipedia.org/wiki/Kara_Mahmud_Bushati)
- `/keyframe_review/4`: southeastern Serbia and 'most of Montenegro' of the peak extent are undated (try https://en.wikipedia.org/wiki/Bushati_family)

Spot checks: /ledger/2 mis-dated (month): fixed; /ledger/5 confirmed; /ledger/7 confirmed; /ledger/10 confirmed; /ledger/12 confirmed.
Area: No infobox area and no Cliopatria row; KF4 resolves to about 28,100 km2 (111 cells), as the author says.

## pashalik-of-yanina: fail

Findings:

- TO DO `/keyframe_review/10 and /ledger (missing, 1820)`: Berat stays in the shape to 1822 though pashalik-of-scutari gains it from this pashalik in 1820; no 1820 loss. Evidence: Mustafa Pasha Bushati page: 'In 1820, the sanjak of Berat was appropriated to him'; Ali Pasha page: Ali was 'declared a rebel in 1820'. pashalik-of-scutari /ledger/9 names pashalik-of-yanina as counterpart; both keyframes hold Berat 1820-1822 (5 cells). Fix: Add {year 1820, type loss, counterpart pashalik-of-scutari, region {admin1 Berat}, source Mustafa_Pasha_Bushati (add to sources), confidence 2}; split KF10 at 1820 with Berat removed from 1820.
- APPLIED `/ledger/15/region`: Parga drawn as a 60 km circle round Ioannina, land held since 1787. Evidence: Pashalik of Yanina: 'the British sold the city of Parga to Ali Pasha' (1819); Parga page: 39.283 N, 20.400 E. Fix: Region set to {lon 20.40, lat 39.28, km 10} with the original text (done by reviewer).

Gaps for a gap-filler:

- `/ledger (1808)`: Attica, 'occupied by force' after Selim III's death in 1808 (Ali page), left out for want of an end date; record the gain at confidence 2 and its end at confidence 1 or explain in a keyframe note. (try https://en.wikipedia.org/wiki/Ali_Pasha_of_Ioannina)
- `/keyframe_review/10`: Korce (Gorice) in the peak list is undated (try https://en.wikipedia.org/wiki/Ali_Pasha_of_Ioannina)

Spot checks: /ledger/4 confirmed; /ledger/7 confirmed; /ledger/10 confirmed; /ledger/13 confirmed; /ledger/15 confirmed (region fixed); /ledger/17 confirmed.
Area: 75,000 km2 is a footnote figure for the undated peak; the 1812-1822 keyframe resolves to 207 cells; no Cliopatria row, so the keyframe area stands in.

## habsburg-military-frontier: fail

Findings:

- TO DO `/keyframe_review/5 to /keyframe_review/11 (corrections)`: The Tisza, Danube and Mures river strips (34 cells) are kept from 1751 to 1872 although the page ends those sections in 1751; no 1751 loss records it, and the strips overlap the banat-of-temeswar shape by 20-22 cells. Evidence: Military Frontier page table: 'Danube Military Frontier 1702-1751' ('one part of its territory was placed under civil administration'), 'Tisa Military Frontier 1702-1751' ('most of its territory was placed under civil administration'), 'Mures Military Frontier 1702-1751' ('its entire territory was placed under civil administration'). The author's own KF1 text says '(1702-1751)'. Fix: Add a 1751 loss (counterpart habsburg-monarchy, the civil administration; or banat-of-temeswar for the Banat side) of the Mures strip, the Tisza strip and the civil part of the Danube strip, and remove them from KF5-KF11; keep only the Sajkaska circle from 1763.
- TO DO `/keyframe_review/1/correction`: The river strips appear from 1699 though the sections were formed in 1702 (ledger/3). Evidence: Military Frontier page: sections '1702-1751'. Fix: Split KF1 at 1702 or drop the strips from 1699-1701.
- TO DO `/ledger/15/region`: The 1873 loss omits Sajkaska, which KF12 drops in the same year. Evidence: Military Frontier page: the Sajkas battalion 'was abolished in 1873, and its territory was incorporated into Backa-Bodrog County'. Fix: Add {lon 20.25, lat 45.2, km 30} (and the remaining Danube/Tisza strip) to the 1873 loss or add a separate 1873 loss.
- TO DO `/ledger/1`: A 'gain' of exactly the region already held since 1553: the page describes a change of authority, not of land. Evidence: Military Frontier page: 'In 1627, the Military Frontier was removed from the control of the Croatian Sabor.' Fix: Delete the event or keep the fact in a keyframe note; no land moves in 1627.
- TO DO `/ledger/2/region`: The Slavonian counties (Brodsko-Posavska, Vukovarsko-Srijemska, Osjecko-Baranjska) enter KF1 in 1699 but no event names them. Evidence: ledger/2 region = Lika-Senj, Karlovac, Sisak-Moslavina only. Fix: Add the Slavonian counties to the 1699 gain (Bosnia Eyalet page: 'losing all the Slavonian sanjaks').
- APPLIED `/ledger/7/counterpart`: Counterpart was the string 'Banat of Temeswar' though the dossier banat-of-temeswar exists. Evidence: banat-of-temeswar /ledger/2: 1751 loss to habsburg-military-frontier. Fix: Set to banat-of-temeswar (done by reviewer).
- APPLIED `/ledger/2, /ledger/4, /ledger/5 counterpart`: Counterpart was ottoman-empire for land the Bosnia Eyalet dossier (same batch) loses to and regains from this dossier. Evidence: Bosnia Eyalet page: lost 'the sanjak of Lika' and the Slavonian sanjaks in 1699; Military Frontier page: 'From 1718 to 1739 the Military Frontier also included the Habsburg-controlled northern parts' of Bosnia. Fix: Set to bosnia-eyalet, mirrored in bosnia-eyalet /ledger/1, 4, 5 (done by reviewer).
- APPLIED `/ledger/3/counterpart`: 1702 'gain from ottoman-empire' of land the Ottomans had ceded to the Habsburgs at Karlowitz three years earlier. Evidence: ottoman-empire /ledger/124: 26 January 1699 loss to habsburg-monarchy of Hungary, Slavonia and Transylvania; Military Frontier page: sections formed 1702. Fix: Set to habsburg-monarchy (done by reviewer).
- APPLIED `/ledger/14/month`: Month missing. Evidence: Military Frontier page: '(Krizevci and Durdevac regiments) was already incorporated into Croatia-Slavonia on 1 August 1871'. Fix: Month 8 added (done by reviewer).

Gaps for a gap-filler:

- `/keyframe_review/0`: 16th-17th century extent and its growth (1553-1698 one shape) (try https://en.wikipedia.org/wiki/Croatian_Military_Frontier)
- `/ledger/12`: return of eastern Syrmia after the Serbian Vojvodina (confidence 1) (try https://en.wikipedia.org/wiki/Serbian_Vojvodina)
- `/wars`: Great Turkish War, Austro-Turkish wars of 1716-1718 and 1737-1739 (the Frontier's 1699, 1718 and 1739 moves) (try https://en.wikipedia.org/wiki/Austro-Turkish_War_(1737%E2%80%931739))

Spot checks: /ledger/1 confirmed date; not a land change; /ledger/4 confirmed; /ledger/14 confirmed (month added); /ledger/15 confirmed; /ledger/16 confirmed.
Area: No infobox area on the main page; KF10 (1851-1870) resolves to 164 cells (about 41,500 km2), of which the river strips the page ends in 1751 are about 34 cells.

## prince-bishopric-of-montenegro: fail

Findings:

- TO DO `/keyframe_review/0, /keyframe_review/1, /keyframe_review/3 (corrections), /ledger/0/region`: The 30 km circle round Cetinje takes in the Bay of Kotor and Budva coast (3 of its 7 cells), land the venetian-dalmatia dossier holds 1420-1797 and Austria from 1815; Montenegro held that coast only in 1813-1814 (KF2). Evidence: Overlap computed with the gazetteer: KF0 x venetian-dalmatia KF1 = 3 cells. Bay of Kotor page: 'in 1813, a union of the bay area with Montenegro was declared'; 'In 1815, the bay was annexed by the Austrian Empire'. Fix: Use {minus: [{lon 18.92, lat 42.39, km 30}, {union: [Kotor, Tivat, Budva, Herceg Novi admin1]}]} in KF0, KF1, KF3 and the found region.
- TO DO `/ledger/4`: Gain from pashalik-of-scutari with no mirror loss in that dossier. Evidence: pashalik-of-scutari ledger has only contest_end in 1796. Fix: Keep; the loss is to be added on the Scutari side (see its finding).

Gaps for a gap-filler:

- `/keyframe_review/3`: Moracani, Rovcani, Kuci and the rest of the Hills joining (the 1853 Cliopatria shape is 6,131 km2 against about 2,800 here, acknowledged) (try https://en.wikipedia.org/wiki/Petar_II_Petrovi%C4%87-Njego%C5%A1)
- `/identity/rulers`: ruler strip omitted; Petar I (1784-1830) and Petar II (1830-1851) reigns (try https://en.wikipedia.org/wiki/Petar_II_Petrovi%C4%87-Njego%C5%A1)

Spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/4 confirmed (infobox 'Unification of (old) Montenegro and the Hills (1796)'); /ledger/8 confirmed; /ledger/9 confirmed; /ledger/10 confirmed.
Area: No infobox area; the successor's 1853 Cliopatria shape (6,131 km2) is 2.2 times KF3 (about 2,780 km2), acknowledged in KF3 and the notes.

## venetian-dalmatia: fail

Findings:

- TO DO `/keyframe_review/8 and /keyframe_review/9 (corrections)`: After 1699 the circles round Vrgorac, Imotski and the Neretva (18.0 E, 43.05 N, 45 km) reach 19 cells (about 4,800 km2) into today's Bosnia and Herzegovina, which bosnia-eyalet draws in the same years. Evidence: Overlap computed with the gazetteer: KF9 x bosnia-eyalet KF3 = 19 cells of 69. Morean War page: in the final peace Venice 'did relinquish the areas of Popovo polje as well as Klek and Sutorina'; Venetian Dalmatia page: Venice lost 'Citluk and Gabela' in 1718 (the Linea Mocenigo); the author's own KF5 note says Knin 'helped set the Dalmatia-Bosnia border that exists today'. Fix: From 1699 intersect the hinterland circles with {country Croatia} (plus the Kotor-Herceg Novi admin1 in Montenegro), and make the 1699 and 1718 losses the land so removed.
- TO DO `/ledger/6/region`: The region (15.0 E, 44.5 N, 40 km) does not contain Krk or Cres named in its text, and no keyframe draws the islands, so the loss has no trace. Evidence: Venetian Dalmatia page: 'made some significant gains, including the capture of the islands of Krk, Pag and Cres' and Novigrad 'surrendered on 4 July'. Fix: Name the places (Novigrad, Pag; Krk and Cres as the page says, flagged) and draw the Venetian islands (Krk, Cres, Rab, Pag, Brac, Hvar, Korcula) in KF0-KF9, or drop the event if the islands are not drawn.
- TO DO `/ledger/8, /ledger/10 to /ledger/14 counterpart`: The hinterland gains of 1669 and 1686-1694 name ottoman-empire while bosnia-eyalet (same batch) records them as one 1699 loss to this dossier. Evidence: Bosnia Eyalet page: the eyalet held the sanjaks of Klis and Krka and lost 'big parts of the Dalmatian coast' in the war; bosnia-eyalet /ledger/2 (1699/1, counterpart venetian-dalmatia). Fix: Name bosnia-eyalet as counterpart of these gains; the Bosnia side moves its losses to 1669 and 1686-1694 (see its finding).

Gaps for a gap-filler:

- `/ledger (1647)`: Klis taken in 1647 and the 1646-1669 places gained (the 1669 'tripled' gain is drawn as a ring of circles) (try https://en.wikipedia.org/wiki/Cretan_War_(1645%E2%80%931669))
- `/ledger (1570-1573)`: Cyprus War changes in Dalmatia and the 1573 limit near Budva (not on the page) (try https://en.wikipedia.org/wiki/Albania_Veneta)

Spot checks: /ledger/6 confirmed text; region does not match; /ledger/10 confirmed; /ledger/12 confirmed; /ledger/13 confirmed; /ledger/14 confirmed; /ledger/17 confirmed.
Area: No infobox area; KF9 (1718-1796) resolves to 69 cells (about 17,450 km2), 19 of them in Bosnia and Herzegovina.

## pashalik-of-belgrade: thin

Gaps for a gap-filler:

- `/keyframe_review/3 and /ledger/4-8`: The insurgents' hold: the serbs dossier has the whole pashalik gained in December 1806, lost in October 1813 and gained again in April 1815 (serbs /ledger/2, 4, 6), while this dossier keeps the land to 1817 under contest; add the losses and gains (counterpart serbs) or explain why the contest blend is meant. (try https://en.wikipedia.org/wiki/First_Serbian_Uprising)
- `/ledger/6`: start of the Second Serbian Uprising (confidence 1; serbs dossier: Takovo, 23 April 1815) (try https://en.wikipedia.org/wiki/Second_Serbian_Uprising)

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/7 confirmed.
Area: No infobox area; KF0 resolves to 92 cells (about 23,300 km2).

## eastern-rumelia: fail

Findings:

- TO DO `/ledger (missing vassal_start 1878/7 and vassal_end 1885/9)`: The province is drawn as fully sovereign; the page makes it an autonomous Ottoman province, and the ottoman-empire dossier records vassal_start (1878/7) and vassal_end (1885) for it. Evidence: Eastern Rumelia page: an autonomous province of the Ottoman Empire under Ottoman political and military jurisdiction, created by the Treaty of Berlin (13 July 1878); ottoman-empire /ledger/193 and /ledger/202 (counterpart 'Eastern Rumelia'); principality-of-bulgaria carries its own vassal_start of 1878/7. Fix: Add {1878/7 vassal_start, counterpart ottoman-empire, the seven provinces, source Eastern_Rumelia, confidence 3} and {1885/9 vassal_end, counterpart ottoman-empire}; the Ottoman side should then use the slug eastern-rumelia.
- TO DO `/wars/0`: The Serbo-Bulgarian War (14 November 1885 to March 1886) falls wholly after the province ended (September 1885). Evidence: principality-of-bulgaria /ledger/3-4; identity.end 1885/9. Fix: Drop the war here (it is Bulgaria's) or mention it in notes only.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed date (9 October 1878); 'occupation' is the author's reading; /ledger/2 confirmed; /ledger/3 confirmed.
Area: No Cliopatria row; keyframe resolves to 124 cells.

## bosnia-eyalet: fail

Findings:

- TO DO `/keyframe_review/0/correction and /ledger/0/region`: The whole Sibenik-Knin and Split-Dalmatia counties make the eyalet hold the Venetian coastal cities and islands (Sibenik, Trogir, Split, Brac, Hvar...) for 1580-1698: 11 of the 19 cells of venetian-dalmatia KF1 and 30 of the 49 cells of its KF2. Evidence: Venetian Dalmatia page: Venice held 'the coastal cities by 1420'; overlap computed with the gazetteer. The author's own KF0 note: 'The county shapes overshoot the sanjaks.' Fix: Subtract the venetian-dalmatia keyframe of the same years (or name the Klis and Krka sanjak area as inland circles) from KF0 and the found region.
- TO DO `/ledger/2`: One 1699 loss to venetian-dalmatia, while that dossier gains the hinterland in 1669 (Peace of Candia) and in 1686, 1687, 1688, 1690 and 1694; KF0 runs unchanged to 1698. Evidence: Morean War page: Sinj 30 September 1686, Herceg Novi 30 September 1687, Knin 11 September 1688, Vrgorac 26 November 1690, 'areas north of the Republic of Ragusa' 1694; Venetian Dalmatia page: 'Peace in 1669 found the Republic of Venice with significant gains in Dalmatia, its territory tripled'. Fix: Record the losses in those years with counterpart venetian-dalmatia and split KF0 accordingly; keep 1699 for Lika and Slavonia.
- TO DO `/keyframe_review/3 and /keyframe_review/5 (corrections)`: The Sanjak of Herzegovina's land outside today's Bosnia and Herzegovina (Niksic, Pljevlja-Prijepolje: 20 cells) moves in the 1833 loss and the 1851 gain but is never in Bosnia's keyframes. Evidence: Herzegovina Eyalet page: kazas Prijepolje, Pljevlja (with Kolasin), Saranci (with Drobnjak), Cajnice, Niksic ...; 'Today part of: Bosnia and Herzegovina, Montenegro, Serbia'. Fix: Add the herzegovina-eyalet region (once corrected) to KF0-KF3 and KF5, or drop the non-Bosnian parts from ledger/8 and ledger/10.
- APPLIED `/ledger/1, /ledger/4, /ledger/5 counterpart`: Counterpart habsburg-monarchy while habsburg-military-frontier (same batch) draws the land from the same year. Evidence: Military Frontier page: 'From 1718 to 1739 the Military Frontier also included the Habsburg-controlled northern parts'; Bosnia Eyalet page: lost the Lika sanjak in 1699. Fix: Set to habsburg-military-frontier (done by reviewer).

Gaps for a gap-filler:

- `/keyframe_review`: Sanjak of Novi Pazar, Vicitrina and Prizren (in the 1580 list) not drawn (try https://en.wikipedia.org/wiki/Sanjak_of_Novi_Pazar)
- `/ledger/7`: end of the Gradascevic revolt (confidence 1) (try https://en.wikipedia.org/wiki/Husein_Grada%C5%A1%C4%8Devi%C4%87)
- `/ledger (1791)`: Sistova 1791 border towns (habsburg-monarchy /ledger/107: 'two small towns on the Croatian border') (try https://en.wikipedia.org/wiki/Treaty_of_Sistova)

Spot checks: /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/8 confirmed.
Area: No Cliopatria row; KF5 resolves to 191 cells.

## herzegovina-eyalet: fail

Findings:

- TO DO `/keyframe_review/0/correction, /ledger/0/region, /ledger/1/region`: The shape leaves out six of the fourteen kazas the page lists: Nevesinje, Ljubinje, Cajnice, Saranci with Drobnjak, Kolasin and Duvno; the keyframe note quotes only five kazas. Evidence: Herzegovina Eyalet page: 'The Pashaluk of Herzegovina was formed from following kazas: Prijepolje, Pljevlja (with Kolasin), Saranci (with Drobnjak), Cajnice, Nevesinje, Niksic, Ljubinje, Trebinje, Stolac, Pocitelj, Blagaj, Mostar, Duvno, and half of Konjic south of the Neretva' (marked citation needed). Gazetteer test: points at Nevesinje, Ljubinje, Cajnice, Zabljak, Kolasin and Tomislavgrad fall outside the region. Fix: Widen the union to cover those kazas (radii on the towns, or Republika Srpska's eastern Herzegovina by name if the gazetteer has it, plus Kolasin, Zabljak and Pljevlja municipalities and Tomislavgrad), and say the list is tagged citation needed; carry the same region into bosnia-eyalet ledger/8 and ledger/10.

Gaps for a gap-filler:

- `/ledger/1`: year of Rizvanbegovic's execution (page silent; infobox 1851) (try https://en.wikipedia.org/wiki/Ali-pa%C5%A1a_Rizvanbegovi%C4%87)

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (infobox 1851).
Area: No area anywhere; the keyframe resolves to 46 cells (about 11,600 km2) and misses six named kazas.

## kingdom-of-albania: fail

Findings:

- TO DO `/ledger/5 and /keyframe_review/3`: Butrint (Sarande circle) is lost in 1281 and left out of KF3 (1281-1287), but the page keeps it Angevin to at least 1292; the event's own note says so. Evidence: Kingdom of Albania (medieval): 'Corfu and Butrint remained in Angevin hands at least up to 1292'; in 1281 the Byzantines 'besieged the Angevin bases of Vlore, Kanine, and Durres but could not capture them'. Fix: Remove Sarande from ledger/5 (and Berat, already lost in 1274: ledger/1), keep the 1281 event only for the interior if a place can be named, and add Sarande to KF3.
- TO DO `/keyframe_review/4 and /ledger/8`: KF4 (1288-1293) re-adds Sarande with no gain, and Sarande leaves after 1293 with no loss (ledger/8 names only Vlore). Evidence: KF3 = Durres, Vlore; KF4 = Vlore, Sarande; ledger has no Sarande event between 1281 and 1294. Fix: Once KF3 holds Sarande, add Sarande to the 1294 loss (confidence 2, 'at least up to 1292').
- APPLIED `/ledger/2/counterpart`: Counterpart was despotate-of-epirus for Butrint lost 'later' than Berat to the Byzantines. Evidence: Kingdom of Albania (medieval): Berat Byzantine 'since 1274', 'later on Butrint'; 'Nikephoros I's troops captured Butrint in 1278'; despotate-of-epirus /ledger/30: 1278 gain from byzantine-empire. Fix: Counterpart set to byzantine-empire and note rewritten (done by reviewer).

Gaps for a gap-filler:

- `/ledger (1376-1383)`: Louis of Evreux holds Durres 1376-1383 (infobox 'Disestablished: 1368 1376-1383'); decide whether the kingdom revives or the land is another polity's (try https://en.wikipedia.org/wiki/Navarrese_Company)

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/5 not on page (Butrint not lost in 1281); /ledger/7 confirmed; /ledger/9 confirmed.
Area: No area on the page; KF0 resolves to 21 cells.

## principality-of-albania-thopia: thin

Gaps for a gap-filler:

- `/keyframe_review/3 and /ledger (1376, 1383)`: Durres 1376-1383: the Kingdom of Albania page and the albanian-principalities dossier (ledger/1-2) have Louis of Evreux taking it in 1376 and Thopia retaking it in 1383; this dossier holds it 1368-1381 and loses it to Balsa II in 1382 (flagged in the notes as a disagreement). Reconcile with albanian-principalities, which tells the same Durres story differently. (try https://en.wikipedia.org/wiki/Karl_Thopia)
- `/keyframe_review/6`: extent 1392-1415 beyond Kruje (page silent) (try https://en.wikipedia.org/wiki/Niketa_Thopia)

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/7 confirmed.
Area: No area on the page; KF3 resolves to 36 cells (about 9,100 km2).

## banat-of-temeswar: fix

Findings:

- APPLIED `/identity/rulers/0/from and /identity/rulers/9/to`: Ruler strip ran 1716-1779, outside the life 1718-1778. Evidence: Banat of Temeswar infobox: 'Established: 12 July 1718', 'Disestablished: 6 June 1778'. Fix: Clipped to 1718 and 1778 with notes (done by reviewer).

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.
Area: No infobox area; KF0 resolves to 145 cells (about 36,700 km2). The 20-22 cell overlap with the Military Frontier's river strips is that dossier's fault.

## kingdom-of-serbia-1718-1739: pass

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed.
Area: No infobox area; keyframe resolves to 84 cells (about 21,200 km2), no overlap with the Banat strip. Tried: dates, the Banat boundary, the successor hand-over to pashalik-of-belgrade (matched); the 1716-1718 war starting before the state is its founding war, accepted.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| pashalik-of-scutari 1757 found (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-scutari 1772 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-scutari 1780 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-scutari 1795 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-scutari 1824 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-scutari 1831 dissolve (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-scutari 1785 vassal_start (republic-of-venice) | none | missing | confidence 1; republic-of-venice has no 1785 or 1796 event; tribute to a pasha is weak evidence of vassalage |
| pashalik-of-scutari 1820 gain (pashalik-of-yanina) | none | missing | Yanina keeps Berat in KF10 to 1822; fix on the Yanina side |
| prince-bishopric-of-montenegro 1796 gain (pashalik-of-scutari) | pashalik-of-scutari 1796 contest_end | missing | Scutari has only contest_end; fix on the Scutari side |
| prince-bishopric-of-montenegro 1785 contest_start (pashalik-of-scutari) | pashalik-of-scutari 1785 contest_start | matched | zones differ (Cetinje circle against Podgorica, Bar, Ulcinj) |
| pashalik-of-yanina 1787 found (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1792 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1799 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1802 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1806 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1807 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1811 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1812 loss (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1822 dissolve (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-yanina 1789 contest_start (Suliotes) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| pashalik-of-yanina 1791 gain (Sanjak of Avlona (Vlorë)) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| pashalik-of-yanina 1803 gain (Suliotes) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| pashalik-of-yanina 1809 gain (pashalik-of-berat) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| pashalik-of-yanina 1810 gain (Sanjak of Avlona (Vlorë)) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| pashalik-of-yanina 1798 gain (french-directory) | none | missing | french-directory has no 1798 loss of Butrint, Preveza, Igoumenitsa, Vonitsa; route to its group |
| pashalik-of-yanina 1819 gain (united-states-of-the-ionian-islands) | none | missing | no 1819 loss of Parga in that dossier; route to its group |
| habsburg-military-frontier 1553 found (habsburg-monarchy) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| habsburg-military-frontier 1627 gain (Kingdom of Croatia (Habsburg)) | none | exception | string counterpart; the event moves no land (see fixes) |
| habsburg-military-frontier 1699 gain (bosnia-eyalet) | bosnia-eyalet 1699 loss | matched | after reviewer counterpart fixes on both sides; Ottoman parent: ottoman-empire 1699 loss to habsburg-monarchy |
| habsburg-military-frontier 1702 gain (habsburg-monarchy) | none | exception | reviewer changed counterpart from ottoman-empire; internal Habsburg transfer |
| habsburg-military-frontier 1718 gain (bosnia-eyalet) | bosnia-eyalet 1718 loss | matched | after reviewer fixes |
| habsburg-military-frontier 1739 loss (bosnia-eyalet) | bosnia-eyalet 1739 gain | matched | after reviewer fixes |
| habsburg-military-frontier 1751 gain (banat-of-temeswar) | banat-of-temeswar 1751 loss | matched | after reviewer slug fix |
| habsburg-military-frontier 1745 loss (Kingdom of Slavonia) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1762 gain (Principality of Transylvania (Habsburg)) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1848 loss (Serbian Vojvodina) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1849 gain (Serbian Vojvodina) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1851 loss (Principality of Transylvania (Habsburg)) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1871 loss (Kingdom of Croatia-Slavonia) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1881 dissolve (Kingdom of Croatia-Slavonia) | none | exception | counterpart listed in the author's counterparts_needing_dossiers |
| habsburg-military-frontier 1763 gain (Bács-Bodrog County (Habsburg Hungary)) | none | exception | a county, not a state; habsburg-monarchy would do |
| habsburg-military-frontier 1873 loss (Kingdom of Hungary (Austria-Hungary)) | none | missing | austria-hungary exists and has no 1873 gain; use the slug austria-hungary or a Kingdom of Hungary dossier |
| prince-bishopric-of-montenegro 1516 found (ottoman-empire) | none | missing | ottoman-empire has no 1516 loss of Montenegro (route to me-10; small) |
| prince-bishopric-of-montenegro 1813 gain (first-french-empire) | first-french-empire 1814 loss | mismatch | first-french-empire loses the Illyrian Provinces to austrian-empire on 27 January 1814; the Bay of Kotor to Montenegro in 1813 is absent |
| prince-bishopric-of-montenegro 1815 loss (austrian-empire) | austrian-empire 1815 gain | mismatch | austrian-empire gains Dalmatia on 9 June 1815 from first-french-empire, not from Montenegro |
| prince-bishopric-of-montenegro 1852 dissolve (montenegro) | montenegro 1852 found | matched |  |
| venetian-dalmatia 1409 found (croatia-in-union-with-hungary) | croatia-in-union-with-hungary 1409 loss | matched | that dossier names republic-of-venice (the parent) |
| venetian-dalmatia 1420 gain (croatia-in-union-with-hungary) | none | missing | no 1420 loss there; republic-of-venice /ledger/57 has the 1420 gain from kingdom-of-hungary |
| venetian-dalmatia 1420 gain (Kotor and Budva communes) | none | exception | string counterpart; republic-of-venice /ledger/58 uses "Commune of Kotor" |
| venetian-dalmatia 1646 loss (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1669 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1686 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1687 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1688 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1690 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1694 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1699 loss (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1718 gain (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1718 loss (ottoman-empire) | none | mismatch | ottoman-empire has no Dalmatian events; republic-of-venice carries parallel events (1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac, 1699 loss); bosnia-eyalet, the Ottoman province concerned, records one 1699 loss to venetian-dalmatia |
| venetian-dalmatia 1797 dissolve (habsburg-monarchy) | habsburg-monarchy 1797 gain | matched | Habsburg side names republic-of-venice (the parent) |
| bosnia-eyalet 1699 loss (venetian-dalmatia) | none | mismatch | venetian-dalmatia gains in 1669 and 1686-1694 from ottoman-empire, not in 1699 from bosnia-eyalet |
| bosnia-eyalet 1833 loss (herzegovina-eyalet) | herzegovina-eyalet 1833 found | matched |  |
| bosnia-eyalet 1851 gain (herzegovina-eyalet) | herzegovina-eyalet 1851 dissolve | matched |  |
| bosnia-eyalet 1878 dissolve (austria-hungary) | austria-hungary 1878 occupation_start | mismatch | austria-hungary records an occupation (29 July 1878) of Ottoman land, counterpart ottoman-empire; consistent in substance, month 7 available there |
| bosnia-eyalet 1580 found (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-belgrade 1739 found (kingdom-of-serbia-1718-1739) | kingdom-of-serbia-1718-1739 1739 loss | matched |  |
| pashalik-of-belgrade 1789 loss (habsburg-monarchy) | habsburg-monarchy 1788 contest_start | mismatch | habsburg-monarchy records only a 1788-1791 contest including Belgrade; route to eu-09 |
| pashalik-of-belgrade 1791 gain (habsburg-monarchy) | habsburg-monarchy 1791 contest_end | mismatch | as above |
| pashalik-of-belgrade 1793 gain (ottoman-empire) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| pashalik-of-belgrade 1817 dissolve (serbs) | serbs 1815 gain | mismatch | serbs gains the land from ottoman-empire in December 1806 and April 1815 (lost October 1813); this dossier keeps it under contest to 1817 |
| eastern-rumelia 1878 found (ottoman-empire) | ottoman-empire 1878 vassal_start | mismatch | Ottoman side records a vassal relation (counterpart string "Eastern Rumelia"); this dossier has none |
| eastern-rumelia 1878 occupation_start (russian-empire) | none | missing | russian-empire has no 1878-1879 occupation of Eastern Rumelia; route to its group |
| eastern-rumelia 1885 merge (principality-of-bulgaria) | principality-of-bulgaria 1885 gain | matched |  |
| kingdom-of-albania 1272 found (byzantine-empire) | none | missing | byzantine-empire (context, eu-05) has no 1272 loss |
| kingdom-of-albania 1274 loss (byzantine-empire) | none | missing | no 1274 gain of Berat in byzantine-empire |
| kingdom-of-albania 1275 loss (byzantine-empire) | despotate-of-epirus 1278 gain | exception | reviewer changed counterpart from despotate-of-epirus; byzantine-empire has no event; Epirus gains Butrint from Byzantium in 1278 |
| kingdom-of-albania 1279 gain (despotate-of-epirus) | despotate-of-epirus 1279 loss | mismatch | Epirus names house-of-anjou-sicily, not kingdom-of-albania |
| kingdom-of-albania 1281 loss (byzantine-empire) | byzantine-empire 1280 gain | mismatch | Byzantine 1280 gain is from despotate-of-epirus |
| kingdom-of-albania 1288 loss (byzantine-empire) | none | missing | no 1288 gain of Durres in byzantine-empire |
| kingdom-of-albania 1294 loss (byzantine-empire) | none | missing | no 1294 gain of Kanine in byzantine-empire |
| kingdom-of-albania 1304 gain (kingdom-of-serbia) | kingdom-of-serbia 1304 loss | mismatch | Serbia names house-of-anjou-sicily |
| kingdom-of-albania 1368 loss (principality-of-albania-thopia) | principality-of-albania-thopia 1368 gain | matched |  |
| principality-of-albania-thopia 1370 gain (muzaka-despotate-of-berat) | none | exception | counterpart listed in counterparts_needing_dossiers |
| principality-of-albania-thopia 1382 loss (serbian-despots) | serbian-despots 1385 gain | mismatch | serbian-despots (Balsic Zeta) has Durres "by 1383 or 1385" from albanian-principalities, confidence 1 |
| principality-of-albania-thopia 1385 gain (serbian-despots) | serbian-despots 1385 loss | mismatch | year agrees; serbian-despots names albanian-principalities |
| principality-of-albania-thopia 1392 loss (republic-of-venice) | republic-of-venice 1392 gain | mismatch | year agrees; Venice names albanian-principalities |
| principality-of-albania-thopia 1415 dissolve (ottoman-empire) | none | missing | ottoman-empire has no 1415 Albanian event |
| banat-of-temeswar 1718 found (ottoman-empire) | ottoman-empire 1718 loss | matched | Ottoman side names habsburg-monarchy (the parent) |
| banat-of-temeswar 1739 loss (ottoman-empire) | ottoman-empire 1739 gain | matched | Ottoman side names habsburg-monarchy |
| banat-of-temeswar 1778 dissolve (habsburg-monarchy) | none | exception | internal transfer inside the parent state: the parent dossier records no event for its own sub-units (see problems) |
| kingdom-of-serbia-1718-1739 1718 found (ottoman-empire) | ottoman-empire 1718 loss | matched | Ottoman side names habsburg-monarchy |
| kingdom-of-serbia-1718-1739 1739 loss (pashalik-of-belgrade) | pashalik-of-belgrade 1739 found | matched |  |

## Problems for the orchestrator

- Design: 12 of the 13 dossiers are sub-units of states that already have dossiers (Ottoman eyalets and pashaliks of ottoman-empire, Habsburg crown lands and the Frontier of habsburg-monarchy, Venetian Dalmatia of republic-of-venice). The parent dossiers draw the same land (republic-of-venice records 1409 Zadar, 1420 Dalmatia and Kotor, 1647 Klis, 1686 Sinj, 1687 Herceg Novi, 1688 Knin, 1690 Vrgorac and the 1699 Dalmatian losses, against the author's KF0 note that the Venice row 'does not hold Dalmatia'), and never record transfers to or from their own sub-units, so every 'gain from ottoman-empire' here has no mirror. The orchestrator must decide how sub-units render (overlay on the parent or cut out of it) before these dossiers can be compiled; the cross-check matrix marks those events 'exception'.
- principality-of-albania-thopia (1359-1415) overlaps the composite albanian-principalities dossier (1375-1421), which already draws Thopia's land and tells a different Durres story (1376 loss to Louis of Durazzo, 1383 recovery); one of the two must cede the land or the renderer must treat Thopia as a part of the composite.
- ottoman-empire /ledger/193 and /ledger/202 use the string 'Eastern Rumelia' as counterpart; once eastern-rumelia adds its vassal pair, that dossier (me-10) should use the slug.
- Several Kingdom of Albania and Thopia mirrors fail only on naming: despotate-of-epirus and kingdom-of-serbia call the Angevin side house-of-anjou-sicily, serbian-despots and republic-of-venice call Thopia albanian-principalities. The orchestrator should pick one convention.
- Reviewer edits applied in place and validated: pashalik-of-scutari ledger/2; pashalik-of-yanina ledger/15; habsburg-military-frontier ledger/2, 3, 4, 5, 7, 14; bosnia-eyalet ledger/1, 4, 5; kingdom-of-albania ledger/2; banat-of-temeswar rulers/0 and rulers/9. Each edited note ends with '[reviewer eu-18-x, 2026-11-01]'.
- WebFetch returns a model summary of each page; quotations above are as the summary gave them. No page failed to load.
