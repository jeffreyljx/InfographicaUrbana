# Notes, group eu-15-a (Samo, Great Moravia, Nitra x2, Magyars, Duchy of Bohemia)

Written 2026-10-25 by the Phase B agent for eu-15-a. Six dossiers, all validate with `--resolve` (0 errors, 0 warnings). Every page below was opened with WebFetch on 2026-10-25; the fetch tool returns a summary, so quotes are the tool's quotations of the page, not a character-exact copy. Nothing is from memory except the coordinates of capitals.

## Cross-cutting

- No Cliopatria row had to be split or merged. `principality-of-nitra` (Q837326, 814-839) and `nitra` (Q26397, 898-910) have different Wikidata ids and stay two dossiers, though they are the same land.
- All six rows are trimmed or re-dated by verdict (shape unchanged) where a page dates the state differently. Where only the years change, the verdict is `adjust` with the Cliopatria shape repeated and the new years in `text`; new keyframes (`from`/`to`) are used only where the shape itself changes.
- Cliopatria shape arithmetic (`minus` / `intersect` of its own years) was used wherever a page says a place changed hands without naming a boundary; cell counts were checked with `tools/gazetteer.py resolve`.
- Overlaps worth knowing: Cliopatria's Magyars and First Bulgarian Empire shapes do not overlap in any year (0 cells); Samo's 623 shape overlaps the Avar 617 shape by about 52,000 km2.

## samo-s-empire (5 pages: Samo's Empire, Battle of Wogastisburg, Dervan, Carantania, Sorbs)

- Start 623 (Fredegar via the page: Samo went to the Slavs c. 623-624), end 658 (infobox; page allows 658 or 659; Cliopatria 660).
- The Dervan page is a disambiguation list (only "fl. 615-636, Sorbian medieval ruler"); the Sorbs page supplied the Dervan material. One page of the budget was spent on it.
- Shape includes about 40,000 km2 of Alpine land that Cliopatria later gives to Carantania; J. B. Bury (quoted on the Samo page) says that inclusion rests on one source. Kept, soft.
- The 633 enlargement is the Lusatian Sorbs; the Sorbs page dates it 631, the Samo and Wogastisburg pages 631 or 632; Cliopatria 633. Re-dated to 631 by verdict and event.
- No capital and no area on any page; `capitals` is empty.
- Not opened: Fredegar's text, Radulf of Thuringia, the Lombard/Alamanni side. Wogastisburg's site is unknown.
- After 658 the page calls the union's history "largely unclear"; land is given to Carantania (Alpine part), the Avars (southern Slovakia) and `nobody` (rest, confidence 1).

## great-moravia (9 pages of its own + 3 shared: Great Moravia, Svatopluk I, Mojmir I, Rastislav, Wilhelminer War, Bořivoj I, Battle of Pressburg; shared: Principality of Nitra, Duchy of Bohemia, Hungarian conquest of the Carpathian Basin)

- The URL https://en.wikipedia.org/wiki/Mojm%C3%ADr_I_of_Moravia failed (url_not_found); https://en.wikipedia.org/wiki/Mojmir_I_of_Moravia loaded.
- Start 822 (first record of the Moravians; Cliopatria 814). The page gives no founding date; Great Moravia proper is "c. 833" (union with Nitra). Rename event not used: the state, rulers and colour are continuous.
- Bohemia: Cliopatria draws it as direct land from 860. The pages (Bořivoj I, Duchy of Bohemia, Svatopluk I) say vassal duchy (recognised c. 872), direct under Svatopluk after the winter-890 agreement with Arnulf, lost June 895. Shapes 860-889 are corrected to minus Bohemia; ledger carries vassal_start 872, vassal_end/gain 890, loss June 895. A reviewer who prefers Cliopatria's blanket treatment can drop the corrections.
- The northern lands (Vistula, Silesia, Lusatia) rest on Cliopatria's single jump in 875; the Great Moravia page calls Silesia/Lusatia "probably" annexed in the early 890s (Bartl) and Lesser Poland doubtful. One confidence-1 gain event; certainty soft.
- Nitra: gained 833 (page: "Around 833, he expelled Pribina"); Bowlus holds it was annexed only under Svatopluk. From 898 it is an appanage (vassal_start/vassal_end naming `nitra`, confidence 1).
- Fall: 902 eastern area occupied (Battle of Pressburg page), collapse "between 902 and 907"; end 907. Cliopatria's 908-910 dropped. Who held the Czech lands of Moravia 907-955 is not on any page opened (Duchy of Bohemia: Boleslaus I "received the lands of Moravia" after Lechfeld 955); successor listed is principality-of-hungary only.
- The 898-900 shrink (8,900 km2 on the west and south edges) is attributed to the Hungarians at confidence 1; the geometry fits an East Frankish gain as well.
- No area on the Great Moravia page, so no infobox comparison.
- Not opened (budget): Treaty of Forchheim, Cyril and Methodius, Pribina/Balaton Principality, Kocel, Lower Pannonia.

## principality-of-nitra (Principality of Nitra, Nitra, Great Moravia pages)

- Infobox: independent 825-833; vassal of Great Moravia 833-906/907; incorporated c. 870. Dossier ends the independent state in 833 (the Great Moravia and Nitra pages: united after Pribina's exile) and notes the disagreement. Cliopatria 814-839 trimmed to 825-832.
- The church "at a place over the Danube called Nitrava" is undated on the page opened.

## nitra (Nitra city page, Principality of Nitra, Great Moravia)

- The Moravian heir's appanage 898-907 (the pages do not name the heir). Type `state`; if the colour agent wants it drawn as the vassal tint of Great Moravia (which is what great-moravia's vassal_start does), it could be typed `colony`.
- End 907 from the infobox (906/907); Cliopatria 910. Cliopatria's Principality of Hungary shape does not cover Nitra before 911: the Hungary dossier should take Nitra from 907.

## magyars (5 pages: Hungarian conquest of the Carpathian Basin, Etelköz, Hungarians, Principality of Hungary, Pechenegs)

- This row is the pre-conquest confederation (Etelköz) and then the eastern tribal lands; the Basin state is the Principality of Hungary (another dossier). End 907 (kende rule "c. 904" in the infobox, 907 in the text; Árpád c. 907). Cliopatria 910.
- Start 840 bridges the Hungarians page (c. 830) and the Etelköz page (c. 850): confidence 1.
- Pecheneg takeover: "by 892 west of the Dnieper" and "around 895 leave Etelköz" (Pechenegs and Etelköz pages). Cliopatria keeps the Etelköz to 899, so the 887, 896 and 898 shapes are corrected by arithmetic on Cliopatria's own shapes. `pechenegs` has no Cliopatria row and needs a dossier (Pecheneg Khanates 889-1091).
- The lower Dniester steppe is a Magyar gain from Bulgaria in Cliopatria 896-897 (the Hungarian-Bulgarian war of 894-896); both events are confidence 1 (the page gives no year or land).
- Khazar suzerainty and the Kabar revolt are undated on the pages: not in the ledger.
- Transylvania: the Principality of Hungary shape (16.3-23.5E) stops west of it; the Magyars row hands the eastern lands to the Principality at 907 and the Hungary dossiers should cover Transylvania 907-1000 ("semi-independent polities, e.g. the domains of Gyula the Younger").
- No capital, no rulers (not dated on the pages opened). No area on any page.

## duchy-of-bohemia (5 pages: Duchy of Bohemia, Bořivoj I, Boleslaus I, Boleslaus II, Mieszko I; plus Great Moravia for June 895)

- Start 870 (infobox "c. 870"; Cliopatria 896, because it draws Bohemia inside Great Moravia). The new keyframe _870 covers 870-889; 890-894 Svatopluk rules it directly (ledger loss/gain), so no duchy shape those years.
- Moravia: the page says both that Boleslaus I "conquered ... Moravia and Silesia" on taking the throne in 935 and that Bohemia "received the lands of Moravia" after Lechfeld in 955. Followed the dated 955; the 947 shape is corrected to minus Moravia for 947-954.
- Silesian slice (947) and Kraków (960) keep Cliopatria's years at confidence 1; the Boleslaus I page gives no year for either. The Mieszko page calls Czech rule over Lesser Poland "only nominal".
- 990: the Mieszko page has the 990 war and Silesia "taken over by Poland" (annexation "possibly ... around 985"); the Cliopatria 990-1002 shape still holds a Silesian slice, removed by verdict.
- End 1002: Henry II enfeoffs Vladivoj, "what had been a fully sovereign duchy became part of the Holy Roman Empire". The duchy itself lasts to 1198 (kingdom) and Cliopatria has no Bohemian row for 1003-1201 (Kingdom of Bohemia starts 1202): a gap for the Kingdom of Bohemia dossier or a gap-filler. Boleslaus the Brave's occupation of Bohemia and Moravia in 1003-1004 is after this dossier's last year (noted in `notes`, not as a war).
- Rulers: only Bořivoj I, Boleslaus I and Boleslaus II have reign years on the pages opened. Spytihněv I, Vratislaus I, Wenceslaus and Boleslaus III are missing.
- No area on the Duchy of Bohemia page (infobox shows none).
- Vassal relations to the East Frankish and German kings (895 Arnulf, 929 Wenceslaus submits to Henry I, 950 Otto I) belong to the East Franks / Kingdom of Germany dossiers as vassal events.

## Gazetteer names needed

Lusatia (region; Upper and Lower Lusatia between the Elbe and the Neisse), Etelköz (region; Dniester-Prut-Siret interfluve and the steppe to the Dnieper), Pannonia / March of Pannonia (region), Mikulčice (place, 48.771N 17.047E).

## Counterparts needing dossiers

- `pechenegs` (Pecheneg Khanates, 889-1091): counterpart of the Magyars' losses in 892 and 895.
- "Sorbs under Dervan" (c. 615-636): tiny tribal polity; Samo's 631 gain names it by string. Low priority.

## Repair pass 2026-10-25 (after review-eu-15-a.md): great-moravia and magyars

Only the two FAIL dossiers were touched; samo-s-empire, principality-of-nitra, duchy-of-bohemia and nitra were not (verdicts thin or fix). Both files validate with `--resolve` (0 errors, 0 warnings). Pages re-opened with WebFetch on 2026-10-25: Great Moravia, Battle of Pressburg, Wilhelminer War, Rastislav of Moravia, Hungarian conquest of the Carpathian Basin (three queries), Svatopluk II, Mojmir II, Vistulans, Byzantine-Bulgarian war of 894-896, Kurszán, Khazars, Levedia, Oleg of Novgorod. Quotes are the fetch tool's; it summarises, and on one query it missed passages a word query then found (Dristra, 'routed the Hungarians'), so absence claims below are from word-level queries.

### Applied (great-moravia)

- 896 loss to nobody split: the 210 cells (53,109 km2) that Cliopatria's Magyars 896 shape shares with the Moravian 895 shape are now a loss to `magyars`; the other 537 cells (135,807 km2) stay with `nobody`. The two halves together equal the old region (checked cell by cell). The magyars dossier gains the same 210 cells from `great-moravia` in 896 (identical cell set; checked).
- 898 `split` event for Nitra added before the vassal_start (the Moravian 898 shape drops Nitra's 106 cells; nitra is founded in 898 with counterpart great-moravia).
- 900 loss (35 cells, 8,852 km2): counterpart now `east-franks` (all 35 cells are inside Cliopatria's East Franks 900; none in the Principality of Hungary's). Source changed to the Great Moravia page: Arnulf sent troops in 898 and 899; the Mojmir II page has the Bavarians' 898 troops defeated and a 901 peace with Eastern Francia. No page records a cession, so confidence stays 1 and the geometry decides.
- 907 dissolve: counterpart `nobody`, region = the Czech remnant (79 cells, 19,979 km2, the 902-907 keyframe). Battle of Pressburg page: 'followed by Hungarian suzerainty over the rest of Moravia and Dalamancia' (suzerainty, not direct rule). `principality-of-hungary` stays the successor, now for the 902 eastern area only.
- `{"region": "Bohemia"}` (58,926 km2) replaced by `{"cliopatria": "Duchy of Bohemia", "year": 896}` (47,545 km2) in keyframes 860-889 and in the 872, 890 (two), 895 and 896 events. The 860-889 shapes now cut out exactly the duchy's 870 keyframe, so no land is dropped and the 850 shape is no longer cut (1 cell instead of 29).
- Wilhelminer War entry runs 882-885 (page: 'from 882 to 884' in the opening sentence, 'late 885' for the agreement).
- 850 gain note: the Rastislav page has only 'In this period Rastislav seems to have acquired new territories in the east' within 'the first eight years of Rastislav's reign' (846 onward); it does not name the Slanské Hills (that is the Great Moravia page's, per the first pass; not re-checked).
- 875 jump split in two: the Vistula land (Małopolskie, Podkarpackie, Świętokrzyskie; 116 cells) at confidence 2 on the Vistulans page ('Probably around 874', a cited source 'between Ad 875-879', 'no conclusive evidence'), and the rest (407 cells) at confidence 1 (Silesia and Lusatia dated to the early 890s by the Great Moravia page).
- Thin items answered from the pages: northern lands after 894 (Mojmir II page: Bohemia 895, Lusatia 897, southern Poland unknown, silent on Silesia and the Vistula land); the Nitra heir is Svatopluk II (page gives no year for the appanage; he rebelled 898, returned to Nitra 901).

### Applied (magyars)

- 895 gain from nobody split: 210 cells (53,109 km2) held by Great Moravia's 892-895 shape become a 896 gain from `great-moravia` (confidence 1); the other 270 cells (68,283 km2) stay a 895 gain from nobody.
- New 884 loss to `kievan-rus` (58 cells, 14,668 km2, confidence 1; 57 of the 58 cells are in Cliopatria's Kievan Rus' 884 shape and none in its 882 shape). Oleg page: Kiev 'In 881-882', Drevlians tributary 'In 883'; neither it nor the Khazars page mentions Magyar land, so this is bridging, not a finding. The 884 keyframe note now points to it.
- Start 840 (Levedia page: Magyars in Levedia 'around 830' per Kristó, exodus 'around 850'; Khazars page: first Pecheneg attack 'around 854', raids from Etelköz 'from 862 onwards') remains a bridge at confidence 1.
- Dniester steppe events (895/898) remain confidence 1: the Byzantine-Bulgarian war page has the 895 Magyar raid on Dobruja and the early-896 Bulgarian-Pecheneg counter-attack but names no land and no 897 or 898 event.
- Kurszán page: 'died 904', 'From this point Árpád became the only ruler', and the attack on Great Moravia with Arnulf is dated 892/893 (the Battle of Pressburg page has 902 'probably led by Kurszán'). The 907 end stays (Principality page); the sole rule dates from 904 on the Kurszán page. Recorded in the 900 and 907 notes, confidence unchanged at 1.

### Where I disagree or could not follow the review

- duchy-of-bohemia /ledger/1-2 still use `{"region": "Bohemia"}`: the dossier is thin and outside this pass, so not edited. Replace by the Cliopatria Duchy of Bohemia 896 shape so that it mirrors great-moravia's 890 and 895 events.
- The nitra dossier (verdict fix) says the pages do not name the heir; the Svatopluk II page names him (Svatopluk II, 'As Prince of Nitra ... subordinated to Mojmír II'; no appanage year). Not edited.
- 900 loss to East Francia: the review asked for it and I made it, but no page I opened says East Francia took land from Moravia in 898-900 (the Mojmir II page says the Moravians defeated the Bavarian troops); the counterpart rests on Cliopatria's East Franks 900 shape alone.
- 902 loss: the page's 'eastern area' is not the Slovak part of Cliopatria's 900 shape, which is 7 cells (1,770 km2) beside Pressburg; the eastern Slovak lands were already out of the Moravian shape from 896-898. Left as is, caveat in the note.
- Pages disagree on 900: the Mojmir II page has the Magyars raiding Bavaria 'together with Mojmir's troops' while the Hungarian conquest page has them invading Moravia.
- Unexplained: the 850-to-860 growth of the Moravian shape by 44 cells (11,128 km2, 13.3-18.9E, 48.4-50.9N) beside the Bohemian shape, no page dates it.
- Still thin: 896 northern loss (year Cliopatria's), Nitra appanage year (page silent), 900/907 hand-over to the Principality (pages silent on land).

### Routing for other batches

- east-franks (eu-07): no gain from great-moravia in 900 for the 35 cells (14.99-16.89E, 48.21-48.93N); its /ledger/20 (900) is Transdanubia, a different land.
- kievan-rus (eu-16, not yet written): gain 884 from `magyars`, 58 cells, 14,668 km2.
- principality-of-hungary (eu-15 other part): may carry a vassal_start for the Moravian remnant from 902/907, and takes the 902 eastern loss of great-moravia; Nitra from 907.
- duchy-of-bohemia: see above; its 955 gain of Moravia from nobody now agrees with great-moravia's dissolve.
- the pechenegs dossier now exists and is no longer a missing counterpart.
