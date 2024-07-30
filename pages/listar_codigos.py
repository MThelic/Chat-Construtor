import streamlit as st
import os
import scr.estilo
scr.estilo.menu_lateral()

st.title("Lista de Códigos")
st.markdown("## Selecione um arquivo .py para visualizar seu conteúdo:")

arquivos = {}
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            arquivos[file] = os.path.join(root, file)

arquivo_selecionado = st.selectbox("Selecione um arquivo:", list(arquivos.keys()))

if arquivo_selecionado:
    with open(arquivos[arquivo_selecionado], "r", encoding='utf-8') as f:
        codigo = f.read()
    st.code(codigo, language="python")