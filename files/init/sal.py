import sqlite3
import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def init_sal(sal):
    insertValuesIntoTable('Sal', '(SalID, Navn, Kapasitet)', f'({sal["id"]},\"{sal["navn"]}\",{sal["kapasitet"]})')