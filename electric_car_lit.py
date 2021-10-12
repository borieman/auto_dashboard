import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
# import plotly.express as px
# import plotly.graph_objects as go


#st.set_page_config(layout="wide")

st.title('Elektrische auto dashboard')

st.write("""
***
""")

columnNames = ['OperatorTitle','Postcode','town','province','latitude','longitude','distance','connectTypeTitle','connectTypeDiscont','isfastcharge','levelTitle','dateLSU','dateCreated']
rows = []

with open('opencharge_10000.json') as json_file:
        data = json.load(json_file)
        for key,document in enumerate(data):
            print(key)
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
            #print('\n',postcode,town,province,latitude,longitude,distance,distanceUnit)
            
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
            print(OperatorTitle,postcode,town,province,latitude,longitude,distance,connectTypeTitle,connectTypeDiscont,isfastcharge,levelTitle,dateLSU,dateCreated)
            #print('\n',OperatorTitle,postcode,town,province,latitude,longitude,distance,connectTypeTitle,connectTypeDiscont,isfastcharge,levelTitle,dateLSU,dateCreated)
            rows.append([OperatorTitle,postcode,town,province,latitude,longitude,distance,connectTypeTitle,connectTypeDiscont,isfastcharge,levelTitle,dateLSU,dateCreated])


















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


