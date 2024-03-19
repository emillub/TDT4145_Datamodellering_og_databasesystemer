import sqlite3
import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def init_sal(sal):
    insertValuesIntoTable('Sal', '(SalID, Navn, Kapasitet)', f'({sal["id"]},\"{sal["navn"]}\",{sal["kapasitet"]})')

def getSalIDFraNavn(navn):
    return selectValuesFromTable(f'Sal', 'SalID', f'Navn = "{navn}"')[0][0]

def getSalKapasitet(salid):
    return selectValuesFromTable(f'Sal', 'Kapasitet', f'SalID = {salid}')[0][0]
