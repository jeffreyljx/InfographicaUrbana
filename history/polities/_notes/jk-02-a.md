# Notes of research batch jk-02-a (Korea, part a)

Written 2026-10-19. Seven dossiers: gojoseon, korean-jin, mahan, byeonhan, jinhan, dongye (the six owned states) and gaya (split from the Byeonhan row). All validate with 0 errors. Eighteen distinct Wikipedia pages opened (one of them a disambiguation page), every one loaded at the first try (no pages failed). The Korean states of this era have thin pages: most events are century-level, so most boundary years are confidence 1 and say so.

## Rows split, merged or corrected

- **Byeonhan (-91..566) is two states.** The 534 and 561 shapes are Gaya after Silla took Geumgwan Gaya (532) and Daegaya (562): the shape loses 3,061 km2 in 534 and Silla's own shape gains 3,113 km2 in the same year; Silla grows by 11,108 km2 in 567, about the 10,542 km2 left. Split into byeonhan (-91..300) and gaya (301..562, new slug, cliopatria_names ["Byeonhan"]). The split year 300/301 is a confidence-1 bridge: the pages give 42 CE (Byeonhan infobox; Gaya "traditional period AD 42-532"), "the 2nd and 3rd centuries", c. 209-212 (Eight Port Kingdoms War between Silla and Kaya), "the late 3rd century" (scholars' transition) and "the 4th century" (Byeonhan lead). The validator warns that byeonhan_534/561 (in byeonhan) and byeonhan_-91 (in gaya) have no verdict: intended, each dossier reviews its own years (gaya_301 is a new keyframe for 301-531). jk-02-x should not write gaya.
- **Gojoseon and Joseon share Wikidata Q28405** but are different states (Old Joseon to 108 BCE; the joseon row 1395-1897). No merge.
- **Korean Jin (-197..-92) equals Mahan + Byeonhan + Jinhan + Dongye** in area (112,814 vs 112,616 km2): Cliopatria draws the east coast (Ye) as Jin land. Both keyframes are adjusted to remove the Dongye shape; the Eastern Ye page puts that coast under Wiman Joseon in 129 BCE, Han in 128 and Lintun in 108. The pages are silent before 129 BCE.
- **Gojoseon's Cliopatria row runs to -92 but the state ends in 108 BCE**; -107..-92 is Han commandery land (Lelang, Lintun, Zhenfan, Xuantu). The -110 shape is adjusted by years only.
- **Dongye starts in 82 BCE, not 91** (Lintun Commandery 108-82 BCE; "Become independent in 82 BC"). -91..-83 is Han's Lintun. Cliopatria's "Dongye" Wikipedia field is a disambiguation page: the article is "Eastern Ye".
- **Dongye ends in 401 (confidence 1), not 391.** The page: "In early 5th-century, however, King Gwanggaeto the Great of Goguryeo annexed Ye". Cliopatria ends Dongye in 391 and starts Goguryeo's 216,216 km2 shape in 392 containing the Ye land (+31,200 km2). The goguryeo dossier should date its gain of the Ye consistently, or the reviewer should pick 391 and shorten keyframe dongye_392. A small southern part went to Silla (no year, no place on the page): not recorded as an event, because no place can be named.
- **Mahan and Jinhan shapes are repeated exactly by Baekje (347) and Silla (378).** Cliopatria hands each over whole in 346/347 and 377/378, although the Baekje page has Baekje founded in 18 BCE inside Mahan and a "full-fledged kingdom" under Goi (234-286), and the Silla page has Silla "its own distinct political entity" by the 2nd century. The Baekje and Silla dossiers must decide their starts; the Mahan and Jinhan shapes then shrink (mahan_-91 and jinhan_-91 notes say so).

## Per state

- **gojoseon**: pages Gojoseon, Wiman Joseon, Four Commanderies of Han. Start -197 is Cliopatria's first year (confidence 1): the pages give only a legend (2333 BCE), a Gija Joseon (1122 BCE) that "many modern experts" deny, and a war with Yan "around 300 BCE". 194 BCE (Wi Man) is a rename. The Liao/Luan river disagreement for the 109 BCE crossing is in the war note. No area on either page, so the infobox comparison could not be made.
- **korean-jin**: pages Jin (Korean state), Samhan, Gojoseon, Wiman Joseon, Eastern Ye. No capital ("Unknown"; "somewhere south of the Han River"), so none is drawn. End -92 is a bridge: the infobox says the Samhan succeeded Jin in the 2nd century BCE, Samhan "formed around ... 108 BCE". King Jun's flight to Jin ("around 194-180 BCE", Samhan page) is not a territorial event.
- **mahan**: pages Mahan confederacy, Samhan, Baekje. Capital Mokji (Cheonan) per the infobox, though the same page has the Mokji state defeated by Paekche in the 1st century CE. End 346 is a bridge: 1st century, late 3rd, 4th (346-375), 5th and 6th centuries are all on the pages.
- **byeonhan**: pages Byeonhan confederacy, Gaya confederacy, Samhan. No capital. The page's thirteen statelets reach Gimcheon/Seongju north of the shape's 35.9N edge; not corrected (the page itself lists 13 names for 12 statelets).
- **jinhan**: pages Jinhan confederacy, Silla, Samhan. No capital. End 377 is a bridge: the page gives "4th century CE"; 377 is the year Silla sent emissaries to China (Silla page).
- **dongye**: pages Eastern Ye, Four Commanderies of Han, Okjeo, Goguryeo, Gwanggaeto the Great. Only two ledger events are dated by the pages. Goguryeo's vassalage of the Ye under Taejo (reign 53-146) is undated, so no vassal_start is recorded here; the goguryeo dossier should carry it with counterpart dongye. Raids of AD 40 (September, Hwaryeo and Bulnaeye) and AD 60 (Haslla on Siljikgok) are in the wars list only.
- **gaya**: pages Gaya confederacy, Geumgwan Gaya, Daegaya, Byeonhan confederacy, Silla. Dated losses 532 (Geumgwan, to Silla) and 562 (Daegaya). The Gaya page also says the confederacy "disintegrated under pressure from Goguryeo between 391 and 412", contradicting its own 532/562; listed as a war, no event. 529 "Silla destroyed Takgitan Gaya" has no place on the page, so no loss event. No contest events: the pages date four episodes, not a front.

## States needing dossiers from others

- Lelang Commandery (lelang-commandery, -108..313), Xuantu (-107..319), Lintun and Zhenfan (-107..-82), Daifang (204..315), and the Canghai Commandery (c. -128..-126): the Han commanderies in Korea, no Cliopatria row, group jk-02-x (or the Han dossier ea-02). Gojoseon's land goes to them in 108 BCE and Dongye's land is Lintun until 82 BCE.
- Goguryeo (jk-02-b/c): Ye vassalage and annexation dates (see above); Lelang absorbed in 313.
- Baekje and Silla: starts and trimmed Mahan/Jinhan shapes (see above).

## Gazetteer

No unresolved region names (all seven dossiers resolve with --resolve). The Samhan have no gazetteer region entry ("Samhan"); the dossiers use the Cliopatria shapes instead.

## Page budget

Gojoseon 3 (2 own), Korean Jin 5 (2 own), Mahan 3, Byeonhan 3, Jinhan 3, Dongye 5, Gaya 5 (new state of a split row). Pages shared across dossiers; 18 distinct pages in all (17 articles and the Dongye disambiguation page).
