from crewai import Task
from textwrap import dedent

class HealthRecommendationTasks:

    def extract_pdf(self, agent, pdf_file_path):
        return Task(
            description=dedent(
                f"""
            **Task**: Extract Blood Test Results Data
            **Description**: Extract all relevant text data from the provided blood test report PDF.
                The PDF file is located at: {pdf_file_path}
                Follow these steps:
                1. Open and read the PDF file.
                2. Extract all text content from each page.
                3. Identify and extract specific sections related to blood test results.
                4. Organize extracted data into a structured plain text format under than specific sections.

            NOTE:
                a. Ensure the health marker is correctly identified based on the name or abbreviation provided.
                b. Extract the numeric result value associated with each health marker accurately.
                c. Verify that the unit of measurement for each health marker is correctly identified.
                d. Extract the reference range for each health marker, which can be a range or a threshold.
                

            **Parameters**:
            - PDF file for Blood Test Report: {pdf_file_path}

        """
            ),
            agent=agent,
            expected_output="A structured dictionary containing extracted blood test data: health marker, it's result value, it's unit, it's reference interval"
        )

    def identify_abnormal_markers(self, agent, context):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify Abnormal Health Markers
            **Description**: Review the extracted blood test data and identify health markers that are outside their reference ranges. Follow these steps:
                1. Review all blood test markers and their values from the extracted data.
                2. Compare each marker's value against its reference interval/value.
                3. Create a list of markers that fall outside their normal ranges.
                4. For each abnormal marker, note:
                   a. The marker name
                   b. It's result value
                   c. it's unit
                   d. Its reference range
                   e. Whether it's high or low
                5. Format the output as a JSON structure.

        """
            ),
            agent=agent,
            expected_output="",
            context=context
        )
    
    def analyze_blood_test(self, agent, context):
        return Task(
            description=dedent(
                f"""
            **Task**: Analyze The Abnormal Health Markers
            **Description**: Interpret the abnormal health markers and their implications from the json file. Follow these steps:
                1. List all abnormal test markers, their values and their reference interval/values in the data.
                2. Determine potential health implications for abnormal markers depending where they are higher or lower than reference interval.
                3. Summarize overall health status based on the results.

        """
            ),
            agent=agent,
            expected_output="A detailed analysis of blood test results, highlighting key health markers and their implications",
            context=context
        )

    def search_articles(self, agent, context):
        return Task(
            description=dedent(
                f"""
            **Task**: Find Relevant Medical Articles
            **Description**: Search for and compile relevant, reputable medical articles related to the identified health markers. Follow these steps:
                1. For each identified health marker which is not in reference interval:
                    a. Formulate relevant search queries based on the analysis of the respective health marker.
                    b. Use search tools to find medical articles from reputable sources.
                    c. Parse the JSON results returned by the search tool.
                    d. Review article summaries for relevance and credibility.
                2. Select the most relevant and informative articles for each health marker.
                3. Compile a list of articles with brief summaries and URLs.
            
        """
            ),
            agent=agent,
            expected_output="A curated list of relevant medical articles for each significant health marker, including summaries and links",
            context=context
        )

    def health_recommendations(self, agent, context):
        return Task(
            description=dedent(
                f"""
            **Task**: Create Personalized Health Recommendations
            **Description**: **Task**: Create Personalized Health Recommendations
                **Description**: Develop comprehensive and personalized health recommendations based on the abnormal health markers, their analysis, and the relevant medical articles. Follow these steps:

                1. Review the following inputs:
                   a. List of abnormal health markers and their values
                   b. Analysis of each abnormal marker's implications
                   c. Relevant medical articles for each marker
                2. For each abnormal health marker:
                   a. Summarize the marker's current status (how far from the reference range)
                   b. Explain potential health implications based on the analysis
                   c. Formulate specific, actionable recommendations, including:
                      - Dietary changes
                      - Exercise suggestions
                      - Lifestyle modifications
                      - Potential supplements (with appropriate disclaimers)
                   d. Support each recommendation with insights from the relevant medical articles
                   e. Suggest follow-up tests or consultations if necessary
                3. Prioritize recommendations based on the severity and potential impact of each abnormal marker
                4. Organize recommendations in a clear, easy-to-understand format:
                   a. Executive summary of key findings and top priorities
                   b. Detailed recommendations for each abnormal marker
                   c. General health and lifestyle advice
                   d. Suggested timeline for implementing changes and follow-up
                5. Include disclaimers about:
                   a. Consulting healthcare providers before making significant changes
                   b. The recommendations being based on the provided blood test results and general research, not a complete medical history
                6. Provide a list of references to the medical articles used, allowing for further reading

                IMPORTANT: Ensure each recommendation is directly tied to the specific abnormal markers found in the individual's blood test and the analysis provided. Avoid generic advice not related to the actual test results.

        """
            ),
            agent=agent,
            expected_output="A comprehensive health recommendation report including personalized advice for each significant health marker, links to relevant medical articles, and general health recommendations",
            context=context,
            output_file='outputs/result.md'
        )
