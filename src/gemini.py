import google.generativeai as genai
import src.ler_pastas
import src.modificar_arquivos
import streamlit as st
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=st.secrets['API_KEY'])

generation_config = { "temperature": 1, "top_p": 0.95, "top_k": 64, "max_output_tokens": 20000, "response_mime_type": "text/plain"}

model = genai.GenerativeModel( model_name="gemini-1.5-flash", generation_config=generation_config,safety_settings={HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH})

def call_google_gemini_api(text):
    instrucoes = open(r'src/instrucoes_gemini.txt', 'r', encoding='utf-8').read()
    codigo_atual=src.ler_pastas.read_folder_structure_and_files()
    chat_session = model.start_chat( history=[ { "role": "user", "parts": [instrucoes + codigo_atual]}]+st.session_state.messages)
    response = chat_session.send_message(text)
    response_text = response.text
    
    return src.modificar_arquivos.ler_resposta(response_text)