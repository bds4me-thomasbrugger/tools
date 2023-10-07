import csv
import random
import os

# Erstellen Sie ein Verzeichnis zum Speichern der CSV-Dateien
if not os.path.exists("csv_files"):
    os.makedirs("csv_files")

# Anzahl der Dateien und Datensätze pro Datei
anzahl_dateien = 12
max_datensatz_pro_datei = 1000000

# Schleife zum Erstellen von 12 CSV-Dateien
for monat_index in range(1, anzahl_dateien + 1):
    dateiname = f"csv_files/{monat_index}.csv"

    # CSV-Datei öffnen und schreiben
    with open(dateiname, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Header schreiben
        writer.writerow(["Jahr", "Monat", "Kundennummer", "Datum", "Abo vorhanden"])

        # Zufällige Daten für jeden Datensatz generieren
        for datensatz in range(max_datensatz_pro_datei):
            jahr = "2023"
            kundennummer = random.randint(100000, 999999)
            datum = f"{random.randint(1, 28)}.{monat_index}.{jahr}"
            abo_vorhanden = random.choice(["ja", "nein", "Widerruf"])
            
            # Daten in die CSV schreiben
            writer.writerow([jahr, monat_index, kundennummer, datum, abo_vorhanden])

print(f"{anzahl_dateien} CSV-Dateien wurden erstellt.")
