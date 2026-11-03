# Review of batch sa-02-d (2026-10-19)

Dossiers: gupta-empire, vakataka-kingdom, late-pallava-empire, yaudheya-republic, kadamba-empire.
Neighbour dossiers read (Context list, existing): western-satraps, white-huns, kidarites. Also read because they name this batch's states: alchon-huns, eastern-kushans, kushan-empire, mahameghavahana-dynasty, satavahana-dynasty, early-cholas. Not written yet (exception: group not run yet): chalukya-dynasty, kamarupa-kingdom, sasanian-empire, kalabhra-dynasty, maitraka-dynasty, rashtrakuta-dynasty, indo-sasanian-empire.

Validator (--resolve): 0 errors in all five. Warnings: gupta /ledger/1 nagas-of-padmavati (listed under counterparts_needing_dossiers), yaudheya /wars/0 before the start, and after the reviewer's fix vakataka /ledger/13 kalachuris-of-mahishmati (listed under counterparts_needing_dossiers).

No event in the batch is at confidence 3. Every event spot-checked said what its note claims (WebFetch extracts).

Verdicts: gupta-empire fail; vakataka-kingdom fail; late-pallava-empire thin; yaudheya-republic fail; kadamba-empire thin.

## gupta-empire: fail

Applied by the reviewer:
- /identity/rulers/0: Chandragupta I from 319 -> 320. The ruler started before the state's life (start 320-02). Chandragupta I page: infobox Reign "c. 319 - c. 335", Coronation "26 February 320". Re-validated.

Blocking, not applied:
1. /ledger/3 (347 gain, counterpart "Allahabad Pillar kings (frontier, forest and southern)"). The region is Gupta 347 minus Gupta 324, minus Western Satraps 346, minus Yaudheya 347. It resolves to 4,513 cells. That includes all 1,029 cells of the Eastern Kushans 345 shape (the Punjab, Pakistan) and 688 of the 954 cells of /ledger/1 (the Doab and Naga lands, gained the same year from nagas-of-padmavati). The text says only "Bengal, Odisha, Chhattisgarh, the Andhra coast". eastern-kushans /ledger/6 dissolves in 346 with gupta-empire as successor, but the Gupta ledger has no gain from eastern-kushans.
   Fix: add a 347 gain with counterpart eastern-kushans and region intersect(Eastern Kushans 345, Gupta 347). It can stay tributary under /ledger/5: Samudragupta page, Eraly: "the Kushans still ruled in Punjab, but under the suzerainty of the Gupta Emperor". Subtract that region and /ledger/1's region from /ledger/3, and rewrite /ledger/3's text to describe what remains.
2. /ledger/24, /ledger/27, /ledger/28 (490 loss, 497-528 contest, counterpart white-huns). white-huns /ledger/7 says the Indian part of its 490 shape came from alchon-huns, not from the Gupta. The alchon-huns dossier (ia-01, exists) claims these events against gupta-empire:
   - 496 contest_start (confidence 3)
   - 500 gain of Malwa and Gujarat
   - 515 loss and contest_end (confidence 3)
   - 520-534 occupation (confidence 3 for the end)
   None of these has a mirror here. The Gupta note itself says "the north-west goes to the Alchon Huns".
   Fix: move these events to counterpart alchon-huns. Record the 520-534 occupation, or reject it with a reason. Settle with ia-01 who holds Malwa c. 490-510: Vakataka here, Toramana there (Alchon page: "Having conquered the territory of Malwa from the Guptas, Toramana was mentioned in a famous inscription in Eran").

Not blocking (routed):
- mahameghavahana-dynasty /ledger/3 dissolves in 350 with gupta-empire as successor, and the Gupta has no gain from it. The Mahameghavahana has no Cliopatria cells in 349; its land (Kalinga) sits inside /ledger/3.
- white-huns contest_end 534 against the Gupta's 528. Both pages give 528 (Gupta page: "The Huns were defeated and driven out of India in 528"), so the white-huns side should move or explain.

Spot checks:
- /ledger/0: confirmed (Chandragupta I infobox coronation 26 February 320).
- /ledger/4: confirmed (Samudragupta: "They seem to have become Samudragupta's tributaries").
- /ledger/15-16: confirmed (Gupta Empire: campaign "lasting until 409").
- /ledger/18: confirmed (Narendrasena: "Around 445 CE ... reclaimed his former capital").
- /ledger/24: confirmed with a caveat. The Gupta page says "In the late 490's the Alchon Huns ... broke through the Gupta defences in the northwest"; the Alchon page gives Toramana "c. 490 - 515 CE". 490 holds as Toramana's start; confidence 2 is acceptable.
- /ledger/28: confirmed (528 on both pages).

Area: infobox 3,500,000 km2 (400, high-end) and 1,700,000 km2 (440, low-end). Cliopatria has 1,990,750 in 400 (ratio 1.76) and 2,494,996 in 440 (ratio 0.68). The author quotes both figures. Not a factor of two.

Thin: 19 confidence-1 events, mostly undated Allahabad Pillar conquests. Pages to try: Allahabad Pillar, Eran, Toramana, Maitraka dynasty, Prabhavatigupta.

## vakataka-kingdom: fail

Applied by the reviewer:
- /ledger/13 (510 dissolve): counterpart chalukya-dynasty -> kalachuris-of-mahishmati. The Chalukyas of Badami were not a state in 510: the batch's own kadamba-empire has them as Kadamba vassals until c. 540. The Vakataka page says the successors were "probably defeated by the Kalachuri of Mahismati". The Harishena page: "The Kalachuris in the north and the Kadambas in the south also seem to have expanded their control over lands formerly under Vakataka sovereignty". kalachuris-of-mahishmati is in the author's counterparts_needing_dossiers. Re-validated.

Blocking, not applied:
1. No vassal pair with gupta-empire. gupta-empire /ledger/13 (390 vassal_start, counterpart vakataka-kingdom) and /ledger/17 (410 vassal_end) have no mirror. The Vakataka page: "Prabhavatigupta (385-405) ruled as a regent on behalf of her two sons" for 20 years.
   Fix: add vassal_start and vassal_end with counterpart gupta-empire, and use one span in both dossiers (390-410 from Chandragupta II, or 385-405 from the Vakataka page).
2. /identity/capitals/0 and /keyframe_review/0-2. Kanchanaka (Nachna, 80.3E 24.4N) is the capital 250-335, but it lies outside every keyframe of those years. The 250 keyframe is Vidarbha. The Cliopatria 260 and 306 shapes (verdict ok) stop at 23.10N (shapes.csv bbox). The Vakataka page says Pravarasena I "certainly ruled from Bundelkhand in the north"; Vyaghradeva of Nachna-Ganj is a vassal 360-385.
   Fix: mark vakataka-kingdom_260 and _306 adjust, with correction = Cliopatria shape plus Bundelkhand (Panna district). Start the Nachna capital at 275, Pravarasena I; the page gives no seat for Vindhyashakti 250-270.

Thin:
- 410 -> 451: +1,199 cells. /ledger/8 covers 1,019 (Gupta land); 180 cells have no event.
- Confidence-1 events: 260 gains, 353 losses, 451/461/490 Malwa moves.
- The Kuntala frontier with the Kadambas.

Spot checks: /ledger/0 confirmed (c. 250; Vindhyashakti r. 250-270); /ledger/7 confirmed; /ledger/11 confirmed ("After his death in 480, his kingdom was probably annexed by Harishena"); /ledger/12 confirmed (Avanti on both pages, year bridged at confidence 1); /ledger/13 confirmed (Harishena page: "very rapidly after Harishena's death in about 510").

Area: the infobox has no area (map caption "circa 350 CE").

## late-pallava-empire: thin

Nothing blocking. Routed:
- /ledger/1 (353 loss of Kanchi, counterpart early-cholas). The early-cholas dossier (sa-02-a) ends in 305 and has no 353 gain. The page is right ("The Cholas drove the Pallavas away from Kanchi in the mid-4th century, in the reign of Vishnugopa"), so either early-cholas is extended or a 4th-century Chola holder gets a dossier. The author explained the gap in the note but did not list it under counterparts_needing_dossiers.

Thin:
- 353 -> 451: 89 -> 140 cells (+67/-16, area +57%) with no event.
- The frontier 353-574.
- 602 loss (confidence 1; Pullalur undated).
- Overlap with Rashtrakuta 806-897 (sa-03 not run).

Spot checks: /ledger/0 confirmed (Established 275; Sivaskandavarman 275-300); /ledger/1 confirmed (mid-4th century; Vishnugopa 350-355); /ledger/3 confirmed (Kalabhra page: "consolidated his kingdom ... up to the Kaveri river by c. 575 CE"); /ledger/5 confirmed (Disestablished 897).

Minor: the capital note quotes the Pallava page as crediting Simhavishnu with "establishing Kanchipuram as a powerful capital". The extract I got does not have that sentence; it may be on the Simhavishnu page. Re-cite it if so.

Area: no infobox area.

## yaudheya-republic: fail

Applied by the reviewer:
- /ledger/0 (200 found): counterpart eastern-kushans -> kushan-empire.
- /identity/predecessors/0: slug -> kushan-empire, land intersect(Kushan Empire 199, Yaudheya 306). That is 818 of the 837 cells.
- Why: eastern-kushans starts in 226, and kushan-empire (30-225) is the Kushan state of 200. The Yaudheya page puts the blow to "the Kushans" at about 180 CE. Re-validated.

Blocking, not applied:
1. No vassal_start with gupta-empire mirroring gupta /ledger/4 (347). Samudragupta page: "They seem to have become Samudragupta's tributaries". The Yaudheya page quotes the Allahabad Pillar: "propitiated with the payment of all tributes".
   Fix: add a 347 vassal_start with counterpart gupta-empire. The 377 dissolve then closes it.

Routed:
- Keyframe yaudheya-republic_200 (200-305) overlaps three neighbours:
  - kushan-empire 200-225: 818 cells
  - eastern-kushans 238-269: 818 cells, keyframes ok
  - western-satraps 270-305: 230 cells
- western-satraps /ledger/11 loses those 230 cells to the Yaudheya in 306, and this dossier has no matching gain.
- The Yaudheya page supports the Yaudheya ("ruling over this territory as an independent power from the beginning of the 3rd century"; "the Kushans ceased to have a presence in the Eastern Punjab"). The cut therefore belongs in kushan-empire, eastern-kushans and western-satraps (sa-02-b/c); if they keep their shapes, this dossier must cut keyframe 200 and add the 306 gain. The author flagged it.

Minor: /wars/0, Rudradaman 145-150, lies before the start (validator warning). Drop it or move it to the notes.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed as bridged (Disestablished "4th century CE", succeeded by the Gupta Empire).

Area: no infobox area.

## kadamba-empire: thin

Nothing blocking. Every keyframe change is explained: 345 core, 353 gains, the 451 and 546 year corrections.

Thin:
- The 353 gains are confidence 1. The page dates Kangavarma's war with the Vakatakas to c. 365.
- The post-510 gains of Vakataka land: Harishena page, and vakataka-kingdom lists kadamba-empire as a successor, but no event exists.
- The 541-554 gap until the Chalukya row starts.
- The keyframe-345 circle overlaps the Vakataka 347 shape by 15 cells (noise).

Spot checks: /ledger/0 confirmed (Established 345; "founded by Mayurasharma in c. 345"); /ledger/1 consistent at confidence 1; /ledger/2 confirmed (Traikutas, Abhiras, Pariyathrakas, Shakasthanas, Maukharis, Punnatas, Sendrakas; the Banas paid tribute); /ledger/3 confirmed ("Around c. 540 the Chalukyas ... conquered the entire kingdom"; Disestablished 540).

Area: no infobox area.

## Cross-dossier matrix (summary)

Matched:
- gupta 347 / western-satraps 347
- gupta 353 / vakataka 353
- gupta 353 / pallava 353
- gupta 378 gain / yaudheya 377 dissolve
- gupta 397-409 contest and 409 gain / western-satraps 397-409
- gupta 445-461 contest / vakataka; gupta 451 loss, 461 gain, 490 loss / vakataka
- gupta 497 contest_start / white-huns 496 (and alchon-huns 496)
- vakataka 260 / western-satraps 260
- vakataka 353 / kadamba 353

Missing:
- vassal pairs gupta-yaudheya 347 and gupta-vakataka 390-410
- gupta gain from eastern-kushans 346/347
- gupta gain from mahameghavahana 350
- alchon-huns 500 gain, 515 loss and 520-534 occupation against gupta
- kadamba gain of Vakataka land after 510

Mismatches:
- gupta 490 loss to white-huns (white-huns takes it from alchon-huns)
- gupta 528 against white-huns 534 contest_end
- pallava 353 loss to early-cholas (ended 305)
- western-satraps 306 loss to yaudheya
- yaudheya keyframe 200-305 against kushan-empire, eastern-kushans and western-satraps

Exceptions (counterpart not written yet or no dossier):
- kamarupa 353, maitraka 476, kalabhra 575, chalukya 602/540, nagas-of-padmavati 347, free-text counterparts.
