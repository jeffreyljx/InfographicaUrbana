# Review of batch am-08-g (2026-10-19)

The validator (--resolve) passes all seven dossiers with 0 errors. The only warning is the deliberately empty correction at republic-of-baja-california /keyframe_review/1. I spot-checked 33 events and keyframes on 10 Wikipedia pages. Nothing is fabricated and no confidence-3 event is mis-dated.

## Verdicts
- mosquito-kingdom: **fix**. The reviewer applied two fixes; one finding is still open.
  - Applied: /ledger/2/note quoted 'Britain and the Miskito seized it in 1848', which is not on the page. The page's sentence is undated: "Miskito-British forces led by the King and Patrick Walker, and backed by two British warships, seized San Juan del Norte". The year 1848 rests on the ultimatum ("before 1 January 1848") and on "the 1848 peace treaty". The quote is replaced and confidence 2 stays.
  - Applied: /identity/rulers/0 started in 1841, before the dossier starts. It is clipped to 1844; the note keeps 1841.
  - OPEN (not blocking): republic-of-nicaragua /ledger/10 is a vassal_start (1860-01) and /ledger/12 a vassal_end (1894-11), both with counterpart mosquito-kingdom. This dossier has no mirror for either: it has only a rename in 1860 and a loss and dissolve in 1894. Add a vassal_start in 1860-01 with counterpart republic-of-nicaragua, the region of the 1860 keyframe and confidence 3 (the page has the Treaty of Managua of 28 January 1860 "transferred suzerainty"). Add a vassal_end in 1894-11.
  - Thin: two events rest on the shape alone and have no page:
    - the 1846 gain from Honduras, at confidence 1;
    - the 1859 cession to Honduras, with no treaty and no day (try the Wyke–Cruz Treaty page).
  - Thin: the time before 1844 is not covered.
  - Thin: the page says the 1860 treaty left the Kingdom "now reduced to the territory around Bluefields", which is smaller than the 71-cell strip drawn.
- republic-of-baja-california: **pass**. I checked these and found them all correct:
  - 3 November 1853, La Paz (Baja page);
  - 21 January 1854 and 8 May 1854 (Walker infobox: "President of Sonora" from January 21, 1854 to May 8, 1854);
  - Walker's Nicaraguan presidency, 12 July 1856 to 1 May 1857, which justifies the wrong verdict on the 1856 shape.
  - Optional for a gap-filler: the Walker page says he moved his headquarters "twice in the following three months, first to Cabo San Lucas and then north to Ensenada", which dates Ensenada to about February 1854.
- state-of-buenos-aires: **thin**. All dated events are confirmed:
  - 11 September 1852, the secession;
  - the siege from 1 December 1852 to 12 July 1853;
  - Cepeda on 23 October 1859 and the pact of 11 November 1859;
  - reunification on 12 December 1861.
  - The open gap is the 1857 enlargement of the outline (306 cells, about 54,000 km2). It is a confidence-1 gain from nobody and is on no page. Pavón's day is also missing (try the Battle_of_Pavón page). This is thin by design within the 1-2 page budget.
- granadine-confederation: **fix**. One finding is open (not blocking).
  - The war page says: "Santander sided against the centralised government on the outbreak of the civil war" (8 May 1860). /ledger/2 instead dates Santander (and Norte de Santander) to 1861 at confidence 1, as "page silent".
  - Move Santander and Norte de Santander into the 1860-05 loss (/ledger/1) at confidence 2. Keep Boyacá, Magdalena and Tolima in 1861. Make the same change in mosquera-s-cauca-rebellion.
  - Confirmed: 22 May 1858, 8 May 1860, Bogotá falling on 18 July 1861 (18 June on the Granadine page; the dossier notes the conflict), and 8 May 1863.
  - Area: Cliopatria has 1,223,348 km2 against the successor's undated infobox figure of 1,331,250 km2. The ratio is 0.92, and the dossier acknowledges it.
- united-states-of-colombia: **thin** by design. The two ledger events are confirmed: 3 February and 8 May 1863, and the 1886 abolition. The 1,331,250 km2 infobox figure is confirmed. What is missing:
  - wars for 1863-1886: the 1876-77 and 1884-85 civil wars;
  - verification of the 1866-1886 keyframe.
- mexican-monarchists: **thin**. These are confirmed on the pages:
  - the Regency, 11 July 1863;
  - Querétaro on 17 November, Morelia on 30 November, Guanajuato on 9 December and San Luis Potosí on 25 December 1863. The years are implied by the page's sequence, so confidence 2 is correct;
  - Guadalajara on 5 January 1864 (year printed);
  - Maximilian's acceptance on 10 April 1864.
  - The open gap is the 1864 shape's composition. Veracruz, Tabasco, Campeche, Zacatecas and Aguascalientes are inside it with no event. San Luis Potosí and Morelia are outside it.
  - The page dates the Imperialists' control of "the central Mexican states, their major cities, two thirds of the population" only to late 1864. The author flagged all of this.
- mosquera-s-cauca-rebellion: **fix**. The reviewer applied one fix; one finding is open.
  - Applied: /ledger/0 was at confidence 3 although its region (Cauca, Valle del Cauca and Nariño) is not named on the page. The war infobox puts Pasto (in Nariño) on the Confederation's side. Confidence is lowered to 2.
  - OPEN (not blocking): move Santander to 1860 in the found region and in /keyframe_review/0, as above.
  - Thin: the capital (Popayán is unsourced), the extent of the Cauca state (Chocó and Caquetá), and when Boyacá, Magdalena and Tolima came over.

## Cross-dossier
- These pairs match:
  - Honduras: 1846 and 1859;
  - Nicaragua: 1848 gain and loss, and 1894 gain and loss;
  - Mexico and Baja California: 1853, and 1854 (01 and 05 fall in the same year);
  - Argentine Confederation: 1852 and 1861;
  - republic-of-new-granada: 1858;
  - Granadine Confederation, the rebels and the United States of Colombia among themselves.
- Mismatch: Nicaragua's vassal_start (1860) and vassal_end (1894) have no mirror in mosquito-kingdom (the fix above).
- Missing, on Mexico's side: federated-republic-of-mexico has no occupation events naming mexican-monarchists:
  - Querétaro, Morelia, Guanajuato and San Luis Potosí (November and December 1863);
  - Guadalajara (5 January 1864).
  - Its 1863 events for Puebla and Mexico City name second-french-empire. This should be routed to the Mexico author.
- Exceptions (no dossier yet, groups that have not run): second-mexican-empire, republic-of-colombia and second-french-empire (eu-20).

## Gazetteer
- La Paz (Baja California Sur), a place. The dossier uses a coordinate radius in its place.
