from builtins import input, print
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from crewai import Crew, Process

# Importing utility functions
from Crews.Tools import (
    select_output_directory,
    combine_markdown_files_with_folders,
    translate_and_combine_markdown_files,
)

# Importing agents and tasks from different crews
from Crews.MainSearchCrew.Agents import Search_Agents
from Crews.MainSearchCrew.Tasks import Search_tasks
from Crews.StudyPlanCrew.Agents import create_study_project_agents
from Crews.StudyPlanCrew.Tasks import create_study_project_roadmap_tasks




# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=1500
)


############################################################################################################
# Function to Select Crew and Configure Tasks
############################################################################################################
def select_crew():
    """
    Allows the user to select a crew and configure tasks for that crew.
    Returns the agents, tasks, output directories, and context topic.
    """
    print("Select the crew you want to use:")
    print("1. Search Crew")
    print("2. Study Plan Crew")


    crew_choice = input("Enter 1, 2, 3, 4 or 5: ")

    # Select the appropriate crew
    if crew_choice == "1":
        context_topic = input("Enter the research context for Search Crew: \n")
        question = input("Enter the research question for Search Crew: \n")
        agents = Search_Agents(context_topic, question, llm)
        separated_folder, combined_folder = select_output_directory("output/1.answers-output-SearchCrew", context_topic)
        tasks = Search_tasks(question, context_topic, separated_folder, agents)
    elif crew_choice == "2":
        context_topic = input("Enter the research context for Study Plan Crew: \n")
        question = input("Enter the research question for Study Plan Crew: \n")
        agents = create_study_project_agents(context_topic, question, llm)
        separated_folder, combined_folder = select_output_directory("output/2.answers-output-StudyPlanCrew", context_topic)
        tasks = create_study_project_roadmap_tasks(context_topic, separated_folder, agents)


    return agents, tasks, separated_folder, combined_folder, context_topic


############################################################################################################
# Main Function
############################################################################################################


def main():
    # Select the crew and configure tasks
    agents, tasks, separated_folder, combined_folder, context_topic = select_crew()

    # Configure and execute the crew
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        manager_llm=llm,
        verbose=True
    )

    print("Starting the crew tasks...")
    result = crew.kickoff()
    print(result)

    # Generate the combined file
    combined_filename = f"{context_topic.replace(' ', '_')}-complete.md"
    print(f"Combining individual markdown files into: {combined_filename}")
    combined_filepath = combine_markdown_files_with_folders(separated_folder, combined_folder, combined_filename)

    # Translate and combine markdown files
    print("Translating and combining markdown files into a single PT-BR file...")
    translate_and_combine_markdown_files(separated_folder, combined_folder, combined_filename, llm)

    print(f"Process completed. Check the '{combined_folder}' folder for results.")


############################################################################################################
# Entry Point
############################################################################################################
if __name__ == "__main__":
    main()
