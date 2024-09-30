-- Erstelle eine Tabelle für Kundeninformationen

CREATE TABLE kunden (
    KundenNr VARCHAR(50) PRIMARY KEY,
    Vorname VARCHAR(100),
    Nachname VARCHAR(100),
    Stadt VARCHAR(100),
    Alter INT,
    Geschlecht VARCHAR(10)
);


/*
   Das obige SQL erstellt eine Tabelle 'kunden', 
   die grundlegende Informationen über Kunden enthält.
   Die Spalte 'kunden_nr' ist der Primärschlüssel.
*/