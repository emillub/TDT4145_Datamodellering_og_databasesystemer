import sqlite3
from ansatt_insertion import getData

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

# Get roles from database
def getRolle():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute('''
                SELECT RolleID, Navn
                from Rolle;
                   ''')
    rolle = cursor.fetchall()
    con.commit()
    con.close()
    return rolle

# Get skuespiller from database
def getSkuespiller():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute('''
                   SELECT AnsattID, Navn
                   from Ansatt
                   where AnsattID in (Select * from Skuespiller);
                   ''')
    skuespillere = cursor.fetchall()
    con.commit()
    con.close()
    return skuespillere

# Creates a list of (RolleID, AnsattID)
def harRolleListe():
    Skuespillere = getSkuespiller()
    roller = getRolle()
    rendered_relationList = []
    data = getData(urlKM)
    rollerData = data[0]["acf"]["actors_list"]
    for el in rollerData:
        rendered_relationList.append((el["actor"]["title"]["rendered"],el["sub_title"]))
    for el in Skuespillere[12:]:
        rendered_relationList.append((el[1],el[1]))
    
    correct_list = []
    for index,el in enumerate(rendered_relationList):
        if ((el[0]==Skuespillere[index][1]) and (el[1]==roller[index][1])):
            correct_list.append((roller[index][0],Skuespillere[index][0]))
    return correct_list

# Insert rolle into database
def insert_harRolle():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()   
    oppgaveList = harRolleListe()
    for el in oppgaveList:
        string = f'INSERT INTO HarRolle VALUES ({el[0]},{el[1]})'
        cursor.execute(string)
        con.commit()
    con.close()
    return None