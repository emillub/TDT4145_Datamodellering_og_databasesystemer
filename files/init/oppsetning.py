import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def init_oppsetninger(teaterstykke):
    for oppsetningsDato in teaterstykke['oppsetninger']:
        insertValuesIntoTable('Oppsetning', '(Dato, TeaterStykkeID)', f'(\"{oppsetningsDato}\", {teaterstykke["id"]})')
    
