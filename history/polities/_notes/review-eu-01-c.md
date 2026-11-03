# Review of batch eu-01-c (Greece, part c)

Reviewer: adversarial reviewer, Phase B, 2026-10-18. Inputs: the author's brief, report and notes; the six dossiers; neighbour dossiers greek-city-states, macedonian-empire, scythia and huns (greek-colonies and achaemenid-empire are not written yet), plus achaean-league, delian-league, kingdom-of-lysimachus and antigonid-dynasty for mirrors. Validator: all six valid before and after the reviewer's edits (warnings are gazetteer names, listed at the end).

Page budget (author's brief section 10): 1-2 pages for sacred-band-of-thebes, second-athenian-league and thebans; up to 5 for peloponnesian-league, odrysian-kingdom and cimmerian-bosporus. Spot-check budget: 4 events per dossier, weighted to confidence 3 and the largest moves.

## Verdicts

| slug | verdict | applied by reviewer | left for the author |
| --- | --- | --- | --- |
| sacred-band-of-thebes | fix | 0 | 4 |
| second-athenian-league | fix | 0 | 3 |
| thebans | fix | 0 | 3 |
| peloponnesian-league | fix | 3 | 3 |
| odrysian-kingdom | fix | 3 | 0 |
| cimmerian-bosporus | fix | 0 | 1 |

No dossier has a fabricated or mis-dated confidence-3 event: every confidence-3 event opened was on its page with its year. One confidence-2 event (odrysian-kingdom /ledger/6) cites a sentence that does not say what its note claims; it was lowered to confidence 1.

## sacred-band-of-thebes: fix

Area: The Thebes, Greece infobox gives the modern municipality (830.112 km2), not the ancient state; no page gives an area for the hegemony. Author: corrected shape about 24,000 km2 by cells (Byzantium, Izmir, Dytiki Makedonia and Corinth cells removed with quotes I confirmed on the Epaminondas page).

Findings:

- `/identity` (for the author). The Theban state is split into two dossiers at -362/-361 (dissolve in sacred-band-of-thebes, found in thebans), although the pages and the author's own notes describe one state, Thebes at the head of the Boeotian League, that outlived the hegemony. Evidence: Theban hegemony page: 'It ended with the tactical Theban victory at Mantinea in 362 BC' (the hegemony ends, not the state); 'Thebes had now lost both of the innovative leaders ...' and Thebes fights on in the Third Sacred War. The author's report (problems[0]) calls them 'one Theban state in substance'; brief section 6: 'One dossier per state, not per dynasty'. Two Cliopatria rows for one state go in one dossier under the earlier slug. Fix: Merge thebans.json into sacred-band-of-thebes.json: cliopatria_names ['Sacred Band of Thebes','Thebans']; end -338 month 8; keep the -362 vassal_end events as the end of the hegemony; drop sacred-band-of-thebes /ledger/16 (dissolve -362) and the thebans found; bring over thebans' ledger, wars, certainty and keyframes (thebans_-361 becomes the new keyframe sacred-band-of-thebes_-361; thebans_-350 is reviewed in the merged file); successors greek-city-states; delete thebans.json; ask the eu-01 owner to rename the counterpart in greek-city-states /ledger/42.
- `/ledger/1/counterpart` (for the author). The -371 gain of Orchomenus names 'Orchomenus', which has no dossier and is not in counterparts_needing_dossiers, and nobody holds Orchomenus -379..-372. Evidence: keyframe_review/0 (-379..-372) is Boeotia minus Orchomenus, but greek-city-states /ledger/26 gives all of Boeotia (the Cliopatria Thebans -350 shape, which contains Orchomenus) to this dossier at -379. Epaminondas page (confirmed): 'compelling the previously Spartan-aligned polis of Orchomenus to join the league'. Fix: Counterpart 'greek-city-states'; route to eu-01: greek-city-states /ledger/26 should give Boeotia minus Orchomenus at -379 and add a -371 loss of Orchomenus to this dossier.
- `/ledger/2/counterpart` (for the author). 'Theban allies in central and western Greece' (also /ledger/11) is a name string with no dossier and is not listed, so the vassal pair has no mirror. Evidence: The allies the Epaminondas page lists ('Aetolians, Acarnanians, Aenianians, West and East Locrians, Phocians, Heracleots, Malians') are greek-city-states land; that dossier records them as a -366 loss to this one (/ledger/31, confidence 1) and a -350 gain (/ledger/37), not as a 370-362 vassalage; aetolian-league starts only in -367. Fix: Counterpart 'greek-city-states' on /ledger/2 and /ledger/11; route to eu-01: greek-city-states /ledger/31 should become vassal_start -370 (central Greece) and -369 (Arcadia, Messenia, Thessaly), /ledger/37 a vassal_end at -362.
- `/wars/0/zones` (for the author). Leuctra has empty zones and the note does not say that no ground changed hands. Evidence: Brief section 2.10: empty zones only where no ground changed hands, and said so. Fix: Add to the note: 'No ground changed hands in the battle; the gain of Orchomenus follows (/ledger/1)'.

Spot checks:

- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Epaminondas)
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Epaminondas)
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Epaminondas)
- `/ledger/7`: confirmed (https://en.wikipedia.org/wiki/Epaminondas)
- `/ledger/16`: confirmed (https://en.wikipedia.org/wiki/Theban_hegemony)
- `/keyframe_review/3/note`: confirmed (https://en.wikipedia.org/wiki/Epaminondas)

Gaps for a gap-filler:

- `/ledger/3`: Year Euboea went over to Thebes (confidence 1; the Epaminondas page has it only in a footnote to 'By late 370'). Try https://en.wikipedia.org/wiki/Euboea
- `/ledger/8`: Any Theban holding or client status in Thessaly; the Pelopidas page has expeditions (369, 364) only; the 364 settlement with Pherae is the likely evidence. Try https://en.wikipedia.org/wiki/Alexander_of_Pherae
- `/ledger/12`: End years of the Euboean, Messenian and Thessalian alliances (12, 14, 15 at confidence 1, all closed at Mantinea). Try https://en.wikipedia.org/wiki/Battle_of_Mantinea_(362_BC)
- `/keyframe_review/3`: Argos, Tegea and Mantinea cells of the Theban shape (unverified: page budget). Try https://en.wikipedia.org/wiki/Battle_of_Mantinea_(362_BC)

## second-athenian-league: fix

Area: No infobox. Polis page: 'Athens had 2,500 km2' against Cliopatria's -366 league shape of 35,040 km2; the dossier draws the allies as client land and gives corrected cell areas in each keyframe note.

Findings:

- `/ledger/17/region` (for the author). The -338 loss hands the Thracian Chersonese and the islands of the -350 shape to greek-city-states, but the page cited says nothing of the Chersonese and keeps Samos Athenian. Evidence: Battle of Chaeronea (338 BC) page: 'Although the Second Athenian League was dissolved, the Athenians were allowed to keep their colony on Samos'; the page does not mention the Chersonese, Oropus or other possessions. The mirror greek-city-states /ledger/40 gains Attica only. Fix: Split /ledger/17: Attica and the islands to greek-city-states (text: Samos stays Athenian; the athens dossier will take them over when written); the Chersonese as a separate -338 loss to macedonian-empire at confidence 1 (Peace of Demades; a page is needed) or left out; ask eu-01 to give greek-city-states /ledger/40 the same land.
- `/ledger/3/counterpart` (for the author). 'Allied cities that became independent in 355' and 'Allied cities that stayed with Athens' (/ledger/3, 4, 11, 16) are name strings with no dossier, not listed. Evidence: The land is greek-city-states' (its /ledger/28 loses the league to this dossier at -377); greek-city-states /ledger/35 regains only Chios, Rhodes, Byzantion and Cos in -355, so /ledger/13 has no mirror. Fix: Counterpart 'greek-city-states' on these four events; route to eu-01: add the -355 gain of the other departing members to greek-city-states.
- `/wars/2/zones` (for the author). Chaeronea has empty zones and the note does not say why. Evidence: Brief section 2.10. Fix: Say in the note that the land changes are the -338 events (/ledger/15-18), not the battlefield.

Spot checks:

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Second_Athenian_League)
- `/ledger/7`: confirmed (https://en.wikipedia.org/wiki/Cersobleptes)
- `/ledger/10`: confirmed (https://en.wikipedia.org/wiki/Social_War_(357%E2%80%93355_BC))
- `/ledger/12`: confirmed (https://en.wikipedia.org/wiki/Social_War_(357%E2%80%93355_BC))
- `/ledger/17`: not on page (the Chersonese part; the dissolution and Samos are confirmed) (https://en.wikipedia.org/wiki/Battle_of_Chaeronea_(338_BC))

Gaps for a gap-filler:

- `/ledger/6`: The -360 loss of the Chersonese to Cotys I rests on the Odrysian dossier (confidence 1, page not opened). Try https://en.wikipedia.org/wiki/Cotys_I_(Odrysian)
- `/ledger/14`: When Euboea came back to Athens (bridged to -350, confidence 1); /ledger/2 and /ledger/5 are confidence 1 too. Try https://en.wikipedia.org/wiki/Euboea
- `/ledger/4`: Which members stayed after 355 (confidence 1; region is Cliopatria's -350 shape). Try https://en.wikipedia.org/wiki/Second_Athenian_League
- `/keyframe_review/1`: Thracian and Chalcidian cells (Abdera, Cardia, Torone, Amphipolis) and Corfu unverified (page budget). Try https://en.wikipedia.org/wiki/Corcyra_(polis)

## thebans: fix

Area: No page gives an area; the author's Boeotia is 14 cells (about 3,500 km2) against Cliopatria's 18 (Locris/Malis cells removed, explained in keyframe_review/1).

Findings:

- `/identity` (for the author). The Theban state is split into two dossiers at -362/-361 (dissolve in sacred-band-of-thebes, found in thebans), although the pages and the author's own notes describe one state, Thebes at the head of the Boeotian League, that outlived the hegemony. Evidence: Theban hegemony page: 'It ended with the tactical Theban victory at Mantinea in 362 BC' (the hegemony ends, not the state); 'Thebes had now lost both of the innovative leaders ...' and Thebes fights on in the Third Sacred War. The author's report (problems[0]) calls them 'one Theban state in substance'; brief section 6: 'One dossier per state, not per dynasty'. Two Cliopatria rows for one state go in one dossier under the earlier slug. Fix: Merge thebans.json into sacred-band-of-thebes.json: cliopatria_names ['Sacred Band of Thebes','Thebans']; end -338 month 8; keep the -362 vassal_end events as the end of the hegemony; drop sacred-band-of-thebes /ledger/16 (dissolve -362) and the thebans found; bring over thebans' ledger, wars, certainty and keyframes (thebans_-361 becomes the new keyframe sacred-band-of-thebes_-361; thebans_-350 is reviewed in the merged file); successors greek-city-states; delete thebans.json; ask the eu-01 owner to rename the counterpart in greek-city-states /ledger/42.
- `/ledger/5` (for the author). The dissolve in August 338 ends a state the cited page says survived under a garrison, and no event records the garrison. Evidence: Battle of Chaeronea (338 BC) page: Philip 'installed a Macedonian garrison' at Thebes and 'did not, however, dissolve the Boeotian Confederacy'; Thebes page: the revolt against Alexander 'was punished ... with the destruction of the city' (335). Fix: Either keep -338/8 as Cliopatria's end and say so in the note, adding an occupation_start of the Cadmea by macedonian-empire at -338/8 if the state continues; or continue to -335 with vassal_start macedonian-empire -338/8 and dissolve -335. Ask eu-02 for the garrison event in macedonian-empire.
- `/wars/1/zones` (for the author). Chaeronea has empty zones and the note does not say why. Evidence: Brief section 2.10. Fix: Say in the note that the land change is the dissolve (/ledger/5).

Spot checks:

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Theban_hegemony)
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Third_Sacred_War)
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Third_Sacred_War)
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Third_Sacred_War)
- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Battle_of_Chaeronea_(338_BC))

Gaps for a gap-filler:

- `/ledger/2`: When Phocis took Orchomenus, Coronea and Corsiae (bridge -347, confidence 1); the Third Sacred War page has Onomarchos invading 'Doris and eventually Boeotia' in 353 and 'The Phocians had occupied several Boeotian cities' with no year. Try https://en.wikipedia.org/wiki/Onomarchus

## peloponnesian-league: fix

Area: No infobox area on the Sparta or Peloponnesian League pages; the Polis page gives 'Lacedaemon had 8,400 km2', which the author quotes correctly (keyframe_review/2: ratio 1.8, surplus = allies). The -404 shape (22,523 km2, 2.7x) is the league with Athens and Boeotia (keyframe_review/5).

Findings:

- `/ledger/55/counterpart` (applied by the reviewer). Counterpart 'antigonid-macedonia' (also /ledger/57, /wars/10/belligerents/2, /wars/11/belligerents/5) is a Cliopatria slug carried by another dossier. Evidence: polities.csv antigonid-macedonia (-277..-165) is in history/polities/antigonid-dynasty.json (cliopatria_names ['Antigonid Dynasty','Antigonid Macedonia']), whose /ledger/31 is the mirror (-223 gain from peloponnesian-league). Fix: antigonid-dynasty in all four places (done, with a reviewer remark in the notes).
- `/ledger/50/region/border_band/year` (applied by the reviewer). The border band (also /wars/8/zones/0) names year -337, for which the Cliopatria row has no shape, so it cannot be drawn. Evidence: validate_dossier --resolve: 'Cliopatria polity peloponnesian-league has no shape in -337; its shapes cover ... -350..-338'; the mirror greek-city-states /ledger/39 uses -338. Fix: year -338 (done; the two warnings are gone).
- `/ledger/56/confidence` (applied by the reviewer). Argos's return to the Achaeans is dated -222 at confidence 2, but the page gives no year. Evidence: Cleomenean War page: the revolt of Argos ('the entire city except for the citadel was in the hands of the Argives') carries no year; achaean-league /ledger/13 dates it -224. Fix: confidence 1 (done); the author should take the year from a page (achaean-league uses -224).
- `/ledger/55/year` (for the author). Mis-dated by one year (confidence 2): the Arcadian towns that 'confined Cleomenes to Laconia' fell in 223, not after Sellasia in 222. Evidence: Cleomenean War page: 'In the early spring of 223 BC, Antigonus advanced upon Tegea.' 'Antigonus proceeded to capture Mantinea, Heraea, and Telphusa, which confined Cleomenes to Laconia.' antigonid-dynasty /ledger/31 has the gain at -223. Fix: Year -223 for the Arcadian part (the Tripoli circle); Corinth (Acrocorinth, no year on the page) as its own event at confidence 1; end keyframe peloponnesian-league_-229 at -224 and start the next keyframe at -223 (shape_id peloponnesian-league_-223).
- `/keyframe_review/5` (for the author). The -404 shape (22,523 km2, reaching Attica and Boeotia) is kept to -384 although the ledger ends the Athenian, Corinthian and Boeotian memberships in -395 and the Aegean one in -394; nothing removes them for -395..-384. Evidence: shapes.csv: peloponnesian-league_-404 bbox to 24.08 E, 38.80 N against 23.41 E, 38.09 N for -550 and -383; /ledger/27-30 are the vassal_ends of 395/394. Fix: Say in keyframe_review/5 text that the shape holds -404..-396 and add a new keyframe peloponnesian-league_-395 (-395..-384) equal to the -383 shape.
- `/keyframe_review/6/verdict` (for the author). Verdict 'wrong' with the shape given unchanged; only its end year is wrong. Evidence: Schema: 'A verdict that only changes the years says so in text and gives the shape unchanged' (adjust). Fix: verdict 'adjust', text 'holds -383..-370; replaced from -369 by the new keyframe'.

Spot checks:

- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Sparta)
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Sparta)
- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Peloponnesian_League)
- `/ledger/14`: confirmed (https://en.wikipedia.org/wiki/Peloponnesian_League)
- `/ledger/15`: confirmed (https://en.wikipedia.org/wiki/Peloponnesian_League)
- `/ledger/16`: confirmed (https://en.wikipedia.org/wiki/Peloponnesian_League)
- `/ledger/33`: confirmed (https://en.wikipedia.org/wiki/Peace_of_Antalcidas)
- `/ledger/44`: confirmed (https://en.wikipedia.org/wiki/Peloponnesian_League)
- `/ledger/55`: mis-dated (https://en.wikipedia.org/wiki/Cleomenean_War)
- `/ledger/56`: not on page (no year for Argos; confidence lowered) (https://en.wikipedia.org/wiki/Cleomenean_War)

Gaps for a gap-filler:

- `/ledger/6`: Joining years of Elis, Mantinea, Sicyon, Epidaurus, Phlius, Troezen (/ledger/6-11) and Megara (/ledger/13), all confidence 1 at -550/-519. Try https://en.wikipedia.org/wiki/Peloponnesian_League
- `/ledger/37`: End of the Olynthian alliance (-371, confidence 1). Try https://en.wikipedia.org/wiki/Chalcidian_League
- `/ledger/47`: Exit years of Elis, Megara and Troezen (/ledger/47-49, confidence 1 at -366). Try https://en.wikipedia.org/wiki/Peloponnesian_League
- `/ledger/50`: Which border districts Philip gave to Messene, Megalopolis, Tegea and Argos after 338 (confidence 1 border band); the Sparta page says only that Philip 'invaded and devastated much of Laconia'. Try https://en.wikipedia.org/wiki/Megalopolis,_Greece
- `/ledger/53`: Mantinea's Achaean interlude (Aratus 227, back to Sparta 226: 'In 226 BC, the citizens of Mantinea appealed to Cleomenes to expel the Achaeans'); achaean-league /ledger/10 has a -226 loss of Mantinea to this dossier with no gain here. Try https://en.wikipedia.org/wiki/Cleomenean_War
- `/ledger/57`: Year Argos passed to Nabis (confidence 1, 200-196 on the page; achaean-league says -198). Try https://en.wikipedia.org/wiki/Nabis

## odrysian-kingdom: fix

Area: Odrysian kingdom infobox 'Total: 160,000 km2' with no year; under a factor of two and explained in the notes (coastal cities and Danube tribes not drawn).

Findings:

- `/ledger/4/confidence` (applied by the reviewer). Confidence 3 on a hedged sentence. Evidence: Cersobleptes page: 'The peninsula seems to have been finally ceded to the Athenians in 357 BC'; the mirror second-athenian-league /ledger/7 is at 2 for this reason. Fix: confidence 2 (done).
- `/ledger/6/confidence` (applied by the reviewer). The -347 loss of the western kingdom (Strymon to Maroneia) cites a sentence about the east: the page does not say what the note claims. Evidence: Philip II page: 'In 347 BC, Philip advanced to the conquest of the eastern districts about Hebrus' and 'compelled the submission of the Thracian prince Cersobleptes'; it names Abdera and Maronea for 354-353 and no western Thracian king. macedonian-empire /ledger/8 reads the same sentence as Cersobleptes' vassalage. Keyframe odrysian-kingdom_-347 rests on this event. Fix: confidence 1 (done); a gap-filler should date the west's absorption (Cetriporis page) and the author move the event and the -347 keyframe if needed.
- `/ledger/19/year` (applied by the reviewer). Mis-dated by one year: the vassalage to Lysimachus ends at his death in 281, not 282 (the note itself says February 281). Evidence: Lysimachus page: 'Died: February 281 BC'; 'In 281 BC, Lysimachus met Seleucus at the Battle of Corupedium'; kingdom-of-lysimachus ends -281/2. Fix: year -281 (done; no month, so that it sorts before the -281 dissolve).

Spot checks:

- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Cersobleptes)
- `/ledger/4`: confirmed (hedged; confidence lowered to 2) (https://en.wikipedia.org/wiki/Cersobleptes)
- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Cersobleptes)
- `/ledger/6`: not on page (https://en.wikipedia.org/wiki/Philip_II_of_Macedon)
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Odrysian_kingdom)
- `/ledger/19`: mis-dated (fixed) (https://en.wikipedia.org/wiki/Lysimachus)

Gaps for a gap-filler:

- `/ledger/6`: Year the western kingdom of Berisades/Cetriporis was absorbed by Macedon (now confidence 1). Try https://en.wikipedia.org/wiki/Cetriporis
- `/ledger/0`: Teres I's extent at the founding and the -450 expansion (/ledger/0-1, confidence 1). Try https://en.wikipedia.org/wiki/Teres_I
- `/ledger/10`: Extent of the tributary rump 340-325 and of Seuthes III's realm (/ledger/10, /ledger/12, confidence 1). Try https://en.wikipedia.org/wiki/Seuthes_III
- `/identity/capitals`: No capital before -320 (Seuthopolis only) for a state from -480. Try https://en.wikipedia.org/wiki/Odrysian_kingdom

## cimmerian-bosporus: fix

Area: The Bosporan Kingdom infobox gives no area. The 776-year row is kept as one state with rename events, which the page supports ('Established: c. 438 BC' / 'Disestablished: c. AD 527', one kingdom).

Findings:

- `/ledger/23` (for the author). The Gothic and Hunnic overlordships that the dossier's own notes and certainty describe are missing from the ledger, so the 373..527 keyframe is drawn as an independent kingdom throughout. Evidence: Bosporan Kingdom page: 'the Goths later held power in the Crimea, from c. 380 onwards' and the kingdom was 'regaining its independence after the empire's collapse in the 450s and 460s'; /ledger/23 note quotes the Rhescuporis VI page (Goths 'took power over at least parts of the Bosporan Kingdom c. 380', then 'likely ... a Hunnic invasion'); /certainty/4 names 'Gothic control c. 380, a Hunnic period'. Fix: Add a vassal_start/vassal_end pair for the Goths from c. 380 and one for the Huns ending c. 455-469 (confidence 1-2, counterpart huns, which runs to 469), and ask the huns owner for the mirror.

Spot checks:

- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Bosporan_Kingdom)
- `/ledger/10`: confirmed (https://en.wikipedia.org/wiki/Pharnaces_II_of_Pontus)
- `/ledger/14`: confirmed (https://en.wikipedia.org/wiki/Pharnaces_II_of_Pontus)
- `/ledger/21`: confirmed (end of the 2nd century; the year 193 is on the Sauromates II page, not opened) (https://en.wikipedia.org/wiki/Bosporan_Kingdom)
- `/ledger/22`: confirmed (https://en.wikipedia.org/wiki/Tanais)
- `/ledger/24`: confirmed (https://en.wikipedia.org/wiki/Bosporan_Kingdom)

Gaps for a gap-filler:

- `/ledger/2`: Year Nymphaion passed from Athens (-405, confidence 1). Try https://en.wikipedia.org/wiki/Nymphaion_(Crimea)
- `/ledger/7`: Who held the Azov shore before the Bosporans (Maeotian tribes, confidence 1). Try https://en.wikipedia.org/wiki/Maeotians
- `/ledger/17`: Year Phanagoria was recovered (-16, confidence 1). Try https://en.wikipedia.org/wiki/Phanagoria
- `/ledger/23`: What the Huns took in the 370s (confidence 1). Try https://en.wikipedia.org/wiki/Chersonesus

## Cross-dossier matrix

Status counts: exception 31, matched 22, mismatch 12, missing 14. Exceptions are counterparts listed for a dossier, Greek poleis left to the eu-01-x additions batch (not run), and kingdom-of-pontus, roman-empire and goths (groups not run). Mismatches and missing mirrors:

- sacred-band-of-thebes /ledger/1 -371 gain (Orchomenus) -> greek-city-states /ledger/26 -379 loss: **mismatch**. Counterpart 'Orchomenus' has no dossier and is not listed; greek-city-states /ledger/26 gives all Boeotia (Thebans -350 shape, which contains Orchomenus) to this dossier at -379, while this dossier keeps Orchomenus out until -371: Orchomenus is nobody's -379..-372. Use counterpart greek-city-states and add a -371 loss there.
- sacred-band-of-thebes /ledger/2 -370 vassal_start (Theban allies in central and western Greece) -> greek-city-states /ledger/31 -366 loss: **mismatch**. The central-Greek allies are greek-city-states land; that dossier has a -366 loss (confidence 1) where this one has a -370 vassal_start, and a -350 gain (/ledger/37) where this one ends the alliances in -362. Pages: 'By late 370' (Epaminondas), 'ended ... at Mantinea in 362 BC' (Theban hegemony). Route to eu-01.
- second-athenian-league /ledger/3 -377 vassal_start (Allied cities that became independent in 355) -> greek-city-states /ledger/28 -377 loss: **mismatch**. Name-string counterpart; the land is greek-city-states', whose /ledger/28 loses it to this dossier at -377 (as a loss, not a vassalage). Use counterpart greek-city-states.
- second-athenian-league /ledger/4 -377 vassal_start (Allied cities that stayed with Athens) -> greek-city-states /ledger/28 -377 loss: **mismatch**. As /ledger/3: name-string counterpart; mirror is greek-city-states /ledger/28 (-377 loss).
- second-athenian-league /ledger/13 -355 loss (greek-city-states) -> greek-city-states /ledger/35 -355 gain: **mismatch**. greek-city-states /ledger/35 regains only Chios, Rhodes, Byzantion and Cos; the other members that left in 355 ('most of the allied cities became independent', league page) have no mirror gain.
- second-athenian-league /ledger/17 -338 loss (greek-city-states) -> greek-city-states /ledger/40 -338 gain: **mismatch**. greek-city-states /ledger/40 gains Attica only; this loss also hands over the -350 islands (Samos stayed Athenian: Chaeronea page 'allowed to keep their colony on Samos') and the Chersonese, which the Chaeronea page does not mention (Macedon is the likelier taker).
- peloponnesian-league /ledger/56 -222 loss (achaean-league) -> achaean-league /ledger/13 -224 gain: **mismatch**. Argos back to the Achaeans: -222 here, -224 in achaean-league; the Cleomenean War page gives no year (confidence lowered to 1 here by the reviewer).
- peloponnesian-league /ledger/57 -197 gain (antigonid-dynasty) -> achaean-league /ledger/19 -198 loss: **mismatch**. Argos to Nabis: this dossier has it from Macedon in -197 (counterpart corrected to antigonid-dynasty), but antigonid-dynasty has no -197/-198 loss of Argos, and achaean-league /ledger/19 has Argos lost directly to this dossier in -198. Three dossiers to reconcile (eu-01-c, eu-02 owners).
- peloponnesian-league /ledger/59 -195 loss (League of Free Laconians) -> none: **missing**. League of Free Laconians has no dossier and is not in counterparts_needing_dossiers (added to the reviewer's list).
- odrysian-kingdom /ledger/1 -450 gain (Thracian tribes) -> none: **missing**. 'Thracian tribes' is a name string; acceptable as a nobody-like counterpart only if the author says so (use 'nobody' or a named tribe).
- odrysian-kingdom /ledger/5 -352 vassal_start (macedonian-empire) -> macedonian-empire /ledger/8 -347 vassal_start: **mismatch**. Cersobleptes' submission: 352 here (Cersobleptes page: hostage after the 352 invasion; Odrysian page: Heraion Teichos 351) against 347 in macedonian-empire (Philip II page: 'In 347 BC ... compelled the submission of the Thracian prince Cersobleptes'). Both have a page; pick one or record both (352 hostage, 347 submission).
- odrysian-kingdom /ledger/6 -347 loss (macedonian-empire) -> macedonian-empire /ledger/8 -347 vassal_start: **mismatch**. This dossier loses the western kingdom in -347 citing the Philip II page, whose 347 sentence is about the eastern districts and Cersobleptes (the macedonian-empire reading). macedonian-empire has no gain of the west at any year. Confidence lowered to 1 by the reviewer; the west's date needs a page (Cetriporis).
- odrysian-kingdom /ledger/9 -340 loss (macedonian-empire) -> none: **missing**. No -340/-341 gain of the eastern kingdom in macedonian-empire (its /ledger/10 takes all 'Thrace' in -342). Route to eu-02.
- odrysian-kingdom /ledger/10 -340 vassal_start (macedonian-empire) -> none: **missing**. No -340 vassal_start of the Odrysian tributary rump in macedonian-empire (Odrysian page: 'put under the loose control of a Strategos', tithes). Route to eu-02.
- odrysian-kingdom /ledger/12 -325 gain (macedonian-empire) -> none: **missing**. No c. -325 loss to Seuthes III in macedonian-empire (Odrysian infobox: 'Rebellion of Seuthes III: c. 330'; Seuthes III page c. 325). Route to eu-02.
- odrysian-kingdom /ledger/15 -321 vassal_start (kingdom-of-lysimachus) -> kingdom-of-lysimachus /ledger/6 -310 vassal_start: **mismatch**. Seuthes III under Lysimachus: vassal from -321 here, from -310 in kingdom-of-lysimachus (whose contest runs -323..-310, against two contests -322..-321 and -313..-312 here). Reconcile on the Seuthes III page.
- cimmerian-bosporus /ledger/3 -389 gain (Sindi kingdom) -> none: **missing**. Sindi kingdom has no dossier and is not listed (added to the reviewer's list).
- cimmerian-bosporus /ledger/7 -230 gain (Maeotian tribes) -> none: **missing**. 'Maeotian tribes' is a name string with no dossier; confidence 1.
- cimmerian-bosporus /ledger/12 -63 loss (Phanagoria (free city)) -> none: **missing**. Phanagoria as a free city (-63..-16) has no dossier and is not listed (added).
- cimmerian-bosporus /ledger/13 -48 gain (roman-republic) -> none: **missing**. roman-republic has no -48 loss of Colchis, Lesser Armenia and Pontus; partly client land (Pharnaces II page: he 'seized Colchis', 'Lesser Armenia, part of Cappadocia', 'the rest of Pontus'). Route to the roman-republic owner.
- cimmerian-bosporus /ledger/14 -47 loss (roman-republic) -> none: **missing**. roman-republic has no -47 regain after Zela.
- cimmerian-bosporus /ledger/17 -16 gain (Phanagoria (free city)) -> none: **missing**. Phanagoria (free city) has no dossier; confidence 1.
- cimmerian-bosporus /ledger/21 193 gain (Crimean Scythians) -> none: **missing**. 'Crimean Scythians' (the late Scythian kingdom of Scythian Neapolis) has no dossier and is not listed; scythia ends -224 (added to the reviewer's list).
- cimmerian-bosporus /ledger/23 372 loss (huns) -> none: **missing**. huns has no event naming cimmerian-bosporus (its 370s gains are from the Alans and gothia). Route to the huns owner.
- greek-city-states /ledger/37 -350 gain (sacred-band-of-thebes) -> sacred-band-of-thebes /ledger/11 -362 vassal_end: **mismatch**. greek-city-states takes the hegemony's allies back at Cliopatria's -350 (confidence 1); the pages end the hegemony at Mantinea 362. Route to eu-01.
- achaean-league /ledger/10 -226 loss (peloponnesian-league) -> none: **missing**. Mantinea lost to Sparta in 226 (Cleomenean War page: 'In 226 BC, the citizens of Mantinea appealed to Cleomenes to expel the Achaeans'); peloponnesian-league has Mantinea (Tripoli circle) from -229 with no Achaean interlude and no -226 gain.

## Counterparts needing dossiers (beyond the author's list)

- League of Free Laconians (`league-of-free-laconians`, -195..-146): peloponnesian-league /ledger/59
- Orchomenus (Boeotia) (`orchomenus`, -379..-371): sacred-band-of-thebes /ledger/1 (or use greek-city-states)
- Corinth (`corinth`, -550..-366): peloponnesian-league vassal pairs (eu-01-x)
- Megara (`megara`, -519..-366): peloponnesian-league vassal pairs (eu-01-x)
- Tegea (`tegea`, -556..-370): peloponnesian-league /ledger/4, /ledger/38
- Mantinea (`mantinea`, -550..-370): peloponnesian-league vassal pairs
- Elis (`elis`, -550..-366): peloponnesian-league vassal pairs
- Sicyon, Epidaurus, Phlius, Troezen (`sicyon`, -550..-366): peloponnesian-league vassal pairs (one dossier each, eu-01-x)
- Chalcidian League (Olynthus) (`chalcidian-league`, -432..-348): peloponnesian-league /ledger/34, /ledger/37
- Sindi kingdom (Sindica) (`sindica`, -500..-389): cimmerian-bosporus /ledger/3
- Phanagoria (free city) (`phanagoria`, -63..-16): cimmerian-bosporus /ledger/12, /ledger/17
- Scythian kingdom of Crimea (Scythian Neapolis) (`scythian-neapolis`, -250..193): cimmerian-bosporus /ledger/21 (scythia ends -224)
- Tylis (Celtic kingdom in Thrace) (`tylis`, -278..-212): odrysian-kingdom successors and /ledger/20

## Gazetteer names needed

Arcadia (region), Messenia (region), Laconia (region), Elis (region), Argolid (region), Thyreatis (region), Chalcidice (region), Orchomenus (place), Coronea (place), Chaeronea (place), Tegea (place), Mantineia (place), Megalopolis (place), Sikyon (place), Epidaurus (place), Phlius (place), Troezen (place), Megara (place), Decelea (place), Gytheio (place).

## Problems

- No page failed to load. Neighbour dossiers greek-colonies and achaemenid-empire are not written yet (groups eu-02 and me-05 have not produced them); no batch event names them.
- Reviewer applied six small fixes in place and re-validated both files (valid): peloponnesian-league /ledger/55, /ledger/57, /wars/10, /wars/11 counterpart antigonid-macedonia -> antigonid-dynasty; /ledger/50 and /wars/8 border_band year -337 -> -338; /ledger/56 confidence 2 -> 1; odrysian-kingdom /ledger/4 confidence 3 -> 2, /ledger/6 confidence 2 -> 1, /ledger/19 year -282 -> -281. Each carries a '[Reviewer eu-01-c, 2026-10-18: ...]' remark in its note.
- sacred-band-of-thebes and thebans should be merged into one dossier (sacred-band-of-thebes, both Cliopatria names); the author offered this and left the choice to the reviewer/orchestrator. greek-city-states /ledger/42 then needs its counterpart renamed.
- Mirror fixes owned by other groups: eu-01 (greek-city-states /ledger/26 Orchomenus, /ledger/28 year 378, /ledger/31 and /ledger/37 Theban years and type, /ledger/35 other league members, /ledger/40 land); eu-02 (macedonian-empire: Odrysian events of 347, 340, 325 and the Theban garrison of 338; kingdom-of-lysimachus vassal year; antigonid-dynasty Argos 197); achaean-league (Argos 224, Mantinea 226, Argos 198); huns (Bosporus 372 and overlordship); roman-republic (Pharnaces II 48-47).
- The three kept dossiers (peloponnesian-league, odrysian-kingdom, cimmerian-bosporus) were written in an earlier run and list name-string counterparts (Greek poleis, tribes) that are not in this batch's counterparts_needing_dossiers; added to this report's list.
