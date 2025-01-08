
# Função para criar agentes específicos de game news scraping
from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

def create_game_news_agents(llm):
    source_validator = Agent(
        role="Gaming Source Validator",
        goal="Identify the most trustworthy sources for gaming news to ensure accurate and up-to-date information.",
        backstory="An expert in finding and validating credible news sources in the gaming industry.",
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    news_scraper = Agent(
        role="Gaming News Scraper",
        goal="Scrape gaming news articles and data from validated sources, ensuring relevance and quality.",
        backstory="A tech-savvy data miner with expertise in scraping and collecting gaming-related content.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    content_analyst = Agent(
        role="Gaming Content Analyst",
        goal="Analyze the collected news articles to identify trends, key insights, and notable updates.",
        backstory="A data analyst with a keen eye for trends and insights in the gaming world.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    news_organizer = Agent(
        role="Gaming News Organizer",
        goal="Organize gaming news into categories for easy access and readability.",
        backstory="An organizer skilled in structuring and categorizing information for clarity and usability.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    summary_writer = Agent(
        role="Gaming News Writer",
        goal="Write summaries and engaging reports of gaming news for publication or sharing.",
        backstory="A writer with a flair for turning complex news into concise, engaging summaries.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    content_idea_generator = Agent(
        role="Content Idea Generator",
        goal="Develop creative ideas and headlines for articles or social media based on gaming news.",
        backstory="A creative thinker with experience in generating compelling content ideas for the gaming industry.",
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    Agents = [
        source_validator, news_scraper, content_analyst,
        news_organizer, summary_writer, content_idea_generator
    ]

    return Agents