
import streamlit as st
import pandas as pd
import webbrowser
from pathlib import Path
from datetime import datetime

st.set_page_config(
    layout = "wide",
    page_title = "Projeto prático do curso de Streamlit da Asimov Academy"
)

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")

st.sidebar.markdown("Desnvolvido por [Intellectus Consulting](https://intellectusconsulting.com.br/)")

btn = st.button("Acesse os dados no Kaggle") # Estados de um botão: True or False

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    '''
    The Football Player Dataset from 2017 to 2023 provides comprehensive information about 
    professional football players. The dataset contains a wide range of attributes, 
    including player demographics, physical characteristics, playing statistics, 
    contract details, and club affiliations. 
    
    With over 17,000 records, this dataset offers 
    a valuable resource for football analysts, researchers, and enthusiasts interested in 
    exploring various aspects of the footballing world, as it allows for studying player 
    attributes, performance metrics, market valuation, club analysis, player positioning, 
    and player development over time.
    ''')

if "dados" not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col = 0, encoding='ISO-8859-1')
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value'] > 0]
    st.session_state["dados"] = df_data
