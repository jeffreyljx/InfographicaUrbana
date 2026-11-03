# Review of batch sa-02-c (reviewer, 2026-10-19)

Verdicts: kushan-empire **fail**, western-satraps **fail**, eastern-kushans **fix** (fixed by the reviewer), western-kushans **fail**. The machine copy is history/notes/phase-b/reviews/sa-02-c.json.

Mechanical checks: all four validate with --resolve. western-satraps has 2 warnings, from the 55 km2 stub shapes 476 and 480, which are correctly marked wrong. No confidence-3 events; spot checks found no fabricated or mis-dated events.

Pages opened: Kushan Empire, Kanishka, Western Satraps, Rudradaman I, Kushano-Sasanian Kingdom, Chandragupta II.

## Edits the reviewer applied (re-validated)
- kushan-empire /identity/rulers/0: Kujula Kadphises changed from 25-85 to 30-90. The page list has 'c. 50 – c. 90', and the new span closes the 85-90 gap before Vima Takto.
- kushan-empire /identity/rulers/1-5: source Kushan Empire page added.
- kushan-empire /ledger/10: the Champa caveat is on the Kushan Empire page, not the Kanishka page; note and source corrected.
- eastern-kushans /identity/rulers: Kipunada clipped to 346; sources added for rulers 1-6.
- eastern-kushans /ledger/4 note: the page names the Yaudheyas ('Around 270 their territories on the Gangetic plain became independent under local dynasties such as the Yaudheyas').
- western-kushans /identity/rulers/1: Peroz I Kushanshah clipped to 259; source added.

## kushan-empire: fail
1. **Blocking.** The Tarim correction (keyframe_review/4-8) subtracts the Tarim Basin region. That leaves 156 cells (about 39,000 km2) of the 117 strip: the Tian Shan rim, 72.4-86.5 E. They vanish in 184 with no event, because ledger/11 covers only the Kashgar circle. Subtract the strip itself: minus([K117, K91]).
2. The Kashgar circle is added to the directly held shape, but the note calls it a client and ledger/6 makes it a vassal. Leave it out of the corrections, or explain why it is direct land.
3. ledger/2 (51, counterpart nobody, text 'held by no Cliopatria state'): 168 of its 181 cells are Cliopatria's Great Yuan shape of 43. great-yuan.json lists kushan-empire as successor. Make the counterpart great-yuan for those cells and add great-yuan as a predecessor.
4. The Purushapura capital from 30 lies outside the 43 and 51 shapes. The page's Hou Hanshu passage has Kujula take Jibin (Kapisha/Gandhara), and indo-parthians loses Gandhara and Taxila to the Kushans in 50. Either adjust keyframe 51 to add Gandhara, with a gain from indo-parthians, or use Kapisa for 30-90.
5. ledger/9 and /12 (Western Satraps vassalage) have no mirror in western-satraps. The Western Satraps page says 'vassals of the Kushans, at least in the early period'; agree the years and cite that page.

## western-satraps: fail
1. **Blocking.** There is no vassal_start/vassal_end with kushan-empire, although the Western Satraps page ('vassals of the Kushans, at least in the early period') and the Rudradaman page (the Kushans 'were the suzerains of the Western Kshatrapas') both say so, and kushan-empire records it.
2. The 35-42 keyframe overlaps indo-scythians, whose loss to the Satraps is in 43. Agree the year with sa-02-b; the page supports 35.
3. The Ujjain capital from 78 is outside the 43-126 shapes, where Cliopatria gives Ujjain to the Satavahanas. Start it at 127, or adjust keyframes 91 and 106.
4. ledger/2 is dated 130, but the 127 shape already holds the land, and satavahana-dynasty's loss is in 127. Align the keyframe and the event.
5. ledger/5 (224, from satavahana-dynasty): the Satavahanas lost Nasik to the Abhiras in 203 and dissolve to abhira-dynasty, so there is no mirror.
6. satavahana-dynasty's 124 gain of the Nahapana lands from western-satraps has no loss here, because the shapes before 127 lack those lands. Settle this with sa-02-b.

## eastern-kushans: fix (done by the reviewer)
Remaining gap: the end in 346 is Cliopatria's. The pages keep the Kushans in the Punjab under Gupta suzerainty (infobox: 375), and kidarites takes the 'Kushan remnants' only c. 390. Add a Gupta vassal phase, or drop kidarites from successors.

## western-kushans: fail
**Blocking.** There is no vassal_start under the Sasanians. The Kushano-Sasanian page dates the capture to 225 and Ardashir I's dominion to 'around 230', with Sasanian governors as Kushanshahs. Add a vassal_start at 230 with counterpart sasanian-empire and keep the rename. The 259 end is Cliopatria's; reconcile the identity with indo-sasanian-empire (me-06).

## For the orchestrator
- Q25979: the page carries the dynasty without a break to Kipunada (335-350) and gives an end of 375. eastern-kushans could be one dossier with kushan-empire. The author's split is explained; this is your decision.
- kidarites (ia-01) uses the slug kushano-sasanian-kingdom, which has no dossier.
- Unchecked mirrors, because those dossiers are not yet written: sasanian, indo-sasanian, vakataka, gupta, yaudheya, Han, Protectorate of the Western Regions.
