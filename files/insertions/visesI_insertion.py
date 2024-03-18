import sqlite3

def insert_visesI():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    string = f'INSERT INTO VisesI VALUES ({1},{1});'
    cursor.execute(string)
    string = f'INSERT INTO VisesI VALUES ({2},{2});'
    cursor.execute(string)
    con.commit()
    con.close()    
    return None