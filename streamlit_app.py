import numpy as np
import pandas as pd 

import streamlit as st 
import pickle
import pandas as pd

from PIL import Image
from PIL import Image
import requests
from io import BytesIO

data = pd.read_csv('data.csv')

def Medicines_Recommendor(disease):
    
    plants = []
    parts = []
    scientificNames = []
    uses = []
    images = []
    
    for i in range(len(data['Disease'])):
        
        if data['Disease'][i].lower() == disease.lower():
            
            plant = data.iloc[i][0]
            scientificName = data.iloc[i][1]
            part = data.iloc[i][2]
            use = data.iloc[i][4]
            image = data.iloc[i][5]
            
            plants.append(plant)
            parts.append(part)
            scientificNames.append(scientificName)
            uses.append(use)
            images.append(image)

    return plants, scientificNames, parts, uses, images
        
        
st.title('Herbal Plants Recommended')

diseases = list(set(data['Disease']))
selected_disease_name = st.selectbox(
    'Search For disease .... ',
    diseases
)


def cards(Medicines):
    
    plants = Medicines[0]
    scientificNames = Medicines[1]
    parts = Medicines[2]
    uses = Medicines[3]
    images = Medicines[4]
    # Create a container for the row
    row_container = st.container()

    for plant in plants:
        i = plants.index(plant)
        # Inside the row container, create a column for each element
        with row_container:
            
            selected_medicine = ''
            with st.expander(f"{plant}", expanded=selected_medicine == plant):
                if images[i] == '0':
                    col1, col2 = st.columns([500,1])
                if images[i] != '0':
                    col1, col2 = st.columns([385,175])

                with col1:
                    st.write(
                    f"""
                    
                    <div class="card" style="width : 100%;">
                    <p style="display : inline-block; border-radius : 7px; padding : 20px; width : 100%;">
                        <u><b>Plant name</b></u>&nbsp :&nbsp {plant}<br>
                        <u><b>Scientific name</b></u>&nbsp :&nbsp {scientificNames[i]}<br>
                        <u><b>Part in Use</b></u>&nbsp :&nbsp {parts[i]}<br>
                        <u><b>Dosage</b></u>&nbsp :&nbsp {uses[i]}<br>
                    <p>
                    </div>
                    
                    """,
                    unsafe_allow_html=True
                    )

                with col2:
                    
                    if images[i] == '0':
                        st.write(f" ", unsafe_allow_html=True)
                    if images[i] != '0':
                        st.write(f'   ', unsafe_allow_html=True)
                        response = requests.get(images[i])
                        image = Image.open(BytesIO(response.content))
                        image = image.resize((600, 400))
                        st.image(image, width=200)
                
                
if st.button('Recommend'):
    Medicines = Medicines_Recommendor(selected_disease_name)
    cards(Medicines)
    
