import sqlite3

from ansatt_insertion import insert_ansatte
from arbeidsOppgave_insertion import insert_arbeidsoppgaver
from table_insertion import table_initialization
from teaterStykke_insertion import insert_teaterStykke
from harOppgave_insertion import insert_harOppgave
from rolle_insertion import insert_rolle
from harRolle_insertion import insert_harRolle
from akt_insertion import insert_akt
from oppsetning_insertion import insert_Oppsetning
from sal_insertion import insert_sal
from harRolleIAkt_insertion import insert_RolleIAkt
from visesI_insertion import insert_visesI

con = sqlite3.connect("./teater.db")
cursor = con.cursor()

# NECESSARY URLS FOR INFORMATIONS
urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

# Runs all insertion-files in correct order.
table_initialization()
insert_teaterStykke()
insert_ansatte()
insert_arbeidsoppgaver()
insert_harOppgave()
insert_rolle()
insert_harRolle()
insert_akt()
insert_Oppsetning()
insert_sal()
insert_RolleIAkt()
insert_visesI()


con.commit()
con.close()
