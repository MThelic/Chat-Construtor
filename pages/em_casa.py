import streamlit as st
import json
import os
import pandas as pd
import random
import string
from src.estilo import menu_lateral
menu_lateral()

def gerar_chave_aleatoria(tamanho=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

st.title("Em Casa")

opcao = st.radio("Selecione uma opção:", ("Vendas", "Estoque"), horizontal=True)

if opcao == "Vendas":
    st.markdown("## Cadastro de Vendas")

    # Gera uma chave aleatória
    chave_aleatoria = gerar_chave_aleatoria()

    # Exibe a chave aleatória
    st.text(f"ID da Venda: {chave_aleatoria}")

    # Lista de itens
    itens = [
        "Berinjela",
        "Mini Pizza",
        "Torta",
        "Esfiha",
        "Pastas Árabes"
    ]

    # Cria a lista suspensa com os itens
    produto = st.selectbox("Produto", itens)

    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    valor_unitario = st.number_input("Valor Unitário", min_value=0.01, step=0.01)
    data_venda = st.date_input("Data da Venda")

    # Botão para salvar venda
    if st.button("Salvar Venda"):
        st.success("Venda salva com sucesso!")

        # Cria o DataFrame com os dados da venda
        data = {'id': [chave_aleatoria], 'produto': [produto], 'quantidade': [quantidade], 'valor_unitario': [valor_unitario], 'data_venda': [data_venda.strftime('%Y-%m-%d')]}
        df = pd.DataFrame(data)

        # Salva o DataFrame em um arquivo CSV
        df.to_csv('base/bd_em_casa/vendas.csv', mode='a', index=False, header=True)

elif opcao == "Estoque":
    st.markdown("## Cadastro de Estoque")

    # Gera uma chave aleatória para o ID do estoque
    chave_estoque = gerar_chave_aleatoria()

    # Exibe a chave aleatória
    st.text(f"ID do Estoque: {chave_estoque}")

    # Lista de itens
    itens = [
        "Berinjela",
        "Mini Pizza",
        "Torta",
        "Esfiha",
        "Pastas Árabes"
    ]

    # Cria a lista suspensa com os itens
    produto_estoque = st.selectbox("Produto", itens)

    quantidade_estoque = st.number_input("Quantidade", min_value=0, step=1)
    data_entrada = st.date_input("Data de Entrada")

    # Botão para salvar estoque
    if st.button("Salvar Estoque"):
        st.success("Estoque salvo com sucesso!")

        # Cria o DataFrame com os dados do estoque
        data = {'id': [chave_estoque], 'produto': [produto_estoque], 'quantidade': [quantidade_estoque], 'data_entrada': [data_entrada.strftime('%Y-%m-%d')]}
        df = pd.DataFrame(data)

        # Salva o DataFrame em um arquivo CSV
        df.to_csv('base/bd_em_casa/estoque.csv', mode='a', index=False, header=True)