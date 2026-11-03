# Phase C: anchors and window drafts compiled from the dossiers

Written by `tools/compile_dossiers.py` (2026-11-03 run). One deterministic engine applies
`briefs/window-brief.md` section 3 (the twelve rules, keyframes versus the ledger, conflicts,
resolution) to every dossier for every year from 6000 BCE to 2026, starting from an empty world, and
slices the result into the 119 Phase D window drafts and their anchors. The window agents then review
and fix their window from its draft instead of compiling it themselves.

## How to run

```sh
mkdir -p /tmp/claude-0/work/compile-c && cd /tmp/claude-0/work/compile-c
python3 -I /mnt/project-files/history/tools/compile_dossiers.py --until 1900 --stage-only   # test: compile to 1900, compare 1600 and 1900 with Phase A, scratch only
python3 -I /mnt/project-files/history/tools/compile_dossiers.py                              # full run: writes and publishes everything below
python3 -I /mnt/project-files/history/tools/compile_dossiers.py --build-colonies             # the same, deriving data/colonies.csv again first (manual rows kept)
```

Re-run it after the dossiers or the gazetteer change: it copies new or changed dossiers from
`polities/` to `/tmp/claude-0/work/compile-c/polities/`, re-resolves only the region leaves whose
gazetteer tables changed (cache: `/tmp/claude-0/work/compile-c/cache/leaves.pkl`; `--refresh` drops it),
recompiles everything and rewrites `data/anchors-c/`, `compiled/_draft/`, the generated section of
`compiled/README.md` and this folder. Options: `--no-sync`, `--workers N`, `--stage-only` (leave the
outputs in `/tmp/claude-0/work/compile-c/stage/`), `--compare 1600,1900`, `--build-colonies`, `--no-rules`
(the size rule alone, without R1 and R2, for comparison). `data/colonies.csv` is read as it is when it
exists; it is derived (and published) only with `--build-colonies` or when it is missing.
This run: 120 s end to end (region resolution is the slow part on a cold cache).

## This run in numbers

| | |
| --- | --- |
| dossiers | 3,029 (0 unreadable or failing `tools/validate_dossier.py`, left out) |
| ledger events | 37,518: 37,358 applied, 160 skipped |
| events skipped because a region does not resolve | 37 (all unresolved specs, keyframes and successor lands included: 42) |
| distinct unresolved names | 18 (`unresolved_names.csv`) |
| conflicts the size rule still settles | 5,466 pairs, 542,279 cell-years (cells summed over the claims), 27,550 claims |
| settled by R2 (succession) | 2,030 pairs, 1,901,435 cell-years, 7,363 claims |
| settled by R3, a constituent against its parent | 199 pairs, 130,185 cell-years, 460 claims |
| settled by R3, a vassal against its parent | 100 pairs, 28,402 cell-years, 277 claims |
| settled by R3, two dossiers of one state | 6 pairs, 112,655 cell-years, 106 claims |
| data/hierarchy.csv | 696 rows, 696 spans applied (constituent, confidence 1 1, constituent, confidence 2 225, constituent, confidence 3 165, same_state, confidence 2 1, same_state, confidence 3 5, vassal, confidence 1 21, vassal, confidence 2 136, vassal, confidence 3 142); 0 notes in `hierarchy_check.csv`, 0 rows not applied |
| cells drawn in a hierarchy tint (R3), summed over the years | constituent 8,339,079; vassal 2,518,065 |
| settled by R1, a colony against another dossier | 661 pairs, 216,274 cell-years, 3,311 claims |
| settled by R1, two colonies of one metropole | 76 pairs, 922,121 cell-years, 1,254 claims |
| settled by rule 4, a vassal against its suzerain | 128 pairs, 68,641 cell-years, 561 claims |
| data/colonies.csv | 394 rows for 227 colony dossiers: 318 high, 65 medium, 11 low confidence; 9 rows without a metropole; 0 problems (`colonies_check.csv`) |
| keyframe snaps (dossier gaps) | 6,305 |
| anchors written | 121 |
| adjacent pairs (any year) | 12,992 |
| self-check | anchors reached 119 of 119; cells with two owners 0; change 'from' differing from the replay 0; cells listed twice in a year 0 |
| `*_end` events that close nothing open | 334 (contest_end 121, occupation_end 124, vassal_end 89; `unclosed_ends.csv`) |

Every counter of the run (`run_summary.json` has them all):

| counter | value |
| --- | --- |
| *_start applied after a same-year *_end of another dossier (ends first) | 412 |
| applied, no cell changed: contest_start | 243 |
| applied, no cell changed: gain | 1,736 |
| applied, no cell changed: loss | 988 |
| applied, no cell changed: merge | 47 |
| applied, no cell changed: occupation_start | 106 |
| applied, no cell changed: split | 120 |
| applied, no cell changed: vassal_start | 99 |
| birth from the first keyframe | 2 |
| birth with no land | 1 |
| cells changed | 8,838,544 |
| colony metropole relations opened | 382 |
| contest with nobody: nothing to blend | 3 |
| contest_end already closed this year by its pair | 697 |
| contest_end closed a relation | 2,395 |
| contest_end closes nothing open | 121 |
| contest_start merged into an open contest | 818 |
| counterpart matched by slugify | 232 |
| events applied | 37,358 |
| events skipped | 160 |
| gain: counterpart holds none of the region, took nobody's land | 1,483 |
| hierarchy relations opened (constituent, confidence 1) | 1 |
| hierarchy relations opened (constituent, confidence 2) | 225 |
| hierarchy relations opened (constituent, confidence 3) | 165 |
| hierarchy relations opened (vassal, confidence 1) | 21 |
| hierarchy relations opened (vassal, confidence 2) | 136 |
| hierarchy relations opened (vassal, confidence 3) | 142 |
| keyframe checks | 19,292 |
| keyframe resolves to no land cell | 30 |
| keyframe snaps | 6,305 |
| keyframe within tolerance | 12,987 |
| keyframe year with no resolvable keyframe | 4 |
| loss: applied as the counterpart's gain | 3,380 |
| merge whose counterpart has no living dossier that year | 42 |
| merge whose counterpart has no living dossier that year: applied as a gain from nobody | 17 |
| occupation_end already closed this year by its pair | 397 |
| occupation_end closed a relation | 977 |
| occupation_end closes nothing open | 124 |
| occupation_start merged into an open occupation | 513 |
| occupation_start recorded by the owner (roles reversed) | 810 |
| relations closed by a party's end | 827 |
| skipped: merge whose counterpart has no living dossier that year: nothing moved (the region holds none of nobody's cells) | 25 |
| skipped: region does not resolve | 37 |
| skipped: region resolves to no land cell (the event moves no land) | 35 |
| skipped: region resolves to no land cell and nothing is open | 3 |
| skipped: umbrella dossier (moves no cells) | 60 |
| successor without a living dossier: its land goes to nobody | 184 |
| vassal_end already closed this year by its pair | 229 |
| vassal_end closed a relation | 1,308 |
| vassal_end closes nothing open | 89 |
| vassal_start between a colony and its metropole: the metropole is the suzerain | 38 |
| vassal_start merged into an open relation | 279 |
| vassal_start over land neither holds: the smaller party is the vassal | 7 |
| vassal_start recorded by both: joined the counterpart's relation | 235 |
| vassal_start recorded by both: the vassal is the party whose shape holds the region | 182 |
| vassal_start recorded by the vassal (roles reversed) | 230 |
| vassal_start recorded by the vassal inside the suzerain's land (roles reversed) | 15 |
| vassal_start recorded by the vassal over its own land (roles reversed) | 10 |
| vassal_start with nobody: skipped | 1 |
| vassal_start: vassal holds none of the region, drawn as the suzerain's vassal land | 154 |

## Rule R3 (hierarchy)

`data/hierarchy.csv` (documented at the end of `data/README.md`) says which state sat inside which:
one row per child, parent and span (`child,parent,from,to,kind,confidence,evidence`), `kind`
constituent (a member of the parent: an Imperial Estate, a Soviet republic), vassal (its own ruler
under the parent's overlordship) or same_state (two dossiers drawing one state). The classifiers wrote
it from this folder's nested, same-state and colony pairs of 500 cell-years or more. R3 comes right
after R2 in the conflict order (see the list below):

- **same_state**: in the row's years the parent's dossier is drawn; the child's claims on cells the
  parent holds yield, and the parent's claims take the child's cells (kashmir over the Lohara and Utpala
  dynasties, the East India Company over `british-empire` 1757-1858, the Habsburg Netherlands over
  `habsburg-monarchy` 1487-1515).
- **constituent or vassal**, in a year of the row: on a cell both the child and the parent claim, the
  child owns it, with status `constituent` or `vassal` and suzerain the parent. **Chains**: when rows
  link three states (an Imperial Estate inside an estate inside the Empire), the deepest child wins
  against any ancestor and its suzerain is its immediate parent.
- **The tint**: a row of confidence 2 or 3 also gives the child's other cells that status and suzerain,
  for the row's years the child is alive, like a colony's metropole tint: a relation flagged
  `"hierarchy"` (`data/anchors-c/` relations, `handoff.open_vassals`) opens at the start of the row's
  first year (the change's `event` names the row) and closes at the start of the year after its last;
  land the child gains meanwhile takes the tint; a suzerainty the dossiers record with `vassal_start`
  shows over it, and the row's tint returns when that ends (the dossier wins where it has an event). A
  parent's keyframe counts its children's tinted cells as its own, so it no longer claims them. A row of
  confidence 1 changes only the cells R3 settles in a conflict.
- **Colonies** keep R1: a colony child's row applies only to years without a `data/colonies.csv` row.
- Spans are clipped to the years both dossiers are alive; rows the compiler could not apply (unknown
  slug, bad years, no common life) and every clipped span are listed in `hierarchy_check.csv`.

R3 conflicts settled this run: constituent: 199 pairs, 78,150 distinct cells, 130,185 cell-years; same state: 6 pairs, 6,831 distinct cells, 112,655 cell-years; vassal: 100 pairs, 16,961 distinct cells, 28,402 cell-years. Cells drawn in a hierarchy tint, summed over the years:
constituent 8,339,079; vassal 2,518,065.

## Rules R1 (colonies) and R2 (succession)

Most of the conflicts of the first run were structural: a colony against its metropole or its
aggregate (the Spanish Empire against its viceroyalties, French Africa against French West Africa,
the British colonial empire against the Australian colonies), and a state against its own predecessor
or successor (the RSFSR against the USSR, colonial Brazil against the Empire of Brazil). Two rules now
settle them before the size rule. A conflict is a found or a keyframe claiming a cell another
dossier holds; a cell that a dated ledger event of the same year moved is settled by that event first.
Then, in this order:

1. **R2, succession.** When B is A's successor (A's `identity.successors` or B's
   `identity.predecessors` names the other) and the year is at or after B's start, B owns the cell.
   When each lists the other, the one born later wins. R2 holds for the whole overlap, also when the
   listed successor is the older state (the Sumerian city-states, born -3400, are listed as the
   successor of Ur, Umma and Kish; window patches give those cities their own land). A switch in the
   script, `R2_BORN_AFTER` (off), would give R2 only to a successor born after its predecessor; it was
   tried in round 12 and left off, because it moved 1.27M owner cell-years in 86 windows reviewed under
   this rule (the pairs it moves: `/tmp/claude-0/work/r12/r2_moves.json`).
2. **Rulings** (`data/patches/<window>.json`, the section on patches below): a window agent's ruling for
   the pair and year, limited to its region's cells when it has one, names the winner (and optionally a
   status).
3. **R3, hierarchy** (`data/hierarchy.csv`, the section above): same_state rows draw the parent; in a
   constituent or vassal row the deepest child owns the cell, in its immediate parent's tint.
4. **Rule 4, a vassal keeps its land.** When one of the two is the other's open vassal (a
   `vassal_start` not yet closed), the vassal keeps or takes the cell, in its suzerain's tint. Without
   this R1 would let a colony's keyframe swallow the protectorates the colony itself records (the
   sultanates of the Dutch East Indies, the princely states of the British Empire in India).
5. **R1, colonies.** Each type-colony dossier has a metropole by years in `data/colonies.csv`. When
   two colonies of the same metropole claim a cell, the smaller (Cliopatria area that year, else the
   compiled area) owns it: the specific colony wins against the aggregate (Queensland against the
   British colonial empire, Anglo-Egyptian Sudan against British Africa). When a colony with a metropole
   that year and any other dossier claim a cell, the colony owns it.
6. Otherwise **the size rule**: the state with the smaller Cliopatria area that year wins.

**The colony tint.** Every colony cell carries status `vassal` with `suzerain` = the colony's metropole
for that year, with or without a conflict: the compiler opens a vassal relation flagged
`"colony": true` (`data/anchors-c/` relations, `handoff.open_vassals`) at the start of each
`colonies.csv` row, closes it when the row ends or the metropole changes, and puts it under any
suzerainty the ledger records for the colony (an explicit `vassal_start` shows above it; when that
ends, the metropole's tint returns). Land the colony gains later is tinted the same way; a contest or
occupation over colony land returns to the tint when it ends. A colony row without a metropole (a
Greek apoikia, a condominium, a year whose metropole has no dossier) leaves the colony an ordinary
state for those years.

**`data/colonies.csv`** has one row per colony and stretch of years: `colony, metropole, from, to,
basis, confidence` (`metropole` empty: no metropole those years). A metropole can change
(Spanish then Austrian Milan; the Dutch colonies under the Batavian Republic, the French Empire in
1811-1814 and the Netherlands). The file is derived by `derive_colonies` and can be edited by hand:
a row whose `basis` starts with `manual` survives a new derivation. The derivation scores, for every
colony and year, the candidate metropoles alive that year:

- the home states of the nation the colony's slug prefix or name names (`british-`, `french-`,
  `spanish-`, `portuguese-`, `dutch-`, "New France", "New Sweden"...): +3; else of a nation its notes
  name, up to +2 for the most named (the table `NATIONS` lists the home states of 29 nations);
- the same colour family as the colony, which follows the metropole's (+2.5, or +1.5 when the family
  holds several nations' home states, as France's holds the Netherlands' and Belgium's);
- the colony's suzerain in a first compile with the size rule only: +4;
- the candidate's keyframe shape holding the colony's that year (the sovereign state whose claim
  contains it): up to +2;
- mentions of the candidate in the dossier: up to +1; a predecessor or the found counterpart of the
  colony's own nation: +0.5.

An aggregate colony (British Africa, French Africa, the British colonial empire, German Africa...) is
a candidate too and stands for its own metropole, so every chain ends at a sovereign state, never at
another colony. When two home states of one nation are alive at once (the Spanish Empire and the
Kingdom of Spain, the Portuguese Empire and the Kingdom of Portugal, the Swedish Empire and the
Kingdom of Sweden, the USSR and the RSFSR) the one listed first in `NATIONS` is taken unless the other
scores more than a point higher. A metropole needs 2.5 points. Confidence: **high** at 5 points with a
lead of 2 over the best metropole of another nation, **medium** at 3 with a lead of 1, **low** below.
`COLONY_MANUAL` in the script fixes 18 colonies where the scores mislead (the Italian
possessions that passed from Spain to Austria, Saint-Domingue, Spanish Tunis, the Greek apoikiai
and the New Hebrides condominium without a metropole, the 1945 occupation governments in Korea,
Nauru); their basis says so.

The 11 low-confidence rows:

| colony | metropole | years | basis |
| --- | --- | --- | --- |
| berbice | dutch-republic | 1627..1795 | its notes name netherlands (1.00), same colour family (via dutch-cape-colony); score 3.50, lead 0.59; next: kingdom-of-france 2.91 |
| colony-of-norfolk-island | united-kingdom | 1856..1914 | its notes name britain (0.33), same colour family; 1 mention; score 2.97, lead 2.97; next: none |
| essequibo | dutch-republic | 1616..1780 | its notes name netherlands (1.00), same colour family (via dutch-cape-colony); score 3.50, lead 0.70; next: kingdom-of-france 2.80 |
| essequibo | kingdom-of-great-britain | 1781..1800 | its notes name britain (1.00); 10 mentions (via british-colonial-empire); score 3.00, lead -0.50; next: dutch-republic 3.50 |
| gandara | (none) | -329..-327 | no metropole: the best candidate, macedonian-empire, scores 1.00 (9 mentions) |
| hindush | (none) | -329..-325 | no metropole: the best candidate, macedonian-empire, scores 1.00 (15 mentions) |
| hospitaller-tripoli | (none) | 1530..1551 | no metropole: the best candidate, ottoman-empire, scores 2.18 (its notes name ottoman (0.77); 4 mentions) |
| jesuit-reducciones | spanish-empire | 1609..1767 | its notes name spain (1.00); 8 mentions; predecessor or found counterpart; score 3.50, lead 0.65; next: kingdom-of-portugal 2.85 |
| kwantung-leased-territory | russian-empire | 1898..1904 | its notes name russia (1.00); its shape holds 100% of the colony's; 18 mentions; score 5.00, lead 0.65; next: empire-of-japan 4.35 |
| protectorate-of-the-western-regions | (none) | 421..439 | no metropole: the best candidate, kingdom-of-kucha, scores 1.19 (its shape holds 10% of the colony's; 52 mentions) |
| province-of-quebec | kingdom-of-great-britain | 1763..1791 | its notes name britain (0.45), same colour family; 7 mentions; score 3.91, lead 0.91; next: united-states-of-america 3.00 |

**Engine fixes that went with the rules.** A `vassal_start` recorded by the vassal (the schema wants
the suzerain to record it, with the vassal as counterpart) used to make the vassal the suzerain in
several cases, and when both dossiers recorded the same vassalage the two records could open two
opposite relations. Checking the colony tint showed it: the Kingdom of Taqali was drawn as British
Africa's suzerain over 15,000 cells from 1898 and as Turco-Egyptian Sudan's over about 3,000 cells
1821-1884, Kongo as Portuguese Angola's over 1,190 cells 1859-1914, Ndongo as Angola's, and Belgium
as the Belgian Congo's vassal. The role rules in "How the brief was read" now settle these: the
metropole is always the suzerain of its own colony; for a same-year pair of records the party whose
shape holds the region is the vassal and the second record joins the first's relation (opposite
same-year relations went from 18 pairs to 0: Himyar under Axum, Aquitaine under France in 990, Ryukyu
under the Southern Ming, the Later Guptas under Harsha); a recorder that holds the region inside its
own shape, against a counterpart with land elsewhere and none of it there, is the vassal (Qatna under
Mitanni, Mitanni under the Hittites, Qocho under the Kara-Khitans, Chola under the Pandyas, Bima
under Gowa, Mengjiang under the Reorganized National Government); and a colony weighs as its
metropole when sizes decide. And a successor that has already ended in the same year's deaths no
longer receives land (Min kept 287 cells from 945 to 2026). In all, 47 of the 1,654 `vassal_start`
records now open a different relation or join one.

## The conflicts that remain

The size rule still settles 5,466 pairs (542,279 cell-years). The largest 60 pairs hold
24.6% of those cell-years, the largest 100 32.0%, 200 44.5% and 400 59.9%. By category
(the largest pairs categorised by hand, `CONFLICT_REVIEWED` in the script; the rest by a heuristic:
a type-rebel dossier; a shared Cliopatria name, Wikipedia title, Wikidata id or primary name; a colony of
another metropole or of none; one year's conflict reaching half the smaller state's area, nested;
otherwise unrelated):

| category | pairs | cell-years | share |
| --- | --- | --- | --- |
| unrelated | 3,817 | 256,469 | 47.3% |
| nested | 1,311 | 254,272 | 46.9% |
| rebel | 237 | 18,876 | 3.5% |
| colony | 95 | 12,539 | 2.3% |
| same state | 6 | 123 | 0.0% |

- **nested**: a state inside a larger one that is not its colony: the Central Asian SSRs inside the
  USSR, the stem duchies inside the Empire, the Rajput and princely states inside the Mughal Empire and
  the Raj, warlord cliques inside the Republic of China, nominal vassals of the Abbasid caliphate.
  These want a `vassal_start` in one of the two dossiers (or a keyframe that leaves the inner state
  out), not a compiler rule;
- **unrelated**: two distinct states whose shapes claim the same land (Tibet and the Republic of
  China, the Han and the Xiongnu, Mexico and the United States before 1848);
- **same state**: two dossiers for one state whose lives overlap (the British Empire in India and the
  East India Company; Kashmir and its Lohara dynasty);
- **rebel**: a type-rebel dossier against the state it rebels in;
- **colony**: a colony against a colony of another metropole, or one without a metropole.

The 60 largest:

| rank | pair | | category | cell-years | years | cells won by |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cuan-clan | liang-dynasty | nested | 8,807 | 502..555 | cuan-clan 8807 |
| 2 | cuan-clan | western-jin | nested | 8,257 | 327..418 | cuan-clan 8257 |
| 3 | mongol-empire | novgorod-republic | unrelated (heuristic) | 7,601 | 1241..1293 | novgorod-republic 7601 |
| 4 | cuan-clan | liu-song-dynasty | nested | 5,198 | 420..476 | cuan-clan 5198 |
| 5 | hotaki-dynasty | khanate-of-kalat | unrelated | 4,627 | 1718..1738 | khanate-of-kalat 4627 |
| 6 | abbasid-caliphate | saffarid-dynasty | nested (heuristic) | 4,431 | 861..905 | saffarid-dynasty 4431 |
| 7 | han-dynasty | xiongnu | unrelated | 4,319 | -127..91 | xiongnu 4241; han-dynasty 78 |
| 8 | eastern-gokturks | yenisei-kyrgyz | nested | 3,504 | 587..628 | yenisei-kyrgyz 3504 |
| 9 | tang-dynasty | tibetan-empire | unrelated | 3,480 | 638..840 | tang-dynasty 2588; tibetan-empire 892 |
| 10 | khwarezmid-empire | salghurids | nested | 3,100 | 1202..1216 | salghurids 3100 |
| 11 | kerait | liao-dynasty | nested | 3,090 | 1000..1124 | kerait 3090 |
| 12 | circassia | golden-horde | nested (heuristic) | 3,043 | 1294..1440 | circassia 3043 |
| 13 | communist-party-of-china | inner-mongolia | rebel (heuristic) | 2,888 | 1947..1948 | inner-mongolia 2888 |
| 14 | banu-kanz | ikhshidid-dynasty | nested (heuristic) | 2,717 | 943..947 | banu-kanz 2717 |
| 15 | cuan-clan | southern-qi | unrelated (heuristic) | 2,595 | 479..500 | cuan-clan 2595 |
| 16 | kangju | kushan-empire | unrelated (heuristic) | 2,368 | 50..224 | kangju 1693; kushan-empire 675 |
| 17 | liu-song-dynasty | northern-wei | unrelated | 2,123 | 420..476 | northern-wei 2123 |
| 18 | gurjara-pratihara-dynasty | umayyad-caliphate | nested (heuristic) | 1,998 | 730..741 | gurjara-pratihara-dynasty 1998 |
| 19 | hazaraspids | mongol-empire | nested (heuristic) | 1,960 | 1260..1290 | hazaraspids 1960 |
| 20 | kingdom-of-taqali | muhammad-ali-dynasty | unrelated (heuristic) | 1,936 | 1822..1865 | kingdom-of-taqali 1936 |
| 21 | kangju | parthian-empire | unrelated (heuristic) | 1,822 | -36..224 | kangju 1822 |
| 22 | mamluk-dynasty | soomra-dynasty | nested (heuristic) | 1,819 | 1236..1287 | soomra-dynasty 1819 |
| 23 | qing-dynasty | russian-empire | unrelated (heuristic) | 1,770 | 1848..1912 | qing-dynasty 1770 |
| 24 | inner-mongolia | republic-of-china | nested (heuristic) | 1,736 | 1947..1947 | inner-mongolia 1736 |
| 25 | kingdom-of-marwar | mughal-empire | nested (heuristic) | 1,728 | 1534..1757 | kingdom-of-marwar 1728 |
| 26 | duchy-of-pomerania | holy-roman-empire-minor-states | nested (heuristic) | 1,723 | 1482..1595 | duchy-of-pomerania 1723 |
| 27 | provisional-priamurye-government | russian-soviet-federative-socialist-republic | nested (heuristic) | 1,715 | 1923..1923 | provisional-priamurye-government 1715 |
| 28 | hunza-and-nagar | mughal-empire | nested (heuristic) | 1,643 | 1588..1741 | hunza-and-nagar 1643 |
| 29 | kuninda-kingdom | kushan-empire | nested (heuristic) | 1,530 | 91..224 | kuninda-kingdom 1530 |
| 30 | ottoman-empire | samtskhe-saatabago | nested (heuristic) | 1,528 | 1507..1572 | samtskhe-saatabago 1528 |
| 31 | chalukya-dynasty | panduvamshi-dynasty | nested (heuristic) | 1,500 | 626..750 | panduvamshi-dynasty 1500 |
| 32 | ottoman-empire | safavid-dynasty | unrelated | 1,472 | 1512..1734 | safavid-dynasty 1440; ottoman-empire 32 |
| 33 | anti-kuomintang-coalition | shanxi-clique | rebel (heuristic) | 1,470 | 1930..1930 | shanxi-clique 1470 |
| 34 | habesh-eyalet | turco-egyptian-sudan | colony (heuristic) | 1,452 | 1840..1855 | habesh-eyalet 1452 |
| 35 | emirate-of-diriyah | sharifate-of-mecca | nested (heuristic) | 1,448 | 1783..1815 | sharifate-of-mecca 1446; emirate-of-diriyah 2 |
| 36 | kingdom-of-prussia | north-german-confederation | nested (heuristic) | 1,397 | 1870..1870 | kingdom-of-prussia 1397 |
| 37 | gupta-empire | traikutaka-dynasty | unrelated (heuristic) | 1,363 | 410..470 | traikutaka-dynasty 1363 |
| 38 | carthage | masaesyli | unrelated (heuristic) | 1,360 | -344..-203 | masaesyli 1360 |
| 39 | hazaraspids | jalayirid-sultanate | nested (heuristic) | 1,330 | 1340..1395 | hazaraspids 1330 |
| 40 | tibet | wu-sangui-s-zhou | rebel (heuristic) | 1,330 | 1674..1677 | tibet 1314; wu-sangui-s-zhou 16 |
| 41 | kangju | yuezhi | unrelated (heuristic) | 1,326 | -128..1 | yuezhi 1228; kangju 98 |
| 42 | ikhshidid-dynasty | makuria | unrelated (heuristic) | 1,315 | 935..947 | makuria 1315 |
| 43 | ming-xia | yuan-dynasty | rebel (heuristic) | 1,307 | 1360..1360 | ming-xia 1307 |
| 44 | kingdom-of-austrasia | saxons | unrelated (heuristic) | 1,302 | 511..742 | saxons 1302 |
| 45 | muhammad-ali-dynasty | sharifate-of-mecca | nested (heuristic) | 1,291 | 1813..1839 | sharifate-of-mecca 1291 |
| 46 | great-seljuk-empire | nasrid-dynasty-of-sistan | nested (heuristic) | 1,280 | 1040..1046 | nasrid-dynasty-of-sistan 1280 |
| 47 | han-dynasty | xianbei | unrelated (heuristic) | 1,253 | 49..165 | xianbei 911; han-dynasty 342 |
| 48 | bikaner-state | mughal-empire | nested | 1,250 | 1740..1757 | bikaner-state 1250 |
| 49 | mongol-empire | shirvan | nested (heuristic) | 1,240 | 1260..1290 | shirvan 1240 |
| 50 | maitraka-dynasty | umayyad-caliphate | nested (heuristic) | 1,237 | 732..741 | maitraka-dynasty 1237 |
| 51 | reorganized-national-government-of-china | shanxi-clique | nested (heuristic) | 1,236 | 1940..1941 | shanxi-clique 1236 |
| 52 | jinghai-circuit | tang-dynasty | unrelated (heuristic) | 1,188 | 875..900 | jinghai-circuit 1188 |
| 53 | emirate-of-diriyah | mamluk-iraq | unrelated (heuristic) | 1,187 | 1805..1815 | mamluk-iraq 1187 |
| 54 | mongol-empire | principality-of-yaroslavl | nested (heuristic) | 1,184 | 1260..1290 | principality-of-yaroslavl 1184 |
| 55 | great-seljuk-empire | hazaraspids | nested (heuristic) | 1,176 | 1115..1192 | hazaraspids 1176 |
| 56 | ulus-of-chagatai | ulus-of-jochi | unrelated (heuristic) | 1,169 | 1227..1271 | ulus-of-chagatai 1169 |
| 57 | later-qin | northern-wei | unrelated (heuristic) | 1,157 | 397..414 | northern-wei 1156; later-qin 1 |
| 58 | antigonid-dynasty | ptolemaic-kingdom | unrelated (heuristic) | 1,145 | -306..-197 | ptolemaic-kingdom 1116; antigonid-dynasty 29 |
| 59 | eastern-chalukyas | rashtrakuta-dynasty | unrelated (heuristic) | 1,136 | 757..973 | eastern-chalukyas 1136 |
| 60 | atropatene | seleucid-empire | nested (heuristic) | 1,125 | -309..-223 | atropatene 1125 |

`conflicts.csv` lists every pair the size rule settled; `conflicts_settled_by_rule.csv` the pairs R1,
R2 and rule 4 settled.

## Phase A comparison

Phase C anchor (1 January, dossiers) against Phase A anchor (Cliopatria shapes alive that year).
"Same state" counts a cell when the Phase C owner is a dossier that lists the Phase A owner among its
`cliopatria_names`.

| year | Phase A cells owned | Phase C cells owned | owned in both | same state | agreement (both) | agreement (comparable) | agreement (either) | Phase A only | Phase C only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1600 | 184,232 | 188,488 | 161,774 | 130,784 | 80.8% | 97.6% | 62.0% | 22,458 | 26,714 |
| 1900 | 461,501 | 487,609 | 458,638 | 332,806 | 72.6% | 89.1% | 67.8% | 2,863 | 28,971 |

"Comparable" leaves out the cells whose Phase C owner is a dossier with no Cliopatria name (a state
Cliopatria lacks, most often a colony or viceroyalty the dossiers split out of Cliopatria's aggregate
empire: the Viceroyalty of Peru and New Spain out of the Spanish Empire in 1600, Canada, the Australian
colonies and British Africa's protectorates out of the British Empire in 1900). Those splits, and the
dossiers' corrected life spans (Cliopatria keeps the Golden Horde alive in 1600; the dossier ends it in
1502), are most of the difference; the rest is the ledger moving borders between keyframes.

Largest per-state differences (cells in one and not the other):

- 1600: spanish-empire 19,229 (C 10,412, A 24,377); viceroyalty-of-peru 8,149 (C 8,149, A 0); tsardom-of-russia 5,111 (C 23,908, A 18,843); viceroyalty-of-new-spain 4,717 (C 4,717, A 0); khalkha-khanates 4,368 (C 4,368, A 0); tibet 2,944 (C 3,296, A 6,038); captaincy-general-of-chile 2,475 (C 2,475, A 0); tumed 2,186 (C 510, A 1,676); ajuran-sultanate 1,808 (C 1,808, A 0); captaincy-general-of-guatemala 1,527 (C 1,527, A 0)
- 1900: british-colonial-empire 51,433 (C 2,042, A 53,459); canada 35,738 (C 35,738, A 0); british-africa 16,608 (C 10,892, A 27,460); colony-of-western-australia 12,128 (C 12,128, A 0); russian-empire 11,719 (C 76,582, A 87,527); qing-dynasty 9,183 (C 41,736, A 43,199); colony-of-south-australia 9,154 (C 9,154, A 0); french-west-africa 9,062 (C 9,062, A 0); congo-free-state 8,228 (C 8,228, A 0); anglo-egyptian-sudan 8,206 (C 8,206, A 0)

## The problems that move the most land

| rank | cells | kind | state(s) | what |
| --- | --- | --- | --- | --- |
| 1 | 31,226 | end to nobody | aboriginal-australians | 31226 of its 31226 cells go to nobody at its end (no living successor's land covers them) |
| 2 | 27,856 | end to nobody | green-sahara-cultures | 27856 of its 27856 cells go to nobody at its end (no living successor's land covers them) |
| 3 | 21,040 | end to nobody | yuan-dynasty | 21040 of its 22803 cells go to nobody at its end (no living successor's land covers them) |
| 4 | 20,244 | keyframe snap | kuomintang | keyframe kuomintang_1928 adds 20233 and removes 11 cells that no ledger event moves (the state had 5903) |
| 5 | 11,835 | end to nobody | uyghur-khaganate | 11835 of its 11896 cells go to nobody at its end (no living successor's land covers them) |
| 6 | 7,063 | end to nobody | hoabinhian | 7063 of its 7063 cells go to nobody at its end (no living successor's land covers them) |
| 7 | 6,354 | keyframe snap | mongol-empire | keyframe mongol-empire_1227 adds 6211 and removes 143 cells that no ledger event moves (the state had 46975) |
| 8 | 6,260 | keyframe snap | khalkha-khanates | keyframe khalkha-khanates_1547 adds 0 and removes 6260 cells that no ledger event moves (the state had 10628) |
| 9 | 5,478 | keyframe snap | ulus-of-jochi | keyframe ulus-of-jochi_1267 adds 4111 and removes 1367 cells that no ledger event moves (the state had 18183) |
| 10 | 5,113 | keyframe snap | mongol-empire | keyframe mongol-empire_1220 adds 3415 and removes 1698 cells that no ledger event moves (the state had 33901) |
| 11 | 5,040 | keyframe snap | mongol-empire | keyframe mongol-empire_1236 adds 4605 and removes 435 cells that no ledger event moves (the state had 72810) |
| 12 | 5,022 | keyframe snap | tsardom-of-russia | keyframe tsardom-of-russia_1600 adds 22 and removes 5000 cells that no ledger event moves (the state had 23908) |
| 13 | 5,017 | end to nobody | viceroyalty-of-peru | 5017 of its 7830 cells go to nobody at its end (no living successor's land covers them) |
| 14 | 4,967 | keyframe snap | dzungar-khanate | keyframe dzungar-khanate_1687 adds 4967 and removes 0 cells that no ledger event moves (the state had 8537) |
| 15 | 4,733 | keyframe snap | saffarid-dynasty | keyframe saffarid-dynasty_900 adds 0 and removes 4733 cells that no ledger event moves (the state had 6329) |
| 16 | 4,533 | keyframe snap | ulus-of-hulegu | keyframe ulus-of-hulegu_1260 adds 3746 and removes 787 cells that no ledger event moves (the state had 10299) |
| 17 | 4,418 | keyframe snap | parthian-empire | keyframe parthian-empire_-164 adds 0 and removes 4418 cells that no ledger event moves (the state had 5714) |
| 18 | 4,403 | end to nobody | yamnaya-culture | 4403 of its 4403 cells go to nobody at its end (no living successor's land covers them) |
| 19 | 4,343 | keyframe snap | samanid-empire | keyframe samanid-empire_900 adds 4343 and removes 0 cells that no ledger event moves (the state had 4459) |
| 20 | 4,312 | keyframe snap | viceroyalty-of-peru | keyframe viceroyalty-of-peru_1600 adds 4260 and removes 52 cells that no ledger event moves (the state had 8149) |

`problems.csv` has the first 3,000. Keyframe snaps are the ledger's gaps: the keyframe of record says
the state held land (or lost land) that no event between the keyframes moves; most trace to an event
whose region does not resolve (`unresolved_events.csv`) or to a ledger that covers only part of the
period. Conflicts are two states whose shapes claim the same cells.

## The names the gazetteer lacks, most needed first

| kind | name | events | dossiers | error |
| --- | --- | --- | --- | --- |
| place | Dewangiri (Bhutan) | 8 | 3 | unknown place 'Dewangiri' in Bhutan |
| place | Kherla (India) | 6 | 1 | unknown place 'Kherla' in India; closest: Pokhran (India), Chirala (India), Kanchipuram (India) |
| place | Baitag Bogd | 4 | 2 | unknown place 'Baitag Bogd'; closest: Ubaitaba (Brazil), Fox Bay (Falkland Islands), Bayan Obo (China), B'abda (Lebanon), Gaziantep (Turkey) |
| region | Fatagar | 4 | 2 | unknown region 'Fatagar'; closest: Katanga, Patagonia, Saurashtra, Wollega, Mataram (Java), Kerala (region) |
| place | Bagys (Kazakhstan) | 2 | 2 | unknown place 'Bagys' in Kazakhstan; closest: Arys (Kazakhstan), Balyqshy (Kazakhstan) |
| region | Mancanegara | 2 | 2 | unknown region 'Mancanegara'; closest: Tabaristan, Canary Islands, Maya Lowlands, Manchuria, Greater Manchuria, Canada (St Lawrence), Phoenicia, Canaan |
| place | Ilaro (Nigeria) | 2 | 1 | unknown place 'Ilaro' in Nigeria; closest: Lagos (Nigeria), Ikare (Nigeria) |
| place | Karangan (Indonesia) | 2 | 1 | unknown place 'Karangan' in Indonesia; closest: Amlapura (Indonesia), Tarakan (Indonesia), Pakalongan (Indonesia), Langsa (Indonesia), Semarang (Indonesia) |
| place | Kutai Lama (Indonesia) | 2 | 1 | unknown place 'Kutai Lama' in Indonesia; closest: Banda Aceh (Indonesia), Langsa (Indonesia), Ambon (Indonesia), Kuta (Indonesia), Kualakapuas (Indonesia), Timi |
| place | Los Arcos | 2 | 1 | unknown place 'Los Arcos'; closest: Los Blancos (Argentina), Los Lagos (Chile), Les Cayes (Haiti), San Marcos (Guatemala), San Marcos (United States of America) |
| place | Muara Kaman (Indonesia) | 2 | 1 | unknown place 'Muara Kaman' in Indonesia; closest: Tarakan (Indonesia), Kualakapuas (Indonesia), Surakarta (Indonesia), Mataram (Indonesia) |
| place | Seocheon | 2 | 1 | unknown place 'Seocheon'; closest: Suncheon (South Korea), Sokcho (South Korea), Ye (China), Cieszyn (Poland), Sunchon (North Korea), Serpukhov (Russia) |
| place | Arsuf | 1 | 1 | unknown place 'Arsuf'; closest: Tarsus (Turkey), Kars (Turkey), Karasuk (Russia), Daru (Papua New Guinea), Barysaw (Belarus) |
| place | Artajona | 1 | 1 | unknown place 'Artajona'; closest: Arjona (Colombia), Barahona (Dominican Republic), Artashat (Armenia), Taonan (China), Tainan (Taiwan), Daejeon (South Korea) |
| place | Coixtlahuaca | 1 | 1 | unknown place 'Coixtlahuaca'; closest: Cuitlahuac (Mexico), Ithaca (United States of America), Covilhã (Portugal), Cilacap (Indonesia) |
| place | Uzengi-Kuush (Kyrgyzstan) | 1 | 1 | unknown place 'Uzengi-Kuush' in Kyrgyzstan |
| region | Massango | 1 | 1 | unknown region 'Massango'; closest: Oman, Awsan, Assam (region), Khorasan, Sistan |
| region | Wej | 1 | 1 | unknown region 'Wej'; closest: Nejd, Jeju |

The full list is `unresolved_names.csv`; each failing spec with its dossier and place is in
`unresolved_events.csv`.

## Files

| file | what |
| --- | --- |
| `unresolved_events.csv` | every event, keyframe and successor land whose region spec does not resolve: slug, where, year, type, the failing leaves, the gazetteer's error, the spec |
| `unresolved_names.csv` | the same aggregated by failing name (kind, name, events, dossiers, event types, examples, error with the closest matches), most used first: the gazetteer agent's work list |
| `skipped_events.csv` | every event not applied, with the reason; also every merge whose counterpart has no living dossier, with the branch that applied (a gain from nobody, or nothing moved) |
| `noop_events.csv` | events applied that changed no cell (the counterpart did not hold the region, the region was already the state's) |
| `unclosed_ends.csv` | `*_end` events that close nothing open |
| `conflicts.csv` | the conflicts the size rule settled, by pair: category (and whether reviewed by hand), the most one year's conflict holds of the smaller state, cells summed over the claims (cell-years), the most in one year, years, who won how many cells, the context (found or keyframe), claims |
| `conflicts_settled_by_rule.csv` | the same for the pairs R2, R1 and rule 4 settled, with the rule |
| `colonies_check.csv` | problems found reading `data/colonies.csv` (unknown slugs, metropoles not alive, overlapping rows, colonies without a row) |
| `keyframe_snaps.csv` | dossier gaps: slug, shape_id, year, cells differing, added, removed, kept by others, the state before, the keyframe |
| `conflict_places.csv` | where the top 150 pairs of `conflicts.csv` (by cell-years) dispute land, one row per pair and conflict year (a pair with more than 12 conflict years keeps the 12 with the most cells, and `years_note` says so): pair_rank, slug_a, slug_b, year, cells (distinct cells that year), winner (cells won when both won some), places (the top 6 admin-1 regions of the cells, "Name (Country) n", from `data/gazetteer/admin1.jsonl`, a cell two rows list going to the smaller; a cell no admin-1 row lists gives "no admin-1 (Country)", or "unmapped" when no country row lists it either), the centroid (lat, lon) and bounding box (lat_min, lon_min, lat_max, lon_max; lon_min greater than lon_max means the box crosses the antimeridian), claim_a and claim_b: the event or keyframe each side claimed the cells by (for the claimant, the event or keyframe that made the claim; for the holder, the one that gave it the cells: `slug/ledger/i`, `slug/keyframe/shape_id` with its correction's `text` when at most 200 characters, or a `data/colonies.csv` or `data/hierarchy.csv` row), with the cells of each when there are several (top 3) |
| `snap_places.csv` | where the top 100 keyframe snaps by cells differing (and the top 100 by cells moved, the order of `keyframe_snaps.csv`) add and remove land: both ranks, slug, shape_id, year, cells differing, added, removed, added_places and removed_places (top 6 admin-1 regions, as above), the cells the keyframe wanted that others kept (count, the top 3 holders, their top 6 regions), the previous keyframe and its year, and ledger_between: the dossier's ledger events after the previous keyframe's year up to the snap's year (from its start when there is none) |
| `areas.csv` | area per state at each anchor against Cliopatria's area that year (the model is `data/anchors/_areas.csv`) |
| `adjacency.csv` | every pair of states sharing a border in any compiled year (owners, whatever the status; land neighbours only, so a strait separates): first year, last year, years adjacent, the most pairs of neighbouring cells across their border in one year (about the border's length in cells), for the colour agent's neighbour rule |
| `deaths.csv` | each state's end: cells it held, to successors, to nobody |
| `problems.csv` | snaps, conflicts and ends to nobody ranked by cells |
| `phase_a_comparison.json` | the comparison above with the 25 largest per-state differences per year |
| `run_summary.json` | every number of the run |
| `patches_check.csv` | every entry of `data/patches/<window>.json`: window, kind, index, slug (for a ruling, its two slugs joined by a vertical bar), outcome (applied, skipped, note) and why; for a ruling, the cell-years it settled |
| `patch-overrides.csv` | every keyframe a patch now controls (an applied `keyframe_overrides` entry): window, shape_id, slug. A dossier round that edits one of these keyframes in the dossier changes nothing on the map while the patch stands |
| `windows/<window>.md` | one review packet per window (under 25 KB): its patch file's entries and the rulings in force, its size-rule conflicts by pair with the admin-1 regions, its keyframe snaps with the regions added and removed, the 10 years with the most cells changed (where, by which events), skipped events and unresolved regions, colony and hierarchy relations opened or closed, contests and occupations, the states alive with their cells at its start and end, and neighbour pairs whose `colours.json` colours are closer than 0.08 in OKLab; each list sorted by cells and cut with a count of the rest |

## Patches (data/patches/<window>.json)

The window agents record corrections in one file per window, which every compile applies (the format,
with an example of each kind, is in `data/patches/README.md`; nothing is written back into the
dossiers):

- **events**: extra ledger events (a ledger event plus `slug`), applied as if they were in that dossier's
  ledger, after the dossier's own events of the same year and month. `found` and `dissolve` are refused
  (a state's life is its dossier's). The act is `data/patches/<window>.json: events/<k>`, so the change's
  `event`, the caption's `"patch"` and the skipped and no-op lists name the file.
- **keyframe_overrides**: a `keyframe_review` entry (plus `slug`, with `why` for `note`) replacing the
  dossier's entry for that `shape_id` (added when it has none); the first file in window order wins
  when two override one shape. Snaps, captions and changes name it: `<slug>/keyframe/<shape_id>
  [data/patches/<window>.json: keyframe_overrides/<k>]`.
- **rulings**: `{years, a, b, winner, status?, suzerain?, region?, source, why}` settle the pair's
  conflicts in those years (after R2, before R3; above): with a region only on its cells, otherwise on
  every cell both claim. With `status` (vassal or constituent with `suzerain`, occupied with `suzerain`
  the occupier, contested) the cells the winner gets or keeps take that status in a relation flagged
  `"ruling"`, which closes at the start of the year after the ruling's last (or when a party ends). The
  rule of a settled conflict is `ruling <window>/rulings/<k>`.

Each entry is checked as `tools/validate_dossier.py` checks a dossier (the schema of a ledger event or a
keyframe entry, the shape's owner, from/to for a new keyframe, the life span; regions through the
gazetteer); a bad entry or file is listed in `patches_check.csv` and skipped, never fatal. Patches dated
outside their window are applied with a note. This run: 91 files (0 skipped); applied 310 events, 453 keyframe overrides and 73 rulings (61 of them settled conflicts); skipped 0 entries.

## How the brief was read (where it is silent or ambiguous)

- **Order within a year.** Ledger events in month order (an event without a month takes the month of
  the event before it in the same dossier and year, so a dossier's own order is kept; births first
  within a month), then keyframe snaps, then deaths (rule 7: after the year's other events). An `*_end`
  (vassal, contest, occupation) of one dossier goes before an `*_start` of another dossier of the same
  month, or where either month is unknown (no event of its dossier in that year has a month), when the
  two regions share land: a relation one state ends that year is closed before another opens over it
  (fix round fx-02: Han's protectorate of the Western Regions and the Xiongnu's in 74 and 91). The start
  waits, with the rest of its dossier's year, only while another dossier still has such an end to apply.
  This run moved 412 starts.
- **Life span.** A dossier with a `dissolve` event ends at `identity.end.year`; one without is alive
  through 2026 (the validator ties both to the ledger). Events of a dead or unborn state, and of
  `umbrella` dossiers, move nothing (captions are kept).
- **Counterparts.** A counterpart is a dossier when it is a dossier slug or slugifies to one, and it
  counts only while that dossier is alive; otherwise it is a name without a dossier.
- **Regions with no land cell.** An event whose region resolves to no land cell moves no land: a gain,
  loss, split, merge, contest_start or occupation_start over it is skipped and logged in
  `skipped_events.csv` ("region resolves to no land cell"), and so is an `*_end` over it when nothing is
  open. The names the gazetteer documents as having no land cell are read as no land while it does not
  know them (`LANDLESS_NAMES` in the script: the Hawar Islands, Janan Island, Fasht ad Dibal, the Swan
  Islands and any Antarctic name), so they are not listed as unresolved; inside a union they add
  nothing. This run: 38 events skipped this way; landless names met: Australian Antarctic Territory, Fasht ad Dibal, Hawar Islands, Janan Island, Ross Dependency, Swan Islands.
- **gain** takes the region's cells the counterpart holds; when the counterpart is nobody, has no
  living dossier or holds none of the region, the region's nobody's land. **loss** gives the region's
  cells this state holds to the counterpart (to nobody when it has no living dossier); a loss whose
  counterpart's dossier carries the matching gain (same year, counterpart this slug, a region that
  resolves) is applied once, as that gain. **split** gives the region's cells to the new state.
  **merge**: the state that ends that year is absorbed; otherwise the side holding more of the region
  is absorbed by the other. A merge whose counterpart has no living dossier that year (a name without a
  dossier, nobody, an umbrella, a slug not alive) is a gain from nobody: the region's cells nobody holds
  pass to the state and its own cells stay (round 12; round 11 gave the state's own cells in the region
  to nobody when it held more of the region than nobody did). Each one is listed in `skipped_events.csv`
  with the branch that applied ("applied as a gain from nobody", or "nothing moved" when the region holds
  none of nobody's cells). This run: 42 merges, 17 applied as a gain from nobody, 25 moving nothing.
- **found** takes the whole region (else the first keyframe's corrected shape) from nobody, the
  predecessors and the counterpart; cells of any other state are a conflict.
- **Relations.** One relation per pair is open at a time: both dossiers often record the same
  contest, occupation or vassalage, and the second record joins the first. Roles of a reciprocal record
  are taken from the land: an occupation recorded by the owner (it holds the region) is the
  counterpart's occupation. For a `vassal_start`, in this order: between a colony and its metropole
  that year, the metropole is the suzerain; when both dossiers record it in the same year, the party
  whose keyframe shape holds most of the region (half or more, the other's under half, 0.25 apart) is
  the vassal, and the second record joins the first's relation; a vassalage recorded by the vassal (it
  holds more of the region and is the smaller) is the counterpart's suzerainty; so is one whose larger
  counterpart already holds the region the recorder's own keyframe covers, and when neither holds any
  of the region the larger party is the suzerain; and when the recorder holds the region inside its own
  shape and the counterpart, which holds land elsewhere, holds none of it and its shape doesn't cover it,
  the recorder is the vassal. "Larger" weighs a colony with a metropole that year as its metropole (when
  the other party is neither that metropole nor another of its colonies). A vassal whose dossier holds
  none of the region (or has none) is
  drawn as the suzerain's land in the vassal tint; its `vassal_end` returns that land to the vassal's
  living dossier or to nobody. A state that is a vassal keeps its new land in the same tint; when one
  of two nested suzerainties ends, the other's tint returns. An `*_end`
  closes the whole relation; one that finds nothing open is counted (`unclosed_ends.csv`), unless the
  pair's other dossier closed it the same year.
- **Keyframes.** The keyframe of record in a year is the union of the state's keyframes alive that
  year (Cliopatria's shape for `ok`, the correction for `adjust` and `wrong`, the keyframe's own years
  for new keyframes, Cliopatria's for reviewed shapes); it is compared in each keyframe's `from` year
  (or the birth year when it starts earlier) against the state's cells plus the cells it holds as
  suzerain, occupier or claimant. The difference counted is what setting the state to the keyframe
  would actually move: the missing cells it may take (nobody's, or another state's under the conflict
  rule) plus its direct cells outside the keyframe. More than 20 cells or more than 5 percent of the
  state sets the state to the keyframe; less is ignored (coastline noise). Cells a smaller neighbour
  keeps are logged as conflicts in every keyframe year but never trigger a snap. Vassal, occupied
  and contested cells are left to their relations. A "years only" or "status only" verdict written in prose is not parsed:
  the shape is used at its Cliopatria years.
- **Conflicts.** A cell another state holds is claimed only by a birth or a keyframe; an event of the
  same year that moved the cell settles it for the event's state; otherwise R2, a ruling, R3, rule 4, R1 and the
  size rule decide in that order (above), and the pair is logged with the rule.
- **Colony cells in keyframes.** A colony's cells in its metropole's tint count as direct when a
  keyframe snap releases the cells outside the keyframe (cells in an explicit vassal, occupation or
  contest relation are left to it).
- **Regions.** Each leaf of a spec is resolved once by `tools/gazetteer.py` and cached; union,
  intersect and minus are composed exactly as the gazetteer composes them; a spec with any unresolved
  leaf is unresolved as a whole and its event skipped. `border_band` resolves against the Phase A
  anchors, as the gazetteer does.
