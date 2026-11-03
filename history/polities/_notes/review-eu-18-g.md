# Review of batch eu-18-g (2026-11-01)

Reviewer: Phase B adversarial reviewer. Dossiers: first-hellenic-republic, montenegro, united-principalities-of-moldavia-and-wallachia. The machine copy is history/notes/phase-b/reviews/eu-18-g.json. All three validate with --resolve: 0 errors, and 0 warnings except montenegro's unknown predecessor slug (prince-bishopric-of-montenegro, listed as needing a dossier). Spot checks: 8 events for Greece, 6 for Montenegro and 7 for Romania, on 13 pages. No event was fabricated or mis-dated at confidence 3.

Verdicts: first-hellenic-republic **fix** (three fixes applied by the reviewer, non-blocking items remain); montenegro **thin** (honest, but parts of the 1878-1913 border moves are undated within budget); united-principalities-of-moldavia-and-wallachia **fail** (two blocking findings, three small fixes applied).

## first-hellenic-republic: fix

Applied by the reviewer (re-validated):
- /ledger/13: counterpart kingdom-of-great-britain (ends 1800) changed to united-states-of-the-ionian-islands. The Treaty of London (1864) page calls the islands the "United States of the Ionian Islands", a British protectorate from 1815, and that dossier dissolves into this one in May 1864.
- /ledger/27: 1916 Bulgarian occupation of eastern Macedonia is now 1916-8, confidence 2, source Macedonian_front. The page has the advance "into Greek-held eastern Macedonia" (offensive launched 17 August) and Bulgaria taking "all Greek territory east of the river Struma". Added to sources[].
- /ledger/28: occupation end moved from 1919 (confidence 1) to 1918-9, confidence 2, source Macedonian_front ("The Macedonian front ended at noon on 30 September 1918"). Both events now match principality-of-bulgaria.

For the author (non-blocking):
- /ledger/25: Crete is gained twice, from cretan-state in October 1908 and from ottoman-empire on 14 December 1913. The second gain has no mirror, because the Ottoman dossier lost Crete in 1900. Keep the 1908 gain, since Cliopatria and cretan-state agree. Fold "formally taken over on 14 December 1913" (Treaty of Bucharest page) into its note or into a non-territorial event.
- /keyframe_review/0..7: every Cliopatria shape from 1822 to 1865 has a stray 5-vertex rectangle at 7.52-7.60 E, 49.58-49.65 N, in the Palatinate. This is why the shapes.csv bbox starts at 7.5155 E. It maps to no r5 cell. Name it in the 1822 keyframe note as a Cliopatria error.
- /keyframe_review/13..15: the 1916-1918 Cliopatria shapes drop eastern Macedonia, but the ledger records that land as occupied. Under rule 4, occupied land stays the owner's, hatched in the occupier's colour. Mark them adjust with the 1913 shape (montenegro_1916 does the same). Not a fault while they are noted "unverified: page budget".
- /keyframe_review/17: the correction is the whole 1920 shape including the Anatolian zone, while its text calls that zone occupied. Subtract admin1 Izmir, Manisa, Aydin, Balikesir, Bursa and Usak.
- 1919-1922: the ledger has no contest_start or contest_end, but ottoman-empire has contest_start 1919-5 and contest_end 1922 against this slug. Add them (Smyrna landing 15 May 1919; Armistice of Mudanya 11 October 1922, effective 15 October), or ask me-10 to drop theirs.
- 1940 technical close: principality-of-bulgaria records occupations of first-hellenic-republic from 1941 to 1944, and kingdom-of-greece starts in 1945. The orchestrator should decide whether this dossier runs to 1944.

Thin, within budget: the 1824 loss (confidence 1); the 1917 Aegean cells (probably the National Defence government, see National_Schism); the Lausanne date and Eastern Thrace handover; the 1897 war; the Epirus frontier.

Area: neither Greek page has an infobox area. The Treaty of Bucharest page gives 108,610 km2 after 1913, against 113,618 for the 1913 shape (ratio 1.05), and 64,790 before, against 64,329 (ratio 0.99). The author acknowledged both.

## montenegro: thin

Confirmed: 13 March 1852; Grahovac in May 1858 (the page also lists Nikšić, which the author noted); 4,405 to 9,475 km2 in 1878 (the page ties the figures to San Stefano and the recognition to Berlin, as the note says); the Treaty of Bucharest awarding "Berane, Ipek and Gjakova (Metohija)"; Skadar abandoned in May 1913; the Sandžak split on 30 May 1913; the occupation from 15 January 1916 to October 1918; Podgorica on 26 November 1918 (the page's lead says 28 November). The kingdom's area of 14,000 km2 against the 1913 shape's 14,164.7 gives a ratio of 1.01.

For the author:
- /ledger/7: Shkodër is lost in May 1913 at confidence 3 but never gained. The 1912 correction removes it and no April 1913 capture precedes the loss. The counterpart albania has no matching gain, and the page names no recipient: the city went to an international administration. Add the capture (23 April 1913; see Siege_of_Scutari_(1912-1913)) and agree the loss's counterpart with the Albania group.
- The dossier covers two states 88 years apart (1852-1918 and 2006-2024). The orchestrator should decide whether to split it.

Thin: Ulcinj's handover (November 1880) and Plav-Gusinje; the 1911 shape's +237 km2; the months of the 1912 conquests (First_Balkan_War); the prince-bishopric predecessor.

## united-principalities-of-moldavia-and-wallachia: fail

Applied by the reviewer (re-validated):
- /ledger/16: counterpart "Bessarabia" changed to "Moldavian Democratic Republic". The Kingdom of Romania page has the Sfatul Țării proclaim the union and lists the Moldavian Democratic Republic in its infobox succession.
- /ledger/14: confidence lowered from 3 to 2. The Galați radius is not on the page, which names "southern Moldavia" and does not mention Galați.
- /keyframe_review/0 note: the United Principalities infobox does give areas: 123,335 km2 for 1860 (ratio 1.04) and 130,177 km2 for 1881 (ratio 1.00).

Blocking, for the author:
1. /keyframe_review/6 (the new 1917 keyframe) removes the occupied south from Romania's land. Its own note says the south "stays Romanian land", keyframe 5 says the state's land is the 1915 shape, and the 1918 keyframe puts the south back with no event in between. Under rule 4, occupied land is the owner's, with the occupier's hatch. Correction: the 1915 shape.
2. The Ottoman suzerainty is missing. The United Principalities infobox reads "Vassal state of the Ottoman Empire (1859–1877)", and the Kingdom page says the union was under "nominal suzerainty". Add vassal_start 1859-2 and vassal_end 1877-5 with counterpart ottoman-empire. The Ottoman dossier does not carry this vassalage: its 1878 vassal_end events point to the Wallachia and Moldavia dossiers, which end in 1859.

Non-blocking:
- /ledger/14 and /ledger/18: the counterpart "Central Powers" cannot be mirrored. Dobruja fell from September 1916 (the page: "The Romanian garrison surrendered on 6 September" at Turtucaia), and principality-of-bulgaria has occupation_start 1916-9. Split the event into Bulgaria (Dobruja, 1916-9) and german-empire (Oltenia and Muntenia, 1916-12), and use Vrancea/Focșani in place of Galați.
- May 1918 Treaty of Bucharest: the Romanian Campaign page does give its terms (Dobruja to Bulgaria, the Carpathian passes to Austria-Hungary; King Ferdinand refused to sign; nullified 11 November 1918). principality-of-bulgaria records a 1918-5 gain from this slug, so say in the 1918 note why no loss is recorded.
- /ledger/19-20: Bukovina and Transylvania are gained from austria-hungary after its break-up. eu-20 should settle the counterpart.

Area: 137,903 km2 (1915 infobox) against 138,434.9 for the 1915 shape (ratio 1.00).

## Cross-dossier
Most unmatched events are on the ottoman-empire side (me-10): the Greek losses of 1824-1826, the 1832 cession, Montenegro's 1858 gain, the 1876-1878 and 1912-1913 wars, the Sandžak and Metohija gains, and the vassal pair for the United Principalities. The full matrix is in the JSON.
