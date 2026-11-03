# Review of batch me-08-d

Reviewer: Phase B adversarial reviewer, 2026-10-20 (brief filled 2026-10-19). Validator: 0 errors for all three; the 17 --resolve warnings are the intentional empty corrections (Hamdanid 1028-1259, Ziyarid exile 980-997). Pages opened with WebFetch: Ziyarid dynasty (twice), Mardavij, Sayf al-Dawla, Nasir al-Dawla (twice), Abu Taghlib, Sa'd al-Dawla of Aleppo, Hamdanid dynasty, Buyid dynasty. Quotes are from WebFetch extracts.

## hamdanid-emirates: fix

Area: infobox None km2 (None), Cliopatria 482214 km2, ratio None; acknowledged True. The Hamdanid dynasty infobox gives no area (checked); every keyframe note says so. Largest real Hamdanid shape 947-959 is 482,214 km2 before the author removes about 120,000 km2 of Iranian and Caucasian cells.

Findings:

- `/ledger/13` (applied by reviewer; not blocking): Confidence 3 on a year the page does not give: the note quoted 'Buyid forces captured Mosul and Nasibin in 958', which is not on the page. Evidence: Nasir al-Dawla page: 'Another round of warfare erupted in 956–958' and 'The Buyids captured Mosul and Nasibin' (no year of its own; 958 is inferred from the round). Fix: Confidence lowered to 2 and the quote corrected in the note (done by the reviewer; validator 0 errors, 0 warnings).
- `/ledger/14` (author to do; not blocking): The whole of Adana province is lost in 962, but the page has only Anazarbus taken in winter 961-962; Cilicia became a Byzantine province only after Tarsus surrendered in 965, and the Hamdanids had only nominal suzerainty there. Evidence: Sayf al-Dawla page: 'They captured Anazarbus in Cilicia' (winter 961-962); 'Tarsus surrendered on 16 August 965' and 'Cilicia became a Byzantine province'. The dossier's own note quotes 'Nominal suzerainty over Byzantine-frontier towns in Cilicia'. Fix: Make the 962 loss {place: Anazarbus, km 40}, and either add a 964-965 loss of the rest of Cilicia or say in the 947/960/962 keyframe notes that Cilicia was nominal and drop it from the corrections; mirror the change with byzantine-empire /ledger/72 (eu-05).
- `/ledger/13` (author to do; not blocking): The contest over Mosul and Nisibis runs 958-974 (16 years of blend), although the page records peace after the 958 capture and separate rounds in 964 and 973-974. Evidence: Nasir al-Dawla page: 'Peace was renewed in exchange for the recommencement of tribute and an additional indemnity'; 'In 964, Nasir al-Dawla tried to renegotiate the terms' and 'Once again Mosul and Nasibin were captured'. Abu Taghlib page: 'the conflict ended in a negotiated settlement in 974'. Fix: Close the 958 contest in 958/959 (peace), add contest_start/contest_end 964-965 and 973-974, each against buyid-dynasty with the same Mosul/Nasibin region.
- `/ledger/25` (author to do; not blocking): The 1002 rename (Lu'lu' takes direct power) keeps Lu'lu' inside this state, while the report asks for a separate dossier emirate-of-lu-lu-of-aleppo for 1002-1016: the two cannot both hold. Evidence: Schema: rename means 'a dynasty changes within the same state; colour and dossier continue'. Report counterparts_needing_dossiers: 'Emirate of Lu'lu' of Aleppo', years [1002, 1016]. Fix: Either drop the rename, dissolve in 1002 (or 1003/1004) with successor emirate-of-lu-lu-of-aleppo and keep the counterparts entry; or keep the rename, run the dossier to the Fatimid take-over (1016/1017) and drop the counterparts entry.
- `/ledger/21` (author to do; not blocking): Mosul 989-990: this dossier has a 989 gain from buyid-dynasty and a 990 loss to the Uqaylids; buyid-dynasty has Mosul lost to the Uqaylids in 989; uqaylid-dynasty founds in 990 from buyid-dynasty. Three dossiers tell three stories. Evidence: Abu Taghlib page: 'The Jazira remained under Buyid control until 989'; the brothers were 'installed as governors' (by the Buyids) to oppose Badh. Hamdanid dynasty page: the lineage 'still ruled in Mosul ... until 990'. Fix: Agree one story with me-08-c (buyid-dynasty /ledger/12) and the uqaylid-dynasty owner: either the brothers held Mosul for the Buyids (drop the 989 gain and the 990 loss here) or in their own right (then buyid-dynasty needs a 989 loss to hamdanid-emirates and uqaylid-dynasty's found counterpart becomes hamdanid-emirates).

Thin (for a gap-filler):

- `/keyframe_review/6`: Aleppo 967/969-977 was held by Qarquya and then Bakjur, not by Sa'd al-Dawla ('forced Qarquya to sign a treaty ... making Aleppo a tributary Byzantine protectorate'; 'Sa'd retook Aleppo in 977', the dossier's own war /wars/5): no event says whose Aleppo was in those years. Page to try: https://en.wikipedia.org/wiki/Qarquya
- `/wars/6`: Year of the Byzantine capture of Homs, Apamea and Shayzar under Basil II before the 1000/1001 treaty. Page to try: https://en.wikipedia.org/wiki/Battle_of_the_Orontes
- `/ledger/23`: Marwanid share of 990 at confidence 1 with an inferred region; marwanids-of-diyar-bakr /ledger/2 has 'Hisn Kayfa and the fortresses retaken from the Hamdanids' in 991 (Batman): align year and land. Page to try: https://en.wikipedia.org/wiki/Marwanids
- `/keyframe_review/7`: Who held Raqqa and Rahba 979-1004 (excluded from Sa'd's grant). Page to try: https://en.wikipedia.org/wiki/Raqqa

Spot checks:

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Hamdanid_dynasty)
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Nasir_al-Dawla)
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Sayf_al-Dawla)
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Sayf_al-Dawla)
- `/ledger/13`: mis-dated (year inferred, quote not on page; confidence lowered to 2) (https://en.wikipedia.org/wiki/Nasir_al-Dawla)
- `/ledger/15`: confirmed (https://en.wikipedia.org/wiki/Sa%27d_al-Dawla_of_Aleppo)
- `/ledger/17`: confirmed (https://en.wikipedia.org/wiki/Abu_Taghlib)
- `/ledger/18`: confirmed (https://en.wikipedia.org/wiki/Buyid_dynasty)
- `/ledger/19`: confirmed (https://en.wikipedia.org/wiki/Sa%27d_al-Dawla_of_Aleppo)
- `/ledger/20`: confirmed (https://en.wikipedia.org/wiki/Abu_Taghlib)
- `/ledger/22`: confirmed (https://en.wikipedia.org/wiki/Hamdanid_dynasty)

## ziyarid-dynasty: fail

Area: infobox None km2 (None), Cliopatria 41018 km2, ratio None; acknowledged True. No area on the Ziyarid or Mardavij page (checked); the dossier says so.

Findings:

- `/ledger/13` (author to do; blocking): Confidence-3 gain of Gorgan and Tabaristan in 947 names the wrong loser: the page takes them from al-Hasan ibn al-Fairuzan, Vushmgir's rebel governor of Sari, not from the Buyids. Evidence: Ziyarid dynasty page: 'Vushmgir fled to Tabaristan, but was faced there with a revolt by his governor of Sari, al-Hasan ibn al-Fairuzan'; 'Returning to Tabaristan, he was defeated there by al-Hasan, who had previously occupied Gorgan'; 'It was only in 947 when he was able to take Gorgan and Tabaristan from al-Hasan with the help of a large Samanid army'; 'While al-Hasan supported the Buyids'. The page calls the Buyid 'Hasan', the Sari governor 'al-Hasan'. Fix: Counterpart 'Hasan ibn al-Fairuzan' (no dossier; listed below), note rewritten; buyid-dynasty then needs no 947 loss.
- `/ledger/12` (author to do; blocking): The 945 contest_start is against buyid-dynasty and its note says 'so the Buyid Hasan held them', which the page does not say. Evidence: Same page: Vushmgir 'captured Gorgan with Samanid support' in 945 from al-Hasan, 'who had previously occupied Gorgan'. Fix: Contest 945-947 against Hasan ibn al-Fairuzan, ending with the 947 gain; keep the Buyid counterattacks (Rukn al-Dawla, 960, 962, 966) as their own contest pair against buyid-dynasty, starting at the first of them (and at 948 if the page's 948 Buyid invasion is confirmed, see below).
- `/keyframe_review/3` (author to do; blocking): The 943-946 keyframe draws Tabaristan (Mazandaran) and Gilan as Ziyarid, while the page has al-Hasan ibn al-Fairuzan holding Tabaristan and Gorgan until 947; the keyframe and the 947 gain of the same land contradict each other, and the 943 capital Gorgan lies in land al-Hasan held. Evidence: Quotes under /ledger/13. Ziyarid keyframe 943 correction is the unchanged Cliopatria 936 shape (85 Mazandaran cells). Fix: Remove Tabaristan from the 943-946 correction (keep only what a page gives Vushmgir in those years, or leave it empty with a note), add a 943/944 loss of Tabaristan to Hasan ibn al-Fairuzan, and say in identity.capitals that Gorgan was not held 943-946.
- `/ledger/1` (author to do; not blocking): Hamadan, Dinavar, Kashan and Isfahan are gained from 'Asfar ibn Shiruya', but the page calls them Abbasid cities; Asfar's own lands (Ray, Qazvin, Zanjan, Abhar, Qom, Karaj), drawn in the 931 keyframe as 'Rey 60 km', have no gain event. Evidence: Mardavij page: Hamadan, Dinavar and Kashan are 'Abbasid cities' and Mardavij 'became ruler of Asfar's former territories, which included Ray, Qazvin, Zanjan, Abhar, Qom and Karaj'. abbasid-caliphate /ledger/59 records the same cities as its 931 loss to ziyarid-dynasty. Fix: Counterpart abbasid-caliphate for /ledger/1; add a 931 gain from 'Asfar ibn Shiruya' with region Ray (Rey) plus Qazvin and Zanjan provinces and the page's list in text.
- `/ledger/4` (author to do; not blocking): Fars is gained from abbasid-caliphate in 934, but the page has Ali ibn Buya in Shiraz acknowledging Mardavij's authority: Fars was Buyid land (buyid-dynasty found 934 Fars; abbasid-caliphate 934 loss of Fars to buyid-dynasty), so it is claimed twice in 934-935. Evidence: Mardavij page: his troops conquered 'as far as Ahvaz' and forced Ali, who 'was now in Shiraz', to acknowledge his authority again; lead: 'By 934, his authority was acknowledged as far as Shiraz and Ahvaz'. Fix: Keep Khuzestan (Ahvaz) as the 934 gain from abbasid-caliphate; drop Fars from /ledger/4, /ledger/5 and /keyframe_review/1 and record it as vassal_start 934 / vassal_end 935 with counterpart buyid-dynasty.
- `/ledger/3` (author to do; not blocking): Gorgan (Golestan) is lost in 933 and again in 936 (/ledger/7) but is never gained and is in no keyframe (the 931 and 934 corrections have no Golestan; Cliopatria's 936 shape has 2 Golestan cells). Evidence: Mardavij page: Mardavij 'agreed to cede Gurgan to the Samanids' (933), so he held it; Ziyarid page: Vushmgir 'wrested Gorgan from Samanid control' (c. 935) before turning it over to Makan in 936. Fix: Add Golestan to the 931-933 keyframe with a 931/932 gain (from Makan ibn Kaki, with Tabaristan) and add a c.935 gain from samanid-empire with Golestan in the 934-935 keyframe; or drop both losses.
- `/keyframe_review/4` (author to do; not blocking): The 947-969 keyframe draws Tabaristan and Gorgan as Ziyarid throughout; the WebFetch extract of the Ziyarid page says the Buyid Hasan took Tabaristan and Gorgan from Vushmgir in 948, and the dossier's own note has Buyid counterattacks 'with brief gains' in 960, 962 and 966. Evidence: Ziyarid dynasty page (extract): 'The Buyid Hasan only takes Tabaristan and Gorgan from Vushmgir in 948, after 947' (the extract's own words, not a verbatim quote; re-check on the page). Fix: Re-read the page; if it holds, add a 948 loss and the recovery to buyid-dynasty (and the matching gain), and make the contest cover the brief Buyid gains.

Thin (for a gap-filler):

- `/keyframe_review/2`: 939-940: Gorgan 'fell after a long siege' and Abu Ali Chaghani defeated Vushmgir 'in battle in Ray', killing Makan: Ray is drawn as Ziyarid 936-942 without these events. Page to try: https://en.wikipedia.org/wiki/Vushmgir
- `/keyframe_review/7`: Extent 998-1090 (capital Amol from 1035; Ghaznavid and Seljuq overlordship); keyframe is the earlier core plus Gorgan by assumption. Page to try: https://en.wikipedia.org/wiki/Qabus
- `/ledger/15`: End of the 958 occupation of Ray at confidence 1 (page says only 'briefly'). Page to try: https://en.wikipedia.org/wiki/Vushmgir

Spot checks:

- `/ledger/1`: not on page (counterpart: the page calls the cities Abbasid, not Asfar's) (https://en.wikipedia.org/wiki/Mardavij)
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Mardavij)
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Mardavij)
- `/ledger/8`: confirmed (https://en.wikipedia.org/wiki/Ziyarid_dynasty)
- `/ledger/10`: confirmed (https://en.wikipedia.org/wiki/Ziyarid_dynasty)
- `/ledger/13`: not on page (year and land confirmed; the loser is al-Hasan ibn al-Fairuzan, not buyid-dynasty) (https://en.wikipedia.org/wiki/Ziyarid_dynasty)
- `/ledger/14`: confirmed (https://en.wikipedia.org/wiki/Ziyarid_dynasty)
- `/ledger/17`: confirmed (https://en.wikipedia.org/wiki/Buyid_dynasty)
- `/ledger/18`: confirmed (https://en.wikipedia.org/wiki/Buyid_dynasty)
- `/ledger/21`: confirmed (https://en.wikipedia.org/wiki/Ziyarid_dynasty)

## abbasid-caliphate-buyid-dynasty: fail

Area: infobox 1600000 km2 (980), Cliopatria 735561 km2, ratio 0.46; acknowledged True. The row has no shape in 980; compared with its last shape (962-969). The author explains the gap by the 967-981 conquests (Kerman, Oman, Jazira, Tabaristan, Gorgan). The Abbasid Caliphate page gives no area.

Findings:

- `/identity/type` (author to do; blocking): A dossier of type umbrella written as a stand-in for a territorial Cliopatria row that the author identifies as the Buyid state's own land 947-969. Evidence: Schema: umbrella is 'an association or empire-wide entity that is not territory of its own ... never coloured as territory'; reviewer brief 2.9: 'umbrella is never a dossier of its own'; research brief: where Cliopatria has two rows for one state, 'write one dossier under the slug of the earlier row, list both Names in cliopatria_names, and review both rows' shapes'. The author's notes: 'The slash row is the Buyid state's land in the 23 years in which Cliopatria's Buyid row has no shape'. buyid-dynasty (row from 936) lists only 'Buyid Dynasty' and copies the shape as a new keyframe buyid-dynasty_947. Fix: Withdraw this dossier. Route to me-08-c: add 'Abbasid Caliphate/Buyid Dynasty' to buyid-dynasty cliopatria_names and review shapes abbasid-caliphate-buyid-dynasty_947, _960 and _962 there in place of the new keyframe buyid-dynasty_947 (same corrections).
- `/ledger/0` (author to do; blocking): All three events (found 947, merge 947, dissolve 969) are Cliopatria row boundaries at confidence 1 that no page supports; the Buyid state was founded in 934 and buyid-dynasty records no merge. Evidence: Buyid dynasty page (checked): established 934; the page never mentions 947 or 969. Author: 'neither page opened dates anything to 947 or 969'. Fix: Drop with the dossier (see /identity/type).
- `/identity/wikipedia` (author to do; not blocking): Wikipedia 'Abbasid Caliphate' and Wikidata Q12536 for an entity the dossier itself says is the Buyid state. Evidence: Author's notes: 'The Wikidata id Q12536 is the Abbasid Caliphate's and looks wrong for both Buyid rows'. Fix: Moot once withdrawn; buyid-dynasty should carry the Buyid Wikidata id rather than Q12536.

Spot checks:

- `/ledger/0`: not on page (as the note says: no event in 947 or 969) (https://en.wikipedia.org/wiki/Buyid_dynasty)
- `/keyframe_review/2`: confirmed (Kerman conquered in 967) (https://en.wikipedia.org/wiki/Buyid_dynasty)
- `/notes`: confirmed (infobox 1,600,000 km2, 980 est.; established 934) (https://en.wikipedia.org/wiki/Buyid_dynasty)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| hamdanid-emirates 929 found (abbasid-caliphate) | abbasid-caliphate 929 vassal_start | matched | Abbasid records the Hamdanids as vassals 929-947 (Mosul and Diyar Bakr). |
| hamdanid-emirates 936 gain (abbasid-caliphate) | none | missing | abbasid-caliphate (me-08-a) has no 936 loss or extension of the vassal region to the whole Jazira; its vassal_start 929 names only Mosul and Diyar Bakr. |
| hamdanid-emirates 942 occupation_start (abbasid-caliphate) | none | missing | Schema: the owner records the same occupation with roles reversed; abbasid-caliphate has no 942 occupation by hamdanid-emirates (Baghdad entered 4 June 942). |
| hamdanid-emirates 943 occupation_end (abbasid-caliphate) | none | missing | As above. |
| hamdanid-emirates 944 gain (ikhshidid-dynasty) | ikhshidid-dynasty 944 loss | matched |  |
| hamdanid-emirates 944 contest_start (ikhshidid-dynasty) | ikhshidid-dynasty 944 contest_start | matched |  |
| hamdanid-emirates 945 gain (ikhshidid-dynasty) | ikhshidid-dynasty 944 loss | matched | Ikhshidid loses Homs and Hamah with Aleppo in 944; this dossier gains them under the October 945 agreement: within a year. |
| hamdanid-emirates 945 contest_end (ikhshidid-dynasty) | ikhshidid-dynasty 945 contest_end | matched |  |
| hamdanid-emirates 946 gain (ikhshidid-dynasty) | ikhshidid-dynasty 946 loss | matched |  |
| hamdanid-emirates 946 contest_start (ikhshidid-dynasty) | ikhshidid-dynasty 946 contest_start | matched |  |
| hamdanid-emirates 947 loss (ikhshidid-dynasty) | ikhshidid-dynasty 947 gain | matched |  |
| hamdanid-emirates 947 contest_end (ikhshidid-dynasty) | ikhshidid-dynasty 947 contest_end | matched |  |
| hamdanid-emirates 958 contest_start (buyid-dynasty) | none | missing | buyid-dynasty (me-08-c) has no Hamdanid contest before 978. |
| hamdanid-emirates 962 loss (byzantine-empire) | byzantine-empire 962 gain | matched | Both draw all of Cilicia in 962; the page gives Anazarbus 961-962 and Cilicia 965 (fix /ledger/14). |
| hamdanid-emirates 969 loss (byzantine-empire) | byzantine-empire 970 gain | matched | Within a year; the Sa'd al-Dawla of Aleppo page gives October 969 for the Byzantine side's confidence-1 event. |
| hamdanid-emirates 974 contest_end (buyid-dynasty) | none | missing | As 958. |
| hamdanid-emirates 978 contest_start (buyid-dynasty) | buyid-dynasty 978 contest_start | matched |  |
| hamdanid-emirates 979 loss (buyid-dynasty) | buyid-dynasty 979 gain | matched |  |
| hamdanid-emirates 979 gain (buyid-dynasty) | none | missing | Diyar Mudar (except Raqqa and Rahba) granted to Sa'd al-Dawla in 979: buyid-dynasty has no matching loss. |
| hamdanid-emirates 979 contest_end (buyid-dynasty) | buyid-dynasty 979 contest_end | matched |  |
| hamdanid-emirates 989 gain (buyid-dynasty) | buyid-dynasty 989 loss | mismatch | buyid-dynasty /ledger/12 loses Mosul to uqaylid-dynasty in 989, not to hamdanid-emirates (fix /ledger/21). |
| hamdanid-emirates 990 loss (uqaylid-dynasty) | uqaylid-dynasty 990 found | mismatch | uqaylid-dynasty /ledger/0 founds in 990 with counterpart buyid-dynasty; it lists hamdanid-emirates only as predecessor. |
| hamdanid-emirates 990 loss (marwanids-of-diyar-bakr) | marwanids-of-diyar-bakr 991 gain | matched | Within a year; land differs (Diyarbakir here, Batman/Hisn Kayfa there). |
| hamdanid-emirates 1004 dissolve (None) | byzantine-empire 1004 vassal_end | exception | Byzantine protectorate ends with the Fatimid turn of Lu'lu'; successor regime of Lu'lu' has no dossier (author's counterparts list). |
| ziyarid-dynasty 931 found (abbasid-caliphate) | abbasid-caliphate 931 loss | matched |  |
| ziyarid-dynasty 931 gain (Asfar ibn Shiruya) | abbasid-caliphate 931 loss | mismatch | abbasid-caliphate /ledger/59 loses the same cities to ziyarid-dynasty; the Mardavij page calls them Abbasid cities (fix /ledger/1). Asfar's own lands have no event; Asfar is in the author's counterparts list. |
| ziyarid-dynasty 932 gain (zaydi-alid-dynasties) | none | exception | zaydi-alid-dynasties is owned by me-08-b, which has not run yet. |
| ziyarid-dynasty 933 loss (samanid-empire) | none | exception | samanid-empire is owned by me-08-b, which has not run yet. |
| ziyarid-dynasty 934 gain (abbasid-caliphate) | abbasid-caliphate 934 loss | mismatch | Khuzestan matched (abbasid /ledger/62); Fars is abbasid's 934 loss to buyid-dynasty and buyid-dynasty's found region (fix /ledger/4). |
| ziyarid-dynasty 935 loss (buyid-dynasty) | buyid-dynasty 935 gain | mismatch | Khuzestan and Isfahan matched (buyid /ledger/1-2); Fars was never Ziyarid; Hamadan/Kermanshah have no Buyid gain in 935 (buyid /ledger/3 takes the Jibal in 943 from 'unnamed rulers'). |
| ziyarid-dynasty 936 loss (Makan ibn Kaki) | none | exception | Makan ibn Kaki is in the author's counterparts_needing_dossiers. |
| ziyarid-dynasty 938 gain (buyid-dynasty) | none | missing | buyid-dynasty has no 938 loss of Isfahan. |
| ziyarid-dynasty 940 loss (buyid-dynasty) | none | missing | buyid-dynasty has no 940 gain of Isfahan. |
| ziyarid-dynasty 943 loss (buyid-dynasty) | buyid-dynasty 943 gain | mismatch | buyid /ledger/3 takes Ray from 'unnamed rulers of the Jibal (page silent)'; the Ziyarid page: 'He then lost it for good in 943, to the Buyid Hasan'. |
| ziyarid-dynasty 945 contest_start (buyid-dynasty) | none | mismatch | Wrong counterpart: the page's opponent in 945-947 is al-Hasan ibn al-Fairuzan (fix /ledger/12). |
| ziyarid-dynasty 947 gain (buyid-dynasty) | none | mismatch | Wrong counterpart: taken from al-Hasan ibn al-Fairuzan (fix /ledger/13); buyid-dynasty correctly has no 947 loss. |
| ziyarid-dynasty 958 occupation_start (buyid-dynasty) | none | missing | buyid-dynasty has no 958 occupation of Ray by ziyarid-dynasty. |
| ziyarid-dynasty 966 contest_end (buyid-dynasty) | none | missing | buyid-dynasty has no contest with the Ziyarids. |
| ziyarid-dynasty 980 loss (buyid-dynasty) | buyid-dynasty 980 gain | matched |  |
| ziyarid-dynasty 981 loss (buyid-dynasty) | buyid-dynasty 981 gain | matched |  |
| ziyarid-dynasty 998 gain (buyid-dynasty) | buyid-dynasty 997 loss | matched | Within a year (the page has 998 in the text, 997 in the table). |
| ziyarid-dynasty 1090 dissolve (None) | none | exception | Successor nizari-ismaili-state has no dossier; in the author's counterparts list. |
| abbasid-caliphate-buyid-dynasty 947 merge (buyid-dynasty) | none | mismatch | buyid-dynasty records no merge; it copies the shape as keyframe buyid-dynasty_947 (fix /identity/type). |

## Counterparts needing dossiers

- Hasan ibn al-Fairuzan (Daylamite lord of Sari, Tabaristan and Gorgan): `hasan-ibn-al-fairuzan` [940, 947]
- Asfar ibn Shiruya: `asfar-ibn-shiruya` [928, 931]
- Makan ibn Kaki: `makan-ibn-kaki` [930, 940]
- Nizari Ismaili State: `nizari-ismaili-state` [1090, 1256]
- Emirate of Lu'lu' of Aleppo: `emirate-of-lu-lu-of-aleppo` [1002, 1016]

## Problems

- WebFetch returns a small model's extract, not raw text: the quotes above are from those extracts; the Ziyarid '948 Buyid conquest' is the extract's own wording and must be re-read on the page before it is written.
- me-08-b (samanid-empire, zaydi-alid-dynasties) has not run: the Ziyarid 932 and 933 events and the overlords' vassal events (Samanid from 936) cannot be checked yet.
- buyid-dynasty (me-08-c) lacks mirrors for eight Hamdanid and Ziyarid events of this batch (958/974 contest, 979 Diyar Mudar, 938/940 Isfahan, 943 Ray counterpart, 958 Ray occupation, 966 contest) and disagrees on Mosul 989: route to me-08-c.
- abbasid-caliphate (me-08-a) lacks the 936 Jazira and the 942-943 Baghdad occupation mirrors: route to me-08-a.
- Reviewer applied one fix in place (hamdanid-emirates /ledger/13 confidence 3 to 2); re-validated 0 errors, 0 warnings; read back after the write.
