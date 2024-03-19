DATABASE_PATH = './teater.db'

#Teaterstykker
# Format: {
#     id: id i databasen,
#     navn: navn på sal/scene,
#     kapasitet : antall billetter som kan selges,
#     omraader : liste over områder på formatet:
#       { områdenavn : (rader, seterPerRad)} eller
#       { områdenavn : [Rad1AntallSeter,Rad2AntallSeter...]}
# 
#          
# }


HOVED_SCENE = {
    'id' : 1,
    'navn' : "Hovedscenen",
    'kapasitet' : 524,
    'omraader' : [
        {'' : (18,28)},
        {'Galleri' : (4,5)}
        ]}

GAMLE_SCENE = {
    'id' : 2,
    'navn' : "Gamle Scene",
    'kapasitet' : 332,
    'omraader' : [
        {'Parkett' : [18,16,17,18,18,17,18,17,17,14]},
        {'Balkong' : [28,27,22,17]},
        {'Galleri': [33,18,17]}
        ]}

STUDIO_SCENEN = {
    'id' : 3,
    'navn' : "Studio Scenen",
    'kapasitet' : 150,
    'omraader' : []}

TEATER_KJELLEREN = {
    'id' : 4,
    'navn' : "Teater Kjelleren",
    'kapasitet' : 60,
    'omraader' : []}

TEATER_CAFEEN = {
    'id' : 5,
    'navn' : "Teater Caféen",
    'kapasitet' : 100,
    'omraader' : []}

SALER = [HOVED_SCENE, GAMLE_SCENE, STUDIO_SCENEN, TEATER_KJELLEREN, TEATER_CAFEEN]

#Teaterstykker
# Format: {
#     id: id i databasen,
#     apiurl : url til data fra api,
#     navn: tittel på stykke,
#     startTid : klokkeslett,
#     forfatter : navn på forfatter,
#     akter : liste over akt navn, dersom en akt heter '' kalles den Akt + aktid,
# }

KONGSEMNENE = {
    'id' : 1,
    'apiURL' : "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene",
    'navn' : "Kongsemnene",
    'startTid' : "18:30",
    'forfatter' : "Henrik Ibsen",
    'akter' : ['','','','',''],
    'visesI' : HOVED_SCENE,
    'oppsetninger' : ["1. februar", "2. februar", "3. februar", "5. februar", "6. februar"],
    'rolleIAkt': {
        "Haakon Haakonssønn" : {1,2,3,4,5},
        "Inga fra Vartejg (Haakons mor)" : {1,3},
        "Skule jarl" : {1,2,3,4,5},
        "Fru Ragnhild (Skules hustru)" : {1,5},
        "Margrete (Skules datter)" : {1,2,3,4,5},
        "Sigrid (Skules søster)": {1,2,5},
        "Ingebjørg" : {4},
        "Biskop Nikolas" : {1,2,3},
        "Gregorius Jonssønn" : {1,2,3,4,5},
        "Paal Flida" : {1,2,3,4,5},
        "Baard Bratte" : {2},
        "Jatgeir Skald": {4},
        "Dagfinn Bonde" : {1,2,3,4,5},
        "Peter (prest og Ingebjørgs sønn)" : {3,4,5},    
        "Trønder" : {2,3,4}
    }
}

STORST_AV_ALT_ER_KJAERLIGHETEN = {
    'id' : 2,
    'apiURL' : "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten",
    'navn' : "Størst av alt er kjærligheten",
    'startTid' : "19:30",
    'forfatter' : "Jonas Corell Petersen",
    'akter' : [''],
    'visesI' : GAMLE_SCENE,
    'oppsetninger' : ["3. februar", "6. februar", "7. februar", "12. februar", "13. februar", "14. februar"],
    'rolleIAkt' : {
        "Sunniva Du Mond Nordal" : {1},
        "Jo Saberniak" : {1},
        "Marte M. Steinholt" : {1},
        "Tor Ivar Hagen" : {1},
        "Trond-Ove Skrødal" : {1},
        "Natalie Grøndahl": {1},
        "Åsmund Flaten" : {1} 
    }
}



TEATERSTYKKER = [KONGSEMNENE, STORST_AV_ALT_ER_KJAERLIGHETEN]


