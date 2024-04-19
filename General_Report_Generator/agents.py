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
        self.OpenAIGPT35_dot9 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
        self.OpenAIGPT35_dot7 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)
        self.GoogleGemini = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.7)
        self.Ollama = Ollama(model="openhermes")
    
    def topic_investigator(self) -> Agent:
        return Agent(
            role="Topic Investigator (Dr. Anya Petrova)",
            backstory=dedent(f"""
                Dr. Petrova holds a Ph.D. in Information Science and has over 15 years 
                of experience as a research librarian and information specialist. She possesses 
                extensive knowledge of various research methodologies and databases, with 
                a keen eye for identifying relevant and credible sources. Dr. Petrova is skilled 
                at synthesizing complex information and formulating clear research questions.
                """),
            goal=dedent(f"""
                Lay the groundwork for a comprehensive research report by analyzing the provided 
                topic and primary goal, then identifying key areas for investigation.
                """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet, 
                SearchTools.search_github], 
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35_dot7
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )

    def evidence_getherer(self) -> Agent:
        return Agent(
            role="Evidence Gatherer (Dr. Wei Chen)",
            backstory=dedent(f"""
                Dr. Chen is a seasoned research scientist with a Ph.D. in Data Science and 
                over 10 years of experience in data analysis and information retrieval. He possesses 
                expertise in various data mining techniques, statistical analysis methods, and academic 
                research databases. Dr. Chen is skilled at critically evaluating sources and extracting 
                key insights from complex data.
                """),
            goal=dedent(f"""
                Gather and analyze evidence to answer the research questions posed by Dr. Petrova, 
                providing a strong foundation for report synthesis.
                """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet,
                SearchTools.search_github, 
                CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35_dot7
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )
    def data_analyst(self) -> Agent:
        return Agent(
            role="Data Analyst (Dr. David Kim)",
            backstory=dedent(f"""
                Dr. Kim is a skilled data analyst with a Ph.D. in Statistics and over 8 years of 
                experience in data interpretation and visualization. He possesses expertise in various 
                statistical modeling techniques and data visualization tools, enabling him to identify 
                trends, patterns, and key insights from complex datasets.
                """),
            goal=dedent(f"""
                Analyze and interpret the data gathered by Dr. Chen, translating it into clear and 
                actionable insights for report synthesis.
                """),
            #TODO: Add more tools
            tools=[SearchTools.search_internet,
                SearchTools.search_github,
                CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35_dot7
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )
    
    def report_synthesizer(self):
        return Agent(
            role="Report Synthesizer (Dr. Maya Singh)",
            backstory=dedent(f"""
                Dr. Singh is an accomplished scientific writer and editor with a Ph.D. in English Literature 
                and over 12 years of experience in crafting compelling narratives from complex research findings. 
                She possesses a deep understanding of scientific communication principles and excels at translating 
                research into clear and engaging prose.
                """),
            goal=dedent(f""" 
                Transform the research findings into a structured, comprehensive, and well-written research report.
                """),
            #TODO: Add more tools
            #tools=[SearchTools.search_internet],    
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35_dot7
            #llm=self.OpenAIGPT4
            #llm=self.GoogleGemini
        )