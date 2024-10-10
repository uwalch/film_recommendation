import pytest
import csv

# pytest -s d:/VSCode/film_recommendation/tests/main/tc01_csv_counter.py
# len muss auf die aktuelle CSV Datei angepasst sein
# Meldung sind daher auch nicht immer passend

def test_fake_userdata_csv_datei():
    dateiname = 'fake_userdata.csv'
    with open(dateiname, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        zeilen = list(reader)
        if len(zeilen) == 100001:
            print("Erfolg: Die Datei enthält einen Header und 100 Datensätze.")
        else:
            pytest.fail(f"Fehler: Die Datei sollte einen Header und 100 Datensätze haben, aber es wurden {len(zeilen)-1} Datensätze gefunden.")


def test_filmdaten_metadaten_csv_datei():
    dateiname = 'filmdaten_metadaten_100.csv'
    with open(dateiname, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        zeilen = list(reader)
        if len(zeilen) == 101:
            print("Erfolg: Die Datei enthält einen Header und 100 Datensätze.")
        else:
            pytest.fail(f"Fehler: Die Datei sollte einen Header und 100 Datensätze haben, aber es wurden {len(zeilen)-1} Datensätze gefunden.")


def test_userdata_film_filmdauer_csv_datei():
    dateiname = 'userdata_film_filmdauer.csv'
    with open(dateiname, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        zeilen = list(reader)
        if len(zeilen) == 100001:
            print("Erfolg: Die Datei enthält einen Header und 100 Datensätze.")
        else:
            pytest.fail(f"Fehler: Die Datei sollte einen Header und 100 Datensätze haben, aber es wurden {len(zeilen)-1} Datensätze gefunden.")
