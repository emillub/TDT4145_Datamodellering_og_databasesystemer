import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_ordre(dato,klokkeslett,kundeid):
    insertValuesIntoTable('Ordre', '(Dato, Klokkeslett, KundeID)', f'("{dato}", "{klokkeslett}",{kundeid})')

def getOrdre(dato,klokkeslett,kundeid):
    return selectValuesFromTable('Ordre', 'OrdreID', f'(Dato = "{dato}" AND Klokkeslett = "{klokkeslett}" AND KundeID = {kundeid})')[0][0]