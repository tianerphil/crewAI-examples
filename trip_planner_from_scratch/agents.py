import os
from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from mytools.search_tools import SearchTools
from mytools.calculator_tools import CalculatorTools
from dotenv import load_dotenv
load_dotenv()

"""
Notes:
- Agents should be result driven and should have a clear goal.
- Role is their job title or position.
- Goal should be actionable and measurable.
- Backstory should be their resume.
"""
# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.GoogleGemini = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=1.0)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics.
                             I have decades of experience in making travel plans for clients."""),
            goal=dedent(f"""create a 7-day travel itinerary with detailed per day plan,
                        including budget, accommodation, and activities, packing suggestions, and safty tips"""),
            tools=[SearchTools.search_internet, 
                   CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.GoogleGemini
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing and selecting cities for travel."""),
            goal=dedent(f"""Select the best cities based on weather, season, price, and activities for a 7-day trip"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.GoogleGemini
        )
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Konwledgeable about local culture, history, and attractions.
                             extensive experience in guiding tourists and travelers.
                             very familiar with the local area, the attractions, and customs."""),
            goal=dedent(f"""Provide best insights, tips, and recommendations about the selected city"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.GoogleGemini
        )
