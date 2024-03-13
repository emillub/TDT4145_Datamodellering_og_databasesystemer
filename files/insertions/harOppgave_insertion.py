import sqlite3


def getMedvirkende():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute('''
                   SELECT * FROM Medvirkende;
                   ''')
    medvirkendeID = cursor.fetchall()
    con.commit()
    con.close()
    return medvirkendeID
