#!/usr/bin/env python3
"""Assign every Cliopatria polity to one of the 76 research groups of the master plan.

Reads  data/polities.csv and data/shapes.csv (built by build_tables.py).
Writes data/research-groups.json and data/research-groups.md.

Run:  python3 -I tools/research_groups.py [--check]

Assignment: explicit OVERRIDES first (historical judgment), then region/era RULES
from modern_countries, centroid and first_year. Umbrella/relation entities
(umbrella = 1) go to the group of their main component: the subject of an
"Allegiance/Vassalage of X to Y", the first party of an alliance or personal
union, or the leaf polity of the same name. Context = polities owned by other
groups that are 25 km neighbours (data/polities/<slug>.json) of an owned polity in an
overlapping year inside the group's era.
"""
import csv
import json
import os
import re
import statistics
import sys
import unicodedata
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from slug import slugify  # noqa: E402

POLITIES_CSV = os.path.join(ROOT, "data", "polities.csv")
SHAPES_CSV = os.path.join(ROOT, "data", "shapes.csv")
OUT_JSON = os.path.join(ROOT, "data", "research-groups.json")
OUT_MD = os.path.join(ROOT, "data", "research-groups.md")

# --------------------------------------------------------------------------
# The 76 groups of the master plan (Orchestration section), in plan order.
# (id, region, name, era_from, era_to, scope)
# --------------------------------------------------------------------------
GROUPS = [
    # Europe, Anatolia, Caucasus: 22
    ("eu-01", "Europe", "Bronze Age and Greece", -3400, -323,
     "Researches the Aegean Bronze Age (Minoans, Mycenaeans), the Greek Dark Age and the archaic and classical poleis, leagues and Thracian kingdoms down to Alexander's death, treating Greek City-States as a federation of named cities with their own dossiers where the record allows. Cliopatria lacks the Minoan palaces before 1600 BCE, the Mycenaean palace states as separate polities, the Thracian and Illyrian tribal kingdoms, the Greek colonies of the Black Sea and Magna Graecia as dated foundations, and Sparta, Athens and Thebes as states in their own right; add them."),
    ("eu-02", "Europe", "Hellenistic world", -336, -30,
     "Researches Alexander's empire and the European Hellenistic states: the Antigonids, Epirus, the Aetolian and Achaean leagues, Lysimachus's Thrace, Rhodes and the Illyrian kingdom, down to the Roman settlement of Greece. Cliopatria lacks the Wars of the Diadochi year by year (the satrapies of 323 to 301 BCE), the Greek leagues' changing membership, Sparta under Cleomenes and Nabis, and the Celtic invasion of 279 BCE; add them (the Asian Hellenistic kingdoms belong to me-05)."),
    ("eu-03", "Europe", "Roman Republic", -753, -27,
     "Researches Italy before and under the Republic: the Etruscan cities, the Roman kingdom and Republic, the Samnites, the Latin and Italian allies, Syracuse and the Mamertines, and the Republic's provincial expansion in Gaul, Iberia and the East to Actium. Cliopatria lacks the Italic peoples (Samnites, Lucanians, Umbrians, Veneti), the Gallic and Celtiberian tribal states Rome fought, Syracuse as a state, and the year-by-year provincial conquests; add them."),
    ("eu-04", "Europe", "Roman Empire", -27, 476,
     "Researches the Roman Empire from Augustus to 476: the provincial frontier year by year, the Gallic and Palmyrene breakaways, the client kingdoms, the third-century crisis and the western collapse, with the Germanic tribes of the limes as neighbours. Cliopatria lacks Britannia, Dacia and the Agri Decumates as dated gains and losses, the client kingdoms (Thrace, Bosporus, Mauretania, Judaea) as vassals, the Marcomanni, Alemanni and Picts as named neighbours, and the usurper domains of 260 to 274 and 383 to 388; add them."),
    ("eu-05", "Europe", "Byzantium", 395, 1461,
     "Researches the Eastern Roman and Byzantine Empire from 395 to the fall of Trebizond, its Arab-era condominiums, and the Latin, Nicaean, Epirote and Trapezuntine successor states of 1204, with the Frankish states of Greece. Cliopatria lacks the Exarchates of Ravenna and Carthage, the themes as internal units, the Arab-Byzantine frontier year by year, the Slavic sclaviniae of Greece, and the Venetian and Genoese holdings in the Aegean as dated possessions; add them."),
    ("eu-06", "Europe", "Migration kingdoms", 30, 774,
     "Researches the Germanic and steppe peoples from the Gothic migrations to the fall of the Lombard kingdom: Goths, Vandals, Huns, Burgundians, Suebi, Alans, Ostrogoths, Visigoths, Gepids, Lombards, Avars, Bavarians, Alamanni, Thuringians, Frisians and the Alpine Slavs. Cliopatria lacks the migration routes as dated moves, the Rugii, Heruli, Sciri and Suebi of the Danube, the Slavic settlement of the Balkans, and the Visigothic kingdom's internal civil wars; add them (the Franks belong to eu-07, Anglo-Saxon England to eu-11)."),
    ("eu-07", "Europe", "Franks and Carolingians", 238, 987,
     "Researches the Franks from the Rhine tribes to the end of the Carolingians: the Merovingian kingdoms and their partitions (Austrasia, Neustria, Burgundy, Aquitaine), Charlemagne's empire, the Verdun partition and the East, Middle and West Frankish kingdoms, Brittany and the Burgundies. Cliopatria lacks the Merovingian partitions as separate kingdoms, the Frankish marches (Spanish March, Breton March, Pannonia), the Saxon wars year by year, and the Viking-era fragmentation of West Francia; add them."),
    ("eu-08", "Europe", "Holy Roman Empire to 1250", 911, 1250,
     "Researches the German kingdom and the Holy Roman Empire from Conrad I to the death of Frederick II, with the kingdom of Arles: the stem duchies, the marches, the Welf and Hohenstaufen contests and the Italian expeditions. Cliopatria draws the Empire as one shape until 1260 and lacks its internal states: Saxony, Bavaria, Swabia, Franconia, Lotharingia, Austria, Bohemia's imperial status, the Saxon and Bavarian eastern marches, the prince-bishoprics and the Lombard communes; add them."),
    ("eu-09", "Europe", "German states 1250 to 1806", 1250, 1806,
     "Researches the states of the Empire from the Interregnum to 1806, including the Low Countries, Switzerland and Austria: the electorates, Habsburg, Wittelsbach, Hohenzollern and Wettin lands, Brandenburg-Prussia, the Dutch Republic, the Swiss Confederation and the imperial cities. Cliopatria lumps most of them into 'Holy Roman Empire minor states' and lacks Wurttemberg, Hesse, the Palatinate, Hanover before 1709, the prince-bishoprics, the Swabian and Franconian circles and the Habsburg Netherlands as separate states; add them."),
    ("eu-10", "Europe", "France", 843, 1789,
     "Researches the kingdom of France and its principalities from the Treaty of Verdun to the Revolution: the Capetian domain, Normandy, Brittany, Flanders, Anjou, Aquitaine, Toulouse, Burgundy and the apanages, the Hundred Years' War and the absorption of the great fiefs. Cliopatria lacks the royal domain as distinct from the fiefs, the Plantagenet holdings year by year, the Burgundian state 1363 to 1477 as a whole, Provence, Alsace and Lorraine's transfers, and the Wars of Religion zones; add them."),
    ("eu-11", "Europe", "England, Scotland, Wales, Ireland", 410, 1789,
     "Researches the British Isles from the end of Roman Britain to 1789: the Brythonic kingdoms, the Anglo-Saxon heptarchy, the Danelaw, Alba and Scotland, the Welsh principalities, Norman and Plantagenet England, the Lordship of Ireland, the Union of 1707 and Great Britain with its colonial empire as one entity. Cliopatria lacks the Picts as a state, the Irish provincial kingdoms (Ulaid, Connacht, Munster, Leinster, Meath), the Lordship and Kingdom of Ireland, the Welsh marcher lordships and the Civil War zones; add them."),
    ("eu-12", "Europe", "Iberia and the taifas", 711, 1789,
     "Researches Iberia from the Arab conquest to 1789: the emirate and caliphate of Cordoba, the taifas, Asturias, Leon, Castile, Navarre, Aragon, the Catalan counties, Portugal, Granada, the union of the crowns and Habsburg and Bourbon Spain. Cliopatria lacks the Reconquista frontier year by year, the Almoravid and Almohad periods in Iberia as occupations, the military orders' lands, the Spanish and Portuguese metropoles distinct from their overseas empires, and Gibraltar; add them."),
    ("eu-13", "Europe", "Italy", 568, 1789,
     "Researches Italy from the Lombard invasion to 1789: the Lombard duchies, the Papal States, Venice, Genoa, Pisa, Florence, Milan, Savoy, Naples, Sicily, Sardinia and the smaller states. Cliopatria lacks the Lombard kingdom's partition, the communes of the twelfth and thirteenth centuries, Mantua, Ferrara, Modena, Lucca, Siena and Urbino, the Venetian terraferma and overseas holdings as dated possessions, and the Spanish and Austrian rule of the south as occupations; add them."),
    ("eu-14", "Europe", "Scandinavia and the Baltic", 161, 1789,
     "Researches Scandinavia, Iceland, Greenland and the Baltic coast to 1789: the petty kingdoms, Denmark, Norway, Sweden, the Viking settlements, the Kalmar Union, the crusading orders of Livonia and Prussia, Courland and the Swedish Empire. Cliopatria lacks Finland's tribes and Swedish conquest, the Baltic peoples (Prussians, Livs, Estonians, Curonians) before the orders, the Hanseatic towns, the Danish and Swedish possessions in Germany, and Norse Greenland's end; add them."),
    ("eu-15", "Europe", "Poland, Lithuania, Bohemia, Hungary", 623, 1789,
     "Researches Central Europe to 1789: Samo, Great Moravia, Bohemia, the Magyars and Hungary, the Piast duchies and kingdom of Poland, Lithuania, the Polish-Lithuanian Commonwealth, Transylvania and the partitions. Cliopatria lacks the Polish duchies between 1304 and 1370 as separate states, Croatia and Slavonia under Hungary, royal Hungary versus Ottoman Hungary after 1541 as a divided state, the Bohemian estates' revolt, and the partition zones of 1772, 1793 and 1795 year by year; add them."),
    ("eu-16", "Europe", "Rus and Russia to 1721", 674, 1721,
     "Researches the East Slavs from the Rus to Peter the Great: Kievan Rus, its principalities, Novgorod and Pskov, Volga Bulgaria, the Mongol yoke, Moscow's gathering of the lands, the Tsardom, the Cossack hosts and Ukraine. Cliopatria lacks the principalities between 1240 and 1294, the Lithuanian conquest of the western Rus year by year, the Livonian War zones, the Time of Troubles, the Siberian advance as dated gains, and the Hetmanate's partition along the Dnieper; add them."),
    ("eu-17", "Europe", "Russian Empire and USSR", 1721, 1991,
     "Researches the Russian Empire, the 1917 republics, the Civil War states and the Soviet Union to 1991, with the European fronts of the Civil War and both World Wars. Cliopatria lacks the Civil War governments (the White Siberia, South Russia, the Far Eastern Republic, Soviet Ukraine), the Soviet republics as internal units, the 1939 to 1945 annexations year by year, and the Russian advance in Central Asia and the Caucasus as dated gains; add them."),
    ("eu-18", "Europe", "Balkans and Ottoman Europe", 681, 1912,
     "Researches the Balkans from the First Bulgarian Empire to the Balkan Wars: Bulgaria, Serbia, Croatia, Bosnia, Duklja and Montenegro, Wallachia, Moldavia, Ragusa, the Albanian principalities, Ottoman rule and the nineteenth-century national states. Cliopatria lacks the Ottoman provinces of Europe as internal units, the Habsburg Military Frontier, the Venetian Dalmatia, the Pashalik of Scutari and Ali Pasha's Janina, and the Balkan War gains of 1912 to 1913; add them (the Ottoman state itself belongs to me-10)."),
    ("eu-19", "Europe", "Caucasus", -860, 2026,
     "Researches the Caucasus in every era: Urartu, Colchis, Iberia, Caucasian Albania, Armenia from the Orontids to Bagratid and Cilician-era kingdoms, Lazica, Georgia and its successor kingdoms, Shirvan, the khanates, the Russian conquest, the 1918 republics and the modern states with their frozen conflicts. Cliopatria lacks the Orontid and Artaxiad Armenia before 326 BCE as named polities, the Arab emirates of Tiflis and Derbent, the North Caucasian peoples (Circassia, Alania, the Dagestani khanates), the Russian conquest year by year, and Nagorno-Karabakh, Abkhazia and South Ossetia as contested zones; add them."),
    ("eu-20", "Europe", "Europe 1789 to 1914", 1789, 1914,
     "Researches every European state founded between the French Revolution and 1914 outside the Balkans, Caucasus and Russia: the French republics and empires, the Napoleonic satellites, the German and Italian states and their unifications, the Netherlands and Belgium, Austria, the Nordic unions and the colonial empires as single entities. Cliopatria lacks the Napoleonic campaigns as yearly occupations, the Italian states 1815 to 1860 beyond the largest, the German Confederation's members as states, Schleswig-Holstein, Alsace-Lorraine and Savoy as dated transfers, and the colonial empires' metropoles distinct from their overseas shapes; add them."),
    ("eu-21", "Europe", "Europe 1914 to 1945", 1914, 1945,
     "Researches Europe through both World Wars: the states born in 1918, the interwar republics and dictatorships, the Spanish Civil War, the Axis conquests and occupations, the puppet states and the resistance governments, with fronts by year. Cliopatria lacks the 1914 to 1918 fronts, the Baltic and Polish wars of 1919 to 1921, the Sudetenland, Memel and Danzig transfers, the Axis occupation zones and puppet states (Slovakia, Protectorate, Serbia, Montenegro, Albania) as occupations, and the 1945 lines; add them."),
    ("eu-22", "Europe", "Europe 1945 to 2026", 1945, 2026,
     "Researches Europe from the end of the Second World War to today: the Allied occupation zones, the two Germanies, the socialist states and their 1989 successors, the Yugoslav wars, the Soviet successor states of Europe, the Cyprus partition, the micro-states and the European Union as an association, not a territory. Cliopatria lacks the occupation zones 1945 to 1949, Trieste, the Yugoslav war fronts and the Dayton entities, Transnistria, the Donbas and Crimea after 2014 as contested or occupied land, and the 2022 war fronts year by year; add them."),
    # Middle East and Egypt: 10
    ("me-01", "Middle East", "Sumer to Akkad", -3400, -2000,
     "Researches Mesopotamia and Elam from the first cities to the fall of Ur III: the Sumerian city-states as named cities (Uruk, Ur, Lagash, Kish, Umma), Akkad, the Gutians, Ur III and Elam's early dynasties. Cliopatria lacks the individual Sumerian cities as polities, Ebla and Mari, the Ur III state as its own entry, and Elam's Awan and Simashki dynasties as dated periods; add them."),
    ("me-02", "Middle East", "Babylon and Assyria", -2000, -539,
     "Researches Mesopotamia from Isin-Larsa to Cyrus: Old Babylon, the Sealand, Assyria from the city-state to the Neo-Assyrian Empire including its Egyptian conquest, the Kassites, Mitanni's Assyrian rivalry and the Neo-Babylonian Empire. Cliopatria lacks Isin, Larsa and Eshnunna, the Kassite dynasty as a separate state, the Middle Assyrian frontier year by year, the Aramean states of the Jazira, and the Chaldean tribal lands; add them."),
    ("me-03", "Middle East", "Egypt to the New Kingdom", -3100, -332,
     "Researches Egypt from Narmer to Alexander: the Early Dynastic, Old, Middle and New Kingdoms, the intermediate periods with their rival dynasties, the Hyksos, the Libyan and Kushite dynasties, the Saite restoration and the Persian occupations. Cliopatria lacks the First Intermediate Period as rival Herakleopolis and Thebes, the New Kingdom's Levantine and Nubian frontier year by year, the Twenty-fifth (Kushite) dynasty as rule over Egypt, and the Persian occupations of 525 and 343 BCE as occupations; add them."),
    ("me-04", "Middle East", "Hittites, Levant, Israel", -1700, -539,
     "Researches Anatolia, the Levant and Iron Age Arabia before the Persians: the Hittites and Neo-Hittite states, Mitanni, Phrygia, Lydia, Tabal, Philistia, Phoenicia and its colonies' home cities, Israel and Judah, and the South Arabian kingdoms of Saba, Hadhramaut, Ma'in and Qataban. Cliopatria lacks Arzawa, Kizzuwatna and the other Bronze Age Anatolian kingdoms, Ugarit, Amurru and the Canaanite city-states, the Aramean kingdoms (Damascus, Hamath), Ammon, Moab and Edom, and Cyprus's kingdoms; add them."),
    ("me-05", "Middle East", "Achaemenids and Seleucids", -700, -30,
     "Researches the Iranian and Hellenistic empires of Asia and Egypt: the Medes, the Achaemenids and their satrapies, the Diadochi settlements of Asia, the Seleucids, the Ptolemies with Cyrenaica, the Anatolian kingdoms (Bithynia, Pontus, Pergamon, Cappadocia, Galatia, Paphlagonia, Sophene), Atropatene, the Greco-Bactrians and Indo-Greeks, the Hasmoneans and Nabataea. Cliopatria lacks the satrapies as internal units, the Diadochi domains year by year between 323 and 301 BCE, the Egyptian revolts, the Seleucid east's loss to Parthia as dated events, and the Roman provincialisation of Asia as occupations; add them."),
    ("me-06", "Middle East", "Parthia and the Sasanians", -247, 651,
     "Researches Iran, Mesopotamia and Arabia before Islam: the Parthian and Sasanian empires, the Roman-Persian frontier kingdoms (Adiabene, Osroene, Gordyene, Commagene), the Kushano-Sasanians, Himyar, the Lakhmids and Ghassanids, and Arabia on the eve of Islam. Cliopatria lacks Characene, Elymais and Persis as Parthian vassals, Hatra, the Roman-Persian frontier year by year, Kindah and the Hejaz towns, and the Sasanian conquests of 602 to 628 as occupations; add them."),
    ("me-07", "Middle East", "Rashidun to Umayyad", 622, 750,
     "Researches the first Islamic state from Medina to the Abbasid revolution: Muhammad's Medina, the Rashidun conquests year by year, the first and second fitnas, the Umayyad caliphate and its frontiers in Transoxiana, Sind, the Maghreb and Iberia, with the Iranian holdouts (Dabuyids). Cliopatria lacks the conquests between 632 and 661 as dated gains, the Kharijite and Zubayrid counter-states of the second fitna, the Umayyad provinces as internal units, and the Khazar and Byzantine frontier zones; add them."),
    ("me-08", "Middle East", "Abbasids and the autonomous dynasties", 750, 1055,
     "Researches the Abbasid caliphate and the dynasties that ruled under its nominal authority: Tahirids, Saffarids, Samanids, Tulunids, Ikhshidids, Hamdanids, Buyids, Ziyarids, Sajids, the Zaydis and Alids of the Caspian, the Yemeni dynasties, the Qarmatians, the Fatimids and the Ghaznavids, following the Anwoo model of allegiance tints inside the caliphate. Cliopatria lacks the Tahirids and Ikhshidids, the Zanj and Qarmatian revolts as rebel zones, the Abbasid provinces as internal units, the Uqaylids and Mazyadids, and the Fatimid-Abbasid frontier in Syria year by year; add them."),
    ("me-09", "Middle East", "Turks, Crusaders, Mamluks", 1037, 1517,
     "Researches the Middle East from the Seljuk arrival to the Ottoman conquest of Egypt: the Great Seljuks and Rum, the Anatolian beyliks, the Crusader states and Cilician Armenia, Zengids, Ayyubids, the Khwarazmians, the Mamluks, the post-Ilkhanid dynasties of Iran (Jalayirids, Muzaffarids, Injuids, Chobanids, Sarbadars, Kartids), the Qara and Aq Qoyunlu, and the Yemeni and Omani dynasties. Cliopatria lacks the Assassins of Alamut, the Artuqids, the Eldiguzids and Salghurids, the Crusades as campaigns with contested zones, the Mongol invasion year by year, and the Mamluk-Timurid frontier; add them (the Ilkhanate and Timurids belong to ia-02)."),
    ("me-10", "Middle East", "Ottomans and the modern Middle East", 1299, 2026,
     "Researches the Ottoman Empire for its whole life, Safavid to Pahlavi and Islamic Iran, the Gulf and Arabian states, Muhammad Ali's Egypt and its successors, the mandates and the modern states of the Middle East with their wars. Cliopatria lacks the Ottoman provinces and the Ottoman-Safavid frontier year by year, the Mamluk beys of Egypt and the mamluks of Baghdad as autonomous rulers, the Zaydi and Omani imamates' internal frontiers, the British and French mandates as occupations, the Arab-Israeli war lines of 1948, 1967 and 1973, and the Syrian and Iraqi wars after 2011 as contested zones; add them."),
    # East Asia: 8
    ("ea-01", "East Asia", "Shang to Warring States", -1600, -221,
     "Researches China from the Shang to the Qin unification: Shang, Western and Eastern Zhou, the Spring and Autumn states and the Warring States, Yue and Minyue, and the Rong and Di neighbours. Cliopatria lacks the Xia as a culture, the Western Zhou vassal states before 750 BCE, Ba, Shu and Dian, the state of Zhongshan's predecessors, and the Warring States frontier walls as dated lines; add them."),
    ("ea-02", "East Asia", "Qin and Han", -221, 220,
     "Researches the Qin, the Eighteen Kingdoms and the Western and Eastern Han with Xin: the commanderies' expansion into Nanyue, Korea and the Western Regions, the Xiongnu wars and the protectorates. Cliopatria lacks the Han commanderies in Korea (Lelang) and Vietnam as internal units, the Hexi corridor and Tarim as dated gains, the Qiang and Dian as neighbours, the Yellow Turbans as a rebel zone, and the warlord domains of 190 to 220 (Yuan Shao, Liu Biao, Sun Ce); add them."),
    ("ea-03", "East Asia", "Three Kingdoms to Sui", 220, 618,
     "Researches China from the Three Kingdoms to the Sui: Wei, Shu and Wu, the Jin, the Sixteen Kingdoms, the Northern and Southern dynasties, Tuyuhun and the Sui reunification. Cliopatria lacks the Sixteen Kingdoms' overlapping years as contests, the Di and Qiang states' frontiers, the Southern dynasties' Lingnan and Vietnamese holdings as internal units, the Northern Wei's steppe frontier, and the Sui campaigns against Goguryeo as contested zones; add them."),
    ("ea-04", "East Asia", "Tang and the Five Dynasties", 618, 960,
     "Researches the Tang (with Wu Zhou as an era, not a new state), the Tibetan Empire and its fragmentation, Nanzhao, the An Lushan rebellion, the Tang protectorates as vassal tints, and the Five Dynasties and Ten Kingdoms. Cliopatria lacks the Tang protectorates (Anxi, Beiting, Andong, Annan) as internal units, the An Lushan and Huang Chao rebel zones, the jiedushi domains of the late Tang, the Tibetan-Tang contests over the Hexi corridor year by year, and the Later Zhou as a separate state from the ancient Zhou; add them."),
    ("ea-05", "East Asia", "Song, Liao, Jin, Xia", 907, 1279,
     "Researches the Liao, Northern and Southern Song, Western Xia, Jin and Dali, the Song-Liao, Song-Xia and Song-Jin frontiers by treaty, and the Jurchen and Mongol conquests. Cliopatria lacks the Sixteen Prefectures as a dated transfer, the Song-Jin front of 1127 to 1141, the Khitan and Jurchen tribal lands before their dynasties, the Tibetan Tsongkha kingdom, and the Mongol conquest of Jin and Song year by year; add them."),
    ("ea-06", "East Asia", "Yuan", 1271, 1368,
     "Researches the Yuan dynasty as the Mongol state in China, Tibet under the Sakya and Phagmodrupa, and the Red Turban and other rebellions that broke the Yuan apart. Cliopatria lacks the Yuan provinces as internal units, the Red Turban states (Han Song, Chen Han, Ming Xia, Zhang Shicheng's Wu, Fang Guozhen), the Yuan campaigns in Japan, Vietnam, Burma and Java as contests, and Goryeo's vassal status as a tint; add them."),
    ("ea-07", "East Asia", "Ming", 1368, 1644,
     "Researches the Ming from Hongwu to the fall of Beijing, the Southern Ming, Li Zicheng's Shun, the northern frontier with the Mongols, the tusi of the south-west and the vassal tints over Joseon and the tributaries. Cliopatria lacks the Ming conquest of Yunnan and Vietnam (1407 to 1427) as dated gains, the Great Wall garrison zones, the Jurchen tribes before Nurhaci, the Wokou-era coast, and the Shun and Xi rebel states of the 1640s as their own polities; add them."),
    ("ea-08", "East Asia", "Qing to the People's Republic", 1616, 2026,
     "Researches the Later Jin and Qing to the Republic and the People's Republic: the Qing conquests, the Taiping and Panthay rebellions, the treaty-port concessions, the 1911 revolution, the warlord era, Manchukuo, the Civil War and Taiwan. Cliopatria lacks the Qing conquest of Xinjiang and Taiwan as dated gains, the Dungan and Nian rebel zones, the foreign concessions and leased territories, the warlord cliques of 1916 to 1928 as states, Manchukuo and the Japanese-occupied zones, and the Civil War fronts 1946 to 1949 year by year; add them."),
    # Inner Asia and the steppe: 3
    ("ia-01", "Inner Asia", "Xiongnu to the Türks", -800, 1206,
     "Researches the steppe from the Scythians to the eve of Chinggis Khan: Scythia, Xiongnu, Yuezhi, Wusun, Xianbei, Rouran, the Iranian Huns (Kidarites, Xionites, Hephthalites), the Türk khaganates, Uyghurs, Yenisei Kyrgyz, Karluks, Karakhanids, the Tarim oasis states, Khazars, Bulgars, Oghuz, Kimek and Cumans, and the Qara Khitai. Cliopatria lacks the Sarmatians and Alans of the Pontic steppe, the Sakas, the Hephthalite-Sasanian frontier, the Pechenegs, the Cumans beyond one tiny shape, the Naiman, Kerait and Merkit before 1206, and the Tarim states beyond Khotan and Qocho; add them."),
    ("ia-02", "Inner Asia", "Mongols and successor khanates", 1206, 1507,
     "Researches the Mongol Empire and its division: the Golden Horde and its fragments (White and Blue Hordes, Kazan, Astrakhan, Crimea, Sibir, Nogai, Qasim), the Chagatai Khanate and Moghulistan, the Ilkhanate, the Timurids, the Northern Yuan and the Oirats, down to the Uzbek conquest of Transoxiana. Cliopatria lacks the Mongol conquests year by year from 1206 to 1260, the uluses before the empire's formal division, the Ilkhanate's successor emirates as a whole, the Timurid partitions after 1405, and the Kazakh and Uzbek emergence from the Golden Horde; add them."),
    ("ia-03", "Inner Asia", "Central Asian khanates to the republics", 1465, 2026,
     "Researches Central Asia, Mongolia and Afghanistan from the Kazakh and Uzbek khanates to the republics: Bukhara, Khiva, Kokand, the Kazakh zhuzes, the Yarkent khanate, the Dzungars, the Khoshuts and Kalmyks, the Mongols under the Qing, the Afghan states from the Hotaki and Durrani to the Taliban, Russian Turkestan, the Soviet republics and the modern states. Cliopatria lacks the Russian conquest of the steppe and Turkestan year by year, the Kokand-Bukhara-Khiva frontiers, the Dzungar genocide and Qing Xinjiang as a dated change, the Turkestan Autonomy and Alash Orda of 1917 to 1920, the Basmachi zones, and the Afghan civil war fronts after 1979; add them."),
    # Japan and Korea: 2
    ("jk-01", "Japan and Korea", "Japan", 250, 2026,
     "Researches Japan from Yamato to today: the Asuka, Nara and Heian states, the Northern Fujiwara, the shogunates, the Sengoku daimyo domains, the Tokugawa system, the Ryukyu kingdoms, Ezo and the Ainu, the Empire of Japan with its colonies and wartime conquests, and post-war Japan. Cliopatria lacks Yamato before 540, the Emishi frontier as dated gains, the Sengoku domains as polities, the Edo-period han as internal units, Japanese Taiwan, Korea, Karafuto and the Mandate islands as colonies, and the 1937 to 1945 occupations as occupations; add them."),
    ("jk-02", "Japan and Korea", "Korea", -300, 2026,
     "Researches Korea from Gojoseon to the two republics: the Samhan, Goguryeo, Baekje, Silla, Gaya, Balhae, the Later Three Kingdoms, Goryeo, Joseon with its vassal tints under Ming and Qing, the Korean Empire, Japanese rule as occupation, and the division with the war front year by year. Cliopatria lacks the Han commanderies in Korea, Gaya, the Goguryeo-Sui and Goguryeo-Tang wars as contests, the Mongol invasions and Goryeo's vassal years, the Imjin War occupation zones, and the Korean War front 1950 to 1953; add them."),
    # South Asia: 6
    ("sa-01", "South Asia", "Indus to the Mahajanapadas", -3300, -321,
     "Researches South Asia from the Indus cities to the Nanda Empire: the Indus Valley Civilisation as a culture, the sixteen Mahajanapadas, the Magadha dynasties and the Nandas, with the Persian satrapies of the north-west as a neighbour. Cliopatria lacks the post-Indus cultures (Painted Grey Ware, the Vedic janapadas before 600 BCE), the southern chiefdoms, the Achaemenid Gandhara and Hindush satrapies as occupations, and the Mahajanapadas' wars as dated transfers; add them."),
    ("sa-02", "South Asia", "Maurya to Gupta", -321, 550,
     "Researches the Mauryas, Shungas, Kanvas, Satavahanas, Kalinga, the Indo-Scythians, Indo-Parthians and Kushans, the Western Satraps, the Guptas and Vakatakas, the early Pallavas, Kadambas and Kalabhras, the Sangam south and early Anuradhapura. Cliopatria lacks the Mauryan provinces, the Sangam Chera, Chola and Pandya frontiers, the Kushan-Gupta transition year by year, the Hunnic (Alchon) invasions as contests, the Nagas and Vakataka branches, and the Sri Lankan Chola occupations; add them (the Indo-Greeks belong to me-05, the Iranian Huns to ia-01)."),
    ("sa-03", "South Asia", "Medieval kingdoms", 550, 1206,
     "Researches India and Sri Lanka from the Chalukyas to the Ghurid conquest: Harsha, the Chalukyas, Pallavas and Pandyas, the Rashtrakutas, Pratiharas and Palas (the tripartite struggle), the Cholas and their overseas empire, the Rajput dynasties, Kashmir, Sind under the Habbaris, Bengal and Assam, and Polonnaruwa. Cliopatria lacks the Chola overseas conquests (Sri Lanka, Srivijaya) as dated gains, the Rajput states before 980, the Eastern Chalukyas, the Shahis of Kabul and Punjab, Nepal's Licchavis and Thakuris, and the Ghaznavid raids as contests; add them."),
    ("sa-04", "South Asia", "Delhi Sultanate", 1152, 1526,
     "Researches the Ghurids and the Delhi Sultanate's five dynasties, the regional sultanates (Bengal, Jaunpur, Malwa, Gujarat, Kashmir, Sind), the Bahmanis and the Deccan sultanates, Vijayanagara, the Rajput kingdoms, the Gajapatis, the Kathmandu valley and the Sri Lankan kingdoms. Cliopatria lacks Malwa and Gujarat as sultanates, the Rajput states (Mewar, Marwar), the Gajapatis and Reddis, the Ahom kingdom, the Tughlaq expansion and contraction year by year, and Timur's 1398 invasion as an occupation; add them."),
    ("sa-05", "South Asia", "Mughals and Marathas", 1526, 1857,
     "Researches the Mughals and Sur, the Deccan sultanates' end, the Marathas, Mysore, Hyderabad, Bengal, Awadh, the Carnatic, the Sikhs, the Rajput and Jat states, Gorkha Nepal and Bhutan, the Sind amirs and the eighteenth-century fragmentation. Cliopatria lacks the Mughal subahs as internal units, the Rajput and Jat states, Travancore and Cochin, the Maratha confederacy's members (Peshwa, Scindia, Holkar, Gaekwad, Bhonsle) as polities, the Rohillas, and the Anglo-Maratha and Anglo-Sikh war zones; add them (Afghanistan belongs to ia-03)."),
    ("sa-06", "South Asia", "British Raj to the republics", 1505, 2026,
     "Researches the European presence in South Asia and its aftermath: Portuguese, Dutch, Danish and French India and Ceylon, the Company Raj, the British Raj with the princely states as vassal tints, Partition, and India, Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan and the Maldives after independence with their wars. Cliopatria lacks the princely states as separate vassals, the Company's gains year by year from 1757 to 1857, Goa, Pondicherry and Chandernagore as dated possessions, the 1947 Partition lines and the Kashmir ceasefire line, and the 1971 war as a contest; add them."),
    # South-east Asia: 4
    ("se-01", "South-east Asia", "Mainland (Khmer, Pagan, Siam, Vietnam)", -300, 1860,
     "Researches mainland South-east Asia to the French arrival: Au Lac and Nanyue's Vietnam, Funan and Chenla, Champa, the Pyu, Dvaravati and Lavo, Haripunjaya, the Khmer Empire, Pagan and the Burmese kingdoms, Sukhothai, Lan Na and Ayutthaya, Lan Xang and its successors, Dai Viet under its dynasties and lords, Arakan, the Shan states and the Toungoo and Konbaung empires. Cliopatria lacks Dvaravati as a state, the Vietnamese march south (nam tien) as dated gains, the Shan states as separate polities, the Burmese-Siamese wars as contested zones, Cambodia between 1431 and 1700, and the Lao principalities' Siamese vassalage as tints; add them."),
    ("se-02", "South-east Asia", "Maritime (Srivijaya, Majapahit, Malacca)", 100, 1700,
     "Researches the island world to 1700: Tarumanagara, Srivijaya, the Javanese kingdoms from Mataram to Majapahit, Sunda and Bali, Malacca, Johor, Aceh, Brunei, the Sulu and Maguindanao sultanates, the Philippine rajahnates, Banjar, Gowa and the Moluccan sultanates. Cliopatria lacks Ternate and Tidore, Makassar's rise, the Minangkabau kingdom (Pagaruyung), Kedah's and Pattani's early history, the Bugis states, the Sulawesi and Maluku polities beyond Gowa and Bone, and Majapahit's vassal network as tints; add them."),
    ("se-03", "South-east Asia", "Colonial", 1511, 1945,
     "Researches the colonial era: Portuguese Malacca and Timor, the Spanish Philippines, the VOC and the Dutch East Indies, the Straits Settlements and British Malaya, Sarawak and North Borneo, British Burma, French Indochina, and the native states that lived under colonial protection (the Javanese courts of 1755, the Malay and Bornean sultanates after 1700) with the Japanese occupation. Cliopatria lacks the Spanish Philippines as a colony, the Straits Settlements and the Federated Malay States, British Burma as a dated conquest in 1826, 1852 and 1885, the Dutch conquests year by year (Aceh War, Bali, Lombok), North Borneo, and the Japanese occupation of 1942 to 1945; add them."),
    ("se-04", "South-east Asia", "Modern", 1932, 2026,
     "Researches South-east Asia from Siam's 1932 revolution and the 1945 independences: Thailand, Indonesia, the Philippines, Burma and Myanmar, the two Vietnams and their war fronts, Laos, Cambodia under its regimes, Malaya and Malaysia, Singapore, Brunei and East Timor. Cliopatria lacks the Indonesian revolution's Dutch-held zones, the First Indochina War fronts, the Vietnam War's contested provinces year by year, the Khmer Rouge-Vietnamese war, the Malayan Emergency, the Indonesian occupation of East Timor, and the Burmese ethnic insurgent zones; add them."),
    # Africa: 8
    ("af-01", "Africa", "Nubia, Kush, Axum, Ethiopia", -2500, 2026,
     "Researches the Nile south of Egypt and the Horn in every era: Kerma, Kush and Meroe, Axum, the Christian Nubian kingdoms, the Zagwe and Solomonic Ethiopia, Ifat, Adal and Harar, the Funj, the Somali sultanates, the Mahdist State and Ethiopia's restoration after the Italian occupation. Cliopatria lacks Kerma, Punt and the Blemmyes, Axum's Arabian holdings as occupations, the Beja, the Ajuran Sultanate, Ethiopia's Oromo and Gondarine-era frontiers year by year, the Egyptian conquest of Sudan 1820 to 1885, and the Italian occupation of 1936 to 1941 as an occupation; add them."),
    ("af-02", "Africa", "Carthage and the Maghreb", -814, 1912,
     "Researches North Africa west of Egypt: the Phoenician colonies and Carthage, Numidia and Mauretania, Vandal and Byzantine Africa as neighbours, the Arab conquest, the Rustamids, Idrisids, Aghlabids, Zirids and Hammadids, the Almoravids and Almohads, the Marinids, Zayyanids and Hafsids, the Saadians and Alaouites, the Ottoman regencies and Tripolitania to the French and Italian conquests. Cliopatria lacks the Garamantes, the Byzantine Exarchate of Africa, the Berber kingdoms of the Arab conquest era (Kusaila, the Kahina), the Zirid-Hilalian collapse year by year, the Spanish presidios and Portuguese Moroccan holdings, and the French conquest of Algeria 1830 to 1870 as dated gains; add them."),
    ("af-03", "Africa", "Sahel empires", 300, 1904,
     "Researches the Sahel and Sudanic belt: Ghana, Takrur, Sosso, Mali, Songhai, Kanem and Bornu, the Hausa states, Wadai, Bagirmi, Darfur, the Bambara kingdoms, the Fulani jihad states (Sokoto, Massina, Futa Jallon, Futa Toro, the Tukulor Empire) and Samori's Wassoulou. Cliopatria lacks the Hausa city-states, the Mossi kingdoms, Jolof, Futa Jallon and Futa Toro, the Tukulor and Wassoulou empires, Kaarta and Segu as separate states, Bagirmi, and the French conquest of the Sudan 1880 to 1900 as dated gains; add them."),
    ("af-04", "Africa", "Forest states", 1000, 1897,
     "Researches the West African forest zone: Ife and Benin, Oyo, Dahomey, the Akan states (Bonoman, Denkyira, Akwamu, Ashanti), the Niger Delta and Igbo polities, the Gold Coast forts, Sierra Leone and Liberia. Cliopatria lacks Benin, Dahomey, Ife, Nri and Aro, Denkyira and Akwamu, the Gold Coast forts of other nations (Brandenburg, Swedish), the Yoruba successor states after Oyo's fall, and the Scramble-era British and French protectorates as dated gains; add them."),
    ("af-05", "Africa", "Swahili and the Great Lakes", 800, 1897,
     "Researches the East African coast and interior: the Swahili city-states (Kilwa, Mombasa, Pate, Zanzibar), Portuguese Mombasa, Omani Zanzibar and its coast, and the Great Lakes kingdoms (Buganda, Bunyoro, Rwanda, Burundi, Karagwe, Ankole, Toro). Cliopatria lacks every Swahili city-state and every Great Lakes kingdom, the Portuguese coast 1505 to 1698, the Kamba and Nyamwezi trade states, Mirambo's Urambo, and the German and British occupations of the 1890s as dated gains; add them."),
    ("af-06", "Africa", "Central Africa", 1300, 1908,
     "Researches the Congo basin and Angola: Kongo, Loango, Ndongo and Matamba, Kasanje, the Luba and Lunda empires, Kazembe, Kuba, the Chokwe, Msiri's Yeke, Tippu Tip's domain and the Congo Free State's conquest. Cliopatria lacks Loango, Ndongo, Matamba and Kasanje, Luba, Kazembe, Kuba, Yeke and the Zanzibari Arab domains of the upper Congo, the Portuguese Angolan frontier year by year, and the Congo Free State as a state before 1890; add them."),
    ("af-07", "Africa", "Southern Africa", 1000, 1910,
     "Researches Southern Africa and Madagascar: Mapungubwe, Great Zimbabwe, Mutapa, Torwa and Rozvi, the Dutch and British Cape, the Mfecane states (Zulu, Ndebele, Swazi, Sotho, Gaza), the Boer republics, the Merina kingdom and the road to Union. Cliopatria lacks Mapungubwe, Great Zimbabwe, Mutapa and Rozvi, the Ndebele kingdom, Basutoland, Gazaland, the Sakalava and Betsimisaraka kingdoms of Madagascar, Stellaland and Goshen, Portuguese Mozambique's prazos, and the Boer War occupations as contested zones; add them."),
    ("af-08", "Africa", "Partition and independence", 1830, 2026,
     "Researches colonial Africa and its successor states: the French, British, German, Belgian, Portuguese, Italian and Spanish territories as dated gains from the French landing at Algiers to the 1914 partition, the World War transfers, the independences year by year, and the post-colonial states with their secessions and wars. Cliopatria draws the colonial empires as single continental shapes and lacks their individual colonies, the Scramble's dated gains, the 1919 mandate transfers, Biafra, Katanga, Eritrea's war, Somaliland, Western Sahara and the Congo wars as contested zones; add them."),
    # Americas: 8
    ("am-01", "Americas", "Olmec to Teotihuacan", -1500, 900,
     "Researches Mesoamerica outside the Maya before 900: the Olmecs, Monte Alban and the Zapotecs, Teotihuacan and its sphere, Classic Veracruz (El Tajin), Cholula and the Epiclassic centres (Xochicalco, Cacaxtla). Cliopatria lacks Monte Alban as distinct from the Zapotec culture, Cholula, Xochicalco and Cacaxtla, Teotihuacan's reach beyond its valley as a sphere rather than territory, and the West Mexican shaft-tomb cultures; add them, drawn as cultures where no state can be shown."),
    ("am-02", "Americas", "Maya", -1000, 1697,
     "Researches the Maya from the Preclassic to the fall of Nojpeten: the Classic city-states (Tikal, Calakmul, Caracol, Copan, Palenque and their alliances), the collapse, Chichen Itza, Mayapan, the Postclassic kingdoms of Yucatan, the Quiche and Kaqchikel highland states and the Itza. Cliopatria lacks the individual Classic kingdoms and their hegemonies year by year, Chichen Itza and Mayapan as states, the sixteen Yucatecan provinces of 1500, the Quiche and Kaqchikel kingdoms, and the Spanish conquest of the highlands and Yucatan as dated gains; add them."),
    ("am-03", "Americas", "Toltec and Aztec", 900, 1521,
     "Researches Postclassic central and western Mexico: the Toltecs, the Chichimec migrations, the Valley of Mexico altepetl (Azcapotzalco, Texcoco, Tenochtitlan), the Triple Alliance and its tributary provinces as vassal tints, Tlaxcala, the Tarascan state, the Mixtec kingdoms and the Huastecs. Cliopatria lacks Azcapotzalco and the Tepanec empire, Tlaxcala and the other independent enclaves, the Aztec tributary provinces as internal units, the Mixtec and Huastec polities, and the Spanish conquest of 1519 to 1521 as a contest; add them."),
    ("am-04", "Americas", "Andes to the Inca", -3000, 1572,
     "Researches the Andes and northern South America from Caral to Vilcabamba: Chavin, Moche, Nazca, Tiwanaku, Wari, Sican, Chimor, the Chachapoya, Chincha and the Aymara lordships, Cuzco and the Inca Empire, the Muisca and Tairona, and the Neo-Inca state. Cliopatria lacks every pre-Chimu Andean polity, Tiwanaku and Wari as states, the Muisca and Tairona, the Aymara kingdoms, the Inca conquests year by year, the civil war of 1529 to 1532 as a contest, and Vilcabamba; add them, drawn as cultures where no state can be shown."),
    ("am-05", "Americas", "North America before contact", -1000, 1890,
     "Researches the indigenous polities of North America in every era, before and after contact: Hopewell and the Mississippian chiefdoms (Cahokia, Moundville, Etowah), the Ancestral Puebloans, Hohokam and the Chaco system, the Haudenosaunee and other confederacies, Powhatan, the Calusa, the Comancheria, the Lakota and the Cherokee, Creek and Choctaw nations, drawn as cultures where no state can be shown. Cliopatria lacks every one of them but Chaco, Aztec-era Pueblo and the Haudenosaunee; add Cahokia and the Mississippian chiefdoms, the Pueblo and Hohokam, the Huron and Powhatan confederacies, the Comancheria, the Plains nations and the Five Civilised Tribes, with the treaty cessions as dated losses."),
    ("am-06", "Americas", "Spanish and Portuguese America", 1492, 1825,
     "Researches colonial Latin America and the Caribbean: the Spanish Empire's viceroyalties and audiencias as internal units, Portuguese Brazil and its captaincies, Dutch Brazil, the Jesuit missions, the French, British, Dutch and Danish Caribbean and the Guianas, Spanish Florida and Louisiana, and the independence wars' fronts to 1825. Cliopatria draws the empires as single shapes and lacks the viceroyalties, the Caribbean colonies as dated possessions, the Bourbon reforms' new units, the Portuguese-Spanish frontier in the Plata year by year, and the independence wars' royalist and patriot zones as contests; add them."),
    ("am-07", "Americas", "United States and Canada", 1600, 2026,
     "Researches the settler states of North America: New France, New Netherland, New Sweden, the Thirteen Colonies, British North America, the United States with its territories and states year by year (monthly where the Newberry atlas allows), Vermont, Texas, California, the Confederacy, Canada's provinces, Russian America and Alaska. Cliopatria lacks the colonies as separate units, the territorial acquisitions (Louisiana, Florida, Oregon, the Mexican Cession, Gadsden, Alaska) as dated gains, the Civil War front year by year, Canada's provincial growth, and the Hudson's Bay Company lands; add them (indigenous nations belong to am-05)."),
    ("am-08", "Americas", "The republics from 1810", 1804, 2026,
     "Researches Latin America and the Caribbean from Haiti's independence and the 1810 juntas to today: Mexico under its empires and republics, Central America, Gran Colombia and its successors, Peru, Bolivia, Chile, the Plata states, Brazil as empire and republic, the Caribbean republics and the Commonwealth Caribbean states, with their wars (the Pacific, the Triple Alliance, the Chaco, the Mexican-American War). Cliopatria lacks the Mexican Cession as a dated loss, the War of the Pacific and Chaco War zones, the Acre and Leticia transfers, the Central American federations' members as states, the Cuban and Mexican revolutions' fronts, and the smaller Caribbean states' colonial predecessors; add them."),
    # Oceania: 2
    ("oc-01", "Oceania", "Polynesian and Melanesian states", 1000, 1900,
     "Researches the indigenous states of the Pacific: the Tu'i Tonga maritime empire, the Hawaiian chiefdoms and kingdom, the Tahitian Pomare kingdom, Samoa's districts, Fiji's confederations and Cakobau's kingdom, the Maori iwi and the Kingitanga, Rapa Nui and the Micronesian chiefdoms (Yap, Pohnpei), drawn as chiefdoms where no state can be shown. Cliopatria holds only Hawaii and Cakobau's Fiji; add the Tu'i Tonga, Tahiti, Samoa, the Maori polities, Rapa Nui and the Micronesian chiefdoms with their dated unifications."),
    ("oc-02", "Oceania", "Australia, New Zealand and the colonial Pacific", 1788, 2026,
     "Researches Australia from New South Wales to the Commonwealth, New Zealand from the Treaty of Waitangi, the colonial partition of the Pacific (German, British, French, American and Japanese holdings), the Pacific War occupations, and the independent island states. Cliopatria lacks the Australian colonies before 1901 as separate units, New Zealand before 1948, the New Zealand Wars as contests, German New Guinea and Samoa, the French, British and American Pacific possessions as dated gains, the Japanese Mandate, the Pacific War occupations, and the island states' independences before 1979; add them."),
    # Cross-cutting: 3
    ("xx-01", "Cross-cutting", "Cultures 6000 to 3400 BCE", -6000, -3400,
     "Researches the archaeological cultures of the world between 6000 and 3400 BCE, drawn as cultures in a muted dotted style: Ubaid, Halaf, Samarra and Uruk in Mesopotamia, Naqada and Badari in Egypt, Yangshao, Hemudu, Dawenkou and Liangzhu in China, Mehrgarh and the early Indus, Vinca, Cucuteni-Trypillia, Linear Pottery and the megalith builders in Europe, Jomon, the Sahara's cattle herders, Caral's precursors and the earliest Americas. Cliopatria holds nothing before 3400 BCE; add every culture with a dated extent from the archaeological literature, so that the map before the first states is never blank."),
    ("xx-02", "Cross-cutting", "The gazetteer", -6000, 2026,
     "Compiles every region name used in the dossiers' ledgers into cells: Cliopatria shapes by polity and year, Natural Earth countries, provinces, rivers and lakes, cities with a radius, historical regions by name, and border bands between two states. Owns no polities; it serves every other group, keeps data/gazetteer/ and its resolution log, and reports every name it cannot resolve back to the group that wrote it."),
    ("xx-03", "Cross-cutting", "Wars and fronts index", -3400, 2026,
     "Compiles the index of wars and fronts across all dossiers: each war's name, years, belligerents, the zones fought over and the outcome, with the documented fronts by year (both World Wars, the Taiping, the Eastern Front, the Mongol conquests) so that contested and occupied zones are consistent between neighbouring dossiers. Owns no polities; it reads every group's wars section, reconciles each contest's start and end between the two claimants, and lists the wars whose zones no gazetteer name covers."),
]
GROUP_IDS = [g[0] for g in GROUPS]
assert len(GROUPS) == 76, len(GROUPS)

# --------------------------------------------------------------------------
# Modern country (Natural Earth ADMIN) -> macro-region
# --------------------------------------------------------------------------
MACRO = {}
for c in ["United Kingdom", "Ireland", "Isle of Man", "France", "Monaco", "Spain", "Portugal", "Andorra", "Gibraltar",
          "Italy", "San Marino", "Vatican", "Malta", "Germany", "Austria", "Switzerland", "Netherlands", "Belgium",
          "Luxembourg", "Liechtenstein", "Denmark", "Norway", "Sweden", "Finland", "Iceland", "Estonia", "Latvia",
          "Greenland", "Faroe Islands", "Poland", "Lithuania", "Czechia", "Slovakia", "Hungary", "Russia", "Ukraine",
          "Belarus", "Moldova", "Greece", "Cyprus", "Northern Cyprus", "Bulgaria", "Republic of Serbia", "Croatia",
          "Bosnia and Herzegovina", "Montenegro", "Albania", "North Macedonia", "Kosovo", "Romania", "Slovenia",
          "Georgia", "Armenia", "Azerbaijan", "Jersey", "Guernsey", "Aland", "Falkland Islands",
          "South Georgia and the Islands", "Saint Pierre and Miquelon"]:
    MACRO[c] = "eu"
for c in ["Iraq", "Iran", "Syria", "Lebanon", "Israel", "Palestine", "Jordan", "Saudi Arabia", "Yemen", "Oman",
          "United Arab Emirates", "Qatar", "Bahrain", "Kuwait", "Turkey", "Egypt"]:
    MACRO[c] = "me"
for c in ["China", "Taiwan", "Hong Kong S.A.R.", "Macao S.A.R"]:
    MACRO[c] = "ea"
for c in ["Japan", "South Korea", "North Korea"]:
    MACRO[c] = "jk"
for c in ["Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan", "Mongolia", "Afghanistan"]:
    MACRO[c] = "ia"
for c in ["India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal", "Bhutan", "Maldives"]:
    MACRO[c] = "sa"
for c in ["Myanmar", "Thailand", "Laos", "Cambodia", "Vietnam", "Malaysia", "Singapore", "Indonesia", "Philippines",
          "Brunei", "East Timor"]:
    MACRO[c] = "se"
AF_SUB = {}
for c in ["Morocco", "Algeria", "Tunisia", "Libya", "Western Sahara"]:
    AF_SUB[c] = "af-02"
for c in ["Sudan", "South Sudan", "Ethiopia", "Eritrea", "Somalia", "Somaliland", "Djibouti"]:
    AF_SUB[c] = "af-01"
for c in ["Mauritania", "Mali", "Niger", "Chad", "Burkina Faso", "Senegal", "Gambia", "Cabo Verde"]:
    AF_SUB[c] = "af-03"
for c in ["Ghana", "Ivory Coast", "Liberia", "Sierra Leone", "Guinea", "Guinea-Bissau", "Togo", "Benin", "Nigeria"]:
    AF_SUB[c] = "af-04"
for c in ["Kenya", "United Republic of Tanzania", "Uganda", "Rwanda", "Burundi", "Seychelles", "Comoros"]:
    AF_SUB[c] = "af-05"
for c in ["Democratic Republic of the Congo", "Republic of the Congo", "Gabon", "Central African Republic", "Angola",
          "Equatorial Guinea", "Cameroon", "São Tomé and Principe"]:
    AF_SUB[c] = "af-06"
for c in ["South Africa", "Namibia", "Botswana", "Zimbabwe", "Mozambique", "Lesotho", "eSwatini", "Madagascar",
          "Zambia", "Malawi", "Mauritius"]:
    AF_SUB[c] = "af-07"
for c in AF_SUB:
    MACRO[c] = "af"
AM_SUB = {}
for c in ["Mexico", "Guatemala", "Belize", "Honduras", "El Salvador", "Nicaragua", "Costa Rica", "Panama"]:
    AM_SUB[c] = "meso"
for c in ["United States of America", "Canada", "United States Minor Outlying Islands"]:
    AM_SUB[c] = "north"
for c in ["Cuba", "Haiti", "Dominican Republic", "Jamaica", "Puerto Rico", "The Bahamas", "Barbados",
          "Trinidad and Tobago", "Antigua and Barbuda", "Saint Kitts and Nevis", "Saint Vincent and the Grenadines",
          "Grenada", "Dominica", "Saint Lucia", "Guyana", "Suriname", "French Guiana"]:
    AM_SUB[c] = "carib"
for c in ["Peru", "Bolivia", "Ecuador", "Colombia", "Venezuela", "Chile", "Argentina", "Uruguay", "Paraguay", "Brazil"]:
    AM_SUB[c] = "south"
for c in AM_SUB:
    MACRO[c] = "am"
for c in ["Australia", "New Zealand", "Papua New Guinea", "Fiji", "Tonga", "Samoa", "Vanuatu", "Solomon Islands",
          "Kiribati", "Federated States of Micronesia", "Marshall Islands", "Palau", "Nauru", "Tuvalu",
          "French Polynesia", "New Caledonia", "Guam", "Northern Mariana Islands", "American Samoa", "Niue",
          "Cook Islands", "Wallis and Futuna", "Pitcairn Islands", "Norfolk Island"]:
    MACRO[c] = "oc"

EU_COUNTRY = {}
for c in ["Greece", "Cyprus", "Northern Cyprus"]:
    EU_COUNTRY[c] = "greece"
for c in ["Italy", "San Marino", "Vatican", "Malta"]:
    EU_COUNTRY[c] = "italy"
for c in ["France", "Monaco"]:
    EU_COUNTRY[c] = "france"
for c in ["United Kingdom", "Ireland", "Isle of Man", "Jersey", "Guernsey"]:
    EU_COUNTRY[c] = "britain"
for c in ["Spain", "Portugal", "Andorra", "Gibraltar"]:
    EU_COUNTRY[c] = "iberia"
for c in ["Germany", "Austria", "Switzerland", "Netherlands", "Belgium", "Luxembourg", "Liechtenstein"]:
    EU_COUNTRY[c] = "germany"
for c in ["Denmark", "Norway", "Sweden", "Finland", "Iceland", "Estonia", "Latvia", "Greenland", "Faroe Islands", "Aland"]:
    EU_COUNTRY[c] = "nordic"
for c in ["Poland", "Lithuania", "Czechia", "Slovakia", "Hungary"]:
    EU_COUNTRY[c] = "central"
for c in ["Russia", "Ukraine", "Belarus", "Moldova"]:
    EU_COUNTRY[c] = "rus"
for c in ["Bulgaria", "Republic of Serbia", "Croatia", "Bosnia and Herzegovina", "Montenegro", "Albania",
          "North Macedonia", "Kosovo", "Romania", "Slovenia"]:
    EU_COUNTRY[c] = "balkans"
for c in ["Georgia", "Armenia", "Azerbaijan"]:
    EU_COUNTRY[c] = "caucasus"


def rule(r):
    """Default group from modern_countries, centroid and first_year."""
    cc = [c for c in r["modern_countries"].split(";") if c]
    c0 = cc[0] if cc else ""
    y = int(r["first_year"])
    lon = float(r["centroid_lon"])
    lat = float(r["centroid_lat"])
    macro = MACRO.get(c0)
    if c0 == "Russia" and lon >= 60:
        macro = "ia"
    if macro is None:
        # centroid fallback
        if lat > 35 and -25 < lon < 45:
            macro = "eu"
        elif 25 < lon < 65 and 10 < lat < 42:
            macro = "me"
        elif lon >= 95 and lat > 18 and lat < 55:
            macro = "ea"
        elif -20 < lon < 55 and -36 < lat < 37:
            macro = "af"
        elif lon < -30:
            macro = "am"
        else:
            macro = "oc"
    if macro == "eu":
        k = EU_COUNTRY.get(c0, "greece")
        if k == "caucasus":
            return "eu-19"
        if y >= 1945:
            return "eu-22"
        if y >= 1914:
            return "eu-21"
        if k == "balkans" and 681 <= y < 1912:
            return "eu-18"
        if k == "rus":
            return "eu-17" if y >= 1721 else "eu-16"
        if y >= 1789:
            return "eu-20"
        if k == "greece":
            if y < -323:
                return "eu-01"
            if y < -30:
                return "eu-02"
            if y < 395:
                return "eu-04"
            if y < 1461:
                return "eu-05"
            return "eu-18"
        if k == "balkans":
            if y < -323:
                return "eu-01"
            if y < -30:
                return "eu-02"
            if y < 395:
                return "eu-04"
            return "eu-06"
        if k == "italy":
            if y < -27:
                return "eu-03"
            if y < 395:
                return "eu-04"
            if y < 568:
                return "eu-06"
            return "eu-13"
        if k == "france":
            if y < -27:
                return "eu-03"
            if y < 238:
                return "eu-04"
            if y < 843:
                return "eu-07"
            return "eu-10"
        if k == "britain":
            return "eu-11" if y >= 410 else "eu-04"
        if k == "iberia":
            if y < -27:
                return "eu-03"
            if y < 395:
                return "eu-04"
            if y < 711:
                return "eu-06"
            return "eu-12"
        if k == "germany":
            if y < 476:
                return "eu-04" if y < 30 else "eu-06"
            if y < 911:
                return "eu-06" if y < 750 else "eu-07"
            if y < 1250:
                return "eu-08"
            return "eu-09"
        if k == "nordic":
            return "eu-14"
        if k == "central":
            return "eu-15"
        return "eu-18"
    if macro == "me":
        egypt = c0 == "Egypt"
        levant = c0 in ("Turkey", "Syria", "Lebanon", "Israel", "Palestine", "Jordan", "Yemen", "Saudi Arabia")
        if egypt and y < -332:
            return "me-03"
        if y < -2000:
            return "me-01"
        if levant and y < -550:
            return "me-04"
        if y < -550:
            return "me-02"
        if y < -63:
            return "me-05"
        if y < 622:
            return "me-06"
        if y < 750:
            return "me-07"
        if y < 1037:
            return "me-08"
        if y < 1500:
            return "me-09"
        return "me-10"
    if macro == "ea":
        if y < -221:
            return "ea-01"
        if y < 220:
            return "ea-02"
        if y < 618:
            return "ea-03"
        if y < 907:
            return "ea-04"
        if y < 1271:
            return "ea-05"
        if y < 1368:
            return "ea-06"
        if y < 1636:
            return "ea-07"
        return "ea-08"
    if macro == "jk":
        return "jk-01" if c0 == "Japan" else "jk-02"
    if macro == "ia":
        if y < 1206:
            return "ia-01"
        if y < 1500:
            return "ia-02"
        return "ia-03"
    if macro == "sa":
        if y < -321:
            return "sa-01"
        if y < 550:
            return "sa-02"
        if y < 1206:
            return "sa-03"
        if y < 1526:
            return "sa-04"
        if y < 1757:
            return "sa-05"
        return "sa-06"
    if macro == "se":
        mainland = c0 in ("Myanmar", "Thailand", "Laos", "Cambodia", "Vietnam")
        if y >= 1945:
            return "se-04"
        if mainland:
            return "se-01" if y < 1860 else "se-03"
        return "se-02" if y < 1700 else "se-03"
    if macro == "af":
        if y >= 1880:
            return "af-08"
        return AF_SUB.get(c0, "af-06")
    if macro == "am":
        sub = AM_SUB.get(c0, "south")
        if sub == "north":
            return "am-05" if y < 1600 else "am-07"
        if sub == "meso":
            if y < 900:
                return "am-02" if c0 in ("Guatemala", "Belize", "Honduras", "El Salvador") else "am-01"
            if y < 1492:
                return "am-03"
            return "am-06" if y < 1810 else "am-08"
        if sub == "carib":
            return "am-06" if y < 1804 else "am-08"
        if y < 1492:
            return "am-04"
        return "am-06" if y < 1810 else "am-08"
    if macro == "oc":
        return "oc-01" if y < 1788 else "oc-02"
    raise ValueError(r["slug"])


# --------------------------------------------------------------------------
# Overrides: historical judgment where the rule is wrong. slug -> group id
# --------------------------------------------------------------------------
OVERRIDES = {}


def _o(gid, *slugs):
    for s in slugs:
        assert s not in OVERRIDES, s
        OVERRIDES[s] = gid


# Europe
_o("eu-01", "minoan-civilization", "mycenaean-greece", "greek-dark-ages", "greek-city-states", "peloponnesian-league",
   "odrysian-kingdom", "cimmerian-bosporus", "sacred-band-of-thebes", "second-athenian-league", "thebans")
_o("eu-02", "macedonian-empire", "athenian-coalition", "kingdom-of-lysimachus", "polyperchon", "antigonid-dynasty",
   "aetolian-league", "achaean-league", "antigonid-macedonia", "greek-colonies", "illyrian-kingdom", "rhodes", "molossians")
_o("eu-03", "etruscans", "roman-kingdom", "roman-republic", "mamertines", "italian-city-states", "thracian-kingdom")
_o("eu-04", "roman-empire", "gallic-empire", "western-roman-empire", "kingdom-of-soissons", "palmyrene-empire")
_o("eu-05", "eastern-roman-empire", "byzantine-empire", "cyprus-condominium", "emirate-of-crete", "despotate-of-epirus",
   "domain-of-rhodes", "duchy-of-athens", "empire-of-trebizond", "kingdom-of-thessalonica", "latin-empire", "negroponte",
   "nicaean-empire", "principality-of-achaea", "duchy-of-the-archipelago", "empire-of-thessalonica", "thessaly",
   "catalan-company", "principality-of-theodoro", "commune-of-the-zealots", "house-of-tocco", "despotate-of-arta")
_o("eu-06", "goths", "huns", "burgundians", "gothia", "saxons", "vandals", "angles", "visigoths", "alans",
   "burgundian-kingdom", "kingdom-of-the-suebi", "hunnic-empire", "visigothic-kingdom", "vandal-kingdom", "ostrogoths",
   "rugiland", "kingdom-of-alamannia", "thuringian-states", "kingdom-of-thuringia", "lombards", "ostrogothic-kingdom",
   "kingdom-of-the-gepids", "bavarians", "avar-khaganate", "duchy-of-thuringia", "magna-frisia", "frisia-kingdom",
   "carantania")
_o("eu-07", "ripuarian-franks", "salian-franks", "kingdom-of-the-franks", "breton-kingdoms", "aquitaine",
   "merovingian-empire", "carolingian-empire", "kingdom-of-neustria", "frisia", "frisians", "obotrites",
   "kingdom-of-brittany", "east-franks", "middle-franks", "west-franks", "lower-burgundy", "upper-burgundy",
   "kingdom-of-lower-burgundy", "upper-burgundy-and-italy")
_o("eu-08", "kingdom-of-germany", "holy-roman-empire", "kingdom-of-arles")
_o("eu-09", "county-of-brabant", "county-of-holland", "duchy-of-bavaria", "duchy-of-styria",
   "holy-roman-empire-minor-states", "house-of-ascania", "house-of-habsburg", "house-of-hohenstaufen",
   "house-of-luxembourg", "house-of-wittelsbach", "margraviate-of-brandenburg", "swiss-confederation",
   "electorate-of-trier", "free-county-of-burgundy", "electorate-of-saxony", "electorate-of-brandenburg",
   "duchy-of-luxembourg", "duchy-of-lorraine", "habsburg-monarchy", "duchy-of-prussia", "union-of-utrecht",
   "dutch-republic", "brandenburg-prussia", "kingdom-of-prussia", "electorate-of-hanover", "principality-of-liechtenstein")
_o("eu-10", "duchy-of-gascony", "duchy-of-normandy", "duchy-of-brittany", "county-of-anjou", "county-of-blois",
   "county-of-champagne", "county-of-flanders", "county-of-maine", "county-of-rouergue", "county-of-toulouse",
   "county-of-vermandois", "county-of-vexin", "duchy-of-aquitaine", "kingdom-of-france", "duchy-of-burgundy",
   "county-of-nevers", "angevins", "county-of-boulogne", "county-of-armagnac", "county-of-auvergne",
   "county-of-perigord", "county-of-poitou", "county-of-touraine", "county-of-foix", "county-of-artois",
   "capetian-house-of-anjou", "dauphine", "principality-of-orange", "comtat-venaissin", "house-of-bourbon",
   "house-of-valois-anjou", "county-of-bearn", "huguenots", "principality-of-monaco")
_o("eu-11", "brythons", "anglo-saxon-england", "kingdom-of-kent", "kingdom-of-sussex", "wihtgar", "kingdom-of-deira",
   "kingdom-of-east-anglia", "kingdom-of-essex", "kingdom-of-lindsey", "kingdom-of-mercia", "kingdom-of-wessex",
   "dal-riata", "kingdom-of-brycheiniog", "kingdom-of-gwent", "kingdom-of-gwynedd", "kingdom-of-morgannwg",
   "kingdom-of-powys", "kingdom-of-bernicia", "hwicce", "kingdom-of-dunoting", "kingdom-of-rheged", "dumnonia",
   "kingdom-of-northumbria", "strathclyde", "cornwall", "danelaw", "kingdom-of-seisyllwg", "kingdom-of-alba",
   "kingdom-of-england", "norman-england", "kingdom-of-the-isles", "kingdom-of-powys-fadog",
   "kingdom-of-powys-wenwynwyn", "kingdom-of-mann", "angevin-empire", "kingdom-of-scotland", "earldom-of-ulster",
   "earldom-of-desmond", "isle-of-man", "irish-catholic-confederation", "commonwealth-of-england",
   "kingdom-of-great-britain", "british-colonial-empire")
_o("eu-12", "kingdom-of-asturias", "emirate-of-cordoba", "kingdom-of-pamplona", "kingdom-of-sobrarbe", "county-of-aragon",
   "county-of-ribagorza", "county-of-urgell", "county-of-pallars", "county-of-rosellon", "county-of-barcelona",
   "county-of-berga", "county-of-besalu", "kingdom-of-galicia", "kingdom-of-leon", "caliphate-of-cordoba",
   "kingdom-of-castile", "county-of-osona", "county-of-ampuria", "kingdom-of-aragon", "county-of-pallars-jussa",
   "county-of-pallars-sobira", "taifa-of-ceuta", "county-of-portugal", "kingdom-of-navarre", "kingdom-of-portugal",
   "crown-of-aragon", "crown-of-castile", "emirate-of-granada", "kingdom-of-majorca", "kingdom-of-spain",
   "iberian-union", "catalonia", "pro-habsburg-spain")
_o("eu-13", "duchy-of-benevento", "duchy-of-spoleto", "duchy-of-tuscia", "kingdom-of-italy", "republic-of-venice",
   "papal-states", "duchy-of-naples", "principality-of-capua", "principality-of-salerno", "emirate-of-sicily",
   "giudicato-of-arborea", "giudicato-of-cagliari", "giudicato-of-gallura", "giudicato-of-logudoro",
   "republic-of-amalfi", "republic-of-genoa", "republic-of-pisa", "norman-italy", "kingdom-of-sicily",
   "county-of-savoy", "patriarchate-of-aquileia", "republic-of-florence", "kingdom-of-naples", "duchy-of-milan",
   "ambrosian-republic", "house-of-savoy", "kingdom-of-sardinia", "corsican-republic", "kingdom-of-naples-napoleonic")
_o("eu-14", "norse", "scandinavian-minor-kingdoms", "old-kingdom-of-norway", "icelandic-commonwealth",
   "kingdom-of-denmark", "kingdom-of-sweden", "jaemtland", "north-sea-empire", "denmark-england", "norway-denmark",
   "livonian-brothers-of-the-sword", "teutonic-order", "danish-magnates", "kalmar-union", "livonian-conference",
   "house-of-oldenburg", "denmark-norway", "swedish-empire", "duchy-of-courland", "norse-greenland", "greenland",
   "viking-settlements")
_o("eu-15", "samo-s-empire", "great-moravia", "principality-of-nitra", "magyars", "duchy-of-bohemia", "nitra",
   "principality-of-hungary", "kingdom-of-poland", "kingdom-of-hungary", "duchy-of-eczyca", "duchy-of-greater-poland",
   "duchy-of-masovia", "duchy-of-sandomierz", "duchy-of-silesia", "pomerania", "duchy-of-wroc-aw", "duchy-of-opole",
   "duchy-of-kuyavia", "kingdom-of-bohemia", "duchy-of-kalisz", "grand-duchy-of-lithuania", "duchy-of-g-ogow",
   "duchies-of-poland", "duchy-of-jawor", "duchy-of-legnica", "grand-duchy-of-krakow", "duchy-of-bytom",
   "duchy-of-raciborz", "margraviate-of-moravia", "house-of-jagiellon", "eastern-hungarian-kingdom",
   "polish-lithuanian-commonwealth", "principality-of-transylvania", "pro-swedish-poland",
   "principality-of-upper-hungary")
_o("eu-16", "volga-bulgaria", "rus", "kievan-rus", "halych-volhynia-occupation", "novgorod-republic",
   "principality-of-chernigov", "principality-of-kiev", "principality-of-peremyshl", "principality-of-pereyaslavl",
   "principality-of-polotsky", "principality-of-rostov-suzdal", "principality-of-smolensk", "principality-of-volhynia",
   "principality-of-terebovlia", "principality-of-ryazan", "principality-of-drutsk", "principality-of-jersika",
   "principality-of-koknese", "principality-of-minsk", "principality-of-vitebsk", "principality-of-halych",
   "principality-of-turov-and-pinsk", "principality-of-galicia-volhynia", "pskov-republic", "galicia-volhynia",
   "grand-principality-of-moscow", "nizhny-novgorod", "principality-of-beloozero", "principality-of-pinsk",
   "principality-of-turov", "principality-of-vladimir-suzdal", "tver", "ryazan", "tsardom-of-russia", "don-cossacks",
   "nalyvaiko-uprising", "zaporozhian-cossacks", "sloboda-ukraine")
_o("eu-17", "russian-empire", "russian-republic", "republics-of-the-soviet-union", "union-of-soviet-socialist-republics",
   "ukrainian-people-s-republic", "provisional-priamurye-government")
_o("eu-18", "first-bulgarian-empire", "duchy-of-croatia", "principality-of-serbia", "kingdom-of-croatia",
   "great-principality-of-duklja", "kingdom-of-duklja", "grand-principality-of-serbia", "banate-of-bosnia",
   "kingdom-of-serbia", "second-bulgarian-empire", "kingdom-of-syrmia", "principality-of-wallachia",
   "principality-of-valona", "serbian-empire", "despotate-of-dobruja", "despotate-of-vidin", "principality-of-moldavia",
   "albanian-principalities", "serbian-despots", "kingdom-of-bosnia", "republic-of-ragusa",
   "principality-of-valona-and-kanina", "duchy-of-saint-sava", "house-of-anjou-sicily", "serbs", "montenegro",
   "first-hellenic-republic", "united-principalities-of-moldavia-and-wallachia", "principality-of-bulgaria",
   "cretan-state", "albania")
_o("eu-19", "kingdom-of-urartu", "kingdom-of-armenia", "colchis", "caucasian-albania", "caucasian-iberia", "lazica",
   "georgia", "balasagan", "kingdom-of-lazica", "principality-of-iberia", "kingdom-of-the-iberians", "shirvan",
   "bagratid-armenia", "kingdom-of-vaspurakan", "kingdom-of-georgia", "kingdom-of-kartli", "kingdom-of-imereti",
   "kingdom-of-kakheti", "principality-of-abkhazia", "principality-of-guria", "principality-of-mingrelia",
   "samtskhe-saatabago", "principality-of-svaneti", "khanates-of-the-caucasus", "caucasian-imamate", "armenia",
   "azerbaijan-democratic-republic", "republic-of-armenia", "republic-of-azerbaijan", "chechen-republic")
_o("eu-20", "french-first-republic", "french-directory", "cisalpine-republic", "grand-duchy-of-tuscany",
   "ligurian-republic", "republic-of-san-marino", "helvetic-republic", "revolutionary-roman-republic",
   "cispadane-republic", "french-consulate", "septinsular-republic", "electorate-of-baden", "electorate-of-hesse",
   "electorate-of-salzburg", "electorate-of-wurttemberg", "italian-republic", "kingdom-of-etruria", "kingdom-of-hanover",
   "first-french-empire", "austrian-empire", "duchy-of-anhalt", "duchy-of-mecklenburg", "duchy-of-nassau",
   "duchy-of-oldenburg", "free-city-of-bremen", "free-city-of-lubeck", "grand-duchy-of-baden", "grand-duchy-of-berg",
   "grand-duchy-of-hesse", "grand-duchy-of-saxe-weimar-eisenach", "grand-duchy-of-wurzburg", "kingdom-of-bavaria",
   "kingdom-of-saxony", "kingdom-of-wurttemberg", "principality-of-hohenzollern-sigmaringen", "principality-of-lippe",
   "principality-of-regensberg", "principality-of-reuss-gera", "principality-of-waldeck-and-pyrmont", "saxe-altenburg",
   "confederation-of-the-rhine", "duchy-of-warsaw", "free-city-of-danzig", "kingdom-of-westphalia", "bessarabia",
   "duchy-of-brunswick", "free-city-of-hamburg", "kingdom-of-norway",
   "sovereign-principality-of-the-united-netherlands", "bourbon-kingdom-of-france", "duchy-of-modena-and-reggio",
   "duchy-of-parma-and-piacenza", "free-city-of-krakow", "german-confederation", "kingdom-of-monaco",
   "kingdom-of-the-two-sicilies", "netherlands", "principality-of-andorra", "united-kingdoms-of-sweden-and-norway",
   "free-city-of-frankfurt", "principality-of-lichtenberg", "principality-of-schwarzburg-sonderhausen",
   "saxe-meiningen", "kingdom-of-belgium", "poles", "saxe-coburg-and-gotha", "duchy-of-holstein",
   "french-second-republic", "italian-nationalists", "hungarian-nationalists", "republic-of-baden",
   "second-french-empire", "austria-hungary", "north-german-confederation", "french-third-republic", "german-empire",
   "first-spanish-republic", "luxembourg", "batavian-republic", "portuguese-republic", "first-french-colonial-empire")
_o("eu-21", "kingdom-of-iceland", "polish-armed-forces", "republic-of-finland", "serbia", "czechoslovakia", "estonia",
   "hungarian-republic", "kingdom-of-lithuania", "kingdom-of-romania", "republic-of-austria", "second-polish-republic",
   "yugoslavia", "republic-of-latvia", "weimar-republic", "irish-free-state", "second-spanish-republic", "nazi-germany",
   "spanish-nationalists", "eire", "francoist-spain", "vichy-france", "independent-state-of-croatia",
   "yugoslav-partisans", "estado-novo", "free-french")
_o("eu-22", "denmark", "french-fourth-republic", "kingdom-of-greece", "people-s-socialist-republic-of-albania",
   "republic-of-iceland", "republic-of-italy", "second-republic-of-austria",
   "socialist-federal-republic-of-yugoslavia", "hungary", "kingdom-of-bulgaria", "people-s-republic-of-bulgaria",
   "socialist-republic-of-romania", "german-democratic-republic", "federal-republic-of-germany",
   "hungarian-people-s-republic", "republic-of-poland", "republic-of-cyprus", "greek-junta", "malta", "portugal",
   "third-hellenic-republic", "turkish-republic-of-northern-cyprus", "republic-of-lithuania", "romania",
   "federated-republic-of-germany", "republic-of-albania", "republic-of-bulgaria", "bosnia-and-herzegovina",
   "czech-republic", "former-yugoslav-republic-of-macedonia", "republic-of-belarus", "republic-of-croatia",
   "republic-of-estonia", "republic-of-moldova", "republic-of-slovenia", "russian-occupied-territories",
   "serbia-montenegro", "slovakia", "ukraine", "kosovo", "republic-of-serbia", "russian-federation",
   "french-fifth-republic", "british-overseas-territories", "rel-commonwealth-of-nations")
# Middle East
_o("me-01", "sumerian-city-states", "elam", "akkadian-empire", "gutian-dynasty")
_o("me-02", "babylonia", "first-sealand-dynasty", "assyria", "neo-assyrian-empire", "assyrian-egypt",
   "neo-babylonian-empire")
_o("me-03", "early-dynastic-period-of-egypt", "old-kingdom-of-egypt", "lower-egypt", "upper-egypt",
   "middle-kingdom-of-egypt", "hyksos", "fifteenth-dynasty-of-egypt", "sixteenth-dynasty-of-egypt",
   "seventeenth-dynasty-of-egypt", "new-kingdom-of-egypt", "twenty-second-dynasty-of-egypt",
   "twenty-third-dynasty-of-egypt", "twenty-sixth-dynasty-of-egypt", "thirtieth-dynasty-of-egypt")
_o("me-04", "hittites", "mitanni", "neo-hittite-states", "phrygia", "tabal-kingdom", "lydia", "philistia", "phoenicia",
   "kingdom-of-israel", "kingdom-of-judah", "sabaeans", "hadhramaut", "minaeans", "qataban")
_o("me-05", "median-kingdom", "achaemenid-empire", "ptolemaic-kingdom", "laomedon", "perdiccas", "seleucid-empire",
   "ankhwennefer", "nabataeans", "judea", "kingdom-of-bithynia", "atropatene", "kingdom-of-pontus", "galatia",
   "kingdom-of-pergamon", "paphlagonia", "kingdom-of-sophene", "kingdom-of-cappadocia", "greco-bactrian-kingdom",
   "indo-greeks", "cyrenaica")
_o("me-06", "parthian-empire", "sasanian-empire", "himyarite-kingdom", "lakhmid-kingdom", "ghassanids",
   "kingdom-of-adiabene", "kingdom-of-commagene", "kingdom-of-gordyene", "kingdom-of-osroene", "indo-sasanian-empire")
_o("me-07", "rashidun-caliphate", "umayyad-caliphate", "dabuyid-dynasty")
_o("me-08", "abbasid-caliphate", "ziyadid-dynasty", "tulunids", "qarmatians", "buyid-dynasty",
   "abbasid-caliphate-buyid-dynasty", "sulayhid-dynasty", "najahid-dynasty", "uyunid-emirate", "zurayid-dynasty",
   "fatimid-caliphate", "samanid-empire", "saffarid-dynasty", "ghaznavid-empire", "hamdanid-emirates",
   "zaydi-alid-dynasties", "ziyarid-dynasty", "sajid-dynasty")
_o("me-09", "kingdom-of-jerusalem", "county-of-tripoli", "mahdids", "nabhani-dynasty", "ayyubid-sultanate",
   "khwarezmid-empire", "khwarezmid-dynasty", "rasulid-dynasty", "mamluk-sultanate", "bahrani-dynasty", "injuids",
   "jalayirid-sultanate", "muzaffarids", "hashemite-arab-federation", "tahirid-sultanate", "great-seljuk-empire",
   "seljuk-dynasty", "danishmendids", "sultanate-of-rum", "armenian-kingdom-of-cilicia", "county-of-edessa",
   "principality-of-antioch", "kingdom-of-cyprus", "zengid-dynasty", "ahi-republic", "beylik-of-aydin",
   "beylik-of-hamid", "beylik-of-isfendiyar", "beylik-of-karaman", "beylik-of-karasi", "beylik-of-menteshe",
   "beylik-of-sinop", "eshrefids", "germiyanids", "kastamonu", "beylik-of-saruhan", "beylik-of-teke",
   "beylik-of-dulkadir", "chobanids", "sarbadars", "qara-qoyunlu", "ramadanid-emirate", "aq-qoyunlu", "kartids")
_o("me-10", "ottoman-empire", "safavid-dynasty", "yarubid-dynasty", "qasimids", "afsharid-iran", "emirate-of-diriyah",
   "sultanate-of-oman", "zand-dynasty", "bahrain", "kuwait", "house-of-khalifa", "qajar-dynasty",
   "muhammad-ali-dynasty", "imamate-of-yemen", "qatar-dynasty", "trucial-states", "emirate-of-nejd",
   "emirate-of-jabal-shammar", "khedivate-of-egypt", "sultanate-of-muscat-and-oman", "imamate-of-oman", "qatar",
   "kingdom-of-hejaz", "asir", "north-yemen", "kingdom-of-egypt", "pahlavi-dynasty", "kingdom-of-hejaz-and-nejd",
   "kingdom-of-iraq", "kingdom-of-saudi-arabia", "lebanon", "kingdom-of-jordan", "qatar-protectorate", "palestinians",
   "state-of-israel", "republic-of-egypt", "arab-federation", "united-arab-republic", "iraqi-republic",
   "state-of-kuwait", "people-s-democratic-republic-of-yemen", "arab-republic-of-egypt", "kingdom-of-bahrain",
   "state-of-qatar", "united-arab-emirates", "islamic-republic-of-iran", "republic-of-yemen", "gaza-hamas",
   "republic-of-iraq", "french-mandate-for-syria-and-lebanon", "republic-of-turkey", "second-syrian-republic",
   "republic-of-syria", "ba-athist-syria", "arab-socialist-ba-ath-party", "syria")
# East Asia
_o("ea-01", "minyue")
_o("ea-02", "protectorate-of-the-western-regions", "nanyue", "han-dynasty", "xin-dynasty", "qin-dynasty")
_o("ea-03", "cao-cao", "eastern-wu", "cao-wei", "shu-han", "tuyuhun")
_o("ea-04", "gao-kaidao", "tang-dynasty", "nanzhao", "former-shu", "later-jin", "later-liang-dynasty", "min",
   "qi-kingdom", "southern-chu", "southern-han", "southern-wu", "wuyue", "yan-kingdom", "former-jin", "jingnan",
   "later-tang", "later-shu", "later-han", "northern-han", "southern-tang", "tibetan-empire", "tibetans")
_o("ea-05", "liao-dynasty", "kingdom-of-dali", "northern-song", "western-xia", "great-jin", "southern-song")
_o("ea-06", "yuan-dynasty", "tibet")
_o("ea-07", "ming-dynasty", "li-zicheng", "southern-ming")
_o("ea-08", "later-jin-dynasty", "qing-dynasty", "taiping-heavenly-kingdom", "panthay-rebellion", "republic-of-china",
   "empire-of-china", "kuomintang", "chinese-communists", "anti-kuomintang-coalition", "communist-party-of-china",
   "people-s-republic-of-china")
# Inner Asia
_o("ia-01", "scythia", "xiongnu", "southern-xiongnu", "xianbei", "rouran-khaganate", "yuezhi", "wusun", "great-yuan",
   "kidarites", "xionites", "white-huns", "gokturk-khaganate", "western-gokturks", "eastern-gokturks", "turks",
   "turgesh", "uyghur-khaganate", "kimek-kipchak-confederation", "qarlugs", "kara-khanids", "qocho-kingdom",
   "kingdom-of-khotan", "eastern-kara-khanids", "western-karakhanid-khanate", "kara-khitans", "khazaria",
   "old-great-bulgaria", "oghuz-turks", "cuman-kipchak-confederation", "yenisei-kyrgyz", "ganzhou-kingdom")
_o("ia-02", "mongol-empire", "chagatai-khanate", "golden-horde", "white-horde", "timurid-empire", "east-turkestan",
   "moghulistan", "kapisa", "eastern-chagatai-khanate", "ilkhanate", "northern-yuan", "mongol-khanate", "four-oirats",
   "khanate-of-sibir", "blue-horde", "khanate-of-kazan", "crimean-khanate", "nogai-horde", "qasim-khanate",
   "astrakhan-khanate")
_o("ia-03", "kazakh-khanate", "shaybanids", "khanate-of-bukhara", "eastern-moghulistan", "western-moghulistan",
   "dzungar-khanate", "oirat-confederation", "khanate-of-kokand", "emirate-of-bukhara", "east-turkestan-republic",
   "kazakhstan", "kyrgyzstan", "republic-of-tajikistan", "republic-of-uzbekistan", "turkmenistan", "tumed",
   "khoshut-khanate", "republic-of-uryankhay", "great-mongol-state", "mongolian-people-s-republic", "mongolia",
   "hotaki-dynasty", "durrani-empire", "emirate-of-afghanistan", "durrani-dynasty", "kingdom-of-afghanistan",
   "republic-of-afghanistan", "afghanistan", "mujahideen", "taliban", "khanate-of-khiva", "kalmyk-khanate",
   "small-horde")
# Japan and Korea
_o("jk-01", "shunten-dynasty", "chuzan", "hokuzan", "nanzan", "ryukyu-kingdom", "empire-of-japan")
_o("jk-02", "gojoseon", "korean-jin", "byeonhan", "dongye", "jinhan", "mahan", "dong-okjeo", "goguryeo", "tamna",
   "baekje", "silla", "unified-silla", "balhae", "hubaekje", "taebong", "goryeo", "joseon", "korean-empire",
   "democratic-people-s-republic-of-korea", "republic-of-korea")
# South Asia
_o("sa-02", "indo-scythians", "kushan-empire", "western-kushans", "indo-parthians", "kalinga", "maurya-empire")
_o("sa-03", "karkota-dynasty", "utpala-dynasty", "lohara-dynasty", "sind-habbari-dynasty", "turk-shahis",
   "chandra-dynasty")
_o("sa-04", "ghurid-dynasty", "kathmandu", "mamluk-dynasty")
_o("sa-05", "sikh-confederacy", "nepal", "sikh-empire", "talpur-dynasty", "mughal-empire", "hussain-shahi-dynasty")
_o("sa-06", "french-india", "portuguese-ceylon", "dutch-ceylon", "british-empire", "danish-india", "british-ceylon",
   "kashmir-and-jammu", "british-raj", "portuguese-colonies")
# South-east Asia
_o("se-01", "au-lac", "trung-sisters", "burma", "pagan-kingdom", "kingdom-of-mrauk-u", "cambodia", "lan-na",
   "chiangmai", "rattanakosin-kingdom")
_o("se-02", "maynila", "sultanate-of-brunei", "mataram-kingdom", "kahuripan", "kediri-kingdom", "kingdom-of-janggala",
   "singhasari", "demak-sultanate", "blambangan-kingdom", "sultanate-of-banjar", "kingdom-of-pajana",
   "mataram-sultanate", "sultanate-of-sukadana", "balinese-kingdom", "bali", "patani-kingdom")
_o("se-03", "dutch-east-indies", "kingdom-of-sarawak", "french-indochina", "sultan-of-yogyakarta", "surakarta-sunanate")
_o("se-04", "kingdom-of-thailand")
# Africa
_o("af-01", "kingdom-of-kush", "kingdom-of-axum", "alodia", "makuria", "nobatia", "zagwe-dynasty", "ethiopian-empire",
   "makuria-kingdom", "funj-sultanate", "ifat-sultanate", "adal-sultanate", "sultanate-of-harar",
   "majeerteen-sultanate", "sultanate-of-hobyo", "mahdist-state", "ethiopia")
_o("af-02", "phoenician-colonies", "carthage", "mauretania", "kingdom-of-numidia", "fihrids", "kharijites",
   "rustamid-dynasty", "barghawata-conference", "idrisids", "aghlabid-dynasty", "emirate-of-nekor", "almoravid-dynasty",
   "zirid-dynasty", "almohad-caliphate", "kingdom-of-africa", "hafsid-dynasty", "marinid-sultanate", "wattasid-dynasty",
   "saadi-sultanate", "morocco", "karamanli-dynasty", "ottoman-tripolitania", "hammadid-dynasty", "zayyanid-dynasty",
   "beylik-of-tunis", "regency-of-algiers")
_o("af-03", "ghana-empire", "takrur", "sosso-empire", "mali-empire", "bornu-empire", "songhai-empire", "empire-of-kanem",
   "sultanate-of-darfur", "wadai-empire", "bamana-empire", "massina-empire", "sokoto-caliphate")
_o("af-04", "oyo-empire", "dutch-gold-coast", "danish-gold-coast", "ashanti-empire", "freetown-colony",
   "republic-of-liberia")
_o("af-05", "omani-slave-coast", "people-s-republic-of-zanzibar")
_o("af-06", "kingdom-of-kongo", "kingdom-of-lunda")
_o("af-07", "dutch-cape-colony", "merina-kingdom", "british-cape-colony", "napoleonic-batavia-republic", "zululand",
   "natalia-republic", "free-orange-state", "south-african-republic", "nieuwe-republiek", "swaziland")
_o("af-08", "british-africa", "italian-africa", "state-of-eritrea", "portuguese-africa", "republic-of-the-rif",
   "french-africa", "kamerun", "german-africa", "british-gold-coast", "belgian-congo", "south-africa",
   "french-algeria", "tangier-international-zone", "british-east-africa")
# Americas
_o("am-01", "olmec-civilization", "zapotec-civilization", "teotihuacan", "classic-veracruz-culture")
_o("am-02", "mayan-city-states", "later-mayan-city-states", "itza-mayans")
_o("am-03", "toltec", "texcoco", "michoacan", "tenochtitlan", "aztec-triple-alliance")
_o("am-04", "chimor", "chimu-empire", "cuzco", "inca-empire")
_o("am-05", "puebloans-chaco-regional-system", "puebloans-aztec-regional-system", "haudenosaunee")
_o("am-06", "spanish-empire", "portuguese-empire", "france-antarctique", "jesuit-reducciones", "new-netherland",
   "french-colony-of-guiana", "french-louisiana", "netherlands-antilles")
_o("am-07", "english-colonial-empire", "new-france", "new-sweden", "united-states-of-america", "vermont-republic",
   "republic-of-texas", "california-republic", "confederate-states-of-america", "canada")
_o("am-08", "haiti", "empire-of-haiti", "mexicans", "mosquito-kingdom", "republic-of-baja-california")
# Oceania
_o("oc-01", "kingdom-of-hawai-i", "kingdom-of-fiji")
_o("oc-02", "new-caledonia", "new-hebrides", "commonwealth-of-australia", "vanuatu", "republic-of-hawai-i",
   "republic-of-fiji", "new-zealand", "papua-new-guinea", "solomon-islands", "micronesia", "palau")
# Umbrella entities whose main component is not a leaf of the same name
_o("ea-01", "rel-spring-and-autumn-states", "rel-warring-states-china")
_o("ea-02", "rel-eighteen-kingdoms")
_o("ea-04", "rel-five-dynasties-and-ten-kingdoms")
_o("eu-12", "rel-taifas-of-iberia", "rel-spanish-empire", "rel-portuguese-empire",
   "rel-personal-union-of-spanish-empire-with-habsburg-monarchy")
_o("eu-15", "rel-polish-lithuania-kingdom")
_o("eu-11", "rel-british-empire")
_o("sa-04", "rel-delhi-sultanate")

# Relation-name parsers (umbrella = 1 rows)
REL_RE = [
    re.compile(r"^\((?:Allegiance|Vassalage) of (.+?) to (.+)\)$"),
    re.compile(r"^\(Alliance between (.+?) and (.+)\)$"),
    re.compile(r"^\(Personal union of (.+?) with (.+)\)$"),
]


def main():
    check = "--check" in sys.argv
    with open(POLITIES_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_slug = {r["slug"]: r for r in rows}
    by_name = {r["name"]: r for r in rows}

    # Pass 1: leaves
    owner = {}
    for r in rows:
        if r["umbrella"] == "1":
            continue
        owner[r["slug"]] = OVERRIDES.get(r["slug"]) or rule(r)

    # Pass 2: umbrella and relation entities -> main component's group
    umbrella_main = {}
    for r in rows:
        if r["umbrella"] != "1":
            continue
        s = r["slug"]
        if s in OVERRIDES:
            owner[s] = OVERRIDES[s]
            umbrella_main[s] = "override"
            continue
        name = r["name"]
        main = None
        for rx in REL_RE:
            m = rx.match(name)
            if m:
                main = m.group(1)
                break
        if main is None:
            main = name[1:-1]  # "(Kingdom of France)" -> "Kingdom of France"
        ms = by_name.get(main, {}).get("slug") or slugify(main)
        if ms not in owner:
            # try the components list
            comps = [c for c in r["components"].split(";") if c]
            cand = [by_name[c]["slug"] for c in comps if c in by_name and by_name[c]["slug"] in owner]
            if cand:
                ms = cand[0]
        if ms not in owner:
            raise SystemExit(f"umbrella {s}: main component {main!r} ({ms}) not found; add an override")
        owner[s] = owner[ms]
        umbrella_main[s] = ms

    unassigned = [r["slug"] for r in rows if r["slug"] not in owner]
    bad = [s for s, g in owner.items() if g not in GROUP_IDS]
    assert not bad, bad

    gmeta = {g[0]: g for g in GROUPS}
    owned = defaultdict(list)
    for s, g in owner.items():
        owned[g].append(s)
    leaf_slugs = [r["slug"] for r in rows if r["umbrella"] != "1"]

    # Context: the 25 km neighbour lists of data/polities/<slug>.json (built by build_tables.py),
    # cached in scratch because every read of the shared folder downloads the file.
    # Falls back to bbox proximity from shapes.csv when the polity files are missing.
    neighbours = load_neighbours(leaf_slugs)
    if neighbours is None:
        neighbours = bbox_neighbours(by_slug, leaf_slugs)

    context = {}
    for gid in GROUP_IDS:
        ef, et = gmeta[gid][3], gmeta[gid][4]
        mine = [s for s in owned[gid] if by_slug[s]["umbrella"] != "1"]
        ctx = set()
        if gid == "xx-01":
            ctx = {s for s in leaf_slugs if int(by_slug[s]["first_year"]) <= -2500}
        else:
            for s in mine:
                for (o, nf, nt) in neighbours.get(s, []):
                    if o in owner and owner[o] != gid and nt >= ef and nf <= et:
                        ctx.add(o)
        context[gid] = sorted(ctx)

    out = []
    for g in GROUPS:
        gid, region, name, ef, et, scope = g
        pol = sorted(owned[gid], key=lambda s: (int(by_slug[s]["first_year"]), s))
        out.append({"id": gid, "region": region, "name": name, "era_from": ef, "era_to": et, "scope": scope,
                    "polities": pol, "context": context[gid]})

    counts = {gid: sum(1 for s in owned[gid] if by_slug[s]["umbrella"] != "1") for gid in GROUP_IDS}
    totals = {gid: len(owned[gid]) for gid in GROUP_IDS}

    if check:
        for o in out:
            print(f"== {o['id']} {o['name']} [{o['era_from']}..{o['era_to']}] owned {totals[o['id']]} "
                  f"(leaf {counts[o['id']]}) context {len(o['context'])}")
            print("   " + ", ".join(o["polities"]))
        print("unassigned:", unassigned)
        print("umbrella->main:", json.dumps(umbrella_main, indent=0)[:4000])
        return

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    lines = ["# Research groups", "",
             "Generated by `tools/research_groups.py` from data/polities.csv (Cliopatria v0.2.1). One row per group of the "
             "master plan's roster; *owned* counts every Cliopatria Name assigned to the group (umbrella and relation "
             "entities included, in parentheses the leaf polities only); *context* counts the polities of other groups "
             "that are 25 km neighbours of an owned polity (data/polities/<slug>.json) in an overlapping year of the "
             "group's era. Groups owning more than about 45 are forced by the plan's split and are listed below the table. "
             "Full lists in research-groups.json.", "",
             "| id | name | era | owned (leaf) | context | five largest by max_area_km2 |",
             "| --- | --- | --- | --- | --- | --- |"]
    for o in out:
        gid = o["id"]
        leaves = [s for s in o["polities"] if by_slug[s]["umbrella"] != "1"]
        top = sorted(leaves, key=lambda s: -float(by_slug[s]["max_area_km2"]))[:5]
        era = f"{fmt_year(o['era_from'])} to {fmt_year(o['era_to'])}"
        lines.append(f"| {gid} | {o['name']} | {era} | {totals[gid]} ({counts[gid]}) | {len(o['context'])} | "
                     + ", ".join(top) + " |")
    over = [f"{gid} ({n})" for gid, n in totals.items() if n > 45]
    lines += ["", f"Groups: {len(out)}. Polities assigned: {len(owner)} of {len(rows)}; unassigned: {len(unassigned)}.",
              f"Groups over 45 owned: {', '.join(over) if over else 'none'}.",
              "Groups owning nothing (cross-cutting, by design): "
              + ", ".join(gid for gid, n in totals.items() if n == 0) + ".", ""]
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    vals = sorted(totals.values())
    report = {"groups": len(out), "assigned": len(owner), "unassigned": unassigned,
              "owned_min": vals[0], "owned_median": statistics.median(vals), "owned_max": vals[-1],
              "over_45": {gid: n for gid, n in totals.items() if n > 45},
              "zero_owned": [gid for gid, n in totals.items() if n == 0],
              "context_sizes": {gid: len(context[gid]) for gid in GROUP_IDS}}
    print(json.dumps(report, indent=1))


def fmt_year(y):
    return f"{-y} BCE" if y < 0 else str(y)


CACHE_DIR = "/tmp/claude-0/work/research-groups"
POLITY_DIR = os.path.join(ROOT, "data", "polities")


def load_neighbours(leaf_slugs):
    """slug -> [(neighbour_slug, from, to)] from data/polities/<slug>.json, cached in scratch."""
    cache = os.path.join(CACHE_DIR, "neighbours.json")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            data = json.load(f)
        if len(data) >= len(leaf_slugs):
            return {k: [tuple(x) for x in v] for k, v in data.items()}
    if not os.path.isdir(POLITY_DIR):
        return None
    data = {}
    for s in leaf_slugs:
        p = os.path.join(POLITY_DIR, s + ".json")
        if not os.path.exists(p):
            return None
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        data[s] = [(n["slug"], int(n["from"]), int(n["to"])) for n in d.get("neighbours", [])]
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(cache, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return data


def bbox_neighbours(by_slug, leaf_slugs, buf=1.0):
    """Fallback: shapes whose bboxes come within `buf` degrees in an overlapping year."""
    shapes = defaultdict(list)
    with open(SHAPES_CSV, encoding="utf-8") as f:
        for sh in csv.DictReader(f):
            if by_slug[sh["slug"]]["umbrella"] == "1":
                continue
            b = [float(x) for x in sh["bbox"].split(",")]
            shapes[sh["slug"]].append((int(sh["from_year"]), int(sh["to_year"]), b))
    out = defaultdict(list)
    for i, a in enumerate(leaf_slugs):
        for b_ in leaf_slugs[i + 1:]:
            span = None
            for (f1, t1, b1) in shapes[a]:
                for (f2, t2, b2) in shapes[b_]:
                    if f1 <= t2 and f2 <= t1 and (b1[0] - buf <= b2[2] and b2[0] - buf <= b1[2]
                                                  and b1[1] - buf <= b2[3] and b2[1] - buf <= b1[3]):
                        lo, hi = max(f1, f2), min(t1, t2)
                        span = (lo, hi) if span is None else (min(span[0], lo), max(span[1], hi))
            if span:
                out[a].append((b_, span[0], span[1]))
                out[b_].append((a, span[0], span[1]))
    return out


if __name__ == "__main__":
    main()
