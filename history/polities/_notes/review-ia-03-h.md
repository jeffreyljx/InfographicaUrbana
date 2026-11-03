# Review, batch ia-03-h (2026-10-19)

Dossiers: taliban, republic-of-uzbekistan, turkmenistan. Validator (`--resolve`): 0 errors in all three; one warning (republic-of-uzbekistan /ledger/2: place 'Bagys' unknown to the gazetteer). Neighbour dossiers read (ledger lines for the years and counterparts concerned): afghanistan, kazakhstan, kyrgyzstan, republic-of-tajikistan, mujahideen. Not yet written (exception: owned by a group that has not run yet): islamic-republic-of-iran (me-10), islamic-republic-of-pakistan and republic-of-india (sa-06). union-of-soviet-socialist-republics has a polities.csv row but no dossier (listed by the author).

Pages opened: Islamic Emirate of Afghanistan (1996-2001) (twice), Northern Alliance, Taliban, Uzbekistan (twice), Kazakhstan-Uzbekistan border, Kyrgyzstan-Uzbekistan border, Turkmenistan, Turkmen SSR. None failed.

Grid geometry was computed with tools/gazetteer.py (cells of 252.9 km2) on the keyframe corrections of taliban and afghanistan.

## taliban: verdict thin (reviewer note fixes applied)

Spot checks, all confirmed on the page with the year: /ledger/0 (Emirate page: 'first emerged near Kandahar in the spring and summer of 1994', 'October-November 1994'), /ledger/4 (Northern Alliance: 'The Taliban seized Kabul on September 27, 1996, and established the Islamic Emirate of Afghanistan'), /ledger/6 ('By 1998, the Taliban controlled 90% of Afghanistan'), /ledger/7 (Taliban: 'On 8 August 1998, the Taliban launched an attack on Mazar-i-Sharif'), /ledger/8 (Taliban: 'In 1999, the town of Bamian was taken'), /ledger/9 (Northern Alliance: Taloqan HQ 'until September 5, 2000'), /ledger/10 (infobox 'Fall of Kabul: 13 November 2001'), /ledger/13 ('ceased to exist on 7 December 2001'). No fabricated or mis-dated event found.

Area: infobox 587,580 km2 (footnote: '90%'; the page says 'By the end of 2000, the Taliban controlled 90%'); taliban_2000 560,314 km2; ratio 0.95; acknowledged in /keyframe_review/4.

Applied by the reviewer (validated after):
- /ledger/4/note: added the Emirate infobox step 'Name changed to "Emirate": 29 October 1997'; the rename stays at September 1996 (Northern Alliance page).
- /ledger/8/note: added the Emirate page's 'After Battles of Mazar-i-Sharif (1997-98), the Bamyan valley came into Taliban control', which with the Northern Alliance page's 1998 points to 1998 rather than 1999.

Not applied (non-blocking, for the author or the gap-filler):
- /keyframe_review/4/correction: the 5 September 2000 gain of Taloqan (/ledger/9, confidence 3) is not drawn: Cliopatria's Taliban 2000 shape holds only 6 of the 18 cells within 40 km of Taloqan, and the afghanistan dossier's afghanistan_2000 correction removes the 50 km disk; for 2000-2001 the 18 cells (about 4,550 km2) belong to nobody. Fix: correction = union of the present correction and {"place": "Taloqan", "km": 50, "country": "Afghanistan"} (same radius as afghanistan); with that the hole closes and no overlap appears (checked).
- Cross-dossier overlap 1998-1999, not flagged in the author's notes: taliban_1998/_1999 (Cliopatria 2000 less Takhar, Bamyan, Pakistan) and afghanistan_1998 (Cliopatria Afghanistan 1996 less Balkh) share 322 cells, about 81,400 km2: Jawzjan, Faryab, Sar-e Pol, Samangan, Kunduz, Baghlan and Badghis. The taliban side rests on 'By 1998, the Taliban controlled 90% of Afghanistan' (confirmed); the afghanistan side keeps the provinces because its pages give only Mazar. Route to the afghanistan author: drop those provinces from afghanistan_1998 and add the 1998 loss to taliban.
- Bamyan (about 15,400 km2) is in neither outline in 1996-1998 (flagged by the author); the taliban /ledger/8 gain of Bamyan from afghanistan has no mirror loss. Route to afghanistan (add Bamyan to afghanistan_1996/_1998 and the loss), or move the taliban gain to 1998 per the Emirate page.
- 1994-1995: taliban_1994 is Kandahar alone, while afghanistan_1992 (1992-1995) still covers Kandahar; the afghanistan dossier records a contest_start (1994, counterpart taliban) on Kandahar, Hilmand, Zabul, Uruzgan, citing the Islamic State of Afghanistan page ('late 1994 ... managed to conquer large parts of southern Afghanistan', 'steady gains throughout 1995 and 1996'). The taliban dossier has no matching contest and its 1994 found has no mirror loss: the overlap is about 49,800 km2 for 1994-1995.
- The native names: the Pashto form 'د افغانستان اسلامي امارت' (Da Afghānistān Islāmī Imārāt) is on the Emirate page; the Dari form is not on it.

Thin (for a gap-filler): the growth from Kandahar to the 1996 outline (/ledger/1 is confidence 1, an inference from Cliopatria's shape): Islamic State of Afghanistan page and the Afghan Civil War (1992-1996) page; the northern provinces of 1998 (/keyframe_review/2): Battles of Mazar-i-Sharif (1997-1998), Afghan Civil War (1996-2001); Bamyan 1998/1999.

## republic-of-uzbekistan: verdict fix (applied by the reviewer)

Spot checks confirmed: /ledger/0 ('On 31 August 1991, Uzbekistan declared independence after the failed coup attempt in Moscow'), /ledger/2 (Kazakhstan-Uzbekistan border: 'Ultimately, Bagys was integrated into Kazakhstan', 517 ha exchange, Treaty on Specific Border Sections 9 September 2002, in force 5 September 2003; the page does not date Bagys itself, confidence 2 is right), /ledger/4 ('On November 17, 2022, Kyrgyzstan gained 156 km2 from Uzbekistan'), /ledger/5 ('Until 2024, the Kyrgyz enclave of Barak existed in Uzbekistan'; confidence 1 is right, the page gives no mechanism).

Area: infobox 448,978 km2 (4.9% water) against 415,143 km2 (2006-2024 shape): 0.92, acknowledged.

Applied: /identity/rulers/1 (Mirziyoyev) had no source; added https://en.wikipedia.org/wiki/Uzbekistan and replaced the note with the page's words ('the Oliy Majlis appointed Prime Minister Shavkat Mirziyoyev as interim president'; elected 'with 88.6% of the vote' and 'sworn in on 14 December').

Cross-checks: Bagys matched by kazakhstan /ledger/3 (2002-09 gain, confidence 1). The other half of the exchange ('semi-desert lands near the villages of Nysan-1, Nysan-2, and Baimurat in the Kyzylorda Region', to Uzbekistan by the reading) is in neither ledger; below a grid cell. The 2022 loss and the 2024 Barak gain have no mirror in kyrgyzstan (flagged by the author): route to kyrgyzstan.

Thin by design (budget 5 pages, used): Aral shore entries /ledger/1 and /ledger/3 (confidence 1, one and five cells); Barak /ledger/5 (confidence 1); the Kempir-Abad (Andijan) reservoir side of the 2022 deal is not on the page; the Turkmenistan-Uzbekistan border and the Tajik 2018 deals are not opened; `wars` empty.

## turkmenistan: verdict fix (applied by the reviewer)

Spot checks confirmed: /ledger/0 ('Turkmenistan declared its independence on 27 October 1991, following the dissolution of the Soviet Union'; constitutional law of 27 October, Article 1), the predecessor land (Turkmen SSR: 'Since its creation, the borders of Soviet Turkmenistan remained unchanged'; 13 May 1925), rulers (Niyazov 'until his death in 2006'; Serdar 'On 19 March 2022 ... sworn in').

Area: infobox 491,210 km2 (body 488,100) against 467,932 km2: 0.95, acknowledged.

Applied: /identity/rulers/1 (Gurbanguly Berdimuhamedow) started in 2007, leaving 2006-2007 empty after Niyazov; the page says that after 'the December 2006 death of Niyazov' he 'was named interim head of government': from set to 2006, source added, note rewritten. /identity/rulers/2 (Serdar) had no source: added https://en.wikipedia.org/wiki/Turkmenistan.

No territorial events after 1991 and the two shapes are identical: nothing to explain. Leads only: Turkmenistan-Uzbekistan border page ('In 2004, a series of bilateral treaties restored friendly relations'), Caspian status.

## Cross-dossier matrix (summary; the machine copy is notes/phase-b/reviews/ia-03-h.json)

- taliban 1996 gain / 1996-09 gain Kabul <-> afghanistan 1996-09 loss (Taliban 1996 shape): matched.
- taliban 1998 gain (north) <-> afghanistan: only Balkh lost; mismatch, 81,400 km2 overlap 1998-1999.
- taliban 1998-08 Balkh <-> afghanistan 1998-08 loss Balkh: matched.
- taliban 1999 Bamyan <-> afghanistan: missing (Bamyan in neither 1996-1998).
- taliban 2000-09 Taloqan (40 km) <-> afghanistan 2000-09 loss Taloqan (50 km): event matched, land mismatch (hole 2000-2001).
- taliban 2001-11 loss Kabul <-> afghanistan 2001-11 gain Kabul: matched.
- taliban 2001-12 loss/dissolve <-> afghanistan 2001-12 gain (Cliopatria Taliban 2000, which still includes 17 Pakistani cells; afghanistan should subtract country Pakistan): matched.
- republic-of-uzbekistan 2002-09 loss Bagys <-> kazakhstan 2002-09 gain: matched.
- republic-of-uzbekistan 2022-11 loss / 2024 gain <-> kyrgyzstan: missing.
- found events of republic-of-uzbekistan and turkmenistan from union-of-soviet-socialist-republics: exception (no dossier yet).
