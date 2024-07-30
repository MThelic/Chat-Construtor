import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scr.estilo

scr.estilo.menu_lateral(pagina="Gráfico Interativo")

st.title("Gráfico Interativo")

st.markdown("""
    Explore diferentes tipos de funções e visualize como seus parâmetros influenciam seu comportamento.
""")

# Lista suspensa para escolher o tipo de função
funcao_escolhida = st.selectbox("Selecione o tipo de função:",
    ("Linear", "Quadrática", "3º Grau", "Senoide", "Circular"))

# Parâmetros da função escolhida
if funcao_escolhida == "Linear":
    a = st.slider("Coeficiente Angular (a)", -5.0, 5.0, 0.0, step=0.1)
    b = st.slider("Coeficiente Linear (b)", -5.0, 5.0, 0.0, step=0.1)
    x = np.linspace(-5, 5, 100)
    y = a * x + b
elif funcao_escolhida == "Quadrática":
    a = st.slider("Coeficiente Quadrático (a)", -5.0, 5.0, 1.0, step=0.1)
    b = st.slider("Coeficiente Linear (b)", -5.0, 5.0, 0.0, step=0.1)
    c = st.slider("Termo Constante (c)", -5.0, 5.0, 0.0, step=0.1)
    x = np.linspace(-5, 5, 100)
    y = a * x**2 + b * x + c
elif funcao_escolhida == "3º Grau":
    a = st.slider("Coeficiente Cúbico (a)", -5.0, 5.0, 1.0, step=0.1)
    b = st.slider("Coeficiente Quadrático (b)", -5.0, 5.0, 0.0, step=0.1)
    c = st.slider("Coeficiente Linear (c)", -5.0, 5.0, 0.0, step=0.1)
    d = st.slider("Termo Constante (d)", -5.0, 5.0, 0.0, step=0.1)
    x = np.linspace(-5, 5, 100)
    y = a * x**3 + b * x**2 + c * x + d
elif funcao_escolhida == "Senoide":
    amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, step=0.1)
    frequencia = st.slider("Frequência", 0.1, 5.0, 1.0, step=0.1)
    fase = st.slider("Fase", -np.pi, np.pi, 0.0, step=0.1)
    x = np.linspace(0, 2 * np.pi, 100)
    y = amplitude * np.sin(frequencia * x + fase)
elif funcao_escolhida == "Circular":
    raio = st.slider("Raio", 0.1, 5.0, 1.0, step=0.1)
    x = raio * np.cos(np.linspace(0, 2 * np.pi, 100))
    y = raio * np.sin(np.linspace(0, 2 * np.pi, 100))

# Plotagem do gráfico
fig, ax = plt.subplots(figsize=(6, 4)) # Reduz o tamanho do gráfico
ax.plot(x, y, "r-", linewidth=2)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title(f"Gráfico de {funcao_escolhida}")
ax.grid(True)

# Exibe o gráfico

st.columns([1,4,1])[1].pyplot(fig)

st.markdown("### :tada[Personalize os parâmetros da função usando os sliders! 🎉]")
