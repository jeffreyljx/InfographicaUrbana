# Review of batch se-03-b (reviewer, 2026-10-19)

Validator: all four dossiers valid, no errors (warnings: unwritten slugs straits-settlements, federated-malay-states, dutch-east-india-company, dutch-new-guinea; gazetteer lacks Naning).
Pages opened: Kelantan, Kelantan_Sultanate, Pontianak_Sultanate, Negeri_Sembilan, Dutch_East_Indies, Dutch_New_Guinea, Padri_War, Anglo-Dutch_Treaty_of_1814, Anglo-Dutch_Treaty_of_1824, Indonesian_National_Revolution. No date checked on them was fabricated or wrong.

## kelantan: fail
Area: infobox 15040 km2 (1957), Cliopatria 8555.4 km2, ratio 0.57, acknowledged True. infobox is the modern state; ratio inside a factor of two and stated in keyframe kelantan_1762
Findings:
- [BLOCKING] `/ledger`: No vassal events for the Siamese suzerainty, although rattanakosin-kingdom /ledger/7 (vassal_start 1786, counterpart kelantan) and /ledger/40 (vassal_end 1909-07, counterpart kelantan) need a mirror here; the notes say the tint 'belongs to the rattanakosin-kingdom dossier', which is the same one-sided reading the se-03-a review failed in sultanate-of-terengganu. Evidence: Kelantan page infobox: 'Siamese control: 1786'; Kelantan_Sultanate page: 'became a separate tributary of Siam in 1812'. Rule 3 of the reviewer brief: a vassal_start of X is a vassal_start in X's ledger with this state as counterpart. Fix: Add vassal_start 1786 (counterpart rattanakosin-kingdom, region cliopatria Kelantan 1762, source the Kelantan page infobox, confidence 2, note the 1812 date of the Sultanate page) and vassal_end 1909-07 (counterpart rattanakosin-kingdom, source Kelantan_Sultanate: 'transferred to British Protection on 19 July 1909').
- [not blocking] `/ledger/5/note`: The second quotation ('Under the terms of the Anglo-Siamese Treaty of 1909, the Thais relinquished ...') is not on the cited Kelantan_Sultanate page; it is on the Kelantan page. Evidence: WebFetch of Kelantan_Sultanate: the Anglo-Siamese Treaty is not mentioned; the Kelantan page has 'the Thais relinquished their claims over Kelantan, Terengganu, Kedah and Perlis to the British Empire'. Fix: Say '(Kelantan page)' after the second quotation; the date stays.
- [not blocking] `/ledger/1`: The 1795-1800 contest has no mirror in sultanate-of-terengganu (se-03-a), whose ledger holds no event naming kelantan. Evidence: grep of sultanate-of-terengganu ledger: only 1909 events. Fix: Nothing to change here; route to se-03-a (Terengganu should carry contest_start 1795 / contest_end 1800 naming kelantan).
Thin (for a gap-filler):
- `/ledger/4`: Counterpart and cause of the 1890 one-cell (about 230 km2) loss; counterpart is a free string 'unnamed neighbour (pages silent)'. Likely a Cliopatria artefact: if no page names it, drop the event and mark keyframe kelantan_1890 adjust (carry the 1762 outline). Try https://en.wikipedia.org/wiki/Anglo-Siamese_Treaty_of_1909
Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kelantan_Sultanate: confirmed (c. 1760, raja at Kubang Labu 'succeeded in reuniting the disparate territories under a single ruler')
- `/ledger/1` https://en.wikipedia.org/wiki/Kelantan_Sultanate: confirmed ('Following the death of Raja Yunus in 1795, control of the state passed to Terengganu')
- `/ledger/2` https://en.wikipedia.org/wiki/Kelantan: confirmed ('The pro-Terengganu faction was defeated in 1800')
- `/ledger/5` https://en.wikipedia.org/wiki/Kelantan_Sultanate: confirmed (19 July 1909); the treaty quote is on the Kelantan page
- `/ledger/3` https://en.wikipedia.org/wiki/Kelantan_Sultanate: confirmed (Istana Balai Besar 'constructed in 1840'; Kelantan page has Kota Bharu 1844)

## pontianak-kadriyah-sultanate: fail
Area: infobox None km2 (None), Cliopatria 4060.7 km2, ratio None, acknowledged True. page gives no area; said in keyframe 1
Findings:
- [BLOCKING] `/ledger`: No vassal events, although dutch-east-indies /ledger/1 (vassal_start 1800, counterpart pontianak-kadriyah-sultanate) and /ledger/69 (vassal_end 1949-12) need a mirror here; the notes push the tint onto the suzerain's dossier only. Evidence: Pontianak_Sultanate infobox status: 'Part of the Dutch East Indies (from 1779)'; the VOC 'endorsement as the sultan of Pontianak ... in 1779'. Reviewer brief rule 3. Fix: Add vassal_start 1800 (counterpart dutch-east-indies, region cliopatria Pontianak Kadriyah Sultanate 1772, source Pontianak_Sultanate, confidence 2, note the 1779 VOC endorsement) and vassal_end 1949-12 (counterpart dutch-east-indies).
- [not blocking] `/ledger`: The dossier draws the sultanate to 1950 but records nothing for the Japanese occupation, during which the page says the Japanese 'destroyed the Pontianak Sultanate' (24 January 1944) and killed the sultan (28 June 1944). Evidence: Pontianak_Sultanate page, quoted in the dossier's own keyframe 3 note; dutch-east-indies /ledger/52 and empire-of-japan /ledger/58 occupy the land in 1942. Fix: Add occupation_start 1942 and occupation_end 1945 (counterpart empire-of-japan), or say in notes why the occupation is carried only by the dutch-east-indies dossier.
- [not blocking] `/ledger/1`: The 17 August 1950 end is on the page, but the same page also has the region joining the Republic 'Prior to 5 April 1950'; the note does not mention the conflict. Evidence: WebFetch of Pontianak_Sultanate. Fix: Mention the April 1950 wording in the note (or lower confidence to 2).
Thin (for a gap-filler):
- `/keyframe_review/3`: Any page for the extent of the sultanate as a Dutch dependency 1828-1950 (carried forward at confidence 1) and the West Borneo convention (sambas, mempawah stop at Cliopatria years). Try https://en.wikipedia.org/wiki/Special_Region_of_West_Kalimantan
Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Pontianak_Sultanate: confirmed (infobox 'Established 23 October 1771')
- `/ledger/1` https://en.wikipedia.org/wiki/Pontianak_Sultanate: confirmed (17 August 1950; page also says 'Prior to 5 April 1950')
- `/keyframe_review/3/note` https://en.wikipedia.org/wiki/Pontianak_Sultanate: confirmed (24 January 1944, 28 June 1944, 29 October 1945, 28 October 1946)
- `/identity/predecessors` https://en.wikipedia.org/wiki/Pontianak_Sultanate: confirmed (infobox: Tanjungpura Kingdom and Mempawah Kingdom)

## negeri-sembilan: fix
Area: infobox 6686 km2 (1895), Cliopatria 2158.7 km2, ratio 0.32, acknowledged True. modern state; the 1890-1894 shape is the Seri Menanti Confederation without Sungai Ujong and Jelebu, explained in keyframe 4; the 1775 shape (5,900 km2) is 0.88 of it
Findings:
- [applied by reviewer] `/ledger/5/counterpart and /ledger/6/counterpart`: The 1895 gains of Sungai Ujong and Jelebu named free strings ('Sungai Ujong (British-protected domain)', 'Jelebu (British-protected domain)') while the 1874 and 1883 losses of the same land name british-colonial-empire, so the dossier's own loss/gain pairs did not match. Evidence: Negeri_Sembilan page: the British 'intervened militarily in a leadership tussle in Sungai Ujong' (1874), 'Jelebu followed in 1883', and 'The domains of Sungai Ujong and Jelebu joined this confederation in 1895'; /ledger/2 and /ledger/3 name british-colonial-empire. Fix: Counterpart set to british-colonial-empire on both 1895 gains (applied by the reviewer; re-validated, no new warnings).
- [not blocking] `/keyframe_review/3`: Keyframe negeri-sembilan_1877 (1877-1889) is verdict ok, yet the ledger's 1883 Jelebu loss (about 1,350 km2, some 37 percent of the 3,626 km2 shape) falls inside it; the note says so but the verdict does not. Evidence: shapes.csv: 1877 shape 3,626 km2, 1890 shape 2,159 km2 (the difference is Jelebu); reviewer brief rule 4: an event inside one shape's span is fine only if small or the keyframe is marked adjust for it. Fix: Mark keyframe 3 adjust and say in its correction text that from 1883 the outline is the 1877 shape minus Jelebu (or split it into 1877-1882 and 1883-1889 keyframes). Not blocking.
Thin (for a gap-filler):
- `/keyframe_review/1`: Years for the loss of Klang (to Selangor), Segamat (to Johor) and Ulu Pahang (to Pahang); the page says only 'in the 19th century'. Cliopatria's 1775 outline already omits them, so no event is drawn wrong. Try https://en.wikipedia.org/wiki/Seri_Menanti
Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Negeri_Sembilan: confirmed (Johor 'granting the title Yamtuan Seri Menanti' in 1773; nine luaks listed)
- `/ledger/1` https://en.wikipedia.org/wiki/Negeri_Sembilan: confirmed ('Naning was incorporated into the Straits Settlement of Malacca in 1832 following the Naning War')
- `/ledger/3` https://en.wikipedia.org/wiki/Negeri_Sembilan: confirmed ('Jelebu followed in 1883 and Rembau in 1887')
- `/ledger/4` https://en.wikipedia.org/wiki/Negeri_Sembilan: confirmed (1889, Seri Menanti 'combined with the domains of Tampin and Rembau')
- `/ledger/5` https://en.wikipedia.org/wiki/Negeri_Sembilan: confirmed (Sungai Ujong and Jelebu 'joined this confederation in 1895'; infobox 'Federated into FMS: 1895')

## dutch-east-indies: fail
Area: infobox 1919440 km2 (1930), Cliopatria 2023053.6 km2, ratio 1.05, acknowledged True. infobox gives no year; the author reads it as greatest extent (population 1930); compared with the 1915-1940 shape in keyframe 29
Findings:
- [applied by reviewer] `/identity/wikidata`: wikidata was null. Evidence: polities.csv row dutch-east-indies has wikidata Q188161 (Wikipedia title Dutch East Indies). Fix: Set to "Q188161" (applied by the reviewer; re-validated).
- [applied by reviewer] `/ledger/26/counterpart and /wars/2/belligerents/1`: The 1837 Minangkabau gain and the Padri War named a free string ('Padri movement and the Pagaruyung kingdom (Minangkabau highlands)') although padri-movement has a dossier whose /ledger/7 is loss 1837-08 to dutch-east-indies. Evidence: Padri_War page: 'on 16 August 1837, Fort Bonjol was completely conquered'; padri-movement /ledger/7. Fix: Counterpart and belligerent set to padri-movement (applied by the reviewer; re-validated). The Pagaruyung half is the next finding.
- [BLOCKING] `/keyframe_review/24/correction`: The 1895-1897 correction (wrong Qajar polygon) uses the 1898 outline, whose note says it holds 'the 1894 land plus Lombok'; but keyframe 25's own note gives the 1898 shape +1,934 cells over 1890-1894 (Kalimantan interior about 1,500, West Sumatra, Jambi, Bengkulu), which /ledger/45 gains only in 1898. Correction and ledger disagree on roughly 500,000 km2 for three years. Evidence: keyframe 25 note; /ledger/45 region = DEI 1898 minus DEI 1894 minus Lombok; shapes.csv 1890 = 1,270,220 km2, 1898 = 1,768,134 km2. Fix: Correction for 1895-1897 = union of (minus DEI 1890, Malaysia), region Minangkabau and place Mataram 55 km (Lombok), text 'the 1890-1894 outline plus Lombok (1894)'.
- [BLOCKING] `/ledger (Bali)`: Bali's dossier records contest_start 1846, contest_end 1849, loss of Karangasem 1894 (place Amlapura) and loss of Badung 1906 (place Denpasar), all to dutch-east-indies; this ledger has only the 1849 north-Bali gain, the 1894 Lombok gain (counterpart 'rulers of Lombok') and the 1908 gain. Evidence: bali /ledger/1, /2, /4, /5; Dutch_East_Indies page: 'failed expeditions ... in 1846 and 1848', 'Bali was subjugated with military conquests in 1906 and 1908'; DEI /wars/7 'Dutch interventions in Bali 1846-1908' has no contest events. Fix: Add contest_start 1846 / contest_end 1849 (counterpart bali, northern Bali), a 1894 gain of Karangasem from bali (place Amlapura 25 km) and a 1906 gain of Badung from bali (place Denpasar 15 km); restrict the 1908 gain to what is left.
- [BLOCKING] `/ledger (Pagaruyung)`: pagaruyung-kingdom /ledger/8 is loss 1833-05 of the Minangkabau highlands to dutch-east-indies; this ledger gains the whole Minangkabau region only in 1837 from the Padri. Evidence: Padri_War page: the sultan 'was captured by the troops of Lieutenant Colonel Elout on 2 May 1833 in Batusangkar'; 'At the beginning of August 1831, Lintau was successfully conquered and put Luhak Tanah Datar under Dutch control'. Fix: Add gain 1833-05 from pagaruyung-kingdom (Tanah Datar round Batusangkar) and restrict the 1837 gain from padri-movement to Agam, Limapuluh Koto and Bonjol (padri-movement /ledger/7 region); keyframe 11 correction to match.
- [BLOCKING] `/ledger (Bulungan)`: kingdom-of-bulungan records vassal_start 1834-09, vassal_end 1878-06 and dissolve 1878-06 to dutch-east-indies; nothing here. Evidence: kingdom-of-bulungan /ledger/6, /9, /10 (27 September 1834 protectorate agreement). Fix: Add vassal_start 1834-09 and vassal_end 1878-06 (counterpart kingdom-of-bulungan) and a 1878 gain, or route if the land is already in a Cliopatria gain.
- [BLOCKING] `/ledger (Gowa)`: sultanate-of-gowa records vassal_start 1800 and vassal_end/loss 1911 to dutch-east-indies; nothing here (the 1905 south-west Sulawesi gain names Bone only). Evidence: sultanate-of-gowa /ledger/23-25. Fix: Add vassal_start 1800 / vassal_end 1911 (counterpart sultanate-of-gowa) and name Gowa in the 1905 or a 1911 gain.
- [BLOCKING] `/ledger (Moluccan sultanates)`: Ternate (loss and dissolve 1914), Tidore (occupation 1806-1811, dissolve 1905) and Bacan (dissolve 1889) record events with dutch-east-indies that have no mirror here; conversely /ledger/15 (gain 1824 from sultanate-of-ternate, c1) has no mirror in Ternate. Evidence: sultanate-of-ternate /ledger/14-15; sultanate-of-tidore /ledger/12, /14, /17; sultanate-of-bacan /ledger/6. Fix: Add the Moluccan sultanates as vassals (vassal_start 1800 or 1817, vassal_end at 1889/1905/1914 with gains), or agree one reading with se-02 and change /ledger/15.
- [BLOCKING] `/ledger (Javanese courts)`: /ledger/23-24 open vassalage of sultan-of-yogyakarta and surakarta-sunanate in 1830 and /ledger/56-57 close it in 1945, but both dossiers end in 1830 and record vassal_start 1806, vassal_end 1811, vassal_start 1816 and vassal_end/dissolve 1830 with dutch-east-indies, none mirrored here. Evidence: sultan-of-yogyakarta /ledger/5, 6, 12-15; surakarta-sunanate /ledger/6, 7, 10-13; Yogyakarta infobox (quoted there): 'Protectorate state ... (1806-1811; 1816-1942)'. Fix: Agree with se-03-a: either the courts' dossiers run to 1945 as vassals (then add the 1806/1811/1816 events here) or drop the 1830-1945 vassal events here.
- [BLOCKING] `/ledger/27`: Kutai gain dated 1846 (c1) from the unwritten slug sultanate-of-kutai-kartanegara, while the existing dossier kutai-kingdom (cliopatria_names includes 'Sultanate of Kutai Kartanegara') records loss 1844 to dutch-east-indies at c2. Evidence: kutai-kingdom /ledger/5: 'In 1844 ... the Dutch defeated the sultan, forced him into exile, and took direct control of Kutai' (Kutai page). Fix: Move to 1844 citing the Kutai page, counterpart kutai-kingdom (unless the orchestrator splits the row), and mark keyframe 11 (1836-1845) for it.
- [BLOCKING] `/ledger/14`: Sambas gain dated 1822 (c1) while sultanate-of-sambas dissolves in 1819 ('The Dutch took control in 1819', c3); three years apart. Evidence: sultanate-of-sambas /ledger/2; the note of /ledger/14 cites that date itself. Fix: Date the gain 1819 from the Sambas page (counterpart sultanate-of-sambas) and mark keyframe 5 (1815-1821) for it.
- [BLOCKING] `/ledger/20 and /ledger/43`: Mempawah gain 1828 and Bima gain 1890 (both c1) have no mirror: sultanate-of-mempawah has vassal 1800-1820 and dissolve 1831, sultanate-of-bima has vassal 1800-1905; neither records a loss in those years. Evidence: sultanate-of-mempawah /ledger/8-9 and last event; sultanate-of-bima /ledger/6, /8. Fix: Add the vassal pairs here (Mempawah 1800-1820, Bima 1800-1905) and re-date the gains to the neighbours' end years (Mempawah 1831, Bima 1905), or route to se-02 with a page.
- [BLOCKING] `/ledger (Portugal, Luwu, Wajo, Siak)`: portuguese-empire /ledger/80 (loss 1859 of Flores cells), luwu /ledger/3 and wajo /ledger/3 (losses 1905) name dutch-east-indies with no mirror; siak-sultanate runs 1722-1946 with no Dutch event while this ledger takes the Riau and north-east Sumatran coast in 1857 and 1862 (/ledger/36 counterpart is a free string). Evidence: Neighbour ledgers; keyframe 14 note concedes Portuguese-row cells in 1853. Fix: Add a gain from portuguese-empire for eastern Flores and Solor (Treaty of Lisbon 1859), name luwu and wajo in the 1905 Sulawesi gains, and name siak-sultanate (vassal from the 1858 treaty) instead of the free string at /ledger/36.
- [not blocking] `/ledger/42`: 1885 loss of eight edge cells (c1) names german-empire, but german-new-guinea (a dossier) gains 1885 from nobody; the cells lie west of the 141st meridian the page gives as the frontier. Evidence: Dutch_New_Guinea page: 'The Dutch established the 141st meridian as the eastern frontier'; german-new-guinea /ledger/1. Fix: Drop the event as a Cliopatria edge artefact (keyframe 22 adjust to the 1873 outline) or name german-new-guinea.
- [not blocking] `/ledger/70/note`: The quotation 'with the exception of Dutch New Guinea' is not on the cited Dutch_New_Guinea page; it is on Indonesian_National_Revolution. Evidence: WebFetch of both pages; the date (infobox 'Established: 27 December 1949') is on the cited page. Fix: Attribute the quote to Indonesian_National_Revolution in the note.
Thin (for a gap-filler):
- `/ledger/3`: Banten 1809 (c1); the banten dossier dates Daendels's annexation November 1808 (c3) Try https://en.wikipedia.org/wiki/Banten_Sultanate
- `/ledger/7`: Padang coast 1814 (c1) Try https://en.wikipedia.org/wiki/Padang
- `/ledger/15`: North Moluccas and Bird's Head 1824 (c1) Try https://en.wikipedia.org/wiki/Sultanate_of_Ternate
- `/ledger/25`: Sukadana 1834 (c1) Try https://en.wikipedia.org/wiki/Tanjungpura_Kingdom
- `/ledger/29`: Berau 1849 (c1) Try https://en.wikipedia.org/wiki/Sambaliung_Sultanate
- `/ledger/30`: East Borneo cells 1853 from Sulu (c1); sultanate-of-sulu has no 1853 loss Try https://en.wikipedia.org/wiki/Dutch_Borneo
- `/ledger/31`: Sumatran cells 1856 (c1) Try https://en.wikipedia.org/wiki/Tapanuli
- `/ledger/32`: Riau-Lingga 1857 (c1) Try https://en.wikipedia.org/wiki/Riau-Lingga_Sultanate
- `/ledger/33`: South Sulawesi 1859 from Bone (c1); sultanate-of-bone has no 1859 loss Try https://en.wikipedia.org/wiki/Bone_State
- `/ledger/36`: North-east Sumatran coast 1862 (c1) Try https://en.wikipedia.org/wiki/Deli_Sultanate
- `/ledger/38`: Lesser Sundas 1866 (c1) Try https://en.wikipedia.org/wiki/Treaty_of_Lisbon_(1859)
- `/ledger/45`: Kalimantan interior, West Sumatra, Jambi and Bengkulu 1898 (c1) Try https://en.wikipedia.org/wiki/Dutch_Borneo
- `/ledger/48`: Jambi 1905 (c1; the jambi dossier has 1904) Try https://en.wikipedia.org/wiki/Jambi_Sultanate
- `/ledger/50`: Rest of Sulawesi 1908 (c1) Try https://en.wikipedia.org/wiki/South_Sulawesi_expedition_of_1905
Spot checks:
- `/ledger/8` https://en.wikipedia.org/wiki/Anglo-Dutch_Treaty_of_1814: confirmed (13 August 1814; 'Britain ceded Bangka Island to the Netherlands' for Dutch Malabar)
- `/ledger/17` https://en.wikipedia.org/wiki/Anglo-Dutch_Treaty_of_1824: confirmed (Fort Marlborough ceded; 'All transfers ... on 1 March 1825'); /ledger/16, 18, 19 also confirmed
- `/ledger/26` https://en.wikipedia.org/wiki/Padri_War: confirmed ('on 16 August 1837, Fort Bonjol was completely conquered'; 4 March 1822, August 1831, 2 May 1833, 8 June 1835 all on the page)
- `/ledger/39` https://en.wikipedia.org/wiki/Dutch_New_Guinea: confirmed at c2 (claim 'made in 1848', Tidore 1872, posts 1898, residency 1920; 1873 is the Cliopatria year, said in the note)
- `/ledger/44` https://en.wikipedia.org/wiki/Dutch_East_Indies: confirmed ('the island of Lombok came under Dutch control in 1894'); /ledger/28 (1849 north Bali), /ledger/49 (1905-06 south-west Sulawesi), /ledger/51 (April 1908 Bali), /ledger/2 (1806), /ledger/10 (1816) also confirmed
- `/ledger/62` https://en.wikipedia.org/wiki/Indonesian_National_Revolution: confirmed (Linggadjati, November 1946, de facto authority over Java, Madura and Sumatra); /ledger/63-67, /ledger/71 also confirmed
- `/ledger/70` https://en.wikipedia.org/wiki/Dutch_New_Guinea: confirmed (Established 27 December 1949); quoted phrase is on the other page

## Cross-dossier matrix (not matched)
- missing: kelantan 1795 contest_start -> sultanate-of-terengganu; mirror none. no event naming kelantan in sultanate-of-terengganu (se-03-a)
- missing: kelantan 1800 contest_end -> sultanate-of-terengganu; mirror none. as above
- missing: rattanakosin-kingdom 1786 vassal_start -> kelantan; mirror none. kelantan has no vassal_start; finding in kelantan
- missing: rattanakosin-kingdom 1909 vassal_end -> kelantan; mirror none. kelantan has no vassal_end; finding in kelantan
- exception: kelantan 1890 loss -> unnamed neighbour (pages silent); mirror none. c1 bridge, counterpart unknown
- exception: kelantan 1909 dissolve -> british-colonial-empire; mirror none. british-colonial-empire (eu-11) not run yet
- missing: dutch-east-indies 1800 vassal_start -> pontianak-kadriyah-sultanate; mirror none. pontianak has no vassal events; finding in pontianak
- missing: dutch-east-indies 1949 vassal_end -> pontianak-kadriyah-sultanate; mirror none. as above
- exception: pontianak-kadriyah-sultanate 1950 dissolve -> republic-of-indonesia; mirror none. republic-of-indonesia (se-04) not run yet
- exception: negeri-sembilan 1832 loss -> straits-settlements; mirror none. listed in counterparts_needing_dossiers (se-03-x)
- exception: negeri-sembilan 1874 loss -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: negeri-sembilan 1883 loss -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: negeri-sembilan 1895 gain -> british-colonial-empire; mirror none. counterpart changed from free strings by the reviewer; eu-11 not run yet
- exception: negeri-sembilan 1895 dissolve -> federated-malay-states; mirror none. listed in counterparts_needing_dossiers (se-03-x)
- exception: dutch-east-indies 1810 occupation_start -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: dutch-east-indies 1811 occupation_start -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: dutch-east-indies 1814 gain -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: dutch-east-indies 1816 occupation_end -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: dutch-east-indies 1825 gain -> british-colonial-empire; mirror none. eu-11 not run yet
- exception: dutch-east-indies 1825 loss -> british-colonial-empire; mirror none. eu-11 not run yet
- mismatch: dutch-east-indies 1822 gain -> sultanate-of-sambas; mirror sultanate-of-sambas 1819 dissolve. three years apart; sambas c3
- missing: dutch-east-indies 1824 gain -> sultanate-of-ternate; mirror none. ternate has no 1824 loss; its loss to DEI is 1914, unmirrored
- missing: sultanate-of-ternate 1914 loss -> dutch-east-indies; mirror none. no 1914 event in DEI
- mismatch: dutch-east-indies 1828 gain -> sultanate-of-mempawah; mirror none. mempawah: vassal_start 1800, vassal_end 1820, dissolve 1831 (no counterpart); no 1828 loss
- missing: sultanate-of-mempawah 1800 vassal_start -> dutch-east-indies; mirror none. no mirror in DEI
- mismatch: dutch-east-indies 1830 vassal_start -> sultan-of-yogyakarta; mirror sultan-of-yogyakarta 1830 vassal_end. yogyakarta ends its vassalage and dissolves in 1830; DEI opens it in 1830 to 1945
- mismatch: dutch-east-indies 1830 vassal_start -> surakarta-sunanate; mirror surakarta-sunanate 1830 vassal_end. same as yogyakarta
- missing: sultan-of-yogyakarta 1806 vassal_start -> dutch-east-indies; mirror none. also 1811 vassal_end and 1816 vassal_start; none in DEI
- missing: surakarta-sunanate 1806 vassal_start -> dutch-east-indies; mirror none. also 1811 and 1816; none in DEI
- missing: pagaruyung-kingdom 1833 loss -> dutch-east-indies; mirror none. DEI gains Minangkabau only in 1837
- missing: padri-movement 1821 contest_start -> dutch-east-indies; mirror none. DEI has the Padri War in wars[] but no contest events (also 1824, 1831, 1837)
- mismatch: dutch-east-indies 1846 gain -> sultanate-of-kutai-kartanegara; mirror kutai-kingdom 1844 loss. slug not written; kutai-kingdom holds the Kutai Kartanegara row and dates the loss 1844
- missing: bali 1846 contest_start -> dutch-east-indies; mirror none. no contest events in DEI
- missing: bali 1894 loss -> dutch-east-indies; mirror none. DEI's 1894 gain is Lombok from 'rulers of Lombok'; Karangasem not gained
- missing: bali 1906 loss -> dutch-east-indies; mirror none. no 1906 gain in DEI
- exception: dutch-east-indies 1849 gain -> sultanate-of-sambaliung; mirror none. se-03 other part, not written
- missing: dutch-east-indies 1853 gain -> sultanate-of-sulu; mirror none. sulu (ends 1878) has no 1853 loss; c1
- exception: dutch-east-indies 1857 gain -> riau-lingga-sultanate; mirror none. se-03 other part, not written
- missing: dutch-east-indies 1859 gain -> sultanate-of-bone; mirror none. bone has no 1859 loss; c1
- mismatch: dutch-east-indies 1863 contest_end -> sultanate-of-banjar; mirror sultanate-of-banjar 1860 contest_end. three years; banjar dissolved 1860, fighting went on to 1863
- mismatch: dutch-east-indies 1862 gain -> northeast Sumatran coast (page names no states); mirror none. free string; siak-sultanate (1722-1946) has no Dutch event
- mismatch: dutch-east-indies 1885 loss -> german-empire; mirror german-new-guinea 1885 gain. german-new-guinea gains from nobody; german-empire (eu-20) not run
- mismatch: dutch-east-indies 1890 gain -> sultanate-of-bima; mirror none. bima: vassal 1800-1905 with DEI, no 1890 loss
- missing: sultanate-of-bima 1800 vassal_start -> dutch-east-indies; mirror none. no mirror in DEI (also 1905 vassal_end)
- exception: dutch-east-indies 1894 gain -> rulers of Lombok (no dossier); mirror none. lombok-kingdoms in counterparts_needing_dossiers
- missing: luwu 1905 loss -> dutch-east-indies; mirror none. DEI 1905 gain names Bone only
- missing: wajo 1905 loss -> dutch-east-indies; mirror none. DEI 1905 gain names Bone only
- missing: sultanate-of-gowa 1800 vassal_start -> dutch-east-indies; mirror none. also 1911 vassal_end and loss; none in DEI
- missing: kingdom-of-bulungan 1834 vassal_start -> dutch-east-indies; mirror none. also 1878 vassal_end and dissolve; none in DEI
- missing: sultanate-of-tidore 1806 occupation_start -> dutch-east-indies; mirror none. also 1811 end and 1905 dissolve; none in DEI
- missing: sultanate-of-bacan 1889 dissolve -> dutch-east-indies; mirror none. none in DEI
- missing: portuguese-empire 1859 loss -> dutch-east-indies; mirror none. Flores cells; no gain from Portugal in DEI
- exception: dutch-east-indies 1946 loss -> republic-of-indonesia; mirror none. se-04 not run yet
- exception: dutch-east-indies 1947 gain -> republic-of-indonesia; mirror none. se-04 not run yet
- exception: dutch-east-indies 1948 gain -> republic-of-indonesia; mirror none. se-04 not run yet
- exception: dutch-east-indies 1949 split -> dutch-new-guinea; mirror none. in counterparts_needing_dossiers (se-03-x)
- exception: dutch-east-indies 1800 found -> dutch-east-india-company; mirror none. in counterparts_needing_dossiers (se-03-x)

## Problems for the orchestrator
- Vassal convention: kelantan and pontianak-kadriyah-sultanate leave vassal events to the suzerain's dossier only, the reading the se-03-a review already failed in four dossiers; the research brief should say both sides carry them.
- Slug clash: dutch-east-indies names sultanate-of-kutai-kartanegara (assigned to another se-03 part by the brief) but the existing dossier kutai-kingdom already lists the Cliopatria row 'Sultanate of Kutai Kartanegara' and ends 1844; the orchestrator should decide which slug owns the row.
- Most dutch-east-indies mismatches involve se-02 and earlier dossiers (bima, mempawah, sambas, ternate, tidore, bacan, gowa, luwu, wajo, siak-sultanate, portuguese-empire, bali, pagaruyung-kingdom, kingdom-of-bulungan); the DEI author should reconcile them with those ledgers, and the West Borneo and Moluccan convention (vassal to 1949 or end at annexation) needs one decision.
- sultanate-of-terengganu (se-03-a) lacks the 1795-1800 contest with kelantan.
- siak-sultanate runs 1722-1946 with no Dutch event, overlapping the DEI's 1857 and 1862 gains.
- Reviewer edits applied on the shared mount: dutch-east-indies (/identity/wikidata, /ledger/26/counterpart, /wars/2/belligerents/1) and negeri-sembilan (/ledger/5/counterpart, /ledger/6/counterpart); both re-validated with no errors.
- No page failed to load. WebFetch summaries did not show '5 February 1898' on Dutch_New_Guinea (the page has 1898).
