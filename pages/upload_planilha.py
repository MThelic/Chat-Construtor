import streamlit as st
import pandas as pd
from src.estilo import menu_lateral

menu_lateral()

st.title("Análise de Planilha")

uploaded_file = st.file_uploader("Escolha uma planilha", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Formato de arquivo inválido. Por favor, escolha um arquivo CSV ou XLSX.")

        num_colunas = len(df.columns)
        st.write(f"Número de colunas: {num_colunas}")

        st.write("Tipos de coluna:")
        for col in df.columns:
            tipo_coluna = str(df[col].dtype)
            st.write(f"- {col}: {tipo_coluna}")

    except Exception as e:
        st.error(f"Erro ao processar a planilha: {e}")