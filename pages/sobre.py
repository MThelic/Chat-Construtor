import streamlit as st
import scr.estilo

scr.estilo.menu_lateral(pagina="Sobre o Chat Construtor")

st.title("Sobre o Chat Construtor")

st.markdown("""
    O Chat Construtor é uma ferramenta poderosa para desenvolvedores de aplicações Streamlit. 
    Ele permite que você crie, modifique e gerencie seu projeto de forma rápida e eficiente, 
    usando a inteligência artificial para gerar código automaticamente.

    ## Como funciona?

    O Chat Construtor usa o modelo de linguagem **Gemini** para entender suas instruções e gerar o código Streamlit desejado. 
    Basta digitar seus requisitos e o Chat Construtor fará o resto! 

    ## Recursos:

    * **Geração de Código Automática:** Crie páginas, componentes e funcionalidades com facilidade.
    * **Integração com o Gemini:** Acesse a inteligência artificial avançada do Gemini para obter resultados precisos.
    * **Gerenciamento de Arquivos:** Organize seu projeto com a função de gerenciamento de arquivos.

    ## Começando:

    1. **Digite suas instruções:** Explique o que você deseja que o Chat Construtor faça.
    2. **Revise o código gerado:** Verifique se o código atende às suas necessidades.
    3. **Execute o código:** Execute o código gerado em seu ambiente Streamlit.

    ## Observações:

    * O Chat Construtor ainda está em desenvolvimento. 
    * Se você encontrar algum erro, por favor, relate-o para que possamos melhorá-lo.
    * O Chat Construtor é uma ferramenta poderosa, mas não substitui o conhecimento de programação.

    ## Explore e experimente!
""")

st.markdown(f"### :rainbow[Essa página foi criada automaticamente pelo Chat Construtor! 🎉]")