from crewai import Task
import os


############################################################################################################
########################                    Task                    ######################################
############################################################################################################
# about task parameters
# description: A description of the task.
# expected_output: The expected output of the task.
# agent: The agent responsible for performing the task.
# async_execution: Whether the task should be executed asynchronously.
# context: A list of tasks that must be completed before this task can be executed.
# output_file: The file path where the output of the task should be saved.
############################################################################################################

def Search_tasks(question, context_topic, output_directory, Agents):
    # Research Management Task
    research_management_task = Task(
        description=f"Identify and validate the most reliable websites and sources to address the question: {question}.",
        expected_output=f"A detailed document summarizing key findings and validated sources addressing the question: {question}.",
        agent=Agents[0]  
    )


    # Data Collection Task
    data_collection_task = Task(
        description=f"""
        Collect updated data from validated sources to address the question: {question}. 
        Ensure data quality and relevance during collection.
        """,
        expected_output="A comprehensive dataset organized for subsequent analysis.",
        agent=Agents[1],
        context=[research_management_task],
        output_file=os.path.join(output_directory, "1-start.md")
    )

    # Data Analysis Task
    data_analysis_task = Task(
        description="Evaluate and analyze the collected data, extracting detailed insights and structuring findings.",
        expected_output=f"A curated list of the most reliable sources offering comprehensive answers to the question: {question}.",
        agent=Agents[2],
        context=[research_management_task, data_collection_task],
        output_file=os.path.join(output_directory, "2-acurate-list.md")
    )


    # Data Review Task
    data_review_task = Task(
        description=f"""
        Review the analyzed material, ensuring accuracy, consistency, and relevance of findings related to {context_topic}.
        """,
        expected_output="A detailed report offering feedback and suggestions for improvement.",
        agent= Agents[3],
        context=[data_analysis_task],
        output_file=os.path.join(output_directory, "3-data-review.md")
    )


    # Article Writing Task
    article_writing_task = Task(
        description=f"Compose a structured, comprehensive document summarizing the findings and the best sources for the question: {question}.",
        expected_output="A final document containing a detailed explanation, links to sources, and actionable insights.",
        agent=Agents[5],
        async_execution=False,
        context=[research_management_task, data_collection_task, data_analysis_task, data_review_task],
        output_file=os.path.join(output_directory, "4-final-report.md"),
        human_input=True
    )


    # New Questions Task
    new_questions_task = Task(
        description=f"Generate new, relevant questions to expand the scope of research based on findings related to {question}.",
        expected_output="A list of additional questions designed to deepen understanding and continue the research.",
        agent=Agents[1],
        output_file=os.path.join(output_directory, "5-questions.md"),
        context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task],
        # human_input=True
    )

    # References Task
    references_task = Task(
        description="Compile a comprehensive list of all sources used during the research, including detailed descriptions and links.",
        expected_output="A detailed reference list of all sources used in the research.",
        agent=Agents[4],
        output_file=os.path.join(output_directory, "6-references.md"),
        context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, new_questions_task]
    )
    Tasks = [research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, new_questions_task, references_task]


    return Tasks

