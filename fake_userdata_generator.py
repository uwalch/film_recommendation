from faker import Faker
import csv
import random

# Setze den Seed für wiederholbare Ergebnisse
Faker.seed(1234)


def generate_fake_data(total_records):
    fake = Faker('de_DE')
    fieldnames = ['KundenNr','Vorname', 'Nachname', 'Stadt', 'Alter', 'Geschlecht']

    with open('fake_userdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(total_records):
            geschlecht = fake.random_element(elements=('Männlich', 'Weiblich'))
            if geschlecht == 'Männlich':
                vorname = fake.first_name_male()
            else:
                vorname = fake.first_name_female()
            nachname = fake.last_name()
            stadt = fake.city()
            alter = fake.random_int(min=18, max=90)
            kundennr = fake.unique.random_int(min=10000, max=100000000)

            writer.writerow({
                'KundenNr': kundennr,
                'Vorname': vorname,
                'Nachname': nachname,
                'Stadt': stadt,
                'Alter': alter,
                'Geschlecht': geschlecht
            })

if __name__ == '__main__':
    try:
        total_records = int(input("Geben Sie die Anzahl der zu generierenden Datensätze ein: "))
        generate_fake_data(total_records)
        print(f"{total_records} Datensätze wurden in 'fake_data.csv' gespeichert.")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")
