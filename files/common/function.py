import sqlite3 

con = sqlite3.connect("./teater.db")
cursor = con.cursor()

def hentSolgteBilletter():
    string = f'SELECT * FROM Billett;'
    cursor.execute(string)
    var = cursor.fetchall()
    print(var)
    return var

def sjekkBillett(BillettID, StolNr):
    solgtebilletter = hentSolgteBilletter()
    code = f'SELECT {BillettID} FROM Billett;'
    cursor.execute(code)
    return None
hentSolgteBilletter()

con.commit()
con.close()