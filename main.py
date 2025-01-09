from builtins import input, print
import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from crewai import Crew, Process


# Importando agentes e tarefas de diferentes equipes
from Crews.Tools import select_output_directory
from Crews.MainSearchCrew.Agents import Search_Agents
from Crews.MainSearchCrew.Tasks import Search_tasks
from Crews.StudyPlanCrew.Agents import create_study_project_agents
from Crews.StudyPlanCrew.Tasks import create_study_project_roadmap_tasks
from Crews.GameNewsCrew.Agents import create_game_news_agents
from Crews.GameNewsCrew.Tasks import create_game_news_scraping_tasks

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
# Função para selecionar a equipe
############################################################################################################
def select_crew():
    print("Select the crew you want to use:")
    print("1. Search Crew")
    print("2. Study Plan Crew")
    print("3. Game News Crew")
    crew_choice = input("Enter 1, 2, or 3: ")
    
    if crew_choice == "1":
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        tasks = Search_tasks(question, context_topic, select_output_directory(context_topic), agents)
        return agents, tasks, context_topic, question
    elif crew_choice == "2":
        context_topic = input("Enter the research context for Study Plan Crew: \n")
        question = input("Enter the research question for Study Plan Crew: \n")
        agents = create_study_project_agents(context_topic, question, llm)
        tasks = create_study_project_roadmap_tasks(context_topic, select_output_directory(context_topic), agents)
        return agents, tasks, context_topic, question
    elif crew_choice == "3":
        context_topic = input("Enter the gaming topic or genre for Game News Crew: \n")
        news_category = input("Enter the news category (e.g., reviews, updates, launches): \n")
        agents = create_game_news_agents(llm)
        tasks = create_game_news_scraping_tasks(context_topic, news_category, select_output_directory(context_topic), agents)
        return agents, tasks, context_topic, None
    else:
        print("Invalid choice, defaulting to Search Crew.")
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        tasks = Search_tasks(question, context_topic, select_output_directory(context_topic), agents)
        return agents, tasks, context_topic, question



############################################################################################################
# Selecionando a equipe e inicializando as tarefas
############################################################################################################
agents, tasks, context_topic, question = select_crew()

# Verificando o valor de question e exibindo uma mensagem apropriada
if question is not None:
    print(f"Research question: {question}")
else:
    print("No specific question was set for this crew.")

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
