import sqlite3
import sys

import requests
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

def selectValuesFromTable(table, values, condition = None):
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

def manualCommandSqlInsert(command):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    try:
        cursor.execute(command)
        con.commit()
    except Exception as e:
        print(e)
    con.close()

def manualCommanSqlSelect(command):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    try:
        cursor.execute(command)
        res = cursor.fetchall()
    except Exception as e:
        print(e)
        res = None
    con.close()
    return res

def hentForestillingOgSolgteBilletter(dato="YYYY-MM-DD"):
    string = f'''SELECT Navn, COUNT (DISTINCT BillettID) AS SolteBilletter
                FROM Oppsetning 
                LEFT JOIN TeaterStykke ON Oppsetning.TeaterStykkeID=TeaterStykke.TeaterstykkeID
                LEFT JOIN Billett USING (OppsetningID)
                WHERE Dato = "{dato}" GROUP BY OppsetningID;
                '''
    res = manualCommanSqlSelect(string)
    return res
