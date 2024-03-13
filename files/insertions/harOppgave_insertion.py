import sqlite3
from ansatt_insertion import getData

urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

# Gets AnsattID and Navn from Ansatt
def getMedvirkende():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute('''
                SELECT AnsattID, Navn
                from Ansatt
                where AnsattID in (select AnsattID from Medvirkende);
                   ''')
    medvirkende = cursor.fetchall()
    con.commit()
    con.close()
    return medvirkende

# Gets OppgaveID and Navn from ArbeidsOppgave
def getArbeidsOppgave():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()    
    cursor.execute('''
                   SELECT OppgaveID, Navn 
                   from ArbeidsOppgave;
                   ''')
    arbeidsOppgave = cursor.fetchall()
    con.commit()
    con.close()
    return arbeidsOppgave

# Gets Creates a list of (AnsatteID, OppgaveID)
def harOppgaveListe():
    rendered_arbeidsOppgaveListe = []
    data = getData(urlKM)
    arbeidsOppgaveListe = data[0]["acf"]["artistic_team_list"]
    medvirkende = getMedvirkende()
    for el in medvirkende:
        for index in arbeidsOppgaveListe:
            if el[1] == index["member"]["title"]["rendered"]:
                rendered_arbeidsOppgaveListe.append((el[0],index["sub_title"]))
                
    data = getData(urlSAAEK)
    arbeidsOppgaveListe = data[0]["acf"]["artistic_team_list"]
    for el in medvirkende:
        for index in arbeidsOppgaveListe:
            if el[1] == index["member"]["title"]["rendered"]:
                rendered_arbeidsOppgaveListe.append((el[0],index["sub_title"]))
    
    arbeidsOppgaver = getArbeidsOppgave()
    final_list = []
    for el in rendered_arbeidsOppgaveListe:
        for index in arbeidsOppgaver:    
            if el[1] == index[1]:
                final_list.append((el[0],index[0]))  
    return final_list

# Inserts list from harOppgaveListe into database in correct order
def insert_harOppgave():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()   
    oppgaveList = harOppgaveListe()
    for el in oppgaveList:
        string = f'INSERT INTO HarOppgave VALUES ({el[1]},{el[0]})'
        cursor.execute(string)
        con.commit()
    con.close()
    
    return None
