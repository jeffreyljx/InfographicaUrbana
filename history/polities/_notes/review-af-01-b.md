# Review of batch af-01-b (Ethiopian Empire, Ifat, Adal, Makuria Kingdom, Funj)

Reviewer, 2026-10-18. The validator shows 0 errors for all five dossiers. `--resolve` warnings are slug warnings for the counterparts the author listed, one vassal_start with no end (the Gibe states), and gazetteer region names (the author's list; Sidamo, Welayta, Wollamo and Gimirra sit inside unions and do not appear as warnings, but they are unknown too). The only Context neighbour dossier on disk is alodia; I also grepped makuria and zagwe-dynasty (af-01-a) for the hand-overs. Everything else (ottoman-empire, sultanate-of-darfur, muhammad-ali-dynasty, italian-africa, british-africa, khedivate-of-egypt) has not been written yet.

Verdicts: ethiopian-empire **thin**, ifat-sultanate **fix** (one fix applied by the reviewer), adal-sultanate **fix** (one fix applied by the reviewer), makuria-kingdom **pass**, funj-sultanate **fail**.

## funj-sultanate: fail (back to the author)

1. **Blocking: Kordofan before 1755.** The keyframes funj-sultanate_1504 to _1636 (1504-1768) take Cliopatria's outline, which includes Kordofan: by the gazetteer, about 264,500 km2 of the 592,500 km2 shape, or 45 percent. The pages say Kordofan was not Funj before 1755:
   - Funj page: Kordofan was "a battlefield between the Funj and the Musabb'at"; "The Fur had the upper hand until 1755", when Abu Likaylik "finally managed to overrun Kordofan and turn it into his new powerbase".
   - Darfur page: "Over the previous centuries Kordofan had largely escaped control by any of the region's major states", though "the Funj Sultanate centred in Sennar projected influence over eastern Kordofan via the Ghudiyat"; "In 1734 Isawi of the Musabba'at had dislodged the Ghudiyat administration" and "repelled subsequent Funj attempts to regain their foothold"; "after Isawi's death Kordofan was conquered by Abu Likaylik".

   The ledger loses Kordofan in 1772 and 1785 but never gains it. **Fix:** mark the 1504-1636 keyframes adjust with corrections that subtract `{"region": "Kordofan"}` (keep at most eastern Kordofan until 1734, and say so); add a 1734 loss of eastern Kordofan (counterpart Musabba'at) and a 1755 gain of Kordofan from the Musabba'at (Funj page, confidence 2); recheck the 1665 Taqali vassalage (South Kordufan) against this.
2. /ledger/2, the Abdallab vassal_start of 1504 (confidence 1), is mis-dated. The page puts "The Abdallabi would receive everything north of the confluence" after Ajib's death "in 1611 or 1612", and the note's own quote ("ruling as vassal kings under Badi I") is from Badi I's reign. The note says the page "ties it to the founding", which the page does not. **Fix:** date it 1612, or cite a page for the earlier subordination.
3. /ledger/3 names banu-kanz for Dongola in 1523, but the Makuria page says "It is unclear who ruled Dongola after 1366". The year is confirmed ("by 1523"). Keep banu-kanz only with the makuria dossier's Banu Kanz source in the note.
4. Confirmed on the pages: Fazughli 1665, Hannik 1585, Dongola to the Shaykiyya c. 1782, Kordofan 1772, 1782 and c. 1785 (Darfur page), Taka after 1791, Gezira after 1802, Badi VII's surrender on 14 June 1821 (Turco-Egyptian page). There is no area figure on the page.

## ethiopian-empire: thin

Spot checks, all confirmed: 1299 (Wedem Arad and Ifat), 1316 and 1332 (Amda Seyon), 1531 and 1533 (Adal page), October 1544 (Ethiopian-Adal War page), 1557 (Habesh Eyalet), and Menelik II's 1881 to 1898 conquests: Arsi 1886, Wollega 1886, Harar 6 January 1887, Gurage 1889, Hadiya 1889 (Ethiopian Empire page), Bale, Sidamo, Ogaden and Welayta 1891, Kambata 1893, Gofa and Wollamo 1894, Beni Shangul, Lake Rudolf, Massonge and Gimirra 1898. Area: the infobox gives 1,221,900 km2 in 1954, after the dossier's end; against the 1932-1935 shape (1,128,249 km2) that is 0.92, acknowledged. The corrections of Cliopatria's 1547-1635 and 1636-1768 shapes are argued and acknowledged.

Not applied, for the author or a gap-filler:

1. **/keyframe_review/14 (1636 keyframe set to the 1769 shape).** After the 1579 keyframe (the 1502 shape, less Wej 1572, Shewa and Damot 1593, Bale 1607), nothing in the ledger removes Dawaro, Fatagar, Hadiya and the rest of the south. The 1502 shape minus the 1769 shape is about 206,900 km2, of which 154,500 km2 lies outside Shewa. Nothing gains the roughly 45,300 km2 in the west that the 1769 shape adds. The 1889 Hadiya gain (/ledger/36) re-takes a Hadiya the ledger never lost. Add a loss to the Oromo (counterpart nobody) of Dawaro, Fatagar and Hadiya, dated 1593-1636 at confidence 1. Source: the page's "much of the Empire's southern territory and vassals were lost", or a dated sentence on the Oromo migrations page.
2. **/ledger/39 (1891).** This event takes the whole Ogaden region (about 344,700 km2), but the 1895 and 1898 keyframes (ok) hold only about 83,500 and 97,100 km2 of it, and the 1900 shape about 335,100 km2. The page says "occupied from 1891 onward". Limit the 1891 part to the 1895 shape and add the rest c. 1899-1900, or mark the keyframes adjust.
3. **/wars: the 1874-1876 Ethiopian-Egyptian war is missing.** The Ethiopian Empire page: "From 1874 to 1876, the Empire re-expanded into Eritrea", "decisively beating the Egyptian forces at the Battle of Gundet in Hamasien". The counterpart is khedivate-of-egypt (me-10), so the notes' "no Egyptian counterpart on the page" is wrong.
4. **/ledger/1.** The 1299 contest_start lies outside every war (/wars/0 begins in 1316). Add a war for Wedem Arad's conflict with Ifat from 1299, here and in ifat-sultanate.
5. **Confidence-1 gaps:** 1329 Semien; Ifat land 1403-1415; the 1890 loss of Eritrea (try Treaty of Wuchale); 1895 (try First Italo-Ethiopian War); Kaffa 1900 (try Kingdom of Kaffa); 1907 (try the 1897 Anglo-Ethiopian treaty); and the Eritrean highlands 1769-1874.

## ifat-sultanate: fix

- **Applied by the reviewer:** /ledger/1 (the 1285 gain of the Sultanate of Shewa) goes from confidence 3 to 2. The Shewa page places the capital "in northern Hararghe" and the territory "possibly to areas west of the Awash River"; 'Harar (region)' (a 100 km circle round Harar) is a proxy, not a name on the page. The year is confirmed. The dossier was re-validated.
- **Not applied (missing mirror, same batch):** there is no vassal_start in 1332 or vassal_end in 1403 with counterpart ethiopian-empire, to match ethiopian-empire /ledger/7 and /ledger/9. Amda Seyon page: Sabr ad-Din "surrendered himself to Amda Seyon's camp"; "Amda Seyon then appointed the governor's brother, Jamal ad-Din I, as his successor in Ifat".
- **Not applied:** the 1299 contest_start (/ledger/3) lies outside both wars, as in ethiopian-empire.
- Confirmed: founded 1275, Hubat and Zeila 1288, Zeila as capital 1387-1403, defeat on the Harar plateau 1403, area 120,000 km2 against 121,451 km2 (1.01).

## adal-sultanate: fix

- **Applied by the reviewer:** /wars/3 (the Oromo invasion of Adal and Harar) ran to 1583, after the state's end in 1577. It is set to 1577 and the note says the 1583 fighting belongs to the Imamate of Aussa. The dossier was re-validated.
- Confirmed: 1415, the capital at Harar from 1520, Dawaro and Shewa 1531, Bete Amhara and Lasta 1533, October 1544, Nur in 1550, Aussa in 1577. Every territorial event has its mirror in ethiopian-empire. The page has no area figure.
- Thin: the 12 percent shrink of 1564 has no event; who held Harar 1577-1647; the site of Dakkar.

## makuria-kingdom: pass

The 1415 hand-over matches makuria's 1414 dissolve. The Dotawo page confirms the traditional end ("around the year 1500", "conquered by the Funj Sultanate, founded in 1504"). The clip to Lower Nubia and the wrong verdicts for 1507 and 1516 are backed by the Makuria page (the last king in the late 15th century; the 1518 "Nubian ruler" is unplaced). The start and end events are at confidence 1, honestly; the end is disputed (the Makuria page has "had finally disappeared by the 1560s"; the Dotawo infobox has the early 17th century).

## Cross-dossier

Inside the batch, every Ethiopia-Adal and Ethiopia-Ifat event is mirrored, except Ifat's missing vassal pair. The hand-overs with zagwe-dynasty, makuria and alodia match by year, but all three failed their own review (af-01-a), so their regions may change. Missing in both sides: the 1755 Kordofan gain (Funj) and the 1874-1876 Egyptian war (Ethiopia). Mirrors owed by groups that have not run: ottoman-empire (Massawa 1557), sultanate-of-darfur (Kordofan c. 1785), muhammad-ali-dynasty (June 1821), italian-africa (1890 and 1935-1936), british-africa (1907), khedivate-of-egypt (1874-1876).
