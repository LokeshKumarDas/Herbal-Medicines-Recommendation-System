import numpy as np
import pandas as pd 

import streamlit as st 
import pickle
import pandas as pd

data = pd.read_csv('data.csv')

def Medicines_Recommendor(disease):
    
    plants = []
    parts = []
    scientificNames = []
    uses = []
    
    for i in range(len(data['Disease'])):
        
        if data['Disease'][i].lower() == disease.lower():
            
            plant = data.iloc[i][0]
            scientificName = data.iloc[i][1]
            part = data.iloc[i][2]
            use = data.iloc[i][4]
            
            plants.append(plant)
            parts.append(part)
            scientificNames.append(scientificName)
            uses.append(use)

    return plants, scientificNames, parts, uses
        
        
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
    
    # Create a container for the row
    row_container = st.container()

    for plant in plants:
        i = plants.index(plant)
        # Inside the row container, create a column for each element
        with row_container:
            
            selected_medicine = ''
            with st.expander(f"{plant}", expanded=selected_medicine == plant):
                
                st.write(
                    f"""
                    
                    <div class="card" style="width : 100%;">
                    <p style="border-radius : 7px; padding : 20px;">
                        <u><b>Plant name</b></u>  : {plant}                      <br>
                        <u><b>Scientific name</b></u>  : {scientificNames[i]}    <br>
                        <u><b>Part in Use</b></u> : {parts[i]}                   <br>
                        <u><b>Dosage</b></u>      : {uses[i]}
                    <p>
                    </div>
                    
                    """,
                    unsafe_allow_html=True
                )


if st.button('Recommend'):
    Medicines = Medicines_Recommendor(selected_disease_name)
    cards(Medicines)
    
