import os
import shutil
import scr.constantes

menu_lateral="import scr.estilo\nscr.estilo.menu_lateral()\n"

def add_pagina(configuracao):
    pag=scr.constantes.PAGINAS
    pag[configuracao[0]]=[configuracao[1],configuracao[2]]
    open(r"scr/constantes.py", "w", encoding='utf-8').write("PAGINAS="+str(pag))

def remover_pagina(value):
    pag=scr.constantes.PAGINAS
    pag.pop(value)
    open(r"scr/constantes.py", "w", encoding='utf-8').write("PAGINAS="+str(pag))

def executar_comando(key,value):
    if key=='chat':
        return f'Resposta: {value}'
    elif key=='criar':
        value=value.strip()
        os.makedirs(value, exist_ok=True)
        return f'Pasta {value} criada'
    elif key=='deletar':
        value=value.strip()
        caminho=os.path.abspath(value)
        if os.path.isfile(caminho):
            os.remove(caminho)
            if 'pages' in value: remover_pagina(value)
        elif os.path.isdir(caminho): shutil.rmtree(caminho)
        else: return f'O caminho {value} não existe.'
        return f'Pasta {value} excluída'
    elif ',' in key:
        configuracao=key.split(',')
        add_pagina(configuracao)
        conteudo=menu_lateral+value if not('scr.estilo.menu_lateral(' in value) else value
        open(f"{configuracao[0]}", "w", encoding='utf-8').write(conteudo)
        return f'Página {configuracao[2]} {configuracao[1]}'
    else:
        open(f"{key}", "w", encoding='utf-8').write(value)
        return f'Arquivo {key} criado'

def ler_resposta(response_text):
    mensagens=[]
    lista=response_text.split('$')
    dicionario = {item: lista[i + 1].strip('|') for i, item in enumerate(lista) if item and item[0] != '|'}
    for key in dicionario:
        mensagens.append(executar_comando(key,dicionario[key]))
    return "\n".join(mensagens)
