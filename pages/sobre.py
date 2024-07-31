import streamlit as st
import src.estilo

src.estilo.menu_lateral(pagina="Sobre o Chat Construtor")

st.title("Sobre o Chat Construtor")

with st.container():
    st.markdown(
        """
        O Chat Construtor é seu assistente de desenvolvimento Streamlit, 
        impulsionado pela inteligência artificial do Google Gemini. 
        Ele transforma suas ideias em código funcional, agilizando a criação e 
        o gerenciamento de suas aplicações.
        """,
    )

st.subheader("Como a mágica acontece?")

st.markdown(
    """
    1. **Você descreve:** Conte ao Chat Construtor o que você deseja criar.
    2. **Gemini entende:** O modelo de linguagem Gemini interpreta suas instruções.
    3. **Código é gerado:** Gemini transforma suas ideias em código Streamlit pronto para usar.
    4. **Você refina:** Revise e ajuste o código gerado para atender às suas necessidades.
    5. **Sua aplicação ganha vida:** Execute o código e veja sua visão se tornar realidade!
    """
)

with st.expander("Recursos que vão te surpreender:",expanded=True):
    st.markdown(
        """
        * **Criação de páginas, componentes e funcionalidades:** Do layout à lógica, o Chat Construtor te ajuda em cada etapa.
        * **Gerenciamento inteligente de arquivos:** Organize seu projeto com facilidade.
        * **Visualização de dados:** Gere gráficos e tabelas interativas para analisar seus dados.
        * **Upload e análise de arquivos:** Carregue seus próprios dados para explorar e transformar.
        """
    )

st.markdown("---")

st.subheader("Observações importantes:")

st.markdown(
    """
    * O Chat Construtor ainda está em desenvolvimento e aprendendo a cada dia.
    * Se encontrar algum erro ou tiver sugestões, compartilhe conosco para que possamos melhorar!
    * O Chat Construtor é uma ferramenta poderosa, mas não substitui o conhecimento em programação. Use-o como um aliado para impulsionar sua criatividade!
    """
)

st.markdown("**Essa página foi criada automaticamente pelo Chat Construtor!** 🎉")