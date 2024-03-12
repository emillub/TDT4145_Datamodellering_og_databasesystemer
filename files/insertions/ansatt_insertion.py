import sqlite3
import requests

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

def getData(url):
    response = requests.get(url)
    return response.json()

def getActors():
    rendered_actor_list = []
    data = getData(urlKM)
    actor_list = data[0]["acf"]["actors_list"]
    
    for el in actor_list:
        rendered_actor_list.append(el["actor"]["title"]["rendered"])
    data = getData(urlSAAEK)
    actor_list = data[0]["acf"]["actors_list"]
    for el in actor_list:
        rendered_actor_list.append(el["actor"]["title"]["rendered"])
    return rendered_actor_list

def getMedvirkende():
    rendered_medvirkende_list = []
    data = getData(urlKM)
    medvirkende_list = data[0]["acf"]["artistic_team_list"]
    
    for el in medvirkende_list:
        rendered_medvirkende_list.append(el["member"]["title"]["rendered"])
    data = getData(urlSAAEK)
    medvirkende_list = data[0]["acf"]["artistic_team_list"]
    for el in medvirkende_list:
        rendered_medvirkende_list.append(el["member"]["title"]["rendered"])
    return rendered_medvirkende_list

con = sqlite3.connect("./teater.db")
cursor = con.cursor() 

for index,el in enumerate(getActors()):
    string = f'INSERT INTO Ansatt VALUES ({index},"{str(el)}",NULL,"innleid");'
    stringSkuespiller = f'INSERT INTO Skuespiller VALUES ({index});'
    cursor.execute(string)
    con.commit()
    cursor.execute(stringSkuespiller)
    con.commit()
    
for index,el in enumerate(getMedvirkende()):
    string = f'INSERT INTO Ansatt VALUES ({index+len(getActors())},"{str(el)}",Null,"innleid");'
    stringMedvirkende = f'INSERT INTO Medvirkende VALUES ({index+len(getActors())});'
    cursor.execute(string)
    con.commit()
    cursor.execute(stringMedvirkende)
    con.commit()
    
con.commit()
con.close()

