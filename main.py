from builtins import input, print
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


############################################################################################################
########################                    App Setup                    ######################################
############################################################################################################
# Load environment variables 

# You can get your API keys from the following websites:
# https://platform.openai.com/
# https://serper.dev/

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.1,
    max_tokens=1500
)
# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
tools = [search_tool, scrape_tool]

############################################################################################################
# Function to select the output directory
############################################################################################################
def select_output_directory():
    output_dir = input("Choose the name of the directory to be created to save your summaries. \n")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

############################################################################################################
# Prompt the user for input
output_directory = select_output_directory()
context_topic = input("Enter the research context: \n")
question = input("Enter the research question: \n")



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
############################################################################################################

# Researcher
researcher = Agent(
    role=f'Senior Research Specialist in {context_topic}',
    goal=f'Identify and validate the best websites and online sources to gather relevant information about {context_topic}.',

    backstory=f"""
    With extensive experience in research on {context_topic}, 
    this agent is capable of finding and validating trustworthy online sources."
    """,
    llm=llm,
    allow_delegation=True,
    tools=tools
)

# Chief Researcher
chief_researcher = Agent(
    role='Chief Researcher',
    goal=f'Define new relevant questions based on initial research findings and validate the best sources about: {context_topic}.',
    backstory=
    """
    Experienced in research methodologies, 
    this agent is capable of identifying gaps and proposing new directions for investigation, 
    as well as validating trustworthy sources.",
    """,
    llm=llm,
    allow_delegation=False,
    tools=tools
)

# Data Miner
data_miner = Agent(
    role='Data Miner',
    goal=f'Collect data from validated websites and organize it for detailed research about: {question}.',
    backstory="Senior data engineer, specializing in collecting and organizing data from trustworthy online sources.",
    llm=llm,
    allow_delegation=False,
    tools=tools
)

# Data Analyst
data_analyst = Agent(
    role='Senior Data Analyst',
    goal=f'Analyze data collected from validated online sources, extracting insights and structuring a clear and understandable document about {question}.',
    backstory="Specialized in data analysis and the preparation of detailed and accurate reports from online sources.",
    allow_delegation=False,
    llm=llm,
    tools=tools
)

# Academic Reviewer
academic_reviewer = Agent(
    role='Academic Reviewer',
    goal=f'Review the data collected from online sources and provide critical feedback to ensure the accuracy of the content about {context_topic} and {question}',
    backstory="With refined skills in reviewing online sources, this agent ensures the quality and accuracy of the research results.",
    llm=llm,
    allow_delegation=True,
    tools=tools
)

# Scientific Writer
scientific_writer = Agent(
    role='Scientific Writer',
    goal='Research, analyze, and write a structured scientific document based on data from validated online sources about {question}.',
    backstory="Capable of conducting detailed research and communicating discoveries clearly and persuasively, this agent produces high-quality scientific documents.",
    llm=llm,
    allow_delegation=False,
    tools=tools
)


############################################################################################################
########################                    AGENTS                    ######################################
############################################################################################################
# about task parameters
# description: A description of the task.
# expected_output: The expected output of the task.
# agent: The agent responsible for performing the task.
# async_execution: Whether the task should be executed asynchronously.
# context: A list of tasks that must be completed before this task can be executed.
# output_file: The file path where the output of the task should be saved.
############################################################################################################


# Research Management Task
research_management_task = Task(
    description=f"Identify and validate the best websites and online sources to answer the question: {question}.",
    expected_output=f'Detailed document covering all necessary topics to answer the question: {question}.',
    agent=researcher,
    
)

# Data Collection Task
data_collection_task = Task(
    description=f"""

    Collect updated data from validated online sources to answer the question: {question}. 
    Use validated methods and ensure the quality of the data collected.",
    """,
    expected_output="Large amount of data collected and prepared for analysis.",
    agent=data_miner,
    context=[research_management_task]
)

# Data Analysis Task
data_analysis_task = Task(
    description="Analyze the data collected from validated online sources, extracting detailed and relevant insights.",
    expected_output=f'List of websites with the best and most detailed answers to the question: {question}.',
    
    agent=data_analyst,
    context=[research_management_task, data_collection_task]
)

# Data Review Task
data_review_task = Task(
    description=f"""
    Review the collected and analyzed material from online sources, ensuring accuracy, consistency, 
    and relevance in the research findings about {context_topic}.',
    """,
    expected_output="Detailed report with improvement suggestions and critical feedback.",

    agent=academic_reviewer,
    context=[data_analysis_task]
)

# Article Writing Task
article_writing_task = Task(
    description=f"Write a structured and complete document with all the websites providing the best answers to the question: {question}.",
    expected_output="Complete and structured document with the best results, links, and detailed explanations.",
    agent=scientific_writer,
    async_execution=False,
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task],
    output_file=os.path.join(output_directory, "3-final.md")
)

# New Questions Task
new_questions_task = Task(
    description=f"Develop new relevant questions to deepen the research based on the findings from the research about: {question}.",
    expected_output="List of new questions that need to be answered to advance the study.",
    agent=chief_researcher,
    output_file=os.path.join(output_directory, "4-questions.md"),
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task],
    human_input=True
)

# References Task
references_task = Task(
    description="List all the sources and websites used during the research, with detailed descriptions.",
    expected_output="List with all sources used, including descriptions and links.",
    agent=academic_reviewer,
    output_file=os.path.join(output_directory, "5-references.md"),
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, new_questions_task]
)


############################################################################################################
########################                    crew######                #####################################
############################################################################################################

# Setting up the team (Crew)
crew = Crew(
    # List of agents in the crew
    agents=[researcher, 
            chief_researcher, 
            data_miner, 
            data_analyst, 
            academic_reviewer,
            scientific_writer], 

    # List of tasks to be performed by the crew
    tasks=[research_management_task, 
           data_collection_task,
           data_analysis_task, 
           data_review_task, 
           article_writing_task, 
           new_questions_task, 
           references_task],

    process=Process.sequential,  # Sequential process for task execution
    manager_llm=llm, # Setting the LLM to manage the crew
    verbose=True
)

# Starting the process with a specific transcription path (pdf_path)
result = crew.kickoff()
print(result)
