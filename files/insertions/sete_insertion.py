import sqlite3
import sys
sys.path.append('files')
from common.sql_utils import insertValuesIntoTable
from common.constants import *

def insert_seter(sal):
    seteIndex = 1
    salID = sal['id']

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

insert_seter(HOVED_SCENE)
insert_seter(GAMLE_SCENE)