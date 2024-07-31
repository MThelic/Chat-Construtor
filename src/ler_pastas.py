import os

def read_folder_structure_and_files():
    folder_path = os.getcwd()
    print(folder_path)
    folder_structure = []
    python_files = []

    # Coletando a estrutura das pastas e arquivos Python (ignorando .git e __pycache__)
    for root, dirs, files in os.walk(folder_path):
        # Exclude '.git' and '__pycache__' directories
        excluded_dirs = ['.git', '__pycache__']
        for dir_name in excluded_dirs:
            if dir_name in dirs:
                dirs.remove(dir_name)

        level = root.replace(folder_path, '').count(os.sep)
        indent = ' ' * 4 * level
        folder_structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            folder_structure.append(f"{subindent}{file}")
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                python_files.append(file_path)

    # Construindo o conteúdo a ser retornado
    output_content = "Estrutura da Pasta:\n"
    output_content += "\n".join(folder_structure)
    output_content += "\n\n"

    for file_path in python_files:
        with open(file_path, 'r', encoding='utf-8') as py_file:
            file_content = py_file.read()
            output_content += "\n\n"
            output_content += f"Nome do Arquivo:{os.path.basename(file_path)}\n"
            output_content += f"Código:{file_content}\n\n"
    open(r'src/estrutura_pasta.txt', 'w', encoding='utf-8').write(output_content)

    return output_content