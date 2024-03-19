import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_billett(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    insertValuesIntoTable('Billett', '(SeteID, OppsetningID, Type, OrdreID,TeaterStykkeID)', f'({seteid}, {oppsetningid}, "{bType}", {ordreid}, {teaterstykkeid})')