import os
import json
import requests
from langchain.tools import tool

session = requests.Session()
session.timeout = 60

class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """
        Useful to search the internet about a
        given topic and return relevant results
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        
        if 'organic' not in response.json():
            return json.dumps({"error": "Sorry, I couldn't find anything about that, there could be an error with your serper api"})
        else:
            results = response.json()['organic']
            formatted_results = []
            for result in results[:top_result_to_return]:
                try:
                    formatted_results.append({
                        "title": result['title'],
                        "link": result['link'],
                        "snippet": result['snippet']
                    })
                except KeyError:
                    continue
            return json.dumps({"results": formatted_results})