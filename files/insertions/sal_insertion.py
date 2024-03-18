import sqlite3

def insert_sal():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute('''
                INSERT INTO Sal VALUES (1, "Hovedscenen", 516);
                ''')
    cursor.execute('''
                INSERT INTO Sal VALUES (2, "Gamle scene", 332);
                    ''')
    cursor.execute('''
                INSERT INTO Sal VALUES (3, "Studioscenen", 150);
                    ''')
    cursor.execute('''
                INSERT INTO Sal VALUES (4, "Teaterkjelleren", 60);
                    ''')
    cursor.execute('''
                INSERT INTO Sal VALUES (5, "Teaterkafeen", 100);
                    ''')
    con.commit()
    con.close()
    return None