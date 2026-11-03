# Colour run, 2026-11-01: notes of the colour agent

Brief: `notes/phase-c/colour-run-2026-11-01.md`, with the orchestrator's adjustments of the same day (vassals, members and colonies are drawn in their suzerain's colour; a batch helper for the 1,494 new states; clashes resolved until none a reader would see). Registry: `colours.json`. Scratch, scripts and every intermediate file: `/tmp/claude-0/work/colours/batch/` (backup of the registry as it stood before the run: `colours.before-2026-11-01.json`; check outputs: `/tmp/claude-0/work/colours/runs/`).

## What changed

- **1,494 new colours**, every slug of `uncoloured-2026-11-01.csv` (all have a dossier under `polities/`; none is unknown): 221 new `fixed` entries (43 rows of an existing state joining its group, 159 colonies joining their metropole's colonial group, 19 continuity successors with a neighbouring hue) and 1273 new `assigned` wheel colours (171 rebels, 84 cultures, 1018 others).
- **187 existing states recoloured** (48 fixed entries, 139 wheel colours), every one for its whole life and logged; **16 existing fixed entries given a group** (colour unchanged) so a new row of the same state joins them. No change was forced; `rules`, `families` and `wheel` are unchanged.
- `colours.json` now holds 636 fixed entries, 2,402 assigned and 1,715 log entries. It was written only through `colour.save_registry`, one pass at a time (passes 0-fixed, 0-premoves, 0-retry, 1-groups, 2-continuity, 3-rebels, 4-cultures, 5-wheel, 6-clashes, 7-final, 8-legend, 9-duplicates), each re-read from disk first and read back ten seconds after the write; every read-back matched.
- `tools/colour.py`: one small option, noted at the top of the file: `check --relations` skips, per year, pairs in a vassal or constituent relation that year (one side the other's vassal or constituent, or both of one suzerain), read from the `status` key of each `{year, owners}` file; `check --drawn` also skips pairs where one side is drawn wholly in a suzerain's tint that year. A status group whose suzerain is its own owner (a state's own vassal land, drawn in its own tint) is not a relation. Nothing else in the file changed.

## The batch helper

`/tmp/claude-0/work/colours/batch/colourbatch.py` is `colour.py set` for many slugs: it imports colour.py and uses its maths, `pick_colour`-style wheel choice (`variant_for`, best capped margin, least-used hue), `load_registry` and `save_registry`. Each entry is checked like `set` (refused under 0.10 from a lifetime neighbour of another group) and logged like `set` (`date, slug, from, to, note, forced`; `from` is null for a new entry), and each new entry carries a note naming the rule that gave the colour. `set` itself cannot create an entry for a slug with no colour (it exits 'has no colour yet (run assign)'), so the helper creates the `fixed` or `assigned` entry. Its neighbour graph is set's (data/anchors adjacency and the polity table's neighbours) plus the compiled snapshots: `years/` pairs drawn in their own colours, `years-realm/` pairs, and (for the pickers only, not for refusal) pairs that touch while one side is drawn wholly in a third state's tint. It does not count a pair that touches only in a vassal or constituent relation, nor a colony beside its own metropole (`data/colonies.csv`, plus the East India Company beside England and Britain). A pass is saved in one atomic write, so each entry is checked against the registry as it stands after the pass. Plan: `plan.py` (decisions and in-memory colouring), `apply.py` (writes), `clashfix.py`, `manualfix.py` (clash pass), `verify.py`, `report.py`, `notes.py`.

## How each new state got its colour

1. **Same state, split-off row: joins the group.** Read from the dossier's notes, `cliopatria_names` and predecessors ("Split from Cliopatria's single 'Kingdom of Great Britain' row ... at 1801"). United Kingdom joins Great Britain (new group `great-britain`, Britain's pink-red); the Russian SFSR and the sixteen other union republics join the USSR (Soviet deep red; the RSFSR is also the Reds of 1917-22); the Ulus of Jochi, of Chagatai and of Hulegu join the Golden Horde, the Chagatai Khanate and the Ilkhanate (the same states before Cliopatria's 1294 rows); Liu Bang's Kingdom of Han joins the Han; Eastern Zhou joins Zhou; the 21st, 27th, 28th, 29th and 31st dynasties join pharaonic Egypt; the Sultanate of Egypt joins modern Egypt; the Third Saudi State, Royal Hungary and the Second Hungarian Republic, Moravian Serbia, Kartli-Kakheti (Georgia), post-Angkor Cambodia (Khmer), the Stem Duchy of Bavaria, the State of Vietnam (Republic of Vietnam), the Burgundian State (Duchy of Burgundy), the royal domain of France (France), the Kingdom of Denmark 1814-1940 (Denmark), the Second Turkic Khaganate (the Gokturks, a restoration), the East India Company (the British colonial rows), and Zhu Yuanzhang's Wu (the rebel that became the Ming: the Ming's convention is kept).
2. **Colonies: the metropole's colonial colour.** 159 colonies cut from Cliopatria's colonial rows join that row's group (British colonies the British colonial pink, French the French colonial blue, Spanish Spain's, Portuguese, Dutch, German, Swedish, Austrian, Byzantine exarchates, Tang protectorates, Han commanderies, Achaemenid satrapies, Venetian and Genoese colonies, US territories, and so on). The map draws a colony in its metropole's tint while the relation holds; its own colour shows only in the years its status is not set (1,090 snapshot-years over the 159, mostly the first or last year or a change of metropole regime), and then it reads as the metropole's. Colonies with their own identity took a wheel colour or a continuity hue instead: Ireland (Lordship, Kingdom: Irish green), Finland (Grand Duchy), Congress Poland, Wales, the Bukey Horde, Milan, Naples, the Presidi, Nauru, Lelang and Daifang, West Prussia, Danish Estonia and the Greek colonies.
3. **Continuity successors: a neighbouring hue in the family**, the smallest hue turn and lightness change that clears every lifetime neighbour (19): the White Russian State and South Russia (Russia's green), the medieval Kingdom of Italy and the Italian Social Republic, the Later Guptas, the Grand Duchy of Finland, Congress Poland, the Lordship and Kingdom of Ireland, the Tokugawa clan, Bonapartist Spain, the Cossack Hetmanate (Ukraine), Persis (Persia), the state of Medina (the caliphates' green), the Congo Free State (Belgian Congo), Austrasia and Frankish Burgundy (the Franks), the 25th dynasty (Kush) and the Murong Xianbei. Allied-occupied Germany found no neighbouring hue of Germany's slate that clears its neighbours and took a wheel colour.
4. **Rebels: their own hue** (171): the wheel colour with the best margin against every lifetime neighbour and at least 0.15 from the government they fight (their predecessor, else their main neighbour).
5. **Cultures: wheel colours drawn as muted pastels** (84): the map draws `tint(hex, 'culture')` (rules.culture); the pick puts the distance between neighbouring cultures' pastels first, then the full colour's margin.
6. **Everything else: the wheel** (1,018), largest first, preferred lightness by the crowding rule, best margin against every neighbour of its whole life (the lowest margin of a new wheel colour is 0.100).

## Clashes

Before the run (registry of 18 Oct, 1,371 slugs uncoloured): `check --anchors years` 157 distinct pairs below 0.10 (152 with `--relations`, 142 with `--drawn`), `years-realm` 195. With the 1,494 new colours in place: 182 / 152 / 135 and realm 184; the union of the drawn and realm lists was 186 pairs, 12 of them colonies beside their own metropole. Resolved by recolouring the smaller or less conventional state everywhere: 139 wheel states took a new wheel colour, and 48 fixed states or groups moved to the nearest readable colour in their family that clears every lifetime neighbour (list below). Fixed moves outside the family's hue range say so in their note (the Chagatai Khanate, the Indo-Greeks, the Republic of China group, Genoa, Carthage, the Latin Empire, Denmark).

Final numbers (`python3 -I tools/colour.py check ...`):

| folder | option | distinct pairs below 0.10 | year-pairs checked | skipped as relations | same-group (intended) | uncoloured |
| --- | --- | --- | --- | --- | --- | --- |
| years/ | none | 29 | 793657 | 0 | 280 | 0 |
| years/ | --relations | 2 | 667861 | 125796 | 117 | 0 |
| years/ | --drawn | 1 | 504511 | 289146 | 88 | 0 |
| years-realm/ | none | 4 | 569709 | 0 | 128 | 0 |
| data/anchors | none | 0 | 12401 | 0 | 14 | 0 |
| data/anchors-c | none | 17 | 31666 | 0 | 232 | 0 |
| data/anchors-c | --relations | 1 | 25802 | 5864 | 42 | 0 |
| data/anchors-c | --drawn | 0 | 18371 | 13295 | 20 | 0 |

The 27 pairs that `years/` shows without `--relations` and not with it are all a vassal or member touching its own suzerain (or two vassals of one suzerain) while the relation holds, which the map draws in the suzerain's tint; two of them shared one colour exactly (Baden with the Palatinate, Taqali with the Funj) and were separated anyway (pass 9).

Remaining pairs, all colonies or a company beside their own metropole, drawn in one national family on purpose, and one pair that is never drawn:

- french-colony-of-guiana ~ vichy-france, 0.021, 1940..1940 (years_drawn, realm, years_relations): a colony beside its own metropole: in 1940, between its Third Republic row (to 1940) and its Vichy row (from 1941) in data/colonies.csv, French Guiana has no status and is drawn in its own colour, the French colonial blue, beside Vichy France; both read as French, which they were (point 1 of this run: a colony touching its own metropole is not a clash). Setting the colony row for 1940 would draw it in France's tint
- french-indochina ~ vichy-france, 0.021, 1940..1943 (realm): a colony beside its own metropole's realm 1940-1943: Indochina's own protectorate land (status vassal of french-indochina itself) is drawn in the French colonial blue beside the part drawn as Vichy's colony; one French colony by design
- east-india-company ~ kingdom-of-england, 0.027, 1608..1701 (realm): the East India Company (British colonial pink, Cliopatria's British Empire row drew its land) beside land drawn in England's tint 1608-1701; both English by design (the company is listed with England and Britain as its metropoles in the helper)
- kingdom-of-england ~ rupert-s-land, 0.027, 1686..1706 (realm): Rupert's Land, an English colony 1670-1707 (British colonial pink): its strip contested with New France stays its own in the realm view and touches the part drawn as England's colony, 1686-1706; both English by design
- illyrian-provinces ~ kingdom-of-bavaria, 0.048, 1809..1812 (years_relations): never drawn: 1809-1812 both are drawn in a suzerain's tint (the Illyrian Provinces as a French colony, Bavaria as a vassal of the French Empire); both are conventional colours (French colonial blue, Bavarian blue), so neither moves

## Checks

- years: 2424 files, 2950 slugs own cells, 0 without a colour.
- years-realm: 2424 files, 2815 slugs own cells, 0 without a colour.
- data/anchors: 120 files, 1259 slugs own cells, 0 without a colour.
- data/anchors-c: 121 files, 2436 slugs own cells, 0 without a colour.
- Every colour in the registry keeps L 0.40-0.86, at least 0.107 from the neutral grey and 0.18 from a pale basemap (#f4f2ee).
- No two contemporary fixed states of different groups sit under 0.02 (Sokoto at 0.0198 from Saxony, from the seed, was nudged 0.010).

## For the orchestrator

- `colour.py set` cannot add a new slug (it exits when the slug has no colour) although the README says it can; its refusal graph is the Phase A anchors and the polity table's neighbours only, not the compiled years. The helper above covers both; a future run can reuse it.
- The hierarchy leaves the Russian SFSR, the Ukrainian and Byelorussian SSRs, the Moldavian SSR (1940-91) and the Transcaucasian SFSR outside the USSR (no constituent rows in data/hierarchy.csv), so 1922-1991 they are drawn as states beside the USSR. They are in the USSR's group (Soviet red), so the Union still reads as one; adding the constituent rows would draw them in the Union's tint like the other republics.
- 165 slugs carry status groups whose suzerain is the owner itself (a state's own vassal land without a dossier); for some, such as colony-of-jamaica, that is all of its land, and british-honduras is a vassal of colony-of-jamaica. `check --drawn` treats such land as drawn (in the owner's own tint).
- Colonies are drawn in their own colour wherever their colony status is not set: the first or last year, and the year the metropole's regime changes (Portugal 1910 and 1926, France 1940), when the status still points at the previous regime. That is why colonies take their metropole's colonial colour, and why the five remaining pairs exist.
- vichy-france is in group `france` with its own hex (#7899d0, the rest #3e6fc2), as seeded; a group normally shares one colour.
- Conventional colours that moved for the neighbour rule: Denmark (orange-red to the Dannebrog's red, for the Dutch colonial realm), Japan (a hair deeper crimson, for the Ming realm at Ryukyu), the Ilkhanate (brick red, for the Mongol Empire), the Republic of China (deeper blue, for France's realm), Canada and Indonesia (deeper reds, for the United Kingdom's realm), the Chagatai Khanate (pale olive to pale green), the Portuguese colonial rows (a little lighter). Window agents that rendered these re-read the registry at packaging.
- Phase A's `data/anchors` check is clean (0 pairs); `data/anchors-c` shows 17 pairs without the option, 1 with `--relations` and 0 with `--drawn`.

## Full lists

### Changes to existing states (187)

| slug | from | to | kind | reason |
| --- | --- | --- | --- | --- |
| afsharid-iran | #006d91 | #005a7f | fixed | clash with qajar-dynasty 0.055: the Qajars at 0.055 in 1789-1793, when the Afsharid remnant was the smaller state; nearest readable colour in family persia that clears every lifetime neighbour, oklch(0.44 0.094 235), margin 0.113 |
| ashikaga-shogunate | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| asuka-japan | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| avar-khaganate | #2396a9 | #008396 | fixed | clash with gokturk-khaganate 0.090: the Gokturk Khaganate at 0.090 in 561-585; the Avars, the smaller, move; nearest readable colour in family steppe that clears every lifetime neighbour, oklch(0.56 0.098 212), margin 0.106 |
| canada | #bd4238 | #af371f | fixed | clash: beside the United Kingdom's realm (Newfoundland) at 0.083: Canada, the smaller state on that border, deepens its red |
| carthage | #5d57a4 | #5d4f9c | fixed | clash with macedonian-empire 0.080: the Macedonian realm at 0.080 in -404..-322; Carthage, the smaller, moves; nearest readable colour in family near-east (hue outside the family range: nothing inside cleared) that clears every lifetime neighbour, oklch(0.48 0.120 290), margin 0.101 |
| chagatai-khanate | #b3b582 | #8acfaa | fixed | clash with white-horde 0.029, four-oirats 0.068: the Four Oirats (larger) at 0.068 in 1399-1461; nearest readable colour in family mongol (hue outside the family range: nothing inside cleared) that clears every lifetime neighbour, oklch(0.80 0.089 160), margin 0.105 |
| crown-of-aragon | #da7134 | #f17800 | fixed | clash with republic-of-venice 0.070: Venice's realm at 0.070 in 1379-1384; no colour near Venice's clears Venice's neighbours, so Aragon turns a little more orange; nearest readable colour in family iberia that clears every lifetime neighbour, oklch(0.70 0.178 53), margin 0.107 |
| denmark | #d45c36 | #f45055 | fixed | clash: Denmark's realm (Gold Coast forts, Tranquebar, the Danish West Indies) touches the Dutch realm 1658-1940 at 0.039: Denmark, the smaller state, moves from orange-red to the Dannebrog's red (outside the nordic hue range: no Nordic hue clears every neighbour) |
| denmark-norway | #d45c36 | #f45055 | fixed | clash: Denmark's realm (Gold Coast forts, Tranquebar, the Danish West Indies) touches the Dutch realm 1658-1940 at 0.039: Denmark, the smaller state, moves from orange-red to the Dannebrog's red (outside the nordic hue range: no Nordic hue clears every neighbour) |
| despotate-of-epirus | #a581c0 | #d37bc1 | fixed | clash with latin-empire 0.047, nicaean-empire 0.087: the Latin Empire at 0.047 and Nicaea at 0.087; Epirus, the smaller, moves; nearest readable colour in family rome that clears every lifetime neighbour, oklch(0.70 0.139 335), margin 0.109 |
| elam | #377e67 | #096150 | fixed | clash with achaemenid-empire 0.048: the Achaemenid Empire at 0.048 in -550..-542; Elam, the smaller and less conventional, moves; nearest readable colour in family persia that clears every lifetime neighbour, oklch(0.44 0.081 174), margin 0.117 |
| empire-of-china | #2863ab | #234f99 | fixed | clash with french-fourth-republic 0.053, french-third-republic 0.053: France's realm (Indochina, Guangzhouwan) at 0.053 in 1912-1952; France blue is the plan's convention, so the Republic of China's blue moves; nearest readable colour in family china (hue outside the family range: nothing inside cle |
| empire-of-japan | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| first-toungoo-empire | #a89a42 | #cd9300 | fixed | clash with dzungar-khanate 0.058, ai-viet 0.085: the Dzungar Khanate at 0.058 (1717-1719) and Ai Viet's realm at 0.085; Toungoo, the smaller beside the Dzungars, moves; nearest readable colour in family southeast-asia that clears every lifetime neighbour, oklch(0.70 0.145 80), margin 0.110 |
| ghana-empire | #c5772c | #c87434 | fixed | clash with almoravid-dynasty 0.096: the Almoravids at 0.096 in 1054-1055; Ghana, the smaller, moves; nearest readable colour in family africa that clears every lifetime neighbour, oklch(0.64 0.130 55), margin 0.107 |
| heian-japan | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| ilkhanate | #b16148 | #c4464f | fixed | clash: the Ulus of Hulegu (the Ilkhanate before 1294) touches the Mongol Empire 1256-1293 at 0.083: the Ilkhanate, the smaller state, turns its red-brown |
| indo-greeks | #a39cd4 | #b483bf | fixed | clash with greco-bactrian-kingdom 0.036, seleucid-empire 0.093: the Greco-Bactrian Kingdom at 0.036 and the Seleucids at 0.093; the Indo-Greeks, the smaller, move; nearest readable colour in family hellenistic (hue outside the family range: nothing inside cleared) that clears every lifetime neighbou |
| japan | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| kalmar-union | #d45c36 | #f45055 | fixed | clash: Denmark's realm (Gold Coast forts, Tranquebar, the Danish West Indies) touches the Dutch realm 1658-1940 at 0.039: Denmark, the smaller state, moves from orange-red to the Dannebrog's red (outside the nordic hue range: no Nordic hue clears every neighbour) |
| kamakura-shogunate | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| kara-khitans | #6c96c2 | #869ed1 | fixed | clash with great-seljuk-empire 0.063: the Great Seljuks at 0.063 and the Liao at 0.083; the Kara-Khitans, the smaller, move; nearest readable colour in family steppe that clears every lifetime neighbour, oklch(0.70 0.081 265), margin 0.106 |
| kingdom-of-aragon | #da7134 | #f17800 | fixed | clash with republic-of-venice 0.070: Venice's realm at 0.070 in 1379-1384; no colour near Venice's clears Venice's neighbours, so Aragon turns a little more orange; nearest readable colour in family iberia that clears every lifetime neighbour, oklch(0.70 0.178 53), margin 0.107 |
| kingdom-of-denmark | #d45c36 | #f45055 | fixed | clash: Denmark's realm (Gold Coast forts, Tranquebar, the Danish West Indies) touches the Dutch realm 1658-1940 at 0.039: Denmark, the smaller state, moves from orange-red to the Dannebrog's red (outside the nordic hue range: no Nordic hue clears every neighbour) |
| kingdom-of-wessex | #d6778a | #cb5e6e | fixed | clash with anglo-saxon-england 0.046: Anglo-Saxon England at 0.046 in 519-526; Wessex, the smaller, moves; nearest readable colour in family britain that clears every lifetime neighbour, oklch(0.62 0.140 13), margin 0.110 |
| kuomintang | #2863ab | #234f99 | fixed | clash with french-fourth-republic 0.053, french-third-republic 0.053: France's realm (Indochina, Guangzhouwan) at 0.053 in 1912-1952; France blue is the plan's convention, so the Republic of China's blue moves; nearest readable colour in family china (hue outside the family range: nothing inside cle |
| latin-empire | #928fd4 | #857ddd | fixed | clash with sultanate-of-rum 0.063, empire-of-trebizond 0.095: the Sultanate of Rum (realm 1215-1219) at 0.063 and Trebizond at 0.095; the Latin Empire, the smaller, moves; nearest readable colour in family rome (hue outside the family range: nothing inside cleared) that clears every lifetime neighbo |
| liao-dynasty | #6079b0 | #736dc3 | fixed | clash with great-jin 0.063, kara-khitans 0.083: the Jin at 0.063 in 1115-1124 (the Jin, the larger, keep their blue); nearest readable colour in family steppe that clears every lifetime neighbour, oklch(0.58 0.130 285), margin 0.107 |
| majapahit | #b54a46 | #cb4f40 | fixed | clash with ming-dynasty 0.070: the Ming realm at 0.070 in 1405; Majapahit, the smaller, moves; nearest readable colour in family southeast-asia that clears every lifetime neighbour, oklch(0.59 0.160 30), margin 0.112 |
| marinid-sultanate | #9b4630 | #9e212f | fixed | clash with almohad-caliphate 0.039: the Almohad Caliphate at 0.039 in 1244-1268; the Marinids, the smaller, move; nearest readable colour in family islam-west that clears every lifetime neighbour, oklch(0.46 0.159 21), margin 0.106 |
| maurya-empire | #7b63a3 | #7e5a97 | fixed | clash with macedonian-empire 0.087: the Macedonian Empire at 0.087 in -322..-309; the Maurya, the smaller, move; nearest readable colour in family india that clears every lifetime neighbour, oklch(0.53 0.100 310), margin 0.106 |
| nara-japan | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| norway-denmark | #d45c36 | #f45055 | fixed | clash: Denmark's realm (Gold Coast forts, Tranquebar, the Danish West Indies) touches the Dutch realm 1658-1940 at 0.039: Denmark, the smaller state, moves from orange-red to the Dannebrog's red (outside the nordic hue range: no Nordic hue clears every neighbour) |
| portuguese-africa | #50a064 | #47a962 | fixed | clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado Novo) at 0.091: the colonial rows and colonies touch Portugal itself in the years their status points at the previous regime (1910, 1926) and through Portuguese Morocco 1458-1506; the colonial group, the less conventional of t |
| portuguese-ceylon | #50a064 | #47a962 | fixed | clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado Novo) at 0.091: the colonial rows and colonies touch Portugal itself in the years their status points at the previous regime (1910, 1926) and through Portuguese Morocco 1458-1506; the colonial group, the less conventional of t |
| portuguese-colonies | #50a064 | #47a962 | fixed | clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado Novo) at 0.091: the colonial rows and colonies touch Portugal itself in the years their status points at the previous regime (1910, 1926) and through Portuguese Morocco 1458-1506; the colonial group, the less conventional of t |
| portuguese-empire | #50a064 | #47a962 | fixed | clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado Novo) at 0.091: the colonial rows and colonies touch Portugal itself in the years their status points at the previous regime (1910, 1926) and through Portuguese Morocco 1458-1506; the colonial group, the less conventional of t |
| republic-of-china | #2863ab | #234f99 | fixed | clash with french-fourth-republic 0.053, french-third-republic 0.053: France's realm (Indochina, Guangzhouwan) at 0.053 in 1912-1952; France blue is the plan's convention, so the Republic of China's blue moves; nearest readable colour in family china (hue outside the family range: nothing inside cle |
| republic-of-genoa | #c67164 | #ab5a47 | fixed | clash with republic-of-venice 0.024, crown-of-aragon 0.061: Venice at 0.024 (1365-1384) and Aragon at 0.061; Genoa, the smaller, moves; nearest readable colour in family italy (hue outside the family range: nothing inside cleared) that clears every lifetime neighbour, oklch(0.56 0.110 35), margin 0. |
| republic-of-indonesia | #b2354a | #b42228 | fixed | clash: beside the United Kingdom's realm (British Borneo and Malaya) at 0.073: Indonesia deepens its red |
| rouran-khaganate | #715c95 | #5b5e8b | fixed | clash with liu-song-dynasty 0.082, western-jin 0.092: the Western Jin realm at 0.092 (402-419); the Rouran, the smaller, move; nearest readable colour in family steppe that clears every lifetime neighbour, oklch(0.50 0.071 280), margin 0.106 |
| second-bulgarian-empire | #b85e31 | #ca4d16 | fixed | clash with mongol-empire 0.087, republic-of-venice 0.093: the Mongol Empire at 0.087 (1240-1284) and Venice's realm; Bulgaria, the smaller, moves; nearest readable colour in family balkans that clears every lifetime neighbour, oklch(0.58 0.170 40), margin 0.110 |
| shu-han | #b84455 | #9b494c | fixed | clash with han-dynasty 0.068: the Han dynasty at 0.068 in the succession year 219; Shu Han, the continuity successor, moves further; nearest readable colour in family china that clears every lifetime neighbour, oklch(0.51 0.110 20), margin 0.111 |
| sokoto-caliphate | #519160 | #519465 | fixed | legend: 0.0198 from the Electorate and Kingdom of Saxony (contemporary, never neighbours), under the 0.02 the seed warns at; nudged 0.010 to keep 0.025 from every contemporary fixed colour |
| tokugawa-shogunate | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| warring-states-japan | #8e2b6b | #8d1768 | fixed | clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the smaller, moves as little as it can; nearest readable colour in family japan that clears every lifetime neighbour, oklch(0.44 0.170 345), margin 0.112 |
| west-franks | #4a76ae | #3d4e89 | fixed | clash: beside the Kingdom of France and its royal domain in the succession year 987-988 at 0.042: West Francia, the predecessor, takes a deeper indigo in the French family |
| afghanistan | #69a1e8 | #4fa8e1 | wheel | clash with mujahideen at 0.092 in years 1979..1986, realm 1979..1986: wheel h240-mid, best margin against every lifetime neighbour |
| ahi-republic | #bb584a | #736dc3 | wheel | clash with ulus-of-hulegu (realm) at 0.040: wheel h285-deep, best margin against every lifetime neighbour |
| alodia | #009068 | #0c82bf | wheel | clash with fatimid-caliphate at 0.038 in realm 970..1169: wheel h240-deep, best margin against every lifetime neighbour |
| aquitaine | #09b2c7 | #008a9b | wheel | clash with middle-franks at 0.061 in years 843..854, realm 843..854: wheel h210-deep, best margin against every lifetime neighbour |
| atropatene | #578b35 | #a45b9f | wheel | clash with parthian-empire at 0.097 in years -148..-66, realm -148..222: wheel h330-deep, best margin against every lifetime neighbour |
| au-lac | #ba5661 | #8766bb | wheel | clash with han-dynasty at 0.059 in realm -196..-184: wheel h300-deep, best margin against every lifetime neighbour |
| bahmani-sultanate | #967600 | #95a94e | wheel | clash with tughlaq-dynasty at 0.099 in years 1347..1393, realm 1347..1393: wheel h120-mid, best margin against every lifetime neighbour |
| beylik-of-isfendiyar | #bb9b39 | #b5c87d | wheel | clash with mamluk-sultanate at 0.063 in realm 1440..1460: wheel h120-light, best margin against every lifetime neighbour |
| bijapur-sultanate | #69a1e8 | #70ccee | wheel | clash with french-india at 0.022 in years 1673..1685: wheel h225-light, best margin against every lifetime neighbour |
| capetian-house-of-anjou | #c7c274 | #6dd3c0 | wheel | clash with papal-states at 0.021 in realm 1274..1381: wheel h180-light, best margin against every lifetime neighbour |
| carantania | #ca933e | #09b2c7 | wheel | clash with first-bulgarian-empire at 0.047 in years 827..827: wheel h210-mid, best margin against every lifetime neighbour |
| chandela-kingdom | #00b5b5 | #e3a6dd | wheel | clash with chauhan-dynasty at 0.000 in years 960..1055, realm 960..1055: wheel h330-light, best margin against every lifetime neighbour |
| chobanids | #dc855d | #df7e86 | wheel | clash with golden-horde at 0.078 in years 1356..1356, realm 1356..1356: wheel h015-mid, best margin against every lifetime neighbour |
| cimmerian-bosporus | #bb584a | #9760af | wheel | clash with roman-republic at 0.041 in years -48..-48, realm -48..-48: wheel h315-deep, best margin against every lifetime neighbour |
| colchis | #0087ab | #65d2d2 | wheel | clash with seleucid-empire at 0.087 in realm -212..-189: wheel h195-light, best margin against every lifetime neighbour |
| county-of-bearn | #c882c2 | #6dd3c0 | wheel | clash with kingdom-of-england at 0.060 in years 1347..1378: wheel h180-light, best margin against every lifetime neighbour |
| county-of-besalu | #dc855d | #ba87d2 | wheel | clash with county-of-osona at 0.000 in years 879..1110, realm 879..1110: wheel h315-mid, best margin against every lifetime neighbour |
| county-of-flanders | #a45b9f | #ba5661 | wheel | clash with burgundian-state (drawn/realm) at 0.081: wheel h015-deep, best margin against every lifetime neighbour |
| county-of-foix | #7daf61 | #f7a3a9 | wheel | clash with angevin-empire at 0.031 in years 1152..1208, realm 1152..1208: wheel h015-light, best margin against every lifetime neighbour |
| county-of-toulouse | #30add6 | #008e7d | wheel | clash with kingdom-of-arles at 0.000 in years 1065..1214: wheel h180-deep, best margin against every lifetime neighbour |
| cuman-kipchak-confederation | #9760af | #f4a988 | wheel | clash with kingdom-of-hungary at 0.032 in years 1227..1240, realm 1227..1240: wheel h045-light, best margin against every lifetime neighbour |
| cyrenaica | #bb584a | #c882c2 | wheel | clash with roman-republic at 0.041 in realm -109..-100: wheel h330-mid, best margin against every lifetime neighbour |
| dai | #dc855d | #f3a3bb | wheel | clash with qi at 0.031 in years -208..-207, realm -208..-207: wheel h000-light, best margin against every lifetime neighbour |
| dominican-republic | #b65577 | #a46e00 | wheel | clash with haiti at 0.000 in years 1844..1934, realm 1844..1934: wheel h075-deep, best margin against every lifetime neighbour |
| don-cossacks | #aa8dde | #69a1e8 | wheel | clash with nogai-horde at 0.062 in years 1572..1641, realm 1572..1641: wheel h255-mid, best margin against every lifetime neighbour |
| duchy-of-aquitaine | #63b376 | #867d00 | wheel | clash with angevin-empire at 0.000 in years 1204..1208, realm 1204..1208: wheel h105-deep, best margin against every lifetime neighbour |
| duchy-of-greater-poland | #aaa23f | #0c82bf | wheel | clash with ulus-of-jochi (realm) at 0.058: wheel h240-deep, best margin against every lifetime neighbour |
| duchy-of-legnica | #c7aff5 | #dc855d | wheel | clash with margraviate-of-brandenburg at 0.052 in years 1262..1290, realm 1262..1290: wheel h045-mid, best margin against every lifetime neighbour |
| duchy-of-mecklenburg | #46b68c | #a2cd8b | wheel | clash with holy-roman-empire-minor-states at 0.000 in years 1805..1805, realm 1805..1805: wheel h135-light, best margin against every lifetime neighbour |
| duchy-of-oldenburg | #a4bbff | #c7aff5 | wheel | clash with duchy-of-holstein at 0.052 in years 1863..1865, realm 1806..1865: wheel h300-light, best margin against every lifetime neighbour |
| duchy-of-raciborz | #d37faf | #e3a6dd | wheel | clash with kingdom-of-poland at 0.042 in years 1305..1448, realm 1305..1448: wheel h330-light, best margin against every lifetime neighbour |
| duchy-of-spoleto | #09b2c7 | #f3a3bb | wheel | clash with middle-franks at 0.061 in years 843..854, realm 843..854: wheel h000-light, best margin against every lifetime neighbour |
| early-balinese-kingdoms | #718516 | #578b35 | wheel | clash with mataram-kingdom at 0.097 in realm 990..1015: wheel h135-deep, best margin against every lifetime neighbour |
| eastern-kara-khanids | #718516 | #348f4f | wheel | clash with ghaznavid-empire at 0.084 in years 1045..1045, realm 1045..1045: wheel h150-deep, best margin against every lifetime neighbour |
| eshrefids | #bb584a | #df8071 | wheel | clash with ulus-of-hulegu (realm) at 0.040: wheel h030-mid, best margin against every lifetime neighbour |
| first-sealand-dynasty | #348f4f | #dc855d | wheel | clash with elam at 0.071 in years -1732..-1500, realm -1732..-1500: wheel h045-mid, best margin against every lifetime neighbour |
| former-shu | #bb9b39 | #30add6 | wheel | clash with later-tang at 0.025 in years 923..924, realm 923..924: wheel h225-mid, best margin against every lifetime neighbour |
| free-city-of-hamburg | #5d74c7 | #e4b572 | wheel | clash with first-french-empire at 0.040 in years 1809..1809, realm 1809..1809: wheel h075-light, best margin against every lifetime neighbour |
| free-county-of-burgundy | #c7c274 | #a2cd8b | wheel | clash with county-of-champagne at 0.052 in years 990..1259, realm 990..1259: wheel h135-light, best margin against every lifetime neighbour |
| gahadavala-dynasty | #867d00 | #df8071 | wheel | clash with ghaznavid-empire at 0.051 in years 1104..1108, realm 1104..1108: wheel h030-mid, best margin against every lifetime neighbour |
| giudicato-of-cagliari | #aaa23f | #ba87d2 | wheel | clash with republic-of-pisa at 0.000 in realm 1256..1257: wheel h315-mid, best margin against every lifetime neighbour |
| grand-duchy-of-tuscany | #7daf61 | #f7a3a9 | wheel | clash with holy-roman-empire-minor-states at 0.062 in years 1737..1800, realm 1737..1800: wheel h015-light, best margin against every lifetime neighbour |
| grand-duchy-of-wurzburg | #7daf61 | #718516 | wheel | clash with holy-roman-empire-minor-states at 0.062 in years 1805..1805, realm 1805..1805: wheel h120-deep, best margin against every lifetime neighbour |
| greek-colonies | #46b68c | #c7aff5 | wheel | clash with antigonid-dynasty at 0.000 in years -271..-227, realm -271..-227: wheel h300-light, best margin against every lifetime neighbour |
| gurjara-pratihara-dynasty | #95a94e | #ca933e | wheel | clash with umayyad-caliphate at 0.070 in years 730..742, realm 730..742: wheel h075-mid, best margin against every lifetime neighbour |
| harsha-s-empire | #967600 | #8766bb | wheel | clash with tibetan-empire at 0.031 in realm 618..646: wheel h300-deep, best margin against every lifetime neighbour |
| honduras | #4fa8e1 | #92c1fd | wheel | clash with united-provinces-of-central-america at 0.062 in years 1838..1838, realm 1838..1838: wheel h255-light, best margin against every lifetime neighbour |
| house-of-ascania | #da7d9b | #aaa23f | wheel | clash with kingdom-of-poland at 0.045 in years 1319..1323, realm 1319..1323: wheel h105-mid, best margin against every lifetime neighbour |
| house-of-jagiellon | #008a9b | #008e7d | wheel | clash with kingdom-of-sweden at 0.056 in years 1561..1563, realm 1561..1568: wheel h180-deep, best margin against every lifetime neighbour (SHORT) |
| hyderabad-state | #63b376 | #aaa23f | wheel | clash with nawabs-of-bengal at 0.031 in years 1724..1751, realm 1724..1751: wheel h105-mid, best margin against every lifetime neighbour |
| indo-parthians | #df7e86 | #dc855d | wheel | clash with eastern-kushans at 0.093 in years 225..225, realm 225..225: wheel h045-mid, best margin against every lifetime neighbour |
| itza-mayans | #9760af | #00b5b5 | wheel | clash with later-mayan-city-states at 0.100 in years 1441..1545, realm 1441..1545: wheel h195-mid, best margin against every lifetime neighbour |
| jamaica | #ba5661 | #5d74c7 | wheel | clash with united-kingdom (realm) at 0.048: wheel h270-deep, best margin against every lifetime neighbour |
| janapada-of-pancala | #578b35 | #407bc5 | wheel | clash with magadha-haryanka-dynasty at 0.000 in years -451..-418, realm -451..-418: wheel h255-deep, best margin against every lifetime neighbour |
| janapada-of-surasena | #008a9b | #718516 | wheel | clash with magadha-shaishunaga-dynasty at 0.026 in years -350..-346, realm -350..-346: wheel h120-deep, best margin against every lifetime neighbour |
| kalinga | #348f4f | #008c8c | wheel | clash with shunga-empire at 0.098 in years -185..-175, realm -185..-175: wheel h195-deep, best margin against every lifetime neighbour |
| kampili-kingdom | #bb9b39 | #24b6a1 | wheel | clash with yadava-dynasty at 0.064 in years 1285..1316, realm 1285..1316: wheel h180-mid, best margin against every lifetime neighbour |
| khmer-rouge | #00b5b5 | #30add6 | wheel | clash with kingdom-of-cambodia at 0.091 in years 1975..1978, realm 1975..1978: wheel h225-mid, best margin against every lifetime neighbour |
| kingdom-of-bahrain | #407bc5 | #967600 | wheel | clash with state-of-qatar at 0.034 in years 2001..2026, realm 2001..2026: wheel h090-deep, best margin against every lifetime neighbour |
| kingdom-of-bernicia | #63b376 | #30add6 | wheel | clash with kingdom-of-mercia at 0.031 in years 604..610, realm 604..610: wheel h225-mid, best margin against every lifetime neighbour |
| kingdom-of-bohemia | #d58b4b | #b85e31 | wheel | clash with ulus-of-jochi (realm) at 0.049: wheel h045-deep, best margin against every lifetime neighbour |
| kingdom-of-commagene | #80c7f8 | #d6aaea | wheel | clash with greek-city-states at 0.029 in years -144..-78, realm -144..-78: wheel h315-light, best margin against every lifetime neighbour |
| kingdom-of-etruria | #00b5b5 | #a4bbff | wheel | clash with cisalpine-republic at 0.063 in years 1801..1801, realm 1801..1801: wheel h270-light, best margin against every lifetime neighbour |
| kingdom-of-fiji | #af578c | #5d74c7 | wheel | clash with united-kingdom (realm) at 0.049: wheel h270-deep, best margin against every lifetime neighbour |
| kingdom-of-jordan | #7daf61 | #c7c274 | wheel | clash with kingdom-of-hejaz at 0.062 in years 1920..1921, realm 1920..1921: wheel h105-light, best margin against every lifetime neighbour |
| kingdom-of-kakheti | #7daf61 | #aaa23f | wheel | clash with zand-dynasty at 0.078 in realm 1760..1761: wheel h105-mid, best margin against every lifetime neighbour |
| kingdom-of-kent | #aa8dde | #d7bb70 | wheel | clash with brythons at 0.000 in years 455..479, realm 455..479: wheel h090-light, best margin against every lifetime neighbour |
| kingdom-of-laos | #30add6 | #f7a597 | wheel | clash with french-indochina at 0.068 in realm 1953..1953: wheel h030-light, best margin against every lifetime neighbour |
| kingdom-of-libya | #a45b9f | #9760af | wheel | clash with united-kingdom (realm) at 0.082: wheel h315-deep, best margin against every lifetime neighbour |
| kingdom-of-lindsey | #ba87d2 | #aa8dde | wheel | clash with anglo-saxon-england at 0.098 in years 450..526, realm 450..526: wheel h300-mid, best margin against every lifetime neighbour |
| kingdom-of-mrauk-u | #8766bb | #e4b572 | wheel | clash with sultanate-of-bengal at 0.000 in years 1429..1533, realm 1429..1537: wheel h075-light, best margin against every lifetime neighbour |
| kingdom-of-osroene | #9793e6 | #d37faf | wheel | clash with seleucid-empire at 0.094 in years -132..-65, realm -132..-65: wheel h345-mid, best margin against every lifetime neighbour |
| kingdom-of-pajana | #df7e86 | #b85e31 | wheel | clash with mataram-sultanate at 0.093 in years 1584..1585, realm 1584..1585: wheel h045-deep, best margin against every lifetime neighbour |
| kingdom-of-pamplona | #00b5b5 | #6dd3c0 | wheel | clash with aquitaine at 0.031 in years 845..894, realm 845..894: wheel h180-light, best margin against every lifetime neighbour |
| kingdom-of-powys | #00b5b5 | #09b2c7 | wheel | clash with angevin-empire at 0.091 in years 1154..1159, realm 1154..1159: wheel h210-mid, best margin against every lifetime neighbour |
| kingdom-of-sicily | #df8071 | #8766bb | wheel | clash with hammadid-dynasty at 0.091 in realm 1148..1151: wheel h300-deep, best margin against every lifetime neighbour |
| kingdom-of-syrmia | #d58b4b | #69a1e8 | wheel | clash with golden-horde at 0.049 in realm 1294..1323: wheel h255-mid, best margin against every lifetime neighbour |
| kuwait | #b85e31 | #407bc5 | wheel | clash with muhammad-ali-dynasty at 0.065 in years 1831..1839: wheel h255-deep, best margin against every lifetime neighbour |
| lazica | #69a1e8 | #f7a597 | wheel | clash with western-gokturks at 0.050 in years 627..629, realm 627..629: wheel h030-light, best margin against every lifetime neighbour |
| mahameghavahana-dynasty | #008e7d | #0c82bf | wheel | clash with kanva-dynasty at 0.066 in years -73..-30, realm -73..-30: wheel h240-deep, best margin against every lifetime neighbour |
| mahdist-state | #b16512 | #c7aff5 | wheel | clash with turco-egyptian-sudan (drawn/hidden/realm) at 0.062: wheel h300-light, best margin against every lifetime neighbour |
| nabhani-dynasty | #008a9b | #bb584a | wheel | clash with safavid-dynasty at 0.021 in years 1622..1623, realm 1622..1623: wheel h030-deep, best margin against every lifetime neighbour |
| nayaks-of-madurai | #b16512 | #9793e6 | wheel | clash with dutch-republic at 0.043 in realm 1661..1666: wheel h285-mid, best margin against every lifetime neighbour |
| new-caledonia | #4fa8e1 | #009068 | wheel | clash with french-indochina at 0.042 in years 1940..1940: wheel h165-deep, best margin against every lifetime neighbour |
| nguyen-lords | #aa8dde | #e3a6dd | wheel | clash with tay-son-dynasty at 0.031 in years 1771..1774, realm 1771..1774: wheel h330-light, best margin against every lifetime neighbour |
| odrysian-kingdom | #da7d9b | #24b6a1 | wheel | clash with kingdom-of-lysimachus at 0.000 in years -313..-313, realm -313..-313: wheel h180-mid, best margin against every lifetime neighbour |
| paramara-dynasty | #819ae9 | #f7a597 | wheel | clash with rashtrakuta-dynasty at 0.037 in years 948..972, realm 948..972: wheel h030-light, best margin against every lifetime neighbour |
| patriarchate-of-aquileia | #c882c2 | #008e7d | wheel | clash with holy-roman-empire at 0.079 in years 1251..1258, realm 1251..1258: wheel h180-deep, best margin against every lifetime neighbour |
| people-s-republic-of-kampuchea | #24b6a1 | #4fa8e1 | wheel | clash with kingdom-of-cambodia at 0.062 in years 1991..1992, realm 1991..1992: wheel h240-mid, best margin against every lifetime neighbour |
| principality-of-beloozero | #bb9b39 | #7daf61 | wheel | clash with golden-horde at 0.032 in realm 1294..1342: wheel h135-mid, best margin against every lifetime neighbour |
| principality-of-galicia-volhynia | #dc855d | #d6aaea | wheel | clash with ulus-of-jochi (realm) at 0.078: wheel h315-light, best margin against every lifetime neighbour |
| principality-of-pinsk | #f7a3a9 | #df7e86 | wheel | clash with principality-of-galicia-volhynia (drawn/hidden/realm) at 0.100: wheel h015-mid, best margin against every lifetime neighbour |
| principality-of-polotsky | #30add6 | #e4b572 | wheel | clash with grand-duchy-of-lithuania at 0.052 in realm 1240..1306: wheel h075-light, best margin against every lifetime neighbour |
| principality-of-regensberg | #f3a3bb | #b65577 | wheel | clash with duchy-of-nassau at 0.026 in years 1806..1808, realm 1806..1808: wheel h000-deep, best margin against every lifetime neighbour |
| principality-of-salerno | #9793e6 | #70ccee | wheel | clash with holy-roman-empire at 0.068 in realm 1043..1046: wheel h225-light, best margin against every lifetime neighbour |
| principality-of-schwarzburg-sonderhausen | #578b35 | #9760af | wheel | clash with electorate-of-saxony at 0.043 in years 1599..1805, realm 1599..1805: wheel h315-deep, best margin against every lifetime neighbour |
| principality-of-turov-and-pinsk | #09b2c7 | #8ed09c | wheel | clash with grand-duchy-of-lithuania at 0.023 in years 1236..1292, realm 1236..1292: wheel h150-light, best margin against every lifetime neighbour |
| principality-of-vitebsk | #ca933e | #09b2c7 | wheel | clash with principality-of-kiev at 0.091 in years 1116..1139, realm 1116..1139: wheel h210-mid, best margin against every lifetime neighbour |
| qi | #d58b4b | #718516 | wheel | clash with zhou-dynasty at 0.064 in years -1046..-753, realm -1046..-753; zhou-dynasty at 0.094 in rescan 0..0: wheel h120-deep, best margin against every lifetime neighbour |
| republic-of-amalfi | #46b68c | #95a94e | wheel | clash with norman-italy at 0.061 in years 1076..1129, realm 1076..1129: wheel h120-mid, best margin against every lifetime neighbour |
| republic-of-costa-rica | #30add6 | #e4b572 | wheel | clash with united-provinces-of-central-america at 0.032 in years 1838..1838, realm 1838..1838: wheel h075-light, best margin against every lifetime neighbour |
| republic-of-san-marino | #ba87d2 | #008a9b | wheel | clash with italian-republic at 0.032 in years 1802..1813, realm 1802..1813: wheel h210-deep, best margin against every lifetime neighbour |
| republic-of-the-congo | #95a94e | #df7e86 | wheel | clash with portuguese-angola at 0.087 in years 1960..1974: wheel h015-mid, best margin against every lifetime neighbour |
| rhodes | #b65577 | #a45b9f | wheel | clash with roman-republic at 0.075 in years -164..-40, realm -168..-40: wheel h330-deep, best margin against every lifetime neighbour |
| ripuarian-franks | #63b376 | #c7c274 | wheel | clash with ostrogothic-kingdom at 0.000 in realm 500..508: wheel h105-light, best margin against every lifetime neighbour |
| samanid-empire | #009068 | #d7bb70 | wheel | clash with fatimid-caliphate at 0.038 in realm 909..998: wheel h090-light, best margin against every lifetime neighbour |
| samudera-pasai-sultanate | #008e7d | #967600 | wheel | clash with portuguese-empire at 0.085 in years 1521..1523, realm 1521..1523: wheel h090-deep, best margin against every lifetime neighbour |
| scythia | #008c8c | #ba5661 | wheel | clash with median-kingdom at 0.082 in years -615..-601, realm -615..-601: wheel h015-deep, best margin against every lifetime neighbour |
| singhasari | #0087ab | #9760af | wheel | clash with srivijaya at 0.042 in years 1277..1291, realm 1290..1291: wheel h315-deep, best margin against every lifetime neighbour |
| sloboda-ukraine | #df7e86 | #d58b4b | wheel | clash with polish-lithuanian-commonwealth at 0.068 in years 1650..1652: wheel h060-mid, best margin against every lifetime neighbour |
| southern-han | #7daf61 | #09b2c7 | wheel | clash with later-zhou at 0.063 in realm 958..959: wheel h210-mid, best margin against every lifetime neighbour |
| southern-liang | #ca933e | #f7a597 | wheel | clash with northern-liang at 0.000 in years 402..413, realm 402..413: wheel h030-light, best margin against every lifetime neighbour |
| southern-tang | #736dc3 | #6dd3c0 | wheel | clash with liao-dynasty at 0.054 in years 947..950, realm 937..950: wheel h180-light, best margin against every lifetime neighbour |
| sultanate-of-aceh | #9760af | #736dc3 | wheel | clash with ayutthaya-kingdom at 0.076 in realm 1620..1628: wheel h285-deep, best margin against every lifetime neighbour |
| sultanate-of-banten | #ba87d2 | #63b376 | wheel | clash with british-bencoolen (drawn/hidden/realm) at 0.099: wheel h150-mid, best margin against every lifetime neighbour |
| sultanate-of-bengal | #8766bb | #ba87d2 | wheel | clash with vijayanagara-empire at 0.053 in realm 1515..1530: wheel h315-mid, best margin against every lifetime neighbour |
| sultanate-of-darfur | #8766bb | #6dd3c0 | wheel | clash with empire-of-kanem at 0.067 in realm 1636..1838: wheel h180-light, best margin against every lifetime neighbour |
| sultanate-of-gowa | #967600 | #af578c | wheel | clash with balinese-kingdom at 0.031 in years 1626..1666, realm 1626..1666: wheel h345-deep, best margin against every lifetime neighbour |
| sultanate-of-jambi | #a45b9f | #da7d9b | wheel | clash with sultanate-of-aceh at 0.033 in realm 1609..1665: wheel h000-mid, best margin against every lifetime neighbour |
| sultanate-of-kedah | #aaa23f | #80c7f8 | wheel | clash with first-toungoo-empire at 0.023 in realm 1564..1583: wheel h240-light, best margin against every lifetime neighbour |
| sultanate-of-oman | #967600 | #a2cd8b | wheel | clash with ottoman-empire at 0.059 in realm 1818..1879: wheel h135-light, best margin against every lifetime neighbour |
| sultanate-of-sambaliung | #718516 | #df8071 | wheel | clash with kingdom-of-bulungan at 0.000 in years 1810..1833: wheel h030-mid, best margin against every lifetime neighbour |
| sultanate-of-sulu | #a45b9f | #8766bb | wheel | clash with united-kingdom (realm) at 0.082: wheel h300-deep, best margin against every lifetime neighbour |
| swaziland | #bb9b39 | #aaa23f | wheel | clash with south-africa at 0.092 in years 1968..2026, realm 1968..2026: wheel h105-mid, best margin against every lifetime neighbour |
| taifa-of-algeciras | #8ed09c | #65d2d2 | wheel | clash with caliphate-of-cordoba at 0.056 in years 1013..1025, realm 1013..1025: wheel h195-light, best margin against every lifetime neighbour |
| taifa-of-almeria | #8ed09c | #dc855d | wheel | clash with caliphate-of-cordoba at 0.056 in years 1012..1014, realm 1012..1014: wheel h045-mid, best margin against every lifetime neighbour |
| taifa-of-seville | #d37faf | #b65577 | wheel | clash with kingdom-of-leon at 0.064 in years 1056..1065, realm 1056..1065: wheel h000-deep, best margin against every lifetime neighbour |
| taifa-of-silves | #9793e6 | #92c1fd | wheel | clash with kingdom-of-leon at 0.061 in years 1055..1062, realm 1055..1062: wheel h255-light, best margin against every lifetime neighbour |
| taifa-of-tejada | #df7e86 | #00b5b5 | wheel | clash with taifa-of-niebla at 0.061 in years 1146..1149, realm 1146..1149: wheel h195-mid, best margin against every lifetime neighbour |
| tibetans | #a45b9f | #736dc3 | wheel | clash with pala-empire at 0.032 in realm 842..849: wheel h285-deep, best margin against every lifetime neighbour |
| tuyuhun | #63b376 | #6dd3c0 | wheel | clash with later-zhao at 0.000 in realm 330..350: wheel h180-light, best margin against every lifetime neighbour |
| tver | #bb9b39 | #d7bb70 | wheel | clash with golden-horde at 0.032 in realm 1294..1479: wheel h090-light, best margin against every lifetime neighbour |
| visigoths | #009068 | #967600 | wheel | clash with alans at 0.060 in years 417..417, realm 417..417: wheel h090-deep, best margin against every lifetime neighbour |
| wei | #7daf61 | #6dd3c0 | wheel | clash with chu at 0.062 in years -403..-224, realm -403..-224: wheel h180-light, best margin against every lifetime neighbour |
| western-liang | #69a1e8 | #7daf61 | wheel | clash with later-liang at 0.062 in years 400..401, realm 400..401: wheel h135-mid, best margin against every lifetime neighbour |
| western-qin | #30add6 | #46b68c | wheel | clash with northern-wei at 0.090 in years 427..429, realm 427..429: wheel h165-mid, best margin against every lifetime neighbour |
| wey | #f3a3bb | #b65577 | wheel | clash with han at 0.025 in years -375..-231, realm -375..-231: wheel h000-deep, best margin against every lifetime neighbour |
| zambia | #95a94e | #aaa23f | wheel | clash with portuguese-angola at 0.087 in years 1964..1974: wheel h105-mid, best margin against every lifetime neighbour |
| zhongshan | #ba87d2 | #b65577 | wheel | clash with zhao at 0.061 in years -350..-297, realm -350..-297: wheel h000-deep, best margin against every lifetime neighbour |

### Existing fixed entries given a group (16, colour unchanged)

- kingdom-of-great-britain: group great-britain (group great-britain added (colour unchanged): united-kingdom joins as the same state)
- kingdom-of-georgia: group georgia (group georgia added (colour unchanged): kingdom-of-kartli-kakheti joins as the same state)
- khmer-empire: group khmer (group khmer added (colour unchanged): post-angkor-cambodia joins as the same state)
- golden-horde: group golden-horde (group golden-horde added (colour unchanged): ulus-of-jochi joins as the same state)
- chagatai-khanate: group chagatai (group chagatai added (colour unchanged): ulus-of-chagatai joins as the same state)
- ilkhanate: group ilkhanate (group ilkhanate added (colour unchanged): ulus-of-hulegu joins as the same state)
- zhou-dynasty: group zhou (group zhou added (colour unchanged): eastern-zhou joins as the same state)
- eastern-gokturks: group gokturk (group gokturk added (colour unchanged): second-turkic-khaganate joins as the same state)
- republic-of-vietnam: group south-vietnam (group south-vietnam added (colour unchanged): state-of-vietnam joins as the same state)
- duchy-of-burgundy: group burgundy (group burgundy added (colour unchanged): burgundian-state joins as the same state)
- tang-dynasty: group tang (group tang added (colour unchanged): protectorate-general-to-pacify-the-west joins as the same state)
- liao-dynasty: group liao (group liao added (colour unchanged): dongdan joins as the same state)
- achaemenid-empire: group achaemenid (group achaemenid added (colour unchanged): hindush joins as the same state)
- republic-of-venice: group venice (group venice added (colour unchanged): venetian-dalmatia joins as the same state)
- united-states-of-america: group usa (group usa added (colour unchanged): united-states-army-military-government-in-korea joins as the same state)
- republic-of-genoa: group genoa (group genoa added (colour unchanged): maona-of-chios joins as the same state)

### New fixed entries (221)

| slug | hex | family | group | rule | note |
| --- | --- | --- | --- | --- | --- |
| gandara | #008287 | persia | achaemenid | colony-group | new state: split-off row / same state as achaemenid-empire (colony of achaemenid-empire,; Cliopatria drew this land in its colonial row); joins group achaemenid |
| hindush | #008287 | persia | achaemenid | colony-group | new state: split-off row / same state as achaemenid-empire (colony of achaemenid-empire,; Cliopatria drew this land in its colonial row); joins group achaemenid |
| yehud-medinata | #008287 | persia | achaemenid | colony-group | new state: split-off row / same state as achaemenid-empire (colony of achaemenid-empire; Cliopatria drew this land in its colonial row); joins group achaemenid |
| banat-of-temeswar | #be3d70 | austria | austria | colony-group | new state: split-off row / same state as habsburg-monarchy (colony of habsburg-monarchy; Cliopatria drew this land in its colonial row); joins group austria |
| habsburg-military-frontier | #be3d70 | austria | austria | colony-group | new state: split-off row / same state as habsburg-monarchy (colony of habsburg-monarchy,austrian-empire,austria-hungary; Cliopatria drew this land in its colonial row); joins group austria |
| kingdom-of-galicia-and-lodomeria | #be3d70 | austria | austria | colony-group | new state: split-off row / same state as habsburg-monarchy (colony of habsburg-monarchy,austrian-empire,austria-hungary; Cliopatria drew this land in its colonial row); joins group austria |
| kingdom-of-serbia-1718-1739 | #be3d70 | austria | austria | colony-group | new state: split-off row / same state as habsburg-monarchy (colony of habsburg-monarchy; Cliopatria drew this land in its colonial row); joins group austria |
| ruanda-urundi | #b8a636 | france | belgium | colony-group | new state: split-off row / same state as belgian-congo (colony of kingdom-of-belgium; Cliopatria drew this land in its colonial row); joins group belgium |
| aden-protectorate | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| anglo-corsican-kingdom | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain; Cliopatria drew this land in its colonial row); joins group british-empire |
| anglo-egyptian-sudan | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-bechuanaland | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-bencoolen | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-england,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-burma | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-cameroons | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-east-florida | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-guiana | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-honduras | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-kaffraria | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-new-guinea | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-north-borneo | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-solomon-islands-protectorate | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-south-africa-company | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-togoland | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| british-west-florida | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-and-protectorate-of-nigeria | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-british-columbia | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-cape-breton-island | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-fiji | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-jamaica | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of commonwealth-of-england,kingdom-of-england,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-labuan | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-natal | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-new-brunswick | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-new-south-wales | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-new-zealand | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-norfolk-island | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-nova-scotia | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-prince-edward-island | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-queensland | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-south-australia | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-tasmania | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-vancouver-island | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-victoria | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| colony-of-western-australia | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| dominion-of-newfoundland | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-england,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| falkland-islands | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| federated-malay-states | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| gibraltar | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-england,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| gilbert-and-ellice-islands | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| imperial-british-east-africa-company | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| lagos-colony | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| lower-canada | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| malayan-union | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| niger-coast-protectorate | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| northern-nigeria-protectorate | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| orange-river-colony | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| pale-of-calais | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-england,kingdom-of-england; Cliopatria drew this land in its colonial row); joins group british-empire |
| prince-of-wales-island | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| province-of-canada | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| province-of-quebec | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain; Cliopatria drew this land in its colonial row); joins group british-empire |
| royal-niger-company | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| rupert-s-land | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-england,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| sierra-leone-colony-and-protectorate | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| straits-settlements | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| tanganyika-territory | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| thirteen-colonies | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-england,kingdom-of-great-britain; Cliopatria drew this land in its colonial row); joins group british-empire |
| transvaal-colony | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| united-states-of-the-ionian-islands | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| upper-canada | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| weihaiwei | #dc7d97 | britain | british-empire | colony-group | new state: split-off row / same state as british-empire (colony of united-kingdom; Cliopatria drew this land in its colonial row); joins group british-empire |
| catepanate-of-italy | #8e3776 | rome | byzantium | colony-group | new state: split-off row / same state as byzantine-empire (colony of byzantine-empire; Cliopatria drew this land in its colonial row); joins group byzantium |
| despotate-of-the-morea | #8e3776 | rome | byzantium | colony-group | new state: split-off row / same state as byzantine-empire (colony of byzantine-empire; Cliopatria drew this land in its colonial row); joins group byzantium |
| exarchate-of-africa | #8e3776 | rome | byzantium | colony-group | new state: split-off row / same state as byzantine-empire (colony of eastern-roman-empire,byzantine-empire; Cliopatria drew this land in its colonial row); joins group byzantium |
| exarchate-of-ravenna | #8e3776 | rome | byzantium | colony-group | new state: split-off row / same state as byzantine-empire (colony of eastern-roman-empire,byzantine-empire; Cliopatria drew this land in its colonial row); joins group byzantium |
| spania | #8e3776 | rome | byzantium | colony-group | new state: split-off row / same state as byzantine-empire (colony of eastern-roman-empire; Cliopatria drew this land in its colonial row); joins group byzantium |
| equatoria-province | #a05000 | egypt | egypt-modern | colony-group | new state: split-off row / same state as muhammad-ali-dynasty (colony of khedivate-of-egypt; Cliopatria drew this land in its colonial row); joins group egypt-modern |
| turco-egyptian-sudan | #a05000 | egypt | egypt-modern | colony-group | new state: split-off row / same state as muhammad-ali-dynasty (colony of muhammad-ali-dynasty,khedivate-of-egypt; Cliopatria drew this land in its colonial row); joins group egypt-modern |
| french-equatorial-africa | #6d9adc | france | france-empire | colony-group | new state: split-off row / same state as french-africa (colony of french-third-republic,free-french,french-fourth-republic,french-fifth-republic; Cliopatria drew this land in its colonial row); joins group france-empire |
| french-west-africa | #6d9adc | france | france-empire | colony-group | new state: split-off row / same state as french-africa (colony of french-third-republic,free-french,french-fourth-republic,french-fifth-republic; Cliopatria drew this land in its colonial row); joins group france-empire |
| guangzhouwan | #6d9adc | france | france-empire | colony-group | new state: split-off row / same state as french-africa (colony of french-third-republic,vichy-france,french-fourth-republic; Cliopatria drew this land in its colonial row); joins group france-empire |
| illyrian-provinces | #6d9adc | france | france-empire | colony-group | new state: split-off row / same state as french-africa (colony of first-french-empire; Cliopatria drew this land in its colonial row); joins group france-empire |
| saint-domingue | #6d9adc | france | france-empire | colony-group | new state: split-off row / same state as french-africa (colony of kingdom-of-france; Cliopatria drew this land in its colonial row); joins group france-empire |
| maona-of-chios | #ab5a47 | italy | genoa | colony-group | new state: split-off row / same state as republic-of-genoa (colony of republic-of-genoa; Cliopatria drew this land in its colonial row); joins group genoa; changed 2026-11-01: clash with republic-of-venice 0.024, crown-of-aragon 0.061: Venice at 0.024 (1365-13 |
| german-east-africa | #786f89 | germany | germany-empire | colony-group | new state: split-off row / same state as german-africa (colony of german-empire,weimar-republic; Cliopatria drew this land in its colonial row); joins group germany-empire |
| german-new-guinea | #786f89 | germany | germany-empire | colony-group | new state: split-off row / same state as german-africa (colony of german-empire,weimar-republic; Cliopatria drew this land in its colonial row); joins group germany-empire |
| german-samoa | #786f89 | germany | germany-empire | colony-group | new state: split-off row / same state as german-africa (colony of german-empire,weimar-republic; Cliopatria drew this land in its colonial row); joins group germany-empire |
| kiautschou-bay-leased-territory | #786f89 | germany | germany-empire | colony-group | new state: split-off row / same state as german-africa (colony of german-empire; Cliopatria drew this land in its colonial row); joins group germany-empire |
| lintun-commandery | #d24e3e | china | han | colony-group | new state: split-off row / same state as han-dynasty (colony of han-dynasty; Cliopatria drew this land in its colonial row); joins group han |
| xuantu-commandery | #d24e3e | china | han | colony-group | new state: split-off row / same state as han-dynasty (colony of han-dynasty,cao-wei,western-jin; Cliopatria drew this land in its colonial row); joins group han |
| zhenfan-commandery | #d24e3e | china | han | colony-group | new state: split-off row / same state as han-dynasty (colony of han-dynasty; Cliopatria drew this land in its colonial row); joins group han |
| italian-libya | #009867 | italy | italy | colony-group | new state: split-off row / same state as kingdom-of-italy (colony of kingdom-of-italy; Cliopatria drew this land in its colonial row); joins group italy |
| kwantung-leased-territory | #8d1768 | japan | japan | colony-group | new state: split-off row / same state as empire-of-japan (colony of russian-empire,empire-of-japan; Cliopatria drew this land in its colonial row); joins group japan; changed 2026-11-01: clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryuk |
| south-seas-mandate | #8d1768 | japan | japan | colony-group | new state: split-off row / same state as empire-of-japan (colony of empire-of-japan; Cliopatria drew this land in its colonial row); joins group japan; changed 2026-11-01: clash with ming-dynasty 0.097: the Ming realm at 0.097 in 1609-1610 (Ryukyu); Japan, the |
| dongdan | #736dc3 | steppe | liao | colony-group | new state: split-off row / same state as liao-dynasty (colony of liao-dynasty; Cliopatria drew this land in its colonial row); joins group liao; changed 2026-11-01: clash with great-jin 0.063, kara-khitans 0.083: the Jin at 0.063 in 1115-1124 (the Jin, the lar |
| berbice | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic,batavian-republic,first-french-empire,sovereign-principality-of-the-united-netherlands; Cliopatria drew this land in its colonial row); joins group netherlands |
| dutch-brazil | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic; Cliopatria drew this land in its colonial row); joins group netherlands |
| dutch-east-india-company | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic,batavian-republic; Cliopatria drew this land in its colonial row); joins group netherlands |
| dutch-formosa | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic; Cliopatria drew this land in its colonial row); joins group netherlands |
| dutch-malacca | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic,batavian-republic,first-french-empire,sovereign-principality-of-the-united-netherlands,first-french-empire,netherlands; Cliopatria drew this land in its colonial row); joins g |
| dutch-new-guinea | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of netherlands; Cliopatria drew this land in its colonial row); joins group netherlands |
| dutch-suriname | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic,batavian-republic,first-french-empire,sovereign-principality-of-the-united-netherlands,netherlands; Cliopatria drew this land in its colonial row); joins group netherlands |
| essequibo | #c85d00 | france | netherlands | colony-group | new state: split-off row / same state as dutch-east-indies (colony of dutch-republic,kingdom-of-great-britain,united-kingdom; Cliopatria drew this land in its colonial row); joins group netherlands |
| habesh-eyalet | #70782c | islam-west | ottoman | colony-group | new state: split-off row / same state as ottoman-empire (colony of ottoman-empire,muhammad-ali-dynasty,ottoman-empire; Cliopatria drew this land in its colonial row); joins group ottoman |
| ottoman-hungary | #70782c | islam-west | ottoman | colony-group | new state: split-off row / same state as ottoman-empire (colony of ottoman-empire; Cliopatria drew this land in its colonial row); joins group ottoman |
| royal-prussia | #cc6f9d | east-europe | poland | colony-group | new state: split-off row / same state as kingdom-of-poland (colony of house-of-jagiellon,polish-lithuanian-commonwealth; Cliopatria drew this land in its colonial row); joins group poland |
| colonial-brazil | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado  |
| portuguese-angola | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire,portuguese-republic,estado-novo; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Port |
| portuguese-india | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire,portuguese-republic,estado-novo; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Port |
| portuguese-malacca | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado  |
| portuguese-mombasa | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado  |
| portuguese-morocco | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado  |
| portuguese-mozambique | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire,portuguese-republic,estado-novo; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Port |
| portuguese-timor | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire,portuguese-republic,estado-novo; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Port |
| state-of-maranhao-and-grao-para | #47a962 | portugal | portugal-empire | colony-group | new state: split-off row / same state as portuguese-empire (colony of portuguese-empire; Cliopatria drew this land in its colonial row); joins group portugal-empire; changed 2026-11-01: clash with kingdom-of-portugal 0.091: Portugal (kingdom, republic, Estado  |
| brandenburger-gold-coast | #495766 | germany | prussia | colony-group | new state: split-off row / same state as kingdom-of-prussia (colony of brandenburg-prussia,kingdom-of-prussia; Cliopatria drew this land in its colonial row); joins group prussia |
| new-east-prussia | #495766 | germany | prussia | colony-group | new state: split-off row / same state as kingdom-of-prussia (colony of kingdom-of-prussia; Cliopatria drew this land in its colonial row); joins group prussia |
| south-prussia | #495766 | germany | prussia | colony-group | new state: split-off row / same state as kingdom-of-prussia (colony of kingdom-of-prussia; Cliopatria drew this land in its colonial row); joins group prussia |
| russian-america | #236436 | russia | russia | colony-group | new state: split-off row / same state as russian-empire (colony of russian-empire; Cliopatria drew this land in its colonial row); joins group russia |
| russian-turkestan | #236436 | russia | russia | colony-group | new state: split-off row / same state as russian-empire (colony of russian-empire,russian-soviet-federative-socialist-republic; Cliopatria drew this land in its colonial row); joins group russia |
| captaincy-general-of-chile | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| captaincy-general-of-cuba | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| captaincy-general-of-guatemala | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| captaincy-general-of-venezuela | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-bougie | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of crown-of-castile,spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-east-indies | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-florida | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-formosa | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-louisiana | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-oran | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of crown-of-castile,spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-presidios-of-morocco | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-tripoli | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of crown-of-castile,spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| spanish-tunis | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| viceroyalty-of-new-granada | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| viceroyalty-of-new-spain | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| viceroyalty-of-peru | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| viceroyalty-of-the-rio-de-la-plata | #df911a | iberia | spain | colony-group | new state: split-off row / same state as spanish-empire (colony of spanish-empire; Cliopatria drew this land in its colonial row); joins group spain |
| bremen-verden | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of swedish-empire; Cliopatria drew this land in its colonial row); joins group sweden |
| kexholm-county | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of swedish-empire,swedish-empire; Cliopatria drew this land in its colonial row); joins group sweden |
| swedish-estonia | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of kingdom-of-sweden,swedish-empire; Cliopatria drew this land in its colonial row); joins group sweden |
| swedish-gold-coast | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of swedish-empire; Cliopatria drew this land in its colonial row); joins group sweden |
| swedish-ingria | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of kingdom-of-sweden,swedish-empire; Cliopatria drew this land in its colonial row); joins group sweden |
| swedish-livonia | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of swedish-empire; Cliopatria drew this land in its colonial row); joins group sweden |
| swedish-pomerania | #3082b5 | nordic | sweden | colony-group | new state: split-off row / same state as swedish-empire (colony of swedish-empire,kingdom-of-sweden; Cliopatria drew this land in its colonial row); joins group sweden |
| beiting-protectorate | #d6ab1b | china | tang | colony-group | new state: split-off row / same state as tang-dynasty (colony of tang-dynasty; Cliopatria drew this land in its colonial row); joins group tang |
| protectorate-general-to-pacify-the-east | #d6ab1b | china | tang | colony-group | new state: split-off row / same state as tang-dynasty (colony of tang-dynasty; Cliopatria drew this land in its colonial row); joins group tang |
| protectorate-general-to-pacify-the-north | #d6ab1b | china | tang | colony-group | new state: split-off row / same state as tang-dynasty (colony of tang-dynasty; Cliopatria drew this land in its colonial row); joins group tang |
| protectorate-general-to-pacify-the-south | #d6ab1b | china | tang | colony-group | new state: split-off row / same state as tang-dynasty (colony of tang-dynasty; Cliopatria drew this land in its colonial row); joins group tang |
| protectorate-general-to-pacify-the-west | #d6ab1b | china | tang | colony-group | new state: split-off row / same state as tang-dynasty (colony of tang-dynasty; Cliopatria drew this land in its colonial row); joins group tang |
| ungjin-commandery | #d6ab1b | china | tang | colony-group | new state: split-off row / same state as tang-dynasty (colony of tang-dynasty; Cliopatria drew this land in its colonial row); joins group tang |
| commonwealth-of-the-northern-mariana-islands | #433889 | americas | usa | colony-group | new state: split-off row / same state as united-states-of-america (colony of united-states-of-america; Cliopatria drew this land in its colonial row); joins group usa |
| insular-government-of-the-philippine-islands | #433889 | americas | usa | colony-group | new state: split-off row / same state as united-states-of-america (colony of united-states-of-america; Cliopatria drew this land in its colonial row); joins group usa |
| trust-territory-of-the-pacific-islands | #433889 | americas | usa | colony-group | new state: split-off row / same state as united-states-of-america (colony of united-states-of-america; Cliopatria drew this land in its colonial row); joins group usa |
| united-states-army-military-government-in-korea | #433889 | americas | usa | colony-group | new state: split-off row / same state as united-states-of-america (colony of united-states-of-america; Cliopatria drew this land in its colonial row); joins group usa |
| soviet-civil-administration | #8d1a1e | russia | ussr | colony-group | new state: split-off row / same state as union-of-soviet-socialist-republics (colony of union-of-soviet-socialist-republics; Cliopatria drew this land in its colonial row); joins group ussr |
| kingdom-of-candia | #c87973 | italy | venice | colony-group | new state: split-off row / same state as republic-of-venice (colony of republic-of-venice; Cliopatria drew this land in its colonial row); joins group venice |
| venetian-dalmatia | #c87973 | italy | venice | colony-group | new state: split-off row / same state as republic-of-venice (colony of republic-of-venice; Cliopatria drew this land in its colonial row); joins group venice |
| venetian-modon-and-coron | #c87973 | italy | venice | colony-group | new state: split-off row / same state as republic-of-venice (colony of republic-of-venice; Cliopatria drew this land in its colonial row); joins group venice |
| dongnyeong-prefecture | #9c672e | mongol | yuan | colony-group | new state: split-off row / same state as yuan-dynasty (colony of mongol-empire; Cliopatria drew this land in its colonial row); joins group yuan |
| ssangseong-prefecture | #9c672e | mongol | yuan | colony-group | new state: split-off row / same state as yuan-dynasty (colony of mongol-empire,yuan-dynasty; Cliopatria drew this land in its colonial row); joins group yuan |
| bonapartist-spain | #a85500 | iberia |  | continuity | new state: continuity successor of kingdom-of-spain (Joseph Bonaparte's Kingdom of Spain, rival of Patriot Spain): a neighbouring hue in family iberia, oklch(0.54 0.134 55), margin 0.180 |
| congo-free-state | #b5c159 | france |  | continuity | new state: continuity successor of belgian-congo (Leopold II's Congo, predecessor of the Belgian Congo): a neighbouring hue in family france (outside the family range: nothing inside cleared its neighbours), oklch(0.78 0.130 115), margin 0.160 |
| congress-poland | #d684c4 | east-europe |  | continuity | new state: continuity successor of kingdom-of-poland (the Kingdom of Poland in union with Russia): a neighbouring hue in family east-europe, oklch(0.72 0.129 335), margin 0.177 |
| cossack-hetmanate | #c6c95e | east-europe |  | continuity | new state: continuity successor of ukraine (the Cossack Hetmanate, Ukrainian statehood's predecessor): a neighbouring hue in family east-europe (outside the family range: nothing inside cleared its neighbours), oklch(0.81 0.130 110), margin 0.137 |
| frankish-burgundy | #593b7e | france |  | continuity | new state: continuity successor of kingdom-of-the-franks (a Merovingian sub-kingdom of the Franks): a neighbouring hue in family france (outside the family range: nothing inside cleared its neighbours), oklch(0.42 0.110 302), margin 0.104 |
| grand-duchy-of-finland | #769fcc | nordic |  | continuity | new state: continuity successor of republic-of-finland (autonomous Finland under Russia, predecessor of the Republic): a neighbouring hue in family nordic, oklch(0.69 0.080 251), margin 0.115 |
| islamic-state-of-medina | #53ae77 | caliphate |  | continuity | new state: continuity successor of rashidun-caliphate (the Prophet's state at Medina, the caliphate's beginning (caliphates green)): a neighbouring hue in family caliphate, oklch(0.68 0.120 155), margin 0.214 |
| italian-social-republic | #68bb72 | italy |  | continuity | new state: continuity successor of kingdom-of-italy (the fascist rump state claiming Italy's continuity): a neighbouring hue in family italy, oklch(0.72 0.132 147), margin 0.125 |
| kingdom-of-austrasia | #315e9b | france |  | continuity | new state: continuity successor of kingdom-of-the-franks (a Merovingian sub-kingdom of the Franks): a neighbouring hue in family france, oklch(0.48 0.110 257), margin 0.122 |
| kingdom-of-ireland | #008a59 | britain |  | continuity | new state: continuity successor of eire (the Kingdom of Ireland under the English and British crowns): a neighbouring hue in family britain (outside the family range: nothing inside cleared its neighbours), oklch(0.56 0.127 160), margin 0.151 |
| kingdom-of-italy-medieval | #2e833d | italy |  | continuity | new state: continuity successor of kingdom-of-italy (the medieval Kingdom of Italy, half of the split of Cliopatria's 'Kingdom of Italy' row): a neighbouring hue in family italy, oklch(0.54 0.132 147), margin 0.169 |
| later-gupta-dynasty | #fba6e9 | india |  | continuity | new state: continuity successor of gupta-empire (the Later Guptas, successors claiming the Gupta name): a neighbouring hue in family india, oklch(0.83 0.130 335), margin 0.141 |
| lordship-of-ireland | #68d7a0 | britain |  | continuity | new state: continuity successor of eire (the Lordship of Ireland under the English crown): a neighbouring hue in family britain (outside the family range: nothing inside cleared its neighbours), oklch(0.80 0.130 160), margin 0.102 |
| murong-xianbei | #6ba7ca | steppe |  | continuity | new state: continuity successor of xianbei (the Murong branch of the Xianbei): a neighbouring hue in family steppe, oklch(0.70 0.080 235), margin 0.119 |
| persis | #305481 | persia |  | continuity | new state: continuity successor of sasanian-empire (the Persian kings of Persis, from whom the Sasanians rose (Persia teal family)): a neighbouring hue in family persia (outside the family range: nothing inside cleared its neighbours), oklch(0.44 0.085 255), m |
| russian-state | #45743b | russia |  | continuity | new state: continuity successor of russian-republic (the White government claiming Russia's continuity): a neighbouring hue in family russia, oklch(0.51 0.099 140), margin 0.140 |
| south-russia | #56854c | russia |  | continuity | new state: continuity successor of russian-republic (the White government of the south claiming Russia's continuity): a neighbouring hue in family russia, oklch(0.57 0.099 140), margin 0.142 |
| tokugawa-clan | #be4d77 | japan |  | continuity | new state: continuity successor of tokugawa-shogunate (the Tokugawa domain that became the shogunate): a neighbouring hue in family japan, oklch(0.58 0.150 360), margin 0.126 |
| twenty-fifth-dynasty-of-egypt | #5c4c00 | africa |  | continuity | new state: continuity successor of kingdom-of-kush (the Kushite pharaohs, Kush ruling Egypt): a neighbouring hue in family africa, oklch(0.42 0.087 95), margin 0.125 |
| stem-duchy-of-bavaria | #579bc2 | germany | bavaria | group | new state: split-off row / same state as duchy-of-bavaria (the Duchy of Bavaria before 1255 (Cliopatria's row starts 1260): one state); joins group bavaria |
| east-india-company | #dc7d97 | britain | british-empire | group | new state: split-off row / same state as british-empire (Company rule in India: Cliopatria's British Empire row drew Bengal from 1762; British colonial pink); joins group british-empire |
| burgundian-state | #884783 | france | burgundy | group | new state: split-off row / same state as duchy-of-burgundy (the Valois dukes' Burgundian State; Cliopatria has the Duchy of Burgundy 1003-1481 as one row); joins group burgundy |
| ulus-of-chagatai | #8acfaa | mongol | chagatai | group | new state: split-off row / same state as chagatai-khanate (the Chagatai Khanate under its earlier name (Ulus of Chagatai 1227-1293): one state); joins group chagatai; changed 2026-11-01: clash with white-horde 0.029, four-oirats 0.068: the Four Oirats (larger) |
| kingdom-of-denmark-1814-1940 | #f45055 | nordic | denmark | group | new state: split-off row / same state as denmark (split from Cliopatria's 'Denmark-Norway' row (1526-1940) at 1814: the same Danish state); joins group denmark; takes its group's new colour #f45055 (Denmark's realm (Gold Coast forts, Tranquebar, the Danish Wes |
| sultanate-of-egypt | #a05000 | egypt | egypt-modern | group | new state: split-off row / same state as kingdom-of-egypt (the Muhammad Ali state as a sultanate 1914-22, between the Khedivate and the Kingdom); joins group egypt-modern |
| thirty-first-dynasty-of-egypt | #c3963b | egypt | egypt-pharaonic | group | new state: split-off row / same state as new-kingdom-of-egypt (Manetho's 31st dynasty of Egypt (second Persian period); a dynasty change within Egypt keeps the colour); joins group egypt-pharaonic |
| twenty-eighth-dynasty-of-egypt | #c3963b | egypt | egypt-pharaonic | group | new state: split-off row / same state as new-kingdom-of-egypt (Manetho's 28th dynasty of Egypt; a dynasty change within Egypt keeps the colour); joins group egypt-pharaonic |
| twenty-first-dynasty-of-egypt | #c3963b | egypt | egypt-pharaonic | group | new state: split-off row / same state as new-kingdom-of-egypt (split from Cliopatria's 'New Kingdom of Egypt' row; a dynasty change within Egypt keeps the colour); joins group egypt-pharaonic |
| twenty-ninth-dynasty-of-egypt | #c3963b | egypt | egypt-pharaonic | group | new state: split-off row / same state as new-kingdom-of-egypt (Manetho's 29th dynasty of Egypt; a dynasty change within Egypt keeps the colour); joins group egypt-pharaonic |
| twenty-seventh-dynasty-of-egypt | #c3963b | egypt | egypt-pharaonic | group | new state: split-off row / same state as new-kingdom-of-egypt (Manetho's 27th dynasty of Egypt (Persian pharaohs); a dynasty change within Egypt keeps the colour); joins group egypt-pharaonic |
| royal-domain-of-france | #3e6fc2 | france | france | group | new state: split-off row / same state as kingdom-of-france (the French king's own lands, a layer inside the Kingdom of France: France blue); joins group france |
| kingdom-of-kartli-kakheti | #6f59a6 | east-europe | georgia | group | new state: split-off row / same state as kingdom-of-georgia (split-off from Cliopatria's 'Kingdom of Georgia' row (1010-1802): the Georgian kingdom's last phase); joins group georgia |
| second-turkic-khaganate | #2b8cad | steppe | gokturk | group | new state: split-off row / same state as eastern-gokturks (the restored Gokturk khaganate of the Ashina (a restoration keeps the old colour)); joins group gokturk |
| ulus-of-jochi | #c28e24 | mongol | golden-horde | group | new state: split-off row / same state as golden-horde (the Golden Horde under its earlier name (Ulus of Jochi 1225-1293, Cliopatria's row starts 1294): one state); joins group golden-horde |
| united-kingdom | #c24976 | britain | great-britain | group | new state: split-off row / same state as kingdom-of-great-britain (the second half of Cliopatria's single 'Kingdom of Great Britain' row (1709-2024), split at the union of 1801; Britain's conventional pink-red); joins group great-britain |
| kingdom-of-han | #d24e3e | china | han | group | new state: split-off row / same state as han-dynasty (Liu Bang's Kingdom of Han (-206..-203), the same state as the Han dynasty from 202 (han-2 is the same kingdom)); joins group han |
| royal-hungary | #946db1 | east-europe | hungary | group | new state: split-off row / same state as kingdom-of-hungary (the continuing Kingdom of Hungary under the Habsburgs (Cliopatria's Hungary rows)); joins group hungary |
| second-hungarian-republic | #946db1 | east-europe | hungary | group | new state: split-off row / same state as hungary (split from Cliopatria's 'Hungary' row: the Hungarian state 1946-49); joins group hungary |
| ulus-of-hulegu | #c4464f | mongol | ilkhanate | group | new state: split-off row / same state as ilkhanate (the Ilkhanate under its earlier name (Ulus of Hulegu 1256-1293): one state); joins group ilkhanate; takes its group's new colour #c4464f (the Ulus of Hulegu (the Ilkhanate before 1294) touches the Mongol Empi |
| post-angkor-cambodia | #c16048 | southeast-asia | khmer | group | new state: split-off row / same state as khmer-empire (split from Cliopatria's 'Khmer Empire' row (800-1867): the same Cambodian kingdom after Angkor); joins group khmer |
| zhu-yuanzhang-s-wu | #a12f35 | china | ming | group | new state: split-off row / same state as ming-dynasty (the rebel state that became the Ming (rule: a rebel that wins and becomes the state shares its colour); Ming's convention is kept); joins group ming |
| third-saudi-state | #005c3a | islam-west | saudi | group | new state: split-off row / same state as emirate-of-nejd (split from Cliopatria's 'Emirate of Nejd' row: the Saudi state from 1902); joins group saudi |
| moravian-serbia | #4c579b | east-europe | serbia | group | new state: split-off row / same state as serbian-empire (split from Cliopatria's 'Serbian Empire' row: Serbia under Lazar, between the Empire and the Despotate); joins group serbia |
| state-of-vietnam | #cdaf33 | southeast-asia | south-vietnam | group | new state: split-off row / same state as republic-of-vietnam (the State of Vietnam became the Republic of Vietnam in 1955: one state); joins group south-vietnam |
| armenian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| azerbaijan-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| byelorussian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| estonian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| georgian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| karelo-finnish-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| kazakh-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| kirghiz-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| latvian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| lithuanian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| moldavian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| russian-soviet-federative-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| tajik-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| transcaucasian-socialist-federative-soviet-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| turkmen-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| ukrainian-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| uzbek-soviet-socialist-republic | #8d1a1e | russia | ussr | group | new state: split-off row / same state as union-of-soviet-socialist-republics (a union republic split from Cliopatria's USSR row; Soviet deep red (the Reds of 1917-22 for the RSFSR)); joins group ussr |
| eastern-zhou | #ba7e2d | china | zhou | group | new state: split-off row / same state as zhou-dynasty (Cliopatria splits the Zhou line at 750: Eastern Zhou is the same royal house); joins group zhou |

### New wheel colours (1273)

| slug | hex | wheel | min distance | rule |
| --- | --- | --- | --- | --- |
| a-group-culture | #ba5661 | h015-deep | 0.232 | culture |
| aboriginal-australians | #718516 | h120-deep | no neighbour | culture |
| aboriginal-tasmanians | #5d74c7 | h270-deep | no neighbour | culture |
| ahar-banas-culture | #348f4f | h150-deep | 0.225 | culture |
| anatolian-neolithic | #bb584a | h030-deep | no neighbour | culture |
| anau-culture | #a46e00 | h075-deep | no neighbour | culture |
| atlantic-megalith-builders | #867d00 | h105-deep | no neighbour | culture |
| badarian-culture | #867d00 | h105-deep | no neighbour | culture |
| beixin-culture | #967600 | h090-deep | 0.216 | culture |
| capsian-culture | #0087ab | h225-deep | 0.202 | culture |
| cardial-ware-culture | #407bc5 | h255-deep | 0.178 | culture |
| chachapoya-culture | #008c8c | h195-deep | 0.227 | culture |
| chavin-culture | #5d74c7 | h270-deep | no neighbour | culture |
| chinchorro-culture | #9760af | h315-deep | no neighbour | culture |
| cishan-culture | #af578c | h345-deep | 0.207 | culture |
| cochise-culture | #348f4f | h150-deep | 0.259 | culture |
| cucuteni-trypillia-culture | #b85e31 | h045-deep | 0.207 | culture |
| dadiwan-culture | #bb584a | h030-deep | no neighbour | culture |
| dapenkeng-culture | #967600 | h090-deep | no neighbour | culture |
| dawenkou-culture | #008e7d | h180-deep | 0.204 | culture |
| daxi-culture | #b16512 | h060-deep | 0.222 | culture |
| epi-olmec-culture | #718516 | h120-deep | no neighbour | culture |
| faiyum-merimde-neolithic | #a46e00 | h075-deep | no neighbour | culture |
| funnelbeaker-culture | #8766bb | h300-deep | 0.183 | culture |
| gandhara-grave-culture | #ba5661 | h015-deep | no neighbour | culture |
| ghassulian | #b85e31 | h045-deep | no neighbour | culture |
| green-sahara-cultures | #867d00 | h105-deep | 0.200 | culture |
| hakra-ware-culture | #867d00 | h105-deep | 0.250 | culture |
| halaf-culture | #8766bb | h300-deep | 0.261 | culture |
| hassuna-culture | #718516 | h120-deep | 0.241 | culture |
| hemudu-culture | #578b35 | h135-deep | no neighbour | culture |
| hoabinhian | #967600 | h090-deep | no neighbour | culture |
| hongshan-culture | #a46e00 | h075-deep | 0.224 | culture |
| houli-culture | #0c82bf | h240-deep | 0.207 | culture |
| jeitun-culture | #736dc3 | h285-deep | no neighbour | culture |
| jeulmun-pottery-period | #008a9b | h210-deep | no neighbour | culture |
| jomon-period | #b65577 | h000-deep | no neighbour | culture |
| jorwe-culture | #578b35 | h135-deep | 0.261 | culture |
| kelteminar-culture | #ba5661 | h015-deep | no neighbour | culture |
| khartoum-mesolithic-and-neolithic | #0c82bf | h240-deep | 0.235 | culture |
| kuk-swamp-agriculture | #9760af | h315-deep | no neighbour | culture |
| lengyel-culture | #008c8c | h195-deep | 0.183 | culture |
| liangzhu-culture | #af578c | h345-deep | no neighbour | culture |
| linear-pottery-culture | #a46e00 | h075-deep | 0.173 | culture |
| longshan-culture | #b16512 | h060-deep | 0.204 | culture |
| maadi-culture | #b65577 | h000-deep | 0.200 | culture |
| majiabang-culture | #b16512 | h060-deep | no neighbour | culture |
| majiayao-culture | #008e7d | h180-deep | 0.204 | culture |
| malwa-culture | #5d74c7 | h270-deep | 0.225 | culture |
| maritime-archaic | #b85e31 | h045-deep | no neighbour | culture |
| mehrgarh-culture | #8766bb | h300-deep | no neighbour | culture |
| moche-culture | #407bc5 | h255-deep | 0.184 | culture |
| nabta-playa-neolithic | #b65577 | h000-deep | 0.200 | culture |
| naqada-culture | #819ae9 | h270-mid | 0.214 | culture |
| nazca-culture | #348f4f | h150-deep | no neighbour | culture |
| norte-chico-civilization | #b16512 | h060-deep | no neighbour | culture |
| ochre-coloured-pottery-culture | #df8071 | h030-mid | 0.214 | culture |
| old-copper-complex | #718516 | h120-deep | no neighbour | culture |
| oshara-tradition | #af578c | h345-deep | 0.259 | culture |
| painted-grey-ware-culture | #dc855d | h045-mid | 0.215 | culture |
| peiligang-culture | #a45b9f | h330-deep | no neighbour | culture |
| pottery-neolithic-levant | #009068 | h165-deep | no neighbour | culture |
| qujialing-culture | #008a9b | h210-deep | 0.200 | culture |
| samarra-culture | #407bc5 | h255-deep | 0.241 | culture |
| sanxingdui-culture | #b65577 | h000-deep | no neighbour | culture |
| sican-culture | #967600 | h090-deep | 0.198 | culture |
| songze-culture | #8766bb | h300-deep | no neighbour | culture |
| southern-neolithic-ashmound-tradition | #9760af | h315-deep | 0.261 | culture |
| sredny-stog-culture | #009068 | h165-deep | 0.218 | culture |
| starcevo-koros-cris-culture | #009068 | h165-deep | 0.173 | culture |
| tairona | #736dc3 | h285-deep | 0.301 | culture |
| tenerian-culture | #0087ab | h225-deep | 0.202 | culture |
| tichitt-tradition | #0c82bf | h240-deep | no neighbour | culture |
| ubaid-period | #bb584a | h030-deep | 0.241 | culture |
| uruk-period | #008c8c | h195-deep | no neighbour | culture |
| valdivia-culture | #b85e31 | h045-deep | no neighbour | culture |
| vinca-culture | #a45b9f | h330-deep | 0.201 | culture |
| watson-brake-culture | #008a9b | h210-deep | no neighbour | culture |
| western-mexico-shaft-tomb-tradition | #736dc3 | h285-deep | no neighbour | culture |
| xia-dynasty | #008e7d | h180-deep | 0.204 | culture |
| xinglongwa-culture | #578b35 | h135-deep | no neighbour | culture |
| yamnaya-culture | #736dc3 | h285-deep | 0.226 | culture |
| yangshao-culture | #a45b9f | h330-deep | 0.200 | culture |
| zhaobaogou-culture | #0087ab | h225-deep | 0.224 | culture |
| abe-clan | #a46e00 | h075-deep | 0.253 | rebel |
| ali-burghul | #af578c | h345-deep | 0.212 | rebel |
| arakan-army | #819ae9 | h270-mid | 0.214 | rebel |
| ariq-boke | #0087ab | h225-deep | 0.225 | rebel |
| atahualpa-faction | #0087ab | h225-deep | 0.233 | rebel |
| autonomous-administration-of-north-and-east-syria | #8ed09c | h150-light | 0.148 | rebel |
| autonomous-province-of-western-bosnia | #63b376 | h150-mid | 0.221 | rebel |
| azariqa-kharijite-emirate | #bb584a | h030-deep | 0.226 | rebel |
| azawad | #736dc3 | h285-deep | 0.130 | rebel |
| azerbaijan-people-s-government | #aa8dde | h300-mid | 0.204 | rebel |
| baekje-restoration-movement | #69a1e8 | h255-mid | 0.257 | rebel |
| bahram-chobin | #b16512 | h060-deep | 0.215 | rebel |
| banu-marwan-of-badajoz | #bb584a | h030-deep | 0.259 | rebel |
| bar-kokhba-state | #736dc3 | h285-deep | 0.230 | rebel |
| basmachi-movement | #30add6 | h225-mid | 0.213 | rebel |
| bessus-artaxerxes-v | #df8071 | h030-mid | 0.260 | rebel |
| biafra | #d58b4b | h060-mid | 0.198 | rebel |
| bohemian-confederacy | #ca933e | h075-mid | 0.170 | rebel |
| bougainville-interim-government | #867d00 | h105-deep | 0.251 | rebel |
| britannic-empire | #009068 | h165-deep | 0.274 | rebel |
| cabanagem-rebels | #b85e31 | h045-deep | 0.208 | rebel |
| carlist-state | #24b6a1 | h180-mid | 0.223 | rebel |
| catholic-league-france | #24b6a1 | h180-mid | 0.223 | rebel |
| chen-han | #63b376 | h150-mid | 0.204 | rebel |
| chimei | #008a9b | h210-deep | 0.184 | rebel |
| chremonidean-alliance | #ba87d2 | h315-mid | 0.214 | rebel |
| cleopatra-ii-alexandria | #a45b9f | h330-deep | 0.275 | rebel |
| coalition-government-of-democratic-kampuchea | #ca933e | h075-mid | 0.120 | rebel |
| communist-party-of-burma | #bb9b39 | h090-mid | 0.149 | rebel |
| confederated-estates-of-hungary | #819ae9 | h270-mid | 0.165 | rebel |
| confederation-of-the-equator | #b65577 | h000-deep | no neighbour | rebel |
| constantine-iii-usurper | #736dc3 | h285-deep | 0.172 | rebel |
| croatian-republic-of-herzeg-bosnia | #a2cd8b | h135-light | 0.201 | rebel |
| diponegoro-s-rebels | #d37faf | h345-mid | 0.182 | rebel |
| domain-of-magnus-maximus | #5d74c7 | h270-deep | 0.119 | rebel |
| domain-of-matthew-iii-csak | #4fa8e1 | h240-mid | 0.148 | rebel |
| donetsk-people-s-republic | #da7d9b | h000-mid | 0.191 | rebel |
| dou-jiande-s-xia | #46b68c | h165-mid | 0.151 | rebel |
| du-fuwei-s-regime | #0c82bf | h240-deep | 0.174 | rebel |
| dungan-revolt | #967600 | h090-deep | 0.242 | rebel |
| eastern-liao | #dc855d | h045-mid | 0.195 | rebel |
| eastern-xia | #a45b9f | h330-deep | 0.170 | rebel |
| emirate-of-afghanistan-1929 | #348f4f | h150-deep | no neighbour | rebel |
| eritrean-people-s-liberation-front | #ba5661 | h015-deep | 0.217 | rebel |
| eugenius-usurpation | #5d74c7 | h270-deep | 0.119 | rebel |
| fang-guozhen-s-regime | #da7d9b | h000-mid | 0.172 | rebel |
| first-philippine-republic | #af578c | h345-deep | 0.223 | rebel |
| forces-nouvelles-de-cote-d-ivoire | #b7b5fc | h285-light | 0.132 | rebel |
| free-republic-of-the-congo | #46b68c | h165-mid | 0.122 | rebel |
| front-for-the-restoration-of-unity-and-democracy | #24b6a1 | h180-mid | 0.169 | rebel |
| fu-gongshi-s-song | #bb584a | h030-deep | 0.228 | rebel |
| glyndwr-s-wales | #009068 | h165-deep | 0.288 | rebel |
| gobierno-del-cerrito | #d37faf | h345-mid | 0.187 | rebel |
| han-song | #8766bb | h300-deep | 0.172 | rebel |
| harsiesi | #ba5661 | h015-deep | 0.227 | rebel |
| hou-jing-s-han | #b85e31 | h045-deep | 0.163 | rebel |
| houthis | #ca933e | h075-mid | 0.207 | rebel |
| hussite-bohemia | #aa8dde | h300-mid | 0.120 | rebel |
| ili-sultanate | #407bc5 | h255-deep | 0.224 | rebel |
| indian-rebels-of-1857 | #407bc5 | h255-deep | no neighbour | rebel |
| islamic-state | #aa8dde | h300-mid | 0.169 | rebel |
| ispah-rebellion | #407bc5 | h255-deep | 0.229 | rebel |
| jewish-provisional-government | #008a9b | h210-deep | 0.269 | rebel |
| jovinus-usurper | #819ae9 | h270-mid | 0.146 | rebel |
| juliana-republic | #008a9b | h210-deep | no neighbour | rebel |
| kachin-independence-organization | #69a1e8 | h255-mid | 0.201 | rebel |
| kaga-ikko-ikki | #a46e00 | h075-deep | 0.206 | rebel |
| karen-national-union | #09b2c7 | h210-mid | 0.148 | rebel |
| kayastha-principality-of-ambadeva | #46b68c | h165-mid | 0.190 | rebel |
| kertabhumi-majapahit | #718516 | h120-deep | 0.208 | rebel |
| khababash | #ba87d2 | h315-mid | 0.214 | rebel |
| khurramites | #df8071 | h030-mid | 0.169 | rebel |
| kingdom-of-achaeus | #c882c2 | h330-mid | 0.149 | rebel |
| kingdom-of-antiochus-hierax | #c882c2 | h330-mid | 0.116 | rebel |
| kuomintang-in-burma | #aaa23f | h105-mid | 0.132 | rebel |
| li-gui-s-liang | #c882c2 | h330-mid | 0.169 | rebel |
| li-mi-s-wei | #aa8dde | h300-mid | 0.212 | rebel |
| li-zitong-s-wu | #da7d9b | h000-mid | 0.120 | rebel |
| liang-province-rebels | #9760af | h315-deep | 0.171 | rebel |
| liang-shidu-s-liang | #c882c2 | h330-mid | 0.120 | rebel |
| lin-shihong-s-chu | #aa8dde | h300-mid | 0.120 | rebel |
| liu-heita-s-handong | #da7d9b | h000-mid | 0.200 | rebel |
| liu-wuzhou-s-dingyang | #819ae9 | h270-mid | 0.120 | rebel |
| luhansk-people-s-republic | #69a1e8 | h255-mid | 0.191 | rebel |
| lulin | #008e7d | h180-deep | 0.267 | rebel |
| maccabean-judea | #bb9b39 | h090-mid | 0.207 | rebel |
| macrianus-and-quietus | #9760af | h315-deep | 0.175 | rebel |
| maximus-usurper | #aaa23f | h105-mid | 0.197 | rebel |
| mercenary-rebels | #967600 | h090-deep | 0.256 | rebel |
| minamoto-clan | #967600 | h090-deep | 0.270 | rebel |
| ming-xia | #da7d9b | h000-mid | 0.172 | rebel |
| mong-tai-army | #ca933e | h075-mid | 0.167 | rebel |
| mosquera-s-cauca-rebellion | #df7e86 | h015-mid | 0.208 | rebel |
| mottama-rebels | #d7bb70 | h090-light | 0.150 | rebel |
| mukhtarid-state-of-kufa | #9760af | h315-deep | 0.117 | rebel |
| myanmar-national-democratic-alliance-army | #ba87d2 | h315-mid | 0.207 | rebel |
| najdat-kharijite-emirate | #b85e31 | h045-deep | 0.185 | rebel |
| negara-islam-indonesia | #867d00 | h105-deep | 0.214 | rebel |
| nian-rebellion | #ba5661 | h015-deep | 0.228 | rebel |
| osroes-i | #8766bb | h300-deep | 0.204 | rebel |
| padri-movement | #a2cd8b | h135-light | 0.132 | rebel |
| pathet-lao | #d37faf | h345-mid | 0.130 | rebel |
| persian-socialist-soviet-republic | #df7e86 | h015-mid | 0.262 | rebel |
| phoenician-and-cypriot-rebels | #af578c | h345-deep | 0.217 | rebel |
| provisional-government-of-schleswig-holstein | #f7a3a9 | h015-light | 0.101 | rebel |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam | #aa8dde | h300-mid | 0.145 | rebel |
| prussian-confederation | #b65577 | h000-deep | no neighbour | rebel |
| qi-huang-chao | #b65577 | h000-deep | 0.268 | rebel |
| qiang | #348f4f | h150-deep | 0.261 | rebel |
| raja-mahdi-s-faction | #ba5661 | h015-deep | 0.212 | rebel |
| rapid-support-forces | #95a94e | h120-mid | 0.120 | rebel |
| rebellion-of-umar-ibn-hafsun | #b16512 | h060-deep | 0.231 | rebel |
| republic-of-acre | #ca933e | h075-mid | 0.240 | rebel |
| republic-of-cuba-in-arms-ten-years-war | #bb584a | h030-deep | no neighbour | rebel |
| republic-of-entre-rios | #d58b4b | h060-mid | 0.189 | rebel |
| republic-of-ezo | #df7e86 | h015-mid | 0.262 | rebel |
| republic-of-graaff-reinet | #7daf61 | h135-mid | 0.215 | rebel |
| republic-of-mahabad | #95a94e | h120-mid | 0.120 | rebel |
| republic-of-saint-titus | #008e7d | h180-deep | 0.216 | rebel |
| republic-of-san-marco | #009068 | h165-deep | 0.290 | rebel |
| republic-of-serbian-krajina | #d6aaea | h315-light | 0.149 | rebel |
| republic-of-south-maluku | #348f4f | h150-deep | 0.287 | rebel |
| republika-srpska | #a2cd8b | h135-light | 0.201 | rebel |
| revolt-of-aristonicus | #eeae7b | h060-light | 0.191 | rebel |
| revolt-of-athanagild | #008e7d | h180-deep | 0.253 | rebel |
| revolt-of-hermenegild | #63b376 | h150-mid | 0.237 | rebel |
| revolt-of-inaros-ii | #ba87d2 | h315-mid | 0.214 | rebel |
| revolt-of-molon | #dc855d | h045-mid | 0.195 | rebel |
| revolt-of-timarchus | #df8071 | h030-mid | 0.174 | rebel |
| revolutionary-government-of-the-republic-of-indonesia | #867d00 | h105-deep | 0.214 | rebel |
| revolutionary-united-front | #d37faf | h345-mid | 0.145 | rebel |
| roman-republic-1849 | #0087ab | h225-deep | no neighbour | rebel |
| sambyeolcho | #5d74c7 | h270-deep | 0.213 | rebel |
| seleka | #d58b4b | h060-mid | 0.119 | rebel |
| sertorian-hispania | #578b35 | h135-deep | 0.247 | rebel |
| sextus-pompeius | #718516 | h120-deep | 0.223 | rebel |
| shen-faxing-s-liang | #24b6a1 | h180-mid | 0.174 | rebel |
| south-kasai | #d37faf | h345-mid | 0.190 | rebel |
| southern-transitional-council | #8766bb | h300-deep | 0.232 | rebel |
| state-of-katanga | #4fa8e1 | h240-mid | 0.138 | rebel |
| sudan-people-s-liberation-movement | #da7d9b | h000-mid | 0.172 | rebel |
| svitrigaila-s-grand-duchy | #bb9b39 | h090-mid | 0.188 | rebel |
| tamil-eelam | #0087ab | h225-deep | 0.211 | rebel |
| tianwan | #008c8c | h195-deep | 0.181 | rebel |
| tigray-people-s-liberation-front | #4fa8e1 | h240-mid | 0.190 | rebel |
| transcaspian-provisional-government | #ca933e | h075-mid | 0.215 | rebel |
| trunajaya-rebellion | #578b35 | h135-deep | 0.213 | rebel |
| unita | #b85e31 | h045-deep | 0.240 | rebel |
| united-belgian-states | #578b35 | h135-deep | no neighbour | rebel |
| vistahm | #df8071 | h030-mid | 0.202 | rebel |
| vologases-vi | #b16512 | h060-deep | 0.201 | rebel |
| wa-state | #00b5b5 | h195-mid | 0.131 | rebel |
| wang-shichong-s-zheng | #aa8dde | h300-mid | 0.120 | rebel |
| wang-tiao | #ba87d2 | h315-mid | 0.207 | rebel |
| western-shu | #aaa23f | h105-mid | 0.121 | rebel |
| wu-geng | #69a1e8 | h255-mid | 0.182 | rebel |
| wu-sangui-s-zhou | #a45b9f | h330-deep | 0.156 | rebel |
| xi-dynasty | #46b68c | h165-mid | 0.197 | rebel |
| xiao-ji-s-rebel-state | #d58b4b | h060-mid | 0.187 | rebel |
| xiao-xian-s-liang | #008c8c | h195-deep | 0.209 | rebel |
| xu-yuanlang-s-lu | #008c8c | h195-deep | 0.209 | rebel |
| xue-ju-s-qin | #4fa8e1 | h240-mid | 0.148 | rebel |
| yan-an-lushan | #da7d9b | h000-mid | 0.200 | rebel |
| yellow-turbans | #578b35 | h135-deep | 0.193 | rebel |
| yemeni-royalists | #95a94e | h120-mid | 0.190 | rebel |
| yin-ten-kingdoms | #c882c2 | h330-mid | 0.147 | rebel |
| zanj-rebellion | #af578c | h345-deep | 0.207 | rebel |
| zhang-chu | #bb9b39 | h090-mid | 0.202 | rebel |
| zhang-shicheng-s-wu | #63b376 | h150-mid | 0.204 | rebel |
| zhizhi-xiongnu | #718516 | h120-deep | 0.210 | rebel |
| zubayrid-caliphate | #348f4f | h150-deep | 0.173 | rebel |
| abdallab | #dc855d | h045-mid | 0.182 | wheel |
| abhira-dynasty | #dc855d | h045-mid | 0.170 | wheel |
| abydos-dynasty | #b65577 | h000-deep | 0.270 | wheel |
| acarnanian-league | #867d00 | h105-deep | 0.171 | wheel |
| acciaioli-duchy-of-athens | #aa8dde | h300-mid | 0.120 | wheel |
| adriatic-veneti | #8766bb | h300-deep | 0.154 | wheel |
| aedui | #348f4f | h150-deep | 0.225 | wheel |
| aequi | #66cfe1 | h210-light | 0.167 | wheel |
| ah-canul | #46b68c | h165-mid | 0.168 | wheel |
| ah-kin-chel | #eda4cc | h345-light | 0.157 | wheel |
| ahlatshahs | #63b376 | h150-mid | 0.124 | wheel |
| ahmadilis | #718516 | h120-deep | 0.206 | wheel |
| ahom-kingdom | #8766bb | h300-deep | 0.165 | wheel |
| ainu | #0c82bf | h240-deep | 0.210 | wheel |
| airgialla | #a46e00 | h075-deep | 0.124 | wheel |
| ajuran-sultanate | #ba5661 | h015-deep | 0.228 | wheel |
| akragas | #b85e31 | h045-deep | 0.229 | wheel |
| akwamu | #24b6a1 | h180-mid | 0.148 | wheel |
| akyem-abuakwa | #b65577 | h000-deep | 0.204 | wheel |
| alania | #46b68c | h165-mid | 0.120 | wheel |
| alans-of-orleans | #348f4f | h150-deep | no neighbour | wheel |
| alash-autonomy | #af578c | h345-deep | 0.187 | wheel |
| alashiya | #bb584a | h030-deep | no neighbour | wheel |
| alchon-huns | #8766bb | h300-deep | 0.154 | wheel |
| alemanni | #00b5b5 | h195-mid | 0.146 | wheel |
| all-palestine-government | #867d00 | h105-deep | no neighbour | wheel |
| allied-occupied-germany | #819ae9 | h270-mid | 0.120 | wheel |
| allobroges | #0087ab | h225-deep | 0.200 | wheel |
| alsace-lorraine | #c882c2 | h330-mid | 0.207 | wheel |
| alwar-state | #7daf61 | h135-mid | 0.175 | wheel |
| amirate-of-qazaghan | #da7d9b | h000-mid | 0.132 | wheel |
| ammon | #65d2d2 | h195-light | 0.107 | wheel |
| amurru | #24b6a1 | h180-mid | no neighbour | wheel |
| ananda-gotrika-dynasty | #4fa8e1 | h240-mid | 0.149 | wheel |
| ancient-estonia | #09b2c7 | h210-mid | 0.206 | wheel |
| andhra-ikshvaku | #b85e31 | h045-deep | 0.207 | wheel |
| anga-kingdom | #a45b9f | h330-deep | 0.259 | wheel |
| anhui-clique | #009068 | h165-deep | 0.173 | wheel |
| annazids | #ba87d2 | h315-mid | 0.161 | wheel |
| antes | #a46e00 | h075-deep | 0.206 | wheel |
| arab-kingdom-of-syria | #df7e86 | h015-mid | 0.226 | wheel |
| aram-damascus | #46b68c | h165-mid | 0.150 | wheel |
| archbishopric-of-magdeburg | #30add6 | h225-mid | 0.108 | wheel |
| archbishopric-of-riga | #b85e31 | h045-deep | 0.154 | wheel |
| arghun-dynasty | #0c82bf | h240-deep | 0.174 | wheel |
| aro-confederacy | #008c8c | h195-deep | 0.147 | wheel |
| artuqids | #009068 | h165-deep | 0.125 | wheel |
| arverni | #5d74c7 | h270-deep | 0.216 | wheel |
| arzawa | #967600 | h090-deep | 0.213 | wheel |
| atabegs-of-yazd | #a45b9f | h330-deep | 0.127 | wheel |
| athens | #d58b4b | h060-mid | 0.120 | wheel |
| aulikara-dynasty | #30add6 | h225-mid | 0.137 | wheel |
| awlad-muhammad-dynasty | #a45b9f | h330-deep | 0.187 | wheel |
| awsan | #bb584a | h030-deep | no neighbour | wheel |
| aymara-kingdoms | #008e7d | h180-deep | 0.199 | wheel |
| azcapotzalco | #bb584a | h030-deep | 0.184 | wheel |
| ba | #736dc3 | h285-deep | 0.248 | wheel |
| bagirmi-sultanate | #30add6 | h225-mid | 0.133 | wheel |
| bahawalpur-state | #63b376 | h150-mid | 0.133 | wheel |
| balbani-sultanate-of-bengal | #ba5661 | h015-deep | 0.206 | wheel |
| banu-ifran | #b16512 | h060-deep | 0.180 | wheel |
| banu-kanz | #09b2c7 | h210-mid | 0.138 | wheel |
| banu-khazrun | #407bc5 | h255-deep | 0.209 | wheel |
| banu-khurasan | #578b35 | h135-deep | 0.213 | wheel |
| banu-makki | #bb584a | h030-deep | 0.228 | wheel |
| banu-mazyad | #867d00 | h105-deep | 0.152 | wheel |
| banu-munqidh | #00b5b5 | h195-mid | 0.138 | wheel |
| banu-qasi | #69a1e8 | h255-mid | 0.168 | wheel |
| banu-thabit | #008c8c | h195-deep | 0.207 | wheel |
| baol | #70ccee | h225-light | 0.133 | wheel |
| baroda-state | #407bc5 | h255-deep | 0.231 | wheel |
| basutoland | #008a9b | h210-deep | 0.196 | wheel |
| benin-empire | #4fa8e1 | h240-mid | 0.149 | wheel |
| betsimisaraka-kingdom | #a45b9f | h330-deep | 0.201 | wheel |
| beylik-of-constantine | #46b68c | h165-mid | 0.168 | wheel |
| bharatpur-state | #008a9b | h210-deep | 0.159 | wheel |
| bhauma-kara-dynasty | #008e7d | h180-deep | 0.175 | wheel |
| bhopal-state | #407bc5 | h255-deep | 0.231 | wheel |
| bikaner-state | #aa8dde | h300-mid | 0.126 | wheel |
| bilala-kingdom | #b85e31 | h045-deep | 0.213 | wheel |
| bishopric-of-courland | #a45b9f | h330-deep | 0.173 | wheel |
| bishopric-of-dorpat | #00b5b5 | h195-mid | 0.131 | wheel |
| bishopric-of-osel-wiek | #009068 | h165-deep | 0.190 | wheel |
| bit-adini | #d58b4b | h060-mid | 0.194 | wheel |
| bit-agusi | #00b5b5 | h195-mid | 0.173 | wheel |
| bit-bahiani | #008e7d | h180-deep | 0.212 | wheel |
| bit-yakin | #718516 | h120-deep | 0.216 | wheel |
| blemmyes | #30add6 | h225-mid | 0.239 | wheel |
| boeotian-league | #aaa23f | h105-mid | 0.120 | wheel |
| boii | #e4b572 | h075-light | 0.168 | wheel |
| boina-kingdom | #46b68c | h165-mid | 0.209 | wheel |
| bonny-kingdom | #b16512 | h060-deep | no neighbour | wheel |
| bono-state | #967600 | h090-deep | 0.159 | wheel |
| bosnia-eyalet | #46b68c | h165-mid | 0.145 | wheel |
| bou-regreg-republic | #63b376 | h150-mid | 0.168 | wheel |
| brigantes | #578b35 | h135-deep | 0.247 | wheel |
| british-mandate-for-palestine | #df7e86 | h015-mid | no neighbour | wheel |
| bruttii | #578b35 | h135-deep | 0.219 | wheel |
| bukey-horde | #bb584a | h030-deep | no neighbour | wheel |
| bukharan-people-s-soviet-republic | #bb9b39 | h090-mid | 0.167 | wheel |
| bundi-state | #c7c274 | h105-light | 0.122 | wheel |
| bundu | #ba5661 | h015-deep | 0.212 | wheel |
| burgraviate-of-nuremberg | #c7c274 | h105-light | 0.122 | wheel |
| burhan-al-din-state | #09b2c7 | h210-mid | 0.148 | wheel |
| burid-dynasty | #d58b4b | h060-mid | 0.139 | wheel |
| buyeo | #a46e00 | h075-deep | 0.168 | wheel |
| cacaxtla | #008e7d | h180-deep | 0.227 | wheel |
| calakmul | #819ae9 | h270-mid | 0.149 | wheel |
| can-pech | #9793e6 | h285-mid | 0.195 | wheel |
| cantabri | #8766bb | h300-deep | 0.204 | wheel |
| capua | #63b376 | h150-mid | 0.146 | wheel |
| caracol | #718516 | h120-deep | 0.206 | wheel |
| carchemish | #aa8dde | h300-mid | 0.190 | wheel |
| carrara-lordship-of-padua | #bb9b39 | h090-mid | 0.128 | wheel |
| catuvellauni | #ba5661 | h015-deep | 0.206 | wheel |
| cayor | #24b6a1 | h180-mid | 0.133 | wheel |
| ceh-pech | #95a94e | h120-mid | 0.216 | wheel |
| celtiberians | #718516 | h120-deep | 0.223 | wheel |
| cenomani | #d37faf | h345-mid | 0.154 | wheel |
| central-lithuania | #ba5661 | h015-deep | no neighbour | wheel |
| chahamanas-of-ranastambhapura | #df8071 | h030-mid | 0.101 | wheel |
| chakan | #80c7f8 | h240-light | 0.159 | wheel |
| chakan-putum | #95a94e | h120-mid | 0.238 | wheel |
| chalcidian-league | #967600 | h090-deep | 0.238 | wheel |
| chalukyas-of-lata | #bb9b39 | h090-mid | 0.149 | wheel |
| chan-santa-cruz | #407bc5 | h255-deep | 0.226 | wheel |
| changsha-kingdom | #009068 | h165-deep | 0.136 | wheel |
| characene | #ba5661 | h015-deep | 0.153 | wheel |
| chatti | #819ae9 | h270-mid | 0.240 | wheel |
| chengjia | #9760af | h315-deep | 0.184 | wheel |
| chera-perumal-kingdom | #b65577 | h000-deep | 0.155 | wheel |
| cherusci | #578b35 | h135-deep | 0.247 | wheel |
| chetumal | #867d00 | h105-deep | 0.200 | wheel |
| chichen-itza | #867d00 | h105-deep | 0.200 | wheel |
| chikinchel | #69a1e8 | h255-mid | 0.187 | wheel |
| chincha-kingdom | #008a9b | h210-deep | 0.228 | wheel |
| cholula | #a45b9f | h330-deep | 0.201 | wheel |
| chosokabe-clan | #009068 | h165-deep | 0.323 | wheel |
| chouchi | #65d2d2 | h195-light | 0.116 | wheel |
| chutia-kingdom | #63b376 | h150-mid | 0.208 | wheel |
| chutu-dynasty | #008a9b | h210-deep | 0.169 | wheel |
| circassia | #7daf61 | h135-mid | 0.118 | wheel |
| co-principality-of-andorra | #af578c | h345-deep | 0.185 | wheel |
| coba | #008c8c | h195-deep | 0.227 | wheel |
| cochuah | #69a1e8 | h255-mid | 0.201 | wheel |
| colla-kingdom | #df8071 | h030-mid | 0.208 | wheel |
| cook-islands | #a45b9f | h330-deep | no neighbour | wheel |
| copan | #008e7d | h180-deep | 0.232 | wheel |
| corinth | #008a9b | h210-deep | 0.181 | wheel |
| county-of-diepholz | #0c82bf | h240-deep | 0.196 | wheel |
| county-of-east-frisia | #0c82bf | h240-deep | 0.196 | wheel |
| county-of-hainaut | #66cfe1 | h210-light | 0.122 | wheel |
| county-of-hanau | #69a1e8 | h255-mid | 0.148 | wheel |
| county-of-henneberg | #bb584a | h030-deep | 0.201 | wheel |
| county-of-holstein | #bb9b39 | h090-mid | 0.132 | wheel |
| county-of-hoya | #70ccee | h225-light | 0.120 | wheel |
| county-of-katzenelnbogen | #bb9b39 | h090-mid | 0.137 | wheel |
| county-of-la-marche | #d37faf | h345-mid | 0.120 | wheel |
| county-of-lippe | #e4b572 | h075-light | 0.100 | wheel |
| county-of-mansfeld | #d58b4b | h060-mid | 0.170 | wheel |
| county-of-mark | #30add6 | h225-mid | 0.120 | wheel |
| county-of-montbeliard | #718516 | h120-deep | 0.154 | wheel |
| county-of-namur | #bb9b39 | h090-mid | 0.122 | wheel |
| county-of-nassau | #30add6 | h225-mid | 0.118 | wheel |
| county-of-oettingen | #f7a597 | h030-light | 0.115 | wheel |
| county-of-oldenburg | #a45b9f | h330-deep | 0.177 | wheel |
| county-of-ponthieu | #9793e6 | h285-mid | 0.150 | wheel |
| county-of-provence | #aaa23f | h105-mid | 0.103 | wheel |
| county-of-ravensberg | #30add6 | h225-mid | 0.120 | wheel |
| county-of-schaumburg | #aaa23f | h105-mid | 0.117 | wheel |
| county-of-schaumburg-lippe | #bb584a | h030-deep | 0.174 | wheel |
| county-of-schwerin | #5d74c7 | h270-deep | 0.174 | wheel |
| county-of-sens | #aa8dde | h300-mid | 0.175 | wheel |
| county-of-stolberg | #008a9b | h210-deep | 0.100 | wheel |
| county-of-tyrol | #bb9b39 | h090-mid | 0.145 | wheel |
| county-of-waldeck | #0c82bf | h240-deep | 0.196 | wheel |
| county-of-wied | #a46e00 | h075-deep | 0.209 | wheel |
| county-of-zutphen | #008c8c | h195-deep | no neighbour | wheel |
| croatia-in-union-with-hungary | #c7c274 | h105-light | no neighbour | wheel |
| croton | #5d74c7 | h270-deep | 0.206 | wheel |
| cuan-clan | #008c8c | h195-deep | 0.130 | wheel |
| cupul | #8ed09c | h150-light | 0.101 | wheel |
| curonians | #5d74c7 | h270-deep | 0.185 | wheel |
| cutch-state | #407bc5 | h255-deep | 0.197 | wheel |
| cyrene-and-barca | #ba5661 | h015-deep | 0.181 | wheel |
| cyrene-under-ptolemy-viii | #c882c2 | h330-mid | 0.169 | wheel |
| dachanghe | #d37faf | h345-mid | 0.146 | wheel |
| dacian-kingdom | #24b6a1 | h180-mid | 0.207 | wheel |
| dahomey | #718516 | h120-deep | 0.169 | wheel |
| dai-baidi | #867d00 | h105-deep | 0.264 | wheel |
| dai-sixteen-kingdoms | #008a9b | h210-deep | 0.110 | wheel |
| daifang-commandery | #a4bbff | h270-light | 0.150 | wheel |
| dalmatae | #8766bb | h300-deep | 0.204 | wheel |
| damagaram | #b85e31 | h045-deep | 0.187 | wheel |
| dangchang-kingdom | #df7e86 | h015-mid | 0.168 | wheel |
| danish-estonia | #a4bbff | h270-light | 0.115 | wheel |
| danubian-suebi | #dc855d | h045-mid | 0.170 | wheel |
| dar-al-kuti | #008c8c | h195-deep | 0.250 | wheel |
| date-clan | #a46e00 | h075-deep | 0.206 | wheel |
| davaka | #b85e31 | h045-deep | 0.218 | wheel |
| deheubarth | #f7a597 | h030-light | 0.101 | wheel |
| delian-league | #95a94e | h120-mid | 0.120 | wheel |
| dendi-kingdom | #a45b9f | h330-deep | 0.157 | wheel |
| deng | #407bc5 | h255-deep | 0.184 | wheel |
| dengzhi | #c7aff5 | h300-light | 0.159 | wheel |
| denkyira | #0087ab | h225-deep | 0.269 | wheel |
| dervish-state | #00b5b5 | h195-mid | 0.123 | wheel |
| despotate-of-angelokastron-and-lepanto | #a2cd8b | h135-light | 0.193 | wheel |
| deva-dynasty | #5d74c7 | h270-deep | 0.206 | wheel |
| dian | #0087ab | h225-deep | 0.202 | wheel |
| diarra | #a45b9f | h330-deep | 0.183 | wheel |
| dila-iya-sultanate | #4fa8e1 | h240-mid | 0.168 | wheel |
| dingnan-circuit | #718516 | h120-deep | 0.101 | wheel |
| dong-ou | #008e7d | h180-deep | 0.267 | wheel |
| donghu | #b85e31 | h045-deep | 0.214 | wheel |
| dos-pilas | #819ae9 | h270-mid | 0.231 | wheel |
| dou-rong | #aaa23f | h105-mid | 0.207 | wheel |
| duan-governors-of-dali | #407bc5 | h255-deep | 0.155 | wheel |
| duan-liaoxi | #ba87d2 | h315-mid | 0.126 | wheel |
| duan-qi | #348f4f | h150-deep | 0.195 | wheel |
| duchy-of-alsace | #dc855d | h045-mid | 0.235 | wheel |
| duchy-of-arenberg | #ba5661 | h015-deep | 0.195 | wheel |
| duchy-of-bar | #aaa23f | h105-mid | 0.107 | wheel |
| duchy-of-berg | #bb9b39 | h090-mid | 0.122 | wheel |
| duchy-of-berry | #b5c87d | h120-light | 0.132 | wheel |
| duchy-of-brunswick-luneburg | #f4a988 | h045-light | 0.132 | wheel |
| duchy-of-carinthia | #66cfe1 | h210-light | 0.131 | wheel |
| duchy-of-cieszyn | #6dd3c0 | h180-light | 0.142 | wheel |
| duchy-of-cleves | #70ccee | h225-light | 0.120 | wheel |
| duchy-of-eczyca-1231-1352 | #09b2c7 | h210-mid | 0.118 | wheel |
| duchy-of-ferrara | #30add6 | h225-mid | 0.120 | wheel |
| duchy-of-francia | #aaa23f | h105-mid | 0.172 | wheel |
| duchy-of-guelders | #bb9b39 | h090-mid | 0.122 | wheel |
| duchy-of-julich-berg | #578b35 | h135-deep | 0.137 | wheel |
| duchy-of-livonia | #bb9b39 | h090-mid | 0.169 | wheel |
| duchy-of-lotharingia | #aaa23f | h105-mid | 0.107 | wheel |
| duchy-of-lower-lorraine | #df8071 | h030-mid | 0.117 | wheel |
| duchy-of-lucca | #dc855d | h045-mid | 0.116 | wheel |
| duchy-of-mantua | #c882c2 | h330-mid | 0.111 | wheel |
| duchy-of-massa-and-carrara | #30add6 | h225-mid | 0.117 | wheel |
| duchy-of-opava | #819ae9 | h270-mid | 0.118 | wheel |
| duchy-of-orleans | #d6aaea | h315-light | no neighbour | wheel |
| duchy-of-oswiecim | #d7bb70 | h090-light | 0.117 | wheel |
| duchy-of-pomerania | #30add6 | h225-mid | 0.120 | wheel |
| duchy-of-pomerelia | #f3a3bb | h000-light | 0.107 | wheel |
| duchy-of-romagna | #967600 | h090-deep | no neighbour | wheel |
| duchy-of-saxe-coburg-saalfeld | #65d2d2 | h195-light | 0.116 | wheel |
| duchy-of-saxe-gotha-altenburg | #6dd3c0 | h180-light | 0.105 | wheel |
| duchy-of-saxe-hildburghausen | #da7d9b | h000-mid | 0.106 | wheel |
| duchy-of-saxe-lauenburg | #e3a6dd | h330-light | 0.101 | wheel |
| duchy-of-saxe-merseburg | #eeae7b | h060-light | 0.158 | wheel |
| duchy-of-saxe-weimar | #69a1e8 | h255-mid | 0.149 | wheel |
| duchy-of-saxe-weissenfels | #d6aaea | h315-light | 0.100 | wheel |
| duchy-of-saxe-zeitz | #92c1fd | h255-light | 0.100 | wheel |
| duchy-of-schleswig | #af578c | h345-deep | 0.149 | wheel |
| duchy-of-sieradz | #a4bbff | h270-light | 0.150 | wheel |
| duchy-of-urbino | #63b376 | h150-mid | 0.146 | wheel |
| duchy-of-wurttemberg | #718516 | h120-deep | 0.154 | wheel |
| duchy-of-zahringen | #bb9b39 | h090-mid | 0.153 | wheel |
| dughlat-emirate | #bb584a | h030-deep | 0.207 | wheel |
| dvaravati | #008c8c | h195-deep | 0.212 | wheel |
| dyfed | #b85e31 | h045-deep | 0.213 | wheel |
| earldom-of-orkney | #009068 | h165-deep | 0.208 | wheel |
| east-hebei-autonomous-council | #bb584a | h030-deep | no neighbour | wheel |
| east-zhou | #69a1e8 | h255-mid | 0.168 | wheel |
| eastern-buyeo | #736dc3 | h285-deep | 0.221 | wheel |
| eastern-chalukyas | #ca933e | h075-mid | 0.196 | wheel |
| eastern-guo | #c882c2 | h330-mid | 0.193 | wheel |
| eastern-rumelia | #9760af | h315-deep | 0.229 | wheel |
| ebla | #a45b9f | h330-deep | no neighbour | wheel |
| edom | #d37faf | h345-mid | 0.161 | wheel |
| egba-united-government | #b16512 | h060-deep | 0.147 | wheel |
| ekab | #0c82bf | h240-deep | 0.226 | wheel |
| eldiguzids | #df8071 | h030-mid | 0.120 | wheel |
| electoral-palatinate | #da7d9b | h000-mid | 0.106 | wheel |
| electorate-of-cologne | #f3a3bb | h000-light | 0.107 | wheel |
| electorate-of-mainz | #b16512 | h060-deep | 0.119 | wheel |
| elymais | #d58b4b | h060-mid | 0.153 | wheel |
| emirate-of-abdelkader | #46b68c | h165-mid | 0.168 | wheel |
| emirate-of-bani-khalid | #9760af | h315-deep | 0.229 | wheel |
| emirate-of-brakna | #24b6a1 | h180-mid | 0.145 | wheel |
| emirate-of-cyrenaica | #7daf61 | h135-mid | 0.242 | wheel |
| emirate-of-derbent | #da7d9b | h000-mid | 0.117 | wheel |
| emirate-of-harar | #736dc3 | h285-deep | 0.213 | wheel |
| emirate-of-mount-lebanon | #736dc3 | h285-deep | 0.230 | wheel |
| emirate-of-multan | #a45b9f | h330-deep | 0.183 | wheel |
| emirate-of-tarsus | #b16512 | h060-deep | 0.202 | wheel |
| emirate-of-tbilisi | #867d00 | h105-deep | 0.188 | wheel |
| emirate-of-trarza | #da7d9b | h000-mid | 0.180 | wheel |
| emishi | #0c82bf | h240-deep | 0.226 | wheel |
| eretnids | #09b2c7 | h210-mid | 0.145 | wheel |
| eshnunna | #aaa23f | h105-mid | 0.170 | wheel |
| fante-confederacy | #00b5b5 | h195-mid | 0.206 | wheel |
| far-eastern-republic | #009068 | h165-deep | 0.173 | wheel |
| fengtian-clique | #b16512 | h060-deep | 0.147 | wheel |
| fihrid-governors-of-al-andalus | #da7d9b | h000-mid | 0.189 | wheel |
| first-deva-dynasty | #348f4f | h150-deep | 0.239 | wheel |
| first-dynasty-of-ur | #00b5b5 | h195-mid | 0.190 | wheel |
| first-east-turkestan-republic | #df8071 | h030-mid | 0.281 | wheel |
| fourteenth-dynasty-of-egypt | #9760af | h315-deep | 0.254 | wheel |
| franconian-circle | #967600 | h090-deep | no neighbour | wheel |
| free-city-of-danzig-1807-1814 | #b85e31 | h045-deep | 0.205 | wheel |
| free-imperial-city-of-cologne | #b65577 | h000-deep | 0.216 | wheel |
| free-imperial-city-of-lubeck | #30add6 | h225-mid | 0.108 | wheel |
| free-imperial-city-of-nuremberg | #718516 | h120-deep | 0.154 | wheel |
| free-imperial-city-of-ulm | #30add6 | h225-mid | 0.118 | wheel |
| free-province-of-guayaquil | #af578c | h345-deep | 0.236 | wheel |
| free-territory-of-trieste | #ba5661 | h015-deep | 0.214 | wheel |
| fuladu | #b85e31 | h045-deep | no neighbour | wheel |
| further-austria | #f3a3bb | h000-light | 0.173 | wheel |
| futa-toro | #aaa23f | h105-mid | 0.146 | wheel |
| gajaaga | #008e7d | h180-deep | 0.154 | wheel |
| gajapati-kingdom | #4fa8e1 | h240-mid | 0.145 | wheel |
| garamantes | #b16512 | h060-deep | 0.202 | wheel |
| garhwal-kingdom | #407bc5 | h255-deep | 0.118 | wheel |
| gattilusi | #0c82bf | h240-deep | 0.208 | wheel |
| gaya | #00b5b5 | h195-mid | 0.170 | wheel |
| gaza-empire | #aa8dde | h300-mid | 0.120 | wheel |
| geledi-sultanate | #5d74c7 | h270-deep | 0.206 | wheel |
| general-government | #63b376 | h150-mid | 0.201 | wheel |
| gododdin | #008c8c | h195-deep | 0.134 | wheel |
| gongsun-liaodong | #c882c2 | h330-mid | 0.150 | wheel |
| gongsun-zan | #09b2c7 | h210-mid | 0.193 | wheel |
| gothic-foederati | #ba5661 | h015-deep | no neighbour | wheel |
| grand-duchy-of-frankfurt | #b7b5fc | h285-light | 0.141 | wheel |
| great-chu | #8766bb | h300-deep | no neighbour | wheel |
| great-perm | #00b5b5 | h195-mid | 0.211 | wheel |
| great-qi | #df7e86 | h015-mid | 0.237 | wheel |
| griqualand-east | #009068 | h165-deep | 0.279 | wheel |
| griqualand-west | #008e7d | h180-deep | 0.165 | wheel |
| guhilas-of-mewar | #ba5661 | h015-deep | 0.136 | wheel |
| guiyi-circuit | #718516 | h120-deep | 0.193 | wheel |
| gujarat-sultanate | #d58b4b | h060-mid | 0.120 | wheel |
| guominjun | #30add6 | h225-mid | 0.213 | wheel |
| gurgum | #dc855d | h045-mid | 0.214 | wheel |
| gwalior-state | #63b376 | h150-mid | 0.119 | wheel |
| gwiriko | #b85e31 | h045-deep | 0.173 | wheel |
| gyaman | #008e7d | h180-deep | 0.159 | wheel |
| ha-tien | #7daf61 | h135-mid | 0.119 | wheel |
| habsburg-netherlands | #4fa8e1 | h240-mid | 0.130 | wheel |
| hadiya-sultanate | #008e7d | h180-deep | 0.204 | wheel |
| hafsids-of-bejaia | #da7d9b | h000-mid | 0.185 | wheel |
| haixi-jurchens | #24b6a1 | h180-mid | 0.220 | wheel |
| hamath | #008e7d | h180-deep | 0.221 | wheel |
| han-sui | #aa8dde | h300-mid | 0.120 | wheel |
| hasanwayhids | #d58b4b | h060-mid | 0.153 | wheel |
| hatay-state | #da7d9b | h000-mid | 0.190 | wheel |
| hatra | #8766bb | h300-deep | 0.191 | wheel |
| hayasa-azzi | #bb9b39 | h090-mid | 0.169 | wheel |
| hazaraspids | #9760af | h315-deep | 0.131 | wheel |
| hecatomnid-caria | #c882c2 | h330-mid | no neighbour | wheel |
| hellenic-state | #9793e6 | h285-mid | 0.203 | wheel |
| helvetii | #008c8c | h195-deep | 0.208 | wheel |
| hermunduri | #bb9b39 | h090-mid | 0.203 | wheel |
| heruli | #a4bbff | h270-light | 0.132 | wheel |
| herzegovina-eyalet | #c7aff5 | h300-light | 0.226 | wheel |
| high-priests-of-amun-at-thebes | #407bc5 | h255-deep | 0.277 | wheel |
| hindu-shahis | #9760af | h315-deep | 0.153 | wheel |
| hiraab-imamate | #348f4f | h150-deep | 0.185 | wheel |
| hospitaller-rhodes | #0087ab | h225-deep | 0.167 | wheel |
| hospitaller-tripoli | #8766bb | h300-deep | 0.289 | wheel |
| hu-luohe | #008a9b | h210-deep | 0.215 | wheel |
| huainan | #d37faf | h345-mid | 0.154 | wheel |
| huang | #df7e86 | h015-mid | 0.215 | wheel |
| hunza-and-nagar | #09b2c7 | h210-mid | 0.121 | wheel |
| ibadan-republic | #e4b572 | h075-light | 0.224 | wheel |
| iceni | #009068 | h165-deep | 0.200 | wheel |
| ife-empire | #0c82bf | h240-deep | 0.207 | wheel |
| igala-kingdom | #63b376 | h150-mid | 0.147 | wheel |
| ijebu-kingdom | #578b35 | h135-deep | 0.158 | wheel |
| ikhshidid-dynasty | #bb584a | h030-deep | 0.224 | wheel |
| ilorin-emirate | #4fa8e1 | h240-mid | 0.120 | wheel |
| imagawa-clan | #46b68c | h165-mid | 0.186 | wheel |
| imamate-of-aussa | #00b5b5 | h195-mid | 0.207 | wheel |
| imamate-of-futa-jallon | #ba5661 | h015-deep | 0.228 | wheel |
| indore-state | #9793e6 | h285-mid | 0.147 | wheel |
| insubres | #63b376 | h150-mid | 0.158 | wheel |
| isin | #00b5b5 | h195-mid | 0.170 | wheel |
| isuwa | #0087ab | h225-deep | no neighbour | wheel |
| italian-governorate-of-montenegro | #ba87d2 | h315-mid | 0.237 | wheel |
| itureans | #8766bb | h300-deep | 0.136 | wheel |
| jahwarid-taifa-of-cordoba | #8ed09c | h150-light | 0.148 | wheel |
| jaipur-state | #5d74c7 | h270-deep | 0.158 | wheel |
| jaisalmer-state | #c7c274 | h105-light | 0.119 | wheel |
| janjira-state | #8766bb | h300-deep | 0.172 | wheel |
| jeongan | #967600 | h090-deep | 0.246 | wheel |
| jhalawar-state | #a46e00 | h075-deep | 0.186 | wheel |
| jhansi-state | #407bc5 | h255-deep | 0.231 | wheel |
| ji-beijing | #9760af | h315-deep | 0.233 | wheel |
| ji-shandong | #24b6a1 | h180-mid | 0.172 | wheel |
| jiang-gushi | #736dc3 | h285-deep | 0.215 | wheel |
| jiang-zhengyang | #a45b9f | h330-deep | 0.200 | wheel |
| jianzhou-jurchens | #8766bb | h300-deep | 0.205 | wheel |
| jinghai-circuit | #819ae9 | h270-mid | 0.120 | wheel |
| jolof-empire | #0087ab | h225-deep | 0.218 | wheel |
| jolof-kingdom | #f4a988 | h045-light | 0.167 | wheel |
| ju | #348f4f | h150-deep | 0.172 | wheel |
| jurchen-confederation | #df7e86 | h015-mid | 0.215 | wheel |
| k-iche-kingdom | #7daf61 | h135-mid | 0.207 | wheel |
| kaabu | #736dc3 | h285-deep | 0.154 | wheel |
| kaarta | #0c82bf | h240-deep | 0.183 | wheel |
| kachari-kingdom | #b85e31 | h045-deep | 0.147 | wheel |
| kakuyids | #009068 | h165-deep | 0.144 | wheel |
| kalachuris-of-kalyani | #bb9b39 | h090-mid | 0.190 | wheel |
| kalachuris-of-mahishmati | #819ae9 | h270-mid | 0.120 | wheel |
| kalachuris-of-ratnapura | #df7e86 | h015-mid | 0.121 | wheel |
| kalachuris-of-tripuri | #80c7f8 | h240-light | 0.134 | wheel |
| kalhora-dynasty | #ba87d2 | h315-mid | 0.208 | wheel |
| kammanu | #736dc3 | h285-deep | 0.110 | wheel |
| kangju | #4fa8e1 | h240-mid | 0.119 | wheel |
| kangra-state | #0087ab | h225-deep | 0.145 | wheel |
| kaqchikel-kingdom | #5d74c7 | h270-deep | 0.206 | wheel |
| kara-del | #ba87d2 | h315-mid | 0.229 | wheel |
| karagwe | #348f4f | h150-deep | 0.183 | wheel |
| karangasem-lombok | #5d74c7 | h270-deep | no neighbour | wheel |
| karelians | #578b35 | h135-deep | 0.178 | wheel |
| karnat-dynasty-of-mithila | #63b376 | h150-mid | 0.146 | wheel |
| kashi-kingdom | #736dc3 | h285-deep | 0.248 | wheel |
| kaska | #348f4f | h150-deep | 0.173 | wheel |
| kathiri-sultanate | #b65577 | h000-deep | 0.158 | wheel |
| kedah-kingdom | #348f4f | h150-deep | 0.154 | wheel |
| kenedougou-kingdom | #b16512 | h060-deep | 0.193 | wheel |
| kengtung | #c7aff5 | h300-light | 0.148 | wheel |
| kerait | #967600 | h090-deep | 0.198 | wheel |
| kerman-seljuk-sultanate | #63b376 | h150-mid | 0.152 | wheel |
| khairpur-state | #9760af | h315-deep | no neighbour | wheel |
| khalji-dynasty-of-bengal | #df8071 | h030-mid | 0.208 | wheel |
| khalkha-khanates | #a45b9f | h330-deep | 0.248 | wheel |
| khanate-of-kalat | #ca933e | h075-mid | 0.125 | wheel |
| khandesh-sultanate | #24b6a1 | h180-mid | 0.102 | wheel |
| khasso | #af578c | h345-deep | 0.234 | wheel |
| khitan-confederation | #867d00 | h105-deep | 0.185 | wheel |
| khorezm-people-s-soviet-republic | #407bc5 | h255-deep | 0.299 | wheel |
| khorshidi-dynasty | #00b5b5 | h195-mid | 0.104 | wheel |
| kilwa-sultanate | #bb584a | h030-deep | no neighbour | wheel |
| kingdom-of-abkhazia | #30add6 | h225-mid | 0.111 | wheel |
| kingdom-of-albania | #ca933e | h075-mid | 0.200 | wheel |
| kingdom-of-allada | #af578c | h345-deep | 0.207 | wheel |
| kingdom-of-altava | #0087ab | h225-deep | 0.233 | wheel |
| kingdom-of-ankole | #348f4f | h150-deep | 0.183 | wheel |
| kingdom-of-artsakh | #63b376 | h150-mid | 0.117 | wheel |
| kingdom-of-aru | #718516 | h120-deep | 0.194 | wheel |
| kingdom-of-bau | #b65577 | h000-deep | no neighbour | wheel |
| kingdom-of-beni-abbas | #bb584a | h030-deep | 0.159 | wheel |
| kingdom-of-buganda | #967600 | h090-deep | 0.203 | wheel |
| kingdom-of-bunyoro | #30add6 | h225-mid | 0.168 | wheel |
| kingdom-of-burebista | #63b376 | h150-mid | 0.158 | wheel |
| kingdom-of-burundi | #718516 | h120-deep | 0.130 | wheel |
| kingdom-of-butua | #736dc3 | h285-deep | 0.207 | wheel |
| kingdom-of-cochin | #0c82bf | h240-deep | 0.120 | wheel |
| kingdom-of-connacht | #0c82bf | h240-deep | 0.207 | wheel |
| kingdom-of-coorg | #0087ab | h225-deep | 0.171 | wheel |
| kingdom-of-d-mt | #b85e31 | h045-deep | no neighbour | wheel |
| kingdom-of-damot | #348f4f | h150-deep | 0.201 | wheel |
| kingdom-of-dardania | #578b35 | h135-deep | 0.126 | wheel |
| kingdom-of-desmond | #578b35 | h135-deep | 0.184 | wheel |
| kingdom-of-dublin | #009068 | h165-deep | 0.209 | wheel |
| kingdom-of-elmet | #6dd3c0 | h180-light | 0.121 | wheel |
| kingdom-of-emesa | #b16512 | h060-deep | no neighbour | wheel |
| kingdom-of-epirus | #9793e6 | h285-mid | 0.120 | wheel |
| kingdom-of-fazughli | #a45b9f | h330-deep | 0.183 | wheel |
| kingdom-of-gaochang | #967600 | h090-deep | 0.206 | wheel |
| kingdom-of-haiti | #008c8c | h195-deep | 0.227 | wheel |
| kingdom-of-herod-agrippa-i | #a46e00 | h075-deep | no neighbour | wheel |
| kingdom-of-hormuz | #867d00 | h105-deep | 0.120 | wheel |
| kingdom-of-jimma | #8766bb | h300-deep | 0.204 | wheel |
| kingdom-of-kaffa | #008e7d | h180-deep | 0.204 | wheel |
| kingdom-of-kakheti-hereti | #c7c274 | h105-light | 0.133 | wheel |
| kingdom-of-kandy | #008a9b | h210-deep | 0.135 | wheel |
| kingdom-of-kars | #967600 | h090-deep | 0.235 | wheel |
| kingdom-of-kasanje | #df8071 | h030-mid | 0.174 | wheel |
| kingdom-of-kauai | #a46e00 | h075-deep | no neighbour | wheel |
| kingdom-of-kazembe | #ba5661 | h015-deep | 0.214 | wheel |
| kingdom-of-kebbi | #df8071 | h030-mid | 0.174 | wheel |
| kingdom-of-kerma | #736dc3 | h285-deep | 0.257 | wheel |
| kingdom-of-kinda | #b85e31 | h045-deep | 0.224 | wheel |
| kingdom-of-kotte | #d37faf | h345-mid | 0.190 | wheel |
| kingdom-of-kucha | #718516 | h120-deep | 0.210 | wheel |
| kingdom-of-kuku | #9760af | h315-deep | 0.159 | wheel |
| kingdom-of-lagos | #bb584a | h030-deep | 0.184 | wheel |
| kingdom-of-leinster | #69a1e8 | h255-mid | 0.200 | wheel |
| kingdom-of-loango | #008a9b | h210-deep | 0.200 | wheel |
| kingdom-of-lombardy-venetia | #da7d9b | h000-mid | no neighbour | wheel |
| kingdom-of-lotharingia | #7daf61 | h135-mid | 0.120 | wheel |
| kingdom-of-lotharingia-zwentibold | #95a94e | h120-mid | no neighbour | wheel |
| kingdom-of-manipur | #8766bb | h300-deep | 0.147 | wheel |
| kingdom-of-mapungubwe | #bb584a | h030-deep | no neighbour | wheel |
| kingdom-of-marwar | #65d2d2 | h195-light | 0.106 | wheel |
| kingdom-of-matamba | #69a1e8 | h255-mid | 0.194 | wheel |
| kingdom-of-maui | #967600 | h090-deep | no neighbour | wheel |
| kingdom-of-meath | #d58b4b | h060-mid | 0.124 | wheel |
| kingdom-of-mewar | #09b2c7 | h210-mid | 0.106 | wheel |
| kingdom-of-munster | #a46e00 | h075-deep | 0.235 | wheel |
| kingdom-of-mycenae | #bb584a | h030-deep | 0.240 | wheel |
| kingdom-of-nagpur | #5d74c7 | h270-deep | 0.218 | wheel |
| kingdom-of-naples-bourbon | #867d00 | h105-deep | 0.152 | wheel |
| kingdom-of-ndongo | #dc855d | h045-mid | 0.195 | wheel |
| kingdom-of-noricum | #348f4f | h150-deep | 0.266 | wheel |
| kingdom-of-odoacer | #95a94e | h120-mid | 0.146 | wheel |
| kingdom-of-opobo | #407bc5 | h255-deep | 0.231 | wheel |
| kingdom-of-paeonia | #bb9b39 | h090-mid | 0.122 | wheel |
| kingdom-of-porto-novo | #0087ab | h225-deep | 0.134 | wheel |
| kingdom-of-porus | #718516 | h120-deep | 0.233 | wheel |
| kingdom-of-pylos | #967600 | h090-deep | 0.222 | wheel |
| kingdom-of-rwanda | #b16512 | h060-deep | 0.130 | wheel |
| kingdom-of-samoa | #736dc3 | h285-deep | no neighbour | wheel |
| kingdom-of-sikkim | #e3a6dd | h330-light | 0.119 | wheel |
| kingdom-of-sitawaka | #4fa8e1 | h240-mid | 0.135 | wheel |
| kingdom-of-syunik | #9793e6 | h285-mid | 0.127 | wheel |
| kingdom-of-tahiti | #b16512 | h060-deep | no neighbour | wheel |
| kingdom-of-tambapanni | #9760af | h315-deep | no neighbour | wheel |
| kingdom-of-taqali | #5d74c7 | h270-deep | no neighbour | wheel |
| kingdom-of-tashir-dzoraget | #a46e00 | h075-deep | 0.219 | wheel |
| kingdom-of-the-aures | #008a9b | h210-deep | 0.217 | wheel |
| kingdom-of-the-lombards | #7daf61 | h135-mid | 0.120 | wheel |
| kingdom-of-thomond | #b85e31 | h045-deep | 0.166 | wheel |
| kingdom-of-tonga | #348f4f | h150-deep | no neighbour | wheel |
| kingdom-of-toro | #df7e86 | h015-mid | 0.206 | wheel |
| kingdom-of-tripura | #69a1e8 | h255-mid | 0.119 | wheel |
| kingdom-of-tungning | #008c8c | h195-deep | 0.212 | wheel |
| kingdom-of-whydah | #69a1e8 | h255-mid | 0.134 | wheel |
| kingdom-of-zimbabwe | #009068 | h165-deep | 0.217 | wheel |
| kiribati | #736dc3 | h285-deep | no neighbour | wheel |
| kish | #da7d9b | h000-mid | 0.120 | wheel |
| kizzuwatna | #ca933e | h075-mid | 0.190 | wheel |
| koch-bihar | #008a9b | h210-deep | 0.148 | wheel |
| koch-hajo | #f3a3bb | h000-light | 0.189 | wheel |
| kolhapur-state | #0c82bf | h240-deep | 0.216 | wheel |
| koliya | #b85e31 | h045-deep | 0.207 | wheel |
| kong-empire | #578b35 | h135-deep | 0.184 | wheel |
| kota-state | #f3a3bb | h000-light | 0.158 | wheel |
| kowoj | #967600 | h090-deep | 0.224 | wheel |
| kuai | #63b376 | h150-mid | 0.164 | wheel |
| kuba-kingdom | #008a9b | h210-deep | 0.200 | wheel |
| kubang-pasu | #b65577 | h000-deep | no neighbour | wheel |
| kumaon-kingdom | #008c8c | h195-deep | 0.118 | wheel |
| kummuh | #00b5b5 | h195-mid | no neighbour | wheel |
| kumul-khanate | #af578c | h345-deep | no neighbour | wheel |
| kuninda-kingdom | #0c82bf | h240-deep | 0.152 | wheel |
| kurdistan-region | #eda4cc | h345-light | 0.132 | wheel |
| kuru-kingdom | #5d74c7 | h270-deep | 0.214 | wheel |
| kutai-martadipura | #a45b9f | h330-deep | no neighbour | wheel |
| kutrigurs | #00b5b5 | h195-mid | 0.241 | wheel |
| kwararafa | #8766bb | h300-deep | 0.183 | wheel |
| lagash | #aa8dde | h300-mid | 0.120 | wheel |
| lai | #c882c2 | h330-mid | 0.190 | wheel |
| landgraviate-of-hesse | #8766bb | h300-deep | 0.155 | wheel |
| landgraviate-of-hesse-darmstadt | #ca933e | h075-mid | 0.149 | wheel |
| landgraviate-of-hesse-kassel | #c882c2 | h330-mid | 0.174 | wheel |
| landgraviate-of-hesse-marburg | #ca933e | h075-mid | 0.167 | wheel |
| landgraviate-of-hesse-rheinfels | #9760af | h315-deep | 0.271 | wheel |
| landgraviate-of-thuringia | #70ccee | h225-light | 0.106 | wheel |
| langah-sultanate | #30add6 | h225-mid | 0.145 | wheel |
| langkasuka | #a46e00 | h075-deep | 0.115 | wheel |
| larsa | #da7d9b | h000-mid | 0.171 | wheel |
| later-hojo-clan | #0c82bf | h240-deep | 0.196 | wheel |
| latin-league | #9793e6 | h285-mid | 0.167 | wheel |
| launggyet-kingdom | #d7bb70 | h090-light | 0.150 | wheel |
| league-of-corinth | #af578c | h345-deep | no neighbour | wheel |
| league-of-free-laconians | #5d74c7 | h270-deep | 0.253 | wheel |
| league-of-the-islanders | #ba87d2 | h315-mid | 0.125 | wheel |
| lelang-commandery | #f4a988 | h045-light | 0.145 | wheel |
| licchavi-kingdom | #5d74c7 | h270-deep | 0.241 | wheel |
| ligures | #c882c2 | h330-mid | 0.180 | wheel |
| lihyan | #967600 | h090-deep | 0.160 | wheel |
| lim-dynasty-of-mari | #009068 | h165-deep | 0.171 | wheel |
| liu-biao | #c882c2 | h330-mid | 0.166 | wheel |
| liu-lu-an | #008a9b | h210-deep | 0.215 | wheel |
| liu-yong | #ba87d2 | h315-mid | 0.207 | wheel |
| liu-zhang | #4fa8e1 | h240-mid | 0.120 | wheel |
| livonians | #4fa8e1 | h240-mid | 0.183 | wheel |
| lombard-league | #ba5661 | h015-deep | no neighbour | wheel |
| lordship-of-albarracin | #46b68c | h165-mid | 0.208 | wheel |
| lordship-of-argos-and-nauplia | #bb584a | h030-deep | 0.153 | wheel |
| lordship-of-chios | #867d00 | h105-deep | 0.202 | wheel |
| lordship-of-galloway | #df8071 | h030-mid | 0.170 | wheel |
| lordship-of-milan | #b7b5fc | h285-light | 0.132 | wheel |
| lordship-of-salona | #95a94e | h120-mid | 0.150 | wheel |
| lordship-of-the-isles | #bb584a | h030-deep | 0.216 | wheel |
| lozi-kingdom | #a46e00 | h075-deep | 0.173 | wheel |
| lu-fang | #aaa23f | h105-mid | 0.207 | wheel |
| luba-empire | #008c8c | h195-deep | 0.197 | wheel |
| lucanians | #eeae7b | h060-light | 0.142 | wheel |
| lulong-circuit | #d37faf | h345-mid | 0.174 | wheel |
| luo | #af578c | h345-deep | 0.181 | wheel |
| lupaca-kingdom | #819ae9 | h270-mid | 0.199 | wheel |
| lusitanians | #578b35 | h135-deep | 0.247 | wheel |
| lutici | #967600 | h090-deep | 0.205 | wheel |
| luwu | #ba5661 | h015-deep | 0.214 | wheel |
| lycian-league | #00b5b5 | h195-mid | no neighbour | wheel |
| macedon-281-277 | #df8071 | h030-mid | 0.122 | wheel |
| macedonian-republics | #aaa23f | h105-mid | 0.204 | wheel |
| madhya-bharat | #578b35 | h135-deep | 0.243 | wheel |
| madurai-sultanate | #407bc5 | h255-deep | 0.197 | wheel |
| maghrawa | #9793e6 | h285-mid | 0.120 | wheel |
| maimana-khanate | #578b35 | h135-deep | 0.138 | wheel |
| makololo-kingdom | #0087ab | h225-deep | no neighbour | wheel |
| maldives | #b65577 | h000-deep | no neighbour | wheel |
| malwa-sultanate | #819ae9 | h270-mid | 0.120 | wheel |
| mam-kingdom | #0c82bf | h240-deep | 0.233 | wheel |
| mamluk-beys-of-egypt | #0c82bf | h240-deep | 0.208 | wheel |
| mamluk-iraq | #9793e6 | h285-mid | 0.174 | wheel |
| manchukuo | #af578c | h345-deep | no neighbour | wheel |
| mandara-kingdom | #b16512 | h060-deep | 0.154 | wheel |
| mangkunegaran | #a45b9f | h330-deep | 0.189 | wheel |
| mangyul-gungthang | #008a9b | h210-deep | 0.184 | wheel |
| maori-king-movement | #407bc5 | h255-deep | 0.231 | wheel |
| mapuche | #348f4f | h150-deep | 0.228 | wheel |
| marcellinus-dalmatia | #aaa23f | h105-mid | 0.208 | wheel |
| march-of-pannonia | #09b2c7 | h210-mid | 0.145 | wheel |
| march-of-styria | #aaa23f | h105-mid | no neighbour | wheel |
| march-of-tuscany | #80c7f8 | h240-light | 0.108 | wheel |
| march-of-verona | #24b6a1 | h180-mid | no neighbour | wheel |
| marcher-lordships | #867d00 | h105-deep | 0.152 | wheel |
| marcomanni | #9760af | h315-deep | 0.129 | wheel |
| margraviate-of-austria | #70ccee | h225-light | 0.123 | wheel |
| margraviate-of-baden | #b85e31 | h045-deep | 0.124 | wheel |
| margraviate-of-meissen | #4fa8e1 | h240-mid | 0.106 | wheel |
| mari | #008c8c | h195-deep | 0.202 | wheel |
| marquisate-of-bodonitsa | #eeae7b | h060-light | 0.127 | wheel |
| marquisate-of-montferrat | #bb584a | h030-deep | 0.170 | wheel |
| marwanids-of-diyar-bakr | #bb9b39 | h090-mid | 0.119 | wheel |
| masaesyli | #008a9b | h210-deep | 0.164 | wheel |
| massalia | #407bc5 | h255-deep | 0.209 | wheel |
| mathara-dynasty | #718516 | h120-deep | 0.190 | wheel |
| matsumae-domain | #b16512 | h060-deep | 0.210 | wheel |
| matsya-union | #69a1e8 | h255-mid | 0.248 | wheel |
| mauro-roman-kingdom | #b16512 | h060-deep | 0.193 | wheel |
| mayapan | #0c82bf | h240-deep | 0.226 | wheel |
| mecklenburg | #da7d9b | h000-mid | 0.109 | wheel |
| mecklenburg-strelitz | #ba87d2 | h315-mid | 0.150 | wheel |
| melayu-kingdom | #718516 | h120-deep | 0.194 | wheel |
| memel-territory | #b16512 | h060-deep | 0.277 | wheel |
| menabe-kingdom | #af578c | h345-deep | 0.180 | wheel |
| mengjiang | #69a1e8 | h255-mid | no neighbour | wheel |
| mengujekids | #d37faf | h345-mid | 0.150 | wheel |
| merkit | #af578c | h345-deep | 0.185 | wheel |
| merovingian-neustria | #ca933e | h075-mid | 0.250 | wheel |
| messapii | #009068 | h165-deep | 0.147 | wheel |
| messene | #008c8c | h195-deep | 0.115 | wheel |
| midrarid-dynasty | #b85e31 | h045-deep | 0.203 | wheel |
| mihrabanids | #d6aaea | h315-light | 0.132 | wheel |
| mirdasid-dynasty | #df7e86 | h015-mid | 0.147 | wheel |
| moab | #24b6a1 | h180-mid | 0.107 | wheel |
| moldavian-autonomous-soviet-socialist-republic | #867d00 | h105-deep | no neighbour | wheel |
| mon-city-states | #aa8dde | h300-mid | 0.120 | wheel |
| mong-mao | #09b2c7 | h210-mid | 0.155 | wheel |
| mori-clan | #008a9b | h210-deep | 0.163 | wheel |
| mossi-kingdoms | #a45b9f | h330-deep | 0.157 | wheel |
| mpondo-kingdom | #867d00 | h105-deep | 0.224 | wheel |
| mtetwa-paramountcy | #ba5661 | h015-deep | 0.225 | wheel |
| muang-phuan | #46b68c | h165-mid | 0.154 | wheel |
| muang-sua | #718516 | h120-deep | 0.154 | wheel |
| muisca-confederation | #a45b9f | h330-deep | 0.257 | wheel |
| musunuri-nayaks | #aa8dde | h300-mid | 0.155 | wheel |
| mutapa-empire | #bb584a | h030-deep | 0.207 | wheel |
| nagas-of-padmavati | #09b2c7 | h210-mid | 0.145 | wheel |
| naiman | #718516 | h120-deep | 0.234 | wheel |
| nala-dynasty | #0087ab | h225-deep | 0.191 | wheel |
| nan-kingdom | #aaa23f | h105-mid | 0.120 | wheel |
| nan-sarunai | #b65577 | h000-deep | no neighbour | wheel |
| naranjo | #9793e6 | h285-mid | 0.167 | wheel |
| nasrid-dynasty-of-sistan | #aa8dde | h300-mid | 0.144 | wheel |
| nauru | #008c8c | h195-deep | no neighbour | wheel |
| ndebele-kingdom | #009068 | h165-deep | 0.173 | wheel |
| ndwandwe-kingdom | #407bc5 | h255-deep | 0.206 | wheel |
| negara-daha | #0087ab | h225-deep | 0.269 | wheel |
| new-oyo | #aa8dde | h300-mid | 0.120 | wheel |
| ngoenyang | #718516 | h120-deep | 0.124 | wheel |
| niue | #009068 | h165-deep | no neighbour | wheel |
| nizari-ismaili-state | #c882c2 | h330-mid | 0.113 | wheel |
| northern-liang-of-gaochang | #967600 | h090-deep | 0.206 | wheel |
| northern-march | #0087ab | h225-deep | 0.196 | wheel |
| nri-kingdom | #867d00 | h105-deep | 0.152 | wheel |
| numayrid-dynasty | #92c1fd | h255-light | 0.201 | wheel |
| nupe-kingdom | #dc855d | h045-mid | 0.199 | wheel |
| oda-clan | #819ae9 | h270-mid | 0.163 | wheel |
| ogedeid-ulus | #008c8c | h195-deep | 0.118 | wheel |
| old-calabar | #a46e00 | h075-deep | no neighbour | wheel |
| old-pahang-sultanate | #4fa8e1 | h240-mid | 0.102 | wheel |
| old-prussians | #92c1fd | h255-light | 0.100 | wheel |
| operational-zone-of-the-adriatic-littoral | #e3a6dd | h330-light | 0.160 | wheel |
| operational-zone-of-the-alpine-foothills | #70ccee | h225-light | 0.160 | wheel |
| order-of-calatrava | #009068 | h165-deep | 0.279 | wheel |
| otomo-clan | #867d00 | h105-deep | 0.235 | wheel |
| pagaruyung-kingdom | #bb9b39 | h090-mid | 0.132 | wheel |
| pakualaman | #008c8c | h195-deep | 0.243 | wheel |
| palatinate-neuburg | #ca933e | h075-mid | 0.131 | wheel |
| palenque | #0087ab | h225-deep | 0.218 | wheel |
| palestinian-national-authority | #ba87d2 | h315-mid | 0.220 | wheel |
| panchala-kingdom | #24b6a1 | h180-mid | 0.214 | wheel |
| panduvamshi-dynasty | #008e7d | h180-deep | 0.175 | wheel |
| parthenopean-republic | #b65577 | h000-deep | no neighbour | wheel |
| pashalik-of-belgrade | #e4b572 | h075-light | 0.170 | wheel |
| pashalik-of-scutari | #b7b5fc | h285-light | 0.194 | wheel |
| pashalik-of-timbuktu | #008e7d | h180-deep | 0.218 | wheel |
| pashalik-of-yanina | #b65577 | h000-deep | 0.197 | wheel |
| pate-sultanate | #348f4f | h150-deep | 0.183 | wheel |
| pechenegs | #c882c2 | h330-mid | 0.108 | wheel |
| pedi-empire | #bb584a | h030-deep | 0.215 | wheel |
| peng-chong | #736dc3 | h285-deep | 0.240 | wheel |
| people-s-republic-of-zanzibar-and-pemba | #008e7d | h180-deep | no neighbour | wheel |
| peureulak-sultanate | #af578c | h345-deep | no neighbour | wheel |
| pi | #f3a3bb | h000-light | 0.105 | wheel |
| picentes | #95a94e | h120-mid | 0.185 | wheel |
| picts | #009068 | h165-deep | 0.208 | wheel |
| piedras-negras | #95a94e | h120-mid | 0.218 | wheel |
| pohnpei-chiefdoms | #ba5661 | h015-deep | no neighbour | wheel |
| portuguese-syriam | #736dc3 | h285-deep | no neighbour | wheel |
| prince-abbey-of-fulda | #718516 | h120-deep | 0.154 | wheel |
| prince-archbishopric-of-bremen | #30add6 | h225-mid | 0.108 | wheel |
| prince-archbishopric-of-salzburg | #da7d9b | h000-mid | 0.103 | wheel |
| prince-bishopric-of-augsburg | #b5c87d | h120-light | 0.122 | wheel |
| prince-bishopric-of-bamberg | #f7a3a9 | h015-light | 0.106 | wheel |
| prince-bishopric-of-brixen | #8766bb | h300-deep | 0.147 | wheel |
| prince-bishopric-of-constance | #30add6 | h225-mid | 0.118 | wheel |
| prince-bishopric-of-eichstatt | #aa8dde | h300-mid | 0.120 | wheel |
| prince-bishopric-of-freising | #ba87d2 | h315-mid | 0.132 | wheel |
| prince-bishopric-of-halberstadt | #80c7f8 | h240-light | 0.108 | wheel |
| prince-bishopric-of-hildesheim | #70ccee | h225-light | 0.123 | wheel |
| prince-bishopric-of-liege | #a2cd8b | h135-light | 0.117 | wheel |
| prince-bishopric-of-lubeck | #736dc3 | h285-deep | 0.240 | wheel |
| prince-bishopric-of-minden | #8ed09c | h150-light | 0.104 | wheel |
| prince-bishopric-of-montenegro | #bb9b39 | h090-mid | 0.128 | wheel |
| prince-bishopric-of-munster | #a2cd8b | h135-light | 0.100 | wheel |
| prince-bishopric-of-osnabruck | #df7e86 | h015-mid | 0.129 | wheel |
| prince-bishopric-of-paderborn | #0c82bf | h240-deep | 0.196 | wheel |
| prince-bishopric-of-passau | #967600 | h090-deep | 0.189 | wheel |
| prince-bishopric-of-speyer | #b5c87d | h120-light | 0.107 | wheel |
| prince-bishopric-of-strasbourg | #578b35 | h135-deep | 0.137 | wheel |
| prince-bishopric-of-trent | #578b35 | h135-deep | 0.137 | wheel |
| prince-bishopric-of-utrecht | #f3a3bb | h000-light | 0.107 | wheel |
| prince-bishopric-of-verden | #bb9b39 | h090-mid | 0.132 | wheel |
| prince-bishopric-of-warmia | #867d00 | h105-deep | 0.125 | wheel |
| prince-bishopric-of-worms | #f7a3a9 | h015-light | 0.106 | wheel |
| prince-bishopric-of-wurzburg | #d58b4b | h060-mid | 0.119 | wheel |
| prince-provostry-of-berchtesgaden | #a46e00 | h075-deep | 0.189 | wheel |
| princely-abbey-of-corvey | #bb584a | h030-deep | 0.174 | wheel |
| principality-of-albania-thopia | #4fa8e1 | h240-mid | 0.148 | wheel |
| principality-of-anhalt | #a2cd8b | h135-light | 0.117 | wheel |
| principality-of-ansbach | #a4bbff | h270-light | 0.151 | wheel |
| principality-of-armenia | #9793e6 | h285-mid | 0.105 | wheel |
| principality-of-bayreuth | #aa8dde | h300-mid | 0.120 | wheel |
| principality-of-herat | #da7d9b | h000-mid | 0.153 | wheel |
| principality-of-hohenzollern-hechingen | #30add6 | h225-mid | 0.120 | wheel |
| principality-of-kandahar | #69a1e8 | h255-mid | 0.150 | wheel |
| principality-of-liang-yunnan | #95a94e | h120-mid | 0.170 | wheel |
| principality-of-lower-pannonia | #7daf61 | h135-mid | 0.144 | wheel |
| principality-of-lucca-and-piombino | #d58b4b | h060-mid | 0.132 | wheel |
| principality-of-luneburg | #a2cd8b | h135-light | 0.117 | wheel |
| principality-of-murom | #7daf61 | h135-mid | 0.118 | wheel |
| principality-of-nassau-orange-fulda | #f7a3a9 | h015-light | 0.132 | wheel |
| principality-of-novgorod-seversk | #af578c | h345-deep | 0.150 | wheel |
| principality-of-raigama | #dc855d | h045-mid | 0.211 | wheel |
| principality-of-reuss-greiz | #5d74c7 | h270-deep | 0.201 | wheel |
| principality-of-rostov | #7daf61 | h135-mid | 0.118 | wheel |
| principality-of-rugen | #ca933e | h075-mid | no neighbour | wheel |
| principality-of-uglich | #6dd3c0 | h180-light | 0.132 | wheel |
| principality-of-wales | #df8071 | h030-mid | no neighbour | wheel |
| principality-of-yaroslavl | #d37faf | h345-mid | 0.184 | wheel |
| principality-of-zvenyhorod | #d58b4b | h060-mid | 0.216 | wheel |
| protectorate-of-bohemia-and-moravia | #736dc3 | h285-deep | 0.208 | wheel |
| provisional-government-of-hawaii | #b85e31 | h045-deep | no neighbour | wheel |
| provisional-government-of-the-republic-of-china | #7daf61 | h135-mid | 0.120 | wheel |
| puntland | #9793e6 | h285-mid | 0.146 | wheel |
| qatna | #0c82bf | h240-deep | 0.226 | wheel |
| qedar | #008e7d | h180-deep | 0.165 | wheel |
| qi-henan | #5d74c7 | h270-deep | 0.225 | wheel |
| qingyuan-circuit | #b65577 | h000-deep | 0.155 | wheel |
| quadi | #4fa8e1 | h240-mid | 0.190 | wheel |
| quanrong | #c882c2 | h330-mid | 0.193 | wheel |
| quedlinburg-abbey | #30add6 | h225-mid | 0.108 | wheel |
| quirigua | #008e7d | h180-deep | 0.232 | wheel |
| qutlugh-khanids | #dc855d | h045-mid | 0.171 | wheel |
| ran-wei | #ca933e | h075-mid | 0.195 | wheel |
| rapa-nui | #348f4f | h150-deep | no neighbour | wheel |
| rawadid-dynasty | #65d2d2 | h195-light | 0.133 | wheel |
| recherla-nayaks | #df7e86 | h015-mid | 0.138 | wheel |
| reddi-kingdom | #af578c | h345-deep | 0.138 | wheel |
| reformed-government-of-the-republic-of-china | #df7e86 | h015-mid | 0.208 | wheel |
| reichskommissariat-ostland | #dc855d | h045-mid | 0.286 | wheel |
| reichskommissariat-ukraine | #df7e86 | h015-mid | 0.221 | wheel |
| reorganized-national-government-of-china | #a46e00 | h075-deep | 0.121 | wheel |
| republic-of-abkhazia | #d58b4b | h060-mid | 0.239 | wheel |
| republic-of-artsakh | #008e7d | h180-deep | 0.253 | wheel |
| republic-of-geneva | #b16512 | h060-deep | 0.204 | wheel |
| republic-of-lucca | #df8071 | h030-mid | 0.106 | wheel |
| republic-of-siena | #df8071 | h030-mid | 0.145 | wheel |
| republic-of-siena-in-montalcino | #af578c | h345-deep | 0.236 | wheel |
| republic-of-south-ossetia | #a45b9f | h330-deep | 0.207 | wheel |
| republic-of-spanish-haiti | #24b6a1 | h180-mid | 0.223 | wheel |
| republic-of-the-marshall-islands | #a46e00 | h075-deep | no neighbour | wheel |
| republic-of-yucatan | #30add6 | h225-mid | 0.213 | wheel |
| restored-hanthawaddy-kingdom | #bb584a | h030-deep | 0.170 | wheel |
| rewa-state | #b5c87d | h120-light | 0.141 | wheel |
| riga | #b85e31 | h045-deep | 0.218 | wheel |
| rohilkhand-state | #7daf61 | h135-mid | 0.163 | wheel |
| rozvi-empire | #5d74c7 | h270-deep | 0.137 | wheel |
| ruhuna | #b65577 | h000-deep | 0.206 | wheel |
| russian-eastern-outskirts | #008c8c | h195-deep | no neighbour | wheel |
| saar-basin-territory | #95a94e | h120-mid | 0.287 | wheel |
| saar-protectorate | #b16512 | h060-deep | no neighbour | wheel |
| sabines | #f7a3a9 | h015-light | 0.185 | wheel |
| sahrawi-arab-democratic-republic | #bb9b39 | h090-mid | 0.234 | wheel |
| sakya-regime | #407bc5 | h255-deep | 0.118 | wheel |
| salankayana-dynasty | #8766bb | h300-deep | 0.183 | wheel |
| salghurids | #867d00 | h105-deep | 0.132 | wheel |
| sallarid-dynasty | #d58b4b | h060-mid | 0.117 | wheel |
| saloum | #c882c2 | h330-mid | 0.120 | wheel |
| saltukids | #b7b5fc | h285-light | 0.141 | wheel |
| sam-al | #736dc3 | h285-deep | 0.213 | wheel |
| samnites | #e3a6dd | h330-light | 0.142 | wheel |
| samoa | #ba5661 | h015-deep | no neighbour | wheel |
| san-marino | #009068 | h165-deep | no neighbour | wheel |
| sarmatians | #967600 | h090-deep | 0.125 | wheel |
| satara-state | #867d00 | h105-deep | 0.224 | wheel |
| satsuma-domain | #967600 | h090-deep | 0.270 | wheel |
| scaliger-lordship-of-verona | #f7a597 | h030-light | 0.140 | wheel |
| sciri | #7daf61 | h135-mid | 0.170 | wheel |
| sclaviniae-of-greece | #a46e00 | h075-deep | 0.206 | wheel |
| scordisci | #c882c2 | h330-mid | 0.180 | wheel |
| second-dynasty-of-lagash | #008e7d | h180-deep | 0.229 | wheel |
| seljuks-of-syria | #b16512 | h060-deep | 0.180 | wheel |
| semigallians | #d37faf | h345-mid | 0.173 | wheel |
| senones | #d37faf | h345-mid | 0.146 | wheel |
| senussi-order | #5d74c7 | h270-deep | 0.206 | wheel |
| sequani | #c882c2 | h330-mid | 0.180 | wheel |
| setul-mambang-segara | #b85e31 | h045-deep | 0.182 | wheel |
| shaddadids | #65d2d2 | h195-light | 0.133 | wheel |
| shaigiya | #008c8c | h195-deep | 0.244 | wheel |
| shakya | #8766bb | h300-deep | 0.207 | wheel |
| shanxi-clique | #ca933e | h075-mid | 0.120 | wheel |
| sharifate-of-mecca | #b65577 | h000-deep | 0.158 | wheel |
| sheikhdom-of-acre | #736dc3 | h285-deep | 0.230 | wheel |
| shen | #0087ab | h225-deep | 0.232 | wheel |
| shi-xie | #407bc5 | h255-deep | 0.192 | wheel |
| shimazu-clan | #0c82bf | h240-deep | 0.235 | wheel |
| shu | #867d00 | h105-deep | 0.252 | wheel |
| siak-sultanate | #009068 | h165-deep | 0.209 | wheel |
| sieben-zenden | #d37faf | h345-mid | 0.116 | wheel |
| sin-kashid-dynasty-of-uruk | #bb9b39 | h090-mid | 0.171 | wheel |
| sindhu-sauvira | #0087ab | h225-deep | no neighbour | wheel |
| sine | #df8071 | h030-mid | 0.117 | wheel |
| sip-song-chau-tai | #63b376 | h150-mid | 0.133 | wheel |
| slovak-republic | #f4a988 | h045-light | 0.201 | wheel |
| somaliland | #da7d9b | h000-mid | 0.146 | wheel |
| somavamshi-dynasty | #a46e00 | h075-deep | 0.170 | wheel |
| song-jian | #008e7d | h180-deep | 0.229 | wheel |
| soomra-dynasty | #69a1e8 | h255-mid | 0.170 | wheel |
| sotuta | #d7bb70 | h090-light | 0.101 | wheel |
| southern-court | #008a9b | h210-deep | no neighbour | wheel |
| spanish-march | #f3a3bb | h000-light | 0.117 | wheel |
| state-of-east-indonesia | #736dc3 | h285-deep | 0.235 | wheel |
| state-of-milan | #b7b5fc | h285-light | 0.132 | wheel |
| state-of-rabih-az-zubayr | #df7e86 | h015-mid | 0.154 | wheel |
| state-of-slovenes-croats-and-serbs | #348f4f | h150-deep | no neighbour | wheel |
| state-of-the-presidi | #9760af | h315-deep | no neighbour | wheel |
| stellaland | #967600 | h090-deep | 0.203 | wheel |
| stem-duchy-of-franconia | #df8071 | h030-mid | 0.106 | wheel |
| stem-duchy-of-saxony | #8ed09c | h150-light | 0.117 | wheel |
| stem-duchy-of-swabia | #65d2d2 | h195-light | 0.101 | wheel |
| subalpine-republic | #c882c2 | h330-mid | 0.170 | wheel |
| sufi-dynasty-of-khwarazm | #69a1e8 | h255-mid | 0.183 | wheel |
| sui-ningyang | #9760af | h315-deep | 0.213 | wheel |
| sultanate-of-agadez | #008c8c | h195-deep | 0.242 | wheel |
| sultanate-of-aussa | #af578c | h345-deep | 0.160 | wheel |
| sultanate-of-bacan | #8766bb | h300-deep | no neighbour | wheel |
| sultanate-of-berau | #0087ab | h225-deep | 0.147 | wheel |
| sultanate-of-buayan | #b65577 | h000-deep | 0.206 | wheel |
| sultanate-of-gobir | #8766bb | h300-deep | 0.175 | wheel |
| sultanate-of-gunung-tabur | #30add6 | h225-mid | 0.194 | wheel |
| sultanate-of-kano | #5d74c7 | h270-deep | 0.200 | wheel |
| sultanate-of-katsina | #7daf61 | h135-mid | 0.189 | wheel |
| sultanate-of-mogadishu | #008c8c | h195-deep | 0.228 | wheel |
| sultanate-of-mombasa | #009068 | h165-deep | 0.178 | wheel |
| sultanate-of-shewa | #a46e00 | h075-deep | no neighbour | wheel |
| sultanate-of-ternate | #407bc5 | h255-deep | 0.206 | wheel |
| sultanate-of-tidore | #578b35 | h135-deep | 0.197 | wheel |
| sumedang-larang | #ca933e | h075-mid | 0.146 | wheel |
| sun-ce | #008a9b | h210-deep | 0.178 | wheel |
| suphannaphum-kingdom | #a45b9f | h330-deep | 0.142 | wheel |
| swabian-circle | #578b35 | h135-deep | no neighbour | wheel |
| swazi-kingdom | #5d74c7 | h270-deep | 0.137 | wheel |
| sybaris | #ba5661 | h015-deep | 0.206 | wheel |
| syracuse | #008a9b | h210-deep | 0.174 | wheel |
| tahirid-dynasty | #009068 | h165-deep | 0.123 | wheel |
| taifa-of-lerida | #0c82bf | h240-deep | 0.138 | wheel |
| taifa-of-majorca | #967600 | h090-deep | no neighbour | wheel |
| taifa-of-malaga | #e3a6dd | h330-light | 0.101 | wheel |
| taifa-of-mertola | #ba87d2 | h315-mid | 0.132 | wheel |
| takeda-clan | #e4b572 | h075-light | 0.186 | wheel |
| tambralinga | #348f4f | h150-deep | 0.147 | wheel |
| tan | #407bc5 | h255-deep | 0.241 | wheel |
| taras | #967600 | h090-deep | 0.147 | wheel |
| tarcondimotid-kingdom | #9760af | h315-deep | 0.175 | wheel |
| tarhuntassa | #867d00 | h105-deep | 0.226 | wheel |
| tashkent-state | #aaa23f | h105-mid | 0.169 | wheel |
| tavastians | #9760af | h315-deep | no neighbour | wheel |
| telugu-chodas-of-nellore | #348f4f | h150-deep | 0.215 | wheel |
| territory-of-nauru | #0087ab | h225-deep | no neighbour | wheel |
| territory-of-the-military-commander-in-serbia | #da7d9b | h000-mid | 0.139 | wheel |
| tetrarchy-of-galilee-and-peraea | #b65577 | h000-deep | no neighbour | wheel |
| tetrarchy-of-philip | #ba5661 | h015-deep | no neighbour | wheel |
| thakuri-dynasty | #ba5661 | h015-deep | 0.259 | wheel |
| thessalian-league | #eda4cc | h345-light | 0.149 | wheel |
| thessalian-league-roman-era | #d37faf | h345-mid | 0.119 | wheel |
| third-dynasty-of-ur | #8766bb | h300-deep | 0.196 | wheel |
| third-republic-of-venezuela | #69a1e8 | h255-mid | 0.211 | wheel |
| thracian-goths | #a46e00 | h075-deep | 0.219 | wheel |
| three-leagues | #c882c2 | h330-mid | 0.111 | wheel |
| tikal | #46b68c | h165-mid | 0.167 | wheel |
| tir-eoghain | #af578c | h345-deep | 0.124 | wheel |
| tiwanaku-empire | #8766bb | h300-deep | no neighbour | wheel |
| tlaxcala | #95a94e | h120-mid | 0.215 | wheel |
| tmutarakan | #b16512 | h060-deep | 0.222 | wheel |
| tokhara-yabghus | #dc855d | h045-mid | 0.119 | wheel |
| tomara-dynasty | #0c82bf | h240-deep | 0.154 | wheel |
| tonina | #008a9b | h210-deep | 0.228 | wheel |
| tovata-confederacy | #a46e00 | h075-deep | no neighbour | wheel |
| toyotomi-clan | #718516 | h120-deep | 0.164 | wheel |
| traikutaka-dynasty | #30add6 | h225-mid | 0.137 | wheel |
| transcaucasian-democratic-federative-republic | #407bc5 | h255-deep | no neighbour | wheel |
| transnistria | #09b2c7 | h210-mid | 0.217 | wheel |
| travancore | #008e7d | h180-deep | 0.120 | wheel |
| travancore-cochin | #b65577 | h000-deep | 0.212 | wheel |
| trinovantes | #5d74c7 | h270-deep | 0.200 | wheel |
| tripolitanian-republic | #9760af | h315-deep | 0.257 | wheel |
| tsongkha | #736dc3 | h285-deep | 0.212 | wheel |
| tu-i-tonga-empire | #b65577 | h000-deep | no neighbour | wheel |
| tukulor-empire | #7daf61 | h135-mid | 0.193 | wheel |
| tunjur-kingdom | #008e7d | h180-deep | 0.220 | wheel |
| turkestan-assr | #578b35 | h135-deep | no neighbour | wheel |
| turkestan-autonomy | #b85e31 | h045-deep | 0.226 | wheel |
| turpan-khanate | #bb9b39 | h090-mid | 0.151 | wheel |
| tutul-xiu | #d58b4b | h060-mid | 0.117 | wheel |
| tututepec | #9760af | h315-deep | 0.239 | wheel |
| tuvalu | #578b35 | h135-deep | no neighbour | wheel |
| tuvan-people-s-republic | #819ae9 | h270-mid | 0.226 | wheel |
| twenty-fourth-dynasty-of-egypt | #819ae9 | h270-mid | 0.239 | wheel |
| tylis | #af578c | h345-deep | no neighbour | wheel |
| tz-utujil-kingdom | #b85e31 | h045-deep | 0.211 | wheel |
| uesugi-clan | #008a9b | h210-deep | 0.163 | wheel |
| ugarit | #af578c | h345-deep | 0.222 | wheel |
| ulaid | #736dc3 | h285-deep | 0.130 | wheel |
| umbri | #819ae9 | h270-mid | 0.146 | wheel |
| umma | #da7d9b | h000-mid | 0.120 | wheel |
| union-of-burma | #8ed09c | h150-light | 0.131 | wheel |
| united-provinces-of-central-italy | #30add6 | h225-mid | 0.124 | wheel |
| united-tribes-of-new-zealand | #008c8c | h195-deep | 0.257 | wheel |
| unyanyembe | #9760af | h315-deep | 0.219 | wheel |
| uqaylid-dynasty | #df8071 | h030-mid | 0.122 | wheel |
| urambo | #a46e00 | h075-deep | 0.219 | wheel |
| uruk | #d58b4b | h060-mid | 0.208 | wheel |
| utigurs | #b16512 | h060-deep | 0.222 | wheel |
| uxmal | #718516 | h120-deep | 0.206 | wheel |
| uzbek-khanate-of-abul-khayr | #f7a3a9 | h015-light | 0.132 | wheel |
| van-lang | #9760af | h315-deep | no neighbour | wheel |
| varman-dynasty-of-east-bengal | #578b35 | h135-deep | 0.213 | wheel |
| vatican-city | #736dc3 | h285-deep | 0.208 | wheel |
| venad | #0087ab | h225-deep | 0.145 | wheel |
| viceroyalty-of-naples | #af578c | h345-deep | 0.236 | wheel |
| videha | #578b35 | h135-deep | 0.259 | wheel |
| vishnukundina-dynasty | #c882c2 | h330-mid | 0.120 | wheel |
| volsci | #ca933e | h075-mid | 0.146 | wheel |
| waalo | #24b6a1 | h180-mid | 0.145 | wheel |
| wajo | #9793e6 | h285-mid | 0.174 | wheel |
| wari-empire | #af578c | h345-deep | 0.184 | wheel |
| warri-kingdom | #ba5661 | h015-deep | 0.260 | wheel |
| wassoulou-empire | #d37faf | h345-mid | 0.145 | wheel |
| wei-ao | #aaa23f | h105-mid | 0.207 | wheel |
| weibo-circuit | #a45b9f | h330-deep | no neighbour | wheel |
| wendat-confederacy | #9760af | h315-deep | no neighbour | wheel |
| west-berlin | #718516 | h120-deep | 0.168 | wheel |
| west-indies-federation | #00b5b5 | h195-mid | 0.239 | wheel |
| west-prussia | #09b2c7 | h210-mid | 0.232 | wheel |
| west-ukrainian-people-s-republic | #46b68c | h165-mid | 0.170 | wheel |
| western-ganga-dynasty | #dc855d | h045-mid | 0.155 | wheel |
| western-guo | #009068 | h165-deep | 0.170 | wheel |
| wituland | #348f4f | h150-deep | 0.183 | wheel |
| wuping-circuit | #da7d9b | h000-mid | 0.190 | wheel |
| xhosa-kingdom | #5d74c7 | h270-deep | 0.206 | wheel |
| xi | #008a9b | h210-deep | 0.200 | wheel |
| xianyu | #867d00 | h105-deep | no neighbour | wheel |
| xianyun | #348f4f | h150-deep | no neighbour | wheel |
| xiliangfu | #bb584a | h030-deep | 0.228 | wheel |
| xing | #008e7d | h180-deep | 0.120 | wheel |
| xochicalco | #af578c | h345-deep | no neighbour | wheel |
| xueyantuo | #b16512 | h060-deep | 0.185 | wheel |
| yamato | #b65577 | h000-deep | 0.226 | wheel |
| yamhad | #b65577 | h000-deep | 0.226 | wheel |
| yapese-empire | #407bc5 | h255-deep | no neighbour | wheel |
| yaxchilan | #0087ab | h225-deep | 0.218 | wheel |
| yaxha | #0087ab | h225-deep | 0.149 | wheel |
| yeke-kingdom | #9793e6 | h285-mid | 0.197 | wheel |
| yelang | #b65577 | h000-deep | 0.222 | wheel |
| yettishar | #0087ab | h225-deep | 0.124 | wheel |
| yiqu | #867d00 | h105-deep | 0.216 | wheel |
| yiwu-five-dynasties | #95a94e | h120-mid | 0.165 | wheel |
| yong-hubei | #a45b9f | h330-deep | 0.202 | wheel |
| yu | #30add6 | h225-mid | 0.169 | wheel |
| yuan-shao | #c882c2 | h330-mid | 0.166 | wheel |
| yuan-shu | #867d00 | h105-deep | 0.178 | wheel |
| yueban | #ca933e | h075-mid | 0.120 | wheel |
| yufirid-dynasty | #ba5661 | h015-deep | 0.206 | wheel |
| yuwen-xianbei | #b16512 | h060-deep | 0.183 | wheel |
| zamfara | #4fa8e1 | h240-mid | 0.175 | wheel |
| zamorin-of-kozhikode | #00b5b5 | h195-mid | 0.109 | wheel |
| zanzibari-domain-of-tippu-tip | #b65577 | h000-deep | 0.227 | wheel |
| zawiya-of-illigh | #578b35 | h135-deep | 0.221 | wheel |
| zazzau | #df7e86 | h015-mid | 0.208 | wheel |
| zeng | #5d74c7 | h270-deep | 0.233 | wheel |
| zhai-wei | #348f4f | h150-deep | 0.205 | wheel |
| zhang-bu | #aaa23f | h105-mid | 0.207 | wheel |
| zhang-lu | #95a94e | h120-mid | 0.207 | wheel |
| zhao-five-dynasties-period | #ba87d2 | h315-mid | 0.232 | wheel |
| zhili-clique | #9760af | h315-deep | 0.185 | wheel |
| zhongli | #407bc5 | h255-deep | 0.215 | wheel |
| zunbils | #09b2c7 | h210-mid | 0.138 | wheel |
