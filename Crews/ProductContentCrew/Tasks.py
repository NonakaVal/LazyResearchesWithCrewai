from crewai import Task
import os

def create_product_content_tasks_with_emotion(product_name, output_directory, Agents):
    # Ensure product name is valid for file paths
    product_name_safe = product_name.replace(" ", "_").lower()

    # Task 1: Source Validation
    source_validation_task = Task(
        description=(
            f"Identify and validate reliable websites and sources for researching detailed information about '{product_name}'. "
            f"Focus on identifying sources that provide insights into consumer emotions and preferences related to the product."
        ),
        expected_output="A list of validated and reliable sources for product research, emphasizing emotional or storytelling elements.",
        agent=Agents[0],
        output_file=os.path.join(output_directory, f"1-source-validation_{product_name_safe}.md")
    )

    # Task 2: Product Research
    product_research_task = Task(
        description=(
            f"Collect detailed information about '{product_name}', including specifications, features, usage scenarios, "
            f"and any emotional or storytelling angles from validated sources."
        ),
        expected_output="A document containing comprehensive product details and potential emotional triggers.",
        agent=Agents[1],
        context=[source_validation_task],
        output_file=os.path.join(output_directory, f"2-product-details{product_name_safe}_.md")
    )

    # Task 3: Competitor Analysis
    competitor_comparison_task = Task(
        description=(
            f"Compare '{product_name}' with similar products in the market. Identify unique strengths, weaknesses, and features, "
            f"highlighting emotional or narrative aspects that make '{product_name}' stand out."
        ),
        expected_output="A comparison table or summary highlighting the product's position in the market and its emotional or storytelling advantages.",
        agent=Agents[2],
        context=[product_research_task],
        output_file=os.path.join(output_directory, f"3-competitor-comparison-{product_name_safe}.md")
    )

    # Task 4: Consumer Review Analysis
    review_analysis_task = Task(
        description=(
            f"Analyze consumer reviews and feedback for '{product_name}'. Identify recurring themes, emotional reactions, "
            f"and user stories that could be leveraged for creating engaging narratives about the product."
        ),
        expected_output="A summary of consumer insights, highlighting emotional triggers and feedback trends.",
        agent=Agents[3],
        context=[product_research_task],
        output_file=os.path.join(output_directory, f"4-review-analysis-{product_name_safe}_.md")
    )

    # Task 5: Content Idea Generation
    content_idea_generation_task = Task(
        description=(
            f"Generate creative content ideas for '{product_name}', such as blog posts, social media captions, or promotional materials. "
            f"Incorporate emotional storytelling elements like excitement, nostalgia, or trust to engage the audience effectively."
        ),
        expected_output="A list of content ideas emphasizing emotional engagement and storytelling.",
        agent=Agents[4],
        context=[competitor_comparison_task, review_analysis_task],
        output_file=os.path.join(output_directory, f"5-content-ideas-{product_name_safe}_.md")
    )

    # Task 6: Content Creation
    content_creation_task = Task(
        description=(
            f"Write high-quality content about '{product_name}', integrating storytelling techniques and evoking emotions "
            f"such as trust, excitement, or connection based on the research and consumer feedback."
        ),
        expected_output="A finalized content document ready for publication, incorporating emotional and storytelling elements.",
        agent=Agents[5],
        context=[product_research_task, content_idea_generation_task],
        output_file=os.path.join(output_directory, f"6-final-content-{product_name_safe}_.md")
    )

    # Task 7: Emotion and Narrative Analysis
    emotion_narrative_task = Task(
        description=(
            f"Analyze the product research, consumer feedback, and content ideas to suggest the most effective emotions or narrative techniques "
            f"to use in the final content about '{product_name}'."
        ),
        expected_output="A report identifying key emotional triggers and narrative strategies for the product.",
        agent=Agents[6],
        context=[review_analysis_task, content_creation_task],
        output_file=os.path.join(output_directory, f"{product_name_safe}_7-emotion-narrative.md")
    )

    return [
        source_validation_task,
        product_research_task,
        competitor_comparison_task,
        review_analysis_task,
        content_idea_generation_task,
        content_creation_task,
        emotion_narrative_task
    ]
