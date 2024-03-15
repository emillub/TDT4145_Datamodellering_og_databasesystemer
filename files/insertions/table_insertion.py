import sqlite3 


def table_initialization():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    
    cursor.execute('''
    CREATE TABLE Ansatt (
        AnsattID INTEGER NOT NULL,
        Navn VARCHAR(30),
        Email VARCHAR(30) UNIQUE,
        AnsattStatus VARCHAR(30) DEFAULT 'innleid',
        CONSTRAINT Ansatt_PK PRIMARY KEY (AnsattID),
        CONSTRAINT ckAnsatt 
        CHECK (AnsattStatus IN 
        ('innleid','fast ansatt','midlertidig ansatt','statist/frivillig'))
        );''')

    cursor.execute('''
    CREATE TABLE Skuespiller (
        AnsattID INTEGER NOT NULL,
        CONSTRAINT Skuespiller_PK PRIMARY KEY (AnsattID),
        CONSTRAINT Skuespiller_FK FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) 
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')

    cursor.execute('''
    CREATE TABLE Medvirkende (
        AnsattID INTEGER NOT NULL,
        CONSTRAINT Medvirkende_PK PRIMARY KEY (AnsattID),
        CONSTRAINT Medvirkende_FK
        FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) 
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')

    cursor.execute('''
    CREATE TABLE Arbeidsoppgave (
        OppgaveID INTEGER NOT NULL,
        Navn VARCHAR(30),
        Beskrivelse VARCHAR(70),
        TeaterStykkeID INTEGER NOT NULL,
        CONSTRAINT Arbeidsoppgave_PK PRIMARY KEY (OppgaveID),
        CONSTRAINT Arbeidsoppgave_FK FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke(TeaterStykkeID) 
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')

    cursor.execute('''	
    CREATE TABLE HarOppgave (
        OppgaveID INTEGER NOT NULL,
        AnsattID INTEGER NOT NULL,
        CONSTRAINT HarOppgave_PK PRIMARY KEY (OppgaveID, AnsattID),
        CONSTRAINT HarOppgave_FK1 FOREIGN KEY (OppgaveID) 
        REFERENCES Arbeidsoppgave(OppgaveID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE,
        CONSTRAINT HarOppgave_FK2 FOREIGN KEY (AnsattID) REFERENCES Medvirkende(AnsattID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')
        
    cursor.execute('''
    CREATE TABLE Rolle (
        RolleID INTEGER NOT NULL,
        Navn VARCHAR(30) NOT NULL,
        CONSTRAINT Rolle_PK PRIMARY KEY (RolleID)
        );''')

    cursor.execute('''
    CREATE TABLE HarRolle (
        RolleID INTEGER NOT NULL,
        AnsattID INTEGER NOT NULL,
        CONSTRAINT HarRolle_PK PRIMARY KEY (RolleID, AnsattID),
        CONSTRAINT HarRolle_FK1 FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) 
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        CONSTRAINT HarRolle_FK2 FOREIGN KEY (AnsattID) 
        REFERENCES Skuespiller(AnsattID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')
        
    cursor.execute('''
    CREATE TABLE Akt (
        TeaterStykkeID INTEGER NOT NULL,
        Nummer INTEGER NOT NULL,
        Name VARCHAR(30) UNIQUE,
        CONSTRAINT Akt_PK PRIMARY KEY (TeaterStykkeID, Nummer),
        CONSTRAINT Akt_FK FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke(TeaterStykkeID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')

    cursor.execute('''
    CREATE TABLE RolleIAkt (
        RolleID INTEGER NOT NULL,
        TeaterStykkeID INTEGER NOT NULL,
        Nummer INTEGER NOT NULL,
        CONSTRAINT RolleIAkt_PK PRIMARY KEY 
        (RolleID, TeaterStykkeID, Nummer),
        CONSTRAINT RolleIAkt_FK1 FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE,
        CONSTRAINT RolleIAkt_FK2 FOREIGN KEY 
        (TeaterStykkeID, Nummer) REFERENCES Akt(TeaterStykkeID, Nummer) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')
        
    cursor.execute('''
    CREATE TABLE Oppsetning (
        OppsetningID INTEGER NOT NULL,
        Dato VARCHAR(30) NOT NULL,
        TeaterstykkeID INTEGER NOT NULL,
        CONSTRAINT Oppsetning_PK PRIMARY KEY (OppsetningID),
        CONSTRAINT Oppsetning_FK FOREIGN KEY (TeaterstykkeID) 
        REFERENCES TeaterStykke (TeaterStykkeID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')
        
    cursor.execute('''
    CREATE TABLE TeaterStykke (
        TeaterStykkeID INTEGER NOT NULL,
        Navn VARCHAR(30) NOT NULL,
        StartTid VARCHAR(30) NOT NULL,
        Forfatter VARCHAR(30),
        CONSTRAINT TeaterStykkeID_PK PRIMARY KEY (TeaterStykkeID)
        );''')

    cursor.execute('''
    CREATE TABLE VisesI (
        TeaterStykkeID INTEGER NOT NULL,
        SalID INTEGER NOT NULL,
        CONSTRAINT VisesI_PK PRIMARY KEY (TeaterStykkeID, SalID),
        CONSTRAINT VisesI_FK1 FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke (TeaterStykkeID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE,
        Constraint VisesI_FK2 FOREIGN KEY (SalID) REFERENCES Sal(SalID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')

    cursor.execute('''
    Create Table Sal (
        SalID INTEGER NOT NULL,
        Navn VARCHAR(30) UNIQUE,
        Kapasitet INTEGER,
            CONSTRAINT Sal_PK PRIMARY KEY (SalID)
        );''')

    cursor.execute('''
    CREATE TABLE Billett (
        BillettID INTEGER NOT NULL,
        StolNr INTEGER NOT NULL,
        RadNr INTEGER NOT NULL,
        Omraade VARCHAR(30),
        OppsetningID INTEGER NOT NULL,
        Type VARCHAR(30) NOT NULL,
        OrdreID INTEGER NOT NULL,
        TeaterStykkeID INTEGER NOT NULL,
        CONSTRAINT Billett_PK PRIMARY KEY (BillettID),
        CONSTRAINT Billett_FK1 FOREIGN KEY (OrdreID) 
        REFERENCES Ordre(OrdreID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        CONSTRAINT Billett_FK2 FOREIGN KEY (Type, TeaterStykkeID) 
        REFERENCES BillettType(Type, TeaterStykkeID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        CONSTRAINT Billett_FK3 FOREIGN KEY (OppsetningID) 
        REFERENCES Oppsetning(OppsetningID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );	''')
        
    cursor.execute('''
    CREATE TABLE BillettType (
        Type VARCHAR(30) NOT NULL,
        TeaterStykkeID INTEGER NOT NULL,
        Pris INTEGER NOT NULL,
        CONSTRAINT BillettType_PK PRIMARY KEY (Type, TeaterStykkeID),
        CONSTRAINT BilettType_FK FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke(TeaterStykkeID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')
    
    cursor.execute('''
    CREATE TABLE Ordre (
        OrdreID INTEGER NOT NULL,
        Dato VARCHAR(30) NOT NULL,
        Klokkeslett VARCHAR(30) NOT NULL,
        KundeID INTEGER NOT NULL,
        CONSTRAINT Ordre_PK PRIMARY KEY (OrdreID),
        CONSTRAINT Ordre_FK FOREIGN KEY (KundeID) REFERENCES Kunde(KundeID) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE
        );''')
    
    cursor.execute('''
    CREATE TABLE Kunde (
        KundeID INTEGER NOT NULL,
        TelefonNr INTEGER UNIQUE NOT NULL,
        Navn VARCHAR(30) NOT NULL,
        Adresse VARCHAR(30) NOT NULL,
        CONSTRAINT Kunde_PK PRIMARY KEY (KundeID) 
        );''')
    
    con.commit()
    con.close()
    return None

#table_initialization()

