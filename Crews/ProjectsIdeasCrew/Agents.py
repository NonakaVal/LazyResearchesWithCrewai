


from crewai import Agent




context_topic = "output/4-final-report.md"

# Initialize tools
from crewai_tools import MDXSearchTool
md_reader = MDXSearchTool(context_topic)


tools = [md_reader]

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




def Project_crew(llm):
    Search_menager = Agent(
        role="Search Manager",
        goal="Identify and validate the best online sources for gathering reliable and relevant information.",
        backstory=f"""
        With extensive expertise in researching various topics, 
        this agent excels at identifying and validating trustworthy sources to ensure high-quality findings.    
        """,
        llm=llm,
        tools=tools)
    
    
    
    return [Search_menager]



    
