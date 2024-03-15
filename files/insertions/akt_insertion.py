import sqlite3
from ansatt_insertion import getData


urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

def getTeaterStykkeID():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute('''
                    SELECT TeaterStykkeID, Navn from TeaterStykke;
                    ''')
    data = cursor.fetchall()
    con.close()
    return data

def AktList():
    lstKM = [1,2,3,4,5]
    lstSAAEK = 1
    rendered_aktList = []
    teaterstykker = getTeaterStykkeID()
    for el in lstKM:
        rendered_aktList.append(((teaterstykker[0][0],el)))
    rendered_aktList.append((teaterstykker[1][0],lstSAAEK))
    return rendered_aktList


def insert_akt():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    lstKM = [1,2,3,4,5]
    lstSAAEK = 1
    TeaterStykker = AktList()
    for el in (TeaterStykker):
        string = f'INSERT INTO Akt VALUES ({el[0]},{el[1]}, "Akt {el[0]}.{el[1]}");'
        cursor.execute(string)
        con.commit()
    con.close()
    return None
