import streamlit as st
import os
from src.estilo import menu_lateral
menu_lateral()

st.title("Estrutura do Projeto")

def gerar_estrutura_diagrama(pasta_raiz):
    """Gera um diagrama da estrutura de pastas e arquivos."""
    estrutura = []
    for root, dirs, files in os.walk(pasta_raiz):
        if '.git' in root or 'pycache' in root: continue
        level = root.replace(pasta_raiz, '').count(os.sep)
        indent = '  ' * level
        estrutura.append(f"{indent}{os.path.basename(root)}/")
        for file in files:
            estrutura.append(f"{indent}  - {file}")
    return estrutura

# Obtém a estrutura do projeto
pasta_raiz = os.getcwd()
estrutura_diagrama = gerar_estrutura_diagrama(pasta_raiz)

# Exibe a estrutura
st.markdown("```\n" + "\n".join(estrutura_diagrama) + "\n```")
