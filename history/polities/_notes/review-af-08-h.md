# Review of batch af-08-h (Phase B)

Reviewer brief filled 2026-10-19; review run 2026-10-20. Dossiers: republic-of-chad, federal-republic-of-nigeria, mauritania, republic-of-cote-d-ivoire, republic-of-benin, gabon, biafra, forces-nouvelles-de-cote-d-ivoire. Neighbour dossiers present: republic-of-liberia (no event against this batch) and morocco (a counterpart, checked). Every other Context polity is unwritten (af-08, eu-21, eu-22).

Mechanical: all 8 files validate (`--resolve`), with no errors. The only warnings are the three gazetteer names Aouzou Strip, Tiris al-Gharbiyya and Northern Cameroons, and the author's report lists all three. Every Cliopatria shape has a verdict. All six owned states get a new 1960 keyframe with a correction, because Cliopatria's shapes start in 1961.

Spot checks: 33 events or entries, every one opened on its page. None was fabricated or mis-dated. Two notes quote loosely but give the right date: Nigeria L0 ('became a formally independent federation on 1 October 1960') and Benin L2 ('officially changed ... on 1 March 1990').

Reviewer edits (applied, revalidated, read back): Chad's capital is now Fort-Lamy 1960-1973 and N'Djamena 1973-2024 (N'Djamena page), and the W1 outcome now attributes its dates to the right page. Nigeria L1 (Northern Cameroons) now has month 6, from the British Cameroons page: 'became the Sardauna Province of Northern Nigeria on 1 June 1961'.

## Verdicts

### republic-of-chad: fix

Tried: Validator passed, with 4 warnings, all the gazetteer name 'Aouzou Strip'. Every Cliopatria shape (1961, 2024) has a verdict. I opened all 3 source pages and checked 5 events: the 1960 independence, the 1973 Aouzou occupation (114,000 km2), Faya-Largeau on 18 February 1978 and the BET, the ceasefire of 11 September 1987, and the ICJ ruling of 3 February 1994 with the withdrawal of 15 April to 10 May 1994. All are on the pages as claimed. The occupation pair, the contest pairs and the certainty spans are contiguous and in order. N'Djamena is inside the bbox. The area is within 1 percent. libyan-arab-republic has no dossier yet (af-08 has not run). Revalidated after the edits: valid.

Area: infobox 1280000 km2 (2024), Cliopatria 1272985 km2, ratio 0.99, acknowledged True.

Fixes:
- `/identity/capitals/0` (applied by reviewer): The capital was named N'Djamena for 1960-2024, but the city was Fort-Lamy until its renaming on 6 April 1973. Evidence: N'Djamena page: 'Before its renaming in 1973, the city was known as Fort-Lamy'; the history section dates Tombalbaye's renaming to 6 April 1973 (the lead says 1975). Fix: Split into Fort-Lamy 1960-1973 and N'Djamena 1973-2024 (same coordinates), source the N'Djamena page, and add that page to sources[].
- `/wars/1/outcome` (applied by reviewer): The outcome cites the Aouzou Strip page, but the 10 May and 30 May 1994 dates in it are not on that page. Evidence: The Aouzou Strip page gives only the February 1994 ICJ decision (16 to 1) and resolutions 915/926. The Chadian-Libyan conflict page has 'completed by 10 May' and 'The formal and final transfer of the Strip from Libya to Chad took place on 30 May'. Fix: Say in the outcome that the two dates come from the Chadian-Libyan conflict page.

Thin (for a gap-filler):
- `/wars/2`: Territory held by FROLINAT and the rebel factions in 1965-1979 (my recollection: much of the north was rebel-held before the 1978 Libyan-backed offensive). There are no contest events for it; this is thin by design within the 1-2 page budget. Page to try: https://en.wikipedia.org/wiki/Chadian_Civil_War_(1965%E2%80%931979)
- `/ledger`: The N'Djamena episode of December 1980 to November 1981 (Libyan troops in the capital) is deliberately not drawn. Confirm whether Libyan forces held central Chad beyond the BET. Page to try: https://en.wikipedia.org/wiki/Chadian-Libyan_conflict

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/Chad); /ledger/1 confirmed (https://en.wikipedia.org/wiki/Aouzou_Strip); /ledger/2 confirmed (https://en.wikipedia.org/wiki/Chadian-Libyan_conflict); /ledger/5 confirmed (https://en.wikipedia.org/wiki/Chadian-Libyan_conflict); /ledger/6 confirmed (https://en.wikipedia.org/wiki/Chadian-Libyan_conflict)

### federal-republic-of-nigeria: thin

Tried: Validator passed, with 3 warnings, all the gazetteer name 'Northern Cameroons'. Shapes 1961, 1969 and 2024 have verdicts, and the 1960 keyframe has a correction. I checked 6 events: independence on 1 October 1960; the 1961 plebiscite; secession on 30 May 1967; Port Harcourt on 19 May 1968; the end on 15 January 1970; Abuja on 12 December 1991. All are on the pages. The L0 note's quote is not verbatim: the page says 'became a formally independent federation on 1 October 1960', but the date is right. All 6 Biafra events are mirrored in biafra.json. The capitals are inside the bbox and contiguous. The area is within 1.5 percent. The verdict is thin because the dated 1967-1970 front, Bakassi 2008 and Boko Haram 2014-15 are missing, within budget. Revalidated after the edit: valid.

Area: infobox 923769 km2 (2024), Cliopatria 910830 km2, ratio 0.99, acknowledged True.

Fixes:
- `/ledger/1/month` (applied by reviewer): The gain of the Northern Cameroons had no month, and the author left the British Cameroons page unopened for the page budget. Evidence: British Cameroons page: plebiscite 'held on 11 February 1961'; 'Northern Cameroons became the Sardauna Province of Northern Nigeria on 1 June 1961'. Fix: Set month 6, change the source to the British Cameroons page with that quote, and add the page to sources[].

Thin (for a gap-filler):
- `/ledger`: Bakassi peninsula: transferred to Cameroon on 14 August 2008 under the 2002 ICJ judgment and the 2006 Greentree Agreement (my recollection, not checked on a page). This is a loss to republic-of-cameroon, missing from the ledger; Cliopatria's Nigeria 1969-2024 shape still lists Cameroon cells among its modern countries. The Lake Chad villages awarded by the same judgment are also missing. The author flagged both (page budget). Page to try: https://en.wikipedia.org/wiki/Bakassi
- `/ledger/6`: Calabar: the Civil War page the author opened says 'On 17 October 1967 Nigerians invaded Calabar', so a Calabar gain (October 1967, confidence 2) can be added with the mirror loss in biafra. The other Biafran losses (Onitsha 1968, Aba and Owerri September 1968, Umuahia April 1969; dates from my recollection) have no date on the pages opened, so the 1968-1970 shrinkage of Biafra is drawn only as a floor. Page to try: https://en.wikipedia.org/wiki/Umuahia
- `/ledger`: The Boko Haram insurgency: the group held territory in Borno, Yobe and Adamawa from August 2014 to March 2015, and ISWAP has held ground around Lake Chad since (my recollection, not checked on a page). There is no contest event and the author's notes do not mention it. Page to try: https://en.wikipedia.org/wiki/Boko_Haram_insurgency

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/Nigeria); /ledger/1 confirmed (https://en.wikipedia.org/wiki/Nigeria); /ledger/3 confirmed (https://en.wikipedia.org/wiki/Nigerian_Civil_War); /ledger/7 confirmed (https://en.wikipedia.org/wiki/Nigerian_Civil_War); /ledger/8 confirmed (https://en.wikipedia.org/wiki/Nigerian_Civil_War); /ledger/9 confirmed (https://en.wikipedia.org/wiki/Abuja)

### mauritania: pass

Tried: Validator passed, with 6 warnings, all the gazetteer name 'Tiris al-Gharbiyya'. Shapes 1961, 1976 and 2024 have verdicts; the author correctly found that the 1976 shape lacks the southern third of Western Sahara. On the pages: Madrid Accords 14 November 1975, Tichla and La Guera 20 December 1975, the 1976 annexation, the 5 August 1979 treaty, and Morocco's annexation on 11 August 1979. The contest pair is in order. Nouakchott is inside the bbox. The area is within 2 percent. The cross-dossier mismatch is on morocco's side; see cross_checks.

Area: infobox 1030000 km2 (2024), Cliopatria 1053246 km2, ratio 1.02, acknowledged True.

Thin (for a gap-filler):
- `/ledger/2`: The month of the gain: the Moroccan-Mauritanian partition agreement (14 April 1976 from my recollection) is not on the pages opened, and Mauritania's troops held Tichla and La Guera from 20 December 1975. Page to try: https://en.wikipedia.org/wiki/Madrid_Accords
- `/ledger/3`: Whether Mauritania kept La Guera (Lagouira) after 1979. If it did, the 1979 loss should exclude it. Page to try: https://en.wikipedia.org/wiki/Lagouira

Spot checks: /ledger/1 confirmed (https://en.wikipedia.org/wiki/Western_Sahara_War); /ledger/2 confirmed (https://en.wikipedia.org/wiki/Mauritania); /ledger/3 confirmed (https://en.wikipedia.org/wiki/Western_Sahara_War); /ledger/4 confirmed (https://en.wikipedia.org/wiki/Western_Sahara_War)

### republic-of-cote-d-ivoire: pass

Tried: Validator passed with no warnings. Shapes 1961 and 2024 have verdicts. On the pages: independence 7 August 1960, Yamoussoukro from 1983, the rebellion of 19 September 2002 with Bouaké and Korhogo, the 'de facto partition', and the 2011 integration into the army. The loss and gain mirror the FN dossier's found and dissolve. The admin-1 reading of the FN zones (Bouna, Katiola, Bouaké, Mankono, Séguéla, Man, Touba) is plausible and resolves. Liberia's dossier has no post-1960 event against this state. Area ratio 1.00.

Area: infobox 322462 km2 (2024), Cliopatria 321727 km2, ratio 1.0, acknowledged True.

Thin (for a gap-filler):
- `/ledger/3`: The 2011 return of the north is confidence 1. Second Ivorian Civil War page: 'On 28 March, the New Forces – now renamed the Republican Forces of Côte d'Ivoire (RFCI)'; 'On 11 April, Ouattara's forces stormed Gbagbo's residence and arrested him'. The First Ivorian Civil War page says the government 'began its administrative redeployment in northern areas formerly held by rebels' in 2007. A gap-filler can set 2011-04 at confidence 2, or split the return between 2007 and 2011. Page to try: https://en.wikipedia.org/wiki/Second_Ivorian_Civil_War

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/Ivory_Coast); /ledger/1 confirmed (https://en.wikipedia.org/wiki/Ivory_Coast); /ledger/2 confirmed (https://en.wikipedia.org/wiki/First_Ivorian_Civil_War); /ledger/3 confirmed (https://en.wikipedia.org/wiki/Forces_Nouvelles_de_C%C3%B4te_d%27Ivoire)

### republic-of-benin: pass

Tried: Validator passed with no warnings. Shapes 1961, 1969 and 2024 have verdicts, and the 0.2 percent refit is acknowledged. On the page: independence 1 August 1960; the rename on 30 November 1975; the name changed to the Republic of Benin on 1 March 1990. The page reads 'officially changed ... on 1 March 1990', not 'took effect', but the date is right. Porto-Novo is inside the bbox. Area ratio 1.03 (infobox) and 1.04 (body).

Area: infobox 114763 km2 (2024), Cliopatria 117637 km2, ratio 1.03, acknowledged True.

Thin (for a gap-filler):
- `/ledger`: Dahomey's 1961 annexation of the Portuguese fort of Sao Joao Baptista de Ajuda at Ouidah (tiny; a place event). Thin by design: 1 page used. Page to try: https://en.wikipedia.org/wiki/S%C3%A3o_Jo%C3%A3o_Baptista_de_Ajuda
- `/ledger`: The 2005 ICJ Benin-Niger frontier judgment (Lété Island and the Niger River islands to Niger). Small. Page to try: https://en.wikipedia.org/wiki/L%C3%A9t%C3%A9_Island

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/Benin); /ledger/1 confirmed (https://en.wikipedia.org/wiki/Benin); /ledger/2 confirmed (https://en.wikipedia.org/wiki/Benin)

### gabon: pass

Tried: Validator passed with no warnings. Shapes 1961 and 2024 have verdicts. On the page: independence 17 August 1960 (text and infobox) and French Equatorial Africa 1910-1958. Libreville is inside the bbox. Area ratio 0.99. With a single event, the 4-check budget reduces to 1.

Area: infobox 267668 km2 (2024), Cliopatria 264939 km2, ratio 0.99, acknowledged True.

Thin (for a gap-filler):
- `/ledger`: The Mbanié/Corisco Bay islands dispute with Equatorial Guinea (Gabon occupied Mbanié in 1972; my recollection, not checked on a page). Tiny; thin by design. Page to try: https://en.wikipedia.org/wiki/Mbani%C3%A9_Island

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/Gabon)

### biafra: thin

Tried: Validator passed with no warnings. The type rebel and family africa are right, the life is 30 May 1967 to 15 January 1970, and found and dissolve fall on those years. The infobox capitals match (Enugu 1967, Umuahia 1967-1969, Owerri 1969-1970, Awka 1970), and each lies in the Eastern Region. The 9-state admin-1 mapping of the Eastern Region is right: Rivers in 1967 included modern Bayelsa. There is no Cliopatria row; the ratio compares the author's grid reading (85,700 km2) with the 77,306 km2 infobox and is acknowledged in K0. All 8 territorial events are mirrored in Nigeria. The verdict is thin, not fail: the floor keyframe is honest but leaves the 1968-1969 extent undrawn.

Area: infobox 77306 km2 (1967), Cliopatria 0 km2, ratio 1.11, acknowledged True.

Thin (for a gap-filler):
- `/keyframe_review/1`: The author marks the 1968-1970 keyframe as only a floor. By 1969 Biafra had shrunk from the whole Eastern Region to an Owerri-Umuahia-Uli enclave (my recollection; the pages opened do not say so), but only Enugu (4 October 1967) and Port Harcourt (19 May 1968) are carved out, so the map over-draws Biafra and under-draws Nigeria for 1968-1969. Calabar, 'invaded' on 17 October 1967, is on the Civil War page and can be added at confidence 2 with Nigeria's mirror gain. Page to try: https://en.wikipedia.org/wiki/Nigerian_Civil_War
- `/identity/capitals/1`: The date Umuahia fell (April 1969 from my recollection) and the date of the move to Owerri. The infobox gives only the years. Page to try: https://en.wikipedia.org/wiki/Umuahia
- `/identity/wikidata`: wikidata is null. Biafra has a Wikidata item, which a gap-filler can add from the page's Wikidata link (wikidata.org is unreachable from here). Page to try: https://en.wikipedia.org/wiki/Biafra

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/Biafra); /ledger/5 confirmed (https://en.wikipedia.org/wiki/Nigerian_Civil_War); /ledger/6 confirmed (https://en.wikipedia.org/wiki/Biafra); /ledger/8 confirmed (https://en.wikipedia.org/wiki/Biafra)

### forces-nouvelles-de-cote-d-ivoire: thin

Tried: Validator passed with no warnings. Type rebel; it held the north for 9 years. On the pages: formed in December 2002 from the MPCI, MPIGO and MJP; the MJP folded into the MPCI; 'mostly integrated into the Ivorian army in 2011'. The Bouaké 'stronghold' is on the Ivory Coast page. The found and dissolve events mirror the government's loss and gain. No infobox area exists, so there is no ratio.

Area: infobox 0 km2 (0), Cliopatria 0 km2, ratio 0.0, acknowledged True.

Thin (for a gap-filler):
- `/ledger/2`: The end, 2011, is confidence 1. The Second Ivorian Civil War page gives the renaming to the Republican Forces (RFCI) on 28 March 2011 and Gbagbo's arrest on 11 April 2011. Set month 3 or 4 at confidence 2 here and in republic-of-cote-d-ivoire /ledger/3. Page to try: https://en.wikipedia.org/wiki/Second_Ivorian_Civil_War
- `/keyframe_review/0/correction`: The extent is the researcher's admin-1 reading; no page gives the ceasefire line or the 'zone of confidence'. The FN page says there were 10 zones but names only 7. Page to try: https://en.wikipedia.org/wiki/Zone_of_confidence

Spot checks: /ledger/0 confirmed (https://en.wikipedia.org/wiki/First_Ivorian_Civil_War); /ledger/1 confirmed (https://en.wikipedia.org/wiki/Forces_Nouvelles_de_C%C3%B4te_d%27Ivoire); /ledger/2 confirmed (https://en.wikipedia.org/wiki/Forces_Nouvelles_de_C%C3%B4te_d%27Ivoire); /identity/capitals/0 confirmed (https://en.wikipedia.org/wiki/Ivory_Coast)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| republic-of-chad 1960 found (french-fifth-republic) | french-fifth-republic 1960 loss | exception | french-fifth-republic has no dossier yet (eu-22 has not run). Cliopatria draws the 1960 land in that row; the eu-22 dossier must lose it at the 1960 independence month. |
| mauritania 1960 found (french-fifth-republic) | french-fifth-republic 1960 loss | exception | french-fifth-republic has no dossier yet (eu-22 has not run). Cliopatria draws the 1960 land in that row; the eu-22 dossier must lose it at the 1960 independence month. |
| republic-of-cote-d-ivoire 1960 found (french-fifth-republic) | french-fifth-republic 1960 loss | exception | french-fifth-republic has no dossier yet (eu-22 has not run). Cliopatria draws the 1960 land in that row; the eu-22 dossier must lose it at the 1960 independence month. |
| republic-of-benin 1960 found (french-fifth-republic) | french-fifth-republic 1960 loss | exception | french-fifth-republic has no dossier yet (eu-22 has not run). Cliopatria draws the 1960 land in that row; the eu-22 dossier must lose it at the 1960 independence month. |
| gabon 1960 found (french-fifth-republic) | french-fifth-republic 1960 loss | exception | french-fifth-republic has no dossier yet (eu-22 has not run). Cliopatria draws the 1960 land in that row; the eu-22 dossier must lose it at the 1960 independence month. |
| republic-of-chad 1973 occupation_start (libyan-arab-republic) | libyan-arab-republic 1973 occupation_start | exception | libyan-arab-republic has no dossier yet (af-08 has not run). Its dossier must carry the Aouzou Strip occupation, 1973 to May 1994; Cliopatria's Libyan shapes do not reach the strip. |
| republic-of-chad 1994 occupation_end (libyan-arab-republic) | libyan-arab-republic 1994 occupation_end | exception | As above: the withdrawal was completed by 10 May 1994, with the formal transfer on 30 May 1994. |
| federal-republic-of-nigeria 1960 found (british-gold-coast) | british-gold-coast 1960 loss | exception | british-gold-coast has no dossier yet (af-08 has not run). Cliopatria draws pre-1961 Nigeria in that row. |
| federal-republic-of-nigeria 1961 gain (british-gold-coast) | british-gold-coast 1961 loss | exception | Northern Cameroons, 1 June 1961. The british-gold-coast row ends in 1960 and has no dossier yet. The author also lists british-cameroons under counterparts_needing_dossiers; one counterpart slug should be chosen. |
| federal-republic-of-nigeria 1967 loss (biafra) | biafra 1967 found | matched | Eastern Region, 30 May 1967. |
| federal-republic-of-nigeria 1967 occupation_start (biafra) | biafra 1967 occupation_start | matched | Mid-West, 9 August 1967; Biafra is the occupier. |
| federal-republic-of-nigeria 1967 occupation_end (biafra) | biafra 1967 occupation_end | matched | Benin City retaken on 22 September 1967. |
| federal-republic-of-nigeria 1967 gain (biafra) | biafra 1967 loss | matched | Enugu, 4 October 1967. |
| federal-republic-of-nigeria 1968 gain (biafra) | biafra 1968 loss | matched | Port Harcourt, 19 May 1968. |
| federal-republic-of-nigeria 1970 gain (biafra) | biafra 1970 dissolve | matched | 15 January 1970. |
| mauritania 1976 gain (francoist-spain) | francoist-spain 1975 loss | exception | francoist-spain has no dossier yet (eu-21 has not run). Its life ends in 1975, inside the one-year window. The Spanish withdrawal ended on 26 February 1976 (my recollection) under the post-Franco state (the kingdom-of-spain row); eu-21 should date Spanish Sahara's loss to the Madrid Accords (14 November 1975). |
| mauritania 1979 loss (morocco) | morocco 1976 occupation_start | mismatch | morocco.json has no 1979 event for Tiris al-Gharbiyya. Its /ledger/25 (1976 occupation_start of {country: Western Sahara} against sahrawi-arab-democratic-republic) covers all of Western Sahara from 1976 and overlaps Mauritania's Tiris al-Gharbiyya 1976-1979. Morocco's author should limit the 1976 event to the northern two-thirds (Saguia el-Hamra and northern Rio de Oro) and add Tiris al-Gharbiyya on 11 August 1979. |
| republic-of-cote-d-ivoire 2002 loss (forces-nouvelles-de-cote-d-ivoire) | forces-nouvelles-de-cote-d-ivoire 2002 found | matched | Rebel-held north, 19 September 2002, same 7 admin-1 units on both sides. |
| republic-of-cote-d-ivoire 2011 gain (forces-nouvelles-de-cote-d-ivoire) | forces-nouvelles-de-cote-d-ivoire 2011 dissolve | matched | Both are confidence 1, so a gap-filler should move them together (March or April 2011). |

## For other groups

- morocco (owner group): /ledger/25 occupies all of Western Sahara from 1976, which overlaps Mauritania's Tiris al-Gharbiyya 1976-1979. Morocco has no 11 August 1979 event. Limit the 1976 event to the northern two-thirds and add the 1979 annexation of Tiris al-Gharbiyya.
- libyan-arab-republic (af-08): carry occupation_start 1973 and occupation_end May 1994 of the Aouzou Strip against republic-of-chad, plus the BET contest pairs 1978-1981 and 1983-1987.
- french-fifth-republic (eu-22) and british-gold-coast (af-08): lose the 1960 land at Chad 11 Aug, Benin 1 Aug, Cote d'Ivoire 7 Aug, Gabon 17 Aug, Mauritania 28 Nov and Nigeria 1 Oct 1960. british-gold-coast also loses the Northern Cameroons on 1 June 1961.
- francoist-spain (eu-21): Spanish Sahara's loss to Mauritania (south) and Morocco (north), at the Madrid Accords of 14 November 1975.
- SADR slug: use `sahrawi-arab-democratic-republic`, which morocco.json already uses, not `western-sahara`.

## Gazetteer names needed

- Aouzou Strip (region, republic-of-chad)
- Tiris al-Gharbiyya (region, mauritania)
- Northern Cameroons (region, federal-republic-of-nigeria)
