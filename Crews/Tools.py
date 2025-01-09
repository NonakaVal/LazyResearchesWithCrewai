
############################################################################################################
# Função para selecionar o diretório de saída
############################################################################################################
import os
from builtins import print, open
def select_output_directory(context_topic):
    # Usando o contexto como nome da pasta, substituindo espaços por underscores para tornar o nome válido
    folder_name = context_topic.replace(" ", "_")
    output_dir = os.path.join("folder_name")  # Diretório será dentro da pasta 'output'
    
    # Se o diretório não existir, cria o diretório
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    return output_dir

############################################################################################################

def combine_markdown_files_with_folders(separated_folder, combined_folder, combined_filename):
    """
    Combines all .md files in the separated folder into a single markdown file
    in the combined folder.
    """
    # Garantir que a pasta de saída combinada exista
    if not os.path.exists(combined_folder):
        os.makedirs(combined_folder)

    combined_filepath = os.path.join(combined_folder, combined_filename)

    # Listar todos os arquivos .md na pasta separada
    md_files = [f for f in os.listdir(separated_folder) if f.endswith(".md")]

    # Garantir que estão ordenados
    md_files.sort()

    # Criar o arquivo combinado
    with open(combined_filepath, "w", encoding="utf-8") as combined_file:
        for md_file in md_files:
            file_path = os.path.join(separated_folder, md_file)
            # Adicionar um cabeçalho para cada arquivo no combinado (opcional)
            combined_file.write(f"\n\n# {md_file}\n\n")
            # Escrever o conteúdo do arquivo no combinado
            with open(file_path, "r", encoding="utf-8") as f:
                combined_file.write(f.read())
                combined_file.write("\n\n")  # Adicionar espaçamento entre arquivos

    print(f"Combined file created at: {combined_filepath}")
