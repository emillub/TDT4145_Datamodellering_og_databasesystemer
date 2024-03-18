import sqlite3
import sys
sys.path.append('files')
from common.constants import *


def insertValuesIntoTable(table, valueNames, values):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    command = f'INSERT INTO {table} {valueNames} VALUES {values}'
    try:
        cursor.execute(command)
        con.commit()
    except Exception as e:
        print(e)
    con.close()

def fetchAllValuesFromTable(table, values, condition = None):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    command = f'SELECT {values} FROM {table}'
    if condition != None:
        command += f' WHERE {condition};'
    try:
        cursor.execute(command)
        res = cursor.fetchall()
    except Exception as e:
        print(e)
        res = None
    con.close()
    return res