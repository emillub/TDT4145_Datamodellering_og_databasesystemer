import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_arbeidsoppgave(index, teaterStykke,medvirker, ansattID):
    oppgave = medvirker['oppgave']
    oppgaveID = int(str(teaterStykke['id'])+str(index))
    insertValuesIntoTable('Arbeidsoppgave', '(OppgaveID, Navn, TeaterStykkeID)', f'({oppgaveID},\"{(oppgave)}\", {teaterStykke["id"]})')
    insertValuesIntoTable('HarOppgave', '(OppgaveID, AnsattID)', f'({oppgaveID}, {ansattID})')