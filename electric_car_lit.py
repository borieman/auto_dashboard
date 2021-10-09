import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
# import numpy as np
# import json
# import requests
# import plotly.express as px
# import plotly.graph_objects as go
# from PIL import Image

#st.set_page_config(layout="wide")

# image = Image.open('trein.jpg')

# st.image(image, width=700)

st.title('Elektrische auto dashboard')


# #Update de figuur om de dropdown buttons toe te voegen en laat de figuur zien
# fig.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

# st.plotly_chart(fig)

st.markdown(""" 
In bovenstaande figuur is een boxplot weergegeven met de impactwaardes van de calamiteiten per station. Met behulp van een 
dropbox kunnen de gegevens per station worden weergegeven. 
Als je met je muis over de boxplot beweegt wordt het minimum, maximum, mediaan, eerste en derde kwartiel gegeven.
Een aantal stations hebben enkel calamiteiten gehad van de impact waarde 4 waardoor de boxplot een lijn is geworden.
Alleen de stations met calamiteiten zullen worden weergegeven. 
""")

st.write("""
***
""")

st.markdown(""" 
**Bronnenlijst**\n
DataCamp. (z.d.). DataCamp. Geraadpleegd op 29 september 2021, 
van https://www.datacamp.com/users/sign_in?redirect=https%3A%2F%2Flearn.datacamp.com%2F
\n
plotly.express.box — 5.3.1 documentation. (z.d.). Plotly. Geraadpleegd op 29 september 2021, 
van https://plotly.github.io/plotly.py-docs/generated/plotly.express.box.html
\n
plotly.express.histogram — 5.3.1 documentation. (n.d.). Plotly. Geraadpleegd op 29 September 2021, 
van https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html
\n
plotly.express.scatter_geo — 5.3.1 documentation. (n.d.). Plotly. Geraadpleegd op 26 September 2021, 
van https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo
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


