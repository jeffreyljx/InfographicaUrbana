# Review of batch sa-06-e (2026-10-25)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/sa-06-e.json. Validator (--resolve): 0 errors on all four dossiers; warnings only (junagadh-state unknown slug, Kachchatheevu radius resolves to no cell).

## republic-of-india: FAIL

Area: infobox 3287263 km2 (2024), Cliopatria/keyframe 3182469 km2, ratio 0.968, acknowledged True.

Findings:
- `/keyframe_review/0/correction; /keyframe_review/1/correction` (blocking, for the author): The NEFA repair unions all of Arunachal Pradesh into India from 1947, including the Tawang tract north of Se La, which Tibet administered until February 1951; no ledger event gains it, and the tibet dossier holds the same 12 cells from 1947 (tibet /ledger/40-41, occupation_end british-raj 1947), so India silently takes Tibetan land for 1947-1950. Evidence: Tawang page: 'India occupied Tawang in February 1951 and removed Tibetan administration from the area.' Tawang district page: 'In 1944, administrative control was extended over the area of the Tawang tract lying South of the Sela Pass' ... 'no steps were taken to evict the Tibetan from the area North of the pass which contained Tawang town.' The cited NEFA page does not mention Tawang at all. Gazetteer: tibet's Tawang-tract spec resolves to 15 cells, 12 of them inside Arunachal Pradesh. Fix: In both corrections replace the Arunachal Pradesh member with {"minus": [{"admin1": "Arunachal Pradesh", "country": "India"}, {"minus": [{"cliopatria": "Tibet", "year": 1939}, {"cliopatria": "Tibet", "year": 1938}], "text": "the Tawang tract"}]}; add a ledger event {"year": 1951, "month": 2, "type": "gain", "counterpart": "tibet", "region": {"minus": [{"cliopatria": "Tibet", "year": 1939}, {"cliopatria": "Tibet", "year": 1938}], "text": "the Tawang tract"}, "source": "https://en.wikipedia.org/wiki/Tawang", "confidence": 3} quoting the sentence above; add the Tawang page to sources[]; update the keyframe notes (the NEFA tracts south of Se La were Indian from 1947, Tawang from Feb 1951). The tibet owner (ea-06) should add the mirror loss of 1951-2.
- `/ledger/2; /keyframe_review/1..4; /keyframe_review/5/note` (non-blocking, for the author): The October 1947 gain (NE Jammu and Kashmir plus Ladakh) holds 40 cells outside Cliopatria's 1948-1962 India outline (37 in Ladakh, 6 inside Pakistan's 1948 shape); 23 of them come back in Cliopatria's 1963 shape, which is the 'unexplained 1963 Ladakh redraw' of keyframe 5. So eastern Ladakh is India's in late 1947, vanishes from 1948 to 1962 with no loss, and returns in 1963 with no gain. Evidence: Gazetteer cell counts: (Ladakh u J&K) minus Republic of India 1948 = 40 cells; Republic of India 1963 minus 1962 = 25 cells added, 23 of them in Ladakh and all 23 among the 40; 6 of the 40 lie in Islamic Republic of Pakistan 1948. Sino-Indian War page: no 1963 line change; 'On the Aksai Chin front, China already controlled most of the disputed territory'. So the 1963 change is Cliopatria's repair of its own 1948-1962 outline, not an Indian gain. Fix: Either add {"minus": [{"admin1": "Ladakh", "country": "India"}, {"cliopatria": "Islamic Republic of Pakistan", "year": 1948}]} to the 1948 correction and mark keyframes 1953, 1956 and 1961 adjust with the same union (keyframe 5 then needs no event; rewrite its note), or intersect the 1947 gain with {"cliopatria": "Republic of India", "year": 1948} and leave keyframe 5 marked unexplained. In either case subtract Pakistan's 1948 shape from the gain region so it does not take Pakistani-held cells.
- `/ledger/6; /keyframe_review/0/note; /keyframe_review/1/note` (non-blocking, for the author): Sikkim (25 of 27 cells) sits inside India's 1947 and 1948 outlines with no relation until the 1950 vassal_start, while kingdom-of-sikkim draws the same land as its own (keyframe 1861-1975) and has no vassal event with India at all; for 1947-1949 the two dossiers both own Sikkim. Evidence: Political integration page: 'in 1950 a full treaty with the Chogyal of Sikkim which in effect made it a protectorate' (no earlier relation on the page). kingdom-of-sikkim ledger: last events 1888 contest with Tibet, then 1975-5 dissolve to republic-of-india. Fix: Subtract {"admin1": "Sikkim", "country": "India"} from the 1947 and 1948 corrections (Sikkim is a protectorate, not Indian land, until the 1975 gain), or find a page for the 1947 standstill arrangement and start the vassal tint in 1947. Route the missing vassal_start (1950) to the kingdom-of-sikkim owner.
- `/ledger (missing, 1949-8)` (non-blocking, for the author): kingdom-of-bhutan /ledger/20 gains Dewangiri from republic-of-india in August 1949; India's ledger has no loss (the author flagged it). Evidence: Cross-check: no republic-of-india loss within a year of 1949 naming kingdom-of-bhutan. The tract is about 83 km2, under one grid cell, so no keyframe is affected. Fix: Add {"year": 1949, "month": 8, "type": "loss", "counterpart": "kingdom-of-bhutan", "region": {"place": "Dewangiri", "km": 6, "country": "Bhutan"}} citing the page the Bhutan dossier cites, confidence 2.
- `/ledger/8` (non-blocking, applied by reviewer): Chandernagore was at confidence 1 with a note saying the Political integration page is silent; the page names it and dates it. Evidence: Political integration of India: 'It was ceded to India on a de facto basis on 14 August 1949 and de jure on 2 May 1950.' The sibling french-india (Chandannagar page) has de facto 2 May 1950, so the pages disagree on the de facto date. Fix: Applied by the reviewer: confidence 2, note rewritten with the quote; year and month 1950-5 kept to match french-india.

Gaps for a gap-filler:
- `/wars/4`: 1965 war listed with empty zones; ground changed hands (Haji Pir, Sialkot and Lahore sectors) until the Tashkent Declaration; also the 1968 Rann of Kutch tribunal award (Pakistan received about 900 km2, transferred 1969) is not in the ledger (try https://en.wikipedia.org/wiki/Indo-Pakistani_war_of_1965)
- `/wars/7`: Kargil War listed with empty zones; Pakistani forces held heights in the Kargil sector May-July 1999 (a contest zone) (try https://en.wikipedia.org/wiki/Kargil_War)
- `/ledger/20`: Sikkim admission month (kingdom-of-sikkim dates it May 1975); India's event has no month (try https://en.wikipedia.org/wiki/Kingdom_of_Sikkim)
- `/keyframe_review/8`: 1979-1982 Bhutan-frontier noise (3 cells) unexplained; within the page budget, acceptable (try https://en.wikipedia.org/wiki/Bhutan%E2%80%93India_border)

Spot checks: /ledger/4 confirmed; /ledger/6 confirmed; /ledger/10 confirmed; /ledger/13 confirmed; /ledger/15 confirmed; /ledger/21 confirmed; /ledger/8 confirmed (page names it; author said silent; confidence raised to 2); /keyframe_review/0/correction (Tawang) not on page: Tawang was Tibetan until February 1951.

## sri-lanka: FIX

Area: infobox 67240 km2 (2024), Cliopatria/keyframe 73532 km2, ratio 1.094, acknowledged True.

Findings:
- `/ledger/10` (non-blocking, applied by reviewer): The 1999 loss of the Vanni had no month. Evidence: Sri Lankan civil war page: 'Nearly all the Vanni rapidly fell back into LTTE hands' in 'Operation Unceasing Waves III on 2 November 1999'. Fix: Applied by the reviewer: month 11, note extended; the mirror tamil-eelam /ledger/5 got the same month.

Gaps for a gap-filler:
- `/ledger/11`: The east (Batticaloa, Trincomalee, Ampara) passing to the Tigers is bridged at 2000, confidence 1; the civil-war page says the LTTE set up 'a series of vital bases around the Trincomalee Harbour ... and the Eastern Province' after the 2001 elections, and the Karuna split of March 2004 is not recorded (try https://en.wikipedia.org/wiki/Eelam_War_III)
- `/ledger/13`: The 2006-2007 eastern recapture is one event at 2007-7; the civil-war page dates Mavil Aru (15 August 2006) and Sampur (4 September 2006) in Trincomalee district and Vakarai (19 January 2007) in Batticaloa, so Trincomalee could be a 2006-9 gain and Batticaloa north a 2007-1 gain (try https://en.wikipedia.org/wiki/Sri_Lankan_civil_war)

Spot checks: /ledger/1 confirmed; /ledger/3 confirmed; /ledger/2 confirmed (ceding party not named; confidence 2 is right); /ledger/6 confirmed; /ledger/12 confirmed; /ledger/13 confirmed; /ledger/10 confirmed (month 11 added).

## people-s-republic-of-bangladesh: PASS

What I tried: Validator clean; new keyframe 1971-1972 has from, to and correction; found, contest_start, contest_end and gain all dated on the Liberation War page (26 March, 25 March night, 16 December 1971) and the 1971-12 gain mirrors islamic-republic-of-pakistan /ledger/13; Meherpur 17 April 1971 confirmed (Bangladesh infobox says 10 April, flagged by the author); infobox area 148,460 km2 against 144,765 (0.975); capitals inside the shape; the 1974 agreement and 2015 enclave exchange are below one cell. Could not break it.

Area: infobox 148460 km2 (2024), Cliopatria/keyframe 144765 km2, ratio 0.975, acknowledged True.

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /identity/capitals/0 confirmed.

## tamil-eelam: THIN

Area: infobox 18880 km2 (2009), Cliopatria/keyframe 0 km2, ratio 1.17, acknowledged True. No Cliopatria row. 18,880 km2 is the claimed state (N+E provinces); the LTTE page gives 76 percent of it held at the 2000 peak (about 14,350 km2); the 2000-2006 keyframe is 58 cells, about 16,800 km2 (ratio 1.17); the author notes whole districts overstate it.

Findings:
- `/ledger/5` (non-blocking, applied by reviewer): The 1999 gain of the Vanni had no month. Evidence: Sri Lankan civil war page: 'Operation Unceasing Waves III on 2 November 1999'; 'Nearly all the Vanni rapidly fell back into LTTE hands'. Fix: Applied by the reviewer: month 11, note extended (mirror sri-lanka /ledger/10 likewise).

Gaps for a gap-filler:
- `/ledger/0`: Start 1990 is a confidence-1 bridge; no page dates the start of the Tigers' administration or names a seat before Kilinochchi 1998 (try https://en.wikipedia.org/wiki/Eelam_War_II)
- `/ledger/6; /keyframe_review/3`: The Eastern Province (3 of the 2000-2006 keyframe's districts, most of its 58 cells) enters at 2000 at confidence 1; the Karuna split (March 2004) and the LTTE bases around Trincomalee after 2001 are not dated (try https://en.wikipedia.org/wiki/Karuna_Amman)
- `/ledger/8`: The eastern losses are one event at 2007-7; the civil-war page dates Mavil Aru 15 August 2006, Sampur 4 September 2006 and Vakarai 19 January 2007 (try https://en.wikipedia.org/wiki/Sri_Lankan_civil_war)
- `/keyframe_review/0; /keyframe_review/2`: Whole-district extents: Mullaitivu's interior (held by the Tigers before July 1996, army only at Mullaitivu town) is missing from 1990-1995, and northern Vavuniya (A9 corridor) never appears (try https://en.wikipedia.org/wiki/Operation_Jayasikurui)

Spot checks: /ledger/0 confirmed (government-like functions after the IPKF left in 1989-90; confidence 1 is honest); /ledger/4 confirmed; /ledger/7 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/12 confirmed.

## Cross-dossier matrix

- republic-of-india 1947 gain <- kashmir-and-jammu: mismatch (mirror kashmir-and-jammu 1949 dissolve). India gains J&K and Ladakh on accession (Oct 1947); kashmir-and-jammu has no loss to India and keeps the land until its 1949-1 dissolve (successor republic-of-india). Author flagged. Route to the kashmir-and-jammu owner (sa-06): add a 1947-10 loss to republic-of-india or end the state at accession.
- republic-of-india 1947 gain <- junagadh-state: exception. No dossier; listed in counterparts_needing_dossiers.
- republic-of-india 1948 gain <- hyderabad-state: matched (mirror hyderabad-state 1948 dissolve). Both 1948-9.
- kingdom-of-bhutan 1949 gain <- republic-of-india: missing. Dewangiri (Aug 1949): no loss in republic-of-india; sub-cell. Author flagged.
- republic-of-india 1950 vassal_start <- kingdom-of-sikkim: missing. kingdom-of-sikkim has no vassal_start with India (its ledger jumps from 1888 to the 1975-5 dissolve). Route to the kingdom-of-sikkim owner.
- republic-of-india 1950 gain <- french-india: matched (mirror french-india 1950 loss). Chandernagore, both 1950-5.
- republic-of-india 1951 gain <- tibet: missing. Event missing on both sides: Tawang taken by India February 1951 (Tawang page). tibet /ledger/40-41 (confidence 1) give the tract back to Tibet in 1947 and nothing removes it before the 1951-5 dissolve; India's corrections hold it from 1947. Route the tibet half to ea-06.
- republic-of-india 1954 gain <- french-india: matched (mirror french-india 1954 loss). Pondicherry, Karaikal, Mahe, Yanam 1954-11 (french-india radii differ slightly: Mahe 15 km against India's 8 km).
- republic-of-india 1961 gain <- Free Dadra and Nagar Haveli: exception. No dossier; listed in counterparts_needing_dossiers.
- republic-of-india 1961 gain <- portuguese-india: matched (mirror portuguese-india 1961 dissolve). 1961-12; contest pair matched too.
- republic-of-india 1974 loss <- sri-lanka: matched (mirror sri-lanka 1974 gain). Kachchatheevu, sub-cell.
- republic-of-india 1975 gain <- kingdom-of-sikkim: matched (mirror kingdom-of-sikkim 1975 dissolve). India has no month; Sikkim has 1975-5. vassal_end 1975 also matched by the dissolve.
- republic-of-india 1984 gain <- islamic-republic-of-pakistan: missing. Siachen (April 1984): islamic-republic-of-pakistan has no loss; its Cliopatria shapes hold 3 of NE's 7 'Siachen Glacier' cells through 1987. Siachen page: 'Prior to 1984 neither India nor Pakistan had any permanent presence in the area', maps showed it on the Pakistani side. Route to the Pakistan owner (sa-06): add a 1984-4 loss of {"country": "Siachen Glacier"} or cut those cells from its shapes.
- people-s-republic-of-bangladesh 1971 gain <- islamic-republic-of-pakistan: matched (mirror islamic-republic-of-pakistan 1971 loss). 1971-12; contest pair 1971-3/1971-12 matched.
- sri-lanka 1990 loss <- tamil-eelam: matched (mirror tamil-eelam 1990 found). Same region (Jaffna, Kilinochchi).
- sri-lanka 1995 gain <- tamil-eelam: matched (mirror tamil-eelam 1995 loss). 1995-12 Jaffna.
- sri-lanka 1996 loss <- tamil-eelam: matched (mirror tamil-eelam 1996 gain). 1996-7 Mullaitivu.
- sri-lanka 1996 gain <- tamil-eelam: matched (mirror tamil-eelam 1996 loss). 1996-9 Kilinochchi town.
- sri-lanka 1998 loss <- tamil-eelam: matched (mirror tamil-eelam 1998 gain). 1998-9 Kilinochchi town.
- sri-lanka 1999 loss <- tamil-eelam: matched (mirror tamil-eelam 1999 gain). 1999-11 (month added to both by the reviewer).
- sri-lanka 2000 loss <- tamil-eelam: matched (mirror tamil-eelam 2000 gain). East (confidence 1 both sides) and Elephant Pass 2000-4.
- sri-lanka 2007 gain <- tamil-eelam: matched (mirror tamil-eelam 2007 loss). 2007-7 east.
- sri-lanka 2008 gain <- tamil-eelam: matched (mirror tamil-eelam 2008 loss). 2008-8 Mannar.
- sri-lanka 2009 gain <- tamil-eelam: matched (mirror tamil-eelam 2009 loss). 2009-1 Kilinochchi and Mullaitivu; 2009-5 last pocket against the tamil-eelam dissolve.

## Problems

- No page failed to load. 14 distinct pages opened: Political integration of India, India, NEFA, Tawang district, Tawang, Sino-Indian War, Siachen conflict, Annexation of Goa, Sri Lankan civil war (twice), LTTE, Tamil Eelam, Sri Lanka, Bangladesh Liberation War, Bangladesh.
- Neighbour dossiers needing changes (other groups): tibet (ea-06) holds the Tawang tract 1947-1951 at confidence 1 and needs a 1951-2 loss to republic-of-india; islamic-republic-of-pakistan (sa-06) lacks the 1984-4 Siachen loss; kingdom-of-sikkim lacks the 1950 vassal_start with India; kashmir-and-jammu (sa-06) lacks the 1947-10 loss to India.
- Neighbours not yet written (exception: groups not run): people-s-republic-of-china, union-of-myanmar, estado-novo.
- Reviewer edits applied in place and re-validated: republic-of-india /ledger/8 (confidence 1 to 2, note), sri-lanka /ledger/10 and tamil-eelam /ledger/5 (month 11). The india fail rests on one blocking finding (Tawang); the others are non-blocking.
