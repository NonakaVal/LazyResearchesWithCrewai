
# Função para criar tarefas específicas de game news scraping

from crewai import Task
import os
def create_game_news_scraping_tasks(context_topic, news_category, output_directory, Agents):
    # Tarefa de Pesquisa Inicial
    source_validation_task = Task(
        description=f"Identify and validate the most reliable gaming news websites for {context_topic} and {news_category}.",
        expected_output="A list of trustworthy gaming news sources.",
        agent=Agents[0]  
    )

    # Tarefa de Coleta de Notícias
    news_scraping_task = Task(
        description=f"""
        Scrape the latest gaming news articles related to {context_topic} and {news_category} 
        from the validated sources.
        """,
        expected_output="A collection of raw data containing the latest news articles.",
        agent=Agents[1],
        context=[source_validation_task],
        output_file=os.path.join(output_directory, "1-raw-news-data.md")
    )

    # Tarefa de Análise de Conteúdo
    content_analysis_task = Task(
        description="Analyze the collected news articles to extract key insights, trends, and notable updates.",
        expected_output="A summarized report of key insights and trends in gaming news.",
        agent=Agents[2],
        context=[news_scraping_task],
        output_file=os.path.join(output_directory, "2-analyzed-news.md")
    )

    # Tarefa de Organização
    news_organization_task = Task(
        description=f"Organize the analyzed news into categories, such as reviews, updates, launches, or other subtopics related to {context_topic}.",
        expected_output="A categorized and well-organized news dataset.",
        agent=Agents[3],
        context=[content_analysis_task],
        output_file=os.path.join(output_directory, "3-organized-news.md")
    )

    # Tarefa de Escrita de Resumo
    news_summary_task = Task(
        description=f"Write a structured and engaging summary of the most significant news items related to {context_topic} and {news_category}.",
        expected_output="A final summary report suitable for publishing or sharing.",
        agent=Agents[4],
        async_execution=False,
        context=[news_organization_task],
        output_file=os.path.join(output_directory, "4-news-summary.md"),
        human_input=True
    )

    # Tarefa de Ideias de Conteúdo
    content_idea_generation_task = Task(
        description=f"Generate content ideas or headlines for articles or social media posts based on the news about {context_topic}.",
        expected_output="A list of creative content ideas based on the latest gaming news.",
        agent=Agents[5],
        context=[news_summary_task],
        output_file=os.path.join(output_directory, "5-content-ideas.md")
    )

    Tasks = [
        source_validation_task, news_scraping_task, content_analysis_task,
        news_organization_task, news_summary_task, content_idea_generation_task
    ]

    return Tasks