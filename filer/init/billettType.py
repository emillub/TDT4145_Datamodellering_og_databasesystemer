import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def init_billettType(teaterStykke):
    for bType,pris in teaterStykke['priser'].items():
        insert_billettType(bType,teaterStykke['id'],pris)

def insert_billettType(type,stykkeID,pris):
    settInnVerdierITabell('BillettType', '(Type, TeaterStykkeID, Pris)', f'("{type}", {stykkeID}, {pris})')