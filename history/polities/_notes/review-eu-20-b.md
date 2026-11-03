# Review of batch eu-20-b (2026-11-01)

Reviewer: adversarial review, Phase B. Validator: all six dossiers 0 errors (warnings only for slugs that still need dossiers, and septinsular /wars/0 outside the life). Every page opened loaded. Machine copy: history/notes/phase-b/reviews/eu-20-b.json.

Verdicts: republic-of-san-marino **fail**; helvetic-republic, revolutionary-roman-republic, cispadane-republic, french-consulate, septinsular-republic **thin**. No event was found fabricated or mis-dated: every confidence-3 event spot-checked says what its note claims.

## Reviewer edits (applied, re-validated)
- revolutionary-roman-republic: counterpart `kingdom-of-naples-napoleonic` (dossier life 1806/3..1815/5) replaced by `kingdom-of-naples-bourbon` (1735..1814) in /ledger/1, /ledger/2, /ledger/3, /wars/0, /wars/1 and /identity/successors/0.
- french-consulate /ledger/10/region: `Piedmont` resolves to all eight Piedmont provinces, including Novara and Verbano-Cusio-Ossola; the Subalpine Republic page gives Novara (department of Agogna) to the Italian Republic, and Cliopatria's 1803 French shape has 1 Novara cell and no VCO cell. Region is now Piedmont + Aoste minus Novara + Verbano-Cusio-Ossola.

## republic-of-san-marino (fail)
- Same state as `san-marino.json` (Q238, 301..2026). Two dossiers mean two drawings and two colours. Merge: add "Republic of San Marino" to san-marino.json `cliopatria_names`, move the two keyframe reviews there, delete this file (the orchestrator has to do it, because the file is outside this batch).
- K0 note is wrong: the Cliopatria shape is not in the same grid cell as San Marino. The gazetteer puts the shape at 12.53 E 43.79 N and the country at 12.41 E 43.91 N, with no cells in common; the capital lies outside the shape's bbox. The correction {country: San Marino} is right; the note should say the shape is displaced about 17 km south-east.
- As a full-life dossier it lacks the 1463 enlargement and the Alberoni occupation (17 October 1739 to 5 February 1740), which both pages give and san-marino.json already holds. The merge resolves this.
- Area: 61.19 km2 (infobox) against 47.0 km2 (Cliopatria): ratio 0.77, acknowledged.

## helvetic-republic (thin)
- Client relation missing. The infobox says "Client state of France". french-directory L15 (vassal_start 1798/4) and french-consulate L1 (1799/11) and L11 (vassal_end 1803/2) name this state; add the four mirror events.
- Jura (non-blocking): the minus removes only the canton of Jura. The page excludes "the old Prince-Bishopric of Basel", which also covered the Bernese Jura, Biel/Bienne and Laufen. The gazetteer has no Bernese Jura region (requested).
- Thin: Fricktal (1802) and Konstanz are named but undated on the page.
- Confirmed: found 12 April 1798; Graubünden 21 April 1799 (Three Leagues infobox); Valais 1798 and 1802 (years only); end 19 February 1803.
- Matched: swiss-confederation L37 (1798/3) and L43 (1803/2).

## revolutionary-roman-republic (thin)
- Client relation missing. The infobox says "Sister republic of Revolutionary France". Mirror french-directory L14 (1798/2) and L23 (1799/8).
- 1799 to 1800 handover: kingdom-of-naples-bourbon has no occupation of Rome (30 September 1799 to June 1800), and papal-states L36 regains the land in June 1800 from this state, which had ended in 1799. Route to eu-13 and the Naples owner. Here, L3 could be typed as the occupation that ends the state.
- The L2 note quotes "re-entered Rome on 14 December 1798". The page says "re-entering Rome on 14 December", with no year, though 1798 is clear from context.
- Thin: when the Tiberina and Anconine Republics were incorporated, and the Austrian siege of Ancona (1799).

## cispadane-republic (thin)
- Modena: the Cisalpine page says "On 19 May 1797, Napoleon transferred the territories of the former Duchy of Modena to Transpadania", and cisalpine-republic L2 records that gain from the duke. This dossier holds Modena until the merger. Add a loss in 1797/5 to transpadane-republic, and say in L3's note that the pages disagree on the union date: 29 June here, 27 July "for the rest of Cispadania".
- Romagna: papal-states L34 sends Romagna, Ferrara and Bologna to the Cispadane at Tolentino, but this dossier never holds Romagna, and cisalpine L0 takes it directly. Open the Treaty of Tolentino page and settle which is right.
- Thin: the Duchy of Massa and Carrara is a predecessor (the Alpi Apuane department by July 1797) with no event.

## french-consulate (thin)
- Malta: kingdom-of-great-britain L16 gains it from the Consulate on 4 September 1800, but there is no loss here, and no Consulate keyframe holds a Malta cell. Add the loss, and add Malta to the 1799 and 1800 shapes.
- Piedmont 1800-1802: kingdom-of-sardinia L21-L23 records a French Consulate occupation from June 1800 and a loss to the Consulate in September 1802. This dossier has no 1800 event and gains Piedmont from subalpine-republic. Add the relation that begins on 20 June 1800 (vassal of the Subalpine Republic, or occupation of Sardinia) and agree the counterpart with eu-13.
- Jura: same partial removal as in the Helvetic Republic (non-blocking). The Paris capital cites a page that names no capital (non-blocking).
- Thin: Parma (confidence 1); the client relations with the restored Cisalpine Republic, the Italian Republic, Liguria, the Batavian Republic and Etruria; the overseas cells.
- Routed: ottoman-empire L156 dates the return of Egypt to 1803 at confidence 1 (this ledger has 1801/6 and 1801/9 from the page). duchy-of-bavaria L34 names the Consulate for Rhine-bank land that french-directory L10 already annexed in 1797. kingdom-of-naples-bourbon L6 (the Presidi ceded to France in March 1801) conflicts with state-of-the-presidi L3 (to Etruria in September 1801). kingdom-of-etruria has no 1802 Elba loss.
- Confirmed: 8 March, 27 June and 2 September 1801 (Egypt); Elba 1802; Piedmont 11 September 1802; 18 May 1804.

## septinsular-republic (thin)
- Protectorate missing. The infobox says "Protectorate of the Russian and the Ottoman Empires" and "Formally under Ottoman suzerainty". Add vassal_start 1800/4 and vassal_end 1807/8 with ottoman-empire (and russian-empire). Neither of those dossiers has it either.
- The found counterpart `french-directory` ended on 9 November 1799 and has no loss of the islands. The Russo-Ottoman fleet held them from autumn 1798 and took Corfu on 4 March 1799. Use ottoman-empire or russian-empire, and route the occupation pair.
- /wars/0 (1798-1799) lies outside the state's life (non-blocking).
- Confirmed: 2 April 1800 and 20 August 1807. first-french-empire L17 (1807/9) matches.

## Gazetteer
- Needed: Elba (region), Bernese Jura / Jura bernois (region).
