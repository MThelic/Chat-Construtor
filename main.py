import streamlit as st
import scr.gemini
import scr.estilo

scr.estilo.menu_lateral()
st.markdown('## CHAT CONSTRUTOR')

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Digite seu texto:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = scr.gemini.call_google_gemini_api('LEMBRE-SE DE TODAS AS INSTRUÇÕES!! '+user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

if not user_input and not st.session_state.messages:
    st.chat_message("assistant").markdown("Insira alguma instrução ou pergunte por sugestões")
