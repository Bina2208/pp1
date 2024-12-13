import pandas as pd
import plotly.express as px

# Datei laden (ersetze 'datei.csv' mit dem Pfad zu deiner Datei)
datei_pfad = '../Dataset1-EVs_and_chargers_by_state.csv'
df = pd.read_csv(datei_pfad, thousands=',', decimal='.')

# Anzeigen aller Spalten und der ersten 5 Zeilen
# pd.set_option('display.max_columns', None)

# Prüfen ob die Datei geladen wurde
print(df.head())
# Datentypen anzeigen
print("Types: ", df.dtypes)

# statistische Analayse
print("\nWichtige Statistiken: ")
print(df.describe())

# Entfernen der Zeilen für Median, Average und Total
filter_values = ['Median', 'Average', 'Total']
df_filtered = df[~df['State'].isin(filter_values)].copy()
# df_filtered.loc[:,'Total Evs'] = pd.to_numeric(df_filtered['Total Evs'], errors='coerce')
# Überprüfen, ob die gefilterten Daten korrekt geladen wurden
print("\nGefilterte Daten:")
print(df_filtered)

number_of_evs = df_filtered['Total Evs']
number_of_chargers = df_filtered['Total Chargers']

# Scatterplot erstellen
fig = px.scatter(
    df_filtered, # DataFrame
    title='Number of Evs and Chargers by State',
    x=number_of_evs, 
    y=number_of_chargers, 
    labels={'x': 'Number of Evs', 'y': 'Number of Chargers'},
    hover_name='State',
    color='State')

# Scatterplot anzeigen
fig.show()
