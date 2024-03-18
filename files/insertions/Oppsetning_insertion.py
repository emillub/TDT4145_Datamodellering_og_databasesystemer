import sqlite3
from akt_insertion import getTeaterStykkeID

def OppsetningList():
    datoKE = ["1. februar", "2. februar", "3. februar", "5. februar", "6. februar"]
    datoSAAEK = ["3. februar", "6. februar", "7. februar", "12. februar", "13. februar", "14. februar"]
    Teaterstykke = getTeaterStykkeID()
    rendered_Oppsetning = []
    for i in datoKE:
        rendered_Oppsetning.append((i, Teaterstykke[0][0]))
    for j in datoSAAEK:
        rendered_Oppsetning.append((j, Teaterstykke[1][0]))
    return rendered_Oppsetning

def insert_Oppsetning():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    opplst = OppsetningList()
    index = 1
    for el in (opplst):
        string = f'INSERT INTO Oppsetning VALUES ({index},"{el[0]}", {el[1]});'
        cursor.execute(string)
        con.commit()
        index +=1
        con.commit()
    con.close()
    return None
