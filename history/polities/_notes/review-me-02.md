# Review: batch me-02 (Babylon and Assyria), 2026-10-18

Adversarial review of the twelve me-02 dossiers. Machine copy: `history/notes/phase-b/reviews/me-02.json`.

Verdicts: assyria **thin**, babylonia **thin**, first-sealand-dynasty **pass**, neo-assyrian-empire **fail**, assyrian-egypt **pass**, neo-babylonian-empire **thin**, eshnunna **thin**, lim-dynasty-of-mari **fix** (fixed by the reviewer), sin-kashid-dynasty-of-uruk **pass**, bit-adini **pass**, bit-bahiani **pass**, bit-yakin **thin**.

How the verdicts are used here: `fix` means the reviewer applied every blocking fix and only non-blocking notes remain; `thin` means valid and honest, with gaps (unexplained keyframe changes, confidence-1 events, non-blocking fixes) for a gap-filler or the author; `fail` means at least one unapplied blocking finding. Vassal ties are booked on the suzerain only (the schema defines `vassal_*` from the suzerain's side, with the vassal as counterpart), so a missing vassal-side mirror is recorded in the matrix as an exception and is not a fault.

## Mechanical checks

`validate_dossier.py --resolve` on all twelve: 0 errors, 0 warnings, before and after the reviewer's edits. File names equal slugs; the six Cliopatria names match `polities.csv`; every Cliopatria shape has a verdict. The known problems in data/README.md (Assyria and Babylonia long spans; Assyria's Wikidata Q41137 shared with Syria) are handled in the notes.

## Fixes applied by the reviewer (all re-validated)

1. **assyria /ledger/6** (-1776 loss): counterpart `eshnunna` changed to `coalition of Mari, Andarig and Eshnunna`. The Shamshi-Adad I page: the rest of the kingdom was lost "first to a coalition of Mari, Andarig, and Eshnunna"; eshnunna books no gain in -1776 (its land reaches Assur only in -1772).
2. **neo-assyrian-empire /ledger/24** (Tabal, was /ledger/26): year -700 changed to -713, confidence 1 to 2, note rewritten. The note said neither page gives an annexation, but the Sargon II page has "In 713 Sargon campaigned against Tabal in southern Anatolia again ... Sargon deposed Ambaris, deporting him to Assyria, and annexed Tabal." The ledger was re-sorted, so NAE pointers from /ledger/24 to /ledger/26 have moved by one (pointers below are to the file as it stands now).
3. **neo-assyrian-empire /ledger/26** (Cyprus -709): confidence 3 to 2, and the note now quotes the page. The cited Sargon II page says only that "the campaign resulted in several Cypriote rulers paying tribute to Sargon" (tribute); the NAE page says "Cyprus was thus absorbed". The pages disagree.
4. **lim-dynasty-of-mari /keyframe_review/1**: `to` changed from -1771 to -1772. It overlapped /keyframe_review/2, which starts in -1771.

## neo-assyrian-empire: fail (back to the author)

Blocking:

- **Urartu is inside the empire, unflagged** (/keyframe_review/4 -700 `ok`, /5 -675 and /6 -655 corrections). Cliopatria has no Urartu shape from -700 to -616, and the Neo-Assyrian -700 and -675 shapes swallow it: 632 of the 632 H3 cells of `kingdom-of-urartu_-750` (about 160,000 km2) lie inside them. Urartu was never annexed. The Urartu page says Rusa I was "crushingly defeated by Sargon II at Lake Urmia", then Argishti II (714-685) "restored Urartu's position" and Rusa II (685-645) and Sarduri III followed, until the Medes took Van c. 590. The Sargon II page says the 714 campaign "put an end to direct confrontations" but nothing of annexation; the NAE page says "Urartu was not decisively beaten" (774). Fix: make -700 `adjust`, and subtract `{"cliopatria": "Kingdom of Urartu", "year": -750}` in the -700, -675 and -655 corrections. This also explains most of the -655 to -615 drop, about 235,000 km2 lost outside Egypt and Babylonia (mostly 38-41 N, 38-46 E).
- **Egypt: the ledger never gives back the Delta** (/ledger/31, /33, /36 gains of "Memphis and the Delta" from kingdom-of-kush; /35 vassal_start assyrian-egypt -664; /38 vassal_end -655). The -663 gain makes Lower Egypt direct Assyrian land in the same years that assyrian-egypt holds it as a vassal. At -655 only the vassal tie ends, so in the ledger the Delta stays Assyrian after -655, against /keyframe_review/6. Fix: give the Delta to the vassal from -664 (a loss to assyrian-egypt in -664, or recast /36 as the contest end), or add a -655 loss.

Non-blocking:

- **/ledger/39 -653 loss of Babylonia** (confidence 1, "no page dates the end of direct Assyrian rule") is wrong on the Ashurbanipal page, which is already in sources: "The two brothers jointly ascended to their respective thrones after Esarhaddon's death in 669"; "Shamash-shum-ukin was somewhat belatedly crowned king of Babylon in the spring of the next year"; "Shamash-shum-ukin was relegated to being Ashurbanipal's closely monitored vassal". Fix (with babylonia /ledger/22): Babylonia becomes Assyria's vassal in -668 (loss plus vassal_start babylonia -668), vassal_end at the -652 revolt, and the existing -648 vassal_start. Babylonia needs a keyframe for -668 to -651.
- **The Levant and the west, -615 to -612.** /keyframe_review/7 (-615, Cliopatria, with the Levant to 28 N) is followed by /8 (-612, a Harran circle). The ledger loses only Assur (-614) and the heartland (-612); the Levant and Syria have no event until neo-babylonian-empire /ledger/3 gains them in -609. Book their loss: Egypt (twenty-sixth-dynasty-of-egypt, me-03) held the Levant 609-605. Or keep them in /8 until -609.
- **-626 to -620.** /ledger/43 ends the Babylonian vassal tie in -626, but Nabopolassar held only Babylon and Nippur until 620 (Babylonia page: "In 620 BC Nabopolassar seized control over much of Babylonia"). neo-babylonian-empire /ledger/1 gains it from this state in -620 with no mirror here. Add a -620 loss (or a contest from -626 to -620).
- **Elam** (elam /ledger/28-31, me-01) books an Assyrian occupation of Susa from -653, an annexation of Susiana from -640, and a return in -612. This dossier has no mirror. The Ashurbanipal page says "Ashurbanipal did not annex Elam, instead leaving it to its own devices" and has Susa plundered on the way back from the 646 campaign; the NAE page says he "chose to not annex and integrate Elam". Recommended: elam drops the -640 to -612 annexation and closes the occupation by about -646. If a short occupation stays, NAE books the same occupation_start and occupation_end.
- The Cyprus loss is never booked (eight thousand km2 leave between -675 and -615), and Tabal's later fate is not on the pages.

Spot checks, all confirmed on the page: /ledger/4 Bit Adini 857/856 (NAE page), /8 Damascus tribute 773 (NAE), /9 Arpad 740, /11 Hama vassal, /12 Gaza 734, /15 Damascus annexed 732, /17 Babylon 729 (Tiglath-Pileser III), /22 Hama annexed 720, /25 Babylon 710 (Sargon II), /46 Nineveh 612, /48 Harran 609 (NAE). Mis-dated: /24 Tabal (fixed). Type disputed: /26 Cyprus (confidence lowered). Area: infobox 1,400,000 km2 for 670 against Cliopatria -675 at 1,400,726 (ratio 1.00), acknowledged in /keyframe_review/5. Once Upper Egypt and Urartu are removed, the drawn -675 shape is roughly 1.0-1.1 million km2, still within a factor of two.

## babylonia: thin

- **Unexplained loss, -1400 to -1300** (/keyframe_review/9 to /10): 226,484 km2 to 155,212 km2. The lost 68,500 km2 is the middle Euphrates and the land between the rivers north of Baghdad (32.7-35.5 N, 40.2-44.5 E). 271 of its 272 cells lie in Cliopatria's Assyria -1300 shape. No event explains it on either side. The Kurigalzu II page has the Sugagi war with Enlil-nirari and the division of "the districts from Šasili of Subartu, to Karduniaš into two", but no year (Kurigalzu II c. 1332-1308). Fix: a loss to assyria c. -1320 (confidence 1-2), region `minus(Babylonia -1400, Babylonia -1300)`, mirrored by an assyria gain. Pages to try: Adad-nirari I, Enlil-nirari, Synchronistic History.
- **Unexplained loss, -1300 to -1240** (/10 to /11): 20,900 km2 east of the Tigris (33.1-34.8 N, 44.2-47.4 E), with no event.
- **/ledger/22 -653 gain** (confidence 1): mis-dated. The Ashurbanipal page has Shamash-shum-ukin crowned in spring 668 as Ashurbanipal's vassal (see the NAE section). This needs a new keyframe for -668 to -651 and vassal events, so it is left to the author. The existing -653 date also has no keyframe for -653 to -651.
- **Bit-Yakin overlap**: Bit-Yakin's land (Cliopatria First Sealand -1700, 33 cells) lies wholly inside Babylonia's -900 shape, which /keyframe_review/17, /18 and /19 use through -711. Neither dossier books the split. Either subtract it from those keyframes or book a loss to bit-yakin.
- /identity/predecessors/0 `akkadian-empire` (from the infobox) is 260 years earlier and is not in akkadian-empire's successors. Use the state that held Babylon before 1894 (Isin or Larsa, me-01), or note the infobox reading.
- Confidence-1 events: /8, /9, /12, /14, /16, /17, /18, /22.
- Spot checks, confirmed: /0 1894 (Babylonia), /3 Larsa c. 1763 (Hammurabi), /6 Mut-Ashkur tribute c. 1751 (Babylonia), /13 Kurigalzu I mid-14th century (Kassites; Kurigalzu II page: "this now tends to be assigned to the earlier king of this name"), /15 1155 Shutruk-Nakhunte (Babylonia), /19 729 (Babylonia), /1-/2 Larsa 1764 and the six-month siege (Rim-Sin I).

## assyria: thin

- Applied fix 1 (above).
- **Missing gain from Babylonia c. -1320/-1300.** /ledger/15 (-1300) names only Hasaka, but the -1300 shape also holds the 68,500 km2 that Babylonia loses (see above).
- Confidence-1 events: /4, /10, /11, /12, /15, /16, /17, /21, /24. Pages not opened: Shalmaneser I, Adad-nirari I, Tukulti-Ninurta I, Ashur-dan II. The Mitanni vassalage (c. 1430-1360, Old Assyrian page) belongs to mitanni (me-04).
- Spot checks, confirmed: /1 c. 1808 (Assyria), /5 Mari c. 1796 (Shamshi-Adad I), /8 c. 1772 (Old Assyrian period), /18 vassal c. 1225-1216 (Assyria), /23 1055-935 decline (Middle Assyrian Empire). /16: the "formally annexed" sentence is on the Assyria page without a year (confidence 1 is honest). There is no infobox area on Assyria or Middle Assyrian Empire.

## neo-babylonian-empire: thin

- **/ledger/3 (-609) and /keyframe_review/2 disagree.** /3 gains "Harran ... and the Levant" in -609, but /keyframe_review/2 (-612..-606) is Babylonia plus Assyria only, and the Levant appears only with /keyframe_review/3 at -605. The page says "Babylon took Transpotamia (the countries west of the Euphrates) and the Levant" but gives no year; Egypt "continued the war against Babylon for a few more years". Fix: either a new keyframe from -609 with Harran and the Levant, or move the Levant to a -605 gain (after Carchemish).
- /ledger/1 (-620) has no NAE mirror (see the NAE section).
- Confidence-1 events: /9 Tayma, /10 the -550 shrinkage (135,000 km2 in south-east Turkey), /11.
- Spot checks, confirmed: /0 626 and the November coronation, /7 587 (NAE page; the Nebuchadnezzar page says 586), /8 Tyre 573 with vassal kings, /12 12 October 539 (Neo-Babylonian Empire page), /4 Ashkelon 604 plundered and levelled (Nebuchadnezzar II). Area: infobox 500,000 km2 for 562 against Cliopatria -600 at 703,406 km2 (ratio 1.41), acknowledged in /keyframe_review/4.

## eshnunna: thin

- /identity/rulers/4: Silli-Sin runs to -1756, past the dissolve at -1762, and his page row has a "Treaty with Hammurabi, in year 4 of reign" (c. 1761). Either Eshnunna outlived the 1762 occupation as a vassal (extend the end) or truncate the ruler and say why. The rulers list also has gaps.
- Confidence-1 events: /1, /6, /13, /14. Not mapped: Iluni's revolt, Mankisum.
- Spot checks, confirmed: /0 2026 (Eshnunna), /5 Arrapha "starting around 1828" (Ipiq-Adad II), /4 Shaduppum 1857 plus the second confrontation two years later (Ipiq-Adad II), /9 Shubut-Enlil c. 1772 (Old Assyrian period), /16 1762 Hammurabi year 31 (Eshnunna), /10-/11 Mari-Eshnunna war 1772-1770 (Zimri-Lim).

## lim-dynasty-of-mari: fix (fixed by the reviewer)

- Applied fix 4.
- Non-blocking: /identity/capitals/0 keeps Mari from -1830 to -1761 continuously, but -1796 to -1777 has no keyframe: Mari was Yasmah-Adad's (assyria /ledger/5). Split the capital entry or note the exile.
- Spot checks, confirmed: /0 c. 1830, /2 Yahdun-Lim c. 1798 and the annexation, /3 c. 1776, /7 c. 1771, /9 c. 1761 (Mari, Syria); /6 and /8 1772-1770 (Zimri-Lim).

## bit-yakin: thin

- Start (-852) and end (-694) are confidence 1 by design. The page dates no founding and no annexation (Bit Yakin: "Babylon and Chaldea remained peacefully under direct Assyrian control" after Esarhaddon).
- Its land is double-claimed with babylonia (see the babylonia section). /ledger/0 counterpart `nobody` should be `babylonia`, with a mirror, or babylonia's keyframes should subtract the land.
- neo-assyrian-empire /ledger/25 (-710) gains `clio:Babylonia@-900`, which already holds this land, and /27 (-694) gains it again from bit-yakin.

## Passed

- **first-sealand-dynasty**: /0 checked ("very speculatively c. 1732-1475 BC"; Ilum-ma-ilī "the founder"); /1 1460 (Kassites); the pottery and Nippur claims in /keyframe_review/1 are on the page. Mirrors with babylonia match. Two events is within the 1-2 page budget.
- **assyrian-egypt**: /0 664 vassal king, /1 656 Thebes, /2 c. 655 independence, all on Assyrian conquest of Egypt. The wrong verdicts on Cliopatria's -650 and -630 rows are argued from cell counts. The Kush mirror matches. The NAE double booking is NAE's fault.
- **sin-kashid-dynasty-of-uruk**: /0 c. 1865 and the Larsa sentence (Sîn-kāšid), /1 c. 1801 (Rim-Sin I). Mirrors are larsa's to fix (me-01).
- **bit-adini**: /0 c. 1000 (infobox), /1 856-5 (Bit Adini; NAE page 857/856). The Qarqar 853 anomaly is flagged by the author.
- **bit-bahiani**: /0 c. 1200, /1 808 (Bit Bahiani infobox; Tell Halaf). The capital from -1000 rests on the Tell Halaf page's "10th century". The NAE /ledger/2 -894 tribute is on Tell Halaf ("a tributary Aramaean city-state").

## Cross-dossier conflicts to route

- **me-01 elam**: -1158 gain of babylonia → -1155 (the Babylonia page dates the conquest to 1155; the Hammurabi page has a 1158 *raid*). -1320/-1319 occupation (Kurigalzu II) → -1350/-1349 (Kurigalzu I, per the Kurigalzu II page). Counterpart `Eshnunna` → slug `eshnunna`, with -1760 → -1764 (or argue it). The -640 to -612 annexation of Susiana is contradicted by Ashurbanipal and NAE.
- **me-01 third-dynasty-of-ur**: loss of `Eshnunna` (text) -2020 → slug `eshnunna`, -2026 (Eshnunna page: "in 2026 BC got rid of the Ur III calendar"). Book the loss of Assur c. -2025 (assyria /ledger/0).
- **me-01 larsa**: add a loss of Uruk to `sin-kashid-dynasty-of-uruk` c. -1865, and re-point /ledger/7's counterpart to that slug.
- **eu-01 greek-city-states**: /ledger/3 Cyprus -700 → -709 (Sargon II: expedition in 709, Cypriot rulers paying tribute; NAE: "Cyprus was thus absorbed"). Consider booking it as tribute.
- **me-03, me-04, me-05, eu-19**: mirrors listed in the matrix (Judah, Philistia, Tyre, Israel, Tabal, Mitanni, Media, the Achaemenids, Egypt 26, Urartu). For eu-19, Urartu must cover -700 to -616, where Cliopatria has no shape.

## Pages that did not answer

None failed to load. Pages read: Assyria, Shamshi-Adad I, Old Assyrian period, Middle Assyrian Empire, Babylonia, Kurigalzu II, Kassites, Hammurabi, Neo-Assyrian Empire, Tiglath-Pileser III, Sargon II, Ashurbanipal, Urartu, Assyrian conquest of Egypt, Neo-Babylonian Empire, Nebuchadnezzar II, Eshnunna, Mari (Syria), Ipiq-Adad II, Sîn-kāšid, Rim-Sin I, Bit Adini, Tell Halaf, Bit Bahiani, Bit Yakin, Chaldea, First Sealand dynasty, Zimri-Lim.
