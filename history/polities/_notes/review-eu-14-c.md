# Review, batch eu-14-c (2026-10-25)

Adversarial review of `old-kingdom-of-norway` and `icelandic-commonwealth`. The machine copy is `history/notes/phase-b/reviews/eu-14-c.json`. The reviewer made no edits to either dossier.

Neighbour dossiers read for cross-checks: `kingdom-of-the-isles`, `kingdom-of-scotland`, `dal-riata`, `brythons`, `norman-england`, `angevin-empire`. The other Context polities in section 6 of the brief are not written yet: kingdom-of-sweden, kingdom-of-alba, kingdom-of-denmark, viking-settlements, jaemtland, scandinavian-minor-kingdoms, strathclyde, north-sea-empire, kingdom-of-england, kingdom-of-mann and denmark-england. The same holds for norway-denmark, kalmar-union and norse-greenland.

Mechanical: `validate_dossier.py --resolve` gives no errors and no warnings for either file. All 22 Cliopatria shapes of Norway and both Iceland shapes have verdicts. The new keyframes (Norway 872, 995, 1046, 1264; Iceland 930) carry from, to and a correction. The ledgers are sorted, with found at start and dissolve at end, and the certainty spans are contiguous. Family `nordic` exists. Every capital tested lies inside its Cliopatria shape on the H3 grid except Konungahella, which is two cells outside (see thin).

## old-kingdom-of-norway: fail (one blocking finding; the rest held up)

Spot checks: 19 entries on eight pages, about 23 events, all confirmed with year and wording. They cover the 875 Northern Isles and Caithness gains, the 1264 Iceland gain, the 1098 grant, Largs 1263, the Treaty of Perth (2 July 1266, Hebrides and Mann to Scotland), the 1028 and 1035 occupation, the 970 and 1000 Viken losses, 866 and 872, Vardøhus 1306, the five capital moves from the Kingdom infobox, and 1380, 1387, 1389 and 17 June 1397. No fabricated or mis-dated event was found.

Area: the Kingdom of Norway (872-1397) infobox has no area, and the Norway article describes the modern state. The author says so; there is nothing to compare.

### Blocking

1. **/keyframe_review/22-25: Greenland dropped 1333-1397.** Keyframes `_1333`, `_1344` and `_1363` (verdict ok) and `_1395` (adjust, "unchanged") leave out the Norse Greenland cells that the 1272-1326 shapes have. No ledger event explains the drop, and the dossier's own ledger has Greenland gained in 1272 and never lost. /ledger/30 says Greenland goes into the Kalmar Union with Norway, and the 1333 note itself says the drop "looks wrong". Evidence: Kalmar Union page, Norway "(then including Iceland, Greenland, the Faroe Islands, and the Northern Isles of Orkney and Shetland)"; Kingdom page, "Iceland, Faroe Islands and Greenland remained under Norwegian administration until 1814". **Fix:** set these keyframes to adjust, with correction `{"union":[{"cliopatria":"Old Kingdom of Norway","year":<Y>},{"intersect":[{"cliopatria":"Old Kingdom of Norway","year":1326},{"country":"Greenland"}]}]}`. In the 1363 note, say that Cliopatria's Norse Greenland row overlaps 1363-1384, so norse-greenland is drawn either as a Norwegian dependency or not at all for those years. Otherwise, write a sourced loss event.

### Non-blocking

2. **Capital moves to Nidaros have no events.** The ledger has capital_move events for 1016, 1067, 1123, 1217 and 1314 but none for the returns to Nidaros in 998, 1029 and 1151. Notes item 10 says those spans are "inferred from gaps", but the infobox gives them: "Niðaróss (Trondheim) (997–1016, 1028–1067, 1150–1217)". **Fix:** add the three events at confidence 3 and correct the note.

### Thin (for the gap-filler; the author already flagged most of these)

- **1333-1401:** about 30,000 km2 of Swedish land is added with no event: Värmland (Karlstad), Västergötland including Skara, and half of Dalarna. It is probably a Cliopatria artefact, perhaps Duke Eric's duchy. Keep only Bohuslän, Idre and Särna unless a page says otherwise. Page to try: Eric Magnusson, Duke of Södermanland.
- **1314:** the growth of Jämtland and the Västerbotten cells are unexplained. Page to try: Härjedalen.
- **Confidence-1 events:**
  - 870 Hålogaland (page: Hålogaland)
  - 995 Viken (page: Olaf Tryggvason)
  - 1015 Viken; Nesjar 1016 is the likely dated event (page: Olaf II of Norway)
  - 1040 Faroes (page: History of the Faroe Islands)
  - 1188 Jämtland; Sverre's campaign around 1178 (page: Jämtland)
  - 1272 Greenland; usually dated 1261 (page: Norse Greenland)
- **Konungahella:** the capital at Kungälv (1123-1150) is just outside the Cliopatria shape, which stops short of the Göta älv. Settle it with the Bohuslän page.

## icelandic-commonwealth: pass

What I tried:
- The 930 found, the 1264 loss and the 1264 dissolve are all confirmed: the Icelandic Commonwealth page ("around the year 930"; "By 1264, all Icelandic chieftains had sworn allegiance to the King of Norway") and the Old Covenant page ("made in 1262–1264").
- The new 930-935 keyframe and the 1260 shape cut to 1263 are consistent with Norway's 1264-1271 keyframe.
- Þingvellir lies inside the shape.
- The infobox has no area. Cliopatria's 112,115 km2 for the island is plausible.
- The 1264 loss is mirrored by Norway's 1264 gain.

The "war" entry (1220-1264, Norway as belligerent, empty zones) is a period of strife rather than a war, but the note says so and the quoted sentence is on the page. I could not break it.

## Cross-dossier

- **Matched:** Norway gain 1264 and Iceland loss 1264.
- **Missing on the Isles side (route to eu-11):** `kingdom-of-the-isles` has no vassal_start 1098 or vassal_end 1266 with counterpart old-kingdom-of-norway. Its notes defer the overlordship to the Norway dossier, and the years agree.
- **Exceptions, counterparts not yet written:**
  - scandinavian-minor-kingdoms (870, 872)
  - viking-settlements (875 twice, 1040)
  - kingdom-of-denmark (970, 995, 1000, 1015)
  - north-sea-empire (1028)
  - jaemtland (1188)
  - norse-greenland (1272)
  - kingdom-of-alba (contest 1263-1266)
- **For the orchestrator:** kalmar-union must start in 1397, or 1398-1401 is empty. norway-denmark must settle 1046-1055 against the new Norway keyframe.
