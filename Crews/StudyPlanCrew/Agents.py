
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

tools = [search_tool, scrape_tool]

def create_study_project_agents(question,context_topic, llm):
    study_planner = Agent(
        role=f"Study Planner specialist in {context_topic}",
        goal=f"Create a high-level roadmap for studies and projects in the field of the specified topic : {question}.",
        backstory="An experienced strategist with a background in educational and project planning. They design structured roadmaps for efficient learning and project execution.",
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    topic_specialist = Agent(
        role=f"{context_topic} Specialist",
        goal=f"Identify key subtopics and areas of specialization for the roadmap to {question}.",
        backstory=f"An expert in the specified field : {context_topic}, capable of breaking down topics into manageable areas of study.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    project_manager = Agent(
        role="Project Manager",
        goal="Design a detailed project timeline with milestones and deadlines.",
        backstory="A seasoned project manager with expertise in structuring tasks, timelines, and key deliverables for successful project completion.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    tools_researcher = Agent(
        role="Tools and Resources Researcher",
        goal="Find the best tools, courses, and resources to aid in the study/project process.",
        backstory="A resourceful researcher capable of identifying relevant tools and educational resources to enhance the roadmap.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    academic_reviewer = Agent(
        role="Academic Reviewer",
        goal="Review the roadmap to ensure accuracy, relevance, and feasibility.",
        backstory="An academic with expertise in reviewing study plans and project roadmaps, ensuring that all components align with learning goals and practical execution.",
        llm=llm,
        allow_delegation=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    documentation_writer = Agent(
        role="Documentation Writer",
        goal="Write clear, structured documentation for the roadmap and project ideas.",
        backstory="A skilled writer experienced in turning complex ideas into clear, actionable documents that guide the execution of plans.",
        llm=llm,
        allow_delegation=False,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

    Agents = [study_planner, topic_specialist, project_manager, tools_researcher, academic_reviewer, documentation_writer]
    
    return Agents