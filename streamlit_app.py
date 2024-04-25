import numpy as np
import pandas as pd 

import streamlit as st 
import pickle
import pandas as pd

data = pd.read_csv('data.csv')

def Medicines_Recommendor(disease):
    
    plants = []
    parts = []
    uses = []
    
    for i in range(len(data['Disease'])):
        if data['Disease'][i].lower() == disease.lower():
            plant = data.iloc[i][0]
            part = data.iloc[i][1]
            use = data.iloc[i][3]
            plants.append(plant)
            parts.append(part)
            uses.append(use)

    return plants, parts, uses
        
st.title('Herbal Plants Recommended')

diseases = list(set(data['Disease']))
selected_disease_name = st.selectbox(
    'Search For disease .... ',
    diseases
)


def cards(Medicines):
    
    plants = Medicines[0]
    parts = Medicines[1]
    uses = Medicines[2]
    
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
                    <p style="border-radius : 7px; border : 2px solid #dedede; padding : 20px;">
                        <u><b>Plant name</b></u>  : {plant}.    <br>
                        <u><b>Part in Use</b></u> : {parts[i]}. <br>
                        <u><b>Dosage</b></u>      : {uses[i]}
                    <p>
                    </div>
                    
                    """,
                    unsafe_allow_html=True
                )


if st.button('Recommend'):
    Medicines = Medicines_Recommendor(selected_disease_name)
    cards(Medicines)
    
