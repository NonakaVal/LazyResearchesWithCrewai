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
        output_file=os.path.join(output_directory, f"7-emotion-narrative.md{product_name_safe}_")
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



def create_inbound_content_tasks(product_name, output_directory, Agents):
    import os

    # Sanitize product name for file paths
    product_name_safe = product_name.replace(" ", "_").lower()

    # Task 1: In-Depth Market Trends Research
    market_research_task = Task(
        description=(
            f"Conduct an in-depth analysis of current market trends, emerging consumer behaviors, and purchasing patterns related to '{product_name}' "
            f"within the collectible items industry. Identify growth opportunities, rising niches, and market challenges."
        ),
        expected_output="A comprehensive report highlighting market trends, consumer interests, and strategic opportunities for collectible items.",
        agent=Agents[0],
        output_file=os.path.join(output_directory, f"1-market-trends-{product_name_safe}.md")
    )

    # Task 2: Comprehensive Competitor Analysis
    competitor_analysis_task = Task(
        description=(
            f"Analyze competitors' inbound marketing strategies for products similar to '{product_name}'. "
            f"Identify their strengths, weaknesses, marketing gaps, and areas where we can differentiate our approach."
        ),
        expected_output="An actionable competitor analysis report comparing marketing tactics and highlighting opportunities for brand positioning.",
        agent=Agents[3],
        context=[market_research_task],
        output_file=os.path.join(output_directory, f"2-competitor-analysis-{product_name_safe}.md")
    )

    # Task 3: Innovative Content Format Development
    content_format_task = Task(
        description=(
            f"Develop a variety of creative and engaging content format ideas for promoting '{product_name}', with a primary focus on Instagram and WhatsApp platforms. "
            f"Include suggestions for social media campaigns, interactive content, reels, stories, and viral marketing tactics."
        ),
        expected_output="A detailed list of innovative content formats tailored for Instagram, WhatsApp, and other relevant platforms to maximize audience reach and engagement.",
        agent=Agents[1],
        context=[market_research_task],
        output_file=os.path.join(output_directory, f"3-content-formats-{product_name_safe}.md")
    )

    # Task 4: Emotional and Engaging Storytelling Framework
    storytelling_task = Task(
        description=(
            f"Craft a compelling and emotionally driven storytelling framework for '{product_name}'. Incorporate key emotional triggers such as nostalgia, exclusivity, "
            f"and the thrill of collecting. Focus on building a strong emotional connection with the audience."
        ),
        expected_output="A well-structured storytelling framework designed to emotionally engage the target audience and elevate the perceived value of the product.",
        agent=Agents[2],
        context=[competitor_analysis_task, content_format_task],
        output_file=os.path.join(output_directory, f"4-storytelling-{product_name_safe}.md")
    )

    # Task 5: Strategic and Actionable Content Plan
    content_plan_task = Task(
        description=(
            f"Develop a comprehensive and actionable inbound content marketing plan for '{product_name}'. Integrate insights from market trends, competitor analysis, "
            f"innovative content formats, and emotional storytelling to create a strategy that drives engagement and conversions."
        ),
        expected_output="A detailed, step-by-step inbound content marketing strategy aligned with brand goals and audience preferences, ready for implementation.",
        agent=Agents[4],
        context=[storytelling_task],
        output_file=os.path.join(output_directory, f"5-content-plan-{product_name_safe}.md")
    )

    return [
        market_research_task,
        competitor_analysis_task,
        content_format_task,
        storytelling_task,
        content_plan_task
    ]
