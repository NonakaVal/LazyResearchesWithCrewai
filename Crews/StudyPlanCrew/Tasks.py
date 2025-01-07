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
# Função para criar tarefas e roadmaps de estudo/projeto
def create_study_project_roadmap_tasks(context_topic, output_directory, Agents):
    # Inicialização das tarefas
    initial_planning_task = Task(
        description=f"Create a high-level study and project roadmap for the topic: {context_topic}. Define phases, goals, and objectives.",
        expected_output="A comprehensive roadmap with structured phases, goals, and actionable steps for the study/project.",
        agent=Agents[0]  
    )

    topic_specialization_task = Task(
        description=f"Identify key subtopics and areas of specialization related to {context_topic} to be included in the roadmap.",
        expected_output="A detailed breakdown of subtopics and specialization areas to be explored during the study/project.",
        agent=Agents[1],
        context=[initial_planning_task],
        output_file=os.path.join(output_directory, "1-topic-specialization.md")
    )

    project_timeline_task = Task(
        description="Create a detailed timeline for the study/project, defining deadlines, milestones, and key deliverables.",
        expected_output="A project timeline with defined deadlines and milestones for each phase.",
        agent=Agents[2],
        context=[initial_planning_task, topic_specialization_task],
        output_file=os.path.join(output_directory, "2-project-timeline.md")
    )

    tools_resources_task = Task(
        description=f"Research and identify the necessary tools, courses, and resources for the study/project roadmap of {context_topic}.",
        expected_output="A list of recommended tools, resources, and courses to support the roadmap.",
        agent=Agents[3],
        context=[project_timeline_task],
        output_file=os.path.join(output_directory, "3-tools-resources.md")
    )

    review_task = Task(
        description="Review the entire roadmap, ensuring that all steps are feasible, relevant, and aligned with the goals of the study/project.",
        expected_output="A review report offering feedback and suggestions for improvement.",
        agent=Agents[4],
        context=[project_timeline_task, tools_resources_task],
        output_file=os.path.join(output_directory, "4-roadmap-review.md")
    )

    documentation_task = Task(
        description=f"Write detailed documentation explaining each step of the study/project roadmap for {context_topic}.",
        expected_output="A detailed document explaining the phases, tasks, milestones, and resources for the study/project.",
        agent=Agents[5],
        async_execution=False,
        context=[initial_planning_task, topic_specialization_task, project_timeline_task, tools_resources_task, review_task],
        output_file=os.path.join(output_directory, "5-roadmap-documentation.md"),
        human_input=True
    )

    new_ideas_task = Task(
        description=f"Generate new, innovative project ideas and study topics related to {context_topic} based on the roadmap created.",
        expected_output="A list of new project ideas and potential areas for further study.",
        agent=Agents[1],
        output_file=os.path.join(output_directory, "6-new-ideas.md"),
        context=[initial_planning_task, topic_specialization_task, project_timeline_task, tools_resources_task, review_task, documentation_task]
    )

    final_report_task = Task(
        description="Compile the final report summarizing the entire study/project roadmap and ideas generated.",
        expected_output="A comprehensive final report containing the complete roadmap and all supporting documentation.",
        agent=Agents[5],
        output_file=os.path.join(output_directory, "7-final-report.md"),
        context=[initial_planning_task, topic_specialization_task, project_timeline_task, tools_resources_task, review_task, documentation_task, new_ideas_task]
    )

    Tasks = [
        initial_planning_task, topic_specialization_task, project_timeline_task, 
        tools_resources_task, review_task, documentation_task, new_ideas_task, final_report_task
    ]

    return Tasks