from builtins import input, print
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from crewai import Crew, Process
import os

# Importing the relevant agents and tasks
from Crews.SearchCrew.Agents import Search_Agents
from Crews.SearchCrew.Tasks import Search_tasks
from Crews.StudyPlanCrew.Agents import create_study_project_agents
from Crews.StudyPlanCrew.Tasks import create_study_project_roadmap_tasks

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=1500
)

############################################################################################################
# Function to select the output directory
############################################################################################################
def select_output_directory():
    output_dir = input("Choose the name of the directory to be created to save your summaries. \n")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


############################################################################################################
# Function to select the crew
############################################################################################################
def select_crew():
    print("Select the crew you want to use:")
    print("1. Search Crew")
    print("2. Study Plan Crew")
    crew_choice = input("Enter 1 or 2: ")
    
    if crew_choice == "1":
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        tasks = Search_tasks(question, context_topic, select_output_directory(), agents)
    elif crew_choice == "2":
        context_topic = input("Enter the research context for Study Plan Crew: \n")
        question = input("Enter the research question for Study Plan Crew: \n")  # Adding question input here
        agents = create_study_project_agents(context_topic, question, llm)
        tasks = create_study_project_roadmap_tasks(context_topic, select_output_directory(), agents)
    else:
        print("Invalid choice, defaulting to Search Crew.")
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        tasks = Search_tasks(question, context_topic, select_output_directory(), agents)

    return agents, tasks, context_topic, question


############################################################################################################
# Selecting the crew and initializing tasks
############################################################################################################
agents, tasks, context_topic, question = select_crew()

# Setting up the crew (Crew)
crew = Crew(
    # List of agents in the crew
    agents=agents,

    # List of tasks to be performed by the crew
    tasks=tasks,

    process=Process.sequential,  # Sequential process for task execution
    manager_llm=llm,  # Setting the LLM to manage the crew
    verbose=True
)

# Starting the process
result = crew.kickoff()
print(result)
