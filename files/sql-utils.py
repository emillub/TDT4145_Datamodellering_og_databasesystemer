import sqlite3


def insertValuesIntoTable(table, valueNames, values):
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    command = f'INSERT INTO {table} {valueNames} VALUES {values}'
    try:
        cursor.execute(command)
        con.commit()
    except Exception as e:
        print(e)
    con.close()

def fetchAllValuesFromTable(table, values):
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    command = f'SELECT {values} FROM {table}'
    try:
        cursor.execute(command)
        res = cursor.fetchall()
    except Exception as e:
        print(e)
        res = None
    con.close()
    return res
