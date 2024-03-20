import sqlite3
import sys

sys.path.append('files')
from common.sql_utils import bestSolgtForestilling

data = bestSolgtForestilling()
for i in data:
    print(f'ForestillingsNavn: {i[0]} || Dato: {i[1]} || Antall solgte plasser: {i[2]}')
