# Review of batch me-08-b (2026-10-24)

Reviewer: adversarial review under history/briefs/reviewer-brief.md and the orchestrator's adjustments: 4 spot checks per dossier, small verified fixes applied in place. The machine copy is history/notes/phase-b/reviews/me-08-b.json.

## samanid-empire: fail

Area: infobox 2850000 km2 (928), Cliopatria 3059840, ratio 1.07. 

Findings:
- `/ledger/25` **blocking**: The 962 event records Ghazna (Zabulistan) as Samanid land lost to the Ghaznavids, but the cited page says Alp Tigin, a nominal Samanid vassal, took Ghazna from the Lawik dynasty, so it was never Samanid land. Evidence: Samanid Empire page: 'Alp Tigin, nominal vassal of the Samanids, conquered Ghazna in 962 from the Lawik dynasty.' The ghaznavid-empire dossier's /ledger/0 (962 found) names lawik-dynasty as counterpart, so this loss has no mirror. Confidence 3. Fix: Delete the 962 loss, or re-type it as vassal_start with counterpart ghaznavid-empire (962, c2: nominal allegiance until 999). Take Ghazna/Zabulistan out of the 922-961 corrections (/keyframe_review/8, /keyframe_review/9) and say the Lawiks held it. Rewrite the /keyframe_review/10 note so the 296 thousand km2 drop is not credited to Ghazna.
- `/ledger/20`: Gorgan is gained three times (931, 933, 935) with no loss in between. Evidence: /ledger/21 (932) takes away only Tabaristan. ziyarid-dynasty /ledger/4 has Mardavij taking Gurgan in 932, and its /ledger/10 has Vushmgir taking Gorgan 'from the Samanids' around 935. Samanid page: 'In 935, Nasr II re-established Samanid control in Gurgan and made Mardavij's successor Vushmgir his vassal.' Fix: Add Gorgan to the 932 loss (/ledger/21). Before /ledger/24, add a 935 loss of Gorgan to ziyarid-dynasty (c1), or drop /ledger/24 and enter 935 as a vassal_start of the Ziyarids, which is what the page says.
- `/ledger/17`: Ray is lost to the Sajids in 917 (/ledger/14) and again in 924, but never regained in between. Ray taken in 928 (/ledger/18) is also never lost again before the 933 vassal_start (/ledger/23) that puts Ray under Ziyarid tribute. Evidence: Yusuf page: 'in 919 the Sajid was defeated'; in 924 'he conquered Ray from its governor, who had rebelled against the Samanids'. ziyarid-dynasty /ledger/2 has Mardavij taking Ray from Asfar ibn Shiruya in 931. zaydi-alid-dynasties /ledger/15 has the Zaydis holding Ray from 914 (c1). Fix: Add a regain of Ray around 919-922 (c1, after Yusuf's defeat), or make the 924 counterpart the rebel governor. Add a loss of Ray in 929-931 (to Asfar ibn Shiruya, or to ziyarid-dynasty in 931). Reconcile Ray 914-928 with the Zaydi and Sajid dossiers and say in notes which page wins.
- `/ledger/2/counterpart` (applied by reviewer): The counterpart 'Karluks' is not a slug, while the kara-khanids dossier already carries this loss. Evidence: kara-khanids /ledger/1: 893 loss of Talas/Taraz to samanid-empire. The qarlugs dossier ends in 840 with kara-khanids as its successor. Fix: Set the counterpart to kara-khanids (done) and drop Karluks from counterparts_needing_dossiers.
- `/ledger/0`: The overlords' dossiers record the Samanids as vassals, but the Samanid ledger has no vassal events to match. Evidence: abbasid-caliphate /ledger/21 (819 vassal_start), /ledger/49 (900 vassal_start) and /ledger/73-74 (999 vassal_end); tahirid-dynasty /ledger/1 (821 vassal_start) and /ledger/13 (873 vassal_end). The /keyframe_review/0 note says the overlords carry the tint, but the brief requires the mirror on both sides. Fix: Add vassal_start abbasid-caliphate 819 (c3: 'governors of territories under Abbasid suzerainty in 819'), vassal_start tahirid-dynasty 821 and vassal_end 873, and vassal_end abbasid-caliphate 999.
- `/ledger/27`: The contest for Transoxiana starts in 992 here but in 990 in the Kara-Khanid dossier, two years apart. Evidence: kara-khanids /ledger/5: 990 contest_start against samanid-empire (Isfijab, Ferghana, Ilaq, Samarkand, Bukhara). The Samanid page dates the capture of Bukhara to 992. Fix: Either open the contest in 990 here (Isfijab/Fergana) and keep 992 for Bukhara, or ask ia-01 to re-date its side to 992.
- `/ledger/30`: The 998 Ghaznavid gain of Balkh and Herat from the Samanids has no Samanid loss. Evidence: ghaznavid-empire /ledger/6: 998 gain from samanid-empire (Balkh, Herat, c2). The author's gap note covers 994-998. Fix: Add a 998 loss of Balkh and Herat to ghaznavid-empire (c2, citing the Ghaznavid source), or explain why not.

Thin:
- `/keyframe_review/9`: the 960 drop (east edge 76.6E to 75.2E); unverified: page budget (try https://en.wikipedia.org/wiki/Abd_al-Malik_I)
- `/keyframe_review/11`: the 970 loss of 321 thousand km2 (Kerman, Banu Ilyas; Ziyarids leave Tabaristan); undated (try https://en.wikipedia.org/wiki/Banu_Ilyas)
- `/keyframe_review/12`: the 980 loss to 1.93 M km2; no event (try https://en.wikipedia.org/wiki/Nuh_II)
- `/ledger/16`: Saffarid tribute 922-999 at c1; the Saffarid page says they were 'reduced to that of vassals of the Samanids' (undated) (try https://en.wikipedia.org/wiki/Saffarid_dynasty)
- `/ledger/21`: 932 Tabaristan loss at c1; counterpart chain Makan to Mardavij unclear (try https://en.wikipedia.org/wiki/Makan_ibn_Kaki)
- `/ledger/26`: 979 end of Ziyarid vassalage at c1 (try https://en.wikipedia.org/wiki/Qabus)
- `/ledger/30`: 994-998: Sebuktigin, Fa'iq, the Simjurids, Mahmud's governorship of Khorasan (try https://en.wikipedia.org/wiki/Simjurids)

Spot checks:
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Samanid_Empire) - 'In 893, Ismail Samani invaded the territories of the Karluk Turks, taking Talas'
- `/ledger/10`: confirmed (https://en.wikipedia.org/wiki/Samanid_Empire) - 'by 911, Sistan was under complete Samanid control'
- `/ledger/18`: confirmed (https://en.wikipedia.org/wiki/Nasr_II)
- `/ledger/19`: confirmed (https://en.wikipedia.org/wiki/Nasr_II)
- `/ledger/22`: confirmed (https://en.wikipedia.org/wiki/Nasr_II) - 933: 'surrender Gurgan and pay tribute to Nasr for his possession of Ray'
- `/ledger/24`: confirmed (https://en.wikipedia.org/wiki/Samanid_Empire)
- `/ledger/25`: not on page (https://en.wikipedia.org/wiki/Samanid_Empire) - the page says Ghazna was taken 'from the Lawik dynasty' by a 'nominal vassal of the Samanids', not from the Samanids
- `/ledger/28`: confirmed (https://en.wikipedia.org/wiki/Samanid_Empire) - 'the Ilig occupied Bukhara definitively in 999'

## saffarid-dynasty: thin

Area: infobox None km2 (None), Cliopatria None, ratio None. No area in the infobox (confirmed); the author says so.

Findings:
- `/ledger/6/counterpart` (applied by reviewer): The 871 Bamiyan gain names turk-shahis, a state that ended in 870, and the note says the page does not name the ruler, though it does. Evidence: Ya'qub page: his army marched to 'Ghazna, Kabul, and Bamyan, conquering these territories from the Hindu Shahi'. The turk-shahis dossier ends in 870 and hindu-shahis is founded in 870. Fix: Counterpart set to hindu-shahis and the note re-quoted (done).
- `/ledger/21/note` (applied by reviewer): The note (and /keyframe_review/15) quotes 'restored independence', which is not on the page. Evidence: Saffarid page: Sistan 'became independent again under the Saffarid Abu Ja'far Ahmad ibn Muhammad'. Fix: Quote corrected in both places; c2 kept (done).
- `/ledger/24`: Kabul is never lost, although the Hindu Shahi dossier gains it from the Saffarids in 878. Keyframes 878-899 keep the reach to 76.6E. Evidence: hindu-shahis /ledger/1: 878 gain of Kabulistan from saffarid-dynasty. The turk-shahis successor note says 'the Saffarids held it to 878'. The Saffarid page never mentions losing Kabul. Fix: Add an 878 loss of Kabulistan to hindu-shahis (c1/c2, citing the Hindu Shahi page), or record in notes why it is not accepted.
- `/ledger/21`: There is no vassal tie to the Samanids, though the Samanid dossier records one from 922 to 999. Evidence: samanid-empire /ledger/16 (922 vassal_start) and /ledger/31 (999 vassal_end). Saffarid page: 'their role was reduced to that of vassals of the Samanids and their successors'. Fix: Add vassal_start samanid-empire 922 and vassal_end 999 (c2, with that quote).
- `/keyframe_review/13`: Kerman is in the 875-899 shapes and in the 900-909 correction, then dropped in 910, but no event gains or loses it. Evidence: Saffarid page: the caliph was forced 'to recognize Ya'qub as governor of Sistan, Fars and Kerman' (undated). Amr page: the remnant held 'Fars and [Kirman] for several more years' after 900. Fix: Add a Kerman gain (c1/c2, by 875) and a Kerman loss by 910 (c1), or keep Kerman out of the 910 keyframe and say why.
- `/ledger/1/counterpart`: The counterpart 'Salih (ruler of Bost) and the ruler of ar-Rukkaj and Zamindawar' is a free string that is not listed in counterparts_needing_dossiers. Evidence: Brief section 2.3: a counterpart without a dossier must be 'nobody' or listed. Fix: Set the counterpart to nobody with the names in the note, or list it.

Thin:
- `/keyframe_review/8`: the 884-885 dip of 90 thousand km2; unverified: page budget (try https://en.wikipedia.org/wiki/Amr_ibn_al-Layth)
- `/keyframe_review/10`: the 896-897 dip; unverified: page budget (try https://en.wikipedia.org/wiki/Rafi_ibn_Harthama)
- `/keyframe_review/14`: 912-921: who held Sistan, and Kerman after 900 (try https://en.wikipedia.org/wiki/Tahir_ibn_Muhammad_ibn_Amr)
- `/predecessors/0`: whom Dirham served (Tahirid side) (try https://en.wikipedia.org/wiki/Tahirid_dynasty)

Spot checks:
- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Ya%27qub_ibn_al-Layth_al-Saffar)
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Ya%27qub_ibn_al-Layth_al-Saffar)
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Ya%27qub_ibn_al-Layth_al-Saffar) - year confirmed; the counterpart was wrong (fixed)
- `/ledger/11`: confirmed (https://en.wikipedia.org/wiki/Ya%27qub_ibn_al-Layth_al-Saffar) - 'near Lake Bakhtegan in August 875'
- `/ledger/14`: confirmed (https://en.wikipedia.org/wiki/Amr_ibn_al-Layth) - 'In 897 Ray too was handed over to the Saffarids by the Abbasids'
- `/ledger/19`: confirmed (https://en.wikipedia.org/wiki/Amr_ibn_al-Layth)
- `/ledger/21`: confirmed (https://en.wikipedia.org/wiki/Saffarid_dynasty) - substance confirmed; the quote's wording was wrong (fixed)

## zaydi-alid-dynasties: thin

Area: infobox None km2 (None), Cliopatria None, ratio None. No area in the infobox (confirmed).

Findings:
- `/ledger/2` (applied by reviewer): The return to Tabaristan was dated 866 at c1 with 'The page does not date his return', but the page dates it to 865. Evidence: Hasan ibn Zayd page: 'he was chased out of Tabaristan in 865 by Sulayman ibn Abdallah, but returned within the same year' and 'recovered the province'. Fix: Year set to 865, confidence to 3, note re-quoted (done).
- `/ledger/6`: The 877 loss of Gurgan leaves out the page's next words, 'but soon recovered it'. So the ledger and /keyframe_review/2 keep Gurgan out from 877 to 896. Evidence: Muhammad ibn Zayd page: 'The Zaydids were expelled from Gurgan by the Tahirid general Ishaq al-Sari in spring 877, but soon recovered it.' Also /ledger/9 (896) 'recovered Gurgan as well' after Rafi', which implies Gurgan was lost to Rafi' in 889. Fix: Add a gain of Gurgan around 877-878 (c2) and a loss of Gurgan to Rafi' in 889 (with /ledger/7). Correct the /keyframe_review/2 note: the 875 shape is short of Gurgan only for about a year. Say in the note that abbasid-caliphate is the counterpart because the Tahirid dossier ends in 873.
- `/ledger/15`: Holding Rey from 914 (c1, counterpart samanid-empire) contradicts the Samanid dossier, which keeps Ray to 917 and then loses it to the Sajids. Evidence: samanid-empire /ledger/14 (917 loss of Ray to sajid-dynasty) and sajid-dynasty /ledger/5 and /ledger/7. Nasr II page: Ray and Tabaristan 'were taken by the Zaydi Alid Hasan al-Utrush' (undated). Fix: Agree one Ray timeline for 914-928 across the three dossiers, or drop Rey from the Zaydi 914-928 land.
- `/ledger/1`: The 865 loss and regain of Tabaristan have no mirror in the Tahirid dossier, which records 864-865 as a contest. Evidence: tahirid-dynasty /ledger/7-8: contest_start 864, contest_end 865 ('returned that same year and recovered the province'), with no 865 gain or loss. Fix: Either turn /ledger/1-2 into a contest_start/contest_end pair within 864-865, or ask the Tahirid author to add the 865 gain and loss. /ledger/3 (867 Gurgan from tahirid-dynasty) also has no Tahirid mirror.

Thin:
- `/ledger/15`: who held Rayy 914-928; c1 (try https://en.wikipedia.org/wiki/Hasan_ibn_al-Qasim)
- `/keyframe_review/8`: the 923-926 deposition by the Nasiris, and Gurgan in 914-928 (try https://en.wikipedia.org/wiki/Hasan_ibn_al-Qasim)
- `/notes`: the Justanids of Daylam as a counterpart (try https://en.wikipedia.org/wiki/Justanids)

Spot checks:
- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Alid_dynasties_of_northern_Iran)
- `/ledger/2`: mis-dated (https://en.wikipedia.org/wiki/Hasan_ibn_Zayd) - 866 at c1; the page says 865 (fixed)
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Muhammad_ibn_Zayd) - date confirmed, but the page adds 'but soon recovered it', which the ledger ignores
- `/ledger/8`: confirmed (https://en.wikipedia.org/wiki/Muhammad_ibn_Zayd)
- `/ledger/11`: confirmed (https://en.wikipedia.org/wiki/Muhammad_ibn_Zayd)
- `/ledger/13`: confirmed (https://en.wikipedia.org/wiki/Hasan_al-Utrush)
- `/ledger/16`: confirmed (https://en.wikipedia.org/wiki/Hasan_al-Utrush)
- `/ledger/18`: confirmed (https://en.wikipedia.org/wiki/Alid_dynasties_of_northern_Iran)

## sajid-dynasty: thin

Area: infobox None km2 (None), Cliopatria None, ratio None. No area in the infobox (confirmed).

Findings:
- `/ledger/7`: Ray is gained in 917 (/ledger/5) and again in 924 with no loss in between, while /keyframe_review/3 holds Ray from 917 to 928. Evidence: Yusuf page: 'in 919 the Sajid was defeated' and he was imprisoned for three years; 'In 924 he conquered Ray from its governor, who had rebelled against the Samanids.' The author flags it ('The page does not say when Ray was lost after 917'). Fix: Add a loss of Ray in 919 (c1) and take Ray out of 919-923 in a split /keyframe_review/3, or drop the 924 gain and say why.
- `/ledger/9/counterpart`: The dissolve names sallarid-dynasty at c3, but the Sallarids reached Azerbaijan only in 941, twelve years after the end. Evidence: Sajid page: 'eventual expansion of the Sallarid dynasty into Azerbaijan in 941'. sallarid-dynasty /ledger/1 gains Azerbaijan from sajid-dynasty in 941, a state that ended in 929. Fix: Set the dissolve counterpart to nobody (keep the Sallarids as successor with the gap in the note). The Sallarid side needs the same change.
- `/ledger/1/source` (applied by reviewer): The 901 capital move cited the Yusuf page, which gives no year for the move. Evidence: Sajid page infobox: 'Capital: Maragha (889–901) Ardabil (901–929)'. Fix: Source set to the Sajid dynasty page and the note updated (done).

Thin:
- `/ledger/4`: Gagik Artsruni's vassalage is undated (c1 start and end) (try https://en.wikipedia.org/wiki/Gagik_I_of_Vaspurakan)
- `/successors/0`: who held Azerbaijan 930-940 (try https://en.wikipedia.org/wiki/Daysam_ibn_Ibrahim)
- `/keyframe_review/0`: 889-897 is a proxy (the 898 shape); the Caucasian conquests are undated (try https://en.wikipedia.org/wiki/Muhammad_ibn_Abi%27l-Saj)

Spot checks:
- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Sajid_dynasty) - 'appointed as its ruler in 889 or 890'
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Yusuf_ibn_Abi%27l-Saj)
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Sajid_dynasty) - Bakikhanov 'from 908–909 to 919'
- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Yusuf_ibn_Abi%27l-Saj)
- `/ledger/7`: confirmed (https://en.wikipedia.org/wiki/Yusuf_ibn_Abi%27l-Saj)
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Sajid_dynasty)

## tulunids: thin

Area: infobox None km2 (None), Cliopatria None, ratio None. No area in the infobox (confirmed).

Findings:
- `/ledger/2` (applied by reviewer): The note quoted a sentence that is not on the page ('his later withdrawal from Tarsus came in autumn 883'), said the page does not name who took Tarsus, and gave abbasid-caliphate as counterpart. Evidence: Ahmad ibn Tulun page: the new governor 'Yazaman al-Khadim, with popular backing, refused to acknowledge Tulunid rule'; 'His attempt in autumn 883 to bring Tarsus to heel failed'. The Abbasid dossier has no gain of Tarsus. Confidence 2. Fix: Note re-quoted and counterpart set to 'Yazaman al-Khadim (governor of Tarsus)' (done).
- `/identity/rulers`: The ruler list jumps from 896 to 904: Jaysh and Harun ibn Khumarawayh are missing. Ahmad's 868 start is also before the state's start in 873. Evidence: Ahmad ibn Tulun page: Jaysh 'was deposed after only a few months and replaced by his brother Harun ibn Khumarawayh'. Tulunids infobox: 'Established: 868'. Fix: Add Jaysh (896) and Harun (896-904), taking the years from their pages. Then either start the state in 868 or start Ahmad's reign in 873.
- `/ledger/0`: The Tulunid ledger has no vassal events, though the Abbasid dossier records the Tulunids as its vassal. Evidence: abbasid-caliphate /ledger/34 (873) and /ledger/37 (878) vassal_start tulunids; /ledger/53-54 vassal_end 905. Tulunids page: 'the caliph's recognition of their rights in Egypt and the Levant'. Fix: Add vassal_start abbasid-caliphate 873 (Egypt) and 878 (Syria), and vassal_end 905 (c2).
- `/keyframe_review/2`: The 898 correction removes only Aleppo with a 100 km radius. 'The capitals' given up in 898 is most likely al-'Awasim, the northern Syrian frontier district. Evidence: Tulunids page: Ahmad 'successfully captured Qinnasrin and the al-'Awasim district'; the treaty of 285 AH (898) made them 'relinquish control over Aleppo, Qinnasrin, and the capitals' (al-'awasim means 'the capitals'). Fix: Remove Qinnasrin, al-'Awasim and the Cilician Thughur in the correction and in /ledger/3; keep the quote.
- `/ledger/2`: Tarsus is lost in 883 but never regained, although the Tulunids held it again by 890. Evidence: Tulunids page: 'as far north as Tarsus by 890', and 'In 284 AH (897 CE), while Ahmad ibn Tughjan, the Tulunid governor of the frontier regions'. Fix: Add a gain of Tarsus around 890 (c2), and include the frontier in the 898 loss.

Thin:
- `/wars/1`: the Qarmatian invasion year and the Makuria and Aghlabid edges (try https://en.wikipedia.org/wiki/Khumarawayh)
- `/identity/rulers`: reign years of Jaysh and Harun (try https://en.wikipedia.org/wiki/Harun_ibn_Khumarawayh)

Spot checks:
- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Tulunids) - 'This year is regarded as the foundation year' (259 AH/873); the infobox says 868
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Ahmad_ibn_Tulun) - 'in 877/8 ... the entirety of Syria and the Cilician frontier'; June comes from the Tulunids page
- `/ledger/2`: not on page (https://en.wikipedia.org/wiki/Ahmad_ibn_Tulun) - the quoted sentence is absent; the substance (autumn 883 failure at Tarsus) is on the page; c2, fixed
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Tulunids)
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Tulunids)

## ziyadid-dynasty: thin

Area: infobox None km2 (None), Cliopatria 215447, ratio None. No area in the infobox (confirmed); the all-Yemen Cliopatria polygon is cut to Tihama plus Aden and noted.

Findings:
- `/ledger/0`: The ledger has no allegiance to the Abbasids. The notes say the Cliopatria relation is 'not on any page opened', but the Ziyadid page states it. Evidence: Ziyadid page: the Ziyadids expanded 'all the while recognizing Abbasid overlordship', and after 866 Ibrahim 'continued reciting the khutba in the name of the Abbasids'. abbasid-caliphate /ledger/28 (866 vassal_start, c1) and /ledger/67 (946 vassal_end, c1). Fix: Add vassal_start abbasid-caliphate 819 (c2) and an undated vassal_end (c1). Correct the note in /notes and _notes/me-08-b.md. The Abbasid side should re-date its start to 819.
- `/keyframe_review/1`: The land grows from Tihama (819-865) to Tihama plus Aden (866) with no event to explain it. Evidence: Ziyadid page: Umara's undated list 'Hadramawt, Diyar Kindah, Shihr, Mirbat in Oman, Abyan, Lahij, Aden and the maritime provinces as far north as Hali'. Fix: Add a gain of Aden and the southern coast (c1, bridged to 866), or keep Aden out of /keyframe_review/1.
- `/ledger/1`: The Yu'firid deference (847-989) has no mirror in the yufirid-dynasty dossier. Evidence: yufirid-dynasty has no vassal event with ziyadid-dynasty. Ziyadid page: the Yufirids 'forced the Ziyadid ruler to tolerate their rule in exchange for mentioning him on coins and in the Friday prayer'. Fix: Route to the Yufirid author. Here, keep c2 and note that the deference was nominal.

Thin:
- `/keyframe_review/1`: when the Ziyadids held Aden, Hadramawt and Hali (undated on the page) (try https://en.wikipedia.org/wiki/Abu_al-Jaysh_Ishaq_ibn_Ibrahim)
- `/ledger/2`: the end of the Yu'firid deference; c1 (try https://en.wikipedia.org/wiki/Yufirids)
- `/ledger/3`: 1018-1021 under Nafis (try https://en.wikipedia.org/wiki/Najahid_dynasty)

Spot checks:
- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Ziyadid_dynasty)
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Ziyadid_dynasty)
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Ziyadid_dynasty) - attack of 989 confirmed; the end of the vassal tie is bridged (c1)
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Ziyadid_dynasty)

## Cross-dossier matrix

- samanid-empire 893 gain / kara-khanids: matched (mirror kara-khanids 893 loss). after the reviewer changed the counterpart from 'Karluks'
- samanid-empire 900 gain / saffarid-dynasty: matched (mirror saffarid-dynasty 900 loss). Khorasan; abbasid-caliphate /ledger/48 also gains Khorasan from the Saffarids in 900 (double count on the Abbasid side, route me-08)
- samanid-empire 900 gain / zaydi-alid-dynasties: matched (mirror zaydi-alid-dynasties 900 loss). Tabaristan and Gurgan
- samanid-empire 901 gain / saffarid-dynasty: matched (mirror saffarid-dynasty 901 loss). Ray
- samanid-empire 911 gain / saffarid-dynasty: matched (mirror saffarid-dynasty 911 loss). Sistan
- samanid-empire 914 loss / zaydi-alid-dynasties: matched (mirror zaydi-alid-dynasties 914 gain). Tabaristan and Gurgan
- samanid-empire 917 loss / sajid-dynasty: matched (mirror sajid-dynasty 917 gain). Zanjan, Qazvin, Ray
- samanid-empire 922 loss / saffarid-dynasty: matched (mirror saffarid-dynasty 922 gain). Sistan
- samanid-empire 922 vassal_start / saffarid-dynasty: missing. the Saffarid ledger has no vassal_start; also the 999 vassal_end
- samanid-empire 924 loss / sajid-dynasty: matched (mirror sajid-dynasty 924 gain). both sides count Ray twice (917 and 924) with no loss in between
- samanid-empire 928 gain / zaydi-alid-dynasties: matched (mirror zaydi-alid-dynasties 928 loss). Tabaristan and Ray
- samanid-empire 930 loss / Makan ibn Kaki: exception. listed in counterparts_needing_dossiers (no makan-ibn-kaki dossier, although me-08-x has run)
- samanid-empire 932 loss / ziyarid-dynasty: mismatch (mirror ziyarid-dynasty 932 gain). ziyarid /ledger/3 names zaydi-alid-dynasties (ended 928) as counterpart; the Nasr II page has Mardavij take Tabaristan from Makan
- samanid-empire 933 gain / ziyarid-dynasty: matched (mirror ziyarid-dynasty 933 loss). Gurgan; but the Samanids already held Gurgan from 931
- samanid-empire 933 vassal_start / ziyarid-dynasty: missing. the Ziyarid ledger has no vassal_start with samanid-empire (nor the 979 vassal_end); route to me-08
- samanid-empire 935 gain / ziyarid-dynasty: mismatch (mirror ziyarid-dynasty 935 gain). both dossiers gain Gorgan from each other in 935
- samanid-empire 962 loss / ghaznavid-empire: mismatch (mirror ghaznavid-empire 962 found). the Ghaznavids founded from lawik-dynasty; the page says Ghazna was Lawik land
- samanid-empire 992 contest_start / kara-khanids: mismatch (mirror kara-khanids 990 contest_start). two years apart
- samanid-empire 999 loss / kara-khanids: matched (mirror kara-khanids 999 gain). Transoxiana
- samanid-empire 999 loss / ghaznavid-empire: matched (mirror ghaznavid-empire 999 gain). Khorasan
- ghaznavid-empire 998 gain / samanid-empire: missing. no Samanid loss in 998 (Balkh, Herat)
- abbasid-caliphate 819 vassal_start / samanid-empire: missing. the Samanid ledger has no vassal events with abbasid-caliphate (819, 900, 999) or tahirid-dynasty (821, 873)
- saffarid-dynasty 861 found / tahirid-dynasty: matched (mirror tahirid-dynasty 861 loss). Sistan
- saffarid-dynasty 864 gain / Salih (ruler of Bost): exception. local ruler with no dossier and not listed; set to nobody or list
- saffarid-dynasty 865 gain / zunbils: matched (mirror zunbils 866 loss). one year apart
- saffarid-dynasty 870 gain / turk-shahis: matched (mirror turk-shahis 870 loss). Kabul
- saffarid-dynasty 870 gain / tahirid-dynasty: matched (mirror tahirid-dynasty 870 loss). Herat; abbasid-caliphate /ledger/30 also records the loss (double count, route me-08)
- saffarid-dynasty 871 gain / hindu-shahis: missing. counterpart corrected from turk-shahis; hindu-shahis has no 871 loss of Bamiyan (route sa-03)
- saffarid-dynasty 873 gain / tahirid-dynasty: matched (mirror tahirid-dynasty 873 loss). Khorasan
- saffarid-dynasty 875 gain / abbasid-caliphate: matched (mirror abbasid-caliphate 875 loss). Fars
- hindu-shahis 878 gain / saffarid-dynasty: missing. the Saffarid ledger has no 878 loss of Kabulistan
- abbasid-caliphate 886 loss / saffarid-dynasty: missing. Cliopatria bridging (c1) on the Abbasid side; no Saffarid gain
- saffarid-dynasty 897 gain / abbasid-caliphate: matched (mirror abbasid-caliphate 898 loss). Ray (Amr page 897); the Abbasid side is a c1 Cliopatria bridge with different land
- saffarid-dynasty 910 loss / abbasid-caliphate: missing. no 910 Abbasid gain of Fars (route me-08)
- saffarid-dynasty 1002 loss / ghaznavid-empire: matched (mirror ghaznavid-empire 1002 gain). Sistan
- zaydi-alid-dynasties 864 found / tahirid-dynasty: matched (mirror tahirid-dynasty 864 loss). Tabaristan; abbasid-caliphate /ledger/27 also records the loss
- zaydi-alid-dynasties 865 loss / tahirid-dynasty: mismatch (mirror tahirid-dynasty 865 contest_end). the Tahirid side records only a contest in 864-865; the Zaydi regain is now 865 (reviewer fix)
- zaydi-alid-dynasties 867 gain / tahirid-dynasty: missing. no Tahirid loss of Gurgan in 867
- zaydi-alid-dynasties 874 contest_start / saffarid-dynasty: matched (mirror saffarid-dynasty 874 contest_start). Tabaristan
- zaydi-alid-dynasties 877 loss / abbasid-caliphate: missing. no Abbasid gain of Gurgan in 877; the page calls Ishaq al-Sari a Tahirid general
- zaydi-alid-dynasties 889 loss / Rafi' ibn Harthama: exception. listed in counterparts_needing_dossiers
- zaydi-alid-dynasties 914 gain / samanid-empire: mismatch. Rey: the Samanid dossier keeps Ray to 917 and loses it to the Sajids
- sajid-dynasty 889 found / abbasid-caliphate: mismatch (mirror abbasid-caliphate 898 loss). the Abbasid side is a c1 Cliopatria bridge at 898; it should be re-dated to 889 (route me-08)
- sajid-dynasty 909 gain / bagratid-armenia: exception. eu-19 has not run (no bagratid-armenia dossier)
- sajid-dynasty 909 vassal_start / shirvan: exception. eu-19 has not run (no shirvan dossier); also the 919 vassal_end
- sajid-dynasty 909 vassal_start / kingdom-of-vaspurakan: exception. eu-19 has not run; also the 929 vassal_end
- sajid-dynasty 929 dissolve / sallarid-dynasty: mismatch (mirror sallarid-dynasty 941 gain). 12-year gap; sallarid /ledger/1 names sajid-dynasty, a state gone since 929
- tulunids 873 found / abbasid-caliphate: mismatch (mirror abbasid-caliphate 873 vassal_start). the Abbasid side records a vassal tie; the Tulunid ledger lacks the vassal_start (also 878 and the 905 vassal_end)
- tulunids 878 gain / abbasid-caliphate: mismatch (mirror abbasid-caliphate 878 vassal_start). Syria: the Abbasid side records a vassal tie, not a loss
- tulunids 883 loss / Yazaman al-Khadim (governor of Tarsus): exception. counterpart corrected from abbasid-caliphate; local governor
- tulunids 898 loss / abbasid-caliphate: matched (mirror abbasid-caliphate 898 gain). Aleppo and Qinnasrin
- tulunids 905 loss / abbasid-caliphate: matched (mirror abbasid-caliphate 905 gain). Egypt and Syria
- ziyadid-dynasty 819 found / abbasid-caliphate: mismatch (mirror abbasid-caliphate 866 vassal_start). the Ziyadid ledger lacks a vassal_start; the Abbasid side dates it 866 (c1); the page supports allegiance from the start
- ziyadid-dynasty 847 vassal_start / yufirid-dynasty: missing. the Yufirid dossier has no vassal event (also the 989 vassal_end)
- ziyadid-dynasty 1018 dissolve / najahid-dynasty: exception (mirror najahid-dynasty 1022 found). the Nafis interregnum 1018-1021, explained on both sides

## Problems

- All six dossiers validate with --resolve (0 errors, 0 warnings), before and after the reviewer's edits. validate.json is in /tmp/claude-0/work/me-08-b/.
- The reviewer made 8 small verified edits in 5 dossiers (samanid-empire /ledger/2 counterpart; saffarid-dynasty /ledger/6 counterpart and note, /ledger/21 and /keyframe_review/15 quote; zaydi-alid-dynasties /ledger/2 year, confidence and note; sajid-dynasty /ledger/1 source and note; tulunids /ledger/2 counterpart and note), as the orchestrator's adjustment allows (the base reviewer brief says reviewers do not edit). All re-validated and read back.
- 13 WebFetch calls; none failed. Extracts come from a small model; quotes are as returned.
- Routed to other groups: abbasid-caliphate (me-08) double-counts Herat 870, Khorasan 873 and Tabaristan 864 with the Tahirid dossier; gains Khorasan from the Saffarids in 900 alongside the Samanids; dates the Sajid 889 start as an 898 loss and the Ziyadid allegiance from 866; has no gain of Fars in 910. ziyarid-dynasty names zaydi-alid-dynasties as its 932 counterpart and has no vassal ties to the Samanids. sallarid-dynasty takes Azerbaijan from sajid-dynasty in 941. yufirid-dynasty has no Ziyadid tie. hindu-shahis has no 871 Bamiyan loss. kara-khanids starts the 990 contest two years early.
- me-08-x has a review file, so it has run, but rafi-ibn-harthama, makan-ibn-kaki, banu-ilyas and justanid-dynasty do not exist; they stay as listed exceptions.
