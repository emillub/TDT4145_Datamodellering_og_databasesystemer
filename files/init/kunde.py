import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_kunde(id,tlfnr,navn,adr):
    insertValuesIntoTable('Kunde', '(KundeID, TelefonNr, Navn, Adresse)', f'({id}, {tlfnr}, "{navn}","{adr}")')