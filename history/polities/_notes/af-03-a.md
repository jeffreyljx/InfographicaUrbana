# Notes, group af-03-a (Sahel empires, part a)

Written 2026-10-19. Five dossiers for the six owned states: ghana-empire, sosso-empire, takrur, mali-empire, empire-of-kanem (which also carries bornu-empire). All validate with 0 errors and 0 unresolved region names (`--resolve`); the only warnings are counterpart slugs that no dossier has yet (jolof-empire, kaabu, bagirmi-sultanate, state-of-rabih-az-zubayr).

Page that failed: https://seshat-db.com/core/polity/ml_mali_emp/ (client error twice; Mali's Seshat page not read).

## bornu-empire merged into empire-of-kanem (rows to merge)
Cliopatria's "Empire of Kanem" (1072-1384) and "Bornu Empire" (1385-1894) share Wikidata Q1139762 and one Wikipedia article, which treats Kanem-Bornu as one empire and one Sayfawa dynasty that moved from Kanem to Bornu c. 1380. Merged under the earlier slug; cliopatria_names holds both; all twelve `bornu-empire_*` shapes are reviewed in it. There is no `bornu-empire.json`. Other dossiers that name `bornu-empire` as counterpart (wadai-empire, sokoto-caliphate, ...) should use `empire-of-kanem`; the colour agent should give the pair one colour.

## ghana-empire
- Founding c. 300 (infobox) not mapped; map starts at Cliopatria's 793 (king list "Dyabe Cisse: 790s"). Infobox area 650,000 km2 (year 1000) vs Cliopatria 204,203: read as a tribute sphere; the oral-tradition vassals (Takrur, Jafunu, Jaara, Bakhunu, Neema, Soso, Guidimakha, Guidime, Gajaaga, Awker, Adrar, Hodh) are not written as vassal events (undated; the Takrur page denies vassalage).
- Almoravid "conquest" 1076-77 is a disputed tradition (Conrad and Fisher: folklore); war entry only.
- Ghana-Sila war: 1060s on the Ghana page, 12th century on the Takrur page.
- End: c. 1200 (Sosso page), "by 1203" (Ghana page, Barth); Cliopatria's 1201/1202 hand-over kept.
- Pages opened: Ghana Empire, Sosso Empire. A gap-filler could open the works the Ghana page cites (al-Bakri, Conrad and Fisher, Lange).

## sosso-empire
- Cliopatria's shape is the Ghana shape (Wagadu); the Sosso seat near Boron/Koulikoro lies outside it and is added in the keyframe corrections.
- Manden conquest before Kirina is undated; year 1227 is a confidence-1 bridge.
- Sosso ends 1235 (Cliopatria) but Mali starts 1236, so the Mali gain is dated 1236.
- Gazetteer lacks "Sosso", "Boron", "Kirina", "Siby"; Koulikoro and Kangaba used as proxies.

## takrur
- Run to c. 1285 (Takrur page: Mali conquest "around 1286", infobox c. 1285) instead of Cliopatria's 1235; the Mali dossier removes Takrur from its shape until 1285. The Mali page says Sundiata's generals reached Takrur (undated): disagreement, dated page followed.
- Only 1040-1285 is drawn; the state is older (9th century, "c. 500") and continues as Jolof's conquest (1450s/1456) and the Denianke kingdom of Futa Toro (1513/1521-1776): that needs a Futa Toro dossier from the additions batch.
- Capital coordinates are the Cliopatria shape centroid (the page gives none).

## mali-empire
- Early shape: Cliopatria's 973,312 km2 for 1236 against the infobox's 100,000 km2 at 1250. Cut to the Sosso lands for 1236-1240; full Cliopatria outline from 1241 (bridge, confidence 1) minus Takrur (to 1285) and the Niger bend (Gao c. 1300, Timbuktu 1324). The dates of Sundiata's conquests (Diafunu, Kita, Senegambia, Kaabu, Jolof vassalage) and of Sakura's are not on the pages opened.
- Losses 1433 Timbuktu, c. 1435 Gao, c. 1436 Oualata are taken out of Cliopatria's 1415-1475 shapes, which keep them to 1468. Mema 1465; 1475 drop is a confidence-1 bridge; 1502 Diafunu; Kaabu 1537 (so the 1564 shape holds from 1537); Gambia suzerainty by 1576; end c. 1610 (shape trimmed from 1611).
- Unexplained by any page: the 1415 growth (+141,000 km2) and the 1463 and 1468 drops beyond Mema.
- Gao's independence is dated three ways: 1370s (Mali page), 1380s-90s (Songhai page text), c. 1430s (Songhai infobox); the infobox was followed.
- No ruler strip (no complete list with years on the pages). Capital Niani is disputed (page: no firm evidence of a royal residence).
- Counterparts needing dossiers: jolof-empire (c. 1360), kaabu (1537-1867), Tuareg of Timbuktu/Takedda, pre-imperial Gao (mapped to songhai-empire), Wuli.
- Gazetteer lacks Mema, Kita, Diafunu; Kayes and Nioro du Sahel used as proxies.

## empire-of-kanem (Kanem-Bornu)
- No page opened gives an area for any year: no infobox comparison was possible (Kanem-Bornu page infobox and text checked again on 2026-10-19).
- Founding c. 700 (Duguwa, Njimi) not mapped; start 1072 is Cliopatria's first year (bridge, confidence 1). Seshat td_kanem (https://seshat-db.com/core/polity/td_kanem/) failed twice with a client error on the second pass: pages_failed.
- Kanem ends 1380 and the Bornu core runs from 1381 (page "around 1380"); Cliopatria switches 1384/85.
- Alooma's reign (c. 1570-1603): Kanem expeditions and the Bilala treaty are undated (Idris Alooma page re-read 2026-10-19: "more than five military expeditions in Kanem", "clear demarcations", no year; only the sack of Amsaka, 4 December 1575, is dated); the contest pair 1570-1603 stays confidence 1. His influence over Hausaland, Aïr, Bilma, Tibesti and Kano is not drawn.
- 1809 loss to the Fulani is read from Cliopatria's 1808 and 1809 shapes (page lists no districts); contest 1808-1827, end year a bridge ("later in the 1820s", al-Kanemi page). The Kanem-Bornu page orders the expulsion differently (a sentence "The Fulani were driven away from the empire and mai Dunama was restored to power", with "Al-Kanemi supported Dunama's restoration in 1814"); the Fulani War page does not describe it: undated on all three.
- The Fulani War page calls the 1846 end of the Sayfawa a jihadist toppling; the Kanem-Bornu page makes it the shehu's coup. The latter is followed.
- Rabih az-Zubayr's state (c. 1892-1900, capital Dikwa) is the successor and needs a dossier: suggested slug state-of-rabih-az-zubayr. Also bagirmi-sultanate, the Bilala kingdom of Kanem (c. 1380-1630s), the Kotoko city states (Kousseri, Ngulfai, Logone) and the colonial split of 1902 (not in scope).
- Capital points: Njimi uses Mao (proxy, inside the region Kanem); Kukawa coordinates are approximate and not on the page; Kafela (mai's seat 1813-1846) has no point.
- Gazetteer names needed: Njimi, Kukawa, Kafela, Amsaka (page: modern-day Kaza near the border of Dikwa and Kala Balge, Borno state), Mafoni (Borno State), Kousseri, Ngulfai, Logone(-Birni).

### Second pass (author, 2026-10-19): fixes after review-af-03-a
Pages reopened: Kanem-Bornu Empire (twice), Dunama Dibbalemi, Fezzan (new, added to sources), Idris Alooma, Muhammad al-Amin al-Kanemi, Fulani War.
Applied:
1. empire-of-kanem_1072 (reviewer: Cliopatria shape disjoint from Kanem): verdict adjust, from 1072 to 1249, correction the region Kanem ("with a core territory in the region of Kanem (northeast of Lake Chad)"); the found event (ledger 0) draws the same region. The reviewer is right: the shape (15.1-16.7 E, 11.3-12.6 N) shares no cell with the region and does not contain Njimi; my first note ("a seventh of it") was wrong. The Cliopatria 1375 shape is the same outline and is replaced the same way.
2. 1350-1380 gap: new keyframe empire-of-kanem_1350 (1350-1374) and the 1375 entry (1375-1380) draw Kanem plus the Bornu core, i.e. the 1250 keyframe minus the Fezzan. The Dunama page ties "until the middle of the 14th century" to the Fezzan only and names no 14th-century loss of Kanem or Bornu. I split it into two entries (not one 1350-1380 entry) so each Cliopatria shape keeps its own review row; the shape is identical. Verdicts are adjust for both (the reviewer asked for adjust on the 1375 entry; for the 1072 entry adjust was the reviewer's first option, and one verdict for one outline is simpler; the correction replaces the outline wholly).
3. Bornu 1250-1349 vs 1381: I took the reviewer's second option and draw Bornu as the Bornu core of Cliopatria's 1385 shape from 1250 (ledger 2 and the keyframes agree: the same 52 cells throughout). I did not take the first option (Borno State to Mafoni, or the gazetteer region Bornu): the region Bornu is 331,000 km2 and includes Kanem, Lac and the whole of Diffa to 18 N, which no page gives to Bornu, and any larger outline would need a dated loss that no page supplies and would reopen an unexplained drop at 1385 or 1482 (Cliopatria's 1482 shape is 63,000 km2). Disagreement and gap: Dunama "reached as far south as Mafoni in modern day Borno State" (Dunama page) is partly beyond the core and is not drawn; the Kanem-Bornu page also says "The Sayfawa quickly regrouped in Bornu, re-establishing a powerful kingdom there", so the 1250-1480 Bornu land is probably larger than 13,000 km2. A gap-filler with a page that outlines 13th-15th-century Bornu should replace the core.
4. 1482 and 1487 corrections now subtract {"region": "Kanem"} (not the Cliopatria Kanem outline), so Kanem is out of the drawing for 1482-1499 as the ledger says. The old Cliopatria "Kanem" outline south-east of the lake stays in the 1482 shape as Cliopatria has it.
5. Ledger 13 (1824): confidence 2 kept (the reviewer's); region text says the province is a container for the three towns; counterpart changed from Bagirmi to the Kotoko city states (the page names them and does not say Bagirmi held them); Bagirmi stays a belligerent of the war entry.
6. Ledger 11 (1809): the region text now uses the page's words; the district list is marked as the Fulani War page's late-18th-century Galadima Dunama district, not a 1809 loss; Deya removed (the al-Kanemi page has al-Kanemi occupying "the Deya- Damaturu area" later in the 1820s).
Author's addition (not asked): ledger 7 (1500 gain of Kanem) is narrowed to the part of Kanem inside Cliopatria's 1487 shape (135 of 531 cells), because Cliopatria's Bornu shapes hold only that quarter of the region from 1487 to 1890; the drawing and the ledger now agree. Reading: the Bilala kept the rest (Alooma's peace with "the Bilala mai of Kanem", "clear demarcations"; Wadai drove the Bilala out c. 1630). If a reviewer prefers the whole region, the 1500-1890 keyframes must be widened too.
Still thin after the second pass (pages tried, all silent on the year): Bornu's incorporation under Dunama (Dunama page: no year); the end of the Fezzan grip (Fezzan page: "During the 13th and 14th centuries, the Fezzan became a part of the Kanem Empire", no end year, no taker; the Dunama page's "middle of the 14th century" is kept at confidence 1); Alooma's Kanem expeditions and the Bilala treaty (Idris Alooma page: undated); the year the Fulani were driven out (al-Kanemi page "Later in the 1820s"; Fulani War page: not described); founding c. 700 and the Hummay change (Seshat failed).
