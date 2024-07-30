import streamlit as st
import scr.estilo
import pandas as pd
import scr.gemini
import matplotlib.pyplot as plt

scr.estilo.menu_lateral()

st.title("Relatório em Casa")

# Lê os arquivos CSV
try:
    df_vendas = pd.read_csv("base/vendas.csv")
except FileNotFoundError:
    df_vendas = pd.DataFrame(columns=['id', 'produto', 'quantidade', 'valor_unitario', 'data_venda'])
try:
    df_estoque = pd.read_csv("base/estoque.csv")
except FileNotFoundError:
    df_estoque = pd.DataFrame(columns=['id', 'produto', 'quantidade', 'data_entrada'])

with st.expander("Banco de Dados"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## Vendas")
        st.dataframe(df_vendas)

    with col2:
        st.markdown("## Estoque")
        st.dataframe(df_estoque)

user_input = st.chat_input("Digite seu texto:")

if user_input:
    response = scr.gemini.call_google_gemini_api('LEMBRE-SE DE TODAS AS INSTRUÇÕES!! Faça modificações apenas para a página relatorio_em_casa.py'+user_input)
    st.chat_message("assistant").markdown(response)
