# eu-03-x: Roman Republic, additions (states Cliopatria lacks)

Written 2026-10-19 by the Phase B research agent of batch eu-03-x. No Cliopatria row is owned by this batch; every dossier here is a new state (`cliopatria_names: []`, every keyframe new).

## What is in the folder

(Updated 2026-10-19: the 16 kept dossiers were repaired after review; see the last section, 'Repair of 2026-10-19'.)

- Written in this run (12, pages opened 2026-10-19): arverni, allobroges, ligures, bruttii, helvetii, aedui, sequani, messapii, kingdom-of-noricum, capua, cantabri, cenomani.
- Kept unchanged from an earlier run (16, validated, sources dated 2026-10-18, not re-opened): adriatic-veneti, aequi, boii, celtiberians, insubres, latin-league, lucanians, lusitanians, picentes, sabines, samnites, senones, sertorian-hispania, syracuse, umbri, volsci. They were written at 07:20 on 2026-10-18 in one pass; no notes or report from that run exist.

## Things the orchestrator and reviewer should know first

1. The 11 tribal dossiers kept from the earlier run (adriatic-veneti, aequi, celtiberians, latin-league, lucanians, lusitanians, picentes, sabines, samnites, umbri, volsci) have `type: umbrella`. The schema reserves umbrella for associations that are not territory ("never coloured as territory"). If the colour agent skips umbrellas, these peoples vanish from the map and the contests in roman-republic's ledger (Samnites, Lucanians, Aequi...) have nothing to blend with. They should probably be `state`.
2. Those 16 dossiers have empty `keyframe_review`; the brief wants a new keyframe per period. Their found-event regions carry the shape, so a gap-filler can turn each found/loss pair into keyframes without new pages.
3. Families: the kept dossiers use `italic`, `gallic`, `celtic`, `venetic`, `latin`, `iberian`, `greek`, none of which is a key of colours.json `families`; the 12 new ones use registry keys (france, italy, austria, iberia). The colour agent should map the old values.
4. roman-republic.json (eu-03-b) names counterparts as strings that now have slugs: 'Arverni and Allobroges' (-121) should become arverni and allobroges; 'Gallic tribes (Helvetii, Suebi, Belgae, Veneti, Arverni)' (-58..-52) should name helvetii, aedui, sequani, arverni; 'Messapii and Sallentini' (-267, -266) messapii; 'Ligures' (-238, -155) ligures; the -216 and -211 Capua events name carthage but should name capua; the -203 gain names carthage for Bruttium and should name bruttii. It also lacks vassal ties for allied peoples: bruttii after c. 272, capua from 343, helvetii 58-52, cenomani 225-89, and a Ligures gain in 155.
5. Nothing in this batch moves a Cliopatria row. Five dossiers end a state whose people were not simply conquered but kept an allied or autonomous status (helvetii at 58; arverni, aedui and sequani at 52; allobroges at 121), the end years matching roman-republic's Gallic gains; a gap-filler may prefer vassal treatment.

## Per state

### arverni (-250..-52)
Pages: Arverni, Bituitus, Allobroges, Gallia Narbonensis, Battle of Alesia. The Arverni page has no infobox, no area, no founding (first record 207 BC) and no extent for the hegemony of Luernius and Bituitus (Strabo's reach to Narbonne 'heavily exaggerated'). Start 250, the client tie (200) and the client departments (Velay, Gevaudan, Quercy: the page does not place the Vellavii, Gabali, Cadurci, Eleuteti) are confidence 1. Dates differ: Isere battle August 121 (Allobroges page) or autumn (Bituitus page).

### allobroges (-218..-121)
Pages: Allobroges, Battle of Vindalium, Gallia Narbonensis, Bituitus. Start 218 is the first dated mention (Hannibal). The Vindalium page is silent on the province and on the Allobroges' later status; the Allobroges page says they kept autonomy and territory inside the province, so the state ends at 121 only to match roman-republic. The revolt of Catugnatus (62-61) is outside the dossier's life and is in the notes only. Land north of the Rhone between Lyon and Geneva (held 'by the mid-1st century BC') is not drawn.

### ligures (-500..-155)
Pages: Ligures, Apuani, Ingauni. A tribal group, not one state; type `state` so roman-republic's contest (-238..-155) has a land. Not placed because no page does: the Friniates (187), the Statielli (173, 'Carystus, unlocated'), the ager Ligustinus et Gallicus, Genoa (an ally from 218). The Ingauni were subjugated in 181 but left their coastal land (Ingauni page). Salyes (transalpine Ligurians) need their own dossier.

### bruttii (-356..-203)
Pages: Bruttii, Bruttium, Second Punic War, Alexander I of Epirus, Pyrrhic War. The pages disagree on Alexander's death (331 on his page, 326 on the Bruttii page) and conquests (Terina, per his page; Consentia too, per the Bruttii page). The Agathocles raid and capture of Hipponium and the peace after Pyrrhus (half of the Sila forest) are undated on the pages and not placed or bridged beyond confidence 1. The end 203 is the midpoint of the page's '204-2'. The Second Punic War page does not date the Bruttian defection or Hannibal's departure.

### helvetii (-100..-58)
Pages: Helvetii, Battle of Bibracte, Orgetorix. No infobox, no borders, no capital before Augustan Aventicum (capitals empty). Start 100 is a placeholder (abandonment of the north 'in the late 2nd century BC'). The Bibracte page does not give the surrender terms; the return home and the foederati status are on the Helvetii page.

### aedui (-150..-52)
Pages: Aedui, Battle of Alesia. Start 150 is the date the page offers for the alliance with Rome, not for the tribe. The page is silent on Ariovistus's dates, Magetobriga, the Boii settled with the Aedui in 58, Litaviccus and Noviodunum. Clients (Segusiavi, Mandubii) are undated.

### sequani (-100..-52)
Pages: Sequani, Ariovistus, Battle of Alesia. The Sequani page says Ariovistus seized a third of Sequani land; the Ariovistus page says a third of Aedui land at Magetobriga (61), turning on the Sequani later. The c. 70 loss of the eastern part to Germanic settlers is the page's, its placement in the Haut-Rhin is the researcher's reading. The 52 end is a bridge (confidence 1). An Ariovistus dossier (Germanic settlers in Alsace, c. 71-58) and a Rauraci one would complete this corner.

### messapii (-550..-266)
Pages: Messapii, Iapygians, Brindisi. Pages disagree on the Taras defeat (473 or 470) and on Brundisium (267, 266 or 245). The Daunians and Peucetians (central and northern Apulia) are not drawn. No capital is named. The Archidamus III episode (342-338, Manduria) is on the page but unplaced.

### kingdom-of-noricum (-200..-16)
Pages: Noricum, Kingdom of Noricum, Battle of Noreia. The Noricum page gives both 400 BC and 200 BC for the founding; the Kingdom infobox says 'c. 200 BC-c. 50 AD'. The pages are silent on Voccio, Caesar in 58, Burebista and the Boii in Noricum. Counterpart of the 16 BC loss is roman-empire (Cliopatria's Roman Empire row starts in -31). Slovenian and Croatian fringes are not drawn.

### capua (-424..-211)
Pages: Capua, First Samnite War, Siege of Capua (211 BC). The 'Siege of Capua' title is a disambiguation page; the (211 BC) article was used. The 216 defection year is on neither page (confidence 1). The dossier carries no shape for 343-217, when Capua was under Roman supremacy. The Etruscan Capua before 424 is the etruscans dossier's.

### cantabri (-200..-19)
Pages: Cantabri, Cantabrian Wars. The Cantabri page gives no span for the war (29-19 comes from the wars page). Tribes, Astures and Gallaeci have no dossiers. The disc that cuts Palencia, Burgos and Leon to the mountain country is the researcher's.

### cenomani (-400..-89)
Pages: Cenomani (Cisalpine Gaul), Cenomani (disambiguation, no content), Cisalpine Gaul. The Cremona colony is on Cenoman land (page) but undated (218 is roman-republic's); the lex Pompeia (89) is on the Cenomani page only.

## Pages that would not load
None. 'Siege of Capua' and 'Cenomani' are disambiguation pages; the specific articles were opened instead.

## Region names the gazetteer lacks (used as coordinates)
Lucca, La Spezia (Luna), Valence (France), Bibracte, Terina, Thurii/Sibari, Amantea (Clampetia), Vindalium (Sorgues), Noreia (site unknown). All other names resolved (`--resolve` shows 0 warnings for the 12 new dossiers).

## States that still need dossiers
Salyes/Salluvii (transalpine Ligurians, Entremont 123), Ariovistus's Germanic settlers (c. 71-58), Rauraci, Peucetians and Daunians (Apulia), Astures, Gallaeci, Vaccaei, Vettones, Belgae, Veneti of Armorica, Taurini, Lingones, the Sabellic peoples (Marsi, Paeligni, Marrucini, Frentani, Vestini) that roman-republic lists as vassals, and the Arvernian and Aeduan clients (Vellavii, Gabali, Cadurci, Eleuteti, Segusiavi, Mandubii).

## Repair of 2026-10-19 (the 16 dossiers kept from the earlier run, after the reviewer's verdict fail)

The reviewer (history/polities/_notes/review-eu-03-x.md) failed the 16 kept dossiers on one blocking defect: `keyframe_review` was empty. Each now has keyframes built from its found, gain and loss events (shape ids `<slug>_<from>`, verdict adjust, source the state's page); the other findings were applied after reopening the pages named below. All 16 validate with 0 errors and 0 warnings under `--resolve`. In all 16 the Wikidata id was from memory and could not be checked (wikidata.org is unreachable), so it is now null. The earlier points 1-3 above (type umbrella, empty keyframes, families) are resolved: type is state, families are colours.json keys, keyframes exist.

### What changed, per state

- adriatic-veneti: the 181 loss of Aquileia is dropped (the Adriatic Veneti page puts the eastern limit at the Tagliamento; Aquileia, the 'Latin colony... by Rome in 181 BC', lies beyond it). vassal_start 238 and vassal_end 89 (month 12) added; the year 89 now rests on the Lex Pompeia de Transpadanis page ('promulgated by the Roman Consul Pompeius Strabo in 89 BC'), which names no people. Verona is cut out from c. 400 with a loss to cenomani (confidence 1). 3 keyframes.
- aequi: 1 keyframe. The chief centre 'taken by the Romans about 484 BC and again about 90 years later' (Aequi page) is unnamed on that page and on the Alba Fucens page (Aequian town, colony 303, no capture), so the second capture only moves the 389 contest to start in 394 (confidence 2). My own change, not asked: the Roma province in every region is cut by a 40-km disc around Rome (the union drew Aequi land over Rome and Latium).
- boii: Emilia minus Rimini everywhere (the Boii page: Livy gives the Utens as the boundary with the Senones; the gazetteer's Emilia still reaches the Adriatic coast, so its east is an overshoot). vassal_start 225 and vassal_end 218 (month 11) added, plus a gain in November 218 mirroring roman-republic's loss to the Boii (/ledger/57). The 225 contest now ends in 225, at the submission, so the contest and the tint do not overlap (the page: 'After Telamon the Boii made their first formal submission to Rome by treaty'). 191: Rome 'took only about half their territory' stays in the keyframe and event notes; the whole of Emilia is still given because no page says which half. 3 keyframes.
- celtiberians: 2 keyframes (Celtiberia; Celtiberia without Zaragoza from 195). The Cato the Elder page (consul 195; 'reduced Hispania Citerior to subjection'; 'the area between the River Iberus and the Pyrenees') does not say which part of Celtiberia fell and names no Celtiberian town, so Zaragoza stays the researcher's reading (loss confidence 2).
- insubres: runs to 89 (month 12) with vassal_start 197 and vassal_end 89, as roman-republic /ledger/80 and /138 have it. Every region is Lombardy minus Brescia, Cremona and Mantova (Insubres page: 'between the Ticino and the Oglio'; the frontier with the Cenomani 'probably ran along the Oglio'). The founding is 396 from etruscans (etruscans /ledger/14; the Etruscan civilization page: 'from 396 BC: Invasion of the Celts into the Po Valley'; the Insubres page gives only the 4th century). 3 keyframes (none for 222-218, when Rome holds the land).
- latin-league: 2 keyframes (the second without the Alba Longa district from 672). The Aricia capital stays a placeholder: the Aricia page and the Latin League page, both reopened, say nothing of a league centre after Alba Longa.
- lucanians: gain c. 390 and loss 356 of the Cosenza province (Bruttii page: the Lucanians 'established their dominion over the interior' of Bruttium, 'probably' after 390; the Bruttii 'became independent' c. 356), so bruttii's found event has its mirror. The found counterpart is nobody (the displaced Oenotrians, Chones and Lauternoi have no dossier). Vassal model: vassal_start 272, vassal_end 91, dissolve 91 to italian-city-states. The capital Grumentum is replaced by Potentia (Lucania page: 'the most considerable' town of the interior). 4 keyframes. The war's belligerent 'Kingdom of Epirus (Pyrrhus)' is now kingdom-of-epirus.
- lusitanians: every Lusitania region is now the Portuguese districts between the Douro and the Tagus (Aveiro, Coimbra, Viseu, Guarda, Castelo Branco, Leiria, Santarem, Lisboa) plus Caceres (Lusitanians page: 'lived between the rivers Douro and Tagus', 'some areas of the Extremadura region'); the gazetteer's 'Lusitania' takes in the Alentejo and the Algarve. 2 keyframes. The page's 'Starting in 193 BCE, the Lusitanians fought the Romans' gives no ground taken or held, so the contest still starts in 155 (noted on the event). Capitals stay empty (no page names a Lusitanian town).
- picentes: the 390 loss to the Senones is dropped and senones is no longer a successor. The Picentes page does say 'In 390 BC, the Senoni Gauls... occupied Picenum north of the Esino river' and that Picenum is 'all of today's Marche', but the Senones page says they displaced the Umbrians between Ariminum and Ancona; the strip is drawn once, in umbri and senones, and this dossier keeps South Picenum (Macerata, Fermo, Ascoli Piceno, Teramo). vassal_start 299 (treaty after Nequinum) and vassal_end 269 ('in 269 BC revolted') added; roman-republic /ledger/29 has the end in 268. 2 keyframes.
- sabines: the 753 loss is removed (legend; no calendar date, no land on any page). I kept the 15-km disc of Latium north of the Anio in the found region, because the Sabines page puts Sabines there and the mirror loss of 585 (month 9, Collatia and the Anio towns, Lucius Tarquinius Priscus page) needs it; roman-kingdom /ledger/3 now has its mirror. The Roman-Etruscan Wars page gives wars in 505-504 (triumph May 504) and 475 and none in 449, so the single contest 504-449 is replaced by three short ones (504, 475, 449; the last from the Roman expansion page). 2 keyframes.
- samnites: Campania is Campania without Caserta (Capua's, 424-343); vassal model (vassal_start 290, vassal_end 91, dissolve 91 to italian-city-states); 5 keyframes. The Samnites page does not mention Capua or 424; the 424 gain cites the Capua page.
- senones: 1 keyframe. The start 390 now cites the Picentes page (confidence 2); the Senones page gives only 'the 4th century BC'.
- sertorian-hispania: 2 keyframes (-80 to -78, -77 to -72); no new page.
- syracuse: 14 keyframes; vassal_start 263 and vassal_end 215 (roman-republic /ledger/36 and /61); loss to carthage in 311 (Agathocles page: defeated at the Himera River and besieged; carthage /ledger/14), and the 306 gain is now the ring only; contest 397-392 (Dionysius I page; carthage has 398-393). From the thin pages: Gelon (gains in 485 and 483), Dionysius II (rename 367; a loss in 357, 'Other Sicilian cities broke away'), Agathocles (gain c. 313). The Hicetas page is the philosopher's, so the 289 loss stays a confidence-1 bridge; the 263 loss to Rome still repeats the same ring (left in place).
- umbri: vassal model (vassal_start 260, vassal_end 90, dissolve 90) instead of ending in 260; 4 keyframes. Neither the Umbri page nor the Iguvine Tablets page calls Iguvium a capital, and the Umbri page does not mention the Senones (the Senones page does).
- volsci: roman-kingdom added to the war's belligerents (Roman Kingdom page: Tarquinius Superbus 'waged a number of wars against... the Volsci'); 2 keyframes. The Privernum page ('a flourishing Volscian site', destroyed in the late 4th century BC) does not call it a capital.

### Where I disagree with the reviewer, or could not do what was asked

- adriatic-veneti: 'Venetia minus Verona west of the Adige' is drawn as Venetia minus the whole Verona province, because the cenomani dossier claims the whole province; the Veneti page's own western border is Lake Garda, so it also contradicts a Cenomani Verona. The loss to cenomani has no mirror: cenomani's found event names nobody (that dossier passed review and was not touched).
- latin-league and umbri: the pages the reviewer proposed (Aricia, Iguvine Tablets) do not support the capitals; they are kept as confidence-1 placeholders and said so.
- lucanians: the reviewer put the missing gain and loss 'to bruttii'; they are added to lucanians, the dossier that lacked them. bruttii (verdict fix) is untouched.
- picentes: see above; the Picentes page itself supports the loss, the Senones page conflicts; the split is a choice.
- volsci /ledger/4 (304 loss): the mirror is eu-03-b's.
- Samnites, Lucanians: the dossiers end in 91 with a dissolve to italian-city-states, but that dossier names roman-republic as its only predecessor, so the hand-over is one-sided. The Samnites' resistance to Sulla (Colline Gate, 82; Samnites page) is not drawn.

### For eu-03-b (roman-republic) and the orchestrator

- picentes vassal_end is 269 on the Picentes page; roman-republic /ledger/29 has 268.
- volsci /ledger/4: roman-republic has no gain from volsci in 304.
- syracuse contest 397-392 against carthage's 398-393.
- adriatic-veneti loss to cenomani c. 400: cenomani's found event names nobody.
- Gazetteer names needed: Gela, Camarina, Megara Hyblaea (syracuse, coordinates used).
