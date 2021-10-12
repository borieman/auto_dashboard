import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import folium
# import plotly.express as px
# import plotly.graph_objects as go


#st.set_page_config(layout="wide")

st.title('Elektrische auto dashboard')

st.write("""
***
""")

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



chargingDf = pd.DataFrame(rows,columns=columnNames)
# chargingDf.head()


#solution: merge a new dataframe that contains the correct geograhpal information on de 'postcode' column
postcodedf = pd.read_csv('postcode_dim.csv',sep=';',engine='python')

DF_charging = chargingDf.merge(postcodedf, left_on='Postcode',right_on='Postcode',suffixes=('_C','_P'))

columns = ['OperatorTitle','Postcode','latitude','longitude','distance','connectTypeTitle','connectTypeDiscont','isfastcharge','levelTitle','dateLSU','dateCreated','Gemeente','Provincie','Latitude','Longitude']
DF_charging = DF_charging[columns]



import folium
from folium.plugins import MarkerCluster
#Code voor het maken van een kleurloze map van Nederland 
m = folium.Map(location = HVAcords, zoom_start = 7.5, tiles = 'Cartodb Positron')

#Code voor het toevoegen van drie markers op drie verschillende locaties in Nederland
#DF_charging2 = pd.DataFrame(DF_charging)
filterProvince = DF_charging['Provincie'] == 'Overijssel'

for key,charger in DF_charging[filterProvince].iterrows():
    #print(charger)
    folium.Marker(location = [charger['latitude'], charger['longitude']], popup = charger['OperatorTitle']+'\n locatie: '+str(charger['latitude'])+' '+str(charger['longitude'])).add_to(m)
    
    
folium.LayerControl().add_to(m)    
    
#Laat de map zien
display(m)









# #Update de figuur om de dropdown buttons toe te voegen en laat de figuur zien
# fig.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

# st.plotly_chart(fig)

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


