import pandas as pd
import plotly.express as px

# Datei laden (ersetze 'datei.csv' mit dem Pfad zu deiner Datei)
datei_pfad = '../Dataset1-EVs_and_chargers_by_state.csv'
df = pd.read_csv(datei_pfad, thousands=',', decimal='.')

# Prüfen ob die Datei geladen wurde
print(df.head())
# Datentypen anzeigen
print("Types: ", df.dtypes)

# Entfernen der Zeilen für Median, Average und Total
filter_values = ['Median', 'Average', 'Total']
df_filtered = df[~df['State'].isin(filter_values)].copy()



fig = px.bar(
    df_filtered,
    title="EVs and chargers by state",
    x="State", 
    y=["Total Evs", "Total Chargers"],
    labels={'value': 'Number of Chargers'})

fig.show()