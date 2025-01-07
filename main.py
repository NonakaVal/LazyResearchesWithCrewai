from builtins import input, print
from Crews.SearchCrew.Agents import Search_crew
from Crews.SearchCrew.Tasks import create_tasks
from crewai import Crew, Process

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


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

output_directory = select_output_directory()
context_topic = input("Enter the research context: \n")
question = input("Enter the research question: \n")





############################################################################################################
########################                    App Setup                    ######################################
############################################################################################################
# Load environment variables 

# You can get your API keys from the following websites:
# https://platform.openai.com/
# https://serper.dev/



############################################################################################################
########################                    AGENTS                    ######################################
############################################################################################################
# about agent parameters
# role: The role of the agent in the research process.
# goal: The goal of the agent in the research process.
# backstory: A description of the agent's background and experience.
# llm: The language model used by the agent.
# allow_delegation: Whether the agent is allowed to delegate tasks to other agents.
# tools: A list of tools that the agent can use to perform tasks.
############################################################################################################
###########################################################################################################



Agents = Search_crew(context_topic, question, llm)
Tasks = create_tasks(question, context_topic, output_directory, Agents)

                                                                                                    
############################################################################################################
########################                    crew######                #####################################
############################################################################################################


# Setting up the team (Crew)
crew = Crew(
    # List of agents in the crew
    agents=Agents, 

    # List of tasks to be performed by the crew
    tasks=Tasks,

    process=Process.sequential,  # Sequential process for task execution
    manager_llm=llm, # Setting the LLM to manage the crew
    verbose =True
)

# Starting the process with a specific transcription path (pdf_path)
result = crew.kickoff()
print(result)