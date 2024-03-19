import sqlite3

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

rollerIAktKM = {
    "Haakon Haakonssønn" : {1,2,3,4,5},
    "Inga fra Vartejg (Haakons mor) " : {1,3},
    "Skule jarl" : {1,2,3,4,5},
    "Fru Ragnhild (Skules hustru)" : {1,5},
    "Margrete (Skules datter)" : {1,2,3,4,5},
    "Sigrid (Skules søster) ": {1,2,5},
    " Ingebjørg" : {4},
    "Biskop Nikolas" : {1,2,3},
    "Gregorius Jonssønn" : {1,2,3,4,5},
    "Paal Flida " : {1,2,3,4,5},
    "Baard Bratte " : {2},
    "Jatgeir Skald ": {4},
    " Dagfinn Bonde" : {1,2,3,4,5},
    "Peter (prest og Ingebjørgs sønn)" : {3,4,5},    
    " Trønder" : {2,3,4}
}

rollerIAktSAAEK = {
    "Sunniva Du Mond Nordal" : {1},
    "Jo Saberniak" : {1},
    "Marte M. Steinholt" : {1},
    "Tor Ivar Hagen" : {1},
    "Trond-Ove Skrødal" : {1},
    "Natalie Grøndahl": {1},
    "Åsmund Flaten" : {1}
    }



def init_RolleIAkt():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    roller = hentRolle()
    for el in roller:
        for key in rollerIAktKM:
            if (el[1]==key):
                for i in rollerIAktKM[key]:
                    string = f'INSERT INTO RolleIAkt VALUES ({el[0]},1,{i});'
                    cursor.execute(string)
                    con.commit()
                    continue
    for el in roller:
        for key in rollerIAktSAAEK:
            if (el[1]==key):
                string = f'INSERT INTO RolleIAkt VALUES ({el[0]},2,1);'                
                cursor.execute(string)
                con.commit()
    con.close()
    return None
