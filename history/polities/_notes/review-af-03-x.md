# Review of batch af-03-x (Sahel additions)

Adversarial review, 2026-10-19, of the 41 new-state dossiers written by the af-03-x research agent. The machine copy is history/notes/phase-b/reviews/af-03-x.json.

Verdicts: 17 pass, 1 fix (fixed by the reviewer), 16 thin, 7 fail.

## Method

- validate_dossier.py --resolve on all 41 files: 0 errors, 1 warning (dendi-kingdom /wars/0 outside the life).
- Every keyframe correction resolved with the gazetteer (cell counts x 252.9 km2) and intersected pairwise across the batch for the same years; batch shapes also intersected with the Cliopatria-based neighbours (saadi-sultanate, bamana-empire, massina-empire, mali-empire, songhai-empire, sokoto-caliphate).
- Capitals tested against the keyframes alive in their years.
- Spot checks: 3-6 events per dossier (all events of the smallest ones), weighted to confidence 3 and to the events that move most land, each read on the cited Wikipedia page with WebFetch. No confidence-3 event was found fabricated or mis-dated.
- Vassal events read as the schema defines them: recorded by the overlord only, counterpart = the vassal.

## Batch-wide points

- Vassal mirrors: brief check 3 asks for a vassal_start in the vassal's ledger, but the schema says vassal events are recorded by the overlord only ('counterpart is the vassal itself in both events'). The authors followed the schema and so did this review: overlord-side vassal events are 'exception' in cross_checks, and missing overlord events are routed as 'missing' in the overlord's ledger.
- The gazetteer region 'Futa Toro' (confidence 1) is Senegal cut to the box -16.5..-12.5, 15.5..16.8: it starts at the Atlantic and covers all of Waalo (Saint-Louis admin1) and the north of Louga. futa-toro and jolof-empire draw with it; fixing the gazetteer entry would fix both.
- The gazetteer region 'Hausaland' reaches 17.4 N (Aïr); kingdom-of-kebbi uses it as a tribute region.
- Older af-03-a/b dossiers name these states by text because the slugs did not exist then: sokoto-caliphate ('Sultanate of Kano', 'Sultanate of Katsina', 'Kingdom of Kebbi', 'Nupe Kingdom', 'Sultanate of Gobir', 'Hausa kingdoms of Zamfara and Zazzau'), songhai-empire ('Sultanate of Agadez'), empire-of-kanem ('Bilala'). Their owners should switch to the slugs and settle the year mismatches listed in cross_checks (Kebbi 1805/1808, Nupe 1808/1835, Zazzau 1809/1805).
- saadi-sultanate (1591-1617 own land, vassal from 1618), bamana-empire (Timbuktu 1748-1769 cp pashalik-of-timbuktu) and massina-empire (Djenné 1818, Timbuktu 1826) all conflict with pashalik-of-timbuktu's 1591-1833 discs.
- Reviewer edits applied and re-validated (0 errors, 0 warnings), each read back intact after about 10 s: jolof-empire /ledger/10 confidence 3->2; cayor /ledger/1 confidence 2->1; bundu /ledger/0 counterpart and /wars/0 belligerent 'Gajaaga'->'gajaaga'; gajaaga /ledger/2 region narrowed to a Bakel disc. Each change carries a '[Reviewer af-03-x, 2026-10-19: ...]' note where a note field exists.
- No page failed to load for the reviewer. Neighbour dossiers of the author's brief section 6 that exist: almoravid-dynasty, funj-sultanate, mahdist-state, saadi-sultanate (only saadi-sultanate touches this batch); british-africa, british-gold-coast, french-africa, german-africa, khedivate-of-egypt, muhammad-ali-dynasty and oyo-empire have no dossier yet (groups af-08, me-10, af-04 not run): their counterpart events are exceptions.

## tukulor-empire: thin

Findings:

- `/keyframe_review/2/correction` (to do, not blocking). The 150 km Nioro disc standing for Kaarta overlaps the Diarra disc by about 10,600 km2 in 1855-1859, so Tukulor and Diarra both claim that land before the 31 May 1860 conquest. Evidence: Resolved with the gazetteer: tukulor-empire_1855 x diarra_1054 overlap 10,622 km2 (30% of Diarra); same overlap between kaarta_1650 and diarra_1054 for 1650-1855. Fix: Cut the Diarra disc out of the Nioro disc in the 1855-1860 keyframe (minus the diarra region) or shrink the disc; same cut in the kaarta keyframe.
- `/ledger` (to do, not blocking). Bundu (taken over 'with the support of the Bundu aristocracy' after 1851) and Khasso (kings 'peacefully submitted' 1854) are not in the ledger; the author flagged both in the report. Evidence: Umar Tall page: 'Between May and November 1854, Tall launched a lightning conquest of Bambuk ... The kings of the Khasso region peacefully submitted.' Fix: Add vassal_start 1854 cp khasso (c2, Umar Tall page) and the mirror in khasso; Bundu as the author can source it.

Gaps for a gap-filler:

- `/keyframe_review/5`: the 1864-1889 outline (Kaarta, Ségou, Massina remnant, Dinguiraye, Bambuk) is carried unchanged for 26 years; Muntaga's 1884 revolt at Nioro and Tidiani's Bandiagara are not drawn (try https://en.wikipedia.org/wiki/Ahmadu_Tall)

Spot checks: `/ledger/2` confirmed ('Nioro du Sahel, the capital of Kaarta, in April 1855'); `/ledger/7` confirmed ('Battle of Segou on March 10, 1861' (Umar Tall page: 10 March 1860, conflict noted by the author)); `/ledger/11` confirmed ('Djenné fell quickly followed by Hamdullahi in May 1862'); `/ledger/15` confirmed ('They captured Nioro in 1891 and drove Ahmadu to Bandiagara'); `/ledger/1` confirmed ('Between May and November 1854, Tall launched a lightning conquest of Bambuk'); `/ledger/12` confirmed ('They captured Hamdallahi in February 1864'; died 14 February 1864)

Area: no Cliopatria row and no area on the page (infobox 1852-1903, map caption only); the drawn 1862-1863 keyframe resolves to about 284,000 km2

## wassoulou-empire: fail

Findings:

- `/keyframe_review/6/correction` (BLOCKING). The 1895-1896 keyframe draws Savanes (Kong's own land) as Wassoulou territory while the ledger has Kong only as a vassal (vassal_start 1895/4), so Kong and Wassoulou both claim about 53,600 km2; and Dabakala, the 1895-1898 capital, lies outside every 1895-1898 keyframe. Evidence: Gazetteer: wassoulou-empire_1895 x kong-empire_1737 overlap 53,615 km2 (66% of Kong). Dabakala (-4.43, 8.37) is in the gazetteer's Vallée du Bandama admin1, not in Denguélé, Savanes or Zanzan. Wassoulou Empire page: Samory 'moved his base out of Kabadougou toward the Bandama and Comoe River to Dabakala in February 1895'; Mandingo Wars page: Kong 'pledged fealty to Samory in April'. Fix: 1895-1896 keyframe: Denguélé plus Vallée du Bandama (or a disc at Dabakala), without Savanes (Kong is drawn by kong-empire as a vassal). 1897-1898 keyframe: add Kong's land after its destruction on 23 May 1897 (a gain cp kong-empire to match Kong's dissolve, whose successor is wassoulou-empire) and the Dabakala area.
- `/keyframe_review/7/correction` (BLOCKING). After 23 May 1897 the ledger ends Kong's vassalage but the land of Kong (Savanes) disappears from both dossiers: kong-empire dissolves with successor wassoulou-empire, but no Wassoulou gain picks it up. Evidence: kong-empire /ledger/4 dissolve 1897/5 cp wassoulou-empire; kong-empire identity.successors: wassoulou-empire (Savanes); wassoulou-empire_1897 = Denguélé + Zanzan only. Fix: Add gain 1897/5 cp kong-empire (Savanes or the Kong area), c2, source Wassoulou Empire page ('Samory destroyed the city on May 23, 1897'), and include it in the 1897-1898 keyframe.
- `/keyframe_review/0/correction` (to do, not blocking). The Wassoulou core (Sikasso admin1 minus an 80 km Sikasso disc) overlaps Kénédougou's Koutiala disc by about 11,100 km2 for 1878-1892. Evidence: Gazetteer: wassoulou-empire_1878..1892 x kenedougou-kingdom_1877 overlap 11,128 km2 (29% of Kénédougou). Fix: Also subtract the kenedougou Koutiala disc (place Koutiala, 60 km) from the Wassoulou core, or shrink the disc in kenedougou.

Gaps for a gap-filler:

- `/ledger/1`: c1: Kouroussa, Baro and Norassoba 'after 1875', no year (try https://en.wikipedia.org/wiki/Samori_Ture)
- `/ledger/2`: c1: Kankan taken from the Cissé, '1878-1879 (approximate)'; no page gives the year (try https://en.wikipedia.org/wiki/Kankan)
- `/ledger/6`: c1: when Buré was taken (held by the 1886 treaty) (try https://en.wikipedia.org/wiki/Samori_Ture)
- `/ledger/17`: c1: when Bouna was taken (held by Saranken Mori in 1897) (try https://en.wikipedia.org/wiki/Bouna)

Spot checks: `/ledger/10` confirmed ('Archinard had little trouble capturing Kankan on April 11 and then a deserted Bissandougou' (expedition left Nyamina 10 March 1891)); `/ledger/16` confirmed (French retreat on the 14th (March 1895); Kong 'pledged fealty to Samory in April'); `/ledger/18` confirmed ('Samory destroyed the city on May 23, 1897'); `/ledger/19` confirmed ('surprised Toure's forces at Guelemou on September 29, 1898, and captured the Almamy without a fight'); `/ledger/12` confirmed ('convened another council at Frankonedou on May 9, 1892'); `/ledger/13` confirmed ('During the first months of 1893 ... capture Faranah'; western vassals surrendered)

Area: no Cliopatria row; infobox (1860-1898) gives no area; the drawn 1879-1890 keyframe is about 172,000 km2

## jolof-empire: fail

Findings:

- `/ledger/3` (BLOCKING). Sine and Saloum are recorded as an outright gain (1390) and loss (1520) with a text counterpart, so the Jolof keyframes 1390-1519 draw all of Fatick as Jolof land while the sine dossier of this batch holds the same Fatick from 1335 (100% overlap), and Kaolack while saloum holds it from 1494. Evidence: Jolof Empire page: 'All of these states were tributary to the land-locked state of Jolof'; Kingdom of Sine page: Ndiadiane Ndiaye's election made 'Sine a vassal of the Jolof Empire'; Kingdom of Saloum page: 'Saloum the kingdom was never a part of the empire.' Gazetteer: jolof-empire_1390/1455/1513 x sine_1335 overlap 7,587 km2 (100% of Sine); x saloum_1494 5,311 km2 for 1494-1519. Fix: Replace /ledger/3 and /ledger/7 by vassal_start 1390 (c1) and vassal_end 1520 (c3) with counterpart sine; drop Fatick and Kaolack from keyframes 1390-1519 (Saloum: no event, per its page, or a c1 vassal_start for the pre-1494 'early form'); the sine dossier mirrors (see its findings).
- `/ledger/4` (BLOCKING). The 1455 gain of Futa Toro names counterpart takrur, a dossier that dissolved in 1285 (to mali-empire), and its region (the gazetteer's confidence-1 Futa Toro box) covers all of Waalo, which this dossier holds only as a vassal. Evidence: takrur.json: start 1040, end 1285, /ledger/1 loss 1285 cp mali-empire. Gazetteer: region Futa Toro = Senegal cut to -16.5..-12.5, 15.5..16.8, so jolof-empire_1455 x waalo_1287 overlap 19,979 km2 (100% of Waalo). Jolof page: Biram Njeme Eler 'conquered Namandirou in approximately the 1450s, then extended his authority over Takrur'. Fix: Counterpart: 'Namandirou (Takrur region)' as text, or the dossier that held the valley in 1455; region: the middle valley only (e.g. Matam admin1 plus the river strip east of Dagana), not the gazetteer Futa Toro box.
- `/ledger/10` (applied by the reviewer). Confidence 3 for the 1549 end of hegemony over 'Gambia states (Niumi, Baddibu, Nyani, Wuli)' drawn as the whole of Gambia, but the cited Danki page names only Wuli and Niani. Evidence: Battle of Danki page: the victory 'signaled the end of Jolof hegemony over Cayor, Baol, Saloum, Sine, Wuli, Niani, and Waalo'; it does not mention Niumi, Baddibu or the Gambia. Fix: Confidence lowered to 2.
- `/identity/capitals/1` (to do, not blocking). Thieung has the same coordinates as Njiayeen Sabur (-15.12, 15.39). Evidence: Both capitals at identical points; the page says Eler moved the capital from Njiayeen Sabur to Thieung. Fix: Give Thieung its own coordinates or mark both as proxies in the note.

Gaps for a gap-filler:

- `/ledger/1`: c1: Cayor and Baol 'absorbed early on', bridged to 1360 (try https://en.wikipedia.org/wiki/Cayor)
- `/ledger/5`: c1: the Gambia states' vassalage in the 1450s; the page names no Gambian state (try https://en.wikipedia.org/wiki/Niumi)

Spot checks: `/ledger/6` confirmed ('In 1513, Koli Tenguella led a strong force of Fulani and Mandinka into Futa Toro, seizing it from the Jolof'); `/ledger/7` confirmed ('In 1520 the Serer kingdoms of Sine and Saloum in the south broke away' (but see the fix: tributaries, not provinces)); `/ledger/8` confirmed (1549; Cayor 'a rebellious vassal' won; end of Jolof hegemony over Cayor, Baol, Saloum, Sine, Wuli, Niani and Waalo); `/ledger/11` confirmed (infobox: 'Battle of Danki and empire reduced to a rump kingdom: 1549'); `/ledger/0` confirmed (infobox 'Established c. 1360')

Area: no Cliopatria row and no area on the page; the 1455-1512 keyframe resolves to about 102,000 km2, of which Sine, Waalo and part of Saloum belong to other dossiers

## futa-toro: fail

Findings:

- `/keyframe_review/0/correction` (BLOCKING). The Futa Toro shape (gazetteer region 'Futa Toro' plus all of Matam and Gorgol, about 76,000 km2) covers the whole of Waalo for 1513-1855 and the north of Jolof (Louga) for 1549-1859, although the page describes Futa Toro as a riverine strip and treats Waalo as outside it. Evidence: Imamate of Futa Toro page: 'a strip of agricultural land along both sides of the Senegal River'; Abdul Kader attacked 'the Wolof states of Cayor and Waalo'. The gazetteer region Futa Toro (confidence 1) is Senegal cut to the box -16.5..-12.5, 15.5..16.8, which includes the delta. Overlaps: futa-toro x waalo 19,979 km2 (100% of Waalo, 1513-1855); x jolof-kingdom 10,369 km2 (41% of Jolof, 1549-1859); x bundu 2,023 km2; x gajaaga 759 km2. Fix: Redraw all three keyframes as the middle valley: e.g. {intersect: [{river: Senegal, km: 40}, a box from about Dagana (-15.5) to Bakel (-12.5)]} (both banks, Mauritanian and Senegalese), minus the waalo region; the author's notes should name the cut. Ask for a gazetteer fix of 'Futa Toro' (the box now starts at the Atlantic).
- `/ledger/1` (BLOCKING). The Denianke tribute is one vassal_start with a text counterpart for five states, four of which have dossiers in this batch (jolof-kingdom, waalo, saloum, gajaaga; diarra is also on the page's list), so none can be mirrored; the region adds Fatick (Sine, not on the page's list) and Thiès (Cayor, which became tributary only 'in the early 17th century'). Evidence: Denianke dynasty page: 'By the end of the 16th century, they were receiving regular tribute from the Kingdom of Jolof, Waalo, Gajaaga, Diarra, Diakhaba, Saloum, Goundiourou, Namandirou and the Lamtuna, and possibly Khasso'; 'In the early 17th century, the Fula added Cayor to their roster of tributaries.' Fix: Split into vassal_start events per slug (jolof-kingdom, waalo, saloum, gajaaga, diarra at 1599, c2; cayor at about 1610, c1) each with its own region, drop Fatick, and pair each with the vassal_end of 1776 (c1); the counterpart dossiers mirror.

Gaps for a gap-filler:

- `/ledger/4`: c1: the end of the Denianke tribute, bridged to 1776 (try https://en.wikipedia.org/wiki/Abdul_Kader_Kane)
- `/ledger/5`: infobox also gives 'Incorporated into Senegal Colony: 1877' and the Almamyate survived; the 1859 annexation is the text's date (try https://en.wikipedia.org/wiki/Futa_Toro)

Spot checks: `/ledger/0` confirmed (Koli's reign 1512-37; Jolof page: 'In 1513, Koli Tenguella ... into Futa Toro, seizing it from the Jolof'); `/ledger/1` confirmed ('By the end of the 16th century ... regular tribute from the Kingdom of Jolof, Waalo, Gajaaga, Diarra ... Saloum' (Cayor only early 17th century)); `/ledger/2` confirmed ('In 1776 the Torodbe overthrew the ruling Denianke Dynasty'); `/ledger/5` confirmed ('Futa Toro was annexed by France in 1859')

Area: no Cliopatria row and no area on the page; the drawn 76,000 km2 is far more than 'a strip of agricultural land along both sides of the Senegal River' and includes Waalo

## bagirmi-sultanate: pass

Tried the 1522 start, the 1805 Wadai sack, the 1893 Rabih conquest and the 1897 protectorate; all confirmed. The page's tributes (Bornu absorbed Bagirmi under Idris Alooma 1571-1602/3, independence under Muhammad al-Amin 1751-1785; Wadai tributary after 1805) are vassal events for the empire-of-kanem and wadai-empire ledgers (routed in cross_checks).

Gaps for a gap-filler:

- `/ledger/1`: c1: Burkumanda's 1635-1665 'influence north to Lake Chad' drawn as a gain of all Hadjer-Lamis (try https://en.wikipedia.org/wiki/Lake_Chad)
- `/ledger/6`: the 1897 treaty made Bagirmi a protectorate ('became a colony in 1902'): a vassal_start 1897 / dissolve 1902 would follow the page more closely than a dissolve in 1897 (try https://en.wikipedia.org/wiki/Bagirmi_Sultanate)

Spot checks: `/ledger/0` confirmed ('emerged from a group of chiefdoms around 1522'); `/ledger/2` confirmed (Wadai invaded in 1805 and 'sacked Massenya, killed the mbang'); `/ledger/4` confirmed (1893: Rabih 'conquered Baguirmi and burnt down its capital Massenya'); `/ledger/6` confirmed (1897 treaty, French protectorate; colony 1902)

Area: no Cliopatria row; no area on the page

## state-of-rabih-az-zubayr: thin

Findings:

- `/keyframe_review/0/correction` (to do, not blocking). The 1890-1891 keyframe (Bamingui-Bangoran) is the same land the dar-al-kuti dossier draws as its own in 1890-1891 (100% overlap), with no vassal relation between them. Evidence: Rabih page: 'In 1890, Rabih was in the Dar al Kuti region'; 'In 1891, Rabih's lieutenant Muhammad al-Sanussi massacred a French expedition'. Gazetteer: rabih_1890 x dar-al-kuti_1890 = 58,673 km2. Fix: Either drop the 1890-1891 keyframe and start the shape in 1892, or record Dar al-Kuti as Rabih's vassal (vassal_start 1890 / vassal_end 1892, mirrored in dar-al-kuti) and leave the land to dar-al-kuti.
- `/keyframe_review/2/correction` (to do, not blocking). The Bornu part of the 1893-1901 shapes (the empire-of-kanem Cliopatria shape) covers 62% of the Mandara kingdom, which no page puts under Rabih. Evidence: Gazetteer: rabih_1893/1897/1900 x mandara-kingdom_1500 = 9,610 km2. Fix: Subtract the mandara-kingdom region from the Bornu part, or note why Mandara is inside.

Gaps for a gap-filler:

- `/ledger/1`: c1: when Rabih left Dar al-Kuti ('until he was defeated by an army sent by the Wadai Sultanate', no year) (try https://en.wikipedia.org/wiki/Dar_al-Kuti)
- `/ledger/7`: c1: the year of the move to Dikwa (try https://en.wikipedia.org/wiki/Dikwa)

Spot checks: `/ledger/0` confirmed ('In 1890, Rabih was in the Dar al Kuti region'); `/ledger/2` confirmed ('In 1892, Rabih defeated a joint Bagirmi-Wadai army ... conquer several Kotoko principalities'); `/ledger/4` confirmed ('battle of Amja, in May 1893'); `/ledger/6` confirmed ('The beginning of Rabih's rule over Bornu would later be dated to 2 October'); `/ledger/10` confirmed ('Fadlallah was killed by the French at Gujba on 23 August 1901')

Area: no Cliopatria row of its own; no area on the page; the 1893-1896 shape (Kotoko disc, Chari-Baguirmi, the Bornu Cliopatria shape) is about 222,000 km2

## mossi-kingdoms: pass

All four checked events confirmed; one block for several kingdoms within the 2-page budget (thin by design). The Songhai overlordship implied by 'the Mossi states reestablished their independence' in 1591 belongs in the songhai-empire ledger (routed).

Gaps for a gap-filler:

- `/keyframe_review`: one block for Tenkodogo, Ouagadougou, Yatenga, Fada N'Gourma, Boussouma and Rizim with no outline; the page's map caption 'Area occupied by Mossi Kingdoms, c. 1530' is the only extent (try https://en.wikipedia.org/wiki/Yatenga)
- `/ledger/0`: c1: the 1050 start (Oubri 'around 1050 to 1090', traditions 11th-15th centuries) (try https://en.wikipedia.org/wiki/Naaba_Oubri)

Spot checks: `/ledger/0` confirmed ('Oubri, who ruled from around 1050 to 1090 CE'); `/ledger/1` confirmed ('Diaba Lompo, who founded the city of Fada N'gourma' (no year, c1 honest)); `/ledger/2` confirmed ('Under the fifth ruler, Komdimie (circa 1170) ... the Kingdom of Yatenga to the north and the Kingdom of Rizim'); `/ledger/3` confirmed ('the French entered the area in 1896 and ignored the treaty of protection')

Area: no Cliopatria row; no area on the page (map caption c. 1530 only)

## kaabu: thin

Gaps for a gap-filler:

- `/keyframe_review/0`: the drawn Kaabu (Gabú, Kolda, Upper and Central River, about 30,000 km2) is smaller than the page's extent: 'centered within modern northeastern Guinea-Bissau, large parts of today's Gambia', extending 'into Koussanar, Koumpentoum, and the Casamance in Senegal' (Bafatá/Oio, Sédhiou, the Tambacounda west and the lower Gambia are missing); mali-empire's 1537 loss to kaabu covers Guinea-Bissau, the Gambia and Casamance, so the two dossiers disagree on the land (try https://en.wikipedia.org/wiki/Kaabu)

Spot checks: `/ledger/0` confirmed (infobox 'Independence from the Mali Empire: 1537'); `/ledger/1` confirmed ('In 1865, at the climax of a long period of on-and-off conflict, Futa Jallon invaded the' Mandinka kingdom); `/ledger/4` confirmed ('Kansala was under Fula control until the Portuguese suppression of the kingdom around the turn of the 20th century'); `/ledger/5` confirmed (infobox 'Battle of Kansala: 1867'; successors Futa Jallon, Fuladu, Portuguese Guinea)

Area: no Cliopatria row; no area on the page; extent narrower than the page's (thin)

## imamate-of-futa-jallon: pass

Tried the 1725/1727 start, the Kaabu war and the 1896 end; all confirmed; the 1867 Gabú gain is mirrored in kaabu. The Fuladu vassalage is recorded here, on the overlord side, as the schema asks.

Gaps for a gap-filler:

- `/ledger/6`: c1: the end of the hold over Fuladu, bridged to 1896; the Fuladu page does not call Fuladu a vassal at all (try https://en.wikipedia.org/wiki/Musa_Molo)

Spot checks: `/ledger/0` confirmed ('Alfa Ba was killed in 1725, however his son Ibrahim Sambegu took over'; infobox 'Established: 1725'); `/ledger/1` confirmed ('defeated the animists at the decisive battle of Talansan in 1727'); `/ledger/5` confirmed ('the Imamate extended its control into Fuladu'); `/ledger/7` confirmed (Timbo entered 'on the 3rd', Porédaka 'On the 14th' (November 1896); infobox 'French protectorate: November 18th 1896' (disestablished 1912, noted by the author))

Area: no Cliopatria row; no area on the page

## kaarta: thin

Findings:

- `/keyframe_review/0/correction` (to do, not blocking). The 150 km Nioro disc overlaps the Diarra disc by about 10,600 km2 for 1650-1855; Diarra is a separate dossier (a vassal only from 1754/1777). Evidence: Gazetteer: kaarta_1650 x diarra_1054 = 10,622 km2 (30% of Diarra). Fix: Subtract the diarra disc (same coordinates as /ledger/2's region) from the Kaarta disc.
- `/ledger/2` (to do, not blocking). The vassalage of Diarra starts 1777 here (Kaarta page) and 1754 on the Diarra page ('conquered and vassalized'); the conflict is not in the notes field of the event. Evidence: Kaarta page: 'vassalizing Diarra in 1777 and Khasso'; Kingdom of Diarra page: 'In 1754, the Bambara kingdom of Kaarta conquered and vassalized the kingdom.' Fix: Keep 1777 or move to 1754 with the Diarra page as source; either way name the other date in /ledger/2's note.

Gaps for a gap-filler:

- `/ledger`: Sira Bo also vassalised Khasso (undated on the page, Sira Bo reigned 1761-1781); the khasso dossier has no Kaarta event (try https://en.wikipedia.org/wiki/Khasso)
- `/ledger/3`: c1: end of the Diarra vassalage, bridged to 1855 (try https://en.wikipedia.org/wiki/Kingdom_of_Diarra)

Spot checks: `/ledger/0` confirmed (infobox 'Massa founds the kingdom: c.1650' (counterpart songhai-empire is the infobox predecessor; Songhai ended 1599)); `/ledger/1` confirmed ('re-established by Sey Bamana Coulibaly, who had fled Segou in 1754'); `/ledger/2` confirmed ('vassalizing Diarra in 1777 and Khasso'); `/ledger/4` confirmed ('He seized Nioro, and put the Faama Mamady Kandian and his entire family to death' (1854 on this page; April 1855 on the Toucouleur page, used and noted))

Area: no Cliopatria row; no area on the page

## kenedougou-kingdom: pass

Tried the capital move, the Sikasso siege, the 1898 fall and the start; all confirmed. The Kong dependency 1737-1825 is recorded by the overlord (kong-empire), as the schema asks. Nit: Bougoula has the same coordinates as Sikasso (proxy).

Gaps for a gap-filler:

- `/ledger/2`: c1: the year of Tieba's Minianka conquest ('Tieba also conquered the Minianka region', no year) (try https://en.wikipedia.org/wiki/Tieba_Traor%C3%A9)

Spot checks: `/ledger/1` confirmed ('moved the capital ... from Bougoula to ... Sikasso in 1877'); `/ledger/3` confirmed ('attacked Sikasso with an army of 12,000 men in April 1887, and laid siege to the city for 15 months'); `/ledger/5` confirmed ('artillery assault against Sikasso's tata on April 15th 1898, and the city fell on May 1'); `/ledger/0` confirmed (infobox 'Established c. 1650')

Area: no Cliopatria row; no area on the page

## kong-empire: fail

Findings:

- `/keyframe_review/1/correction` (BLOCKING). The 1737-1897 keyframe keeps the 100 km Bobo-Dioulasso (Sya) disc for 157 years although gwiriko of this batch takes that land in 1740 (gain cp kong-empire, unmatched here), so the two dossiers both claim about 21,000 km2 for 1740-1897. Evidence: Gwiriko page: 'At Seku's death around 1740, Famagah refused to pay allegiance' and 'seized the area which included Tiefo, Dafin, and Bwamu'; infobox 'Established independence from Kong Empire: 1740'. Gazetteer: kong-empire_1737 x gwiriko_1740 = 20,991 km2 (66% of Gwiriko). The author's report flags the missing loss but the dossier was not changed. Fix: Add loss 1740 cp gwiriko (c2, Gwiriko page; the Kong page has Seku die 'around 1745') with Gwiriko's 1740 region, and a keyframe kong-empire_1740 without the Sya disc (or without the part inside Houet, Tuy and Mou Houn).

Gaps for a gap-filler:

- `/keyframe_review`: the page says the empire 'encompassed much of present-day Burkina Faso' with parts of Mali and Ghana; only the Savanes core and the Sya disc are drawn (try https://en.wikipedia.org/wiki/Kong_Empire)
- `/ledger/2`: c1: start of the Kénédougou dependency, bridged to 1737 (try https://en.wikipedia.org/wiki/K%C3%A9n%C3%A9dougou_Kingdom)

Spot checks: `/ledger/0` confirmed (infobox 'Founding of Kong dynasty by Seku Watara: 1710'; Lasiri Gbambele killed); `/ledger/1` confirmed ('He eventually reached Sya in 1737'); `/ledger/3` confirmed (infobox 'Established independence from Kong Empire: 1825'); `/ledger/4` confirmed (Samory destroyed the city 'either on May 23, 1897' or May 18, 1898 (infobox 1898; 1897 followed with the Wassoulou page))

Area: no Cliopatria row; no area on the page

## sultanate-of-kano: pass

All four checked events confirmed. Kano's tribute to Bornu (under Abdullahi Burja, 1438-52, on this page) is a vassal event for the empire-of-kanem ledger (routed). sokoto-caliphate names 'Sultanate of Kano' as text for its 1807 gain: matched, slug to update there.

Spot checks: `/ledger/0` confirmed (Bagauda took Sheme 'after defeating the rulers in 999 CE'); `/ledger/1` confirmed (Gijimasu (1095-1134) founded a settlement 'at the foot of Dala Hill which would become Kano'); `/ledger/2` confirmed ('By 1200, Kano had extended its rule over all of the chiefdoms in the area apart from Santolo'); `/ledger/3` confirmed (Alwali 'deposed in 1805 and killed in 1807'; Kano 'became an emirate subject to Sokoto' (infobox 999-1805))

Area: no Cliopatria row; no area on the page

## sultanate-of-katsina: thin

Findings:

- `/ledger/1` (to do, not blocking). The Songhai period 1512-1554 is recorded as an occupation (hatched) although the page calls Katsina a vassal; the schema records a vassalage only in the overlord's ledger (vassal_start cp sultanate-of-katsina in songhai-empire), and songhai-empire has neither. Evidence: Katsina Emirate page: 'Askia Muhammad conquered Katsina in 1512, and Katsina essentially became a vassal of Gao'; it 'regained its independence in 1554 following the battle of Karfata against Askia Daud.' Fix: Remove the occupation pair here once songhai-empire carries vassal_start 1512 / vassal_end 1554 cp sultanate-of-katsina (c2, this page); until then keep it and route it.

Gaps for a gap-filler:

- `/ledger/0`: c1: the 1015 start is the regnal list's; the infobox says '1100-15th century' (try https://en.wikipedia.org/wiki/Katsina)

Spot checks: `/ledger/0` confirmed ('Katsina's regnal list dates this to 1015 CE'); `/ledger/1` confirmed ('Askia Muhammad conquered Katsina in 1512' - a vassal, not an occupation); `/ledger/2` confirmed ('regained its independence in 1554 following the battle of Karfata'); `/ledger/3` confirmed (conquest 'in 1805/6 during the jihad of Usman dan Fodio'; Halidu threw himself down a well)

Area: no Cliopatria row; no area on the page

## kingdom-of-kebbi: thin

Findings:

- `/ledger/2` (to do, not blocking). The 1530 'gain' of a 150 km Agadez disc (about 68,500 km2, larger than Kebbi itself) never appears in a keyframe, and both pages call it an occupation; the loss of 1580 is bridged although the Kebbi page ties it to the years after Kanta's death in 1556. Evidence: Kebbi Kingdom page: Kanta 'occupied Agadez, capturing the region from Songhay' (no year); Kebbi lost control after Kanta's death in 1556 when Kano and Katsina backed a rival. Sultanate of Agadez page: 'Agadez was occupied by Kanta's Kebbi empire'. kingdom-of-kebbi_1516 (Kebbi admin1, 39,452 km2) never includes it. Fix: Turn /ledger/2 and /ledger/3 into occupation_start (c1, bridge c. 1530) and occupation_end (c1, about 1556-1560, Kebbi page) cp sultanate-of-agadez; the agadez dossier then records the owner's side.
- `/ledger/1` (to do, not blocking). The vassal region is the gazetteer's whole 'Hausaland' (about 407,000 km2, reaching 17.4 N and so including Aïr), drawing Kano, Katsina, Zazzau, Gobir and Zamfara, all dossiers of this batch, as Kebbi vassals for 125 years at confidence 1; the Kano page mentions no tribute to Kebbi. Evidence: Gazetteer: {region: Hausaland} = 1,610 cells, bbox 3.47..12.0 E, 9.11..17.41 N. Kebbi page: 'exacted tributes from much of Hausaland' (no states, no years). Fix: Name the tributaries the page or a second page supports as separate vassal_start events with their slugs (each with its own region), or drop the event and keep the claim in notes.
- `/identity/capitals/0` (to do, not blocking). Surame (5.2, 12.95), capital 1516-1599, lies outside the only keyframe (Kebbi admin1). Evidence: Capital check against kingdom-of-kebbi_1516; Surame is in present Sokoto State. Fix: Add the Surame-Leka area (a disc or the western Sokoto LGAs) to the keyframe, or say the capital is outside the proxy.

Gaps for a gap-filler:

- `/ledger/4`: c1: the end of the Hausa tributes, bridged to 1650 ('ceased to be a great power' by the mid-17th century) (try https://en.wikipedia.org/wiki/Kebbi_Emirate)

Spot checks: `/ledger/0` confirmed ('Kanta Kuta, ruler of Leka, revolted against the dendi fari' in 1516-7); `/ledger/2` confirmed ('occupied Agadez, capturing the region from Songhay' (no year; c1 honest; see fix)); `/ledger/3` confirmed (loss after Kanta's death in 1556 (the dossier's 1580 bridge is later than the page suggests)); `/ledger/5` confirmed ('In 1808, Abdullahi dan Fodio defeated Kebbi's forces' (capture of Birnin Kebbi undated))

Area: no Cliopatria row; no area on the page

## sultanate-of-agadez: pass

All four checked events confirmed. Type mismatch to route: songhai-empire records Aïr as a gain (1515, cp 'Sultanate of Agadez') where this dossier records a Songhai occupation 1516-1591; the Kebbi occupation (both pages) is recorded by kebbi as a gain and not here. The 1405-1449 overlap with the gobir Aïr disc is gobir's.

Spot checks: `/ledger/0` confirmed ('It was founded in 1405 by the Tuareg'); `/ledger/1` confirmed ('conquered by the Songhai Empire in 1500'; 'Circa 1516-7 the Songhai Empire successfully campaigned against Agadez'); `/ledger/2` confirmed ('After the defeat of the Songhai kingdom in 1591, the Agadez Sultanate regained its independence'); `/ledger/3` confirmed ('The sultanate came under French suzerainty in 1906')

Area: no Cliopatria row; no area on the page

## sultanate-of-gobir: fail

Findings:

- `/keyframe_review/2/correction` (BLOCKING). The 1756-1808 keyframe is the Sokoto admin1 alone, so Gobir's own country (Maradi, held since 1450) vanishes in 1756 with no loss event; the page has the Gobir heartland intact (Goran Rami near Sabon Birni, Tibiri near Maradi built in 1836 by the surviving court). Evidence: Gazetteer: sultanate-of-gobir_1450 (Maradi, 155 cells) and _1756 (Sokoto, 133 cells) share no cell; the ledger has only the 1756 gain from zamfara. Gobir page: Babari 'founded Alkalawa' on Zamfara's farmlands; after 1808 'The state was then partially absorbed into Sokoto' and Mayaki built 'a new capital at Tibiri, about 10 km north of Maradi'. Fix: Correction for 1756-1808: union of the Maradi region and the Sokoto admin1 (the 1756 gain); the 1808 loss then takes Sokoto only and the dissolve both, or the dossier continues at Tibiri.
- `/keyframe_review/0/correction` (to do, not blocking). The 1150-1449 Aïr disc is the same 150 km Agadez disc as sultanate-of-agadez from 1405, so both states claim the Aïr in 1405-1449 (flagged in the notes, not fixed). Evidence: Gazetteer: gobir_1150 x agadez_1405 = 68,536 km2 (100%). Gobir page: 'due to constant pressure from the Tuaregs since the 12th century' the Gobirawa 'were forced to move southwards'; the Tuareg set up the Sultanate of Agadez 'early in the 15th century'. Fix: End the Aïr keyframe at 1404 (loss 1405 cp sultanate-of-agadez, c1) or shrink it to southern Aïr outside the Agadez disc.

Gaps for a gap-filler:

- `/ledger/2`: c1: the 1450 move to the Maradi country; the page gives Birnin Lalle 1450-1600 in the infobox and 'early 18th century' in the text, Maigali and Goran Rami in between (try https://en.wikipedia.org/wiki/Tibiri_(Maradi))
- `/ledger/6`: Gobir survived at Tibiri (1836) as a rump state; the dossier ends in 1808 (try https://en.wikipedia.org/wiki/Gobir)

Spot checks: `/ledger/0` confirmed (infobox first capital Asben 1150-1450; 'Founded by the Hausa in the 12th century'); `/ledger/1` confirmed (infobox Birnin Lalle 1450-1600 (text: early 18th century, noted by the author)); `/ledger/3` confirmed (Birnin Zamfara ravaged 'about 1756' (Barth) or 1762; Babari founded Alkalawa); `/ledger/5` confirmed (Alkalawa fell in October 1808 (infobox 3 October), Yunfa killed)

Area: no Cliopatria row; no area on the page

## dendi-kingdom: thin

Findings:

- `/wars/0` (to do, not blocking). The war of 1592-1594 lies before the state's start (1599), the one validator warning in the batch. Evidence: validate_dossier warning: 'span 1592..1594 lies outside the state's life 1599..1901'. Dendi Kingdom page: 'In 1594 Mahmud was forced to discontinue the war and retreated'. Fix: Move the war to songhai-empire's wars (the Askia court at Lulami is songhai-empire's until 1599) or start the state in 1591/1592 with songhai-empire's agreement.

Gaps for a gap-filler:

- `/keyframe_review/0`: the page names Dendi's centres as Gaya (Niger), Kamba (Nigeria) and Malanville (Benin) and gives no extent; the shape is the whole Tillabéri region (most of it the Sahel north and west of Niamey) plus a Gaya disc, which also overlaps kebbi by about 13,400 km2 (try https://en.wikipedia.org/wiki/Dendi_people)

Spot checks: `/ledger/0` confirmed (Nuh's war ended 1594; Nuh deposed in favour of Harun (1599 in the dossier, from the page)); `/ledger/1` confirmed ('In 1901, the French deposed the last askia of Dendi'); `/ledger/2` confirmed ('survived the fall of the Empire as a kingdom until 1901')

Area: no Cliopatria row; no area on the page; the 134,000 km2 stand-in is likely far too large

## nupe-kingdom: pass

Gaps for a gap-filler:

- `/ledger/1`: 1835 appears only in the page's section headings; the text has Ma'azu die in 1818 and the kingdom 'came under the control of the Gwandu Emirate' (no year), Masaba in 1841; sokoto-caliphate has the gain in 1808. A second page should settle the year (try https://en.wikipedia.org/wiki/Bida_Emirate)

Spot checks: `/ledger/0` confirmed (heading 'Nupe Kingdom (1531-1835)'; text 'established in the middle of the 15th century'); `/ledger/1` confirmed (heading 1835; 'came under the control of the Gwandu Emirate' (undated)); `/ledger/2` confirmed ('Nupe Emirate (1835-1901)' heading)

Area: no Cliopatria row; no area on the page

## cayor: thin

Findings:

- `/ledger/1` (applied by the reviewer). Confidence 2 for a 1549 gain of Baol that the page gives only as Amary Ngone's personal union, with no year, and that the same page contradicts for the next 150 years (Baol had its own Teigne, Lat Sukaabe Fall, who took Cayor in 1693; Cayor 'annexed the Kingdom of Baol' only under Maïsa Teindde Ouédji in the 18th century). Evidence: Cayor page: 'he thus became the first Damel-Teigne ruling over both Cayor and Baol' (no year); 'In 1693, He took over Cayor and declared himself the Damel-Teigne'; Cayor annexed Baol under Maïsa Teindde Ouédji, 'Baol regained its independence in 1756'. Fix: Confidence lowered to 1. The author should move the annexation to Maïsa Teindde Ouédji's reign (18th century, year from a ruler page) and give Baol its own keyframe 1549-that year (see baol).

Gaps for a gap-filler:

- `/keyframe_review/0`: the year Maïsa Teindde Ouédji annexed Baol (the union of 1549 was personal and Baol had its own Teigne by the 1690s); the 1549-1755 Diourbel strip should be Baol's until then (try https://en.wikipedia.org/wiki/Lat_Sukaabe_Fall)
- `/ledger/3`: the lead dates the end 1876, the body 6 October 1886; the infobox 'French colonization: 1886 1879' is garbled (try https://en.wikipedia.org/wiki/Lat_Jor)

Spot checks: `/ledger/0` confirmed (reign list Amari Fall 1549-1593; Danki 1549); `/ledger/1` confirmed (first Damel-Teigne ruling both, no year (confidence lowered)); `/ledger/2` confirmed ('Baol regained its independence in 1756'); `/ledger/3` confirmed ('negotiations in Tivaouane on October 6, 1886'; 'ceased to exist as an independent, united state')

Area: no Cliopatria row; no area on the page; Thiès + Dakar is about 7,100 km2 and the author notes the Ndiambour coast is not drawn

## bilala-kingdom: thin

Findings:

- `/keyframe_review/0` (to do, not blocking). The notes say the Bilala page dates nothing before c. 1630 and that the Kanem keyframe 'follows the Bilala page', but the page itself has Bornu recapture Kanem in the early 16th century and keep the Bilala as governors of a province; empire-of-kanem records a 1500 gain cp 'Bilala' that this ledger does not answer, so both dossiers claim about 34,000 km2 of Kanem for 1500-1630. Evidence: Bilala page: 'mai Idris III Katagarmabe captured Kanem in the early 16th century, more than a century after the Sayfawa lost the region', and he let the Bilala keep governing Kanem as a province. empire-of-kanem /ledger/7: 1500 gain cp Bilala (the part of Kanem inside the 1487 Bornu shape). Fix: Record the early-16th-century change from this page (loss 1500 cp empire-of-kanem for the part Bornu holds, c2), or agree with the empire-of-kanem owner that it becomes a Bornu vassal_start cp bilala-kingdom with the land left to the Bilala; correct the notes.

Gaps for a gap-filler:

- `/ledger/0`: c1: the late-14th-century start, bridged to 1380 from empire-of-kanem (try https://en.wikipedia.org/wiki/Kanem%E2%80%93Bornu_Empire)
- `/ledger/3`: c1: the Yao sultanate's founding year (placed at the 1630 loss of Kanem) (try https://en.wikipedia.org/wiki/Yao,_Chad)

Spot checks: `/ledger/1` confirmed ('In the late 14th century, the Bilala captured the Sayfawa capital of Njimi' (no year, c1 honest)); `/ledger/2` confirmed ('In around 1630, the Wadai Sultanate drove the Bilala out of Kanem'); `/ledger/3` confirmed (re-established 'in the lands around Lake Fitri', 'an area roughly 5,000 km2 in size'); `/ledger/4` confirmed ('In May 1909, the region around Lake Fitri, including Yao, was occupied and colonised by France')

Area: no infobox; the text's 'roughly 5,000 km2' for the Fitri sultanate matches the 40 km Yao disc

## waalo: thin

Findings:

- `/keyframe_review/0/correction` (to do, not blocking). Saint-Louis admin1 includes the Podor department, the Toro province of Futa Toro, and the notes' claim that the overlap with futa-toro is slight is wrong: futa-toro's shape covers all of Waalo (19,979 km2, 100%). Evidence: Gazetteer overlap futa-toro_1513/1776 x waalo_1287 = 19,979 km2. Waalo page: 'included parts of the valley proper and areas north and south, extending to the Atlantic Ocean'; Nder on Lac de Guiers. Fix: Draw Waalo as the delta and Lac de Guiers (Saint-Louis admin1 west of about -15.0, i.e. minus the Podor stretch) and correct the note; the main fix is in futa-toro.

Spot checks: `/ledger/0` confirmed ('associated with the rule of the first king, the semi-legendary Ndiadiane Ndiaye, in 1287'); `/ledger/1` confirmed ('the French finally conquered the kingdom in 1855'; infobox 'French colonization: 1855')

Area: no Cliopatria row; no area on the page

## baol: thin

Gaps for a gap-filler:

- `/keyframe_review`: Baol has no keyframe for 1549-1755 (207 of its 345 years) because the Damel-Teigne personal union is drawn as annexation by Cayor; the Cayor page has Baol with its own Teigne (Lat Sukaabe Fall took Cayor in 1693) and the annexation only under Maïsa Teindde Ouédji in the 18th century. A keyframe baol_1549 (Diourbel) up to the real annexation year is needed, as the author's notes already propose. The Baol page itself: 'In 1697 Teigne Lat Sukaabe Fall conquered Cayor' (reign 1697-1719). (try https://en.wikipedia.org/wiki/Lat_Sukaabe_Fall)
- `/ledger/1`: c1: the year of the union/annexation; the Baol page gives none and Amary Ngoné's reign is c. 1560-1593 there (try https://en.wikipedia.org/wiki/Cayor)

Spot checks: `/ledger/2` confirmed ('Baol regained its independence in 1756' (Cayor page, same claim as the Baol page quote)); `/ledger/0` confirmed (Danki 1549 ended Jolof hegemony over Baol); `/ledger/3` confirmed (infobox 'French colonization 1894'; Tanor Gogne to '3 July 1894'; 'complete control' 1895); `/ledger/1` confirmed ('reigning over both kingdoms in a personal union' (Amary Ngone Sobel Fall c. 1560-1593): a union, not an annexation (c1 honest))

Area: no Cliopatria row; no area given; Diourbel admin1 about 5,600 km2, the Mbour coast not drawn (noted)

## saloum: pass

Tried: the 1494 founding, the 1566 north-bank extension, the 1867 end; the Jolof overlap of 1494-1519 is jolof-empire's to fix (Saloum page: 'never a part of the empire'). The Denianke tribute is futa-toro's to record per slug (overlord side).

Spot checks: `/ledger/0` confirmed ('in the later part of the 15th century (c. 1494)'); `/ledger/1` confirmed ('By 1566 ... Lat Ciloor Bajaan' 'extended Saloum's power to the north bank of the Gambia'); `/ledger/3` confirmed (1867, Maba 'defeated and killed' invading Sine); `/ledger/4` confirmed ('After Maba's defeat, Saloum was incorporated into the colony of Senegal' (no year; c2 honest))

Area: no Cliopatria row; no area on the page

## sine: fail

Findings:

- `/ledger/2` (BLOCKING). Sine is held as a sovereign state until August 1969, so it is drawn on top of French Senegal through the colonial period and over independent Senegal 1960-1969, although its own page speaks of 'the colonial period'. Evidence: Kingdom of Sine page: the rulers 'retained their title (Maad a Sinig) throughout the colonial period'; Sine 'was very reluctant to grow groundnut for the French market, in spite of French colonial directives'; infobox status 'Non-sovereign monarchy within Senegal'. The 1969 date is the end of official recognition of the monarchy, not of sovereignty. Fix: End the state at the French takeover (a page that dates it: History of Senegal, Kumba Ndoffene Famak Joof's successors, or the French West Africa page); if no page dates it, end it at a bridging year with confidence 1 and counterpart french-africa, not 1969 with counterpart 'independent Senegal'.
- `/ledger/1` (to do, not blocking). The 1520 event is a 'gain' of all of Fatick from jolof-empire although the dossier already holds Fatick from 1335; it is the end of a vassalage, which the schema records only in the overlord's ledger (vassal_end cp sine in jolof-empire). Evidence: Kingdom of Sine page: Ndiadiane Ndiaye's election made 'Sine a vassal of the Jolof Empire'; Sine and Saloum 'were the first to leave the Jolof Empire, at least twenty-nine years before the famous Battle of Danki in 1549'. Fix: Delete /ledger/1 (or keep it as a note); jolof-empire replaces its gain/loss with vassal_start/vassal_end cp sine.
- `/ledger/0` (to do, not blocking). The 1335 found names counterpart kaabu, whose dossier starts in 1537. Evidence: kaabu.json start 1537 (found from mali-empire). The page: Maysa Wali fled Kaabu 'after a battle in 1335' in oral tradition. Fix: Counterpart nobody (the Guelowar came from Kaabu, which was then a Mali province: mali-empire if anything).

Spot checks: `/ledger/0` confirmed (infobox 'ca. 1335'); `/ledger/1` confirmed ('at least twenty-nine years before the famous Battle of Danki in 1549' (but a vassalage, see fix)); `/ledger/2` confirmed ('did not lose official recognition until 1969 after the death of Maad a Sinig Mahecor Joof' - recognition of the monarchy, not sovereignty)

Area: no Cliopatria row; no area on the page

## fuladu: pass

All four checked events confirmed. The imamate-of-futa-jallon vassal_start 1867 cp fuladu is recorded on the overlord side as the schema asks; the Fuladu page itself does not call Fuladu a vassal.

Spot checks: `/ledger/0` confirmed (infobox established 1867; 'the creation of Fuladu, stretching from the upper Casamance River to northeastern Guinea-Bissau'); `/ledger/2` confirmed ('In 1874 he established his capital in Ndorna'); `/ledger/3` confirmed (British section annexed 'into the Gambia Colony and Protectorate in 1902'); `/ledger/4` confirmed ('In May 1903 the French attempted to bring Musa to heel'; 'Fuladu ceased to exist as an independent power')

Area: no Cliopatria row; no area on the page; NE Guinea-Bissau not drawn (noted by the author)

## bundu: fix

Findings:

- `/ledger/0/counterpart` (applied by the reviewer). The found event names its counterpart 'Gajaaga' instead of the slug gajaaga, whose dossier (this batch) records the matching 1690 loss cp bundu; the same in /wars/0/belligerents. Evidence: gajaaga.json /ledger/1: 1690 loss cp bundu. Bundu (state) page: Bundu was 'a sparsely populated part of the kingdom of Gajaaga' in the 17th century; 'In 1690, Fula Torodbe cleric Malick Sy came to the region'. Fix: Counterpart and war belligerent set to 'gajaaga'. Re-validated: 0 errors, 0 warnings.

Gaps for a gap-filler:

- `/ledger/1`: the 1858 end is the infobox's; the body has Bundu become 'a French protectorate dependent on the colony of Senegal' (no year), French control 'effectively complete' only after the 1885-87 jihad, and the last almamy dying in 1902 (try https://en.wikipedia.org/wiki/Mahmadu_Lamine)
- `/keyframe_review/0`: the page's own box includes the Bakel stretch that the gajaaga strip also draws (about 3,000 km2 overlap) and the Kédougou corner the tukulor Bambuk proxy uses (about 2,800 km2, 1854-1858) (try https://en.wikipedia.org/wiki/Bundu_(state))

Spot checks: `/ledger/0` confirmed (infobox 'Established: 1690'; Malick Sy came 'In 1690'); `/keyframe_review/0` confirmed ('between 13 and 15 degrees north latitude, and 12 and 13 degrees west longitude'); `/ledger/1` confirmed (infobox 'Disestablished: 1858'); `/wars/1` confirmed ('In 1851 Saada Amadi died and a civil war broke out'; Umar Tall took advantage)

Area: no Cliopatria row; no area; the page's lat/lon box cut to Senegal is used

## damagaram: pass

All four checked events confirmed and the area agrees with the page. The early Bornu vassalage ('at the beginning a vassal state of the decaying borno') belongs in the empire-of-kanem ledger (routed).

Gaps for a gap-filler:

- `/ledger/2`: c1: the 1830s conquest bridged to 1830 (the page gives the decade) (try https://en.wikipedia.org/wiki/Tanimoune_Dan_Souleymane)

Spot checks: `/ledger/0` confirmed ('founded in 1731 (near Mirriah, modern Niger)'); `/ledger/1` confirmed ('the moving of the capital of Damagaram there in 1736'); `/ledger/2` confirmed ('In the 1830s ... conquered the Myrria kingdom, the Sassebaki sultanates (including Zinder)'); `/ledger/3` confirmed ('on 30 July at the Battle of Tirmini, 10 km from Zinder ... took Damagaram's capital' (1899))

Area: no infobox; the text's 'some 70,000 square kilometers' (mid-19th century) is matched by the 150 km Zinder disc of 1830-1899

## gwiriko: thin

Findings:

- `/identity/capitals/0` (to do, not blocking). Bobo-Dioulasso is the capital from 1714, but the 1714-1739 keyframe is Mou Houn only, so the capital lies outside the state; the Bobo-Dioulasso page has Sia conquered only in the late 1730s. Evidence: Capital check: Bobo-Dioulasso (-4.29, 11.18) is not in gwiriko_1714 (Mou Houn). Gwiriko page: kingdom founded 'in the bend of the Mouhoun River' about 1714; it does not say when Bobo-Dioulasso became the capital. Fix: Start the Bobo-Dioulasso capital in 1740 (with the Houet gain) and give 1714-1739 a Mouhoun-bend proxy, or mark the 1714-1739 capital unknown.
- `/keyframe_review/1` (to do, not blocking). The 1740 shape (Houet, Tuy, Mou Houn) is held unchanged to 1897 although the page says the state collapsed after 1839 and its peoples became independent. Evidence: Gwiriko page: after Diori Ouattara's death in 1839 'the state collapsed, and the Tiefo, Bobo Joola, Bolon, and other peoples became independent.' Fix: Add loss 1839 cp nobody (c2) of Tuy and Mou Houn (or the Tiefo and Bolon lands) and a keyframe gwiriko_1839 reduced to the Bobo-Dioulasso area (Houet), which the Watara held until 1897.

Spot checks: `/ledger/0` confirmed ('In about 1714, Seku's brother Famagan Ouattara established the Kingdom of Gwiriko in the bend of the Mouhoun River'); `/ledger/1` confirmed ('At Seku's death around 1740 ... seized the area which included Tiefo, Dafin, and Bwamu'); `/ledger/3` confirmed (infobox 'French colonial control: 1897'; 'in 1897, Pintieba Ouattara was installed ... by the French')

Area: no Cliopatria row; no area on the page

## pashalik-of-timbuktu: fail

Findings:

- `/ledger/0` (BLOCKING). The pashalik is founded in March 1591 holding Gao, Timbuktu and Djenné as its own land, but its own infobox calls it a 'Moroccan Governorate (1591-1621)' and saadi-sultanate already gains the same land in 1591-1592 and records the pashalik as its vassal only from 1618: the two dossiers both claim about 83,000 km2 in 1591-1618, and the Saadi vassal_start of 1618 has no counterpart event here. Evidence: Pashalik of Timbuktu page infobox: 'Moroccan Governorate (1591-1621)', 'Moroccan Vassal (1621-1826)'; 'Sultan Moulay Zidan relinquished direct control over the Sudan territories in 1618'. saadi-sultanate /ledger/19 (1591 gain cp songhai-empire, Timbuktu and Gao), /ledger/20 (1592 Djenné), /ledger/25 (1618 vassal_start cp pashalik-of-timbuktu). Gazetteer: saadi-sultanate 1595 x pashalik_1591 = 82,698 km2. Fix: Start the state when Morocco let go: found 1618 (c2; 1612 or 1621 in the notes) as a split from saadi-sultanate (counterpart saadi-sultanate), keep 1591-1617 in the notes, and agree the Saadi loss with its owner; the Saadi vassal_start 1618 then stands as the overlord's record.
- `/keyframe_review/1/correction` (to do, not blocking). The 1770-1833 keyframe keeps a 100 km Djenné disc and a 120 km Timbuktu disc to 1833 although the page ends Arma rule over Timbuktu in 1737 and makes the pashalik a Tuareg tributary from 1787, and the existing Bamana (1769-1818) and Massina (1818-1833) dossiers draw much of the same land. Evidence: Pashalik page: 'The rule of the Arma over Timbuktu lasted until 1737'; 'in 1787 they entered Timbuktu and made the Pashalik their tributary'. massina-empire /ledger/0 (1818, Djenné and Massina) and /ledger/1 (1826, Timbuktu); bamana-empire /ledger/1, /3, /5 (Timbuktu 1748, 1752, 1769, cp pashalik-of-timbuktu, unanswered here). Gazetteer: bamana-empire 1815 x pashalik_1770 = 50,074 km2; massina-empire 1830 x pashalik_1770 = 50,074 km2. Fix: Drop Djenné by 1818 (loss cp massina-empire) and Timbuktu by 1826 (loss cp massina-empire), and either answer bamana's 1748/1752/1769 Timbuktu events or record why not; or end the state earlier on the page's 1737.

Spot checks: `/ledger/0` confirmed ('It was formed after the Battle of Tondibi'; infobox established 1591 (but 'Moroccan Governorate (1591-1621)')); `/ledger/1` confirmed (Timbuktu 'captured ... on May 30th', the official capital); `/ledger/2` confirmed ('The Moroccan army conquered Djenné in 1592'); `/ledger/3` confirmed ('In about 1770, the Tuareg took possession of Gao'); `/ledger/4` confirmed (infobox disestablished 1833, succeeded by the Caliphate of Hamdullahi (body silent))

Area: no Cliopatria row; no area on the page; three discs as stand-ins

## emirate-of-trarza: pass

Tried the 1640 start, the 1902 protectorate and the wars; all confirmed. Influence south of the river ('raided and briefly conquered or backed political factions' in Cayor, Djolof and Waalo) is undated and rightly not drawn.

Spot checks: `/ledger/0` confirmed (infobox 'Confederation founded: 1640'); `/ledger/1` confirmed (infobox '15 Dec 1902 French protectorate'); `/wars/1` confirmed ('At the Battle of Jubuldu on 25 February 1855, the French defeated a combined Waalo and Moorish force')

Area: no Cliopatria row; no area on the page

## emirate-of-brakna: pass

Gaps for a gap-filler:

- `/ledger/0`: c1: the founding year (infobox 'Confederation founded: 17th century'; after the Char Bouba war 1673-77) (try https://en.wikipedia.org/wiki/Char_Bouba_war)

Spot checks: `/ledger/0` confirmed ('Char Bouba war: 1673-77'; victory 'strengthened them enough to establish the emirates'); `/ledger/1` confirmed (infobox 'Declared a French protectorate: 1902'); `/wars/0` confirmed ('Brakna and Trarza fought a war from 1720-22')

Area: no Cliopatria row; no area on the page

## dar-al-kuti: thin

The 28 August 1897 protectorate (page) belongs in french-africa's ledger as a vassal_start cp dar-al-kuti; Wadai's tributary tie until 1890 in wadai-empire's (both routed).

Gaps for a gap-filler:

- `/ledger/1`: c1: the 1890 'gain' of Nana-Grébizi, Ouham and Ouham-Pendé (about 110,000 km2) rests on the page's 'sphere of influence' covering 'much of the modern Central African Republic' with no region or year; Ouham-Pendé on the Cameroon border is a guess. Rabih installed Sanussi in 1890, so the 1890-1891 overlap with state-of-rabih-az-zubayr should become a Rabih vassal_start cp dar-al-kuti (Rabih's ledger) (try https://en.wikipedia.org/wiki/Muhammad_al-Sanusi_(Dar_al-Kuti))
- `/identity/capitals/1`: Chá and N'Délé share coordinates; the page has Chá destroyed in October 1894 and an itinerant court 'for two years' before N'Délé (about 1896, not 1894) (try https://en.wikipedia.org/wiki/N%27D%C3%A9l%C3%A9)

Spot checks: `/ledger/0` confirmed ('in 1830 settled in a still more southerly frontier region, Bilad al-Kuti'); `/ledger/1` confirmed (Rabih installed Sanussi in 1890; 'sphere of influence' over 'much of the modern Central African Republic' (influence, c1)); `/ledger/2` confirmed ('until 17 December 1912, when Ouanda Djallé fell to Captain Souclier')

Area: no Cliopatria row; no area on the page

## khasso: thin

Findings:

- `/ledger/1` (to do, not blocking). The c. 1800 split uses the whole Khasso strip as its region and names no successor, yet the keyframe keeps the whole strip to 1880: read literally, all of Khasso leaves in 1800. Evidence: Khasso page: Khasso 'fragmented into five smaller states' after Demba Séga's death: Dembaya (capital Médine), Séro, Almamya (Silatiguiya), Diadiéya and Guimbaya; in September 1855 Faidherbe 'extended French protection' over the 'Khasso Confederation'. Fix: Keep the confederation as the state and move the fragmentation into the notes (or record splits of the four states other than Dembaya with their own regions, if a page locates them).

Gaps for a gap-filler:

- `/ledger`: Kaarta's sack of Kouniakary (after 1796, undated) and Sira Bo's vassalisation (Kaarta page) are the overlords' to record; Umar Tall's submission of the Khasso kings (November 1854) is tukulor-empire's (try https://en.wikipedia.org/wiki/Kaarta)

Spot checks: `/ledger/0` confirmed (Fula 'won their independence in battle at Toumbifara, near Bafoulabe' in 1681; Séga Doua (r. 1681-1725)); `/ledger/1` confirmed (infobox split into five kingdoms around 1800); `/ledger/2` confirmed ('assimilated into French Sudan in 1880'); `/keyframe_review/0` confirmed ('roughly from Kayes to Bafoulabe', a strip 'at most 60 km wide')

Area: no Cliopatria row; the page's 60 km strip from Kayes to Bafoulabé is drawn

## gajaaga: thin

Findings:

- `/ledger/2/region` (applied by the reviewer). The 1855 loss took the whole kingdom although the keyframe keeps it to 1857 and the 1858 loss takes the whole kingdom again; the page names only Bakel (and Medine, which is in Khasso) for 1855. Evidence: Gajaaga page: 'In 1855 he annexed Bakel and Medine, where he built another fort'; 'In 1858 they annexed half of Gooy and made the rest a protectorate.' Fix: Region narrowed to a 25 km disc at Bakel (-12.46, 14.9) with the page's words; reviewer note appended. Re-validated: 0 errors, 0 warnings.
- `/keyframe_review/0` (to do, not blocking). The 1690 loss of the Bundu box is land the only keyframe (1000-1857) never drew, and the Gajaaga strip overlaps the Khasso strip round Kayes (about 5,800 km2, 43% of Khasso, 1681-1857). Evidence: Gazetteer: gajaaga_1000 x khasso_1681 = 5,817 km2; bundu's region is outside gajaaga_1000 except the Bakel corner. Bundu page: Bundu was 'a sparsely populated part of the kingdom of Gajaaga' in the 17th century. Fix: Add a keyframe gajaaga_1000 (to 1689) that includes the Bundu box, and end the strip downstream of Kayes (e.g. east edge -11.6) so it meets Khasso instead of covering it.

Gaps for a gap-filler:

- `/ledger/0`: c1: start bridged to 1000 (infobox 'before 1000CE') (try https://en.wikipedia.org/wiki/Soninke_people)

Spot checks: `/ledger/1` confirmed ('Malick Sy came to Gajaaga ...'; the tunka gave him a town and influence over Bundu (1690 is on the Bundu page)); `/ledger/2` confirmed ('In 1855 he annexed Bakel and Medine' (region narrowed, see fix)); `/ledger/3` confirmed ('In 1858 they annexed half of Gooy and made the rest a protectorate'); `/wars/0` confirmed ('a 1750 invasion by Kaarta and Khasso which, though defeated')

Area: no Cliopatria row; no area on the page

## mandara-kingdom: pass

Confirmed. The Bornu installation of 1614 ('Bornu thus attained an influential position over Mandara') is empire-of-kanem's to record; the 62% overlap with Rabih's Bornu shape is Rabih's.

Gaps for a gap-filler:

- `/ledger/1`: c1: the Fulani contest 1893-1902 (the page says it 'finally fell to them in 1893' but also has Dulo destroyed by Muhammad Ahmad's army in 1895 or 1896 and the kingdom continuing) (try https://en.wikipedia.org/wiki/Adamawa_Emirate)

Spot checks: `/ledger/0` confirmed ('founded shortly before 1500 by a female ruler named Soukda'; infobox c. 1500); `/ledger/1` confirmed ('faced a setback in 1809'; 'finally fell to them in 1893'); `/ledger/3` confirmed ('In 1902, the kingdom was conquered by Germany')

Area: no Cliopatria row; no area on the page

## kwararafa: thin

Findings:

- `/ledger/2` (to do, not blocking). The 1810 loss to the Chamba takes the whole state (Taraba and Benue), yet the only keyframe keeps all of it to 1840, the capital Wukari is held 1820-1840 and the dissolve of 1840 again hands over the whole region: the ledger contradicts the keyframe for 30 years. Evidence: Kwararafa page: 'A Chamba invasion forced the last king, Adi Matswen (r. 1780-1810), into exile'; 'a Jukun dynasty at Wukari had taken control of the remains of the Kwararafa state'; infobox end 'c. 1840'; body 'had collapsed by the early 19th century'. kwararafa_1300 runs 1300-1840 unchanged. Fix: Either make the 1810 event a partial loss (the Chamba lands, c1) with a reduced keyframe round Wukari for 1810-1840, or end the state at the Chamba invasion (dissolve 1810, successor a Wukari/Jukun dossier) and drop the 1840 date.

Gaps for a gap-filler:

- `/ledger/0`: c1: the start (infobox 'c. 13th/14th/15th century'), bridged to 1300 (try https://en.wikipedia.org/wiki/Jukun_people)
- `/keyframe_review/0`: Taraba plus Benue (about 99,000 km2) is a stand-in with no support on the page; the tributes the page names (to Zazzau, Kano, Bornu) belong in those ledgers (try https://en.wikipedia.org/wiki/Wukari)

Spot checks: `/ledger/1` confirmed ('In 1380, possibly immediately after the conquest, the centre of Kwararafa shifted to Tagara'); `/ledger/2` confirmed (Chamba invasion, Adi Matswen (r. 1780-1810) exiled (no year for the invasion)); `/ledger/3` confirmed (infobox end 'c. 1840')

Area: no Cliopatria row; no area on the page

## zazzau: pass

Confirmed the 1536 start and the 1805 end. sokoto-caliphate dates the gain 1809 (as part of a text counterpart 'Hausa kingdoms of Zamfara and Zazzau'): routed as a 4-year mismatch.

Gaps for a gap-filler:

- `/ledger`: Amina's campaigns 'established a tributary region including the kingdoms of Kano and Katsina' (undated; Zazzau's own vassal events cp sultanate-of-kano and sultanate-of-katsina at c1); the Kaduna admin1 is much larger than the city-state (try https://en.wikipedia.org/wiki/Amina)

Spot checks: `/ledger/0` confirmed ('Zazzau is thought to have been founded in or about 1536'); `/ledger/1` confirmed ('In 1805 it was captured by the Fulani'); `/ledger/2` confirmed (emirate continues; 'British forces led by Frederick Lugard took the city in 1901')

Area: no Cliopatria row; the infobox area field is empty

## zamfara: pass

The page has Zamfara revolt against its overlord Kebbi c. 1715 while kebbi ends its Hausa tributes in 1650 (both c1); routed to kebbi.

Gaps for a gap-filler:

- `/ledger/0`: c1: start bridged to 1300 (first ruler Dakka I 'before 1300') (try https://en.wikipedia.org/wiki/Dutsi)
- `/ledger/2`: c1: the year Sokoto absorbed Zamfara ('in the 19th century'); 1809 follows the sokoto-caliphate dossier (try https://en.wikipedia.org/wiki/Fulani_War)

Spot checks: `/ledger/0` confirmed (infobox 'before 1300: Dakka I (first)'; settled at Dutsi); `/ledger/1` confirmed (destruction of Birnin Zamfara 'around 1756' (Barth), 1762 by others); `/ledger/2` confirmed (absorbed by Sokoto 'in the 19th century' (c1 honest))

Area: no Cliopatria row; no area on the page

## jolof-kingdom: pass

Tried the 1549 start, the 1865 Maba occupation and the 1890 end; all confirmed. The 41% overlap with futa-toro is futa-toro's shape error; the Denianke tribute (1599-1776) is futa-toro's to record per slug.

Spot checks: `/ledger/0` confirmed ('Jolof was reduced to a kingdom' after Danki 1549); `/ledger/1` confirmed (Warkhokh 'entered ... in July' 1865); `/ledger/2` confirmed ('a rebellion in Rip forced him to leave Jolof in October'); `/ledger/3` confirmed (Dodds 'marched on Yang-Yang in May 1890', 'installed a puppet buurba and officially established a protectorate over Jolof, ending its independence')

Area: no Cliopatria row; no area on the pages

## diarra: pass

Gaps for a gap-filler:

- `/keyframe_review/0`: the disc is a coordinate stand-in ('centered around the town of Diarra', Kingui/Kaniaga) and overlaps the kaarta and tukulor Nioro discs; the page's overlordships (Sosso and Mali 'beginning in the early 13th century', Songhai fealty after 1512, Kaarta 1754, the Denianke tribute) belong in the overlords' ledgers and are routed in cross_checks (try https://en.wikipedia.org/wiki/Kingdom_of_Diarra)
- `/keyframe_review/0`: the Diarra disc lies wholly inside the mali-empire Cliopatria shapes (1300, 1400) and the songhai-empire shapes (1520, 1580): both dossiers draw the land as their own while Diarra's page makes it a vassal; to be settled with those owners (vassal_start cp diarra and the land left to Diarra) (try https://en.wikipedia.org/wiki/Kingdom_of_Diarra)

Spot checks: `/ledger/0` confirmed (infobox 'Established 1054'; 'Founded in the 11th century'); `/ledger/1` confirmed ('Biranté Karounga Diawara, was captured and executed by Omar Saidou Tall on May 31, 1860'); `/ledger/2` confirmed (succeeded by the Toucouleur Empire)

Area: no Cliopatria row; no area on the page

## Cross-dossier matrix: what is not matched

- mismatch: jolof-empire 1455 gain cp takrur / mirror takrur 1285 dissolve. counterpart takrur dissolved in 1285 (to mali-empire); the 1455 conquest of Namandirou/Takrur needs another counterpart
- missing: sultanate-of-katsina 1512 occupation_start cp songhai-empire. songhai-empire has no Katsina event; the Katsina page calls it a vassal ('essentially became a vassal of Gao'), so songhai-empire should carry vassal_start 1512 / vassal_end 1554 cp sultanate-of-katsina and this occupation pair can go
- missing: sultanate-of-katsina 1554 occupation_end cp songhai-empire. see the 1512 entry
- mismatch: kingdom-of-kebbi 1530 gain cp songhai-empire / mirror songhai-empire 1515 gain. songhai-empire gains Aïr in 1515 (cp 'Sultanate of Agadez') and records no loss to Kebbi; both the Kebbi and Agadez pages call Kebbi's hold an occupation: make it occupation_start cp sultanate-of-agadez
- missing: kingdom-of-kebbi 1580 loss cp sultanate-of-agadez. sultanate-of-agadez (this batch) records no Kebbi event; if Kebbi's hold becomes an occupation, agadez records the owner's side
- mismatch: kingdom-of-kebbi 1808 loss cp sokoto-caliphate / mirror sokoto-caliphate 1805 gain. sokoto-caliphate /ledger/2 1805 'Kingdom of Kebbi' (text) vs 1808 here (Kebbi page: 'In 1808, Abdullahi dan Fodio defeated Kebbi's forces'); 3 years apart
- mismatch: sultanate-of-agadez 1516 occupation_start cp songhai-empire / mirror songhai-empire 1515 gain. songhai-empire annexes Aïr (gain 1515, cp 'Sultanate of Agadez') where this dossier has a Songhai occupation 1516-1591; one of the two must change type
- mismatch: sultanate-of-agadez 1591 occupation_end cp songhai-empire / mirror songhai-empire 1591 loss. songhai-empire's 1591 loss cp nobody covers 'the rest of the empire'; no event returns Aïr to Agadez
- mismatch: nupe-kingdom 1835 loss cp sokoto-caliphate / mirror sokoto-caliphate 1808 gain. sokoto-caliphate /ledger/5 1808 'Nupe Kingdom' (text) vs 1835 here (page headings; text has Ma'azu d. 1818, Masaba 1841); 27 years apart, Sokoto and Nupe both draw about 32,000 km2 for 1808-1835
- mismatch: bilala-kingdom 1630 loss cp wadai-empire / mirror wadai-empire 1635 found. wadai-empire starts 1635 with no Bilala/Kanem event; the Bilala page has Wadai drive the Bilala out of Kanem 'around 1630'
- mismatch: sine 1520 gain cp jolof-empire / mirror jolof-empire 1520 loss. jolof-empire /ledger/7 1520 loss cp 'Sine and Saloum' (text); both should become jolof-empire's vassal_end cp sine (overlord side) and this 'gain' be dropped
- missing: gwiriko 1740 gain cp kong-empire. kong-empire (this batch) has no 1740 loss to gwiriko; the two dossiers overlap by about 21,000 km2 for 1740-1897 (author flagged, not fixed)
- mismatch: pashalik-of-timbuktu 1591 gain cp songhai-empire / mirror songhai-empire 1591 loss. songhai-empire /ledger/12 gives Gao and Timbuktu to saadi-sultanate, whose /ledger/19 gains them in 1591; the pashalik's own infobox has it a 'Moroccan Governorate (1591-1621)'
- mismatch: pashalik-of-timbuktu 1592 gain cp songhai-empire / mirror songhai-empire 1592 loss. songhai-empire /ledger/16 gives Djenné to saadi-sultanate (/ledger/20, 1592)
- mismatch: pashalik-of-timbuktu 1833 loss cp massina-empire / mirror massina-empire 1826 gain. massina-empire takes Djenné in 1818 (found) and Timbuktu in 1826 (cp 'Tuareg of Timbuktu'); the pashalik keeps both to 1833
- mismatch: zazzau 1805 loss cp sokoto-caliphate / mirror sokoto-caliphate 1809 gain. sokoto-caliphate /ledger/11 1809, text counterpart 'Hausa kingdoms of Zamfara and Zazzau'; Zazzau page: 'In 1805 it was captured by the Fulani'; 4 years apart
- mismatch: saadi-sultanate 1618 vassal_start cp pashalik-of-timbuktu. Saadi holds Timbuktu, Gao and Djenné as its own 1591-1617 and the pashalik as vassal from 1618, while pashalik-of-timbuktu holds the same land from 1591 (about 83,000 km2 double claim)
- missing: bamana-empire 1748 gain cp pashalik-of-timbuktu. bamana-empire /ledger/1 (and /3 1752 loss, /5 1769 gain) of Timbuktu cp pashalik-of-timbuktu; the pashalik has no event (its page is silent on the Bambara)
- missing: empire-of-kanem 1500 gain cp Bilala. Bornu retakes part of Kanem (about 34,000 km2); bilala-kingdom has no loss and keeps all of Kanem to 1630; the Bilala page has Idris Katagarmabe capture Kanem 'in the early 16th century' and leave it to Bilala governors (a vassalage)
- missing: kong-empire 1897 dissolve cp wassoulou-empire. Kong's successor is wassoulou-empire (Savanes) but wassoulou records no gain in 1897 and drops Savanes from its 1897-1898 keyframe
- mismatch: mali-empire 1537 loss cp kaabu / mirror kaabu 1537 found. years agree; the land does not: mali-empire hands over Guinea-Bissau, the Gambia and Casamance, kaabu draws Gabú, Kolda and two Gambian regions (about 30,000 km2)
- mismatch: futa-toro 1599 vassal_start cp Tributary states (Jolof, Waalo, Saloum, Cayor, Gajaaga). the tributaries jolof-kingdom, waalo, saloum, gajaaga (and diarra) have dossiers in this batch: one vassal_start per slug is needed; Cayor only from the early 17th century; Fatick (Sine) is not on the page's list
- missing: empire-of-kanem 1571 vassal_start cp bagirmi-sultanate. to add in the empire-of-kanem ledger (overlord side): Bagirmi page: Bornu 'succeeded in absorbing Bagirmi' under Idris Alooma (1571-1602/3); independence under Muhammad al-Amin (1751-1785)
- missing: wadai-empire 1805 vassal_start cp bagirmi-sultanate. to add in the wadai-empire ledger (overlord side): Bagirmi page: after the 1805 sack 'Bagirmi subsequently became a tributary'; wadai-empire records only a one-year contest
- missing: empire-of-kanem 1438 vassal_start cp sultanate-of-kano. to add in the empire-of-kanem ledger (overlord side): Kano page: under Abdullahi Burja (1438-52) Kano began paying tribute to Bornu
- missing: empire-of-kanem 1731 vassal_start cp damagaram. to add in the empire-of-kanem ledger (overlord side): Damagaram page: 'at the beginning a vassal state of the decaying borno' (end undated)
- missing: empire-of-kanem 1614 vassal_start cp mandara-kingdom. to add in the empire-of-kanem ledger (overlord side): Mandara page: Idris Alaoma 'personally installed Nanda as king in 1614'
- missing: songhai-empire 1497 vassal_start cp mossi-kingdoms. to add in the songhai-empire ledger (overlord side): Mossi page: the Mossi 'reestablished their independence' after 1591 (Askia's 1497 war)
- missing: songhai-empire 1512 vassal_start cp diarra. to add in the songhai-empire ledger (overlord side): Diarra page: after 1512 'Diarra likely then swore fealty to Songhai'; songhai and mali Cliopatria shapes cover the whole Diarra disc
- missing: mali-empire 1235 vassal_start cp diarra. to add in the mali-empire ledger (overlord side): Diarra page: Diarra 'fell under the Sosso Empire and the Mali Empire beginning in the early 13th century'
- missing: state-of-rabih-az-zubayr 1890 vassal_start cp dar-al-kuti. to add in the state-of-rabih-az-zubayr ledger (overlord side): Dar al-Kuti page: Rabih installed Sanussi in 1890; Rabih page calls him 'Rabih's lieutenant' (1891); both dossiers draw Bamingui-Bangoran in 1890-1891
- missing: tukulor-empire 1854 vassal_start cp khasso. to add in the tukulor-empire ledger (overlord side): Umar Tall page: 'The kings of the Khasso region peacefully submitted' (1854); Khasso page: Khasso's petty kings submitted in November 1854
- missing: kaarta 1770 vassal_start cp khasso. to add in the kaarta ledger (overlord side): Kaarta page: Sira Bo (1761-1781) vassalised 'Diarra in 1777 and Khasso' (Khasso undated)
- missing: french-africa 1897 vassal_start cp dar-al-kuti. to add in the french-africa ledger (overlord side): Dar al-Kuti page: protectorate of 28 August 1897 (af-08)
- missing: zazzau 1576 vassal_start cp sultanate-of-kano. to add in the zazzau ledger (overlord side): Zazzau page: Amina's campaigns 'established a tributary region including the kingdoms of Kano and Katsina' (undated, c1)

Matched: tukulor-empire 1855 gain = kaarta 1855 loss; tukulor-empire 1860 gain = diarra 1860 loss; tukulor-empire 1861 gain = bamana-empire 1861 dissolve; tukulor-empire 1862 gain = massina-empire 1862 dissolve; jolof-empire 1513 loss = futa-toro 1513 found; jolof-empire 1549 loss = cayor 1549 found; state-of-rabih-az-zubayr 1893 gain = empire-of-kanem 1894 loss; kaabu 1867 loss = fuladu 1867 found; kaabu 1867 loss = imamate-of-futa-jallon 1867 gain; imamate-of-futa-jallon 1867 gain = kaabu 1867 loss; kaarta 1855 loss = tukulor-empire 1855 gain; sultanate-of-kano 1807 loss = sokoto-caliphate 1807 gain; sultanate-of-katsina 1806 loss = sokoto-caliphate 1807 gain; sultanate-of-gobir 1756 gain = zamfara 1756 loss; sultanate-of-gobir 1808 loss = sokoto-caliphate 1808 gain; cayor 1549 gain = baol 1549 loss; cayor 1756 loss = baol 1756 gain; bilala-kingdom 1380 gain = empire-of-kanem 1380 loss; baol 1549 loss = cayor 1549 gain; baol 1756 gain = cayor 1756 loss; fuladu 1867 gain = kaabu 1867 loss; gajaaga 1690 loss = bundu 1690 found; zamfara 1756 loss = sultanate-of-gobir 1756 gain; zamfara 1809 loss = sokoto-caliphate 1809 gain; diarra 1860 loss = tukulor-empire 1860 gain; mali-empire 1360 vassal_end = jolof-empire 1360 found.

Exceptions (counterpart nobody, af-08 not run, no dossier and listed, overlord-side vassal events): 74 rows, listed in the JSON.
