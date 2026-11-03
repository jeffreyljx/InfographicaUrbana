# eu-06-b research notes (Migration kingdoms, part b)

Written 2026-10-19. Five dossiers: saxons, vandals, angles, visigoths, alans. All validate with `validate_dossier.py --resolve` (0 errors, 0 warnings). Read this before the dossiers.

## Method caveat for the reviewer

WebFetch returned a summary written by a small model, not the raw page, in every case. The quoted sentences in `note` fields are the sentences that summary printed as quotations; where the summary said the page was silent (for example the 411 partition on the Vandals page, Addax on the Alans page, Seville on the Hasdingi page) the dossier says so. A reviewer with raw access should spot-check the quoted sentences, above all the dates the summaries supplied without a quotation (Vandals page: Pyrenees crossing 13 October 409, the Rhine crossing as 31 December 405).

## Decisions that touch other groups

- **visigoths / visigothic-kingdom (eu-06-?)**: Cliopatria's Visigoths row runs 396-425 and its Visigothic Kingdom row begins 426, but the pages (and the visigothic-kingdom dossier, found 418) date the settled kingdom to 418. This dossier therefore ends in 418 (the army is still in Baetica and Lusitania until the recall; the kingdom's `found` is also 418, so both exist in that one year on different land). The 417-425 Aquitaine shape belongs to visigothic-kingdom_418 from 418.
- **vandals / vandal-kingdom**: the Vandals row (337-438) is cut at 434; vandal-kingdom starts 435 (treaty). Cliopatria's 426-438 Baetica shape is wrong from 429 (the Vandals crossed to Africa); the 435-438 years are the kingdom's.
- **alans**: ends 418 (Attaces killed; survivors join Gunderic); Cliopatria's 417-438 shapes are corrected to 417-418 and `wrong` for 426-438. The vandals dossier has the `merge` with alans in 418.
- **saxons**: ends 804 (Cliopatria's last shape is 799; its Franks cover Saxony 788-792 and from 800). The Frankish side of every Saxon `contest`/`loss`/`gain` pair uses the counterpart `kingdom-of-the-franks` (eu-07); the Saxon tribute to Chlothar (555-556), Charles Martel (738) and Pepin (758) should appear in that dossier as vassal tint if it uses one. Nordalbingia goes to `obotrites` (eu-07) in 804.
- **angles**: successor `scandinavian-minor-kingdoms` (eu-14) for Angeln (Cliopatria's 500 shape covers it) and `anglo-saxon-england` (eu-11) for the migrants. The saxons dossier also has a `split` event to anglo-saxon-england at 449 (Adventus Saxonum).

## Per state

### saxons (9 pages: Saxons, Old Saxony, Saxon Wars, Widukind, Nordalbingia, Chauci, Charles Martel, Chlothar I, Obotrites)
- Cliopatria's 455 jump (6,335 to 82,798 km2) is on no page: `saxons_455` is ok with 'unverified: page budget' and the `gain` is confidence 1 against `nobody`. The Chauci page puts the Chauci-Saxon merger in the 3rd century (Ems-Elbe lowland); the first dated Saxon reach to the Weser is 555.
- 469-641 and 724: the shapes differ by 0-4 cells (boundary noise); all ok, unverified.
- 772-804: the dossier follows the Saxon Wars page's phases. Cliopatria agrees with the page at 775-777 (all but Nordalbingia Frankish) and 788-792 (no Saxon shape; Cliopatria's Franks cover Saxony). It disagrees at 772-774 (a Westphalian patch is Frankish: treated as an incursion, adjust), 778-787 (all Saxony independent: true 778 and 782-784 only), 793-799 (true 793-794; after that only Nordalbingia, adjust plus a new 795-804 keyframe). 779-781 is Nordalbingia only (new keyframe).
- Open: who held the Elbe-north land 795-797 (no page); the date of the 10,000 deportations (795 infobox, 798 Nordalbingia page, 804 Saxon Wars text); Widukind's flight 776 or 777; the Capitulatio de partibus Saxoniae (785 or 755-790).
- No capitals or rulers (a league of four peoples without a king in the pages).
- Page failures: none.

### vandals (6 pages, one over the 5-page budget: Vandals, Crossing of the Rhine, Silingi, Hasdingi, Gaiseric, plus Gunderic read for the alans dossier and cited for reign dates)
- Shapes: Pannonia 337-405 ok (the 358-394 shapes unverified, unchanged); 407 loses its German half; 410 is a one-year plunder zone; 411-413 is Gerontius's allotment (Galicia plus Baetica) and Cliopatria's own 414-416 shape; 417-418 only Gallaecia; 419-428 Baetica; 429-434 Mauretania and Numidia (new).
- Disagreements: crossing 405 (Vandals page, Kulikowski) / 406 (Crossing page, tradition: used); Gunderic to Baetica 419 / 419-420 / 420-1; Hippo Regius 431 (14-month siege) / 432 (Vandals page: used); migrants 80,000 / 50,000.
- No capital before Hippo Regius (432). Silingi and Hasdingi have no dossier of their own (Cliopatria has one row).

### visigoths (5 pages: Visigoths, Alaric I, Wallia, Athaulf, Sack of Rome (410))
- The row is a track of presence zones; seven Cliopatria shapes became thirteen keyframes. Dropped: the Peloponnese after 397 (Epirus only), the Greek half of the 402 shape, Rome 410-413 beyond 410. Added: 395 Thessaly, 403-406 Pannonia, 407 Noricum, 411 southern Italy, 413 Narbonne/Toulouse, 415-416 Barcelona, 417-418 Baetica and Lusitania.
- Pages disagree on Alaric's death (early 411 / late 410) and on the 408 siege date (September / late 408 / October). The Visigoths article is thin on 412-417; Athaulf's and Wallia's pages cover it. The 416 location, the 401 departure from Epirus and the 403 move into Pannonia are confidence 1.
- The 416 treaty and the 418 foedus make the Goths a client of the western-roman-empire; the schema's vassal event names the vassal, so it belongs on that dossier.
- Gazetteer lacks Pannonia and Noricum: Hungary and Austria stand in.

### alans (2 pages: Alans, Gunderic)
- Starts 409 (page: 'around 409'), not Cliopatria's 414. The kingdom ends 418 with Attaces's death. Alans of Gaul (Goar, Orléans 442, Sangiban, Orléans 463, Childeric 466) and the Alans of the Caucasus (alania) are not in this dossier; the first is a state Cliopatria lacks (suggested slug alans-of-orleans, about 442-470s, additions batch eu-06-x).
- Page spellings: Attaces on the Alans page, Addax on the Wallia page (used in visigoths).

### angles (2 pages: Angles (a disambiguation page), Angles (tribe))
- The pages give no founding or ending year; found 387, split 441 and dissolve 479 are confidence 1 (Cliopatria's). Tacitus about 98 is the earliest mention; the invasion of Britain is 'during the fifth century'. A gap-filler could open Bede or 'Anglo-Saxon settlement of Britain'.
- No wars on the pages.

## Gazetteer names wanted

Pannonia (region, western Hungary and east Austria), Noricum (region, Austria), Carthaginensis / Hispania Carthaginensis (region), Angeln (region, Schleswig-Holstein), Nordalbingia, Eastphalia, Angria (Engria), Eresburg and Verden (places). The dossiers use countries or Cliopatria shapes instead and carry the name in `text`.

## Families (colour hue)

saxons germany; vandals africa (continuity with vandal-kingdom); visigoths iberia (with visigothic-kingdom); alans steppe (with alania); angles britain (with the English kingdoms).
