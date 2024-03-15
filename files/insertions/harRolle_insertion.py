import sqlite3
from ansatt_insertion import getData
from rolle_insertion import getRoller

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

# Get roles from database
def hentRolle():
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
    roller = hentRolle()
    rendered_relationList = []
    data = getData(urlKM)
    rollerData = data[0]["acf"]["actors_list"]
    for el in rollerData:
        rendered_relationList.append((el["actor"]["title"]["rendered"],el["sub_title"]))
    for el in rendered_relationList:
        if ("/" in el[1]):
            temp = el[1].split("/")
            rendered_relationList.pop(rendered_relationList.index(el))
            rendered_relationList.append((el[0],temp[0]))
            rendered_relationList.append((el[0],temp[1]))
    fml = rendered_relationList[7]
    fu = rendered_relationList[7][1].split("/")
    rendered_relationList.pop(7)
    rendered_relationList.append((fml[0],fu[0]))
    rendered_relationList.append((fml[0],fu[1]))
    
    for el in Skuespillere[12:]:
        rendered_relationList.append((el[1],el[1]))
    swapped_name = []
    correct_list = []
    for el in rendered_relationList:
        for j in Skuespillere:
            if (el[0]==j[1]):
                swapped_name.append((j[0],el[1]))
                
    for el in swapped_name:
        for j in roller:
            if (el[1]==j[1]):
                correct_list.append((el[0],j[0]))
    return correct_list

# Insert rolle into database
def insert_harRolle():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()   
    oppgaveList = harRolleListe()
    print(oppgaveList)
    for el in oppgaveList:
        string = f'INSERT INTO HarRolle VALUES ({el[0]},{el[1]})'
        cursor.execute(string)
        con.commit()
    con.close()
    return None
# insert_harRolle()