from builtins import input, print, open 
import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from crewai import Crew, Process

# Importando agentes e tarefas de diferentes equipes
from Crews.MainSearchCrew.Agents import Search_Agents
from Crews.MainSearchCrew.Tasks import Search_tasks
from Crews.StudyPlanCrew.Agents import create_study_project_agents
from Crews.StudyPlanCrew.Tasks import create_study_project_roadmap_tasks
from Crews.GameNewsCrew.Agents import create_game_news_agents
from Crews.GameNewsCrew.Tasks import create_game_news_scraping_tasks
from Crews.ProductContentCrew.Agents import create_product_content_agents_with_emotion
from Crews.ProductContentCrew.Tasks import create_product_content_tasks_with_emotion

# Carregar variáveis de ambiente
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Inicializar o modelo de linguagem
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=1500
)

############################################################################################################
# Função para selecionar o diretório de saída
############################################################################################################
def select_output_directory(base_folder, context_topic):
    """
    Select the output directory based on the context_topic.
    Separates files into 'separated' and 'full' subdirectories under the given base folder.
    """
    # Usando o contexto como nome da pasta, substituindo espaços por underscores
    folder_name = context_topic.replace(" ", "_")
    output_dir = os.path.join(base_folder, folder_name)

    # Criando subdiretórios "separated" e "full"
    separated_folder = os.path.join(output_dir, "separated")
    combined_folder = os.path.join(output_dir, "full")

    # Criar as pastas, se não existirem
    os.makedirs(separated_folder, exist_ok=True)
    os.makedirs(combined_folder, exist_ok=True)

    return separated_folder, combined_folder


############################################################################################################
# Função para combinar arquivos Markdown em uma pasta separada
############################################################################################################
def combine_markdown_files_with_folders(separated_folder, combined_folder, combined_filename):
    """
    Combines all .md files in the separated folder into a single markdown file
    in the combined folder.
    """
    # Caminho completo para o arquivo combinado
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


############################################################################################################
# Função para selecionar a equipe
############################################################################################################
def select_crew():
    print("Select the crew you want to use:")
    print("1. Search Crew")
    print("2. Study Plan Crew")
    print("3. Game News Crew")
    print("4. Product Content Crew with Emotion Analysis")
    crew_choice = input("Enter 1, 2, 3, or 4: ")
    
    if crew_choice == "1":
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        separated_folder, combined_folder = select_output_directory("answers-output", context_topic)
        tasks = Search_tasks(question, context_topic, separated_folder, agents)
        return agents, tasks, separated_folder, combined_folder, context_topic
    elif crew_choice == "2":
        context_topic = input("Enter the research context for Study Plan Crew: \n")
        question = input("Enter the research question for Study Plan Crew: \n")
        agents = create_study_project_agents(context_topic, question, llm)
        separated_folder, combined_folder = select_output_directory("answers-output", context_topic)
        tasks = create_study_project_roadmap_tasks(context_topic, separated_folder, agents)
        return agents, tasks, separated_folder, combined_folder, context_topic
    elif crew_choice == "3":
        context_topic = input("Enter the gaming topic or genre for Game News Crew: \n")
        news_category = input("Enter the news category (e.g., reviews, updates, launches): \n")
        agents = create_game_news_agents(llm)
        separated_folder, combined_folder = select_output_directory("answers-output", context_topic)
        tasks = create_game_news_scraping_tasks(context_topic, news_category, separated_folder, agents)
        return agents, tasks, separated_folder, combined_folder, context_topic
    elif crew_choice == "4":
        product_name = input("Enter the name of the product for Product Content Crew: \n")
        agents = create_product_content_agents_with_emotion(llm)
        separated_folder, combined_folder = select_output_directory("answers-output", product_name)
        tasks = create_product_content_tasks_with_emotion(product_name, separated_folder, agents)
        return agents, tasks, separated_folder, combined_folder, product_name
    else:
        print("Invalid choice, defaulting to Search Crew.")
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        separated_folder, combined_folder = select_output_directory("answers-output", context_topic)
        tasks = Search_tasks(question, context_topic, separated_folder, agents)
        return agents, tasks, separated_folder, combined_folder, context_topic


############################################################################################################
# Selecionando a equipe e inicializando as tarefas
############################################################################################################
agents, tasks, separated_folder, combined_folder, context_topic = select_crew()

# Configurando a equipe (Crew)
crew = Crew(
    # Lista de agentes na equipe
    agents=agents,

    # Lista de tarefas a serem executadas pela equipe
    tasks=tasks,

    process=Process.sequential,  # Processo sequencial para execução das tarefas
    manager_llm=llm,  # Definindo o LLM para gerenciar a equipe
    verbose=True
)

# Iniciando o processo
result = crew.kickoff()
print(result)

# Nome do arquivo combinado baseado no contexto
combined_filename = f"{context_topic.replace(' ', '_')}-complete.md"

# Combinando arquivos Markdown gerados na pasta separada
combine_markdown_files_with_folders(separated_folder, combined_folder, combined_filename)

print(f"All .md files have been combined into a single file: {combined_filename}")
