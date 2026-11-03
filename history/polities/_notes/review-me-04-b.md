# Review of batch me-04-b (2026-10-19)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (spot-check budget 4 per dossier; thin judged against the page budget; small verified fixes applied by the reviewer).

Mechanical: all six dossiers validate with 0 errors (--resolve). Warnings: unresolved regions Aeolis, Shephelah, Awsan (gazetteer requests), and the slug-like counterparts awsan and nashshan (listed for me-04-x). Every Cliopatria shape has a verdict. Ledgers are sorted, and the found and dissolve events fall at the start and end years. Each capital lies inside its first shape's bbox, and every family is near-east.

Area: none of the six state articles has an infobox area (reviewer checked each), so no factor-of-two test was possible; every dossier says so.

## Verdicts

### lydia: thin

Validates. Every Cliopatria shape has a verdict. The years are in order and the c3 events are true. Four confidence-1 events carry the largest moves (Troad, Caria, the northern peoples, Ionia), thin within a 5-page budget. Greek mirrors are missing on the greek-city-states side (eu-01).

Findings:
- [non-blocking] `/ledger/10`: The -560 event books the Ionian and Aeolian mainland as a direct gain, but the dossier's own /ledger/13 note quotes the Siege of Sardis page calling these cities 'formerly Lydian tributaries'. Evidence: Siege of Sardis (547 BC) page, as quoted in /ledger/13. The Croesus page has Croesus 'annex' only Ephesus; Smyrna and Colophon fell to Alyattes. Fix: Keep Ephesus, Smyrna and Colophon as gains. Record the rest of Ionia and Aeolis as vassal_start -560 (counterpart greek-city-states), closed by vassal_end -546. Ask eu-01 to mirror it.

Thin (for a gap-filler):
- `/ledger/1`: year and page for Gyges's Troad and Hellespont conquest (confidence 1; -650 is Cliopatria's shape year) (try https://en.wikipedia.org/wiki/Troad)
- `/ledger/2`: date of the Carian alliance or control (confidence 1) (try https://en.wikipedia.org/wiki/Caria)
- `/ledger/4`: a dated page for the Mysian, Bithynian and Paphlagonian conquests (confidence 1) (try https://en.wikipedia.org/wiki/Alyattes_of_Lydia)
- `/ledger/10`: a year for Croesus's subjugation of Ionia and Aeolis (confidence 1) (try https://en.wikipedia.org/wiki/Ionia)

Spot checks:
- `/ledger/3` (https://en.wikipedia.org/wiki/Phrygia): confirmed: 'eventually expelled them by around 620 BC' and 'expanded to incorporate much of Phrygia'. The note gives this as a verbatim quote, but it is a close paraphrase.
- `/ledger/5` (https://en.wikipedia.org/wiki/Lydia): confirmed: infobox 'Lydian-Milesian War: 612-600 BC'
- `/ledger/9` (https://en.wikipedia.org/wiki/Lydia): confirmed: war from 590, 'a solar eclipse occurred in 585 BC during a battle', Halys as the border
- `/ledger/11` (https://en.wikipedia.org/wiki/Lydia): confirmed: 'In 547 BC, the Lydian king Croesus besieged and captured the Persian city of Pteria in Cappadocia'
- `/ledger/13` (https://en.wikipedia.org/wiki/Lydia): confirmed: 'In 546 BC, it became a satrapy of the Achaemenid Empire'; infobox 'Fall to Persia: 546 BC'

### phrygia: thin

Validates. The years and the fall date are honest. Two keyframe jumps have no event; this is thin by design within its 1-2 page budget.

Findings:
- [non-blocking] `/identity/successors/0`: The dossier names lydia as successor (land: Phrygia), but /ledger/3 sends that same land to nobody in -676, and Lydia takes it from nobody only in -620. lydia's predecessors are empty, which is correct, since Lydia arose in -700 on its own land. Evidence: Schema: dissolve sends the land to identity.successors. The phrygia ledger's own -676 loss names counterpart nobody, and lydia /ledger/3 is a -620 gain from nobody. Fix: Empty successors, or keep lydia and say in its note that Lydia took the land in -620, after a stateless interval of 56 years.

Thin (for a gap-filler):
- `/keyframe_review/1`: No ledger event explains the growth from 29,488 to 78,628 km2 in -750, when Midas succeeds c. 740. (try https://en.wikipedia.org/wiki/Midas)
- `/keyframe_review/2`: No ledger event explains the growth from 78,628 to 188,102 km2 in -700. Only the Lydian core is removed, and the page says only 'dominating most of central and western Anatolia'. (try https://en.wikipedia.org/wiki/Gordion)
- `/ledger/0`: founding year (confidence 1, Cliopatria's -900) (try https://en.wikipedia.org/wiki/Phrygians)

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Phrygia): confirmed: 'Phrygia engaged in military conflict with Assyria from 715 BC'
- `/ledger/2` (https://en.wikipedia.org/wiki/Phrygia): confirmed: 'suggests Phrygia had offered its submission and struck a truce by that time'
- `/ledger/3` (https://en.wikipedia.org/wiki/Phrygia): confirmed: 'about 695 BC (according to Eusebius) or 676 BC (according to Julius Africanus)'; infobox 'Fall to the Cimmerians: 675 BC'
- `/keyframe_review/2` (https://en.wikipedia.org/wiki/Phrygia): confirmed as far as the page goes: 'dominating most of central and western Anatolia'; the page says nothing of the Aegean coast

### tabal-kingdom: fail

Every dated event is true, but the c. 738-713 tributary relation that the dossier's own page states has no vassal pair in either ledger.

Findings:
- [blocking] `/ledger`: The ledger has no vassal_start or vassal_end for Tabal's subjection to Assyria, which ran c. 738/740 to 713. neo-assyrian-empire has no such pair either. Evidence: Tabal (state) page, the dossier's own source: infobox 'Submission to the Neo-Assyrian Empire: c. 740 BC'; text 'By c. 738 BC, the Tabalian region, including Tabal proper, had become a tributary of the Neo-Assyrian king'. /wars/0 note says 'Tabal as a tributary is the Neo-Assyrian dossier's vassal_start', but the reviewer brief requires the pair in both ledgers (precedent: me-04-a review, phoenicia). Fix: Add vassal_start -738 (counterpart neo-assyrian-empire, region: the tabal-kingdom shape, confidence 2) and vassal_end -713, citing the annexation. Ask me-02 to add the mirror with counterpart tabal-kingdom. The 837/836 tribute may be noted in /wars/0 only.
- [non-blocking] `/keyframe_review/0`: The verdict is ok, but the note says the shape reaches Cilicia and Malatya, far beyond the Kayseri-Nevsehir-Nigde land the page gives. Evidence: Tabal (state) page: 'covered the areas surrounding what is presently the city of Kayseri', 'in the modern Turkish provinces of Kayseri, Nevsehir, and Nigde'. Fix: Set the verdict to adjust, with the correction = the /ledger/0 admin1 union (text from the page), or say in the note why the wider Tabalian region is kept.

Thin (for a gap-filler):
- `/ledger/0`: founding year (confidence 1); nothing dated before 837 (try https://en.wikipedia.org/wiki/Shalmaneser_III)

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Tabal_(state)): confirmed: infobox 'Reorganisation into Bit-Burutas: c. 718 BC'
- `/ledger/2` (https://en.wikipedia.org/wiki/Tabal_(state)): confirmed: 'deported Ambaris, his family and his chief courtiers to Assyria in 713 BCE'; infobox 'Annexation by the Neo-Assyrian Empire: 713 BC'
- `/ledger/3` (https://en.wikipedia.org/wiki/Tabal_(state)): confirmed (annexed and made a province)
- `/wars/1` (https://en.wikipedia.org/wiki/Tabal_(state)): confirmed: tributary by c. 738, Wasusarmas deposed c. 732-730; this tributary status is the missing vassal pair

### kingdom-of-judah: fail

All c3 events are true. The Assyrian, Egyptian and Babylonian vassal relations are missing from the ledger, although the dossier's own page states them and neo-babylonian-empire records its pair.

Findings:
- [blocking] `/ledger`: No vassal_start or vassal_end mirrors neo-babylonian-empire /ledger/5 (-597 vassal_start, counterpart kingdom-of-judah) and /ledger/6 (-587 vassal_end). Evidence: The Kingdom of Judah page: after Carchemish (605) 'Jehoiakim changed allegiances to pay tribute to Nebuchadnezzar II of Babylon'; Zedekiah 'made a tributary of Babylon'. The author's notes say overlordships belong to the suzerains only, but the reviewer brief requires the pair in both ledgers (precedent: me-04-a, philistia and kingdom-of-israel). Fix: Add vassal_start (counterpart neo-babylonian-empire) at -605 or -597, aligned with neo-babylonian-empire (the page gives 605 for the tribute), and vassal_end -587/-586 at the fall.
- [blocking] `/ledger`: No vassal pair for the Assyrian overlordship. neo-assyrian-empire /ledger/13 (-734 vassal_start) and /ledger/57 (-609 vassal_end) name the counterpart in free text, 'Judah, Edom, Moab and Ammon'. Evidence: The Kingdom of Judah page: 'Judah was a vassal of Assyrian rulers: Sennacherib and his successors'. The /keyframe_review/4 note says Judah paid tribute to Assyria under Manasseh. Fix: Add vassal_start -734 (counterpart neo-assyrian-empire) and vassal_end -609. Ask me-02 to put the slug kingdom-of-judah in its counterpart.
- [blocking] `/ledger`: No vassal pair for Egypt's overlordship of 609-605. twenty-sixth-dynasty-of-egypt has none either. Evidence: The Kingdom of Judah page: 'Jehoiakim ruled originally as a vassal of the Egyptians by paying a heavy tribute'; 'Necho imposed on Judah a levy of a hundred talents of silver' (609). Fix: Add vassal_start -609 / vassal_end -605 (counterpart twenty-sixth-dynasty-of-egypt). Ask the Egyptian dossier's group to mirror it.
- [non-blocking] `/ledger/3`: The note says no page reports a Judean gain, but the Judah page gives one in the 9th or 8th century. philistia has no -800 loss to mirror the gain. Evidence: The Kingdom of Judah page: some Shephelah sites 'became under influence of Judah later during the 9th or 8th centurty BCE'. philistia's ledger has no -800 event with counterpart kingdom-of-judah. Fix: Cite that sentence. Keep confidence 1 or raise it to 2 with the Shephelah named in the text. Ask the me-04-a author to add the mirror loss to philistia, or drop the gain if philistia's shape does not cede the cells.

Thin (for a gap-filler):
- `/ledger/2`: end of the Israel-Judah war (confidence 1, Rehoboam's death) (try https://en.wikipedia.org/wiki/Abijah_of_Judah)
- `/ledger/3`: the Judean westward gain c. 800 (Amaziah/Uzziah) (try https://en.wikipedia.org/wiki/Uzziah)

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Kingdom_of_Judah): confirmed: 'After the death of Solomon circa 930 BCE', ten tribes rebelled against Rehoboam
- `/ledger/4` (https://en.wikipedia.org/wiki/Siege_of_Jerusalem_(701_BC)): confirmed: 'give the surrounding towns to Assyrian vassal rulers in Ekron, Gaza and Ashdod'; 46 cities destroyed (the page names no towns, so confidence 2 is right)
- `/ledger/5` (https://en.wikipedia.org/wiki/Kingdom_of_Judah): confirmed: 'In 589 BCE, Nebuchadnezzar II returned to Judah and again besieged Jerusalem'
- `/ledger/7` (https://en.wikipedia.org/wiki/Kingdom_of_Judah): confirmed: 'capture of Jerusalem in 586 BCE' (the page also says 587; neo-babylonian-empire uses 587, which is within one year)

### sabaeans: fix

Strong dossier: every spot-checked event says what its note claims. One keyframe/ledger contradiction was fixed by the reviewer. The Aksum mismatch is routed to af-01, and the Himyar overlaps to me-06.

Findings:
- [APPLIED by reviewer] `/keyframe_review/13`: sabaeans_-25 (-25..-20, 28,196 km2) was marked ok, while /ledger/15 merges all of Saba into Himyar in -25. The two contradicted each other for -24..-20. Evidence: Himyarite Kingdom page: 'The kingdom conquered neighbouring Saba' in c. 25 BCE (for the first time)'. The keyframe's own note says the ledger puts the absorption in -25. Fix: Verdict adjust, correction {cliopatria: Sabaeans, year: -25, text: 'Unchanged shape, held to -25 instead of -20 ...'}, plus a reviewer sentence in the note. Applied and re-validated (0 errors).
- [non-blocking] `/ledger/5`: /ledger/5 and /ledger/6 give the same whole region, Awsan, to two counterparts (qataban and hadhramaut) in the same year, so the renderer cannot split it. Evidence: Awsan page: Saba 'divided the territory between two of its other allies at the time', with no shares. Hadhramaut /ledger/1 takes the whole of Awsan. Fix: Give each share a region, Qataban's west (Wadi Markha, Bayhan side) and Hadhramaut's east. Or keep one counterpart and say in the note that the split is unknown.
- [non-blocking] `/ledger/11`: The -110 rename to 'Saba and Dhu-Raydan' conflicts with the Himyarite Kingdom page, on which Himyar is an independent kingdom after 110 and first conquers Saba c. 25 BCE. The title is the one Himyar's kings bore. Evidence: Qataban page: Himyar 'seceded from it around 110 BCE' and 'joined Saba' to form the kingdom of Saba and Dhu-Raydan' (confirmed). Himyarite Kingdom page: 'afterward, it was recognized as an independent kingdom'. Fix: Leave this to me-06 to reconcile. If the himyarite-kingdom dossier keeps Himyar separate in -110..-26, drop the rename or move it into the note.

Thin (for a gap-filler):
- `/ledger/3`: a year and a page for the Hadhramaut vassalage start (confidence 1). The Awsan page calls Hadhramaut an ally. hadhramaut has no mirror (see the hadhramaut verdict). (try https://en.wikipedia.org/wiki/Karib%27il_Watar)
- `/ledger/9`: date of the loss of the Jawf and Najran to Ma'in (confidence 1, Cliopatria's -383) (try https://en.wikipedia.org/wiki/Minaeans)
- `/ledger/19`: the 238-246 loss to Aksum rests on shapes only (confidence 1). kingdom-of-axum records it as occupation of himyarite-kingdom land, 200-275. (try https://en.wikipedia.org/wiki/GDRT)
- `/ledger/0`: founding year (confidence 1, Cliopatria's -800; infobox '~1000-800 BCE') (try https://en.wikipedia.org/wiki/Mukarrib)

Spot checks:
- `/ledger/2` (https://en.wikipedia.org/wiki/Sabaeans): confirmed: Karib'il extended Sabaean control to Najran; reign 'late 8th and early 7th centuries BCE'
- `/ledger/4` (https://en.wikipedia.org/wiki/Awsan): confirmed: alliance in the 8th century, rivalry and obliteration under Karib'il Watar in the late 7th century; territory divided between two allies
- `/ledger/7` (https://en.wikipedia.org/wiki/Qataban): confirmed: 'During the 6th century BCE, Qataban had come under the control of Saba'
- `/ledger/8` (https://en.wikipedia.org/wiki/Qataban): confirmed: 'Qataban regained its independence in the late 5th century BCE'
- `/ledger/12` (https://en.wikipedia.org/wiki/History_of_Yemen): confirmed: 'The Sabaeans regained their control over Ma'in after the collapse of Qataban in 50 BC'
- `/ledger/15` (https://en.wikipedia.org/wiki/Himyarite_Kingdom): confirmed: c. 25 BCE, for the first time
- `/ledger/16` (https://en.wikipedia.org/wiki/Sabaeans): confirmed: 'liberating itself from Himyar by around 100 CE'
- `/ledger/21` (https://en.wikipedia.org/wiki/Sabaeans): confirmed: 'finally permanently conquered by the Himyarites around 275 CE'

### hadhramaut: fail

Every event is true, but the Sabaean vassal pair, written by the same author, has no mirror here.

Findings:
- [blocking] `/ledger`: No vassal_start or vassal_end mirrors sabaeans /ledger/3 (-675 vassal_start, counterpart hadhramaut) and /ledger/10 (-330 vassal_end). The /keyframe_review/1 note quotes the independence sentence, but the ledger has no event for it. Evidence: Hadhramaut page: 'Hadhramaut became independent from Sheba in c. 330 BCE'. Sabaeans page: 'Karib'il conquered all surrounding neighbours, including the Awsan, Qataban, and Hadhramaut'. Both dossiers are by the same author in this batch. Fix: Add vassal_start -675 (counterpart sabaeans, confidence 1) and vassal_end -330 (confidence 2, Hadhramaut page). Alternatively, if the author judges the vassalage unproven, as the Awsan page's 'allies' suggests, remove the pair from sabaeans. Either way the two ledgers must agree.

Thin (for a gap-filler):
- `/ledger/2`: date of the Qataban annexation (confidence 1, Cliopatria's 184; Qataban page: late 1st century CE; Himyar page: c. 200) (try https://en.wikipedia.org/wiki/Shabwa)
- `/wars/0`: zones are empty; say 'no ground changed hands' or name the zone of the 1st-century-BCE coalition war (try https://en.wikipedia.org/wiki/Qataban)

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Hadhramaut): confirmed: 'established in the early 1st millennium BCE'; Surwah inscription c. 700-680 BCE
- `/ledger/1` (https://en.wikipedia.org/wiki/Awsan): confirmed: late 7th century; division between two allies (no shares)
- `/ledger/3` (https://en.wikipedia.org/wiki/Himyarite_Kingdom): confirmed: 'Hadramaut c. 300 CE'; 'By 300, the Himyarite Kingdom had vanquished ...'
- `/ledger/4` (https://en.wikipedia.org/wiki/Hadhramaut): confirmed: 'ceased to exist by the end of the 3rd century CE, having been annexed by the Himyarite Kingdom'

## Cross-dossier matrix

- lydia -650 gain (nobody) <-> -: **exception**. counterpart nobody
- lydia -650 gain (Carian dynasts (Mylasa, Pedasa)) <-> -: **exception**. listed in counterparts_needing_dossiers (caria)
- lydia -620 gain (nobody) <-> -: **exception**. Phrygia land stateless since -676 (phrygia /ledger/3 loss to nobody)
- lydia -620 gain (nobody) <-> -: **exception**. Mysia, Bithynia, Paphlagonia; counterpart nobody
- lydia -600 gain (greek-city-states) <-> greek-city-states None loss: **missing**. greek-city-states (eu-01) has no -600 loss of Smyrna to lydia; route to eu-01
- lydia -560 gain (greek-city-states) <-> greek-city-states -547 loss: **mismatch**. greek-city-states /ledger/12 loses Ionia to achaemenid-empire in -547 and never to lydia, so Ionia is double-booked in -560..-547. eu-01 should add a -560 loss or vassal_start to lydia and change its -547 loss counterpart; lydia should consider a vassal pair (see its fixes)
- lydia -546 loss (achaemenid-empire) <-> -: **exception**. achaemenid-empire (me-05) no dossier yet; owned by a group that has not run yet
- phrygia -676 loss (nobody) <-> -: **exception**. counterpart nobody (Cimmerian sack)
- tabal-kingdom -713 loss (neo-assyrian-empire) <-> neo-assyrian-empire -713 gain: **matched**. neo-assyrian-empire /ledger/24 (confidence 2 there, 3 here)
- tabal-kingdom -738 vassal_start (missing) (neo-assyrian-empire) <-> -: **missing**. neither ledger has the c. 738/740-713 tributary pair stated by the Tabal (state) page; tabal-kingdom (me-04-b) and neo-assyrian-empire (me-02) both to add
- kingdom-of-judah -930 found (kingdom-of-israel) <-> kingdom-of-israel -930 split: **matched**. kingdom-of-israel /ledger/9
- kingdom-of-judah -800 gain (philistia) <-> philistia None loss: **missing**. philistia (me-04-a) has no -800 loss to kingdom-of-judah; judah gain is confidence 1
- kingdom-of-judah -701 loss (philistia) <-> philistia -701 gain: **matched**. philistia /ledger/12
- kingdom-of-judah -586 loss (neo-babylonian-empire) <-> neo-babylonian-empire -587 gain: **matched**. one year apart (neo-babylonian-empire /ledger/7, 587); the Judah page gives both 587 and 586; align if convenient
- neo-babylonian-empire -597 vassal_start (kingdom-of-judah) <-> kingdom-of-judah None vassal_start: **missing**. kingdom-of-judah has no vassal_start (blocking fix in its verdict)
- neo-babylonian-empire -587 vassal_end (kingdom-of-judah) <-> kingdom-of-judah None vassal_end: **missing**. kingdom-of-judah has no vassal_end
- neo-assyrian-empire -734 vassal_start (Judah, Edom, Moab and Ammon) <-> kingdom-of-judah None vassal_start: **missing**. the Assyrian counterpart is free text (me-02 should use slug kingdom-of-judah); judah has no mirror
- neo-assyrian-empire -609 vassal_end (Judah, Edom, Moab and Ammon) <-> kingdom-of-judah None vassal_end: **missing**. as above
- kingdom-of-judah -609 vassal_start (missing) (twenty-sixth-dynasty-of-egypt) <-> -: **missing**. Egyptian overlordship 609-605 (Kingdom of Judah page) in neither ledger
- sabaeans -675 gain (nashshan) <-> -: **exception**. listed in counterparts_needing_dossiers (me-04-x)
- sabaeans -675 gain (nobody) <-> -: **exception**. Najran, counterpart nobody
- sabaeans -675 vassal_start (hadhramaut) <-> hadhramaut None vassal_start: **missing**. same batch; hadhramaut has no vassal events (blocking fix in hadhramaut)
- sabaeans -625 gain (awsan) <-> -: **exception**. listed in counterparts_needing_dossiers (me-04-x)
- sabaeans -625 loss (qataban) <-> -: **exception**. qataban (me-04 sibling part) not yet written
- sabaeans -625 loss (hadhramaut) <-> hadhramaut -625 gain: **matched**. hadhramaut /ledger/1; both give the whole region Awsan, as qataban will (see sabaeans fixes)
- sabaeans -550 gain (qataban) <-> -: **exception**. qataban not yet written
- sabaeans -420 loss (qataban) <-> -: **exception**. qataban not yet written
- sabaeans -383 loss (minaeans) <-> -: **exception**. minaeans (me-04 sibling part) not yet written
- sabaeans -330 vassal_end (hadhramaut) <-> hadhramaut None vassal_end: **missing**. same batch; hadhramaut has none
- sabaeans -50 gain (minaeans) <-> -: **exception**. minaeans not yet written
- sabaeans -25 merge (himyarite-kingdom) <-> -: **exception**. himyarite-kingdom (me-06) no dossier yet; owned by a group that has not run yet
- sabaeans 100 gain (himyarite-kingdom) <-> -: **exception**. me-06 not run
- sabaeans 238 loss (kingdom-of-axum) <-> kingdom-of-axum 200 occupation_start: **mismatch**. kingdom-of-axum (af-01) /ledger/1-2 occupy himyarite-kingdom land (Hudaydah, Hajjah, Taizz, Ibb, Dhamar) 200-275 at confidence 1 and name no Sabaean land; sabaeans loses the Najran/Tihama side 238 and regains it 247 (confidence 1, from shapes). Route to af-01 and me-06 to agree on whose land Aksum held
- sabaeans 247 gain (kingdom-of-axum) <-> kingdom-of-axum None loss: **mismatch**. as above; no Axum event in 247
- sabaeans 275 loss (himyarite-kingdom) <-> -: **exception**. me-06 not run
- hadhramaut 184 gain (qataban) <-> -: **exception**. qataban not yet written
- hadhramaut 300 loss (himyarite-kingdom) <-> -: **exception**. me-06 not run

## Problems and routing

- No page failed for the reviewer. None of the six state articles has an infobox area, so area_check carries null figures; each dossier acknowledges this.
- qataban, minaeans (me-04 sibling parts), himyarite-kingdom (me-06), achaemenid-empire (me-05), kingdom-of-urartu (eu-19) and roman-empire (eu-04) have no dossier yet; their mirrors are counted as exceptions.
- Routed to other groups: greek-city-states (eu-01) lacks the Lydian conquests of Smyrna (600) and Ionia (560) and loses Ionia straight to Persia in 547; kingdom-of-axum (af-01) records its 3rd-century Arabian holdings as occupation of himyarite-kingdom land, not Sabaean; neo-assyrian-empire (me-02) lacks the Tabal tributary pair and names Judah in free text; neo-babylonian-empire gain 587 vs Judah 586 (within a year, matched); philistia (me-04-a) lacks a -800 loss to kingdom-of-judah; twenty-sixth-dynasty-of-egypt lacks the 609-605 Judah vassalage.
- Reviewer edit: history/polities/sabaeans.json /keyframe_review/13 verdict ok -> adjust (held to -25), re-validated 0 errors, read back after the write.
