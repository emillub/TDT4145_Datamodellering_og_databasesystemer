import sqlite3 

con = sqlite3.connect("./teater.db")
cursor = con.cursor()

con.commit()
con.close()