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
    role=f"Senior Research Specialist in {context_topic}",
    goal=f"Identify and validate the best online sources for gathering reliable and relevant information on {context_topic}.",
    backstory=f"""
    With extensive expertise in researching {context_topic}, 
    this agent excels at identifying and validating trustworthy sources to ensure high-quality findings.
    """,
    llm=llm,
    allow_delegation=True,
    tools=tools
)


# Chief Researcher

chief_researcher = Agent(
    role="Chief Researcher",
    goal=f"Define new, relevant questions based on initial findings and validate the most reliable sources on {context_topic}.",
    backstory=f"""
    With a strong background in advanced research methodologies, 
    this agent identifies knowledge gaps, proposes innovative directions, and ensures source credibility.
    """,
    llm=llm,
    allow_delegation=False,
    tools=tools
)


# Data Miner
data_miner = Agent(
    role="Data Miner",
    goal=f"Gather and organize data from verified sources to support research on {question}.",
    backstory="A senior data engineer specializing in sourcing and organizing information from credible online resources.",
    llm=llm,
    allow_delegation=False,
    tools=tools
)



# Data Analyst
data_analyst = Agent(
    role="Senior Data Analyst",
    goal=f"Analyze data collected from validated sources and extract clear, actionable insights related to {question}.",
    backstory="An expert in data interpretation, structuring findings into accurate and comprehensive reports.",
    llm=llm,
    allow_delegation=False,
    tools=tools
)



# Academic Reviewer
academic_reviewer = Agent(
    role="Academic Reviewer",
    goal=f"Critically review the collected and analyzed data for accuracy, consistency, and relevance to {context_topic} and {question}.",
    backstory="An expert in academic review, ensuring quality, accuracy, and reliability in all research outcomes.",
    llm=llm,
    allow_delegation=True,
    tools=tools
)


scientific_writer = Agent(
    role="Scientific Writer",
    goal=f"Research, analyze, and compose a detailed scientific document based on validated data regarding {question}.",
    backstory="An accomplished writer skilled in creating clear, structured, and impactful scientific documents.",
    llm=llm,
    allow_delegation=False,
    tools=tools
)


############################################################################################################
########################                    Task                    ######################################
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
    description=f"Identify and validate the most reliable websites and sources to address the question: {question}.",
    expected_output=f"A detailed document summarizing key findings and validated sources addressing the question: {question}.",
    agent=researcher
)


# Data Collection Task
data_collection_task = Task(
    description=f"""
    Collect updated data from validated sources to address the question: {question}. 
    Ensure data quality and relevance during collection.
    """,
    expected_output="A comprehensive dataset organized for subsequent analysis.",
    agent=data_miner,
    context=[research_management_task],
    output_file=os.path.join(output_directory, "1-start.md")
)

# Data Analysis Task
data_analysis_task = Task(
    description="Evaluate and analyze the collected data, extracting detailed insights and structuring findings.",
    expected_output=f"A curated list of the most reliable sources offering comprehensive answers to the question: {question}.",
    agent=data_analyst,
    context=[research_management_task, data_collection_task],
    output_file=os.path.join(output_directory, "2-acurate-list.md")
)


# Data Review Task
data_review_task = Task(
    description=f"""
    Review the analyzed material, ensuring accuracy, consistency, and relevance of findings related to {context_topic}.
    """,
    expected_output="A detailed report offering feedback and suggestions for improvement.",
    agent=academic_reviewer,
    context=[data_analysis_task],
    output_file=os.path.join(output_directory, "3-data-review.md")
)


# Article Writing Task
article_writing_task = Task(
    description=f"Compose a structured, comprehensive document summarizing the findings and the best sources for the question: {question}.",
    expected_output="A final document containing a detailed explanation, links to sources, and actionable insights.",
    agent=scientific_writer,
    async_execution=False,
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task],
    output_file=os.path.join(output_directory, "4-final-report.md")
)


# New Questions Task
new_questions_task = Task(
    description=f"Generate new, relevant questions to expand the scope of research based on findings related to {question}.",
    expected_output="A list of additional questions designed to deepen understanding and continue the research.",
    agent=chief_researcher,
    output_file=os.path.join(output_directory, "5-questions.md"),
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task],
    # human_input=True
)

# References Task
references_task = Task(
    description="Compile a comprehensive list of all sources used during the research, including detailed descriptions and links.",
    expected_output="A detailed reference list of all sources used in the research.",
    agent=academic_reviewer,
    output_file=os.path.join(output_directory, "6-references.md"),
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
    verbose =True
)

# Starting the process with a specific transcription path (pdf_path)
result = crew.kickoff()
print(result)
