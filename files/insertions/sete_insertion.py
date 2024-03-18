import sqlite3
import sys
sys.path.append('files')
from common.sql_utils import insertValuesIntoTable
from common.constants import *

seterPerRadPerOmraadeHovedScene = {'' : (18,28), 'Galleri' : (4,5) }

def insert_seter(salid, seterPerRadPerOmraade : dict):
    seteIndex = 1
    for omraade in seterPerRadPerOmraade.keys():
        omraadeValue = f'"{omraade}"'
        if omraade == '':
            omraadeValue = 'NULL'
        rader = seterPerRadPerOmraade[omraade][0]
        seter = seterPerRadPerOmraade[omraade][1]
        for r in range (rader):
            for s in range (seter):
                insert_sete(seteIndex,radnr=r+1, setenr=s+1, omraade=omraadeValue, salID=salid)
                seteIndex+=1

def insert_sete(seteIndex,radnr,setenr,omraade,salID : int,):
    seteID = int((str(salID) + str(seteIndex)))
    insertValuesIntoTable("Sete", "(SeteID ,RadNr, SeteNr, Område, SalID)", f'({seteIndex},{radnr}, {setenr}, {omraade},{salID})')

insert_seter(HOVED_SCENE_ID, seterPerRadPerOmraadeHovedScene)