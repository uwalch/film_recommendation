import pandas as pd

# Beispiel Daten für Filmdaten (Metadaten) in einer CSV-Struktur
film_data = {
    'Film_ID': [101, 102, 103, 104, 105],
    'Titel': ['Inception', 'The Matrix', 'Interstellar', 'Avatar', 'The Dark Knight'],
    'Regisseur': ['Christopher Nolan', 'Lana Wachowski', 'Christopher Nolan', 'James Cameron', 'Christopher Nolan'],
    'Genre': ['Sci-Fi', 'Action', 'Sci-Fi', 'Adventure', 'Action'],
    'Erscheinungsjahr': [2010, 1999, 2014, 2009, 2008],
    'Schauspieler': ['Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page', 
                     'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss', 
                     'Matthew McConaughey, Anne Hathaway, Jessica Chastain',
                     'Sam Worthington, Zoe Saldana, Sigourney Weaver',
                     'Christian Bale, Heath Ledger, Aaron Eckhart'],
    'Produktionsfirma': ['Warner Bros.', 'Warner Bros.', 'Paramount Pictures', '20th Century Fox', 'Warner Bros.'],
    'Laufzeit_Minuten': [148, 136, 169, 162, 152],
    'Bewertung_IMDb': [8.8, 8.7, 8.6, 7.8, 9.0],
    'Bewertung_RottenTomatoes': [87, 88, 72, 82, 94]
}

# DataFrame erstellen
film_df = pd.DataFrame(film_data)

# CSV Datei erstellen und speichern
film_file_path = 'filmdaten_metadaten_example.csv'
film_df.to_csv(film_file_path, index=False)

film_file_path
