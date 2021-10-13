import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import folium
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
pio.templates.default = 'seaborn'
import statsmodels.api as sm

st.beta_set_page_config(layout="wide")

st.title('Elektrische auto dashboard')

st.write("""
***
""")

col1, col2 = st.beta_columns(2)

df1 = pd.read_csv('RDW_csv.csv')

# Alleen de merken meenemen die meer dan 500 counts bevatten.
df_merk = df1[df1['Merk'].map(df1['Merk'].value_counts()) > 500]


col1.header("Algemene informatie elektrische auto's")

# Histogram van het aantal per merk, waarbij we kijken naar de merken met meer dan 500 counts. 
fig = go.Figure()

fig = px.histogram(data_frame=df_merk, 
                   x="Merk", color='Merk').update_xaxes(categoryorder='total descending')
fig.update_layout(
    title_text='Aantallen per automerk', # title of plot
    title_x=0.5,
    xaxis_title_text="Automerk", # xaxis label
    yaxis_title_text="Aantal auto's")

col1.plotly_chart(fig)



col2.header("🚗")
# Aantal zitplaatsen van een object naar een categorie veranderen. 
df1['Aantal zitplaatsen'] = df1['Aantal zitplaatsen'].astype('category')
assert df1['Aantal zitplaatsen'].dtype == 'category'
print(df1['Aantal zitplaatsen'].describe())

# Selecteren op Handelsbenamen met meer dan 3000 counts. 
df_veel = df1[df1['Handelsbenaming'].map(df1['Handelsbenaming'].value_counts()) > 3000]

# Histogram waarbij per handelsbenaming wordt gekeken naar het aantal zitplaatsen, met dropdown.
# Waarbij we kijken naar de handelsbenaming met meer dan 3000 counts. 
fig = go.Figure()

fig = px.histogram(data_frame=df_veel, 
                   x="Handelsbenaming", 
                   color='Aantal zitplaatsen')

fig.update_layout(
    title_text='Handelsbenaming met zitplaats', # title of plot
    title_x=0.5,
    xaxis_title_text="Handelsbenaming", # xaxis label
    yaxis_title_text="Aantal zitplaatsen") 

dropdown_buttons = [
{'label': "ALL", 'method': "update", 'args': [{"visible": [True, True, True,True,True,True,True,True,True]}, {"title": "ALL"}]},
{'label': "1.0", 'method': "update", 'args': [{"visible": [False, False, False,False,True,False,False,False,False]}, {"title": 1.0}]},
{'label': "2.0", 'method': "update", 'args': [{"visible": [False, False, False,False,False,False,True,False,False]}, {"title": 2.0}]},
{'label': "3.0", 'method': "update", 'args': [{"visible": [False, False, False,False,False,True,False,False,False]}, {"title": 3.0}]},
{'label': "4.0", 'method': "update", 'args': [{"visible": [False, False, False, True, False,False,False,False,False]}, {"title": 4.0}]},
{'label': "5.0", 'method': "update", 'args': [{"visible": [True, False, False,False,False,False,False,False,False]}, {"title": 5.0}]},
{'label': "6.0", 'method': "update", 'args': [{"visible": [False, False, True,False,False,False,False,False,False]}, {"title": 6.0}]},
{'label': "7.0", 'method': "update", 'args': [{"visible": [False, True, False,False,False,False,False,False,False]}, {"title": 7.0}]},
{'label': "8.0", 'method': "update", 'args': [{"visible": [False, False, False,False,False,False,False,True,False]}, {"title": 8.0}]},
{'label': "9.0", 'method': "update", 'args': [{"visible": [False, False, False,False,False,False,False,False,True]}, {"title": 9.0}]},

]

# Update the figure to add dropdown menu
fig.update_layout({'updatemenus': [{'active': 0, 'buttons': dropdown_buttons}]})
col2.plotly_chart(fig)



#Kolom 1 rij 2
# Histogram van het aantal per kleur. 
fig = go.Figure()

fig = px.histogram(data_frame = df1, 
                   x = "Eerste kleur",
                   color = df1['Eerste kleur'],
                   color_discrete_sequence=["grey", "ivory", "black", "blue", "red", "brown", "yellow", 
                                           "green", "orange", "purple", "beige", "tan"])


fig.update_layout(
    title_text="Aantal auto's per kleur", # title of plot
    title_x=0.5,
    xaxis_title_text="Gekozen eerste kleur", # xaxis label
    yaxis_title_text="Aantal auto's", legend_title = 'Kleur')

col1.plotly_chart(fig)

#Kolom 2 rij 2
fig = go.Figure()

fig = px.histogram(data_frame=df_merk, 
                   x="Merk", 
                   color='Eerste kleur',
                   color_discrete_sequence=["grey", "ivory", "black", "blue", "red", "brown", "yellow", 
                                           "green", "orange", "purple", "beige", "tan"])
fig.update_layout(
    title_text='Soort kleur per automerk', # title of plot
    title_x=0.5,
    xaxis_title_text="Merk", # xaxis label
    yaxis_title_text="Aantal auto's")                     
                     
                     
dropdown_buttons = [{'label':"All", 'method':"update", 'args':[{"visible":[True,True,True,True,True,True,True,True,True,True,True, True, True]},{"title":"All"}]},
                    {'label':"Grijs", 'method':"update", 'args':[{"visible":[True,False,False,False,False,False,False,False,False,False, False, False]},{"title":"Grijs"}]},
                    {'label':"Wit", 'method':"update", 'args':[{"visible":[False,True,False,False,False,False,False,False,False,False, False, False]}, {"title":"Wit"}]},
                    {'label':"Zwart", 'method':"update", 'args':[{"visible":[False,False,True,False,False,False,False,False,False,False, False, False]}, {"title":"Zwart"}]},
                    {'label':"Blauw", 'method':"update", 'args':[{"visible":[False,False,False,True,False,False,False,False,False,False, False, False]}, {"title":"Blauw"}]},
                    {'label':"Rood", 'method':"update", 'args':[{"visible":[False,False,False,False,True,False,False,False,False,False, False, False]}, {"title":"Rood"}]},
                    {'label':"Bruin", 'method':"update", 'args':[{"visible":[False,False,False,False,False,True,False,False,False,False, False, False]}, {"title":"Bruin"}]},
                    {'label':"Geel", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,True,False,False,False, False, False]}, {"title":"Geel"}]},
                    {'label':"Groen", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,True,False,False, False, False]}, {"title":"Groen"}]},
                    {'label':"Oranje", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,True,False, False, False]}, {"title":"Oranje"}]}, 
                    {'label':"Paars", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,True, False, False]}, {"title":"Paars"}]},
                    {'label':"Beige", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False, True, False]}, {"title":"Beige"}]},
                    {'label':"Creme", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False, False, True]}, {"title":"Creme"}]}]                    
  

#Update de figuur om de dropdown buttons toe te voegen en laat de figuur zien
fig.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

col2.plotly_chart(fig)

#Kolom 1 rij 3
# Histogram waarbij per merk wordt gekeken naar de inrichting, met dropdown.
# Waarbij we kijken naar de merken met meer dan 500 counts. 
fig = go.Figure()

fig = px.histogram(data_frame=df_merk, 
                   x="Inrichting", color='Merk')
fig.update_layout(
    title_text='Soort inrichting per automerk', # title of plot
    title_x=0.5,
    xaxis_title_text="Inrichting", # xaxis label
    yaxis_title_text="Aantal auto's")                     
                     
dropdown_buttons = [{'label':"All", 'method':"update", 'args':[{"visible":[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]}, {"title":"All"}]}, 
                    {'label':"Volkswagen", 'method':"update", 'args':[{"visible":[True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Volkswagen"}]},
                    {'label':"Tesla", 'method':"update", 'args':[{"visible":[False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Tesla"}]},
                    {'label':"Renault", 'method':"update", 'args':[{"visible":[False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Renault"}]},
                    {'label':"Hyundai", 'method':"update", 'args':[{"visible":[False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Hyundi"}]},
                    {'label':"Jaguar", 'method':"update", 'args':[{"visible":[False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Jaguar"}]},
                    {'label':"Polestar", 'method':"update", 'args':[{"visible":[False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Polestar"}]},
                    {'label':"Peugot", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Peugot"}]},
                    {'label':"BMW", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"BMW"}]},
                    {'label':"Sköda", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Sköda"}]},
                    
                    {'label':"KIA", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"KIA"}]},
                    {'label':"Opel", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Opel"}]},
                    {'label':"Smart", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Smart"}]},
                    {'label':"Nissan", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Nissan"}]},
                    {'label':"Audi", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Audi"}]},
                    {'label':"Mazda", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Mazda"}]},
                    {'label':"Ford", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Ford"}]},
                    {'label':"Mercedes-Benz", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"Mercedes-Benz":"All"}]},
                    {'label':"Citroën", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Citroën"}]},
                    {'label':"Seat", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Seat"}]},
                    
                    {'label':"MG", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"MG"}]},
                    {'label':"Mini", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Mini"}]},
                    {'label':"Fiat", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Fiat"}]},
                    {'label':"Porsche", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Porsche"}]},
                    {'label':"XPENG", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"XPENG"}]},
                    {'label':"Volvo", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Volvo"}]},
                    {'label':"Lexus", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Lexus"}]},
                    {'label':"Mitsubishi", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Mitsubishi"}]},
                    {'label':"Toyota", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Toyota"}]},
                    {'label':"Aiways", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Aiways"}]},
                    
                    {'label':"Honda", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Honda"}]},
                    {'label':"Maxus", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Maxus"}]},
                    {'label':"DS", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"DS"}]},
                    {'label':"Dacia", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Dacia"}]},
                    {'label':"VW-Porsche", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"VW-Porsche"}]},
                    {'label':"Chevrolet", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Chevrolet"}]},
                    {'label':"Seres", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Seres"}]},
                    {'label':"JAC", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"JAC"}]},
                    {'label':"N.S.U.", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"N.S.U."}]},
                    {'label':"Mia", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Mia"}]},
                    
                    {'label':"E GO", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"E GO"}]},
                    {'label':"BYD", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"BYD"}]},
                    {'label':"Rover", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Rover"}]},
                    {'label':"Austin", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Austin"}]},
                    {'label':"THINK", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"THINK"}]},
                    {'label':"Lotus", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Lotus"}]},
                    {'label':"DFSK", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"DFSK"}]},
                    {'label':"Jeep", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Jeep"}]},
                    {'label':"Daihtsu", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Daihtsu"}]},
                    {'label':"Aston-Martin", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"Aston-Martin"}]},
                    
                    {'label':"MAN", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False]}, {"title":"MAN"}]},
                    {'label':"Zotye", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False]}, {"title":"Zotye"}]},
                    {'label':"Matra", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False]}, {"title":"Matra"}]},
                    {'label':"Cecomp", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False]}, {"title":"Cecomp"}]},
                    {'label':"Poessl", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False]}, {"title":"Poessl"}]},
                    {'label':"MW Motors SRO", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False]}, {"title":"MX Motors SRO"}]},
                    {'label':"Alfa Romeo", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False]}, {"title":"Alfa Romeo"}]},
                    {'label':"German E-Cars", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False]}, {"title":"German E-Cars"}]},
                    {'label':"SAAB", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False]}, {"title":"SAAB"}]},
                    {'label':"Stella", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False]}, {"title":"Stella"}]},
                    
                    {'label':"Morris", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False]}, {"title":"Morris"}]},
                    {'label':"Trabant", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True]}, {"title":"Trabant"}]}
                   ]

#Update de figuur om de dropdown buttons toe te voegen en laat de figuur zien
fig.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

col1.plotly_chart(fig)



# Histogram van de hoeveelheid auto met het soort inrichting met een dropdown menu. 
fig = go.Figure()
fig = px.histogram(data_frame=df1, 
                   x="Inrichting", color='Inrichting')
fig.update_layout(
    title_text='Soort inrichting', # title of plot
    title_x=0.5,
    xaxis_title_text="Inrichting", # xaxis label
    yaxis_title_text="Aantal auto's")

dropdown_buttons = [{'label':"All", 'method':"update", 'args':[{"visible":[True,True,True,True,True,True,True,True,True,True,True]},{"title":"All"}]},
                    {'label':"Stationwagen", 'method':"update", 'args':[{"visible":[True,False,False,False,False,False,False,False,False,False]},{"title":"Stationwagen"}]},
                    {'label':"Sedan", 'method':"update", 'args':[{"visible":[False,True,False,False,False,False,False,False,False,False]}, {"title":"Sedan"}]},
                    {'label':"Hatchback", 'method':"update", 'args':[{"visible":[False,False,True,False,False,False,False,False,False,False]}, {"title":"Hatchback"}]},
                    {'label':"Multi-Purpose Vehicle", 'method':"update", 'args':[{"visible":[False,False,False,True,False,False,False,False,False,False]}, {"title":"Multi-Purpose Vehicle"}]},
                    {'label':"Coupe", 'method':"update", 'args':[{"visible":[False,False,False,False,True,False,False,False,False,False]}, {"title":"Coupe"}]},
                    {'label':"Rolstoel toegankelijk", 'method':"update", 'args':[{"visible":[False,False,False,False,False,True,False,False,False,False]}, {"title":"Rolstoel toegankelijk"}]},
                    {'label':"Cabriolet", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,True,False,False,False]}, {"title":"Cabriolet"}]},
                    {'label':"Niet geregistreerd", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,True,False,False]}, {"title":"Niet geregistreerd"}]},
                    {'label':"Kampeerwagen", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,True,False]}, {"title":"Kampeerwagen"}]}, 
                    {'label':"Speciale groep", 'method':"update", 'args':[{"visible":[False,False,False,False,False,False,False,False,False,True]}, {"title":"Speciale groep"}]}]                    
  
                     
           
#Update de figuur om de dropdown buttons toe te voegen en laat de figuur zien
fig.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

col2.plotly_chart(fig)










#INGEEEEEEE
#Laad en lees df3 in 
df4 = pd.read_csv('df3.csv')
df5 = df4.drop(columns = 'Unnamed: 0')

#Code voor interactieve barplot met plotly.express
fig1 = px.bar(df5, 
              x = "DagLabelKort", 
              y = "ChargeTime", 
              color = "DagLabelKort", 
              hover_name = "Started_datum",
              animation_frame = "MaandLabelKort", 
              labels = {'DagLabelKort':'Dag', 'MaandLabelKort':'Maand', 'ChargeTime':'Totale oplaadtijd (in uren)'}, 
              opacity = 0.5,
              title = 'Totale oplaadtijd van de elektrische autos per dag per maand in 2018')

#Laat de figuur zien
st.plotly_chart(fig1)

#Code voor interactieve histogram met plotly.express
fig2 = px.histogram(df5, 
                    x = 'Started_datum', 
                    y = 'ChargeTime', 
                    color = 'MaandLabelKort', 
                    hover_name = 'Started_datum', 
                    labels = {'MaandLabelKort':'Maand', 'Started_datum':'Maand 2018', 'ChargeTime':'oplaadtijd (in uren)'}, 
                    opacity = 0.5, 
                    range_x = (df5['Started_datum'].min(), df5['Started_datum'].max()),
                    histfunc = 'avg',
                    nbins = 12, 
                    title = 'Gemiddelde oplaadtijd van de elektrische autos per maand in 2018')

#Dropdown buttons
dropdown_buttons = [
    {'label':"2018", 'method':"update", 'args':[{"visible":[True, True, True, True, True, True, True, True, True, True, True, True]}]},
    {'label':"jan", 'method':"update", 'args':[{"visible":[True, False, False, False, False, False, False, False, False, False, False, False]}]},
    {'label':"feb", 'method':"update", 'args':[{"visible":[False, True, False, False, False, False, False, False, False, False, False, False]}]},
    {'label':"mrt", 'method':"update", 'args':[{"visible":[False, False, True, False, False, False, False, False, False, False, False, False]}]}, 
    {'label':"apr", 'method':"update", 'args':[{"visible":[False, False, False, True, False, False, False, False, False, False, False, False]}]}, 
    {'label':"mei", 'method':"update", 'args':[{"visible":[False, False, False, False, True, False, False, False, False, False, False, False]}]}, 
    {'label':"jun", 'method':"update", 'args':[{"visible":[False, False, False, False, False, True, False, False, False, False, False, False]}]}, 
    {'label':"jul", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, True, False, False, False, False, False]}]}, 
    {'label':"aug", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, True, False, False, False, False]}]}, 
    {'label':"sep", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, True, False, False, False]}]}, 
    {'label':"okt", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, True, False, False]}]}, 
    {'label':"nov", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, False, True, False]}]}, 
    {'label':"dec", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, False, False, True]}]}
]

#Lijn met annotatie van de gemiddelde oplaadtijd
fig2.add_hline(y = df5['ChargeTime'].mean(), 
               line_dash = "dot", 
               line_width = 2,
               annotation_text = "Gemiddelde oplaadtijd (in uren)", 
               annotation_position = "top right")

#Lijn met annotatie van de mediane oplaadtijd
fig2.add_hline(y = df5['ChargeTime'].median(), 
               line_dash = "dot", 
               line_width = 2, 
               annotation_text = "Mediane oplaadtijd (in uren)", 
               annotation_position = "bottom right")

#Update de figuur
fig2.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Laat de figuur zien
st.plotly_chart(fig2)

#Code voor interactieve boxplot met plotly.express
fig3 = px.box(df5, 
              x = 'MaandLabelKort', 
              y = "ChargeTime", 
              color = 'MaandLabelKort', 
              hover_name = 'Started_datum', 
              labels = {'MaandLabelKort':'Maand', 'ChargeTime':'Oplaadtijd (in uren)'}, 
              points = 'all',
              title = 'Oplaadtijd van de elektrische autos per maand in 2018')

#Dropdown buttons
dropdown_buttons = [
    {'label':"2018", 'method':"update", 'args':[{"visible":[True, True, True, True, True, True, True, True, True, True, True, True]}]},
    {'label':"jan", 'method':"update", 'args':[{"visible":[True, False, False, False, False, False, False, False, False, False, False, False]}]},
    {'label':"feb", 'method':"update", 'args':[{"visible":[False, True, False, False, False, False, False, False, False, False, False, False]}]},
    {'label':"mrt", 'method':"update", 'args':[{"visible":[False, False, True, False, False, False, False, False, False, False, False, False]}]}, 
    {'label':"apr", 'method':"update", 'args':[{"visible":[False, False, False, True, False, False, False, False, False, False, False, False]}]}, 
    {'label':"mei", 'method':"update", 'args':[{"visible":[False, False, False, False, True, False, False, False, False, False, False, False]}]}, 
    {'label':"jun", 'method':"update", 'args':[{"visible":[False, False, False, False, False, True, False, False, False, False, False, False]}]}, 
    {'label':"jul", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, True, False, False, False, False, False]}]}, 
    {'label':"aug", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, True, False, False, False, False]}]}, 
    {'label':"sep", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, True, False, False, False]}]}, 
    {'label':"okt", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, True, False, False]}]}, 
    {'label':"nov", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, False, True, False]}]}, 
    {'label':"dec", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, False, False, True]}]}
]

#Lijn met annotatie van de gemiddelde oplaadtijd
fig3.add_hline(y = df5['ChargeTime'].mean(), 
               line_dash = "dot", 
               line_width = 2,
               annotation_text = "Gemiddelde oplaadtijd (in uren)", 
               annotation_position = "top right")

#Update de figuur
fig3.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Laat de figuur zien
st.plotly_chart(fig3)

#Code voor interactieve kansdichtheidsfunctie met plotly.figure_factory
jan = df5[df5['MaandLabelKort'] == 'jan']['ChargeTime']
feb = df5[df5['MaandLabelKort'] == 'feb']['ChargeTime']
mrt = df5[df5['MaandLabelKort'] == 'mrt']['ChargeTime']
apr = df5[df5['MaandLabelKort'] == 'apr']['ChargeTime']
mei = df5[df5['MaandLabelKort'] == 'mei']['ChargeTime']
jun = df5[df5['MaandLabelKort'] == 'jun']['ChargeTime']
jul = df5[df5['MaandLabelKort'] == 'jul']['ChargeTime']
aug = df5[df5['MaandLabelKort'] == 'aug']['ChargeTime']
sep = df5[df5['MaandLabelKort'] == 'sep']['ChargeTime']
okt = df5[df5['MaandLabelKort'] == 'okt']['ChargeTime']
nov = df5[df5['MaandLabelKort'] == 'nov']['ChargeTime']
dec = df5[df5['MaandLabelKort'] == 'dec']['ChargeTime']

data = [jan, feb, mrt, apr, mei, jun, jul, aug, sep, okt, nov, dec]

labels = ['Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'November', 'December']

fig4 = ff.create_distplot(hist_data = data, group_labels = labels, curve_type = 'normal')

#Dropdown buttons
dropdown_buttons = [
    {'label':"2018", 'method':"update", 'args':[{"visible":[True, True, True, True, True, True, True, True, True, True, True, True]}]},
    {'label':"jan", 'method':"update", 'args':[{"visible":[True, False, False, False, False, False, False, False, False, False, False, False]}]},
    {'label':"feb", 'method':"update", 'args':[{"visible":[False, True, False, False, False, False, False, False, False, False, False, False]}]},
    {'label':"mrt", 'method':"update", 'args':[{"visible":[False, False, True, False, False, False, False, False, False, False, False, False]}]}, 
    {'label':"apr", 'method':"update", 'args':[{"visible":[False, False, False, True, False, False, False, False, False, False, False, False]}]}, 
    {'label':"mei", 'method':"update", 'args':[{"visible":[False, False, False, False, True, False, False, False, False, False, False, False]}]}, 
    {'label':"jun", 'method':"update", 'args':[{"visible":[False, False, False, False, False, True, False, False, False, False, False, False]}]}, 
    {'label':"jul", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, True, False, False, False, False, False]}]}, 
    {'label':"aug", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, True, False, False, False, False]}]}, 
    {'label':"sep", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, True, False, False, False]}]}, 
    {'label':"okt", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, True, False, False]}]}, 
    {'label':"nov", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, False, True, False]}]}, 
    {'label':"dec", 'method':"update", 'args':[{"visible":[False, False, False, False, False, False, False, False, False, False, False, True]}]}
]

#Update de figuur
fig4.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]}, 
                   xaxis_title = 'Oplaadtijd (in uren)', 
                   title='Oplaadtijd van de elektrische autos per maand in 2018', 
                   legend = {'traceorder':'normal'})

#Laat de figuur zien
st.plotly_chart(fig4)

#Code voor interactieve scatterplot met plotly.express
fig5 = px.scatter(df5, 
                  x = "TotalEnergy", 
                  y = "ChargeTime", 
                  size = "MaxPower", 
                  hover_name = "Started_datum",
                  color = "DagLabelKort", 
                  animation_frame = "MaandLabelKort",
                  labels = {'DagLabelKort':'Dag', 'MaandLabelKort':'Maand', 'TotalEnergy':'Totaal verbruikte energie (in wattuur)', 
                            'ChargeTime':'Oplaadtijd (in uren)', 'MaxPower':'Maximaal gevraagde vermogen (in watt)'}, 
                  opacity = 0.5, 
                  trendline = 'ols', 
                  trendline_scope = 'overall', 
                  title = 'Totale energie, oplaadtijd en maximaal vermogen van de elektrische autos')

#Laat de figuur zien
st.plotly_chart(fig5)







#YASINNNNNNNN
HVAcords = [52.34590306716925,4.916398740317223]
lat = HVAcords[0]
long = HVAcords[1]

columnNames = ['OperatorTitle','Postcode','town','province','latitude','longitude','distance','connectTypeTitle','connectTypeDiscont','isfastcharge','levelTitle','dateLSU','dateCreated']
rows = []

with open('opencharge_10000.json') as json_file:
        data = json.load(json_file)
        for key,document in enumerate(data):
            #
            operatorInfo = document['OperatorInfo']
            #als er meerdere van dit soort checks er in moeten dan kan je er een functie van maken waarbij als parameter een vervang waarde
            if operatorInfo :
                OperatorTitle = operatorInfo['Title']
            else:
                OperatorTitle = 'unkown'
            #adressinfo columns
            adressInfo = document['AddressInfo']
            #print(adressInfo)
            postcode = adressInfo['Postcode']
            town = adressInfo['Town']
            province = adressInfo['StateOrProvince']
            latitude = adressInfo['Latitude'] 
            longitude = adressInfo['Longitude']
            distance = adressInfo['Distance']
            
            #Connections columns
            connections = document['Connections']
            #print('\n',connections[0],'\n',connections[1])
            if connections:
                connectTypeTitle = connections[0]['ConnectionType']['Title']
                connectTypeDiscont = connections[0]['ConnectionType']['IsDiscontinued']
              
            else:
                connectTypeTitle = 'unkown2'
                connectTypeDiscont = 'unkown3'
        
            if connections and connections[0]['Level']:
                isfastcharge = connections[0]['Level']['IsFastChargeCapable']
                levelTitle = connections[0]['Level']['Title']
            else:
                isfastcharge = False
                levelTitle = 'unkown5'
            
            
            #
            dateLSU = document['DateLastStatusUpdate']
            dateCreated = document['DateCreated']
            #
            rows.append([OperatorTitle,postcode,town,province,latitude,longitude,distance,connectTypeTitle,connectTypeDiscont,isfastcharge,levelTitle,dateLSU,dateCreated])

# #Dataframe van alle stationsinformatie
# df_stations = pd.DataFrame(stations)
# print(df_stations.columns)

chargingDf = pd.DataFrame(rows, columns=columnNames)
print(chargingDf.columns())


# #solution: merge a new dataframe that contains the correct geograhpal information on de 'postcode' column
# postcodedf = pd.read_csv('postcode_dim.csv',sep=';',engine='python')

# DF_charging = chargingDf.merge(postcodedf, left_on='Postcode',right_on='Postcode',suffixes=('_C','_P'))

# columns = ['OperatorTitle','Postcode','latitude','longitude','distance','connectTypeTitle','connectTypeDiscont','isfastcharge','levelTitle','dateLSU','dateCreated','Gemeente','Provincie','Latitude','Longitude']
# DF_charging = DF_charging[columns]


st.markdown(""" 
blip bloop bloop 
""")

st.write("""
***
""")

st.markdown(""" 
**Bronnenlijst**\n
DataCamp. (z.d.). DataCamp. Geraadpleegd op 10 oktober 2021, 
van https://www.datacamp.com/users/sign_in?redirect=https%3A%2F%2Flearn.datacamp.com%2F

\n
plotly.express.timeline — 5.3.1 documentation. (n.d.). Plotly. Geraadpleegd op 29 September 2021, 
van https://plotly.com/python-api-reference/generated/plotly.express.timeline.html
""")

st.write("""
***
""")

st.markdown(""" 
***Gemaakt door:***\n
Yasin Arslaner (500889084)\n
Coco de Brouwer (500832466)\n
Boris van Dam (500831201)\n
Inge Vijsma (500819598)\n
""")

st.write("""
***
""")


