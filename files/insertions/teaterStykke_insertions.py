import sqlite3

con = sqlite3.connect("./teater.db")
cursor = con.cursor()

cursor.execute('''
               INSERT INTO TeaterStykke VALUES (1, "Kongsemnene","18:30","Henrik Ibsen");
               ''')

cursor.execute('''
               INSERT INTO TeaterStykke VALUES (2, "Størst av alt er kjærligheten","19:30","Jonas Corell Petersen");
               ''')

con.commit()
con.close()