import sqlite3
import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def init_sal(sal):
    settInnVerdierITabell('Sal', '(SalID, Navn, Kapasitet)', f'({sal["id"]},\"{sal["navn"]}\",{sal["kapasitet"]})')

def hentSalIDFraNavn(navn):
    return velgVerdierFraTabell(f'Sal', 'SalID', f'Navn = "{navn}"')[0][0]

def hentSalKapasitet(salid):
    return velgVerdierFraTabell(f'Sal', 'Kapasitet', f'SalID = {salid}')[0][0]
