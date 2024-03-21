import sqlite3
import sys

sys.path.append('filer')
from diverse.sql_kommandoer import bestSolgtForestilling

data = bestSolgtForestilling()
for i in data:
    print(f'ForestillingsNavn: {i[0]} || Dato: {i[1]} || Antall solgte plasser: {i[2]}')
