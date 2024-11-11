
import streamlit as st

st.set_page_config(
    layout = "wide",
    page_title = "Projeto prático do curso de Streamlit da Asimov Academy"
)

df_data = st.session_state['dados']
    
clubes = df_data['Club'].unique()
clube = st.sidebar.selectbox("Escolha o clube", clubes)

df_filtrado = df_data[df_data['Club'] == clube]
jogadores = df_filtrado['Name'].unique()
jogador = st.sidebar.selectbox('Escolha o jogador', jogadores)

dados_jogador = df_data[df_data['Name'] == jogador].iloc[0]

st.image(dados_jogador['Photo'])
st.title(dados_jogador['Name'])
st.markdown(f"**Clube:** {dados_jogador['Club']}")
st.markdown(f"**Clube:** {dados_jogador['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {dados_jogador['Age']}")
col2.markdown(f"**Altura:** {dados_jogador['Height(cm.)']}")
col3.markdown(f"**Peso:** {dados_jogador['Weight(lbs.)'] * 0.453:.1f}")
st.divider()

st.subheader(f"**Overall** {dados_jogador['Overall']} ")
st.progress(int(dados_jogador['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Valor de mercado', value=f"R$ {dados_jogador['Value']:,}")
col2.metric(label='Remuneração semana', value=f"R$ {dados_jogador['Wage']:,}")
