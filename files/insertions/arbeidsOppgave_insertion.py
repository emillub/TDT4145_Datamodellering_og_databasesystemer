import sqlite3
from ansatt_insertion import getData 

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

def getArbeidsOppgave():
    rendered_arbeidsOppgave_list = []
    data = getData(urlKM)
    arbeidsOppgave_list = data[0]["acf"]["artistic_team_list"]
    for el in arbeidsOppgave_list:
        rendered_arbeidsOppgave_list.append((el["sub_title"],1))
        
    data = getData(urlSAAEK)
    arbeidsOppgave_list = data[0]["acf"]["artistic_team_list"]
    for el in arbeidsOppgave_list:
        rendered_arbeidsOppgave_list.append((el["sub_title"],2))
    return rendered_arbeidsOppgave_list

def insert_arbeidsoppgaver():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    arbeidsOppgaveList = getArbeidsOppgave()
    for index,el in enumerate(arbeidsOppgaveList):
        string = f'INSERT INTO Arbeidsoppgave VALUES ({index},"{str(el[0])}","Ansvarlig for {str(el[0])}",{el[1]});'
        cursor.execute(string)
        con.commit()
    con.close()
    return None
        
#insert_arbeidsoppgaver()
