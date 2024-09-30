import pandas as pd
import psycopg2

# Verbindung zur PostgreSQL-Datenbank herstellen
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",  # oder der entsprechende Server
    port="5432"
)

# CSV-Datei laden
df = pd.read_csv('fake_userdata.csv')

# Daten in die PostgreSQL-Tabelle importieren
cursor = conn.cursor()
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO kunden (kundennr, vorname, nachname, stadt, alter, geschlecht)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['KundenNr'], row['Vorname'], row['Nachname'], row['Stadt'], row['Alter'], row['Geschlecht']))

conn.commit()
cursor.close()
conn.close()
