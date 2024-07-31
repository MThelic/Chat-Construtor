import streamlit as st
import os
import pandas as pd
from src.gemini import call_google_gemini_api
from src.estilo import menu_lateral

# Aplicando estilo da página (menu lateral)
menu_lateral()

st.title("Insights")

# Caminho da pasta para salvar os arquivos
insights_path = "base/insights"
os.makedirs(insights_path, exist_ok=True)  # Cria a pasta se não existir

# Função para obter os nomes dos arquivos na pasta Insights
def get_insight_files():
    return [f for f in os.listdir(insights_path) if f.endswith((".csv", ".xlsx", ".txt"))]

# Configuração do uploader de arquivos
uploaded_files = st.file_uploader(
    "Faça upload dos seus arquivos (CSV, XLSX, TXT)",
    type=["csv", "xlsx", "txt"],
    accept_multiple_files=True,
)

# Processamento dos arquivos enviados
if uploaded_files:
    for file in uploaded_files:
        filename = file.name
        file_path = os.path.join(insights_path, filename)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        st.success(f"Arquivo '{filename}' salvo com sucesso!")

# Dropdown para selecionar arquivos existentes e botão para remover
cols = st.columns([3, 1])
with cols[0]:
    selected_file = st.selectbox("Selecione um arquivo existente:", get_insight_files())
if selected_file:
    with cols[1]:
        st.text(' ')
        if st.button("Remover Arquivo ❌", key=selected_file):
            file_path = os.path.join(insights_path, selected_file)
            os.remove(file_path)
            st.success("Arquivo removido com sucesso!")

# Botão para obter insights
if st.button("Obter Insights"):
    if selected_file:
        file_path = os.path.join(insights_path, selected_file)
        try:
            if selected_file.endswith((".csv", ".xlsx")):
                df = pd.read_csv(file_path) if selected_file.endswith(".csv") else pd.read_excel(file_path)
                insight_data = f"**{selected_file}:**\n{df.head().to_markdown(index=False, numalign='left', stralign='left')}"
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                insight_data = f"**{selected_file}:**\n{content}"

            prompt = f"Obtenha insights sobre esses dados:\n\n{insight_data}"
            with st.spinner("Gerando insights..."):
                response = call_google_gemini_api(prompt)
                st.write(response)
        except Exception as e:
            st.error(f"Erro ao ler o arquivo '{selected_file}': {e}")
    else:
        st.warning("Selecione um arquivo ou faça upload de um novo para obter insights.")