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

def hentSkuespillereISammeAktogStykke(navn):
    kommando = f'''SELECT  A.Navn,  RA.Nummer AS AktNummer,  TS.Navn
                FROM Skuespiller AS S
                JOIN HarRolle AS HR ON (HR.AnsattID =  S.AnsattID)
                JOIN Ansatt AS A ON (A.AnsattID = S.AnsattID)
                JOIN RolleIAkt AS RA ON (RA.RolleID = HR.RolleID)
                JOIN TeaterStykke AS TS ON (TS.TeaterStykkeID = RA.TeaterStykkeID)
                ORDER BY RA.TeaterStykkeID, AktNummer
                '''
    res = manualCommanSqlSelect(kommando)
    lst = []
    lst2 = []
    for i in res:
        for j in res:
            if (i[0] == navn):
                if ((i[1] == j[1]) and (i[0] != j[0]) and (i[2] == j[2])):
                    tuppel = (i[0], j[0], i[2])
                    lst.append(tuppel)
    for el in lst:
        if navn in el:
            lst2.append(el)
    return lst2