# Import für die Process Discovery
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualizer
import pm4py
from overview import df
import pandas as pd

# 1. Directly-Follows Graph (DFG) ermitteln
# case_id und activity sind standardmäßig 'case:concept:name' und 'concept:name'
dfg = dfg_discovery.apply(df)

# 2. Die Top 10 der häufigsten Übergänge (Sequenzen) anzeigen
print("\n--- TOP 10 DIREKTE AKTIVITÄTSÜBERGÄNGE (DFG) ---")
# Konvertieren Sie das DFG-Dictionary für die bessere Darstellung in ein DataFrame
dfg_series = pd.Series(dfg).sort_values(ascending=False)
print(dfg_series.head(10))

# 3. Den DFG visualisieren (erzeugt eine .png- oder .svg-Datei)
# Hinweis: Das Log muss eventuell noch einmal als pm4py-Log geladen werden
log = pm4py.convert_to_event_log(df) # Konvertiert das DataFrame zurück
gviz = dfg_visualizer.apply(dfg, log=log, parameters={dfg_visualizer.Variants.FREQUENCY.value.Parameters.ACTIVITY_KEY: 'concept:name'})
dfg_visualizer.view(gviz)
# Oder speichern: dfg_visualizer.save(gviz, "dfg_bpi_2017.png")
