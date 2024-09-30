import pandas as pd

def finde_duplikate_pandas(dateiname):
    df = pd.read_csv(dateiname, encoding='utf-8')
    duplikate = df[df.duplicated(subset='KundenNr', keep=False)]

    if not duplikate.empty:
        print("Folgende Kundennummern kommen mehrfach vor:")
        duplikate_anzahl = duplikate['KundenNr'].value_counts()
        for nr, anzahl in duplikate_anzahl.items():
            print(f"KundenNr: {nr}, Anzahl: {anzahl}")
    else:
        print("Keine Duplikate gefunden.")

# Beispielaufruf
finde_duplikate_pandas('fake_userdata.csv')
