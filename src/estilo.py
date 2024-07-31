import streamlit as st
from streamlit.errors import StreamlitAPIException
from PIL import Image
from pathlib import Path
import base64
import src.constantes

def importar_assets():
    def abrir_imagem(path):
        return Image.open(Path(path))
    def abrir_imagem_base64(path):
        return base64.b64encode(Path(path).read_bytes()).decode()

    assets={
        'logo_ico': abrir_imagem('assets/logo_icone_rgb.ico'),
        'logo_dark': abrir_imagem('assets/logo_dark.png'),
        'logo_light': abrir_imagem('assets/logo_light.png'),
        'logo_dark_base64':abrir_imagem_base64('assets/logo_dark.png')
    }
    return assets

def importar_estilos():
    with open(r"src/estilos.css", "r") as f:
        css = f.read()
    return css

def aplicar_estilos(*classes, texto="", imagem=None, link=None, link_pagina=None):
    css = importar_estilos()
    classes_str = " ".join(classes)
    if imagem != None:
        elemento = f"<img src=data:image/png;base64,{imagem}>"
    else:
        elemento = texto
    div = f"""<div class="{classes_str}">{elemento}</div>"""
    if link != None:
        div = f"<a href='{link}'>{div}</a>"
    elif link_pagina != None:
        div = f"<a href='{link_pagina}' target='_self'>{div}</a>"

    return f"""<style>{css}</style>{div}"""

def menu_lateral(pagina="Chat Construtor"):
    if pagina != "Chat Construtor" and "Bug Iniciar" not in st.session_state:
        st.session_state["Bug Iniciar"] = True
        st.rerun()
    assets = importar_assets()
    try:
        st.set_page_config(
            page_title="Chat Construtor", page_icon=assets["logo_ico"], layout="wide"
        )
    except StreamlitAPIException:
        pass
    with st.sidebar:
        st.markdown(
            aplicar_estilos(
                "imagens", link_pagina="", imagem=assets["logo_dark_base64"]
            ),
            unsafe_allow_html=True,
        )
        st.divider()
        st.subheader("MENU EM CONSTRUÇÃO")
        for pag, value in src.constantes.PAGINAS.items():
            try:st.page_link(pag, label=value[0], icon=value[1])
            except Exception: st.warning('Recarregue a página apertando R para visualizar as alterações. Ou clique em Rerun')