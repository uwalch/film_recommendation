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

print("\n")
# SQL-Abfrage, um die Daten aus der 'kunden'-Tabelle abzurufen
query = "SELECT * FROM kunden"

print("\n")
# Daten in ein Pandas DataFrame laden
df = pd.read_sql_query(query, conn)

# Verbindung schließen
conn.close()

# Daten analysieren
# Beispielanalysen:

print("\n")
# 1. Überblick über die Daten
print(df.head())

print("\n")
# 2. Statistische Zusammenfassung
print(df.describe())

print("\n")
# 3. Anzahl der Kunden nach Geschlecht
geschlecht_counts = df['geschlecht'].value_counts()
print(geschlecht_counts)

print("\n")
# 4. Durchschnittsalter der Kunden
durchschnittsalter = df['alter'].mean()
print(f"Durchschnittsalter der Kunden: {durchschnittsalter}")

print("\n")
# 5. Kunden nach Stadt gruppieren und zählen
stadt_counts = df['stadt'].value_counts()
print(stadt_counts)

# Weitere Analysen können hier hinzugefügt werden
