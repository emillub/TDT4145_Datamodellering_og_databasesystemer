import sqlite3
import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

from init._table_init import init_table
from init.ansatt import init_ansatte
from init.teaterStykke import init_teaterStykke
from init.billettType import init_billettType
from init.oppsetning import init_oppsetninger
from init.akt import init_akter
from init.sal import init_sal
from init.sete import init_seter

# Runs all insertion-filer in correct order.
init_table()

# for sal in SALER:
for sal in SALER:
    init_sal(sal)
    init_seter(sal)

for teaterstykke in TEATERSTYKKER:
    init_teaterStykke(teaterstykke)
    init_billettType(teaterstykke)
    init_ansatte(teaterstykke)
    init_akter(teaterstykke)
    init_oppsetninger(teaterstykke)