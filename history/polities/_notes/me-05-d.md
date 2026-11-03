# me-05-d notes (Achaemenids and Seleucids, part d)

Written 2026-10-19 by the Phase B agent for batch me-05-d. Dossiers: kingdom-of-pontus, galatia, kingdom-of-pergamon, paphlagonia, kingdom-of-sophene, plus the rebel state revolt-of-aristonicus (added because Pergamon's 133-129 contest needs a counterpart). All validate with `validate_dossier.py --resolve` (0 errors; one warning, the unknown region Acilisene).

Every page was read through WebFetch, which returns a small model's answer to a prompt, not the page text; quotes in the dossiers are those answers. Where an answer said the page was silent, the dossier says so and records the event at confidence 1.

## kingdom-of-pontus (9 pages, budget 9)
- Cliopatria -126..-78 puts Galatia (-127 shape), Paphlagonia (-127 shape) and a 123-cell Lycaonia block (Konya, Isparta) inside Pontus; none of the pages opened supports it. Corrected by subtracting Cliopatria's Galatia -77 shape; Paphlagonia kept only after the 108 partition (repaired 2026-10-19; first written as c. 116). The Lycaonia block is the same one Cliopatria gives Pergamon in -188..-127 and Galatia in -77..-26.
- The -87..-78 shape is the First Mithridatic War conquest (Bithynia, Cappadocia, Roman Asia); Dardanus (85) ended it, so a new keyframe -84 applies from -84.
- Colchis and Crimea: Cliopatria -91. After the repair: Lesser Armenia c. 115-106 and Colchis undated (conquered before the 83 uprising, Colchis page) at confidence 1; the Chersonesus c. 110 (Chersonesus page, confidence 2); the Bosporan cession c. 107 (Diophantus page, confidence 2).
- Client kingdom after 63 lacks Colchis and Lesser Armenia (Polemon I, 31 BC; Colchis undated). Kingdom ends 62 (Polemon II page), not 67.
- Disagreements: Sinope 183 (Paphlagonia page) or 182 (Kingdom page); Paphlagonia partition: no year on the Kingdom page, 108 ('probably') on the Mithridates VI page; Senate on Cappadocia 97 against Ariobarzanes I from 95; Bithynia bequest 74 or 73.
- Schema one-sidedness: Pontus' client status (63 BC-62 AD) and the Seleucid/Parthian/Pergamene dependencies must be recorded by the overlord. The Roman Republic/Empire dossiers need `vassal_start kingdom-of-pontus` 63 BC to 62 AD.
- No infobox area on the page: the area check was not possible.

## galatia (4 own pages + 2 from Pontus, budget 5)
- Cliopatria has no Galatia -126..-78 (land drawn inside Pontus): a core keyframe is added, soft.
- The -77/-63/-49 shapes carry the Lycaonia block; corrected to the core (plus Lesser Armenia 63-48). Amyntas' kingdom (-37..-26) uses the -27 shape.
- Start -279 (Brennus's bands; settlement in Anatolia 277-275/269); end -25 (province), one year after Cliopatria's last.
- Not on any page opened: where Mithridates VI's 'part of Galatia' (108) and Deiotarus' 'part of eastern Pontus' (c. 63) lay; which dominions Caesar took in 47; when Amyntas became king of Galatia.

## kingdom-of-pergamon (5 pages, budget 5)
- Start -282 (infobox), not -279; end -129 (province of Asia), not -127. The -223..-213 shape wrongly keeps the 105-cell extension through Achaeus' war.
- The -188 shape contains 124 Lycaonia cells and 22 Lycia / 4 Caria cells that the pages do not give Eumenes II (Lycia and Caria went to Rhodes first). The pages disagree on Pisidia.
- Area: the page's 143,000 km2 (about 227 BC) against the -225 shape (38.4 k) gives 0.27; against the -188 shape (176.0 k) 1.23.
- Not covered: Pergamon's tribute to the Galatians until Attalus I refused (c. 238-235); the 168-166 Galatian war; Seleucid overlordship of Philetaerus and Eumenes I (281-261).

## paphlagonia (1 own page + 4 from sisters, budget 1-2)
- Ends 108 (partition), not -127 (repaired 2026-10-19; first written as c. 116). The Paphlagonia page says Pontus held the whole province after 183, which contradicts the Pharnaces I page (179 peace), the Aristonicus page (Pylaemenes of Paphlagonia, 133-129) and the Kingdom of Pontus page; the dossier follows the latter three.
- No capital, founding date or ruler list on any page; capitals left empty. A native Paphlagonia may continue 97-65 (Senate order of 97; Pompey leaves the interior to native princes): a gap-filler should open 'Pylaemenes' pages.

## kingdom-of-sophene (5 pages, budget 5; Zariadris failed, Zariadres loaded)
- Independent kingdom -256..-95 (Tigranes c. 95). Cliopatria's -110..-88 shape ends 8 years late; its Armenia shapes hold the cells only from -80, so -94..-81 is a hole for the Armenia dossier.
- The four Roman-era shapes (-63..113) are marked wrong: the page has no independent Sophene between c. 95 BCE and c. 54 CE and says it is debated whether it was Armenian or Cappadocian after 66. The two pages meant to date the Roman period (Sohaemus of Armenia, Ariobarzanes I) were thin. A gap-filler should open the Corbulo and Roman-Parthian War pages.
- Gazetteer lacks Acilisene and Akisene. Arsamosata and Eğil coordinates are approximations.

## revolt-of-aristonicus (rebel, 2 pages)
- Union of circles round the named cities; the coordinates are the researcher's geography. The Wikipedia title 'Revolt of Aristonicus' returned URL_NOT_FOUND; 'Aristonicus of Pergamon' was used.

## For other groups
- Seleucid dossier: vassal_start kingdom-of-sophene c. 212 to c. 190; Philetaerus/Eumenes I autonomy to 261.
- Parthian dossier: vassal kingdom-of-sophene under Mithridates II (124-91) to c. 95.
- Armenia dossier (eu-19): gain Sophene c. 95 (Cliopatria has it from -80); Orontid predecessor of Sophene.
- Cappadocia dossier (me-05): vassal_start/end under Pontus -101..-97; gains/losses -91..-85; the 129 share of the Pergamene kingdom.
- Bithynia (me-05): Paphlagonia partition 108; Bithynia taken 89, returned 85, 74 invasion.
- Roman Republic/Empire: client Pontus 63 BC-62 AD, the province of Asia (129), Bithynia et Pontus (63), Galatia (25).
- Rhodes (eu-02): the Rhodian Peraia (Lycia, Caria) after Apamea.

## Review repair, 2026-10-19 (author, after the adversarial review of kingdom-of-pontus and paphlagonia)
Pages reopened with WebFetch on 2026-10-19: Kingdom of Pontus (twice), Mithridates VI, First Mithridatic War, Nicomedes IV of Bithynia, Third Mithridatic War, Phrygia, Diophantus (general), Chersonesus, Colchis, Bosporan Kingdom, Pylaemenes. Both dossiers validate with `--resolve` (0 errors, 0 warnings).

What changed, by finding:
- Paphlagonia partition (kingdom-of-pontus ledger 11-12, paphlagonia end): c. 116 to 108. The Kingdom of Pontus page has no timeline and no year for it (its '116' is Ariarathes VI's murder); the Mithridates VI page: 'He contrived to partition Paphlagonia and Galatia with King Nicomedes III of Bithynia' and 'probably ... the Paphlagonian invasion of 108 BC'. Keyframes -120 (now -120..-111), -110 (-110..-109, Paphlagonia subtracted) and -108 (-108..-92); the old -116 and -105 keyframes are gone. Paphlagonia: end -108, dissolve -108 (Mithridates VI page), keyframe -126..-108, war -108, certainty to -108. Galatia's loss at -108 (already moved by the reviewer) now matches.
- Kerch double count: the circle (90 km round 36.5 E 45.3 N) is subtracted from every direct Crimea shape (keyframes -110, -108, -91, -87, -84, -77, -66; ledger -110 and -63). The reviewer named /11, /14 and /41; the later Cliopatria shapes held the same 17 Kerch cells, so I treated them alike.
- Occupations: Bithynia (-89 to -85) and Cappadocia (-90 to -85) are occupation_start/occupation_end, no longer gain/loss; added the -90 Bithynian pair and the Athens pair (greek-city-states, -88 to -86 March). No kingdom-of-cappadocia dossier existed on 2026-10-19, so Cappadocia could not be agreed with its author.
- Galatia -63: the loss of Lesser Armenia now also takes the Pontic-Galatian frontier band, the same band spec as galatia ledger 8.
- Quotations that were summaries (ledger 13, 16-20, 36) are labelled paraphrases and now carry the sentences read again; the 97 vassal_end is confidence 2 (the Senate decree is undated on the page).
- Thin items tried: Chersonesus gain moved -105 to -110 and the Bosporan protection -105 to -107 (Diophantus and Chersonesus pages); Phrygia, Colchis, Bosporan Kingdom, Third Mithridatic War and Pylaemenes gave no new date (see each dossier's notes).

What I disagree with, and why:
- The Bithynia dossier starts the Pontic occupation in 88 (confidence 3). I used 89: the Kingdom of Pontus page says 'In the summer of 89 BC, Mithridates invaded Bithynia and defeated Nicomedes and Aquillius in battle'; the First Mithridatic War page gives no year for 'captured Bythinia without opposition' (the 'late summer of 89' my first version attached to it is not on that page); the Nicomedes IV page has Mithridates retaliating 'again in 88 BC'. The two dossiers differ by one year; the Bithynia author should look at it.
- The reviewer said to replace keyframe /9 (-116..-111); I removed it and extended -120 to -111 instead, because with Paphlagonia dated 108 the two keyframes are the same shape.
- The reviewer's reading that 'the better one' for Bithynia is an occupation is followed; I kept the Roman Asia gain/loss -88/-85 with roman-republic, because that dossier records the same pair (a province, not a hatched client).
- Rome's retaking of Phrygia stays at -120, confidence 1: the Phrygia page is silent on Pontus; the Roman Republic dossier says 116 and a four-year hole remains (-119..-117) until a page dates it.
- The fate of the Chersonesus in 63 stays a bridging reading: the Chersonesus page says only 'subject to Rome and received a garrison from the middle of the 1st century BC' and the Bosporan Kingdom page does not mention it, so the transfer to cimmerian-bosporus has no matching gain in that dossier.

For other groups: kingdom-of-bithynia (occupation start 88 against 89 here); kingdom-of-cappadocia (needs occupation by Pontus -90 to -85, vassal -101 to -97); greek-city-states (Chersonesus returns to the polis in 63? no page says); cimmerian-bosporus (Pontic vassal 107 matches; the Chersonesus side in 63 is unmatched); roman-republic (client Pontus 63 BC to 62 AD still missing: vassal_start kingdom-of-pontus).

