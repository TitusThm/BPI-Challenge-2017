import pm4py
import pandas as pd
import os

# 1. Dateipfad anpassen
# Ersetzen Sie 'pfad/zur/ihrer/datei.xes' durch den tatsächlichen Pfad zu Ihrem Event-Log
file_path = '/Users/titusthamm/Library/Mobile Documents/com~apple~CloudDocs/Masterstudium/3. Semester/Praktikum/1. Assignment/BPI Challenge 2017_1_all/BPI Challenge 2017_1_all.xes'

# Überprüfen, ob die Datei existiert
if not os.path.exists(file_path):
    print(f"FEHLER: Datei nicht gefunden unter: {file_path}")
else:
    # 2. Event Log laden
    print(f"Lade Event Log von: {file_path}")
    log = pm4py.read_xes(file_path)

    # 3. Konvertierung zu Pandas DataFrame für einfachere Inspektion
    # Event Logs in pm4py sind Sammlungen von Traces (Fällen), die wiederum Sammlungen von Events (Aktivitäten) sind
    df = pm4py.convert_to_dataframe(log)

    print("\n--- ERSTER ÜBERBLICK (HEAD) ---")
    print(df.head())

    print("\n--- SCHLÜSSELINFORMATIONEN ---")
    
    # 4. Anzahl der Fälle (Traces)
    num_cases = df['case:concept:name'].nunique()
    print(f"Gesamtzahl der Fälle (Kreditanträge): {num_cases}")

    # 5. Anzahl der Events (Aktivitäten)
    num_events = len(df)
    print(f"Gesamtzahl der Events (Prozessschritte): {num_events}")

    # 6. Zeitraum des Logs
    start_date = df['time:timestamp'].min()
    end_date = df['time:timestamp'].max()
    print(f"Log-Zeitraum: {start_date} bis {end_date}")

    # 7. Die häufigsten Aktivitäten
    print("\n--- TOP 10 AKTIVITÄTEN ---")
    print(df['concept:name'].value_counts().head(10))

    # 8. Überblick über die Spalten (Attribute)
    print("\n--- LOG-ATTRIBUTE (SPALTEN) ---")
    print(df.info())
