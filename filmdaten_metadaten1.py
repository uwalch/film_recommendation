import pandas as pd
from faker import Faker
import random

# Faker-Instanz erstellen
fake = Faker()

# Beispiel-Genres und Produktionsfirmen
genres = ['Sci-Fi', 'Action', 'Adventure', 'Drama', 'Comedy', 'Horror', 'Thriller', 'Fantasy', 'Romance']
production_companies = ['Warner Bros.', 'Paramount Pictures', '20th Century Fox', 'Universal Pictures', 'Sony Pictures', 'MGM']
directors = ['Christopher Nolan', 'Lana Wachowski', 'James Cameron', 'Steven Spielberg', 'Quentin Tarantino', 'Martin Scorsese']

# Leere Liste für Filmdaten
film_data = {
    'Film_ID': [],
    'Titel': [],
    'Regisseur': [],
    'Genre': [],
    'Erscheinungsjahr': [],
    'Schauspieler': [],
    'Produktionsfirma': [],
    'Laufzeit_Minuten': [],
    'Bewertung_IMDb': [],
    'Bewertung_RottenTomatoes': []
}

# 100 zufällige Filme generieren
for i in range(1, 101):
    film_data['Film_ID'].append(i + 100)
    film_data['Titel'].append(fake.catch_phrase())
    film_data['Regisseur'].append(random.choice(directors))
    film_data['Genre'].append(random.choice(genres))
    film_data['Erscheinungsjahr'].append(random.randint(1980, 2024))
    film_data['Schauspieler'].append(fake.name() + ', ' + fake.name() + ', ' + fake.name())
    film_data['Produktionsfirma'].append(random.choice(production_companies))
    film_data['Laufzeit_Minuten'].append(random.randint(80, 180))
    film_data['Bewertung_IMDb'].append(round(random.uniform(6.0, 9.5), 1))
    film_data['Bewertung_RottenTomatoes'].append(random.randint(50, 100))

# DataFrame erstellen
film_df = pd.DataFrame(film_data)

# CSV-Datei speichern
film_file_path = 'filmdaten_metadaten_100.csv'
film_df.to_csv(film_file_path, index=False)

film_file_path
