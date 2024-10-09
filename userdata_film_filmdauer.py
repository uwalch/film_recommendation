import csv
import random
from faker import Faker

# Erstellen eines Faker-Objekts
fake = Faker()

# Benutzereingabe für die Anzahl der Datensätze
anzahl_datensaetze = int(input("Wie viele Datensätze möchten Sie erstellen? "))

# CSV-Dateiname
csv_datei = 'userdata_film_filmdauer.csv'

# Erstellen der CSV-Datei und Hinzufügen der Daten
with open(csv_datei, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Schreiben der Kopfzeile
    writer.writerow(['KundenNr', 'Film1', 'Film1Dauer', 'Film2', 'Film2Dauer', 'Film3', 'Film3Dauer'])
    
    # Generieren und Schreiben der Datensätze
    for _ in range(anzahl_datensaetze):
        kunden_nr = fake.unique.random_int(min=10000, max=100000000)
        film1 = random.randint(101, 200)
        film1_dauer = random.randint(1, 60)
        film2 = random.randint(101, 200)
        film2_dauer = random.randint(1, 60)
        film3 = random.randint(101, 200)
        film3_dauer = random.randint(1, 60)
        
        # Schreiben der Datenzeile
        writer.writerow([kunden_nr, film1, film1_dauer, film2, film2_dauer, film3, film3_dauer])

print(f"{anzahl_datensaetze} Datensätze wurden erfolgreich in {csv_datei} gespeichert.")
