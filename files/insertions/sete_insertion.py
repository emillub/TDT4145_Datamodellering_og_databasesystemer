import sqlite3
import sys
sys.path.append('files')

from common.constants import *
from common.sql_utils import *


def insert_seter(sal):
    seteIndex = 1
    cond = f'Navn = \"{sal["navn"]}\"'
    salID = fetchAllValuesFromTable('Sal', 'SalID', cond)[0][0]
    for omraade in sal['omraader']:
        for omradenavn,raderOgSeter in omraade.items():
            omraadeValue = f'"{omradenavn}"'
            if omradenavn == '':
                omraadeValue = 'NULL'
            if isinstance(raderOgSeter,tuple):
                print(raderOgSeter)
                rader = raderOgSeter[0]
                seter = raderOgSeter[1]
                for r in range (rader):
                    for s in range (seter):
                        insert_sete(seteIndex,radnr=r+1, setenr=s+1, omraade=omraadeValue, salID=salID)
                        seteIndex+=1
            else:
                for r in raderOgSeter:
                    for s in range(r):
                        insert_sete(seteIndex,radnr=r+1, setenr=s+1, omraade=omraadeValue, salID=salID)
                        seteIndex+=1

def insert_sete(seteIndex,radnr,setenr,omraade,salID : int,):
    seteID = int((str(salID) + str(seteIndex)))
    insertValuesIntoTable("Sete", "(SeteID ,RadNr, SeteNr, Område, SalID)", f'({seteID},{radnr}, {setenr}, {omraade},{salID})')

def init_sete():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sete (
        SeteID INTEGER NOT NULL,
        RadNr INTEGER NOT NULL,
        SeteNr INTEGER NOT NULL,
        Område VARCHAR(30),
        SalID INTEGER NOT NULL,
        CONSTRAINT Sete_PK PRIMARY KEY (SeteID),
        CONSTRAINT Sete_FK FOREIGN KEY (SalID) REFERENCES Sal(SalID)
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')

    con.commit()
    con.close
    
    insert_seter(HOVED_SCENE)
    insert_seter(GAMLE_SCENE)

init_sete()