import os
import shutil
import src.constantes

def add_pagina(configuracao):
    """Adiciona uma nova página à lista de páginas."""
    try:
        pag = src.constantes.PAGINAS
        pag[configuracao[0]] = [configuracao[1], configuracao[2]]
        with open(r"src/constantes.py", "w", encoding='utf-8') as f:
            f.write("PAGINAS=" + str(pag))
    except IndexError:
        return "Erro: Formato de configuração de página inválido."

def remover_pagina(value):
    """Remove uma página da lista de páginas."""
    pag = src.constantes.PAGINAS
    if value in pag:
        pag.pop(value)
        with open(r"src/constantes.py", "w", encoding='utf-8') as f:
            f.write("PAGINAS=" + str(pag))
    else:
        return f"Erro: Página '{value}' não encontrada."

def executar_chat(value):
    """Retorna a resposta do chat."""
    return f'Resposta: {value}'

def executar_criar_pasta(value):
    """Cria uma nova pasta."""
    value = value.strip()
    try:
        os.makedirs(value, exist_ok=True)
        return f'Pasta {value} criada'
    except Exception as e:
        return f"Erro ao criar a pasta '{value}': {e}"

def executar_deletar(value):
    """Deleta um arquivo ou pasta."""
    value = value.strip()
    caminho = os.path.abspath(value)
    try:
        if os.path.isfile(caminho):
            os.remove(caminho)
            if 'pages' in value:
                remover_pagina(value)
            return f'Página {value} excluída'
        elif os.path.isdir(caminho):
            shutil.rmtree(caminho)
            return f'Pasta {value} excluída'
        else:
            return f'O caminho {value} não existe.'
    except Exception as e:
        return f"Erro ao deletar '{value}': {e}"

def executar_criar_pagina(key, value):
    """Cria uma nova página no projeto."""
    try:
        configuracao = key.split(',')
        add_pagina(configuracao)
        with open(f"{configuracao[0]}", "w", encoding='utf-8') as f:
            f.write(value)
        return f'Página {configuracao[2]} {configuracao[1]}'
    except Exception as e:
        return f"Erro ao criar a página '{configuracao[0]}': {e}"

def executar_modificar_arquivo(key, value):
    """Modifica um arquivo existente."""
    try:
        with open(f"{key}", "w", encoding='utf-8') as f:
            f.write(value)
        return f'Arquivo {key} modificado'
    except Exception as e:
        return f"Erro ao modificar o arquivo '{key}': {e}"

def executar_comando(key, value):
    """Executa um comando com base na chave e no valor fornecidos."""
    if key == 'chat':
        return executar_chat(value)
    elif key == 'criar':
        return executar_criar_pasta(value)
    elif key == 'deletar':
        return executar_deletar(value)
    elif ',' in key:
        return executar_criar_pagina(key, value)
    else:
        return executar_modificar_arquivo(key, value)

def ler_resposta(response_text):
    """Lê e processa a resposta do modelo de linguagem."""
    mensagens = []
    lista = response_text.split('$')
    dicionario = {item: lista[i + 1].strip('|') for i, item in enumerate(lista) if item and item[0] != '|'}
    for key in dicionario:
        mensagens.append(executar_comando(key, dicionario[key]))
    return "\n".join(mensagens)