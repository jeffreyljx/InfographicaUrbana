import csv, re, unicodedata, json
ISO={'Algeria':'dz','Argentina':'ar','Armenia':'am','Australia':'au','Austria':'at','Azerbaijan':'az','Bangladesh':'bd','Belarus':'by','Belgium':'be','Brazil':'br','Bulgaria':'bg','Canada':'ca','Chile':'cl','China':'cn','Colombia':'co','Czech Republic':'cz','Denmark':'dk','Dominican Republic':'do','Ecuador':'ec','Egypt':'eg','Finland':'fi','France':'fr','Georgia':'ge','Germany':'de','Greece':'gr','Hungary':'hu','India':'in','Indonesia':'id','Iran':'ir','Italy':'it','Japan':'jp','Kazakhstan':'kz','Malaysia':'my','Mexico':'mx','Netherlands':'nl','Nigeria':'ng','North Korea':'kp','Norway':'no','Pakistan':'pk','Panama':'pa','Peru':'pe','Philippines':'ph','Poland':'pl','Portugal':'pt','Qatar':'qa','Romania':'ro','Russia':'ru','Saudi Arabia':'sa','Singapore':'sg','South Korea':'kr','Spain':'es','Sweden':'se','Switzerland':'ch','Taiwan':'tw','Thailand':'th','Turkey':'tr','Ukraine':'ua','United Arab Emirates':'ae','United Kingdom':'gb','United States':'us','Uzbekistan':'uz','Venezuela':'ve','Vietnam':'vn'}
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
OVR={'Mass Transit Railway':'hk-mtr','Hong Kong':'hk','Macau Light Rapid Transit':'mo-macau-lrt','Chicago "L"':'us-chicago-l',
 'SEPTA Metro: L, B, M':'us-septa-metro','Red Line (RTA Rapid Transit)':'us-cleveland-rta-red-line','Metro Rail':'us-la-metro-rail',
 'Metrorail':'us-miami-metrorail','Skyline':'us-honolulu-skyline','MBTA subway':'us-mbta-subway','Washington Metro':'us-wmata-metro',
 'Mass Rapid Transit':'sg-mrt','SkyTrain':'ca-vancouver-skytrain','Toronto subway':'ca-toronto-subway','SITEUR':'mx-guadalajara-siteur',
 'Metrorrey':'mx-monterrey-metrorrey','Rapid KL':'my-kuala-lumpur-rapid-kl','Metropolitan Rapid Transit':'th-bangkok-mrt','BTS Skytrain':'th-bangkok-bts',
 'Shinbundang Line (Neo Trans)':'kr-shinbundang-line','Namma Metro':'in-bengaluru-namma-metro','Bursaray':'tr-bursaray','Federal District Metro':'br-brasilia-metro',
 'Tren Urbano':'us-san-juan-tren-urbano','PATH':'us-path','BART':'us-bart','MARTA':'us-marta','Metro Valencia':'ve-valencia-metro','Lima and Callao Metro':'pe-lima-metro',
 'Réseau express métropolitain':'ca-montreal-rem','Mashhad Urban Railway':'ir-mashhad-metro','Astram Line':'jp-hiroshima-astram-line','Lagos Rail Mass Transit':'ng-lagos-rail-mass-transit',
 'Manila Light Rail Transit System':'ph-manila-lrt','Manila Metro Rail Transit System':'ph-manila-mrt','Dhaka Metro Rail':'bd-dhaka-metro-rail','Docklands Light Railway':'gb-london-dlr'}
# Rulings from metro-definition.md v1.1 (section 9) applied at system level; line-level rulings are applied by the line pass
RUL={
 'Wuhu Rail Transit':('out','T1','Both lines are straddle monorails (Jeffrey 05:27 ruling)'),
 'Mecca Metro':('out','T5','Runs only during the Hajj season, not every day (new ruling, this thread)'),
 'Rinkai Line':('out','T7','Definition 9.3: extension of JR Saikyo services'),
 'Minatomirai Line':('out','T7','Definition 9.3: extension of the Tokyu Toyoko Line'),
 'Wenzhou Rail Transit':('out','T7','Definition 9.3: presented as suburban railway (市域铁路)'),
 'Taizhou Rail Transit':('check','T7','Line S1 is a 市域铁路 like Wenzhou S1; default out unless it runs under metro identity'),
 'Jinhua Rail Transit':('check','T7','Jinyi-Dong lines: apply the China express rule (in, tagged express, if metro-branded; out if presented as 市域铁路)'),
 'Chongqing Rail Transit':('partial','T1','Lines 2 and 3 are monorails and are out'),
 'Rapid KL':('partial','T1/T7','KL Monorail out; KLIA Ekspres/Transit are not part of Rapid KL'),
 'São Paulo Metro':('partial','T1','Lines 15 and 17 are monorails and are out'),
 'Metropolitan Rapid Transit':('partial','T1','Yellow and Pink lines are monorails and are out'),
 'Daegu Metro':('partial','T1','Line 3 is a monorail and is out'),
 'Seoul Metropolitan Subway':('partial','T7','Korail-run sections of Lines 1, 3, 4 in; Korail own lines, AREX, GTX-A out'),
 'Mass Transit Railway':('partial','T6','Disneyland Resort line out; Light Rail out'),
 'London Underground':('in','','Definition 9.1: from 10 Jan 1863 (Metropolitan Railway), not 1890'),
 'New York City Subway':('in','','Definition 9.1: elevated railways from first public service (1870); demolished Els kept with closing dates'),
 'Chicago "L"':('in','','From 6 Jun 1892; closed branches kept'),
 'MBTA subway':('partial','T3','Red, Orange, Blue in (Main Line El from 10 Jun 1901); Green and Mattapan out'),
 'Toronto subway':('partial','T3','Lines 1, 2, 4 in; Line 3 in 1985-2023; Lines 5, 6 out'),
 'Vienna U-Bahn':('in','','Definition 9.1: electric Stadtbahn from 4 Jun 1925'),
 'Athens Metro':('in','','Line 1 from 16 Sep 1904 (electrification)'),
 'Buenos Aires Underground':('partial','T3','Premetro (tram) out'),
 'Medellín Metro':('partial','T1/T3','Lines A, B in; Metrocable and tram out'),
 'SITEUR':('partial','T3','Lines 1-3 in (check crossings); Line 4 to test'),
 'Rotterdam Metro':('in','','Check that each line has 10 or fewer priority crossings'),
 'Lausanne Metro':('partial','T3','m2 in from 27 Oct 2008; m1 out'),
 'Recife Metro':('partial','T3/T7','Diesel VLT lines to test'),
 'Cairo Metro':('check','T3','Line 1 at-grade running to check'),
 'Mashhad Urban Railway':('check','T3','Line 1 at-grade running to check'),
 'Kobe New Transit':('in','','AGT'),
 'Mumbai Metro':('in','','Mumbai Monorail is a separate system and out'),
 'SEPTA Metro: L, B, M':('in','','L (Market-Frankford), B (Broad Street), M (Norristown High Speed Line)'),
}
rows=[]
for ln in open('/tmp/claude-0/metro/wiki_list_raw.txt',encoding='utf8'):
    c=[x.strip() for x in ln.rstrip('\n').split('|')]
    city,country,name,op,last,st,length,rid=c
    iso=ISO[country]
    if country=='China' and city in('Hong Kong','Macau'): iso={'Hong Kong':'hk','Macau':'mo'}[city]
    sid=OVR.get(name) or f"{iso}-{slug(name)}"
    if not sid.startswith(iso+'-') and sid!='hk': sid=sid
    m=re.match(r'([\d,\.]+)\s*\(([^)]*)\)',rid)
    rm, ry = (m.group(1).replace(',',''), m.group(2)) if m else ('','')
    r=RUL.get(name,('in','',''))
    rows.append(dict(system_id=sid,system_name=name,city=city,country=country,iso2=iso.upper(),in_wikipedia_list='yes',
        opened_year_wikipedia=op,last_expansion_wikipedia=last if last!='?' else '',stations_wikipedia=st,length_km_wikipedia=length,
        annual_ridership_m=rm,ridership_year=ry,ruling=r[0],ruling_test=r[1],ruling_note=r[2]))
ADD=[
 ('gb-liverpool-overhead-railway','Liverpool Overhead Railway','Liverpool','United Kingdom','GB','1893','','','','','','in','','Definition 9.1: in, 6 Mar 1893 to 30 Dec 1956 (closed)'),
 ('de-frankfurt-u-bahn','Frankfurt U-Bahn','Frankfurt','Germany','DE','1968','','','','','','partial','T3','Definition 9.2: only U4 is in (all tunnel); 2008 Enkheim extension left out; other lines out'),
 ('es-seville-metro','Seville Metro','Seville','Spain','ES','2009','','','','','','in','','Definition 9.2: in'),
 ('es-metrovalencia','Metrovalencia','Valencia','Spain','ES','1988','','','','','','check','T3/T4','Definition 9.2: lines 1, 2 out; 3, 5, 7, 9 to test'),
 ('es-malaga-metro','Málaga Metro','Málaga','Spain','ES','2014','','','','','','check','T3','Definition 9.2: Line 1 out; Line 2 to test'),
 ('es-palma-metro','Palma Metro','Palma','Spain','ES','2007','','','','','','check','T4','Definition 9.2: M2 shared track with SFM 2013-22; to test'),
 ('gb-tyne-and-wear-metro','Tyne and Wear Metro','Newcastle','United Kingdom','GB','1980','','','','','','check','T3','Definition 9.2: out by default (unbarriered crossings) unless all lie on later extensions'),
]
for a in ADD:
    rows.append(dict(zip(['system_id','system_name','city','country','iso2','opened_year_wikipedia','last_expansion_wikipedia','stations_wikipedia','length_km_wikipedia','annual_ridership_m','ridership_year','ruling','ruling_test','ruling_note'],a),in_wikipedia_list='no'))
ids=[r['system_id'] for r in rows]
dup=[i for i in ids if ids.count(i)>1]
assert not dup, dup
json.dump(rows, open('/tmp/claude-0/metro/systems.json','w'), ensure_ascii=False, indent=0)
print(len(rows)); 
for r in rows: print(r['system_id'], '|', r['system_name'], '|', r['ruling'])
