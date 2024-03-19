import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def init_billettType(teaterStykke):
    for bType,pris in teaterStykke['priser'].items():
        insert_billettType(bType,teaterStykke['id'],pris)

def insert_billettType(type,stykkeID,pris):
    insertValuesIntoTable('BillettType', '(Type, TeaterStykkeID, Pris)', f'("{type}", {stykkeID}, {pris})')
