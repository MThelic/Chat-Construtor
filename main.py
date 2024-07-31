import streamlit as st
import src.gemini
import src.estilo

def main():
    """Função principal para executar o chatbot."""
    src.estilo.menu_lateral()
    st.markdown('## CHAT CONSTRUTOR')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Digite seu texto:")

    if user_input:
        try:
            st.session_state.messages.append({"role": "user", "parts": user_input})
            prompt = "LEMBRE-SE DE TODAS AS INSTRUÇÕES!! " + user_input
            response = src.gemini.call_google_gemini_api(prompt)
            st.session_state.messages.append({"role": "model", "parts": response})
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao processar a resposta: {e}")

    for message in st.session_state.messages:
        with st.chat_message(message["role"] if message["role"]=='user' else 'ai'):
            st.markdown(message["parts"])

    if not user_input and not st.session_state.messages:
        try:
            sugestao = src.gemini.call_google_gemini_api('Gere uma sugestão de prompt para o chat do Streamlit.')
            sugestao = sugestao.strip('Resposta: ').strip()  # Remove "Resposta:" e espaços extras
            st.chat_message("ai").markdown(f"Experimente: *{sugestao}*")
        except Exception as e:
            st.error(f"Erro ao gerar sugestão: {e}")

if __name__ == "__main__":
    main()