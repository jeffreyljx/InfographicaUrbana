# af-07-b: Southern Africa (part b): notes for the reviewer and the gap-fillers

Written 2026-10-19. Ten distinct pages were opened (all loaded on the first try; no page failed): Natalia Republic, Colony of Natal, Orange Free State, Free State-Basotho Wars, South African Republic (twice), First Boer War, Second Boer War, Nieuwe Republiek, Eswatini, History of Eswatini. All Wikipedia, read through WebFetch (a summarising relay: quotes in the dossiers are only the sentences the relay presented in quotation marks; everything else is paraphrase and unquoted). Dossiers: natalia-republic, colony-of-natal (new, split), free-orange-state, south-african-republic, nieuwe-republiek, swaziland (merged with the eswatini row).

## Rows to split or merge

- natalia-republic: Cliopatria's one row 'Natalia Republic' 1840..1910 (8 shapes) is the Boer republic (12 Oct 1839 - May 1843) and then the British Colony of Natal (4 May 1843 - 31 May 1910). Split: natalia-republic (1839-1843, shape 1840 + a new 1839 keyframe) and colony-of-natal (new slug, type colony, family britain; reviews the shapes 1848-1908 and new keyframes 1843, 1900). The validator warns that 7 shapes have no verdict in natalia-republic and 1 (1840) has none in colony-of-natal: intended (shape 1840 serves the republic to May 1843 and the colony after). The colour agent should seed colony-of-natal (British colony) with a different colour from the Boer republic.
- swaziland / eswatini: same Wikidata Q1050 and the same Swazi monarchy; Cliopatria's gap 1908-1968 is the British protectorate period. ONE dossier under the earlier slug 'swaziland', cliopatria_names ['Swaziland', 'Eswatini'], 1885-2024, with the protectorate years as vassal events (South African Republic 1894-1899, Britain 1903-1968) and new keyframes 1895-1899 and 1908-1968. af-08-l (owner of the eswatini row) must not write a second dossier. The slug 'eswatini' is redundant; the 1969-2024 shapes are reviewed in swaziland.json.
- nieuwe-republiek: no split. Its Cliopatria shape is in the wrong place (see below).
- free-orange-state, south-african-republic: no split; each starts before Cliopatria (1854 and 1852) and ends after it (1902), so new keyframes were added for the early and late years.

## Per state: what could not be settled

### natalia-republic
- The republic's boundary: the page gives none ('the Drakensberg was set as the northern limit of Natal in August 1843'). REPAIRED 2026-10-19: the shape is now Cliopatria's 1840 shape minus Klip River county (see 'Repair of 2026-10-19' at the end); Pretorius's proclamation of 'a large tract from St Lucia Bay' is now dated (14 February 1840, Battle of Maqongqe page) but still not drawn (no inland line on either page).
- Annexation date: infobox 12 May 1843 (Natalia page), 4 May 1843 (Colony page), Volksraad acceptance 8 August 1843; the ledger uses May.
- Natal 'became part of Cape Colony in 1844 and was separated again in 1856' (Natalia page) against 'administered from the Cape Colony in 1844' (Colony page): Cliopatria keeps Natal separate; no event.
- No ruler strip (the page's president, Pretorius 1839-1843, stands alone).

### colony-of-natal
- Area: Colony page infobox 91,610 km2 (1904) against Cliopatria 62,052 km2 (0.68): within a factor of two, but the shape is still short; Alfred County/Nomansland and Tongaland, if Natal gained them, are not on the page.
- 1843 Buffalo-Tugela gift ('Mpande gave up to Natal all the territory between the Buffalo and Tugela rivers, which later formed Klip River county', Natalia page): REPAIRED 2026-10-19. The first version read it as the 10 Msinga cells; the gain now covers all of Klip River county (39 cells of Cliopatria's Natalia shape north of the Tugela) plus the Msinga circle (10 cells Cliopatria draws in Zululand). The page places the gift in its narrative after the Volksraad's acceptance of 8 August 1843 (Cloete's visit to Mpande) and dates it no closer, so the event stays at the year 1843. The zululand dossier (af-07-a) still has no matching 1843 loss.
- Vryheid land: Cliopatria's Natal 1898-1910 shapes contain 24 cells (6,070 km2) around Vryheid that were the New Republic's (1884-1888) and then the Transvaal's until the January 1903 transfer; cut out for 1898-1902 (keyframes natalia-republic_1898 and colony-of-natal_1900) and restored by the January 1903 gain (keyframes _1900 and _1908 add Vryheid and a circle for Utrecht/Wakkerstroom). The districts' extent is my reading of the page's 'Vryheid, Utrecht and part of Wakkerstroom' (the Colony page; the Nieuwe Republiek page names none).
- Anglo-Zulu War of 1879: the Colony page 'gives no date', so none is recorded here (zululand dossier: 11 January to 4 July 1879).
- Counterparts needing dossiers: transvaal-colony (successor of the South African Republic, 1900 or 1902 to 1910), union-of-south-africa (successor, 1910).
- Boer War zone: northern Natal (Newcastle/Dundee/Ladysmith) as two circles, from 11 October 1899 to the relief of Ladysmith on 28 February 1900; Boers' withdrawal from the rest of Natal and the renewed invasion of September 1901 are not dated by the pages.

### free-orange-state
- 'Conquered Territory': the page and the Basotho page do not define its extent (the Basotho page: the disputed area ran 'from present-day Wepener to Zastron', and 'north of the Caledon, including Harrismith' for the wider area). The dossier uses {region: Conquered Territory}, absent from the gazetteer: define it as the eastern Free State strip between the Warden Line (Cornetspruit and the Orange River through Vechtkop to Jammerbergdrift on the Caledon) and the Caledon river (Zastron-Wepener-Ladybrand-Ficksburg). Until then the 1854-1868 corrections and the 1858-1869 contest/gain events resolve to nothing.
- Cliopatria's outline is the modern Free State province from 1856 and so contains the Conquered Territory 13 years early; its 1885 and 1898 shapes lose a 3-cell notch (759 km2) near Ladybrand-Ficksburg that no page explains; both corrected.
- Area: infobox 181,299 km2 (1875) against 133,104 (0.73). The infobox figure looks large for the republic; no decision needed (within a factor of two).
- Keate arbitration of 19 February 1870 ('the Klip River was fixed as the dividing line with the Transvaal, giving the Transvaal the Wakkerstroom area'): the geography on the page is unclear, so no event. Griqualand West (proclaimed British 27 October 1871; Free State paid £90,000 in July 1876): no land change in the shape; whether Cliopatria's outline touches the diamond fields was not tested.
- Boer War: only the Natal front is dated for the Free State (a train seized on the Natal border on 11 October 1899); its Cape front (Colesberg, Stormberg) is on no page opened. Annexation (28 May 1900, Orange River Colony) is shown as occupation (hatched) to the Treaty of Vereeniging, 31 May 1902, matching the infobox end. Successor orange-river-colony needs a dossier (British colony 1900-1910).
- Counterpart basutoland is listed for af-07-x (its slug in their scope); first Basotho war contest 1858 is from the declaration date (the page names no battle).

### south-african-republic
- Cliopatria's 1890 addition (36 cells, 9,104 km2, lon 31.8-32.7E, lat 28.0-26.9S) is the same mislocated polygon as its Nieuwe Republiek row, and is dated 1890 instead of 20 July 1888; replaced by a 66 km circle at Vryheid from 1888. The Cliopatria 1895 addition (62 cells) is all of Swaziland, which was a protectorate, not direct land: corrected to a vassal.
- 1852-1859: the Lydenburg and Utrecht republics (merged November 1859) are subtracted by circles of my reading; the Zoutpansberg republic's date is not on the page and it stays inside.
- 1856 to 1885: the shape loses 12 cells (3,035 km2) in the north and west and gains 4; no page explains (the London Convention of 1884 ended British suzerainty; the page states no boundary terms). Stellaland and Goshen (franchise to their burghers on 9 May 1887) are not defined by the page.
- 1877-1884: Cliopatria draws the Transvaal in its British Cape Colony row; the dossier adds a new keyframe 1877-1884 and mirrors the Cape ledger (occupation 12 April 1877 to 3 August 1881, vassal 3 August 1881 to 27 February 1884), plus a contest 20 December 1880 to March 1881 that the Cape dossier lacks. The counterpart 'british-cape-colony' follows Cliopatria's row, not history (it was the Crown's annexation).
- Pretoria's years as capital are bridged (page: Potchefstroom 1858-1860, Heidelberg 1880-1881).
- Counterparts needing dossiers: transvaal-colony, republic-of-lydenburg, republic-of-utrecht (small Boer republics merged November 1859; start years not on any page).

### nieuwe-republiek
- Cliopatria shape (1885-1889, 10,205 km2) sits at 31.7-32.8E east of Swaziland, not at Vryheid (30.8E): verdict wrong, replaced by a 66 km circle at Vryheid (the same region the zululand dossier uses for its 1884 loss); the real life is 5/16 August 1884 to 20 July 1888.
- Two founding dates on the page (5 and 16 August 1884); recognition by Britain on 22 October 1886 changes no border (no event); the 1887 coastal annexation has an event but no keyframe (extension not dated).
- 'Utrecht' is not named by the page among the 1903 transfers to Natal.

### swaziland
- Pre-1885 history is not dated on the pages (Ngwane III mid-18th century; Sobhuza I 1815; Mswati II 1839-1865; land deeds of 1846 and 1855; the South African Republic's 1868 proclamation): the 'found' event at 1885 is confidence 1 (only the first year of Cliopatria's shape). A 'swazi-kingdom' dossier before 1885 is needed (af-07-x).
- 1903 status: Eswatini page 'British High Commission Territory ... a protectorate was not established', History of Eswatini 'British protectorate'; drawn as a British vassal 1903-1968. The 1908-1968 outline is bridged from the 1900 and 1969 shapes (confidence 1; no boundary change mentioned). The 1890 'triumviral administration', the 1889 provisional council, the 1904-1909 land partition (38% set aside for the Swazi by 1910) and the 1964 reserve share move no border.
- Capital: one bridged entry (Lobamba/Mbabane), as neither is dated; no ruler strip.
- Cliopatria's 1973-1975 area (17,289 km2) differs from 1969 and 1976 (17,129 km2) by vertex noise only (no H3 cell differs).

## Gazetteer names needed
- region 'Conquered Territory' (free-orange-state): above.
- Coordinate circles stand for places the gazetteer lacks and could be replaced by names: Utrecht (South Africa, 30.32E 27.65S), Wakkerstroom (30.14E 27.35S), Lydenburg (30.45E 25.10S), Newcastle (South Africa, 29.93E 27.76S), Dundee (South Africa, 30.23E 28.17S), Msinga/Rorke's Drift (30.5E 28.4S), St Lucia Bay and the Mhlatuze mouth (32.2E 28.6S).

## Cross-dossier mirrors to check (other groups)
- zululand (af-07-a): no 1843 loss to Natal; its Cliopatria shapes 1840-1897 overlap the Buffalo-Tugela country and the Vryheid land.
- british-cape-colony (af-07-a): its 1854 loss to free-orange-state and its 1877-1884 Transvaal events are mirrored here.
- british-africa / british-colonial-empire (af-08): Boer War counterparts use british-colonial-empire.

## Repair of 2026-10-19 (after review-af-07-b: natalia-republic fail)

Pages re-opened (WebFetch): Natalia Republic (the Mpande, Klip River and Tugela sentences), Battle of Maqongqe (new). Files changed: natalia-republic.json (fail), and, because the finding pairs them, colony-of-natal.json (ledger /0 gain, /1 found, predecessor land, the colony-of-natal_1843 note and notes; the other thin items of colony-of-natal are not touched). Both validate (0 errors; warnings unchanged: 7 and 2).

What changed
- natalia-republic_1839 and _1840, ledger /0 (found) and /3 (dissolve), predecessor and successor land: {minus: [Cliopatria Natalia Republic 1840, polygon 28.8-30.7E 27.4-28.75S]}, 102 cells, about 25,800 km2 against 35,700 km2 for the full 1840 shape in the gazetteer's cells (Cliopatria's own figure 37,668 km2).
- Why the polygon and not {region: Klip River County}: the gazetteer has no such region (gazetteer_names_needed), and an unresolved name would leave the old shape on the map; the polygon resolves now and is a stand-in to swap for the region later. The box is the reviewer's (north of the Tugela, west of the Buffalo) extended west from 29.4E to 28.8E: the page says the Tugela 'from source to mouth' was the frontier, so the 5 cells along the upper river (the Drakensberg end; centres about 28.5-28.7S) are north of it too. The reviewer's 34 cells become 39 (9,863 km2); one more Natalia cell north of 28.75S (30.72E, 28.72S, east of the box) is kept in the republic as a Tugela-bank cell.
- colony-of-natal /ledger/0: gain = union of Klip River county (the same box cut to Cliopatria's Natalia shape, 39 cells) and the Msinga circle (10 cells), counterpart zululand, still year 1843, confidence 2. Dundee and Nqutu cells that Cliopatria draws in Zululand beyond the Msinga circle are not included: the page names only the two rivers.
- natalia-republic_1840 note and certainty: the St Lucia Bay proclamation is dated (14 February 1840; the battle was 29 January, the Boers reached Mpande on 6 February) and written up as a claim, not drawn. The war 'Boer-Mpande campaign against Dingane' now cites the Maqongqe page (dates above).

What I disagree with, and where
- Nothing in the finding. One reading I weighed against it: the Maqongqe page says a large stretch of land from St Lucia Bay 'was now the border' with the Zulu kingdom (14 February 1840), which could put Klip River county in the republic from 1840. I kept it out because neither page gives an inland line, the Natalia page still has the Tugela as 'the recognized frontier' before Mpande's concession to Natal, and that concession is of this very country. The alternative is written in the _1840 keyframe note, as the finding allows.
- The Maqongqe page (relay) puts the Boers' arrival on 6 February 1840, after the battle of 29 January; the Natalia page's war entry (belligerents natalia-republic and zululand) is kept but cannot be called Boer fighting at Maqongqo.

For af-07-a (zululand), not mine to edit: (1) an 1843 loss of Klip River county and the Msinga cells to colony-of-natal; (2) its keyframes must hold Klip River county until 1843, since the republic's shape no longer does (Cliopatria's Zululand shape does not contain it: it sits in Cliopatria's Natalia shape); (3) its February 1838 loss to the republic precedes the republic's 12 October 1839 founding by 20 months.

Gazetteer names needed (added by this repair): region 'Klip River County' (north of the Tugela and west of the Buffalo; Ladysmith and Newcastle; replaces the polygon in natalia-republic and colony-of-natal).

