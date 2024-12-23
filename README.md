# Research Automation Framework

Creating research summaries with [GPT](https://platform.openai.com) and [crewAI](https://crewai.com),

This project is a Python-based framework designed to automate research workflows. By leveraging AI agents, tools, and task management, the framework assists in conducting comprehensive research and generating well-structured outputs.


## Features

1. **AI-Driven Agents**: Specialized agents with distinct roles to handle various aspects of the research process.
2. **Task Management**: Tasks are defined and executed sequentially to ensure a smooth workflow.
3. **Tool Integration**: Integrated tools for web scraping and search functionality.
4. **Customizable Output**: Allows users to select an output directory and define research parameters.
5. **Structured Outputs**: Generates reports, insights, and references based on research findings.

---

## Prerequisites

### Python Libraries
Ensure you have the following Python libraries installed:
- `dotenv`
- `os`
- `crewai`
- `crewai_tools`
- `langchain_openai`

Install any missing dependencies using pip:
```bash
pip install python-dotenv crewai langchain_openai
```

### API Keys
You will need API keys for:
- [OpenAI](https://platform.openai.com/)
- [Serper.dev](https://serper.dev/)

Store these keys in a `.env` file:
```
OPENAI_API_KEY="your_openai_key"
SERPER_API_KEY="your_serper_key"
```

---

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/NonakaVal/LazyResearchesWithCrewai.git
cd LazyResearchesWithCrewai
```

### 2. Set Up Environment
Ensure your `.env` file is correctly configured with your API keys.

### 3. Run the Script
Execute the main script:
```bash
python main.py
```

### 4. Input Parameters
You will be prompted to:
1. Choose a directory for saving results.
2. Define the research context.
3. Enter the primary research question.

### 5. Outputs
- **Summaries**: Saved in the selected output directory.
- **New Questions**: File named `4-questions.md` with follow-up research questions.
- **References**: File named `5-references.md` listing all sources used.

---

## Framework Overview

### Agents
- **Researcher**: Identifies and validates online sources.
- **Chief Researcher**: Proposes new directions and validates findings.
- **Data Miner**: Collects and organizes data.
- **Data Analyst**: Extracts insights and structures findings.
- **Academic Reviewer**: Ensures quality and accuracy.
- **Scientific Writer**: Compiles findings into a structured document.

### Tasks
- Research Management
- Data Collection
- Data Analysis
- Data Review
- Article Writing
- Developing New Questions
- References Compilation

### Tools
- **SerperDevTool**: For performing online searches.
- **ScrapeWebsiteTool**: For extracting content from websites.

---

## Customization
You can adapt this framework by:
1. Adding new agents or modifying existing ones.
2. Adjusting tasks and workflows.
3. Incorporating additional tools.

---

## Contributions
Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## Acknowledgments
- [OpenAI](https://openai.com/)
- [Serper.dev](https://serper.dev/)



## First Outputs

- [DataScience Portifoli Ideas](https://github.com/NonakaVal/LazyResearchesWithCrewai/tree/main/output/datascience)
- [Backend Portifoli Ideas](https://github.com/NonakaVal/LazyResearchesWithCrewai/tree/main/output/backend)