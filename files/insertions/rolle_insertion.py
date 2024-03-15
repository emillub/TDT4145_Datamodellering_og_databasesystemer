import sqlite3
from ansatt_insertion import getData

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

# Get roller from API
def getRoller():
    rendered_Rolle_list = []
    data = getData(urlKM)
    rolleListe = data[0]["acf"]["actors_list"]
    for el in rolleListe:
        rendered_Rolle_list.append(el["sub_title"])
        
    data = getData(urlSAAEK)
    rolleListe = data[0]["acf"]["actors_list"]
    for el in rolleListe:
        rendered_Rolle_list.append(el["actor"]["title"]["rendered"])
    return rendered_Rolle_list    

# Insert roller int database
def insert_rolle():
    list = getRoller()
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    for index,el in enumerate(list):
        string = f'INSERT INTO Rolle VALUES ({index}, "{el}")'
        cursor.execute(string)
        con.commit()
    con.close()
    return None
