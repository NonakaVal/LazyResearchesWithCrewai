from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

def create_product_content_agents_with_emotion(llm):
    # Validador de Fontes
    source_validator = Agent(
        role="Source Validation Specialist",
        goal="Ensure all research is conducted using reliable, high-quality sources. Validate the credibility of websites and resources.",
        backstory=(
            "An experienced researcher skilled in identifying trustworthy sources and ensuring the "
            "accuracy and authenticity of data to build a strong foundation for content creation."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Pesquisador de Produto
    product_researcher = Agent(
        role="Product Research Specialist",
        goal="Collect in-depth information about the product, including specifications, features, and potential use cases.",
        backstory=(
            "A dedicated product research expert with years of experience in gathering detailed insights "
            "about products and understanding their market impact."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Analista de Comparação
    competitor_analyst = Agent(
        role="Competitor Analyst",
        goal="Compare the product to competitors by identifying strengths, weaknesses, and differentiating features.",
        backstory=(
            "A market research specialist skilled in analyzing industry competition, identifying "
            "unique selling points, and providing actionable insights."
        ),
        llm=llm,
        allow_delegation=True,  # Allowing delegation for collaboration
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Analista de Avaliações
    review_analyst = Agent(
        role="Consumer Review Analyst",
        goal="Analyze consumer feedback and reviews to extract recurring themes, emotional responses, and common sentiments.",
        backstory=(
            "A customer insights expert with a keen eye for analyzing large volumes of consumer feedback, "
            "identifying key patterns, and translating them into actionable data."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool()]
    )

    # Criador de Ideias de Conteúdo
    content_idea_generator = Agent(
        role="Creative Content Strategist",
        goal="Develop innovative and engaging content ideas tailored to the product’s unique qualities and target audience.",
        backstory=(
            "A creative strategist with a strong background in brainstorming, ideation, and crafting "
            "content strategies that resonate with audiences and drive engagement."
        ),
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool()]
    )

    # Redator de Conteúdo
    content_writer = Agent(
        role="Content Writer",
        goal="Craft compelling, high-quality content based on research and creative ideas, tailored to the target audience.",
        backstory=(
            "A professional writer with expertise in creating clear, engaging, and impactful content across "
            "various formats, including blogs, product descriptions, and promotional material."
        ),
        llm=llm,
        allow_delegation=True,  # Allowing delegation for potential peer reviews
        tools=[SerperDevTool()]
    )

    # Analista de Emoção e Narrativa
    emotion_narrative_analyst = Agent(
        role="Emotion and Storytelling Specialist",
        goal="Identify the most effective emotional triggers and storytelling techniques to highlight in content creation.",
        backstory=(
            "A storytelling expert with deep knowledge of crafting emotional narratives that connect "
            "with audiences, enhance brand appeal, and drive engagement."
        ),
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Assembling all agents
    Agents = [
        source_validator,
        product_researcher,
        competitor_analyst,
        review_analyst,
        content_idea_generator,
        content_writer,
        emotion_narrative_analyst
    ]

    return Agents


def create_inbound_content_agents(llm):
    # Market Analyst
    market_analyst = Agent(
        role="Market Trends Analyst",
        goal="Identify market trends and consumer behaviors related to collectible video items.",
        backstory=(
            "A market analysis expert with extensive experience in identifying patterns and trends relevant "
            "to crafting effective inbound marketing strategies."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Format Strategist
    format_strategist = Agent(
        role="Format Strategist",
        goal="Generate creative ideas for content formats (blog posts, videos, carousels, e-books, etc.).",
        backstory=(
            "A creative strategist with deep expertise in developing innovative content formats that maximize audience engagement."
        ),
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool()]
    )

    # Storytelling Specialist
    storytelling_specialist = Agent(
        role="Storytelling Specialist",
        goal="Craft engaging and emotional narratives to highlight the value of collectible items.",
        backstory=(
            "A professional storyteller skilled in using narrative techniques to build emotional connections between products and audiences."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool()]
    )

    # Competitor Researcher
    competitor_researcher = Agent(
        role="Competitor Researcher",
        goal="Analyze competitors’ inbound marketing strategies and identify opportunities to stand out.",
        backstory=(
            "A competitive research expert who excels at uncovering unique selling points and creative marketing strategies to differentiate the brand."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    # Content Planner
    content_planner = Agent(
        role="Content Planner",
        goal="Develop a strategic inbound content plan tailored to the target audience of collectible items.",
        backstory=(
            "A strategic thinker with a background in organizing content calendars and aligning marketing goals with audience needs."
        ),
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool()]
    )

    return [
        market_analyst,
        format_strategist,
        storytelling_specialist,
        competitor_researcher,
        content_planner
    ]
