import json
import os

import requests
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

class SearchTools():

  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet
    about a a given topic and return relevant results"""
    top_result_to_return = 10
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # check if there is an organic key
    if 'organic' not in response.json():
      return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
    else:
      results = response.json()['organic']
      string = []
      for result in results[:top_result_to_return]:
        try:
          string.append('\n'.join([
              f"Title: {result['title']}", f"Link: {result['link']}",
              f"Snippet: {result['snippet']}", "\n-----------------"
          ]))
        except KeyError:
          next

      return '\n'.join(string)


  @tool("Search github content")
  def search_github(query):
    """Useful to search github for a given query"""
    max_project_to_return = 5
    token = os.environ['GITHUB_TOKEN']
    headers = {
        'Authorization' : f'token {token}'
    } if token else {}

    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      data = response.json()
      projects = []
      for item in data['items'][:max_project_to_return]:
        try:
          name = item['name']
          description = item['description'] or "No description provided"
          projects.append('\n'.join([f"Project Name:{name}", f"Project Desc: {description}"]))
        except KeyError:
          next

      return '\n'.join(projects)
    else:
      return "failed to fetch github projects"
        