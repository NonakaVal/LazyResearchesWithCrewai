
############################################################################################################
# Função para selecionar o diretório de saída
############################################################################################################
import os
def select_output_directory(context_topic):
    # Usando o contexto como nome da pasta, substituindo espaços por underscores para tornar o nome válido
    folder_name = context_topic.replace(" ", "_")
    output_dir = os.path.join("answers-output", folder_name)  # Diretório será dentro da pasta 'output'
    
    # Se o diretório não existir, cria o diretório
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    return output_dir
