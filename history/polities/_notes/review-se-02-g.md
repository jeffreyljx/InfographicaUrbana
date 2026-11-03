# Review of batch se-02-g (2026-10-19)

Reviewer: adversarial review of seven dossiers (six owned states and the new rebel state). Validator: 0 errors on all seven before and after the reviewer's edits. Machine copy: history/notes/phase-b/reviews/se-02-g.json.

## patani-kingdom: thin

- **/ledger** (for the author, non-blocking): The dossier carries none of the Ayutthaya tributary spans that ayutthaya-kingdom records with patani-kingdom as counterpart (vassal_start 1512 c1, vassal_end 1563 c2, vassal_start 1584 c2, vassal_end 1688 c3). Evidence: Patani page: 'Raja Hijau (or Ratu Hijau, the Green Queen) came to the throne in 1584' and acknowledged Siamese authority; 'When Phetracha took control of Ayutthaya in 1688, Patani refused to acknowledge his authority and rebelled' (ayutthaya-kingdom /ledger/29, /31, /35, /56). The author's notes defer the tint to the Ayutthaya dossier, but the mirror rule needs both ledgers. Fix: Add vassal_start 1584 and vassal_end 1688, counterpart ayutthaya-kingdom, region {"region": "Pattani"} with text, source the Patani page (confidence 2 and 3); add 1512/1563 only if the author accepts Ayutthaya's reading of "subject to Siamese control for some time".
- Thin /ledger/3: When Kelantan (Jembal) ceased to be Patani's: the 1691 loss is a confidence-1 bridge on Cliopatria's row end; the page only has Patani incursions into Kelantan around the 1750s. Try https://en.wikipedia.org/wiki/History_of_Kelantan
- Thin /identity/predecessors/0: The Langkasuka hand-over (no dossier; no date). Try https://en.wikipedia.org/wiki/Langkasuka
- Thin /ledger/0: Founding year: infobox c. 1400, Hikayat Patani 1350-1450, founder dated c. 1488-1511 elsewhere on the page. Try https://en.wikipedia.org/wiki/Hikayat_Patani
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed.
- Area: Infobox gives no area (only "approximately the area of" Patani, Yala, Narathiwat); Cliopatria 11.9-19.8 k km2 matches that description.

## mataram-sultanate: fix

- **/ledger/18/region** (applied by reviewer, blocking): The 1676 loss to trunajaya-rebellion named only the coast towns, not Madura, although trunajaya-rebellion /ledger/0 founds the rebel state on Madura in 1676 with mataram-sultanate as counterpart and this ledger regains Madura from the rebels in 1677 (/ledger/20): Madura was drawn as both Mataram and rebel land 1676-1677. Evidence: Trunajaya page: 'In 1671 Trunajaya returned to Madura', 'the master of Madura'; 'In September 1676, a rebel army of 9,000 ... crossed over from Madura to Java.' Fix: Region is now {"union": [the three Madura circles of /ledger/20, the coast-town union]} with text "Madura and the northern coastal towns from Surabaya to Cirebon, Jepara excepted"; reviewer sentence appended to the note.
- **/ledger/20/confidence** (applied by reviewer, non-blocking): Confidence 1 with the note "The page does not say when", but the Trunajaya page dates the return of Madura to 1677. Evidence: Trunajaya page, after the April 1677 Surabaya campaign: 'VOC forces also took Madura, Trunajaya's native island, and laid his residence there in ruin.' Fix: Confidence 2 and the note quotes the sentence (applied together with the same change to trunajaya-rebellion /ledger/3).
- **/ledger/32** (for the author, non-blocking): A 1705 loss of "the regions of Cirebon" to dutch-republic removes land that lies outside every Mataram outline and after the dossier's own vassal_end of Cirebon (/ledger/27, c. 1680): the event has nothing to subtract. Evidence: Mataram page: 'In 1705 he agreed to cede the regions of Cirebon and eastern part of Madura'; the author's own note says 'Cirebon is outside every Mataram outline and had left Mataram's orbit by c. 1680'. Fix: Delete /ledger/32 and mention the Cirebon clause in the note of /ledger/31; or, if Mataram's claim is kept to 1705, move /ledger/27 to 1705 and drop the loss.
- **/ledger/11/counterpart** (for the author, non-blocking): The Cirebon vassalage (1625-1680) uses the free string "Cirebon (sultanates)" although sultanate-of-cirebon has a dossier (1482-1677) that records no Mataram suzerainty. Evidence: Mataram page: 'Cirebon too was forced to shift allegiance from Mataram to the Dutch'; sultanate-of-cirebon /ledger/3-6 partition the state in 1677. Fix: Use counterpart sultanate-of-cirebon for the 1625 vassal_start with its vassal_end at 1677 (the partition; the Trunajaya page has Cirebon declaring independence in 1677-1678), or keep the string and say in the note that it covers the 1677 successor sultanates; the Cirebon group should add the mirror.
- Thin /ledger/2: The 1588 Madiun-Kediri strip in Cliopatria's first outline (confidence 1; no page dates it). Try https://en.wikipedia.org/wiki/Panembahan_Senopati
- Thin /ledger/11: Start of the Cirebon relation (confidence 1). Try https://en.wikipedia.org/wiki/Sultanate_of_Cirebon
- Thin /ledger/12: Start of the Priangan (Sumedang, Ukur) relation (confidence 1). Try https://en.wikipedia.org/wiki/Sumedang_Larang_Kingdom
- Thin /ledger/15: End of Sukadana's vassalage (confidence 1 at Agung's death). Try https://en.wikipedia.org/wiki/Tanjungpura_Kingdom
- Thin /ledger: Palembang and Jambi vassals named on the Mataram page ("with vassals in Palembang, Sukadana, and Jambi") are not recorded; no years. Try https://en.wikipedia.org/wiki/Palembang_Sultanate
- Thin /ledger/33: The 1743 cession of the Pasisir: the Mataram page has Pakubuwono II "ceded sovereignty over the Pasisir to the VOC" after the 1741 rebellion but no treaty date. Try https://en.wikipedia.org/wiki/Java_War_(1741%E2%80%931743)
- Spot checks: /ledger/9 confirmed; /ledger/10 confirmed; /ledger/13 confirmed; /ledger/33 confirmed; /ledger/4-7 confirmed; /ledger/0, /ledger/1, /ledger/30-31 confirmed.
- Area: No infobox area. The page: "At its greatest extent, Mataram's territory spanned most of mainland Java and Madura"; the author compares Java with Madura (about 133 k km2) against 65.7 k (ratio 0.49) in /keyframe_review/2 and explains the missing West Java and Blambangan. Central Java, Yogyakarta and East Java with Madura are about 83 k km2, so the outline is plausible.

## trunajaya-rebellion: fix

- **/ledger/6** (applied by reviewer, non-blocking): Mis-dated at confidence 2: the note says the page gives 1677-1678 for Puger seizing Plered; the page says 1677. Evidence: Trunajaya page: Pangeran Puger 'had taken the old capital in Plered and had claimed the throne for himself in 1677' (after the rebels withdrew to Kediri in June 1677). Fix: Confidence lowered to 1 and the note quotes the page; the year stays 1678 only to keep the event after the June 1677 capture (no month on the page). If a page gives the month, move it to 1677 with that month.
- **/ledger/3/confidence** (applied by reviewer, non-blocking): Confidence 1 with "The page does not say when or how", but the page dates the loss of Madura to the 1677 Surabaya campaign. Evidence: Trunajaya page: 'VOC forces also took Madura, Trunajaya's native island, and laid his residence there in ruin.' Fix: Confidence 2 and the note quotes the sentence; a reviewer sentence is appended to /keyframe_review/1/note.
- Thin /ledger/3: When the coast towns other than Surabaya (Tuban, Demak, Pati, Semarang, Tegal) left rebel hands after April 1677. Try https://en.wikipedia.org/wiki/Cornelis_Speelman
- Spot checks: /ledger/0 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/7 confirmed; /ledger/6 mis-dated.
- Area: No Cliopatria row and no infobox area; rebel land is circles round named towns.

## sultanate-of-sambas: pass

- Thin /keyframe_review/0: The early realm (1609-1731) was smaller than Cliopatria's late outline (Tanjung Datuk to the Duri River, under the 4th sultan); no step is dated. Thin by design within the 1-2 page budget. Try https://en.wikipedia.org/wiki/Sambas_Regency
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /wars/0 confirmed.
- Area: Infobox gives no area; Cliopatria 5.8 k km2 for the Sambas and Paloh basins is plausible.
- Tried: Years, the found/dissolve pair, the Brunei link (the page dates only Sultan Tengah's arrival, 1639), capital inside the bbox, the 1820 "wrong" verdict (years only); could not break it. The Brunei dossier's 1619 loss to Sambas is a Brunei-side mismatch (cross_checks).

## sultanate-of-mempawah: fail

- **/ledger/0/confidence** (applied by reviewer, non-blocking): Confidence 1 with "The page gives no founding year", but the page has a founding sentence for c. 1610. Evidence: Mempawah page: 'Two hundred years later, or around 1610, a new government was established' 'that was built on the former ruins of the Sidiniang Kingdom.' Fix: Confidence 2 and the note quotes the sentence.
- **/ledger** (for the author, blocking): The 1787 Dutch intervention is missing from the ledger and wars: the Dutch landed, beat Panembahan Adiwijaya, who withdrew inland to Karangan, and installed the Pontianak prince Syarif Kasim Alkadrie by agreement; the map shows Mempawah fully independent 1787-1831. Evidence: Mempawah page: 'Not long after the Dutch landed in Mempawah in about 1787' 'there was a battle against the troops of Mempawah led by Panembahan Adiwijaya'; 'Panembahan Adiwijaya finally withdrew to Karangan in Mempawah to arrange a counterattack'; 'The appointment of Syarif Kasim Alkadrie as Panembahan was enshrined in the agreement dated 27 August 1787'; the Pontianak conflict flared again around 1794. The author quotes the agreement only inside the 1831 dissolve note. Fix: Add vassal_start 1787 month 8 (counterpart dutch-republic, or pontianak-kadriyah-sultanate if the VOC acted through Pontianak; region the Cliopatria Mempawah 1619 shape; confidence 3) with its vassal_end at 1831; add a war "Dutch-Pontianak intervention in Mempawah" 1787-1790 with a contest zone round Karangan (Adiwijaya died in 1790 before his counterattack, per the page); say in notes whether 1787 or 1831 ends independence.
- Thin /ledger/0: Mempawah's relation to the Matan Sultanate before 1740 ("concurrent with the Matan Sultanate") and to Landak. Try https://en.wikipedia.org/wiki/Pontianak_Sultanate
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.
- Area: Infobox gives no area (Established 1740, Disestablished 1944); Cliopatria 2.9 k km2 round the Mempawah River is plausible.

## sultanate-of-sukadana: fix

- **/ledger** (for the author, non-blocking): No mirror of mataram-sultanate /ledger/8 (vassal_start 1622, counterpart sultanate-of-sukadana) and /ledger/15 (vassal_end 1645); the 1622 Mataram expedition is only a war with no zones here. Evidence: Tanjungpura page: 'Adipati Kendal with his Mataram Expedition, attacked Matan (1622)'; Sultan Agung page: 'capturing Sukadana, Surabaya's ally in southwest Kalimantan, in 1622'; Mataram page: 'with vassals in Palembang, Sukadana, and Jambi'. Fix: Add vassal_start 1622 (confidence 2) and vassal_end 1645 (confidence 1, the Mataram dossier's bridge), counterpart mataram-sultanate, region {"cliopatria": "Sultanate of Sukadana", "year": 1619} with text. Non-blocking: the tint is already drawn from the Mataram side.
- Thin /identity/end: The infobox's "Part of the Dutch East Indies (from 1779)" is unexplained by any sentence; the 1833 end is a succession dispute, not a cession. Try https://en.wikipedia.org/wiki/Ketapang_Regency
- Thin /keyframe_review/1: The page's claim that the territory "stretched from Tanjung Dato to Tanjung Sambar" (the whole west coast) against Cliopatria's southern Matan outline: acknowledged in the note, undated. Try https://en.wikipedia.org/wiki/Tanjungpura_Kingdom
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.
- Area: Infobox gives no area; Cliopatria 11.5 k km2 is the Matan coast; the page's Tanjung Dato to Tanjung Sambar claim is acknowledged in /keyframe_review/1.

## sultanate-of-bima: fail

- **/ledger/2** (applied by reviewer, blocking): The vassal_end of the Flores dependencies lay in 1920, after the state's end (1621..1905), and after the dissolve in the ledger. Evidence: Bima page: 'In 1920 Bima lost control over Manggarai'; 'In 1905 Bima was turned into a "fief" (leen)' (the dossier's end). Fix: Moved to 1905 before the dissolve, confidence 2, note quotes the 1920 sentence (was /ledger/3).
- **/ledger** (for the author, blocking): The VOC subordination from 8 December 1669 is missing: the dossier draws Bima as fully independent 1669-1905, and no other dossier carries the relation yet. Evidence: Bima page: 'The Bima Sultanate surrendered to the VOC on 8 December 1669' under an agreement signed in Batavia; after this Bima and the other Sumbawan kingdoms were 'subordinated allies of the VOC'. The author quotes it only in the report's problems. Fix: Add vassal_start 1669 month 12, counterpart dutch-republic (region the Sumbawa core, confidence 3), with vassal_end 1799/1800 and a new vassal_start of dutch-east-indies from 1800 (or whatever split the Dutch dossiers use) ending at the 1905 dissolve; add the 1669 surrender to the "VOC subjugation of Bima" war note.
- **/ledger** (for the author, non-blocking): No mirror of sultanate-of-gowa /ledger/8 (vassal_start 1626) and /ledger/16 (vassal_end 1667), which Gowa files against the free string "Sumbawa". Evidence: Bima page: 'Sumbawa was attacked through three expeditions in 1618, 1619, and 1626'; Bima's ruler 'signed a contract of alliance with Makassar'; 'A rebellion against his Makassarese-backed rule took place in 1632-33'. Fix: Add vassal_start 1626 (confidence 2) and vassal_end 1667 (confidence 2), counterpart sultanate-of-gowa; the Gowa group should change its counterpart string to sultanate-of-bima.
- Thin /ledger/0: Start of the Flores/Sumba tribute (the page: "according to tradition", peak in the 15th century). Try https://en.wikipedia.org/wiki/Manggarai_Regency
- Thin /keyframe_review/2: Cliopatria's 1866 shape drops the Bima plain (bbox 119.21 E against 118.54 E); no page explains it (the author keeps the core, reasonably). Try https://en.wikipedia.org/wiki/Bima_Sultanate
- Spot checks: /ledger/1 confirmed; /ledger/3 confirmed; /ledger/2 confirmed; /ledger/0 confirmed.
- Area: Infobox gives no area; Cliopatria 10.4 k km2 (eastern Sumbawa plus Komodo and west Flores) with the Flores part moved to a tint.

## Cross-dossier matrix (unmatched and exceptions)

- ayutthaya-kingdom 1512 vassal_start (counterpart patani-kingdom) -> missing: Patani carries no vassal events (also 1563 vassal_end, 1584 vassal_start, 1688 vassal_end); fix listed on patani-kingdom.
- ayutthaya-kingdom 1584 vassal_start (counterpart patani-kingdom) -> missing: see above; 1688 vassal_end likewise.
- patani-kingdom 1616 gain (counterpart Kelantan fiefdoms) -> exception: no dossier; listed as kelantan-jembal in counterparts_needing_dossiers.
- patani-kingdom 1691 loss (counterpart Kelantan fiefdoms) -> exception: same; confidence-1 bridge.
- patani-kingdom 1400 found (counterpart langkasuka) -> exception: langkasuka listed in counterparts_needing_dossiers.
- mataram-sultanate 1584 found (counterpart kingdom-of-pajana) -> missing: Pajang (1568-1586) records no 1584 loss of the Kota Gede core; route to se-02 (Pajang).
- mataram-sultanate 1586 gain (counterpart kingdom-of-pajana) -> matched: Pajang /ledger/3 dissolve with counterpart mataram-sultanate.
- mataram-sultanate 1588 gain (counterpart East Java principalities) -> exception: confidence-1 bridge for the Madiun-Kediri strip; no state named.
- mataram-sultanate 1615 gain (counterpart Wirasaba) -> exception: no dossier and not in the author's counterparts_needing_dossiers; added to this report's list (or fold into the Surabaya-league dossier).
- mataram-sultanate 1616 gain (counterpart Lasem) -> exception: no dossier and not in the author's counterparts_needing_dossiers; added to this report's list (or fold into the Surabaya-league dossier).
- mataram-sultanate 1617 gain (counterpart Pasuruan) -> exception: no dossier and not in the author's counterparts_needing_dossiers; added to this report's list (or fold into the Surabaya-league dossier).
- mataram-sultanate 1619 gain (counterpart Tuban) -> exception: no dossier and not in the author's counterparts_needing_dossiers; added to this report's list (or fold into the Surabaya-league dossier).
- mataram-sultanate 1622 vassal_start (counterpart sultanate-of-sukadana) -> missing: in-batch: Sukadana records the 1622 expedition only as a war; fix listed on sultanate-of-sukadana (also the 1645 vassal_end).
- mataram-sultanate 1624 gain (counterpart Madura (Surabaya's ally)) -> exception: madura listed in counterparts_needing_dossiers.
- mataram-sultanate 1625 gain (counterpart Surabaya) -> exception: surabaya listed.
- mataram-sultanate 1625 vassal_start (counterpart Cirebon (sultanates)) -> missing: sultanate-of-cirebon (1482-1677) has a dossier with no Mataram vassalage; Mataram uses a free string; fix listed on mataram-sultanate /ledger/11; route the mirror to se-02 (Cirebon).
- mataram-sultanate 1631 vassal_start (counterpart Sumedang and Ukur (Priangan)) -> exception: sumedang-larang listed; vassal_end 1677/9 likewise.
- mataram-sultanate 1639 vassal_start (counterpart blambangan-kingdom) -> mismatch: Blambangan ends its 1635-1639 contest with Mataram but records no vassal_start/vassal_end (its keyframe note says the Mataram dossier should carry the 1639-1659 tint); route the mirror to se-02 (Blambangan).
- mataram-sultanate 1659 vassal_end (counterpart blambangan-kingdom) -> missing: as above; Blambangan's 1665 note (Tawang Alun freed it during the Trunajaya revolt) disagrees with the Mataram page's 1659.
- mataram-sultanate 1676 loss (counterpart trunajaya-rebellion) -> matched: after the reviewer added Madura to /ledger/18 (rebel found on Madura, gain of the coast).
- mataram-sultanate 1677 loss (counterpart trunajaya-rebellion) -> matched: Kediri.
- mataram-sultanate 1677 gain (counterpart trunajaya-rebellion) -> matched: Madura and the rest of the coast; both now confidence 2.
- mataram-sultanate 1677 gain (counterpart trunajaya-rebellion) -> matched: Surabaya, April 1677 on both sides.
- mataram-sultanate 1677 loss (counterpart trunajaya-rebellion) -> matched: Plered, June 1677 on both sides.
- mataram-sultanate 1678 gain (counterpart trunajaya-rebellion) -> matched: Kediri, 25 November 1678 on both sides.
- trunajaya-rebellion 1678 loss (counterpart Pangeran Puger) -> exception: puger-regime-plered listed; Mataram regains Plered from Puger in 1680 and 1681 (also exceptions).
- mataram-sultanate 1705 loss (counterpart dutch-republic) -> exception: dutch-republic (eu-09) not written yet; three 1705 losses (Semarang, eastern Madura, Cirebon; the Cirebon one should go, see fixes).
- mataram-sultanate 1743 loss (counterpart dutch-republic) -> exception: dutch-republic not written; Cliopatria's Dutch Republic row covers the coast from 1744.
- sultanate-of-brunei 1619 loss (counterpart sultanate-of-sambas) -> mismatch: Brunei loses three cells to Sambas in 1619 (confidence 1, Cliopatria's first Sambas year); Sambas holds that land from its 1609 found with no counterpart, and its page dates no Bruneian rule. Route to se-02 (Brunei): move the loss to 1609 or drop it.
- sultanate-of-gowa 1626 vassal_start (counterpart Sumbawa) -> mismatch: Gowa uses the free string "Sumbawa" (vassal 1626-1667); Bima has no vassal events; fix listed on sultanate-of-bima; Gowa should use slug sultanate-of-bima.
- sultanate-of-bima 1621 vassal_start (counterpart Manggarai and West Flores dependencies) -> exception: manggarai listed; vassal_end now 1905.
- sultanate-of-bima 1669 vassal_start (counterpart dutch-republic) -> missing: not in the ledger at all (fix listed); dutch-republic (eu-09) and dutch-east-indies (se-03) not written yet.
- sultanate-of-mempawah 1787 vassal_start (counterpart dutch-republic / pontianak-kadriyah-sultanate) -> missing: not in the ledger (fix listed); counterparts not written yet (eu-09, se-03).

## Counterparts needing dossiers (added by the reviewer)

- Wirasaba (East Java principality) (wirasaba): conquered by Mataram 1615 (Sultan Agung page); or fold into the Surabaya league
- Lasem (lasem): conquered by Mataram 1616
- Pasuruan (principality) (pasuruan): taken from Blambangan by Demak 1545-1546 (Blambangan dossier); conquered by Mataram 1617
- Tuban (tuban): conquered by Mataram 1619
