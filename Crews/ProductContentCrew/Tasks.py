from crewai import Task
import os

def create_product_content_tasks(product_name, output_directory, Agents):
    # Tarefa 1: Validação de Fontes
    source_validation_task = Task(
        description=f"Identify and validate reliable websites and sources for researching detailed information about {product_name}.",
        expected_output="A list of validated and reliable sources for product research.",
        agent=Agents[0]
    )

    # Tarefa 2: Pesquisa Detalhada sobre o Produto
    product_research_task = Task(
        description=f"Collect detailed information about {product_name}, including specifications, features, and usage scenarios from validated sources.",
        expected_output="A document containing comprehensive product details.",
        agent=Agents[1],
        context=[source_validation_task],
        output_file=os.path.join(output_directory, "1-product-details.md")
    )

    # Tarefa 3: Comparação com Concorrentes
    competitor_comparison_task = Task(
        description=f"Compare {product_name} with similar products in the market to identify strengths, weaknesses, and unique features.",
        expected_output="A comparison table or summary highlighting the product's position in the market.",
        agent=Agents[2],
        context=[product_research_task],
        output_file=os.path.join(output_directory, "2-competitor-comparison.md")
    )

    # Tarefa 4: Análise de Avaliações
    review_analysis_task = Task(
        description=f"Analyze consumer reviews and feedback for {product_name} to identify key positive and negative aspects.",
        expected_output="A summary of consumer insights and common feedback trends.",
        agent=Agents[3],
        context=[product_research_task],
        output_file=os.path.join(output_directory, "3-review-analysis.md")
    )

    # Tarefa 5: Geração de Ideias de Conteúdo
    content_idea_generation_task = Task(
        description=f"Generate creative content ideas (e.g., blog posts, social media captions, promotional materials) based on the research and analysis of {product_name}.",
        expected_output="A list of content ideas tailored for promoting or explaining the product.",
        agent=Agents[4],
        context=[competitor_comparison_task, review_analysis_task],
        output_file=os.path.join(output_directory, "4-content-ideas.md")
    )

    # Tarefa 6: Criação de Conteúdo
    content_creation_task = Task(
        description=f"Write high-quality content (e.g., articles, social media posts, product descriptions) about {product_name} based on the research and generated ideas.",
        expected_output="A finalized content document ready for publication.",
        agent=Agents[5],
        async_execution=False,
        context=[product_research_task, content_idea_generation_task],
        output_file=os.path.join(output_directory, "5-final-content.md"),
        human_input=True
    )

    Tasks = [
        source_validation_task,
        product_research_task,
        competitor_comparison_task,
        review_analysis_task,
        content_idea_generation_task,
        content_creation_task
    ]

    return Tasks
