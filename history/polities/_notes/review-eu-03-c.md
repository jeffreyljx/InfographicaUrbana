# Review of batch eu-03-c (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: mamertines, italian-city-states, thracian-kingdom. Validator: 0 errors, 0 warnings (also with --resolve) before and after the reviewer fixes. Neighbours read: roman-republic, carthage, greek-city-states, greek-colonies, syracuse; roman-empire (eu-04) and ptolemaic-kingdom (me-05) are not written yet.

Verdicts: mamertines **fix**, italian-city-states **fix**, thracian-kingdom **thin**. "fix" with applied: true means the reviewer made the change in place; items with applied: false are for the author or gap-filler.

## mamertines: fix

### Findings
- `/identity/family` (applied): 'italic-mercenary' is not a key of colours.json families. Evidence: colours.json families has 29 keys (africa ... steppe) and no 'italic-mercenary'; the Italic peoples of this group use 'italy' (etruscans, fixed the same way in review eu-03-a). Fix: family 'italy'.
- `/ledger (after /ledger/3)` (NOT applied): No vassal-side events mirror roman-republic's vassal_start mamertines (-264) and vassal_end mamertines (-257). Evidence: roman-republic ledger: vassal_start mamertines -264 (c2) and vassal_end mamertines -257 (c1). The vassal side records the relation with the overlord as counterpart elsewhere in the project (greek-city-states: vassal_start roman-republic -272); the reviewer brief 2.3 asks for the mirror. Mamertines page: 'Hard-pressed by Syracuse, the Mamertines appealed to both Rome and Carthage for assistance in 265 BC' (First Punic War page), 'Rome responded by entering into an alliance with the Mamertines' (Mamertines page, no year). Non-blocking: the dossier's notes say the tint comes from roman-republic. Fix: Add vassal_start (counterpart roman-republic, region {cliopatria: Mamertines, year: -264}, -264, c2, First Punic War page) and vassal_end (roman-republic, -257, c1) before the dissolve.

### Thin (for a gap-filler)
- `/ledger/5`: Dissolve -257 is Cliopatria's year at confidence 1; no page dates the end of the Mamertine state. Also roman-republic has only vassal_end at -257 and gains Messana only with Sicily in -241, so Messana is drawn by nobody -257..-241. Page to try: https://en.wikipedia.org/wiki/Messina#History
- `/wars`: The Mamertines fought Pyrrhus (Syracuse appealed to him 'against the Mamertines' in 280 BC, Mamertines page); the syracuse dossier lists mamertines as a belligerent of 'Pyrrhic War (Sicilian campaign)' -278..-276, this dossier has no such war. No land is known to have changed hands; add the war with empty zones if a page confirms Mamertine fighting. Page to try: https://en.wikipedia.org/wiki/Pyrrhic_War
- `/ledger/3`: After expelling the Carthaginian garrison in 264 the Mamertines 'were besieged by both the Carthaginians and the Syracusans' until both withdrew (First Punic War page); the Carthaginian side of the 264 siege is not a contest event here (non-territorial, optional). Page to try: https://en.wikipedia.org/wiki/First_Punic_War

### Spot checks
- `/ledger/0` https://en.wikipedia.org/wiki/Mamertines: confirmed: 'they claimed Messina for themselves in 288 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Mamertines: confirmed at c2: 'In around 270 BC, the Mamertine exploits came to the attention of Syracuse'; Longanus battle undated, as the note says
- `/ledger/2` https://en.wikipedia.org/wiki/Mamertines: confirmed: 'Hiero returned to besiege their base at Messina in 265 BC' and a Carthaginian fleet 'occupied the harbour of Messina'
- `/ledger/3` https://en.wikipedia.org/wiki/First_Punic_War: confirmed: in 264 Caudex's legions reached Messana 'where the Mamertines had expelled the Carthaginian garrison'; 'The war began in 264 BC'
- `/ledger/4` https://en.wikipedia.org/wiki/First_Punic_War: confirmed at c2: 'first the Syracusans, and then the Carthaginians withdrew from the siege' (264); Syracuse allied with Rome in 263

Area: infobox None (year None), Cliopatria 933.8 km2, ratio None. The Mamertines page has no infobox; one city territory, 934 km2 is plausible.

## italian-city-states: fix

### Findings
- `/identity/family` (applied): 'italic' is not a key of colours.json families. Evidence: colours.json families has no 'italic'; the Italic peoples use 'italy' (etruscans, review eu-03-a). Fix: family 'italy'.
- `/ledger/2 (capital_move to Bovianum)` (applied): Mis-dated at confidence 3: dated 90 BC, but the page places the fall of Corfinium and the move to Bovianum in its 89 BC narrative; the quoted wording is not on the page. Evidence: Social War (91-87 BC): 'Corfinium was also taken, forcing the Italians to transfer their capital to Bovianum.' This sits after 'The new consuls for 89 BC were Gnaeus Pompeius Strabo and Lucius Porcius Cato'; no explicit year is given. The dossier quoted 'was taken by the Romans, and the Italians moved their capital to Bovianum' under 90 BC. Fix: year -89, confidence 2, verbatim quote; identity.capitals Corfinium to -89, Bovianum from -89; event moved after the contest_start to keep the ledger order.
- `/ledger/4 (was /ledger/3, loss of the northern theatre)` (applied): Mis-dated at confidence 2: the loss of the Marsic north was dated October 90 BC (the lex Julia), but the page has the north subdued in 89. Evidence: Page: 'The northern front of the war largely collapsed after these victories' (90), then in 89 the Romans 'forced the Marsi to petition for peace', 'also subjugated the Vestini and the Marrucini', took Corfinium, and 'By summer, the Romans had pacified the northern theatre, except for Asculum'. The author's own keyframe 0 note says 'the northern theatre collapsed in 89'; the old date also put the capital Corfinium inside land already lost. roman-republic's gain is -89/11. Fix: year -89, month 6 ('by summer'), with the page's sentences added to the note; the event now sorts after the two -89 capital moves.
- `/ledger/1/note` (applied): Misquote: the note had Marius defeat the Marsi near the Fucine Lake 'in 91 BC'. Evidence: Page: the Battle of the Tolenus River was 11 June 90 BC, after which Marius 'inflicted a defeat on the Marsi near the Fucine Lake' (90 BC campaign). Fix: Note rewritten with the page's words and 90 BC; the event itself (contest_start late 91, 'The war began in late 91 BC with the rebellion of Asculum') is right.

### Thin (for a gap-filler)
- `/identity/wikidata`: Q4115680 is the medieval 'Italian city-states' item (author flagged; wikidata.org unreachable). The Social War or 'Italia' confederation id is needed; route to the identity/colour agent. Page to try: https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC)

### Spot checks
- `/ledger/1` https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC): confirmed (start 'late 91 BC'); note misquoted the Fucine Lake year (fixed)
- `/ledger/2` https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC): mis-dated: 89 BC narrative, not 90 (fixed, confidence 3 to 2)
- `/ledger/4` https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC): mis-dated: north pacified 'By summer' 89, not October 90 (fixed)
- `/ledger/5` https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC): confirmed: Asculum surrendered November 89 BC after Vidacilius' suicide
- `/ledger/7` https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC): confirmed: Silo killed in 88 BC in Apulia, defeated by Metellus Pius
- `/ledger/8` https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9387_BC): confirmed: Samnites and Lucanians 'nominal pacification' in 87; Bruttium remnant; settlement siding with Cinna and Marius

Area: infobox None (year None), Cliopatria 36108.7 km2, ratio None. Social War page has no area (infobox gives dates, location, strengths only); the 36,109 km2 blob matches the page's two theatres less Capua, central Campania and Naples.

## thracian-kingdom: thin

### Findings
- `/identity/family` (applied): 'thracian' is not a key of colours.json families. Evidence: colours.json families has no 'thracian'; 'balkans' is the family for Bulgaria's land. Fix: family 'balkans'.
- `/keyframe_review/4/correction and /keyframe_review/5/correction (also /ledger/6, /ledger/9-11, /identity/successors/0/land)` (NOT applied): The AD 6 Moesia removal leaves Romanian Dobruja (Constanta and Tulcea, the delta coast added by the -27 shape) inside the client kingdom to AD 46, although the keyframe 4 note says the kingdom keeps only 'the land south of the Haemus'. Evidence: Gazetteer 'Moesia' is a union of north-Bulgarian and Serbian admin1 (Vidin ... Silistra, Dobrich, Varna, Borski ...) without Constanta or Tulcea; 'Dobruja' is Constanta, Tulcea, Dobrich, Silistra. shapes.csv thracian-kingdom_-27 bbox reaches 29.67 E, 45.56 N. Sapaean kingdom page: no mention of Moesia, Dobruja or the Black Sea coast. Fix: Add {region: Dobruja} to the minus union in keyframes 4-5, the AD 6 loss, the 44-46 events and the successor land, or say in the keyframe 4 note why the delta coast stays Thracian.
- `/identity/rulers` (NOT applied): Rulers overlap (Rhescuporis I -48..-41, Cotys II -42..-15), start at -57 (life starts -87), and list Sapaean kings before 31 BC although the dossier's own rename (/ledger/3) has the Odrysian-Astaean house ruling the kingdom until 31. Evidence: Sapaean kingdom page list: Cotys I (57-48 BC), Rhescuporis I (48-41 BC), Cotys II (42-15 BC), Rhoemetalces I (15 BC-12 AD), Cotys III (12-18) east and Rhescuporis II (12-19) west, Rhoemetalces II (19-38), Rhoemetalces III (38-46); the page says the Sapaean kingdom 'existed from the middle of the 1st century BC' and 'The Romans removed the Odrysian-Astaean royal family from power' after Actium. Fix: Start the rulers list at -31 (Cotys II -31..-15, then as now), or mark the pre-31 entries as rulers of the separate Sapaean principality in their notes; make consecutive entries meet (Cotys II from -41).
- `/ledger (after /ledger/3)` (NOT applied): No vassal-side event mirrors roman-republic's vassal_start thracian-kingdom (-31, month 9). Evidence: roman-republic ledger: vassal_start thracian-kingdom -31/9 (c2), region {cliopatria: Thracian Kingdom, year: -30} (untrimmed, includes Wallachia), with no vassal_end before its -27/1 dissolve into roman-empire. Vassal side records the overlord as counterpart elsewhere (greek-city-states vassal_start roman-republic -272). Fix: Add vassal_start roman-republic -31/9 (Sapaean page, c2) and vassal_end roman-republic -27/1, vassal_start roman-empire -27/1 and vassal_end roman-empire 46 (or one pair with roman-empire once eu-04 settles whether the client relation continues from the Republic).

### Thin (for a gap-filler)
- `/keyframe_review/3`: The -27 shape adds about 7,550 km2 (Black Sea coast to the Danube delta) with no ledger event; kept at confidence 1. A gain (counterpart: the Getae of Rholes or nobody, Crassus' 29-28 BC Moesian campaign) or a removal is needed. Page to try: https://en.wikipedia.org/wiki/Marcus_Licinius_Crassus_(consul_30_BC)
- `/ledger/0`: Found -87 at confidence 1: no page founds the state; the Macedonia page names a Thracian king Sordinus in 89 BC and Thracian attacks with Mithridates 'From 87 BC onwards'. Page to try: https://en.wikipedia.org/wiki/Sadalas_II
- `/ledger/2 to /ledger/3`: No event for -85..-31 (54 years): the Macedonia page lists Lucullus' campaign against the Bessi (73-71 BC) and the Dardanian-Bessi invasion under Piso (57-55 BC); whether these touched the kingdom is unchecked. Page to try: https://en.wikipedia.org/wiki/Bessi
- `/ledger/6`: AD 6 Moesia removal at confidence 1: the Macedonia page says only 'Moesia was split off as a separate military command some time before 10 BC, and had become a separate province by AD 6'; whether the client kings ever held the Danube bank is unknown. Page to try: https://en.wikipedia.org/wiki/Moesia
- `/identity/capitals/0`: Bizye carried back to -87 at confidence 1; no page names the Odrysian-Astaean seat before 31 BC. Page to try: https://en.wikipedia.org/wiki/Bizye

### Spot checks
- `/ledger/1` https://en.wikipedia.org/wiki/Macedonia_(Roman_province): confirmed: 'From 87 BC onwards, Thracian forces allied with Mithridates VI attacked Macedonia, as part of the First Mithridatic War' (c1 could be 2)
- `/ledger/3` https://en.wikipedia.org/wiki/Sapaean_kingdom: confirmed: 'Probably soon after the Battle of Actium in 31 BC'; Odrysian-Astaean family removed, 'entire kingdom under Sapaean rule with Bizye acting as the initial center'
- `/ledger/6` https://en.wikipedia.org/wiki/Macedonia_(Roman_province): confirmed (wording): Moesia 'had become a separate province by AD 6'; the land assignment is the author's (c1)
- `/ledger/7` https://en.wikipedia.org/wiki/Odrysian_kingdom: confirmed: 'In 21 AD king Rhoemetalces II took refuge in Philippopolis when he was confronted with a rebellion, among them Odrysians'; 'their uprising failed'
- `/ledger/11` https://en.wikipedia.org/wiki/Sapaean_kingdom: confirmed: 'In 46 AD, Roman Emperor Claudius put an end to the kingdom by annexing it'; Odrysian page 'dissolved the Sapaean kingdom in 45/6 and turned it into the province of Thracia'

Area: infobox 160000 (year None), Cliopatria 90345.1 km2, ratio 0.56. No article or infobox for this state (Sapaean kingdom page has none); the only figure is the Odrysian kingdom infobox 160,000 km2 with no year, for the classical kingdom at its height (Teres and Sitalces, Danube to Abdera). Under a factor of two; the dossier cites it in sources.

## Cross-dossier matrix

- mamertines -288 found (greek-city-states) <-> greek-city-states -288 loss: **matched**. greek-city-states /ledger loss mamertines -288 (c3)
- mamertines -265 occupation_start (carthage) <-> carthage -265 occupation_start: **matched**. harbour of Messina
- mamertines -264 occupation_end (carthage) <-> carthage -264 occupation_end: **matched**. 
- mamertines -270 contest_start (syracuse) <-> syracuse -270 contest_start: **matched**. contest_end -264 matched on both sides too
- roman-republic -264 vassal_start (mamertines) <-> none: **missing**. mamertines has no vassal_start roman-republic -264 (finding /ledger, applied false)
- roman-republic -257 vassal_end (mamertines) <-> mamertines -257 dissolve: **mismatch**. mamertines dissolves -257 with successor roman-republic, but roman-republic records only a vassal_end (no gain) and takes Messana only with Sicily in -241 (gain carthage, Sicily minus Syracuse): Messana is unowned -257..-241. One side must assign it (roman-republic gain mamertines -257, or keep the vassal relation to -241).
- italian-city-states -91 found (roman-republic) <-> roman-republic -91 loss: **matched**. 
- italian-city-states -89 loss (roman-republic) <-> roman-republic -89 gain: **matched**. northern theatre: was -90/10 (13 months before roman-republic's -89/11 gain); moved by the reviewer to -89/6 per the page
- italian-city-states -89 loss (roman-republic) <-> roman-republic -89 gain: **matched**. Asculum -89/11 and Campania -89/12 both inside roman-republic's -89/11 gain (shape minus Samnium, Basilicata, Apulia)
- italian-city-states -88 loss (roman-republic) <-> roman-republic -88 gain: **matched**. Apulia
- italian-city-states -87 loss (roman-republic) <-> roman-republic -87 gain: **matched**. Samnium and Basilicata; dissolve -87 to roman-republic agrees
- roman-republic -31 vassal_start (thracian-kingdom) <-> none: **missing**. thracian-kingdom has no vassal-side event; roman-republic's region {cliopatria: Thracian Kingdom, year: -30} is not trimmed of Wallachia as the thracian dossier's keyframes are, and roman-republic has no vassal_end before its -27/1 dissolve
- thracian-kingdom -87 contest_start (roman-republic) <-> roman-republic -88 contest_start: **mismatch**. roman-republic has contest_start kingdom-of-pontus -88 (Greece, Macedonia, Thrace) and lists thracian-kingdom in the First Mithridatic War, but no contest_start thracian-kingdom; minor, non-territorial
- thracian-kingdom 6 loss (roman-empire) <-> none: **exception**. roman-empire is owned by group eu-04, which has not run (file absent on 2026-10-19); listed in the author's counterparts_needing_dossiers
- thracian-kingdom 46 dissolve (roman-empire) <-> none: **exception**. roman-empire (eu-04) should carry gain thracian-kingdom 46 and vassal_end thracian-kingdom 46

## Other

- Neighbour dossiers read: roman-republic, carthage, greek-city-states, greek-colonies (no events for this batch), and syracuse (not in the Context list but a counterpart of mamertines). roman-empire and ptolemaic-kingdom are not on the mount yet (eu-04, me-05).
- The dossiers' quotes are often paraphrases inside quotation marks (e.g. 'A separate, unsuccessful revolt followed in 11 BC' for the page's 'Another unsuccessful revolt broke out in 11 BC'); the facts checked agree with the pages except the two Social War dates fixed here.
- roman-republic.json was rewritten by another agent during this review (ledger indices shifted between reads); cross-checks use year and type, not indices.
- Reviewer fixes applied in place and re-validated (0 errors, 0 warnings with --resolve): mamertines family; italian-city-states family, /ledger/1 note, capital move to Bovianum (-90 to -89, c3 to c2), northern loss (-90/10 to -89/6), capitals; thracian-kingdom family.
- Gazetteer names needed (author list, all thracian-kingdom; used only as circles/admin1 unions or in notes): Bizye (place), Rhodope (region), Haemus (region), Seuthopolis (place).
