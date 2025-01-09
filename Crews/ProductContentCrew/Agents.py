from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

def create_product_content_agents(llm):
    # Validador de Fontes
    source_validator = Agent(
        role="Source Validator",
        goal="Identify and validate reliable websites and sources for researching the product.",
        backstory="An expert in identifying trustworthy sources to ensure research accuracy.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Pesquisador de Produto
    product_researcher = Agent(
        role="Product Researcher",
        goal="Gather comprehensive details about the product from validated sources.",
        backstory="A skilled researcher focused on understanding product features and specifications.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Analista de Comparação
    competitor_analyst = Agent(
        role="Competitor Analyst",
        goal="Compare the product with competitors to identify unique selling points and weaknesses.",
        backstory="An analyst with expertise in market research and competitive analysis.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Analista de Avaliações
    review_analyst = Agent(
        role="Review Analyst",
        goal="Analyze consumer reviews to identify common themes, strengths, and concerns.",
        backstory="An expert in extracting insights from customer feedback.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Criador de Ideias de Conteúdo
    content_idea_generator = Agent(
        role="Content Idea Generator",
        goal="Develop creative ideas for content based on the research and analysis.",
        backstory="A creative thinker with experience in content ideation and strategy.",
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Redator de Conteúdo
    content_writer = Agent(
        role="Content Writer",
        goal="Write high-quality content based on the product research and ideas generated.",
        backstory="A professional writer experienced in creating engaging and informative content.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    Agents = [
        source_validator,
        product_researcher,
        competitor_analyst,
        review_analyst,
        content_idea_generator,
        content_writer
    ]

    return Agents
