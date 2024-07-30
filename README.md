# CrewAI Health Recommendations System

## Overview
This project sets up a crew of agents using the CrewAI framework to analyze blood test reports, search for relevant articles, and provide health recommendations. The system is designed to help users gain insights into their health by processing medical data and retrieving relevant information from various sources.

## Approach

Starting from scratch, break the main objective into smaller, manageable tasks. Identify the needs of smaller task. Designed specific agents to handle each of these tasks using the CrewAI framework.

1. **Agent Design**: Created multiple specialized agents with specific roles, including PDF extraction, abnormal marker identification, blood test analysis, article searching, and health recommendation generation.
2. **Task Handling**: Defined tasks for each agent in a modular fashion to ensure clear responsibilities and easy maintenance.
3. **CrewAI Integration**: Leveraged the CrewAI framework to coordinate the tasks of these agents and ensure efficient processing of user input.
4. **Internet Search Integration**: Developed a tool to perform internet searches using the Serper API, allowing the system to find relevant medical information based on blood test analysis.
5. **PDF Data Extraction**: Implemented a tool to extract text from PDF files using the PyMuPDF library, enabling efficient processing of blood test reports.

## Files
- `agents.py`: Contains the definitions and implementations of the agents used in the project.
- `main.py`: The main script that sets up the CrewAI environment and runs the agents.
- `tasks.py`: Defines the tasks assigned to the agents, detailing how each task is performed.
- `search_tools.py`: Implements internet search functionality using the Serper API.
- `pdf_tools.py`: Provides tools for extracting text from PDF files.

## How to Run

Follow these steps to run the Health Recommendation Agent:

1. **Clone the repository**:
   ```
   git clone https://github.com/onismn/Health-Recommendation-Agent
   cd health-recommendation-agent
   ```

2. **Set up the environment**:
   Ensure you have Python 3.11.0 to 3.11.2 installed. Then, install Poetry if you haven't already:
   ```
   pip install poetry
   ```

3. **Install dependencies**:
   ```
   poetry install
   ```

4. **Set up your API keys**:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

5. **Run the application**:
   ```
   poetry run python main.py
   ```

6. **Follow the prompts**:
   When prompted, enter the file path to your blood test report PDF.

7. **Review the results**:
   The program will output a comprehensive health recommendation report based on your blood test results.

## Usage
- Place blood test report files in the designated input directory.
- The system will automatically process these files, search for relevant articles, and generate health recommendations.
- Output will be saved in the designated output directory.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
