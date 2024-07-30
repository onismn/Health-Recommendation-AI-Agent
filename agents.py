from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.pdf_tools import PDFTools


class HealthRecommendationAgents:
    def __init__(self):
        self.OpenAIGPT = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

    def pdf_extractor(self):
        return Agent(
            role="PDF Extractor",
            backstory=dedent(f"""Expert in extracting data from PDF to covert it to a structured format"""),
            goal=dedent(f"""Expert in parsing PDF documents and extracting relevant information"""),
            max_iter=5,
            tools=[PDFTools.extract_text_from_pdf],
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )
        
    def abnormal_markers_identifier(self):
        return Agent(
            role="Abnormal Health Markers Identifier",
            backstory=dedent(f"""Medical expert specializing in identifying abnormal health markers using their test result values and reference values"""),
            goal=dedent(f""""Identify health markers outside the reference range from blood test results"""),
            max_iter=10,
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )

    def blood_test_analyzer(self):
        return Agent(
            role="Blood Test Analyzer",
            backstory=dedent(f"""Medical expert specializing in interpreting blood test results"""),
            goal=dedent(f"""Analyze blood test results and provide a summary"""),
            max_iter=10,
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT

        )

    def article_searcher(self):
        return Agent(
            role="Article Searcher",
            backstory=dedent(f"""Researcher skilled in finding accurate and relevant health information"""),
            goal=dedent(f"""Find relevant health articles based on analysis of blood test results"""),
            max_iter=10,
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )

    def health_recommender(self):
        return Agent(
            role="Health Recommender",
            backstory=dedent(f"""Health coach with expertise in translating medical data into actionable advice"""),
            goal=dedent(f"""Provide personalized health recommendations based on blood test results and research"""),
            max_iter=15,
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )
