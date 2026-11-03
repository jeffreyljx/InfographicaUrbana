# Review of batch me-06-a (2026-10-19)

The machine copy of this review is history/notes/phase-b/reviews/me-06-a.json; it holds every finding, spot check and cross-check.

Both dossiers validate (0 errors). The only warnings are the expected ones: slugs with no dossier yet (characene, elymais, persis) and the region "Characene", which the gazetteer does not have.

## parthian-empire: fail (back to the author)

Ten confidence-3 events were checked on their pages, and each page says what the note claims: -148 Media, -141 Babylonia, -129 Ecbatana, -122 Characene, -113 Dura-Europos, the -95 vassals Adiabene, Gordyene and Osroene, -40 and -38 Syria, and 197. Area: the infobox gives 2,800,000 km2 for 1 AD, the Cliopatria 1..42 shape is 2,702,797 km2 (ratio 1.04), and the dossier says so.

One fix was applied by the reviewer: /ledger/59 (197 loss of northern Mesopotamia) goes from confidence 3 to 2. The page dates the sack of Ctesiphon to 197 but not the acquisition ("These wars led to..."). The file was re-validated.

Blocking:

1. **Atropatene.** The -148 keyframe and every later outline draw Atropatene as direct Parthian land: 317 of its 496 cells, from -126 to 224. The ledger never gains it (it has only contest -148/-147), yet it loses it to Armenia at -87 and contests it with Rome in -36. The existing atropatene dossier keeps the land as an autonomous state -148..225 ("frequently a vassal of the Parthian Empire"). Fix: add vassal_start atropatene at -147 (confidence 2, Mithridates I page) and the matching ends, and subtract {"cliopatria": "Atropatene", "year": -170} from the Parthian keyframes. Or agree with the atropatene author that the land is direct Parthian.
2. **Sistan after 19.** /ledger/46 loses Sistan to the indo-parthians in 19, but keyframes 17-32 (1..224) all keep 122 of the 256 Sistan cells. The indo-parthians dossier draws Sistan 19-226, so the land is drawn twice. Fix: split keyframe 17 at 19 and subtract {"region": "Sistan"} from then on, or drop the confidence-1 loss and settle it with sa-02.

Also to fix:

3. **First capital.** Hecatompylos (54.35 E, 36.17 N) lies outside the -239, -223 and -218 outlines that keyframes 0-2 accept as ok: the bbox's southern edge is 36.42 N and no cell is within 40 km. Add Comisene, for example {"place": "Hecatompylos", "km": 60}.
4. **The -66 keyframe.** It is marked ok while its note calls the Syrian cells unsupported. The -63 loss (confidence 1) removes 253 cells at 38.1-46.8 E, which are upper Mesopotamia, not Pompey's Syria; roman-republic takes Syria from the Seleucids at -64.
5. **The -115 gain from yuezhi.** It is at confidence 2, but the page does not name the nomads, and yuezhi has no mirror. Lower it to 1, or name the people a page gives.

Thin (for a gap-filler):

- -209/-188 Seleucid vassalage (Antiochus III page).
- Persis in the 130s BC (Persis page).
- The -77 step: 423 cells lost, some as far east as 67 E (Indo-Scythians page).
- The 19 Indo-Parthian split.
- The ends of Characene and Elymais in 224.
- The Kushan frontier and Hatra.
- Margiana from -144 to -92 and the Pakistani cells at -91.

## himyarite-kingdom: thin

Six events were checked on their pages, all confirmed: -110 independence, -25 Saba, 100 Saba free, 275 Saba, 300 Hadramawt, 522 Dhu Nuwas. Not splitting the 711-year row is argued from the Himyar page and is accepted. Area: the infobox gives none, and the dossier says so. Capitals are inside the shapes.

Findings, not applied and not blocking:

1. **Qataban c. 200.** /ledger/3 takes Qataban's land from the qataban dossier, which ends at 183. The hadhramaut dossier takes that land at 184 and holds it to 300. Agree with me-04: drop the event, or keep it at confidence 1 with counterpart hadhramaut.
2. **Late steps.** The 275 Saba gain and the 300 Hadramawt gain are drawn only from 283 and 306, and Hadramawt is nobody's land for 300-305. Add keyframes 275..282 and 300..305.

Thin (for a gap-filler):

- **Kinda as a client c. 450-550.** The Kingdom of Kinda page calls Himyar Kinda's "patron" and Hujr its "dependent", and compares the tie to "the Arab client kingdoms". That is a vassal tint under rule 4, over southern Najd; add it once kingdom-of-kinda exists (me-06-x).
- The capital move to Sanaa (401, confidence 1).
- The end of the Aksumite occupation: 230 here, 275 in kingdom-of-axum.
- Abraha: 531 here, 525 in kingdom-of-axum.

## Cross-dossier mismatches to route

- **seleucid-empire (me-05):** its -164 loss to Parthia is rejected by the Parthian dossier; its -110 loss falls against Dura-Europos in -113.
- **indo-scythians (sa-02):** Sakastan is taken in -100 there and in -115 here.
- **yuezhi (ia-01):** no mirror for the -115 gain.
- **roman-republic (eu-03):** it takes Syria from the Seleucids in -64, while Parthia loses land to Rome in -63.
- **roman-empire (eu-04):** no 165 gain of upper Mesopotamia.
- **atropatene:** the land overlap described in finding 1.
- **kingdom-of-axum (af-01):** a direct conquest in 520 where Himyar becomes a vassal only in 525; the occupation ends in 275 there and in 230 here.
- **Exceptions:** sasanian-empire, adiabene, gordyene and osroene (other parts of me-06, not written yet); kingdom-of-armenia (eu-19, not run); characene, elymais, persis and kinda (me-06-x).
