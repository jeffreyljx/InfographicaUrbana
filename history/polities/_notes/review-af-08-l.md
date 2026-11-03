# Review of batch af-08-l (written 2026-10-24)

Reviewer: adversarial review, Phase B. Dossiers: libyan-arab-republic, zaire, mozambique, republic-of-guinea-bissau, mauritius. Neighbour dossiers read (ledgers grepped): republic-of-chad, kingdom-of-libya, republic-of-sudan, republic-of-tunisia, south-africa, guinea (context list), plus democratic-republic-of-the-congo and portuguese-mozambique (same land / predecessor). The other context polities (zambia, malawi, tanzania, estado-novo, people-s-republic-of-angola, rhodesia, arab-republic-of-egypt, republic-of-senegal, ...) have no file yet: their groups have not run.

Mechanical: validator --resolve passes all five; the only warnings are the gazetteer's unknown 'Aouzou Strip' (3 places in libyan-arab-republic, also used by republic-of-chad). Families are colours.json keys; capitals fall inside their shapes' bboxes; ledgers sorted; found/dissolve at start/end.

## Verdicts

| slug | verdict | spot checks | area (infobox / Cliopatria) |
| --- | --- | --- | --- |
| libyan-arab-republic | pass | 6 confirmed | 1,759,541 / 1,614,019 = 0.92 |
| zaire | pass (duplicate state: see Problems) | 4 confirmed | 2,345,409 / 2,307,837 = 0.98 |
| mozambique | thin (1 note fixed by reviewer) | 4 confirmed | 801,590 / 784,529 = 0.98 |
| republic-of-guinea-bissau | fix (applied by reviewer) | 3 confirmed + war dates | 36,125 / 32,871 = 0.91 |
| mauritius | fix (applied by reviewer) | 4 dates confirmed | 2,040 / 2,480 = 1.22 (acknowledged) |

### libyan-arab-republic: pass
- Confirmed on the pages: /ledger/1 (Aouzou Strip: "in 1973, Libya proceeded to occupy and annex"); /ledger/4 (Chadian-Libyan conflict: attack of 6 December 1980, "the fall of the capital on 16 December"); /ledger/6 ("by 16 November all Libyan forces had left Chad, redeploying in the Aouzou Strip"); /ledger/9 ("an OAU-brokered ceasefire on 11 September" 1987); /ledger/10 (withdrawal "began on 15 April and was completed by 10 May" 1994); /ledger/13 (First Libyan Civil War: NTC declared liberation 23 October 2011). /ledger/2 and /ledger/8 renames confirmed on the Libya page (2 March 1977; name to 1986).
- /ledger/3 is dated February 1978; the page opens the offensive on 29 January 1978 (ground taken in the following weeks): acceptable at confidence 2, the Chad mirror uses the same month.
- Mirrors: all Chad events match within the month except the N'Djamena occupation (see cross-checks): republic-of-chad lacks occupation_start 1980-12 / occupation_end 1981-11. The Libyan side is confirmed by its page; the Chad group (af-08-h) should add the mirror.
- Thin (budget 5, used 6): the 2011 contest is Cyrenaica only (Misrata, Nafusa Mountains, Tripoli August 2011 undrawn); dissolve 2013 at confidence 1 is a Cliopatria row boundary (the Libya page gives GNC handover 8 August 2012 and the Second Civil War from May 2014). Minor: /ledger/13 contest_end names all Libya while /ledger/11 names Cyrenaica (harmless).

### zaire: pass on content
- Confirmed: /ledger/0 (renaming announced 27 October 1971); /ledger/1-2 (Shaba I infobox "8 March - 26 May 1977"; Dilolo, Kapanga, Kissenge captured, Mutshatsha entered 25 March); /ledger/3-4 (Battle of Kolwezi "fought in May 1978"); /ledger/6-7 (Mobutu fled 17 May; renamed 21 May 1997).
- Same state as democratic-republic-of-the-congo, which already covers 1960-2024 with a new keyframe pointing at the Zaire shape (af-08-f review flagged the same). Both dossiers own the land 1971-1997. Not an author fault (the slug was assigned and the author flagged it); routed under Problems. The zaire ledger's Shaba I and Shaba II contests are what the DRC dossier lacks (af-08-f listed them as DRC thin items).
- Thin: /ledger/5 has no month (DRC dossier has October 1996 from the First Congo War page) and the AFDL contest stays on the two Kivus until May 1997 although the advance crossed the country.

### mozambique: thin
- Confirmed: /ledger/0 (25 June 1975); /ledger/1 (civil war "30 May 1977 - 4 October 1992"); /ledger/2 (infobox "People's Republic of Mozambique: 25 June 1975 - 30 November 1990"); /ledger/3 ("On 4 October 1992, the Rome General Peace Accords").
- Applied: /keyframe_review/1/note said the civil war is "carried by a contest event in the north"; the contest is Sofala (central). Note corrected.
- Not applied (author or gap-filler): /wars/1 says the Mozambique page "says nothing of ground held", but the page says "Islamist rebels seized the city of Palma" (March 2021 by its context). Add a Palma contest (zone {"place": "Palma", "km": 30}) with dates from the insurgency page, and correct the note. /wars is missing the 2013-2019 RENAMO insurgency: the page says "From 2013 to 2019, a low-intensity insurgency by RENAMO occurred, mainly in the country's central and northern regions" and "the Accord on Cessation of Hostilities" (5 September 2014): add a war entry (zones empty unless a page names held ground).
- Thin: RENAMO extent in the 1980s (the civil war page: raids "virtually anywhere in the country except for the major cities"); Rhodesian incursions (Mapai 1977).

### republic-of-guinea-bissau: fix (applied)
- Confirmed: /ledger/0 and /ledger/1 ("On 23-24 September 1973 ... declared the independence"; Portuguese forces "largely confined to the major cities and a diminished collection of fortified camps"); /ledger/2 ("Portugal granted full independence to Guinea-Bissau on September 10, 1974"); Algiers accord 26 August 1974.
- Applied: /wars/0/from was 1963, before the state's start (1973-09): set to 1973 and the note now records the infobox dates "January 23, 1963 - September 10, 1974".
- Thin: the 1973-74 contest is the whole country; the Portuguese-held towns are not listed on the pages opened.

### mauritius: fix (applied)
- Confirmed: /ledger/0 ("independence was proclaimed on 12 March 1968"); /ledger/1 ("On 12 March 1992, Mauritius was proclaimed a republic"); the ICJ opinion "In February 2019" and the joint statement "In October 2024" are on the page as dated.
- Applied: removed the contest_start 2019-02 / contest_end 2024-10 pair over the British Indian Ocean Territory (counterpart kingdom-of-great-britain). The master plan draws contested land "from the first campaign that takes ground until the fighting ends"; the Chagos dispute is a claim pursued in the ICJ and the UN with no fighting and no war entry (the event's own note said "a sovereignty dispute ..., not a campaign"), and the author's own note (3) declines a Tromelin contest for the same reason. The claim stays in certainty; the notes field now says why. A gain from kingdom-of-great-britain belongs to a later update once the 2025 treaty takes effect.

## Cross-dossier matrix
- libyan-arab-republic 1969 found (kingdom-of-libya) / kingdom-of-libya 1969-09 dissolve: matched.
- libyan-arab-republic 1973 occupation_start Aouzou (republic-of-chad) / republic-of-chad 1973 occupation_start: matched.
- libyan-arab-republic 1978-02 and 1983-06 contest_start, 1981-11 and 1987-09 contest_end / republic-of-chad same months: matched.
- libyan-arab-republic 1980-12 occupation_start and 1981-11 occupation_end N'Djamena / republic-of-chad: MISSING on the Chad side (route to af-08-h).
- libyan-arab-republic 1994-05 occupation_end Aouzou / republic-of-chad 1994-05: matched.
- libyan-arab-republic 2011-02 contest (National Transitional Council): exception, no dossier (listed by the author; under a year of ground).
- libyan-arab-republic 2013 dissolve / state-of-libya: exception, not yet written (another af-08 part).
- zaire 1971-10 found / democratic-republic-of-the-congo 1971 rename: matched (same state).
- zaire 1977, 1978 contests (FNLC): exception, rebel held ground under a year.
- zaire 1996 contest_start AFDL / democratic-republic-of-the-congo 1996-10: mismatch by month only (zaire has none).
- zaire 1997-05 dissolve / democratic-republic-of-the-congo 1997-05 rename: matched.
- mozambique 1975-06 found / portuguese-mozambique 1975-06 dissolve: matched.
- mozambique 1977-05 contest (RENAMO): exception, listed as needing a dossier.
- republic-of-guinea-bissau 1973-09 found and contest, 1974-09 contest_end (estado-novo): exception, estado-novo (eu-21) not yet written; portuguese-guinea listed.
- mauritius 1968-03 found (british-colonial-empire): exception, not yet written (a European group).

## Problems for the orchestrator
- zaire and democratic-republic-of-the-congo are one state; both own 1971-1997. Keep one (the earlier slug, democratic-republic-of-the-congo, per the one-dossier rule): fold zaire /ledger/1-4 and /wars/0-1 (Shaba I, Shaba II) into it and retire the zaire slug, or the state gets two colours and double-owned cells.
- Libya is one continuous state across three Cliopatria rows (kingdom-of-libya 1951-1969, libyan-arab-republic 1969-2013, state-of-libya 2014-2024; data/README.md lists Kingdom/State of Libya as near-duplicate Names): a colour decision for the integrator.
- republic-of-chad needs the N'Djamena occupation mirror (1980-12 to 1981-11).
- Three dossiers were edited by the reviewer (mauritius, republic-of-guinea-bissau, mozambique); all re-validate.
