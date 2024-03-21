# Innlevering 2 - Gruppe 115
Laget av:
Emil Lunde-Bakke
August Damm Lindbæk
Mauritz Hardersen Skogøy
_________________________


Dette dokumenter har som hensikt å gi en beskrivelse av innlevert prosjekt, dokumentere endringer i modellen fra innlevering 1 og gi en manual på hvordan man skal kjøre de forskjellige brukerhistoriene gitt i oppgaveteksten.

Innlevert mappe inneholder to mapper, en readME og den tomme databasefilen. Mappene heter filer og txt, som inneholder henholdsvis koden som utfører brukerhistoriene og initierer databasen, og utdelte txt-filer som brukes til å initiere solgte billetter. 

# Forutsetninger

For at man skal kunne kjøre dette prosjektet forutsetter det at leser har en grunnleggende forståelse av kodespråket python og hvordan man skal kjøre et pythonscript. Vi forutsetter at man kjører programmet enten gjennom terminalvinduet eller gjennom vscode. Applikasjonen vår gjør API kall for å hente informasjon fra nettsiden til Trønderlag Teater, så leser må ha internett-tilgang for å kunne kjøre programmet. For å holde koden ryddig har vi skrevet SQL-statementene i brukerhistorier 4-7 i bunnen av filen .files/brukerhistorier/sql_utils.py linje 64-119 i stedet for å levere inn rå SQL kode. Dette følte vi var fordelaktig fremfor å levere rå SQL sammen med et pythonprosjekt. 
# Kjøreoppskrift

Før man kan kjøre programmet er det viktig at man har to python-pakker installert. Dette er **request**-modulen og **sqlite3**-modulen. Disse er nødvendige for henholdsvis å kunne gjøre http-kall og for å kunne kommunisere med databasen. Etter man har installert python kan man kjøre kommandoene under får å installere modulene  i enten terminal-vinduet eller i integrert terminal i VS code.

`Pip install sqlite3`
`Pip install requests`  

Når du har installert disse har du to alternativer for å kjøre brukerhistoriene; gjennom terminalvindu eller gjennom vscode

### Terminal-vindu
Når du har åpnet terminalviduet må du navigere deg fram til bunnen av prosjektet. Det er viktig at du "unzip"'er prosjektfilen for at du skal kunne navigere deg til bunnen av prosjektet. Naviger deg så fram til bunnen av prosjektet. Du er i bunnen når filplasseringen viser at du har følgende mapper tilgjengelige i directoriet ditt: 

- filer
- txt
- README.md
- teater.db

Fra her kan man kjøre følgende kommando for å kjøre python scriptene som gjennomfører brukerhistoriene:

`python .\files\brukerhistorier\bh1.py` 
eller eventuelt 
`python3 .\files\brukerhistorier\bh1.py`

Slik kan man kjøre gjennom brukerhistorie 1-7 ved å endre tallet før .py deklarasjonen til hvaenn man ønsker mellom 1 og 7. Vi anbefaler at man kjører 1 og 2 først for å initiere databasen. Hvis du ønsker å endre input til programmene, kan du åpne brukerhistorie-filene i et tekst-redigerings-program og endre på de oppgitte variablene for å få annen output. Husk å lagre endringene før du kjører filen på nytt.

### VScode
For å kjøre prosjektet i VScode trenger man også å pakke ut prosjektet på samme måte som om man kjører det i terminalvinduet. Åpne så prosjektet i VScode med root-folder der hvor du ser følgende mapper i prosjektet:

- filer
- txt
- README.md
- teater.db

Derfra kan du åpne filene og kjøre koden ved å trykke på "kjør" knappen oppe til høyre i VScode. Programmene skal kjøre og output skal vises i den integrerte terminalen i VScode. Her kan man også endre på de oppgitte feltene i brukerhistorie-filene for å få forskjellig output ut fra hva man ønsker å se.

# Output fra brukerhistorier

Under finner dere hva forventet output fra de forskjellige brukerhistoriene skal være gitt en spesifisert input.
## BH1

Ingen output - skal kun initiere database


## BH2
Ingen output - skal kun initiere database

## BH3
Når du kjører programmet skal du få opp trinnvis følgende spørsmål:

	La oss lage en kundeprofil til deg!	
	Hva heter du? Mauritz
	Hva er tlf. nr ditt? 49234
	Hva er adressen din? Hern
	Det er 17 rader med 9 ledige stoler
	[0] : ('Balkong', 1)
	[1] : ('Balkong', 2)
	[2] : ('Balkong', 3)
	[3] : ('Balkong', 4)
	[4] : ('Galleri', 1)
	[5] : ('Galleri', 2)
	[6] : ('Galleri', 3)
	[7] : ('Parkett', 1)
	[8] : ('Parkett', 2)
	[9] : ('Parkett', 3)
	[10] : ('Parkett', 4)
	[11] : ('Parkett', 5)
	[12] : ('Parkett', 6)
	[13] : ('Parkett', 7)
	[14] : ('Parkett', 8)
	[15] : ('Parkett', 9)
	[16] : ('Parkett', 10)

	Velg en rad ved å skrive inn tallet til venstre for raden: 16
Skriver du inn inputen spesifisert til venstre for semikolonene på hvert spørsmål, skal du få samme output.

## BH4
Kjører du bh4.py-filen uten modifikasjoner skal du få denne outputen. 

	TeaterStykke: Kongsemnene || SolteBilletter: 65
	TeaterStykke: Størst av alt er kjærligheten || SolteBilletter: 36

Programmet er satt til å skrive ut forestillinger for dato: 2024-02-03, men dette kan endres på ved en kode-editor. Da kan du endre på følgende felt for å se forstillinger for andre dager. Det er viktig at du velger en dag hvor det faktisk er satt opp en forestilling (se oppgavebeskrivelsen) for å få output. Dette er linje 10 i bh4.py

	# Her kan man endre dato for å se hvilke forestillinger som er satt opp.
	dato = "2024-02-03"

## BH5
Under følger output hvis man kjører bh5.py. Den skal ikke ta noen input.

	TeaterStykke: Kongsemnene || Skuespiller: Arturo Scotti || Rolle: Haakon Haakonssønn
	TeaterStykke: Kongsemnene || Skuespiller: Emil Olafsson || Rolle: Jatgeir Skald
	TeaterStykke: Kongsemnene || Skuespiller: Emil Olafsson || Rolle: Dagfinn Bonde
	TeaterStykke: Kongsemnene || Skuespiller: Emma Caroline Deichmann || Rolle: Sigrid (Skules søster)
	TeaterStykke: Kongsemnene || Skuespiller: Emma Caroline Deichmann || Rolle: Ingebjørg
	TeaterStykke: Kongsemnene || Skuespiller: Fabian Heidelberg Lunde || Rolle: Baard Bratte
	TeaterStykke: Kongsemnene || Skuespiller: Fabian Heidelberg Lunde || Rolle: Trønder
	TeaterStykke: Kongsemnene || Skuespiller: Hans Petter Nilsen || Rolle: Skule jarl
	TeaterStykke: Kongsemnene || Skuespiller: Ingunn Beate Strige Øyen || Rolle: Inga fra Vartejg (Haakons mor)
	TeaterStykke: Kongsemnene || Skuespiller: Isak Holmen Sørensen || Rolle: Paal Flida
	TeaterStykke: Kongsemnene || Skuespiller: Isak Holmen Sørensen || Rolle: Trønder
	TeaterStykke: Kongsemnene || Skuespiller: Madeleine Brandtzæg Nilsen || Rolle: Fru Ragnhild (Skules hustru)
	TeaterStykke: Kongsemnene || Skuespiller: Per Bogstad Gulliksen || Rolle: Gregorius Jonssønn
	TeaterStykke: Kongsemnene || Skuespiller: Snorre Ryen Tøndel || Rolle: Peter (prest og Ingebjørgs sønn)
	TeaterStykke: Kongsemnene || Skuespiller: Synnøve Fossum Eriksen || Rolle: Margrete (Skules datter)
	TeaterStykke: Kongsemnene || Skuespiller: Thomas Jensen Takyi || Rolle: Biskop Nikolas
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Jo Saberniak || Rolle: Jo Saberniak
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Marte M. Steinholt || Rolle: Marte M. Steinholt
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Natalie Grøndahl Tangen || Rolle: Natalie Grøndahl Tangen
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Sunniva Du Mond Nordal || Rolle: Sunniva Du Mond Nordal
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Tor Ivar Hagen || Rolle: Tor Ivar Hagen
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Trond-Ove Skrødal || Rolle: Trond-Ove Skrødal
	TeaterStykke: Størst av alt er kjærligheten || Skuespiller: Åsmund Flaten || Rolle: Åsmund Flaten

Vår SQL query finnes som oppgitt under seksjonen *Forutsetninger*, men er for enkelthets skyld gjengitt her:

	SELECT DISTINCT TS.Navn, Ansatt.Navn, R.Navn 
	from Ansatt
	JOIN HarRolle AS HR ON HR.AnsattID = Ansatt.AnsattID
	JOIN Rolle AS R USING(RolleID)
	JOIN RolleIAkt AS RIA USING (RolleID)
	JOIN TeaterStykke AS TS USING (TeaterStykkeID)
	ORDER BY TS.Navn, Ansatt.Navn

## BH6
Under følger output fra BH6.py. 

	ForestillingsNavn: Kongsemnene || Dato: 2024-02-03 || Antall solgte plasser: 65
	ForestillingsNavn: Størst av alt er kjærligheten || Dato: 2024-02-03 || Antall solgte plasser: 36
	ForestillingsNavn: Kongsemnene || Dato: 2024-02-01 || Antall solgte plasser: 0
	ForestillingsNavn: Kongsemnene || Dato: 2024-02-02 || Antall solgte plasser: 0
	ForestillingsNavn: Kongsemnene || Dato: 2024-02-05 || Antall solgte plasser: 0
	ForestillingsNavn: Kongsemnene || Dato: 2024-02-06 || Antall solgte plasser: 0
	ForestillingsNavn: Størst av alt er kjærligheten || Dato: 2024-02-06 || Antall solgte plasser: 0
	ForestillingsNavn: Størst av alt er kjærligheten || Dato: 2024-02-07 || Antall solgte plasser: 0
	ForestillingsNavn: Størst av alt er kjærligheten || Dato: 2024-02-12 || Antall solgte plasser: 0
	ForestillingsNavn: Størst av alt er kjærligheten || Dato: 2024-02-13 || Antall solgte plasser: 0
	ForestillingsNavn: Størst av alt er kjærligheten || Dato: 2024-02-14 || Antall solgte plasser: 0
Dette programmet skal ikke ta input og output skal være lignende over. Det kan være forskjell i siste tall på linje 2 avhengig av hvor mange ganger bh3.py kjører ettersom det oppdaterer kjøpte billetter.

## BH7
Under er output fra BH7.py gitt.

	Skuespiller: Jo Saberniak:
	--------------------------
	MedSkuespiller: Sunniva Du Mond Nordal || TeaterStykke: Størst av alt er kjærligheten
	MedSkuespiller: Marte M. Steinholt || TeaterStykke: Størst av alt er kjærligheten
	MedSkuespiller: Tor Ivar Hagen || TeaterStykke: Størst av alt er kjærligheten
	MedSkuespiller: Trond-Ove Skrødal || TeaterStykke: Størst av alt er kjærligheten
	MedSkuespiller: Natalie Grøndahl Tangen || TeaterStykke: Størst av alt er kjærligheten
	MedSkuespiller: Åsmund Flaten || TeaterStykke: Størst av alt er kjærligheten
Denne outputen gjelder for skuespiller "Jo Saberniak" men dette kan endres på samme måte som for bh4, hvis man ønsker å se annen output. Da kan man endre på følgende felt i bh7.py filen:

	# Her kan man endre skuespillernavn for å se medskuespillere og teaterstykke.
	navn =  'Jo Saberniak'
Dette er linje 7 og 8 vist i bh7.py filen.

# Bemerkninger

Vi har sett det hensiktsmessig å endre på enkelte aspekter med modellen vår for å gjøre den implementerbar i python- og SQL-kode. Under er det gitt en liste med endringer fra leveranse 1 som er gjort for å gjøre implementasjon mulig:

- Vi har introdusert seteklasse for å gjøre salg av seter enklere å implementere i databasemodellen vår.
- Akt-navn er ikke lengre unike ettersom man kan ha samme navn på flere akter i forskjellige teaterstykker.
- VisesI tabellen som er illustrer i ERR-diagrammet er unødvendig. Dette kommer av at oppgavebeskrivelsen oppgir at et stykke kun vises i en sal og dette er dermed lagt inn under konstanter-mappen

Disse endringene er lagt til for å implementere modellen.

Kunsitg intelligens er ikke brukt for å generere kode, men minimalt brukt som verktøy for å debugge kode. 