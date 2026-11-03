# Notes, group eu-02-b (Hellenistic world, part b)

Run history. First run of this batch for four dossiers; achaean-league.json already existed from an earlier run (validates, 32 events, 12 pages, kept unchanged, notes read: it is complete). No page failed to load. WebFetch returns a model summary of the page, so quotation marks in notes enclose only strings the tool returned as quotations; other wording is paraphrase.

## Written
achaean-league (kept; repaired in the repair run below), greek-colonies, illyrian-kingdom, rhodes, molossians. Not written: antigonid-macedonia (below).

## antigonid-macedonia: merged, not written
'Antigonid Dynasty' (-291..-278) and 'Antigonid Macedonia' (-277..-165) share Q237325 and are one state. Group eu-02-a wrote one dossier, antigonid-dynasty, with both Names in cliopatria_names; it validates and reviews all 18 antigonid-macedonia shapes plus the 4 antigonid-dynasty ones (26 keyframes). A second dossier would give the colour agent two states for one. The orchestrator should reassign the slug as 'merged into antigonid-dynasty'.

## greek-colonies (5 pages: Greek colonisation, Massalia, Hiero II, Cleomenes III, Chersonesos Taurica; the Molossians, Rhodian Peraia and Rhodes pages were opened for the other dossiers and cited here)
- The row is not a state. Its 12 clusters (Languedoc and Provence coast, west Pontic coast, Pontic Anatolia, Crimea, Olbia, Caria, Crete, Valencia coast, Syracuse, Propontis, Aetolian coast, Azov; Epirus from 247, Laconia from 230) are independent poleis and colonies, the same aggregate that 'Greek City-States' carries to 272 and from 225. Type 'state' (as eu-01 chose; 'umbrella' would turn the land grey), no capital.
- DUPLICATE: eu-01's greek-city-states holds a bridging keyframe for -271..-226 (greek-city-states_-271, piece -257) and asks eu-02 whether to write greek-colonies. This dossier reviews the six shapes under their own ids with the same carve-outs (Syracuse, Rhodes, Massalia, Epirus, Laconia). Keep one: either drop the eu-01 keyframe or merge this dossier into greek-city-states.
- All six events are confidence 1 (Cliopatria's window; unexplained cell changes in Caria, Sicily, the Propontis, Colchis, Elis). Unverified: page budget: West Pontic cities, Olbia and Tyras, Crimea, Crete, the Iberian cluster, Byzantium, Sinope, Acarnania.
- Caria: 20 cells in 271 shrink to 5 by 247 with no page; the Pontic coast east of Sinope may overlap kingdom-of-pontus.

## illyrian-kingdom (5 pages: Illyrian kingdom, Agron, First Illyrian War, Ardiaei, Gentius)
- Runs to 168, not Cliopatria's 226: the kingdom page keeps one kingdom to Gentius. Three new keyframes (228 core north of the Drin, 196 plus Lissus, 180 minus Dalmatia).
- Start 256 is Cliopatria's year (confidence 1); the earlier Illyrian dynasties (Bardylis, Glaucias) are other tribes' states and are not drawn.
- Page conflicts: Corcyra annexed by Agron (undated) or taken in 229; peace 229/228 or 227; Agron died 231 or 230; Demetrius of Pharos 228-219 or 222-219; end 168 (text) or 135 (infobox).
- Not on pages and left out: Pharos and Issa, the Second Illyrian War (220-219), Demetrius's fall, the extent 227-197, the land rewarded in 196 (Lissus is a bridge, confidence 1).
- Counterparts with no matching loss elsewhere: kingdom-of-epirus (239, 231), antigonid-dynasty (196). No dossier: Corcyra, Epidamnos, Apollonia, Parthini, Atintani, Dalmatae and Daorsi.

## rhodes (4 pages: Rhodes, Treaty of Apamea, Rhodian Peraia, Third Macedonian War; over the 1-2 page budget by two, because the 167 loss is on none of the first two)
- Whole state -408..-39. Q43048 is shared with domain-of-rhodes (1206-1249), a different state 1,400 years on: two dossiers; that row is not in this batch.
- Cliopatria's 188 shape is right for 188-167; its 170-165 shape is wrong from 167 (loss of the wider Peraia, Peraia page). New keyframes -408..-189 (island only; the mainland holdings before 188 are on no page) and 167..-39 (island plus the Cnidus-Kaunos strip).
- End 39 is a bridge (confidence 1): no page says Rhodian self-rule ended. The Peraia page's 'tributary remainder of Caria and Lycia' has an ambiguous date (vassal events at confidence 1).
- Other dossiers should carry: roman-republic vassal_start on Rhodes in 164 (alliance); seleucid-empire the 188 loss of Caria and Lycia; greek-city-states should subtract the island (408-) and the Peraia (188-).

## molossians (2 pages: Molossians, Third Macedonian War)
- A sliver of the Epirote core; kingdom-of-epirus already covers the Molossian state 370-167. They overlap on the Molossis in 170-167; one Epirus dossier with a contested Molossis would be cleaner.
- 170-168 (Cliopatria 165 is late). The pages do not date the sack (seventy cities, 150,000 enslaved); kingdom-of-epirus has 167 from the Epirus (ancient state) page, not opened here.

## Gazetteer names needed
Laconia (region); Agde, Hyères, Antibes (places; massalia needs them too); Phoenice/Finiq, Rhizon/Risan, Cnidus, Kaunos, Passaron, Dodona (places; capitals or text only, polygons or radii stand in).

## Repair run (2026-10-19): achaean-league, reviewer verdict fail
Validates with --resolve: 0 errors, 0 warnings; 33 events, 21 keyframes, 7 wars, 17 sources. Pages re-opened: Cleomenean War, Achaean League, Nabis of Sparta, Aratus of Sicyon, First Macedonian War, Roman-Seleucid War (URL with lower-case 'war'; the capitalised one returned not found), Elis, Messene, Antigonus III Doson. No page failed except that one URL spelling.

Changed:
- K10 (206-165) held the whole Peloponnese from 206. It now holds 206-199 (Cliopatria less Corinth and Megara) and is followed by new keyframes -198 (also less Argos), -197..-196 (Corinth back, Argos still out), -195..-193 (Argos back), -192 (plus Sparta) and -191..-165 (region Peloponnese). The reviewer asked for 206-192 as one shape plus -191, with -198 optional; I split by the ledger's own years (198, 197, 195, 192) so keyframes and events agree. I also subtracted Megara (K9 does; /ledger/14 loses it in 223 with no dated return): the 10 km disc changes no Cliopatria cell, but the 'Peloponnese' polygon takes in the Megara cell (23.28 E 38.02 N), noted in -191.
- K8 (225-211) now holds 225 only; new -224 (Argos back, Corinth out, Megara in) and -223..-211 (Corinth and Megara out). The reviewer asked for one -224..-211 keyframe; Megara leaves in 223, so I made two.
- K6 (239-231) now holds 239-236 (Cliopatria unchanged); new -235 (plus Megalopolis) and -234..-231 (plus Orchomenus and Mantinea, c. 234, confidence 1).
- /ledger/25 split into the 191 gain of Messenia (counterpart messene) and of Elis (counterpart greek-city-states, whose /ledger/68 loses 'Messene and Elis' with the rest of the Peloponnese; an elis dossier would be truer). Both confidence 1.
- wars: First Macedonian War (214-205, zones empty, 'no ground changed hands') and Roman-Seleucid War (192-188, zone Messenia and Elis).
- sources: +5 (First Macedonian War, Roman-Seleucid War, Elis, Messene, Antigonus III Doson).
- /ledger/19 counterpart antigonid-dynasty was applied by the reviewer; checked in the file.

Where I differ from the review, or the pages are silent:
- 'Heraea and Orchomenus ceded to Macedon 224': the Cleomenean War page has Antigonus take them in early spring 223 (Cleomenes took Orchomenus in 229 and Heraea about 227). Not 224, and not subtracted from the shape (no coordinates on the pages; they are in the infobox's territorial changes). antigonid-dynasty should carry them.
- First Macedonian War 'from 211': the infobox says 214-205 (page: First Macedonian War); 211 is the Aetolian-Roman treaty, and the league appears on the page from 209 (Philip and Cycliadas at Dyme, the attack on Elis). I followed the page.
- Argive revolt: neither the Cleomenean War, Aratus nor Antigonus III pages put a year on it. 224 rests on the Aratus page ('In 224 BC, while Antigonus was liberating the occupied cities in the Peloponnese'); ledger 13 stays confidence 2.
- 191 for Messene and Elis: the Achaean League, Elis, Messene and Roman-Seleucid War pages date neither. The Roman-Seleucid infobox lists both on Antiochus's side in 192-188, so 191 is a bridge (confidence 1); the latest possible year is 183 (Dinocrates' revolt, /ledger/27).
- Sparta in the league: the Nabis page says 192; the Roman-Seleucid War page puts Nabis's coastal attack in late 193 and his death by Aetolians before the war's 192 start. 192 kept. Apamea has no year on that page.

Left alone, not in the findings: keyframes K0 (to -276) and K1 (-272) leave 275-273 uncovered; K7 and K8 still draw Mantinea and Orchomenus after 226 and 229 (ledger 10, 11 lose them in the text only); peloponnesian-league's Argos loss is dated 222 against this dossier's 224 (the reviewer routes it to eu-01); Mantinea's loss in 226 has no peloponnesian-league gain.
