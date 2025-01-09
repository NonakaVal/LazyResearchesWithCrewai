
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

############################################################################################################

def combine_markdown_files(output_directory, combined_filename="combined_output.md"):
    """
    Combines all .md files in the specified directory into a single markdown file.

    Args:
        output_directory (str): The directory containing the .md files.
        combined_filename (str): The name of the output combined markdown file.
    """
    combined_filepath = os.path.join(output_directory, combined_filename)

    # Check if the output directory exists
    if not os.path.exists(output_directory):
        print(f"The directory {output_directory} does not exist.")
        return

    # List all .md files in the directory
    md_files = [f for f in os.listdir(output_directory) if f.endswith(".md")]

    # Sort files alphabetically to ensure proper order
    md_files.sort()

    # Open the combined output file for writing
    with open(combined_filepath, "w", encoding="utf-8") as combined_file:
        for md_file in md_files:
            file_path = os.path.join(output_directory, md_file)
            
            # Add a header for each file (optional)
            combined_file.write(f"\n\n# {md_file}\n\n")
            
            # Read and write the content of each .md file
            with open(file_path, "r", encoding="utf-8") as f:
                combined_file.write(f.read())
                combined_file.write("\n\n")  # Add spacing between files

    print(f"Combined file created at: {combined_filepath}")
