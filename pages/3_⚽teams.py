
import streamlit as st


st.set_page_config(
    layout = "wide",
    page_title = "Helloooo"
)

df_data = st.session_state['dados']
    
clubes = df_data['Club'].unique()
clube = st.sidebar.selectbox("Escolha o clube", clubes)

df_filtrado = df_data[df_data['Club'] == clube]

st.image(df_filtrado['Club Logo'].iloc[0])
st.markdown(f"## {df_filtrado['Club'].iloc[0]}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value', 'Wage', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause']

st.dataframe(df_filtrado[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtrado["Wage"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })