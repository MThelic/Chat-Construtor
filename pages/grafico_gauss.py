import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps  # Importa o módulo colormaps
from src.estilo import menu_lateral

menu_lateral()

st.title("Explorador de Gráficos Interativos")

st.markdown(
    """
    Explore diferentes tipos de gráficos e visualize como seus parâmetros influenciam seu 
    comportamento. Descubra padrões, tendências e relações nos dados de forma interativa!
    """
)

# Lista suspensa para escolher o tipo de gráfico
grafico_escolhido = st.selectbox(
    "Selecione o tipo de gráfico:",
    ("Funções Matemáticas", "Distribuição Normal", "Gráfico de Barras", "Dispersão 3D"),
)

# Parâmetros e plotagem do gráfico escolhido
if grafico_escolhido == "Funções Matemáticas":
    funcao = st.selectbox("Escolha a função:", ("seno", "cosseno", "tangente", "exponencial"))
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

    if funcao == "seno":
        y = np.sin(x)
    elif funcao == "cosseno":
        y = np.cos(x)
    elif funcao == "tangente":
        y = np.tan(x)
    else:  # exponencial
        y = np.exp(x)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, color="blue", linewidth=2)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("f(x)", fontsize=12)
    ax.set_title(f"Gráfico da função {funcao}(x)", fontsize=14)
    ax.grid(True, linestyle="--")

elif grafico_escolhido == "Distribuição Normal":
    media = st.slider("Média (μ)", -3.0, 3.0, 0.0, step=0.1)
    desvio_padrao = st.slider("Desvio Padrão (σ)", 0.1, 2.0, 1.0, step=0.1)
    x = np.linspace(media - 3 * desvio_padrao, media + 3 * desvio_padrao, 100)
    y = (1 / (desvio_padrao * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desvio_padrao) ** 2)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, color="purple", linewidth=2)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("Densidade de Probabilidade", fontsize=12)
    ax.set_title(f"Distribuição Normal (μ={media}, σ={desvio_padrao})", fontsize=14)
    ax.grid(True, linestyle="--")
    ax.fill_between(x, y, color="purple", alpha=0.3)  # Preenchimento sob a curva

elif grafico_escolhido == "Gráfico de Barras":
    categorias = ["Maçã", "Banana", "Laranja", "Uva", "Pera"]
    valores = np.random.randint(10, 50, len(categorias))

    fig, ax = plt.subplots(figsize=(10, 5))
    cores = colormaps.get_cmap("tab20c").colors  # Uso do colormaps
    ax.bar(categorias, valores, color=cores)
    ax.set_xlabel("Frutas", fontsize=12)
    ax.set_ylabel("Quantidade", fontsize=12)
    ax.set_title("Gráfico de Barras de Frutas", fontsize=14)
    for i, v in enumerate(valores):
        ax.text(i, v + 1, str(v), ha="center", va="bottom")  # Rótulos nas barras

elif grafico_escolhido == "Dispersão 3D":
    np.random.seed(0)
    n = 100
    x = np.random.rand(n)
    y = np.random.rand(n)
    z = np.random.rand(n)
    cores = colormaps.get_cmap("viridis")(z)  # Uso do colormaps

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c=cores, marker="o", s=50)
    ax.set_xlabel("X", fontsize=12)
    ax.set_ylabel("Y", fontsize=12)
    ax.set_zlabel("Z", fontsize=12)
    ax.set_title("Gráfico de Dispersão 3D", fontsize=14)

# Exibe o gráfico
st.pyplot(fig)