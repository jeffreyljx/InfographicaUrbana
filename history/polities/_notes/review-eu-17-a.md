# Review of batch eu-17-a (russian-empire)

Reviewer: adversarial review, 2026-10-31. Dossier: history/polities/russian-empire.json (113 events, 71 keyframes, 20 wars, 14 sources). Validator: valid, 0 errors; warnings: five unpaired vassal/occupation starts (Bukhara, Khiva, Uryankhay to 1917; Iran 1915, Turkey 1916) and Yedisan unknown to the gazetteer.

## Verdict: fail

Nothing fabricated: ten spot checks (TE, RE, CA, AM) confirmed the quoted rows and dates. Area sanity passes (1895: 22.8 M km2 infobox vs 22.34 M Cliopatria, ratio 0.98; 1725 0.96; 1906 0.99). The dossier fails because events stated on pages the author already opened, and mirrored at confidence 2-3 in existing neighbour dossiers, are missing (Azov 1739, the Kalmyk Khanate 1771, the Kokand conquests 1859-1864 behind the unexplained 0.92 M km2 jump of the 1864 keyframe, Ganja/Shaki/Shirvan 1804-1805, Tabriz 1827, the Kurils 1875), and because the 1813 Duchy of Warsaw event is a gain where its page says occupation. Most of the work is additive and uses pages already in sources[].

## Fixes

- **/ledger/9/counterpart** (applied by reviewer): 1735 loss of Baku, Shirvan and Derbent named afsharid-iran as counterpart, a state whose dossier starts in January 1736. Evidence: afsharid-iran.json identity.start 1736-01; safavid-dynasty.json (to March 1736) records this as /ledger/71 '1735 gain russian-empire'. The note itself says RE does not name the Persian side. Fix: counterpart safavid-dynasty (done, note extended, dossier re-validated).
- **/ledger (new event, 1739)**: Missing gain of Azov from the Ottoman Empire in 1739, on a page the author opened. Evidence: TE table row: '1739 | Anna of Russia | Regain of Azov | Ottoman Empire | Russo-Turkish War (1735-1739)'. ottoman-empire.json /ledger/146: 1739 loss russian-empire c3 ('Ottomans cede the demilitarized Azov to Russia, as well as the Zaporozhye region'). Fix: Add {year 1739, type gain, counterpart ottoman-empire, region {place Azov, km 60}, source TE, confidence 3}; add the war 'Russo-Turkish War (1735-1739)' to wars[]; in /ledger/18 (1774) say Azov was already Russian (or keep it only as the Cliopatria shape date) so the land is not gained twice.
- **/ledger (new event, 1771)**: Missing annexation of the Kalmyk Khanate in 1771, on a page the author opened. Evidence: TE row: '1771 | Catherine the Great | Kalmyk Khanate | Kalmyk Khanate | exodus of the Kalmyks to Dzungaria'. kalmyk-khanate.json /ledger/6: October 1771 dissolve, counterpart russian-empire, c3. Fix: Add {year 1771, month 10, type gain, counterpart kalmyk-khanate, region {cliopatria 'Kalmyk Khanate', year 1771}, source TE, confidence 3}, and say in the 1772 keyframe note whether the Volga steppe is already inside the 1769/1772 shapes.
- **/ledger (new events 1859-1864) and /keyframe_review/48**: The 1863 to 1864 keyframe change (22.04 to 22.96 M km2, about 3,090 cells in Kazakhstan, Uzbekistan, Kyrgyzstan) has no ledger event, although the opened CA page dates the steps. Evidence: CA: 'in 1862, Russia took Tokmak' (and Pishpek), 'In 1864, Chernayev ... captured Aulie-Ata', 'In June 1864 Veryovkin took Hazrat-i-Turkestan from Kokand', Chimkent taken in 1864. khanate-of-kokand.json /ledger/15-19 records losses to russian-empire in 1859, 1861-09, 1862, 1864 and 1864-06 with no mirror here. Fix: Add gains from khanate-of-kokand: 1862 (Bishkek/Tokmak radius), 1864 (Taraz@80), 1864-06 (Turkistan@60), 1864 (Shymkent@60), and 1859/1861 (Syr Darya forts, Qyzylorda radius) from the CA page, matching the Kokand dossier's regions.
- **/keyframe_review/48**: Verdict 'ok' on the 1864-1867 shape although its own note says it holds Tashkent and Samarkand, which the ledger gains in 1865-06 (/ledger/78) and 1868-05 (/ledger/81), and Bukhara's Jizzakh land (1866). Evidence: Note: 'the shape (which already holds Tashkent, 49 of 49 cells, and most of Samarkand, 47 of 53) runs one to four years ahead of the page'. Brief section 2.4: a keyframe and its ledger must agree. Fix: verdict adjust; correction {minus: [{cliopatria Russian Empire 1864}, {union: [Tashkent@60, Samarkand@80, Jizzakh admin1, Istaravshan@60, Khujand@60]}]} with text; the 1865, 1866 and 1868 gains then add them back.
- **/ledger/50**: 1813 Duchy of Warsaw recorded as a gain at confidence 3, but the cited page says occupation. Evidence: TE row: '1813 | Alexander I of Russia | Duchy of Warsaw (Under occupation) | France | Napoleonic Wars'; the note itself says 'Russia occupies the Duchy of Warsaw'. With /ledger/55 the same land is gained twice (1813 and 1815). Fix: type occupation_start (counterpart duchy-of-warsaw); add an occupation_end 1815 for the same region just before /ledger/55; /ledger/55 stays the 1815 gain of Congress Poland.
- **/ledger (new events 1804-1805, 1827-1828)**: Missing gains and an occupation on the Persian front that the qajar-dynasty dossier records at confidence 2-3. Evidence: qajar-dynasty.json /ledger/13 '1804-01 loss russian-empire: Ganja falls to Russia on 15 January' (c3), /ledger/14 1805-05 Karabakh and Shaki (c2), /ledger/15 1805-12 Shirvan (c2), /ledger/20 '1827-10 occupation_start: Tabriz surrendered ... 24 October 1827' (c3) with end 1828. The Russo-Persian War (1804-1813) page (S5) was opened. The 1805 keyframe note counts Dagestan +123 and Azerbaijan +60 cells that only the Karabakh vassal event covers. Fix: Add gain 1804-01 Ganja@60 (S5), gain 1805-05 Sheki@50 and 1805-12 Shirvan (counterpart qajar-dynasty, or the khanates if they get dossiers), and occupation_start 1827-10 / occupation_end 1828-02 for Tabriz and Ardabil with a war entry for 1826-1828 zones.
- **/ledger (new event, 1875)**: Missing loss of the Kuril Islands to Japan under the 1875 Treaty of Saint Petersburg, the other half of the Sakhalin exchange in /ledger/87. Evidence: empire-of-japan.json /ledger/15: 1877 gain russian-empire, 'The entire Kuril archipelago Japanese territory' (treaty 'signed on 7 May 1875'). No loss on this side; the 1875 Sakhalin gain also disagrees with Japan's /ledger/14 contest_end dated 1877. Fix: Add {year 1875, month 5, type loss, counterpart empire-of-japan, region {region 'Kuril Islands'} minus the southern islands already Japanese}, citing https://en.wikipedia.org/wiki/Treaty_of_Saint_Petersburg_(1875); agree the year (1875 signature vs 1877 effect) with jk-01.
- **/ledger/89/counterpart**: 1878 regain of Southern Bessarabia from ottoman-empire contradicts the dossier's own /ledger/71, which gives the same land to Moldavia in 1856. Evidence: TE row does say '1878 | Regain of Southern Bessarabia | Ottoman Empire', but ottoman-empire.json /ledger/199 (1878-07) lists only Kars, Ardahan and Batum; southern Bessarabia was Moldavian/Romanian from 1856 to 1878. Fix: counterpart united-principalities-of-moldavia-and-wallachia (Romania), month 7, confidence 2, citing https://en.wikipedia.org/wiki/Treaty_of_Berlin_(1878) or https://en.wikipedia.org/wiki/Southern_Bessarabia.
- **/ledger/79/region**: 1866 gain from Bukhara drawn as all of Russian Uzbekistan in 1868, which includes Tashkent (gained from Kokand 1865) and Samarkand (gained 1868-05). Evidence: emirate-of-bukhara.json /ledger/6 (1866 loss russian-empire, c3) names 'Ura-Tepe and Jizzakh': region union(Jizzakh admin1, Istaravshan@60). Brief 2.8: regions specific enough to draw. Fix: region {union: [{admin1 Jizzakh, country Uzbekistan}, {place Istaravshan, km 60}]}; add the 1866 gain of Khujand from khanate-of-kokand (Kokand /ledger/22).
- **/ledger/93**: 1885 Panjdeh gain drawn as the whole of Mary Province, which also holds Merv (gained 1884-03, /ledger/92); month missing. Evidence: CA names only 'the Afghan fort of Panjdeh'; emirate-of-afghanistan.json /ledger/16 dates the loss to 1885-03 (c3). Fix: region a radius around Panjdeh (Tagtabazar, about 40 km), month 3; Panjdeh may need a gazetteer place.
- **/ledger/12/counterpart and /ledger/10/counterpart**: Shape-bridge gains from 'nobody' where neighbour dossiers record the same land as their loss to the Russian Empire. Evidence: zaporozhian-cossacks.json /ledger/9: 1752 loss russian-empire (New Serbia, 'on the land of the Zaporizhian Sich'), matching the 92 Ukrainian cells of /ledger/12; kazakh-khanate.json /ledger/32: 1738 loss russian-empire (Orenburg country, 52-61 E), matching /ledger/10. Fix: Split /ledger/12 into a Ukrainian part (counterpart zaporozhian-cossacks) and a steppe part; set /ledger/10's steppe part to kazakh-khanate.
- **/ledger/68, /ledger/70**: Occupation of the Danubian principalities dated 1849 to 1856 as one span (c1), against the Wallachia dossier's two dated occupations. Evidence: principality-of-wallachia.json /ledger/29-34: occupation_start 1848-09 (c3), end 1851-04 (c3); start 1853-07 (c3), end 1854 (c3). Fix: Re-date to 1848-09..1851-04 and 1853-07..1854 (two pairs), confidence 2-3 from the pages the Wallachia dossier cites; the 1849 keyframe stays adjust for the cells to 1855.
- **/wars**: Wars in the opened sources are missing: Russo-Turkish War (1735-1739), Russo-Turkish War (1828-1829); the World War I entry lacks the Caucasus and Persian fronts. Evidence: TE gives both Russo-Turkish wars as the background of its 1739 and 1829 rows; /ledger/61 (1829 gain) has no war; /ledger/107 (Iran 1915) and /ledger/111 (Turkey 1916) fall in no war zone; ottoman-empire.json /ledger/219 has contest_start 1914-11 with russian-empire. Fix: Add the two wars with zones (Azov; Danube Delta, Anapa, Poti, Akhaltsikhe), and either add ottoman-empire and qajar-dynasty to the World War I belligerents with zones (eastern Anatolia, northern Iran) or add a Caucasus campaign war.

## Thin (confidence-1 gaps for a gap-filler)

- /ledger/13: Start of the occupation of East Prussia: dated 1762 from the shape; kingdom-of-prussia.json has the contest from 1757-08 and cites the Russian advance through East Prussia in 1758. Page to try: https://en.wikipedia.org/wiki/East_Prussia
- /ledger/8, /ledger/10, /ledger/12: 1734, 1738 and 1752 steppe and Siberian frontier steps (shape bridges, c1). Page to try: https://en.wikipedia.org/wiki/Orenburg
- /ledger/15: Sloboda Ukraine: gained 1769 from the shape, but sloboda-ukraine.json ends 1765-07 (dissolve without counterpart) and the land was already the tsar's. Page to try: https://en.wikipedia.org/wiki/Sloboda_Ukraine
- /ledger/21: Destruction of the Zaporozhian Sich (zaporozhian-cossacks.json dissolve 1775-08). Page to try: https://en.wikipedia.org/wiki/Zaporozhian_Sich
- /ledger/22: Chukotka coast 1778 (shape only). Page to try: https://en.wikipedia.org/wiki/Chukchi_people
- /ledger/25, /ledger/26: 1791-1792 occupation of Moldavia and Wallachia (shape only): principality-of-wallachia.json has no Russian occupation in these years; check which principality Russia held and from when. Page to try: https://en.wikipedia.org/wiki/Russo-Turkish_War_(1787%E2%80%931792)
- /ledger/35, /ledger/36: 1796 Persian expedition (no qajar-dynasty mirror). Page to try: https://en.wikipedia.org/wiki/Persian_expedition_of_1796
- /ledger/47, /ledger/51: 1812 French invasion and 1813 recovery of Lithuania and Belarus. Page to try: https://en.wikipedia.org/wiki/French_invasion_of_Russia
- /ledger/60, /ledger/64: 1828-1834 occupation of the principalities (Wallachia dossier: 1828 to 1834-04). Page to try: https://en.wikipedia.org/wiki/Russo-Turkish_War_(1828%E2%80%931829)
- /ledger/62, /ledger/63: November Uprising 1830-1831 (Cliopatria 'Poles' 1830-1833). Page to try: https://en.wikipedia.org/wiki/November_Uprising
- /ledger/68, /ledger/70: 1848-1851 and 1853-1854 occupations (see fixes). Page to try: https://en.wikipedia.org/wiki/Crimean_War
- /ledger/83: Novaya Zemlya 1870. Page to try: https://en.wikipedia.org/wiki/Novaya_Zemlya
- /ledger/84, /ledger/94: Ili occupation 1871 to 1881 (qing-dynasty.json /ledger/73: returned under the 1881 Treaty of Saint Petersburg, c3; this dossier ends it in 1885 at c1). Page to try: https://en.wikipedia.org/wiki/Ili_crisis
- /ledger/96: Second 1895 cell change (shape only). Page to try: https://en.wikipedia.org/wiki/Great_Game
- /ledger/98: Occupation of Manchuria 1900 (qing-dynasty.json has 1900-06 at c3). Page to try: https://en.wikipedia.org/wiki/Russian_invasion_of_Manchuria
- /ledger/102: Severnaya Zemlya 1913. Page to try: https://en.wikipedia.org/wiki/Severnaya_Zemlya
- /ledger/107: Russian occupation of northern Iran: qajar-dynasty.json has Tabriz 1909 and Urmia/Khoy 1910 (c3) and 1915-11 (c2) with ends 1917; this dossier has only 1915 at c1. Page to try: https://en.wikipedia.org/wiki/Persian_campaign_(World_War_I)
- /ledger/111: Occupation of eastern Anatolia 1916 (ottoman-empire.json /ledger/221 c3 'captured Western Armenia in 1916'). Page to try: https://en.wikipedia.org/wiki/Caucasus_campaign
- /identity/rulers: Ruler strip omitted (author flagged). Page to try: https://en.wikipedia.org/wiki/List_of_Russian_monarchs

## Spot checks

- /ledger/2 (https://en.wikipedia.org/wiki/Territorial_evolution_of_Russia): confirmed: row '1723 | Peter the Great | Derbent, Baku, Shirvan, Gilan, Mazandaran, and Astarabad | Guarded Domains of Iran'
- /ledger/4 (https://en.wikipedia.org/wiki/Russian_conquest_of_Central_Asia): confirmed: 'Tevkelev met with the leaders of the Junior juz on 10 October 1731' (/ledger/5 Middle Juz: emissaries 15 December 1731, oath undated; c2 is honest)
- /ledger/37 (https://en.wikipedia.org/wiki/Territorial_evolution_of_Russia): confirmed: row '1799 | Paul I of Russia | Alaska | Indigenous people | Russian America'
- /ledger/45 (https://en.wikipedia.org/wiki/Russian_Empire): confirmed: 'the signing of the Treaty of Fredrikshamn on 17 September 1809'
- /ledger/50 (https://en.wikipedia.org/wiki/Territorial_evolution_of_Russia): confirmed year, wrong type: row reads 'Duchy of Warsaw (Under occupation) | France', recorded as gain (see fixes)
- /ledger/61 (https://en.wikipedia.org/wiki/Territorial_evolution_of_Russia): confirmed: row '1829 | Danube Delta, Anapa, Novorossiysk, Poti, Akhaltsikhe and Akhalkalaki | Ottoman Empire | Russo-Turkish War (1828-1829)'
- /ledger/72 (https://en.wikipedia.org/wiki/Amur_Annexation): confirmed: Aigun 1858 'ceded all territories north of the Amur to Russia' (page gives the year only)
- /ledger/89 (https://en.wikipedia.org/wiki/Territorial_evolution_of_Russia): confirmed as quoted ('Regain of Southern Bessarabia | Ottoman Empire'); counterpart conflicts with /ledger/71 (see fixes)
- /ledger/92 (https://en.wikipedia.org/wiki/Russian_conquest_of_Central_Asia): confirmed: 'On 16 March 1884, Komarov occupied Merv.'
- /ledger/95 (https://en.wikipedia.org/wiki/Territorial_evolution_of_Russia): confirmed: row '1895 | Alexander III of Russia | East Tajikistan | sparsely populated | Exploration of the Pamir plateau'

## Cross-dossier matrix (non-matched rows)

- russian-empire 1721 gain swedish-empire -> swedish-empire None None: exception. no dossier yet (eu-14 not run)
- russian-empire 1731 vassal_start kazakh-khanate -> kazakh-khanate None None: mismatch. kazakh-khanate has no vassal_start; it records losses to russian-empire 1721, 1738, 1769 (c1) and occupation_start 1822/1824, ends 1847; route to ia-03 to agree the 1731 oaths (CA 10 October 1731)
- russian-empire 1738 gain nobody -> kazakh-khanate 1738 loss: mismatch. kazakh-khanate records the Orenburg country as lost to russian-empire; this dossier says nobody
- ottoman-empire 1739 loss russian-empire -> russian-empire None None: missing. TE row 1739 Regain of Azov; no gain in this dossier
- russian-empire 1743 gain swedish-empire -> swedish-empire None None: exception. no dossier yet (eu-14)
- russian-empire 1752 gain nobody -> zaporozhian-cossacks 1752 loss: mismatch. New Serbia: zaporozhian-cossacks records the loss to russian-empire
- russian-empire 1762 occupation_start kingdom-of-prussia -> kingdom-of-prussia 1757 contest_start: mismatch. Prussia: contest 1757-08 to 1762-05 (two starts); this dossier occupation only in 1762 (c1)
- russian-empire 1769 gain sloboda-ukraine -> sloboda-ukraine 1765 dissolve: mismatch. sloboda-ukraine ends 1765-07 without counterpart; 4 years apart
- russian-empire 1771 gain (absent) kalmyk-khanate -> kalmyk-khanate 1771 dissolve: missing. kalmyk-khanate dissolve 1771-10 counterpart russian-empire; TE row 1771; no event here
- russian-empire 1772 gain polish-lithuanian-commonwealth -> polish-lithuanian-commonwealth None None: exception. no dossier yet (eu-15)
- russian-empire 1774 vassal_start crimean-khanate -> crimean-khanate 1774 loss: mismatch. crimean-khanate has no vassal_start: occupation 1771-07..1772-11 and 1776-11..1783-04, loss of Kerch 1774-07
- russian-empire 1791 occupation_start ottoman-empire -> principality-of-wallachia None None: missing. principality-of-wallachia has no Russian occupation in 1791; c1 here
- russian-empire 1793 gain polish-lithuanian-commonwealth -> polish-lithuanian-commonwealth None None: exception. no dossier yet (eu-15)
- russian-empire 1795 gain polish-lithuanian-commonwealth -> polish-lithuanian-commonwealth None None: exception. no dossier yet (eu-15)
- russian-empire 1795 gain duchy-of-courland -> duchy-of-courland None None: exception. no dossier yet (eu-14)
- russian-empire 1796 occupation_start qajar-dynasty -> qajar-dynasty None None: missing. qajar-dynasty has no 1796 event; c1 here
- russian-empire 1801 gain kingdom-of-georgia -> kingdom-of-georgia None None: exception. no dossier yet (eu-19)
- qajar-dynasty 1804 loss russian-empire -> russian-empire None None: missing. Ganja 1804-01 c3 in qajar; no gain here
- russian-empire 1805 vassal_start Karabakh Khanate -> qajar-dynasty 1805 loss: exception. Karabakh Khanate has no dossier (listed); qajar records Karabakh and Shaki as loss 1805-05 and Shirvan 1805-12 (Shaki, Shirvan missing here)
- russian-empire 1809 gain austrian-empire -> austrian-empire None None: exception. no dossier yet (eu-20)
- russian-empire 1809 gain swedish-empire -> swedish-empire None None: exception. no dossier yet (eu-14); denmark-norway /ledger/36 has an odd 1809 loss of one Finnmark cell to russian-empire (c1), route to eu-14
- russian-empire 1810 gain kingdom-of-imereti -> kingdom-of-imereti None None: exception. no dossier yet (eu-19)
- russian-empire 1812 loss first-french-empire -> first-french-empire None None: exception. no dossier yet
- russian-empire 1813 gain duchy-of-warsaw -> duchy-of-warsaw None None: exception. no dossier yet; should be occupation_start (see fixes)
- russian-empire 1815 gain duchy-of-warsaw -> duchy-of-warsaw None None: exception. no dossier yet
- russian-empire 1815 loss austrian-empire -> austrian-empire None None: exception. no dossier yet (eu-20)
- qajar-dynasty 1827 occupation_start russian-empire -> russian-empire None None: missing. Tabriz 1827-10 c3; no occupation here
- russian-empire 1830 loss poles -> poles None None: exception. no dossier yet (Cliopatria row Poles 1830-1833)
- russian-empire 1847 gain kazakh-khanate -> kazakh-khanate 1847 occupation_end: mismatch. kazakh records occupation_end and contest_end 1847, no loss; types disagree
- russian-empire 1849 occupation_start ottoman-empire -> principality-of-wallachia 1848 occupation_start: mismatch. Wallachia 1848-09..1851-04 and 1853-07..1854 (c3) vs 1849..1856 here (c1)
- russian-empire 1856 loss principality-of-moldavia -> principality-of-moldavia None None: exception. no dossier yet (eu-18); the Danube Delta part went to the Ottomans and ottoman-empire has no 1856 gain
- russian-empire 1858 gain qing-dynasty -> qing-dynasty 1858 contest_start: mismatch. qing treats the Amur left bank as contested 1858-05..1860-11 (Qing refused to ratify Aigun, per AM); both defensible, agree with ea-08
- russian-empire 1859 gain caucasian-imamate -> caucasian-imamate None None: exception. no dossier yet (eu-19)
- khanate-of-kokand 1859 loss russian-empire -> russian-empire None None: missing. also 1861-09, 1862, 1864, 1864-06, 1866 (Khujand) Kokand losses with no gain here
- russian-empire 1864 gain Circassians -> circassia None None: exception. listed in counterparts_needing_dossiers
- russian-empire 1868 vassal_start emirate-of-bukhara -> emirate-of-bukhara None None: missing. emirate-of-bukhara has contest_end 1868-07 but no vassal_start; route to ia-03
- russian-empire 1885 occupation_end qing-dynasty -> qing-dynasty 1881 occupation_end: mismatch. qing 1881 c3 (Treaty of Saint Petersburg) vs 1885 c1 here
- russian-empire 1873 vassal_start khanate-of-khiva -> khanate-of-khiva None None: missing. khanate-of-khiva has no vassal_start; route to ia-03
- russian-empire 1875 gain empire-of-japan -> empire-of-japan 1877 contest_end: mismatch. japan dates the Sakhalin exchange to 1877 (effect) and has the Kuril gain from russian-empire in 1877; no Kuril loss here
- russian-empire 1878 gain ottoman-empire -> ottoman-empire 1878 loss: mismatch. Budjak: ottoman 1878-07 loss is Kars, Ardahan, Batum only; southern Bessarabia was Romanian
- russian-empire 1898 occupation_start qing-dynasty -> qing-dynasty None None: missing. Kwantung lease 1898-03: qing-dynasty has no event; route to ea-08
- qajar-dynasty 1909 occupation_start russian-empire -> russian-empire None None: missing. Tabriz 1909, Urmia and Khoy 1910 (c3) not in this dossier
- russian-empire 1914 vassal_start republic-of-uryankhay -> republic-of-uryankhay 1914 loss: mismatch. uryankhay records loss (and end) 1914-04; TU says protectorate, so this side is right
- russian-empire 1914 occupation_start austria-hungary -> austria-hungary None None: exception. no dossier yet (eu-20)
- russian-empire 1915 loss german-empire -> german-empire None None: exception. no dossier yet (eu-20)
- russian-empire 1916 occupation_start ottoman-empire -> ottoman-empire 1916 loss: mismatch. ottoman records a loss (c3); types disagree

Matched (within a year): safavid 1723/1732/1735; ottoman 1774, 1792, 1812, 1829, 1878 (Kars); wallachia occupations 1769, 1774, 1806, 1812, 1828, 1834; crimean 1783; zaporozhian 1775; prussia 1762 end, 1807; qajar 1806, 1813, 1828, 1915; kokand 1853, 1865, 1876; bukhara 1866, 1868; khiva 1873; afghanistan 1885; USA 1867; qing 1860, 1871, 1900, 1905; japan 1905.

## Other observations

- Author flagged honestly: 27 confidence-1 shape bridges, the East Prussia page failure, the principalities, rulers omitted, Turkmenistan and Bukhara/Khiva folded into the shape (adjusted). Identity, capitals (RE infobox: Saint Petersburg 1721-1726 and 1732-1917, Moscow 1727-1732), certainty spans 1721-1917 and the 1917 dissolve are sound.
- Gazetteer: Yedisan (region, Southern Bug to Dniester); Panjdeh (place, if the fix above uses it).
