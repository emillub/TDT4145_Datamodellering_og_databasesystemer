import sqlite3

from ansatt_insertion import insert_ansatte
from arbeidsOppgave_insertion import insert_arbeidsoppgaver
from table_insertion import table_initialization
from teaterStykke_insertions import insert_teaterStykke


con = sqlite3.connect("./teater.db")
cursor = con.cursor()

# NECESSARY URLS FOR INFORMATIONS
urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

table_initialization()
insert_teaterStykke()
insert_ansatte()
insert_arbeidsoppgaver()

con.commit()
con.close()
