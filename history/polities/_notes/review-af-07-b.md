# Review af-07-b (2026-10-19): Southern Africa part b

Reviewer: adversarial pass on natalia-republic, colony-of-natal, free-orange-state, south-african-republic, nieuwe-republiek, swaziland. Neighbours read: zululand, british-cape-colony (others not written yet). Pages opened (WebFetch): Natalia Republic, Colony of Natal, Orange Free State, Free State-Basotho Wars, South African Republic, First Boer War, Second Boer War, Nieuwe Republiek (twice), Eswatini, History of Eswatini. Machine copy: history/notes/phase-b/reviews/af-07-b.json.

Validator: 0 errors in all six before and after the reviewer's edits. Warnings: natalia-republic 7 (colony shapes, intended), colony-of-natal 2, free-orange-state 20 (Conquered Territory not in the gazetteer; basutoland not written).

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| natalia-republic | fail | the 1839-1843 shape holds Klip River county, which the page says Mpande ceded in 1843 |
| colony-of-natal | thin | one fix applied; paired Klip River gain region; Alfred County 1866 and the 1879 war missing |
| free-orange-state | fix | three fixes applied by the reviewer; Cape front of 1899 thin |
| south-african-republic | fix | three fixes applied by the reviewer (new 1888 keyframe); western border and Cape front thin |
| nieuwe-republiek | thin | 22 October 1886 Melmoth loss missed (the page has it); 1884-1886 extent not drawn |
| swaziland | thin | starts at Cliopatria's 1885; the kingdom dates from about 1745 and belongs in this dossier |

All 30 spot checks (4 to 6 per dossier, chosen among confidence 3 and the largest moves) were confirmed on the page: no fabricated or mis-dated event found.

## natalia-republic: fail (back to the author)

- /keyframe_review/0 and /1 (correction "shape unchanged"): Cliopatria's Natalia 1840 shape already contains most of the land between the Buffalo and Tugela rivers. Gazetteer test: a box north of the Tugela and west of the Buffalo holds 34 cells (about 9,000 km2) of that shape, all of Ladysmith and the Newcastle tip; only 10-14 cells (Msinga, Dundee) are in Cliopatria's Zululand. The Natalia page: "Mpande gave up to Natal all the territory between the Buffalo and Tugela rivers, which later formed Klip River county", placed during Cloete's visit after the Volksraad accepted the terms on 8 August 1843. Zululand's own note quotes Dingane's cession as "all the land south of the Tugela River". The notes' premise (the gift is the 10 Msinga cells) is wrong.
  Fix: natalia-republic_1839/_1840 = minus [Natalia 1840, {region: "Klip River County"}] (or a polygon north of the Tugela until the gazetteer has the county); same region in /ledger/0, /ledger/3 and predecessor/successor land; widen colony-of-natal /ledger/0 to the whole county plus the Msinga circle; zululand (af-07-a) then needs the county to 1843 and an 1843 loss. If you keep the land in the republic (Pretorius's 1840 proclamation), say so in the note with the page's words.
- Thin: Pretorius's St Lucia Bay proclamation (1840) undated and undrawn.
- Spot checks: 12 October 1839, 26 May and 26 June 1842, 12 May 1843: confirmed. No area on the page.

## colony-of-natal: thin

- Applied: /ledger/8 (dissolve) region set to the keyframe natalia-republic_1908 correction (with the 1903 districts).
- Not applied, paired with natalia-republic: /ledger/0 gain region to the whole Klip River county once the republic is corrected. The colony's keyframes from 1843 are already right.
- Thin: Alfred County (1866) lies south of Cliopatria's 30.5S edge in every shape; corrected 1903 shape about 71,000 km2 against the infobox's 91,610 (1904). Anglo-Zulu War 1879 (Rorke's Drift is in Natal) has no war or contest entry. Boer withdrawal after Ladysmith not dated.
- The notes say the page does not place Mpande's gift before or after the annexation: it does (after 8 August 1843), so the gain belongs here, as written.
- Spot checks: 4 May 1843, 1897, January 1903, 11 October 1899 / 28 February 1900, 31 May 1910: confirmed.

## free-orange-state: fix (applied by the reviewer)

- /wars/3/zones: added the northern-Natal zone that /ledger/8-9 contest (rule 10).
- /ledger/10-12 and /wars/3/zones/0: Cliopatria 1898 shape replaced by the 1871 outline, as the dossier's own keyframes _1885/_1898 require (3-cell notch).
- /ledger/10: confidence 3 to 2 (the page dates Bloemfontein's fall, not the occupation of the whole state).
- Thin: Cape front (Kimberley siege November 1899 to 15 February 1900, Stormberg 10 December 1899, invasion of the Cape October 1899 to January 1900: on the Second Boer War page); what the 15 October 1858 treaty's "new boundary" moved; the pre-1871 western edge (diamond fields).
- Spot checks: 23 February 1854, 19 March 1858, 15 October 1858, July 1867, 12 February 1869, 13 March 1900: confirmed. Area 181,299 km2 (1875) against 133,104: 0.73, acknowledged.

## south-african-republic: fix (applied by the reviewer)

- New keyframe south-african-republic_1888 (1888-1889, the _1890 correction): the 20 July 1888 Vryheid gain fell inside the 1885-1889 shape marked ok, so 1888-1889 drew no Vryheid. _1885's note now says it applies to 1885-1887.
- /wars/2/zones/1: Cliopatria 1898 shape (with Swaziland and the Lubombo polygon) replaced by the corrected outline used in /ledger/14.
- /ledger/14: confidence 3 to 2 (the page dates Johannesburg and Pretoria, not the whole republic).
- Thin: the 12-cell 1856-1885 change (Keate 1871 or London 1884 boundary); Stellaland and Goshen 1882-1885; Klein Vrystaat (about 1891); Zoutpansberg merger; Cape front (Mafeking 13 October 1899 to 18 May 1900).
- Spot checks: 17 January 1852, November 1859, 12 April 1877, 3 August 1881, 27 February 1884, 20 July 1888, 5 June 1900: confirmed. Area 191,789 km2 (undated) against 293,990: 1.53, acknowledged.

## nieuwe-republiek: thin

- Missed on the page the author opened: under the 22 October 1886 recognition agreement "the Melmouth district be administered by the British". The notes say the recognition changed no border; add a loss (Melmoth district, about 31.4E 28.6S).
- The 1884-1886 extent ("the whole of the Northwest of Zululand", the border extended "to the sea from the mouth of the Mhlatuze river to St Lucia Bay") is not drawn, so the 1886 and 1887 losses take land no keyframe has. The 13,600 km2 figure is undated.
- 1887 coast: it went to British Zululand, which zululand continues after its 1887 rename; counterpart zululand may fit better.
- /wars/0 (Tshaneni, 5 June 1884) predates the republic and does not list it.
- Verdict wrong on Cliopatria's shape: confirmed (no cell within 40 km of Vryheid).

## swaziland: thin

- The Eswatini page dates the kingdom to "the mid-18th century under the leadership of Ngwane III"; History of Eswatini: Dlamini III died 1744, Sobhuza I king 1815, Mswati II 1839-1865 ("twice its current size"), and the 1881 Pretoria Convention "reduced" Swazi territory. Extend this dossier back (start about 1745) instead of writing the separate 'swazi-kingdom' dossier the author proposed: the one-state argument that merged Swaziland and Eswatini applies before 1885 too.
- Merge of the swaziland and eswatini rows: agreed.
- Spot checks: 1894, October 1899, 1903, 6 September 1968: confirmed. Area 17,364 against 17,129: 0.99.

## Cross-dossier matrix (summary)

Matched: Cape 1854 loss / Free State 1854 found; Cape 1877-1884 occupation and vassalage / SAR; SAR 1888 gain / Nieuwe Republiek 1888 dissolve; SAR-Swaziland vassalage 1894-1899; zululand 1884 loss / Nieuwe Republiek found; zululand 1897 dissolve / Natal 1897 gain; the 1899-1900 Natal contest on all three sides.
Missing or mismatched (route to af-07-a): zululand has no 1843 loss to Natal; zululand's February 1838 loss is 20 months before the republic's 12 October 1839 founding; the Cape has no First Boer War contest (December 1880 to March 1881) and no 1899-1900 Cape-front contest (also missing on the Boer side).
Exceptions (not written yet): transvaal-colony, basutoland, Lydenburg and Utrecht republics, british-colonial-empire.

## Gazetteer names needed

Conquered Territory (region); Klip River County (region); Melmoth, Utrecht, Wakkerstroom, Lydenburg, Newcastle, Dundee (places, South Africa).
