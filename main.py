import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from crewai import Crew, Process
from textwrap import dedent
import pymupdf

from agents import HealthRecommendationAgents
from tasks import HealthRecommendationTasks

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("## Welcome to Health Recommendation Crew")
print('-------------------------------')
pdf_file_path = input(dedent("Upload your Blood Report in PDF (enter the file path): "))


class HealthRecommendationCrew:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path

    def run(self):
        agents = HealthRecommendationAgents()
        tasks = HealthRecommendationTasks()

        pdf_extractor = agents.pdf_extractor()
        abnormal_markers_identifier = agents.abnormal_markers_identifier()
        blood_test_analyzer = agents.blood_test_analyzer()
        article_searcher = agents.article_searcher()
        health_recommender = agents.health_recommender()

        extract_pdf = tasks.extract_pdf(pdf_extractor, self.pdf_file_path)
        identify_abnormal_markers = tasks.identify_abnormal_markers(abnormal_markers_identifier, [extract_pdf])
        analyze_blood_test = tasks.analyze_blood_test(blood_test_analyzer, [identify_abnormal_markers])
        search_articles = tasks.search_articles(article_searcher, [identify_abnormal_markers, analyze_blood_test])
        health_recommendations = tasks.health_recommendations(health_recommender, [identify_abnormal_markers, analyze_blood_test, search_articles])

        crew = Crew(
            agents=[pdf_extractor,
                    abnormal_markers_identifier,
                    blood_test_analyzer,
                    article_searcher,
                    health_recommender],
            tasks=[extract_pdf,
                    identify_abnormal_markers,
                    analyze_blood_test,
                    search_articles,
                    health_recommendations],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        result = crew.kickoff()
        return result


health_recommendation_crew = HealthRecommendationCrew(pdf_file_path)
result = health_recommendation_crew.run()
print("\n\n##############################")
print("## Here is you custom crew run result:")
print("##############################\n")
print(result)
