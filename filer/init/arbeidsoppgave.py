import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def insert_arbeidsoppgave(index, teaterStykke,medvirker, ansattID):
    oppgave = medvirker['oppgave']
    oppgaveID = int(str(teaterStykke['id'])+str(index))
    settInnVerdierITabell('Arbeidsoppgave', '(OppgaveID, Navn, TeaterStykkeID)', f'({oppgaveID},\"{(oppgave)}\", {teaterStykke["id"]})')
    settInnVerdierITabell('HarOppgave', '(OppgaveID, AnsattID)', f'({oppgaveID}, {ansattID})')