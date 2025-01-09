


from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

tools = [search_tool, scrape_tool]

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
############################################################################################################

def Search_Agents(context_topic, question, llm):
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

    Agents = [researcher, chief_researcher, data_miner, data_analyst, academic_reviewer, scientific_writer]


    return Agents
