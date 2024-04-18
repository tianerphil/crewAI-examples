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
class ResearchAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)
        self.GoogleGemini = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def technical_writer(self):
        return Agent(
            role="technical writer",
            backstory=dedent(f"""A skilled communicator with a background in technology and a talent for 
                             translating complex information into clear, concise, and engaging narratives.
                             """),
            goal=dedent(f""" 
                        To synthesize the findings from the Visionary Director, Technical Architect, 
                        and Audience Advocate into a comprehensive and cohesive report.
                        To effectively communicate the potential of realistic avatar technology for 
                        online streaming to a broad audience, including stakeholders, investors, and the general public.
                        To document the entire research process and findings in a clear and organized manner 
                        for future reference and development efforts.
                        """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet,
                   SearchTools.search_github],    
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )
    
    def vision_director(self):
        return Agent(
            role="AI Technology Vision Director",
            backstory=dedent(f"""A veteran AI technology director with a passion for pushing technological 
                             boundaries and exploring new forms of storytelling. Believes avatars can 
                             revolutionize entertainment and communication."""),
            goal=dedent(f""" 
                        To identify the cutting-edge technologies enabling highly realistic avatar creation.
                        To understand the potential applications and limitations of these technologies.
                        To envision the future of interactive entertainment using realistic avatars.
                        """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet, 
                   SearchTools.search_github, 
                   CalculatorTools.calculate], 
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )

    def technical_architect(self):
        return Agent(
            role="Technical Architect",
            backstory=dedent(f"""A skilled software engineer with expertise in computer graphics, 
                             machine learning, and real-time systems. Fascinated by the intersection 
                             of AI and human-computer interaction."""),
            goal=dedent(f"""
                        To evaluate the technical feasibility of building a realistic, interactive 
                        avatar for live streaming. 
                        To assess the computational resources and infrastructure 
                        required for such a system. 
                        To identify potential technical hurdles and propose solutions.
                        """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet,
                   SearchTools.search_github, 
                   CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )
    def audience_advocate(self):
        return Agent(
            role="The Audience Advocate",
            backstory=dedent(f"""A social media influencer and content creator with a large and engaged 
                             online audience. Passionate about building genuine connections and fostering 
                             interactive communities."""),
            goal=dedent(f"""
                        To understand the audience's expectations and desires regarding realistic 
                        avatars in live streaming.
                        To identify potential ethical concerns and social implications of using such technology. 
                        To ensure the avatar experience is engaging, inclusive, and respectful of user privacy.
                        """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet,
                   SearchTools.search_github],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )
    

