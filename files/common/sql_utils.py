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
        print(command)

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
        print(command)
        print(e)
        res = None
    con.close()
    return res

def manualInsert(command):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    try:
        cursor.execute(command)
        con.commit()
    except Exception as e:
        print(command)
        print(e)
    con.close()

def manualSelect(command):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    try:
        cursor.execute(command)
        res = cursor.fetchall()

    except Exception as e:
        print(command)
        print(e)
        res = None
    con.close()
    return res

# Funksjoner for brukerhistorier 4-7 under

def hentForestillingOgSolgteBilletter(dato="YYYY-MM-DD"):
    string = f'''SELECT Navn, COUNT (DISTINCT BillettID) AS SolteBilletter
                FROM Oppsetning 
                LEFT JOIN TeaterStykke ON Oppsetning.TeaterStykkeID=TeaterStykke.TeaterstykkeID
                LEFT JOIN Billett USING (OppsetningID)
                WHERE Dato = "{dato}" GROUP BY OppsetningID;
                '''
    res = manualSelect(string)
    return res

def hentTeaterstykkeSkueSpillerRolle():
    string = f'''
                SELECT DISTINCT TS.Navn, Ansatt.Navn, R.Navn 
                from Ansatt
                JOIN HarRolle AS HR ON HR.AnsattID = Ansatt.AnsattID
                JOIN Rolle AS R USING(RolleID)
                JOIN RolleIAkt AS RIA USING (RolleID)
                JOIN TeaterStykke AS TS USING (TeaterStykkeID)
                ORDER BY TS.Navn, Ansatt.Navn;
                    '''
    res = manualSelect(string)
    return res

def bestSolgtForestilling():
    string = f'''SELECT TS.navn AS ForestillingsNavn, O.dato AS Dato, COUNT(B.BillettID) AS AntallSolgtePlasser
                FROM Oppsetning AS O
                JOIN TeaterStykke  AS TS ON O.TeaterStykkeID = TS.TeaterStykkeID
                LEFT JOIN Billett  AS B ON O.OppsetningID = B.OppsetningID
                GROUP BY O.OppsetningID
                ORDER BY AntallSolgtePlasser DESC;
                '''
    res =manualSelect(string)
    return res

def hentSkuespillereISammeAktogStykke(navn):
    kommando = f'''SELECT DISTINCT sNavn, teaterstykkeNavn
                FROM (RolleIAkt as ria2
                JOIN(
                SELECT ria.TeaterStykkeID, ria.Nummer
                FROM ((SELECT AnsattID as SkuespillerID FROM Skuespiller) AS S
                JOIN (SELECT Navn, AnsattID FROM Ansatt WHERE Navn = "{navn}" ) AS A ON (A.AnsattID = S.SkuespillerID)
                NATURAL JOIN HarRolle as hr
                NATURAL JOIN RolleIAkt as ria)) as ria1
                ON ria1.TeaterStykkeID = ria2.TeaterStykkeID AND ria1.Nummer = ria2.Nummer) as aktid
                NATURAL JOIN HarRolle as hr
                NATURAL JOIN (SELECT Navn as sNavn, AnsattID FROM ansatt) as a
                NATURAL JOIN (SELECT Navn as teaterstykkeNavn, TeaterStykkeID FROM TeaterStykke)
                WHERE sNavn != "{navn}"
                '''
    return manualSelect(kommando)