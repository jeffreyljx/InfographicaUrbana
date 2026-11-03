# Review of batch af-07-x (Southern Africa, additions): adversarial reviewer's findings

Reviewed 2026-10-19 against history/briefs/reviewer-brief.md with the orchestrator's adjustments (page budget 1-2 pages per new state, 4-6 spot checks per dossier, small reviewer fixes allowed). The machine copy is history/notes/phase-b/reviews/af-07-x.json.

## How the verdicts were set

- **fail**: at least one finding the author must make and the reviewer could not apply: a keyframe that contradicts its own ledger, an in-batch overlap of roughly 10,000 km2 or more, land that appears with no event, a counterpart that does not exist in that year, or a confidence-3 claim not on the page.
- **thin**: honest, page-silent gaps (confidence-1 bridges, events a gap-filler could find); any reviewer edit is listed too.
- **fix**: the reviewer applied every finding that needed a change.
- **pass**: the reviewer could not break it.

The validator (with --resolve) passed all 27 files with no errors; its warnings are unknown gazetteer regions (listed below) and new-slug counterparts already in the author's counterparts_needing_dossiers.

| dossier | verdict | findings (applied) | thin items | spot checks |
| --- | --- | --- | --- | --- |
| kingdom-of-mapungubwe | pass | 0 (0) | 0 | 3 |
| kingdom-of-zimbabwe | thin | 0 (0) | 2 | 3 |
| kingdom-of-butua | thin | 0 (0) | 2 | 4 |
| mutapa-empire | fail | 3 (0) | 4 | 6 |
| rozvi-empire | thin | 0 (0) | 3 | 5 |
| ndebele-kingdom | fix | 1 (1) | 1 | 6 |
| gaza-empire | fail | 2 (0) | 2 | 5 |
| basutoland | fail | 1 (0) | 0 | 7 |
| portuguese-mozambique | fail | 4 (0) | 1 | 9 |
| betsimisaraka-kingdom | thin | 0 (0) | 2 | 4 |
| boina-kingdom | thin | 0 (0) | 2 | 3 |
| menabe-kingdom | fix | 2 (2) | 3 | 6 |
| transvaal-colony | pass | 0 (0) | 0 | 3 |
| orange-river-colony | pass | 0 (0) | 0 | 2 |
| pedi-empire | fail | 3 (0) | 2 | 5 |
| mpondo-kingdom | thin | 0 (0) | 2 | 3 |
| griqualand-east | fix | 2 (2) | 1 | 3 |
| griqualand-west | fail | 1 (0) | 1 | 5 |
| british-kaffraria | pass | 0 (0) | 0 | 2 |
| stellaland | thin | 0 (0) | 2 | 3 |
| british-bechuanaland | thin | 0 (0) | 1 | 2 |
| mtetwa-paramountcy | thin | 0 (0) | 1 | 3 |
| ndwandwe-kingdom | thin | 0 (0) | 2 | 3 |
| swazi-kingdom | thin | 1 (1) | 4 | 4 |
| lozi-kingdom | fail | 2 (0) | 3 | 6 |
| makololo-kingdom | pass | 0 (0) | 0 | 3 |
| xhosa-kingdom | thin | 1 (1) | 4 | 6 |

## Reviewer edits made in the dossiers

- ndebele-kingdom `/ledger/7`: Counterpart and belligerent set to 'Voortrekkers', the string the dossier already uses for 1836-1838 (listed under counterparts_needing_dossiers); notes say why.
- menabe-kingdom `/ledger/5`: Confidence lowered to 2 (rule 7).
- menabe-kingdom `/ledger/3`: Confidence lowered to 2 on both.
- griqualand-east `/ledger/1`: Re-dated to 1872, confidence 2, note rewritten; the 1874 British control is left as a thin item.
- griqualand-east `/identity/capitals`: Added 'Laager near Mount Currie (stand-in: Kokstad)' 1862-1871 with the Kokstad point, flagged APPROXIMATE.
- swazi-kingdom `/ledger/1`: Confidence lowered to 2 and both notes rewritten with the page's words.
- xhosa-kingdom `/ledger/3`: Confidence lowered to 2.

## Per dossier

### kingdom-of-mapungubwe: pass

Area: infobox 30000 km2 (year None), drawn 30172 km2, ratio 1.01; infobox area has no year; drawn as a 98 km disc; tried and failed to break dates, successor and area

Spot checks:
- `/ledger/0` on Kingdom_of_Mapungubwe: confirmed: 'Around 1220, amid a dry period, the Mapungubwe elite moved to settle the top of Mapungubwe Hill'; infobox 'Established: c. 1220'
- `/ledger/2` on Kingdom_of_Mapungubwe: confirmed: 'around 1300, Mapungubwe's population migrated elsewhere'; 'The basin was abandoned'
- `/ledger/3` on Kingdom_of_Mapungubwe: confirmed: Great Zimbabwe 'rose to become its successor'; infobox 'Mapungubwe Hill abandoned: c. 1300'

### kingdom-of-zimbabwe: thin

Area: infobox 50000 km2 (year None), drawn 49876 km2, ratio 1.0; 50,000 km2 is a body-text figure with no year; the infobox has none

Gaps for a gap-filler:
- `/ledger/1`: the end of the Great Zimbabwe state and who took its core (1450 is a bridge at confidence 1; the page gives only 'From the early 15th century' decline and 'By the 16th century' replacement) (try https://en.wikipedia.org/wiki/Great_Zimbabwe)
- `/ledger/2`: the dissolve year (confidence 1 bridge to the Butua dossier) (try https://en.wikipedia.org/wiki/Great_Zimbabwe)

Spot checks:
- `/ledger/0` on Kingdom_of_Zimbabwe: confirmed: 'By 1250 Great Zimbabwe had become an important trade centre'
- `/ledger/1` on Kingdom_of_Zimbabwe: not on page (year): the page dates no end and names Mutapa and Butua only 'By the 16th century'; honestly entered at confidence 1
- `/keyframe_review/0` on Kingdom_of_Zimbabwe: confirmed: 'Around 1300, Great Zimbabwe replaced Mapungubwe'; body area 50,000 km2

### kingdom-of-butua: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Gaps for a gap-filler:
- `/ledger/1`: the date Butua took the Great Zimbabwe core (1450 is a confidence-1 bridge; the page has only 'the rise of Khami ... precipitating its decline') (try https://en.wikipedia.org/wiki/Khami)
- `/ledger`: the Butua-Mutapa vassalage of 1520 that the author's notes mention is not typed (try https://en.wikipedia.org/wiki/Torwa_dynasty)

Spot checks:
- `/ledger/0` on Kingdom_of_Butua: confirmed: infobox 'Established: c. 1425', 'c. 1425-?: Madabhale'
- `/ledger/2` on Kingdom_of_Butua: confirmed: 'Around 1683, the kingdom was conquered by Changamire Dombo'; 'Certainly by his death in 1696, Changamire controlled all of Butua's territory'
- `/ledger/3` on Kingdom_of_Butua: confirmed: infobox 'Conquest by Rozwi Empire: c. 1683'
- `/wars/0` on Kingdom_of_Butua: confirmed: Changamire I 'ruled Mutapa from 1490-1494'; the Torwa 'warred against Mutapa until at least 1512'

### mutapa-empire: fail

Area: infobox 700000 km2 (year 1550), drawn 266000 km2, ratio 0.38; infobox '16th century: 700,000 km2' is tagged dubious by the page; K1 note acknowledges the factor and resolves it for the documented conquests

Findings:
- `/ledger/6`: The 1632 loss to portuguese-mozambique of the lower Zambezi valley (Zambezi 60 km within Zambezia and Sofala) takes away land that no Mutapa keyframe ever draws (K0-K3 are Mashonaland, Tete, Manica, Manicaland). Evidence: Mutapa_Empire: 'In 1632, a Portuguese captain led an army to subdue the Valley from Quelimane to Sena, and conquered Manyika.' The page does not say the valley was Mutapa's; the note itself calls the region 'the researcher's reading'. portuguese-mozambique /ledger/6 mirrors it as a gain from mutapa-empire. Fix: Delete this loss (and make portuguese-mozambique /ledger/6 a gain from 'nobody' or from the valley chiefdoms), or, if a page puts the valley under Mutapa, add it to K1-K3 and cite that page.
- `/keyframe_review/1`: K1 (1450-1606) draws Manica and Manicaland from 1450, but /ledger/2 gains them only in 1470; the keyframe and the ledger disagree for 20 years. Evidence: Both years are the researcher's bridges (Mutapa_Empire gives no year for Matope's or Mukombero's conquests). Fix: Split K1 at 1470 (1450-1469 without Manica and Manicaland) or move /ledger/2 to 1450 and say so in its note.
- `/identity/capitals/1`: The Chidima capital (1723-1885) is placed at Tete town (-16.17, 33.58), inside the Tete 60 km disc that K3-K5 subtract as Portuguese land, so the capital lies outside the state's own shape. Evidence: Mutapa_Empire: capitals 'moved to the region of Chidima'; 'From 1723 onwards the capital was located in the Zambezi Valley'. The note says it is the gazetteer's Tete. Fix: Use a stand-in inside K4/K5 (Tete province more than 60 km from Tete town, up-river toward Chidima), flagged APPROXIMATE.

Gaps for a gap-filler:
- `/ledger/0`: the founding year (1430 bridge, confidence 1; infobox 'Established: 15th century') (try https://en.wikipedia.org/wiki/Nyatsimba_Mutota)
- `/ledger/1`: the year of Matope's Tavara-Tonga conquest (1450 bridge, confidence 1) (try https://en.wikipedia.org/wiki/Nyanhehwe_Matope (unverified title))
- `/ledger/2`: the year of Mukombero's Uteve conquest (1470 bridge, confidence 1) (try https://en.wikipedia.org/wiki/Uteve (unverified title))
- `/ledger/9`: the end of Barue and Manyika suzerainty (1692 bridges, confidence 1) (try https://en.wikipedia.org/wiki/Kingdom_of_Barue (unverified title))

Spot checks:
- `/ledger/5` on Mutapa_Empire: confirmed: Mavhura 'signed terms of vassalage with the Portuguese Crown' (1629) including 'the return of territory around Tete that Gatsi Rusere had conquered'
- `/ledger/6` on Mutapa_Empire: year confirmed (1632) but the page does not say the valley was Mutapa land: see fix
- `/ledger/11` on Mutapa_Empire: confirmed: 1690s Rozvi 'took control of the remaining gold-producing regions'
- `/ledger/12` on Mutapa_Empire: confirmed: 'From 1723 onwards the capital was located in the Zambezi Valley'
- `/ledger/13` on Mutapa_Empire: confirmed: infobox 'Fragmentation during civil war: c. 1760'; 'Dande did split away from the state'
- `/ledger/14` on Mutapa_Empire: confirmed: 'In 1884 the Portuguese attacked Mutapa' ... 'annexing Chidima a year later'

### rozvi-empire: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Gaps for a gap-filler:
- `/ledger/4`: the end of the Rozvi suzerainty over Mutapa (1760 bridge, confidence 1) (try https://en.wikipedia.org/wiki/Mutapa_Empire)
- `/ledger/6`: who held the rest of the plateau after 1838 (confidence 1); the Rozvi remnant to 1866 ('he finally surrendered after a lengthy siege in 1866') is not drawn (try https://en.wikipedia.org/wiki/Tohwechipi (unverified title))
- `/ledger`: Manyika as a Rozvi vassal from 1695 ('From then on, Manyika was a Rozvi vassal', Rozvi_Empire) is not typed as a vassal_start (try https://en.wikipedia.org/wiki/Rozvi_Empire)

Spot checks:
- `/ledger/0` on Rozvi_Empire: confirmed: 'The Rozvi Empire (c. 1683-1866)'
- `/ledger/1` on Rozvi_Empire: confirmed: 'Dombo defeated the Portuguese and Mutapa in battle before turning south to conquer Butua c. 1683'
- `/ledger/2` on Rozvi_Empire: confirmed: 'In 1693 Dombo's forces attacked the feira ... of Dambarare'; 'In 1695 Dombo's forces invaded Manyika'
- `/ledger/3` on Mutapa_Empire: confirmed: 'the Changamire placed a Rozvi official in his zimbabwe and imposed conditions of vassalage' around 1712 (not on the Rozvi page, correctly sourced to Mutapa)
- `/ledger/5` on Rozvi_Empire: confirmed: 'conquered and subdued around 1838 by Mzilikazi's Ndebele'

### ndebele-kingdom: fix

Area: infobox None km2 (year None), drawn n/a km2, ratio None; Mthwakazi infobox 'Total' field is empty; infobox span 1840-1893 against the dossier's 1823-1894 (judgement call, stated in notes)

Findings:
- `/ledger/7` (APPLIED by reviewer): contest_start 1847 (and its pair /ledger/8, war /wars/2) named south-african-republic, whose dossier starts in January 1852. Evidence: Ndebele_Kingdom (Mthwakazi): 'campaigns defending the Limpopo line in battles against the Boer attacks of 1847-1851'; the treaty of 1852 was signed by the South African Republic's government. Fix: Counterpart and belligerent set to 'Voortrekkers', the string the dossier already uses for 1836-1838 (listed under counterparts_needing_dossiers); notes say why.

Gaps for a gap-filler:
- `/identity/capitals`: seats for 1823-1826 and 1838-1839 (Kungwini/Mosega run 1827-1837, Inyathi from 1840; Mzilikazi: Inyathi 'his first capital', undated) (try https://en.wikipedia.org/wiki/Inyathi (unverified title))

Spot checks:
- `/ledger/0` on Mzilikazi: confirmed: 'In 1823 Mzilikazi left Nguniland during the Mfecane with a large kraal of Shaka's cattle'
- `/ledger/1` on Mzilikazi: confirmed: 'in 1826 he moved west into the Transvaal'
- `/ledger/4` on Mzilikazi: confirmed: 'By early 1838, Mzilikazi and his people were forced northwards and out of Transvaal altogether'
- `/ledger/7` on Ndebele_Kingdom: confirmed (years): 'Boer attacks of 1847-1851'; 1852 treaty signed by the SAR government (counterpart corrected)
- `/ledger/9` on First_Matabele_War: confirmed: infobox 'October 1893 - January 1894'; columns combined 16 October 1893; Bulawayo reached 3 November
- `/ledger/10` on First_Matabele_War: confirmed: 'Lobengula died from smallpox on January 22 or 23, 1894'

### gaza-empire: fail

Area: infobox 56000 km2 (year 1824), drawn 67000 km2, ratio 1.2; 56,000 km2 is the 'initial stages' figure of the Ngungunyane page (no infobox area on the Gaza page); K0 note compares it with Gaza province

Findings:
- `/keyframe_review/1/correction`: K1 (1837-1895) draws the whole of Gaza, Inhambane, Maputo, Sofala and Manica provinces on top of portuguese-mozambique K5-K7 in this batch: the Sofala, Sena, Inhambane (1727) and Maputo (1545, 1781) posts and the Zambezi 60 km strip in Sofala province (1632), about 25,000 km2 drawn twice for 58 years; neither dossier says so. Evidence: Gaza_Empire: 'Soshangane's army overran these Portuguese settlements during the time of the Gaza Empire' (no date, no later status); 'In 1727, they founded a trading post at Inhambane'; 'in 1781 they permanently occupied Delagoa Bay'. portuguese-mozambique keeps the posts and the valley throughout 1632-1894. Fix: Decide who holds the posts and the south bank of the Zambezi: subtract them from K1 (minus the PM discs and the Zambezi strip), or keep them in Gaza and enter dated losses in portuguese-mozambique, or enter contest_start/contest_end with portuguese-mozambique over them; say which in both dossiers.
- `/ledger/1`: The 1830 gain of Inhambane and Maputo provinces falls inside K0 (1824-1836), whose shape is Gaza province only; K1 adds them only from 1837. Evidence: Gaza_Empire gives no year for the subjugation; the only 1830 on the page is 'from 1830 onwards, groups of Tsonga speakers moved southwards' (not Soshangane's conquest). Both the 1830 event and the 1837 keyframe boundary are bridges. Fix: Either split K0 at 1830 or move /ledger/1 to 1837 (and keep confidence 1), so that ledger and keyframes agree.

Gaps for a gap-filler:
- `/ledger/1`: the year Soshangane subjugated the Tsonga and Chopi coast (confidence 1) (try https://en.wikipedia.org/wiki/Soshangane)
- `/identity/capitals`: the seat 1824-1827 (the infobox list starts with Chaimite 1828) (try https://en.wikipedia.org/wiki/Soshangane)

Spot checks:
- `/ledger/0` on Gaza_Empire: confirmed: infobox 'Established: 1824'
- `/ledger/1` on Gaza_Empire: not on page (year): no year for Soshangane's subjugation; honest at confidence 1
- `/ledger/2` on Gaza_Empire: confirmed: Nxaba 'in 1837 ... was defeated by Soshangane'
- `/ledger/3` on Ngungunyane: confirmed: imprisoned 'in the fortified village of Chaimite' on 28 December 1895
- `/keyframe_review/1` on Gaza_Empire: confirmed: 'at its height in the 1860s, covered all of Mozambique between the Zambezi and Limpopo rivers'; 'Soshangane extended his control over the area between the Komati (Incomati) and the Zambezi rivers'

### basutoland: fail

Area: infobox 30355 km2 (year None), drawn 28072 km2, ratio 0.92; drawn as Lesotho (gazetteer figure quoted by the author)

Findings:
- `/keyframe_review/1`: K1 (1869-1966) keeps drawing Lesotho through 1871-1883, although /ledger/9 loses the whole of it to british-cape-colony in 1871 and /ledger/12 regains it in February 1884; british-cape-colony (af-07-b) draws it as gained 1871-11 and lost 1884-02, so Lesotho is drawn by two states for 13 years. The K1 note ('Applies through the Cape annexation') chooses this deliberately but the ledger contradicts it. Evidence: Basutoland: 'Basutoland was annexed to the Cape Colony by Act No. 12 of 1871'; 'By an Order in Council dated 2 February 1884, which came into force on 18 March 1884'; infobox 'Established: 18 March 1884'. Fix: End K1 in 1870 and add a keyframe basutoland_1884 (1884-1966, Lesotho), leaving 1871-1883 to the Cape; or, if Basutoland should stay drawn as a distinct territory, replace the 1871 loss and 1884 gain with a vassal relation and have the Cape dossier match. The 1880-1881 Gun War contest stays either way.

Spot checks:
- `/ledger/1` on Free_State%E2%80%93Basotho_Wars: confirmed: 'Boshoff declaring war on the Basotho on 19 March 1858'
- `/ledger/2` on Free_State%E2%80%93Basotho_Wars: confirmed: 'On 1 June an armistice was agreed upon and signed' (free-orange-state uses 15 October 1858, a treaty this page does not mention)
- `/ledger/4` on Free_State%E2%80%93Basotho_Wars: confirmed: 'the peace of Thaba Bosiu on 11 April 1866'
- `/ledger/6` on Basutoland: confirmed: 'On 12 March 1868, a proclamation declared the Basotho to be British subjects'
- `/ledger/8` on Free_State%E2%80%93Basotho_Wars: confirmed: February 1869 Convention of Aliwal North 'gave the Conquered Territory to the Orange Free State'
- `/ledger/9` on Basutoland: confirmed: 'annexed to the Cape Colony by Act No. 12 of 1871'
- `/ledger/13` on Basutoland: confirmed: 'independence from the United Kingdom on 4 October 1966'

### portuguese-mozambique: fail

Area: infobox 801590 km2 (year 1970), drawn 801590 km2, ratio 1.0; body-text figure for the early 1970s; the infobox has none

Findings:
- `/keyframe_review/8`: K8 (1895-1975) draws all of Mozambique, but the ledger explains only Tete (1885) and the five Gaza provinces (1895); Niassa, Cabo Delgado, Nampula and most of Zambezia, roughly 350,000 km2 or nearly half the colony, appear in 1895 with no event. The K8 note admits 'the pages do not date the effective occupation of the north'. Evidence: Portuguese_Mozambique: 'Northern Mozambique was the last part of the territory to be incorporated by the Portuguese'; the Niassa Company held 'the lands of the modern provinces of Cabo Delgado and Niassa' (concession ended 1929); the author's own Niassa Company and Anglo-Portuguese Treaty of 1891 sources date the charter (1893) and the treaty boundary (11 June 1891). Fix: Add gain events for the northern interior (counterpart 'nobody' or the Yao and Makua chiefdoms as strings) dated by the 1891 treaty or the 1893 Niassa charter at confidence 2, and start the matching keyframe there; keep K8 for the whole colony from the last of them.
- `/ledger/16`: The 1897 contest_start and its pair /ledger/17 (1902) and war /wars/2 name mutapa-empire, whose dossier dissolves in 1885. Evidence: Mutapa_Empire: 'From 1897, the coalition attacked Portuguese centres in the Zambezi Valley up to Tete'; 'in 1902 Chioko was killed while assisting the Barue against the Portuguese'. Fix: Name the coalition as a string (e.g. 'Chioko's Mutapa-Barue coalition') in both events and the war, or have mutapa-empire extended to 1902 as a remnant; the author's notes flag the clash but leave it.
- `/ledger/6`: The 1632 gain from mutapa-empire (Zambezi valley in Zambezia and Sofala) mirrors a Mutapa loss of land that Mutapa never draws. Evidence: Mutapa_Empire: 'a Portuguese captain led an army to subdue the Valley from Quelimane to Sena' (no Mutapa ownership stated). Fix: Counterpart 'nobody' or the valley chiefdoms, together with the mutapa-empire fix.
- `/keyframe_review/5`: K5-K7 (1727-1894) keep the Sofala, Sena, Inhambane and Maputo posts and the Zambezi strip that gaza-empire K1 (1837-1895) also draws (see gaza-empire). Evidence: Gaza_Empire: 'Soshangane's army overran these Portuguese settlements'. Fix: Settle with gaza-empire which dossier holds them; enter losses or contest events here if Gaza does.

Gaps for a gap-filler:
- `/ledger/2`: Sena and Tete as 1530 posts rest on 'By the 1530s' (confidence 2) (try https://en.wikipedia.org/wiki/Sena,_Mozambique (unverified title))

Spot checks:
- `/ledger/0` on Portuguese_Mozambique: confirmed: '1505-1569: Captaincy of Sofala'
- `/ledger/5` on Mutapa_Empire: confirmed: 1629 terms with 'the return of territory around Tete'
- `/ledger/7` on Mutapa_Empire: confirmed: 'refused to acknowledge their suzerainty in 1678'
- `/ledger/8` on Gaza_Empire: confirmed: 'In 1727, they founded a trading post at Inhambane'
- `/ledger/10` on Gaza_Empire: confirmed: 'in 1781 they permanently occupied Delagoa Bay'
- `/ledger/11` on Gaza_Empire: confirmed: infobox 'Portuguese protectorate (1882-1895)'
- `/ledger/13` on Portuguese_Mozambique: confirmed: '1891-1893: State of Eastern Africa'
- `/ledger/18` on Portuguese_Mozambique: confirmed: 'on 28 June 1919, the Treaty of Versailles transferred the Kionga Triangle'
- `/ledger/20` on Portuguese_Mozambique: confirmed: 'independent from Portugal on 25 June 1975'

### betsimisaraka-kingdom: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Gaps for a gap-filler:
- `/ledger/0`: the extent in 1710-1711: the found region already includes Analanjirofo, which /ledger/1 gains only with Fenerive in 1712 (two years, inside one keyframe; the page itself is inconsistent about 1710) (try https://en.wikipedia.org/wiki/Ratsimilaho)
- `/ledger/4`: an end date for the kingdom (the page gives none; 1817 is the Merina conquest of Toamasina) (try https://en.wikipedia.org/wiki/Ratsimilaho)

Spot checks:
- `/ledger/0` on Betsimisaraka_people: confirmed (with the page's own inconsistency): 'emerged to unite these clans under his rule in 1710'
- `/ledger/1` on Betsimisaraka_people: confirmed: 'He captured Fenerive in 1712'
- `/ledger/2` on Betsimisaraka_people: confirmed: 'In 1817, Merina king Radama I led an army of 25,000 soldiers from Antananarivo to successfully capture Toamasina'
- `/ledger/3` on Betsimisaraka_people: confirmed (undated): 'Merina garrisons established at ports and across the Betsimisaraka interior'; honest at confidence 2

### boina-kingdom: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Gaps for a gap-filler:
- `/ledger`: the Boina infobox's '1820-1832: Tributary state of Imerina' and 'Occupied by Imerina: 1832' are on the page the author opened but are not typed (an occupation_start 1832 / occupation_end 1840 with merina-kingdom, and the tributary relation in the Merina dossier) (try https://en.wikipedia.org/wiki/Boina_Kingdom)
- `/identity/capitals/0`: the seat after the fall of Mahajanga in 1824 (the stand-in stays at Mahajanga, inside the disc lost in 1824) (try https://en.wikipedia.org/wiki/Boina_Kingdom)

Spot checks:
- `/ledger/0` on Boina_Kingdom: confirmed: 'The kingdom was founded c. 1690 by King Andriamandisoarivo'
- `/ledger/1` on Sakalava_people: confirmed: 'Deposed 1824 by Radama I after the fall of Mahajanga'
- `/ledger/2` on Boina_Kingdom: confirmed: infobox 'Annexed by Imerina: 1840'; 'The last ruler of this kingdom was Queen Tsiomeko' (Sakalava_people says the Merina 'were never to annex' Boina: noted by the author)

### menabe-kingdom: fix

Area: infobox None km2 (year None), drawn n/a km2, ratio None; the Menabe page is the modern region article; no area for the kingdom

Findings:
- `/ledger/5` (APPLIED by reviewer): Confidence 3 on the 1834 loss of a 100 km disc round Morondava, a region the page does not name (the note calls it the researcher's reading of 'southern Menabe territories'). Evidence: Menabe: 'the Merina conquered and subjugated the southern Menabe territories in 1834'. Fix: Confidence lowered to 2 (rule 7).
- `/ledger/3` (APPLIED by reviewer): Confidence 3 on the 1820 and 1822 contest events (/ledger/3, /ledger/4) whose zone is the same researcher's disc round Morondava. Evidence: Menabe: 'three ravaging campaigns in the kingdom of Menabe in 1820, in 1821 and finally in 1822' (no district named). Fix: Confidence lowered to 2 on both.

Gaps for a gap-filler:
- `/ledger/7`: Menabe after 1846 under Merina governors ('Menabe rulers were allowed to keep their authority but under the local Merina governor'): a vassal relation in the Merina dossier, not typed anywhere (try https://en.wikipedia.org/wiki/Menabe)
- `/identity/capitals/0`: the seat after 1834 (Andakabe/Morondava lies inside the disc lost in 1834) (try https://en.wikipedia.org/wiki/Menabe)
- `/ledger/2`: the 1690 split takes away Sofia and Betsiboka, which Menabe's K1 never drew (only Boeny); the Boina shape is wider than the land Menabe loses (try https://en.wikipedia.org/wiki/Sakalava_people)

Spot checks:
- `/ledger/0` on Menabe: confirmed: 'founded by Adriamandazoala (reigned c. 1540 - 1560)'
- `/ledger/1` on Sakalava_people: confirmed: 'After 1610, his descendant Andriandahifotsy ... extended his authority northwards past the Mangoky River'; sons 'further up to the Tsongay region'
- `/ledger/3` on Menabe: confirmed (years; region lowered to confidence 2): campaigns 'in 1820, in 1821 and finally in 1822'
- `/ledger/5` on Menabe: confirmed (year; region lowered to confidence 2): 'southern Menabe territories in 1834'
- `/ledger/8` on Menabe: confirmed: 'On August 14, 1897 and August 30, 1897 the 100 Menabe chiefs ... met the French troops'
- `/ledger/9` on Menabe: confirmed: 'the Menabe was not pacified until the year 1900'

### transvaal-colony: pass

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page; tried overlap with colony-of-natal 1903 (mirrored) and the SAR occupation (not double-counted)

Spot checks:
- `/ledger/0` on Transvaal_Colony: confirmed: infobox 'Treaty of Vereeniging: 31 May 1902' (the 1 September 1900 proclamation is left to the SAR occupation events, stated in notes)
- `/ledger/1` on Colony_of_Natal: confirmed: 'the territories were formally transferred to Natal in January 1903' (Vryheid, Utrecht, part of Wakkerstroom)
- `/ledger/2` on Transvaal_Colony: confirmed: infobox 'Union of South Africa: 31 May 1910'

### orange-river-colony: pass

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Spot checks:
- `/ledger/0` on Orange_River_Colony: confirmed: 'Established: 31 May 1902'; annexation 'declared' on 6 October 1900 (left to the free-orange-state occupation, stated in notes)
- `/ledger/1` on Orange_River_Colony: confirmed: 'Incorporation in the Union of South Africa: 31 May 1910'

### pedi-empire: fail

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Findings:
- `/keyframe_review/0/correction`: The K0 box (27.0-31.8E, 24.0-27.0S, 1780-1819) takes in the northern half of eSwatini (about 11,000 km2 north of 27.0S and west of 31.8E), which swazi-kingdom K0 (1744-1838, this batch) draws as Swazi; /ledger/0 and /ledger/1 use the same box. Evidence: Pedi_people: Thulare's land 'stretched from present-day Rustenburg to the lowveld ... and as far south as the Vaal River'; none of those names lies in eSwatini, and the box's 31.8E and 27.0S edges are the researcher's. Fix: Subtract {"country": "eSwatini"} from the box in K0, /ledger/0 and /ledger/1 (or pull the south-east corner back to the lowveld north of eSwatini).
- `/identity/capitals/0`: The stand-in seat Polokwane (-23.89, 29.45) lies outside both Pedi shapes: north of the K0 box's 24.0S edge and north of Sekhukhuneland (24.2-25.2S by the author's own gazetteer hint). Evidence: Pedi_people names no capital; the note marks the point APPROXIMATE. Fix: Use a stand-in inside Sekhukhuneland (e.g. a gazetteer place between the Olifants and the Steelpoort), flagged APPROXIMATE.
- `/ledger/1`: The 1820 loss names ndwandwe-kingdom, which has no matching gain and itself dissolves in 1820 with all its land to zululand, so the Pedi land lost in 1820 goes to a state that no longer exists. Evidence: Pedi_people: 'Pedi power was undermined during the Mfecane by Ndwandwe invaders from the south-east' (no year); Ndwandwe: Zwide's groups went north after 1820 (no years). Fix: Counterpart 'nobody' (the land emptied by the raids) or a string for the Ndwandwe remnant, keeping confidence 1.

Gaps for a gap-filler:
- `/ledger/1`: the date and extent of the Mfecane losses (confidence 1 bridge) (try https://en.wikipedia.org/wiki/Sekwati)
- `/ledger`: extent 1820-1876 (Sekwati's re-stabilised state) is drawn as Sekhukhuneland only; page silent (try https://en.wikipedia.org/wiki/Sekhukhune)

Spot checks:
- `/ledger/0` on Pedi_people: confirmed: 'led by supreme leaders from the Maroteng clan'; Thulare's land 'from present-day Rustenburg to the lowveld ... as far south as the Vaal River'
- `/ledger/2` on Pedi_people: confirmed: 'the Transvaal declared war in May 1876'
- `/ledger/3` on Pedi_people: confirmed: 'the British annexing the Transvaal in April 1877'
- `/ledger/5` on Pedi_people: confirmed: Wolseley 'defeated him in 1879'
- `/ledger/6` on Pedi_people: confirmed: 'In 1882, Sekhukhune was assassinated by conspirators, leading to the dismantling of the monarchy and statehood'

### mpondo-kingdom: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area; the page bounds Mpondoland by the Mthatha and the Mtamvuna, 'not more than 50 km wide'

Gaps for a gap-filler:
- `/ledger/0`: the founding of the Mpondo kingdom (1820 is the first dated act, confidence 1) (try https://en.wikipedia.org/wiki/Faku_kaNgqungqushe (unverified title))
- `/ledger`: the Port St Johns cession (1878) and the 1844 treaty, not on the Pondoland page (try https://en.wikipedia.org/wiki/Port_St._Johns)

Spot checks:
- `/ledger/0` on Pondoland: confirmed as the first dated act: 'In 1820, Mpondo King Faku granted permission to the Wesleyans'; no founding date (confidence 1, honest)
- `/ledger/1` on Pondoland: confirmed: 'In 1886 the British annexed Xesibeland, traditionally part of the Mpondo Kingdom'
- `/ledger/2` on Pondoland: confirmed: 'in 1894 the amaMpondo were forced to accept the annexation of their own region to the Cape Colony'

### griqualand-east: fix

Area: infobox 20000 km2 (year None), drawn n/a km2, ratio None; infobox 'Estimate: 20,000 km2' is a maximum extent; the region 'Griqualand East' is not in the gazetteer yet, so the drawn area cannot be computed

Findings:
- `/ledger/1` (APPLIED by reviewer): A capital_move dated 1874 at confidence 1 was a marker for the British assumption of control, not a move; the real move (Mount Currie laager to Kokstad) is dated 1872 on the page. Evidence: Griqualand_East: infobox 'Move from Mt.Currie: 1869', 'Kokstad founded: 1872'; the text places the move and founding in 1872; 'The British assumed direct control of the territory in 1874.' Fix: Re-dated to 1872, confidence 2, note rewritten; the 1874 British control is left as a thin item.
- `/identity/capitals` (APPLIED by reviewer): No capital covered 1862-1871 (Kokstad from 1872 only). Evidence: Griqualand_East: the Griqua 'settled at a Laager near Mount Currie, where they stayed for over five years'; infobox 'Laager: 1862'. Fix: Added 'Laager near Mount Currie (stand-in: Kokstad)' 1862-1871 with the Kokstad point, flagged APPROXIMATE.

Gaps for a gap-filler:
- `/ledger`: the British assumption of direct control in 1874 (between Adam Kok III's state and the 1877 act) is not typed; a vassal or occupation pair with british-colonial-empire would carry it (try https://en.wikipedia.org/wiki/Griqualand_East)

Spot checks:
- `/ledger/0` on Griqualand_East: confirmed: infobox 'Laager: 1862'; trek 1861, exile 1863
- `/ledger/1` on Griqualand_East: not as entered: no move in 1874; re-dated to the 1872 move (applied)
- `/ledger/2` on Griqualand_East: confirmed: 'in 1877 the Cape Parliament passed the Griqualand East Annexation Act (Act 38 of 1877)'; promulgated 17 September 1879

### griqualand-west: fail

Area: infobox 40000 km2 (year None), drawn n/a km2, ratio None; the region 'Griqualand West' is not in the gazetteer yet

Findings:
- `/ledger/2`: The 27 October 1871 event is a loss of the whole of Griqualand West to british-colonial-empire, yet K0 (1800-1880) keeps drawing it and the dossier continues as the same territory (rename 1873, merge into the Cape 1880); meanwhile british-cape-colony (af-07-b) gains it from 'Griqualand West' in 1871-10 and merges it again in 1880-10. The land is drawn by two or three states for nine years. Evidence: Griqualand_West: on 27 October 1871 the district was proclaimed 'British territory'; infobox 'British rule imposed: 1871'; 'In 1873 it was proclaimed as a British colony, with its capital at Kimberley'; 'formally united with the Cape Colony' on 18 October 1880. Fix: Make 1871 a 'rename' (Griqua state to British territory; British sovereignty in the note; certainty already turns sharp in 1871) and keep K0 to 1880, or end this dossier in 1871 and give the colony 1871-1880 to the Cape; route to af-07-b: the Cape's 1871-10 gain should go if this dossier keeps the colony.

Gaps for a gap-filler:
- `/ledger/0`: the pre-1871 outline (K0 note: confidence 1) and the 1800 founding (infobox, no source for the extent) (try https://en.wikipedia.org/wiki/Griqua_people)

Spot checks:
- `/ledger/0` on Griqualand_West: confirmed: infobox 'Established: 1800'; Adam Kok I 1800-1820, Andries Waterboer 1820-1852
- `/ledger/1` on Griqualand_West: confirmed: 'At the settlement of Klipdrift, on 30 July 1870' Stafford Parker declared the Klipdrift Republic
- `/ledger/2` on Griqualand_West: confirmed (date): proclaimed 'British territory' on 27 October 1871; the type is the fault
- `/ledger/3` on Griqualand_West: confirmed: 'In 1873 it was proclaimed as a British colony'
- `/ledger/4` on Griqualand_West: confirmed: Act of 27 July 1877, union 'set for 18 October 1880'

### british-kaffraria: pass

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area; infobox 'Established: 1835' against the lead's 1847 is stated in the notes; mirrored by british-cape-colony 1860-03 and 1866-04

Spot checks:
- `/ledger/0` on British_Kaffraria: confirmed: 7 March 1860 'the Cape Colony again dis-annexed British Kaffraria, and it became a separate crown colony'
- `/ledger/1` on British_Kaffraria: confirmed: 're-incorporated into the Cape Colony on 17 April 1866'

### stellaland: thin

Area: infobox 15500 km2 (year 1882), drawn 15394 km2, ratio 0.99; K0 disc of 70 km round Vryburg matches; Goshen 10,400 km2 against the 40 km Mmabatho disc (5,027 km2) in K1 is drawn small

Gaps for a gap-filler:
- `/ledger`: the South African Republic's protection and annexation of September 1884 ('On 10 September 1884, President Paul Kruger ... declared the area under the protection of the South African Republic', annexed 'six days later'), on the page the author opened, is not typed (occupation or vassal pair with south-african-republic) (try https://en.wikipedia.org/wiki/Stellaland)
- `/ledger/1`: Goshen's own founding (1882) and extent before the 1883 merger (Stellaland page: Goshen 10,400 km2); the Goshen titles tried did not load (try https://en.wikipedia.org/wiki/Goshen_(country) (unverified title))

Spot checks:
- `/ledger/0` on Stellaland: confirmed: 'Founding of Stellaland: 26 July 1882'
- `/ledger/1` on Stellaland: confirmed: 'In 1883, Stellaland merged with Goshen to form the United States of Stellaland'
- `/ledger/2` on Stellaland: confirmed: 'Abolished: August 1885'; Warren's force 'In December 1884'

### british-bechuanaland: thin

Area: infobox 133190 km2 (year 1885), drawn n/a km2, ratio None; body-text figure; the region 'British Bechuanaland' is not in the gazetteer yet

Gaps for a gap-filler:
- `/ledger/0`: the Tswana lands south of the Molopo (Mankoroane's Tlhaping, Montshiwa's Rolong) enter at the 1885 founding with stellaland as the only counterpart; they make up most of the 133,190 km2 (try https://en.wikipedia.org/wiki/Montshiwa (unverified title))

Spot checks:
- `/ledger/0` on British_Bechuanaland: confirmed: 'Crown colony established: 30 September 1885' from 'Stellaland, Goshen and other territories to the south of the Molopo and Nossob rivers'
- `/ledger/1` on British_Bechuanaland: confirmed: 'Annexation to Cape Colony: 16 November 1895'

### mtetwa-paramountcy: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; infobox area blank

Gaps for a gap-filler:
- `/keyframe_review/0`: the box's 30.2S and 28.0S limits are the researcher's own placing of the Umkhomazi and Hluhluwe; it overlaps the ndwandwe-kingdom box (28.0-28.25S, 30.6-32.9E, about 6,000 km2) for 1780-1816, and the zululand 1816 core (try https://en.wikipedia.org/wiki/Mthethwa_Paramountcy)

Spot checks:
- `/ledger/0` on Mthethwa_Paramountcy: confirmed: infobox 'c. 1780-1817'; 'arose in the 18th century south of Delagoa Bay'
- `/ledger/1` on Dingiswayo: confirmed: died 1817, 'captured and beheaded by Zwide at Ngome'; 'then superseded by the Zulu Kingdom under Shaka' (Mthethwa page)
- `/keyframe_review/0` on Dingiswayo: confirmed: 'it dominated the areas from the Umkhomazi River which is in the south of the Hluhluwe in the north' (Etherington)

### ndwandwe-kingdom: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the page

Gaps for a gap-filler:
- `/keyframe_review/0`: the box's 27.4S and 28.25S limits are the researcher's placing of the Pongola and the Black Umfolozi; it overlaps the mtetwa-paramountcy box in 28.0-28.25S for 1780-1816 (try https://en.wikipedia.org/wiki/Zwide)
- `/ledger/2`: the end date: infobox 'Disestablished: 1825' against the dossier's 1820 (stated in notes) (try https://en.wikipedia.org/wiki/Zwide)

Spot checks:
- `/ledger/0` on Ndwandwe: confirmed: infobox 'Established: c. 1780'; 'c. 1780 - 1805: Langa KaXaba'
- `/ledger/1` on Ndwandwe: confirmed: in early 1820 'the Ndwandwe forces were divided and decisively defeated in the Battle of Mhlatuze River'
- `/keyframe_review/0` on Ndwandwe: confirmed: 'settled in the area between the Pongola River and the Black Umfolozi River'

### swazi-kingdom: thin

Area: infobox 17364 km2 (year 2024), drawn n/a km2, ratio None; modern area; Kingdom_of_Eswatini: Mswati II 'greatly extended the area of the country to twice its current size' (undated), matching K1's eSwatini plus 105 km disc

Findings:
- `/ledger/1` (APPLIED by reviewer): capital_move 1815 at confidence 3 rested on a quoted timeline sentence ('1815: Ndvungunye died. Sobhuza I ... moved the capital to Zombodze in central Swaziland') that is not on the page; the page dates Sobhuza's accession (1815) but not the move. The same quote stood in /identity/capitals/1/note. Evidence: History_of_Eswatini: Ndvungunye served 'until 1815'; Somhlolo moved 'his capital from Zombodze in Shiselweni to the centre of Swaziland at another kraal called Zombodze' (tied to the Ndwandwe conflict, no year); the page has no timeline table of that kind. Fix: Confidence lowered to 2 and both notes rewritten with the page's words.

Gaps for a gap-filler:
- `/ledger/4`: the 1881 Nomahasha loss names portuguese-mozambique, which records no such gain and does not hold that land in 1881 (gaza-empire K1 draws Maputo province until 1895); confidence-1 bridge: find the treaty or name 'nobody' / gaza-empire (try https://en.wikipedia.org/wiki/Namaacha_District (unverified title))
- `/ledger/2`: the date Swazi rule reached Barberton and Nomahasha (Mswati II 'inherited' it in 1839, so the gain is earlier; confidence 1) (try https://en.wikipedia.org/wiki/Sobhuza_I)
- `/ledger/0`: the founding under Ngwane III (1744 bridge, confidence 1) (try https://en.wikipedia.org/wiki/Ngwane_III)
- `/ledger`: the deeds of sale of 1846 and 1855 to the Dutch republics (History_of_Eswatini: they 'seemed to surrender the whole of the Swazi territory') and the 1850s campaigns (try https://en.wikipedia.org/wiki/History_of_Eswatini)

Spot checks:
- `/ledger/1` on History_of_Eswatini: not on page as quoted (applied: confidence 2, quote replaced)
- `/ledger/2` on History_of_Eswatini: confirmed (inheritance, not a dated gain): 'succeeded in 1839 by his son Mswati II'; land 'as far as present-day Barberton ... included the Nomahasha district'
- `/ledger/3` on History_of_Eswatini: confirmed: Pretoria Convention article 24; 'the Swazi territory was reduced in size'
- `/wars/0` on History_of_Eswatini: confirmed: 'Mbandzeni aided the British ... to defeat Sekhukhune' in 1879

### lozi-kingdom: fail

Area: infobox 390000 km2 (year 1890), drawn 389256 km2, ratio 1.0; body-text 'In the late 19th century ... around 150,000 sq mi (390,000 km2)'; K1 disc of 352 km round Mongu

Findings:
- `/keyframe_review/0`: K0 (1650-1877) draws the Western Province straight through 1840-1863, although /ledger/1 loses it to makololo-kingdom around 1840 and /ledger/2 regains it in 1864; makololo-kingdom K0 (1840-1863, this batch) draws the same province, so about 126,000 km2 is drawn by two states for 24 years. Evidence: Barotseland: infobox status '17th c. - c. 1840' and '1864-1899'; 'around 1840, Sebitwane's Makololo entered onto the Plain'; 'A rebellion in 1864 restored the kingdom'. Fix: Split K0 into lozi-kingdom_1650 (1650-1839) and lozi-kingdom_1864 (1864-1877), with no Lozi shape for 1840-1863.
- `/ledger/6`: The 1911 loss of the Caprivi part to german-africa follows the page ('In 1905 and 1911 respectively ... Portuguese Angola and the Caprivi Strip'), but K2 and K3 then draw that strip as Lozi through 1890-1910, the years Cliopatria's German Africa holds it. Evidence: Barotseland (page text as quoted); german-africa is a Cliopatria row (group not run). Fix: Keep the page's year but say in the K2/K3 note that the strip overlaps german-africa from 1890, so the af-08 group can settle it.

Gaps for a gap-filler:
- `/ledger/0`: the founding (17th century; 1650 bridge, confidence 1) (try https://en.wikipedia.org/wiki/Lozi_people)
- `/ledger/3`: the 1878 extent of about 390,000 km2 and its counterparts (confidence 1) (try https://en.wikipedia.org/wiki/Lewanika)
- `/ledger`: 'In 1895, the Portuguese occupied some of the Lozi's western territory' (Barotseland) is not typed (occupation_start 1895 with portuguese-angola, ending in the 1905 loss) (try https://en.wikipedia.org/wiki/Barotseland)

Spot checks:
- `/ledger/1` on Barotseland: confirmed: 'around 1840, Sebitwane's Makololo entered onto the Plain'
- `/ledger/2` on Barotseland: confirmed: 'A rebellion in 1864 restored the kingdom'
- `/ledger/4` on Barotseland: confirmed: 'With the 1899 Order, Lewanika lost powers over territory outside of the Valley (Bulozi proper) to the BSAC'
- `/ledger/5` on Barotseland: confirmed: 1905 loss in the west to Portuguese Angola
- `/ledger/6` on Barotseland: confirmed as the page states it (1911, Caprivi Strip); see fix on the overlap
- `/ledger/7` on Barotseland: confirmed: 'The 1911 Order of Council merged Barotziland-North-Western Rhodesia and North-Eastern Rhodesia'

### makololo-kingdom: pass

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the pages; the Makololo shape is safe once lozi-kingdom stops drawing 1840-1863

Spot checks:
- `/ledger/0` on Barotseland: confirmed: 'around 1840, Sebitwane's Makololo entered onto the Plain' (Makololo page: 'By 1845, Sebetwane had conquered Barotseland'; the conflict is in the notes)
- `/ledger/1` on Barotseland: confirmed: 'A rebellion in 1864 restored the kingdom'
- `/ledger/2` on Makololo: confirmed: 'the Makololo dynasty of Sebetwane in Barotseland came to an end in 1864'

### xhosa-kingdom: thin

Area: infobox None km2 (year None), drawn n/a km2, ratio None; no area on the pages

Findings:
- `/ledger/3` (APPLIED by reviewer): Confidence 3 on the 1820 loss of the Fish-Keiskamma strip, though the page does not date the push to the Keiskamma; 1820 is the year it gives for the Albany district, on the Cape side of the Fish. Evidence: Xhosa_Wars: 'The British colonial authorities pushed the Xhosa further east beyond the Fish River to the Keiskamma River'; 'The Albany district was established in 1820, on the Cape's side of the Fish River'. Fix: Confidence lowered to 2.

Gaps for a gap-filler:
- `/ledger/7`: Gcalekaland in 1878 was 'administered as a British territory' (Xhosa_Wars), not annexed to the Cape; british-cape-colony has no 1878 gain: find the annexation date (the Transkei annexations) or name british-colonial-empire (try https://en.wikipedia.org/wiki/Gcalekaland (unverified title))
- `/ledger/2`: the end of the Zuurveld war (1812 bridge, confidence 1) (try https://en.wikipedia.org/wiki/Fourth_Xhosa_War (unverified title))
- `/identity/capitals/0`: the stand-in seat (Bhisho) lies in British Kaffraria, outside the Xhosa shape in 1835 and from 1847; the Gcaleka seat east of the Kei is not named on the pages (try https://en.wikipedia.org/wiki/Xhosa_people)
- `/ledger/0`: the kingdom is older than 1779 ('before the 15th century', Xhosa people); 1779 is the first dated frontier (try https://en.wikipedia.org/wiki/Xhosa_people)

Spot checks:
- `/ledger/0` on Xhosa_Wars: confirmed: 'demarcated the Great Fish River as the eastern boundary of the colony in 1779'
- `/ledger/1` on Xhosa_Wars: confirmed: 'In 1811, the Xhosa occupied the area'
- `/ledger/3` on Xhosa_Wars: not dated on page (applied: confidence 2)
- `/ledger/4` on Xhosa_Wars: confirmed: land 'from the Cape's prior frontier, the Keiskamma River, as far as the Great Kei River' annexed as Queen Adelaide Province (1835)
- `/ledger/5` on Xhosa_Wars: confirmed: 'The province was disannexed in December 1836'
- `/ledger/6` on Xhosa_Wars: confirmed: on 23 December 1847 Smith 'announced the annexation of the country between the Keiskamma and the Kei rivers'

## Cross-dossier matrix (unmatched and disputed rows only; the JSON has all rows)

- mismatch: mutapa-empire 1632 loss (counterpart portuguese-mozambique) vs portuguese-mozambique 1632 gain: both sides exist and agree on the year, but the valley is not in any Mutapa keyframe; see the mutapa-empire fix
- mismatch: portuguese-mozambique 1632 gain (counterpart mutapa-empire) vs mutapa-empire 1632 loss: both sides exist and agree on the year, but the valley is not in any Mutapa keyframe; see the mutapa-empire fix
- mismatch: betsimisaraka-kingdom 1817 loss (counterpart merina-kingdom) vs merina-kingdom 1817 gain: merina-kingdom gains only Toamasina in 1817; the rest of the Betsimisaraka coast lost here has no Merina gain (af-07-a)
- missing: boina-kingdom 1840 loss (counterpart merina-kingdom): merina-kingdom (af-07-a) has no 1840 gain
- missing: menabe-kingdom 1834 loss (counterpart merina-kingdom): merina-kingdom (af-07-a) has no 1834 gain (and no 1834-1846 contest)
- missing: pedi-empire 1820 loss (counterpart ndwandwe-kingdom): ndwandwe-kingdom has no gain and dissolves in 1820; see the pedi-empire fix
- mismatch: griqualand-west 1871 loss (counterpart british-colonial-empire) vs british-cape-colony 1871 gain: british-cape-colony gains Griqualand West in 1871-10 (string counterpart) while this ledger loses it to british-colonial-empire and keeps drawing it; see the griqualand-west fix
- missing: stellaland 1883 merge (counterpart Goshen): Goshen has no dossier and is not in the author's counterparts_needing_dossiers (added to this report)
- missing: swazi-kingdom 1881 loss (counterpart south-african-republic): south-african-republic (af-07-b) records no 1881 gain
- missing: swazi-kingdom 1881 loss (counterpart portuguese-mozambique): portuguese-mozambique (this batch) records no 1881 gain and does not hold that land; gaza-empire K1 does
- missing: lozi-kingdom 1905 loss (counterpart portuguese-angola): portuguese-angola has no 1905 gain from lozi-kingdom
- missing: xhosa-kingdom 1878 loss (counterpart british-cape-colony): british-cape-colony (af-07-b) has no 1878 gain; the page says Gcalekaland was administered as British territory
- mismatch: portuguese-mozambique 1897 contest_start (counterpart mutapa-empire): mutapa-empire dissolves in 1885; the contest names a dead state (fix in portuguese-mozambique)
- missing: pedi-empire 1876 contest_start (counterpart south-african-republic): south-african-republic (af-07-b) has no contest with pedi-empire in 1876-1877 and no gain at the 1882 dissolve
- mismatch: gaza-empire 1895 loss (counterpart portuguese-mozambique) vs portuguese-empire 1895 gain: portuguese-empire (eu-12) also gains the Gaza land in 1895 (string 'Gaza Empire'): the same land is gained by two Portuguese dossiers; route to eu-12/af-08
- mismatch: gaza-empire 1837 gain (counterpart Nxaba's Ngoni kingdom) vs portuguese-mozambique 1632 gain: overlap: gaza-empire K1 (1837-1895) and portuguese-mozambique K5-K7 both draw the Portuguese posts and the Zambezi strip in Sofala province; see the gaza-empire fix

## Gazetteer names needed

- Conquered Territory (region): basutoland (also free-orange-state)
- Sekhukhuneland (region): pedi-empire; swazi-kingdom
- Pondoland (region): mpondo-kingdom
- Xesibeland (region): mpondo-kingdom (also british-cape-colony)
- Griqualand East (region): griqualand-east (also british-cape-colony)
- Griqualand West (region): griqualand-west
- British Kaffraria (region): british-kaffraria; xhosa-kingdom (also british-cape-colony)
- British Bechuanaland (region): british-bechuanaland (also british-cape-colony)
- Kionga Triangle (region): portuguese-mozambique
- Sena (place): portuguese-mozambique

## Counterparts needing dossiers (added by the reviewer; the author's list follows in the JSON)

- Goshen (Land Goshen / Het Land van Goossen) (goshen, [1882, 1883]): merged into Stellaland in 1883 (stellaland /ledger/1); Stellaland page gives 10,400 km2; not in the author's list
- Chioko's Mutapa-Barue coalition (Zambezi rising) (string counterpart only, [1897, 1902]): needed by portuguese-mozambique /ledger/16-17 unless mutapa-empire is extended

## Problems and routing

- Nothing failed to load: 38 WebFetch calls on 35 distinct Wikipedia pages. The WebFetch relay summarises, so 'quotes' in the spot checks are the relay's verbatim extracts.
- Verdict rule used here: fail = at least one unapplied finding that changes the drawing or the ledger's meaning (keyframe contradicting its own ledger, in-batch overlap over about 10,000 km2, an area or land move with no event, a counterpart that does not exist at that date, a confidence-3 claim not on the page); thin = honest page-silent gaps for gap-fillers (findings I applied may also be listed); fix = I applied every finding that needed one; pass = I could not break it.
- Reviewer edits (re-validated, read back): xhosa-kingdom /ledger/3 confidence 3->2; menabe-kingdom /ledger/3-5 confidence 3->2; swazi-kingdom /ledger/1 confidence 3->2 and two notes (a quoted 'timeline' sentence is not on History_of_Eswatini); ndebele-kingdom /ledger/7-8 and /wars/2 counterpart south-african-republic -> Voortrekkers; griqualand-east /ledger/1 re-dated 1874->1872 (confidence 1->2) and a capital entry added for the Mount Currie laager 1862-1871. Files were re-serialised with json indent 2.
- Cross-batch items for af-07-b (british-cape-colony, south-african-republic, free-orange-state): the Cape's 1871-10 gain of Griqualand West conflicts with griqualand-west (colony to 1880); no 1878 Gcalekaland gain; Cape and Merina use strings ('Xhosa chiefdoms', 'Mpondo kingdom', 'Griqualand West', 'Griqualand East', 'British Kaffraria', 'British Bechuanaland', 'Sakalava kingdom of Menabe', 'Sakalava kingdom of Boina') where slugs now exist; SAR lacks the 1876-77 Pedi contest, the 1881 Swazi gain and any 1882 Pedi gain.
- Cross-batch items for af-07-a (merina-kingdom): no 1834 gain from menabe-kingdom, no 1834-1846 contest, no 1840 gain from boina-kingdom, no 1820-1832 Boina tributary or 1846+ Menabe suzerainty, and only Toamasina gained from betsimisaraka-kingdom in 1817.
- portuguese-empire (eu-12) gains the Gaza lands in 1895 as portuguese-mozambique does: double-drawn Portuguese land to settle between eu-12 and af-08.
- The author's note that british-cape-colony has 'no mirror of the 1877 annexation of Griqualand East' is out of date: the Cape ledger has a 1877 gain from 'Griqualand East'.
- Neighbour dossiers named in the author's brief section 6: new-france, republic-of-liberia and united-states-of-america exist but share no border or event with this batch; british-africa, french-africa and kingdom-of-portugal have no file yet (groups af-08 and eu-12 not run). The real neighbours read for the matrix were british-cape-colony, free-orange-state, south-african-republic, zululand, swaziland, merina-kingdom, colony-of-natal, portuguese-angola, dutch-cape-colony, natalia-republic and portuguese-empire.
